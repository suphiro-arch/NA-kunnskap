---
title: "Forside"
weight: 1
description: "Inngang til dokumentasjonen for nasjonal arkitektur, prinsipper, kapabiliteter og nasjonale fellesressurser."
---

# Om denne dokumentasjonen

Denne prototypen samler arbeidsgrunnlag for nasjonal arkitektur i én lesbar dokumentasjonsflate. Målet er å gjøre det enklere å se sammenhengen mellom kapabiliteter, prinsipper og felles ressurser som støtter samhandling på tvers av virksomheter.

## Hva finner du her?

Denne dokumentasjonen er bygget opp rundt tre spørsmål:

- Hvilke evner må økosystemet ha for å lykkes?
- Hvilke føringer bør styre valg av løsninger og prioriteringer?
- Hvilke felles ressurser og produkter kan brukes i praksis?

Svarene ligger i hver sin hovedseksjon:

- [Kapabiliteter](kapabiliteter/) beskriver hvilke evner som må finnes i økosystemet.
- [Prinsipper](prinsipper/) forklarer hvilke arkitekturfaglige føringer som bør styre utviklingen.
- [Ressursoversikt](ressursoversikt/) samler konkrete produkter og fellesløsninger.

## Hvem er den for?

Prototypen er særlig relevant for:

- arkitekter som trenger en felles referanse for samhandling på tvers
- produktledere og forvaltere som må plassere egne løsninger i en større sammenheng
- utviklingsteam som trenger oversikt over tilgjengelige fellesressurser
- beslutningstakere som vil forstå koblingen mellom mål, prinsipper og virkemidler

## Hvordan ressursoversikten bygges

Ressursoversikten og ressursbeskrivelsene er bygget fra kildedata i repoet, lenkesjekkede kilder og KI-assistert utforming. Alt arbeidsgrunnlaget er åpent: registeret, ressursbeskrivelsene, kapabilitetskoblingene og genereringsskriptene ligger i [NA-kunnskap på GitHub](https://github.com/suphiro-arch/NA-kunnskap).

Prosess i korte trekk:

1. Ressurser registreres med ressurs-ID, type og dokumentlenke i registeret.
2. Relevante eksterne lenker brukes som kildegrunnlag ved utfylling av korte beskrivelser.
3. KI brukes til førsteutkast og strukturering, deretter justeres innholdet manuelt.
4. Kapabilitetskoblinger er hentet fra rammeverket. Delkapabiliteter og konkrete koblinger mellom ressurser og kapabiliteter er utarbeidet med KI-støtte og bør kvalitetssikres faglig.
5. Genereringsscript bygger oversiktssider med filtrering, kapabilitetsvisning og lenker til detaljerte md-filer.

Verktøy som brukes i dag:

- PowerShell-script for generering av ressurssider.
- Python-script for sammenstilling av kapabilitetssider og koblinger.
- Kontrollskript som stopper publisering ved tegnkodingsfeil, versjonsavvik mellom register og kapabilitetsmapping, ressursbeskrivelser som mangler seksjoner malen krever, syntaksfeil i innebygd JavaScript, og kildelenker som ikke er registrert.
- Hugo for bygging og visning av nettstedet.

Vil du se hvordan dette henger sammen, ligger både kildefilene og skriptene åpent i [repoet](https://github.com/suphiro-arch/NA-kunnskap).

Løsningen er fortsatt en testflate. Struktur, innhold og presentasjon justeres fortløpende etter hvert som ressursgrunnlaget modnes.
