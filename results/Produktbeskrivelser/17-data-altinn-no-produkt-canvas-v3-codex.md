# Produkt-canvas: data.altinn.no

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
data.altinn.no

## Ressurs ID
DIGDIR-015

## Status/Livsfase
**Produksjon** - etablert felleslÃ¸sning i Altinn for kontrollert datadeling mellom virksomheter.

**Fakta:** data.altinn.no tilbyr dokumenterte domenetjenester gjennom samme tekniske API-mÃ¸nster, og lÃ¸sningens tjenestekatalog omfatter blant annet eBevis, DrosjelÃ¸yve, Advokatregisteret, Tilda og BITS (hentet 2026-03-10).

## Modenhet
**HÃ¸y funksjonell modenhet** - etablert lÃ¸sning med tydelig produkt- og tjenestestruktur:
- LÃ¸sningen er laget for Ã¥ forenkle datadeling mellom nÃ¦ringsliv og offentlig sektor ved Ã¥ hente informasjon direkte fra kilden.
- Datadeling skjer gjennom en felles, generisk API-modell som gjenbrukes pÃ¥ tvers av domenetjenester.
- Dokumentasjonen dekker bÃ¥de overordnet produktforstÃ¥else, tilgangsmekanismer og tjenestespesifikke beskrivelser.

**Deduksjon:** Modenheten er hÃ¸y for selve datadelingsmÃ¸nsteret, mens bredden og modenheten i hver enkel domenetjeneste vil variere etter hvilke kilder og rettighetsregler som er tatt i bruk.

## Kort beskrivelse
data.altinn.no er Altinns felleslÃ¸sning for kontrollert datadeling mellom virksomheter. Produktet gjÃ¸r det mulig Ã¥ hente informasjon direkte fra autoritative kilder nÃ¥r det finnes lovlig grunnlag, autorisasjon eller samtykke, og gir konsumenter Ã©n teknisk modell for Ã¥ bruke flere ulike datadelingstjenester.

## Kapabiliteter
- **Datautveksling og integrasjon: Dele data med andre** gir datatilbydere en felles mÃ¥te Ã¥ tilgjengeliggjÃ¸re data gjennom tjenestebaserte oppslag i stedet for punkt-til-punkt-integrasjoner.
- **Datautveksling og integrasjon: Bruke data fra andre** gjÃ¸r det mulig for konsumenter Ã¥ hente data direkte fra kilden gjennom en standardisert API-modell.
- **Tillit: Autentisering** stÃ¸tter maskin-til-maskin-tilgang gjennom virksomhetssertifikat eller Maskinporten.
- **Tillit: Tilgangskontroll** hÃ¥ndterer tilgang gjennom tjenestekontekst, rettigheter og definerte datakilder.
- **Tillit: Samtykke** muliggjÃ¸r datadeling nÃ¥r bruk av data forutsetter et gyldig samtykke.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** legger til rette for sikker utveksling ogsÃ¥ nÃ¥r data ikke er Ã¥pne eller inneholder personopplysninger.
- **Datadrevet: Sammenstilling av data** stÃ¸tter datapakker som kombinerer informasjon fra Ã©n eller flere kilder og samtidig minimerer datamengden som deles.
- **Tjenesteutvikling: Integrerbare tjenester** bruker samme tekniske mÃ¸nster pÃ¥ tvers av produkter og gjÃ¸r nye datadelingstjenester lettere Ã¥ integrere.
- **Standardisering: Forvaltningsstandarder** gir et felles API- og tilgangsmÃ¸nster som gjÃ¸r lÃ¸sningene mer forutsigbare for bÃ¥de tilbydere og konsumenter.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon pÃ¥ data.altinn.no og docs.data.altinn.no.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** data.altinn.no, produktsiden og docs.data.altinn.no.

Dokumenterte mÃ¥l:
- Forenkle utveksling av informasjon mellom nÃ¦ringsliv og offentlig sektor.
- GjÃ¸re det mulig Ã¥ gjenbruke informasjon offentlig sektor allerede har.
- GjÃ¸re det enklere for bÃ¥de datakilder og datakonsumenter Ã¥ komme i gang med datadeling.
- Tilby sikker utveksling av data gjennom en enkel og generisk API-modell.

Operative mÃ¥l utledet fra de samme kildene:
- Hente data direkte fra kilden hver gang, slik at konsumenter bruker oppdatert informasjon.
- Gi tilgang til data basert pÃ¥ samtykke, autorisasjon eller annet rettsgrunnlag.
- Gjenbruke samme tekniske mÃ¸nster pÃ¥ tvers av flere domenetjenester.

**Deduksjon:** Produktet har ogsÃ¥ et tydelig mÃ¥l om Ã¥ redusere behovet for skreddersydde integrasjoner ved Ã¥ samle flere datadelingstjenester bak samme API-struktur.

## Brukerbehov
- Datatilbydere trenger en kontrollert mÃ¥te Ã¥ tilgjengeliggjÃ¸re data uten Ã¥ bygge unike integrasjoner for hver konsument.
- Konsumentsystemer trenger en standardisert mÃ¥te Ã¥ hente data direkte fra kilden pÃ¥.
- Juridiske og forvaltningsmessige miljÃ¸er trenger tydelige mekanismer for samtykke, rettigheter og tilgangskontroll.
- Utviklere og integrasjonsteam trenger forutsigbar dokumentasjon, onboarding og tjenestespesifikke beskrivelser.
- Tjenesteeiere trenger en modell der nye datadelingstjenester kan etableres uten Ã¥ endre grunnmÃ¸nsteret for autentisering og tilgang.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige virksomheter som datatilbydere | Dele data med kontrollert tilgang | Etablere eller forvalte domenetjenester | Kildedata forblir hos den autoritative kilden |
| Konsumentsystemer i offentlig og privat sektor | Hente data med lovlig grunnlag | Automatiserte oppslag og gjenbruk av data | Krever registrering, API-nÃ¸kkel og maskin-til-maskin-tilgang |
| Tjenesteeiere i Altinn-portefÃ¸ljen | Bruke felles teknisk mÃ¸nster | Nye eller videreutviklede datadelingstjenester | Produktene deler samme API-modell |
| Utviklere og integrasjonsteam | ForstÃ¥ API, tilgang og tjenestelogikk | Integrasjon, test og implementasjon | Teknisk dokumentasjon er sentral for bruk |
| Forvaltnings- og juridiske miljÃ¸er | Avklare rettigheter, samtykke og hjemmel | Tilgangsstyring og etterlevelse | Viktig sÃ¦rlig for ikke-Ã¥pne data og personopplysninger |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- Generisk API for datadeling pÃ¥ tvers av flere domenetjenester.
- Oppslag direkte mot kilden ved hver uthenting, i stedet for fast replikerte datasett i lÃ¸sningen.
- Sammensetting og minimering av datapakker nÃ¥r det er behov for Ã¥ hente opplysninger fra Ã©n eller flere kilder.
- Tilgangsstyring gjennom tjenestekontekst, samtykke, rettigheter og annet rettsgrunnlag.
- Autentisering gjennom virksomhetssertifikat eller Maskinporten.
- Registrering av konsumenter og utstedelse av API-nÃ¸kkel som del av bruksmodellen.
- Produktside som samler de ulike domenetjenestene og viser at de teknisk bruker samme API.
- Tjenestespesifikk dokumentasjon for lÃ¸sninger som eBevis, DrosjelÃ¸yve, Advokatregisteret, Tilda og BITS.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Datadeling gjennom en generisk API-modell | Ã…pen, generell datakatalog for hele offentlig sektor |
| Henting av data direkte fra autoritative kilder | Langtidslagring eller varig kopiering av alle kildedata i lÃ¸sningen |
| Tilgangsstyring basert pÃ¥ rettigheter, samtykke og tjenestekontekst | Eierskap til de underliggende kildedataene |
| Domenetjenester som bruker samme tekniske mÃ¸nster | Full datakvalitetsforvaltning hos hver datakilde |
| Teknisk dokumentasjon og tjenestebeskrivelser | Manuell saksbehandling eller ikke-digital tilgangsbehandling |

## Veikart over kommende funksjonalitet
**Fakta:** Produktet har en etablert produkt- og tjenestestruktur, men ingen offentlig tidsfestet utviklingsplan ble verifisert i kildene brukt i denne arbeidsÃ¸kten.

**Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Konkrete roadmap-punkter, planlagte lanseringer og prioriteringer for nye tjenester.

**Deduksjon:** Videreutviklingen vil sannsynligvis dreie seg om flere domenetjenester, enklere onboarding og videre forbedring av tilgangsstyring og dokumentasjon, men dette mÃ¥ bekreftes i eventuelle interne eller senere publiserte planer.

## Forretningsverdi/Verdiforslag
### For datatilbydere
- Reduserer behovet for skreddersydde integrasjoner mot hver enkelt konsument.
- GjÃ¸r det mulig Ã¥ dele data gjennom en etablert sikkerhets- og tilgangsmodell.

### For datakonsumenter
- Gir Ã©n teknisk inngang til flere ulike datadelingstjenester.
- Reduserer implementasjonstid ved at autentisering, tilgang og API-mÃ¸nster er mer forutsigbart.

### For offentlig sektor og samfunn
- StÃ¸tter gjenbruk av informasjon direkte fra kilden i stedet for ny innsamling.
- Legger til rette for mer effektiv og kontrollert datadeling mellom virksomheter og nÃ¦ringsliv.
- Bidrar til mer sammenhengende digitale tjenester gjennom standardiserte integrasjonsmÃ¸nstre.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Feil hjemmel, mangelfullt samtykke eller uklar tilgang kan gi ulovlig datadeling | Tydelige tjenesteregler, juridisk avklaring og kontroll av rettsgrunnlag |
| Teknisk | Tilgjengelighet og svartid avhenger av underliggende kildesystemer nÃ¥r data hentes direkte fra kilden | Robust feil- og timeout-hÃ¥ndtering, tydelige avtaler og teknisk overvÃ¥king |
| Sikkerhet | Ikke-Ã¥pne data eller personopplysninger kan eksponeres ved feil tilgangsstyring | Sterk autentisering, minst mulig datadeling og tydelige tilgangsregler |
| LeverandÃ¸r/forvaltning | Mange tjenester avhenger av samme tekniske mÃ¸nster og felles tillitsmekanismer | Felles forvaltningsregime, standardiserte kontroller og koordinert videreutvikling |
| Brukeropplevelse | Registrering, API-nÃ¸kler og tilgangskrav kan gjÃ¸re oppstart krevende for nye konsumenter | Bedre onboarding, tydelig dokumentasjon og eksempler per tjeneste |

## Kanaler
- Webportal: https://data.altinn.no/
- Produktside: https://data.altinn.no/products
- Teknisk dokumentasjon: https://docs.data.altinn.no/
- Tjenestedokumentasjon: https://docs.data.altinn.no/tjenester/
- Overordnet Altinn-dokumentasjon: https://docs.altinn.studio/nb/

## Plattform
DatadelingslÃ¸sning i Altinn-portefÃ¸ljen basert pÃ¥ en generisk API-modell for kontrollert datadeling mellom virksomheter.

**Fakta:**
- Alle dokumenterte produkter pÃ¥ data.altinn.no bruker samme tekniske API.
- LÃ¸sningen henter data direkte fra kilden ved hver forespÃ¸rsel.
- Autentisering skjer gjennom virksomhetssertifikat eller Maskinporten.

**Ikke offentlig dokumentert i brukte kilder:** Full runtime-arkitektur, hostingvalg, intern sÃ¸keteknologi og detaljer om driftsplattform.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Samme API-mÃ¸nster kan brukes pÃ¥ tvers av flere domenetjenester.
- Felles autentisering og tilgangsstyring reduserer behovet for egne sÃ¦rintegrasjoner.
- Konsumenter kan gjenbruke samme integrasjonsmÃ¸nster nÃ¥r nye tjenester legges til.
- Datadeling direkte fra kilden reduserer behovet for parallelle kopier og sÃ¦rskilte uthentingslÃ¸p.

## StÃ¸tter arkitekturprinsipper
- **P4 Del og gjenbruk data** - LÃ¸sningen er direkte innrettet mot kontrollert deling og gjenbruk av data fra autoritative kilder.
- **P5 Del og gjenbruk lÃ¸sninger** - samme tekniske API- og tilgangsmÃ¸nster kan brukes av flere tjenester.
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** - produktet gir et felles mÃ¸nster for datadeling mellom virksomheter og konsumenter.
- **P7 SÃ¸rg for tillit til oppgavelÃ¸sningen** - autentisering, tilgangskontroll og samtykke er sentrale deler av produktets virkemÃ¥te.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Finansieringsmodell, budsjettansvar og eventuelle prismekanismer er ikke offentlig beskrevet i kildene brukt i denne arbeidsÃ¸kten.
- **Deduksjon:** Produktet fremstÃ¥r som del av Altinn-forvaltningen, men kostnads- og finansieringsmodell mÃ¥ bekreftes i andre kilder dersom dette skal beskrives nÃ¦rmere.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Altinn-forvaltningen i Digdir | Offisielle produkt- og dokumentasjonsdomener for data.altinn.no |
| Driftsansvar | Ikke offentlig spesifisert i brukte kilder | Ingen eksplisitt driftsbeskrivelse i kontrollert materiale |
| Budsjettansvar | Ikke offentlig spesifisert i brukte kilder | Finansieringsmodell er ikke offentlig verifisert |
| Styringsmodell | Forvaltes som del av Altinn-portefÃ¸ljen med tjenestebasert produktstruktur | Produkt- og tjenestestrukturen pÃ¥ data.altinn.no og docs.data.altinn.no |

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
- Vurderingen bygger videre pÃ¥ `17-data-altinn-no-produkt-canvas-copilot.md`, men er kontrollert mot offisielle kilder pÃ¥ data.altinn.no og docs.data.altinn.no.
- ProduktmÃ¥l, funksjoner og brukersegmenter er strammet inn til det som lot seg verifisere offentlig i denne arbeidsÃ¸kten.
- Flere detaljerte pÃ¥stander fra `-copilot`-versjonen er fjernet eller tonet ned fordi de ikke lot seg bekrefte i brukte kilder, blant annet konkrete kostnadsestimater, oppetidsnivÃ¥, Azure-hosting, Elasticsearch, Altinn Studio-koblinger som direkte produktegenskap og detaljerte roadmap-punkter.

### Tekstlige forbedringer
- Hovedteksten er skrevet som en selvstendig produktbeskrivelse for mÃ¥lgruppen, ikke som et referat av kilder.
- Brukersegmenter, kapabiliteter og risiko er skrevet om til mer presis og sammenlignbar struktur.
- Fakta, deduksjon og manglende offentlig dokumentasjon er markert tydeligere der kildegrunnlaget er begrenset.
