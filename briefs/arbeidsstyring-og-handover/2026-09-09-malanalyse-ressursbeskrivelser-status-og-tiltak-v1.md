---
date: 2026-09-09
author: copilot
status: draft
topic: malanalyse-ressursbeskrivelser
sources:
  - config/templates/operative-ressurs-template.md
  - config/templates/normerende-ressurs-template.md
  - config/templates/samarbeidsforum-template.md
  - config/templates/okonomiske-og-juridiske-rammer-og-virkemidler-template.md
  - config/prompts/operative-ressurs-canvas.system.md
  - config/prompts/normerende-ressurs-canvas.system.md
  - config/prompts/samarbeidsforum-canvas.system.md
  - config/prompts/okonomiske-og-juridiske-rammer-og-virkemidler-canvas.system.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/02-Maskinporten-produkt-canvas-v4-codex.md
  - arkitektur/ressurser/normerende-ressurser/149-Felles-informasjonsmodeller-v1-claude.md
  - arkitektur/ressurser/samarbeidsfora/120-Styringsradet-for-felleslosningene-v1-codex.md
  - arkitektur/ressurser/rammer-og-virkemidler/144-eForvaltningsforskriften-v2-copilot.md
---

# Malanalyse for ressursbeskrivelser

## Formål
Denne rapporten sammenlikner malene for ressursbeskrivelser med de tilhørende instruksene per ressurstype, og vurderer hvordan faktiske ressursbeskrivelser ligger i forhold til begge. Målet er å avklare om porteføljen har drevet bort fra malen, om instruksen faktisk støtter malen, og hva som bør normaliseres før vi flytter utfyllingen over i skjema.

## Kort konklusjon
Det er en reell forskjell mellom mal og faktisk praksis, men den er ikke lik for alle kategorier.

- For gjenbrukbare løsninger er ressursbeskrivelsene i praksis rikere og mer analysevennlige enn malen.
- For standarder og veiledning er malen, instruksen og praksisen stort sett i samsvar.
- For samhandlingsarenaer og organisering er instruksen tydelig mer fleksibel enn malen, og praksis følger ofte instruksen mer enn malen.
- For økonomiske og juridiske rammer og virkemidler er samsvaret godt, men enkelte filer viser at praksis er mer presis og nyansert enn malen alene.

Det betyr at vi ikke bør normalisere alt blindt tilbake til malen. Vi bør heller bestemme bevisst hvilke avvik som er ønsket forbedring, og hvilke som er uønsket glidning.

## Sammenlikning per kategori

| Kategori | Mal | Instruks | Faktisk praksis | Vurdering | Anbefaling |
|---|---|---|---|---|---|
| Gjenbrukbare løsninger | Relativt generell. Vektlegger flere faste felt, men beskriver dem kort og med mindre krav til beslutningsstøtte. | Tydelig om analysebruk, løsningsbredde, beslutningsstøtte, kapabiliteter og kildearbeid. | Gode beskrivelser, som [Maskinporten](../arkitektur/ressurser/operative-losninger-og-tjenester/02-Maskinporten-produkt-canvas-v4-codex.md), går lenger enn malen og gir bedre gjenbruks- og valgstøtte. | Beskrivelsene er ofte bedre enn malen. Malen er for smal som styringsgrunnlag for det nivået vi faktisk ønsker. | Oppdater malen til å støtte rikere analyse, men behold disiplin på kanoniske kapabiliteter og tydelig avgrensning. |
| Standarder og veiledning | Mer analyseorientert enn operativ malen. Har eksplisitte krav til forpliktelsesnivå, normerende rolle, relasjoner og analysekontekst. | Støtter malen godt og presiserer hva som skal være substansielt fylt ut i v1. | Ressursen [Felles informasjonsmodeller](../arkitektur/ressurser/normerende-ressurser/149-Felles-informasjonsmodeller-v1-claude.md) følger strukturen tett og har god sporbarhet og avgrensning. | Godt samsvar. Her er det lite som tyder på at malen og instruksen er ute av synk. | Behold malen som hovedspor, og juster enkeltfiler ved behov. Ikke masseendre for formens skyld. |
| Samhandlingsarenaer og organisering | Ganske formell og forumorientert, med tydelig mandat-, deltakelses- og grensesnittstruktur. | Mer fleksibel enn malen. Den åpner eksplisitt for åpne nettfora og lavterskelarenaer der formelle forumfelt kan være mindre relevante. | [Styringsrådet for fellesløsningene](../arkitektur/ressurser/samarbeidsfora/120-Styringsradet-for-felleslosningene-v1-codex.md) viser at praksis ofte skriver mer om påvirkning, saksflyt og grensesnitt enn malen krever. | Instruksen og praksisen er bedre tilpasset mangfoldet i kategorien enn malen er. Det er risiko for at malen blir for rigid hvis den brukes uten nyansering. | Oppdater malen slik at den skiller klarere mellom formelle fora og åpne arenaer. Behold fleksibiliteten i instruksen. |
| Økonomiske og juridiske rammer og virkemidler | Tydelig struktur for binding, virkemiddelmekanisme, aktører, konsekvenser og avgrensning. | Understreker eksplisitt forskjellen mellom juridisk binding, økonomisk effekt og styringsvirkning. | [eForvaltningsforskriften](../arkitektur/ressurser/rammer-og-virkemidler/144-eForvaltningsforskriften-v2-copilot.md) følger strukturen godt og er mer presis enn en ren malutfylling ville vært. | Høy samsvar. Få tegn til systematisk avvik. | Små justeringer ved behov, ikke bred omlegging. |

## Typiske avvik vi faktisk ser
| Avvikstype | Hvor det skjer | Effekt | Vurdering |
|---|---|---|---|
| Beskrivelsene er rikere enn malen | Særlig i operative og samhandlingsbaserte ressurser | Gir bedre analyseverdi, men gjør malen mindre treffende som felles skjemagrunnlag | Dette er et ønsket avvik så lenge strukturen er bevisst og kan oversettes til skjema |
| Instruksen er mer nyansert enn malen | Særlig for samhandlingsarenaer og åpne nettfora | Støtter faktisk praksis bedre enn malen gjør | Malen bør bringes nærmere instruksen |
| Enkelte filer har små strukturelle redundanser | Særlig i operative ressurser | Kan gi mindre elegant struktur, men ikke nødvendigvis dårligere analyseinnhold | Bør ryddes der det skaper friksjon for skjema og maskinell bruk |
| Kapabilitetsfeltet brukes mer som beslutningsstøtte enn som ren koblingsliste | Særlig i operative beskrivelser | Godt for leseren, men krever tydelig skille mellom funksjon og beslutningsstøtte | Må formaliseres tydelig i ny modell for å unngå fri tekst i skjema |
| Ulike kategorier har ulik modenhet i språk og struktur | På tvers av hele porteføljen | Gir ulik kvalitet og ulik brukbarhet i analyse | Bør håndteres med kategorispesifikke regler, ikke én lik tvangsmal |

## Vurdering: bedre eller dårligere enn malen?
Det korte svaret er: noen steder bedre, noen steder mer ujevnt, men sjelden dårligere i innhold. Det viktigste er at avvikene ikke er nøytrale.

- Når beskrivelsene er rikere enn malen, er det som regel positivt for analyse og gjenbruk.
- Når instruksen er mer fleksibel enn malen, er det ofte fordi kategorien i praksis er mer variert enn malstrukturen fanger opp.
- Når praksis blir mer fri enn både mal og instruks, er det et reelt avvik som bør ryddes.

Det betyr at spørsmålet ikke bør være om vi skal tvinge alt tilbake til malens nåværende form. Spørsmålet bør være hvilke deler av dagens praksis som skal gjøres til ny standard.

## Hva bør gjøres

### 1. Oppdater malene der de er for smale
Malen for gjenbrukbare løsninger bør revideres hvis vi vil beholde dagens analyseverdi i en skjemabasert fremtid. Den bør ikke krympe ressursene til ren katalogdata. Den må støtte:

- tydelig beslutningsstøtte
- eksplisitt løsningsbredde
- sterkere krav til avgrensning
- kanoniske kapabiliteter med forklaring i tekst, ikke bare navn

For samhandlingsarenaer og organisering bør malen bli mer fleksibel for åpne nettfora og uformelle arenaer. Den bør kunne representere både formelle råd og lavterskelarenaer uten at brukeren må jukse med felt eller presse inn fiktive mandatformuleringer.

### 2. Behold eller formaliser de gode avvikene
Noen avvik er ikke feil, men forbedringer. Det gjelder særlig:

- beslutningsstøttefelter i operative beskrivelser
- tydelig markering av fakta, deduksjon og usikkerhet
- eksplisitte grensesnitt mot andre fora og ressurser
- presis beskrivelse av virkemiddelmekanisme og etterlevelse

Disse bør inn i ny struktur, ikke ut av den.

### 3. Normaliser det som er tilfeldig eller inkonsistent
Det er også avvik vi bør rette før skjema eller YAML overtar:

- ulik bruk av overskrifter og underseksjoner mellom filer
- små redundanser i operative beskrivelser
- forskjellig grad av detalj i tabeller og punktlister der det burde være likt
- variasjon i hvor tydelig instruksens krav faktisk er omsatt i teksten

### 4. Lag en eksplisitt overgangsstandard før skjema
Før malen gjøres skjemabasert, bør vi lage en tydelig norm for hvilke felt som er:

- obligatoriske
- valgfrie
- kategoriavhengige
- kun tekstfelt for forklaring
- rene maskinfelter

Da kan JSON eller YAML bli et uttrykk for den normen, ikke en ny tilfeldig struktur.

## Forslag til oppdatert mal
Dette er ikke en endelig beslutning, men et konkret forslag som tar utgangspunkt i dagens praksis og gjør skjemaovergangen enklere.

### 1. Gjenbrukbare løsninger
Forslaget under beholder dagens hovedstruktur, men gjør noen felt mer eksplisitte og bedre egnet som skjema.

| Felt | Forslag | Begrunnelse |
|---|---|---|
| Navn | Beholdes | Nødvendig identifikator |
| Ressurs ID | Beholdes | Skal være eierbasert og kanonisk |
| Status/Livsfase | Beholdes | Stabilt styringsfelt |
| Modenhet | Beholdes | Nyttig for vurdering av bruk og risiko |
| Kort beskrivelse | Beholdes, men skal være strammere | Bør beskrive løsningens rolle, ikke dokumentets formål |
| Kapabiliteter | Beholdes | Må være kanonisk og forklarende |
| Produktmål | Beholdes | Trengs for prioritering og analyse |
| Brukerbehov | Beholdes | Gjør behovet eksplisitt |
| Hvem er brukerne og brukersegmentene | Beholdes | Egner seg godt som skjema-tabell |
| Hovedfunksjoner | Beholdes | Trengs for funksjonsforståelse |
| Scope og avgrensning | Eget hovedfelt, ikke bare underseksjon | Viktig for skjema og validering |
| Veikart over kommende funksjonalitet | Beholdes, men kan være valgfritt | Ofte usikkert, men nyttig når kjent |
| Forretningsverdi/Verdiforslag | Beholdes | Viktig for beslutningsstøtte |
| Utfordringer og risiko | Beholdes | Kan struktureres som tabellfelt |
| Kanaler | Beholdes der det er relevant | Nyttig for løsningstyper med flere innganger |
| Plattform | Beholdes | Viktig for teknisk plassering |
| Gjenbruk | Beholdes, men splittes tydelig | Bør ha egen struktur for API, kombinasjoner, lisens og kildekode |
| Lisens | Nytt eget felt | Gjør det mulig å utlede åpen kildekode uten fri teksttolking |
| Kildekode | Beholdes som eget underpunkt | Må kunne uttrykke åpen/proprietær status eksplisitt |
| Støtter arkitekturprinsipper | Beholdes | Trengs for analyse og vurdering av svakheter |
| Finansiering | Beholdes | Relevant for ressursforvaltning |
| Forvaltning/eier | Beholdes, men bør standardiseres i underfelt | Egner seg for skjema og validering |
| Lenke til dokumentasjon | Beholdes | Må kunne drives maskinelt |
| Kildegrunnlag brukt i utfyllingen | Beholdes | Sporbarhet og kvalitetssikring |

Foreslåtte tillegg eller endringer:

- Del `Gjenbruk` i faste underfelter: `API-er`, `Standarder`, `Lisens`, `Kildekode`, `Vanlige kombinasjoner med andre produkter`.
- Bruk faste verdier for `Kildekode`: `Åpen kildekode`, `Proprietær`, `Ikke offentlig dokumentert`.
- Bruk `Lisens` som eget tekst- eller valgfelt, med kontrollert liste der det er mulig.
- Gjør `Hovedfunksjoner` til en strukturert blokk med minst tre underdeler: operativ funksjon, typiske brukssituasjoner, ikke førstevalg.
- Legg `Scope og avgrensning` opp som et tydelig skjemaavsnitt, ikke som en underseksjon av hovedfunksjoner.
- Gjør `Forvaltning/eier` om til standardiserte underfelt for produktansvar, driftsansvar, budsjettansvar og styringsmodell.

### 2. Samhandlingsarenaer og organisering
For samhandlingsarenaer bør malen være mer fleksibel enn for løsninger, men fortsatt strukturelt lik nok til å kunne fylles av andre.

| Felt | Forslag | Begrunnelse |
|---|---|---|
| Navn | Beholdes | Nødvendig identifikator |
| Ressurs ID | Beholdes | Kanonisk kobling til registeret |
| Status/Livsfase | Beholdes | Viktig for å skille planlagt, aktiv og avviklet arena |
| Kort beskrivelse | Beholdes, men skal beskrive rolle og funksjon | Bør si hva forumet er, ikke hvorfor det er viktig for oversikten |
| Mandat og rolle | Beholdes | Sentral for analyse |
| Beslutningsmyndighet og forpliktelse | Beholdes | Må være eksplisitt for å skille råd, beslutning og dialog |
| Kapabiliteter | Beholdes | Må fortsatt være rene og kanoniske |
| Deltakere og målgruppe | Beholdes | Nødvendig for å forstå representasjon |
| Hvilke ressurser forumet påvirker | Beholdes | En av de viktigste analysedelene |
| Arbeidsform og møtearena | Beholdes | Praktisk nyttig og lett å skjemaifisere |
| Slik melder du inn en sak | Beholdes, men kan være valgfritt for åpne arenaer | Skal kunne markeres `Ikke relevant` der det ikke passer |
| Typiske saker og leveranser | Beholdes | Viser hva forumet faktisk gjør |
| Når forumet bør involveres | Beholdes | Viktig for bruk i analyse og utvikling |
| Scope og avgrensning | Beholdes | Må skille forumet fra linje og andre fora |
| Forvaltningsmodell | Beholdes | Egner seg godt som strukturerte underfelt |
| Grensesnitt mot andre fora | Beholdes | Viktig for å unngå overlapp og feil bruk |
| Relasjon til andre ressurser | Beholdes | Trengs for porteføljeanalyse |
| Forretningsverdi og arkitekturverdi | Beholdes | Skal være beslutningsrelevant |
| Konsekvens ved manglende involvering eller svak forankring | Beholdes | Viser hvorfor forumet finnes |
| Utfordringer og risiko | Beholdes | Kan struktureres som tabellfelt |
| Publiseringsform og tilgjengelighet | Beholdes | Egnet som skjema- eller metadatafelt |
| Støtter arkitekturprinsipper | Beholdes | Må fortsatt vurdere styrker og svakheter |
| Lenke til dokumentasjon | Beholdes | Sporbarhet |
| Kildegrunnlag brukt i utfyllingen | Beholdes | Sporbarhet |

Foreslåtte tillegg eller endringer:

- Del `Beslutningsmyndighet og forpliktelse` i faste verdier eller sjekkbokser for `beslutter`, `anbefaler`, `fasiliterer`, `informerer`.
- Gjør `Slik melder du inn en sak` valgfritt eller `Ikke relevant` for åpne arenaer.
- Gjør `Grensesnitt mot andre fora` til et eget strukturfelt med obligatorisk sammenlikning når forumet har overlappende mandat.
- La `Kort beskrivelse` og `Mandat og rolle` være de to første innholdsdelene i alle ressursformer, slik at skjemaet får en fast inngang.
- Gi `Forvaltningsmodell` standardiserte underfelt for eier/oppdragsgiver, sekretariat, deltakelse og publiserings-/beslutningsarena.

### 3. Prioritert rekkefølge
Hvis vi skal ta dette stegvis, bør rekkefølgen være:

1. Operative løsninger, fordi de allerede har et tydelig feltsett og nå får et nytt lisensfelt.
2. Samhandlingsarenaer, fordi de trenger mer fleksibilitet og har større variasjon i form.
3. Deretter kan vi vurdere om de normerende og juridiske malene også bør få tilsvarende skjemaform.

## Anbefalt videre løp
1. Lag en egen avklaringsrunde for maldesign før skjema, med fokus på hvilke felt som faktisk skal standardiseres på tvers av alle kategorier.
2. Revider spesielt malen for gjenbrukbare løsninger og samhandlingsarenaer.
3. Behold dagens normerende og juridiske maler som utgangspunkt, men juster dem bare der de ikke passer til skjemastrukturen eller der praksis allerede er bedre.
4. Lag et lite sett med pilotfiler eller pilotobjekter i YAML/JSON for å teste om de nye feltene faktisk dekker behovet.
5. Kjør deretter en strukturrevisjon av eksisterende ressursbeskrivelser mot den nye normen, ikke mot dagens mal alene.

## Konklusjon
Vi har ikke bare et avvik mellom mal og praksis. Vi har også et tegn på at malene ikke er modne nok som grunnlag for en framtidig skjemabasert modell.

Derfor bør vi ikke automatisk rette alle ressursbeskrivelser mot dagens mal. Vi bør først bestemme hvilke avvik som er ønsket forbedring, og så oppdatere malen slik at den kan bli et reelt skjema- og maskingrunnlag for resten av porteføljen.
