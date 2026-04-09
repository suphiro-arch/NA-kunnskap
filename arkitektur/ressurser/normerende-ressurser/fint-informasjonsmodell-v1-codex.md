# FINT Informasjonsmodell

## Ressurs ID
Ikke fastsatt ennå

## Ressurskategori
Normerende ressurs

## Type normerende ressurs
Informasjonsmodell

## Status/Livsfase
**Under revisjon** - normerende ressurs i aktiv bruk.  
**Fakta:** Novari opplyser at FINT informasjonsmodell versjon 3 har vært i bruk siden 2018, og at versjon 4.0 er under innføring med planlagt produksjonsdato 17. april 2026.

## Kort beskrivelse
FINT Informasjonsmodell er den felles semantiske og strukturelle modellen som beskriver hvilken informasjon fylkeskommunene kan utveksle gjennom FINT-økosystemet. Modellen gir et felles språk for data på tvers av fylkeskommuner, fagsystemer og leverandører, og er en sentral forutsetning for at FINT Felleskomponent, FINT Arkiv og tilhørende integrasjoner kan fungere på en standardisert og leverandøruavhengig måte.

## Formål og normerende rolle
Formålet med ressursen er å etablere en omforent informasjonsstruktur for fylkeskommunal datadeling. Den normerende rollen ligger først og fremst i at modellen definerer hvilke objekter, relasjoner og felt som skal forstås likt på tvers av systemer og organisasjoner.

Ressursen brukes ikke primært som en løsning i drift, men som felles grunnlag for hvordan operative FINT-løsninger skal bygges, kobles sammen og videreutvikles. Den fungerer derfor både som semantisk styringsgrunnlag og som praktisk spesifikasjon for adaptere, klienter og integrasjoner.

Novari beskriver også modellen som et virkemiddel for å redusere leverandøravhengighet og gjøre det mulig å digitalisere én gang og på samme måte for flere fylkeskommuner. Det gjør modellen relevant både for anskaffelser, videreutvikling av eksisterende løsninger og utforming av nye digitale tjenester.

## Kapabiliteter
- **Informasjonsforvaltning: Informasjonsarkitektur**  
  Ressursen strukturerer og modellerer informasjon på en standardisert måte, slik at data kan forstås og brukes likt på tvers av fylkeskommuner og systemleverandører.

- **Informasjonsforvaltning: Oversikt over informasjonsmodeller**  
  Ressursen er selv en sentral informasjonsmodell og gjør det mulig å etablere en felles forståelse av datastrukturer i FINT-økosystemet.

- **Standardisering: Forvaltningsstandarder**  
  Ressursen fungerer som et omforent normerende grunnlag for hvordan informasjon skal representeres og utveksles innenfor de delene av fylkeskommunal samhandling som FINT dekker.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Fylkeskommuner | Felles struktur for data og integrasjoner | Anskaffelse, integrasjon og forvaltning | Viktig for å redusere lokal spesialtilpasning |
| Systemleverandører og adapterutviklere | Tydelige objekter, relasjoner og felt | Implementasjon av adaptere, klienter og API-er | Avgjørende for interoperabilitet og lavere integrasjonskostnad |
| Integrasjons- og arkitektmiljøer | Felles semantisk referanse | Arkitekturvalg, informasjonsflyt og avgrensning | Brukes som grunnlag for teknisk og faglig samordning |
| Novari og FINT-forvaltningen | Styrbart og videreutviklbart modellgrunnlag | Endringsarbeid, versjonering og koordinering | Særlig viktig i overgang fra versjon 3 til 4.0 |

## Normerende innhold
Informasjonsmodellen beskriver hvilke informasjonselementer som kan overføres gjennom FINT Felleskomponent, og hvilke fagområder som inngår i dette felles grunnlaget. Novari oppgir at modellen dekker blant annet administrasjon, utdanning, arkiv, økonomi, ressurs og personvern/samtykke.

Det normerende innholdet består ikke bare i en liste over felter, men i den samlede definisjonen av objekter, relasjoner og struktur på tvers av disse domenene. Dette gjør modellen til et felles semantisk kontraktsgrunnlag mellom kildesystemer, adaptere, API-er og mottakende løsninger.

Ressursen er også publisert i flere former, blant annet som komplett modell og som Java- og C#-modeller. Det viser at den ikke bare er et faglig dokument, men et normerende artefakt som brukes direkte i teknisk implementasjon og test.

Versjon 4.0 markerer et viktig skille i det normerende innholdet. Ifølge Novari skal denne versjonen rydde opp i utgåtte felter, redusere unødvendig kompleksitet og gi et mer konsistent og fremtidsrettet modellgrunnlag enn versjon 3.

## Bruksområde
FINT Informasjonsmodell bør brukes når fylkeskommuner, leverandører eller integrasjonsmiljøer skal avklare hvordan informasjon skal representeres og utveksles gjennom FINT-baserte integrasjoner. Den er særlig relevant i planlegging av nye integrasjoner, ved anskaffelser som skal støtte FINT, og ved vurdering av hvordan eksisterende systemer skal kobles til felleskomponenter og adaptere.

Ressursen er også relevant i arkitektur- og caseanalyser når en ønsker å vurdere om et behov kan løses gjennom eksisterende fylkeskommunale integrasjonsmønstre i stedet for lokale spesialløsninger. I slike analyser fungerer modellen som en indikator på hvor modent og standardisert et informasjonsområde allerede er.

## Når ressursen normalt ikke er tilstrekkelig alene
Informasjonsmodellen er ikke tilstrekkelig alene når en skal realisere en faktisk integrasjon, fordi den må suppleres med operative løsninger og tjenester. I praksis betyr dette blant annet FINT Felleskomponent, relevante API-er, adaptere, integrasjonsoppsett og lokal forvaltningskapasitet.

Ressursen er heller ikke alene nok til å løse spørsmål om ansvar, tilgang, sikkerhet, testregimer eller innføring i hver enkelt fylkeskommune. Den gir et felles semantisk grunnlag, men må kombineres med operative og organisatoriske virkemidler for å gi full effekt.

## Scope og avgrensning
Inngår:
- felles struktur for informasjon som utveksles gjennom FINT
- modellgrunnlag for flere fylkeskommunale fagområder
- versjonering og videreutvikling av modellens objekter, relasjoner og felt
- grunnlag for tekniske modeller og implementasjoner i Java og C#

Inngår ikke:
- selve driften av API-er, adaptere eller integrasjonsplattformer
- lokal implementasjon i hvert enkelt fagsystem
- full styring av sikkerhet, tilgang eller juridiske forhold i den konkrete integrasjonen
- alle typer fylkeskommunale data utenfor de områdene FINT faktisk modellerer

Avgrensningen mot operative FINT-ressurser er viktig: FINT Informasjonsmodell beskriver hvordan informasjon skal forstås og struktureres, mens FINT Felleskomponent og FINT Arkiv beskriver hvordan informasjon eksponeres og brukes i drift.

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Novari/FINT forvalter modellgrunnlaget og videreutvikler det i takt med behovene i fylkeskommunene |
| Forvaltningsansvar | Novari publiserer informasjon, modeller og statusoppdateringer knyttet til ressursen |
| Endringsprosess | Versjon 4.0 er fulgt opp gjennom informasjonsskriv, hørings- og statusløp, testperioder og koordinering med fylkeskommunene |
| Publiserings- og beslutningsarena | Novaris tjeneste- og prosjektsider fungerer som offentlig innsynsflate, mens koordinering skjer gjennom oppnevnte kontakter og statusmøter i omleggingsarbeidet |

## Relasjon til andre ressurser
- **FINT Felleskomponent**  
  Informasjonsmodellen er et normerende grunnlag for hvordan Felleskomponenten eksponerer og formidler data.

- **FINT Arkiv**  
  Arkivressursen bruker den felles modellen for å tilgjengeliggjøre arkivinformasjon på en standardisert måte.

- **Arkivintegrasjoner**  
  Integrasjonene er avhengige av modellen for å kunne omforme og utveksle data på en konsistent måte mellom fagsystem og arkivsystem.

- **VIGO-relaterte løsninger**  
  VIGO og tilhørende løsninger er ikke identiske med FINT, men de inngår i samme fylkeskommunale samhandlingslandskap og er relevante å se opp mot ved caseanalyser i utdanningsdomenet.

## Forretningsverdi og arkitekturverdi
Den viktigste forretningsverdien er at fylkeskommunene får et mer enhetlig grunnlag for digitalisering på tvers av organisasjoner og leverandører. Dette gjør det lettere å stille like krav i anskaffelser, lettere å gjenbruke integrasjoner og mindre kostbart å koble sammen systemer som ellers ville hatt ulike datamodeller.

Den viktigste arkitekturverdien er at ressursen reduserer semantisk fragmentering. Når objekter og relasjoner beskrives likt på tvers, blir det lettere å bygge sammenhengende integrasjoner, oppdage overlapp, sammenligne løsninger og unngå at hver integrasjon må løses som et eget spesialtilfelle.

Overgangen til versjon 4.0 gir også verdi fordi modellen skal bli enklere og mindre historisk tynget. Det kan redusere dobbeltarbeid i adaptere og klienter og gi et mer robust grunnlag for videre utvikling.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Semantisk kvalitet | Eldre felt og historiske tilpasninger gjør modellen unødig kompleks | Høyere implementasjonskostnad og større tolkningsrom | Rydde i modellen og samle endringer i ny hovedversjon |
| Endringsstyring | Overgang fra versjon 3 til 4.0 gir periodevis dobbeltspor og usynkroniserte relasjoner | Feilforståelser, testfeil og midlertidig lavere datakvalitet | Tydelig statuskommunikasjon, testperioder og gradvis overgang |
| Avhengighet til kildesystemer | Omlegging av underliggende datagrunnlag, som InSchool-ressurser, kan forsinke innføringen | Forskyvning av produksjonsdato og usikkerhet i testløp | Samordnet planlegging med leverandører og tydelig datoperiodisering |
| Adopsjon | Ikke alle aktører tolker eller implementerer modellen likt | Svekket samhandling og lavere gjenbruk | Bruke felles dokumentasjon, modeller og tett dialog med leverandører og fylker |
| Sammenheng til operative løsninger | Modellen beskrives uten at operative avhengigheter forstås godt nok | Risiko for å overvurdere hvor mye modellen alene løser | Beskrive modellen sammen med FINT Felleskomponent, Arkiv og integrasjonsløp |

## Publiseringsform og tilgjengelighet
Ressursen publiseres gjennom Novaris tjeneste- og prosjektsider, og Novari viser videre til komplett modell, Java-modeller, C#-modeller, utfyllende beskrivelse, releasenotater og statusmateriale for versjon 4.0. Dette gjør ressursen tilgjengelig både som overordnet faglig beskrivelse og som teknisk implementasjonsgrunnlag.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**  
  Ressursen gjør det mulig å beskrive data på en måte som kan deles og gjenbrukes på tvers av fylkeskommuner og systemleverandører.

- **P6: Lag digitale løsninger som støtter samhandling**  
  Ressursen gir et felles semantisk grunnlag som gjør samhandling og integrasjon mer forutsigbar på tvers av organisatoriske og tekniske grenser.

- **P5: Del og gjenbruk løsninger**  
  Ressursen støtter gjenbruk indirekte ved å gjøre det mulig å utvikle adaptere, integrasjoner og anskaffelser på et felles og standardisert modellgrunnlag.

## Lenke til dokumentasjon
- Novari tjenesteside: https://novari.no/tjenester/fint-informasjonsmodell/
- Prosjektside for versjon 4.0: https://novari.no/prosjekter/informasjonsmodell-versjon-4-0/
- Novari tjenesteoversikt: https://novari.no/tjenester/

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, hentet 2026-04-09
- https://novari.no/tjenester/fint-informasjonsmodell/ , kontrollert 2026-04-09
- https://novari.no/prosjekter/informasjonsmodell-versjon-4-0/ , kontrollert 2026-04-09
- https://novari.no/tjenester/fint-felleskomponent/ , kontrollert 2026-04-09
- https://novari.no/tjenester/fint-arkiv/ , kontrollert 2026-04-09
- https://novari.no/tjenester/arkivintegrasjoner/ , kontrollert 2026-04-09
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-04-09
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-04-09
