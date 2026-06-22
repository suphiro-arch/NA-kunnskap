from __future__ import annotations

import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
CONTENT_DIR = REPO_ROOT / "web" / "hugo-prototype" / "content"
QUOTED_SCALAR = re.compile(r"^[A-Za-z0-9_-]+:\s*(\".*)$")


def frontmatter_block(path: Path) -> tuple[list[str], list[str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return [], []

    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return lines[1:index], []

    return [], [f"{path}: mangler avsluttende frontmatter-markør"]


def validate_file(path: Path) -> list[str]:
    frontmatter, errors = frontmatter_block(path)
    for line_number, line in enumerate(frontmatter, start=2):
        match = QUOTED_SCALAR.match(line)
        if not match:
            continue

        value = match.group(1)
        try:
            json.loads(value)
        except json.JSONDecodeError as exc:
            errors.append(
                f"{path}:{line_number}: ugyldig sitert frontmatter-verdi ({exc.msg})"
            )

    return errors


def main() -> int:
    errors: list[str] = []
    for path in sorted(CONTENT_DIR.rglob("*.md")):
        errors.extend(validate_file(path))

    if errors:
        print("FEIL: Ugyldig Hugo-frontmatter funnet.")
        for error in errors:
            print(f"- {error}")
        return 1

    print("OK: Hugo-frontmatter ser gyldig ut.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
