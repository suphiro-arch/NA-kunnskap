# HL7 FHIR – norske basisprofiler (no-basis)

## Navn
Norske basisprofiler for HL7 FHIR (`hl7.fhir.no.basis`)

## Ressurs ID
HL7-001

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Standard, publisert som informasjonsmodell i form av FHIR-profiler

## Status/Livsfase
Aktiv. Gjeldende versjon er 2.2.

**Fakta:** Helsedirektoratet oppgir `hl7.fhir.no.basis 2.2` som gjeldende versjon i Referansekatalogen for e-helse, med første publisering 15. oktober 2019 og siste faglige endring 20. oktober 2023. Siste pakke på Simplifier er 2.2.2, en feilrettingsversjon datert 26. mars 2025 i endringsloggen. Profilene bygger på HL7 FHIR R4 (4.0.1).

**Fakta:** Merknaden i Referansekatalogen sier at flere basisprofiler skal utvikles, og at eksisterende profiler må vedlikeholdes. Repositoriet hos HL7 Norge på GitHub er i aktiv bruk, med siste endring i oktober 2026.

## Kort beskrivelse
Norske basisprofiler for HL7 FHIR er en felles norsk tilpasning av ressursene i den internasjonale standarden HL7 FHIR R4. Profilene fastsetter hvordan grunnleggende helseinformasjon, som pasient, helsepersonell, virksomhet og legemiddel, skal representeres med norske identifikatorer, kodeverk og utvidelser. De kan brukes direkte, men er oftest utgangspunkt for videre profilering i konkrete grensesnitt.

## Formål og normerende rolle
Formålet er at FHIR-baserte grensesnitt i helse- og omsorgstjenesten bygger på samme norske tilpasninger, slik at ulike løsninger representerer de samme grunnbegrepene på samme måte.

**Fakta:** Profilene utgis og forvaltes av HL7 Norge. Helsedirektoratet har gitt dem status som **anbefalt standard** i Referansekatalogen for e-helse, med anbefalt handling «Bruke» for virksomheter og leverandører som skal utvikle samhandlingsløsninger for datadeling i helse- og omsorgstjenesten. Helsedirektoratets anbefaling om bruk av HL7 FHIR for datadeling sier at aktører i helsesektoren bør ta i bruk FHIR-grensesnitt med nasjonale basisprofiler.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er **anbefalt**, uten rettslig forankring.

**Fakta:** Helsedirektoratet skiller mellom anbefalte og obligatoriske standarder i Referansekatalogen for e-helse. Obligatoriske standarder er hjemlet i forskrift, og en standard er alltid anbefalt før den kan bli obligatorisk. Basisprofilene har status anbefalt, og siden for standarden viser ikke til noen forskrift.

**Deduksjon:** Basisprofilene er dermed ikke gjort bindende gjennom forskrift om standarder og nasjonale e-helseløsninger. Etterlevelse skjer gjennom leverandørers og virksomheters egne valg ved utvikling av grensesnitt, og gjennom videre profiler som bygger på basisprofilene.

**Ikke offentlig dokumentert:** Om det finnes konformitetstesting eller annen kontroll av at løsninger faktisk følger profilene.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`. Profilene er ikke rettslig forankret, og `Juridisk samhandling` er derfor ikke aktuell. `Veiledning: Utvikling og formidling av veiledning` er ikke satt, fordi ressursen er en informasjonsmodell og ikke veiledning om hvordan løsninger bygges. `Datautveksling og integrasjon: Dele data med andre` er vurdert og ikke satt: profilene gjør deling enklere, men det er løsningene som implementerer dem som deler data.

- **Informasjonsforvaltning: Informasjonsarkitektur** profilene strukturerer og modellerer grunnleggende helseinformasjon på en standardisert måte, med norske identifikatorer som fødselsnummer, D-nummer, HPR-nummer og organisasjonsnummer, og med norske kodeverk og utvidelser.
- **Standardisering: Forvaltningsstandarder** profilene er en nasjonal tilpasning av en internasjonal standard, forvaltet i åpen prosess av HL7 Norge og med status anbefalt standard i Referansekatalogen for e-helse.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Systemleverandører i helse- og omsorgssektoren | Felles grunnlag for FHIR-grensesnitt | Utvikling av samhandlingsløsninger for datadeling | Referansekatalogen retter anbefalingen mot leverandører og virksomheter |
| Helsevirksomheter og forvaltere av nasjonale e-helseløsninger | Forutsigbar representasjon av grunnbegreper | Kravstilling og egne FHIR-profiler | Basisprofilene er oftest utgangspunkt for videre profilering |
| Utviklere av egne profiler og implementasjonsguider | Felles norske identifikatorer, kodeverk og utvidelser | Profilering for konkrete brukstilfeller | Bygger videre på pakken `hl7.fhir.no.basis` |
| Bidragsytere i HL7 Norge | Kanal for endringsforslag | Workshops, saker og endringsforslag på GitHub | Høringer gjennomføres av HL7 Norge |

## Normerende innhold
**Fakta:** Pakken `hl7.fhir.no.basis` 2.2.2 inneholder profiler for blant annet Patient, Person, RelatedPerson, Practitioner, PractitionerRole, Organization, Location, HealthcareService, Endpoint, Medication, MedicationStatement, Substance, AllergyIntolerance, Procedure, Composition, DocumentReference, Appointment og AppointmentResponse, i tillegg til datatypeprofiler for adresse og navn.

**Fakta:** Profilene fastsetter norske identifikatorer som egne «slices». Pasientprofilen har fødselsnummer, D-nummer, hjelpenummer og felles hjelpenummer, helsepersonellprofilen har HPR-nummer, og virksomhetsprofilen har organisasjonsnummer fra Enhetsregisteret og identifikator fra Register for enheter i spesialisthelsetjenesten (RESH). Pakken har også norske utvidelser, blant annet for kommunenummer, bydel, mellomnavn, statsborgerskap og offisiell adresse, og tilhørende kodeverk og verdisett.

**Fakta:** Versjon 2.2 la til profilene Appointment og AppointmentResponse og rettet feil, blant annet for hjelpenummer. Versjon 2.1 la til Procedure. Profiler under arbeid har status `draft` og distribueres ikke i den aktive pakken.

## Bruksområde
Basisprofilene bør legges til grunn når en løsning i helse- og omsorgssektoren skal tilby eller ta i bruk FHIR-grensesnitt for deling av strukturerte helsedata, og når det lages egne profiler eller implementasjonsguider for konkrete brukstilfeller.

De hjelper med å avklare hvordan norske identifikatorer, adresser, navn og kodeverk skal uttrykkes i FHIR, slik at dette ikke løses ulikt i hvert prosjekt.

## Typiske analyse- og beslutningssituasjoner
- når et prosjekt skal velge grunnlag for et nytt FHIR-grensesnitt i helsesektoren
- når krav til FHIR-støtte skal formuleres i anskaffelser av helse-IKT
- når en sektorspesifikk profil eller implementasjonsguide skal bygges, og det må avgjøres hva som arves fra basisprofilene
- når to løsninger med FHIR-grensesnitt skal kobles, og det må vurderes om de bygger på samme versjon av basisprofilene

## Når ressursen normalt ikke er tilstrekkelig alene
Basisprofilene er ikke tilstrekkelige alene for å realisere et konkret grensesnitt. De må suppleres med brukstilfellespesifikke profiler, API- og sikkerhetsmekanismer, rettslig grunnlag for delingen og avtaler mellom partene. Helsedirektoratet viser selv til anbefalingene om bruk av HL7 FHIR for datadeling og om SMART on FHIR som tilleggsdokumentasjon.

## Scope og avgrensning
Inngår:
- norske tilpasninger av utvalgte FHIR R4-ressurser
- norske identifikatorer, utvidelser, kodeverk og verdisett som profilene bruker
- eksempler og endringslogg

Inngår ikke:
- brukstilfellespesifikke profiler for enkelte tjenester
- transport, autentisering og tilgangsstyring for FHIR-grensesnitt
- meldingsbasert samhandling
- obligatoriske krav etter forskrift

Avgrensning mot `DIGDIR-026` Referansekatalogen for IT-standarder: Basisprofilene er oppført i Referansekatalogen for e-helse, som Helsedirektoratet forvalter for helse- og omsorgssektoren. Det er en annen katalog enn Digdirs Referansekatalogen for IT-standarder for offentlig sektor.

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | HL7 Norge, som utgir profilene. HL7 Norge er tilknyttet HL7 International |
| Forvaltningsansvar | HL7 Norge. **Fakta:** Profilene utarbeides under HL7 Norges tekniske styringskomité, og kontaktpersonene for repositoriet kommer fra Helsedirektoratet og er medlemmer av komiteen |
| Endringsprosess | **Fakta:** Utvikling skjer åpent på GitHub. Forslag og feilmeldinger tas imot som saker eller endringsforslag i repositoriet, eller på e-post til HL7 Norge. HL7 Norge arrangerer workshops og gjennomfører høringsrunder for profilene |
| Publiserings- og beslutningsarena | Profilene publiseres på Simplifier.net under HL7 Norway. Helsedirektoratet fastsetter normeringsstatusen i Referansekatalogen for e-helse. **Fakta:** Forslaget om å sette versjon 2.2 som anbefalt standard, til erstatning for versjon 2.0, ble sendt på høring av Direktoratet for e-helse høsten 2023, med frist 15. desember 2023. Høringssiden på ehelse.no er ikke lenger tilgjengelig og videresendes til Helsedirektoratets nettsted |

## Relasjon til andre ressurser
- **HPR (`HDIR-002`)**: helsepersonellprofilen bruker HPR-nummer som identifikator.
- **Folkeregisteret (`SKATT-001`)**: pasientprofilen bruker fødselsnummer og D-nummer.
- **Enhetsregisteret (`BRREG-003`)**: virksomhetsprofilen bruker organisasjonsnummer.
- **Referansekatalogen for IT-standarder (`DIGDIR-026`)**: en annen katalog enn Referansekatalogen for e-helse, se `Scope og avgrensning`.
- **Felles informasjonsmodeller (`DIGDIR-069`)**: tverrsektorielle prinsipper for informasjonsmodeller. Basisprofilene er en sektorspesifikk modell for helse.
- **HL7 FHIR R4**: den internasjonale standarden profilene tilpasser. Den er ikke egen ressurs i registeret.
- **Anbefaling om bruk av HL7 FHIR for datadeling og anbefaling om bruk av SMART on FHIR**: Helsedirektoratets veiledere som viser til basisprofilene. De er ikke egne ressurser i registeret.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er at leverandører og virksomheter ikke må gjøre de samme norske tilpasningene hver for seg, og at integrasjoner mellom løsninger som bygger på profilene krever mindre særtilpasning.

Arkitekturverdien er et felles semantisk grunnlag for grunnbegrepene i helsesektoren, med norske identifikatorer knyttet til de nasjonale registrene. Profilene gir et felles startpunkt som brukstilfellespesifikke profiler kan arve fra.

## Konsekvens ved manglende bruk eller avvik
Lager hver løsning egne norske tilpasninger av FHIR, kan samme pasient, helsepersonell eller virksomhet bli representert ulikt, med ulike identifikatorer eller utvidelser. Det gir høyere integrasjonskostnad og risiko for feil når data deles.

**Deduksjon:** Løsninger som bygger på ulike versjoner av basisprofilene kan få avvik seg imellom, også når begge følger profilene.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Forankring | Profilene er anbefalt, ikke obligatoriske | Ujevn bruk i sektoren | Stille krav om basisprofilene i anskaffelser og egne profiler |
| Adopsjon | Konformitetskontroll er ikke offentlig dokumentert | Løsninger kan oppgi FHIR-støtte uten å følge profilene | Validere mot pakken `hl7.fhir.no.basis` |
| Endringsstyring | Flere versjoner i bruk samtidig | Avvik mellom løsninger på ulike versjoner | Oppgi versjon ved kravstilling og følge endringsloggen |
| Forvaltning | Utviklingen avhenger av en frivillig organisasjon og bidrag fra sektoren | Nye profiler kan komme sent | Bidra gjennom HL7 Norges åpne prosess |

## Publiseringsform og tilgjengelighet
Profilene publiseres som FHIR-pakken `hl7.fhir.no.basis` og som implementasjonsguide på Simplifier.net. Kildene forvaltes åpent i repositoriet `HL7Norway/basisprofiler-r4` på GitHub. Helsedirektoratet har en egen side for standarden i Referansekatalogen for e-helse, med lenke til tidligere versjoner.

**Lisens:** Ikke offentlig dokumentert. Repositoriet har ingen lisensfil, og verken Simplifier eller Helsedirektoratet oppgir lisens.

## Støtter arkitekturprinsipper
- **P6: Lag digitale løsninger som støtter samhandling**
  Profilene gir felles semantikk for grunnbegrepene i helsesektoren og bygger på en åpen internasjonal standard.
- **P4: Del og gjenbruk data**
  Felles norske identifikatorer knytter FHIR-data til de nasjonale registrene, slik at data fra ulike kilder kan kobles.
- **P5: Del og gjenbruk løsninger**
  Profilene er laget for å arves av brukstilfellespesifikke profiler, i stedet for at hvert prosjekt lager sine egne.

Svakheter, spenninger og begrensninger mot prinsippene: Profilene er sektorspesifikke for helse og bygger ikke på tverrsektorielle informasjonsmodeller. Fordi bruken er anbefalt og ikke kontrolleres, støtter de samhandling bare i den grad løsningene faktisk følger dem.

## Lenke til dokumentasjon
- https://www.helsedirektoratet.no/standarder/norske-basisprofiler-for-hl7-fhir
- https://simplifier.net/hl7norwayno-basis
- https://simplifier.net/guide/no-basis-entities-individuals?version=current
- https://github.com/HL7Norway/basisprofiler-r4
- https://www.helsedirektoratet.no/veiledere/anbefaling-om-bruk-av-hl7-fhir-for-datadeling

## Kildegrunnlag brukt i utfyllingen
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-10-23
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-10-23
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-10-23
- https://www.helsedirektoratet.no/standarder/norske-basisprofiler-for-hl7-fhir , siste faglige endring 20. oktober 2023, kontrollert 2026-10-23
- https://www.helsedirektoratet.no/om-oss/om-helsedirektoratets-normerende-produkter , kontrollert 2026-10-23
- https://www.helsedirektoratet.no/veiledere/anbefaling-om-bruk-av-hl7-fhir-for-datadeling/anbefaling , siste faglige endring 15. juni 2023, kontrollert 2026-10-23
- https://simplifier.net/hl7norwayno-basis , kontrollert 2026-10-23
- https://packages.simplifier.net/hl7.fhir.no.basis , pakkeoversikt og endringslogg til versjon 2.2.2, kontrollert 2026-10-23
- https://github.com/HL7Norway/basisprofiler-r4 , README og innhold, kontrollert 2026-10-23
- https://hl7.no/ , kontrollert 2026-10-23

## Endringer fra forrige versjon
Dette er første publiserte versjon av ressursbeskrivelsen.
