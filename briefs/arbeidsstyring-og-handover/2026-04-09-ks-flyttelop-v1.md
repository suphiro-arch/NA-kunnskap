---
date: 2026-04-09
author: codex
status: gjennomfort
topic: andre sektorvise flytteløp for KS Digital
sources:
  - arkitektur/produkter/produktnummerering.md
  - arkitektur/produkter/produktbeskrivelser/
  - briefs/arbeidsstyring-og-handover/2026-04-09-digdir-flyttelop-v1.md
---

# Andre sektorvise flytteløp: KS Digital

Dette notatet følger samme mønster som Digdir-piloten, men for KS Digital.

## Valgt bolk

Andre flytteløp bør være **KS Digital-bolken**.

Begrunnelse:
- bolken er avgrenset og fullt operativ
- ressursene er tydelig registrert i samme eierområde
- den inneholder både plattform, meldingsressurser, registertilgang og oversiktsressurser
- den lar oss teste at migreringsmønsteret også fungerer godt for en annen sektor enn Digdir

## Arbeidsregler

- bare siste registrerte versjon flyttes
- eldre versjoner blir stående i `arkitektur/produkter/produktbeskrivelser/`
- filnavn beholdes uendret i dette løpet
- målmappe er `arkitektur/ressurser/operative-losninger-og-tjenester/`
- `arkitektur/produkter/produktnummerering.md` forblir registermaster

## Kandidater i KS-løpet

| Løpenr | Ressurs-ID | Navn | Nåværende fil | Foreslått mål |
|---:|---|---|---|---|
| 25 | `KS-001` | Fiks-plattformen | `arkitektur/produkter/produktbeskrivelser/25-FIKS-plattformen-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/25-FIKS-plattformen-produkt-canvas-v1-codex.md` |
| 26 | `KS-002` | Fiks melding | `arkitektur/produkter/produktbeskrivelser/26-FIKS-Melding-produkt-canvas-v2-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/26-FIKS-Melding-produkt-canvas-v2-codex.md` |
| 27 | `KS-003` | Fiks SvarUt | `arkitektur/produkter/produktbeskrivelser/27-FIKS-SvarUt-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/27-FIKS-SvarUt-produkt-canvas-v3-codex.md` |
| 28 | `KS-004` | Fiks register | `arkitektur/produkter/produktbeskrivelser/28-FIKS-Register-produkt-canvas-v2-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v2-codex.md` |
| 30 | `KS-006` | Fiks digiorden | `arkitektur/produkter/produktbeskrivelser/30-FIKS-Digiorden-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/30-FIKS-Digiorden-produkt-canvas-v1-codex.md` |
| 57 | `KS-007` | SvarInn | `arkitektur/produkter/produktbeskrivelser/57-SvarInn-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/57-SvarInn-produkt-canvas-v1-codex.md` |
| 67 | `KS-008` | Fiks folkeregister | `arkitektur/produkter/produktbeskrivelser/67-FIKS-Folkeregister-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/67-FIKS-Folkeregister-produkt-canvas-v1-codex.md` |
| 68 | `KS-009` | Fiks skatte- og inntektsopplysninger | `arkitektur/produkter/produktbeskrivelser/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v1-codex.md` |
| 69 | `KS-010` | Fiks kjøretøyregister | `arkitektur/produkter/produktbeskrivelser/69-FIKS-Kjoretoyregister-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/69-FIKS-Kjoretoyregister-produkt-canvas-v1-codex.md` |

Totalt: **9 filer**

## Gjennomføringsrekkefølge

1. Flytt de 9 siste KS-filene til `arkitektur/ressurser/operative-losninger-og-tjenester/`
2. Oppdater dokumentlenker i `produktnummerering.md`
3. Oppdater relative stier og GitHub-lenker i `produkt-kapabilitet-koblinger.yaml`
4. Regenerer ressursoversikt og kapabilitetssider
5. Kjør tegnkodingskontroll

## Status etter gjennomføring 2026-04-09

KS-løpet er nå gjennomført som andre sektorvise migrering.

Gjennomført:
- 9 siste KS-filer er flyttet fra `arkitektur/produkter/produktbeskrivelser/` til `arkitektur/ressurser/operative-losninger-og-tjenester/`
- dokumentlenker i `arkitektur/produkter/produktnummerering.md` er oppdatert
- relative stier og GitHub-lenker i `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` er oppdatert
- webgrunnlaget er regenerert
- tegnkodingskontroll er kjørt uten feil

Ikke verifisert lokalt:
- full Hugo-build, fordi `hugo` ikke er installert i dette miljøet
