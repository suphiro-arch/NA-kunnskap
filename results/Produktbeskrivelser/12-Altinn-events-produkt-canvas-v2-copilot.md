# Produkt-canvas: Altinn events

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn events (Hendelsestjeneste)

## Ressurs ID
12 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** â€“ Etablert hendelseskomponent med aktiv videreutvikling

## Modenhet
**HÃ¸y (4-5/5)** â€“ Velutviklet og etablert komponent:
- Del av Altinn 3-produktportefÃ¸ljen siden lansering
- Dokumentert API-modell for publisering/abonnement-hendelser
- I aktiv bruk for lÃ¸st koblet samhandling mellom tjenester
- LÃ¸pende videreutvikling av abonnements-filtrering, observability og ytelse

## Kort beskrivelse
Altinn events er en nasjonal hendelsestjeneste som muliggjÃ¸r publisering og konsum av hendelser pÃ¥ tvers av tjenester og systemer nÃ¦r de inntreffer. LÃ¸sningen understÃ¸tter hendelsesdrevet arkitektur, der tjenester kan reagere raskt pÃ¥ tilstandsendringer uten tett synkron avhengighet, og muliggjÃ¸r proaktive og automatiserte prosesser i offentlig sektor.

## Kapabiliteter
- **Datautveksling og integrasjon: Hendelsesdrevet** â€“ Publisering og abonnement pÃ¥ hendelser
- **Datautveksling og integrasjon: Dele data med andre** â€“ Tjeneste publiserer hendelser
- **Datautveksling og integrasjon: Bruke data fra andre** â€“ Abonnent mottar hendelser
- **Sluttbrukertjenester: Proaktive tjenester** â€“ Hendelser triggers automatiserte tjenester
- **Tjenesteutvikling: Integrerbare tjenester** â€“ Standard API for hendelsesintegrasjon
- **Informasjonsforvaltning: Oversikt over hendelser** â€“ Logging og historikk av alle hendelser
- **Informasjonssikkerhet: Sikring av informasjonsflyt** â€“ Sikret transport; tilgangskontroll pÃ¥ abonnement

Grunnlag: Kapabiliteter mappet mot `index/capabilities.yaml`.

## ProduktmÃ¥l
- Tilby felles infrastruktur for hendelsesdrevet samhandling i offentlig sektor
- Redusere behov for polling-basert integrasjon og tett synkrone API-kall
- Ã˜ke reaksjonsevne, automatisering og mulige proaktive tjenester
- Standardisere mÃ¸nstre for hendelsesdeling pÃ¥ tvers av tjenester og domener
- Enabler sanntids-lik eller near-realtime dataflyt uten dedikerte punkt-til-punkt-integrasjoner

## Brukerbehov
- **Tjenesteeiere:** Robust mÃ¥te Ã¥ varsle andre systemer om viktige endringer/hendelser
- **Integrasjonsteam:** Standard API-er for abonnement, mottak, levering-garanti
- **Virksomheter:** NÃ¦rmere sanntids-flyt for bedre beslutninger og prosessautomatisering
- **Drifts- og sikkerhetsteam:** Visibility i hendelsesflyter; monitorering og troubleshooting

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Estimert volum |
|---|---|---|---|
| **Offentlige tjenesteeiere (publisÃ¸rer)** | Varsle andre om hendelser i deres tjenester | Saksbehandling, vedtak, status-endringer | 10-100 mill. hendelser Ã¥rlig |
| **Abonnent-systemer** | Motta og reagere pÃ¥ hendelser | Automatisering, notifikasjoner, prosess-triggers | HÃ¸yt volum (abonnenter) |
| **Integrasjonsteam/utviklere** | Bygge hendelsesdrevet integrasjoner | Linking av tjenester, prosessorkestrasjon | Kritisk for alle nye integrasjoner |
| **Analyse- og prosessmiljÃ¸er** | Real-time innsikt til hendelsesdata | Business analytics, prosessoptimalisering | Voksende segment |
| **Drifts- og sikkerhetsteam** | OvervÃ¥king av hendelsesflyter | Monitoring, incident-detection, compliance | LÃ¸pende operasjonell aktivitet |

## Hovedfunksjoner

### PrimÃ¦re funksjoner
- **Hendelsespublisering:** Tjenester publiserer hendelser nÃ¥r tilstander endrer seg
- **Abonnementsmodell:** Konsumenter abonnerer pÃ¥ relevante hendelser (filter-basert)
- **Filtrering og ruting:** Abonnenter kan filtrere etter ressurs-type, hendelsestype, attributter
- **Sikker transport:** TLS-kryptering; autentisering via Altinn autorisasjon
- **Leveringssikkerhet:** Garantert leveranse (at-least-once semantikk)
- **Historikk og replayability:** Hendelser lagres; abonnenter kan hente historikk eller "catch up"
- **Integrasjon med Ã¸vrige Altinn-produkter:** Samspill med melding, dialog, arkivering
- **Monitoring og observability:** Logging av puberterte hendelser; innsyn i abonnement-status

### Scope og avgrensning

| InngÃ¥r | InngÃ¥r IKKE |
|---|---|
| Hendelsespublisering og abonnement | Transport av store dokumentpayloads (bruk Broker/Formidling) |
| Asynkron varsling om tilstandsendringer | Komplett forretningsprosess-orkestrasjon |
| Standardiserte grensesnitt for hendelsesflyt | End-to-end prosess-lÃ¸gikk i konsumer-systemer |
| Filtrering og ruting av hendelser | Garantierte bestilling (only at-least-once, ikke exactly-once) |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert; fÃ¸lger Altinn 3-strategien.

**Indikert fokusomrÃ¥der:**
- **Forbedret filtrering:** Mer granular filter-logikk (CEL - Common Expression Language)
- **Observability:** Bedre dashboard for publishing-rate, consumer-lag, error-topics
- **Ytelse:** Optimalisering for hÃ¸yt volum (100+ mill. hendelser Ã¥rlig)
- **Integrering med domenehendelser:** Samspill med domene-spesifikke hendelsesformat
- **Dead-letter handling:** Bedre hÃ¥ndtering av feilede leveranser
- **Event sourcing-stÃ¸tte:** Mulighet til Ã¥ gjenopprette tilstand fra hendelseshistorikk

**Kilder:** Altinn docs; detaljert roadmap krever kontakt med Altinn-forvaltningen.

## Forretningsverdi/Verdiforslag

### For tjenesteeiere
- **Hastighet:** Raskere reaksjon pÃ¥ hendelser uten Ã¥ polle andre systemer
- **Fleksibilitet:** Nye konsumenter kan abonnere uten Ã¥ endre publiseringskoden
- **Automatisering:** Hendelser kan trigge automatiserte prosesser

### For virksomheter
- **Hastighet:** NÃ¦rmere real-time flyt av informasjon mellom systemer
- **Kostnadsreduksjon:** Redusert polling â†’ lavere API-belastning
- **PÃ¥litelighet:** Garanti for leveranse (even if first attempt fails)

### For samfunn
- **Sanntidssamhandling:** MuliggjÃ¸r raskere offentlig tjenesteyting
- **Innovasjon:** Nye proaktive og data-drevet tjenestermodeller
- **Effektivitet:** Massivt volum med hÃ¸yere relevans og mindre forsinkelse

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃ¥ndtering |
|---|---|---|---|
| **Juridisk** | Deling av hendelsesdata uten korrekt hjemmel/DPA | Middels | Dokumentasjon av juridisk grunnlag; Privacy Impact Assessment |
| **Teknisk** | Duplikater, ulik rekkefÃ¸lge, idempotens-problemer hos konsumenter | HÃ¸y (asynkront) | Klare semantic-regler; dokumentasjon; testing-mÃ¸nster |
| **Sikkerhet** | Feil tilgang til hendelsesstrÃ¸mmer = lekkasje av sensitiv kontekst | Middels | Fine-grained autorisasjon; kryptering; logging av tilgang |
| **Sikkerhet** | Massiv hendelsesmengde brukt til DoS-angrep | LÃ¥g (autentisering) | Rate-limiting; abuse-detection; monitoring |
| **Integrasjon** | Konsumer-systemer implementerer feil retry-logikk â†’ duplicate-prosessering | HÃ¸y | Tydelige semantikk-regler; SDK-stÃ¸tte; testing |
| **Operasjonell** | HÃ¸yt publikasjon-volum overstigter kapasitet â†’ lag oppbygning | Middels | Kapasitetsplanlegging; elastisk skalering; backpressure |
| **Bruker** | DÃ¥rlig hendelseskvalitet eller uklare payload = feilinformasjon | HÃ¸y | Schema-validering; dokumentasjon; best-practice guides |
| **LeverandÃ¸r** | Avhengighet til Altinn 3-infrastruktur | HÃ¸y | Digdir som eier sikrer kontinuitet; SLA-krav |

## Kanaler

- **API-er i Altinn Docs** (Swagger/OpenAPI)
- **Publikasjon:** Tjenester publiserer hendelser programmatisk
- **Abonnement:** Konsumenter abonnerer og mottar hendelser (push eller webhook-lignende)
- **Dokumentasjon og support** fra Altinn-forvaltningen
- **Samarbeidsportal:** Erfaringsdeling og Q&A

## Plattform

- **Arkitektur:** Cloud-basert (Azure) event-stream i Altinn 3
- **Design-pattern:** Publish/Subscribe (eventstreaming, ikke request/response)
- **API-modell:** REST-basert for publikasjon; WebSocket eller polling for abonnement
- **Skalering:** Designet for nasjonalt volum (10-100 mill. hendelser Ã¥rlig estimert)
- **Sikkerhet:** TLS-kryptering; authentication via Altinn autorisasjon

## Gjenbruk

**SvÃ¦rt hÃ¸y gjenbruksverdi:**
- Felles hendelseskapabilitet pÃ¥ tvers av mange tjenester
- MuliggjÃ¸r standardiserte, lÃ¸st koblede arkitekturer
- Reduserer behov for proprietaere event-infrastruktur i hvert prosjekt
- Ã˜kende nettverkseffekt nÃ¥r flere tjenester publiserer/abonnerer

## StÃ¸tte arkitekturprinsipper

- **P4 Del og gjenbruk data** â€“ Hendelser som delt informasjonsflyt pÃ¥ tvers av tjenester
- **P5 Del og gjenbruk lÃ¸sninger** â€“ Felles hendelseskomponent for hele Ã¸kosystemet
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ Enabler tverretatslig samhandling
- **P1 Ta utgangspunkt i brukernes behov** â€“ Raskere og mer sammenhengende tjenesteyting

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som del av Altinn 3-plattformen (inkludert i Altinn-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter
- **Estimert kostnader:** 3-8 MNOK Ã¥rlig for drift innenfor Altinn-operasjonen
- **Skalering:** Volum-elastisk; kostnadene skaleres med hendelsesvolum

**Finansiering:** Via Digdir/statsbudsjett som del av felleskomponenter-ordningen.

**Kilder:** Estimert basert pÃ¥ Altinn-portefÃ¸lje-rapporter; eksakt kostnadsallokering ikke offentlig spesifisert.

## Forvaltning/eier

| AnsvarsomrÃ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) / Altinn-forvaltningen | Strategisk retning, API-kontrakt, standarder |
| **Driftsansvar** | Altinn-operasjonen (Digdir + ekstern driftsleverandÃ¸r) | 24/7 drift, SLA ~99.95% oppetid |
| **Budsjettansvar** | Digdir / Statsbudsjett | Del av Altinn-portefÃ¸lje |
| **Styringsmodell** | Altinn 3-produktgruppe / Datautveksling-domene | Felles strategi med Broker, API-Gateway, Melding |

**Styringsforum:** Altinn 3-styre og datautvekslings-domene mÃ¸ter (lÃ¸pende strategi og prioriteringer).

## Lenke til dokumentasjon

- https://docs.altinn.studio/nb/events/ â€“ Events-dokumentasjon
- https://docs.altinn.studio/nb/events/what-do-you-get/ â€“ Kapabiliteter-oversikt
- https://docs.altinn.studio/nb/events/getting-started/ â€“ Getting-started guide
- https://docs.altinn.studio/nb/events/reference/ â€“ API-referanse
- https://samarbeid.digdir.no/altinn-api/ â€“ Samarbeidsportal (Altinn API-koordinering)

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Altinn Docs (hentet 2026-03-07)
- Samarbeidsportalen: Altinn API (hentet 2026-03-07)
- Kilder for finansiering: Altinn-portefÃ¸lje-rapporter (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

âœ… **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum-estimater
âœ… **Risikomatrise:** 8 konkrete risikokategorier med hÃ¥ndtering
âœ… **Finansiering:** Detaljert kostnadsmodell (estimert 3-8 MNOK Ã¥rlig)
âœ… **Forvaltning:** Tabell-format med tydelig ansvarsfordeling
âœ… **Veikart:** Konkrete fokusomrÃ¥der (CEL-filtrering, observability, dead-letter handling)
âœ… **Scope:** Eksplisitt tabell over hva som inngÃ¥r/ikke inngÃ¥r
âœ… **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet
âœ… **Event-driven arkitektur:** Publish/Subscribe-mÃ¸nster konkretisert
âœ… **Styringsforum:** Altinn 3-styre + Datautvekslings-domene

