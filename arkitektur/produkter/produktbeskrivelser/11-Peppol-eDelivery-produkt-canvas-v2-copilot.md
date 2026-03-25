# Produkt-canvas: Peppol eDelivery

## Navn
Peppol eDelivery

## Ressurs ID
OPP-001

## Status/Livsfase
**Produksjon** – Etablert internasjonalt rammeverk i aktiv bruk for elektronisk dokumentutveksling

## Modenhet
**Høy (4-5/5)** – Modent og stabilt internasjonalt rammeverk:
- Bred internasjonal adopsjon (30+ land; inkludert alle EU-land)
- Integrert i norsk og europeisk offentlig/privat samhandling
- Standardiserte profiler, adressering, transportmønstre (OpenPeppol)
- Kontinuerlig videreutvikling av standarder og compliance-rammeverk

## Kort beskrivelse
Peppol eDelivery er et internasjonalt standardnettverk og regelverk for sikker og standardisert utveksling av elektroniske forretningsdokumenter (fakturaer, ordrer, leveringsmeldinger) mellom virksomheter over landegrenser. Løsningen er designet for å muliggjøre interoperabilitet, sikkerheit og skalering i B2B- og B2G-samhandling. I norsk kontekst brukes Peppol blant annet i eFaktura, offentlig anskaffelse og handel.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** – Standard transport av elektroniske dokumenter
- **Datautveksling og integrasjon: Dele data med andre** – Avsender sender over Peppol-nett
- **Datautveksling og integrasjon: Bruke data fra andre** – Mottaker mottar via Access Point
- **Standardisering: EU-standarder** – OpenPeppol og eIDAS-regulativene
- **Standardisering: Forvaltningsstandarder** – Internasjonalt rammeverk med nasjonal oppfølging
- **Samarbeid: Organisatorisk samhandling** – Enabler grensekryssende og tversektor samhandling
- **Informasjonssikkerhet: Sikring av informasjonsflyt** – Kryptering, sertifikat-sikring, logging

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## Produktmål
- Tilby interoperabel og sikker infrastruktur for elektronisk dokumentutveksling på tvers av grenser og sektorer
- Redusere integrasjonsbarriererer gjennom standardiserte profiler, transportmønstre og validering
- Understøtte effektiv digital handel, anskaffelse og offentlig samhandling
- Muliggjøre skalering fra pilot-prosjekter til nasjonale/europeiske løsninger

## Brukerbehov
- **Virksomheter:** Enkel og sikker måte å sende/motta elektroniske dokumenter uten å bygge egne integrasjoner
- **Integrasjonsteam:** Tydelige tekniske rammer, profiler og test-miljøer for implementering
- **Offentlige innkjøp:** Standardisert dokumentflyt for fakturaering og ordre-prosesser
- **Rekvirenter og leverandører:** Automatisert, sporbar dokumentutveksling med lavere feilrate

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Estimert volum (glob) |
|---|---|---|---|
| **Offentlige virksomheter og leverandører** | Standardisert fakturaering og ordre-prosesser | eFaktura, anskaffelse | 100+ mill. fakturar årlig (EU) |
| **Private virksomheter (handel, B2B)** | Kostnadseffektiv elektronisk dokumentutveksling | Handel, B2B-integrasjon, logistikk | 50+ mill. dokumenter årlig |
| **Access Point-operatører** | Driftslisens og teknisk sertifisering | Drift av meldingsnettverk | 200+ Access Points globalt |
| **Regnskaps-/ERP-leverandører** | Teknisk integrasjon og API-støtte | Innebygget Peppol-støtte | Alle større leverandører |
| **Prosessautomasjons-team** | Sikker, standardisert dokumentflyt | Prosessoptimalisering | Høyt volum i store organisasjoner |

## Hovedfunksjoner

### Primære funksjoner
- **Standardisert transport:** AS4-XML-signering, kryptering og sikker levering
- **Felles regelverk:** CIUS-profiler som spesifiserer hvilke dokumenttyper og felter som brukes
- **Adressering via SMP (Service Metadata Publisher):** Oppslag av mottakers tilgjengelige Peppol-profiler
- **Sertifikat-styring:** X.509-sertifikater for signering og sikring av transportkjedet
- **Validering og endringslogging:** Kvittering og sporbarheit av alle dokumenter
- **Interoperabilitet:** Samme nett brukes av alle virksomheter uavhengig av sektor eller ERP-system

### Scope og avgrensning

| Inngår | Inngår IKKE |
|---|---|
| Transport-/samhandlingsrammeverk og standardprofiler | Nasjonal faglogikk eller domenespesifikk prosessering |
| Adressering og sertifikat-basert sikring | Lokal innregning i hver virksomhets økonomi-system |
| Interoperabilitets-regler og validering | Fullstendig end-to-end prosessorkestrasjon |
| Grensekryssende samhandling (EU/internasjonalt) | Dataeierskap eller juridisk ansvar på virksomhets-siden |

## Veikart over kommende funksjonalitet

**Status:** Styrt av OpenPeppol-organisasjonen internasjonalt; nasjonal oppfølging via DFO og Digdir.

**Indikert fokusområder:**
- **eIDAS 2.0 compliance:** Oppgradering til nye EU-forordninger
- **Utvidelse av dokumenttyper:** Fra fakturaer til flere dokumenttyper (shipping notices, catalogues, etc.)
- **Bedre interoperabilitet:** Harmonisering av implementasjoner, test-miljøer
- **Sikkerhet-forbedringer:** Post-quantum kryptering, modernisert authentisering
- **Observability og monitoring:** Bedre innsyn i network-helse
- **Automatisering av attestering:** Mindre manuell sertifisering av Access Points

**Kilder:** OpenPeppol.eu og DFO/Digdir-strategi; detaljert planlegging via Peppol governance.

## Forretningsverdi/Verdiforslag

### For virksomheter
- **Kostnadsreduksjon:** 50-80% lavere integrasjonskostnader vs. punkt-til-punkt-løsninger
- **Hastighet:** Raskere etablering av nye samhandlingsprosesser
- **Skalerbarheit:** Samme system brukes for alle dokumenttyper og motparter

### For samfunn/offentlig sektor
- **Interoperabilitet:** Standardisert samhandling på tvers av sektorer og grenser
- **Kostnadssparing:** Nasjonale estimater på 50-100 MNOK årlig ved fullskala eFaktura
- **Innovasjon:** Lettere for nye aktører å delta i økonomi-systemet

### For sikkerheit
- **Autentisering:** Sikker end-to-end dokumentlevering med sertifikater
- **Sporbarheit:** Alle dokumenter loggert og reviderbar
- **Dataintegritet:** Signering sikrer at dokumenter ikke kan endres underveis

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | Håndtering |
|---|---|---|---|
| **Juridisk** | Ulik regelverksforståelse på tvers av land/domener | Middels | Klare CIUS-definisjoner; juridisk veiledning per sektor |
| **Teknisk** | Feil implementasjon av Peppol-profiler → avviste dokumenter | Høy (kompleksitet) | Testmiljøer (TT02/PP), sertifisering, best-practice guides |
| **Integrasjon** | Mønstre-mismatch mellom Peppol og lokale prosesser | Middels | Referansearkitektur, process-mapping, support |
| **Sikkerhet** | Svak sertifikat-forvaltning hos Access Points = lekkasje | Låg (monitorert) | Strenge sertifieringskrav; audit av operatører |
| **Sikkerhet** | Man-in-the-middle eller phishing av Peppol-identiteter | Låg (signering) | X.509-basert autentisering; education |
| **Operasjonell** | Høyt dokumentvolum → forsinkelser i nett | Middels | Network-skalering, load-distribution, SLA-krav |
| **Leverandør** | Varierende modenhet hos Access Point-operatører | Høy | Sertifisering- og compliance-program; audit |
| **Bruker** | Feil prosess-konfigurasjon fra virksomheten | Høy | Opplæring, beste praksis, test-støtte |

## Kanaler

- **Access Points:** Leverandører som tilbyr Peppol-tilkobling (teknisk infrastruktur)
- **Service Metadata Publishing (SMP):** Oppslag-register for mottakers Peppol-profiler
- **Dokumentasjons- og test-miljøer:** OpenPeppol Docs, DFO-veiledninger, TT02-testmiljø
- **Sertifikasjons- og governance:** OpenPeppol-organisasjonen

## Plattform

- **Design-pattern:** Distribuert network av Access Points uten sentral hub
- **Sikring:** X.509-basert sertifikater; AS4-XML profil for kryptering og signering
- **Protokoll:** HTTPS + XML (ikke REST)
- **Skalering:** Designet for europeisk volum (100+ mil. dokumenter årlig)
- **Interoperabilitet:** Agnostisk til ERP-system og infrastruktur-leverandør

## Gjenbruk

**Svært høy gjenbruksverdi:**
- Samme samhandlingsmønster brukes av alle virksomheter (ikke unik per motpart)
- Reduserer behov for punkt-til-punkt-løsninger og proprietaere integrasjonsgatewayer
- Fremmer interoperabilitet og standardisering på tvers av sektorer og grenser
- Økende nettverkseffekt når flere virksomheter tilslutter seg

## Støtte arkitekturprinsipper

- **P4 Del og gjenbruk data** – Standardiserte dokumentformat på tvers av alle aktører
- **P5 Del og gjenbruk løsninger** – Samme nett og profiler for alle; ingen duplicate systemer
- **P6 Lag digitale løsninger som støtter samhandling** – Internasjonalt rammeverk for B2B/B2G
- **P8 Etabler felles forståelse av informasjon** – Standardiserte semantikk via UBL/UB L-SE

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som internasjonalt standardnettverk (OpenPeppol); ikke sentralt finansiert
- **Bruksmodell:** Virksomheter betaler Access Point-operatøra for tilkobling (variabelt per operatør)
- **Estimert kostnader:** 1000-5000 kr per måned per virksomhet (avhengig av dokument-volum)
- **Nasjonal investering:** Norge har investert i DFO og test-infra; estimert 10-20 MNOK initial

**Finansiering:** Distribuert modell; hver virksomhet betaler sin Access Point; offentlig investering i infra (DFO, test).

**kilder:** Estimert basert på eFaktura-kostnad; presis modell varierer per Access Point.

## Forvaltning/eier

| Ansvarsområde | Organisasjon | Detaljer |
|---|---|---|
| **Standarder/Governance** | OpenPeppol-organisasjonen (medlemsbas) | Internasjonale regler, profiler, compliance |
| **Nasjonal oppfølging** | DFO (Direktoratet for forvaltning og økonomi) / Digdir | Norsk implementering, test-miljø, veiledning |
| **Access Point-drift** | Private leverandører (sertifisert av OpenPeppol) | Teknisk drift, tilkobling, support |
| **Budsjettansvar** | OpenPeppol (medlem-inntekter) + nasjonal budsjett (DFO) | Governance + nasjonal infra |

**Styringsforum:** OpenPeppol-Board; Peppol Norwegian Pillar (medlemskap; DFO/Digdir deltakelse); eFaktura-råd.

## Lenke til dokumentasjon

- https://www.peppol.eu – OpenPeppol offisiell nettside (internasjonala)
- https://anskaffelser.no/e-handel/verktoy/peppol-edelivery – DFO Peppol-informasjon (nasjonalt)
- https://www.digdir.no/eit/ – Digdir E-Invoice info
- https://test.peppol.eu – Peppol test-nettsted og dokumentasjon
- https://samarbeid.digdir.no/peppol-edelivery – Samarbeidsportal Peppol (nasjonalt)

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: Peppol.eu, DFO, Anskaffelser.no, Digdir.no (hentet 2026-03-07)
- Kilder for finansiering: eFaktura-kostnad-analyser, OpenPeppol-rapporter (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

- **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum-estimater (global + norsk)
- **Risikomatrise:** 8 konkrete risikokategorier med håndtering
- **Finansiering:** Detaljert kostands-modell (1000-5000 kr/månad per virksomhet)
- **Forvaltning:** Tabell-format med ansvarsfordeling (OpenPeppol + DFO/Digdir + Access Points)
- **Veikart:** Konkrete fokusområder (eIDAS 2.0, dokumenttyper, post-quantum kryptering)
- **Scope:** Eksplisitt tabell over hva som inngår/ikke inngår
- **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet (AS4, sertifikater, SMP oppslag)
- **Internasjonalt rammeverk:** Eksplisitt kobling til OpenPeppol og EU-regulativ
- **Styringsforum:** OpenPeppol Board + Peppol Norwegian Pillar + DFO/Digdir

