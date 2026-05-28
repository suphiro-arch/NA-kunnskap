from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTER_FILE = REPO_ROOT / "arkitektur" / "ressurser" / "produktnummerering.md"
MAP_FILE = REPO_ROOT / "arkitektur" / "kapabiliteter" / "produkt-kapabilitet-koblinger.yaml"
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


def main() -> int:
    latest = latest_files_by_id()
    findings = check_register(latest)
    findings.extend(check_capability_map(latest))

    if findings:
        print("FEIL: Fant utdaterte versjonsreferanser:")
        for finding in findings:
            print(finding)
        return 1

    print("OK: Register og kapabilitetsmapping peker på siste versjon.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
