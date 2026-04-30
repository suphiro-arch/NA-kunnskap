# Arkitektur for hendelser

## Ressurs ID
DIGDIR-027

## Ressurskategori
Normerende ressurs

## Type normerende ressurs
Referansearkitektur

## Status/Livsfase
Aktiv. Ressursen er publisert som del av Digdirs samhandlings- og arkitekturarbeid.

## Kort beskrivelse
Arkitektur for hendelser er en normerende ressurs som beskriver mønstre og føringer for hendelsesdrevet samhandling i offentlig sektor. Ressursen er viktig fordi den gir et felles grunnlag for hvordan hendelser kan publiseres, oppdages og brukes på tvers av virksomheter.

## Formål og normerende rolle
Formålet er å redusere ulik praksis i hendelsesbasert integrasjon og gi virksomheter en tydeligere struktur for valg av mønstre, ansvar og samspill.

Den normerende rollen er styrende og veiledende. Ressursen er ikke en operativ plattform i seg selv, men et referansegrunnlag som skal brukes i analyse, arkitekturvalg og design av samhandlingsløsninger.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er primært anbefalt/styrende. Virksomheter forventes å vurdere ressursen når de etablerer eller videreutvikler hendelsesdrevne løsninger.

Etterlevelse skjer normalt gjennom arkitekturarbeid, løsningsdesign, krav i anskaffelser og samordning mellom dataeiere og databrukere. Avvik krever vanligvis ikke sentral godkjenning, men bør begrunnes faglig.

## Kapabiliteter
- Hendelsesdrevet
- Forvaltningsstandarder

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Arkitekter og integrasjonsmiljøer | Felles mønster for hendelser | Løsningsdesign og samhandlingsarkitektur | Kjernebrukere |
| Produkt- og prosjektmiljøer | Klarere valg i integrasjonsløp | Krav og avklaringer i utvikling | Relevans i tidlig fase |
| Virksomheter som deler data | Forutsigbar samhandling | Publisering og konsum av hendelser | Viktig ved tverrvirksomhetsavhengigheter |

## Normerende innhold
Ressursen beskriver hvordan hendelsesdrevne samhandlingsmønstre kan brukes for å støtte løpende informasjonsflyt mellom aktører. Den bidrar med felles begreper, avgrensninger og arkitekturføringer for når hendelser er egnet.

Den normerende verdien ligger i å gjøre hendelsesdrevet samhandling mer sammenlignbar og mindre personavhengig, slik at virksomheter lettere kan samarbeide om løsninger som reagerer på endringer i data og prosess.

## Bruksområde
Ressursen bør brukes når virksomheter vurderer hendelsesbasert integrasjon, abonnementsmønstre eller behov for raskere og mer løpende samhandling enn klassiske forespørsel-svar-mønstre gir.

Den er særlig relevant i tiltak som krever koordinering på tvers, der flere aktører må reagere på samme hendelser med tydelig rollefordeling.

## Typiske analyse- og beslutningssituasjoner
- når en virksomhet vurderer om hendelsesdrevet samhandling er bedre egnet enn synkrone API-kall
- når publisering og konsum av hendelser må standardiseres mellom flere aktører
- når arkitekturvalg må redusere kobling og polling i tverrvirksomhetsprosesser
- når ansvarsdeling for hendelser, metadata og forvaltning må avklares tidlig

## Når ressursen normalt ikke er tilstrekkelig alene
Ressursen er ikke tilstrekkelig alene for teknisk implementasjon eller drift. Den må suppleres med konkrete plattformer, sikkerhetsmekanismer, operativ dokumentasjon og virksomhetsspesifikke krav.

## Scope og avgrensning
Inngår:
- referanseføringer for hendelsesdrevet samhandling
- mønstre og arkitekturfaglige vurderingspunkter
- støtte til samordning mellom aktører

Inngår ikke:
- drift av hendelsesinfrastruktur
- detaljert teknisk spesifikasjon av konkrete produkter
- full metode for prosjektgjennomføring

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | Digdir publiserer og vedlikeholder ressursen |
| Endringsprosess | Oppdateres ved videreutvikling av samhandlings- og arkitekturgrunnlaget |
| Publiserings- og beslutningsarena | Digdir.no |

## Relasjon til andre ressurser
- **Rammeverk for digital samhandling**: overordnet samhandlingsramme der hendelsesarkitekturen gir konkret mønsterstøtte.
- **Referansearkitektur forespørsel-svar (eOppslag)**: utfyllende mønster med annen samhandlingslogikk som ofte må vurderes opp mot hendelser.
- **Operative hendelsestjenester (f.eks. Altinn Events)**: praktiske gjennomføringsflater som kan implementere mønstre fra ressursen.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er raskere og mer forutsigbar informasjonsflyt i tverrvirksomhetsprosesser. Arkitekturverdien er bedre samhandlingsdesign, redusert unødig kobling mellom løsninger og tydeligere felles praksis for hendelsesbaserte integrasjoner.

## Konsekvens ved manglende bruk eller avvik
Ved manglende bruk øker risikoen for uens implementering av hendelsesmønstre, uklar ansvarsdeling og svakere interoperabilitet. Det kan gi høyere integrasjonskostnad og mer feil i samspill mellom løsninger.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Samordning | Ulik tolkning mellom aktører | Uforutsigbar samhandling | Bruke felles begreper og avklaringer tidlig |
| Adopsjon | Ressursen brukes sent i løpene | Kostbar omarbeiding | Ta mønstervalg i tidligfase |
| Avgrensning | Hendelser brukes der andre mønstre er bedre | Unødig kompleksitet | Vurdere hendelser opp mot forespørsel-svar og behovsbilde |

## Publiseringsform og tilgjengelighet
Ressursen publiseres som åpen samhandlings- og arkitekturressurs på digdir.no.

## Støtter arkitekturprinsipper
- **P2: Ta arkitekturbeslutninger på rett nivå** ved å tydeliggjøre når hendelsesmønstre bør løftes som tverrgående valg.
- **P5: Del og gjenbruk løsninger** ved å støtte gjenbruk av samhandlingsmønstre.
- **P6: Lag digitale løsninger som støtter samhandling** som ressursens hovedformål.

Begrensning: Ressursen må kombineres med operative og tekniske ressurser for å gi full gjennomføringsevne i praksis.

## Lenke til dokumentasjon
- https://www.digdir.no/samhandling/arkitektur-hendelser/4691
- https://www.digdir.no/samhandling/referansearkitekturer/2131

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-04-30
- https://www.digdir.no/samhandling/arkitektur-hendelser/4691 , kontrollert 2026-04-30
- https://www.digdir.no/samhandling/referansearkitekturer/2131 , kontrollert 2026-04-30
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-04-30
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-04-30
