# Produkt-canvas: data.altinn.no

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
data.altinn.no

## Ressurs ID
DIGDIR-015

## Status/Livsfase
**Produksjon** - etablert fellesløsning i Altinn for kontrollert datadeling mellom virksomheter.

**Fakta:** data.altinn.no tilbyr dokumenterte domenetjenester gjennom samme tekniske API-mønster, og løsningens tjenestekatalog omfatter blant annet eBevis, Drosjeløyve, Advokatregisteret, Tilda og BITS (hentet 2026-03-10).

## Modenhet
**Høy funksjonell modenhet** - etablert løsning med tydelig produkt- og tjenestestruktur:
- Løsningen er laget for å forenkle datadeling mellom næringsliv og offentlig sektor ved å hente informasjon direkte fra kilden.
- Datadeling skjer gjennom en felles, generisk API-modell som gjenbrukes på tvers av domenetjenester.
- Dokumentasjonen dekker både overordnet produktforståelse, tilgangsmekanismer og tjenestespesifikke beskrivelser.

**Deduksjon:** Modenheten er høy for selve datadelingsmønsteret, mens bredden og modenheten i hver enkel domenetjeneste vil variere etter hvilke kilder og rettighetsregler som er tatt i bruk.

## Kort beskrivelse
data.altinn.no er Altinns fellesløsning for kontrollert datadeling mellom virksomheter. Produktet gjør det mulig å hente informasjon direkte fra autoritative kilder når det finnes lovlig grunnlag, autorisasjon eller samtykke, og gir konsumenter én teknisk modell for å bruke flere ulike datadelingstjenester.

## Kapabiliteter
- **Datautveksling og integrasjon: Dele data med andre** gir datatilbydere en felles måte å tilgjengeliggjøre data gjennom tjenestebaserte oppslag i stedet for punkt-til-punkt-integrasjoner.
- **Datautveksling og integrasjon: Bruke data fra andre** gjør det mulig for konsumenter å hente data direkte fra kilden gjennom en standardisert API-modell.
- **Tillit: Autentisering** støtter maskin-til-maskin-tilgang gjennom virksomhetssertifikat eller Maskinporten.
- **Tillit: Tilgangskontroll** håndterer tilgang gjennom tjenestekontekst, rettigheter og definerte datakilder.
- **Tillit: Samtykke** muliggjør datadeling når bruk av data forutsetter et gyldig samtykke.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** legger til rette for sikker utveksling også når data ikke er åpne eller inneholder personopplysninger.
- **Datadrevet: Sammenstilling av data** støtter datapakker som kombinerer informasjon fra én eller flere kilder og samtidig minimerer datamengden som deles.
- **Tjenesteutvikling: Integrerbare tjenester** bruker samme tekniske mønster på tvers av produkter og gjør nye datadelingstjenester lettere å integrere.
- **Standardisering: Forvaltningsstandarder** gir et felles API- og tilgangsmønster som gjør løsningene mer forutsigbare for både tilbydere og konsumenter.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon på data.altinn.no og docs.data.altinn.no.

## Produktmål
**Primærkilder:** data.altinn.no, produktsiden og docs.data.altinn.no.

Dokumenterte mål:
- Forenkle utveksling av informasjon mellom næringsliv og offentlig sektor.
- Gjøre det mulig å gjenbruke informasjon offentlig sektor allerede har.
- Gjøre det enklere for både datakilder og datakonsumenter å komme i gang med datadeling.
- Tilby sikker utveksling av data gjennom en enkel og generisk API-modell.

Operative mål utledet fra de samme kildene:
- Hente data direkte fra kilden hver gang, slik at konsumenter bruker oppdatert informasjon.
- Gi tilgang til data basert på samtykke, autorisasjon eller annet rettsgrunnlag.
- Gjenbruke samme tekniske mønster på tvers av flere domenetjenester.

**Deduksjon:** Produktet har også et tydelig mål om å redusere behovet for skreddersydde integrasjoner ved å samle flere datadelingstjenester bak samme API-struktur.

## Brukerbehov
- Datatilbydere trenger en kontrollert måte å tilgjengeliggjøre data uten å bygge unike integrasjoner for hver konsument.
- Konsumentsystemer trenger en standardisert måte å hente data direkte fra kilden på.
- Juridiske og forvaltningsmessige miljøer trenger tydelige mekanismer for samtykke, rettigheter og tilgangskontroll.
- Utviklere og integrasjonsteam trenger forutsigbar dokumentasjon, onboarding og tjenestespesifikke beskrivelser.
- Tjenesteeiere trenger en modell der nye datadelingstjenester kan etableres uten å endre grunnmønsteret for autentisering og tilgang.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter som datatilbydere | Dele data med kontrollert tilgang | Etablere eller forvalte domenetjenester | Kildedata forblir hos den autoritative kilden |
| Konsumentsystemer i offentlig og privat sektor | Hente data med lovlig grunnlag | Automatiserte oppslag og gjenbruk av data | Krever registrering, API-nøkkel og maskin-til-maskin-tilgang |
| Tjenesteeiere i Altinn-porteføljen | Bruke felles teknisk mønster | Nye eller videreutviklede datadelingstjenester | Produktene deler samme API-modell |
| Utviklere og integrasjonsteam | Forstå API, tilgang og tjenestelogikk | Integrasjon, test og implementasjon | Teknisk dokumentasjon er sentral for bruk |
| Forvaltnings- og juridiske miljøer | Avklare rettigheter, samtykke og hjemmel | Tilgangsstyring og etterlevelse | Viktig særlig for ikke-åpne data og personopplysninger |

## Hovedfunksjoner
### Primære funksjoner
- Generisk API for datadeling på tvers av flere domenetjenester.
- Oppslag direkte mot kilden ved hver uthenting, i stedet for fast replikerte datasett i løsningen.
- Sammensetting og minimering av datapakker når det er behov for å hente opplysninger fra én eller flere kilder.
- Tilgangsstyring gjennom tjenestekontekst, samtykke, rettigheter og annet rettsgrunnlag.
- Autentisering gjennom virksomhetssertifikat eller Maskinporten.
- Registrering av konsumenter og utstedelse av API-nøkkel som del av bruksmodellen.
- Produktside som samler de ulike domenetjenestene og viser at de teknisk bruker samme API.
- Tjenestespesifikk dokumentasjon for løsninger som eBevis, Drosjeløyve, Advokatregisteret, Tilda og BITS.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Datadeling gjennom en generisk API-modell | Åpen, generell datakatalog for hele offentlig sektor |
| Henting av data direkte fra autoritative kilder | Langtidslagring eller varig kopiering av alle kildedata i løsningen |
| Tilgangsstyring basert på rettigheter, samtykke og tjenestekontekst | Eierskap til de underliggende kildedataene |
| Domenetjenester som bruker samme tekniske mønster | Full datakvalitetsforvaltning hos hver datakilde |
| Teknisk dokumentasjon og tjenestebeskrivelser | Manuell saksbehandling eller ikke-digital tilgangsbehandling |

## Veikart over kommende funksjonalitet
**Fakta:** Produktet har en etablert produkt- og tjenestestruktur, men ingen offentlig tidsfestet utviklingsplan ble verifisert i kildene brukt i denne arbeidsøkten.

**Ikke offentlig verifisert i denne arbeidsøkten:** Konkrete roadmap-punkter, planlagte lanseringer og prioriteringer for nye tjenester.

**Deduksjon:** Videreutviklingen vil sannsynligvis dreie seg om flere domenetjenester, enklere onboarding og videre forbedring av tilgangsstyring og dokumentasjon, men dette må bekreftes i eventuelle interne eller senere publiserte planer.

## Forretningsverdi/Verdiforslag
### For datatilbydere
- Reduserer behovet for skreddersydde integrasjoner mot hver enkelt konsument.
- Gjør det mulig å dele data gjennom en etablert sikkerhets- og tilgangsmodell.

### For datakonsumenter
- Gir én teknisk inngang til flere ulike datadelingstjenester.
- Reduserer implementasjonstid ved at autentisering, tilgang og API-mønster er mer forutsigbart.

### For offentlig sektor og samfunn
- Støtter gjenbruk av informasjon direkte fra kilden i stedet for ny innsamling.
- Legger til rette for mer effektiv og kontrollert datadeling mellom virksomheter og næringsliv.
- Bidrar til mer sammenhengende digitale tjenester gjennom standardiserte integrasjonsmønstre.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil hjemmel, mangelfullt samtykke eller uklar tilgang kan gi ulovlig datadeling | Tydelige tjenesteregler, juridisk avklaring og kontroll av rettsgrunnlag |
| Teknisk | Tilgjengelighet og svartid avhenger av underliggende kildesystemer når data hentes direkte fra kilden | Robust feil- og timeout-håndtering, tydelige avtaler og teknisk overvåking |
| Sikkerhet | Ikke-åpne data eller personopplysninger kan eksponeres ved feil tilgangsstyring | Sterk autentisering, minst mulig datadeling og tydelige tilgangsregler |
| Leverandør/forvaltning | Mange tjenester avhenger av samme tekniske mønster og felles tillitsmekanismer | Felles forvaltningsregime, standardiserte kontroller og koordinert videreutvikling |
| Brukeropplevelse | Registrering, API-nøkler og tilgangskrav kan gjøre oppstart krevende for nye konsumenter | Bedre onboarding, tydelig dokumentasjon og eksempler per tjeneste |

## Kanaler
- Webportal: https://data.altinn.no/
- Produktside: https://data.altinn.no/products
- Teknisk dokumentasjon: https://docs.data.altinn.no/
- Tjenestedokumentasjon: https://docs.data.altinn.no/tjenester/
- Overordnet Altinn-dokumentasjon: https://docs.altinn.studio/nb/

## Plattform
Datadelingsløsning i Altinn-porteføljen basert på en generisk API-modell for kontrollert datadeling mellom virksomheter.

**Fakta:**
- Alle dokumenterte produkter på data.altinn.no bruker samme tekniske API.
- Løsningen henter data direkte fra kilden ved hver forespørsel.
- Autentisering skjer gjennom virksomhetssertifikat eller Maskinporten.

**Ikke offentlig dokumentert i brukte kilder:** Full runtime-arkitektur, hostingvalg, intern søketeknologi og detaljer om driftsplattform.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme API-mønster kan brukes på tvers av flere domenetjenester.
- Felles autentisering og tilgangsstyring reduserer behovet for egne særintegrasjoner.
- Konsumenter kan gjenbruke samme integrasjonsmønster når nye tjenester legges til.
- Datadeling direkte fra kilden reduserer behovet for parallelle kopier og særskilte uthentingsløp.

## Støtter arkitekturprinsipper
- **P4 Del og gjenbruk data** - Løsningen er direkte innrettet mot kontrollert deling og gjenbruk av data fra autoritative kilder.
- **P5 Del og gjenbruk løsninger** - samme tekniske API- og tilgangsmønster kan brukes av flere tjenester.
- **P6 Lag digitale løsninger som støtter samhandling** - produktet gir et felles mønster for datadeling mellom virksomheter og konsumenter.
- **P7 Sørg for tillit til oppgaveløsningen** - autentisering, tilgangskontroll og samtykke er sentrale deler av produktets virkemåte.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Finansieringsmodell, budsjettansvar og eventuelle prismekanismer er ikke offentlig beskrevet i kildene brukt i denne arbeidsøkten.
- **Deduksjon:** Produktet fremstår som del av Altinn-forvaltningen, men kostnads- og finansieringsmodell må bekreftes i andre kilder dersom dette skal beskrives nærmere.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Altinn-forvaltningen i Digdir | Offisielle produkt- og dokumentasjonsdomener for data.altinn.no |
| Driftsansvar | Ikke offentlig spesifisert i brukte kilder | Ingen eksplisitt driftsbeskrivelse i kontrollert materiale |
| Budsjettansvar | Ikke offentlig spesifisert i brukte kilder | Finansieringsmodell er ikke offentlig verifisert |
| Styringsmodell | Forvaltes som del av Altinn-porteføljen med tjenestebasert produktstruktur | Produkt- og tjenestestrukturen på data.altinn.no og docs.data.altinn.no |

## Lenke til dokumentasjon
- https://data.altinn.no/
- https://data.altinn.no/products
- https://docs.data.altinn.no/
- https://docs.data.altinn.no/tjenester/
- https://docs.altinn.studio/nb/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `results/Produktbeskrivelser/17-data-altinn-no-produkt-canvas.md`
- Lokal fil: `results/Produktbeskrivelser/17-data-altinn-no-produkt-canvas-copilot.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://data.altinn.no/ (hentet 2026-03-10)
- Nettkilde: https://data.altinn.no/products (hentet 2026-03-10)
- Nettkilde: https://docs.data.altinn.no/ (hentet 2026-03-10)
- Nettkilde: https://docs.data.altinn.no/tjenester/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/ (hentet 2026-03-10)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Vurderingen bygger videre på `17-data-altinn-no-produkt-canvas-copilot.md`, men er kontrollert mot offisielle kilder på data.altinn.no og docs.data.altinn.no.
- Produktmål, funksjoner og brukersegmenter er strammet inn til det som lot seg verifisere offentlig i denne arbeidsøkten.
- Flere detaljerte påstander fra `-copilot`-versjonen er fjernet eller tonet ned fordi de ikke lot seg bekrefte i brukte kilder, blant annet konkrete kostnadsestimater, oppetidsnivå, Azure-hosting, Elasticsearch, Altinn Studio-koblinger som direkte produktegenskap og detaljerte roadmap-punkter.

### Tekstlige forbedringer
- Hovedteksten er skrevet som en selvstendig produktbeskrivelse for målgruppen, ikke som et referat av kilder.
- Brukersegmenter, kapabiliteter og risiko er skrevet om til mer presis og sammenlignbar struktur.
- Fakta, deduksjon og manglende offentlig dokumentasjon er markert tydeligere der kildegrunnlaget er begrenset.
