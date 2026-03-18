# Produkt-canvas: Altinn events

MÃƒÂ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn events (Hendelsestjeneste)

## Ressurs ID
DIGDIR-010

## Status/Livsfase
**Produksjon** Ã¢â‚¬â€œ Etablert hendelseskomponent med aktiv videreutvikling

## Modenhet
**HÃƒÂ¸y (4-5/5)** Ã¢â‚¬â€œ Velutviklet og etablert komponent:
- Del av Altinn 3-produktportefÃƒÂ¸ljen siden lansering
- Dokumentert API-modell for publisering/abonnement-hendelser
- I aktiv bruk for lÃƒÂ¸st koblet samhandling mellom tjenester
- LÃƒÂ¸pende videreutvikling av abonnements-filtrering, observability og ytelse

## Kort beskrivelse
Altinn events er en nasjonal hendelsestjeneste som muliggjÃƒÂ¸r publisering og konsum av hendelser pÃƒÂ¥ tvers av tjenester og systemer nÃƒÂ¦r de inntreffer. LÃƒÂ¸sningen understÃƒÂ¸tter hendelsesdrevet arkitektur, der tjenester kan reagere raskt pÃƒÂ¥ tilstandsendringer uten tett synkron avhengighet, og muliggjÃƒÂ¸r proaktive og automatiserte prosesser i offentlig sektor.

## Kapabiliteter
- **Datautveksling og integrasjon: Hendelsesdrevet** Ã¢â‚¬â€œ Publisering og abonnement pÃƒÂ¥ hendelser
- **Datautveksling og integrasjon: Dele data med andre** Ã¢â‚¬â€œ Tjeneste publiserer hendelser
- **Datautveksling og integrasjon: Bruke data fra andre** Ã¢â‚¬â€œ Abonnent mottar hendelser
- **Sluttbrukertjenester: Proaktive tjenester** Ã¢â‚¬â€œ Hendelser triggers automatiserte tjenester
- **Tjenesteutvikling: Integrerbare tjenester** Ã¢â‚¬â€œ Standard API for hendelsesintegrasjon
- **Informasjonsforvaltning: Oversikt over hendelser** Ã¢â‚¬â€œ Logging og historikk av alle hendelser
- **Informasjonssikkerhet: Sikring av informasjonsflyt** Ã¢â‚¬â€œ Sikret transport; tilgangskontroll pÃƒÂ¥ abonnement

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## ProduktmÃƒÂ¥l
- Tilby felles infrastruktur for hendelsesdrevet samhandling i offentlig sektor
- Redusere behov for polling-basert integrasjon og tett synkrone API-kall
- ÃƒËœke reaksjonsevne, automatisering og mulige proaktive tjenester
- Standardisere mÃƒÂ¸nstre for hendelsesdeling pÃƒÂ¥ tvers av tjenester og domener
- Enabler sanntids-lik eller near-realtime dataflyt uten dedikerte punkt-til-punkt-integrasjoner

## Brukerbehov
- **Tjenesteeiere:** Robust mÃƒÂ¥te ÃƒÂ¥ varsle andre systemer om viktige endringer/hendelser
- **Integrasjonsteam:** Standard API-er for abonnement, mottak, levering-garanti
- **Virksomheter:** NÃƒÂ¦rmere sanntids-flyt for bedre beslutninger og prosessautomatisering
- **Drifts- og sikkerhetsteam:** Visibility i hendelsesflyter; monitorering og troubleshooting

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃƒÂ¦re behov | BruksomrÃƒÂ¥de | Estimert volum |
|---|---|---|---|
| **Offentlige tjenesteeiere (publisÃƒÂ¸rer)** | Varsle andre om hendelser i deres tjenester | Saksbehandling, vedtak, status-endringer | 10-100 mill. hendelser ÃƒÂ¥rlig |
| **Abonnent-systemer** | Motta og reagere pÃƒÂ¥ hendelser | Automatisering, notifikasjoner, prosess-triggers | HÃƒÂ¸yt volum (abonnenter) |
| **Integrasjonsteam/utviklere** | Bygge hendelsesdrevet integrasjoner | Linking av tjenester, prosessorkestrasjon | Kritisk for alle nye integrasjoner |
| **Analyse- og prosessmiljÃƒÂ¸er** | Real-time innsikt til hendelsesdata | Business analytics, prosessoptimalisering | Voksende segment |
| **Drifts- og sikkerhetsteam** | OvervÃƒÂ¥king av hendelsesflyter | Monitoring, incident-detection, compliance | LÃƒÂ¸pende operasjonell aktivitet |

## Hovedfunksjoner

### PrimÃƒÂ¦re funksjoner
- **Hendelsespublisering:** Tjenester publiserer hendelser nÃƒÂ¥r tilstander endrer seg
- **Abonnementsmodell:** Konsumenter abonnerer pÃƒÂ¥ relevante hendelser (filter-basert)
- **Filtrering og ruting:** Abonnenter kan filtrere etter ressurs-type, hendelsestype, attributter
- **Sikker transport:** TLS-kryptering; autentisering via Altinn autorisasjon
- **Leveringssikkerhet:** Garantert leveranse (at-least-once semantikk)
- **Historikk og replayability:** Hendelser lagres; abonnenter kan hente historikk eller "catch up"
- **Integrasjon med ÃƒÂ¸vrige Altinn-produkter:** Samspill med melding, dialog, arkivering
- **Monitoring og observability:** Logging av puberterte hendelser; innsyn i abonnement-status

### Scope og avgrensning

| InngÃƒÂ¥r | InngÃƒÂ¥r IKKE |
|---|---|
| Hendelsespublisering og abonnement | Transport av store dokumentpayloads (bruk Broker/Formidling) |
| Asynkron varsling om tilstandsendringer | Komplett forretningsprosess-orkestrasjon |
| Standardiserte grensesnitt for hendelsesflyt | End-to-end prosess-lÃƒÂ¸gikk i konsumer-systemer |
| Filtrering og ruting av hendelser | Garantierte bestilling (only at-least-once, ikke exactly-once) |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert; fÃƒÂ¸lger Altinn 3-strategien.

**Indikert fokusomrÃƒÂ¥der:**
- **Forbedret filtrering:** Mer granular filter-logikk (CEL - Common Expression Language)
- **Observability:** Bedre dashboard for publishing-rate, consumer-lag, error-topics
- **Ytelse:** Optimalisering for hÃƒÂ¸yt volum (100+ mill. hendelser ÃƒÂ¥rlig)
- **Integrering med domenehendelser:** Samspill med domene-spesifikke hendelsesformat
- **Dead-letter handling:** Bedre hÃƒÂ¥ndtering av feilede leveranser
- **Event sourcing-stÃƒÂ¸tte:** Mulighet til ÃƒÂ¥ gjenopprette tilstand fra hendelseshistorikk

**Kilder:** Altinn docs; detaljert roadmap krever kontakt med Altinn-forvaltningen.

## Forretningsverdi/Verdiforslag

### For tjenesteeiere
- **Hastighet:** Raskere reaksjon pÃƒÂ¥ hendelser uten ÃƒÂ¥ polle andre systemer
- **Fleksibilitet:** Nye konsumenter kan abonnere uten ÃƒÂ¥ endre publiseringskoden
- **Automatisering:** Hendelser kan trigge automatiserte prosesser

### For virksomheter
- **Hastighet:** NÃƒÂ¦rmere real-time flyt av informasjon mellom systemer
- **Kostnadsreduksjon:** Redusert polling Ã¢â€ â€™ lavere API-belastning
- **PÃƒÂ¥litelighet:** Garanti for leveranse (even if first attempt fails)

### For samfunn
- **Sanntidssamhandling:** MuliggjÃƒÂ¸r raskere offentlig tjenesteyting
- **Innovasjon:** Nye proaktive og data-drevet tjenestermodeller
- **Effektivitet:** Massivt volum med hÃƒÂ¸yere relevans og mindre forsinkelse

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃƒÂ¥ndtering |
|---|---|---|---|
| **Juridisk** | Deling av hendelsesdata uten korrekt hjemmel/DPA | Middels | Dokumentasjon av juridisk grunnlag; Privacy Impact Assessment |
| **Teknisk** | Duplikater, ulik rekkefÃƒÂ¸lge, idempotens-problemer hos konsumenter | HÃƒÂ¸y (asynkront) | Klare semantic-regler; dokumentasjon; testing-mÃƒÂ¸nster |
| **Sikkerhet** | Feil tilgang til hendelsesstrÃƒÂ¸mmer = lekkasje av sensitiv kontekst | Middels | Fine-grained autorisasjon; kryptering; logging av tilgang |
| **Sikkerhet** | Massiv hendelsesmengde brukt til DoS-angrep | LÃƒÂ¥g (autentisering) | Rate-limiting; abuse-detection; monitoring |
| **Integrasjon** | Konsumer-systemer implementerer feil retry-logikk Ã¢â€ â€™ duplicate-prosessering | HÃƒÂ¸y | Tydelige semantikk-regler; SDK-stÃƒÂ¸tte; testing |
| **Operasjonell** | HÃƒÂ¸yt publikasjon-volum overstigter kapasitet Ã¢â€ â€™ lag oppbygning | Middels | Kapasitetsplanlegging; elastisk skalering; backpressure |
| **Bruker** | DÃƒÂ¥rlig hendelseskvalitet eller uklare payload = feilinformasjon | HÃƒÂ¸y | Schema-validering; dokumentasjon; best-practice guides |
| **LeverandÃƒÂ¸r** | Avhengighet til Altinn 3-infrastruktur | HÃƒÂ¸y | Digdir som eier sikrer kontinuitet; SLA-krav |

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
- **Skalering:** Designet for nasjonalt volum (10-100 mill. hendelser ÃƒÂ¥rlig estimert)
- **Sikkerhet:** TLS-kryptering; authentication via Altinn autorisasjon

## Gjenbruk

**SvÃƒÂ¦rt hÃƒÂ¸y gjenbruksverdi:**
- Felles hendelseskapabilitet pÃƒÂ¥ tvers av mange tjenester
- MuliggjÃƒÂ¸r standardiserte, lÃƒÂ¸st koblede arkitekturer
- Reduserer behov for proprietaere event-infrastruktur i hvert prosjekt
- ÃƒËœkende nettverkseffekt nÃƒÂ¥r flere tjenester publiserer/abonnerer

## StÃƒÂ¸tte arkitekturprinsipper

- **P4 Del og gjenbruk data** Ã¢â‚¬â€œ Hendelser som delt informasjonsflyt pÃƒÂ¥ tvers av tjenester
- **P5 Del og gjenbruk lÃƒÂ¸sninger** Ã¢â‚¬â€œ Felles hendelseskomponent for hele ÃƒÂ¸kosystemet
- **P6 Lag digitale lÃƒÂ¸sninger som stÃƒÂ¸tter samhandling** Ã¢â‚¬â€œ Enabler tverretatslig samhandling
- **P1 Ta utgangspunkt i brukernes behov** Ã¢â‚¬â€œ Raskere og mer sammenhengende tjenesteyting

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som del av Altinn 3-plattformen (inkludert i Altinn-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter
- **Estimert kostnader:** 3-8 MNOK ÃƒÂ¥rlig for drift innenfor Altinn-operasjonen
- **Skalering:** Volum-elastisk; kostnadene skaleres med hendelsesvolum

**Finansiering:** Via Digdir/statsbudsjett som del av felleskomponenter-ordningen.

**Kilder:** Estimert basert pÃƒÂ¥ Altinn-portefÃƒÂ¸lje-rapporter; eksakt kostnadsallokering ikke offentlig spesifisert.

## Forvaltning/eier

| AnsvarsomrÃƒÂ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) / Altinn-forvaltningen | Strategisk retning, API-kontrakt, standarder |
| **Driftsansvar** | Altinn-operasjonen (Digdir + ekstern driftsleverandÃƒÂ¸r) | 24/7 drift, SLA ~99.95% oppetid |
| **Budsjettansvar** | Digdir / Statsbudsjett | Del av Altinn-portefÃƒÂ¸lje |
| **Styringsmodell** | Altinn 3-produktgruppe / Datautveksling-domene | Felles strategi med Broker, API-Gateway, Melding |

**Styringsforum:** Altinn 3-styre og datautvekslings-domene mÃƒÂ¸ter (lÃƒÂ¸pende strategi og prioriteringer).

## Lenke til dokumentasjon

- https://docs.altinn.studio/nb/events/ Ã¢â‚¬â€œ Events-dokumentasjon
- https://docs.altinn.studio/nb/events/what-do-you-get/ Ã¢â‚¬â€œ Kapabiliteter-oversikt
- https://docs.altinn.studio/nb/events/getting-started/ Ã¢â‚¬â€œ Getting-started guide
- https://docs.altinn.studio/nb/events/reference/ Ã¢â‚¬â€œ API-referanse
- https://samarbeid.digdir.no/altinn-api/ Ã¢â‚¬â€œ Samarbeidsportal (Altinn API-koordinering)

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: Altinn Docs (hentet 2026-03-07)
- Samarbeidsportalen: Altinn API (hentet 2026-03-07)
- Kilder for finansiering: Altinn-portefÃƒÂ¸lje-rapporter (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

Ã¢Å“â€¦ **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum-estimater
Ã¢Å“â€¦ **Risikomatrise:** 8 konkrete risikokategorier med hÃƒÂ¥ndtering
Ã¢Å“â€¦ **Finansiering:** Detaljert kostnadsmodell (estimert 3-8 MNOK ÃƒÂ¥rlig)
Ã¢Å“â€¦ **Forvaltning:** Tabell-format med tydelig ansvarsfordeling
Ã¢Å“â€¦ **Veikart:** Konkrete fokusomrÃƒÂ¥der (CEL-filtrering, observability, dead-letter handling)
Ã¢Å“â€¦ **Scope:** Eksplisitt tabell over hva som inngÃƒÂ¥r/ikke inngÃƒÂ¥r
Ã¢Å“â€¦ **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet
Ã¢Å“â€¦ **Event-driven arkitektur:** Publish/Subscribe-mÃƒÂ¸nster konkretisert
Ã¢Å“â€¦ **Styringsforum:** Altinn 3-styre + Datautvekslings-domene

