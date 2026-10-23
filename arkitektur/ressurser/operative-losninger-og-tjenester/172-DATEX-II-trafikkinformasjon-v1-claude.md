# DATEX II trafikkinformasjon

## Navn
DATEX trafikkinformasjon fra Statens vegvesen (DATEX II versjon 3.1)

## Ressurs ID
SVV-003

## Status/Livsfase
**Produksjon** - trafikkmeldinger, værdata, værprognoser og webkamera publiseres i drift; publikasjonen for reisetider er under utfasing.

**Fakta:** Statens vegvesen tilbyr informasjon om vær, reisetider, kamerabilder og trafikk i DATEX II versjon 3.1. Publikasjonene for reisetider (`TravelTimeData` og `PredefinedTravelTimeLocations`) skal saneres: Statens vegvesen venter at saneringen starter i november 2026 og pågår gjennom 2027, og at datakvaliteten gradvis kan bli dårligere etter hvert som utstyr fases ut.

## Modenhet
**Høy modenhet for trafikkmeldinger og værdata, synkende for reisetider:**
- DATEX II er en europeisk CEN-standard for trafikk- og reiseinformasjon, med datamodeller i CEN 16157-serien.
- Statens vegvesen publiserer åtte DATEX-publikasjoner fra ett felles endepunkt, med spesifikasjoner, WSDL og eksempeldata på git.vegvesen.no.
- Tilgangen er formalisert gjennom bestilling, registrering og egne bruksvilkår.
- Reisetidene bygger på gammelt utstyr som skal fases ut, og Statens vegvesen har ennå ikke beskrevet hvilken løsning som kommer i stedet.

**Deduksjon:** Ressursen er moden for trafikkmeldinger, værdata og webkamera. Det svakeste leddet er reisetidene, som ikke bør brukes som grunnlag for nye tjenester før erstatningen er kjent.

## Kort beskrivelse
DATEX II er en europeisk standard for utveksling av trafikkinformasjon mellom vegmyndigheter og tjenesteleverandører, bygd på XML-meldinger. Statens vegvesen bruker standarden til å publisere trafikkinformasjon fra riks- og fylkesvegnettet som åpne data: trafikkmeldinger om hendelser og forhold som påvirker trafikken, målinger fra værstasjoner langs vegen, værprognoser for de samme stasjonene, bilder fra webkamera og målte reisetider på utvalgte strekninger. Tjenesten er gratis, men krever at brukeren bestiller tilgang og registreres som DATEX-bruker. Ressursen er Statens vegvesens publisering av data i formatet, ikke selve standarden.

## Kapabiliteter
- **Datakilder: Sanntidsdata** Statens vegvesen publiserer trafikkmeldinger fortløpende, værmålinger hvert tiende minutt og reisetider hvert femte minutt fra eget måle- og meldingsapparat langs vegnettet.
- **Datakilder: Åpne data** Statens vegvesen gjør DATEX-dataene tilgjengelige gratis under NLOD i et maskinlesbart standardformat; tilgangen krever registrering, men ikke betaling eller særskilt formål.
- **Datautveksling og integrasjon: Dele data med andre** Statens vegvesen deler trafikk- og værdata med media, trafikkinformasjonstjenester og andre aktører gjennom dokumenterte DATEX-endepunkter, slik at de kan bruke dataene i egne tjenester.

## Produktmål
**Dokumentert mål:** Statens vegvesen tilbyr DATEX til media, ulike tilbydere av trafikkinformasjon og andre aktører som vil bruke Statens vegvesens informasjon i egne tjenester.

**Deduksjon:** Målet er at trafikkinformasjon fra vegnettet skal nå trafikantene gjennom flere kanaler enn Statens vegvesens egne, og at dataene skal kunne brukes i europeiske tjenester fordi formatet er felleseuropeisk.

## Brukerbehov
- Trafikkinformasjonstjenester og navigasjonstjenester trenger oppdaterte meldinger om vegarbeid, stengte veger, ulykker, uvær, ras og flom.
- Media trenger trafikk- og føreforhold for å formidle dem videre.
- Aktører som vurderer føreforhold trenger målte værdata og prognoser fra stasjoner langs vegen.
- Tjenester som viser forholdene på vegen trenger bilder fra webkamera.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Tilbydere av trafikkinformasjon | Trafikkmeldinger og reisetider | Varsling og ruteinformasjon til trafikanter | Nevnt som målgruppe av Statens vegvesen |
| Media | Trafikkmeldinger, værdata og kamerabilder | Formidling av trafikk- og føreforhold | Nevnt som målgruppe av Statens vegvesen |
| Andre virksomheter | Trafikk- og værdata i egne tjenester | Ulike tjenester og analyser | **Ikke offentlig dokumentert:** hvilke virksomheter som bruker tjenesten |
| Trafikanter | Oppdatert informasjon om forholdene på vegen | Møter dataene gjennom tjenester fra andre og i Vegvesen trafikk | Ikke direkte brukere av DATEX-endepunktene |
| Statens vegvesen | Forvaltning av data, endepunkter og brukerregister | Publisering og varsling om oppgraderinger og nedetid | Forvalter ressursen |

## Hovedfunksjoner
**Trafikkmeldinger.** Publikasjonen dekker hendelser og forhold som kan påvirke trafikken på offentlige veger i hele landet, som vegarbeid, stengte veger, ulykker, uvær, ras og flom. Meldingene publiseres fortløpende og kan filtreres på tema, for eksempel ulykker, vedlikehold eller føreforhold.

**Værdata og værprognoser.** Værdata er målte meteorologiske verdier fra værstasjoner på riks- og fylkesvegnettet, oppdatert hvert tiende minutt. Værprognosene gir prognoser 24 timer fram i tid for de samme stasjonene og oppdateres hver time. Begge publikasjonene har en egen del med stasjonenes posisjon, vegnummer og navn.

**Webkamera og reisetider.** Webkamera gir bilder fra kameraer langs vegen, med oppdateringsfrekvens som varierer med kameratype og oppsett. Kameraer kan være ute av drift i dager eller vise et gammelt bilde, og skal ikke kunne identifisere personer eller registreringsnummer. Reisetider gir målt reisetid mellom to målepunkter på utvalgte strekninger i de største byene og på utvalgte riks- og europaveger, oppdatert hvert femte minutt. Målingen bygger på antenner som registrerer AutoPASS-brikker, og publikasjonen er under sanering.

**Tilgang og teknisk form.** Alle publikasjonene er pull-tjenester: mottakeren henter et øyeblikksbilde fra endepunktet, og det finnes ingen push-tjeneste. Dataene er XML etter DATEX II versjon 3.1, og spesifikasjoner, WSDL og eksempeldata ligger på git.vegvesen.no. Brukeren bestiller tilgang med organisasjon, organisasjonsnummer og formål, godtar bruksvilkårene og får brukernavn og passord som skal holdes fortrolig.

### Typiske brukssituasjoner (generisk)
- En tjeneste skal varsle trafikanter om hendelser, stengte veger eller vegarbeid.
- En tjeneste skal vise føreforhold basert på målte værdata og prognoser langs vegen.
- En tjeneste skal vise bilder fra vegnettet.
- En aktør med DATEX-støtte skal motta norske trafikkdata i samme format som data fra andre europeiske land.

### Når DATEX trafikkinformasjon normalt ikke er førstevalg
- Når behovet er sanntidsdata for kollektivtrafikk, som Entur publiserer i SIRI og GTFS-RT.
- Når behovet er data om selve vegnettet, som vegobjekter og vegreferanser, som forvaltes i NVDB.
- Når behovet er reisetider for nye tjenester, fordi publikasjonen er under sanering.
- Når mottakeren trenger hendelser levert som push eller i et enklere format enn XML; tjenesten tilbyr bare pull i DATEX-format.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Trafikkmeldinger for offentlige veger i Norge | Selve DATEX II-standarden, som forvaltes i europeisk standardisering |
| Værdata og værprognoser fra vegens værstasjoner | Vegnettsdata og vegobjekter (NVDB) |
| Webkamera og kameraplassering | Trafikkmengdedata og trafikkregistreringer |
| Reisetider på utvalgte strekninger (under sanering) | Push-levering av data |

## Veikart over kommende funksjonalitet
**Fakta:** Publikasjonene for reisetider skal saneres fra november 2026 og gjennom 2027. Statens vegvesen har testet nyere teknologier og datakilder for reisetid og vil publisere mer informasjon om videre steg og hvilke løsninger som blir tilgjengelige.

**Ikke offentlig dokumentert i denne arbeidsøkten:** hvilken løsning som erstatter dagens reisetider, og et samlet veikart for øvrige DATEX-publikasjoner.

## Forretningsverdi/Verdiforslag
### For tilbydere av trafikkinformasjon og næringsliv
- Gratis tilgang til trafikk- og værdata for hele riks- og fylkesvegnettet fra ett endepunkt.
- Standardformat som også brukes for trafikkdata i andre europeiske land.

### For media
- Oppdatert og autoritativ trafikk- og føreinformasjon som kan formidles videre.

### For trafikanter
- **Deduksjon:** Informasjon om hendelser og føreforhold når fram gjennom flere tjenester enn Statens vegvesens egne.

### For Statens vegvesen
- Ett register over DATEX-brukere gjør det mulig å varsle mottakerne om oppgraderinger og nedetid.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Utfasing | Reisetidsdataene kan gradvis bli dårligere og forsvinne | Sanering fra november 2026 gjennom 2027; erstatningsløsning ikke beskrevet |
| Tilgjengelighet | Endepunktet kan være nede, og webkamera kan være ute av drift i dager eller vise gamle bilder | Registrerte brukere varsles om oppgraderinger og nedetid; ingen oppetidsgaranti er beskrevet |
| Teknisk terskel | Mottakeren må kunne tolke DATEX II-XML, som er mer krevende enn et enkelt JSON-API | Spesifikasjoner, WSDL og eksempeldata på git.vegvesen.no; DATEX II Academy på datex2.eu |
| Juridisk | Bruksvilkårene forbyr å forvrenge informasjonen og å oversette norske meldinger, og krever kildeangivelse | Vilkårene godtas ved bestilling av tilgang |
| Sikkerhet | Brukernavn og passord kan deles videre i strid med vilkårene | Vilkårene sier at påloggingsinformasjonen er fortrolig |
| Dokumentasjon | Datasettoppføringen på dataut.vegvesen.no viser at dokumentasjonsressursen sist ble oppdatert i 2019 | Den gjeldende beskrivelsen ligger på vegvesen.no og git.vegvesen.no |

## Kanaler
- Maskinelt grensesnitt: DATEX II 3.1-endepunkter for pull av øyeblikksbilder, med SOAP og WSDL tilgjengelig.
- Tilgang krever bestilling og registrering som DATEX-bruker. Brukeren oppgir organisasjon, organisasjonsnummer og formål, godtar bruksvilkårene og får brukernavn og passord som er knyttet til DATEX-tjenesten.
- Brukerflate: Vegvesen trafikk (dit.vegvesen.no) viser DATEX-data i kart. Trafikkinformasjonen finnes også som WMS- og WFS-kartlag.
- Nyheter om DATEX publiseres i en RSS-strøm.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** driftsmodell, skyleverandør og vertsplassering. Kjent er at endepunktene eksponeres over internett fra Statens vegvesens domene.

## Gjenbruk
DATEX-dataene er åpne under NLOD, gratis og i et europeisk standardformat, men gjenbruk forutsetter registrering og at vilkårene om kildeangivelse og uforvrengt gjengivelse følges.

### Vanlige kombinasjoner med andre produkter
- **Deduksjon:** NVDB, når trafikkmeldinger skal kobles til vegnett og vegobjekter.
- **Deduksjon:** Entur sanntids- og rutedata, når en tjeneste skal kombinere vegtrafikk med kollektivtrafikk.

**Kildekode:** Ikke offentlig dokumentert. Statens vegvesen publiserer spesifikasjoner, WSDL og eksempeldata på git.vegvesen.no, men ikke kildekoden til selve tjenesten.

**Lisens:** Ikke offentlig dokumentert. Dataene er lisensiert under NLOD, som gjelder data og ikke kildekode.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Statens vegvesen deler trafikk- og værdata fra vegnettet som åpne data under NLOD.
- **P6: Lag digitale løsninger som støtter samhandling**
  Dataene publiseres i en europeisk standard, slik at mottakere kan bruke samme format for trafikkdata fra flere land.

**Spenning og begrensning:** Registreringskravet med brukernavn og passord gir en terskel som ellers ikke er vanlig for åpne data, og XML-formatet krever mer av mottakeren enn enklere API-er. Saneringen av reisetidene viser at en del av datagrunnlaget kan forsvinne uten at erstatningen er kjent.

## Finansiering
**Fakta:** Tjenesten er gratis for brukerne.

**Ikke offentlig dokumentert i denne arbeidsøkten:** hvordan utvikling og drift finansieres.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Statens vegvesen | vegvesen.no, side om DATEX |
| Driftsansvar | Statens vegvesen | Endepunkter på Statens vegvesens domene; varsling om nedetid til registrerte brukere |
| Budsjettansvar | Ikke offentlig dokumentert i denne arbeidsøkten | - |
| Styringsmodell for standarden | DATEX II er en europeisk CEN-standard; standardiseringsarbeidet videreføres gjennom NAPCORE | datex2.eu |

## Lenke til dokumentasjon
- Kva er DATEX: https://www.vegvesen.no/nn/fag/teknologi/data-og-api-ar/et-utvalg-apne-data/kva-er-datex/
- Få tilgang: https://www.vegvesen.no/nn/fag/teknologi/data-og-api-ar/et-utvalg-apne-data/kva-er-datex/fa-tilgang/
- Planlagt sanering av reisetidsdata: https://www.vegvesen.no/nn/fag/teknologi/data-og-api-ar/et-utvalg-apne-data/kva-er-datex/informasjon-og-nyheiter/planlagt-sanering-av-reisetidsdata/
- Engelsk versjon: https://www.vegvesen.no/en/fag/technology/open-data/a-selection-of-open-data/what-is-datex/
- Spesifikasjoner for DATEX 3.1: https://git.vegvesen.no/projects/DATEX2/repos/datex2-spesifications/browse/3.1
- Datasettoppføring: https://dataut.vegvesen.no/en/dataset/trafikkmeldinger/resource/542496d4-be2b-4053-8dff-e37d93e4a739
- Vegvesen trafikk: https://dit.vegvesen.no/
- DATEX II: https://www.datex2.eu/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/operative-ressurs-canvas.system.md`
- Lokal fil: `config/templates/operative-ressurs-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Nettkilde: https://www.vegvesen.no/nn/fag/teknologi/data-og-api-ar/et-utvalg-apne-data/kva-er-datex/ (kontrollert 2026-10-23)
- Nettkilde: https://www.vegvesen.no/nn/fag/teknologi/data-og-api-ar/et-utvalg-apne-data/kva-er-datex/fa-tilgang/ (kontrollert 2026-10-23)
- Nettkilde: https://www.vegvesen.no/nn/fag/teknologi/data-og-api-ar/et-utvalg-apne-data/kva-er-datex/informasjon-og-nyheiter/planlagt-sanering-av-reisetidsdata/ (kontrollert 2026-10-23)
- Nettkilde: https://www.vegvesen.no/en/fag/technology/open-data/a-selection-of-open-data/what-is-datex/ (kontrollert 2026-10-23)
- Nettkilde: https://dataut.vegvesen.no/en/dataset/trafikkmeldinger/resource/542496d4-be2b-4053-8dff-e37d93e4a739 (kontrollert 2026-10-23)
- Nettkilde: https://www.datex2.eu/ (kontrollert 2026-10-23)

## Endringer fra forrige versjon
Første publiserte versjon. Det finnes ingen tidligere versjon av ressursen i repoet.
