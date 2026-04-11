# Standardprompt: Samarbeidsforum-canvas

Formål: Sikre lik, analysevennlig og beslutningsrelevant utfylling av ressursbeskrivelser for samarbeidsfora (råd, nettverk, samordningsarenaer, fora, osv.).

---

## Arbeidsgang

### Trinn 1: Fastslå ressurskategori
- Bruk `arkitektur/ressurser/styringsregler.md` til å avgjøre hvis ressursen er et **samarbeidsforum**.
- Hvis ressursen i praksis er en operativ løsning eller tjeneste, bruk ikke denne prompten. Da gjelder `config/prompts/operative-ressurs-canvas.system.md`.
- Hvis ressursen er en normering eller standard, bruk `config/prompts/normerende-ressurs-canvas.system.md`.

### Trinn 2: Velg mal og lagringssted
- Bruk `config/templates/samarbeidsforum-template.md`.
- Lagres i `arkitektur/ressurser/samarbeidsfora/`.
- Bruk løpenummer fra `arkitektur/ressurser/produktnummerering.md` først i filnavnet.
- Bruk gjeldende filnavnmønster: `NN-Forumsnavn-vX-format.md` (f.eks. `88-Arkitektur-og-standardiseringsradet-v0-codex.md`).

### Trinn 3: Les eksisterende versjon (viktig)
- Hvis ressursbeskrivelse allerede finnes: les siste versjon først.
- Hvis flere versjoner finnes: bruk høyeste versjonsnummer som primært utgangspunkt.
- Bygg videre på det som allerede fungerer, og forbedre bare der kilder, presisjon eller analysegrunnlag tilsier det.

### Trinn 4: Hent grunnlag
1. `arkitektur/ressurser/styringsregler.md`
2. `config/templates/samarbeidsforum-template.md`
3. `arkitektur/kapabiliteter/capabilities.yaml`
4. `arkitektur/prinsipper/principles.md`
5. `arkitektur/ressurser/produktnummerering.md`
6. `sources/links.md`
7. Åpne kilder som bekrefter mandat, deltakere, forvalter og scope

### Trinn 5: Skriv for analysebruk
Beskriv forumet slik at det kan brukes senere i:
- caseanalyser
- vurdering av samordningsbehov
- vurdering av når det må involveres
- vurdering av hvilke ressurser forumet påvirker
- tidligfase og prioriteringsprosesser

Dette betyr at teksten må svare tydelig på:
- Hva forumet faktisk handler om
- Hvem som sitter og hvilken rolle de har
- Hvem som beslutter hva
- Hvilke ressurser forumet påvirker
- Når forumet bør involveres i utviklingsløp
- Hva slags saker og leveranser forumet typisk utløser

### Trinn 6: Merk hva som er sikkert og hva som er tolket
- Skill aktivt mellom:
  - **Fakta**: bekreftet i åpne kilder eller tydelige repo-kilder
  - **Deduksjon**: rimelig tolkning basert på kjent kontekst
  - **Usikkerhet**: forhold som ikke kan bekreftes godt nok
- Hvis mandat, beslutningsmyndighet, medlemskap eller innmeldingsløp ikke kan bekreftes i åpne kilder, skriv det eksplisitt.
- Ikke presenter sannsynlige antakelser som om de er bekreftede styringsforhold.

---

## Særregler for samarbeidsfora

### Beslutningsmyndighet må være eksplisitt
- Beskriv beslutningsmyndighet tydelig. Ikke la det være uklart om forumet:
  - **Beslutter** (gir bindende retning)
  - **Anbefaler** (gir innspill til andre som beslutter)
  - **Fasiliterer** (legger til rette for dialog)
  - **Informerer** (deler kunnskap og status)
- Hvis åpne kilder ikke er tydelige nok, si at beslutningsmyndighet er uavklart eller delvis uklar.

### Grensesnitt mot andre fora
- Beskriv **eksplisitt** hvordan dette forumet skiller seg fra og utfyller andre fora med lignende tematikk.
- Bruk tabell: `Forum | Rolle-fordeling | Når dette forumet, når det andre | Typisk samspill`
- Unngå generelle formuleringer som «ses i sammenheng med». Beskriv konkret hva som går hit og hva som går dit.
- Ta stilling til hva som skjer i skjæringsflaten mellom to fora med overlappende mandat.

### Saksinnmelding må være praktisk beskrevet
- Beskriv hvem som kan melde inn saker og gjennom hvilken kanal.
- Beskriv hvilken type saker forumet tar imot og hvilke det sender videre.
- Beskriv hva som bør følge med en innmelding, og hva som skjer etterpå.
- Hvis inngangen ikke er kjent fra åpne kilder, skriv hva som er sannsynlig basert på type forum og sekretariatets eier.
- Marker tydelig når dette er deduksjon og ikke bekreftet praksis.

### Påvirkning på ressurser
- Beskriv **eksplisitt** hvilke ressurser forumet faktisk påvirker, og **på hvilken måte**.
- Beskriv også hvilke andre fora forumet må samordne med.

### Når involveringspunkt
- Beskriv når forumet bør involveres i analyse- og utviklingsløp.
- Beskriv typiske saker, anbefalinger eller leveranser forumet utløser.

### Representasjon og deltakelse
- Beskriv hvem som deltar og hvilken rolle de har.
- Beskriv om representasjonen er stabil eller endrer seg, og hvorfor.

### Kapabiliteter skal være rene nok for videre bruk
- Bruk bare kanoniske kapabilitetsnavn i selve kapabilitetslisten.
- Legg forklaring, begrunnelse og nyanser i egen tekst rundt listen, ikke inne i navnelabelen.
- Unngå formuleringer som gjør kapabilitetsseksjonen vanskelig å gjenbruke i web, filtrering eller senere analyser.

---

## Utfyllingsregler

### Generelt
- Følg felles språkregler i `config/regler/sprakforing.md`.
- Skriv selvstendig tekst for målgruppen, ikke referat av kilder.
- Skill tydelig mellom fakta, deduksjon og usikkerhet.
- Ikke bruk `Status/Livsfase` om dokumentutkastet; feltet gjelder selve forumet.
- Behold hele malstrukturen også i v0.x-versjoner.
- Hvis et felt ikke kan fylles godt nok ennå, skriv `Foreløpig ikke fylt ut i v0.1.`

### Forventet nivå i v1

En `v1` skal være mer enn et arbeidsutkast og skal kunne brukes direkte i analyser.

**Feltene som må være substansielt utfylt:**
- Navn, ressurs-ID, kategori, type og status
- Kort beskrivelse
- Formål/rolle eller mandat
- Deltakere / hvem som er med
- Bruksområde / når det bør involveres
- Scope og avgrensning
- Grensesnitt mot andre fora
- Relasjon til andre ressurser og fora
- Forretningsverdi og arkitekturverdi
- Lenker og kildegrunnlag

**Analysekritiske felt som bør være fylt ut:**
- `Beslutningsmyndighet og forpliktelse`
- `Hvilke ressurser forumet påvirker`
- `Når forumet bør involveres`
- `Typiske saker og leveranser`
- `Grensesnitt mot andre fora`
- `Slik melder du inn en sak`

**Anbefaling:**
- Hvis kildegrunnlaget ikke er godt nok til dette nivået, bruk heller `v0.x` enn å kalle dokumentet `v1`.

### Sjekk før du bruker `v1`
- Er mandat, rolle og beslutningsmyndighet tydelige nok til at forumet kan brukes som analysegrunnlag?
- Er påvirkning på ressurser, involveringstidspunkt og typiske saker beskrevet konkret nok?
- Er viktige påstander forankret i åpne kilder eller tydelig merket som deduksjon/usikkerhet?
- Er grensesnittet mot andre fora avklart uten generelle fraser eller skjult overlapp?
- Er kapabilitetsnavnene rene og kanoniske, uten forklaringer bygget inn i labelen?
