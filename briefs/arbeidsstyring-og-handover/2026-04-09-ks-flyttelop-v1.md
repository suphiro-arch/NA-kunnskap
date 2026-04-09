---
date: 2026-04-09
author: codex
status: gjennomfort
topic: andre sektorvise flyttelÃ¸p for KS Digital
sources:
  - arkitektur/ressurser/produktnummerering.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/
  - briefs/arbeidsstyring-og-handover/2026-04-09-digdir-flyttelop-v1.md
---

# Andre sektorvise flyttelÃ¸p: KS Digital

Dette notatet fÃ¸lger samme mÃ¸nster som Digdir-piloten, men for KS Digital.

## Valgt bolk

Andre flyttelÃ¸p bÃ¸r vÃ¦re **KS Digital-bolken**.

Begrunnelse:
- bolken er avgrenset og fullt operativ
- ressursene er tydelig registrert i samme eieromrÃ¥de
- den inneholder bÃ¥de plattform, meldingsressurser, registertilgang og oversiktsressurser
- den lar oss teste at migreringsmÃ¸nsteret ogsÃ¥ fungerer godt for en annen sektor enn Digdir

## Arbeidsregler

- bare siste registrerte versjon flyttes
- eldre versjoner blir stÃ¥ende i `arkitektur/ressurser/operative-losninger-og-tjenester/`
- filnavn beholdes uendret i dette lÃ¸pet
- mÃ¥lmappe er `arkitektur/ressurser/operative-losninger-og-tjenester/`
- `arkitektur/ressurser/produktnummerering.md` forblir registermaster

## Kandidater i KS-lÃ¸pet

| LÃ¸penr | Ressurs-ID | Navn | NÃ¥vÃ¦rende fil | ForeslÃ¥tt mÃ¥l |
|---:|---|---|---|---|
| 25 | `KS-001` | Fiks-plattformen | `arkitektur/ressurser/operative-losninger-og-tjenester/25-FIKS-plattformen-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/25-FIKS-plattformen-produkt-canvas-v1-codex.md` |
| 26 | `KS-002` | Fiks melding | `arkitektur/ressurser/operative-losninger-og-tjenester/26-FIKS-Melding-produkt-canvas-v2-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/26-FIKS-Melding-produkt-canvas-v2-codex.md` |
| 27 | `KS-003` | Fiks SvarUt | `arkitektur/ressurser/operative-losninger-og-tjenester/27-FIKS-SvarUt-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/27-FIKS-SvarUt-produkt-canvas-v3-codex.md` |
| 28 | `KS-004` | Fiks register | `arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v2-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v2-codex.md` |
| 30 | `KS-006` | Fiks digiorden | `arkitektur/ressurser/operative-losninger-og-tjenester/30-FIKS-Digiorden-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/30-FIKS-Digiorden-produkt-canvas-v1-codex.md` |
| 57 | `KS-007` | SvarInn | `arkitektur/ressurser/operative-losninger-og-tjenester/57-SvarInn-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/57-SvarInn-produkt-canvas-v1-codex.md` |
| 67 | `KS-008` | Fiks folkeregister | `arkitektur/ressurser/operative-losninger-og-tjenester/67-FIKS-Folkeregister-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/67-FIKS-Folkeregister-produkt-canvas-v1-codex.md` |
| 68 | `KS-009` | Fiks skatte- og inntektsopplysninger | `arkitektur/ressurser/operative-losninger-og-tjenester/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v1-codex.md` |
| 69 | `KS-010` | Fiks kjÃ¸retÃ¸yregister | `arkitektur/ressurser/operative-losninger-og-tjenester/69-FIKS-Kjoretoyregister-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/69-FIKS-Kjoretoyregister-produkt-canvas-v1-codex.md` |

Totalt: **9 filer**

## GjennomfÃ¸ringsrekkefÃ¸lge

1. Flytt de 9 siste KS-filene til `arkitektur/ressurser/operative-losninger-og-tjenester/`
2. Oppdater dokumentlenker i `produktnummerering.md`
3. Oppdater relative stier og GitHub-lenker i `produkt-kapabilitet-koblinger.yaml`
4. Regenerer ressursoversikt og kapabilitetssider
5. KjÃ¸r tegnkodingskontroll

## Status etter gjennomfÃ¸ring 2026-04-09

KS-lÃ¸pet er nÃ¥ gjennomfÃ¸rt som andre sektorvise migrering.

GjennomfÃ¸rt:
- 9 siste KS-filer er flyttet fra `arkitektur/ressurser/operative-losninger-og-tjenester/` til `arkitektur/ressurser/operative-losninger-og-tjenester/`
- dokumentlenker i `arkitektur/ressurser/produktnummerering.md` er oppdatert
- relative stier og GitHub-lenker i `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` er oppdatert
- webgrunnlaget er regenerert
- tegnkodingskontroll er kjÃ¸rt uten feil

Ikke verifisert lokalt:
- full Hugo-build, fordi `hugo` ikke er installert i dette miljÃ¸et

