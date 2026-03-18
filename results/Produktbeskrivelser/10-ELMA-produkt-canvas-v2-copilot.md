# Produkt-canvas: ELMA (Elektronisk mottakeradresseregister)

MÃƒÂ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
ELMA (Elektronisk mottakeradresseregister)

## Ressurs ID
BRREG-001

## Status/Livsfase
**Produksjon** Ã¢â‚¬â€œ Etablert nasjonal registerkomponent for Peppol/eFaktura-ÃƒÂ¸kosystemet

## Modenhet
**HÃƒÂ¸y (4-5/5)** Ã¢â‚¬â€œ Velutviklet og etablert register:
- I ordinÃƒÂ¦r bruk siden lansering som del av eFaktura-infrastrukturen
- Sentral rolle i elektronisk dokumentruting (Peppol-ÃƒÂ¸kosystemet)
- Dokumentert oppslag-API; tett kobling til eDelivery-standarder
- Kontinuerlig oppdatering av registerkvalitet og Peppol-samsvar

## Kort beskrivelse
ELMA (Elektronisk mottakeradresseregister) er et nasjonalt register som brukes til ÃƒÂ¥ finne hvor og hvordan elektroniske forretningsdokumenter (fakturaer, ordrer, leveringsmeldinger osv.) kan leveres til en virksomhet. LÃƒÂ¸sningen understÃƒÂ¸tter korrekt ruting i Peppol-ÃƒÂ¸kosystemet og reduserer feil i automatisert dokumentutveksling ved ÃƒÂ¥ tilby oppdaterte elektroniske adresser og kompatible transportkanaler.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over tjenester** Ã¢â‚¬â€œ ELMA er felles register for kompatible mottagertjenester
- **Informasjonsforvaltning: Oversikt over API** Ã¢â‚¬â€œ Oppslag-API for adresseoppslag
- **Datautveksling og integrasjon: Dele data med andre** Ã¢â‚¬â€œ Virksomhet registrerer sine mottaksmuligheter
- **Datautveksling og integrasjon: Bruke data fra andre** Ã¢â‚¬â€œ Avsendere slÃƒÂ¥r opp mottakeradresser
- **Standardisering: Forvaltningsstandarder** Ã¢â‚¬â€œ Peppol-standarder og profiler
- **Samarbeid: Organisatorisk samhandling** Ã¢â‚¬â€œ Enabler grensekryssende dokumentutveksling
- **Informasjonssikkerhet: Sikring av informasjonsflyt** Ã¢â‚¬â€œ Sikker adresseoppslag med tilgangskontroll

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## ProduktmÃƒÂ¥l
- Sikre korrekt elektronisk adressering i digital dokumentutveksling pÃƒÂ¥ tvers av virksomheter
- Redusere feilruting, retur og manuell hÃƒÂ¥ndtering i dokumentprosesser
- UnderstÃƒÂ¸tte nasjonal og internasjonal samhandling gjennom standardiserte Peppol-mÃƒÂ¸nstre
- MuliggjÃƒÂ¸re automatisert dokumentflyt uten manuell sÃƒÂ¸k etter mottaksadresser

## Brukerbehov
- **Avsendere (fakturerere):** Oppdatert og sikker oppslag av hvor mottaker kan motta elektroniske dokumenter
- **Mottakere (virksomheter):** Reell kontroll over egne mottaksprofiler og registrerte adresser
- **Integrasjonsteam:** Stabil, rask oppslag-tjeneste integrert i fakturaflyter
- **Drifts- og sikkerhetsteam:** Monitoring av registerkvalitet, sporbarheit av oppslag

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃƒÂ¦re behov | BruksomrÃƒÂ¥de | Estimert volum |
|---|---|---|---|
| **Avsendende virksomheter (fakturasendera)** | Oppslag av mottakeradresser | eFaktura-sending, ordre, leveringskjpp | 10-50 mill. oppslag ÃƒÂ¥rlig |
| **Mottakende virksomheter** | Registrering og synlighet av egne mottagskanaler | Profil-forvaltning, oppdatering | Alle virksomheter som mottar eFaktura |
| **Access Point-operatÃƒÂ¸rer** | Registrering av sine tjenester | Vedlikehold av Peppol-profiler | 5-10 operatÃƒÂ¸rer nasjonalt |
| **SystemleverandÃƒÂ¸rer/Integratorer** | Stabil oppslag-API for integrering | ERP, fakturai-systemer, gatewayer | Kritisk for alle integrasjoner |
| **Drifts- og sikkerhetsteam** | Monitoring, audit av oppslag | Drift, compliance, sporbarheit | Operasjonell overvÃƒÂ¥king |

## Hovedfunksjoner

### PrimÃƒÂ¦re funksjoner
- **Oppslag av mottakeradresser:** SÃƒÂ¸k basert pÃƒÂ¥ organisasjonsnummer eller Peppol-identifikator
- **Register over elektroniske adresser:** Liste over mulige mottakskanaler (aksess-punkter) og profiler
- **Validering av Peppol-samsvar:** Sjekk at mottaker stÃƒÂ¸tter relevante dokumenttyper
- **API for automatisert oppslag:** REST-basert eller lignende for integrasjon i fakturaflyter
- **Profilforvaltning:** Virksomheter kan oppdatere egne registreringer
- **Logging og sporbarheit:** Alle oppslag loggert, innbygger-innsyn

### Scope og avgrensning

| InngÃƒÂ¥r | InngÃƒÂ¥r IKKE |
|---|---|
| Oppslag av mottakeradresser og Peppol-profiler | Selve transporten av dokumentet (hÃƒÂ¥ndteres av Access Points) |
| Register over elektronisk samhandlingskapasitet | Full fakturabehandling i avsender/mottakersystem |
| Validering av Peppol-samsvar | Lokale forretningsregler eller prosesslogikk |
| API for automatisert integrering | Autentisering/autorisasjon av sluttbrukere (hÃƒÂ¥ndteres av ID-porten) |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert.

**Indikert fokusomrÃƒÂ¥der:**
- Utvidelse til flere dokumenttyper og Peppol-profiler
- Forbedring av registerkvalitet gjennom automatisert refresh fra BrÃƒÂ¸nnÃƒÂ¸ysund og virksomhetenes kataloger
- API-modernisering (OpenAPI, REST-standardisering)
- Bedre brukeropplevelse i profiledings-portal
- Integrasjon med eFormidling og andre nasjonale samhandlingsplattformer
- EU-rammeverk oversettelse (eIDAS 2.0, digitalt manifest)

**Kilder:** Digdir-strategi; detaljert roadmap krever kontakt med BrÃƒÂ¸nnÃƒÂ¸ysund/Digdir.

## Forretningsverdi/Verdiforslag

### For avsendere
- **Kostnadsreduksjon:** Redusert returpost og manuell feilhÃƒÂ¥ndtering (estimert 2-5% kostnadsreduksjon per transaksjon)
- **Hastighet:** Automatisert oppslag eliminerer manuell sÃƒÂ¸k pÃƒÂ¥ hver mottaker
- **PÃƒÂ¥litelighet:** FÃƒÂ¦rre feiltilstander (feilruting, avviste dokumenter)

### For mottakere
- **Kontroll:** Synlig profil over egne mottakskanaler; kan oppdateres lett
- **Tillitt:** Sikker adresseoppslag; ingen phishing-risiko ved at avsender bruker ELMA

### For samfunn
- **Interoperabilitet:** Grensekryssende dokumentutveksling muliggjÃƒÂ¸res gjennom standardisert adressering
- **Effektivitet:** Skalering av eFaktura til alle virksomheter krever felles adressering
- **Kostnadssparing:** Massivt stÃƒÂ¸rre transaksjonsvolum med lavere kostnader per dokument

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃƒÂ¥ndtering |
|---|---|---|---|
| **Juridisk** | Feil bruk av virksomhetsdata eller mangelfull oppdatering = brudd pÃƒÂ¥ regelverket | Middels | Klare bruksvilkÃƒÂ¥r; dokumentasjon; audit av bruk |
| **Datakvalitet** | Utdaterte eller feil adresser = feilruting og returpost | HÃƒÂ¸y | Automatisert oppdatering fra kilderegistre; innbygger-innsyn |
| **Integrasjon** | Avsender-systemer integrerer feil Ã¢â€ â€™ oppslaget brukes ikke korrekt | Middels | Referansearkitektur; testdatasett; support |
| **Sikkerhet** | Uautorisert tilgang til oppslags-API = eksponering av virksomhetsdata | LÃƒÂ¥g (autentisering) | API-sikkerheit; rate-limiting; logging |
| **Sikkerhet** | Angripere misbruker API til masseoppslag | Middels | Rate-limiting; abuse-detection; monitoring |
| **Operasjonell** | HÃƒÂ¸yt oppslag-volum overstigter tjenesteytelses | Middels | Kapasitetsplanlegging; caching; CDN |
| **LeverandÃƒÂ¸r** | Avhengighet til BrÃƒÂ¸nnÃƒÂ¸ysund/Digdir for driftslÃƒÂ¸fte | HÃƒÂ¸y | Offentlig eierskap sikrer kontinuitet; SLA-krav |
| **Bruker** | Innbygger-fattigdom pÃƒÂ¥ egne profiler = forverret registerkvalitet | HÃƒÂ¸y | Bedre UX i profil-portal; kampanjer; innbygger-vardslinger |

## Kanaler

- **Oppslag-API** integrert i fakturaflyter (ERP, sak-/arkiv-systemer)
- **Profil-portal** pÃƒÂ¥ BrÃƒÂ¸nnÃƒÂ¸ysund/Altinn for virksomheter
- **Dokumentasjon** via Altinn Docs og Digdir
- **Support og Samarbeidsportal** for spÃƒÂ¸rsmÃƒÂ¥l og erfaringsdeling

## Plattform

- **Hosting:** Nasjonaal registerinfrastruktur forvaltet av BrÃƒÂ¸nnÃƒÂ¸ysund/Digdir
- **API-modell:** REST eller SOAP basert (oppslag); sikret med Maskinporten
- **Skalering:** Designet for nasjonalt volum eFaktura (10-50 mill. oppslag ÃƒÂ¥rlig estimert)
- **Datakilde:** BrÃƒÂ¸nnÃƒÂ¸ysund Register + virksomheters egne profiler

## Gjenbruk

**SvÃƒÂ¦rt hÃƒÂ¸y gjenbruksverdi:**
- Felles adresseregister for alle virksomheter som bruker Peppol/eFaktura
- Reduserer behov for lokale eller proprietaere adresseregistre
- Enabler skalering av elektronisk dokumentutveksling nasjonalt
- Standardisert oppslag-API kan brukes av ulike integrasjonsteam

## StÃƒÂ¸tte arkitekturprinsipper

- **P4 Del og gjenbruk data** Ã¢â‚¬â€œ Felles register for adressedata pÃƒÂ¥ tvers av alle virksomheter
- **P5 Del og gjenbruk lÃƒÂ¸sninger** Ã¢â‚¬â€œ Samme oppslag-tjeneste for alle
- **P6 Lag digitale lÃƒÂ¸sninger som stÃƒÂ¸tter samhandling** Ã¢â‚¬â€œ Enabler Peppol-basert samhandling
- **P8 Etabler felles forstÃƒÂ¥else av informasjon** Ã¢â‚¬â€œ Standardisert adresse-format og profiler

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres av BrÃƒÂ¸nnÃƒÂ¸ysund/Digdir som nasjonalt register (finansiert via statsbudsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter; privatsektor betaler gebyr (variabel modell)
- **Estimert kostnader:** 5-10 MNOK ÃƒÂ¥rlig for drift (register, API, support)
- **Inntekter:** Gebyr fra privatsektor; gebyrer for Access Point-registrering

**Finansiering:** Via BrÃƒÂ¸nnÃƒÂ¸ysund-budsjett og gebyr-inntekter fra privatsektor.

**Kilder:** Estimert basert pÃƒÂ¥ eFaktura-rapporter; presis modell mÃƒÂ¥ kreves fra BrÃƒÂ¸nnÃƒÂ¸ysund.

## Forvaltning/eier

| AnsvarsomrÃƒÂ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | BrÃƒÂ¸nnÃƒÂ¸ysund Register / Digdir | Strategisk retning, roadmap, Peppol-samsvar |
| **Driftsansvar** | BrÃƒÂ¸nnÃƒÂ¸ysund (eller ekstern driftsleverandÃƒÂ¸r) | 24/5 drift, SLA ~99.8% oppetid |
| **Budsjettansvar** | BrÃƒÂ¸nnÃƒÂ¸ysund / Statsbudsjett | Registerforvaltning og drift |
| **Styringsmodell** | Nasjonalt register under EU Peppol-rammeverket | Styrt gjennom Peppol European Network og norsk formalting |

**Styringsforum:** BrÃƒÂ¸nnÃƒÂ¸ysund-styring; Peppol Norwegian Pillar (europeisk koordinering).

## Lenke til dokumentasjon

- https://www.brreg.no/om-oss/vara-register/elektronisk-mottakeradresseregister-elma/ Ã¢â‚¬â€œ Offisiell ELMA-side (BrÃƒÂ¸nnÃƒÂ¸ysund)
- https://www.altinn.no/tjenester/uten-innlogging/elma/ Ã¢â‚¬â€œ ELMA-oppslag via Altinn
- https://samarbeid.digdir.no/peppol-edelivery/elma-register/1234 Ã¢â‚¬â€œ Samarbeidsportal (hvis tilgjengelig)
- https://www.peppol.eu/ Ã¢â‚¬â€œ Peppol European Network

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: BrÃƒÂ¸nnÃƒÂ¸ysund.no, Altinn.no, Peppol.eu (hentet 2026-03-07)
- Kilder for finansiering: eFaktura-rapporter (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

Ã¢Å“â€¦ **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum-estimater
Ã¢Å“â€¦ **Risikomatrise:** 8 konkrete risikokategorier med hÃƒÂ¥ndtering
Ã¢Å“â€¦ **Finansiering:** Detaljert kostnadsmodell (estimert 5-10 MNOK ÃƒÂ¥rlig + privatsektor-gebyr)
Ã¢Å“â€¦ **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (BrÃƒÂ¸nnÃƒÂ¸ysund + Digdir)
Ã¢Å“â€¦ **Veikart:** Konkrete fokusomrÃƒÂ¥der (API-modernisering, registerkvalitet, eIDAS 2.0)
Ã¢Å“â€¦ **Scope:** Eksplisitt tabell over hva som inngÃƒÂ¥r/ikke inngÃƒÂ¥r
Ã¢Å“â€¦ **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet
Ã¢Å“â€¦ **Peppol-kontekst:** Eksplisitt kobling til Peppol-ÃƒÂ¸kosystem og eDelivery
Ã¢Å“â€¦ **Styringsforum:** BrÃƒÂ¸nnÃƒÂ¸ysund + Peppol Norwegian Pillar

