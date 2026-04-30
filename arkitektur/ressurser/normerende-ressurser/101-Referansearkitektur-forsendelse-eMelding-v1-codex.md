# Referansearkitektur forsendelse (eMelding)

## Ressurs ID
DIGDIR-033

## Ressurskategori
Normerende ressurs

## Type normerende ressurs
Referansearkitektur

## Status/Livsfase
Aktiv. Ressursen er publisert som del av Digdirs referansearkitekturer for samhandling.

## Kort beskrivelse
Referansearkitektur forsendelse (eMelding) er en normerende ressurs for meldingsbasert forsendelse mellom avsender og mottaker i offentlig samhandling. Ressursen gir et felles mønster for hvordan meldingsflyt kan utformes mer forutsigbart på tvers av virksomheter.

## Formål og normerende rolle
Formålet er å etablere en felles arkitekturforståelse for forsendelsesmønstre, slik at aktører kan beskrive og vurdere meldingsflyt med lavere tolkningsrom.

Den normerende rollen er styrende/veiledende. Ressursen er ikke en operativ transporttjeneste, men et referansegrunnlag som skal brukes i analyse, kravstilling og arkitekturdesign.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er anbefalt/styrende. Virksomheter forventes å bruke mønsteret når meldingsbasert samhandling vurderes eller etableres.

Etterlevelse skjer typisk gjennom arkitekturarbeid, anskaffelser og design av integrasjoner. Avvik bør dokumenteres og begrunnes når de påvirker interoperabilitet og samhandlingsevne.

## Kapabiliteter
- Meldingsformidling
- Forvaltningsstandarder

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Arkitekter og integrasjonsmiljøer | Felles forsendelsesmønster | Løsningsdesign og samhandlingsarkitektur | Kjernebrukere |
| Prosjekt- og produktmiljøer | Tydeligere mønstervalg | Krav og avklaringer i utvikling | Relevant i tidlig fase |
| Virksomheter i datadeling | Forutsigbar meldingsflyt | Samhandling på tvers | Viktig ved flerpartsflyt |

## Normerende innhold
Ressursen beskriver meldingsbasert forsendelse med fokus på roller, samspill og flyt mellom avsender og mottaker.

Den normerende verdien ligger i at den standardiserer hvordan virksomheter kan modellere forsendelsesmønstre før de velger konkret teknologi og plattform.

## Bruksområde
Ressursen bør brukes når virksomheter vurderer asynkron meldingsflyt, behov for robust levering eller tydelig separasjon mellom avsender og mottaker.

Den er særlig relevant i tverrvirksomhetlige forløp der pålitelig overføring og tydelig flytstruktur er viktigere enn synkrone oppslag.

## Typiske analyse- og beslutningssituasjoner
- når meldingsbasert samhandling vurderes mot forespørsel-svar
- når forsendelsesflyt mellom flere aktører skal standardiseres
- når ansvar for avsender-/mottakerroller må tydeliggjøres
- når anskaffelser trenger mønsterforankrede samhandlingskrav

## Når ressursen normalt ikke er tilstrekkelig alene
Ressursen er ikke tilstrekkelig alene for implementasjon eller drift. Den må suppleres med operative løsninger, sikkerhetsmekanismer, juridiske avklaringer og teknisk dokumentasjon.

## Scope og avgrensning
Inngår:
- meldingsbaserte forsendelsesmønstre
- roller og samspill i forsendelsesflyt
- arkitekturfaglig støtte i tidligfase

Inngår ikke:
- valg av konkret plattform eller produkt
- full teknisk spesifikasjon og driftsdesign
- komplett metode for prosjektgjennomføring

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | Digdir publiserer og vedlikeholder referansearkitekturen |
| Endringsprosess | Oppdateres ved videreutvikling av samhandlings- og referansearkitekturgrunnlag |
| Publiserings- og beslutningsarena | Digdir.no |

## Relasjon til andre ressurser
- **Referansearkitektur forespørsel-svar (eOppslag)**: komplementært mønster med synkron samhandlingslogikk.
- **Arkitektur for hendelser**: alternativ/utfyllende mønster for hendelsesdrevet samhandling.
- **Operative meldingsløsninger (f.eks. eFormidling)**: praktiske gjennomføringsflater for mønsteret.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er mer forutsigbar samhandling og redusert risiko for lokale særmønstre. Arkitekturverdien er tydeligere mønsterbruk, bedre interoperabilitet og lavere tolkningsrom mellom aktører.

## Konsekvens ved manglende bruk eller avvik
Manglende bruk kan gi fragmenterte forsendelsesløsninger, uklare rollegrenser og høyere integrasjonskostnader. Ubegrunnede avvik kan svekke robusthet i tverrvirksomhetlige meldingsforløp.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Forankring | Mønsteret brukes ikke tidlig nok | Sen omarbeiding | Ta mønstervalg i konseptfase |
| Avgrensning | Forveksling med andre samhandlingsmønstre | Feil løsningsvalg | Sammenligne eksplisitt med eOppslag/hendelser |
| Adopsjon | Ulik tolkning mellom virksomheter | Lavere interoperabilitet | Dokumentere valg og avvik i arkitekturbeslutninger |

## Publiseringsform og tilgjengelighet
Ressursen publiseres som del av Digdirs åpne referansearkitekturer.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger** ved å fremme gjenbruk av felles samhandlingsmønster.
- **P6: Lag digitale løsninger som støtter samhandling** ved å tydeliggjøre struktur for meldingsflyt.
- **P2: Ta arkitekturbeslutninger på rett nivå** ved å løfte mønstervalg tidlig.

Begrensning: Ressursen gir ikke alene nok styring for operativ implementasjon uten supplement fra konkrete løsninger og standarder.

## Lenke til dokumentasjon
- https://www.digdir.no/samhandling/referansearkitekturer/2131

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-04-30
- https://www.digdir.no/samhandling/referansearkitekturer/2131 , kontrollert 2026-04-30
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-04-30
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-04-30
