# eIDAS-node (Norge)

## Navn
eIDAS-node (Norge)

## Ressurs ID
DIGDIR-024

## Status/Livsfase
**Produksjon** - noden er i drift som Norges tilknytning til det europeiske eIDAS-nettverket, og brukes gjennom ID-porten.

**Fakta:** Digdir dokumenterer at ID-porten er integrert med EUs infrastruktur for autentisering på tvers av landegrenser, slik at europeiske brukere med EU-godkjent eID kan logge inn på norske offentlige tjenester. For produksjonsbruk må landet være formelt notifisert og fagfellevurdert av Europakommisjonen.

**Fakta:** Digdir viser til EUs eIDAS Dashboard for oppdatert status over notifiserte ordninger, og til en demotjeneste på `eidasnode.no` for å kontrollere hvilke land som faktisk er koblet til Norge i produksjon.

## Modenhet
**Teknisk moden, funksjonelt begrenset av identitetsmatching.**

- Teknisk: noden er i produksjon, integrert i ID-porten, og eksponeres for tjenesteeiere gjennom ordinære `acr_values` uten egen integrasjon.
- Funksjonelt: fire kjerneattributter følger alltid med en eIDAS-innlogging, nemlig eIDAS-identifikator, fødselsdato, fornavn og etternavn. Norsk personidentifikator følger bare med når oppslaget mot Folkeregisteret lykkes.
- Bruksmessig: Digdir beskriver selv volumet av vellykkede identitetsmatchinger i Europa som svært lavt.
- Regulatorisk: grunnlaget er eIDAS 1. eIDAS 2 med lommebok er planlagt fra 2026, og vil endre bildet.

**Deduksjon:** Det svakeste leddet er ikke autentiseringen, men matchingen. En utenlandsk bruker kan logge inn, men tjenesten får bare fødselsnummer eller D-nummer hvis personen allerede er registrert i Folkeregisteret med samme utenlandske identifikator. En tjeneste som forutsetter norsk personidentifikator, vil derfor stoppe for en stor del av de brukerne noden slipper inn.

## Kort beskrivelse
eIDAS-node (Norge) er Norges tilknytning til det europeiske nettverket for gjensidig anerkjennelse av elektroniske identiteter. Noden tar imot autentiseringsforespørsler fra norske tjenester, ruter dem til noden i brukerens hjemland, og leverer tilbake et standardisert identitetsdatasett. Den gjør også et oppslag mot Folkeregisteret for å knytte den utenlandske identiteten til et norsk fødsels- eller D-nummer.

Noden er ikke en egen brukerflate. Den er eksponert gjennom ID-porten, og en tjenesteeier aktiverer den ved å be om `eidas-loa-high` eller `eidas-loa-substantial` i `acr_values`. Den er dermed en infrastrukturkomponent i innloggingsflyten, ikke en tjeneste virksomheter integrerer mot direkte.

## Kapabiliteter
- **Tillit: Autentisering**
  gjør det mulig for en norsk tjeneste å verifisere en innlogging utført med en notifisert eID fra et annet EØS-land, på eIDAS-nivå betydelig eller høyt. Uten noden ville evnen til å autentisere utenlandske brukere forsvinne fra norsk arkitektur; den leveres ikke av ID-porten selv.

- **Tillit: Identifisering**
  knytter den utenlandske identiteten til en norsk personidentifikator gjennom oppslag i Folkeregisteret, slik at tjenesten kan bruke identiteten videre i egen saks- og tjenestelogikk.

Koblingene er satt fordi noden selv utfører rutingen mot utlandet og matchingen mot Folkeregisteret. Selve eID-en utstedes i brukerens hjemland, og persondataene eies av Folkeregisteret; begge er avhengigheter og er beskrevet under `Gjenbruk`.

## Produktmål
**Dokumenterte mål**, slik Digdir beskriver funksjonen:
- Gi europeiske brukere med EU-godkjent eID tilgang til norske offentlige tjenester.
- Oppfylle eIDAS-forordningens krav til gjensidig anerkjennelse av notifiserte eID-ordninger.
- Gjøre grensekryssende innlogging tilgjengelig gjennom ID-porten, uten at hver tjenesteeier må bygge egen løsning.

**Utledede operative mål:**
- Redusere antall manuelle unntaksløp for brukere uten norsk eID.
- Gi et forutsigbart, definert datasett som tjenesteeiere kan planlegge saksbehandling rundt.

**Ikke offentlig dokumentert i denne arbeidsøkten:** måltall for antall vellykkede innlogginger eller matchinger i Norge.

## Brukerbehov
- Norske offentlige tjenester trenger å kunne betjene EØS-borgere som ikke har norsk eID.
- Utenlandske brukere trenger å bruke eID-en de allerede har, framfor å skaffe en norsk.
- Saksbehandlere trenger å vite hvilke identitetsopplysninger som faktisk følger med, og hva som skjer når norsk personidentifikator mangler.
- Tjenesteeiere trenger å kunne aktivere grensekryssende innlogging uten egen integrasjon mot hvert land.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Norske tjenesteeiere | Slippe inn brukere med utenlandsk eID | Søknader, innsyn, rapportering | Aktiverer noden gjennom `acr_values` i ID-porten |
| EØS-borgere med notifisert eID | Bruke egen nasjonal eID i Norge | Skatt, arbeid, studier, etablering | Møter noden som et valg i ID-porten |
| Skatteetaten som registerforvalter | Levere grunnlag for identitetsmatching | Oppslag i Folkeregisteret | Eier persondataene, ikke noden |
| Digdir | Drifte noden og koordinere eIDAS i Norge | Nasjonal nodeoperatør | Produkt- og driftsansvar |
| Saksbehandlingsmiljøer | Håndtere brukere uten norsk personidentifikator | Manuelle og halvautomatiske løp | Må ha en plan for match som feiler |

## Hovedfunksjoner
Den første hovedfunksjonen er **ruting av autentisering til utlandet**. Når en tjeneste ber om eIDAS-innlogging, sender ID-porten forespørselen via den norske noden til noden i brukerens hjemland. Selve innloggingen skjer der, med brukerens nasjonale eID, og resultatet kommer tilbake som en bekreftelse med et definert datasett. Tjenesteeieren forholder seg bare til ID-porten.

Den andre er **levering av et standardisert kjernedatasett**. Fire attributter følger alltid med: eIDAS-identifikator, fødselsdato, fornavn og etternavn. Dette er minimumsgrunnlaget en norsk tjeneste kan bygge på, og det er vesentlig mindre enn det en norsk innlogging normalt gir.

Den tredje er **identitetsmatching mot Folkeregisteret**. Noden forsøker å finne et norsk fødsels- eller D-nummer ved å slå opp den utenlandske identifikatoren. Lykkes det, følger norsk personidentifikator med i `pid`. Matchingen forutsetter at personen allerede er registrert i Folkeregisteret med nettopp den utenlandske identifikatoren, og det er denne forutsetningen som i praksis avgjør om et digitalt løp kan fullføres.

Den fjerde er **styring av sikkerhetsnivå**. Tjenesteeieren velger mellom `eidas-loa-high` og `eidas-loa-substantial` i `acr_values`, og styrer dermed hvilket eIDAS-nivå som kreves. Enkeltinnlogging på tvers av tjenester er foreløpig ikke støttet ved eIDAS-pålogging, noe som påvirker brukeropplevelsen i sammensatte løp.

### Typiske brukssituasjoner (generisk)
- En arbeidstaker bosatt i et annet EØS-land skal levere opplysninger til en norsk myndighet.
- En utenlandsk student eller forsker skal bruke en norsk selvbetjeningsløsning.
- En virksomhet i et annet EØS-land skal rapportere til norsk myndighet, og representanten identifiseres med eID fra hjemlandet.
- En tjeneste skal vurdere hvilket eIDAS-nivå som er tilstrekkelig for et gitt saksfelt.

### Når eIDAS-node (Norge) normalt ikke er førstevalg
- Når brukergruppen er norsk. Da dekker `ID-porten` behovet med høyere sikkerhet, bedre datasett og enkeltinnlogging.
- Når tjenesten er avhengig av norsk personidentifikator for å fungere i det hele tatt. Da bør løpet enten ha en plan for manglende match, eller bruke et annet identifiseringsløp.
- Når brukeren ikke kommer fra et notifisert land. Digdir dokumenterer e-postbrukere som en egen, lavere mekanisme for slike tilfeller, og en passbasert registrering er beskrevet, men ikke implementert.
- Når behovet er maskinell tilgang uten person. Da hører løsningen hos `Maskinporten`.
- Når løsningen først settes i drift etter at eIDAS 2 er innført. Da bør `European Digital Identity Wallet` vurderes som primærspor.

### Scope og avgrensning
Inngår: norsk tilknytning til eIDAS-nettverket, ruting av autentiseringsforespørsler til og fra utenlandske noder, levering av eIDAS-kjernedatasett, og oppslag mot Folkeregisteret for identitetsmatching.

Inngår ikke: innloggingsflaten og valgsiden, som hører til `ID-porten`; selve eID-ene, som utstedes i brukerens hjemland; registrering av personer i Folkeregisteret; tilgangsstyring og rettigheter etter innlogging, som ligger i `Altinn Autorisasjon`; og kontaktopplysninger, siden utenlandske brukere ikke registreres i Kontakt- og reservasjonsregisteret.

Avgrensningen mot `eID Building Block` går på nivå: byggesteinen er den europeiske spesifikasjonen og referanseprogramvaren, mens denne ressursen er den norske implementasjonen og driften av den.

## Veikart over kommende funksjonalitet
**Fakta:** Digdir dokumenterer eIDAS 2 med digital identitetslommebok som planlagt fra 2026, og en passbasert registrering med tofaktorautentisering som beskrevet, men ikke implementert.

**Fakta:** NOBID Identity Matching-prosjektet, som går fra 2024 til 2026, leverte i tredje kvartal 2025 en sandkasse som gjør det mulig å matche svenske brukere i Norge. Løsningen er integrert med svensk eIDAS-autentisering og med ID-porten, og utvikles i to varianter: én basert på nasjonale befolkningsregistre og én modulær med vekt på personvern. Kantega AS utvikler teknologien, og arbeidet har politisk forankring fra nordiske og baltiske digitaliseringsministre i 2023 og nordiske statsministre i 2024.

**Deduksjon:** Retningen er at matchingproblemet løses i et nordisk-baltisk spor før det løses i EU som helhet. For en norsk tjenesteeier betyr det at dekningen sannsynligvis blir god for nordiske brukere først.

## Forretningsverdi/Verdiforslag
**For tjenesteeiere:** én aktivering i ID-porten gir tilgang til eID-er fra alle notifiserte EØS-land, uten integrasjon per land.

**For utenlandske brukere:** de kan bruke eID-en de har, og slipper å skaffe norsk eID for å bruke en norsk tjeneste.

**For samfunnet:** lavere terskel for arbeids- og studiemobilitet, og oppfyllelse av Norges forpliktelser etter eIDAS.

**For forvaltningen:** færre manuelle unntaksløp, og et definert minimumsdatasett som gjør det mulig å planlegge saksbehandling for utenlandske brukere framfor å håndtere dem som enkelttilfeller.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Funksjonell | Identitetsmatching feiler når personen ikke er registrert i Folkeregisteret med samme utenlandske identifikator | Tjenesten får da bare kjernedatasettet uten `pid`, og må ha et alternativt løp. NOBID-sporet arbeider med bedre matching |
| Bruker | Enkeltinnlogging er ikke støttet ved eIDAS-pålogging | Brukeren må logge inn på nytt i sammensatte løp; Digdir oppgir ingen dato for endring |
| Data | Utenlandske brukere registreres ikke i Kontakt- og reservasjonsregisteret | Digital varsling må løses på annen måte, eller tjenesten må be om kontaktopplysninger selv |
| Juridisk | Sikkerhetsnivå notifisert i et annet land må vurderes mot norske krav i den enkelte tjenesten | eIDAS definerer nivåene; vurderingen ligger hos tjenesteeier |
| Dekning | Bare notifiserte og fagfellevurderte land er koblet i produksjon | Kontroller faktisk dekning mot EUs eIDAS Dashboard og demotjenesten på `eidasnode.no` før løsningen planlegges |
| Overgang | eIDAS 2 med lommebok endrer mekanismen | Skill tjenestens identitetskrav fra innloggingsmekanismen, slik at bytte blir mulig |
| Volum | Digdir beskriver svært lave matchingvolum i Europa | Feil og mangler oppdages sent fordi bruken er liten |

## Kanaler
Noden har ingen egen brukerflate. Den nås gjennom `ID-porten`, der brukeren velger eIDAS-innlogging, og gjennom tjenesteeierens forespørsel med `eidas-loa-high` eller `eidas-loa-substantial` i `acr_values`. Uten at tjenesteeieren ber om disse verdiene, er eIDAS ikke aktivert.

I tillegg finnes en demotjeneste på `eidasnode.no` som gjør det mulig å kontrollere hvilke land som faktisk er koblet til Norge i produksjon. Den er en verifikasjonskanal for tjenesteeiere, ikke en sluttbrukerflate.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** driftsmodell og plattform for den norske noden. Det som er kjent, er at noden driftes nasjonalt av Digdir som del av ID-porten-plattformen, og at referanseimplementasjonen av eIDAS-noden publiseres av Europakommisjonen.

## Gjenbruk
Noden er selv en gjenbruksmekanisme: alle norske tjenester som bruker ID-porten kan aktivere grensekryssende innlogging uten egen utvikling. Gjenbruket skjer gjennom `acr_values`, ikke gjennom et eget grensesnitt.

Avhengigheter som ikke er kapabiliteter her: `ID-porten` leverer innloggingsflaten og valgsiden, `Folkeregisteret` leverer persondataene som matchingen bygger på, og de utenlandske eID-ordningene leverer selve identitetsbeviset. Evnen til å levere grunndata hører hos Folkeregisteret, ikke her.

**Vanlige kombinasjoner med andre produkter:**
- `ID-porten` som inngang; noden er ikke tilgjengelig uten den.
- `Folkeregisteret` for identitetsmatching mot norsk personidentifikator.
- `eID Building Block` som den europeiske spesifikasjonen og referanseprogramvaren noden bygger på.
- `European Digital Identity Wallet` som neste generasjon av samme behov.
- `Altinn Autorisasjon` når den utenlandske brukeren skal opptre på vegne av en virksomhet.

**Kildekode:** Ikke offentlig dokumentert. Kildene i denne arbeidsøkten sier ikke om den norske nodeimplementasjonen er publisert. Europakommisjonens referanseimplementasjon av eIDAS-noden er derimot åpent tilgjengelig.

**Lisens:** Ikke offentlig dokumentert.

## Støtter arkitekturprinsipper
- **P6: Lag digitale løsninger som støtter samhandling**
  Noden er selve mekanismen som gjør norske tjenester tilgjengelige for brukere med eID fra andre land.
- **P7: Sørg for tillit til oppgaveløsningen**
  Notifisering og fagfellevurdering av eID-ordninger, sammen med definerte sikkerhetsnivåer, gir et etterprøvbart grunnlag for å stole på en utenlandsk identitet.
- **P5: Del og gjenbruk løsninger**
  Støttes ved at én nasjonal komponent dekker behovet for alle tjenester i ID-porten, framfor at hver tjeneste bygger sitt eget.
- **P1: Ta utgangspunkt i brukernes behov**
  Støttes delvis: brukeren får bruke eID-en hun allerede har, men opplevelsen er svakere enn ved norsk innlogging.

**Spenning og begrensning:** Den tydeligste spenningen er mot **P1: Ta utgangspunkt i brukernes behov**. Manglende enkeltinnlogging, et tynt datasett og matching som ofte feiler, gjør at brukeren kommer inn, men ikke nødvendigvis gjennom. For en tjeneste som forutsetter norsk personidentifikator, kan noden i verste fall gi en brukeropplevelse der innloggingen lykkes og oppgaven likevel stopper. Noden er også i spenning mot **P2: Ta arkitekturbeslutninger på rett nivå** i overgangen til eIDAS 2: mekanismen er besluttet erstattet på europeisk nivå, mens norske tjenester fortsatt må bygge på den i dag. Ved vurdering av bruk bør det derfor være avklart hva tjenesten gjør når matchingen feiler, før noden aktiveres.

## Finansiering
**Ikke offentlig dokumentert i denne arbeidsøkten:** finansieringsmodell for noden. Det som er kjent, er at den driftes av Digdir som del av ID-porten, og at NOBID Identity Matching-prosjektet er et eget, politisk forankret samarbeid i Norden og Baltikum.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir | Digdirs dokumentasjon av eIDAS i ID-porten |
| Driftsansvar | Digdir, som del av ID-porten-plattformen | Samme |
| Persondata for identitetsmatching | Skatteetaten som forvalter av Folkeregisteret | Digdir om at matching skjer i samarbeid mellom Skatteetaten og Digdir |
| Nasjonal koordinering av eIDAS | Digdir | Digdirs sider om elektronisk identitet og internasjonalt arbeid |
| Notifisering av eID-ordninger | Europakommisjonen, med nasjonale myndigheter som avsender | Digdirs omtale av notifisering og fagfellevurdering |
| Budsjettansvar | Ikke offentlig dokumentert i denne arbeidsøkten | - |

## Lenke til dokumentasjon
- eIDAS i ID-porten: https://docs.digdir.no/docs/idporten/oidc/oidc_func_eidas.html
- Utenlandske brukere i ID-porten: https://docs.digdir.no/docs/idporten/oidc/oidc_func_utanlandske_brukarar
- Digdir om identitetsmatching: https://www.digdir.no/internasjonalt-arbeid/identity-matching/6681
- Digdir om identitetsmatching på tvers av grensene: https://samarbeid.digdir.no/digital-lommebok/identitetsmatching-pa-tvers-av-grensene/3223
- Digdir om elektronisk identitet: https://www.digdir.no/digital-identitet/elektronisk-identitet-eid/4047

## Kildegrunnlag brukt i utfyllingen
- Digdir, eIDAS i ID-porten, docs.digdir.no, hentet 25. september 2026.
- Digdir, Utanlandske brukarar i ID-porten, docs.digdir.no, hentet 25. september 2026.
- Digdir, Identity Matching, digdir.no, hentet 25. september 2026.
- Lokale kilder: `arkitektur/ressurser/produktnummerering.md`, `arkitektur/ressurser/operative-losninger-og-tjenester/42-eID-Building-Block-v1-claude.md`, `arkitektur/kapabiliteter/capabilities.yaml`, `arkitektur/prinsipper/principles.md`, `sources/links.md`.
