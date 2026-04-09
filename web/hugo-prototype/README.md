# Hugo prototype

Dette er en isolert prototype for en framtidig nettside om nasjonal arkitektur.

## Foreløpig struktur

- Forside
- Kapabiliteter
- Prinsipper
- Ressursoversikt

## Kilder i repoet

- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/produkter/produktnummerering.md` er registermaster for ressurs-ID, status og dokumentlenker
- `arkitektur/produkter/produktbeskrivelser/` brukes fortsatt for eksisterende produktbeskrivelser
- `arkitektur/ressurser/` brukes for nye ressursbeskrivelser og ny struktur
- `arkitektur/prinsipper/principles.md`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`

## Generering av innhold

Produkter og kapabiliteter genereres fra repoets kildefiler:

```bash
python scripts/generate-capabilities.py
python scripts/sync-principles.py
powershell -ExecutionPolicy Bypass -File scripts/generate-products.ps1
```

Kapabilitetsscriptet bygger:
- hovedkapabiliteter
- delkapabiliteter
- mapping fra kapabiliteter til siste versjon av relevante produktbeskrivelser

Produktscriptet bygger:
- en inngangsside for ressursoversikten
- egne undersider for ressursene gruppert etter hovedtype
- oversikter basert på `produktnummerering.md`

Prinsippscriptet bygger:
- websidens prinsippinnhold direkte fra `arkitektur/prinsipper/principles.md`

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
