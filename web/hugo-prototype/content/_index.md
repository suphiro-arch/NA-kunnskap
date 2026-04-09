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

Ressursoversikten og ressursbeskrivelsene er bygget fra kildedata i repoet, lenkesjekkede kilder og KI-assistert utforming.

Prosess i korte trekk:

1. Ressurser registreres med ressurs-ID, type og dokumentlenke i registeret.
2. Relevante eksterne lenker brukes som kildegrunnlag ved utfylling av korte beskrivelser.
3. KI brukes til førsteutkast og strukturering, deretter justeres innholdet manuelt.
4. Kapabilitetskoblinger hentes fra koblingsfilen og brukes som metadata i visningen.
5. Genereringsscript bygger oversiktssider med filtrering, kapabilitetsvisning og lenker til detaljerte md-filer.

VerktÃ¸y som brukes i dag:

- PowerShell-script for generering av ressurssider.
- Python-script for sammenstilling av kapabilitetssider og koblinger.
- Hugo for bygging og visning av nettstedet.

Denne lÃ¸sningen er under stadig utvikling. Struktur, innhold og presentasjon justeres fortlÃ¸pende etter hvert som ressursgrunnlaget modnes.

Dette er en testflate i kontinuerlig forbedring.

