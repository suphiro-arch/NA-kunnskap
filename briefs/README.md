# NA kunnskap arbeidsflyt

Denne fila beskriver hvordan assistenter (Copilot/Codex) samarbeider via filer i repoet.

## Mapper
- `sources/`: raadata, kilder, linker, notater fra oppslag.
- `results/`: bearbeidede leveranser og ferdige beskrivelser.
- `briefs/`: handoff, avklaringer, beslutninger og neste steg.
- `config/`: schema, prompts og felles konfig.

## Minimum metadata i nye markdownfiler
Bruk denne frontmatteren:

```yaml
---
date: YYYY-MM-DD
author: codex|copilot|manual
status: draft|review|final
topic: kort-tema
sources:
  - path/eller-url
---
```

## Foreslaatt arbeidsprosess
1. Legg kilder i `sources/`.
2. Skriv oppsummering/leveranse i `results/` med kildehenvisning.
3. Oppdater `briefs/next-step.md` med hva som er gjort og hva som gjenstaar.
4. Logg viktige valg i `briefs/decisions.md`.

## Navngiving
Format: `YYYY-MM-DD-tema-vN.md`
Eksempel: `2026-03-06-altinn-produkter-v1.md`
