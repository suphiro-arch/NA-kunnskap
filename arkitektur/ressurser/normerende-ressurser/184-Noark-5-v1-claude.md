# Noark 5

## Navn
Noark 5 – Norsk arkivstandard

## Ressurs ID
ARKIV-001

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Standard, med funksjonelle krav, konseptuell og logisk datamodell, metadatakatalog og XML-skjemaer for arkivuttrekk

## Status/Livsfase
Aktiv. Gjeldende versjon er Noark 5 versjon 6.0, datert 24. september 2025.

**Fakta:** Versjon 6.0 er utgitt av Arkivverket, som fra 2026 heter Nasjonalarkivet. Forordet sier at versjonen viderefører forenklingen fra versjon 5.0, i tråd med anbefalingene fra arkivlovutvalget i NOU 2019:9 *Fra kalveskinn til datasjø*. Krav som ikke lenger var hensiktsmessige er fjernet, og andre er slått sammen til mer overordnede krav, slik at standarden er mindre detaljert enn før.

**Fakta:** Noark ble opprinnelig utviklet av Statens rasjonaliseringsdirektorat i samarbeid med Riksarkivaren. Noark 5 kom i 2008 og skilte kravene til arkiv fra kravene til saksbehandling, slik at standarden kan brukes til å stille krav til ulike typer dokumentasjonssystemer, ikke bare sak- og arkivsystemer.

## Kort beskrivelse
Noark 5 er den norske standarden for dokumentasjonsforvaltning og arkiv i informasjonssystemer. Den stiller krav til arkivstruktur, metadata og funksjonalitet, slik at dokumentasjon kan opprettes, forvaltes, kasseres og overføres til arkivdepot på en måte som ivaretar autentisitet, pålitelighet, integritet og anvendbarhet. Standarden stiller ikke krav til teknisk implementering. Kravene kan realiseres i et fagsystem, i en arkivmodul i fagsystemet eller i et eksternt arkivsystem som fagsystemene integreres med.

Standarden er også grunnlaget for arkivuttrekk: et uttrekk etter Noark 5 er en avleveringspakke i tråd med OAIS-modellen, og XML-skjemaene i standarden brukes til å validere den.

## Formål og normerende rolle
Noark 5 skal gi felles rammer for utvikling og anskaffelse av dokumentasjons- og arkivsystemer. Standarden påvirker hvordan virksomheter og leverandører strukturerer arkivet, hvilke metadata som registreres, hvordan endringer logges, og hvordan dokumentasjon trekkes ut for bevaring.

**Fakta:** Versjon 6.0 oppgir fem formål: sikre dokumentenes autentisitet og pålitelighet, støtte effektiv forvaltning, bevare dokumenter over tid, fremme standardisering og samhandlingsevne, og legge grunnlaget for at informasjonssystemene kan overholde krav i lov og forskrift. Standarden bygger på ISO-standarder for informasjon og dokumentasjon, blant annet ISO 15489-1 og ISO 30300.

Normerende rolle: Som helhet **anbefalt**. Kravene om uttrekk er **obligatoriske** for statlige organer som avleverer fra systemer bygget etter Noark 5. Se `Forpliktelsesnivå og etterlevelse`.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er delt. Den rettslige forankringen dekker bare uttrekk fra systemer som allerede er bygget etter Noark 5, ikke valget av system.

**Fakta:** Lov om dokumentasjon og arkiv (arkivlova, LOV-2025-06-20-96) og forskrift om dokumentasjon og arkiv (arkivforskrifta, FOR-2025-12-17-2647) gjelder fra 1. januar 2026, under Kultur- og likestillingsdepartementet. Loven nevner ikke Noark. Forskriften nevner Noark bare i § 28: Når et statlig organ skal avlevere dokumentasjon fra et informasjonssystem som er utformet i tråd med Noark 5, skal organet følge retningslinjene i Noark 5 for å produsere uttrekk. Ved særlige grunner kan organet avtale en annen framgangsmåte med Nasjonalarkivet.

**Fakta:** Forskriften § 5 stiller funksjonelle krav til informasjonssystemer som inneholder dokumentasjon som skal forvaltes som arkiv: blant annet nødvendige metadata om opphav og kontekst, vern mot ikke-autoriserte endringer, sporing av endringer, kontrollert eksport og kassasjon, gjenfinning og uttrekk av journalmetadata. Paragrafen krever ikke at kravene oppfylles med Noark. § 52 opphever riksarkivarens forskrift (FOR-2017-12-19-2286), og den tidligere arkivforskriften (FOR-2017-12-15-2105) er opphevet fra samme dato. Riksarkivarens forskrift § 3-1 krevde at Noark-systemer skulle godkjennes av Riksarkivaren før de ble tatt i bruk.

**Fakta:** I høringssvaret til forslaget om ny arkivforskrift skriver Arkivverket at forskriften ikke stiller krav om Noark-baserte systemer for å oppfylle arkivplikten, og at Noark 5.6 er lansert som en frivillig standard virksomhetene kan velge å bruke. **Deduksjon:** «Noark 5.6» viser til Noark 5 versjon 6.0.

**Deduksjon:** Fra 1. januar 2026 er Noark 5 ikke lenger generelt pålagt for journal- og arkivsystemer i offentlig forvaltning. Virksomhetene kan oppfylle kravene i forskriften § 5 med Noark 5 eller på andre måter. Bruker et statlig organ et system bygget etter Noark 5, er uttrekkskravene likevel bindende ved avlevering, med mindre annet er avtalt med Nasjonalarkivet.

**Fakta:** Digdirs Referansekatalog for IT-standarder fører fortsatt Noark 5 som obligatorisk for offentlige virksomheter som bruker journal- og arkivsystem. Siden viser til versjonen fra 2009 og til arkivforskriften og riksarkivarens forskrift fra 2017, som begge er opphevet. Siden ble sist endret 6. september 2023.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Om Nasjonalarkivet fortsatt har en godkjenningsordning eller annen frivillig kontroll av Noark-systemer etter at kravet om godkjenning falt bort. Nasjonalarkivets egen side om Noark kunne ikke leses maskinelt.

Etterlevelse skjer i praksis gjennom kravstilling i anskaffelser, gjennom leverandørenes produkter og gjennom Nasjonalarkivets kontroll og godkjenning av arkivpakker ved avlevering, jf. arkivforskrifta § 27.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`. `Juridisk samhandling: Regelverkstolkning` er ikke satt. Arkivforskrifta viser til Noark 5 for uttrekk, men standarden sier ikke hvordan arkivregelverket skal forstås. Den beskriver løsninger som kan oppfylle kravene. `Tillit: Sporbarhet og innsyn` er ikke satt: standarden krever endringslogg i arkivet, men kapabiliteten gjelder logg over bruk av tillitstjenester. `Veiledning: Utvikling og formidling av veiledning` er ikke satt, fordi ressursen er en kravstandard og ikke veiledning.

- **Informasjonsforvaltning: Informasjonsarkitektur** standarden fastsetter en konseptuell informasjonsmodell for dokumentasjon, en logisk datamodell med 29 objekter og en metadatakatalog med 183 metadataelementer, som arkivsystemer og arkivuttrekk struktureres etter.
- **Standardisering: Forvaltningsstandarder** Noark 5 er den nasjonale standarden for dokumentasjons- og arkivsystemer i forvaltningen, forvaltet av Nasjonalarkivet, og arkivforskrifta § 28 gjør uttrekksreglene bindende for statlige organer som avleverer fra Noark 5-systemer.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Arkivfaglig ansvarlige i offentlige virksomheter | Rammer for forsvarlig dokumentasjonsforvaltning | Krav til egne systemer og rutiner | Standardens primære målgruppe |
| Systemleverandører og systemutviklere | Kravsett for arkivfunksjonalitet | Utvikling av sak- og arkivsystemer og arkivmoduler i fagsystemer | Gjelder både hyllevare og egenutviklede løsninger |
| Løsnings- og virksomhetsarkitekter | Plassering av arkivfunksjonen i systemarkitekturen | Valg mellom innebygd arkiv, arkivmodul og integrasjon med eksternt arkivsystem | Standarden har ingen foretrukket arkitektur |
| Ansvarlige for anskaffelser | Krav til systemer som skal ivareta arkivkrav | Kravspesifikasjon | Standarden nevner anskaffere uttrykkelig som målgruppe |
| Statlige organer som avleverer | Gyldige arkivuttrekk | Produksjon av avleveringspakker | Bindende etter arkivforskrifta § 28 |
| Arkivinstitusjoner | Systemuavhengige uttrekk for langtidsbevaring | Mottak og kontroll av avleveringspakker | Nasjonalarkivet for statlig sektor |

## Normerende innhold
**Fakta:** Standarden består av fire dokumenter og et sett XML-skjemaer:

- **Noark 5-standarden:** konseptuell informasjonsmodell for dokumentasjon og funksjonelle krav, ordnet i kapitler om datamodell, dokumentfangst, sikkerhet og tilgang, integrasjonsløsninger, søk, gjenfinning og bruk, dokumentasjon av oppgavestøtte, og bevaring, kassasjon og uttrekk. Tillegg med ordforklaringer og detaljert beskrivelse av objektene i modellen.
- **Vedlegg 1: Metadatakatalog:** definerer 183 metadataelementer med entydig identifikasjon, navn og betingelser for bruk.
- **Vedlegg 2: Metadata gruppert på objekter:** logisk datamodell med 29 objekter og relasjonene mellom dem, med obligatoriske og valgfrie metadata.
- **Vedlegg 3: Logging av endringer:** hvilke metadata som skal logges ved endring. Endringsloggen skal følge med arkivuttrekk.
- **XML-skjemaer** for validering av uttrekk: `arkivstruktur.xsd`, `endringslogg.xsd`, `loependeJournal.xsd`, `offentligJournal.xsd` og `metadatakatalog.xsd`.

**Fakta:** Kravene er merket O, B eller V. B-krav er obligatoriske under et vilkår som står i merknaden, for eksempel «obligatorisk for løsninger med journalføring». Sentrale krav er at systemets fysiske datamodell skal kunne avbildes mot den logiske datamodellen, at arkivdokumenter skal inngå i en arkivstruktur med minst arkiv, arkivdel, registrering, dokumentbeskrivelse og dokumentobjekt, og at journalføringspliktige saksdokumenter skal registreres som journalpost i en saksmappe.

**Fakta:** Et arkivuttrekk etter Noark 5 skal være en avleveringspakke (Submission Information Package) etter OAIS-modellen i ISO 14721, med arkivdokumenter, journalrapporter, metadata og endringslogg for en avgrenset periode. Vedleggene kan også brukes sammen med andre standarder, som ISO 16175-1.

## Bruksområde
Noark 5 brukes når en virksomhet skal anskaffe, utvikle eller vurdere et system som skal forvalte dokumentasjon som arkiv, og når dokumentasjon skal trekkes ut for avlevering eller overføres ved systembytte.

Standarden hjelper med å avklare hvilken arkivstruktur og hvilke metadata dokumentasjonen skal ha, hvordan endringer skal logges, og hvordan arkivfunksjonen kan plasseres: innebygd i fagsystemet, som egen modul eller i et eksternt arkivsystem via API eller tjenestegrensesnitt.

## Typiske analyse- og beslutningssituasjoner
- når en virksomhet skal anskaffe sak- og arkivsystem eller fagsystem med arkivfunksjoner, og må avgjøre om Noark 5 skal stilles som krav
- når kravene i arkivforskrifta § 5 skal oppfylles i et fagsystem som ikke er bygget etter Noark 5
- når et fagsystem skal integreres med et eksternt arkivsystem, og det må avgjøres hvordan arkivkravene fordeles mellom systemene
- når et statlig organ skal planlegge avlevering og uttrekk fra et system bygget etter Noark 5
- når krav i eldre anskaffelser eller i Referansekatalogen for IT-standarder skal vurderes mot gjeldende regelverk

## Når ressursen normalt ikke er tilstrekkelig alene
Noark 5 er ikke tilstrekkelig alene. Plikten til å dokumentere og arkivere følger av arkivlova og arkivforskrifta, ikke av standarden. Standarden må suppleres med virksomhetens egne rutiner og systembeskrivelser etter forskriften § 6, med regler for format og avlevering i forskriften, med avtaler med arkivinstitusjonen, og med tekniske grensesnitt for integrasjon mellom fag- og arkivsystemer, som `Fiks arkiv` i kommunal sektor.

## Scope og avgrensning
Inngår:
- krav til arkivstruktur, metadata og funksjonalitet i informasjonssystemer som forvalter dokumentasjon
- konseptuell og logisk datamodell og metadatakatalog
- krav til logging av endringer
- krav til bevaring, kassasjon og uttrekk, med XML-skjemaer for validering av uttrekk

Inngår ikke:
- teknisk implementering eller valg av systemarkitektur
- arkivplikten selv og reglene for avlevering, som følger av arkivlova og arkivforskrifta
- et felles tjenestegrensesnitt for integrasjon. Versjon 6.0 omtaler API og tjenestegrensesnitt generelt, men fastsetter ikke et bestemt grensesnitt
- formater og pakker for andre arkivstandarder, som Nasjonalarkivet forvalter separat

**Ikke offentlig dokumentert i denne arbeidsøkten:** Status for den separate spesifikasjonen Noark 5 Tjenestegrensesnitt, og om den er oppdatert til versjon 6.0.

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Nasjonalarkivet, tidligere Arkivverket. **Fakta:** Arkivlova bruker navnet Nasjonalarkivet og gjelder fra 1. januar 2026. Versjon 6.0 er datert september 2025 og utgitt under navnet Arkivverket |
| Forvaltningsansvar | Nasjonalarkivet |
| Endringsprosess | **Fakta:** Forordet til versjon 6.0 oppgir at endringene bygger på tilbakemeldinger og erfaringer fra arkivskapere, leverandører, arkivinstitusjoner og Arkivverket selv. **Ikke offentlig dokumentert i denne arbeidsøkten:** Hvordan endringsforslag meldes inn, og om det gjennomføres høring av nye versjoner |
| Publiserings- og beslutningsarena | Standarden publiseres på nasjonalarkivet.no. Kultur- og likestillingsdepartementet fastsetter arkivforskrifta, som avgjør hvor bindende standarden er |

**Ikke offentlig dokumentert i denne arbeidsøkten:** Eksakt dato for navnebyttet fra Arkivverket til Nasjonalarkivet. Navnet følger av arkivlova, og navnebyttet skjedde trolig ved ikrafttredelsen 1. januar 2026, men det er ikke bekreftet i en primærkilde fra etaten.

## Relasjon til andre ressurser
- **Referansekatalogen for IT-standarder (`DIGDIR-026`)**: fører Noark 5 under arkivstandarder som obligatorisk, med henvisning til forskrifter som er opphevet. Se `Forpliktelsesnivå og etterlevelse`.
- **Fiks protokoll (`KS-013`)**: `Fiks arkiv` er et standardisert grensesnitt for kommunikasjon mellom fagsystemer og Noark-baserte sak- og arkivsystemer i kommunal sektor.
- **FINT Arkiv (`NOVARI-002`)**: arkiv- og integrasjonstjeneste med komponenter mot Noark-arkiv.
- **eInnsyn (`DIGDIR-006`)**: publiserer journalposter som produseres i virksomhetenes sak- og arkivsystemer. Offentlig journal er et av uttrekksformatene i Noark 5.
- **eFormidling (`DIGDIR-007`)**: meldingsutveksling som kobles til virksomhetenes sak- og arkivløsninger. Langtidsarkivering inngår ikke i eFormidling.
- **Arkivlova og arkivforskrifta**: rettslig grunnlag for arkivplikten og for kravet om uttrekk etter Noark 5 i arkivforskrifta § 28. Ingen av dem er egne ressurser i registeret.
- **ISO 15489-1, ISO 30300, ISO 16175-1 og ISO 14721 (OAIS)**: internasjonale standarder Noark 5 bygger på eller er avstemt mot. De er ikke egne ressurser i registeret.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er at leverandører kan bygge mot ett kravsett i stedet for ulike krav fra hver virksomhet, og at virksomheter kan stille kjente krav i anskaffelser. Felles uttrekksformat gjør avlevering og systembytte forutsigbart.

Arkitekturverdien er en felles datamodell og metadatakatalog for dokumentasjon i offentlig forvaltning. Det gir sammenlignbar struktur på tvers av systemer og et felles grunnlag for integrasjoner som `Fiks arkiv` og for publisering av offentlig journal. Standarden skiller arkivkravene fra den tekniske løsningen, slik at arkivfunksjonen kan legges der dokumentasjonen skapes.

## Konsekvens ved manglende bruk eller avvik
Bruker et statlig organ et system bygget etter Noark 5 og produserer uttrekk som ikke følger standarden, kan Nasjonalarkivet avvise avleveringspakken, jf. arkivforskrifta § 27, og organet må lage en ny.

**Deduksjon:** Velger en virksomhet en annen løsning enn Noark 5, må den selv dokumentere at kravene i arkivforskrifta § 5 er oppfylt, og avtale uttrekksform med arkivinstitusjonen. Når Noark ikke lenger er felles krav, kan arkivstruktur og metadata bli mer ulike mellom virksomheter, og integrasjoner og uttrekk kan kreve mer særtilpasning.

**Deduksjon:** Krav i anskaffelser som bygger på Referansekatalogens omtale av Noark 5 som obligatorisk, kan stille strengere krav enn regelverket gjør.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Forankring | Referansekatalogen omtaler Noark 5 som obligatorisk med henvisning til opphevede forskrifter | Uklart for virksomheter og leverandører hva som faktisk kreves | Oppdatere omtalen i Referansekatalogen mot arkivforskrifta fra 2026 |
| Adopsjon | Standarden er frivillig for valg av system | Ujevn bruk og ulik arkivstruktur på tvers av virksomheter | Stille Noark 5 eller tilsvarende krav eksplisitt i anskaffelser |
| Endringsstyring | Systemer i drift er bygget etter eldre versjoner av Noark 5 | Avvik mellom versjoner ved uttrekk og integrasjon | Oppgi versjon i kravstilling og avtaler om uttrekk |
| Kontroll | Godkjenningskravet for Noark-systemer er opphevet, og en eventuell ny ordning er ikke dokumentert | Leverandører kan oppgi Noark-støtte uten ekstern kontroll | Kontrollere uttrekk mot XML-skjemaene og kravene i standarden |
| Sammenheng med gjenbrukbare løsninger | Integrasjon mellom fag- og arkivsystem er ikke standardisert i Noark 5 selv | Sektorvise grensesnitt, som `Fiks arkiv` og FINT Arkiv | Bruke etablerte grensesnitt der de finnes |

## Publiseringsform og tilgjengelighet
Standarden publiseres som PDF på nasjonalarkivet.no, med vedleggene og XML-skjemaene som egne filer. Nasjonalarkivets side om Noark ga 403 ved maskinell henting i denne arbeidsøkten, så oversikten over filene der er ikke kontrollert. PDF-en for versjon 6.0 er lest direkte.

**Lisens:** Ikke offentlig dokumentert. Versjon 6.0 oppgir ingen lisens for standarden, vedleggene eller XML-skjemaene.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Felles metadatakatalog og logisk datamodell gjør dokumentasjon fra ulike systemer sammenlignbar, og standarden krever funksjoner for å trekke ut dokumenter og metadata til bruk i andre løsninger.
- **P6: Lag digitale løsninger som støtter samhandling**
  Standarden fremmer standardisering av metadata og utvekslingsformat, slik at systemer kan samhandle og arkivfunksjoner kan integreres med fagsystemer.
- **P7: Sørg for tillit til oppgaveløsningen**
  Kravene til autentisitet, integritet, endringslogg og systemuavhengige uttrekk skal gjøre det mulig å etterprøve dokumentasjonen over tid.

Svakheter, spenninger og begrensninger mot prinsippene: Etter at kravet om Noark falt bort, støtter standarden samhandling bare i den grad virksomhetene velger å bruke den. Avviket mellom regelverket og Referansekatalogen svekker forutsigbarheten for leverandører og virksomheter. Standarden fastsetter ikke et felles integrasjonsgrensesnitt, så samhandling mellom fag- og arkivsystemer avhenger av sektorvise løsninger.

## Lenke til dokumentasjon
- https://www.nasjonalarkivet.no/offentlig-forvaltning/regelverk-og-standarder/noark/
- https://www.nasjonalarkivet.no/content/uploads/2025/10/Noark-5-versjon-6.pdf
- https://lovdata.no/dokument/SF/forskrift/2025-12-17-2647
- https://lovdata.no/dokument/NL/lov/2025-06-20-96
- https://www.digdir.no/standarder/arkivstandarder/1482

## Kildegrunnlag brukt i utfyllingen
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-10-24
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-10-24
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-10-24
- `arkitektur/ressurser/operative-losninger-og-tjenester/94-Fiks-protokoll-v1-claude.md`, kontrollert 2026-10-24
- https://www.nasjonalarkivet.no/content/uploads/2025/10/Noark-5-versjon-6.pdf , Noark 5 versjon 6.0, datert 24.09.2025, kontrollert 2026-10-24
- https://lovdata.no/dokument/SF/forskrift/2025-12-17-2647 , arkivforskrifta §§ 5, 6, 27, 28 og 52, kontrollert 2026-10-24
- https://lovdata.no/forskrift/2017-12-15-2105 , tidligere arkivforskrift, status opphevet fra 1. januar 2026, kontrollert 2026-10-24
- https://lovdata.no/lov/2025-06-20-96 , arkivlova, kontrollert 2026-10-24
- https://www.digdir.no/standarder/arkivstandarder/1482 , sist endret 6. september 2023, kontrollert 2026-10-24
- https://www.nasjonalarkivet.no/content/uploads/2026/01/Horingssvar-Forslag-til-ny-forskrift-om-arkiv-arkivforskriften.pdf , Arkivverkets høringssvar til forslag til ny arkivforskrift, kontrollert 2026-10-24
- https://www.nasjonalarkivet.no/offentlig-forvaltning/regelverk-og-standarder/noark/ , kunne ikke leses maskinelt (HTTP 403) 2026-10-24
