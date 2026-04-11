from __future__ import annotations

import html
import json
import re
import unicodedata
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
CAPABILITIES_FILE = REPO_ROOT / 'arkitektur' / 'kapabiliteter' / 'capabilities.yaml'
MAP_FILE = REPO_ROOT / 'arkitektur' / 'kapabiliteter' / 'produkt-kapabilitet-koblinger.yaml'
SOURCE_DIRS = [
    REPO_ROOT / 'arkitektur' / 'ressurser' / 'operative-losninger-og-tjenester',
    REPO_ROOT / 'arkitektur' / 'ressurser' / 'normerende-ressurser',
    REPO_ROOT / 'arkitektur' / 'ressurser' / 'samarbeidsfora',
]
OUT_DIR = REPO_ROOT / 'web' / 'hugo-prototype' / 'content' / 'kapabiliteter'
REPO_BLOB_BASE = 'https://github.com/suphiro-arch/NA-kunnskap/blob/main'

CURRENT_PATTERN = re.compile(r'^(?P<id>\d+)-(?P<name>.+)-produkt-canvas-v(?P<ver>\d+)-(?P<author>[^.]+)\.md$')
NO_AUTHOR_PATTERN = re.compile(r'^(?P<id>\d+)-(?P<name>.+)-produkt-canvas-v(?P<ver>\d+)\.md$')
LEGACY_PATTERN = re.compile(r'^(?P<id>\d+)-(?P<name>.+)-produkt-canvas(?:-(?P<author>[^.]+))?\.md$')
SECTION_PATTERN = re.compile(r'^##\s+(.+?)\s*$')
BOLD_BULLET_PATTERN = re.compile(r'^-\s+\*\*(.+?)\*\*(?:\s*(?:[–-]\s*)?(.+))?$')


def read_text(path: Path) -> str:
    # Use utf-8-sig to transparently handle files saved with UTF-8 BOM.
    text = path.read_text(encoding='utf-8-sig')
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


def parse_capabilities_yaml(path: Path) -> dict:
    lines = read_text(path).splitlines()

    model = {
        'id': '',
        'navn': '',
        'beskrivelse': '',
        'kapabiliteter': [],
    }

    capabilities: list[dict] = []
    i = 0
    while i < len(lines):
        if lines[i].startswith('  id:') and not model['id']:
            model['id'], i = parse_scalar(lines, i, 2)
            continue
        if lines[i].startswith('  navn:') and not model['navn']:
            model['navn'], i = parse_scalar(lines, i, 2)
            continue
        if lines[i].startswith('  beskrivelse:') and not model['beskrivelse']:
            model['beskrivelse'], i = parse_scalar(lines, i, 2)
            continue
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

    model['kapabiliteter'] = capabilities
    return model


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
    for source_dir in SOURCE_DIRS:
        if not source_dir.exists():
            continue
        for path in source_dir.glob('*.md'):
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

    capability_by_slug = {cap['navn'].strip().lower().replace(' ', '-'): cap for cap in capabilities}
    capability_by_name = {cap['navn']: cap for cap in capabilities}
    subcap_lookup: dict[tuple[str, str], dict] = {}
    subcap_name_lookup: dict[tuple[str, str], dict] = {}
    for cap in capabilities:
        for subcap in cap.get('delkapabiliteter', []):
            subcap_slug = slugify(subcap['navn'])
            subcap_lookup[(cap['id'], subcap_slug)] = subcap
            subcap_name_lookup[(cap['id'], subcap['navn'])] = subcap

    mapping = json.loads(MAP_FILE.read_text(encoding='utf-8-sig'))
    for product in mapping.get('products', []):
        for capability in product.get('capabilities', []):
            capability_slug = capability.get('capability_slug') or slugify(capability.get('capability_name', ''))
            canonical_capability = capability_by_slug.get(capability_slug) or capability_by_name.get(capability.get('capability_name', ''))
            if not canonical_capability:
                continue

            subcap_slug = capability.get('subcapability_slug') or slugify(capability.get('subcapability_name', ''))
            canonical_subcap = (
                subcap_lookup.get((canonical_capability['id'], subcap_slug))
                or subcap_name_lookup.get((canonical_capability['id'], capability.get('subcapability_name', '')))
            )

            entry = {
                'product_id': product['product_id'],
                'product_name': product['product_name'],
                'version': product['version'],
                'author': product['author'],
                'relative_path': product['relative_path'],
                'product_url': f"{REPO_BLOB_BASE}/{product['relative_path']}",
                'mapping_label': capability.get('mapping_label', ''),
                'explanation': capability.get('explanation', ''),
                'subcap_name': canonical_subcap['navn'] if canonical_subcap else capability.get('subcapability_name', ''),
            }

            capability_products[canonical_capability['id']].append(entry)
            if canonical_subcap:
                subcap_products[canonical_subcap['id']].append({
                    **entry,
                    'subcap_name': canonical_subcap['navn'],
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


def simplify_capability_relevance(explanations: list[str], via_names: list[str]) -> str:
    cleaned = []
    for explanation in explanations:
        text = explanation.strip()
        if text and text not in cleaned:
            cleaned.append(text)

    if len(via_names) > 1:
        return 'Støtter flere delkapabiliteter i denne hovedkapabiliteten.'
    if cleaned:
        return cleaned[0]
    return 'Produktet er eksplisitt koblet til denne kapabiliteten.'


def classify_resource(relative_path: str) -> tuple[str, str]:
    normalized = relative_path.replace('\\', '/')
    if '/operative-losninger-og-tjenester/' in normalized:
        return 'resource-type--operative', 'Operativ løsning'
    if '/normerende-ressurser/' in normalized:
        return 'resource-type--normative', 'Normerende ressurs'
    if '/samarbeidsfora/' in normalized:
        return 'resource-type--forum', 'Samarbeidsforum'
    return 'resource-type--other', 'Annen ressurs'


def render_product_link_cards(products: list[dict], capability_name: str, *, include_relevance: bool) -> str:
    if not products:
        return '<p>Ingen produkter er koblet til denne kapabiliteten forelopig.</p>'

    grouped: dict[int, dict] = {}

    for entry in products:
        product = grouped.setdefault(entry['product_id'], {
            'product_name': entry['product_name'],
            'product_url': entry['product_url'],
            'via_names': [],
            'explanations': [],
        })

        # Keep subcapability linkage in data for correct grouping and relevance text,
        # even when the UI does not explicitly show "Koblet via".
        via_name = entry['subcap_name'] or capability_name
        if via_name and via_name not in product['via_names']:
            product['via_names'].append(via_name)

        explanation = (entry.get('explanation') or '').strip()
        if explanation and explanation not in product['explanations']:
            product['explanations'].append(explanation)

    parts = ['<div class="capability-product-links">']
    for product_id in sorted(grouped):
        product = grouped[product_id]
        title = html.escape(product['product_name'])
        url = html.escape(product['product_url'])
        relevance = simplify_capability_relevance(product['explanations'], product['via_names'])
        resource_class, resource_label = classify_resource(product['product_url'].replace(f'{REPO_BLOB_BASE}/', ''))

        parts.append(f'  <article class="capability-product-link {resource_class}">')
        parts.append(f'    <p class="capability-product-link__type">{html.escape(resource_label)}</p>')
        parts.append(f'    <h3 class="capability-product-link__title">{title}</h3>')
        if include_relevance and relevance:
            parts.append(f'    <p class="capability-product-link__description">{html.escape(relevance)}</p>')
        parts.append(f'    <a class="resource-card__button resource-card__button--primary" href="{url}">Åpne ressursbeskrivelse</a>')
        parts.append('  </article>')

    parts.append('</div>')
    return '\n'.join(parts)


def aggregate_capability_product_rows(products: list[dict], capability_name: str) -> list[list[str]]:
    grouped: dict[int, dict] = {}

    for entry in products:
        product = grouped.setdefault(entry['product_id'], {
            'product_name': entry['product_name'],
            'version': entry['version'],
            'author': entry['author'],
            'product_url': entry['product_url'],
            'via_names': [],
            'explanations': [],
        })

        via_name = entry['subcap_name'] or capability_name
        if via_name not in product['via_names']:
            product['via_names'].append(via_name)

        explanation = (entry.get('explanation') or '').strip()
        if explanation and explanation not in product['explanations']:
            product['explanations'].append(explanation)

    rows = []
    for product_id in sorted(grouped):
        product = grouped[product_id]
        version_label = (
            f"[v{product['version']} ({product['author']})]({product['product_url']})"
            if product['version'] > 0 else
            f"[legacy]({product['product_url']})"
        )
        rows.append([
            product['product_name'],
            version_label,
            ', '.join(product['via_names']),
            simplify_capability_relevance(product['explanations'], product['via_names']),
        ])
    return rows


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + '\n', encoding='utf-8')


def indent_block(text: str, spaces: int = 2) -> str:
    prefix = ' ' * spaces
    return '\n'.join(prefix + line if line else prefix for line in text.splitlines())


def generate() -> None:
    model = parse_capabilities_yaml(CAPABILITIES_FILE)
    capabilities = model['kapabiliteter']
    capability_products, subcap_products = parse_product_capability_mappings(capabilities)

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
headerTitle: "{capability['navn']} - {subcap['navn']}"
eyebrow: "Kapabilitet"
weight: {sub_index}
description: "{subcap['beskrivelse']}"
cardMeta: "{len({entry['product_id'] for entry in sub_products})} produkter"
---

{subcap['beskrivelse']}

## Relaterte produkter

{render_product_link_cards(sub_products, subcap['navn'], include_relevance=True)}
"""
            write_file(cap_dir / sub_slug / '_index.md', sub_content)

        products_markdown = (
            "## Relaterte produkter\n\n"
            + render_product_link_cards(products, capability['navn'], include_relevance=False)
        )

        capability_content = f"""
---
title: "{capability['navn']}"
eyebrow: "Kapabilitet"
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
eyebrow: "Kapabilitetsmodell"
headerTitle: "{model['navn']}"
weight: 10
description: "Oversikt over hovedkapabiliteter, delkapabiliteter og hvilke produkter som støtter dem."
---

{model['beskrivelse'].replace('\n', ' ')}

- Start med en hovedkapabilitet.
- Gå videre til delkapabiliteter.
- Bruk koblede ressurser for konkrete løsninger og virkemidler.
"""
    write_file(OUT_DIR / '_index.md', top_content)

    print(f'Genererte kapabilitetssider: {len(capabilities)} hovedkapabiliteter')


if __name__ == '__main__':
    generate()

