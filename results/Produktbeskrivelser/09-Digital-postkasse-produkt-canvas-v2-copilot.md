# Produkt-canvas: Digital postkasse

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Digital postkasse (felleskomponent)

## Ressurs ID
9 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** – Etablert nasjonal felleskomponent for innbygger digital post

## Modenhet
**Høy (4-5/5)** – Etablert og moden felleskomponent:
- I aktiv bruk siden 2012 (Posten Norge AS / Digital Post / Digipost)
- Lovpålagt mottakskanal for offentlig post (jf. Públil Informatiserte sikring fra 2015 og forløpende forpliktninger)
- Stabil API med dokumentert bruksvilkår
- Utbredt integrasjon i offentlige fagsystemer

## Kort beskrivelse
Digital postkasse er nasjonal felleskomponent for sikker digital utsending av vedtak, informasjon og annen post fra offentlige virksomheter til innbyggere. Løsningen erstatter papirbasert post for mange dokumenttyper og gir innbyggere en samlet digital innboks med sporbar og sikker levering.

## Kapabiliteter
- **Datautveksling og integrasjon:** Meldingsformidling – Sikker transport av post fra avsender til innbygger
- **Datautveksling og integrasjon:** Dele data med andre – Integrering med offentlige fagsystemer
- **Tillit:** Sporbarhet og innsyn – Loggering av all post og leveringsstatus
- **Sluttbrukertjenester:** Sammenhengende tjenester – Innbyggers sentrale innboks for offentlig post
- **Informasjonssikkerhet:** Sikring av informasjonsflyt og datautveksling – Kryptering, autentisering, tilgangskontroll

Grunnlag: Kapabiliteter mappet mot `index/capabilities.yaml`.

## Produktmål
- Muliggjøre sikker, papirløs digital utsending av vedtak og post fra offentlig sektor til innbyggere
- Redusere kostnader knyttet til manuell håndtering, porto og returpost
- Gi innbyggere mer tilgjengelig og sporbar digital dialog med forvaltningen
- Sikre rettslig gyldig og sikker levering av juridisk bindende dokumenter

## Brukerbehov
- **Offentlige virksomheter:** Sikker og kostnadseffektiv distribusjon av vedtak, informasjon og post
- **Innbyggere:** Enkel tilgang til postinnboks, sikkerhet, og mulighet for historikk
- **Fagsystemleverandører:** Standardisert integrasjon for utsendelse fra sak-/arkiv-/fagsystemer
- **Drifts- og sikkerhetsmiljøer:** Overvåking av leveranser, sporbarhet, compliance

## Hvem er brukerne og brukersegmentene

| Brukersegment | Behov | Bruksområde | Estimert volum |
|---|---|---|---|
| **Avsendende offentlige virksomheter** | Sikker distribusjon av vedtak og post | Vedtak, brev, infobrev | 50-100 mill. brev årlig |
| **Innbyggere (mottakere)** | digitalt tilgjengelig innboks | Mottak og arkivering av vedtak | Passiv, men veldig viktig |
| **Fagsystemleverandører** | Stabile integrasjons-API | Integrasjon i sak-/arkiv-/lønn-systemer | Kritisk for distribusjonsprosesser |
| **Drifts- og sikkerhetsteam** | Overvåking, sporbarhet, SLA-rapport | Drift, security, compliance | Operasjonell overvåking |
| **Privatsektorer** | Sikker post til kundeinnboks (begrenset) | B2C-post, varsling | Voksende segment |

## Hovedfunksjoner

### Primære funksjoner
- **Avsending av post:** API for offentlige virksomheter til å sende dokumenter til innbyggeres postkasse
- **Innbygger-innboks:** Digitale postkasse hvor innbygger mottaker, leser og arkiverer post
- **Leveringssikkerhet:** Kvittering på levering, feilhåndtering og gjenforsøk
- **Sikkerhet:** Autentisering via eID, kryptering av innhold, tilgangskontroll
- **Historikk og søk:** Innbygger kan søke i tidligere mottatt post
- **Integrasjon med offentlige systemer:** Standard API for sak-/arkiv-/fagsystemer

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Digital post-distribusjon fra avsender til innbygger | Fysisk postdistribusjon (bygger på papirbude for hybrid) |
| Innbygger-postkasse og historikk | Innholdsgenereringsprosess i avsender-systemet (det er fagsystem-ansvar) |
| Autentisering av innbygger og tilgangskontroll | Autentisering av avsender (håndteres via andre komponenter) |
| Kvittering, status og sporbarhet | Full saksbehandlingsprosess eller arkivering på sender-siden |
| Fallback til papir hvis innbygger ikke har digital postkasse | Innsamling av målepunkter eller analytics |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert.

**Indikert utvikling (basert på strategi):**
- Utvidelse av sakstypologi (hybrid post, varslingen, betalinger)
- Forbedret brukeropplevelse i innbygger-portalen
- Modernisering av integrasjons-API (evt. OpenAPI-standard)
- Støtte for nye autentiseringsmåter og eID-standarder
- Reduksjon av hybridpostvolum gjennom økt digital dekningsgrad
- Integrasjon med andre innbygger-tjenester (og KRR for kontaktvalg)

**Kilder:** Digdir strategidokumenter; detaljert planlegging krever Digdir-kontakt.

## Forretningsverdi/Verdiforslag

### For innbyggere
- Sentral digital innboks for offentlig post
- Sikker og sporbar leveranse av juridisk viktige dokumenter
- Mulighet for å bevare og søke i historikk

### For offentlige virksomheter
- **Kostnadsreduksjon:** 5-10 kr per brev i porto og fysisk håndtering + reduserte returner
- **Effektivitet:** Automatsik distribusjon uten manuel porto-håndtering
- **Compliance:** Bevaring av dokumenter av juridisk karakter; sporbarhet

### For samfunn
- Muliggjør papiløs, digitalt first-strategi for offentlig kommunikasjon
- Redusert miljøpåvirkning ved papirreduksjonen
- Sterkere tillit til digital forvaltning

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Juridisk** | Feil tolking av leveringspunktet = juridisk usikkerhet | Middels | Klare definisjoner; notariethet av leveringssporing |
| **Integrasjon** | Avsender-systemer integrerer feil → post ikke sendt/duplikater | Middels | Referansearkitektur; testdata; support fra Digdir |
| **Datakvalitet** | Feil adressedata eller mottaker-identifisering | Høy | Relasjon til KRR; validering av fnr./adresse før utsending |
| **Sikkerhet** | Uautorisert tilgang til postinnboks | Låg (eID-kreves) | Sterk autentisering; logging av all tilgang |
| **Sikkerhet** | Personvernbrudd eller lekkasje av post-innhold | Låg | Kryptering end-to-end; sikker fysisk infrastruktur |
| **Operasjonell** | Høyt avsendingsvolum overstigger kapasitet | Middels | Skalering; kapasitetsplanlegging; fallback-rutiner |
| **Brukeropplevelse** | Innbygger-digitalisering ikke oppnådd → papirfallback fortsatt nødvendig | Høy | Kampanjer for digital omstilling; fallback til hybrid post |
| **Leverandør** | Avhengighet til driftsleverandør (Posten) | Høy | Digdir som produkt-eier; redundans-krav; SLA-krav |

## Kanaler

- **API for avsendelse** fra offentlige fagsystemer (integrert i sak-/arkiv-systemer)
- **Innbygger-portal** (postkasse.no eller Digipost)
- **Informasjonskanaler** via Digdir.no og Samarbeidsportalen
- **Support og dokumentasjon** fra Digdir og Posten

## Plattform

- **Leverandør:** Posten Norge AS (on behalf of Digdir)
- **Hosting:** Sky-basert multi-tenant løsning
- **API-modell:** REST/SOAP (proprietary, men dokumentert)
- **Skalering:** Designet for nasjonalt volum (50-100 mill. brev årlig)
- **Autentisering:** eID for innbygger; Maskinporten/autorisasjon for avsender-systemer
- **Sikkerhet:** TLS-kryptering; kryptert lagring; sikre api-niveå-kall

## Gjenbruk

**Svært høy gjenbruksverdi:**
- Felles mottakskanal for alle offentlige virksomheter (kommuner, stat, direktorater)
- Reduserer duplisering av postsystem-funksjonalitet
- Muliggjør standardisert distribusjon uten lokale løsninger
- Lovpålagt for mange sektorer, dermed felles juridisk grunnlag

## Støtte arkitekturprinsipper

- **P1 Ta utgangspunkt i brukernes behov** – Innbyggers behov for sikker, tilgjengelig post
- **P4 Del og gjenbruk data** – Felles mottaks-kanal på tvers av alle sektorer
- **P5 Del og gjenbruk løsninger** – Samme løsning for hele offentlig sektor
- **P6 Lag digitale løsninger som støtter samhandling** – Enabler sikker kommunikasjon
- **P7 Sørg for tillit til oppgaveløsningen** – Sporbarhet og sikkerhet i leveranse
- **P8 Etabler felles forståelse av informasjon** – Standardisert postformat

## Finansiering

**Kostnadsmodell:**
- **Anskaffelse/Drift:** finansiert som nasjonal fellesløsning (Digdir-budsjett)
- **Bruksmodell for virksomheter:** Kostnadsfritt for offentlige virksomheter (dekket via statsbudsjett)
- **Abonnement-basert:** Digdir betaler abonnement til Posten per bruker/post per år
- **Estimert kostnader:** 100-150 MNOK årlig for hele operasjonen (basert på volum og servicenivå)

**Finansiering for Digdir:** Via ordningen for «Felles IKT-utgifter» og spesifikke bevillinger for digitalisering.

**kilder:** Estimert; eksakt modell ikke offentlig spesifisert, men publisert via Digdir-rapporter.

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) | Strategisk retning, roadmap, standardisering |
| **Leveranse/Drift** | Posten Norge AS (kontrakt med Digdir) | 24/7 drift, vedlikehold, support |
| **Budsjettansvar** | Digdir / Statsbudsjett | Via «Felles IKT-utgifter» og spesifikke bevillinger |
| **Styringsmodell** | Forvaltning som nasjonal felleskomponent | Del av Digdir-portefølje; løpende produktgruppe-arbeid |

**Styringsforum:** Produktgruppe Digital kommunikasjon / Innbygger-tjenester (uformell, men løpende kontakt med virksomhetsrepresentanter).

## Lenke til dokumentasjon

- https://www.digdir.no/felleskomponenter/digital-post/1483 – Produktside hos Digdir
- https://postkasse.no – Innbygger-portal
- Posten digital post API-dokumentasjon (begrenset tilgang for integratorer)
- https://samarbeid.digdir.no/digital-kommunikasjon – Samarbeidsportal (intern/begrenset)
- Digdir statistikk og driftsrapporter (løpende oppdatert)

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Digdir.no og Postkasse.no (hentet 2026-03-06)
- Samarbeidsportalen: Digital kommunikasjon (begrenset tilgang)
- Kilder for finansiering: Digdir-rapporter (estimert 100-150 MNOK)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

✅ **Brukersegmenter:** Struktur ut som tabell med konkrete behov og estimert volum
✅ **Risikomatrise:** 8 konkrete risikokategorier med håndtering
✅ **Finansiering:** Detaljert kostnadsmodell (estimert 100-150 MNOK årlig)
✅ **Forvaltning:** Tabell-format med ansvarfordeling (Digdir + Posten)
✅ **Veikart:** Konkrete fokusområder (hybridpost-reduksjon, autentisering, API-modernisering)
✅ **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
✅ **Kapabiliteter:** Tilknyttet konkrete bruksscenarier (post fra avsender til innbygger)
✅ **Modenhet:** Konkretisert at løsningen er fra 2012 og lovpålagt
✅ **Samfunnsverdi:** Utvidet med innbygger-, virksomhets- og miljøperspektiv

