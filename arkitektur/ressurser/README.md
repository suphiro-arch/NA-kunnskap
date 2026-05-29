# Ressurser

Denne mappa samler styringsgrunnlag, registerføring og ressursbeskrivelser for hele ressursområdet.

## Formål
- Gi én felles inngang til ressurser etter rammeverkskategoriene.
- Skille tydelig mellom gjenbrukbare løsninger, standarder og veiledning, samhandlingsarenaer og organisering, og økonomiske eller juridiske rammer og virkemidler.
- Gjøre det lett å registrere og finne ressurser på nettsiden.

## Kategoriavgrensning (kortversjon)
- `Gjenbrukbare løsninger`: tekniske komponenter, applikasjoner og tjenester som leverer funksjonalitet eller dataprodukter som kan brukes av flere.
- `Standarder og veiledning`: ressurser som setter regler eller gir retning, som standarder, veiledere, referansearkitekturer og metodikk.
- `Samhandlingsarenaer og organisering`: organiserte nettverk og styringsorganer for dialog, strategisk samarbeid og samordning.
- `Økonomiske og juridiske rammer og virkemidler`: finansielle og regulative virkemidler som muliggjør gjennomføring og setter handlingsrom.

---

## Filstruktur

| Fil/Mappe | Formål |
|---|---|
| `produktnummerering.md` | **Master for ressurs-ID-er og dokumentkoblinger** — hver ressurs får ett register-entry her |
| `styringsregler.md` | Definisjoner, opptakskriterier og klassifiseringsregler |
| `operative-losninger-og-tjenester/` | Teknisk mappe for gjenbrukbare løsninger: tjenester, plattformer, registre og felleskomponenter i bruk |
| `normerende-ressurser/` | Teknisk mappe for standarder og veiledning: veiledere, referansearkitektur, modeller og rammeverk som gir føringer |
| `samarbeidsfora/` | Teknisk mappe for samhandlingsarenaer og organisering: fora, råd, nettverk og samordningsarenaer |
| `rammer-og-virkemidler/` | Teknisk mappe for økonomiske og juridiske rammer og virkemidler når slike ressurser etableres |

---

## Verktøy for å lage ressursbeskrivelser

Bruk disse systemprompter og maler når du skal lage eller oppdatere innhold:

| Rammeverkskategori | Systempromt (AI-instruks) | Mal |
|---|---|---|
| Gjenbrukbare løsninger | `config/prompts/operative-ressurs-canvas.system.md` | `config/templates/operative-ressurs-template.md` |
| Standarder og veiledning | `config/prompts/normerende-ressurs-canvas.system.md` | `config/templates/normerende-ressurs-template.md` |
| Samhandlingsarenaer og organisering | `config/prompts/samarbeidsforum-canvas.system.md` | `config/templates/samarbeidsforum-template.md` |
| Økonomiske og juridiske rammer og virkemidler | `config/prompts/okonomiske-og-juridiske-rammer-og-virkemidler-canvas.system.md` | `config/templates/okonomiske-og-juridiske-rammer-og-virkemidler-template.md` |

Last systemprompten i din AI-assistent **før** du begynner på innholdet, slik at navneregler, kildehenting og feltstruktur følges riktig.

---

## Hvordan arbeide med ressurser

### Opprett ny ressurs

1. **Velg ressurstype** og mappe:
   - Gjenbrukbare løsninger → `operative-losninger-og-tjenester/`
   - Standarder og veiledning → `normerende-ressurser/`
   - Samhandlingsarenaer og organisering → `samarbeidsfora/`
   - Økonomiske og juridiske rammer og virkemidler → `rammer-og-virkemidler/`

2. **Tildel ressurs-ID**:
   - Åpne `produktnummerering.md` og finn neste ledige ID hos riktig eier (f.eks. `KS-016` hvis `KS-015` er siste).
   - Noter nummeret lokalt.

3. **Opprett fil med riktig navn**:
   ```
   NN-Ressursnavn-ressurs-type-v1-format.md
   ```
   Eksempler:
   - Gjenbrukbar løsning: `01-ID-porten-operative-ressurs-canvas-v1-copilot.md`
   - Standarder og veiledning: `72-FINT-Informasjonsmodell-v1-codex.md`
   - Samhandlingsarena: `88-Arkitektur-og-standardiseringsradet-v0-codex.md`

   **Konvensjoner:**
   - `NN` = løpenummer (stabil sortering)
   - `v1` = versjon (starter på v1 for ny ressurs)
   - `codex`, `produktkort` osv. = format/type (valgfritt)

4. **Bruk riktig mal**:
   - Gjenbrukbare løsninger: `config/templates/operative-ressurs-template.md`
   - Standarder og veiledning: `config/templates/normerende-ressurs-template.md`
   - Samhandlingsarenaer og organisering: `config/templates/samarbeidsforum-template.md`
   - Økonomiske og juridiske rammer og virkemidler: `config/templates/okonomiske-og-juridiske-rammer-og-virkemidler-template.md`

5. **Legg inn ressurs-ID i dokumentet**:
   - Fyll inn feltet "Ressurs ID" med den ressurs-IDen du tildelte i steg 2 (f.eks. `KS-016`).

6. **Registrer i produktnummerering.md**:
   - Legg til ny rad i riktig eierseksjon:
     ```
   | NN | `EIER-NR` | Ressursnavn | Emne | Kapabiliteter (komma-separert) | [Åpne](path/til/fil.md) |
     ```
   - Generatoren plukker automatisk denne og bygger nettsiden.
   - Hvis ressursen også finnes i `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`, skal den legges inn eller oppdateres der samtidig.

---

### Opprett ny versjon av eksisterende ressurs

En oppdatering av en ressursbeskrivelse er ikke ferdig før også `produktnummerering.md` og relevant kapabilitetsmapping er oppdatert.

1. **Kopier den gamle filen** og gi den nytt versjonsnummer:
   ```
   Gammel: 01-ID-porten-operative-ressurs-canvas-v3-codex.md
   Ny:     01-ID-porten-operative-ressurs-canvas-v4-codex.md
   ```
   (Lopenummeret `NN` blir det samme.)

2. **Oppdater innholdet** i den nye filen.

3. **Oppdater `produktnummerering.md`**:
   - Finn raden med ressursen.
   - Endre dokumentlenken til å peke på den nye filen.

4. **Oppdater `produkt-kapabilitet-koblinger.yaml` ved behov**:
   - Hvis ressursen finnes i `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`, skal `version`, `author`, `relative_path` og `product_url` oppdateres til den nye filen.
   - Hvis hovedfunksjonene er endret vesentlig, skal også selve kapabilitetskoblingene vurderes på nytt.
   - Du kan bruke `python tools/sync-resource-metadata.py --apply` for å synkronisere metadata og opprette manglende mappingoppføringer som førsteutkast.

5. **Valgfritt: Rydd gammel versjon**:
   - Hvis du vil holde repoet rent, kan du slette den gamle filen:
     ```bash
     git rm arkitektur/ressurser/operative-losninger-og-tjenester/01-ID-porten-operative-ressurs-canvas-v3-codex.md
     ```
   - Kommitter med melding som "Update ID-porten to v4" eller "Deprecate ID-porten v3".

---

## Hva som skjer automatisk

- **Nettside**: Generator-scriptet (`web/hugo-prototype/scripts/generate-products.ps1`) leser `produktnummerering.md` og bygger ressursovesiktssidene og filtrert oversikt med alle registrerte ressurser.
- **Visning**: Nettsiden viser alltid **siste versjon som register og kapabilitetsmapping peker til**.
- **Søk og filtrering**: Besøkende kan filtrere etter kategori, eier og kapabilitet.
- **Kvalitetsport**: Lokale hooks og GitHub Actions stopper commit, push eller publisering hvis `produktnummerering.md` eller `produkt-kapabilitet-koblinger.yaml` peker til eldre versjoner.
- **Førsteutkast til mapping**: `tools/sync-resource-metadata.py --apply` kan fylle inn manglende mappingoppføringer og oppdatere metadata, men kapabilitetskoblingene må fortsatt kvalitetssikres faglig.

---

## Kobling til nettside

Når du legger inn en ressurs og kan nå finne den på:
- **Toppnivå**: `https://suphiro-arch.github.io/NA-kunnskap/ressursoversikt/` (alle ressurser)
- **Kategori**: `/ressursoversikt/produkter/operative-losninger-og-tjenester/`, `/normerende-ressurser/`, `/samarbeidsfora/` og `/rammer-og-virkemidler/`
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
A: Nei – du kan beholde dem i Git for historiebakgrunn. Generator-scriptet viser **kun den versjonen som registeret peker til**, og kapabilitetssidene bruker versjonen i `produkt-kapabilitet-koblinger.yaml`. Gamle filer blir ignorert så lenge begge pekerne er oppdatert. Du kan:
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

**Sikkerhet:** Hvis du glemmer å oppdatere registeret eller kapabilitetsmappingen etter å ha opprettet ny versjon, skal lokale hooks og GitHub Actions stoppe endringen før publisering.
