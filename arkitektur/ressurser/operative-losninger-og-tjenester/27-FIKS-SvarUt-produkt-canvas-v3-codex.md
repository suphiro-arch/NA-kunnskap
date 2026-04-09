# Produkt-canvas: Fiks SvarUt

## Navn
Fiks SvarUt

## Ressurs ID
KS-003

## Status/Livsfase
**Produksjon** - etablert utsendingstjeneste i KS Digital med offentlig driftsstatus og aktiv teknisk videreutvikling.

**Fakta:** KS Digital presenterer SvarUt som operativ tjeneste for kommuner og andre offentlige virksomheter. Offentlig statusside viser bÃ¥de `Fiks SvarUt`, `SvarUt` og `SvarUt signering` som operative tjenester.

## Modenhet
**HÃ¸y funksjonell modenhet** - tjenesten er i drift, har tydelig funksjonsavgrensning, publisert utviklerdokumentasjon og et versjonert API-landskap.

- Tjenesten har et klart skille mellom utgÃ¥ende post i Fiks SvarUt og innkommende post i SvarInn.
- Utviklerdokumentasjonen viser bÃ¥de webportal og maskin-til-maskin-grensesnitt.
- API-versjonsoversikten viser at REST-grensesnittene er i aktiv forvaltning, med stabile V2- og V3-endepunkter og planlagt avvikling av REST felles V1 31.12.2026.

**Deduksjon:** Modenheten er hÃ¸y for standardisert utsending og kanalhÃ¥ndtering. Samtidig er produktet avhengig av korrekt integrasjon og konfigurasjon i avsendersystemene for Ã¥ gi full verdi.

## Kort beskrivelse
Fiks SvarUt er KS Digitals sentraliserte utsendingstjeneste for utgÃ¥ende dokumentformidling. Tjenesten gjÃ¸r det mulig for kommuner og andre offentlige virksomheter Ã¥ sende dokumenter gjennom Ã©n felles distribusjonsmekanisme, i stedet for Ã¥ bygge separate lÃ¸p mot hver mottakerkanal. Fiks SvarUt kan brukes bÃ¥de gjennom integrasjon fra sak-/arkivsystemer og andre fagsystemer, og gjennom portalbaserte og manuelle arbeidsmÃ¥ter. Tjenesten hÃ¥ndterer utgÃ¥ende post og formidler den videre til blant annet digital post til innbygger, Altinn, SvarInn eller print, avhengig av mottakertype og kanaltilgjengelighet.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling**
  Fiks SvarUt sin kjernefunksjon er Ã¥ motta, rute og levere dokumentforsendelser til riktig kanal og mottaker.
- **Samarbeid: Organisatorisk samhandling**
  LÃ¸sningen muliggjÃ¸r et felles utsendingslÃ¸p mellom kommuner, andre offentlige virksomheter og sentrale mottakerkanaler.
- **Sluttbrukertjenester: Sammenhengende tjenester**
  Fiks SvarUt bidrar til en mer sammenhengende mottakeropplevelse ved at samme forsendelse kan nÃ¥ fram gjennom riktig kanal uten at avsender bygger ulike lÃ¸sninger per kanal.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals produkt- og utviklerdokumentasjon kontrollert 2026-03-25.

## ProduktmÃ¥l
Dokumenterte mÃ¥l:
- Formidle dokumenter mellom avsender og mottaker via flere kanaler.
- GjÃ¸re tjenesten tilgjengelig for kommuner og andre offentlige virksomheter.
- HÃ¥ndtere utgÃ¥ende post gjennom et sentralisert og standardisert tjenestelÃ¸p.

Operative mÃ¥l utledet fra kildene:
- Redusere behovet for kanalspesifikke integrasjoner i hver virksomhet.
- Gi et mer forutsigbart utsendingslÃ¸p for bÃ¥de digital og fysisk post.
- UnderstÃ¸tte sikker, sporbar og gjenbrukbar dokumentformidling i Fiks-Ã¸kosystemet.

## Brukerbehov
- Offentlige virksomheter trenger Ã©n tjeneste for utsending til flere mottakerkanaler.
- FagsystemleverandÃ¸rer trenger stabile og dokumenterte API-er for automatisert utsending.
- Noen virksomheter trenger ogsÃ¥ Ã¥ kunne sende manuelt eller halvmanuelt uten full systemintegrasjon.
- Virksomheter trenger Ã¥ kunne sende til bÃ¥de privatpersoner, virksomheter og i enkelte tilfeller mottakere i Norsk Helsenett.
- Drift- og forvaltningsmiljÃ¸er trenger tydelig statusinformasjon og versjonsstyrt integrasjonsgrunnlag.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Kommuner, fylkeskommuner og andre offentlige virksomheter | Enhetlig og kontrollerbar utsending av dokumenter | UtgÃ¥ende post fra sak-/arkivsystemer, andre fagsystemer og manuelle arbeidsflater | PrimÃ¦rbrukere |
| SystemleverandÃ¸rer og integrasjonsmiljÃ¸er | Dokumenterte API-er, autentisering og versjonsstyring | Integrasjon mot send-, status- og hendelsesgrensesnitt | Teknisk brukergruppe |
| Innbyggere og virksomheter som mottakere | Mottak i egnet kanal | Digital post, Altinn, SvarInn eller print | Opplever resultatet av tjenesten, ikke nÃ¸dvendigvis tjenesten direkte |
| KS Digital forvaltning og drift | Stabil drift, versjonsforvaltning og kanaloppfÃ¸lging | Tjenesteforvaltning, statusoppfÃ¸lging og videreutvikling | Sentral produkteier og forvalter |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
Fiks SvarUt sin kjernefunksjon er Ã¥ motta utgÃ¥ende dokumenter og styre dem videre til riktig kanal og mottaker. For virksomheten betyr dette at utsendingen kan samles i Ã©n fellestjeneste i stedet for Ã¥ hÃ¥ndteres som flere separate integrasjoner og rutiner. Produktet er derfor fÃ¸rst og fremst en utsendingstjeneste med sentral kanalhÃ¥ndtering, ikke en dialogplattform eller et saksbehandlingssystem.

Tjenesten stÃ¸tter bÃ¥de integrert og mer manuell bruk. Dokumentasjonen viser at forsendelser kan sendes fra sak-/arkivsystemer og andre fagsystemer gjennom maskin-til-maskin-grensesnitt, men KS beskriver ogsÃ¥ webportal og manuelle lÃ¸p som del av tjenesten. Dette er viktig for Ã¥ forstÃ¥ produktet riktig: Fiks SvarUt er ikke bare et API, men en felles tjeneste som kan brukes gjennom flere arbeidsmÃ¥ter avhengig av modenhet og behov hos virksomheten.

En sentral del av funksjonaliteten er kanalstyring og ruting. For privatpersoner beskrives prioritert kanalrekkefÃ¸lge som digital post til innbygger, deretter Altinn og til slutt print. For virksomheter beskrives prioritert kanalrekkefÃ¸lge som SvarInn, deretter Altinn og til slutt print. Denne kanalstyringen er en vesentlig del av verdien i lÃ¸sningen, fordi avsender slipper Ã¥ bygge og vedlikeholde egen logikk for hver kanal og mottakertype.

Tjenesten har ogsÃ¥ et mer detaljert teknisk funksjonssett enn det som kommer fram av den overordnede produktsiden alene. Utviklerdokumentasjonen viser egne REST-grensesnitt for blant annet sending, status, hendelser, metadata og mottakersystem. Det betyr at virksomheter og leverandÃ¸rer ikke bare kan sende dokumenter, men ogsÃ¥ fÃ¸lge opp leveranse, hendelser og teknisk status i et mer finmasket integrasjonslÃ¸p. Dokumentasjonen viser i tillegg egne lÃ¸p for sending til privatpersoner, virksomheter og mottakere i Norsk Helsenett, samt koblinger til relaterte funksjoner som eDialog og signeringslÃ¸p.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| UtgÃ¥ende dokumentformidling via sentral tjeneste | Mottak av inngÃ¥ende post, som dekkes av SvarInn |
| API-basert og portalbasert innsending, statusoppfÃ¸lging og hendelseshÃ¥ndtering | Lokal produksjon av dokumentinnhold |
| Ruting til flere mottakerkanaler, inkludert print | Saksbehandling og arbeidsflyt i fagsystemene |
| Standardisert kanalhÃ¥ndtering og integrasjonsmÃ¸nster | Full dialogplattform for alle meldingstyper |

## Veikart over kommende funksjonalitet
**Fakta:** KS Digital omtaler planlagt utprÃ¸ving av forsendelseslÃ¸p mot fastlegenes pasientjournalsystemer i Q1-Q2 2026, med barnevernstjenestene som anbefalt fÃ¸rste omrÃ¥de for utprÃ¸ving. API-versjonsoversikten viser ogsÃ¥ pÃ¥gÃ¥ende modernisering gjennom stabile nyere REST-endepunkter og planlagt avvikling av REST felles V1 31.12.2026.

**Deduksjon:** Det offentlige veikartet peker fÃ¸rst og fremst mot videre modernisering av grensesnitt og utvidelse av bruksomrÃ¥der, ikke mot en ny produktrolle eller stÃ¸rre endring i kjernetjenesten.

## Forretningsverdi/Verdiforslag
### For virksomheter
- Lavere integrasjonskostnad ved ett felles utsendingsgrensesnitt.
- Mulighet for bÃ¥de integrert og mer manuell bruk av samme tjeneste.
- Mer forutsigbar kanalhÃ¥ndtering enn ved separate integrasjoner mot hver kanal.

### For mottakere
- HÃ¸yere sannsynlighet for at dokumenter kommer fram i en kanal som allerede er i bruk.
- Mindre behov for at avsender tilpasser prosessen manuelt per mottakergruppe.

### For sektoren
- Standardiserer utsendingsmÃ¸nsteret pÃ¥ tvers av kommunal sektor og andre offentlige aktÃ¸rer.
- StÃ¸tter gjenbruk av felles infrastruktur framfor parallelle lokale utsendingslÃ¸sninger.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Feil mottaker eller feil kanalvalg kan gi brudd pÃ¥ taushetsplikt eller personvern. | Validering i avsendersystem, god kvalitet i mottakerdata og tydelige regler for hvilke dokumenttyper som kan sendes i hvilke kanaler. |
| Teknisk | Feil i integrasjon, versjonsbruk eller lokale oppsett kan gi forsinkelser eller avviste forsendelser. | Bruke oppdatert API-versjon, testmiljÃ¸, versjonsstyrt innfÃ¸ring og tydelig feil- og hendelseshÃ¥ndtering. |
| Sikkerhet | Tjenesten hÃ¥ndterer dokumenter som kan inneholde sensitiv informasjon. | Sterk autentisering via Fiks-integrasjoner og Maskinporten, tilgangsstyring og sikker hÃ¥ndtering hos bÃ¥de KS Digital og avsender. |
| LeverandÃ¸r | Virksomheten blir avhengig av sentral tjeneste og tilhÃ¸rende integrasjonsmÃ¸nster. | Dokumenterte API-er, offentlig statusinformasjon, vedlikeholdsvarsling og tydelige avtalevilkÃ¥r. |
| Brukeropplevelse | Manglende sporbarhet eller uklart kanalutfall kan skape usikkerhet hos bÃ¥de avsender og mottaker. | Tydelig statusoppfÃ¸lging i integrasjonene, bedre logging og god informasjon ved avvik. |

## Kanaler
- https://ksdigital.no/tjenestene/svarut-tjenesten/
- https://developers.fiks.ks.no/tjenester/svarut/
- https://developers.fiks.ks.no/tjenester/svarut/rest/
- https://developers.fiks.ks.no/tjenester/svarut/api-versjoner/
- https://ksdigital.no/avtaler-og-priser/prisoversikt-2026/
- https://status.fiks.ks.no/

## Plattform
Fiks SvarUt er en sentralt forvaltet utsendingstjeneste i Fiks-Ã¸kosystemet.

**Fakta:**
- Autentisering og autorisering i REST-grensesnittene skjer med OAuth 2.0, Fiks-integrasjoner og Maskinporten.
- API-landskapet er versjonert, og nyere REST-endepunkter er etablert som stabile grensesnitt.
- Offentlig statusside viser tjenesten som en egen operativ komponent i Fiks-plattformen.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full intern driftsarkitektur, skyplassering og detaljert teknologistakk.

## Gjenbruk
**HÃ¸y gjenbruksverdi**
- Gjenbruksverdien ligger i standardisert utsending, kanalhÃ¥ndtering og felles grensesnitt for bÃ¥de integrert og portalbasert bruk.
- Produktet er sÃ¦rlig relevant for virksomheter som sender mange dokumenter eller trenger et robust felles utsendingslÃ¸p.
- Gjenbruket gjelder infrastrukturen og samhandlingsmÃ¸nsteret, ikke lokal forretningslogikk i hvert fagsystem.

## StÃ¸tter arkitekturprinsipper
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling**
  Fiks SvarUt gjÃ¸r dokumentutsending pÃ¥ tvers av kanaler og aktÃ¸rer enklere og mer standardisert.
- **P1: Ta utgangspunkt i brukernes behov**
  Tjenesten legger til rette for at mottakeren kan nÃ¥s gjennom egnet kanal uten at avsender mÃ¥ bygge flere parallelle spesiallÃ¸sninger.

## Finansiering
**Fakta:** Prisoversikten for 2026 viser publiserte priser for Fiks SvarUt og Fiks SvarInn, med forskjell mellom kommunal/fylkeskommunal og statlig/privat bruk. For kommuner, fylkeskommuner og (inter)kommunale selskap er fastpris oppgitt til 262,5 kroner per mÃ¥ned, mens kanalpriser beregnes per forsendelse.

**Ikke offentlig detaljert dokumentert:** Full modell for intern finansiering av sentral forvaltning og drift.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktside, utviklerdokumentasjon og prisoversikt peker pÃ¥ KS Digital som tjenesteforvalter. |
| Driftsansvar | KS Digital med offentlig driftsrapportering i Fiks status | Offentlig statusside viser operativ tjeneste og historisk oppetid. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert | Prisoversikt finnes, men ikke full intern budsjettmodell. |
| Styringsmodell | Sentral tjenesteforvaltning i KS Digital-portefÃ¸ljen | FramgÃ¥r av tjenesteplassering, dokumentasjon og driftskommunikasjon. |

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
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/27-SvarUt-produkt-canvas-v2-copilot.md`
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
- Tydeliggjort mottakertyper og kanalrekkefÃ¸lge for privatpersoner og virksomheter.
- Presisert at produktet er en bredere utsendingstjeneste og ikke bare en API-tjeneste, siden KS ogsÃ¥ beskriver webportal og manuelle lÃ¸p.

### Tekstlige forbedringer
- Strammet inn navnebruk til `Fiks SvarUt` som operativt navn i repoet.
- Redusert spekulative formuleringer og gjort scope, plattform og risiko mer presise.
- Forbedret sammenhengen mellom funksjonsbeskrivelse, tekniske grensesnitt og verdiforslag.

