---
date: 2026-05-21
author: copilot
status: forslag
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
| DIGDIR-047 | Ja/Nei | Regelverksutvikling / Regelverkstolkning / ... | Kort faglig begrunnelse | Fakta / Deduksjon / Usikker |

2. Oppdatert mapping og ressursfiler for godkjente koblinger.
3. Oppdatert next-step med hva som er gjort og hva som gjenstar.

## 5. Observasjon fra kvalitetskjoring

Portefoljesjekk (latest_only) viser at mange filer fortsatt har mangler/advarsler. Dette styrker behovet for trinnvis oppdatering med hoy-prioritert start i normerende ressurser som berorer juridisk samhandling og veiledning.

Filvis sjekk av hoy-prioritert femmer gir forelopig samme minimumsavvik i alle fem filer:

| Ressurs | Resultat |
|---|---|
| DIGDIR-047 | 1 mangel, 1 advarsel (mangler `## Navn`) |
| DIGDIR-025 | 1 mangel, 1 advarsel (mangler `## Navn`) |
| DIGDIR-060 | 1 mangel, 1 advarsel (mangler `## Navn`) |
| DIGDIR-061 | 1 mangel, 1 advarsel (mangler `## Navn`) |
| DIGDIR-031 | 1 mangel, 1 advarsel (mangler `## Navn`) |

Tolkning:
- Dette avviket er strukturelt og likt pa tvers av kandidatene, og bor handteres samtidig med eventuell kapabilitetsoppdatering i samme endringssett.

## 6. Anbefalt neste arbeidsokt

Start med hoy-prioritert femmer:
- DIGDIR-047
- DIGDIR-025
- DIGDIR-060
- DIGDIR-061
- DIGDIR-031

Mål for okten:
- ferdig beslutningstabell
- oppdatert kobling for de ressursene som får Ja
- grønn kvalitetskontroll etter batch 1
