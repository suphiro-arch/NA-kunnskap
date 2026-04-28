# Standardprompt: Operative ressurs-canvas

Formål: Sikre lik, detaljert og grundig utfylling av ressursbeskrivelser for operative løsninger og tjenester som brukes i arkitekturvurderinger, analyser og gjenbruk.

---

## Arbeidsgang

### Trinn 1: Les eksisterende versjon (VIKTIG!)
- **Hvis ressursbeskrivelse allerede finnes**: Les gjennom hele filen først
- **Hvis flere versjoner finnes**: Bygg videre på filen med høyest versjonsnummer som utgangspunkt, med mindre brukeren ber om noe annet
- Versjonsrekkefølgen gjelder på tvers av forfattere og modeller; høyeste versjon er siste versjon
- Dette gjelder også når siste versjon er laget av `copilot`: den skal leses, vurderes og brukes som primært utgangspunkt på lik linje med `codex`-filer
- Ikke hopp over siste versjon fordi forfatteren er en annen modell; bruk eldre versjoner bare som supplement når de gir nyttig historikk eller forklarer endringer
- Hvis eldre filer mangler versjonsnummer: behandle dem som historiske filer og bruk den faglig mest oppdaterte av dem som lesegrunnlag, men skriv nye leveranser etter den nye versjonsregelen
- Identifiser hvilke felt som er fylt ut, og hvilke som er merket `Usikkert:`
- Vurder hvilke seksjoner som kan forbedres, detaljeres eller utdypes
- **Mål:** Bygge videre på eksisterende jobb, ikke starte fra scratch

### Trinn 2: Vurder oppgavetyp
- **Forbedring av eksisterende:** Lage en revisjonert versjon (se navngivning)
- **Ny ressursbeskrivelse:** Starte fra mal + kilder

### Trinn 2B: Avklar forbedringsnivå (OBLIGATORISK ved revisjon)
- En forbedret versjon skal alltid inneholde både:
  1. **Analyseforbedring:** ny eller oppdatert kildegjennomgang med verifiserte fakta
  2. **Tekstforbedring:** bedre struktur, presisjon, språk og lesbarhet
- Ved tekstforbedring skal tone og språkføring fra siste versjon som hovedregel bevares når den allerede fungerer godt for målgruppen.
- Unngå unødvendig full omskriving av avsnitt som allerede er tydelige og presise; forbedre heller målrettet der analyse eller presisjon faktisk blir bedre.
- **Ikke godkjent forbedring:** kun språkvask, omformulering eller tabellformattering uten nytt analysegrunnlag
- Dokumenter kort hva som er nytt i analysen (nye kilder, nye funn, avklarte usikkerheter)

### Trinn 2C: v1-minstekrav (KVALITETSGATE)
En ressursbeskrivelse skal normalt ikke merkes som `v1` hvis ett eller flere av punktene under mangler:
1. `Hovedfunksjoner` har minst 3-4 forklarende avsnitt (ikke bare korte punkt).
2. `Hovedfunksjoner` inneholder både `Typiske brukssituasjoner (generisk)` og `Når <produktet> normalt ikke er førstevalg` når produktet brukes i analyser.
3. `Kapabiliteter` inneholder forklaring på *hvordan* produktet bidrar per kapabilitet, ikke bare opplisting av navn.
4. `Forretningsverdi/Verdiforslag` er delt i minst 3 målgruppe- eller interessentperspektiver.
5. `Gjenbruk` inkluderer `Vanlige kombinasjoner med andre produkter` når dette er relevant for arkitekturvurdering.

Hvis kildegrunnlaget ikke støtter dette nivået, behold dokumentet som `v0.x` til videre analyse er gjort.

### Trinn 3: Hent kilder (samme hver gang)
1. Mal: `config/templates/operative-ressurs-template.md`
2. Kapabiliteter: `arkitektur/kapabiliteter/capabilities.yaml` (kun navnene som finnes her)
3. Prinsipper: `arkitektur/prinsipper/principles.md` (bruk prinsippnavn og koblinger som finnes her)
4. Lenker: `sources/links.md` (lokal liste + aktive lenker til dokumentasjon)
5. Ressursregister, Ressurs-ID og Merknad: `arkitektur/ressurser/produktnummerering.md`
5. **Åpne kilder**: Digdir Docs, Samarbeidsportalen, felles-IKT, produkteier-nettsteder (f.eks. altinn.studio)
6. **URL-valg:** Bruk som hovedregel de konkrete URL-ene som allerede er listet i `sources/links.md` før du prøver bredere søk
7. **Utvid bare ved behov:** Gå utover `sources/links.md` kun hvis lenkene der er utilstrekkelige, utdaterte eller utilgjengelige, og dokumenter hvorfor

### Trinn 4: Skriv/forbedre innhold
Følg reglene under.

### Trinn 4A: Kontroller løsningsbredden (OBLIGATORISK)
- Før du skriver `Kort beskrivelse`, `Hovedfunksjoner`, `Scope og avgrensning` og `Type ressurs` i produktregisteret, skal du eksplisitt kontrollere om produktet består av mer enn én bruksmåte eller leveranseflate.
- Sjekk alltid minst disse vinklene når kildene finnes:
  1. **Brukerflate:** portal, webflate, manuelt arbeidsløp, selvbetjent løsning
  2. **Integrasjonsflate:** API, hendelser, maskin-til-maskin, filutveksling
  3. **Tjenesteflate:** sentral kanalhåndtering, saksflyt, regelmotor, distribusjon, oppslag, forvaltning
- Hvis produktet har både portal og API, eller både manuell og integrert bruk, skal dette beskrives eksplisitt. Det er ikke nok å beskrive bare den tekniske flaten som er best dokumentert.
- Hvis produktet inngår i et større tjenesteløp med flere kanaler eller arbeidsmåter, skal teksten beskrive hele produktets operative rolle, ikke bare ett grensesnitt.
- Når produktet omtales både på produktside og i utviklerdokumentasjon, skal du bruke begge for å forstå helheten:
  - produktsiden brukes primært for å forstå hva løsningen er i bruk
  - utviklerdokumentasjonen brukes primært for å forstå hvordan den integreres og avgrenses teknisk
- Skriv eksplisitt hva slags ressurs dette er på riktig nivå: for eksempel `utsendingstjeneste`, `registertilgangstjeneste`, `plattform`, `portal` eller `dialogtjeneste`, ikke bare `API-basert tjeneste` hvis API bare er én av flere flater.
- Legg inn en kort egen kontroll for deg selv før lagring: `Har jeg beskrevet hele løsningen, eller bare én kanal / ett grensesnitt?`

---

## Utfyllingsregler

### Generelt
- Fyll alle seksjoner med konkret, nyttig innhold (ikke generiske setninger)
- Skill tydelig mellom **fakta** (fra kilder), **deduksjon** (logisk utledet), og **usikkerhet**
- Tittel og Ressurs ID må alltid være korrekt
- Lenker skal være aktive og relevante
- Målgruppen for teksten er både forretningsside og arkitektur; skriv derfor klart og lett forståelig uten å forutsette dyp systemforståelse
- Samtidig skal innholdet ha nok presisjon til at arkitekter og KI kan vurdere mulighetsrom for gjenbruk på tvers av nye behov
- Ikke legg inn egen linje for `Målgruppe` øverst i dokumentet; målgruppen er styrende for språk og innhold, men skal ikke stå som egen metadata-linje i ressursbeskrivelsen
- Skriv `Ressurs ID` med den kanoniske ressurs-ID-en fra `arkitektur/ressurser/produktnummerering.md`, for eksempel `DIGDIR-001`
- Ikke bruk bare internt løpenummer som `01` eller `17` i nye ressursbeskrivelser
- Løpenummeret beholdes for filnavn og sortering, men `Ressurs ID` i dokumentet skal være eierbasert
- Hvis raden i ressursregisteret har en `Merknad`, skal den brukes som en kort standard presisering tidlig i `Kort beskrivelse` eller `Scope og avgrensning`, så lenge den ikke motsier oppdatert kildegrunnlag
- Ved revisjon: vis eksplisitt hvilke deler som er forbedret i analysen, ikke bare i språk/drakt
- Skriv resultatet som en selvstendig ressursbeskrivelse for målgruppen, ikke som referat av hva som står på nettsider eller i dokumentasjon
- Unngå formuleringer som "nettsiden sier", "forsiden viser", "kilden beskriver" i selve hovedteksten; bruk heller dette kun i kildegrunnlag eller når du markerer usikkerhet/kildekonflikt
- Syntetiser kilder til én ny, helhetlig beskrivelse med egne formuleringer, samtidig som innholdet skal være sporbar til kildene

### Språk og tegn (OBLIGATORISK NORSK)
- Følg felles språkregler i `config/regler/sprakforing.md`.
- **Alt innhold skal skrives på norsk** – ikke engelsk eller blandete språk
- **Bruk norske tegn:** æ, ø, å (ikke bokstaver som "ae", "o", "a" som erstatninger)
- **Norske termer prioriteres:** f.eks. "innbygger" (ikke "citizen"), "virksomhet" (ikke "enterprise"), "tjenesteeier" (ikke "service owner")
- **Unngå engelsk i parenteser** dersom det finnes norske termer (f.eks. "autorisasjon" ikke "authorization/autorisasjon")
- **Engelske akronym/forkortelser** kan brukes hvis de er etablerte (f.eks. "API", "XACML", "SLA"), men forklar på norsk første gang
- **Lagre filer som UTF-8:** nye og oppdaterte ressursbeskrivelser skal lagres som ren `UTF-8`
- **Valider tegnkoding eksplisitt:** ikke stol på visning i terminal alene; kontroller at teksten ikke inneholder doble bokstavsekvenser eller ødelagte typografitegn som tyder på feil tegnkoding
- **Rett tegnkodingsfeil før lagring:** hvis slike sekvenser oppstår, skal fila normaliseres før commit og før genererte oversikter oppdateres
- **Eksempler på korrekt norsk:**
  - "Brukersegmenter og risikomatrise" (ikke "User segments and risk matrix")
  - "Lovpålagt nasjonal felleskomponent" (ikke "Mandatory national common component")
  - "Digitalisering av offentlig sektor" (ikke "Digitalization of public sector")
  - "Sikker datautveksling med kryptering" (ikke "Secure data exchange with encryption")

### Håndtering av usikkerhet
- Bruk `**Usikkert:**` kun når kilder ikke gir grunnlag
- **Ikke** la usikkerhet være en unnskyldning for å hoppe over seksjonen
- Prøvd derimot å **dedusere fra kontekst**: Hvis produktet er i produksjon, hvordan oppfyller det sine formål?
- Eks.: "Status er ikke eksplisitt dokumentert, men ut fra at produktet er aktivt i bruk, vurderes det som i Produksjon"

### Spesifikke felt

**Status/Livsfase:**
- Start med livsfase (`Planlagt`, `Under utvikling`, `Pilot`, `Produksjon`, `Utfasing`)
- Det er tillatt med 1-2 korte faktasetninger i statusfeltet når dette tydeliggjør overgangsfase eller produksjonsstatus
- Unngå lang funksjonsbeskrivelse i statusfeltet; dette hører hjemme i **Kort beskrivelse**
- Bruk gjerne mønsteret: `**Produksjon** - kort statuskontekst` etterfulgt av `**Fakta:** ...` ved behov

**Kapabiliteter:**
- Knytt eksplisitt til navn i `arkitektur/kapabiliteter/capabilities.yaml`
- Beskriv *hvordan* produktet bidrar (ikke bare list opp navn)
- Ta bare med kapabiliteter der koblingen er sterk og direkte dokumentert eller klart utledbar fra produktets egen funksjon
- Ikke ta med kapabiliteter som bare berøres indirekte gjennom andre produkter, plattformer eller avhengigheter
- Hvis du er i tvil om koblingen er sterk nok, skal kapabiliteten utelates
- Ikke utled nye kapabiliteter bare fordi seksjoner som `Typiske brukssituasjoner`, `Når produktet normalt ikke er førstevalg` eller `Vanlige kombinasjoner med andre produkter` er lagt til. Disse seksjonene er beslutningsstøtte, ikke funksjonsutvidelse.
- Hvis `Hovedfunksjoner` endres vesentlig, skal du eksplisitt kontrollere om kapabilitetsmappingen fortsatt er riktig. Endre bare mappingen når produktets faktiske funksjonelle rolle er blitt tydeligere eller dokumentert annerledes.
- Format: `- **Tillit: Autentisering**` etterfulgt av forklaring i vanlig skrift på neste linje eller i samme punkt
- Navnet på kapabiliteten skal være i fet skrift; forklaringen skal være i vanlig skrift

**Arkitekturprinsipper:**
- Bruk `arkitektur/prinsipper/principles.md` som kuratert kilde for hvilke prinsipper som gjelder og hvordan de er koblet til hovedkapabiliteter
- Ikke utled eller finn på nye prinsippnavn utenfor denne fila
- Når seksjonen `Støtter arkitekturprinsipper` fylles ut, skal den bygge på prinsippene i `principles.md` og produktets direkte kapabilitetskoblinger
- Seksjonen skal ikke bare beskrive hva produktet støtter; vurder også tydelige svakheter, spenninger eller begrensninger mot viktige prinsipper når dette er relevant for mulig bruk
- Hvis produktet for eksempel støtter samhandling og gjenbruk, men samtidig kan gi sterk leverandørbinding, kompleks innføring eller svak brukerorientering i noen kontekster, skal dette sies eksplisitt
- Vurderingen skal brukes som beslutningsstøtte, ikke som ren prinsippmarkering

**Produktmål:**
- Beskriv både strategiske og operative mål, med tydelig kobling til dokumenterte prioriteringer
- Skriv målformuleringer i et språk som også er forståelig for forretningssiden, uten å miste den arkitektoniske presisjonen
- For Digdir-produkter: sjekk alltid dokumentasjon i Samarbeidsportalen i tillegg til Digdir Docs
- Hvis målformuleringer avviker mellom kilder: marker hva som er primærkilde og hva som er deduksjon

**Brukere og brukersegmenter:**
- Del opp brukerbildet eksplisitt i segmenter, ikke bare som løpende tekst
- Bruk som hovedregel tabell med kolonnene `Brukersegment | Primære behov | Bruksområde | Kommentar`
- Skill mellom hvem brukeren er, hva brukeren trenger, og hvordan produktet faktisk brukes
- Beskriv behov og bruksområde med begreper som kan leses av både fagpersoner uten teknisk bakgrunn og av arkitekturmiljø
- Ta med både primærbrukere, sekundærbrukere og forvaltnings-/støttemiljø når det er relevant

**Scope og avgrensning:**
- Be konkret hva som inngår og hva som ikke inngår
- Bruk lister eller tabeller for klarhet
- Eksempel: "Inngår: autentisering, sesjonsstyring. Inngår IKKE: autorisasjon, saksbehandling"

**Funksjonalitet og hovedfunksjoner:**
- Beskriv funksjonaliteten på et konseptnivå som gjør det mulig å forstå om produktet faktisk kan løse behovene det er ment å dekke
- Hver hovedfunksjon skal beskrives med noen setninger, ikke bare som navn i punktliste
- Når kildene gir nok grunnlag, skal seksjonen `Hovedfunksjoner` normalt bestå av minst **3-4 avsnitt** som forklarer produktets operative funksjon, arbeidsmåter, kanaler/grensesnitt og viktigste avgrensninger
- Unngå å komprimere hele funksjonsbildet til 3-4 korte kulepunkter hvis underlaget støtter en mer forklarende tekst
- Forklar hva funksjonen gjør, hvilken type behov den dekker, og hvilke avgrensninger som er viktige for å forstå når produktet er relevant
- Hvis løsningen har flere flater, som portal + API, manuell + integrert bruk, eller flere operative kanaler, skal funksjonsbeskrivelsen dekke dette eksplisitt og ikke reduseres til én teknisk komponent
- Bruk klart språk uten intern systemsjargong som eneste forklaring; forklar tekniske begreper kort når de er nødvendige
- Beskriv funksjoner slik at overlappende løsninger kan skilles fra hverandre, slik at leseren blir veiledet til den mest relevante løsningen for gjenbruk
- Legg inn nok funksjonsdetaljer til at arkitekter og KI kan identifisere gjenbrukspotensial, avhengigheter og grenser mot nærliggende løsninger
- Unngå bare tekniske etiketter som "API", "innboks" eller "varsling" uten forklarende tekst om hvordan funksjonen brukes i praksis
- Hvis flere produkter dekker tilstøtende eller delvis overlappende behov, skal funksjonsbeskrivelsen tydeliggjøre hva dette produktet gjør, og hva det ikke gjør
- Når produktet brukes i arkitekturvurderinger, bør `Hovedfunksjoner` normalt suppleres med egne underseksjoner for `Typiske brukssituasjoner (generisk)` og `Når <produktet> normalt ikke er førstevalg`.
- Legg `Vanlige kombinasjoner med andre produkter` under `Gjenbruk`, ikke under `Hovedfunksjoner`, med mindre det finnes en særskilt grunn til å samle dette annerledes.

**Gjenbruk og kildekode:**
- Legg alltid inn et eget underpunkt `**Kildekode:**` i `Gjenbruk`-seksjonen
- Bruk én av disse verdiene: `Åpen kildekode`, `Proprietær`, `Ikke offentlig dokumentert`
- Hvis åpen kildekode: oppgi lisens (f.eks. MIT, Apache 2.0, EUPL) og lenke til repositorium (f.eks. GitHub)
- Hvis proprietær eller ukjent: skriv `Ikke offentlig dokumentert` – ikke gjett
- Åpen kildekode er relevant for vurdering av leverandøravhengighet, lokal tilpasning og gjenbruk i andre virksomheter
- Legg kildekodeinformasjonen som siste underpunkt i `Gjenbruk`, etter `Vanlige kombinasjoner med andre produkter` hvis den seksjonen finnes

**Risiko:**
- Dekk minst: juridisk, teknisk, sikkerhet, leverandør, bruker-opplevelse
- Bruk tabell med kategori + konkret risiko + håndtering
- Vær presis (unngå generiske formuleringer som "integrasjonsrisiko")

**Forvaltning/Eier:**
- Fordel på: Produktansvar, Driftsansvar, Budsjettansvar, Styringsmodell
- Navngi konkrete organisasjoner dersom mulig
- Vis relasjon til overordnede styringsforum (f.eks. Arkitekturråd, Digitaliseringsrådet)

**Veikart, Finansiering, Plattform:**
- Disse feltene er ofte usikre – Oppgi kilder eksplisitt
- Hvis informasjon er privat/intern – Skriv "Ikke offentlig dokumentert" i stedet for "Usikkert"
- Gi linker til steder hvor informasjonen finnes (f.eks. Samarbeidsportalen for tilgang)

**Forretningsverdi:**
- Konkretiser for ulike brukergrupper (innbygger, virksomhet, samfunn, tjenesteeier)
- Gi både kvalitative (bedre opplevelse) og kvantitative estimater (hvis mulig)
- Koble til arkitekturprinsipper og nasjonale satsingsområder

**Type ressurs og kort klassifisering i ressursregisteret:**
- Klassifiseringen skal beskrive hele løsningen på riktig nivå, ikke bare ett teknisk grensesnitt.
- Unngå å bruke `API-basert tjeneste` som hovedtype hvis produktet også har portal, manuelle arbeidsløp, kanalhåndtering eller annen operativ funksjon som er sentral for hva løsningen faktisk er.
- Bruk heller formuleringer som beskriver løsningens rolle, for eksempel `utsendingstjeneste for digital og fysisk post`, `registertilgangstjeneste`, `plattform for samhandling` eller `portal for oppslag og innsending`.

### Kilder
- Alltid oppgi konkrete, aktive lenker
- Skille mellom lokale kilder (`sources/links.md`) og eksterne kilder (Digdir Docs, Samarbeidsportalen osv.)
- Oppgi hentedato
- Bruk både offisielle kilder og praktisk erfaring / dokumentererte use cases
- For revisjoner: oppgi minst 2 oppdaterte eksterne kilder kontrollert i aktuell arbeidsøkt
- Prioriter direkte oppslag i URL-er fra `sources/links.md` fremfor brede nettsøk

---

## Kvalitetskriterier for ferdig dokument

| Kriterium | Sjekk |
|-----------|-------|
| **Sporbarhet** | Alle påstander kan spores til konkret kilde (lenke eller dokument) |
| **Sammenlignbarhet** | Samme struktur og detalj-nivå som andre ressursbeskrivelser |
| **Gjenbrukbarhet** | Teksten kan brukes direkte i arkitekturvurdering eller screening uten redigering |
| **Tydelig status** | Usikkerhet er marked eksplisitt; gjetninger er unngått |
| **Konkretisering** | Hver seksjonen inneholder spesifikke eksempler og konkrete detaljer (ikke generic tekst) |
| **Tabeller** | Komplekse felt (risiko, forvaltning, brukersegmenter) er fremstilt i tabellformat for lesbarhet |
| **Beslutningsstøtte** | Det er tydelig når produktet bør velges, når det ikke er førstevalg, og hvilke kombinasjoner som er vanlige |
| **Kapabilitetsdisiplin** | Kapabilitetsmappingen er kontrollert mot faktiske hovedfunksjoner, ikke bare mot beslutningsstøttefeltene |
| **v1-gate** | Alle fem v1-minstekrav i `Trinn 2C` er oppfylt, eller dokumentet er beholdt som `v0.x` |

---

## Navngiving av filer

### Obligatorisk format for alle filer
`NN-<Ressursnavn>-operative-ressurs-canvas-vX-<forfatter>.md`

- `NN` = løpenummer (to siffer)
- `<Ressursnavn>` = kebab-case-navn
- `vX` = versjonsnummer (`v1`, `v2`, `v3`, ...)
- `<forfatter>` = hvem som opprettet filen (f.eks. `copilot`, `codex`, `hilros`, `manuel`)

**Eksempler:**
- `01-ID-porten-operative-ressurs-canvas-v1-copilot.md`
- `01-ID-porten-operative-ressurs-canvas-v2-codex.md`
- `21-Altinn-Portal-operative-ressurs-canvas-v3-manuel.md`

**Regler:**
- Versjonsnummer og forfatter er **alltid obligatorisk** i filnavnet
- Første opprettede fil for en ressurs får alltid `v1`
- Neste versjoner av samme ressurs får `v2`, `v3`, `v4` ... i kronologisk rekkefølge
- Versjonsnummeret er globalt per ressurs – det øker uavhengig av hvem som lager neste versjon
- Høyeste versjonsnummer er gjeldende siste versjon
- Det skal ikke opprettes parallelle versjonsspor per forfatter
- Eldre versjoner beholdes for historikk

### Overgangsregel for eksisterende repo
- Eldre filer uten versjonsnummer behandles som historiske referanser
- Nye filer skal alltid følge formatet over med `vX` og `<forfatter>`
- Hvis det finnes flere eldre, uversjonerte filer for samme ressurs: bygg på den mest faglig oppdaterte, men lagre ny leveranse etter ny versjonsregel

---

## Tips for god arbeidsprosess

1. **Les først, skriv siden:** Aldri overskriv eldre arbeid uten å forstå det først
2. **Bruk kilder aktivt:** Åpne 2-3 lenker mens du skriver (ikke skriv fra hukommelse)
3. **Iterering:** Start med basisfakta, så deduser verdier + strategisk betydning
4. **Konsistens:** Sjekk formatering og tonalitet mot eksisterende canvas-filer
5. **Versjonering:** Bruk alltid neste globale versjonsnummer for ressursen og inkluder alltid forfatter i filnavnet
6. **Dokumenter:** Legg inn "Merknad om kvalitetsforbedringer" eller "Endringer fra forrige versjon" i slutten hvis relevant
7. **Skill forbedringstyper:** Legg inn korte punkt for "Analyseforbedringer" og "Tekstlige forbedringer"
