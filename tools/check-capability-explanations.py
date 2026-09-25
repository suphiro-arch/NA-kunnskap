"""Kontroll av at hvert kapabilitetspunkt i gjeldende ressursfiler har en forklaring.

Bakgrunn: AGENTS.md krever en faglig begrunnelse under hvert kapabilitetspunkt.
En kobling uten begrunnelse blir aldri prøvd mot definisjonen i
capabilities.yaml, og det er slik feilkoblinger overlever. Tidligere forsøk på å
måle omfanget ga upålitelige tall fordi porteføljen bruker flere kulepunktformater.
Denne kontrollen tolker alle formatene som faktisk forekommer:

    - **Hoved: Del**                  label alene, forklaring på innrykket linje under
      Forklaring ...
    - **Hoved: Del** forklaring ...   forklaring på samme linje som labelen
    - **Hoved: Del:** forklaring      kolon eller tankestrek som skille godtas
    - Hoved: Del                      label uten fet skrift, med eller uten forklaring
    - **Hoved: Del**                  innrykket underpunkt som forklaring
      - Forklaring ...

En ikke-innrykket linje rett under kulepunktet, uten blank linje imellom, regnes
også som forklaring (markdowns «lazy continuation»). Et eget avsnitt etter en
blank linje hører derimot ikke til kulepunktet over.

Kontrollen skiller mellom tre nivåer:

Feil      Kapabilitetspunkt uten forklaring.

Advarsel  Forklaring som er kortere enn terskelen (`--min-ord`, standard 8 ord
          utover labelen), eller som bare gjentar labelen.

Merknad   Tekst etter siste kulepunkt i seksjonen, som `Grunnlag:`-linjer eller
          et samlende avsnitt. `tools/sync-resource-metadata.py` trekker slik
          tekst inn i forklaringen til siste kapabilitet i
          produkt-kapabilitet-koblinger.yaml. AGENTS.md sier at avsluttende
          brødtekst skal stå før kulelista.

Bare gjeldende versjoner kontrolleres, med samme versjonsvalg som
`tools/check-resource-version-sync.py`. Erstattede versjoner er historikk.

Med `--mapping` kontrolleres også `explanation` i
produkt-kapabilitet-koblinger.yaml: tomme forklaringer, automatiske plassholdere
og tekst som er trukket inn fra utenfor kapabilitetspunktet.

Bruk:
    python tools/check-capability-explanations.py              rapport, avslutter alltid med 0
    python tools/check-capability-explanations.py --strict     avslutter med 1 ved feil
    python tools/check-capability-explanations.py --new-only   bare filer som er nye eller endret i Git
    python tools/check-capability-explanations.py --advarsler  vis også korte forklaringer og merknader
    python tools/check-capability-explanations.py --mapping    kontroller også forklaringene i mappingfila
    python tools/check-capability-explanations.py --formater   vis hvilke kulepunktformater som brukes
    python tools/check-capability-explanations.py --min-ord N  endre terskelen for korte forklaringer
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
VERSION_SYNC = REPO_ROOT / "tools" / "check-resource-version-sync.py"
MAP_FILE = REPO_ROOT / "arkitektur" / "kapabiliteter" / "produkt-kapabilitet-koblinger.yaml"

CAP_SECTION_PATTERN = re.compile(r"^##\s+Kapabiliteter\s*$")
BULLET_PATTERN = re.compile(r"^(?P<indent>\s*)[-*]\s+(?P<body>.*)$")
BOLD_LABEL_PATTERN = re.compile(r"^\*\*(?P<label>.+?)\*\*(?P<rest>.*)$")
# Skilletegn mellom label og forklaring på samme linje.
SEPARATOR_PATTERN = re.compile(r"^\s*(?:[:–—-]\s*)?")
WORD_PATTERN = re.compile(r"\w+", re.UNICODE)

DEFAULT_MIN_WORDS = 8

# Tekst sync-verktøyet kan ha trukket inn i `explanation` fra utenfor punktet.
MAPPING_POLLUTION_MARKERS = (
    "Grunnlag:",
    "Koblingene er satt fordi",
    "**Deduksjon:**",
    "Deduksjon:",
)
MAPPING_PLACEHOLDER = "Foreløpig automatisk opprettet"

CATEGORY_NAMES = {
    "operative-losninger-og-tjenester": "operative løsninger og tjenester",
    "normerende-ressurser": "standarder og veiledning",
    "samarbeidsfora": "samhandlingsarenaer og organisering",
    "rammer-og-virkemidler": "økonomiske og juridiske rammer og virkemidler",
}


def load_version_sync():
    spec = importlib.util.spec_from_file_location("check_resource_version_sync", VERSION_SYNC)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Kunne ikke laste {VERSION_SYNC.relative_to(REPO_ROOT)}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@dataclass
class CapabilityPoint:
    lineno: int
    label: str
    base_format: str
    explanation_parts: list[str] = field(default_factory=list)
    continuation: str = ""

    @property
    def format(self) -> str:
        return f"{self.base_format}, {self.continuation}" if self.continuation else self.base_format

    @property
    def explanation(self) -> str:
        return " ".join(part for part in self.explanation_parts if part).strip()


@dataclass
class ParsedSection:
    found: bool = False
    points: list[CapabilityPoint] = field(default_factory=list)
    trailing_text: list[tuple[int, str]] = field(default_factory=list)
    leading_text: list[tuple[int, str]] = field(default_factory=list)


def valid_labels(version_sync) -> set[str]:
    """Alle skrivemåter som godtas som merkelapp, for å skille label fra forklaring
    i kulepunkter uten fet skrift."""
    capability_names, parents_by_subcapability, _ = version_sync.canonical_capability_names()
    labels = set(capability_names)
    for name in capability_names:
        labels.add(f"{name}: {name}")
    for child, parents in parents_by_subcapability.items():
        labels.add(child)
        for parent in parents:
            labels.add(f"{parent}: {child}")
    return labels


def split_plain_bullet(body: str, labels: set[str]) -> tuple[str, str]:
    """Kulepunkt uten fet skrift: finn lengste kjente merkelapp i starten.

    `- Hoved: Del: forklaring` og `- Hoved: Del – forklaring` gir label og
    forklaring. Finnes ingen kjent merkelapp, er hele teksten label, slik
    sync-verktøyet også tolker den.
    """
    text = body.strip()
    best = ""
    for label in labels:
        if len(label) <= len(best):
            continue
        if text == label or (
            text.startswith(label) and re.match(r"^\s*[:–—-]?\s", text[len(label):] + " ")
        ):
            best = label
    if not best:
        return text.rstrip(":.").strip(), ""
    rest = text[len(best):]
    return best, SEPARATOR_PATTERN.sub("", rest, count=1).strip()


def parse_section(path: Path, labels: set[str]) -> ParsedSection:
    result = ParsedSection()
    lines = path.read_text(encoding="utf-8-sig").splitlines()
    in_section = False
    current: CapabilityPoint | None = None
    previous_blank = True

    for lineno, raw in enumerate(lines, start=1):
        line = raw.rstrip()
        stripped = line.strip()
        if CAP_SECTION_PATTERN.match(stripped):
            in_section = True
            result.found = True
            continue
        if not in_section:
            continue
        if line.startswith("## "):
            break
        if not stripped:
            previous_blank = True
            continue
        if stripped.startswith("#"):
            # Underoverskrift avslutter et eventuelt punkt.
            current = None
            previous_blank = False
            continue

        indent = len(line) - len(line.lstrip())
        bullet = BULLET_PATTERN.match(line)

        if bullet and indent == 0:
            body = bullet.group("body").strip()
            bold = BOLD_LABEL_PATTERN.match(body)
            if bold:
                label = bold.group("label").strip().rstrip(":").strip()
                rest = SEPARATOR_PATTERN.sub("", bold.group("rest"), count=1).strip()
                fmt = "fet label, forklaring på samme linje" if rest else "fet label alene"
            else:
                label, rest = split_plain_bullet(body, labels)
                fmt = "label uten fet skrift, forklaring på samme linje" if rest else "label uten fet skrift"
            current = CapabilityPoint(lineno=lineno, label=label, base_format=fmt)
            if rest:
                current.explanation_parts.append(rest)
            result.points.append(current)
            previous_blank = False
            continue

        if current is not None and indent > 0:
            # Innrykket linje eller innrykket underpunkt hører til punktet over.
            text = bullet.group("body").strip() if bullet else stripped
            current.explanation_parts.append(text)
            if len(current.explanation_parts) == 1:
                current.continuation = "forklaring som innrykket underpunkt" if bullet else "forklaring på innrykket linje under"
            previous_blank = False
            continue

        if current is not None and not previous_blank:
            # Lazy continuation: ikke-innrykket linje rett under punktet.
            current.explanation_parts.append(stripped)
            if len(current.explanation_parts) == 1:
                current.continuation = "forklaring på fortsettelseslinje uten innrykk"
            previous_blank = False
            continue

        # Eget avsnitt: enten før lista eller etter et punkt.
        if result.points:
            result.trailing_text.append((lineno, stripped))
            current = None
        else:
            result.leading_text.append((lineno, stripped))
        previous_blank = False

    return result


def meaningful_words(explanation: str, label: str) -> int:
    """Antall ord i forklaringen som ikke allerede står i labelen."""
    label_words = {w.casefold() for w in WORD_PATTERN.findall(label)}
    words = WORD_PATTERN.findall(explanation.replace("**", "").replace("`", ""))
    return sum(1 for w in words if w.casefold() not in label_words)


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


def category_of(path: Path) -> str:
    return CATEGORY_NAMES.get(path.parent.name, path.parent.name)


def check_mapping(
    latest: dict[int, dict], points_by_id: dict[int, list[CapabilityPoint]]
) -> tuple[Counter, list[str], list[str]]:
    """Forklaringene i mappingfila: tomme, plassholdere og forurensede.

    Sammenligner også med forklaringen kontrollen leser i ressursfila. Avvik
    betyr at sync-verktøyet ikke har ført forklaringen videre, typisk fordi den
    står på samme linje som labelen eller fordi labelen mangler prefiks.
    """
    counts: Counter = Counter()
    findings: list[str] = []
    differences: list[str] = []
    data = json.loads(MAP_FILE.read_text(encoding="utf-8-sig"))
    for product in data.get("products", []):
        product_id = product.get("product_id")
        if product_id not in latest:
            continue
        source_points = {
            point.label.rpartition(":")[2].strip(): point for point in points_by_id.get(product_id, [])
        }
        for cap in product.get("capabilities", []):
            counts["totalt"] += 1
            label = cap.get("mapping_label") or cap.get("subcapability_name") or cap.get("capability_name")
            explanation = (cap.get("explanation") or "").strip()
            origin = f"produkt {product_id} {product.get('product_name')}: «{label}»"
            if not explanation:
                counts["tom"] += 1
                findings.append(f"{origin}: tom forklaring")
            elif explanation.startswith(MAPPING_PLACEHOLDER):
                counts["plassholder"] += 1
                findings.append(f"{origin}: automatisk plassholder, ikke faglig forklaring")
            else:
                marker = next((m for m in MAPPING_POLLUTION_MARKERS if m in explanation), None)
                if marker:
                    counts["forurenset"] += 1
                    findings.append(f"{origin}: inneholder «{marker}», trukket inn fra utenfor punktet")

            short_name = cap.get("subcapability_name") or cap.get("capability_name") or ""
            point = source_points.get(short_name)
            if point is None:
                counts["uten punkt i ressursfila"] += 1
                differences.append(f"{origin}: finnes i mappingfila, men ikke under ## Kapabiliteter i ressursfila")
            elif point.explanation and point.explanation != explanation:
                counts["avviker fra ressursfila"] += 1
                differences.append(f"{origin}: forklaringen avviker fra ressursfila ({point.format})")
    return counts, findings, differences


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--strict", action="store_true", help="avslutt med kode 1 hvis et kapabilitetspunkt mangler forklaring")
    parser.add_argument("--new-only", action="store_true", help="kontroller bare ressursfiler som er nye eller endret i arbeidskopien")
    parser.add_argument("--advarsler", action="store_true", help="skriv ut korte forklaringer og merknader i sin helhet, ikke bare antallet")
    parser.add_argument("--mapping", action="store_true", help="kontroller også explanation i produkt-kapabilitet-koblinger.yaml")
    parser.add_argument("--formater", action="store_true", help="skriv ut hvilke kulepunktformater som brukes, med antall filer per format")
    parser.add_argument(
        "--min-ord",
        type=int,
        default=DEFAULT_MIN_WORDS,
        help=f"minste antall ord utover labelen før forklaringen regnes som for kort (standard {DEFAULT_MIN_WORDS})",
    )
    args = parser.parse_args()

    version_sync = load_version_sync()
    latest = version_sync.latest_files_by_id()
    labels = valid_labels(version_sync)

    entries = sorted(latest.values(), key=lambda e: e["id"])
    if args.new_only:
        changed = changed_files()
        entries = [e for e in entries if e["path"].resolve() in changed]

    if not entries:
        print("OK: Ingen gjeldende ressursfiler å kontrollere.")
        return 0

    errors: dict[str, list[str]] = defaultdict(list)
    warnings: dict[str, list[str]] = defaultdict(list)
    notes: dict[str, list[str]] = defaultdict(list)
    per_category: dict[str, Counter] = defaultdict(Counter)
    formats: dict[str, set[str]] = defaultdict(set)
    total_points = 0
    points_by_id: dict[int, list[CapabilityPoint]] = {}

    for entry in entries:
        path = entry["path"]
        rel = entry["relative_path"]
        category = category_of(path)
        per_category[category]["filer"] += 1
        section = parse_section(path, labels)
        points_by_id[entry["id"]] = section.points

        if not section.found:
            errors[rel].append("mangler seksjonen ## Kapabiliteter")
            per_category[category]["uten seksjon"] += 1
            continue
        if not section.points:
            errors[rel].append("## Kapabiliteter har ingen kapabilitetspunkter")
            per_category[category]["uten punkter"] += 1
            continue

        file_has_error = False
        for point in section.points:
            total_points += 1
            per_category[category]["punkter"] += 1
            formats[point.format].add(rel)
            explanation = point.explanation
            if not explanation:
                errors[rel].append(f"linje {point.lineno}: «{point.label}» mangler forklaring")
                per_category[category]["uten forklaring"] += 1
                file_has_error = True
                continue
            words = meaningful_words(explanation, point.label)
            if words == 0:
                warnings[rel].append(f"linje {point.lineno}: «{point.label}» har en forklaring som bare gjentar labelen")
                per_category[category]["for kort"] += 1
            elif words < args.min_ord:
                warnings[rel].append(
                    f"linje {point.lineno}: «{point.label}» har bare {words} ord forklaring utover labelen: «{explanation}»"
                )
                per_category[category]["for kort"] += 1
        if file_has_error:
            per_category[category]["filer med feil"] += 1

        if section.trailing_text:
            first_line = section.trailing_text[0][0]
            preview = section.trailing_text[0][1]
            if len(preview) > 70:
                preview = preview[:67] + "..."
            notes[rel].append(
                f"linje {first_line}: tekst etter kulepunkt trekkes inn i forklaringen til «{section.points[-1].label}» "
                f"av sync-verktøyet: «{preview}»"
            )

    missing = sum(c["uten forklaring"] for c in per_category.values())
    short = sum(c["for kort"] for c in per_category.values())

    if errors:
        print(f"FEIL: {missing} kapabilitetspunkter i {len(errors)} gjeldende ressursfiler mangler forklaring.\n")
        for rel in sorted(errors, key=lambda r: (category_of(REPO_ROOT / r), r)):
            print(rel)
            for message in errors[rel]:
                print(f"  - {message}")
        print()
        print("Skriv én eller flere setninger under hvert kapabilitetspunkt om hvorfor ressursen")
        print("selv realiserer kapabiliteten, prøvd mot definisjonen i capabilities.yaml.\n")
    else:
        print(f"OK: Alle {total_points} kapabilitetspunkter i {len(entries)} gjeldende ressursfiler har forklaring.")

    print("Fordeling per kategori:")
    for category in sorted(per_category):
        c = per_category[category]
        print(
            f"  {category}: {c['filer']} filer, {c['punkter']} punkter, "
            f"{c['uten forklaring']} uten forklaring i {c['filer med feil']} filer, {c['for kort']} for korte"
        )
    print()

    if warnings or notes:
        print(
            f"{short} advarsler om korte forklaringer i {len(warnings)} filer, "
            f"og {sum(len(v) for v in notes.values())} merknader om tekst etter kulelista."
        )
        if args.advarsler:
            print()
            for rel in sorted(set(warnings) | set(notes)):
                print(rel)
                for message in warnings.get(rel, []):
                    print(f"  - {message}")
                for message in notes.get(rel, []):
                    print(f"  - merknad, {message}")
            print()
        else:
            print("Kjør med --advarsler for å se dem.\n")

    if args.formater:
        print("Kulepunktformater (antall filer som bruker formatet minst én gang):")
        for fmt, files in sorted(formats.items(), key=lambda item: -len(item[1])):
            print(f"  {len(files):4d}  {fmt}")
        print()

    if args.mapping:
        counts, findings, differences = check_mapping(latest, points_by_id)
        print(
            f"Mappingfila: {counts['totalt']} koblinger for gjeldende ressurser, {counts['tom']} tomme, "
            f"{counts['plassholder']} plassholdere og {counts['forurenset']} med tekst trukket inn fra utenfor punktet."
        )
        for finding in findings:
            print(f"  - {finding}")
        print(
            f"  {counts['avviker fra ressursfila']} forklaringer avviker fra ressursfila, og "
            f"{counts['uten punkt i ressursfila']} koblinger har ikke noe tilsvarende punkt i ressursfila."
        )
        if args.advarsler:
            for difference in differences:
                print(f"  - {difference}")
        elif differences:
            print("  Kjør med --advarsler for å se dem.")
        print()

    return 1 if (errors and args.strict) else 0


if __name__ == "__main__":
    sys.exit(main())
