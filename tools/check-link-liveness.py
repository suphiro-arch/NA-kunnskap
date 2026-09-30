"""Kontroll av at lenkene i sources/links.md fortsatt svarer.

`check-source-links.py` kontrollerer at lenker som er brukt i ressursbeskrivelser
er registrert i `sources/links.md`. Ingen kontroll gaar andre veien og ser om de
registrerte lenkene fortsatt lever. Konsekvensen har vaert at doede lenker blir
staaende: 2026-09-30 viste det seg at tre registrerte repositorielenker hadde
vaert feil i fem dager, og de ble bare oppdaget fordi en kjoering tilfeldigvis
kontrollerte lisensvilkaar mot GitHub.

Kontrollen deler svarene i fire:

    OK          2xx, lenken svarer
    FLYTTET     permanent omdirigering til en annen adresse, tittel eller URL
                boer oppdateres
    DOED        404 eller 410, lenken skal rettes eller fjernes
    USIKKER     403, 429, 5xx, tidsavbrudd og navneoppslagsfeil. Sier ikke at
                lenken er doed. Flere offentlige nettsteder avviser maskinell
                henting, jf. merknaden om 403 fra digdir.no i links.md.

Bare DOED og FLYTTET er avvik. USIKKER rapporteres separat og maa kontrolleres
manuelt i nettleser foer noe endres.

Kontrollen er ikke en foer-commit-kontroll. Den gaar mot nettet, tar noen
minutter og boer kjoeres med jevne mellomrom, ikke i hver kjoering.

Bruk:
    python tools/check-link-liveness.py                 rapport, avslutter alltid med 0
    python tools/check-link-liveness.py --strict        avslutter med 1 ved DOED eller FLYTTET
    python tools/check-link-liveness.py --host github   bare lenker med dette i vertsnavnet
    python tools/check-link-liveness.py --vis-usikre    ta med USIKKER i rapporten
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlsplit

REPO_ROOT = Path(__file__).resolve().parents[1]
LINKS_FILE = REPO_ROOT / "sources" / "links.md"

URL_PATTERN = re.compile(r"https?://[^\s\)\],<>\"']+")

# Noen nettsteder avviser standard Python-UA. En beskrivende UA gir faerre
# falske 403 og gjoer det mulig for mottakeren aa se hvem som henter.
USER_AGENT = (
    "NA-kunnskap-lenkekontroll/1.0 "
    "(+https://github.com/suphiro-arch/NA-kunnskap)"
)

OK = "OK"
FLYTTET = "FLYTTET"
DOED = "DOED"
USIKKER = "USIKKER"


@dataclass
class Resultat:
    url: str
    linje: int
    tittel: str
    status: str
    detalj: str = ""


class RedirectSporer(urllib.request.HTTPRedirectHandler):
    """Fanger opp om veien til svaret gikk gjennom en permanent omdirigering."""

    def __init__(self) -> None:
        self.permanent_til: str | None = None

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        if code in (301, 308):
            self.permanent_til = newurl
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def les_lenker() -> list[tuple[str, int, str]]:
    """Returnerer (url, linjenummer, tittel) for hver lenke i links.md."""
    if not LINKS_FILE.exists():
        print("FEIL: finner ikke %s" % LINKS_FILE.relative_to(REPO_ROOT))
        sys.exit(2)

    lenker = []
    for nr, linje in enumerate(LINKS_FILE.read_text(encoding="utf-8").splitlines(), 1):
        treff = URL_PATTERN.search(linje)
        if not treff:
            continue
        url = treff.group(0).rstrip(".,;:")
        tittel = linje[: treff.start()].lstrip("- ").rstrip(": ").strip()
        lenker.append((url, nr, tittel or "(uten tittel)"))
    return lenker


def sjekk(url: str, linje: int, tittel: str, timeout: float) -> Resultat:
    sporer = RedirectSporer()
    opener = urllib.request.build_opener(sporer)
    hode = {"User-Agent": USER_AGENT, "Accept": "*/*"}

    # HEAD foerst. Mange servere svarer 403 eller 405 paa HEAD, og da
    # gjentas forsoeket med GET foer noe konkluderes.
    for metode in ("HEAD", "GET"):
        sporer.permanent_til = None
        try:
            req = urllib.request.Request(url, headers=hode, method=metode)
            with opener.open(req, timeout=timeout) as svar:
                if sporer.permanent_til and sporer.permanent_til != url:
                    return Resultat(url, linje, tittel, FLYTTET, sporer.permanent_til)
                return Resultat(url, linje, tittel, OK, str(svar.status))
        except urllib.error.HTTPError as feil:
            if feil.code in (404, 410):
                return Resultat(url, linje, tittel, DOED, "HTTP %d" % feil.code)
            if metode == "HEAD" and feil.code in (400, 403, 405, 406, 501):
                continue
            return Resultat(url, linje, tittel, USIKKER, "HTTP %d" % feil.code)
        except urllib.error.URLError as feil:
            return Resultat(url, linje, tittel, USIKKER, str(feil.reason))
        except Exception as feil:  # tidsavbrudd, ugyldig sertifikat, feil i svaret
            return Resultat(url, linje, tittel, USIKKER, type(feil).__name__)

    return Resultat(url, linje, tittel, USIKKER, "ikke besvart")


def skriv_gruppe(tittel: str, treff: list[Resultat], forklaring: str) -> None:
    print("%s (%d)" % (tittel, len(treff)))
    print("  %s\n" % forklaring)
    etter_vert: dict[str, list[Resultat]] = defaultdict(list)
    for r in treff:
        etter_vert[urlsplit(r.url).netloc].append(r)
    for vert in sorted(etter_vert, key=lambda v: (-len(etter_vert[v]), v)):
        for r in sorted(etter_vert[vert], key=lambda r: r.linje):
            print("  links.md:%d  %s" % (r.linje, r.tittel))
            print("      %s" % r.url)
            print("      %s" % r.detalj)
    print()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="avslutt med kode 1 hvis noen lenker er doede eller permanent flyttet",
    )
    parser.add_argument(
        "--host",
        default="",
        help="kontroller bare lenker der vertsnavnet inneholder denne teksten",
    )
    parser.add_argument(
        "--vis-usikre",
        action="store_true",
        help="ta med lenker som ikke kunne kontrolleres maskinelt",
    )
    parser.add_argument(
        "--timeout", type=float, default=15.0, help="tidsavbrudd per lenke i sekunder"
    )
    parser.add_argument(
        "--workers", type=int, default=8, help="antall parallelle forespoersler"
    )
    args = parser.parse_args()

    lenker = les_lenker()
    if args.host:
        lenker = [l for l in lenker if args.host.lower() in urlsplit(l[0]).netloc.lower()]

    # Samme URL kan staa flere steder. Hver forekomst rapporteres, men
    # nettverkskallet gjoeres bare en gang per unike adresse.
    unike = sorted({url for url, _, _ in lenker})
    if not unike:
        print("OK: Ingen lenker aa kontrollere.")
        return 0

    print(
        "Kontrollerer %d unike lenker fra %d linjer i sources/links.md ...\n"
        % (len(unike), len(lenker))
    )

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        svar = dict(
            zip(
                unike,
                pool.map(lambda u: sjekk(u, 0, "", args.timeout), unike),
            )
        )

    resultater = [
        Resultat(url, nr, tittel, svar[url].status, svar[url].detalj)
        for url, nr, tittel in lenker
    ]

    doede = [r for r in resultater if r.status == DOED]
    flyttede = [r for r in resultater if r.status == FLYTTET]
    usikre = [r for r in resultater if r.status == USIKKER]
    levende = len(resultater) - len(doede) - len(flyttede) - len(usikre)

    if not doede and not flyttede:
        print(
            "OK: Ingen doede eller permanent flyttede lenker. %d svarte, %d kunne ikke "
            "kontrolleres maskinelt." % (levende, len(usikre))
        )
    else:
        print(
            "AVVIK: %d doede og %d permanent flyttede lenker i sources/links.md."
            % (len(doede), len(flyttede))
        )
        print(
            "%d svarte, %d kunne ikke kontrolleres maskinelt.\n"
            % (levende, len(usikre))
        )
        if doede:
            skriv_gruppe(
                "DOEDE LENKER",
                doede,
                "Rett adressen eller fjern oppfoeringen. Er kilden erstattet av en "
                "nyere, registrer den nye og behold\n  den gamle bare hvis den fortsatt "
                "svarer og har historisk verdi.",
            )
        if flyttede:
            skriv_gruppe(
                "PERMANENT FLYTTET",
                flyttede,
                "Lenken svarer, men adressen er endret. Oppdater URL-en slik at "
                "kildegrunnlaget peker rett.",
            )

    if usikre and args.vis_usikre:
        skriv_gruppe(
            "IKKE KONTROLLERT",
            usikre,
            "Dette er ikke avvik. Flere offentlige nettsteder avviser maskinell "
            "henting. Kontroller i nettleser\n  foer noe endres.",
        )
    elif usikre:
        print(
            "%d lenker kunne ikke kontrolleres maskinelt. Kjoer med --vis-usikre for "
            "aa se dem." % len(usikre)
        )

    return 1 if args.strict and (doede or flyttede) else 0


if __name__ == "__main__":
    sys.exit(main())
