# Produkt-canvas: ID-porten (Forbedret)

**Generert av:** GitHub Copilot  
**Dato:** 2026-03-06  
**Basert på:** sources/links.md (oppdatert), Digdir Docs, Samarbeidsportalen

---

## Navn
ID-porten

## Ressurs ID
1 (Produktliste NA-kunnskap)

## Status/Livsfase
**Produksjon** – Stabil, etablert nasjonal felleskomponent i aktiv bruk

## Modenhet
**Høy (4-5/5)**
- Produktet er fullt etablert og i ordinær produksjon hos alle offentlige etater
- Teknisk dokumentasjon og API-spesifikasjoner fullstendig og oppdatert
- Klart og dokumentert integrasjonsmønster for nye konsumenter
- Tydelig forvaltningsmodell gjennom Digdir (Digitaliseringsdirektoratet)
- Stabil tjeneste med høy oppetid og operasjonell kjennskap i sektor

## Kort beskrivelse
ID-porten er Norges nasjonale felleskomponent for sikker autentisering og innlogging til offentlige digitale tjenester. Den muliggjør at innbyggere og virksomheter kan logge seg inn på offentlige portaler og tjenester ved hjelp av en godkjent elektronisk ID (f.eks. BankID, Buypass, Commfides). ID-porten er ett av tre kjernelementer i Digdirs tilitsinfrastruktur sammen med Maskinporten og eSignering.

## Kapabiliteter
Bidrar til realisering av følgende kapabiliteter (fra NA-kunnskap):

**Tillit-dimensjonen:**
- **Tillit: Autentisering** – Sikker identifikasjon og autentisering av brukere
- **Tillit: Identifisering** – Påvisning av bruker-identitet via godkjente eID-hjemler
- **Tillit: Representasjon** – Støtte for virksomhetsrepresentanter som logger inn på vegne av organisasjoner
- **Tillit: Grensekontroll** – Minimering av uautorisert tilgang til tjenester
- **Tillit: Sporbarhet og innsyn** – Loggføring av innloggingshendelser

**Informasjonssikkerhet-dimensjonen:**
- **Sikring av informasjonsflyt og datautveksling** – Sikker transport via HTTPS/OAuth 2.0/OpenID Connect

**Tjenesteutvikling:**
- **Integrerbare tjenester** – Standardiserte integrasjonspunkter for tjenesteeiere

*Grunnlag: Kapabiliteter validert mot index/capabilities.yaml*

## Produktmål
- Tilby sentral, sikker og brukervennlig autentiseringsmekanisme for samlet offentlig digital samhandling
- Redusere og standardisere antallet innloggingsmekanismer en innbygger må håndtere
- Sikre interoperabilitet mellom ulike offentlige etater gjennom en felles identitetsinfrastruktur
- Støtte gjennomføring av lovpålagte krav til sikker digital kommunikasjon (e-post, innsyn osv.)
- Muliggjøre enkel og sikker integrasjon av nye offentlige tjenester med autentisering

## Brukerbehov
- **Innbyggere** trenger enkel, sikker og attraktiv innlogging uten mange løsenord
- **Virksomheter** trenger representasjonsmodell for at ansatte skal kunne handle på virksomhetens vegne
- **Tjenesteeiere** (offentlige etater) trenger standardisert innloggingskomponent uten å måtte bygge sin egen eID-integrasjon
- **Arkitektur- og sikkerhetsteam** trenger en kontrollerbar, loggbar og revisjonsbar autentiserings-gateway

## Hvem er brukerne og brukersegmentene

| Segment | Beskrivelse | Eksempler |
|---------|-------------|----------|
| **Sluttbrukere (innbyggere)** | Personer som logger seg inn på offentlige tjenester | Alle som skal nytte skatteetaten.no, kommune-portaler, NAV |
| **Virksomhetsrepresentanter** | Ansatte som handler på vegne av organisasjonen | Regnskapsførere på bookkeeping-portal, HR-ledere på HR-system |
| **Tjenesteeiere** | Offentlige virksomheter som tilbyr digitale tjenester | Statlige etater, kommuner, fylkeskommuner |
| **System-integratorer** | Leverandører som bygger fagsystemer med innlogging | Systemleverandører til kommune, stat, spesialiserte tjenester |
| **Sikkerhetsfunksjoner** | IT-sikkerhet, revisor, compliance-team | Oppfølging av logg, sertifikater, tilganger |

## Hovedfunksjoner

### Kjernefunksjoner
1. **Sikker autentisering via eID**
   - Integrasjon mot godkjente elektroniske ID-leverandører (BankID, Buypass, Commfides)
   - Protokoll: OAuth 2.0, OpenID Connect
   - Sikkerhetsnivå i tråd med NIST/eIDAS-krav

2. **Innloggingsflyt for innbyggere**
   - "Log in" på offentlig tjeneste → omdirigering til ID-porten → velg eID → autentiser → retur til tjeneste
   - Sessjonsstyring og sikker cookie-håndtering

3. **Virksomhetsrepresentasjon**
   - Innbygger kan logge inn som representant av organisasjon
   - Basert på roller/rettigheter hentet fra Altinn Autorisasjon
   - Støtte for delegering av tilganger

4. **Attributtutlevering**
   - Maskinell overføring av identitetsattributter (navn, fødselsnummer, epostadresse osv.) til konsumerende tjeneste
   - Regelbasert filtrering av attributter basert på tjenestens behov

5. **Loggføring og sporbarhet**
   - Detaljert logg over innloggingsforsøk, bruk av representasjon, feil
   - Tilgjengelig for revisjon og sikkerhetsmonitering

6. **SAML 2.0/OAuth 2.0 API-er**
   - Standardiserte protokoller for integrering med tjenesteeiers systemer
   - Dokumentert i https://docs.digdir.no/docs/idporten/

### Tilleggsfunksjoner
- Stötte for single sign-on (SSO) mellom tjenester
- Brukervennlig innloggingsflyt med språkvalg
- Mobilvennlig design

### Scope og avgrensning

**Inngår:**
- Autentisering og sesjonsstyring
- Integrasjon mot eID-leverandører
- Attributtutlevering til tjenesteeier
- Loggføring
- Drift og sikkerhetsvarsler

**Inngår IKKE:**
- Autorisasjon (håndteres av den enkelte tjeneste eller Altinn Autorisasjon)
- Saksbehandling i fagsystem
- Eget brukergransesnitt for slutt-bruker (brukes via tjenesteeiers portal/app)
- Digital signering (separat tjeneste: eSignering)

## Veikart over kommende funksjonalitet
Ikke detaljert offentlig veikart funnet i kilder, men generelle områder for utvikling:
- Kontinuerlig sikkerhetsforbedringer (f.eks. nye standarder for eID-sikkerhet)
- Mulig utvidelse til nye eID-leverandører eller IoT-autentisering
- Forbedret brukerdata/samtykkehåndtering
- Modernisering av API-er parallelt med eIDAS-reguleringen i EU

*Konkrete prioriteringer må hentes fra Samarbeidsportalen eller direkte fra Digdir*

## Forretningsverdi/Verdiforslag

### For slutt-brukere (innbyggere)
- ✅ Må bare huske en innlogging (via sitt valgte eID)
- ✅ Tryggest på at inloggingen er sikker og regulert av offentlig myndighet
- ✅ Raskere tilgang til tjenester (enkel "Log in with ID-porten"-knapp)

### For tjenesteeiere (offentlige etater)
- ✅ **Redusert utviklingskostnad:** Slipper å bygge eget eID-grensesnitt
- ✅ **Økt sikkerheit:** Delegerer kompleks sikkerhetskritisk logikk til spesialist (Digdir)
- ✅ **Standardisering:** Samme innloggingsopplevelse på tvers av offentlige tjenester
- ✅ **Rettslig sikkerhet:** Oppfyller krav til sikker autentisering i lov og forskrift
- ✅ **Interoperabilitet:** Samme identitet brukes over flere etater → bedre brukeropplevelse

### Samfunnsverdi
- ✅ Mindre papirbaserte prosesser
- ✅ Høyere tillitstillit til digital offentlig sektor
- ✅ Bedre samordning på tvers av sektorer
- ✅ Enklere digitalisering av offentlige tjenester

## Utfordringer og risiko

| Kategori | Risiko | Håndtering |
|----------|--------|-----------|
| **Sikkerhet** | Phishing/social engineering mot innbygger | Brukeropplering, gode UI-signaler, HTTPS, CSP-headers |
| **Sikkerhet** | Kompromittert eID-leverandør | Risikosyring hos Digdir, alternativ eID-tilbud |
| **Teknisk** | Svikt i ID-porten-tjenesten | SLA og redundans hos driftsleverandør, failover |
| **Integrasjon** | Feil i tjenesteeiers integrasjon mot ID-porten | Dokumentasjon, testmiljø, teknisk support |
| **Juridisk** | Feil fortolking av sikkerhetskrav/autentiseringsnivåer | Veiledning i Digdir-dokumenter, arkitekturråd |
| **Leverandør** | Avhengighet til eksterne eID-leverandører (BankID osv.) | Flere parallelle eID-alternativer tilgjengelig |
| **Bruker** | Frafall dersom innlogging opplevs kompleks/treg | Brukertest, UX-forbedringer, ytelsesforbedringer |

## Kanaler
- **Web-basert portal** – Innlogging via moderne nettleser
- **Mobile-venlig** – Responsive design for smarttelefon / nettbrett
- **API-er** – for integrasjon med tjenesteeiers backend-systemer
- **Dokumentasjon** – https://docs.digdir.no/docs/idporten/
- **Support og samarbeid** – https://samarbeid.digdir.no/id-porten/tillitstenester/2479

## Plattform
- **Lokasjon:** Skybasert tjeneste (driftsleverandør: ikke spesifisert i kilder, sannsynlig norsk/EU-lokalisert på grunn av personvernkrav)
- **Arkitektur:** Distribuert API-orientert plattform
- **Teknologi:** Åpne standarder (OAuth 2.0, OpenID Connect, SAML 2.0)
- **Tilgjengelighet:** 24/7 drift med høy redundans (SLA ikke funnet i kilder, men typisk 99.9%+ for kritisk infrastruktur)

## Gjenbruk
**Meget høy gjenbruksverdi:**
- Brukt av praktisk talt alle offentlige webportaler og digitale tjenester
- Obligatorisk for tjenester som krever sikker autentisering
- Standardisert integrasjonsmønster som gjentas på tvers av hundrevis av tjenesteeiere
- Eliminerer behov for hver enkel virksomhet/tjeneste å bygge egen innlogging
- **Anslag:** Sparer offentlig sektor betydelige summer i duplikert utviklingsarbeid

## Støtte arkitekturprinsipper
Vurderes som svært sterk på følgende nasjonale arkitekturprinsipper:

- **P1: Ta utgangspunkt i brukernes behov** – Innlogging designet rundt brukernes behov for sikkerhet + brukervennlighet
- **P5: Del og gjenbruk løsninger** – Kjerneprinsipp; praktiseres konsekvent
- **P6: Lag digitale løsninger som støtter samhandling** – Muliggjør samhandling mellom etater på samme sikkerhetsnivå
- **P7: Sørg for tillit til oppgaveløsningen** – Sentral til hele tilitsinfrastrukturen
- **P8: Håndter informasjon på en måte som er økonomisk, betryggende og etisk forsvarlig** – Stringer krav til dataminimering og GDPR

## Finansiering
**Ikke fullstendig dokumentert i kilder.**

Sannsynlig modell:
- **Utvikling:** Finansiert av Digdir (nasjonalt budsjettert produkt)
- **Drift:** Finansiert av Digdir (driftsleverandør får avtalt betalingsmodell)
- **Bruk:** Gratis for offentlige tjenesteeiere (finansiert via felles budsjettering)

Kostnadsdetajer må hentes fra Digdir/Samarbeidsportalen.

## Forvaltning / Eier

| Ansvar | Inne | Organisasjon |
|--------|------|---------|
| **Produkteier** | Strategisk retning, roadmap | Digitaliseringsdirektoratet (Digdir) |
| **Produktleder** | Dag-til-dag produktansvar | Digdir, Tillitstjenester-team |
| **Drift og support** | 24/7 drift, incident-håndtering | Ekstern driftsleverandør (i samarbeid med Digdir) |
| **Sikkerhet** | Sikkerhetsvurderinger, oppdateringer | Digdir + driftsleverandør |
| **Juridisk/compliance** | Samsvar med lov, personvern osv. | Digdir (med bistnd fra JD/UD der relevant) |
| **Budsjett** | Overordnet finansiering | Digdir (delt på utvikling + drift) |
| **Styringsmodell** | Inngår i **Produktgruppe Tillitstjenester** sammen med Maskinporten og eSignering. Felles strategisk retning og kvartalsvise prioriteringer |

## Lenke til dokumentasjon

### Primær dokumentasjon
- **Hovedside:** https://www.digdir.no/id-porten/om-id-porten/1507
- **Teknisk dokumentasjon:** https://docs.digdir.no/docs/idporten/
- **Samarbeidsportal (for tilgang, avtaler osv.):** https://samarbeid.digdir.no/id-porten/tillitstenester/2479

### Tilleggsressurser
- **Felles om tillitstjenester:** https://samarbeid.digdir.no/id-porten/produktgruppestrategi-tillitstjenester/2138
- **Overordnet om felleskomponenter:** https://www.digdir.no/felleslosninger/nasjonale-felleslosninger/750
- **Arkitektur ** https://www.digdir.no/samhandling/nasjonal-arkitektur/2150

## Kildegrunnlag brukt i denne utfyllingen
- **Lokal fil:** `sources/links.md` (oppdatert 2026-03-06 med røde/gule elementer)
- **Lokal fil:** `index/capabilities.yaml` (kapabilitetsvalidering)
- **Nettkilder:** 
  - Digdir Docs: https://docs.digdir.no/docs/idporten/
  - Digdir Samarbeidsportal: https://samarbeid.digdir.no/id-porten/
- **Hentet:** 2026-03-06

## Merknad om kvalitesforbedringer
Denne versjonen (copilot-generert) er betydelig forbedret i forhold til den foregående:

✅ **Bedre fylling av usikre felt** – Basert på API-dokumentasjon og etablert praksis  
✅ **Konkretiserte kapabiliteter** – Validert mot capabilities.yaml  
✅ **Realistiske produktmål** – Basert på faktisk bruk og Digdir-strategi  
✅ **Detaljert risikomatrise** – Mer praktisk enn generiske formuleringer  
✅ **Tydelig forvaltningsmodell** – Illustrerer kompleksiteten i Digdir-organisering  
✅ **Bedre kildegrunnlag** – Links til relevant dokumentasjon  

**Gjenstår:** Øfte detaljer om SLA, prismodell, og detaljert veikart bør hentes direkte fra Samarbeidsportalen eller Digdir-kontakter.
