# Lovdatas åpne data og API

## Navn
Lovdata API – åpne datasett med gjeldende lover, sentrale forskrifter og Norsk Lovtidend

## Ressurs ID
LOVDAT-001

## Status/Livsfase
**Produksjon** – de åpne datapakkene er tilgjengelige og oppdateres hver natt.

**Fakta:** Lovdata tilbyr gratis datapakker uten krav om bruker eller autentisering. Oversikten over åpne datapakker i API-et viste 25. oktober 2026 seks pakker, med siste oppdatering mellom 17. og 24. oktober 2026 (api.lovdata.no, Om API-tjenesten; endepunktet `/v1/publicData/list`).

## Modenhet
**Høy teknisk modenhet og stabil forvaltning, men uten brukerstøtte og leveransegaranti for den åpne delen.**

- Stiftelsen Lovdata ble opprettet i 1981, og den elektroniske kunngjøringen av regelverk i Norsk Lovtidend har hatt status som offisiell kunngjøring siden 2001 (lovdata.no, Om Lovdata).
- API-et er dokumentert med en OpenAPI-beskrivelse og har en egen endringslogg (api.lovdata.no, Swagger).
- De konsoliderte tekstene holdes ajour parallelt med publiseringen på lovdata.no og i Lovdata Pro, og nye pakker legges ut hver natt (api.lovdata.no, FAQ).
- Dataene er lisensiert under NLOD 2.0 (api.lovdata.no, Om API-tjenesten).
- Lovdata gir ikke brukerstøtte på det åpne API-et. Support og vedlikehold tilbys bare gjennom betalt SLA-avtale (api.lovdata.no, FAQ og SLA).

**Deduksjon:** Det svakeste leddet for den som bygger på de åpne dataene, er at det ikke finnes leveransegaranti eller brukerstøtte uten avtale, og at de åpne dataene bare omfatter gjeldende regelverk. Den som trenger historiske versjoner, rettsavgjørelser eller spørringer mot enkeltbestemmelser, må inngå avtale med Lovdata.

## Kort beskrivelse
Lovdatas åpne data og API gir maskinlesbar tilgang til norsk regelverk. Den åpne delen består av gratis datapakker med konsoliderte, gjeldende lover og sentrale forskrifter, og med kunngjøringene i Norsk Lovtidend avdeling I og II fra 2001. Dokumentene leveres i Lovdatas XML-kompatible HTML-format med struktur for kapitler, paragrafer og ledd, og kan lastes ned uten brukerkonto.

Lovdata er en privat stiftelse, opprettet i 1981 av Justisdepartementet og Det juridiske fakultet ved Universitetet i Oslo. Lovdata produserer og utgir Norsk Lovtidend på oppdrag fra Justis- og beredskapsdepartementet, og konsoliderer hele det norske regelverket fortløpende. De konsoliderte tekstene er Lovdatas eget redaksjonelle arbeid.

API-et har også endepunkter for oppslag, søk, strukturert regelverk med versjoner og KI-funksjoner. Disse krever API-nøkkel og avtale med Lovdata.

## Kapabiliteter
Lovdata er den som konsoliderer regelverket og gjør de konsoliderte tekstene tilgjengelige som åpne data. `Datautveksling og integrasjon: Dele data med andre` er vurdert og ikke satt: den åpne delen er nedlastbare datapakker, mens API-endepunktene for oppslag og spørringer krever avtale. `Juridisk samhandling: Regelverkstolkning` er vurdert og ikke satt: Lovdata konsoliderer og publiserer regelverket, men tolker det ikke.

- **Datakilder: Åpne data** Lovdata publiserer konsoliderte, gjeldende lover og sentrale forskrifter og kunngjøringene i Norsk Lovtidend som maskinlesbare datapakker under NLOD 2.0, oppdatert hver natt og tilgjengelige for alle uten registrering.

## Produktmål
**Fakta:** Lovdata oppgir at formålet med å åpne gjeldende og konsoliderte lover er å gjøre det enkelt å finne ut hvilke lover og regler som gjelder i dag, og at de åpne dataene er et gratis tilbud for alle som vil bruke det konsoliderte regelverket i egne systemer og tjenester, til innovasjon eller forskning (api.lovdata.no, FAQ). Stiftelsens formål er å opprette, vedlikeholde og drive systemer for rettslig informasjon (lovdata.no, Om Lovdata).

**Deduksjon:** Det operative målet er at regelverket kan brukes direkte i andre løsninger, for eksempel saksbehandlingssystemer, søketjenester og KI-assistenter, uten at hver aktør må hente og strukturere regelverket selv.

## Brukerbehov
Virksomheter som lager saksbehandlingssystemer, veiledningstjenester og KI-løsninger, trenger oppdatert og strukturert regelverk de kan bygge inn i egne løsninger. Uten et maskinlesbart datagrunnlag må regelverket hentes manuelt eller skrapes fra nettsider, med risiko for at løsningen bygger på utdatert tekst.

Forskning og analysemiljøer trenger regelverket som datasett for analyser av regelverksutvikling, språk og struktur.

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter | Oppdatert regelverk i egne løsninger | Saksbehandling, veiledning, regelverksforvaltning | Lovdata viser Direktoratet for byggkvalitet, Lånekassen og NAV som brukereksempler |
| Leverandører og næringsliv | Regelverk som grunnlag for produkter og tjenester | Juridiske verktøy, søk, KI-assistenter | Flere endepunkter tilbys mot betaling til innovasjonsformål |
| Forskning | Regelverket som datasett | Juridisk og språklig forskning, KI-eksperimenter | Lovdata oppfordrer til fri bruk til eksperimentering og forskning med KI |
| Utviklere | Strukturert tekst og metadata | Integrasjon og visning av regelverk | Ingen brukerstøtte uten SLA-avtale |

## Hovedfunksjoner
Den første hovedfunksjonen er **åpne datapakker med gjeldende regelverk**. Lovdata tilbyr to gratis pakker, én med gjeldende lover og én med gjeldende sentrale forskrifter, ajourført med endringer. Pakkene lastes ned som komprimerte arkiver uten brukerkonto eller autentisering, og nye pakker legges ut hver natt.

Den andre er **åpne datapakker med Norsk Lovtidend**. API-et gir pakker med avdeling I, lover og sentrale forskrifter, og avdeling II, lokale forskrifter, for perioden fra 2001 og for inneværende år. Datasettet for avdeling I er også beskrevet i Felles datakatalog med Stiftelsen Lovdata som utgiver.

Den tredje er **strukturert format og metadata**. Dokumentene leveres i Lovdatas XML-kompatible HTML-format med struktur for kapitler, paragrafer og ledd. Dokumentidentifikatorene skiller mellom verket og de enkelte utgavene, for eksempel den kunngjorte loven i Lovtidend, den konsoliderte loven og den engelske oversettelsen.

Den fjerde er **avtalebaserte API-tjenester**. Med API-nøkkel og avtale gir API-et blant annet oppslag og søk i alle rettskilder, nedlasting av dokumenter i flere formater, historikk og versjoner av strukturert regelverk, detaljerte endringer i enkeltbestemmelser, gjenkjenning av henvisninger i tekst og KI-funksjoner for søk og svar. Bruken er begrenset av et fast antall kall per minutt.

### Typiske brukssituasjoner (generisk)
- bygge gjeldende lover og forskrifter inn i et saksbehandlings- eller veiledningssystem
- bruke regelverket som kunnskapsgrunnlag for en KI-assistent eller et søk
- analysere regelverket som datasett i forskning
- følge med på nye kunngjøringer i Norsk Lovtidend

### Når Lovdatas åpne data normalt ikke er førstevalg
De åpne dataene er ikke førstevalg når løsningen trenger historiske eller opphevede regler, versjonen som gjaldt på en bestemt dato, rettsavgjørelser, forarbeider eller juridisk litteratur. Dette ligger i Lovdata Pro og i de avtalebaserte endepunktene. De åpne dataene er heller ikke førstevalg for løsninger som trenger brukerstøtte eller leveransegaranti, siden det krever SLA-avtale.

### Scope og avgrensning
Inngår:
- gratis datapakker med gjeldende lover og gjeldende sentrale forskrifter
- gratis datapakker med Norsk Lovtidend avdeling I og II fra 2001
- API-dokumentasjon og endepunkter for å liste og hente de åpne pakkene

Inngår ikke:
- Lovdata Pro og nettstedet lovdata.no som brukertjenester
- historisk og opphevet regelverk, rettsavgjørelser, forarbeider og litteratur
- avtalebaserte endepunkter for søk, oppslag, strukturert regelverk og KI, som krever API-nøkkel
- lokale forskrifter i konsolidert form

## Veikart over kommende funksjonalitet
**Fakta:** Lovdata oppgir at API-et er under stadig utvikling, og at flere endepunkter og datakilder tilbys mot betaling til innovasjonsformål (api.lovdata.no, Om API-tjenesten). Endringer som kan bryte bakoverkompatibilitet, skal bare komme i nye versjoner av API-et med egne adresser (api.lovdata.no, Swagger).

**Ikke offentlig dokumentert i denne arbeidsøkten:** Planer om å utvide den åpne, gratis delen.

## Forretningsverdi/Verdiforslag
For offentlige virksomheter ligger verdien i at regelverket kan brukes direkte i egne løsninger, oppdatert hver natt, uten egen innsamling og strukturering.

For næringsliv og leverandører ligger verdien i et åpent datagrunnlag med lisens som tillater kommersiell bruk, slik at nye juridiske tjenester og KI-løsninger kan bygges på det konsoliderte regelverket.

For forskning ligger verdien i at hele det gjeldende regelverket og Lovtidend fra 2001 er tilgjengelig som datasett.

For innbyggere ligger verdien indirekte i at tjenester som viser eller bygger på regelverket, kan bruke samme oppdaterte tekst som lovdata.no.

## Utfordringer og risiko

| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Leveransesikkerhet | Ingen brukerstøtte eller leveransegaranti for den åpne delen | Support og vedlikehold tilbys bare gjennom betalt SLA-avtale |
| Omfang | De åpne dataene omfatter bare gjeldende regelverk og Lovtidend | Historikk, rettsavgjørelser og forarbeider krever avtale eller Lovdata Pro |
| Juridisk | Konsoliderte tekster er Lovdatas redaksjonelle arbeid, og Lovdata krever kreditering | Kildeangivelse må bygges inn i løsninger som bruker dataene |
| Juridisk | Lisensen for Lovtidend avdeling II er ikke uttrykkelig oppgitt | Ikke offentlig dokumentert i denne arbeidsøkten |
| Finansiering | Lovdata mottar ikke offentlige midler, og den åpne delen er finansiert av betalte tjenester | Uavklart hvordan dette påvirker den åpne delen over tid |
| Kvalitet | Den konsoliderte teksten er ikke den offisielle kunngjøringen | Den offisielle kunngjøringen skjer i Norsk Lovtidend, som også er tilgjengelig som åpne data |

## Kanaler
**Maskinell kanal:** API på api.lovdata.no. De åpne datapakkene hentes uten innlogging. Øvrige endepunkter krever API-nøkkel i HTTP-headeren `X-API-Key` eller Basic Auth mot en bruker med API-rolle hos Lovdata.

**Katalog:** Datasettet Norsk Lovtidend avdeling I er beskrevet i Felles datakatalog og kan finnes på data.norge.no.

**Brukerflate:** lovdata.no er Lovdatas åpne nettsted for lover, forskrifter og nyere rettsavgjørelser, og Lovdata Pro er den betalte tjenesten for profesjonelle brukere. Ingen av dem er del av denne ressursen.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** Driftsmodell og plattform for Lovdata API.

## Gjenbruk
Dataene er laget for gjenbruk: åpen lisens, strukturert format og nattlige oppdateringer. Gjenbruket har to vilkår brukeren må ta inn i egen løsning: kreditering av Lovdata, og bevissthet om at de åpne dataene viser gjeldende regelverk og ikke tidligere versjoner.

### Vanlige kombinasjoner med andre produkter
- `DIGDIR-014` data.norge.no, der datasettet for Norsk Lovtidend avdeling I er katalogisert og kan finnes sammen med andre åpne offentlige datasett.

**Kildekode:** Proprietær. Kildekoden for API-et er ikke funnet publisert.

**Lisens:** Ikke relevant for kildekoden. Dataene er lisensiert under `NLOD-2.0`.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Regelverket deles som åpne, maskinlesbare data under NLOD 2.0, slik at andre kan bygge på samme oppdaterte tekst.

- **P3: Bidra til digitaliseringsvennlige regelverk**
  Støttes delvis. Strukturert regelverk med kapitler, paragrafer og ledd gjør det lettere å koble regler til systemer, men ressursen påvirker ikke hvordan regelverket utformes.

- **P5: Del og gjenbruk løsninger**
  Støttes delvis. Mange aktører kan bruke samme datagrunnlag i stedet for å strukturere regelverket selv, men avanserte funksjoner krever avtale.

Spenningen ligger mellom åpenhet og finansiering. Lovdata er en privat stiftelse uten offentlige midler, og holder historisk regelverk, rettsavgjørelser og de mest avanserte API-funksjonene i betalte tjenester for å finansiere driften. Den åpne delen er derfor avgrenset til gjeldende regelverk og Lovtidend, uten brukerstøtte, og løsninger som trenger regelverket på et bestemt tidspunkt eller med rettspraksis, blir avhengige av en avtale med én leverandør.

## Finansiering
**Fakta:** De åpne datapakkene er gratis. Lovdata er selvfinansierende og mottar ikke offentlige midler. Driften finansieres hovedsakelig av tjenesten for profesjonelle brukere, i tillegg til regeltilsyn og produksjon av trykkeklar tekst (lovdata.no, Om Lovdata; api.lovdata.no, FAQ). Support- og vedlikeholdsavtaler og flere endepunkter tilbys mot betaling.

## Forvaltning/eier

| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Stiftelsen Lovdata | api.lovdata.no, Om API-tjenesten |
| Driftsansvar | Stiftelsen Lovdata | api.lovdata.no |
| Budsjettansvar | Stiftelsen Lovdata, uten offentlige midler | lovdata.no, Om Lovdata |
| Styringsmodell | Privat stiftelse med styre med representanter for Det juridiske fakultet ved Universitetet i Oslo, Abelia, Stortinget, Justis- og beredskapsdepartementet, Den norske dommerforening, Advokatforeningen og de ansatte | lovdata.no, Om Lovdata |
| Oppdrag for staten | Lovdata produserer og utgir Norsk Lovtidend på oppdrag fra Justis- og beredskapsdepartementet | api.lovdata.no, Om API-tjenesten |

**Ikke offentlig dokumentert i denne arbeidsøkten:** Avtalen mellom Justis- og beredskapsdepartementet og Lovdata om Norsk Lovtidend, og om den regulerer de åpne dataene.

## Lenke til dokumentasjon
- Om API-tjenesten: https://api.lovdata.no/om-api-tjenesten/
- API-dokumentasjon: https://api.lovdata.no/swagger/index.html
- Spørsmål og svar: https://api.lovdata.no/faq/
- SLA: https://api.lovdata.no/sla/
- Norsk Lovtidend avdeling I i Felles datakatalog: https://data.norge.no/datasets/c0c6a87c-f597-3735-965f-650be23426a0
- Om Lovdata: https://lovdata.no/info/om_lovdata
- NLOD 2.0: https://data.norge.no/nlod/no/2.0

## Kildegrunnlag brukt i utfyllingen
Hentet 2026-10-25:
- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/prinsipper/principles.md`
- `arkitektur/ressurser/produktnummerering.md`
- Lovdata API, forside: https://api.lovdata.no/
- Lovdata API, Om API-tjenesten: https://api.lovdata.no/om-api-tjenesten/
- Lovdata API, FAQ: https://api.lovdata.no/faq/
- Lovdata API, SLA: https://api.lovdata.no/sla/
- Lovdata API, OpenAPI-beskrivelse: https://api.lovdata.no/swagger/index.html
- Lovdata API, liste over åpne datapakker: https://api.lovdata.no/v1/publicData/list
- Lovdata, Om Lovdata: https://lovdata.no/info/om_lovdata
- Felles datakatalog, Norsk Lovtidend avdeling I: https://data.norge.no/datasets/c0c6a87c-f597-3735-965f-650be23426a0
- Enhetsregisteret, Stiftelsen Lovdata (org.nr. 934282744): https://data.brreg.no/enhetsregisteret/api/enheter/934282744
