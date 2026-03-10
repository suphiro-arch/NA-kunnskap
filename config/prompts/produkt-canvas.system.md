# Standardprompt: Produktbeskrivelser (Produkt-canvas)

Formål: Sikre lik, detaljert og grundig utfylling av produktbeskrivelser for arkitekturvurderinger, analyser og gjenbruk.

---

## Arbeidsgang

### Trinn 1: Les eksisterende versjon (VIKTIG!)
- **Hvis produktbeskrivelse allerede finnes**: Les gjennom hele filen først
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
1. Mal: `results/templates/produkt-canvas-template.md`
2. Kapabiliteter: `index/capabilities.yaml` (kun navnene som finnes her)
3. Lenker: `sources/links.md` (lokal liste + aktive lenker til dokumentasjon)
4. Produktnummer: `index/produktnummerering.md`
5. **Åpne kilder**: Digdir Docs, Samarbeidsportalen, felles-IKT, produkteier-nettsteder (f.eks. altinn.studio)

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
- Format: `- Tillit: Autentisering` og forklaring

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

### Når du forbedrer eksisterende versjon
Format: `NN-<Produktnavn>-produkt-canvas-<forfatter>.md`

Eksempler:
- `01-ID-porten-produkt-canvas-copilot.md` (forbedret av GitHub Copilot)
- `01-ID-porten-produkt-canvas-codex.md` (forbedret av ChatGPT)
- `01-ID-porten-produkt-canvas-manuel.md` (forbedret manuelt)

**Hensikt:** Tillater sammenlikning av ulike tilnærminger + versjonskontroll

### Når du lager nye filer
Format: `NN-<Produktnavn>-produkt-canvas.md`

Eksempel: `05-Kontakt-og-reservasjonsregisteret-produkt-canvas.md`

---

## Tips for god arbeidsprosess

1. **Les først, skriv siden:** Aldri overskriv eldre arbeid uten å forstå det først
2. **Bruk kilder aktivt:** Åpne 2-3 lenker mens du skriver (ikke skriv fra hukommelse)
3. **Iterering:** Start med basisfakta, så deduser verdier + strategisk betydning
4. **Konsistens:** Sjekk formatering og tonalitet mot eksisterende canvas-filer
5. **Versjonering:** Hvis du gør stort forbedring – lag "-forfatter"-versjon for sammenlikning
6. **Dokumenter:** Legg inn "Merknad om kvalitetsforbedringer" eller "Endringer fra forrige versjon" i slutten hvis relevant
7. **Skill forbedringstyper:** Legg inn korte punkt for "Analyseforbedringer" og "Tekstlige forbedringer"
