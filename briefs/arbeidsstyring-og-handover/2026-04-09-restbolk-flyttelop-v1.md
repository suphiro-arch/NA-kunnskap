---
date: 2026-04-09
author: codex
status: gjennomfort
topic: femte sektorvise flyttelop for gjenværende operative bolker
sources:
  - arkitektur/ressurser/produktnummerering.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/
  - briefs/arbeidsstyring-og-handover/2026-04-09-digdir-flyttelop-v1.md
  - briefs/arbeidsstyring-og-handover/2026-04-09-ks-flyttelop-v1.md
  - briefs/arbeidsstyring-og-handover/2026-04-09-sikt-flyttelop-v1.md
  - briefs/arbeidsstyring-og-handover/2026-04-09-helse-flyttelop-v1.md
---

# Femte flyttelop: gjenværende operative bolker

Dette notatet samler de gjenværende små operative bolkene i ett siste flyttelop.

## Valgt bolk

Femte flyttelop samler:
- NAV
- Skatteetaten
- Kartverket
- Statens vegvesen
- SSB
- Flere virksomheter

Begrunnelse:
- hver delbolk er liten alene
- de resterende operative beskrivelsene er få nok til å håndteres samlet
- dette avslutter første hovedmigrering av operative beskrivelser

## Arbeidsregler

- bare siste registrerte versjon flyttes
- eldre versjoner blir stående i `arkitektur/ressurser/operative-losninger-og-tjenester/`
- filnavn beholdes uendret i dette løpet
- målmappe er `arkitektur/ressurser/operative-losninger-og-tjenester/`
- `arkitektur/ressurser/produktnummerering.md` forblir registermaster

## Kandidater i restlopet

| Løpenr | Ressurs-ID | Navn | Nåværende fil | Foreslått mål |
|---:|---|---|---|---|
| 36 | `NAV-001` | Aa-registeret | `arkitektur/ressurser/operative-losninger-og-tjenester/36-Aa-registeret-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/36-Aa-registeret-produkt-canvas-v1-codex.md` |
| 37 | `SKATT-001` | Folkeregisteret | `arkitektur/ressurser/operative-losninger-og-tjenester/37-Folkeregisteret-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/37-Folkeregisteret-produkt-canvas-v1-codex.md` |
| 38 | `SKATT-002` | Skatteetatens delingstjenester | `arkitektur/ressurser/operative-losninger-og-tjenester/38-Skatteetatens-delingstjenester-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/38-Skatteetatens-delingstjenester-produkt-canvas-v1-codex.md` |
| 39 | `KART-001` | Matrikkelen | `arkitektur/ressurser/operative-losninger-og-tjenester/39-Matrikkelen-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/39-Matrikkelen-produkt-canvas-v1-codex.md` |
| 40 | `KART-002` | Geonorge | `arkitektur/ressurser/operative-losninger-og-tjenester/40-Geonorge-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/40-Geonorge-produkt-canvas-v1-codex.md` |
| 46 | `BRREG-003` | Enhetsregisteret | `arkitektur/ressurser/operative-losninger-og-tjenester/46-Enhetsregisteret-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/46-Enhetsregisteret-produkt-canvas-v1-codex.md` |
| 59 | `FLERE-001` | A-ordningen | `arkitektur/ressurser/operative-losninger-og-tjenester/59-A-ordningen-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/59-A-ordningen-produkt-canvas-v1-codex.md` |
| 60 | `SVV-001` | Motorvognregisteret | `arkitektur/ressurser/operative-losninger-og-tjenester/60-Motorvognregisteret-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/60-Motorvognregisteret-produkt-canvas-v1-codex.md` |
| 62 | `FLERE-002` | DSOP-tjenester | `arkitektur/ressurser/operative-losninger-og-tjenester/62-DSOP-tjenester-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/62-DSOP-tjenester-produkt-canvas-v1-codex.md` |
| 63 | `SSB-001` | microdata.no | `arkitektur/ressurser/operative-losninger-og-tjenester/63-microdata-no-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/63-microdata-no-produkt-canvas-v1-codex.md` |
| 66 | `NAV-002` | NAIS | `arkitektur/ressurser/operative-losninger-og-tjenester/66-NAIS-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/66-NAIS-produkt-canvas-v1-codex.md` |

Totalt: **11 filer**

## Gjennomforingsrekkefolge

1. Flytt de 11 siste operative filene til `arkitektur/ressurser/operative-losninger-og-tjenester/`
2. Oppdater dokumentlenker i `produktnummerering.md`
3. Oppdater relative stier og GitHub-lenker i `produkt-kapabilitet-koblinger.yaml`
4. Regenerer ressursoversikt og kapabilitetssider
5. Kjør tegnkodingskontroll
6. Kontroller at relevante webfiler faktisk peker riktig etter generering

## Status

Flytteløpet er gjennomført.

Følgende 11 siste operative beskrivelser er flyttet fra `arkitektur/ressurser/operative-losninger-og-tjenester/` til `arkitektur/ressurser/operative-losninger-og-tjenester/`:

- `36-Aa-registeret-produkt-canvas-v1-codex.md`
- `37-Folkeregisteret-produkt-canvas-v1-codex.md`
- `38-Skatteetatens-delingstjenester-produkt-canvas-v1-codex.md`
- `39-Matrikkelen-produkt-canvas-v1-codex.md`
- `40-Geonorge-produkt-canvas-v1-codex.md`
- `46-Enhetsregisteret-produkt-canvas-v1-codex.md`
- `59-A-ordningen-produkt-canvas-v1-codex.md`
- `60-Motorvognregisteret-produkt-canvas-v1-codex.md`
- `62-DSOP-tjenester-produkt-canvas-v1-codex.md`
- `63-microdata-no-produkt-canvas-v1-codex.md`
- `66-NAIS-produkt-canvas-v1-codex.md`

Tilhørende pekere er oppdatert i:

- `arkitektur/ressurser/produktnummerering.md`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`

Verifisert:

- `powershell -ExecutionPolicy Bypass -File web/hugo-prototype/scripts/generate-products.ps1`
- `python web/hugo-prototype/scripts/generate-capabilities.py`
- `python web/hugo-prototype/scripts/validate-text-encoding.py`

Ekstra webkontroll er gjort i:

- `web/hugo-prototype/content/ressursoversikt/produkter/_index.md`
- `web/hugo-prototype/content/kapabiliteter/datakilder/grunndata/_index.md`
- `web/hugo-prototype/content/kapabiliteter/datautveksling-og-integrasjon/dele-data-med-andre/_index.md`
- `web/hugo-prototype/content/kapabiliteter/datautveksling-og-integrasjon/bruke-data-fra-andre/_index.md`
- `web/hugo-prototype/content/kapabiliteter/informasjonsforvaltning/oversikt-over-datasett/_index.md`
- `web/hugo-prototype/content/kapabiliteter/tjenesteutvikling/gjenbrukbare-tjenester/_index.md`
- `web/hugo-prototype/content/kapabiliteter/tjenesteutvikling/utviklings-og-kjoretidsmiljo/_index.md`

Resultat:

- ressursene vises i generert ressursoversikt
- relevante kapabilitetssider peker til ny plassering under `arkitektur/ressurser/operative-losninger-og-tjenester/`
- ingen gamle pekere for denne restbolken står igjen i register eller mappingfil
- lokal Hugo-build er fortsatt ikke verifisert fordi `hugo` ikke er installert i miljøet


