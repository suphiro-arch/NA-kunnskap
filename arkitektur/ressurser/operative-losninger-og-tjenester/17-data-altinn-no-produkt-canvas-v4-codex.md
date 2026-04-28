# Produkt-canvas: data.altinn.no

## Navn
data.altinn.no

## Ressurs ID
DIGDIR-015

## Status/Livsfase
**Produksjon** - etablert fellesløsning i Altinn for kontrollert datadeling mellom virksomheter gjennom en felles API-modell.

**Fakta:** Offisiell dokumentasjon beskriver data.altinn.no som en generisk løsning for å forenkle deling og gjenbruk av informasjon direkte fra kilden. Tjenestekatalogen omfatter blant annet eBevis, Drosjeløyve, Advokatregisteret, Tilda og BITS kontrollinformasjon per 26. mars 2026.

## Modenhet
**Høy funksjonell modenhet** - produktet fremstår som et etablert mønster for datadeling i Altinn:
- Dokumentasjonen dekker både overordnet produktforståelse, teknisk API-bruk og tjenestespesifikke eksempler.
- Flere ulike datadelingstjenester bruker samme grunnmodell for forespørsel, tilgang og uthenting.
- Produktet er tydelig avgrenset som kontrollert datadelingstjeneste, ikke som åpen datakatalog eller generell portal.

**Deduksjon:** Modenheten er høy for den generiske delingsmodellen, mens hver enkelt domenetjeneste fortsatt kan ha ulik modenhet og kompleksitet.

## Kort beskrivelse
data.altinn.no er Altinns fellesløsning for kontrollert datadeling mellom virksomheter. Produktet gjør det mulig å hente informasjon direkte fra autoritative kilder i en definert tjenestekontekst, med en felles API-modell for forespørsler, tilgangskontroll og uthenting av datasett.

Produktet har både en tjenesteflate og en integrasjonsflate. Tjenesteflaten består av konkrete datadelingstjenester som eBevis, Drosjeløyve, Advokatregisteret, Tilda og BITS kontrollinformasjon. Integrasjonsflaten består av den generiske API-modellen, API-nøkler, Maskinporten-tilgang og tjenestekontekst som styrer hvilke data som kan hentes og på hvilket grunnlag. Dette gjør produktet bredere enn en enkelt API-endepunktssamling, men smalere enn en generell nasjonal datakatalog.

## Kapabiliteter
- **Datadrevet: Sammenstilling av data** støttes når flere datasett og datakilder kombineres i samme tjenestekontekst.
- **Datautveksling og integrasjon: Bruke data fra andre** gjør det mulig for konsumenter å hente data direkte fra kilder gjennom en standardisert modell.
- **Datautveksling og integrasjon: Dele data med andre** gjør det mulig for datatilbydere å eksponere data gjennom en felles Altinn-løsning.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** er sentral fordi produktet håndterer kontrollert tilgang til ikke-åpne data og personopplysninger.
- **Standardisering: Forvaltningsstandarder** realiseres gjennom en generisk og gjenbrukbar API-modell på tvers av flere tjenester.
- **Tillit: Autentisering** støttes gjennom bruk av Maskinporten og API-nøkler i produktets integrasjonsmodell.
- **Tillit: Samtykke** er relevant fordi enkelte tjenester bruker samtykke som grunnlag for datadeling.
- **Tillit: Tilgangskontroll** er sentral fordi tjenestekontekst og regler styrer hvilke data som kan hentes.
- **Tjenesteutvikling: Integrerbare tjenester** gjør det mulig å etablere flere datadelingstjenester innenfor samme grunnmønster.

## Produktmål
**Primærkilder:** data.altinn.no, tjenestesidene og teknisk dokumentasjon.

Dokumenterte mål:
- Forenkle deling av data fra virksomheter og gjenbruk av informasjon direkte fra kilden.
- Gjøre det enklere å komme i gang med datadeling både for datakilder og konsumenter.
- Tilby et enkelt, generisk API for utveksling av datasett på en sikker måte.
- Styre datadeling gjennom tjenestekontekst, autorisasjonsregler og eventuelt samtykke.

Operative mål utledet fra de samme kildene:
- Gjøre det mulig å gjenbruke samme delingsmodell på flere forretningsområder og tjenester.
- Minimere behovet for at hver datadelingstjeneste lager sitt eget tekniske grunnmønster.
- Gi konsumenter en mer forutsigbar integrasjonsopplevelse på tvers av ulike domenetjenester.

**Deduksjon:** Produktet har også en viktig rolle som standardiseringslag for kontrollert datadeling i Altinn-økosystemet.

## Brukerbehov
- Datatilbydere trenger en felles modell for å tilgjengeliggjøre data uten å bygge unik infrastruktur for hver konsument.
- Konsumentsystemer trenger en standard måte å hente data i riktig tjenestekontekst på.
- Juridiske og forvaltningsmessige miljøer trenger tydelig styring av samtykke, hjemler og tilgangsregler.
- Integrasjonsteam trenger dokumentasjon, API-nøkler og autentiseringsmønstre som kan brukes på tvers av flere tjenester.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige og andre datatilbydere | Dele data kontrollert gjennom en felles modell | Eksponering av datasett og tjenester | Beholder data hos kilden og bruker tjenestekontekst for styring |
| Konsumentsystemer i offentlig og privat sektor | Hente data fra autoritative kilder | Automatiserte oppslag og datagjenbruk | Må bruke både API-nøkkel og autentisering etter produktets modell |
| Tjenesteeiere for domenetjenester | Etablere nye datadelingstjenester | eBevis, Tilda og andre tjenestekontekster | Bruker samme grunnmønster med ulike regler |
| Juridiske og forvaltningsmessige miljøer | Styring av grunnlag for deling | Samtykke, hjemler og autorisasjon | Viktig fordi samme datasett kan brukes i ulike kontekster |
| Utviklings- og integrasjonsteam | Forutsigbar teknisk modell | Implementasjon, test og drift av integrasjoner | Møter produktet som API- og tilgangsmodell, ikke bare som portal |

## Hovedfunksjoner
data.altinn.no gir en generisk modell for å be om og hente datasett direkte fra kilden. Dokumentasjonen beskriver at alle uthentinger skjer i kontekst av en tjeneste, og at tjenesten regulerer autorisasjon og hvilke datasett som kan brukes. Dette betyr at produktet ikke bare er en teknisk API-gateway, men en struktur for kontrollert datadeling der samme datasett kan brukes under ulike regler avhengig av tjenestekontekst.

En sentral funksjon ved produktet er at det kobler sammen flere konkrete datadelingstjenester innenfor samme tekniske mønster. eBevis, Drosjeløyve, Advokatregisteret, Tilda og BITS kontrollinformasjon fremstår som ulike tjenester oppå samme grunnmodell. Det gjør løsningen relevant når behovet er å etablere eller bruke kontrollert datadeling uten å oppfinne nye integrasjonsmønstre for hver tjeneste.

Produktet har også en tydelig tillits- og tilgangsflate. Dokumentasjonen viser bruk av Maskinporten, API-nøkler og i noen tilfeller samtykke eller annet rettsgrunnlag. Dermed dekker løsningen mer enn bare transport av data; den tilbyr et mønster for sikker og styrt datatilgang direkte fra kilden. Samtidig inngår ikke eierskap til kildedataene eller faglig kvalitetssikring av innholdet som produktets hovedansvar.

data.altinn.no er derfor riktig produkt når vurderingen gjelder kontrollert datadeling i Altinn-økosystemet. Det er mindre presist når behovet primært er å publisere åpne data, katalogisere metadata eller bygge sluttbrukerrettede portaler. Produktet er heller ikke en erstatning for de konkrete domenetjenestene som bruker løsningen; det er den felles delingsmodellen og tjenesteflaten rundt disse.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Generisk API-modell for kontrollert datadeling | Åpen datakatalog for hele offentlig sektor |
| Tjenestekontekst som styrer regler og tilgang | Full eierskap til eller forvaltning av alle underliggende kildedata |
| Maskinporten- og API-nøkkelbasert integrasjon | Sluttbrukerportal for innbyggere som hovedflate |
| Flere domenetjenester bygget på samme mønster | Generell metadataforvaltning som eget hovedformål |
| Henting av data direkte fra kilden | Erstatning for juridiske vurderinger hos tjenesteeier og datatilbyder |
### Typiske brukssituasjoner (generisk)
- Offentlig virksomhet eller privat aktør trenger kontrollert maskinell tilgang til spesifikke offentlige data for å fatte vedtak eller gjennomføre vurderinger.
- Finansinstitusjon, advokat eller revisor trenger å verifisere virksomhetsopplysninger direkte fra kilden.
- Offentlig etat trenger tilgang til kontrolldata for saksbehandling uten å lagre kopier lokalt.

### Når data.altinn.no normalt ikke er førstevalg
- Når behovet er åpen publisering og oppdagelse av datasett – da er data.norge.no og Felles datakatalog mer relevant.
- Når behovet er innbyggers egne oppslag uten maskinelt tilgangsregime.
- Når tilgangen til kildedataene håndteres direkte med kilderegistrets eget API uten behov for den generiske delingsmodellen.

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-26):**
- Dokumentasjonen viser en etablert tjenestekatalog og flere produktiserte datadelingstjenester.
- Kildene viser videre at nye tjenester kan legges til innenfor samme generiske modell.

**Ikke offentlig dokumentert i brukte kilder:** En samlet, tidsfestet roadmap for produktet.

**Deduksjon:** Videreutviklingen vil trolig bestå i flere tjenester, videreutvikling av dokumentasjon og fortsatt forbedring av tilgangs- og integrasjonsmønstre, men dette er ikke konkret offentlig tidsfestet.

## Forretningsverdi/Verdiforslag
### For datatilbydere
- Reduserer behovet for egne tekniske delingsløsninger for hver enkelt konsument.
- Gjør det mulig å dele data gjennom en etablert og dokumentert modell for kontrollert tilgang.

### For datakonsumenter
- Gir en mer forutsigbar integrasjonsopplevelse på tvers av flere datadelingstjenester.
- Gjør det mulig å hente oppdaterte data direkte fra kilden i stedet for å basere seg på lokale kopier.

### For offentlig sektor
- Øker gjenbruk av én felles modell for kontrollert datadeling.
- Støtter mer sammenhengende tjenester gjennom sikker gjenbruk av informasjon som allerede finnes.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil forståelse av tjenestekontekst, hjemmel eller samtykke kan gi ulovlig datadeling | Tydelig regelmodell, juridisk avklaring og god dokumentasjon |
| Teknisk | Avhengighet til underliggende datakilder kan påvirke tilgjengelighet og svartid | Robust feilbehandling, overvåking og tydelige forventninger til kildesystemer |
| Sikkerhet | Feil tilgangskontroll eller feil bruk av API-nøkler og tokens kan gi uønsket datatilgang | Streng tilgangsstyring, minst mulig deling og god nøkkelhåndtering |
| Forvaltning | Uklare grenser mellom den generiske løsningen og de konkrete domenetjenestene kan gi feil ansvarsbilde | Tydelig produktavgrensning og klar dokumentasjon av tjenestekontekst |
| Brukeropplevelse | Oppstart kan oppleves krevende når flere mekanismer må være på plass samtidig | Bedre onboarding, tydelige eksempler og tjenestespesifikk dokumentasjon |

## Kanaler
- Produktside: https://data.altinn.no/
- Tjenesteoversikt: https://data.altinn.no/products
- Teknisk dokumentasjon: https://docs.data.altinn.no/
- Tjenester: https://docs.data.altinn.no/tjenester/

## Plattform
Felles datadelingsløsning i Altinn-porteføljen med generisk API-modell, tjenestekontekst og tilgangsstyring for kontrollert datadeling.

**Fakta:** Dokumentasjonen viser at produktet bruker tjenestekontekst for å styre hvilke datasett som kan hentes, og at kall typisk krever både API-nøkkel og autentisering gjennom Maskinporten. Løsningen er bygget for gjenbruk på tvers av flere domenetjenester.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsmodell, detaljert plattformarkitektur og separat kostnadsmodell for produktet alene.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme delingsmodell kan brukes på flere ulike forretningsområder.
- Produktet reduserer behovet for lokale særintegrasjoner for kontrollert datadeling.
- Gjenbruksverdien er størst når behovet gjelder sikker og styrt datadeling direkte fra kilden, ikke åpen publisering eller metadataoversikt.


### Vanlige kombinasjoner med andre produkter
- **Maskinporten** – er autentiseringsmekanismen for tilgang via data.altinn.no.
- **Altinn Autorisasjon** – brukes for delegering og tilgangsstyring i tjenestekonteksten.
- **Enhetsregisteret, Folkeregisteret, Skatteetatens delingstjenester** – er eksempler på kilderegistre som deles via data.altinn.no.

**Kildekode:** Åpen kildekode. Lisens: MIT. Kildekode: [github.com/Altinn/altinn-accessmanagement](https://github.com/Altinn/altinn-accessmanagement).

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** er direkte relevant fordi produktet er laget for å hente og gjenbruke data fra kilden.
- **P5: Del og gjenbruk løsninger** realiseres ved at flere tjenester bygger på samme tekniske delingsmodell.
- **P6: Lag digitale løsninger som støtter samhandling** styrkes fordi datadeling kan skje gjennom et felles mønster mellom virksomheter.
- **P7: Sørg for tillit til oppgaveløsningen** støttes gjennom kontrollert tilgang, autentisering og samtykkemekanismer.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Separat finansieringsmodell eller kostnadsnivå for data.altinn.no isolert fra øvrig Altinn-portefølje.
- **Deduksjon:** Produktet må forstås som del av Altinns samlede forvaltning og finansiering.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir / Altinn-forvaltningen | Offisiell dokumentasjon på data.altinn.no og docs.data.altinn.no |
| Driftsansvar | Altinns forvaltnings- og driftsmiljø | Produktet beskrives som del av Altinn-økosystemet |
| Budsjettansvar | Del av Altinn-porteføljen | Ingen separat offentlig kostnadsmodell verifisert |
| Styringsmodell | Produktforvaltning i Altinn med flere tjenestekontekster | Fremgår av produkt- og tjenestestrukturen |

## Lenke til dokumentasjon
- https://data.altinn.no/
- https://data.altinn.no/products
- https://docs.data.altinn.no/
- https://docs.data.altinn.no/tjenester/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/17-data-altinn-no-produkt-canvas-v3-codex.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://data.altinn.no/ (kontrollert 2026-03-26)
- Nettkilde: https://data.altinn.no/products (kontrollert 2026-03-26)
- Nettkilde: https://docs.data.altinn.no/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.data.altinn.no/tjenester/ (kontrollert 2026-03-26)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen er oppdatert med kontroll mot gjeldende tjenestekatalog og teknisk dokumentasjon for data.altinn.no.
- Produktets bredde som både tjenesteflate og integrasjonsflate er tydeligere beskrevet.
- Avgrensningen mot åpne datakataloger og rene portalprodukter er strammet inn.

### Tekstlige forbedringer
- Hovedfunksjoner er skrevet om til mer forklarende avsnitt i tråd med oppdatert instruks.
- Språket er harmonisert med nyere canvas-filer og tydeligere målrettet mot nasjonal arkitektur.
- Gjenbruk og scope er gjort mer presist for å støtte produktvalg i senere analyser.



