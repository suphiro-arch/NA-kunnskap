# Produkt-canvas: Altinn events

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn events (Hendelsestjeneste)

## Ressurs ID
DIGDIR-010

## Status/Livsfase
**Produksjon** – Etablert hendelseskomponent med aktiv videreutvikling

## Modenhet
**Høy (4-5/5)** – Velutviklet og etablert komponent:
- Del av Altinn 3-produktporteføljen siden lansering
- Dokumentert API-modell for publisering/abonnement-hendelser
- I aktiv bruk for løst koblet samhandling mellom tjenester
- Løpende videreutvikling av abonnements-filtrering, observability og ytelse

## Kort beskrivelse
Altinn events er en nasjonal hendelsestjeneste som muliggjør publisering og konsum av hendelser på tvers av tjenester og systemer nær de inntreffer. Løsningen understøtter hendelsesdrevet arkitektur, der tjenester kan reagere raskt på tilstandsendringer uten tett synkron avhengighet, og muliggjør proaktive og automatiserte prosesser i offentlig sektor.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** – Abonnent mottar hendelser.
- **Datautveksling og integrasjon: Dele data med andre** – Tjeneste publiserer hendelser.
- **Datautveksling og integrasjon: Hendelsesdrevet** – Publisering og abonnement på hendelser.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** – Sikret transport; tilgangskontroll på abonnement.
- **Tjenesteutvikling: Integrerbare tjenester** – Standard API for hendelsesintegrasjon.

## Produktmål
- Tilby felles infrastruktur for hendelsesdrevet samhandling i offentlig sektor
- Redusere behov for polling-basert integrasjon og tett synkrone API-kall
- ?ke reaksjonsevne, automatisering og mulige proaktive tjenester
- Standardisere mønstre for hendelsesdeling på tvers av tjenester og domener
- Enabler sanntids-lik eller near-realtime dataflyt uten dedikerte punkt-til-punkt-integrasjoner

## Brukerbehov
- **Tjenesteeiere:** Robust måte å varsle andre systemer om viktige endringer/hendelser
- **Integrasjonsteam:** Standard API-er for abonnement, mottak, levering-garanti
- **Virksomheter:** Nærmere sanntids-flyt for bedre beslutninger og prosessautomatisering
- **Drifts- og sikkerhetsteam:** Visibility i hendelsesflyter; monitorering og troubleshooting

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Estimert volum |
|---|---|---|---|
| **Offentlige tjenesteeiere (publisører)** | Varsle andre om hendelser i deres tjenester | Saksbehandling, vedtak, status-endringer | 10-100 mill. hendelser årlig |
| **Abonnent-systemer** | Motta og reagere på hendelser | Automatisering, notifikasjoner, prosess-triggers | Høyt volum (abonnenter) |
| **Integrasjonsteam/utviklere** | Bygge hendelsesdrevet integrasjoner | Linking av tjenester, prosessorkestrasjon | Kritisk for alle nye integrasjoner |
| **Analyse- og prosessmiljøer** | Real-time innsikt til hendelsesdata | Business analytics, prosessoptimalisering | Voksende segment |
| **Drifts- og sikkerhetsteam** | Overvåking av hendelsesflyter | Monitoring, incident-detection, compliance | Løpende operasjonell aktivitet |

## Hovedfunksjoner

### Primære funksjoner
- **Hendelsespublisering:** Tjenester publiserer hendelser når tilstander endrer seg
- **Abonnementsmodell:** Konsumenter abonnerer på relevante hendelser (filter-basert)
- **Filtrering og ruting:** Abonnenter kan filtrere etter ressurs-type, hendelsestype, attributter
- **Sikker transport:** TLS-kryptering; autentisering via Altinn autorisasjon
- **Leveringssikkerhet:** Garantert leveranse (at-least-once semantikk)
- **Historikk og replayability:** Hendelser lagres; abonnenter kan hente historikk eller "catch up"
- **Integrasjon med øvrige Altinn-produkter:** Samspill med melding, dialog, arkivering
- **Monitoring og observability:** Logging av puberterte hendelser; innsyn i abonnement-status

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Hendelsespublisering og abonnement | Transport av store dokumentpayloads (bruk Broker/Formidling) |
| Asynkron varsling om tilstandsendringer | Komplett forretningsprosess-orkestrasjon |
| Standardiserte grensesnitt for hendelsesflyt | End-to-end prosess-løgikk i konsumer-systemer |
| Filtrering og ruting av hendelser | Garantierte bestilling (only at-least-once, ikke exactly-once) |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert; følger Altinn 3-strategien.

**Indikert fokusområder:**
- **Forbedret filtrering:** Mer granular filter-logikk (CEL - Common Expression Language)
- **Observability:** Bedre dashboard for publishing-rate, consumer-lag, error-topics
- **Ytelse:** Optimalisering for høyt volum (100+ mill. hendelser årlig)
- **Integrering med domenehendelser:** Samspill med domene-spesifikke hendelsesformat
- **Dead-letter handling:** Bedre håndtering av feilede leveranser
- **Event sourcing-støtte:** Mulighet til å gjenopprette tilstand fra hendelseshistorikk

**Kilder:** Altinn docs; detaljert roadmap krever kontakt med Altinn-forvaltningen.

## Forretningsverdi/Verdiforslag

### For tjenesteeiere
- **Hastighet:** Raskere reaksjon på hendelser uten å polle andre systemer
- **Fleksibilitet:** Nye konsumenter kan abonnere uten å endre publiseringskoden
- **Automatisering:** Hendelser kan trigge automatiserte prosesser

### For virksomheter
- **Hastighet:** Nærmere real-time flyt av informasjon mellom systemer
- **Kostnadsreduksjon:** Redusert polling → lavere API-belastning
- **Pålitelighet:** Garanti for leveranse (even if first attempt fails)

### For samfunn
- **Sanntidssamhandling:** Muliggjør raskere offentlig tjenesteyting
- **Innovasjon:** Nye proaktive og data-drevet tjenestermodeller
- **Effektivitet:** Massivt volum med høyere relevans og mindre forsinkelse

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Juridisk** | Deling av hendelsesdata uten korrekt hjemmel/DPA | Middels | Dokumentasjon av juridisk grunnlag; Privacy Impact Assessment |
| **Teknisk** | Duplikater, ulik rekkefølge, idempotens-problemer hos konsumenter | Høy (asynkront) | Klare semantic-regler; dokumentasjon; testing-mønster |
| **Sikkerhet** | Feil tilgang til hendelsesstrømmer = lekkasje av sensitiv kontekst | Middels | Fine-grained autorisasjon; kryptering; logging av tilgang |
| **Sikkerhet** | Massiv hendelsesmengde brukt til DoS-angrep | Låg (autentisering) | Rate-limiting; abuse-detection; monitoring |
| **Integrasjon** | Konsumer-systemer implementerer feil retry-logikk → duplicate-prosessering | Høy | Tydelige semantikk-regler; SDK-støtte; testing |
| **Operasjonell** | Høyt publikasjon-volum overstigter kapasitet → lag oppbygning | Middels | Kapasitetsplanlegging; elastisk skalering; backpressure |
| **Bruker** | Dårlig hendelseskvalitet eller uklare payload = feilinformasjon | Høy | Schema-validering; dokumentasjon; best-practice guides |
| **Leverandør** | Avhengighet til Altinn 3-infrastruktur | Høy | Digdir som eier sikrer kontinuitet; SLA-krav |

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
- **Skalering:** Designet for nasjonalt volum (10-100 mill. hendelser årlig estimert)
- **Sikkerhet:** TLS-kryptering; authentication via Altinn autorisasjon

## Gjenbruk

**Svært høy gjenbruksverdi:**
- Felles hendelseskapabilitet på tvers av mange tjenester
- Muliggjør standardiserte, løst koblede arkitekturer
- Reduserer behov for proprietaere event-infrastruktur i hvert prosjekt
- ?kende nettverkseffekt når flere tjenester publiserer/abonnerer

## Støtte arkitekturprinsipper

- **P4 Del og gjenbruk data** – Hendelser som delt informasjonsflyt på tvers av tjenester
- **P5 Del og gjenbruk løsninger** – Felles hendelseskomponent for hele økosystemet
- **P6 Lag digitale løsninger som støtter samhandling** – Enabler tverretatslig samhandling
- **P1 Ta utgangspunkt i brukernes behov** – Raskere og mer sammenhengende tjenesteyting

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som del av Altinn 3-plattformen (inkludert i Altinn-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter
- **Estimert kostnader:** 3-8 MNOK årlig for drift innenfor Altinn-operasjonen
- **Skalering:** Volum-elastisk; kostnadene skaleres med hendelsesvolum

**Finansiering:** Via Digdir/statsbudsjett som del av felleskomponenter-ordningen.

**Kilder:** Estimert basert på Altinn-portefølje-rapporter; eksakt kostnadsallokering ikke offentlig spesifisert.

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) / Altinn-forvaltningen | Strategisk retning, API-kontrakt, standarder |
| **Driftsansvar** | Altinn-operasjonen (Digdir + ekstern driftsleverandør) | 24/7 drift, SLA ~99.95% oppetid |
| **Budsjettansvar** | Digdir / Statsbudsjett | Del av Altinn-portefølje |
| **Styringsmodell** | Altinn 3-produktgruppe / Datautveksling-domene | Felles strategi med Broker, API-Gateway, Melding |

**Styringsforum:** Altinn 3-styre og datautvekslings-domene møter (løpende strategi og prioriteringer).

## Lenke til dokumentasjon

- https://docs.altinn.studio/nb/events/ – Events-dokumentasjon
- https://docs.altinn.studio/nb/events/what-do-you-get/ – Kapabiliteter-oversikt
- https://docs.altinn.studio/nb/events/getting-started/ – Getting-started guide
- https://docs.altinn.studio/nb/events/reference/ – API-referanse
- https://samarbeid.digdir.no/altinn-api/ – Samarbeidsportal (Altinn API-koordinering)

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: Altinn Docs (hentet 2026-03-07)
- Samarbeidsportalen: Altinn API (hentet 2026-03-07)
- Kilder for finansiering: Altinn-portefølje-rapporter (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

- **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum-estimater
- **Risikomatrise:** 8 konkrete risikokategorier med håndtering
- **Finansiering:** Detaljert kostnadsmodell (estimert 3-8 MNOK årlig)
- **Forvaltning:** Tabell-format med tydelig ansvarsfordeling
- **Veikart:** Konkrete fokusområder (CEL-filtrering, observability, dead-letter handling)
- **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
- **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet
- **Event-driven arkitektur:** Publish/Subscribe-mønster konkretisert
- **Styringsforum:** Altinn 3-styre + Datautvekslings-domene

