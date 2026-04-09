# Produkt-canvas: Fiks melding

## Navn
Fiks melding

## Ressurs ID
KS-002

## Status/Livsfase
**Produksjon** - etablert meldingstjeneste i KS Digital med flere operative kanaler, publisert veiledningsløp og dokumentert sikkerhetsgrunnlag.

**Fakta:** KS Digital beskriver Fiks melding som en plattform for å sende informasjon gjennom ulike kanaler, der kommunen selv velger hvilke kanaler som tas i bruk og betaler for faktisk bruk. Produktsiden og prisinformasjonen viser at løsningen er i ordinær bruk med flere aktive undertjenester.

## Modenhet
**Høy funksjonell modenhet** - løsningen har et tydelig kanalsett, etablert avtalegrunnlag, publiserte veiledere og dokumentert sikkerhetsstøtte for flere bruksmønstre.

- Tjenesten omfatter konkrete kanaler og funksjoner for SMS, dokumentdeling, eDialog og utsending av brev.
- KS Digital publiserer både produktinformasjon, prisinformasjon og teknisk dokumentasjon for deler av funksjonssettet.
- Produktet er modent som felles kanalplattform, men detaljmodenheten varierer mellom undertjenestene og hvor dypt de er integrert i lokale arbeidsprosesser.

**Deduksjon:** Modenheten er høy for det overordnede kanalgrunnlaget og for praktisk bruk i kommunal sektor. Samtidig må produktet forstås som en familie av meldingskanaler og kommunikasjonsmønstre, ikke som én ensartet funksjon.

## Kort beskrivelse
Fiks melding er KS Digitals kanalplattform for meldingsutveksling og dokumentdeling i kommunal sektor. Løsningen gjør det mulig å sende og motta informasjon gjennom flere ulike kommunikasjonsformer fra samme tjenestegrunnlag, slik at kommunen kan velge kanal etter behov, risiko og brukssituasjon. Produktet dekker både utgående og inngående kommunikasjon, og kan brukes til alt fra enkel varsling og deling av dokumenter til sikker innsending og masseutsendelser. I praksis er Fiks melding derfor ikke bare en enkelt meldingstjeneste, men et samlet kommunikasjonsområde med flere operative undertjenester og arbeidsmåter.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** er produktets kjernefunksjon fordi løsningen pakker, sender, mottar og leverer meldinger og dokumenter gjennom flere valgbare kanaler fra samme tjenestegrunnlag.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** er direkte relevant fordi produktet brukes til sikker kommunikasjon og KS Digital publiserer eget sikkerhetsunderlag for ROS og DPIA for deler av funksjonssettet.
- **Samarbeid: Organisatorisk samhandling** er direkte relevant fordi løsningen gir kommuner, innbyggere og andre virksomheter et felles kanalgrunnlag for digital kommunikasjon.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals produkt-, pris- og utviklerdokumentasjon kontrollert 2026-03-26.

## Produktmål
Dokumenterte mål:
- Gi kommunene kontroll over informasjonsflyten fra avsender til mottaker gjennom flere kanaler i samme løsning.
- Gjøre det mulig å sende informasjon gjennom ulike kommunikasjonsformer uten å etablere separate løsninger for hver kanal.
- Forenkle masseutsendelser, dokumentdeling og sikker kommunikasjon.

Operative mål utledet fra kildene:
- Redusere behovet for parallelle meldings- og kanalplattformer i kommunen.
- Gi kommunene et mer standardisert grunnlag for både enkel og sensitiv kommunikasjon.
- Gjøre kanalvalg, dokumentdeling og sikker innsending mer forutsigbar på tvers av ulike tjenesteområder.

## Brukerbehov
- Kommuner trenger én samlet løsning for ulike meldings- og kommunikasjonsløp i stedet for mange små kanalløsninger.
- Fagmiljøer trenger sikre og praktiske kanaler for både utsending, dokumentdeling og innkommende dialog.
- Tekniske miljøer trenger et felles integrasjons- og oppsettsmønster for kommunikasjonskanaler.
- Innbyggere og virksomheter trenger en kanal inn til kommunen i brukssituasjoner der sikker innsending eller dokumentdeling er nødvendig.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Håndtere flere kommunikasjonsløp i én løsning | Varsling, dokumentdeling, brev og sikker dialog | Primærbrukere av produktområdet |
| Fag- og tjenestemiljøer | Riktig kanal for ulike typer kommunikasjon | Utsending, innkommende dialog og deling av dokumenter i tjenesteproduksjon | Operative brukere |
| Innbyggere og virksomheter | Motta eller sende informasjon gjennom relevante kanaler | Mottak av meldinger, innsending via eDialog eller tilgang til delte dokumenter | Sekundærbrukere |
| Tekniske forvaltere og leverandører | Integrasjon, oppsett og sikker bruk av kanalene | Konfigurasjon, integrasjon og sikkerhetsvurdering | Teknisk brukergruppe |
| KS Digital | Forvalte kanalplattformen og støtte innføring | Produktforvaltning, sikkerhetsstøtte og videreutvikling | Sentral tjenesteforvalter |

## Hovedfunksjoner
### Primære funksjoner
Fiks melding sin viktigste funksjon er å samle flere kommunikasjonskanaler i ett felles tjenestegrunnlag for kommunal sektor. Produktet er derfor ikke bare en teknisk meldingstjeneste, men en kanalplattform som gjør det mulig å håndtere ulike former for kommunikasjon innenfor samme produktområde. Dette gir kommunene større frihet til å velge kanal etter innhold, risiko og arbeidsprosess.

Løsningen dekker flere forskjellige operative bruksmåter. Den støtter blant annet SMS for varsling og meldinger, deling av større dokumenter og filer, sikker innsending gjennom eDialog og utsending av brev til mange mottakere. Når disse funksjonene beskrives samlet, blir det tydelig at produktet er bredere enn én kanal og bredere enn én type kommunikasjon. Det er nettopp kombinasjonen av kanalene som utgjør produktets hovedverdi.

Produktet må også avgrenses tydelig mot nærliggende løsninger. Fiks melding dekker et generelt kommunikasjonsområde med flere kanaler, mens Fiks SvarUt er en mer spesialisert utsendingstjeneste for dokumentformidling med egen kanalstyring for digital og fysisk post. SvarInn er på sin side en spesialisert mottakstjeneste for innkommende post. Fiks melding er derfor best forstått som bred kanalplattform og meldingsområde, ikke som erstatning for hele SvarUt-/SvarInn-løpet.

En sentral del av funksjonen ligger i at kommunen kan ta i bruk bare de kanalene som er relevante lokalt. Produktsiden beskriver eksplisitt at kommunen velger hvilke kanaler som skal brukes og betaler for faktisk bruk. Det betyr at produktet både er fleksibelt og modulært: kommunene kan bygge videre på samme grunnlag uten å måtte innføre hele funksjonssettet samtidig.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Kanalplattform for SMS, dokumentdeling, eDialog og brevutsending | Lokal saksbehandling og arbeidsflyt i kommunens fagsystemer |
| Valg og bruk av flere kommunikasjonsformer innenfor samme produktområde | Full erstatning for alle spesialiserte dokument- og postløp i SvarUt og SvarInn |
| Veiledere, sikkerhetsunderlag og praktisk innføringsstøtte for kanalene | Nasjonal autoritativ datakilde eller register |
| Både utgående og enkelte inngående kommunikasjonsmønstre | Automatisk semantisk behandling av innhold eller full dialogplattform for alle brukstilfeller |

## Veikart over kommende funksjonalitet
**Fakta:** KS Digital publiserer løpende endringer, veiledere og sikkerhetsunderlag for deler av Fiks melding-området. Jeg fant ikke et samlet offentlig roadmap med tidsfestede milepæler i denne arbeidsøkten.

**Deduksjon:** Videreutviklingen vil trolig være kanalnær og behovsdrevet, med forbedringer i eksisterende undertjenester og eventuelt støtte for nye kommunikasjonsbehov innenfor samme produktområde.

## Forretningsverdi/Verdiforslag
### For kommuner
- Samler flere kommunikasjonskanaler i én fellestjeneste.
- Reduserer behovet for å etablere og forvalte ulike lokale kanalløsninger hver for seg.

### For fagmiljøer
- Gjør det enklere å velge riktig kanal for ulike typer kommunikasjon.
- Gir støtte for både enkel varsling, dokumentdeling og sikker dialog i samme produktområde.

### For sektoren
- Bidrar til mer standardisert og styrbar meldingsutveksling.
- Styrker gjenbruk av felles infrastruktur i stedet for parallelle kommunikasjonsløsninger.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil kanalvalg eller feil bruk av personopplysninger kan gi brudd på krav til konfidensialitet og personvern. | Bruke kanalene etter formål, gjøre lokale ROS- og DPIA-vurderinger og avgrense sensitiv bruk til riktige kanaler. |
| Teknisk | Avhengighet til flere kanaler og lokale integrasjoner kan gi ujevn leveransekvalitet eller vanskelig feilsøking. | Teste lokale oppsett, bruke dokumenterte integrasjonsmønstre og skille tydelig mellom kanalroller og produktområder. |
| Sikkerhet | Meldings- og dokumentløp kan inneholde sensitiv informasjon og store konsekvenser ved feil konfigurasjon. | Bygge på sikker kanalbruk, kryptering og dokumenterte sikkerhetsvurderinger. |
| Leverandør | Kommunen blir avhengig av sentral tjenesteforvaltning og kanaltilbudet som inngår i Fiks melding. | Tydelige avtaler, kjent prismodell og forutsigbar videreutvikling av kanalene. |
| Brukeropplevelse | Kommunikasjonen kan bli fragmentert hvis kanalene brukes ulikt eller uten tydelig tjenestedesign. | Bevisst valg av kanal per brukssituasjon og tydelig sammenheng mellom lokal prosess og valgt kommunikasjonsform. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-melding/
- https://ksdigital.no/avtaler-og-priser/prisoversikt-2026/
- https://developers.fiks.ks.no/tjenester/fiksmelding/fiks-sms/
- https://status.fiks.ks.no

## Plattform
Fiks melding er en sentralt forvaltet fellestjeneste i KS Digital og et eget kommunikasjonsområde på Fiks-plattformen.

**Fakta:**
- Tjenesten tilbyr flere kanaler for meldingsutveksling og dokumentdeling.
- Kommunen velger selv hvilke kanaler som skal tas i bruk.
- KS Digital publiserer veiledere, prisinformasjon og sikkerhetsunderlag for deler av funksjonssettet.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full driftsarkitektur og detaljert teknologistakk per kanal.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme tjenestegrunnlag kan brukes til flere kommunikasjonsbehov i mange kommuner.
- Gjenbruksverdien ligger i at kanalene kan kombineres og styres innenfor samme produktområde i stedet for å bygges og forvaltes hver for seg.
- Produktet er mest gjenbrukbart som felles kanalplattform, ikke som lokal spesialfunksjon.

## Støtter arkitekturprinsipper
- **P6: Lag digitale løsninger som støtter samhandling** - produktet er laget for strukturert kommunikasjon og meldingsutveksling mellom kommuner, innbyggere og andre virksomheter gjennom et felles kanalgrunnlag.
- **P7: Sørg for tillit til oppgaveløsningen** - sikker kommunikasjon og publisert sikkerhetsunderlag er sentrale deler av produktets verdi og praktiske bruk.

## Finansiering
**Fakta:** Kommunen må signere tjenestevedlegg i tillegg til hovedavtale for å ta i bruk Fiks melding, og prisoversikten for 2026 viser at brukeren betaler per kanal og faktisk bruk.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full finansieringsmodell for videreutvikling og sentral forvaltning utover publisert prisoversikt.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsiden, prisinformasjonen og avtalegrunnlaget ligger hos KS Digital. |
| Driftsansvar | Ikke offentlig detaljert spesifisert i brukte kilder | Må avklares i mer tekniske eller kontraktsnære kilder. |
| Budsjettansvar | Kombinasjon av sentral forvaltning og bruksbasert kundegrunnlag | Delvis utledet fra avtale- og prismodell på produktsiden. |
| Styringsmodell | KS Digital med sentral tjenesteforvaltning og kanalvis innførings- og sikkerhetsstøtte | Synlig i produktsiden og de tilhørende veiledningsløpene. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-melding/
- https://ksdigital.no/avtaler-og-priser/prisoversikt-2026/
- https://developers.fiks.ks.no/tjenester/fiksmelding/fiks-sms/
- https://status.fiks.ks.no

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/26-FIKS-Melding-produkt-canvas-v1-codex.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-melding/ (hentet 2026-03-26)
- Nettkilde: https://ksdigital.no/avtaler-og-priser/prisoversikt-2026/ (hentet 2026-03-26)
- Nettkilde: https://developers.fiks.ks.no/tjenester/fiksmelding/fiks-sms/ (hentet 2026-03-26)
- Nettkilde: https://status.fiks.ks.no/ (hentet 2026-03-26)

## Endringer fra forrige versjon
### Analyseforbedringer
- Oppdatert kildegrunnlag med ny kontroll av produktside, prisoversikt, teknisk dokumentasjon og driftsstatus 2026-03-26.
- Presisert at produktet må forstås som kanalplattform og produktområde med flere undertjenester, ikke bare som én meldingstjeneste.
- Tydeliggjort avgrensningen mot `Fiks SvarUt` og `SvarInn`.

### Tekstlige forbedringer
- Skrevet `Hovedfunksjoner` om til forklarende avsnitt som beskriver hele produktets operative rolle.
- Strammet inn språk og struktur i `Kort beskrivelse`, `Scope og avgrensning` og `Forretningsverdi`.
- Gjort produktrollen tydeligere for både forretningsside og arkitektur.


