# Tenor testdatasøk

## Navn
Tenor testdatasøk

## Ressurs ID
SKATT-003

## Status/Livsfase
**Fakta:** Aktiv. Skatteetaten oppgir at Tenor testdatasøk er i drift, med løpende utvidelse av datakilder etter hvert som nye kilder blir klare. Løsningen ble etablert gjennom et prosjekt som fikk støtte fra medfinansieringsordningen i 2019, og som Digdir oppgir som avsluttet.

**Deduksjon:** Lanseringen skjedde i 2020. Dette er omtalt i bransjepresse, men vi fant ingen datert lanseringsmelding fra Skatteetaten selv, så årstallet bør regnes som omtrentlig.

**Fakta:** Skatteetaten har både driftsansvar og forvaltningsansvar for løsningen.

**Deduksjon:** Løsningen er ute av innføringsfase og i ordinær forvaltning. Den har vært i drift i over seks år, har etablert API, publisert dokumentasjon og en definert prosess for å ta inn nye datakilder.

## Modenhet
**Fakta:** Løsningen har webgrensesnitt med både forhåndsdefinerte søk og avansert søk, et API for maskin-til-maskin-bruk, og publisert teknisk dokumentasjon med kildeoversikt.

**Fakta:** Digdir viser til Tenor i sin egen tekniske dokumentasjon som anbefalt måte å finne testbrukere på for ID-porten og Kontakt- og reservasjonsregisteret.

**Deduksjon:** Modenheten er høy. At en annen etat anbefaler løsningen i sin egen produktdokumentasjon er et sterkere modenhetssignal enn forvalterens egen omtale, fordi det forutsetter at løsningen er stabil nok til å inngå i andres anbefalte arbeidsflyt.

## Kort beskrivelse
Tenor testdatasøk er en søkeløsning som gir tilgang til syntetiske testdata fra Test-Norge. Test-Norge er en syntetisk parallellverden med over én million innbyggere som har syntetiske personnumre, virksomheter, inntekter, arbeidsforhold og kjøretøy, bygget slik at de speiler kompleksiteten i reelle data uten å inneholde personopplysninger.

Løsningen er et arbeidsverktøy for systemutvikling og test. Den løser et problem som ellers presser virksomheter mot å bruke produksjonsdata i testmiljøer.

## Kapabiliteter
Koblingene er satt fordi Tenor selv tilgjengeliggjør testdatagrunnlaget og gir det et søkbart inngangspunkt. Forsvant løsningen, ville ikke noen annen ressurs i porteføljen levert et tverrsektorielt, personvernsikkert testdatagrunnlag med felles inngang. Tenor bruker samtidig ID-porten for innlogging og Maskinporten for API-tilgang; de avhengighetene er beskrevet under `Gjenbruk`, ikke som egne kapabiliteter.

- **Datakilder: Testdata**
  genererer og tilgjengeliggjør representative og personvernsikre datasett, som er kapabilitetens kjerne. Test-Norge speiler statistiske egenskaper i reelle registerdata uten å inneholde personopplysninger, og Tenor er inngangen til det grunnlaget.

- **Tjenesteutvikling: Utviklings- og kjøretidsmiljø**
  inngår som felles verktøy i verktøykassen for utvikling av digitale tjenester. Uten et felles testdatagrunnlag må hver virksomhet bygge og vedlikeholde sitt eget, og testdata blir en kostnad i hvert enkelt utviklingsløp framfor en delt byggekloss.

- **Datautveksling og integrasjon: Dele data med andre**
  tilgjengeliggjør testdataene som et dokumentert og sikret API, slik at andre virksomheter kan finne og gjenbruke dem i egne automatiserte tester i stedet for å hente dem manuelt.

## Produktmål
**Fakta:** Skatteetaten beskriver formålet som å gi enkel tilgang til testdata fra Test-Norge for alle som driver systemutvikling og trenger testdata, med data fra flere ulike kilder samlet ett sted.

**Deduksjon:** Et underliggende mål er å redusere bruken av produksjonsdata i testmiljøer. Dette følger av at løsningen konsekvent framhever at dataene er syntetiske og uten personvernrisiko, men er ikke formulert som et eksplisitt måltall noe sted vi fant.

**Deduksjon:** Et annet mål er å gjøre testdata sammenhengende på tvers av registre. Verdien av at samme syntetiske person finnes både i Folkeregisteret, Enhetsregisteret og skattedataene er at man kan teste hele verdikjeder, ikke bare enkeltoppslag.

## Brukerbehov
Utviklings- og testmiljøer trenger data som ligner produksjonsdata i struktur, variasjon og kompleksitet. Uten et slikt grunnlag oppstår tre uønskede utfall: testene blir for enkle til å avdekke reelle feil, virksomheter tar i bruk produksjonsdata med personopplysninger i testmiljøer, eller hver virksomhet bygger sitt eget testdatasett som ikke henger sammen med andres.

Behovet er særlig sterkt ved integrasjonstesting mot nasjonale fellesløsninger, der en testperson må eksistere konsistent i flere registre samtidig for at testen skal ha verdi.

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Utviklere i offentlige virksomheter | Testpersoner og testvirksomheter med riktige egenskaper | Integrasjonstest mot fellesløsninger og registre | Primærbrukergruppen |
| Testere og testledere | Gjenfinnbare testdata for definerte testtilfeller | Manuell og utforskende test | Bruker særlig avansert søk |
| Leverandører og konsulentmiljøer | Testdata uten tilgang til produksjonsdata hos kunden | Utvikling på oppdrag for offentlig sektor | Tilgang forutsetter eget organisasjonsnummer |
| Datakildeeiere i etatene | Få egne syntetiske data eksponert og holdt synkronisert | Levere data inn i Tenor | Må holde egne testmiljøer i synk med Tenor |
| Skatteetaten som forvalter | Drift, videreutvikling og koordinering mot kildeeiere | Forvaltning av løsningen | Både drifts- og forvaltningsansvar |

## Hovedfunksjoner
Den første hovedfunksjonen er søk i syntetiske testdata gjennom et webgrensesnitt. Brukeren kan enten søke med forhåndsdefinerte søkekriterier, som dekker de vanligste behovene, eller bygge egne spørringer i avansert søk når testtilfellet krever en person eller virksomhet med bestemte egenskaper.

Den andre er at dataene er sammenhengende på tvers av kilder. Syntetiske personer fra Folkeregisteret, syntetiske virksomheter fra Enhetsregisteret og Foretaksregisteret, og syntetiske inntekts- og skattedata henger sammen i samme syntetiske univers. Skatteetaten oppgir i tillegg arbeidsforhold og kjøretøy blant datatypene som er tilgjengelige.

Den tredje er API-tilgang for automatisert bruk. Testdata kan hentes direkte fra automatiserte testløp i stedet for å kopieres manuelt fra webgrensesnittet. Tilgangen går via Maskinportens testmiljø, og krever at virksomheten ber om tilgang til Tenors scope ved å oppgi organisasjonsnummer.

Den fjerde er en definert prosess for å ta inn nye datakilder. Skatteetaten oppgir at både offentlige etater og private aktører kan bidra med egne syntetiske testdata, forutsatt at dataene knytter seg til personer eller virksomheter, og at bidragsyteren holder egne testmiljøer synkronisert med det som ligger i Tenor.

### Typiske brukssituasjoner (generisk)
- finne en testperson med bestemte egenskaper for integrasjonstest mot et nasjonalt register
- finne testbrukere for pålogging og testing mot ID-porten og Kontakt- og reservasjonsregisteret
- hente testdata automatisk inn i regresjonstester i en byggekjede
- teste en verdikjede der samme syntetiske person må finnes i flere registre samtidig

### Når Tenor testdatasøk normalt ikke er førstevalg
Tenor er ikke førstevalg når testbehovet ikke handler om person- eller virksomhetsdata. Løsningen er bygget rundt syntetiske personer og virksomheter, og bidrag fra nye kilder forutsetter nettopp en slik tilknytning.

Den er heller ikke tilstrekkelig alene når en virksomhet trenger å konstruere testdata med helt bestemte, sjeldne egenskaper som ikke finnes i grunnlaget. Da må testdata genereres i egne verktøy, og Tenor brukes eventuelt som grunnlag.

Tenor erstatter ikke testmiljøene hos den enkelte tjenesteeier. Løsningen gjør testdataene søkbare, men selve testingen skjer mot etatenes egne testmiljøer, som må være synkronisert med Tenor for at dataene skal stemme.

### Scope og avgrensning
Inngår:
- søkeløsning over syntetiske testdata fra Test-Norge
- API for maskinell henting av testdata
- samling og synliggjøring av datakilder fra flere etater

Inngår ikke:
- testmiljøene til den enkelte tjenesteeier
- generering av skreddersydde testdata på bestilling
- testdata som ikke knytter seg til personer eller virksomheter

## Veikart over kommende funksjonalitet
**Fakta:** Skatteetaten oppgir at Tenor utvides med testdata fra nye kilder etter hvert som kildene blir klare, og at samarbeidet omfatter jevnlig erfaringsutveksling og seminarer.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Det ble ikke funnet et datert veikart, en prioritert liste over hvilke kilder som står for tur, eller uttalte planer for funksjonell videreutvikling av selve søkeløsningen. Utvidelsen framstilles som kildedrevet framfor som en planlagt funksjonsutvikling.

## Forretningsverdi/Verdiforslag
For den enkelte virksomheten ligger verdien i at testdata blir en ressurs man henter, ikke en man bygger. Det fjerner et arbeid som ellers gjentas i hvert utviklingsløp, og gjør at testene kan bygge på et grunnlag med realistisk variasjon.

For personvernet ligger verdien i at et fullgodt alternativ til produksjonsdata faktisk finnes. Uten et slikt alternativ er presset mot å bruke reelle personopplysninger i test et vedvarende problem, som må håndteres med kontroller og etterlevelse framfor å fjernes ved kilden.

For samhandlingen mellom etatene ligger verdien i at testdataene er felles. Når to virksomheter tester en tjenestekjede mot hverandre, kan de vise til samme syntetiske person. Uten felles grunnlag må slike testløp koordineres manuelt mellom partene.

For leverandørmarkedet ligger verdien i at utvikling for offentlig sektor kan skje uten tilgang til kundens produksjonsdata, noe som senker terskelen for å delta og reduserer risikoen i kontraktsforhold.

## Utfordringer og risiko

| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Synkronisering | Kildeeiere må holde egne testmiljøer i synk med Tenor | Testdata som finnes i søket, men ikke virker i testmiljøet | Tydelige forventninger til kildeeiere, og synlig status per kilde |
| Dekning | Nye kilder kommer etter hvert som de blir klare | Ujevn dekning mellom sektorer over tid | Prioritert og kommunisert rekkefølge for nye kilder |
| Tilgang | API-tilgang krever egen forespørsel og Maskinporten-oppsett | Terskel for automatisert bruk hos mindre aktører | Forenklet tilgangsflyt og god kom-i-gang-dokumentasjon |
| Realisme | Syntetiske data speiler statistiske egenskaper, ikke alle virkelige særtilfeller | Feil som først oppdages i produksjon | Mulighet for å supplere med egengenererte spesialtilfeller |
| Navnelikhet | `Test-Norge` og NAVs `testnorge`-verktøykasse forveksles | Uklarhet om hva som forvaltes av hvem | Konsekvent navnebruk i dokumentasjon og register |

## Kanaler
Løsningen er tilgjengelig som webapplikasjon med innlogging via ID-porten, og som API for maskinell bruk. Dokumentasjonen publiseres på egne dokumentasjonssider på GitHub Pages, i tillegg til Skatteetatens egne nettsider.

## Plattform
**Fakta:** Løsningen tilbys som en sentral tjeneste forvaltet av Skatteetaten, med webgrensesnitt og API. API-tilgang går gjennom Maskinportens testmiljø.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Teknisk plattform, driftsmodell og hvor løsningen kjøres er ikke beskrevet i de åpne kildene vi gikk gjennom.

## Gjenbruk
Tenor er selv en gjenbrukbar ressurs på tvers av sektorer, og brukes av virksomheter som ikke har noe annet forhold til Skatteetaten enn testbehovet.

Løsningen bygger på andre ressurser i porteføljen:
- **ID-porten** brukes for innlogging i webgrensesnittet.
- **Maskinporten** brukes for tilgang til API-et.
- **Folkeregisteret**, som er `SKATT-001` i porteføljen, leverer det syntetiske folkeregistergrunnlaget gjennom Skatteetaten.

### Vanlige kombinasjoner med andre produkter
Tenor brukes typisk sammen med den fellesløsningen som faktisk skal testes. Digdir viser til Tenor for å finne testbrukere ved test mot ID-porten og Kontakt- og reservasjonsregisteret, og tilsvarende behov oppstår ved test mot eFormidling og andre fellesløsninger med personreferanser.

Løsningen har også en kobling til `142` Medfinansieringsordningen, som finansierte etableringen. Den koblingen er historisk og forklarer hvordan løsningen ble til, men er ikke en driftsavhengighet.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Tenor gjør syntetiske data fra flere etater tilgjengelige gjennom ett felles inngangspunkt, i stedet for at hver virksomhet henter dem kildevis.

- **P5: Del og gjenbruk løsninger**
  Løsningen er bygget én gang og brukes av mange. Alternativet er at hver virksomhet bygger og vedlikeholder eget testdatagrunnlag.

- **P6: Lag digitale løsninger som støtter samhandling**
  Felles testdata gjør det mulig å teste tjenestekjeder på tvers av virksomheter mot samme syntetiske person.

- **P7: Sørg for tillit til oppgaveløsningen**
  Ved å gjøre syntetiske data til et reelt alternativ reduserer løsningen behovet for å bruke personopplysninger i testmiljøer.

Svakhet: Tenor løser tilgangen til testdata, men ikke synkroniseringen mot etatenes egne testmiljøer. Den avhengigheten ligger hos kildeeierne, og et avvik der slår ut som feil hos brukeren av Tenor.

## Finansiering
**Fakta:** Løsningen ble etablert gjennom prosjektet `Nasjonal tilgang til syntetiske persondata for testformål`, som fikk støtte fra medfinansieringsordningen i 2019 med kr 8 836 256. Digdir oppgir at prosjektet er avsluttet. Medfinansieringsordningen er beskrevet som `142` i porteføljen.

**Fakta:** Digdir oppgir i sluttvurderingen at etatenes egne interne ressurser utgjorde om lag tre ganger så mye innsats som de eksterne konsulentressursene ordningen finansierte.

**Deduksjon:** Finansieringsmodellen var altså i praksis en delfinansiering, der ordningen utløste arbeidet mens hoveddelen av innsatsen ble båret av etatene selv. Det er verdt å merke seg ved vurdering av hva medfinansieringsordningen faktisk koster og utløser.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Hvordan løsningen finansieres i ordinær drift etter at prosjektet ble avsluttet, og om deltakende etater bidrar med midler eller bare med data, ble ikke funnet i de åpne kildene.

## Forvaltning/eier

| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Skatteetaten |
| Forvaltningsansvar | Skatteetaten har både drifts- og forvaltningsansvar for løsningen |
| Datakildeansvar | Den enkelte kildeeier, som Brønnøysundregistrene for syntetisk Enhetsregister og Foretaksregister |
| Samarbeidsform | Samarbeid mellom etater, med erfaringsutveksling og seminarer |
| Endringsprosess | Nye kilder tas inn etter hvert som de blir klare, etter avtale med kildeeier |
| Publiseringsarena | Skatteetatens nettsider og egne dokumentasjonssider |

**Deduksjon:** Forvaltningsmodellen kombinerer et tydelig eierskap hos Skatteetaten med distribuert ansvar for dataene. Det gir ett kontaktpunkt for brukerne, men gjør datakvaliteten avhengig av kildeeiere som Skatteetaten ikke styrer.

## Lenke til dokumentasjon
- https://www.skatteetaten.no/testdata/
- https://skatteetaten.github.io/testnorge-tenor-dokumentasjon/
- https://skatteetaten.github.io/testnorge-tenor-dokumentasjon/kilder/
- https://skatteetaten.github.io/api-dokumentasjon/en/test/tenor
- https://docs.digdir.no/docs/Kontaktregisteret/krr_testbrukere
- https://docs.digdir.no/docs/idporten/idporten/idporten_testbrukere.html
- https://www.digdir.no/medfinansieringsordningen/skatteetaten-nasjonal-tilgang-til-syntetiske-persondata-testformal/994

## Kildegrunnlag brukt i utfyllingen
- https://www.skatteetaten.no/testdata/, kontrollert 2026-09-28
- https://skatteetaten.github.io/testnorge-tenor-dokumentasjon/, kontrollert 2026-09-28
- https://skatteetaten.github.io/testnorge-tenor-dokumentasjon/kilder/, kontrollert 2026-09-28
- https://docs.digdir.no/docs/Kontaktregisteret/krr_testbrukere, kontrollert 2026-09-28
- https://docs.digdir.no/docs/idporten/idporten/idporten_testbrukere.html, kontrollert 2026-09-28
- https://www.digdir.no/medfinansieringsordningen/skatteetaten-nasjonal-tilgang-til-syntetiske-persondata-testformal/994, kontrollert 2026-09-28
- https://www.digi.no/tumstudio/digitalisering-og-offentlig-it/annonse-testdata-revolusjon-det-som-tok-dager-kan-na-gjores-med-fa-klikk/558040, kontrollert 2026-09-28. Merk: annonsørinnhold, brukt bare som støtte for lanseringsår og omfang av etatssamarbeid
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-28
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-28
