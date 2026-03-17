# Setup: automatisk push til GitHub

## Hva er dette?

Repoet bruker to former for automatisering:

1. `GitHub Actions` for publisering av Hugo-prototypen og andre repo-oppgaver
2. `post-commit`-hook lokalt for automatisk pull og push etter commit på `main`

Dette dokumentet beskriver den lokale hooken og hvordan den virker sammen med GitHub Actions.

---

## Alternativ 1: GitHub Actions

**Status:** i bruk

Workflowene i `.github/workflows/` håndterer blant annet:

- publisering av Hugo-prototypen til GitHub Pages
- automatisering knyttet til produktbeskrivelser

GitHub Actions brukes ikke lenger til å speile filer til `docs/`.

---

## Alternativ 2: Post-commit-hook

**Status:** krever lokal hook, men er allerede satt opp i dette repoet

**Hvordan det fungerer:**

```text
git commit -> post-commit-hook kjører -> git pull --rebase -> git push
```

Hooken kjører bare automatisk når du står på `main`.

### Installering på Windows (PowerShell)

```powershell
cd c:\Users\HILROS\NA-kunnskap

# `.git\hooks\post-commit.bat` er allerede opprettet.
# Git bruker den automatisk når den finnes.

git commit --allow-empty -m "test: test post-commit hook"
```

### Installering på Mac/Linux (Bash)

```bash
cd ~/NA-kunnskap

chmod +x .git/hooks/post-commit

git commit --allow-empty -m "test: test post-commit hook"
```

---

## Slik deaktiverer du automatisk push

### Windows

```powershell
Move-Item .git\hooks\post-commit.bat .git\hooks\post-commit.bat.bak
```

eller:

```powershell
Remove-Item .git\hooks\post-commit.bat
```

### Mac/Linux

```bash
mv .git/hooks/post-commit .git/hooks/post-commit.bak
```

eller:

```bash
rm .git/hooks/post-commit
```

### GitHub Actions

Hvis du vil stoppe en workflow, deaktiver den i GitHub eller fjern workflowfila under `.github/workflows/`.

---

## Anbefaling

Bruk `post-commit`-hooken lokalt hvis du vil ha enkel flyt med automatisk push etter commit.

Fordeler:

- lite manuelt arbeid
- rask tilbakemelding
- fungerer godt sammen med repoets arbeidsflyt på `main`

GitHub Actions bør brukes for:

- publisering av Hugo-prototypen
- validering og annen server-side automasjon

---

## GitHub Pages

Dette repoet publiserer nå Hugo-prototypen via:

- `.github/workflows/publish-hugo-prototype.yml`
- `GitHub Pages`
- `Source = GitHub Actions`

GitHub Pages skal ikke lenger peke til `/docs`.

---

## Troubleshooting

**Problem:** Hooken kjører ikke etter commit

- Sjekk at riktig hookfil finnes i `.git/hooks/`
- På Mac/Linux: sørg for at hooken er kjørbar med `chmod +x`

**Problem:** Rebase stopper på konflikt

- Kjør `git status`
- Løs konfliktene
- Kjør `git add <fil>`
- Fortsett med `git rebase --continue`

**Problem:** Du vil ha kontroll over når du pusher

- Deaktiver hooken og kjør `git push` manuelt

---

## Neste steg

1. Test hooken med en tom commit hvis du vil verifisere lokal flyt.
2. Verifiser at GitHub Pages bruker `GitHub Actions` som source.
3. Fjern `docs/prototype/` når ny publiseringsmodell er bekreftet.
