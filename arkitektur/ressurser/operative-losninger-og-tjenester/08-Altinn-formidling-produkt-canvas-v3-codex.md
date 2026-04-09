# Produkt-canvas: Altinn Formidling

## Navn
Altinn Formidling

## Ressurs ID
DIGDIR-008

## Status/Livsfase
**Produksjon** - etablert formidlingstjeneste i Altinn for styrt og sporbar filoverfÃ¸ring mellom avsendere og mottakere.

**Fakta:** Offisiell dokumentasjon bruker nÃ¥ i stor grad navnet Altinn Broker, men beskriver den samme formidlingstjenesten med stÃ¸tte for ende-til-ende filoverfÃ¸ringer, store payloads, logging, varsling og hendelsesabonnementer per 26. mars 2026.

## Modenhet
**HÃ¸y funksjonell modenhet** - produktet fremstÃ¥r som en etablert integrasjonstjeneste med tydelig dokumenterte funksjoner:
- Tjenesten har egen produktdokumentasjon, oppstartsguider og referansestoff.
- Dokumentasjonen dekker bÃ¥de operativ bruk, API-tilgang og hendelsesabonnementer.
- LÃ¸sningen er tydelig avgrenset mot andre Altinn-produkter ved at den hÃ¥ndterer filoverfÃ¸ring, ikke generell hendelsesdeling eller sluttbrukerdialog.

**Deduksjon:** Produktet er modent som formidlingsledd for store og asynkrone leveranser, men bÃ¸r forstÃ¥s som styrt filoverfÃ¸ring og ikke som en generell meldings- eller prosessmotor.

## Kort beskrivelse
Altinn Formidling er Altinns formidlingstjeneste for sikker og styrt overfÃ¸ring av filer mellom avsendere og mottakere. Produktet er laget for situasjoner der store eller viktige payloads mÃ¥ overfÃ¸res asynkront, spores og kunne hentes av autoriserte mottakere uten at avsender og mottaker trenger Ã¥ vÃ¦re tett koblet i samme prosess.

Produktet har bÃ¥de en tjenesteflate og en integrasjonsflate. Tjenesteflaten bestÃ¥r av styrt filoverfÃ¸ring med logging, status, varsling og tilgangskontroll. Integrasjonsflaten bestÃ¥r av API-er og abonnementer som gjÃ¸r det mulig Ã¥ sende, hente og fÃ¸lge leveranser programmatisk. Dette gjÃ¸r produktet bredere enn et rent transport-API, men smalere enn en full meldingslÃ¸sning med egen sluttbrukerdialog.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** gjÃ¸r det mulig for mottakere Ã¥ hente formidlede filer gjennom en kontrollert tjeneste.
- **Datautveksling og integrasjon: Dele data med andre** gjÃ¸r det mulig for avsendere Ã¥ levere filer til andre virksomheter gjennom en felles kanal.
- **Datautveksling og integrasjon: Meldingsformidling** er kjernefunksjonen og dekker sikker, asynkron overfÃ¸ring og oppfÃ¸lging av leveranser.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** stÃ¸ttes gjennom tilgangskontroll, logging og sikker hÃ¥ndtering av innhold.
- **Samarbeid: Organisatorisk samhandling** gjÃ¸r det mulig Ã¥ etablere standardiserte leveranselÃ¸p mellom virksomheter.
- **Tjenesteutvikling: Integrerbare tjenester** tilbyr API-er og integrasjonsmÃ¸nstre som kan brukes av fagsystemer og integrasjonsmiljÃ¸er.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Altinn Broker-dokumentasjonen, Â«Hva fÃ¥r du?Â» og oppstartsveiledning.

Dokumenterte mÃ¥l:
- Tilby ende-til-ende filoverfÃ¸ringer mellom avsender og mottaker.
- HÃ¥ndtere store payloads som ikke passer godt i vanlige API-kall eller enklere meldingsmÃ¸nstre.
- Gi sporbarhet gjennom logging, varsling og statusoppfÃ¸lging.
- Gi kontrollert tilgang til filoverfÃ¸ringer for autoriserte brukere og systemer.

Operative mÃ¥l utledet fra de samme kildene:
- Redusere behovet for proprietÃ¦re eller punkt-til-punkt-baserte filoverfÃ¸ringslÃ¸sninger.
- GjÃ¸re det mulig Ã¥ bygge robuste leveranselÃ¸p med bÃ¥de API-tilgang og hendelsesbasert oppfÃ¸lging.
- Gi tjenesteeiere oversikt over eget forbruk og egne overfÃ¸ringer.

**Deduksjon:** Produktet har ogsÃ¥ en viktig rolle som nasjonalt standardmÃ¸nster for filoverfÃ¸ring der hverken synkrone API-kall eller rene hendelser alene er tilstrekkelige.

## Brukerbehov
- Avsendende virksomheter trenger en sikker og sporbar kanal for Ã¥ overfÃ¸re filer til andre.
- Mottakende virksomheter trenger en kontrollert mÃ¥te Ã¥ hente og fÃ¸lge opp leveranser pÃ¥.
- Integrasjonsteam trenger API-er og hendelsesabonnementer for Ã¥ automatisere overfÃ¸ring og oppfÃ¸lging.
- Forvaltnings- og sikkerhetsmiljÃ¸er trenger logging, tilgangskontroll og oversikt over bruk.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Avsendende virksomheter | Sende filer sikkert og asynkront | OverfÃ¸ring av dokumenter, dataleveranser og andre payloads | Trenger en kanal som tÃ¥ler stÃ¸rre payloads og lÃ¸s kobling |
| Mottakende virksomheter | Hente og fÃ¸lge opp leveranser | Mottak, behandling og kvittering for filer | Bruker produktet som kontrollert innboks for overfÃ¸ringer |
| Integrasjonsteam og systemleverandÃ¸rer | API-er og hendelsesoppfÃ¸lging | Automatisert innsending, uthenting og statusoppfÃ¸lging | Viktig for maskin-til-maskin-samhandling |
| Tjenesteeiere og forvaltningsmiljÃ¸er | Oversikt og styring | Oppsett av tjenester, tilgang og forbruk | Produktet dekker ogsÃ¥ operativ kontrollflate, ikke bare API |
| Sikkerhets- og revisjonsmiljÃ¸er | Sporbarhet og kontroll | Logging, hendelsesspor og tilgangsstyring | Sentralt nÃ¥r innhold og leveranser er sensitive eller kritiske |

## Hovedfunksjoner
Altinn Formidling hÃ¥ndterer fÃ¸rst og fremst styrt filoverfÃ¸ring fra opprettelse og sending til mottak og oppfÃ¸lging. Dokumentasjonen beskriver ende-til-ende filoverfÃ¸ringer som hovedverdi, noe som gjÃ¸r produktet sÃ¦rlig relevant nÃ¥r store eller viktige leveranser mÃ¥ hÃ¥ndteres robust over tid. Produktet dekker derfor et annet behov enn vanlige API-kall: det gir et mellomliggende formidlingsledd med egen kontroll, sporbarhet og uthenting.

Produktet har ogsÃ¥ tydelig stÃ¸tte for store payloads og ulike filformater. Dette er en viktig avgrensning mot bÃ¥de enklere meldingsmÃ¸nstre og mer hendelsesorienterte produkter i Altinn. Formidling er riktig nÃ¥r det primÃ¦re behovet er sikker transport og kontrollert tilgjengeliggjÃ¸ring av filer, ikke nÃ¥r det primÃ¦re behovet er Ã¥ eksponere dialog, varsle sluttbrukere eller publisere domenehendelser.

En sentral del av lÃ¸sningen er samspillet mellom transport, hendelser og tilgangskontroll. Dokumentasjonen viser at tjenesten stÃ¸tter varsling, hendelsesabonnementer og avansert tilgangsstyring, slik at avsender og mottaker kan fÃ¸lge om leveransen er kommet frem og hÃ¥ndtere prosessen videre i egne systemer. Det betyr at produktet ikke bare er et filarkiv eller en opplastings-API, men en kontrollert formidlingstjeneste med egen operativ logikk.

Produktet har dessuten en forvaltningsflate gjennom oversikt over eget forbruk og tjenestekonfigurasjon. Dette styrker lÃ¸sningsbredden: Altinn Formidling er bÃ¥de en integrasjonstjeneste og en operativ fellestjeneste for styrte leveranser. Samtidig inngÃ¥r ikke forretningslogikken for hva filene betyr eller hvordan de viderebehandles hos mottaker; dette ligger fortsatt hos avsender- og mottakersystemene.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Ende-til-ende filoverfÃ¸ring mellom avsender og mottaker | Faglig tolkning og behandling av innholdet i filene |
| API-tilgang for sending, uthenting og oppfÃ¸lging | Generell publisering av domenehendelser uten payloadoverfÃ¸ring |
| Logging, varsling og hendelsesabonnementer knyttet til leveranser | Sluttbrukerdialog eller meldingsboks for innbyggere og virksomheter |
| Tilgangsstyring for filoverfÃ¸ringer | Full prosessmotor eller saksbehandlingssystem |
| StÃ¸tte for store payloads og ulike filformater | Datakatalog eller Ã¥pen delingsportal |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 26. mars 2026):**
- Dokumentasjonen viser eksisterende stÃ¸tte for store payloads, logging, varsling, hendelsesabonnementer og API-tilgang.
- Produktet har ogsÃ¥ offentlig backlog i tilknytning til dokumentasjonen.

**Ikke offentlig dokumentert i brukte kilder:** Tidsfestet roadmap med prioriterte leveranser i samlet form.

**Deduksjon:** Videreutviklingen vil trolig dreie seg om forbedringer i integrasjonsopplevelse, styring, hendelsesoppfÃ¸lging og drift av store overfÃ¸ringer, men dette bÃ¸r ikke konkretiseres mer enn kildene stÃ¸tter.

## Forretningsverdi/Verdiforslag
### For avsendere og mottakere
- Gir en felles og robust kanal for overfÃ¸ring av filer som ellers kunne krevd egne transportlÃ¸sninger.
- Reduserer behovet for tett koblede integrasjoner mellom avsender og mottaker.

### For integrasjonsmiljÃ¸er
- Gir standardiserte API-er og oppfÃ¸lgingsmekanismer for filbasert samhandling.
- GjÃ¸r det enklere Ã¥ bygge automatiserte leveranselÃ¸p med status og hendelser.

### For offentlig sektor
- Ã˜ker gjenbruk av Ã©n nasjonal formidlingstjeneste i stedet for mange lokale varianter.
- Styrker sporbarhet og kontroll i samhandlingslÃ¸p som involverer store eller viktige payloads.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Feil bruk av formidlingstjenesten kan gi overfÃ¸ring av innhold uten riktig hjemmel eller avtalegrunnlag | Tydelig ansvar hos tjenesteeier og klare tjenesteregler |
| Teknisk | Store payloads og asynkrone leveranser kan gi krevende feil- og gjenopptakssituasjoner | Robust klientimplementasjon, tydelig statusmodell og god overvÃ¥king |
| Sikkerhet | Feil tilgangsstyring kan gi uvedkommende tilgang til filer eller metadata | Streng tilgangskontroll, logging og revisjon |
| Forvaltning | Uklare grenser mot Events eller andre meldingsprodukter kan gi feil produktvalg | Tydelig produktavgrensning og god veiledning i dokumentasjonen |
| Brukeropplevelse | Asynkron flyt kan gjÃ¸re det vanskelig Ã¥ oppdage forsinkelser eller feil uten god oppfÃ¸lging | Varsling, hendelsesabonnementer og oversiktsflater for oppfÃ¸lging |

## Kanaler
- Produktside: https://docs.altinn.studio/nb/broker/
- Hva fÃ¥r du?: https://docs.altinn.studio/nb/broker/what-do-you-get/
- Kom i gang: https://docs.altinn.studio/nb/broker/getting-started/
- Referanse: https://docs.altinn.studio/nb/broker/reference/

## Plattform
Formidlingstjeneste i Altinn-portefÃ¸ljen med API-er, hendelsesabonnementer og kontrollert tilgang til filoverfÃ¸ringer.

**Fakta:** Dokumentasjonen beskriver stÃ¸tte for store payloads, logging, varsling, hendelsesabonnementer, API-tilgang og oversikt over eget forbruk. Dette viser at produktet er bÃ¥de integrasjonstjeneste og operativ formidlingstjeneste.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur og detaljert intern plattformimplementasjon.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet kan brukes av mange virksomheter som trenger samme grunnmÃ¸nster for sikker filoverfÃ¸ring.
- Det reduserer behovet for lokale spesiallÃ¸sninger for store og asynkrone leveranser.
- Gjenbruksverdien er sÃ¦rlig hÃ¸y nÃ¥r behovet er robust transport av payloads, ikke nÃ¥r behovet er hendelsesdeling eller sluttbrukerkommunikasjon.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** stÃ¸ttes ved at data kan deles gjennom en felles, kontrollert overfÃ¸ringsmekanisme.
- **P5: Del og gjenbruk lÃ¸sninger** realiseres ved at Ã©n formidlingstjeneste kan brukes av mange virksomheter.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** styrkes fordi produktet tilbyr et standardmÃ¸nster for asynkron samhandling.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** stÃ¸ttes gjennom tilgangskontroll, logging og sporbarhet.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Egen finansieringsmodell eller separat kostnadsnivÃ¥ for produktet isolert fra Altinn-portefÃ¸ljen.
- **Deduksjon:** Produktet mÃ¥ forstÃ¥s som del av Altinns samlede forvaltning og finansiering.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir / Altinn-forvaltningen | Offisiell produktdokumentasjon |
| Driftsansvar | Altinns forvaltnings- og driftsmiljÃ¸ | Produktet beskrives som del av Altinn-portefÃ¸ljen |
| Budsjettansvar | Del av Altinn-portefÃ¸ljen | Ingen separat offentlig kostnadsmodell verifisert |
| Styringsmodell | Produktforvaltning i Altinn | FremgÃ¥r av produktstruktur og dokumentasjon |

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
- Beskrivelsen er oppdatert mot dagens Altinn Broker-dokumentasjon og ikke bare eldre antakelser om Â«formidlingÂ».
- Uverifiserte pÃ¥stander om volum, intern teknologistack, SLA og kostnader er fjernet.
- Produktet er tydeligere avgrenset mot Events og andre Altinn-produkter.

### Tekstlige forbedringer
- Navn og hovedtekst er skrevet om til en tydeligere beskrivelse av styrt filoverfÃ¸ring som produkt.
- Hovedfunksjoner beskriver nÃ¥ bÃ¥de tjenesteflate og integrasjonsflate.
- SprÃ¥ket er gjort mer presist og mindre preget av teknisk oppramsing og spekulasjon.

