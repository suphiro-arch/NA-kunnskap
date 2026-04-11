# Ressurser

Denne mappa samler styringsgrunnlag, registerføring og ressursbeskrivelser for hele ressursområdet.

## Formål
- Gi én felles inngang til ressurser (operative løsninger, normerende ressurser, samarbeidsfora).
- Skille tydelig mellom løsning, styring og normering.
- Gjøre det lett å registrere og finne ressurser på nettsiden.

---

## Filstruktur

| Fil/Mappe | Formål |
|---|---|
| `produktnummerering.md` | **Master for ressurs-ID-er og dokumentkoblinger** — hver ressurs får ett register-entry her |
| `styringsregler.md` | Definisjoner, opptakskriterier og klassifiseringsregler |
| `ressursregister.md` | Midlertidig arbeidsnotat fra overgangsfase (ikke i bruk nå) |
| `operative-losninger-og-tjenester/` | Operative løsninger, tjenester, plattformer, registre i bruk |
| `normerende-ressurser/` | Standarder, veiledere, referansearkitektur, modeller som gir føringer |
| `samarbeidsfora/` | Fora, råd, nettverk, samordningsarenaer |

---

## Hvordan arbeide med ressurser

### Opprett ny ressurs

1. **Velg ressurstype** og mappe:
   - Operative løsninger → `operative-losninger-og-tjenester/`
   - Normering/standarder → `normerende-ressurser/`
   - Fora/samordning → `samarbeidsfora/`

2. **Tildel ressurs-ID**:
   - Åpne `produktnummerering.md` og finn neste ledige ID hos riktig eier (f.eks. `KS-016` hvis `KS-015` er siste).
   - Noter nummeret lokalt.

3. **Opprett fil med riktig navn**:
   ```
   NN-Ressursnavn-ressurs-type-v1-format.md
   ```
   Eksempler:
   - Operative: `01-ID-porten-operative-ressurs-canvas-v1-copilot.md`
   - Normering: `72-FINT-Informasjonsmodell-v1-codex.md`
   - Samarbeid: `88-Arkitektur-og-standardiseringsradet-v0-codex.md`

   **Konvensjoner:**
   - `NN` = løpenummer (stabil sortering)
   - `v1` = versjon (starter på v1 for ny ressurs)
   - `codex`, `produktkort` osv. = format/type (valgfritt)

4. **Bruk riktig mal**:
   - Operative: `config/templates/operative-ressurs-template.md`
   - Normering: `config/templates/normerende-ressurs-template.md`
   - Samarbeid: `config/templates/samarbeidsforum-template.md`

5. **Legg inn ressurs-ID i dokumentet**:
   - Fyll inn feltet "Ressurs ID" med den ressurs-IDen du tildelte i steg 2 (f.eks. `KS-016`).

6. **Registrer i produktnummerering.md**:
   - Legg til ny rad i riktig eierseksjon:
     ```
     | NN | `EIER-NR` | Ressursnavn | Type | Kapabiliteter (komma-separert) | [Åpne](path/til/fil.md) |
     ```
   - Generatoren plukker automatisk denne og bygger nettsiden.

---

### Opprett ny versjon av eksisterende ressurs

1. **Kopier den gamle filen** og gi den nytt versjonsnummer:
   ```
   Gammel: 01-ID-porten-operative-ressurs-canvas-v3-codex.md
   Ny:     01-ID-porten-operative-ressurs-canvas-v4-codex.md
   ```
   (Lopenummeret `NN` blir det samme.)

2. **Oppdater innholdet** i den nye filen.

3. **Oppdater `produktnummerering.md`**:
   - Finn raden med ressursen.
   - Endre `Siste versjon` fra `v3 (codex)` til `v4 (codex)`.
   - Endre dokumentlenken til å peke på den nye filen.

4. **Valgfritt: Rydd gammel versjon**:
   - Hvis du vil holde repoet rent, kan du slette den gamle filen:
     ```bash
     git rm arkitektur/ressurser/operative-losninger-og-tjenester/01-ID-porten-operative-ressurs-canvas-v3-codex.md
     ```
   - Kommitter med melding som "Update ID-porten to v4" eller "Deprecate ID-porten v3".

---

## Hva som skjer automatisk

- **Nettside**: Generator-scriptet (`web/hugo-prototype/scripts/generate-products.ps1`) leser `produktnummerering.md` og bygger ressursovesiktssidene og filtrert oversikt med alle registrerte ressurser.
- **Visning**: Nettsiden viser alltid **siste versjon** av hver ressurs (basert på det som registeret peker til).
- **Søk og filtrering**: Besøkende kan filtrere etter kategori, eier og kapabilitet.

---

## Kobling til nettside

Når du legger inn en ressurs og kan nå finne den på:
- **Toppnivå**: `https://suphiro-arch.github.io/NA-kunnskap/ressursoversikt/` (alle ressurser)
- **Kategori**: `/ressursoversikt/produkter/operative-losninger-og-tjenester/` osv.
- **Søk og filtrering**: Direkte på oversiktssiden med valgbare filter.

---

## Tips og vanlige saker

**Q: Skal jeg slette eller arkivere gamle versjoner?**  
A: Valgfritt. Repoet viser bare siste versjon, så gamle filer tar ikke plass på nettsiden. Men du kan rydde dem når som helst.

**Q: Hva hvis ressurs-IDen endres?**  
A: Endre den i både filnavn og `produktnummerering.md`. ID-en er kanonisk identifikator, så både mennesker og systemer stoler på den.

**Q: Kan jeg ha kapabiliteter som hovedinndeling i stedet for ressurstype?**  
A: Nei – ressurstype-mappene er primær struktur. Bruk kapabiliteter som filter og metadata på nettstedet.

**Q: Hva med gamle versjoner — skal jeg slette dem?**  
A: Nei – du kan beholde dem i Git for historiebakgrunn. Generator-scriptet viser **kun den versjonen som registeret peker til**. Gamle filer blir ignorert. Du kan:
- Beholde dem i samme mappe som arkiv
- Slette dem hvis du ønsker å rydde (Bruk `git rm`)
- Navngi arkiverte filer med suffikser som `-deprecated` eller slå dem i en `_archive/` undermappe

---

## Teknisk detalj: Versjonskontroll

Generator-scriptet (`web/hugo-prototype/scripts/generate-products.ps1`) fungerer slik:
1. Les `produktnummerering.md` og plukk ut ressurs-IDer og dokumentlenker
2. For hver ressurs: les **kun** filen som registeret peker til
3. Generer nettsidesidene bare for disse filene
4. Alle andre filer i mappen (gamle versjoner) blir ignorert

**Sikkerhet:** Hvis du glemmer å oppdatere registeret etter å ha opprettet v4, vil nettsiden fortsatt vise v3. Generator warning ikke – du får bare ikke oppdatering. Så sørg for å alltid oppdatere `produktnummerering.md` når du lager ny versjon!
