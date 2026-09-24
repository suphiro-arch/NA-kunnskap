# Core Vocabularies

## Navn
Core Vocabularies

## Ressurs ID
EU-008

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Semantiske kjernemodeller med tilhørende anvendelsesprofiler

## Status/Livsfase
Aktiv. Vokabularene forvaltes gjennom SEMIC på Interoperable Europe-portalen, med åpen utvikling i offentlige kodelager.

**Fakta:** Versjon 2.0.0 ble publisert i april 2021 etter offentlige høringsrunder. Kildene i denne arbeidsøkten oppgir ikke en nyere samlet versjon for hele settet.

## Kort beskrivelse
Core Vocabularies er et sett forenklede, gjenbrukbare og utvidbare datamodeller som beskriver de grunnleggende egenskapene ved sentrale dataenheter i offentlig forvaltning, uavhengig av hvilken sammenheng de brukes i. Settet omfatter åtte vokabularer, blant dem Core Person for personopplysninger, Core Business, også kalt Registered Organization, for juridiske enheter, Core Location for adresser og geografi, Core Criterion and Core Evidence for krav og dokumentasjon, Core Public Service for offentlige tjenester, Core Public Organisation for offentlige virksomheter, Core Assessment for vurderinger og Core Standards and Specifications for standarder.

Vokabularene er kontekstnøytrale. De sier hva en person, en virksomhet eller en tjeneste minst består av, og lar den enkelte sektoren utvide modellen med sitt eget. Det er i den utvidelsen anvendelsesprofilene kommer inn, som CPSV-AP for offentlige tjenester.

## Formål og normerende rolle
Formålet er semantisk interoperabilitet: at data utvekslet mellom europeiske forvaltninger betyr det samme hos mottakeren som hos avsenderen. Vokabularene skal påvirke hvordan informasjonsmodeller utformes, hvordan registre eksponerer data, og hvordan datasett publiseres og integreres.

Den normerende rollen er **anbefalende**. Vokabularene er et felles utgangspunkt, ikke et påbudt format. De virker gjennom at mange bygger videre på de samme kjernemodellene, slik at kartlegging mellom to sektorers modeller blir mulig uten at de er identiske. Et vokabular som brukes som grunnlag for en anvendelsesprofil, får i praksis normerende kraft gjennom profilen.

## Forpliktelsesnivå og etterlevelse
Vokabularene er **anbefalte**, ikke obligatoriske. Det finnes ingen plikt i norsk rett til å bruke dem, og ingen hjemmel som gjør dem bindende.

Indirekte binding kan oppstå på to måter. Den ene er gjennom rettsakter som forutsetter bestemte datamodeller, slik utveksling under `Once-Only Technical System` gjør. Den andre er gjennom forordning (EU) 2024/903, som pålegger å identifisere relevante Interoperable Europe-løsninger i en interoperabilitetsvurdering. Plikten gjelder da å vurdere vokabularene, ikke å bruke dem.

Etterlevelse skjer gjennom arkitekturarbeid og informasjonsforvaltning: vokabularene tas i bruk når en informasjonsmodell utformes, ikke som et etterkontrollpunkt. Avvik krever ingen godkjenning, men bør begrunnes når data skal utveksles over landegrenser, fordi avviket da flyttes over på mottakeren som kartleggingsarbeid.

**Deduksjon:** For norske virksomheter er den praktiske forpliktelsen i dag lav. Verdien ligger i å unngå framtidig kartleggingsgjeld, ikke i å oppfylle et krav.

## Kapabiliteter
- **Informasjonsforvaltning: Informasjonsarkitektur**
  gir felles, standardiserte modeller for hvordan sentrale dataenheter struktureres, slik at data blir finnbare, forståelige og gjenbrukbare for både mennesker og maskiner på tvers av forvaltninger.

- **Standardisering: EU standarder**
  forvalter og tilgjengeliggjør de europeiske kjernemodellene som skal tas i bruk, med dokumentert metode for utvikling og endring.

Koblingene er satt fordi vokabularene selv er modellene, og fordi SEMIC forvalter dem med en definert prosess. De registrene og tjenestene som tar modellene i bruk, leverer sine egne evner, og de hører ikke her.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Informasjonsarkitekter | Felles utgangspunkt for modellering av person, virksomhet, sted og tjeneste | Utforming av informasjonsmodeller | Viktigste brukergruppe |
| Registereiere | Eksponere data i former som kan forstås utenfor egen sektor | API-er og datasett | Særlig relevant ved grensekryssende utveksling |
| Utviklings- og integrasjonsmiljøer | Unngå å definere egne modeller for kjente begreper | Bygging av tjenester og integrasjoner | Bruker ofte en anvendelsesprofil, ikke kjernemodellen direkte |
| Miljøer som publiserer datasett | Beskrive data slik at de kan finnes og forstås | Datakataloger og åpne data | Kombineres med anvendelsesprofiler for datakataloger |
| SEMIC og Core Vocabularies-arbeidsgruppen | Forvalte og videreutvikle modellene | Endringsprosess | Eier metoden og prosessen |

## Normerende innhold
Hvert vokabular definerer et lite sett med klasser og egenskaper for sin dataenhet, med tydelige definisjoner og avgrensninger. Core Person beskriver de grunnleggende egenskapene ved en person. Core Business, også kjent som Registered Organization, modellerer juridiske enheter med navn, aktivitet og identifikatorer. Core Location dekker adresser, stedsnavn og geometri, og er samordnet med INSPIRE-spesifikasjonene. Core Criterion and Core Evidence beskriver hvilke krav en aktør må oppfylle for å ha rett til en offentlig tjeneste, og hvilken dokumentasjon som kan vise det.

Core Public Service beskriver offentlige tjenester og har anvendelsesprofilen CPSV-AP, som utvider modellen for å beskrive tjenester knyttet til livshendelser og forretningshendelser. Core Public Organisation modellerer offentlige virksomheter på tvers av EU. Core Assessment gir et domeneuavhengig rammeverk for vurderinger basert på kriterier, og Core Standards and Specifications gjør det mulig å utveksle informasjon om standarder mellom programvareløsninger.

Det som harmoniseres, er kjernen, ikke helheten. Vokabularene er bevisst holdt små og kontekstnøytrale, slik at den enkelte sektoren kan utvide dem uten å bryte med grunnlaget. Endringer diskuteres i Core Vocabularies-arbeidsgruppen nettopp for å sikre at eksisterende implementasjoner ikke brytes.

## Bruksområde
Vokabularene bør brukes når en ny informasjonsmodell utformes, når et register skal eksponere data for andre, og når data skal utveksles over sektor- eller landegrenser. De er særlig relevante når de samme begrepene, som person, virksomhet og sted, dukker opp i flere modeller og risikerer å bli definert ulikt hver gang.

De er også et praktisk verktøy i kartlegging: to eksisterende modeller kan sammenlignes gjennom kjernemodellen framfor direkte mot hverandre.

## Typiske analyse- og beslutningssituasjoner
- Utforming av informasjonsmodell eller begrepsapparat i et nytt løsningsløp.
- Vurdering av om et register kan levere data til grensekryssende tjenester uten omfattende tilpasning.
- Anskaffelser der kravene til datamodell og datautveksling skal formuleres.
- Arbeid med tjenestebeskrivelser og tjenestekataloger, der CPSV-AP er relevant.
- Interoperabilitetsvurdering etter artikkel 3 i forordning (EU) 2024/903, der semantiske løsninger skal identifiseres.

## Når ressursen normalt ikke er tilstrekkelig alene
Vokabularene er kjernemodeller og dekker bevisst lite. De må suppleres med:
- Anvendelsesprofiler for det aktuelle domenet, som CPSV-AP for tjenester eller profiler for datakataloger.
- Nasjonale begreps- og informasjonsmodeller, siden norske registerbegreper ofte har rettslig innhold som kjernemodellen ikke fanger.
- Nasjonale grunndataressurser, som Folkeregisteret og Enhetsregisteret, som definerer hva en person og en virksomhet faktisk er i norsk forvaltning.
- Juridisk vurdering av hvilke opplysninger som kan deles, som semantikken ikke sier noe om.

## Scope og avgrensning
Omfatter: åtte kontekstnøytrale kjernevokabularer med klasser, egenskaper og definisjoner, dokumentert metode for utvikling og endring, og tilhørende anvendelsesprofiler som CPSV-AP.

Omfatter ikke: sektorspesifikke datamodeller, rettslige definisjoner i nasjonal lovgivning, transport og utveksling av data, og kvalitetssikring av de dataene som beskrives.

Grensen mot `Interoperable Europe Solutions` går på nivå: vokabularene er én av løsningene som katalogen viser til. Grensen mot nasjonale informasjonsmodeller går på autoritet: norske registre definerer innholdet i norsk rett, mens vokabularene gir en felles europeisk struktur å uttrykke det i.

## Forvaltningsmodell
Faglig ansvar ligger hos SEMIC, som er Kommisjonens arbeid for semantisk interoperabilitet og som har sin opprinnelse i ISA²-programmet. SEMIC vedlikeholder vokabularene etter en dokumentert prosess og metode for utvikling av kjernevokabularer.

Endringsprosessen går gjennom Core Vocabularies-arbeidsgruppen. Endringer diskuteres der før de gjennomføres, med det uttalte formålet å unngå at eksisterende implementasjoner brytes. Utviklingen skjer åpent i offentlige kodelager, med egne repositorier for person, virksomhet, sted, offentlig organisasjon og kriterier og dokumentasjon.

Publisering skjer gjennom Interoperable Europe-portalen. Løsningene er gjort tilgjengelige under European Union Public Licence.

**Ikke offentlig dokumentert i denne arbeidsøkten:** gjeldende versjonsnummer per enkeltvokabular og fast utgivelsesfrekvens.

## Relasjon til andre ressurser
- `Interoperable Europe Solutions` (`EU-007`) er katalogen vokabularene publiseres og finnes gjennom.
- `Interoperable Europe Act` (`EU-009`) etablerer plikten til å vurdere relevante løsninger, som omfatter semantiske løsninger.
- `Once-Only Technical System` (`EU-005`) bygger på felles datamodeller for at bevis skal kunne forstås på tvers av land.
- Nasjonalt er `Folkeregisteret` og `Enhetsregisteret` de autoritative kildene for det innholdet Core Person og Core Business strukturerer.
- `Rammeverk for nasjonale grunndata` og `Orden i eget hus` er de norske ressursene som dekker tilsvarende behov for struktur og informasjonsforvaltning.

## Forretningsverdi og arkitekturverdi
Vokabularene gir felles forståelse av begreper som ellers defineres på nytt i hvert prosjekt. Når person, virksomhet og sted er modellert likt i utgangspunktet, faller mye av diskusjonen om grunnleggende struktur bort.

De gir sammenlignbarhet mellom modeller fra ulike sektorer og land, fordi kartleggingen kan gå gjennom en felles kjerne framfor å være bilateral.

De reduserer tolkningsrommet i datautveksling: en mottaker som kjenner kjernemodellen, vet hva feltene betyr uten å lese avsenderens dokumentasjon.

For arkitekturarbeid er verdien størst tidlig. Å ta inn kjernemodellene når en informasjonsmodell utformes koster lite; å kartlegge mot dem i etterkant koster vesentlig mer.

## Konsekvens ved manglende bruk eller avvik
Uten felles kjernemodeller får hver sektor sin egen definisjon av de samme begrepene. Kostnaden dukker opp ved første grensekryssende eller tverrsektorielle utveksling, i form av kartleggingsarbeid som må gjøres for hvert par av modeller.

Brukt for sent blir vokabularene et konverteringslag framfor et fundament, med den datakvalitetsrisikoen som følger av at opplysninger må tolkes og omformes.

Ulik tolkning av de samme begrepene gir også svakere sammenlignbarhet i analyser og statistikk på tvers av virksomheter.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Semantisk kvalitet | Kjernemodellene er bevisst små og dekker lite alene | Miljøer opplever dem som utilstrekkelige og velger egne modeller | Bruk anvendelsesprofiler i stedet for å forkaste kjernen |
| Adopsjon | Lav kjennskap i norske fagmiljøer | Nye modeller utformes uten kobling til europeisk semantikk | Ta dem inn i maler for informasjonsmodellering |
| Endringsstyring | Versjonsstatus per vokabular er ikke lett å lese ut av kildene | Usikkerhet om hva som er gjeldende | Oppgi versjon og hentedato ved bruk |
| Forankring | Ingen rettslig plikt til bruk i Norge | Vokabularene taper mot nasjonale begreper med rettslig innhold | Bruk dem som struktur, ikke som erstatning for rettslige definisjoner |
| Sammenheng med løsninger | Norske registerbegreper lar seg ikke alltid uttrykke i kjernemodellen | Informasjonstap ved utveksling | Dokumenter utvidelser eksplisitt framfor å tvinge innholdet inn |

## Publiseringsform og tilgjengelighet
Vokabularene publiseres på Interoperable Europe-portalen under SEMIC, med dokumentasjon og spesifikasjoner fritt tilgjengelig uten innlogging. Utviklingen foregår åpent i offentlige kodelager, der forslag og endringer kan følges og kommenteres.

Løsningene er gjort tilgjengelige under European Union Public Licence.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Felles semantikk er forutsetningen for at delte data faktisk kan brukes av mottakeren, ikke bare overføres.
- **P6: Lag digitale løsninger som støtter samhandling**
  Vokabularene dekker den semantiske dimensjonen av samhandling, som er den som oftest svikter når det tekniske allerede virker.
- **P5: Del og gjenbruk løsninger**
  Modellene er selv gjenbrukbare komponenter, publisert under en åpen lisens og utviklet i åpne kodelager.

**Spenning og begrensning:** Vokabularene støtter **P1: Ta utgangspunkt i brukernes behov** bare indirekte, og kan i praksis stå i spenning mot det: en modell som er kontekstnøytral for hele Europa, treffer sjelden en norsk brukergruppes begrepsbruk presist. De står også i spenning mot **P2: Ta arkitekturbeslutninger på rett nivå**, siden nasjonale registerbegreper med rettslig innhold ikke uten videre lar seg presse inn i en felles europeisk kjerne. Når et norsk begrep har innhold som kjernemodellen ikke dekker, skal utvidelsen dokumenteres framfor at innholdet tilpasses modellen.

## Lenke til dokumentasjon
- Core Vocabularies: https://interoperable-europe.ec.europa.eu/collection/semic-support-centre/solution/core-vocabularies
- Interoperable Europe Solutions: https://interoperable-europe.ec.europa.eu/interoperable_solutions
- Interoperable Europe Act: https://interoperable-europe.ec.europa.eu/Interoperable-Europe-Act-Regulation

## Kildegrunnlag brukt i utfyllingen
- Europakommisjonen, SEMIC, Core Vocabularies, hentet 24. september 2026.
- Europakommisjonen, Interoperable Europe Act, artikkel 3, hentet 24. september 2026.
- Lokale kilder: `arkitektur/ressurser/produktnummerering.md`, `arkitektur/kapabiliteter/capabilities.yaml`, `arkitektur/prinsipper/principles.md`, `sources/links.md`.
