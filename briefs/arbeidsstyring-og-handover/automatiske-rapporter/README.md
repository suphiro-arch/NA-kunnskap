---
date: 2026-05-05
author: codex
status: aktiv
topic: automatiske-rapporter
sources:
  - codex_app automation_update
---

# Automatiske rapporter

Denne mappa brukes for rapporter fra automatiske Codex-kjøringer mot repoet.

Typiske rapporter herfra skal:

- beskrive hvilke ressurser som ble vurdert eller oppdatert
- si tydelig hvilke filer som ble endret
- skille mellom faktiske endringer, forslag og avvik
- peke på neste anbefalte oppfølging når det er relevant

## Kvalitetsport for automatiske kjøringer

Automatiske Codex-kjøringer som oppretter eller endrer markdownfiler i repoet skal følge samme kvalitetskrav som manuelle arbeidsøkter.

Minimumskrav før kjøringen avsluttes:

- kjør eksplisitt kontroll for tegnkodingsfeil på berørte tekstfiler
- rett eventuelle mojibake- eller UTF-8-feil før rapport eller handover ferdigstilles
- legg nye filer til i Git når rapport, register, mapping eller annet publiseringsgrunnlag peker til dem
- oppgi i rapporten hvilke filer som faktisk ble endret
- oppgi om kjøringen bare vurderte innhold, eller også oppdaterte kilder, register, webgrunnlag eller andre avledede filer
- oppdatere `sources/links.md` i samme kjøring hvis rapporten eller ressursarbeidet tar i bruk nye stabile eksterne lenker som mangler i lenkelista
- bruke minst mulig eskalering når Git-steg krever skriving til `.git`

## Smal Git-prosedyre for automatiske kjøringer

Når automasjonen kjører i et miljø der vanlige repo-filer er skrivbare, men `.git` er låst uten eskalering, skal denne rekkefølgen brukes:

1. Gjør alt innholdsarbeid uten eskalering:
   - oppdater ressursfiler, register, mapping, rapporter, `sources/links.md` og eventuelt generert webgrunnlag
2. Kjør alle faglige og tekniske kontroller uten eskalering:
   - versjonssynk
   - encoding-kontroll
   - mojibake-sjekk
   - relevante generatorer og eventuelle repo-spesifikke verifikasjoner
3. Eskaler først når resultatet er klart for publisering:
   - `git add -A`
   - `git commit -m "<presis melding>"`
   - `git push origin main`

Prinsipp:
- Ikke eskaler skript, søk, lesing, skriving av vanlige repo-filer eller validering hvis de kan kjøres utenfor `.git`.
- Eskaler bare de Git-kommandoene som faktisk trenger å oppdatere indeks eller refs.
- Hvis validering feiler, stopp før Git-eskalering og rett innholdet først.

Når en automatisk kjøring endrer tekstfiler som kan påvirke publisert innhold eller videre generering, skal den normalt kjøre minst disse kontrollene:

- `python web/hugo-prototype/scripts/validate-text-encoding.py <berorte-filer-eller-mapper>`
- `powershell -ExecutionPolicy Bypass -File tools/check-mojibake.ps1 -Root <relevant-map>`

For kjøringer som endrer ressursbeskrivelser eller andre filer som mater ressursoversikten, er dette ikke valgfritt. Encoding-feil skal stoppes og rettes i samme kjøring.

Rapportene er arbeidslogg og handover-grunnlag, ikke faglige sluttleveranser.
