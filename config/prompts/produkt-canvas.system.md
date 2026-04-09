# Standardprompt: Produktbeskrivelser (Produkt-canvas)

FormÃ¥l: Sikre lik, detaljert og grundig utfylling av produktbeskrivelser for arkitekturvurderinger, analyser og gjenbruk.

---

## Arbeidsgang

### Trinn 1: Les eksisterende versjon (VIKTIG!)
- **Hvis produktbeskrivelse allerede finnes**: Les gjennom hele filen fÃ¸rst
- **Hvis flere versjoner finnes**: Bygg videre pÃ¥ filen med hÃ¸yest versjonsnummer som utgangspunkt, med mindre brukeren ber om noe annet
- VersjonsrekkefÃ¸lgen gjelder pÃ¥ tvers av forfattere og modeller; hÃ¸yeste versjon er siste versjon
- Dette gjelder ogsÃ¥ nÃ¥r siste versjon er laget av `copilot`: den skal leses, vurderes og brukes som primÃ¦rt utgangspunkt pÃ¥ lik linje med `codex`-filer
- Ikke hopp over siste versjon fordi forfatteren er en annen modell; bruk eldre versjoner bare som supplement nÃ¥r de gir nyttig historikk eller forklarer endringer
- Hvis eldre filer mangler versjonsnummer: behandle dem som historiske filer og bruk den faglig mest oppdaterte av dem som lesegrunnlag, men skriv nye leveranser etter den nye versjonsregelen
- Identifiser hvilke felt som er fylt ut, og hvilke som er merket `Usikkert:`
- Vurder hvilke seksjoner som kan forbedres, detaljeres eller utdypes
- **MÃ¥l:** Bygge videre pÃ¥ eksisterende jobb, ikke starte fra scratch

### Trinn 2: Vurder oppgavetyp
- **Forbedring av eksisterende:** Lage en revisjonert versjon (se navngivning)
- **Ny produktbeskrivelse:** Starte fra mal + kilder

### Trinn 2B: Avklar forbedringsnivÃ¥ (OBLIGATORISK ved revisjon)
- En forbedret versjon skal alltid inneholde bÃ¥de:
  1. **Analyseforbedring:** ny eller oppdatert kildegjennomgang med verifiserte fakta
  2. **Tekstforbedring:** bedre struktur, presisjon, sprÃ¥k og lesbarhet
- Ved tekstforbedring skal tone og sprÃ¥kfÃ¸ring fra siste versjon som hovedregel bevares nÃ¥r den allerede fungerer godt for mÃ¥lgruppen.
- UnngÃ¥ unÃ¸dvendig full omskriving av avsnitt som allerede er tydelige og presise; forbedre heller mÃ¥lrettet der analyse eller presisjon faktisk blir bedre.
- **Ikke godkjent forbedring:** kun sprÃ¥kvask, omformulering eller tabellformattering uten nytt analysegrunnlag
- Dokumenter kort hva som er nytt i analysen (nye kilder, nye funn, avklarte usikkerheter)

### Trinn 3: Hent kilder (samme hver gang)
1. Mal: `config/templates/produkt-canvas-template.md`
2. Kapabiliteter: `arkitektur/kapabiliteter/capabilities.yaml` (kun navnene som finnes her)
3. Prinsipper: `arkitektur/prinsipper/principles.md` (bruk prinsippnavn og koblinger som finnes her)
4. Lenker: `sources/links.md` (lokal liste + aktive lenker til dokumentasjon)
5. Produktregister, Ressurs-ID og Merknad: `arkitektur/ressurser/produktnummerering.md`
5. **Ã…pne kilder**: Digdir Docs, Samarbeidsportalen, felles-IKT, produkteier-nettsteder (f.eks. altinn.studio)
6. **URL-valg:** Bruk som hovedregel de konkrete URL-ene som allerede er listet i `sources/links.md` fÃ¸r du prÃ¸ver bredere sÃ¸k
7. **Utvid bare ved behov:** GÃ¥ utover `sources/links.md` kun hvis lenkene der er utilstrekkelige, utdaterte eller utilgjengelige, og dokumenter hvorfor

### Trinn 4: Skriv/forbedre innhold
FÃ¸lg reglene under.

### Trinn 4A: Kontroller lÃ¸sningsbredden (OBLIGATORISK)
- FÃ¸r du skriver `Kort beskrivelse`, `Hovedfunksjoner`, `Scope og avgrensning` og `Type ressurs` i produktregisteret, skal du eksplisitt kontrollere om produktet bestÃ¥r av mer enn Ã©n bruksmÃ¥te eller leveranseflate.
- Sjekk alltid minst disse vinklene nÃ¥r kildene finnes:
  1. **Brukerflate:** portal, webflate, manuelt arbeidslÃ¸p, selvbetjent lÃ¸sning
  2. **Integrasjonsflate:** API, hendelser, maskin-til-maskin, filutveksling
  3. **Tjenesteflate:** sentral kanalhÃ¥ndtering, saksflyt, regelmotor, distribusjon, oppslag, forvaltning
- Hvis produktet har bÃ¥de portal og API, eller bÃ¥de manuell og integrert bruk, skal dette beskrives eksplisitt. Det er ikke nok Ã¥ beskrive bare den tekniske flaten som er best dokumentert.
- Hvis produktet inngÃ¥r i et stÃ¸rre tjenestelÃ¸p med flere kanaler eller arbeidsmÃ¥ter, skal teksten beskrive hele produktets operative rolle, ikke bare ett grensesnitt.
- NÃ¥r produktet omtales bÃ¥de pÃ¥ produktside og i utviklerdokumentasjon, skal du bruke begge for Ã¥ forstÃ¥ helheten:
  - produktsiden brukes primÃ¦rt for Ã¥ forstÃ¥ hva lÃ¸sningen er i bruk
  - utviklerdokumentasjonen brukes primÃ¦rt for Ã¥ forstÃ¥ hvordan den integreres og avgrenses teknisk
- Skriv eksplisitt hva slags ressurs dette er pÃ¥ riktig nivÃ¥: for eksempel `utsendingstjeneste`, `registertilgangstjeneste`, `plattform`, `portal` eller `dialogtjeneste`, ikke bare `API-basert tjeneste` hvis API bare er Ã©n av flere flater.
- Legg inn en kort egen kontroll for deg selv fÃ¸r lagring: `Har jeg beskrevet hele lÃ¸sningen, eller bare Ã©n kanal / ett grensesnitt?`

---

## Utfyllingsregler

### Generelt
- Fyll alle seksjoner med konkret, nyttig innhold (ikke generiske setninger)
- Skill tydelig mellom **fakta** (fra kilder), **deduksjon** (logisk utledet), og **usikkerhet**
- Tittel og Ressurs ID mÃ¥ alltid vÃ¦re korrekt
- Lenker skal vÃ¦re aktive og relevante
- MÃ¥lgruppen for teksten er bÃ¥de forretningsside og arkitektur; skriv derfor klart og lett forstÃ¥elig uten Ã¥ forutsette dyp systemforstÃ¥else
- Samtidig skal innholdet ha nok presisjon til at arkitekter og KI kan vurdere mulighetsrom for gjenbruk pÃ¥ tvers av nye behov
- Ikke legg inn egen linje for `MÃ¥lgruppe` Ã¸verst i dokumentet; mÃ¥lgruppen er styrende for sprÃ¥k og innhold, men skal ikke stÃ¥ som egen metadata-linje i produktbeskrivelsen
- Skriv `Ressurs ID` med den kanoniske ressurs-ID-en fra `arkitektur/ressurser/produktnummerering.md`, for eksempel `DIGDIR-001`
- Ikke bruk bare internt lÃ¸penummer som `01` eller `17` i nye produktbeskrivelser
- LÃ¸penummeret beholdes for filnavn og sortering, men `Ressurs ID` i dokumentet skal vÃ¦re eierbasert
- Hvis raden i produktregisteret har en `Merknad`, skal den brukes som en kort standard presisering tidlig i `Kort beskrivelse` eller `Scope og avgrensning`, sÃ¥ lenge den ikke motsier oppdatert kildegrunnlag
- Ved revisjon: vis eksplisitt hvilke deler som er forbedret i analysen, ikke bare i sprÃ¥k/drakt
- Skriv resultatet som en selvstendig produktbeskrivelse for mÃ¥lgruppen, ikke som referat av hva som stÃ¥r pÃ¥ nettsider eller i dokumentasjon
- UnngÃ¥ formuleringer som "nettsiden sier", "forsiden viser", "kilden beskriver" i selve hovedteksten; bruk heller dette kun i kildegrunnlag eller nÃ¥r du markerer usikkerhet/kildekonflikt
- Syntetiser kilder til Ã©n ny, helhetlig beskrivelse med egne formuleringer, samtidig som innholdet skal vÃ¦re sporbar til kildene

### SprÃ¥k og tegn (OBLIGATORISK NORSK)
- **Alt innhold skal skrives pÃ¥ norsk** â€“ ikke engelsk eller blandete sprÃ¥k
- **Bruk norske tegn:** Ã¦, Ã¸, Ã¥ (ikke bokstaver som "ae", "o", "a" som erstatninger)
- **Norske termer prioriteres:** f.eks. "innbygger" (ikke "citizen"), "virksomhet" (ikke "enterprise"), "'tjenesteeier" (ikke "service owner")
- **UnngÃ¥ engelsk i parenteser** dersom det finnes norske termer (f.eks. "autorisasjon" ikke "authorization/autorisasjon")
- **Engelske akronym/forkortelser** kan brukes hvis de er etablerte (f.eks. "API", "XACML", "SLA"), men forklar pÃ¥ norsk fÃ¸rste gang
- **Lagre filer som UTF-8:** nye og oppdaterte produktbeskrivelser skal lagres som ren `UTF-8`
- **Valider tegnkoding eksplisitt:** ikke stol pÃ¥ visning i terminal alene; kontroller at teksten ikke inneholder doble bokstavsekvenser eller Ã¸delagte typografitegn som tyder pÃ¥ feil tegnkoding
- **Rett tegnkodingsfeil fÃ¸r lagring:** hvis slike sekvenser oppstÃ¥r, skal fila normaliseres fÃ¸r commit og fÃ¸r genererte oversikter oppdateres
- **Eksempler pÃ¥ korrekt norsk:**
  - âœ… "Brukersegmenter og risikomatrise" (ikke "User segments and risk matrix")
  - âœ… "LovpÃ¥lagt nasjonal felleskomponent" (ikke "Mandatory national common component")
  - âœ… "Digitalisering av offentlig sektor" (ikke "Digitalization of public sector")
  - âœ… "Sikker datautveksling med kryptering" (ikke "Secure data exchange with encryption")

### HÃ¥ndtering av usikkerhet
- Bruk `**Usikkert:**` kun nÃ¥r kilder ikke gir grunnlag
- **Ikke** la usikkerhet vÃ¦re en unnskyldning for Ã¥ hoppe over seksjonen
- PrÃ¸vd derimot Ã¥ **dedusere fra kontekst**: Hvis produktet er i produksjon, hvordan oppfyller det sine formÃ¥l?
- Eks.: "Status er ikke eksplisitt dokumentert, men ut fra at produktet er aktivt i bruk, vurderes det som i Produksjon"

### Spesifikke felt

**Status/Livsfase:**
- Start med livsfase (`Planlagt`, `Under utvikling`, `Pilot`, `Produksjon`, `Utfasing`)
- Det er tillatt med 1-2 korte faktasetninger i statusfeltet nÃ¥r dette tydeliggjÃ¸r overgangsfase eller produksjonsstatus
- UnngÃ¥ lang funksjonsbeskrivelse i statusfeltet; dette hÃ¸rer hjemme i **Kort beskrivelse**
- Bruk gjerne mÃ¸nsteret: `**Produksjon** - kort statuskontekst` etterfulgt av `**Fakta:** ...` ved behov

**Kapabiliteter:**
- Knytt eksplisitt til navn i `arkitektur/kapabiliteter/capabilities.yaml`
- Beskriv *hvordan* produktet bidrar (ikke bare list opp navn)
- Ta bare med kapabiliteter der koblingen er sterk og direkte dokumentert eller klart utledbar fra produktets egen funksjon
- Ikke ta med kapabiliteter som bare berÃ¸res indirekte gjennom andre produkter, plattformer eller avhengigheter
- Hvis du er i tvil om koblingen er sterk nok, skal kapabiliteten utelates
- Ikke utled nye kapabiliteter bare fordi seksjoner som `Typiske brukssituasjoner`, `NÃ¥r produktet normalt ikke er fÃ¸rstevalg` eller `Vanlige kombinasjoner med andre produkter` er lagt til. Disse seksjonene er beslutningsstÃ¸tte, ikke funksjonsutvidelse.
- Hvis `Hovedfunksjoner` endres vesentlig, skal du eksplisitt kontrollere om kapabilitetsmappingen fortsatt er riktig. Endre bare mappingen nÃ¥r produktets faktiske funksjonelle rolle er blitt tydeligere eller dokumentert annerledes.
- Format: `- **Tillit: Autentisering**` etterfulgt av forklaring i vanlig skrift pÃ¥ neste linje eller i samme punkt
- Navnet pÃ¥ kapabiliteten skal vÃ¦re i fet skrift; forklaringen skal vÃ¦re i vanlig skrift

**Arkitekturprinsipper:**
- Bruk `arkitektur/prinsipper/principles.md` som kuratert kilde for hvilke prinsipper som gjelder og hvordan de er koblet til hovedkapabiliteter
- Ikke utled eller finn pÃ¥ nye prinsippnavn utenfor denne fila
- NÃ¥r seksjonen `StÃ¸tter arkitekturprinsipper` fylles ut, skal den bygge pÃ¥ prinsippene i `principles.md` og produktets direkte kapabilitetskoblinger

**ProduktmÃ¥l:**
- Beskriv bÃ¥de strategiske og operative mÃ¥l, med tydelig kobling til dokumenterte prioriteringer
- Skriv mÃ¥lformuleringer i et sprÃ¥k som ogsÃ¥ er forstÃ¥elig for forretningssiden, uten Ã¥ miste den arkitektoniske presisjonen
- For Digdir-produkter: sjekk alltid dokumentasjon i Samarbeidsportalen i tillegg til Digdir Docs
- Hvis mÃ¥lformuleringer avviker mellom kilder: marker hva som er primÃ¦rkilde og hva som er deduksjon

**Brukere og brukersegmenter:**
- Del opp brukerbildet eksplisitt i segmenter, ikke bare som lÃ¸pende tekst
- Bruk som hovedregel tabell med kolonnene `Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar`
- Skill mellom hvem brukeren er, hva brukeren trenger, og hvordan produktet faktisk brukes
- Beskriv behov og bruksomrÃ¥de med begreper som kan leses av bÃ¥de fagpersoner uten teknisk bakgrunn og av arkitekturmiljÃ¸
- Ta med bÃ¥de primÃ¦rbrukere, sekundÃ¦rbrukere og forvaltnings-/stÃ¸ttemiljÃ¸ nÃ¥r det er relevant

**Scope og avgrensning:**
- Be konkret hva som inngÃ¥r og hva som ikke inngÃ¥r
- Bruk lister eller tabeller for klarhet
- Eksempel: "InngÃ¥r: autentisering, sesjonsstyring. InngÃ¥r IKKE: autorisasjon, saksbehandling"

**Funksjonalitet og hovedfunksjoner:**
- Beskriv funksjonaliteten pÃ¥ et konseptnivÃ¥ som gjÃ¸r det mulig Ã¥ forstÃ¥ om produktet faktisk kan lÃ¸se behovene det er ment Ã¥ dekke
- Hver hovedfunksjon skal beskrives med noen setninger, ikke bare som navn i punktliste
- NÃ¥r kildene gir nok grunnlag, skal seksjonen `Hovedfunksjoner` normalt bestÃ¥ av minst **3-4 avsnitt** som forklarer produktets operative funksjon, arbeidsmÃ¥ter, kanaler/grensesnitt og viktigste avgrensninger
- UnngÃ¥ Ã¥ komprimere hele funksjonsbildet til 3-4 korte kulepunkter hvis underlaget stÃ¸tter en mer forklarende tekst
- Forklar hva funksjonen gjÃ¸r, hvilken type behov den dekker, og hvilke avgrensninger som er viktige for Ã¥ forstÃ¥ nÃ¥r produktet er relevant
- Hvis lÃ¸sningen har flere flater, som portal + API, manuell + integrert bruk, eller flere operative kanaler, skal funksjonsbeskrivelsen dekke dette eksplisitt og ikke reduseres til Ã©n teknisk komponent
- Bruk klart sprÃ¥k uten intern systemsjargong som eneste forklaring; forklar tekniske begreper kort nÃ¥r de er nÃ¸dvendige
- Beskriv funksjoner slik at overlappende lÃ¸sninger kan skilles fra hverandre, slik at leseren blir veiledet til den mest relevante lÃ¸sningen for gjenbruk
- Legg inn nok funksjonsdetaljer til at arkitekter og KI kan identifisere gjenbrukspotensial, avhengigheter og grenser mot nÃ¦rliggende lÃ¸sninger
- UnngÃ¥ bare tekniske etiketter som "API", "innboks" eller "varsling" uten forklarende tekst om hvordan funksjonen brukes i praksis
- Hvis flere produkter dekker tilstÃ¸tende eller delvis overlappende behov, skal funksjonsbeskrivelsen tydeliggjÃ¸re hva dette produktet gjÃ¸r, og hva det ikke gjÃ¸r
- NÃ¥r produktet brukes i arkitekturvurderinger, bÃ¸r `Hovedfunksjoner` normalt suppleres med egne underseksjoner for `Typiske brukssituasjoner (generisk)` og `NÃ¥r <produktet> normalt ikke er fÃ¸rstevalg`.
- Legg `Vanlige kombinasjoner med andre produkter` under `Gjenbruk`, ikke under `Hovedfunksjoner`, med mindre det finnes en sÃ¦rskilt grunn til Ã¥ samle dette annerledes.

**Risiko:**
- Dekk minst: juridisk, teknisk, sikkerhet, leverandÃ¸r, bruker-opplevelse
- Bruk tabell med kategori + konkret risiko + hÃ¥ndtering
- VÃ¦r presis (unngÃ¥ generiske formuleringer som "integrasjonsrisiko")

**Forvaltning/Eier:**
- Fordel pÃ¥: Produktansvar, Driftsansvar, Budsjettansvar, Styringsmodell
- Navngi konkrete organisasjoner dersom mulig
- Vis relasjon til overordnede styringsforum (f.eks. ArkitekturrÃ¥d, DigitaliseringsrÃ¥det)

**Veikart, Finansiering, Plattform:**
- Disse feltene er ofte usikre â†’ Oppgi kilder eksplisitt
- Hvis informasjon er privat/intern â†’ Skriv "Ikke offentlig dokumentert" i stedet for "Usikkert"
- Gi linker til steder hvor informasjonen finnes (f.eks. Samarbeidsportalen for tilgang)

**Forretningsverdi:**
- Konkretiser for ulike brukergrupper (innbygger, virksomhet, samfunn, tjenesteeier)
- Gi bÃ¥de kvalitative (bedre opplevelse) og kvantitative estimater (hvis mulig)
- Koble til arkitekturprinsipper og nasjonale satsingsomrÃ¥der

**Type ressurs og kort klassifisering i produktregisteret:**
- Klassifiseringen skal beskrive hele lÃ¸sningen pÃ¥ riktig nivÃ¥, ikke bare ett teknisk grensesnitt.
- UnngÃ¥ Ã¥ bruke `API-basert tjeneste` som hovedtype hvis produktet ogsÃ¥ har portal, manuelle arbeidslÃ¸p, kanalhÃ¥ndtering eller annen operativ funksjon som er sentral for hva lÃ¸sningen faktisk er.
- Bruk heller formuleringer som beskriver lÃ¸sningens rolle, for eksempel `utsendingstjeneste for digital og fysisk post`, `registertilgangstjeneste`, `plattform for samhandling` eller `portal for oppslag og innsending`.

### Kilder
- Alltid oppgi konkrete, aktive lenker
- Skille mellom lokale kilder (`sources/links.md`) og eksterne kilder (Digdir Docs, Samarbeidsportalen osv.)
- Oppgi hentedato
- Bruk bÃ¥de offisielle kilder og praktisk erfaring / dokumentererte use cases
- For revisjoner: oppgi minst 2 oppdaterte eksterne kilder kontrollert i aktuell arbeidsÃ¸kt
- Prioriter direkte oppslag i URL-er fra `sources/links.md` fremfor brede nettsÃ¸k

---

## Kvalitetskriterier for ferdig dokument

| Kriterium | Sjekk |
|-----------|-------|
| **Sporbarhet** | Alle pÃ¥stander kan spores til konkret kilde (lenke eller dokument) |
| **Sammenlignbarhet** | Samme struktur og detalj-nivÃ¥ som andre produktbeskrivelser |
| **Gjenbrukbarhet** | Teksten kan brukes direkte i arkitekturvurdering eller screening uten redigering |
| **Tydelig status** | Usikkerhet er marked eksplisitt; gjetninger er unngÃ¥tt |
| **Konkretisering** | Hver seksjonen inneholder spesifikke eksempler og konkrete detaljer (ikke generic tekst) |
| **Tabeller** | Komplekse felt (risiko, forvaltning, brukersegmenter) er fremstilt i tabellformat for lesbarhet |
| **BeslutningsstÃ¸tte** | Det er tydelig nÃ¥r produktet bÃ¸r velges, nÃ¥r det ikke er fÃ¸rstevalg, og hvilke kombinasjoner som er vanlige |
| **Kapabilitetsdisiplin** | Kapabilitetsmappingen er kontrollert mot faktiske hovedfunksjoner, ikke bare mot beslutningsstÃ¸ttefeltene |

---

## Navngiving av filer

### Obligatorisk format for alle filer
`NN-<Produktnavn>-produkt-canvas-vX-<forfatter>.md`

- `NN` = produktnummer (to siffer)
- `<Produktnavn>` = kebab-case-navn
- `vX` = versjonsnummer (`v1`, `v2`, `v3`, ...)
- `<forfatter>` = hvem som opprettet filen (f.eks. `copilot`, `codex`, `hilros`, `manuel`)

**Eksempler:**
- `01-ID-porten-produkt-canvas-v1-copilot.md`
- `01-ID-porten-produkt-canvas-v2-codex.md`
- `21-Altinn-Portal-produkt-canvas-v3-manuel.md`

**Regler:**
- Versjonsnummer og forfatter er **alltid obligatorisk** i filnavnet
- FÃ¸rste opprettede fil for et produkt fÃ¥r alltid `v1`
- Neste versjoner av samme produkt fÃ¥r `v2`, `v3`, `v4` ... i kronologisk rekkefÃ¸lge
- Versjonsnummeret er globalt per produkt â€“ det Ã¸ker uavhengig av hvem som lager neste versjon
- HÃ¸yeste versjonsnummer er gjeldende siste versjon
- Det skal ikke opprettes parallelle versjonsspor per forfatter
- Eldre versjoner beholdes for historikk

### Overgangsregel for eksisterende repo
- Eldre filer uten versjonsnummer behandles som historiske referanser
- Nye filer skal alltid fÃ¸lge formatet over med `vX` og `<forfatter>`
- Hvis det finnes flere eldre, uversjonerte filer for samme produkt: bygg pÃ¥ den mest faglig oppdaterte, men lagre ny leveranse etter ny versjonsregel

---

## Tips for god arbeidsprosess

1. **Les fÃ¸rst, skriv siden:** Aldri overskriv eldre arbeid uten Ã¥ forstÃ¥ det fÃ¸rst
2. **Bruk kilder aktivt:** Ã…pne 2-3 lenker mens du skriver (ikke skriv fra hukommelse)
3. **Iterering:** Start med basisfakta, sÃ¥ deduser verdier + strategisk betydning
4. **Konsistens:** Sjekk formatering og tonalitet mot eksisterende canvas-filer
5. **Versjonering:** Bruk alltid neste globale versjonsnummer for produktet og inkluder alltid forfatter i filnavnet
6. **Dokumenter:** Legg inn "Merknad om kvalitetsforbedringer" eller "Endringer fra forrige versjon" i slutten hvis relevant
7. **Skill forbedringstyper:** Legg inn korte punkt for "Analyseforbedringer" og "Tekstlige forbedringer"

