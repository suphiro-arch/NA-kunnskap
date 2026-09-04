# Felles informasjonsmodeller

## Navn
Felles informasjonsmodeller

## Ressurs ID
DIGDIR-069

## Ressurskategori
Normerende ressurs

## Type standard eller veiledning
Prinsipper og modelleringsregler for informasjonsmodellering

## Status/Livsfase
Aktiv. Prinsippene og modelleringsreglene er publisert og i bruk som Digdirs føringer for informasjonsmodellering i offentlig forvaltning.

## Kort beskrivelse
Felles informasjonsmodeller er Digdirs føringer for hvordan informasjonsmodeller i offentlig forvaltning bør utformes, dokumenteres og gjøres tilgjengelige. Modellene skal være uavhengige av et bestemt IT-verktøy, deles i gjenbrukbare moduler og publiseres på standardformater, slik at de kan brukes videre av andre enn den som laget dem.

Ressursen består av to hoveddeler. Ni grunnleggende designprinsipper sier hvilke egenskaper en modell skal ha. Et sett felles modelleringsregler er mer konkret og sier hvordan navngiving, identifikatorer, dokumentasjon, formater og gjenbruk av modellelementer bør håndteres.

Poenget med felles føringer er sammenlignbarhet. Når virksomheter modellerer på ulike måter, blir modellene vanskelige å lese på tvers, og gjenbruk krever tolkningsarbeid i hvert enkelt tilfelle. Prinsippene og reglene skal gjøre modellene mest mulig ensartet, slik at de kan leses, sammenlignes og gjenbrukes.

## Formål og normerende rolle
Formålet er å etablere felles designgrunnlag for informasjonsmodeller som skal deles på tvers av offentlige virksomheter. De etablerte fellesmodellene er kjernemodeller: en overordnet modell for Person og Enhet, med koblinger til identifikasjon og adresse, og en egen modell for Adresse. Begge er utarbeidet av arbeidsgrupper med deltakere fra flere offentlige virksomheter, og de brukes som eksempler i modelleringsreglene.

Den normerende rollen er å påvirke hvordan modeller utformes, ikke å bestemme hvilke modeller som skal finnes. Ressursen sier noe om form, dokumentasjon og tilgjengeliggjøring, og lar det faglige innholdet ligge hos den som eier modellen.

## Forpliktelsesnivå og etterlevelse
Modelleringsreglene er anbefalinger, ikke krav. Digdir omtaler dem som regler virksomheter bør vurdere når de etablerer egen modelleringspraksis eller samarbeider på tvers.

Etterlevelse skjer i praksis gjennom to kanaler. Den ene er faglig veiledning og eget arkitekturarbeid i virksomheten. Den andre er publisering: reglene forutsetter at modeller beskrives etter spesifikasjonen ModellDCAT-AP-NO og gjøres tilgjengelige i Felles datakatalog, og den som publiserer der møter et mer konkret formatkrav enn prinsippene alene innebærer.

Det finnes ingen tilsyns- eller kontrollordning knyttet til reglene, og kildene beskriver ingen mekanisme for å begrunne avvik. Nivået er dermed anbefalt, ikke styrende.

## Kapabiliteter
- **Informasjonsforvaltning: Informasjonsarkitektur**
  Ressursen er selve føringsgrunnlaget for hvordan informasjon struktureres og modelleres på en standardisert måte, slik at data blir forståelige og gjenbrukbare på tvers av virksomheter.

- **Informasjonsforvaltning: Oversikt over informasjonsmodeller**
  Reglene krever at modeller dokumenteres, dateres, ansvarsplasseres og publiseres maskinlesbart i Felles datakatalog, som er det som gjør modellene mulige å finne og forstå på tvers.

- **Standardisering: Forvaltningsstandarder**
  Ressursen operasjonaliserer nasjonale standarder for modellbeskrivelse, blant annet ModellDCAT-AP-NO og standardiserte datatyper fra XSD, RDFS og ISO/TC 211.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Informasjonsarkitekter og modellansvarlige | Felles designgrunnlag for egne modeller | Etablering og revisjon av informasjonsmodeller | Primærmålgruppen |
| Virksomheter som deler data | Modeller andre kan tolke korrekt | Publisering i Felles datakatalog | Reglene om maskinlesbarhet og dokumentasjon er avgjørende her |
| Virksomheter som skal gjenbruke data | Kunne lese og sammenligne andres modeller | Vurdering av om et datasett dekker eget behov | Nytten kommer indirekte, gjennom at andre følger reglene |
| Anskaffelses- og prosjektmiljøer | Kravgrunnlag for modellarbeid | Kravstilling til leverandør | Deduksjon: bruken i anskaffelser er ikke beskrevet eksplisitt i kildene |
| Domenesamarbeid på tvers av sektorer | Omforent modelleringspraksis | Felles modeller for et fagområde | Kjernemodellene for Person og Enhet og for Adresse er laget på denne måten |

## Normerende innhold
**Ni designprinsipper.** Modellene skal være sammenhengende på tvers av modelleringsfaser og abstraksjonsnivåer. De skal være så enkle som mulig til å dekke behovet, og forståelige for målgruppen. De skal bygge på eksisterende begreper og definisjoner så langt det er mulig. De skal ha dokumentasjon som kan presenteres for aktuelle målgrupper, og gjøres tilgjengelige på standardformater. De skal legge til rette for gjenbruk og utveksling av data både internt og mellom virksomheter. De skal deles i gjenbrukbare moduler. De skal være stabile og utvidbare, med nye versjoner utviklet gjennom en definert forvaltning. Og de skal ikke være avhengige av bestemte verktøy.

**Felles modelleringsregler.** Reglene er gruppert i tre nivåer:

- *Generelle regler* om forståelighet og meningsbærende navngiving, skrivemåte for datastrukturer, og persistente identifikatorer i form av URI-er.
- *Regler for informasjonsmodellen* om visuell representasjon, modularitet og tilgjengeliggjøring, maskinlesbarhet i åpne formater, datering, ansvar og status, og hvordan relasjoner mellom modeller uttrykkes.
- *Regler for elementer og egenskaper* om begrepsdokumentasjon, gjenbruk av eksisterende modellelementer, og bruk av standardiserte datatyper.

**Modellspråk.** Reglene krever ikke et bestemt modellspråk, men anbefaler et språk som gir god visuell representasjon. UML-klassediagram nevnes som eksempel. Føringene er dermed teknologinøytrale på modellspråk, men konkrete på publiseringsformat.

**Kobling til ModellDCAT-AP-NO.** Spesifikasjonen er det bærende elementet for maskinlesbarhet. Den skiller mellom begrepsmodell, logisk modell og fysisk modell, og gir et felles vokabular for modellklassifisering.

## Bruksområde
Ressursen bør brukes når en virksomhet etablerer eller reviderer en informasjonsmodell som skal kunne leses eller gjenbrukes av andre. Den er særlig relevant når flere virksomheter skal samarbeide om en domenemodell, og når en modell skal publiseres i Felles datakatalog.

Den er mindre relevant for rent interne modeller uten deling, men prinsippene om verktøyuavhengighet og stabilitet har verdi også der.

## Typiske analyse- og beslutningssituasjoner
- Vurdering av om en eksisterende modell kan gjenbrukes framfor å bygge en ny
- Etablering av felles domenemodell mellom flere virksomheter
- Kravstilling til modellarbeid i anskaffelser og utviklingsprosjekter
- Vurdering av om et datasett er dokumentert godt nok til å kunne tolkes riktig i en tverrgående tjeneste
- Avklaring av versjonering og forvaltning før en modell tas i bruk av flere

## Når ressursen normalt ikke er tilstrekkelig alene
Ressursen gir form, ikke innhold. Den sier hvordan en modell bør utformes, men ikke hva den skal inneholde. Faglig modellinnhold må hentes fra domenet.

For begrepsarbeid må ressursen suppleres med begrepsforvaltning og `Begrepskatalog` (`DIGDIR-012`). For selve publiseringen kreves ModellDCAT-AP-NO og `Felles datakatalog` (`DIGDIR-011`). For det bredere styringsgrunnlaget rundt informasjonsforvaltning gjelder `Rammeverk for informasjonsforvaltning` (`DIGDIR-029`) og `Orden i eget hus` (`DIGDIR-036`).

Ressursen løser heller ikke juridiske spørsmål. Behandlingsgrunnlag, taushetsplikt og deling må avklares uavhengig av hvordan modellen er utformet.

## Scope og avgrensning
Inngår:
- ni designprinsipper for informasjonsmodeller
- felles modelleringsregler på tre nivåer
- føringer for navngiving, identifikatorer, dokumentasjon, datatyper og publiseringsformat
- kobling til ModellDCAT-AP-NO og til publisering i Felles datakatalog

Inngår ikke:
- faglig innhold i konkrete modeller
- valg av modelleringsverktøy
- begrepsforvaltning som eget fagområde
- juridisk vurdering av deling og behandlingsgrunnlag
- kravsetting med bindende virkning

Grensen mot `Rammeverk for informasjonsforvaltning` (`DIGDIR-029`) er nivået: rammeverket beskriver informasjonsforvaltning som styringsområde, mens denne ressursen gir konkrete føringer for én oppgave innenfor det. Grensen mot Referansekatalogen for IT-standarder (`DIGDIR-026`) er at Referansekatalogen fører standarder med formell status, mens modelleringsreglene er faglige anbefalinger.

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digdir, fagområdet informasjonsforvaltning |
| Forvaltningsansvar | Digdir |
| Endringsprosess | Ikke beskrevet i åpne kilder for prinsippene og reglene selv. ModellDCAT-AP-NO forvaltes som egen spesifikasjon med versjonering |
| Publiserings- og beslutningsarena | Digdirs nettsider under informasjonsforvaltning. Faglig arena for informasjonsforvaltning og deling av data (`DIGDIR-053`) er den naturlige arenaen for faglig behandling, men kildene bekrefter ikke at reglene besluttes der |

## Relasjon til andre ressurser
- **Felles datakatalog (`DIGDIR-011`)**
  Den operative motparten. Reglene forutsetter publisering i katalogen, og katalogen er stedet der etterlevelsen faktisk blir synlig.

- **Begrepskatalog (`DIGDIR-012`)**
  Prinsippet om terminologi krever at modeller bygger på eksisterende begreper og definisjoner. Begrepskatalogen er kilden til dem.

- **Rammeverk for informasjonsforvaltning (`DIGDIR-029`)**
  Overordnet styringsgrunnlag. Denne ressursen er den konkrete modelleringsdelen innenfor rammeverket.

- **Orden i eget hus (`DIGDIR-036`)**
  Beskriver hva en virksomhet må ha på plass internt for å forvalte informasjonen sin. Modelleringsreglene sier hvordan modellene i den ordenen bør se ut.

- **Nasjonal verktøykasse for deling av data (`DIGDIR-038`)**
  Samler veiledning om datadeling. Modelleringsreglene er en del av forutsetningene for at delte data kan tolkes riktig.

- **FINT Informasjonsmodell (`NOVARI-003`)**
  Et konkret eksempel på en sektormodell som kan vurderes mot disse føringene.

- **Faglig arena for informasjonsforvaltning og deling av data (`DIGDIR-053`)**
  Arena der modelleringspraksis diskuteres på tvers av virksomheter.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er lavere tolkningskostnad. Når modeller er dokumentert og publisert etter samme mønster, kan en virksomhet vurdere om andres data dekker eget behov uten å måtte gjennomføre et eget kartleggingsprosjekt først.

Arkitekturverdien er sammenlignbarhet og gjenbruk. Prinsippene om modularitet, verktøyuavhengighet og stabilitet gjør at modellelementer kan gjenbrukes framfor å modelleres på nytt i hver virksomhet, og at en modell overlever bytte av verktøy og leverandør.

## Konsekvens ved manglende bruk eller avvik
Uten felles føringer blir modeller låst til lokale begreper, formater og systemforståelser. Det gir høyere integrasjonskostnad hver gang data skal brukes på tvers, og kartleggingsarbeidet gjentas i hvert prosjekt.

Brukt for sent er konsekvensen dyrere. En modell som er tatt i bruk i produksjon, kan ikke navngis om eller restruktureres uten at grensesnitt og integrasjoner må endres.

Tolkes reglene ulikt, oppstår modeller som formelt følger anbefalingene men ikke lar seg sammenligne, fordi abstraksjonsnivå og modularisering er valgt forskjellig.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Adopsjon | Reglene er anbefalinger uten kontrollmekanisme | Ujevn etterlevelse, og gjenbruksverdien avhenger av at nok virksomheter følger dem | Bruke publiseringskravene i Felles datakatalog som praktisk kvalitetsport |
| Semantisk kvalitet | Prinsippet om å gjenbruke eksisterende begreper forutsetter at begrepene finnes og er gode nok | Modeller bygger på lokale definisjoner likevel | Prioritere begrepsarbeid parallelt med modellarbeidet |
| Endringsstyring | Prinsippet om stabilitet og utvidbarhet forutsetter en definert forvaltning som ikke alle modelleiere har | Versjoner utvikles ad hoc, og konsumenter mister forutsigbarhet | Avklare forvaltningsmodell for modellen før den publiseres for andre |
| Forankring | Føringene er faglige og ikke koblet til styring, finansiering eller anskaffelseskrav | Modellarbeid nedprioriteres i prosjekter med knapp tid | Ta modellkrav inn i kravgrunnlag og arkitekturvurdering tidlig |
| Sammenheng med gjenbrukbare løsninger | Kravet om maskinlesbar publisering er tett koblet til Felles datakatalog og ModellDCAT-AP-NO | Virksomheter som ikke publiserer der, får svakere nytte av reglene | Vurdere publisering i Felles datakatalog som del av modellarbeidet |

## Publiseringsform og tilgjengelighet
Føringene er publisert som åpne nettsider på digdir.no under informasjonsforvaltning, med en hovedside for felles informasjonsmodeller og egne undersider for designprinsippene og for modelleringsreglene. ModellDCAT-AP-NO og tilhørende veileder for beskrivelse av informasjonsmodeller er publisert på data.norge.no. Alt er fritt tilgjengelig uten pålogging.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Direkte støtte. Hele formålet er å gjøre datastrukturer forståelige og gjenbrukbare på tvers av virksomheter.

- **P6: Lag digitale løsninger som støtter samhandling**
  Kravene om standardformater, persistente identifikatorer og maskinlesbar publisering er forutsetninger for teknisk og semantisk samhandling.

- **P5: Del og gjenbruk løsninger**
  Støttes delvis. Prinsippene om modularitet og gjenbruk av modellelementer gjelder modeller, ikke løsninger.

- **P1: Ta utgangspunkt i brukernes behov**
  Støttes indirekte gjennom prinsippene om enkelhet og forståelighet for målgruppen, men brukerbehov i tjenestesammenheng er ikke tema.

Begrensninger: føringene er anbefalinger uten forpliktende virkning, og gjenbruksverdien avhenger derfor av frivillig oppslutning. Prinsippet om stabilitet og utvidbarhet forutsetter en forvaltningsmodell hos hver modelleier som ressursen selv ikke etablerer. Kravene om maskinlesbarhet gir også reell arbeidsinnsats for virksomheter som ikke allerede har modelleringspraksis, og dette bør vurderes som en kostnad i konkrete case, ikke som en ren gevinst.

## Lenke til dokumentasjon
- https://www.digdir.no/informasjonsforvaltning/prinsipper-informasjonsmodeller/3030
- https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029
- https://data.norge.no/guide/veileder-modelldcat-ap-no
- https://www.digdir.no/informasjonsforvaltning/referansemodeller-innen-informasjonsforvaltning/2156

## Kildegrunnlag brukt i utfyllingen
- https://www.digdir.no/informasjonsforvaltning/prinsipper-informasjonsmodeller/3030, kontrollert 2026-09-04
- https://www.digdir.no/informasjonsforvaltning/felles-modelleringsregler-offentlig-forvaltning/3029, kontrollert 2026-09-04
- https://www.digdir.no/informasjonsforvaltning/referansemodeller-innen-informasjonsforvaltning/2156, kontrollert 2026-09-04
- https://data.norge.no/guide/veileder-modelldcat-ap-no, kontrollert 2026-09-04
- `Digdirs virkemiddeloversikt (intern presentasjon, mars 2026)`, brukt som kandidatkilde
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-04
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-04
- `arkitektur/ressurser/styringsregler.md`, kontrollert 2026-09-04
