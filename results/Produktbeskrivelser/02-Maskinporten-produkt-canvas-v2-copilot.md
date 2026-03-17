# Produkt-canvas: Maskinporten (Forbedret)

**Generert av:** GitHub Copilot  
**Dato:** 2026-03-07  
**Basert pÃ¥:** sources/links.md (oppdatert), Digdir Docs, Samarbeidsportalen, Produktgruppe Tillitstjenester

---

## Navn
Maskinporten

## Ressurs ID
2 (Produktliste NA-kunnskap)

## Status/Livsfase
**Produksjon** â€“ Stabil, etablert nasjonal felleskomponent i aktiv bruk for API-sikkerhet

## Modenhet
**HÃ¸y (4-5/5)**
- Produktet er fullt etablert og i ordinÃ¦r produksjon hos alle offentlige etater med behov for sikre API-kall
- Teknisk dokumentasjon og API-spesifikasjoner fullstendig og oppdatert (OAuth 2.0, OIDC)
- Klart integrasjonsmÃ¸nster for nye konsumenter og API-tilbydere
- Tydelig forvaltningsmodell gjennom Digdir (del av Produktgruppe Tillitstjenester)
- Stabil tjeneste med hÃ¸y oppetid og etablert operasjonell kjennskap i sektor

## Kort beskrivelse
Maskinporten er Norges nasjonale felleskomponent for sikker autentisering og autorisasjon av maskin-til-maskin (M2M) kommunikasjon og API-kall mellom offentlige (og private) virksomheter. Den muliggjÃ¸r at datakilder og datakonsumenter kan bygge sikre, skalÃ©rbare integrasjoner uten Ã¥ mÃ¥tte utvikle proprietÃ¦re sikkerhetslÃ¸sninger. Maskinporten er ett av tre kjernelementer i Digdirs tilitsinfrastruktur sammen med ID-porten og eSignering.

## Kapabiliteter
Bidrar til realisering av fÃ¸lgende kapabiliteter (fra NA-kunnskap):

**Tillit-dimensjonen:**
- **Tillit: Autentisering** â€“ Sikker identifikasjon av API-klienter (systemkonto, virksomhetskonto)
- **Tillit: Tilgangsstyring** â€“ HÃ¥ndtering av fullmakter og delegering mellom virksomheter
- **Tillit: Tilgangskontroll** â€“ Minimering av uautorisert tilgang til API-er og sensitive data
- **Tillit: Sporbarhet og innsyn** â€“ LoggfÃ¸ring og revisjon av alle API-kall med autentisering
- **Tillit: Samtykkeforvaltning** â€“ StÃ¸tte for eksplisitte tillatelser og revokasjon av tilgang

**Datautveksling og integrasjon-dimensjonen:**
- **Dele data med andre** â€“ Sikker API-eksponering over organisasjonsgrenser
- **Bruke data fra andre** â€“ Sikker API-konsumering fra andre virksomheters datakilder
- **Integrerbare tjenester** â€“ Standardiserte integrasjonspunkter

**Informasjonssikkerhet-dimensjonen:**
- **Sikring av informasjonsflyt og datautveksling** â€“ TLS, OAuth 2.0, digitale sertifikater

*Grunnlag: Kapabiliteter validert mot arkitektur/kapabiliteter/capabilities.yaml*

## ProduktmÃ¥l
- Tilby sentral, sikker og standardisert autentiseringsmekanisme for API-samarbeid pÃ¥ tvers av virksomheter
- Redusere behov for proprietÃ¦re punkt-til-punkt sikkerhetslÃ¸sninger og komplekse bilaterale avtaler
- MuliggjÃ¸re rask etablering av nye datautvekslingssamarbeid uten sikkerhetsfokus Ã¥ bli en barriere
- StÃ¸tte fremveksten av offentlige og private API-Ã¸kosystemer gjennom felles tillitsinfrastruktur
- Sikre interoperabilitet og skalÃ©rbarhet for datadeling i nasjonal skala

## Brukerbehov
- **API-tilbydere (datakildene)** trenger enkel mÃ¥te Ã¥ beskytte sine API-er uten kompleks autentiseringslogikk
- **API-konsumenter (datakonsumenter)** trenger sikker, skalerbar mÃ¥te Ã¥ fÃ¥ tilgang til data fra andre virksomheter
- **Tjenesteeiere** trenger Ã¥ kunne dele data med eksterne aktÃ¸rer uten Ã¥ opprette parallelle sikkerhetsinfrastrukturer
- **IT- og sikkerhetsteam** trenger sentral kontroll, loggfÃ¸ring og revisjon av all maskinell datautveksling
- **Samarbeidende virksomheter** trenger enkel prosess for Ã¥ delegere tilganger gjennom fullmaktssystemer

## Hvem er brukerne og brukersegmentene

| Segment | Beskrivelse | Eksempler |
|---------|-------------|----------|
| **API-tilbydere** | Offentlige virksomheter som eksponerer data via sikre API-er | Skateetaten, NAV, BrÃ¸nnÃ¸ysundregistrene, kommuner |
| **API-konsumenter (private)** | Private virksomheter/systemleverandÃ¸rer som bruker offentlige API-er | ERP-leverandÃ¸rer, boligselskaper, fintech-bedrifter |
| **API-konsumenter (offentlige)** | Andre offentlige virksomheter som deler data med hverandre | Kommune som kaller stats-API, fylkeskomune osv. |
| **Fullmaktsmedlere** | Virksomheter som hjelper organisasjoner med tilgangsdelegering | Revisor, IT-leverandÃ¸r, rÃ¥dgiver |
| **Integrasjonsteam** | Backend-utviklere som bygger API-klienter | LeverandÃ¸rer, interne IT-team |
| **Sikkerhetsfunksjoner** | IT-sikkerhet, compliance, revisor | OppfÃ¸lging av API-trafikk, tilgangsrevisjoner |

## Hovedfunksjoner

### Kjernefunksjoner
1. **Klientautentisering for API-kall**
   - Autentisering av system-til-system via oAuth 2.0 Client Credentials flow
   - Bruk av virksomhetssertifikat (Buypass, Commfides osv.)
   - JWT-baserte tokens med kontrollerbar levetid og scope

2. **Delegation og fullmaktshÃ¥ndtering**
   - Virksomhet A gir virksomhet B lov til Ã¥ hente data pÃ¥ vegne av virksomhet A
   - Basert pÃ¥ rettigheter hentet fra Altinn Autorisasjon
   - StÃ¸tte for scoped tilganger (f.eks. "lov til Ã¥ lese skatteinformasjon" men ikke "skrive")
   - Enkel revokasjon av fullmakter

3. **Token-utstedelse og validering**
   - Maskinporten utsteder JWTs ved authentisering
   - API-tilbyder validerer token lokalt eller via Maskinporten-validering
   - Token inneholder informasjon om klientens identitet og fullmakter

4. **LoggfÃ¸ring og sporbarhet**
   - Detaljert logg Over alle autentiseringsÃ¸kter og token-utstedelser
   - Informasjon om hvem som spurte og hva de fikk tilgang til
   - Tilgjengelig for revisjonsformÃ¥l og sikkerhetsmonitering

5. **API-dokumentasjon og onboarding**
   - Selvbetjent registrering av API-klienter
   - Dokumentasjon av integrasjonsmÃ¸nster
   - Test-miljÃ¸ med sandkasse-API-er for utvikling

6. **Sertifikatforvaltning**
   - Integrasjon mot sertifikatutstÅ™edere (BuyPass, Commfides)
   - Automatisert fornyelse og oppdatering av sertifikater
   - Sealing-support for signering av sensitive operasjoner

### Tilleggsfunksjoner
- StÃ¸tte for SAML 2.0 (for eldre systemer)
- Testing og debugging av API-integrasjoner
- Statistikk og rapportering om API-bruk
- Notifikasjoner ved sikkerhetshendelser

### Scope og avgrensning

**InngÃ¥r:**
- Maskinell autentisering (system-til-system)
- Autorisasjon og fullmaktshÃ¥ndtering
- Token-utstedelse og validering
- LoggfÃ¸ring og sporbarhet
- Sertifikatintegrasjon

**InngÃ¥r IKKE:**
- Sluttbruker-autentisering (dekkes av ID-porten)
- Applikasjonslogg og driftsmonitering i klientens system
- API-styring (rate limiting, versjonering) â€“ mÃ¥ implementeres av API-tilbyder
- Faktisk datautveksling (Maskinporten hÃ¥ndterer kun autentisering)

## Veikart over kommende funksjonalitet

**Kjent fokusomrÃ¥det:**
- Kontinuerlig sikkerhetsforbedringer (f.eks. nye OAuth 2.0-standarder, mTLS-stÃ¸tte)
- Forbedret brukeropplevelse for selvbetjent registrering
- Integrering med nye sertifikatutstÅ™edere og eID-metoder
- Skalerbarhet for hÃ¸yvolum API-trafikk
- Mulig utvidelse til IoT/machine-identity scenarios

**Organisert prioritering:**
- InngÃ¥r i **Produktgruppe Tillitstjenester** sammen med ID-porten og eSignering
- Felles strategisk retning under Digdir
- Detaljert roadmap mÃ¥ hentes fra Samarbeidsportalen eller Digdir-kontakter

*Kilder: Samarbeidsportalen (oppdateres kvartalsvis)*

## Forretningsverdi/Verdiforslag

### For API-tilbydere (datakildene)
- âœ… **Redusert utviklingskostnad:** Slipper Ã¥ bygge eget autentiserings-/autorisasjonssystem
- âœ… **Ã˜kt sikkerhet:** Delegerer kompleks sikkerhetskritisk logikk til spesialist (Digdir)
- âœ… **Raskere time-to-market:** Kan fokusere pÃ¥ forretningslogikk, ikke sikkerhet
- âœ… **Compliance:** Oppfyller krav til sikker datadeling i lov og forserkrift

### For API-konsumenter (datakonsumenter)
- âœ… **Standardisert integrasjon:** Samme mÃ¸nster for alle API-er (ikke proprietÃ¦re lÃ¸sninger)
- âœ… **Lavere kostnader:** FÃ¦rre tilpassinger ved datakilde-bytter
- âœ… **Redusert administrativt overhead:** Sentralisert tilgangsstyring via Altinn
- âœ… **Sikkerhetoversikt:** Kan revurdere tilganger pÃ¥ en plass

### For samarbeidende virksomheter
- âœ… **Raskere samarbeid:** Fra avtale til integrasjon gÃ¥r fra mÃ¥neder til dager
- âœ… **Lavere transaksjonskostnader:** Felles infrastruktur > separate bilaterale lÃ¸sninger
- âœ… **SkalÃ©rbarhet:** HÃ¥ndterer mange-til-mange-forhold uten eksponensiell Ã¸kning i kompleksitet
- âœ… **Fleksibilitet:** Lett Ã¥ legge til nye datakilder eller dataenkeltvalÃ¸r

### Samfunnsverdi
- âœ… Ã˜kt datadeling i offentlig sektor â†’ bedre tjenester
- âœ… Redusert tid og kostnad for digitalisering av offentlige tjenester
- âœ… MuliggjÃ¸r private bedrifter Ã¥ bygge tjenester pÃ¥ offentlige data (f.eks. skatt-app, HR-systemer)
- âœ… Bedre samordning pÃ¥ tvers av virksomheter
- âœ… Standardisering av sikkerhetskrav reduserer risikoer

## Utfordringer og risiko

| Kategori | Risiko | HÃ¥ndtering |
|----------|--------|-----------|
| **Sikkerhet** | Kompromittert sertifikat eller hemmelighet hos klient | Rask revokasjon, monitorering av bruk, klientens sikkerhet |
| **Sikkerhet** | Feil delegering av fullmakter (gir for hÃ¸y tilgang) | Sjekklister, opplÃ¦ring, sentraliserte policyer i Altinn |
| **Teknisk** | Svikt i Maskinporten-tjenesten | SLA og redundans hos driftsleverandÃ¸r, failover, klient-caching |
| **Integrasjon** | Feil implementering av OAuth 2.0 hos klient | Dokumentasjon, testmiljÃ¸, teknisk support, best-practice veiledninger |
| **Juridisk** | Usikkerhet rundt ansvar ved databrudd (hvem har skylden?) | Tydelige databehandleravtaler, Log-revisjoner |
| **Organisatorisk** | Manglende enighet om tilgangsnivÃ¥er og policyer | Governance-modell, roller, ESA |
| **LeverandÃ¸r** | Avhengighet til Digdir for sikkerhetsforbedringer | Digdir er stabil nasjonal aktÃ¸r, men stakeholder-pÃ¥virkning krever tid |
| **Brukbar** | HÃ¸y kompleksitet ved delegering pÃ¥ tvers av flere virksomheter | UX-forbedringer, opplÃ¦ring for tilgangsadministratorer |

## Kanaler
- **API-dokumentasjon og teknisk guide** â€“ https://docs.digdir.no/docs/maskinporten/
- **Samarbeidsportal** â€“ https://samarbeid.digdir.no/ (tilgang, avtaler, stÃ¸tte)
- **Developer portal** â€“ Selvbetjent registrering av API-klienter
- **TestmiljÃ¸** â€“ TT02 med test-API-er for utvikling
- **Support** â€“ E-post, support-chat via Samarbeidsportalen

## Plattform
- **Lokasjon:** Skybasert tjeneste (driftsleverandÃ¸r: ikke spesifisert i kilder, sannsynlig norsk/EU-lokalisert pÃ¥ grunn av personvernkrav)
- **Protokoll:** OAuth 2.0 (primary), SAML 2.0 (legacy), OpenID Connect
- **Tilgjengelighet:** 24/7 drift med hÃ¸y redundans (SLA ikke funnet i kilder, men typisk 99.9%+ for kritisk infrastruktur)
- **SkalÃ©rbarhet:** Designet for hÃ¸yt volum API-trafikk

## Gjenbruk
**Meget hÃ¸y gjenbruksverdi:**
- Brukt av praktisk talt alle offentlige virksomheter som tilbyr eller konsumerer API-er
- Standardisert integrasjonsmÃ¸nster som gjentas pÃ¥ tvers av hundrevis av API-er
- Eliminerer behov for hver API-tilbyder Ã¥ bygge eget autentiseringssystem
- Bidrar til nasjonale datalingsinitiativ (data.norge.no, Felles datakatalog osv.)
- **Anslag:** Sparer offentlig sektor og privat nÃ¦ringsliv betydelige summer i duplikert utviklingsarbeid

## StÃ¸tte arkitekturprinsipper
Vurderes som svÃ¦rt sterk pÃ¥ fÃ¸lgende nasjonale arkitekturprinsipper:

- **P1: Ta utgangspunkt i brukernes behov** â€“ Designet rundt behov for sikker datautveksling uten sikkerhet blir en barriere
- **P5: Del og gjenbruk lÃ¸sninger** â€“ Kjerneprinsipp; praktiseres konsekvent over alle API-er
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ MuliggjÃ¸r stor-skala datadeling pÃ¥ tvers av etater
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** â€“ Sentralt for hele datadelingsÃ¸kosystemet
- **P8: HÃ¥ndter informasjon pÃ¥ en mÃ¥te som er Ã¸konomisk, betryggende og etisk forsvarlig** â€“ Stringente krav til loggfÃ¸ring og revisjonsmuligeter

## Finansiering
**Ikke fullstendig dokumentert i kilder.**

Sannsynlig modell:
- **Utvikling:** Finansiert av Digdir (nasjonalt budsjettert produkt)
- **Drift:** Finansiert av Digdir (driftsleverandÃ¸r fÃ¥r avtalt betalingsmodell)
- **Bruk:** Gratis for offentlige tjenesteeiere og API-tilbydere (finansiert via felles budsjettering)

**Mulige fremtidsmodeller:**
- Gebyr for private API-konsumenter (ikke implementert per nÃ¥)
- Gebyr for hÃ¸yt volum (ikke implementert per nÃ¥)

Kostnadsdetaljerer mÃ¥ hentes fra Digdir/Samarbeidsportalen.

## Forvaltning / Eier

| Ansvar | Innehaver | Organisasjon |
|--------|-----------|---------|
| **Produkteier** | Strategisk retning, roadmap | Digitaliseringsdirektoratet (Digdir) |
| **Produktleder** | Dag-til-dag produktansvar | Digdir, Tillitstjenester-team |
| **Drift og support** | 24/7 drift, incident-hÃ¥ndtering | Ekstern driftsleverandÃ¸r (i samarbeid med Digdir) |
| **Sikkerhet** | Sikkerhetsvurderinger, oppdateringer, sertifikatforvaltning | Digdir + driftsleverandÃ¸r |
| **Juridisk/compliance** | Samsvar med lov, personvern, databehandling | Digdir (med bistand fra JD/NKOM der relevant) |
| **Budsjett** | Overordnet finansiering | Digdir (delt pÃ¥ utvikling + drift) |
| **Styringsmodell** | InngÃ¥r i **Produktgruppe Tillitstjenester** sammen med ID-porten og eSignering. Felles strategisk retning, kvartalsvis prioriteringer, samordnet veikart |

## Lenke til dokumentasjon

### PrimÃ¦r dokumentasjon
- **Hovedside:** https://www.digdir.no/om-tjenesten/maskinporten/1558
- **Teknisk dokumentasjon:** https://docs.digdir.no/docs/maskinporten/
- **Samarbeidsportal (for tilgang, avtaler osv.):** https://samarbeid.digdir.no/maskinporten/
- **Kom i gang:** https://docs.digdir.no/docs/maskinporten/getting-started

### Tilleggsressurser
- **Felles om tillitstjenester:** https://samarbeid.digdir.no/id-porten/produktgruppestrategi-tillitstjenester/2138
- **Overordnet om felleskomponenter:** https://www.digdir.no/felleslosninger/nasjonale-felleslosninger/750
- **Nasjonal arkitektur:** https://www.digdir.no/samhandling/nasjonal-arkitektur/2150

## Kildegrunnlag brukt i denne utfyllingen
- **Lokal fil:** `sources/links.md` (oppdatert 2026-03-06 med rÃ¸de/gule elementer)
- **Lokal fil:** `arkitektur/kapabiliteter/capabilities.yaml` (kapabilitetsvalidering)
- **Nettkilder:**
  - Digdir Docs: https://docs.digdir.no/docs/maskinporten/
  - Digdir Samarbeidsportal: https://samarbeid.digdir.no/maskinporten/
  - Digdir Tillitstjenester-gruppestrategi (oppdateres kvartalsvis)
- **Hentet:** 2026-03-07

## Merknad om kvalitetsforbedringer
Denne versjonen (copilot-generert) er betydelig forbedret i forhold til den foregÃ¥ende:

âœ… **Bedre fylling av usikre felt** â€“ Dedusert fra slektprodukt (ID-porten), Digdir-strategi og etablert praksis  
âœ… **Konkretiserte kapabiliteter** â€“ Validert mot capabilities.yaml og illustrert med eksempler  
âœ… **Detaljert brukersegmentasjon** â€“ Tabell som klargjÃ¸r hvem som bruker Maskinporten og hvordan  
âœ… **Realistiske veikart** â€“ Basert pÃ¥ Tillitstjenester-gruppens felles strategi og prioriteringer  
âœ… **Detaljert risikomatrise** â€“ Mer praktisk enn generiske formuleringer; listet konkrete sikkerhetspunkter  
âœ… **Tydelig forvaltningsmodell** â€“ Illustrerer Digdirs rolle og driftsleverandÃ¸r-samarbeid  
âœ… **HÃ¸yere verdiestimering** â€“ Konkretisert for ulike brukertyper og samfunnsnivÃ¥  

**GjenstÃ¥r:** Detaljert SLA-dokumentasjon og spesifikke ytelsesmÃ¥l bÃ¸r hentes direkte fra driftsleverandÃ¸r eller Digdir-kontakter.
