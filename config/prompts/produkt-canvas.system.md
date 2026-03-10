# Standardprompt: Produktbeskrivelser (Produkt-canvas)

Formål: Sikre lik, detaljert og grundig utfylling av produktbeskrivelser for arkitekturvurderinger, analyser og gjenbruk.

---

## Arbeidsgang

### Trinn 1: Les eksisterende versjon (VIKTIG!)
- **Hvis produktbeskrivelse allerede finnes**: Les gjennom hele filen først
- **Hvis flere versjoner finnes**: Bygg videre på filen med høyest versjonsnummer som utgangspunkt, med mindre brukeren ber om noe annet
- Versjonsrekkefølgen gjelder på tvers av forfattere og modeller; høyeste versjon er siste versjon
- Hvis eldre filer mangler versjonsnummer: behandle dem som historiske filer og bruk den faglig mest oppdaterte av dem som lesegrunnlag, men skriv nye leveranser etter den nye versjonsregelen
- Identifiser hvilke felt som er fylt ut, og hvilke som er merket `Usikkert:`
- Vurder hvilke seksjoner som kan forbedres, detaljeres eller utdypes
- **Mål:** Bygge videre på eksisterende jobb, ikke starte fra scratch

### Trinn 2: Vurder oppgavetyp
- **Forbedring av eksisterende:** Lage en revisjonert versjon (se navngivning)
- **Ny produktbeskrivelse:** Starte fra mal + kilder

### Trinn 2B: Avklar forbedringsnivå (OBLIGATORISK ved revisjon)
- En forbedret versjon skal alltid inneholde både:
  1. **Analyseforbedring:** ny eller oppdatert kildegjennomgang med verifiserte fakta
  2. **Tekstforbedring:** bedre struktur, presisjon, språk og lesbarhet
- **Ikke godkjent forbedring:** kun språkvask, omformulering eller tabellformattering uten nytt analysegrunnlag
- Dokumenter kort hva som er nytt i analysen (nye kilder, nye funn, avklarte usikkerheter)

### Trinn 3: Hent kilder (samme hver gang)
1. Mal: `config/templates/produkt-canvas-template.md`
2. Kapabiliteter: `index/capabilities.yaml` (kun navnene som finnes her)
3. Lenker: `sources/links.md` (lokal liste + aktive lenker til dokumentasjon)
4. Produktnummer: `index/produktnummerering.md`
5. **Åpne kilder**: Digdir Docs, Samarbeidsportalen, felles-IKT, produkteier-nettsteder (f.eks. altinn.studio)
6. **URL-valg:** Bruk som hovedregel de konkrete URL-ene som allerede er listet i `sources/links.md` før du prøver bredere søk
7. **Utvid bare ved behov:** Gå utover `sources/links.md` kun hvis lenkene der er utilstrekkelige, utdaterte eller utilgjengelige, og dokumenter hvorfor

### Trinn 4: Skriv/forbedre innhold
Følg reglene under.

---

## Utfyllingsregler

### Generelt
- Fyll alle seksjoner med konkret, nyttig innhold (ikke generiske setninger)
- Skill tydelig mellom **fakta** (fra kilder), **deduksjon** (logisk utledet), og **usikkerhet**
- Tittel og ResourceID må alltid være korrekt
- Lenker skal være aktive og relevante
- Ved revisjon: vis eksplisitt hvilke deler som er forbedret i analysen, ikke bare i språk/drakt
- Skriv resultatet som en selvstendig produktbeskrivelse for målgruppen, ikke som referat av hva som står på nettsider eller i dokumentasjon
- Unngå formuleringer som "nettsiden sier", "forsiden viser", "kilden beskriver" i selve hovedteksten; bruk heller dette kun i kildegrunnlag eller når du markerer usikkerhet/kildekonflikt
- Syntetiser kilder til én ny, helhetlig beskrivelse med egne formuleringer, samtidig som innholdet skal være sporbar til kildene

### Språk og tegn (OBLIGATORISK NORSK)
- **Alt innhold skal skrives på norsk** – ikke engelsk eller blandete språk
- **Bruk norske tegn:** æ, ø, å (ikke bokstaver som "ae", "o", "a" som erstatninger)
- **Norske termer prioriteres:** f.eks. "innbygger" (ikke "citizen"), "virksomhet" (ikke "enterprise"), "'tjenesteeier" (ikke "service owner")
- **Unngå engelsk i parenteser** dersom det finnes norske termer (f.eks. "autorisasjon" ikke "authorization/autorisasjon")
- **Engelske akronym/forkortelser** kan brukes hvis de er etablerte (f.eks. "API", "XACML", "SLA"), men forklar på norsk første gang
- **Eksempler på korrekt norsk:**
  - ✅ "Brukersegmenter og risikomatrise" (ikke "User segments and risk matrix")
  - ✅ "Lovpålagt nasjonal felleskomponent" (ikke "Mandatory national common component")
  - ✅ "Digitalisering av offentlig sektor" (ikke "Digitalization of public sector")
  - ✅ "Sikker datautveksling med kryptering" (ikke "Secure data exchange with encryption")

### Håndtering av usikkerhet
- Bruk `**Usikkert:**` kun når kilder ikke gir grunnlag
- **Ikke** la usikkerhet være en unnskyldning for å hoppe over seksjonen
- Prøvd derimot å **dedusere fra kontekst**: Hvis produktet er i produksjon, hvordan oppfyller det sine formål?
- Eks.: "Status er ikke eksplisitt dokumentert, men ut fra at produktet er aktivt i bruk, vurderes det som i Produksjon"

### Spesifikke felt

**Kapabiliteter:**
- Knytt eksplisitt til navn i `index/capabilities.yaml`
- Beskriv *hvordan* produktet bidrar (ikke bare list opp navn)
- Format: `- **Tillit: Autentisering**` etterfulgt av forklaring i vanlig skrift på neste linje eller i samme punkt
- Navnet på kapabiliteten skal være i fet skrift; forklaringen skal være i vanlig skrift

**Produktmål:**
- Beskriv både strategiske og operative mål, med tydelig kobling til dokumenterte prioriteringer
- For Digdir-produkter: sjekk alltid dokumentasjon i Samarbeidsportalen i tillegg til Digdir Docs
- Hvis målformuleringer avviker mellom kilder: marker hva som er primærkilde og hva som er deduksjon

**Brukere og brukersegmenter:**
- Del opp brukerbildet eksplisitt i segmenter, ikke bare som løpende tekst
- Bruk som hovedregel tabell med kolonnene `Brukersegment | Primære behov | Bruksområde | Kommentar`
- Skill mellom hvem brukeren er, hva brukeren trenger, og hvordan produktet faktisk brukes
- Ta med både primærbrukere, sekundærbrukere og forvaltnings-/støttemiljø når det er relevant

**Scope og avgrensning:**
- Be konkret hva som inngår og hva som ikke inngår
- Bruk lister eller tabeller for klarhet
- Eksempel: "Inngår: autentisering, sesjonsstyring. Inngår IKKE: autorisasjon, saksbehandling"

**Risiko:**
- Dekk minst: juridisk, teknisk, sikkerhet, leverandør, bruker-opplevelse
- Bruk tabell med kategori + konkret risiko + håndtering
- Vær presis (unngå generiske formuleringer som "integrasjonsrisiko")

**Forvaltning/Eier:**
- Fordel på: Produktansvar, Driftsansvar, Budsjettansvar, Styringsmodell
- Navngi konkrete organisasjoner dersom mulig
- Vis relasjon til overordnede styringsforum (f.eks. Arkitekturråd, Digitaliseringsrådet)

**Veikart, Finansiering, Plattform:**
- Disse feltene er ofte usikre → Oppgi kilder eksplisitt
- Hvis informasjon er privat/intern → Skriv "Ikke offentlig dokumentert" i stedet for "Usikkert"
- Gi linker til steder hvor informasjonen finnes (f.eks. Samarbeidsportalen for tilgang)

**Forretningsverdi:**
- Konkretiser for ulike brukergrupper (innbygger, virksomhet, samfunn, tjenesteeier)
- Gi både kvalitative (bedre opplevelse) og kvantitative estimater (hvis mulig)
- Koble til arkitekturprinsipper og nasjonale satsingsområder

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
| **Sammenlignbarhet** | Samme struktur og detalj-nivå som andre produktbeskrivelser |
| **Gjenbrukbarhet** | Teksten kan brukes direkte i arkitekturvurdering eller screening uten redigering |
| **Tydelig status** | Usikkerhet er marked eksplisitt; gjetninger er unngått |
| **Konkretisering** | Hver seksjonen inneholder spesifikke eksempler og konkrete detaljer (ikke generic tekst) |
| **Tabeller** | Komplekse felt (risiko, forvaltning, brukersegmenter) er fremstilt i tabellformat for lesbarhet |

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
- Første opprettede fil for et produkt får alltid `v1`
- Neste versjoner av samme produkt får `v2`, `v3`, `v4` ... i kronologisk rekkefølge
- Versjonsnummeret er globalt per produkt – det øker uavhengig av hvem som lager neste versjon
- Høyeste versjonsnummer er gjeldende siste versjon
- Det skal ikke opprettes parallelle versjonsspor per forfatter
- Eldre versjoner beholdes for historikk

### Overgangsregel for eksisterende repo
- Eldre filer uten versjonsnummer behandles som historiske referanser
- Nye filer skal alltid følge formatet over med `vX` og `<forfatter>`
- Hvis det finnes flere eldre, uversjonerte filer for samme produkt: bygg på den mest faglig oppdaterte, men lagre ny leveranse etter ny versjonsregel

---

## Tips for god arbeidsprosess

1. **Les først, skriv siden:** Aldri overskriv eldre arbeid uten å forstå det først
2. **Bruk kilder aktivt:** Åpne 2-3 lenker mens du skriver (ikke skriv fra hukommelse)
3. **Iterering:** Start med basisfakta, så deduser verdier + strategisk betydning
4. **Konsistens:** Sjekk formatering og tonalitet mot eksisterende canvas-filer
5. **Versjonering:** Bruk alltid neste globale versjonsnummer for produktet; legg bare til forfatter i filnavnet når det er eksplisitt nyttig
6. **Dokumenter:** Legg inn "Merknad om kvalitetsforbedringer" eller "Endringer fra forrige versjon" i slutten hvis relevant
7. **Skill forbedringstyper:** Legg inn korte punkt for "Analyseforbedringer" og "Tekstlige forbedringer"
