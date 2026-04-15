# 1. Kort oppsummering

- Case: Flytting av elever i skoleåret mellom kommuner/fylkeskommuner
- Analysetillit: Middels
- Hovedfunn (1-3 setninger): Caset kan løses med et sammensatt mønster der flyttehendelse utløser notifikasjon (spor A), rettighetsstyrt API-oppslag (spor B) og kontrollert overgang med standardisert eksport (spor C). Hovedutfordringen er ikke mangel på enkeltprodukter, men semantisk harmonisering av elevmappe, juridisk avklaring av delingsgrunnlag og samordnet innføring mellom kommuner, fylker og leverandører.
- Viktigste kapabilitetsgap: Informasjonsarkitektur for standardisert elevmappe, juridisk samhandling ved sensitiv deling/samtykke og samordning i leverandørmarkedet.
- Mest relevante produkter for gjenbruk: KS-008 Fiks folkeregister, DIGDIR-010 Altinn Events, DIGDIR-002 Maskinporten, DIGDIR-004 Altinn Autorisasjon, KS-001 FIKS-plattformen, KS-002 Fiks melding, DIGDIR-011/012/013 katalogressurser, NOVARI-003 FINT Informasjonsmodell.
- Hva mangler: En felles nasjonal profil for innhold i grunnpakke/utvidet pakke, standard for samtykke- og avviksløp, og tydelig styring for overgang fra spor C til spor A+B.
- Anbefalt prioritering:
  1. Etabler standardisert elevmappeprofil og felles begreper.
  2. Definer juridisk/teknisk kontrollpunkt for hjemmel og samtykke.
  3. Pilotér spor A+B med leverandørforpliktelse og målbar utfasing av spor C.

## 2. Formål

- Analyseformål: Vurdere hvordan elevinformasjon kan følge eleven digitalt ved flytting i skoleåret, med minst mulig manuelt arbeid og høy trygghet.
- Beslutning analysen skal understøtte: Valg av nasjonalt løsningsmønster og prioriterte tiltak for innføring.
- Avgrensning: Caset dekker overføring av elevinformasjon mellom skoleeierne ved flytting, inkludert samtykkeløp og overgangsløp ved manglende API-støtte.

## 3. Input / casebeskrivelse

- Case-tittel: Flytting av elever i skoleåret mellom kommuner/fylkeskommuner
- Kort casebeskrivelse: En flyttehendelse fra Folkeregisteret eller søknad om skoleplass i ny kommune/fylke skal utløse digital og rettighetsstyrt overføring av elevinformasjon. Målbildet er notification-first med API-henting av grunnpakke og eventuelt utvidet pakke, med samtykke ved behov og standardisert eksport i overgangsløp.
- Berørte livshendelser / tjenester / overganger: Flytting i skoleløpet, elevoppfølging ved skolestart i ny kommune/fylke, tverrsektoriell oppfølging av sårbare barn.
- Hovedutfordring i caset: Etablere rask, trygg og semantisk konsistent deling på tvers av forvaltningsnivåer og leverandører.
- Kildemateriale brukt: Brukerens casebeskrivelse, kapabiliteter, prinsipper, produktregister, operative produkter, normerende ressurser og samarbeidsfora.

## 3.1 Inputgrunnlag og analysetillit

| Vurderingspunkt | Vurdering |
|---|---|
| Inputgrunnlag | Høy. Caset er tydelig på mål, aktører, trigger, hovedforløp, alternativer og gevinster. |
| Datagrunnlag | Middels. Caset mangler kvantifiserte volum, responstidskrav og avgrensning per datakategori. |
| Produktgrunnlag | Middels til høy. De viktigste operative produktene har gode beskrivelser; enkelte normerende ressurser er fortsatt overordnet beskrevet. |
| Samlet analysetillit (høy/middels/lav) | Middels |

Viktigste usikkerheter (minst 3):
- Hvilke opplysninger som alltid inngår i grunnpakke versus utvidet pakke er ikke nasjonalt standardisert.
- Juridiske grenser mellom hjemmelsbasert deling og samtykkebasert deling er ikke operasjonalisert i en felles prosessmodell.
- Leverandørenes faktiske API-modenhet og støtte for felles standarder varierer betydelig.
- Samhandling med PPT/barnevern i samme flyttehendelse er faglig ønsket, men ikke avklart i ansvar og omfang.

## 4. Problembilde

### 4.1 Hovedproblem

Ved flytting i skoleåret oppstår ofte tidsforsinkelse før ny skole får nødvendig elevinformasjon. Konsekvensen er risiko for brudd i tilrettelegging, særlig for elever med særskilte behov. Caset skisserer et godt digitalt målbildeløp, men gjennomføringen krever felles semantikk, tydelig hjemmelsvurdering og koordinert leverandørinnsats. Uten dette får man fragmentert praksis, mer manuelt arbeid og svakere kontinuitet for eleven.

### 4.2 Konsekvenser for målgrupper

- Elev og foreldre kan oppleve usikker overgang og forsinket tilrettelegging.
- Lærer og skoleledelse i tilflyttingskommune får for lite beslutningsgrunnlag ved skolestart.
- Fraflyttingskommune må håndtere ad hoc-forespørsler i stedet for standardisert overføring.

### 4.3 Konsekvenser for forvaltning og tjenesteutøvelse

- Ulik datakvalitet og semantikk mellom systemer gir feiltolkning og ekstra oppfølging.
- Manglende standard for samtykkeløp kan stoppe nødvendig deling i praksis.
- Stor variasjon i API-modenhet gir risiko for varig overgangsløp (spor C) uten utfasing.

## 5. Kapabilitetsanalyse

| Kapabilitet | Relevans (høy/middels/lav) | Hva finnes i dag | Identifisert gap | Konsekvens for caset |
|---|---|---|---|---|
| Hendelsesdrevet | Høy | Hendelsestjenester og flyttedata er tilgjengelige. | Ulik modell for hendelsestyper og utløsende kriterier. | Ujevn automatiseringsgrad. |
| Dele data med andre | Høy | Flere kanaler for deling finnes. | Ingen felles profil for elevmappeinnhold i deling. | Mottaker får ulik datakvalitet. |
| Bruke data fra andre | Høy | API-oppslag kan støttes med eksisterende komponenter. | Ulik API-modenhet hos leverandører/eiere. | Forsinket oppstart i ny skole. |
| Tilgangskontroll / tilgangsstyring | Høy | Autorisasjonskomponenter finnes. | Felles policyprofil for elevflytting mangler. | Risiko for over- eller underdeling. |
| Informasjonsarkitektur | Høy | Begreps- og API-katalog finnes, samt FINT-modell. | Manglende nasjonal standard for grunnpakke/utvidet pakke. | Feiltolkning og dårlig sammenheng. |
| Juridisk samhandling | Høy | Veiledning finnes. | Operasjonell modell for hjemmel/samtykke mangler. | Ulik praksis og mulig stopp i flyt. |
| Datastyring | Middels | Kvalitetsarbeid kan etableres ved kilden. | Uklart ansvar for avvikshåndtering mellom partene. | Lavere tillit til data. |
| Organisatorisk samhandling / samordning | Høy | Arenaer og innføringsmønstre finnes. | Manglende forpliktende leverandørsamordning. | Lang innføringstid og lokalt særpreg. |

### Oppsummering av kapabilitetsgap

- Viktigste gap 1: Semantisk gap i standardisert elevmappe (innhold og struktur).
- Viktigste gap 2: Juridisk gap i operasjonalisering av hjemmel og samtykke.
- Viktigste gap 3: Samordningsgap i leverandør- og innføringsløp på tvers av kommune/fylke.

## 6. Prinsippvurdering

| Prinsipp | Status (oppfylt/delvis/brutt) | Hva finnes i dag | Hvordan caset utfordrer prinsippet |
|---|---|---|---|
| P1 Ta utgangspunkt i brukernes behov | Delvis | Caset er tydelig på barnets beste og rask oppstart. | Uten standardisering kan behovet ikke møtes likt overalt. |
| P2 Ta arkitekturbeslutninger på rett nivå | Delvis | Både nasjonale og kommunale komponenter er tilgjengelige. | Beslutninger om pakkeinnhold og policy tas for lokalt i dag. |
| P3 Bidra til digitaliseringsvennlige regelverk | Delvis | Veiledning finnes for juridisk avklaring. | Samtykke/hjemmel er ikke harmonisert i praktisk flyt. |
| P4 Del og gjenbruk data | Delvis | Teknisk deling er mulig i flere spor. | Semantisk variasjon svekker faktisk gjenbruk. |
| P5 Del og gjenbruk løsninger | Delvis | Et bredt sett fellesløsninger finnes. | Risiko for lokale punktintegrasjoner uten felles styring. |
| P6 Lag digitale løsninger som støtter samhandling | Delvis | Hendelser, API og melding kan kombineres. | Samhandling med PPT/barnevern er ikke avklart i samme mønster. |
| P7 Sørg for tillit til oppgaveløsningen | Delvis | Autentisering/autorisasjon og sporbarhet kan etableres. | Manglende enhetlig avviksløp kan svekke etterprøvbarhet. |

### Oppsummering av prinsippvurdering

Caset er prinsipielt riktig innrettet, men prinsippoppfyllelsen er avhengig av felles semantikk, juridisk avklaring og forpliktende samordning i innføring.

## 7. Produktvurdering

### 7.0 Vurderingsrekkefølge for produktkategorier

1. Identitet og representasjon: DIGDIR-002, DIGDIR-004 og SIKT-001 vurdert.
2. Datadeling og integrasjon: KS-001, KS-008 og DIGDIR-008 vurdert.
3. Hendelser og meldinger: DIGDIR-010 og KS-002 vurdert.
4. Dialog og brukerflate: Ikke prioritert som hovedmønster, men relevant for samtykkegrensesnitt.
5. Register og datagrunnlag: Folkeregistertilgang via KS-008 vurdert som triggernær komponent.
6. Katalog og semantikk: DIGDIR-011/012/013 og NOVARI-003 vurdert.
7. Sektorprodukter og domeneprodukter: Leverandørnære skolefagsystem er sentrale i gjennomføring, men utenfor direkte produktkatalog her.

### 7.1 Vurderte produkter fra katalogen

| Produkt (fra produktkatalogen) | Produktkategori | Relevans for caset | Klassifisering (brukes direkte/videreutvikles/ikke relevant) | Begrunnelse |
|---|---|---|---|---|
| KS-008 Fiks folkeregister | Register og datagrunnlag | Høy | Brukes direkte | Gir praktisk tilgang til flytte- og persondata i kommunal sektor og støtter triggerløp. Grunnlag: full produktbeskrivelse. |
| DIGDIR-010 Altinn Events | Hendelser og meldinger | Høy | Brukes direkte | Dekker notifikasjon og asynkron hendelsesflyt i spor A. Grunnlag: full produktbeskrivelse. |
| DIGDIR-002 Maskinporten | Identitet og representasjon | Høy | Brukes direkte | Standard autentisering for maskin-til-maskin API-oppslag i spor B. Grunnlag: full produktbeskrivelse. |
| DIGDIR-004 Altinn Autorisasjon | Identitet og representasjon | Høy | Brukes direkte | Policy- og representasjonsstøtte for tilgang til elevdata. Grunnlag: full produktbeskrivelse. |
| DIGDIR-008 Altinn Formidling | Datadeling og integrasjon | Middels | Brukes direkte | Relevante egenskaper for spor C ved manglende API-støtte. Grunnlag: full produktbeskrivelse. |
| KS-001 FIKS-plattformen | Datadeling og integrasjon | Middels | Videreutvikles | Egnet som kommunalt innførings- og integrasjonslag, men krever tydelig rolle mot nasjonalt målbilde. Grunnlag: full produktbeskrivelse. |
| KS-002 Fiks melding | Hendelser og meldinger | Middels | Videreutvikles | Relevant kanal i overgangsløp og meldingsutveksling, men ikke ønsket som permanent sluttmønster. Grunnlag: full produktbeskrivelse. |
| DIGDIR-011 Felles datakatalog | Katalog og semantikk | Middels | Brukes direkte | Understøtter synlighet og sammenheng mellom datasett/modeller/API. Grunnlag: full produktbeskrivelse. |
| DIGDIR-012 Begrepskatalog | Katalog og semantikk | Høy | Brukes direkte | Kritisk for semantisk harmonisering av elevmappe og begreper. Grunnlag: full produktbeskrivelse. |
| DIGDIR-013 API-katalog | Katalog og semantikk | Middels | Brukes direkte | Støtter oppdagbarhet og standardisering av API-kontrakter. Grunnlag: full produktbeskrivelse. |
| NOVARI-003 FINT Informasjonsmodell | Sektorprodukter og domeneprodukter | Middels | Videreutvikles | Nyttig normerende grunnlag for semantikk i utdanningsområdet, men må harmoniseres mot nasjonal profil. Grunnlag: full normerende beskrivelse. |
| SIKT-001 Feide | Identitet og representasjon | Lav/middels | Ikke relevant (primært) | Feide er viktig i utdanning for brukerinnlogging, men caset er primært system-til-system deling mellom skoleeiere. Grunnlag: full produktbeskrivelse. |
| DIGDIR-047 Digitaliseringsvennlig regelverk | Normerende ressurs | Høy | Brukes direkte | Nødvendig for å avklare juridisk grunnlag i automatisk deling av sensitive elevdata. Grunnlag: moderat produktbeskrivelse. |
| DIGDIR-042 Skate | Samarbeidsforum | Middels | Brukes direkte | Relevans for tverrsektoriell forankring av felles retning og leverandørsamordning. Grunnlag: full forumbeskrivelse. |
| KS-011 Felles mal for innføring av digitale fellestjenester | Normerende ressurs | Middels | Brukes direkte (lavere tillit) | Relevans for innføringsstyring er sannsynlig, men detaljert produktbeskrivelse mangler i repo og vurderingen har lavere tillit. Grunnlag: registermetadata. |

### 7.2 Oppsummering: hva finnes, hva kan gjenbrukes, hva må videreutvikles

- Hva finnes: Teknisk og organisatorisk byggesett for hendelse, autorisasjon, API-oppslag, melding og semantisk katalogstøtte.
- Hva kan gjenbrukes direkte: KS-008, DIGDIR-010, DIGDIR-002, DIGDIR-004, DIGDIR-008, DIGDIR-011/012/013.
- Hva må videreutvikles: Felles elevmappeprofil, samtykke-/hjemmelsflyt og leverandørforpliktelse på API-standarder.
- Hva er ikke relevant i dette caset: Feide som primærmønster for selve dataoverføringen mellom skoleeiere.

### 7.3 Eksplisitte mangler og behov for nye/sammensatte løsninger

| Identifisert mangel | Hvorfor mangelen oppstår | Konsekvens hvis ikke løst | Forslag til ny/sammensatt løsning | Kan bygge på eksisterende produkter |
|---|---|---|---|---|
| Ulik definisjon av grunnpakke/utvidet pakke | Ingen felles nasjonal semantisk profil | Ulikt innhold ved flytting og svak kontinuitet | Nasjonal elevmappeprofil med obligatoriske og valgfrie felter | Ja, DIGDIR-012 + NOVARI-003 + DIGDIR-011 |
| Uklart samtykkeløp for sensitive data | Samspill hjemmel/samtykke ikke standardisert | Forsinket deling eller feil deling | Standardisert samtykke- og beslutningsflyt med tydelige kontrollpunkter | Ja, DIGDIR-004 + DIGDIR-047 |
| Manglende enhetlig avviksløp | Ulik praksis for feil og korrigering | Feil varer lenger og oppfølging forsinkes | Felles mønster for avviksmelding tilbake til kildesystem | Ja, DIGDIR-010 + DIGDIR-008 + KS-002 |
| Risiko for varig spor C | API-modenhet varierer mellom leverandører | Dobbeltspor med høy kostnad og lav standardisering | Utfasingsplan med modenhetskriterier og milepæler | Ja, KS-001 + DIGDIR-042 + KS-011 |

### 7.4 Sammensatte løsningsmønstre

| Løsningsmønster | Produkter som inngår | Hva mønsteret dekker | Hva som fortsatt mangler |
|---|---|---|---|
| Mønster A: Flyttehendelse + oppslag (målbilde) | KS-008 + DIGDIR-010 + DIGDIR-002 + DIGDIR-004 + DIGDIR-013 | Trigger, notifikasjon, autentisering, autorisasjon og API-oppslag av elevdata | Felles elevmappeprofil og standard for avvik/kvittering |
| Mønster B: Overgang ved lav API-modenhet | DIGDIR-008 + KS-002 + KS-001 | Standardisert eksport og sikker meldingsutveksling i spor C | Tidsfestet utfasing og harmonisert innhold |
| Mønster C: Semantikk- og styringsløp | DIGDIR-012 + DIGDIR-011 + NOVARI-003 + DIGDIR-047 + DIGDIR-042 | Felles begreper, modellforankring, juridisk avklaring og samordning | Forpliktende implementering hos alle leverandører |

## 8. Tiltak prioritert etter effekt

### 8.0 Gap-type per tiltak

| Tiltak | Type (gjenbruk/videreutvikling/nyutvikling/avklaring) | Forventet effekt (høy/middels/lav) | Tidshorisont (kort/middels/lang) | Avhengigheter | Kobling til kapabilitet/prinsipp/produkt | Primær gap-type |
|---|---|---|---|---|---|---|
| Definer nasjonal profil for elevmappe (grunnpakke/utvidet pakke) | Videreutvikling | Høy | Kort/middels | DIGDIR-012, NOVARI-003, leverandører | Informasjonsarkitektur, P4/P6 | Semantisk gap |
| Standardiser hjemmel- og samtykkekontroll i flyten | Avklaring | Høy | Kort | DIGDIR-004, DIGDIR-047, juridiske miljø | Juridisk samhandling, P3/P7 | Juridisk gap |
| Etabler felles avviksmønster tilbake til kildesystem | Videreutvikling | Høy | Kort/middels | DIGDIR-010, DIGDIR-008, KS-002 | Datastyring, Sporbarhet, P7 | Produktgap |
| Sett nasjonale kriterier for utfasing av spor C | Avklaring | Høy | Middels | KS-001, DIGDIR-042, KS-011 | Samordning, P2/P5 | Samordningsgap |
| Pilotér spor A+B i utvalgt skoleområde | Gjenbruk/videreutvikling | Høy | Kort/middels | Kommuner, fylker, leverandører | Hendelsesdrevet, Dele/Bruke data, P1/P6 | Samordningsgap |
| Avklar om PPT/barnevern skal kobles på samme hendelse | Avklaring | Middels | Middels/lang | Tverrsektorielle aktører | Samordning, Juridisk samhandling, P2/P6 | Juridisk gap |

### Prioritert liste

1. Definer nasjonal elevmappeprofil - Begrunnelse: Gir felles semantikk og reduserer feiltolkning ved oppstart i ny skole.
2. Standardiser hjemmel/samtykke-kontroll - Begrunnelse: Kritisk for trygg og lovlig deling av sensitive elevdata.
3. Pilotér spor A+B med avviksmønster - Begrunnelse: Dokumenterer gevinst og skaper grunnlag for kontrollert utfasing av spor C.

## 9. Strategisk vurdering

- Betydning for porteføljeprioritering: Caset bør prioriteres som et tverrkommunalt samhandlingsløft med høy samfunnsverdi for barn og unge.
- Betydning for nasjonal arkitektur/felles retning: Egnet som referansecase for notification-first i oppvekstområdet med tydelig kobling mellom trigger, oppslag og samtykke.
- Behov for samordning mellom aktører: Svært høy. Kommuner, fylker, statlige aktører og leverandører må styres etter felles profil og milepæler.

## 10. Konklusjon

Caset har et tydelig og realistisk målbildeløp med eksisterende produkter som kan settes sammen til en fungerende løsning. Den største risikoen ligger i manglende standardisering av elevmappeinnhold, ujevn juridisk praksis og svak leverandørsamordning. Spor A+B bør etableres som nasjonal retning, mens spor C må være tidsbegrenset og styrt av definerte modenhetskriterier. Ved å kombinere triggerdata, hendelsesflyt, autorisert API-oppslag og semantisk forankring kan man redusere tid til tilrettelagt oppstart i ny skole betydelig. Neste steg bør være en forpliktende pilot med klar gevinstmåling, før bredding på tvers av tjenesteområder og eventuelt mot PPT/barnevern.

### 10.1 Spørsmål til videre diskusjon

1. Hvilke felter skal være obligatoriske i grunnpakke versus utvidet pakke nasjonalt?
2. Hvilke konkrete kriterier avgjør om deling kan skje på hjemmel alene eller krever samtykke?
3. Hvordan skal avvik meldes, kvitteres og korrigeres ved kilden på enhetlig måte?
4. Hvilke leverandørkrav må gjelde for API-standard og hendelsesmodell i anskaffelser?
5. Når skal spor C fases ut i ulike tjenesteområder, og hvem beslutter dette?
6. Skal flyttehendelsen i samme mønster utløse koordinert informasjonsflyt mot PPT/barnevern?
