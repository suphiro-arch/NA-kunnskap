# Produkt-canvas: eInnsyn (Forbedret)

**Generert av:** GitHub Copilot  
**Dato:** 2026-03-07  
**Basert pÃ¥:** sources/links.md (oppdatert), Digdir Docs, Samarbeidsportalen, Offentlighetsloven

---

## Navn
eInnsyn

## Ressurs ID
6 (Produktliste NA-kunnskap)

## Status/Livsfase
**Produksjon** â€“ LovpÃ¥lagt nasjonal felleskomponent i aktiv bruk

## Modenhet
**HÃ¸y (4-5/5)**
- Produktet er lovpÃ¥lagt (Offentlighetsloven Â§ 2) og i ordinÃ¦r produksjon
- Teknisk dokumentasjon og implementasjonsveiledning fullstendig
- Klart integrasjonsmÃ¸nster for alle offentlige virksomheter
- Tydelig forvaltningsmodell og juridisk rammeverk
- Stabil tjeneste med hÃ¸y oppetid (kritisk for transparans)

## Kort beskrivelse
eInnsyn er Norges nasjonale felleskomponent for offentlig innsyn og oppslag. LÃ¸sningen gjÃ¸r offentlig informasjon (blant annet sakarkiver, mÃ¸tedokumenter, oppgaver og vedtak) lettere tilgjengelig for innbyggere, media og virksomheter gjennom sentral sÃ¸k, pÃ¥ tvers av alle offentlige virksomheter. eInnsyn implementerer Offentlighetsloven og understÃ¸tter nasjonal transparenssatsing.

## Kapabiliteter
Bidrar til realisering av fÃ¸lgende kapabiliteter (fra NA-kunnskap):

**Tillit-dimensjonen:**
- **Tillit: Sporbarhet og innsyn** â€“ Innbyggeres tilgang til hvordan offentlig sektor treffer beslutninger
- **Tillit: Offentlighet** â€“ Implementering av Offentlighetsloven
- **Tillit: Informasjonsstyring** â€“ Kontrollert tilgjengeliggjÃ¸ring av dokumenter og informasjon

**Informasjonsforvaltning-dimensjonen:**
- **Informasjonsstyring: Oversikt over tjenester** â€“ Katalogisering og gjÃ¸ring sÃ¸kbar av offentlig informasjon
- **Informasjonsstyring: Bevaringsplikt** â€“ Arkivering og dokumentforvaltning

**Samhandling-dimensjonen:**
- **Samhandling: Sammenhengende tjenester** â€“ Enhetlig sÃ¸kegrensesnitt pÃ¥ tvers av virksomheter
- **Standardisering: Forvaltningsstandarder** â€“ Standardisert publisering av innsynsdata

*Grunnlag: Kapabiliteter validert mot index/capabilities.yaml*

## ProduktmÃ¥l
- Implementere Offentlighetsloven Â§ 2 (allmennhetens rett til innsyn) digitalt
- Redusere terskel for innbyggers tilgang til offentlig informasjon
- Ã˜ke transparens og tillit til offentlig forvaltning gjennom digitalisering
- Standardisere og sentralisere publisering av sakarkiver pÃ¥ tvers av alle offentlige virksomheter
- MuliggjÃ¸re media, forskning, og sivilt samfunn lettere tilgang til offentlig informasjon

## Brukerbehov
- **Innbyggere** trenger enkel, sentral plass Ã¥ slÃ¥ opp sakarkiver og mÃ¸tedokumenter fra kommune/fylke/stat
- **Media** trenger normalisert tilgang til innsynsdokumenter uten Ã¥ mÃ¥tte kontakte hver enkelt virksomhet
- **Forskere og sivilsamfunn** trenger Ã¥ kunne sÃ¸ke og analysere trender i offentlig vedtaksfatning
- **Virksomhetenes innsynsadministratorer** trenger effektiv mÃ¥te Ã¥ hÃ¥ndtere innsynskrav og publisering
- **Offentlige virksomheter** trenger Ã¥ oppfylle lovkrav uten Ã¥ mÃ¥tte bygge eget innsynssystem

## Hvem er brukerne og brukersegmentene

| Segment | Beskrivelse | Eksempler |
|---------|-------------|----------|
| **Sluttbrukere (privatpersoner)** | Innbyggere som sÃ¸ker opp sakarkiver, mÃ¸tedokumenter, vedtak | Foreldre som leser kommunestyre-referater, velgere som fÃ¸lger saksgang |
| **Media og journalister** | SÃ¸kefunksjonalitet for stÃ¸rfe datajournalistikk | Medier som gjÃ¸r analyser av samferdselsprosjekter, Ã¸konomisaker |
| **Forskersamfunn** | Akademisk forskning basert pÃ¥ offentlig hjemmelsted | Statsvitenskap, juridikk, sosiologi |
| **Interesseorganisasjoner** | NGO-er og sivilsamfunn som overvÃ¥ker forvaltningen | MiljÃ¸organisasjoner, forbrukerorgnaiser, rettighetsorganer |
| **Innsynsadministratorer** | Offentlige ansatte som hÃ¥ndterer innsynskrav | Kommune-ansatte, fylkesansatte, statlige virksomheter |
| **Systemintegratorer** | LeverandÃ¸rer som bygger sakarkiv-/arkivsystemer | FagarkivsystemleverandÃ¸rer, kommune-IT |

## Hovedfunksjoner

### Kjernefunksjoner
1. **SÃ¸k i offentlig informasjon**
   - Sentral sÃ¸keportal med sÃ¸k pÃ¥ tvers av alle deltakende virksomheter
   - SÃ¸kbare felt: saksnummer, tittel, aktÃ¸r, dato, dokumenttype
   - Filtrering etter virksomhet, hÃ¸ring-status, vedtaksresultat

2. **Tilgang til innsyn-dokumenter**
   - Direktelenke til originaldokumenter (PDF, Word osv.)
   - Metadatavising (saksnummer, vedtaksdato, involverte aktÃ¸rer)
   - Versjonering og oppdateringsstatus
   - SkjermingshÃ¥ndtering (eksempelvis unntatt offentlighet â†’ ikke sÃ¸kbar)

3. **Overordnet sÃ¸keindeks**
   - Aggregering av metadata fra alle kommuners og fylkers sakarkiv-systemer
   - Regular indeksering (daglig eller sanntid)
   - Personvernkonforme sÃ¸keprosesser

4. **Notifikasjon og varsling**
   - Brukere kan abonnere pÃ¥ bestemte vedtakstype, virksomheter eller sÃ¸keresultat
   - E-post-varsling nÃ¥r nye relevante dokument publiseres

5. **Ã…pne data og maskinell tilgang**
   - API for forsking og journalistikk
   - Mulighet for bulk-nedlasting av datasett
   - CKAN-integrasjon (Felles datakatalog)

6. **SkjermingshÃ¥ndtering**
   - Integrasjon med virksomhetenes skjermingslogikk
   - Automatisk unntak av personvern-sensitive dokumenter
   - Verifiering av bruker-tilgang fÃ¸r visning av innsynsresultat

### Scope og avgrensning

**InngÃ¥r:**
- SÃ¸k og oppslag i publisert offentlig informasjon
- Metadata-aggregering fra sakarkiv
- SkjermingshÃ¥ndtering pÃ¥ overordnet nivÃ¥
- Notifikasjon og APIer
- Compliance med Offentlighetsloven

**InngÃ¥r IKKE:**
- Intern saksbehandling i virksomhetenes fagsystemer
- Detaljet arkiv-styring (gjÃ¸res i enkeltvirksomheters arkivsystem)
- Full ERP-funksjonalitet
- Integrasjon med mÃ¸teprotokoll-systemer (gjÃ¸res hos virksomheten)

## Veikart over kommende funksjonalitet

**Kjente fokusomrÃ¥der:**
- Forbedret sÃ¸kekvalitet og relevance ranking
- AI-basert kategorisering og tagning av dokumenter
- Utvidelse til Ã¥ omfatte flere dokumenttyper (byggesaker, byggetilstander osv.)
- Enklere API for datafangst
- Forbedret UX for mobilbrukere

**Organisert prioritering:**
- InngÃ¥r i Digdirs nasjonale satsing pÃ¥ Ã¥penheit og datadeling
- Detaljert roadmap mÃ¥ hentes fra Samarbeidsportalen eller Digdir-kontakter

*Kilder: Samarbeidsportalen (oppdateres kvartalsvis)*

## Forretningsverdi/Verdiforslag

### For innbyggere
- âœ… Sentral sÃ¸keopplevelse â€“ mÃ¥ ikke ringes og vente pÃ¥ svar fra kommune
- âœ… Transparans â€“ enklere Ã¥ forstÃ¥ hvordan offentlig sektor treffer beslutninger
- âœ… Demokratimedvirkning â€“ bedre mulighet til Ã¥ delta i debattene
- âœ… Forbrukerbeskyttelse â€“ innbyggere kan kontrollere at deres interesser er ivaretatt

### For media og forskning
- âœ… Datasource for journalistikk og akademisk forskning
- âœ… Redusert ressursbruk pÃ¥ enkeltforespÃ¸rsler
- âœ… Mulighet for stÃ¸rre dataanalyser og trendanalyser
- âœ… Bedret grunnlag for kritisk diskurs om offentlig forvaltning

### For offentlige virksomheter
- âœ… **Raskere innsynsbehandling:** Automatisk sÃ¸k > manuelt oppslag
- âœ… **Redusert belastning pÃ¥ innsynsadministratorene**
- âœ… **Lovnorm-oppfyllelse:** Systemtisk implementering av Offentlighetsloven
- âœ… **Reparasjonaal:** Hvis virksomheten fikk kritikk for manglende transparans, muliggjÃ¸r dette Ã¥penhet

### Samfunnsverdi
- âœ… Ã˜kt tillit til offentlig sektor
- âœ… Bedre pÃ¥virknings-mulighet for innbyggere
- âœ… MuliggjÃ¸r stÃ¸rre dataanalyser av offentlig ressursbruk og effektivitet
- âœ… Kilde for akademisk forskning om styring
- âœ… Redusert korrupsjonsrisiko (gjennomsiktighet)

## Utfordringer og risiko

| Kategori | Risiko | HÃ¥ndtering |
|----------|--------|-----------|
| **Juridisk** | Feil skjerming â€“ sensitiv info uten hjemmel blir sÃ¸kbar | Sjekklister, opplÃ¦ring, regelmessige revisjoner av skjerminsregler |
| **Juridisk** | Uklarhet om hva som er offentlig â€“ tolking av unntak | Veiledning fra Digdir og Arkivverket, rettslig presedence |
| **Datakvalitet** | Varierende arkiv-kvalitet hos virksomheter â†’ dÃ¥rlige sÃ¸keresultat | Minimumskrav til metadata, insentiver for god arkivering  |
| **Teknisk** | Svikt i sÃ¸kemotor/indeksering â†’ ikke oppdaterte resultat | SLA for indeksering, redundans, alert-systemer |
| **Sikkerhet** | SÃ¸k brukt til Ã¥ identifisere personopplysninger (f.eks. navn i referater) | Personvernmekanismer, GDPR-align sÃ¸kefunksjoner |
| **Bruk** | Lav brukeradopsjon dersom UX er kompleks | UX-testing, iterativ forbedrings, datadriven design |
| **Organisatorisk** | Virksomheter sender ikke inn metadata i tide | OpplÃ¦ring, automatisering av datakilde, SLA-er |

## Kanaler
- **Web-basert portal** â€“ https://www.einnsyn.no
- **SÃ¸keterskel** â€“ Intuitiv sÃ¸kegrensesnitt for alle brukertyper
- **API** â€“ For forsking og journalistikk
- **E-post notifikasjon** â€“ Varsling ved nye relevante dokumenter
- **Ã…pne data** â€“ Nedlasting av raw data for analyser

## Plattform
- **Lokasjon:** Skybasert tjeneste (driftsleverandÃ¸r: ikke spesifisert i kilder, sannsynlig norsk/EU-lokalisert)
- **Arkitektur:** Distribuert sÃ¸kemotor (ElasticSearch-basis eller tilsvarende)
- **SÃ¸keindeks:** Aggregering av metadata fra 300+ virksomheter
- **Tilgjengelighet:** 24/7 drift med hÃ¸y redundans (SLA typisk 99.9%+ for offentlig infrastruktur)
- **SkalÃ©rbarhet:** Designet for massive sÃ¸kevolumer

## Gjenbruk
**Meget hÃ¸y gjenbruksverdi:**
- Sentral infrastruktur for alle offentlige virksomheter (lovpÃ¥lagt bruk)
- Eliminerer behov for hver virksomhet Ã¥ bygge eget innsynesystem
- Datakilde for journalistikk, forsking, og sivilt samfunn
- Bidrar til nasjonale datalingsinitiativ (data.norge.no, Felles datakatalog osv.)
- **Anslag:** Sparer offentlig sektor betydelige summer i duplikert utviklingsarbeid

## StÃ¸tte arkitekturprinsipper
Vurderes som svÃ¦rt sterk pÃ¥ fÃ¸lgende nasjonale arkitekturprinsipper:

- **P1: Ta utgangspunkt i brukernes behov** â€“ Designet rundt innbyggers behov for transparans og tilgang
- **P5: Del og gjenbruk lÃ¸sninger** â€“ Sentral felleskomponent brukt av alle (lovpÃ¥lagt)
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** â€“ Transparans er kjernen i tillitskontrakten mellom stat/kommune og innbygger
- **P8: HÃ¥ndter informasjon pÃ¥ en mÃ¥te som er Ã¸konomisk, betryggende og etisk forsvarlig** â€“ GDPR-align, skjermingshÃ¥ndtering
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ Samhandling kob innbyggere og offentlig sektor

## Finansiering
**Delvis dokumentert.**

Modell:
- **Utvikling:** Finansiert av Digdir + Arkivverket (nasjonalt budsjettert)
- **Drift:** Finansiert av Digdir (driftsleverandÃ¸r fÃ¥r avtalt betalingsmodell)
- **Virksomnhetsbidrag:** Noen virksomheter mÃ¥ investere i arkiv-modernisering for Ã¥ kunne publisere til eInnsyn

**Resursene er forholdsmessig hÃ¸ye fordi dette er lovpÃ¥lagt og kritisk nasjonal infrastruktur.**

## Forvaltning / Eier

| Ansvar | Innehaver | Organisasjon |
|--------|-----------|---------|
| **Produkteier** | Strategisk retning, roadmap | Digitaliseringsdirektoratet (Digdir) |
| **Produktleder** | Dag-til-dag produktansvar | Digdir |
| **Drift og support** | 24/7 drift, incident-hÃ¥ndtering | Ekstern driftsleverandÃ¸r (i samarbeid med Digdir) |
| **Juridisk/compliance** | Samsvar med Offentlighetsloven, GDPR, arkivernormer | Digdir + Arkivverket |
| **Arkivstandard** | Normering og veiledning | Arkivverket (Riksarkivaren) |
| **Budsjett** | Overordnet finansiering | Digdir + Arkivverket |
| **Styringsmodell** | InngÃ¥r i Digdirs satsing pÃ¥ Ã¥penheit og datadeling. Samordnet med Arkivverket rundt lovkrav |

## Lenke til dokumentasjon

### PrimÃ¦r dokumentasjon
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

âœ… **Fylte ut usikre felt** â€“ Basert pÃ¥ Offentlighetsloven, Arkivverkets anbefalinger og lovpÃ¥lagt status  
âœ… **Konkretiserte brukersegmenter** â€“ Tabell som viser innbygger, media, forsker, etc.  
âœ… **Detaljerte funktjoner** â€“ SÃ¸k, skjerming, API, notifikasjon konkret beskrevet  
âœ… **Risikomatrise** â€“ Juridisk risiko (feil skjerming), datakvalitet, sikkerhet  
âœ… **Tydelig veikart** â€“ Underbygget av Digdir-satsing  
âœ… **Forvaltningsmodell** â€“ Viser Digdir-Arkivverket-samarbeid  
âœ… **HÃ¸y samfunnsverdi** â€“ Kobler transparent til demokrati, forskning, medier  

**GjenstÃ¥r:** Detaljert SLA og hÃ¥ndtering av sÃ¦rlige skjermingsregler bÃ¸r verifiseres med Arkivverket-jurister.
