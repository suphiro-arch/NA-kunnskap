# SOSI

## Navn
SOSI – standarder for geografisk informasjon (Samordnet opplegg for stedfestet informasjon)

## Ressurs ID
KART-006

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Standardserie: nasjonale bransjestandarder for geografisk informasjon, med modelleringsregler, formatrealiseringer, objektkatalog og produktspesifikasjoner

## Status/Livsfase
Aktiv. Serien forvaltes løpende, og enkeltstandarder revideres eller trekkes tilbake hver for seg.

**Fakta:** I Kartverkets register for SOSI Del 1 – Generell del er blant annet «Regler for UML-modellering» 5.1, «Realisering i SOSI-format» 5.0, «Realisering i GML-format» 5.0, «Generelle typer» 4.5, «Nettverk og lineære referanser» 5.0, «Metadataprofil» 1.2 og «SOSI Produktspesifikasjoner – Krav og godkjenning» 5.0 oppført som gyldige. Flere eldre deler, som «Introduksjon» 4.0 og «Generelle konsepter» 4.0, er tilbaketrukket.

**Fakta:** I SOSI Del 2 – Generell objektkatalog er de fleste fagområdene fra versjon 4.x tilbaketrukket. Blant de gyldige er Plan 5.0, Landskapsarkitektur 5.0, Løsmassegeologi 5.0, Ledningsnett 4.6, Gravplass 4.6, Stedsnavn 4.5, Samfunnssikkerhet 4.1 og Geologi generell del 4.0. Registeret for «Standarder geografisk informasjon» har ni gyldige og ti tilbaketrukne standarder.

**Fakta:** Kartverket har flyttet innholdet om standardisering fra kartverket.no til Geonorge.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Om SOSI-formatet skal fases ut til fordel for GML. Begge realiseringene er gyldige i registeret, og det er ikke funnet noen kunngjøring fra Kartverket om utfasing. Registreringen av medietypen `text/vnd.sosi` hos IANA fra 2019 oppgir at det finnes intensjoner om å erstatte bruken av formatet med GML, men den er ikke et vedtak fra forvalteren.

## Kort beskrivelse
SOSI er den norske serien av bransjestandarder for geografisk informasjon. Serien fastsetter hvordan geodata skal modelleres, beskrives og utveksles: regler for UML-modellering, felles typer og metadataprofil, realisering i SOSI-format og i GML, en generell objektkatalog med objekttyper for ulike fagområder, og krav til produktspesifikasjoner for kart- og geodata. I tillegg omfatter serien fagstandarder for blant annet geodetisk grunnlag, posisjonsbestemmelse, stedfesting og kartutforming. Kartverket eier og forvalter standardene.

## Formål og normerende rolle
Formålet er at geodata fra ulike produsenter blir modellert og levert etter samme regler, slik at de kan brukes sammen og utveksles uten særtilpasning.

**Fakta:** Kartverket skal koordinere utviklingen av standarder for geografisk informasjon, og utvikler nasjonale standarder der det ikke finnes dekkende nasjonale, europeiske eller internasjonale standarder. Standarder utviklet etter Kartverkets styrende dokument for nasjonale bransjestandarder kalles SOSI-standarder.

**Fakta:** Produktspesifikasjonene i SOSI Del 3 bygger på objektkatalogen i Del 2, legger til regler for hvordan katalogen brukes i produktet og snevrer den ofte inn. Kartverket oppgir at produktspesifikasjonene følger NS-EN ISO 19131 (produktspesifikasjoner), NS-EN ISO 19136 (GML) og NS-EN ISO 19109 (regler for applikasjonsskjema).

Rollen er styrende for den delen av geodataproduksjonen som er bundet til nasjonale produktspesifikasjoner, og anbefalt ellers. Se `Forpliktelsesnivå og etterlevelse`.

## Forpliktelsesnivå og etterlevelse
SOSI er en frivillig bransjestandard som ikke er nevnt med navn i lov eller forskrift. Deler av bruken er likevel bundet gjennom forskriftskrav til produktspesifikasjoner.

**Fakta:** Forskrift om kart, stedfestet informasjon, arealformål og kommunalt planregister (kart- og planforskriften), FOR-2025-01-20-52, gjelder fra 1. juli 2025 og opphevet forskriften fra 2009. Etter § 6 skal det offentlige kartgrunnlaget følge spesifikasjoner godkjent av Statens kartverk. Etter §§ 8–12 skal planforslag leveres digitalt etter «Nasjonal produktspesifikasjon for arealplan og digitalt planregister», plandata kodes og plankart framstilles etter den, og planregisteret oppfylle kravene i den. Forskriften nevner ikke SOSI.

**Fakta:** Geodataloven § 8 krever at deltakende virksomheter gjør data og tjenester tilgjengelige i harmonisert form og holder metadata oppdatert. Loven nevner ikke SOSI eller andre bestemte standarder.

**Deduksjon:** Produktspesifikasjonene forskriften viser til, er publisert i Geonorges register for produktspesifikasjoner, som også inneholder spesifikasjoner med status «SOSI godkjent», og SOSI Del 2 har en gyldig objektkatalog for Plan. Den rettslige forpliktelsen knytter seg til de navngitte og godkjente spesifikasjonene, og når SOSI bare i den grad spesifikasjonene bygger på SOSI-reglene. Hvor langt hver enkelt spesifikasjon gjør det, må kontrolleres i spesifikasjonen selv.

**Fakta:** Digdirs referansekatalog for IT-standarder oppfører SOSI som arkivformat for kart, med henvisning til riksarkivarens forskrift (FOR-2017-12-19-2286) og SOSI versjon 4.5. Riksarkivarens forskrift er opphevet ved § 52 i forskrift om dokumentasjon og arkiv (arkivforskrifta), FOR-2025-12-17-2647, som gjelder fra 1. januar 2026. Arkivforskrifta § 30 krever at statlige organ avtaler filformat for datafiler i uttrekk med Nasjonalarkivet, og nevner ikke SOSI.

**Deduksjon:** SOSIs rolle som forskriftsfestet arkivformat har dermed falt bort, og bruken som arkivformat avhenger nå av avtale med Nasjonalarkivet. Oppføringen i referansekatalogen er ikke oppdatert etter dette.

Etterlevelse skjer ellers gjennom kravstilling i kartleggingskontrakter, gjennom samarbeidet i Norge digitalt og gjennom at dataeiere lager produktspesifikasjoner etter SOSI-reglene. **Ikke offentlig dokumentert i denne arbeidsøkten:** En samlet ordning for kontroll av at leverte data følger SOSI, utover kravene til godkjenning av produktspesifikasjoner.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`. `Juridisk samhandling` er ikke satt: kart- og planforskriften binder bruken av produktspesifikasjonene, men SOSI tolker ikke regelverket og former det ikke. `Informasjonsforvaltning: Oversikt over informasjonsmodeller` er ikke satt, fordi registrene der modellene og spesifikasjonene gjøres tilgjengelige, drives i Geonorge.

- **Informasjonsforvaltning: Informasjonsarkitektur** SOSI fastsetter reglene for hvordan geografisk informasjon modelleres i UML, realiseres i SOSI-format og GML og beskrives med metadata, og gir en felles objektkatalog som produktspesifikasjonene bygger på.
- **Standardisering: Forvaltningsstandarder** SOSI er den nasjonale bransjestandarden for geografisk informasjon, utviklet og vedtatt i en egen standardiseringsprosess under Kartverket og tilpasset de internasjonale ISO 19100-standardene.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Dataeiere i stat og kommune | Felles regler for egne geodataprodukter | Utarbeiding av produktspesifikasjoner og datamodeller | Produktspesifikasjonsregisteret har mange eiere, blant dem direktorater, Statistisk sentralbyrå og Kommunal- og distriktsdepartementet |
| Kommuner og plankonsulenter | Leveranser som oppfyller forskriftskrav | Arealplaner, planregister og offentlig kartgrunnlag | Kravet følger av kart- og planforskriften via produktspesifikasjonene |
| Geomatikkbransjen og systemleverandører | Forutsigbare formater og modeller | Kartlegging, oppmåling, programvare og dataleveranser | Bransjen er representert i standardiseringskomiteen |
| Brukere av geodata | Data som kan kombineres på tvers av kilder | Analyse, saksbehandling og tjenesteutvikling | Får nytte gjennom data som er harmonisert etter samme regler |
| Arkivskapere | Avklart format for langtidsbevaring av kartdata | Uttrekk og avlevering | Formatet avtales nå med Nasjonalarkivet |

## Normerende innhold
**Fakta:** Kartverket deler SOSI-serien i fire deler:

- **Del 1 – Generell del:** basisstandarder for modellering, formatering, metadata og lignende, blant annet regler for UML-modellering, generelle typer, metadataprofil, nettverk og lineære referanser, realisering i SOSI-format og i GML, og krav til og godkjenning av produktspesifikasjoner.
- **Del 2 – Generell objektkatalog:** objekttyper med egenskaper og assosiasjoner som er felles innenfor et fagområde eller på tvers av flere. Katalogen er tilgjengelig i SOSI modellregister.
- **Del 3 – Produktspesifikasjoner:** spesifikasjoner for konkrete kart- og geodataprodukter, som bygger på Del 2 og kan omfatte registreringsinstruks og forvaltningsbeskrivelse. Dataeierne er ansvarlige for å lage dem, og SOSI-standardiserte produktspesifikasjoner går gjennom en egen standardiseringsprosess.
- **Standarder for geografisk informasjon:** fagstandarder for kart, oppmåling og geografisk informasjon, blant annet geodetisk grunnlag, geosynkronisering, satellittbasert posisjonsbestemmelse, posisjonstjenester i sanntid, produksjon av basis geodata, stedfesting av matrikkelenhets- og råderettsgrenser, stedfesting av natur- og samfunnsgeografisk informasjon, VA-ledningskartverk og grafisk utforming av kart.

Fra versjon 5.0 er realiseringen i SOSI-format og realiseringen i GML egne standarder. Begge er gyldige.

## Bruksområde
SOSI brukes når geodata skal modelleres, spesifiseres, produseres eller utveksles, og særlig når en virksomhet skal lage eller revidere en produktspesifikasjon for et geodataprodukt. Standardene avklarer hvilke objekttyper og egenskaper som skal brukes, hvordan modellen skal uttrykkes i UML, hvilket utvekslingsformat som gjelder og hvilke metadata som kreves.

Fagstandardene brukes i kartlegging og oppmåling, for eksempel ved krav til geodetisk grunnlag, stedfesting og nøyaktighet.

## Typiske analyse- og beslutningssituasjoner
- når en virksomhet skal etablere et nytt nasjonalt geodataprodukt og må avgjøre om det skal bygge på eksisterende objekttyper i SOSI Del 2
- når krav til leveranseformat og datamodell skal formuleres i kontrakter om kartlegging, oppmåling eller planleveranser
- når en løsning skal ta imot eller levere plandata eller data til det offentlige kartgrunnlaget, og må oppfylle produktspesifikasjoner som kart- og planforskriften viser til
- når det skal velges mellom SOSI-format og GML for utveksling eller lagring
- når geodata skal avleveres til arkiv, og format skal avtales med Nasjonalarkivet

## Når ressursen normalt ikke er tilstrekkelig alene
SOSI gir regler og modeller, men ikke data, distribusjon eller forpliktelse til deling. For å få effekt må standardene suppleres med produktspesifikasjonen for det aktuelle produktet, Geonorge for publisering av registre og distribusjon av data, avtaler i Norge digitalt om hvem som leverer hva, og rettslige krav som kart- og planforskriften der de gjelder. For tjenester og metadata på europeisk nivå må det i tillegg ses hen til internasjonale standarder og de europeiske kravene geodataloven gjennomfører.

## Scope og avgrensning
Inngår:
- regler for modellering, formatrealisering og metadata for geografisk informasjon
- generell objektkatalog og regler for produktspesifikasjoner
- nasjonale fagstandarder for kart, oppmåling og stedfesting
- prosessen for å utvikle, vedta og trekke tilbake slike standarder

Inngår ikke:
- registrene, katalogen og distribusjonsløsningene der standardene og dataene gjøres tilgjengelige
- avtalene om deling og finansiering av geodata mellom partene
- selve geodatasettene
- arkivfaglige krav til avlevering

Avgrensning mot `KART-002` Geonorge: Geonorge er løsningen som publiserer SOSI-registrene, modellregisteret og produktspesifikasjonsregisteret, og som distribuerer data. SOSI er innholdet i standardene, ikke publiseringsflaten.

Avgrensning mot `KART-005` Norge digitalt: Norge digitalt er arenaen der partene forplikter seg til felles krav og deling. SOSI er en av standardseriene partene bruker, men forvaltes i Kartverkets egen standardiseringsprosess.

Avgrensning mot `ARKIV-001` Noark 5: SOSI berører arkivområdet bare som mulig format for kartdata ved avlevering. Krav til arkivsystemer og arkivstruktur ligger utenfor.

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Kartverket, som eier SOSI-standardene og koordinerer standardiseringen av geografisk informasjon |
| Forvaltningsansvar | **Fakta:** Standardiseringssekretariatet i Kartverket organiserer arbeidet og utgir standardene. Sekretariatet tar imot behov for nye, endrede eller tilbaketrukne standarder, fremmer forslag til godkjenning, drifter registre og infrastruktur, kontrollerer harmonisering med nasjonale og internasjonale standarder og forvalter katalogen «Standarder geografisk informasjon» |
| Endringsprosess | **Fakta:** Behov meldes inn på eget skjema til sekretariatet. Prosjekter for revisjon og nye standarder er åpne for deltakelse, og pågående prosjekter og høringer publiseres på Geonorge. SOSI-referansegruppen er en distribusjonsliste mellom sekretariatet og bransjen for invitasjoner til prosjekter, høringer og informasjon om ferdige standarder. Prosessen er beskrevet i Kartverkets styrende dokument for utvikling av nasjonale bransjestandarder for geografisk informasjon |
| Publiserings- og beslutningsarena | **Fakta:** Standardiseringskomiteen for geomatikk er formelt beslutningsorgan. Den godkjenner oppstart av standardiseringsprosjekter, vedtar nye og reviderte standarder og trekker standarder tilbake, og beslutter ved konsensus. Komiteen ledes og administreres av sekretariatet, og har representanter fra blant annet Kartverket, direktorater, Kommunal- og distriktsdepartementet, kommunesektoren, universitetssektoren, geomatikkbransjen og Standard Norge. Komiteen kan foreslå for Standardiseringsrådet at standarder for geomatikk tas inn i referansekatalogen. Standardene publiseres i registrene på Geonorge |

**Ikke offentlig dokumentert i denne arbeidsøkten:** Hvordan SOSI-serien formelt forholder seg til Standard Norges komitéarbeid og til ISO/TC 211, utover at Standard Norge sitter i komiteen og at produktspesifikasjonene følger NS-EN ISO 19100-standarder.

## Relasjon til andre ressurser
- **Geonorge (`KART-002`)**: publiserer SOSI-registrene, SOSI modellregister og registeret for produktspesifikasjoner, og distribuerer data som er produsert etter dem.
- **Norge digitalt (`KART-005`)**: samarbeidet der partene forplikter seg til felles tekniske krav for geodata. SOSI er en del av det tekniske grunnlaget, men vedtas i Kartverkets egen prosess.
- **Referansekatalogen for IT-standarder (`DIGDIR-026`)**: oppfører SOSI som arkivformat for kart, med henvisning til den opphevede riksarkivarens forskrift.
- **Felles informasjonsmodeller (`DIGDIR-069`)**: tverrsektorielle prinsipper og modelleringsregler. SOSI er det sektorspesifikke regelverket for geografisk informasjon.
- **Noark 5 (`ARKIV-001`)**: arkivstandarden for journal- og arkivsystemer. Berøringspunktet er bare SOSI som format for kartdata ved avlevering.
- **Kart- og planforskriften (FOR-2025-01-20-52)**: binder bruken av nasjonale produktspesifikasjoner for arealplan, planregister og offentlig kartgrunnlag. Den er ikke egen ressurs i registeret.
- **Geodataloven (LOV-2010-09-03-56)**: § 8 om harmonisering og metadata. Den er ikke egen ressurs i registeret.
- **Arkivforskrifta (FOR-2025-12-17-2647)**: § 30 om avtale om filformat med Nasjonalarkivet. Den er ikke egen ressurs i registeret.
- **NS-EN ISO 19109, 19131 og 19136**: internasjonale standarder produktspesifikasjonene følger. De er ikke egne ressurser i registeret.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er at dataeiere, kommuner og leverandører kan bygge på samme objekttyper, modelleringsregler og formater i stedet for å avtale dem i hver leveranse. Det senker kostnaden ved kartlegging, planleveranser og dataflyt mellom kommune, stat og bransje.

Arkitekturverdien er et felles semantisk og teknisk grunnlag for geodata i Norge, med en lagdeling fra generelle regler via objektkatalog til konkrete produktspesifikasjoner. Lagdelingen gjør det mulig å kombinere data fra ulike produsenter og å kontrollere leveranser mot en kjent spesifikasjon.

## Konsekvens ved manglende bruk eller avvik
Lager hver dataeier egne modeller og formater, blir geodata fra ulike kilder vanskelige å sammenstille, og hver integrasjon krever særtilpasning. For plandata og offentlig kartgrunnlag gir avvik fra produktspesifikasjonene brudd på kart- og planforskriften.

**Deduksjon:** Løsninger som bygger på ulike versjoner av objektkatalogen, for eksempel tilbaketrukne 4.x-versjoner, kan få avvik seg imellom selv om begge oppgir å følge SOSI.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Endringsstyring | Mange deler av objektkatalogen er tilbaketrukket, og flere versjoner er i bruk | Uklart hvilken versjon som skal legges til grunn | Oppgi versjon og status ved kravstilling, og kontrollere mot registeret |
| Format | Uavklart om SOSI-formatet fases ut til fordel for GML | Investeringer i SOSI-format kan bli kortlivet | Vurdere GML-realiseringen der begge er mulige |
| Forankring | SOSI er ikke nevnt i forskrift, og bindingen går via produktspesifikasjonene | Ulik oppfatning av hvor bindende SOSI er | Lese de konkrete spesifikasjonene og forskriftskravene sammen |
| Arkiv | Referansekatalogen viser til opphevet forskrift | Feil grunnlag for valg av arkivformat | Avtale format med Nasjonalarkivet etter arkivforskrifta § 30 |
| Gjenbruk | Lisens for standarddokumentene er ikke oppgitt | Usikkerhet ved gjenbruk og bearbeiding av modeller og tekst | Avklare med standardiseringssekretariatet |

## Publiseringsform og tilgjengelighet
Standardene publiseres som dokumenter, hovedsakelig PDF, i registrene for SOSI på register.geonorge.no, med status og versjon for hver standard. Objektkatalogen er tilgjengelig i SOSI modellregister, og produktspesifikasjonene i et eget register på Geonorge. Registrene kan eksporteres i flere maskinlesbare formater. Prosess, prosjekter og høringer beskrives på Geonorges sider om standardisering.

**Lisens:** Ikke offentlig dokumentert. Registersidene for SOSI og produktspesifikasjonene oppgir ingen lisens.

## Støtter arkitekturprinsipper
- **P6: Lag digitale løsninger som støtter samhandling**
  SOSI gir felles semantikk og felles utvekslingsformater for geodata, og produktspesifikasjonene følger internasjonale ISO-standarder.
- **P4: Del og gjenbruk data**
  Felles objektkatalog og produktspesifikasjoner gjør det mulig å bruke data fra ulike produsenter sammen.
- **P7: Sørg for tillit til oppgaveløsningen**
  Kjente spesifikasjoner gjør det mulig å kontrollere at leverte data har avtalt innhold og kvalitet.

Svakheter, spenninger og begrensninger mot prinsippene: SOSI-formatet er et særnorsk format, og de mange tilbaketrukne versjonene av objektkatalogen kan gi friksjon ved samhandling på tvers av løsninger og mot europeiske krav. At lisens ikke er oppgitt, svekker gjenbruken av selve modellene.

## Lenke til dokumentasjon
- https://www.geonorge.no/Geodataarbeid/standardisering/
- https://www.geonorge.no/Geodataarbeid/standardisering/standarder-under-sosi-paraplyen/
- https://www.geonorge.no/Geodataarbeid/standardisering/slik-jobber-vi-med-standardisering/
- https://register.geonorge.no/standarder/sosi
- https://register.geonorge.no/standarder/sosi/del-1-generell-del
- https://register.geonorge.no/standarder/sosi/del-2-generell-objektkatalog
- https://register.geonorge.no/standarder/sosi/standarder-geografisk-informasjon
- https://register.geonorge.no/produktspesifikasjoner

## Kildegrunnlag brukt i utfyllingen
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-10-24
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-10-24
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-10-24
- https://www.geonorge.no/Geodataarbeid/standardisering/ , kontrollert 2026-10-24
- https://www.geonorge.no/Geodataarbeid/standardisering/standarder-under-sosi-paraplyen/ , kontrollert 2026-10-24
- https://www.geonorge.no/Geodataarbeid/standardisering/slik-jobber-vi-med-standardisering/ , kontrollert 2026-10-24
- https://www.geonorge.no/Geodataarbeid/standardisering/slik-jobber-vi-med-standardisering/standardiseringskomiteen-for-geomatikk/ , kontrollert 2026-10-24
- https://www.geonorge.no/Geodataarbeid/standardisering/slik-jobber-vi-med-standardisering/sosi-referansegruppe/ , kontrollert 2026-10-24
- https://www.geonorge.no/Geodataarbeid/standardisering/nasjonal-strategi-for-viderutvikling-av-sosi/ , kontrollert 2026-10-24
- https://register.geonorge.no/standarder/sosi , kontrollert 2026-10-24
- https://register.geonorge.no/standarder/sosi/del-1-generell-del , oppdatert 27.06.2025, kontrollert 2026-10-24
- https://register.geonorge.no/standarder/sosi/del-2-generell-objektkatalog , oppdatert 17.07.2026, kontrollert 2026-10-24
- https://register.geonorge.no/standarder/sosi/standarder-geografisk-informasjon , oppdatert 31.08.2026, kontrollert 2026-10-24
- https://register.geonorge.no/produktspesifikasjoner , oppdatert 19.10.2026, kontrollert 2026-10-24
- https://lovdata.no/dokument/SF/forskrift/2025-01-20-52 , kontrollert 2026-10-24
- https://lovdata.no/dokument/NL/lov/2010-09-03-56 , kontrollert 2026-10-24
- https://lovdata.no/dokument/SF/forskrift/2025-12-17-2647 , kontrollert 2026-10-24
- https://www.digdir.no/standarder/sosi-samordna-opplegg-stadfesta-informasjon/1729 , sist oppdatert 21. april 2022, kontrollert 2026-10-24
- https://www.digdir.no/standarder/arkivstandarder/1482 , sist oppdatert 6. september 2023, kontrollert 2026-10-24
- https://www.iana.org/assignments/media-types/text/vnd.sosi , registrert 3. juni 2019, kontrollert 2026-10-24
