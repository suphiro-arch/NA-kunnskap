---
date: 2026-05-03
author: copilot
status: aktiv
topic: neste-steg
---

# Neste steg

## Nytt siste steg

- Opprettet [103-Nasjonalt-veikart-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/103-Nasjonalt-veikart-v1-codex.md), [105-Rammeverk-nasjonale-grunndata-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/105-Rammeverk-nasjonale-grunndata-v1-codex.md) og [106-Nasjonal-verktoykasse-for-deling-av-data-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/106-Nasjonal-verktoykasse-for-deling-av-data-v1-codex.md) som oppgraderinger fra v0 til v1.
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) slik at `DIGDIR-035`, `DIGDIR-037` og `DIGDIR-038` peker til v1-filer.
- Synkronisert [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) med oppdatert versjon/sti for produkt-id `103`, `105` og `106`.

- Opprettet [114-Klart-sprak-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/114-Klart-sprak-v1-codex.md), [115-Digitaliseringsvennlig-regelverk-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/115-Digitaliseringsvennlig-regelverk-v1-codex.md) og [116-Rammeverk-for-innovasjon-i-offentlig-sektor-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/116-Rammeverk-for-innovasjon-i-offentlig-sektor-v1-codex.md) som oppgraderinger fra v0 til v1.
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) slik at `DIGDIR-046`, `DIGDIR-047` og `DIGDIR-048` peker til v1-filer.
- Synkronisert [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) med oppdatert versjon/sti for produkt-id `114`, `115` og `116`.

- Lagt inn [vurdering av flere ressurstyper fra Digdirs virkemiddeloversikt](../briefs/arbeidsstyring-og-handover/2026-05-03-vurdering-av-flere-ressurstyper-fra-digdir-virkemiddeloversikt-v1.md) som anbefaler å beholde dagens tre hovedtyper, men vurdere noen nye normerende ressurser og samarbeidsfora.
- Avklart pulje 5 for EU-sporet: `EU-001` til `EU-011` beholdes i registeret som referanseressurser uten egne produktfiler i denne runden.
- Oppdatert [decisions.md](../briefs/decisions.md) med varig beslutning om EU-avgrensning og prioritering.

- Opprettet [96-KS-Bekymringsmelding-produkt-canvas-v1-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/96-KS-Bekymringsmelding-produkt-canvas-v1-codex.md) som ny operativ ressursbeskrivelse for `KS-015`.
- Opprettet [80-VIGO-portalen-v1-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/80-VIGO-portalen-v1-codex.md) som ny operativ ressursbeskrivelse for `NOVARI-005`.
- Opprettet [81-VIGO-Sentralbase-v1-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/81-VIGO-Sentralbase-v1-codex.md) som ny operativ ressursbeskrivelse for `NOVARI-006`.
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) med dokumentlenker for `KS-015`, `NOVARI-005` og `NOVARI-006`.
- Synkronisert [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) med `sync-resource-metadata.py`, inkludert nye oppføringer for produkt-id `96`, `80` og `81`.

- Opprettet [93-Fiks-Digisos-produkt-canvas-v1-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/93-Fiks-Digisos-produkt-canvas-v1-codex.md) som ny operativ ressursbeskrivelse for `KS-012`.
- Opprettet [97-MinKommune-produkt-canvas-v1-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/97-MinKommune-produkt-canvas-v1-codex.md) som ny operativ ressursbeskrivelse for `KS-016`.
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) med dokumentlenker for `KS-012` og `KS-016`.
- Oppdatert [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) med koblinger for `FHI-005`, `FHI-006`, `KS-012` og `KS-016`.

- Opprettet [135-Norsk-pasientregister-produkt-canvas-v1-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/135-Norsk-pasientregister-produkt-canvas-v1-codex.md) som ny operativ ressurs under `FHI-005`.
- Opprettet [136-Kommunalt-pasient-og-brukerregister-produkt-canvas-v1-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/136-Kommunalt-pasient-og-brukerregister-produkt-canvas-v1-codex.md) som ny operativ ressurs under `FHI-006`.
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) slik at `FHI-005` og `FHI-006` er registerført.

- Ryddet bort gammel auto-push-dokumentasjon og ubrukt GitHub-workflow for automatisk push.
- Lagt til [check-resource-version-sync.py](../tools/check-resource-version-sync.py) som stopper commit, push og GitHub-publisering hvis `produktnummerering.md` eller `produkt-kapabilitet-koblinger.yaml` peker til eldre ressursversjoner.
- Lagt til [sync-resource-metadata.py](../tools/sync-resource-metadata.py) og brukt den til å fylle inn manglende oppføringer i `produkt-kapabilitet-koblinger.yaml` og synkronisere metadata mot siste ressursversjoner.
- Strammet inn [generate-products.ps1](../web/hugo-prototype/scripts/generate-products.ps1) slik at webgeneratoren bruker den versjonen registeret faktisk peker til, i stedet for å hoppe til nyere filer automatisk.
- Oppdatert styrende dokumentasjon i [AGENTS.md](../AGENTS.md), [README.md](../README.md), [arkitektur/ressurser/README.md](../arkitektur/ressurser/README.md) og [operative-ressurs-canvas.system.md](../config/prompts/operative-ressurs-canvas.system.md) slik at register og mapping alltid skal oppdateres til siste versjon.

- Opprettet [134-Sentralt-stedsnavnregister-produkt-canvas-v1-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/134-Sentralt-stedsnavnregister-produkt-canvas-v1-codex.md) som ny operativ ressurs under `KART-004`.
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) slik at `KART-004` er registerført.

- Opprettet [85-Rammeverk-for-digital-samhandling-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/85-Rammeverk-for-digital-samhandling-v1-codex.md) som normerende ressurs for `DIGDIR-025`.
- Opprettet [86-Referansekatalogen-for-IT-standarder-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/86-Referansekatalogen-for-IT-standarder-v1-codex.md) som normerende ressurs for `DIGDIR-026`.
- Opprettet [89-Rammeverk-for-informasjonsforvaltning-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/89-Rammeverk-for-informasjonsforvaltning-v1-codex.md) som normerende ressurs for `DIGDIR-029`.
- Opprettet [87-Arkitektur-for-hendelser-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/87-Arkitektur-for-hendelser-v1-codex.md) som normerende ressurs for `DIGDIR-027`.
- Opprettet [98-Overordnede-arkitekturprinsipper-for-offentlig-sektor-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/98-Overordnede-arkitekturprinsipper-for-offentlig-sektor-v1-codex.md), [99-Sjekkliste-for-sammenhengende-tjenester-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/99-Sjekkliste-for-sammenhengende-tjenester-v1-codex.md) og [100-Kart-for-tjenestekjeder-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/100-Kart-for-tjenestekjeder-v1-codex.md) som oppgraderinger fra v0 til v1.
- Opprettet [101-Referansearkitektur-forsendelse-eMelding-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/101-Referansearkitektur-forsendelse-eMelding-v1-codex.md), [102-Referansearkitektur-foresporsel-svar-eOppslag-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/102-Referansearkitektur-foresporsel-svar-eOppslag-v1-codex.md) og [104-Orden-i-eget-hus-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/104-Orden-i-eget-hus-v1-codex.md) som oppgraderinger fra v0 til v1.
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) med dokumentlenker for `DIGDIR-025`, `DIGDIR-026`, `DIGDIR-027` og `DIGDIR-029`.

- Opprettet [132-Grunnboken-produkt-canvas-v1-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/132-Grunnboken-produkt-canvas-v1-codex.md) som ny operativ ressurs under `KART-003`.
- Opprettet [133-Register-over-reelle-rettighetshavere-produkt-canvas-v1-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/133-Register-over-reelle-rettighetshavere-produkt-canvas-v1-codex.md) som ny operativ ressurs under `BRREG-004`.
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) slik at begge ressursene nå er registerført.

## Foreslått neste prioritering

**Tredje pulje – gjennomfort (2026-05-03):**
- `MinKommune` (`KS-016`) ✓
- `Fiks Digisos` (`KS-012`) ✓
- Koblinger i `produkt-kapabilitet-koblinger.yaml` oppdatert for `KS-012`, `KS-016`, `FHI-005` og `FHI-006` ✓

**Fjerde pulje – gjennomfort (2026-05-03):**
- `KS-015` Bekymringsmelding ✓
- `NOVARI-005` VIGO-portalen ✓
- `NOVARI-006` VIGO Sentralbase ✓
- Register og kapabilitetskoblinger oppdatert for alle tre ✓

**Femte pulje – gjennomfort (2026-05-03):**
- EU-avklaring fullfort: `EU-001` til `EU-011` holdes som referanseressurser i registeret ✓
- Beslutning forankret i `briefs/decisions.md` ✓

**Sjette pulje – gjennomfort (2026-05-03):**
- Oppgradert `DIGDIR-046`, `DIGDIR-047` og `DIGDIR-048` fra v0 til v1 ✓
- Register og kapabilitetskoblinger oppdatert for alle tre ✓

**Sjuende pulje – gjennomfort (2026-05-03):**
- Oppgradert `DIGDIR-035`, `DIGDIR-037` og `DIGDIR-038` fra v0 til v1 ✓
- Register og kapabilitetskoblinger oppdatert for alle tre ✓

**Neste steg – foreslatte kandidater (pulje 8):**
- Vurdere `KS-011`, `KS-013` og `KS-014` pa nytt med samme kriterier for tversgaende NA-verdi som i pulje 3 og 4.
- Ta en rask statuskontroll av `NOVARI-007`, `NOVARI-008` og `NOVARI-009` for om en av dem bor prioriteres foran KS-kandidatene i neste bolk.

**Utsatt – lav NA-prioritet akkurat nå:**
- `Kreftregisteret` – primærverdi er klinisk forskning; holdes utenfor uten tydeligere casebehov.
- `KS-011`, `KS-013`, `KS-014` – sektorinterne eller innføringsveiledere uten tydelig tversgående verdi.

---

## Hva gjenstår – Produktgrunnlag

**Kjerneprioriteter:**

- Fortsette revisjon av eldre produktbeskrivelser sektorvis etter samme metode som for KS- og Altinn-rundene.
- Følge opp kvaliteten i koblingene mellom produkter og kapabiliteter, særlig i eldre produktbeskrivelser der kapabilitetsseksjonen er svakere.
- Vurdere om de normerende Digdir-ressursene som fortsatt er på `v0` bør få utfylt analysefeltene (`Forpliktelsesnivå og etterlevelse`, `Typiske analyse- og beslutningssituasjoner`, `Konsekvens ved manglende bruk`) før neste større bolk legges inn.
- Vurdere om FHI-sektoren skal utvides med flere kandidater, f.eks. Norsk pasientregister (NPR) eller Kreftregisteret.

**Produktregisteret – konkrete valg som trengs:**

- Avklare om `FIKS IO` skal inn som egen ressurs, eller fortsatt behandles som teknisk komponent under `FIKS Melding`.
- Stramme inn `Fiks register`-beskrivelsen som overordnet registerfamilie nå som undertjenestene er ført som egne ressurskandidater.
- Vurdere om `DIGDIR-048 Rammeverk for innovasjon i offentlig sektor` skal stå som normerende ressurs, eller avgrenses tydeligere.

---

## Strategiske forbedringer – Arbeidsflyt og kvalitetssikring

### Evalueringsrubrikk i analysemalen
Neste forbedring som bør vurderes: legge inn en enkel evalueringsrubrikk i malen med score 1–5 for sporbarhet, gjenbrukbarhet, styringsrelevans og presisjon i produktvurdering.

### Modulær struktur for produktbeskrivelser
Nåværende produktbeskrivelser blander kilder, KI-analyse og publiserbar tekst i ett lag. Dette gjør det uklart hva som er verifisert kilde, hva som er arbeidsgrunnlag, og hva som skal publiseres.

**Forslag – tre-lags modell:**
1. **Kildegrunnlag og arkitekturnotater** – strukturerte kilder og masterdata fra `arkitektur/`
2. **Analyseblokker** – KI-utledet innhold som koblingsvurderinger og gjenbruksmuligheter
3. **Publiserbar tekst** – validert tekst for nett og arkitekturveiledning

**Praktisk gjennomføring:**
- Lag en annotasjonsstandard i produkt-canvas-prompten: `[Analyse]`, `[Kilde]`, `[Utledet fra X]`.
- Legg inn tydelig merking: «KI-støttet arbeidsgrunnlag – ikke faglig godkjent» inntil kvalitetssikring etableres.

---

## Bekjente blokkere og risiko

- Eldre produktbeskrivelser kan gi ujevn retrieval-kvalitet (må oppgraderes gradvis).
- Produktbeskrivelsene mangler tydelig merking av arbeidsgrunnlag vs. godkjent innhold (fikses med modulær struktur).
- Lokal Hugo-build er ikke verifisert fordi `hugo` ikke er installert i dette miljøet.

---

## Strukturelle forbedringer – Dagens repo

Kan gjøres parallelt, men er ikke kritisk for produktgrunnlag-arbeidet:

- Vurdere om `produktnummerering.md` bør omdøpes til `produktregister.md` når strukturen ellers er stabil.
- Vurdere om `sources/links.md` på sikt bør flyttes nærmere produktområdet.
- Vurdere om delressurser under `VIGO` bør beskrives som egne operative ressurser.
- Vurdere om neste sektorbolk etter Digdir og KS er EU-kandidater, nye nasjonale produkter eller ny revisjon av eldre beskrivelser.

---

## Assistenten på web – Planlegging og MVP (framtidig)

**Status:** Kun aktuelt hvis beslutning tas om å investere. Se [MVP-skisse](arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md) for detaljer.

**Blokkere:**
- Repoet har ingen eksplisitt lisens for dokumentasjonsinnholdet.
- Åpen internettflate krever moderering, rate limiting og tydelig avgrensning av datagrunnlag.
- Produktbeskrivelsene må ha høy og konsistent kvalitet før de brukes i retrieval.

**Neste steg hvis prosjekt startes:**
- Avklar lisens for dokumentasjonsinnholdet.
- Velg backend-plattform (foreslått: Azure Functions).
- Lag første backend-skjelett for `/api/ask` og første indeksjobb for repo-dokumentasjonen.
- Legg inn enkel chat-widget i Hugo-prototypen.
