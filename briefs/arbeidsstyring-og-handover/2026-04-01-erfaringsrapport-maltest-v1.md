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

Malen og instruksen ble testet på to relaterte problemstillinger:
- overgang fra ungdomsskole til videregående opplæring
- tilgjengeliggjøring av resultater fra videregående opplæring

## Hva fungerte godt

- Malen ga en tydelig struktur fra problembilde til tiltak.
- Koblingen mellom kapabiliteter, prinsipper og produkter ble konkret og sporbar.
- Kravet om å bruke produktkatalogen som fasit reduserte risiko for generiske eller uforankrede forslag.
- Kortversjon for ledelse fungerte godt for styringsdialog.

## Hva fungerte mindre godt i første runde

- ån samlet analyse med to problemstillinger gjorde produktvurderingen mindre presis.
- Tiltaksprioriteringen ble delvis blandet mellom to ulike overganger.
- Noen produktbeskrivelser var gode på produktfakta, men svake på beslutningsstøtte (når velges produktet, når velges det ikke).

## Tiltak som ble innført etter test

- Case ble splittet i separate analyser per problemstilling.
- Instruksen fikk eksplisitt regel for når analyse skal splittes.
- Malen ble utvidet med tidlig avklaring av om input er ett eller flere case.
- Mal og instruks ble utvidet med:
  - fast vurderingsrekkefølge for produktkategorier
  - eksplisitt gap-type per tiltak (produkt, semantisk, juridisk, samordning)
  - krav om sammensatt løsningsmønster før nyutvikling foreslås

## Vurdering av produktbeskrivelsene i testen

### Særlig sterke beskrivelser

- Feide
- Altinn autorisasjon
- Altinn Events
- Dialogporten
- Nasjonal vitnemålsdatabase
- Begrepskatalog

Kjennetegn:
- tydelig scope/avgrensning
- god forklaring av produktets operative rolle
- lettere å bruke som beslutningsstøtte i analyser

### Beskrivelser med størst forbedringsbehov

- Opptaksløsninger (hadde kort og smalt førsteutkast, fortsatt behov for tydeligere beslutningsstøtte)
- FIKS-plattformen (hadde behov for tydeligere beslutningsstøttefelt i første versjon)
- Vitnemålsportalen (hadde behov for tydeligere avgrensning i bruk i første versjon)

## Oppdatert vurdering etter forbedringer

Det er nå lagt inn standard beslutningsstøttefelt i utvalgte produktbeskrivelser:
- typiske brukssituasjoner
- når produktet normalt ikke er førstevalg
- vanlige kombinasjoner med andre produkter

Dette gjør produktbeskrivelsene mer anvendelige i nye analyser uten case-spesifikk tilpasning.

### Status etter ny sjekk av de tre beskrivelsene

- FIKS-plattformen: beslutningsstøttefeltene er nå tydelige og anvendelige (typiske brukssituasjoner, ikke-førstevalg, kombinasjoner). Kun mindre forbedringsbehov gjenstår.
- Vitnemålsportalen: avgrensningen er nå tydeligere (hva som inngår/ikke inngår, når produktet ikke er førstevalg). Kun mindre forbedringsbehov gjenstår.
- Opptaksløsninger: beslutningsstøttefeltene er nå lagt inn, og beskrivelsen er dermed mer konsistent med mønsteret brukt i de sterkeste produktbeskrivelsene.

Etter samme gjennomgang ble også Nasjonal vitnemålsdatabase og Nasjonalt utdanningsregister vurdert som kandidater for sterkere beslutningsstøtte. Begge er nå oppdatert med tydeligere brukssituasjoner, ikke-førstevalg og vanlige kombinasjoner med andre produkter.

## Konklusjon

Utprøvingen bekrefter at oppsettet fungerer både som rask analyse og beslutningsgrunnlag, så lenge flere problemstillinger splittes tidlig og produktvurderingen følger fast metode.

Største gevinst i testen:
- bedre sporbarhet mellom problembilde og tiltak
- mer presis bruk av eksisterende produkter før nyutvikling foreslås
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
- problem og ønsket effekt (kort)
- anbefalt retning (gjenbruk, sammensatt løsning eller nyutvikling)
- topp 3 tiltak med forventet effekt
- viktigste risikoer og avhengigheter
- beslutning som trengs nå

### 2) Full analyse (arbeidsdokument)

Skal alltid inneholde:
- problembilde, avgrensning og berørte aktører
- vurdering av relevante produkter i fast rekkefølge
- tydelig begrunnelse for produktvalg og fravalg
- kapabilitetsmapping for anbefalt løsningsmønster og sentrale produktvalg
- gap per tiltak (produkt, semantisk, juridisk, samordning)
- anbefalt løsningsmønster og prioritering

### 3) Tiltakslogg for styring og oppfolging

Skal alltid inneholde:
- tiltak, ansvarlig, frist, status
- forventet gevinst og målepunkt
- berørt kapabilitet eller kapabilitetsgap per tiltak
- avhengigheter og beslutningspunkt
- risikoeier for tiltak med høy usikkerhet

### Foreslått arbeidsflyt

- utarbeid full analyse
- trekk ut kortversjon for ledelse
- oppdater tiltakslogg med beslutninger og eierskap

### Kort sjekkliste for kapabilitetsmapping

Brukes sammen med full analyse og tiltakslogg:
- Hvilke 1-3 kapabiliteter er direkte realisert av anbefalt løsningsmønster?
- Hvilke kapabiliteter støttes av produktets faktiske hovedfunksjoner, ikke bare av beslutningsstøttefeltene?
- Er det kapabiliteter som bare er indirekte berørt gjennom kombinasjoner med andre produkter? Hvis ja, skal de normalt ikke mappes til produktet alene.
- Finnes det et tydelig kapabilitetsgap bak tiltaket, for eksempel manglende datadeling, datastyring, autentisering eller organisatorisk samhandling?
- Er kapabilitetsmappingen konsistent med begrunnelsen for produktvalg og fravalg?



