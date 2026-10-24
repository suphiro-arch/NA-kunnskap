# SSB Statistikkbanken og PxWebApi

## Navn
Statistikkbanken og PxWebApi – Statistisk sentralbyrås statistikkbank med åpent API

## Ressurs ID
SSB-003

## Status/Livsfase
**Produksjon** – ny Statistikkbank og PxWebApi v2 i drift, med v1 i overgangsperiode.

**Fakta:** PxWebApi v2 ble lansert høsten 2025 og er utviklet i samarbeid med Statistiska centralbyrån (SCB) i Sverige (ssb.no/api/pxwebapi). SCB oppgir at API-et ble lansert i deres statistikkdatabase i oktober 2025 (scb.se). Ny Statistikkbank ble lansert 29. januar 2026 (ssb.no/en/api).

**Fakta:** PxWebApi v1 er fortsatt tilgjengelig i en overgangsperiode, og SSB anbefaler at spørringer defineres på nytt i v2. Det er ikke oppgitt noen sluttdato for v1 (ssb.no/api/pxwebapi).

## Modenhet
**Høy modenhet som publiseringskanal for statistikk, med en pågående versjonsovergang.**

- API-et gir tilgang til alle om lag 7 500 tabeller i Statistikkbanken, uten registrering (ssb.no/en/api).
- Grensene er dokumentert: inntil 800 000 dataceller per uttrekk og 30 spørringer per minutt per IP-adresse (ssb.no/api/pxwebapiv2).
- Dataene leveres i flere standardformater, med JSON-stat2 som standard (ssb.no/api/pxwebapiv2).
- Kildekoden er åpen og vedlikeholdes aktivt i et felles repositorium (GitHub, PxTools/PxWebApi, siste endring oktober 2026).
- v2 er ikke bakoverkompatibel med v1 (scb.se).

**Deduksjon:** Det svakeste leddet er versjonsovergangen. Integrasjoner bygget på v1 må skrives om, og uten oppgitt sluttdato for v1 er det uklart hvor lang tid brukerne har. Lagrede spørringer fra v1 oppfører seg også annerledes i v2, blant annet ved at de ikke gir CSV eller Excel som utformat (ssb.no/api/pxwebapiv2).

## Kort beskrivelse
Statistikkbanken er Statistisk sentralbyrås (SSB) publiseringsbase for offisiell statistikk, med om lag 7 500 tabeller om befolkning, økonomi, arbeidsliv, offentlig sektor og andre samfunnsområder. Tabellene kan brukes i nettgrensesnittet på ssb.no eller hentes maskinelt gjennom PxWebApi.

PxWebApi er et åpent API uten registrering. Brukerne kan hente hele eller deler av en tabell, med metadata og kodelister, i formater som JSON-stat2, CSV, Excel og PX. Dataene er lisensiert under CC BY 4.0.

Ressursen dekker publisert, aggregert statistikk. Mikrodata for forskning tilbys gjennom `SSB-001` microdata.no, og rapporteringen fra kommunesektoren gjennom `SSB-002` KOSTRA, som publiserer sine tall i Statistikkbanken.

## Kapabiliteter
SSB er den sentrale produsenten av offisiell statistikk, og Statistikkbanken med PxWebApi er kanalen den publiseres gjennom. Uten ressursen ville ingen annen kilde gitt samlet, maskinlesbar tilgang til den offisielle statistikken.

- **Datakilder: Åpne data** Statistikkbanken publiserer SSBs offisielle statistikk som åpne data under CC BY 4.0, og PxWebApi gjør alle tabellene maskinelt tilgjengelige uten registrering.

## Produktmål
**Fakta:** SSB oppgir at PxWebApi v2 gir tilgang til alle tabellene i Statistikkbanken, og at v2 er mer robust mot endringer i tabellene fordi spørringer kan be om alle koder innenfor en verdimengde eller gruppering (ssb.no/api/pxwebapi; ssb.no/en/api).

**Deduksjon:** Målet med v2 er å gjøre maskinell bruk av statistikken mer stabil over tid, slik at integrasjoner ikke brytes når SSB legger til nye perioder eller endrer inndelinger. Det følger av at SSB framhever robusthet mot tabellendringer som hovedgrunn til å gå over til v2.

## Brukerbehov
Virksomheter, forskere og utviklere trenger offisiell statistikk som grunnlag for analyse, styring og tjenester. Uten et maskinelt grensesnitt måtte tabellene lastes ned manuelt og oppdateres for hånd hver gang SSB publiserer nye tall.

PxWebApi dekker behovet for å hente den samme statistikken som vises på ssb.no direkte inn i egne systemer, med metadata som forklarer variabler, koder og enheter.

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter | Offisiell statistikk i egne systemer og rapporter | Styringsdata, planlegging, dashbord | Unngår manuell nedlasting |
| Kommuner og fylkeskommuner | Sammenlignbare tall om egen befolkning og tjenester | Planarbeid, oversikter, KOSTRA-sammenligning | KOSTRA-tallene ligger i Statistikkbanken |
| Forskere og analysemiljøer | Tidsserier og tverrsnittsdata på aggregert nivå | Analyse og forskning | Mikrodata går gjennom `SSB-001` microdata.no |
| Utviklere og tredjeparter | Stabilt, åpent API | Visualiseringer, apper, datatjenester | CC BY 4.0, ingen registrering |
| Presse og innbyggere | Oppslag i offisiell statistikk | Journalistikk, innsyn | Bruker i hovedsak nettgrensesnittet |

## Hovedfunksjoner
Den første hovedfunksjonen er **Statistikkbanken som publiseringsbase**. SSB publiserer offisiell statistikk som tabeller med variabler, kodelister og tidsperioder. Tabellene kan filtreres og lastes ned i nettgrensesnittet på ssb.no. SSB fører en oversikt over endringer i tabellene, blant annet når tabeller erstattes eller avsluttes, og brukere kan be om e-postvarsel om slike endringer.

Den andre er **maskinell henting gjennom PxWebApi v2**. API-et har egne endepunkter for å liste tabeller, hente metadata for en tabell, hente data og bruke lagrede spørringer og kodelister. Spørringer kan uttrykkes direkte i URL-en med GET eller som POST. Dataene leveres som JSON-stat2, CSV, PX, Excel, HTML eller JSON-PX, og Parquet er tilgjengelig i betaversjon.

Den tredje er **robuste spørringer over tid**. I v2 kan en spørring be om alle verdier eller perioder i en verdimengde eller gruppering. Da fanges nye perioder opp automatisk, i stedet for at spørringen må endres hver gang tabellen oppdateres.

Den fjerde er **overgangen fra v1**. PxWebApi v1 er tilgjengelig i en overgangsperiode. v2 er ikke bakoverkompatibel, men SCB tilbyr en konverterer som oversetter spørringer fra v1 til v2.

### Typiske brukssituasjoner (generisk)
- hente befolknings-, nærings- eller økonomistatistikk automatisk inn i egne dashbord og rapporter
- holde tidsserier oppdatert i analysemodeller uten manuell nedlasting
- bygge visualiseringer eller tjenester på offisiell statistikk
- hente KOSTRA-tall maskinelt for sammenligning av kommuner

### Når SSB Statistikkbanken og PxWebApi normalt ikke er førstevalg
Ressursen er ikke førstevalg når analysen trenger data på individnivå eller kobling mellom registre. Da er `SSB-001` microdata.no rett kanal.

Den er heller ikke en kanal for innrapportering til SSB. Kommunesektorens rapportering skjer gjennom `SSB-002` KOSTRA, og Statistikkbanken er bare der tallene publiseres.

Den er ikke egnet for svært store uttrekk i én operasjon. Grensen på 800 000 celler per uttrekk og 30 spørringer per minutt betyr at store datamengder må deles opp.

### Scope og avgrensning
Inngår:
- Statistikkbanken med publiserte tabeller fra SSB
- PxWebApi v2 og v1 i overgangsperioden
- metadata, kodelister og lagrede spørringer

Inngår ikke:
- mikrodata og analyseplattform, som tilbys gjennom `SSB-001` microdata.no
- innrapportering fra kommunesektoren, som skjer gjennom `SSB-002` KOSTRA
- SSBs API for klassifikasjoner og kodelister (Klass), som er et eget API
- statistikkbanker hos andre virksomheter

## Veikart over kommende funksjonalitet
**Fakta:** v1 skal fases ut etter en overgangsperiode, og SSB anbefaler at brukerne definerer spørringene sine på nytt i v2 (ssb.no/api/pxwebapi). Parquet som utformat er i betaversjon (ssb.no/api/pxwebapiv2).

**Ikke offentlig dokumentert:** Sluttdato for v1, og plan for videre utvikling av v2 utover det som framgår av repositoriet.

## Forretningsverdi/Verdiforslag
For offentlige virksomheter ligger verdien i at offisiell statistikk kan hentes rett inn i styrings- og planleggingsverktøy, og holdes oppdatert uten manuelt arbeid.

For forskning og analyse ligger verdien i reproduserbar tilgang til lange tidsserier med metadata, i standardformater som støttes av vanlige analyseverktøy.

For næringsliv og utviklere ligger verdien i et åpent API uten registrering og en lisens som tillater fri bruk mot kreditering.

For samfunnet ligger verdien i åpenhet: den samme offisielle statistikken er tilgjengelig for alle, både i nettgrensesnittet og maskinelt.

## Utfordringer og risiko

| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Versjonsovergang | Integrasjoner mot v1 må skrives om, og v2 er ikke bakoverkompatibel | SCB tilbyr konverterer fra v1 til v2. Sluttdato for v1 er ikke oppgitt |
| Teknisk | Store uttrekk avvises over 800 000 celler, og over 30 spørringer per minutt gir HTTP 429 | Uttrekk må deles opp |
| Tabellendringer | Tabeller kan erstattes eller avsluttes, slik at faste integrasjoner brytes | SSB publiserer endringer i tabellene og sender varsel på e-post etter avtale |
| Lagrede spørringer | Lagrede spørringer fra v1 gir ikke CSV eller Excel i v2 | Beskrevet i SSBs veiledning for v2 |
| Leveransesikkerhet | Ingen tjenestenivåavtale er funnet | Ikke offentlig dokumentert |

## Kanaler
Statistikkbanken er tilgjengelig på ssb.no uten innlogging. PxWebApi er åpent uten registrering eller nøkkel, og bruker GET- og POST-forespørsler. Endringer i tabeller publiseres på ssb.no, og brukere kan få varsel på e-post ved å melde seg på hos SSB. Spørsmål går til statistikkbanken@ssb.no.

## Plattform
**Fakta:** PxWebApi er skrevet i C# og publisert som åpen kildekode (GitHub, PxTools/PxWebApi).

**Ikke offentlig dokumentert:** Driftsmodell og plattform for SSBs installasjon av Statistikkbanken og PxWebApi.

## Gjenbruk
Statistikken er åpen under CC BY 4.0, og API-et er fritt tilgjengelig. Programvaren er utviklet sammen med SCB og publisert som åpen kildekode, og SCB tilbyr PxWebApi v2 for sin egen statistikkdatabase.

**Deduksjon:** Fordi begge byråene bruker samme API-versjon, kan klienter og verktøy laget for den ene i stor grad brukes mot den andre. Dette er ikke kontrollert i praksis.

### Vanlige kombinasjoner med andre produkter
- `SSB-002` KOSTRA, som publiserer kommunale nøkkeltall i Statistikkbanken.
- `SSB-001` microdata.no, når analysen trenger mikrodata i tillegg til publisert statistikk.
- SSBs API for klassifikasjoner og kodelister (Klass), for koder og inndelinger som brukes i tabellene.
- `DIGDIR-014` data.norge.no, som felles katalog for å finne åpne offentlige datasett.

**Kildekode:** Åpen kildekode for PxWebApi.

**Lisens:** `Apache-2.0`, kontrollert mot `LICENSE.md` i repositoriet 2026-10-23. Dataene er lisensiert under CC BY 4.0, som gjelder data, ikke kildekode.

**Repositorium:** https://github.com/PxTools/PxWebApi

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Offisiell statistikk deles åpent og maskinlesbart, med metadata og fri lisens.

- **P5: Del og gjenbruk løsninger**
  PxWebApi er utviklet sammen med SCB og publisert som åpen kildekode, slik at andre kan ta i bruk samme løsning.

- **P6: Lag digitale løsninger som støtter samhandling**
  Støttes delvis. API-et gjør statistikken lett å bygge inn i andre systemer, men samhandlingen er enveis og uten avtalefestet leveransenivå.

Spenningen ligger i versjonsovergangen. v2 er mer robust enn v1, men er ikke bakoverkompatibel, og sluttdato for v1 er ikke oppgitt. Det flytter kostnaden ved overgangen over på brukerne og gjør det vanskelig å planlegge når den må tas. Grensene for uttrekk og spørringer begrenser også bruken til moderate datamengder per kall.

## Finansiering
**Ikke offentlig dokumentert:** Hvordan Statistikkbanken og PxWebApi finansieres. Kildene skiller ikke ressursen ut fra SSBs øvrige virksomhet.

**Fakta:** Bruken er gratis og uten registrering (ssb.no/en/api).

## Forvaltning/eier

| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Statistisk sentralbyrå (SSB) | ssb.no/api/pxwebapi, ssb.no/en/api |
| Driftsansvar | SSB, for egen installasjon av Statistikkbanken og API-et | ssb.no/en/api |
| Utvikling av PxWebApi v2 | SSB og SCB i samarbeid | ssb.no/api/pxwebapi, scb.se |
| Budsjettansvar | Ikke offentlig dokumentert | – |
| Styringsmodell | Ikke offentlig dokumentert for samarbeidet med SCB | – |

## Lenke til dokumentasjon
- PxWebApi hos SSB: https://www.ssb.no/api/pxwebapi
- Veiledning for PxWebApi v2: https://www.ssb.no/api/pxwebapiv2
- API-oversikt på engelsk: https://www.ssb.no/en/api
- PxWebApi v2 hos SCB, med konverterer: https://www.scb.se/vara-tjanster/oppna-data/pxwebapi/pxwebapi-v2/
- Kildekode: https://github.com/PxTools/PxWebApi

## Kildegrunnlag brukt i utfyllingen
Hentet 2026-10-23:
- SSB, PxWebApi: https://www.ssb.no/api/pxwebapi
- SSB, Veiledning for PxWebApi v2: https://www.ssb.no/api/pxwebapiv2
- SSB, API: https://www.ssb.no/en/api
- SCB, PxWebApi v2: https://www.scb.se/vara-tjanster/oppna-data/pxwebapi/pxwebapi-v2/
- GitHub, PxTools/PxWebApi: https://github.com/PxTools/PxWebApi

Lokale kilder:
- `arkitektur/ressurser/operative-losninger-og-tjenester/169-KOSTRA-v1-claude.md`
