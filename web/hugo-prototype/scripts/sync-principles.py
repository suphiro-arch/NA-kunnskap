from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
SOURCE_FILE = REPO_ROOT / "arkitektur" / "prinsipper" / "principles.md"
OUT_FILE = REPO_ROOT / "web" / "hugo-prototype" / "content" / "prinsipper" / "_index.md"

FRONT_MATTER = """---
title: "Prinsipper"
weight: 20
description: "Arkitekturprinsipper som gir retning for samhandling, gjenbruk, tillit og styring i nasjonal arkitektur."
---

"""


def main() -> None:
    content = SOURCE_FILE.read_text(encoding="utf-8").strip() + "\n"
    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(FRONT_MATTER + content, encoding="utf-8")
    print(f"Synket prinsipper: {SOURCE_FILE} -> {OUT_FILE}")


if __name__ == "__main__":
    main()
