---
date: 2026-04-11
author: codex
status: draft
topic: vurdering-av-nye-ressurskandidater
sources:
  - arkitektur/ressurser/styringsregler.md
  - sources/links.md
---

# Vurdering av nye ressurskandidater

## Formål
Dette notatet vurderer et lite sett nye ressurskandidater opp mot de oppdaterte opptakskravene for NA-oversikten.

Det er særlig lagt vekt på én ny presisering:
- sektorspesifikke løsninger bør normalt ikke tas inn bare fordi de er store eller viktige i egen sektor
- de bør bare tas inn når de også har tydelig betydning for samhandling på tvers av sektorer eller forvaltningsnivåer

## Vurderingsgrunnlag
Kandidatene er vurdert mot:
- må-kravene i `arkitektur/ressurser/styringsregler.md`
- vurderingskriteriene utover minstekravene
- den praktiske femspørsmålstesten

## Kort konklusjon

### Bør inn
- `NVDB`

### Bør vurderes nærmere før eventuell innlegging
- `Videokonsultasjon (VIO)`
- `Enhetsregisteret API / åpne data`

### Bør ikke inn nå
- `Virtuelle møterom`
- `KS Bibliotek`

## Vurdering per kandidat

### 1. NVDB
**Foreløpig vurdering:** Bør inn

**Hvorfor**
- Ressursen er tydelig avgrenset og har identifiserbar forvalter.
- Den har varig rolle som nasjonal datakilde og delingsressurs for vegdata.
- Den kan påvirke caseanalyser der geografi, transport, planlegging, beredskap eller tverrsektorielt datagrunnlag er relevant.
- Den har tydelig verdi utover én sektor fordi vegdata brukes i samspill med mange andre aktører og forvaltningsnivåer.

**Kommentar**
NVDB treffer den nye terskelen godt, fordi den ikke bare er viktig i samferdsel, men også har tydelig verdi som delt nasjonalt informasjonsgrunnlag.

### 2. Videokonsultasjon (VIO)
**Foreløpig vurdering:** Bør vurderes nærmere før eventuell innlegging

**Hvorfor**
- Ressursen er tydelig operativ og har identifiserbar forvalter.
- Den har varig rolle i helse, men det er foreløpig mindre tydelig om den har tilstrekkelig verdi for samhandling på tvers av sektorer eller forvaltningsnivåer til å høre hjemme i NA-oversikten.
- Den kan være relevant på tvers av forvaltningsnivåer innen helse, men det er ikke det samme som tverrsektoriell verdi.

**Kommentar**
Dette er et godt eksempel på en ressurs som er viktig i egen sektor, men som bør vurderes strengere mot den nye opptaksterskelen. Hvis hovedverdien er intern i helsesektoren, bør den kanskje ikke prioriteres inn nå.

### 3. Enhetsregisteret API / åpne data
**Foreløpig vurdering:** Bør vurderes nærmere før eventuell innlegging

**Hvorfor**
- Ressursen har tydelig verdi for samhandling og deling på tvers.
- Den kan være mer relevant i praksis enn registeret som abstrakt ressurs, fordi det er delingsflaten andre faktisk bruker.
- Samtidig er det uklart om den bør være egen ressurs, eller om dette heller bør løses ved å styrke eksisterende beskrivelse av `Enhetsregisteret`.

**Kommentar**
Dette er først og fremst et avklaringsspørsmål om ressursnivå:
- egen delressurs
- eller tydeligere beskrevet operativ delingsflate i eksisterende ressurs

### 4. Virtuelle møterom
**Foreløpig vurdering:** Bør ikke inn nå

**Hvorfor**
- Ressursen kan være nyttig og operativ, men framstår foreløpig som mer sektorspesifikk og mindre sentral i tverrsektorielle samhandlingsanalyser.
- Den virker svakere på kriteriet om å påvirke anbefalinger i case på tvers av sektorer eller forvaltningsnivåer.

**Kommentar**
Bør eventuelt vurderes på nytt hvis det dukker opp case der den faktisk har tydelig nasjonal eller tverrgående rolle.

### 5. KS Bibliotek
**Foreløpig vurdering:** Bør ikke inn nå

**Hvorfor**
- Ressursen ser ut til å være tydelig avgrenset, men den framstår foreløpig som sektorspesifikk og uten sterk nok kobling til tverrsektoriell digital samhandling.
- Det er ikke tydelig nok at den vil påvirke caseanalyser utover kommunal sektor.

**Kommentar**
Bør holdes utenfor NA-oversikten inntil det eventuelt finnes tydeligere grunnlag for nasjonal og tverrgående relevans.

## Foreslått arbeidsregel videre
Ved nye sektorspesifikke kandidater bør vi eksplisitt stille dette spørsmålet tidlig:

`Har denne ressursen betydning utover egen sektor, enten i samhandling på tvers av sektorer eller mellom forvaltningsnivåer?`

Hvis svaret er uklart eller svakt, bør ressursen normalt ikke tas inn i NA-oversikten nå.

## Anbefalt neste steg
1. Ta `NVDB` som neste klare kandidat.
2. Avklar om `Enhetsregisteret API / åpne data` skal være egen ressurs eller del av `Enhetsregisteret`.
3. Vent med `Videokonsultasjon` til vi eventuelt ser tydeligere tverrgående analyseverdi.
