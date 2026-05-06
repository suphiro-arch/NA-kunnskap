# Prioritering av kapabiliteter basert på modenhet og ressursdekning

**Dato:** 2026-05-05  
**Utarbeidet av:** Codex med lokalt MCP-grunnlag (`arkifix-mcp`)  
**Grunnlag:** [2026-05-05-modenhetsanalyse-felleslosninger-ssb.md](./2026-05-05-modenhetsanalyse-felleslosninger-ssb.md), `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`, MCP-verktøyet `get_product_capability_links()`

---

## Formål

Denne analysen supplerer modenhetsanalysen med ett ekstra spørsmål: hvilke kapabiliteter bør prioriteres først når vi også ser på hvor mange ressurser i repoet som faktisk støtter eller berører dem?

Utgangspunktet er at kapabiliteter med både lav modenhet og høy ressursdekning er gode kandidater for prioritering. De representerer sannsynlige flaskehalser som påvirker mange ressurser samtidig.

---

## Metode

Analysen bygger på koblingene i `produkt-kapabilitet-koblinger.yaml`, hentet via MCP-serveren `arkifix-mcp`. For hver kapabilitet og delkapabilitet er det telt antall unike ressurser som er koblet til den.

Dette er sammenholdt med modenhetsvurderingene i den eksisterende modenhetsanalysen fra samme dato.

**Tolkning:**

- Lav modenhet + mange koblede ressurser = høy prioritetsverdi
- Lav modenhet + få eller ingen koblede ressurser = mulig blindflekk eller umodent område som bør bygges opp
- Høy modenhet + mange koblede ressurser = styrkeområde som kan brukes som fundament for videre utvikling

---

## Ressursdekning i dagens portefølje

Antall ressurser per toppnivå-kapabilitet:

| Kapabilitet | Antall ressurser |
|---|---:|
| Datautveksling og integrasjon | 63 |
| Samarbeid | 32 |
| Informasjonsforvaltning | 28 |
| Datakilder | 27 |
| Tjenesteutvikling | 22 |
| Sluttbrukertjenester | 22 |
| Standardisering | 20 |
| Informasjonssikkerhet | 19 |
| Strategisk styring | 17 |
| Tillit | 16 |

Delkapabiliteter med høyest ressursdekning:

| Delkapabilitet | Antall ressurser |
|---|---:|
| Datautveksling og integrasjon: Dele data med andre | 42 |
| Datakilder: Grunndata | 27 |
| Datautveksling og integrasjon: Bruke data fra andre | 20 |
| Samarbeid: Organisatorisk samhandling | 20 |
| Sluttbrukertjenester: Sammenhengende tjenester | 20 |
| Standardisering: Forvaltningsstandarder | 20 |
| Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling | 19 |
| Informasjonsforvaltning: Datastyring | 17 |

Totalt antall produkter og ressurser i tellingen: **115**

---

## Prioriterte kapabiliteter

### 1. Datautveksling og integrasjon -> Bruke data fra andre

**Modenhet:** Lav  
**Ressursdekning:** 20

Dette framstår som en av de tydeligste prioriteringene. Modenhetsanalysen peker på systemintegrasjon som en betydelig hindring, samtidig som mange ressurser er avhengige av denne evnen. Det tyder på at området er en praktisk flaskehals i porteføljen.

### 2. Sluttbrukertjenester -> Sammenhengende tjenester

**Modenhet:** Lav  
**Ressursdekning:** 20

Dette området har både høy strategisk betydning og høy ressursberøring. Mangel på felles infrastruktur for sammenhengende tjenester slår sannsynligvis bredt ut i mange av ressursene som allerede er beskrevet.

### 3. Informasjonsforvaltning -> Datastyring

**Modenhet:** Lav  
**Ressursdekning:** 17

Datastyring ser ut til å være et grunnlagsproblem. Når dette området er svakt, blir også deling, gjenbruk, oversikter og sammenstilling av data vanskeligere. Dette er derfor en kandidat med høy systemeffekt.

### 4. Sluttbrukertjenester -> Tjenestekjeder

**Modenhet:** Lav  
**Ressursdekning:** 6

Dekningen er lavere enn for sammenhengende tjenester, men kapabiliteten er tett koblet til samme problemrom. Hvis målet er reell samhandling på tvers av virksomheter, er dette et naturlig oppfølgingsområde.

### 5. Tillit -> Representasjon

**Modenhet:** Lav  
**Ressursdekning:** 3

Dette er ikke et bredt dekket område i dagens ressursmasse, men det er strategisk viktig. Representasjon og fullmakter er ofte en forutsetning for at personer og virksomheter kan handle på vegne av andre i digitale tjenester.

---

## Områder som ser ut som blinde flekker

Noen kapabiliteter vurderes som svake i modenhetsanalysen, men har svært få eller ingen koblede ressurser i dagens portefølje.

| Delkapabilitet | Modenhet | Antall ressurser | Tolking |
|---|---|---:|---|
| Strategisk styring: Finansiering | Lav | 0 | Kritisk styringsproblem, men svakt representert i ressursmassen |
| Juridisk samhandling | Lav | 0 | Viktig hinderområde uten tydelig ressursdekning |
| Datakilder: Sanntidsdata | Lav | 0 | Lite operasjonalisert i dagens portefølje |
| Datakilder: Testdata | Lav | 0 | Tyder på manglende nasjonal infrastruktur og svak porteføljerepresentasjon |
| Datakilder: Ustrukturerte data | Lav | 0 | Område med lav modenhet og lite eksplisitt ressursfokus |
| Informasjonsforvaltning: Oversikt over hendelser | Lav | 1 | Svak dekning i et område som er viktig for hendelsesdrevet samhandling |
| Tillit: Samtykke | Lav | 1 | Umodent område med svært begrenset porteføljestøtte |
| Samarbeid: Tjenesteforvaltning | Lav | 2 | Høy praktisk betydning, men lite eksplisitt ressursmessig forankring |

Disse områdene bør ikke nødvendigvis prioriteres først for bred porteføljeeffekt, men de bør vurderes som kandidater for målrettet oppbygging av nye normerende ressurser, styringsgrunnlag eller tydeligere kapabilitetskoblinger.

---

## Anbefalt prioriteringsrekkefølge

Basert på kombinasjonen av lav modenhet og høy ressursdekning anbefales følgende prioriteringsrekkefølge:

1. `Datautveksling og integrasjon -> Bruke data fra andre`
2. `Sluttbrukertjenester -> Sammenhengende tjenester`
3. `Informasjonsforvaltning -> Datastyring`
4. `Sluttbrukertjenester -> Tjenestekjeder`
5. `Tillit -> Representasjon`

Hvis målet i stedet er å styrke selve kunnskapsgrunnlaget i repoet, bør en parallell prioritering være å bygge opp bedre ressursdekning for:

1. `Strategisk styring -> Finansiering`
2. `Juridisk samhandling`
3. `Datakilder -> Sanntidsdata`
4. `Datakilder -> Testdata`
5. `Informasjonsforvaltning -> Oversikt over hendelser`

---

## Konklusjon

Sammenstillingen peker på at neste store innsats bør rettes mot kapabiliteter som allerede berører mange ressurser, men som fortsatt framstår som svake i modenhetsanalysen. Særlig gjelder dette evnen til å bruke data fra andre, etablere sammenhengende tjenester og styrke datastyring som felles grunnlag.

Analysen peker også på flere blinde flekker i porteføljen. Disse handler særlig om finansiering, juridisk samhandling og enkelte datakildekapabiliteter. Her kan det være behov for både flere ressursbeskrivelser og tydeligere normerende grunnlag.
