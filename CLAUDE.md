# Claude-instruks for NA-kunnskap

## Les AGENTS.md først

[AGENTS.md](AGENTS.md) er den autoritative regelfila for alt assistentarbeid i dette repoet. Les den
før du gjør endringer. Denne fila erstatter den ikke — den legger bare til det som gjelder spesifikt
for Claude og for kjøringer på denne maskinen.

Ved motstrid: `AGENTS.md` går foran.

## Suffix: du er `claude`

Filnavn skal reflektere hvilket verktøy som opprettet fila. Når du oppretter en ressursfil, er
suffixet `-claude`.

Merk at porteføljen i dag bare inneholder `-codex` og `-copilot`. Du blir den første som bruker
`-claude`, og det er riktig — regelen i `AGENTS.md` er at suffixet følger **utførende verktøy i den
aktuelle kjøringen**, ikke suffixet på forrige versjon. Ikke arv `-codex` fordi det ser konsistent
ut.

Filnavnmønsteret håndheves mekanisk av `tools/check-resource-version-sync.py`:

```
NNN-Navn-med-bindestrek-vN-claude.md
```

Sjekk alltid eksisterende filnavn i samme kategori før du oppretter noe. Er du i tvil om suffix,
stopp og spør.

## Miljø: Windows og PowerShell

Primærskallet er PowerShell, ikke bash. Det slår ut på flere av verktøyene repoet bruker:

```powershell
# encoding-kontroll (kjør alltid før commit)
pwsh tools/check-mojibake.ps1

# register og kapabilitetsmapping
python tools/sync-resource-metadata.py --apply
python tools/check-resource-version-sync.py

# strukturkontroll av ressursbeskrivelser mot malen
python tools/check-resource-structure.py --strict

# syntakskontroll av innebygd JavaScript i Hugo-maler (krever node)
python tools/check-inline-js.py --strict

# encoding-validering før Hugo-build
python web/hugo-prototype/scripts/validate-text-encoding.py
```

`&&` og `||` finnes ikke i Windows PowerShell 5.1. Bruk `;` eller `if ($?) { ... }`. Bash-verktøyet
er også tilgjengelig hvis en POSIX-kommando er enklere — men da gjelder bash-syntaks fullt ut.

## Encoding er ikke valgfritt

Repoet har tre lag med mojibake-vern: lokale git-hooks (`core.hooksPath` = `.githooks`),
`.github/workflows/encoding-guard.yml` i CI, og validering før Hugo-build. Alle tre stopper arbeidet
ditt hvis du skriver ødelagte tegn.

Etter at du har opprettet eller endret markdown: kjør `tools/check-mojibake.ps1` eksplisitt. Ikke
nøy deg med at teksten ser riktig ut i terminalen — Windows-konsollen skjuler nettopp den feilen
kontrollen leter etter.

Filer skal lagres som ren UTF-8. Bruk `æ`, `ø` og `å` i dokumentinnhold; ASCII bare i filnavn,
slugger og kode.

## Git

- Ikke commit eller push uten at det er bedt om det.
- Git-identiteten skal være `suphiro-arch` med noreply-adresse. Ikke bruk jobbmail i
  commit-metadata.
- Oppretter du en fil som register, kapabilitetsmapping eller publiseringsgrunnlag peker til, skal
  fila legges til i Git i samme endringssett. Det skal aldri stå igjen en peker til en `untracked`
  fil.

## Fallgruver i dette repoet

- **`briefs/next-step.md` står i `.gitignore`, men er sporet fra før.** Dette er bevisst og
  dokumentert i `AGENTS.md`. Fila skal oppdateres som normalt — ikke konkluder ut fra `.gitignore`
  at den er utenfor repoet, og ikke prøv å «rette» oppføringen.
- **`print/` og `tmp-overordnet-malbilde/` er gitignorert og lokale.** Ikke forsøk å committe
  innhold der.
- **`web/hugo-prototype/content/` er generert.** Endre kildene i `arkitektur/` og regenerer; ikke
  håndrediger genererte oversikter.
- **`arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` vedlikeholdes manuelt** og er
  autoritativ. Ingen generator retter den for deg.
- **`capabilities.yaml` har CRLF i arbeidskopien.** Git normaliserer til LF. Ikke tolk
  linjeskiftvarsler som en reell endring.

## Arbeidsmåte

- Skriv på norsk i alt dokumentinnhold, også i forklaringer og arbeidsnotater.
- Ved revisjon: behold velfungerende formuleringer fra forrige versjon. Målet er forbedring, ikke
  full omskriving.
- Skill tydelig mellom fakta, deduksjon og usikkerhet. Kan en påstand ikke bekreftes i tilgjengelige
  kilder, si det i teksten.
- Bruk `sources/links.md` som førstevalg for eksterne kilder, og oppdater fila når du tar i bruk nye
  stabile lenker med gjenbruksverdi.
- Logg varige metode- og strukturvalg i `briefs/decisions.md`, ikke i nye beslutningsdokumenter.
