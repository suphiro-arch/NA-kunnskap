# Produkt-canvas: eSignering

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
eSignering

## Ressurs ID
3 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** – Lovpålagt nasjonal signeringstjeneste med aktiv videreutvikling

## Modenhet
**Høy (4-5/5)** – Etablert og moden fellessolsning:
- I ordinær bruk siden lansering (ca. 2010)
- Lovpålagt mottakskanal for digital signering fra offentlig sektor (eIDAS-regulativene, Signeringsplakaten)
- Dokumentert tjenestemodell med dokumentasjon, bruksvilkår, statistikk, og SLA
- Løsningen inngår i Digdirs produktgruppe for Tillisstjenester sammen med ID-porten og Maskinporten
- Løpende videreutvikling av sikkerhet, bruksvilkår, API-modeller

## Kort beskrivelse
eSignering er en nasjonal fellesløsning som lar offentlige virksomheter gjennomføre sikker, brukervennlig og effektiv digital signering av dokumenter med elektronisk ID (eID). Tjenesten muliggjør maskinell opplasting og sporing av signeringsoppdrag, sikrer integriteten av signerte dokumenter, og legger til rette for videre arkivering og prosessautomatisering uten papirflyt.

## Kapabiliteter
- **Tillit: Signering** – Digital signering av dokumenter
- **Tillit: Autentisering** – Verifikasjon av signeringsperson via eID
- **Tillit: Identifisering** – Sikker identifikasjon basert på fnr./personnavn
- **Tillit: Sporbarheit og innsyn** – Logging av all signering; innbygger-innsyn
- **Tillit: Samtykke** – Mulighet for konsent-håndtering i signeringsprosess
- **Informasjonssikkerhet: Sikring av informasjonsflyt** – Kryptering, TLS, sikker transport
- **Tjenesteutvikling: Integrerbare tjenester** – Standard API for integrasjon i fagsystemer

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## Produktmål
- Tilby en felles nasjonal signeringstjeneste som kan gjenbrukes på tvers av offentlig sektor
- Redusere tidsbruk og manuell oppfølging i signeringsprosesser ved automatisering
- Øke rettslig og teknisk sikkerhet i digital dokumenthåndtering
- Standardisere integrasjon og forvaltning av signeringsprosesser i offentlige tjenester
- Understøtte lovgivningskrav for elektronisk signering (eIDAS, Signeringsplakaten)

## Brukerbehov
- **Offentlige virksomheter:** Sikker innhenting av underskrift uten papirflyt eller fysisk møte
- **Innbyggere:** Enkel og trygg signering via kjent eID (BankID, Buypass, osv.)
- **Fagsystem og arkivmiljøer:** Sporbar, maskinell flyt fra oppdrag til ferdig signert dokument
- **Drifts- og sikkerhetsteam:** Overvåking av signeringsprosesser, SLA-rapportering

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Estimert volum |
|---|---|---|---|
| **Avsendende offentlige virksomheter** | Sikker innhenting av signaturer | Vedtak, kontrakter, samtykker | 5-20 mill. signeringsoppdrag årlig |
| **Innbyggere (signérere)** | Enkel, trygg signering | Signering av dokumenter via mobil/nettleser | Passiv, men viktig brukerkategori |
| **Fagsystemleverandører** | Integrering av signering i arbeidsprosess | Integrasjon i sak-/arkiv-/fagsystemer | Kritisk for hele oppdrags-flowen |
| **Arkiv- og saksbehandlingsmiljøer** | Mottakelse av signerte dokumenter | Automatisk opptak i arkiv etter signering | Høyt volum automatisiert |
| **Drifts- og sikkerhetsteam** | Monitorering, statistikk, SLA | Drift, sikkerhet-monitoring, rapportering | Løpende operasjonell aktivitet |

## Hovedfunksjoner

### Primære funksjoner
- **Opprettelse av signeringsoppdrag:** Avsender laster opp dokument til signering
- **Varsling og mobilisering:** SMS/epost til innbygger med signeringslenke
- **Tekst-basert signering:** Enkel undersignering via mobil eller nettleser
- **Avansert signering:** Støtte for QES (Qualified Digital Signature) ved behov
- **Multisignatur:** Flere signerere på samme dokument
- **Signeringshistorikk:** Full sporbarheit av hvem som signerte når
- **Dokumenthåndtering:** PDF-produksjon, JSON-oppdrag, API-status
- **Integrering med fagsystemer:** API-basert integrasjon; webhook-støtte for events
- **Compliance og logging:** Loggering av all signering for audit; tilgang til Revisjonstvang-rapporter

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Signeringstjeneste som felleskomponent | Full saksbehandlingsprosess i avsender-system |
| Funksjoner for signeringsoppdrag og innbygger-flyt | Lokal dokumentproduksjon hos avsender |
| Forvaltning av bruksvilkår, kostnadsmodell, tilgangsprosess | Innbyggers interne IT-miljø (terminal, nettleser) |
| Integrasjon mot eID-leverandører (BankID, Buypass, osv.) | Arkivering i avsender-system (håndteres av fagsystem) |
| Juridisk veiledning om signeringstype | Juridisk verifikasjon av signeringsrett |

## Veikart over kommende funksjonalitet

**Status:** Delvis offentlig dokumentert gjennom Produktgruppe Tillisstjenester og Digdir.

**Indikert fokusområder:**
- **Sikkerhet:** Lenkefri varsling (reduksjon av phishing-risiko)
- **eIDAS 2.0:** Tilpasning til nye EU-standarder for digital signering
- **API-modernisering:** Forbedring av API-design etter OpenAPI-standarder
- **Brukervennlighet:** Forbedret mobilflyt, enklere integrasjon
- **Kostnadsmodell:** Potensielle endringer i prismodell på basis av volum
- **Rapportering:** Bedre innsyn i prosessmetrikker og bruksmønstre

**Kilder:** Produktgruppe Tillisstjenester-strategi (Samarbeidsportalen); detaljert roadmap krever kontakt med Digdir.

## Forretningsverdi/Verdiforslag

### For offentlige virksomheter
- **Kostnadsreduksjon:** Eliminerer manuell porto, fysisk arkivering, return-håndtering
- **Hastighet:** Automatiskere signeringsprosess; raskere vedtaks-effektuering
- **Risikomitigering:** Juridisk sikker signering; redusert risiko for papir-tap

### For innbyggere
- **Bekvemmelighet:** Signering fra mobil/nettleser; ingen fysisk møte nødvendig
- **Sikkerhet:** Kjent eID-leverandør; sporbar prosess
- **Tilgjengelighet:** Mulighet for signering utenfor åpningstider

### For samfunn
- **Modernisering:** Muliggjør papiløs, digitalt first-strategi i offentlig sektor
- **Effektivitet:** Hurtigere lovgivningsprosesser; mindre ressurskrevende
- **Sikkerhet:** Juridisk sikker digital underskrift; etterproevbarhet

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Juridisk** | Feil tolkining av signaturtype-krav = ikke rettslig bindend | Middels | Sjekklister for signaturtyper; veiledning per sakstype |
| **Juridisk** | Manglende dokumentasjon av signeringsprosess = vanskelig å bevise samtykke | Middels | Automatisk logging; audit-trail i PDF; emot-taker-vahndtering |
| **Sikkerhet** | Phishing i varsling = innbygger trykker på falsk lenke | Høy | Lenkefri varsling; SMS-varsel; autentisering på portal |
| **Sikkerhet** | Tokenmisbruk eller nøkkel-lekkasje | Låg (eID kreves) | Sterk autentisering; TLS-kryptering; monitoring |
| **Integrasjon** | Avsender-systemer integrerer feil → oppdrag ikke sendt/duplikater | Middels | Referansearkitektur; testdatasett; SDK-er |
| **Bruker** | Innbygger forstår ikke prosessen → frafall fra signering | Høy | Bedre UX; tydelig varslingstekst; innføring |
| **Bruker** | Representasjon gir forvirring → feil personer signerer | Middels | Tydelig identitet-idemfikasjon i signeringsprosess |
| **Leverandør** | Avhengighet til Posten (driftsleverandør) | Høy | Digdir som eier sikrer kontinuitet; SLA-krav; redundans |

## Kanaler

- **API-integrasjon** fra offentlige virksomheters fagsystemer
- **Signeringsportal/-flyt** for innbygger (nettleser/mobil)
- **Varslingskanaler** (SMS/epost) for mobilisering av innbygger
- **Dokumentasjon og support** via Digdir Docs og Samarbeidsportalen
- **Driftsinformasjon** og statistikk via Samarbeidsportalen

## Plattform

- **Leverandør:** Posten AS (driftsleverandør på vegne av Digdir)
- **Hosting:** Sky-basert multi-tenant SaaS
- **API-modell:** REST-basert; dokumentert via OpenAPI
- **Autentisering:** eID (BankID, Buypass, 2faktor-koder osv.)
- **Sikkerhet:** TLS-kryptering; sikker key-management; PSD2-compliance

## Gjenbruk

**Svært høy gjenbruksverdi:**
- Felles signeringstjeneste for hele offentlig sektor
- Reduserer behov for sektorvise spesiall-løsninger
- Enig løste for alle signeringsbehovene (enkelt, multi, kvalifisert)
- Lovpålagt for mange sektorer; dermed felles juridisk grunnlag

## Støtte arkitekturprinsipper

- **P1 Ta utgangspunkt i brukernes behov** – Innbyggers behov for enkel signering; virksomhetens behov for sikker prosess
- **P5 Del og gjenbruk løsninger** – Felles signeringskomponent for hele sektoren
- **P6 Lag digitale løsninger som støtter samhandling** – Signering som del av samhandlingsprosesser
- **P7 Sørg for tillit til oppgaveløsningen** – Sporbar, juridisk sikker signering
- **P8 Etabler felles forståelse av informasjon** – Standardisert signeringsformat (PAdES, XAdES)

## Finansiering

**Kostnadsmodell:**
- **Anskaffelse/Drift:** finansiert som nasjonal fellesløsning (Digdir-budsjett)
- **Bruksmodell for virksomheter:** Kostnadsfritt for offentlige virksomheter (dekket via statsbudsjett)
- **Gebyr-modell:** Fra April 2024 nye priser basert på signeringaktivitet (gebyr per oppfdrag)
- **Estimert kostnader:** 20-50 MNOK årlig for hele operasjonen (basert på volum 5-20 mill. signeringer/år)

**Finansiering for Digdir:** Via ordningen for «Felles IKT-utgifter» og spesifikke bevillinger for eSignering.

**kilder:** Publisert på Samarbeidsportalen og Digdir Docs (April 2024-oppdatert kostnadsmodell).

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) | Strategisk retning, roadmap, bruksvilkår |
| **Driftsansvar** | Posten AS (kontrakt med Digdir) | 24/7 drift, SLA ~99.5% oppetid |
| **Budsjettansvar** | Digdir / Statsbudsjett | Via «Felles IKT-utgifter» og spesifikke bevillinger |
| **Styringsmodell** | Produktgruppe Tillisstjenester (felles med ID-porten, Maskinporten, Autorisasjon) | Felles strategisk retning og veikart |

**Styringsforum:** Produktgruppe Tillisstjenester (møter 4-6 ganger årlig for strategi, prioriteringer, kostnadsmodell).

## Lenke til dokumentasjon

- https://www.digdir.no/digital-sikkerhet/esignering/1487 – Hovud-produktside hos Digdir
- https://docs.digdir.no/docs/esignering/ – teknisk dokumentasjon
- https://docs.digdir.no/docs/esignering/esign_komigang – Getting started-guide
- https://samarbeid.digdir.no/esignering/esignering/22 – Samarbeidsportal (kostnadsinformasjon, statistikk)
- https://samarbeid.digdir.no/esignering/kostnadsmodell-esignering/103 – Kostnadsmodell (April 2024-oppdatert)
- https://samarbeid.digdir.no/id-porten/produktgruppestrategi-tillisstjenester/2138 – Produktgruppe Tillisstjenester strategi

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: Digdir Docs og Samarbeidsportalen (hentet 2026-03-07)
- Kostnadsmodell: Samarbeidsportalen (April 2024-versjon)
- Kilder for finansiering: Digdir-rapporter (estimert 20-50 MNOK)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

- **Brukersegmenter:** Struktur ut som tabell med konkrete behov og estimert volum
- **Risikomatrise:** 8 konkrete risikokategorier med håndtering  
- **Finansiering:** Detaljert kostnadsmodell (estimert 20-50 MNOK årlig, April 2024-modell)
- **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Digdir + Posten)
- **Veikart:** Konkrete fokusområder (lenkefri varsling, eIDAS 2.0, API-modernisering, brukervennlighet)
- **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
- **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet
- **Sturingsforum:** Eksplisett referanse til Produktgruppe Tillisstjenester
- **Juridisk sikkerheit:** Konkrete referanser til eIDAS, Signeringsplakaten, kvalifisert signatur

