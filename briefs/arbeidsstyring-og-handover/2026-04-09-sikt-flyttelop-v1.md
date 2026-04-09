---
date: 2026-04-09
author: codex
status: gjennomfort
topic: tredje sektorvise flytteløp for SIKT
sources:
  - arkitektur/ressurser/produktnummerering.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/
  - briefs/arbeidsstyring-og-handover/2026-04-09-digdir-flyttelop-v1.md
  - briefs/arbeidsstyring-og-handover/2026-04-09-ks-flyttelop-v1.md
---

# Tredje sektorvise flytteløp: SIKT

Dette notatet følger samme migreringsmønster som Digdir og KS, men for SIKT.

## Valgt bolk

Tredje flytteløp er **SIKT-bolken**.

Begrunnelse:
- bolken er avgrenset og operativ
- den dekker et sammenhengende utdanningsområde
- den gir en god test på om migreringsmønsteret fungerer også for sektorressurser med sterk kobling til opptak, studentdata og vitnemål

## Arbeidsregler

- bare siste registrerte versjon flyttes
- eldre versjoner blir stående i `arkitektur/ressurser/operative-losninger-og-tjenester/`
- filnavn beholdes uendret i dette løpet
- målmappe er `arkitektur/ressurser/operative-losninger-og-tjenester/`
- `arkitektur/ressurser/produktnummerering.md` forblir registermaster

## Kandidater i SIKT-løpet

| Løpenr | Ressurs-ID | Navn | Nåværende fil | Foreslått mål |
|---:|---|---|---|---|
| 47 | `SIKT-001` | Feide | `arkitektur/ressurser/operative-losninger-og-tjenester/47-Feide-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/47-Feide-produkt-canvas-v1-codex.md` |
| 48 | `SIKT-002` | Felles studentsystem (FS) | `arkitektur/ressurser/operative-losninger-og-tjenester/48-Felles-studentsystem-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/48-Felles-studentsystem-produkt-canvas-v1-codex.md` |
| 49 | `SIKT-003` | Opptaksløsninger | `arkitektur/ressurser/operative-losninger-og-tjenester/49-Opptakslosninger-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/49-Opptakslosninger-produkt-canvas-v1-codex.md` |
| 50 | `SIKT-004` | Nasjonal vitnemålsdatabase (NVB) | `arkitektur/ressurser/operative-losninger-og-tjenester/50-Nasjonal-vitnemalsdatabase-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/50-Nasjonal-vitnemalsdatabase-produkt-canvas-v1-codex.md` |
| 51 | `SIKT-005` | Vitnemålsportalen | `arkitektur/ressurser/operative-losninger-og-tjenester/51-Vitnemalsportalen-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/51-Vitnemalsportalen-produkt-canvas-v1-codex.md` |
| 52 | `SIKT-006` | Nasjonalt utdanningsregister | `arkitektur/ressurser/operative-losninger-og-tjenester/52-Nasjonalt-utdanningsregister-produkt-canvas-v1-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/52-Nasjonalt-utdanningsregister-produkt-canvas-v1-codex.md` |

Totalt: **6 filer**

## Gjennomføringsrekkefølge

1. Flytt de 6 siste SIKT-filene til `arkitektur/ressurser/operative-losninger-og-tjenester/`
2. Oppdater dokumentlenker i `produktnummerering.md`
3. Oppdater relative stier og GitHub-lenker i `produkt-kapabilitet-koblinger.yaml`
4. Regenerer ressursoversikt og kapabilitetssider
5. Kjør tegnkodingskontroll
6. Kontroller at relevante webfiler faktisk peker riktig etter generering

## Status etter gjennomføring 2026-04-09

SIKT-løpet er nå gjennomført som tredje sektorvise migrering.

Gjennomført:
- 6 siste SIKT-filer er flyttet fra `arkitektur/ressurser/operative-losninger-og-tjenester/` til `arkitektur/ressurser/operative-losninger-og-tjenester/`
- dokumentlenker i `arkitektur/ressurser/produktnummerering.md` er oppdatert
- relative stier og GitHub-lenker i `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` er oppdatert
- webgrunnlaget er regenerert
- tegnkodingskontroll er kjørt uten feil
- kapabilitetssidene bruker nå lenker bygget fra faktisk `relative_path`, slik at flyttede filer fortsatt peker riktig i weben

Ikke verifisert lokalt:
- full Hugo-build, fordi `hugo` ikke er installert i dette miljøet


