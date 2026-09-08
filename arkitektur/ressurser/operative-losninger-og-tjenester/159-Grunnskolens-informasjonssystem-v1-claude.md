# Produkt-canvas: Grunnskolens informasjonssystem (GSI)

## Navn
Grunnskolens informasjonssystem (GSI)

## Ressurs ID
UDIR-003

## Status/Livsfase
**Produksjon, med teknisk omlegging i 2026** — løsningen er i ordinær drift, men innsamlingen høsten 2026 skjer i en ny teknisk løsning.

**Fakta:** Udir opplyser at GSI fra høsten 2026 samles inn i en ny teknisk løsning, at rapporteringen i hovedsak er den samme som før, og at tilgang nå gis gjennom Altinn med egen rettighet for GSI-administrasjon. Innlogging åpner 14. september, og innsamlingen starter 21. september.

## Modenhet
**Høy funksjonell modenhet, ny teknisk plattform** — datainnholdet og rapporteringsmønsteret er innarbeidet over mange år, mens den tekniske løsningen er ny fra høsten 2026.

- GSI omtales av Udir som Norges offisielle oversikt over grunnskoleopplæringen og den viktigste kilden til grunnskoledata i landet.
- Skolene som skal rapportere hentes fra Nasjonalt skoleregister (NSR), som igjen bygger på Virksomhets- og foretaksregisteret.
- Løsningen støtter filimport fra skoleadministrative systemer, slik at rapporteringen ikke må skje manuelt.
- Historiske data fra tidligere år er fortsatt tilgjengelige gjennom den forrige rapporteringsløsningen.
- Tilgangsstyringen er flyttet til Altinn, og alle brukere må ha riktig rettighet før de kan rapportere.

**Deduksjon:** Den tekniske omleggingen er den vesentligste usikkerheten i 2026. Innholdet endres bare i mindre grad, men overgangen til ny løsning og til Altinn-basert tilgangsstyring flytter arbeid ut til skoleeierne, som må ha delegert rettigheter i tid før innsamlingen starter.

## Kort beskrivelse
Grunnskolens informasjonssystem er den nasjonale innrapporteringsløsningen for grunnskolen i Norge, inkludert norske grunnskoler i utlandet. Skolene registrerer én gang i året opplysninger om elever, ansatte, årstimer, spesialundervisning, språkopplæring og øvrig drift, og datagrunnlaget blir Norges offisielle oversikt over grunnskoleopplæringen.

Løsningen har tre separate innganger: grunnskole, voksenopplæring og kulturskole. Hvilke skoler som skal rapportere, bestemmes av Nasjonalt skoleregister, og tilgangen styres gjennom Altinn med en egen rettighet for GSI-administrasjon.

Fra høsten 2026 samles GSI inn i en ny teknisk løsning. Rapporteringen er i hovedsak den samme som før, med noen mindre justeringer i skjemaet.

## Kapabiliteter
- **Datakilder: Grunndata**
  Løsningen etablerer det autoritative datagrunnlaget om grunnskoleopplæringen, og skoleutvalget hentes fra Nasjonalt skoleregister.
- **Datautveksling og integrasjon: Bruke data fra andre**
  Løsningen henter skoleopplysninger fra NSR og tar imot filimport fra skoleadministrative systemer framfor å kreve manuell registrering.
- **Datautveksling og integrasjon: Dele data med andre**
  Innsamlede data publiseres videre gjennom Statistikkbanken og brukes av skoleeiere, statsforvaltere, direktorat og departement.
- **Tillit: Tilgangsstyring**
  Tilgang til rapportering gis gjennom Altinn, med en egen rettighet som skoleeier må delegere til de som skal rapportere.

## Produktmål
Dokumenterte mål:
- Registrere informasjon om grunnskolene i Norge og norske grunnskoler i utlandet.
- Gi Norges offisielle oversikt over grunnskoleopplæringen.
- Gi skoleeiere, statsforvalteren, Utdanningsdirektoratet og Kunnskapsdepartementet et felles datagrunnlag.

Operative mål utledet fra kildene:
- Samle rapporteringen i én årlig syklus med felles frister framfor spredte innhentinger.
- Redusere manuell registrering gjennom filimport fra skoleadministrative systemer.
- Bruke ett autoritativt skoleregister som grunnlag for hvem som skal rapportere.

## Brukerbehov
- Skoleeiere trenger sammenlignbare tall om sine egne skoler for å kunne styre og prioritere.
- Skolene trenger å rapportere én gang, i én løsning, framfor å svare på gjentatte enkeltforespørsler.
- Statsforvalteren trenger et datagrunnlag for tilsyn og oppfølging av kommunene.
- Direktorat og departement trenger nasjonale tall for regelverksutvikling, tilskuddsforvaltning og styring.
- Forskere og offentligheten trenger tilgang til grunnskoledata over tid.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Skoler og skoleledere | Rapportere korrekte tall med minst mulig manuelt arbeid | Årlig innrapportering | Trenger delegert Altinn-rettighet før innsamlingen starter |
| Skoleeiere: kommuner og private skoleeiere | Kvalitetssikre og godkjenne rapporteringen, og bruke tallene lokalt | Styring og kvalitetsutvikling | Ansvarlig for at rettigheter er delegert i tid |
| Statsforvalteren | Oversikt over kommunene i eget embete | Tilsyn og veiledning | Egne samlinger om GSI arrangeres av statsforvalterne |
| Utdanningsdirektoratet | Nasjonalt datagrunnlag | Statistikk, tilskuddsforvaltning og regelverksarbeid | Forvalter løsningen |
| Kunnskapsdepartementet | Grunnlag for politikkutvikling og budsjett | Styring av sektoren | Bruker aggregerte tall |
| Leverandører av skoleadministrative systemer | Kunne levere data på riktig format | Filimport til GSI | Berøres direkte av teknisk omlegging |
| Forskere og offentligheten | Tilgang til tall over tid | Analyse og innsyn | Får data gjennom Statistikkbanken |

## Hovedfunksjoner

### Primære funksjoner
Løsningen gjennomfører den årlige innsamlingen av grunnskoledata. Skolene fyller ut et skjema med opplysninger om elever, ansatte, timer og drift, og skoleeier kvalitetssikrer før tallene låses. Innsamlingen har faste datoer, og for 2026 åpner innlogging 14. september med innsamlingsstart 21. september.

Løsningen bestemmer rapporteringsplikten ut fra Nasjonalt skoleregister. Det betyr at skoleutvalget ikke vedlikeholdes i GSI selv, men følger av registreringene i NSR, som igjen bygger på Virksomhets- og foretaksregisteret. Er en skole feilregistrert i NSR, slår det direkte ut i hvem som blir bedt om å rapportere.

Løsningen tar imot filimport fra skoleadministrative systemer. Det gjør at data som allerede finnes i skolens fagsystem kan overføres framfor å tastes inn på nytt, som er den vesentligste arbeidsbesparelsen i rapporteringen.

Løsningen styrer tilgang gjennom Altinn. Alle brukere må ha rettigheten for GSI-administrasjon, som skoleeier delegerer. Dette er en endring fra tidligere tilgangsmodell og må være på plass før innsamlingen kan begynne.

Løsningen leverer tallene videre til Statistikkbanken, der de publiseres som rapporter om elevtall, lærertetthet og årsverk. Løsningen har i tillegg egne rapportvisninger som skoleeier kan bruke i kvalitetssikringen underveis.

### Typiske brukssituasjoner (generisk)
- En skole skal gjennomføre den årlige rapporteringen innen fristen.
- En skoleeier skal kontrollere og godkjenne tallene for alle sine skoler før innsamlingen lukkes.
- En kommune skal sammenligne lærertetthet eller spesialundervisning med nasjonale tall.
- Statsforvalteren skal forberede tilsyn og trenger tallgrunnlaget for kommunene i embetet.
- En leverandør av skoleadministrativt system skal tilpasse eksporten til den nye løsningen.

### Når GSI normalt ikke er førstevalg
- Når behovet er registerdata om skolen som virksomhet — organisasjonsnummer, adresse, eierform. Da er Nasjonalt skoleregister kilden.
- Når behovet er data om videregående opplæring. GSI dekker grunnskolen, mens videregående dekkes gjennom VIGO-sporet.
- Når behovet er elevenes opplevelse av skolemiljøet. Da er Elevundersøkelsen kilden.
- Når behovet er læreplaner, fagkoder eller opplæringstilbud. Da er `Grep` kilden.
- Når behovet er data på individnivå. GSI samler aggregerte tall per skole, ikke elevdata.

### Scope og avgrensning
Inngår:
- Årlig innrapportering fra grunnskoler, voksenopplæring og kulturskole.
- Norske grunnskoler i utlandet.
- Filimport fra skoleadministrative systemer.
- Tilgangsstyring gjennom Altinn.
- Rapportvisninger og videre publisering i Statistikkbanken.

Inngår ikke:
- Registerføring av skoler som virksomheter. Det skjer i NSR.
- Løpende drift av skolens egen administrasjon.
- Data om videregående opplæring.
- Personopplysninger om enkeltelever.

## Veikart over kommende funksjonalitet
**Fakta:** Udir opplyser at GSI fra høsten 2026 samles inn i en ny teknisk løsning, at rapporteringen i hovedsak er den samme som før med noen mindre justeringer, og at det er publisert et webinaropptak som gjennomgår endringene. Historiske data fra tidligere år er fortsatt tilgjengelige gjennom den forrige rapporteringsløsningen.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Hva den nye løsningen bygger på teknisk, om og når den forrige løsningen skal avvikles, og om historiske data skal migreres inn i den nye.

## Forretningsverdi/Verdiforslag
- For skolene: én årlig rapportering med felles frist og mulighet for filimport, framfor gjentatte enkeltforespørsler fra flere nivåer.
- For skoleeierne: sammenlignbare tall om egne skoler, og et grunnlag for å se seg selv mot nasjonale nivåer.
- For statsforvalteren: et felles datagrunnlag for tilsyn som ikke må innhentes særskilt fra hver kommune.
- For direktorat og departement: nasjonale tall som gjør det mulig å følge utviklingen i grunnskolen over tid, og å knytte tilskudd og regelverk til faktiske forhold.
- For offentligheten og forskningen: åpen tilgang til grunnskoledata gjennom Statistikkbanken.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Teknisk omlegging | Ny løsning tas i bruk midt i en innsamlingssyklus med faste frister. Feil eller forsinkelser rammer alle skoler samtidig | Udir har publisert webinaropptak og veiledning, og statsforvalterne arrangerer egne samlinger |
| Tilgangsstyring | Overgangen til Altinn-rettighet gjør at en skole uten delegert rettighet ikke kan rapportere, uavhengig av om dataene er klare | Skoleeier må delegere rettigheten for GSI-administrasjon før innlogging åpner |
| Avhengighet til NSR | Rapporteringsplikten følger av NSR. Feil eller manglende registrering der gir feil skoleutvalg i GSI | Følger av at NSR er autoritativ kilde; feilen må rettes i registeret, ikke i GSI |
| Datakvalitet | Tallene rapporteres av skolene selv, med varierende tolkning av skjemafeltene | Skoleeier kvalitetssikrer, og Udir publiserer veiledning til feltene |
| Integrasjon | Leverandører av skoleadministrative systemer må tilpasse eksport til ny løsning innenfor samme tidsvindu | Ikke dokumentert hvilken frist leverandørene har fått |
| Kontinuitet i tidsserien | Justeringer i skjemaet kan gjøre enkelte felt ikke direkte sammenlignbare over omleggingen | Udir omtaler endringene som mindre justeringer, men konsekvensen for tidsserien er ikke dokumentert |

## Kanaler
- Rapporteringsløsningen på https://gsi.udir.no/ med tre separate innganger for grunnskole, voksenopplæring og kulturskole.
- Altinn som tilgangs- og innloggingskanal.
- Filimport fra skoleadministrative systemer.
- Statistikkbanken hos Udir for publisering av resultatene.
- Hjelpesider og eget serviceskjema for teknisk brukerstøtte.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten.** Kildene opplyser at det tas i bruk en ny teknisk løsning fra høsten 2026, men beskriver ikke driftsplattform, skylokasjon eller teknisk arkitektur. Tilgangsstyringen skjer gjennom Altinn.

## Gjenbruk
**Middels gjenbruksverdi:**
- Datagrunnlaget har høy gjenbruksverdi og publiseres videre gjennom Statistikkbanken, tilgjengelig for skoleeiere, forskere og offentligheten.
- Filimport fra skoleadministrative systemer er et definert integrasjonspunkt som mange leverandører bruker.
- Bruken av Altinn for tilgangsstyring følger et nasjonalt fellesmønster framfor en egen løsning.
- Selve rapporteringsløsningen er sektorspesifikk og ikke ment gjenbrukt av andre. Kildene beskriver ikke et åpent API for uttak av GSI-data.

**Vanlige kombinasjoner med andre produkter:**
- `Nasjonale registre for barnehage og grunnopplæring` (`UDIR-002`) der Nasjonalt skoleregister avgjør hvilke skoler som skal rapportere.
- `Altinn Autorisasjon` (`DIGDIR-004`) som styrer hvem som har rettighet til å rapportere på vegne av skolen.
- `Grep` (`UDIR-001`) som forvalter fagkodene og læreplanverket som GSI rapporterer aktivitet mot.
- `Elevundersøkelsen` (`UDIR-004`) som dekker elevenes opplevelse der GSI dekker strukturtallene.
- `Enhetsregisteret` (`BRREG-003`) som ligger bak Virksomhets- og foretaksregisteret, som NSR igjen bygger på.

**Kildekode:** Ikke offentlig dokumentert. Kildene beskriver ikke om løsningens kode er publisert.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Løsningen henter skoleutvalget fra NSR framfor å vedlikeholde eget register, tar imot filimport framfor å kreve manuell registrering, og publiserer resultatene videre i Statistikkbanken.
- **P5: Del og gjenbruk løsninger**
  Tilgangsstyringen er lagt til Altinn som nasjonal fellesløsning framfor en egen brukeradministrasjon.
- **P6: Lag digitale løsninger som støtter samhandling**
  Løsningen kobler skoleadministrative systemer, et nasjonalt register og en statistikkflate i samme kjede.
- **P2: Ta arkitekturbeslutninger på rett nivå**
  Støttes delvis. Rapporteringsplikten og skjemaet fastsettes nasjonalt, mens kvalitetssikringen skjer hos skoleeier der kunnskapen om tallene finnes.

Spenning og begrensning: løsningen er sterk som datainnsamler og svak som datadeler. Tallene blir tilgjengelige gjennom Statistikkbanken, men kildene beskriver ikke et API som gjør GSI-data maskinelt tilgjengelig på samme måte som registerdataene i NSR. Avhengigheten til NSR er arkitektonisk riktig, men den gjør samtidig at en registerfeil ett sted får konsekvenser for rapporteringsplikten et annet sted. Den tekniske omleggingen høsten 2026 er en reell risiko fordi innsamlingen har harde frister og ingen alternativ kanal.

## Finansiering
Løsningen forvaltes av Utdanningsdirektoratet som del av direktoratets ordinære virksomhet. Kildene beskriver ikke en egen finansieringsmodell.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Utdanningsdirektoratet | udir.no og gsi.udir.no |
| Driftsansvar | Utdanningsdirektoratet, ny teknisk løsning fra høsten 2026 | udir.no om GSI-innsamling |
| Tilgangsstyring | Skoleeier delegerer Altinn-rettigheten for GSI-administrasjon | udir.no om tilgang |
| Kvalitetssikring av rapporterte tall | Skoleeier | udir.no om GSI |
| Grunnlag for rapporteringsplikt | Nasjonalt skoleregister, som bygger på Virksomhets- og foretaksregisteret | udir.no om GSI-innsamling |
| Budsjettansvar og styringsmodell | Ikke offentlig dokumentert i denne arbeidsøkten | — |

## Lenke til dokumentasjon
- https://www.udir.no/tall-og-forskning/innrapportering/gsi/
- https://www.udir.no/tall-og-forskning/statistikk/gsi-innsamling/
- https://gsi.udir.no/
- https://gsi.udir.no/hjelp/
- https://gsi.udir.no/hjelp/nytt/system

## Kildegrunnlag brukt i utfyllingen
- https://www.udir.no/tall-og-forskning/innrapportering/gsi/, kontrollert 2026-09-08
- https://www.udir.no/tall-og-forskning/statistikk/gsi-innsamling/, kontrollert 2026-09-08
- `arkitektur/ressurser/operative-losninger-og-tjenester/152-Nasjonale-registre-for-barnehage-og-grunnopplaering-v1-claude.md`, kontrollert 2026-09-08
- `arkitektur/ressurser/normerende-ressurser/151-Grep-v1-claude.md`, kontrollert 2026-09-08
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-08
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-08
