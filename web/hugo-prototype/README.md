# Hugo prototype

Dette er en isolert prototype for en framtidig nettside om nasjonal arkitektur.

## Foreløpig struktur

- Forside
- Kapabiliteter
- Prinsipper
- Ressursoversikt

## Kilder i repoet

- `arkitektur/kapabiliteter/capabilities.yaml`
- `results/Produktbeskrivelser/`
- `arkitektur/prinsipper/principles.md` brukes ikke foreløpig fordi den ikke er ferdig utfylt

## Generering av innhold

Produkter og kapabiliteter genereres fra repoets kildefiler:

```bash
python scripts/generate-capabilities.py
powershell -ExecutionPolicy Bypass -File scripts/generate-products.ps1
```

Kapabilitetsscriptet bygger:
- hovedkapabiliteter
- delkapabiliteter
- mapping fra kapabiliteter til siste versjon av relevante produktbeskrivelser

Produktscriptet bygger:
- samlet oversikt over siste versjon per produkt

## Lokal kjøring

```bash
hugo server
```

## Bygg

```bash
hugo --gc --minify
```

## Publisering

- GitHub Actions bygger prototypen direkte fra `web/hugo-prototype/`.
- GitHub Pages deployer bygget som artifact.
- `docs/prototype/` brukes ikke lenger som publiseringsmål for denne prototypen.
