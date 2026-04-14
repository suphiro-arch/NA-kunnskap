# Kapabilitesanalyse - modernisert-rapportering-kommune-stat

## Metadata
- Løpenummer: 20
- Filnavn: 20-kapabilitesanalyse-modernisert-rapportering-kommune-stat-kostra.md
- Dato: 2026-04-14
- Utarbeidet av / språkmodell: GitHub Copilot / GPT-5.3-Codex
- Kilde/case: Brukerinnspill i chat om modernisert rapportering kommune-stat med spor A+B som hovedmønster og spor C som overgang

## 1. Kort problembilde
Behovet er å erstatte manuelle uttrekk og tunge rapporteringsperioder med en løpende datastrøm mellom kommune og stat, med minimal administrativ byrde og høy datakvalitet for nasjonal statistikk. Hovedløpet er notification-first: kommunalt fagsystem publiserer hendelse (spor A), og statlig mottaker henter nødvendige detaljer via autorisert API-oppslag (spor B), både ved hendelsesdrevne og tilstandsdrevne triggere. For områder uten API-beredskap må automatisert innsending (spor C) brukes som overgang, samtidig som kvittering og avvik skal tilbakeføres til kilden for rask korrigering og bedre kvalitet.

## 2. Kapabilitetsmapping
| Kapabilitet | Rolle i helheten (kjerne/støtte) | Hvorfor relevant for problemet | Relevans (høy/middels) |
|---|---|---|---|
| Hendelsesdrevet | kjerne | Relevant hendelse i kommunalt fagsystem er trigger for hele rapporteringsflyten. | høy |
| Dele data med andre | kjerne | Kommunalt kildesystem må kunne dele data kontrollert og standardisert med statlig mottaker. | høy |
| Bruke data fra andre | kjerne | Statlig mottaker må kunne hente data maskinelt for statistikk, analyse og kontroll. | høy |
| Tilgangskontroll | kjerne | API-oppslag må være strengt rettighetsstyrt etter hjemmel og formål. | høy |
| Informasjonsarkitektur | kjerne | Felles begreper og modeller er nødvendig for at data tolkes likt på tvers av aktører. | høy |
| Juridisk samhandling | kjerne | Deling kommune-stat krever tydelig hjemmel, ansvarslinjer og sporbarhet. | høy |
| Meldingsformidling | støtte | Trengs i overgangsløp der data fortsatt må sendes som automatisert innsending. | middels |
| Datastyring | støtte | Lokal validering mot KOSTRA-regler og avvik tilbake til kilden forutsetter tydelige kvalitets- og ansvarsregimer. | middels |
| Organisatorisk samhandling | støtte | Felles innføring krever koordinering mellom kommuner, leverandører og statlige mottakere. | middels |

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
| KS-001 | Fiks-plattformen | middels | Kan fungere som kommunal integrasjonsnær plattform i innføring der kommuner trenger et felles operativt lag. | Rollen må avklares mot nasjonale felleskomponenter i målbildet. |
| KS-002 | Fiks melding | middels | Kan støtte overgangsløp for meldingsutveksling der API-modenhet varierer mellom kommuner og leverandører. | Bør brukes kontrollert for å unngå varig parallellarkitektur. |
| FLERE-001 | A-ordningen | middels | Gir et etablert referansemønster for standardisert rapportering på tvers av mange aktører. | Er et mønstergrunnlag, ikke en direkte komponent i denne løsningen. |

Vurderingskommentar ved funksjonelt overlapp:
- Dersom både Altinn Formidling og Fiks melding dekker samme overgangsbehov, velg primærløsning etter mottakers modenhet, volumkrav og behov for nasjonal skalerbarhet.
- Dersom både Fiks-plattformen og nasjonale felleskomponenter kan dekke integrasjonsbehovet, bruk Fiks som innføringslag, men forankre målbilde og grensesnitt i nasjonale standarder.
- Bruk A-ordningen som referanse for styrings- og forvaltningsmodell, ikke som direkte teknisk komponent i dette caset.

## 4. Foreløpig konklusjon
- mest lovende ressurser: Altinn Events, Maskinporten og Altinn Autorisasjon gir en robust kjerne for spor A+B, mens Altinn Formidling, Fiks-plattformen og Fiks melding er relevante i kontrollert overgang og kommunal innføring.
- viktigste usikkerheter: modenhet hos statlige mottakere for API-basert uthenting, semantisk harmonisering på tvers av tjenesteområder og faktisk leverandørstøtte for standardiserte API.
- viktige avklaringer å ta stilling til: kriterier for når spor C er akseptabelt, standard for kvittering og avviksmeldinger tilbake til kildesystem, og tydelig styring av begreper og kodeverk.
- eksplisitt vurdering av behov utover dagens grunnlag: det trengs mer forpliktende samordning av innføring mellom kommune og stat, samt pilotering med SSB/direktorat for å dokumentere effekt i tidsbruk og kvalitet.
