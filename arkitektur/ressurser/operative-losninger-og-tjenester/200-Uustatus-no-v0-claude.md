# uustatus.no

## Navn
uustatus.no

## Ressurs ID
DIGDIR-075

## Status/Livsfase
**Aktiv** – løsningen er i drift og under videre utbygging.

**Fakta:** Forsiden til uustatus.no viser at innlogging er åpen for offentlig sektor og for private leverandører av ikt-løsninger i bruk i offentlig sektor, og at migrering av leverandørvurderinger fra Feides tidligere skjemaløsning til uustatus.no «er godt i gang, men ikkje heilt i mål» (uustatus.no, hentet 2026-10-29).

## Modenhet
**Middels modenhet: kjernefunksjonen er i drift, men deler av løsningen er under migrering.**

- Offentlige virksomheter kan logge inn med ID-porten og opprette tilgjengelighetserklæringer (uustatus.no).
- Private leverandører kan logge inn og opprette leverandørvurderinger som offentlige virksomheter kan ta i bruk (uustatus.no).
- Erklæringer kan søkes opp og filtreres på status gjennom Uutilsynets nettsted (uutilsynet.no).
- Migreringen av leverandørvurderinger fra Feides skjemaløsning er ikke fullført (uustatus.no).

**Deduksjon:** Det svakeste leddet er registreringsveien for private leverandører, som krever e-post til Uutilsynet med organisasjonsnummer for å få tilsendt en PIN-kode, i stedet for selvbetjent pålogging. Dette er en manuell flaskehals i en løsning som ellers er selvbetjent for offentlig sektor.

## Kort beskrivelse
uustatus.no er Digdirs sentrale løsning for tilgjengelighetserklæringer, forvaltet av Tilsynet for universell utforming av ikt (Uutilsynet), som er organisert under Digdir. Offentlige virksomheter oppretter og publiserer her den lovpålagte tilgjengelighetserklæringen for sine nettsteder og apper. Private leverandører av ikt-løsninger kan opprette leverandørvurderinger som offentlige kunder kan gjenbruke i egne erklæringer og anskaffelser.

Løsningen er verktøyet som gjør kravet i `DIGDIR-070` (tilsyns- og regelverksvirkemiddelet for universell utforming av ikt) operativt: `DIGDIR-070` fastsetter og håndhever plikten til å ha en tilgjengelighetserklæring, mens uustatus.no er stedet erklæringen faktisk opprettes, oppdateres og publiseres.

## Kapabiliteter
- **Tjenesteutvikling: Gjenbrukbare tjenester**
  Leverandørportalen lar en privat leverandør dokumentere én leverandørvurdering som flere offentlige kunder kan gjenbruke i egne tilgjengelighetserklæringer og anskaffelser, i stedet for at hver virksomhet bestiller eller gjennomfører egen vurdering av samme løsning.

**Vurdert og ikke tatt med:** `Tillit: Sporbarhet og innsyn` ble vurdert, men holdt utenfor. Beslutningen 2026-10-25 om at kapabiliteten gjelder innsynshåndtering og brukerens innsyn i egne data og logger – ikke alminnelig publisering av opplysninger – er samme grunn til at `06` eInnsyn ikke fikk koblingen. Tilgjengelighetserklæringer er generell, offentlig informasjon om en virksomhets status, ikke en innbyggers innsyn i egne data eller en logg over bruk, og realiserer derfor ikke kapabiliteten slik den nå er avgrenset.

## Produktmål
**Deduksjon:** Målet er å gjøre det mulig for offentlig sektor å oppfylle den lovpålagte plikten til å dokumentere status for universell utforming av ikt, og å redusere dobbeltarbeid ved at leverandørers vurderinger kan gjenbrukes av flere kunder. Ikke funnet et eksplisitt formulert produktmål i kildene brukt her.

## Brukerbehov
Offentlige virksomheter har plikt til å dokumentere i hvilken grad nettsteder og apper oppfyller kravene til universell utforming, i et maskinlesbart format, og til å oppdatere dette minst én gang i året. Private leverandører av ikt-løsninger til offentlig sektor har behov for å dokumentere løsningens tilgjengelighetsstatus én gang, i stedet for å svare på det samme fra hver enkelt kunde. Innkjøpere og brukere har behov for å kunne finne og sammenligne status på tvers av virksomheter.

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter | Oppfylle lovpålagt dokumentasjonsplikt | Opprette og årlig oppdatere tilgjengelighetserklæring | Innlogging med ID-porten |
| Private leverandører av ikt-løsninger | Dokumentere tilgjengelighet uten å gjenta vurderingen for hver kunde | Opprette leverandørvurdering i leverandørportalen | Innlogging med PIN-kode bestilt per e-post |
| Innkjøpere i offentlig sektor | Sjekke dokumentert status før anskaffelse | Bruke leverandørvurderinger i anskaffelsesprosesser | Forutsetter at leverandøren har registrert seg |
| Uutilsynet | Følge opp etterlevelse | Tilsyn og kontroll, jf. `DIGDIR-070` | Uustatus.no er datagrunnlaget tilsynet bygger på |
| Innbyggere og presse | Finne status for et konkret nettsted eller en app | Søk i publiserte erklæringer | Søkefunksjonen ligger på uutilsynet.no |

## Hovedfunksjoner
Den første hovedfunksjonen er **opprettelse og publisering av tilgjengelighetserklæringer**. Offentlige virksomheter logger inn med ID-porten og fyller ut erklæringen i seks steg; den skal oppdateres minst én gang i året.

Den andre er **leverandørvurderinger**. Private leverandører av ikt-løsninger logger inn med en PIN-kode bestilt per e-post til Uutilsynet, og oppretter vurderinger som offentlige kunder kan ta i bruk i egne erklæringer, i stedet for å vurdere den samme løsningen på nytt for hver kunde.

Den tredje er **søk og filtrering av publiserte erklæringer**, som gjør status for en virksomhet eller løsning tilgjengelig for andre enn den som opprettet den.

### Typiske brukssituasjoner (generisk)
- en offentlig virksomhet skal opprette eller oppdatere tilgjengelighetserklæringen for et nettsted eller en app
- en leverandør av en ikt-løsning som brukes i offentlig sektor skal dokumentere løsningens tilgjengelighetsstatus for flere kunder samtidig
- en innkjøper skal sjekke om en leverandørs løsning har en dokumentert leverandørvurdering før anskaffelse
- en innbygger eller journalist skal finne status for et konkret offentlig nettsted

### Når uustatus.no normalt ikke er førstevalg
uustatus.no er ikke stedet for selve tilgjengelighetstestingen. Den faktiske WCAG-vurderingen gjøres med egne testprosedyrer og sjekklister som Uutilsynet publiserer separat; uustatus.no er rapporterings- og publiseringsverktøyet, ikke testverktøyet.

Løsningen er heller ikke kanalen for å klage på manglende tilgjengelighet eller for selve tilsynssaken. Det håndteres av Uutilsynet som virkemiddel, beskrevet i `DIGDIR-070`.

### Scope og avgrensning
Inngår:
- opprettelse, oppdatering og publisering av tilgjengelighetserklæringer for offentlig sektor
- leverandørvurderinger opprettet av private leverandører
- innlogging for offentlig sektor (ID-porten) og for leverandører (PIN-kode)

Inngår ikke:
- selve testingen/revisjonen av løsninger mot WCAG-kravene
- tilsyn, kontroll og sanksjoner, som ligger i `DIGDIR-070`
- regelverket som fastsetter kravene

## Veikart over kommende funksjonalitet
**Fakta:** Migrering av leverandørvurderinger fra Feides tidligere skjemaløsning til uustatus.no pågår og er ikke fullført (uustatus.no, hentet 2026-10-29).

**Ikke offentlig dokumentert:** Øvrige planer for videreutvikling av løsningen.

## Forretningsverdi/Verdiforslag
For offentlige virksomheter ligger verdien i ett sted å oppfylle den lovpålagte dokumentasjonsplikten, med en strukturert prosess i seks steg.

For private leverandører ligger verdien i å kunne dokumentere tilgjengelighetsstatus én gang og la flere kunder gjenbruke vurderingen, i stedet for å svare på det samme fra hver enkelt kunde.

For innkjøpere ligger verdien i å kunne sjekke dokumentert status før en anskaffelse, i stedet for å etterspørre det separat.

For innbyggere og presse ligger verdien i å kunne finne og sammenligne status for offentlige nettsteder og apper.

## Utfordringer og risiko

| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Overgang | Migrering av leverandørvurderinger fra Feide er ikke fullført | Uustatus.no oppgir selv at arbeidet pågår |
| Tilgang | Leverandører må bestille PIN-kode per e-post for å logge inn, ikke selvbetjent | Ikke offentlig dokumentert om dette er en midlertidig eller varig løsning |
| Kvalitetssikring | Om og hvordan Uutilsynet kvalitetssikrer innholdet i leverandørvurderinger før de gjenbrukes | Ikke offentlig dokumentert |
| Juridisk | Leveransesikkerhet og driftsavtale for løsningen | Ikke offentlig dokumentert |

## Kanaler
uustatus.no er innloggingskanalen: ID-porten for offentlige virksomheter, PIN-kode for private leverandører. Søk i publiserte erklæringer skjer gjennom uutilsynet.no. Veiledning, WCAG-sjekklister og film om utfylling publiseres på uutilsynet.no.

## Plattform
**Ikke offentlig dokumentert:** Teknisk plattform, drift og infrastruktur for uustatus.no.

## Gjenbruk
Kjernefunksjonen i leverandørportalen er gjenbruk: én leverandørvurdering kan brukes av flere offentlige kunder, i stedet for at hver kunde bestiller sin egen vurdering av samme løsning.

### Vanlige kombinasjoner med andre produkter
- `DIGDIR-070` Tilsyn og kontroll med regelverk for universell utforming av ikt, som fastsetter og håndhever kravet uustatus.no gjør operativt.
- ID-porten, som innloggingsmekanisme for offentlige virksomheter.

**Kildekode:** Ikke offentlig dokumentert.

**Lisens:** Ikke offentlig dokumentert.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger**
  Leverandørvurderinger opprettes én gang og gjenbrukes av flere offentlige kunder, i stedet for at hver kunde bygger sin egen vurdering.

Spenningen ligger i tilgangen for leverandører: en PIN-kode bestilt per e-post er en manuell inngang som bryter med selvbetjeningen ID-porten gir offentlig sektor, og kan bremse hvor raskt leverandører tar løsningen i bruk.

## Finansiering
**Ikke offentlig dokumentert.**

## Forvaltning/eier

| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Faglig og forvaltningsansvar | Tilsynet for universell utforming av ikt, organisert under Digdir | uutilsynet.no; samme forvalter som `DIGDIR-070` |
| Driftsansvar | Ikke offentlig dokumentert | – |
| Budsjettansvar | Ikke offentlig dokumentert | – |
| Styringsmodell | Ikke offentlig dokumentert | – |

## Lenke til dokumentasjon
- uustatus.no: https://uustatus.no/
- Om tilgjengelighetserklæring: https://www.uutilsynet.no/tilgjengelighetserklaering/tilgjengelighetserklaering/1127
- Uutilsynet: https://www.uutilsynet.no/

## Kildegrunnlag brukt i utfyllingen
Hentet 2026-10-29:
- uustatus.no, forside: https://uustatus.no/
- Uutilsynet, Tilgjengelighetserklæring: https://www.uutilsynet.no/tilgjengelighetserklaering/tilgjengelighetserklaering/1127

Lokale kilder:
- `arkitektur/ressurser/rammer-og-virkemidler/150-Tilsyn-og-kontroll-universell-utforming-av-ikt-v2-claude.md`
