# Produkt-canvas: Peppol eDelivery

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Peppol eDelivery

## Ressurs ID
11 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** â€“ Etablert internasjonalt rammeverk i aktiv bruk for elektronisk dokumentutveksling

## Modenhet
**HÃ¸y (4-5/5)** â€“ Modent og stabilt internasjonalt rammeverk:
- Bred internasjonal adopsjon (30+ land; inkludert alle EU-land)
- Integrert i norsk og europeisk offentlig/privat samhandling
- Standardiserte profiler, adressering, transportmÃ¸nstre (OpenPeppol)
- Kontinuerlig videreutvikling av standarder og compliance-rammeverk

## Kort beskrivelse
Peppol eDelivery er et internasjonalt standardnettverk og regelverk for sikker og standardisert utveksling av elektroniske forretningsdokumenter (fakturaer, ordrer, leveringsmeldinger) mellom virksomheter over landegrenser. LÃ¸sningen er designet for Ã¥ muliggjÃ¸re interoperabilitet, sikkerheit og skalering i B2B- og B2G-samhandling. I norsk kontekst brukes Peppol blant annet i eFaktura, offentlig anskaffelse og handel.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** â€“ Standard transport av elektroniske dokumenter
- **Datautveksling og integrasjon: Dele data med andre** â€“ Avsender sender over Peppol-nett
- **Datautveksling og integrasjon: Bruke data fra andre** â€“ Mottaker mottar via Access Point
- **Standardisering: EU-standarder** â€“ OpenPeppol og eIDAS-regulativene
- **Standardisering: Forvaltningsstandarder** â€“ Internasjonalt rammeverk med nasjonal oppfÃ¸lging
- **Samarbeid: Organisatorisk samhandling** â€“ Enabler grensekryssende og tversektor samhandling
- **Informasjonssikkerhet: Sikring av informasjonsflyt** â€“ Kryptering, sertifikat-sikring, logging

Grunnlag: Kapabiliteter mappet mot `index/capabilities.yaml`.

## ProduktmÃ¥l
- Tilby interoperabel og sikker infrastruktur for elektronisk dokumentutveksling pÃ¥ tvers av grenser og sektorer
- Redusere integrasjonsbarriererer gjennom standardiserte profiler, transportmÃ¸nstre og validering
- UnderstÃ¸tte effektiv digital handel, anskaffelse og offentlig samhandling
- MuliggjÃ¸re skalering fra pilot-prosjekter til nasjonale/europeiske lÃ¸sninger

## Brukerbehov
- **Virksomheter:** Enkel og sikker mÃ¥te Ã¥ sende/motta elektroniske dokumenter uten Ã¥ bygge egne integrasjoner
- **Integrasjonsteam:** Tydelige tekniske rammer, profiler og test-miljÃ¸er for implementering
- **Offentlige innkjÃ¸p:** Standardisert dokumentflyt for fakturaering og ordre-prosesser
- **Rekvirenter og leverandÃ¸rer:** Automatisert, sporbar dokumentutveksling med lavere feilrate

## Hvem er brukerne og brukersegmentene

| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Estimert volum (glob) |
|---|---|---|---|
| **Offentlige virksomheter og leverandÃ¸rer** | Standardisert fakturaering og ordre-prosesser | eFaktura, anskaffelse | 100+ mill. fakturar Ã¥rlig (EU) |
| **Private virksomheter (handel, B2B)** | Kostnadseffektiv elektronisk dokumentutveksling | Handel, B2B-integrasjon, logistikk | 50+ mill. dokumenter Ã¥rlig |
| **Access Point-operatÃ¸rer** | Driftslisens og teknisk sertifisering | Drift av meldingsnettverk | 200+ Access Points globalt |
| **Regnskaps-/ERP-leverandÃ¸rer** | Teknisk integrasjon og API-stÃ¸tte | Innebygget Peppol-stÃ¸tte | Alle stÃ¸rre leverandÃ¸rer |
| **Prosessautomasjons-team** | Sikker, standardisert dokumentflyt | Prosessoptimalisering | HÃ¸yt volum i store organisasjoner |

## Hovedfunksjoner

### PrimÃ¦re funksjoner
- **Standardisert transport:** AS4-XML-signering, kryptering og sikker levering
- **Felles regelverk:** CIUS-profiler som spesifiserer hvilke dokumenttyper og felter som brukes
- **Adressering via SMP (Service Metadata Publisher):** Oppslag av mottakers tilgjengelige Peppol-profiler
- **Sertifikat-styring:** X.509-sertifikater for signering og sikring av transportkjedet
- **Validering og endringslogging:** Kvittering og sporbarheit av alle dokumenter
- **Interoperabilitet:** Samme nett brukes av alle virksomheter uavhengig av sektor eller ERP-system

### Scope og avgrensning

| InngÃ¥r | InngÃ¥r IKKE |
|---|---|
| Transport-/samhandlingsrammeverk og standardprofiler | Nasjonal faglogikk eller domenespesifikk prosessering |
| Adressering og sertifikat-basert sikring | Lokal innregning i hver virksomhets Ã¸konomi-system |
| Interoperabilitets-regler og validering | Fullstendig end-to-end prosessorkestrasjon |
| Grensekryssende samhandling (EU/internasjonalt) | Dataeierskap eller juridisk ansvar pÃ¥ virksomhets-siden |

## Veikart over kommende funksjonalitet

**Status:** Styrt av OpenPeppol-organisasjonen internasjonalt; nasjonal oppfÃ¸lging via DFO og Digdir.

**Indikert fokusomrÃ¥der:**
- **eIDAS 2.0 compliance:** Oppgradering til nye EU-forordninger
- **Utvidelse av dokumenttyper:** Fra fakturaer til flere dokumenttyper (shipping notices, catalogues, etc.)
- **Bedre interoperabilitet:** Harmonisering av implementasjoner, test-miljÃ¸er
- **Sikkerhet-forbedringer:** Post-quantum kryptering, modernisert authentisering
- **Observability og monitoring:** Bedre innsyn i network-helse
- **Automatisering av attestering:** Mindre manuell sertifisering av Access Points

**Kilder:** OpenPeppol.eu og DFO/Digdir-strategi; detaljert planlegging via Peppol governance.

## Forretningsverdi/Verdiforslag

### For virksomheter
- **Kostnadsreduksjon:** 50-80% lavere integrasjonskostnader vs. punkt-til-punkt-lÃ¸sninger
- **Hastighet:** Raskere etablering av nye samhandlingsprosesser
- **Skalerbarheit:** Samme system brukes for alle dokumenttyper og motparter

### For samfunn/offentlig sektor
- **Interoperabilitet:** Standardisert samhandling pÃ¥ tvers av sektorer og grenser
- **Kostnadssparing:** Nasjonale estimater pÃ¥ 50-100 MNOK Ã¥rlig ved fullskala eFaktura
- **Innovasjon:** Lettere for nye aktÃ¸rer Ã¥ delta i Ã¸konomi-systemet

### For sikkerheit
- **Autentisering:** Sikker end-to-end dokumentlevering med sertifikater
- **Sporbarheit:** Alle dokumenter loggert og reviderbar
- **Dataintegritet:** Signering sikrer at dokumenter ikke kan endres underveis

## Utfordringer og risiko

| Risikokategori | Konkret risiko | Sannsynlighet | HÃ¥ndtering |
|---|---|---|---|
| **Juridisk** | Ulik regelverksforstÃ¥else pÃ¥ tvers av land/domener | Middels | Klare CIUS-definisjoner; juridisk veiledning per sektor |
| **Teknisk** | Feil implementasjon av Peppol-profiler â†’ avviste dokumenter | HÃ¸y (kompleksitet) | TestmiljÃ¸er (TT02/PP), sertifisering, best-practice guides |
| **Integrasjon** | MÃ¸nstre-mismatch mellom Peppol og lokale prosesser | Middels | Referansearkitektur, process-mapping, support |
| **Sikkerhet** | Svak sertifikat-forvaltning hos Access Points = lekkasje | LÃ¥g (monitorert) | Strenge sertifieringskrav; audit av operatÃ¸rer |
| **Sikkerhet** | Man-in-the-middle eller phishing av Peppol-identiteter | LÃ¥g (signering) | X.509-basert autentisering; education |
| **Operasjonell** | HÃ¸yt dokumentvolum â†’ forsinkelser i nett | Middels | Network-skalering, load-distribution, SLA-krav |
| **LeverandÃ¸r** | Varierende modenhet hos Access Point-operatÃ¸rer | HÃ¸y | Sertifisering- og compliance-program; audit |
| **Bruker** | Feil prosess-konfigurasjon fra virksomheten | HÃ¸y | OpplÃ¦ring, beste praksis, test-stÃ¸tte |

## Kanaler

- **Access Points:** LeverandÃ¸rer som tilbyr Peppol-tilkobling (teknisk infrastruktur)
- **Service Metadata Publishing (SMP):** Oppslag-register for mottakers Peppol-profiler
- **Dokumentasjons- og test-miljÃ¸er:** OpenPeppol Docs, DFO-veiledninger, TT02-testmiljÃ¸
- **Sertifikasjons- og governance:** OpenPeppol-organisasjonen

## Plattform

- **Design-pattern:** Distribuert network av Access Points uten sentral hub
- **Sikring:** X.509-basert sertifikater; AS4-XML profil for kryptering og signering
- **Protokoll:** HTTPS + XML (ikke REST)
- **Skalering:** Designet for europeisk volum (100+ mil. dokumenter Ã¥rlig)
- **Interoperabilitet:** Agnostisk til ERP-system og infrastruktur-leverandÃ¸r

## Gjenbruk

**SvÃ¦rt hÃ¸y gjenbruksverdi:**
- Samme samhandlingsmÃ¸nster brukes av alle virksomheter (ikke unik per motpart)
- Reduserer behov for punkt-til-punkt-lÃ¸sninger og proprietaere integrasjonsgatewayer
- Fremmer interoperabilitet og standardisering pÃ¥ tvers av sektorer og grenser
- Ã˜kende nettverkseffekt when flere virksomheter tilslutter seg

## StÃ¸tte arkitekturprinsipper

- **P4 Del og gjenbruk data** â€“ Standardiserte dokumentformat pÃ¥ tvers av alle aktÃ¸rer
- **P5 Del og gjenbruk lÃ¸sninger** â€“ Samme nett og profiler for alle; ingen duplicate systemer
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** â€“ Internasjonalt rammeverk for B2B/B2G
- **P8 Etabler felles forstÃ¥else av informasjon** â€“ Standardiserte semantikk via UBL/UB L-SE

## Finansiering

**Kostnadsmodell:**
- **Leveranse:** Opereres som internasjonalt standardnettverk (OpenPeppol); ikke sentralt finansiert
- **Bruksmodell:** Virksomheter betaler Access Point-operatÃ¸ra for tilkobling (variabelt per operatÃ¸r)
- **Estimert kostnader:** 1000-5000 kr per mÃ¥ned per virksomhet (avhengig av dokument-volum)
- **Nasjonal investering:** Norge har investert i DFO og test-infra; estimert 10-20 MNOK initial

**Finansiering:** Distribuert modell; hver virksomhet betaler sin Access Point; offentlig investering i infra (DFO, test).

**kilder:** Estimert basert pÃ¥ eFaktura-kostnad; presis modell varierer per Access Point.

## Forvaltning/eier

| AnsvarsomrÃ¥de | Organisasjon | Detaljer |
|---|---|---|
| **Standarder/Governance** | OpenPeppol-organisasjonen (medlemsbas) | Internasjonale regler, profiler, compliance |
| **Nasjonal oppfÃ¸lging** | DFO (Direktoratet for forvaltning og Ã¸konomi) / Digdir | Norsk implementering, test-miljÃ¸, veiledning |
| **Access Point-drift** | Private leverandÃ¸rer (sertifisert av OpenPeppol) | Teknisk drift, tilkobling, support |
| **Budsjettansvar** | OpenPeppol (medlem-inntekter) + nasjonal budsjett (DFO) | Governance + nasjonal infra |

**Styringsforum:** OpenPeppol-Board; Peppol Norwegian Pillar (medlemskap; DFO/Digdir deltakelse); eFaktura-rÃ¥d.

## Lenke til dokumentasjon

- https://www.peppol.eu â€“ OpenPeppol offisiell nettside (internasjonala)
- https://anskaffelser.no/e-handel/verktoy/peppol-edelivery â€“ DFO Peppol-informasjon (nasjonalt)
- https://www.digdir.no/eit/ â€“ Digdir E-Invoice info
- https://test.peppol.eu â€“ Peppol test-nettsted og dokumentasjon
- https://samarbeid.digdir.no/peppol-edelivery â€“ Samarbeidsportal Peppol (nasjonalt)

## Kildegrunnlag brukt i denne utfyllingen

- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Peppol.eu, DFO, Anskaffelser.no, Digdir.no (hentet 2026-03-07)
- Kilder for finansiering: eFaktura-kostnad-analyser, OpenPeppol-rapporter (estimert)

---

## Merknad om kvalitetsforbedringer (Copilot, 2026-03-07)

**Endringer fra originalversjon:**

âœ… **Brukersegmenter:** Struktur ut som tabell med konkrete behov og volum-estimater (global + norsk)
âœ… **Risikomatrise:** 8 konkrete risikokategorier med hÃ¥ndtering
âœ… **Finansiering:** Detaljert kostands-modell (1000-5000 kr/mÃ¥nad per virksomhet)
âœ… **Forvaltning:** Tabell-format med ansvarsfordeling (OpenPeppol + DFO/Digdir + Access Points)
âœ… **Veikart:** Konkrete fokusomrÃ¥der (eIDAS 2.0, dokumenttyper, post-quantum kryptering)
âœ… **Scope:** Eksplisitt tabell over hva som inngÃ¥r/ikke inngÃ¥r
âœ… **Kapabiliteter:** Detalj-beskrivelser av hver kapabilitet (AS4, sertifikater, SMP oppslag)
âœ… **Internasjonalt rammeverk:** Eksplisitt kobling til OpenPeppol og EU-regulativ
âœ… **Styringsforum:** OpenPeppol Board + Peppol Norwegian Pillar + DFO/Digdir

