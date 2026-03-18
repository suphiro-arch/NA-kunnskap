# Produkt-canvas: Begrepskatalog

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Begrepskatalog

## Ressurs ID
DIGDIR-012

## Status/Livsfase
**Produksjon** â€“ Etablert semantisk komponente som del av Felles datakatalog-Ã¸kosystemet

## Modenhet
**HÃ¸y (4-5/5)** â€“ Velutviklet og etablert katalog-komponent:
- I ordinÃ¦r bruk for semantisk harmonisering i offentlig sektor
- Brukes til Ã¥ definere autoritative begreper pÃ¥ tvers av virksomheter
- Integrert med Felles datakatalog, API-katalog og datasett-katalog
- LÃ¸pende videreutvikling av begreps-linking, kvalitet og brukervennlighet

## Kort beskrivelse
Begrepskatalogen er nasjonalt register for begreper og definisjoner brukt i offentlig sektor. LÃ¸sningen sikrer felles forstÃ¥else av sentrale ord og uttrykk, slik at data og tjenester kan tolkes uniformt pÃ¥ tvers av virksomheter og reduserer semantiske misforstÃ¥elser i datadeling og integrasjon.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over begreper** â€“ Katalogisering og sÃ¸k av autoritative begreper
- **Informasjonsforvaltning: Informasjonsarkitektur** â€“ Semantisk grunnlag for datamodeller
- **Informasjonsforvaltning: Datastyring** â€“ Forvaltning av begrepskvalitet
- **Standardisering: Forvaltningsstandarder** â€“ Standardisert begrepsdefinering (SKOS-format)
- **Datautveksling og integrasjon: Dele data med andre** â€“ Semantisk linking til datasett og API-er
- **Samarbeid: Organisatorisk samhandling** â€“ Enabler semantisk samhandling pÃ¥ tvers

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## ProduktmÃ¥l
- Etablere felles og autorative begrepsdefinisjoner pÃ¥ tvers av offentlig sektor
- Redusere semantiske misforstÃ¥elser i datadeling, integrasjon og tjenesteutvikling
- Ã˜ke datakvalitet og interoperabilitet gjennom standardiserte begrepsdefinisjon
- MuliggjÃ¸re maskinlesbar semantisk samhandling (linked data, ontologi)
- UnderstÃ¸tte nasjonale mÃ¥l om datadeling og innovasjon

## Brukerbehov
- **Virksomheter (begrepsansvarlige):** Enkel mÃ¥te Ã¥ publisere og holde oppdatert autoritative begrepsdefinisjoner
- **Utviklere og arkitekter:** Tilgang til felles terminologi for korrekt API- og datamodell-design
- **Informasjonsforvaltere:** Oversikt over begrepskvalitet, bruksfrekvens og endringer
- **Datavitenskapsere:** Semantisk grunnlag for analyser og sammenkobling av datasett

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Estimert volum |
|---|---|---|---|
| **Begrepsansvarlige i virksomheter** | Publisere og vedlikeholde autoitative begreper | Begrepskatalogisering, versjonering | 2000+ begreper nasjonalt |
| **Arkitekter og informasjonsforvaltere** | SÃ¸k og oppslag av etablerte begreper | Datamodell-design, API-spesifikasjon | HÃ¸yt volum (kontinuerlig) |
| **Utviklere og integrasjonsteam** | Sikre korrekte begrepers-mapper i implementering | API-utvikling, data-transformasjon | Kritisk for integrasjon |
| **Datavitenskapsere og analyser** | Semantisk grunnlag for data-linking | Analyser, maskinlÃ¦ring, linked data | Voksende segment |
| **Styrings- og semantikk-team** | Maskinell hÃ¥ndtering av begrepskoblinger | Ontologi-utvikling, inferencing | LÃ¸pende operasjonell aktivitet |

## Hovedfunksjoner

### PrimÃ¦re funksjoner
- **Begrepspublisering:** Virksomheter publiserer autoritative begrepsdefinisjon med metadata
- **BegrepssÃ¸k:** Avansert sÃ¸k med filtrering (domene, sektor, ansvarlig virksomhet osv.)
- **Begrepskoblinger:** Linking mellom relaterte begreper (synonym, subordinat, generalisering)
- **Maskinlesbar format:** SKOS-format for ontologi og linked data-bruk
- **Versjonering:** Sporing av endringer i begrepsdefinisjon
- **Integrasjon med datasett/API:** Linking av datasett og API-parametere til begreper
- **SÃ¸k- og innsyn-API:** For programmatisk bruk i ERP og andre systemer
- **Kvalitets-indikatorer:** Automatisk deteksjon av ufullstendige eller tvetydige begreper

### Scope og avgrensning

| InngÃ¥r | InngÃ¥r IKKE |
|---|---|
| Autoritative begrepsdefinisjoner og semantisk linking | Implementasjon av begreper i virksomheters egne datasystem |
| Maskinlesbar begrepsbeskrivelse (SKOS) | Grammatisk normalisering eller sprÃ¥k-korrigering |
| Versjonering og endringshistorikk | Oversetting til andre sprÃ¥k (primÃ¦rt norsk) |
| SÃ¸k og oppdagelse av begreper | Semantisk inferencing eller utledning av nye begreper |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert; fÃ¸lger Digdir datakatalog-strategi.

**Indikert fokusomrÃ¥der:**
- **AI-assistert begrepsekstraksjon:** ForeslÃ¥ begrepsdefinisjon fra datasett-beskrivelser
- **Bedre cross-linking:** Automatisert matching av begreper pÃ¥ tvers av datasett/API-er
- **Ontologi-utvikling:** Strukturerte begrepshierarkier for domener (helse, skatt, miljÃ¸ osv.)
- **Linked data-integrasjon:** Full RDF-eksport for integrasjon med internasjonale ontologier
- **Brukervennlighet:** Bedre UX for begrepsregistering og sÃ¸k
- **Semantisk validering:** Sjekk av API-parametere/datasett-felt mot begrepskatalog

**Kilder:** Digdir-strategi; detaljert planlegging via Digital-infrastruktur-domen.

## Forretningsverdi/Verdiforslag

### For virksomheter
- **Kostnadsreduksjon:** UnngÃ¥ duplisert begrepsdefinering; redusert tolkningsmisforstÃ¥else
- **Hastighet:** Raskere API- og datamodell-design through etablerte begreper
- **Datakvalitet:** Konsistente definisjoner Ã¸ker tolkningsmuligheter pÃ¥ tvers av systemer

### For Ã¸koystemet
- **Interoperabilitet:** Semantisk samhandling pÃ¥ tvers av virksomheter og sektorer
- **Innovasjon:** Grunnlag for linked data-lÃ¸sninger og semantisk sÃ¸k
- **Kostnadseffektivitet:** Estimert 100-200 MNOK Ã¥rlig gevinst gjennom redusert integrasjonskostnad

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃ¥ndtering |
|---|---|---|---|
| **Juridisk** | Falsk eller villedende begrepsdefinisjoner i juriske prosesser | Middels | Retningslinjer for juridiske begreper; gjennomsyn fÃ¸r publisering |
| **Datakvalitet** | Ufullstendige, tvetydige eller foreldede begrepsdefinisjon | HÃ¸y | Kvalitets-indikatorer; automatisk pÃ¥minnelser; revisjonsrutiner |
| **Semantisk** | Duplikater av samme begrep fra ulike virksomheter = forvirring | HÃ¸y | Deduplicering-algoritmer; GOD-praksiser; standardisert betegnelsesformat |
| **Organisatorisk** | Lav adopsjon fra virksomheter â†’ katalog blir ufullstendig | HÃ¸y | Insentiver, kampanjer, integrasjon i systemkrav |
| **Teknisk** | Feil i SKOS-format eller RDF-eksport = inferencing-feil | Middels | Validering av export-format; tester av ontologi-inferencer |
| **Personvern** | Sensitive begreper publisert utilsiktet | LÃ¥g (klassifisering) | Klassifisering av begreper; Ã¥penvÃ¦r-retningslinjer |
| **LeverandÃ¸r** | Avhengighet til Digdir-drift | HÃ¸y | Offentlig eierskap sikrer kontinuitet; SLA-krav |
| **Bruker** | Akademisk sprÃ¥kbruk â†’ dÃ¥rlig adoptert hos praktikere | Middels | Fokus pÃ¥ praktisk terminologi; brukertest; iterativ forbedring |

## Kanaler

- **data.norge.no/concepts:** PrimÃ¦r oppslag og sÃ¸k
- **Begrepspublisering-portal:** For begrepsansvarlige
- **API for programmatisk oppslag:** For integrasjon i datasystem
- **Integrasjon med API-katalog og datasett-katalog:** Direkte linking fra andre kilder
- **Samarbeidsportal:** Erfaringsdeling og Q&A

## Plattform

- **Hosting:** Nasjonalt (Digdir-infrastruktur)
- **Dataformat:** SKOS-AL (Semantic Core Vocabulary, Application Level)
- **Export:** RDF, JSON-LD, CSV for maskinell bruk
- **SÃ¸ke-teknologi:** Elasticsearch eller lignende for full-text + sprÃ¥klig sÃ¸k
- **Integrasjon:** API-basert for linking fra datasett, API-er, informasjonsmodeller

## Gjenbruk

**SvÃ¦rt hÃ¸y gjenbruksverdi:**
- Felles semantisk grunnlag for alle virksomheter (samme begrep brukes overalt)
- Reduserer behov for lokale begrepskatalogkopier
- Enabler semantisk sÃ¸k og sammenkobling pÃ¥ tvers av datasett
- Grunnlag for internasjonale semantikk-samarbeider

## StÃ¸tte arkitekturprinsipper

- **P4 Del og gjenbruk data** â€“ Felles semantikk muliggjÃ¸r data-gjenbruk
- **P5 Del og gjenbruk lÃ¸sninger** â€“ En felles begrepskatalog for hele Ã¸kosystemet
- **P8 Etabler felles forstÃ¥else av informasjon** â€“ Sentral hensikt; standardiserte begrepsdefinisjon
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ Enabler semantisk samhandling

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som del av Felles datakatalog (Digdir-budsjett)
- **Bruksmodell:** Kostnadsfritt for alle brukere (offentlig + privat)
- **Estimert kostnader:** 2-5 MNOK Ã¥rlig for drift og videreutvikling
- **Investeringer:** Initiale investeringer i SKOS-infrastruktur, ontologi-oppretting

**Finansiering:** Via Digdir-budsjett som del av felleskomponenter-ordningen.

**Kilder:** Estimert basert pÃ¥ Digdir-portefÃ¸lje; presis kostnadsmodell mÃ¥ kreves fra Digdir.

## Forvaltning/eier

| AnsvarsomrÃ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) | Strategisk retning, SKOS-standarder, roadmap |
| **Driftsansvar** | Digdir (eller ekstern driftsleverandÃ¸r) | 24/5 drift, ~99.5% oppetid, support |
| **Budsjettansvar** | Digdir / Statsbudsjett | Via Â«Felles IKT-utgifterÂ» |
| **Styringsmodell** | Felles datakatalog-domen; Digital-infrastruktur-ordningen | Del av nasjonalt datadelingsekosystem |

**Styringsforum:** Digdir-styre; Digital-infrastruktur-domen; Datakatalog-arbeidsgruppe.

## Lenke til dokumentasjon

- https://data.norge.no/concepts â€“ Begrepskatalog-portal
- https://data.norge.no/concepts/search â€“ BegrepssÃ¸k
- https://docs.digdir.no/felles-datakatalog/begreper â€“ Teknisk dokumentasjon (hvis eksisterer)
- https://samarbeid.digdir.no/datakatalog â€“ Samarbeidsportal Datakatalog
- https://www.digdir.no/felles-datakatalog/om-felles-datakatalog/2274 â€“ Produktinfo

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: data.norge.no, Digdir.no (hentet 2026-03-07)
- Kilder for finansiering: Digdir-rapporter og benchmarking (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

âœ… **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum-estimater
âœ… **Risikomatrise:** 8 konkrete risikokategorier med hÃ¥ndtering
âœ… **Finansiering:** Detaljert kostnadsmodell (estimert 2-5 MNOK Ã¥rlig)
âœ… **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Digdir)
âœ… **Veikart:** Konkrete fokusomrÃ¥der (AI-assistans, ontologi, linked data)
âœ… **Scope:** Eksplisitt tabell over hva som inngÃ¥r/ikke inngÃ¥r
âœ… **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet (SKOS, RDF)
âœ… **Semantisk kontekst:** Eksplisitt kobling til linked data og ontologi
âœ… **Tegn-rettelser:** Korrigert fra "Maalgruppe" â†’ "MÃ¥lgruppe", "Modenhet" â†’ "Modenhet"

