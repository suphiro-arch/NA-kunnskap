# Fellestjenester BYGG

## Navn
Fellestjenester BYGG – Direktoratet for byggkvalitets felles digitale tjenester for byggesøknader, del av Fellestjenester plan og bygg

## Ressurs ID
DIBK-001

## Status/Livsfase
**Produksjon** – tjenestene for byggesøknader har vært i bruk siden 2018, og dokumentasjonen for leverandørene er lagt om til Altinn 3.

**Fakta:** Direktoratet for byggkvalitet (DiBK) startet utviklingen våren 2017, og de første nettbaserte søknadsløsningene kom høsten 2018 (dibk.no, Dette er Fellestjenester bygg). Dokumentasjonen for tjenesteleverandører har egne sider for Altinn 3, mens sidene for søknadstjenestene i Altinn II er merket for arkivering (dibk.atlassian.net, Informasjon om tjenester, oppdatert 06.10.2026).

**Deduksjon:** Søknadstjenestene er i hovedsak flyttet fra Altinn II til Altinn 3. Hvilke enkelttjenester som eventuelt gjenstår, er ikke offentlig dokumentert i denne arbeidsøkten.

## Modenhet
**Høy organisatorisk modenhet og etablert bruk, med et smalt leverandørmarked og sterk avhengighet av andre fellesløsninger.**

- Plattformen har vært i drift siden 2018 og er forankret i DiBKs strategi ByggNett, som ble etablert i 2014 (dibk.no, ByggNett).
- Fem søknadssystemer for byggesak tilbys i dag på grunnlag av Fellestjenester bygg, i tillegg til to løsninger for varsel om oppstart av planarbeid (dibk.no, Tjenester for proffbrukere; dibk.no, Fellestjenester plan og bygg).
- Utviklere må ha tjenestekonsesjon fra DiBK. Sytten firmaer og interesseorganisasjoner fikk konsesjon etter utlysningen høsten 2016, og DiBK har ikke planer om ny utlysning (dibk.no, Dette er Fellestjenester bygg).
- Tjenesteleverandørene har en egen dokumentasjonsside med veiledere for søknadssystemer og for kommunenes mottakssystemer, testmiljø og driftsvarsler (dibk.atlassian.net, Fellestjenester BYGG).
- Kommunene kan ta imot søknadene på tre måter, fra strukturert import i saksbehandlingssystemet til manuell henting i Altinn (dibk.no, Gjør kommunen din klar for digitale byggesøknader).

**Deduksjon:** Det svakeste leddet er tilgangen til markedet. Siden ingen nye konsesjoner lyses ut, er det de eksisterende konsesjonshaverne som avgjør hvilke søknadsløsninger som finnes. Gevinsten i kommunen avhenger dessuten av om kommunen har et saksbehandlingssystem som kan ta imot strukturerte data.

## Kort beskrivelse
Fellestjenester BYGG er DiBKs tjenesteplattform på Altinn for digitale byggesøknader. Plattformen er ikke en søknadsløsning for sluttbrukeren selv, men et sett felles tjenester som kommersielle søknadssystemer bygger på. Den kontrollerer byggesøknaden automatisk mot regelverket før innsending, sender den til riktig kommune, og legger til rette for dialog mellom søker og kommune under behandlingen. Søknadene kommer til kommunen i et felles format og utseende, uansett hvilket søknadssystem søkeren har brukt.

Plattformen omfatter også signering av erklæringer om ansvarsrett, samsvar og kontroll i Altinn, digitalt nabovarsel og nasjonale sjekklister for byggesak. Søknadene leveres til kommunen gjennom KS Fiks, enten direkte til kommunens saksbehandlingssystem eller til arkiv, eller til kommunens innboks i Altinn.

Fellestjenester BYGG er den ene delen av Fellestjenester plan og bygg. Den andre delen, Fellestjenester plan, gjelder varsel om oppstart av planarbeid og innsending av reguleringsplanforslag, og inngår ikke i denne ressursen.

## Kapabiliteter
Fellestjenester BYGG realiserer den felles kontrollen og formidlingen av byggesøknader mellom søknadssystemene og kommunene. Innlogging, tilgangsstyring og transport til kommunen leveres av Altinn, ID-porten og KS Fiks.

- **Datautveksling og integrasjon: Meldingsutveksling** Fellestjenester BYGG sender byggesøknaden som maskinlesbar XML og en utskriftsvennlig versjon til riktig kommune, i et felles format med fastsatte dokumenttyper og navnemønster for vedlegg, uansett hvilket søknadssystem som er brukt.
- **Tjenesteutvikling: Gjenbrukbare tjenester** Fellestjenester BYGG gir alle konsesjonshavere de samme tjenestene for automatisk kontroll av søknaden mot regelverket, innsending, signering av erklæringer og nabovarsel, slik at forretningsreglene for byggesøknader ikke må bygges i hvert søknadssystem.

## Produktmål
**Fakta:** Fellestjenester plan og bygg skal gjøre det enklere å sende inn riktige og komplette planforslag og byggesøknader, og gjøre det mulig for kommunene å behandle dem raskere (dibk.no, Fellestjenester plan og bygg – enklere og smartere planforslag og byggesøknader).

**Fakta:** Målet for ByggNett er å gjøre byggesaksprosessen enklere, mer effektiv og forutsigbar. DiBK skal være pådriver og tilrettelegger, mens markedet leverer løsningene. Ett av tiltakene er å bygge digital infrastruktur på statlige fellesløsninger som støtter informasjonsflyt og regelsjekk (dibk.no, ByggNett).

**Deduksjon:** Det operative målet er at kommunen mottar komplette, kontrollerte og strukturerte søknader, slik at saksbehandlingen kan starte uten manuell registrering og uten runder med mangelbrev.

## Brukerbehov
Søkere, både profesjonelle og privatpersoner, trenger å vite at søknaden er komplett og i tråd med regelverket før den sendes, og å slippe å finne ut hvilken kommune eller hvilket kontor som skal ha den.

Kommunene trenger søknader i et forutsigbart og maskinlesbart format, slik at de kan importeres i saksbehandlingssystemet og behandles likt uavhengig av hvem som har laget søknadsløsningen.

Leverandører av søknadssystemer trenger felles tjenester for kontroll, innsending og signering, slik at de kan konkurrere på brukeropplevelse uten å bygge regelverket og kommunekoblingene selv.

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Leverandører av søknadssystemer (konsesjonshavere) | Kontroll, innsending, signering og status for søknader | Kommersielle søknadsløsninger for byggesak | Krever tjenestekonsesjon fra DiBK |
| Profesjonelle søkere | Sende komplette søknader og håndtere erklæringer | Rammetillatelse, igangsettingstillatelse, ferdigattest m.m. | Bruker søknadssystemer som Byggesøknaden.no, eByggesøk, EG Byggsøk, MAKS-søk og Sinec Byggsøk |
| Privatpersoner | Enkle søknader og nabovarsel | Bruksendring av rom og nabovarsel | Egen oversikt på dibk.no |
| Ansvarlige foretak | Signere erklæringer om ansvarsrett, samsvar og kontroll | Byggeprosjekter med ansvarsrett | Eneste tjenestene som krever innlogging i Altinn |
| Naboer | Motta og svare på nabovarsel | Nabovarsling i byggesaker | Svar på nabovarsel kan komme i Altinn-innboksen |
| Kommunene | Motta søknader i felles format | Byggesaksbehandling | Mottak gjennom eByggesak, SvarInn eller Altinn-innboksen |
| Leverandører av kommunale saksbehandlingssystemer | Importere søknader strukturert | eByggesak-systemer | Egen veileder for mottaksleverandører |
| DiBK | Forvaltning og videreutvikling | Nasjonal fellestjeneste for byggesak | Kontakt for tjenesteleverandører og kommuner |

## Hovedfunksjoner
Den første hovedfunksjonen er **automatisk kontroll av søknaden før innsending**. Søknadssystemet sender søknaden til Fellestjenester BYGG, som kontrollerer den mot regelverket før den går til kommunen. Kontrollen bygger på felles valideringsregler og de nasjonale sjekklistene for byggesak, som skal sikre lik og riktig saksbehandling og hjelpe både søker og saksbehandler. Sjekklistene er publisert åpent på ftb-checklist.dibk.no.

Den andre er **innsending og videreformidling til riktig kommune**. Fellestjenester BYGG sender søknaden til kommunen gjennom KS Fiks. Hver forsendelse inneholder hele søknaden som maskinlesbar XML og som utskriftsvennlig versjon, med vedlegg etter et fast navnemønster, og forsendelsen signeres i Altinn. Kommunen tar imot på én av tre måter: med strukturert import i et saksbehandlingssystem som støtter eByggesak, gjennom SvarInn i KS Fiks, eller i kommunens innboks i Altinn. Søknaden når riktig mottaker bare når kommunens organisasjonsnummer er registrert både i Fellestjenester BYGG og i KS Fiks.

Den tredje er **signering, nabovarsel og erklæringer**. Ansvarlige foretak signerer erklæringer om ansvarsrett, samsvar og kontroll i Altinn, og dette er de eneste tjenestene som krever innlogging i Altinn. Søknadssystemene tilbyr digitalt nabovarsel, og svar på nabovarsel er blant meldingene som kan komme i Altinn-innboksen. Søknadssystemene dekker blant annet rammetillatelse, igangsettingstillatelse, tillatelse i ett trinn, tiltak uten ansvarsrett, automatisk samtykke fra Arbeidstilsynet, midlertidig brukstillatelse, endring av tillatelse og ferdigattest.

Den fjerde er **API-er og grunnlag for leverandørene**. Dokumentasjonen for tjenesteleverandører omfatter API-er for status, validering og kommuner, hendelser, datamodeller i XML-skjema og et testmiljø der testsøknader går gjennom testmiljøet til KS Fiks. Tjenesten GeoLett skal gi søkerne grunndata av god kvalitet, som DiBK beskriver som en forutsetning for selvbetjente byggesøknader.

### Typiske brukssituasjoner (generisk)
- en leverandør bygger en søknadsløsning for byggesak og bruker de felles tjenestene for kontroll, innsending og signering
- et ansvarlig foretak sender søknad om rammetillatelse og samler inn erklæringer om ansvarsrett digitalt
- en kommune setter opp saksbehandlingssystemet til å importere byggesøknader strukturert
- en privatperson sender digitalt nabovarsel eller søknad om bruksendring av rom

### Når Fellestjenester BYGG normalt ikke er førstevalg
Fellestjenester BYGG er ikke en søknadsløsning som sluttbrukeren bruker direkte. Den profesjonelle søkeren må bruke et av søknadssystemene som bygger på plattformen.

Den er heller ikke en generell kanal for å sende dokumenter til kommunen. Til generell digital post til kommunen brukes `KS-003` Fiks SvarUt, og til mottak av inngående post i kommunen `KS-007` SvarInn, som Fellestjenester BYGG selv bruker for å levere søknadene.

For opplysninger om eiendom, adresse og bygning er `KART-001` Matrikkelen kilden, og for geografiske plandata og kartgrunnlag er `KART-002` Geonorge rett inngang.

### Scope og avgrensning
Inngår:
- automatisk kontroll av byggesøknader mot regelverket før innsending
- innsending og videreformidling av byggesøknader til riktig kommune i felles format
- signering av erklæringer om ansvarsrett, samsvar og kontroll i Altinn
- tjenester for digitalt nabovarsel
- nasjonale sjekklister for byggesak
- API-er, datamodeller, veiledere og testmiljø for leverandører av søknadssystemer og mottakssystemer

Inngår ikke:
- de kommersielle søknadssystemene, som eies og driftes av leverandørene
- kommunenes saksbehandlingssystemer og selve saksbehandlingen
- Fellestjenester plan, med planvarsel og innsending av reguleringsplanforslag
- KS Fiks og Altinn, som Fellestjenester BYGG bruker til transport, innboks og signering

## Veikart over kommende funksjonalitet
**Fakta:** Innenfor Fellestjenester plan og bygg har DiBK utviklet en tjeneste for innsending av reguleringsplanforslag til kommunen, som er varslet som kommende (dibk.no, Fellestjenester plan og bygg). DiBK overtar ansvaret for nasjonal deling av plandata fra 1. januar 2026 (dibk.no, Digitalisering av plan- og byggesak). Fremtidige satsingsområder i ByggNett er relasjonsbygging, kompetansebygging, regelverksutvikling og tjenesteutvikling (dibk.no, ByggNett).

**Ikke offentlig dokumentert i denne arbeidsøkten:** Konkrete planer for nye søknadstyper eller funksjoner i Fellestjenester BYGG.

## Forretningsverdi/Verdiforslag
For søkerne ligger verdien i at søknaden kontrolleres før den sendes, går automatisk til riktig kommune, og at erklæringer og nabovarsel kan håndteres digitalt.

For kommunene ligger verdien i at søknadene kommer i samme format uansett søknadssystem, og at de kan importeres strukturert i saksbehandlingssystemet. DiBK oppfordrer kommunene til å slutte å ta imot søknader på e-post og kreve digital innsending, med effektivisering og bedre datakvalitet som begrunnelse.

For leverandørene ligger verdien i at regelverkskontroll, kommunekoblinger og signering er felles, slik at de kan konkurrere på søknadsløsningen.

For samfunnet ligger verdien i likere og raskere saksbehandling på tvers av kommunene, og i maskinlesbare data som kan brukes direkte i digitale verktøy.

## Utfordringer og risiko

| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Marked | Lukket konsesjonsordning begrenser hvem som kan tilby søknadsløsninger | DiBK har ikke planer om ny utlysning av konsesjoner |
| Teknisk | Avhengighet av Altinn, ID-porten og KS Fiks | Driftsvarsler publiseres på dokumentasjonssiden, også ved feil i Altinn 3 og ID-porten |
| Mottak i kommunen | Feil organisasjonsnummer gjør at søknaden havner feil | Organisasjonsnummeret må stemme i Fellestjenester BYGG og KS Fiks; feil meldes til DiBK |
| Gevinstrealisering | Kommuner uten eByggesak-system må laste opp søknaden manuelt | Strukturert import krever saksbehandlingssystem med støtte for eByggesak |
| Personvern | Søknader kan inneholde opplysninger som skal unntas offentlighet | Leverandørdokumentasjonen har egen veiledning for søknader som ønskes unntatt offentlighet |
| Overgang | Migrering fra Altinn II til Altinn 3 krever endringer hos leverandørene | Egen veiledning for Altinn 3; Altinn II-sidene er merket for arkivering |

## Kanaler
**Søknadssystemer:** Profesjonelle søkere og privatpersoner bruker kommersielle søknadssystemer som bygger på Fellestjenester BYGG. Plattformen har ingen egen brukerflate for søknader.

**Altinn:** Signering av erklæringer om ansvarsrett, samsvar og kontroll krever innlogging i Altinn. Svar på nabovarsel og søknader til kommuner uten annet mottak kommer i Altinn-innboksen.

**Maskinelle kanaler:** API-er for status, validering og kommuner, med egen autentisering, og levering til kommunene gjennom KS Fiks.

**Åpne nettjenester:** Nasjonale sjekklister for byggesak på ftb-checklist.dibk.no.

## Plattform
**Fakta:** Fellestjenester BYGG er etablert som tjenesteplattform på Altinn, og leverandørdokumentasjonen beskriver tjenestene i Altinn 3 (dibk.no, Dette er Fellestjenester bygg; dibk.atlassian.net, Informasjon om tjenester).

**Ikke offentlig dokumentert i denne arbeidsøkten:** Driftsmodell og plattform for DiBKs egne komponenter utenfor Altinn, som valideringstjenesten og API-ene.

## Gjenbruk
Plattformen er laget for gjenbruk: mange søknadssystemer bruker de samme tjenestene, og alle kommuner mottar søknader i samme format. Gjenbruket på leverandørsiden er avgrenset til konsesjonshaverne. Datamodellene i XML-skjema, de nasjonale sjekklistene og veilederne for søknads- og mottakssystemer er publisert åpent.

### Vanlige kombinasjoner med andre produkter
- `KS-007` SvarInn og `KS-001` Fiks-plattformen, for levering av søknadene til kommunens saksbehandlingssystem eller arkiv.
- `DIGDIR-017` Altinn 3 plattform, som tjenestene kjører på, og `DIGDIR-004` Altinn Autorisasjon for rettigheter til å signere og se innboksen.
- `KART-001` Matrikkelen, for eiendoms-, adresse- og bygningsopplysninger i byggesøknaden.

**Kildekode:** Ikke offentlig dokumentert. Kildekoden for Fellestjenester BYGG er ikke funnet publisert.

**Lisens:** Ikke offentlig dokumentert.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger**
  Kontroll, innsending og signering er bygget én gang og brukes av alle søknadssystemene, og plattformen bygger selv på Altinn og KS Fiks.

- **P6: Lag digitale løsninger som støtter samhandling**
  Søknadene flyter strukturert fra søker via søknadssystem til kommunens saksbehandlingssystem, og plattformen legger til rette for dialog mellom søker og kommune.

- **P3: Bidra til digitaliseringsvennlige regelverk**
  Støttes delvis. DiBK beskriver plattformen som en digital regelverksplattform, der regelverket for byggesak er omsatt til automatisk kontroll og nasjonale sjekklister.

- **P1: Ta utgangspunkt i brukernes behov**
  Støttes delvis. Søkeren får kontroll før innsending og slipper å finne riktig kommune, men brukeropplevelsen avhenger av søknadssystemet søkeren velger.

Spenningen ligger i markedsmodellen. DiBK lar markedet levere søknadsløsningene, men konsesjonsordningen er lukket, og det er færre søknadssystemer i dag enn det var konsesjonshavere. Gevinsten i kommunen er ujevn, fordi kommuner uten eByggesak-system må håndtere søknadene manuelt. Plattformen er tett koblet til Altinn og KS Fiks, slik at feil der stopper innsendingen.

## Finansiering
**Ikke offentlig dokumentert i denne arbeidsøkten:** Hvordan utvikling og drift av Fellestjenester BYGG finansieres, og om konsesjonshaverne eller kommunene betaler for bruk.

## Forvaltning/eier

| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Direktoratet for byggkvalitet | dibk.no, Dette er Fellestjenester bygg |
| Driftsansvar | Ikke offentlig dokumentert i denne arbeidsøkten; driftsvarsler publiseres av DiBK | dibk.atlassian.net, Driftsvarsler og utviklingsstatus |
| Søknadssystemer | Konsesjonshaverne, som utvikler og drifter de kommersielle søknadsløsningene | dibk.no, Tjenester for proffbrukere |
| Mottak i kommunen | Kommunene og leverandørene av saksbehandlingssystemer; levering gjennom KS Fiks | dibk.no, Gjør kommunen din klar for digitale byggesøknader |
| Budsjettansvar | Ikke offentlig dokumentert i denne arbeidsøkten | – |
| Styringsmodell | DiBK styrer tilgangen gjennom tjenestekonsesjon, og plattformen inngår i DiBKs strategi ByggNett | dibk.no, Dette er Fellestjenester bygg; dibk.no, ByggNett |

## Lenke til dokumentasjon
- Fellestjenester plan og bygg: https://www.dibk.no/verktoy-og-veivisere/andre-fagomrader/fellestjenester-bygg
- Dette er Fellestjenester bygg: https://www.dibk.no/verktoy-og-veivisere/andre-fagomrader/fellestjenester-bygg/dette-er-fellestjenester-bygg
- Dokumentasjon for tjenesteleverandører: https://dibk.atlassian.net/wiki/spaces/FB/overview
- Veileder for utviklere av søknadssystemer: https://dibk.atlassian.net/wiki/spaces/FB/pages/732725253/Veileder+for+utviklere+av+s+knadssystemer
- Veileder for utviklere av eByggesakssystemer: https://dibk.atlassian.net/wiki/spaces/FB/pages/38043659/Veileder+for+utviklere+av+eByggesakssystemer+mottaksleverand+rer
- Gjør kommunen din klar for digitale byggesøknader: https://www.dibk.no/saksbehandling-tilsyn-og-kontroll/gjor-kommunen-din-klar-for-digitale-byggesoknader
- Nasjonale sjekklister for byggesak: https://ftb-checklist.dibk.no/

## Kildegrunnlag brukt i utfyllingen
Hentet 2026-10-25:
- DiBK, Fellestjenester plan og bygg: https://www.dibk.no/verktoy-og-veivisere/andre-fagomrader/fellestjenester-bygg
- DiBK, Dette er Fellestjenester bygg: https://www.dibk.no/verktoy-og-veivisere/andre-fagomrader/fellestjenester-bygg/dette-er-fellestjenester-bygg
- DiBK, Tjenester for proffbrukere: https://www.dibk.no/verktoy-og-veivisere/andre-fagomrader/fellestjenester-bygg/tjenestene/tjenester-for-proffbrukere
- DiBK, Tips til organisasjoner om bruk av Altinn i byggesøknadsprosessen: https://www.dibk.no/verktoy-og-veivisere/andre-fagomrader/fellestjenester-bygg/tips-til-organisasjoner-om-bruk-av-altinn-i-byggesoknadsprosessen
- DiBK, Fellestjenester plan og bygg – enklere og smartere planforslag og byggesøknader: https://www.dibk.no/saksbehandling-tilsyn-og-kontroll/digitalisering-av-byggesak/fellestjenester-plan-og-bygg--enklere-og-smartere-planforslag-og-byggesoknader
- DiBK, Digitalisering av plan- og byggesak: https://www.dibk.no/saksbehandling-tilsyn-og-kontroll/digitalisering-av-byggesak
- DiBK, ByggNett – strategien for en digital byggsektor: https://www.dibk.no/saksbehandling-tilsyn-og-kontroll/digitalisering-av-byggesak/byggnett--strategien-for-en-digital-byggsektor
- DiBK, Gjør kommunen din klar for digitale byggesøknader: https://www.dibk.no/saksbehandling-tilsyn-og-kontroll/gjor-kommunen-din-klar-for-digitale-byggesoknader
- DiBK, Har kommunen mottatt en digital byggesøknad?: https://www.dibk.no/saksbehandling-tilsyn-og-kontroll/har-kommunen-mottatt-en-digital-byggesoknad
- DiBK, Fellestjenester BYGG – dokumentasjon for tjenesteleverandører: https://dibk.atlassian.net/wiki/spaces/FB/overview
- DiBK, Informasjon om tjenester (Altinn 3): https://dibk.atlassian.net/wiki/spaces/FB/pages/2827649025/Informasjon+om+tjenester
- DiBK, Veileder for utviklere av søknadssystemer: https://dibk.atlassian.net/wiki/spaces/FB/pages/732725253/Veileder+for+utviklere+av+s+knadssystemer
- DiBK, API-er på Fellestjenester BYGG: https://dibk.atlassian.net/wiki/spaces/FB/pages/2733375625/API-er+p+Fellestjenester+BYGG
- DiBK, Veileder for utviklere av eByggesakssystemer (mottaksleverandører): https://dibk.atlassian.net/wiki/spaces/FB/pages/38043659/Veileder+for+utviklere+av+eByggesakssystemer+mottaksleverand+rer
- DiBK, Nasjonale sjekklister for byggesak: https://ftb-checklist.dibk.no/
