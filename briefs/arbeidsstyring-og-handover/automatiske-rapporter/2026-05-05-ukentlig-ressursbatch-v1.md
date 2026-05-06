---
date: 2026-05-05
author: codex
status: final
topic: ukentlig-ressursbatch
sources:
  - arkitektur/ressurser/produktnummerering.md
  - arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml
  - web/hugo-prototype/content/
  - https://www.digdir.no/digitalisering-og-samordning/kompetansemodell-digital-transformasjon/3293
  - https://www.digdir.no/informasjonssikkerhet/nettverk-informasjonssikkerhet-nifs/2186
  - https://www.digdir.no/informasjonssikkerhet/felles-sikkerhet-i-forvaltningen/5957
---

# Ukentlig ressursbatch 2026-05-05

## Vurderte ressurser

- `DIGDIR-039` Kunnskapsgrunnlag og KPI-er for datadeling
- `DIGDIR-040` Kunnskapsgrunnlag dataspaces
- `DIGDIR-041` Kapabilitetskart (planlagt)
- `DIGDIR-049` Kompetansemodell for digital transformasjon
- `DIGDIR-054` NIFS
- `DIGDIR-055` DSOP-samarbeidet
- `DIGDIR-056` Felles sikkerhet i forvaltningen
- `DIGDIR-057` KI Norge

## Faktisk oppdatert i denne batchen

- `DIGDIR-049` Kompetansemodell for digital transformasjon
  - Ny fil: [117-Kompetansemodell-for-digital-transformasjon-v1-codex.md](/arkitektur/ressurser/normerende-ressurser/117-Kompetansemodell-for-digital-transformasjon-v1-codex.md)
  - Løftet fra `v0` til `v1` med tydeligere tre-nivå-struktur, normerende rolle, brukssituasjoner og relasjon til øvrige Digdir-ressurser.

- `DIGDIR-054` NIFS
  - Ny fil: [122-NIFS-v1-codex.md](/arkitektur/ressurser/samarbeidsfora/122-NIFS-v1-codex.md)
  - Løftet fra `v0` til `v1` med bekreftet møtesyklus, medlemsmodell, kontaktpunkt, praktisk bruk i analysearbeid og tydeligere grensesnitt mot FSIF og lokale fora.

- `DIGDIR-056` Felles sikkerhet i forvaltningen
  - Ny fil: [124-Felles-sikkerhet-i-forvaltningen-v1-codex.md](/arkitektur/ressurser/samarbeidsfora/124-Felles-sikkerhet-i-forvaltningen-v1-codex.md)
  - Løftet fra `v0` til `v1` med tydeligere beskrivelse av programstatus, deltakende aktører, samordningsrolle, påvirkning på veiledningslandskapet og involveringspunkt.

## Ikke oppdatert nå

- `DIGDIR-039`, `DIGDIR-040` og `DIGDIR-041` ble vurdert, men har fortsatt svakere og mer indirekte åpent kildegrunnlag enn de tre som ble prioritert i denne kjøringen.
- `DIGDIR-055` og `DIGDIR-057` ble vurdert som gode kandidater til neste batch, men ble holdt utenfor for å holde denne kjøringen avgrenset til tre ressurser.

## Endrede filer

- [117-Kompetansemodell-for-digital-transformasjon-v1-codex.md](/arkitektur/ressurser/normerende-ressurser/117-Kompetansemodell-for-digital-transformasjon-v1-codex.md)
- [122-NIFS-v1-codex.md](/arkitektur/ressurser/samarbeidsfora/122-NIFS-v1-codex.md)
- [124-Felles-sikkerhet-i-forvaltningen-v1-codex.md](/arkitektur/ressurser/samarbeidsfora/124-Felles-sikkerhet-i-forvaltningen-v1-codex.md)
- [produktnummerering.md](/arkitektur/ressurser/produktnummerering.md)
- [produkt-kapabilitet-koblinger.yaml](/arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml)
- [web/hugo-prototype/content/ressursoversikt/_index.md](/web/hugo-prototype/content/ressursoversikt/_index.md)
- [web/hugo-prototype/content/ressursoversikt/produkter/normerende-ressurser/_index.md](/web/hugo-prototype/content/ressursoversikt/produkter/normerende-ressurser/_index.md)
- [web/hugo-prototype/content/ressursoversikt/produkter/samarbeidsfora/_index.md](/web/hugo-prototype/content/ressursoversikt/produkter/samarbeidsfora/_index.md)
- [web/hugo-prototype/content/kapabiliteter/strategisk-styring/_index.md](/web/hugo-prototype/content/kapabiliteter/strategisk-styring/_index.md)
- [web/hugo-prototype/content/kapabiliteter/strategisk-styring/samordning/_index.md](/web/hugo-prototype/content/kapabiliteter/strategisk-styring/samordning/_index.md)
- [web/hugo-prototype/content/kapabiliteter/tjenesteutvikling/_index.md](/web/hugo-prototype/content/kapabiliteter/tjenesteutvikling/_index.md)
- [web/hugo-prototype/content/kapabiliteter/tjenesteutvikling/tjenestedesign/_index.md](/web/hugo-prototype/content/kapabiliteter/tjenesteutvikling/tjenestedesign/_index.md)
- [web/hugo-prototype/content/kapabiliteter/informasjonssikkerhet/_index.md](/web/hugo-prototype/content/kapabiliteter/informasjonssikkerhet/_index.md)
- [web/hugo-prototype/content/kapabiliteter/informasjonssikkerhet/sikring-av-informasjonsflyt-og-datautveksling/_index.md](/web/hugo-prototype/content/kapabiliteter/informasjonssikkerhet/sikring-av-informasjonsflyt-og-datautveksling/_index.md)
- [web/hugo-prototype/content/kapabiliteter/samarbeid/_index.md](/web/hugo-prototype/content/kapabiliteter/samarbeid/_index.md)
- [web/hugo-prototype/content/kapabiliteter/samarbeid/samarbeidsarenaer-og-nettverk/_index.md](/web/hugo-prototype/content/kapabiliteter/samarbeid/samarbeidsarenaer-og-nettverk/_index.md)

## Kjørte kontroller

- `python tools/check-resource-version-sync.py`
- `python web/hugo-prototype/scripts/validate-text-encoding.py`
- `python web/hugo-prototype/scripts/generate-capabilities.py`
- `powershell -ExecutionPolicy Bypass -File web/hugo-prototype/scripts/generate-products.ps1`

Alle kontroller gikk grønt i denne kjøringen.

## Bør tas i neste batch

- Prioriter `DIGDIR-055` DSOP-samarbeidet hvis målet er flere samarbeidsfora med tydelig tverrsektoriell påvirkning og relativt godt åpent kildegrunnlag.
- Prioriter `DIGDIR-057` KI Norge hvis målet er å dekke nyere nasjonale samordningsarenaer med raskt voksende betydning.
- Vurder `DIGDIR-039` Kunnskapsgrunnlag og KPI-er for datadeling på nytt først når det finnes tydeligere og mer direkte åpent grunnlag enn dagens enkle arbeidsutkastlenke.



