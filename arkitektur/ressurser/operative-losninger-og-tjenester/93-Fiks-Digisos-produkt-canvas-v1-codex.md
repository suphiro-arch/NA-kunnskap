# Produkt-canvas: Fiks digisos

## Navn
Fiks digisos

## Ressurs ID
KS-012

## Status/Livsfase
**Produksjon** - etablert tjeneste i drift i kommunesektoren, med høy utbredelse i Norge.

**Fakta:** KS Digital beskriver Fiks Digisos som en tjeneste for kommunal behandling av sosialsøknader via nav.no. NAV beskriver Digisos som et samarbeid mellom KS Digital, kommunene og Arbeids- og velferdsdirektoratet, med løsninger for digital søknad, innsyn for søker og innsynsflate for NAV kontaktsenter.

## Modenhet
**Høy modenhet** - bred innføring og etablert samhandlingsmodell mellom kommune og stat:
- NAV oppgir at digital soknad er tilgjengelig i 348 kommuner (99,8 prosent av befolkningen), med tilsvarende høy dekning for innsynsløsninger.
- Tjenesten har etablert teknisk dokumentasjon, API-spesifikasjoner og tydelig konfigurasjonsløp i Fiks.
- Drifts- og sikkerhetsmodellen er beskrevet med kryptering, autentisering og fallback-mekanismer.

**Deduksjon:** Fiks Digisos er moden som samhandlingsløsning i et avgrenset domene (økonomisk sosialhjelp), men verdien er tett knyttet til integrasjonskvalitet i kommunale fagsystemer og gode avtaler mellom aktørene.

## Kort beskrivelse
Fiks Digisos er en nasjonal samhandlings- og integrasjonstjeneste for digital behandling av søknader om økonomisk sosialhjelp. Løsningen kobler innbyggersøknad på nav.no med kommunale fagsystemer gjennom Fiks-plattformen, slik at søknader, ettersendelser og saksoppdateringer kan flyte sikkert mellom NAV, kommune og innbygger.

Produktet skaper verdi ved at innbygger får et mer sammenhengende søknads- og oppfølgingsløp, mens kommunene får bedre kvalitet i søknader og mer effektiv saksbehandling. I NA-sammenheng er Fiks Digisos interessant fordi det representerer en konkret tversnivåløsning mellom statlig kanal (nav.no) og kommunal tjenesteutøvelse.

## Kapabiliteter
- **Samarbeid: Organisatorisk samhandling**
  Fiks Digisos kobler NAV, kommuner, KS Digital og fagsystemleverandører i et felles operativt samhandlingsløp for sosialhjelp.
- **Sluttbrukertjenester: Sammenhengende tjenester**
  Søker kan sende søknad, ettersende dokumentasjon og følge saksgang i en sammenhengende brukerreise på nav.no.
- **Datautveksling og integrasjon: Dele data med andre**
  Tjenesten deler og overfører søknads- og saksdata kontrollert mellom statlige og kommunale systemer gjennom Fiks API-er og meldingskanaler.

## Produktmål
Dokumenterte mål:
- Tilrettelegge for kommunal behandling av sosialsoknader sendt fra nav.no.
- Gi innbygger innsyn i saksgang og dokumenter.
- Gi NAV kontaktsenter tilgang til sentrale opplysninger slik at brukere får bedre veiledning.

Operative mål utledet fra kildene:
- Redusere manuelt arbeid og forbedre kvaliteten i kommunal saksbehandling av sosialhjelp.
- Styrke samhandling mellom NAV og kommunene i et felles digitalt tjenesteløp.
- Sikre trygg og sporbar håndtering av sensitive opplysninger i hele flyten.

## Brukerbehov
- Innbyggere trenger enkel digital soknad og fortløpende status på egen sak.
- Kommunale saksbehandlere trenger mer komplette soknader og mindre manuell oppfølging.
- NAV kontaktsenter trenger tilgang til sentral sakstatus for a kunne gi bedre forstelinjeveiledning.
- Kommuner og leverandorer trenger standardiserte API-er og tydelige konfigurasjonsløp for drift og integrasjon.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Innbyggere som soker sosialhjelp | Enkel innsending og innsyn i egen sak | Soknad, ettersending og oppfølging på nav.no | Primær sluttbruker |
| Kommunale sosialtjenester | Effektiv og trygg saksbehandling | Mottak, behandling og oppdatering av saker | Primær virksomhetsbruker |
| NAV kontaktsenter | Innsyn i sentrale stonadsopplysninger | Veiledning i forstelinje | Avhenger av kommunal aktivering |
| Fagsystemleverandorer | Stabil integrasjon mot Fiks Digisos | API-integrasjoner og meldingsflyt | Teknisk brukergruppe |
| KS Digital og NAV/Arbeids- og velferdsdirektoratet | Forvaltning, videreutvikling og samhandling | KS Digital har tjenesteforvaltning; NAV har statlig fag- og kanalansvar | Delte roller i okosystemet |

## Hovedfunksjoner
Fiks Digisos sin kjernefunksjon er a motta digitale soknader om økonomisk sosialhjelp fra nav.no og levere disse trygt til kommunens fagsystem for videre behandling. Løsningen fungerer som et sammenbindende lag mellom statlig brukerflate og kommunal tjenesteutovelse.

Tjenesten gir ogsa innbygger et sammenhengende oppfølgingsløp med innsyn i saksgang og dokumenter. Dette reduserer behovet for manuell statushenvendelser og gir bedre transparens i prosessen.

Teknisk bygger Digisos på flere Fiks-komponenter, blant annet Digisos API, dokumentlager, Fiks IO og i noen løp SvarUt/SvarInn som alternativ kanal. Fallback fra Fiks IO til SvarUt gir robusthet ved integrasjonsutfordringer i mottakersystem.

Løsningen inkluderer sikkerhetsmekanismer som ID-porten-autentisering, transportkryptering, dokumentkryptering og logging i Fiks Audit. Dette er sentralt fordi tjenesten håndterer sensitive personopplysninger.

### Typiske brukssituasjoner
- når en innbygger sender digital soknad om økonomisk sosialhjelp på nav.no og kommunen behandler saken i eget fagsystem
- når innbygger ettersender dokumentasjon og følger status i samme digitale løp
- når NAV kontaktsenter trenger innsyn i sentrale opplysninger for a veilede soker
- når kommunen innforer ny digital sosialhjelpsflyt og trenger standardisert integrasjon

### Når Fiks Digisos normalt ikke er førstevalg
- når behovet gjelder andre kommunale tjenester enn sosialhjelp
- når virksomheten trenger en generell meldingsbro uten domene- og prosesslogikken i Digisos
- når saken gjelder intern fagsystemflyt uten samhandling mot nav.no eller NAV
- når behovet er statistikkregister eller langtidslagring for analyse (ikke operativ saksgang)

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Digital soknad, ettersendelse og innsyn for økonomisk sosialhjelp | Generell plattform for alle kommunale tjenester |
| Integrasjon mellom nav.no og kommunale fagsystem | Full kommunal saksbehandlingsløsning i seg selv |
| Kanalstyring via Fiks IO og/eller SvarUt/SvarInn | Erstatning for kommunens fagsystem |
| Samhandling med NAV kontaktsenter der aktivert | Andre NAV-domener utenfor Digisos-løsningene |

## Veikart over kommende funksjonalitet
Ingen samlet offentlig veikartsplan er hentet i denne arbeidsøkten. Kildene viser fortløpende videreutvikling i tjenesten, utbredelsesoppfølging og tilpasninger i integrasjonsløp.

## Forretningsverdi/Verdiforslag
- For innbyggere: enklere soknadsprosess og bedre oversikt over egen sak.
- For kommuner: høyere kvalitet i soknader og mindre tid brukt på administrativ oppfølging.
- For NAV: bedre førstelinjeoppfølging gjennom innsynsflate for kontaktsenter.
- For offentlig sektor samlet: konkret, skalerbar modell for digital samhandling på tvers av forvaltningsnivå.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Integrasjon | Ulik modenhet i kommunale fagsystem kan gi variasjon i flyt og stabilitet | Tydelig API-dokumentasjon, konfigurasjonsveiviser og fallback-kanaler |
| Informasjonssikkerhet | Sensitivt datainnhold krever robust beskyttelse i hele kjeden | Kryptering, autentisering, logging og tydelig ansvarsdeling |
| Samhandlingsstyring | Flere aktører med ulike roller kan skape uklarhet i ansvar | Klare avtaler, databehandlerroller og felles forvaltningsmodeller |
| Brukeropplevelse | Ulik lokal innføring kan gi varierende innbyggeropplevelse | Standardiserte løp og tett oppfølging ved innføring |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-digisos/
- https://developers.fiks.ks.no/tjenester/digisos/
- https://www.nav.no/samarbeidspartner/digisos

## Plattform
Tjenesten leveres på Fiks-plattformen med webgrensesnitt på nav.no for innbygger og maskin-til-maskin-integrasjoner mot kommunale fagsystemer.

## Gjenbruk
Fiks Digisos har høy gjenbruksverdi for kommuner som skal digitalisere sosialhjelp i standardisert samspill med NAV. Gjenbruk utenfor dette domenet er begrenset fordi tjenesten har spesifikk prosesslogikk for økonomisk sosialhjelp.

**Vanlige kombinasjoner med andre produkter:**
- `Fiks-plattformen`
- `Fiks IO`
- `Fiks SvarUt` og `SvarInn`
- `ID-porten` (for innbyggers autentisering)
- NAVs løsninger på nav.no

**Kildekode:** Ikke offentlig dokumentert. Selve tjenesten er ikke publisert som åpen kildekode, men klientbibliotek og SDK-er for Fiks-plattformen er tilgjengelige på [github.com/ks-no](https://github.com/ks-no), flere av dem under MIT-lisens.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Losningen muligjor kontrollert deling av søknads- og saksdata mellom statlig og kommunal sektor.
- **P6: Lag digitale løsninger som støtter samhandling**
  Produktet er bygget for samhandling på tvers av forvaltningsnivå, med tydelig arbeidsdeling mellom NAV og kommune.

Svakhet: Domenet er smalt (økonomisk sosialhjelp), så overførbarheten til andre tjenesteområder avhenger av tilsvarende organisatorisk og juridisk tilrettelegging.

## Finansiering
Kommuner må inngå avtaler med aktørene i Digisos-samarbeidet, og bruk av løsningene er forbundet med kostnader. Finansieringsmodell er dermed delt mellom kommunal betaling og felles forvaltning i samarbeidet mellom KS Digital og NAV-side.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Tjenesteforvaltning i Fiks | KS Digital | KS Digital og developers.fiks |
| Statlig kanal og domeneoppfølging | Arbeids- og velferdsdirektoratet / NAV | nav.no samarbeidspartnersider |
| Lokal operativ bruk | Kommuner | Digisos innførings- og avtalesider |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-digisos/
- https://developers.fiks.ks.no/tjenester/digisos/
- https://www.nav.no/samarbeidspartner/digisos

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-digisos/ (kontrollert 2026-05-03)
- Nettkilde: https://developers.fiks.ks.no/tjenester/digisos/ (kontrollert 2026-05-03)
- Nettkilde: https://www.nav.no/samarbeidspartner/digisos (kontrollert 2026-05-03)
