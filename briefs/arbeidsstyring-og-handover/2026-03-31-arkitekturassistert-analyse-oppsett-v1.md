---
date: 2026-03-31
author: copilot
status: draft
topic: arkitekturassistert-analyse-oppsett
sources:
  - config/templates/arkitekturassistert-analyse-av-utviklingsbehov-template.md
  - config/prompts/arkitekturassistert-analyse-av-utviklingsbehov.system.md
  - arkitektur/kapabiliteter/capabilities.yaml
  - arkitektur/prinsipper/principles.md
  - arkitektur/produkter/produktnummerering.md
  - arkitektur/produkter/produktbeskrivelser/
---

# Oppsett for arkitekturassistert analyse av utviklingsbehov

## Hensikt

Dette dokumentet beskriver valgt oppsett for ny analysetype i repoet, slik at arbeidet blir konsistent og gjenbrukbart.

## Valgt plassering

- Mal legges i `config/templates/`.
- Instruks legges i `config/prompts/`.

## Opprettede filer

- `config/templates/arkitekturassistert-analyse-av-utviklingsbehov-template.md`
- `config/prompts/arkitekturassistert-analyse-av-utviklingsbehov.system.md`

## Styrende føringer i oppsettet

- Produktkatalogen brukes som fasit for hva som finnes.
- Produkter som ikke finnes i katalogen skal ikke foreslås, med mindre det identifiseres et eksplisitt gap.
- Relevante produktkategorier skal vurderes systematisk.
- Hvert vurdert produkt skal klassifiseres som:
  - brukes direkte
  - videreutvikles
  - ikke relevant
- Manglende dekning skal beskrives eksplisitt.
- Analyse skal ha tydelig kobling mellom kapabiliteter, prinsipper og produkter.
- Leveransen skal kunne brukes både som rask analyse og som beslutningsgrunnlag.

## Hvorfor dette oppsettet

- `config/templates/` er etablert plassering for malfiler.
- `config/prompts/` er etablert plassering for instruksfiler.
- Kombinasjonen gir en tydelig arbeidsdeling:
  - malen styrer struktur på leveransen
  - instruksen styrer metode og kvalitetskrav
