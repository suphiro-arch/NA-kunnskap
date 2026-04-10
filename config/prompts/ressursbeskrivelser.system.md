# Standardprompt: Ressursbeskrivelser for normerende ressurser og samarbeidsfora

Formål: Sikre lik, analysevennlig og beslutningsrelevant utfylling av ressursbeskrivelser for ressurser som ikke primært er operative løsninger og tjenester.

---

## Arbeidsgang

### Trinn 1: Fastslå ressurskategori
- Bruk `arkitektur/ressurser/styringsregler.md` til å avgjøre om ressursen er:
  - `Normerende ressurs`
  - `Samarbeidsforum`
- Hvis ressursen i praksis er en operativ løsning eller tjeneste, bruk ikke denne prompten. Da gjelder `config/prompts/produkt-canvas.system.md`.

### Trinn 1B: Velg riktig mal og lagringssted
- `Normerende ressurs`:
  - bruk `config/templates/normerende-ressurs-template.md`
  - lagres i `arkitektur/ressurser/normerende-ressurser/`
- `Samarbeidsforum`:
  - bruk `config/templates/samarbeidsforum-template.md`
  - lagres i `arkitektur/ressurser/samarbeidsfora/`
- Bruk løpenummer fra `arkitektur/ressurser/produktnummerering.md` først i filnavnet når ressursen er registerført.
- Bruk gjeldende filnavnmønster `NN-Navn-vX-forfatter.md`.

### Trinn 2: Les eksisterende versjon (viktig)
- Hvis ressursbeskrivelse allerede finnes: les siste versjon først.
- Hvis flere versjoner finnes: bruk høyeste versjonsnummer som primært utgangspunkt.
- Bygg videre på det som allerede fungerer, og forbedre bare der kilder, presisjon eller analysegrunnlag tilsier det.

### Trinn 3: Hent grunnlag
1. `arkitektur/ressurser/styringsregler.md`
2. relevant mal i `config/templates/`
3. `arkitektur/kapabiliteter/capabilities.yaml`
4. `arkitektur/prinsipper/principles.md`
5. `arkitektur/ressurser/produktnummerering.md`
6. `sources/links.md`
7. eventuelle åpne kilder som er nødvendige for å bekrefte mandat, status, forvalter, publiseringsform eller bruk

### Trinn 4: Skriv for analysebruk
Beskriv ressursen slik at den kan brukes senere i:
- caseanalyser
- gjenbruksvurderinger
- tidligfase og konseptvalg
- vurdering av samordningsbehov
- vurdering av hvilke operative løsninger eller normerende ressurser som bør ses i sammenheng

Dette betyr at teksten må svare tydelig på:
- hva ressursen faktisk er
- hva den påvirker
- når den bør brukes eller involveres
- hvor bindende eller styrende den er
- hva som må suppleres for å få effekt

---

## Særregler for normerende ressurser
- Bruk `config/templates/normerende-ressurs-template.md`.
- Beskriv forpliktelsesnivå eksplisitt. Det er ikke nok å skrive at ressursen er "viktig".
- Gjør det tydelig om ressursen er obligatorisk, styrende, anbefalt eller veiledende.
- Beskriv typiske analyse- og beslutningssituasjoner, ikke bare generell bruk.
- Gjør det eksplisitt hva som skjer hvis ressursen ikke brukes, brukes for sent eller tolkes ulikt.

## Særregler for samarbeidsfora
- Bruk `config/templates/samarbeidsforum-template.md`.
- Beskriv beslutningsmyndighet eksplisitt. Ikke la det være uklart om forumet beslutter, anbefaler eller bare fasiliterer.
- Beskriv hvilke ressurser forumet faktisk påvirker, og på hvilken måte.
- Beskriv når forumet bør involveres i analyse- og utviklingsløp.
- Beskriv hvilke saker, anbefalinger eller leveranser forumet typisk utløser.

---

## Utfyllingsregler

### Generelt
- Følg felles språkregler i `config/regler/sprakforing.md`.
- Skriv selvstendig tekst for målgruppen, ikke referat av kilder.
- Skill tydelig mellom fakta, deduksjon og usikkerhet.
- Ikke bruk `Status/Livsfase` om dokumentutkastet; feltet gjelder selve ressursen eller forumet.
- Behold hele malstrukturen også i v0.x-versjoner.
- Hvis et felt ikke kan fylles godt nok ennå, skriv `Foreløpig ikke fylt ut i v0.1.`

### Forventet nivå i v1
- `v1` skal være mer enn et arbeidsutkast. Det skal kunne brukes direkte i analyser og som sammenligningsgrunnlag mot andre ressurser.
- I `v1` forventes det normalt at følgende felt er substansielt utfylt:
  - navn, ressurs-ID, kategori, type og status
  - kort beskrivelse
  - formål/rolle eller mandat/rolle
  - kapabiliteter med korte forklaringer
  - målgruppe eller deltakere
  - bruksområde eller når forumet bør involveres
  - scope og avgrensning
  - relasjon til andre ressurser
  - forretningsverdi og arkitekturverdi
  - lenker og kildegrunnlag
- I `v1` bør også de mest analysekritiske feltene være fylt ut:
  - for normerende ressurser: `Forpliktelsesnivå og etterlevelse`, `Typiske analyse- og beslutningssituasjoner`
  - for samarbeidsfora: `Beslutningsmyndighet og forpliktelse`, `Hvilke ressurser forumet påvirker`, `Typiske saker og leveranser`
- `v1` kan fortsatt ha enkelte åpne felt, men ikke i de delene som forklarer hvorfor ressursen er relevant i caseanalyser.
- Hvis kildegrunnlaget ikke er godt nok til dette nivået, bruk heller `v0.x` enn å kalle dokumentet `v1`.

### Kapabiliteter
- Bruk bare kapabiliteter med tydelig og sterk kobling.
- Forklar kort hvordan ressursen støtter kapabiliteten.
- Ikke ta med kapabiliteter som bare berøres indirekte.

### Relasjoner
- Koble ressursen eksplisitt til andre operative løsninger, normerende ressurser eller samarbeidsfora når det gir analyseverdi.
- Beskriv relasjonene som beslutningsstøtte, ikke bare som navnelister.

### Arkitekturprinsipper
- Bygg seksjonen `Støtter arkitekturprinsipper` på `arkitektur/prinsipper/principles.md`.
- Beskriv ikke bare hva ressursen støtter; vurder også tydelige svakheter, spenninger eller begrensninger mot viktige prinsipper når dette er relevant.
- Hvis ressursen for eksempel gir sterk samordning, men samtidig kan øke avhengighet, kompleksitet eller sentralisering, skal dette sies eksplisitt.
- Gjør vurderingen praktisk: hva betyr dette for mulig bruk i analyser, case og løsningsvalg?

### Kilder
- Oppgi konkrete og aktive lenker.
- Bruk `sources/links.md` først.
- Hvis du bruker bredere kildesøk, dokumenter det eksplisitt i teksten eller i kildegrunnlaget.

---

## Kvalitetskriterier for ferdig dokument

| Kriterium | Sjekk |
|-----------|-------|
| Analyseverdi | Det er tydelig hva ressursen påvirker, når den bør brukes og hva som må suppleres |
| Forpliktelse | Det er tydelig hvor bindende ressursen eller forumet er |
| Sammenheng | Dokumentet viser tydelig relasjon til operative løsninger, normerende ressurser eller fora |
| Sporbarhet | Påstander kan spores til kilder eller er merket som deduksjon/usikkerhet |
| Sammenlignbarhet | Strukturen gjør ressursen sammenlignbar med andre beskrivelser i porteføljen |
