---
date: 2026-03-16
author: codex
status: draft
topic: dokumentasjonsassistent-mvp
sources:
  - web/hugo-prototype/README.md
  - briefs/arbeidsstyring-og-handover/AUTOMATISK-PUSH-SETUP.md
  - arkitektur/kapabiliteter/capabilities.yaml
  - arkitektur/ressurser/operative-losninger-og-tjenester/
  - https://platform.openai.com/docs/api-reference/responses/tutorials-and-guides
  - https://platform.openai.com/docs/guides/tools-file-search
  - https://openai.com/policies/services-agreement/
  - https://openai.com/policies/data-processing-addendum
  - https://openai.com/policies/api-data-usage-policies/
  - https://platform.openai.com/docs/usage-policies/usage-policies
---

# MVP-skisse: dokumentasjonsassistent for nasjonal arkitektur

## FormÃ¥l

Lage en Ã¥pen dokumentasjonsassistent pÃ¥ nettsiden som bruker kun offentlig informasjon fra repoet og hjelper prosjekter med Ã¥:

- finne relevante produkter og kapabiliteter
- tolke prinsipper og underlag opp mot prosjektbehov
- peke pÃ¥ hva som bÃ¸r gjenbrukes
- synliggjÃ¸re mulige gap i kapabiliteter, produkter og styrende prinsipper
- fungere som en fÃ¸rste versjon av en bredere arkitekturassistent

Assistenten skal ikke vÃ¦re en generell chatbot. Den skal vÃ¦re en domenespesifikk veileder bygget pÃ¥ repoets innhold.

## Scope for MVP

MVP-en bÃ¸r bare gjÃ¸re tre ting:

1. Svare med grunnlag i repoet
2. Henvise til konkrete kilder i repoet
3. Hjelpe brukeren med tolkning og orientering i materialet

MVP-en bÃ¸r ikke i fÃ¸rste fase:

- skrive tilbake til repoet
- opprette issues eller PR-er
- bruke interne dokumenter
- bruke eksterne kilder i sanntid
- gi beslutninger uten kildegrunnlag

## Ã˜nsket brukeropplevelse

Brukeren kommer inn pÃ¥ den Ã¥pne nettsiden og kan stille spÃ¸rsmÃ¥l som:

- "Hvilke kapabiliteter er mest relevante for et prosjekt som skal dele data med andre virksomheter?"
- "Hvilke produkter bÃ¸r et prosjekt vurdere hvis de trenger representasjon, tilgangsstyring og meldingsutsending?"
- "Hva ser ut til Ã¥ mangle i prosjektet hvis mÃ¥let er proaktive tjenester?"
- "Hva bÃ¸r gjenbrukes i stedet for Ã¥ bygges lokalt?"

Assistenten skal svare med:

- kort vurdering
- relevante kapabiliteter
- relevante produkter
- relevante prinsipper
- eventuelle gap eller forbedringsomrÃ¥der
- kildehenvisninger til sider eller markdownfiler

## Hva dere allerede har

Eksisterende styrker i repoet:

- statisk nettside i `web/hugo-prototype`
- GitHub Pages-publisering fra Hugo-prototypen via workflow
- GitHub Actions for publisering
- strukturert dokumentgrunnlag i:
  - `arkitektur/kapabiliteter/capabilities.yaml`
  - `arkitektur/ressurser/operative-losninger-og-tjenester/`
  - `web/hugo-prototype/content/`
- generering av produktsider og kapabilitetssider
- lenker mellom produkter, kapabiliteter og prinsipper i nettstedet

Det betyr at dere allerede har et godt innholdslag. Det som mangler er et eget sporrende lag for retrieval og modellkall.

## Anbefalt arkitektur for MVP

```text
Bruker i nettleser
  -> Hugo/GitHub Pages frontend
  -> /api/ask pÃ¥ egen backend
  -> retrieval mot repo-basert kunnskapsbase
  -> OpenAI Responses API med file_search
  -> svar tilbake med kilder
```

## ForeslÃ¥tt lÃ¸sning

### 1. Frontend

Behold Hugo-siden som offentlig dokumentasjonsflate.

Legg til en enkel chat-komponent som:

- sender spÃ¸rsmÃ¥l til en backend
- viser svar med kildehenvisninger
- tilbyr ferdige spÃ¸rsmÃ¥l, for eksempel:
  - "Hvilke kapabiliteter er relevante?"
  - "Hvilke produkter bÃ¸r gjenbrukes?"
  - "Hva ser ut som gap?"

Frontend bÃ¸r ikke kalle modell-API direkte.

### 2. Backend

Legg til en liten backend, helst serverless.

Anbefaling:

- `Azure Functions` hvis dette skal inn i Digdir/Azure-oppsett
- alternativt enkel `Node.js`-tjeneste hvis dere vil prototype raskere

Backend bÃ¸r ha ett ansvar:

- ta imot spÃ¸rsmÃ¥l
- hente relevante dokumentbiter
- sende prompt + kunnskapsgrunnlag til modell
- returnere svar med kilder

### 3. Modell og retrieval

Anbefaling for MVP:

- `OpenAI Responses API`
- `file_search` med OpenAI-hosted vector store

Begrunnelse:

- minst mulig infrastruktur a drifte
- passer bra for repo-dokumentasjon
- raskest vei til prototype

Alternativ for fase 2:

- egen retrieval med `pgvector` eller tilsvarende

Det er bedre hvis dere senere vil ha mer kontroll, men bÃ¸r ikke vÃ¦re startpunktet.

### 4. Kunnskapsgrunnlag

MVP-en skal bruke bare offentlig repo-innhold.

FÃ¸rste kunnskapskilder:

- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/ressurser/operative-losninger-og-tjenester/*.md`
- `web/hugo-prototype/content/**/*.md`

Hver chunk bÃ¸r merkes med metadata:

- filsti
- seksjon
- produktnummer
- versjon
- kapabilitet
- type: `produkt`, `kapabilitet`, `prinsipp`, `oversikt`

### 5. Indeksering

Legg til en GitHub Action eller egen deploy-jobb som:

1. leser relevante filer fra repoet
2. splitter dem i mindre tekstbiter
3. laster dem til vector store
4. oppdaterer eller erstatter kunnskapsbasen ved ny publisering

Dette bÃ¸r trigges ved endringer i:

- `arkitektur/ressurser/operative-losninger-og-tjenester/`
- `arkitektur/`
- `web/hugo-prototype/content/`

## Svarprofil for assistenten

MVP-en bÃ¸r styres med en fast systeminstruks:

- bruk bare repoets offentlig publiserbare innhold
- svar som arkitekturassistent, ikke som generisk chatbot
- veiled prosjektet mot gjenbruk der det er relevant
- bruk kapabiliteter, produkter og prinsipper som analyseakse
- pek pÃ¥ gap eller svakheter nÃ¥r grunnlaget tilsier det
- oppgi alltid hvilke kilder i repoet som ligger til grunn
- si tydelig fra ved usikkerhet eller manglende dekning

## MVP-funksjoner

### MVP 1: Dokumentasjonsassistent

Skal kunne:

- svare pÃ¥ frie spÃ¸rsmÃ¥l
- foreslÃ¥ relevante kapabiliteter
- foreslÃ¥ relevante produkter
- peke pÃ¥ styrende prinsipper
- gi enkel gap-vurdering
- vise kildegrunnlag

### MVP 2: Veiledet prosjektmodus

Skal kunne ta inn et prosjektbehov som tekst og svare med:

- foreslÃ¥tte kapabiliteter
- relevante produkter
- relevante prinsipper
- forslag til gjenbruk
- mulige gap i prosjektet

Dette kan bygges som en enkel prompt-mal over samme backend.

## Teknologi som bÃ¸r avklares

### Frontend

Dere har:

- Hugo
- GitHub Pages

Dere mangler:

- chat-komponent
- kall til ekstern backend

Anbefaling:

- enkel JS-komponent integrert i Hugo

### Backend

Dere har ikke dette i repoet i dag.

Dere mÃ¥ velge:

- `Azure Functions` anbefales
- eventuelt en separat API-app

### Modell

Anbefaling:

- OpenAI `Responses API`

### Retrieval

Anbefaling for MVP:

- OpenAI `file_search`

### Drift og secrets

Dere mÃ¥ ha:

- OpenAI API-nÃ¸kkel
- backend-hosting
- env-vars / secrets i GitHub og backend-plattform

## Lisens- og avtaleavklaringer

### 1. OpenAI-avtale

For business/API-bruk gjelder OpenAI Services Agreement.

Kilde verifisert:

- oppdatert `1. desember 2025`
- effektiv fra `1. januar 2026`

Dette mÃ¥ legges til grunn hvis dere bygger lÃ¸sningen pÃ¥ OpenAI API.

### 2. Data Processing Addendum

Hvis dere sender innhold til OpenAI API og dette behandles som virksomhetsdata, mÃ¥ dere vurdere DPA-en.

Kilde verifisert:

- oppdatert `1. desember 2025`
- effektiv fra `1. januar 2026`

### 3. API-/business-data

OpenAI oppgir i sin virksomhets-/API-informasjon at de ikke trener modellene pÃ¥ API-data som standard.

Kilde verifisert:

- side oppdatert `8. januar 2026`

Dette er viktig for vurderingen av offentlig dokumentasjonsbruk.

### 4. Usage policies

Bruk mÃ¥ fortsatt fÃ¸lge OpenAI Usage Policies.

Kilde verifisert:

- effektiv fra `29. oktober 2025`

### 5. Lisens pÃ¥ repo-innholdet

Repoet har per nÃ¥ ingen eksplisitt `LICENSE`-fil.

Det mÃ¥ avklares fordi assistenten skal vÃ¦re Ã¥pen pÃ¥ internett og bruke innholdet som offentlig kunnskapsgrunnlag.

Anbefaling:

- vurder `CC BY 4.0` for dokumentasjonsinnhold hvis dere Ã¸nsker Ã¥pen gjenbruk med kreditering
- vurder separat kode-lisens, for eksempel `MIT`, hvis dere senere legger til applikasjonskode som skal deles

Hvis dere ikke vil lisensiere Ã¥pent, bÃ¸r dere minst dokumentere eksplisitt at innholdet er offentlig publisert som informasjon, men ikke fritt gjenbrukbart uten avklaring.

### 6. Offentlig informasjon

Siden assistenten skal vÃ¦re Ã¥pen pÃ¥ internett, bÃ¸r kun disse datatypene brukes i MVP:

- offentlig dokumentasjon i repoet
- ingen personopplysninger
- ingen interne notater
- ingen ikke-publiserte analyser

## ForeslÃ¥tt MVP-oppskrift

### Fase 0: Avklaringer

1. Bekreft at assistenten bare skal bruke offentlig innhold
2. Velg lisens for dokumentasjonsinnhold
3. Velg backend-plattform
4. Velg OpenAI som modellleverandÃ¸r for MVP

### Fase 1: Teknisk grunnmur

1. Opprett ny mappe for backend, for eksempel `apps/docs-assistant-api/`
2. Lag endpoint `POST /api/ask`
3. Sett opp OpenAI-klient
4. Sett opp enkel logging og rate limit

### Fase 2: Innhold og retrieval

1. Lag script som samler relevante markdown- og yaml-filer
2. Chunk dokumentene
3. Last dem til vector store
4. Behold metadata per dokumentbit

### Fase 3: Chat i nettsiden

1. Legg chatpanel i Hugo-prototypen
2. Legg inn faste forslag til spÃ¸rsmÃ¥l
3. Vis svar med:
   - oppsummering
   - relevante kapabiliteter
   - relevante produkter
   - relevante prinsipper
   - kilder

### Fase 4: Prosjektveiledning

Legg til en modus med ett fritekstfelt:

- "Beskriv prosjektet ditt"

Output:

- foreslÃ¥tte kapabiliteter
- relevante produkter
- relevante prinsipper
- mulige gap
- forslag til hva som bÃ¸r gjenbrukes

## ForeslÃ¥tte akseptansekriterier for MVP

- Assistenten er offentlig tilgjengelig via nettsiden
- Den bruker bare repoets offentlige innhold
- Den svarer med kildehenvisning
- Den kan finne relevante produkter og kapabiliteter for et prosjektbehov
- Den kan peke pÃ¥ gap og gjenbruksmuligheter
- Den gjÃ¸r ingen handlinger utover Ã¥ svare

## Viktigste risikoer

- Manglende eksplisitt lisens pÃ¥ dokumentasjonsinnholdet
- For ujevn kvalitet i eldre produktbeskrivelser gir ujevne svar
- For lite metadata i retrieval gir svak presisjon
- Ã…pen internettflate krever moderering, rate limiting og enkel misbruksbeskyttelse

## Anbefalt neste gjennomfÃ¸rbare steg

1. Avklar lisens for dokumentasjonsinnholdet
2. Velg backend-plattform, helst Azure Functions
3. Lag et minimalt backend-skjelett i repoet
4. Lag et enkelt indekseringsscript for repo-dokumentasjonen
5. Koble en enkel chat-widget til Hugo-prototypen

