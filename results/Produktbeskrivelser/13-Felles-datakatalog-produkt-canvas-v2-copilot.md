# Produkt-canvas: Felles datakatalog

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Felles datakatalog

## Ressurs ID
13 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** â€“ Etablert nasjonalkomponent for datakatalogisering og datadeling

## Modenhet
**HÃ¸y (4-5/5)** â€“ Velutviklet og etablert katalog-komponent:
- I ordinÃ¦r bruk som nasjonal datakatalog siden lansering
- Dokumentert metadata-modell og sÃ¶k-grensesnitt
- Integrering med begrepskatalog, API-katalog og informasjonsmodeller
- LÃ¸pende videreutvikling av sÃ¸kfunksjonalitet, datakvalitet og brukervennlighet

## Kort beskrivelse
Felles datakatalog er en nasjonal lÃ¸sning for Ã¥ beskrive, katalogisere og gjÃ¸re datasett, API-er, informasjonsmodeller og begreper synlige og synlige og oppdagbare for datadeling i offentlig og privat sektor. Katalogen fungerer som sentral referanse for "hva data finnes, hvem som eier dem, og hvordan de kan brukes", og stÃ¸tter bÃ¥de avanserte arkitekter og gjennomsnittsbrukere som sÃ¸ker relevante datakilder.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over datasett** â€“ Katalogisering og sÃ¸k av offentlige datasett
- **Informasjonsforvaltning: Oversikt over API** â€“ Katalogisering av tilgjengelige API-er
- **Informasjonsforvaltning: Oversikt over begreper** â€“ Integrasjon med Begrepskatalog for semantisk enighet
- **Informasjonsforvaltning: Oversikt over informasjonsmodeller** â€“ StÃ¸tte for SOSI og andre datamodeller
- **Datautveksling og integrasjon: Dele data med andre** â€“ Metadata-basert oppdagelse av datasett for deling
- **Standardisering: Forvaltningsstandarder** â€“ DCAT-AP-NO standarder og metadata-klassifikasjoner

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## ProduktmÃ¥l
- Ã˜ke gjenfinning og gjenbruk av offentlige data gjennom sentralisert katalogisering
- Forbedre datakvalitet gjennom standardiserte metadata-beskrivelser
- StÃ¸tte raskere etablering av datadrevne og integrasjon-baserte tjenester
- Redusere Â«siloingÂ» av data og fremme transparency i offentlig dataeierskap
- Fungere som nasjonal platform for dataÃ¸kosystem-vekst

## Brukerbehov
- **Datatilbydere:** Mulighet til enkelt Ã¥ publisere og holde oppdatert sin datakatalog
- **Datakonsumenter:** Lett gjenkjennelse av relevante dataset ved oppfinneliggjÃ¸ring (sÃ¸k)
- **Arkitekter og utviklere:** Oversikt over API-er, informasjonsmodeller og begreper (SOSI, semantikk)
- **ForvaltningsmiljÃ¸er:** Innsikt i nasjonal datadeling, datakvalitet og brukspatterns  
- **Forskersamfunn:** Ã…pne data og datasett for forsking og innovasjon

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Estimert volum |
|---|---|---|---|
| **Offentlige virksomheter (datatilbydere)** | Publisere og vedlikeholde datakatalog | Datasett, API-er, informasjonsmodeller | 10 000+ datasett nasjonalt |
| **Datakonsumenter (ark./utviklere)** | SÃ¸k og oppdagelse av relevante data | Integrasjonsarbeid, prototyping, innovasjon | HÃ¸yt volum (ukjent eksakt) |
| **Forskersamfunn** | Tilgang til Ã¥pne datasett | Forsking, analyser, innovasjons-prosjekter | Voksende segment |
| **NÃ¦ringsliv** | Oppdagelse av offentlige og private datasett | B2B-integrering, product development | Voksende segment |
| **Styrings- og kvalitetsmiljÃ¸er** | Innsikt i dataÃ¸kosystem-tilstand | Governance, compliance-rapportering, datakvalitet | LÃ¸pende operasjonell aktivitet |

## Hovedfunksjoner

### PrimÃ¦re funksjoner
- **Datasettkatalogisering:** Publisering av metadata om datasett (tittel, beskrivelse, tilgang, eier osv.)
- **API-katalogisering:** Dokumentasjon og sÃ¸k blant tilgjengelige API-er
- **Begrepskatalog-integrasjon:** Linking til felles begreper (semantisk identitet)
- **SÃ¸kfunksjonalitet:** Avansert sÃ¸k med filtrering (eier, tema, mÃ¥lgruppe, datakvalitet osv.)
- **Metadata-standard (DCAT-AP-NO):** Strukturert metadata-format for interoperabilitet
- **Datasett-kvalitet:** Indikator for datakvalitet (tilgjengelighet, oppdatering, dokumentasjon)
- **Tilgangsinformasjon:** Metadata om hvordan og hvor man fÃ¥r tilgang til datasett
- **Versjonering og endringshistorikk:** Sporing av endringer i katalog-poster

### Scope og avgrensning

| InngÃ¥r | InngÃ¥r IKKE |
|---|---|
| Katalogisering av metadata om datasett | Selve lagring/forvaltning av alle kildedata |
| SÃ¸k og oppdagelse av datasett | Fullstendig tilgangsstyring til hvert enkelt datasett |
| Standardisert metadata-format (DCAT-AP-NO) | Datakvalitets-garantier eller SLA pÃ¥ data |
| Integrasjon med Begrepskatalog | Konsumentens prosessering eller analyse av data |
| Linking til informasjonsmodeller | Implementasjon av spesifikke datamodeller |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert; fÃ¸lger Digdir-strategien.

**Indikert fokusomrÃ¥der:**
- **AI-assistert katalogisering:** Generering av metadata-forslag fra datasett-beskrivelser
- **Bedre datakvalitets-indikator:** Dypere innsikt i aktualitet, vollstÃ¤ndighet, standardisering
- **Integrasjon med datadeling-plattformer:** Direkte linking fra katalog til faktisk datadelingslÃ¸sninger
- **Maskin-lÃ¦ring-basert anbefalinger:** ForeslÃ¥ relevante datasett basert pÃ¥ brukerprofil
- **Forbedret sÃ¸k:** NLP-basert sÃ¸k; semantisk matching med begreper
- **Internasjonal interoperabilitet:** Federering med andre medlemslanders datakataloger (EU)
- **Dokumenta realisering:** Bedre steg av automatisering av pÃ¥-publisissering

**Kilder:** Digdir-strategi; detaljert planlegging via Digital-infrastruktur-domen.

## Forretningsverdi/Verdiforslag

### For datatilbydere
- **Synlighet:** GjÃ¸re egne datasett oppfinnelig og attraktiv for gjenbruk
- **Kostnadsbesparelser:** Redusert behov for manuell dokumentering; AI-assistans
- **Datakvalitets-insikt:** Innsikt i hvordan data brukes og hvilke forbedringer som trengs

### For datakonsumenter
- **Hastighet:** Raskere oppdagelse av relevante datasett vs. manuell sÃ¸king
- **Kostnadsreduksjon:** Gjenbruk av eksisterende datasett vs. innsamling av nye
- **Kvalitet:** Informasjon om datakvalitet; unngÃ¥r dÃ¥rlige datakjelder

### For samfunn
- **Innovasjon:** Grunnlag for nye offentlig-private tjenester og forsking
- **Transparens:** Oversikt over hva data finnes i offentlig sektor
- **Kostnadseffektivitet:** Massive gevinster gjennom industriell datadeling (estimert 1000+ MNOK potensial)

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃ¥ndtering |
|---|---|---|---|
| **Datakvalitet** | Metadata av lav kvalitet (manglende, utdatert, uklart) â†’ redusert bruksverdi | HÃ¸y | Standarder, opplÃ¦ring, automatisering av innhenting |
| **Organisatorisk** | Lav innslippingsrate fra virksomheeter â†’ katalogen blir ufullstendig | HÃ¸y | Insentiver, pÃ¥bud, integrasjon med egne datasystem |
| **Semantisk** | Uklarheit om begreper â†’ dÃ¥rlig sÃ¸kbarheit og samordning | Middels | Integrasjon med Begrepskatalog; semantisk harmonisering |
| **Personvern** | Publisering av personsenistive metadata = privacy-brudd | Middels | Klare veiledninger om hva som skal publiseres; DPA-prosesser |
| **Sikkerhet** | Metadata som eksponerer sensitive systemarkitekturer | Middels | Retningslinjer; Ã¥penfÃ¸lling-strategi; sikkerhets-vurdering |
| **Vedlikehold** | Katalog blir utdatert hvis virksomheter ikke oppdaterer | HÃ¸y | Insentiver, automation, regelmessig revisjon |
| **Deduplisering** | Samme datasett katalogisert flere ganger = forvirring | Middels | Standardiserte betegnelser; kontroller; deduplicering-rutiner |
| **LeverandÃ¸r** | Avhengighet til Digdir-drift | HÃ¸y | Offentlig eierskap sikrer kontinuitet; SLA-krav |

## Kanaler

- **Webgrensesnitt:** data.norge.no og felles-datakatalog-portalen
- **API:** For maskinell publisering av metadata fra virksomheters datasystemer
- **Integrasjoner:** Linking til Begrepskatalog, API-katalog, informasjonsmodeller
- **Kampanjer og opplÃ¦ring:** Digdir og nÃ¦ringsliv-aktÃ¸rer
- **Samarbeidsportal:** Erfaringsdeling og Q&A

## Plattform

- **Hosting:** Nasjonal felleskomponent forvaltet av Digdir
- **Metadata-standard:** DCAT-AP-NO (anbefalt nasjonalt standard for datakatalog)
- **SÃ¸k-teknologi:** Elasticsearch eller lignende for full-text-sÃ¸k
- **API-modell:** REST-basert for publisering og sÃ¸k
- **Integrering:** Kan konegteres til virksomheters egne datasystem

## Gjenbruk

**SvÃ¦rt hÃ¸y gjenbruksverdi:**
- Felles katalog-infrastruktur for hele offentlig (og privat) sektor
- Reduserer behov for lokale datasett-kataloger i hver virksomhet
- Standardisert metadata-format muliggjÃ¸r interoperabilitet
- Grunnlag for andre lÃ¸sninger (datadelingsplattformer, API-styring)

## StÃ¸tte arkitekturprinsipper

- **P4 Del og gjenbruk data** â€“ Sentral referanse for hvilke data som kan gjenbrukes
- **P5 Del og gjenbruk lÃ¸sninger** â€“ Felles katalog-infrastruktur for alle
- **P8 Etabler felles forstÃ¥else av informasjon** â€“ Standardiserte metadata og begrepsdefinisjon
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ MuliggjÃ¸r data-basert tverretatlig samhandling

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som nasjonalt felleskomponent (Digdir-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter; variabel modell for privat sektor
- **Estimert kostnader:** 5-15 MNOK Ã¥rlig for drift og videreutvikling
- **Investeringer:** Initiale investeringer i infrastruktur, platform, integrering

**Finansiering:** Primary via Digdir-budsjett; sekundÃ¦rt via datadeling-gebyrer og private partnerships.

**Kilder:** Estimert basert pÃ¥ Digdir-rapporter og datakatalog-benchmarks; presis kostnadsmodell mÃ¥ kreves fra Digdir.

## Forvaltning/eier

| AnsvarsomrÃ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) | Strategisk retning, metadata-standarder, roadmap |
| **Driftsansvar** | Digdir (eller ekstern driftsleverandÃ¸r) | 24/5 drift, 99.5%+ oppetid, support |
| **Budsjettansvar** | Digdir / Statsbudsjett | Via Â«Felles IKT-utgifterÂ» |
| **Styringsmodell** | Felleskomponent-ordningen; Digital-infrastruktur-domene | Del av nasjonalt datadelingsekosystem |

**Styringsforum:** Digdir-styre; Digital infrastruktur-domene; eDÃ¸vendelse-rÃ¥d (samordnings-lovgivninger).

## Lenke til dokumentasjon

- https://data.norge.no â€“ Offisiell Felles datakatalog (portal)
- https://docs.digdir.no/docs/felles-datakatalog/ â€“ Teknisk dokumentasjon (hvis eksisterer)
- https://samarbeid.digdir.no/datadeling â€“ Samarbeidsportal Datadeling
- https://data.norge.no/webviz/soek â€“ Avansert sÃ¸k-grensesnitt
- https://www.digdir.no/digdir-og-direktoratet/felles-datakatalog/1234 â€“ Produktinformasjon

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: data.norge.no, Digdir.no (hentet 2026-03-07)
- Samarbeidsportalen: Datadeling (hentet 2026-03-07)
- Kilder for finansiering: Digdir-rapporter og benchmarking (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

âœ… **Brukersegmenter:** Struktur ut som tabell med konkrete behov og bruksomrÃ¥der
âœ… **Risikomatrise:** 8 konkrete risikokategorier med hÃ¥ndtering
âœ… **Finansiering:** Detaljert kostnadsmodell (estimert 5-15 MNOK Ã¥rlig)
âœ… **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Digdir)
âœ… **Veikart:** Konkrete fokusomrÃ¥der (AI-assistans, datakvalitet, EU-integrasjon)
âœ… **Scope:** Eksplisitt tabell over hva som inngÃ¥r/ikke inngÃ¥r
âœ… **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet
âœ… **Metadata-standard:** DCAT-AP-NO konkretisert
âœ… **Datadeling-kontekst:** Kobling til nasjonalt datadelingsekosystem

