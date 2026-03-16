# NA kunnskap arbeidsflyt

Denne fila beskriver hvordan assistenter (Copilot/Codex) samarbeider via filer i repoet.

## Mapper
- `sources/`: rådata, kilder, linker, notater fra oppslag.
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

## Språk og tegnsett i nye filer

Nye tekstfiler som opprettes av assistenter i dette repoet skal:

- skrives på norsk
- bruke vanlig norsk tegnsett i løpende tekst
- skrive `æ`, `ø` og `å` bare der tekniske begrensninger krever det, for eksempel i filnavn, slugger eller kode

Begrunnelse:

- vanlig norsk tegnsett gir bedre leseopplevelse i dokumenter
- ASCII kan fortsatt være nødvendig i enkelte tekniske sammenhenger

Dette gjelder som standard for nye markdown- og dokumentasjonsfiler. Hvis en bestemt generator, publiseringsjobb eller teknisk komponent ikke handterer norsk tegnsett stabilt, skal dette avgrenses til den konkrete delen og ikke brukes som generell skriveregel for dokumentinnhold.

## Foreslått arbeidsprosess
1. Legg kilder i `sources/`.
2. Skriv oppsummering/leveranse i `results/` med kildehenvisning.
3. Oppdater `briefs/next-step.md` med hva som er gjort og hva som gjenstår.
4. Logg viktige valg i `briefs/decisions.md`.

## Navngiving
Format: `YYYY-MM-DD-tema-vN.md`
Eksempel: `2026-03-06-altinn-produkter-v1.md`
