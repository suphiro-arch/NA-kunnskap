# Hugo prototype

Dette er en isolert prototype for en framtidig nettside om nasjonal arkitektur.

## Foreløpig struktur

- Forside
- Kapabiliteter
- Prinsipper
- Ressursoversikt

## Kilder i repoet

- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/ressurser/produktnummerering.md` er registermaster for ressurs-ID, status og dokumentlenker
- `arkitektur/ressurser/` brukes for ressursbeskrivelser etter rammeverkskategoriene
- `arkitektur/ressurser/operative-losninger-og-tjenester/` er teknisk mappe for gjenbrukbare løsninger
- `arkitektur/ressurser/normerende-ressurser/` er teknisk mappe for standarder og veiledning
- `arkitektur/ressurser/samarbeidsfora/` er teknisk mappe for samhandlingsarenaer og organisering
- `arkitektur/ressurser/rammer-og-virkemidler/` er teknisk mappe for økonomiske og juridiske rammer og virkemidler
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

Ressursscriptet bygger:
- en inngangsside for ressursoversikten
- egne undersider for ressursene gruppert etter rammeverkskategori
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
python scripts/validate-built-prototype.py
```

## Publisering

- GitHub Actions bygger prototypen direkte fra `web/hugo-prototype/`.
- GitHub Pages deployer bygget som artifact.

