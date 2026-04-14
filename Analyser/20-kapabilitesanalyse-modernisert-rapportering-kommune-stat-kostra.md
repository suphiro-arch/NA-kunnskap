# Kapabilitesanalyse - modernisert-rapportering-kommune-stat-kostra

## Metadata
- Løpenummer: 20
- Filnavn: 20-kapabilitesanalyse-modernisert-rapportering-kommune-stat-kostra.md
- Dato: 2026-04-14
- Utarbeidet av / språkmodell: GitHub Copilot / GPT-5.3-Codex
- Kilde/case: Brukerinnspill i chat om modernisert rapportering kommune-stat (KOSTRA)

## 1. Kort problembilde
Behovet er å gå fra periodisk, manuell rapportering til løpende datadeling med lav administrativ byrde for kommunene og høy kvalitet for nasjonal styringsinformasjon. Caset krever et notification-first-mønster der hendelser publiseres uten sensitive detaljer, og staten henter nødvendige data via autoriserte API-oppslag. Løsningen må samtidig håndtere et overgangsspor for områder uten API-beredskap og sikre at data kan gjenbrukes både til statlig statistikk og kommunal styring.

## 2. Kapabilitetsmapping
| Kapabilitet | Rolle i helheten (kjerne/støtte) | Hvorfor relevant for problemet | Relevans (høy/middels) |
|---|---|---|---|
| Hendelsesdrevet | kjerne | Hele målbildet bygger på at relevante hendelser i fagsystemene utløser notifikasjon og videre dataflyt. | høy |
| Dele data med andre | kjerne | Kommunale kildesystem må dele data standardisert og sikkert med statlige mottakere. | høy |
| Bruke data fra andre | kjerne | SSB og direktorater må kunne hente og bruke data automatisk til analyse, statistikk og kontroll. | høy |
| Tilgangskontroll | kjerne | API-oppslag må begrenses til data mottaker har hjemmel til å se. | høy |
| Informasjonsarkitektur | kjerne | Felles informasjonsmodeller, kodeverk og semantikk er nødvendig for sammenlignbar KOSTRA-kvalitet. | høy |
| Juridisk samhandling | kjerne | Hjemmelsgrunnlag, formålsavgrensning og regelverk må være tydelig for løpende rapportering av sensitive opplysninger. | høy |
| Meldingsformidling | støtte | Overgangsspor med automatisert innsending trenger robust og sikker transport av meldinger/filer. | middels |
| Datastyring | støtte | Datakvalitet ved kilden, avvikshåndtering og sporbar oppfølging krever tydelig dataansvar og styring. | middels |
| Organisatorisk samhandling | støtte | Kommuner, leverandører og statlige mottakere må samordne innføringstakt, standarder og feilhåndtering. | middels |

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

## 4. Foreløpig konklusjon
- mest lovende ressurser: kombinasjonen Altinn Events, Maskinporten, Altinn Autorisasjon og katalogressursene gir et troverdig mønster for notification-first med rettighetsstyrt API-henting.
- viktigste usikkerheter: statlig mottaksmodenhet for API-oppslag, felles semantikk for hendelser og indikatorer, samt juridisk avgrensning av dataformål.
- viktige avklaringer å ta stilling til: tydelig grense mellom målarkitektur (spor A+B) og overgangsarkitektur (spor C), inklusive avvikshåndtering tilbake til kildesystem.
- eksplisitt vurdering av behov utover dagens grunnlag: sterkere kapabilitet for datakvalitet ved kilden og mer forpliktende tverraktør-samordning vurderes som delvis dekket og bør konkretiseres i videre arbeid.
