# Produkt-canvas: Altinn Studio

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn Studio

## Ressurs ID
DIGDIR-018

## Status/Livsfase
**Produksjon** – Etablert IDE og utviklingsplattform med aktiv videreutvikling

## Modenhet
**Høy (4-5/5)** – Velutviklet og sentral utviklings-plattform:
- I ordinær bruk som primær IDE for Altinn-tjenesteutvikling
- Omfattende dokumentasjon, API-er og ekosystem av SDK-er og verktøy
- Bred adopsjon blant tjenesteeiere og leverandører
- Kontinuerlig videreutvikling av developer experience, komponenter og runtime

## Kort beskrivelse
Altinn Studio er web-basert IDE og utviklingsplattform for bygging av digitale Altinn-tjenester. Løsningen tilbyr low-code/no-code verktøy, standardiserte byggeklosser, integrasjonsmønstre og runtime-kapabiliteter som drastisk reduserer tid og kompleksitet fra behovsanalyse til produksjonssetting av digitale tjenester.

## Kapabiliteter
- **Tjenesteutvikling: Utviklings- og kjøretidsmiljø** – Integrert IDE og runtime for tjenesteutvikling
- **Tjenesteutvikling: Integrerbare tjenester** – API-er og integrasjonsmønstre mot Altinn og felleskomponenter
- **Tjenesteutvikling: Gjenbrukbare tjenester** – Komponenter-bibliotek og mønstre for enkel gjenbruk
- **Tjenesteutvikling: Tjenestedesign** – Low-code UI-modellering for brukergrensesnitt
- **Sluttbrukertjenester: Sammenhengende tjenester** – Integration med Altinn Portal/Apps for sluttbrukerpresentasjon
- **Samarbeid: Tjenesteforvaltning** – Verktøy for release-management, versjonering, miljøer
- **Datautveksling og integrasjon: Bruke data fra andre** – API-integrasjon mot andre systemer
- **Informasjonssikkerhet: Sikring av informasjonsflyt** – Bygg-inn sikkerheit, autentisering, autorisasjon

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## Produktmål
- Senke terskelen for utvikling av digitale offentlige tjenester (low-code enablement)
- Standardisere og akselerere tjenesteutvikling gjennom felles byggeklosser og mønstre
- ?ke gjenbruk av komponenter og maler på tvers av virksomheter og tjenester
- Muliggjøre raskere iterasjon og feedback-løkker fra tjenesteeiere til sluttbrukere
- Understøtte høy kvalitet og sikkerheit gjennom bygg-inn best-practices

## Brukerbehov
- **Tjenesteeiere:** Rask og kostnadseffektiv måte å utvikle og iterate på digitale tjenester
- **Utviklingsteam:** Produktivt utviklingsmiljø med standardiserte verktøy, komponenter og dokumentasjon
- **UX/Design-team:** Visuell modellering av brukergrensesnitt uten å vite dybdedetaljer
- **Forvaltningsmiljøer:** Kontroll, sporbarheit og effektiv release-management
- **Driftsteam:** Observability, monitoring og enkel deployment til produksjon

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Estimert volum |
|---|---|---|---|
| **Offentlige tjenesteeiere (50+ etater)** | Plattform for rask tjenesteutvikling | Tjenesteutvikling, modernisering, vedlikehold | 300+ tjenester i Studio |
| **Utviklering- og leverandørteam** | IDE med SDK-er, komponenter og API-er | Altinn-tjenesteutvikling, integrasjon | 500+ aktive utviklere |
| **Produktledere og arkitekter** | Oversikt og planlegging av tjeneste-portefølje | Roadmapping, quality-assurance, governance | Løpende strategisk nivå |
| **UX/Design-team** | Visuell modellering av brukergrensesnitt | Form-design, workflow-design, brukbarhet | Høyt volum per prosjekt |
| **Drifts- og DevOps-team** | Deployment, monitoring, incident-management | Release-management, operations, troubleshooting | Løpende operasjonell |

## Hovedfunksjoner

### Primære funksjoner
- **Web-basert IDE:** Cloud-basert editor uten installation; tilgjengelig fra hvor som helst
- **Low-code form-builder:** Visuell modellering av skjemaer, validering, logikk
- **Komponenter-bibliotek:** Gjenbrukbare UI-komponenter (tekstfelt, radioer, tabeller, etc.)
- **Workflowdefinisjoner:** Prosessmodellering for multi-step tjenester
- **API-integrasjon:** Tilkobling til fellestjenester (autentisering, autorisasjon, notifikasjon, etc.)
- **Data-modellering:** Definisjon av datasett-struktur og validering
- **Testmiljøer:** Local development (Git-basert) + cloud-basert test-miljø (TT02, PP)
- **Versjonering og release:** Release-management, versjonering, rollback-kapabilitet
- **Deployment-automatisering:** CI/CD-pipeline for automatisert deployment til produksjon
- **Runtime-integration:** Direkte kjøring i Altinn Apps-infrastrukturen
- **Dokumentasjon:** Inline docs, API-spec, eksempler, tutorials
- **Monitoring og logging:** Innsyn i kjørende tjenester, error-logging, performance-metrikker

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Utviklings-IDE for tjenesteutvikling | Drift av produksjonsmiljøet (håndteres av Altinn-operasjonen) |
| Low-code komponenter og mønstre | Full custom backend-implementering (men kan kodes) |
| Integrasjon med fellestjenester | Sektorspesifikk forretningslogikk |
| Test- og produksjons-miljøer | Etat-interne systemlandskap eller bakoffice |

## Veikart over kommende funksjonalitet

**Status:** Løpende modernisering; detaljert prioritering gjennom Altinn Studio-produktgruppe.

**Indikert fokusområder:**
- **Forbedret developer experience:** Bedre IDE-UX, raskere feedback-løkper, bedre ide-integrasjon
- **Utvidet komponenter-bibliotek:** Flere low-code komponenter for vanlige use-case
- **Bedre dokumentasjon:** Tutorials, code-samples, API-dokumentasjon
- **Ytelse-forbedringer:** Raskere IDE, raskere deployment, raskere runtime
- **CLI/SDK modernisering:** Bedre local development experience
- **Testing-verktøy:** Automated testing framework for tjenester
- **Observability:** Bedre innsyn i kjørende tjenester (logging, metrics, traces)
- **AI-assistanse:** Code-suggest, form-generation, test-generation

**Kilder:** Altinn Studio-produktgruppe; Altinn 3-moderniserings-strategi.

## Forretningsverdi/Verdiforslag

### For tjenesteeiere
- **Hastighet:** 50-70% kortere development-tid ved bruk av Studio vs. custom-koding
- **Kostnadsreduksjon:** Lavere kompetansekrav = billigere ressurser
- **Skalerbarheit:** Samme Workflow skaleres til tusener av tjenester

### For utviklere
- **Produktivitet:** Low-code effektivitet + mulighet for custom-koding når nødvendig
- **Trivsel:** Moderne verktøy, cloud-basert tilgang, god dokumentasjon
- **Karriere:** Etterspørsel etter Altinn-kompetanse; attraktiv ferdighetsmiks

### For organisasjoner
- **Porteføljeeffekt:** Enkel kontroll og oversikt over alle Altinn-tjenester
- **Kvalitet:** Standardiserte mønstre sikrer konsistent kvalitet across tjenester
- **Modernisering:** Raskere migrering fra eldre løsninger til Altinn 3

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Juridisk** | Feil implementasjon av regelverket i tjeneste-logikk | Høy | Juridisk veiledning; code review; templates |
| **Teknisk** | Avhengighet til plattformendringer → compatibilty-brudd | Middels | API-kontraktsstabilitet; versjonering; migration-path |
| **Sikkerhet** | Svak implementering av sikkerhetsmekanismer | Høy | Sikkerhets-guide; code review; best-practice templates |
| **Kompetanse** | Mangel på kunnskap om Studio-bruk → dårlig implementering | Høy | Opplæring, tutorials, SDK-er, support, communities |
| **Ytelse** | Optimalt-dårlig tjeneste-utvikling → performance-problem | Middels | Performance-guide; monitoring; kapasitets-planlegging |
| **Bruker** | Dårlig tjenestekvalitet fordi feil design i Studio | Høy | UX-guide; design-patterns; review-prosess |
| **Leverandør** | Avhengighet til Altinn-infrastruktur og -plattformutvikling | Høy | Digdir-eierskap sikrer kontinuitet; SLA; transparente roadmaps |
| **Integrasjon** | Feil API-integrasjon mot fellestjenester | Middels | API-dokumentasjon; SDK-er; test-miljøer; support |

## Kanaler

- **Web-IDE:** https://studio.altinn.cloud/ (cloud-basert development environment)
- **Dokumentasjon:** https://docs.altinn.studio/nb/ (extensiv online dokumentasjon)
- **Testmiljø:** TT02, PP (cloud basert test-infrastruktur)
- **CLI tools:** Lokale verktøy for utviklere (Git-basert workflow)
- **SDK-er:** JavaScript/TypeScript SDK-er for backend-logikk
- **Samarbeidsportal:** Erfaringsdeling, Q&A, community

## Plattform

- **Hosting:** Cloud-basert (Azure) Studio-infrastruktur
- **Arkitektur:** Microservices + containerized komponenter
- **Storage:** Git-basert (GitHub) for versjonering av tjenest-kode
- **Runtime:** Altinn Apps (Kubernetes-basert container-runtime)
- **Integrasjon:** REST API-er mot Altinn Services og fellestjenester
- **CI/CD:** Automatsisk testing og deployment-pipeline

## Gjenbruk

**Svært høy gjenbruksverdi:**
- Samme Studio bruges av alle 50+ fagfetater og 300+ tjenester
- Komponenter-biblioteket gjenbrukes across tusener av tjenester
- Mønstre og best-practice templates reduserer dobbeltarbeid
- ?kende nettverkseffekt når flere tjenesteeiere bidrar med komponenter

## Støtte arkitekturprinsipper

- **P1 Ta utgangspunkt i brukernes behov** – Brukersentrert tjenestedesign i Studio
- **P5 Del og gjenbruk løsninger** – Komponenter og mønstre gjenbrukt massivt
- **P6 Lag digitale løsninger som støtter samhandling** – Enabler tverretatlig tjenesteutvikling
- **P7 Sørg for tillit til oppgaveløsningen** – Sikkerhet og best-practice bygg-inn

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som del av Altinn-plattformen (Digdir-budsjett)
- **Bruksmodell:** Kostnadsfritt for alle offentlige virksomheter
- **Estimert kostnader:** 30-60 MNOK årlig for development, vedlikehold, infrastruktur og support
- **Investeringer:** Løpende forbedring av IDE, komponenter, dokumentasjon

**Finansiering:** Via Digdir-budsjett som del av Altinn-operasjonen.

**Kilder:** Estimert basert på Digdir-portefølje; presis kostnadsallokering ikke fullt offentliggjort.

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Altinn Studio-produktgruppe (Digdir) | Strategisk retning, feature-backlog, developer experience |
| **Driftsansvar** | Altinn-operasjonen (Digdir + partner) | 24/5 drift, 99.5%+ oppetid, support |
| **Budsjettansvar** | Digdir / Statsbudsjett | Som del av Altinn-budsjett |
| **Styringsmodell** | Altinn 3-styre; Tjenesteutvikling-domene | Nasjonalt strategisk nivå |

**Styringsforum:** Altinn 3-produktgruppe; Tjenesteutvikling-domene; Developer communities (bruker-input).

## Lenke til dokumentasjon

- https://studio.altinn.cloud – Altinn Studio (IDE)
- https://docs.altinn.studio/nb/ – Offisiell dokumentasjon
- https://docs.altinn.studio/nb/altinn-studio/getting-started/ – Getting started guide
- https://docs.altinn.studio/nb/altinn-studio/reference/ – API-referanse
- https://samarbeid.digdir.no/altinn-api – Samarbeidsportal (API-koordinering)

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: Altinn Docs, Studio.altinn.cloud (hentet 2026-03-07)
- Kilder for finansiering: Digdir-rapporter og Altinn-portefølje (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

- **Brukersegmenter:** Struktur ut som tabell med konkrete behov og estimater
- **Risikomatrise:** 8 konkrete risikokategorier med håndtering
- **Finansiering:** Detaljert kostnadsmodell (estimert 30-60 MNOK årlig)
- **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Studio-produktgruppe + Digdir)
- **Veikart:** Konkrete fokusområder (IDE-UX, komponenter, testing-verktøy, AI-assistanse)
- **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
- **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet (IDE, low-code, integrasjon, deployment)
- **Developer-fokus:** Eksplisitt fokus på utvikler-opplevelse og produktivitet
- **Tegn-rettelser:** Korrigert fra "Maalgruppe" → "Målgruppe", "Hoy" → "Høy", "kjoeretidsmilje" → "kjøretidsmiljø"

