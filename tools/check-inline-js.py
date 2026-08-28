"""Syntakskontroll av JavaScript som ligger innebygd i Hugo-maler og innhold.

Bakgrunn: en ødelagt strengliteral i `layouts/_default/baseof.html` stoppet
hele Hugo-byggingen. Skriptet ligger på hver side, så feilen slo ut på alle
sider samtidig. Ingen av de andre kontrollene ser på om innebygd JavaScript er
gyldig, og byggingen som avdekker det kjører bare i CI. Denne kontrollen gjør
den samme valideringen lokalt, før push.

Kontrollen henter ut hver `<script>`-blokk og lar Node parse den med
`node --check`. Ingenting kjøres, bare syntaksen kontrolleres.

Blokker som inneholder Hugo-syntaks (`{{ ... }}`) kan ikke parses som ren
JavaScript og hoppes over. Antallet rapporteres, slik at det ikke ser ut som
om alt er kontrollert når noe faktisk er utelatt.

Bruk:
    python tools/check-inline-js.py              rapport, avslutter alltid med 0
    python tools/check-inline-js.py --strict     avslutter med 1 ved syntaksfeil
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCAN_DIRS = [
    REPO_ROOT / "web" / "hugo-prototype" / "layouts",
    REPO_ROOT / "web" / "hugo-prototype" / "content",
]
SCAN_SUFFIXES = {".html", ".md"}

SCRIPT_PATTERN = re.compile(r"<script(?![^>]*\bsrc=)[^>]*>(.*?)</script>", re.S)
HUGO_SYNTAX = re.compile(r"\{\{.*?\}\}", re.S)
ERROR_LINE = re.compile(r"^\w*Error: .+")


def find_node() -> str | None:
    return shutil.which("node")


def collect_blocks() -> list[tuple[Path, int, str]]:
    """Alle innebygde skriptblokker som (fil, startlinje, kode)."""
    blocks = []
    for directory in SCAN_DIRS:
        if not directory.exists():
            continue
        for path in sorted(directory.rglob("*")):
            if not path.is_file() or path.suffix not in SCAN_SUFFIXES:
                continue
            text = path.read_text(encoding="utf-8")
            for match in SCRIPT_PATTERN.finditer(text):
                line = text[: match.start()].count("\n") + 1
                blocks.append((path, line, match.group(1)))
    return blocks


def check_block(node: str, code: str) -> str | None:
    """Returnerer feilmeldingen fra Node, eller None hvis syntaksen er gyldig."""
    result = subprocess.run(
        [node, "--check"],
        input=code,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if result.returncode == 0:
        return None
    # Node skriver kodeutdrag og pekelinje foerst, deretter selve feilen, og
    # til slutt stakksporet og versjonsnummeret. Vi vil ha feillinja.
    for linje in (result.stderr or "").splitlines():
        if ERROR_LINE.match(linje.strip()):
            return linje.strip()
    return "ukjent syntaksfeil"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="avslutt med kode 1 hvis en skriptblokk har syntaksfeil",
    )
    args = parser.parse_args()

    node = find_node()
    if not node:
        print("HOPPET OVER: finner ikke `node`, kan ikke kontrollere innebygd JavaScript.")
        print("Byggesteget i CI fanger fortsatt syntaksfeil, men da foerst etter push.")
        return 0

    blocks = collect_blocks()
    if not blocks:
        print("OK: Fant ingen innebygde skriptblokker aa kontrollere.")
        return 0

    hoppet_over = []
    feil = []
    kontrollert = 0

    for path, line, code in blocks:
        if HUGO_SYNTAX.search(code):
            hoppet_over.append((path, line))
            continue
        kontrollert += 1
        melding = check_block(node, code)
        if melding:
            feil.append((path, line, melding))

    if feil:
        print("FEIL: %d innebygde skriptblokker har syntaksfeil.\n" % len(feil))
        for path, line, melding in feil:
            print("%s:%d" % (path.relative_to(REPO_ROOT).as_posix(), line))
            print("  %s\n" % melding)
        print("Hugo-byggingen vil feile paa alle sider som bruker malen.")
        print("Unngaa escape-sekvenser i innebygd JavaScript naar teksten kan")
        print("skrives ferdig prosentkodet i stedet.\n")
    else:
        print("OK: Alle %d innebygde skriptblokker har gyldig syntaks." % kontrollert)

    if hoppet_over:
        print(
            "%d blokker hoppet over fordi de inneholder Hugo-syntaks og ikke kan"
            % len(hoppet_over)
        )
        print("parses som ren JavaScript:")
        for path, line in hoppet_over:
            print("  %s:%d" % (path.relative_to(REPO_ROOT).as_posix(), line))

    return 1 if (feil and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
