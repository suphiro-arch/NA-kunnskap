# Struktur og bearbeiding av arkitekturgrunnlaget

Denne beskrivelsen forklarer hvordan rÃ¥data, kuraterte arbeidsfiler og videre bruk henger sammen i repoet.

## 1. RÃ¥kilder

RÃ¥kilder ligger i `sources/`.

Viktigste rÃ¥kilde for kapabiliteter og prinsipper:
- `sources/2025-03-18-Nasjonal Arkitektur.xml`

Dette er en modellfil som inneholder mer enn det repoet faktisk skal bruke videre. Den har ogsÃ¥ hjelpeelementer, generiske objekter og kopier som ikke bÃ¸r gÃ¥ rett inn i dokumentasjon og web.

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
- prinsippfaglig forklaring som tidligere lÃ¥ duplisert i `capabilities.yaml`

### MÃ¥l
- `arkitektur/maal/maal.md`

Denne fila er den kuraterte arbeidsfila for:
- overordnet mÃ¥lspor i arkitekturmodellen
- strategiske mÃ¥l som er eksplisitt koblet til nasjonal arkitektur i XML-kilden
- dokumentasjon av hva som faktisk er modellert, og hva som ikke er kuratert videre ennÃ¥

### Produkter og koblinger
- `arkitektur/ressurser/produktnummerering.md`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`

Disse filene brukes videre for ressursoversikt, produktkoblinger og webnavigasjon.

## 3. Produktbeskrivelser og leveransefiler

Produktbeskrivelsene ligger i `arkitektur/ressurser/operative-losninger-og-tjenester/`.

Ã˜vrige leveranser ligger fortsatt i `results/`.

Produktbeskrivelsene skal bruke:
- `capabilities.yaml` for kapabilitetsnavn
- `principles.md` for prinsippnavn og prinsippgrunnlag
- `produktnummerering.md` for ressurs-ID og registerinformasjon

## 4. Bruk i webprototypen

Hugo-prototypen ligger i `web/hugo-prototype/`.

FÃ¸lgende arbeidsfiler brukes videre mot web:
- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/prinsipper/principles.md`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
- `arkitektur/ressurser/operative-losninger-og-tjenester/`

ForelÃ¸pig brukes ikke mÃ¥lsporet direkte i weben, men det er nÃ¥ dokumentert og kuratert i:
- `arkitektur/maal/maal.md`

Prinsippsiden i weben synkes fra:
- `arkitektur/prinsipper/principles.md`

Kapabilitetssidene genereres fra:
- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
- `arkitektur/ressurser/operative-losninger-og-tjenester/`

Produktsiden genereres fra:
- `arkitektur/ressurser/operative-losninger-og-tjenester/`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`

## 5. Praktisk regel

NÃ¥r rÃ¥kilder og kuraterte filer avviker:

1. RÃ¥kilden skal ikke brukes direkte som publiseringsgrunnlag.
2. Avvik skal vurderes og dokumenteres.
3. De kuraterte filene i `arkitektur/` er styrende for videre analyser, produktbeskrivelser og web.

