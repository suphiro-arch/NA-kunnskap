# Produkt-canvas: Altinn

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn

## Ressurs ID
DIGDIR-017

## Status/Livsfase
**Produksjon** – Etablert og modent fellesprodukt med aktiv videreutvikling

## Modenhet
**Høy (5/5)** – Velutviklet og dominerende fellesløsning:
- I ordinær bruk siden lansering (originalt 2006, modernisert til Altinn 3)
- Viktigste platform for digitale offentlige tjenester i Norge
- Dokumentert API-er, arkitektur og integrasjonsrammer
- Kontinuerlig modernisering av plattformen og tjenestesettingen

## Kort beskrivelse
Altinn er Norges nasjonale plattform for digitale tjenester, meldingsutveksling og samhandling mellom offentlige virksomheter, innbyggere og næringsliv. Løsningen tilbyr end-to-end infrastruktur for tjenesteutvikling, -kjøring og -forvaltning, med integrering av felles sikkerhets- og samhandlings-komponenter.

## Kapabiliteter
- **Samarbeid: Tjenesteforvaltning** – Verktøy for tjenesteeiere til å administrere tjenester.
- **Tjenesteutvikling: Gjenbrukbare tjenester** – Byggeklosser og mønstre for rask tjenesteutvikling.
- **Tjenesteutvikling: Integrerbare tjenester** – Standard API-er for integrasjon med andre systemer.

## Produktmål
- Standardisere og effektivisere digital tjenesteleveranse i offentlig sektor
- Tilby nøkkelferdige infrastruktur som reduserer tidsbrukt og kostnad fra behov til produksjon
- Muliggjøre effektiv samhandling mellom innbyggere, virksomheter og offentlig sektor
- Øke gjenbruk av felles komponenter og mønstre på tvers av virksomheter
- Understøtte brukerorient at og tilgjengelig digital tjenesteutvikling

## Brukerbehov
- **Tjenesteeiere:** Sikker, skalabel og kostnadseffektiv platform for tjenesteutvikling og drift
- **Slutbrukere (innbyggere/virksomheter):** Sikre, brukervenlige og tilgjengelige digitale tjenester
- **Utviklingsteam:** Standardiserte verktøy, komponenter og dokumentasjon som akselererer development
- **Driftsoperasjoner:** Robust infrastruktur, monitoring, support, og god «ops»-erfaring

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Estimert volum |
|---|---|---|---|
| **Offentlige tjenesteeiere (50+ etater)** | Plattform for tjenesteutvikling/drift | Hundrevis av tjenester, millioner av transaksjoner | 500+ tjenester i produksjon |
| **Innbyggere som sluttbrukere** | Enkle, sikre og tilgjengelige tjenester | Innsending, søknader, meldinger, innsyn | Millioner av innbyggere årlig |
| **Næringsliv som sluttbrukere** | Automatisert integrasjon mot offentlig sektor | Rapportering, søknader, integrasjon | 100 000+ virksomheter |
| **Utviklings- og leverandørteam** | Verktøy og API-er for tjenesteutvikling | Altinn Studio, SDK-er, API-dokumentasjon | 1000+ utviklere |
| **Drifts- og sikkerhetsteam** | Robust infrastruktur, monitoring, support | Operations, incident-management, compliance | Løpende operasjonell |
| **Arkitektur- og strategiteam** | Oversikt over tilløket og retning | Strategi, kapasitetsplanlegging, modernisering | Nasjonal nivå |

## Hovedfunksjoner

### Primære funksjoner
- **Altinn Studio:** Cloud-basert IDE/plattform for tjenesteutvikling (low-code/no-code + custom logic)
- **Altinn Apps:** Runtime-miljø for kjøring av digitale Altinn-tjenester
- **Altinn Portal:** Innbygger-grensesnitt for søknader, meldinger, innsyn (legacy; migreres til Altinn Apps)
- **Altinn Formidling:** Rammeverk for sikker og pålitelig meldingsutveksling
- **Autentisering:** Integrering med ID-porten og andre sikkerhets-komponenter
- **Autorisasjon:** Integrering med Altinn autorisasjon (PDP/PEP) for tilgangskontroll
- **Notifikasjoner:** Varsling til brukere (e-post, SMS osv.)
- **Innsyn og logging:** Sporing av alle transaksjoner; brukerinnsyn
- **API-er:** Maskinlesbare grensesnitt for integrasjon med andre systemer
- **Administrasjonsverktøy:** Portal for tjenesteeiere til å administrere tjenester

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Plattform for utvikling, kjøring og forvaltning av digitale tjenester | Sektorspesifikk forretningslogikk eller fagprosesser |
| Infrastruktur, sikkerheit, integrasjon med felles komponenter | Etat-interne systemlandskap eller bakoffice-prosesser |
| Standard mønstre og byggeklosser for rask utvikling | Garantier om full end-to-end prosess-håndtering |
| API-basert integrasjon og datautveksling | Datalagring eller fullstendig content management utenfor plattformen |

## Veikart over kommende funksjonalitet

**Status:** Løpende modernisering; detaljert prioritering gjennom Altinn-styring.

**Indikert fokusområder:**
- **Altinn 3-migrering:** Fullskala migration fra legacy Altinn 2 til Altinn 3 (2024-2026+)
- **Bedre developer experience:** Forbedret IDE, SDK-er, dokumentasjon, test-miljøer
- **Personalisering:** Innlogging for bedre relevans i bruker-opplevelse
- **Event-driven arkitektur:** Hendelsesdrevet integrasjon (Altinn Events) for real-time prosesser
- **API-modernisering:** OpenAPI/REST-standardisering av alle API-er
- **Ytelse og skalering:** Optimalisering for massive volum (millioner av transaksjoner årlig)
- **UX-forbedring:** Bedre brukeropplevelse for både tjenesteeiere og sluttbrukere
- **AI/ML-integrasjon:** Automation og intelligent prosess-håndtering

**Kilder:** Altinn-strategi og roadmap; Digdir-domenostrategi.

## Forretningsverdi/Verdiforslag

### For offentlig sektor
- **Kostnadsreduksjon:** Estimert 50-70% lavere kostnad vs. bygging av eget system
- **Hastighet:** 6-12 mnd kortere time-to-market for nye tjenester
- **Skalerbarheit:** Samme plattform brukes av alle etater; massiv gjenbruk

### For innbyggere og næringsliv
- **Brukervennlighet:** Sikre, moderne digitale tjenester
- **Effektivitet:** Raskere saksbehandling gjennom digitalisering
- **Tilgjengelighet:** Enkelt og tilgjengelig digital inngev av søknader

### For samfunn
- **Innovasjon:** Plattform åpner for raskere tjenesteinnovasjon
- **Kostnadseffektivitet:** Estimert 5-10 MNOK årlig gevinst gjennom redusert tjeneste-etablering
- **Digitalisering:** Grunnlag for massivt digitaliserings-løft i offentlig sektor

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Juridisk** | Feil tolkning av regelverket i tjeneste-logikk | Høy | Juridisk veiledning; code review; testing |
| **Teknisk** | Avhengighet til plattformendringer → breaking changes | Høy | API-kontraktsstabilitet; versjonering; migration-planer |
| **Sikkerhet** | Svak implementering av autentisering/autorisasjon hos tjenesteeier | Høy | Sikkerhets-guidelines; code-review; audit |
| **Integrasjon** | Feil bruk av API-er → dårlig performance eller sikkerhet | Høy | API-dokumentasjon; best-practice guides; support |
| **Organisatorisk** | Mangel på kompetanse hos tjenesteeiere til å implementere | Høy | Opplæring, SDK-er, templates, supportperson |
| **Operasjonell** | Høyt dokument-volum > kapasitetsproblem | Middels | Kapasitetsplanlegging; skalering; performance-optimalisering |
| **Leverandør** | Avhengighet til Altinn-infrastruktur og -driftsleverandør | Høy | Offentlig eierskap (Digdir) sikrer kontinuitet; SLA 99.5%+ |
| **Bruker** | Dårlig tjenestekvalitet frå tjenesteeiere → innbygger-frustrasjon | Høy | Quality assurance; bruker-feedback-løkker; insentiver |

## Kanaler

- **Altinn.no:** Primær inngang for innbyggere/næringsliv
- **Altinn Portal:** Bruker-grensesnitt for tjenester og innsyn
- **Altinn Studio:** Webbasert IDE for tjenesteeiere
- **API-er:** Maskinlesbar integrering for andre systemer
- **SMS/E-post:** Varslinger og notifikasjoner til brukere
- **Administratorportaler:** Tjenesteeiere-administration

## Plattform

- **Arkitektur:** Microservices-basert cloud-løsning (Azure) med high-availability design
- **Kjøretid:** Cloud-basert Kubernetes + container-orkestrasjon
- **Utviklermiljø:** Altinn Studio (web-IDE) + SDK-er for lokalt development
- **Skalering:** Auto-scaling designet for nasjonalt volum (100+ mill. transaksjoner årlig)
- **Sikkerhet:** Integrering med ID-porten, Maskinporten, eSignering, Altinn autorisasjon

## Gjenbruk

**Svært høy gjenbruksverdi:**
- Felles plattform for alle 50+ fagfetater = massive skalerings-effekter
- Standardiserte byggeklosser (UI-komponenter, integrasjonsmønstre) gjenbrukt across 500+ tjenester
- En gang bygget = utgift delt på alle som bruker
- Reduserer dobbeltarbeid på tvers av virksomheter

## Støtte arkitekturprinsipper

- **P1 Ta utgangspunkt i brukernes behov** – Brukersentrert tjenestedesign
- **P2 Bruk nasjonale fellesløsninger** – _Altinn er_ en nasjonal fellesløsning
- **P5 Del og gjenbruk løsninger** – Felles plattform for alle
- **P6 Lag digitale løsninger som støtter samhandling** – Enabler tverretatlig samhandling
- **P7 Sørg for tillit til oppgaveløsningen** – Sikkerhet og transparens bygg-inn

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som nasjonal felleskomponent (Digdir-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter; privat sektor betaler brukergebyr (variabel)
- **Estimert kostnader:** 200-400 MNOK årlig for drift, utvikling, infrastruktur og support
- **Investeringer:** Løpende modernisering av plattformen (Altinn 3-migrering, 2024-2026)

**Finansiering:** Via Digdir-budsjett (felleskomponenter); EU-finansiering for modernisering (Digital Europe-program).

**kilder:** Digdir-budsjett-dokumenter, offentlige rapporter; presis kostnadsallokering ikke fullt offentliggjort.

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Altinn-forvaltningen (Digdir) | Strategisk retning, roadmap, produkts-gouvernans |
| **Driftsansvar** | Altinn-operasjonen (Digdir + partner) | 24/7 drift, 99.5%+ oppetid, incident-management |
| **Budsjettansvar** | Digdir / Statsbudsjett / EU-finansiering | Via «Felleskomponenter» og modernisering-budsjett |
| **Styringsmodell** | Altinn-styre (fagfeteater + Digdir) | Nasjonalt strategisk nivå; brukerrepresentasjon |

**Styringsforum:** Altinn-styre; Altinn 3-produktgruppe; Digitaliserings-råd (offentlig sektor).

## Lenke til dokumentasjon

- https://www.altinn.no – Brukerportal
- https://docs.altinn.studio/nb/ – Altinn Studio dokumentasjon
- https://docs.altinn.studio/nb/altinn-studio/architecture/ – Arkitektur-dokumentasjon
- https://samarbeid.digdir.no/altinn-api – Samarbeidsportal (API-forvaltning)
- https://www.digdir.no/altinn – Altinn-informasjon fra Digdir

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: Altinn.no, Altinn Docs, Digdir.no (hentet 2026-03-07)
- Kilder for finansiering: Digdir-rapporter, statsbudsjett (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

- **Brukersegmenter:** Struktur ut som tabell med konkrete behov, bruksområder og volum-estimater
- **Risikomatrise:** 8 konkrete risikokategorier med håndtering
- **Finansiering:** Detaljert kostnadsmodell (estimert 200-400 MNOK årlig)
- **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Digdir + Altinn-styre)
- **Veikart:** Konkrete fokusområder (Altinn 3-migrering, developer experience, event-driven, AI/ML)
- **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
- **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet (Studio, Apps, Portal, Formidling)
- **Strategisk kontekst:** Eksplisitt kobling til Altinn 3-modernisering og nasjonal strategi
- **Scale-dimensjon:** Tydelig at dette er landets viktigste plattform for digitale tjenester
- **Tegn-rettelser:** Korrigert fra "Maalgruppe" → "Målgruppe", "Hoy" → "Høy"
