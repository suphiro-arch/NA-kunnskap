---
title: "Forside"
weight: 1
description: "Inngang til dokumentasjonen for nasjonal arkitektur, prinsipper, kapabiliteter og nasjonale fellesressurser."
---

# Nasjonal arkitektur for samhandling

Denne prototypen er en dokumentasjonsside for nasjonal arkitektur. Den skal gjÃ¸re det enklere Ã¥ forstÃ¥ sammenhengen mellom kapabiliteter, prinsipper og felles produkter som stÃ¸tter samhandling pÃ¥ tvers av virksomheter.

## Hva finner du her?

Denne dokumentasjonen er bygget opp rundt tre spÃ¸rsmÃ¥l:

- Hvilke evner mÃ¥ Ã¸kosystemet ha for Ã¥ lykkes?
- Hvilke fÃ¸ringer bÃ¸r styre valg av lÃ¸sninger og prioriteringer?
- Hvilke felles ressurser og produkter kan brukes i praksis?

Svarene ligger i hver sin hovedseksjon:

- [Kapabiliteter](kapabiliteter/) beskriver hvilke evner som mÃ¥ finnes i Ã¸kosystemet.
- [Prinsipper](prinsipper/) forklarer hvilke arkitekturfaglige fÃ¸ringer som bÃ¸r styre utviklingen.
- [Ressursoversikt](ressursoversikt/) samler konkrete produkter og felleslÃ¸sninger.

## Hvem er dokumentasjonen for?

Prototypen er sÃ¦rlig relevant for:

- arkitekter som trenger en felles referanse for samhandling pÃ¥ tvers
- produktledere og forvaltere som mÃ¥ plassere egne lÃ¸sninger i en stÃ¸rre sammenheng
- utviklingsteam som trenger oversikt over tilgjengelige fellesressurser
- beslutningstakere som vil forstÃ¥ koblingen mellom mÃ¥l, prinsipper og virkemidler

## Hvordan ressursoversikten er generert

Ressursoversikten i prototypen er delvis generert fra kildedata i repoet.

Prosess i korte trekk:

1. Ressurser registreres med ressurs-ID, type og dokumentlenke i registeret.
2. Kapabilitetskoblinger hentes fra koblingsfilen og brukes som metadata i visningen.
3. Genereringsscript bygger oversiktssider med filtrering, kapabilitetsvisning og lenker til detaljerte md-filer.

VerktÃ¸y som brukes i dag:

- PowerShell-script for generering av ressurssider.
- Python-script for sammenstilling av kapabilitetssider og koblinger.
- Hugo for bygging og visning av nettstedet.

Denne lÃ¸sningen er under stadig utvikling. Struktur, innhold og presentasjon justeres fortlÃ¸pende etter hvert som ressursgrunnlaget modnes.

## Hvordan bruke prototypen

Bruk siden som et oppslagsverk, ikke som en lineÃ¦r rapport.

- NÃ¥r du arbeider med en bestemt problemstilling, start i den seksjonen som svarer pÃ¥ behovet ditt.
- NÃ¥r du trenger sammenheng, bruk lenkene mellom kapabiliteter, prinsipper og produkter.
- NÃ¥r du leter etter konkrete virkemidler, bruk [Ressursoversikt](ressursoversikt/) og Ã¥pne Full beskrivelse (md-fil) fra ressurskortet.

## Kildegrunnlag og avgrensning

Prototypen bygger forelÃ¸pig pÃ¥ innhold fra:

- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/prinsipper/principles.md`
- `arkitektur/ressurser/produktnummerering.md`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
- `arkitektur/ressurser/`

Dette er fortsatt en testflate. MÃ¥let nÃ¥ er Ã¥ gjÃ¸re strukturen tydelig og lesbar fÃ¸r innholdet utvides videre.

