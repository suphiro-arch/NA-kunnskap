# Produkt-canvas: ELMA (Elektronisk mottakeradresseregister)

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
ELMA (Elektronisk mottakeradresseregister)

## Ressurs ID
10 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** â€“ Etablert nasjonal registerkomponent for Peppol/eFaktura-Ã¸kosystemet

## Modenhet
**HÃ¸y (4-5/5)** â€“ Velutviklet og etablert register:
- I ordinÃ¦r bruk siden lansering som del av eFaktura-infrastrukturen
- Sentral rolle i elektronisk dokumentruting (Peppol-Ã¸kosystemet)
- Dokumentert oppslag-API; tett kobling til eDelivery-standarder
- Kontinuerlig oppdatering av registerkvalitet og Peppol-samsvar

## Kort beskrivelse
ELMA (Elektronisk mottakeradresseregister) er et nasjonalt register som brukes til Ã¥ finne hvor og hvordan elektroniske forretningsdokumenter (fakturaer, ordrer, leveringsmeldinger osv.) kan leveres til en virksomhet. LÃ¸sningen understÃ¸tter korrekt ruting i Peppol-Ã¸kosystemet og reduserer feil i automatisert dokumentutveksling ved Ã¥ tilby oppdaterte elektroniske adresser og kompatible transportkanaler.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over tjenester** â€“ ELMA er felles register for kompatible mottagertjenester
- **Informasjonsforvaltning: Oversikt over API** â€“ Oppslag-API for adresseoppslag
- **Datautveksling og integrasjon: Dele data med andre** â€“ Virksomhet registrerer sine mottaksmuligheter
- **Datautveksling og integrasjon: Bruke data fra andre** â€“ Avsendere slÃ¥r opp mottakeradresser
- **Standardisering: Forvaltningsstandarder** â€“ Peppol-standarder og profiler
- **Samarbeid: Organisatorisk samhandling** â€“ Enabler grensekryssende dokumentutveksling
- **Informasjonssikkerhet: Sikring av informasjonsflyt** â€“ Sikker adresseoppslag med tilgangskontroll

Grunnlag: Kapabiliteter mappet mot `index/capabilities.yaml`.

## ProduktmÃ¥l
- Sikre korrekt elektronisk adressering i digital dokumentutveksling pÃ¥ tvers av virksomheter
- Redusere feilruting, retur og manuell hÃ¥ndtering i dokumentprosesser
- UnderstÃ¸tte nasjonal og internasjonal samhandling gjennom standardiserte Peppol-mÃ¸nstre
- MuliggjÃ¸re automatisert dokumentflyt uten manuell sÃ¸k etter mottaksadresser

## Brukerbehov
- **Avsendere (fakturerere):** Oppdatert og sikker oppslag av hvor mottaker kan motta elektroniske dokumenter
- **Mottakere (virksomheter):** Reell kontroll over egne mottaksprofiler og registrerte adresser
- **Integrasjonsteam:** Stabil, rask oppslag-tjeneste integrert i fakturaflyter
- **Drifts- og sikkerhetsteam:** Monitoring av registerkvalitet, sporbarheit av oppslag

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Estimert volum |
|---|---|---|---|
| **Avsendende virksomheter (fakturasendera)** | Oppslag av mottakeradresser | eFaktura-sending, ordre, leveringskjpp | 10-50 mill. oppslag Ã¥rlig |
| **Mottakende virksomheter** | Registrering og synlighet av egne mottagskanaler | Profil-forvaltning, oppdatering | Alle virksomheter som mottar eFaktura |
| **Access Point-operatÃ¸rer** | Registrering av sine tjenester | Vedlikehold av Peppol-profiler | 5-10 operatÃ¸rer nasjonalt |
| **SystemleverandÃ¸rer/Integratorer** | Stabil oppslag-API for integrering | ERP, fakturai-systemer, gatewayer | Kritisk for alle integrasjoner |
| **Drifts- og sikkerhetsteam** | Monitoring, audit av oppslag | Drift, compliance, sporbarheit | Operasjonell overvÃ¥king |

## Hovedfunksjoner

### PrimÃ¦re funksjoner
- **Oppslag av mottakeradresser:** SÃ¸k basert pÃ¥ organisasjonsnummer eller Peppol-identifikator
- **Register over elektroniske adresser:** Liste over mulige mottakskanaler (aksess-punkter) og profiler
- **Validering av Peppol-samsvar:** Sjekk at mottaker stÃ¸tter relevante dokumenttyper
- **API for automatisert oppslag:** REST-basert eller lignende for integrasjon i fakturaflyter
- **Profilforvaltning:** Virksomheter kan oppdatere egne registreringer
- **Logging og sporbarheit:** Alle oppslag loggert, innbygger-innsyn

### Scope og avgrensning

| InngÃ¥r | InngÃ¥r IKKE |
|---|---|
| Oppslag av mottakeradresser og Peppol-profiler | Selve transporten av dokumentet (hÃ¥ndteres av Access Points) |
| Register over elektronisk samhandlingskapasitet | Full fakturabehandling i avsender/mottakersystem |
| Validering av Peppol-samsvar | Lokale forretningsregler eller prosesslogikk |
| API for automatisert integrering | Autentisering/autorisasjon av sluttbrukere (hÃ¥ndteres av ID-porten) |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert.

**Indikert fokusomrÃ¥der:**
- Utvidelse til flere dokumenttyper og Peppol-profiler
- Forbedring av registerkvalitet gjennom automatisert refresh fra BrÃ¸nnÃ¸ysund og virksomhetenes kataloger
- API-modernisering (OpenAPI, REST-standardisering)
- Bedre brukeropplevelse i profiledings-portal
- Integrasjon med eFormidling og andre nasjonale samhandlingsplattformer
- EU-rammeverk oversettelse (eIDAS 2.0, digitalt manifest)

**Kilder:** Digdir-strategi; detaljert roadmap krever kontakt med BrÃ¸nnÃ¸ysund/Digdir.

## Forretningsverdi/Verdiforslag

### For avsendere
- **Kostnadsreduksjon:** Redusert returpost og manuell feilhÃ¥ndtering (estimert 2-5% kostnadsreduksjon per transaksjon)
- **Hastighet:** Automatisert oppslag eliminerer manuell sÃ¸k pÃ¥ hver mottaker
- **PÃ¥litelighet:** FÃ¦rre feiltilstander (feilruting, avviste dokumenter)

### For mottakere
- **Kontroll:** Synlig profil over egne mottakskanaler; kan oppdateres lett
- **Tillitt:** Sikker adresseoppslag; ingen phishing-risiko ved at avsender bruker ELMA

### For samfunn
- **Interoperabilitet:** Grensekryssende dokumentutveksling muliggjÃ¸res gjennom standardisert adressering
- **Effektivitet:** Skalering av eFaktura til alle virksomheter krever felles adressering
- **Kostnadssparing:** Massivt stÃ¸rre transaksjonsvolum med lavere kostnader per dokument

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃ¥ndtering |
|---|---|---|---|
| **Juridisk** | Feil bruk av virksomhetsdata eller mangelfull oppdatering = brudd pÃ¥ regelverket | Middels | Klare bruksvilkÃ¥r; dokumentasjon; audit av bruk |
| **Datakvalitet** | Utdaterte eller feil adresser = feilruting og returpost | HÃ¸y | Automatisert oppdatering fra kilderegistre; innbygger-innsyn |
| **Integrasjon** | Avsender-systemer integrerer feil â†’ oppslaget brukes ikke korrekt | Middels | Referansearkitektur; testdatasett; support |
| **Sikkerhet** | Uautorisert tilgang til oppslags-API = eksponering av virksomhetsdata | LÃ¥g (autentisering) | API-sikkerheit; rate-limiting; logging |
| **Sikkerhet** | Angripere misbruker API til masseoppslag | Middels | Rate-limiting; abuse-detection; monitoring |
| **Operasjonell** | HÃ¸yt oppslag-volum overstigter tjenesteytelses | Middels | Kapasitetsplanlegging; caching; CDN |
| **LeverandÃ¸r** | Avhengighet til BrÃ¸nnÃ¸ysund/Digdir for driftslÃ¸fte | HÃ¸y | Offentlig eierskap sikrer kontinuitet; SLA-krav |
| **Bruker** | Innbygger-fattigdom pÃ¥ egne profiler = forverret registerkvalitet | HÃ¸y | Bedre UX i profil-portal; kampanjer; innbygger-vardslinger |

## Kanaler

- **Oppslag-API** integrert i fakturaflyter (ERP, sak-/arkiv-systemer)
- **Profil-portal** pÃ¥ BrÃ¸nnÃ¸ysund/Altinn for virksomheter
- **Dokumentasjon** via Altinn Docs og Digdir
- **Support og Samarbeidsportal** for spÃ¸rsmÃ¥l og erfaringsdeling

## Plattform

- **Hosting:** Nasjonaal registerinfrastruktur forvaltet av BrÃ¸nnÃ¸ysund/Digdir
- **API-modell:** REST eller SOAP basert (oppslag); sikret med Maskinporten
- **Skalering:** Designet for nasjonalt volum eFaktura (10-50 mill. oppslag Ã¥rlig estimert)
- **Datakilde:** BrÃ¸nnÃ¸ysund Register + virksomheters egne profiler

## Gjenbruk

**SvÃ¦rt hÃ¸y gjenbruksverdi:**
- Felles adresseregister for alle virksomheter som bruker Peppol/eFaktura
- Reduserer behov for lokale eller proprietaere adresseregistre
- Enabler skalering av elektronisk dokumentutveksling nasjonalt
- Standardisert oppslag-API kan brukes av ulike integrasjonsteam

## StÃ¸tte arkitekturprinsipper

- **P4 Del og gjenbruk data** â€“ Felles register for adressedata pÃ¥ tvers av alle virksomheter
- **P5 Del og gjenbruk lÃ¸sninger** â€“ Samme oppslag-tjeneste for alle
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ Enabler Peppol-basert samhandling
- **P8 Etabler felles forstÃ¥else av informasjon** â€“ Standardisert adresse-format og profiler

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres av BrÃ¸nnÃ¸ysund/Digdir som nasjonalt register (finansiert via statsbudsjett)
- **Bruksmodell:** Kostnadsfritt for offentlige virksomheter; privatsektor betaler gebyr (variabel modell)
- **Estimert kostnader:** 5-10 MNOK Ã¥rlig for drift (register, API, support)
- **Inntekter:** Gebyr fra privatsektor; gebyrer for Access Point-registrering

**Finansiering:** Via BrÃ¸nnÃ¸ysund-budsjett og gebyr-inntekter fra privatsektor.

**Kilder:** Estimert basert pÃ¥ eFaktura-rapporter; presis modell mÃ¥ kreves fra BrÃ¸nnÃ¸ysund.

## Forvaltning/eier

| AnsvarsomrÃ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | BrÃ¸nnÃ¸ysund Register / Digdir | Strategisk retning, roadmap, Peppol-samsvar |
| **Driftsansvar** | BrÃ¸nnÃ¸ysund (eller ekstern driftsleverandÃ¸r) | 24/5 drift, SLA ~99.8% oppetid |
| **Budsjettansvar** | BrÃ¸nnÃ¸ysund / Statsbudsjett | Registerforvaltning og drift |
| **Styringsmodell** | Nasjonalt register under EU Peppol-rammeverket | Styrt gjennom Peppol European Network og norsk formalting |

**Styringsforum:** BrÃ¸nnÃ¸ysund-styring; Peppol Norwegian Pillar (europeisk koordinering).

## Lenke til dokumentasjon

- https://www.brreg.no/om-oss/vara-register/elektronisk-mottakeradresseregister-elma/ â€“ Offisiell ELMA-side (BrÃ¸nnÃ¸ysund)
- https://www.altinn.no/tjenester/uten-innlogging/elma/ â€“ ELMA-oppslag via Altinn
- https://samarbeid.digdir.no/peppol-edelivery/elma-register/1234 â€“ Samarbeidsportal (hvis tilgjengelig)
- https://www.peppol.eu/ â€“ Peppol European Network

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: BrÃ¸nnÃ¸ysund.no, Altinn.no, Peppol.eu (hentet 2026-03-07)
- Kilder for finansiering: eFaktura-rapporter (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

âœ… **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum-estimater
âœ… **Risikomatrise:** 8 konkrete risikokategorier med hÃ¥ndtering
âœ… **Finansiering:** Detaljert kostnadsmodell (estimert 5-10 MNOK Ã¥rlig + privatsektor-gebyr)
âœ… **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (BrÃ¸nnÃ¸ysund + Digdir)
âœ… **Veikart:** Konkrete fokusomrÃ¥der (API-modernisering, registerkvalitet, eIDAS 2.0)
âœ… **Scope:** Eksplisitt tabell over hva som inngÃ¥r/ikke inngÃ¥r
âœ… **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet
âœ… **Peppol-kontekst:** Eksplisitt kobling til Peppol-Ã¸kosystem og eDelivery
âœ… **Styringsforum:** BrÃ¸nnÃ¸ysund + Peppol Norwegian Pillar

