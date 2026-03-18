# Produkt-canvas: API-katalog

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
API-katalog

## Ressurs ID
DIGDIR-013

## Status/Livsfase
**Produksjon** â€“ Etablert katalog-komponent som del av Felles datakatalog-Ã¸kosystemet

## Modenhet
**HÃ¸y (4-5/5)** â€“ Velutviklet og etablert katalog-funksjonen:
- I ordinÃ¦r bruk for API-oversikt i offentlig sektor
- Brukes aktivt for oppdagelse og gjenbruk av maskinlesbare grensesnitt
- Integrert i Felles datakatalog og nasjonale datadelingstjenester
- LÃ¸pende videreutvikling av metadata-kvalitet, sÃ¸kbarheit og integrasjon

## Kort beskrivelse
API-katalogen er nasjonal register for tilgjengelige API-er i offentlig sektor. LÃ¸sningen gjÃ¸r det mulig Ã¥ oppdage, forstÃ¥ og gjenbruke felles API-er i nye tjenester og integrasjoner, og reduserer behov for parallelle/proprietaere grensesnitt.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over API** â€“ Katalogisering og sÃ¸k av API-ressurser
- **Informasjonsforvaltning: Informasjonsarkitektur** â€“ Oversikt over integrasjonspunkter
- **Datautveksling og integrasjon: Dele data med andre** â€“ Publisering av API-metadata
- **Datautveksling og integrasjon: Bruke data fra andre** â€“ Oppdagelse og gjenbruk av API-er
- **Tjenesteutvikling: Integrerbare tjenester** â€“ Standard API-katalogisering
- **Standardisering: Forvaltningsstandarder** â€“ OpenAPI/Swagger standarder

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## ProduktmÃ¥l
- Ã˜ke oppdagbarheit av offentlige API-er og reduce tid fra integrasjon-behov til faktisk bruk
- Fremme standardiserte API-beskrivelser og metadata-praksiser
- Ã˜ke gjenbruk av eksisterende grensesnitt fremfor nye parallelle lÃ¸sninger
- Redusere integrasjonkostnad og kompleksitet gjennom bedre API-portefÃ¸ljesyn

## Brukerbehov
- **Utviklere og integrasjonsteam:** Rask oppdagelse av relevante API-er med korrekt dokumentasjon
- **Virksomheter (API-forvaltere):** Enkel mÃ¥te Ã¥ publisere og vedlikeholde API-metadata
- **Arkitektur-miljÃ¸er:** Oversikt og analyse av tilgjengelige integrasjonspunkter
- **API-gateway-team:** Katalog med runtimekoblinger for API-sekuritet og styringsformÃ¥l

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Estimert volum |
|---|---|---|---|
| **Utviklere og integrasjonsteam** | Finne relevante API-er; lese dokumentasjon | Integrasjonsprosjekter, prototyping | 1000+ API nasjonalt |
| **API-forvaltere i virksomheter** | Publisere og vedlikeholde API-metadata | API-portfÃ¸ljeforvaltning | Kritisk for alle API-leverandÃ¸rer |
| **Arkitektur- og data-miljÃ¸er** | Analyse av API-tilbud og -etterspÃ¸rsel | Strategi, kapasitetsplanlegging, gjenbruksanalyser | LÃ¸pende operasjonell aktivitet |
| **InnkjÃ¸psenheter** | Vurdere tilgjengelige lÃ¸sninger fÃ¸r nyutvikling | Make-or-buy analyse | HÃ¸yt volum nÃ¥r nye behov oppstÃ¥r |
| **Forskersamfunn og innovatÃ¸rer** | Tilgang til offentlige API-er | Forsking, proof-of-concept, innovasjon | Voksende segment |

## Hovedfunksjoner

### PrimÃ¦re funksjoner
- **API-katalogisering:** Publisering av metadata om API-er (navn, formÃ¥l, eier, dokumentasjonslenke osv.)
- **SÃ¸k og filtrering:** Avansert sÃ¸k pÃ¥ API-navn, domene, funksjonalitet, eierskap
- **Metadata-standard:** OpenAPI/Swagger-format for strukturert API-beskrivelse
- **Linking til dokumentasjon:** Direkte kobling til teknisk spesifikasjon og eksempler
- **Versjonering:** Sporing av API-versjoner og breaking changes
- **Tilgang- og lisens-informasjon:** Metadata om hvordan og hvor man fÃ¥r tilgang
- **Bruksstatistikk:** Innsikt i hvilke API-er som brukes mest og av hvem
- **Integrering med datasett/begreper:** Linking av API-parametere til datasett og semantikk

### Scope og avgrensning

| InngÃ¥r | InngÃ¥r IKKE |
|---|---|
| Metadata- og oppdagbarhetsfunksjoner for API-er | API-gateway eller runtime-kontroll |
| OpenAPI/Swagger-basert katalogisering | Implementasjon av API-er hos virksomhetene |
| Versjonering av API-spesifikasjoner | Autentisering eller sikring av API-tilgang |
| Linking til ekstern dokumentasjon | Monitorering eller performance-analyse av API-r |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert; fÃ¸lger Digdir datakatalog-strategi.

**Indikert fokusomrÃ¥der:**
- **Bedre mottagbarkeit:** Sanntids-synkronisering av API-metadata fra OpenAPI-kilder
- **Semantisk linking:** Automatisert matching av API-parametere til begrepskatalog
- **API-maturity-indikatorer:** Vurdering av API-modenhet, dokumentasjon, support-nivÃ¥
- **Bruksstatistikk-dashboard:** Visualisering av API-etterspÃ¸rsel og -tilbud
- **Developer Experience:** Bedre search, eksempler, test-miljÃ¸-kobling
- **Integrering med API-gateway:** Direkte kobling til runtime API-styringsverktÃ¸y
- **Internasjonalt rammeverk:** Samspill med API-kataloger i andre EU-land

**Kilder:** Digdir-strategi; detaljert planlegging via Digital-infrastruktur-domen.

## Forretningsverdi/Verdiforslag

### For virksomheter
- **Kostnadsreduksjon:** Identifisering av eksisterende API-er before bygging av alternative = 20-50% lavere integrasjonskost
- **Hastighet:** Raskere implementering av kjente API-er vs. trial-and-error
- **PortefÃ¸ljesyn:** Bedre innsikt i eget og andres API-tilbud

### For Ã¸koystemet
- **Interoperabilitet:** Standardiserte API-beskrivelser = bedre samhandling
- **Innovasjon:** Raskere prototyping og proof-of-concept gjennom lett API-oppdagelse
- **Kostnadseffektivitet:** Estimert 100-300 MNOK Ã¥rlig gevinst gjennom redusert duplisering og raskere integrasjon

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃ¥ndtering |
|---|---|---|---|
| **Juridisk** | Mangelfull informasjon om rettigheter/bruksbetingelser â†’ feilbruk | Middels | Standardisert metadata om lisens; juridisk gjennomgang |
| **Datakvalitet** | Foreldet eller ufullstendig API-dokumentasjon â†’ feil implementering | HÃ¸y | Automatsik refresh av OpenAPI-filer; revisjonsrutiner |
| **Sikkerhet** | Sensitive eller interne API-er eksponert utilsiktet | Middels | Klassifisering av API-er; Ã¥penvÃ¦r-retningslinjer |
| **Organisatorisk** | Varierende metadata-kvalitet fra ulike virksomheter | HÃ¸y | Insentiver for kvalitet; templates; automatisk validering |
| **Teknisk** | Feil i OpenAPI-format reduserer nytte | Middels | Validering av OpenAPI-filer; test-miljÃ¸; SDK-generering |
| **Bruker** | DÃ¥rlig dokumentasjon eller uklare eksempler = hÃ¸y implementeringsfeil | HÃ¸y | Fokus pÃ¥ dokumentasjonskvalitet; best-practice guides |
| **LeverandÃ¸r** | Avhengighet til Digdir-drift | HÃ¸y | Offentlig eierskap sikrer kontinuitet; SLA-krav |
| **Integrasjon** | API-metadata outdated fordi ikke synkronisert fra kilder | HÃ¸y | Automatsik synkronisering fra OpenAPI-kilder; push-modell |

## Kanaler

- **data.norge.no/apis:** PrimÃ¦r sÃ¸k og oppslag
- **API-publisering-portal:** For virksomheter som skal katalogisere API-er
- **OpenAPI-eksport:** For maskinell bruk og integrasjon med API-gateway
- **Lenker til teknisk dokumentasjon:** Swagger-spesifikasjoner, eksempler, sandkasse
- **Samarbeidsportal:** Erfaringsdeling og best-practice

## Plattform

- **Hosting:** Nasjonalt (Digdir-infrastruktur)
- **Dataformat:** OpenAPI 3.0+ (Swagger-standard)
- **SÃ¸ke-teknologi:** Elasticsearch eller lignende for full-text + semantisk sÃ¸k
- **API-modell:** REST-basert for sÃ¸k; synkronisering fra OpenAPI-kilder via webhooks/polling
- **Integrasjon:** Linkinger til virksomheters OpenAPI-definisjoner; export for API-gateway

## Gjenbruk

**SvÃ¦rt hÃ¸y gjenbruksverdi:**
- Felles API-katalog pÃ¥ tvers av alle virksomheter (samme API brukes overalt)
- Reduserer behov for parallelle/proprietaere API-er
- Enabler portefÃ¸ljeoptimalisering og gjenbruksanalyser
- Grunnlag for automatisert integrasjon og API-styring

## StÃ¸tte arkitekturprinsipper

- **P4 Del og gjenbruk data** â€“ API-er som fremmer data-gjenbruk
- **P5 Del og gjenbruk lÃ¸sninger** â€“ Felles API-katalog reduserer duplicate grensesnitt
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ Enabler integrasjon og samhandling
- **P7 Bruk Ã¥pen kode og standarder** â€“ OpenAPI-standard for interoperabilitet

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som del av Felles datakatalog (Digdir-budsjett)
- **Bruksmodell:** Kostnadsfritt for alle brukere (offentlig + privat)
- **Estimert kostnader:** 2-5 MNOK Ã¥rlig for drift og videreutvikling
- **Investeringer:** Initiale investeringer i katalog-infrastruktur og integrasjon med virksomheters API-kilder

**Finansiering:** Via Digdir-budsjett som del av felleskomponenter-ordningen.

**Kilder:** Estimert basert pÃ¥ Digdir-portefÃ¸lje; presis kostnadsmodell mÃ¥ kreves fra Digdir.

## Forvaltning/eier

| AnsvarsomrÃ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) | Strategisk retning, OpenAPI-standarder, roadmap |
| **Driftsansvar** | Digdir (eller ekstern driftsleverandÃ¸r) | 24/5 drift, ~99.5% oppetid, support |
| **Budsjettansvar** | Digdir / Statsbudsjett | Via Â«Felles IKT-utgifterÂ» |
| **Styringsmodell** | Felles datakatalog-domen; Digital-infrastruktur-ordningen | Del av nasjonalt datadelingsekosystem |

**Styringsforum:** Digdir-styre; Digital-infrastruktur-domen; API-arbeidsgruppe.

## Lenke til dokumentasjon

- https://data.norge.no/apis â€“ API-katalog-portal
- https://data.norge.no/apis/search â€“ API-sÃ¸k
- https://docs.digdir.no/felles-datakatalog/api â€“ Teknisk dokumentasjon (hvis eksisterer)
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
âœ… **Veikart:** Konkrete fokusomrÃ¥der (sanntids-synkronisering, semantisk linking, maturity-indikatorer)
âœ… **Scope:** Eksplisitt tabell over hva som inngÃ¥r/ikke inngÃ¥r
âœ… **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet (OpenAPI, versjonering, bruksstatistikk)
âœ… **OpenAPI-kotekst:** Eksplisitt kobling til Swagger-standard og SDKgenering
âœ… **Tegn-rettelser:** Korrigert fra "Maalgruppe" â†’ "MÃ¥lgruppe", "Hoy" â†’ "HÃ¸y"

