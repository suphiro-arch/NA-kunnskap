# Kapabilitetsanalyse - modernisert rapportering kommune stat

## Metadata
- Løpenummer: 17
- Filnavn: 17-kapabilitesanalyse-modernisert-rapportering-kommune-stat.md
- Dato: 2026-04-13
- Kilde/case: analyser/17-Modernisert-rapportering-kommune-stat-analyse.md

## 1. Kort problembilde
Behovet er å gå fra manuell, periodisk rapportering mellom kommune og stat til kontinuerlig, hendelsesdrevet datadeling. Caset krever både trygg datautveksling, tydelig semantikk og samordnet forvaltningspraksis på tvers av aktører.

## 2. Kapabilitetsmapping
| Kapabilitet | Hvorfor relevant for problemet | Tillit (høy/middels/lav) |
|---|---|---|
| Hendelsesdrevet | Kjernen i målbildet er at hendelser publiseres fortløpende i stedet for periodisk filrapportering | høy |
| Bruke data fra andre | Statlige mottakere må kunne hente detaljer via oppslag basert på hendelser | høy |
| Dele data med andre | Kommunale fagsystem må dele strukturert data med statlige aktører | høy |
| Meldingsformidling | Overgangsfasen har behov for robust transport av meldinger og datasett | middels |
| Sikring av informasjonsflyt og datautveksling | Datadeling mellom forvaltningsnivåer krever sikker overføring og kontroll | høy |
| Juridisk samhandling | Deling mellom forvaltningsnivåer krever tydelig hjemmel, formålsavklaring og ansvarslinjer for å ta løsningen i bruk | middels |
| Informasjonsarkitektur | Felles begreper og datamodeller er en forutsetning for sammenlignbarhet | høy |

## 3. Mulige gjenbrukbare ressurser
| Ressurs-ID | Ressursnavn | Relevans (høy/middels/lav) | Hvordan kan den gjenbrukes | Merknad/usikkerhet |
|---|---|---|---|---|
| DIGDIR-010 | Altinn Events | høy | Hendelsespublisering og abonnement for notifikasjon-først-mønster | Krever avklaring av volum, hendelsestyper og livssyklus |
| DIGDIR-002 | Maskinporten | høy | Maskin-til-maskin-autentisering ved API-oppslag | Krever avklaring av tilgangsstyring per aktørrolle |
| DIGDIR-008 | Altinn Formidling | middels | Overgangsløp der API ikke er klart i alle systemer | Bør behandles som overgangsmekanisme, ikke endelig målbilde |
| DIGDIR-011 | Felles datakatalog | høy | Felles metadata og publisering av datasett og API-er | Krever moden forvaltningspraksis hos dataeiere |
| DIGDIR-012 | Begrepskatalog | høy | Felles begrepsforvaltning for rapporteringsdomene | Avhenger av aktiv semantisk samordning mellom aktører |
| DIGDIR-013 | API-katalog | middels | Synliggjøre og standardisere tilgjengelige API-grensesnitt | Effekt avhenger av at API-er faktisk etableres |
| DIGDIR-007 | eFormidling | middels | Kan brukes der sikker meldingsutveksling er hovedbehov | Relevans avhenger av valgt teknisk mønster i caset |

## 4. Behov for andre kapabiliteter enn dagens grunnlag
| Foreslått kapabilitet | Hvorfor den trengs i caset | Finnes i dagens grunnlag (ja/nei/delvis) | Konsekvens hvis den mangler |
|---|---|---|---|
| Datakvalitet ved kilden | Gevinsten av hendelsesdrevet rapportering krever kvalitet i avsendersystemer | delvis | Flere avvik flyttes bare tidligere i kjeden, uten reell kvalitetsforbedring |
| Samordning av styringspraksis | Endringen krysser virksomhetsgrenser og krever felles prioritering | delvis | Ulik implementering og lav skaleringsevne på tvers av sektoren |

## 5. Foreløpig konklusjon
- mest lovende ressurser: Altinn Events, Maskinporten og datakatalog-ressursene som kombinert mønster.
- viktigste usikkerheter: juridisk grunnlag, felles semantikk og modenhet i kommunale kildesystem.
- overgangsmekanisme kan bygges med Altinn Formidling/eFormidling der API-basert modell ikke er klar.
- anbefaling: gå videre til full analyse med juridisk og semantisk avklaring som egne arbeidsspor.
