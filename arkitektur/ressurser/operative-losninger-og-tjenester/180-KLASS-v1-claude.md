# KLASS

## Navn
KLASS – Statistisk sentralbyrås system for klassifikasjoner og kodelister

## Ressurs ID
SSB-004

## Status/Livsfase
**Produksjon** – KLASS-API v1 og ny nettflate i SSBs dataportal er i drift.

**Fakta:** KLASS-API v1 svarer uten autentisering, og API-veiledningen ble sist oppdatert 23. oktober 2026 (data.ssb.no/api/klass/v1/api-guide.html). Den tidligere nettadressen ssb.no/klass videresendes til SSBs dataportal, der klassifikasjoner og kodelister vises (dataportal.ssb.no/classifications, kontrollert 2026-10-24).

**Fakta:** Dataportalen omtaler seg selv som en første versjon som skal utvides gradvis (dataportal.ssb.no/classifications).

## Modenhet
**Høy modenhet som innholds- og API-tjeneste, med en ny nettflate og en varslet endring i API-et.**

- KLASS inneholder 152 klassifikasjoner og 616 kodelister (dataportal.ssb.no/classifications; samme tall fra API-et med og uten `includeCodelists`, kontrollert 2026-10-24).
- Innholdet er versjonert. En ny versjon opprettes når kodeverket endres vesentlig, slik regionreformene i 2020 og 2024 ga nye versjoner av blant annet Standard for kommuneinndeling (ssb.no/metadata/om-klass).
- API-et er dokumentert med egne ressurser for klassifikasjoner, versjoner, varianter, korrespondanser og endringer, og dataene er lisensiert under CC BY 4.0 (data.ssb.no/api/klass/v1/api-guide.html).
- Kildekoden er åpen under Apache-2.0 og vedlikeholdes aktivt (GitHub, statisticsnorway/klass, siste endring 23. oktober 2026).
- Valg av format med filendelse i URL-en (`.json`, `.csv`, `.xml`) er varslet fjernet, uten oppgitt dato (data.ssb.no/api/klass/v1/api-guide.html).

**Deduksjon:** Det svakeste leddet er forutsigbarheten i endringer. Fjerningen av filendelser er varslet uten dato, og klienter som bruker dem vil slutte å virke når endringen gjennomføres. Dataportalen er dessuten ny og beskrevet som en første versjon. Innholdet og API-et er etablert, mens nettflaten er i endring.

## Kort beskrivelse
KLASS er Statistisk sentralbyrås (SSB) system for å dokumentere og publisere klassifikasjoner og kodelister. Eksempler er Standard for kommuneinndeling, Standard for næringsgruppering (SN), Standard for yrkesklassifisering, Standard for sivilstand og Standard for landkoder. Formålet er at statistikk skal bli sammenlignbar over tid og på tvers av fagområder.

KLASS skiller mellom to typer kodeverk. Klassifikasjoner er offisielle, navnene begynner med «Standard for», og kategoriene skal være gjensidig utelukkende og dekke hele området de beskriver. Kodelister er ikke offisielle og kan være tilpasset én bestemt statistikk. For hvert kodeverk viser KLASS gjeldende koder, alle versjoner, endringer fra forrige versjon, varianter med alternative grupperinger og korrespondanser mot andre kodeverk.

Kodeverkene er tilgjengelige i SSBs dataportal og gjennom et åpent API uten autentisering. Dataene er lisensiert under CC BY 4.0.

Ressursen dekker kodeverkene som brukes i statistikken. Selve statistikken publiseres gjennom `SSB-003` Statistikkbanken og PxWebApi, mikrodata gjennom `SSB-001` microdata.no, og kommunesektorens rapportering gjennom `SSB-002` KOSTRA.

## Kapabiliteter
KLASS er stedet der SSB forvalter og publiserer kodeverkene som offisiell statistikk bygger på. Kodeverkene brukes også utenfor SSB, men det er KLASS som holder versjonene, endringene og koblingene mellom dem.

- **Informasjonsforvaltning: Informasjonsarkitektur** KLASS strukturerer kodeverk etter en felles modell med versjoner, gyldighetsperioder, varianter og korrespondanser, slik at koder kan tolkes entydig på et gitt tidspunkt og oversettes mellom inndelinger.
- **Standardisering: Forvaltningsstandarder** KLASS publiserer SSBs offisielle klassifikasjoner, som Standard for kommuneinndeling og Standard for næringsgruppering, i maskinlesbar form, slik at virksomheter kan ta standardene i bruk direkte i egne systemer.
- **Datakilder: Åpne data** KLASS gjør alle klassifikasjoner og kodelister fritt tilgjengelige under CC BY 4.0, både i dataportalen og gjennom et åpent API uten registrering.

## Produktmål
**Fakta:** SSB oppgir at KLASS skal bidra til at statistikk kan sammenlignes over tid og på tvers av fagområder, ved at kodeverkene statistikken bygger på dokumenteres samlet (ssb.no/metadata/om-klass).

**Fakta:** Statistikkloven § 5 andre ledd krever at offisiell statistikk utvikles, utarbeides og formidles på grunnlag av enhetlige standarder og harmoniserte metoder, og § 6 første ledd gir SSB ansvar for å samordne all utvikling, utarbeiding og formidling av offisiell statistikk i Norge (lovdata.no, lov 2019-06-21-32). Loven sier ikke uttrykkelig at SSB skal fastsette klassifikasjoner.

**Deduksjon:** KLASS er et verktøy for å oppfylle kravet om enhetlige standarder og SSBs samordningsansvar. Koblingen er SSBs egen arbeidsdeling, ikke en oppgave loven tildeler KLASS.

## Brukerbehov
Statistikk og registerdata kan bare sammenlignes når de bruker samme koder for kommuner, næringer, yrker, land og andre inndelinger. Kodeverkene endres over tid, blant annet ved kommunesammenslåinger, og den som sammenstiller data fra ulike år eller kilder trenger å vite hvilken kode som gjaldt når, og hvordan gamle og nye koder henger sammen.

KLASS dekker behovet for én autoritativ kilde til SSBs kodeverk, med historikk og korrespondanser, som både mennesker og systemer kan slå opp i.

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| SSB internt | Felles kodeverk i statistikkproduksjonen | Koding, publisering, kobling til variabler i Statistikkbanken | KLASS er lenket fra variabler i Statistikkbanken |
| Virksomheter som rapporterer til SSB | Riktige koder i innrapportering | KOSTRA-rapportering, rapportering av stillinger med yrkeskatalogen | SSB nevner yrkeskatalogen og KOSTRA-kodelister som eksempler |
| Offentlige virksomheter og systemleverandører | Oppdaterte standardkoder i egne systemer | Kommune- og fylkesnummer, næringskoder, landkoder i fagsystemer og registre | **Deduksjon:** Hvilke virksomheter som henter kodeverk fra KLASS, er ikke kontrollert |
| Forskere og analysemiljøer | Historiske koder og omkodinger | Tidsserier på tvers av kommunereformer og standardrevisjoner | Korrespondanser og endringer er tilgjengelige i API-et |
| Utviklere og tredjeparter | Åpent API med fri lisens | Oppslagstjenester, nedtrekkslister, datavask | CC BY 4.0, ingen autentisering |

## Hovedfunksjoner
Den første hovedfunksjonen er **forvaltning og publisering av kodeverk**. SSB dokumenterer klassifikasjoner og kodelister i KLASS, med navn, koder, beskrivelser, ansvarlig seksjon og endringslogg. Kodeverkene er gruppert i 22 familier, som Befolkning, Region, Utdanning og Arbeid og lønn. SSB vedlikeholder innholdet i et internt forvaltningsverktøy, mens alle andre har lesetilgang.

Den andre er **versjoner og endringer over tid**. Hvert kodeverk har gyldige versjoner med start- og sluttdato. API-et kan levere kodene slik de var på en bestemt dato (`codesAt`) eller over et tidsrom (`codes`), og kan liste kodeendringer innenfor en periode (`changes`). Det gjør det mulig å bruke riktig kodeverk for historiske data uten å holde egne kopier.

Den tredje er **varianter og korrespondanser**. En variant er en alternativ gruppering av en klassifikasjonsversjon, for eksempel land gruppert etter verdensdel. En korrespondanse viser hvordan koder i én versjon svarer til koder i en annen versjon eller et annet kodeverk, for eksempel kommuner mot politidistrikter. Begge er tilgjengelige i nettflaten og i API-et.

Den fjerde er **tilgang gjennom dataportal og API**. I SSBs dataportal kan brukerne søke og filtrere på type og fagområde. SSB oppgir at kodeverk kan lastes ned som CSV fra nettflaten. KLASS-API v1 er et lese-API uten autentisering. Dokumentasjonen oppgir XML som standardformat, JSON som alternativ og CSV for mange av ressursene, valgt med `Accept`-headeren. Å velge format med filendelse i URL-en er varslet fjernet. CSV leveres som standard i ISO-8859-1, men kan bestilles i UTF-8.

**Fakta:** En forespørsel uten bestemt format (`Accept: */*`) ga JSON ved kontroll 2026-10-24. Klienter bør derfor alltid oppgi ønsket format eksplisitt.

### Typiske brukssituasjoner (generisk)
- hente gjeldende kommune- og fylkesinndeling inn i fagsystemer og registre
- omkode historiske data til ny kommunestruktur med korrespondanser og endringslister
- bruke Standard for næringsgruppering eller yrkesklassifisering ved koding av data
- slå opp hva en kode betydde på et bestemt tidspunkt
- bruke KOSTRA-kodelister ved innrapportering til SSB

### Når KLASS normalt ikke er førstevalg
KLASS er ikke en kilde til statistikk. Tall hentes fra `SSB-003` Statistikkbanken og PxWebApi, og mikrodata fra `SSB-001` microdata.no.

KLASS er heller ikke en katalog over begrepsdefinisjoner eller datasett for hele offentlig sektor. Begreper publiseres i `DIGDIR-012` Begrepskatalog, og datasett, API-er og informasjonsmodeller finnes gjennom `DIGDIR-011` Felles datakatalog og `DIGDIR-014` data.norge.no.

KLASS dekker SSBs kodeverk. Kodeverk som forvaltes av andre virksomheter, er ikke nødvendigvis med, og kodelistene i KLASS er ikke offisielle standarder.

### Scope og avgrensning
Inngår:
- SSBs klassifikasjoner og kodelister, med versjoner, varianter og korrespondanser
- visning i SSBs dataportal
- KLASS-API v1 med lesetilgang

Inngår ikke:
- publisert statistikk, som tilbys gjennom `SSB-003` Statistikkbanken og PxWebApi
- mikrodata, som tilbys gjennom `SSB-001` microdata.no
- innrapportering fra kommunesektoren, som skjer gjennom `SSB-002` KOSTRA
- definisjoner av begreper og variabler, som SSB publiserer i en egen tjeneste for variabeldefinisjoner, og begreper i `DIGDIR-012` Begrepskatalog
- SSBs interne forvaltningsverktøy for å vedlikeholde kodeverkene

## Veikart over kommende funksjonalitet
**Fakta:** Valg av format med filendelse i URL-en skal fjernes, og klienter må gå over til `Accept`-headeren (data.ssb.no/api/klass/v1/api-guide.html). Dataportalen skal utvides gradvis (dataportal.ssb.no/classifications).

**Ikke offentlig dokumentert i denne arbeidsøkten:** Dato for fjerning av filendelser, planer for en ny API-versjon og innholdet i videre utvikling av dataportalen.

## Forretningsverdi/Verdiforslag
For offentlige virksomheter ligger verdien i at standardkoder kan hentes fra én autoritativ kilde i stedet for å vedlikeholdes lokalt. Det reduserer risikoen for utdaterte kommunenummer og næringskoder etter reformer og revisjoner.

For forskning og analyse ligger verdien i historikken. Versjoner, endringer og korrespondanser gjør det mulig å sammenligne data på tvers av år og kodeverk uten egen omkodingsjobb.

For virksomheter som rapporterer til SSB ligger verdien i at kodene de skal bruke, er publisert åpent og maskinlesbart.

For utviklere og næringsliv ligger verdien i et åpent API uten registrering og en lisens som tillater fri bruk mot kreditering.

For SSB ligger verdien i at statistikken bygger på felles, dokumenterte kodeverk, i tråd med statistikklovens krav om enhetlige standarder.

## Utfordringer og risiko

| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Teknisk | Klienter som velger format med filendelse i URL-en, slutter å virke når funksjonen fjernes | Varslet i API-veiledningen. Dato er ikke oppgitt |
| Teknisk | Standardformat avhenger av `Accept`-headeren, og CSV leveres som ISO-8859-1 hvis ikke annet bes om | Oppgi format og tegnsett eksplisitt |
| Innhold | Kodelister er ikke offisielle og kan være tilpasset én statistikk, men ligger i samme system som klassifikasjonene | Skillet er markert med type i dataportalen og API-et |
| Endringer i kodeverk | Reformer gir nye versjoner, og systemer som kopierer koder uten å følge med, får utdaterte koder | API-et har endringsliste og datobaserte oppslag |
| Juridisk | Statistikkloven gir ikke uttrykkelig hjemmel for at SSB fastsetter klassifikasjoner | Klassifikasjonenes status utenfor offisiell statistikk er ikke avklart i kildene |
| Leveransesikkerhet | Ingen tjenestenivåavtale eller dokumenterte grenser for antall forespørsler er funnet | Ikke offentlig dokumentert i denne arbeidsøkten |

## Kanaler
KLASS er tilgjengelig i SSBs dataportal uten innlogging. Innlogging finnes bare for SSBs egne ansatte. Dataportalen har søk, filtrering på type og fagområde, og språkvalg for bokmål, nynorsk og engelsk.

KLASS-API v1 er åpent uten autentisering og leverer XML, JSON og CSV. Dokumentasjonen er på engelsk, og SSB har i tillegg en videoveiledning. Spørsmål om SSBs API-er går til statistikkbanken@ssb.no.

## Plattform
**Fakta:** KLASS er skrevet i Java med Spring Boot og bruker PostgreSQL og OpenSearch. Løsningen består av et API, et internt forvaltningsverktøy og en indekseringsjobb. Repositoriet oppgir at applikasjonene kjøres på applikasjonsplattformen Nais (GitHub, statisticsnorway/klass).

**Ikke offentlig dokumentert i denne arbeidsøkten:** Driftsmiljø og skyleverandør for SSBs installasjon.

## Gjenbruk
Kodeverkene er åpne under CC BY 4.0 og kan hentes fritt gjennom API-et. Mange av klassifikasjonene bygger på internasjonale klassifikasjoner fra Eurostat og FNs statistikkavdeling (ssb.no/metadata/om-klass).

Kildekoden er publisert som åpen kildekode. Datamodellen følger GSIM, en internasjonal informasjonsmodell for statistikkproduksjon (GitHub, statisticsnorway/klass).

**Deduksjon:** Fordi kildekoden er åpen og datamodellen bygger på en internasjonal modell, kan løsningen i prinsippet tas i bruk av andre som forvalter kodeverk. Det er ikke kjent at noen andre har gjort det.

### Vanlige kombinasjoner med andre produkter
- `SSB-003` Statistikkbanken og PxWebApi, der variablene i tabellene er lenket til kodeverk i KLASS.
- `SSB-002` KOSTRA, som bruker kodelister fra KLASS i rapporteringen.
- `SSB-001` microdata.no, når mikrodata skal tolkes eller grupperes med SSBs standardkoder.
- `DIGDIR-012` Begrepskatalog, når begrepene bak en kode også skal defineres.

**Kildekode:** Åpen kildekode.

**Lisens:** `Apache-2.0`, kontrollert mot repositoriet 2026-10-24. Kodeverkene er lisensiert under CC BY 4.0, som gjelder dataene, ikke kildekoden.

**Repositorium:** https://github.com/statisticsnorway/klass

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Kodeverkene deles åpent og maskinlesbart, med historikk og fri lisens.

- **P5: Del og gjenbruk løsninger**
  Støttes delvis. Kildekoden er åpen, men den er laget for SSBs egen forvaltning, og gjenbruk utenfor SSB er ikke dokumentert.

- **P6: Lag digitale løsninger som støtter samhandling**
  Felles koder med versjoner og korrespondanser gjør det mulig for ulike systemer å tolke data likt, også når kodeverkene endres.

Spenningen ligger i forutsigbarheten. En varslet endring i API-et er ikke tidfestet, og nettflaten er ny. Det legger ansvaret for å følge med på brukerne. I tillegg ligger offisielle klassifikasjoner og uoffisielle kodelister i samme system, og den som henter kodeverk må selv skille mellom dem.

## Finansiering
**Ikke offentlig dokumentert i denne arbeidsøkten:** Hvordan KLASS finansieres. Kildene skiller ikke ressursen ut fra SSBs øvrige virksomhet.

**Fakta:** Bruken er gratis og uten registrering (data.ssb.no/api/klass/v1/api-guide.html).

## Forvaltning/eier

| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Statistisk sentralbyrå (SSB) | ssb.no/metadata/om-klass |
| Ansvar for innholdet i det enkelte kodeverk | Fagseksjoner i SSB, oppgitt per kodeverk | API-ressursen `ssbsections` og kodeverkenes metadata |
| Driftsansvar | SSB | GitHub, statisticsnorway/klass |
| Budsjettansvar | Ikke offentlig dokumentert i denne arbeidsøkten | – |
| Styringsmodell | SSB samordner offisiell statistikk etter statistikkloven § 6. Styringsmodell for KLASS er ikke offentlig dokumentert i denne arbeidsøkten | lovdata.no, lov 2019-06-21-32 |

## Lenke til dokumentasjon
- Klassifikasjoner og kodelister i SSBs dataportal: https://dataportal.ssb.no/classifications
- Om KLASS: https://www.ssb.no/metadata/om-klass
- API-veiledning for KLASS v1: https://data.ssb.no/api/klass/v1/api-guide.html
- Kildekode: https://github.com/statisticsnorway/klass
- Statistikkloven: https://lovdata.no/dokument/NL/lov/2019-06-21-32

## Kildegrunnlag brukt i utfyllingen
Hentet 2026-10-24:
- SSB, Klassifikasjoner og kodelister i dataportalen: https://dataportal.ssb.no/classifications
- SSB, Om KLASS: https://www.ssb.no/metadata/om-klass
- SSB, KLASS API v1-veiledning: https://data.ssb.no/api/klass/v1/api-guide.html
- SSB, KLASS API v1, oppslag på klassifikasjoner, familier og enkelte kodeverk: https://data.ssb.no/api/klass/v1/classifications
- GitHub, statisticsnorway/klass: https://github.com/statisticsnorway/klass
- Lov om offisiell statistikk og Statistisk sentralbyrå (statistikkloven): https://lovdata.no/dokument/NL/lov/2019-06-21-32

Lokale kilder:
- `arkitektur/ressurser/operative-losninger-og-tjenester/176-SSB-Statistikkbanken-PxWebApi-v1-claude.md`
- `arkitektur/ressurser/operative-losninger-og-tjenester/169-KOSTRA-v1-claude.md`

## Endringer fra forrige versjon
Dette er første publiserte versjon av ressursbeskrivelsen.
