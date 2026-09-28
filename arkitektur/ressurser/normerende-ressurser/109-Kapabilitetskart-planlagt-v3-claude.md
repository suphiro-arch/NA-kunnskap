# Kapabilitetskart (planlagt)

## Navn
Kapabilitetskart (planlagt)

## Ressurs ID
DIGDIR-041

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Kapabilitetsmodell

## Status/Livsfase
Under utvikling, publisert som arbeidsversjon.

**Fakta:** Kapabilitetskartet er publisert som del av modellen for nasjonal arkitektur i Digdirs repositorium `digdir/nasjonal-arkitektur` på GitHub, med dokumentasjonsside på digdir.github.io. Repositoriet ble opprettet 29. april 2026, og dokumentasjonssiden oppgir 11. september 2026 som sist oppdatert. Modellfilene er versjonert med dato, fra 2026-05-20 til 2026-09-02.

**Fakta:** Dokumentasjonssiden beskriver arbeidet med kartlegging av felles ressurser som pågående, med prototype tilgjengelig, og sier at dokumentasjonen forbedres kontinuerlig. Digdir omtaler på digdir.no arbeidet som en kapabilitetsoversikt som kan legges til grunn for en framtidig gapanalyse.

**Deduksjon:** Kartet er ikke lenger bare planlagt. Det finnes en publisert, datert modell, men den er ikke fastsatt som ferdig produkt, og innholdet endres mellom versjonene.

## Kort beskrivelse
Kapabilitetskartet beskriver hvilke evner offentlig sektor må ha for å få samhandling, gjenbruk og strategisk retning i et felles digitalt økosystem. Det er den sentrale delen av Digdirs modell for nasjonal arkitektur, og skiller mellom kapabiliteter, som er evner beskrevet uavhengig av løsning, og ressurser, som er de konkrete byggeklossene som realiserer evnene.

Kartet har tre nivåer: én overordnet kapabilitet, `Nasjonal arkitektur for samhandling`, hovedkapabiliteter som strukturerer modellen, og delkapabiliteter som knyttes til ressurser og mål. Modellen er laget i Archi og publiseres både som ArchiMate-fil, YAML og Turtle, sammen med metamodell, arkitekturprinsipper og EIF-lagmodellen.

## Formål og normerende rolle
Formålet er å gi et felles språk for hvilke evner som må være på plass når offentlig sektor skal utvikle mer sammenhengende tjenester og et felles digitalt økosystem. Ved å koble ressurser til kapabiliteter skal kartet gjøre det lettere å se hva som finnes, hva som mangler, og hvordan løsningene henger sammen.

Den normerende rollen er veiledende. Kartet setter en felles struktur for hvordan behov, ressurser og gap beskrives, men er ikke gjort forpliktende for noen.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er **veiledende, uten rettslig forankring i kildene**.

**Fakta:** Verken dokumentasjonssiden eller Digdirs sider om nasjonal arkitektur viser til lov, forskrift, rundskriv eller vedtak som gjør kartet forpliktende. Digitaliseringsrundskrivet nevner ikke kapabilitetskartet.

**Deduksjon:** Kartet får praktisk betydning gjennom bruk, ikke gjennom plikt: når Digdir bruker det i casearbeid, i ressursoversikten og i framtidige gapanalyser. Det finnes ingen etterlevelsesmekanisme, og avvik fra kartets struktur har ingen formell konsekvens.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentasjonssiden for nasjonal arkitektur og Digdirs sider om arbeidet.

`Informasjonsforvaltning: Datastyring` er tatt ut. Kapabiliteten gjelder forvaltning av dataressurser gjennom roller, ansvar og kvalitetsarbeid, og kartet gjør ikke det. `Veiledning: Utvikling og formidling av veiledning` er vurdert og ikke satt: kartet er en referansemodell for styring, ikke veiledning om hvordan løsninger skal bygges. Kartet har ingen rettslig forankring, og `Juridisk samhandling` er ikke aktuell.

- **Strategisk styring: Arkitekturstyring**
  Kartet er den felles kapabilitetsmodellen som kapabiliteten sier må forvaltes og tolkes likt av alle virksomheter, og det er grunnlaget Digdir vil bruke for å vurdere om nasjonale ressurser dekker behovene og for å prioritere gap. Definisjonen nevner forvaltning av felles metamodeller, bruk av ArchiMate og evaluering av modenhet for kapabiliteter, som er det modellen gjør.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Arkitekter og fagansvarlige | Felles modell for behov, avhengigheter og gap | Analyse, målarkitektur og prioritering | Kjernebrukere |
| Portefølje- og ledelsesmiljøer | Begrunnelse for tiltak og prioriteringer | Veikart, samordning og styringsdialog | Nyttig når tiltak konkurrerer om oppmerksomhet |
| Produkt- og programmiljøer | Kobling mellom problem, kapabiliteter og ressurser | Konseptvalg og løsningsvurdering | Digdir bruker kartet slik i Samt BU |
| Digdir, KS og kommunal sektor | Felles struktur for utvikling av nasjonal arkitektur | Metodeutvikling og caseutprøving | Digdir leder arbeidet i samarbeid med KS og kommunal sektor |

## Normerende innhold
**Fakta:** Kartet er strukturert i tre nivåer. Den overordnede kapabiliteten er definert som evnen til å sikre samhandling, gjenbruk og strategisk retning i et nasjonalt digitalt økosystem. Hovedkapabilitetene omfatter blant annet `Strategisk styring`, `Tillit`, `Sluttbrukertjenester`, `Datautveksling og integrasjon`, `Standardisering`, `Tjenesteutvikling`, `Informasjonssikkerhet` og `Informasjonsforvaltning`. Hver kapabilitet har en kort definisjon som evne. I YAML-eksporten har hver delkapabilitet i tillegg begrunnelse, omfang fordelt på juridisk, organisatorisk, semantisk og teknisk nivå, og bidrag til sammenhengende tjenester.

**Fakta:** Metoden er at kapabiliteter beskriver hva økosystemet, en sektor, en virksomhet eller et domene må kunne gjøre for å skape verdi, mens ressursene er byggeklossene som realiserer evnene. Modellen skal kunne brukes til å identifisere gap, prioritere tiltak og koble nasjonalt nivå til domenenivå.

Det normerende ligger ikke i lista over kapabiliteter alene, men i at samme struktur brukes til å koble mål, ressurser og gap.

## Bruksområde
Kartet bør brukes når en trenger å forstå hvilke evner som må være på plass for å realisere mål eller løse et samhandlingsproblem, og når en vil vurdere om eksisterende ressurser dekker behovene. Det er særlig nyttig i tidligfase, i målarkitektur og når flere alternative tiltak må sammenlignes mot samme problem.

**Fakta:** Digdir bruker kartet i samarbeid med prosjektet Samt BU, Sammenhengende tjenester for barn og unge, til å identifisere hvilke samhandlingsevner som må være på plass og hvilke gjenbrukbare løsninger som bør vurderes.

## Typiske analyse- og beslutningssituasjoner
- når en skal identifisere gap mellom ønsket målbilde og dagens ressursdekning
- når flere tiltak må prioriteres ut fra hvilke kapabiliteter de styrker
- når en trenger å skille mellom manglende ressurs, manglende styring og manglende modenhet
- når konkrete case skal kobles til et helhetlig kapabilitets- og ressursbilde

## Når ressursen normalt ikke er tilstrekkelig alene
Kartet er ikke tilstrekkelig alene når en skal beslutte finansiering, velge konkrete tekniske løsninger eller avklare hjemmel. Da må det kombineres med beskrivelser av de konkrete ressursene, juridiske vurderinger og styringsinformasjon for sektoren eller porteføljen.

Det er heller ikke nok når problemet handler om lokal organisering eller detaljert tjenestedesign uten behov for sammenligning på tvers.

## Scope og avgrensning
Inngår:
- kapabiliteter på tre nivåer med definisjoner
- skillet mellom kapabiliteter og ressurser, og koblingen mellom dem
- kobling til arkitekturprinsipper, mål og EIF-lagmodellen i samme modell

Inngår ikke:
- valg av operative løsninger eller standarder
- budsjettvedtak eller prosjektplanlegging
- selve gapanalysen, som er omtalt som framtidig arbeid
- en fastsatt forvaltningsmodell for kartet

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digdir, som leder arbeidet med nasjonal arkitektur i samarbeid med KS og kommunal sektor |
| Forvaltningsansvar | **Fakta:** Digdir forvalter modellen i repositoriet `digdir/nasjonal-arkitektur`, der dokumentasjonen bygges fra ArchiMate-modellen. Kontaktpunkt er nasjonalarkitektur@digdir.no |
| Endringsprosess | **Fakta:** Nye versjoner publiseres som daterte modellfiler, og Digdir beskriver arbeidsformen som iterativ med hyppige leveranser. **Ikke offentlig dokumentert i denne arbeidsøkten:** hvem som beslutter endringer i kartet, og om det er tenkt høring eller forankring i Arkitektur- og standardiseringsrådet |
| Publiserings- og beslutningsarena | GitHub og digdir.github.io for modellen, digdir.no for omtale av arbeidet |

## Relasjon til andre ressurser
- **Overordnede arkitekturprinsipper for offentlig sektor (`DIGDIR-030`):** inngår i samme modell og er koblet til kapabilitetene.
- **Digitaliseringsrådet (`DIGDIR-043`):** rådets anbefalingsbrev om nasjonal arkitektur for samhandling og tjenesteutvikling, fra april 2026, omtaler kapabilitetsoversikten som grunnlag Digdir tenker å legge til grunn for en framtidig gapanalyse.
- **Rammeverk for digital samhandling (`DIGDIR-025`):** bygger på samme EIF-inndeling i juridisk, organisatorisk, semantisk og teknisk samhandlingsevne som modellen bruker.
- **Ressursoversikten for nasjonal arkitektur:** Digdir lenker på digdir.no til en ressursoversikt på GitHub Pages som bruker kapabilitetskartet til å kategorisere ressurser.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er at prioritering og samordning kan bli mer behovsdrevet. Et felles kart gjør det lettere å forklare om et tiltak dekker et reelt gap, og om eksisterende ressurser bør gjenbrukes før nye bygges.

Arkitekturverdien er sporbarhet mellom mål, kapabiliteter, ressurser og tiltak, og et felles begrepsapparat for evner som tolkes likt på tvers av virksomheter.

## Konsekvens ved manglende bruk eller avvik
Hvis kartet ikke brukes, bygger analyser, veikart og prioriteringer lettere på ulike begreper og ulikt begrunnelsesnivå. Da blir det vanskeligere å sammenligne tiltak og se felles behov.

Fordi kartet endres mellom versjoner, kan analyser som bygger på ulike versjoner bruke forskjellige navn og definisjoner uten at det er synlig.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Modenhet | Kartet framstilles som mer ferdig enn det er | Feil forventninger og svak tillit | Oppgi hvilken dato modellen er hentet fra |
| Endringsstyring | Kapabiliteter kan endre navn og definisjon mellom versjoner | Koblinger og analyser blir inkonsistente | Versjonere avledede kopier og kontrollere mot siste modellfil |
| Forankring | Ingen formell forpliktelse eller beslutningsarena er dokumentert | Lav sammenlignbarhet mellom virksomheters analyser | Bruke kartet aktivt i samordnings- og casearbeid |
| Abstraksjon | Kartet blir brukt som katalog framfor som grunnlag for gapanalyse | Lav styringsverdi | Knytte kartet til konkrete case og prioriteringer |

## Publiseringsform og tilgjengelighet
Kartet publiseres åpent i repositoriet `digdir/nasjonal-arkitektur` på GitHub, som ArchiMate-modell, YAML og Turtle, og som dokumentasjonsside og interaktiv modell på digdir.github.io.

**Lisens:** `MIT` for repositoriet. **Deduksjon:** Lisensfila gjelder repositoriet som helhet, og det er ikke sagt uttrykkelig om den også er ment å gjelde modellinnholdet.

## Støtter arkitekturprinsipper
- **P2: Ta arkitekturbeslutninger på rett nivå** ved å tydeliggjøre hvilke evner som må løses felles og hvilke som kan løses lokalt.
- **P5: Del og gjenbruk løsninger** ved å synliggjøre hvor eksisterende ressurser dekker en kapabilitet, slik at nye tiltak ikke dupliserer dem.
- **P6: Lag digitale løsninger som støtter samhandling** ved å gi et felles språk for evnene som må styrkes på tvers av aktører.

Spenning og begrensning: Prinsippstøtten realiseres bare hvis kartet faktisk brukes i analyse og prioritering. Det er en spenning mellom smidig utvikling og behovet for forutsigbar styring: endres kartet ofte, mister det autoritet som felles referanse; fastsettes det for tidlig, mister det praksisnærhet.

## Lenke til dokumentasjon
- https://digdir.github.io/nasjonal-arkitektur/
- https://github.com/digdir/nasjonal-arkitektur
- https://www.digdir.no/digitalisering-og-samordning/en-mer-praksisnaer-nasjonal-arkitektur/8163
- https://www.digdir.no/digitaliseringsradet/digdir-nasjonal-arkitektur-samhandling-og-tjenesteutvikling-i-offentlig-sektor/8079

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-09-25
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-25
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-25
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-09-25
- https://digdir.github.io/nasjonal-arkitektur/ , kontrollert 2026-09-25
- https://github.com/digdir/nasjonal-arkitektur , innhold, modellfiler og lisens kontrollert 2026-09-25
- https://www.digdir.no/digitalisering-og-samordning/en-mer-praksisnaer-nasjonal-arkitektur/8163 , kontrollert 2026-09-25
- https://www.digdir.no/digitaliseringsradet/digdir-nasjonal-arkitektur-samhandling-og-tjenesteutvikling-i-offentlig-sektor/8079 , kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/nasjonal-arkitektur-standarder-og-informasjonsforvaltning/2150 , kontrollert 2026-09-25; siden omtaler ikke kapabilitetskartet og er fjernet som dokumentasjonslenke

## Endringer fra forrige versjon

### Analyseforbedringer
- `Status/Livsfase` er oppdatert. `v2` beskrev kartet som et arbeidsspor uten ferdig produkt. Kartet er nå publisert som datert arbeidsversjon i Digdirs repositorium `digdir/nasjonal-arkitektur`, med dokumentasjonsside, tre nivåer og modellfiler fra 2026-05-20 til 2026-09-02.
- `Kort beskrivelse` og `Normerende innhold` beskriver nå selve kartet: nivåene, skillet mellom kapabiliteter og ressurser, formatene og hva som følger med hver kapabilitet. `v2` beskrev arbeidsløpet rundt kartet.
- Forpliktelsesnivået sier nå eksplisitt at det ikke finnes rettslig forankring, etter regelen fra 2026-09-13.
- `Informasjonsforvaltning: Datastyring` er tatt ut, fordi kartet ikke forvalter dataressurser. `Strategisk styring: Arkitekturstyring` har fått forklaring og fullt navn. `v2` hadde begge punktene uten forklaring.
- `Forvaltningsmodell` og `Publiseringsform og tilgjengelighet` bygger nå på repositoriet, og delfeltet `**Lisens:**` er lagt inn.
- `Relasjon til andre ressurser` har fått ressurs-ID-er, og Digitaliseringsrådets anbefalingsbrev og de overordnede arkitekturprinsippene er lagt til.
- Siden om nasjonal arkitektur, standarder og informasjonsforvaltning er fjernet som dokumentasjonslenke fordi den ikke omtaler kartet, og dokumentasjonssiden og repositoriet er lagt til.

### Tekstlige forbedringer
- Formuleringer som «Det viktigste kvalitetsløftet fra nyere kilder er», «Dette er en viktig presisering», «gjør ressursen mer relevant som beslutningsstøtte» og vurderingen av om kartet dupliserer `capabilities.yaml` er fjernet. De beskrev beskrivelsens egen historikk og ressursens verdi, ikke ressursen.
- Fakta, deduksjon og det som ikke er offentlig dokumentert, er merket.
