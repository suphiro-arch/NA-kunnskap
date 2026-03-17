from __future__ import annotations

import json
import re
import unicodedata
from collections import defaultdict
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
CAPABILITIES_FILE = REPO_ROOT / 'arkitektur' / 'kapabiliteter' / 'capabilities.yaml'
PRODUCTS_DIR = REPO_ROOT / 'results' / 'Produktbeskrivelser'
OUT_FILE = REPO_ROOT / 'arkitektur' / 'kapabiliteter' / 'produkt-kapabilitet-koblinger.json'
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
    return slugify(value.replace(':', ' '))


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


def parse_capabilities_yaml(path: Path) -> list[dict]:
    lines = read_text(path).splitlines()
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
                        'beskrivelse': '',
                        'slug': '',
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
                            capability['slug'] = slugify(capability['navn'])
                            continue
                        if line.startswith('      beskrivelse:'):
                            capability['beskrivelse'], i = parse_scalar(lines, i, 6)
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
                                        'slug': '',
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
                                            subcap['slug'] = slugify(subcap['navn'])
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
    return capabilities


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


def build_mapping() -> dict:
    capabilities = parse_capabilities_yaml(CAPABILITIES_FILE)
    capability_lookup = {normalize_name(cap['navn']): cap for cap in capabilities}
    subcap_lookup: dict[str, tuple[dict, dict]] = {}
    capability_entries: dict[str, dict] = {}
    subcap_entries: dict[str, dict] = {}

    for cap in capabilities:
        capability_entries[cap['id']] = {
            'capability_id': cap['id'],
            'capability_name': cap['navn'],
            'capability_slug': cap['slug'],
            'description': cap['beskrivelse'],
            'products': [],
            'subcapabilities': [],
        }
        for sub in cap['delkapabiliteter']:
            subcap_lookup[normalize_name(sub['navn'])] = (cap, sub)
            subcap_entry = {
                'subcapability_id': sub['id'],
                'subcapability_name': sub['navn'],
                'subcapability_slug': sub['slug'],
                'description': sub['beskrivelse'],
                'products': [],
            }
            capability_entries[cap['id']]['subcapabilities'].append(subcap_entry)
            subcap_entries[sub['id']] = subcap_entry

    products_out = []

    for product in latest_product_files():
        markdown = read_text(product['path'])
        display_name = extract_display_name(markdown, product['name'])
        section = extract_section(markdown, 'Kapabiliteter')
        product_entry = {
            'product_id': product['id'],
            'product_name': display_name,
            'version': product['version'],
            'author': product['author'],
            'relative_path': product['relative_path'],
            'product_url': f"{REPO_BLOB_BASE}/{product['relative_path']}",
            'capabilities': [],
        }

        if section:
            for raw_line in section.splitlines():
                line = raw_line.strip()
                if not line.startswith('- '):
                    continue
                match = BOLD_BULLET_PATTERN.match(line)
                if not match:
                    continue
                label = match.group(1).strip()
                explanation = (match.group(2) or '').strip().lstrip('–- ').rstrip('.')
                label_parts = [part.strip() for part in label.split(':', 1)]

                mapped_capability = None
                mapped_subcap = None
                if len(label_parts) == 2:
                    main_key = normalize_name(label_parts[0])
                    sub_key = normalize_name(label_parts[1])
                    mapped_capability = capability_lookup.get(main_key)
                    if sub_key in subcap_lookup:
                        mapped_capability, mapped_subcap = subcap_lookup[sub_key]
                else:
                    key = normalize_name(label)
                    mapped_capability = capability_lookup.get(key)
                    if key in subcap_lookup:
                        mapped_capability, mapped_subcap = subcap_lookup[key]

                if not mapped_capability:
                    continue

                mapping = {
                    'capability_id': mapped_capability['id'],
                    'capability_name': mapped_capability['navn'],
                    'capability_slug': mapped_capability['slug'],
                    'subcapability_id': mapped_subcap['id'] if mapped_subcap else '',
                    'subcapability_name': mapped_subcap['navn'] if mapped_subcap else '',
                    'subcapability_slug': mapped_subcap['slug'] if mapped_subcap else '',
                    'mapping_label': label,
                    'explanation': explanation,
                }
                product_entry['capabilities'].append(mapping)

                capability_product_entry = {
                    'product_id': product['id'],
                    'product_name': display_name,
                    'version': product['version'],
                    'author': product['author'],
                    'relative_path': product['relative_path'],
                    'product_url': f"{REPO_BLOB_BASE}/{product['relative_path']}",
                    'mapping_label': label,
                    'explanation': explanation,
                    'subcapability_id': mapping['subcapability_id'],
                    'subcapability_name': mapping['subcapability_name'],
                    'subcapability_slug': mapping['subcapability_slug'],
                }
                capability_entries[mapped_capability['id']]['products'].append(capability_product_entry)
                if mapped_subcap:
                    subcap_entries[mapped_subcap['id']]['products'].append(capability_product_entry)

        products_out.append(product_entry)

    for product in products_out:
        product['capabilities'].sort(key=lambda item: (item['capability_name'], item['subcapability_name']))
    for cap in capability_entries.values():
        cap['products'].sort(key=lambda item: (item['product_id'], item['subcapability_name'], item['product_name']))
        for sub in cap['subcapabilities']:
            sub['products'].sort(key=lambda item: (item['product_id'], item['product_name']))

    return {
        'generated_at': date.today().isoformat(),
        'source': 'latest-productbeskrivelser',
        'products': products_out,
        'capabilities': list(capability_entries.values()),
    }


def main() -> None:
    mapping = build_mapping()
    OUT_FILE.write_text(json.dumps(mapping, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"Genererte masterfil for produkt-kapabilitet-koblinger: {len(mapping['products'])} produkter")


if __name__ == '__main__':
    main()
