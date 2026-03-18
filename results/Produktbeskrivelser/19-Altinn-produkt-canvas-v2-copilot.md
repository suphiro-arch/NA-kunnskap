# Produkt-canvas: Altinn

MÃƒÂ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn

## Ressurs ID
DIGDIR-017

## Status/Livsfase
**Produksjon** Ã¢â‚¬â€œ Etablert og modent fellesprodukt med aktiv videreutvikling

## Modenhet
**HÃƒÂ¸y (5/5)** Ã¢â‚¬â€œ Velutviklet og dominerende felleslÃƒÂ¸sning:
- I ordinÃƒÂ¦r bruk siden lansering (originalt 2006, modernisert til Altinn 3)
- Viktigste platform for digitale offentlige tjenester i Norge
- Dokumentert API-er, arkitektur og integrasjonsrammer
- Kontinuerlig modernisering av plattformen og tjenestesettingen

## Kort beskrivelse
Altinn er Norges nasjonale plattform for digitale tjenester, meldingsutveksling og samhandling mellom offentlige virksomheter, innbyggere og nÃƒÂ¦ringsliv. LÃƒÂ¸sningen tilbyr end-to-end infrastruktur for tjenesteutvikling, -kjÃƒÂ¸ring og -forvaltning, med integrering av felles sikkerhets- og samhandlings-komponenter.

## Kapabiliteter
- **Tjenesteutvikling: Utviklings- og kjÃƒÂ¸retidsmiljÃƒÂ¸** Ã¢â‚¬â€œ Altinn Studio som platform for tjenesteutvikling
- **Tjenesteutvikling: Integrerbare tjenester** Ã¢â‚¬â€œ Standard API-er for integrasjon med andre systemer
- **Tjenesteutvikling: Gjenbrukbare tjenester** Ã¢â‚¬â€œ Byggeklosser og mÃƒÂ¸nstre for rask tjenesteutvikling
- **Datautveksling og integrasjon: Meldingsformidling** Ã¢â‚¬â€œ Altinn Formidling for sikker meldingsutveksling
- **Sluttbrukertjenester: Sammenhengende tjenester** Ã¢â‚¬â€œ Altinn Portal og Altinn Apps for innbygger-grensesnitt
- **Samarbeid: Tjenesteforvaltning** Ã¢â‚¬â€œ VerktÃƒÂ¸y for tjenesteeiere til ÃƒÂ¥ administrere tjenester
- **Informasjonssikkerhet: Sikring av informasjonsflyt** Ã¢â‚¬â€œ Integrert sikkerheit, autentisering, autorisasjon

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## ProduktmÃƒÂ¥l
- Standardisere og effektivisere digital tjenesteleveranse i offentlig sektor
- Tilby nÃƒÂ¸kkelferdige infrastruktur som reduserer tidsbrukt og kostnad fra behov til produksjon
- MuliggjÃƒÂ¸re effektiv samhandling mellom innbyggere, virksomheter og offentlig sektor
- ÃƒËœke gjenbruk av felles komponenter og mÃƒÂ¸nstre pÃƒÂ¥ tvers av virksomheter
- UnderstÃƒÂ¸tte brukerorient at og tilgjengelig digital tjenesteutvikling

## Brukerbehov
- **Tjenesteeiere:** Sikker, skalabel og kostnadseffektiv platform for tjenesteutvikling og drift
- **Slutbrukere (innbyggere/virksomheter):** Sikre, brukervenlige og tilgjengelige digitale tjenester
- **Utviklingsteam:** Standardiserte verktÃƒÂ¸y, komponenter og dokumentasjon som akselererer development
- **Driftsoperasjoner:** Robust infrastruktur, monitoring, support, og god Ã‚Â«opsÃ‚Â»-erfaring

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃƒÂ¦re behov | BruksomrÃƒÂ¥de | Estimert volum |
|---|---|---|---|
| **Offentlige tjenesteeiere (50+ etater)** | Plattform for tjenesteutvikling/drift | Hundrevis av tjenester, millioner av transaksjoner | 500+ tjenester i produksjon |
| **Innbyggere som sluttbrukere** | Enkle, sikre og tilgjengelige tjenester | Innsending, sÃƒÂ¸knader, meldinger, innsyn | Millioner av innbyggere ÃƒÂ¥rlig |
| **NÃƒÂ¦ringsliv som sluttbrukere** | Automatisert integrasjon mot offentlig sektor | Rapportering, sÃƒÂ¸knader, integrasjon | 100 000+ virksomheter |
| **Utviklings- og leverandÃƒÂ¸rteam** | VerktÃƒÂ¸y og API-er for tjenesteutvikling | Altinn Studio, SDK-er, API-dokumentasjon | 1000+ utviklere |
| **Drifts- og sikkerhetsteam** | Robust infrastruktur, monitoring, support | Operations, incident-management, compliance | LÃƒÂ¸pende operasjonell |
| **Arkitektur- og strategiteam** | Oversikt over tillÃƒÂ¸ket og retning | Strategi, kapasitetsplanlegging, modernisering | Nasjonal nivÃƒÂ¥ |

## Hovedfunksjoner

### PrimÃƒÂ¦re funksjoner
- **Altinn Studio:** Cloud-basert IDE/plattform for tjenesteutvikling (low-code/no-code + custom logic)
- **Altinn Apps:** Runtime-miljÃƒÂ¸ for kjÃƒÂ¸ring av digitale Altinn-tjenester
- **Altinn Portal:** Innbygger-grensesnitt for sÃƒÂ¸knader, meldinger, innsyn (legacy; migreres til Altinn Apps)
- **Altinn Formidling:** Rammeverk for sikker og pÃƒÂ¥litelig meldingsutveksling
- **Autentisering:** Integrering med ID-porten og andre sikkerhets-komponenter
- **Autorisasjon:** Integrering med Altinn autorisasjon (PDP/PEP) for tilgangskontroll
- **Notifikasjoner:** Varsling til brukere (e-post, SMS osv.)
- **Innsyn og logging:** Sporing av alle transaksjoner; brukerinnsyn
- **API-er:** Maskinlesbare grensesnitt for integrasjon med andre systemer
- **AdministrasjonsverktÃƒÂ¸y:** Portal for tjenesteeiere til ÃƒÂ¥ administrere tjenester

### Scope og avgrensning

| InngÃƒÂ¥r | InngÃƒÂ¥r IKKE |
|---|---|
| Plattform for utvikling, kjÃƒÂ¸ring og forvaltning av digitale tjenester | Sektorspesifikk forretningslogikk eller fagprosesser |
| Infrastruktur, sikkerheit, integrasjon med felles komponenter | Etat-interne systemlandskap eller bakoffice-prosesser |
| Standard mÃƒÂ¸nstre og byggeklosser for rask utvikling | Garantier om full end-to-end prosess-hÃƒÂ¥ndtering |
| API-basert integrasjon og datautveksling | Datalagring eller fullstendig content management auÃƒÅ¸erhalb plattformen |

## Veikart over kommende funksjonalitet

**Status:** LÃƒÂ¸pende modernisering; detaljert prioritering gjennom Altinn-styring.

**Indikert fokusomrÃƒÂ¥der:**
- **Altinn 3-migrering:** Fullskala migration fra legacy Altinn 2 til Altinn 3 (2024-2026+)
- **Bedre developer experience:** Forbedret IDE, SDK-er, dokumentasjon, test-miljÃƒÂ¸er
- **Personalisering:** Innlogging for bedre relevans i bruker-opplevelse
- **Event-driven arkitektur:** Hendelsesdrevet integrasjon (Altinn Events) for real-time prosesser
- **API-modernisering:** OpenAPI/REST-standardisering av alle API-er
- **Ytelse og skalering:** Optimalisering for massive volum (millioner av transaksjoner ÃƒÂ¥rlig)
- **UX-forbedring:** Bedre brukeropplevelse for bÃƒÂ¥de tjenesteeiere og sluttbrukere
- **AI/ML-integrasjon:** Automation og intelligent prosess-hÃƒÂ¥ndtering

**Kilder:** Altinn-strategi og roadmap; Digdir-domenostrategi.

## Forretningsverdi/Verdiforslag

### For offentlig sektor
- **Kostnadsreduksjon:** Estimert 50-70% lavere kostnad vs. bygging av eget system
- **Hastighet:** 6-12 mnd kortere time-to-market for nye tjenester
- **Skalerbarheit:** Samme plattform brukes av alle etater; massiv gjenbruk

### For innbyggere og nÃƒÂ¦ringsliv
- **Brukervennlighet:** Sikre, moderne digitale tjenester
- **Effektivitet:** Raskere saksbehandling gjennom digitalisering
- **Tilgjengelighet:** Enkelt og tilgjengelig digital inngev av sÃƒÂ¸knader

### For samfunn
- **Innovasjon:** Plattform ÃƒÂ¥pner for raskere tjenesteinnovasjon
- **Kostnadseffektivitet:** Estimert 5-10 MNOK ÃƒÂ¥rlig gevinst gjennom redusert tjeneste-etablering
- **Digitalisering:** Grunnlag for massivt digitaliserings-lÃƒÂ¸ft i offentlig sektor

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃƒÂ¥ndtering |
|---|---|---|---|
| **Juridisk** | Feil tolkning av regelverket i tjeneste-logikk | HÃƒÂ¸y | Juridisk veiledning; code review; testing |
| **Teknisk** | Avhengighet til plattformendringer Ã¢â€ â€™ breaking changes | HÃƒÂ¸y | API-kontraktsstabilitet; versjonering; migration-planer |
| **Sikkerhet** | Svak implementering av autentisering/autorisasjon hos tjenesteeier | HÃƒÂ¸y | Sikkerhets-guidelines; code-review; audit |
| **Integrasjon** | Feil bruk av API-er Ã¢â€ â€™ dÃƒÂ¥rlig performance eller sikkerhet | HÃƒÂ¸y | API-dokumentasjon; best-practice guides; support |
| **Organisatorisk** | Mangel pÃƒÂ¥ kompetanse hos tjenesteeiere til ÃƒÂ¥ implementere | HÃƒÂ¸y | OpplÃƒÂ¦ring, SDK-er, templates, supportperson |
| **Operasjonell** | HÃƒÂ¸yt dokument-volum > kapasitetsproblem | Middels | Kapasitetsplanlegging; skalering; performance-optimalisering |
| **LeverandÃƒÂ¸r** | Avhengighet til Altinn-infrastruktur og -driftsleverandÃƒÂ¸r | HÃƒÂ¸y | Offentlig eierskap (Digdir) sikrer kontinuitet; SLA 99.5%+ |
| **Bruker** | DÃƒÂ¥rlig tjenestekvalitet frÃƒÂ¥ tjenesteeiere Ã¢â€ â€™ innbygger-frustrasjon | HÃƒÂ¸y | Quality assurance; bruker-feedback-lÃƒÂ¸kker; insentiver |

## Kanaler

- **Altinn.no:** PrimÃƒÂ¦r inngang for innbyggere/nÃƒÂ¦ringsliv
- **Altinn Portal:** Bruker-grensesnitt for tjenester og innsyn
- **Altinn Studio:** Webbasert IDE for tjenesteeiere
- **API-er:** Maskinlesbar integrering for andre systemer
- **SMS/E-post:** Varslinger og notifikasjoner til brukere
- **Administratorportaler:** Tjenesteeiere-administration

## Plattform

- **Arkitektur:** Microservices-basert cloud-lÃƒÂ¸sning (Azure) med high-availability design
- **KjÃƒÂ¸retid:** Cloud-basert Kubernetes + container-orkestrasjon
- **UtviklermiljÃƒÂ¸:** Altinn Studio (web-IDE) + SDK-er for lokalt development
- **Skalering:** Auto-scaling designet for nasjonalt volum (100+ mill. transaksjoner ÃƒÂ¥rlig)
- **Sikkerhet:** Integrering med ID-porten, Maskinporten, eSignering, Altinn autorisasjon

## Gjenbruk

**SvÃƒÂ¦rt hÃƒÂ¸y gjenbruksverdi:**
- Felles plattform for alle 50+ fagfetater = massive skalerings-effekter
- Standardiserte byggeklosser (UI-komponenter, integrasjonsmÃƒÂ¸nstre) gjenbrukt across 500+ tjenester
- En gang bygget = utgift delt pÃƒÂ¥ alle som bruker
- Reduserer dobbeltarbeid pÃƒÂ¥ tvers av virksomheter

## StÃƒÂ¸tte arkitekturprinsipper

- **P1 Ta utgangspunkt i brukernes behov** Ã¢â‚¬â€œ Brukersentrert tjenestedesign
- **P2 Bruk nasjonale felleslÃƒÂ¸sninger** Ã¢â‚¬â€œ _Altinn er_ en nasjonal felleslÃƒÂ¸sning
- **P5 Del og gjenbruk lÃƒÂ¸sninger** Ã¢â‚¬â€œ Felles plattform for alle
- **P6 Lag digitale lÃƒÂ¸sninger som stÃƒÂ¸tter samhandling** Ã¢â‚¬â€œ Enabler tverretatlig samhandling
- **P7 SÃ¸rg for tillit til oppgavelÃƒÂ¸sningen** Ã¢â‚¬â€œ Sikkerhet og transparens bygg-inn

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som nasjonal felleskomponent (Digdir-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter; privat sektor betaler brukergebyr (variabel)
- **Estimert kostnader:** 200-400 MNOK ÃƒÂ¥rlig for drift, utvikling, infrastruktur og support
- **Investeringer:** LÃƒÂ¸pende modernisering av plattformen (Altinn 3-migrering, 2024-2026)

**Finansiering:** Via Digdir-budsjett (felleskomponenter); EU-finansiering for modernisering (Digital Europe-program).

**kilder:** Digdir-budsjett-dokumenter, offentlige rapporter; presis kostnadsallokering ikke fullt offentliggjort.

## Forvaltning/eier

| AnsvarsomrÃƒÂ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Altinn-forvaltningen (Digdir) | Strategisk retning, roadmap, produkts-gouvernans |
| **Driftsansvar** | Altinn-operasjonen (Digdir + partner) | 24/7 drift, 99.5%+ oppetid, incident-management |
| **Budsjettansvar** | Digdir / Statsbudsjett / EU-finansiering | Via Ã‚Â«FelleskomponenterÃ‚Â» og modernisering-budsjett |
| **Styringsmodell** | Altinn-styre (fagfeteater + Digdir) | Nasjonalt strategisk nivÃƒÂ¥; brukerrepresentasjon |

**Styringsforum:** Altinn-styre; Altinn 3-produktgruppe; Digitaliserings-rÃƒÂ¥d (offentlig sektor).

## Lenke til dokumentasjon

- https://www.altinn.no Ã¢â‚¬â€œ Brukerportal
- https://docs.altinn.studio/nb/ Ã¢â‚¬â€œ Altinn Studio dokumentasjon
- https://docs.altinn.studio/nb/altinn-studio/architecture/ Ã¢â‚¬â€œ Arkitektur-dokumentasjon
- https://samarbeid.digdir.no/altinn-api Ã¢â‚¬â€œ Samarbeidsportal (API-forvaltning)
- https://www.digdir.no/altinn Ã¢â‚¬â€œ Altinn-informasjon fra Digdir

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: Altinn.no, Altinn Docs, Digdir.no (hentet 2026-03-07)
- Kilder for finansiering: Digdir-rapporter, statsbudsjett (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

Ã¢Å“â€¦ **Brukersegmenter:** Struktur ut som tabell med konkrete behov, bruksomrÃƒÂ¥der og volum-estimater
Ã¢Å“â€¦ **Risikomatrise:** 8 konkrete risikokategorier med hÃƒÂ¥ndtering
Ã¢Å“â€¦ **Finansiering:** Detaljert kostnadsmodell (estimert 200-400 MNOK ÃƒÂ¥rlig)
Ã¢Å“â€¦ **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Digdir + Altinn-styre)
Ã¢Å“â€¦ **Veikart:** Konkrete fokusomrÃƒÂ¥der (Altinn 3-migrering, developer experience, event-driven, AI/ML)
Ã¢Å“â€¦ **Scope:** Eksplisitt tabell over hva som inngÃƒÂ¥r/ikke inngÃƒÂ¥r
Ã¢Å“â€¦ **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet (Studio, Apps, Portal, Formidling)
Ã¢Å“â€¦ **Strategisk kontekst:** Eksplisitt kobling til Altinn 3-modernisering og nasjonal strategi
Ã¢Å“â€¦ **Scale-dimensjon:** Tydelig at dette er landets viktigste plattform for digitale tjenester
Ã¢Å“â€¦ **Tegn-rettelser:** Korrigert fra "Maalgruppe" Ã¢â€ â€™ "MÃƒÂ¥lgruppe", "Hoy" Ã¢â€ â€™ "HÃƒÂ¸y"

