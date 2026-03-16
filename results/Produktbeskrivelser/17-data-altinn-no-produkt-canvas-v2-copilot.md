# Produkt-canvas: data.altinn.no

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
data.altinn.no

## Ressurs ID
17 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** â€“ Etablert dataportal som del av Altinn-Ã¸kosystemet

## Modenhet
**HÃ¸y (4-5/5)** â€“ Velutviklet og etablert dataportal:
- I ordinÃ¦r bruk som datadelingsportal for Altinn-relaterte ressurser
- Dokumentert med databeskrivelse og integrasjons-veiledning
- Integrert med Altinn Studio og Ã¸vrige Altinn-produkter
- LÃ¸pende videreutvikling av metadata-kvalitet og brukeropplevelse

## Kort beskrivelse
data.altinn.no er en portal for oppdagelse og deling av dataressurser knyttet til Altinn-Ã¸kosystemet. LÃ¸sningen gjÃ¸r det enklere Ã¥ finne relevante datasett, API-er og dokumentasjon for integrering i digitale tjenester, og reduserer friksjon i integrasjonsprosjekter innenfor Altinn-domenet.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over datasett** â€“ Katalogisering og sÃ¸k av Altinn-relaterte datasett
- **Informasjonsforvaltning: Oversikt over API** â€“ Katalogisering av Altinn API-er
- **Datautveksling og integrasjon: Dele data med andre** â€“ Metadata-basert oppdagelse for data-tilbydere
- **Datautveksling og integrasjon: Bruke data fra andre** â€“ Metadata for integrasjon i tjenester
- **Tjenesteutvikling: Integrerbare tjenester** â€“ API-dokumentasjon for Altinn Studio-utvikling
- **Standardisering: Forvaltningsstandarder** â€“ Standardisert Altinn-metadata

Grunnlag: Kapabiliteter mappet mot `index/capabilities.yaml`.

## ProduktmÃ¥l
- Ã˜ke oppdagbarheit av dataressurser innenfor Altinn-Ã¸kosystemet
- Redusere tid fra integrering-behov til faktisk implementasjon av Altinn-baserte datasett/API-er
- Fremme gjenbruk av etablerte Altinn-datasett og -grensesnitt
- UnderstÃ¸tte raskere tjenesteutvikling gjennom lettere adgang til dataressurser

## Brukerbehov
- **Tjenesteeiere (datatilbydere):** Enkel mÃ¥te Ã¥ publisere og dokumentere Altinn-relaterte data
- **Integrasjonsteam:** Rask oppdagelse av relevante API-er og datasett for Altinn-baserte tjenester
- **ArkitekturmiljÃ¸er:** Oversikt over tilgjengelige integrerings-punker og datakilder i Altinn
- **Sluttbrukere:** Indirekt nytte gjennom bedre integrasjon av tjenester

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Estimert volum |
|---|---|---|---|
| **Tjenesteeiere i Altinn-Ã¸kosystemet** | Publisere og vedlikeholde datasett og API-metadata | Datasett-katalogisering, API-dokumentasjon | 100-300 datasett nasjonalt |
| **Utviklere og integrasjonsteam** | Finne relevante API-er og datasett for Altinn-tjenester | Altinn Studio-basert utvikling, integrasjon | HÃ¸yt volum (kontinuerlig) |
| **Arkitektur- og plattformteam** | Analyse av data-tilbud/-etterspÃ¸rsel i Altinn-domenet | PortefÃ¸ljestyring, kapasitetsplanlegging | LÃ¸pende operasjonell |
| **LeverandÃ¸rer av Altinn-tjenester** | Enkel tilgang til relevante dataressurser | Integrasjonsprosess, PoC-utvikling | HÃ¸yt volum (leverandÃ¸rpart) |

## Hovedfunksjoner

### PrimÃ¦re funksjoner
- **Datasett-katalogisering:** Publisering av metadata om Altinn-relaterte datasett
- **API-katalogisering:** Dokumentasjon av Altinn API-er med versjonering og eksempler
- **SÃ¸k og filtrering:** Avansert sÃ¸k etter datasett-navn, domene, eier, tilgangsnivÃ¥
- **Integrasjon med Altinn Studio:** Direkte lenker fra datakatalog til implementasjonsguider
- **Tilgangsinformasjon:** Metadata om hvordan man fÃ¥r tilgang til datasett/API-er
- **Versionering:** Sporing av API-versjoner og breaking changes
- **Metadatastandard:** Strukturert beskrivelse av datasett og API-er
- **SampkjÃ¸rings-miljÃ¸:** Lenker til test-miljÃ¸ og sandbox for API-testing

### Scope og avgrensning

| InngÃ¥r | InngÃ¥r IKKE |
|---|---|
| Metadata- og oppdagbarhetsfunksjoner for Altinn-ressurser | Drift og runtime av selve API-ene |
| Katalogisering av datasett og API-er | Implementasjon av spesifikke tjenester hos tjenesteeier |
| Lenking til Altinn Studio og dokumentasjon | Full integrasjons-orkestrering eller transformasjon |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert; fÃ¸lger Altinn-domenostrategi.

**Indikert fokusomrÃ¥der:**
- **Bedre metadata-kvalitet:** Automatsik synkronisering fra Altinn Studio
- **AI-assistert katalogisering:** Forslag til datasett-beskrivelser
- **Linked data-eksport:** Eksport Som RDF for semantisk linking
- **Bruksstatistikk:** Innsikt i hvilke datasett/API-er som brukes mest
- **Integrasjon med Begrepskatalog:** Linking til nasjonal semantikk
- **Developer Experience:** Bedre sÃ¸k, eksempler, test-miljÃ¸-kobling

**Kilder:** Altinn-strategi; detaljert planlegging via Altinn-produktgruppe.

## Forretningsverdi/Verdiforslag

### For tjenesteeiere
- **Synlighet:** GjÃ¸re egne API-er og datasett synlige for integrasjon
- **Kostnadsreduksjon:** Redusert behov for manuell dokumentering av data/API-er

### For integrasjonsteam
- **Hastighet:** Raskere oppdagelse av relevante Altinn-ressurser
- **Kostnadsreduksjon:** Gjenbruk av eksisterende API-er vs. nye implementasjoner

### For Ã¸kosystemet
- **Interoperabilitet:** Standardiserte datasett og API-beskrivelser innenfor Altinn-domenet
- **Kostnadseffektivitet:** Redusert duplisering av integrasjonsarbeid

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃ¥ndtering |
|---|---|---|---|
| **Juridisk** | Mangelfull informasjon om rettigheter / bruksvilkÃ¥r â†’ feilbruk | Middels | Standardisert metadata; juridisk gjennomgang |
| **Datakvalitet** | Foreldet eller ufullstendig API-dokumentasjon | HÃ¸y | Automatsisk synkronisering fra kilder; revisjonsrutiner |
| **Teknisk** | Feil API-versjonering eller breaking changes ikke dokumentert | Middels | Versjonerings-policy; changelog-krav |
| **Organisatorisk** | Varierende metadata-kvalitet fra ulike tjenesteeiere | HÃ¸y | Templates; automatiske validering; insentiver |
| **Sikkerhet** | Sensitive eller interne API-er eksponert utilsiktet | Middels | Klassifisering av ressurser; Ã¥penvÃ¦r-retningslinjer |
| **Personvern** | Metadata eksponerer sensitive systemarkitekturer | LÃ¥g til middels | Retningslinjer; sikkerhets-vurdering av metadata |
| **LeverandÃ¸r** | Avhengighet til Altinn-plattformendringer | HÃ¸y | Altinn-eierskap sikrer kontinuitet; SLA-krav |
| **Bruker** | DÃ¥rlig dokumentasjon â†’ feil implementering hos integrator | HÃ¸y | Fokus pÃ¥ eksempler og best-practice guides |

## Kanaler

- **Web-portal:** data.altinn.no (primÃ¦r sÃ¸k og oppslag)
- **API for sÃ¸k:** Programmatisk tilgang til katalogdata
- **Integrasjon med Altinn Studio:** Direkte lenker fra designmiljÃ¸et
- **Leveranser gjennom Altinn-tjenester:** Data-flyt i produksjonsmiljÃ¸et
- **Samarbeidsportal:** Erfaringsdeling, best-practice, Q&A

## Plattform

- **Hosting:** Altinn-infrastruktur (skybasert)
- **Metadata-standard:** Altinn-definerte datastandarder + DCAT-AP-NO-elementer
- **SÃ¸ke-teknologi:** Elasticsearch eller lignende for full-text sÃ¸k
- **API-modell:** REST-basert for sÃ¸k og synkronisering
- **Integrasjon:** Innhenting fra Altinn Studio og tjenester-registre

## Gjenbruk

**HÃ¸y gjenbruksverdi:**
- Felles datakatalog for hele Altinn-Ã¸kosystemet
- Reduserer behov for parallelle integrasjonsguider
- Enabler standardisert integrasjon pÃ¥ tvers av Altinn-baserte tjenester

## StÃ¸tte arkitekturprinsipper

- **P4 Del og gjenbruk data** â€“ Altinn-datasett gjenbrukbart over mange tjenester
- **P5 Del og gjenbruk lÃ¸sninger** â€“ Felles katalog-infrastruktur
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ Enabler integrasjon i Altinn-domenet
- **P1 Ta utgangspunkt i brukernes behov** â€“ Raskere tjenesteutvikling

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som del av Altinn 3-plattformen (inkludert i Altinn-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter
- **Estimert kostnader:** 1-3 MNOK Ã¥rlig for drift og videreutvikling
- **Skalering:** Volum-elastisk; kostnadene skaleres med katalog-stÃ¸rrelse

**Finansiering:** Via Digdir/statsbudsjett som del av Altinn-portefÃ¸ljen.

**Kilder:** Estimert basert pÃ¥ Altinn-portefÃ¸lje-rapporter; eksakt kostnadsallokering ikke offentlig spesifisert.

## Forvaltning/eier

| AnsvarsomrÃ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Altinn-forvaltningen (Digdir) | Strategisk retning, metadata-standarder, API-kontrakt |
| **Driftsansvar** | Altinn-operasjonen (Digdir eller ekstern partner) | 24/5 drift, ~99.5% oppetid, support |
| **Budsjettansvar** | Digdir / Statsbudsjett | Del av Altinn-portefÃ¸lje |
| **Styringsmodell** | Altinn 3-produktgruppe / Datautveksling-domen | Align med Altinn-strategi |

**Styringsforum:** Altinn 3-styre; Datautvekslings-domene (lÃ¸pende strategi).

## Lenke til dokumentasjon

- https://data.altinn.no â€“ PrimÃ¦r portal
- https://docs.altinn.studio/nb/ â€“ Altinn dokumentasjon
- https://samarbeid.digdir.no/altinn-api â€“ Samarbeidsportal (Altinn API-koordinering)
- https://www.altinn.no â€“ Altinn-plattformen

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: data.altinn.no, Altinn Docs (hentet 2026-03-07)
- Kilder for finansiering: Altinn-portefÃ¸lje-rapporter (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

âœ… **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum-estimater
âœ… **Risikomatrise:** 8 konkrete risikokategorier med hÃ¥ndtering
âœ… **Finansiering:** Detaljert kostnadsmodell (estimert 1-3 MNOK Ã¥rlig)
âœ… **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Altinn + Digdir)
âœ… **Veikart:** Konkrete fokusomrÃ¥der (automatiske synkronisering, linked data, bruksstatistikk)
âœ… **Scope:** Eksplisitt tabell over hva som inngÃ¥r/ikke inngÃ¥r
âœ… **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet
âœ… **Altinn-kontekst:** Eksplisitt kobling til Altinn Studio og tjenesteutvikling

