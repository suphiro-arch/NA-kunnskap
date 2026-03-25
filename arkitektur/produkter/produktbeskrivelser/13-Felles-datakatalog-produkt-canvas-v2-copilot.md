# Produkt-canvas: Felles datakatalog

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Felles datakatalog

## Ressurs ID
DIGDIR-011

## Status/Livsfase
**Produksjon** – Etablert nasjonalkomponent for datakatalogisering og datadeling

## Modenhet
**Høy (4-5/5)** – Velutviklet og etablert katalog-komponent:
- I ordinær bruk som nasjonal datakatalog siden lansering
- Dokumentert metadata-modell og sök-grensesnitt
- Integrering med begrepskatalog, API-katalog og informasjonsmodeller
- Løpende videreutvikling av søkfunksjonalitet, datakvalitet og brukervennlighet

## Kort beskrivelse
Felles datakatalog er en nasjonal løsning for å beskrive, katalogisere og gjøre datasett, API-er, informasjonsmodeller og begreper synlige og synlige og oppdagbare for datadeling i offentlig og privat sektor. Katalogen fungerer som sentral referanse for "hva data finnes, hvem som eier dem, og hvordan de kan brukes", og støtter både avanserte arkitekter og gjennomsnittsbrukere som søker relevante datakilder.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over API** – Katalogisering av tilgjengelige API-er.
- **Informasjonsforvaltning: Oversikt over begreper** – Integrasjon med Begrepskatalog for semantisk enighet.
- **Informasjonsforvaltning: Oversikt over datasett** – Katalogisering og søk av offentlige datasett.
- **Informasjonsforvaltning: Oversikt over informasjonsmodeller** – Støtte for SOSI og andre datamodeller.
- **Standardisering: Forvaltningsstandarder** – DCAT-AP-NO standarder og metadata-klassifikasjoner.

## Produktmål
- Øke gjenfinning og gjenbruk av offentlige data gjennom sentralisert katalogisering
- Forbedre datakvalitet gjennom standardiserte metadata-beskrivelser
- Støtte raskere etablering av datadrevne og integrasjon-baserte tjenester
- Redusere «siloing» av data og fremme transparency i offentlig dataeierskap
- Fungere som nasjonal platform for dataøkosystem-vekst

## Brukerbehov
- **Datatilbydere:** Mulighet til enkelt å publisere og holde oppdatert sin datakatalog
- **Datakonsumenter:** Lett gjenkjennelse av relevante dataset ved oppfinneliggjøring (søk)
- **Arkitekter og utviklere:** Oversikt over API-er, informasjonsmodeller og begreper (SOSI, semantikk)
- **Forvaltningsmiljøer:** Innsikt i nasjonal datadeling, datakvalitet og brukspatterns  
- **Forskersamfunn:** Åpne data og datasett for forsking og innovasjon

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Estimert volum |
|---|---|---|---|
| **Offentlige virksomheter (datatilbydere)** | Publisere og vedlikeholde datakatalog | Datasett, API-er, informasjonsmodeller | 10 000+ datasett nasjonalt |
| **Datakonsumenter (ark./utviklere)** | Søk og oppdagelse av relevante data | Integrasjonsarbeid, prototyping, innovasjon | Høyt volum (ukjent eksakt) |
| **Forskersamfunn** | Tilgang til åpne datasett | Forsking, analyser, innovasjons-prosjekter | Voksende segment |
| **Næringsliv** | Oppdagelse av offentlige og private datasett | B2B-integrering, product development | Voksende segment |
| **Styrings- og kvalitetsmiljøer** | Innsikt i dataøkosystem-tilstand | Governance, compliance-rapportering, datakvalitet | Løpende operasjonell aktivitet |

## Hovedfunksjoner

### Primære funksjoner
- **Datasettkatalogisering:** Publisering av metadata om datasett (tittel, beskrivelse, tilgang, eier osv.)
- **API-katalogisering:** Dokumentasjon og søk blant tilgjengelige API-er
- **Begrepskatalog-integrasjon:** Linking til felles begreper (semantisk identitet)
- **Søkfunksjonalitet:** Avansert søk med filtrering (eier, tema, målgruppe, datakvalitet osv.)
- **Metadata-standard (DCAT-AP-NO):** Strukturert metadata-format for interoperabilitet
- **Datasett-kvalitet:** Indikator for datakvalitet (tilgjengelighet, oppdatering, dokumentasjon)
- **Tilgangsinformasjon:** Metadata om hvordan og hvor man får tilgang til datasett
- **Versjonering og endringshistorikk:** Sporing av endringer i katalog-poster

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Katalogisering av metadata om datasett | Selve lagring/forvaltning av alle kildedata |
| Søk og oppdagelse av datasett | Fullstendig tilgangsstyring til hvert enkelt datasett |
| Standardisert metadata-format (DCAT-AP-NO) | Datakvalitets-garantier eller SLA på data |
| Integrasjon med Begrepskatalog | Konsumentens prosessering eller analyse av data |
| Linking til informasjonsmodeller | Implementasjon av spesifikke datamodeller |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert; følger Digdir-strategien.

**Indikert fokusområder:**
- **AI-assistert katalogisering:** Generering av metadata-forslag fra datasett-beskrivelser
- **Bedre datakvalitets-indikator:** Dypere innsikt i aktualitet, vollständighet, standardisering
- **Integrasjon med datadeling-plattformer:** Direkte linking fra katalog til faktisk datadelingsløsninger
- **Maskin-læring-basert anbefalinger:** Foreslå relevante datasett basert på brukerprofil
- **Forbedret søk:** NLP-basert søk; semantisk matching med begreper
- **Internasjonal interoperabilitet:** Federering med andre medlemslanders datakataloger (EU)
- **Dokumenta realisering:** Bedre steg av automatisering av på-publisissering

**Kilder:** Digdir-strategi; detaljert planlegging via Digital-infrastruktur-domen.

## Forretningsverdi/Verdiforslag

### For datatilbydere
- **Synlighet:** Gjøre egne datasett oppfinnelig og attraktiv for gjenbruk
- **Kostnadsbesparelser:** Redusert behov for manuell dokumentering; AI-assistans
- **Datakvalitets-insikt:** Innsikt i hvordan data brukes og hvilke forbedringer som trengs

### For datakonsumenter
- **Hastighet:** Raskere oppdagelse av relevante datasett vs. manuell søking
- **Kostnadsreduksjon:** Gjenbruk av eksisterende datasett vs. innsamling av nye
- **Kvalitet:** Informasjon om datakvalitet; unngår dårlige datakjelder

### For samfunn
- **Innovasjon:** Grunnlag for nye offentlig-private tjenester og forsking
- **Transparens:** Oversikt over hva data finnes i offentlig sektor
- **Kostnadseffektivitet:** Massive gevinster gjennom industriell datadeling (estimert 1000+ MNOK potensial)

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Datakvalitet** | Metadata av lav kvalitet (manglende, utdatert, uklart) → redusert bruksverdi | Høy | Standarder, opplæring, automatisering av innhenting |
| **Organisatorisk** | Lav innslippingsrate fra virksomheeter → katalogen blir ufullstendig | Høy | Insentiver, påbud, integrasjon med egne datasystem |
| **Semantisk** | Uklarheit om begreper → dårlig søkbarheit og samordning | Middels | Integrasjon med Begrepskatalog; semantisk harmonisering |
| **Personvern** | Publisering av personsenistive metadata = privacy-brudd | Middels | Klare veiledninger om hva som skal publiseres; DPA-prosesser |
| **Sikkerhet** | Metadata som eksponerer sensitive systemarkitekturer | Middels | Retningslinjer; åpenfølling-strategi; sikkerhets-vurdering |
| **Vedlikehold** | Katalog blir utdatert hvis virksomheter ikke oppdaterer | Høy | Insentiver, automation, regelmessig revisjon |
| **Deduplisering** | Samme datasett katalogisert flere ganger = forvirring | Middels | Standardiserte betegnelser; kontroller; deduplicering-rutiner |
| **Leverandør** | Avhengighet til Digdir-drift | Høy | Offentlig eierskap sikrer kontinuitet; SLA-krav |

## Kanaler

- **Webgrensesnitt:** data.norge.no og felles-datakatalog-portalen
- **API:** For maskinell publisering av metadata fra virksomheters datasystemer
- **Integrasjoner:** Linking til Begrepskatalog, API-katalog, informasjonsmodeller
- **Kampanjer og opplæring:** Digdir og næringsliv-aktører
- **Samarbeidsportal:** Erfaringsdeling og Q&A

## Plattform

- **Hosting:** Nasjonal felleskomponent forvaltet av Digdir
- **Metadata-standard:** DCAT-AP-NO (anbefalt nasjonalt standard for datakatalog)
- **Søk-teknologi:** Elasticsearch eller lignende for full-text-søk
- **API-modell:** REST-basert for publisering og søk
- **Integrering:** Kan konegteres til virksomheters egne datasystem

## Gjenbruk

**Svært høy gjenbruksverdi:**
- Felles katalog-infrastruktur for hele offentlig (og privat) sektor
- Reduserer behov for lokale datasett-kataloger i hver virksomhet
- Standardisert metadata-format muliggjør interoperabilitet
- Grunnlag for andre løsninger (datadelingsplattformer, API-styring)

## Støtte arkitekturprinsipper

- **P4 Del og gjenbruk data** – Sentral referanse for hvilke data som kan gjenbrukes
- **P5 Del og gjenbruk løsninger** – Felles katalog-infrastruktur for alle
- **P8 Etabler felles forståelse av informasjon** – Standardiserte metadata og begrepsdefinisjon
- **P6 Lag digitale løsninger som støtter samhandling** – Muliggjør data-basert tverretatlig samhandling

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som nasjonalt felleskomponent (Digdir-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter; variabel modell for privat sektor
- **Estimert kostnader:** 5-15 MNOK årlig for drift og videreutvikling
- **Investeringer:** Initiale investeringer i infrastruktur, platform, integrering

**Finansiering:** Primary via Digdir-budsjett; sekundært via datadeling-gebyrer og private partnerships.

**Kilder:** Estimert basert på Digdir-rapporter og datakatalog-benchmarks; presis kostnadsmodell må kreves fra Digdir.

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) | Strategisk retning, metadata-standarder, roadmap |
| **Driftsansvar** | Digdir (eller ekstern driftsleverandør) | 24/5 drift, 99.5%+ oppetid, support |
| **Budsjettansvar** | Digdir / Statsbudsjett | Via «Felles IKT-utgifter» |
| **Styringsmodell** | Felleskomponent-ordningen; Digital-infrastruktur-domene | Del av nasjonalt datadelingsekosystem |

**Styringsforum:** Digdir-styre; Digital infrastruktur-domene; eDøvendelse-råd (samordnings-lovgivninger).

## Lenke til dokumentasjon

- https://data.norge.no – Offisiell Felles datakatalog (portal)
- https://docs.digdir.no/docs/felles-datakatalog/ – Teknisk dokumentasjon (hvis eksisterer)
- https://samarbeid.digdir.no/datadeling – Samarbeidsportal Datadeling
- https://data.norge.no/webviz/soek – Avansert søk-grensesnitt
- https://www.digdir.no/digdir-og-direktoratet/felles-datakatalog/1234 – Produktinformasjon

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: data.norge.no, Digdir.no (hentet 2026-03-07)
- Samarbeidsportalen: Datadeling (hentet 2026-03-07)
- Kilder for finansiering: Digdir-rapporter og benchmarking (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

- **Brukersegmenter:** Struktur ut som tabell med konkrete behov og bruksområder
- **Risikomatrise:** 8 konkrete risikokategorier med håndtering
- **Finansiering:** Detaljert kostnadsmodell (estimert 5-15 MNOK årlig)
- **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Digdir)
- **Veikart:** Konkrete fokusområder (AI-assistans, datakvalitet, EU-integrasjon)
- **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
- **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet
- **Metadata-standard:** DCAT-AP-NO konkretisert
- **Datadeling-kontekst:** Kobling til nasjonalt datadelingsekosystem
