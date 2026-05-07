"""
arkifix-mcp server
Eksponerer nasjonal arkitektur-kunnskapsbase og offentlige API-er til Copilot.
Kjøres lokalt via stdio – ingen porter åpne, ingen data forlater maskinen unødvendig.
"""

import json
import re
from pathlib import Path
import yaml
import httpx
from mcp.server.fastmcp import FastMCP

REPO_ROOT = Path(__file__).parent.parent

mcp = FastMCP("arkifix-mcp")


# ---------------------------------------------------------------------------
# Lokale kunnskapskilder
# ---------------------------------------------------------------------------

@mcp.tool()
def get_capabilities() -> str:
    """
    Returner hele kapabilitetsmodellen for nasjonal arkitektur.
    Bruk dette som grunnlag for arkitekturanalyser og vurdering av hvilke
    kapabiliteter en løsning eller et tiltak berører.
    """
    path = REPO_ROOT / "arkitektur" / "kapabiliteter" / "capabilities.yaml"
    return path.read_text(encoding="utf-8")


@mcp.tool()
def get_principles() -> str:
    """
    Returner de syv arkitekturprinsippene for nasjonal arkitektur.
    Bruk dette til å vurdere om en løsning er i tråd med nasjonale prinsipper.
    """
    path = REPO_ROOT / "arkitektur" / "prinsipper" / "principles.md"
    return path.read_text(encoding="utf-8")


@mcp.tool()
def get_goals() -> str:
    """
    Returner målstrukturen for nasjonal arkitektur.
    Bruk dette til å vurdere om et tiltak bidrar til strategiske mål.
    """
    path = REPO_ROOT / "arkitektur" / "maal" / "maal.md"
    return path.read_text(encoding="utf-8")


@mcp.tool()
def get_product_capability_links() -> str:
    """
    Returner koblinger mellom produkter og kapabiliteter.
    Viser hvilke kapabiliteter hvert produkt dekker.
    Bruk dette til gjenbruksvurderinger og gap-analyser.
    """
    path = REPO_ROOT / "arkitektur" / "kapabiliteter" / "produkt-kapabilitet-koblinger.yaml"
    return path.read_text(encoding="utf-8")


@mcp.tool()
def get_product_register() -> str:
    """
    Returner produktregisteret med alle registrerte ressurser, ID-er og statusoversikt.
    """
    path = REPO_ROOT / "arkitektur" / "ressurser" / "produktnummerering.md"
    return path.read_text(encoding="utf-8")


@mcp.tool()
def search_resources(query: str) -> str:
    """
    Søk i ressursbeskrivelser (operative løsninger, normerende ressurser, samarbeidsfora).
    Returnerer tittel og første 400 tegn av matchende ressurser.

    Args:
        query: Søkeord eller frase, f.eks. "autentisering", "ID-porten", "datadeling"
    """
    results = []
    resource_dirs = [
        REPO_ROOT / "arkitektur" / "ressurser" / "operative-losninger-og-tjenester",
        REPO_ROOT / "arkitektur" / "ressurser" / "normerende-ressurser",
        REPO_ROOT / "arkitektur" / "ressurser" / "samarbeidsfora",
    ]
    query_lower = query.lower()
    for d in resource_dirs:
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            content = f.read_text(encoding="utf-8")
            if query_lower in content.lower():
                # Hent første linje som tittel
                first_line = content.split("\n")[0].lstrip("#").strip()
                snippet = content[:400].replace("\n", " ")
                results.append(f"### {first_line}\nFil: {f.name}\n{snippet}\n")
    if not results:
        return f"Ingen ressurser funnet for søket: '{query}'"
    return f"Fant {len(results)} ressurs(er) for '{query}':\n\n" + "\n---\n".join(results)


@mcp.tool()
def get_resource(filename: str) -> str:
    """
    Hent full innhold av én ressursbeskrivelse basert på filnavn.

    Args:
        filename: Filnavn, f.eks. "01-ID-porten-produkt-canvas-v3-codex.md"
    """
    # Avvis filnavn med path-separatorer for å hindre path traversal
    if "/" in filename or "\\" in filename or filename.startswith("."):
        return "Ugyldig filnavn."
    for subdir in ["operative-losninger-og-tjenester", "normerende-ressurser", "samarbeidsfora"]:
        base = REPO_ROOT / "arkitektur" / "ressurser" / subdir
        path = (base / filename).resolve()
        # Bekreft at den løste stien fortsatt er innenfor forventet mappe
        if not str(path).startswith(str(base.resolve())):
            return "Ugyldig filnavn."
        if path.exists():
            return path.read_text(encoding="utf-8")
    return f"Fant ikke ressursfilen: {filename}"


@mcp.tool()
def list_resources(resource_type: str = "alle") -> str:
    """
    List alle tilgjengelige ressursbeskrivelser.

    Args:
        resource_type: "operative", "normerende", "samarbeidsfora", eller "alle"
    """
    mapping = {
        "operative": ["operative-losninger-og-tjenester"],
        "normerende": ["normerende-ressurser"],
        "samarbeidsfora": ["samarbeidsfora"],
        "alle": ["operative-losninger-og-tjenester", "normerende-ressurser", "samarbeidsfora"],
    }
    dirs = mapping.get(resource_type, mapping["alle"])
    lines = []
    for subdir in dirs:
        d = REPO_ROOT / "arkitektur" / "ressurser" / subdir
        if not d.exists():
            continue
        files = sorted(d.glob("*.md"))
        lines.append(f"\n**{subdir}** ({len(files)} filer):")
        for f in files:
            lines.append(f"  - {f.name}")
    return "\n".join(lines) if lines else "Ingen ressurser funnet."


# ---------------------------------------------------------------------------
# Offentlige API-er – data.norge.no
# ---------------------------------------------------------------------------

@mcp.tool()
def search_norge_datasets(query: str, limit: int = 5) -> str:
    """
    Søk etter åpne datasett på data.norge.no.
    Bruk dette for å finne relevante offentlige datasett knyttet til en ressurs eller et tema.

    Args:
        query: Søkeord, f.eks. "autentisering", "folkeregister", "helse"
        limit: Maks antall resultater (standard 5)
    """
    url = "https://search.api.fellesdatakatalog.digdir.no/search/datasets"
    payload = {"query": query, "pagination": {"size": min(limit, 10), "page": 0}}
    try:
        resp = httpx.post(url, json=payload, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        hits = data.get("hits", [])
        if not hits:
            return f"Ingen datasett funnet for '{query}' på data.norge.no"
        lines = [f"Datasett fra data.norge.no for '{query}':\n"]
        for h in hits:
            title_raw = h.get("title", {})
            title = title_raw.get("nb", title_raw.get("no", title_raw.get("en", "Ukjent tittel")))
            desc_raw = h.get("description", {})
            desc = desc_raw.get("nb", desc_raw.get("no", desc_raw.get("en", "")))[:200]
            org = h.get("organization", {})
            publisher = org.get("name", h.get("publisher", {}).get("name", "Ukjent utgiver"))
            publisher_uri = org.get("uri", h.get("publisher", {}).get("uri", "Ukjent"))
            source_uri = h.get("uri", "Ukjent")
            dataset_id = h.get("id", "")
            catalog_url = f"https://data.norge.no/datasets/{dataset_id}" if dataset_id else "Ukjent"
            modified = h.get("metadata", {}).get("modified", "Ukjent")
            lines.append(
                f"**{title}**\n"
                f"Forvalter: {publisher}\n"
                f"Forvalter-URI: {publisher_uri}\n"
                f"Kilde-URI: {source_uri}\n"
                f"Sist oppdatert: {modified}\n"
                f"Katalog-URL: {catalog_url}\n"
                f"{desc}\n"
            )
        return "\n".join(lines)
    except Exception as e:
        return f"Feil ved oppslag mot data.norge.no: {e}"


@mcp.tool()
def search_norge_concepts(query: str, limit: int = 5) -> str:
    """
    Søk i begrepskatalogen på data.norge.no.
    Bruk dette for å finne offisielle definisjoner av fagtermer.

    Args:
        query: Begrep eller term, f.eks. "autentisering", "datadeling", "tjenesteorientering"
        limit: Maks antall resultater (standard 5)
    """
    url = "https://search.api.fellesdatakatalog.digdir.no/search/concepts"
    payload = {"query": query, "pagination": {"size": min(limit, 10), "page": 0}}
    try:
        resp = httpx.post(url, json=payload, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        hits = data.get("hits", [])
        if not hits:
            return f"Ingen begreper funnet for '{query}' i begrepskatalogen"
        lines = [f"Begreper fra data.norge.no for '{query}':\n"]
        for h in hits:
            title_raw = h.get("title", {})
            term = title_raw.get("nb", title_raw.get("nn", title_raw.get("en", "Ukjent")))
            desc_raw = h.get("description", {})
            defn = desc_raw.get("nb", desc_raw.get("nn", desc_raw.get("en", "Ingen definisjon")))[:300]
            org = h.get("organization", {})
            publisher = org.get("name", "Ukjent")
            publisher_uri = org.get("uri", "Ukjent")
            source_uri = h.get("uri", "Ukjent")
            modified = h.get("metadata", {}).get("modified", "Ukjent")
            lines.append(
                f"**{term}**\n"
                f"Forvalter: {publisher}\n"
                f"Forvalter-URI: {publisher_uri}\n"
                f"Kilde-URI: {source_uri}\n"
                f"Sist oppdatert: {modified}\n"
                f"{defn}\n"
            )
        return "\n".join(lines)
    except Exception as e:
        return f"Feil ved oppslag mot begrepskatalogen: {e}"


# ---------------------------------------------------------------------------
# Brønnøysundregistrene
# ---------------------------------------------------------------------------

@mcp.tool()
def lookup_organization(org_identifier: str) -> str:
    """
    Slå opp en organisasjon i Enhetsregisteret (Brønnøysundregistrene).
    Bruk dette for å finne hvem som eier eller drifter en tjeneste.

    Args:
        org_identifier: Organisasjonsnummer (9 siffer) eller navn, f.eks. "974760673" eller "Digdir"
    """
    # Rens for mellomrom og punktum
    org_nr = re.sub(r"[\s.]", "", org_identifier)
    if org_nr.isdigit() and len(org_nr) == 9:
        url = f"https://data.brreg.no/enhetsregisteret/api/enheter/{org_nr}"
    else:
        url = "https://data.brreg.no/enhetsregisteret/api/enheter"
        params = {"navn": org_identifier, "size": 5}
        try:
            resp = httpx.get(url, params=params, timeout=10)
            resp.raise_for_status()
            data = resp.json()
            enheter = data.get("_embedded", {}).get("enheter", [])
            if not enheter:
                return f"Ingen organisasjon funnet for '{org_identifier}'"
            lines = [f"Søkeresultat for '{org_identifier}':\n"]
            for e in enheter:
                lines.append(
                    f"**{e.get('navn')}** (org.nr: {e.get('organisasjonsnummer')})\n"
                    f"Organisasjonsform: {e.get('organisasjonsform', {}).get('beskrivelse', 'Ukjent')}\n"
                    f"Næring: {e.get('naeringskode1', {}).get('beskrivelse', 'Ukjent')}\n"
                )
            return "\n".join(lines)
        except Exception as ex:
            return f"Feil ved oppslag mot Enhetsregisteret: {ex}"

    try:
        resp = httpx.get(url, timeout=10)
        resp.raise_for_status()
        e = resp.json()
        forretningsadresse = e.get("forretningsadresse", {})
        adresse = ", ".join(filter(None, [
            ", ".join(forretningsadresse.get("adresse", [])),
            forretningsadresse.get("postnummer", ""),
            forretningsadresse.get("poststed", ""),
        ]))
        return (
            f"**{e.get('navn')}**\n"
            f"Org.nr: {e.get('organisasjonsnummer')}\n"
            f"Organisasjonsform: {e.get('organisasjonsform', {}).get('beskrivelse', 'Ukjent')}\n"
            f"Næring: {e.get('naeringskode1', {}).get('beskrivelse', 'Ukjent')}\n"
            f"Adresse: {adresse}\n"
            f"Antall ansatte: {e.get('antallAnsatte', 'Ukjent')}\n"
            f"Registrert: {e.get('registreringsdatoEnhetsregisteret', 'Ukjent')}\n"
            f"Konkurs: {e.get('konkurs', False)}\n"
        )
    except Exception as ex:
        return f"Feil ved oppslag mot Enhetsregisteret: {ex}"


# ---------------------------------------------------------------------------
# SSB
# ---------------------------------------------------------------------------

@mcp.tool()
def search_ssb_statistics(query: str, limit: int = 5) -> str:
    """
    Søk etter statistikk fra Statistisk sentralbyrå (SSB).
    Bruk dette for å finne relevante tall om digitalisering, IKT-bruk og offentlig sektor.

    Args:
        query: Søkeord, f.eks. "IKT offentlig sektor", "digitale tjenester kommuner"
        limit: Maks antall resultater (standard 5)
    """
    url = "https://data.ssb.no/api/v0/no/table/"
    search_url = f"https://data.ssb.no/api/v0/no/table/?query={query}&lang=no"
    try:
        resp = httpx.get(search_url, timeout=10)
        resp.raise_for_status()
        tables = resp.json()
        if not tables:
            return f"Ingen statistikktabeller funnet for '{query}' hos SSB"
        lines = [f"SSB-statistikk for '{query}':\n"]
        for t in tables[:limit]:
            lines.append(
                f"**{t.get('title', 'Ukjent')}**\n"
                f"Tabell-ID: {t.get('id', 'Ukjent')}\n"
                f"Oppdatert: {t.get('updated', 'Ukjent')}\n"
                f"URL: https://www.ssb.no/statbank/table/{t.get('id', '')}\n"
            )
        return "\n".join(lines)
    except Exception as e:
        return f"Feil ved oppslag mot SSB: {e}"


# ---------------------------------------------------------------------------
# Kvalitetssjekk av ressursbeskrivelser
# ---------------------------------------------------------------------------

# Felt som må være substansielt utfylt per mal-type (v1-krav)
_REQUIRED_FIELDS_OPERATIVE = [
    "## Navn",
    "## Ressurs ID",
    "## Status/Livsfase",
    "## Modenhet",
    "## Kort beskrivelse",
    "## Kapabiliteter",
    "## Produktmål",
    "## Brukerbehov",
    "## Hvem er brukerne",
    "## Hovedfunksjoner",
]

_REQUIRED_FIELDS_NORMERENDE = [
    "## Navn",
    "## Ressurs ID",
    "## Status/Livsfase",
    "## Kort beskrivelse",
    "## Formål og normerende rolle",
    "## Forpliktelsesnivå",
    "## Kapabiliteter",
    "## Målgruppe",
    "## Normerende innhold",
    "## Bruksområde",
    "## Scope og avgrensning",
    "## Relasjon til andre ressurser",
    "## Lenke til dokumentasjon",
]

_REQUIRED_FIELDS_SAMARBEIDSFORUM = [
    "## Navn",
    "## Ressurs ID",
    "## Status/Livsfase",
    "## Kort beskrivelse",
    "## Formål",
    "## Kapabiliteter",
    "## Medlemmer",
    "## Mandat",
    "## Møtestruktur",
]

# Markører for ufullstendige felt
_INCOMPLETE_MARKERS = [
    "foreløpig ikke fylt ut",
    "tbd",
    "todo",
    "ikke fastsatt ennå",
    "under utarbeidelse",
    "[fyll inn",
    "ikke utfylt",
]

_RESOURCE_SUBDIRS = [
    "operative-losninger-og-tjenester",
    "normerende-ressurser",
    "samarbeidsfora",
]

# Kanoniske kapabilitetsnavn (hentes dynamisk fra capabilities.yaml)
def _load_canonical_capability_names() -> set:
    path = REPO_ROOT / "arkitektur" / "kapabiliteter" / "capabilities.yaml"
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        names = set()
        for kap in data.get("kapabilitetsmodell", {}).get("kapabiliteter", []):
            names.add(kap["navn"])
            for del_kap in kap.get("delkapabiliteter", []):
                names.add(del_kap["navn"])
        return names
    except Exception:
        return set()


def _extract_resource_id_and_version(filename: str) -> tuple[str | None, int]:
    """Hent ressurs-ID (løpenummer) og major-versjon fra filnavn."""
    id_match = re.match(r"^(\d+)-", filename)
    version_match = re.search(r"-v(\d+)(?:[.-]|$)", filename, re.IGNORECASE)
    resource_id = id_match.group(1) if id_match else None
    version = int(version_match.group(1)) if version_match else 0
    return resource_id, version


def _collect_resource_files(latest_only: bool) -> list[tuple[str, str]]:
    """Samle filer på tvers av ressurskategorier.

    Returnerer liste med (subdir, filename).
    """
    if not latest_only:
        all_files: list[tuple[str, str]] = []
        for subdir in _RESOURCE_SUBDIRS:
            base = REPO_ROOT / "arkitektur" / "ressurser" / subdir
            if not base.exists():
                continue
            for path in sorted(base.glob("*.md")):
                if not re.match(r"^\d+-.*\.md$", path.name):
                    continue
                all_files.append((subdir, path.name))
        return all_files

    # Velg én siste versjon per ressurs-ID innen hver ressurskategori.
    latest: dict[tuple[str, str], tuple[int, str]] = {}
    for subdir in _RESOURCE_SUBDIRS:
        base = REPO_ROOT / "arkitektur" / "ressurser" / subdir
        if not base.exists():
            continue
        for path in sorted(base.glob("*.md")):
            if not re.match(r"^\d+-.*\.md$", path.name):
                continue
            resource_id, version = _extract_resource_id_and_version(path.name)
            if resource_id is None:
                # Fallback for filer uten nummerering i navnet.
                key = (subdir, path.name)
            else:
                key = (subdir, resource_id)
            current = latest.get(key)
            if current is None or version > current[0] or (version == current[0] and path.name > current[1]):
                latest[key] = (version, path.name)

    selected: list[tuple[str, str]] = []
    for key, value in latest.items():
        subdir = key[0]
        filename = value[1]
        selected.append((subdir, filename))
    selected.sort(key=lambda item: (item[0], item[1]))
    return selected


@mcp.tool()
def check_resource_completeness(filename: str) -> str:
    """
    Sjekk kvaliteten og fullstendigheten av en ressursbeskrivelse.
    Kontrollerer at obligatoriske felt er til stede og substansielt utfylt,
    at kapabiliteter bruker kanoniske navn, og at ingen felt inneholder
    ufullstendige plassholdere.

    Støtter operative ressurser, normerende ressurser og samarbeidsfora.
    Kapabiliteter merket med selvstendig: true i capabilities.yaml er gyldige
    operative enheter på lik linje med delkapabiliteter.

    Args:
        filename: Filnavn, f.eks. "01-ID-porten-produkt-canvas-v3-codex.md"
    """
    if "/" in filename or "\\" in filename or filename.startswith("."):
        return "Ugyldig filnavn."

    content = None
    for subdir in _RESOURCE_SUBDIRS:
        base = REPO_ROOT / "arkitektur" / "ressurser" / subdir
        path = (base / filename).resolve()
        if not str(path).startswith(str(base.resolve())):
            return "Ugyldig filnavn."
        if path.exists():
            content = path.read_text(encoding="utf-8")
            resource_type = subdir
            break

    if content is None:
        return f"Fant ikke ressursfilen: {filename}"

    # Velg riktig sjekkliste basert på type
    if resource_type == "operative-losninger-og-tjenester":
        required = _REQUIRED_FIELDS_OPERATIVE
        type_label = "Operativ ressurs"
    elif resource_type == "normerende-ressurser":
        required = _REQUIRED_FIELDS_NORMERENDE
        type_label = "Normerende ressurs"
    else:
        required = _REQUIRED_FIELDS_SAMARBEIDSFORUM
        type_label = "Samarbeidsforum"

    issues = []
    warnings = []
    content_lower = content.lower()

    # 1. Sjekk at obligatoriske seksjoner finnes
    for field in required:
        if field.lower() not in content_lower:
            issues.append(f"Mangler seksjon: `{field}`")

    # 2. Sjekk at felt ikke er tomme eller inneholder plassholdere
    lines = content.split("\n")
    current_heading = None
    heading_content: dict[str, list] = {}
    for line in lines:
        if line.startswith("## "):
            current_heading = line.strip()
            heading_content[current_heading] = []
        elif current_heading:
            heading_content[current_heading].append(line)

    # Felt der én linje med verdi er tilstrekkelig
    _SHORT_OK = {"## navn", "## ressurs id", "## ressurskategori",
                 "## status/livsfase", "## type normerende ressurs", "## modenhet"}

    for heading, body_lines in heading_content.items():
        body = " ".join(body_lines).strip()
        min_len = 2 if heading.lower() in _SHORT_OK else 20
        if len(body) < min_len:
            issues.append(f"Feltinnhold for kort (muligens tomt): `{heading}`")
        else:
            for marker in _INCOMPLETE_MARKERS:
                if marker in body.lower():
                    warnings.append(f"Mulig plassholder i `{heading}`: inneholder «{marker}»")
                    break

    # 3. Sjekk kapabilitetsnavn mot kanonisk liste
    canonical = _load_canonical_capability_names()
    if canonical:
        kap_section = heading_content.get("## Kapabiliteter", [])
        kap_text = "\n".join(kap_section)
        # Finn bold-markerte kapabilitetsnavn: **Navn**
        mentioned = re.findall(r"\*\*([^*]+)\*\*", kap_text)
        # Filtrer bort → (arrownotasjon brukes for delkapabiliteter)
        mentioned_names = [m.split("→")[-1].strip() for m in mentioned]
        non_canonical = [n for n in mentioned_names if n and n not in canonical]
        if non_canonical:
            warnings.append(
                f"Mulige ikke-kanoniske kapabilitetsnavn i Kapabiliteter-seksjonen: "
                + ", ".join(f"«{n}»" for n in non_canonical[:8])
            )

    # 4. Versjon
    version_match = re.search(r"v(\d+)\.?(\d*)", filename)
    if version_match:
        major = int(version_match.group(1))
        if major >= 1 and issues:
            warnings.insert(0, f"⚠️ Filen er merket som v{major}, men har {len(issues)} manglende felt.")

    # Bygg rapport
    title = lines[0].lstrip("#").strip() if lines else filename
    result = [f"## Kvalitetssjekk: {title}", f"Type: {type_label} | Fil: {filename}", ""]

    if not issues and not warnings:
        result.append("✅ Ingen problemer funnet. Ressursen ser fullstendig ut.")
    else:
        if issues:
            result.append(f"### ❌ Mangler ({len(issues)})")
            for i in issues:
                result.append(f"- {i}")
            result.append("")
        if warnings:
            result.append(f"### ⚠️ Advarsler ({len(warnings)})")
            for w in warnings:
                result.append(f"- {w}")

    result.append("")
    result.append(
        f"Totalt: {len(issues)} mangler, {len(warnings)} advarsler. "
        f"Sjekket mot mal for «{type_label}»."
    )
    return "\n".join(result)


@mcp.tool()
def check_all_resources_completeness(latest_only: bool = True) -> str:
    """
    Sjekk fullstendighet for alle ressursbeskrivelser.

    Som standard sjekkes kun siste versjon per ressurs-ID i hver kategori.

    Args:
        latest_only: Hvis true, sjekk kun siste versjon per ressurs-ID.
    """
    files = _collect_resource_files(latest_only=latest_only)
    if not files:
        return "Fant ingen ressursfiler å sjekke."

    summary_lines = [
        "## Porteføljeanalyse: Fullstendighet av ressursbeskrivelser",
        f"Totalt vurderte filer: {len(files)}",
        f"Modus: {'Siste versjon per ressurs-ID' if latest_only else 'Alle versjoner'}",
        "",
    ]

    total_missing = 0
    total_warnings = 0
    with_missing: list[tuple[str, int, int]] = []

    for _, filename in files:
        report = check_resource_completeness(filename)
        match = re.search(r"Totalt:\s*(\d+) mangler,\s*(\d+) advarsler", report)
        if not match:
            continue
        missing = int(match.group(1))
        warnings = int(match.group(2))
        total_missing += missing
        total_warnings += warnings
        if missing > 0 or warnings > 0:
            with_missing.append((filename, missing, warnings))

    summary_lines.append(f"Sum mangler: {total_missing}")
    summary_lines.append(f"Sum advarsler: {total_warnings}")
    summary_lines.append(f"Filer med funn: {len(with_missing)}")
    summary_lines.append("")

    if not with_missing:
        summary_lines.append("✅ Ingen mangler eller advarsler funnet i valgt utvalg.")
        return "\n".join(summary_lines)

    with_missing.sort(key=lambda item: (-(item[1] + item[2]), item[0]))
    summary_lines.append("### Filer med funn")
    for filename, missing, warnings in with_missing:
        summary_lines.append(f"- {filename}: {missing} mangler, {warnings} advarsler")

    return "\n".join(summary_lines)


# ---------------------------------------------------------------------------
# Eurostat
# ---------------------------------------------------------------------------

_EUROSTAT_ALLOWED_DATASETS = frozenset({
    "isoc_ciegi_ac",  # E-forvaltning: individers bruk av offentlige nettsider
    "isoc_ciweb",     # Bruk av nettskytjenester, offentlig sektor
    "desi_4b1",       # DESI – digital offentlig sektor
})


@mcp.tool()
def get_eurostat_statistics(dataset: str, since_year: int = 2024) -> str:
    """
    Hent statistikk fra Eurostat for sammenligning av norsk digital modenhet mot EU27.
    Filtrerer automatisk på Norge (NO) og EU27 (EU27_2020), enhet: % av individer.

    Tilgjengelige datasett:
    - isoc_ciegi_ac: E-forvaltning – individers bruk av offentlige nettsider
    - isoc_ciweb:    Nettskytjenester i offentlig sektor
    - desi_4b1:      DESI – digital offentlig sektor

    Args:
        dataset:    Eurostat datasett-kode (se liste over)
        since_year: Vis data fra og med dette året (standard 2024)
    """
    if dataset not in _EUROSTAT_ALLOWED_DATASETS:
        allowed = ", ".join(sorted(_EUROSTAT_ALLOWED_DATASETS))
        return f"Ikke tillatt datasett. Tillatte koder: {allowed}"
    if not isinstance(since_year, int) or since_year < 2000 or since_year > 2035:
        return "Ugyldig årstall."
    url = (
        f"https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/"
        f"{dataset}?format=JSON&lang=en&sinceTimePeriod={since_year}&unit=PC_IND&ind_type=IND_TOTAL"
    )
    try:
        resp = httpx.get(url, timeout=20)
        resp.raise_for_status()
        data = resp.json()
        dims = data.get("dimension", {})
        ind_labels = dims.get("indic_is", {}).get("category", {}).get("label", {})
        ind_idx    = dims.get("indic_is", {}).get("category", {}).get("index", {})
        geo_idx    = dims.get("geo",      {}).get("category", {}).get("index", {})
        time_idx   = dims.get("time",     {}).get("category", {}).get("index", {})
        values     = data.get("value", {})
        n_ind = len(ind_idx)
        n_geo = len(geo_idx)
        n_time = len(time_idx)
        label = data.get("label", dataset)
        TARGET = {"NO", "EU27_2020"}
        time_keys = list(time_idx.keys())
        header_cols = "  ".join(
            f"{g.replace('EU27_2020', 'EU27')} {t}" for g in ["NO", "EU27_2020"] for t in time_keys
        )
        lines = [
            f"**{label}** (Eurostat: {dataset}, enhet: % av individer)",
            f"{'Indikator':<60}  {header_cols}",
        ]
        for ind_code, i_ind in ind_idx.items():
            lbl = ind_labels.get(ind_code, ind_code)[:58]
            row = {}
            for geo_code, i_geo in geo_idx.items():
                if geo_code not in TARGET:
                    continue
                for t_code, i_time in time_idx.items():
                    key = str(i_ind * n_geo * n_time + i_geo * n_time + i_time)
                    row[f"{geo_code}_{t_code}"] = values.get(key)
            vals = []
            for geo in ["NO", "EU27_2020"]:
                for t in time_keys:
                    v = row.get(f"{geo}_{t}")
                    vals.append(f"{v:>7.1f}" if v is not None else "      -")
            lines.append(f"{lbl:<60}  {'  '.join(vals)}")
            if len(lines) > 42:  # Begrens output til ~40 indikatorer
                lines.append(f"... ({len(ind_idx) - 40} flere indikatorer utelatt)")
                break
        return "\n".join(lines)
    except Exception as e:
        return f"Feil ved oppslag mot Eurostat: {e}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
