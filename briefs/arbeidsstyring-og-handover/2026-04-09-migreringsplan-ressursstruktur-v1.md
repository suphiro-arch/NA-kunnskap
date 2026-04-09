---
date: 2026-04-09
author: codex
status: draft
topic: migreringsplan-ressursstruktur
sources:
  - arkitektur/ressurser/produktnummerering.md
  - arkitektur/ressurser/styringsregler.md
  - web/hugo-prototype/scripts/generate-products.ps1
  - web/hugo-prototype/README.md
---

# Migreringsplan for ressursstruktur

## Formål

Denne planen beskriver hvordan repoet kan gå fra dagens operative produktstruktur til en bredere ressursstruktur uten å miste:
- én operativ master for register og ressurs-ID
- fungerende webgenerering
- sporbarhet mellom gamle og nye filplasseringer

Planen tar utgangspunkt i at:
- `arkitektur/ressurser/produktnummerering.md` fortsatt er operativ master for registerføring
- `arkitektur/ressurser/` brukes for ny faglig struktur og nye ressursbeskrivelser
- webgrunnlaget fortsatt er tett koblet til dagens produktstruktur

## Målbilde

På sikt bør repoet ha:
- én operativ registermaster med eksisterende løpenummer og ressurs-ID-logikk
- operative beskrivelser samlet under `arkitektur/ressurser/operative-losninger-og-tjenester/`
- normerende ressurser samlet under `arkitektur/ressurser/normerende-ressurser/`
- eventuelle samarbeidsfora samlet under `arkitektur/ressurser/samarbeidsfora/`
- generatorer og webgrunnlag som leser fra ny ressursstruktur

Det bør ikke etableres parallelle varige mastere for registerføring.

## Viktigste tekniske observasjoner

- `produktnummerering.md` er fortsatt eneste operative registermaster.
- weben har en eksisterende ressursoversikt under `web/hugo-prototype/content/ressursoversikt/produkter/`.
- generatorgrunnlaget for produktsider ligger i `web/hugo-prototype/scripts/generate-products.ps1`.
- flere repo-deler peker fortsatt til `arkitektur/ressurser/operative-losninger-og-tjenester/`.
- ny ressursstruktur finnes nå, men brukes foreløpig bare for nye beskrivelser og styringsfiler.

## Anbefalt migreringsrekkefølge

### Fase 1: Stabiliser register og nye ressurser

Mål:
- bruke eksisterende registerlogikk konsekvent
- få inn nye Novari-ressurser uten å røre gammel masseflyt ennå

Oppgaver:
- føre nye ressurser i `arkitektur/ressurser/produktnummerering.md`
- opprette nye beskrivelser i `arkitektur/ressurser/` når ressurskategorien tilsier det
- beholde gamle produktbeskrivelser på gammel plass midlertidig
- dokumentere at `arkitektur/ressurser/ressursregister.md` ikke er operativ master

Status:
- gjennomført for `FINT Felleskomponent`, `FINT Arkiv`, `FINT Informasjonsmodell` og `VIGO`

### Fase 2: Forbered flytting av operative beskrivelser

Mål:
- kartlegge hvilke skript, lenker og README-er som må oppdateres før flytting
- unngå at web og generatorer brekker når første gruppe beskrivelser flyttes

Oppgaver:
- kartlegge alle eksplisitte referanser til `arkitektur/ressurser/operative-losninger-og-tjenester/`
- gå gjennom `web/hugo-prototype/scripts/generate-products.ps1`
- avklare om generatoren skal støtte både gammel og ny mappe i en overgangsperiode
- definere om flyttingen skal gjøres med speiling eller ren flytting

Anbefaling:
- bruk overgangsperiode der generatoren kan lese begge plasseringer
- unngå stor engangsflytting før generatoren tåler begge kilder

### Fase 3: Migrer første operative bolk

Mål:
- teste full flyt på en sammenhengende gruppe operative beskrivelser

Anbefalt første bolk:
- Digdir

Begrunnelse:
- Digdir-porteføljen er stor nok til å være en reell test
- den er relativt konsistent og mye brukt i weboversikt og analyser
- den gir god verdi som pilot for flytting, generatorendring og lenkekontroll

Oppgaver:
- flytte Digdir-beskrivelser fra `arkitektur/ressurser/operative-losninger-og-tjenester/` til `arkitektur/ressurser/operative-losninger-og-tjenester/`
- oppdatere dokumentlenker i `produktnummerering.md`
- oppdatere generatoren til å lese ny plassering
- regenerere weboversiktene
- kontrollere avvik i lenker, kapabilitetssider og ressursoversikt

### Fase 4: Oppdater webgrunnlaget

Mål:
- gjøre weben strukturmessig riktig i forhold til ny ressursmodell

Oppgaver:
- vurdere om `ressursoversikt/produkter/` skal beholdes som URL av hensyn til stabilitet, eller om det bør få ny URL senere
- oppdatere generatorlogikk og eventuelle README-er i `web/hugo-prototype/`
- sikre at operative beskrivelser fortsatt vises riktig i ressursoversikten
- vurdere om normerende ressurser senere skal få egen seksjon i weben

Anbefaling:
- behold URL-er og navigasjon stabile i første runde
- prioriter riktig datagrunnlag før eventuell omdøping i weben

### Fase 5: Rydd opp etter overgang

Mål:
- redusere dobbeltstruktur når den ikke lenger trengs

Oppgaver:
- oppdatere README-er og styringsfiler så de beskriver ny normalsituasjon
- vurdere om `arkitektur/ressurser/operative-losninger-og-tjenester/` skal avvikles eller stå igjen som historisk spor
- vurdere om `produktnummerering.md` bør få nytt navn når strukturen er moden, for eksempel `ressursregister.md`

## Flyttestrategi

### Anbefalt strategi

1. Behold `produktnummerering.md` som registermaster.
2. Flytt bare beskrivelser, ikke registerlogikken, i første omgang.
3. Gjør flytting sektorvis, ikke filvis på kryss og tvers.
4. Oppdater generator og web etter hver sektorvise migrering.
5. Verifiser hver bolk før neste bolk flyttes.

### Ikke anbefalt strategi

- flytte alle beskrivelser i én stor operasjon
- endre både registermaster, generatorlogikk, webstruktur og filplassering samtidig
- etablere to operative registermastere i lengre tid

## Foreslått gjennomføringsrekkefølge

1. Ferdigstille Novari-sporet som pilot for nye ressurstyper.
2. Kartlegge generatoravhengigheter i weben.
3. Oppdatere generatoren for støtte til ny plassering.
4. Migrere Digdir som første operative bolk.
5. Regenerere og kontrollere weboversiktene.
6. Migrere neste sektorvise bolker.
7. Til slutt ta stilling til om `produktnummerering.md` skal få nytt navn.

## Konkret anbefaling for neste arbeidsøkt

Neste arbeidsøkt bør prioritere:
- teknisk gjennomgang av `web/hugo-prototype/scripts/generate-products.ps1`
- identifisering av alle steder der gammel produktmappe er hardkodet
- forslag til minimal endring som gjør generatoren kompatibel med både gammel og ny mappe

Det er først når dette er på plass at første sektorvise flytteløp bør gjennomføres.


