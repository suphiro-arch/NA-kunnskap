---
title: "Forside"
weight: 1
description: "Inngang til dokumentasjonen for nasjonal arkitektur, prinsipper, kapabiliteter og nasjonale fellesressurser."
---

# Nasjonal arkitektur for samhandling

Denne prototypen er en dokumentasjonsside for nasjonal arkitektur. Den skal gjøre det enklere å forstå sammenhengen mellom kapabiliteter, prinsipper og felles produkter som støtter samhandling på tvers av virksomheter.

## Hva finner du her?

Denne dokumentasjonen er bygget opp rundt tre spørsmål:

- Hvilke evner må økosystemet ha for å lykkes?
- Hvilke føringer bør styre valg av løsninger og prioriteringer?
- Hvilke felles ressurser og produkter kan brukes i praksis?

Svarene ligger i hver sin hovedseksjon:

- [Kapabiliteter](kapabiliteter/) beskriver hvilke evner som må finnes i økosystemet.
- [Prinsipper](prinsipper/) forklarer hvilke arkitekturfaglige føringer som bør styre utviklingen.
- [Ressursoversikt](ressursoversikt/) samler konkrete produkter og fellesløsninger.

## Hvem er dokumentasjonen for?

Prototypen er særlig relevant for:

- arkitekter som trenger en felles referanse for samhandling på tvers
- produktledere og forvaltere som må plassere egne løsninger i en større sammenheng
- utviklingsteam som trenger oversikt over tilgjengelige fellesressurser
- beslutningstakere som vil forstå koblingen mellom mål, prinsipper og virkemidler

## Hvordan ressursoversikten er generert

Ressursoversikten i prototypen er delvis generert fra kildedata i repoet.

Prosess i korte trekk:

1. Ressurser registreres med ressurs-ID, type og dokumentlenke i registeret.
2. Kapabilitetskoblinger hentes fra koblingsfilen og brukes som metadata i visningen.
3. Genereringsscript bygger oversiktssider med filtrering, kapabilitetsvisning og lenker til detaljerte md-filer.

Verktøy som brukes i dag:

- PowerShell-script for generering av ressurssider.
- Python-script for sammenstilling av kapabilitetssider og koblinger.
- Hugo for bygging og visning av nettstedet.

Denne løsningen er under stadig utvikling. Struktur, innhold og presentasjon justeres fortløpende etter hvert som ressursgrunnlaget modnes.

## Hvordan bruke prototypen

Bruk siden som et oppslagsverk, ikke som en lineær rapport.

- Når du arbeider med en bestemt problemstilling, start i den seksjonen som svarer på behovet ditt.
- Når du trenger sammenheng, bruk lenkene mellom kapabiliteter, prinsipper og produkter.
- Når du leter etter konkrete virkemidler, bruk [Ressursoversikt](ressursoversikt/) og åpne Full beskrivelse (md-fil) fra ressurskortet.

## Kildegrunnlag og avgrensning

Prototypen bygger foreløpig på innhold fra:

- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/prinsipper/principles.md`
- `arkitektur/produkter/produktnummerering.md`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
- `arkitektur/ressurser/`

Dette er fortsatt en testflate. Målet nå er å gjøre strukturen tydelig og lesbar før innholdet utvides videre.
