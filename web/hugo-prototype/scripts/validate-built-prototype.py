from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PUBLIC_DIR = REPO_ROOT / "web" / "hugo-prototype" / "public" / "kapabiliteter"

EMPTY_INTRO_PATTERN = re.compile(
    r'<article class="content-card content-card--capability-intro".*?<div class=prose><p>\s*</p>',
    re.DOTALL,
)
EMPTY_CARD_PATTERN = re.compile(r'<p class=section-card__description>\s*</p>')


def main() -> int:
    if not PUBLIC_DIR.exists():
        print(f"FEIL: Fant ikke bygget kapabilitetsinnhold i {PUBLIC_DIR}")
        return 1

    intro_failures: list[str] = []
    card_failures: list[str] = []

    for path in PUBLIC_DIR.rglob("index.html"):
        html = path.read_text(encoding="utf-8")
        rel = path.relative_to(REPO_ROOT).as_posix()

        if EMPTY_INTRO_PATTERN.search(html):
            intro_failures.append(rel)
        if EMPTY_CARD_PATTERN.search(html):
            card_failures.append(rel)

    if intro_failures or card_failures:
        if intro_failures:
            print("FEIL: Fant kapabilitetssider med tom introtekst:")
            for rel in intro_failures:
                print(f" - {rel}")
        if card_failures:
            print("FEIL: Fant kapabilitetssider med tom kortbeskrivelse for delkapabiliteter:")
            for rel in card_failures:
                print(f" - {rel}")
        return 1

    print("OK: Bygget prototype har ikke tomme kapabilitetsintroer eller tomme delkapabilitetskort.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
