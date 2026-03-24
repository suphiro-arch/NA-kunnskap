# Produkt-canvas: Maskinporten

## Navn
Maskinporten

## Ressurs ID
DIGDIR-002

## Status/Livsfase
**Produksjon** - etablert nasjonal fellesløsning for sikker maskin-til-maskin-autentisering og tilgang til API-er.

**Fakta:** Digdir beskriver Maskinporten som fellesløsningen for virksomheters bruk av API-er og annen maskin-til-maskin-kommunikasjon. Dokumentasjonen og Samarbeidsportalen beskriver et etablert løp for å ta løsningen i bruk, og løsningen inngår i Digdirs tillitstjenester.

## Modenhet
**Høy modenhet** - innarbeidet felleskomponent med tydelige integrasjonsmønstre og bred praktisk bruk:
- Teknisk dokumentasjon beskriver anbefalte flyter, scopes, tokenbruk og systembruker-scenarier.
- Samarbeidsportalen beskriver tjenesten som en etablert del av Digdirs felles tillitsinfrastruktur.
- Det finnes dokumenterte løp for onboarding, test og produksjonssetting.
- Produktet er modent både som teknisk komponent og som forvaltningsmodell.

**Deduksjon:** Modenheten er høy fordi produktet brukes som grunnlag for sikker datadeling på tvers av virksomheter, og fordi mønstrene er standardiserte nok til å være gjenbrukbare på tvers av sektorer.

## Kort beskrivelse
Maskinporten er den nasjonale fellesløsningen for å autentisere systemer og styre tilgang når virksomheter utveksler data eller bruker hverandres API-er. Produktet gjør det mulig å bygge sikre integrasjoner uten at hver datatilbyder og datakonsument må etablere egne autentiserings- og tokenløsninger. Maskinporten er særlig relevant når behovet er kontrollert maskin-til-maskin-kommunikasjon mellom virksomheter, ikke innlogging for sluttbrukere.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** gjør det mulig for datakonsumenter å hente data fra andre virksomheter gjennom samme nasjonale tillitsmønster.
- **Datautveksling og integrasjon: Dele data med andre** gjør det mulig for datatilbydere å eksponere API-er på en standardisert og sikker måte for andre virksomheter.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter tokenutstedelse, klientautentisering og overføring av tilgangsgrunnlag i integrasjonsflyten.
- **Tillit: Autentisering** bekrefter identiteten til virksomheter og systemer som skal bruke API-er eller hente data maskinelt.
- **Tillit: Tilgangskontroll** gir grunnlag for å slippe inn bare systemer som har riktig token, scope og godkjent tilgang til den aktuelle ressursen.

## Produktmål
**Primærkilder:** Digdir Docs for Maskinporten og Samarbeidsportalen for produktområdet.

Dokumenterte mål:
- Gi virksomheter en felles løsning for sikker maskin-til-maskin-kommunikasjon.
- Forenkle bruk av API-er og datadeling på tvers av virksomheter.
- Redusere behovet for lokale og bilaterale autentiseringsløsninger.
- Legge til rette for trygg gjenbruk av API-er og data i offentlig sektor og i samspill med private aktører.

Operative mål utledet fra de samme kildene:
- Gi datatilbydere et felles mønster for å beskytte API-er.
- Gi datakonsumenter et gjenkjennelig og dokumentert tokenregime.
- Gjøre onboarding, test og produksjonssetting mer forutsigbar for nye integrasjoner.

## Brukerbehov
- Datatilbydere trenger en felles måte å beskytte API-er og kontrollere hvilke systemer som får tilgang.
- Datakonsumenter trenger et standardisert oppsett for å hente data fra andre virksomheter.
- Integrasjonsteam trenger tydelige protokoller, scopes og dokumentasjon for å bygge robuste API-kall.
- Sikkerhets- og forvaltningsmiljøer trenger en løsning som gjør tilgang til maskinell datautveksling sporbar og styrbar.
- Virksomheter som opptrer på vegne av andre trenger et mønster som kan kombineres med fullmakter og systembruker der dette er relevant.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Datatilbydere i offentlig sektor | Beskytte API-er og styre tilgang | Eksponering av data og tjenester til andre virksomheter | Trenger et felles sikkerhetsmønster i stedet for lokale særvarianter |
| Datakonsumenter i offentlig og privat sektor | Hente data sikkert fra andre | Integrasjon mot offentlige API-er | Møter Maskinporten som del av integrasjonsløpet |
| Integrasjonsteam og systemleverandører | Standardiserte grensesnitt og testløp | Utvikling av API-klienter og integrasjoner | Er avhengige av tydelige scopes, tokenflyt og dokumentasjon |
| Sikkerhets- og forvaltningsmiljøer | Kontroll og sporbarhet | Risikooppfølging, avtaler og tilgangsstyring | Trenger forutsigbare mønstre og tydelig ansvarsdeling |
| Virksomheter med systembrukerbehov | Maskinell bruk på vegne av virksomhet | Automatiserte prosesser og delegerte integrasjoner | Relevante der systemer skal opptre i en virksomhetskontekst |

## Hovedfunksjoner
### Primære funksjoner
- **Utstedelse av tilgangstoken for maskin-til-maskin-bruk.** Maskinporten utsteder token som systemer bruker for å identifisere seg overfor API-er. Dette dekker behovet for en felles og sikker mekanisme for å bekrefte hvem som kaller et API, og hva klienten ber om tilgang til.
- **Standardisert autentisering av systemer og virksomheter.** Produktet gir et nasjonalt mønster for klientautentisering basert på virksomhetsforankrede oppsett og dokumenterte protokoller. Dette gjør at datatilbydere og datakonsumenter kan samhandle uten å etablere egne proprietære autentiseringsordninger.
- **Scope-basert tilgang til API-er.** Maskinporten gjør det mulig å styre tilgang på et konseptnivå gjennom scopes som beskriver hvilke API-er eller datatyper en klient skal kunne bruke. Det er relevant når en virksomhet trenger kontrollert og differensiert tilgang, men ikke når behovet egentlig er detaljert faglig autorisasjon inne i mottakersystemet.
- **Støtte for systembruker og virksomhetskontekst.** Dokumentasjonen beskriver hvordan løsningen kan brukes i scenarier der systemer opptrer på vegne av en virksomhet. Dette er viktig i automatiserte prosesser, men det erstatter ikke egne løsninger for fullmakt og representasjon der den juridiske og faglige konteksten er mer kompleks.
- **Kontrollert innføring og forvaltning.** Tjenesten tilbyr dokumentasjon, onboarding og etablerte bruksløp som gjør produktet gjenbrukbart organisatorisk, ikke bare teknisk. Det er en sentral del av verdien når mange aktører skal koble seg på samme tillitsinfrastruktur.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Maskin-til-maskin-autentisering for API-bruk | Innlogging for sluttbrukere |
| Tokenutstedelse og scope-basert tilgangsgrunnlag | Faglig autorisasjon i den enkelte tjeneste |
| Standardiserte integrasjonsmønstre for API-er | Selve API-ene eller datamodellene som tilbys |
| Støtte for systembruker-scenarier | Dokument- eller transaksjonssignering |
| Onboarding, test og produksjonsløp | Full erstatning for fullmakts- og representasjonsløsninger |

## Veikart over kommende funksjonalitet
**Fakta fra Samarbeidsportalen og Digdir Docs (hentet 2026-03-17):**
- Produktområdet arbeider videre med forenklet bruk, tydeligere innføringsløp og videreutvikling av tillitstjenestene som helhet.
- Dokumentasjonen viser også at systembruker og mer avanserte integrasjonsscenarier er et tydelig utviklingsområde.

**Deduksjon:** Veikartet peker mot videre modning av Maskinporten som felles grunnmur for API-sikkerhet, særlig der virksomheter trenger mer standardisert samspill mellom autentisering, tilgang og delegerte integrasjoner.

## Forretningsverdi/Verdiforslag
### For datatilbydere
- Reduserer behovet for å bygge og forvalte egne autentiseringsløsninger for API-er.
- Senker risiko ved at tilgang til API-er bygger på et etablert nasjonalt sikkerhetsmønster.
- Gjør det enklere å eksponere data til flere aktører uten å etablere unike oppsett per mottaker.

### For datakonsumenter
- Gir et gjenkjennelig mønster for å bruke data fra mange virksomheter.
- Reduserer integrasjonskostnader ved at samme token- og autentiseringslogikk kan gjenbrukes.
- Gjør det lettere å etablere nye samarbeid og automatiserte prosesser.

### For offentlig sektor og økosystemet
- Styrker nasjonal datadeling ved å standardisere hvordan systemer får tilgang til API-er.
- Bidrar til raskere gjenbruk av data og tjenester på tvers av sektorer.
- Gjør det enklere å skille mellom når behovet er maskinell autentisering, og når andre produkter må brukes for innlogging, autorisasjon eller fullmakt.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk og styringsmessig | Virksomheter kan gi tilgang til API-er uten tydelig hjemmel eller feil avgrensede scopes | Tydeligere tilgangsmodeller, avtaler og gjennomgang av scope-bruk |
| Teknisk | Feil integrasjon hos klient eller API-tilbyder kan gi utilgjengelige eller usikre API-kall | Testmiljø, dokumenterte mønstre og validering før produksjon |
| Sikkerhet | Kompromitterte klienthemmeligheter eller feil tokenhåndtering kan gi uautorisert tilgang | Streng nøkkelhåndtering, overvåking og begrensede levetider på token |
| Avhengigheter | Feil forståelse av samspillet mellom Maskinporten og andre tillitstjenester kan gi feil løsningsvalg | Tydelig avgrensning mellom autentisering, autorisasjon og representasjon |
| Brukbarhet | Onboarding kan oppleves som krevende for nye integrasjonsteam | Bedre innføringsstøtte, eksempler og forenklede startløp |

## Kanaler
- Produktside: https://www.digdir.no/om-tjenesten/maskinporten/1558
- Teknisk dokumentasjon: https://docs.digdir.no/docs/Maskinporten/
- Overordnet dokumentasjon: https://docs.digdir.no/docs/Maskinporten/maskinporten_overordnet
- Samarbeidsportal: https://samarbeid.digdir.no/maskinporten/dette-er-maskinporten/96
- Ta i bruk: https://samarbeid.digdir.no/maskinporten/ta-i-bruk-maskinporten/97

## Plattform
Maskinporten er en nasjonal plattform for klientautentisering og tokenutstedelse i maskinelle integrasjoner.

**Fakta:** Digdir Docs beskriver løsningen gjennom standardiserte protokoller, tokenflyter og bruk av scopes. Dokumentasjonen beskriver også systembruker som et eget funksjonelt område.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur, konkret skylokasjon og detaljert runtime-oppsett.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er laget for gjenbruk i mange integrasjoner på tvers av virksomheter.
- Det er særlig relevant når behovet er sikker maskinell tilgang til API-er.
- Det er mindre relevant dersom behovet egentlig er sluttbrukerinnlogging eller detaljert faglig autorisasjon, der andre produkter treffer bedre.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger** realiseres ved at autentisering for API-bruk tilbys som felleskomponent.
- **P6: Lag digitale løsninger som støtter samhandling** styrkes fordi flere virksomheter kan bygge på samme sikkerhetsmønster for datautveksling.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi produktet etablerer grunnlaget for sikker maskinell tilgang og kontrollert informasjonsflyt.

## Finansiering
- **Fakta:** Samarbeidsportalen har en egen side for kostnadsmodell for Maskinporten.
- **Ikke fullt offentlig dokumentert i brukte kilder:** Detaljerte satser og full kostnadsfordeling.
- **Deduksjon:** Produktet forvaltes som nasjonal fellesløsning, men virksomheter må forholde seg til en dokumentert modell for bruk og innføring.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Digdirs produktside og Samarbeidsportalen |
| Driftsansvar | Ikke eksplisitt navngitt i brukte offentlige kilder | Offentlige kilder beskriver ikke detaljert leverandør- eller driftsmodell |
| Budsjett- og kostnadsmodell | Digdir forvalter produktet, med publisert kostnadsmodell | Samarbeidsportalen |
| Styringsmodell | Del av Digdirs tillitstjenester | Samarbeidsportalen |

## Lenke til dokumentasjon
- https://www.digdir.no/om-tjenesten/maskinporten/1558
- https://docs.digdir.no/docs/Maskinporten/
- https://docs.digdir.no/docs/Maskinporten/maskinporten_overordnet
- https://docs.digdir.no/docs/Maskinporten/maskinporten_func_systembruker.html
- https://samarbeid.digdir.no/maskinporten/dette-er-maskinporten/96
- https://samarbeid.digdir.no/maskinporten/ta-i-bruk-maskinporten/97
- https://samarbeid.digdir.no/maskinporten/kostnadsmodell-maskinporten/64

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/produkter/produktbeskrivelser/02-Maskinporten-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.digdir.no/om-tjenesten/maskinporten/1558 (hentet 2026-03-17)
- Nettkilde: https://docs.digdir.no/docs/Maskinporten/ (hentet 2026-03-17)
- Nettkilde: https://docs.digdir.no/docs/Maskinporten/maskinporten_overordnet (hentet 2026-03-17)
- Nettkilde: https://docs.digdir.no/docs/Maskinporten/maskinporten_func_systembruker.html (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/maskinporten/dette-er-maskinporten/96 (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/maskinporten/ta-i-bruk-maskinporten/97 (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/maskinporten/kostnadsmodell-maskinporten/64 (hentet 2026-03-17)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Kapabilitetslisten er redusert til de direkte funksjonene Maskinporten faktisk realiserer, og indirekte koblinger til andre tillitstjenester er tatt ut.
- Funksjonsbeskrivelsen er strammet inn rundt maskin-til-maskin-autentisering, scopes og systembruker i stedet for bredere antakelser om fullmakt og sporbarhet.
- Finansiering og forvaltning er skrevet om slik at publiserte forhold skilles fra det som ikke er offentlig dokumentert.

### Tekstlige forbedringer
- Metadata er ryddet slik at dokumentet ikke starter med målgruppelinje, og `Ressurs ID` er skrevet uten parentesforklaring.
- Hovedfunksjoner og avgrensning er skrevet som en tydeligere veiledning for når Maskinporten er riktig løsning.
- Verdibeskrivelse og gjenbruksvurdering skiller klarere mellom Maskinporten og tilgrensende produkter.
