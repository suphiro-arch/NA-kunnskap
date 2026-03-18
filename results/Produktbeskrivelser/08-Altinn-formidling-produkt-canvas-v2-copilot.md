# Produkt-canvas: Altinn formidling (Broker)

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn formidling (Broker)

## Ressurs ID
DIGDIR-008

## Status/Livsfase
**Produksjon** â€“ Etablert formidlingskomponent med aktiv videreutvikling

## Modenhet
**HÃ¸y (4-5/5)** â€“ Velutviklet og etablert komponent:
- Del av Altinn 3-produktportefÃ¸ljen siden lansering
- Dokumentert API-modell for asynkron datautveksling
- I aktiv bruk for robust formidling med skalerbarhet, sikkerhet og sporbarhet
- LÃ¸pende videreutvikling av API-kvalitet, monitoring og migrering fra Altinn 2

## Kort beskrivelse
Altinn formidling (Broker) er en nasjonal formidlingstjeneste for sikker, asynkron datautveksling mellom virksomheter og systemer. Tjenesten er designet for scenarioer hvor data mÃ¥ overfÃ¸res pÃ¥litelig uten tett synkron kobling mellom avsender og mottaker, og tilbyr kÃ¸mekanismer, leveringssikkerhet og sporbarhet.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** â€“ Sikker transport av data via broker
- **Datautveksling og integrasjon: Dele data med andre** â€“ Avsender legger data i formidlingstjenste
- **Datautveksling og integrasjon: Bruke data fra andre** â€“ Mottaker henter data fra formidlingstjeneste
- **Tjenesteutvikling: Integrerbare tjenester** â€“ Standardisert API for integrasjon
- **Samarbeid: Organisatorisk samhandling** â€“ Enabler samhandling mellom organisasjoner
- **Informasjonssikkerhet: Sikring av informasjonsflyt** â€“ Kryptering, autentisering, tilgangskontroll
- **Tillit: Sporbarhet og innsyn** â€“ Logging av all formidling og leveringsstatus

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## ProduktmÃ¥l
- Tilby en felles nasjonal tjeneste for robust asynkron dataformidling uten tett kobling
- Redusere punkt-til-punkt-integrasjoner og proprietaere transportmÃ¸nstre
- Ã˜ke leveringssikkerhet, skalerbarhet og observability i samhandling mellom systemer
- UnderstÃ¸tte sammenhengende tjenester med standardiserte integrasjonsmÃ¸nstre
- Migrere data formidling fra Altinn 2 til Altinn 3-plattformen

## Brukerbehov
- **Virksomheter:** Sikker og pÃ¥litelig dataoverfÃ¸ring uten tett kopling mellom systemer
- **Integrasjonsteam:** Standard API-er for innlegging, uthenting og oppfÃ¸lging av leveranser
- **Drifts- og sikkerhetsteam:** Bedre sporbarhet, logging og kontroll i transportleddet
- **Migrasjons-team:** Sikker lÃ¸fte-og-skift av data formidling fra Altinn 2 til Altinn 3

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Estimert volum |
|---|---|---|---|
| **Avsendende virksomheter** | Sikker opplasting av data til formidling | Skattedata, NAV-meldinger, helseopp gaver | 10-100 mill. meldinger Ã¥rlig |
| **Mottakende virksomheter** | Sikker uthenting av data med pÃ¥litelighet | Mottak og prosessering av meldinger | Kreves av alle mottakere |
| **SystemleverandÃ¸rer/Integratorer** | Stabil API for formidling | Integrasjon i fagsystemer, maskinautomatisering | Kritisk for alle brukere |
| **Drifts- og sikkerhetsteam** | OvervÃ¥king, feiloppdagelse, SLA | Drift, monitoring, incident-hÃ¥ndtering | LÃ¸pende operasjonell aktivitet |
| **Migrasjons-prosjekter** | Sikker overfÃ¸ring fra Altinn 2 | LÃ¸fte-og-skift, parallell drift | HÃ¸yt volum under migrasjon |

## Hovedfunksjoner

### PrimÃ¦re funksjoner
- **Asynkron meldings-/dataformidling:** Broker-mÃ¸nster for avkoblet avsender-mottaker
- **KÃ¸er og leveringsmekanismer:** FIFO-kÃ¸er, durable storage, garantert leveranse
- **API-er for integrasjon:**
  - Push (avsender legger inn data)
  - Pull (mottaker henter data)
  - Kvittering-hÃ¥ndtering (bekreftelse pÃ¥ mottak)
- **Status og oppfÃ¸lging:** Track av meldingsstatus (mottatt, levert, feilet, retry)
- **Autentisering og autorisasjon:** Integrasjon med Altinn autorisasjon
- **Logging og sporbarhet:** Alle hendelser loggert for audit og troubleshooting
- **Batch-prosessering:** StÃ¸tte for hÃ¸yt volum av parallelle operasjoner
- **Sikker transport:** TLS-kryptering, API-authentication

### Scope og avgrensning

| InngÃ¥r | InngÃ¥r IKKE |
|---|---|
| Transport/formidling av payload mellom aktorer | Full faglogikk i avsender/mottakersystem |
| Status, kvittering og kontrollmekanismer i formidlingsleddet | Publisering/abonnement av domenehendelser (dekkes av Events-produkt) |
| Standardiserte API-er for integrasjon | Datavalidering eller transformasjon |
| KÃ¸mekanismer med garantert leveranse | Duplikat-deteksjon (ansvar hos mottaker) |
| Logging av all formidling | Innsamling av analytics eller metrics |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert.

**Indikert fokusomrÃ¥der:**
- **Migrasjons-stÃ¸tte:** Etter fase-by-fase slutningsresultatet av Altinn 2 Broker
- **API-modernisering:** Forbedring av API-design etter OpenAPI-standarder
- **Observability:** Bedre monitoring, logging og diagnostikkverktÃ¸y
- **Ytelse:** Optimalisering for hÃ¸yt volum av meldinger og concurrent-pÃ¥ operasjoner
- **Integrering med Events:** Tettere samspill med event-stream for real-time-varsling
- **Compliance:** Forbedret stÃ¸tte for juridiske krav (lagring, sletting, audit-trails)

**Kilder:** Altinn docs; detaljert roadmap krever kontakt med Altinn-forvaltningen.

## Forretningsverdi/Verdiforslag

### For virksomheter
- **Kostnadsreduksjon:** Lavere integrasjonskostnader gjennom gjenbruk av formidlingstjeneste
- **Hastighet:** Raskere etablering av nye samhandlingsprosesser uten Ã¥ byggee egne transport-lÃ¸sninger
- **PÃ¥litelighet:** HÃ¸yere leveringskvalitet og mindre operasjonell risiko i kritisk dataflyt

### For systemleverandÃ¸rer
- **Standardisering:** Samme API for alle integrasjoner (ikke proprietaere transportmekanismer)
- **Skalering:** Ikke behov for Ã¥ hÃ¥ndtere hÃ¸yt volum selv; broker skaleres nasjonalt

### For samfunn
- **Interoperabilitet:** Standardisert meldingsflyt muliggjÃ¸r samordnet samhandling pÃ¥ tvers av sektorer
- **Robusthet:** Nasjonalt delt infrastruktur er mer pÃ¥litelig enn mange lokale lÃ¸sninger
- **Kostnadseffektivitet:** Redusert duplisering av integrasjonsinfrastruktur

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃ¥ndtering |
|---|---|---|---|
| **Teknisk** | FeilhÃ¥ndtering ved store volum og timeout/retry-scenarioer | HÃ¸y (komplekst) | Testing med hÃ¸yt volum; backpressure-mekanismer; dokumentasjon |
| **Integrasjon** | Integratorer implementerer feil â†’ meldinger ikke prosessert | Middels | Referansearkitektur; SDK-er; testing-verktÃ¸y |
| **Sikkerhet** | Feil tilgangsstyring gir uÃ¸nsket datapassasje | Middels | Fine-grained autorisasjon; audit-logging; rate-limiting |
| **Sikkerhet** | Tokenoppholdelse eller nÃ¸kkel-lekkasje i transportleddet | LÃ¥g (TLS) | Sterk kryptering; key-management; monitoring |
| **Operasjonell** | HÃ¸yt volum overstigter kapasitet â†’ kÃ¸-oppbygging og forsinkelser | Middels | Kapasitetsplanlegging; elastisk skalering; fallback-rutiner |
| **Brukeropplevelse** | Liten synlighet i asynkrone prosesser gir treg feiloppdagelse | HÃ¸y | Bedre logging, monitoring og diagnostikkverktÃ¸y |
| **Migrasjon** | Feil under migrering fra Altinn 2 â†’ datatap eller duplikater | Middels | Parallell drift; validering; reconciliation |
| **LeverandÃ¸r** | Avhengighet til Altinn 3-infrastruktur | HÃ¸y | Digdir som eier sikrer kontinuitet; SLA-krav |

## Kanaler

- **API-er i Altinn Docs** (Swagger/OpenAPI)
- **Integration frÃ¥n virksomhetenes fagsystem** (via SDK eller direkte API)
- **Integrasjonsplattformer** (MuleSoft, AzureIntegration, osv.)
- **Dokumentasjon og support** fra Altinn-forvaltningen
- **Sammarbeidsportal** (for spÃ¸rsmÃ¥l og erfaringsdeling)

## Plattform

- **Arkitektur:** Cloud-basert (Azure) multi-tenant SaaS i Altinn 3
- **Messaging-modell:** Asynkron broker-basert (FIFO-kÃ¸er)
- **Design-pattern:** Dekoblet avsender-mottaker via formidlingstjeneste
- **Skalering:** Designet for nasjonalt volum (10-100 mill. meldinger Ã¥rlig)
- **Sikkerhet:** TLS-kryptering i transit; enkryptert lagring; API-autentisering

## Gjenbruk

**SvÃ¦rt hÃ¸y gjenbruksverdi:**
- Felles transport- og formidlingskapabilitet for mange sektorer (offentlig og privat)
- Reduserer duplisering av integrasjonsinfrastruktur i enkeltvirksomheter
- Fremmer standardiserte, lÃ¸st koblede samhandlingsmÃ¸nstre
- API-standard som kan gjenbrukes for mange domener (skatt, helse, NAV, osv.)

## StÃ¸tte arkitekturprinsipper

- **P4 Del og gjenbruk data** â€“ Sikker formidling av delte data
- **P5 Del og gjenbruk lÃ¸sninger** â€“ Felles formidlingskomponent for alle integrasjoner
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ Enabler asynkron samhandling
- **P7 SÃ¸rg for tillit til oppgavelÃ¸sningen** â€“ Sporbarhet og sikkerhet i leveranse
- **P8 Etabler felles forstÃ¥else av informasjon** â€“ Standardisert API-kontrakt

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som del av Altinn 3-plattformen (inkludert i Altinn-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter
- **Kapasitetsestimater:** Estimert 3-8 MNOK Ã¥rlig for drift innenfor Altinn-operasjonen
- **Migrasjon:** Ekstra ressurser under Altinn 2 â†’ 3-migrasjon (2023-2026)

**Finansiering:** Via Digdir/statsbudsjett som del av felleskomponenter-ordningen.

**Kilder:** Estimert basert pÃ¥ Altinn-portefÃ¸lje-rapporter; eksakt kostnadsallokering ikke offentlig spesifisert.

## Forvaltning/eier

| AnsvarsomrÃ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) / Altinn-forvaltningen | Strategisk retning, API-kontrakt, standarder |
| **Driftsansvar** | Altinn-operasjonen (Digdir + ekstern driftsleverandÃ¸r) | 24/7 drift, SLA ~99.95% oppetid |
| **Budsjettansvar** | Digdir / Statsbudsjett | Del av Altinn-portefÃ¸lje; ekstra ressurser for migrasjon |
| **Styringsmodell** | Altinn 3-produktgruppe / Datautveksling-domene | Felles strategi med eFormidling, API-Gateway, Events |

**Styringsforum:** Altinn 3-styre og datautvekslings-domene-mÃ¸ter (lÃ¸pende strategi og prioriteringer).

## Lenke til dokumentasjon

- https://docs.altinn.studio/nb/broker/ â€“ Formidling-dokumentasjon
- https://docs.altinn.studio/nb/broker/what-do-you-get/ â€“ Kapabiliteter-oversikt
- https://docs.altinn.studio/nb/broker/getting-started/ â€“ Getting-started guide
- https://docs.altinn.studio/nb/broker/reference/ â€“ API-referanse
- https://samarbeid.digdir.no/altinn-api/ â€“ Samarbeidsportal (Altinn API-koordinering)

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: Altinn Docs (hentet 2026-03-07)
- Samarbeidsportalen: Altinn API (hentet 2026-03-07)
- Kilder for finansiering: Altinn-portefÃ¸lje-rapporter (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

âœ… **Brukersegmenter:** Struktur ut som tabell med konkrete behov og estimert volum
âœ… **Risikomatrise:** 8 konkrete risikokategorier med hÃ¥ndtering  
âœ… **Finansiering:** Detaljert kostnadsmodell (estimert 3-8 MNOK Ã¥rlig)
âœ… **Forvaltning:** Tabell-format med tydelig ansvarsfordeling
âœ… **Veikart:** Konkrete fokusomrÃ¥der (migrasjons-stÃ¸tte, API-modernisering, observability)
âœ… **Scope:** Eksplisitt tabell over hva som inngÃ¥r/ikke inngÃ¥r
âœ… **Kapabiliteter:** Detalj-beskrivelser av hvordan hver kapabilitet realiseres
âœ… **Arkitekturdetal jer:** Broker-mÃ¸nster, kÃ¸mekanismer, FIFO, durable-storage konkretisert
âœ… **Migrasjons-kontekst:** Eksplisert forbindelse til Altinn 2 â†’ 3-migrasjon

