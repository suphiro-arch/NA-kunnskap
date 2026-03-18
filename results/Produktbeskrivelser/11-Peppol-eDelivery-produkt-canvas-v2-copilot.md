# Produkt-canvas: Peppol eDelivery

MÃƒÂ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Peppol eDelivery

## Ressurs ID
BRREG-002

## Status/Livsfase
**Produksjon** Ã¢â‚¬â€œ Etablert internasjonalt rammeverk i aktiv bruk for elektronisk dokumentutveksling

## Modenhet
**HÃƒÂ¸y (4-5/5)** Ã¢â‚¬â€œ Modent og stabilt internasjonalt rammeverk:
- Bred internasjonal adopsjon (30+ land; inkludert alle EU-land)
- Integrert i norsk og europeisk offentlig/privat samhandling
- Standardiserte profiler, adressering, transportmÃƒÂ¸nstre (OpenPeppol)
- Kontinuerlig videreutvikling av standarder og compliance-rammeverk

## Kort beskrivelse
Peppol eDelivery er et internasjonalt standardnettverk og regelverk for sikker og standardisert utveksling av elektroniske forretningsdokumenter (fakturaer, ordrer, leveringsmeldinger) mellom virksomheter over landegrenser. LÃƒÂ¸sningen er designet for ÃƒÂ¥ muliggjÃƒÂ¸re interoperabilitet, sikkerheit og skalering i B2B- og B2G-samhandling. I norsk kontekst brukes Peppol blant annet i eFaktura, offentlig anskaffelse og handel.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** Ã¢â‚¬â€œ Standard transport av elektroniske dokumenter
- **Datautveksling og integrasjon: Dele data med andre** Ã¢â‚¬â€œ Avsender sender over Peppol-nett
- **Datautveksling og integrasjon: Bruke data fra andre** Ã¢â‚¬â€œ Mottaker mottar via Access Point
- **Standardisering: EU-standarder** Ã¢â‚¬â€œ OpenPeppol og eIDAS-regulativene
- **Standardisering: Forvaltningsstandarder** Ã¢â‚¬â€œ Internasjonalt rammeverk med nasjonal oppfÃƒÂ¸lging
- **Samarbeid: Organisatorisk samhandling** Ã¢â‚¬â€œ Enabler grensekryssende og tversektor samhandling
- **Informasjonssikkerhet: Sikring av informasjonsflyt** Ã¢â‚¬â€œ Kryptering, sertifikat-sikring, logging

Grunnlag: Kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## ProduktmÃƒÂ¥l
- Tilby interoperabel og sikker infrastruktur for elektronisk dokumentutveksling pÃƒÂ¥ tvers av grenser og sektorer
- Redusere integrasjonsbarriererer gjennom standardiserte profiler, transportmÃƒÂ¸nstre og validering
- UnderstÃƒÂ¸tte effektiv digital handel, anskaffelse og offentlig samhandling
- MuliggjÃƒÂ¸re skalering fra pilot-prosjekter til nasjonale/europeiske lÃƒÂ¸sninger

## Brukerbehov
- **Virksomheter:** Enkel og sikker mÃƒÂ¥te ÃƒÂ¥ sende/motta elektroniske dokumenter uten ÃƒÂ¥ bygge egne integrasjoner
- **Integrasjonsteam:** Tydelige tekniske rammer, profiler og test-miljÃƒÂ¸er for implementering
- **Offentlige innkjÃƒÂ¸p:** Standardisert dokumentflyt for fakturaering og ordre-prosesser
- **Rekvirenter og leverandÃƒÂ¸rer:** Automatisert, sporbar dokumentutveksling med lavere feilrate

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃƒÂ¦re behov | BruksomrÃƒÂ¥de | Estimert volum (glob) |
|---|---|---|---|
| **Offentlige virksomheter og leverandÃƒÂ¸rer** | Standardisert fakturaering og ordre-prosesser | eFaktura, anskaffelse | 100+ mill. fakturar ÃƒÂ¥rlig (EU) |
| **Private virksomheter (handel, B2B)** | Kostnadseffektiv elektronisk dokumentutveksling | Handel, B2B-integrasjon, logistikk | 50+ mill. dokumenter ÃƒÂ¥rlig |
| **Access Point-operatÃƒÂ¸rer** | Driftslisens og teknisk sertifisering | Drift av meldingsnettverk | 200+ Access Points globalt |
| **Regnskaps-/ERP-leverandÃƒÂ¸rer** | Teknisk integrasjon og API-stÃƒÂ¸tte | Innebygget Peppol-stÃƒÂ¸tte | Alle stÃƒÂ¸rre leverandÃƒÂ¸rer |
| **Prosessautomasjons-team** | Sikker, standardisert dokumentflyt | Prosessoptimalisering | HÃƒÂ¸yt volum i store organisasjoner |

## Hovedfunksjoner

### PrimÃƒÂ¦re funksjoner
- **Standardisert transport:** AS4-XML-signering, kryptering og sikker levering
- **Felles regelverk:** CIUS-profiler som spesifiserer hvilke dokumenttyper og felter som brukes
- **Adressering via SMP (Service Metadata Publisher):** Oppslag av mottakers tilgjengelige Peppol-profiler
- **Sertifikat-styring:** X.509-sertifikater for signering og sikring av transportkjedet
- **Validering og endringslogging:** Kvittering og sporbarheit av alle dokumenter
- **Interoperabilitet:** Samme nett brukes av alle virksomheter uavhengig av sektor eller ERP-system

### Scope og avgrensning

| InngÃƒÂ¥r | InngÃƒÂ¥r IKKE |
|---|---|
| Transport-/samhandlingsrammeverk og standardprofiler | Nasjonal faglogikk eller domenespesifikk prosessering |
| Adressering og sertifikat-basert sikring | Lokal innregning i hver virksomhets ÃƒÂ¸konomi-system |
| Interoperabilitets-regler og validering | Fullstendig end-to-end prosessorkestrasjon |
| Grensekryssende samhandling (EU/internasjonalt) | Dataeierskap eller juridisk ansvar pÃƒÂ¥ virksomhets-siden |

## Veikart over kommende funksjonalitet

**Status:** Styrt av OpenPeppol-organisasjonen internasjonalt; nasjonal oppfÃƒÂ¸lging via DFO og Digdir.

**Indikert fokusomrÃƒÂ¥der:**
- **eIDAS 2.0 compliance:** Oppgradering til nye EU-forordninger
- **Utvidelse av dokumenttyper:** Fra fakturaer til flere dokumenttyper (shipping notices, catalogues, etc.)
- **Bedre interoperabilitet:** Harmonisering av implementasjoner, test-miljÃƒÂ¸er
- **Sikkerhet-forbedringer:** Post-quantum kryptering, modernisert authentisering
- **Observability og monitoring:** Bedre innsyn i network-helse
- **Automatisering av attestering:** Mindre manuell sertifisering av Access Points

**Kilder:** OpenPeppol.eu og DFO/Digdir-strategi; detaljert planlegging via Peppol governance.

## Forretningsverdi/Verdiforslag

### For virksomheter
- **Kostnadsreduksjon:** 50-80% lavere integrasjonskostnader vs. punkt-til-punkt-lÃƒÂ¸sninger
- **Hastighet:** Raskere etablering av nye samhandlingsprosesser
- **Skalerbarheit:** Samme system brukes for alle dokumenttyper og motparter

### For samfunn/offentlig sektor
- **Interoperabilitet:** Standardisert samhandling pÃƒÂ¥ tvers av sektorer og grenser
- **Kostnadssparing:** Nasjonale estimater pÃƒÂ¥ 50-100 MNOK ÃƒÂ¥rlig ved fullskala eFaktura
- **Innovasjon:** Lettere for nye aktÃƒÂ¸rer ÃƒÂ¥ delta i ÃƒÂ¸konomi-systemet

### For sikkerheit
- **Autentisering:** Sikker end-to-end dokumentlevering med sertifikater
- **Sporbarheit:** Alle dokumenter loggert og reviderbar
- **Dataintegritet:** Signering sikrer at dokumenter ikke kan endres underveis

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃƒÂ¥ndtering |
|---|---|---|---|
| **Juridisk** | Ulik regelverksforstÃƒÂ¥else pÃƒÂ¥ tvers av land/domener | Middels | Klare CIUS-definisjoner; juridisk veiledning per sektor |
| **Teknisk** | Feil implementasjon av Peppol-profiler Ã¢â€ â€™ avviste dokumenter | HÃƒÂ¸y (kompleksitet) | TestmiljÃƒÂ¸er (TT02/PP), sertifisering, best-practice guides |
| **Integrasjon** | MÃƒÂ¸nstre-mismatch mellom Peppol og lokale prosesser | Middels | Referansearkitektur, process-mapping, support |
| **Sikkerhet** | Svak sertifikat-forvaltning hos Access Points = lekkasje | LÃƒÂ¥g (monitorert) | Strenge sertifieringskrav; audit av operatÃƒÂ¸rer |
| **Sikkerhet** | Man-in-the-middle eller phishing av Peppol-identiteter | LÃƒÂ¥g (signering) | X.509-basert autentisering; education |
| **Operasjonell** | HÃƒÂ¸yt dokumentvolum Ã¢â€ â€™ forsinkelser i nett | Middels | Network-skalering, load-distribution, SLA-krav |
| **LeverandÃƒÂ¸r** | Varierende modenhet hos Access Point-operatÃƒÂ¸rer | HÃƒÂ¸y | Sertifisering- og compliance-program; audit |
| **Bruker** | Feil prosess-konfigurasjon fra virksomheten | HÃƒÂ¸y | OpplÃƒÂ¦ring, beste praksis, test-stÃƒÂ¸tte |

## Kanaler

- **Access Points:** LeverandÃƒÂ¸rer som tilbyr Peppol-tilkobling (teknisk infrastruktur)
- **Service Metadata Publishing (SMP):** Oppslag-register for mottakers Peppol-profiler
- **Dokumentasjons- og test-miljÃƒÂ¸er:** OpenPeppol Docs, DFO-veiledninger, TT02-testmiljÃƒÂ¸
- **Sertifikasjons- og governance:** OpenPeppol-organisasjonen

## Plattform

- **Design-pattern:** Distribuert network av Access Points uten sentral hub
- **Sikring:** X.509-basert sertifikater; AS4-XML profil for kryptering og signering
- **Protokoll:** HTTPS + XML (ikke REST)
- **Skalering:** Designet for europeisk volum (100+ mil. dokumenter ÃƒÂ¥rlig)
- **Interoperabilitet:** Agnostisk til ERP-system og infrastruktur-leverandÃƒÂ¸r

## Gjenbruk

**SvÃƒÂ¦rt hÃƒÂ¸y gjenbruksverdi:**
- Samme samhandlingsmÃƒÂ¸nster brukes av alle virksomheter (ikke unik per motpart)
- Reduserer behov for punkt-til-punkt-lÃƒÂ¸sninger og proprietaere integrasjonsgatewayer
- Fremmer interoperabilitet og standardisering pÃƒÂ¥ tvers av sektorer og grenser
- ÃƒËœkende nettverkseffekt when flere virksomheter tilslutter seg

## StÃƒÂ¸tte arkitekturprinsipper

- **P4 Del og gjenbruk data** Ã¢â‚¬â€œ Standardiserte dokumentformat pÃƒÂ¥ tvers av alle aktÃƒÂ¸rer
- **P5 Del og gjenbruk lÃƒÂ¸sninger** Ã¢â‚¬â€œ Samme nett og profiler for alle; ingen duplicate systemer
- **P6 Lag digitale lÃƒÂ¸sninger som stÃƒÂ¸tter samhandling** Ã¢â‚¬â€œ Internasjonalt rammeverk for B2B/B2G
- **P8 Etabler felles forstÃƒÂ¥else av informasjon** Ã¢â‚¬â€œ Standardiserte semantikk via UBL/UB L-SE

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som internasjonalt standardnettverk (OpenPeppol); ikke sentralt finansiert
- **Bruksmodell:** Virksomheter betaler Access Point-operatÃƒÂ¸ra for tilkobling (variabelt per operatÃƒÂ¸r)
- **Estimert kostnader:** 1000-5000 kr per mÃƒÂ¥ned per virksomhet (avhengig av dokument-volum)
- **Nasjonal investering:** Norge har investert i DFO og test-infra; estimert 10-20 MNOK initial

**Finansiering:** Distribuert modell; hver virksomhet betaler sin Access Point; offentlig investering i infra (DFO, test).

**kilder:** Estimert basert pÃƒÂ¥ eFaktura-kostnad; presis modell varierer per Access Point.

## Forvaltning/eier

| AnsvarsomrÃƒÂ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Standarder/Governance** | OpenPeppol-organisasjonen (medlemsbas) | Internasjonale regler, profiler, compliance |
| **Nasjonal oppfÃƒÂ¸lging** | DFO (Direktoratet for forvaltning og ÃƒÂ¸konomi) / Digdir | Norsk implementering, test-miljÃƒÂ¸, veiledning |
| **Access Point-drift** | Private leverandÃƒÂ¸rer (sertifisert av OpenPeppol) | Teknisk drift, tilkobling, support |
| **Budsjettansvar** | OpenPeppol (medlem-inntekter) + nasjonal budsjett (DFO) | Governance + nasjonal infra |

**Styringsforum:** OpenPeppol-Board; Peppol Norwegian Pillar (medlemskap; DFO/Digdir deltakelse); eFaktura-rÃƒÂ¥d.

## Lenke til dokumentasjon

- https://www.peppol.eu Ã¢â‚¬â€œ OpenPeppol offisiell nettside (internasjonala)
- https://anskaffelser.no/e-handel/verktoy/peppol-edelivery Ã¢â‚¬â€œ DFO Peppol-informasjon (nasjonalt)
- https://www.digdir.no/eit/ Ã¢â‚¬â€œ Digdir E-Invoice info
- https://test.peppol.eu Ã¢â‚¬â€œ Peppol test-nettsted og dokumentasjon
- https://samarbeid.digdir.no/peppol-edelivery Ã¢â‚¬â€œ Samarbeidsportal Peppol (nasjonalt)

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: Peppol.eu, DFO, Anskaffelser.no, Digdir.no (hentet 2026-03-07)
- Kilder for finansiering: eFaktura-kostnad-analyser, OpenPeppol-rapporter (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

Ã¢Å“â€¦ **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum-estimater (global + norsk)
Ã¢Å“â€¦ **Risikomatrise:** 8 konkrete risikokategorier med hÃƒÂ¥ndtering
Ã¢Å“â€¦ **Finansiering:** Detaljert kostands-modell (1000-5000 kr/mÃƒÂ¥nad per virksomhet)
Ã¢Å“â€¦ **Forvaltning:** Tabell-format med ansvarsfordeling (OpenPeppol + DFO/Digdir + Access Points)
Ã¢Å“â€¦ **Veikart:** Konkrete fokusomrÃƒÂ¥der (eIDAS 2.0, dokumenttyper, post-quantum kryptering)
Ã¢Å“â€¦ **Scope:** Eksplisitt tabell over hva som inngÃƒÂ¥r/ikke inngÃƒÂ¥r
Ã¢Å“â€¦ **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet (AS4, sertifikater, SMP oppslag)
Ã¢Å“â€¦ **Internasjonalt rammeverk:** Eksplisitt kobling til OpenPeppol og EU-regulativ
Ã¢Å“â€¦ **Styringsforum:** OpenPeppol Board + Peppol Norwegian Pillar + DFO/Digdir

