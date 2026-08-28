"""Kontroll av at eksterne lenker i ressursbeskrivelser er registrert i sources/links.md.

AGENTS.md krever at nye stabile og relevante eksterne URL-er legges inn i
`sources/links.md` i samme kjøring som de tas i bruk. Denne kontrollen finner
lenker som er brukt i ressursbeskrivelser uten å være registrert.

Bruk:
    python tools/check-source-links.py              rapport, avslutter alltid med 0
    python tools/check-source-links.py --strict     avslutter med 1 hvis noe mangler
    python tools/check-source-links.py --new-only   bare filer som er nye eller endret i Git
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import urlsplit

REPO_ROOT = Path(__file__).resolve().parents[1]
LINKS_FILE = REPO_ROOT / "sources" / "links.md"
RESOURCE_DIRS = [
    REPO_ROOT / "arkitektur" / "ressurser" / "operative-losninger-og-tjenester",
    REPO_ROOT / "arkitektur" / "ressurser" / "normerende-ressurser",
    REPO_ROOT / "arkitektur" / "ressurser" / "samarbeidsfora",
    REPO_ROOT / "arkitektur" / "ressurser" / "rammer-og-virkemidler",
]

URL_PATTERN = re.compile(r"https?://[^\s\)\],<>\"']+")

# Lenker til repoet selv er ikke eksterne kilder og skal ikke i sources/links.md.
IGNORED_HOST_FRAGMENTS = ("github.com/suphiro-arch",)

# Teknisk dybdedokumentasjon. Disse er kildegrunnlag for den enkelte ressursen og
# har sjelden gjenbruksverdi paa tvers, jf. regelen i AGENTS.md om at rene
# engangskilder ikke skal inn i sources/links.md.
TECHNICAL_DOC_HOSTS = {
    "docs.altinn.studio",
    "docs.digdir.no",
    "developers.fiks.ks.no",
    "docs.data.altinn.no",
}


def is_technical_doc(url: str) -> bool:
    host = urlsplit(url).netloc
    if host in TECHNICAL_DOC_HOSTS:
        return True
    # Dyplenker inn i en kodebase, men ikke organisasjons- eller repo-rot.
    return host == "github.com" and url.count("/") > 4


def normalize(url: str) -> str:
    """Fjerner tegnsetting som ofte henger igjen etter en URL i loepende tekst."""
    return url.rstrip(".,;:")


def load_registered_links() -> str:
    if not LINKS_FILE.exists():
        print("FEIL: finner ikke %s" % LINKS_FILE.relative_to(REPO_ROOT))
        sys.exit(2)
    return LINKS_FILE.read_text(encoding="utf-8")


def changed_files() -> set[Path]:
    """Filer som er nye eller endret i arbeidskopien, sammenlignet med HEAD."""
    try:
        out = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        ).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return set()
    paths = set()
    for line in out.splitlines():
        if len(line) > 3:
            paths.add((REPO_ROOT / line[3:].strip().strip('"')).resolve())
    return paths


def collect_resource_files(new_only: bool) -> list[Path]:
    files = []
    for directory in RESOURCE_DIRS:
        if directory.exists():
            files.extend(sorted(directory.glob("*.md")))
    if new_only:
        changed = changed_files()
        files = [f for f in files if f.resolve() in changed]
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="avslutt med kode 1 hvis lenker mangler i sources/links.md",
    )
    parser.add_argument(
        "--new-only",
        action="store_true",
        help="kontroller bare ressursfiler som er nye eller endret i arbeidskopien",
    )
    args = parser.parse_args()

    registered = load_registered_links()
    files = collect_resource_files(args.new_only)

    if not files:
        print("OK: Ingen ressursfiler aa kontrollere.")
        return 0

    missing: dict[str, set[str]] = defaultdict(set)
    occurrences = 0

    for path in files:
        text = path.read_text(encoding="utf-8")
        for raw in URL_PATTERN.findall(text):
            url = normalize(raw)
            if any(fragment in url for fragment in IGNORED_HOST_FRAGMENTS):
                continue
            if is_technical_doc(url):
                continue
            occurrences += 1
            if url not in registered:
                missing[url].add(path.name)

    if not missing:
        print(
            "OK: Alle %d eksterne lenker i %d ressursfiler er registrert i sources/links.md."
            % (occurrences, len(files))
        )
        return 0

    by_host: dict[str, list[str]] = defaultdict(list)
    for url in missing:
        by_host[urlsplit(url).netloc].append(url)

    print(
        "AVVIK: %d unike lenker i %d ressursfiler mangler i sources/links.md."
        % (len(missing), len(files))
    )
    print("Kontrollerte %d lenkeforekomster totalt.\n" % occurrences)

    for host in sorted(by_host, key=lambda h: (-len(by_host[h]), h)):
        urls = sorted(by_host[host])
        print("%s (%d)" % (host, len(urls)))
        for url in urls:
            brukt_i = sorted(missing[url])
            vist = ", ".join(brukt_i[:3])
            if len(brukt_i) > 3:
                vist += " og %d flere" % (len(brukt_i) - 3)
            print("  %s\n      brukt i: %s" % (url, vist))
        print()

    print(
        "Vurder hver lenke mot regelen i AGENTS.md: stabile, offisielle og relevante"
    )
    print(
        "lenker for videre ressursarbeid skal inn i sources/links.md. Rene engangskilder"
    )
    print("uten gjenbruksverdi skal bare staa i ressursfilas eget kildegrunnlag.")

    return 1 if args.strict else 0


if __name__ == "__main__":
    sys.exit(main())
