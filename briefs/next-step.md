---
date: 2026-09-01
author: claude
status: aktiv
topic: neste-steg
---

# Neste steg

Fila er et planleggingsverktøy. Den viser hva som er åpent nå, ikke hva som har vært gjort.

- **Hva som er gjort** ligger i Git-historikken (`git log`) og på nettstedet.
- **Varige metode- og strukturvalg** ligger i [decisions.md](./decisions.md).
- **Større arbeidsnotater og handover** ligger i [arbeidsstyring-og-handover/](./arbeidsstyring-og-handover/).

Punkter som er ferdige, fjernes herfra i stedet for å bli stående som logg. Punkter som ikke er
fulgt opp og heller ikke er besluttet, flyttes ned til `Løse ideer`.

## Aktive prioriteringer

### Ressursarbeid

- Fullføre innholdsrevisjonen av `Standarder og veiledning`. Kartleggingen 2026-09-10 viser at kategorien er i bedre stand enn ventet: alle tretti
  har de tre analysekritiske feltene og ingen har pseudokilder. Den reelle svakheten er tynt
  innhold og manglende merking av fakta og deduksjon. Toogtyve av tretti filer har null merker.
  Påstanden om at alle brukte faktiske prinsippnavn med riktig P-kode holdt ikke helt:
  `115` oppgav `P3: Ta hensyn til juridiske og organisatoriske rammer`, mens prinsippet heter
  `Bidra til digitaliseringsvennlige regelverk`. Rettet i `v2`. En mekanisk kontroll av alle 141
  gjeldende filer 2026-09-11 fant ingen andre avvik.
  Revidert etter mønstersøket: `104`, `99`, `100` og `114` 2026-09-17, og `105`, `107`, `108`,
  `116`, `117` og `138` 2026-09-25, pluss `137` i `rammer-og-virkemidler/`. Alle hadde de
  samme fire manglene: formuleringen `Ressursen er viktig fordi` i åpningen, kapabiliteter uten
  forklaring, ingen merking av fakta og deduksjon, og forpliktelsesnivå uten å si om hjemmel
  finnes. Runden 2026-09-25 viste også at kildene må leses på nytt, ikke bare språket: `107` har
  ingen åpen kilde som beskriver ressursen, og hovedkilden i `108` nevnte ikke dataområder. De gjenstående `-codex`-filene etter ordantall er `98`,
  `112`, `89`, `109`, `85`, `101`, `102` og `87`. `89` og `109` er de to siste filene i porteføljen
  med kapabilitetspunkter uten forklaring.
  Blokkeringen fra 2026-09-10 var delvis feildiagnostisert. `104` var ikke utilgjengelig; URL-en i
  fila var feil. `/orden-eget-hus/orden-eget-hus/2717` gir 403, men
  `/informasjonsforvaltning/veileder-orden-i-eget-hus/2716` virker. Lærdommen er å prøve alternative
  adresser før en kilde føres som utilgjengelig.
- Følge opp de fire uavklarte punktene i arbeidsdelingen mellom `21` Altinn.no og `18` Norge.no.
  Selve overlappen er dokumentert i begge canvasene 2026-09-18, se [decisions.md](./decisions.md).
  Det som gjenstår er å finne ut om noe av dette faktisk er avklart et sted vi ikke har funnet:
  hvor grensen går for innbyggerrettede Altinn-tjenester, hvem som avgjør enkelttilfeller, om
  Norge.no har en egen publisert innholdsstrategi, og hva statusen er for den mulige sammenslåingen
  av de to portalene som Altinns innholdsstrategi nevner. Dette krever kilder vi ikke fant i åpne
  søk, og bør antakelig avklares direkte med produktmiljøene framfor gjennom flere søkerunder.
- Rette den gjenstående referansen til det gamle navnet `Altinn Portal` i
  `23-Altinn-3-Melding-produkt-canvas-v5-codex.md`, som er gjeldende versjon. Den står i ett
  kulepunkt under `Vanlige kombinasjoner`. Ikke verdt en egen versjon for ett ord; tas ved neste
  ordinære revisjon av fila. Eldre versjoner og historiske notater beholder navnet som historikk.
- Melde fra om, eller finne ny adresse for, om-sidene til Norge.no. Både
  `www.norge.no/om-norge-no` og `www.norge.no/en/about-norgeno` svarer `404`. De var
  primærkilder i `v3` av `18`, og er nå merket som døde i `sources/links.md`. Portalens forsiden
  lot seg heller ikke lese maskinelt, så vi har i dag ingen egenpresentasjon fra Norge.no selv.
- Bruke regelen for `Veiledning`-kapabilitetene fra 2026-09-25 (se [decisions.md](./decisions.md))
  på de normerende ressursene som er publisert veiledning, men ikke har
  `Utvikling og formidling av veiledning`: `85`, `89`, `98`, `100`, `101`, `102`, `87`, `104` og
  `105`. Hovedkapabiliteten nevner referansearkitekturer, prinsipper og beste praksis uttrykkelig.
  Tas ved neste ordinære revisjon av hver fil framfor som egne versjoner; de fleste står uansett i
  køen av `-codex`-filer over.
- Vurdere om noen ressurs faktisk leverer `Tjenestekjeder`. Etter opprydningen 2026-09-25 står
  kapabiliteten bare på `100`, som normerer beskrivelsen av kjeder, og ingen operativ ressurs
  realiserer den. Nærmeste kandidater er `22` Dialogporten og `87` Arkitektur for hendelser.
- Fylle det valgfrie delfeltet `**Lisens:**` i de normerende ressursene der innholdet gjenbrukes
  maskinelt: `72` FINT Informasjonsmodell, `82` VIGO Kodeverk, `149` Felles informasjonsmodeller og
  `55` Core Vocabularies. `151` Grep og `164` Barnevernsfaglig kvalitetssystem oppgir allerede NLOD
  i brødteksten og kan flyttes over til feltet. Kan gjøres uten versjonsløft, siden feltet er nytt
  i malen.
- Følge opp lisensfeltet i de operative filene som hadde det fra før: `41`, `42` og `43` sier
  `Åpen kildekode` uten kontrollert lisens og uten `Repositorium`, og `166` Simpl oppgir EUPL-1.2
  uten at det er kontrollert mot lisensfila. Vurdere også om `94` Fiks protokoll og `83` FINT
  Arkivintegrasjoner har riktig `Kildekode`-status, siden relaterte spesifikasjoner og
  `fint-flyt`-repoer er publisert.
- Prøve `144` eForvaltningsforskriften for `Regelverkstolkning` med samme test som ble brukt på
  `137`: en forskrift er regelverket som tolkes, ikke en ressurs som tolker.
- Rydde den gamle fila `137-Forskrift-om-IT-standarder-i-offentlig-forvaltning-v1-codex.md`, som
  fortsatt ligger i `normerende-ressurser/` selv om ressursen er flyttet til
  `rammer-og-virkemidler/`. Den er historikk og røres ikke av kontrollene, men plasseringen er
  misvisende.
- Vurdere senere om delkapabilitetene under `Veiledning` fungerer optimalt. Modellen er arvet fra
  rammeverket i `digdir/nasjonal-arkitektur`, så en endring krever forankring der og gjøres ikke
  her. Utfordringene slik de står 2026-09-25:
  - `Anvendelse av veiledning` er definert som virksomhetens egen evne til å bruke veiledere i
    prosjekter. Nesten ingen nasjonal ressurs realiserer den; etter regelen i
    [decisions.md](./decisions.md) står bare `113` og `121` igjen.
  - Modellen mangler kompetanse og kompetanseutvikling, slik at `117`, tilskuddet til digital
    kompetanse og mulige kandidater som DigiUng ikke har noen naturlig kobling. En omdøping til
    noe som `Kompetanse og støtte til anvendelse` kunne løst begge punktene.
  - Beskrivelsen av hovedkapabiliteten nevner både standarder og regelverkstolkning, som
    overlapper `Standardisering` og `Juridisk samhandling: Regelverkstolkning`.
  - Delkapabilitetene deler etter aktør, den som lager og den som bruker, ikke etter type
    veiledning. `Utvikling og formidling av veiledning` blir derfor en samlepost for alle
    veiledere, med lite analyseverdi.
- Sammenligne den øvrige porteføljen mot Digdirs egen fellesløsningsoversikt
  (https://samarbeid.digdir.no/felleslosninger/felleslosninger/1309). Sammenligningen 2026-09-17
  fant to avvik: `Arbeidsflate`, som nå er opprettet som `165`, og `ki.norge.no`, som er dekket som
  publiseringsflate i `125-KI-Norge-v3-claude.md` framfor som egen ressurs. Prosjektsporet på siden
  (`Digitalt dødsbo`, `Digital representasjon`, `MinID i skolen`, `Moderniseringen av Altinn`,
  `Ny finansieringsmodell for fellesløsningene`) er bevisst holdt utenfor: oversikten dekker
  ressurser, ikke prosjekter. `Ny finansieringsmodell for fellesløsningene` bør likevel følges,
  fordi utfallet treffer både `120` Styringsrådet og `142` Medfinansieringsordningen.
- Etterfylle rettslig forankring i `standarder og veiledning` etter regelen som ble lagt inn
  2026-09-13, se [decisions.md](./decisions.md). Alle tretti gjeldende filer er gjennomgått
  2026-09-13, og behovet er mindre enn ventet: kategorien er allerede eksplisitt om manglende
  binding. Filer som `114`, `117`, `138` og `146` sier rett ut at de ikke er juridisk bindende,
  som er nettopp det regelen ber om. `101` eMelding er forbilledlig: den forklarer at
  referansearkitekturer ikke er pålagt, men at binding kan oppstå gjennom digitaliseringsrundskrivet
  eller Referansekatalogen.
  Det som gjenstår:
  - `87-Arkitektur-for-hendelser` oppgir `anbefalt/styrende` uten å si hva styringen bygger på og
    uten å si at hjemmel mangler. Eneste reelle kandidat, og det mangler bare en setning. Tas ved
    neste ordinære revisjon av fila framfor som egen versjon.
  - `86-Referansekatalogen-for-IT-standarder` navngir forskriften og sier at avvik fra en
    obligatorisk standard er brudd på et rettslig krav, men har ingen kobling til
    `Juridisk samhandling`. Vurder om katalogen tolker regelverk eller bare er hjemlet i det.
    Bare én av de tretti filene har juridisk kapabilitetskobling i dag.
- Kjøre en strukturrevisjon av eksisterende ressursbeskrivelser mot de oppdaterte malene. Malene og
  instruksene er harmonisert, og navnegjelden i `Ressurskategori` og `Type ...` er ryddet i
  gjeldende versjoner. Det som gjenstår er å vurdere selve innholdet i eldre beskrivelser mot det
  hevede nivået i malen, særlig `Modenhet`, `Utfordringer og risiko`, `Forvaltning` og avsnittet om
  spenning og begrensning i prinsippvurderingen. Dette er en innholdsjobb per fil, ikke en
  mekanisk retting, og bør tas kategorivis.

- Vurdere EU-standardsporet for barn og unge, som eget spor foran den bredere batch 3. To kandidater
  er avklart nok til å planlegges, se [decisions.md](./decisions.md) 2026-09-08:
  - Aldersverifisering etter DSA artikkel 28, med Kommisjonens hvitmerkede løsning. Skal avklares
    mot norsk gjennomføring av DSA og mot forslaget om aldersgrense i sosiale medier, og mot om
    norsk anvendelse skal skje gjennom EUDI-lommebok eller nasjonal løsning.
  - European Learning Model og europeiske digitale kvalifikasjonsbevis. Skal avklares mot `Grep`,
    `VIGO Kodeverk` og `utdanning.no`, som i dag klassifiserer mot NUS og STYRK uten dokumentert
    mapping mot ESCO og ELM.
- Gå gjennom de åtte norske oppføringene i DPG-registeret og avklare hvilke som treffer ressurser i
  oversikten. Alle de åtte er oppført i DPG Registry, så spørsmålet er opptak i NA-oversikten, ikke
  om de eksisterer. `Altinn Studio` og `Designsystemet` er allerede ført. Bekreftet uten å være
  vurdert ennå er API-et til `Yr` og `SimpleAudit` fra Simula og SimulaMet. De øvrige oppføringene
  må vurderes direkte mot registeret og opptakskriteriene.
- Vurdere `Digital Public Goods Alliance` som egen ressurs i det internasjonale sporet. Norge er
  medstifter sammen med UNICEF, iSPIRT og Sierra Leones regjering, og DPG-standarden med sine ni
  krav fungerer som et normerende rammeverk for gjenbrukbarhet. Hører i samme nivåavklaring som
  resten av batch 3.
- Fullføre barn-og-unge-sporet med de gjenstående kandidatene: `Barnehagefakta` som mulig peker
  under `UDIR-002` framfor egen ressurs, `DigiUng` som mulig samhandlingsarena, og
  `Barnevernsfaglig kvalitetssystem` som fortsatt er ubekreftet i kildene.
- Kjøre resten av batch 3, det internasjonale sporet: `Digital Europe Programme`, `NOBID`,
  `European Digital Identity Cooperation Group`, `OECD OPSI` og konkrete nordisk-baltiske
  samarbeidsmekanismer. EU-gruppen `EU-001` til `EU-011` er skrevet som `v1` 2026-09-24, se
  [decisions.md](./decisions.md), og dekker `OOTS`, `Interoperable Europe Act` og
  `European Digital Identity Wallet`. `eIDAS 2.0` og `Single Digital Gateway` er ikke opprettet som
  egne ressurser: begge er omtalt som rettsgrunnlag i `EU-001` og `EU-005`, og en egen ressurs bør
  bare vurderes hvis forordningene trengs som selvstendige virkemiddelressurser på linje med
  `EU-009`.
- Avklare forkortelsen `VIO` i registernavnet `Videokonsultasjon (VIO)` for `NHN-005`. Forkortelsen
  er ikke funnet i åpne kilder hos Norsk helsenett eller Helsenorge 2026-09-25. Navnet i registeret
  er beholdt uendret inntil den er avklart, og usikkerheten står i ressursfila. Avklares enklest
  direkte med Norsk helsenett.
- Avklare om `Helse Nord` bruker `NHN-005` Videokonsultasjon. Norsk helsenett navngir Helse Vest,
  Helse Sør-Øst og Helse Midt-Norge, men ikke Helse Nord, og kildene sier ikke om det skyldes
  manglende innføring eller et annet valg.
- Vurdere `FINT Flyt` som egen ressurs. `NOVARI-008` FINT Arkivintegrasjoner er arkivsporet på
  plattformen, men selve integrasjonsplattformen er ikke registrert. Novari fører begge som egne
  tjenester.
- Følge forvaltningsmodellen for `EU-012` Simpl etter den treårige kontraktsperioden. Hvem som
  overtar eierskapet er ikke dokumentert, og det er den vesentligste usikkerheten for om plattformen
  kan legges til grunn i norske planer. Norsk deltakelse i Simpl er heller ikke dokumentert og bør
  avklares med Digdir.
- Avklare norsk status for `EU-005` OOTS. Kildene i arbeidsøkta 2026-09-24 dokumenterer ikke hvilke
  norske bevisleverandører og bevismottakere som er koblet til, og Digdirs egen prosjektside svarte
  `403` ved maskinell henting. Bør avklares direkte med Digdir framfor gjennom flere søkerunder.
- Avklare tre spørsmål før batch 3 kan gjennomføres:
  - Skal `Digital Europe Programme` og `OECD OPSI` registreres som egne ressurser, eller bare inngå
    i en bredere ressurs? For OPSI er ett grunnlag nå avklart: Digdir har rollen som nasjonalt
    kontaktpunkt i nettverket, og Norge sluttet seg til OECDs erklæring om innovasjon i offentlig
    sektor 22. mai 2019 sammen med 39 andre land.
  - Er `NOBID` en selvstendig ressurs eller først og fremst et prosjekt-/programspor?
  - Skillet mellom juridisk ramme, felles internasjonal infrastruktur, norsk implementering og norsk
    løsning er avklart for EU-gruppen 2026-09-24, se [decisions.md](./decisions.md). De elleve
    EU-filene beskriver det europeiske nivået, og norsk implementering er holdt utenfor som eget
    spor. Samme skille må brukes for de gjenstående kandidatene i batch 3.
- Kontrollere hjemmelsgrunnlaget for `DIGDIR-066` eForvaltningsforskriften på nytt når ny
  forvaltningslov (lov 20. juni 2025 nr. 81) settes i kraft. Ikrafttredelsen er ikke bestemt.
  Forskriften er i kraft i dag, så `v1` og status `aktiv` står inntil videre.
- Gjennomføre canvas-konsekvensanalyse av kapabilitetsbeskrivelsene fra modelloppdateringen.
  Navne- og ID-effekten er håndtert, men den brede faglige vurderingen av nye beskrivelser mot
  ressurscanvasene gjenstår. Grunnlaget ligger i
  [2026-06-18-kapabilitetsendringer-konsekvensanalyse-v1.md](./arbeidsstyring-og-handover/2026-06-18-kapabilitetsendringer-konsekvensanalyse-v1.md).
- Følge opp `DIGDIR-039`, `DIGDIR-040` og `DIGDIR-041` med vanlig kvalitetsrevisjon hvis de viser
  svak kildeforankring, tynn kapabilitetskobling eller ujevn beslutningsstøtte. For `107`
  Kunnskapsgrunnlag og KPI-er for datadeling fant revisjonen 2026-09-25 ingen åpen kilde som
  beskriver ressursen. Avklar med Digdir om den finnes som eget produkt eller er det samme som
  statusmålingen av digitaliseringsstrategien; hvis ikke bør den tas ut eller slås sammen.
- Vurdere `HELFO-001` KUHR, eller en egen avklaring av eier- og forvaltningslinjen for `HDIR-001`.
- Få `sync-resource-metadata.py` til å oppdatere kapabilitetskoblinger for ressurser som allerede
  finnes i mappingen. Verktøyet oppdaterer i dag navn, versjon, forfatter, sti og forklaringer, men
  aldri selve koblingslista. Legger en revisjon til en ny kapabilitet, blir den stille ignorert, og
  ressursen dukker aldri opp på den kapabilitetssiden. Oppdaget da `DIGDIR-028` fikk `EU standarder`
  i `v2`. Midlertidig framgangsmåte er å slette produktet fra mappingen og kjøre `--apply` på nytt,
  slik at det bygges opp igjen fra registeret og ressursfila.
- Utvide tegnkodingskontrollene til å fange tegn som er strippet til ASCII, ikke bare mojibake i
  form av doble tegnsekvenser. Bakgrunnen er logget i [decisions.md](./decisions.md) 2026-09-04:
  to ressursfiler var systematisk strippet for `æ`, `ø` og `å` uten at
  [check-mojibake.ps1](../tools/check-mojibake.ps1) eller
  [safe_bulk_text_repair.py](../tools/safe_bulk_text_repair.py) reagerte. Filene er rettet, men
  kontrollen som skulle fanget dem finnes fortsatt ikke. En mulig tilnærming er en ordliste over
  vanlige strippede former, eller en test på om en norsk tekstfil har mistenkelig få norske tegn
  i forhold til lengden.
- Vurdere et tredje nivå `valgfrie` per kategori i `check-resource-structure.py`, ved siden av
  `kjernefelt` (feil) og malens overskrifter (advarsel). Da kan et nytt felt legges inn uten å bli
  gjeld i hele kategorien før etterfyllingsrunden er kjørt.
- Vurdere om `Ressurskategori` skal legges til i den operative malen. Feltet finnes i de tre andre
  kategoriene, men i ingen av de 127 operative filene. Kategorien er utledbar fra katalogen og fra
  registeret, så dette er et skjemaspørsmål og ikke gjeld: enten skal feltet være i alle fire
  kategorier, eller i ingen.

Kandidater som er identifisert, men ikke vurdert ferdig:

- `Legemiddelregisteret` som egen ressurs, nå som `FHI-004` er avgrenset som historisk registerspor.
- `DHIS2`, med eksplisitt opptaksvurdering mot styringsreglene for sektorspesifikke ressurser.
- `SIMPL` (Smart Middleware Platform), med avklaring av norsk anvendbarhet.
- `Kreftregisteret`, hvis det kommer tydeligere casebehov.
- `FIKS IO`: egen ressurs, eller fortsatt teknisk komponent under `FIKS Melding`?
- Åtte KS Digital-tjenester som ikke er vurdert mot opptakskravene: `Fiks eiendomsavtaler`,
  `Fiks konsesjon`, `Fiks smittevern`, `KS Bibliotek`, `KS Digitalt ledsagerbevis`,
  `KS Hjelpemiddel`, `KS Kunnskap` og `KS Min kommune – barnevern`.

Restkandidater fra Digdirs virkemiddeloversikt, gjennomgått 2026-09-01. Lista navngav rundt seksti
virkemidler, og alle unntatt disse er registrert.

Veiledersporet fra denne lista er komplett, og det eneste uregistrerte juridiske virkemiddelet er
tatt inn. `Brukerrådet` og `Konkurranseevnefondet` er kildesjekket og avgjort, se
[decisions.md](./decisions.md).

Parkert. Ikke opprett ressursbeskrivelse for disse nå. De er ikke avvist, men ingen av dem er
avklart godt nok til at en beskrivelse ville blitt annet enn gjetning. Vurderingene under bygger på
navnet i Digdirs virkemiddeloversikt, ikke på egen kildesjekk, og en ny runde må starte med
kildesjekk:

- `Nasjonal portefølje`. Må avklares om dette er en konkret ressurs eller primært et
  styringsprinsipp og en arbeidsform.
- `KI-laben`. Sannsynligvis del av `DIGDIR-057` KI Norge, ikke egen ressurs. Avgrensningen må
  sjekkes mot hvordan KI Norge er beskrevet.
- `Dynamisk kunnskapsgrunnlag`. Uklart hva ordningen konkret er.
- `Partnerskap med KS`. Kan være dekket av DSOP-samarbeidet og Skate. Vurderes mot eksisterende
  dekning før det eventuelt beskrives som egen samhandlingsressurs.

Møteplasser og arrangementer. Foreløpig vurdering: faller utenfor opptakskravene i
[decisions.md](./decisions.md), som holder arrangementer og små møteplasser utenfor oversikten. Tatt
med her slik at neste gjennomgang slipper å gjøre vurderingen på nytt:

- `Altinn-kaffen` og `Samskapingsverkstedet`: for små til å bære en egen ressursbeskrivelse.
- `Nettverk for veiledningsaktører informasjonssikkerhet`: vurderes mot `DIGDIR-056` Felles sikkerhet
  i forvaltningen og `NIFS`, som begge er registrert.
- `NOKIOS`, `Digitaliseringskonferansen` og `eIDAS-konferansen`: arrangementer, ikke ressurser.

### Register og kontroller

- Utvide [check-resource-version-sync.py](../tools/check-resource-version-sync.py) slik at
  ressursfiler og mapping-oppføringer uten rad i registeret fanges. Kontrollen validerer i dag at
  pekere fra registeret stemmer, ikke at alt som finnes er registerført. Denne blindsonen gjorde at
  løpenr 21 og 69 lå uregistrert uoppdaget.
- Fange opp at genererte kapabilitetssider viser utdatert forklaringstekst. Kontrollen sammenligner
  versjoner og stier, ikke selve teksten, og melder `synkronisert` selv når en side viser en eldre
  variant av `explanation` enn den som står i kapabilitetsmappingen. Konkret tilfelle: MinID fikk ny
  forklaringstekst i mappingen 2026-08-28, men kapabilitetssidene var sist regenerert 2026-06-25, så
  nettstedet viste den gamle teksten i over to måneder uten at noen kontroll sa fra. Enten bør
  kontrollen sammenligne teksten, eller den bør varsle når en generert side er eldre enn kilden sin.
- Rette `sync-resource-metadata.py` etter funnene fra
  [check-capability-explanations.py](../tools/check-capability-explanations.py) 2026-09-25:
  - Forklaring på samme linje som merkelappen blir aldri ført over til mappingen, fordi hele linja
    leses som merkelapp. Det gjelder 196 punkter i 61 filer, og mappingen har eldre tekst for 192 av
    dem. Bør rettes før eller sammen med etterfyllingen, ellers kommer nye forklaringer ikke fram.
  - Merkelapper uten prefiks (`**Samordning**`) blir aldri oppdatert, fordi sync slår opp på
    `Hoved: Del`. Gjelder 16 punkter i `85`, `87`, `98`, `101`, `102`, `107` og `108`.
  - Labelkontrollen i `check-resource-version-sync.py` ser bare fete merkelapper, så merkelapper
    uten fet skrift blir aldri kontrollert.
- Flytte tekst som står etter kulelista under `## Kapabiliteter` foran lista, og rense de
  forurensede forklaringene i mappingen. Kontrollen gir merknad for 57 filer, og 18 forklaringer i
  mappingen har fått slik tekst inn: `27` Fiks SvarUt har `Grunnlag`-teksten, og `41`–`45`,
  `53`–`56`, `74`, `79`, `83`, `90`–`92`, `94` og `166` har avsnittet «Koblingene er satt fordi …».
  Rettingen må gjøres i ressursfila, siden sync ellers skriver feilen inn igjen.
- Kjøre `check-capability-explanations.py --strict` på hele porteføljen når `89` og `109` er fylt
  ut. Til da gjelder `--new-only --strict` for endrede filer. Korte forklaringer (11 punkter, mest i
  eldre operative `-codex`-filer) er advarsel og skal ikke gi feilkode.
- Planlegge trinnvis innføring av feltet `Type` i ressursbeskrivelser, med samme kategorier som i
  registeret, slik at koblingen mellom register og enkeltbeskrivelser blir entydig.
- Vurdere å gi `DIGDIR-048` et navn Digdir selv bruker, for eksempel `Veiledning om innovasjon i
  offentlig sektor`, og rette `Type` i registeret fra `Rammeverk`. Kategorien er avgjort
  2026-09-25, se [decisions.md](./decisions.md), men registeret bruker fortsatt det gamle navnet
  og typen.

## Løse ideer

Ikke besluttet, ikke påbegynt. Står her for ikke å gå tapt, ikke som forpliktelse.

- **Forhåndsvisning av nettstedet før publisering.** En egen arbeidsflyt som bygger på branch og
  laster opp resultatet som artefakt, slik at endringer kan ses før de treffer `main`. Vurdert
  2026-09-01 og lagt bort inntil videre til fordel for å prøve og feile direkte mot `main`.
- **Egne nettsider per ressursbeskrivelse.** Generatoren lager en avledet Hugo-side per ressurs, med
  lenke tilbake til originalfila på GitHub. Kilden forblir markdown i `arkitektur/ressurser/`.
- **Federert synk mot modellrepoet.** Et eget repo (`digdir/na-sync-pipeline`) som henter siste
  modell fra `digdir/nasjonal-arkitektur`, lager differanserapport og åpner PR automatisk. Ideen er
  ikke forankret hos Digdir og er ingen besluttet plan.
- **Turtle- og grafspor.** Eksport til Turtle for kunnskapsgraf og SPARQL-søk, som eget spor uten å
  blokkere ordinær synk.
- **Viderekobling fra gamle web-URL-er.** Hugo `aliases` i `generate-products.ps1` for URL-er som
  forsvinner ved omstrukturering. Vurdert 2026-09-01 og lagt bort: adressene det gjaldt viste feil
  innhold, og nettstedet er merket som under arbeid.
- **Evalueringsrubrikk i analysemalen** med score for sporbarhet, gjenbrukbarhet, styringsrelevans
  og presisjon.
- **Eiernavn i to lag** i ressursregisteret: lesbart visningsnavn og registrert navn fra
  Enhetsregisteret, før en eventuell større navneharmonisering.
- **Andre selvstendige tillitstjenester** som i dag bare er omtalt indirekte gjennom ID-porten:
  egne ressurser, eller eksplisitt avgrenset i ID-porten-canvaset?
- **Repoet som åpen kunnskapskilde for KI-bruk.** Ingen beslutning om egen assistent-MVP; skissen
  beholdes som arbeidsnotat i
  [2026-03-16-dokumentasjonsassistent-mvp-v1.md](./arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md).
  Lavterskelsporet er tydelig README og struktur, veiledning for KI-bruk med krav om kildehenvisning
  tilbake til repo-filer, og jevn kvalitet i ressursfilene.

## Kjente blokkere og risiko

- **Repoet er offentlig.** Alt som committes er publisert i samme øyeblikk, og historikken er
  permanent. Sletting i en senere commit fjerner ingenting.
- **Ingen lokal Hugo-build.** `hugo` er ikke installert i arbeidsmiljøet, så nettstedet kan ikke ses
  før det er publisert. Konsekvensen ble konkret 2026-08-28, da en syntaksfeil i mal-JavaScript
  passerte alle lokale kontroller og først stoppet i CI.
- **Eldre ressursbeskrivelser** gir ujevn retrieval-kvalitet og må forbedres gradvis.
- **Skillet mellom arbeidsgrunnlag og godkjent innhold** er fortsatt utydelig flere steder i
  ressursbeskrivelsene.
