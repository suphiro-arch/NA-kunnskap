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

## FormÃ¥l

Denne planen beskriver hvordan repoet kan gÃ¥ fra dagens operative produktstruktur til en bredere ressursstruktur uten Ã¥ miste:
- Ã©n operativ master for register og ressurs-ID
- fungerende webgenerering
- sporbarhet mellom gamle og nye filplasseringer

Planen tar utgangspunkt i at:
- `arkitektur/ressurser/produktnummerering.md` fortsatt er operativ master for registerfÃ¸ring
- `arkitektur/ressurser/` brukes for ny faglig struktur og nye ressursbeskrivelser
- webgrunnlaget fortsatt er tett koblet til dagens produktstruktur

## MÃ¥lbilde

PÃ¥ sikt bÃ¸r repoet ha:
- Ã©n operativ registermaster med eksisterende lÃ¸penummer og ressurs-ID-logikk
- operative beskrivelser samlet under `arkitektur/ressurser/operative-losninger-og-tjenester/`
- normerende ressurser samlet under `arkitektur/ressurser/normerende-ressurser/`
- eventuelle samarbeidsfora samlet under `arkitektur/ressurser/samarbeidsfora/`
- generatorer og webgrunnlag som leser fra ny ressursstruktur

Det bÃ¸r ikke etableres parallelle varige mastere for registerfÃ¸ring.

## Viktigste tekniske observasjoner

- `produktnummerering.md` er fortsatt eneste operative registermaster.
- weben har en eksisterende ressursoversikt under `web/hugo-prototype/content/ressursoversikt/produkter/`.
- generatorgrunnlaget for produktsider ligger i `web/hugo-prototype/scripts/generate-products.ps1`.
- flere repo-deler peker fortsatt til `arkitektur/ressurser/operative-losninger-og-tjenester/`.
- ny ressursstruktur finnes nÃ¥, men brukes forelÃ¸pig bare for nye beskrivelser og styringsfiler.

## Anbefalt migreringsrekkefÃ¸lge

### Fase 1: Stabiliser register og nye ressurser

MÃ¥l:
- bruke eksisterende registerlogikk konsekvent
- fÃ¥ inn nye Novari-ressurser uten Ã¥ rÃ¸re gammel masseflyt ennÃ¥

Oppgaver:
- fÃ¸re nye ressurser i `arkitektur/ressurser/produktnummerering.md`
- opprette nye beskrivelser i `arkitektur/ressurser/` nÃ¥r ressurskategorien tilsier det
- beholde gamle produktbeskrivelser pÃ¥ gammel plass midlertidig
- dokumentere at `arkitektur/ressurser/ressursregister.md` ikke er operativ master

Status:
- gjennomfÃ¸rt for `FINT Felleskomponent`, `FINT Arkiv`, `FINT Informasjonsmodell` og `VIGO`

### Fase 2: Forbered flytting av operative beskrivelser

MÃ¥l:
- kartlegge hvilke skript, lenker og README-er som mÃ¥ oppdateres fÃ¸r flytting
- unngÃ¥ at web og generatorer brekker nÃ¥r fÃ¸rste gruppe beskrivelser flyttes

Oppgaver:
- kartlegge alle eksplisitte referanser til `arkitektur/ressurser/operative-losninger-og-tjenester/`
- gÃ¥ gjennom `web/hugo-prototype/scripts/generate-products.ps1`
- avklare om generatoren skal stÃ¸tte bÃ¥de gammel og ny mappe i en overgangsperiode
- definere om flyttingen skal gjÃ¸res med speiling eller ren flytting

Anbefaling:
- bruk overgangsperiode der generatoren kan lese begge plasseringer
- unngÃ¥ stor engangsflytting fÃ¸r generatoren tÃ¥ler begge kilder

### Fase 3: Migrer fÃ¸rste operative bolk

MÃ¥l:
- teste full flyt pÃ¥ en sammenhengende gruppe operative beskrivelser

Anbefalt fÃ¸rste bolk:
- Digdir

Begrunnelse:
- Digdir-portefÃ¸ljen er stor nok til Ã¥ vÃ¦re en reell test
- den er relativt konsistent og mye brukt i weboversikt og analyser
- den gir god verdi som pilot for flytting, generatorendring og lenkekontroll

Oppgaver:
- flytte Digdir-beskrivelser fra `arkitektur/ressurser/operative-losninger-og-tjenester/` til `arkitektur/ressurser/operative-losninger-og-tjenester/`
- oppdatere dokumentlenker i `produktnummerering.md`
- oppdatere generatoren til Ã¥ lese ny plassering
- regenerere weboversiktene
- kontrollere avvik i lenker, kapabilitetssider og ressursoversikt

### Fase 4: Oppdater webgrunnlaget

MÃ¥l:
- gjÃ¸re weben strukturmessig riktig i forhold til ny ressursmodell

Oppgaver:
- vurdere om `ressursoversikt/produkter/` skal beholdes som URL av hensyn til stabilitet, eller om det bÃ¸r fÃ¥ ny URL senere
- oppdatere generatorlogikk og eventuelle README-er i `web/hugo-prototype/`
- sikre at operative beskrivelser fortsatt vises riktig i ressursoversikten
- vurdere om normerende ressurser senere skal fÃ¥ egen seksjon i weben

Anbefaling:
- behold URL-er og navigasjon stabile i fÃ¸rste runde
- prioriter riktig datagrunnlag fÃ¸r eventuell omdÃ¸ping i weben

### Fase 5: Rydd opp etter overgang

MÃ¥l:
- redusere dobbeltstruktur nÃ¥r den ikke lenger trengs

Oppgaver:
- oppdatere README-er og styringsfiler sÃ¥ de beskriver ny normalsituasjon
- vurdere om `arkitektur/ressurser/operative-losninger-og-tjenester/` skal avvikles eller stÃ¥ igjen som historisk spor
- vurdere om `produktnummerering.md` bÃ¸r fÃ¥ nytt navn nÃ¥r strukturen er moden, for eksempel `ressursregister.md`

## Flyttestrategi

### Anbefalt strategi

1. Behold `produktnummerering.md` som registermaster.
2. Flytt bare beskrivelser, ikke registerlogikken, i fÃ¸rste omgang.
3. GjÃ¸r flytting sektorvis, ikke filvis pÃ¥ kryss og tvers.
4. Oppdater generator og web etter hver sektorvise migrering.
5. Verifiser hver bolk fÃ¸r neste bolk flyttes.

### Ikke anbefalt strategi

- flytte alle beskrivelser i Ã©n stor operasjon
- endre bÃ¥de registermaster, generatorlogikk, webstruktur og filplassering samtidig
- etablere to operative registermastere i lengre tid

## ForeslÃ¥tt gjennomfÃ¸ringsrekkefÃ¸lge

1. Ferdigstille Novari-sporet som pilot for nye ressurstyper.
2. Kartlegge generatoravhengigheter i weben.
3. Oppdatere generatoren for stÃ¸tte til ny plassering.
4. Migrere Digdir som fÃ¸rste operative bolk.
5. Regenerere og kontrollere weboversiktene.
6. Migrere neste sektorvise bolker.
7. Til slutt ta stilling til om `produktnummerering.md` skal fÃ¥ nytt navn.

## Konkret anbefaling for neste arbeidsÃ¸kt

Neste arbeidsÃ¸kt bÃ¸r prioritere:
- teknisk gjennomgang av `web/hugo-prototype/scripts/generate-products.ps1`
- identifisering av alle steder der gammel produktmappe er hardkodet
- forslag til minimal endring som gjÃ¸r generatoren kompatibel med bÃ¥de gammel og ny mappe

Det er fÃ¸rst nÃ¥r dette er pÃ¥ plass at fÃ¸rste sektorvise flyttelÃ¸p bÃ¸r gjennomfÃ¸res.

