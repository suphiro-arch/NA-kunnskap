# eID Building Block

## Navn
eID Building Block

## Ressurs ID
EU-002

## Status/Livsfase
**Produksjon** - byggesteinen er i aktiv bruk i det europeiske eIDAS-nettverket, samtidig som den peker mot EUDI-lommeboka som neste generasjon.

**Fakta:** Europakommisjonen fører eID som en aktiv byggestein i DIGITAL Building Blocks, og oppgir bruksmålinger med 65 prosjekter som gjenbruker eID, 464 offentlige tjenester koblet til nettverket og 1,14 millioner grensekryssende identifiseringsforespørsler.

**Deduksjon:** Byggesteinen er i en overgangsfase. Den er i drift under eIDAS 1, mens det rettslige og tekniske tyngdepunktet flyttes mot eIDAS 2.0 og lommebok. Kildene i denne arbeidsøkten sier ikke når eller om eIDAS-nodemodellen fases ut.

## Modenhet
**Høy teknisk og organisatorisk modenhet, men med kjent overgangsrisiko.**

- Teknisk: eIDAS-noden er en referanseimplementasjon av eID eIDAS-profilen, med testverktøy, og er i drift i hele nettverket.
- Organisatorisk: modellen bygger på gjensidig anerkjennelse av nasjonale eID-ordninger notifisert etter eIDAS, med etablerte roller per land.
- Bruksmessig: målingene Kommisjonen oppgir viser reell, men beskjeden transaksjonsvolum sammenlignet med nasjonale eID-er.
- Regulatorisk: grunnlaget er eIDAS-forordningen. Revisjonen gjennom eIDAS 2.0 endrer retningen mot brukerstyrt lommebok.

**Deduksjon:** Det svakeste leddet er levetiden. En virksomhet som investerer i integrasjon mot eIDAS-nodemodellen nå, bør regne med at den samme brukergruppen på sikt skal betjenes gjennom lommebok, og bør derfor skille tydelig mellom tjenestens egne krav til identitet og selve overføringsmekanismen.

## Kort beskrivelse
eID Building Block er Europakommisjonens felles byggestein for gjensidig anerkjennelse av nasjonale elektroniske identiteter over landegrenser. Byggesteinen består av spesifikasjoner, referanseprogramvare i form av eIDAS-noden, konformitetstesting og støttetjenester, slik at et land kan koble sin egen eID-infrastruktur til det europeiske nettverket i stedet for å bygge bilaterale løsninger mot hvert enkelt land.

Byggesteinen dekker fire samhandlingsdimensjoner: juridisk, organisatorisk, semantisk og teknisk. Den leverer ikke selve eID-en, men mekanismen som gjør at en eID utstedt i ett land kan verifiseres og forstås i et annet.

## Kapabiliteter
- **Tillit: Autentisering**
  gir mekanismen for at en tjeneste i ett land kan verifisere en innlogging utført med en eID fra et annet land, innenfor eIDAS-rammeverkets sikkerhetsnivåer.

- **Tillit: Identifisering**
  overfører et minimumsdatasett som identifiserer personen eller virksomheten entydig på tvers av landegrenser, slik at mottakeren kan koble identiteten videre i egen tjenestelogikk.

Koblingene er satt fordi byggesteinen selv leverer den grensekryssende delen av evnen. Uten den ville en norsk tjeneste måtte bygge egne løsninger mot hvert enkelt lands eID-ordning. De nasjonale eID-ene som brukes gjennom nettverket, eies av andre aktører, og evnen til å utstede dem hører hos dem.

## Produktmål
**Dokumenterte mål** slik Kommisjonen beskriver byggesteinen:
- Gjøre det mulig for europeere å bruke sin nasjonale eID når de bruker offentlige tjenester i andre land.
- Redusere den administrative byrden ved å bruke offentlige tjenester i utlandet.
- Sikre etterlevelse av eIDAS-forordningens krav til gjensidig anerkjennelse.

**Utledede operative mål:**
- Gi et felles teknisk mønster, slik at hvert land kobler seg til nettverket én gang framfor å integrere bilateralt.
- Gjøre det mulig å gjenbruke samme nodekomponent på tvers av mange nasjonale tjenester.

## Brukerbehov
- Offentlige tjenester trenger å kunne identifisere brukere som ikke har nasjonal eID i landet der tjenesten tilbys.
- Innbyggere og virksomheter trenger å bruke eID-en de allerede har, framfor å skaffe en ny i hvert land.
- Nasjonale eID-forvaltere trenger et felles mønster for å eksponere sin ordning mot andre land på en kontrollert måte.
- Arkitekturmiljøer trenger å forstå hvilket sikkerhetsnivå og hvilket datasett som følger med en grensekryssende innlogging.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige tjenesteeiere | Betjene brukere med utenlandsk eID | Innlogging i søknads- og selvbetjeningsløsninger | Kobler seg til nasjonal node, ikke direkte til andre land |
| Innbyggere og virksomheter i EØS | Bruke egen nasjonal eID i utlandet | Studier, arbeid, etablering, skatt | Merker byggesteinen bare indirekte |
| Nasjonale nodeoperatører | Drifte tilknytningen til nettverket | eIDAS-node i eget land | I Norge dekket av `eIDAS-node (Norge)` |
| Europakommisjonen | Forvalte spesifikasjon, programvare og testing | Referanseimplementasjon og konformitet | Eier byggesteinen |
| Systemleverandører | Bygge integrasjoner mot noden | Tilkobling av fagløsninger | Trenger spesifikasjoner og testmiljø |

## Hovedfunksjoner
Den sentrale funksjonen er **formidling av identitet mellom land**. En tjeneste sender en autentiseringsforespørsel til sin nasjonale node, som ruter den videre til noden i brukerens hjemland. Der utføres selve innloggingen med nasjonal eID, og resultatet sendes tilbake som en assertjon med et definert minimumsdatasett. Tjenesten trenger dermed bare å forholde seg til én motpart.

Den andre funksjonen er **referanseprogramvare**. Kommisjonen publiserer eIDAS-noden som en referanseimplementasjon av eID eIDAS-profilen, med testverktøy egnet for demonstrasjon og verifikasjon. Et land kan velge å bruke denne programvaren direkte, eller bygge en egen implementasjon som følger samme profil.

Den tredje funksjonen er **konformitetstesting og støtte**. Byggesteinen tilbyr testtjenester, dokumentasjon av spesifikasjoner og fellesskapsstøtte, slik at nye deltakere kan verifisere at implementasjonen faktisk virker sammen med resten av nettverket før den settes i produksjon.

Den fjerde funksjonen er **semantisk og juridisk tilrettelegging**. Byggesteinen definerer hvilke attributter som følger med, og hvordan sikkerhetsnivåene etter eIDAS skal forstås. Dette er en forutsetning for at mottakeren kan vurdere om innloggingen er god nok for det aktuelle formålet, og er like viktig som den tekniske transporten.

### Typiske brukssituasjoner (generisk)
- En norsk offentlig tjeneste skal ta imot søknader fra personer bosatt i andre EØS-land.
- En virksomhet fra et annet land skal registrere seg eller rapportere til norsk myndighet.
- En tjeneste må vurdere hvilket eIDAS-sikkerhetsnivå som kreves for et gitt saksfelt.

### Når eID Building Block normalt ikke er førstevalg
- Når brukergruppen er norsk og har norsk eID. Da er `ID-porten` riktig inngang, og byggesteinen er bare relevant for de utenlandske brukerne.
- Når behovet er å dele dokumentasjon og bevis, ikke å identifisere. Da er `Once-Only Technical System` eller EUDI-lommebok mer treffsikkert.
- Når løsningen først settes i drift flere år fram i tid. Da bør EUDI-lommebok vurderes som primærspor, med eIDAS-node som overgangsløsning.
- Når behovet er maskinell tilgang uten innlogget person.

### Scope og avgrensning
Inngår: spesifikasjoner for eID eIDAS-profilen, eIDAS-noden som referanseprogramvare, konformitetstesting, dokumentasjon og støtte.

Inngår ikke: selve de nasjonale eID-ordningene, notifiseringen av dem, nasjonal identitetsmatching mot folkeregister, og tilgangsstyring etter innlogging.

Den norske noden og norsk identitetsmatching er en egen ressurs i registeret, `eIDAS-node (Norge)`. Denne beskrivelsen dekker den europeiske byggesteinen.

## Veikart over kommende funksjonalitet
**Fakta:** Kommisjonen omtaler eID-byggesteinen som komplementær til EUDI-lommeboka, som er neste steg i det europeiske identitetsarbeidet.

**Fakta:** Digdir beskriver eIDAS2 som leverandør av tillitstjenester på høyt nivå og av lommebok, og at SDG og OOTS bygger på eIDAS2 for autentisering.

**Ikke offentlig dokumentert i denne arbeidsøkten:** en publisert utfasingsplan eller sluttdato for eIDAS-nodemodellen.

## Forretningsverdi/Verdiforslag
**For tjenesteeiere:** én tilknytning gir tilgang til eID-er fra hele EØS, i stedet for integrasjoner per land. Det gjør det praktisk mulig å tilby digitale løp til brukere som i dag må håndteres manuelt.

**For innbyggere og virksomheter:** de kan bruke eID-en de allerede har, og slipper å skaffe ny identifikasjon i hvert land de har et forhold til.

**For samfunnet:** senker terskelen for arbeids- og studiemobilitet i EØS, og gir et felles sikkerhetsnivåbegrep som gjør risikovurderinger sammenlignbare på tvers.

**For forvaltningen:** færre manuelle unntaksløp for utenlandske brukere, og et definert grunnlag for hvilke identitetsopplysninger som faktisk følger med.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Overgang | Investering i nodeintegrasjon kan få kort levetid når eIDAS 2.0 tar over | Skill tjenestens identitetskrav fra overføringsmekanismen, slik at bytte blir mulig |
| Teknisk | Identitetsmatching mot nasjonale registre er ikke del av byggesteinen, og er ofte det vanskeligste steget | Håndteres nasjonalt; i Norge gjennom `eIDAS-node (Norge)` og Folkeregisteret |
| Bruker | Grensekryssende innlogging gir ofte brukeropplevelse på et annet språk og med ukjente steg | Ikke offentlig dokumentert i denne arbeidsøkten |
| Juridisk | Sikkerhetsnivå notifisert i ett land må vurderes mot norske krav i den enkelte tjenesten | eIDAS definerer nivåene, men vurderingen ligger hos tjenesteeier |
| Volum | Lave transaksjonstall gjør at feil og mangler oppdages sent | Uavklart. Konformitetstesting dekker teknisk samvirke, ikke bruksvolum |

## Kanaler
Byggesteinen leveres som spesifikasjoner, nedlastbar referanseprogramvare og testtjenester gjennom Kommisjonens portal for DIGITAL Building Blocks. Den har ingen egen sluttbrukerflate: brukeren møter den bare som et omdirigeringsløp i innloggingen til en tjeneste.

Integrasjonsflaten er nasjonal. En norsk tjeneste kobler seg til den norske noden, ikke direkte til byggesteinen.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** driftsmodell for de nasjonale nodene. Det som er kjent, er at eIDAS-noden er programvare som hvert land installerer og drifter selv, slik at plattformvalget er nasjonalt og ikke fastsatt av byggesteinen.

## Gjenbruk
Byggesteinen er i seg selv et gjenbruksprodukt: spesifikasjonene er åpne, referanseprogramvaren kan lastes ned, og konformitetstesting gjør det mulig å verifisere egen implementasjon. Kommisjonen oppgir at 65 prosjekter gjenbruker eID, og at ytterligere 15 har forpliktet seg til analyse eller gjenbruk.

Avhengigheter som ikke er kapabiliteter her: nasjonale eID-ordninger leverer selve identitetsbeviset, og nasjonale folkeregistre leverer koblingen til en kjent person. Begge evnene hører hos de ressursene.

**Vanlige kombinasjoner med andre produkter:**
- `eIDAS-node (Norge)` som den norske implementasjonen av byggesteinen.
- `ID-porten` som nasjonal innloggingsløsning, der grensekryssende innlogging presenteres som ett av valgene.
- `European Digital Identity Wallet` som neste generasjon av det samme behovet.
- `Once-Only Technical System`, som forutsetter autentisering etter eIDAS før dokumentasjon kan hentes.

**Kildekode:** Åpen kildekode. eIDAS-noden publiseres som referanseimplementasjon av Europakommisjonen.

**Lisens:** Ikke offentlig dokumentert. Lisensvilkårene er ikke kontrollert mot repositoriet i denne arbeidsøkten.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger**
  Referanseprogramvare, spesifikasjoner og testtjenester er laget for å gjenbrukes av alle land framfor at hvert land bygger sitt eget.
- **P6: Lag digitale løsninger som støtter samhandling**
  Hele formålet er samhandling over landegrenser, med felles profil for hvordan identitet formidles.
- **P7: Sørg for tillit til oppgaveløsningen**
  Notifisering av eID-ordninger og felles sikkerhetsnivåer gir et etterprøvbart grunnlag for å stole på en identitet fra et annet land.

**Spenning og begrensning:** Byggesteinen støtter **P1: Ta utgangspunkt i brukernes behov** bare delvis. Brukerløpet går gjennom flere ledd og språk, og oppleves ofte som mer tungvint enn nasjonal innlogging. Den er også i spenning mot **P2: Ta arkitekturbeslutninger på rett nivå** i en overgangsfase: nasjonale virksomheter må investere i en mekanisme som europeisk nivå allerede har besluttet å erstatte. For et konkret case bør det derfor vurderes om behovet kan vente på lommebok, eller om utenlandske brukere må betjenes nå.

## Finansiering
**Fakta:** Byggesteinen forvaltes og finansieres av Europakommisjonen som del av DIGITAL-programmet for byggesteiner.

**Ikke offentlig dokumentert i denne arbeidsøkten:** hvordan drift av nasjonale noder finansieres i Norge, og om det påløper kostnader for den enkelte tjenesteeier.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar for byggesteinen | Europakommisjonen | DIGITAL Building Blocks, eID |
| Drift av nasjonal node | Den enkelte medlemsstaten; i Norge Digdir | Registeroppføring for `eIDAS-node (Norge)` i `produktnummerering.md` |
| Regelverksgrunnlag | eIDAS-forordningen, forvaltet i EU | Kommisjonens beskrivelse av byggesteinen |
| Budsjettansvar | Europakommisjonen for byggesteinen; nasjonalt for nodene | Deduksjon fra ansvarsdelingen over |
| Styringsmodell | Ikke offentlig dokumentert i denne arbeidsøkten | - |

## Lenke til dokumentasjon
- eID Building Block: https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eID
- DIGITAL Building Blocks, samleside: https://interoperable-europe.ec.europa.eu/collection/digital-building-blocks
- Digdir om tre EU-regelverk og én digital infrastruktur: https://www.digdir.no/digitalisering-og-samordning/tre-eu-regelverk-en-digital-infrastruktur/8120

## Kildegrunnlag brukt i utfyllingen
- Europakommisjonen, eID Building Block, hentet 24. september 2026.
- Europakommisjonen, DIGITAL Building Blocks, hentet 24. september 2026.
- Digdir, Tre EU-regelverk, én digital infrastruktur, hentet 24. september 2026.
- Lokale kilder: `arkitektur/ressurser/produktnummerering.md`, `arkitektur/kapabiliteter/capabilities.yaml`, `arkitektur/prinsipper/principles.md`, `sources/links.md`.
