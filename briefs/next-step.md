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

- Kjøre batch 3, det internasjonale sporet: `Digital Europe Programme`, `NOBID`, `European Digital
  Identity Cooperation Group`, `OECD OPSI` og konkrete nordisk-baltiske samarbeidsmekanismer. Eget
  vurderingsspor for `eIDAS 2.0`, `Single Digital Gateway`, `OOTS`, `Interoperable Europe Act` og
  `European Digital Identity Wallet`.
- Avklare tre spørsmål før batch 3 kan gjennomføres:
  - Skal `Digital Europe Programme` og `OECD OPSI` registreres som egne ressurser, eller bare inngå
    i en bredere ressurs?
  - Er `NOBID` en selvstendig ressurs eller først og fremst et prosjekt-/programspor?
  - For EU-nivå må det skilles tydelig mellom juridisk ramme, felles internasjonal infrastruktur,
    norsk implementering og norsk løsning, slik at registeret ikke får duplikater.
- Kontrollere hjemmelsgrunnlaget for `DIGDIR-066` eForvaltningsforskriften på nytt når ny
  forvaltningslov (lov 20. juni 2025 nr. 81) settes i kraft. Ikrafttredelsen er ikke bestemt.
  Forskriften er i kraft i dag, så `v1` og status `aktiv` står inntil videre.
- Gjennomføre canvas-konsekvensanalyse av kapabilitetsbeskrivelsene fra modelloppdateringen.
  Navne- og ID-effekten er håndtert, men den brede faglige vurderingen av nye beskrivelser mot
  ressurscanvasene gjenstår. Grunnlaget ligger i
  [2026-06-18-kapabilitetsendringer-konsekvensanalyse-v1.md](./arbeidsstyring-og-handover/2026-06-18-kapabilitetsendringer-konsekvensanalyse-v1.md).
- Følge opp `DIGDIR-039`, `DIGDIR-040` og `DIGDIR-041` med vanlig kvalitetsrevisjon hvis de viser
  svak kildeforankring, tynn kapabilitetskobling eller ujevn beslutningsstøtte.
- Vurdere `HELFO-001` KUHR, eller en egen avklaring av eier- og forvaltningslinjen for `HDIR-001`.
- Gå gjennom `v0`-beskrivelsene og løfte dem til `v1`. De mangler typisk `Navn`,
  `Forpliktelsesnivå og etterlevelse`, `Typiske analyse- og beslutningssituasjoner` og
  `Konsekvens ved manglende bruk eller avvik`. [check-resource-structure.py](../tools/check-resource-structure.py)
  lister dem med `--advarsler`. Når gjelden er nede, kan kjernefeltene i kontrollen strammes inn.

Kandidater som er identifisert, men ikke vurdert ferdig:

- `Legemiddelregisteret` som egen ressurs, nå som `FHI-004` er avgrenset som historisk registerspor.
- `DHIS2`, med eksplisitt opptaksvurdering mot styringsreglene for sektorspesifikke ressurser.
- `SIMPL` (Smart Middleware Platform), med avklaring av norsk anvendbarhet.
- `Kreftregisteret`, hvis det kommer tydeligere casebehov.
- `FIKS IO`: egen ressurs, eller fortsatt teknisk komponent under `FIKS Melding`?

Restkandidater fra Digdirs virkemiddeloversikt, gjennomgått 2026-09-01. Lista navngav rundt seksti
virkemidler, og alle unntatt disse er registrert. Vurderingene under er foreløpige og bygger på
navnet i oversikten, ikke på egen kildesjekk.

Veiledersporet fra denne lista er nå komplett, og det eneste uregistrerte juridiske virkemiddelet er
tatt inn. Det som gjenstår er de organisatoriske og økonomiske ordningene under.

Organisatoriske ordninger som krever avklaring før de kan vurderes mot opptakskravene:

- `Nasjonal portefølje`. Foreløpig vurdering: usikker. Må avklares om dette er en konkret ressurs
  eller primært et styringsprinsipp og en arbeidsform.
- `KI-laben`. Foreløpig vurdering: sannsynligvis del av `DIGDIR-057` KI Norge, ikke egen ressurs.
  Avgrensningen må sjekkes mot hvordan KI Norge er beskrevet.
- `Dynamisk kunnskapsgrunnlag`. Foreløpig vurdering: uklart hva ordningen konkret er. Krever
  kildesjekk før den kan vurderes.
- `Partnerskap med KS`. Foreløpig vurdering: kan være dekket av DSOP-samarbeidet og Skate. Vurderes
  mot eksisterende dekning før det eventuelt beskrives som egen samhandlingsressurs.
- `Brukerrådet`. Foreløpig vurdering: bør vurderes som råd, ikke som konferanse. Står under
  `Konferanser` i kildelista, men navnet tyder på et fast organ. Sjekk mandat og møtefrekvens.

Økonomisk virkemiddel:

- `Konkurranseevnefondet (EKF)`. Foreløpig vurdering: lavere prioritet, men bør vurderes for NA-verdi
  og forankring.

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
- Rydde eller regenerere de avledede produktlistene i
  [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml).
  Toppnivået er korrekt, men listene under kapabilitetsseksjonene har eldre versjonsmetadata for
  tolv ressurser. Ingen kontroll fanger intern inkonsistens i fila.
- Planlegge trinnvis innføring av feltet `Type` i ressursbeskrivelser, med samme kategorier som i
  registeret, slik at koblingen mellom register og enkeltbeskrivelser blir entydig.
- Vurdere om KS-sporet trenger egen struktur for overordnet registerfamilie mot underliggende
  undertjenester, nå som `Fiks register` er strammet inn som tilgangslag.
- Vurdere om `DIGDIR-048` Rammeverk for innovasjon i offentlig sektor bør stå som normerende
  ressurs eller avgrenses tydeligere.

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
