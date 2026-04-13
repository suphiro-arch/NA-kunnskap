# Kapabilitesanalyse - modernisert rapportering kommune stat

## Metadata
- Lopenummer: 17
- Filnavn: 17-kapabilitesanalyse-modernisert-rapportering-kommune-stat.md
- Dato: 2026-04-13
- Kilde/case: analyser/17-Modernisert-rapportering-kommune-stat-analyse.md

## 1. Kort problembilde
Behovet er a ga fra manuell, periodisk rapportering mellom kommune og stat til kontinuerlig, hendelsesdrevet datadeling. Caset krever baade trygg datautveksling, tydelig semantikk og samordnet forvaltningspraksis pa tvers av aktorer.

## 2. Kapabilitetsmapping
| Kapabilitet | Hvorfor relevant for problemet | Tillit (hoy/middels/lav) |
|---|---|---|
| Hendelsesdrevet | Kjernen i malbildet er at hendelser publiseres fortlopende i stedet for periodisk filrapportering | hoy |
| Bruke data fra andre | Statlige mottakere ma kunne hente detaljer via oppslag basert pa hendelser | hoy |
| Dele data med andre | Kommunale fagsystem ma dele strukturert data med statlige aktorer | hoy |
| Meldingsformidling | Overgangsfasen har behov for robust transport av meldinger/datasetter | middels |
| Sikring av informasjonsflyt og datautveksling | Datadeling mellom forvaltningsnivaer krever sikker overforing og kontroll | hoy |
| Informasjonsarkitektur | Felles begreper og datamodeller er en forutsetning for sammenlignbarhet | hoy |

## 3. Mulige gjenbrukbare ressurser
| Ressurs-ID | Ressursnavn | Relevans (hoy/middels/lav) | Hvordan kan den gjenbrukes | Merknad/usikkerhet |
|---|---|---|---|---|
| DIGDIR-010 | Altinn Events | hoy | Hendelsespublisering og abonnement for notifikasjon-forst-monster | Krever avklaring av volum, hendelsestyper og livssyklus |
| DIGDIR-002 | Maskinporten | hoy | Maskin-til-maskin autentisering ved API-oppslag | Krever avklaring av tilgangsstyring per aktorrolle |
| DIGDIR-008 | Altinn Formidling | middels | Overgangslop der API ikke er klart i alle systemer | Bør behandles som overgangsmekanisme, ikke endelig malbilde |
| DIGDIR-011 | Felles datakatalog | hoy | Felles metadata og publisering av datasett/API-er | Krever moden forvaltningspraksis hos dataeiere |
| DIGDIR-012 | Begrepskatalog | hoy | Felles begrepsforvaltning for rapporteringsdomene | Avhenger av aktiv semantisk samordning mellom aktorer |
| DIGDIR-013 | API-katalog | middels | Synliggjore og standardisere tilgjengelige API-grensesnitt | Effekt avhenger av at API-er faktisk etableres |
| DIGDIR-007 | eFormidling | middels | Kan brukes der sikker meldingsutveksling er hovedbehov | Relevans avhenger av valgt teknisk monster i caset |

## 4. Behov for andre kapabiliteter enn dagens grunnlag
| Foreslatt kapabilitet | Hvorfor den trengs i caset | Finnes i dagens grunnlag (ja/nei/delvis) | Konsekvens hvis den mangler |
|---|---|---|---|
| Juridisk samhandling | Deling mellom kommune og stat krever tydelig hjemmel, formalsavklaring og ansvarslinjer | delvis | Teknisk løsning kan bygges, men tas ikke i bruk i praksis |
| Datakvalitet ved kilden | Gevinsten av hendelsesdrevet rapportering krever kvalitet i avsendersystemer | delvis | Flere avvik flyttes bare tidligere i kjeden, uten reell kvalitetsforbedring |
| Samordning av styringspraksis | Endringen krysser virksomhetsgrenser og krever felles prioritering | delvis | Ulik implementering og lav skaleringsevne pa tvers av sektoren |

## 5. Forelopig konklusjon
- mest lovende ressurser: Altinn Events, Maskinporten og datakatalog-ressursene som kombinert monster.
- viktigste usikkerheter: juridisk grunnlag, felles semantikk og modenhet i kommunale kildesystem.
- overgangsmekanisme kan bygges med Altinn Formidling/eFormidling der API-basert modell ikke er klar.
- anbefaling: ga videre til full analyse med juridisk og semantisk avklaring som egne arbeidsspor.
