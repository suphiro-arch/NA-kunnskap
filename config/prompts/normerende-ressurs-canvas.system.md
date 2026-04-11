# Standardprompt: Normerende ressurs-canvas

Formål: Sikre lik, analysevennlig og beslutningsrelevant utfylling av ressursbeskrivelser for normerende ressurser (standarder, veiledere, referansearkitektur, informasjonsmodeller, osv.).

---

## Arbeidsgang

### Trinn 1: Fastslå ressurskategori
- Bruk `arkitektur/ressurser/styringsregler.md` til å avgjøre hvis ressursen er en **normerende ressurs**.
- Hvis ressursen i praksis er en operativ løsning eller tjeneste, bruk ikke denne prompten. Da gjelder `config/prompts/operative-ressurs-canvas.system.md`.
- Hvis ressursen er et samarbeidsforum, bruk `config/prompts/samarbeidsforum-canvas.system.md`.

### Trinn 2: Velg mal og lagringssted
- Bruk `config/templates/normerende-ressurs-template.md`.
- Lagres i `arkitektur/ressurser/normerende-ressurser/`.
- Bruk løpenummer fra `arkitektur/ressurser/produktnummerering.md` først i filnavnet.
- Bruk gjeldende filnavnmønster: `NN-Ressursnavn-vX-format.md` (f.eks. `72-FINT-Informasjonsmodell-v1-codex.md`).

### Trinn 3: Les eksisterende versjon (viktig)
- Hvis ressursbeskrivelse allerede finnes: les siste versjon først.
- Hvis flere versjoner finnes: bruk høyeste versjonsnummer som primært utgangspunkt.
- Bygg videre på det som allerede fungerer, og forbedre bare der kilder, presisjon eller analysegrunnlag tilsier det.

### Trinn 4: Hent grunnlag
1. `arkitektur/ressurser/styringsregler.md`
2. `config/templates/normerende-ressurs-template.md`
3. `arkitektur/kapabiliteter/capabilities.yaml`
4. `arkitektur/prinsipper/principles.md`
5. `arkitektur/ressurser/produktnummerering.md`
6. `sources/links.md`
7. Åpne kilder som bekrefter mandat, status, forvalter og bruk

### Trinn 5: Skriv for analysebruk
Beskriv ressursen slik at den kan brukes senere i:
- caseanalyser
- gjenbruksvurderinger
- tidligfase og konseptvalg
- vurdering av samordningsbehov
- vurdering av hvilke operative løsninger som bør ses i sammenheng

Dette betyr at teksten må svare tydelig på:
- Hva ressursen faktisk er
- Hva den påvirker
- Når den bør brukes eller involveres
- Hvor bindende eller styrende den er
- Hva som må suppleres for å få effekt

---

## Særregler for normerende ressurser

### Forpliktelsesnivå må være eksplisitt
- Beskriv forpliktelsesnivå tydelig. Det er ikke nok å skrive at ressursen er "viktig".
- Gjør det klart om ressursen er:
  - **Obligatorisk** (må bruges/følges)
  - **Styrende** (gir tydelig retning)
  - **Anbefalt** (bør vurderes)
  - **Veiledende** (hjelper til orientering)

### Analyse- og beslutningskontekst
- Beskriv typiske analyse- og beslutningssituasjoner, ikke bare generell bruk.
- Gjør det eksplisitt hva som skjer hvis ressursen:
  - Ikke brukes
  - Brukes for sent
  - Tolkes ulikt

### Scope og gjenbruk
- Beskriv eksplisitt scope og avgrensning.
- Beskriv hvilke andre ressurser som naturlig kobles til denne.

---

## Utfyllingsregler

### Generelt
- Følg felles språkregler i `config/regler/sprakforing.md`.
- Skriv selvstendig tekst for målgruppen, ikke referat av kilder.
- Skill tydelig mellom fakta, deduksjon og usikkerhet.
- Ikke bruk `Status/Livsfase` om dokumentutkastet; feltet gjelder selve ressursen.
- Behold hele malstrukturen også i v0.x-versjoner.
- Hvis et felt ikke kan fylles godt nok ennå, skriv `Foreløpig ikke fylt ut i v0.1.`

### Forventet nivå i v1

En `v1` skal være mer enn et arbeidsutkast og skal kunne brukes direkte i analyser.

**Feltene som må være substansielt utfylt:**
- Navn, ressurs-ID, kategori, type og status
- Kort beskrivelse
- Formål/rolle eller mandat
- Kapabiliteter med korte forklaringer
- Målgruppe / hvem som skal bruke det
- Bruksområde / når det bør brukes
- Scope og avgrensning
- Relasjon til andre ressurser
- Forretningsverdi og arkitekturverdi
- Lenker og kildegrunnlag

**Analysekritiske felt som bør være fylt ut:**
- `Forpliktelsesnivå og etterlevelse`
- `Typiske analyse- og beslutningssituasjoner`
- `Hva skjer hvis ressursen ikke brukes eller tolkes ulikt`

**Anbefaling:**
- Hvis kildegrunnlaget ikke er godt nok til dette nivået, bruk heller `v0.x` enn å kalle dokumentet `v1`.
