# EU Open Source Solutions Catalogue

## Navn
EU Open Source Solutions Catalogue

## Ressurs ID
EU-006

## Status/Livsfase
**Produksjon** - katalogen er i drift på Interoperable Europe-portalen og utvides med nye nasjonale kataloger.

**Fakta:** Katalogen ble lansert i mars 2025 med om lag 600 løsninger hentet fra fem åpen kildekode-kataloger. Etter fem måneder inneholdt den nærmere 800 løsninger fra åtte kataloger, med kataloger fra blant annet Finland, Belgia og Sverige og fra EU-institusjoner koblet på.

## Modenhet
**Moden som publiseringsflate, tidlig som beslutningsgrunnlag.**

- Teknisk: katalogen er bygget som en føderert løsning som henter innhold fra nasjonale og lokale kataloger gjennom åpne grensesnitt, framfor at hver løsning registreres manuelt sentralt.
- Metadata: oppføringer klargjøres med `publiccode.yml`, som er et maskinlesbart metadataformat for offentlig programvare.
- Innholdsmessig: katalogen viser aktivitetsmål som nedlastinger, forgreninger og fellesskapsaktivitet, men er en katalog og ikke en kvalitetsvurdering.
- Organisatorisk: modellen forutsetter at et land har en nasjonal katalog som oppfyller tekniske og forvaltningsmessige kriterier.

**Deduksjon:** Det svakeste leddet er tilfanget fra land som ikke har en nasjonal katalog. Så lenge norske løsninger ikke har en norsk katalog å bli hentet fra, vil norsk programvare være underrepresentert uavhengig av hvor gjenbrukbar den er. Kildene i denne arbeidsøkten sier ikke om Norge har en slik katalog.

## Kort beskrivelse
EU Open Source Solutions Catalogue er Europakommisjonens samlede katalog over åpen kildekode-løsninger laget av og for europeisk offentlig sektor. Katalogen samler innhold fra nasjonale og lokale kataloger i én flate, slik at en offentlig virksomhet kan lete etter eksisterende løsninger på tvers av land framfor å søke i hvert lands egen oversikt.

Katalogen er en oppdagelsesflate, ikke en distribusjonsplattform. Den peker videre til det stedet løsningen faktisk forvaltes, og den vurderer ikke om en løsning er egnet for et bestemt formål.

## Kapabiliteter
- **Tjenesteutvikling: Gjenbrukbare tjenester**
  gjør det praktisk mulig å finne løsninger som allerede er utviklet i offentlig sektor i andre land, som et alternativ til å utvikle eller anskaffe på nytt.

- **Informasjonsforvaltning: Oversikt over tjenester**
  gir en samlet, søkbar oversikt over programvare som tilbys av eller på vegne av offentlig sektor i Europa, med maskinlesbare metadata.

Koblingene er satt fordi katalogen selv leverer oversikten og aggregeringen. Selve løsningene den peker til, forvaltes av andre, og evnene de leverer hører hos dem.

## Produktmål
**Dokumenterte mål** slik Kommisjonen beskriver katalogen:
- Gi én samlet flate for å oppdage åpen kildekode-løsninger for europeisk offentlig sektor.
- Samle nasjonale og lokale kataloger som oppfyller tekniske og forvaltningsmessige kriterier.
- Støtte samarbeid og effektivitet gjennom gjenbruk av åpne løsninger.

**Utledede operative mål:**
- Redusere dobbeltutvikling ved at samme behov ikke løses parallelt i flere land.
- Gjøre gjenbruksplikten i Interoperable Europe Act praktisk gjennomførbar ved å gi et sted å lete.

## Brukerbehov
- Offentlige virksomheter trenger å vite om noen allerede har løst behovet, før de starter anskaffelse eller utvikling.
- Arkitektur- og innkjøpsmiljøer trenger et utgangspunkt for markedsdialog som ikke bare består av kommersielle leverandører.
- Utviklingsmiljøer trenger å finne komponenter de kan bygge videre på, med lisens og forvaltning oppgitt.
- Forvaltere av nasjonale kataloger trenger en kanal for å gjøre egne løsninger synlige utover eget land.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter | Finne eksisterende løsninger før utvikling | Tidligfase, konseptvalg, anskaffelse | Primærbruker av katalogen |
| Arkitektur- og innkjøpsmiljøer | Kartlegge alternativer og lisensvilkår | Behovsvurdering og markedsdialog | Bruker katalogen som ett av flere grunnlag |
| Utviklingsmiljøer | Finne komponenter og vurdere aktivitet i prosjektet | Utvikling og videreutvikling | Ser på aktivitetsmål og repositorium |
| Forvaltere av nasjonale kataloger | Få egne løsninger synlige i Europa | Publisering gjennom egen katalog | Må oppfylle kriteriene for tilkobling |
| Europakommisjonen | Drifte og utvide den felles katalogen | Aggregering og portalflate | Eier katalogen |

## Hovedfunksjoner
Den første hovedfunksjonen er **aggregering fra nasjonale kataloger**. Katalogen henter innhold gjennom åpne grensesnitt fra nasjonale og lokale kataloger som oppfyller fastsatte kriterier, framfor å være et sted hver enkelt løsning registreres manuelt. Det betyr at veien inn i katalogen normalt går gjennom en nasjonal katalog, ikke direkte.

Den andre er **søk og filtrering**. Løsningene kan finnes etter kategori og bruksområde, og oppføringene viser metadata om hva løsningen er, hvem som forvalter den og hvor koden ligger. Metadataene er basert på `publiccode.yml`, som gjør oppføringene maskinlesbare og mulige å gjenbruke i andre oversikter.

Den tredje er **innsyn i aktivitet**. Oppføringene viser mål som nedlastinger, forgreninger og fellesskapsaktivitet. Dette er et grovt, men nyttig signal for om et prosjekt lever, og er ofte det første en vurdering av gjenbruk må avklare.

Den fjerde er **kobling til resten av Interoperable Europe-portalen**. Katalogen er én av flere publiseringsveier på portalen, ved siden av den bredere løsningskatalogen og betegnelsen `Interoperable Europe Solution` som styret tildeler. Skillet er verdt å kjenne: oppføring i åpen kildekode-katalogen er ikke en anbefaling fra styret.

### Typiske brukssituasjoner (generisk)
- En virksomhet skal vurdere om et behov kan dekkes av eksisterende offentlig programvare før anskaffelse startes.
- Et utviklingsmiljø leter etter en komponent å bygge videre på, med kjent lisens.
- En virksomhet skal dokumentere at gjenbruk er vurdert, som del av et interoperabilitetsarbeid.

### Når EU Open Source Solutions Catalogue normalt ikke er førstevalg
- Når behovet er å finne norske fellesløsninger. Da er Digdirs egen oversikt over fellesløsninger og denne ressursoversikten mer treffsikre.
- Når løsningen skal settes i drift raskt uten egen utviklingskapasitet. Katalogen peker til kode, ikke til driftede tjenester.
- Når kravet er en kvalitetssikret anbefaling. Katalogen lister, den vurderer ikke.
- Når behovet gjelder spesifikasjoner, vokabularer eller rammeverk framfor programvare. Da hører søket i `Interoperable Europe Solutions`.

### Scope og avgrensning
Inngår: aggregerte oppføringer av åpen kildekode-løsninger fra tilkoblede nasjonale og lokale kataloger, med metadata, kategorier og aktivitetsmål.

Inngår ikke: hosting eller distribusjon av selve koden, kvalitetsvurdering eller godkjenning av løsningene, støtte og forvaltning av den enkelte løsningen, og lukket programvare.

## Veikart over kommende funksjonalitet
**Fakta:** Katalogen har vokst fra fem til åtte tilkoblede kataloger i løpet av de første fem månedene, med kataloger fra Finland, Sverige, Belgia og EU-institusjoner blant dem som er koblet på.

**Deduksjon:** Videre utvikling ser ut til å handle mest om å koble til flere nasjonale kataloger, ikke om nye funksjoner i selve flaten.

**Ikke offentlig dokumentert i denne arbeidsøkten:** en publisert plan for hvilke land som kobles til når, og om det stilles nye krav til metadatakvalitet.

## Forretningsverdi/Verdiforslag
**For offentlige virksomheter:** et konkret sted å lete før man utvikler eller anskaffer, som kan spare både utviklingskostnad og tid i tidligfase.

**For utviklingsmiljøer:** tilgang til komponenter med kjent lisens og synlig aktivitetsnivå, som gjør risikoen ved gjenbruk lettere å vurdere.

**For samfunnet:** mindre dobbeltarbeid i europeisk offentlig sektor, og styrket digital selvstendighet gjennom bruk av åpen kildekode.

**For norske virksomheter som forvalter åpen kildekode:** en kanal for at egne løsninger kan bli funnet og gjenbrukt utenfor Norge, forutsatt at de er tilgjengelige gjennom en tilkoblet katalog.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Dekning | Land uten nasjonal katalog blir underrepresentert | Modellen forutsetter nasjonale kataloger; norsk status er ikke dokumentert i denne arbeidsøkten |
| Kvalitet | Oppføring sier ingenting om at løsningen er egnet, sikker eller vedlikeholdt | Aktivitetsmål gir et signal; reell vurdering må gjøres mot repositoriet |
| Metadata | Ujevn kvalitet på `publiccode.yml` gir ujevn søkbarhet | Onboardingkrav finnes; håndheving er ikke dokumentert i denne arbeidsøkten |
| Lisens | Lisensvilkår må kontrolleres mot repositoriet, ikke mot katalogoppføringen | Følger repoets egen regel om at repositoriet går foran tredjepartsomtale |
| Forvaltning | En løsning kan være forlatt uten at katalogoppføringen sier det | Uavklart. Sjekk siste aktivitet i repositoriet |

## Kanaler
Katalogen er en nettflate på Interoperable Europe-portalen, uten innlogging for å søke og lese. Publisering går normalt gjennom en nasjonal eller lokal katalog som er koblet til, og aggregeringen skjer maskinelt gjennom åpne grensesnitt.

**Ikke offentlig dokumentert i denne arbeidsøkten:** om katalogen tilbyr et offentlig grensesnitt for å hente ut hele innholdet til bruk i andre oversikter.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** driftsmodell og plattform. Det som er kjent, er at katalogen driftes av Europakommisjonen som del av Interoperable Europe-portalen, og at arkitekturen er føderert med innhenting fra eksterne kataloger.

## Gjenbruk
Katalogens hele formål er gjenbruk, og den er selv bygget på åpne grensesnitt og et maskinlesbart metadataformat. Metadataene i `publiccode.yml` gjør det mulig for andre kataloger å bruke de samme oppføringene.

Avhengigheter som ikke er kapabiliteter her: innholdet kommer fra nasjonale og lokale kataloger, og selve løsningene forvaltes av sine respektive eiere.

**Vanlige kombinasjoner med andre produkter:**
- `Interoperable Europe Solutions` for spesifikasjoner, vokabularer og rammeverk, og for løsninger som styret har gitt betegnelsen `Interoperable Europe Solution`.
- `Interoperable Europe Act`, som etablerer plikten til å dele og vurdere gjenbruk av interoperabilitetsløsninger.
- `Assessment Toolbox`, når gjenbruksvurderingen inngår i en interoperabilitetsvurdering.

**Kildekode:** Ikke offentlig dokumentert. Kildene i denne arbeidsøkten sier ikke om katalogplattformen selv publiseres som åpen kildekode. Løsningene katalogen viser til, er derimot åpen kildekode.

**Lisens:** Ikke offentlig dokumentert for selve katalogplattformen.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger**
  Dette er katalogens hovedformål, og den er den mest direkte europeiske støtten til prinsippet: et felles sted å finne løsninger andre allerede har laget.
- **P2: Ta arkitekturbeslutninger på rett nivå**
  Støttes delvis. Katalogen gir grunnlag for å se om et behov er løst andre steder, slik at valget mellom egen utvikling og gjenbruk kan tas på et informert grunnlag.
- **P6: Lag digitale løsninger som støtter samhandling**
  Støttes indirekte ved at felles bruk av samme løsninger gjør samhandling enklere.

**Spenning og begrensning:** Katalogen støtter **P7: Sørg for tillit til oppgaveløsningen** svakt. En oppføring er ikke en kvalitetssikring, og en virksomhet som legger katalogen til grunn uten egen vurdering av sikkerhet, forvaltning og lisens, tar en risiko katalogen ikke dekker. Den er også i praktisk spenning mot **P1: Ta utgangspunkt i brukernes behov**: gjenbruk av en løsning laget for et annet lands forvaltningsmodell kan gi dårlig brukertilpasning hvis den overtas uten tilpasning. For et konkret case bør katalogen brukes til å finne kandidater, ikke til å konkludere.

## Finansiering
**Fakta:** Katalogen driftes og finansieres av Europakommisjonen som del av Interoperable Europe-portalen, og er fritt tilgjengelig.

**Ikke offentlig dokumentert i denne arbeidsøkten:** om det påløper kostnader for et land som vil koble til en nasjonal katalog.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Europakommisjonen | Interoperable Europe-portalen, EU OSS Catalogue |
| Innholdsansvar per oppføring | Den nasjonale eller lokale katalogen løsningen kommer fra | Kommisjonens beskrivelse av føderert modell |
| Forvaltning av den enkelte løsningen | Løsningens egen eier | Følger av at katalogen bare peker videre |
| Budsjettansvar | Europakommisjonen | Deduksjon fra at katalogen er del av portalen |
| Styringsmodell | Ikke offentlig dokumentert i denne arbeidsøkten | - |

## Lenke til dokumentasjon
- EU Open Source Solutions Catalogue: https://interoperable-europe.ec.europa.eu/eu-oss-catalogue
- Nyhetssak om lansering av katalogen: https://interoperable-europe.ec.europa.eu/interoperable-europe/news/eu-open-source-solutions-catalogue-now-live
- Interoperable Europe Solutions: https://interoperable-europe.ec.europa.eu/interoperable_solutions

## Kildegrunnlag brukt i utfyllingen
- Europakommisjonen, EU Open Source Solutions Catalogue, hentet 24. september 2026.
- Europakommisjonen, nyhetssaker om lansering og vekst i katalogen, hentet 24. september 2026.
- Lokale kilder: `arkitektur/ressurser/produktnummerering.md`, `arkitektur/kapabiliteter/capabilities.yaml`, `arkitektur/prinsipper/principles.md`, `sources/links.md`.
