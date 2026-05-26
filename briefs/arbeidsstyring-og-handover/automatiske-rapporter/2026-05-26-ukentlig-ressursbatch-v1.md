---
date: 2026-05-26
author: codex
status: final
topic: ukentlig-ressursbatch
sources:
  - arkitektur/ressurser/produktnummerering.md
  - arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml
  - arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v3-codex.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/67-FIKS-Folkeregister-produkt-canvas-v2-codex.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v2-codex.md
  - https://ksdigital.no/tjenestene/fiks-register/
  - https://ksdigital.no/tjenestene/fiks-register/fiks-folkeregister/
  - https://ksdigital.no/tjenestene/fiks-register/fiks-skatte-og-inntektsopplysninger/
  - https://ksdigital.no/tjenestene/segmentsamarbeid/
  - https://ksdigital.no/avtaler-og-priser/fakturalinjer/
  - https://www.skatteetaten.no/nn/deling/folkeregisteret/intro/fa-tilgang/
  - https://www.skatteetaten.no/deling/bruksvilkar-for-delingstjenester/
---

# Ukentlig ressursbatch 2026-05-26

## Kort oppsummering

Denne batchen tok en liten, avgrenset KS/Fiks-pulje og løftet tre operative ressursbeskrivelser til nyere versjoner: `KS-004` Fiks register, `KS-008` Fiks folkeregister og `KS-009` Fiks skatte- og inntektsopplysninger.

Hovedgevinsten i denne runden var å oppdatere kildegrunnlaget, stramme inn avgrensningen mellom overordnet registerfamilie og undertjenester, og gjøre styrings- og tilgangsbildet tydeligere mot KS, KS Digital og Skatteetaten.

## Ressurser som ble vurdert

| Ressurs-ID | Ressurs | Vurdering |
|---|---|---|
| `KS-004` | Fiks register | Valgt. Trengte ny versjon for tydeligere avgrensning som overordnet registerfamilie og tilgangslag. |
| `KS-008` | Fiks folkeregister | Valgt. Trengte sterkere sporbarhet til dagens tilgangsløp, rollemodell og Altinn-/Maskinporten-avhengighet. |
| `KS-009` | Fiks skatte- og inntektsopplysninger | Valgt. Trengte sterkere sporbarhet til tjenesteområder, segmentansvar og Skatteetatens bruksvilkår. |

## Ressurser som faktisk ble oppdatert

| Ressurs-ID | Ny fil | Viktigste endring |
|---|---|---|
| `KS-004` | `arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v3-codex.md` | Presiserte at ressursen er en registerfamilie og et kommunalt tilgangslag, ikke et selvstendig register. |
| `KS-008` | `arkitektur/ressurser/operative-losninger-og-tjenester/67-FIKS-Folkeregister-produkt-canvas-v2-codex.md` | Tydeliggjorde weboppslag, innbyggerlister, systemintegrasjon, Altinn-delegering og lokal rolleforvaltning. |
| `KS-009` | `arkitektur/ressurser/operative-losninger-og-tjenester/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v2-codex.md` | Tydeliggjorde tjenesteområder, beregningsnært overbygg, segmentansvar og avhengighet til Skatteetatens endringsløp. |

## Filer som ble endret i denne batchen

- `arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v3-codex.md`
- `arkitektur/ressurser/operative-losninger-og-tjenester/67-FIKS-Folkeregister-produkt-canvas-v2-codex.md`
- `arkitektur/ressurser/operative-losninger-og-tjenester/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v2-codex.md`
- `arkitektur/ressurser/produktnummerering.md`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
- `web/hugo-prototype/content/ressursoversikt/_index.md`
- `web/hugo-prototype/content/ressursoversikt/produkter/_index.md`
- `web/hugo-prototype/content/ressursoversikt/produkter/andre-ressurser/_index.md`
- `web/hugo-prototype/content/ressursoversikt/produkter/normerende-ressurser/_index.md`
- `web/hugo-prototype/content/ressursoversikt/produkter/operative-losninger-og-tjenester/_index.md`
- `web/hugo-prototype/content/ressursoversikt/produkter/samarbeidsfora/_index.md`
- `web/hugo-prototype/content/kapabiliteter/datakilder/_index.md`
- `web/hugo-prototype/content/kapabiliteter/datakilder/grunndata/_index.md`
- `web/hugo-prototype/content/kapabiliteter/datautveksling-og-integrasjon/_index.md`
- `web/hugo-prototype/content/kapabiliteter/datautveksling-og-integrasjon/bruke-data-fra-andre/_index.md`

## Kilde- og kvalitetsnotater

- Alle tre oppdaterte ressursene ble kontrollert mot offisielle KS Digital-sider i denne arbeidsøkten 26. mai 2026.
- `KS-008` ble i tillegg kontrollert mot Skatteetatens side for tilgang til Folkeregisteret for å verifisere Altinn-delegering, Maskinporten og testløp.
- `KS-009` ble i tillegg kontrollert mot Skatteetatens bruksvilkår for delingstjenester for å verifisere segmentsporet og styringsforutsetningene.
- `python tools/sync-resource-metadata.py --apply` ble kjørt og oppdaterte metadata for `28`, `67` og `68` i kapabilitetsmappingen.
- `powershell -ExecutionPolicy Bypass -File web/hugo-prototype/scripts/generate-products.ps1` og `python web/hugo-prototype/scripts/generate-capabilities.py` ble kjørt etter innholdsoppdatering.
- `python tools/check-resource-version-sync.py`, `python web/hugo-prototype/scripts/validate-text-encoding.py` og `powershell -ExecutionPolicy Bypass -File tools/check-mojibake.ps1 -Root .` ble kjørt og var grønne.
- Forsøk på `git add` for nye ressursfiler og avledet publiseringsgrunnlag ble blokkert av `Permission denied` på `.git/index.lock`, så filene er fortsatt ikke lagt i Git-indeksen fra denne kjøringen.

## Hva bør tas i neste batch

1. Vurdere `Legemiddelregisteret` som ny ressurs før neste større helsebolk.
2. Ta `FHI-005` Norsk pasientregister og `FHI-006` Kommunalt pasient- og brukerregister som neste naturlige par når helseavgrensningen er avklart.
