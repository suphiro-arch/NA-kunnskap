"""Kontroll av at ressursbeskrivelser har den strukturen malen krever.

Bakgrunn: en ressursfil mistet åtte seksjoner ved et uhell, ble committet,
publisert og generert videre uten at noen av de andre kontrollene reagerte.
Verken tegnkoding, versjonssynk eller lenkekontroll ser at en fil mangler
obligatoriske seksjoner. Denne kontrollen lukker det hullet.

Kontrollen skiller mellom to nivåer:

Feil    Manglende h1-tittel, manglende kjernefelt, en seksjon uten innhold,
        eller en prinsippreferanse der koden og navnet ikke hører sammen.
        Kjernefeltene er de seksjonene som i dag finnes i samtlige ressursfiler
        i kategorien, så en feil betyr at fila er dårligere strukturert enn alt
        annet i porteføljen. Dette er signalet som fanger skade.

        Prinsippkontrollen sammenligner `**Pn: navn**` mot de kanoniske navnene
        i arkitektur/prinsipper/principles.md, og gjelder bare gjeldende
        versjoner. Erstattede versjoner er historikk og skal ikke ryddes.

Advarsel Seksjoner malen har, men som fila mangler, og overskrifter som
        verken står i malen eller er en kjent variant. Dette er synlig gjeld,
        ikke skade, og stopper ikke arbeidet.

Bruk:
    python tools/check-resource-structure.py              rapport, avslutter alltid med 0
    python tools/check-resource-structure.py --strict     avslutter med 1 ved feil
    python tools/check-resource-structure.py --new-only   bare filer som er nye eller endret i Git
    python tools/check-resource-structure.py --advarsler  vis også advarslene i sin helhet
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RESOURCE_ROOT = REPO_ROOT / "arkitektur" / "ressurser"
TEMPLATE_ROOT = REPO_ROOT / "config" / "templates"
PRINCIPLES_PATH = REPO_ROOT / "arkitektur" / "prinsipper" / "principles.md"

HEADING_PATTERN = re.compile(r"^## (.+?)\s*$", re.M)
VERSION_PATTERN = re.compile(r"-v(\d+)-")

# Prinsippkoden og prinsippnavnet slik de står i ressursfilene, for eksempel
# `- **P3: Bidra til digitaliseringsvennlige regelverk**`. Både kolon og punktum
# forekommer som skille.
PRINCIPLE_REF_PATTERN = re.compile(r"\*\*(P\d+)[:.]\s*([^*]+?)\s*\*\*")

# Kanonisk kode og navn i principles.md, som er kuratert kilde for prinsippene.
PRINCIPLE_CANON_PATTERN = re.compile(
    r"principle-panel__code\">(P\d+)</p>\s*<h3>([^<]+)</h3>"
)

# Kjernefeltene er utledet mekanisk: for hver kategori er dette snittet av
# overskriftene i alle eksisterende ressursfiler. Settet kan strammes inn etter
# hvert som eldre v0-filer fylles ut, men skal ikke utvides uten at samtlige
# filer i kategorien faktisk har seksjonen.
CATEGORIES: dict[str, dict] = {
    "normerende-ressurser": {
        "mal": "normerende-ressurs-template.md",
        "kjernefelt": [
            "Ressurs ID",
            "Ressurskategori",
            "Status/Livsfase",
            "Kort beskrivelse",
            "Formål og normerende rolle",
            "Kapabiliteter",
            "Målgruppe og brukere",
            "Normerende innhold",
            "Bruksområde",
            "Når ressursen normalt ikke er tilstrekkelig alene",
            "Scope og avgrensning",
            "Forvaltningsmodell",
            "Relasjon til andre ressurser",
            "Forretningsverdi og arkitekturverdi",
            "Utfordringer og risiko",
            "Publiseringsform og tilgjengelighet",
            "Støtter arkitekturprinsipper",
            "Lenke til dokumentasjon",
            "Kildegrunnlag brukt i utfyllingen",
        ],
        "alternativer": [
            ["Type standard eller veiledning", "Type normerende ressurs"],
        ],
    },
    "operative-losninger-og-tjenester": {
        "mal": "operative-ressurs-template.md",
        "kjernefelt": [
            "Ressurs ID",
            "Status/Livsfase",
            "Modenhet",
            "Kort beskrivelse",
            "Kapabiliteter",
            "Brukerbehov",
            "Hvem er brukerne og brukersegmentene",
            "Hovedfunksjoner",
            "Veikart over kommende funksjonalitet",
            "Forretningsverdi/Verdiforslag",
            "Utfordringer og risiko",
            "Kanaler",
            "Plattform",
            "Gjenbruk",
            "Finansiering",
            "Forvaltning/eier",
        ],
        "alternativer": [],
    },
    "rammer-og-virkemidler": {
        "mal": "okonomiske-og-juridiske-rammer-og-virkemidler-template.md",
        "kjernefelt": [
            "Navn",
            "Ressurs ID",
            "Ressurskategori",
            "Type virkemiddel",
            "Status/Livsfase",
            "Kort beskrivelse",
            "Formål og virkemiddelrolle",
            "Forpliktelsesnivå og etterlevelse",
            "Kapabiliteter",
            "Målgruppe og berørte aktører",
            "Virkemiddelmekanisme",
            "Bruksområde",
            "Typiske analyse- og beslutningssituasjoner",
            "Når ressursen normalt ikke er tilstrekkelig alene",
            "Økonomiske konsekvenser og insentiver",
            "Juridiske konsekvenser og handlingsrom",
            "Scope og avgrensning",
            "Forvaltningsmodell",
            "Relasjon til andre ressurser",
            "Forretningsverdi og arkitekturverdi",
            "Konsekvens ved manglende bruk eller avvik",
            "Utfordringer og risiko",
            "Publiseringsform og tilgjengelighet",
            "Støtter arkitekturprinsipper",
            "Lenke til dokumentasjon",
            "Kildegrunnlag brukt i utfyllingen",
        ],
        "alternativer": [],
    },
    "samarbeidsfora": {
        "mal": "samarbeidsforum-template.md",
        "kjernefelt": [
            "Ressurs ID",
            "Ressurskategori",
            "Status/Livsfase",
            "Kort beskrivelse",
            "Mandat og rolle",
            "Kapabiliteter",
            "Lenke til dokumentasjon",
            "Kildegrunnlag brukt i utfyllingen",
        ],
        "alternativer": [
            ["Type arena eller forum", "Type forum"],
        ],
    },
}

# Seksjoner som ikke står i malen, men som er bevisst brukt i porteføljen.
# Disse gir ingen advarsel.
AKSEPTERTE_TILLEGG = {
    "Endringer fra forrige versjon",
    "Endringer fra forrige versjoner",
    "Endringer i denne revisjonen",
    "Merknad om kvalitetsforbedringer",
    "Svakheter, spenninger og begrensninger mot prinsippene",
    # Malen for gjenbrukbare løsninger har denne som underoverskrift under
    # Hovedfunksjoner. Flere filer har løftet den til egen seksjon.
    "Scope og avgrensning",
}

# Seksjoner i malfilene som er instruks til den som skriver, ikke seksjoner som
# skal finnes i selve ressursfila. Kontrollen utleder de forventede seksjonene
# fra malens overskrifter, så en ny instruksjonsseksjon i en mal må føres opp her.
# Ellers blir den umiddelbart rapportert som manglende i hver fil i kategorien.
MAL_INNLEDNING = {
    "Arbeidsregel for v0.1",
    "Forventning til v1",
    "Kort v1-sjekkliste",
    "Minstekrav for v1",
    "Merking av fakta, deduksjon og usikkerhet",
    "To typer arenaer i samme mal",
}


def malseksjoner(template_name: str) -> list[str]:
    """Seksjonene malen definerer, uten instruksjonsdelen på toppen."""
    path = TEMPLATE_ROOT / template_name
    if not path.exists():
        print("FEIL: finner ikke malen %s" % path.relative_to(REPO_ROOT))
        sys.exit(2)
    headings = HEADING_PATTERN.findall(path.read_text(encoding="utf-8"))
    return [h for h in headings if h not in MAL_INNLEDNING]


def kanoniske_prinsipper() -> dict[str, str]:
    """Prinsippkode til prinsippnavn, hentet fra den kuraterte prinsippfila.

    Returnerer tomt oppslag hvis fila mangler eller ikke lar seg lese. Kontrollen
    skal ikke stoppe arbeidet fordi prinsippfila er flyttet; da faller
    prinsippkontrollen bare bort.
    """
    if not PRINCIPLES_PATH.exists():
        return {}
    tekst = PRINCIPLES_PATH.read_text(encoding="utf-8")
    return {m.group(1): m.group(2).strip() for m in PRINCIPLE_CANON_PATTERN.finditer(tekst)}


def prinsippfeil(text: str, kanon: dict[str, str]) -> list[str]:
    """Prinsippreferanser der koden og navnet ikke hører sammen.

    Bakgrunn: to filer oppgav prinsippnavn som ikke finnes, en tredje brukte
    riktig navn med feil P-kode, og en fjerde hadde et navn fra et helt annet
    rammeverk. Feilen er usynlig for de øvrige kontrollene, fordi strukturen er
    korrekt og bare innholdet er galt. Den er samtidig alvorlig: en
    prinsippreferanse er et sporbarhetsløfte, og en leser som slår opp koden
    finner noe annet enn det fila påstår.
    """
    if not kanon:
        return []
    feil = []
    for match in PRINCIPLE_REF_PATTERN.finditer(text):
        kode, navn = match.group(1), match.group(2).strip().rstrip(".")
        if kode not in kanon:
            feil.append(
                "prinsippkoden %s finnes ikke i principles.md (gyldige: %s)"
                % (kode, ", ".join(sorted(kanon)))
            )
        elif navn.casefold() != kanon[kode].casefold():
            feil.append(
                "%s er oppgitt som '%s', men heter '%s' i principles.md"
                % (kode, navn, kanon[kode])
            )
    return feil


def gjeldende_filnavn() -> set[str]:
    """Filnavnene registeret peker på, altså gjeldende versjon av hver ressurs.

    Registeret er autoritativt for hvilken versjon som gjelder, jf. beslutningen
    om streng versjonspeking. Erstattede versjoner beholdes som historikk, og
    avvik i dem er ikke gjeld som skal ryddes.
    """
    register = REPO_ROOT / "arkitektur" / "ressurser" / "produktnummerering.md"
    if not register.exists():
        return set()
    tekst = register.read_text(encoding="utf-8")
    return set(re.findall(r"([^/()\s]+\.md)\)", tekst))


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


def collect_resource_files(new_only: bool) -> list[tuple[str, Path]]:
    files = []
    for category in CATEGORIES:
        directory = RESOURCE_ROOT / category
        if not directory.exists():
            continue
        for path in sorted(directory.glob("*.md")):
            if path.name == "README.md":
                continue
            files.append((category, path))
    if new_only:
        changed = changed_files()
        files = [(c, p) for c, p in files if p.resolve() in changed]
    return files


def tomme_seksjoner(text: str) -> list[str]:
    """Seksjoner uten noe innhold i det hele tatt før neste seksjon.

    Underoverskrifter teller som innhold. En seksjon som bare består av
    `###`-blokker er altså i orden.
    """
    tomme = []
    blokker = re.split(r"^## (.+?)\s*$", text, flags=re.M)
    # blokker veksler mellom overskrift og innhold etter første element.
    for i in range(1, len(blokker) - 1, 2):
        if not blokker[i + 1].strip():
            tomme.append(blokker[i])
    return tomme


def kontroller(
    category: str,
    path: Path,
    mal: list[str],
    kanon: dict[str, str] | None = None,
    er_gjeldende: bool = True,
) -> tuple[list[str], list[str]]:
    text = path.read_text(encoding="utf-8")
    funnet = HEADING_PATTERN.findall(text)
    funnet_sett = set(funnet)
    regler = CATEGORIES[category]

    feil: list[str] = []
    advarsler: list[str] = []

    if not re.match(r"^#\s+\S", text.lstrip("﻿")):
        feil.append("mangler h1-tittel på første linje")

    mangler_kjerne = [s for s in regler["kjernefelt"] if s not in funnet_sett]
    if mangler_kjerne:
        feil.append("mangler kjernefelt: %s" % ", ".join(mangler_kjerne))

    for gruppe in regler["alternativer"]:
        if not any(s in funnet_sett for s in gruppe):
            feil.append("mangler en av: %s" % " / ".join(gruppe))

    for seksjon in tomme_seksjoner(text):
        feil.append("seksjonen '%s' er tom" % seksjon)

    # Prinsippnavn kontrolleres bare i gjeldende versjoner. Erstattede versjoner
    # er bevart som historikk, og avvik i dem skal ikke ryddes.
    if er_gjeldende:
        feil.extend(prinsippfeil(text, kanon or {}))

    kjente = set(mal) | AKSEPTERTE_TILLEGG
    for gruppe in regler["alternativer"]:
        kjente.update(gruppe)

    # Seksjoner som allerede dekkes av kjernefeltene eller av en oppfylt
    # alternativgruppe, skal ikke gi advarsel i tillegg.
    dekket = set(regler["kjernefelt"])
    for gruppe in regler["alternativer"]:
        if any(s in funnet_sett for s in gruppe):
            dekket.update(gruppe)

    mangler_mal = [s for s in mal if s not in funnet_sett and s not in dekket]
    if mangler_mal:
        advarsler.append("mangler malseksjon: %s" % ", ".join(mangler_mal))

    ukjente = [s for s in funnet if s not in kjente]
    if ukjente:
        advarsler.append("overskrift utenfor malen: %s" % ", ".join(sorted(set(ukjente))))

    return feil, advarsler


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict",
        action="store_true",
        help="avslutt med kode 1 hvis en ressursfil har strukturfeil",
    )
    parser.add_argument(
        "--new-only",
        action="store_true",
        help="kontroller bare ressursfiler som er nye eller endret i arbeidskopien",
    )
    parser.add_argument(
        "--advarsler",
        action="store_true",
        help="skriv ut alle advarsler, ikke bare antallet",
    )
    args = parser.parse_args()

    maler = {c: malseksjoner(r["mal"]) for c, r in CATEGORIES.items()}
    files = collect_resource_files(args.new_only)

    if not files:
        print("OK: Ingen ressursfiler å kontrollere.")
        return 0

    kanon = kanoniske_prinsipper()
    gjeldende = gjeldende_filnavn()

    feil_per_fil: dict[Path, list[str]] = {}
    advarsler_per_fil: dict[Path, list[str]] = {}

    for category, path in files:
        feil, advarsler = kontroller(
            category,
            path,
            maler[category],
            kanon=kanon,
            er_gjeldende=path.name in gjeldende,
        )
        if feil:
            feil_per_fil[path] = feil
        if advarsler:
            advarsler_per_fil[path] = advarsler

    if feil_per_fil:
        print("FEIL: %d ressursfiler har strukturfeil.\n" % len(feil_per_fil))
        for path in sorted(feil_per_fil):
            print("%s" % path.relative_to(REPO_ROOT).as_posix())
            for melding in feil_per_fil[path]:
                print("  - %s" % melding)
            print()
        print("Sammenlign fila med malen i config/templates/ før den committes.")
        print("Ved uhell under redigering: hent tapte seksjoner tilbake med")
        print("git show <commit>:<sti> framfor å skrive dem på nytt.\n")
    else:
        print(
            "OK: Alle %d ressursfiler har kjernestrukturen malen krever, og"
            % len(files)
        )
        print("    prinsippreferansene i gjeldende versjoner stemmer med principles.md.")

    if advarsler_per_fil:
        antall = sum(len(v) for v in advarsler_per_fil.values())
        aktive = [p for p in advarsler_per_fil if p.name in gjeldende]
        historiske = [p for p in advarsler_per_fil if p.name not in gjeldende]
        print(
            "%d advarsler i %d filer (ufullstendige maler og avvikende overskrifter)."
            % (antall, len(advarsler_per_fil))
        )
        if gjeldende:
            print(
                "  Av disse er %d %s og %d %s."
                % (
                    len(aktive),
                    "gjeldende versjon" if len(aktive) == 1 else "gjeldende versjoner",
                    len(historiske),
                    "erstattet versjon" if len(historiske) == 1 else "erstattede versjoner",
                )
            )
            if aktive:
                print("  Reell strukturgjeld ligger i de gjeldende versjonene:")
                for path in sorted(aktive):
                    print("    %s" % path.relative_to(REPO_ROOT).as_posix())
            else:
                print("  Ingen gjeldende versjon har avvik. Resten er historikk.")
        if args.advarsler:
            print()
            for path in sorted(advarsler_per_fil):
                merke = "" if path.name in gjeldende else "  [erstattet versjon]"
                print("%s%s" % (path.relative_to(REPO_ROOT).as_posix(), merke))
                for melding in advarsler_per_fil[path]:
                    print("  - %s" % melding)
                print()
        else:
            print("Kjør med --advarsler for å se dem.")

    return 1 if (feil_per_fil and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
