---
date: 2026-05-05
author: codex
status: avviklet
topic: automatiske-rapporter
sources:
  - codex_app automation_update
---

# Automatiske rapporter

Automatiske kjøringer er avviklet, og mappa får ingen nye rapporter. Reglene i [AGENTS.md](../../../AGENTS.md) gjelder for alt arbeid i repoet, og rapportene her er beholdt som historikk.

Denne mappa ble brukt for rapporter fra automatiske Codex-kjøringer mot repoet.

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

Rapportene er arbeidslogg og handover-grunnlag, ikke faglige sluttleveranser.
