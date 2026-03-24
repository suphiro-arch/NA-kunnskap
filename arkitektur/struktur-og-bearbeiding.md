# Struktur og bearbeiding av arkitekturgrunnlaget

Denne beskrivelsen forklarer hvordan rådata, kuraterte arbeidsfiler og videre bruk henger sammen i repoet.

## 1. Råkilder

Råkilder ligger i `sources/`.

Viktigste råkilde for kapabiliteter og prinsipper:
- `sources/2025-03-18-Nasjonal Arkitektur.xml`

Dette er en modellfil som inneholder mer enn det repoet faktisk skal bruke videre. Den har også hjelpeelementer, generiske objekter og kopier som ikke bør gå rett inn i dokumentasjon og web.

## 2. Kuraterte arbeidsfiler

Repoet bruker egne kuraterte arbeidsfiler i `arkitektur/` for det som skal brukes videre i analyser og publisering.

### Kapabiliteter
- `arkitektur/kapabiliteter/capabilities.yaml`

Denne fila er den kuraterte arbeidsfila for:
- hovedkapabiliteter
- delkapabiliteter
- lokal kobling fra hver hovedkapabilitet til relevante prinsipp-ID-er

### Prinsipper
- `arkitektur/prinsipper/principles.md`

Denne fila er den kuraterte arbeidsfila for:
- operative prinsippnavn
- kort forklaring av prinsippene
- kobling mellom prinsipper og hovedkapabiliteter
- prinsippfaglig forklaring som tidligere lå duplisert i `capabilities.yaml`

### Mål
- `arkitektur/maal/maal.md`

Denne fila er den kuraterte arbeidsfila for:
- overordnet målspor i arkitekturmodellen
- strategiske mål som er eksplisitt koblet til nasjonal arkitektur i XML-kilden
- dokumentasjon av hva som faktisk er modellert, og hva som ikke er kuratert videre ennå

### Produkter og koblinger
- `arkitektur/produkter/produktnummerering.md`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`

Disse filene brukes videre for ressursoversikt, produktkoblinger og webnavigasjon.

## 3. Produktbeskrivelser og leveransefiler

Produktbeskrivelsene ligger i `arkitektur/produkter/produktbeskrivelser/`.

Øvrige leveranser ligger fortsatt i `results/`.

Produktbeskrivelsene skal bruke:
- `capabilities.yaml` for kapabilitetsnavn
- `principles.md` for prinsippnavn og prinsippgrunnlag
- `produktnummerering.md` for ressurs-ID og registerinformasjon

## 4. Bruk i webprototypen

Hugo-prototypen ligger i `web/hugo-prototype/`.

Følgende arbeidsfiler brukes videre mot web:
- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/prinsipper/principles.md`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
- `arkitektur/produkter/produktbeskrivelser/`

Foreløpig brukes ikke målsporet direkte i weben, men det er nå dokumentert og kuratert i:
- `arkitektur/maal/maal.md`

Prinsippsiden i weben synkes fra:
- `arkitektur/prinsipper/principles.md`

Kapabilitetssidene genereres fra:
- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
- `arkitektur/produkter/produktbeskrivelser/`

Produktsiden genereres fra:
- `arkitektur/produkter/produktbeskrivelser/`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`

## 5. Praktisk regel

Når råkilder og kuraterte filer avviker:

1. Råkilden skal ikke brukes direkte som publiseringsgrunnlag.
2. Avvik skal vurderes og dokumenteres.
3. De kuraterte filene i `arkitektur/` er styrende for videre analyser, produktbeskrivelser og web.
