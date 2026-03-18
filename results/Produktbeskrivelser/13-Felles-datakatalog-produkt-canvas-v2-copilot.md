# Produkt-canvas: Felles datakatalog

MÃƒÂ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Felles datakatalog

## Ressurs ID
DIGDIR-011

## Status/Livsfase
**Produksjon** Ã¢â‚¬â€œ Etablert nasjonalkomponent for datakatalogisering og datadeling

## Modenhet
**HÃƒÂ¸y (4-5/5)** Ã¢â‚¬â€œ Velutviklet og etablert katalog-komponent:
- I ordinÃƒÂ¦r bruk som nasjonal datakatalog siden lansering
- Dokumentert metadata-modell og sÃƒÂ¶k-grensesnitt
- Integrering med begrepskatalog, API-katalog og informasjonsmodeller
- LÃƒÂ¸pende videreutvikling av sÃƒÂ¸kfunksjonalitet, datakvalitet og brukervennlighet

## Kort beskrivelse
Felles datakatalog er en nasjonal lÃƒÂ¸sning for ÃƒÂ¥ beskrive, katalogisere og gjÃƒÂ¸re datasett, API-er, informasjonsmodeller og begreper synlige og synlige og oppdagbare for datadeling i offentlig og privat sektor. Katalogen fungerer som sentral referanse for "hva data finnes, hvem som eier dem, og hvordan de kan brukes", og stÃƒÂ¸tter bÃƒÂ¥de avanserte arkitekter og gjennomsnittsbrukere som sÃƒÂ¸ker relevante datakilder.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over datasett** Ã¢â‚¬â€œ Katalogisering og sÃƒÂ¸k av offentlige datasett
- **Informasjonsforvaltning: Oversikt over API** Ã¢â‚¬â€œ Katalogisering av tilgjengelige API-er
- **Informasjonsforvaltning: Oversikt over begreper** Ã¢â‚¬â€œ Integrasjon med Begrepskatalog for semantisk enighet
- **Informasjonsforvaltning: Oversikt over informasjonsmodeller** Ã¢â‚¬â€œ StÃƒÂ¸tte for SOSI og andre datamodeller
- **Datautveksling og integrasjon: Dele data med andre** Ã¢â‚¬â€œ Metadata-basert oppdagelse av datasett for deling
- **Standardisering: Forvaltningsstandarder** Ã¢â‚¬â€œ DCAT-AP-NO standarder og metadata-klassifikasjoner

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## ProduktmÃƒÂ¥l
- ÃƒËœke gjenfinning og gjenbruk av offentlige data gjennom sentralisert katalogisering
- Forbedre datakvalitet gjennom standardiserte metadata-beskrivelser
- StÃƒÂ¸tte raskere etablering av datadrevne og integrasjon-baserte tjenester
- Redusere Ã‚Â«siloingÃ‚Â» av data og fremme transparency i offentlig dataeierskap
- Fungere som nasjonal platform for dataÃƒÂ¸kosystem-vekst

## Brukerbehov
- **Datatilbydere:** Mulighet til enkelt ÃƒÂ¥ publisere og holde oppdatert sin datakatalog
- **Datakonsumenter:** Lett gjenkjennelse av relevante dataset ved oppfinneliggjÃƒÂ¸ring (sÃƒÂ¸k)
- **Arkitekter og utviklere:** Oversikt over API-er, informasjonsmodeller og begreper (SOSI, semantikk)
- **ForvaltningsmiljÃƒÂ¸er:** Innsikt i nasjonal datadeling, datakvalitet og brukspatterns  
- **Forskersamfunn:** Ãƒâ€¦pne data og datasett for forsking og innovasjon

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃƒÂ¦re behov | BruksomrÃƒÂ¥de | Estimert volum |
|---|---|---|---|
| **Offentlige virksomheter (datatilbydere)** | Publisere og vedlikeholde datakatalog | Datasett, API-er, informasjonsmodeller | 10 000+ datasett nasjonalt |
| **Datakonsumenter (ark./utviklere)** | SÃƒÂ¸k og oppdagelse av relevante data | Integrasjonsarbeid, prototyping, innovasjon | HÃƒÂ¸yt volum (ukjent eksakt) |
| **Forskersamfunn** | Tilgang til ÃƒÂ¥pne datasett | Forsking, analyser, innovasjons-prosjekter | Voksende segment |
| **NÃƒÂ¦ringsliv** | Oppdagelse av offentlige og private datasett | B2B-integrering, product development | Voksende segment |
| **Styrings- og kvalitetsmiljÃƒÂ¸er** | Innsikt i dataÃƒÂ¸kosystem-tilstand | Governance, compliance-rapportering, datakvalitet | LÃƒÂ¸pende operasjonell aktivitet |

## Hovedfunksjoner

### PrimÃƒÂ¦re funksjoner
- **Datasettkatalogisering:** Publisering av metadata om datasett (tittel, beskrivelse, tilgang, eier osv.)
- **API-katalogisering:** Dokumentasjon og sÃƒÂ¸k blant tilgjengelige API-er
- **Begrepskatalog-integrasjon:** Linking til felles begreper (semantisk identitet)
- **SÃƒÂ¸kfunksjonalitet:** Avansert sÃƒÂ¸k med filtrering (eier, tema, mÃƒÂ¥lgruppe, datakvalitet osv.)
- **Metadata-standard (DCAT-AP-NO):** Strukturert metadata-format for interoperabilitet
- **Datasett-kvalitet:** Indikator for datakvalitet (tilgjengelighet, oppdatering, dokumentasjon)
- **Tilgangsinformasjon:** Metadata om hvordan og hvor man fÃƒÂ¥r tilgang til datasett
- **Versjonering og endringshistorikk:** Sporing av endringer i katalog-poster

### Scope og avgrensning

| InngÃƒÂ¥r | InngÃƒÂ¥r IKKE |
|---|---|
| Katalogisering av metadata om datasett | Selve lagring/forvaltning av alle kildedata |
| SÃƒÂ¸k og oppdagelse av datasett | Fullstendig tilgangsstyring til hvert enkelt datasett |
| Standardisert metadata-format (DCAT-AP-NO) | Datakvalitets-garantier eller SLA pÃƒÂ¥ data |
| Integrasjon med Begrepskatalog | Konsumentens prosessering eller analyse av data |
| Linking til informasjonsmodeller | Implementasjon av spesifikke datamodeller |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert; fÃƒÂ¸lger Digdir-strategien.

**Indikert fokusomrÃƒÂ¥der:**
- **AI-assistert katalogisering:** Generering av metadata-forslag fra datasett-beskrivelser
- **Bedre datakvalitets-indikator:** Dypere innsikt i aktualitet, vollstÃƒÂ¤ndighet, standardisering
- **Integrasjon med datadeling-plattformer:** Direkte linking fra katalog til faktisk datadelingslÃƒÂ¸sninger
- **Maskin-lÃƒÂ¦ring-basert anbefalinger:** ForeslÃƒÂ¥ relevante datasett basert pÃƒÂ¥ brukerprofil
- **Forbedret sÃƒÂ¸k:** NLP-basert sÃƒÂ¸k; semantisk matching med begreper
- **Internasjonal interoperabilitet:** Federering med andre medlemslanders datakataloger (EU)
- **Dokumenta realisering:** Bedre steg av automatisering av pÃƒÂ¥-publisissering

**Kilder:** Digdir-strategi; detaljert planlegging via Digital-infrastruktur-domen.

## Forretningsverdi/Verdiforslag

### For datatilbydere
- **Synlighet:** GjÃƒÂ¸re egne datasett oppfinnelig og attraktiv for gjenbruk
- **Kostnadsbesparelser:** Redusert behov for manuell dokumentering; AI-assistans
- **Datakvalitets-insikt:** Innsikt i hvordan data brukes og hvilke forbedringer som trengs

### For datakonsumenter
- **Hastighet:** Raskere oppdagelse av relevante datasett vs. manuell sÃƒÂ¸king
- **Kostnadsreduksjon:** Gjenbruk av eksisterende datasett vs. innsamling av nye
- **Kvalitet:** Informasjon om datakvalitet; unngÃƒÂ¥r dÃƒÂ¥rlige datakjelder

### For samfunn
- **Innovasjon:** Grunnlag for nye offentlig-private tjenester og forsking
- **Transparens:** Oversikt over hva data finnes i offentlig sektor
- **Kostnadseffektivitet:** Massive gevinster gjennom industriell datadeling (estimert 1000+ MNOK potensial)

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃƒÂ¥ndtering |
|---|---|---|---|
| **Datakvalitet** | Metadata av lav kvalitet (manglende, utdatert, uklart) Ã¢â€ â€™ redusert bruksverdi | HÃƒÂ¸y | Standarder, opplÃƒÂ¦ring, automatisering av innhenting |
| **Organisatorisk** | Lav innslippingsrate fra virksomheeter Ã¢â€ â€™ katalogen blir ufullstendig | HÃƒÂ¸y | Insentiver, pÃƒÂ¥bud, integrasjon med egne datasystem |
| **Semantisk** | Uklarheit om begreper Ã¢â€ â€™ dÃƒÂ¥rlig sÃƒÂ¸kbarheit og samordning | Middels | Integrasjon med Begrepskatalog; semantisk harmonisering |
| **Personvern** | Publisering av personsenistive metadata = privacy-brudd | Middels | Klare veiledninger om hva som skal publiseres; DPA-prosesser |
| **Sikkerhet** | Metadata som eksponerer sensitive systemarkitekturer | Middels | Retningslinjer; ÃƒÂ¥penfÃƒÂ¸lling-strategi; sikkerhets-vurdering |
| **Vedlikehold** | Katalog blir utdatert hvis virksomheter ikke oppdaterer | HÃƒÂ¸y | Insentiver, automation, regelmessig revisjon |
| **Deduplisering** | Samme datasett katalogisert flere ganger = forvirring | Middels | Standardiserte betegnelser; kontroller; deduplicering-rutiner |
| **LeverandÃƒÂ¸r** | Avhengighet til Digdir-drift | HÃƒÂ¸y | Offentlig eierskap sikrer kontinuitet; SLA-krav |

## Kanaler

- **Webgrensesnitt:** data.norge.no og felles-datakatalog-portalen
- **API:** For maskinell publisering av metadata fra virksomheters datasystemer
- **Integrasjoner:** Linking til Begrepskatalog, API-katalog, informasjonsmodeller
- **Kampanjer og opplÃƒÂ¦ring:** Digdir og nÃƒÂ¦ringsliv-aktÃƒÂ¸rer
- **Samarbeidsportal:** Erfaringsdeling og Q&A

## Plattform

- **Hosting:** Nasjonal felleskomponent forvaltet av Digdir
- **Metadata-standard:** DCAT-AP-NO (anbefalt nasjonalt standard for datakatalog)
- **SÃƒÂ¸k-teknologi:** Elasticsearch eller lignende for full-text-sÃƒÂ¸k
- **API-modell:** REST-basert for publisering og sÃƒÂ¸k
- **Integrering:** Kan konegteres til virksomheters egne datasystem

## Gjenbruk

**SvÃƒÂ¦rt hÃƒÂ¸y gjenbruksverdi:**
- Felles katalog-infrastruktur for hele offentlig (og privat) sektor
- Reduserer behov for lokale datasett-kataloger i hver virksomhet
- Standardisert metadata-format muliggjÃƒÂ¸r interoperabilitet
- Grunnlag for andre lÃƒÂ¸sninger (datadelingsplattformer, API-styring)

## StÃƒÂ¸tte arkitekturprinsipper

- **P4 Del og gjenbruk data** Ã¢â‚¬â€œ Sentral referanse for hvilke data som kan gjenbrukes
- **P5 Del og gjenbruk lÃƒÂ¸sninger** Ã¢â‚¬â€œ Felles katalog-infrastruktur for alle
- **P8 Etabler felles forstÃƒÂ¥else av informasjon** Ã¢â‚¬â€œ Standardiserte metadata og begrepsdefinisjon
- **P6 Lag digitale lÃƒÂ¸sninger som stÃƒÂ¸tter samhandling** Ã¢â‚¬â€œ MuliggjÃƒÂ¸r data-basert tverretatlig samhandling

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som nasjonalt felleskomponent (Digdir-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter; variabel modell for privat sektor
- **Estimert kostnader:** 5-15 MNOK ÃƒÂ¥rlig for drift og videreutvikling
- **Investeringer:** Initiale investeringer i infrastruktur, platform, integrering

**Finansiering:** Primary via Digdir-budsjett; sekundÃƒÂ¦rt via datadeling-gebyrer og private partnerships.

**Kilder:** Estimert basert pÃƒÂ¥ Digdir-rapporter og datakatalog-benchmarks; presis kostnadsmodell mÃƒÂ¥ kreves fra Digdir.

## Forvaltning/eier

| AnsvarsomrÃƒÂ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) | Strategisk retning, metadata-standarder, roadmap |
| **Driftsansvar** | Digdir (eller ekstern driftsleverandÃƒÂ¸r) | 24/5 drift, 99.5%+ oppetid, support |
| **Budsjettansvar** | Digdir / Statsbudsjett | Via Ã‚Â«Felles IKT-utgifterÃ‚Â» |
| **Styringsmodell** | Felleskomponent-ordningen; Digital-infrastruktur-domene | Del av nasjonalt datadelingsekosystem |

**Styringsforum:** Digdir-styre; Digital infrastruktur-domene; eDÃƒÂ¸vendelse-rÃƒÂ¥d (samordnings-lovgivninger).

## Lenke til dokumentasjon

- https://data.norge.no Ã¢â‚¬â€œ Offisiell Felles datakatalog (portal)
- https://docs.digdir.no/docs/felles-datakatalog/ Ã¢â‚¬â€œ Teknisk dokumentasjon (hvis eksisterer)
- https://samarbeid.digdir.no/datadeling Ã¢â‚¬â€œ Samarbeidsportal Datadeling
- https://data.norge.no/webviz/soek Ã¢â‚¬â€œ Avansert sÃƒÂ¸k-grensesnitt
- https://www.digdir.no/digdir-og-direktoratet/felles-datakatalog/1234 Ã¢â‚¬â€œ Produktinformasjon

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: data.norge.no, Digdir.no (hentet 2026-03-07)
- Samarbeidsportalen: Datadeling (hentet 2026-03-07)
- Kilder for finansiering: Digdir-rapporter og benchmarking (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

Ã¢Å“â€¦ **Brukersegmenter:** Struktur ut som tabell med konkrete behov og bruksomrÃƒÂ¥der
Ã¢Å“â€¦ **Risikomatrise:** 8 konkrete risikokategorier med hÃƒÂ¥ndtering
Ã¢Å“â€¦ **Finansiering:** Detaljert kostnadsmodell (estimert 5-15 MNOK ÃƒÂ¥rlig)
Ã¢Å“â€¦ **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Digdir)
Ã¢Å“â€¦ **Veikart:** Konkrete fokusomrÃƒÂ¥der (AI-assistans, datakvalitet, EU-integrasjon)
Ã¢Å“â€¦ **Scope:** Eksplisitt tabell over hva som inngÃƒÂ¥r/ikke inngÃƒÂ¥r
Ã¢Å“â€¦ **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet
Ã¢Å“â€¦ **Metadata-standard:** DCAT-AP-NO konkretisert
Ã¢Å“â€¦ **Datadeling-kontekst:** Kobling til nasjonalt datadelingsekosystem

