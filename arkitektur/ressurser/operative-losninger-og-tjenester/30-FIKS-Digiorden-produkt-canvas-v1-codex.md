# Produkt-canvas: Fiks digiorden

## Navn
Fiks digiorden

## Ressurs ID
KS-006

## Status/Livsfase
**Produksjon** - etablert nasjonal fellesløsning for informasjonsforvaltning og styringsstøtte i kommunal sektor.

**Fakta:** KS beskriver Fiks Digiorden som et verktøy som understøtter Orden i eget hus og gir oversikt over applikasjoner og datasett i kommunens digitale landskap. KS omtaler også løsningen som en nasjonal fellesløsning og et styringsverktøy som brukes i kommunenes arbeid med informasjonsforvaltning og informasjonssikkerhet.

## Modenhet
**Middels til høy funksjonell modenhet** - løsningen er i bruk i kommuner, har publisert funksjonsforståelse og er videreutviklet etter flytting til FIKS-plattformen.
- Produktsiden beskriver tydelig hvordan løsningen brukes til oversikt over applikasjoner og datasett.
- Nyhetssiden viser at tjenesten videreutvikles og at kommuner allerede bruker den.
- Produktet er modent som styrings- og oversiktsløsning, men ikke som full datakatalog eller full sikkerhetsplattform i seg selv.

## Kort beskrivelse
Fiks digiorden er KS Digitals styrings- og oversiktsløsning for kommunal informasjonsforvaltning. Løsningen hjelper kommuner med å få oversikt over applikasjoner, datasett og sentrale styringsopplysninger i eget digitalt landskap, slik at det blir lettere å planlegge prosjekter, vurdere konsekvenser og bruke fellesløsninger mer målrettet. Produktet er særlig relevant når kommunen trenger beslutningsstøtte og systematisk oversikt over hvilke data, systemer og tjenester som allerede finnes.

## Kapabiliteter
- **Informasjonsforvaltning: Datastyring** er direkte relevant fordi løsningen brukes som styringsverktøy for å holde oversikt over applikasjoner, data og tilhørende forvaltningsinformasjon.
- **Informasjonsforvaltning: Oversikt over datasett** er direkte relevant fordi produktet gir kommunen oversikt over hvilke datasett som finnes i eget landskap.
- **Informasjonsforvaltning: Oversikt over tjenester** er relevant fordi løsningen gjør det enklere å se hvilke applikasjoner og fellestjenester som allerede er i bruk og dermed hvilke ressurser som bør gjenbrukes.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals kilder brukt i denne arbeidsøkten.

## Produktmål
Dokumenterte mål:
- Skape klarhet og struktur i kommunens digitale landskap.
- Gi oversikt over applikasjoner og datasett.
- Hjelpe kommunene til å bruke fellesløsninger bedre.

Operative mål utledet fra kildene:
- Støtte nye prosjekter med bedre beslutningsgrunnlag.
- Gjøre det enklere å se hvor personopplysninger behandles og hvilke applikasjoner som berøres.
- Gi styringsinformasjon som kan brukes i informasjonsforvaltning, strategi og beredskap.

## Brukerbehov
- Kommuner trenger oversikt over egne applikasjoner, datasett og styringsobjekter.
- Prosjektmiljøer trenger raskere innsikt i hvilke systemer og data som blir berørt av endringer.
- Virksomhetsarkitektur og informasjonsforvaltning trenger et verktøy som samler dette i én oversikt.
- Kommuner trenger å se hvilke fellestjenester som allerede er i bruk for å unngå overlappende arbeid.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommunale ledere og digitaliseringsmiljøer | Beslutningsstøtte og oversikt over digitalt landskap | Strategi, prioritering og porteføljestyring | Primær målgruppe |
| Virksomhetsarkitekter og informasjonsforvaltere | Oversikt over applikasjoner, datasett og styringsinformasjon | Orden i eget hus og informasjonsforvaltning | Kjernebrukere i fagmiljøet |
| Prosjekt- og utviklingsmiljøer | Se hvilke systemer, data og avtaler som blir berørt | Konsekvensvurdering i nye prosjekter | Bruker løsningen som beslutningsstøtte |
| KS Digital | Forvalte nasjonal fellestjeneste og videreutvikle funksjonssettet | Produktforvaltning og videreutvikling | Tjenesteforvalter |

## Hovedfunksjoner
### Primære funksjoner
- Fiks Digiorden gir oversikt over applikasjoner og datasett i kommunens digitale landskap. Det gjør løsningen relevant som oversikts- og styringsverktøy, ikke som operativ datadelingstjeneste.
- Produktet brukes som beslutningsstøtte når kommuner starter nye prosjekter. Det skiller løsningen fra en ren katalog ved at den brukes aktivt for å vurdere konsekvenser og avhengigheter.
- Løsningen kan gi oversikt over om ROS, DPIA og databehandleravtaler er registrert for ulike applikasjoner. Dette styrker verdien som styrings- og forvaltningsverktøy, men gjør ikke produktet til en egen sikkerhetstjeneste.
- Fiks Digiorden hjelper kommunene å se hvilke fellestjenester som allerede er i bruk. Dermed støtter løsningen også bedre gjenbruk og mindre dobbeltarbeid.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Oversikt over applikasjoner, datasett og utvalgte styringsopplysninger | Selve drift og forvaltning av alle underliggende systemer |
| Beslutningsstøtte i prosjekter og informasjonsforvaltning | Automatisk datadeling mellom systemer |
| Støtte til Orden i eget hus | Full datakatalog eller nasjonal metadatahub |
| Oversikt over fellestjenester i bruk | Eget autoritativt register for alle kommunale data |

## Veikart over kommende funksjonalitet
**Fakta:** KS har publisert at Digiorden er videreutviklet etter flytting til FIKS-plattformen, og nyhetssiden viser konkrete forbedringer i funksjonssettet. Jeg fant ikke et samlet offentlig roadmap med tidsfestede milepæler utover dette i denne arbeidsøkten.

**Deduksjon:** Videreutviklingen vil trolig være knyttet til bedre oversikt, flere styringsdata og støtte for kommunenes praktiske arbeid med informasjonsforvaltning.

## Forretningsverdi/Verdiforslag
### For kommuner
- Gir bedre oversikt og mindre leting i eget digitalt landskap.
- Reduserer risiko for overlappende arbeid og gjør det lettere å gjenbruke eksisterende løsninger.

### For prosjekter og arkitekturfag
- Gir bedre beslutningsgrunnlag tidlig i prosjektløp.
- Støtter systematisk arbeid med informasjonsforvaltning og porteføljestyring.

### For sektoren
- Kan bidra til mer ensartet praksis for orden i eget hus i kommunal sektor.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Oversiktene kan bli misvisende hvis styringsinformasjon om behandling, avtaler eller ansvar ikke holdes oppdatert. | Tydelige rutiner for ajourhold og ansvar i hver kommune. |
| Teknisk | Verdien blir svak hvis løsningen ikke er koblet godt nok til kommunens faktiske informasjonsgrunnlag. | Fokus på datakvalitet, god innføring og jevnlig oppdatering. |
| Sikkerhet | Oversikt over systemer og data kan i seg selv være sensitiv styringsinformasjon. | Tilgangsstyring og bevisst håndtering av hvem som får innsyn i hvilke oversikter. |
| Leverandør | Kommunene kan bli avhengige av én felles løsning for å holde orden i eget hus. | Sikre eksportmuligheter, dokumentasjon og tydelig forvaltning. |
| Brukeropplevelse | Løsningen mister verdi hvis den oppleves som ekstra rapportering i stedet for nyttig styringsstøtte. | Knytte bruken tett til konkrete prosjekter, strategi og styringsbehov. |

## Kanaler
- https://ksdigital.no/tjenestene/digiorden/
- https://ksdigital.no/2022/06/14/nyheter-om-fiks-digiorden/

## Plattform
Fiks Digiorden er en fellestjeneste i KS Digital og er flyttet til FIKS-plattformen.

**Fakta:**
- KS opplyser at løsningen ble flyttet til FIKS-plattformen i 2021 og videreutviklet derfra.
- Produktet brukes som styrings- og oversiktsløsning, ikke som selvstendig dataplattform eller register.

**Ikke offentlig dokumentert i brukte kilder:** Full teknisk arkitektur, lagringsmodell og integrasjonsdetaljer.

## Gjenbruk
**Middels til høy gjenbruksverdi:**
- Løsningen har høy verdi som felles metode- og oversiktsverktøy for mange kommuner.
- Gjenbruksverdien ligger i struktur, oversiktsmodell og arbeidsmåte, ikke i at produktet utfører alle fagfunksjoner selv.

## Støtter arkitekturprinsipper
- **P4 Del og gjenbruk data** - bedre oversikt over data og datasett er en forutsetning for å dele og gjenbruke dem på en kontrollert måte.
- **P6 Lag digitale løsninger som støtter samhandling** - produktet gjør det lettere å se hvilke tjenester og fellestjenester som allerede finnes og bør brukes sammen.

## Finansiering
**Fakta:** KS opplyser at Digiorden er utviklet i samarbeid med kommunene med støtte fra Digifin.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Langsiktig finansieringsmodell for videre forvaltning og videreutvikling.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsiden og nyhetssiden presenterer løsningen som KS Digital-tjeneste. |
| Driftsansvar | KS Digital forvalter løsningen på FIKS-plattformen; detaljert drift er ikke offentlig spesifisert | Fremgår indirekte av kildene. |
| Budsjettansvar | Utviklet med støtte fra Digifin; videre modell ikke offentlig detaljert dokumentert | Oppgitt i nyhetssiden. |
| Styringsmodell | Utviklet i samarbeid med kommunene og brukerrådsmiljøer | Nyhetssiden beskriver videreutvikling sammen med kommunene i brukerrådet. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/digiorden/
- https://ksdigital.no/2022/06/14/nyheter-om-fiks-digiorden/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://ksdigital.no/tjenestene/digiorden/ (hentet 2026-03-18)
- Nettkilde: https://ksdigital.no/2022/06/14/nyheter-om-fiks-digiorden/ (hentet 2026-03-18)


