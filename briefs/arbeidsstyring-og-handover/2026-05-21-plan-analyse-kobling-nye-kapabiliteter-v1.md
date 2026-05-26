---
date: 2026-05-21
author: copilot
status: ferdig
topic: plan-analyse-kobling-nye-kapabiliteter
---

# Plan for analyse av ressurskoblinger mot nye kapabilitetsendringer

## 1. Endringsgrunnlag

Følgende endringer i kapabilitetsmodellen er nye eller utvidet siden forrige runde:

- Juridisk samhandling er utvidet med:
  - Regelverksutvikling
  - Regelverkstolkning
- Veiledning er utvidet med:
  - Utvikling og formidling av veiledning
  - Anvendelse av veiledning
- P6-kobling er styrket for Sluttbrukertjenester.

Kilder:
- arkitektur/kapabiliteter/capabilities.yaml
- arkitektur/prinsipper/principles.md

## 2. Prioritert kandidatliste for vurdering

Prioriteringen er gjort ut fra:
- eksisterende koblinger i register og mapping
- sannsynlig faglig relevans for nye delkapabiliteter
- forventet effekt i analyser og webvisning

### Høy prioritet

1. DIGDIR-047 Digitaliseringsvennlig regelverk
- Fil: arkitektur/ressurser/normerende-ressurser/115-Digitaliseringsvennlig-regelverk-v1-codex.md
- Hvorfor: allerede koblet til Juridisk samhandling og Veiledning, men bør vurderes eksplisitt mot Regelverksutvikling og Regelverkstolkning.

2. DIGDIR-025 Rammeverk for digital samhandling
- Fil: arkitektur/ressurser/normerende-ressurser/85-Rammeverk-for-digital-samhandling-v1-codex.md
- Hvorfor: bærer juridisk samhandlingslag i EIF-sporet, mulig kandidat for mer presis kobling til Regelverkstolkning.

3. DIGDIR-060 Forskrift om IT-standarder i offentlig forvaltning
- Fil: arkitektur/ressurser/normerende-ressurser/137-Forskrift-om-IT-standarder-i-offentlig-forvaltning-v1-codex.md
- Hvorfor: sterk juridisk føring, naturlig kandidat for Regelverksutvikling og/eller Regelverkstolkning.

4. DIGDIR-061 Veileder for virksomhetsautentisering
- Fil: arkitektur/ressurser/normerende-ressurser/138-Veileder-for-virksomhetsautentisering-v1-codex.md
- Hvorfor: tydelig veiledningsressurs, bør vurderes mot både Utvikling og formidling av veiledning og Anvendelse av veiledning.

5. DIGDIR-031 Sjekkliste for sammenhengende tjenester
- Fil: arkitektur/ressurser/normerende-ressurser/99-Sjekkliste-for-sammenhengende-tjenester-v1-codex.md
- Hvorfor: kan være nøkkelressurs for P6 + Sluttbrukertjenester i praksisnære vurderinger.

### Middels prioritet

1. DIGDIR-045 Prosjektveiviseren
- Fil: arkitektur/ressurser/normerende-ressurser/113-Prosjektveiviseren-v1-codex.md
- Hvorfor: veiledningsinnhold med bred bruk, mulig kandidat for Anvendelse av veiledning.

2. DIGDIR-046 Klart språk
- Fil: arkitektur/ressurser/normerende-ressurser/114-Klart-sprak-v1-codex.md
- Hvorfor: praktisk anvendelse av veiledning i tjenesteutforming.

3. DIGDIR-038 Nasjonal verktøykasse for deling av data
- Fil: arkitektur/ressurser/normerende-ressurser/106-Nasjonal-verktoykasse-for-deling-av-data-v1-codex.md
- Hvorfor: veiledningsorientert ressurs med konkret anvendelsesformål.

4. DIGDIR-032 Kart for tjenestekjeder
- Fil: arkitektur/ressurser/normerende-ressurser/100-Kart-for-tjenestekjeder-v1-codex.md
- Hvorfor: relevant for P6 og mulig kobling til Sluttbrukertjenester i samhandlingsforlop.

### Lav prioritet

- Ressurser som kun indirekte nevner regelverk eller veiledning uten tydelig normerende rolle.
- Ressurser med svak eller fraværende kobling til P6/sluttbrukerspor i formål og brukssituasjon.

## 3. Analyseprosess (stegvis)

### Steg A: Kvalitetsport og kandidatbekreftelse

Kjor fullstendighetskontroll for siste versjoner:
- mcp: check_all_resources_completeness(latest_only=true)

Bekreft kandidatlista mot:
- arkitektur/ressurser/produktnummerering.md
- arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml

### Steg B: Ressursvis vurdering

For hver kandidat, dokumenter:
- Eksisterende kapabiliteter i ressursfil
- Om nye delkapabiliteter bor legges til
- Om forklaringstekst i Kapabiliteter-seksjon bor skjerpes
- Om påstand er fakta, deduksjon eller usikker

Beslutningskriterier:
- Ja til ny kobling kun hvis ressursens formal/funksjon faktisk understotter kapabiliteten operativt.
- Nei til ny kobling hvis koblingen bare er tematisk nærhet uten tydelig virkemiddelrolle.

### Steg C: Oppdateringsbatch

Batch 1:
- kun hoy-prioritet

Batch 2:
- middels prioritet etter kontroll av effekt i mapping og web

Etter hver batch:
- kjor tools/sync-resource-metadata.py --apply
- kjor tools/check-resource-version-sync.py
- regenerer berorte websider
- kjor web/hugo-prototype/scripts/validate-text-encoding.py

## 4. Leveranser

1. Analysekort per kandidat (beslutningstabell)

| Ressurs-ID | Ny kobling? | Foreslått kapabilitet | Begrunnelse | Kildestatus |
|---|---|---|---|---|
| DIGDIR-047 | Ja | Juridisk samhandling: Regelverkstolkning | Ressursen brukes for avklaring av juridisk handlingsrom i eksisterende regelverk på tvers av fag og virksomheter. | Fakta + deduksjon |
| DIGDIR-047 | Ja | Veiledning: Anvendelse av veiledning | Veilederen brukes direkte i analyse- og utviklingsløp for vurdering av juridiske barrierer og tidlig beslutningsstøtte. | Fakta + deduksjon |
| DIGDIR-025 | Nei (ny delkapabilitet) | Juridisk samhandling: Regelverkstolkning (beholdt) | Regelverkstolkning er fortsatt presis, men foreløpige forklaringer i øvrige koblinger er erstattet med faglig tekst. | Fakta + deduksjon |
| DIGDIR-060 | Nei | Juridisk samhandling: Regelverkstolkning (beholdt) | Forskriften brukes primært som rettslig tolkningsgrunnlag i praksis. Regelverksutvikling er vurdert, men ikke lagt inn som egen delkapabilitetskobling i denne runden. | Fakta + deduksjon |
| DIGDIR-061 | Ja | Veiledning: Utvikling og formidling av veiledning | Ressursen er utviklet og publisert som felles normerende veileder for virksomhetsautentisering. | Fakta |
| DIGDIR-031 | Nei (ny delkapabilitet) | Sluttbrukertjenester og Tjenestedesign (beholdt) | Ingen ny delkapabilitet lagt til, men foreløpige forklaringer er erstattet med faglig begrunnelse og tydeligere P6-nær effekt. | Fakta + deduksjon |

2. Oppdatert mapping og ressursfiler for godkjente koblinger.
3. Oppdatert next-step med hva som er gjort og hva som gjenstar.

## 5. Statusoppdatering per 2026-05-26

Ferdigstilt siden planen ble opprettet:

1. Hoy-prioritert femmer er gjennomgaatt med faglig beslutning per kandidat
- DIGDIR-047: lagt til `Juridisk samhandling: Regelverkstolkning` og `Veiledning: Anvendelse av veiledning`.
- DIGDIR-025: beholdt juridisk delkapabilitet, og erstattet foreløpige forklaringer for standardisering/datautveksling/samarbeid.
- DIGDIR-060: beholdt `Juridisk samhandling: Regelverkstolkning`; ikke lagt til `Regelverksutvikling` i denne runden.
- DIGDIR-061: lagt til `Veiledning: Utvikling og formidling av veiledning`.
- DIGDIR-031: beholdt kapabilitetssett, og erstattet foreløpige forklaringer for sluttbrukertjenester og tjenestedesign.

2. Kvalitetsport er kjort for kandidatene
- Filvis kompletthetssjekk viser `0 mangler / 0 advarsler` for alle fem kandidatfiler.

3. Porteføljesjekk er kjørt som referanse
- `check_all_resources_completeness(latest_only=true)` viser fortsatt mangler i andre deler av porteføljen, men dette stopper ikke høy-prioritert koblingsrunde.

4. Middels-prioritert batch er nå oppdatert i mapping
- DIGDIR-032: erstattet foreløpige koblingstekster med faglig begrunnelse for `Tjenestekjeder` og `Organisatorisk samhandling`.
- DIGDIR-038: erstattet foreløpige koblingstekster med faglig begrunnelse for `Dele data med andre` og `Datastyring`.
- DIGDIR-045 og DIGDIR-046: beholdt gjeldende delkapabilitetskoblinger i veiledningssporet (`Anvendelse av veiledning`) uten nye delkapabiliteter i denne runden.

## 6. Status etter sluttforing 2026-05-26

Fokus for denne runden er nå gjennomfort, inkludert validering og handover.

1. Konsistens og regenerering
- `tools/sync-resource-metadata.py --apply`: ingen uventede metadataendringer.
- `tools/check-resource-version-sync.py`: grønn.
- `web/hugo-prototype/scripts/generate-capabilities.py`: kjørt.
- `web/hugo-prototype/scripts/validate-text-encoding.py`: grønn.

2. Tekstmessig presisering i ressursfiler
- `DIGDIR-060` er presisert tekstlig slik at `Regelverkstolkning` fremgår som primær kobling i tråd med vedtatt mapping.

3. Handover
- Handover-notat er oppdatert med beslutningstabell, valideringsresultater og avgrensninger for høy- og middels-prioritert batch.

## 7. Neste naturlige oppstart

Anbefalt rekkefolge for videre arbeid etter denne planen:

1. Bruk beslutningene fra høy- og middels-prioritert batch som referanse ved senere revisjoner av normerende ressurser.
2. Følg opp lavprioriterte kandidater i egen runde dersom nye analyser avdekker tydelig koblingsgap.
3. Knytt eventuelle nye koblingsforslag til konkrete ressursendringer, med samme valideringsløp som i denne planen.

## 8. Lavprioritetsvurdering 2026-05-26

Lavprioritet er vurdert i en avgrenset runde med fokus på ressurser som kan se tematisk relevante ut, men som ikke har tydelig nok normerende rolle mot nye delkapabiliteter i denne runden.

| Ressurs-ID | Fil | Beslutning | Vurdering |
|---|---|---|---|
| DIGDIR-033 | `arkitektur/ressurser/normerende-ressurser/101-Referansearkitektur-forsendelse-eMelding-v1-codex.md` | Ingen ny kobling nå | Referansearkitektur for meldingsmønster. Berører ikke direkte de nye delkapabilitetene i juridisk/veiledningssporet, og P6-relevans er allerede indirekte dekket via eksisterende samhandlingskapabiliteter. |
| DIGDIR-034 | `arkitektur/ressurser/normerende-ressurser/102-Referansearkitektur-foresporsel-svar-eOppslag-v1-codex.md` | Ingen ny kobling nå | Referansearkitektur for oppslagsmønster. Faglig nærhet til samhandling, men ikke tydelig grunnlag for nye delkapabiliteter i denne prosessen. |
| DIGDIR-035 | `arkitektur/ressurser/normerende-ressurser/103-Nasjonalt-veikart-v2-codex.md` | Vurder senere | Har samordnings- og styringsrolle, men er ikke primært en normerende veiledningsressurs i forstand av nye delkapabiliteter. Følges opp ved neste strategiske styringsrunde. |
| DIGDIR-036 | `arkitektur/ressurser/normerende-ressurser/104-Orden-i-eget-hus-v1-codex.md` | Ingen ny kobling nå | Metodikk for informasjonsforvaltning. Ingen tydelig operativ støtte for nye juridisk/veiledning-delkapabiliteter utover eksisterende informasjonsforvaltningsspor. |
| DIGDIR-044 | `arkitektur/ressurser/normerende-ressurser/112-Digitaliseringsrundskrivet-v1-codex.md` | Vurder senere | Sterk styringsressurs, men koblingsendring her bør eventuelt tas i egen normeringsrunde for juridisk samhandling og ikke i denne delkapabilitetsbatchen. |

Konklusjon:
- Lavprioritetsrunden ga ingen anbefalte nye koblinger i mapping nå.
- To ressurser (`DIGDIR-035`, `DIGDIR-044`) markeres for eventuell senere vurdering i en egen styrings-/normeringsrunde.

## 9. Opprydding i handover-dokumenter for prosessen

Opprydding er gjennomført slik:

1. Dette plannotatet er markert `ferdig` og inneholder nå full sporbarhet for høy, middels og lav prioritet.
2. Handover-notatet for koblingsplanen er oppdatert med lavprioritetsstatus, slik at ett dokument fungerer som endelig overlevering.
3. `briefs/next-step.md` er oppdatert med sluttstatus for denne prosessen.
