# BarentsWatch

## Navn
BarentsWatch – Kystverkets tjenester for datadeling og samhandling om norske hav- og kystområder

## Ressurs ID
KYST-001

## Status/Livsfase
**Produksjon** – åpne tjenester, API-er og lukkede tjenester for etatene er i drift.

**Fakta:** BarentsWatch har siden 2012 gjort offentlige data tilgjengelige gjennom egne tjenester, og er en avdeling i Kystverket (kystverket.no, BarentsWatch; barentswatch.no, Ny instruks for BarentsWatch). Nærings- og fiskeridepartementet (NFD) fastsatte 22. desember 2025 en ny hovedinstruks for Kystverket, gjeldende fra 1. januar 2026, med et eget punkt om BarentsWatch (hovedinstruks for Kystverket, punkt 3.2.5). Det tidligere mandatet fra 2017 er merket som utgått (barentswatch.no, Målsettinger og mandat).

## Modenhet
**Høy teknisk og organisatorisk modenhet, med åpne vilkår men uten forpliktende leveransenivå for de åpne tjenestene.**

- Oppdraget er forankret i hovedinstruksen for Kystverket, med krav om etatsgruppe, departementsgruppe, femårig strategi og årlig rapportering (hovedinstruks for Kystverket, punkt 3.2.5).
- De åpne API-ene har publiserte bruksvilkår, NLOD som lisens og krav om kildeangivelse (barentswatch.no, API terms and conditions).
- API-ene er dokumentert med OpenAPI-beskrivelser, og endringer varsles på developer.barentswatch.no (live.ais.barentswatch.no; barentswatch.no, Open data via BarentsWatch).
- Live AIS-API-et er i versjon v1 og brukes av Kystverkets egen AIS-tjeneste NAIS (live.ais.barentswatch.no).
- Vilkårene sier at informasjonen kan inneholde feil, og at verken BarentsWatch eller Kystverket garanterer innhold eller relevans (barentswatch.no, API terms and conditions).

**Deduksjon:** Det svakeste leddet for den som bygger på de åpne tjenestene, er fraværet av leveransegaranti. Instruksen gir Kystverket ansvar for oppetid, men de åpne vilkårene gir ingen avtale om tilgjengelighet å vise til. For data fra andre fagetater avhenger kvaliteten dessuten av den enkelte etatens leveranse.

## Kort beskrivelse
BarentsWatch er Kystverkets tjenester for datadeling og samhandling om norske hav- og kystområder. Tjenestene sammenstiller data fra flere statlige fagetater og gjør dem tilgjengelige på to måter.

Den **åpne delen** er kartbaserte tjenester, nedlastbare datasett og åpne API-er for alle. Her ligger blant annet åpne AIS-data om skipstrafikk fra Kystverkets nasjonale AIS-nett, fiskehelse- og havbruksdata, fiskeriinformasjon, bølgevarsel og varsel for polare lavtrykk. Dataene er lisensiert under NLOD med kildeangivelsen «Data levert av BarentsWatch».

Den **lukkede delen** er sikre tjenester for havovervåking, beredskap og redning, der offentlige etater med operative oppgaver til havs kan dele et felles situasjonsbilde og samhandle fortrolig på tvers av etatsgrenser.

Kystverket har hovedansvaret for tjenestene og ansvaret for oppetid og informasjonssikkerhet. Fagetatene har medansvar for tjenester innen eget fagområde og ansvar for å dele, kvalitetssikre og oppdatere dataene.

## Kapabiliteter
BarentsWatch er kanalen der flere fagetaters hav- og kystdata, og Kystverkets egne AIS-data, blir sammenstilt og delt åpent. Dataene har andre eiere, men sammenstillingen, distribusjonen og strømmetjenesten for AIS leveres av BarentsWatch selv.

- **Datautveksling og integrasjon: Dele data med andre** BarentsWatch gjør data fra Kystverket, Fiskeridirektoratet, Mattilsynet, Veterinærinstituttet, Meteorologisk institutt og andre dataeiere tilgjengelige gjennom dokumenterte API-er, kart- og nedlastingstjenester, slik at mottakeren ikke må hente dataene fra hver etat.
- **Datakilder: Åpne data** BarentsWatch publiserer AIS-, fiskehelse-, havbruks-, fiskeri- og varslingsdata maskinlesbart under NLOD, med fast kildeangivelse, slik at alle kan bruke dem også kommersielt.
- **Datakilder: Sanntidsdata** Live AIS-API-et er en strømmetjeneste der klienten mottar nye AIS-meldinger med posisjoner og skipsdata fortløpende så lenge forbindelsen er åpen, med data fra Kystverkets nasjonale AIS-nett.

## Produktmål
**Fakta:** Kystverket skal gjennom BarentsWatch tilby oppdaterte digitale tjenester for datadeling og samhandling om norske havområder, og bidra til at hav- og kystområdene brukes og forvaltes effektivt, bærekraftig og godt koordinert (hovedinstruks for Kystverket, punkt 3.2.5).

**Fakta:** Instruksen deler oppdraget i to:
- sikre digitale tjenester for havovervåking, beredskap og redning, som gir et felles situasjonsbilde og gjør fortrolig samhandling på tvers av etatsgrenser mulig
- åpent tilgjengelige digitale tjenester for sammenstilling og formidling av offentlige kartbaserte data om kyst- og havområdene

**Fakta:** Kystverket kan også tilby andre tjenester for datadeling og samhandling etter behov, forutsatt finansiering og avklaring med NFD. Utvikling som ikke gjelder hav- og kystområder, skal løftes til NFD (hovedinstruks for Kystverket, punkt 3.2.5).

**Deduksjon:** Det operative målet for den åpne delen er at hav- og kystdata fra mange etater skal kunne hentes fra ett sted med felles vilkår, i stedet for at hver bruker inngår avtaler med hver dataeier.

## Brukerbehov
Etater med oppgaver til havs trenger et felles og oppdatert bilde av skipstrafikk, ressurser og hendelser når de skal overvåke, varsle eller redde. Uten en felles tjeneste ligger opplysningene spredt hos hver etat, og samordningen tar tid i situasjoner der tid er avgjørende.

Næring, forskning og publikum trenger åpne og sammenstilte data om havet: skipstrafikk, fiskehelse og havbruk, fiskerireguleringer og bølge- og strømforhold. Behovet er både visning i kart og maskinell tilgang til data som kan bygges inn i egne tjenester.

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige etater med operative oppgaver til havs | Felles situasjonsbilde og fortrolig samhandling | Havovervåking, beredskap, redning | Lukket del; tilgangsregler er ikke offentlig dokumentert i denne arbeidsøkten |
| Utviklere og virksomheter som bruker åpne API-er | AIS i sanntid, fiskehelse-, fiskeri- og varslingsdata | Egne tjenester, analyse, overvåking | Krever registrert bruker og API-klient; kildeangivelse er påkrevd |
| Havbruks- og fiskerinæringen | Fiskehelse, lus, reguleringer, navigasjonsvarsler | Drift og planlegging | Tjenester som Fiskehelse, AkvaInfo og FiskInfo |
| Sjøfarende og publikum | Skipstrafikk, bølge- og strømvarsel, arktisk seilasinformasjon | Planlegging av ferd og innsyn | Kartbaserte tjenester på barentswatch.no og NAIS |
| Forskning og analysemiljøer | Historiske og sammenstilte havdata | Analyse og forskning | Fiskehelsedata fra 2012; åpne AIS-data bare 14 dager tilbake |
| Fagetatene som dataeiere | Formidling av egne data i felles flate | Deling, kvalitetssikring og oppdatering av data | Medansvar for tjenester innen eget fagområde |
| Kystverket ved BarentsWatch | Drift, utvikling og forvaltning | Nasjonal tjeneste for hav- og kystdata | Leder etatsgruppen |

## Hovedfunksjoner
Den første hovedfunksjonen er **lukkede tjenester for etatssamhandling**. Kystverket skal gjennom BarentsWatch tilby sikre tjenester for havovervåking, beredskap og redning, som gir et felles situasjonsbilde og gjør det mulig for etatene å samhandle fortrolig på tvers av etatsgrenser. BarentsWatch beskriver dette som et skjermet overvåkingssystem som støtter operativ innsats, og omtaler et felles ressursregister bygget på innsamling og deling av eksisterende data. Hvilke enkelttjenester den lukkede delen består av i dag, og hvem som får tilgang, er ikke offentlig dokumentert i denne arbeidsøkten.

Den andre er **åpne AIS-data om skipstrafikk**. Kystverket driver det nasjonale AIS-nettet med om lag 90 landbaserte basestasjoner og fem AIS-satellitter. BarentsWatch gjør et utvalg av dataene tilgjengelig gjennom Live AIS-API-et, en JSON-strømmetjeneste der klienten mottar nye meldinger fortløpende, med mulighet for nedsampling til én melding per minutt per fartøy. API-et leverer posisjonsrapporter, statiske skipsdata, navigasjonsinstallasjoner og meteorologiske og hydrografiske meldinger, og et eget API gir historiske spor. De åpne dataene dekker norsk økonomisk sone og vernesonene ved Svalbard og Jan Mayen, og omfatter ikke fiskefartøy under 15 meter, fritidsfartøy og seilfartøy under 45 meter eller data eldre enn 14 dager.

Den tredje er **andre åpne fagtjenester og API-er**. Fiskehelse-API-et gir data om oppdrettslokaliteter, sykdom, lakselus, rømming og fartøytrafikk ved anlegg, med historikk fra 2012 og data fra Fiskeridirektoratet, Mattilsynet, Veterinærinstituttet og Kystverket. FiskInfo gir fiskerireguleringer, navigasjonsvarsler, seismisk aktivitet og oppslag i skipsregister. Bølgevarsel og Saltstraumen gir varsler for bølger og strøm i leder og utvalgte områder, med data fra NORCE og Meteorologisk institutt, og Polare lavtrykk bygger på data fra Meteorologisk institutt. Kartlag publiseres som WMS og WFS, og tjenesten Data gir nedlastbare datasett i CSV, JSON og formater for kartplottere.

Den fjerde er **styrt åpen tilgang med kildeangivelse**. API-ene er gratis, men brukeren må registrere seg på barentswatch.no og opprette en API-klient på Min side. Autentisering skjer med OpenID Connect og tilgangstoken. Tjenester som bruker dataene, skal vise «Data levert av BarentsWatch» og i tillegg oppgi dataeieren der den er en annen. Data med særskilt tilgang, som detaljerte opplysninger om faststående redskap i FiskInfo, er ikke lisensiert under NLOD. Ved stor trafikk skal brukeren kontakte BarentsWatch på forhånd.

### Typiske brukssituasjoner (generisk)
- hente skipstrafikk i sanntid i norske farvann til overvåking, analyse eller visning i egen tjeneste
- bruke fiskehelse- og havbruksdata i forvaltning, rådgivning eller næringsanalyse
- vise bølge- og strømvarsel eller fiskerireguleringer for sjøfarende og fiskere
- dele et felles situasjonsbilde mellom etater ved beredskap og redning, gjennom den lukkede delen

### Når BarentsWatch normalt ikke er førstevalg
BarentsWatch er ikke førstevalg for fullstendige AIS-data. Data om mindre fiskefartøy og fritidsfartøy og data eldre enn 14 dager inngår ikke i den åpne tilgangen. Full tilgang gis av Kystverket etter søknad, som en direkte datastrøm fra Kystverkets AIS-server, og er i hovedsak for offentlige myndigheter og havner.

BarentsWatch er heller ikke førstevalg for vær- og havvarsler generelt. Meteorologisk institutts egne prognoser, farevarsler og havvarsler hentes fra `MET-001` Frost og MET Weather API. BarentsWatch formidler bare enkelte varsler der MET er dataeier, sammenstilt for kyst og hav.

For å finne og hente geografiske datasett generelt er `KART-002` Geonorge rett inngang. Geonorge er den nasjonale katalogen der også BarentsWatch sine kartlag er dokumentert. Norgeskart er Kartverkets karttjeneste med ferdige kart over hele landet, og er ikke en tjeneste for havdata.

### Scope og avgrensning
Inngår:
- åpne kartbaserte tjenester og nedlastbare datasett på barentswatch.no
- åpne API-er: AIS (Live AIS og historiske spor), fiskehelse og AkvaInfo, FiskInfo, Polare lavtrykk, Saltstraumen og bølgevarsel
- kartlag publisert som WMS og WFS
- lukkede tjenester for havovervåking, beredskap og redning for offentlige etater
- NAIS som visning av skipstrafikk, utviklet av BarentsWatch for Kystverket

Inngår ikke:
- Kystverkets nasjonale AIS-nett og den lukkede, fullstendige AIS-tilgangen, som Kystverket gir etter søknad utenom BarentsWatch
- Kystinfo, som er Kystverkets egen karttjeneste
- dataeiernes egne fagsystemer og registre, som Fiskeridirektoratets, Mattilsynets og Meteorologisk institutts
- FiskInfo-rapportering og andre data med særskilt tilgang, som ikke er åpne data

## Veikart over kommende funksjonalitet
**Fakta:** Kystverket skal hvert femte år sende NFD forslag til langsiktig strategi for BarentsWatch, og rapportere resultater, prioriteringer og avveininger mellom sektorene i vedlegg til årsrapporten (hovedinstruks for Kystverket, punkt 3.2.5). API-endringer varsles på developer.barentswatch.no, og Live AIS-API-et oppgir at flere AIS-meldingstyper kan bli lagt til (live.ais.barentswatch.no).

**Ikke offentlig dokumentert i denne arbeidsøkten:** Innholdet i gjeldende strategi for BarentsWatch og konkrete planer for nye tjenester.

## Forretningsverdi/Verdiforslag
For etatene med oppgaver til havs ligger verdien i et felles situasjonsbilde og en fortrolig kanal for samhandling, slik at overvåking, beredskap og redning kan samordnes på tvers av etatsgrenser uten at hver etat bygger egne løsninger.

For dataeierne ligger verdien i at egne data blir formidlet i en felles flate med felles lisens og vilkår, der Kystverket står for drift og informasjonssikkerhet og fagetaten for innholdet.

For næringsliv og utviklere ligger verdien i gratis tilgang til sammenstilte havdata, også i sanntid for skipstrafikk, under en lisens som tillater kommersiell bruk mot kildeangivelse.

For sjøfarende og publikum ligger verdien i kartbaserte tjenester for skipstrafikk, bølger, strøm og arktisk seilas samlet på ett sted.

## Utfordringer og risiko

| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Leveransesikkerhet | Ingen leveransegaranti i de åpne vilkårene | Vilkårene sier at verken BarentsWatch eller Kystverket garanterer innhold eller relevans |
| Datakvalitet | Kvaliteten avhenger av hver fagetats leveranse | Fagetatene har ansvar for deling, kvalitetssikring og oppdatering av egne data (hovedinstruks, punkt 3.2.5) |
| Personvern | AIS kan identifisere enkeltpersoners fartøy | Mindre fiskefartøy og fritidsfartøy er unntatt fra de åpne dataene; ved full tilgang kan slike data bare brukes til oppgitt formål og ikke videreformidles |
| Juridisk | Data med særskilt tilgang har andre vilkår enn NLOD | Vilkårene skiller ut slike data; dataeier skal oppgis der den er en annen enn BarentsWatch |
| Teknisk | Stor trafikk kan gi gebyr for serverhåndtering | Brukeren skal kontakte BarentsWatch før bruk med stor trafikk |
| Styring | Prioritering mellom sektorer kan gi uenighet mellom etatene | Saker drøftes i etatsgruppen, og uenighet løftes til departementsnivå |

## Kanaler
**Webportal:** barentswatch.no med kartbaserte tjenester og nedlastbare datasett, åpent uten innlogging for publikumstjenestene. NAIS (nais.kystverket.no) viser skipstrafikk i sanntid.

**Maskinelle kanaler:** REST- og strømme-API-er dokumentert på developer.barentswatch.no og live.ais.barentswatch.no. Bruk krever registrert bruker på barentswatch.no og en API-klient opprettet på Min side, med autentisering etter OpenID Connect. Kartlag leveres som WMS og WFS fra BarentsWatch sin kartserver.

**Lukket kanal:** Den lukkede delen for etatene. Påloggingsmekanisme og tilgangsregler er ikke offentlig dokumentert i denne arbeidsøkten.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** Driftsmodell og plattform for BarentsWatch.

**Fakta:** Utviklingen gjøres av kommersielle leverandører valgt gjennom offentlige anskaffelser, og BarentsWatch har kontor i Tromsø (kystverket.no, BarentsWatch).

## Gjenbruk
Dataene er laget for gjenbruk: åpen lisens, dokumenterte API-er og fast kildeangivelse. Gjenbruket har tre vilkår brukeren må ta inn i egen løsning: registrert API-klient, synlig kildeangivelse «Data levert av BarentsWatch» med eventuell annen dataeier, og forhåndskontakt ved stor trafikk. Tjenester som bygger på dataene, kan ikke gi inntrykk av å være laget av BarentsWatch, og kan ikke endre datainnholdet.

### Vanlige kombinasjoner med andre produkter
- `MET-001` Frost og MET Weather API, for vær-, hav- og farevarsler direkte fra Meteorologisk institutt sammen med skipstrafikk og havdata.
- `KART-002` Geonorge, for å finne BarentsWatch sine kartlag og andre geografiske datasett som havdataene vises eller analyseres mot.
- `DIGDIR-014` data.norge.no, som felles katalog for å finne åpne offentlige datasett.

**Kildekode:** Ikke offentlig dokumentert. Kildekoden for BarentsWatch er ikke funnet publisert.

**Lisens:** Ikke offentlig dokumentert for kildekoden. Dataene er lisensiert under NLOD, som gjelder data, ikke kildekode.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  BarentsWatch deler data fra mange fagetater åpent og maskinlesbart under NLOD, og fagetatene har plikt til å dele og oppdatere dataene innen eget ansvarsområde.

- **P6: Lag digitale løsninger som støtter samhandling**
  Den lukkede delen er laget for fortrolig samhandling og felles situasjonsbilde på tvers av etatsgrenser, og den åpne delen gir dokumenterte API-er for integrasjon.

- **P2: Ta arkitekturbeslutninger på rett nivå**
  Støttes delvis. Saker som berører andre etaters ansvarsområde, drøftes i etatsgruppen, og uenighet løftes til departementsnivå. Utvikling utenfor hav- og kystområder skal løftes til NFD.

- **P5: Del og gjenbruk løsninger**
  Støttes delvis. Mange etater bruker samme tjenester i stedet for å bygge egne, men programvaren er ikke publisert for gjenbruk.

Spenningen ligger mellom bredde og forpliktelse. BarentsWatch samler data fra mange eiere, men de åpne vilkårene gir ingen leveransegaranti, og kvaliteten avhenger av hver fagetat. Den åpne AIS-tilgangen er bevisst avgrenset av personvernhensyn, slik at den ikke kan erstatte Kystverkets fullstendige AIS-tilgang der det trengs et komplett trafikkbilde. Den lukkede delen er lite beskrevet i åpne kilder, noe som gjør det vanskelig å vurdere den for nye brukere utenfra.

## Finansiering
**Fakta:** De åpne API-ene er gratis (barentswatch.no, API terms and conditions). Nye tjenester utover kjerneoppdraget forutsetter finansiering av investering og drift og avklaring med NFD (hovedinstruks for Kystverket, punkt 3.2.5).

**Ikke offentlig dokumentert i denne arbeidsøkten:** Hvordan utvikling og drift av BarentsWatch finansieres, og om fagetatene bidrar økonomisk.

## Forvaltning/eier

| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Kystverket, ved avdelingen BarentsWatch, har hovedansvar for tjenestene | Hovedinstruks for Kystverket, punkt 3.2.5; barentswatch.no, Ny instruks for BarentsWatch |
| Driftsansvar | Kystverket har ansvar for oppetid og informasjonssikkerhet | Hovedinstruks for Kystverket, punkt 3.2.5 |
| Medansvar | Fagetatene har medansvar for tjenester innen sitt fagområde, ansvar for deling, kvalitetssikring og oppdatering av egne data, og skal medvirke i forvaltning og utvikling av enkelttjenester de har medansvar for | Hovedinstruks for Kystverket, punkt 3.2.5 |
| Dataeiere | Blant annet Kystverket, Fiskeridirektoratet, Mattilsynet, Veterinærinstituttet, Meteorologisk institutt og NORCE for enkeltdatasett | barentswatch.no, Open data via BarentsWatch |
| Budsjettansvar | Ikke offentlig dokumentert i denne arbeidsøkten | – |
| Styringsmodell | NFD styrer Kystverket. Det skal være en etatsgruppe, ledet av Kystverket, og en departementsgruppe for BarentsWatch for å ivareta tverrsektorielle hensyn | Hovedinstruks for Kystverket, punkt 3.2.5 |

**Fakta:** BarentsWatch oppgir ti departementer og 29 forvaltningsetater og forskningsinstitutter som partnere (barentswatch.no, About us).

**Fakta:** Det utgåtte mandatet fra 2017 listet 16 etater i etatsgruppen, blant dem Direktoratet for samfunnssikkerhet og beredskap, Fiskeridirektoratet, Forsvaret, Hovedredningssentralene, Kartverket, Meteorologisk institutt, Politidirektoratet og Sjøfartsdirektoratet, og en departementsgruppe ledet av NFD (barentswatch.no, Målsettinger og mandat, utgått).

**Ikke offentlig dokumentert i denne arbeidsøkten:** Gjeldende sammensetning av etatsgruppen og departementsgruppen etter instruksen fra 2026.

## Lenke til dokumentasjon
- BarentsWatch: https://www.barentswatch.no/
- Ny instruks for BarentsWatch: https://www.barentswatch.no/kontakt-oss/ny-instruks-for-barentswatch/
- Åpne data via BarentsWatch: https://www.barentswatch.no/en/articles/open-data-via-barentswatch
- API-vilkår: https://www.barentswatch.no/en/articles/api-terms-and-conditions/
- Utviklerdokumentasjon: https://developer.barentswatch.no/
- Live AIS-API, OpenAPI-dokumentasjon: https://live.ais.barentswatch.no/
- Tilgang til AIS-data hos Kystverket: https://www.kystverket.no/en/sea-transport-and-ports/ais/access-to-ais-data/

## Kildegrunnlag brukt i utfyllingen
Hentet 2026-10-24:
- Nærings- og fiskeridepartementet, Hovedinstruks for styringen av Kystverket, fastsatt 22.12.2025 med virkning fra 01.01.2026, punkt 3.2.5: https://www.kystverket.no/contentassets/1520e4f23cc3429fbbb5722269eabe2f/hovedinstrukskystverket-010126.pdf/download
- BarentsWatch, Ny instruks for BarentsWatch: https://www.barentswatch.no/kontakt-oss/ny-instruks-for-barentswatch/
- BarentsWatch, Målsettinger og mandat (utgått, fastsatt 2017): https://www.barentswatch.no/kontakt-oss/malsettinger-og-mandat/
- BarentsWatch, About us: https://www.barentswatch.no/en/contact-us/about-us/
- BarentsWatch, Open data (API) via BarentsWatch: https://www.barentswatch.no/en/articles/open-data-via-barentswatch
- BarentsWatch, API terms and conditions: https://www.barentswatch.no/en/articles/api-terms-and-conditions/
- BarentsWatch Developer, Live AIS API: https://developer.barentswatch.no/docs/AIS/live-ais-api
- BarentsWatch, AIS Live API, OpenAPI-beskrivelse: https://live.ais.barentswatch.no/
- Kystverket, Access to AIS data: https://www.kystverket.no/en/sea-transport-and-ports/ais/access-to-ais-data/
- Kystverket, AIS Norway: https://kystverket.no/en/sea-transport-and-ports/ais/ais-norge
- Kystverket, BarentsWatch: https://www.kystverket.no/en/navigation-and-monitoring/barentswatch/
- Teknisk Ukeblad, Ny nettjeneste viser sjøtrafikken langs norskekysten i sanntid (2022), om at NAIS er utviklet av BarentsWatch for Kystverket: https://www.tu.no/artikler/ny-nettjeneste-viser-sjotrafikken-langs-norskekysten-i-sanntid/519917
