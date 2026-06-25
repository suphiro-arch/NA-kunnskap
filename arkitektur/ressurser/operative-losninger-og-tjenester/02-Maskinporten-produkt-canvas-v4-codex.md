# Produkt-canvas: Maskinporten

## Navn
Maskinporten

## Ressurs ID
DIGDIR-002

## Status/Livsfase
**Produksjon** - etablert nasjonal fellesløsning for maskin-til-maskin-autentisering og tilgang til API-er, med utvidelser for delegering, systembruker og samtykke i samspill med Altinn Autorisasjon.

**Fakta:** Digdir beskriver Maskinporten som fellesløsningen for virksomheters bruk av API-er og annen maskin-til-maskin-kommunikasjon. Overordnet dokumentasjon beskriver en enkel modell for API-sikring basert på OAuth2 og JWT-bearer grants. Dokumentasjonen for delegering, systembruker og samtykke viser at Maskinporten også inngår i mer avanserte tilgangsmønstre der Altinn Autorisasjon gir representasjon, delegering eller samtykkegrunnlag.

## Modenhet
**Høy modenhet** - innarbeidet felleskomponent med tydelige integrasjonsmønstre og dokumenterte utvidelser:
- Teknisk dokumentasjon beskriver standard tokenflyt, scopes, klientregistrering og selvbetjening.
- Dokumentasjonen beskriver også tre konkrete utvidelser i samspill med Altinn Autorisasjon: API-delegering, systembruker og samtykketoken.
- Det finnes etablerte løp for onboarding, test og produksjonssetting.
- Funksjonalitet for systembruker og samtykke er dokumentert som lansert i 2025.

**Deduksjon:** Modenheten er høy fordi Maskinporten både fungerer som grunnmønster for vanlig API-sikring og som et stabilt inngangspunkt for mer presise tilgangsmønstre når datadeling skjer på vegne av andre.

## Kort beskrivelse
Maskinporten er den nasjonale fellesløsningen for virksomhetsautentisering og tokenutstedelse når systemer skal bruke API-er på tvers av organisasjoner. I grunnmønsteret gir Maskinporten scope-basert tilgang mellom API-tilbyder og API-konsument. I mer avanserte scenarier brukes Maskinporten sammen med Altinn Autorisasjon for å håndtere tre ulike behov: videredelegering av en API-tilgang til en leverandør, finmasket systembruker-tilgang for et bestemt fagsystem, og samtykkebaserte token når tilgang til persondata krever samtykke.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** gjør det mulig for datakonsumenter å hente data fra andre virksomheter gjennom samme nasjonale tillitsmønster.
- **Datautveksling og integrasjon: Dele data med andre** gjør det mulig for datatilbydere å eksponere API-er på en standardisert og sikker måte for andre virksomheter.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter tokenutstedelse, klientautentisering og overføring av tilgangsgrunnlag i integrasjonsflyten.
- **Tillit: Autentisering** bekrefter identiteten til virksomheter og systemer som skal bruke API-er eller hente data maskinelt.
- **Tillit: Tilgangskontroll** gir grunnlag for å slippe inn bare systemer som har riktig token, scope og godkjent tilgang til den aktuelle ressursen.

## Produktmål
**Primærkilder:** Digdir Docs for Maskinporten, inkludert overordnet beskrivelse og funksjonssidene for delegering, systembruker og samtykke.

Dokumenterte mål:
- Gi virksomheter en felles løsning for sikker maskin-til-maskin-kommunikasjon.
- Gi API-tilbydere et felles mønster for å definere scopes og styre hvilke organisasjoner som kan bruke et API.
- Gjøre det mulig å utvide vanlig scope-tilgang med delegering, systembruker eller samtykke når tilgangsbehovet krever det.
- Legge til rette for trygg gjenbruk av API-er og data i offentlig sektor og i samspill med private aktører.

Operative mål utledet fra de samme kildene:
- Redusere behovet for lokale autentiserings- og tokenløsninger mellom hver enkelt tilbyder og konsument.
- Gjøre onboarding, test og produksjonssetting mer forutsigbar for nye integrasjoner.
- Skille tydelig mellom hva Maskinporten gjør alene og hva som krever samspill med Altinn Autorisasjon.
- Gi API-tilbydere et mønster for å velge riktig tilgangsform: direkte scope-tilgang, API-delegering, systembruker eller samtykke.

## Brukerbehov
- Datatilbydere trenger en felles måte å beskytte API-er og styre hvilke virksomheter og systemer som får tilgang.
- Datakonsumenter trenger et standardisert oppsett for å hente data fra andre virksomheter uten å forhandle fram særskilte tokenløsninger per API.
- Leverandører og sluttbrukersystemer trenger et mønster for å opptre på vegne av kundene sine uten å få videre rettigheter enn nødvendig.
- API-tilbydere trenger tydelig støtte for å skille mellom grovkornet scope-tilgang og mer finmasket autorisasjon i Altinn.
- Tjenesteeiere som håndterer persondata trenger et mønster der samtykke kan kontrolleres og transporteres i tokenet.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Datatilbydere i offentlig sektor | Beskytte API-er og styre tilgang | Eksponering av data og tjenester til andre virksomheter | Trenger et felles sikkerhetsmønster og tydelig avgrensning mot autorisasjon |
| Datakonsumenter i offentlig og privat sektor | Hente data sikkert fra andre | Integrasjon mot offentlige API-er | Møter Maskinporten som standard inngang til API-bruk |
| Leverandører og sluttbrukersystemer | Opptre på vegne av kunder på en kontrollert måte | Kunde-leverandør-scenarier og automatiserte prosesser | Er særlig relevante i delegering og systembruker-scenarier |
| Integrasjonsteam og systemleverandører | Standardiserte grensesnitt og testløp | Utvikling av API-klienter og integrasjoner | Er avhengige av tydelige scopes, claims og dokumentasjon |
| Sikkerhets- og forvaltningsmiljøer | Kontroll og sporbarhet | Risikooppfølging, avtaler og tilgangsstyring | Må forstå samspillet mellom Maskinporten og Altinn Autorisasjon |

## Hovedfunksjoner
### Primære funksjoner
- **Utstedelse av token for vanlig maskin-til-maskin-bruk.** Maskinporten utsteder access tokens basert på registrert klient og tildelte scopes. Dette er grunnmønsteret for at en API-konsument skal identifisere seg overfor en API-tilbyder og dokumentere hvilken tilgang som er tildelt.
- **Scope-basert tilgang til API-er.** API-tilbyder modellerer tilgang som scopes og gir disse til bestemte organisasjoner. Dette gir en enkel og grovkornet modell for tilgang mellom virksomheter, og er riktig når lovhjemmel eller avtalegrunnlag allerede er avklart og det ikke trengs ytterligere representasjons- eller samtykkelogikk.
- **API-delegering via Altinn Autorisasjon.** Når en API-konsument skal la en leverandør hente data på sine vegne, kan API-tilbyder registrere scopet med `delegation_source`, opprette delegeringsoppsett i Altinn og fortsatt gi selve API-tilgangen til konsumenten, ikke til leverandøren. Konsumenten delegerer deretter API-tilgangen videre i Altinn, og leverandøren henter Maskinporten-token med `consumer_org`-claim for å opptre på vegne av kunden. Dette passer når leverandøren trenger samme API-tilgang som kunden, men uten at API-tilbyder skal administrere leverandørforholdet direkte.
- **Systembruker for finmasket maskinell tilgang.** Når vanlig API-delegering ville gitt for brede rettigheter, kan leverandøren registrere et bestemt fagsystem i Altinn og knytte det til én Maskinporten-klient. Kunden delegerer da konkrete Altinn-rettigheter til en systembruker, ikke hele API-tilgangen til leverandørens organisasjonsnummer. Tokenet fra Maskinporten inneholder systembrukeropplysninger, og API-tilbyder må både validere scope og spørre Altinn Autorisasjon sitt PDP-endepunkt for å avgjøre hva systemet faktisk har lov til å gjøre.
- **Samtykketoken i samspill med Altinn.** Når tilgang til data krever samtykke, kan datakonsumenten be om et Maskinporten-token som inneholder en bestemt samtykkeressurs og hvem som har gitt samtykket. Maskinporten spør Altinn om samtykket finnes og returnerer token med samtykkedetaljer som API-tilbyder må validere. Dette passer når rettsgrunnlaget er samtykke, ikke bare virksomhet-til-virksomhet-tilgang.
- **Selvbetjening og standardisert innføring.** Både tilbydere og konsumenter bruker selvbetjening for scope-oppsett, klientregistrering og innføring. Det gjør løsningen organisatorisk gjenbrukbar, ikke bare teknisk.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Klientautentisering og tokenutstedelse for API-bruk | Innlogging for sluttbrukere |
| Scope-basert tilgang mellom virksomheter | Faglig autorisasjon inne i den enkelte tjenesten |
| Støtte for API-delegering, systembruker og samtykketoken | Full erstatning for Altinn Autorisasjon som policy- og rettighetsmotor |
| Standardiserte integrasjonsmønstre for API-er | Selve API-ene eller datamodellene som tilbys |
| Onboarding, test og produksjonsløp | Dokumentsignering eller meldingsformidling som eget produktområde |

### Typiske brukssituasjoner
- En virksomhet skal bruke et offentlig API og trenger vanlig scope-basert tilgang uten sluttbruker i løkka.
- En datatilbyder skal gi en kunde tilgang til et API, men kunden vil at en ekstern leverandør skal hente data på sine vegne. Da brukes API-delegering mellom Maskinporten og Altinn.
- En leverandør leverer et fagsystem som bare skal få et avgrenset sett med rettigheter hos kunden. Da brukes systembruker i stedet for bred API-delegering.
- En tjeneste skal dele persondata eller andre data der sluttbrukers samtykke er nødvendig. Da brukes samtykketoken med samtykkeressurs fra Altinn.

### Når Maskinporten normalt ikke er førstevalg
- Når behovet er innlogging for sluttbrukere - da er ID-porten mer relevant.
- Når behovet primært er policybasert representasjon, delegering og tilgangsbeslutning uten at det samtidig brukes et Maskinporten-beskyttet API - da er Altinn Autorisasjon den viktigste byggesteinen.
- Når behovet er meldingsformidling mellom systemer - da er eFormidling eller Altinn Melding mer relevant.
- Når tjenesten trenger detaljert faglig autorisasjon, men ikke et nasjonalt mønster for virksomhetsautentisering og tokenutstedelse - da er Maskinporten alene for lite.

## Veikart over kommende funksjonalitet
**Fakta fra Digdir Docs (kontrollert 2026-06-25):**
- Systembruker og samtykke er dokumentert som lansert i 2025.
- Dokumentasjonen viser at Digdir videreutvikler Maskinporten som del av en bredere tillitsinfrastruktur sammen med Altinn.

**Deduksjon:** Veikartet peker ikke bare mot mer av det samme, men mot tydeligere standardisering av avanserte tilgangsmønstre der Maskinporten brukes som tokenlag og Altinn som kilde til delegasjon, rettigheter eller samtykke.

## Forretningsverdi/Verdiforslag
### For datatilbydere
- Reduserer behovet for å bygge og forvalte egne autentiseringsløsninger for API-er.
- Gir et tydeligere beslutningsgrunnlag for når vanlig scope-tilgang er nok, og når tjenesten bør kreve delegering, systembruker eller samtykke.
- Gjør det enklere å beskytte API-er for mange konsumenter uten å etablere unike oppsett per mottaker.

### For datakonsumenter og leverandører
- Gir et gjenkjennelig mønster for å bruke data fra mange virksomheter.
- Gjør det mulig å bygge leverandørintegrasjoner som kan opptre på vegne av kunder uten at kunden må etablere egne lokale sikkerhetsmønstre.
- Gir en tydelig vei til samtykkebasert API-bruk når datadeling krever det.

### For offentlig sektor og økosystemet
- Standardiserer hvordan virksomheter og systemer får tilgang til API-er.
- Gjør samspillet mellom autentisering, delegering og samtykke mer forutsigbart på tvers av tjenester.
- Reduserer behovet for proprietære sikkerhetsløsninger i hvert enkelt API-økosystem.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk og styringsmessig | Virksomheter kan bruke vanlig scope-tilgang der samtykke eller mer presis representasjon egentlig er nødvendig | Vurdere rettsgrunnlag tidlig og velge riktig mønster: direkte tilgang, delegering, systembruker eller samtykke |
| Teknisk | API-tilbyder kan implementere tokenvalidering riktig, men likevel glemme å validere `consumer_org`, systembrukeropplysninger eller samtykkeclaims | Lage eksplisitte integrasjonskrav per scenario og teste dem i hele kjeden |
| Sikkerhet | For brede scopes eller feil valg mellom API-delegering og systembruker kan gi leverandører mer tilgang enn de trenger | Bruke minste privilegium, tydelige scopes og systembruker der bred delegering blir for grovkornet |
| Avhengigheter | Svak forståelse av samspillet mellom Maskinporten og Altinn Autorisasjon kan gi feil løsningsvalg | Beskrive samspillet tydelig i onboarding, arkitektur og utviklerguider |
| Brukbarhet | Nye integrasjonsteam kan oppleve avanserte scenarier som komplekse fordi de krever både Maskinporten- og Altinn-oppsett | Bedre eksempler, scenariobaserte guider og tydeligere valgmatrise |

## Kanaler
- Produktside: https://www.digdir.no/om-tjenesten/maskinporten/1558
- Teknisk dokumentasjon: https://docs.digdir.no/docs/Maskinporten/
- Overordnet dokumentasjon: https://docs.digdir.no/docs/Maskinporten/maskinporten_overordnet
- API-delegering: https://docs.digdir.no/docs/Maskinporten/maskinporten_func_delegering.html
- Systembruker: https://docs.digdir.no/docs/Maskinporten/maskinporten_func_systembruker.html
- Samtykketoken: https://docs.digdir.no/docs/Maskinporten/maskinporten_func_samtykke.html
- Samarbeidsportal: https://samarbeid.digdir.no/maskinporten/dette-er-maskinporten/96
- Ta i bruk: https://samarbeid.digdir.no/maskinporten/ta-i-bruk-maskinporten/97

## Plattform
Maskinporten er en nasjonal plattform for klientautentisering og tokenutstedelse i maskinelle integrasjoner.

**Fakta:** Digdir Docs beskriver grunnmønsteret som OAuth2-basert API-sikring med JWT-bearer grants og scopes. Dokumentasjonen for systembruker og samtykke viser i tillegg bruk av OAuth2-utvidelsen Rich Authorization Requests, med egne typer for `urn:altinn:systemuser` og `urn:altinn:consent`.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur, konkret skylokasjon og detaljert runtime-oppsett.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er laget for gjenbruk i mange integrasjoner på tvers av virksomheter.
- Gjenbruksverdien er størst når behovet er sikker maskinell tilgang til API-er med et felles nasjonalt tokenmønster.
- Verdien øker ytterligere når datatilbyder vil kombinere samme grunnmønster med delegering, systembruker eller samtykke i stedet for å etablere egne spesialløsninger.
- Produktet er mindre relevant dersom behovet egentlig er sluttbrukerinnlogging eller ren policyforvaltning uten Maskinporten-beskyttet API.

### Vanlige kombinasjoner med andre produkter
- **Altinn Autorisasjon** - brukes sammen med Maskinporten i tre ulike mønstre: API-delegering til leverandør, systembruker for finmasket maskinell autorisasjon og samtykke som grunnlag for token.
- **data.altinn.no** - bruker Maskinporten som autentiseringsmekanisme for kontrollert datadeling, og kan i enkelte tilfeller også være avhengig av Altinn-samtykke eller annen autorisasjonslogikk.
- **Altinn Events** - abonnementer på hendelsesstrømmer autentiseres typisk med Maskinporten.
- **Folkeregisteret, Enhetsregisteret, Skatteetatens delingstjenester** - disse API-ene er ofte beskyttet av Maskinporten, og integrasjon mot dem forutsetter at Maskinporten er på plass.

**Kildekode:** Ikke offentlig dokumentert i brukte kilder.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger** realiseres ved at autentisering for API-bruk tilbys som felleskomponent.
- **P6: Lag digitale løsninger som støtter samhandling** styrkes fordi flere virksomheter kan bygge på samme sikkerhetsmønster og samme utvidelser for delegering og samtykke.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi produktet etablerer grunnlaget for sikker maskinell tilgang og kontrollert informasjonsflyt.

## Finansiering
- **Fakta:** Samarbeidsportalen har en egen side for kostnadsmodell for Maskinporten.
- **Ikke fullt offentlig dokumentert i brukte kilder:** Detaljerte satser og full kostnadsfordeling.
- **Deduksjon:** Produktet forvaltes som nasjonal fellesløsning, men virksomheter må forholde seg til en dokumentert modell for bruk og innføring.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Digdirs produktside og Digdir Docs |
| Driftsansvar | Ikke eksplisitt navngitt i brukte offentlige kilder | Offentlige kilder beskriver ikke detaljert leverandør- eller driftsmodell |
| Budsjett- og kostnadsmodell | Digdir forvalter produktet, med publisert kostnadsmodell | Samarbeidsportalen |
| Styringsmodell | Del av Digdirs tillitstjenester og brukes i samspill med Altinn Autorisasjon | Digdir Docs og Samarbeidsportalen |

## Lenke til dokumentasjon
- https://www.digdir.no/om-tjenesten/maskinporten/1558
- https://docs.digdir.no/docs/Maskinporten/
- https://docs.digdir.no/docs/Maskinporten/maskinporten_overordnet
- https://docs.digdir.no/docs/Maskinporten/maskinporten_func_delegering.html
- https://docs.digdir.no/docs/Maskinporten/maskinporten_func_systembruker.html
- https://docs.digdir.no/docs/Maskinporten/maskinporten_func_samtykke.html
- https://samarbeid.digdir.no/maskinporten/dette-er-maskinporten/96
- https://samarbeid.digdir.no/maskinporten/ta-i-bruk-maskinporten/97
- https://samarbeid.digdir.no/maskinporten/kostnadsmodell-maskinporten/64

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/02-Maskinporten-produkt-canvas-v3-codex.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/04-Altinn-autorisasjon-produkt-canvas-v4-codex.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.digdir.no/om-tjenesten/maskinporten/1558 (kontrollert 2026-06-25)
- Nettkilde: https://docs.digdir.no/docs/Maskinporten/ (kontrollert 2026-06-25)
- Nettkilde: https://docs.digdir.no/docs/Maskinporten/maskinporten_overordnet (kontrollert 2026-06-25)
- Nettkilde: https://docs.digdir.no/docs/Maskinporten/maskinporten_func_delegering.html (kontrollert 2026-06-25)
- Nettkilde: https://docs.digdir.no/docs/Maskinporten/maskinporten_func_systembruker.html (kontrollert 2026-06-25)
- Nettkilde: https://docs.digdir.no/docs/Maskinporten/maskinporten_func_samtykke.html (kontrollert 2026-06-25)
- Nettkilde: https://samarbeid.digdir.no/maskinporten/dette-er-maskinporten/96 (kontrollert 2026-06-25)
- Nettkilde: https://samarbeid.digdir.no/maskinporten/ta-i-bruk-maskinporten/97 (kontrollert 2026-06-25)
- Nettkilde: https://samarbeid.digdir.no/maskinporten/kostnadsmodell-maskinporten/64 (kontrollert 2026-06-25)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen skiller nå tydelig mellom vanlig scope-basert Maskinporten-bruk og tre mer avanserte scenarier i samspill med Altinn Autorisasjon: API-delegering, systembruker og samtykke.
- Hovedfunksjonene er gjort mer konkrete rundt claims, oppsett og valideringsansvar hos API-tilbyder, slik at teksten kan brukes bedre som analysegrunnlag.
- Risiko- og avgrensningsdelene er spisset mot feilvalg mellom direkte tilgang, delegering, systembruker og samtykke.

### Tekstlige forbedringer
- Kortbeskrivelsen og brukssituasjonene er strammet inn for å unngå generiske formuleringer om "sikker datadeling" uten å si hva Maskinporten faktisk gjør.
- Kombinasjonen med Altinn Autorisasjon er skrevet som konkrete mønstre i stedet for løse henvisninger.
- Kildelisten er utvidet med de tre funksjonssidene som dokumenterer de mest spesifikke bruksscenariene.
