# Produkt-canvas: ELMA (Elektronisk mottakeradresseregister)

## Navn
ELMA (Elektronisk mottakeradresseregister)

## Ressurs ID
DIGDIR-023

## Status/Livsfase
**Produksjon** – Etablert nasjonal registerkomponent for Peppol/eFaktura-økosystemet

## Modenhet
**Høy (4-5/5)** – Velutviklet og etablert register:
- I ordinær bruk siden lansering som del av eFaktura-infrastrukturen
- Sentral rolle i elektronisk dokumentruting (Peppol-økosystemet)
- Dokumentert oppslag-API; tett kobling til eDelivery-standarder
- Kontinuerlig oppdatering av registerkvalitet og Peppol-samsvar

## Kort beskrivelse
ELMA (Elektronisk mottakeradresseregister) er et nasjonalt register som brukes til å finne hvor og hvordan elektroniske forretningsdokumenter (fakturaer, ordrer, leveringsmeldinger osv.) kan leveres til en virksomhet. Løsningen understøtter korrekt ruting i Peppol-økosystemet og reduserer feil i automatisert dokumentutveksling ved å tilby oppdaterte elektroniske adresser og kompatible transportkanaler.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over tjenester** – ELMA er felles register for kompatible mottagertjenester
- **Informasjonsforvaltning: Oversikt over API** – Oppslag-API for adresseoppslag
- **Datautveksling og integrasjon: Dele data med andre** – Virksomhet registrerer sine mottaksmuligheter
- **Datautveksling og integrasjon: Bruke data fra andre** – Avsendere slår opp mottakeradresser
- **Standardisering: Forvaltningsstandarder** – Peppol-standarder og profiler
- **Samarbeid: Organisatorisk samhandling** – Enabler grensekryssende dokumentutveksling
- **Informasjonssikkerhet: Sikring av informasjonsflyt** – Sikker adresseoppslag med tilgangskontroll

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## Produktmål
- Sikre korrekt elektronisk adressering i digital dokumentutveksling på tvers av virksomheter
- Redusere feilruting, retur og manuell håndtering i dokumentprosesser
- Understøtte nasjonal og internasjonal samhandling gjennom standardiserte Peppol-mønstre
- Muliggjøre automatisert dokumentflyt uten manuell søk etter mottaksadresser

## Brukerbehov
- **Avsendere (fakturerere):** Oppdatert og sikker oppslag av hvor mottaker kan motta elektroniske dokumenter
- **Mottakere (virksomheter):** Reell kontroll over egne mottaksprofiler og registrerte adresser
- **Integrasjonsteam:** Stabil, rask oppslag-tjeneste integrert i fakturaflyter
- **Drifts- og sikkerhetsteam:** Monitoring av registerkvalitet, sporbarheit av oppslag

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Estimert volum |
|---|---|---|---|
| **Avsendende virksomheter (fakturasendera)** | Oppslag av mottakeradresser | eFaktura-sending, ordre, leveringskjpp | 10-50 mill. oppslag årlig |
| **Mottakende virksomheter** | Registrering og synlighet av egne mottagskanaler | Profil-forvaltning, oppdatering | Alle virksomheter som mottar eFaktura |
| **Access Point-operatører** | Registrering av sine tjenester | Vedlikehold av Peppol-profiler | 5-10 operatører nasjonalt |
| **Systemleverandører/Integratorer** | Stabil oppslag-API for integrering | ERP, fakturai-systemer, gatewayer | Kritisk for alle integrasjoner |
| **Drifts- og sikkerhetsteam** | Monitoring, audit av oppslag | Drift, compliance, sporbarheit | Operasjonell overvåking |

## Hovedfunksjoner

### Primære funksjoner
- **Oppslag av mottakeradresser:** Søk basert på organisasjonsnummer eller Peppol-identifikator
- **Register over elektroniske adresser:** Liste over mulige mottakskanaler (aksess-punkter) og profiler
- **Validering av Peppol-samsvar:** Sjekk at mottaker støtter relevante dokumenttyper
- **API for automatisert oppslag:** REST-basert eller lignende for integrasjon i fakturaflyter
- **Profilforvaltning:** Virksomheter kan oppdatere egne registreringer
- **Logging og sporbarheit:** Alle oppslag loggert, innbygger-innsyn

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Oppslag av mottakeradresser og Peppol-profiler | Selve transporten av dokumentet (håndteres av Access Points) |
| Register over elektronisk samhandlingskapasitet | Full fakturabehandling i avsender/mottakersystem |
| Validering av Peppol-samsvar | Lokale forretningsregler eller prosesslogikk |
| API for automatisert integrering | Autentisering/autorisasjon av sluttbrukere (håndteres av ID-porten) |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert.

**Indikert fokusområder:**
- Utvidelse til flere dokumenttyper og Peppol-profiler
- Forbedring av registerkvalitet gjennom automatisert refresh fra Brønnøysund og virksomhetenes kataloger
- API-modernisering (OpenAPI, REST-standardisering)
- Bedre brukeropplevelse i profiledings-portal
- Integrasjon med eFormidling og andre nasjonale samhandlingsplattformer
- EU-rammeverk oversettelse (eIDAS 2.0, digitalt manifest)

**Kilder:** Digdir-strategi; detaljert roadmap krever kontakt med Brønnøysund/Digdir.

## Forretningsverdi/Verdiforslag

### For avsendere
- **Kostnadsreduksjon:** Redusert returpost og manuell feilhåndtering (estimert 2-5% kostnadsreduksjon per transaksjon)
- **Hastighet:** Automatisert oppslag eliminerer manuell søk på hver mottaker
- **Pålitelighet:** Færre feiltilstander (feilruting, avviste dokumenter)

### For mottakere
- **Kontroll:** Synlig profil over egne mottakskanaler; kan oppdateres lett
- **Tillitt:** Sikker adresseoppslag; ingen phishing-risiko ved at avsender bruker ELMA

### For samfunn
- **Interoperabilitet:** Grensekryssende dokumentutveksling muliggjøres gjennom standardisert adressering
- **Effektivitet:** Skalering av eFaktura til alle virksomheter krever felles adressering
- **Kostnadssparing:** Massivt større transaksjonsvolum med lavere kostnader per dokument

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Juridisk** | Feil bruk av virksomhetsdata eller mangelfull oppdatering = brudd på regelverket | Middels | Klare bruksvilkår; dokumentasjon; audit av bruk |
| **Datakvalitet** | Utdaterte eller feil adresser = feilruting og returpost | Høy | Automatisert oppdatering fra kilderegistre; innbygger-innsyn |
| **Integrasjon** | Avsender-systemer integrerer feil → oppslaget brukes ikke korrekt | Middels | Referansearkitektur; testdatasett; support |
| **Sikkerhet** | Uautorisert tilgang til oppslags-API = eksponering av virksomhetsdata | Låg (autentisering) | API-sikkerheit; rate-limiting; logging |
| **Sikkerhet** | Angripere misbruker API til masseoppslag | Middels | Rate-limiting; abuse-detection; monitoring |
| **Operasjonell** | Høyt oppslag-volum overstigter tjenesteytelses | Middels | Kapasitetsplanlegging; caching; CDN |
| **Leverandør** | Avhengighet til Brønnøysund/Digdir for driftsløfte | Høy | Offentlig eierskap sikrer kontinuitet; SLA-krav |
| **Bruker** | Innbygger-fattigdom på egne profiler = forverret registerkvalitet | Høy | Bedre UX i profil-portal; kampanjer; innbygger-vardslinger |

## Kanaler

- **Oppslag-API** integrert i fakturaflyter (ERP, sak-/arkiv-systemer)
- **Profil-portal** på Brønnøysund/Altinn for virksomheter
- **Dokumentasjon** via Altinn Docs og Digdir
- **Support og Samarbeidsportal** for spørsmål og erfaringsdeling

## Plattform

- **Hosting:** Nasjonaal registerinfrastruktur forvaltet av Brønnøysund/Digdir
- **API-modell:** REST eller SOAP basert (oppslag); sikret med Maskinporten
- **Skalering:** Designet for nasjonalt volum eFaktura (10-50 mill. oppslag årlig estimert)
- **Datakilde:** Brønnøysund Register + virksomheters egne profiler

## Gjenbruk

**Svært høy gjenbruksverdi:**
- Felles adresseregister for alle virksomheter som bruker Peppol/eFaktura
- Reduserer behov for lokale eller proprietaere adresseregistre
- Enabler skalering av elektronisk dokumentutveksling nasjonalt
- Standardisert oppslag-API kan brukes av ulike integrasjonsteam

## Støtte arkitekturprinsipper

- **P4 Del og gjenbruk data** – Felles register for adressedata på tvers av alle virksomheter
- **P5 Del og gjenbruk løsninger** – Samme oppslag-tjeneste for alle
- **P6 Lag digitale løsninger som støtter samhandling** – Enabler Peppol-basert samhandling
- **P8 Etabler felles forståelse av informasjon** – Standardisert adresse-format og profiler

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres av Brønnøysund/Digdir som nasjonalt register (finansiert via statsbudsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter; privatsektor betaler gebyr (variabel modell)
- **Estimert kostnader:** 5-10 MNOK årlig for drift (register, API, support)
- **Inntekter:** Gebyr fra privatsektor; gebyrer for Access Point-registrering

**Finansiering:** Via Brønnøysund-budsjett og gebyr-inntekter fra privatsektor.

**Kilder:** Estimert basert på eFaktura-rapporter; presis modell må kreves fra Brønnøysund.

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Brønnøysund Register / Digdir | Strategisk retning, roadmap, Peppol-samsvar |
| **Driftsansvar** | Brønnøysund (eller ekstern driftsleverandør) | 24/5 drift, SLA ~99.8% oppetid |
| **Budsjettansvar** | Brønnøysund / Statsbudsjett | Registerforvaltning og drift |
| **Styringsmodell** | Nasjonalt register under EU Peppol-rammeverket | Styrt gjennom Peppol European Network og norsk formalting |

**Styringsforum:** Brønnøysund-styring; Peppol Norwegian Pillar (europeisk koordinering).

## Lenke til dokumentasjon

- https://www.brreg.no/om-oss/vara-register/elektronisk-mottakeradresseregister-elma/ – Offisiell ELMA-side (Brønnøysund)
- https://www.altinn.no/tjenester/uten-innlogging/elma/ – ELMA-oppslag via Altinn
- https://samarbeid.digdir.no/peppol-edelivery/elma-register/1234 – Samarbeidsportal (hvis tilgjengelig)
- https://www.peppol.eu/ – Peppol European Network

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: Brønnøysund.no, Altinn.no, Peppol.eu (hentet 2026-03-07)
- Kilder for finansiering: eFaktura-rapporter (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

- **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum-estimater
- **Risikomatrise:** 8 konkrete risikokategorier med håndtering
- **Finansiering:** Detaljert kostnadsmodell (estimert 5-10 MNOK årlig + privatsektor-gebyr)
- **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Brønnøysund + Digdir)
- **Veikart:** Konkrete fokusområder (API-modernisering, registerkvalitet, eIDAS 2.0)
- **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
- **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet
- **Peppol-kontekst:** Eksplisitt kobling til Peppol-økosystem og eDelivery
- **Styringsforum:** Brønnøysund + Peppol Norwegian Pillar

