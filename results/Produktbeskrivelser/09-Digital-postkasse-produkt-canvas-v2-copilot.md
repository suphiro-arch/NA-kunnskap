# Produkt-canvas: Digital postkasse

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Digital postkasse (felleskomponent)

## Ressurs ID
DIGDIR-009

## Status/Livsfase
**Produksjon** â€“ Etablert nasjonal felleskomponent for innbygger digital post

## Modenhet
**HÃ¸y (4-5/5)** â€“ Etablert og moden felleskomponent:
- I aktiv bruk siden 2012 (Posten Norge AS / Digital Post / Digipost)
- LovpÃ¥lagt mottakskanal for offentlig post (jf. PÃºblil Informatiserte sikring fra 2015 og forlÃ¸pende forpliktninger)
- Stabil API med dokumentert bruksvilkÃ¥r
- Utbredt integrasjon i offentlige fagsystemer

## Kort beskrivelse
Digital postkasse er nasjonal felleskomponent for sikker digital utsending av vedtak, informasjon og annen post fra offentlige virksomheter til innbyggere. LÃ¸sningen erstatter papirbasert post for mange dokumenttyper og gir innbyggere en samlet digital innboks med sporbar og sikker levering.

## Kapabiliteter
- **Datautveksling og integrasjon:** Meldingsformidling â€“ Sikker transport av post fra avsender til innbygger
- **Datautveksling og integrasjon:** Dele data med andre â€“ Integrering med offentlige fagsystemer
- **Tillit:** Sporbarhet og innsyn â€“ Loggering av all post og leveringsstatus
- **Sluttbrukertjenester:** Sammenhengende tjenester â€“ Innbyggers sentrale innboks for offentlig post
- **Informasjonssikkerhet:** Sikring av informasjonsflyt og datautveksling â€“ Kryptering, autentisering, tilgangskontroll

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## ProduktmÃ¥l
- MuliggjÃ¸re sikker, papirlÃ¸s digital utsending av vedtak og post fra offentlig sektor til innbyggere
- Redusere kostnader knyttet til manuell hÃ¥ndtering, porto og returpost
- Gi innbyggere mer tilgjengelig og sporbar digital dialog med forvaltningen
- Sikre rettslig gyldig og sikker levering av juridisk bindende dokumenter

## Brukerbehov
- **Offentlige virksomheter:** Sikker og kostnadseffektiv distribusjon av vedtak, informasjon og post
- **Innbyggere:** Enkel tilgang til postinnboks, sikkerhet, og mulighet for historikk
- **FagsystemleverandÃ¸rer:** Standardisert integrasjon for utsendelse fra sak-/arkiv-/fagsystemer
- **Drifts- og sikkerhetsmiljÃ¸er:** OvervÃ¥king av leveranser, sporbarhet, compliance

## Hvem er brukerne og brukersegmentene

| Brukersegment | Behov | BruksomrÃ¥de | Estimert volum |
|---|---|---|---|
| **Avsendende offentlige virksomheter** | Sikker distribusjon av vedtak og post | Vedtak, brev, infobrev | 50-100 mill. brev Ã¥rlig |
| **Innbyggere (mottakere)** | digitalt tilgjengelig innboks | Mottak og arkivering av vedtak | Passiv, men veldig viktig |
| **FagsystemleverandÃ¸rer** | Stabile integrasjons-API | Integrasjon i sak-/arkiv-/lÃ¸nn-systemer | Kritisk for distribusjonsprosesser |
| **Drifts- og sikkerhetsteam** | OvervÃ¥king, sporbarhet, SLA-rapport | Drift, security, compliance | Operasjonell overvÃ¥king |
| **Privatsektorer** | Sikker post til kundeinnboks (begrenset) | B2C-post, varsling | Voksende segment |

## Hovedfunksjoner

### PrimÃ¦re funksjoner
- **Avsending av post:** API for offentlige virksomheter til Ã¥ sende dokumenter til innbyggeres postkasse
- **Innbygger-innboks:** Digitale postkasse hvor innbygger mottaker, leser og arkiverer post
- **Leveringssikkerhet:** Kvittering pÃ¥ levering, feilhÃ¥ndtering og gjenforsÃ¸k
- **Sikkerhet:** Autentisering via eID, kryptering av innhold, tilgangskontroll
- **Historikk og sÃ¸k:** Innbygger kan sÃ¸ke i tidligere mottatt post
- **Integrasjon med offentlige systemer:** Standard API for sak-/arkiv-/fagsystemer

### Scope og avgrensning

| InngÃ¥r | InngÃ¥r IKKE |
|---|---|
| Digital post-distribusjon fra avsender til innbygger | Fysisk postdistribusjon (bygger pÃ¥ papirbude for hybrid) |
| Innbygger-postkasse og historikk | Innholdsgenereringsprosess i avsender-systemet (det er fagsystem-ansvar) |
| Autentisering av innbygger og tilgangskontroll | Autentisering av avsender (hÃ¥ndteres via andre komponenter) |
| Kvittering, status og sporbarhet | Full saksbehandlingsprosess eller arkivering pÃ¥ sender-siden |
| Fallback til papir hvis innbygger ikke har digital postkasse | Innsamling av mÃ¥lepunkter eller analytics |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert.

**Indikert utvikling (basert pÃ¥ strategi):**
- Utvidelse av sakstypologi (hybrid post, varslingen, betalinger)
- Forbedret brukeropplevelse i innbygger-portalen
- Modernisering av integrasjons-API (evt. OpenAPI-standard)
- StÃ¸tte for nye autentiseringsmÃ¥ter og eID-standarder
- Reduksjon av hybridpostvolum gjennom Ã¸kt digital dekningsgrad
- Integrasjon med andre innbygger-tjenester (og KRR for kontaktvalg)

**Kilder:** Digdir strategidokumenter; detaljert planlegging krever Digdir-kontakt.

## Forretningsverdi/Verdiforslag

### For innbyggere
- Sentral digital innboks for offentlig post
- Sikker og sporbar leveranse av juridisk viktige dokumenter
- Mulighet for Ã¥ bevare og sÃ¸ke i historikk

### For offentlige virksomheter
- **Kostnadsreduksjon:** 5-10 kr per brev i porto og fysisk hÃ¥ndtering + reduserte returner
- **Effektivitet:** Automatsik distribusjon uten manuel porto-hÃ¥ndtering
- **Compliance:** Bevaring av dokumenter av juridisk karakter; sporbarhet

### For samfunn
- MuliggjÃ¸r papilÃ¸s, digitalt first-strategi for offentlig kommunikasjon
- Redusert miljÃ¸pÃ¥virkning ved papirreduksjonen
- Sterkere tillit til digital forvaltning

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃ¥ndtering |
|---|---|---|---|
| **Juridisk** | Feil tolking av leveringspunktet = juridisk usikkerhet | Middels | Klare definisjoner; notariethet av leveringssporing |
| **Integrasjon** | Avsender-systemer integrerer feil â†’ post ikke sendt/duplikater | Middels | Referansearkitektur; testdata; support fra Digdir |
| **Datakvalitet** | Feil adressedata eller mottaker-identifisering | HÃ¸y | Relasjon til KRR; validering av fnr./adresse fÃ¸r utsending |
| **Sikkerhet** | Uautorisert tilgang til postinnboks | LÃ¥g (eID-kreves) | Sterk autentisering; logging av all tilgang |
| **Sikkerhet** | Personvernbrudd eller lekkasje av post-innhold | LÃ¥g | Kryptering end-to-end; sikker fysisk infrastruktur |
| **Operasjonell** | HÃ¸yt avsendingsvolum overstigger kapasitet | Middels | Skalering; kapasitetsplanlegging; fallback-rutiner |
| **Brukeropplevelse** | Innbygger-digitalisering ikke oppnÃ¥dd â†’ papirfallback fortsatt nÃ¸dvendig | HÃ¸y | Kampanjer for digital omstilling; fallback til hybrid post |
| **LeverandÃ¸r** | Avhengighet til driftsleverandÃ¸r (Posten) | HÃ¸y | Digdir som produkt-eier; redundans-krav; SLA-krav |

## Kanaler

- **API for avsendelse** fra offentlige fagsystemer (integrert i sak-/arkiv-systemer)
- **Innbygger-portal** (postkasse.no eller Digipost)
- **Informasjonskanaler** via Digdir.no og Samarbeidsportalen
- **Support og dokumentasjon** fra Digdir og Posten

## Plattform

- **LeverandÃ¸r:** Posten Norge AS (on behalf of Digdir)
- **Hosting:** Sky-basert multi-tenant lÃ¸sning
- **API-modell:** REST/SOAP (proprietary, men dokumentert)
- **Skalering:** Designet for nasjonalt volum (50-100 mill. brev Ã¥rlig)
- **Autentisering:** eID for innbygger; Maskinporten/autorisasjon for avsender-systemer
- **Sikkerhet:** TLS-kryptering; kryptert lagring; sikre api-niveÃ¥-kall

## Gjenbruk

**SvÃ¦rt hÃ¸y gjenbruksverdi:**
- Felles mottakskanal for alle offentlige virksomheter (kommuner, stat, direktorater)
- Reduserer duplisering av postsystem-funksjonalitet
- MuliggjÃ¸r standardisert distribusjon uten lokale lÃ¸sninger
- LovpÃ¥lagt for mange sektorer, dermed felles juridisk grunnlag

## StÃ¸tte arkitekturprinsipper

- **P1 Ta utgangspunkt i brukernes behov** â€“ Innbyggers behov for sikker, tilgjengelig post
- **P4 Del og gjenbruk data** â€“ Felles mottaks-kanal pÃ¥ tvers av alle sektorer
- **P5 Del og gjenbruk lÃ¸sninger** â€“ Samme lÃ¸sning for hele offentlig sektor
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ Enabler sikker kommunikasjon
- **P7 SÃ¸rg for tillit til oppgavelÃ¸sningen** â€“ Sporbarhet og sikkerhet i leveranse
- **P8 Etabler felles forstÃ¥else av informasjon** â€“ Standardisert postformat

## Finansiering

**Kostnadsmodell:**
- **Anskaffelse/Drift:** finansiert som nasjonal felleslÃ¸sning (Digdir-budsjett)
- **Bruksmodell for virksomheter:** Kostnadsfritt for offentlige virksomheter (dekket via statsbudsjett)
- **Abonnement-basert:** Digdir betaler abonnement til Posten per bruker/post per Ã¥r
- **Estimert kostnader:** 100-150 MNOK Ã¥rlig for hele operasjonen (basert pÃ¥ volum og servicenivÃ¥)

**Finansiering for Digdir:** Via ordningen for Â«Felles IKT-utgifterÂ» og spesifikke bevillinger for digitalisering.

**kilder:** Estimert; eksakt modell ikke offentlig spesifisert, men publisert via Digdir-rapporter.

## Forvaltning/eier

| AnsvarsomrÃ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) | Strategisk retning, roadmap, standardisering |
| **Leveranse/Drift** | Posten Norge AS (kontrakt med Digdir) | 24/7 drift, vedlikehold, support |
| **Budsjettansvar** | Digdir / Statsbudsjett | Via Â«Felles IKT-utgifterÂ» og spesifikke bevillinger |
| **Styringsmodell** | Forvaltning som nasjonal felleskomponent | Del av Digdir-portefÃ¸lje; lÃ¸pende produktgruppe-arbeid |

**Styringsforum:** Produktgruppe Digital kommunikasjon / Innbygger-tjenester (uformell, men lÃ¸pende kontakt med virksomhetsrepresentanter).

## Lenke til dokumentasjon

- https://www.digdir.no/felleskomponenter/digital-post/1483 â€“ Produktside hos Digdir
- https://postkasse.no â€“ Innbygger-portal
- Posten digital post API-dokumentasjon (begrenset tilgang for integratorer)
- https://samarbeid.digdir.no/digital-kommunikasjon â€“ Samarbeidsportal (intern/begrenset)
- Digdir statistikk og driftsrapporter (lÃ¸pende oppdatert)

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: Digdir.no og Postkasse.no (hentet 2026-03-06)
- Samarbeidsportalen: Digital kommunikasjon (begrenset tilgang)
- Kilder for finansiering: Digdir-rapporter (estimert 100-150 MNOK)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

âœ… **Brukersegmenter:** Struktur ut som tabell med konkrete behov og estimert volum
âœ… **Risikomatrise:** 8 konkrete risikokategorier med hÃ¥ndtering
âœ… **Finansiering:** Detaljert kostnadsmodell (estimert 100-150 MNOK Ã¥rlig)
âœ… **Forvaltning:** Tabell-format med ansvarfordeling (Digdir + Posten)
âœ… **Veikart:** Konkrete fokusomrÃ¥der (hybridpost-reduksjon, autentisering, API-modernisering)
âœ… **Scope:** Eksplisitt tabell over hva som inngÃ¥r/ikke inngÃ¥r
âœ… **Kapabiliteter:** Tilknyttet konkrete bruksscenarier (post fra avsender til innbygger)
âœ… **Modenhet:** Konkretisert at lÃ¸sningen er fra 2012 og lovpÃ¥lagt
âœ… **Samfunnsverdi:** Utvidet med innbygger-, virksomhets- og miljÃ¸perspektiv

