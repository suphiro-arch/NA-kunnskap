## 1. Kort oppsummering

- Case: Gapanalyse av kapabiliteter for prioritering av videre innsats i NA-kunnskap
- Analysetillit: Middels
- Hovedfunn (1-3 setninger): Porteføljen har høy dekning på flere sentrale kapabiliteter, men modenhetstallene peker samtidig på svake områder med stor systemeffekt. De tydeligste prioriteringene er `Bruke data fra andre`, `Sammenhengende tjenester` og `Datastyring`. I tillegg finnes blinde flekker med lav dekning innen blant annet finansiering, juridisk samhandling og testdata.
- Viktigste kapabilitetsgap: Bruke data fra andre, Sammenhengende tjenester, Datastyring
- Mest relevante produkter for gjenbruk: Maskinporten, Felles datakatalog, Begrepskatalog, data.altinn.no, API-katalogen, relevante registerressurser
- Hva mangler: Tydeligere samordnet styring, sterkere semantisk forvaltning og målrettet oppbygging av ressurser i blinde flekker
- Anbefalt prioritering:
  1. Prioriter tiltak som øker evnen til å bruke data fra andre på tvers av sektorer
  2. Etabler en samordnet satsing på sammenhengende tjenester med tydelig ansvar
  3. Bygg opp datastyring og semantisk kvalitet som felles grunnmur

## 2. Formål

- Analyseformål: Teste ny designprofil og analysemal på et reelt grunnlag, og samtidig gi et oppdatert prioriteringsnotat for kapabilitetsgap.
- Beslutning analysen skal understøtte: Hvilke kapabiliteter som bør prioriteres i neste arbeidsrunder for størst mulig effekt i porteføljen.
- Avgrensning: Analysen bruker eksisterende modenhetsanalyse og ressurskoblinger i repoet. Den er ikke en full ny datainnsamling.

## 3. Input / casebeskrivelse

- Case-tittel: Gapanalyse av kapabiliteter for NA-kunnskap (test av mal)
- Kort casebeskrivelse: Vi skal prioritere videre arbeid i ressurs- og analyseporteføljen ved å kombinere modenhetsvurdering med faktisk ressursdekning per kapabilitet.
- Berørte livshendelser / tjenester / overganger: Tverrgående samhandling i offentlig sektor på tvers av livshendelser og sektorgrenser.
- Hovedutfordring i caset: Å velge riktig prioriteringsrekkefølge når både modenhet, ressursdekning og styringsbehov peker i ulike retninger.
- Kildemateriale brukt:
  - `analyser/Modenhetsanalyser/2026-05-05-modenhetsanalyse-felleslosninger-ssb.md`
  - `analyser/Modenhetsanalyser/2026-05-05-prioritering-av-kapabiliteter-basert-pa-modenhet-og-ressursdekning.md`
  - `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
  - `arkitektur/kapabiliteter/capabilities.yaml`
  - `arkitektur/prinsipper/principles.md`

## 3.1 Inputgrunnlag og analysetillit

| Vurderingspunkt | Vurdering |
|---|---|
| Inputgrunnlag | Godt for overordnet prioritering, med tydelig dokumenterte observasjoner i eksisterende analyser |
| Datagrunnlag | Middels: bygger på tidligere uttrekk og ikke ny fulltelling i denne arbeidsøkten |
| Produktgrunnlag | Middels til godt: bred dekning i koblingsfil, men ulik kvalitet i enkelte ressursbeskrivelser |
| Samlet analysetillit (høy/middels/lav) | Middels |

Viktigste usikkerheter (minst 3):
- Telling av ressursdekning er hentet fra tidligere analysepunkt og kan ha små avvik mot dagens arbeidskopi.
- Modenhetsvurderingene er overordnet og ikke kalibrert per delsektor eller tjenestekjede.
- Noen kapabiliteter med lav dekning kan være underrepresentert i mapping, ikke nødvendigvis i faktisk nasjonal praksis.

## 4. Problembilde

### 4.1 Hovedproblem

Porteføljen inneholder mange etablerte ressurser, men dette betyr ikke automatisk høy modenhet i samhandlingsevnen. Flere kapabiliteter med stor ressursberøring er fortsatt vurdert som svake. Samtidig finnes områder med lav modenhet og nesten ingen ressurskoblinger, som kan bli stående uten tydelig ansvar eller fremdrift. Uten en tydelig prioriteringslogikk risikerer vi at innsatsen fordeles for tynt og at strukturelle gap vedvarer.

### 4.2 Konsekvenser for målgrupper

- Virksomheter får tregere effekt av eksisterende fellesløsninger når dataflyt og samhandling ikke fungerer godt nok.
- Innbyggere og næringsliv opplever mindre sammenhengende tjenester selv om tekniske byggesteiner finnes.
- Produkteiere og arkitekturmiljøer får høyere kostnad i koordinering og flere lokale tilpasninger.

### 4.3 Konsekvenser for forvaltning og tjenesteutøvelse

- Prioritering blir mer reaktiv enn styrt av dokumenterte gap.
- Ressurser med høy påvirkning kan forbli flaskehalser over tid.
- Blinde flekker i styring og juridisk samhandling kan forsinke sektorovergripende tiltak.

## 5. Kapabilitetsanalyse

| Kapabilitet | Relevans (høy/middels/lav) | Hva finnes i dag | Identifisert gap | Konsekvens for caset |
|---|---|---|---|---|
| Datautveksling og integrasjon: Bruke data fra andre | Høy | Høy ressursdekning og flere etablerte delingsprodukter | Lav modenhet i praktisk utnyttelse og tverrsektoriell bruk | Stor systemeffekt ved forbedring, men også stor risiko ved passivitet |
| Sluttbrukertjenester: Sammenhengende tjenester | Høy | Mange tjenester og kanaler finnes | Svak helhet i brukerreise og samordning på tvers | Vedvarende fragmentert tjenesteopplevelse |
| Informasjonsforvaltning: Datastyring | Høy | Flere ressurser støtter metadata og datadeling | Ujevn kvalitet i styring av begreper, dataansvar og livsløp | Redusert gjenbruk og svakere beslutningsgrunnlag |
| Strategisk styring: Finansiering | Middels/høy | Svak eller ingen eksplisitt ressursdekning i kartleggingen | Finansieringsmekanismer er ikke godt nok operasjonalisert | Tiltak stopper opp eller skalerer dårlig |
| Juridisk samhandling | Høy | Svært begrenset eksplisitt ressursdekning | Manglende felles praksis for juridiske avklaringer i samhandling | Økt gjennomføringstid og høyere risiko i tiltak |

### Oppsummering av kapabilitetsgap

- Viktigste gap 1: Bruke data fra andre (lav modenhet + høy ressursberøring)
- Viktigste gap 2: Sammenhengende tjenester (lav modenhet + høy brukerpåvirkning)
- Viktigste gap 3: Datastyring (grunnmurskapabilitet med bred effekt)

## 6. Prinsippvurdering

| Prinsipp | Status (oppfylt/delvis/brutt) | Hva finnes i dag | Hvordan caset utfordrer prinsippet |
|---|---|---|---|
| Ta utgangspunkt i brukernes behov | Delvis | Mange tjenester eksisterer | Manglende sammenheng i tjenestekjeder svekker faktisk brukerverdi |
| Del og gjenbruk data | Delvis | Delingsprodukter og registre er etablert | Lav modenhet i bruk av andres data begrenser reell gjenbruk |
| Del og gjenbruk løsninger | Delvis | Fellesløsninger er bredt representert | Potensialet realiseres ikke fullt ut uten bedre styring og samordning |
| Lag digitale løsninger som støtter samhandling | Delvis | Teknisk grunnlag er tilgjengelig | Juridiske og organisatoriske gap bremser samhandling i praksis |

### Oppsummering av prinsippvurdering

Prinsippretningen er i stor grad riktig, men gjennomføringsevnen er ujevn. Gapene ligger særlig i operasjonalisering, styring og felles praksis på tvers.

## 7. Produktvurdering

### 7.0 Vurderingsrekkefølge for produktkategorier

1. Identitet og representasjon
2. Datadeling og integrasjon
3. Hendelser og meldinger
4. Dialog og brukerflate
5. Register og datagrunnlag
6. Katalog og semantikk
7. Sektorprodukter og domeneprodukter

### 7.1 Vurderte produkter fra katalogen

| Produkt (fra produktkatalogen) | Produktkategori | Relevans for caset | Klassifisering (brukes direkte/videreutvikles/ikke relevant) | Begrunnelse |
|---|---|---|---|---|
| Maskinporten | Datadeling og integrasjon | Høy | Brukes direkte | Kritisk byggestein for sikker maskin-til-maskin-delingsflyt |
| data.altinn.no | Datadeling og integrasjon | Høy | Videreutvikles | Viktig delingsflate, men effekt avhenger av bedre datastyring og samordning |
| Felles datakatalog | Katalog og semantikk | Høy | Brukes direkte | Nasjonal metadata- og oversiktsstruktur som støtter gjenbruk |
| Begrepskatalog | Katalog og semantikk | Høy | Videreutvikles | Krever sterkere felles begrepsforvaltning for større effekt |
| API-katalog | Katalog og semantikk | Middels/høy | Brukes direkte | Viktig for oppdagbarhet og gjenbruk av API-er |
| Utvalgte registerressurser | Register og datagrunnlag | Høy | Brukes direkte | Gir nødvendig datagrunnlag, men krever bedre tilgjengeliggjøring og styring |
| Samarbeidsfora med samordningsrolle | Samarbeid/styring | Middels/høy | Videreutvikles | Struktur finnes, men bør brukes mer målrettet i gjennomføringsløp |

### 7.2 Oppsummering: hva finnes, hva kan gjenbrukes, hva må videreutvikles

- Hva finnes: En bred portefølje av felleskomponenter og datagrunnlag med dokumentert relevans.
- Hva kan gjenbrukes direkte: Maskinporten, Felles datakatalog, API-katalogen og sentrale registerressurser.
- Hva må videreutvikles: Begrepsforvaltning, samordning av gjennomføring og styringsnære kapabiliteter.
- Hva er ikke relevant i dette caset: Smale domeneprodukter uten tydelig kobling til de identifiserte toppgapene.

### 7.3 Eksplisitte mangler og behov for nye/sammensatte løsninger

| Identifisert mangel | Hvorfor mangelen oppstår | Konsekvens hvis ikke løst | Forslag til ny/sammensatt løsning | Kan bygge på eksisterende produkter |
|---|---|---|---|---|
| Lav modenhet i bruk av andres data | Ujevn styring, ulik praksis og fragmentert gjennomføring | Lavere gevinst av eksisterende delingskomponenter | Etablere felles gjennomføringspakker per sektor med tydelig ansvar | Ja |
| Svak sammenheng i tjenester | Manglende koordinering mellom fag, data og kanal | Fortsatt fragmentert brukeropplevelse | Tverrsektorielle tjenestekjeder med standardisert samordning | Ja |
| Blinde flekker i finansiering og juridisk samhandling | Lite eksplisitt ressursdekning i porteføljen | Tiltak stopper i avklaringsfaser | Etablere normerende og samordnende spor for finansiering/juridikk | Delvis |

### 7.4 Sammensatte løsningsmønstre

| Løsningsmønster | Produkter som inngår | Hva mønsteret dekker | Hva som fortsatt mangler |
|---|---|---|---|
| Datadrevet samhandlingsmønster | Maskinporten + data.altinn.no + registerressurser + API-katalog + Felles datakatalog | Sikker deling, oppdagbarhet og standardisert bruk av data | Juridisk og organisatorisk gjennomføring i stor skala |
| Semantisk styringsmønster | Begrepskatalog + Felles datakatalog + relevante normerende ressurser + samordningsfora | Felles språk, bedre datakvalitet og tydeligere gjenbruk | Tydelig finansieringsmodell og forpliktende etterlevelse |

## 8. Tiltak prioritert etter effekt

### 8.0 Gap-type per tiltak

| Tiltak | Type (gjenbruk/videreutvikling/nyutvikling/avklaring) | Forventet effekt (høy/middels/lav) | Tidshorisont (kort/middels/lang) | Avhengigheter | Kobling til kapabilitet/prinsipp/produkt | Primær gap-type |
|---|---|---|---|---|---|---|
| Prioritert program for `Bruke data fra andre` i utvalgte sektorløp | Videreutvikling | Høy | Kort/middels | Sektoreiere, datatilbydere, integrasjonsmiljø | Datautveksling og integrasjon, Del og gjenbruk data, Maskinporten/data.altinn.no | Produktgap |
| Felles innsats for sammenhengende tjenester med tydelig styringsforankring | Videreutvikling/avklaring | Høy | Middels | Tverrsektoriell samordning og mandat | Sluttbrukertjenester, Ta utgangspunkt i brukernes behov, samordningsfora | Samordningsgap |
| Opptrapping av datastyring og begrepsforvaltning | Videreutvikling | Høy | Kort/middels | Fagmiljø, metadataansvarlige, produkteiere | Informasjonsforvaltning, Del og gjenbruk løsninger, Begrepskatalog/Felles datakatalog | Semantisk gap |
| Eget avklaringsspor for juridisk samhandling | Avklaring | Middels/høy | Middels | Juridiske miljøer og sektoreiere | Juridisk samhandling, samhandlingsprinsipper | Juridisk gap |
| Kartlegge og etablere finansieringsmønster for tverrgående tiltak | Avklaring/nyutvikling | Middels | Middels/lang | Virksomhetsledelse og departementale spor | Strategisk styring: Finansiering | Samordningsgap |

### Prioritert liste

1. Program for `Bruke data fra andre` - Begrunnelse: størst dokumentert systemeffekt ved kombinasjon av lav modenhet og høy ressursberøring.
2. Samordnet satsing på sammenhengende tjenester - Begrunnelse: direkte effekt for brukeropplevelse og tverrsektoriell samhandling.
3. Datastyring og begrepsforvaltning som grunnmur - Begrunnelse: høy multiplikatoreffekt for kvalitet og gjenbruk.

## 9. Strategisk vurdering

- Betydning for porteføljeprioritering: Porteføljen bør styres med tydelig kobling mellom modenhet og ressursdekning, ikke bare med tema- eller sektorlister.
- Betydning for nasjonal arkitektur/felles retning: Analysen understøtter en retning der eksisterende felleskomponenter brukes mer systematisk før nyutvikling.
- Behov for samordning mellom aktører: Høyt. Både styringsmiljø, produkteiere og juridiske miljøer må involveres i samme prioriteringsløp.

## 10. Konklusjon

Denne testanalysen bekrefter at gapanalyse av kapabiliteter er egnet som styringsverktøy når den kombinerer modenhet og ressursdekning. De viktigste prioriteringene er tydelige: styrk evnen til å bruke data fra andre, bygg sammenhengende tjenester og løft datastyring som felles grunnmur. Samtidig må blinde flekker i juridisk samhandling og finansiering løftes fra indirekte utfordring til eksplisitte tiltaksspor. Med denne prioriteringen kan repoet støtte mer målrettede beslutninger, raskere gjenbruk og høyere effekt av eksisterende ressurser.

### 10.1 Spørsmål til videre diskusjon

1. Hvilke 2-3 sektorløp bør brukes som første prioriterte pilot for `Bruke data fra andre`?
2. Hvem skal ha mandat til å prioritere på tvers når kapabilitetsgap går på tvers av sektoransvar?
3. Hvordan måles faktisk forbedring i sammenhengende tjenester over tid?
4. Hvilke minimumskrav til datastyring bør gjelde før nye delingstiltak startes?
5. Hvordan etableres et praktisk juridisk avklaringsløp som ikke stopper fremdrift?
6. Hvilke finansieringsmekanismer kan gi varig støtte til tverrgående kapabilitetsløft?
