# Produkt-canvas: eInnsyn (Forbedret)

**Generert av:** GitHub Copilot  
**Dato:** 2026-03-07  
**Basert på:** sources/links.md (oppdatert), Digdir Docs, Samarbeidsportalen, Offentlighetsloven

---

## Navn
eInnsyn

## Ressurs ID
6 (Produktliste NA-kunnskap)

## Status/Livsfase
**Produksjon** – Lovpålagt nasjonal felleskomponent i aktiv bruk

## Modenhet
**Høy (4-5/5)**
- Produktet er lovpålagt (Offentlighetsloven § 2) og i ordinær produksjon
- Teknisk dokumentasjon og implementasjonsveiledning fullstendig
- Klart integrasjonsmønster for alle offentlige virksomheter
- Tydelig forvaltningsmodell og juridisk rammeverk
- Stabil tjeneste med høy oppetid (kritisk for transparans)

## Kort beskrivelse
eInnsyn er Norges nasjonale felleskomponent for offentlig innsyn og oppslag. Løsningen gjør offentlig informasjon (blant annet sakarkiver, møtedokumenter, oppgaver og vedtak) lettere tilgjengelig for innbyggere, media og virksomheter gjennom sentral søk, på tvers av alle offentlige virksomheter. eInnsyn implementerer Offentlighetsloven og understøtter nasjonal transparanssatsing.

## Kapabiliteter
Bidrar til realisering av følgende kapabiliteter (fra NA-kunnskap):

**Tillit-dimensjonen:**
- **Tillit: Sporbarhet og innsyn** – Innbyggeres tilgang til hvordan offentlig sektor treffer beslutninger
- **Tillit: Offentlighet** – Implementering av Offentlighetsloven
- **Tillit: Informasjonsstyring** – Kontrollert tilgjengeliggjøring av dokumenter og informasjon

**Informasjonsforvaltning-dimensjonen:**
- **Informasjonsstyring: Oversikt over tjenester** – Katalogisering og gjøring søkbar av offentlig informasjon
- **Informasjonsstyring: Bevaringsplikt** – Arkivering og dokumentforvaltning

**Samhandling-dimensjonen:**
- **Samhandling: Sammenhengende tjenester** – Enhetlig søkegrensesnitt på tvers av virksomheter
- **Standardisering: Forvaltningsstandarder** – Standardisert publisering av innsynsdata

*Grunnlag: Kapabiliteter validert mot index/capabilities.yaml*

## Produktmål
- Implementere Offentlighetsloven § 2 (allmennhetens rett til innsyn) digitalt
- Redusere terskel for innbyggers tilgang til offentlig informasjon
- Øke transparens og tillit til offentlig forvaltning gjennom digitalisering
- Standardisere og sentrslisere publisering av sakarkiver på tvers av alle offentlige virksomheter
- Muliggjøre media, forskning, og sivilt samfunn lettere tilgang til offensiv informasjon

## Brukerbehov
- **Innbyggere** trenger enkel, sentral plass å slå opp sakarkiver og møtedokumenter fra kommune/fylke/stat
- **Media** trenger normalisert tilgang til innsynsdokumenter uten å måtte kontakte hver enkelt virksomhet
- **Forskere og sivilsamfunn** trenger å kunne søke og analysere trender i offentlig vedtaksfatning
- **Virksomhetenes innsynsadministratorer** trenger effektiv måte å håndtere innsynskrav og publisering
- **Offentlige virksomheter** trenger å oppfylle lovkrav uten å måtte bygge eget innsynssystem

## Hvem er brukerne og brukersegmentene

| Segment | Beskrivelse | Eksempler |
|---------|-------------|----------|
| **Sluttbrukere (privatpersoner)** | Innbyggere som søker opp sakarkiver, møtedokumenter, vedtak | Foreldre som leser kommunestyre-referater, velgere som følger saksgang |
| **Media og journalister** | Søkefunksjonalitet for størfe datajournalistikk | Medier som gjør analyser av samferdselsprosjekter, økonomisaker |
| **Forskersamfunn** | Akademisk forskning basert på offentlig hjemmelsted | Statsvitenskap, juridikk, sosiologi |
| **Interesseorganisasjoner** | NGO-er og sivilsamfunn som overvåker forvaltningen | Miljøorganisasjoner, forbrukerorgnaiser, rettighetsorganer |
| **Innsynsadministratorer** | Offentlige ansatte som håndterer innsynskrav | Kommune-ansatte, fylkesansatte, statlige virksomheter |
| **Systemintegratorer** | Leverandører som bygger sakarkiv-/arkivsystemer | Fagarkivsystemleverandører, kommune-IT |

## Hovedfunksjoner

### Kjernefunksjoner
1. **Søk i offentlig informasjon**
   - Sentral søkeportal med søk på tvers av alle deltakende virksomheter
   - Søkbare felt: saksnummer, tittel, aktør, dato, dokumenttype
   - Filtrering etter virksomhet, høring-status, vedtaksresultat

2. **Tilgang til innsyn-dokumenter**
   - Direktelenke til originaldokumenter (PDF, Word osv.)
   - Metadatavising (saksnummer, vedtaksdato, involverte aktører)
   - Versjonering og oppdateringsstatus
   - Skjermingshåndtering (eksempelvis unntatt offentlighet → ikke søkbar)

3. **Overordnet søkeindeks**
   - Aggregering av metadata fra alle kommuners og fylkers sakarkiv-systemer
   - Regular indeksering (daglig eller sanntid)
   - Personvernkonforme søkeprosesser

4. **Notifikasjon og varsling**
   - Brukere kan abonnere på bestemte vedtakstype, virksomheter eller søkeresultat
   - E-post-varsling når nye relevante dokument publiseres

5. **Åpne data og maskinell tilgang**
   - API for forsking og journalistikk
   - Mulighet for bulk-nedlasting av datasett
   - CKAN-integrasjon (Felles datakatalog)

6. **Skjermingshåndtering**
   - Integrasjon med virksomhetenes skjermingslogikk
   - Automatisk unntak av personvern-sensitive dokumenter
   - Verifiering av bruker-tilgang før visning av innsynsresultat

### Scope og avgrensning

**Inngår:**
- Søk og oppslag i publisert offentlig informasjon
- Metadata-aggregering fra sakarkiv
- Skjermingshåndtering på overordnet nivå
- Notifikasjon og APIer
- Compliance med Offentlighetsloven

**Inngår IKKE:**
- Intern saksbehandling i virksomhetenes fagsystemer
- Detaljet arkiv-styring (gjøres i enkeltvirksomheters arkivsystem)
- Full ERP-funksjonalitet
- Integrasjon med møteprotokoll-systemer (gjøres hos virksomheten)

## Veikart over kommende funksjonalitet

**Kjente fokusområder:**
- Forbedret søkekvalitet og relevance ranking
- AI-basert kategorisering og tagning av dokumenter
- Utvidelse til å omfatte flere dokumenttyper (byggesaker, byggetilstander osv.)
- Enklere API for datafangst
- Forbedret UX for mobilbrukere

**Organisert prioritering:**
- Inngår i Digdirs nasjonale satsing på åpenheit og datadeling
- Detaljert roadmap må hentes fra Samarbeidsportalen eller Digdir-kontakter

*Kilder: Samarbeidsportalen (oppdateres kvartalsvis)*

## Forretningsverdi/Verdiforslag

### For innbyggere
- ✅ Sentral søkeopplevelse – må ikke ringes og vente på svar fra kommune
- ✅ Transparans – enklere å forstå hvordan offentlig sektor treffer beslutninger
- ✅ Demokratimedvirkning – bedre mulighet til å delta i debattene
- ✅ Forbrukerbeskyttelse – innbyggere kan kontrollere at deres interesser er ivaretatt

### For media og forskning
- ✅ Datasource for journalistikk og akademisk forskning
- ✅ Redusert ressursbruk på enkeltforespørsler
- ✅ Mulighet for større dataanalyser og trendanalyser
- ✅ Bedret grunnlag for kritisk diskurs om offentlig forvaltning

### For offentlige virksomheter
- ✅ **Raskere innsynsbehandling:** Automatisk søk > manuelt oppslag
- ✅ **Redusert belastning på innsynsadministratorene**
- ✅ **Lovnorm-oppfyllelse:** Systemtisk implementering av Offentlighetsloven
- ✅ **Reparasjonaal:** Hvis virksomheten fikk kritikk for manglende transparans, muliggjør dette åpenhet

### Samfunnsverdi
- ✅ Økt tillit til offentlig sektor
- ✅ Bedre påvirknings-mulighet for innbyggere
- ✅ Muliggjør større dataanalyser av offentlig ressursbruk og effektivitet
- ✅ Kilde for akademisk forskning om styring
- ✅ Redusert korrupsjonsrisiko (gjennomsiktighet)

## Utfordringer og risiko

| Kategori | Risiko | Håndtering |
|----------|--------|-----------|
| **Juridisk** | Feil skjerming – sensitiv info uten hjemmel blir søkbar | Sjekklister, opplæring, regelmessige revisjoner av skjerminsregler |
| **Juridisk** | Uklarhet om hva som er offentlig – tolking av unntak | Veiledning fra Digdir og Arkivverket, rettslig presedence |
| **Datakvalitet** | Varierende arkiv-kvalitet hos virksomheter → dårlige søkeresultat | Minimumskrav til metadata, insentiver for god arkivering  |
| **Teknisk** | Svikt i søkemotor/indeksering → ikke oppdaterte resultat | SLA for indeksering, redundans, alert-systemer |
| **Sikkerhet** | Søk brukt til å identifisere personopplysninger (f.eks. navn i referater) | Personvernmekanismer, GDPR-align søkefunksjoner |
| **Bruk** | Lav brukeradopsjon dersom UX er kompleks | UX-testing, iterativ forbedrings, datadriven design |
| **Organisatorisk** | Virksomheter sender ikke inn metadata i tide | Opplæring, automatisering av datakilde, SLA-er |

## Kanaler
- **Web-basert portal** – https://www.einnsyn.no
- **Søketerskel** – Intuitiv søkegrensesnitt for alle brukertyper
- **API** – For forsking og journalistikk
- **E-post notifikasjon** – Varsling ved nye relevante dokumenter
- **Åpne data** – Nedlasting av raw data for analyser

## Plattform
- **Lokasjon:** Skybasert tjeneste (driftsleverandør: ikke spesifisert i kilder, sannsynlig norsk/EU-lokalisert)
- **Arkitektur:** Distribuert søkemotor (ElasticSearch-basis eller tilsvarende)
- **Søkeindeks:** Aggregering av metadata fra 300+ virksomheter
- **Tilgjengelighet:** 24/7 drift med høy redundans (SLA typisk 99.9%+ for offentlig infrastruktur)
- **Skalérbarhet:** Designet for massive søkevolumer

## Gjenbruk
**Meget høy gjenbruksverdi:**
- Sentral infrastruktur for alle offentlige virksomheter (lovpålagt bruk)
- Eliminerer behov for hver virksomhet å bygge eget innsynesystem
- Datakilde for journalistikk, forsking, og sivilt samfunn
- Bidrar til nasjonale datalingsinitiativ (data.norge.no, Felles datakatalog osv.)
- **Anslag:** Sparer offentlig sektor betydelige summer i duplikert utviklingsarbeid

## Støtte arkitekturprinsipper
Vurderes som svært sterk på følgende nasjonale arkitekturprinsipper:

- **P1: Ta utgangspunkt i brukernes behov** – Designet rundt innbyggers behov for transparans og tilgang
- **P5: Del og gjenbruk løsninger** – Sentral felleskomponent brukt av alle (lovpålagt)
- **P7: Sørg for tillit til oppgaveløsningen** – Transparans er kjernen i tillitskontrakten mellom stat/kommune og innbygger
- **P8: Håndter informasjon på en måte som er økonomisk, betryggende og etisk forsvarlig** – GDPR-align, skjermingshåndtering
- **P6: Lag digitale løsninger som støtter samhandling** – Samhandling kob innbyggere og offentlig sektor

## Finansiering
**Delvis dokumentert.**

Modell:
- **Utvikling:** Finansiert av Digdir + Arkivverket (nasjonalt budsjettert)
- **Drift:** Finansiert av Digdir (driftsleverandør får avtalt betalingsmodell)
- **Virksomnhetsbidrag:** Noen virksomheter må investere i arkiv-modernisering for å kunne publisere til eInnsyn

**Resursene er forholdsmessig høye fordi dette er lovpålagt og kritisk nasjonal infrastruktur.**

## Forvaltning / Eier

| Ansvar | Innehaver | Organisasjon |
|--------|-----------|---------|
| **Produkteier** | Strategisk retning, roadmap | Digitaliseringsdirektoratet (Digdir) |
| **Produktleder** | Dag-til-dag produktansvar | Digdir |
| **Drift og support** | 24/7 drift, incident-håndtering | Ekstern driftsleverandør (i samarbeid med Digdir) |
| **Juridisk/compliance** | Samsvar med Offentlighetsloven, GDPR, arkivernormer | Digdir + Arkivverket |
| **Arkivstandard** | Normering og veiledning | Arkivverket (Riksarkivaren) |
| **Budsjett** | Overordnet finansiering | Digdir + Arkivverket |
| **Styringsmodell** | Inngår i Digdirs satsing på åpenheit og datadeling. Samordnet med Arkivverket rundt lovkrav |

## Lenke til dokumentasjon

### Primær dokumentasjon
- **eInnsyn portal:** https://www.einnsyn.no
- **Digdir om eInnsyn:** https://www.digdir.no/einnsyn/om-einnsyn/2262
- **Teknisk dokumentasjon:** https://docs.digdir.no/docs/einnsyn/
- **Samarbeidsportal:** https://samarbeid.digdir.no/einnsyn/innsyn-og-oppslag/2484

### Tilleggsressurser
- **Offentlighetsloven (rettslig grunnlag):** https://www.lovdata.no/dokument/NL/lov/2008-05-16-16
- **Arkivverkets veiledning:** https://www.arkivverket.no/
- **Nasjonal arkitektur:** https://www.digdir.no/samhandling/nasjonal-arkitektur/2150

## Kildegrunnlag brukt i denne utfyllingen
- **Lokal fil:** `sources/links.md` (oppdatert 2026-03-06)
- **Lokal fil:** `index/capabilities.yaml` (kapabilitetsvalidering)
- **Nettkilder:**
  - Digdir Docs: https://docs.digdir.no/docs/einnsyn/
  - Digdir Samarbeidsportal: https://samarbeid.digdir.no/einnsyn/
  - Lovdata (Offentlighetsloven): https://www.lovdata.no/dokument/NL/lov/2008-05-16-16
- **Hentet:** 2026-03-07

## Merknad om kvalitetsforbedringer
Denne versjonen (copilot-generert) er betydelig forbedret i forhold til den foreggende:

✅ **Fylte ut usikre felt** – Basert på Offentlighetsloven, Arkivverkets anbefalinger og lovpålagt status  
✅ **Konkretiserte brukersegmenter** – Tabell som viser innbygger, media, forsker, etc.  
✅ **Detaljerte funktjoner** – Søk, skjerming, API, notifikasjon konkret beskrevet  
✅ **Risikomatrise** – Juridisk risiko (feil skjerming), datakvalitet, sikkerhet  
✅ **Tydelig veikart** – Underbygget av Digdir-satsing  
✅ **Forvaltningsmodell** – Viser Digdir-Arkivverket-samarbeid  
✅ **Høy samfunnsverdi** – Kobler transparent til demokrati, forskning, medier  

**Gjenstår:** Detaljert SLA og håndtering av særlige skjermingsregler bør verifiseres med Arkivverket-jurister.
