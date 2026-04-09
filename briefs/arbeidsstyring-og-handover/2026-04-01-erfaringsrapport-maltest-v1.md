---
date: 2026-04-01
author: copilot
status: draft
topic: erfaringsrapport-maltest-arkitekturassistert-analyse
sources:
  - Analyser/2026-03-31-case-overgang-ungdomsskole-videregaende-v2.md
  - Analyser/2026-03-31-case-tilgjengeliggjoring-resultater-videregaende-v1.md
  - config/templates/arkitekturassistert-analyse-av-utviklingsbehov-template.md
  - config/prompts/arkitekturassistert-analyse-av-utviklingsbehov.system.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/
---

# Erfaringsrapport: test av mal for arkitekturassistert analyse av utviklingsbehov

## Bakgrunn

Malen og instruksen ble testet pÃ¥ to relaterte problemstillinger:
- overgang fra ungdomsskole til videregÃ¥ende opplÃ¦ring
- tilgjengeliggjÃ¸ring av resultater fra videregÃ¥ende opplÃ¦ring

## Hva fungerte godt

- Malen ga en tydelig struktur fra problembilde til tiltak.
- Koblingen mellom kapabiliteter, prinsipper og produkter ble konkret og sporbar.
- Kravet om Ã¥ bruke produktkatalogen som fasit reduserte risiko for generiske eller uforankrede forslag.
- Kortversjon for ledelse fungerte godt for styringsdialog.

## Hva fungerte mindre godt i fÃ¸rste runde

- Ã‰n samlet analyse med to problemstillinger gjorde produktvurderingen mindre presis.
- Tiltaksprioriteringen ble delvis blandet mellom to ulike overganger.
- Noen produktbeskrivelser var gode pÃ¥ produktfakta, men svake pÃ¥ beslutningsstÃ¸tte (nÃ¥r velges produktet, nÃ¥r velges det ikke).

## Tiltak som ble innfÃ¸rt etter test

- Case ble splittet i separate analyser per problemstilling.
- Instruksen fikk eksplisitt regel for nÃ¥r analyse skal splittes.
- Malen ble utvidet med tidlig avklaring av om input er ett eller flere case.
- Mal og instruks ble utvidet med:
  - fast vurderingsrekkefÃ¸lge for produktkategorier
  - eksplisitt gap-type per tiltak (produkt, semantisk, juridisk, samordning)
  - krav om sammensatt lÃ¸sningsmÃ¸nster fÃ¸r nyutvikling foreslÃ¥s

## Vurdering av produktbeskrivelsene i testen

### SÃ¦rlig sterke beskrivelser

- Feide
- Altinn autorisasjon
- Altinn Events
- Dialogporten
- Nasjonal vitnemÃ¥lsdatabase
- Begrepskatalog

Kjennetegn:
- tydelig scope/avgrensning
- god forklaring av produktets operative rolle
- lettere Ã¥ bruke som beslutningsstÃ¸tte i analyser

### Beskrivelser med stÃ¸rst forbedringsbehov

- OpptakslÃ¸sninger (hadde kort og smalt fÃ¸rsteutkast, fortsatt behov for tydeligere beslutningsstÃ¸tte)
- FIKS-plattformen (hadde behov for tydeligere beslutningsstÃ¸ttefelt i fÃ¸rste versjon)
- VitnemÃ¥lsportalen (hadde behov for tydeligere avgrensning i bruk i fÃ¸rste versjon)

## Oppdatert vurdering etter forbedringer

Det er nÃ¥ lagt inn standard beslutningsstÃ¸ttefelt i utvalgte produktbeskrivelser:
- typiske brukssituasjoner
- nÃ¥r produktet normalt ikke er fÃ¸rstevalg
- vanlige kombinasjoner med andre produkter

Dette gjÃ¸r produktbeskrivelsene mer anvendelige i nye analyser uten case-spesifikk tilpasning.

### Status etter ny sjekk av de tre beskrivelsene

- FIKS-plattformen: beslutningsstÃ¸ttefeltene er nÃ¥ tydelige og anvendelige (typiske brukssituasjoner, ikke-fÃ¸rstevalg, kombinasjoner). Kun mindre forbedringsbehov gjenstÃ¥r.
- VitnemÃ¥lsportalen: avgrensningen er nÃ¥ tydeligere (hva som inngÃ¥r/ikke inngÃ¥r, nÃ¥r produktet ikke er fÃ¸rstevalg). Kun mindre forbedringsbehov gjenstÃ¥r.
- OpptakslÃ¸sninger: beslutningsstÃ¸ttefeltene er nÃ¥ lagt inn, og beskrivelsen er dermed mer konsistent med mÃ¸nsteret brukt i de sterkeste produktbeskrivelsene.

Etter samme gjennomgang ble ogsÃ¥ Nasjonal vitnemÃ¥lsdatabase og Nasjonalt utdanningsregister vurdert som kandidater for sterkere beslutningsstÃ¸tte. Begge er nÃ¥ oppdatert med tydeligere brukssituasjoner, ikke-fÃ¸rstevalg og vanlige kombinasjoner med andre produkter.

## Konklusjon

UtprÃ¸vingen bekrefter at oppsettet fungerer bÃ¥de som rask analyse og beslutningsgrunnlag, sÃ¥ lenge flere problemstillinger splittes tidlig og produktvurderingen fÃ¸lger fast metode.

StÃ¸rste gevinst i testen:
- bedre sporbarhet mellom problembilde og tiltak
- mer presis bruk av eksisterende produkter fÃ¸r nyutvikling foreslÃ¥s
- tydeligere skille mellom tekniske, juridiske, semantiske og samordningsmessige gap

## Anbefalt neste forbedring

Legg inn en enkel evalueringsrubrikk i malen (score 1-5) for:
- sporbarhet
- gjenbrukbarhet
- styringsrelevans
- presisjon i produktvurdering

## Enkel beslutningspakke (fast leveranse per analyse)

### 1) Kortversjon for ledelse (1 side)

Skal alltid inneholde:
- problem og Ã¸nsket effekt (kort)
- anbefalt retning (gjenbruk, sammensatt lÃ¸sning eller nyutvikling)
- topp 3 tiltak med forventet effekt
- viktigste risikoer og avhengigheter
- beslutning som trengs nÃ¥

### 2) Full analyse (arbeidsdokument)

Skal alltid inneholde:
- problembilde, avgrensning og berÃ¸rte aktÃ¸rer
- vurdering av relevante produkter i fast rekkefÃ¸lge
- tydelig begrunnelse for produktvalg og fravalg
- kapabilitetsmapping for anbefalt lÃ¸sningsmÃ¸nster og sentrale produktvalg
- gap per tiltak (produkt, semantisk, juridisk, samordning)
- anbefalt lÃ¸sningsmÃ¸nster og prioritering

### 3) Tiltakslogg for styring og oppfolging

Skal alltid inneholde:
- tiltak, ansvarlig, frist, status
- forventet gevinst og mÃ¥lepunkt
- berÃ¸rt kapabilitet eller kapabilitetsgap per tiltak
- avhengigheter og beslutningspunkt
- risikoeier for tiltak med hÃ¸y usikkerhet

### ForeslÃ¥tt arbeidsflyt

- utarbeid full analyse
- trekk ut kortversjon for ledelse
- oppdater tiltakslogg med beslutninger og eierskap

### Kort sjekkliste for kapabilitetsmapping

Brukes sammen med full analyse og tiltakslogg:
- Hvilke 1-3 kapabiliteter er direkte realisert av anbefalt lÃ¸sningsmÃ¸nster?
- Hvilke kapabiliteter stÃ¸ttes av produktets faktiske hovedfunksjoner, ikke bare av beslutningsstÃ¸ttefeltene?
- Er det kapabiliteter som bare er indirekte berÃ¸rt gjennom kombinasjoner med andre produkter? Hvis ja, skal de normalt ikke mappes til produktet alene.
- Finnes det et tydelig kapabilitetsgap bak tiltaket, for eksempel manglende datadeling, datastyring, autentisering eller organisatorisk samhandling?
- Er kapabilitetsmappingen konsistent med begrunnelsen for produktvalg og fravalg?

