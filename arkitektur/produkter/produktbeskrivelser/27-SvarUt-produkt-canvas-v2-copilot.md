# Produkt-canvas: SvarUt

## Navn
SvarUt

## Ressurs ID
KS-003

## Status/Livsfase
**Produksjon** - etablert utsendingstjeneste i KS Digital med aktiv driftsoppfølging i FIKS-status.

**Fakta:** Tjenesten beskrives som sentralisert formidling av dokumenter mellom avsender og mottaker via flere kanaler. Driftsstatus viser SvarUt som operativ tjeneste.

## Modenhet
**Høy funksjonell modenhet** - tjenesten har tydelig produktavgrensning, kjent integrasjonsmønster og operativ bruk i kommunal/offentlig sektor.

- Produktet har klart skille mellom utgående post (SvarUt) og inngående post (SvarInn).
- Dokumentasjonen viser både webportal og maskin-til-maskin API-er, som gir modenhet for ulike innføringsmodeller.
- Driftsstatus og historikk viser at tjenesten forvaltes som en løpende kritisk komponent i FIKS-porteføljen.

**Deduksjon:** Modenheten er høy for standardisert utsending, men gevinsten avhenger fortsatt av lokal konfigurasjon i fagsystem og rutiner for kanalvalg.

## Kort beskrivelse
SvarUt er KS Digitals sentraliserte løsning for å sende dokumenter fra offentlige virksomheter til riktig mottakerkanal. Tjenesten gjør det mulig å formidle utgående post videre til blant annet Altinn, SvarInn, Digipost, e-Boks eller fysisk brev, uten at avsender må bygge separate distribusjonsløp mot hver kanal. Produktet er særlig relevant når virksomheten trenger kontrollert dokumentutsending til mange mottakergrupper gjennom én felles distribusjonsmekanisme.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling**
  SvarUt sin kjernefunksjon er å motta, rute og levere dokumentforsendelser til riktig kanal og mottaker.
- **Samarbeid: Organisatorisk samhandling**
  Løsningen muliggjør samordnet dokumentflyt mellom kommuner og andre offentlige virksomheter gjennom et felles tjenesteløp.
- **Sluttbrukertjenester: Sammenhengende tjenester**
  SvarUt bidrar til sammenheng i mottakeropplevelsen ved at samme forsendelse kan nå fram via riktig kanal uten at avsender bygger ulike løsninger.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot produktets dokumenterte funksjon i kildene nedenfor.

## Produktmål
Dokumenterte mål:
- Formidle dokumenter mellom avsender og mottaker via ulike kanaler.
- Gjøre SvarUt tilgjengelig for kommuner og andre offentlige virksomheter.
- Håndtere utgående post gjennom et sentralisert tjenesteløp.

Operative mål utledet fra kildene:
- Redusere lokal kompleksitet ved kanalspesifikke integrasjoner.
- Gi virksomheter et mer forutsigbart utsendingsløp for digital og fysisk post.
- Understøtte sikker og sporbar dokumentformidling i samspill med FIKS-plattformen.

## Brukerbehov
- Offentlige virksomheter trenger én tjeneste for dokumentutsending til flere kanaler.
- Fagsystemleverandører trenger stabile API-er for automatisert utsending.
- Virksomheter trenger kanalvalg som dekker både innbyggere og virksomheter.
- Drift- og forvaltningsmiljøer trenger tydelig statusbilde for hendelser og vedlikehold.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og andre offentlige virksomheter | Enhetlig utsending av dokumenter | Utgående post fra sak-/arkivsystem og fagsystem | Primærbrukere |
| Systemleverandører og integrasjonsmiljøer | API-basert maskinell utsending | Integrasjon mot SvarUt REST og tilhørende funksjoner | Teknisk brukergruppe |
| Innbyggere og virksomheter som mottakere | Mottak i riktig kanal | Digital post til innbygger, Altinn, SvarInn eller print | Opplever resultatet av tjenesten |
| KS Digital forvaltning og drift | Stabil drift og videreutvikling | Tjenesteforvaltning, statusoppfølging, konfigurasjon | Sentral produkteier/forvalter |

## Hovedfunksjoner
### Primære funksjoner
- SvarUt tar imot utgående dokumenter fra avsender og sender dem videre til riktig mottakerkanal. Det gjør løsningen relevant når dokumentdistribusjon er viktigere enn bred dialogfunksjonalitet.
- Tjenesten kan formidle dokumenter til flere etablerte kanaler i offentlig sektor, blant annet Altinn, SvarInn, Digipost og e-Boks, eller videre til fysisk brev. Kanalflyten er beskrevet med prioritert rekkefølge for privatpersoner og virksomheter.
- SvarUt er sentralisert. Det er et viktig skille fra lokale utsendingsrutiner, fordi produktet samler distribusjonslogikken i én fellestjeneste.
- Utviklerdokumentasjonen viser et eksplisitt API- og integrasjonsmønster for hvordan forsendelser opprettes, overføres og kvitteres. I tillegg inngår tjenesten i løp som inkluderer eDialog og signeringsoppdrag.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Utgående dokumentformidling via sentral tjeneste | Mottak av inngående post (dekkes av SvarInn) |
| API- og portalbasert innsending av forsendelser | Lokal produksjon av dokumentinnhold |
| Ruting til flere mottakerkanaler inkl. print | Saksbehandling og arbeidsflyt i fagsystem |
| Tjenesteoppsett/konfigurasjon etter avtale med KS Digital | Full kommunikasjonsplattform for alle meldingstyper |

## Veikart over kommende funksjonalitet
**Fakta:** Produktsidene viser at løsningen er i aktiv bruk og i løpende videreutvikling. Det er omtalt planlagt utprøving av forsendelsesløp mot fastlegenes journalsystem (EPJ) i Q1-Q2 2026.

**Usikkert:** Det finnes ikke et samlet, offentlig tidslinjebasert veikart for hele SvarUt-tjenesten i kildene brukt i denne økten.

## Forretningsverdi/Verdiforslag
### For virksomheter
- Lavere integrasjonskost ved ett felles utsendingsgrensesnitt.
- Mer robust utsending gjennom sentral kanalhåndtering.

### For mottakere
- Større sannsynlighet for at dokumenter leveres i kanal som allerede brukes.
- Mer konsistent mottaksopplevelse på tvers av offentlige avsendere.

### For sektoren
- Standardiserer utsendingsmønster på tvers av kommunal og offentlig sektor.
- Støtter gjenbruk av felles infrastruktur framfor parallelle lokale løsninger.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil adressat eller kanalvalg kan gi brudd på taushetsplikt/personvern. | Tydelige valideringsrutiner i avsendersystem, kvalitetssikret adressedata og kanalpolicy. |
| Teknisk | Feil i kanalavhengigheter eller lokale integrasjoner kan gi forsinket levering. | Overvåking, retry-håndtering og tydelige driftsprosedyrer mellom leverandør og virksomhet. |
| Sikkerhet | Forsendelser kan inneholde sensitiv informasjon. | Sikkerhetsmekanismer i tjenesten, kontroll med nøkler/sertifikater der relevant og intern klassifisering hos avsender. |
| Leverandør | Høy avhengighet til sentral tjeneste og tilhørende økosystem. | Tydelige avtaler, dokumenterte API-versjoner, testmiljø og vedlikeholdsvarsling. |
| Brukeropplevelse | Uklart kanalutfall eller forsinket levering kan skape usikkerhet hos mottaker. | Bedre sporbarhet i avsendersystem, tydelig kommunikasjon ved avvik og oppfølging av statusmeldinger. |

## Kanaler
- https://ksdigital.no/tjenestene/svarut-tjenesten/
- https://developers.fiks.ks.no/tjenester/svarut/
- https://status.fiks.ks.no/

## Plattform
SvarUt er en sentralt forvaltet utsendingstjeneste som inngår i KS Digitals tjenesteportefølje.

**Fakta:**
- Driftsstatus rapporteres i offentlig statusside for FIKS.
- Utviklerdokumentasjon beskriver tekniske grensesnitt, konfigurasjon og nettverkskrav.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full intern driftsarkitektur, skyplassering og detaljert teknologistakk.

## Gjenbruk
**Høy gjenbruksverdi**
- Gjenbruket ligger i standardisert utsending, API-er og felles kanalmodell.
- Løsningen er spesielt relevant for virksomheter med behov for stor eller regelmessig dokumentdistribusjon.
- Gjenbruket gjelder infrastruktur og samhandlingsmønster, ikke lokal forretningslogikk i fagsystemene.

## Støtter arkitekturprinsipper
- **P6: Lag digitale løsninger som støtter samhandling**
  SvarUt gjør dokumentutsending på tvers av kanaler og aktører enklere og mer standardisert.
- **P1: Ta utgangspunkt i brukernes behov**
  Mottakeren kan nås gjennom kanaler som allerede brukes i offentlig sektor, uten at avsender må bygge ulike lokale spesialløsninger.

## Finansiering
**Fakta:** Prisoversikten for 2026 viser at SvarUt har publiserte priser per kanal og forsendelsestype. Kildene beskriver også at kostnadsbildet skiller mellom år 1 (inkludert prosjektavgift til Digifin) og fra år 2, samt at deler av kostnadene ligger hos systemleverandør.

**Usikkert:** Full finansieringsmodell for sentral forvaltning og intern budsjettfordeling er ikke offentlig detaljert i kildene brukt i denne økten.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsider, dokumentasjon og avtalespor peker på KS Digital som tjenesteforvalter. |
| Driftsansvar | KS Digital med driftsoppfølging i FIKS statusmiljø | Offentlig statusside viser operativ tjeneste og planlagt vedlikehold. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert | Prisoversikt finnes, men ikke full intern budsjett- og styringsmodell. |
| Styringsmodell | Sentral forvaltning i KS Digital-porteføljen | Framgår av tjenesteplassering, avtalespor og driftskommunikasjon. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/svarut-tjenesten/
- https://developers.fiks.ks.no/tjenester/svarut/
- https://developers.fiks.ks.no/tjenester/svarut/rest/
- https://developers.fiks.ks.no/tjenester/svarut/api-versjoner/
- https://ksdigital.no/avtaler-og-priser/prisoversikt-2026/
- https://status.fiks.ks.no/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/produkter/produktbeskrivelser/27-SvarUt-produkt-canvas-v1-codex.md`
- Nettkilde: https://ksdigital.no/tjenestene/svarut-tjenesten/ (hentet 2026-03-22)
- Nettkilde: https://developers.fiks.ks.no/tjenester/svarut/ (hentet 2026-03-22)
- Nettkilde: https://developers.fiks.ks.no/tjenester/svarut/rest/ (hentet 2026-03-22)
- Nettkilde: https://developers.fiks.ks.no/tjenester/svarut/api-versjoner/ (hentet 2026-03-22)
- Nettkilde: https://ksdigital.no/avtaler-og-priser/prisoversikt-2026/ (hentet 2026-03-22)
- Nettkilde: https://status.fiks.ks.no/ (hentet 2026-03-22)

## Endringer fra forrige versjon
### Analyseforbedringer
- Oppdatert kildegrunnlag med nye kontroller av produktside, utviklerdokumentasjon, prisoversikt og driftsstatus i dagens arbeidsøkt.
- Presisert kanalrekkefølge for privatpersoner og virksomheter, samt tydeliggjort API- og grensesnittperspektivet.
- Oppdatert statusvurdering med observasjoner fra operativ statusside og vedlikeholdsvarsler.

### Tekstlige forbedringer
- Strammet inn avgrensning mot SvarInn og lokal saksbehandling.
- Tydeligere segmentering av brukergrupper og behov.
- Mer presise formuleringer i risiko-, finansierings- og forvaltningsseksjonene.
