---
date: 2026-04-09
author: codex
status: gjennomfort
topic: fjerde sektorvise flytteløp for helsesektoren
sources:
  - arkitektur/ressurser/produktnummerering.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/
  - briefs/arbeidsstyring-og-handover/2026-04-09-digdir-flyttelop-v1.md
  - briefs/arbeidsstyring-og-handover/2026-04-09-ks-flyttelop-v1.md
  - briefs/arbeidsstyring-og-handover/2026-04-09-sikt-flyttelop-v1.md
---

# Fjerde sektorvise flytteløp: Helsesektoren

Dette notatet samler første flytteløp for helseområdet på tvers av flere eiere.

## Valgt bolk

Fjerde flytteløp er en samlet **helsebolk** for:
- Helsedirektoratet (`HDIR`)
- Norsk helsenett (`NHN`)
- Helfo (`HELFO`)

Begrunnelse:
- hver delbolk er liten alene
- ressursene hører til samme overordnede sektorlandskap
- samlet flytting gir mer mening enn tre små, separate løp

## Arbeidsregler

- bare siste registrerte versjon flyttes
- eldre versjoner blir stående i `arkitektur/ressurser/operative-losninger-og-tjenester/`
- filnavn beholdes uendret i dette løpet
- målmappe er `arkitektur/ressurser/operative-losninger-og-tjenester/`
- `arkitektur/ressurser/produktnummerering.md` forblir registermaster

## Kandidater i helse-løpet

| Løpenr | Ressurs-ID | Navn | Nåværende fil | Foreslått mål |
|---:|---|---|---|---|
| 31 | `HDIR-001` | Helsedata.no | `arkitektur/ressurser/operative-losninger-og-tjenester/31-Helsedata-no-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/31-Helsedata-no-produkt-canvas-v1-codex.md` |
| 32 | `NHN-001` | Helsenorge | `arkitektur/ressurser/operative-losninger-og-tjenester/32-Helsenorge-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/32-Helsenorge-produkt-canvas-v1-codex.md` |
| 33 | `NHN-002` | HelseID | `arkitektur/ressurser/operative-losninger-og-tjenester/33-HelseID-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/33-HelseID-produkt-canvas-v1-codex.md` |
| 34 | `NHN-003` | Kjernejournal | `arkitektur/ressurser/operative-losninger-og-tjenester/34-Kjernejournal-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/34-Kjernejournal-produkt-canvas-v1-codex.md` |
| 35 | `NHN-004` | e-resept | `arkitektur/ressurser/operative-losninger-og-tjenester/35-e-resept-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/35-e-resept-produkt-canvas-v1-codex.md` |
| 64 | `HDIR-002` | HPR | `arkitektur/ressurser/operative-losninger-og-tjenester/64-HPR-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/64-HPR-produkt-canvas-v1-codex.md` |
| 65 | `HELFO-001` | KUHR | `arkitektur/ressurser/operative-losninger-og-tjenester/65-KUHR-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/65-KUHR-produkt-canvas-v1-codex.md` |

Totalt: **7 filer**

## Gjennomføringsrekkefølge

1. Flytt de 7 siste helsefilene til `arkitektur/ressurser/operative-losninger-og-tjenester/`
2. Oppdater dokumentlenker i `produktnummerering.md`
3. Oppdater relative stier og GitHub-lenker i `produkt-kapabilitet-koblinger.yaml`
4. Regenerer ressursoversikt og kapabilitetssider
5. Kjør tegnkodingskontroll
6. Kontroller at relevante webfiler faktisk peker riktig etter generering

## Status etter gjennomføring 2026-04-09

Helse-løpet er nå gjennomført som fjerde sektorvise migrering.

Gjennomført:
- 7 siste helsefiler er flyttet fra `arkitektur/ressurser/operative-losninger-og-tjenester/` til `arkitektur/ressurser/operative-losninger-og-tjenester/`
- dokumentlenker i `arkitektur/ressurser/produktnummerering.md` er oppdatert
- relative stier og GitHub-lenker i `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` er oppdatert
- webgrunnlaget er regenerert
- tegnkodingskontroll er kjørt uten feil
- relevante webfiler for helseområdet er kontrollert etter generering og peker riktig

Ikke verifisert lokalt:
- full Hugo-build, fordi `hugo` ikke er installert i dette miljøet


