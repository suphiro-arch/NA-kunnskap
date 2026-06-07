# Standardprompt: Rammer og virkemidler-canvas

Formål: Sikre lik, analysevennlig og beslutningsrelevant utfylling av ressursbeskrivelser for økonomiske og juridiske rammer og virkemidler (forskrifter, rundskriv, finansieringsordninger, styringsmekanismer osv.).

---

## Arbeidsgang

### Trinn 1: Fastslå ressurskategori
- Bruk `arkitektur/ressurser/styringsregler.md` til å avgjøre om ressursen hører til **økonomiske og juridiske rammer og virkemidler**.
- Hvis ressursen i praksis er en gjenbrukbar løsning, bruk ikke denne prompten. Da gjelder `config/prompts/operative-ressurs-canvas.system.md`.
- Hvis ressursen primært er en standard eller veileder, bruk `config/prompts/normerende-ressurs-canvas.system.md`.
- Hvis ressursen primært er en samhandlingsarena, bruk `config/prompts/samarbeidsforum-canvas.system.md`.

### Trinn 2: Velg mal og lagringssted
- Bruk `config/templates/okonomiske-og-juridiske-rammer-og-virkemidler-template.md`.
- Lagres i `arkitektur/ressurser/rammer-og-virkemidler/`.
- Bruk løpenummer fra `arkitektur/ressurser/produktnummerering.md` først i filnavnet.
- Bruk gjeldende filnavnmønster: `NN-Ressursnavn-vX-format.md` (f.eks. `137-Forskrift-om-IT-standarder-i-offentlig-forvaltning-v2-copilot.md`).

### Trinn 3: Les eksisterende versjon (viktig)
- Hvis ressursbeskrivelse allerede finnes: les siste versjon først.
- Hvis flere versjoner finnes: bruk høyeste versjonsnummer som primært utgangspunkt.
- Bygg videre på det som allerede fungerer, og forbedre bare der kilder, presisjon eller analysegrunnlag tilsier det.

### Trinn 4: Hent grunnlag
1. `arkitektur/ressurser/styringsregler.md`
2. `config/templates/okonomiske-og-juridiske-rammer-og-virkemidler-template.md`
3. `arkitektur/kapabiliteter/capabilities.yaml`
4. `arkitektur/prinsipper/principles.md`
5. `arkitektur/ressurser/produktnummerering.md`
6. `sources/links.md`
7. Åpne kilder som bekrefter hjemmel, forvalter, virkeområde, binding og praktisk bruk
8. Hvis du bruker nye stabile og relevante eksterne URL-er som mangler i `sources/links.md`, skal `sources/links.md` normalt oppdateres i samme kjøring

### Trinn 5: Skriv for analysebruk
Beskriv ressursen slik at den kan brukes senere i:
- caseanalyser
- styrings- og prioriteringsvurderinger
- vurdering av handlingsrom og etterlevelsesrisiko
- vurdering av hvilke operative tiltak som er mulige eller begrensede
- vurdering av samspill mellom juridiske og økonomiske virkemidler

Dette betyr at teksten må svare tydelig på:
- Hva ressursen faktisk er
- Hvor bindende den er og for hvem
- Hvordan den påvirker prioritering, styring og gjennomføring
- Når den må brukes i beslutningsløpet
- Hva som må suppleres for å få praktisk effekt

### Trinn 6: Merk hva som er sikkert og hva som er tolket
- Skill aktivt mellom:
  - **Fakta**: bekreftet i åpne kilder eller tydelige repo-kilder
  - **Deduksjon**: rimelig tolkning basert på kjent kontekst
  - **Usikkerhet**: forhold som ikke kan bekreftes godt nok
- Hvis forpliktelsesnivå, virkeområde eller etterlevelsesmekanisme ikke kan bekreftes tydelig, skriv det eksplisitt.
- Ikke gi inntrykk av sterkere juridisk binding eller økonomisk effekt enn kildene underbygger.

---

## Særregler for økonomiske og juridiske rammer og virkemidler

### Forpliktelsesnivå må være eksplisitt
- Beskriv tydelig om ressursen er:
  - **Juridisk bindende**
  - **Styrende**
  - **Anbefalt**
  - **Veiledende**
- Gjør det eksplisitt hva som er krav, hva som er forventning, og hva som er støtteinformasjon.

### Virkemiddelmekanisme må beskrives konkret
- Forklar hvordan ressursen påvirker praksis:
  - gjennom rettslig krav
  - gjennom økonomisk insentiv
  - gjennom styringskrav i portefølje eller budsjett
  - gjennom samspill med andre virkemidler

### Juridisk og økonomisk effekt skal skilles
- Ikke bland juridisk binding og økonomisk virkning i samme påstand uten å forklare sammenhengen.
- Beskriv tydelig handlingsrommet: hva virksomheter må gjøre, bør gjøre og kan velge.

### Analysekontekst og avviksrisiko
- Beskriv typiske beslutningssituasjoner der ressursen må inn tidlig.
- Beskriv konsekvenser ved manglende bruk, for sen bruk eller ulik tolkning.

### Kapabiliteter skal være rene nok for videre bruk
- Bruk bare kanoniske kapabilitetsnavn i selve kapabilitetslisten.
- Legg forklaring, begrunnelse og nyanser i egen tekst rundt listen, ikke inne i navnelabelen.
- Unngå formuleringer som gjør kapabilitetsseksjonen vanskelig å gjenbruke i web, filtrering eller senere analyser.

---

## Utfyllingsregler

### Generelt
- Følg felles språkregler i `config/regler/sprakforing.md`.
- Følg designprofilen i `config/prompts/designprofil-rapporter-og-presentasjoner.system.md` når innholdet brukes som rapport- eller presentasjonsgrunnlag.
- Skriv selvstendig tekst for målgruppen, ikke referat av kilder.
- Skill tydelig mellom fakta, deduksjon og usikkerhet.
- Ikke bruk `Status/Livsfase` om dokumentutkastet; feltet gjelder selve ressursen.
- Behold hele malstrukturen også i v0.x-versjoner.
- Hvis et felt ikke kan fylles godt nok ennå, skriv `Foreløpig ikke fylt ut i v0.1.`
- Hvis nye eksterne kilder tas i bruk fordi `sources/links.md` ikke var tilstrekkelig, skal disse normalt legges inn i `sources/links.md` når de er stabile og relevante for senere arbeid

### Forventet nivå i v1

En `v1` skal være mer enn et arbeidsutkast og skal kunne brukes direkte i analyser.

**Feltene som må være substansielt utfylt:**
- Navn, ressurs-ID, kategori, type og status
- Kort beskrivelse
- Formål og virkemiddelrolle
- Forpliktelsesnivå og etterlevelse
- Virkemiddelmekanisme
- Målgruppe og berørte aktører
- Bruksområde
- Scope og avgrensning
- Relasjon til andre ressurser
- Forretningsverdi og arkitekturverdi
- Lenker og kildegrunnlag

**Analysekritiske felt som bør være fylt ut:**
- `Typiske analyse- og beslutningssituasjoner`
- `Økonomiske konsekvenser og insentiver`
- `Juridiske konsekvenser og handlingsrom`
- `Konsekvens ved manglende bruk eller avvik`

**Anbefaling:**
- Hvis kildegrunnlaget ikke er godt nok til dette nivået, bruk heller `v0.x` enn å kalle dokumentet `v1`.

### Sjekk før du bruker `v1`
- Er virkemiddelets rolle, binding og handlingsrom tydelig nok til direkte analysebruk?
- Er viktige påstander forankret i åpne kilder eller tydelig merket som deduksjon/usikkerhet?
- Er juridisk effekt, økonomisk effekt og styringsvirkning skilt tydelig nok?
- Er behovet for supplement fra standarder, veiledning eller operative løsninger konkret nok beskrevet?
- Er kapabilitetsnavnene rene og kanoniske, uten forklaringer bygget inn i labelen?
