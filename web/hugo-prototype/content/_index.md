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

Ressursoversikten og ressursbeskrivelsene er bygget fra kildedata i repoet, lenkesjekkede kilder og KI-assistert utforming.

Prosess i korte trekk:

1. Ressurser registreres med ressurs-ID, type og dokumentlenke i registeret.
2. Relevante eksterne lenker brukes som kildegrunnlag ved utfylling av korte beskrivelser.
3. KI brukes til førsteutkast og strukturering, deretter justeres innholdet manuelt.
4. Kapabilitetskoblinger hentes fra koblingsfilen og brukes som metadata i visningen.
5. Genereringsscript bygger oversiktssider med filtrering, kapabilitetsvisning og lenker til detaljerte md-filer.

Verktøy som brukes i dag:

- PowerShell-script for generering av ressurssider.
- Python-script for sammenstilling av kapabilitetssider og koblinger.
- Hugo for bygging og visning av nettstedet.

Denne løsningen er under stadig utvikling. Struktur, innhold og presentasjon justeres fortløpende etter hvert som ressursgrunnlaget modnes.

Dette er en testflate i kontinuerlig forbedring.



