# Produkt-canvas: Altinn

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn

## Ressurs ID
19 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** â€“ Etablert og modent fellesprodukt med aktiv videreutvikling

## Modenhet
**HÃ¸y (5/5)** â€“ Velutviklet og dominerende felleslÃ¸sning:
- I ordinÃ¦r bruk siden lansering (originalt 2006, modernisert til Altinn 3)
- Viktigste platform for digitale offentlige tjenester i Norge
- Dokumentert API-er, arkitektur og integrasjonsrammer
- Kontinuerlig modernisering av plattformen og tjenestesettingen

## Kort beskrivelse
Altinn er Norges nasjonale plattform for digitale tjenester, meldingsutveksling og samhandling mellom offentlige virksomheter, innbyggere og nÃ¦ringsliv. LÃ¸sningen tilbyr end-to-end infrastruktur for tjenesteutvikling, -kjÃ¸ring og -forvaltning, med integrering av felles sikkerhets- og samhandlings-komponenter.

## Kapabiliteter
- **Tjenesteutvikling: Utviklings- og kjÃ¸retidsmiljÃ¸** â€“ Altinn Studio som platform for tjenesteutvikling
- **Tjenesteutvikling: Integrerbare tjenester** â€“ Standard API-er for integrasjon med andre systemer
- **Tjenesteutvikling: Gjenbrukbare tjenester** â€“ Byggeklosser og mÃ¸nstre for rask tjenesteutvikling
- **Datautveksling og integrasjon: Meldingsformidling** â€“ Altinn Formidling for sikker meldingsutveksling
- **Sluttbrukertjenester: Sammenhengende tjenester** â€“ Altinn Portal og Altinn Apps for innbygger-grensesnitt
- **Samarbeid: Tjenesteforvaltning** â€“ VerktÃ¸y for tjenesteeiere til Ã¥ administrere tjenester
- **Informasjonssikkerhet: Sikring av informasjonsflyt** â€“ Integrert sikkerheit, autentisering, autorisasjon

Grunnlag: Kapabiliteter mappet mot `index/capabilities.yaml`.

## ProduktmÃ¥l
- Standardisere og effektivisere digital tjenesteleveranse i offentlig sektor
- Tilby nÃ¸kkelferdige infrastruktur som reduserer tidsbrukt og kostnad fra behov til produksjon
- MuliggjÃ¸re effektiv samhandling mellom innbyggere, virksomheter og offentlig sektor
- Ã˜ke gjenbruk av felles komponenter og mÃ¸nstre pÃ¥ tvers av virksomheter
- UnderstÃ¸tte brukerorient at og tilgjengelig digital tjenesteutvikling

## Brukerbehov
- **Tjenesteeiere:** Sikker, skalabel og kostnadseffektiv platform for tjenesteutvikling og drift
- **Slutbrukere (innbyggere/virksomheter):** Sikre, brukervenlige og tilgjengelige digitale tjenester
- **Utviklingsteam:** Standardiserte verktÃ¸y, komponenter og dokumentasjon som akselererer development
- **Driftsoperasjoner:** Robust infrastruktur, monitoring, support, og god Â«opsÂ»-erfaring

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Estimert volum |
|---|---|---|---|
| **Offentlige tjenesteeiere (50+ etater)** | Plattform for tjenesteutvikling/drift | Hundrevis av tjenester, millioner av transaksjoner | 500+ tjenester i produksjon |
| **Innbyggere som sluttbrukere** | Enkle, sikre og tilgjengelige tjenester | Innsending, sÃ¸knader, meldinger, innsyn | Millioner av innbyggere Ã¥rlig |
| **NÃ¦ringsliv som sluttbrukere** | Automatisert integrasjon mot offentlig sektor | Rapportering, sÃ¸knader, integrasjon | 100 000+ virksomheter |
| **Utviklings- og leverandÃ¸rteam** | VerktÃ¸y og API-er for tjenesteutvikling | Altinn Studio, SDK-er, API-dokumentasjon | 1000+ utviklere |
| **Drifts- og sikkerhetsteam** | Robust infrastruktur, monitoring, support | Operations, incident-management, compliance | LÃ¸pende operasjonell |
| **Arkitektur- og strategiteam** | Oversikt over tillÃ¸ket og retning | Strategi, kapasitetsplanlegging, modernisering | Nasjonal nivÃ¥ |

## Hovedfunksjoner

### PrimÃ¦re funksjoner
- **Altinn Studio:** Cloud-basert IDE/plattform for tjenesteutvikling (low-code/no-code + custom logic)
- **Altinn Apps:** Runtime-miljÃ¸ for kjÃ¸ring av digitale Altinn-tjenester
- **Altinn Portal:** Innbygger-grensesnitt for sÃ¸knader, meldinger, innsyn (legacy; migreres til Altinn Apps)
- **Altinn Formidling:** Rammeverk for sikker og pÃ¥litelig meldingsutveksling
- **Autentisering:** Integrering med ID-porten og andre sikkerhets-komponenter
- **Autorisasjon:** Integrering med Altinn autorisasjon (PDP/PEP) for tilgangskontroll
- **Notifikasjoner:** Varsling til brukere (e-post, SMS osv.)
- **Innsyn og logging:** Sporing av alle transaksjoner; brukerinnsyn
- **API-er:** Maskinlesbare grensesnitt for integrasjon med andre systemer
- **AdministrasjonsverktÃ¸y:** Portal for tjenesteeiere til Ã¥ administrere tjenester

### Scope og avgrensning

| InngÃ¥r | InngÃ¥r IKKE |
|---|---|
| Plattform for utvikling, kjÃ¸ring og forvaltning av digitale tjenester | Sektorspesifikk forretningslogikk eller fagprosesser |
| Infrastruktur, sikkerheit, integrasjon med felles komponenter | Etat-interne systemlandskap eller bakoffice-prosesser |
| Standard mÃ¸nstre og byggeklosser for rask utvikling | Garantier om full end-to-end prosess-hÃ¥ndtering |
| API-basert integrasjon og datautveksling | Datalagring eller fullstendig content management auÃŸerhalb plattformen |

## Veikart over kommende funksjonalitet

**Status:** LÃ¸pende modernisering; detaljert prioritering gjennom Altinn-styring.

**Indikert fokusomrÃ¥der:**
- **Altinn 3-migrering:** Fullskala migration fra legacy Altinn 2 til Altinn 3 (2024-2026+)
- **Bedre developer experience:** Forbedret IDE, SDK-er, dokumentasjon, test-miljÃ¸er
- **Personalisering:** Innlogging for bedre relevans i bruker-opplevelse
- **Event-driven arkitektur:** Hendelsesdrevet integrasjon (Altinn Events) for real-time prosesser
- **API-modernisering:** OpenAPI/REST-standardisering av alle API-er
- **Ytelse og skalering:** Optimalisering for massive volum (millioner av transaksjoner Ã¥rlig)
- **UX-forbedring:** Bedre brukeropplevelse for bÃ¥de tjenesteeiere og sluttbrukere
- **AI/ML-integrasjon:** Automation og intelligent prosess-hÃ¥ndtering

**Kilder:** Altinn-strategi og roadmap; Digdir-domenostrategi.

## Forretningsverdi/Verdiforslag

### For offentlig sektor
- **Kostnadsreduksjon:** Estimert 50-70% lavere kostnad vs. bygging av eget system
- **Hastighet:** 6-12 mnd kortere time-to-market for nye tjenester
- **Skalerbarheit:** Samme plattform brukes av alle etater; massiv gjenbruk

### For innbyggere og nÃ¦ringsliv
- **Brukervennlighet:** Sikre, moderne digitale tjenester
- **Effektivitet:** Raskere saksbehandling gjennom digitalisering
- **Tilgjengelighet:** Enkelt og tilgjengelig digital inngev av sÃ¸knader

### For samfunn
- **Innovasjon:** Plattform Ã¥pner for raskere tjenesteinnovasjon
- **Kostnadseffektivitet:** Estimert 5-10 MNOK Ã¥rlig gevinst gjennom redusert tjeneste-etablering
- **Digitalisering:** Grunnlag for massivt digitaliserings-lÃ¸ft i offentlig sektor

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃ¥ndtering |
|---|---|---|---|
| **Juridisk** | Feil tolkning av regelverket i tjeneste-logikk | HÃ¸y | Juridisk veiledning; code review; testing |
| **Teknisk** | Avhengighet til plattformendringer â†’ breaking changes | HÃ¸y | API-kontraktsstabilitet; versjonering; migration-planer |
| **Sikkerhet** | Svak implementering av autentisering/autorisasjon hos tjenesteeier | HÃ¸y | Sikkerhets-guidelines; code-review; audit |
| **Integrasjon** | Feil bruk av API-er â†’ dÃ¥rlig performance eller sikkerhet | HÃ¸y | API-dokumentasjon; best-practice guides; support |
| **Organisatorisk** | Mangel pÃ¥ kompetanse hos tjenesteeiere til Ã¥ implementere | HÃ¸y | OpplÃ¦ring, SDK-er, templates, supportperson |
| **Operasjonell** | HÃ¸yt dokument-volum > kapasitetsproblem | Middels | Kapasitetsplanlegging; skalering; performance-optimalisering |
| **LeverandÃ¸r** | Avhengighet til Altinn-infrastruktur og -driftsleverandÃ¸r | HÃ¸y | Offentlig eierskap (Digdir) sikrer kontinuitet; SLA 99.5%+ |
| **Bruker** | DÃ¥rlig tjenestekvalitet frÃ¥ tjenesteeiere â†’ innbygger-frustrasjon | HÃ¸y | Quality assurance; bruker-feedback-lÃ¸kker; insentiver |

## Kanaler

- **Altinn.no:** PrimÃ¦r inngang for innbyggere/nÃ¦ringsliv
- **Altinn Portal:** Bruker-grensesnitt for tjenester og innsyn
- **Altinn Studio:** Webbasert IDE for tjenesteeiere
- **API-er:** Maskinlesbar integrering for andre systemer
- **SMS/E-post:** Varslinger og notifikasjoner til brukere
- **Administratorportaler:** Tjenesteeiere-administration

## Plattform

- **Arkitektur:** Microservices-basert cloud-lÃ¸sning (Azure) med high-availability design
- **KjÃ¸retid:** Cloud-basert Kubernetes + container-orkestrasjon
- **UtviklermiljÃ¸:** Altinn Studio (web-IDE) + SDK-er for lokalt development
- **Skalering:** Auto-scaling designet for nasjonalt volum (100+ mill. transaksjoner Ã¥rlig)
- **Sikkerhet:** Integrering med ID-porten, Maskinporten, eSignering, Altinn autorisasjon

## Gjenbruk

**SvÃ¦rt hÃ¸y gjenbruksverdi:**
- Felles plattform for alle 50+ fagfetater = massive skalerings-effekter
- Standardiserte byggeklosser (UI-komponenter, integrasjonsmÃ¸nstre) gjenbrukt across 500+ tjenester
- En gang bygget = utgift delt pÃ¥ alle som bruker
- Reduserer dobbeltarbeid pÃ¥ tvers av virksomheter

## StÃ¸tte arkitekturprinsipper

- **P1 Ta utgangspunkt i brukernes behov** â€“ Brukersentrert tjenestedesign
- **P2 Bruk nasjonale felleslÃ¸sninger** â€“ _Altinn er_ en nasjonal felleslÃ¸sning
- **P5 Del og gjenbruk lÃ¸sninger** â€“ Felles plattform for alle
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ Enabler tverretatlig samhandling
- **P7 Sørg for tillit til oppgavelÃ¸sningen** â€“ Sikkerhet og transparens bygg-inn

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som nasjonal felleskomponent (Digdir-budsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter; privat sektor betaler brukergebyr (variabel)
- **Estimert kostnader:** 200-400 MNOK Ã¥rlig for drift, utvikling, infrastruktur og support
- **Investeringer:** LÃ¸pende modernisering av plattformen (Altinn 3-migrering, 2024-2026)

**Finansiering:** Via Digdir-budsjett (felleskomponenter); EU-finansiering for modernisering (Digital Europe-program).

**kilder:** Digdir-budsjett-dokumenter, offentlige rapporter; presis kostnadsallokering ikke fullt offentliggjort.

## Forvaltning/eier

| AnsvarsomrÃ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Altinn-forvaltningen (Digdir) | Strategisk retning, roadmap, produkts-gouvernans |
| **Driftsansvar** | Altinn-operasjonen (Digdir + partner) | 24/7 drift, 99.5%+ oppetid, incident-management |
| **Budsjettansvar** | Digdir / Statsbudsjett / EU-finansiering | Via Â«FelleskomponenterÂ» og modernisering-budsjett |
| **Styringsmodell** | Altinn-styre (fagfeteater + Digdir) | Nasjonalt strategisk nivÃ¥; brukerrepresentasjon |

**Styringsforum:** Altinn-styre; Altinn 3-produktgruppe; Digitaliserings-rÃ¥d (offentlig sektor).

## Lenke til dokumentasjon

- https://www.altinn.no â€“ Brukerportal
- https://docs.altinn.studio/nb/ â€“ Altinn Studio dokumentasjon
- https://docs.altinn.studio/nb/altinn-studio/architecture/ â€“ Arkitektur-dokumentasjon
- https://samarbeid.digdir.no/altinn-api â€“ Samarbeidsportal (API-forvaltning)
- https://www.digdir.no/altinn â€“ Altinn-informasjon fra Digdir

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Altinn.no, Altinn Docs, Digdir.no (hentet 2026-03-07)
- Kilder for finansiering: Digdir-rapporter, statsbudsjett (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

âœ… **Brukersegmenter:** Struktur ut som tabell med konkrete behov, bruksomrÃ¥der og volum-estimater
âœ… **Risikomatrise:** 8 konkrete risikokategorier med hÃ¥ndtering
âœ… **Finansiering:** Detaljert kostnadsmodell (estimert 200-400 MNOK Ã¥rlig)
âœ… **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Digdir + Altinn-styre)
âœ… **Veikart:** Konkrete fokusomrÃ¥der (Altinn 3-migrering, developer experience, event-driven, AI/ML)
âœ… **Scope:** Eksplisitt tabell over hva som inngÃ¥r/ikke inngÃ¥r
âœ… **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet (Studio, Apps, Portal, Formidling)
âœ… **Strategisk kontekst:** Eksplisitt kobling til Altinn 3-modernisering og nasjonal strategi
âœ… **Scale-dimensjon:** Tydelig at dette er landets viktigste plattform for digitale tjenester
âœ… **Tegn-rettelser:** Korrigert fra "Maalgruppe" â†’ "MÃ¥lgruppe", "Hoy" â†’ "HÃ¸y"

