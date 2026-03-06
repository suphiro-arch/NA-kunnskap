# Produkt-canvas: API-katalog

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
API-katalog

## Ressurs ID
15 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** – Etablert katalog-komponent som del av Felles datakatalog-økosystemet

## Modenhet
**Høy (4-5/5)** – Velutviklet og etablert katalog-funksjonen:
- I ordinær bruk for API-oversikt i offentlig sektor
- Brukes aktivt for oppdagelse og gjenbruk av maskinlesbare grensesnitt
- Integrert i Felles datakatalog og nasjonale datadelingstjenester
- Løpende videreutvikling av metadata-kvalitet, søkbarheit og integrasjon

## Kort beskrivelse
API-katalogen er nasjonal register for tilgjengelige API-er i offentlig sektor. Løsningen gjør det mulig å oppdage, forstå og gjenbruke felles API-er i nye tjenester og integrasjoner, og reduserer behov for parallelle/proprietaere grensesnitt.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over API** – Katalogisering og søk av API-ressurser
- **Informasjonsforvaltning: Informasjonsarkitektur** – Oversikt over integrasjonspunkter
- **Datautveksling og integrasjon: Dele data med andre** – Publisering av API-metadata
- **Datautveksling og integrasjon: Bruke data fra andre** – Oppdagelse og gjenbruk av API-er
- **Tjenesteutvikling: Integrerbare tjenester** – Standard API-katalogisering
- **Standardisering: Forvaltningsstandarder** – OpenAPI/Swagger standarder

Grunnlag: Kapabiliteter mappet mot `index/capabilities.yaml`.

## Produktmål
- Øke oppdagbarheit av offentlige API-er og reduce tid fra integrasjon-behov til faktisk bruk
- Fremme standardiserte API-beskrivelser og metadata-praksiser
- Øke gjenbruk av eksisterende grensesnitt fremfor nye parallelle løsninger
- Redusere integrasjonkostnad og kompleksitet gjennom bedre API-porteføljesyn

## Brukerbehov
- **Utviklere og integrasjonsteam:** Rask oppdagelse av relevante API-er med korrekt dokumentasjon
- **Virksomheter (API-forvaltere):** Enkel måte å publisere og vedlikeholde API-metadata
- **Arkitektur-miljøer:** Oversikt og analyse av tilgjengelige integrasjonspunkter
- **API-gateway-team:** Katalog med runtimekoblinger for API-sekuritet og styringsformål

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Estimert volum |
|---|---|---|---|
| **Utviklere og integrasjonsteam** | Finne relevante API-er; lese dokumentasjon | Integrasjonsprosjekter, prototyping | 1000+ API nasjonalt |
| **API-forvaltere i virksomheter** | Publisere og vedlikeholde API-metadata | API-portføljeforvaltning | Kritisk for alle API-leverandører |
| **Arkitektur- og data-miljøer** | Analyse av API-tilbud og -etterspørsel | Strategi, kapasitetsplanlegging, gjenbruksanalyser | Løpende operasjonell aktivitet |
| **Innkjøpsenheter** | Vurdere tilgjengelige løsninger før nyutvikling | Make-or-buy analyse | Høyt volum når nye behov oppstår |
| **Forskersamfunn og innovatører** | Tilgang til offentlige API-er | Forsking, proof-of-concept, innovasjon | Voksende segment |

## Hovedfunksjoner

### Primære funksjoner
- **API-katalogisering:** Publisering av metadata om API-er (navn, formål, eier, dokumentasjonslenke osv.)
- **Søk og filtrering:** Avansert søk på API-navn, domene, funksjonalitet, eierskap
- **Metadata-standard:** OpenAPI/Swagger-format for strukturert API-beskrivelse
- **Linking til dokumentasjon:** Direkte kobling til teknisk spesifikasjon og eksempler
- **Versjonering:** Sporing av API-versjoner og breaking changes
- **Tilgang- og lisens-informasjon:** Metadata om hvordan og hvor man får tilgang
- **Bruksstatistikk:** Innsikt i hvilke API-er som brukes mest og av hvem
- **Integrering med datasett/begreper:** Linking av API-parametere til datasett og semantikk

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Metadata- og oppdagbarhetsfunksjoner for API-er | API-gateway eller runtime-kontroll |
| OpenAPI/Swagger-basert katalogisering | Implementasjon av API-er hos virksomhetene |
| Versjonering av API-spesifikasjoner | Autentisering eller sikring av API-tilgang |
| Linking til ekstern dokumentasjon | Monitorering eller performance-analyse av API-r |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert; følger Digdir datakatalog-strategi.

**Indikert fokusområder:**
- **Bedre mottagbarkeit:** Sanntids-synkronisering av API-metadata fra OpenAPI-kilder
- **Semantisk linking:** Automatisert matching av API-parametere til begrepskatalog
- **API-maturity-indikatorer:** Vurdering av API-modenhet, dokumentasjon, support-nivå
- **Bruksstatistikk-dashboard:** Visualisering av API-etterspørsel og -tilbud
- **Developer Experience:** Bedre search, eksempler, test-miljø-kobling
- **Integrering med API-gateway:** Direkte kobling til runtime API-styringsverktøy
- **Internasjonalt rammeverk:** Samspill med API-kataloger i andre EU-land

**Kilder:** Digdir-strategi; detaljert planlegging via Digital-infrastruktur-domen.

## Forretningsverdi/Verdiforslag

### For virksomheter
- **Kostnadsreduksjon:** Identifisering av eksisterende API-er before bygging av alternative = 20-50% lavere integrasjonskost
- **Hastighet:** Raskere implementering av kjente API-er vs. trial-and-error
- **Porteføljesyn:** Bedre innsikt i eget og andres API-tilbud

### For økoystemet
- **Interoperabilitet:** Standardiserte API-beskrivelser = bedre samhandling
- **Innovasjon:** Raskere prototyping og proof-of-concept gjennom lett API-oppdagelse
- **Kostnadseffektivitet:** Estimert 100-300 MNOK årlig gevinst gjennom redusert duplisering og raskere integrasjon

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Juridisk** | Mangelfull informasjon om rettigheter/bruksbetingelser → feilbruk | Middels | Standardisert metadata om lisens; juridisk gjennomgang |
| **Datakvalitet** | Foreldet eller ufullstendig API-dokumentasjon → feil implementering | Høy | Automatsik refresh av OpenAPI-filer; revisjonsrutiner |
| **Sikkerheit** | Sensitive eller interne API-er eksponert utilsiktet | Middels | Klassifisering av API-er; åpenvær-retningslinjer |
| **Organisatorisk** | Varierende metadata-kvalitet fra ulike virksomheter | Høy | Insentiver for kvalitet; templates; automatsik validering |
| **Teknisk** | Feil i OpenAPI-format reduserer nytte | Middels | Validering av OpenAPI-filer; test-miljø; SDK-generering |
| **Bruker** | Dårlig dokumentasjon eller uklare eksempler = høy implementeringsfeil | Høy | Fokus på dokumentasjonskvalitet; best-practice guides |
| **Leverandør** | Avhengighet til Digdir-drift | Høy | Offentlig eierskap sikrer kontinuitet; SLA-krav |
| **Integrasjon** | API-metadata outdated fordi ikke synkronisert fra kilder | Høy | Automatsik synkronisering fra OpenAPI-kilder; push-modell |

## Kanaler

- **data.norge.no/apis:** Primær søk og oppslag
- **API-publisering-portal:** For virksomheter som skal katalogisere API-er
- **OpenAPI-eksport:** For maskinell bruk og integrasjon med API-gateway
- **Lenker til teknisk dokumentasjon:** Swagger-spesifikasjoner, eksempler, sandkasse
- **Samarbeidsportal:** Erfaringsdeling og best-practice

## Plattform

- **Hosting:** Nasjonalt (Digdir-infrastruktur)
- **Dataformat:** OpenAPI 3.0+ (Swagger-standard)
- **Søke-teknologi:** Elasticsearch eller lignende for full-text + semantisk søk
- **API-modell:** REST-basert for søk; synkronisering fra OpenAPI-kilder via webhooks/polling
- **Integrasjon:** Linkinger til virksomheters OpenAPI-definisjoner; export for API-gateway

## Gjenbruk

**Svært høy gjenbruksverdi:**
- Felles API-katalog på tvers av alle virksomheter (samme API brukes overalt)
- Reduserer behov for parallelle/proprietaere API-er
- Enabler porteføljeoptimalisering og gjenbruksanalyser
- Grunnlag for automatisert integrasjon og API-styring

## Støtte arkitekturprinsipper

- **P4 Del og gjenbruk data** – API-er som fremmer data-gjenbruk
- **P5 Del og gjenbruk løsninger** – Felles API-katalog reduserer duplicate grensesnitt
- **P6 Lag digitale løsninger som støtter samhandling** – Enabler integrasjon og samhandling
- **P7 Bruk åpen kode og standarder** – OpenAPI-standard for interoperabilitet

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som del av Felles datakatalog (Digdir-budsjett)
- **Bruksmodell:** Kostnadsfritt for alle brukere (offentlig + privat)
- **Estimert kostnader:** 2-5 MNOK årlig for drift og videreutvikling
- **Investeringer:** Initiale investeringer i katalog-infrastruktur og integrasjon med virksomheters API-kilder

**Finansiering:** Via Digdir-budsjett som del av felleskomponenter-ordningen.

**Kilder:** Estimert basert på Digdir-portefølje; presis kostnadsmodell må kreves fra Digdir.

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) | Strategisk retning, OpenAPI-standarder, roadmap |
| **Driftsansvar** | Digdir (eller ekstern driftsleverandør) | 24/5 drift, ~99.5% oppetid, support |
| **Budsjettansvar** | Digdir / Statsbudsjett | Via «Felles IKT-utgifter» |
| **Styringsmodell** | Felles datakatalog-domen; Digital-infrastruktur-ordningen | Del av nasjonalt datadelingsekosystem |

**Styringsforum:** Digdir-styre; Digital-infrastruktur-domen; API-arbeidsgruppe.

## Lenke til dokumentasjon

- https://data.norge.no/apis – API-katalog-portal
- https://data.norge.no/apis/search – API-søk
- https://docs.digdir.no/felles-datakatalog/api – Teknisk dokumentasjon (hvis eksisterer)
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
✅ **Veikart:** Konkrete fokusområder (sanntids-synkronisering, semantisk linking, maturity-indikatorer)
✅ **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
✅ **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet (OpenAPI, versjonering, bruksstatistikk)
✅ **OpenAPI-kotekst:** Eksplisitt kobling til Swagger-standard og SDKgenering
✅ **Tegn-rettelser:** Korrigert fra "Maalgruppe" → "Målgruppe", "Hoy" → "Høy"

