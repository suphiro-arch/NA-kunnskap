# Referansearkitektur forespørsel-svar (eOppslag)

## Ressurs ID
DIGDIR-034

## Ressurskategori
Normerende ressurs

## Type normerende ressurs
Referansearkitektur

## Status/Livsfase
Aktiv. Ressursen er publisert som del av Digdirs referansearkitekturer for samhandling.

## Kort beskrivelse
Referansearkitektur forespørsel-svar (eOppslag) er en normerende ressurs for synkront oppslag mellom datakonsument og datatilbyder. Ressursen er viktig fordi den gir et felles mønster for når og hvordan oppslag bør brukes i tverrvirksomhetlig datadeling.

## Formål og normerende rolle
Formålet er å standardisere vurdering og utforming av forespørsel-svar-flyt slik at virksomheter lettere kan etablere samhandling med tydelig rollefordeling og forventet svartid.

Den normerende rollen er styrende/veiledende. Ressursen er ikke et API i seg selv, men en referansearkitektur for analyse, design og kravstilling.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er anbefalt/styrende. Virksomheter forventes å bruke mønsteret når de vurderer synkront oppslag eller forbruk av data fra andre.

Etterlevelse skjer gjennom arkitekturbeslutninger, integrasjonsdesign, anskaffelser og dokumentasjon av samhandlingsvalg. Avvik bør begrunnes når de påvirker samhandlingsevne.

## Kapabiliteter
- Bruke data fra andre
- Forvaltningsstandarder

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Arkitekter og integrasjonsmiljøer | Felles oppslagsmønster | Samhandlingsdesign og API-vurdering | Kjernebrukere |
| Prosjekt- og produktmiljøer | Klarere mønstervalg | Krav og planlegging | Relevans i tidlig fase |
| Datakonsumenter/datatilbydere | Felles forventning til flyt | Tverrvirksomhetlig oppslag | Viktig i avklaringer |

## Normerende innhold
Ressursen beskriver forespørsel-svar-mønsteret med fokus på samspill mellom konsument og tilbyder, samt avgrensning mot andre samhandlingsmønstre.

Den normerende verdien ligger i at den gjør vurdering av synkron samhandling mer sammenlignbar og mindre tilfeldig på tvers av virksomheter.

## Bruksområde
Ressursen bør brukes når virksomheter trenger oppslag med direkte svar, for eksempel ved behov for sanntidsvalidering eller umiddelbar tilgang til data fra andre.

Den er særlig relevant når brukerforløp eller prosesser er avhengige av rask respons fra eksterne datakilder.

## Typiske analyse- og beslutningssituasjoner
- når synkront oppslag vurderes mot meldingsbasert eller hendelsesdrevet samhandling
- når ansvar og avhengigheter mellom datakonsument og tilbyder skal avklares
- når API-krav i anskaffelser skal forankres i felles mønster
- når ytelse, stabilitet og robusthet må vurderes i samhandlingsdesign

## Når ressursen normalt ikke er tilstrekkelig alene
Ressursen er ikke tilstrekkelig alene for implementasjon, sikkerhet eller drift. Den må suppleres med tekniske standarder, juridiske vurderinger, sikkerhetskrav og operative løsninger.

## Scope og avgrensning
Inngår:
- forespørsel-svar som samhandlingsmønster
- roller og flyt mellom datakonsument og datatilbyder
- vurderingsstøtte for oppslagsbasert datadeling

Inngår ikke:
- konkrete API-kontrakter
- detaljert teknisk implementasjon
- komplett styringsmodell for tjenesteforvaltning

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | Digdir publiserer og vedlikeholder referansearkitekturen |
| Endringsprosess | Oppdateres ved videreutvikling av samhandlingsgrunnlag |
| Publiserings- og beslutningsarena | Digdir.no |

## Relasjon til andre ressurser
- **Referansearkitektur forsendelse (eMelding)**: komplementært mønster for asynkron meldingsflyt.
- **Arkitektur for hendelser**: alternativ/utfyllende mønster ved hendelsesdrevet behov.
- **Rammeverk for digital samhandling**: overordnet retning for når mønsteret bør vurderes.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er mer forutsigbar tilgang til data i prosesser som krever direkte svar. Arkitekturverdien er mer konsistente integrasjonsvalg og tydeligere avgrensning mellom synkrone og asynkrone samhandlingsmønstre.

## Konsekvens ved manglende bruk eller avvik
Manglende bruk kan gi uens oppslagsmønstre, uklare avhengigheter og redusert robusthet. Ubegrunnede avvik kan føre til unødvendig kompleksitet og høyere integrasjonskostnad.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Avgrensning | Forespørsel-svar brukes i feil situasjon | Lavere skalerbarhet/robusthet | Sammenligne systematisk med eMelding/hendelser |
| Forankring | Mønstervalg tas uten referansearkitektur | Ulik praksis | Kreve mønsterbegrunnelse i beslutningsgrunnlag |
| Adopsjon | Ulik tolkning på tvers av aktører | Svekket interoperabilitet | Felles begrepsbruk og tydelig dokumentasjon |

## Publiseringsform og tilgjengelighet
Ressursen publiseres som del av Digdirs åpne referansearkitekturer.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** ved å støtte strukturert bruk av data fra andre.
- **P6: Lag digitale løsninger som støtter samhandling** ved å standardisere oppslagsmønster.
- **P2: Ta arkitekturbeslutninger på rett nivå** ved å tydeliggjøre mønstervalg i tidligfase.

Begrensning: Ressursen må kombineres med konkrete tekniske og organisatoriske tiltak for å gi full effekt.

## Lenke til dokumentasjon
- https://www.digdir.no/samhandling/referansearkitekturer/2131

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-04-30
- https://www.digdir.no/samhandling/referansearkitekturer/2131 , kontrollert 2026-04-30
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-04-30
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-04-30
