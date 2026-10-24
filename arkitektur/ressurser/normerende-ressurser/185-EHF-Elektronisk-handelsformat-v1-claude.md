# EHF (Elektronisk handelsformat)

## Navn
EHF (Elektronisk handelsformat)

## Ressurs ID
DFO-003

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Standard, i form av en familie av tekniske spesifikasjoner for strukturerte handelsdokumenter. EHF er en nasjonal profil av internasjonale spesifikasjoner fra OpenPeppol og av den europeiske normen for elektronisk faktura.

## Status/Livsfase
Aktiv.

**Fakta:** DFØ publiserer spesifikasjonene på anskaffelser.dev. Den norske spesifikasjonssiden for EHF Billing 3.0 er i versjon 3.0.3, og repositoriet for EHF Post-Award G3 på GitHub ble sist endret 2. oktober 2026. Peppol BIS Billing 3.0, som EHF Billing 3.0 bygger på, er hos OpenPeppol publisert som «May 2026 Release».

**Fakta:** Spesifikasjonene er organisert i generasjoner. Gjeldende generasjon for kontraktsoppfølging er EHF Post-Award G3. Den eldre generasjonen G2, med blant annet EHF Invoice and Credit Note 2.0, er fortsatt publisert på anskaffelser.dev. For konkurransefasen er EHF Pre-Award G2 gjeldende, der EHF ESPD 1.2 er publisert som ferdig spesifikasjon og flere andre dokumenter har status RC1.

## Kort beskrivelse
EHF (Elektronisk handelsformat) er en samling spesifikasjoner for strukturerte elektroniske handelsdokumenter mellom kjøpere og leverandører, som faktura, kreditnota, ordre, katalog, pakkeseddel og egenerklæringsskjema i konkurranser. DFØ utvikler og forvalter spesifikasjonene i samarbeid med brukere og tjenesteleverandører. EHF er harmonisert med Peppol BIS der det finnes en Peppol BIS-spesifikasjon, og dokumentene sendes gjennom Peppol-nettverket. EHF Fakturering 3.0 er obligatorisk for faktura til offentlige oppdragsgivere.

## Formål og normerende rolle
Formålet er at kjøpere, leverandører og systemleverandører bruker samme dokumentformater i hele anskaffelsesprosessen, slik at dokumentene kan sendes, mottas og behandles automatisk i økonomi- og innkjøpssystemer på tvers av leverandører og land.

**Fakta:** DFØ beskriver EHF som spesifikasjoner som hjelper systemleverandører å sende og motta digitale transaksjoner, og oppgir at EHF er harmonisert med Peppol BIS der slike spesifikasjoner finnes, for å støtte samhandling mellom land. Peppol-myndighetssiden til DFØ begrunner en nasjonal spesifikasjon med at den gir et land mulighet til å uttrykke nasjonale behov, samtidig som nasjonale spesifikasjoner bør harmoniseres med Peppol BIS for å redusere implementeringskostnadene.

**Fakta:** For faktura er den norske tilpasningen lagt inn i den internasjonale spesifikasjonen. EHF Billing 3.0 er den norske implementasjonen av EN 16931 etter direktiv 2014/55/EU, gjennom Peppol BIS Billing 3.0, som er en CIUS (Core Invoice Usage Specification) av EN 16931. Spesifikasjonen sier at de norske reglene er innarbeidet i Peppol BIS Billing 3.0, at det ikke lages en egen norsk CIUS, og at EHF Billing 3.0 implementeres ved å implementere Peppol BIS Billing 3.0 uten utvidelser eller ekstra regler. EHF Fakturering 3.0 er navnet som brukes i norsk regelverk.

Rollen er delt: fakturadelen og ESPD er **obligatoriske**, resten av EHF er **anbefalt**. Se `Forpliktelsesnivå og etterlevelse`.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er **obligatorisk for faktura og ESPD**, og **anbefalt** for de øvrige EHF-dokumentene.

**Fakta:** Forskrift om elektronisk faktura i offentlige anskaffelser (FOR-2019-04-01-444) er hjemlet i anskaffelsesloven § 16 tredje ledd og gjennomfører direktiv 2014/55/EU. Etter § 2 gjelder den fakturering knyttet til anskaffelser som er omfattet av anskaffelsesloven, for oppdragsgivere som nevnt i anskaffelsesloven § 2 annet ledd. Etter § 4 er godkjente standardformater under EØS-terskelverdi «EHF (Elektronisk handelsformat) fakturering versjon 3.0 eller nyere» og PEPPOL BIS Billing v3.0 eller nyere. Over EØS-terskelverdi godtas i tillegg andre formater som implementerer EN 16931. Etter § 5 skal oppdragsgiveren kreve elektronisk faktura i godkjent format i kontraktene, kunne motta faktura gjennom PEPPOL-nettverket og rapportere antall mottatte fakturaer til DFØ. § 6 gir unntak for faktura med taushetsbelagte opplysninger når tilfredsstillende tekniske sikringsløsninger mangler.

**Fakta:** Forskrift om IT-standarder i offentlig forvaltning § 10 krever at offentlige virksomheter bruker EHF for mottak av elektronisk faktura og kreditnota, og at leverandører som sender elektronisk faktura eller kreditnota til offentlige virksomheter, gjør det i EHF. For utenlandske leverandører gjelder Peppol BIS på samme måte.

**Fakta:** Referansekatalogen for IT-standarder, siden for digitale anskaffelser, fører EHF Fakturering 3.0 og Peppol BIS Billing 3.0 som obligatoriske fra 1. april 2019, med forskrift om elektronisk faktura i offentlige anskaffelser som grunnlag. EHF Egenerklæringsskjema (ESPD) er obligatorisk for offentlige virksomheter å utstede og motta ved anskaffelser over EØS-terskelverdi, med anskaffelsesforskriften § 17-1 og regjeringens veileder for ESPD som grunnlag. Øvrige EHF-dokumenter i konkurransefasen, EHF Katalog, EHF Ordre og ordrebekreftelse, EHF Pakkeseddel og EHF Purring er ført som anbefalt.

Hjemmelen dekker altså fakturaformatet og ESPD, ikke EHF som helhet. Kravene treffer både offentlige oppdragsgivere og leverandørene deres.

**Fakta:** Etter § 5 i fakturaforskriften kan oppdragsgiveren holde tilbake betaling når leverandøren ikke sender faktura i godkjent format, og betalingsfristen løper da først fra elektronisk faktura er levert.

**Ikke offentlig dokumentert i denne arbeidsøkten:** at det føres tilsyn med oppdragsgivernes etterlevelse utover rapporteringen av antall mottatte fakturaer til DFØ.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`. `Standardisering: EU standarder` er ikke satt: EHF Fakturering 3.0 implementerer EN 16931, men er vedtatt som obligatorisk standard i norsk regelverk, og `Forvaltningsstandarder` omfatter etter definisjonen også EU-harmoniserte standarder som er vedtatt i norsk forvaltning. `Datautveksling og integrasjon: Meldingsutveksling` er ikke satt, fordi transporten leveres av Peppol eDelivery (`OPP-001`) og oppslaget av mottakere av ELMA (`DIGDIR-023`). `Juridisk samhandling: Regelverkstolkning` og `Regelverksutvikling` er vurdert og ikke satt: EHF er forankret i forskrift, men spesifikasjonene tolker ikke regelverket og former ikke nytt regelverk.

- **Standardisering: Forvaltningsstandarder** EHF er den nasjonale standarden for elektronisk faktura og andre handelsdokumenter, utviklet og forvaltet av DFØ, med fakturadelen gjort obligatorisk i forskrift og ført i Referansekatalogen for IT-standarder.
- **Informasjonsforvaltning: Informasjonsarkitektur** spesifikasjonene strukturerer innholdet i handelsdokumentene med felles semantisk modell, syntaks, kodelister og valideringsregler, slik at dokumentene kan behandles maskinelt likt hos avsender og mottaker.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige oppdragsgivere | Motta og behandle faktura automatisk | Fakturamottak, kontraktsvilkår og ESPD i konkurranser | Pliktsubjekter etter fakturaforskriften og forskrift om IT-standarder § 10 |
| Leverandører til offentlig sektor | Vite hvilket format faktura skal sendes i | Elektronisk fakturering | Norske leverandører skal bruke EHF, utenlandske Peppol BIS |
| Systemleverandører for økonomi- og innkjøpssystemer | Spesifikasjoner, valideringsregler og eksempelfiler | Implementering av utsending, mottak og validering | DFØ retter spesifikasjonene primært mot denne gruppen |
| Aksesspunktleverandører | Kjenne dokumenttyper og profiler | Formidling i Peppol-nettverket | Transporterer EHF-dokumentene, men eier ikke formatet |
| Private kjøpere og selgere | Felles format i handel mellom virksomheter | Ordre, katalog, faktura | Kildene viser ikke et krav om EHF i rent privat handel |

## Normerende innhold
**Fakta:** EHF Post-Award G3 omfatter spesifikasjonene EHF Advanced Ordering 3.0, EHF Catalogue 3.0, EHF CV 1.0, EHF CV Request 1.0, EHF Despatch Advice 3.0, EHF Fakturering og Peppol BIS Billing, EHF Forward Billing 3.0, EHF Order Agreement 3.0, EHF Ordering 3.0, EHF Payment Request 3.0, EHF Punch Out 3.0, EHF Reminder 3.0, EHF Selvfakturering og Peppol BIS Self-Billing 3.0 og Peppol Logistics 1.3. EHF Pre-Award G2 omfatter EHF ESPD 1.2 og, med status RC1, EHF Document Folder, EHF Pre-Award Cataloguing, EHF Supplier List og EHF Supplier List Light.

**Fakta:** DFØ oppgir at spesifikasjonene bygger på OASIS UBL og CEN-standarder. For faktura ligger den semantiske modellen i EN 16931, og Peppol BIS Billing 3.0 legger til regler, kodelister og Schematron-filer for validering.

**Fakta:** De norske reglene i EHF Billing 3.0 gjelder blant annet teksten «Foretaksregisteret» på faktura fra aksjeselskap, allmennaksjeselskap og filial av utenlandsk selskap, jf. foretaksregisterloven § 10-2, kategorier og satser for merverdiavgift og strukturert betalingsinformasjon for kortbetaling, kontooverføring, direktedebitering og giro.

**Fakta:** DFØ deler endringer i tre nivåer: feilretting, mindre endringer med kort eller middels varslingstid, og større endringer som ikke er bakoverkompatible og krever lang innføringstid. Varsling skjer gjennom markedsdialog og utgivelsesnotater.

## Bruksområde
EHF bør legges til grunn når en virksomhet skal motta eller sende elektronisk faktura i offentlige anskaffelser, når et økonomi- eller innkjøpssystem skal støtte digital handel med offentlig sektor, og når en anskaffelse skal digitaliseres videre fra konkurranse til ordre, katalog og fakturering.

EHF avklarer hvordan innholdet i handelsdokumentene skal se ut. Hvordan dokumentene transporteres og adresseres, avklares i Peppol eDelivery og ELMA.

## Typiske analyse- og beslutningssituasjoner
- når en oppdragsgiver skal formulere kontraktskrav om elektronisk faktura
- når en virksomhet velger eller bytter økonomisystem og må avklare hvilke EHF-dokumenter systemet skal støtte
- når en innkjøpsprosess skal digitaliseres utover faktura, og det må vurderes hvilke anbefalte EHF-dokumenter som skal tas i bruk
- når faktura med taushetsbelagt innhold skal vurderes mot unntaket i fakturaforskriften § 6
- når handel med utenlandske leverandører krever avklaring av forholdet mellom EHF og Peppol BIS

## Når ressursen normalt ikke er tilstrekkelig alene
EHF beskriver dokumentinnholdet, men ikke hvordan dokumentet kommer fram. Bruken forutsetter Peppol eDelivery for transport gjennom aksesspunkt og ELMA for oppslag av mottakerens adresse og hvilke dokumenttyper mottakeren kan ta imot. Plikten til å bruke formatet følger av fakturaforskriften og forskrift om IT-standarder, ikke av spesifikasjonene. Selve anskaffelsesprosessen reguleres av anskaffelsesregelverket.

## Scope og avgrensning
Inngår:
- spesifikasjoner for handelsdokumenter i konkurransefasen og i kontraktsoppfølgingen
- norske regler og tilpasninger i felles Peppol BIS-spesifikasjoner
- valideringsregler, kodelister og eksempelfiler
- varsling og utgivelse av nye versjoner

Inngår ikke:
- transport, adressering og sikring av dokumentene, som ligger i Peppol eDelivery (`OPP-001`)
- oppslag av mottakere og registrering av mottakskapasitet, som ligger i ELMA (`DIGDIR-023`)
- de internasjonale Peppol BIS-spesifikasjonene og EN 16931 som grunnlag, som forvaltes av OpenPeppol og CEN
- plikten til å bruke formatet, som følger av forskrift

Avgrensning mot forskrift om IT-standarder (`DIGDIR-060`): forskriften gjør EHF obligatorisk for fakturamottak, mens EHF er selve standarden forskriften peker på.

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | DFØ utvikler EHF i samarbeid med brukere og tjenesteleverandører. OpenPeppol forvalter Peppol BIS, som EHF er harmonisert med |
| Forvaltningsansvar | DFØ. **Fakta:** anskaffelser.dev oppgir at spesifikasjonene for EHF Post-Award G3 forvaltes av DFØ for bruk i Peppol-nettverket. Spesifikasjonsteksten for EHF Billing 3.0 omtaler fortsatt Difi som den som innarbeidet de norske reglene i Peppol BIS Billing 3.0 |
| Endringsprosess | **Fakta:** Feil og endringsønsker for EHF Billing 3.0 meldes som Request for Change i OpenPeppol Service Desk, fordi fakturaspesifikasjonen er Peppol BIS Billing 3.0. Øvrige EHF-spesifikasjoner endres etter DFØs varslingsregime med feilretting, mindre og større endringer |
| Publiserings- og beslutningsarena | Spesifikasjonene publiseres på anskaffelser.dev og i repositorier under `anskaffelser` på GitHub. Normeringsstatus fastsettes i forskrift og i Referansekatalogen for IT-standarder |

**Fakta om Peppol-myndighetsrollen:** DFØ omtaler seg på anskaffelser.no som norsk Peppol-myndighet. Siden oppgir at den norske Peppol-myndigheten har ansvar for tre domener: eProcurement, forvaltet av Digdir, og eGov og Payment, som begge forvaltes av DFØ, ved to ulike divisjoner. Den norske Peppol-myndigheten er medlem av Peppol Authority Community. Den samme siden oppgir at ELMA er den offisielle norske SMP-en, forvaltet av Digdir.

**Ikke offentlig dokumentert i denne arbeidsøkten:** hvordan domenefordelingen mellom DFØ og Digdir henger sammen med at DFØ forvalter EHF-spesifikasjonene for faktura og ordre, og om domenet eProcurement i denne sammenhengen omfatter EHF-dokumentene.

## Relasjon til andre ressurser
- **Peppol eDelivery (`OPP-001`)**: transportnettverket EHF-dokumentene sendes gjennom. Fakturaforskriften § 5 krever at oppdragsgiveren kan motta faktura gjennom PEPPOL-nettverket.
- **ELMA (`DIGDIR-023`)**: den norske SMP-en der mottakere og dokumenttypene de kan motta, er registrert.
- **Forskrift om IT-standarder i offentlig forvaltning (`DIGDIR-060`)**: § 10 gjør EHF obligatorisk for fakturamottak i offentlige virksomheter og for leverandørenes faktura.
- **Referansekatalogen for IT-standarder (`DIGDIR-026`)**: fører EHF Fakturering 3.0 og ESPD som obligatoriske og øvrige EHF-dokumenter som anbefalt.
- **Statens standardavtaler (`DFO-002`)**: en annen standard fra DFØ for offentlige anskaffelser. SSA standardiserer kontraktsvilkår, EHF standardiserer dokumentene i handelen.
- **Forskrift om elektronisk faktura i offentlige anskaffelser**: hjemmelen for fakturakravet. Den er ikke egen ressurs i registeret.
- **Peppol BIS og EN 16931**: de internasjonale spesifikasjonene EHF bygger på, forvaltet av OpenPeppol og CEN. De er ikke egne ressurser i registeret.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er automatisk behandling av faktura og andre handelsdokumenter, uten manuell registrering og uten egne avtaler om format mellom hver kjøper og leverandør. Fordi EHF Billing 3.0 er det samme som Peppol BIS Billing 3.0, kan norske og utenlandske leverandører bruke samme implementasjon.

Arkitekturverdien er et felles semantisk grunnlag for handelsdokumenter i hele offentlig sektor, med et tydelig skille mellom dokumentinnhold, transport og mottakeroppslag.

## Konsekvens ved manglende bruk eller avvik
Sender en leverandør faktura i et annet format enn de godkjente, kan oppdragsgiveren holde tilbake betalingen etter fakturaforskriften § 5. En oppdragsgiver som ikke kan motta EHF gjennom Peppol-nettverket, bryter både fakturaforskriften og forskrift om IT-standarder § 10.

**Deduksjon:** For de anbefalte dokumentene er konsekvensen av manglende bruk at ordre, katalog og pakkeseddel må utveksles manuelt eller i bilaterale formater, slik at prosessen før faktura ikke blir automatisert.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Forankring | Bare faktura og ESPD er obligatoriske | Ujevn bruk av ordre, katalog og andre dokumenter | Stille krav om anbefalte EHF-dokumenter i kontrakter der det er aktuelt |
| Endringsstyring | Fakturaspesifikasjonen endres gjennom OpenPeppol, ikke nasjonalt | Norske behov må fremmes i en internasjonal prosess | Følge utgivelsesnotater for Peppol BIS Billing 3.0 |
| Endringsstyring | Flere generasjoner publiseres samtidig, og flere pre-award-dokumenter har status RC1 | Usikkerhet om hvilken versjon som skal støttes | Oppgi generasjon og versjon ved kravstilling |
| Forvaltning | Ansvaret er fordelt mellom DFØ, Digdir og OpenPeppol | Uklart hvor spørsmål og endringsønsker skal rettes | Skille mellom format, transport og mottakeroppslag i kravstilling og dokumentasjon |
| Adopsjon | Unntak for sensitivt innhold i § 6 | Parallelle papir- eller PDF-løp for enkelte fakturaer | Vurdere tekniske sikringsløsninger |

## Publiseringsform og tilgjengelighet
Spesifikasjonene publiseres som dokumentasjonssider på anskaffelser.dev, med valideringsregler og eksempelfiler. Kildene ligger i offentlige repositorier under organisasjonen `anskaffelser` på GitHub, blant annet `ehf-postaward-g3`. DFØ har en innføringsside om EHF på anskaffelser.no, og anskaffelser.dev har tjenester for validering og visning av dokumenter. Deler av EN 16931 kan lastes ned fra Standard Norge for norske virksomheter.

**Lisens:** Ikke offentlig dokumentert. Repositoriet `ehf-postaward-g3` har ingen lisensfil, og verken anskaffelser.no eller spesifikasjonssiden for EHF Billing 3.0 oppgir lisens.

## Støtter arkitekturprinsipper
- **P6: Lag digitale løsninger som støtter samhandling**
  EHF gir felles dokumentformater for handel mellom virksomheter og er harmonisert med internasjonale spesifikasjoner, slik at samme format fungerer på tvers av land.
- **P4: Del og gjenbruk data**
  Strukturerte handelsdokumenter kan behandles automatisk hos mottaker, uten ny registrering av de samme opplysningene.
- **P5: Del og gjenbruk løsninger**
  Spesifikasjoner, valideringsregler og eksempelfiler deles åpent, slik at hver systemleverandør ikke må lage egne formater.

Svakheter, spenninger og begrensninger mot prinsippene: Den sterke koblingen til Peppol BIS gjør at norske tilpasninger må gå gjennom OpenPeppols endringsprosess. Fordi bare faktura og ESPD er obligatoriske, støtter EHF samhandling i hele anskaffelsesprosessen bare i den grad virksomhetene tar i bruk de anbefalte dokumentene. Manglende lisens gjør vilkårene for gjenbruk av spesifikasjonene uklare.

## Lenke til dokumentasjon
- https://www.anskaffelser.no/kategorispesifik-veiledning/fagsystemer-digitale-anskaffelser/elektronisk-handelsformat-ehf
- https://anskaffelser.dev/postaward/g3/spec/
- https://anskaffelser.dev/postaward/g3/spec/current/billing-3.0/norway/
- https://anskaffelser.dev/preaward/g2/spec/
- https://github.com/anskaffelser/ehf-postaward-g3
- https://docs.peppol.eu/poacc/billing/3.0/
- https://lovdata.no/dokument/SF/forskrift/2019-04-01-444
- https://www.digdir.no/standarder/digitale-anskaffelser/1486
- https://www.anskaffelser.no/english/e-procurement/norwegian-agency-public-and-financial-management-dfo-peppol-authority

## Kildegrunnlag brukt i utfyllingen
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-10-24
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-10-24
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-10-24
- `arkitektur/ressurser/operative-losninger-og-tjenester/10-ELMA-produkt-canvas-v3-codex.md`, kontrollert 2026-10-24
- `arkitektur/ressurser/operative-losninger-og-tjenester/11-Peppol-eDelivery-produkt-canvas-v3-codex.md`, kontrollert 2026-10-24
- `arkitektur/ressurser/rammer-og-virkemidler/137-Forskrift-om-IT-standarder-i-offentlig-forvaltning-v3-claude.md`, kontrollert 2026-10-24
- https://www.anskaffelser.no/kategorispesifik-veiledning/fagsystemer-digitale-anskaffelser/elektronisk-handelsformat-ehf , oppdatert 13. august 2026, kontrollert 2026-10-24
- https://www.anskaffelser.no/english/e-procurement/norwegian-agency-public-and-financial-management-dfo-peppol-authority , oppdatert 15. desember 2025, kontrollert 2026-10-24
- https://anskaffelser.dev/postaward/g3/spec/current/billing-3.0/norway/ , versjon 3.0.3, kontrollert 2026-10-24
- https://anskaffelser.dev/postaward/g3/spec/ , kontrollert 2026-10-24
- https://anskaffelser.dev/preaward/g2/spec/ , kontrollert 2026-10-24
- https://github.com/anskaffelser/ehf-postaward-g3 , README og lisensstatus, kontrollert 2026-10-24
- https://docs.peppol.eu/poacc/billing/3.0/ , May 2026 Release, kontrollert 2026-10-24
- https://lovdata.no/dokument/SF/forskrift/2019-04-01-444 , sist endret ved FOR-2020-10-16-2063, kontrollert 2026-10-24
- https://lovdata.no/dokument/SF/forskrift/2013-04-05-959 , § 10, kontrollert 2026-10-24
- https://www.digdir.no/standarder/digitale-anskaffelser/1486 , kontrollert 2026-10-24
