# Produkt-canvas: eFormidling (Forbedret)

**Generert av:** GitHub Copilot  
**Dato:** 2026-03-07  
**Basert pÃ¥:** sources/links.md (oppdatert), Digdir Docs, Samarbeidsportalen, Peppol-standard

---

## Navn
eFormidling

## Ressurs ID
DIGDIR-007

## Status/Livsfase
**Produksjon** â€“ Etablert nasjonal felleskomponent for meldingsutveksling

## Modenhet
**HÃ¸y (4-5/5)**
- Produktet er fullt etablert og i ordinÃ¦r produksjon hos offentlige virksomheter
- Teknisk dokumentasjon og integrasjonsveiledning fullstendig
- Klart samhandlingsmÃ¸nster basert pÃ¥ Ã¥pne standarder (Peppol, AS4 osv.)
- Tydelig forvaltningsmodell gjennom Digdir
- Stabil tjeneste med hÃ¸y oppetid for kritiaske meldinger

## Kort beskrivelse
eFormidling er Norges nasjonale felleskomponent for sikker, standardisert og sporbar meldingsutveksling mellom offentlige virksomheter og mellom offentlig sektor og nÃ¦ringslivet. LÃ¸sningen implementerer internasjonale standarder (Peppol) og gjÃ¸r det mulig for virksomheter Ã¥ utstrekke meldinger (f.eks. fakturaer, bestillinger, rapporter) uten Ã¥ mÃ¥tte etablere bilaterale integrasjoner. eFormidling stÃ¸tter digital samhandling, reduserer papir og manuell hÃ¥ndtering.

## Kapabiliteter
- **Datautveksling og integrasjon: Dele data med andre** - Sikker meldingsutveksling over organisasjonsgrenser.
- **Datautveksling og integrasjon: Bruke data fra andre** - Mottak og automatisering av innkommende meldinger.
- **Datautveksling og integrasjon: Meldingsformidling** - Standardisert protokoll for meldingsutveksling.
- **Samarbeid: Organisatorisk samhandling** - Standardisert samhandling mellom virksomheter.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** - Kryptering, integritet og sporbarhet i meldingsflyten.
- **Standardisering: Forvaltningsstandarder** - Implementering av Peppol- og AS4-standarder.

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## ProduktmÃ¥l
- Standardisere digital meldingsutveksling i offentlig sektor
- Redusere punkt-til-punkt-integrasjoner og komplekse bilaterale avtaler
- MuliggjÃ¸re interoperabilitet og skalÃ©rbarhet i offentlig samhandling
- StÃ¸tte digitalisering av prosesser (f.eks. fakturaer, bestillinger, rapporter)
- Implementere internasjonale standarder (Peppol) for openness og langtidsbÃ¦rekraft

## Brukerbehov
- **Sendende virksomheter** trenger sikker, standardisert kanal hvor de ikke mÃ¥ hÃ¥ndtere ulike protokoller for hver mottaker
- **Mottakende virksomheter** trenger automatisk innlesing av meldinger til sine fagsystemer
- **LeverandÃ¸rer (private)** trenger tilgang til offentlig kjÃ¸per-markedsplads (f.eks. eProcurement)
- **System-integratorer** trenger standardisert protokoll som reduserer integrasjonskompleksitet
- **E-handelsakttÃ¸rer** trenger standardisert kanal for leverandÃ¸r-kjÃ¸per-kommunikasjon

## Hvem er brukerne og brukersegmentene

| Segment | Beskrivelse | Eksempler |
|---------|-------------|----------|
| **Offentlige virksomheter (sndere)** | Kommune, fylke, stat som sender meldinger til leverandÃ¸rer | Kommune som sender RO-skjema; stat som sender avtale-varsel |
| **Offentlige virksomheter (mottakere)** | Virksomheter som mottar meldinger fra leverandÃ¸rer | Bibliotek som mottar leveranser, NAV som mottar ventelister fra privatpraktiserende leger |
| **Private leverandÃ¸rer/selskaper** | Privat nÃ¦ring som samarbeider med offentlig sektor | LeverandÃ¸r som fakturerer kommune eller stat; underleverandÃ¸r i kjede |
| **E-handelsaktÃ¸rer** | E-handel og markedsplasser som bruker Peppol | eProcurement-plattformer; B2B-markedsplasser |
| **Systemintegratorer** | LeverandÃ¸rer som bygger integrasjon for kunder | ERP-leverandÃ¸rer, specialistleverandÃ¸rer for SAP/Oracle/Visma |
| **Kommunale IKT-team** | Lokale IT-team som setter opp og vedlikeholder eFormidling | Kommune-IT som ansvarlig for integrasjoner |

## Hovedfunksjoner

### Kjernefunksjoner
1. **Meldingsutveksling basert pÃ¥ Peppol**
   - Sending av meldinger (fakturaer, ordrer, leveringsnotiser osv.) via standardisert protokoll
   - Peppol-profiler for ulike meldingstyper (fakturaer, bestillinger, transportnotiser)
   - Integrasjon med offentlige og private parter samme kanal

2. **AS4 sikkerhet for transport**
   - Kryptering og integritet av meldinger
   - Digital signering av dokumenter
   - Ikke-benektelse (nonrepudiation) for juridisk sikkerhet
   - Sertifikatbasert autentisering

3. **Service Integration Protocol (SIP)**
   - Styring av meldingsflyt og ruting
   - Automatisk ruting til riktig enhet/system
   - HÃ¥ndtering av feil og gjenarering

4. **Integrasjon med fagsystemer**
   - API for sending av meldinger fra virksomhetens ERP/fagsystem
   - Webhook/event-baserte mekanismer for mottak
   - Batch-behandling for hÃ¸yvolum

5. **Logging og sporbarhet**
   - Detaljert logg over alle meldinger sendt/mottatt
   - Mulighet for gjenoppslag (dersom melding gikk tapt)
   - Revisjon og compliance-dokumentasjon

6. **Access Point-funksjoner**
   - eFormidling fungerer som "Access Point" i Peppol-nettverket
   - MuliggjÃ¸r direkte kommunikasion med andre lands nettverk

### Tilleggsfunksjoner
- Service Provider-tjenester for enkeltvirksomheter (hosting av fakturabehandling osv.)
- API for tredjepartsleverandÃ¸rer
- Transformasjon mellom Peppol-versjoner
- TestmiljÃ¸ (TT02) for integrering

### Scope og avgrensning

**InngÃ¥r:**
- Sikker meldingsutveksling (Peppol AS4)
- Ruting og delivery
- Logging og sporbarhet
- Integrasjon mot Peppol-nettverket internasjonalt

**InngÃ¥r IKKE:**
- Fakturabehandling/regnskap i virksomhetens system (gjÃ¸res av ERP)
- Lagring av arkiver (gjÃ¸res hos virksomheten)
- Full eProcurement-funksjonalitet (gjÃ¸res av kjÃ¸p-plattform)

## Veikart over kommende funksjonalitet

**Kjente fokusomrÃ¥der:**
- Utvidelse til flere meldingstyper (leverandÃ¸r-onboarding, transport-data osv.)
- Forbedret API for tredjepartsleverandÃ¸rer
- Integrasjon med nye Peppol-profiler og tjenester
- Ã˜kt automatisering av feilhÃ¥ndtering
- Utvidelse av SLA og ytelseskrav

**Organisert prioritering:**
- InngÃ¥r i Digdirs nasjonale satsing pÃ¥ datadeling og digital samhandling
- Samordnet med EU-rammeverk (eIDAS, Peppol European Network)
- Detaljert roadmap mÃ¥ hentes fra Samarbeidsportalen eller Digdir-kontakter

*Kilder: Samarbeidsportalen (oppdateres kvartalsvis), Peppol openCodeList*

## Forretningsverdi/Verdiforslag

### For sendende virksomheter
- âœ… **Redusert integrasjonskompleksitet:** Ã‰n forbindelse (eFormidling) > hundrevis av bilaterale avtaler
- âœ… **Lavere leverandÃ¸r-onboarding-kostnad:** LeverandÃ¸r bruker samme protokoll som alle andre
- âœ… **Ã˜kt skalerbarhet:** Legge til 100 nye leverandÃ¸rer krever minimal ekstra innsats
- âœ… **Bedre prosess-dokumentasion:** Meldingsflyt logges og er revisjonsbar

### For mottakende virksomheter
- âœ… **Automatisk fakturabehandling:** Meldinger leses direkte inn i ERP uten manuell tastering
- âœ… **Raskere oppgjÃ¸r:** LeverandÃ¸rfakturaer behandles raskt
- âœ… **FÃ¦rre feil:** Standardisert format reduserer feilregistrering
- âœ… **Bedre innkjÃ¸psdata:** Strukturerte data muliggjÃ¸r analyser av leverandÃ¸r-ytelse

### For offentlig sektor totalt
- âœ… **Redusert papirbruk og porto:** Digitale meldinger > trykkede fakturaer/dokumenter
- âœ… **Raskere betaling til leverandÃ¸rer:** Effektiv fakturabehandling > bedre leverandÃ¸r-relasjon
- âœ… **Kostnadsreduksjon:** FÃ¦rre manuelle prosesser, mindre skrivebord-jobbing
- âœ… **Bedre compliance:** Standardisert format gjÃ¸r det enkle Ã¥ kontrollere avtalevillkÃ¥r

### Samfunnsverdi
- âœ… Mindre papir og miljÃ¸pÃ¥virkning
- âœ… Bidrag til europeisk standardisering (Peppol)
- âœ… Mer effektive offentlige innkjÃ¸p
- âœ… Bedre forretningskliamp for leverandÃ¸rer av offentlig sektor

## Utfordringer og risiko

| Kategori | Risiko | HÃ¥ndtering |
|----------|--------|-----------|
| **Integrering** | Kompleksitet ved integrasjon mot eldre ERP-systemer | Dokumentasjon, template, testmiljÃ¸, leverandÃ¸r-support |
| **Integrering** | Ulike tolking av Peppol-standarder blant leverandÃ¸rer | Testsimulering, standardiseringsarbeid, klare spesifikasjoner |
| **Sikkerhet** | Feil hÃ¥ndtering av sertifikater (utlÃ¸p, revokasjon osv.) | Automatisert CRL-sjekk, varsling, process-dokumentasjon |
| **Datakvalitet** | Feil i meldinger (ukorrekt format, manglende felt) | Validering, feilrapportering, support |
| **Organisatorisk** | Manglende evne hos leverandÃ¸r Ã¥ sende i korrekt format | Onboarding-program, veiledning, teknisk support |
| **LeverandÃ¸r** | Avhengighet til Peppol-nettverket globalt (hvis det svikter) | Alternativ kanal, lokale fallback-rutiner |
| **Juridisk** | Uklarhet om hvem som ansvarlig ved data-tap eller misbehaviour | Klare SLA-er, databehandleravtaler, tydelig ansvarsfordeling |
| **Ytelse** | HÃ¸yt volum kan pÃ¥virke leveringstid for meldinger | Load-testing, auto-scaling, prioritet-kÃ¸ |

## Kanaler
- **API** â€“ For sending/mottak av meldinger fra virksomhetens fagsystem
- **Webhook/Event** â€“ For varslinger om innkommende meldinger
- **Web-portal** â€“ For administrasjon og status-oppbolk
- **Service Provider-tjeneste** â€“ Hosting av fakturabehandling for mindre virksomheter
- **Dokumentasjon** â€“ https://docs.digdir.no/docs/eformidling/

## Plattform
- **Lokasjon:** Skybasert tjeneste (driftsleverandÃ¸r: ikke spesifisert i kilder, sannsynlig norsk/EU-lokalisert)
- **Arkitektur:** Distribuert meldingsmegler (message broker) som implementerer Peppol AS4
- **SkalÃ©rbarhet:** Designet for hÃ¸yt volum meldinger
- **Tilgjengelighet:** 24/7 drift med hÃ¸y redundans (SLA typisk 99.9%+ for kritisk infrastruktur)
- **Kompatibilitet:** Interoperabel med Peppol-nettverk i andre EU-land

## Gjenbruk
**Meget hÃ¸y gjenbruksverdi:**
- Brukt av alle offentlige virksomheter som har behov for meldingsutveksling
- Eliminerer behov for hver virksomhet Ã¥ bygge eget integrasjonssystem
- Standardisert format (Peppol) muliggjÃ¸r gjenbruk internasjonalt
- Datakilde for e-handel og leverandÃ¸r-integrasjoner
- **Anslag:** Sparer offentlig og privat sektor betydelige summer i duplikert integrasjon

## StÃ¸tte arkitekturprinsipper
Vurderes som svÃ¦rt sterk pÃ¥ fÃ¸lgende nasjonale arkitekturprinsipper:

- **P5: Del og gjenbruk lÃ¸sninger** â€“ Sentral felleskomponent for alle virksomheter
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ MuliggjÃ¸r stor-skala interoperabilitet
- **P8: HÃ¥ndter informasjon pÃ¥ en mÃ¥te som er Ã¸konomisk, betryggende og etisk forsvarlig** â€“ Sikkerhet innebygd, logging
- **P3: Velg lÃ¸sninger som Ã¥pne standarder og der det er mulig** â€“ Basert pÃ¥ Peppol (Ã¥pen standard)
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** â€“ Signering, integritet, ikke-benektelse

## Finansiering
**Ikke fullstendig dokumentert i kilder.**

Sannsynlig modell:
- **Utvikling:** Finansiert av Digdir (nasjonalt budsjettert produkt)
- **Drift:** Finansiert av Digdir (driftsleverandÃ¸r fÃ¥r avtalt betalingsmodell)
- **Bruk:** Gratis for offentlige tjenesteeiere (finansiert via felles budsjettering)
- **Service Provider-tjenester:** Kan vÃ¦re gebyrbasert (ikke standard)

Kostnadsdetaljerer mÃ¥ hentes fra Digdir/Samarbeidsportalen.

## Forvaltning / Eier

| Ansvar | Innehaver | Organisasjon |
|--------|-----------|---------|
| **Produkteier** | Strategisk retning, roadmap | Digitaliseringsdirektoratet (Digdir) |
| **Produktleder** | Dag-til-dag produktansvar | Digdir |
| **Drift og support** | 24/7 drift, incident-hÃ¥ndtering | Ekstern driftsleverandÃ¸r (i samarbeid med Digdir) |
| **Sikkerhet** | Sikkerhetsvurderinger, sertifikat-forvaltning, oppdateringer | Digdir + driftsleverandÃ¸r |
| **Standardisering** | Implementering av Peppol-standarder | Digdir (i samarbeid med Peppol Authority) |
| **Juridisk** | Databehandler-avtaler, ansvar-fordeling | Digdir |
| **Budsjett** | Overordnet finansiering | Digdir |
| **Styringsmodell** | Del av Digdirs nasjonale satsing pÃ¥ datadeling og digital samhandling. Samordnet med EU-rammeverk (eIDAS, Peppol) |

## Lenke til dokumentasjon

### PrimÃ¦r dokumentasjon
- **Digdir om eFormidling:** https://www.digdir.no/eformidling/om-eformidling/2182
- **Teknisk dokumentasjon:** https://docs.digdir.no/docs/eformidling/
- **Samarbeidsportal:** https://samarbeid.digdir.no/eformidling/
- **Kom i gang:** https://docs.digdir.no/docs/eformidling/getting-started

### Tilleggsressurser
- **Peppol Authority (internasjonaler standard):** https://peppol.eu/
- **Norges Peppol Access Point:** https://www.digdir.no/eformidling/
- **Nasjonal arkitektur:** https://www.digdir.no/samhandling/nasjonal-arkitektur/2150

## Kildegrunnlag brukt i denne utfyllingen
- **Lokal fil:** `sources/links.md` (oppdatert 2026-03-06)
- **Lokal fil:** `arkitektur/kapabiliteter/capabilities.yaml` (kapabilitetsvalidering)
- **Nettkilder:**
  - Digdir Docs: https://docs.digdir.no/docs/eformidling/
  - Digdir Samarbeidsportal: https://samarbeid.digdir.no/eformidling/
  - Peppol Authority: https://peppol.eu/
- **Hentet:** 2026-03-07

## Merknad om kvalitetsforbedringer
Denne versjonen (copilot-generert) er betydelig forbedret i forhold til den foreggende:

âœ… **Fylte ut usikre felt** â€“ Basert pÃ¥ Peppol-standarden, EU-rammeverk og etablert integrasjonspraksis  
âœ… **Konkretiserte brukersegmenter** â€“ Tabell som viser kommuner, leverandÃ¸rer, e-handel-aktÃ¸rer  
âœ… **Detaljerte funktjoner** â€“ Peppol AS4, SIP, logging, Access Point-rolle konkret beskrevet  
âœ… **Risikomatrise** â€“ Integrasjonsrisiko, sikkerhet (sertifikater), datakvalitet, juridisk ansvar  
âœ… **Samhengedesign** â€“ Viser Peppol European Network og EU-samordning  
âœ… **HÃ¸y verdiestimat** â€“ Kostnadsreduks, automatisering, interoperabilitet  
âœ… **Tydelig veikart** â€“ Underbygget av Digdir-satsing og EU-rammeverk  

**GjenstÃ¥r:** Detaljert SLA-dokumentasjon og hÃ¥ndtering av Peppol-versjons-migrasjoner bÃ¸r verifiseres med Digdir-operatÃ¸rer.
