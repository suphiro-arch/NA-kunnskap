---
date: 2026-04-13
author: codex
status: draft
topic: modernisert-rapportering-kommune-stat-analyse-v2
sources:
  - config/prompts/arkitekturassistert-analyse-av-utviklingsbehov.system.md
  - config/templates/arkitekturassistert-analyse-av-utviklingsbehov-template.md
  - Analyser/17-Modernisert-rapportering-kommune-stat-analyse.md
  - arkitektur/prinsipper/principles.md
  - arkitektur/ressurser/produktnummerering.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/02-Maskinporten-produkt-canvas-v3-codex.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/04-Altinn-autorisasjon-produkt-canvas-v4-codex.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/08-Altinn-formidling-produkt-canvas-v3-codex.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/12-Altinn-events-produkt-canvas-v3-codex.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/13-Felles-datakatalog-produkt-canvas-v3-codex.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/14-Begrepskatalog-produkt-canvas-v3-codex.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/15-API-katalog-produkt-canvas-v3-codex.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/25-FIKS-plattformen-produkt-canvas-v1-codex.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/70-FINT-Felleskomponent-v1-codex.md
---

# 17v2 Modernisert rapportering mellom kommune og stat

## Kortversjon for ledelse

Rapportering mellom kommune og stat kan moderniseres uten å starte med en helt ny nasjonal løsning. Det finnes allerede sterke byggesteiner i den nasjonale porteføljen, særlig for hendelser, sikker maskin-til-maskin tilgang, overgangsvis formidling og semantisk standardisering.

Det viktigste først er ikke ny teknologi, men å etablere et felles samhandlingsmønster og et felles semantisk grunnlag. Anbefalt retning er derfor:

- bruk eksisterende Digdir-komponenter som kjerne
- standardiser begreper og API-er tidlig
- pilotér ett til to rapporteringsløp
- bruk filbasert formidling kun som definert overgangsmønster

Dette gir høyere gjenbruk, mindre fragmentering og bedre grunnlag for gradvis overgang til mer løpende og standardisert rapportering.

## 1. Formål

Denne analysen vurderer hvordan rapportering mellom kommune og stat kan moderniseres fra periodisk og filbasert innsending til en mer hendelsesdrevet, sporbar og integrert samhandlingsmodell. Målet er å identifisere hvilke deler av behovet som kan dekkes med eksisterende nasjonale ressurser, hvilke gap som gjenstår, og hvilke tiltak som gir størst effekt først.

Analysen bygger på eksisterende casebeskrivelse i repoet, men er skrevet på nytt etter oppdatert instruks for arkitekturassistert analyse av utviklingsbehov. Det betyr blant annet tydeligere avklaring av case, fast vurderingsrekkefølge for produktkategorier, eksplisitt gap-klassifisering og en skarpere vurdering av sammensatte løsningsmønstre.

## 2. Input / casebeskrivelse

Kommunesektoren rapporterer i dag til statlige mottakere gjennom flere ulike løp, ofte med varierende definisjoner, periodisering, filformat og modenhet i grensesnitt. I dette caset er det særlig overgangene mellom kommuner og statlige mottakere som er i fokus, med SSB som den tydeligste referansen for behovet, men problemstillingen er bredere enn én virksomhet.

Målbildet er ikke én ny nasjonal løsning for all rapportering, men et felles samhandlingsmønster som kan brukes på tvers av flere rapporteringsløp. Det ønskede skiftet er fra:

- manuell eller halvmanuell sammenstilling og innsending
- filorientert og periodepreget rapportering
- svak semantisk harmonisering på tvers av løp

til:

- hendelsesnær deling der det er realistisk
- sikker API-basert uthenting eller abonnement der det passer
- tydelig semantisk beskrivelse av hva som rapporteres, når og med hvilket ansvar

### 2.1 Inputgrunnlag og analysetillit

**Analysetillit: middels**

Vurderingen har et godt nasjonalt arkitekturgrunnlag for gjenbruk av eksisterende ressurser, men svakere grunnlag for detaljer om mottakersiden hos statlige aktører og om juridisk og organisatorisk gjennomførbarhet i konkrete rapporteringsløp.

Følgende usikkerheter er særlig viktige:

1. Det er ikke fullt avklart hvor moden mottakersiden er for å gå fra filmottak til API-basert uthenting eller hendelsesdrevet oppdatering.
2. Det finnes ikke et etablert felles semantisk grunnlag i caset for rapporteringshendelser, rapporteringsobjekter og avgrensning av når data er "klare" for deling.
3. Autorisasjons- og rettighetsbildet mellom kommune, leverandør, statlig mottaker og eventuelle mellomledd er ikke konkretisert nok til å vurdere endelig målbilde.
4. Det er uklart hvor mye av behovet som i praksis er likt på tvers av sektorer, og hvor mye som fortsatt er domene- eller formålsavhengig.

### 2.2 Avklaring: ett case eller flere

Dette vurderes som **ett hovedcase**: modernisering av rapportering mellom kommune og stat.

Caset har flere mulige gjennomføringsspor, men problemstillingen er den samme:

- hvordan rapportering kan gå fra innsending av avgrensede filer til mer løpende og standardisert deling
- hvordan samme mønster kan brukes på tvers av flere rapporteringsområder

Det er derfor ikke hensiktsmessig å splitte analysen i flere separate case på dette stadiet. Det riktige skillet går heller mellom overgangsmønster og ønsket fremtidig målbilde.

## 3. Målgruppe og styringsnivå

Primær målgruppe er:

- nasjonale arkitekter og løsningsansvarlige i stat og kommune
- virksomheter som mottar eller leverer rapporteringsdata
- portefølje- og styringsmiljøer som skal prioritere videre standardisering og felleskomponentbruk

Styringsnivå:

- strategisk og taktisk nivå for valg av felles mønster
- ikke detaljert løsningsdesign for ett enkelt rapporteringsløp

## 4. Problembilde

### 4.1 Hovedproblem

Dagens rapportering mellom kommune og stat er preget av ulike integrasjonsformer, varierende begrepsbruk og svak samordning mellom semantikk, transport, autorisasjon og mottakslogikk. Det gjør det krevende å modernisere løpene stegvis og vanskelig å etablere et gjenbrukbart nasjonalt mønster.

### 4.2 Konsekvenser for målgrupper

- Kommuner må forholde seg til flere ulike rapporteringsformer og mottakskrav.
- Leverandører må støtte flere parallelle mønstre i stedet for ett tydelig nasjonalt samhandlingsmønster.
- Statlige mottakere får svakere grunnlag for konsistent kvalitet, sporbarhet og gradvis modernisering.

### 4.3 Konsekvenser for forvaltning og tjenesteutøvelse

- Høyere kostnad ved hver ny rapporteringsordning eller endring i eksisterende ordning.
- Langsommere overgang til mer oppdaterte og gjenbrukbare data.
- Økt risiko for at rapportering forbedres lokalt uten at nasjonal samhandling forbedres tilsvarende.

## 5. Kapabilitetsanalyse

| Kapabilitet | Relevans i caset | Vurdering |
|---|---|---|
| Dele data med andre | Svært høy | Kjernen i caset er trygg og standardisert deling fra kommune til stat. |
| Bruke data fra andre | Høy | Statlige mottakere må kunne hente og bruke data på en mer strukturert måte enn i dagens filmønstre. |
| Meldingsformidling | Høy | Trengs både i overgangsfasen og i løp der asynkron utveksling fortsatt er riktig. |
| Hendelsesdrevet | Høy | Viktig for modernisering der rapportering kan utløses av endringer fremfor periodekjøring. |
| Sikring av informasjonsflyt og datautveksling | Svært høy | Tillit, sporbarhet og sikker transport er grunnleggende. |
| Tilgangskontroll | Høy | Mottaker må ha riktig tilgang til riktig rapporteringsgrunnlag og riktig representasjonsnivå. |
| Informasjonsarkitektur | Svært høy | Felles begreper, informasjonsmodeller og API-beskrivelser er en forutsetning for gjenbruk. |
| Datastyring | Høy | Ansvar for datakvalitet, definisjoner og livsløp må tydeliggjøres. |
| Organisatorisk samhandling | Høy | Caset avhenger av samordning mellom kommuner, leverandører, statlige mottakere og nasjonale virkemidler. |
| Juridisk samhandling | Høy | Deling mellom forvaltningsnivåer krever tydelig hjemmel, formålsavklaring og ansvarslinjer for å ta løsningen i bruk. |
| Forvaltningsstandarder | Høy | Et felles mønster må kunne forankres som anbefalt eller styrende praksis over tid. |

**Oppsummering av kapabilitetsanalyse**

Caset er ikke primært et problem med mangel på transportteknologi. Det er et sammensatt behov der semantikk, sikker tilgang, hendelser og samordning må virke sammen. De sterkeste gapene ligger derfor i koblingen mellom informasjonsarkitektur, autorisasjon og organisatorisk samordning, ikke bare i fravær av én ny teknisk komponent.

## 6. Prinsippvurdering

| Prinsipp | Relevans | Vurdering i caset |
|---|---|---|
| P1 Ta utgangspunkt i brukernes behov | Høy | Rapportering må utformes ut fra faktisk behov hos både rapporterende kommune og mottakende statlig aktør, ikke bare dagens interne organisering. |
| P2 Ta arkitekturbeslutninger på rett nivå | Svært høy | Nasjonalt mønster bør besluttes som felles retning, mens sektorspesifikke detaljer må håndteres nærmere det enkelte rapporteringsløpet. |
| P3 Bidra til digitaliseringsvennlige regelverk | Høy | Regelverk og rapporteringskrav må ikke låse caset til unødig filbasert og periodisk innsending. |
| P4 Del og gjenbruk data | Svært høy | Hele moderniseringsgevinsten avhenger av at data kan deles og brukes på en mer direkte og standardisert måte. |
| P5 Del og gjenbruk løsninger | Høy | Eksisterende nasjonale ressurser bør brukes før nye løp eller produkter etableres. |
| P6 Lag digitale løsninger som støtter samhandling | Svært høy | Caset er et direkte samhandlingscase mellom forvaltningsnivåer. |
| P7 Sørg for tillit til oppgaveløsningen | Svært høy | Uten tydelig autorisasjon, sporbarhet og styring blir ikke mønsteret brukbart i praksis. |

**Oppsummering av prinsippvurdering**

Caset støtter i stor grad prinsippene om deling, gjenbruk og samhandling, men det er også en viktig spenning mot P2 og P7: hvis det nasjonale mønsteret blir for generelt, vil det gi svak styringsverdi; hvis det blir for detaljert uten avklart ansvar og tilgangsstyring, vil tilliten svekkes.

## 7. Produktvurdering

### 7.0 Vurderingsrekkefølge

Produktene er vurdert i denne rekkefølgen, i tråd med oppdatert instruks:

1. identitet og representasjon
2. datadeling og integrasjon
3. hendelser og meldinger
4. dialog og brukerflate
5. register og datagrunnlag
6. katalog og semantikk
7. sektorprodukter og domeneprodukter

### 7.1 Vurderte produkter fra katalogen

| Kategori | Ressurs | Ressurs-ID | Vurdering | Begrunnelse |
|---|---|---|---|---|
| Identitet og representasjon | Maskinporten | `DIGDIR-002` | Brukes direkte | Relevant for sikker maskin-til-maskin tilgang til API-er og datakilder i målbilde og overgangsløp. |
| Identitet og representasjon | Altinn Autorisasjon | `DIGDIR-004` | Brukes direkte | Relevant der rettigheter og representasjon mellom aktører må håndteres mer presist enn ren teknisk autentisering. |
| Datadeling og integrasjon | data.altinn.no | `DIGDIR-015` | Ikke relevant | Mer relevant for kontrollert API-delingsmønster i andre typer delingsløp enn dette caset. Ikke nødvendig som kjernekomponent i første anbefaling. |
| Datadeling og integrasjon | FIKS-plattformen | `KS-001` | Ikke relevant | Kan være relevant i kommunal kontekst, men gir ikke et tilstrekkelig nasjonalt fellesmønster for kommune-stat-rapportering. |
| Datadeling og integrasjon | FINT Felleskomponent | `NOVARI-001` | Ikke relevant | Viktig i enkelte sektorløp, men ikke riktig som nasjonalt hovedmønster for dette caset. |
| Hendelser og meldinger | Altinn Events | `DIGDIR-010` | Brukes direkte | Sterk kandidat for varsling om endringer og for å redusere behovet for tidsstyrt polling og batchbasert rapportering. |
| Hendelser og meldinger | Altinn Formidling | `DIGDIR-008` | Brukes direkte | God overgangsløsning der fil- eller dokumentbasert utveksling fortsatt trengs før mottaker er klar for full API-/hendelsesmodell. |
| Hendelser og meldinger | eFormidling | `DIGDIR-007` | Ikke relevant | Har verdi i andre samhandlingsløp, men er ikke det mest treffsikre hovedmønsteret her gitt eksisterende Digdir-retning rundt Altinn-komponentene. |
| Dialog og brukerflate | Dialogporten | `DIGDIR-020` | Ikke relevant | Caset er primært system-til-system og ikke først og fremst en dialog- eller brukerflateproblemstilling. |
| Register og datagrunnlag | Enhetsregisteret | `BRREG-003` | Brukes direkte | Kan støtte identifisering av virksomheter og organisasjoner i rapporteringskjeden, men er ikke alene løsningen på caset. |
| Register og datagrunnlag | A-ordningen | `FLERE-001` | Ikke relevant | Relevante erfaringer, men ikke et produkt som direkte bør gjenbrukes som løsningskomponent i dette caset. |
| Katalog og semantikk | Felles datakatalog | `DIGDIR-011` | Brukes direkte | Egnet for synliggjøring av datasett, API-er og informasjonsmodeller som inngår i rapporteringsmønsteret. |
| Katalog og semantikk | Begrepskatalog | `DIGDIR-012` | Brukes direkte | Viktig for å etablere felles begreper for rapporteringsobjekter, hendelser og status. |
| Katalog og semantikk | API-katalog | `DIGDIR-013` | Brukes direkte | Viktig for å gjøre grensesnitt og forventede kontrakter synlige og gjenbrukbare. |
| Sektorprodukter og domeneprodukter | microdata.no | `SSB-001` | Ikke relevant | Relevans som analysemiljø, men ikke som hovedkomponent i operativ rapporteringssamhandling. |

### 7.2 Oppsummering

Det finnes et troverdig nasjonalt gjenbruksmønster allerede i porteføljen, men det er sammensatt:

- **Maskinporten** og eventuelt **Altinn Autorisasjon** dekker identitet, teknisk tilgang og representasjon.
- **Altinn Events** dekker varsling og hendelsesnær oppdatering.
- **Altinn Formidling** dekker et realistisk overgangsløp der filutveksling fortsatt må støttes.
- **Felles datakatalog**, **Begrepskatalog** og **API-katalog** dekker synliggjøring og semantisk/teknisk standardisering.

Det som mangler er ikke først og fremst et nytt generisk produkt, men et avtalt og gjenbrukbart mønster som binder disse delene sammen i rapporteringskontekst.

### 7.3 Eksplisitte mangler og behov for nye eller sammensatte løsninger

Følgende mangler er tydelige i caset:

- Det mangler en felles informasjonsmodell for rapporteringshendelser, rapporteringsobjekter og statusoverganger.
- Det mangler et tydelig nasjonalt mønster for når rapportering bør skje som hendelse, når data bør hentes via API, og når filbasert utveksling fortsatt er akseptabelt.
- Det mangler avklart autorisasjonsmodell for hvem som kan eksponere, hente, videredele eller representere rapporteringsdata.
- Det mangler tilstrekkelig samordnet mottaksmodenhet hos statlige aktører til å gjøre samme moderniseringsspor realistisk i flere løp samtidig.

### 7.4 Sammensatte løsningsmønstre

**Mønster A: Hendelsesvarsling med sikker uthenting**

- Altinn Events varsler at rapporteringsrelevant data er oppdatert eller tilgjengelig.
- Mottaker bruker Maskinporten for sikker maskin-til-maskin tilgang.
- Altinn Autorisasjon brukes der representasjon og rettigheter må uttrykkes mer presist.
- API-katalog, Begrepskatalog og Felles datakatalog brukes for å beskrive grensesnitt, begreper og datagrunnlag.

Dette er det sterkeste langsiktige mønsteret i caset.

**Mønster B: Kontrollert overgang fra fil til hendelser og API**

- Altinn Formidling brukes for asynkron overføring i løp som ennå ikke er klare for full API-basert uthenting.
- Maskinporten brukes fortsatt for sikker integrasjon der det er relevant.
- Semantikken standardiseres parallelt i Begrepskatalog og Felles datakatalog.
- Mottakere kan senere flytte samme løp over til Mønster A uten å starte på nytt med semantikk og styring.

Dette er det mest realistiske overgangsmønsteret.

## 8. Tiltak prioritert etter effekt

### 8.0 Gap-type per tiltak

| Tiltak | Primær gap-type | Begrunnelse |
|---|---|---|
| Etablere felles begreps- og informasjonsmodell for rapporteringshendelser | Semantisk gap | Dette er nødvendig for at samme samhandlingsmønster skal kunne brukes på tvers av flere løp. |
| Definere nasjonalt referansemønster for hendelse, API-henting og overgang til formidling | Produktgap | Caset mangler en tydelig arkitektonisk pakke eller anbefalt kombinasjon av eksisterende ressurser. |
| Avklare autorisasjons- og rettighetsmodell mellom kommune, leverandør og statlig mottaker | Juridisk gap | Tilgangsgrunnlag og representasjon er ikke avklart nok. |
| Samordne mottaksmodenhet og prioriterte pilotløp med statlige mottakere | Samordningsgap | Modernisering stopper uten koordinert mottakerside og forpliktelse til samme retning. |
| Bruke Altinn Formidling som definert overgangsmønster der API-/hendelsesløp ikke er modne | Produktgap | Dette reduserer behovet for særmønstre og gir mer kontrollert overgang. |

### Prioritert liste

1. **Etabler felles semantisk kjerne for rapportering.**
   Dette er det viktigste førstegrepet fordi både hendelser, API-er og filutveksling blir svake uten felles begreper, objekter og statusforståelse.

2. **Beslut et nasjonalt samhandlingsmønster med to spor.**
   Spor 1 bør være hendelsesvarsling kombinert med sikker uthenting. Spor 2 bør være kontrollert formidling som overgangsmønster.

3. **Avklar autorisasjon og ansvarskjeder tidlig.**
   Dette må skje før det investeres tungt i teknisk modernisering, ellers blir løsningen vanskelig å skalere.

4. **Velg ett til to pilotløp med høy verdi og realistisk mottaksmodenhet.**
   Pilotene bør brukes til å validere både semantikk, tilgangsstyring og kombinasjonen av Altinn Events, Maskinporten og katalogressursene.

5. **Bruk katalog- og semantikkressursene systematisk i pilotene.**
   Dette gjør at læringen kan gjenbrukes videre og ikke blir låst til ett enkelt løp.

## 9. Strategisk vurdering

Strategisk peker caset mot at Norge allerede har mange av de tekniske og arkitektoniske byggesteinene som trengs, men at de ikke ennå er bundet sammen til et tydelig og styrbart mønster for kommune-stat-rapportering. Det taler mot å starte med ny produktutvikling og for å starte med samordnet bruk av eksisterende ressurser kombinert med sterkere semantisk og organisatorisk styring.

Det er også viktig å unngå to feilspor:

- å gjøre caset for teknisk, slik at semantikk og styring kommer for sent
- å gjøre caset for generelt, slik at ingen faktisk overgang blir prioritert og testet

Den beste strategien er derfor å definere et konkret nasjonalt referansemønster med én tydelig overgangsbane og én tydelig målarkitektur.

## 10. Konklusjon

Det finnes et godt grunnlag for å modernisere rapportering mellom kommune og stat uten å starte med en ny nasjonal plattform. Den mest robuste retningen er å bruke:

- **Altinn Events** for hendelsesnær varsling
- **Maskinporten** og ved behov **Altinn Autorisasjon** for sikker tilgang og representasjon
- **Altinn Formidling** som kontrollert overgangsløsning der filutveksling fortsatt er nødvendig
- **Felles datakatalog**, **Begrepskatalog** og **API-katalog** for standardisering og synliggjøring

De største hindringene ligger i semantikk, autorisasjon og samordning, ikke i fravær av enkeltprodukter. Videre arbeid bør derfor fokusere på å pakke eksisterende ressurser inn i et gjenbrukbart nasjonalt rapporteringsmønster.

### 10.1 Spørsmål til videre diskusjon

1. Hvilke rapporteringsløp egner seg best som første pilot for hendelsesvarsling kombinert med API-henting?
2. Hvilke statlige mottakere er mest modne for å gå bort fra filmottak som hovedmønster?
3. Hvilke begreper og informasjonsobjekter må standardiseres først for å få effekt på tvers av flere løp?
4. Når er Altinn Formidling en riktig overgangsløsning, og når vil den bare forlenge et filbasert mønster?
5. Hvem bør eie og forvalte et nasjonalt referansemønster for denne typen rapportering?
