# Setup: Automatisk Push til GitHub

## Hva er dette?

To måter å automatisere push til GitHub:

1. **GitHub Actions (`.github/workflows/auto-push-produktbeskrivelser.yml`)** – Cloud-basert, trigges når du pusher filer
2. **Post-commit hook (`.git/hooks/post-commit`)** – Lokalt, automatisk push etter hver commit

---

## Alternativ 1: GitHub Actions (enklest – ingen setup nødvendig!)

**Status:** ✅ Allerede installert

De GitHub Actions workflow vil:
- Trigges når filer endres i `results/Produktbeskrivelser/`
- Automatisk committe og pushe videre
- Kreves: GitHub Personal Access Token (hvis private repo)

**Aktivering:**
1. Gå til GitHub → Settings → Developer settings → Personal access tokens
2. Lag en token med `repo` og `workflow` tillatelser
3. Gå til repo → Settings → Secrets → New repository secret
4. Legg inn som `GITHUB_TOKEN` eller bare bruk default GitHub token (gjøres automatisk for actions)

**Hvordan det fungerer:**
```
Lokal commit → Push til GitHub → GitHub Actions trigges → Auto-commit+push
```

---

## Alternativ 2: Post-commit Hook (enklest for lokal bruk)

**Status:** ⚠️ Krever setup

**Hvordan det fungerer:**
```
git commit → Post-commit hook trigges automatisk → Auto-pull → Auto-push
```

### Installering på Windows (PowerShell)

```powershell
# Gå til repo-directory
cd c:\Users\HILROS\NA-kunnskap

# Den `.git\hooks\post-commit.bat` fil er allerede opprettet.
# Git vil automatisk bruke den når den finnes.

# Test at hook fungerer:
git commit --allow-empty -m "test: test post-commit hook"
# Dette skulle automatisk pushe
```

### Installering på Mac/Linux (Bash)

```bash
# Gå til repo-directory
cd ~/NA-kunnskap

# Gjør bash-versjonen kjørbar:
chmod +x .git/hooks/post-commit

# Test at hook fungerer:
git commit --allow-empty -m "test: test post-commit hook"
```

---

## Slik deaktiverer du automatisk push

**Hvis du vil ha kontroll tilbake (kommitter uten å pushe automatisk):**

### Windows:
```powershell
# Flytt eller fjern post-commit.bat
Move-Item .git\hooks\post-commit.bat .git\hooks\post-commit.bat.bak
# eller: Remove-Item .git\hooks\post-commit.bat
```

### Mac/Linux:
```bash
# Flytt eller fjern post-commit
mv .git/hooks/post-commit .git/hooks/post-commit.bak
# eller: rm .git/hooks/post-commit
```

### GitHub Actions:
```
Gå til .github/workflows/auto-push-produktbeskrivelser.yml
Slett filen eller disable workflow i GitHub
```

---

## Anbefaling

**Bruk post-commit hook (Alternativ 2)** fordi:
- ✅ Enklest å sette opp
- ✅ Ingen credentials nødvendig
- ✅ Fungerer offline (vel, ikke push-delen)
- ✅ Gir deg immediate feedback lokalt

**GitHub Actions kan brukes som backup** for:
- Automatisk synkronisering av `results/` til `docs/`
- Running lint/validation på filer
- GitHub Pages deployment

---

## Troubleshooting

**Problem:** Hook kjøres ikke etter commit
- **Løsning:** Sjekk at filen er kjørbar (`chmod +x .git/hooks/post-commit` på Mac/Linux)
- **Løsning Mac/Linux:** Git hooks må være `.sh` eller ingen extension; ikke `.bat`

**Problem:** Post-commit hook feiler silencully
- **Løsning:** Legg til `set -x` i toppen av bash-versjonen for debug-output

**Problem:** Infinite loop (push trigges endringer som trigges push)
- **Løsning:** Hook sjekker at vi er på `main` branch – bør være trygt

**Problem:** Du vil ha kontroll over når du pusher
- **Løsning:** Deaktiver hook (se avsnittet over), commit manuelt, og push når du vil

---

## Neste steg

1. **Test post-commit hook:**
   ```powershell
   git commit --allow-empty -m "test: test auto-push"
   ```

2. **Eller:** Lag en normal commit og se om den automatisk pushes

3. **Eller:** Deaktiver hvis du foretrekker manuell kontroll

Lykke til!
