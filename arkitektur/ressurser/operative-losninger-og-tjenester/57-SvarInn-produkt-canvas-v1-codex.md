# Produkt-canvas: SvarInn

## Navn
SvarInn

## Ressurs ID
KS-007

## Status/Livsfase
**Produksjon** - etablert mottakstjeneste i KS Digital for innkommende post fra andre virksomheter som bruker SvarUt.

**Fakta:** KS beskriver SvarInn som tjenesten for innkommet post til kommuner og andre virksomheter som har avtale med KS. Statussiden for FIKS viser `SvarInn` som operativ tjeneste.

## Modenhet
**Høy funksjonell modenhet** - løsningen har tydelig funksjon, kjent integrasjonsmønster og publisert veiledning for oppsett i sak- og arkivsystemer.
- Tjenesten er avgrenset til mottak og import av forsendelser, og fremstår derfor mer presis og forutsigbar enn en bredere meldingsplattform.
- Kildene viser både maskinell mottaksflyt, sikkerhetskrav rundt sertifikater og praktiske rutiner for feilhåndtering.
- Modenheten er høy for selve mottaksløpet, men faktisk verdi avhenger av at lokale fagsystemer er riktig konfigurert.

## Kort beskrivelse
SvarInn er en API-basert tjeneste og komplement til SvarUt. Løsningen tar imot innkommende post fra andre virksomheter som bruker SvarUt, og gjør den tilgjengelig for sak- og arkivsystemer eller andre fagsystemer i kommunen. Produktet er særlig relevant når virksomheten trenger et standardisert og sentralisert mottaksløp for digital post mellom offentlige aktører, uten å etablere egne kanalspesifikke mottaksintegrasjoner.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** er kjernefunksjonen fordi SvarInn henter, dekrypterer og leverer forsendelser videre til mottakersystemene i kommunen.
- **Samarbeid: Organisatorisk samhandling** er direkte relevant fordi løsningen gir et felles mønster for innkommende post mellom kommuner og andre offentlige virksomheter som bruker samme samhandlingsløp.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals kilder brukt i denne arbeidsøkten.

## Produktmål
Dokumenterte mål:
- Gi kommuner og andre virksomheter en tjeneste for innkommet post når avsender bruker SvarUt.
- Automatisere nedlasting og import av forsendelser direkte i sak- og arkivsystemer eller andre fagsystemer.
- Gjøre det mulig å motta sensitive forsendelser gjennom sertifikatbasert dekryptering.

Operative mål utledet fra kildene:
- Redusere behovet for manuelle mottaksrutiner for digital post mellom offentlige virksomheter.
- Gi kommuner et mer standardisert og forutsigbart mottaksløp for innkommende dokumenter.
- Oppdage og håndtere importfeil raskere gjennom varsling og dokumenterte feilhåndteringsrutiner.

## Brukerbehov
- Kommuner trenger en felles tjeneste for å ta imot digital post fra andre offentlige virksomheter.
- Sak- og arkivsystemer trenger et standardisert grensesnitt for automatisk nedlasting og import av forsendelser.
- Virksomheter trenger å kunne motta også sensitive forsendelser på en sikker måte.
- Forvaltere trenger tydelig oppsett, sertifikatforvaltning og rutiner for feilhåndtering når import svikter.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og andre offentlige virksomheter | Standardisert mottak av digital post | Innkommende dokumenter og meldinger fra andre virksomheter | Primærbrukere |
| Sak- og arkivsystemer og andre fagsystemer | Automatisk nedlasting og import av forsendelser | Integrasjon mot innkommende postløp | Teknisk kjerne i bruksmønsteret |
| Tekniske forvaltere | Konfigurere mottakersystem, sertifikater og feilhåndtering | Oppsett og drift av mottaksløpet | Må håndtere sertifikater og overvåking |
| KS Digital | Forvalte tjenesten og støtte innføring | Opprettelse av mottakersystemer, veiledning og videreutvikling | Sentral tjenesteforvalter |

## Hovedfunksjoner
### Primære funksjoner
- SvarInn fungerer som mottaksservice for dokumenter og forsendelser som er sendt via SvarUt. Dette gjør løsningen relevant når behovet er å hente innkommende digital post inn i kommunens egne systemer, ikke å sende eller produsere meldinger.
- Tjenesten automatiserer nedlasting og import av forsendelser direkte i sak- og arkivsystemer eller andre fagsystemer. Det skiller produktet fra en ren portal eller manuell innboks, fordi hovedverdien ligger i maskinell integrasjon.
- SvarInn håndterer også sensitive forsendelser. Kommunen må legge inn offentlig sertifikat og bruke privat nøkkel til å dekryptere forsendelsesfilene som lastes ned. Dette gjør at sikkerhetskrav er en del av produktets praktiske kjernefunksjon.
- Løsningen varsler når forsendelser ikke hentes innen angitt tidsrom. Dermed støtter produktet også operativ oppfølging av feil i mottakskjeden, ikke bare selve overføringen.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Mottak og import av innkommende post fra SvarUt | Utgående dokumentdistribusjon |
| Integrasjon med sak- og arkivsystemer og andre fagsystemer | Produksjon av dokumentinnhold |
| Sertifikatbasert dekryptering av sensitive forsendelser | Lokal saksbehandling etter at dokumentet er importert |
| Varsling ved manglende henting og støtte for feilhåndtering | Full kommunikasjonsplattform for alle meldingstyper |

## Veikart over kommende funksjonalitet
**Fakta:** Jeg fant ikke et samlet offentlig roadmap for SvarInn i denne arbeidsøkten. Produktsidene viser operativ bruk, teknisk dokumentasjon og praktiske veiledere, men ikke et tidsfestet veikart.

**Deduksjon:** Videreutviklingen vil trolig være knyttet til robusthet i mottaksløpet, bedre integrasjoner mot fagsystemer og videre forbedring av sikker håndtering av sensitive forsendelser.

## Forretningsverdi/Verdiforslag
### For kommuner og offentlige virksomheter
- Gir ett standardisert mottaksløp for innkommende digital post fra andre offentlige aktører.
- Reduserer behovet for å bygge egne mottaksintegrasjoner mot flere avsendere eller kanaler.

### For tekniske miljøer
- Gir et kjent integrasjonsmønster for nedlasting, import og overvåking av innkommende forsendelser.
- Gjør sikker håndtering av sensitive forsendelser mer forutsigbar gjennom dokumenterte sertifikatkrav.

### For sektoren
- Understøtter mer ensartet samhandling om dokumentflyt mellom offentlige virksomheter.
- Reduserer variasjon i hvordan innkommende post håndteres teknisk på tvers av kommuner.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil håndtering av sensitiv post kan gi brudd på lovkrav og taushetsplikt. | Bruke korrekt hjemmel, klassifisering og sikre at mottak bare er tilgjengelig for riktig rolle og system. |
| Teknisk | Import kan svikte i mottakende fagsystem selv om SvarInn fungerer. | Overvåke import, bruke varsling og etablere tydelige rutiner for feilhåndtering. |
| Sikkerhet | Feil sertifikatoppsett eller nøkkelhåndtering kan hindre mottak eller svekke sikkerheten. | Dokumentert sertifikatforvaltning, test av oppsett og kontroll av nøkkelbruk. |
| Leverandør | Virksomheten blir avhengig av både KS Digital og lokale systemleverandører for at hele mottakskjeden skal virke. | Tydelig ansvarsdeling, testregimer og teknisk dokumentasjon mot fagsystemleverandører. |
| Brukeropplevelse | Feil i import kan gjøre at viktige dokumenter ikke blir synlige i arbeidsprosessene. | Varsling ved manglende henting, manuelle nødrutiner og god operativ oppfølging. |

## Kanaler
- https://ksdigital.no/tjenestene/svarut-tjenesten/svarinn/
- https://ksdigital.no/tjenestene/svarut-tjenesten/ks-svarinn/
- https://status.fiks.ks.no

## Plattform
SvarInn er en sentralt forvaltet mottakstjeneste i KS Digital og inngår i samme samhandlingsområde som SvarUt.

**Fakta:**
- Tjenesten er laget for å hente innkommende post fra virksomheter som bruker SvarUt.
- Bruk av SvarInn forutsetter avtale med KS Digital og oppsett av mottakersystem.
- Statussiden viser `SvarInn` som egen operativ komponent i FIKS-plattformen.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur, detaljert teknologistakk og full endringsplan for videreutvikling.

## Gjenbruk
**Høy gjenbruksverdi:**
- Tjenesten kan brukes av mange kommuner og andre offentlige virksomheter med samme behov for standardisert mottak av digital post.
- Gjenbruksverdien ligger i felles mottakslogikk og integrasjonsmønster, ikke i lokal forretningslogikk eller saksbehandling.

## Støtter arkitekturprinsipper
- **P6 Lag digitale løsninger som støtter samhandling** - SvarInn standardiserer mottak av innkommende post mellom offentlige virksomheter og gjør samhandlingsmønsteret mer forutsigbart.
- **P7 Sørg for tillit til oppgaveløsningen** - sertifikatbruk, dekryptering og kontroll av sensitive forsendelser er sentrale deler av løsningen.

## Finansiering
**Fakta:** For å ta i bruk SvarInn må virksomheten ha avtale med KS Digital, og KS opplyser at innkommende post gjennom SvarInn ikke prises separat slik utgående post gjør gjennom SvarUt.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full modell for sentral finansiering, forvaltningskostnader og eventuell intern kryssubsidiering mot SvarUt.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsidene og avtalegrunnlaget ligger hos KS Digital. |
| Driftsansvar | Ikke offentlig detaljert spesifisert i brukte kilder | Statusside og tjenestesider viser operativ drift, men ikke full ansvarsmodell. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Prisinformasjon er delvis beskrevet gjennom SvarUt/SvarInn-sammenheng, men ikke full finansieringsmodell. |
| Styringsmodell | KS Digital som sentral forvalter av tjenesten | Fremgår av tjenestesider, oppsett og avtalevilkår. |

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



