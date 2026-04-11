# Mal: arkitekturassistert analyse av utviklingsbehov

Formål med malen:
- kunne brukes som rask analyse
- kunne utvides til beslutningsgrunnlag
- sikre sporbar kobling mellom case, kapabiliteter, prinsipper og produkter i dette repoet

Bruk denne malen sammen med:
- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/prinsipper/principles.md`
- `arkitektur/ressurser/produktnummerering.md`
- `arkitektur/ressurser/operative-losninger-og-tjenester/`
- `arkitektur/ressurser/normerende-ressurser/` (kun når standarder/retningslinjer faktisk påvirker tiltaket)
- `arkitektur/ressurser/samarbeidsfora/` (kun når koordinering mellom aktører er en tydelig forutsetning)

Viktig avgrensning:
- Velg et spisset utvalg av de mest relevante ressursene for caset.
- Ikke list opp alt som kan være interessant.
- Begrunn kort hvorfor hver valgt ressurs er tatt med.

## 1. Formål

Hjelpetekst: Beskriv hvorfor analysen gjennomføres, hvilket beslutningsbehov den skal dekke, og hvilken styring den skal understøtte.

- Analyseformål: [Sett inn]
- Beslutning analysen skal understøtte: [Sett inn]
- Avgrensning: [Sett inn]

## 2. Input / casebeskrivelse

Hjelpetekst: Beskriv caset kort og presist. Hold fokus på behov, ikke løsning.

- Case-tittel: [Sett inn]
- Kort casebeskrivelse: [Sett inn]
- Berørte livshendelser / tjenester / overganger: [Sett inn]
- Hovedutfordring i caset: [Sett inn]
- Kildemateriale brukt: [Sett inn]

## 2.1 Inputgrunnlag og analysetillit

Hjelpetekst: Vurder hvor solid inputgrunnlaget er, og hvor sikker konklusjonen kan være. Skill mellom usikkerhet i input, produktgrunnlag og juridisk/organisatorisk avklaring.

| Vurderingspunkt | Vurdering |
|---|---|
| Inputgrunnlag | [Sett inn] |
| Datagrunnlag | [Sett inn] |
| Produktgrunnlag | [Sett inn] |
| Samlet analysetillit (høy/middels/lav) | [Sett inn] |

Viktigste usikkerheter (minst 3):
- [Sett inn]
- [Sett inn]
- [Sett inn]

### 2.2 Avklaring: ett case eller flere

Hjelpetekst: Avklar tidlig om innsendt tekst egentlig inneholder flere problemstillinger eller overganger. Hvis ja, splitt analysen før videre arbeid.

- Er dette ett case eller flere separate case: [Sett inn]
- Begrunnelse for vurderingen: [Sett inn]
- Skal analysen splittes: [Ja/nei]
- Hvis ja, navngi delcasene: [Sett inn]

## 3. Målgruppe og styringsnivå

Hjelpetekst: Angi hvem analysen skal skape verdi for, og hvilket nivå tiltakene skal styres på.

- Primær målgruppe: [Sett inn]
- Sekundær målgruppe: [Sett inn]
- Styringsnivå (nasjonalt / sektor / virksomhet): [Sett inn]
- Viktig avgrensning for tiltak: [Sett inn]

## 4. Problembilde

Hjelpetekst: Oppsummer problemet og konsekvensene før du vurderer tiltak.

### 4.1 Hovedproblem

[Sett inn 3-6 setninger]

### 4.2 Konsekvenser for målgrupper

- [Sett inn]
- [Sett inn]
- [Sett inn]

### 4.3 Konsekvenser for forvaltning og tjenesteutøvelse

- [Sett inn]
- [Sett inn]
- [Sett inn]

## 5. Kapabilitetsanalyse

Hjelpetekst: Koble caset direkte til kapabiliteter i `capabilities.yaml`. Vurder både relevans, gap og konsekvens.

| Kapabilitet | Relevans (høy/middels/lav) | Hva finnes i dag | Identifisert gap | Konsekvens for caset |
|---|---|---|---|---|
| [Kapabilitet] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] |
| [Kapabilitet] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] |

### Oppsummering av kapabilitetsgap

- Viktigste gap 1: [Sett inn]
- Viktigste gap 2: [Sett inn]
- Viktigste gap 3: [Sett inn]

## 6. Prinsippvurdering

Hjelpetekst: Vurder kun prinsipper som finnes i `principles.md`. Beskriv hvordan caset støtter, utfordrer eller bryter prinsippene.

| Prinsipp | Status (oppfylt/delvis/brutt) | Hva finnes i dag | Hvordan caset utfordrer prinsippet |
|---|---|---|---|
| [Prinsipp] | [Sett inn] | [Sett inn] | [Sett inn] |
| [Prinsipp] | [Sett inn] | [Sett inn] | [Sett inn] |

### Oppsummering av prinsippvurdering

[Sett inn kort oppsummering]

## 7. Produktvurdering

Hjelpetekst: Bruk produktkatalogen som fasit for hva som finnes. Vurder relevante produkter systematisk og skill tydelig mellom gjenbruk, videreutvikling, ikke relevant og mangler.

### 7.0 Vurderingsrekkefølge for produktkategorier

Hjelpetekst: Gå gjennom kategoriene i denne rekkefølgen for å sikre lik metode mellom analyser.
Viktig: Bruk `produktnummerering.md` som oversikt over hva som finnes, men begrunn produktvalg med innhold fra den konkrete produktbeskrivelsen der den finnes.
Hvis produktbeskrivelsen mangler eller er for tynn, marker vurderingen som usikker.

1. Identitet og representasjon (for eksempel Feide, ID-porten, Altinn Autorisasjon)
2. Datadeling og integrasjon (for eksempel Maskinporten, data.altinn.no, eFormidling)
3. Hendelser og meldinger (for eksempel Altinn Events, Altinn Melding, FIKS Melding)
4. Dialog og brukerflate (for eksempel Dialogporten, portaler)
5. Register og datagrunnlag (for eksempel Folkeregisteret, NVB, sektorrelevante registre)
6. Katalog og semantikk (for eksempel Felles datakatalog, Begrepskatalog, API-katalog)
7. Sektorprodukter og domeneprodukter (for eksempel opptaksløsninger, fagsystemnære fellesløsninger)

### 7.1 Vurderte produkter fra katalogen

| Produkt (fra produktkatalogen) | Produktkategori | Relevans for caset | Klassifisering (brukes direkte/videreutvikles/ikke relevant) | Begrunnelse |
|---|---|---|---|---|
| [Produkt] | [Sett inn] | [Høy/middels/lav] | [Sett inn] | [Sett inn] |
| [Produkt] | [Sett inn] | [Høy/middels/lav] | [Sett inn] | [Sett inn] |

### 7.2 Oppsummering: hva finnes, hva kan gjenbrukes, hva må videreutvikles

- Hva finnes: [Sett inn]
- Hva kan gjenbrukes direkte: [Sett inn]
- Hva må videreutvikles: [Sett inn]
- Hva er ikke relevant i dette caset: [Sett inn]

### 7.3 Eksplisitte mangler og behov for nye/sammensatte løsninger

| Identifisert mangel | Hvorfor mangelen oppstår | Konsekvens hvis ikke løst | Forslag til ny/sammensatt løsning | Kan bygge på eksisterende produkter |
|---|---|---|---|---|
| [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] |

### 7.4 Sammensatte løsningsmønstre

Hjelpetekst: Beskriv kombinasjoner av produkter som samlet kan løse behovet. Dette skal brukes før du foreslår nye produkter.

| Løsningsmønster | Produkter som inngår | Hva mønsteret dekker | Hva som fortsatt mangler |
|---|---|---|---|
| [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] |

## 8. Tiltak prioritert etter effekt

Hjelpetekst: Tiltak skal være sporbare til kapabilitetsgap, prinsippvurdering og produktvurdering.

### 8.0 Gap-type per tiltak

Hjelpetekst: Klassifiser hvert tiltak med primær gap-type for å unngå at alle tiltak blir behandlet som teknisk utvikling.

Tillatte gap-typer:
- Produktgap
- Semantisk gap
- Juridisk gap
- Samordningsgap

| Tiltak | Type (gjenbruk/videreutvikling/nyutvikling/avklaring) | Forventet effekt (høy/middels/lav) | Tidshorisont (kort/middels/lang) | Avhengigheter | Kobling til kapabilitet/prinsipp/produkt | Primær gap-type |
|---|---|---|---|---|---|---|
| [Tiltak] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] |
| [Tiltak] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] |

### Prioritert liste

1. [Tiltak] - Begrunnelse: [Sett inn]
2. [Tiltak] - Begrunnelse: [Sett inn]
3. [Tiltak] - Begrunnelse: [Sett inn]

## 9. Strategisk vurdering

Hjelpetekst: Løft analysen til styringsnivå. Beskriv konsekvenser for portefølje, nasjonal retning og samordning.

- Betydning for porteføljeprioritering: [Sett inn]
- Betydning for nasjonal arkitektur/felles retning: [Sett inn]
- Behov for samordning mellom aktører: [Sett inn]

## 10. Konklusjon

Hjelpetekst: Oppsummer i 5-8 setninger med tydelig svar på hva som bør gjøres videre.

[Sett inn]

### 10.1 Spørsmål til videre diskusjon

Hjelpetekst: List opp 3-7 konkrete spørsmål som hjelper beslutningstakere med å avklare retning, ansvar, avhengigheter og prioritering.

1. [Sett inn]
2. [Sett inn]
3. [Sett inn]

## 11. Kortversjon for ledelse

Hjelpetekst: Brukes når analysen skal leses raskt i styringsmøter.

- Case: [Sett inn]
- Analysetillit: [Høy/middels/lav]
- Hovedfunn (1-3 setninger): [Sett inn]
- Viktigste kapabilitetsgap: [Sett inn]
- Mest relevante produkter for gjenbruk: [Sett inn]
- Hva mangler: [Sett inn]
- Anbefalt prioritering:
  1. [Sett inn]
  2. [Sett inn]
  3. [Sett inn]

## Bruksnivå (rask analyse og beslutningsgrunnlag)

### Nivå 1 - rask analyse

Minimum som fylles ut:
- inputgrunnlag og analysetillit (inkludert minst tre konkrete usikkerheter)
- problembilde
- kapabilitetsanalyse
- prinsippvurdering
- foreløpig produktvurdering
- minst ett sammensatt løsningsmønster (eller tydelig begrunnelse for hvorfor dette ikke er mulig nå)
- prioriterte tiltak

### Nivå 2 - beslutningsgrunnlag

Utvid med:
- full produktvurdering av relevante produktkategorier
- eksplisitte mangler og behov for nye/sammensatte løsninger
- strategisk vurdering
- kortversjon for ledelse


