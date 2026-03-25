# Produkt-canvas: Fiks SvarUt

## Navn
Fiks SvarUt

## Ressurs ID
KS-003

## Status/Livsfase
**Produksjon** - etablert utsendingstjeneste i KS Digital med offentlig driftsstatus og aktiv teknisk videreutvikling.

**Fakta:** KS Digital presenterer SvarUt som operativ tjeneste for kommuner og andre offentlige virksomheter. Offentlig statusside viser både `Fiks SvarUt`, `SvarUt` og `SvarUt signering` som operative tjenester.

## Modenhet
**Høy funksjonell modenhet** - tjenesten er i drift, har tydelig funksjonsavgrensning, publisert utviklerdokumentasjon og et versjonert API-landskap.

- Tjenesten har et klart skille mellom utgående post i Fiks SvarUt og innkommende post i SvarInn.
- Utviklerdokumentasjonen viser både webportal og maskin-til-maskin-grensesnitt.
- API-versjonsoversikten viser at REST-grensesnittene er i aktiv forvaltning, med stabile V2- og V3-endepunkter og planlagt avvikling av REST felles V1 31.12.2026.

**Deduksjon:** Modenheten er høy for standardisert utsending og kanalhåndtering. Samtidig er produktet avhengig av korrekt integrasjon og konfigurasjon i avsendersystemene for å gi full verdi.

## Kort beskrivelse
Fiks SvarUt er KS Digitals API-baserte tjeneste for utgående dokumentformidling. Tjenesten gjør det mulig for kommuner og andre offentlige virksomheter å sende dokumenter fra sak-/arkivsystemer og andre fagsystemer gjennom én sentral distribusjonsmekanisme, i stedet for å bygge separate løp mot hver mottakerkanal. Fiks SvarUt håndterer utgående post og formidler den videre til blant annet digital post til innbygger, Altinn, SvarInn eller print, avhengig av mottakertype og kanaltilgjengelighet.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling**
  Fiks SvarUt sin kjernefunksjon er å motta, rute og levere dokumentforsendelser til riktig kanal og mottaker.
- **Samarbeid: Organisatorisk samhandling**
  Løsningen muliggjør et felles utsendingsløp mellom kommuner, andre offentlige virksomheter og sentrale mottakerkanaler.
- **Sluttbrukertjenester: Sammenhengende tjenester**
  Fiks SvarUt bidrar til en mer sammenhengende mottakeropplevelse ved at samme forsendelse kan nå fram gjennom riktig kanal uten at avsender bygger ulike løsninger per kanal.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals produkt- og utviklerdokumentasjon kontrollert 2026-03-25.

## Produktmål
Dokumenterte mål:
- Formidle dokumenter mellom avsender og mottaker via flere kanaler.
- Gjøre tjenesten tilgjengelig for kommuner og andre offentlige virksomheter.
- Håndtere utgående post gjennom et sentralisert og standardisert tjenesteløp.

Operative mål utledet fra kildene:
- Redusere behovet for kanalspesifikke integrasjoner i hver virksomhet.
- Gi et mer forutsigbart utsendingsløp for både digital og fysisk post.
- Understøtte sikker, sporbar og gjenbrukbar dokumentformidling i Fiks-økosystemet.

## Brukerbehov
- Offentlige virksomheter trenger én tjeneste for utsending til flere mottakerkanaler.
- Fagsystemleverandører trenger stabile og dokumenterte API-er for automatisert utsending.
- Virksomheter trenger å kunne sende til både privatpersoner, virksomheter og i enkelte tilfeller mottakere i Norsk Helsenett.
- Drift- og forvaltningsmiljøer trenger tydelig statusinformasjon og versjonsstyrt integrasjonsgrunnlag.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner, fylkeskommuner og andre offentlige virksomheter | Enhetlig og kontrollerbar utsending av dokumenter | Utgående post fra sak-/arkivsystemer og andre fagsystemer | Primærbrukere |
| Systemleverandører og integrasjonsmiljøer | Dokumenterte API-er, autentisering og versjonsstyring | Integrasjon mot send-, status- og hendelsesgrensesnitt | Teknisk brukergruppe |
| Innbyggere og virksomheter som mottakere | Mottak i egnet kanal | Digital post, Altinn, SvarInn eller print | Opplever resultatet av tjenesten, ikke nødvendigvis tjenesten direkte |
| KS Digital forvaltning og drift | Stabil drift, versjonsforvaltning og kanaloppfølging | Tjenesteforvaltning, statusoppfølging og videreutvikling | Sentral produkteier og forvalter |

## Hovedfunksjoner
### Primære funksjoner
- Fiks SvarUt tar imot utgående dokumenter fra avsendersystemer og fordeler dem videre til riktig mottakerkanal. Dette gjør produktet relevant når behovet er standardisert utsending, ikke full dialog- eller saksbehandlingsstøtte.
- Tjenesten håndterer kanalvalg forskjellig for privatpersoner og virksomheter. For privatpersoner brukes prioritert rekkefølge digital post til innbygger, Altinn og print. For virksomheter brukes prioritert rekkefølge SvarInn, Altinn og print.
- REST-grensesnittene er delt opp i egne funksjonsområder for blant annet sending, status, hendelser, metadata og mottakersystem. Dette gjør det mulig å integrere og følge opp forsendelser mer presist enn i en eldre monolittisk API-modell.
- Tjenesten støtter ulike mottakertyper. Dokumentasjonen viser egne løp for sending til privatperson, virksomhet og mottaker i Norsk Helsenett.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Utgående dokumentformidling via sentral tjeneste | Mottak av inngående post, som dekkes av SvarInn |
| API-basert innsending, statusoppfølging og hendelseshåndtering | Lokal produksjon av dokumentinnhold |
| Ruting til flere mottakerkanaler, inkludert print | Saksbehandling og arbeidsflyt i fagsystemene |
| Standardisert kanalhåndtering og integrasjonsmønster | Full dialogplattform for alle meldingstyper |

## Veikart over kommende funksjonalitet
**Fakta:** KS Digital omtaler planlagt utprøving av forsendelsesløp mot fastlegenes pasientjournalsystemer i Q1-Q2 2026, med barnevernstjenestene som anbefalt første område for utprøving. API-versjonsoversikten viser også pågående modernisering gjennom stabile nyere REST-endepunkter og planlagt avvikling av REST felles V1 31.12.2026.

**Deduksjon:** Det offentlige veikartet peker først og fremst mot videre modernisering av grensesnitt og utvidelse av bruksområder, ikke mot en ny produktrolle eller større endring i kjernetjenesten.

## Forretningsverdi/Verdiforslag
### For virksomheter
- Lavere integrasjonskostnad ved ett felles utsendingsgrensesnitt.
- Mer forutsigbar kanalhåndtering enn ved separate integrasjoner mot hver kanal.

### For mottakere
- Høyere sannsynlighet for at dokumenter kommer fram i en kanal som allerede er i bruk.
- Mindre behov for at avsender tilpasser prosessen manuelt per mottakergruppe.

### For sektoren
- Standardiserer utsendingsmønsteret på tvers av kommunal sektor og andre offentlige aktører.
- Støtter gjenbruk av felles infrastruktur framfor parallelle lokale utsendingsløsninger.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil mottaker eller feil kanalvalg kan gi brudd på taushetsplikt eller personvern. | Validering i avsendersystem, god kvalitet i mottakerdata og tydelige regler for hvilke dokumenttyper som kan sendes i hvilke kanaler. |
| Teknisk | Feil i integrasjon, versjonsbruk eller lokale oppsett kan gi forsinkelser eller avviste forsendelser. | Bruke oppdatert API-versjon, testmiljø, versjonsstyrt innføring og tydelig feil- og hendelseshåndtering. |
| Sikkerhet | Tjenesten håndterer dokumenter som kan inneholde sensitiv informasjon. | Sterk autentisering via Fiks-integrasjoner og Maskinporten, tilgangsstyring og sikker håndtering hos både KS Digital og avsender. |
| Leverandør | Virksomheten blir avhengig av sentral tjeneste og tilhørende integrasjonsmønster. | Dokumenterte API-er, offentlig statusinformasjon, vedlikeholdsvarsling og tydelige avtalevilkår. |
| Brukeropplevelse | Manglende sporbarhet eller uklart kanalutfall kan skape usikkerhet hos både avsender og mottaker. | Tydelig statusoppfølging i integrasjonene, bedre logging og god informasjon ved avvik. |

## Kanaler
- https://ksdigital.no/tjenestene/svarut-tjenesten/
- https://developers.fiks.ks.no/tjenester/svarut/
- https://developers.fiks.ks.no/tjenester/svarut/rest/
- https://developers.fiks.ks.no/tjenester/svarut/api-versjoner/
- https://ksdigital.no/avtaler-og-priser/prisoversikt-2026/
- https://status.fiks.ks.no/

## Plattform
Fiks SvarUt er en sentralt forvaltet utsendingstjeneste i Fiks-økosystemet.

**Fakta:**
- Autentisering og autorisering i REST-grensesnittene skjer med OAuth 2.0, Fiks-integrasjoner og Maskinporten.
- API-landskapet er versjonert, og nyere REST-endepunkter er etablert som stabile grensesnitt.
- Offentlig statusside viser tjenesten som en egen operativ komponent i Fiks-plattformen.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full intern driftsarkitektur, skyplassering og detaljert teknologistakk.

## Gjenbruk
**Høy gjenbruksverdi**
- Gjenbruksverdien ligger i standardisert utsending, kanalhåndtering og felles API-er.
- Produktet er særlig relevant for virksomheter som sender mange dokumenter eller trenger et robust felles utsendingsløp.
- Gjenbruket gjelder infrastrukturen og samhandlingsmønsteret, ikke lokal forretningslogikk i hvert fagsystem.

## Støtter arkitekturprinsipper
- **P6: Lag digitale løsninger som støtter samhandling**
  Fiks SvarUt gjør dokumentutsending på tvers av kanaler og aktører enklere og mer standardisert.
- **P1: Ta utgangspunkt i brukernes behov**
  Tjenesten legger til rette for at mottakeren kan nås gjennom egnet kanal uten at avsender må bygge flere parallelle spesialløsninger.

## Finansiering
**Fakta:** Prisoversikten for 2026 viser publiserte priser for Fiks SvarUt og Fiks SvarInn, med forskjell mellom kommunal/fylkeskommunal og statlig/privat bruk. For kommuner, fylkeskommuner og (inter)kommunale selskap er fastpris oppgitt til 262,5 kroner per måned, mens kanalpriser beregnes per forsendelse.

**Ikke offentlig detaljert dokumentert:** Full modell for intern finansiering av sentral forvaltning og drift.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktside, utviklerdokumentasjon og prisoversikt peker på KS Digital som tjenesteforvalter. |
| Driftsansvar | KS Digital med offentlig driftsrapportering i Fiks status | Offentlig statusside viser operativ tjeneste og historisk oppetid. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert | Prisoversikt finnes, men ikke full intern budsjettmodell. |
| Styringsmodell | Sentral tjenesteforvaltning i KS Digital-porteføljen | Framgår av tjenesteplassering, dokumentasjon og driftskommunikasjon. |

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
- Lokal fil: `arkitektur/produkter/produktbeskrivelser/27-SvarUt-produkt-canvas-v2-copilot.md`
- Nettkilde: https://ksdigital.no/tjenestene/svarut-tjenesten/ (hentet 2026-03-25)
- Nettkilde: https://developers.fiks.ks.no/tjenester/svarut/ (hentet 2026-03-25)
- Nettkilde: https://developers.fiks.ks.no/tjenester/svarut/rest/ (hentet 2026-03-25)
- Nettkilde: https://developers.fiks.ks.no/tjenester/svarut/api-versjoner/ (hentet 2026-03-25)
- Nettkilde: https://ksdigital.no/avtaler-og-priser/prisoversikt-2026/ (hentet 2026-03-25)
- Nettkilde: https://status.fiks.ks.no/ (hentet 2026-03-25)

## Endringer fra forrige versjon
### Analyseforbedringer
- Oppdatert kildegrunnlag med ny kontroll av produktside, utviklerdokumentasjon, API-versjonsoversikt, prisoversikt og driftsstatus 2026-03-25.
- Presisert at REST felles V1 er planlagt avviklet 31.12.2026, og at nyere REST-endepunkter er stabile.
- Tydeliggjort mottakertyper og kanalrekkefølge for privatpersoner og virksomheter.

### Tekstlige forbedringer
- Strammet inn navnebruk til `Fiks SvarUt` som operativt navn i repoet.
- Redusert spekulative formuleringer og gjort scope, plattform og risiko mer presise.
- Forbedret sammenhengen mellom funksjonsbeskrivelse, tekniske grensesnitt og verdiforslag.
