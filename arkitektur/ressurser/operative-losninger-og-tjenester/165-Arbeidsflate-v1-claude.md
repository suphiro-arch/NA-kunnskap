# Arbeidsflate

## Navn
Arbeidsflate

## Ressurs ID
DIGDIR-071

## Status/Livsfase
**Produksjon** - etablert som hovedløsning for innboks og dialogoversikt i Altinn etter at Altinn II ble avviklet.

**Fakta:** Digdirs milepælsplan for Altinn beskriver at arbeidsflaten ble gjort tilgjengelig for alle brukere og etablert som primærløsning i fjerde kvartal 2025, mens den gamle innboksen fortsatt var tilgjengelig i en overgangsperiode. Altinn II ble avviklet 19. juni 2026, med 31. mai 2026 som siste frist for reetablering av tjenester i Altinn 3. Overgangsperioden med to parallelle innbokser er dermed over.

## Modenhet
**Middels til høy modenhet** - løsningen er i produksjon for alle brukere, men er fortsatt under aktiv videreutvikling.

- Teknisk: kildekoden er åpen og publisert under MIT-lisens i `Altinn/dialogporten-frontend`, med aktiv utvikling og et offentlig veikart.
- Funksjonelt: innboks, profil og innstillinger er etablert i Altinn 3, og historiske meldinger og innsendte skjemaer fra Altinn II gjøres tilgjengelige gjennom arbeidsflaten og Dialogporten.
- Organisatorisk: løsningen inngår i produktgruppen `Portalar og brukaroppleving` i Altinn-porteføljen, med egne tilbakemeldingskanaler i GitHub og på Slack.

**Deduksjon:** Det svakeste leddet er at arbeidsflaten arver et bruksmønster mange virksomheter og sluttbrukere har innarbeidet gjennom mange år i Altinn II, samtidig som innholdet nå hentes fra en ny datamodell i Dialogporten. Funksjonell modenhet må derfor vurderes per bruksområde, ikke bare ut fra at løsningen er i produksjon. Åpne endringsforslag i det offentlige veikartet viser at funksjonaliteten fortsatt bygges ut.

## Kort beskrivelse
Arbeidsflate er den felles brukerflaten for digital dialog med det offentlige i Altinn. Løsningen gir innbyggere og virksomheter én samlet oversikt over meldinger, oppgaver og dialoger fra ulike offentlige virksomheter, og har erstattet innboksen og arkivet i Altinn II.

Arbeidsflate lagrer ikke dialogene selv. Innholdet hentes fra Dialogporten gjennom API-er, og arbeidsflaten står for presentasjon, navigasjon, sortering og oppfølging. Skillet er viktig for å forstå hva løsningen er: Dialogporten er representasjons- og integrasjonslaget, mens Arbeidsflate er det visuelle laget oppå det.

Løsningen er også ment å kunne gjenbrukes. Digdir beskriver Arbeidsflate som et felles visuelt brukergrensesnitt som kan gjøres tilgjengelig i ulike portaler, ikke bare som Altinns egen innboks. Det gjør produktet relevant også for virksomheter som vurderer om de trenger å bygge en egen dialogoversikt.

## Kapabiliteter
Arbeidsflate er avhengig av flere kapabiliteter som realiseres andre steder. Autentisering leveres av ID-porten, representasjon og tilgangsstyring av Altinn Autorisasjon, og selve dialogrepresentasjonen av Dialogporten. Disse er beskrevet som avhengigheter under `Gjenbruk`, ikke som kapabiliteter Arbeidsflate selv realiserer.

- **Sluttbrukertjenester: Sammenhengende tjenester**
  Arbeidsflate samler meldinger, oppgaver og dialoger fra mange offentlige virksomheter i én oversikt, slik at brukeren slipper å oppsøke hver enkelt etat for å se hva som venter. Der Dialogporten gjør dialogene tilgjengelige i et felles format, er det Arbeidsflate som gir brukeren den samlede flaten.

- **Tillit: Sporbarhet og innsyn**
  Løsningen gir sluttbrukeren innsyn i egen dialoghistorikk, status på innsendinger og arkiverte meldinger, inkludert historikk overført fra Altinn II. Innsynet er brukerrettet og gjelder egne eller representerte parters dialoger, ikke innsyn på vegne av offentligheten.

- **Tjenesteutvikling: Gjenbrukbare tjenester**
  Brukergrensesnittet er bygget som en gjenbrukbar flate som kan gjøres tilgjengelig i flere portaler, og kildekoden er publisert under åpen lisens. Virksomheter som trenger en dialogoversikt kan dermed ta i bruk en felles flate framfor å bygge og forvalte sin egen.

## Produktmål
Dokumenterte mål:
- erstatte innboksen og arkivet i Altinn II med en moderne løsning for alle typer sluttbrukere
- gjøre innholdet i Dialogporten tilgjengelig gjennom et felles visuelt brukergrensesnitt
- gjøre grensesnittet gjenbrukbart på tvers av portaler

Utledede mål, basert på milepælsplanen og overgangsløpet:
- gi sluttbrukere tilgang til historikk fra Altinn II etter at den gamle plattformen er avviklet, slik at avviklingen ikke fører til tap av innsyn
- redusere behovet for at hver enkelt virksomhet bygger sin egen dialog- eller meldingsoversikt

## Brukerbehov
- Innbyggere og virksomheter trenger ett sted å se hva det offentlige har sendt dem, hva som venter på handling og hva som er sendt inn tidligere.
- Brukere som opptrer på vegne av flere parter, trenger å kunne skifte mellom aktører uten å miste oversikten.
- Virksomheter trenger tilgang til historiske meldinger og innsendinger etter at Altinn II er avviklet.
- Tjenesteeiere trenger at dialogene de publiserer faktisk blir synlige og handlingsbare for sluttbrukeren, uten å måtte bygge egen brukerflate.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Innbyggere | Se og følge opp meldinger og oppgaver fra det offentlige | Daglig bruk av innboks, varsler og innsyn i egen historikk | Primærbrukere |
| Virksomheter og deres ansatte | Oversikt over oppgaver, frister og korrespondanse på vegne av virksomheten | Oppfølging av pålegg, innsendinger og dialoger | Primærbrukere med høyt volum |
| Brukere som representerer andre | Skifte mellom aktører og se riktig innhold per rolle | Regnskapsførere, fullmektige, verger og andre representanter | Avhenger av rettigheter i Altinn Autorisasjon |
| Tjenesteeiere | At egne dialoger presenteres riktig og blir handlingsbare | Publisering av dialoger via Dialogporten, Altinn Melding og Altinn Apps | Sekundærbrukere; påvirker sluttbrukeropplevelsen indirekte |
| Portal- og sluttbrukersystemleverandører | Vurdere om flaten kan gjenbrukes framfor egen utvikling | Integrasjon og gjenbruk av grensesnitt | Gjenbruksmuligheten er beskrevet i kildene, men ikke hvor mange som faktisk bruker den |

## Hovedfunksjoner
Arbeidsflate presenterer innboksen: en samlet, sorterbar oversikt over dialoger fra offentlige virksomheter, med status, avsender og hva som eventuelt krever handling. Innholdet dekker dialogtjenester, meldinger fra Altinn Melding og skjemaer bygget som Altinn Apps, og suppleres av historikk overført fra Altinn II. Arbeidsflaten viser dialogen med metadata og lenker videre; selve faginnholdet og vedleggene ligger i de underliggende tjenesteplattformene.

Løsningen håndterer også aktørbildet. En bruker som har rettigheter på vegne av en virksomhet eller en annen person, kan skifte mellom aktører og se innholdet den valgte aktøren har tilgang til. Rettighetene kommer fra Altinn Autorisasjon, og arbeidsflaten håndhever dem i presentasjonen framfor å forvalte dem selv. Selve administrasjonen av tilganger skjer i en egen brukerflate for tilgangsstyring, som brukeren når fra arbeidsflaten.

Profil og innstillinger ble reetablert i Altinn 3 som del av arbeidsflaten. Her ligger kontaktopplysninger, varslingsinnstillinger og innstillinger som styrer hvordan brukeren blir varslet om nye dialoger. Varslene sendes av Altinn Varsling, mens arbeidsflaten er stedet brukeren styrer dem fra.

Arkivfunksjonen er den fjerde hoveddelen. Dialoger som er ferdigbehandlet, skal fortsatt kunne finnes igjen, og arbeidsflaten gir tilgang til tidligere innsendinger og meldinger. Dette er en sentral del av begrunnelsen for løsningen: uten den ville avviklingen av Altinn II gitt et brudd i sluttbrukernes tilgang til egen historikk.

### Scope og avgrensning
Inngår:
- innboks med oversikt over dialoger, meldinger og oppgaver på tvers av virksomheter
- aktørvalg og visning tilpasset hvilken part brukeren opptrer på vegne av
- profil, kontaktopplysninger og varslingsinnstillinger for sluttbruker
- tilgang til arkiv og historikk, inkludert innhold overført fra Altinn II
- et gjenbrukbart brukergrensesnitt som kan gjøres tilgjengelig i flere portaler

Inngår ikke:
- lagring av dialogdata, som ligger i Dialogporten og i de underliggende tjenesteplattformene
- utsending og transport av meldinger, som ligger i Altinn Melding, Altinn Formidling og Altinn Varsling
- forvaltning av rettigheter og delegering, som ligger i Altinn Autorisasjon
- innlogging og identitetsverifisering, som ligger i ID-porten
- utforming og kjøring av skjemaer og tjenester, som ligger i Altinn Studio og Altinn Apps
- informasjons- og veiledningsinnholdet på altinn.no

### Typiske brukssituasjoner (generisk)
- En virksomhet skal ha én inngang der ansatte finner alle offentlige henvendelser, uavhengig av hvilken etat de kommer fra.
- En tjenesteeier vil at dialogene den publiserer skal være synlige for sluttbrukeren uten å bygge egen innboks.
- En bruker trenger å finne igjen en tidligere innsending eller melding, også fra tiden før Altinn 3.
- En portaleier vurderer om en eksisterende felles flate kan brukes framfor å utvikle en egen dialogoversikt.

### Når Arbeidsflate normalt ikke er førstevalg
- Når behovet gjelder maskinell tilgang til dialoger i egne fagsystemer. Da er Dialogportens API-er riktig inngang, ikke brukerflaten.
- Når behovet gjelder å sende, transportere eller varsle om meldinger. Da hører løsningen i Altinn Melding, Altinn Formidling eller Altinn Varsling.
- Når behovet gjelder delegering og administrasjon av rettigheter. Da er Altinn Autorisasjon riktig produkt.
- Når brukerflaten må være tett integrert i en fagspesifikk arbeidsprosess med egen saksflyt. Da er en egen fagflate ofte mer treffsikker, eventuelt kombinert med Dialogporten som datakilde.

## Veikart over kommende funksjonalitet
**Fakta:** Digdir publiserer et offentlig veikart for Arbeidsflate på GitHub, og tar imot endringsforslag og feilmeldinger gjennom samme repositorium og gjennom Slack-kanalen for produktet. Åpne saker i repositoriet viser at det arbeides med brukerstyrte merkelapper på dialoger, egne notater på en dialog og bedre navigasjon mellom skjema og innboks.

**Fakta:** Milepælsplanen for Altinn 3 beskriver overgangsløpet fram til avviklingen av Altinn II 19. juni 2026, med gradvis tilgjengeliggjøring av historisk innhold fra Altinn II.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Et samlet, tidfestet veikart for perioden etter avviklingen av Altinn II er ikke funnet som egen publisering. Veikartet i GitHub viser retning og åpne saker, men ikke forpliktende leveransedatoer.

## Forretningsverdi/Verdiforslag
### For innbyggere og virksomheter
Verdien ligger i at all offentlig dialog samles ett sted. Brukeren slipper å holde orden på hvilken etat som bruker hvilken kanal, og får en felles inngang til både nye oppgaver og tidligere korrespondanse. For virksomheter med mange ansatte og mange etatskontakter er dette også en arbeidsbesparelse i den daglige oppfølgingen.

### For tjenesteeiere
Tjenesteeiere får en ferdig sluttbrukerflate uten å bygge den selv. Når en dialog publiseres gjennom Dialogporten, Altinn Melding eller en Altinn App, blir den synlig og handlingsbar i en flate brukerne allerede kjenner. Det senker terskelen for å ta i bruk Altinn 3, og reduserer behovet for egne portalprosjekter.

### For offentlig sektor som helhet
Verdien er redusert dobbeltarbeid og mer enhetlig brukeropplevelse. Én felles flate med åpen kildekode er billigere å forvalte enn mange parallelle innbokser, og gjør det lettere å heve kvalitet, universell utforming og klarspråk ett sted framfor i mange løsninger samtidig. Flaten var også en forutsetning for at avviklingen av Altinn II kunne gjennomføres uten at sluttbrukerne mistet tilgang til egen historikk.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Overgang og historikk | Historisk innhold fra Altinn II gjøres tilgjengelig gradvis, og brukere kan oppleve at noe mangler i en periode | Digdir har publisert statusoppdateringer for innholdsmigreringen i Altinn Studio-dokumentasjonen |
| Avhengighetskjede | Flaten avhenger av Dialogporten, Altinn Autorisasjon og ID-porten samtidig, og feil i ett ledd blir synlig som feil i brukerflaten | Uavklart hvordan feilsituasjoner i underliggende produkter presenteres for sluttbruker |
| Brukeropplevelse | Brukere med lang erfaring fra Altinn II må lære nye mønstre, og den nye flaten dekker ikke nødvendigvis alle innarbeidede arbeidsmåter | Tilbakemeldingskanaler i GitHub og Slack er etablert; omfanget av gjenstående funksjonsgap er ikke offentlig oppsummert |
| Universell utforming | En felles flate for hele offentlig sektor gir stort nedslagsfelt hvis tilgjengelighetsfeil oppstår | Ikke offentlig dokumentert i denne arbeidsøkten om det finnes egen tilgjengelighetserklæring for arbeidsflaten ut over Altinns samlede erklæring |
| Gjenbruk i andre portaler | Gjenbruk av grensesnittet i andre portaler er beskrevet som en mulighet, men bruken er ikke dokumentert med konkrete eksempler | Virksomheter som vurderer gjenbruk, bør avklare forutsetninger direkte med produktmiljøet |
| Leverandør- og teknologibinding | Flaten er tett koblet til Dialogportens datamodell | Åpen kildekode under MIT reduserer bindingen til selve grensesnittet, men ikke avhengigheten av Dialogporten |

## Kanaler
Arbeidsflate leveres som en innlogget webflate. Produksjonsflaten ligger på `af.altinn.no`, og testflaten på `af.tt02.altinn.no`. Innlogging skjer med ID-porten, og hvilket innhold brukeren ser, styres av rettigheter i Altinn Autorisasjon.

Det finnes ingen egen maskinell kanal for Arbeidsflate. Maskinell tilgang til det samme innholdet går gjennom Dialogportens API-er og GraphQL-grensesnitt. Kanalbildet for produktet er dermed rent brukerrettet, mens integrasjonsflaten hører til Dialogporten.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** Driftsmodell og kjøremiljø for Arbeidsflate er ikke beskrevet i de kontrollerte kildene. Det som er kjent, er at løsningen er en webapplikasjon utviklet i `Altinn/dialogporten-frontend` med Node.js, TypeScript og containerbasert lokalt utviklingsoppsett, og at den leveres som del av Altinn 3. Skyleverandør og driftsarkitektur er ikke utledet her.

## Gjenbruk
Arbeidsflate er gjenbrukbar på to nivåer. Som tjeneste kan flaten gjøres tilgjengelig i ulike portaler, slik at flere aktører kan bruke samme dialogoversikt framfor å bygge hver sin. Som kode er hele grensesnittet publisert under en tillatende lisens, slik at virksomheter kan studere, gjenbruke eller bygge videre på løsningen.

Den praktiske forutsetningen for begge formene for gjenbruk er tilgang til Dialogporten. Arbeidsflate uten Dialogporten har ikke noe innhold å vise, og gjenbruk bør derfor vurderes som gjenbruk av et par, ikke av en enkeltkomponent.

### Vanlige kombinasjoner med andre produkter
- **Dialogporten** leverer dialogene som arbeidsflaten viser. Dette er den bærende avhengigheten.
- **ID-porten** leverer innlogging og identitetsverifisering for sluttbrukeren.
- **Altinn Autorisasjon** leverer rettigheter, aktørvalg og representasjon, og avgjør hva den enkelte brukeren faktisk får se.
- **Altinn Varsling** sender varslene som gjør at brukeren oppdager nye dialoger; varslingsinnstillingene styres fra arbeidsflaten.
- **Altinn Melding og Altinn Apps** produserer mye av innholdet som havner i innboksen.
- **Felles designsystem** leverer komponenter og mønstre for brukergrensesnittet.
- **altinn.no** dekker informasjon, veiledning og tjenesteoversikt rundt flaten, mens Arbeidsflate dekker den innloggede dialogen.

**Kildekode:** Åpen kildekode

**Lisens:** MIT

**Repositorium:** https://github.com/Altinn/dialogporten-frontend

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov**
  Løsningen er organisert rundt brukerens samlede dialogbilde framfor rundt avsendervirksomhetenes inndeling, og samler det brukeren må følge opp på ett sted.

- **P5: Del og gjenbruk løsninger**
  Én felles brukerflate med åpen kildekode erstatter behovet for at hver virksomhet bygger sin egen dialogoversikt.

- **P6: Lag digitale løsninger som støtter samhandling**
  Flaten viser dialoger fra flere tjenesteplattformer i samme representasjon, og gjør samhandlingen synlig for sluttbrukeren.

- **P7: Sørg for tillit til oppgaveløsningen**
  Støttes delvis. Brukeren får innsyn i egen historikk og status, men tilliten hviler på at underliggende produkter håndterer autentisering og autorisasjon riktig. Arbeidsflate er presentasjonslaget, ikke kontrollpunktet.

Spenninger og begrensninger: den sterkeste spenningen går mot **P2: Ta arkitekturbeslutninger på rett nivå**. En felles nasjonal brukerflate flytter beslutninger om brukeropplevelse bort fra den enkelte virksomheten, og virksomheter med fagspesifikke arbeidsprosesser kan oppleve at flaten ikke treffer deres behov. Gevinsten i gjenbruk betales med mindre lokalt handlingsrom. I tillegg gjør konsentrasjonen at feil i én flate får konsekvenser for svært mange brukere samtidig, noe som stiller høyere krav til tilgjengelighet og kvalitetssikring enn en lokal løsning ville gjort.

## Finansiering
**Ikke offentlig dokumentert i denne arbeidsøkten:** Det er ikke funnet en egen, publisert finansieringsmodell for Arbeidsflate som eget produkt. Løsningen inngår i Digdirs portefølje av fellesløsninger, som forvaltes under Styringsrådet for Digitaliseringsdirektoratets fellesløsninger.

**Fakta:** Digdir har et pågående arbeid med ny finansieringsmodell for fellesløsningene. Utfallet kan påvirke hvordan Arbeidsflate finansieres framover.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir, som eget produkt i produktgruppen `Portalar og brukaroppleving` | Samarbeidsportalens produktside for Arbeidsflate og produktgruppesiden for portaler og brukeropplevelse |
| Driftsansvar | Digdir, som del av Altinn 3 | Produksjonsflaten leveres på `af.altinn.no` som del av Altinn |
| Budsjettansvar | Ikke offentlig dokumentert i denne arbeidsøkten | Ingen egen budsjettoppføring for Arbeidsflate funnet i kontrollerte kilder |
| Styringsmodell | Styringsrådet for Digitaliseringsdirektoratets fellesløsninger er styringsarena for Digdirs fellesløsninger. Produktutviklingen styres i Altinn-porteføljen med offentlig veikart og åpne tilbakemeldingskanaler | Samarbeidsportalens sider om styringsrådet og om produktet |

## Lenke til dokumentasjon
- Produktside: https://samarbeid.digdir.no/altinn/arbeidsflate/2350
- Produktgruppe portaler og brukeropplevelse: https://samarbeid.digdir.no/altinn/portalar-og-brukaroppleving/2485
- Milepælsplan for Altinn: https://samarbeid.digdir.no/altinn/milepaelsplan/2392
- Produksjonsflate: https://af.altinn.no/
- Kildekode og veikart: https://github.com/Altinn/dialogporten-frontend
- Dialogporten-dokumentasjon: https://docs.altinn.studio/nb/dialogporten/

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-09-17
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-17
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-17
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-09-17
- https://samarbeid.digdir.no/altinn/arbeidsflate/2350, kontrollert 2026-09-17
- https://samarbeid.digdir.no/altinn/portalar-og-brukaroppleving/2485, kontrollert 2026-09-17
- https://samarbeid.digdir.no/altinn/milepaelsplan/2392, kontrollert 2026-09-17
- https://samarbeid.digdir.no/felleslosninger/felleslosninger/1309, kontrollert 2026-09-17
- https://samarbeid.digdir.no/felleslosninger/altinn-3-naermer-seg-full-overgang-dette-skjer-i-2026/3500, kontrollert 2026-09-17
- https://github.com/Altinn/dialogporten-frontend, kontrollert 2026-09-17
- https://af.altinn.no/, kontrollert 2026-09-17
