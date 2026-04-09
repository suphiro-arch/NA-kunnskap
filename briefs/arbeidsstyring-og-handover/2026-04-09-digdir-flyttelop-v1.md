---
date: 2026-04-09
author: codex
status: gjennomfort
topic: første sektorvise flytteløp for Digdir
sources:
  - arkitektur/produkter/produktnummerering.md
  - arkitektur/produkter/produktbeskrivelser/
  - web/hugo-prototype/scripts/generate-products.ps1
  - web/hugo-prototype/scripts/generate-capabilities.py
---

# Første sektorvise flytteløp: Digdir

Dette notatet konkretiserer første flytteløp fra gammel produktstruktur til ny ressursstruktur.

Målet er å flytte første større, sammenhengende operative bolk uten å bryte:
- registerføring i `arkitektur/produkter/produktnummerering.md`
- webgenerering i `web/hugo-prototype/`
- tegnkodingskontroll
- sporbarhet mellom gammel og ny struktur

## Valgt første bolk

Første flytteløp bør være **Digdir-bolken**.

Begrunnelse:
- Digdir har mange eksisterende beskrivelser på relativt likt modenhetsnivå.
- Porteføljen dekker flere ressurskategorier innen samme operative hovedtype.
- Webgrunnlaget er allerede sterkt eksponert mot Digdir-ressursene.
- Vi får testet overgang for felleskomponenter, plattformer, registre, portaler og fellesløsninger i samme løp.

## Arbeidsregler for flytteløpet

### Hva som flyttes

- Bare **siste registrerte versjon** av hver ressurs flyttes i første løp.
- Målkatalog for denne bolken er `arkitektur/ressurser/operative-losninger-og-tjenester/`.
- Registermasteren forblir `arkitektur/produkter/produktnummerering.md`.

### Hva som ikke flyttes i første løp

- Eldre versjoner blir stående i `arkitektur/produkter/produktbeskrivelser/` som historisk arkiv.
- Ressurser som ikke har beskrivelse ennå, flyttes ikke.
- `Altinn Portal` inngår ikke i dette løpet fordi den ikke står i operativt register som aktiv Digdir-ressurs.
- `Peppol eDelivery` inngår ikke i dette løpet fordi den er registrert under `OPP`, ikke `DIGDIR`.

### Prinsipp for filnavn

Eksisterende filnavn beholdes i første migrering, selv om de fortsatt inneholder `produkt-canvas`.

Begrunnelse:
- minst mulig risiko i første løp
- enklere oppdatering av register- og webpekere
- reduserer behov for samtidige navne- og strukturendringer

Et senere løp kan rydde i navnekonvensjon hvis vi ønsker å gå fra `produkt-canvas` til en bredere ressursnavngivning.

## Sanity check: navnekonvensjon før flytting

Det finnes nå to navnekonvensjoner i repoet:

1. Eldre og etablerte produktfiler under `arkitektur/produkter/produktbeskrivelser/`
   - format: `NN-<navn>-produkt-canvas-vX-<forfatter>.md`
   - sterkt koblet til eksisterende produktprompt, historikk og tidligere arbeidsflyt

2. Nye ressursfiler under `arkitektur/ressurser/`
   - format: `<slug>-vX-<forfatter>.md`
  - brukt for `70-FINT-Felleskomponent-v1-codex.md`, `71-FINT-Arkiv-v1-codex.md`, `72-FINT-Informasjonsmodell-v1-codex.md` og `73-VIGO-v1-codex.md`

### Vurdering

Det ville vært ryddigst å ha én samlet navnekonvensjon på sikt, men det er **ikke** klokt å innføre det samtidig med første store filflytting.

Hvis vi både:
- flytter 22 filer
- endrer registerlenker
- oppdaterer webgrunnlaget
- og samtidig bytter filnavn

så øker vi risikoen unødvendig for:
- brutte lenker
- feil i mapping og generatorer
- unødvendig vanskelig diff og feilsøking

### Anbefalt beslutning før Digdir-flytting

For **første Digdir-løp** bør vi holde fast ved denne arbeidsregelen:

- Migrerte Digdir-filer **beholder eksisterende filnavn uendret**
- Nye ressursfiler som opprettes direkte i `arkitektur/ressurser/` **beholder dagens enklere slug-baserte navngivning**
- Navneharmonisering behandles som **eget senere oppryddingsløp**, ikke som del av første migrering

### Praktisk konsekvens

Det betyr at vi aksepterer en midlertidig, bevisst asymmetri:

- migrerte legacy-produkter kan ligge i ressursstruktur med `produkt-canvas` i filnavnet
- nye ressurser kan ligge i samme struktur uten `produkt-canvas` i filnavnet

Dette er faglig litt ujevnt, men operasjonelt tryggere enn å rydde alt i samme steg.

### Foreslått senere harmonisering

Når første migrering er gjennomført og stabilisert, bør vi ta en separat beslutning om langsiktig navnekonvensjon. Da bør vi velge mellom to hovedspor:

1. Videreføre dagens etablerte produktnavnlogikk også i ressursområdet
   - fordel: tett kobling til historikk og eksisterende prompt
   - ulempe: `produkt-canvas` blir for smalt for normerende ressurser og samarbeidsfora

2. Gå over til en bredere ressurslogikk for nye filer og eventuelt senere omdøping av gamle
   - eksempel: `<slug>-vX-<forfatter>.md`
   - fordel: passer bedre med ny ressursmodell
   - ulempe: krever et eget omdøpings- og oppdateringsløp for eldre filer hvis alt skal harmoniseres

### Anbefaling

Min anbefaling er å **ikke** røre filnavnene i første Digdir-flytting.

Det riktige nå er:
- flytte plassering
- beholde navn
- oppdatere pekere
- verifisere web

Deretter kan vi ta en roligere og mer bevisst navneopprydding når vi vet at ny struktur faktisk fungerer stabilt.

## Kandidater i første Digdir-løp

Følgende siste versjoner er kandidater for flytting:

| Løpenr | Ressurs-ID | Navn | Nåværende fil | Foreslått mål |
|---:|---|---|---|---|
| 1 | `DIGDIR-001` | ID-porten | `arkitektur/produkter/produktbeskrivelser/01-ID-porten-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/01-ID-porten-produkt-canvas-v3-codex.md` |
| 2 | `DIGDIR-002` | Maskinporten | `arkitektur/produkter/produktbeskrivelser/02-Maskinporten-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/02-Maskinporten-produkt-canvas-v3-codex.md` |
| 3 | `DIGDIR-003` | eSignering | `arkitektur/produkter/produktbeskrivelser/03-eSignering-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/03-eSignering-produkt-canvas-v3-codex.md` |
| 4 | `DIGDIR-004` | Altinn Autorisasjon | `arkitektur/produkter/produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v4-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/04-Altinn-autorisasjon-produkt-canvas-v4-codex.md` |
| 5 | `DIGDIR-005` | Kontakt- og reservasjonsregisteret | `arkitektur/produkter/produktbeskrivelser/05-Kontakt-og-reservasjonsregisteret-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/05-Kontakt-og-reservasjonsregisteret-produkt-canvas-v3-codex.md` |
| 6 | `DIGDIR-006` | eInnsyn | `arkitektur/produkter/produktbeskrivelser/06-eInnsyn-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/06-eInnsyn-produkt-canvas-v3-codex.md` |
| 7 | `DIGDIR-007` | eFormidling | `arkitektur/produkter/produktbeskrivelser/07-eFormidling-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/07-eFormidling-produkt-canvas-v3-codex.md` |
| 8 | `DIGDIR-008` | Altinn Formidling | `arkitektur/produkter/produktbeskrivelser/08-Altinn-formidling-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/08-Altinn-formidling-produkt-canvas-v3-codex.md` |
| 9 | `DIGDIR-009` | Digital postkasse | `arkitektur/produkter/produktbeskrivelser/09-Digital-postkasse-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/09-Digital-postkasse-produkt-canvas-v3-codex.md` |
| 10 | `DIGDIR-023` | ELMA | `arkitektur/produkter/produktbeskrivelser/10-ELMA-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/10-ELMA-produkt-canvas-v3-codex.md` |
| 12 | `DIGDIR-010` | Altinn Events | `arkitektur/produkter/produktbeskrivelser/12-Altinn-events-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/12-Altinn-events-produkt-canvas-v3-codex.md` |
| 13 | `DIGDIR-011` | Felles datakatalog | `arkitektur/produkter/produktbeskrivelser/13-Felles-datakatalog-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/13-Felles-datakatalog-produkt-canvas-v3-codex.md` |
| 14 | `DIGDIR-012` | Begrepskatalog | `arkitektur/produkter/produktbeskrivelser/14-Begrepskatalog-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/14-Begrepskatalog-produkt-canvas-v3-codex.md` |
| 15 | `DIGDIR-013` | API-katalog | `arkitektur/produkter/produktbeskrivelser/15-API-katalog-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/15-API-katalog-produkt-canvas-v3-codex.md` |
| 16 | `DIGDIR-014` | data.norge.no | `arkitektur/produkter/produktbeskrivelser/16-data-norge-no-produkt-canvas-v4-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/16-data-norge-no-produkt-canvas-v4-codex.md` |
| 17 | `DIGDIR-015` | data.altinn.no | `arkitektur/produkter/produktbeskrivelser/17-data-altinn-no-produkt-canvas-v4-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/17-data-altinn-no-produkt-canvas-v4-codex.md` |
| 18 | `DIGDIR-016` | Norge.no | `arkitektur/produkter/produktbeskrivelser/18-Norge-no-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/18-Norge-no-produkt-canvas-v3-codex.md` |
| 19 | `DIGDIR-017` | Altinn 3 plattform | `arkitektur/produkter/produktbeskrivelser/19-Altinn-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/19-Altinn-produkt-canvas-v3-codex.md` |
| 20 | `DIGDIR-018` | Altinn Studio | `arkitektur/produkter/produktbeskrivelser/20-Altinn-Studio-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/20-Altinn-Studio-produkt-canvas-v3-codex.md` |
| 22 | `DIGDIR-020` | Dialogporten | `arkitektur/produkter/produktbeskrivelser/22-Dialogporten-produkt-canvas-v5-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/22-Dialogporten-produkt-canvas-v5-codex.md` |
| 23 | `DIGDIR-021` | Altinn Melding | `arkitektur/produkter/produktbeskrivelser/23-Altinn-3-Melding-produkt-canvas-v5-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/23-Altinn-3-Melding-produkt-canvas-v5-codex.md` |
| 24 | `DIGDIR-022` | Altinn Varsling | `arkitektur/produkter/produktbeskrivelser/24-Varslinger-produkt-canvas-v5-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/24-Varslinger-produkt-canvas-v5-codex.md` |

Totalt: **22 filer**

Ikke med i dette løpet:
- `DIGDIR-024 eIDAS-node (Norge)` fordi ressursbeskrivelse ikke finnes ennå

## Tekniske forberedelser som allerede er på plass

Følgende overgangsstøtte er nå etablert:
- `generate-products.ps1` bygger ressursoversikten fra `produktnummerering.md`
- `generate-capabilities.py` tåler ny ressursstruktur
- `validate-text-encoding.py` validerer også `arkitektur/ressurser/`
- Novari-ressursene er lagt inn i kapabilitetsmappingen

Det betyr at Digdir-flytting nå primært handler om:
- filflytting
- oppdatering av dokumentlenker i registeret
- eventuell kontroll av relative pekere i innhold

## Foreslått gjennomføringsrekkefølge for selve flyttingen

1. Flytt de 22 siste Digdir-filene til `arkitektur/ressurser/operative-losninger-og-tjenester/`.
2. Oppdater dokumentlenkene for de 22 radene i `produktnummerering.md`.
3. Oppdater eventuelle eksplisitte referanser i README-er og styringsfiler som fortsatt peker til gammel filplassering.
4. Regenerer:
   - `web/hugo-prototype/scripts/generate-products.ps1`
   - `web/hugo-prototype/scripts/generate-capabilities.py`
5. Kjør tegnkodingskontroll.
6. Kjør Hugo-build når verktøyet er tilgjengelig.

## Risikoer i selve flytteløpet

- Enkelte manuelle lenker i repoet kan fortsatt peke til gammel Digdir-plassering.
- Filnavnene bruker fortsatt `produkt-canvas`, noe som er semantisk smalere enn ny struktur.
- Eldre versjoner blir liggende i gammel mappe, så det må være tydelig at bare siste versjon er migrert.

## Anbefaling

Når vi er klare til faktisk flytting, bør Digdir-løpet gjennomføres som **én samlet endring**, ikke stykkevis. Da blir det lettere å:
- holde register og web synkronisert
- se reelle avvik med én gang
- unngå at repoet havner i en halvmigrert mellomtilstand

## Status etter gjennomføring 2026-04-09

Første Digdir-løp er nå gjennomført som pilot.

Gjennomført:
- 22 siste Digdir-filer er flyttet fra `arkitektur/produkter/produktbeskrivelser/` til `arkitektur/ressurser/operative-losninger-og-tjenester/`
- dokumentlenker i `arkitektur/produkter/produktnummerering.md` er oppdatert
- relative stier og GitHub-lenker i `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` er oppdatert
- webgrunnlaget er regenerert
- tegnkodingskontroll er kjørt uten feil

Ikke verifisert lokalt:
- full Hugo-build, fordi `hugo` ikke er installert i dette miljøet
