# Digital sykmelding

## Navn
Digital sykmelding – Navs løsning for elektronisk innsending, behandling og videreformidling av sykmeldinger og tilhørende dialogmeldinger

## Ressurs ID
NAV-003

## Status/Livsfase
**Produksjon** – digital sykmelding fra journalsystemene til Nav og videre til den sykmeldte og arbeidsgiveren er i drift, samtidig som Nav utvikler en ny sykmeldingsløsning.

**Fakta:** De fleste allmennleger plikter å sende sykmeldingen elektronisk til Nav, og sykmeldingen kommer i de fleste tilfeller digitalt til pasienten (nav.no, Om sykmeldingen). Nav oppgir at det utvikles en ny sykmelding og endret adressering for dialogmeldinger, og at deler av den tekniske informasjonen derfor er utdatert (nav.no, Digital sykmelding og dialogmeldinger – tekniske spesifikasjoner). Kildekoden til den nye innsendingsløsningen for behandlere er publisert og i aktiv utvikling (github.com/navikt/syk-inn).

## Modenhet
**Høy teknisk og organisatorisk modenhet for dagens meldingsflyt, med en overgangsfase mot ny løsning.**

- Meldingsformatet er fastsatt i XML-skjemaet Sykmelding 2013 v1.4, med informasjonsmodell, meldingsbeskrivelse og en egen Nav-standard og veiledning for sykmelding og dialogmeldinger (nav.no, tekniske spesifikasjoner; github.com/navikt/Sykmelding_v1.4).
- Plikten til elektronisk innsending er forankret i forskrift om elektronisk kommunikasjon med Nav, med en egen forskrift om unntak (nav.no, Om sykmeldingen; Lovdata, forskrift 2009-10-02-1285 og 2009-12-07-1480).
- Mottaket kontrollerer sykmeldingen automatisk, og en sykmelding som ikke er riktig utfylt, blir avvist uten at Nav kan overprøve avvisningen manuelt (nav.no, Om sykmeldingen).
- Arbeidsgiverens tilgang styres gjennom egne Altinn-rettigheter og tilgangspakker (nav.no, Tilganger for arbeidsgivere).
- Papir er fortsatt en reserveløsning for pasienter uten innlogging på høyeste sikkerhetsnivå, for sykehus som skriver på papir, og for pasienter som har reservert seg mot digital kommunikasjon (nav.no, Om sykmeldingen).

**Deduksjon:** Det svakeste leddet er overgangen mellom dagens meldingsbaserte løsning og den nye løsningen. Nav varsler at deler av spesifikasjonene er utdatert, men har ikke publisert en tidsplan for når den nye løsningen tar over. Leverandører av journalsystemer som skal utvikle nå, må derfor avklare med Nav hvilken løsning de skal bygge mot.

## Kort beskrivelse
Digital sykmelding er Navs løsning for at sykmeldingen går digitalt fra den som sykmelder til Nav, til den sykmeldte og til arbeidsgiveren. Legen eller annen behandler fyller ut sykmeldingen i journalsystemet (EPJ), som sender den som en signert og kryptert melding til Nav. Nav kontrollerer sykmeldingen automatisk og gjør den tilgjengelig for den sykmeldte i tjenesten Ditt sykefravær på nav.no. Derfra sender den sykmeldte sykmeldingen videre til arbeidsgiveren, som mottar den i Altinn uten diagnose og sykdomshistorie. Den nærmeste lederen følger opp den sykmeldte gjennom Dine sykmeldte på nav.no.

Til løsningen hører også dialogmeldinger mellom Nav og behandleren om sykefraværsoppfølging, som legger seg direkte i journalsystemet, og formidling av arbeidsgiverens oppfølgingsplan til fastlegen, der Nav bare er teknisk videreformidler.

Digital sykmelding er ikke selve sykepengeordningen. Søknad om sykepenger, inntektsmelding og vedtak om sykepenger er egne tjenester i Nav som bygger på sykmeldingen.

## Kapabiliteter
Digital sykmelding realiserer meldingsflyten og den samlede brukerreisen fra behandler via Nav til arbeidsgiver. Innloggingen og transportinfrastrukturen leveres av andre ressurser.

- **Datautveksling og integrasjon: Meldingsutveksling** Nav har fastsatt meldingsformatet for sykmelding og dialogmeldinger, med XML-skjema, informasjonsmodell, krav til signering og kryptering og en avvisningsmekanisme der behandleren får melding i journalsystemet når sykmeldingen ikke kan tas imot.
- **Sluttbrukertjenester: Sammenhengende tjenester** Sykmeldingen følger den sykmeldte fra behandleren via Nav til arbeidsgiveren uten at den sykmeldte må bære papirkopier mellom aktørene, og arbeidsgiveren mottar en versjon uten medisinske opplysninger.

## Produktmål
**Fakta:** Sykmeldingen skal sendes elektronisk til Nav, og de fleste allmennleger har plikt til det (nav.no, Om sykmeldingen; Lovdata, forskrift om elektronisk kommunikasjon med Nav). Sykmeldingen bør sendes til arbeidsgiveren første dag i fraværet, slik at oppfølgingen kan starte (nav.no, Sykmelding).

**Fakta:** Arbeidsgiveren har ikke rett til å få vite sykdomshistorien eller diagnosen til den sykmeldte (nav.no, Sykmelding). Løsningen skiller derfor mellom det Nav og behandleren ser, og det arbeidsgiveren får.

**Deduksjon:** Det operative målet er at sykmeldingen skal være komplett og kontrollert når den kommer inn, slik at sykefraværsoppfølgingen og sykepengebehandlingen kan starte uten manuell registrering hos Nav og uten papirflyt til arbeidsgiveren.

## Brukerbehov
Den som sykmelder, trenger å sende sykmeldingen fra journalsystemet uten dobbeltregistrering, og å få beskjed med en gang hvis den ikke kan tas imot. Behandleren trenger også en trygg kanal for dialog med Nav om pasientens sykefravær.

Den sykmeldte trenger å få sykmeldingen digitalt og å kunne sende den til arbeidsgiveren uten at diagnosen følger med.

Arbeidsgiveren trenger å få sykmeldingen raskt og strukturert for å kunne følge opp den ansatte, og å kunne styre hvem i virksomheten som får tilgang.

Nav trenger sykmeldingene som strukturerte data for å følge opp sykefraværet og behandle krav om sykepenger.

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Leger og andre behandlere som sykmelder | Sende sykmelding fra journalsystemet, få avvisningsmelding, dialog med Nav | Fastlegekontor, legevakt, spesialisthelsetjeneste | De fleste allmennleger har plikt til elektronisk innsending |
| Leverandører av journalsystemer (EPJ) | Spesifikasjoner, skjema, testfiler | Utvikling av kommunikasjonsløsning mot Nav | Nye leverandører skal kontakte Nav før utvikling |
| Sykmeldte arbeidstakere, frilansere og selvstendige | Motta sykmeldingen og sende den videre | Ditt sykefravær på nav.no | Krever innlogging på høyeste sikkerhetsnivå; ellers papir |
| Arbeidsgivere, HR og lønn | Motta sykmelding og sykepengesøknad | Altinn-innboksen for underenheten | Krever rettighetene Sykmelding til arbeidsgiver og Dialog for sykepenger, eller tilgangspakken Lønn med personopplysninger av særlig kategori |
| Nærmeste leder | Følge opp den sykmeldte | Dine sykmeldte på nav.no | Registreres av arbeidsgiveren; varsles på e-post |
| Nav | Strukturerte sykmeldinger og dialog med behandler | Sykefraværsoppfølging og sykepengebehandling | Forvalter løsningen og spesifikasjonene |

## Hovedfunksjoner
Den første hovedfunksjonen er **innsending fra journalsystemet**. Behandleren fyller ut sykmeldingen i sitt journalsystem, som sender den til Nav som en strukturert melding etter skjemaet Sykmelding 2013 v1.4. Behandleren må ha en PKI-løsning som gir elektronisk signatur og kryptering, og programvare for kommunikasjon og sikkerhet fra journalleverandøren. Transporten bygger på ebXML med CPP/CPA-avtaler, og hodemelding og vedlegg følger standarder fra Direktoratet for e-helse. Nav utvikler i tillegg en ny innsendingsløsning som kan startes fra journalsystemet som en SMART on FHIR-applikasjon eller brukes direkte med innlogging gjennom HelseID.

Den andre er **automatisk kontroll og avvisning**. Nav kontrollerer sykmeldingen automatisk ved mottak. En sykmelding som ikke er riktig fylt ut, blir avvist; behandleren får melding i journalsystemet, og pasienten får SMS eller e-post med lenke til nav.no. Nav kan ikke overprøve avvisningen eller godkjenne sykmeldingen manuelt, så feilen må rettes av den som sykmelder.

Den tredje er **videreformidling til den sykmeldte og arbeidsgiveren**. Den sykmeldte finner sykmeldingen i Ditt sykefravær på nav.no og sender den derfra til arbeidsgiveren. Arbeidsgiveren mottar sykmeldingen i Altinn-innboksen til den underenheten den ansatte er registrert på i a-meldingen, og får varsel på SMS eller e-post etter varslingsinnstillingene i Altinn. Den nærmeste lederen får e-post og følger opp gjennom Dine sykmeldte. Papirsykmeldinger digitaliseres av Nav og kommer etter noen dager inn i Ditt sykefravær.

Den fjerde er **dialogmeldinger i sykefraværsoppfølgingen**. Nav sender innkalling, avlysning og unntak for dialogmøter til behandleren, og behandleren kan sende henvendelser om sykefraværsoppfølging og svar på forespørsler fra Nav. Meldingene legger seg direkte i journalsystemet. Arbeidsgiveren kan sende oppfølgingsplanen digitalt til fastlegen, der Nav bare er teknisk videreformidler uten innsyn i planen.

### Typiske brukssituasjoner (generisk)
- en fastlege sykmelder en pasient og sender sykmeldingen direkte fra journalsystemet
- en arbeidsgiver mottar sykmeldingen i Altinn og starter oppfølgingen av den ansatte
- Nav kaller inn behandleren til dialogmøte, og behandleren svarer fra journalsystemet
- en leverandør av journalsystem bygger eller oppdaterer kommunikasjonen med Nav

### Når Digital sykmelding normalt ikke er førstevalg
Digital sykmelding er ikke en generell kanal for meldinger mellom helsetjenesten og Nav. Den dekker sykmelding og dialogmeldinger i sykefraværsoppfølgingen, ikke legeerklæringer og andre erklæringer som har egne skjema og løp.

Den er heller ikke kilden til inntekts- og arbeidsforholdsopplysninger. Slike opplysninger rapporteres gjennom `FLERE-001` A-ordningen og ligger i `NAV-001` Aa-registeret. Søknad om sykepenger og inntektsmelding er egne tjenester i Nav.

For pasienter uten innlogging på høyeste sikkerhetsnivå, uten fødselsnummer eller D-nummer, og for pasienter som har reservert seg mot digital kommunikasjon, brukes fortsatt papir.

### Scope og avgrensning
Inngår:
- innsending av sykmelding fra journalsystemet til Nav, med automatisk kontroll og avvisning
- meldingsformat, spesifikasjoner og eksempelfiler for sykmelding og dialogmeldinger
- visning og innsending av sykmeldingen for den sykmeldte i Ditt sykefravær
- formidling av sykmeldingen til arbeidsgiverens Altinn-innboks og til nærmeste leder i Dine sykmeldte
- dialogmeldinger mellom Nav og behandler, og formidling av oppfølgingsplan fra arbeidsgiver til fastlege
- den nye innsendingsløsningen for behandlere som er under utvikling

Inngår ikke:
- søknad om sykepenger, inntektsmelding og vedtak om sykepenger
- journalsystemene og deres kommunikasjonsprogramvare, som leveres av EPJ-leverandørene
- innlogging, tilgangsstyring og transport, som leveres av HelseID, ID-porten, Altinn og meldingsinfrastrukturen i helsesektoren
- legeerklæringer og andre erklæringer til Nav

## Veikart over kommende funksjonalitet
**Fakta:** Nav utvikler en ny sykmelding og endrer adresseringen for dialogmeldinger, og ber nye leverandører kontakte Nav før de starter utvikling (nav.no, tekniske spesifikasjoner). Den nye innsendingsløsningen kan startes fra journalsystemet med SMART on FHIR eller brukes frittstående med innlogging gjennom HelseID (github.com/navikt/syk-inn).

**Ikke offentlig dokumentert i denne arbeidsøkten:** Tidsplan for når den nye løsningen tar over, og om dagens XML-baserte innsending skal fases ut.

## Forretningsverdi/Verdiforslag
For den sykmeldte ligger verdien i at sykmeldingen kommer digitalt og kan sendes til arbeidsgiveren med noen få valg, uten at diagnosen følger med og uten papir som skal leveres.

For behandleren ligger verdien i at sykmeldingen sendes fra journalsystemet der arbeidet gjøres, med umiddelbar tilbakemelding ved feil, og at dialogen med Nav om sykefraværet kommer inn i samme system.

For arbeidsgiveren ligger verdien i at sykmeldingen kommer strukturert i Altinn fra første dag, med styrt tilgang for HR, lønn og nærmeste leder, slik at oppfølgingen kan starte tidlig.

For Nav ligger verdien i at sykmeldingene kommer inn som kontrollerte, strukturerte data som kan brukes direkte i sykefraværsoppfølging og sykepengebehandling.

## Utfordringer og risiko

| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Teknisk | Overgang til ny løsning mens dagens spesifikasjoner delvis er utdatert | Nav ber nye leverandører ta kontakt før utvikling; tidsplan er ikke offentlig dokumentert i denne arbeidsøkten |
| Leverandør | Behandleren er avhengig av journalleverandøren for innsending og feilretting | Ved feil i innsendingen skal legen kontakte EPJ-leverandøren før Nav |
| Juridisk | Automatisk avvisning kan ikke overprøves manuelt | Behandleren må rette og sende sykmeldingen på nytt |
| Personvern | Sykmeldingen inneholder helseopplysninger | Arbeidsgiveren får ikke diagnose; tilgang i Altinn krever egne rettigheter for personopplysninger av særlig kategori |
| Brukeropplevelse | Pasienter uten innlogging på høyeste nivå faller utenfor den digitale flyten | Papir brukes som reserveløsning, og Nav digitaliserer papirsykmeldinger |
| Tilgangsstyring | Feil oppsett av underenhet eller rettigheter gjør at arbeidsgiveren ikke finner sykmeldingen | Sykmeldingen går til underenheten fra a-meldingen; Nav anbefaler tilgangspakken Lønn med personopplysninger av særlig kategori |

## Kanaler
**Journalsystem:** Behandlere sender sykmelding og dialogmeldinger fra EPJ med PKI-basert signatur og kryptering. Den nye innsendingsløsningen kan startes fra journalsystemet eller brukes frittstående på nav.no med innlogging gjennom HelseID.

**Nav.no:** Den sykmeldte bruker Ditt sykefravær med innlogging på høyeste sikkerhetsnivå. Nærmeste leder bruker Dine sykmeldte.

**Altinn:** Arbeidsgiveren mottar sykmeldinger og sykepengesøknader i Altinn-innboksen, med tilgang styrt av Altinn-rettigheter og tilgangspakker.

**Papir:** Reserveløsning for pasienter og behandlere utenfor den digitale flyten.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** Driftsmodell og plattform for sykmeldingsløsningen.

**Fakta:** Kildekoden ligger i Navs organisasjon på GitHub, og den nye innsendingsløsningen bruker blant annet Wonderwall med HelseID som innloggingsproxy (github.com/navikt/syk-inn).

## Gjenbruk
Løsningen gjenbrukes ved at alle journalsystemer bygger mot samme meldingsformat og samme mottak hos Nav, og ved at alle arbeidsgivere mottar sykmeldingen i samme Altinn-innboks. Spesifikasjoner, skjema og eksempelfiler er publisert åpent. Selve tjenesten er bundet til Navs oppgaver med sykefravær og sykepenger, og er ikke laget for at andre virksomheter skal bruke den til egne formål.

### Vanlige kombinasjoner med andre produkter
- `NHN-002` HelseID, for innlogging av helsepersonell i den nye innsendingsløsningen.
- `DIGDIR-004` Altinn Autorisasjon, for arbeidsgiverens rettigheter og tilgangspakker til sykmelding og sykepengesøknad.
- `FLERE-001` A-ordningen og `NAV-001` Aa-registeret, for arbeidsforholdet som bestemmer hvilken underenhet sykmeldingen sendes til.

**Kildekode:** Åpen kildekode. Mottak, kontroll og den nye innsendingsløsningen er publisert i Navs organisasjon på GitHub.

**Lisens:** MIT for de kontrollerte repositoriene navikt/syk-inn, navikt/syfosmmottak og navikt/flex-sykmeldinger-backend. Enkelte tilhørende bibliotek har andre lisenser, for eksempel Apache-2.0 for navikt/sykmelding-ocr.

**Repositorium:** https://github.com/navikt/syk-inn, https://github.com/navikt/syfosmmottak, https://github.com/navikt/Sykmelding_v1.4

## Støtter arkitekturprinsipper
- **P6: Lag digitale løsninger som støtter samhandling**
  Sykmeldingen flyter digitalt mellom helsetjenesten, Nav og arbeidsgiveren etter ett felles meldingsformat, og dialogmeldingene gir en fast kanal mellom Nav og behandleren.

- **P1: Ta utgangspunkt i brukernes behov**
  Den sykmeldte slipper å bære papir mellom lege, Nav og arbeidsgiver, og arbeidsgiveren får det den trenger for oppfølgingen uten diagnose.

- **P7: Sørg for tillit til oppgaveløsningen**
  Støttes delvis. Meldingene signeres og krypteres, og arbeidsgiverens tilgang krever egne rettigheter. Automatisk avvisning uten mulighet for manuell overprøving gir forutsigbarhet, men kan gi brudd i flyten for pasienten.

- **P4: Del og gjenbruk data**
  Støttes delvis. Sykmeldingen registreres én gang og brukes av Nav, den sykmeldte og arbeidsgiveren, men dataene deles bare innenfor sykefraværsløpet.

Spenningen ligger i overgangen og i avhengigheten av journalleverandørene. Meldingsformatet har vært stabilt lenge, men Nav varsler at deler av spesifikasjonene er utdatert uten å ha publisert når den nye løsningen tar over. Behandleren kan ikke rette feil i innsendingen uten journalleverandøren. Papir lever videre for grupper som står utenfor innlogging på høyeste sikkerhetsnivå.

## Finansiering
**Fakta:** Behandlerens svar på dialogmeldinger honoreres etter takst L8 (nav.no, Om sykmeldingen).

**Ikke offentlig dokumentert i denne arbeidsøkten:** Hvordan utvikling og drift av løsningen finansieres, og om journalleverandørene får tilskudd eller betaling for å utvikle mot den nye løsningen.

## Forvaltning/eier

| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Arbeids- og velferdsetaten (Nav) | nav.no, Om sykmeldingen; tekniske spesifikasjoner utarbeidet av Arbeids- og velferdsdirektoratet |
| Spesifikasjoner | Arbeids- og velferdsdirektoratet; standarder for hodemelding, dialogmelding og vedlegg fra Direktoratet for e-helse | nav.no, tekniske spesifikasjoner |
| Driftsansvar | Ikke offentlig dokumentert i denne arbeidsøkten | – |
| Innlogging for helsepersonell | Norsk helsenett SF gjennom HelseID i den nye innsendingsløsningen | github.com/navikt/syk-inn |
| Journalsystemer | EPJ-leverandørene, som utvikler kommunikasjonsløsningen etter Navs spesifikasjoner | nav.no, Om sykmeldingen |
| Budsjettansvar | Ikke offentlig dokumentert i denne arbeidsøkten | – |
| Styringsmodell | Nav styres av Arbeids- og inkluderingsdepartementet. Plikten til elektronisk innsending er fastsatt i forskrift | Lovdata, forskrift 2009-10-02-1285 |

## Lenke til dokumentasjon
- Om sykmeldingen, for leger og andre behandlere: https://www.nav.no/samarbeidspartner/om-sykmeldingen
- Digital sykmelding og dialogmeldinger – tekniske spesifikasjoner: https://www.nav.no/samarbeidspartner/digital-sykmelding-og-dialogmeldinger-tekniske-spesifikasjoner
- Sykmelding for arbeidsgivere: https://www.nav.no/arbeidsgiver/sykmelding
- Tilganger for arbeidsgivere: https://www.nav.no/arbeidsgiver/tilganger
- Sykmelding for den sykmeldte: https://www.nav.no/sykmelding
- Skjema Sykmelding 2013 v1.4: https://github.com/navikt/Sykmelding_v1.4

## Kildegrunnlag brukt i utfyllingen
Hentet 2026-10-25:
- Nav, Om sykmeldingen (for leger og andre behandlere): https://www.nav.no/samarbeidspartner/om-sykmeldingen
- Nav, Digital sykmelding og dialogmeldinger – tekniske spesifikasjoner: https://www.nav.no/samarbeidspartner/digital-sykmelding-og-dialogmeldinger-tekniske-spesifikasjoner
- Nav, Sykmelding (for arbeidsgivere): https://www.nav.no/arbeidsgiver/sykmelding
- Nav, Tilganger for arbeidsgivere: https://www.nav.no/arbeidsgiver/tilganger
- Nav, Sykmelding (for den sykmeldte): https://www.nav.no/sykmelding
- Lovdata, forskrift om elektronisk kommunikasjon med Nav: https://lovdata.no/nav/forskrift/2009-10-02-1285
- Lovdata, forskrift om unntak fra pålegg om elektronisk kommunikasjon: https://lovdata.no/nav/forskrift/2009-12-07-1480
- GitHub, navikt/Sykmelding_v1.4: https://github.com/navikt/Sykmelding_v1.4
- GitHub, navikt/syk-inn (ny innsendingsløsning, MIT): https://github.com/navikt/syk-inn
- GitHub, navikt/syfosmmottak (mottak av sykmeldinger, MIT): https://github.com/navikt/syfosmmottak
