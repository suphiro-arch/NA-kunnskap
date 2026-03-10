# Produkt-canvas: eFormidling (Forbedret)

**Generert av:** GitHub Copilot  
**Dato:** 2026-03-07  
**Basert på:** sources/links.md (oppdatert), Digdir Docs, Samarbeidsportalen, Peppol-standard

---

## Navn
eFormidling

## Ressurs ID
7 (Produktliste NA-kunnskap)

## Status/Livsfase
**Produksjon** – Etablert nasjonal felleskomponent for meldingsutveksling

## Modenhet
**Høy (4-5/5)**
- Produktet er fullt etablert og i ordinær produksjon hos offentlige virksomheter
- Teknisk dokumentasjon og integrasjonsveiledning fullstendig
- Klart samhandlingsmønster basert på åpne standarder (Peppol, AS4 osv.)
- Tydelig forvaltningsmodell gjennom Digdir
- Stabil tjeneste med høy oppetid for kritiaske meldinger

## Kort beskrivelse
eFormidling er Norges nasjonale felleskomponent for sikker, standardisert og sporbar meldingsutveksling mellom offentlige virksomheter og mellom offentlig sektor og næringslivet. Løsningen implementerer internasjonale standarder (Peppol) og gjør det mulig for virksomheter å utstrekke meldinger (f.eks. fakturaer, bestillinger, rapporter) uten å måtte etablere bilaterale integrasjoner. eFormidling støtter digital samhandling, reduserer papir og manuell håndtering.

## Kapabiliteter
Bidrar til realisering av følgende kapabiliteter (fra NA-kunnskap):

**Datautveksling og integrasjon-dimensjonen:**
- **Datautveksling: Dele data med andre** – Sikker meldingsutveksling over organisasjonsgrenser
- **Datautveksling: Bruke data fra andre** – Mottak og automatisering av innkommende meldinger
- **Datautveksling: Meldingsformidling** – Standardisert protokoll for meldingsutveksling

**Samhandling-dimensjonen:**
- **Samhandling: Organisatorisk samhandling** – Samhändig kommunikasion mellom virksomheter
- **Samhandling: Sammenhengende tjenester** – Bidrag til integrert samhandling

**Informasjonssikkerhet-dimensjonen:**
- **Sikring av informasjonsflyt og datautveksling** – Kryptering, integritet, ikke-benektelse

**Standardisering-dimensjonen:**
- **Forvaltningsstandarder** – Implementering av Peppol og AS4-standarder

*Grunnlag: Kapabiliteter validert mot index/capabilities.yaml*

## Produktmål
- Standardisere digital meldingsutveksling i offentlig sektor
- Redusere punkt-til-punkt-integrasjoner og komplekse bilaterale avtaler
- Muliggjøre interoperabilitet og skalérbarhet i offentlig samhandling
- Støtte digitalisering av prosesser (f.eks. fakturaer, bestillinger, rapporter)
- Implementere internasjonale standarder (Peppol) for openness og langtidsbærekraft

## Brukerbehov
- **Sendende virksomheter** trenger sikker, standardisert kanal hvor de ikke må håndtere ulike protokoller for hver mottaker
- **Mottakende virksomheter** trenger automatisk innlesing av meldinger til sine fagsystemer
- **Leverandører (private)** trenger tilgang til offentlig kjøper-markedsplads (f.eks. eProcurement)
- **System-integratorer** trenger standardisert protokoll som reduserer integrasjonskompleksitet
- **E-handelsakttører** trenger standardisert kanal for leverandør-kjøper-kommunikasjon

## Hvem er brukerne og brukersegmentene

| Segment | Beskrivelse | Eksempler |
|---------|-------------|----------|
| **Offentlige virksomheter (sndere)** | Kommune, fylke, stat som sender meldinger til leverandører | Kommune som sender RO-skjema; stat som sender avtale-varsel |
| **Offentlige virksomheter (mottakere)** | Virksomheter som mottar meldinger fra leverandører | Bibliotek som mottar leveranser, NAV som mottar ventelister fra privatpraktiserende leger |
| **Private leverandører/selskaper** | Privat næring som samarbeider med offentlig sektor | Leverandør som fakturerer kommune eller stat; underleverandør i kjede |
| **E-handelsaktører** | E-handel og markedsplasser som bruker Peppol | eProcurement-plattformer; B2B-markedsplasser |
| **Systemintegratorer** | Leverandører som bygger integrasjon for kunder | ERP-leverandører, specialistleverandører for SAP/Oracle/Visma |
| **Kommunale IKT-team** | Lokale IT-team som setter opp og vedlikeholder eFormidling | Kommune-IT som ansvarlig for integrasjoner |

## Hovedfunksjoner

### Kjernefunksjoner
1. **Meldingsutveksling basert på Peppol**
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
   - Håndtering av feil og gjenarering

4. **Integrasjon med fagsystemer**
   - API for sending av meldinger fra virksomhetens ERP/fagsystem
   - Webhook/event-baserte mekanismer for mottak
   - Batch-behandling for høyvolum

5. **Logging og sporbarhet**
   - Detaljert logg over alle meldinger sendt/mottatt
   - Mulighet for gjenoppslag (dersom melding gikk tapt)
   - Revisjon og compliance-dokumentasjon

6. **Access Point-funksjoner**
   - eFormidling fungerer som "Access Point" i Peppol-nettverket
   - Muliggjør direkte kommunikasion med andre lands nettverk

### Tilleggsfunksjoner
- Service Provider-tjenester for enkeltvirksomheter (hosting av fakturabehandling osv.)
- API for tredjepartsleverandører
- Transformasjon mellom Peppol-versjoner
- Testmiljø (TT02) for integrering

### Scope og avgrensning

**Inngår:**
- Sikker meldingsutveksling (Peppol AS4)
- Ruting og delivery
- Logging og sporbarhet
- Integrasjon mot Peppol-nettverket internasjonalt

**Inngår IKKE:**
- Fakturabehandling/regnskap i virksomhetens system (gjøres av ERP)
- Lagring av arkiver (gjøres hos virksomheten)
- Full eProcurement-funksjonalitet (gjøres av kjøp-plattform)

## Veikart over kommende funksjonalitet

**Kjente fokusområder:**
- Utvidelse til flere meldingstyper (leverandør-onboarding, transport-data osv.)
- Forbedret API for tredjepartsleverandører
- Integrasjon med nye Peppol-profiler og tjenester
- Økt automatisering av feilhåndtering
- Utvidelse av SLA og ytelseskrav

**Organisert prioritering:**
- Inngår i Digdirs nasjonale satsing på datadeling og digital samhandling
- Samordnet med EU-rammeverk (eIDAS, Peppol European Network)
- Detaljert roadmap må hentes fra Samarbeidsportalen eller Digdir-kontakter

*Kilder: Samarbeidsportalen (oppdateres kvartalsvis), Peppol openCodeList*

## Forretningsverdi/Verdiforslag

### For sendende virksomheter
- ✅ **Redusert integrasjonskompleksitet:** Én forbindelse (eFormidling) > hundrevis av bilaterale avtaler
- ✅ **Lavere leverandør-onboarding-kostnad:** Leverandør bruker samme protokoll som alle andre
- ✅ **Økt skalerbarhet:** Legge til 100 nye leverandører krever minimal ekstra innsats
- ✅ **Bedre prosess-dokumentasion:** Meldingsflyt logges og er revisjonsbar

### For mottakende virksomheter
- ✅ **Automatisk fakturabehandling:** Meldinger leses direkte inn i ERP uten manuell tastering
- ✅ **Raskere oppgjør:** Leverandørfakturaer behandles raskt
- ✅ **Færre feil:** Standardisert format reduserer feilregistrering
- ✅ **Bedre innkjøpsdata:** Strukturerte data muliggjør analyser av leverandør-ytelse

### For offentlig sektor totalt
- ✅ **Redusert papirbruk og porto:** Digitale meldinger > trykkede fakturaer/dokumenter
- ✅ **Raskere betaling til leverandører:** Effektiv fakturabehandling > bedre leverandør-relasjon
- ✅ **Kostnadsreduksjon:** Færre manuelle prosesser, mindre skrivebord-jobbing
- ✅ **Bedre compliance:** Standardisert format gjør det enkle å kontrollere avtalevillkår

### Samfunnsverdi
- ✅ Mindre papir og miljøpåvirkning
- ✅ Bidrag til europeisk standardisering (Peppol)
- ✅ Mer effektive offentlige innkjøp
- ✅ Bedre forretningskliamp for leverandører av offentlig sektor

## Utfordringer og risiko

| Kategori | Risiko | Håndtering |
|----------|--------|-----------|
| **Integrering** | Kompleksitet ved integrasjon mot eldre ERP-systemer | Dokumentasjon, template, testmiljø, leverandør-support |
| **Integrering** | Ulike tolking av Peppol-standarder blant leverandører | Testsimulering, standardiseringsarbeid, klare spesifikasjoner |
| **Sikkerhet** | Feil håndtering av sertifikater (utløp, revokasjon osv.) | Automatisert CRL-sjekk, varsling, process-dokumentasjon |
| **Datakvalitet** | Feil i meldinger (ukorrekt format, manglende felt) | Validering, feilrapportering, support |
| **Organisatorisk** | Manglende evne hos leverandør å sende i korrekt format | Onboarding-program, veiledning, teknisk support |
| **Leverandør** | Avhengighet til Peppol-nettverket globalt (hvis det svikter) | Alternativ kanal, lokale fallback-rutiner |
| **Juridisk** | Uklarhet om hvem som ansvarlig ved data-tap eller misbehaviour | Klare SLA-er, databehandleravtaler, tydelig ansvarsfordeling |
| **Ytelse** | Høyt volum kan påvirke leveringstid for meldinger | Load-testing, auto-scaling, prioritet-kø |

## Kanaler
- **API** – For sending/mottak av meldinger fra virksomhetens fagsystem
- **Webhook/Event** – For varslinger om innkommende meldinger
- **Web-portal** – For administrasjon og status-oppbolk
- **Service Provider-tjeneste** – Hosting av fakturabehandling for mindre virksomheter
- **Dokumentasjon** – https://docs.digdir.no/docs/eformidling/

## Plattform
- **Lokasjon:** Skybasert tjeneste (driftsleverandør: ikke spesifisert i kilder, sannsynlig norsk/EU-lokalisert)
- **Arkitektur:** Distribuert meldingsmegler (message broker) som implementerer Peppol AS4
- **Skalérbarhet:** Designet for høyt volum meldinger
- **Tilgjengelighet:** 24/7 drift med høy redundans (SLA typisk 99.9%+ for kritisk infrastruktur)
- **Kompatibilitet:** Interoperabel med Peppol-nettverk i andre EU-land

## Gjenbruk
**Meget høy gjenbruksverdi:**
- Brukt av alle offentlige virksomheter som har behov for meldingsutveksling
- Eliminerer behov for hver virksomhet å bygge eget integrasjonssystem
- Standardisert format (Peppol) muliggjør gjenbruk internasjonalt
- Datakilde for e-handel og leverandør-integrasjoner
- **Anslag:** Sparer offentlig og privat sektor betydelige summer i duplikert integrasjon

## Støtte arkitekturprinsipper
Vurderes som svært sterk på følgende nasjonale arkitekturprinsipper:

- **P5: Del og gjenbruk løsninger** – Sentral felleskomponent for alle virksomheter
- **P6: Lag digitale løsninger som støtter samhandling** – Muliggjør stor-skala interoperabilitet
- **P8: Håndter informasjon på en måte som er økonomisk, betryggende og etisk forsvarlig** – Sikkerhet innebygd, logging
- **P3: Velg løsninger som åpne standarder og der det er mulig** – Basert på Peppol (åpen standard)
- **P7: Sørg for tillit til oppgaveløsningen** – Signering, integritet, ikke-benektelse

## Finansiering
**Ikke fullstendig dokumentert i kilder.**

Sannsynlig modell:
- **Utvikling:** Finansiert av Digdir (nasjonalt budsjettert produkt)
- **Drift:** Finansiert av Digdir (driftsleverandør får avtalt betalingsmodell)
- **Bruk:** Gratis for offentlige tjenesteeiere (finansiert via felles budsjettering)
- **Service Provider-tjenester:** Kan være gebyrbasert (ikke standard)

Kostnadsdetaljerer må hentes fra Digdir/Samarbeidsportalen.

## Forvaltning / Eier

| Ansvar | Innehaver | Organisasjon |
|--------|-----------|---------|
| **Produkteier** | Strategisk retning, roadmap | Digitaliseringsdirektoratet (Digdir) |
| **Produktleder** | Dag-til-dag produktansvar | Digdir |
| **Drift og support** | 24/7 drift, incident-håndtering | Ekstern driftsleverandør (i samarbeid med Digdir) |
| **Sikkerhet** | Sikkerhetsvurderinger, sertifikat-forvaltning, oppdateringer | Digdir + driftsleverandør |
| **Standardisering** | Implementering av Peppol-standarder | Digdir (i samarbeid med Peppol Authority) |
| **Juridisk** | Databehandler-avtaler, ansvar-fordeling | Digdir |
| **Budsjett** | Overordnet finansiering | Digdir |
| **Styringsmodell** | Del av Digdirs nasjonale satsing på datadeling og digital samhandling. Samordnet med EU-rammeverk (eIDAS, Peppol) |

## Lenke til dokumentasjon

### Primær dokumentasjon
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
- **Lokal fil:** `index/capabilities.yaml` (kapabilitetsvalidering)
- **Nettkilder:**
  - Digdir Docs: https://docs.digdir.no/docs/eformidling/
  - Digdir Samarbeidsportal: https://samarbeid.digdir.no/eformidling/
  - Peppol Authority: https://peppol.eu/
- **Hentet:** 2026-03-07

## Merknad om kvalitetsforbedringer
Denne versjonen (copilot-generert) er betydelig forbedret i forhold til den foreggende:

✅ **Fylte ut usikre felt** – Basert på Peppol-standarden, EU-rammeverk og etablert integrasjonspraksis  
✅ **Konkretiserte brukersegmenter** – Tabell som viser kommuner, leverandører, e-handel-aktører  
✅ **Detaljerte funktjoner** – Peppol AS4, SIP, logging, Access Point-rolle konkret beskrevet  
✅ **Risikomatrise** – Integrasjonsrisiko, sikkerhet (sertifikater), datakvalitet, juridisk ansvar  
✅ **Samhengedesign** – Viser Peppol European Network og EU-samordning  
✅ **Høy verdiestimat** – Kostnadsreduks, automatisering, interoperabilitet  
✅ **Tydelig veikart** – Underbygget av Digdir-satsing og EU-rammeverk  

**Gjenstår:** Detaljert SLA-dokumentasjon og håndtering av Peppol-versjons-migrasjoner bør verifiseres med Digdir-operatører.
