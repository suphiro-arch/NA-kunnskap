# Mal: arkitekturassistert analyse av utviklingsbehov

FormÃ¥l med malen:
- kunne brukes som rask analyse
- kunne utvides til beslutningsgrunnlag
- sikre sporbar kobling mellom case, kapabiliteter, prinsipper og produkter i dette repoet

Bruk denne malen sammen med:
- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/prinsipper/principles.md`
- `arkitektur/ressurser/produktnummerering.md`
- `arkitektur/ressurser/operative-losninger-og-tjenester/`

## 1. FormÃ¥l

Hjelpetekst: Beskriv hvorfor analysen gjennomfÃ¸res, hvilket beslutningsbehov den skal dekke, og hvilken styring den skal understÃ¸tte.

- AnalyseformÃ¥l: [Sett inn]
- Beslutning analysen skal understÃ¸tte: [Sett inn]
- Avgrensning: [Sett inn]

## 2. Input / casebeskrivelse

Hjelpetekst: Beskriv caset kort og presist. Hold fokus pÃ¥ behov, ikke lÃ¸sning.

- Case-tittel: [Sett inn]
- Kort casebeskrivelse: [Sett inn]
- BerÃ¸rte livshendelser / tjenester / overganger: [Sett inn]
- Hovedutfordring i caset: [Sett inn]
- Kildemateriale brukt: [Sett inn]

## 2.1 Inputgrunnlag og analysetillit

Hjelpetekst: Vurder hvor solid inputgrunnlaget er, og hvor sikker konklusjonen kan vÃ¦re. Skill mellom usikkerhet i input, produktgrunnlag og juridisk/organisatorisk avklaring.

| Vurderingspunkt | Vurdering |
|---|---|
| Inputgrunnlag | [Sett inn] |
| Datagrunnlag | [Sett inn] |
| Produktgrunnlag | [Sett inn] |
| Samlet analysetillit (hÃ¸y/middels/lav) | [Sett inn] |

Viktigste usikkerheter (minst 3):
- [Sett inn]
- [Sett inn]
- [Sett inn]

### 2.2 Avklaring: ett case eller flere

Hjelpetekst: Avklar tidlig om innsendt tekst egentlig inneholder flere problemstillinger eller overganger. Hvis ja, splitt analysen fÃ¸r videre arbeid.

- Er dette ett case eller flere separate case: [Sett inn]
- Begrunnelse for vurderingen: [Sett inn]
- Skal analysen splittes: [Ja/nei]
- Hvis ja, navngi delcasene: [Sett inn]

## 3. MÃ¥lgruppe og styringsnivÃ¥

Hjelpetekst: Angi hvem analysen skal skape verdi for, og hvilket nivÃ¥ tiltakene skal styres pÃ¥.

- PrimÃ¦r mÃ¥lgruppe: [Sett inn]
- SekundÃ¦r mÃ¥lgruppe: [Sett inn]
- StyringsnivÃ¥ (nasjonalt / sektor / virksomhet): [Sett inn]
- Viktig avgrensning for tiltak: [Sett inn]

## 4. Problembilde

Hjelpetekst: Oppsummer problemet og konsekvensene fÃ¸r du vurderer tiltak.

### 4.1 Hovedproblem

[Sett inn 3-6 setninger]

### 4.2 Konsekvenser for mÃ¥lgrupper

- [Sett inn]
- [Sett inn]
- [Sett inn]

### 4.3 Konsekvenser for forvaltning og tjenesteutÃ¸velse

- [Sett inn]
- [Sett inn]
- [Sett inn]

## 5. Kapabilitetsanalyse

Hjelpetekst: Koble caset direkte til kapabiliteter i `capabilities.yaml`. Vurder bÃ¥de relevans, gap og konsekvens.

| Kapabilitet | Relevans (hÃ¸y/middels/lav) | Hva finnes i dag | Identifisert gap | Konsekvens for caset |
|---|---|---|---|---|
| [Kapabilitet] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] |
| [Kapabilitet] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] |

### Oppsummering av kapabilitetsgap

- Viktigste gap 1: [Sett inn]
- Viktigste gap 2: [Sett inn]
- Viktigste gap 3: [Sett inn]

## 6. Prinsippvurdering

Hjelpetekst: Vurder kun prinsipper som finnes i `principles.md`. Beskriv hvordan caset stÃ¸tter, utfordrer eller bryter prinsippene.

| Prinsipp | Status (oppfylt/delvis/brutt) | Hva finnes i dag | Hvordan caset utfordrer prinsippet |
|---|---|---|---|
| [Prinsipp] | [Sett inn] | [Sett inn] | [Sett inn] |
| [Prinsipp] | [Sett inn] | [Sett inn] | [Sett inn] |

### Oppsummering av prinsippvurdering

[Sett inn kort oppsummering]

## 7. Produktvurdering

Hjelpetekst: Bruk produktkatalogen som fasit for hva som finnes. Vurder relevante produkter systematisk og skill tydelig mellom gjenbruk, videreutvikling, ikke relevant og mangler.

### 7.0 VurderingsrekkefÃ¸lge for produktkategorier

Hjelpetekst: GÃ¥ gjennom kategoriene i denne rekkefÃ¸lgen for Ã¥ sikre lik metode mellom analyser.
Viktig: Bruk `produktnummerering.md` som oversikt over hva som finnes, men begrunn produktvalg med innhold fra den konkrete produktbeskrivelsen der den finnes.
Hvis produktbeskrivelsen mangler eller er for tynn, marker vurderingen som usikker.

1. Identitet og representasjon (for eksempel Feide, ID-porten, Altinn Autorisasjon)
2. Datadeling og integrasjon (for eksempel Maskinporten, data.altinn.no, eFormidling)
3. Hendelser og meldinger (for eksempel Altinn Events, Altinn Melding, FIKS Melding)
4. Dialog og brukerflate (for eksempel Dialogporten, portaler)
5. Register og datagrunnlag (for eksempel Folkeregisteret, NVB, sektorrelevante registre)
6. Katalog og semantikk (for eksempel Felles datakatalog, Begrepskatalog, API-katalog)
7. Sektorprodukter og domeneprodukter (for eksempel opptakslÃ¸sninger, fagsystemnÃ¦re felleslÃ¸sninger)

### 7.1 Vurderte produkter fra katalogen

| Produkt (fra produktkatalogen) | Produktkategori | Relevans for caset | Kan brukes direkte | BÃ¸r videreutvikles | Ikke relevant | Begrunnelse |
|---|---|---|---|---|---|---|
| [Produkt] | [Sett inn] | [HÃ¸y/middels/lav] | [Ja/nei] | [Ja/nei] | [Ja/nei] | [Sett inn] |
| [Produkt] | [Sett inn] | [HÃ¸y/middels/lav] | [Ja/nei] | [Ja/nei] | [Ja/nei] | [Sett inn] |

### 7.2 Oppsummering: hva finnes, hva kan gjenbrukes, hva mÃ¥ videreutvikles

- Hva finnes: [Sett inn]
- Hva kan gjenbrukes direkte: [Sett inn]
- Hva mÃ¥ videreutvikles: [Sett inn]
- Hva er ikke relevant i dette caset: [Sett inn]

### 7.3 Eksplisitte mangler og behov for nye/sammensatte lÃ¸sninger

| Identifisert mangel | Hvorfor mangelen oppstÃ¥r | Konsekvens hvis ikke lÃ¸st | Forslag til ny/sammensatt lÃ¸sning | Kan bygge pÃ¥ eksisterende produkter |
|---|---|---|---|---|
| [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] |

### 7.4 Sammensatte lÃ¸sningsmÃ¸nstre

Hjelpetekst: Beskriv kombinasjoner av produkter som samlet kan lÃ¸se behovet. Dette skal brukes fÃ¸r du foreslÃ¥r nye produkter.

| LÃ¸sningsmÃ¸nster | Produkter som inngÃ¥r | Hva mÃ¸nsteret dekker | Hva som fortsatt mangler |
|---|---|---|---|
| [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] |

## 8. Tiltak prioritert etter effekt

Hjelpetekst: Tiltak skal vÃ¦re sporbare til kapabilitetsgap, prinsippvurdering og produktvurdering.

### 8.0 Gap-type per tiltak

Hjelpetekst: Klassifiser hvert tiltak med primÃ¦r gap-type for Ã¥ unngÃ¥ at alle tiltak blir behandlet som teknisk utvikling.

Tillatte gap-typer:
- Produktgap
- Semantisk gap
- Juridisk gap
- Samordningsgap

| Tiltak | Type (gjenbruk/videreutvikling/nyutvikling/avklaring) | Forventet effekt (hÃ¸y/middels/lav) | Tidshorisont (kort/middels/lang) | Avhengigheter | Kobling til kapabilitet/prinsipp/produkt | PrimÃ¦r gap-type |
|---|---|---|---|---|---|---|
| [Tiltak] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] |
| [Tiltak] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] | [Sett inn] |

### Prioritert liste

1. [Tiltak] - Begrunnelse: [Sett inn]
2. [Tiltak] - Begrunnelse: [Sett inn]
3. [Tiltak] - Begrunnelse: [Sett inn]

## 9. Strategisk vurdering

Hjelpetekst: LÃ¸ft analysen til styringsnivÃ¥. Beskriv konsekvenser for portefÃ¸lje, nasjonal retning og samordning.

- Betydning for portefÃ¸ljeprioritering: [Sett inn]
- Betydning for nasjonal arkitektur/felles retning: [Sett inn]
- Behov for samordning mellom aktÃ¸rer: [Sett inn]

## 10. Konklusjon

Hjelpetekst: Oppsummer i 5-8 setninger med tydelig svar pÃ¥ hva som bÃ¸r gjÃ¸res videre.

[Sett inn]

## 11. Kortversjon for ledelse

Hjelpetekst: Brukes nÃ¥r analysen skal leses raskt i styringsmÃ¸ter.

- Case: [Sett inn]
- Analysetillit: [HÃ¸y/middels/lav]
- Hovedfunn (1-3 setninger): [Sett inn]
- Viktigste kapabilitetsgap: [Sett inn]
- Mest relevante produkter for gjenbruk: [Sett inn]
- Hva mangler: [Sett inn]
- Anbefalt prioritering:
  1. [Sett inn]
  2. [Sett inn]
  3. [Sett inn]

## BruksnivÃ¥ (rask analyse og beslutningsgrunnlag)

### NivÃ¥ 1 - rask analyse

Minimum som fylles ut:
- problembilde
- kapabilitetsanalyse
- prinsippvurdering
- forelÃ¸pig produktvurdering
- prioriterte tiltak

### NivÃ¥ 2 - beslutningsgrunnlag

Utvid med:
- full produktvurdering av relevante produktkategorier
- eksplisitte mangler og behov for nye/sammensatte lÃ¸sninger
- strategisk vurdering
- kortversjon for ledelse

