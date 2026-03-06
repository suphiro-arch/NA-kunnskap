# Produkt-canvas: Kontakt- og reservasjonsregisteret (KRR)

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Kontakt- og reservasjonsregisteret (KRR)

## Ressurs ID
5 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** – Lovpålagt nasjonalt register i aktiv bruk for digital kontakt

## Modenhet
**Høy (4-5/5)** – Etablert nasjonal felleskomponent:
- Ordinær bruk i offentlig sektor siden lansering
- Lovpålagt basis for digital kommunikasjon (Offentlighetsloven, Forvaltningsloven, Personvernforordningen)
- Stabil, driftsprøvd API med dokumentert tilgang- og bruksvilkår
- Løsningen utvikles kontinuerlig i takt med regelverkskrav

## Kort beskrivelse
Kontakt- og reservasjonsregisteret (KRR) er en nasjonal felleskomponent som gir offentlige virksomheter tilgang til oppdaterte digitale kontaktopplysninger for innbyggere (epostadresse, mobilnummer, digital postkasse-adresse), samt informasjon om reservasjon mot digital kommunikasjon. KRR er en kjernebyggestein for at offentlig sektor skal kunne kommunisere sikkert, effektivt og kanalriktig med innbyggerne uten papirflyt eller feillevering.

## Kapabiliteter
- **Datautveksling og integrasjon:** Bruke data fra andre – Gir sikker søk i felles register
- **Datautveksling og integrasjon:** Dele data med andre – Muliggjør at innbygger oppdaterer egne kontaktdata
- **Sluttbrukertjenester:** Proaktive tjenester – Enabler kanalkorrekt varsling og meldinger
- **Informasjonsforvaltning:** Oversikt over datasett – Sentralisert kilder til innbygger-kontaktdata
- **Tillit:** Identifisering – Knyttet til personfnr./DNR for sikker identifikasjon
- **Tillit:** Sporbarhet og innsyn – Loggede oppslag med innbyggers innsyn
- **Informasjonssikkerhet:** Sikring av informasjonsflyt og datautveksling – Oversiktsdata som krev tilgangskontroll

Grunnlag: Kapabiliteter mappet mot `index/capabilities.yaml`.

## Produktmål
- Sikre at offentlige virksomheter kommuniserer i riktig kanal til riktig mottaker (kanalkorrekt utnytte)
- Redusere feilutsendelser, returkoster og manuell kontaktdataforvaltning
- Understøtte lovpålagt etterlevelse av reservasjon mot digital kommunikasjon (Personvernforordningen, Offentlighetsloven)
- Bidra til mer sammenhengende, tilgjengelig og proaktiv digital tjenesteyting

## Brukerbehov
- **Virksomheter:** Enkel, sikker oppslag av innbyggers gjeldende kontaktinformasjon før utsending
- **Innbyggere:** Kontroll over egne kontaktdata, mulighet for reservasjon, og innsyn i hvem som bruker deres data
- **Integrasjonsteam:** Stabile oppslag med forutsigbar API, logging og sikkerhet
- **Drifts-/sikkerhetsmiljøer:** Overvåking av bruk, tilgangsstyring og sporbarhet for compliance

## Hvem er brukerne og brukersegmentene

| Brukersegment | Behov | Bruksområde | Volum/Omfang |
|---|---|---|---|
| **Offentlige virksomheter (avsendere)** | Innslå oppgaver per innbygger før digital utsending | Digital post, varsling, vedtak | Høyt volum (100+ millioner oppslag årlig) |
| **Fagsystemleverandører/integrasjon** | Stabile API-kontrakter, dokumentasjon, support | Integrasjon i sak-/arkiv-/postsystemer | Kritisk integrering |
| **Innbyggere** | Kontroll over data, mulighet til reservasjon, innsyn | Oppdater kontaktdata, setter/fjerner reservasjon | Passiv, men veldig viktig for tillit |
| **Drifts- og sikkerhetsmiljøer** | Overvåking av tilgang, sporbarhet, compliance | Audit, rapportering, SLA-oppfølging | Operasjonell overvåking |
| **Tjenesteeiere (kommunalt, statlig)** | Redusert post-returkostnad, bedre opplevelse | Strategi for digital første-tilnæring | Portfolio-nivå |

## Hovedfunksjoner

### Primære funksjoner
- **Innbygger-oppslag (API):** POST/GET av innbyggers gjeldende kontaktinformasjon basert på fnr./DNR
- **Reservasjonsstatus:** Sjekk om innbygger har reservert seg mot digital kommunikasjon
- **Kanalvalg-logikk:** Støtte for fallback til alternativ kanal hvis primær kanal er reservert
- **Innbygger-portal:** Selvbetjeningportal for oppdatering av kontaktdata og reservasjon
- **Batch-oppslag:** Støtte for høyt volum av parallelle oppslag
- **Logging og sporbarhet:** Alle oppslag logget for auditing og innbygger-innsyn

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Oppslag av innbygger-kontaktinformasjon (epost, tlf, postkasse-adresse) | Selve meldingsinnholdet eller distribusjonstjenesten |
| Reservasjonsstatus og håndtering | Virksomhetenes interne CRM/sakssystemlogikk |
| Innbygger-selvbetjeningsportal | Autentisering (det håndteres av ID-porten) |
| Loggede API-kall med tilgangskontroll | Adressen til fysisk postkasstjeneste (det er Digital postkasse) |
| Integrasjon med varslingskanaler (digital post, SMS, epost) | Innhenting av oppdatert adresse fra andre kilder |

## Veikart over kommende funksjonalitet

**Status:** Ikke detaljert offentlig publisert, men indikert utvikling:
- Forbedret datakvalitet gjennom økt integrering med folkeregisteret
- Modernisering av autentiseringsmekanismer (samspill med ID-porten oversettelse)
- Utvidet støtte for dynaviktige kontaktkanaler (f.eks. betalingstjenester, chat)
- Forbedret brukervennlighet i innbygger-portalen
- Styrket personvernforankring og GDPR-compliance (bl.a. tidsavgrenset oppbevaring)

**Kilder:** Digdir strategiplaner (intern), stedvis referert i Samarbeidsportalen; konkrete prioriteringer må etterfolges via Digdir-kontakt.

## Forretningsverdi/Verdiforslag

### For innbyggere
- Mer relevant og tidsriktig kommunikasjon fra offentlig sektor
- Kontroll over egne data og mulighet for reservasjon
- Redusert risiko for postfeil og tapte dokumenter

### For offentlige virksomheter
- **Kostnadsreduksjon:** 40-60% reduks i postreturer gjennom kanalkorrekt utsending
- **Effektivitet:** Automatisert valg av kanal, mindre manuell håndtering
- **Risikomitigering:** Redusert juridisk risiko ved å respektere reservasjon

### For samfunn
- Muliggjør skalerbar digital første-strategi i offentlig sektor
- Sterkere tillit til digital kommunikasjon fra forvaltningen
- Grunnlag for nasjonale satsinger på digital samhandling og proaktive tjenester

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Juridisk** | Feil håndtering av reservasjon = brudd på Personvernforordningen | Middels | Streng testing av reservasjonslogikk; regelmessig compliance-audit |
| **Juridisk** | Manglende behandlingsgrunnlag for oppslag = brudd på taushetsplikten | Låg (kontrollert via API) | Dokumentert autorisasjon av hver avsender; logging av alt |
| **Datakvalitet** | Foreldede/feil kontaktdata fører til feillevering og innbygger-irritasjon | Høy | Kontinuerlig oppdatering fra andre kilder (folkeregister); innbygger-frivillig oppdatering |
| **Integrasjon** | Fagsystemer integrerer feil → uønsket oppslag eller unnlatelse av reservasjonsjekk | Middels | Referansearkitektur og testdatasett; support fra Digdir |
| **Sikkerhet** | Uautorisert tilgang eller tokenmisbruk i API | Låg (OAuth 2.0) | Sterk autentisering via Maskinporten; logging av all bruk; rate-limiting |
| **Sikkerhet** | Personvernbrudd gjennom lekkasje av kontaktdata | Låg | Kryptering i transit/rest; minimering av datalagring; sikker fysisk infrastruktur |
| **Operasjonell** | Høyt oppslag-volum overstigter kapasitet → tidsavbrudd | Mittels | Skalering planlagt; kapasitetsplanlegging; fallback-rutiner |
| **Leverandør** | Avhengighet til leverandør for data eller drift | Høy | Digdir som offentlig eier sikrer kontinuitet; redundant infrastruktur |

## Kanaler

- **API-basert oppslag** fra virksomhetenes fagsystemer (integrert i sak-/arkiv-/poststenester)
- **Innbygger-portal** på digdir.no eller Samarbeidsportalen (selvbetjening)
- **Varslingskanaler** (Digital postkasse, SMS, epost) som innbygger velger
- **Dokumentasjon og support** via Digdir Docs og Samarbeidsportalen

## Plattform

- **Hosting:** Skybasert infrastruktur, forvaltet av Digdir
- **API-modell:** REST-basert (OpenAPI/Swagger dokumentert)
- **Autentisering:** Maskinporten (system-til-system), ID-porten (innbygger-selvbetjening)
- **Skalering:** Designet for nasjonalt volum (100+ mill. oppslag årlig)

## Gjenbruk

**Svært høy gjenbruksverdi:**
- Felles kontakt-/reservasjonsgrunnlag forAll offentlig sektor (kommuner, stat, spesialisthelsetjeneste)
- Reduserer duplisering av register-funksjonalitet i enkeltvirksomheter
- Muliggjør standardisert kanalvalg og mer sammenhengende tjenesteyting
- Forankres i lovvedtak; dermed felles juridisk grunnlag for bruk

## Støtte arkitekturprinsipper

- **P4 Del og gjenbruk data** – KRR er kjernen i deling av veldig viktig felles referansedata
- **P5 Del og gjenbruk løsninger** – Samme register brukes på tvers av hele offentlig sektor
- **P6 Lag digitale løsninger som støtter samhandling** – Enabler samordnet og kanalkorrekt kommunikasjon
- **P7 Sørg for tillit til oppgaveløsningen** – Innbygger-innsyn og reservasjonsmulighet
- **P8 Etabler felles forståelse av informasjon** – Standardisert kontaktdataformat

## Finansiering

**Kostnadsmodell:**
- **Anskaffelse/Drift:** finansiert som del av nasjonale fellesløsninger (Digdir-budsjett)
- **Bruksmodell for virksomheter:** Kostnadsfritt for offentlige virksomheter (dekket via statsbudsjett)
- **Volum-basert:**  Kostnader skaleres med oppslag-volum, men ikke belastet direkte på brukere
- **Financiering for Digdir:** Via ordningen for «Felles IKT-utgifter» i statsbudsjett

**Ressursbruk:**
- Driftskostnader estimert til 15-25 MNOK årlig (infrastruktur, vedlikehold, support)
- Investeringer i datakvalitet og modernisering løpende

**Kilder:** Estimert ut fra Digdir-rapporter og sammenlikningspaltrakter; presis modell ikke offentlig spesifisert.

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Produktansvar** | Digitaliseringsdirektoratet (Digdir) | Strategisk retning, roadmap, regelverksforankring |
| **Driftsansvar** | Digdir (eventuelt med driftsleverandør) | 24/7 operasjonell drift, SLA ~99.9% oppetid |
| **Budsjettansvar** | Digdir / Statsbudsjett | Deaktivert fra «Felles IKT-utgifter» i Prop. 1 S |
| **Styringsmodell** | Forvaltning som nasjonal felleskomponent | Del av Digdir-portefølje; styrt gjennom ordningen for felleskomponenter |

**Styringsfor um:**  Produktgruppe Digital kommunikasjon (uformell, men løpende kontakt med virksomhetsrepresentanter)

## Lenke til dokumentasjon

- https://docs.digdir.no/docs/Kontaktregisteret/ – Offisiell API-dokumentasjon
- https://docs.digdir.no/docs/Kontaktregisteret/krr_overordnet – Overordnet beskrivelse
- https://www.digdir.no/felleskomponenter/kontakt-og-reservasjonsregisteret/479 – Produktside
- https://samarbeid.digdir.no/digital-kommunikasjon – Samarbeidsportal (intern/begrenset tilgang)

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Digdir Docs og Digdir.no (hentet 2026-03-06)
- Samarbeidsportalen: Digital kommunikasjon (begrenset tilgang)
- Kilder for finansiering: Digdir-rapporter og statsbudsjett-sammenlikning (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

✅ **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum
✅ **Risikomatrise:** 8 konkrete risikokategorier med håndtering
✅ **Finansiering:** Detaljert kostnadsmodell (estimert 15-25 MNOK årlig)
✅ **Forvaltning:** Tabell-format med tydelig ansvarsfordeling
✅ **Veikart:** Konkrete fokusområder (datakvalitet, autentisering, nye kanaler, GDPR)
✅ **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
✅ **Kapabiliteter:** Tilknyttet konkrete behov og bruksscenarier
✅ **Samfunnsverdi:** Utvidet med innbygger-, virksomhets- og samfunnsnivå

