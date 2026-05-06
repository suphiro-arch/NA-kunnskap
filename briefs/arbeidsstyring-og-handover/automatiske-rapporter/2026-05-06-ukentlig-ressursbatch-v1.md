---
date: 2026-05-06
author: codex
status: final
topic: ukentlig-ressursbatch
sources:
  - arkitektur/ressurser/produktnummerering.md
  - arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml
  - web/hugo-prototype/content/
  - https://bits.no/project/dsop/
  - https://dokumentasjon.dsop.no/
  - https://www.bits.no/document/5620-2/
  - https://www.digdir.no/digdir/far-nasjonal-arena-kunstig-intelligens/6885
  - https://www.digdir.no/kunstig-intelligens/digdir-etablerer-ki-norge/7412
  - https://www.digdir.no/kunstig-intelligens/ki-norge-innspillsmote/7975
  - https://www.digdir.no/digitaliseringsradet/digdir-nasjonal-arkitektur-samhandling-og-tjenesteutvikling-i-offentlig-sektor/8079
---

# Ukentlig ressursbatch 2026-05-06

## Vurderte ressurser

- `DIGDIR-040` Kunnskapsgrunnlag - dataspaces
- `DIGDIR-041` Kapabilitetskart (planlagt)
- `DIGDIR-055` DSOP-samarbeidet
- `DIGDIR-057` KI Norge

## Faktisk oppdatert i denne batchen

- `DIGDIR-055` DSOP-samarbeidet
  - Ny fil: [123-DSOP-samarbeidet-v1-codex.md](/arkitektur/ressurser/samarbeidsfora/123-DSOP-samarbeidet-v1-codex.md)
  - Løftet fra `v0` til `v1` med tydelig styringsmodell, beslutningsnivå, innmeldingsløp, porteføljelogikk og skille mellom forumet og de operative DSOP-tjenestene.

- `DIGDIR-057` KI Norge
  - Ny fil: [125-KI-Norge-v1-codex.md](/arkitektur/ressurser/samarbeidsfora/125-KI-Norge-v1-codex.md)
  - Løftet fra `v0` til `v1` med oppdatert etableringsstatus, tydeligere mandat, samspill med Nkom og Datatilsynet, innspillsløp og bedre avgrensning mot andre fora.

## Ikke oppdatert nå

- `DIGDIR-041` ble vurdert på nytt mot nyere Digdir-omtale av nasjonal arkitektur, men ble ikke oppdatert fordi det fortsatt ikke finnes en egen publisert ressursbeskrivelse eller tydelig offentlig artefakt utover omtale av en planlagt kapabilitetsoversikt.
- `DIGDIR-040` ble vurdert, men står fortsatt på for svakt og for indirekte åpent kildegrunnlag. Ressursen framstår mer som et temaspor enn som en tydelig avgrenset normerende ressurs med egen publisert forvaltningsflate.

## Endrede filer

- [123-DSOP-samarbeidet-v1-codex.md](/arkitektur/ressurser/samarbeidsfora/123-DSOP-samarbeidet-v1-codex.md)
- [125-KI-Norge-v1-codex.md](/arkitektur/ressurser/samarbeidsfora/125-KI-Norge-v1-codex.md)
- [produktnummerering.md](/arkitektur/ressurser/produktnummerering.md)
- [produkt-kapabilitet-koblinger.yaml](/arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml)
- [next-step.md](/briefs/next-step.md)
- [2026-05-06-ukentlig-ressursbatch-v1.md](/briefs/arbeidsstyring-og-handover/automatiske-rapporter/2026-05-06-ukentlig-ressursbatch-v1.md)
- [ressursoversikt/_index.md](/web/hugo-prototype/content/ressursoversikt/_index.md)
- [ressursoversikt/produkter/samarbeidsfora/_index.md](/web/hugo-prototype/content/ressursoversikt/produkter/samarbeidsfora/_index.md)
- [kapabiliteter/datautveksling-og-integrasjon/_index.md](/web/hugo-prototype/content/kapabiliteter/datautveksling-og-integrasjon/_index.md)
- [kapabiliteter/datautveksling-og-integrasjon/dele-data-med-andre/_index.md](/web/hugo-prototype/content/kapabiliteter/datautveksling-og-integrasjon/dele-data-med-andre/_index.md)
- [kapabiliteter/samarbeid/_index.md](/web/hugo-prototype/content/kapabiliteter/samarbeid/_index.md)
- [kapabiliteter/samarbeid/samarbeidsarenaer-og-nettverk/_index.md](/web/hugo-prototype/content/kapabiliteter/samarbeid/samarbeidsarenaer-og-nettverk/_index.md)
- [kapabiliteter/strategisk-styring/_index.md](/web/hugo-prototype/content/kapabiliteter/strategisk-styring/_index.md)
- [kapabiliteter/strategisk-styring/samordning/_index.md](/web/hugo-prototype/content/kapabiliteter/strategisk-styring/samordning/_index.md)

## Kjørte kontroller

- `python tools/check-resource-version-sync.py`
- `python web/hugo-prototype/scripts/validate-text-encoding.py`
- `python web/hugo-prototype/scripts/generate-capabilities.py`
- `powershell -ExecutionPolicy Bypass -File web/hugo-prototype/scripts/generate-products.ps1`

Alle kontroller gikk grønt i denne kjøringen.

## Bør tas i neste batch

- Prioriter `DIGDIR-041` hvis Digdir publiserer en tydeligere egen beskrivelse av kapabilitetsoversikten eller det nasjonale arkitektursporet.
- Hold `DIGDIR-040` tilbake til det finnes et mer konkret og sporbart ressursgrunnlag enn dagens generelle dataspaces-kilder.
- Ta deretter stilling til om `KS-011`, `KS-013` eller `KS-014` fortsatt er riktige neste sektorkandidater, eller om Digdir-sporet bør ryddes ferdig først.



