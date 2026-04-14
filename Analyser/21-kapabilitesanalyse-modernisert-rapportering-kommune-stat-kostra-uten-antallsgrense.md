# Kapabilitesanalyse - modernisert-rapportering-kommune-stat-kostra-uten-antallsgrense

## Metadata
- Løpenummer: 21
- Filnavn: 21-kapabilitesanalyse-modernisert-rapportering-kommune-stat-kostra-uten-antallsgrense.md
- Dato: 2026-04-14
- Utarbeidet av / språkmodell: GitHub Copilot / GPT-5.3-Codex
- Kilde/case: Brukerinnspill i chat om modernisert rapportering kommune-stat (KOSTRA), analysert uten bruk av retningslinje om antall kapabiliteter

## 1. Kort problembilde
Behovet er å modernisere rapportering fra kommunesektoren til staten ved å erstatte manuelle, periodiske uttrekk med løpende datadeling i en moderne arkitektur. Caset krever både notification-first med hendelser og rettighetsstyrt API-henting, samt overgangsmekanismer for områder som ennå ikke har API-beredskap. Samtidig må løsningen sikre datakvalitet ved kilden, tydelig semantikk, juridisk avklaring og samordnet innføring mellom kommuner, leverandører og statlige mottakere.

## 2. Kapabilitetsmapping
| Kapabilitet | Rolle i helheten (kjerne/støtte) | Hvorfor relevant for problemet | Relevans (høy/middels) |
|---|---|---|---|
| Hendelsesdrevet | kjerne | Målbildet bygger på at relevante endringer i kommunale fagsystem utløser notifikasjoner og videre dataflyt. | høy |
| Dele data med andre | kjerne | Kommunale kildesystem må kunne tilgjengeliggjøre data strukturert og sikkert til statlige mottakere. | høy |
| Bruke data fra andre | kjerne | Statlige aktører må kunne hente og bruke data maskinelt til statistikk, analyse og kontroll. | høy |
| Tilgangskontroll | kjerne | API-oppslag må begrenses til data mottaker faktisk har hjemmel og behov for. | høy |
| Informasjonsarkitektur | kjerne | Felles informasjonsmodeller og kodeverk er nødvendig for sammenlignbare rapporteringsdata. | høy |
| Juridisk samhandling | kjerne | Løpende deling av kommunale data krever tydelig hjemmel, formålsavgrensning og ansvarslinjer. | høy |
| Sikring av informasjonsflyt og datautveksling | kjerne | Notification-first og API-oppslag forutsetter trygg utveksling, kontroll og beskyttelse av data. | høy |
| Meldingsformidling | støtte | Overgangssporet med automatisert innsending trenger robust og sporbar meldingstransport. | middels |
| Datastyring | støtte | Datakvalitet ved kilden, validering og avvikshåndtering krever tydelig dataansvar og kvalitetsregimer. | middels |
| Organisatorisk samhandling | støtte | Kommuner, leverandører og statlige mottakere må samordne prosess, standarder og feilretting. | middels |
| Forvaltningsstandarder | støtte | Felles standarder for API-er, kodeverk og meldingsmønstre må forankres og forvaltes over tid. | middels |
| Tilgangsstyring | støtte | Rettigheter må kunne styres og vedlikeholdes på tvers av ulike aktører, systemer og formål. | middels |
| Autentisering | støtte | Maskinporten og andre tillitsmekanismer forutsetter sikker verifisering av systemidentiteter. | middels |
| Oversikt over API | støtte | Deling i skala krever at statlige mottakere og kommunale leverandører finner og forstår relevante grensesnitt. | middels |
| Oversikt over begreper | støtte | KOSTRA-lignende rapportering blir sårbar hvis aktørene tolker indikatorer og hendelser ulikt. | middels |
| Samordning | støtte | Nasjonal innføring krever koordinert retning, prioritering og tempo på tvers av aktørene. | middels |

Retningslinje:
- 3-6 kjernekapabiliteter med høy relevans.
- 1-3 støttekapabiliteter med middels relevans.
- Kapabiliteter uten delkapabiliteter vurderes som fullverdige på lik linje med øvrige kapabiliteter.
- Kritiske kapabiliteter skal ikke utelates kun for å treffe antall.

## 3. Mulige gjenbrukbare ressurser
| Ressurs-ID | Ressursnavn | Relevans (høy/middels/lav) | Hvordan kan den gjenbrukes | Merknad/usikkerhet |
|---|---|---|---|---|
| DIGDIR-010 | Altinn Events | høy | Publisering og abonnement på hendelsesnotifikasjoner i notification-first-mønster. | Krever avklart hendelsesmodell og volumhåndtering. |
| DIGDIR-002 | Maskinporten | høy | Sikker maskin-til-maskin autentisering ved API-oppslag mot kommunale kildesystem. | Må kombineres med tydelig autorisasjonsmodell. |
| DIGDIR-004 | Altinn Autorisasjon | høy | Støtter rettighets- og rollebasert tilgang til data på tvers av aktører. | Sektorprofil for KOSTRA-behov må avklares. |
| DIGDIR-008 | Altinn Formidling | middels | Overgangsspor for automatisert innsending der API-oppslag ikke er mulig ennå. | Bør være midlertidig spor, ikke sluttmål. |
| DIGDIR-011 | Felles datakatalog | høy | Synliggjøring av datasett, API-er og informasjonsmodeller for rapporteringsløp. | Nytten avhenger av oppdatert metadataforvaltning. |
| DIGDIR-012 | Begrepskatalog | høy | Felles begreper for hendelser, indikatorer og rapporteringsobjekter. | Krever aktiv tverrsektoriell begrepsforvaltning. |
| DIGDIR-013 | API-katalog | middels | Standardisert synliggjøring av API-grensesnitt og kontrakter for datahenting. | Avhenger av moden API-praksis hos leverandører. |
| DIGDIR-015 | data.altinn.no | middels | Kan brukes for kontrollert deling i løp som krever standardisert tilgangslag. | Relevans må avklares mot valgt målarkitektur og volumkrav. |

| Ressurs-ID | Ressursnavn | Relevans (høy/middels/lav) | Hvordan kan den gjenbrukes | Merknad/usikkerhet |
|---|---|---|---|---|
| DIGDIR-027 | Arkitektur for hendelser | høy | Gir referansemønster for hendelsesdrevet deling og notification-first-arkitektur. | Ikke operativ løsning, men viktig normerende føring. |
| DIGDIR-034 | Referansearkitektur forespørsel-svar (eOppslag) | høy | Understøtter API-basert uthenting av data etter mottatt notifikasjon. | Må oversettes til sektorens konkrete API-mønstre. |
| DIGDIR-038 | Nasjonal verktøykasse for deling av data | middels | Gir metode- og styringsstøtte for deling, ansvar og datakvalitet. | Ikke løsningskomponent, men nyttig som arbeidsgrunnlag. |
| DIGDIR-047 | Digitaliseringsvennlig regelverk | middels | Relevant for å avklare hjemmel og regelverksutforming for løpende rapportering. | Krever juridisk oppfølging, ikke teknisk innføring alene. |

## 4. Foreløpig konklusjon
- mest lovende ressurser: kombinasjonen Altinn Events, Maskinporten, Altinn Autorisasjon, Felles datakatalog, Begrepskatalog og API-katalog gir et robust hovedmønster for notification-first og autorisert datahenting.
- viktigste usikkerheter: statlig mottaksmodenhet for API-oppslag, felles semantikk for hendelser og indikatorer, juridisk avgrensning av dataformål, og hvor raskt leverandører kan støtte standardiserte grensesnitt.
- viktige avklaringer å ta stilling til: tydelig skille mellom målarkitektur og overgangsarkitektur, håndtering av avvik tilbake til kilden, og hvem som eier nasjonale standarder og regelsett for denne rapporteringsformen.
- eksplisitt vurdering av behov utover dagens grunnlag: datakvalitet ved kilden og mer forpliktende samordning fremstår fortsatt som delvis dekket, men denne brede analysen viser at grunnlaget i repoet dekker flere relevante kapabiliteter enn den strammere versjonen fikk fram.
