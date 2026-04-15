# 11. Kortversjon for ledelse

- Case: Modernisert rapportering kommune-stat
- Analysetillit: Middels
- Hovedfunn (1-3 setninger): Caset kan realiseres med et sammensatt mønster av eksisterende produkter, der spor A+B (hendelse + API-oppslag) er målbildet og spor C er kontrollert overgang. De største gapene ligger i semantikk, juridisk avklaring og samordning mellom kommune, leverandør og statlig mottaker, ikke i mangel på tekniske komponenter alene.
- Viktigste kapabilitetsgap: Informasjonsarkitektur og datastyring på tvers, samt samordnet styring av overgang fra filbasert innsending til API-basert deling.
- Mest relevante produkter for gjenbruk: DIGDIR-010 Altinn Events, DIGDIR-002 Maskinporten, DIGDIR-004 Altinn Autorisasjon, DIGDIR-008 Altinn Formidling, KS-001 FIKS-plattformen, KS-002 Fiks melding, DIGDIR-011/012/013 katalogressurser.
- Hva mangler: Felles nasjonal hendelses- og begrepsmodell for rapporteringshendelser, tydelig kriteriesett for spor C, og felles opplegg for kvittering/avvik tilbake til kilden.
- Anbefalt prioritering:
  1. Etabler felles semantisk og juridisk ramme for spor A+B og spor C.
  2. Pilotér spor A+B med tydelig avviksflyt mot kildesystem.
  3. Definer styrt utfasing av spor C per tjenesteområde.

## 1. Formål

- Analyseformål: Vurdere hvordan caset "Modernisert rapportering kommune-stat" kan realiseres med gjenbruk av eksisterende nasjonale og kommunale ressurser.
- Beslutning analysen skal understøtte: Prioritering av løsningsmønster (spor A+B som mål, spor C som overgang) og hvilke tiltak som må settes først.
- Avgrensning: Analysen dekker arkitektur, kapabiliteter, prinsipper, produkter og styringsbehov. Den går ikke inn i detaljert løsningsdesign per domene.

## 2. Input / casebeskrivelse

- Case-tittel: Modernisert rapportering kommune-stat
- Kort casebeskrivelse: Caset beskriver overgang fra manuelle uttrekk og periodisk rapportering til løpende datadeling mellom kommunalt fagsystem og statlig mottaker. Hovedløpet er hendelsespublisering (spor A) og autorisert API-oppslag (spor B), med automatisert innsending (spor C) som overgang der API-beredskap mangler.
- Berørte livshendelser / tjenester / overganger: Løpende rapportering i kommunale tjenesteområder med behov for statistikk, analyse og kontroll hos statlige mottakere.
- Hovedutfordring i caset: Få til skalerbar og trygg overgang fra fil- og periodedrevet rapportering til hendelsesdrevet og API-basert deling uten å øke administrativ byrde.
- Kildemateriale brukt: Inndata fra bruker, kapabilitetsmodell, prinsipper, produktregister og spisset utvalg operative produkter samt normerende ressurser og samarbeidsforum.

## 2.1 Inputgrunnlag og analysetillit

| Vurderingspunkt | Vurdering |
|---|---|
| Inputgrunnlag | Godt beskrevet case med mål, aktører, forutsetninger og hoved-/alternativløp. |
| Datagrunnlag | Middels. Caset beskriver retning godt, men har begrenset konkretisering av volum, SLA og sektorvise forskjeller. |
| Produktgrunnlag | Middels til høy. De fleste sentrale produkter har fyldige beskrivelser; noen normerende ressurser er fortsatt tynne i v0.1. |
| Samlet analysetillit (høy/middels/lav) | Middels |

Viktigste usikkerheter (minst 3):
- Statlig mottaksmodenhet for API-basert uthenting varierer og er ikke konkretisert per mottaker.
- Semantisk harmonisering av hendelser, indikatorer og kvalitetsregler er ikke avklart i caset.
- Kriterier for når spor C er akseptabelt, og når det må fases ut, er ikke definert.
- Juridisk avgrensning av formål, hjemmel og ansvar i avviksløp er ikke tilstrekkelig konkret.

### 2.2 Avklaring: ett case eller flere

- Er dette ett case eller flere separate case: Ett hovedcase.
- Begrunnelse for vurderingen: Teksten beskriver samme mål og samme kjerneflyt med ett målbildeløp (A+B) og ett overgangsløp (C).
- Skal analysen splittes: Nei.
- Hvis ja, navngi delcasene: Ikke aktuelt.

## 3. Målgruppe og styringsnivå

- Primær målgruppe: Arkitektur- og digitaliseringsmiljø i kommune, stat og fellesforvaltning.
- Sekundær målgruppe: Leverandørmiljøer og styringsfora som skal prioritere innføring.
- Styringsnivå (nasjonalt / sektor / virksomhet): Nasjonalt og sektor, med virksomhetsnær gjennomføring.
- Viktig avgrensning for tiltak: Tiltak må støtte både rask overgang og langsiktig standardisering uten permanent dobbeltspor.

## 4. Problembilde

### 4.1 Hovedproblem

Dagens rapporteringsmønster er preget av manuelle uttrekk, periodiske toppbelastninger og varierende semantikk mellom aktører. Caset peker på et tydelig målbilde med hendelsesdrevet notifikasjon og API-oppslag, men gjennomføringen krever samordnet utvikling av teknologi, semantikk, juss og styring. Uten en styrt overgang risikerer man varig parallell drift av spor A+B og spor C. Det vil redusere gevinst i datakvalitet og administrativ forenkling.

### 4.2 Konsekvenser for målgrupper

- Kommuner risikerer dobbeltarbeid dersom overgangsløp blir varig i stedet for midlertidig.
- Statlige mottakere får lavere gevinst hvis API-oppslag ikke standardiseres på tvers av tjenester.
- Leverandører får høyere kompleksitet hvis krav til hendelser, API og kvittering ikke harmoniseres.

### 4.3 Konsekvenser for forvaltning og tjenesteutøvelse

- Datakvalitet forblir ujevn hvis validering og avvik ikke kobles tett til kildesystem.
- Personvernrisiko øker dersom filer fortsatt brukes bredt der notifikasjon + oppslag kunne dekket behovet.
- Gevinstuttak forsinkes dersom samordning mellom nivåene ikke er forpliktende.

## 5. Kapabilitetsanalyse

| Kapabilitet | Relevans (høy/middels/lav) | Hva finnes i dag | Identifisert gap | Konsekvens for caset |
|---|---|---|---|---|
| Hendelsesdrevet | Høy | Altinn Events og arkitektur for hendelser gir mønster og plattform. | Ulik hendelsesmodell mellom domener. | Ulik kvalitet og lav gjenbruk på tvers. |
| Dele data med andre | Høy | API-baserte og meldingsbaserte kanaler finnes. | Ulik modenhet i kommunale kildesystemer. | Ujevn gjennomføring og forsinket innføring. |
| Bruke data fra andre | Høy | Maskinporten + autorisasjon muliggjør oppslag. | Manglende standard for oppslag og kvittering. | Økt integrasjonskostnad per mottaker. |
| Tilgangskontroll / tilgangsstyring | Høy | Altinn Autorisasjon og policybasert tilgang finnes. | Manglende felles policyprofil for rapporteringsløp. | Ulik praksis og høy juridisk risiko. |
| Informasjonsarkitektur | Høy | Begrepskatalog, API-katalog og datakatalog finnes. | Begreper/hendelser ikke harmonisert nok. | Feiltolkning og svak datakvalitet. |
| Datastyring | Middels | Veiledere og kvalitetsprinsipper finnes. | Utydelig ansvar for avvik tilbake til kilden. | Vedvarende feil og lav tillit til data. |
| Organisatorisk samhandling / samordning | Høy | Skate og etablerte samarbeidsstrukturer finnes. | Ikke tydelig nok beslutnings- og prioriteringsløp. | Fragmentert innføring mellom aktører. |
| Juridisk samhandling | Høy | Veiledere for digitaliseringsvennlig regelverk finnes. | Formåls- og hjemmelsavklaringer ikke operasjonalisert. | Risiko for stopp i utrulling og ulik tolkning. |

### Oppsummering av kapabilitetsgap

- Viktigste gap 1: Semantisk gap i hendelses- og begrepsmodell.
- Viktigste gap 2: Juridisk gap i felles operasjonalisering av hjemmel, formål og avviksløp.
- Viktigste gap 3: Samordningsgap i overgangsstyring fra spor C til spor A+B.

## 6. Prinsippvurdering

| Prinsipp | Status (oppfylt/delvis/brutt) | Hva finnes i dag | Hvordan caset utfordrer prinsippet |
|---|---|---|---|
| P2 Ta arkitekturbeslutninger på rett nivå | Delvis | Nasjonale felleskomponenter og samordningsarenaer finnes. | Beslutninger om overgang/målbilde kan bli for lokale og usammenhengende. |
| P3 Bidra til digitaliseringsvennlige regelverk | Delvis | Veiledning og sjekklister finnes. | Hjemmel- og formålsavklaring er ikke konkretisert i gjennomføringsmodellen. |
| P4 Del og gjenbruk data | Delvis | Hendelser, API-oppslag og katalogressurser er etablert. | Manglende semantikk svekker faktisk gjenbruk. |
| P5 Del og gjenbruk løsninger | Oppfylt/delvis | Både Digdir- og KS-løsninger kan kombineres. | Risiko for permanent dobbeltspor hvis overgang ikke styres stramt. |
| P6 Lag digitale løsninger som støtter samhandling | Delvis | Produkter for samhandling er tilgjengelige. | Avhengigheter mellom kommune, leverandør og stat er ikke tilstrekkelig avklart. |
| P7 Sørg for tillit til oppgaveløsningen | Delvis | Autentisering, autorisasjon og sporbarhet finnes i komponenter. | Felles praksis for kvittering, avvik og revisjon mangler. |

### Oppsummering av prinsippvurdering

Caset er godt i tråd med prinsippretningen, men trenger tydeligere styring av semantikk, juridisk avklaring og overgangslogikk for å unngå at prinsippene bare blir delvis oppfylt i praksis.

## 7. Produktvurdering

### 7.0 Vurderingsrekkefølge for produktkategorier

1. Identitet og representasjon: DIGDIR-002, DIGDIR-004 vurdert som kjerne.
2. Datadeling og integrasjon: DIGDIR-008, KS-001, KS-002 vurdert for overgang og innføring.
3. Hendelser og meldinger: DIGDIR-010 vurdert som kjerne for spor A.
4. Dialog og brukerflate: vurdert som mindre relevant i dette caset fordi flyten er system-til-system.
5. Register og datagrunnlag: FLERE-001 vurdert som referansemønster for samordnet rapportering.
6. Katalog og semantikk: DIGDIR-011/012/013 vurdert som nødvendig støtte for standardisering.
7. Sektorprodukter og domeneprodukter: vurdert som kontekstavhengig og derfor ikke prioritert i denne tverrgående analysen.

### 7.1 Vurderte produkter fra katalogen

| Produkt (fra produktkatalogen) | Produktkategori | Relevans for caset | Klassifisering (brukes direkte/videreutvikles/ikke relevant) | Begrunnelse |
|---|---|---|---|---|
| DIGDIR-010 Altinn Events | Hendelser og meldinger | Høy | Brukes direkte | Egnet for notifikasjon i spor A med publisering/abonnement og asynkron levering. Grunnlag: full produktbeskrivelse. |
| DIGDIR-002 Maskinporten | Identitet og representasjon | Høy | Brukes direkte | Standard for sikker maskin-til-maskin autentisering ved API-oppslag i spor B. Grunnlag: full produktbeskrivelse. |
| DIGDIR-004 Altinn Autorisasjon | Identitet og representasjon | Høy | Brukes direkte | Policybasert tilgangsstyring og representasjon støtter rettighetsstyrt datahenting. Grunnlag: full produktbeskrivelse. |
| DIGDIR-008 Altinn Formidling | Datadeling og integrasjon | Høy | Brukes direkte | Dekker spor C for robust fil-/payloadformidling der API ikke er klart. Grunnlag: full produktbeskrivelse. |
| KS-001 FIKS-plattformen | Datadeling og integrasjon | Middels | Videreutvikles | Relevant som kommunalt innføringslag, men må avgrenses tydelig mot nasjonalt målbilde. Grunnlag: full produktbeskrivelse. |
| KS-002 Fiks melding | Hendelser og meldinger | Middels | Videreutvikles | Relevant i overgang for meldingsløp, men bør styres for å unngå varig parallellarkitektur. Grunnlag: full produktbeskrivelse. |
| DIGDIR-011 Felles datakatalog | Katalog og semantikk | Middels | Brukes direkte | Gir synlighet av datasett/modeller/API og styrker gjenbruk. Grunnlag: full produktbeskrivelse. |
| DIGDIR-012 Begrepskatalog | Katalog og semantikk | Høy | Brukes direkte | Nødvendig for felles begrepsforståelse i hendelser, indikatorer og kvittering. Grunnlag: full produktbeskrivelse. |
| DIGDIR-013 API-katalog | Katalog og semantikk | Middels | Brukes direkte | Understøtter oppdagelse og standardisering av API-kontrakter. Grunnlag: full produktbeskrivelse. |
| FLERE-001 A-ordningen | Register og datagrunnlag | Middels | Ikke relevant (direkte) | Ikke en direkte komponent her, men et sterkt referansemønster for samordnet rapportering. Grunnlag: full produktbeskrivelse. |
| DIGDIR-034 Referansearkitektur eOppslag | Normerende ressurs | Middels | Brukes direkte | Gir mønster for forespørsel-svar i spor B, men er normerende støtte og ikke operativ komponent. Grunnlag: tynn v0.1-beskrivelse. |
| DIGDIR-038 Nasjonal verktøykasse for deling av data | Normerende ressurs | Middels | Brukes direkte | Veiledningsstøtte for etablering av datadeling og ansvar. Grunnlag: tynn v0.1-beskrivelse. |
| DIGDIR-047 Digitaliseringsvennlig regelverk | Normerende ressurs | Høy | Brukes direkte | Nødvendig for å avklare juridiske barrierer i overgang fra fil til API. Grunnlag: moderat produktbeskrivelse. |
| DIGDIR-042 Skate | Samarbeidsforum | Middels | Brukes direkte | Relevans for tverrsektoriell samordning og forankring av felles retning. Grunnlag: full forumbeskrivelse. |

### 7.2 Oppsummering: hva finnes, hva kan gjenbrukes, hva må videreutvikles

- Hva finnes: Et komplett sett av byggesteiner for hendelser, autentisering, autorisasjon, meldingsformidling og katalogstøtte.
- Hva kan gjenbrukes direkte: Altinn Events, Maskinporten, Altinn Autorisasjon, Altinn Formidling, Felles datakatalog, Begrepskatalog, API-katalog.
- Hva må videreutvikles: Felles semantisk profil, kvitterings-/avviksmønster og styrt overgang mellom spor C og A+B.
- Hva er ikke relevant i dette caset: Dialognære produkter som primærmønster, og A-ordningen som direkte komponent.

### 7.3 Eksplisitte mangler og behov for nye/sammensatte løsninger

| Identifisert mangel | Hvorfor mangelen oppstår | Konsekvens hvis ikke løst | Forslag til ny/sammensatt løsning | Kan bygge på eksisterende produkter |
|---|---|---|---|---|
| Manglende felles hendelses- og begrepsmodell | Ulike domener og leverandører modellerer ulikt | Lav sammenlignbarhet og økt feilrate | Felles semantisk profil for hendelser, indikatorer og status | Ja, DIGDIR-012 + DIGDIR-011 + DIGDIR-013 |
| Uklart kvitterings- og avviksregime | Caset beskriver behov, men ikke standard | Svak sporbarhet og treg feilretting | Standardisert mønster for kvittering, avvik og tilbakeføring til kilden | Ja, DIGDIR-010 + DIGDIR-008 + DIGDIR-034 |
| Ustyrt overgang fra spor C til spor A+B | Ulik API-modenhet og lokal variasjon | Permanent dobbeltspor og høy kostnad | Nasjonalt kriteriesett og utfasingsplan for spor C per område | Ja, DIGDIR-038 + DIGDIR-042 + KS-001/002 |
| Juridisk operasjonalisering ikke nok konkret | Hjemmel/formål oversettes ulikt i praksis | Ulik tilgangspraksis og stopp i utrulling | Felles juridisk kontrollpunkt i innføringsløpet | Ja, DIGDIR-047 + DIGDIR-004 |

### 7.4 Sammensatte løsningsmønstre

| Løsningsmønster | Produkter som inngår | Hva mønsteret dekker | Hva som fortsatt mangler |
|---|---|---|---|
| Mønster A: Notification-first målbildeløp | DIGDIR-010 + DIGDIR-002 + DIGDIR-004 + DIGDIR-013 | Hendelsespublisering, sikker API-tilgang, policybasert autorisasjon og API-synlighet | Felles semantisk profil og standard for kvittering/avvik |
| Mønster B: Kontrollert overgangsløp | DIGDIR-008 + KS-001 + KS-002 + DIGDIR-038 | Automatisert innsending der API mangler, med kommunal innføringsstøtte | Klare utfasingskriterier for spor C |
| Mønster C: Semantikk- og styringsløp | DIGDIR-011 + DIGDIR-012 + DIGDIR-047 + DIGDIR-042 | Begrepsharmonisering, datastyring, juridisk avklaring og tverrsektoriell forankring | Forpliktende implementering i alle domener |

## 8. Tiltak prioritert etter effekt

### 8.0 Gap-type per tiltak

| Tiltak | Type (gjenbruk/videreutvikling/nyutvikling/avklaring) | Forventet effekt (høy/middels/lav) | Tidshorisont (kort/middels/lang) | Avhengigheter | Kobling til kapabilitet/prinsipp/produkt | Primær gap-type |
|---|---|---|---|---|---|---|
| Etabler felles semantisk profil for rapporteringshendelser | Videreutvikling | Høy | Kort/middels | DIGDIR-012, DIGDIR-011, DIGDIR-013 | Informasjonsarkitektur, P4/P6 | Semantisk gap |
| Definer standard for kvittering og avvik tilbake til kilden | Videreutvikling | Høy | Kort/middels | DIGDIR-010, DIGDIR-008, DIGDIR-034 | Datastyring, Sporbarhet, P7 | Produktgap |
| Innfør juridisk kontrollpunkt i overgangsløp | Avklaring | Høy | Kort | DIGDIR-047, DIGDIR-004 | Juridisk samhandling, P3/P7 | Juridisk gap |
| Etabler nasjonalt kriteriesett for spor C og utfasing | Avklaring | Høy | Middels | DIGDIR-042, DIGDIR-038, KS-001/002 | Samordning, P2/P5 | Samordningsgap |
| Pilotér spor A+B i avgrenset tjenesteområde med måling | Gjenbruk/videreutvikling | Høy | Kort/middels | Kommune, leverandør, statlig mottaker | Hendelsesdrevet, Dele/Bruke data, P6 | Samordningsgap |
| Standardiser profil for tilgangspolicy i rapporteringsløp | Videreutvikling | Middels | Middels | DIGDIR-004, DIGDIR-002 | Tilgangskontroll/tilgangsstyring, P7 | Juridisk gap |

### Prioritert liste

1. Etabler felles semantisk profil - Begrunnelse: Lav semantisk kvalitet undergraver alle tekniske gevinster.
2. Definer kvittering/avvik som standard - Begrunnelse: Datakvalitet og tillit krever rask korreksjon ved kilden.
3. Sett kriterier for spor C og utfasing - Begrunnelse: Hindrer varig dobbeltspor og styrer investeringene riktig.

## 9. Strategisk vurdering

- Betydning for porteføljeprioritering: Tiltakene bør prioriteres som felles samhandlingsløft, ikke som isolerte sektorprosjekter.
- Betydning for nasjonal arkitektur/felles retning: Caset er godt egnet til å operasjonalisere notification-first som nasjonalt mønster med tydelig overgangslogikk.
- Behov for samordning mellom aktører: Høy. Kommune, stat, leverandører og fellesforvaltning må ha felles styringspunkter for semantikk, juss og innføring.

## 10. Konklusjon

Caset kan realiseres med eksisterende produkter, men krever tydeligere samordning enn det tekniske produktlandskapet alene gir. Spor A+B bør være målbildet, med spor C som styrt overgang i områder uten API-beredskap. De mest kritiske gapene er semantiske, juridiske og organisatoriske, ikke bare tekniske. Produktvurderingen viser at både Digdir- og KS-ressurser er relevante når de brukes i riktig rolle og rekkefølge. Før nyutvikling vurderes bør man etablere felles semantisk profil, standard for kvittering/avvik og kriterier for utfasing av spor C. Pilotering med tydelig måling av tidsbruk, datakvalitet og avviksrate anbefales som neste steg for beslutningsgrunnlag i skala.

### 10.1 Spørsmål til videre diskusjon

1. Hvilke konkrete kriterier skal avgjøre når et tjenesteområde kan gå fra spor C til spor A+B?
2. Hvem eier den autoritative hendelsesmodellen og begrepsforvaltningen på tvers av kommune og stat?
3. Hvilken minimumsprofil for tilgangspolicy skal gjelde før API-oppslag kan settes i produksjon?
4. Hvordan skal kvittering og avvik standardiseres slik at korrigering alltid skjer ved kilden?
5. Hvilke statlige mottakere er først modne for pilotering av full notification-first-flyt?
6. Hvilket styringsforum skal beslutte avhengigheter og prioritering når kommunal og statlig modenhet avviker?
