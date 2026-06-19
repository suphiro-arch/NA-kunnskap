---
date: 2026-06-18
author: codex
status: aktiv
topic: kapabilitetsendringer-konsekvensanalyse
---

# Konsekvensanalyse av oppdaterte kapabilitetsbeskrivelser

## Kort status

Denne analysen følger opp modelloppdateringen fra Digdir der kapabilitetsbeskrivelsene i `arkitektur/kapabiliteter/capabilities.yaml` ble vesentlig utvidet. Formålet er å se hvilke endringer som bør påvirke ressursbeskrivelser/canvaser, og hvilke kontroller som bør hindre at gamle kapabilitetsnavn, slugger eller avledede pekere blir liggende igjen.

Konklusjon:
- Den tekniske navneendringen fra `Meldingsformidling` til `Meldingsutveksling` er håndtert i aktiv mapping, register og webgrunnlag.
- De nye beskrivelsene gir mer analyseinnhold enn bare nye definisjoner. De gjør juridisk, organisatorisk, semantisk og teknisk vurdering viktigere i flere canvaser.
- Første målrettede canvasløft er gjennomført for `DIGDIR-033` Referansearkitektur forsendelse (eMelding), fordi ressursen både var direkte berørt av navneendringen og hadde tynn kapabilitetsseksjon.

## Kapabiliteter med størst semantisk endring

Maskinell differanse mot forrige lokale modellversjon viser at flere kapabiliteter har fått lange, nye beskrivelser med eksplisitte vurderingsdimensjoner. De viktigste for videre ressursarbeid er:

| Kapabilitet | Hvorfor viktig nå | Typisk effekt på canvaser |
|---|---|---|
| Arkitekturstyring | Beskrivelsen er utvidet med styring, portefølje, felles rammer, modenhet og oppfølging av nasjonale byggeklosser. | Samarbeidsfora, rammeverk og styringsressurser bør forklare tydeligere hvordan de påvirker beslutninger og prioritering. |
| Sammenhengende tjenester | Beskrivelsen kobler brukeropplevelse, juridiske rammer, tjenesteeierskap, semantikk og teknisk samspill. | Sluttbrukerrettede og tverrsektorielle ressurser bør beskrive reell tjenestekjedeeffekt, ikke bare portal eller kanal. |
| Sikring av informasjonsflyt og datautveksling | Beskrivelsen gjør sikkerhet i informasjonsflyt til mer enn teknisk beskyttelse. | Ressurser med datadeling, meldinger eller API bør vurdere sporbarhet, tilgang, konfidensialitet og avvik tydeligere. |
| Meldingsutveksling | Nytt navn og rikere innhold: meldinger forstås som avtalt prosess, informasjonsmodell, sikkerhet og kvittering/avvik, ikke bare transport. | Meldingsressurser bør forklare roller, ansvar, meldingsformat, kvittering, avvik og grense mot oppslag/hendelser. |
| Hendelsesdrevet | Beskrivelsen tydeliggjør hendelser som samhandlingsmønster med egne organisatoriske og tekniske krav. | Hendelsesressurser bør tydeligere skilles fra meldingsforsendelse og synkrone oppslag. |
| Juridisk samhandling | Regelverksutvikling og regelverkstolkning er mer substansielt beskrevet. | Normerende og juridiske ressurser bør beskrive når de påvirker hjemmel, ansvar, avtaler og etterlevelse. |
| Datakilder og grunndata | Beskrivelsene styrker koblingen mellom autoritative datakilder, dataansvar, semantikk og sammenhengende tjenester. | Register- og datakilderessurser bør skille bedre mellom datakilde, tilgang, kvalitet, ansvar og gjenbruk. |

## Prioritert canvaskø

Maskinell sjekk av aktive ressursfiler viste særlig tynne kapabilitetsseksjoner i flere `v1`-beskrivelser. Første revisjonskø bør være:

1. `DIGDIR-033` Referansearkitektur forsendelse (eMelding) - gjennomført som `v2` i denne runden.
2. `DIGDIR-034` Referansearkitektur forespørsel-svar (eOppslag) - gjennomført som `v2` 2026-06-19 for å skille oppslag tydelig fra meldingsutveksling og hendelser.
3. `DIGDIR-027` Arkitektur for hendelser - gjennomført som `v2` 2026-06-19 fordi `Hendelsesdrevet` har fått tydeligere semantisk innhold.
4. `DIGDIR-025` Rammeverk for digital samhandling - gjennomført som `v2` 2026-06-19, med sterkere vurdering av juridisk, organisatorisk, semantisk og teknisk samhandling samlet.
5. `DIGDIR-030` Overordnede arkitekturprinsipper - gjennomført som `v2` 2026-06-19, med sterkere kobling til `Arkitekturstyring`.
6. `DIGDIR-031` Sjekkliste for sammenhengende tjenester og `DIGDIR-032` Kart for tjenestekjeder - bør vurderes mot ny `Sammenhengende tjenester`-beskrivelse.

Operative ressurser som bør inn i senere batch:
- Meldings- og forsendelsesressurser: eFormidling, Altinn Formidling, Altinn Melding, Digital postkasse, Fiks Melding, Fiks SvarUt, SvarInn og Peppol eDelivery.
- Sikker datautveksling og API-/datadelingsressurser: ID-porten, Maskinporten, Altinn Events, Felles datakatalog, data.norge.no, Helsenorge/Kjernejournal og sentrale registertilganger.

## Første målrettede canvasløft

Opprettet ny versjon:
- `arkitektur/ressurser/normerende-ressurser/101-Referansearkitektur-forsendelse-eMelding-v2-codex.md`

Viktigste forbedringer:
- Kapabilitetsseksjonen er utvidet med forklaring av `Meldingsutveksling` og `Forvaltningsstandarder`.
- Teksten forklarer eMelding som mønster for meldingsforsendelse fra avsender til kjent mottaker.
- Forpliktelsesnivå, bruksområde, analyse- og beslutningssituasjoner og avgrensning mot eOppslag/hendelser er tydeligere.
- Risiko og prinsippvurdering er oppdatert slik at ressursen kan brukes mer direkte i analyser.

## Andre målrettede canvasløft

Opprettet nye versjoner 2026-06-19:
- `arkitektur/ressurser/normerende-ressurser/102-Referansearkitektur-foresporsel-svar-eOppslag-v2-codex.md`
- `arkitektur/ressurser/normerende-ressurser/87-Arkitektur-for-hendelser-v2-codex.md`

Viktigste forbedringer:
- eOppslag er tydeliggjort som oppslagsmønster for bruk av data fra datatilbyder, med sterkere vurdering av formål, tilgang, ansvar, datakvalitet, sporbarhet og teknisk robusthet.
- Arkitektur for hendelser er tydeliggjort som hendelsesdrevet samhandlingsmønster, med sterkere skille mellom hendelser, kommandoer, oppslag og meldingsforsendelse.
- Begge beskrivelsene har fått tydeligere avgrensning mot eMelding og mot hverandre, slik at de kan brukes bedre i mønstervalg og tidligfaseanalyse.
- Register, kapabilitetsmapping, kildeliste og webgrunnlag er oppdatert til å peke på de nye `v2`-filene.

## Tredje målrettede canvasløft

Opprettet nye versjoner 2026-06-19:
- `arkitektur/ressurser/normerende-ressurser/85-Rammeverk-for-digital-samhandling-v2-codex.md`
- `arkitektur/ressurser/normerende-ressurser/98-Overordnede-arkitekturprinsipper-for-offentlig-sektor-v2-codex.md`

Viktigste forbedringer:
- Rammeverk for digital samhandling er tydeliggjort som helhetlig samhandlingsgrunnlag der juridiske, organisatoriske, semantiske og tekniske vurderinger må ses samlet.
- Overordnede arkitekturprinsipper er tydeliggjort som aktivt styringsgrunnlag for arkitekturvalg, porteføljeprioritering, avviksbegrunnelse og oppfølging av nasjonale byggeklosser.
- Begge beskrivelsene er oppdatert med mer direkte beslutningssituasjoner, risiko, avgrensning og kobling til kapabiliteter.
- Register, kapabilitetsmapping, kildeliste og webgrunnlag er oppdatert til å peke på de nye `v2`-filene.

## Kontroll- og vedlikeholdstiltak

`tools/check-resource-version-sync.py` er utvidet slik at kontrollen nå også sjekker:
- avledede produktreferanser inne i `produkt-kapabilitet-koblinger.yaml`, ikke bare toppnivået i `products`
- at `capability_slug`, `subcapability_slug`, `capability_id` og `subcapability_id` finnes i `capabilities.yaml`
- at genererte kapabilitetssider i `web/hugo-prototype/content/kapabiliteter/` ikke inneholder mapper for utgåtte kapabilitetsslugger

Dette skal fange samme type restfeil som oppsto da `meldingsformidling` fortsatt lå igjen som generert webside og i gamle avledede mappingseksjoner.

## Videre plan

1. Kjør en liten operativ batch for meldings-, oppslags- og hendelsesressursene, men bare der kapabilitetsseksjonen ikke allerede forklarer roller, ansvar, tilgang, kvittering, avvik, sikkerhet og robusthet godt nok.
2. Løft `DIGDIR-031` Sjekkliste for sammenhengende tjenester og `DIGDIR-032` Kart for tjenestekjeder mot ny `Sammenhengende tjenester`-beskrivelse.
3. Vurder om `DIGDIR-041` Kapabilitetskart trenger et mindre justeringsløft mot ny `Arkitekturstyring`, selv om registeret allerede peker til `v2`.
4. Lag en fast rapportfunksjon for "tynne kapabilitetsseksjoner" hvis denne analysen skal gjentas ukentlig.
5. Vurder om `produkt-kapabilitet-koblinger.yaml` bør deles i én manuell masterdel og én generert avledet del, slik at metadata ikke kan drive fra hverandre.
