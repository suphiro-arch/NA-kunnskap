from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
REGISTER_FILE = REPO_ROOT / "arkitektur" / "ressurser" / "produktnummerering.md"
MAP_FILE = REPO_ROOT / "arkitektur" / "kapabiliteter" / "produkt-kapabilitet-koblinger.yaml"
CAPABILITIES_FILE = REPO_ROOT / "arkitektur" / "kapabiliteter" / "capabilities.yaml"
SOURCE_DIRS = [
    REPO_ROOT / "arkitektur" / "ressurser" / "operative-losninger-og-tjenester",
    REPO_ROOT / "arkitektur" / "ressurser" / "normerende-ressurser",
    REPO_ROOT / "arkitektur" / "ressurser" / "samarbeidsfora",
]
REPO_BLOB_BASE = "https://github.com/suphiro-arch/NA-kunnskap/blob/main"

CURRENT_PATTERN = re.compile(r"^(?P<id>\d+)-(?P<name>.+)-produkt-canvas-v(?P<ver>\d+)-(?P<author>[^.]+)\.md$")
RESOURCE_PATTERN = re.compile(r"^(?P<id>\d+)-(?P<name>.+)-v(?P<ver>\d+)-(?P<author>[^.]+)\.md$")
NO_AUTHOR_PATTERN = re.compile(r"^(?P<id>\d+)-(?P<name>.+)-produkt-canvas-v(?P<ver>\d+)\.md$")
LINK_PATTERN = re.compile(r"\((?P<path>[^)]+\.md)\)")
CAP_SECTION_PATTERN = re.compile(r"^##\s+Kapabiliteter\s*$")
BULLET_PATTERN = re.compile(r"^-\s+(?:\*\*)?(?P<label>.+?)(?:\*\*)?(?:\s{2,}.*)?$")


def parse_versioned_file(path: Path) -> dict | None:
    for pattern in (CURRENT_PATTERN, RESOURCE_PATTERN, NO_AUTHOR_PATTERN):
        match = pattern.match(path.name)
        if not match:
            continue
        author = match.groupdict().get("author") or "ukjent"
        return {
            "id": int(match.group("id")),
            "version": int(match.group("ver")),
            "author": author,
            "path": path,
            "relative_path": path.relative_to(REPO_ROOT).as_posix(),
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


def load_capability_catalog() -> tuple[dict[str, dict], dict[str, dict]]:
    text = CAPABILITIES_FILE.read_text(encoding="utf-8-sig")
    main_lookup: dict[str, dict] = {}
    sub_lookup: dict[str, dict] = {}
    current_main: dict | None = None

    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("    - id: "):
            current_main = {"id": line.split(": ", 1)[1].strip()}
            continue
        if current_main is not None and line.startswith("      navn: "):
            current_main["name"] = line.split(": ", 1)[1].strip()
            current_main["slug"] = slugify(current_main["name"])
            main_lookup[current_main["name"]] = current_main.copy()
            continue
        if current_main is not None and line.startswith("        - id: "):
            sub_id = line.split(": ", 1)[1].strip()
            sub_lookup[f"__pending__:{sub_id}"] = {"id": sub_id, "parent": current_main.copy()}
            continue
        if line.startswith("          navn: "):
            name = line.split(": ", 1)[1].strip()
            pending_key = next((k for k in reversed(list(sub_lookup.keys())) if k.startswith("__pending__:")), None)
            if pending_key is None:
                continue
            pending = sub_lookup.pop(pending_key)
            parent = pending["parent"]
            sub_lookup[name] = {
                "id": pending["id"],
                "name": name,
                "slug": slugify(name),
                "parent_id": parent["id"],
                "parent_name": parent["name"],
                "parent_slug": parent["slug"],
            }

    return main_lookup, sub_lookup


def slugify(value: str) -> str:
    value = value.strip().lower()
    translit = (
        ("æ", "ae"), ("ø", "o"), ("å", "a"),
        ("é", "e"), ("è", "e"), ("ê", "e"),
        ("ä", "a"), ("ö", "o"), ("ü", "u"),
    )
    for src, dest in translit:
        value = value.replace(src, dest)
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-")


def parse_register() -> dict[int, dict]:
    rows: dict[int, dict] = {}
    for lineno, raw in enumerate(REGISTER_FILE.read_text(encoding="utf-8-sig").splitlines(), start=1):
        line = raw.strip()
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 6 or not cells[0].isdigit():
            continue
        link = LINK_PATTERN.search(line)
        if not link:
            continue
        relative_doc = (REGISTER_FILE.parent / Path(link.group("path"))).resolve().relative_to(REPO_ROOT).as_posix()
        rows[int(cells[0])] = {
            "row_number": int(cells[0]),
            "resource_id": cells[1].replace("`", "").strip(),
            "product_name": cells[2].replace("`", "").strip(),
            "resource_type": cells[3].replace("`", "").strip(),
            "capability_labels": [part.strip() for part in cells[4].split("<br>") if part.strip() and part.strip() != "-"],
            "relative_path": relative_doc,
            "lineno": lineno,
        }
    return rows


def extract_capabilities_from_markdown(path: Path) -> list[dict]:
    items: list[dict] = []
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    in_section = False
    pending: dict | None = None
    for raw in lines:
        line = raw.rstrip()
        if CAP_SECTION_PATTERN.match(line):
            in_section = True
            continue
        if in_section and line.startswith("## "):
            if pending:
                items.append(pending)
            break
        if not in_section:
            continue
        match = BULLET_PATTERN.match(line.strip())
        if match:
            if pending:
                items.append(pending)
            label = match.group("label").strip()
            pending = {"label": label, "explanation": ""}
            continue
        if pending and line.strip():
            text = line.strip()
            pending["explanation"] = f"{pending['explanation']} {text}".strip()
    if pending:
        items.append(pending)

    normalized: list[dict] = []
    for item in items:
        label = item["label"].replace("**", "").strip()
        explanation = item["explanation"].strip()
        if not label:
            continue
        lookup_label = label.split(":", 1)[1].strip() if ":" in label else label
        normalized.append({"label": lookup_label, "mapping_label": label, "explanation": explanation})
    return normalized


def build_capability_entries(product_name: str, labels: list[dict], main_lookup: dict[str, dict], sub_lookup: dict[str, dict]) -> list[dict]:
    entries: list[dict] = []
    seen: set[tuple[str, str]] = set()

    for item in labels:
        label = item["label"]
        source_explanation = item.get("explanation", "").strip()
        if label in sub_lookup:
            sub = sub_lookup[label]
            key = (sub["parent_name"], sub["name"])
            if key in seen:
                continue
            seen.add(key)
            entries.append(
                {
                    "capability_id": sub["parent_id"],
                    "capability_name": sub["parent_name"],
                    "capability_slug": sub["parent_slug"],
                    "subcapability_id": sub["id"],
                    "subcapability_name": sub["name"],
                    "subcapability_slug": sub["slug"],
                    "mapping_label": f"{sub['parent_name']}: {sub['name']}",
                    "explanation": source_explanation or f"Foreløpig automatisk opprettet kobling for {product_name} basert på register og ressursbeskrivelse. Må kvalitetssikres faglig.",
                }
            )
            continue

        if label in main_lookup:
            main = main_lookup[label]
            key = (main["name"], "")
            if key in seen:
                continue
            seen.add(key)
            entries.append(
                {
                    "capability_id": main["id"],
                    "capability_name": main["name"],
                    "capability_slug": main["slug"],
                    "subcapability_id": "",
                    "subcapability_name": "",
                    "subcapability_slug": "",
                    "mapping_label": main["name"],
                    "explanation": source_explanation or f"Foreløpig automatisk opprettet hovedkapabilitet for {product_name} basert på register og ressursbeskrivelse. Må kvalitetssikres faglig.",
                }
            )

    return entries


def sync(apply_changes: bool) -> int:
    latest = latest_files_by_id()
    register = parse_register()
    main_lookup, sub_lookup = load_capability_catalog()
    data = json.loads(MAP_FILE.read_text(encoding="utf-8-sig"))
    products = data.get("products", [])
    by_id = {item["product_id"]: item for item in products}

    changes: list[str] = []

    for product_id, latest_entry in sorted(latest.items()):
        register_entry = register.get(product_id)
        if register_entry is None:
            continue

        markdown_labels = extract_capabilities_from_markdown(latest_entry["path"])
        label_explanations = {}
        for item in markdown_labels:
            label_explanations[item["mapping_label"]] = item.get("explanation", "").strip()
            if ":" in item["mapping_label"]:
                label_explanations[item["mapping_label"].split(":", 1)[1].strip()] = item.get("explanation", "").strip()

        existing = by_id.get(product_id)
        if existing:
            if existing.get("product_name") != register_entry["product_name"]:
                existing["product_name"] = register_entry["product_name"]
                changes.append(f"Oppdaterte navn for {product_id}")
            if existing.get("version") != latest_entry["version"]:
                existing["version"] = latest_entry["version"]
                changes.append(f"Oppdaterte version for {product_id}")
            if existing.get("author") != latest_entry["author"]:
                existing["author"] = latest_entry["author"]
                changes.append(f"Oppdaterte author for {product_id}")
            if existing.get("relative_path") != latest_entry["relative_path"]:
                existing["relative_path"] = latest_entry["relative_path"]
                changes.append(f"Oppdaterte relative_path for {product_id}")
            product_url = f"{REPO_BLOB_BASE}/{latest_entry['relative_path']}"
            if existing.get("product_url") != product_url:
                existing["product_url"] = product_url
                changes.append(f"Oppdaterte product_url for {product_id}")

            updated_any = False
            for cap in existing.get("capabilities", []):
                label = cap.get("mapping_label") or cap.get("subcapability_name") or cap.get("capability_name")
                better = label_explanations.get(label, "").strip()
                current = (cap.get("explanation") or "").strip()
                if better and current != better:
                    cap["explanation"] = better
                    updated_any = True
            if updated_any:
                changes.append(f"Oppdaterte forklaringer i mapping for {product_id}")
            continue

        labels = [{"label": label, "mapping_label": label, "explanation": ""} for label in register_entry["capability_labels"]]
        if markdown_labels:
            labels = markdown_labels

        capabilities = build_capability_entries(register_entry["product_name"], labels, main_lookup, sub_lookup)
        products.append(
            {
                "product_id": product_id,
                "product_name": register_entry["product_name"],
                "version": latest_entry["version"],
                "author": latest_entry["author"],
                "relative_path": latest_entry["relative_path"],
                "product_url": f"{REPO_BLOB_BASE}/{latest_entry['relative_path']}",
                "capabilities": capabilities,
            }
        )
        changes.append(f"La til manglende mapping for {product_id}")

    products.sort(key=lambda item: item["product_id"])
    data["products"] = products

    if not changes:
        print("Ingen endringer foreslått.")
        return 0

    for change in changes:
        print(change)

    if apply_changes:
        MAP_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=4) + "\n", encoding="utf-8")
        print(f"Skrev oppdatert mapping til {MAP_FILE}")
    else:
        print("Dry-run: ingen filer skrevet. Kjør med --apply for å lagre.")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    return sync(args.apply)


if __name__ == "__main__":
    sys.exit(main())
