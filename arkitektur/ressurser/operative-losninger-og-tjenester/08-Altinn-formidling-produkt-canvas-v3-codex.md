# Produkt-canvas: Altinn Formidling

## Navn
Altinn Formidling

## Ressurs ID
DIGDIR-008

## Status/Livsfase
**Produksjon** - etablert formidlingstjeneste i Altinn for styrt og sporbar filoverføring mellom avsendere og mottakere.

**Fakta:** Offisiell dokumentasjon bruker nå i stor grad navnet Altinn Broker, men beskriver den samme formidlingstjenesten med støtte for ende-til-ende filoverføringer, store payloads, logging, varsling og hendelsesabonnementer per 26. mars 2026.

## Modenhet
**Høy funksjonell modenhet** - produktet fremstår som en etablert integrasjonstjeneste med tydelig dokumenterte funksjoner:
- Tjenesten har egen produktdokumentasjon, oppstartsguider og referansestoff.
- Dokumentasjonen dekker både operativ bruk, API-tilgang og hendelsesabonnementer.
- Løsningen er tydelig avgrenset mot andre Altinn-produkter ved at den håndterer filoverføring, ikke generell hendelsesdeling eller sluttbrukerdialog.

**Deduksjon:** Produktet er modent som formidlingsledd for store og asynkrone leveranser, men bør forstås som styrt filoverføring og ikke som en generell meldings- eller prosessmotor.

## Kort beskrivelse
Altinn Formidling er Altinns formidlingstjeneste for sikker og styrt overføring av filer mellom avsendere og mottakere. Produktet er laget for situasjoner der store eller viktige payloads må overføres asynkront, spores og kunne hentes av autoriserte mottakere uten at avsender og mottaker trenger å være tett koblet i samme prosess.

Produktet har både en tjenesteflate og en integrasjonsflate. Tjenesteflaten består av styrt filoverføring med logging, status, varsling og tilgangskontroll. Integrasjonsflaten består av API-er og abonnementer som gjør det mulig å sende, hente og følge leveranser programmatisk. Dette gjør produktet bredere enn et rent transport-API, men smalere enn en full meldingsløsning med egen sluttbrukerdialog.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** gjør det mulig for mottakere å hente formidlede filer gjennom en kontrollert tjeneste.
- **Datautveksling og integrasjon: Dele data med andre** gjør det mulig for avsendere å levere filer til andre virksomheter gjennom en felles kanal.
- **Datautveksling og integrasjon: Meldingsformidling** er kjernefunksjonen og dekker sikker, asynkron overføring og oppfølging av leveranser.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** støttes gjennom tilgangskontroll, logging og sikker håndtering av innhold.
- **Samarbeid: Organisatorisk samhandling** gjør det mulig å etablere standardiserte leveranseløp mellom virksomheter.
- **Tjenesteutvikling: Integrerbare tjenester** tilbyr API-er og integrasjonsmønstre som kan brukes av fagsystemer og integrasjonsmiljøer.

## Produktmål
**Primærkilder:** Altinn Broker-dokumentasjonen, «Hva får du?» og oppstartsveiledning.

Dokumenterte mål:
- Tilby ende-til-ende filoverføringer mellom avsender og mottaker.
- Håndtere store payloads som ikke passer godt i vanlige API-kall eller enklere meldingsmønstre.
- Gi sporbarhet gjennom logging, varsling og statusoppfølging.
- Gi kontrollert tilgang til filoverføringer for autoriserte brukere og systemer.

Operative mål utledet fra de samme kildene:
- Redusere behovet for proprietære eller punkt-til-punkt-baserte filoverføringsløsninger.
- Gjøre det mulig å bygge robuste leveranseløp med både API-tilgang og hendelsesbasert oppfølging.
- Gi tjenesteeiere oversikt over eget forbruk og egne overføringer.

**Deduksjon:** Produktet har også en viktig rolle som nasjonalt standardmønster for filoverføring der hverken synkrone API-kall eller rene hendelser alene er tilstrekkelige.

## Brukerbehov
- Avsendende virksomheter trenger en sikker og sporbar kanal for å overføre filer til andre.
- Mottakende virksomheter trenger en kontrollert måte å hente og følge opp leveranser på.
- Integrasjonsteam trenger API-er og hendelsesabonnementer for å automatisere overføring og oppfølging.
- Forvaltnings- og sikkerhetsmiljøer trenger logging, tilgangskontroll og oversikt over bruk.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Avsendende virksomheter | Sende filer sikkert og asynkront | Overføring av dokumenter, dataleveranser og andre payloads | Trenger en kanal som tåler større payloads og løs kobling |
| Mottakende virksomheter | Hente og følge opp leveranser | Mottak, behandling og kvittering for filer | Bruker produktet som kontrollert innboks for overføringer |
| Integrasjonsteam og systemleverandører | API-er og hendelsesoppfølging | Automatisert innsending, uthenting og statusoppfølging | Viktig for maskin-til-maskin-samhandling |
| Tjenesteeiere og forvaltningsmiljøer | Oversikt og styring | Oppsett av tjenester, tilgang og forbruk | Produktet dekker også operativ kontrollflate, ikke bare API |
| Sikkerhets- og revisjonsmiljøer | Sporbarhet og kontroll | Logging, hendelsesspor og tilgangsstyring | Sentralt når innhold og leveranser er sensitive eller kritiske |

## Hovedfunksjoner
Altinn Formidling håndterer først og fremst styrt filoverføring fra opprettelse og sending til mottak og oppfølging. Dokumentasjonen beskriver ende-til-ende filoverføringer som hovedverdi, noe som gjør produktet særlig relevant når store eller viktige leveranser må håndteres robust over tid. Produktet dekker derfor et annet behov enn vanlige API-kall: det gir et mellomliggende formidlingsledd med egen kontroll, sporbarhet og uthenting.

Produktet har også tydelig støtte for store payloads og ulike filformater. Dette er en viktig avgrensning mot både enklere meldingsmønstre og mer hendelsesorienterte produkter i Altinn. Formidling er riktig når det primære behovet er sikker transport og kontrollert tilgjengeliggjøring av filer, ikke når det primære behovet er å eksponere dialog, varsle sluttbrukere eller publisere domenehendelser.

En sentral del av løsningen er samspillet mellom transport, hendelser og tilgangskontroll. Dokumentasjonen viser at tjenesten støtter varsling, hendelsesabonnementer og avansert tilgangsstyring, slik at avsender og mottaker kan følge om leveransen er kommet frem og håndtere prosessen videre i egne systemer. Det betyr at produktet ikke bare er et filarkiv eller en opplastings-API, men en kontrollert formidlingstjeneste med egen operativ logikk.

Produktet har dessuten en forvaltningsflate gjennom oversikt over eget forbruk og tjenestekonfigurasjon. Dette styrker løsningsbredden: Altinn Formidling er både en integrasjonstjeneste og en operativ fellestjeneste for styrte leveranser. Samtidig inngår ikke forretningslogikken for hva filene betyr eller hvordan de viderebehandles hos mottaker; dette ligger fortsatt hos avsender- og mottakersystemene.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Ende-til-ende filoverføring mellom avsender og mottaker | Faglig tolkning og behandling av innholdet i filene |
| API-tilgang for sending, uthenting og oppfølging | Generell publisering av domenehendelser uten payloadoverføring |
| Logging, varsling og hendelsesabonnementer knyttet til leveranser | Sluttbrukerdialog eller meldingsboks for innbyggere og virksomheter |
| Tilgangsstyring for filoverføringer | Full prosessmotor eller saksbehandlingssystem |
| Støtte for store payloads og ulike filformater | Datakatalog eller åpen delingsportal |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 26. mars 2026):**
- Dokumentasjonen viser eksisterende støtte for store payloads, logging, varsling, hendelsesabonnementer og API-tilgang.
- Produktet har også offentlig backlog i tilknytning til dokumentasjonen.

**Ikke offentlig dokumentert i brukte kilder:** Tidsfestet roadmap med prioriterte leveranser i samlet form.

**Deduksjon:** Videreutviklingen vil trolig dreie seg om forbedringer i integrasjonsopplevelse, styring, hendelsesoppfølging og drift av store overføringer, men dette bør ikke konkretiseres mer enn kildene støtter.

## Forretningsverdi/Verdiforslag
### For avsendere og mottakere
- Gir en felles og robust kanal for overføring av filer som ellers kunne krevd egne transportløsninger.
- Reduserer behovet for tett koblede integrasjoner mellom avsender og mottaker.

### For integrasjonsmiljøer
- Gir standardiserte API-er og oppfølgingsmekanismer for filbasert samhandling.
- Gjør det enklere å bygge automatiserte leveranseløp med status og hendelser.

### For offentlig sektor
- Øker gjenbruk av én nasjonal formidlingstjeneste i stedet for mange lokale varianter.
- Styrker sporbarhet og kontroll i samhandlingsløp som involverer store eller viktige payloads.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil bruk av formidlingstjenesten kan gi overføring av innhold uten riktig hjemmel eller avtalegrunnlag | Tydelig ansvar hos tjenesteeier og klare tjenesteregler |
| Teknisk | Store payloads og asynkrone leveranser kan gi krevende feil- og gjenopptakssituasjoner | Robust klientimplementasjon, tydelig statusmodell og god overvåking |
| Sikkerhet | Feil tilgangsstyring kan gi uvedkommende tilgang til filer eller metadata | Streng tilgangskontroll, logging og revisjon |
| Forvaltning | Uklare grenser mot Events eller andre meldingsprodukter kan gi feil produktvalg | Tydelig produktavgrensning og god veiledning i dokumentasjonen |
| Brukeropplevelse | Asynkron flyt kan gjøre det vanskelig å oppdage forsinkelser eller feil uten god oppfølging | Varsling, hendelsesabonnementer og oversiktsflater for oppfølging |

## Kanaler
- Produktside: https://docs.altinn.studio/nb/broker/
- Hva får du?: https://docs.altinn.studio/nb/broker/what-do-you-get/
- Kom i gang: https://docs.altinn.studio/nb/broker/getting-started/
- Referanse: https://docs.altinn.studio/nb/broker/reference/

## Plattform
Formidlingstjeneste i Altinn-porteføljen med API-er, hendelsesabonnementer og kontrollert tilgang til filoverføringer.

**Fakta:** Dokumentasjonen beskriver støtte for store payloads, logging, varsling, hendelsesabonnementer, API-tilgang og oversikt over eget forbruk. Dette viser at produktet er både integrasjonstjeneste og operativ formidlingstjeneste.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur og detaljert intern plattformimplementasjon.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet kan brukes av mange virksomheter som trenger samme grunnmønster for sikker filoverføring.
- Det reduserer behovet for lokale spesialløsninger for store og asynkrone leveranser.
- Gjenbruksverdien er særlig høy når behovet er robust transport av payloads, ikke når behovet er hendelsesdeling eller sluttbrukerkommunikasjon.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** støttes ved at data kan deles gjennom en felles, kontrollert overføringsmekanisme.
- **P5: Del og gjenbruk løsninger** realiseres ved at én formidlingstjeneste kan brukes av mange virksomheter.
- **P6: Lag digitale løsninger som støtter samhandling** styrkes fordi produktet tilbyr et standardmønster for asynkron samhandling.
- **P7: Sørg for tillit til oppgaveløsningen** støttes gjennom tilgangskontroll, logging og sporbarhet.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Egen finansieringsmodell eller separat kostnadsnivå for produktet isolert fra Altinn-porteføljen.
- **Deduksjon:** Produktet må forstås som del av Altinns samlede forvaltning og finansiering.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir / Altinn-forvaltningen | Offisiell produktdokumentasjon |
| Driftsansvar | Altinns forvaltnings- og driftsmiljø | Produktet beskrives som del av Altinn-porteføljen |
| Budsjettansvar | Del av Altinn-porteføljen | Ingen separat offentlig kostnadsmodell verifisert |
| Styringsmodell | Produktforvaltning i Altinn | Fremgår av produktstruktur og dokumentasjon |

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/broker/
- https://docs.altinn.studio/nb/broker/what-do-you-get/
- https://docs.altinn.studio/nb/broker/getting-started/
- https://docs.altinn.studio/nb/broker/reference/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/08-Altinn-formidling-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.altinn.studio/nb/broker/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/broker/what-do-you-get/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/broker/getting-started/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/broker/reference/ (kontrollert 2026-03-26)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen er oppdatert mot dagens Altinn Broker-dokumentasjon og ikke bare eldre antakelser om «formidling».
- Uverifiserte påstander om volum, intern teknologistack, SLA og kostnader er fjernet.
- Produktet er tydeligere avgrenset mot Events og andre Altinn-produkter.

### Tekstlige forbedringer
- Navn og hovedtekst er skrevet om til en tydeligere beskrivelse av styrt filoverføring som produkt.
- Hovedfunksjoner beskriver nå både tjenesteflate og integrasjonsflate.
- Språket er gjort mer presist og mindre preget av teknisk oppramsing og spekulasjon.



