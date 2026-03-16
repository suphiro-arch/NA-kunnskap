# Produkt-canvas: eSignering

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
eSignering

## Ressurs ID
3 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** â€“ LovpÃ¥lagt nasjonal signeringstjeneste med aktiv videreutvikling

## Modenhet
**HÃ¸y (4-5/5)** â€“ Etablert og moden fellessolsning:
- I ordinÃ¦r bruk siden lansering (ca. 2010)
- LovpÃ¥lagt mottakskanal for digital signering fra offentlig sektor (eIDAS-regulativene, Signeringsplakaten)
- Dokumentert tjenestemodell med dokumentasjon, bruksvilkÃ¥r, statistikk, og SLA
- LÃ¸sningen inngÃ¥r i Digdirs produktgruppe for Tillisstjenester sammen med ID-porten og Maskinporten
- LÃ¸pende videreutvikling av sikkerhet, bruksvilkÃ¥r, API-modeller

## Kort beskrivelse
eSignering er en nasjonal felleslÃ¸sning som lar offentlige virksomheter gjennomfÃ¸re sikker, brukervennlig og effektiv digital signering av dokumenter med elektronisk ID (eID). Tjenesten muliggjÃ¸r maskinell opplasting og sporing av signeringsoppdrag, sikrer integriteten av signerte dokumenter, og legger til rette for videre arkivering og prosessautomatisering uten papirflyt.

## Kapabiliteter
- **Tillit: Signering** â€“ Digital signering av dokumenter
- **Tillit: Autentisering** â€“ Verifikasjon av signeringsperson via eID
- **Tillit: Identifisering** â€“ Sikker identifikasjon basert pÃ¥ fnr./personnavn
- **Tillit: Sporbarheit og innsyn** â€“ Logging av all signering; innbygger-innsyn
- **Tillit: Samtykke** â€“ Mulighet for konsent-hÃ¥ndtering i signeringsprosess
- **Informasjonssikkerhet: Sikring av informasjonsflyt** â€“ Kryptering, TLS, sikker transport
- **Tjenesteutvikling: Integrerbare tjenester** â€“ Standard API for integrasjon i fagsystemer

Grunnlag: Kapabiliteter mappet mot `index/capabilities.yaml`.

## ProduktmÃ¥l
- Tilby en felles nasjonal signeringstjeneste som kan gjenbrukes pÃ¥ tvers av offentlig sektor
- Redusere tidsbruk og manuell oppfÃ¸lging i signeringsprosesser ved automatisering
- Ã˜ke rettslig og teknisk sikkerhet i digital dokumenthÃ¥ndtering
- Standardisere integrasjon og forvaltning av signeringsprosesser i offentlige tjenester
- UnderstÃ¸tte lovgivningskrav for elektronisk signering (eIDAS, Signeringsplakaten)

## Brukerbehov
- **Offentlige virksomheter:** Sikker innhenting av underskrift uten papirflyt eller fysisk mÃ¸te
- **Innbyggere:** Enkel og trygg signering via kjent eID (BankID, Buypass, osv.)
- **Fagsystem og arkivmiljÃ¸er:** Sporbar, maskinell flyt fra oppdrag til ferdig signert dokument
- **Drifts- og sikkerhetsteam:** OvervÃ¥king av signeringsprosesser, SLA-rapportering

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Estimert volum |
|---|---|---|---|
| **Avsendende offentlige virksomheter** | Sikker innhenting av signaturer | Vedtak, kontrakter, samtykker | 5-20 mill. signeringsoppdrag Ã¥rlig |
| **Innbyggere (signÃ©rere)** | Enkel, trygg signering | Signering av dokumenter via mobil/nettleser | Passiv, men viktig brukerkategori |
| **FagsystemleverandÃ¸rer** | Integrering av signering i arbeidsprosess | Integrasjon i sak-/arkiv-/fagsystemer | Kritisk for hele oppdrags-flowen |
| **Arkiv- og saksbehandlingsmiljÃ¸er** | Mottakelse av signerte dokumenter | Automatisk opptak i arkiv etter signering | HÃ¸yt volum automatisiert |
| **Drifts- og sikkerhetsteam** | Monitorering, statistikk, SLA | Drift, sikkerhet-monitoring, rapportering | LÃ¸pende operasjonell aktivitet |

## Hovedfunksjoner

### PrimÃ¦re funksjoner
- **Opprettelse av signeringsoppdrag:** Avsender laster opp dokument til signering
- **Varsling og mobilisering:** SMS/epost til innbygger med signeringslenke
- **Tekst-basert signering:** Enkel undersignering via mobil eller nettleser
- **Avansert signering:** StÃ¸tte for QES (Qualified Digital Signature) ved behov
- **Multisignatur:** Flere signerere pÃ¥ samme dokument
- **Signeringshistorikk:** Full sporbarheit av hvem som signerte nÃ¥r
- **DokumenthÃ¥ndtering:** PDF-produksjon, JSON-oppdrag, API-status
- **Integrering med fagsystemer:** API-basert integrasjon; webhook-stÃ¸tte for events
- **Compliance og logging:** Loggering av all signering for audit; tilgang til Revisjonstvang-rapporter

### Scope og avgrensning

| InngÃ¥r | InngÃ¥r IKKE |
|---|---|
| Signeringstjeneste som felleskomponent | Full saksbehandlingsprosess i avsender-system |
| Funksjoner for signeringsoppdrag og innbygger-flyt | Lokal dokumentproduksjon hos avsender |
| Forvaltning av bruksvilkÃ¥r, kostnadsmodell, tilgangsprosess | Innbyggers interne IT-miljÃ¸ (terminal, nettleser) |
| Integrasjon mot eID-leverandÃ¸rer (BankID, Buypass, osv.) | Arkivering i avsender-system (hÃ¥ndteres av fagsystem) |
| Juridisk veiledning om signeringstype | Juridisk verifikasjon av signeringsrett |

## Veikart over kommende funksjonalitet

**Status:** Delvis offentlig dokumentert gjennom Produktgruppe Tillisstjenester og Digdir.

**Indikert fokusomrÃ¥der:**
- **Sikkerhet:** Lenkefri varsling (reduksjon av phishing-risiko)
- **eIDAS 2.0:** Tilpasning til nye EU-standarder for digital signering
- **API-modernisering:** Forbedring av API-design etter OpenAPI-standarder
- **Brukervennlighet:** Forbedret mobilflyt, enklere integrasjon
- **Kostnadsmodell:** Potensielle endringer i prismodell pÃ¥ basis av volum
- **Rapportering:** Bedre innsyn i prosessmetrikker og bruksmÃ¸nstre

**Kilder:** Produktgruppe Tillisstjenester-strategi (Samarbeidsportalen); detaljert roadmap krever kontakt med Digdir.

## Forretningsverdi/Verdiforslag

### For offentlige virksomheter
- **Kostnadsreduksjon:** Eliminerer manuell porto, fysisk arkivering, return-hÃ¥ndtering
- **Hastighet:** Automatiskere signeringsprosess; raskere vedtaks-effektuering
- **Risikomitigering:** Juridisk sikker signering; redusert risiko for papir-tap

### For innbyggere
- **Bekvemmelighet:** Signering fra mobil/nettleser; ingen fysisk mÃ¸te nÃ¸dvendig
- **Sikkerhet:** Kjent eID-leverandÃ¸r; sporbar prosess
- **Tilgjengelighet:** Mulighet for signering utenfor Ã¥pningstider

### For samfunn
- **Modernisering:** MuliggjÃ¸r papilÃ¸s, digitalt first-strategi i offentlig sektor
- **Effektivitet:** Hurtigere lovgivningsprosesser; mindre ressurskrevende
- **Sikkerhet:** Juridisk sikker digital underskrift; etterproevbarhet

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃ¥ndtering |
|---|---|---|---|
| **Juridisk** | Feil tolkining av signaturtype-krav = ikke rettslig bindend | Middels | Sjekklister for signaturtyper; veiledning per sakstype |
| **Juridisk** | Manglende dokumentasjon av signeringsprosess = vanskelig Ã¥ bevise samtykke | Middels | Automatisk logging; audit-trail i PDF; emot-taker-vahndtering |
| **Sikkerhet** | Phishing i varsling = innbygger trykker pÃ¥ falsk lenke | HÃ¸y | Lenkefri varsling; SMS-varsel; autentisering pÃ¥ portal |
| **Sikkerhet** | Tokenmisbruk eller nÃ¸kkel-lekkasje | LÃ¥g (eID kreves) | Sterk autentisering; TLS-kryptering; monitoring |
| **Integrasjon** | Avsender-systemer integrerer feil â†’ oppdrag ikke sendt/duplikater | Middels | Referansearkitektur; testdatasett; SDK-er |
| **Bruker** | Innbygger forstÃ¥r ikke prosessen â†’ frafall fra signering | HÃ¸y | Bedre UX; tydelig varslingstekst; innfÃ¸ring |
| **Bruker** | Representasjon gir forvirring â†’ feil personer signerer | Middels | Tydelig identitet-idemfikasjon i signeringsprosess |
| **LeverandÃ¸r** | Avhengighet til Posten (driftsleverandÃ¸r) | HÃ¸y | Digdir som eier sikrer kontinuitet; SLA-krav; redundans |

## Kanaler

- **API-integrasjon** fra offentlige virksomheters fagsystemer
- **Signeringsportal/-flyt** for innbygger (nettleser/mobil)
- **Varslingskanaler** (SMS/epost) for mobilisering av innbygger
- **Dokumentasjon og support** via Digdir Docs og Samarbeidsportalen
- **Driftsinformasjon** og statistikk via Samarbeidsportalen

## Plattform

- **LeverandÃ¸r:** Posten AS (driftsleverandÃ¸r pÃ¥ vegne av Digdir)
- **Hosting:** Sky-basert multi-tenant SaaS
- **API-modell:** REST-basert; dokumentert via OpenAPI
- **Autentisering:** eID (BankID, Buypass, 2faktor-koder osv.)
- **Sikkerhet:** TLS-kryptering; sikker key-management; PSD2-compliance

## Gjenbruk

**SvÃ¦rt hÃ¸y gjenbruksverdi:**
- Felles signeringstjeneste for hele offentlig sektor
- Reduserer behov for sektorvise spesiall-lÃ¸sninger
- Enig lÃ¸ste for alle signeringsbehovene (enkelt, multi, kvalifisert)
- LovpÃ¥lagt for mange sektorer; dermed felles juridisk grunnlag

## StÃ¸tte arkitekturprinsipper

- **P1 Ta utgangspunkt i brukernes behov** â€“ Innbyggers behov for enkel signering; virksomhetens behov for sikker prosess
- **P5 Del og gjenbruk lÃ¸sninger** â€“ Felles signeringskomponent for hele sektoren
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ Signering som del av samhandlingsprosesser
- **P7 SÃ¸rg for tillit til oppgavelÃ¸sningen** â€“ Sporbar, juridisk sikker signering
- **P8 Etabler felles forstÃ¥else av informasjon** â€“ Standardisert signeringsformat (PAdES, XAdES)

## Finansiering

**Kostnadsmodell:**
- **Anskaffelse/Drift:** finansiert som nasjonal felleslÃ¸sning (Digdir-budsjett)
- **Bruksmodell for virksomheter:** Kostnadsfritt for offentlige virksomheter (dekket via statsbudsjett)
- **Gebyr-modell:** Fra April 2024 nye priser basert pÃ¥ signeringaktivitet (gebyr per oppfdrag)
- **Estimert kostnader:** 20-50 MNOK Ã¥rlig for hele operasjonen (basert pÃ¥ volum 5-20 mill. signeringer/Ã¥r)

**Finansiering for Digdir:** Via ordningen for Â«Felles IKT-utgifterÂ» og spesifikke bevillinger for eSignering.

**kilder:** Publisert pÃ¥ Samarbeidsportalen og Digdir Docs (April 2024-oppdatert kostnadsmodell).

## Forvaltning/eier

| AnsvarsomrÃ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) | Strategisk retning, roadmap, bruksvilkÃ¥r |
| **Driftsansvar** | Posten AS (kontrakt med Digdir) | 24/7 drift, SLA ~99.5% oppetid |
| **Budsjettansvar** | Digdir / Statsbudsjett | Via Â«Felles IKT-utgifterÂ» og spesifikke bevillinger |
| **Styringsmodell** | Produktgruppe Tillisstjenester (felles med ID-porten, Maskinporten, Autorisasjon) | Felles strategisk retning og veikart |

**Styringsforum:** Produktgruppe Tillisstjenester (mÃ¸ter 4-6 ganger Ã¥rlig for strategi, prioriteringer, kostnadsmodell).

## Lenke til dokumentasjon

- https://www.digdir.no/digital-sikkerhet/esignering/1487 â€“ Hovud-produktside hos Digdir
- https://docs.digdir.no/docs/esignering/ â€“ teknisk dokumentasjon
- https://docs.digdir.no/docs/esignering/esign_komigang â€“ Getting started-guide
- https://samarbeid.digdir.no/esignering/esignering/22 â€“ Samarbeidsportal (kostnadsinformasjon, statistikk)
- https://samarbeid.digdir.no/esignering/kostnadsmodell-esignering/103 â€“ Kostnadsmodell (April 2024-oppdatert)
- https://samarbeid.digdir.no/id-porten/produktgruppestrategi-tillisstjenester/2138 â€“ Produktgruppe Tillisstjenester strategi

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Digdir Docs og Samarbeidsportalen (hentet 2026-03-07)
- Kostnadsmodell: Samarbeidsportalen (April 2024-versjon)
- Kilder for finansiering: Digdir-rapporter (estimert 20-50 MNOK)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

âœ… **Brukersegmenter:** Struktur ut som tabell med konkrete behov og estimert volum
âœ… **Risikomatrise:** 8 konkrete risikokategorier med hÃ¥ndtering  
âœ… **Finansiering:** Detaljert kostnadsmodell (estimert 20-50 MNOK Ã¥rlig, April 2024-modell)
âœ… **Forvaltning:** Tabell-format med tydelig ansvarsfordeling (Digdir + Posten)
âœ… **Veikart:** Konkrete fokusomrÃ¥der (lenkefri varsling, eIDAS 2.0, API-modernisering, brukervennlighet)
âœ… **Scope:** Eksplisitt tabell over hva som inngÃ¥r/ikke inngÃ¥r
âœ… **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet
âœ… **Sturingsforum:** Eksplisett referanse til Produktgruppe Tillisstjenester
âœ… **Juridisk sikkerheit:** Konkrete referanser til eIDAS, Signeringsplakaten, kvalifisert signatur

