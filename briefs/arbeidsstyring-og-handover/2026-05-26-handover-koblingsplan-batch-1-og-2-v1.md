---
date: 2026-05-26
author: codex
status: ferdig
topic: handover-koblingsplan-batch-1-2-og-lavprioritet
sources:
  - arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml
  - arkitektur/ressurser/normerende-ressurser/137-Forskrift-om-IT-standarder-i-offentlig-forvaltning-v1-codex.md
  - briefs/arbeidsstyring-og-handover/2026-05-21-plan-analyse-kobling-nye-kapabiliteter-v1.md
  - arkitektur/ressurser/normerende-ressurser/101-Referansearkitektur-forsendelse-eMelding-v1-codex.md
  - arkitektur/ressurser/normerende-ressurser/102-Referansearkitektur-foresporsel-svar-eOppslag-v1-codex.md
  - arkitektur/ressurser/normerende-ressurser/103-Nasjonalt-veikart-v2-codex.md
  - arkitektur/ressurser/normerende-ressurser/104-Orden-i-eget-hus-v1-codex.md
  - arkitektur/ressurser/normerende-ressurser/112-Digitaliseringsrundskrivet-v1-codex.md
---

# Handover: koblingsplan batch 1, 2 og lavprioritet

## Kort oppsummering

Planen for analyse av koblinger mot nye delkapabiliteter er sluttført for høy- og middels-prioritert kandidatliste.

Gjennomføringen har omfattet:
- faglig oppdatering av koblingsforklaringer i mapping
- selektiv innlegging av nye delkapabiliteter der grunnlaget er tydelig
- validering av versjonssynk, metadata og tegnkoding
- presisering av DIGDIR-060 slik at ressursomtalen matcher vedtatt mappinglinje

## Beslutningstabell (endelig status)

| Ressurs-ID | Beslutning | Resultat i mapping | Kort begrunnelse |
|---|---|---|---|
| DIGDIR-047 | Ja | Lagt til `Regelverkstolkning` og `Anvendelse av veiledning` | Ressursen brukes både til juridisk avklaring og som praktisk veiledning i analyse- og utviklingsløp. |
| DIGDIR-025 | Delvis | Beholdt juridisk delkapabilitet, erstattet foreløpige forklaringer | Regelverkstolkning er presis kobling, mens øvrige forklaringer er gjort faglige. |
| DIGDIR-060 | Nei (ny delkapabilitet) | Beholdt `Regelverkstolkning` som primær kobling | Forskriften brukes primært som rettslig tolkningsgrunnlag. `Regelverksutvikling` er vurdert, men ikke lagt inn som egen kobling. |
| DIGDIR-061 | Ja | Lagt til `Utvikling og formidling av veiledning` | Ressursen er en normerende veileder utviklet og publisert for bred bruk. |
| DIGDIR-031 | Delvis | Beholdt eksisterende kapabiliteter, erstattet foreløpige forklaringer | Ingen ny delkapabilitet lagt til, men forklaringene er skjerpet faglig. |
| DIGDIR-032 | Delvis | Beholdt eksisterende kapabiliteter, erstattet foreløpige forklaringer | Koblingene til tjenestekjeder og organisatorisk samhandling er nå begrunnet faglig. |
| DIGDIR-038 | Delvis | Beholdt eksisterende kapabiliteter, erstattet foreløpige forklaringer | Koblingene til dele data med andre og datastyring er nå begrunnet faglig. |
| DIGDIR-045 | Nei (ny delkapabilitet) | Beholdt `Anvendelse av veiledning` | Dagens delkapabilitet treffer ressursens faktiske bruk i praksis. |
| DIGDIR-046 | Nei (ny delkapabilitet) | Beholdt `Anvendelse av veiledning` | Ressursen brukes direkte i tjenesteutvikling, uten behov for ny delkapabilitet i denne runden. |

## Kjørte kontroller og resultat

Kontroller kjørt i forbindelse med sluttføringen:
- `python tools/sync-resource-metadata.py --apply`
- `python tools/check-resource-version-sync.py`
- `python web/hugo-prototype/scripts/generate-capabilities.py`
- `python web/hugo-prototype/scripts/validate-text-encoding.py`
- `./tools/check-mojibake.ps1`

Resultat:
- grønn synk mellom register og mapping
- ingen uventede metadataendringer
- kapabilitetssider regenerert
- ingen tegnkodingsfeil
- ingen mojibake-funn

## Avgrensninger

- Lavprioriterte kandidater er vurdert, men uten nye anbefalte koblinger i mapping.
- Handover dekker koblingsplanen for høy-, middels- og lavprioritet, samt tekstpresisering for DIGDIR-060.
- Videre revisjoner bør følge samme prinsipp: ny kobling bare når ressursens funksjon tydelig støtter kapabiliteten operativt.

## Lavprioritetsvurdering (sluttført)

| Ressurs-ID | Beslutning | Kort begrunnelse |
|---|---|---|
| DIGDIR-033 | Ingen ny kobling nå | Referansearkitektur for meldingsmønster; ingen tydelig ny kobling mot delkapabiliteter i juridisk/veiledningssporet. |
| DIGDIR-034 | Ingen ny kobling nå | Referansearkitektur for oppslagsmønster; tematisk nærhet, men ikke tydelig normerende virkemiddelrolle for nye delkapabiliteter i denne runden. |
| DIGDIR-035 | Vurder senere | Samordningsressurs med styringsverdi, men bør vurderes i egen styrings-/normeringsrunde framfor i denne delkapabilitetsbatchen. |
| DIGDIR-036 | Ingen ny kobling nå | Metodikk for informasjonsforvaltning; ingen tydelig direkte støtte for nye juridisk/veiledning-delkapabiliteter utover eksisterende spor. |
| DIGDIR-044 | Vurder senere | Sentralt rundskriv med styringsrolle, men koblingsendring bør håndteres i egen normeringsrunde. |

Konklusjon:
- Ingen nye mappingkoblinger anbefales fra lavprioritetsrunden nå.
- `DIGDIR-035` og `DIGDIR-044` tas med som mulige kandidater i senere styrings-/normeringsarbeid.

## Neste anbefalte steg

1. Bruk denne tabellen som referanse ved senere revisjoner av de samme ressursene.
2. Ta `DIGDIR-035` og `DIGDIR-044` i egen styrings-/normeringsbatch ved behov.
3. Behold samme valideringsløp før hver commit/push i koblingsarbeid.
