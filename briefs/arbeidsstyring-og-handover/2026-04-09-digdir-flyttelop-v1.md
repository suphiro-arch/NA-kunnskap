---
date: 2026-04-09
author: codex
status: gjennomfort
topic: fÃ¸rste sektorvise flyttelÃ¸p for Digdir
sources:
  - arkitektur/ressurser/produktnummerering.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/
  - web/hugo-prototype/scripts/generate-products.ps1
  - web/hugo-prototype/scripts/generate-capabilities.py
---

# FÃ¸rste sektorvise flyttelÃ¸p: Digdir

Dette notatet konkretiserer fÃ¸rste flyttelÃ¸p fra gammel produktstruktur til ny ressursstruktur.

MÃ¥let er Ã¥ flytte fÃ¸rste stÃ¸rre, sammenhengende operative bolk uten Ã¥ bryte:
- registerfÃ¸ring i `arkitektur/ressurser/produktnummerering.md`
- webgenerering i `web/hugo-prototype/`
- tegnkodingskontroll
- sporbarhet mellom gammel og ny struktur

## Valgt fÃ¸rste bolk

FÃ¸rste flyttelÃ¸p bÃ¸r vÃ¦re **Digdir-bolken**.

Begrunnelse:
- Digdir har mange eksisterende beskrivelser pÃ¥ relativt likt modenhetsnivÃ¥.
- PortefÃ¸ljen dekker flere ressurskategorier innen samme operative hovedtype.
- Webgrunnlaget er allerede sterkt eksponert mot Digdir-ressursene.
- Vi fÃ¥r testet overgang for felleskomponenter, plattformer, registre, portaler og felleslÃ¸sninger i samme lÃ¸p.

## Arbeidsregler for flyttelÃ¸pet

### Hva som flyttes

- Bare **siste registrerte versjon** av hver ressurs flyttes i fÃ¸rste lÃ¸p.
- MÃ¥lkatalog for denne bolken er `arkitektur/ressurser/operative-losninger-og-tjenester/`.
- Registermasteren forblir `arkitektur/ressurser/produktnummerering.md`.

### Hva som ikke flyttes i fÃ¸rste lÃ¸p

- Eldre versjoner blir stÃ¥ende i `arkitektur/ressurser/operative-losninger-og-tjenester/` som historisk arkiv.
- Ressurser som ikke har beskrivelse ennÃ¥, flyttes ikke.
- `Altinn Portal` inngÃ¥r ikke i dette lÃ¸pet fordi den ikke stÃ¥r i operativt register som aktiv Digdir-ressurs.
- `Peppol eDelivery` inngÃ¥r ikke i dette lÃ¸pet fordi den er registrert under `OPP`, ikke `DIGDIR`.

### Prinsipp for filnavn

Eksisterende filnavn beholdes i fÃ¸rste migrering, selv om de fortsatt inneholder `produkt-canvas`.

Begrunnelse:
- minst mulig risiko i fÃ¸rste lÃ¸p
- enklere oppdatering av register- og webpekere
- reduserer behov for samtidige navne- og strukturendringer

Et senere lÃ¸p kan rydde i navnekonvensjon hvis vi Ã¸nsker Ã¥ gÃ¥ fra `produkt-canvas` til en bredere ressursnavngivning.

## Sanity check: navnekonvensjon fÃ¸r flytting

Det finnes nÃ¥ to navnekonvensjoner i repoet:

1. Eldre og etablerte produktfiler under `arkitektur/ressurser/operative-losninger-og-tjenester/`
   - format: `NN-<navn>-produkt-canvas-vX-<forfatter>.md`
   - sterkt koblet til eksisterende produktprompt, historikk og tidligere arbeidsflyt

2. Nye ressursfiler under `arkitektur/ressurser/`
   - format: `<slug>-vX-<forfatter>.md`
  - brukt for `70-FINT-Felleskomponent-v1-codex.md`, `71-FINT-Arkiv-v1-codex.md`, `72-FINT-Informasjonsmodell-v1-codex.md` og `73-VIGO-v1-codex.md`

### Vurdering

Det ville vÃ¦rt ryddigst Ã¥ ha Ã©n samlet navnekonvensjon pÃ¥ sikt, men det er **ikke** klokt Ã¥ innfÃ¸re det samtidig med fÃ¸rste store filflytting.

Hvis vi bÃ¥de:
- flytter 22 filer
- endrer registerlenker
- oppdaterer webgrunnlaget
- og samtidig bytter filnavn

sÃ¥ Ã¸ker vi risikoen unÃ¸dvendig for:
- brutte lenker
- feil i mapping og generatorer
- unÃ¸dvendig vanskelig diff og feilsÃ¸king

### Anbefalt beslutning fÃ¸r Digdir-flytting

For **fÃ¸rste Digdir-lÃ¸p** bÃ¸r vi holde fast ved denne arbeidsregelen:

- Migrerte Digdir-filer **beholder eksisterende filnavn uendret**
- Nye ressursfiler som opprettes direkte i `arkitektur/ressurser/` **beholder dagens enklere slug-baserte navngivning**
- Navneharmonisering behandles som **eget senere oppryddingslÃ¸p**, ikke som del av fÃ¸rste migrering

### Praktisk konsekvens

Det betyr at vi aksepterer en midlertidig, bevisst asymmetri:

- migrerte legacy-produkter kan ligge i ressursstruktur med `produkt-canvas` i filnavnet
- nye ressurser kan ligge i samme struktur uten `produkt-canvas` i filnavnet

Dette er faglig litt ujevnt, men operasjonelt tryggere enn Ã¥ rydde alt i samme steg.

### ForeslÃ¥tt senere harmonisering

NÃ¥r fÃ¸rste migrering er gjennomfÃ¸rt og stabilisert, bÃ¸r vi ta en separat beslutning om langsiktig navnekonvensjon. Da bÃ¸r vi velge mellom to hovedspor:

1. ViderefÃ¸re dagens etablerte produktnavnlogikk ogsÃ¥ i ressursomrÃ¥det
   - fordel: tett kobling til historikk og eksisterende prompt
   - ulempe: `produkt-canvas` blir for smalt for normerende ressurser og samarbeidsfora

2. GÃ¥ over til en bredere ressurslogikk for nye filer og eventuelt senere omdÃ¸ping av gamle
   - eksempel: `<slug>-vX-<forfatter>.md`
   - fordel: passer bedre med ny ressursmodell
   - ulempe: krever et eget omdÃ¸pings- og oppdateringslÃ¸p for eldre filer hvis alt skal harmoniseres

### Anbefaling

Min anbefaling er Ã¥ **ikke** rÃ¸re filnavnene i fÃ¸rste Digdir-flytting.

Det riktige nÃ¥ er:
- flytte plassering
- beholde navn
- oppdatere pekere
- verifisere web

Deretter kan vi ta en roligere og mer bevisst navneopprydding nÃ¥r vi vet at ny struktur faktisk fungerer stabilt.

## Kandidater i fÃ¸rste Digdir-lÃ¸p

FÃ¸lgende siste versjoner er kandidater for flytting:

| LÃ¸penr | Ressurs-ID | Navn | NÃ¥vÃ¦rende fil | ForeslÃ¥tt mÃ¥l |
|---:|---|---|---|---|
| 1 | `DIGDIR-001` | ID-porten | `arkitektur/ressurser/operative-losninger-og-tjenester/01-ID-porten-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/01-ID-porten-produkt-canvas-v3-codex.md` |
| 2 | `DIGDIR-002` | Maskinporten | `arkitektur/ressurser/operative-losninger-og-tjenester/02-Maskinporten-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/02-Maskinporten-produkt-canvas-v3-codex.md` |
| 3 | `DIGDIR-003` | eSignering | `arkitektur/ressurser/operative-losninger-og-tjenester/03-eSignering-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/03-eSignering-produkt-canvas-v3-codex.md` |
| 4 | `DIGDIR-004` | Altinn Autorisasjon | `arkitektur/ressurser/operative-losninger-og-tjenester/04-Altinn-autorisasjon-produkt-canvas-v4-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/04-Altinn-autorisasjon-produkt-canvas-v4-codex.md` |
| 5 | `DIGDIR-005` | Kontakt- og reservasjonsregisteret | `arkitektur/ressurser/operative-losninger-og-tjenester/05-Kontakt-og-reservasjonsregisteret-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/05-Kontakt-og-reservasjonsregisteret-produkt-canvas-v3-codex.md` |
| 6 | `DIGDIR-006` | eInnsyn | `arkitektur/ressurser/operative-losninger-og-tjenester/06-eInnsyn-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/06-eInnsyn-produkt-canvas-v3-codex.md` |
| 7 | `DIGDIR-007` | eFormidling | `arkitektur/ressurser/operative-losninger-og-tjenester/07-eFormidling-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/07-eFormidling-produkt-canvas-v3-codex.md` |
| 8 | `DIGDIR-008` | Altinn Formidling | `arkitektur/ressurser/operative-losninger-og-tjenester/08-Altinn-formidling-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/08-Altinn-formidling-produkt-canvas-v3-codex.md` |
| 9 | `DIGDIR-009` | Digital postkasse | `arkitektur/ressurser/operative-losninger-og-tjenester/09-Digital-postkasse-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/09-Digital-postkasse-produkt-canvas-v3-codex.md` |
| 10 | `DIGDIR-023` | ELMA | `arkitektur/ressurser/operative-losninger-og-tjenester/10-ELMA-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/10-ELMA-produkt-canvas-v3-codex.md` |
| 12 | `DIGDIR-010` | Altinn Events | `arkitektur/ressurser/operative-losninger-og-tjenester/12-Altinn-events-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/12-Altinn-events-produkt-canvas-v3-codex.md` |
| 13 | `DIGDIR-011` | Felles datakatalog | `arkitektur/ressurser/operative-losninger-og-tjenester/13-Felles-datakatalog-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/13-Felles-datakatalog-produkt-canvas-v3-codex.md` |
| 14 | `DIGDIR-012` | Begrepskatalog | `arkitektur/ressurser/operative-losninger-og-tjenester/14-Begrepskatalog-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/14-Begrepskatalog-produkt-canvas-v3-codex.md` |
| 15 | `DIGDIR-013` | API-katalog | `arkitektur/ressurser/operative-losninger-og-tjenester/15-API-katalog-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/15-API-katalog-produkt-canvas-v3-codex.md` |
| 16 | `DIGDIR-014` | data.norge.no | `arkitektur/ressurser/operative-losninger-og-tjenester/16-data-norge-no-produkt-canvas-v4-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/16-data-norge-no-produkt-canvas-v4-codex.md` |
| 17 | `DIGDIR-015` | data.altinn.no | `arkitektur/ressurser/operative-losninger-og-tjenester/17-data-altinn-no-produkt-canvas-v4-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/17-data-altinn-no-produkt-canvas-v4-codex.md` |
| 18 | `DIGDIR-016` | Norge.no | `arkitektur/ressurser/operative-losninger-og-tjenester/18-Norge-no-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/18-Norge-no-produkt-canvas-v3-codex.md` |
| 19 | `DIGDIR-017` | Altinn 3 plattform | `arkitektur/ressurser/operative-losninger-og-tjenester/19-Altinn-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/19-Altinn-produkt-canvas-v3-codex.md` |
| 20 | `DIGDIR-018` | Altinn Studio | `arkitektur/ressurser/operative-losninger-og-tjenester/20-Altinn-Studio-produkt-canvas-v3-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/20-Altinn-Studio-produkt-canvas-v3-codex.md` |
| 22 | `DIGDIR-020` | Dialogporten | `arkitektur/ressurser/operative-losninger-og-tjenester/22-Dialogporten-produkt-canvas-v5-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/22-Dialogporten-produkt-canvas-v5-codex.md` |
| 23 | `DIGDIR-021` | Altinn Melding | `arkitektur/ressurser/operative-losninger-og-tjenester/23-Altinn-3-Melding-produkt-canvas-v5-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/23-Altinn-3-Melding-produkt-canvas-v5-codex.md` |
| 24 | `DIGDIR-022` | Altinn Varsling | `arkitektur/ressurser/operative-losninger-og-tjenester/24-Varslinger-produkt-canvas-v5-codex.md` | `arkitektur/ressurser/operative-losninger-og-tjenester/24-Varslinger-produkt-canvas-v5-codex.md` |

Totalt: **22 filer**

Ikke med i dette lÃ¸pet:
- `DIGDIR-024 eIDAS-node (Norge)` fordi ressursbeskrivelse ikke finnes ennÃ¥

## Tekniske forberedelser som allerede er pÃ¥ plass

FÃ¸lgende overgangsstÃ¸tte er nÃ¥ etablert:
- `generate-products.ps1` bygger ressursoversikten fra `produktnummerering.md`
- `generate-capabilities.py` tÃ¥ler ny ressursstruktur
- `validate-text-encoding.py` validerer ogsÃ¥ `arkitektur/ressurser/`
- Novari-ressursene er lagt inn i kapabilitetsmappingen

Det betyr at Digdir-flytting nÃ¥ primÃ¦rt handler om:
- filflytting
- oppdatering av dokumentlenker i registeret
- eventuell kontroll av relative pekere i innhold

## ForeslÃ¥tt gjennomfÃ¸ringsrekkefÃ¸lge for selve flyttingen

1. Flytt de 22 siste Digdir-filene til `arkitektur/ressurser/operative-losninger-og-tjenester/`.
2. Oppdater dokumentlenkene for de 22 radene i `produktnummerering.md`.
3. Oppdater eventuelle eksplisitte referanser i README-er og styringsfiler som fortsatt peker til gammel filplassering.
4. Regenerer:
   - `web/hugo-prototype/scripts/generate-products.ps1`
   - `web/hugo-prototype/scripts/generate-capabilities.py`
5. KjÃ¸r tegnkodingskontroll.
6. KjÃ¸r Hugo-build nÃ¥r verktÃ¸yet er tilgjengelig.

## Risikoer i selve flyttelÃ¸pet

- Enkelte manuelle lenker i repoet kan fortsatt peke til gammel Digdir-plassering.
- Filnavnene bruker fortsatt `produkt-canvas`, noe som er semantisk smalere enn ny struktur.
- Eldre versjoner blir liggende i gammel mappe, sÃ¥ det mÃ¥ vÃ¦re tydelig at bare siste versjon er migrert.

## Anbefaling

NÃ¥r vi er klare til faktisk flytting, bÃ¸r Digdir-lÃ¸pet gjennomfÃ¸res som **Ã©n samlet endring**, ikke stykkevis. Da blir det lettere Ã¥:
- holde register og web synkronisert
- se reelle avvik med Ã©n gang
- unngÃ¥ at repoet havner i en halvmigrert mellomtilstand

## Status etter gjennomfÃ¸ring 2026-04-09

FÃ¸rste Digdir-lÃ¸p er nÃ¥ gjennomfÃ¸rt som pilot.

GjennomfÃ¸rt:
- 22 siste Digdir-filer er flyttet fra `arkitektur/ressurser/operative-losninger-og-tjenester/` til `arkitektur/ressurser/operative-losninger-og-tjenester/`
- dokumentlenker i `arkitektur/ressurser/produktnummerering.md` er oppdatert
- relative stier og GitHub-lenker i `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` er oppdatert
- webgrunnlaget er regenerert
- tegnkodingskontroll er kjÃ¸rt uten feil

Ikke verifisert lokalt:
- full Hugo-build, fordi `hugo` ikke er installert i dette miljÃ¸et

