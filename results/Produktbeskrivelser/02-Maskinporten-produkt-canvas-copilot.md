# Produkt-canvas: Maskinporten (Forbedret)

**Generert av:** GitHub Copilot  
**Dato:** 2026-03-07  
**Basert på:** sources/links.md (oppdatert), Digdir Docs, Samarbeidsportalen, Produktgruppe Tillitstjenester

---

## Navn
Maskinporten

## Ressurs ID
2 (Produktliste NA-kunnskap)

## Status/Livsfase
**Produksjon** – Stabil, etablert nasjonal felleskomponent i aktiv bruk for API-sikkerhet

## Modenhet
**Høy (4-5/5)**
- Produktet er fullt etablert og i ordinær produksjon hos alle offentlige etater med behov for sikre API-kall
- Teknisk dokumentasjon og API-spesifikasjoner fullstendig og oppdatert (OAuth 2.0, OIDC)
- Klart integrasjonsmønster for nye konsumenter og API-tilbydere
- Tydelig forvaltningsmodell gjennom Digdir (del av Produktgruppe Tillitstjenester)
- Stabil tjeneste med høy oppetid og etablert operasjonell kjennskap i sektor

## Kort beskrivelse
Maskinporten er Norges nasjonale felleskomponent for sikker autentisering og autorisasjon av maskin-til-maskin (M2M) kommunikasjon og API-kall mellom offentlige (og private) virksomheter. Den muliggjør at datakilder og datakonsumenter kan bygge sikre, skalérbare integrasjoner uten å måtte utvikle proprietære sikkerheitsløsninger. Maskinporten er ett av tre kjernelementer i Digdirs tilitsinfrastruktur sammen med ID-porten og eSignering.

## Kapabiliteter
Bidrar til realisering av følgende kapabiliteter (fra NA-kunnskap):

**Tillit-dimensjonen:**
- **Tillit: Autentisering** – Sikker identifikasjon av API-klienter (systemkonto, virksomhetskonto)
- **Tillit: Tilgangsstyring** – Håndtering av fullmakter og delegering mellom virksomheter
- **Tillit: Tilgangskontroll** – Minimering av uautorisert tilgang til API-er og sensitive data
- **Tillit: Sporbarhet og innsyn** – Loggføring og revisjon av alle API-kall med autentisering
- **Tillit: Samtykkeforvaltning** – Støtte for eksplisitte tillatelser og revokasjon av tilgang

**Datautveksling og integrasjon-dimensjonen:**
- **Dele data med andre** – Sikker API-eksponering over organisasjonsgrenser
- **Bruke data fra andre** – Sikker API-konsumering fra andre virksomheters datakilder
- **Integrerbare tjenester** – Standardiserte integrasjonspunkter

**Informasjonssikkerhet-dimensjonen:**
- **Sikring av informasjonsflyt og datautveksling** – TLS, OAuth 2.0, digitale sertifikater

*Grunnlag: Kapabiliteter validert mot index/capabilities.yaml*

## Produktmål
- Tilby sentral, sikker og standardisert autentiseringsmekanisme for API-samarbeid på tvers av virksomheter
- Redusere behov for proprietære punkt-til-punkt sikkerhetsløsninger og komplekse bilaterale avtaler
- Muliggjøre rask etablering av nye datautvekslingssamarbeid uten sikkerhetsfokus å bli en barriere
- Støtte fremveksten av offentlige og private API-økosystemer gjennom felles tillitsinfrastruktur
- Sikre interoperabilitet og skalérbarhet for datadeling i nasjonal skala

## Brukerbehov
- **API-tilbydere (datakildene)** trenger enkel måte å beskytte sine API-er uten kompleks autentiseringslogikk
- **API-konsumenter (datakonsumenter)** trenger sikker, skalerbar måte å få tilgang til data fra andre virksomheter
- **Tjenesteeiere** trenger å kunne dele data med eksterne aktører uten å opprette parallelle sikkerhetsinfrastrukturer
- **IT- og sikkerhetsteam** trenger sentral kontroll, loggføring og revisjon av all maskinell datautveksling
- **Samarbeidende virksomheter** trenger enkel prosess for å delegere tilganger gjennom fullmaktssystemer

## Hvem er brukerne og brukersegmentene

| Segment | Beskrivelse | Eksempler |
|---------|-------------|----------|
| **API-tilbydere** | Offentlige virksomheter som eksponerer data via sikre API-er | Skateetaten, NAV, Brønnøysundregistrene, kommuner |
| **API-konsumenter (private)** | Private virksomheter/systemleverandører som bruker offentlige API-er | ERP-leverandører, boligselskaper, fintech-bedrifter |
| **API-konsumenter (offentlige)** | Andre offentlige virksomheter som deler data med hverandre | Kommune som kaller stats-API, fylkeskomune osv. |
| **Fullmaktsmedlere** | Virksomheter som hjelper organisasjoner med tilgangsdelegering | Revisor, IT-leverandør, rådgiver |
| **Integrasjonsteam** | Backend-utviklere som bygger API-klienter | Leverandører, interne IT-team |
| **Sikkerhetsfunksjoner** | IT-sikkerhet, compliance, revisor | Oppfølging av API-trafikk, tilgangsrevisjoner |

## Hovedfunksjoner

### Kjernefunksjoner
1. **Klientautentisering for API-kall**
   - Autentisering av system-til-system via oAuth 2.0 Client Credentials flow
   - Bruk av virksomhetssertifikat (Buypass, Commfides osv.)
   - JWT-baserte tokens med kontrollerbar levetid og scope

2. **Delegation og fullmaktshåndtering**
   - Virksomhet A gir virksomhet B lov til å hente data på vegne av virksomhet A
   - Basert på rettigheter hentet fra Altinn Autorisasjon
   - Støtte for scoped tilganger (f.eks. "lov til å lese skatteinformasjon" men ikke "skrive")
   - Enkel revokasjon av fullmakter

3. **Token-utstedelse og validering**
   - Maskinporten utsteder JWTs ved authentisering
   - API-tilbyder validerer token lokalt eller via Maskinporten-validering
   - Token inneholder informasjon om klientens identitet og fullmakter

4. **Loggføring og sporbarhet**
   - Detaljert logg Over alle autentiseringsøkter og token-utstedelser
   - Informasjon om hvem som spurte og hva de fikk tilgang til
   - Tilgjengelig for revisjonsformål og sikkerhetsmonitering

5. **API-dokumentasjon og onboarding**
   - Selvbetjent registrering av API-klienter
   - Dokumentasjon av integrasjonsmønster
   - Test-miljø med sandkasse-API-er for utvikling

6. **Sertifikatforvaltning**
   - Integrasjon mot sertifikatutstředere (BuyPass, Commfides)
   - Automatisert fornyelse og oppdatering av sertifikater
   - Sealing-support for signering av sensitive operasjoner

### Tilleggsfunksjoner
- Støtte for SAML 2.0 (for eldre systemer)
- Testing og debugging av API-integrasjoner
- Statistikk og rapportering om API-bruk
- Notifikasjoner ved sikkerhetshendelser

### Scope og avgrensning

**Inngår:**
- Maskinell autentisering (system-til-system)
- Autorisasjon og fullmaktshåndtering
- Token-utstedelse og validering
- Loggføring og sporbarhet
- Sertifikatintegrasjon

**Inngår IKKE:**
- Sluttbruker-autentisering (dekkes av ID-porten)
- Applikasjonslogg og driftsmonitering i klientens system
- API-styring (rate limiting, versjonering) – må implementeres av API-tilbyder
- Faktisk datautveksling (Maskinporten håndterer kun autentisering)

## Veikart over kommende funksjonalitet

**Kjent fokusområdet:**
- Kontinuerlig sikkerhetsforbedringer (f.eks. nye OAuth 2.0-standarder, mTLS-støtte)
- Forbedret brukeropplevelse for selvbetjent registrering
- Integrering med nye sertifikatutstředere og eID-metoder
- Skalerbarhet for høyvolum API-trafikk
- Mulig utvidelse til IoT/machine-identity scenarios

**Organisert prioritering:**
- Inngår i **Produktgruppe Tillitstjenester** sammen med ID-porten og eSignering
- Felles strategisk retning under Digdir
- Detaljert roadmap må hentes fra Samarbeidsportalen eller Digdir-kontakter

*Kilder: Samarbeidsportalen (oppdateres kvartalsvis)*

## Forretningsverdi/Verdiforslag

### For API-tilbydere (datakildene)
- ✅ **Redusert utviklingskostnad:** Slipper å bygge eget autentiserings-/autorisasjonssystem
- ✅ **Økt sikkerhet:** Delegerer kompleks sikkerhetskritisk logikk til spesialist (Digdir)
- ✅ **Raskere time-to-market:** Kan fokusere på forretningslogikk, ikke sikkerhet
- ✅ **Compliance:** Oppfyller krav til sikker datadeling i lov og forserkrift

### For API-konsumenter (datakonsumenter)
- ✅ **Standardisert integrasjon:** Samme mønster for alle API-er (ikke proprietære løsninger)
- ✅ **Lavere kostnader:** Færre tilpassinger ved datakilde-bytter
- ✅ **Redusert administrativt overhead:** Sentralisert tilgangsstyring via Altinn
- ✅ **Sikkerhetoversikt:** Kan revurdere tilganger på en plass

### For samarbeidende virksomheter
- ✅ **Raskere samarbeid:** Fra avtale til integrasjon går fra måneder til dager
- ✅ **Lavere transaksjonskostnader:** Felles infrastruktur > separate bilaterale løsninger
- ✅ **Skalérbarhet:** Håndterer mange-til-mange-forhold uten eksponensiell økning i kompleksitet
- ✅ **Fleksibilitet:** Lett å legge til nye datakilder eller dataenkeltvalør

### Samfunnsverdi
- ✅ Økt datadeling i offentlig sektor → bedre tjenester
- ✅ Redusert tid og kostnad for digitalisering av offentlige tjenester
- ✅ Muliggjør private bedrifter å bygge tjenester på offentlige data (f.eks. skatt-app, HR-systemer)
- ✅ Bedre samordning på tvers av virksomheter
- ✅ Standardisering av sikkerhetskrav reduserer risikoer

## Utfordringer og risiko

| Kategori | Risiko | Håndtering |
|----------|--------|-----------|
| **Sikkerhet** | Kompromittert sertifikat eller hemmelighet hos klient | Rask revokasjon, monitorering av bruk, klientens sikkerhet |
| **Sikkerhet** | Feil delegering av fullmakter (gir for høy tilgang) | Sjekklister, opplæring, sentraliserte policyer i Altinn |
| **Teknisk** | Svikt i Maskinporten-tjenesten | SLA og redundans hos driftsleverandør, failover, klient-caching |
| **Integrasjon** | Feil implementering av OAuth 2.0 hos klient | Dokumentasjon, testmiljø, teknisk support, best-practice veiledninger |
| **Juridisk** | Usikkerhet rundt ansvar ved databrudd (hvem har skylden?) | Tydelige databehandleravtaler, Log-revisjoner |
| **Organisatorisk** | Manglende enighet om tilgangsnivåer og policyer | Governance-modell, roller, ESA |
| **Leverandør** | Avhengighet til Digdir for sikkerhetsforbedringer | Digdir er stabil nasjonal aktør, men stakeholder-påvirkning krever tid |
| **Brukbar** | Høy kompleksitet ved delegering på tvers av flere virksomheter | UX-forbedringer, opplæring for tilgangsadministratorer |

## Kanaler
- **API-dokumentasjon og teknisk guide** – https://docs.digdir.no/docs/maskinporten/
- **Samarbeidsportal** – https://samarbeid.digdir.no/ (tilgang, avtaler, støtte)
- **Developer portal** – Selvbetjent registrering av API-klienter
- **Testmiljø** – TT02 med test-API-er for utvikling
- **Support** – E-post, support-chat via Samarbeidsportalen

## Plattform
- **Lokasjon:** Skybasert tjeneste (driftsleverandør: ikke spesifisert i kilder, sannsynlig norsk/EU-lokalisert på grunn av personvernkrav)
- **Protokoll:** OAuth 2.0 (primary), SAML 2.0 (legacy), OpenID Connect
- **Tilgjengelighet:** 24/7 drift med høy redundans (SLA ikke funnet i kilder, men typisk 99.9%+ for kritisk infrastruktur)
- **Skalérbarhet:** Designet for høyt volum API-trafikk

## Gjenbruk
**Meget høy gjenbruksverdi:**
- Brukt av praktisk talt alle offentlige virksomheter som tilbyr eller konsumerer API-er
- Standardisert integrasjonsmønster som gjentas på tvers av hundrevis av API-er
- Eliminerer behov for hver API-tilbyder å bygge eget autentiseringssystem
- Bidrar til nasjonale datalingsinitiativ (data.norge.no, Felles datakatalog osv.)
- **Anslag:** Sparer offentlig sektor og privat næringsliv betydelige summer i duplikert utviklingsarbeid

## Støtte arkitekturprinsipper
Vurderes som svært sterk på følgende nasjonale arkitekturprinsipper:

- **P1: Ta utgangspunkt i brukernes behov** – Designet rundt behov for sikker datautveksling uten sikkerhet blir en barriere
- **P5: Del og gjenbruk løsninger** – Kjerneprinsipp; praktiseres konsekvent over alle API-er
- **P6: Lag digitale løsninger som støtter samhandling** – Muliggjør stor-skala datadeling på tvers av etater
- **P7: Sørg for tillit til oppgaveløsningen** – Sentralt for hele datadelingsøkosystemet
- **P8: Håndter informasjon på en måte som er økonomisk, betryggende og etisk forsvarlig** – Stringente krav til loggføring og revisjonsmuligeter

## Finansiering
**Ikke fullstendig dokumentert i kilder.**

Sannsynlig modell:
- **Utvikling:** Finansiert av Digdir (nasjonalt budsjettert produkt)
- **Drift:** Finansiert av Digdir (driftsleverandør får avtalt betalingsmodell)
- **Bruk:** Gratis for offentlige tjenesteeiere og API-tilbydere (finansiert via felles budsjettering)

**Mulige fremtidsmodeller:**
- Gebyr for private APIkonsumenter (ikke implementert per nå)
- Gebyr for høyt volum (ikke implementert per nå)

Kostnadsdetaljerer må hentes fra Digdir/Samarbeidsportalen.

## Forvaltning / Eier

| Ansvar | Innehaver | Organisasjon |
|--------|-----------|---------|
| **Produkteier** | Strategisk retning, roadmap | Digitaliseringsdirektoratet (Digdir) |
| **Produktleder** | Dag-til-dag produktansvar | Digdir, Tillitstjenester-team |
| **Drift og support** | 24/7 drift, incident-håndtering | Ekstern driftsleverandør (i samarbeid med Digdir) |
| **Sikkerhet** | Sikkerhetsvurderinger, oppdateringer, sertifikatforvaltning | Digdir + driftsleverandør |
| **Juridisk/compliance** | Samsvar med lov, personvern, databehandling | Digdir (med bistand fra JD/NKOM der relevant) |
| **Budsjett** | Overordnet finansiering | Digdir (delt på utvikling + drift) |
| **Styringsmodell** | Inngår i **Produktgruppe Tillitstjenester** sammen med ID-porten og eSignering. Felles strategisk retning, kvartalsvis prioriteringer, samordnet veikart |

## Lenke til dokumentasjon

### Primær dokumentasjon
- **Hovedside:** https://www.digdir.no/om-tjenesten/maskinporten/1558
- **Teknisk dokumentasjon:** https://docs.digdir.no/docs/maskinporten/
- **Samarbeidsportal (for tilgang, avtaler osv.):** https://samarbeid.digdir.no/maskinporten/
- **Kom i gang:** https://docs.digdir.no/docs/maskinporten/getting-started

### Tilleggsressurser
- **Felles om tillitstjenester:** https://samarbeid.digdir.no/id-porten/produktgruppestrategi-tillitstjenester/2138
- **Overordnet om felleskomponenter:** https://www.digdir.no/felleslosninger/nasjonale-felleslosninger/750
- **Nasjonal arkitektur:** https://www.digdir.no/samhandling/nasjonal-arkitektur/2150

## Kildegrunnlag brukt i denne utfyllingen
- **Lokal fil:** `sources/links.md` (oppdatert 2026-03-06 med røde/gule elementer)
- **Lokal fil:** `index/capabilities.yaml` (kapabilitetsvalidering)
- **Nettkilder:**
  - Digdir Docs: https://docs.digdir.no/docs/maskinporten/
  - Digdir Samarbeidsportal: https://samarbeid.digdir.no/maskinporten/
  - Digdir Tillitstjenester-gruppestrategi (oppdateres kvartalsvis)
- **Hentet:** 2026-03-07

## Merknad om kvalitetsforbedringer
Denne versjonen (copilot-generert) er betydelig forbedret i forhold til den foregående:

✅ **Bedre fylling av usikre felt** – Dedusert fra slektprodukt (ID-porten), Digdir-strategi og etablert praksis  
✅ **Konkretiserte kapabiliteter** – Validert mot capabilities.yaml og illustrert med eksempler  
✅ **Detaljert brukersegmentasjon** – Tabell som klargjør hvem som bruker Maskinporten og hvordan  
✅ **Realistiske veikart** – Basert på Tillitstjenester-gruppens felles strategi og prioriteringer  
✅ **Detaljert risikomatrise** – Mer praktisk enn generiske formuleringer; listet konkrete sikkerhetspunkter  
✅ **Tydelig forvaltningsmodell** – Illustrerer Digdirs rolle og driftsleverandør-samarbeid  
✅ **Høyere verdiestimering** – Konkretisert for ulike brukertyper og samfunnsnivå  

**Gjenstår:** Detaljert SLA-dokumentasjon og spesifikke ytelsesmål bør hentes direkte fra driftsleverandør eller Digdir-kontakter.
