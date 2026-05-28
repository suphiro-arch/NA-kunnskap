# Produkt-canvas: Fiks Digisos

## Navn
Fiks Digisos

## Ressurs ID
KS-012

## Status/Livsfase
**Produksjon** - etablert tjeneste i drift i kommunesektoren, med høy utbredelse i Norge.

**Fakta:** KS Digital beskriver Fiks Digisos som en tjeneste for kommunal behandling av sosialsoknader via nav.no. NAV beskriver Digisos som et samarbeid mellom KS Digital, kommunene og Arbeids- og velferdsdirektoratet, med losninger for digital soknad, innsyn for soker og innsynsflate for NAV kontaktsenter.

## Modenhet
**Hoy modenhet** - bred innforing og etablert samhandlingsmodell mellom kommune og stat:
- NAV oppgir at digital soknad er tilgjengelig i 348 kommuner (99,8 prosent av befolkningen), med tilsvarende hoy dekning for innsynslosninger.
- Tjenesten har etablert teknisk dokumentasjon, API-spesifikasjoner og tydelig konfigurasjonslop i Fiks.
- Drifts- og sikkerhetsmodellen er beskrevet med kryptering, autentisering og fallback-mekanismer.

**Deduksjon:** Fiks Digisos er moden som samhandlingslosning i et avgrenset domene (okonomisk sosialhjelp), men verdien er tett knyttet til integrasjonskvalitet i kommunale fagsystemer og gode avtaler mellom aktorene.

## Kort beskrivelse
Fiks Digisos er en nasjonal samhandlings- og integrasjonstjeneste for digital behandling av soknader om okonomisk sosialhjelp. Losningen kobler innbyggersoknad pa nav.no med kommunale fagsystemer gjennom Fiks-plattformen, slik at soknader, ettersendelser og saksoppdateringer kan flyte sikkert mellom NAV, kommune og innbygger.

Produktet skaper verdi ved at innbygger far et mer sammenhengende soknads- og oppfolgingslop, mens kommunene far bedre kvalitet i soknader og mer effektiv saksbehandling. I NA-sammenheng er Fiks Digisos interessant fordi det representerer en konkret tversnivalosning mellom statlig kanal (nav.no) og kommunal tjenesteutovelse.

## Kapabiliteter
- **Samarbeid: Organisatorisk samhandling**
  Fiks Digisos kobler NAV, kommuner, KS Digital og fagsystemleverandorer i et felles operativt samhandlingslop for sosialhjelp.
- **Sluttbrukertjenester: Sammenhengende tjenester**
  Soker kan sende soknad, ettersende dokumentasjon og folge saksgang i en sammenhengende brukerreise pa nav.no.
- **Datautveksling og integrasjon: Dele data med andre**
  Tjenesten deler og overforer soknads- og saksdata kontrollert mellom statlige og kommunale systemer gjennom Fiks API-er og meldingskanaler.

## Produktmal
Dokumenterte mal:
- Tilrettelegge for kommunal behandling av sosialsoknader sendt fra nav.no.
- Gi innbygger innsyn i saksgang og dokumenter.
- Gi NAV kontaktsenter tilgang til sentrale opplysninger slik at brukere far bedre veiledning.

Operative mal utledet fra kildene:
- Redusere manuelt arbeid og forbedre kvaliteten i kommunal saksbehandling av sosialhjelp.
- Styrke samhandling mellom NAV og kommunene i et felles digitalt tjenestelop.
- Sikre trygg og sporbar handtering av sensitive opplysninger i hele flyten.

## Brukerbehov
- Innbyggere trenger enkel digital soknad og fortlopende status pa egen sak.
- Kommunale saksbehandlere trenger mer komplette soknader og mindre manuell oppfolging.
- NAV kontaktsenter trenger tilgang til sentral sakstatus for a kunne gi bedre forstelinjeveiledning.
- Kommuner og leverandorer trenger standardiserte API-er og tydelige konfigurasjonslop for drift og integrasjon.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primaere behov | Bruksomrade | Kommentar |
|---|---|---|---|
| Innbyggere som soker sosialhjelp | Enkel innsending og innsyn i egen sak | Soknad, ettersending og oppfolging pa nav.no | Primar sluttbruker |
| Kommunale sosialtjenester | Effektiv og trygg saksbehandling | Mottak, behandling og oppdatering av saker | Primar virksomhetsbruker |
| NAV kontaktsenter | Innsyn i sentrale stonadsopplysninger | Veiledning i forstelinje | Avhenger av kommunal aktivering |
| Fagsystemleverandorer | Stabil integrasjon mot Fiks Digisos | API-integrasjoner og meldingsflyt | Teknisk brukergruppe |
| KS Digital og NAV/Arbeids- og velferdsdirektoratet | Forvaltning, videreutvikling og samhandling | KS Digital har tjenesteforvaltning; NAV har statlig fag- og kanalansvar | Delte roller i okosystemet |

## Hovedfunksjoner
Fiks Digisos sin kjernefunksjon er a motta digitale soknader om okonomisk sosialhjelp fra nav.no og levere disse trygt til kommunens fagsystem for videre behandling. LOsningen fungerer som et sammenbindende lag mellom statlig brukerflate og kommunal tjenesteutovelse.

Tjenesten gir ogsa innbygger et sammenhengende oppfolgingslop med innsyn i saksgang og dokumenter. Dette reduserer behovet for manuell statushenvendelser og gir bedre transparens i prosessen.

Teknisk bygger Digisos pa flere Fiks-komponenter, blant annet Digisos API, dokumentlager, Fiks IO og i noen lop SvarUt/SvarInn som alternativ kanal. Fallback fra Fiks IO til SvarUt gir robusthet ved integrasjonsutfordringer i mottakersystem.

LOsningen inkluderer sikkerhetsmekanismer som ID-porten-autentisering, transportkryptering, dokumentkryptering og logging i Fiks Audit. Dette er sentralt fordi tjenesten handterer sensitive personopplysninger.

### Typiske brukssituasjoner
- nar en innbygger sender digital soknad om okonomisk sosialhjelp pa nav.no og kommunen behandler saken i eget fagsystem
- nar innbygger ettersender dokumentasjon og folger status i samme digitale lop
- nar NAV kontaktsenter trenger innsyn i sentrale opplysninger for a veilede soker
- nar kommunen innforer ny digital sosialhjelpsflyt og trenger standardisert integrasjon

### Nar Fiks Digisos normalt ikke er forstevalg
- nar behovet gjelder andre kommunale tjenester enn sosialhjelp
- nar virksomheten trenger en generell meldingsbro uten domene- og prosesslogikken i Digisos
- nar saken gjelder intern fagsystemflyt uten samhandling mot nav.no eller NAV
- nar behovet er statistikkregister eller langtidslagring for analyse (ikke operativ saksgang)

### Scope og avgrensning
| Inngar | Inngar ikke |
|---|---|
| Digital soknad, ettersendelse og innsyn for okonomisk sosialhjelp | Generell plattform for alle kommunale tjenester |
| Integrasjon mellom nav.no og kommunale fagsystem | Full kommunal saksbehandlingslosning i seg selv |
| Kanalstyring via Fiks IO og/eller SvarUt/SvarInn | Erstatning for kommunens fagsystem |
| Samhandling med NAV kontaktsenter der aktivert | Andre NAV-domener utenfor Digisos-losningene |

## Veikart over kommende funksjonalitet
Ingen samlet offentlig veikartsplan er hentet i denne arbeidsokten. Kildene viser fortlopende videreutvikling i tjenesten, utbredelsesoppfolging og tilpasninger i integrasjonslop.

## Forretningsverdi/Verdiforslag
- For innbyggere: enklere soknadsprosess og bedre oversikt over egen sak.
- For kommuner: hoyere kvalitet i soknader og mindre tid brukt pa administrativ oppfolging.
- For NAV: bedre forstelinjeoppfolging gjennom innsynsflate for kontaktsenter.
- For offentlig sektor samlet: konkret, skalerbar modell for digital samhandling pa tvers av forvaltningsniva.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Handtering |
|---|---|---|
| Integrasjon | Ulik modenhet i kommunale fagsystem kan gi variasjon i flyt og stabilitet | Tydelig API-dokumentasjon, konfigurasjonsveiviser og fallback-kanaler |
| Informasjonssikkerhet | Sensitivt datainnhold krever robust beskyttelse i hele kjeden | Kryptering, autentisering, logging og tydelig ansvarsdeling |
| Samhandlingsstyring | Flere aktorer med ulike roller kan skape uklarhet i ansvar | Klare avtaler, databehandlerroller og felles forvaltningsmodeller |
| Brukeropplevelse | Ulik lokal innforing kan gi varierende innbyggeropplevelse | Standardiserte lop og tett oppfolging ved innforing |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-digisos/
- https://developers.fiks.ks.no/tjenester/digisos/
- https://www.nav.no/samarbeidspartner/digisos

## Plattform
Tjenesten leveres pa Fiks-plattformen med webgrensesnitt pa nav.no for innbygger og maskin-til-maskin-integrasjoner mot kommunale fagsystemer.

## Gjenbruk
Fiks Digisos har hoy gjenbruksverdi for kommuner som skal digitalisere sosialhjelp i standardisert samspill med NAV. Gjenbruk utenfor dette domenet er begrenset fordi tjenesten har spesifikk prosesslogikk for okonomisk sosialhjelp.

**Vanlige kombinasjoner med andre produkter:**
- `Fiks-plattformen`
- `Fiks IO`
- `Fiks SvarUt` og `SvarInn`
- `ID-porten` (for innbyggers autentisering)
- NAVs losninger pa nav.no

## Stotter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Losningen muligjor kontrollert deling av soknads- og saksdata mellom statlig og kommunal sektor.
- **P6: Lag digitale losninger som stotter samhandling**
  Produktet er bygget for samhandling pa tvers av forvaltningsniva, med tydelig arbeidsdeling mellom NAV og kommune.

Svakhet: Domenet er smalt (okonomisk sosialhjelp), sa overforbarheten til andre tjenesteomrader avhenger av tilsvarende organisatorisk og juridisk tilrettelegging.

## Finansiering
Kommuner ma innga avtaler med aktorene i Digisos-samarbeidet, og bruk av losningene er forbundet med kostnader. Finansieringsmodell er dermed delt mellom kommunal betaling og felles forvaltning i samarbeidet mellom KS Digital og NAV-side.

## Forvaltning/eier
| Ansvarsomrade | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Tjenesteforvaltning i Fiks | KS Digital | KS Digital og developers.fiks |
| Statlig kanal og domeneoppfolging | Arbeids- og velferdsdirektoratet / NAV | nav.no samarbeidspartnersider |
| Lokal operativ bruk | Kommuner | Digisos innforings- og avtalesider |

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
