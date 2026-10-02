# Omdøping av ressursmappene til rammeverkskategoriene

Status: plan, ikke startet. Gjennomføres når ingen andre økter arbeider i repoet.

## Bakgrunn

Mappene under `arkitektur/ressurser/` har fortsatt navnene fra ressursstrukturen i april 2026. Feltet
`Ressurskategori`, `Type`-kolonnen i `produktnummerering.md` og visningsnavnene på nettsiden bruker
allerede rammeverkskategoriene. Det er altså bare de tekniske sluggene som avviker.

[Overgangsplanen fra mai](2026-05-27-overgang-til-rammeverkskategorier-v1.md) utsatte mappe- og
URL-endringer til fase 4, fordi URL-stabilitet ble vurdert som viktigere enn navnesamsvar mens
begrepene ble innarbeidet. Begrepene er nå stabile, og denne planen er fase 4.

## Nye slugger

| Gammel mappe | Rammeverkskategori | Ny mappe |
|---|---|---|
| `operative-losninger-og-tjenester` | Gjenbrukbare løsninger | `gjenbrukbare-losninger` |
| `normerende-ressurser` | Standarder og veiledning | `standarder-og-veiledning` |
| `samarbeidsfora` | Samhandlingsarenaer og organisering | `samhandlingsarenaer-og-organisering` |
| `rammer-og-virkemidler` | Økonomiske og juridiske rammer og virkemidler | `okonomiske-og-juridiske-rammer-og-virkemidler` |

Den fjerde kategorien får fullt navn. Overgangsplanen foreslo den korte formen fordi den «tåler senere
justering i visningstekst», men det er ikke logget som beslutning i `briefs/decisions.md`, og de tre
andre sluggene følger kategorinavnet. Fullt navn samsvarer dessuten med de eksisterende filnavnene for
prompt og mal, `okonomiske-og-juridiske-rammer-og-virkemidler-canvas.system.md` og
`okonomiske-og-juridiske-rammer-og-virkemidler-template.md`.

## Avklart

- Det er akseptert at eksterne lenker direkte til ressursfiler på GitHub
  (`github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/...`) slutter å virke. GitHub
  videresender ikke stier etter omdøping, og det finnes ikke noe tiltak for det.
- Gamle URL-er på nettsiden skal videresendes med Hugo-`aliases`.
- Historiske arbeidsdokumenter i `briefs/arbeidsstyring-og-handover/` og `Analyser/` skrives ikke om.
  De beskriver strukturen slik den var, og stiene i dem blir stående som historikk.

## Forutsetninger før start

1. Ingen andre økter er aktive, verken Claude, Copilot eller manuelt arbeid.
2. `git status` er tom. Alt arbeid fra andre økter er committet eller forkastet av eieren, ikke av
   denne økta.
3. Lokal `main` er lik `origin/main`.
4. Alle kontroller går grønt på utgangspunktet, slik at feil etter flyttingen kan tilskrives
   flyttingen:
   ```powershell
   python tools/check-resource-version-sync.py
   python tools/check-capability-explanations.py --strict
   python tools/check-resource-structure.py --strict
   python tools/check-inline-js.py --strict
   powershell -NoProfile -ExecutionPolicy Bypass -File tools/check-mojibake.ps1
   ```
   Noter antall filer hver kontroll rapporterer. Etter flyttingen skal tallene være de samme.

## Steg 1: Samle kategoridefinisjonen ett sted

Kan gjøres og committes for seg, før selve flyttingen, og endrer ingen stier.

I dag har sju filer hver sin hardkodede liste over mappene:

- `tools/check-resource-version-sync.py`
- `tools/sync-resource-metadata.py`
- `tools/check-source-links.py`
- `tools/check-resource-structure.py` (malkravene er nøklet på mappenavnet)
- `tools/check-capability-explanations.py`
- `web/hugo-prototype/scripts/generate-products.ps1` (mappenavnet er også URL-slugg)
- `web/hugo-prototype/scripts/generate-capabilities.py` (`classify_resource` klassifiserer på sti)

Opprett `config/ressurskategorier.yaml` med én oppføring per kategori: `slug`, `visningsnavn`
(rammeverkskategorien ordrett), `mal`, `prompt` og `tidligere_slugger`. La verktøyene lese fra fila.
`generate-products.ps1` leser den med samme enkle linjeparser som resten av PowerShell-skriptet, ikke
med en ny avhengighet.

Gevinst: Selve omdøpingen blir én endring i én fil i stedet for sju, og `tidligere_slugger` gir både
aliasene og kontrollen i steg 3 fra samme kilde.

Kontroll: Alle kontroller rapporterer samme antall filer som før, og regenerert `web/hugo-prototype/content/`
er identisk med det som er committet.

## Steg 2: Flytt og skriv om stier, i én commit

Alt i dette steget må med i samme commit. Pre-commit-hooken kjører kontrollene, og en delvis flytting
får dem enten til å stoppe eller til å finne null filer og gå stille gjennom.

1. Flytt med `git mv`, én mappe om gangen:
   ```powershell
   git mv arkitektur/ressurser/operative-losninger-og-tjenester arkitektur/ressurser/gjenbrukbare-losninger
   git mv arkitektur/ressurser/normerende-ressurser arkitektur/ressurser/standarder-og-veiledning
   git mv arkitektur/ressurser/samarbeidsfora arkitektur/ressurser/samhandlingsarenaer-og-organisering
   git mv arkitektur/ressurser/rammer-og-virkemidler arkitektur/ressurser/okonomiske-og-juridiske-rammer-og-virkemidler
   ```
2. Oppdater `config/ressurskategorier.yaml` med nye slugger og legg de gamle i `tidligere_slugger`.
3. Skriv om stier med et engangsskript i scratchpad, ikke med fritt søk-og-erstatt. Skriptet skal bare
   erstatte forankrede stier:
   - `arkitektur/ressurser/<gammel>/` til `arkitektur/ressurser/<ny>/`
   - `ressursoversikt/ressurser/<gammel>/` til `ressursoversikt/ressurser/<ny>/`
   - relative lenker mellom ressursfiler, `../<gammel>/` til `../<ny>/`

   Tre feller skriptet må tåle:
   - `samarbeidsfora` er et vanlig norsk ord og står som brødtekst i mange ressursfiler («støtte fra
     samarbeidsfora»). Det står også i en ekstern URL,
     `samarbeid.digdir.no/digital-lommebok/samarbeidsfora-digital-lommebok/2902`. Ingen av dem skal
     endres.
   - `rammer-og-virkemidler` er en del av den nye sluggen og av filnavnene for prompt og mal. En
     erstatning uten `ressurser/`-forankring er ikke idempotent og gir
     `okonomiske-og-juridiske-okonomiske-og-juridiske-...` ved andre kjøring.
   - Filer med BOM eller CRLF skal beholde det. Les og skriv med `newline=''` og samme koding.

   Filer som skal skrives om:
   - `arkitektur/ressurser/produktnummerering.md` (160 stier)
   - `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` (`relative_path` og `product_url`,
     160 av hver)
   - gjeldende og eldre ressursfiler med lenker til hverandre (rundt 120 forekomster)
   - `config/prompts/` (fem filer) og `config/templates/arkitekturassistert-analyse-av-utviklingsbehov-template.md`
   - `AGENTS.md`, `README.md`, `arkitektur/README.md`, `arkitektur/ressurser/README.md`,
     `arkitektur/ressurser/styringsregler.md` og `arkitektur/struktur-og-bearbeiding.md`
   - `sources/links.md` og andre filer i `sources/` som peker til ressursfiler
   - `.github/workflows/publish-hugo-prototype.yml`: fjern linja
     `arkitektur/ressurser/operative-losninger-og-tjenester/**`. Den er allerede dekket av
     `arkitektur/**`.
   - `briefs/decisions.md` og `briefs/next-step.md`: bare lenker som brukes aktivt, ikke historiske
     beskrivelser i beslutningsraden.
4. Legg inn `aliases` i `generate-products.ps1` for kategorisidene og hver ressursside, fra
   `ressursoversikt/ressurser/<gammel>/...` til ny URL. Hent gamle slugger fra `tidligere_slugger`.
   Sjekk om `generate-capabilities.py` lager sider under stier som også endres; i dag gjør den ikke det.
5. Regenerer nettsiden og slett de gamle mappene under
   `web/hugo-prototype/content/ressursoversikt/ressurser/`. Generatoren rydder ikke gamle mapper selv,
   og blir de stående, publiseres de med feil antall. Dette skjedde med `produkter/`-treet, se
   beslutningen 2026-08-31 i `briefs/decisions.md`.
6. Logg beslutningen i `briefs/decisions.md`: nye slugger, at fjerde kategori fikk fullt navn, at
   GitHub-lenker brytes og at historiske dokumenter ikke skrives om.
7. Oppdater `briefs/next-step.md`.

## Steg 3: Hindre at de gamle stiene kommer tilbake

Utvid `tools/check-resource-version-sync.py`, eller lag en egen kontroll, som stopper hvis en sporet fil
utenfor de historiske mappene inneholder `arkitektur/ressurser/<tidligere slugg>/`. Gamle stier i
prompter og maler er den mest sannsynlige veien tilbake: en assistent som leser en utdatert instruks,
oppretter fila i en mappe som ikke finnes lenger.

## Kontroll før commit

- `git diff --cached -M --stat` viser alle ressursfilene som `R`, ikke som slett og ny. Per 2026-10-02 var
  det 308 sporede filer i de fire mappene, og tallet må telles på nytt ved start. Git
  oppdager omdøping så lenge innholdsendringene er små, og det er det som gjør at `git log --follow`
  virker per fil.
- Ingen av de gamle sluggene finnes i forankrede stier i sporede filer utenom historiske dokumenter:
  ```powershell
  git grep -n -E "ressurser/(operative-losninger-og-tjenester|normerende-ressurser|samarbeidsfora|rammer-og-virkemidler)/" -- . ":!briefs/arbeidsstyring-og-handover" ":!Analyser"
  ```
- Alle kontrollene fra forutsetningene gir samme antall filer som før, og `python tools/sync-resource-metadata.py --apply` gir ingen endringer.
- Hugo-build lokalt, og stikkprøve på at en gammel URL videresender til ny.
- `python tools/check-source-links.py`. `check-link-liveness.py` sjekker bare eksterne lenker i
  `sources/links.md` og fanger ikke opp interne stier, så den er ikke nok alene.
- `powershell -NoProfile -ExecutionPolicy Bypass -File tools/check-mojibake.ps1`. `pwsh` er ikke
  installert på maskinen, og pre-commit-hooken faller tilbake til `powershell`.
- Commit med eksplisitt filliste. Med over 300 omdøpte filer er det enklest å bygge lista fra
  `git diff --cached --name-only` etter at `git status` er lest og bekreftet uten fremmede filer.

## Etter publisering

- Sjekk på GitHub Pages at de fire kategorisidene og et utvalg ressurssider svarer på ny URL, og at
  gamle URL-er videresender.
- Gi beskjed til de som kjenner til nettsiden om at lenker direkte til filer på GitHub har endret seg.

## Risiko

| Risiko | Tiltak |
|---|---|
| Eksterne lenker til nettsiden brytes | Hugo-`aliases` fra gamle URL-er |
| Eksterne lenker til filer på GitHub brytes | Ingen. Akseptert |
| Gamle genererte sider blir stående publisert | Slett gamle mapper under `web/hugo-prototype/content/` i samme commit |
| Søk-og-erstatt treffer brødtekst, ekstern URL eller prompt- og malfilnavn | Erstatt bare forankrede stier, og kjør skriptet to ganger for å bekrefte at det er idempotent |
| Kontroller finner null filer og går stille gjennom | Sammenlign antall filer før og etter |
| Konflikt med parallelle økter | Start bare med tomt arbeidstre og ingen aktive økter |
| Gamle stier lever videre i prompter | Kontrollen i steg 3 |
| Historikken per fil går tapt | `git mv`, små innholdsendringer, kontroll av `R` i diff |
