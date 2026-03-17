from __future__ import annotations

import json
import re
import shutil
import unicodedata
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
CAPABILITIES_FILE = REPO_ROOT / 'arkitektur' / 'kapabiliteter' / 'capabilities.yaml'
MAP_FILE = REPO_ROOT / 'arkitektur' / 'kapabiliteter' / 'produkt-kapabilitet-koblinger.json'
PRODUCTS_DIR = REPO_ROOT / 'results' / 'Produktbeskrivelser'
OUT_DIR = REPO_ROOT / 'web' / 'hugo-prototype' / 'content' / 'kapabiliteter'
REPO_BLOB_BASE = 'https://github.com/suphiro-arch/NA-kunnskap/blob/main'

CURRENT_PATTERN = re.compile(r'^(?P<id>\d+)-(?P<name>.+)-produkt-canvas-v(?P<ver>\d+)-(?P<author>[^.]+)\.md$')
NO_AUTHOR_PATTERN = re.compile(r'^(?P<id>\d+)-(?P<name>.+)-produkt-canvas-v(?P<ver>\d+)\.md$')
LEGACY_PATTERN = re.compile(r'^(?P<id>\d+)-(?P<name>.+)-produkt-canvas(?:-(?P<author>[^.]+))?\.md$')
SECTION_PATTERN = re.compile(r'^##\s+(.+?)\s*$')
BOLD_BULLET_PATTERN = re.compile(r'^-\s+\*\*(.+?)\*\*(?:\s*(?:[–-]\s*)?(.+))?$')


def read_text(path: Path) -> str:
    text = path.read_text(encoding='utf-8')
    suspicious = text.count('Ã') + text.count('â') + text.count('�')
    if suspicious:
        try:
            fixed = text.encode('latin-1').decode('utf-8')
            fixed_suspicious = fixed.count('Ã') + fixed.count('â') + fixed.count('�')
            if fixed_suspicious < suspicious:
                return fixed
        except Exception:
            pass
    return text


def slugify(value: str) -> str:
    value = value.strip().lower()
    translit = (
        ('æ', 'ae'), ('ø', 'o'), ('å', 'a'),
        ('é', 'e'), ('è', 'e'), ('ê', 'e'),
        ('ä', 'a'), ('ö', 'o'), ('ü', 'u')
    )
    for src, dest in translit:
        value = value.replace(src, dest)
    value = unicodedata.normalize('NFKD', value)
    value = ''.join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(r'[^a-z0-9]+', '-', value)
    return value.strip('-') or 'item'


def normalize_name(value: str) -> str:
    value = value.replace('–', '-').replace('—', '-')
    value = value.replace('**', '').replace('`', '')
    value = value.replace('(', ' ').replace(')', ' ')
    value = slugify(value.replace(':', ' '))
    return value


def markdown_escape(text: str) -> str:
    return text.replace('|', '\\|').replace('\n', ' ').strip()


def parse_scalar(lines: list[str], index: int, field_indent: int) -> tuple[str, int]:
    line = lines[index]
    _, raw_value = line.split(':', 1)
    value = raw_value.strip()
    if value == '>':
        parts: list[str] = []
        index += 1
        while index < len(lines):
            current = lines[index]
            if not current.strip():
                index += 1
                continue
            indent = len(current) - len(current.lstrip(' '))
            if indent <= field_indent:
                break
            parts.append(current.strip())
            index += 1
        return ' '.join(parts).strip(), index
    if value.startswith('"') and value.endswith('"') and len(value) >= 2:
        value = value[1:-1]
    return value.strip(), index + 1


def parse_capabilities_yaml(path: Path) -> tuple[list[dict], dict[str, str], dict[str, list[dict]]]:
    lines = read_text(path).splitlines()

    principles: dict[str, str] = {}
    principle_reason_map: dict[str, list[dict]] = defaultdict(list)

    # Top-level principles names
    for idx, line in enumerate(lines):
        if line.strip() == 'prinsipper:' and not line.startswith(' '):
            i = idx + 1
            while i < len(lines):
                if re.match(r'^[A-Za-z_]+:', lines[i]):
                    break
                if lines[i].startswith('  - id:'):
                    principle_id = lines[i].split(':', 1)[1].strip()
                    i += 1
                    name = ''
                    while i < len(lines) and not lines[i].startswith('  - id:') and not re.match(r'^[A-Za-z_]+:', lines[i]):
                        if lines[i].startswith('    navn:'):
                            name, i = parse_scalar(lines, i, 4)
                            continue
                        i += 1
                    principles[principle_id] = name
                    continue
                i += 1
            break

    capabilities: list[dict] = []
    i = 0
    while i < len(lines):
        if lines[i].strip() == 'kapabiliteter:' and lines[i].startswith('  '):
            i += 1
            while i < len(lines):
                if not lines[i].startswith('    ') and lines[i].strip():
                    break
                if lines[i].startswith('    - id:'):
                    capability = {
                        'id': lines[i].split(':', 1)[1].strip(),
                        'navn': '',
                        'ikon': '',
                        'beskrivelse': '',
                        'prinsipper': [],
                        'delkapabiliteter': [],
                    }
                    i += 1
                    while i < len(lines):
                        line = lines[i]
                        if line.startswith('    - id:'):
                            break
                        if not line.strip() or line.lstrip().startswith('#'):
                            i += 1
                            continue
                        if line.startswith('      navn:'):
                            capability['navn'], i = parse_scalar(lines, i, 6)
                            continue
                        if line.startswith('      ikon:'):
                            capability['ikon'], i = parse_scalar(lines, i, 6)
                            continue
                        if line.startswith('      beskrivelse:'):
                            capability['beskrivelse'], i = parse_scalar(lines, i, 6)
                            continue
                        if line.startswith('      prinsipper:'):
                            i += 1
                            while i < len(lines):
                                current = lines[i]
                                if current.startswith('      delkapabiliteter:') or current.startswith('      navn:') or current.startswith('      ikon:') or current.startswith('      beskrivelse:') or current.startswith('    - id:'):
                                    break
                                if current.startswith('        - '):
                                    capability['prinsipper'].append(current.split('-', 1)[1].strip().split()[0])
                                i += 1
                            continue
                        if line.startswith('      delkapabiliteter:'):
                            i += 1
                            while i < len(lines):
                                current = lines[i]
                                if current.startswith('    - id:') or (current.startswith('      ') and not current.startswith('        ')):
                                    break
                                if current.startswith('        - id:'):
                                    subcap = {
                                        'id': current.split(':', 1)[1].strip(),
                                        'navn': '',
                                        'beskrivelse': '',
                                    }
                                    i += 1
                                    while i < len(lines):
                                        subline = lines[i]
                                        if subline.startswith('        - id:') or subline.startswith('    - id:') or (subline.startswith('      ') and not subline.startswith('        ')):
                                            break
                                        if not subline.strip() or subline.lstrip().startswith('#'):
                                            i += 1
                                            continue
                                        if subline.startswith('          navn:'):
                                            subcap['navn'], i = parse_scalar(lines, i, 10)
                                            continue
                                        if subline.startswith('          beskrivelse:'):
                                            subcap['beskrivelse'], i = parse_scalar(lines, i, 10)
                                            continue
                                        i += 1
                                    capability['delkapabiliteter'].append(subcap)
                                    continue
                                i += 1
                            continue
                        i += 1
                    capabilities.append(capability)
                    continue
                i += 1
        i += 1

    # Principle-capability reasons
    for idx, line in enumerate(lines):
        if line.strip() == 'prinsipp_kapabilitet_koblinger:' and not line.startswith(' '):
            i = idx + 1
            while i < len(lines):
                if lines[i].startswith('  - prinsipp_id:'):
                    principle_id = lines[i].split(':', 1)[1].strip().split()[0]
                    i += 1
                    while i < len(lines):
                        if lines[i].startswith('  - prinsipp_id:'):
                            break
                        if lines[i].startswith('      - kapabilitet_id:'):
                            capability_id = lines[i].split(':', 1)[1].strip().split()[0]
                            i += 1
                            reason = ''
                            while i < len(lines):
                                if lines[i].startswith('      - kapabilitet_id:') or lines[i].startswith('  - prinsipp_id:'):
                                    break
                                if lines[i].startswith('        begrunnelse:'):
                                    reason, i = parse_scalar(lines, i, 8)
                                    continue
                                i += 1
                            principle_reason_map[capability_id].append({
                                'principle_id': principle_id,
                                'principle_name': principles.get(principle_id, principle_id),
                                'reason': reason,
                            })
                            continue
                        i += 1
                    continue
                i += 1
            break

    return capabilities, principles, principle_reason_map


def extract_section(markdown: str, heading: str) -> str:
    lines = markdown.splitlines()
    start = None
    for idx, line in enumerate(lines):
        if line.strip() == f'## {heading}':
            start = idx + 1
            break
    if start is None:
        return ''
    end = len(lines)
    for idx in range(start, len(lines)):
        if SECTION_PATTERN.match(lines[idx]):
            end = idx
            break
    return '\n'.join(lines[start:end]).strip()


def first_nonempty_line(text: str) -> str:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return ''


def latest_product_files() -> list[dict]:
    items: list[dict] = []
    for path in PRODUCTS_DIR.glob('*.md'):
        match = CURRENT_PATTERN.match(path.name)
        if match:
            items.append({
                'id': int(match.group('id')),
                'name': match.group('name'),
                'version': int(match.group('ver')),
                'author': match.group('author'),
                'path': path,
                'relative_path': path.relative_to(REPO_ROOT).as_posix(),
                'filename': path.name,
            })
            continue
        match = NO_AUTHOR_PATTERN.match(path.name)
        if match:
            items.append({
                'id': int(match.group('id')),
                'name': match.group('name'),
                'version': int(match.group('ver')),
                'author': 'ukjent',
                'path': path,
                'relative_path': path.relative_to(REPO_ROOT).as_posix(),
                'filename': path.name,
            })
            continue
        match = LEGACY_PATTERN.match(path.name)
        if match:
            items.append({
                'id': int(match.group('id')),
                'name': match.group('name'),
                'version': 0,
                'author': match.group('author') or 'legacy',
                'path': path,
                'relative_path': path.relative_to(REPO_ROOT).as_posix(),
                'filename': path.name,
            })

    latest_by_id: dict[int, dict] = {}
    for item in items:
        current = latest_by_id.get(item['id'])
        if current is None:
            latest_by_id[item['id']] = item
            continue
        key = (item['version'], item['path'].stat().st_mtime, item['filename'])
        current_key = (current['version'], current['path'].stat().st_mtime, current['filename'])
        if key > current_key:
            latest_by_id[item['id']] = item
    return [latest_by_id[key] for key in sorted(latest_by_id)]


def extract_display_name(markdown: str, fallback: str) -> str:
    section = extract_section(markdown, 'Navn')
    name = first_nonempty_line(section)
    return name or fallback.replace('-', ' ')


def parse_product_capability_mappings(capabilities: list[dict]) -> tuple[dict[str, list[dict]], dict[str, list[dict]]]:
    capability_products: dict[str, list[dict]] = defaultdict(list)
    subcap_products: dict[str, list[dict]] = defaultdict(list)

    mapping = json.loads(MAP_FILE.read_text(encoding='utf-8'))
    for capability in mapping['capabilities']:
        for product in capability.get('products', []):
            capability_products[capability['capability_id']].append({
                'product_id': product['product_id'],
                'product_name': product['product_name'],
                'version': product['version'],
                'author': product['author'],
                'relative_path': product['relative_path'],
                'product_url': product['product_url'],
                'mapping_label': product['mapping_label'],
                'explanation': product['explanation'],
                'subcap_name': product.get('subcapability_name', ''),
            })
        for subcap in capability.get('subcapabilities', []):
            for product in subcap.get('products', []):
                subcap_products[subcap['subcapability_id']].append({
                    'product_id': product['product_id'],
                    'product_name': product['product_name'],
                    'version': product['version'],
                    'author': product['author'],
                    'relative_path': product['relative_path'],
                    'product_url': product['product_url'],
                    'mapping_label': product['mapping_label'],
                    'explanation': product['explanation'],
                    'subcap_name': product.get('subcapability_name', ''),
                })

    for entries in capability_products.values():
        entries.sort(key=lambda item: (item['product_id'], item['subcap_name'], item['product_name']))
    for entries in subcap_products.values():
        entries.sort(key=lambda item: (item['product_id'], item['product_name']))

    return capability_products, subcap_products


def table_or_message(headers: list[str], rows: list[list[str]], empty_message: str) -> str:
    if not rows:
        return empty_message
    lines = [
        '| ' + ' | '.join(headers) + ' |',
        '| ' + ' | '.join(['---'] * len(headers)) + ' |',
    ]
    for row in rows:
        lines.append('| ' + ' | '.join(markdown_escape(cell) for cell in row) + ' |')
    return '\n'.join(lines)


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + '\n', encoding='utf-8')


def indent_block(text: str, spaces: int = 2) -> str:
    prefix = ' ' * spaces
    return '\n'.join(prefix + line if line else prefix for line in text.splitlines())


def generate() -> None:
    capabilities, _, _ = parse_capabilities_yaml(CAPABILITIES_FILE)
    capability_products, subcap_products = parse_product_capability_mappings(capabilities)

    if OUT_DIR.exists():
        for child in OUT_DIR.iterdir():
            if child.is_dir():
                shutil.rmtree(child)
            else:
                child.unlink()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for index, capability in enumerate(capabilities, start=1):
        cap_slug = slugify(capability['navn'])
        cap_dir = OUT_DIR / cap_slug
        products = capability_products.get(capability['id'], [])
        subcaps = capability['delkapabiliteter']
        card_meta = f"{len(subcaps)} delkapabiliteter / {len({entry['product_id'] for entry in products})} produkter"

        for sub_index, subcap in enumerate(subcaps, start=1):
            sub_slug = slugify(subcap['navn'])
            sub_products = subcap_products.get(subcap['id'], [])

            sub_product_rows = []
            for entry in sub_products:
                sub_product_rows.append([
                    entry['product_name'],
                    f"[v{entry['version']} ({entry['author']})]({entry['product_url']})" if entry['version'] > 0 else f"[legacy]({entry['product_url']})",
                    entry['explanation'] or 'Produktet er eksplisitt koblet til denne delkapabiliteten i produktbeskrivelsen.',
                ])

            sub_content = f"""
---
title: "{subcap['navn']}"
weight: {sub_index}
description: "{subcap['beskrivelse']}"
cardMeta: "{len({entry['product_id'] for entry in sub_products})} produkter"
---

{subcap['beskrivelse']}

## Hører til

Denne delkapabiliteten er en del av [{capability['navn']}](../).

## Relaterte produkter

{table_or_message(['Produkt', 'Produktbeskrivelse', 'Hvorfor relevant'], sub_product_rows, 'Ingen produkter er koblet til denne delkapabiliteten foreløpig.')}
"""
            write_file(cap_dir / sub_slug / '_index.md', sub_content)

        product_rows = []
        for entry in products:
            mapping_name = entry['subcap_name'] or capability['navn']
            product_rows.append([
                entry['product_name'],
                f"[v{entry['version']} ({entry['author']})]({entry['product_url']})" if entry['version'] > 0 else f"[legacy]({entry['product_url']})",
                mapping_name,
                entry['explanation'] or 'Produktet er eksplisitt koblet til denne kapabiliteten i produktbeskrivelsen.',
            ])

        products_markdown = (
            "## Relaterte produkter\n\n"
            + table_or_message(
                ['Produkt', 'Produktbeskrivelse', 'Koblet via', 'Hvorfor relevant'],
                product_rows,
                'Ingen produkter er koblet til denne kapabiliteten foreløpig.',
            )
        )

        capability_content = f"""
---
title: "{capability['navn']}"
weight: {index}
description: "{capability['beskrivelse']}"
cardMeta: "{card_meta}"
productsMarkdown: |
{indent_block(products_markdown.strip(), 2)}
---

{capability['beskrivelse']}
"""
        write_file(cap_dir / '_index.md', capability_content)

    top_content = f"""
---
title: "Kapabiliteter"
weight: 10
description: "Oversikt over hovedkapabiliteter, delkapabiliteter og hvilke produkter som støtter dem."
---

Kapabilitetene beskriver hvilke evner som må være på plass for å utvikle, forvalte og videreutvikle et nasjonalt økosystem for digital samhandling. I denne prototypen er de organisert som en navigerbar struktur: først hovedkapabiliteter, deretter delkapabiliteter og til slutt koblinger videre til relevante produkter.

- Velg en hovedkapabilitet for å åpne beskrivelse og delkapabiliteter.
- Gå videre til delkapabiliteter for å se mer avgrensede evner.
- Bruk produktoversikten nederst på kapabilitetssidene for å finne relevante fellesløsninger.
"""
    write_file(OUT_DIR / '_index.md', top_content)

    print(f'Genererte kapabilitetssider: {len(capabilities)} hovedkapabiliteter')


if __name__ == '__main__':
    generate()
