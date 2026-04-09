# Produkt-canvas: Fiks digiorden

## Navn
Fiks digiorden

## Ressurs ID
KS-006

## Status/Livsfase
**Produksjon** - etablert nasjonal felleslÃ¸sning for informasjonsforvaltning og styringsstÃ¸tte i kommunal sektor.

**Fakta:** KS beskriver Fiks Digiorden som et verktÃ¸y som understÃ¸tter Orden i eget hus og gir oversikt over applikasjoner og datasett i kommunens digitale landskap. KS omtaler ogsÃ¥ lÃ¸sningen som en nasjonal felleslÃ¸sning og et styringsverktÃ¸y som brukes i kommunenes arbeid med informasjonsforvaltning og informasjonssikkerhet.

## Modenhet
**Middels til hÃ¸y funksjonell modenhet** - lÃ¸sningen er i bruk i kommuner, har publisert funksjonsforstÃ¥else og er videreutviklet etter flytting til FIKS-plattformen.
- Produktsiden beskriver tydelig hvordan lÃ¸sningen brukes til oversikt over applikasjoner og datasett.
- Nyhetssiden viser at tjenesten videreutvikles og at kommuner allerede bruker den.
- Produktet er modent som styrings- og oversiktslÃ¸sning, men ikke som full datakatalog eller full sikkerhetsplattform i seg selv.

## Kort beskrivelse
Fiks digiorden er KS Digitals styrings- og oversiktslÃ¸sning for kommunal informasjonsforvaltning. LÃ¸sningen hjelper kommuner med Ã¥ fÃ¥ oversikt over applikasjoner, datasett og sentrale styringsopplysninger i eget digitalt landskap, slik at det blir lettere Ã¥ planlegge prosjekter, vurdere konsekvenser og bruke felleslÃ¸sninger mer mÃ¥lrettet. Produktet er sÃ¦rlig relevant nÃ¥r kommunen trenger beslutningsstÃ¸tte og systematisk oversikt over hvilke data, systemer og tjenester som allerede finnes.

## Kapabiliteter
- **Informasjonsforvaltning: Datastyring** er direkte relevant fordi lÃ¸sningen brukes som styringsverktÃ¸y for Ã¥ holde oversikt over applikasjoner, data og tilhÃ¸rende forvaltningsinformasjon.
- **Informasjonsforvaltning: Oversikt over datasett** er direkte relevant fordi produktet gir kommunen oversikt over hvilke datasett som finnes i eget landskap.
- **Informasjonsforvaltning: Oversikt over tjenester** er relevant fordi lÃ¸sningen gjÃ¸r det enklere Ã¥ se hvilke applikasjoner og fellestjenester som allerede er i bruk og dermed hvilke ressurser som bÃ¸r gjenbrukes.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals kilder brukt i denne arbeidsÃ¸kten.

## ProduktmÃ¥l
Dokumenterte mÃ¥l:
- Skape klarhet og struktur i kommunens digitale landskap.
- Gi oversikt over applikasjoner og datasett.
- Hjelpe kommunene til Ã¥ bruke felleslÃ¸sninger bedre.

Operative mÃ¥l utledet fra kildene:
- StÃ¸tte nye prosjekter med bedre beslutningsgrunnlag.
- GjÃ¸re det enklere Ã¥ se hvor personopplysninger behandles og hvilke applikasjoner som berÃ¸res.
- Gi styringsinformasjon som kan brukes i informasjonsforvaltning, strategi og beredskap.

## Brukerbehov
- Kommuner trenger oversikt over egne applikasjoner, datasett og styringsobjekter.
- ProsjektmiljÃ¸er trenger raskere innsikt i hvilke systemer og data som blir berÃ¸rt av endringer.
- Virksomhetsarkitektur og informasjonsforvaltning trenger et verktÃ¸y som samler dette i Ã©n oversikt.
- Kommuner trenger Ã¥ se hvilke fellestjenester som allerede er i bruk for Ã¥ unngÃ¥ overlappende arbeid.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Kommunale ledere og digitaliseringsmiljÃ¸er | BeslutningsstÃ¸tte og oversikt over digitalt landskap | Strategi, prioritering og portefÃ¸ljestyring | PrimÃ¦r mÃ¥lgruppe |
| Virksomhetsarkitekter og informasjonsforvaltere | Oversikt over applikasjoner, datasett og styringsinformasjon | Orden i eget hus og informasjonsforvaltning | Kjernebrukere i fagmiljÃ¸et |
| Prosjekt- og utviklingsmiljÃ¸er | Se hvilke systemer, data og avtaler som blir berÃ¸rt | Konsekvensvurdering i nye prosjekter | Bruker lÃ¸sningen som beslutningsstÃ¸tte |
| KS Digital | Forvalte nasjonal fellestjeneste og videreutvikle funksjonssettet | Produktforvaltning og videreutvikling | Tjenesteforvalter |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- Fiks Digiorden gir oversikt over applikasjoner og datasett i kommunens digitale landskap. Det gjÃ¸r lÃ¸sningen relevant som oversikts- og styringsverktÃ¸y, ikke som operativ datadelingstjeneste.
- Produktet brukes som beslutningsstÃ¸tte nÃ¥r kommuner starter nye prosjekter. Det skiller lÃ¸sningen fra en ren katalog ved at den brukes aktivt for Ã¥ vurdere konsekvenser og avhengigheter.
- LÃ¸sningen kan gi oversikt over om ROS, DPIA og databehandleravtaler er registrert for ulike applikasjoner. Dette styrker verdien som styrings- og forvaltningsverktÃ¸y, men gjÃ¸r ikke produktet til en egen sikkerhetstjeneste.
- Fiks Digiorden hjelper kommunene Ã¥ se hvilke fellestjenester som allerede er i bruk. Dermed stÃ¸tter lÃ¸sningen ogsÃ¥ bedre gjenbruk og mindre dobbeltarbeid.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Oversikt over applikasjoner, datasett og utvalgte styringsopplysninger | Selve drift og forvaltning av alle underliggende systemer |
| BeslutningsstÃ¸tte i prosjekter og informasjonsforvaltning | Automatisk datadeling mellom systemer |
| StÃ¸tte til Orden i eget hus | Full datakatalog eller nasjonal metadatahub |
| Oversikt over fellestjenester i bruk | Eget autoritativt register for alle kommunale data |

## Veikart over kommende funksjonalitet
**Fakta:** KS har publisert at Digiorden er videreutviklet etter flytting til FIKS-plattformen, og nyhetssiden viser konkrete forbedringer i funksjonssettet. Jeg fant ikke et samlet offentlig roadmap med tidsfestede milepÃ¦ler utover dette i denne arbeidsÃ¸kten.

**Deduksjon:** Videreutviklingen vil trolig vÃ¦re knyttet til bedre oversikt, flere styringsdata og stÃ¸tte for kommunenes praktiske arbeid med informasjonsforvaltning.

## Forretningsverdi/Verdiforslag
### For kommuner
- Gir bedre oversikt og mindre leting i eget digitalt landskap.
- Reduserer risiko for overlappende arbeid og gjÃ¸r det lettere Ã¥ gjenbruke eksisterende lÃ¸sninger.

### For prosjekter og arkitekturfag
- Gir bedre beslutningsgrunnlag tidlig i prosjektlÃ¸p.
- StÃ¸tter systematisk arbeid med informasjonsforvaltning og portefÃ¸ljestyring.

### For sektoren
- Kan bidra til mer ensartet praksis for orden i eget hus i kommunal sektor.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Oversiktene kan bli misvisende hvis styringsinformasjon om behandling, avtaler eller ansvar ikke holdes oppdatert. | Tydelige rutiner for ajourhold og ansvar i hver kommune. |
| Teknisk | Verdien blir svak hvis lÃ¸sningen ikke er koblet godt nok til kommunens faktiske informasjonsgrunnlag. | Fokus pÃ¥ datakvalitet, god innfÃ¸ring og jevnlig oppdatering. |
| Sikkerhet | Oversikt over systemer og data kan i seg selv vÃ¦re sensitiv styringsinformasjon. | Tilgangsstyring og bevisst hÃ¥ndtering av hvem som fÃ¥r innsyn i hvilke oversikter. |
| LeverandÃ¸r | Kommunene kan bli avhengige av Ã©n felles lÃ¸sning for Ã¥ holde orden i eget hus. | Sikre eksportmuligheter, dokumentasjon og tydelig forvaltning. |
| Brukeropplevelse | LÃ¸sningen mister verdi hvis den oppleves som ekstra rapportering i stedet for nyttig styringsstÃ¸tte. | Knytte bruken tett til konkrete prosjekter, strategi og styringsbehov. |

## Kanaler
- https://ksdigital.no/tjenestene/digiorden/
- https://ksdigital.no/2022/06/14/nyheter-om-fiks-digiorden/

## Plattform
Fiks Digiorden er en fellestjeneste i KS Digital og er flyttet til FIKS-plattformen.

**Fakta:**
- KS opplyser at lÃ¸sningen ble flyttet til FIKS-plattformen i 2021 og videreutviklet derfra.
- Produktet brukes som styrings- og oversiktslÃ¸sning, ikke som selvstendig dataplattform eller register.

**Ikke offentlig dokumentert i brukte kilder:** Full teknisk arkitektur, lagringsmodell og integrasjonsdetaljer.

## Gjenbruk
**Middels til hÃ¸y gjenbruksverdi:**
- LÃ¸sningen har hÃ¸y verdi som felles metode- og oversiktsverktÃ¸y for mange kommuner.
- Gjenbruksverdien ligger i struktur, oversiktsmodell og arbeidsmÃ¥te, ikke i at produktet utfÃ¸rer alle fagfunksjoner selv.

## StÃ¸tter arkitekturprinsipper
- **P4 Del og gjenbruk data** - bedre oversikt over data og datasett er en forutsetning for Ã¥ dele og gjenbruke dem pÃ¥ en kontrollert mÃ¥te.
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** - produktet gjÃ¸r det lettere Ã¥ se hvilke tjenester og fellestjenester som allerede finnes og bÃ¸r brukes sammen.

## Finansiering
**Fakta:** KS opplyser at Digiorden er utviklet i samarbeid med kommunene med stÃ¸tte fra Digifin.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Langsiktig finansieringsmodell for videre forvaltning og videreutvikling.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsiden og nyhetssiden presenterer lÃ¸sningen som KS Digital-tjeneste. |
| Driftsansvar | KS Digital forvalter lÃ¸sningen pÃ¥ FIKS-plattformen; detaljert drift er ikke offentlig spesifisert | FremgÃ¥r indirekte av kildene. |
| Budsjettansvar | Utviklet med stÃ¸tte fra Digifin; videre modell ikke offentlig detaljert dokumentert | Oppgitt i nyhetssiden. |
| Styringsmodell | Utviklet i samarbeid med kommunene og brukerrÃ¥dsmiljÃ¸er | Nyhetssiden beskriver videreutvikling sammen med kommunene i brukerrÃ¥det. |

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

