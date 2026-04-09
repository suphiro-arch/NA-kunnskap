# Produkt-canvas: Maskinporten

## Navn
Maskinporten

## Ressurs ID
DIGDIR-002

## Status/Livsfase
**Produksjon** - etablert nasjonal felleslÃ¸sning for sikker maskin-til-maskin-autentisering og tilgang til API-er.

**Fakta:** Digdir beskriver Maskinporten som felleslÃ¸sningen for virksomheters bruk av API-er og annen maskin-til-maskin-kommunikasjon. Dokumentasjonen og Samarbeidsportalen beskriver et etablert lÃ¸p for Ã¥ ta lÃ¸sningen i bruk, og lÃ¸sningen inngÃ¥r i Digdirs tillitstjenester.

## Modenhet
**HÃ¸y modenhet** - innarbeidet felleskomponent med tydelige integrasjonsmÃ¸nstre og bred praktisk bruk:
- Teknisk dokumentasjon beskriver anbefalte flyter, scopes, tokenbruk og systembruker-scenarier.
- Samarbeidsportalen beskriver tjenesten som en etablert del av Digdirs felles tillitsinfrastruktur.
- Det finnes dokumenterte lÃ¸p for onboarding, test og produksjonssetting.
- Produktet er modent bÃ¥de som teknisk komponent og som forvaltningsmodell.

**Deduksjon:** Modenheten er hÃ¸y fordi produktet brukes som grunnlag for sikker datadeling pÃ¥ tvers av virksomheter, og fordi mÃ¸nstrene er standardiserte nok til Ã¥ vÃ¦re gjenbrukbare pÃ¥ tvers av sektorer.

## Kort beskrivelse
Maskinporten er den nasjonale felleslÃ¸sningen for Ã¥ autentisere systemer og styre tilgang nÃ¥r virksomheter utveksler data eller bruker hverandres API-er. Produktet gjÃ¸r det mulig Ã¥ bygge sikre integrasjoner uten at hver datatilbyder og datakonsument mÃ¥ etablere egne autentiserings- og tokenlÃ¸sninger. Maskinporten er sÃ¦rlig relevant nÃ¥r behovet er kontrollert maskin-til-maskin-kommunikasjon mellom virksomheter, ikke innlogging for sluttbrukere.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** gjÃ¸r det mulig for datakonsumenter Ã¥ hente data fra andre virksomheter gjennom samme nasjonale tillitsmÃ¸nster.
- **Datautveksling og integrasjon: Dele data med andre** gjÃ¸r det mulig for datatilbydere Ã¥ eksponere API-er pÃ¥ en standardisert og sikker mÃ¥te for andre virksomheter.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter tokenutstedelse, klientautentisering og overfÃ¸ring av tilgangsgrunnlag i integrasjonsflyten.
- **Tillit: Autentisering** bekrefter identiteten til virksomheter og systemer som skal bruke API-er eller hente data maskinelt.
- **Tillit: Tilgangskontroll** gir grunnlag for Ã¥ slippe inn bare systemer som har riktig token, scope og godkjent tilgang til den aktuelle ressursen.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Digdir Docs for Maskinporten og Samarbeidsportalen for produktomrÃ¥det.

Dokumenterte mÃ¥l:
- Gi virksomheter en felles lÃ¸sning for sikker maskin-til-maskin-kommunikasjon.
- Forenkle bruk av API-er og datadeling pÃ¥ tvers av virksomheter.
- Redusere behovet for lokale og bilaterale autentiseringslÃ¸sninger.
- Legge til rette for trygg gjenbruk av API-er og data i offentlig sektor og i samspill med private aktÃ¸rer.

Operative mÃ¥l utledet fra de samme kildene:
- Gi datatilbydere et felles mÃ¸nster for Ã¥ beskytte API-er.
- Gi datakonsumenter et gjenkjennelig og dokumentert tokenregime.
- GjÃ¸re onboarding, test og produksjonssetting mer forutsigbar for nye integrasjoner.

## Brukerbehov
- Datatilbydere trenger en felles mÃ¥te Ã¥ beskytte API-er og kontrollere hvilke systemer som fÃ¥r tilgang.
- Datakonsumenter trenger et standardisert oppsett for Ã¥ hente data fra andre virksomheter.
- Integrasjonsteam trenger tydelige protokoller, scopes og dokumentasjon for Ã¥ bygge robuste API-kall.
- Sikkerhets- og forvaltningsmiljÃ¸er trenger en lÃ¸sning som gjÃ¸r tilgang til maskinell datautveksling sporbar og styrbar.
- Virksomheter som opptrer pÃ¥ vegne av andre trenger et mÃ¸nster som kan kombineres med fullmakter og systembruker der dette er relevant.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Datatilbydere i offentlig sektor | Beskytte API-er og styre tilgang | Eksponering av data og tjenester til andre virksomheter | Trenger et felles sikkerhetsmÃ¸nster i stedet for lokale sÃ¦rvarianter |
| Datakonsumenter i offentlig og privat sektor | Hente data sikkert fra andre | Integrasjon mot offentlige API-er | MÃ¸ter Maskinporten som del av integrasjonslÃ¸pet |
| Integrasjonsteam og systemleverandÃ¸rer | Standardiserte grensesnitt og testlÃ¸p | Utvikling av API-klienter og integrasjoner | Er avhengige av tydelige scopes, tokenflyt og dokumentasjon |
| Sikkerhets- og forvaltningsmiljÃ¸er | Kontroll og sporbarhet | RisikooppfÃ¸lging, avtaler og tilgangsstyring | Trenger forutsigbare mÃ¸nstre og tydelig ansvarsdeling |
| Virksomheter med systembrukerbehov | Maskinell bruk pÃ¥ vegne av virksomhet | Automatiserte prosesser og delegerte integrasjoner | Relevante der systemer skal opptre i en virksomhetskontekst |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- **Utstedelse av tilgangstoken for maskin-til-maskin-bruk.** Maskinporten utsteder token som systemer bruker for Ã¥ identifisere seg overfor API-er. Dette dekker behovet for en felles og sikker mekanisme for Ã¥ bekrefte hvem som kaller et API, og hva klienten ber om tilgang til.
- **Standardisert autentisering av systemer og virksomheter.** Produktet gir et nasjonalt mÃ¸nster for klientautentisering basert pÃ¥ virksomhetsforankrede oppsett og dokumenterte protokoller. Dette gjÃ¸r at datatilbydere og datakonsumenter kan samhandle uten Ã¥ etablere egne proprietÃ¦re autentiseringsordninger.
- **Scope-basert tilgang til API-er.** Maskinporten gjÃ¸r det mulig Ã¥ styre tilgang pÃ¥ et konseptnivÃ¥ gjennom scopes som beskriver hvilke API-er eller datatyper en klient skal kunne bruke. Det er relevant nÃ¥r en virksomhet trenger kontrollert og differensiert tilgang, men ikke nÃ¥r behovet egentlig er detaljert faglig autorisasjon inne i mottakersystemet.
- **StÃ¸tte for systembruker og virksomhetskontekst.** Dokumentasjonen beskriver hvordan lÃ¸sningen kan brukes i scenarier der systemer opptrer pÃ¥ vegne av en virksomhet. Dette er viktig i automatiserte prosesser, men det erstatter ikke egne lÃ¸sninger for fullmakt og representasjon der den juridiske og faglige konteksten er mer kompleks.
- **Kontrollert innfÃ¸ring og forvaltning.** Tjenesten tilbyr dokumentasjon, onboarding og etablerte brukslÃ¸p som gjÃ¸r produktet gjenbrukbart organisatorisk, ikke bare teknisk. Det er en sentral del av verdien nÃ¥r mange aktÃ¸rer skal koble seg pÃ¥ samme tillitsinfrastruktur.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Maskin-til-maskin-autentisering for API-bruk | Innlogging for sluttbrukere |
| Tokenutstedelse og scope-basert tilgangsgrunnlag | Faglig autorisasjon i den enkelte tjeneste |
| Standardiserte integrasjonsmÃ¸nstre for API-er | Selve API-ene eller datamodellene som tilbys |
| StÃ¸tte for systembruker-scenarier | Dokument- eller transaksjonssignering |
| Onboarding, test og produksjonslÃ¸p | Full erstatning for fullmakts- og representasjonslÃ¸sninger |

## Veikart over kommende funksjonalitet
**Fakta fra Samarbeidsportalen og Digdir Docs (hentet 2026-03-17):**
- ProduktomrÃ¥det arbeider videre med forenklet bruk, tydeligere innfÃ¸ringslÃ¸p og videreutvikling av tillitstjenestene som helhet.
- Dokumentasjonen viser ogsÃ¥ at systembruker og mer avanserte integrasjonsscenarier er et tydelig utviklingsomrÃ¥de.

**Deduksjon:** Veikartet peker mot videre modning av Maskinporten som felles grunnmur for API-sikkerhet, sÃ¦rlig der virksomheter trenger mer standardisert samspill mellom autentisering, tilgang og delegerte integrasjoner.

## Forretningsverdi/Verdiforslag
### For datatilbydere
- Reduserer behovet for Ã¥ bygge og forvalte egne autentiseringslÃ¸sninger for API-er.
- Senker risiko ved at tilgang til API-er bygger pÃ¥ et etablert nasjonalt sikkerhetsmÃ¸nster.
- GjÃ¸r det enklere Ã¥ eksponere data til flere aktÃ¸rer uten Ã¥ etablere unike oppsett per mottaker.

### For datakonsumenter
- Gir et gjenkjennelig mÃ¸nster for Ã¥ bruke data fra mange virksomheter.
- Reduserer integrasjonskostnader ved at samme token- og autentiseringslogikk kan gjenbrukes.
- GjÃ¸r det lettere Ã¥ etablere nye samarbeid og automatiserte prosesser.

### For offentlig sektor og Ã¸kosystemet
- Styrker nasjonal datadeling ved Ã¥ standardisere hvordan systemer fÃ¥r tilgang til API-er.
- Bidrar til raskere gjenbruk av data og tjenester pÃ¥ tvers av sektorer.
- GjÃ¸r det enklere Ã¥ skille mellom nÃ¥r behovet er maskinell autentisering, og nÃ¥r andre produkter mÃ¥ brukes for innlogging, autorisasjon eller fullmakt.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk og styringsmessig | Virksomheter kan gi tilgang til API-er uten tydelig hjemmel eller feil avgrensede scopes | Tydeligere tilgangsmodeller, avtaler og gjennomgang av scope-bruk |
| Teknisk | Feil integrasjon hos klient eller API-tilbyder kan gi utilgjengelige eller usikre API-kall | TestmiljÃ¸, dokumenterte mÃ¸nstre og validering fÃ¸r produksjon |
| Sikkerhet | Kompromitterte klienthemmeligheter eller feil tokenhÃ¥ndtering kan gi uautorisert tilgang | Streng nÃ¸kkelhÃ¥ndtering, overvÃ¥king og begrensede levetider pÃ¥ token |
| Avhengigheter | Feil forstÃ¥else av samspillet mellom Maskinporten og andre tillitstjenester kan gi feil lÃ¸sningsvalg | Tydelig avgrensning mellom autentisering, autorisasjon og representasjon |
| Brukbarhet | Onboarding kan oppleves som krevende for nye integrasjonsteam | Bedre innfÃ¸ringsstÃ¸tte, eksempler og forenklede startlÃ¸p |

## Kanaler
- Produktside: https://www.digdir.no/om-tjenesten/maskinporten/1558
- Teknisk dokumentasjon: https://docs.digdir.no/docs/Maskinporten/
- Overordnet dokumentasjon: https://docs.digdir.no/docs/Maskinporten/maskinporten_overordnet
- Samarbeidsportal: https://samarbeid.digdir.no/maskinporten/dette-er-maskinporten/96
- Ta i bruk: https://samarbeid.digdir.no/maskinporten/ta-i-bruk-maskinporten/97

## Plattform
Maskinporten er en nasjonal plattform for klientautentisering og tokenutstedelse i maskinelle integrasjoner.

**Fakta:** Digdir Docs beskriver lÃ¸sningen gjennom standardiserte protokoller, tokenflyter og bruk av scopes. Dokumentasjonen beskriver ogsÃ¥ systembruker som et eget funksjonelt omrÃ¥de.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur, konkret skylokasjon og detaljert runtime-oppsett.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet er laget for gjenbruk i mange integrasjoner pÃ¥ tvers av virksomheter.
- Det er sÃ¦rlig relevant nÃ¥r behovet er sikker maskinell tilgang til API-er.
- Det er mindre relevant dersom behovet egentlig er sluttbrukerinnlogging eller detaljert faglig autorisasjon, der andre produkter treffer bedre.

## StÃ¸tter arkitekturprinsipper
- **P5: Del og gjenbruk lÃ¸sninger** realiseres ved at autentisering for API-bruk tilbys som felleskomponent.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** styrkes fordi flere virksomheter kan bygge pÃ¥ samme sikkerhetsmÃ¸nster for datautveksling.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** er sentralt fordi produktet etablerer grunnlaget for sikker maskinell tilgang og kontrollert informasjonsflyt.

## Finansiering
- **Fakta:** Samarbeidsportalen har en egen side for kostnadsmodell for Maskinporten.
- **Ikke fullt offentlig dokumentert i brukte kilder:** Detaljerte satser og full kostnadsfordeling.
- **Deduksjon:** Produktet forvaltes som nasjonal felleslÃ¸sning, men virksomheter mÃ¥ forholde seg til en dokumentert modell for bruk og innfÃ¸ring.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Digdirs produktside og Samarbeidsportalen |
| Driftsansvar | Ikke eksplisitt navngitt i brukte offentlige kilder | Offentlige kilder beskriver ikke detaljert leverandÃ¸r- eller driftsmodell |
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
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/02-Maskinporten-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
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
- Metadata er ryddet slik at dokumentet ikke starter med mÃ¥lgruppelinje, og `Ressurs ID` er skrevet uten parentesforklaring.
- Hovedfunksjoner og avgrensning er skrevet som en tydeligere veiledning for nÃ¥r Maskinporten er riktig lÃ¸sning.
- Verdibeskrivelse og gjenbruksvurdering skiller klarere mellom Maskinporten og tilgrensende produkter.

