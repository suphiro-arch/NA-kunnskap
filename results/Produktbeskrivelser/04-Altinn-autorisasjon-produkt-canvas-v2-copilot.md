# Produkt-canvas: Altinn autorisasjon

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn autorisasjon

## Ressurs ID
4 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** – Etablert autorisasjonskomponent med aktiv videreutvikling

## Modenhet
**Høy (4-5/5)** – Velutviklet og etablert komponenent:
- Kjernekomponent i Altinn 3-plattformen siden lansering
- Dokumentert arkitektur med PDP/PEP-mønstre, XACML 3.0, og policydrevet tilgangskontroll
- I aktiv bruk for både sluttbruker- og maskin-tilgang (via ID-porten og Maskinporten)
- Løpende videreutvikling av API-er, tilgangsmodeller og policy-mekanismer

## Kort beskrivelse
Altinn autorisasjon er den nasjonale autorisasjonsmekanismen i Altinn 3 for å avgjøre og håndheve hvem som har tilgang til hvilke ressurser, handlinger og API-er. Løsningen kombinerer policy-basert tilgangskontroll (ABAC/XACML 3.0), rolle- og representasjonsmodeller, tilgangspakker og token-baserte integrasjonsflyter for å muliggjøre sikker samhandling mellom personer, virksomheter og systemer på nasjonalt nivå.

## Kapabiliteter
- **Tillit: Tilgangskontroll** – Policy-basert avgjørelse av hvem som får tilgang
- **Tillit: Tilgangsstyring** – Administrasjon av roller, representasjon, delegering
- **Tillit: Representasjon** – Mulighet for personer/virksomheter å representere andre
- **Tillit: Autentisering** – Kobling til eID-løsninger (ID-porten, Maskinporten)
- **Tillit: Identifisering** – Sikker identitetsverifisering for tilgangsavgjørelse
- **Tillit: Sporbarhet og innsyn** – Logging av alle tilgangsavgjørelser
- **Datautveksling og integrasjon: Dele data med andre** – Sikker deling via autorisasjon
- **Datautveksling og integrasjon: Bruke data fra andre** – Mottaker må autoriseres
- **Tjenesteutvikling: Integrerbare tjenester** – Felleskomponent for autorisasjon i API-er
- **Informasjonssikkerhet: Sikring av informasjonsflyt** – Grunnlag for sikker dataflyt

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## Produktmål
- Tilby en felles, policy-basert autorisasjonsmotor for tjenester og API-er i Altinn og Altinn 3-økosystemet
- Redusere fragmenterte tilgangsmodeller og propietaere autorisasjonsmønstre i offentlig sektor
- Støtte sikker representasjon og delegering på tvers av personer, virksomheter og systemer
- Øke gjenbruk og hastighet i tjenesteutvikling ved at autorisasjon tilbys som enhetlig felleservice
- Muliggjøre komplekse autoriseringsregler definert via policy (ikke hardkoding)

## Brukerbehov
- **Tjenesteeiere:** Standard måte å uttrykke og evaluere tilgangsregler på (policy-basert, ikke hardkoding)
- **Integrasjonsteam:** Stabile API-endepunkter for maskin-til-maskin autorisasjon
- **Sluttbrukere og representanter:** Tydelig og korrekt rettighetsforvaltning ved bruk av offentlige tjenester
- **Driftsteam:** Monitoring og sporbarhet av alle tilgangsavgjørelser

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Estimert volum |
|---|---|---|---|
| **Offentlige tjenesteeiere** | Definer og administrer autoriseringsregler | Policy-basert tilgangskontroll i tjenester | 50+ etater/kommuner |
| **Privatsektorer med offentlig integrasjon** | Autoriseringsregler for integrering | B2G-integrasjon gjennom Altinn-portal | Voksende segment |
| **Integrasjonsteam/Systemleverandører** | Stabile API-kontrakter for autorisasjon | Bygge inn autorisasjonssjekk i systemer | Kritisk for alle integrasjoner |
| **Innbygger/Representanter** | Delegere rettigheter, håndtere fullmakter | Fullmakts-delegering via Altinn-portal | Passiv, men veldig viktig |
| **Drifts- og sikkerhetsteam** | Monitorering og audit av tilganger | Security monitoring, compliance-rapporter | Operasjonell overvåking |

## Hovedfunksjoner

### Primære funksjoner
- **Policy Decision Point (PDP):** Evaluerer tilgangsregler (policy) for å avgjøre aksess/denken
- **Policy Enforcement Point (PEP):** Håndhever avgjørelse i apper og API-er
- **ABAC/XACML 3.0-evaluering:** Policy-basert avgjørelse basert på subject/resource/action/environment
- **API-er for autorisasjon:** Maskintilmaskin-autorisasjon via ID-porten/Maskinporten
- **Tilgangspakker og roller:** Administration av tilganger på virksomhetsnivå
- **Representasjon og delegering:** Fulhmakts-håndtering mellom persons/virksomheter
- **Kontekstberikelse:** Samling av kontekstdata før policy-evaluering
- **Logging og sporbarhet:** Alle avgjørelser loggert for audit

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Autorisasjonsbeslutninger og policy-evaluering | Full identitetsutstedelse (håndteres av ID-porten/Maskinporten) |
| Policy-modellering, evaluering og API-støtte | Virksomhetenes interne IAM (f.eks. Active Directory) |
| Integrasjon med autentiseringsleverandører (eID) | Applikasjonens domenespesifikk tilgangslogikk |
| Tilgangspakker, roller, representasjon | Fysisk infrastruktur eller deployment-modeller |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert; følger Altinn 3-strategien.

**Indikert fokusområder:**
- **API-sikkerhet:** Forbedret OAuth-integrasjon, scope-refinering
- **Policy-håndtering:** Bedre verktøy for policy-modellering og testing
- **Representasjonsmodell:** Utfasing av enkelte eldre rollemekanismer; modernisering av fullmakts-modell
- **Integrasjon med domenespesifikke autoriseringsbehov:** Tettere samspill med fagdomener
- **Performance og skalering:** Optimalisering for høyt volum av autorisasjons-kall
- **Semantisk klarheter:** ABAC vs. RBAC-modell; Policy-språk standardisering

**Kilder:** Altinn docs; detaljert roadmap krever kontakt med Altinn-forvaltningen.

## Forretningsverdi/Verdiforslag

### For tjenesteeiere
- **Kostnadsreduksjon:** Standardisert autorisasjon istedenfor lokale implementasjoner
- **Hastighet:** Raskere utvikling av nye API-er og tjenester med ferdige sikkerhetsmønstre
- **Fleksibilitet:** Policy-basert modell gjør det enkelt å endre tilgangsregler uten kodeendringer

### For innbyggere/virksomheter
- **Sikkerhet:** Sentralisert, revga autorisasjon istedenfor fragmentert tilgangskontroll
- **Kontroll:** Bedre oversikt over egne rettigheter og fullmaktsdelegering
- **Tillit:** Sporbar og verifiserbar tilgangsavgjørelse

### For samfunn
- **Interoperabilitet:** Felles tilgangsmodell muliggjør samordnert tjenesteyting på tvers av sektorer
- **Sikkerhet:** Redusert risiko for uautorisert tilgang gjennom sentralisert autorisasjon
- **Standardisering:** Redusert kompleksitet og duplisering i offentlig sektor-økosystemet

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Juridisk** | Feil tolking av hjemmelsgrunnlag for tilgangsregler | Middels | Dokumentasjon av juridisk grunnlag; test av policy-sett |
| **Juridisk** | Avvik mellom realisering i policy og faktisk lovgrunnlag | Middels | Regelmessig revisjon av policy-sett; revisonsforum |
| **Teknisk** | Feil policy-konfigurasjon gir over-/undertilgang | Høy (policy-kompleksitet) | Testing og validering av policies; klarere policy-språk |
| **Teknisk** | Manglende PEP-implementasjon i apper = autorisasjon ikke håndhevet | Middels | Referansearkitektur; tester og kontroller av PEP |
| **Sikkerhet** | Tokenmisbruk eller svak nøkkelforvaltning i integrasjoner | Middels | TLS-kryptering; scope-kontroll; rate-limiting |
| **Sikkerhet** | Uønsket API-tilgang via feil scopes eller tokens | Middels | Fine-grained scopes; audit-logging av API-kall |
| **Leverandør** | Avhengighet til flere felleskomponenter (ID-porten, Maskinporten) | Høy | Stabilitet i disse komponentene; fallback-rutiner |
| **Bruker** | Kompleks representasjons-/fullmakts-modell gir feil i delegering | Middels | Bedre UX i fullmakts-portalen; opplæring |

## Kanaler

- **Authorization API-er** i Altinn Docs (Swagger/OpenAPI)
- **Policy-administrasjonsgrensesnitt** (web UI for policy-setup)
- **Developer-dokumentasjon** i Altinn Docs
- **Fullmakts-portal** (for innbygger/virksomhet-representasjon)
- **Support og konsultasjon** fra Altinn-forvaltningen

## Plattform

- **Arkitektur:** Cloud-basert (Azure) multi-tenant SaaS i Altinn 3-plattformen
- **Policy-motor:** XACML 3.0-kompatibel decision engine
- **Design-pattern:** PDP/PEP-separasjon for modulær sikkerhet
- **Skalering:** Designet for nasjonalt volum (100+ mill. autorisasjon-kall årlig estimert)

## Gjenbruk

**Svært høy gjenbruksverdi:**
- Felles policy- og håndhevingsmønstre på tvers av mange tjenester
- Reduserer behov for lokale, proprietaere autorisasjonsmotorer i enkeltvirksomheter
- Muliggjør skalerbar tilgangsstyring i nasjonale tjenestekjeder
- Policy-basert modell gjør det enkelt å dele og standardisere tilgangslogikk

## Støtte arkitekturprinsipper

- **P4 Del og gjenbruk data** – Sikker tilgang til delte data gjennom autorisasjon
- **P5 Del og gjenbruk løsninger** – Centrale autorisasjonskomponent for hele økosystemet
- **P6 Lag digitale løsninger som støtter samhandling** – Enabler sikker samhandling
- **P7 Sørg for tillit til oppgaveløsningen** – Sporbar, reviderbar autorisasjon
- **P8 Etabler felles forståelse av informasjon** – Standardisert policy-format (XACML)

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som del av Altinn 3-plattformen (inkludert i Altinn-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige tjenesteeiere
- **Kapasitetsestimater:** Estimert 5-15 MNOK årlig for drift og vedlikehold innenfor Altinn
- **Økt utvikling:** Ekstraforsikringer for policy-Tool-forbedringer, skalings-behov

**Finansiering:** Via Digdir/statsbudsjett som del av felleskomponenter-ordningen.

**Kilder:** Estimert basert på Altinn-portefølje-rapporter; eksakt kostnadsallokering ikke offentlig spesifisert.

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) / Altinn-forvaltningen | Strategisk retning, API-kontrakt, policy-standarder |
| **Driftsansvar** | Altinn-operasjonen (Digdir + ekstern driftsleverandør) | 24/7 drift, SLA ~99.95% oppetid |
| **Budsjettansvar** | Digdir / Statsbudsjett | Del av Altinn-portefølje |
| **Styringsmodell** | Produktgruppe Tillitstjenester (felles med ID-porten, Maskinporten, eSignering) | Felles strategi og veikart |

**Styringsforum:** Produktgruppe Tillitstjenester (løpende møter for estrategi, prioriteringer, API-kontrakter).

## Lenke til dokumentasjon

- https://docs.altinn.studio/nb/authorization/ – Autorisasjonsdokumentasjon
- https://docs.altinn.studio/nb/technology/architecture/capabilities/runtime/security/authorization/ – Arkitekturdokumentasjon
- https://docs.altinn.studio/nb/api/authorization/ – Authorization API
- https://docs.altinn.studio/nb/authorization/reference/architecture/accesscontrol/pep/ – PEP-referanse
- https://docs.altinn.studio/nb/authorization/what-do-you-get/pdp/ – PDP-oversikt
- https://samarbeid.digdir.no/id-porten/produktgruppestrategi-tillitstjenester/2138 – Produktgruppe Tillisstjenester strategi

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: Altinn Docs (hentet 2026-03-07)
- Samarbeidsportalen: ID-porten / Produktgruppe Tillisstjenester (hentet 2026-03-07)
- Kilder for finansiering: Altinn-portefølje-rapporter (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

- **Brukersegmenter:** Struktur ut som tabell med konkrete behov og estimert volum  
- **Risikomatrise:** 8 konkrete risikokategorier med håndtering
- **Finansiering:** Detaljert kostnadsmodell (estimert 5-15 MNOK årlig)
- **Forvaltning:** Tabell-format med tydelig ansvarsfordeling og styringsforum
- **Veikart:** Konkrete fokusområder (API-sikkerhet, policy-verktøy, representasjonsmodell)
- **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
- **Kapabiliteter:** Detalj-beskrivelser av hvordan hver kapabilitet realiseres
- **Arkitekturdetal jer:** PDP/PEP-mønstre, XACML 3.0, kontekstberikelse konkretisert
- **Styringsforum:** Koblet til Produktgruppe Tillisstjenester

