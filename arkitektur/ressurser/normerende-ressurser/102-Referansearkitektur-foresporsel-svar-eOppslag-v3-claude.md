# Referansearkitektur forespørsel-svar (eOppslag)

## Navn
Referansearkitektur forespørsel-svar (eOppslag)

## Ressurs ID
DIGDIR-034

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Referansearkitektur

## Status/Livsfase
Aktiv.

**Fakta:** Digdir publiserer eOppslag som ett av to dokumenter på siden om referansearkitekturer, som sist ble oppdatert 18. februar 2025. Selve dokumentet er en udatert PDF.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Når dokumentet sist ble revidert. Det omtaler Felles API-katalog og Altinn autorisasjon som de nasjonale fellesløsningene for registrering av API og delegering, uten å nevne nyere løsninger.

## Kort beskrivelse
Referansearkitektur forespørsel-svar (eOppslag) beskriver tilgjengeliggjøring av data og oppslag i data, sett fra henholdsvis datatilbyder og datakonsument. Den gir et felles arkitekturmønster for når data bør hentes ved forespørsel, hvordan rollene bør forstås, og hvilke avklaringer som må på plass før virksomheter låser API-design eller velger operativ løsning.

Dokumentet har to nivåer. Det generiske mønsteret dekker både synkrone og asynkrone oppslag, tar ikke stilling til kommunikasjonsprotokoll, og gjelder både åpne og tilgangsbegrensede data. eOppslag er den løsningsnære spesialiseringen: synkrone API-kall mot en datatilbyder med tilgangsstyring ved bruk av sikkerhetsbilletter, med et løsningsmønster basert på Maskinporten, Felles API-katalog og Altinn autorisasjon.

## Formål og normerende rolle
Formålet er å etablere en felles arkitekturforståelse for forespørsel-svar som samhandlingsmønster, slik at virksomheter kan kravstille og vurdere oppslagsbasert datadeling konsistent.

Den normerende rollen er anbefalt. Referansearkitekturen er ikke et konkret API eller en ferdig sikkerhetsprofil, men et analyse- og designgrunnlag. Dokumentet sier selv at det ikke er meningen å låse referansearkitekturen til bestemte løsninger, men at de foreslåtte fellesløsningene gir god støtte for synkrone REST-kall med tilgangsstyring basert på OAuth2-token.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er **anbefalt**, forankret som anbefaling i Digitaliseringsrundskrivet. Ingen lov eller forskrift pålegger bruk av referansearkitekturen.

**Fakta:** Digdir skriver at referansearkitekturer normalt ikke er pålagt, men at nasjonale føringer kan komme gjennom Digitaliseringsrundskrivet eller Referansekatalogen. Digitaliseringsrundskrivet (D-2/25) punkt 1.11 sier at referansearkitekturene for eMelding og eOppslag bør benyttes ved nyutvikling av løsninger for informasjonsutveksling. Rundskrivet gjelder statlig sektor. Digdir fører anbefalingen for både stat og kommune i sin oversikt over krav og anbefalinger.

**Fakta:** Digdirs side om referansearkitekturer viser til Digitaliseringsrundskrivet fra 2024. Gjeldende rundskriv er D-2/25 av 27. mai 2025, som har samme anbefaling.

**Deduksjon:** Bruken av Maskinporten, Felles API-katalog og Altinn autorisasjon i løsningsmønsteret er et eksempel, ikke en del av anbefalingen. Rundskrivet anbefaler referansearkitekturen, og dokumentet åpner selv for andre løsninger.

Etterlevelse skjer primært gjennom arkitekturbeslutninger, kravarbeid, løsningsdesign og forvaltning av API-er og datatilganger. Rundskrivet krever ikke at avvik fra en anbefaling begrunnes, men et annet mønster for et oppslagsbehov bør begrunnes ut fra svartid, robusthet, dataminimering, tilgangsstyring, sporbarhet og ansvar.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot eOppslag-dokumentet og Digdirs side om referansearkitekturer.

Referansearkitekturen normerer begge sider av oppslaget like konkret, og er derfor koblet til både `Dele data med andre` og `Bruke data fra andre`. `Tillit: Tilgangsstyring` og `Tillit: Representasjon` er ikke koblet: mønsteret beskriver hvordan tilgang og delegering skal brukes, men evnene leveres av Maskinporten (`DIGDIR-002`) og Altinn Autorisasjon (`DIGDIR-004`). Referansearkitekturen er ikke rettslig forankret, og `Juridisk samhandling` er ikke aktuell.

- **Datautveksling og integrasjon: Dele data med andre**
  Tilbydersiden normeres gjennom prosessene tilgjengeliggjøre data og avgi data: tilby data gjennom et API, registrere API-et i API-katalog og tilgangsstyring, inngå bruksavtale, tildele tilganger og kontrollere sikkerhetsbilletten før data avgis. Det er det definisjonen av kapabiliteten omfatter: veldokumenterte og sikre API-er som andre med lovlig grunnlag kan oppdage og gjenbruke.
- **Datautveksling og integrasjon: Bruke data fra andre**
  Konsumentsiden normeres gjennom prosessene få tilgang til data, delegere rettigheter til databehandler og innhente data: finne API-et, inngå avtale, registrere klienten, innhente samtykke ved behov, hente sikkerhetsbillett og utføre kallet. Dokumentet beskriver også hvordan en leverandør kan opptre på vegne av konsumenten som har behandlingsgrunnlaget.
- **Standardisering: Forvaltningsstandarder**
  Digitaliseringsrundskrivet punkt 1.11 plasserer eOppslag blant arkitektur- og standardkravene og sier at den bør benyttes ved nyutvikling av løsninger for informasjonsutveksling. Løsningsmønsteret bygger på REST, OpenAPI-beskrivelser og OAuth2-token, slik at en virksomhet som følger det, tar i bruk nasjonalt anbefalte spesifikasjoner.
- **Veiledning: Utvikling og formidling av veiledning**
  Referansearkitekturen er publisert veiledning fra Digdir, og Digdir beskriver referansearkitekturer som veiledning til utforming av arkitekturer og løsninger innen et avgrenset område.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Arkitekter og integrasjonsmiljøer | Felles mønster for oppslag og API-basert datadeling | Målarkitektur, løsningsdesign og mønstervalg | Kjernebrukere av ressursen |
| Prosjekt- og produktmiljøer | Tydeligere krav til datatilgang, svartid og ansvar | Tidligfase, kravarbeid, anskaffelser og løsningsutvikling | Bør bruke ressursen før API-design låses |
| Datatilbydere | Forutsigbare krav til eksponering og tilgang | Tilgjengeliggjøring av API og tildeling av tilganger | Eier datakvalitet, kapasitet og tilgangskontroll |
| Datakonsumenter | Avklart bruk av data fra andre | Saksbehandling, validering, kontroll og innsyn | Må forstå både tekniske og juridiske vilkår |
| Leverandører | Opptre på vegne av konsument | Integrasjoner som databehandler | Krever registrert representasjonsforhold |

## Normerende innhold
Mønsteret deler evnen til å dele data på forespørsel i fem kapabiliteter: tilgjengeliggjøre data og avgi data hos tilbyderen, få tilgang til data og innhente data hos konsumenten, og delegere rettigheter til databehandler. Hver av dem er beskrevet som en prosess:

- **Tilgjengeliggjøre data.** Tilbyderen tilbyr data gjennom et API, registrerer API-et i API-katalog og tilgangsstyring, inngår avtale om tilgang og bruk, tildeler tilganger og registrerer eventuelt hvem som kan innhente samtykke.
- **Få tilgang til data.** Konsumenten finner API-et gjennom kataloger, inngår avtale og registrerer klienten som skal bruke sikkerhetsbilletten.
- **Delegere rettigheter til databehandler.** Konsumenten registrerer et representasjonsforhold, slik at en leverandør kan identifisere seg med eget virksomhetssertifikat og opptre på vegne av konsumenten.
- **Innhente data.** Konsumenten innhenter samtykke ved behov, slår opp teknisk endepunkt ved behov, henter en sikkerhetsbillett og utfører kallet.
- **Avgi data.** Tilbyderen autentiserer konsumenten, kontrollerer tilgang mot sikkerhetsbilletten og eventuelle interne regler, og avgir data.

Bruksavtalen kan være bilateral, aksept av generelle vilkår eller en lisens for åpne data. Ved åpne API-er faller trinnene for tilgangsstyring bort. Løsningsmønsteret viser hvordan Maskinporten utsteder sikkerhetsbilletter, Felles API-katalog tar imot OpenAPI-beskrivelser, og Altinn autorisasjon registrerer representasjonsforhold og samtykke, med rettigheter basert på roller i Enhetsregisteret.

## Bruksområde
Ressursen bør brukes når virksomheter vurderer synkront eller oppslagsbasert samspill med en datatilbyder, når en prosess må hente oppdaterte data før den kan fortsette, eller når en tjeneste trenger sikker og avklart tilgang til data fra andre virksomheter.

Dokumentet nevner selv oppslag i et felles register som Folkeregisteret, oppslag hos en annen virksomhet og oppslag i egen virksomhet som eksempler.

## Typiske analyse- og beslutningssituasjoner
- Når et tiltak må velge mellom forespørsel-svar, meldingsutveksling og hendelsesdrevet samhandling.
- Når en datakonsument trenger tilgang til oppdaterte data fra en datatilbyder.
- Når API-krav, sikkerhetsbilletter, tilgangsstyring og logging må beskrives før anskaffelse eller løsningsdesign.
- Når en leverandør skal hente data på vegne av en virksomhet, og representasjonsforholdet må avklares.
- Når avhengighet til ekstern datatilbyder påvirker brukeropplevelse, robusthet eller tjenestenivå.

## Når ressursen normalt ikke er tilstrekkelig alene
Ressursen er ikke tilstrekkelig alene for implementasjon eller drift. Den må suppleres med:
- konkrete API-kontrakter, informasjonsmodeller, begreper og metadata
- tekniske sikkerhetsprofiler, logging og driftskrav
- juridiske avklaringer om formål, behandlingsgrunnlag, taushetsplikt, databehandlerroller og avtaler
- organisatoriske avtaler om datakvalitet, responstid, forvaltningsansvar og feilhåndtering
- operative fellesløsninger for tilgangsstyring, katalog og delegering

Den er heller ikke førstevalg når behovet primært er forsendelse til kjent mottaker, publisering av hendelser til abonnenter eller periodisk bulkdeling.

## Scope og avgrensning
Inngår:
- generisk mønster for forespørsel-svar og oppslag i data
- prosessene for tilgjengeliggjøring, tilgang, delegering, innhenting og avgivelse
- løsningsmønster for synkrone oppslag med sikkerhetsbilletter

Inngår ikke:
- API-spesifikasjon eller datakontrakt
- valg av konkret plattform, produkt eller leverandør
- full teknisk sikkerhetsarkitektur
- juridisk avtaleverk eller sektorvis styringsmodell
- operativ drift, overvåking eller hendelseshåndtering

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | Digdir publiserer referansearkitekturen som PDF på siden om referansearkitekturer |
| Endringsprosess | **Ikke offentlig dokumentert i denne arbeidsøkten:** Endringslogg, versjonsnummer eller beslutningsprosess for dokumentet |
| Publiserings- og beslutningsarena | digdir.no |

## Relasjon til andre ressurser
- **Referansearkitektur forsendelse (eMelding) (`DIGDIR-033`):** komplementært mønster når behovet er forsendelse til kjent mottaker.
- **Arkitektur for hendelser (`DIGDIR-027`):** mønsteret når noe som har skjedd skal publiseres, og tilbyderen ikke bør være tett koblet til kjente konsumenter.
- **Rammeverk for digital samhandling (`DIGDIR-025`):** bredere ramme for juridisk, organisatorisk, semantisk og teknisk samhandling.
- **Digitaliseringsrundskrivet (`DIGDIR-044`):** punkt 1.11 anbefaler eOppslag ved nyutvikling av løsninger for informasjonsutveksling.
- **Referansekatalogen for IT-standarder (`DIGDIR-026`):** kan gi mer konkrete standardkrav der mønsteret skal operasjonaliseres.
- **Maskinporten (`DIGDIR-002`), Felles datakatalog (`DIGDIR-011`) og Altinn Autorisasjon (`DIGDIR-004`):** fellesløsningene løsningsmønsteret bygger på for sikkerhetsbilletter, API-katalog og delegering.
- **Nasjonal verktøykasse for deling av data (`DIGDIR-038`):** praktisk støtte til datadeling som Digdir viser til fra samme side.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er mer forutsigbar tilgang til oppdaterte data i tjenester og prosesser som krever direkte svar. Når datakonsument og datatilbyder beskriver forventninger på samme måte, blir det enklere å avklare ansvar, kvalitet, sikkerhet og tjenestenivå.

Arkitekturverdien ligger i at mønsteret kobler teknisk API-bruk til avtaler, samtykke, delegering og tilgangskontroll, og i at det beskriver begge sider av oppslaget i samme modell.

## Konsekvens ved manglende bruk eller avvik
Hvis ressursen ikke brukes, brukes for sent eller tolkes ulikt, øker risikoen for:
- lokale og usammenlignbare oppslagsmønstre
- uklare rollegrenser mellom datatilbyder, datakonsument og leverandør
- svakere krav til formål, tilgangsstyring, logging og sporbarhet
- sårbare avhengigheter til eksterne API-er
- synkrone oppslag der forsendelse, hendelser eller periodisk datadeling ville vært mer egnet

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Aktualitet | Dokumentet er udatert og viser til løsninger slik de var da det ble skrevet | Løsningseksemplene kan avvike fra dagens fellesløsninger | Kontroller mot gjeldende dokumentasjon for Maskinporten, Felles datakatalog og Altinn Autorisasjon |
| Mønstervalg | eOppslag brukes der behovet egentlig er forsendelse, hendelser eller bulkdeling | Tette avhengigheter og unødvendig last | Sammenlign eksplisitt med eMelding og Arkitektur for hendelser i tidligfase |
| Juridisk avklaring | Formål, behandlingsgrunnlag eller taushetsplikt avklares for sent | Forsinket innføring og svak etterlevelse | Avklar behandlingsgrunnlag før tilgang tildeles |
| Organisatorisk ansvar | Tilbyder og konsument forstår kvalitet, responstid og feilhåndtering ulikt | Uforutsigbare tjenester og konflikter om ansvar | Avtal tjenestenivå, datakvalitet og endringsvarsling |
| Teknisk robusthet | Synkrone kall gir sterke avhengigheter til ekstern tilbyder | Dårlig brukeropplevelse ved feil | Vurder mellomlagring, feilhåndtering og alternative mønstre |

## Publiseringsform og tilgjengelighet
Ressursen publiseres som en åpen PDF på Digdirs side om referansearkitekturer, sammen med eMelding.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** støttes tydelig ved at mønsteret beskriver hvordan data tilgjengeliggjøres og gjenbrukes gjennom avtalte og sikrede API-er.
- **P6: Lag digitale løsninger som støtter samhandling** støttes ved at tilbyder og konsument beskrives i samme modell.
- **P5: Del og gjenbruk løsninger** støttes ved at løsningsmønsteret bygger på nasjonale fellesløsninger for tilgang, katalog og delegering.
- **P7: Sørg for tillit til oppgaveløsningen** støttes ved krav om autentisering, sikkerhetsbilletter, tilgangskontroll og samtykke der det trengs.
- **P2: Ta arkitekturbeslutninger på rett nivå** støttes ved at mønstervalget tas før API-design og plattformvalg låses.

Synkrone oppslag skaper sterkere avhengigheter i kjøretid enn meldings- eller hendelsesmønstre, og mønsteret må derfor vurderes sammen med robusthet, responstid og hvor kritisk tjenesten er. Mønsteret gir svak praktisk effekt uten konkrete API-kontrakter, metadata og forvaltningsavtaler.

## Lenke til dokumentasjon
- https://www.digdir.no/digital-samhandling/referansearkitekturer/2131
- https://www.digdir.no/media/3740/download
- https://www.digdir.no/digitalisering-og-samordning/bruk-gjeldande-referansearkitekturar-ved-utvikling-av-loysingar-informasjonsutveksling/3114
- https://www.regjeringen.no/no/dokumenter/digitaliseringsrundskrivet/id3103320/

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-09-25
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-09-25
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-25
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/referansearkitekturer/2131 , kontrollert 2026-09-25
- https://www.digdir.no/media/3740/download , eOppslag-dokumentet, lest 2026-09-25
- https://www.digdir.no/digitalisering-og-samordning/bruk-gjeldande-referansearkitekturar-ved-utvikling-av-loysingar-informasjonsutveksling/3114 , kontrollert 2026-09-25
- https://www.regjeringen.no/no/dokumenter/digitaliseringsrundskrivet/id3103320/ , punkt 1.11, kontrollert 2026-09-25

## Endringer fra forrige versjon

### Analyseforbedringer
- Selve eOppslag-dokumentet er lest. `v2` bygde på samlesiden for referansearkitekturer alene. `Normerende innhold` gjengir nå de fem kapabilitetene og prosessene i mønsteret, bruksavtaleformene og løsningsmønsteret med Maskinporten, Felles API-katalog og Altinn autorisasjon.
- Forpliktelsesnivået er presisert med samme presisjon som i `101`. `v2` skrev `anbefalt/styrende` og viste til Digdirs side. `v3` navngir Digitaliseringsrundskrivet D-2/25 punkt 1.11, sier at det er en anbefaling og ikke et krav, at rundskrivet gjelder staten, og skiller anbefalingen av mønsteret fra fellesløsningene i løsningseksemplet.
- `Datautveksling og integrasjon: Dele data med andre` er lagt til. Dokumentet normerer tilbydersiden like konkret som konsumentsiden, og `v2` koblet bare konsumentsiden. `Veiledning: Utvikling og formidling av veiledning` er lagt til etter regelen fra 2026-09-25. `Tilgangsstyring` og `Representasjon` er vurdert og ikke koblet, med begrunnelse før lista.
- Kapabilitetspunktene har fullt navn med hovedkapabilitet, slik at `sync-resource-metadata.py` gjenkjenner dem.
- `Relasjon til andre ressurser` har fått ressurs-ID-er. «Tillitstjenester: ID-porten …» er erstattet av de tre fellesløsningene dokumentet faktisk bygger på; ID-porten inngår ikke i mønsteret.
- `Status/Livsfase` sier nå at dokumentet er udatert, og aktualitet er lagt inn som risiko.

### Tekstlige forbedringer
- Formuleringene «Ressursen er særlig relevant når», henvisningen til «den oppdaterte kapabilitetsbeskrivelsen» og «Ved bruk i analyser bør ressursen behandles som …» er fjernet, etter regelen i AGENTS.md.
- Fakta, deduksjon og det som ikke er offentlig dokumentert, er merket.
- Den gamle kortadressen under `/samhandling/` er fjernet fra lenkelista; den videresender til samme side.
