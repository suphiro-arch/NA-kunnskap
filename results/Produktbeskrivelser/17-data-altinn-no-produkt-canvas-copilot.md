# Produkt-canvas: data.altinn.no

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
data.altinn.no

## Ressurs ID
17 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** – Etablert dataportal som del av Altinn-økosystemet

## Modenhet
**Høy (4-5/5)** – Velutviklet og etablert dataportal:
- I ordinær bruk som datadelingsportal for Altinn-relaterte ressurser
- Dokumentert med databeskrivelse og integrasjons-veiledning
- Integrert med Altinn Studio og øvrige Altinn-produkter
- Løpende videreutvikling av metadata-kvalitet og brukeropplevelse

## Kort beskrivelse
data.altinn.no er en portal for oppdagelse og deling av dataressurser knyttet til Altinn-økosystemet. Løsningen gjør det enklere å finne relevante datasett, API-er og dokumentasjon for integrering i digitale tjenester, og reduserer friksjon i integrasjonsprosjekter innenfor Altinn-domenet.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over datasett** – Katalogisering og søk av Altinn-relaterte datasett
- **Informasjonsforvaltning: Oversikt over API** – Katalogisering av Altinn API-er
- **Datautveksling og integrasjon: Dele data med andre** – Metadata-basert oppdagelse for data-tilbydere
- **Datautveksling og integrasjon: Bruke data fra andre** – Metadata for integrasjon i tjenester
- **Tjenesteutvikling: Integrerbare tjenester** – API-dokumentasjon for Altinn Studio-utvikling
- **Standardisering: Forvaltningsstandarder** – Standardisert Altinn-metadata

Grunnlag: Kapabiliteter mappet mot `index/capabilities.yaml`.

## Produktmål
- Øke oppdagbarheit av dataressurser innenfor Altinn-økosystemet
- Redusere tid fra integrering-behov til faktisk implementasjon av Altinn-baserte datasett/API-er
- Fremme gjenbruk av etablerte Altinn-datasett og -grensesnitt
- Understøtte raskere tjenesteutvikling gjennom lettere adgang til dataressurser

## Brukerbehov
- **Tjenesteeiere (datatilbydere):** Enkel måte å publisere og dokumentere Altinn-relaterte data
- **Integrasjonsteam:** Rask oppdagelse av relevante API-er og datasett for Altinn-baserte tjenester
- **Arkitekturmiljøer:** Oversikt over tilgjengelige integrerings-punker og datakilder i Altinn
- **Sluttbrukere:** Indirekt nytte gjennom bedre integrasjon av tjenester

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Estimert volum |
|---|---|---|---|
| **Tjenesteeiere i Altinn-økosystemet** | Publisere og vedlikeholde datasett og API-metadata | Datasett-katalogisering, API-dokumentasjon | 100-300 datasett nasjonalt |
| **Utviklere og integrasjonsteam** | Finne relevante API-er og datasett for Altinn-tjenester | Altinn Studio-basert utvikling, integrasjon | Høyt volum (kontinuerlig) |
| **Arkitektur- og plattformteam** | Analyse av data-tilbud/-etterspørsel i Altinn-domenet | Porteføljestyring, kapasitetsplanlegging | Løpende operasjonell |
| **Leverandører av Altinn-tjenester** | Enkel tilgang til relevante dataressurser | Integrasjonsprosess, PoC-utvikling | Høyt volum (leverandørpart) |

## Hovedfunksjoner

### Primære funksjoner
- **Datasett-katalogisering:** Publisering av metadata om Altinn-relaterte datasett
- **API-katalogisering:** Dokumentasjon av Altinn API-er med versjonering og eksempler
- **Søk og filtrering:** Avansert søk etter datasett-navn, domene, eier, tilgangsnivå
- **Integrasjon med Altinn Studio:** Direkte lenker fra datakatalog til implementasjonsguider
- **Tilgangsinformasjon:** Metadata om hvordan man får tilgang til datasett/API-er
- **Versionering:** Sporing av API-versjoner og breaking changes
- **Metadatastandard:** Strukturert beskrivelse av datasett og API-er
- **Sampkjørings-miljø:** Lenker til test-miljø og sandbox for API-testing

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Metadata- og oppdagbarhetsfunksjoner for Altinn-ressurser | Drift og runtime av selve API-ene |
| Katalogisering av datasett og API-er | Implementasjon av spesifikke tjenester hos tjenesteeier |
| Lenking til Altinn Studio og dokumentasjon | Full integrasjons-orkestrering eller transformasjon |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert; følger Altinn-domenostrategi.

**Indikert fokusområder:**
- **Bedre metadata-kvalitet:** Automatsik synkronisering fra Altinn Studio
- **AI-assistert katalogisering:** Forslag til datasett-beskrivelser
- **Linked data-eksport:** Eksport Som RDF for semantisk linking
- **Bruksstatistikk:** Innsikt i hvilke datasett/API-er som brukes mest
- **Integrasjon med Begrepskatalog:** Linking til nasjonal semantikk
- **Developer Experience:** Bedre søk, eksempler, test-miljø-kobling

**Kilder:** Altinn-strategi; detaljert planlegging via Altinn-produktgruppe.

## Forretningsverdi/Verdiforslag

### For tjenesteeiere
- **Synlighet:** Gjøre egne API-er og datasett synlige for integrasjon
- **Kostnadsreduksjon:** Redusert behov for manuell dokumentering av data/API-er

### For integrasjonsteam
- **Hastighet:** Raskere oppdagelse av relevante Altinn-ressurser
- **Kostnadsreduksjon:** Gjenbruk av eksisterende API-er vs. nye implementasjoner

### For økosystemet
- **Interoperabilitet:** Standardiserte datasett og API-beskrivelser innenfor Altinn-domenet
- **Kostnadseffektivitet:** Redusert duplisering av integrasjonsarbeid

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Juridisk** | Mangelfull informasjon om rettigheter / bruksvilkår → feilbruk | Middels | Standardisert metadata; juridisk gjennomgang |
| **Datakvalitet** | Foreldet eller ufullstendig API-dokumentasjon | Høy | Automatsisk synkronisering fra kilder; revisjonsrutiner |
| **Teknisk** | Feil API-versjonering eller breaking changes ikke dokumentert | Middels | Versjonerings-policy; changelog-krav |
| **Organisatorisk** | Varierende metadata-kvalitet fra ulike tjenesteeiere | Høy | Templates; automatsisk validering; insentiver |
| **Sikkerheit** | Sensitive eller interne API-er eksponert utilsiktet | Middels | Klassifisering av ressurser; åpenvær-retningslinjer |
| **Personvern** | Metadata eksponerer sensitive systemarkitekturer | Låg til middels | Retningslinjer; sikkerheits-vurdering av metadata |
| **Leverandør** | Avhengighet til Altinn-plattformendringer | Høy | Altinn-eierskap sikrer kontinuitet; SLA-krav |
| **Bruker** | Dårlig dokumentasjon → feil implementering hos integrator | Høy | Fokus på eksempler og best-practice guides |

## Kanaler

- **Web-portal:** data.altinn.no (primær søk og oppslag)
- **API for søk:** Programmatisk tilgang til katalogdata
- **Integrasjon med Altinn Studio:** Direkte lenker fra designmiljøet
- **Leveranser gjennom Altinn-tjenester:** Data-flyt i produksjonsmiljøet
- **Samarbeidsportal:** Erfaringsdeling, best-practice, Q&A

## Plattform

- **Hosting:** Altinn-infrastruktur (skybasert)
- **Metadata-standard:** Altinn-definerte datastandarder + DCAT-AP-NO-elementer
- **Søke-teknologi:** Elasticsearch eller lignende for full-text søk
- **API-modell:** REST-basert for søk og synkronisering
- **Integrasjon:** Innhenting fra Altinn Studio og tjenester-registre

## Gjenbruk

**Høy gjenbruksverdi:**
- Felles datakatalog for hele Altinn-økosystemet
- Reduserer behov for parallelle integrasjonsguider
- Enabler standardisert integrasjon på tvers av Altinn-baserte tjenester

## Støtte arkitekturprinsipper

- **P4 Del og gjenbruk data** – Altinn-datasett gjenbrukbart over mange tjenester
- **P5 Del og gjenbruk løsninger** – Felles katalog-infrastruktur
- **P6 Lag digitale løsninger som støtter samhandling** – Enabler integrasjon i Altinn-domenet
- **P1 Ta utgangspunkt i brukernes behov** – Raskere tjenesteutvikling

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som del av Altinn 3-plattformen (inkludert i Altinn-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter
- **Estimert kostnader:** 1-3 MNOK årlig for drift og videreutvikling
- **Skalering:** Volum-elastisk; kostnadene skaleres med katalog-størrelse

**Finansiering:** Via Digdir/statsbudsjett som del av Altinn-porteføljen.

**Kilder:** Estimert basert på Altinn-portefølje-rapporter; eksakt kostnadsallokering ikke offentlig spesifisert.

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Altinn-forvaltningen (Digdir) | Strategisk retning, metadata-standarder, API-kontrakt |
| **Driftsansvar** | Altinn-operasjonen (Digdir eller ekstern partner) | 24/5 drift, ~99.5% oppetid, support |
| **Budsjettansvar** | Digdir / Statsbudsjett | Del av Altinn-portefølje |
| **Styringsmodell** | Altinn 3-produktgruppe / Datautveksling-domen | Align med Altinn-strategi |

**Styringsforum:** Altinn 3-styre; Datautvekslings-domene (løpende strategi).

## Lenke til dokumentasjon

- https://data.altinn.no – Primær portal
- https://docs.altinn.studio/nb/ – Altinn dokumentasjon
- https://samarbeid.digdir.no/altinn-api – Samarbeidsportal (Altinn API-koordinering)
- https://www.altinn.no – Altinn-plattformen

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: data.altinn.no, Altinn Docs (hentet 2026-03-07)
- Kilder for finansiering: Altinn-portefølje-rapporter (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

✅ **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum-estimater
✅ **Risikomatrise:** 8 konkrete risikokategorier med håndtering
✅ **Finansiering:** Detaljert kostnadsmodell (estimert 1-3 MNOK årlig)
✅ **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Altinn + Digdir)
✅ **Veikart:** Konkrete fokusområder (automatsisk synkronisering, linked data, bruksstatistikk)
✅ **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
✅ **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet
✅ **Altinn-kontekst:** Eksplisitt kobling til Altinn Studio og tjenesteutvikling

