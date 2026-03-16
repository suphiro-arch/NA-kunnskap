# Briefs: arbeidsstyring og handover

Denne fila beskriver hvordan `briefs/` brukes til arbeidsstyring, handover og beslutningsstøtte i repoet.

## Rolle i repoet
- `briefs/` brukes for arbeidsstyring, handover, avklaringer, beslutninger og mellomdokumenter.
- `results/` brukes for leveranser og innhold som skal fungere som kunnskapsgrunnlag videre.
- Hvis et dokument primært er et arbeidsnotat eller en skisse, hører det hjemme i `briefs/`.
- Hvis et dokument er en faglig leveranse eller et innholdsdokument som skal gjenbrukes direkte, hører det hjemme i `results/`.

## Struktur i `briefs/`
- `briefs/next-step.md`: kort status over hva som er gjort og hva som gjenstår.
- `briefs/decisions.md`: varige beslutninger om metode, struktur og arkitektur.
- `briefs/arbeidsstyring-og-handover/`: arbeidsdokumenter, skisser, handover-notater og større mellomleveranser som ikke er faglige sluttresultater.
- Bruk `results/` for leveranser som skal fungere som kunnskapsgrunnlag eller ferdig innhold; bruk `briefs/` for arbeidsstyring og overgang mellom økter.

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
5. Legg arbeidsdokumenter og handover-notater i `briefs/arbeidsstyring-og-handover/`.

## Navngiving
Format: `YYYY-MM-DD-tema-vN.md`
Eksempel: `2026-03-06-altinn-produkter-v1.md`
