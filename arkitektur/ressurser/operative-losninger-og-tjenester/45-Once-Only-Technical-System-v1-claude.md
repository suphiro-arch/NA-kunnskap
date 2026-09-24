# Once-Only Technical System

## Navn
Once-Only Technical System (OOTS)

## Ressurs ID
EU-005

## Status/Livsfase
**Produksjon** - fellestjenestene er i drift, og medlemsstatene kobler til nasjonale plattformer og myndigheter.

**Fakta:** Europakommisjonen opplyser at OOTS-fellestjenestene gikk i drift i desember 2023, og at medlemsstatene siden har bygget nasjonale plattformer og koblet til offentlige myndigheter. Over 1 000 offentlige myndigheter er omtalt som del av økosystemet.

**Fakta:** Digdir opplyser at både SDG-forordningen og OOTS er innlemmet i EØS-avtalen, og at høring er gjennomført for SDG. For OOTS er det ikke oppgitt tidsplan.

**Deduksjon:** Ressursen er i produksjon på europeisk nivå, mens norsk tilkobling er i innføringsfase. Kildene i denne arbeidsøkten dokumenterer ikke hvilke norske myndigheter som er koblet til i dag.

## Modenhet
**Moden infrastruktur, umoden utbredelse.**

- Teknisk: arkitekturen er fastsatt i gjennomføringsforordning (EU) 2022/1463, og fellestjenestene har vært i drift siden desember 2023. Kommisjonen omtaler infrastrukturen som testet, prøvd og klar.
- Funksjonelt: systemet dekker 25 sentrale prosedyrer og om lag 60 identifiserte bevistyper, med utdanning, næringsliv og yrkeskvalifikasjoner som de områdene som er lengst framme. Befolknings- og kjøretøyprosedyrer er omtalt som kommende.
- Organisatorisk: verdien avhenger av at både bevisleverandør og bevismottaker er koblet til i hvert landpar. Dette er den langsomme delen.
- Nordisk: OOTS 2.0-prosjektet under Nordisk ministerråd arbeider med å forbedre arkitekturen og overføring av strukturerte data mellom nordiske og baltiske land. Norge deltok også i det tidligere nordisk-baltiske pilotprosjektet, som ble avsluttet i juni 2023.

**Deduksjon:** Det svakeste leddet er dekningsgraden. Et bevis kan bare hentes hvis nøyaktig den bevistypen er tilgjengelig fra nøyaktig det landet brukeren kommer fra. For en norsk tjeneste betyr det at OOTS i praksis er et supplement til manuelle løp, ikke en erstatning, inntil dekningen er høy nok.

## Kort beskrivelse
Once-Only Technical System er EUs infrastruktur for at offentlige myndigheter skal kunne hente dokumentasjon direkte fra hverandre over landegrenser, slik at innbyggere og virksomheter slipper å levere de samme opplysningene flere ganger. Systemet er hjemlet i forordning (EU) 2018/1724 om en felles digital portal, med tekniske krav i gjennomføringsforordning (EU) 2022/1463.

Utvekslingen skjer mellom myndigheter, ikke gjennom brukeren, men brukeren har kontroll: en forhåndsvisningsflate lar innbyggeren se hva som skal overføres før det godkjennes. Systemet er avgrenset til de prosedyrene og bevistypene som er listet i regelverket.

## Kapabiliteter
- **Datautveksling og integrasjon: Dele data med andre**
  gjør at en norsk bevisutsteder kan gjøre dokumentasjon tilgjengelig for myndigheter i andre land innenfor et definert og rettslig forankret formål.

- **Datautveksling og integrasjon: Bruke data fra andre**
  gjør at en norsk tjeneste kan hente inn bevis fra utenlandske registre i stedet for å be brukeren om å skaffe dem selv.

- **Samarbeid: Organisatorisk samhandling**
  effektiviserer forretningsprosessene på tvers av organisatoriske og nasjonale grenser, ved at søknadsbehandling i ett land kan trekke på registerdata i et annet.

Koblingene er satt fordi OOTS selv etablerer mekanismen for grensekryssende bevisutveksling. Den underliggende transporten leveres av `eDelivery Building Block`, og autentiseringen av brukeren av eIDAS-rammeverket. Begge er avhengigheter, ikke kapabiliteter i denne ressursen.

## Produktmål
**Dokumenterte mål** slik Kommisjonen og regelverket beskriver systemet:
- Gjennomføre engangsprinsippet for de prosedyrene som er listet i forordningen om felles digital portal.
- Gjøre det mulig for innbyggere og virksomheter å levere dokumentasjon bare én gang, også når prosedyren gjelder et annet land.
- Gi brukeren kontroll gjennom forhåndsvisning før bevis overføres.

**Utledede operative mål:**
- Fjerne manuelle, papirbaserte dokumentasjonsløp i grensekryssende søknader.
- Gjøre det mulig for en tjeneste å forholde seg til ett felles oppslagsmønster framfor å kjenne registerstrukturen i hvert land.

## Brukerbehov
- Innbyggere som studerer, arbeider eller etablerer virksomhet i et annet land, trenger å slippe å skaffe attester og bekreftelser manuelt.
- Saksbehandlere trenger dokumentasjon de kan stole på, hentet direkte fra kilden i utstederlandet.
- Bevisutstedere trenger et kontrollert mønster for å gi fra seg opplysninger til utenlandske myndigheter uten å inngå avtaler med hver enkelt.
- Innbyggere trenger innsyn i og kontroll over hva som faktisk deles om dem.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Innbyggere og virksomheter | Slippe å levere samme dokumentasjon flere ganger | Studier, arbeid, etablering, yrkeskvalifikasjoner | Møter systemet gjennom forhåndsvisningsflaten |
| Bevismottakere, offentlige myndigheter | Hente bevis fra utenlandske registre | Søknadsbehandling i de listede prosedyrene | Må koble seg til nasjonal plattform |
| Bevisleverandører, registereiere | Levere bevis på forespørsel i standardisert form | Utdanningsregistre, enhetsregistre, yrkesregistre | Krever tilpasning av registeruttrekk |
| Nasjonale koordinatorer | Bygge og drifte nasjonal plattform | Tilknytning til fellestjenestene | I Norge er Digdir sentral aktør |
| Europakommisjonen | Drifte fellestjenestene | Bevismegler, tjenestekatalog, semantisk register | Eier og drifter fellesnivået |

## Hovedfunksjoner
Den første hovedfunksjonen er **å finne ut hvilket bevis som gjelder**. Bevismegleren kobler et krav i en prosedyre til de bevistypene som kan oppfylle det, og tjenestekatalogen sier hvor et slikt bevis kan hentes i det aktuelle landet. Uten disse fellestjenestene måtte hver myndighet kjenne registerstrukturen i alle andre land.

Den andre er **selve bevisutvekslingen**. Bevismottakeren sender en forespørsel som rutes til riktig bevisleverandør, og beviset sendes tilbake gjennom samme infrastruktur. Transporten bygger på eDelivery, slik at utvekslingen er kryptert, signert og kvittert for.

Den tredje er **brukerkontroll gjennom forhåndsvisning**. Før beviset går videre til mottakeren, får brukeren se hva som skal overføres og kan godkjenne eller avbryte. Dette er et rettslig krav, ikke en valgfri funksjon, og det er også det som skiller OOTS fra ren registerutveksling mellom myndigheter.

Den fjerde er **semantisk tilrettelegging**. Et bevis fra ett land må kunne forstås i et annet. Det semantiske registeret og de felles datamodellene sørger for at innholdet kan tolkes maskinelt, ikke bare overføres som en fil. Dette er ofte den mest krevende delen for en registereier som skal bli bevisleverandør.

### Typiske brukssituasjoner (generisk)
- En person med utdanning fra et annet EØS-land søker om godkjenning av yrkeskvalifikasjon i Norge.
- En virksomhet registrert i et annet land skal dokumentere sin registrering i en norsk prosess.
- En norsk registereier skal gjøre et bevis tilgjengelig for myndigheter i andre land.

### Når Once-Only Technical System normalt ikke er førstevalg
- Når begge parter er norske. Da gjelder nasjonale mekanismer for deling av data, ikke OOTS.
- Når prosedyren eller bevistypen ikke er omfattet av forordningen. Systemet er avgrenset til de listede prosedyrene og bevistypene, og kan ikke brukes fritt.
- Når brukeren selv skal styre delingen av egne dokumenter. Da er `European Digital Identity Wallet` den brukerstyrte motparten til OOTS.
- Når behovet er sanntidsoppslag med lav svartid. Utvekslingen er asynkron og involverer flere ledd.

### Scope og avgrensning
Inngår: fellestjenestene bevismegler, tjenestekatalog og semantisk register, arkitekturen for bevisutveksling, forhåndsvisningsflaten og kravene til nasjonale plattformer.

Inngår ikke: innholdet i bevisene, som eies av registereierne; nasjonale plattformer, som bygges av hvert land; transportlaget, som leveres av eDelivery; og autentisering av brukeren, som følger eIDAS.

Ressursen beskriver det europeiske systemet. Norsk tilknytning og norsk plattform er ikke registrert som egen ressurs i denne oversikten, og kildene i denne arbeidsøkten dokumenterer ikke status for den.

## Veikart over kommende funksjonalitet
**Fakta:** Kommisjonen omtaler befolknings- og kjøretøyprosedyrer som kommende utvidelser, mens utdanning, næringsliv og yrkeskvalifikasjoner er de områdene som er lengst framme.

**Fakta:** OOTS 2.0-prosjektet under Nordisk ministerråd arbeider med å forbedre arkitekturen og legge til rette for overføring av strukturerte data mellom nordiske og baltiske land, og med å identifisere tekniske, personvernmessige og juridiske utfordringer.

**Ikke offentlig dokumentert i denne arbeidsøkten:** en datofestet plan for norsk tilkobling av bevisleverandører og bevismottakere.

## Forretningsverdi/Verdiforslag
**For innbyggere og virksomheter:** færre attester å skaffe, kortere behandlingstid og mindre risiko for at en søknad stopper på manglende dokumentasjon fra utlandet.

**For saksbehandlende myndigheter:** dokumentasjon hentet direkte fra kilden, som er mer pålitelig enn innsendte kopier og reduserer behovet for manuell verifisering.

**For samfunnet:** lavere terskel for arbeids- og studiemobilitet i EØS, og en felles infrastruktur som kan gjenbrukes når flere prosedyrer tas inn i regelverket.

**For registereiere:** ett standardisert uttrekksmønster mot alle land, framfor bilaterale ordninger og manuelle forespørsler.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Dekning | Verdien uteblir så lenge få bevistyper og få land faktisk er koblet til | Kommisjonen rapporterer over 1 000 tilkoblede myndigheter; dekning per bevistype og land er ikke dokumentert i denne arbeidsøkten |
| Semantikk | Bevis fra ulike land må kunne tolkes maskinelt, ikke bare overføres | Semantisk register og felles datamodeller; tilpasning av nasjonale registre er fortsatt en betydelig jobb |
| Juridisk | Bruk utenfor de listede prosedyrene har ikke hjemmel | Avgrensningen følger av forordning (EU) 2018/1724 |
| Personvern | Grensekryssende deling av personopplysninger krever kontroll og innsyn | Forhåndsvisning og brukergodkjenning er innebygd i arkitekturen |
| Organisatorisk | Norsk status for tilkobling er ikke offentlig dokumentert i denne arbeidsøkten | Bør avklares direkte med Digdir før en tjeneste planlegger å bygge på OOTS |
| Teknisk | Avhengigheten til eDelivery og eIDAS gir en kjede med flere ledd som alle må virke | Følger av arkitekturen; feilsøking krever kompetanse på alle lagene |

## Kanaler
OOTS har to flater. Den maskinelle flaten er utveksling mellom nasjonale plattformer gjennom eDelivery, med oppslag mot fellestjenestene. Den brukerrettede flaten er forhåndsvisningen, der innbyggeren ser og godkjenner hva som skal overføres. Forhåndsvisningen presenteres i sammenheng med den tjenesten brukeren faktisk holder på med, og forutsetter innlogging etter eIDAS.

Det finnes ingen egen portal der en innbygger kan bruke OOTS direkte. Systemet nås alltid gjennom en prosedyre hos en myndighet.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** driftsmodell og plattformvalg for fellestjenestene. Det som er kjent, er at fellestjenestene driftes sentralt av Europakommisjonen, og at de nasjonale plattformene bygges og driftes av hvert enkelt land.

## Gjenbruk
OOTS er selv et gjenbruksprodukt: arkitekturen, datamodellene og fellestjenestene er felles for alle land, og bygger videre på eDelivery framfor å definere egen transport. Nasjonale plattformer kan gjenbrukes på tvers av prosedyrer og sektorer i eget land.

Avhengigheter som ikke er kapabiliteter her: `eDelivery Building Block` leverer sikker meldingsutveksling, og eIDAS-rammeverket leverer autentisering av brukeren. Begge evnene hører hos de ressursene.

**Vanlige kombinasjoner med andre produkter:**
- `eDelivery Building Block` som transportlag under bevisutvekslingen.
- `eID Building Block` og `eIDAS-node (Norge)` for autentisering av brukeren før forhåndsvisning.
- `European Digital Identity Wallet` som det brukerstyrte alternativet til myndighetsstyrt bevisutveksling.
- `Core Vocabularies` og de semantiske modellene som gjør bevisene forståelige på tvers.

**Kildekode:** Ikke offentlig dokumentert. Kildene i denne arbeidsøkten sier ikke om fellestjenestene eller referansekomponentene publiseres som åpen kildekode.

**Lisens:** Ikke offentlig dokumentert.

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov**
  Hele formålet er å fjerne dokumentasjonsarbeid fra brukeren, og forhåndsvisningen gir innsyn og kontroll i det øyeblikket delingen skjer.
- **P4: Del og gjenbruk data**
  Systemet henter data fra kilden i stedet for å be brukeren om kopier, som er engangsprinsippet satt i praksis over landegrenser.
- **P6: Lag digitale løsninger som støtter samhandling**
  Støttes tydelig: bevismegler, tjenestekatalog og semantisk register er bygget for at uavhengige forvaltninger skal kunne samhandle.
- **P7: Sørg for tillit til oppgaveløsningen**
  Bevis hentet direkte fra utstederregisteret er mer pålitelig enn innsendte kopier, og utvekslingen er sikret gjennom eDelivery.

**Spenning og begrensning:** Den viktigste begrensningen ligger mot **P2: Ta arkitekturbeslutninger på rett nivå**. Avgrensningen til listede prosedyrer og bevistyper er bestemt i EU-regelverket, og en norsk virksomhet kan ikke utvide bruken selv om infrastrukturen teknisk sett ville passet. Systemet støtter **P5: Del og gjenbruk løsninger** delvis: fellestjenestene er gjenbrukbare, men hver stat må likevel bygge og drifte sin egen nasjonale plattform, noe som gir høy inngangskostnad. For et konkret case bør det derfor vurderes om bevistypen faktisk er dekket, og om motparten i det aktuelle landet er koblet til, før OOTS legges til grunn.

## Finansiering
**Fakta:** Fellestjenestene finansieres og driftes av Europakommisjonen. Det nordisk-baltiske pilotprosjektet som Norge deltok i, ble finansiert av Nordisk ministerråd og avsluttet i juni 2023.

**Ikke offentlig dokumentert i denne arbeidsøkten:** finansieringsmodellen for norsk plattform og for tilkobling av norske bevisleverandører.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Fellestjenester og arkitektur | Europakommisjonen | Kommisjonens sider om OOTS |
| Regelverksgrunnlag | Forordning (EU) 2018/1724 og gjennomføringsforordning (EU) 2022/1463 | Kommisjonens beskrivelse av rettsgrunnlaget |
| Nasjonal plattform | Den enkelte medlemsstaten | Kommisjonen om at medlemsstatene bygger nasjonale plattformer |
| Norsk koordinering | Digdir | Digdirs omtale av SDG, OOTS og norsk deltakelse i pilotprosjekt |
| Budsjettansvar i Norge | Ikke offentlig dokumentert i denne arbeidsøkten | - |
| Styringsmodell | Gateway Coordination Group under SDG | Kommisjonens omtale av statusdiskusjoner i gruppen |

## Lenke til dokumentasjon
- Om OOTS: https://ec.europa.eu/digital-building-blocks/sites/spaces/OOTS/pages/610468075/About+OOTS
- Digdir om tre EU-regelverk og én digital infrastruktur: https://www.digdir.no/digitalisering-og-samordning/tre-eu-regelverk-en-digital-infrastruktur/8120
- Digdir om prosjekt for testing av SDG og OOTS: https://www.digdir.no/internasjonalt-arbeid/project-testing-single-digital-gateway-once-only-technical-system/5042
- Nordisk ministerråd om Once Only Technical System 2.0: https://www.norden.org/en/project/once-only-technical-system-20-oots

## Kildegrunnlag brukt i utfyllingen
- Europakommisjonen, About OOTS, hentet 24. september 2026.
- Digdir, Tre EU-regelverk, én digital infrastruktur, hentet 24. september 2026.
- Nordisk ministerråd, Once Only Technical System 2.0, hentet 24. september 2026.
- Digdirs side om prosjektet for testing av SDG og OOTS svarte `403` ved maskinell henting 24. september 2026, og er derfor bare brukt som referanse til at prosjektet finnes.
- Lokale kilder: `arkitektur/ressurser/produktnummerering.md`, `arkitektur/kapabiliteter/capabilities.yaml`, `arkitektur/prinsipper/principles.md`, `sources/links.md`.
