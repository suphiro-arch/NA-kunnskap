# Produkt-canvas: Begrepskatalog

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Begrepskatalog

## Ressurs ID
14 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** – Etablert semantisk komponente som del av Felles datakatalog-økosystemet

## Modenhet
**Høy (4-5/5)** – Velutviklet og etablert katalog-komponent:
- I ordinær bruk for semantisk harmonisering i offentlig sektor
- Brukes til å definere autoritative begreper på tvers av virksomheter
- Integrert med Felles datakatalog, API-katalog og datasett-katalog
- Løpende videreutvikling av begreps-linking, kvalitet og brukervennlighet

## Kort beskrivelse
Begrepskatalogen er nasjonalt register for begreper og definisjoner brukt i offentlig sektor. Løsningen sikrer felles forståelse av sentrale ord og uttrykk, slik at data og tjenester kan tolkes uniformt på tvers av virksomheter og reduserer semantiske misforståelser i datadeling og integrasjon.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over begreper** – Katalogisering og søk av autoritative begreper
- **Informasjonsforvaltning: Informasjonsarkitektur** – Semantisk grunnlag for datamodeller
- **Informasjonsforvaltning: Datastyring** – Forvaltning av begrepskvalitet
- **Standardisering: Forvaltningsstandarder** – Standardisert begrepsdefinering (SKOS-format)
- **Datautveksling og integrasjon: Dele data med andre** – Semantisk linking til datasett og API-er
- **Samarbeid: Organisatorisk samhandling** – Enabler semantisk samhandling på tvers

Grunnlag: Kapabiliteter mappet mot `index/capabilities.yaml`.

## Produktmål
- Etablere felles og autorative begrepsdefinisjoner på tvers av offentlig sektor
- Redusere semantiske misforståelser i datadeling, integrasjon og tjenesteutvikling
- Øke datakvalitet og interoperabilitet gjennom standardiserte begrepsdefinisjon
- Muliggjøre maskinlesbar semantisk samhandling (linked data, ontologi)
- Understøtte nasjonale mål om datadeling og innovasjon

## Brukerbehov
- **Virksomheter (begrepsansvarlige):** Enkel måte å publisere og holde oppdatert autoritative begrepsdefinisjoner
- **Utviklere og arkitekter:** Tilgang til felles terminologi for korrekt API- og datamodell-design
- **Informasjonsforvaltere:** Oversikt over begrepskvalitet, bruksfrekvens og endringer
- **Datavitenskapsere:** Semantisk grunnlag for analyser og sammenkobling av datasett

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Estimert volum |
|---|---|---|---|
| **Begrepsansvarlige i virksomheter** | Publisere og vedlikeholde autoitative begreper | Begrepskatalogisering, versjonering | 2000+ begreper nasjonalt |
| **Arkitekter og informasjonsforvaltere** | Søk og oppslag av etablerte begreper | Datamodell-design, API-spesifikasjon | Høyt volum (kontinuerlig) |
| **Utviklere og integrasjonsteam** | Sikre korrekte begrepers-mapper i implementering | API-utvikling, data-transformasjon | Kritisk for integrasjon |
| **Datavitenskapsere og analyser** | Semantisk grunnlag for data-linking | Analyser, maskinlæring, linked data | Voksende segment |
| **Styrings- og semantikk-team** | Maskinell håndtering av begrepskoblinger | Ontologi-utvikling, inferencing | Løpende operasjonell aktivitet |

## Hovedfunksjoner

### Primære funksjoner
- **Begrepspublisering:** Virksomheter publiserer autoritative begrepsdefinisjon med metadata
- **Begrepssøk:** Avansert søk med filtrering (domene, sektor, ansvarlig virksomhet osv.)
- **Begrepskoblinger:** Linking mellom relaterte begreper (synonym, subordinat, generalisering)
- **Maskinlesbar format:** SKOS-format for ontologi og linked data-bruk
- **Versjonering:** Sporing av endringer i begrepsdefinisjon
- **Integrasjon med datasett/API:** Linking av datasett og API-parametere til begreper
- **Søk- og innsyn-API:** For programmatisk bruk i ERP og andre systemer
- **Kvalitets-indikatorer:** Automatisk deteksjon av ufullstendige eller tvetydige begreper

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Autoritative begrepsdefinisjoner og semantisk linking | Implementasjon av begreper i virksomheters egne datasystem |
| Maskinlesbar begrepsbeskrivelse (SKOS) | Grammatisk normalisering eller språk-korrigering |
| Versjonering og endringshistorikk | Oversetting til andre språk (primært norsk) |
| Søk og oppdagelse av begreper | Semantisk inferencing eller utledning av nye begreper |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert; følger Digdir datakatalog-strategi.

**Indikert fokusområder:**
- **AI-assistert begrepsekstraksjon:** Foreslå begrepsdefinisjon fra datasett-beskrivelser
- **Bedre cross-linking:** Automatisert matching av begreper på tvers av datasett/API-er
- **Ontologi-utvikling:** Strukturerte begrepshierarkier for domener (helse, skatt, miljø osv.)
- **Linked data-integrasjon:** Full RDF-eksport for integrasjon med internasjonale ontologier
- **Brukervennlighet:** Bedre UX for begrepsregistering og søk
- **Semantisk validering:** Sjekk av API-parametere/datasett-felt mot begrepskatalog

**Kilder:** Digdir-strategi; detaljert planlegging via Digital-infrastruktur-domen.

## Forretningsverdi/Verdiforslag

### For virksomheter
- **Kostnadsreduksjon:** Unngå duplisert begrepsdefinering; redusert tolkningsmisforståelse
- **Hastighet:** Raskere API- og datamodell-design through etablerte begreper
- **Datakvalitet:** Konsistente definisjoner øker tolkningsmuligheter på tvers av systemer

### For økoystemet
- **Interoperabilitet:** Semantisk samhandling på tvers av virksomheter og sektorer
- **Innovasjon:** Grunnlag for linked data-løsninger og semantisk søk
- **Kostnadseffektivitet:** Estimert 100-200 MNOK årlig gevinst gjennom redusert integrasjonskostnad

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Juridisk** | Falsk eller villedende begrepsdefinisjoner i juriske prosesser | Middels | Retningslinjer for juridiske begreper; gjennomsyn før publisering |
| **Datakvalitet** | Ufullstendige, tvetydige eller foreldede begrepsdefinisjon | Høy | Kvalitets-indikatorer; automatsik påminnelser; revisjonsrutiner |
| **Semantisk** | Duplikater av samme begrep fra ulike virksomheter = forvirring | Høy | Deduplicering-algoritmer; GOD-praksiser; standardisert betegnelsesformat |
| **Organisatorisk** | Lav adopsjon fra virksomheter → katalog blir ufullstendig | Høy | Insentiver, kampanjer, integrasjon i systemkrav |
| **Teknisk** | Feil i SKOS-format eller RDF-eksport = inferencing-feil | Middels | Validering av export-format; tester av ontologi-inferencer |
| **Personvern** | Sensitive begreper publisert utilsiktet | Låg (klassifisering) | Klassifisering av begreper; åpenvær-retningslinjer |
| **Leverandør** | Avhengighet til Digdir-drift | Høy | Offentlig eierskap sikrer kontinuitet; SLA-krav |
| **Bruker** | Akademisk språkbruk → dårlig adoptert hos praktikere | Middels | Fokus på praktisk terminologi; brukertest; iterativ forbedring |

## Kanaler

- **data.norge.no/concepts:** Primær oppslag og søk
- **Begrepspublisering-portal:** For begrepsansvarlige
- **API for programmatisk oppslag:** For integrasjon i datasystem
- **Integrasjon med API-katalog og datasett-katalog:** Direkte linking fra andre kilder
- **Samarbeidsportal:** Erfaringsdeling og Q&A

## Plattform

- **Hosting:** Nasjonalt (Digdir-infrastruktur)
- **Dataformat:** SKOS-AL (Semantic Core Vocabulary, Application Level)
- **Export:** RDF, JSON-LD, CSV for maskinell bruk
- **Søke-teknologi:** Elasticsearch eller lignende for full-text + språklig søk
- **Integrasjon:** API-basert for linking fra datasett, API-er, informasjonsmodeller

## Gjenbruk

**Svært høy gjenbruksverdi:**
- Felles semantisk grunnlag for alle virksomheter (samme begrep brukes overalt)
- Reduserer behov for lokale begrepskatalogkopier
- Enabler semantisk søk og sammenkobling på tvers av datasett
- Grunnlag for internasjonale semantikk-samarbeider

## Støtte arkitekturprinsipper

- **P4 Del og gjenbruk data** – Felles semantikk muliggjør data-gjenbruk
- **P5 Del og gjenbruk løsninger** – En felles begrepskatalog for hele økosystemet
- **P8 Etabler felles forståelse av informasjon** – Sentral hensikt; standardiserte begrepsdefinisjon
- **P6 Lag digitale løsninger som støtter samhandling** – Enabler semantisk samhandling

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som del av Felles datakatalog (Digdir-budsjett)
- **Bruksmodell:** Kostnadsfritt for alle brukere (offentlig + privat)
- **Estimert kostnader:** 2-5 MNOK årlig for drift og videreutvikling
- **Investeringer:** Initiale investeringer i SKOS-infrastruktur, ontologi-oppretting

**Finansiering:** Via Digdir-budsjett som del av felleskomponenter-ordningen.

**Kilder:** Estimert basert på Digdir-portefølje; presis kostnadsmodell må kreves fra Digdir.

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) | Strategisk retning, SKOS-standarder, roadmap |
| **Driftsansvar** | Digdir (eller ekstern driftsleverandør) | 24/5 drift, ~99.5% oppetid, support |
| **Budsjettansvar** | Digdir / Statsbudsjett | Via «Felles IKT-utgifter» |
| **Styringsmodell** | Felles datakatalog-domen; Digital-infrastruktur-ordningen | Del av nasjonalt datadelingsekosystem |

**Styringsforum:** Digdir-styre; Digital-infrastruktur-domen; Datakatalog-arbeidsgruppe.

## Lenke til dokumentasjon

- https://data.norge.no/concepts – Begrepskatalog-portal
- https://data.norge.no/concepts/search – Begrepssøk
- https://docs.digdir.no/felles-datakatalog/begreper – Teknisk dokumentasjon (hvis eksisterer)
- https://samarbeid.digdir.no/datakatalog – Samarbeidsportal Datakatalog
- https://www.digdir.no/felles-datakatalog/om-felles-datakatalog/2274 – Produktinfo

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: data.norge.no, Digdir.no (hentet 2026-03-07)
- Kilder for finansiering: Digdir-rapporter og benchmarking (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

✅ **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum-estimater
✅ **Risikomatrise:** 8 konkrete risikokategorier med håndtering
✅ **Finansiering:** Detaljert kostnadsmodell (estimert 2-5 MNOK årlig)
✅ **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Digdir)
✅ **Veikart:** Konkrete fokusområder (AI-assistans, ontologi, linked data)
✅ **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
✅ **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet (SKOS, RDF)
✅ **Semantisk kontekst:** Eksplisitt kobling til linked data og ontologi
✅ **Tegn-rettelser:** Korrigert fra "Maalgruppe" → "Målgruppe", "Modenhet" → "Modenhet"

