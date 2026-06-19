from __future__ import annotations

import json
import importlib.util
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTER_FILE = REPO_ROOT / "arkitektur" / "ressurser" / "produktnummerering.md"
CAPABILITIES_FILE = REPO_ROOT / "arkitektur" / "kapabiliteter" / "capabilities.yaml"
MAP_FILE = REPO_ROOT / "arkitektur" / "kapabiliteter" / "produkt-kapabilitet-koblinger.yaml"
CAPABILITY_WEB_DIR = REPO_ROOT / "web" / "hugo-prototype" / "content" / "kapabiliteter"
CAPABILITY_GENERATOR = REPO_ROOT / "web" / "hugo-prototype" / "scripts" / "generate-capabilities.py"
SOURCE_DIRS = [
    REPO_ROOT / "arkitektur" / "ressurser" / "operative-losninger-og-tjenester",
    REPO_ROOT / "arkitektur" / "ressurser" / "normerende-ressurser",
    REPO_ROOT / "arkitektur" / "ressurser" / "samarbeidsfora",
    REPO_ROOT / "arkitektur" / "ressurser" / "rammer-og-virkemidler",
]

CURRENT_PATTERN = re.compile(r"^(?P<id>\d+)-(?P<name>.+)-v(?P<ver>\d+)-(?P<author>[^.]+)\.md$")
PRODUCT_PATTERN = re.compile(r"^(?P<id>\d+)-(?P<name>.+)-produkt-canvas-v(?P<ver>\d+)-(?P<author>[^.]+)\.md$")
NO_AUTHOR_PATTERN = re.compile(r"^(?P<id>\d+)-(?P<name>.+)-produkt-canvas-v(?P<ver>\d+)\.md$")
LINK_PATTERN = re.compile(r"\((?P<path>[^)]+\.md)\)")
# Legacyressurser som bevisst holdes utenfor operativ oversikt og derfor ikke
# skal kreve aktiv register- eller mappingoppføring i kvalitetsporten.
EXCLUDED_PRODUCT_IDS = {21}


def parse_versioned_file(path: Path) -> dict | None:
    for pattern in (CURRENT_PATTERN, PRODUCT_PATTERN, NO_AUTHOR_PATTERN):
        match = pattern.match(path.name)
        if not match:
            continue
        author = match.groupdict().get("author") or "ukjent"
        return {
            "id": int(match.group("id")),
            "version": int(match.group("ver")),
            "author": author,
            "path": path,
            "relative_path": path.relative_to(REPO_ROOT).as_posix() if path.is_absolute() else path.as_posix(),
            "filename": path.name,
        }
    return None


def latest_files_by_id() -> dict[int, dict]:
    latest: dict[int, dict] = {}
    for source_dir in SOURCE_DIRS:
        if not source_dir.exists():
            continue
        for path in source_dir.glob("*.md"):
            parsed = parse_versioned_file(path)
            if not parsed:
                continue
            current = latest.get(parsed["id"])
            if current is None:
                latest[parsed["id"]] = parsed
                continue
            key = (parsed["version"], path.stat().st_mtime, parsed["filename"])
            current_key = (current["version"], current["path"].stat().st_mtime, current["filename"])
            if key > current_key:
                latest[parsed["id"]] = parsed
    return latest


def check_register(latest: dict[int, dict]) -> list[str]:
    findings: list[str] = []
    for lineno, raw_line in enumerate(REGISTER_FILE.read_text(encoding="utf-8-sig").splitlines(), start=1):
        line = raw_line.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue
        match = LINK_PATTERN.search(line)
        if not match:
            continue
        rel_path = match.group("path")
        resolved = (REGISTER_FILE.parent / Path(rel_path)).resolve()
        normalized = resolved.relative_to(REPO_ROOT).as_posix()
        file_name = Path(rel_path).name
        parsed = parse_versioned_file(Path(file_name))
        if not parsed:
            continue
        latest_entry = latest.get(parsed["id"])
        if not latest_entry:
            continue
        if normalized != latest_entry["relative_path"]:
            findings.append(
                f"{REGISTER_FILE.relative_to(REPO_ROOT)}:{lineno}: "
                f"registeret peker på {normalized}, men siste versjon er {latest_entry['relative_path']}"
            )
    return findings


def check_capability_map(latest: dict[int, dict]) -> list[str]:
    findings: list[str] = []
    data = json.loads(MAP_FILE.read_text(encoding="utf-8-sig"))
    mapped_ids = set()
    for index, product in enumerate(data.get("products", []), start=1):
        product_id = product.get("product_id")
        if product_id in EXCLUDED_PRODUCT_IDS:
            continue
        mapped_ids.add(product_id)
        latest_entry = latest.get(product_id)
        if not latest_entry:
            continue

        relative_path = product.get("relative_path")
        version = product.get("version")
        author = product.get("author")

        if relative_path != latest_entry["relative_path"]:
            findings.append(
                f"{MAP_FILE.relative_to(REPO_ROOT)}: produkt {product_id} peker på {relative_path}, "
                f"men siste versjon er {latest_entry['relative_path']}"
            )
        if version != latest_entry["version"]:
            findings.append(
                f"{MAP_FILE.relative_to(REPO_ROOT)}: produkt {product_id} har version={version}, "
                f"men siste versjon er v{latest_entry['version']}"
            )
        if author != latest_entry["author"]:
            findings.append(
                f"{MAP_FILE.relative_to(REPO_ROOT)}: produkt {product_id} har author={author}, "
                f"men siste versjon bruker {latest_entry['author']}"
            )

    for product_id in sorted(latest):
        if product_id in EXCLUDED_PRODUCT_IDS:
            continue
        if product_id not in mapped_ids:
            findings.append(
                f"{MAP_FILE.relative_to(REPO_ROOT)}: mangler mappingoppføring for produkt {product_id} "
                f"({latest[product_id]['relative_path']})"
            )
    return findings


def load_capability_helpers():
    spec = importlib.util.spec_from_file_location("generate_capabilities", CAPABILITY_GENERATOR)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Kunne ikke laste {CAPABILITY_GENERATOR.relative_to(REPO_ROOT)}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_canonical_capabilities() -> dict:
    helper = load_capability_helpers()
    model = helper.parse_capabilities_yaml(CAPABILITIES_FILE)
    capability_by_slug = {}
    subcapability_by_slug = {}

    for capability in model.get("kapabiliteter", []):
        cap_slug = helper.slugify(capability["navn"])
        capability_by_slug[cap_slug] = capability
        for subcapability in capability.get("delkapabiliteter", []):
            sub_slug = helper.slugify(subcapability["navn"])
            subcapability_by_slug[(cap_slug, sub_slug)] = subcapability

    return {
        "capabilities": capability_by_slug,
        "subcapabilities": subcapability_by_slug,
    }


def walk_dicts(value, location: str = "root"):
    if isinstance(value, dict):
        yield location, value
        for key, child in value.items():
            yield from walk_dicts(child, f"{location}.{key}")
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk_dicts(child, f"{location}[{index}]")


def check_nested_product_references(latest: dict[int, dict]) -> list[str]:
    findings: list[str] = []
    data = json.loads(MAP_FILE.read_text(encoding="utf-8-sig"))

    for location, item in walk_dicts(data):
        if location.startswith("root.products["):
            continue
        if "product_id" not in item or "relative_path" not in item:
            continue

        product_id = item.get("product_id")
        latest_entry = latest.get(product_id)
        if not latest_entry:
            continue

        relative_path = item.get("relative_path")
        version = item.get("version")
        author = item.get("author")

        if (
            relative_path != latest_entry["relative_path"]
            or version != latest_entry["version"]
            or author != latest_entry["author"]
        ):
            findings.append(
                f"{MAP_FILE.relative_to(REPO_ROOT)}: avledet produktreferanse {location} for produkt "
                f"{product_id} peker på v{version} ({author}) {relative_path}, men siste versjon er "
                f"v{latest_entry['version']} ({latest_entry['author']}) {latest_entry['relative_path']}"
            )

    return findings


def check_capability_slugs() -> list[str]:
    findings: list[str] = []
    data = json.loads(MAP_FILE.read_text(encoding="utf-8-sig"))
    canonical = load_canonical_capabilities()
    capability_by_slug = canonical["capabilities"]
    subcapability_by_slug = canonical["subcapabilities"]

    for location, item in walk_dicts(data):
        capability_slug = item.get("capability_slug")
        subcapability_slug = item.get("subcapability_slug")
        if not capability_slug:
            continue

        capability = capability_by_slug.get(capability_slug)
        if not capability:
            findings.append(
                f"{MAP_FILE.relative_to(REPO_ROOT)}: {location} bruker ukjent capability_slug={capability_slug}"
            )
            continue

        if item.get("capability_id") and item.get("capability_id") != capability.get("id"):
            findings.append(
                f"{MAP_FILE.relative_to(REPO_ROOT)}: {location} har capability_id={item.get('capability_id')}, "
                f"men {capability_slug} har id={capability.get('id')}"
            )

        if subcapability_slug:
            subcapability = subcapability_by_slug.get((capability_slug, subcapability_slug))
            if not subcapability:
                findings.append(
                    f"{MAP_FILE.relative_to(REPO_ROOT)}: {location} bruker ukjent "
                    f"subcapability_slug={capability_slug}/{subcapability_slug}"
                )
                continue

            if item.get("subcapability_id") and item.get("subcapability_id") != subcapability.get("id"):
                findings.append(
                    f"{MAP_FILE.relative_to(REPO_ROOT)}: {location} har "
                    f"subcapability_id={item.get('subcapability_id')}, men "
                    f"{capability_slug}/{subcapability_slug} har id={subcapability.get('id')}"
                )

    return findings


def check_generated_capability_pages() -> list[str]:
    findings: list[str] = []
    if not CAPABILITY_WEB_DIR.exists():
        return findings

    canonical = load_canonical_capabilities()
    valid_capability_slugs = set(canonical["capabilities"])
    valid_subcapability_slugs = canonical["subcapabilities"]

    for capability_dir in CAPABILITY_WEB_DIR.iterdir():
        if not capability_dir.is_dir():
            continue
        cap_slug = capability_dir.name
        if cap_slug not in valid_capability_slugs:
            findings.append(
                f"{capability_dir.relative_to(REPO_ROOT)}: generert kapabilitetsside finnes ikke i capabilities.yaml"
            )
            continue

        for subcapability_dir in capability_dir.iterdir():
            if not subcapability_dir.is_dir():
                continue
            sub_slug = subcapability_dir.name
            if (cap_slug, sub_slug) not in valid_subcapability_slugs:
                findings.append(
                    f"{subcapability_dir.relative_to(REPO_ROOT)}: generert delkapabilitetsside finnes ikke i capabilities.yaml"
                )

    return findings


def main() -> int:
    latest = latest_files_by_id()
    findings = check_register(latest)
    findings.extend(check_capability_map(latest))
    findings.extend(check_nested_product_references(latest))
    findings.extend(check_capability_slugs())
    findings.extend(check_generated_capability_pages())

    if findings:
        print("FEIL: Fant utdaterte eller inkonsistente referanser:")
        for finding in findings:
            print(finding)
        return 1

    print("OK: Register, kapabilitetsmapping og genererte kapabilitetssider er synkronisert.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
