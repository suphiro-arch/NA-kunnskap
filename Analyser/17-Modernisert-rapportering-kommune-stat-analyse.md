# Arkitekturassistert analyse: Modernisert rapportering kommune-stat

**Status:** Analyse (tidlig utkast basert på workshop 8. april 2026)  
**Dato:** 2026-04-09  
**Basert på:** Standardinstruks for arkitekturassistert analyse  
**Kilder:** Kapabilitetsmodell, prinsipper, produktnummerering, og 8 produktbeskrivelser

---

## Kortversjon for ledelse (Executive Summary)

Vertskaptet har et modent og fokusert problemrom: **overgangen fra manuell årlig rapportering kommune-stat til kontinuerlig hendelsesdrevet datadeling.** Casen har høy strategisk relevans fordi den knytter til tre arkitekturprinsipper (P4, P6, P7) og adresserer både administrative besparelser og datakvalitet.

**Anbefalingen er en **Hybrid hendelsesdrevet API-modell (Spor A+B)** som kombinerer eksisterende felleskomponenter:**

| Rolle | Produkt | Argument |
|---|---|---|
| **Hendelsespublisering** | Altinn Events (DIGDIR-010) | Notification-first-mønster; 90-dagers lagring; pub/subscribe |
| **Maskin-autentisering** | Maskinporten (DIGDIR-002) | Kjerne for sikre API-oppslag mellom systemer |
| **Overgangsløsning** | Altinn Formidling (DIGDIR-008) | For områder der API ikke er klar; automatisk pakking av data |
| **Metadataforvaltning** | Felles datakatalog + Begrepskatalog + API-katalog | Semantisk grunnlag og oversikt over dataressurser |

**Primærfordeler:**
- Eliminerer manuelle rapporteringstopper; rapportering blir kontinuerlig
- Validering ved kilden reduserer etterarbeid og datakvalitet
- Notification-first-mønster minimerer datafluks av sensitive detaljer
- Kommunal innovasjon enableres ved sanntidstilgang til strukturert data

**Kritiske forutsetninger:**
- SSB må være villig til å gå fra filmottak til API-oppslag
- Dialog med statlige IT-arkitekter om volumhåndtering
- Felles begrepsmodell må være etablert for "hendelse" og rapporterte fenomener

**Neste steg:** Pilot på barnevern eller helsetjenester for å validere tidsbesparelser og tekniske antakelser.

---

## 1. Formål

Denne analysen skal:
- Gi beslutningsgrunnlag for overgang fra dagens rapporterings-modell til modernisert hendelsesdrevet datadeling mellom kommuner og staten
- Identifisere relevante eksisterende produkter og deres rollen i løsningen
- Avklare mangler som krever nyutvikling eller juridisk oppklaring
- Prioritere tiltak basert på effekt og beredskap

---

## 2. Input / casebeskrivelse

**Utgangspunkt:** Tidlig utkast fra workshop 8. april 2026

**Dagens situasjon:**
- Kommuner sender årlige eller periodiske manuelle rapporter til staten (SSB/direktorater)
- Rapportering baseres på uttak fra kommunale fagsystemer
- Stor administrativ byrde ved årsslutt
- Data valideres først når de er mottatt av staten
- Datakvalitetsproblemer genererer etterarbeid både i kommune og stat

**Ønsket framtidstilstand:**
- Hendelsesdrevet datadeling hvor kommunale fagsystemer publiserer hendelser når noe skjer
- Staten gjør API-oppslag basert på notifikasjoner for å hente detaljer
- Lokal validering av data mens sakene er «ferske»
- Kontinuerlig rapportering gjennom året, ikke samlet årsstokking
- Mulighet for kommunal innsikt og innovasjon basert på samme data i sanntid

**Foreslåtte spor:**
- **Spor A+B (anbefalt):** Hendelsespublisering + API-oppslag  
- **Spor C (overgang):** Automatisert pakking og innsending av komplette datasett  

---

## 2.1 Inputgrunnlag og analysetillit

| Vurderingspunkt | Vurdering |
|---|---|
| Inputgrunnlag | Workshop-utkast med tydelig målbilde, aktører og hovedforløp, men begrenset dokumentert kildemateriale utover caseteksten |
| Datagrunnlag | Begrenset for kvantifisering av effekter og volum; godt for overordnet arkitekturretning |
| Produktgrunnlag | Sterkt; analysen bygger på eksisterende produktkatalog og konkrete produktbeskrivelser |
| Samlet analysetillit | Middels |

Viktigste usikkerheter:
- SSBs faktiske veikart og beredskap for API-oppslag i stedet for filbasert mottak
- Manglende felles semantisk modell for rapporteringshendelser og obligatoriske felt
- Uavklart autorisasjonsmodell for detaljert tilgang til data på tvers av aktører

---

## 3. Målgruppe og styringsnivå

| Aktør | Rolle | Styringsnivå |
|---|---|---|
| **Saksbehandler i kommune** | Oppfatter som enkel registrering uten ekstra rapporteri | Operativ |
| **Kommune (leder/datafm)** | Ønsker innebygd kvalitetssikring og egen tilgang til data | Taktisk |
| **Statlige mottaker** (SSB/Direktorat) | Trenger stabil, høykvalitetsdatastrøm med minimalt manuelt arbeid | Strategisk & operativ |
| **Integrasjonsplattform** (staten) | Ansvar for infrastruktur, sikkerhet, autorisasjon | Operativ |
| **DIGDIR / Arkitekturforum** | Skal sikre gjenbruk og nasjonale standarder | Strategisk |

---

## 4. Problembilde

| Problem | Dagens symptom | Årsak |
|---|---|---|
| **Administrativ byrde** | Store årsavslutningstopper for rapportering | Manuelle uttrekk og manuell validering av ferdig data |
| **Datakvalitet** | Mange feil oppdages for sent (av staten) | Validering skjer lang tid etter registrering; kilden har ikke korrigert |
| **Informasjonsfluks** | Massive datamengder sendes på utsatt datodels | Ingen hendelsesfiltrering; alt sendes («full dump») |
| **Datafragmentering** | Samme data lagres flere steder | Kommune har ikke tilgang til sitt eget aggregerte data; stat må lagre parallelt |
| **Innovasjonshinder** | Kommune kan ikke bruke egne rapportdata til egen analyse i sanntid | Data blir tilgjengelige for kommunal bruk 1 år senere, hvis i det hele tatt |
| **Systemavhengighet** | Hver statlig mottaker krever egne uttrekk | Ingen standardisert grensesnitt towards kommunal fagsystemer |

---

## 5. Kapabilitetsanalyse

| Kapabilitet | Relevans | Hvordan dekkes | Gap? |
|---|---|---|---|
| **Datautveksling og integrasjon: Dele data med andre** | HØY | Altinn Events (hendelsespublisering), Maskinporten (sikker API-eksponering) | Samordning av kommunale fagsystemer rundt standardiserte grensesnitt |
| **Datautveksling og integrasjon: Bruke data fra andre** | HØYS | API-oppslag via Maskinporten; staten henter data når hendelse publiseres | Statlig mottak må redesignes fra passiv mottaker til aktiv konsument |
| **Datautveksling og integrasjon: Hendelsesdrevet** | **KJERNE** | Altinn Events er direkte løsning for publish/subscribe | Spørsmål: Skal alle kommunale data-hendelser gå gjennom Altinn Events, eller skal noen kommuner/systemer bruke FINT Felleskomponent? |
| **Datautveksling og integrasjon: Meldingsformidling** | MEDIUM | Altinn Formidling (Spor C overgang) for områder som ikke har API klar | Begrenset til overgang; ikke primær løsning |
| **Informasjonsforvaltning: Informasjonsarkitektur** | HØY | Begrepskatalog + FINT Informasjonsmodell gir semantisk grunnlag | **Gap:** Felles begrepsmodell for "hendelse" mangler; krever arbeidsgruppe |
| **Informasjonsforvaltning: Oversikt over API** | MEDIUM | API-katalog skal synliggjøre kommunale API-er som del av nasjonal løsning | **Gap:** Kommune-API-er må registreres og klassifiseres i katalog |
| **Informasjonsforvaltning: Datastyring** | HØY | Felles datakatalog for registrering av kommunale datasett og deres karakteristikker | **Gap:** Kommuner må etablere rutiner for registrering og vedlikehold av metadata |
| **Tillit: Autentisering** | **KJERNE** | Maskinporten for maskin-til-maskin sikring av API-oppslag | **Forutsetning som ligger fast:** Maskinporten må være på plass før API-oppslag kan starte |
| **Tillit: Tilgangskontroll** | HØY | Altinn Autorisasjon via Altinn Events; Maskinporten scopes for API | **Gap:** Detaljert autorisasjonsmodell for hvem som får hente hvilke data mangler |
| **Standardisering: Forvaltningsstandarder** | HØY | Felles datakatalog, begrepskatalog og API-katalog er normerende | **Gap:** Rapporteringsstandard for hendelser og datamodell for kommunale fagsystemer må utarbeides |

**Konklusjon på kapabilitetsdel:** Casen dekkes stort sett av eksisterende kapabiliteter, men med **to kritiske semantiske gap:**
1. Felles begrepsmodell for hendelse, registrering og rapportering
2. Detaljerte autorisasjonsmodeller for hva som kan deles

---

## 6. Prinsippvurdering

| Prinsipp | Vurdert mot casesenarioet | Hvordan støttes | Konflikt? |
|---|---|---|---|
| **P1: Ta utgangspunkt i brukernes behov** | Saksbehandler skal oppleve enkel registrering uten ekstra rapporteri; Kommune skal få tilgang til egne data; Stat skal få pålitelig datakilde | Hendelsesdrevet modell pilotter validering ved source; innebygd i fagsystemet | OK |
| **P2: Ta arkitekturbeslutninger på rett nivå** | Valg av hendelsestjeneste og API-modell er nasjonalt; imple lokalt | DIGDIR fastsetter standarder via Altinn Events + Maskinporten; Kommuner velger implementering | OK |
| **P4: Del og gjenbruk data** | **Kjerne:** Data skal deles kontinuerlig, ikke årlig; samme data for statsreportering OG kommunal analyse | Notification-first-mønster gjør data tilgjengelig for flere formål | **Sterk støtte** |
| **P5: Del og gjenbruk løsninger** | Felleskomponenter (Altinn Events, Maskinporten, kataloger) skal brukes i stedet for kommune-spesifikke løsninger | Anbefaling går på gjenbruk av eksisterende produkter | **Sterk støtte** |
| **P6: Lag digitale løsninger som støtter samhandling** | Hendelsesdrevet arkitektur muliggjør at andre autorisertin aktører kan abonnere på samme hendelser | Pub/subscribe-modell i Altinn Events tillater fleksibel ekspansjon av mottakere | **Sterk støtte** |
| **P7: Sørg for tillit til oppgaveløsningen** | Sikkerhet må være innebygd; sporbarhet på validering og levering; kvittering på rapporteringsplikten oppfylt | Maskinporten sikrer maskinell tilgang; Altinn Events logger; Altinn Autorisasjon kontrollerer tilgang | **Sterk støtte** |

**Konklusjon:** Casen **understøtter P4, P6 og P7 direkte.** Det er høy kongruens mellom ønsket løsning og arkitekturprinsippene.

---

## 7. Produktvurdering

### 7.1 Vurderingsrekkefølge

Iht. obligatorisk arbeidsmåte vurderes produktkategoriene i denne rekkefølgen:
1. **Identitet og representasjon** → Ingenting relevant
2. **Datadeling og integrasjon** → Altinn Events, Maskinporten, eFormidling, Altinn Formidling
3. **Hendelser og meldinger** → Altinn Events (kjerneprodukt)
4. **Dialog og brukerflate** → Ingenting direkte relevant for denne casen
5. **Register og datagrunnlag** → Implisitt via kommunale fagsystemer (ikke egen produkt i registeret)
6. **Katalog og semantikk** → Felles datakatalog, Begrepskatalog, API-katalog
7. **Sektorprodukter** → FINT Felleskomponent, Fiks-plattformen (kommunal side)

---

### 7.2 Detaljert produktvurdering

#### **Datadeling og integrasjon**

##### **DIGDIR-010: Altinn Events**
**Status:**  ✅ **BRUKES DIREKTE** (Spor A – Hendelsespublisering)

**Begrunnelse:** 
- Produktbeskrivelsen viser tydelig support for pub/subscribe-mønster, CloudEvents, filtrering, webhook-levering og retry
- 90-dagers lagringsperiode gir robusthet
- Autorisasjonsmodellen går gjennom Altinn Autorisasjon
- Hendelsesformatet er standardisert (CloudEvents)

**Vurderingsstøtte:** 
- Full produktbeskrivelse (DIGDIR-010) som viser etablert funksionalitet
- Modenhet: Høy funksjonell modenhet, etablert i produksjon
- Tillit: Høy – produktet er aktivt brukt i Altinn-økosystemet

**Kritiske spørsmål for implementering:**
- Skal alle kommunale hendelser gå gjennom Altinn Events, eller bare rapporteringshendelser?
- Hva defineres som «tilstandsendring» som skal generere notifikasjon?
- Skalabilitet ved høyt volum (X-antall kommuner)?

---

##### **DIGDIR-002: Maskinporten**
**Status:**  ✅ **BRUKES DIREKTE** (Spor B – Sikker API-autentisering)

**Begrunnelse:**
- Produktbeskrivelsen viser etablert mønster for maskin-til-maskin-autentisering
- Token-basert tilgang; scope-modell for differensiert tilgang
- Dokumentert onboarding og test-/produksjonsløp
- Inngår i nasjonal tillitsinfrastruktur

**Vurderingsstøtte:**
- Full produktbeskrivelse (DIGDIR-002) som viser scope-model and token lifecycle
- Modenhet: Høy; brukes allerede på tvers av virksomheter
- Tillit: Kjerne-felleskomponent for sikkerhet

**Kritiske spørsmål for implementering:**
- Hvilke scopes skal defineres? (Én per rapporttype? Én per kommune?)
- Hvem administrerer systembrukere på kommunal side?
- Hvordan håndteres tilgangsrevokering hvis et system må tas av drift?

---

##### **DIGDIR-008: Altinn Formidling**
**Status:** ✅ **BRUKES DIREKTE** (Spor C – Overgangsløsning)

**Begrunnelse:**
- Produktbeskrivelsen viser support for ende-til-ende filoverføring, logging, varsling
- API-tilgang for automatisert innsending
- Relevant for områder der kommunale fagsystemer ennå ikke kan eksponere API
- Alternativ til manuell innsending via Altinn eller direktekontakt

**Vurderingsstøtte:**
- Full produktbeskrivelse (DIGDIR-008); høy funksjonell modenhet
- Etablert i produksjon
- Kjent bruksmodell for formidling av komplette datasett

**Rolle i løsningen:**
- **Overgangsløsning,** ikke primærmål
- For kommuner/systemer som ikke har ressurser til API-implementering på kort sikt
- Skal gradvis erstattes av Spor A+B når API-beredskapen øker

**Kritiske spørsmål:**
- Hva er akseptregime for innsending av større datasett?
- Er 90-dagers retensjonsperiode tilstrekkelig?
- Hvordan koordineres Spor C-tilbakemeldinger om feil?

---

##### **DIGDIR-007: eFormidling**
**Status:** ❌ **IKKE RELEVANT** (primært)

**Begrunnelse:**
- eFormidling er relevant for meldingsutveksling **mellom virksomheter** og **til innbyggere**
- Casen handler om maskinell datadeling, ikke menneskerettet kommunikasjon
- eFormidling er for komplette meldinger/dokumenter, ikke for hendelsesnotifikasjoner
- For rapporteringsfølgene passer Altinn Formidling (filoverføring) eller API-oppslag bedre

**Ikke relevant for:** Hendelsesflyten i denne casen

---

##### **DIGDIR-004: Altinn Autorisasjon**
**Status:** ✅ **BRUKES INDIREKTE** (Tilgangskontroll)

**Begrunnelse:**
- Altinn Events bruker Altinn Autorisasjon for å styre hvem som kan publisere og abonnere
- Må konfigureres med policyer for rap-behovet
- Inngår som del av Altinn Events-implementeringen

**Rolle:** Infrastruktur, ikke separat produkt å velge

---

#### **Hendelser og meldinger**

**Kun Altinn Events relevant; allerede vurdert ovenfor.**

---

#### **Katalog og semantikk**

##### **DIGDIR-011: Felles datakatalog**
**Status:** ✅ **BRUKES DIREKTE** (Metadataforvaltning)

**Begrunnelse:**
- Produktbeskrivelsen viser støtte for registrering og høsting av metadata
- Relevante delkataloger: datasett, API, begreper, informasjonsmodeller
- Nasjonal fellesløsning for oppdagelse og beskrivelse

**Rolle i løsningen:**
- Kommunale datasett registreres (f.eks. «Barn i kommunal omsorg» som datasett)
- Rapporterings-API-er registreres i API-katalog
- Gjør det mulig for staten å oppdage tilgjengelige data

**Kritiske spørsmål:**
- Hvem ansvarlig for å registrere kommunale datasett? (Kommune, DIGDIR, SSB?)
- Hva er metadata-minimumnivå for en rapporting-hendelse?

---

##### **DIGDIR-012: Begrepskatalog**
**Status:** ✅ **BRUKES DIREKTE** (Semantisk grunnlag – **GAP identifisert**)

**Begrunnelse:**
- Produktbeskrivelsen viser support for strukturert begrepsbeskrivelse
- Brukes til å unngå semantiske misforståelser når data deles
- Relevant for nasjonale rapporteringsstandaroder

**Rolle i løsningen:**
- Sentrale rapporterbegreper må beskrives (f.eks. «vedtak», «undersøkelse», «tjeneste»)
- Staten og kommuner må konverge på samme definisjon

**GAP:** 
- Iødig felles begrepskatalog spesifikt for rapporting kommune-stat finnes **ikke** i dag
- Må etableres som arbeidsgruppe med SSB, kommunepartner, direktorat

---

##### **DIGDIR-013: API-katalog**
**Status:** ✅ **BRUKES DIREKTE** (API-synliggjøring)

**Begrunnelse:**
- Produktbeskrivelsen viser at API-er registreres som delkatalog i Felles datakatalog
- Kommunale rapporterings-API-er skal være synlige her
- Gir staten og andre aktører oversikt

**Rolle i løsningen:**
- Kommunale fagsystemer som har hendelsespublikering vil dermed eksponere API-er
- Disse skal registreres i API-katalog

---

#### **Sektorprodukter**

##### **NOVARI-001: FINT Felleskomponent**
**Status:** ⚙️ **VIDEREUTVIKLES / MULIG ALTERNATIV** (for fylker)

**Begrunnelse:**
- Produktbeskrivelsen viser etablert hendelsesdrevet integrasjon i fylkeskommunal sektor
- Gir API-basert deling og informasjonsarkitektur
- FINT Informasjonsmodell (NOVARI-003) er semantisk grunnlag

**Rolle i løsningen:**
- **For fylkeskommuner** som deltar i rapportering: FINT kan være alternativ til ren Altinn-events
- **Spørsmål:** Skal fylker bruke FINT eller må de også koble seg til Altinn Events for statsrapportering?
- **Interdependens:** Om FINT skal brukes, må data-hendelser mapper fra FINT → Altinn Events

**Klassifisering:**
- Ikke primær løsning for denne casen (som er kommune+stat)
- Bruk kun hvis fylker har eget behov og kan bridges til nasjonalt løp

---

##### **KS-001: Fiks-plattformen**
**Status:** ⚙️ **MULIG ALTERNATIV** (Integrasjonsplattform kommunal side)

**Begrunnelse:**
- Produktbeskrivelsen viser Fiks som kommunal integrasjonsplattform
- Kunne ha fungert som kommunalt mellomlag for datadeling
- KS-002 (Fiks Melding) og KS-007 (SvarInn) er meldingsløsninger

**Rolle i løsningen:**
- **Ikke anbefalt som primær:** Altinn Events og Maskinporten er nasjonale standarder
- **Mulig lokalt:** Kan brukes som mellomlag i kommuner som allerede er på Fiks
- **Risk:** Fragmentering hvis noen bruker Fiks og noen bruker Altinn Events direkte

**Klassifisering:** 
- Ikke primær løsning; legger til kompleksitet
- Anbefaling: Kommune kobler fagsystem til Altinn Events direkte

---

### 7.3 Oppsamt produktvurderingstabell

| Ressurs-ID | Navn | Klassifisering | Begrunnelse | Tillit |
|---|---|---|---|---|
| **DIGDIR-010** | Altinn Events | ✅ Brukes direkte | Kjernprodukt for hendelsespublisering; høy modenhet | Høy – full produktbeskrivelse |
| **DIGDIR-002** | Maskinporten | ✅ Brukes direkte | Kjernprodukt for sikker API-auth; etablert standard | Høy – kjerne felleskomponent |
| **DIGDIR-008** | Altinn Formidling | ✅ Brukes direkte | Overgangsløsning for områder uten API-beredskap | Høy – etablert produkt |
| **DIGDIR-011** | Felles datakatalog | ✅ Brukes direkte | Metadataforvaltning og oppdagelse | Høy – etablert standard |
| **DIGDIR-012** | Begrepskatalog | ✅ Brukes direkte | Semantisk grunnlag; **GAP** på rapportingsbegreper | Høy – produktet finnes, men spesifikk innhold mangler |
| **DIGDIR-013** | API-katalog | ✅ Brukes direkte | Synliggjøring av kommunale API-er | Høy – del av Felles datakatalog |
| **DIGDIR-004** | Altinn Autorisasjon | ✅ Brukes indirekte | Del av Altinn Events infrastruktur | Høy – kjerne tillitstjeneste |
| **DIGDIR-007** | eFormidling | ❌ Ikke relevant | Ikke for maskinell hendelsesflyten | – |
| **NOVARI-001** | FINT Felleskomponent | ⚙️ Videreutvikles | Alternativ for fylker; bridging til nasjonalt løp | Medium – sektor-spesifikk |
| **KS-001** | Fiks-plattformen | ❌ Ikke primær | Fragmentering hvis brukt parallelt med Altinn | Medium – lokalt alternativ |
| **KS-002** | Fiks Melding | ❌ Ikke relevant | For formidling, ikke hendelser | Low – annat domene |

---

## 8. Identifiserte mangler (gap-analyse)

### 8.1 Produktgap

| Gap | Beskrivelse | Alvorlighet | Løsning |
|---|---|---|---|
| **Ingen nasjonal rapporte-ringsstandardisering** | Det finnes hendelse- og katalogprodukter, men ikke eksplisitt rapporterings-standard med datamodell | HØYT | Arbeidsgruppe: SSB + kommune + Direktorat + DIGDIR skal utarbeide standard for kommunal rapportvedhendelse og påkrevd metadata |
| **Ingen dedikert kommunal tilpasning av Alterninger Events** | Altinn Events ble designet som generell pub/sub; mangler guider for rapportingsbruk | MEDIUM | Dokumentasjon + implementeringsstudie |

---

### 8.2 Semantisk gap

| Gap | Beskrivelse | Alvorlighet | Løsning |
|---|---|---|---|
| **Felles begrepsmodell mangler** | Begreper som «hendelse», «registrering», «rapportpliktig fenomen» har ikke felles definisjon | HØYT | **Gap tiltakstype:** Semantisk gap. Krever arbeidsgruppe med arkitekter og fagfolk fra kommune + stat |
| **Informasjonsmodell for rapport-data mangler** | Hvilke felt skal være obligatorisk? Hva er kontrollregler? Hva er KOSTRA-regler? | HØYT | **Gap tiltakstype:** Semantisk gap + Standardiseringstap |

---

### 8.3 Juridisk/Organisatorisk gap

| Gap | Beskrivelse | Alvorlighet | Løsning |
|---|---|---|---|
| **SSBs bereitskap til API-oppslag** | SSB er i dag «filmottaker»; overgang til pull-modell krever nye prosesser | HØYT | Dialog med SSB om veikart for overgang fra «filmottak» til maskinell API-oppslag; avklare SLA og rapporteringsrytme |
| **Autorisasjonsmodell** | Hvem får se hvilke data? Granularitet? Revisjonslogg? | HØYT | Arbeidsgruppe skal definere autorisasjonsmatriser |
| **Dataeierskap og vedlikehold** | Hvem ansvarlig for å registrere metadata i Felles datakatalog? | MEDIUM | Rolleavklaring: Kommune, DIGDIR eller SSB? |

---

### 8.4 Samordningsgap

| Gap | Beskrivelse | Alvorlighet | Løsning |
|---|---|---|---|
| **Kommunal API-beredskap varierer** | Ikke alle Kommune-fagsystemer kan eksponere API i dag | HØYT | Spor C (Altinn Formidling) som overgangsløsning; gradvis API-implementering |
| **Statlig mottakskapasitet** | Statlig side må ha kapasitet til å håndtere kontinuerlig hendelsesstrøm | HØYT | KTV arkitekter, SSB, direktorater skal kartlegge kapasitet og design konsumentsiden |

---

## 9. Tiltak prioritert etter effekt

### 9.1 Prioriteringsmatrise

**Priortering:** Effekt × Avhengighet × Tidsfrist

| Prioritet | Tiltak | Gap-type | Effekt | Avhengighet | Tidslinje | Ansvarlig |
|---|---|---|---|---|---|---|
| **P1** | Pilot: Hendelsesdrevet rapportering (Spor A+B) på ett domene (f.eks. barnevern eller HLT) | Samordning + Semantikk | Validere tidsbesparelser; tette semantisk gap | SSB-samarbeid | Q2-Q3 2026 | Kommune partner + SSB + DIGDIR |
| **P1** | Arbeidsgruppe: Felles rapportingsbegreper og datamodell | Semantikk | Etablere felles grunnlag | Høy | Q2 2026 start | Direktorat + SSB + Kommune + arkitekter |
| **P1** | Dialog: SSB veikart for API-oppslag | Juridisk/Org | Sikre staten er villig til å endre | Kritisk | Q2 2026 | DIGDIR + SSB + Direktorat |
| **P2** | Implementeringsstudie: Altinn Events + Maskinporten konfigurl for rapportering | Produktgap + Semantikk | Klargjøre teknisk løp | Medium | Q2 2026 | DIGDIR + tekniske partner |
| **P2** | Autorisasjonsmodell: Definiser hvem ser hva | Juridisk/Org | Sikre tilgang styres riktig | Høy | Q2-Q3 2026 | Lovavdeling + arkitekter + Kommune |
| **P3** | Overgangsstrategi: Spor C (Altinn Formidling) for områder uten API | Samordning | Sikre alle kan delta | Medium | Q3 2026 | Kommune + DIGDIR |
| **P3** | Registrering av kommunale datasett i Felles datakatalog | Samordning | Transparensering av tilgjengelige data | Medium | Q3 2026 løpende | Kommune + DIGDIR |
| **P4** | Veiledning og innføringsstøtte for kommuner | Samordning | Redusere gjennomføringskompleksitet | Medium | Q3-Q4 2026 | KS/DIGDIR + UU team |

---

### 9.2 Kritisk sti

```
Q2 2026:
  └─ Arbeidsgruppe: Begreper + datamodell STARTES
  └─ Dialog SSB: Veikart for API AVSLUTTES med avklaringer
  └─ Implementeringsstudie: Teknikk PÅBEGYNNES

Q2-Q3 2026:
  └─ Pilot STARTER på ett domene (barnevern eller HLT)
  └─ Autorisasjonsmodell UTARBEIDES

Q3 2026:
  └─ Pilot RESULTAT: Tidsbesparelser dokumenteres
  └─ Spor C overgang-strategi TAS I BRUK for områder uten API

Q4 2026:
  └─ Skala fra pilot til flere domener
  └─ Gradvis API-implementering i Kommune-fagsystemer
```

---

## 10. Strategisk vurdering

### 10.1 Risikoer

| Risiko | Sannsynlighet | Konsekvens | Håndtering |
|---|---|---|---|
| SSB ikke villig til API-oppslag; fortsetter med filmottak | Medium | HØYT – hele casen mislykkes | Avklaring allerede i Q2; kontingensplan for Spor C |
| Kommune-fagsystemer kan ikke implementere hendelsespublisering | Medium | HØYT – kan ikke skalere | Spor C som overgang; gradvis begrensning av Spor C over tid |
| Statlige IT-arkitekter ikke klare for høyt datavolu | Medium | MEDIUM – forsinkelse | Early dialog; volumveiledning; eventuelt throttling på hendelsesflyten |
| Semantisk uenighet på tvers av kommune/stat om rapportgebegreper | Høy | HØYT – implementeringstap | Arbeidsgruppe må ferdigstilles før implementering; arkitekt-governance |

### 10.2 Gevinster (potensial)

| Gevinst | Realiserbetingelse | Tidslinje |
|---|---|---|
| **Administrative besparelser** (50-80% reduksjon i rapporteringsarbeid) | Pilot viser tidsrealisering | Q3 2026 |
| **Datakvalitet** (færre etterarbeid, validering ved kilde) | Innebygd validering implementert | Q4 2026 |
| **Kontinuert rapportering** (ingen årsavslutningstopp) | Hendelsesflyt operativt | Q4 2026 |
| **Kommunal innovasjon** (egen tilgang til sanntidsdata) | API-tilgang til egne data gitt | Q4 2026 |

---

## 11. Konklusjon

### Anbefalte løsningsmønster

**Hybrid Hendelsesdrevet API-modell (Spor A+B):**

1. **Hendelsespublisering (Spor A):** Kommune publiserer lettvektsmeldinger via **Altinn Events** når tilstandsendring skjer
2. **API-oppslag (Spor B):** Staten henter detaljene på etterspørsel via **Maskinporten**-sikret API
3.  **Overgang (Spor C):** For områder der API ikke er klar: Automatisert pakking + innsending via **Altinn Formidling**

### Produktportefølje

| Område | Produkt | Rolle |
|---|---|---|
| **Hendelsesinfrastruktur** | Altinn Events (DIGDIR-010) | ✅ Kjernprodukt |
| **Sikker API-tilgang** | Maskinporten (DIGDIR-002) | ✅ Kjernprodukt |
| **Overgang** | Altinn Formidling (DIGDIR-008) | ✅ Overgangsløsning |
| **Metadataforvaltning** | Felles datakatalog (DIGDIR-011) | ✅ Katalogisering |
| **Semantikk** | Begrepskatalog (DIGDIR-012) | ⚙️ Må fylles med rapportingsbegreper |
| **API-synliggjøring** | API-katalog (DIGDIR-013) | ✅ Registrering |

### Kritiske forUtsetninger

1. **SSB-vilje:** Må være villig til å gå fra filmottak til API-oppslag (større organisatorisk endring)
2. **Semantisk avklaring:** Felles begrepsmodell må etableres før implementering
3. **Kommune-API-beredskap:** Varierer idag; krever gradvis oppgradering

### Neste steg

1. **Q2 2026:** Arbeidsgruppe startes; dialog med SSB; implementeringsstudie
2. **Q2-Q3 2026:** Pilot på ett domene (barnevern eller helsetjenester)
3. **Q3 2026:** Evaluering + skaleringsbeslutning

---

## 12. Vedlegg: Analyseforutsetninger og kilder

**Arbeidsmåte:** Obligatorisk strukturert analyse iht. `config/prompts/arkitekturassistert-analyse-av-utviklingsbehov.system.md`

**Kilder vurdert i rekkefølge:**
- ✅ `arkitektur/kapabiliteter/capabilities.yaml` (v.2026-02-27)
- ✅ `arkitektur/prinsipper/principles.md` (sju prinsipper)
- ✅ `arkitektur/ressurser/produktnummerering.md` (full register)  
- ✅ Produktbeskrivelser: DIGDIR-002, DIGDIR-007, DIGDIR-008, DIGDIR-010, DIGDIR-011, DIGDIR-012, DIGDIR-013, NOVARI-001, KS-001, KS-002

**Produktvurderinger basert på:**
- Full produktbeskrivelse (når tilgjengelig)
- Registrerte kapabilitetstreff
- Modenhet og tillit i katalogen

**Analyse ikke splittet:** Casen er enhetlig; alle deler av løsningen dreier seg om hendelsesdrevet datadeling kommune-stat. En splittet analyse ville svekket produktvurderingen.

---

**Analyse ferdigstilt:** 2026-04-09  
**Analyseansvarlig:** Arkitekturassistert analyse-verktøy  
**Status:** Klar for ledelsesdiskusjon og oppfølging
