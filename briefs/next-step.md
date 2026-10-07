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

## Nye ressurser i prioritert rekkefølge

Før lovene tas inn, skal det besluttes en avgrensningsregel i [decisions.md](./decisions.md): bare
regelverk som direkte regulerer digital samhandling eller deling av opplysninger. Nye kilder legges
i `sources/links.md` når ressursen skrives.

Klare til å skrives, kildesjekket 2026-10-07:

1. `KLASS` (SSB, `Gjenbrukbare løsninger`). Bekreft lisensen i primærkilde.
2. `NSMs grunnprinsipper for IKT-sikkerhet`, versjon 2.1 (ny eierkode `NSM`,
   `Standarder og veiledning`).
3. `KOSTRA` (SSB, `Gjenbrukbare løsninger`). KDD forvalter KOSTRA-forskriften.
4. `Norge digitalt` (Kartverket, `Samhandlingsarenaer og organisering`). Kontroller
   paragrafhenvisningene i geodataloven mot Lovdata.
5. `Utredningsinstruksen` (Finansdepartementet og DFØ, `Økonomiske og juridiske rammer og
   virkemidler`).

Kildesjekket, men med åpne punkter:

6. `Noark 5` versjon 6.0 (ny eierkode for Nasjonalarkivet, `Standarder og veiledning`). Les kravene
   i ny arkivforskrift fra 1.1.2026 i primærkilde.
7. `Digitalsikkerhetsloven` (JD og NSM). Finn forskriften i Lovdata og offisiell status for NIS2 i
   EØS.
8. `Statens standardavtaler` (DFØ, `Standarder og veiledning`). Avklar om bruken er pålagt staten.
9. `Vergemål og fremtidsfullmakter` (Sivilrettsforvaltningen, `Gjenbrukbare løsninger`). Finn
   primærkilde for registeret og rettsgrunnlaget, og avklar forholdet til vergefullmaktene i
   Folkeregisteret og digital fullmakt i `04` Altinn Autorisasjon.
10. `Konsultasjonsordningen mellom staten og kommunesektoren` (KDD og KS). Finn ny adresse for
    temasiden på regjeringen.no.
11. `Ny forvaltningslov` (JD). Opprettes når ikrafttredelsen er fastsatt. Kontroller samtidig
    hjemmelsgrunnlaget for `144` eForvaltningsforskriften.

Ikke kildesjekket ennå:

- `Standarder og veiledning`: `SOSI` (Kartverket) og `Nasjonalt ID-senter` (Politiet).
- `Gjenbrukbare løsninger`: `Digital sykmelding` (NAV), `Fellestjenester BYGG` (DiBK),
  `Nødvarsel` (DSB), `KommuneCSIRT` (KS) og `Lovdatas åpne data og API` (Lovdata).
- `Økonomiske og juridiske rammer og virkemidler`: `Personopplysningsloven og
  personvernforordningen`, `DigiFin` (KS) og `Fremtidens digitale Norge` (KDD).
- `Samhandlingsarenaer og organisering`: `Regionale digitaliseringsnettverk` i kommunesektoren, som
  én samleressurs.

## Andre kandidater

- Nasjonal regulatorisk KI-sandkasse etter KI-forordningen artikkel 57 og 58 (Digdir, Datatilsynet
  og Nkom). Ikke den samme ressursen som `DTIL-001`, se [decisions.md](./decisions.md) 2026-09-30.
- EU-sporet for barn og unge: aldersverifisering etter DSA artikkel 28, og European Learning Model
  med europeiske digitale kvalifikasjonsbevis.
- Batch 3, det internasjonale sporet: `Digital Europe Programme`, `NOBID`,
  `European Digital Identity Cooperation Group`, `OECD OPSI`, `Digital Public Goods Alliance`, EUs
  dataforordninger (`Data Act`, `Data Governance Act` og høyverdidatasett) og nordisk-baltiske
  samarbeidsmekanismer. Bruk samme skille mellom europeisk nivå og norsk implementering som i
  EU-gruppen, se [decisions.md](./decisions.md) 2026-09-24.
- Norske oppføringer i DPG-registeret som ikke er ført: blant annet API-et til `Yr` og
  `SimpleAudit` fra Simula og SimulaMet.
- `FINT Flyt` (Novari), `FIKS IO` (KS), `Legemiddelregisteret`, `Kreftregisteret` og `DHIS2`.
- Åtte KS Digital-tjenester: `Fiks eiendomsavtaler`, `Fiks konsesjon`, `Fiks smittevern`,
  `KS Bibliotek`, `KS Digitalt ledsagerbevis`, `KS Hjelpemiddel`, `KS Kunnskap` og
  `KS Min kommune – barnevern`.
- Fra Digdirs virkemiddeloversikt: `Nasjonal portefølje`, `KI-laben`, `Dynamisk kunnskapsgrunnlag`
  og `Partnerskap med KS`.

## Register og kontroller

- Få `sync-resource-metadata.py` til å oppdatere kapabilitetskoblinger for ressurser som allerede
  finnes i mappingen. I dag blir en ny kobling i en revisjon stille ignorert. Midlertidig
  framgangsmåte er å slette produktet fra mappingen og kjøre `--apply` på nytt.
- Utvide [check-resource-version-sync.py](../tools/check-resource-version-sync.py) slik at
  ressursfiler og mapping-oppføringer uten rad i registeret fanges.
- Varsle når en generert kapabilitetsside er eldre enn forklaringsteksten i mappingen.
- Utvide tegnkodingskontrollene til å fange `æ`, `ø` og `å` som er strippet til ASCII.
- Rydde den gamle fila `137-Forskrift-om-IT-standarder-i-offentlig-forvaltning-v1-codex.md` ut av
  `normerende-ressurser/`.
- Gi `DIGDIR-048` et navn Digdir selv bruker, og rett `Type` i registeret fra `Rammeverk`.
- Følge nye versjoner av kapabilitetsmodellen i `digdir/nasjonal-arkitektur`. Sammenlign på id, og
  kontroller id-settet i `capabilities.yaml` før noe endres.
- Gi ressursmappene navn etter rammeverkskategoriene, etter
  [planen for omdøping av ressursmappene](./arbeidsstyring-og-handover/2026-10-02-omdoping-av-ressursmapper-v1.md).
  Gjennomføres bare når ingen andre økter arbeider i repoet og arbeidstreet er tomt.

## Løse ideer

Ikke besluttet, ikke påbegynt. Står her for ikke å gå tapt, ikke som forpliktelse.

- NAVs `testnorge` og `Dolly` som ressurskandidat. Ikke det samme som Skatteetatens Test-Norge.
- Andre selvstendige tillitstjenester enn ID-porten som egne ressurser.
- Internasjonale referansearkitekturer som sammenligningsgrunnlag, for eksempel KLs felleskommunale
  rammearkitektur, Ena, X-Road, Aula og SS 12000.
- Egne nettsider per ressursbeskrivelse, generert fra markdown.
- Federert synk mot modellrepoet, og eksport til Turtle for kunnskapsgraf.
- Eiernavn i to lag i registeret: visningsnavn og registrert navn fra Enhetsregisteret.
- Repoet som åpen kunnskapskilde for KI-bruk, se
  [2026-03-16-dokumentasjonsassistent-mvp-v1.md](./arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md).

## Kjente blokkere og risiko

- **Repoet er offentlig.** Alt som committes er publisert i samme øyeblikk, og historikken er
  permanent.
- **Ingen lokal Hugo-build.** Nettstedet kan ikke ses før det er publisert, og feil i
  mal-JavaScript stopper først i CI.
