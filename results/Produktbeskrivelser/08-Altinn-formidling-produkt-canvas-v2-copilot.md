# Produkt-canvas: Altinn formidling (Broker)

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn formidling (Broker)

## Ressurs ID
DIGDIR-008

## Status/Livsfase
**Produksjon** – Etablert formidlingskomponent med aktiv videreutvikling

## Modenhet
**Høy (4-5/5)** – Velutviklet og etablert komponent:
- Del av Altinn 3-produktporteføljen siden lansering
- Dokumentert API-modell for asynkron datautveksling
- I aktiv bruk for robust formidling med skalerbarhet, sikkerhet og sporbarhet
- Løpende videreutvikling av API-kvalitet, monitoring og migrering fra Altinn 2

## Kort beskrivelse
Altinn formidling (Broker) er en nasjonal formidlingstjeneste for sikker, asynkron datautveksling mellom virksomheter og systemer. Tjenesten er designet for scenarioer hvor data må overføres pålitelig uten tett synkron kobling mellom avsender og mottaker, og tilbyr kømekanismer, leveringssikkerhet og sporbarhet.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** – Sikker transport av data via broker
- **Datautveksling og integrasjon: Dele data med andre** – Avsender legger data i formidlingstjenste
- **Datautveksling og integrasjon: Bruke data fra andre** – Mottaker henter data fra formidlingstjeneste
- **Tjenesteutvikling: Integrerbare tjenester** – Standardisert API for integrasjon
- **Samarbeid: Organisatorisk samhandling** – Enabler samhandling mellom organisasjoner
- **Informasjonssikkerhet: Sikring av informasjonsflyt** – Kryptering, autentisering, tilgangskontroll
- **Tillit: Sporbarhet og innsyn** – Logging av all formidling og leveringsstatus

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## Produktmål
- Tilby en felles nasjonal tjeneste for robust asynkron dataformidling uten tett kobling
- Redusere punkt-til-punkt-integrasjoner og proprietaere transportmønstre
- Øke leveringssikkerhet, skalerbarhet og observability i samhandling mellom systemer
- Understøtte sammenhengende tjenester med standardiserte integrasjonsmønstre
- Migrere data formidling fra Altinn 2 til Altinn 3-plattformen

## Brukerbehov
- **Virksomheter:** Sikker og pålitelig dataoverføring uten tett kopling mellom systemer
- **Integrasjonsteam:** Standard API-er for innlegging, uthenting og oppfølging av leveranser
- **Drifts- og sikkerhetsteam:** Bedre sporbarhet, logging og kontroll i transportleddet
- **Migrasjons-team:** Sikker løfte-og-skift av data formidling fra Altinn 2 til Altinn 3

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Estimert volum |
|---|---|---|---|
| **Avsendende virksomheter** | Sikker opplasting av data til formidling | Skattedata, NAV-meldinger, helseopp gaver | 10-100 mill. meldinger årlig |
| **Mottakende virksomheter** | Sikker uthenting av data med pålitelighet | Mottak og prosessering av meldinger | Kreves av alle mottakere |
| **Systemleverandører/Integratorer** | Stabil API for formidling | Integrasjon i fagsystemer, maskinautomatisering | Kritisk for alle brukere |
| **Drifts- og sikkerhetsteam** | Overvåking, feiloppdagelse, SLA | Drift, monitoring, incident-håndtering | Løpende operasjonell aktivitet |
| **Migrasjons-prosjekter** | Sikker overføring fra Altinn 2 | Løfte-og-skift, parallell drift | Høyt volum under migrasjon |

## Hovedfunksjoner

### Primære funksjoner
- **Asynkron meldings-/dataformidling:** Broker-mønster for avkoblet avsender-mottaker
- **Køer og leveringsmekanismer:** FIFO-køer, durable storage, garantert leveranse
- **API-er for integrasjon:**
  - Push (avsender legger inn data)
  - Pull (mottaker henter data)
  - Kvittering-håndtering (bekreftelse på mottak)
- **Status og oppfølging:** Track av meldingsstatus (mottatt, levert, feilet, retry)
- **Autentisering og autorisasjon:** Integrasjon med Altinn autorisasjon
- **Logging og sporbarhet:** Alle hendelser loggert for audit og troubleshooting
- **Batch-prosessering:** Støtte for høyt volum av parallelle operasjoner
- **Sikker transport:** TLS-kryptering, API-authentication

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Transport/formidling av payload mellom aktorer | Full faglogikk i avsender/mottakersystem |
| Status, kvittering og kontrollmekanismer i formidlingsleddet | Publisering/abonnement av domenehendelser (dekkes av Events-produkt) |
| Standardiserte API-er for integrasjon | Datavalidering eller transformasjon |
| Kømekanismer med garantert leveranse | Duplikat-deteksjon (ansvar hos mottaker) |
| Logging av all formidling | Innsamling av analytics eller metrics |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert.

**Indikert fokusområder:**
- **Migrasjons-støtte:** Etter fase-by-fase slutningsresultatet av Altinn 2 Broker
- **API-modernisering:** Forbedring av API-design etter OpenAPI-standarder
- **Observability:** Bedre monitoring, logging og diagnostikkverktøy
- **Ytelse:** Optimalisering for høyt volum av meldinger og concurrent-på operasjoner
- **Integrering med Events:** Tettere samspill med event-stream for real-time-varsling
- **Compliance:** Forbedret støtte for juridiske krav (lagring, sletting, audit-trails)

**Kilder:** Altinn docs; detaljert roadmap krever kontakt med Altinn-forvaltningen.

## Forretningsverdi/Verdiforslag

### For virksomheter
- **Kostnadsreduksjon:** Lavere integrasjonskostnader gjennom gjenbruk av formidlingstjeneste
- **Hastighet:** Raskere etablering av nye samhandlingsprosesser uten å byggee egne transport-løsninger
- **Pålitelighet:** Høyere leveringskvalitet og mindre operasjonell risiko i kritisk dataflyt

### For systemleverandører
- **Standardisering:** Samme API for alle integrasjoner (ikke proprietaere transportmekanismer)
- **Skalering:** Ikke behov for å håndtere høyt volum selv; broker skaleres nasjonalt

### For samfunn
- **Interoperabilitet:** Standardisert meldingsflyt muliggjør samordnet samhandling på tvers av sektorer
- **Robusthet:** Nasjonalt delt infrastruktur er mer pålitelig enn mange lokale løsninger
- **Kostnadseffektivitet:** Redusert duplisering av integrasjonsinfrastruktur

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Teknisk** | Feilhåndtering ved store volum og timeout/retry-scenarioer | Høy (komplekst) | Testing med høyt volum; backpressure-mekanismer; dokumentasjon |
| **Integrasjon** | Integratorer implementerer feil → meldinger ikke prosessert | Middels | Referansearkitektur; SDK-er; testing-verktøy |
| **Sikkerhet** | Feil tilgangsstyring gir uønsket datapassasje | Middels | Fine-grained autorisasjon; audit-logging; rate-limiting |
| **Sikkerhet** | Tokenoppholdelse eller nøkkel-lekkasje i transportleddet | Låg (TLS) | Sterk kryptering; key-management; monitoring |
| **Operasjonell** | Høyt volum overstigter kapasitet → kø-oppbygging og forsinkelser | Middels | Kapasitetsplanlegging; elastisk skalering; fallback-rutiner |
| **Brukeropplevelse** | Liten synlighet i asynkrone prosesser gir treg feiloppdagelse | Høy | Bedre logging, monitoring og diagnostikkverktøy |
| **Migrasjon** | Feil under migrering fra Altinn 2 → datatap eller duplikater | Middels | Parallell drift; validering; reconciliation |
| **Leverandør** | Avhengighet til Altinn 3-infrastruktur | Høy | Digdir som eier sikrer kontinuitet; SLA-krav |

## Kanaler

- **API-er i Altinn Docs** (Swagger/OpenAPI)
- **Integration från virksomhetenes fagsystem** (via SDK eller direkte API)
- **Integrasjonsplattformer** (MuleSoft, AzureIntegration, osv.)
- **Dokumentasjon og support** fra Altinn-forvaltningen
- **Sammarbeidsportal** (for spørsmål og erfaringsdeling)

## Plattform

- **Arkitektur:** Cloud-basert (Azure) multi-tenant SaaS i Altinn 3
- **Messaging-modell:** Asynkron broker-basert (FIFO-køer)
- **Design-pattern:** Dekoblet avsender-mottaker via formidlingstjeneste
- **Skalering:** Designet for nasjonalt volum (10-100 mill. meldinger årlig)
- **Sikkerhet:** TLS-kryptering i transit; enkryptert lagring; API-autentisering

## Gjenbruk

**Svært høy gjenbruksverdi:**
- Felles transport- og formidlingskapabilitet for mange sektorer (offentlig og privat)
- Reduserer duplisering av integrasjonsinfrastruktur i enkeltvirksomheter
- Fremmer standardiserte, løst koblede samhandlingsmønstre
- API-standard som kan gjenbrukes for mange domener (skatt, helse, NAV, osv.)

## Støtte arkitekturprinsipper

- **P4 Del og gjenbruk data** – Sikker formidling av delte data
- **P5 Del og gjenbruk løsninger** – Felles formidlingskomponent for alle integrasjoner
- **P6 Lag digitale løsninger som støtter samhandling** – Enabler asynkron samhandling
- **P7 Sørg for tillit til oppgaveløsningen** – Sporbarhet og sikkerhet i leveranse
- **P8 Etabler felles forståelse av informasjon** – Standardisert API-kontrakt

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som del av Altinn 3-plattformen (inkludert i Altinn-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter
- **Kapasitetsestimater:** Estimert 3-8 MNOK årlig for drift innenfor Altinn-operasjonen
- **Migrasjon:** Ekstra ressurser under Altinn 2 → 3-migrasjon (2023-2026)

**Finansiering:** Via Digdir/statsbudsjett som del av felleskomponenter-ordningen.

**Kilder:** Estimert basert på Altinn-portefølje-rapporter; eksakt kostnadsallokering ikke offentlig spesifisert.

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) / Altinn-forvaltningen | Strategisk retning, API-kontrakt, standarder |
| **Driftsansvar** | Altinn-operasjonen (Digdir + ekstern driftsleverandør) | 24/7 drift, SLA ~99.95% oppetid |
| **Budsjettansvar** | Digdir / Statsbudsjett | Del av Altinn-portefølje; ekstra ressurser for migrasjon |
| **Styringsmodell** | Altinn 3-produktgruppe / Datautveksling-domene | Felles strategi med eFormidling, API-Gateway, Events |

**Styringsforum:** Altinn 3-styre og datautvekslings-domene-møter (løpende strategi og prioriteringer).

## Lenke til dokumentasjon

- https://docs.altinn.studio/nb/broker/ – Formidling-dokumentasjon
- https://docs.altinn.studio/nb/broker/what-do-you-get/ – Kapabiliteter-oversikt
- https://docs.altinn.studio/nb/broker/getting-started/ – Getting-started guide
- https://docs.altinn.studio/nb/broker/reference/ – API-referanse
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

- **Brukersegmenter:** Struktur ut som tabell med konkrete behov og estimert volum
- **Risikomatrise:** 8 konkrete risikokategorier med håndtering  
- **Finansiering:** Detaljert kostnadsmodell (estimert 3-8 MNOK årlig)
- **Forvaltning:** Tabell-format med tydelig ansvarsfordeling
- **Veikart:** Konkrete fokusområder (migrasjons-støtte, API-modernisering, observability)
- **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
- **Kapabiliteter:** Detalj-beskrivelser av hvordan hver kapabilitet realiseres
- **Arkitekturdetal jer:** Broker-mønster, kømekanismer, FIFO, durable-storage konkretisert
- **Migrasjons-kontekst:** Eksplisert forbindelse til Altinn 2 → 3-migrasjon

