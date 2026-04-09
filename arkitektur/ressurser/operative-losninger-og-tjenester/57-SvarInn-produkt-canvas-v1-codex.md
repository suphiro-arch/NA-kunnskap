# Produkt-canvas: SvarInn

## Navn
SvarInn

## Ressurs ID
KS-007

## Status/Livsfase
**Produksjon** - etablert mottakstjeneste i KS Digital for innkommende post fra andre virksomheter som bruker SvarUt.

**Fakta:** KS beskriver SvarInn som tjenesten for innkommet post til kommuner og andre virksomheter som har avtale med KS. Statussiden for FIKS viser `SvarInn` som operativ tjeneste.

## Modenhet
**HÃ¸y funksjonell modenhet** - lÃ¸sningen har tydelig funksjon, kjent integrasjonsmÃ¸nster og publisert veiledning for oppsett i sak- og arkivsystemer.
- Tjenesten er avgrenset til mottak og import av forsendelser, og fremstÃ¥r derfor mer presis og forutsigbar enn en bredere meldingsplattform.
- Kildene viser bÃ¥de maskinell mottaksflyt, sikkerhetskrav rundt sertifikater og praktiske rutiner for feilhÃ¥ndtering.
- Modenheten er hÃ¸y for selve mottakslÃ¸pet, men faktisk verdi avhenger av at lokale fagsystemer er riktig konfigurert.

## Kort beskrivelse
SvarInn er en API-basert tjeneste og komplement til SvarUt. LÃ¸sningen tar imot innkommende post fra andre virksomheter som bruker SvarUt, og gjÃ¸r den tilgjengelig for sak- og arkivsystemer eller andre fagsystemer i kommunen. Produktet er sÃ¦rlig relevant nÃ¥r virksomheten trenger et standardisert og sentralisert mottakslÃ¸p for digital post mellom offentlige aktÃ¸rer, uten Ã¥ etablere egne kanalspesifikke mottaksintegrasjoner.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** er kjernefunksjonen fordi SvarInn henter, dekrypterer og leverer forsendelser videre til mottakersystemene i kommunen.
- **Samarbeid: Organisatorisk samhandling** er direkte relevant fordi lÃ¸sningen gir et felles mÃ¸nster for innkommende post mellom kommuner og andre offentlige virksomheter som bruker samme samhandlingslÃ¸p.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals kilder brukt i denne arbeidsÃ¸kten.

## ProduktmÃ¥l
Dokumenterte mÃ¥l:
- Gi kommuner og andre virksomheter en tjeneste for innkommet post nÃ¥r avsender bruker SvarUt.
- Automatisere nedlasting og import av forsendelser direkte i sak- og arkivsystemer eller andre fagsystemer.
- GjÃ¸re det mulig Ã¥ motta sensitive forsendelser gjennom sertifikatbasert dekryptering.

Operative mÃ¥l utledet fra kildene:
- Redusere behovet for manuelle mottaksrutiner for digital post mellom offentlige virksomheter.
- Gi kommuner et mer standardisert og forutsigbart mottakslÃ¸p for innkommende dokumenter.
- Oppdage og hÃ¥ndtere importfeil raskere gjennom varsling og dokumenterte feilhÃ¥ndteringsrutiner.

## Brukerbehov
- Kommuner trenger en felles tjeneste for Ã¥ ta imot digital post fra andre offentlige virksomheter.
- Sak- og arkivsystemer trenger et standardisert grensesnitt for automatisk nedlasting og import av forsendelser.
- Virksomheter trenger Ã¥ kunne motta ogsÃ¥ sensitive forsendelser pÃ¥ en sikker mÃ¥te.
- Forvaltere trenger tydelig oppsett, sertifikatforvaltning og rutiner for feilhÃ¥ndtering nÃ¥r import svikter.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Kommuner og andre offentlige virksomheter | Standardisert mottak av digital post | Innkommende dokumenter og meldinger fra andre virksomheter | PrimÃ¦rbrukere |
| Sak- og arkivsystemer og andre fagsystemer | Automatisk nedlasting og import av forsendelser | Integrasjon mot innkommende postlÃ¸p | Teknisk kjerne i bruksmÃ¸nsteret |
| Tekniske forvaltere | Konfigurere mottakersystem, sertifikater og feilhÃ¥ndtering | Oppsett og drift av mottakslÃ¸pet | MÃ¥ hÃ¥ndtere sertifikater og overvÃ¥king |
| KS Digital | Forvalte tjenesten og stÃ¸tte innfÃ¸ring | Opprettelse av mottakersystemer, veiledning og videreutvikling | Sentral tjenesteforvalter |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- SvarInn fungerer som mottaksservice for dokumenter og forsendelser som er sendt via SvarUt. Dette gjÃ¸r lÃ¸sningen relevant nÃ¥r behovet er Ã¥ hente innkommende digital post inn i kommunens egne systemer, ikke Ã¥ sende eller produsere meldinger.
- Tjenesten automatiserer nedlasting og import av forsendelser direkte i sak- og arkivsystemer eller andre fagsystemer. Det skiller produktet fra en ren portal eller manuell innboks, fordi hovedverdien ligger i maskinell integrasjon.
- SvarInn hÃ¥ndterer ogsÃ¥ sensitive forsendelser. Kommunen mÃ¥ legge inn offentlig sertifikat og bruke privat nÃ¸kkel til Ã¥ dekryptere forsendelsesfilene som lastes ned. Dette gjÃ¸r at sikkerhetskrav er en del av produktets praktiske kjernefunksjon.
- LÃ¸sningen varsler nÃ¥r forsendelser ikke hentes innen angitt tidsrom. Dermed stÃ¸tter produktet ogsÃ¥ operativ oppfÃ¸lging av feil i mottakskjeden, ikke bare selve overfÃ¸ringen.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Mottak og import av innkommende post fra SvarUt | UtgÃ¥ende dokumentdistribusjon |
| Integrasjon med sak- og arkivsystemer og andre fagsystemer | Produksjon av dokumentinnhold |
| Sertifikatbasert dekryptering av sensitive forsendelser | Lokal saksbehandling etter at dokumentet er importert |
| Varsling ved manglende henting og stÃ¸tte for feilhÃ¥ndtering | Full kommunikasjonsplattform for alle meldingstyper |

## Veikart over kommende funksjonalitet
**Fakta:** Jeg fant ikke et samlet offentlig roadmap for SvarInn i denne arbeidsÃ¸kten. Produktsidene viser operativ bruk, teknisk dokumentasjon og praktiske veiledere, men ikke et tidsfestet veikart.

**Deduksjon:** Videreutviklingen vil trolig vÃ¦re knyttet til robusthet i mottakslÃ¸pet, bedre integrasjoner mot fagsystemer og videre forbedring av sikker hÃ¥ndtering av sensitive forsendelser.

## Forretningsverdi/Verdiforslag
### For kommuner og offentlige virksomheter
- Gir ett standardisert mottakslÃ¸p for innkommende digital post fra andre offentlige aktÃ¸rer.
- Reduserer behovet for Ã¥ bygge egne mottaksintegrasjoner mot flere avsendere eller kanaler.

### For tekniske miljÃ¸er
- Gir et kjent integrasjonsmÃ¸nster for nedlasting, import og overvÃ¥king av innkommende forsendelser.
- GjÃ¸r sikker hÃ¥ndtering av sensitive forsendelser mer forutsigbar gjennom dokumenterte sertifikatkrav.

### For sektoren
- UnderstÃ¸tter mer ensartet samhandling om dokumentflyt mellom offentlige virksomheter.
- Reduserer variasjon i hvordan innkommende post hÃ¥ndteres teknisk pÃ¥ tvers av kommuner.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Feil hÃ¥ndtering av sensitiv post kan gi brudd pÃ¥ lovkrav og taushetsplikt. | Bruke korrekt hjemmel, klassifisering og sikre at mottak bare er tilgjengelig for riktig rolle og system. |
| Teknisk | Import kan svikte i mottakende fagsystem selv om SvarInn fungerer. | OvervÃ¥ke import, bruke varsling og etablere tydelige rutiner for feilhÃ¥ndtering. |
| Sikkerhet | Feil sertifikatoppsett eller nÃ¸kkelhÃ¥ndtering kan hindre mottak eller svekke sikkerheten. | Dokumentert sertifikatforvaltning, test av oppsett og kontroll av nÃ¸kkelbruk. |
| LeverandÃ¸r | Virksomheten blir avhengig av bÃ¥de KS Digital og lokale systemleverandÃ¸rer for at hele mottakskjeden skal virke. | Tydelig ansvarsdeling, testregimer og teknisk dokumentasjon mot fagsystemleverandÃ¸rer. |
| Brukeropplevelse | Feil i import kan gjÃ¸re at viktige dokumenter ikke blir synlige i arbeidsprosessene. | Varsling ved manglende henting, manuelle nÃ¸drutiner og god operativ oppfÃ¸lging. |

## Kanaler
- https://ksdigital.no/tjenestene/svarut-tjenesten/svarinn/
- https://ksdigital.no/tjenestene/svarut-tjenesten/ks-svarinn/
- https://status.fiks.ks.no

## Plattform
SvarInn er en sentralt forvaltet mottakstjeneste i KS Digital og inngÃ¥r i samme samhandlingsomrÃ¥de som SvarUt.

**Fakta:**
- Tjenesten er laget for Ã¥ hente innkommende post fra virksomheter som bruker SvarUt.
- Bruk av SvarInn forutsetter avtale med KS Digital og oppsett av mottakersystem.
- Statussiden viser `SvarInn` som egen operativ komponent i FIKS-plattformen.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur, detaljert teknologistakk og full endringsplan for videreutvikling.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Tjenesten kan brukes av mange kommuner og andre offentlige virksomheter med samme behov for standardisert mottak av digital post.
- Gjenbruksverdien ligger i felles mottakslogikk og integrasjonsmÃ¸nster, ikke i lokal forretningslogikk eller saksbehandling.

## StÃ¸tter arkitekturprinsipper
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** - SvarInn standardiserer mottak av innkommende post mellom offentlige virksomheter og gjÃ¸r samhandlingsmÃ¸nsteret mer forutsigbart.
- **P7 SÃ¸rg for tillit til oppgavelÃ¸sningen** - sertifikatbruk, dekryptering og kontroll av sensitive forsendelser er sentrale deler av lÃ¸sningen.

## Finansiering
**Fakta:** For Ã¥ ta i bruk SvarInn mÃ¥ virksomheten ha avtale med KS Digital, og KS opplyser at innkommende post gjennom SvarInn ikke prises separat slik utgÃ¥ende post gjÃ¸r gjennom SvarUt.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full modell for sentral finansiering, forvaltningskostnader og eventuell intern kryssubsidiering mot SvarUt.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsidene og avtalegrunnlaget ligger hos KS Digital. |
| Driftsansvar | Ikke offentlig detaljert spesifisert i brukte kilder | Statusside og tjenestesider viser operativ drift, men ikke full ansvarsmodell. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Prisinformasjon er delvis beskrevet gjennom SvarUt/SvarInn-sammenheng, men ikke full finansieringsmodell. |
| Styringsmodell | KS Digital som sentral forvalter av tjenesten | FremgÃ¥r av tjenestesider, oppsett og avtalevilkÃ¥r. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/svarut-tjenesten/svarinn/
- https://ksdigital.no/tjenestene/svarut-tjenesten/ks-svarinn/
- https://status.fiks.ks.no

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://ksdigital.no/tjenestene/svarut-tjenesten/svarinn/ (hentet 2026-03-19)
- Nettkilde: https://ksdigital.no/tjenestene/svarut-tjenesten/ks-svarinn/ (hentet 2026-03-19)
- Nettkilde: https://status.fiks.ks.no/ (hentet 2026-03-19)
- Nettkilde: https://ksdigital.no/avtaler-og-priser/ (hentet 2026-03-19)


