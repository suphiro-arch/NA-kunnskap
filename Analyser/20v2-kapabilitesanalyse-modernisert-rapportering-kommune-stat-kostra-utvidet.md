# Kapabilitesanalyse - modernisert-rapportering-kommune-stat-utvidet

## Metadata
- Løpenummer: 20v2
- Filnavn: 20v2-kapabilitesanalyse-modernisert-rapportering-kommune-stat-kostra-utvidet.md
- Dato: 2026-04-14
- Utarbeidet av / språkmodell: GitHub Copilot / GPT-5.3-Codex
- Kilde/case: Brukerinnspill i chat (limt fra PDF) om modernisert rapportering kommune-stat

## 1. Kort problembilde
Målet er å gi statlige myndigheter nødvendige styringsdata fra kommunesektoren med lav administrativ byrde, ved å gå fra manuelle uttrekk til løpende datadeling. Caset beskriver en moderne datastrøm der notifikasjon og API-henting er hovedmønsteret: kommunalt fagsystem publiserer hendelse (spor A), statlig mottaker henter detaljer via autorisert API (spor B), og kommunen får kvittering på oppfylt rapporteringsplikt. Der API-beredskap mangler, brukes automatisert innsending (spor C) som overgang, med digital avvikshåndtering tilbake til kildesystemet. Gevinstene er mindre årssluttpress, høyere datakvalitet, bedre personvern gjennom redusert deling av sensitive detaljer, og raskere grunnlag for både statlig statistikk og lokal analyse.

## 2. Kapabilitetsmapping
| Kapabilitet | Rolle i helheten (kjerne/støtte) | Hvorfor relevant for problemet | Relevans (høy/middels) |
|---|---|---|---|
| Hendelsesdrevet | kjerne | Trigger i fagsystemet skal starte rapporteringsflyten uten manuelle mellomledd. | høy |
| Dele data med andre | kjerne | Kommunalt kildesystem må dele data strukturert og kontrollert med statlige mottakere. | høy |
| Bruke data fra andre | kjerne | Statlig mottaker må kunne hente detaljer via API etter notifikasjon. | høy |
| Tilgangskontroll | kjerne | API-oppslag må begrenses til det mottaker har hjemmel og formål for. | høy |
| Informasjonsarkitektur | kjerne | Felles modeller og kodeverk er nødvendig for sammenlignbar og stabil rapportering. | høy |
| Juridisk samhandling | kjerne | Løpende deling kommune-stat krever tydelig hjemmel, ansvar og sporbarhet. | høy |
| Sikring av informasjonsflyt og datautveksling | kjerne | Notification-first og API-oppslag krever trygg transport og god beskyttelse av data. | høy |
| Meldingsformidling | støtte | Spor C forutsetter robust og sporbar innsending der API ennå ikke er mulig. | middels |
| Datastyring | støtte | Lokal validering mot KOSTRA-regler og korrigering ved kilden krever tydelige kvalitetsregimer. | middels |
| Organisatorisk samhandling | støtte | Kommune, leverandør og statlige mottakere må samordne innføring og avvikshåndtering. | middels |
| Forvaltningsstandarder | støtte | Felles standarder for hendelser, API og meldingsløp må forankres over tid. | middels |
| Samordning | støtte | Nasjonal innføring krever koordinert prioritering av områder og tempo. | middels |

## 3. Mulige gjenbrukbare ressurser
| Ressurs-ID | Ressursnavn | Relevans (høy/middels/lav) | Hvordan kan den gjenbrukes | Merknad/usikkerhet |
|---|---|---|---|---|
| DIGDIR-010 | Altinn Events | høy | Hendelsespublisering i spor A med lettvektsnotifikasjon uten sensitive detaljer. | Krever felles modell for hendelsestyper og status. |
| DIGDIR-002 | Maskinporten | høy | Sikker autentisering mellom statlig mottaker og kommunalt API i spor B. | Må kombineres med tydelig autorisasjon per formål. |
| DIGDIR-004 | Altinn Autorisasjon | høy | Rettighetsstyring for hvem som kan hente hvilke data i ulike rapporteringsformål. | Krever sektoravklaringer for roller og delegering. |
| DIGDIR-008 | Altinn Formidling | høy | Automatisert innsending i spor C for områder uten moden API-støtte. | Bør brukes som overgangsmønster, ikke permanent sluttløsning. |
| DIGDIR-011 | Felles datakatalog | høy | Beskrivelse av datasett og informasjonsmodeller som inngår i rapporteringen. | Avhenger av oppdatert metadata fra aktørene. |
| DIGDIR-012 | Begrepskatalog | høy | Felles begreper for hendelser, vedtak, status og rapporteringsobjekter. | Krever aktiv tverrsektoriell begrepsforvaltning. |
| DIGDIR-013 | API-katalog | middels | Synliggjør og standardiserer API-kontrakter for datahenting i spor B. | Avhenger av moden API-praksis i leverandørmarkedet. |
| DIGDIR-015 | data.altinn.no | middels | Kan støtte kontrollert datadeling i løp med behov for et standardisert delingslag. | Bør vurderes opp mot faktisk volum, latency og styringsbehov. |
| KS-001 | Fiks-plattformen | middels | Kan brukes som kommunal innføringsplattform for integrasjon og operativ samhandling i overgang til spor A+B. | Krever tydelig avgrensning mot nasjonale felleskomponenter i målarkitekturen. |
| KS-002 | Fiks melding | middels | Kan støtte trygg meldingsutveksling i spor C der API-modenhet er ujevn i sektoren. | Bør håndteres som overgang for å unngå permanent dobbeltspor. |
| NOVARI-003 | FINT Informasjonsmodell | middels | Kan bidra til harmonisering av begreper og informasjonsstrukturer i kommunal leverandørkontekst. | Må samordnes med nasjonale begreps- og API-standarder. |
| FLERE-001 | A-ordningen | middels | Relevant som referanse for hvordan tverrgående rapportering kan standardiseres og forvaltes i stor skala. | Gir erfaringsgrunnlag, men er ikke direkte løsningskomponent i caset. |

| Ressurs-ID | Ressursnavn | Relevans (høy/middels/lav) | Hvordan kan den gjenbrukes | Merknad/usikkerhet |
|---|---|---|---|---|
| DIGDIR-027 | Arkitektur for hendelser | høy | Normerende mønster for notification-first og hendelsesdrevet samhandling. | Ikke en operativ komponent, men viktig for konsistent arkitekturvalg. |
| DIGDIR-034 | Referansearkitektur forespørsel-svar (eOppslag) | høy | Understøtter API-basert uthenting etter mottatt notifikasjon i spor B. | Må konkretiseres i sektorvise API-standarder. |
| DIGDIR-038 | Nasjonal verktøykasse for deling av data | middels | Gir metode for ansvar, datastyring og kvalitet i delingsløp. | Nytten avhenger av faktisk bruk i innføringsarbeidet. |
| DIGDIR-047 | Digitaliseringsvennlig regelverk | middels | Understøtter juridisk avklaring av hjemmel, formål og avgrensning av deling. | Krever juridisk oppfølging utover teknisk prosjektleveranse. |

Vurderingskommentar ved funksjonelt overlapp:
- Ved overlapp mellom Altinn Formidling og Fiks melding i spor C bør valg baseres på mottakerarkitektur, volum, sporbarhetskrav og behov for nasjonal harmonisering.
- Ved overlapp mellom Fiks-plattformen og nasjonale delingskomponenter bør kommunal innføringsstøtte skilles tydelig fra langsiktig målbilde for å unngå permanent dobbeltspor.
- Ved semantisk overlapp mellom FINT Informasjonsmodell og nasjonale begrepsressurser bør begrepsforvaltning samordnes, med en autoritativ definisjon per sentralt begrep.
- Når flere løsninger dekker deler av samme behov, prioriter kombinasjoner som minimerer leverandørlåsning og gir gradvis overgang fra spor C til spor A+B.

## 4. Foreløpig konklusjon
- mest lovende ressurser: Altinn Events, Maskinporten og Altinn Autorisasjon dekker kjernen i spor A+B, mens Altinn Formidling, Fiks-plattformen og Fiks melding gir et realistisk overgangsløp i kommunal innføring.
- viktigste usikkerheter: statlig mottaksmodenhet for API-henting i flere sektorløp, enhetlig semantikk for hendelser og indikatorer, og hastighet i leverandørenes API-standardisering.
- viktige avklaringer å ta stilling til: felles kriterier for når spor C kan brukes, standard for kvittering på oppfylt rapporteringsplikt, og standardisert avviksmelding tilbake til kildesystem.
- eksplisitt vurdering av behov utover dagens grunnlag: tydeligere nasjonal samordning av innføring, forpliktende dialog med SSB/direktorat om veikart fra filmottak til API-oppslag, og pilotering i avgrenset fagområde for dokumentert gevinst.
