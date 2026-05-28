---
date: 2026-05-27
author: codex
status: draft
topic: overgang-til-rammeverkskategorier
sources:
  - brukerinnspill-med-modellbilde-2026-05-27
  - arkitektur/ressurser/styringsregler.md
  - arkitektur/ressurser/README.md
  - arkitektur/ressurser/produktnummerering.md
  - web/hugo-prototype/scripts/generate-products.ps1
  - web/hugo-prototype/README.md
---

# Plan for overgang til nye ressurskategorier

## Status 2026-05-28

Første gjennomføringsbolk er startet. Webgenerator, styringsregler, README-er og mal-/promptgrunnlag oppdateres til fire rammeverkskategorier. `Andre ressurser` fjernes som publisert kategori, og uklassifiserte ressursstier skal håndteres som avvik. Kategorien `Økonomiske og juridiske rammer og virkemidler` etableres teknisk, men får ingen automatisk flytting av eksisterende normerende ressurser i denne runden.

## Formål

Nettsiden skal ligge tettere på rammeverket der `Ressurs` er felles overbygning, med tydeligere underkategorier:

- Gjenbrukbar løsning
- Standarder og veiledning
- Samhandlingsarenaer og organisering
- Økonomiske og juridiske rammer og virkemidler

Planen legger opp til en trygg overgang uten å endre kapabilitetsmapping eller registerpeking for eksisterende ressurser i første runde. Hovedgrepet er å endre språk, kategori- og malnavn kontrollert, fjerne behovet for en egen `Andre ressurser`-kategori, og først senere vurdere om noen ressurser faktisk bør flyttes mellom de fire rammeverkskategoriene.

## Kort anbefaling

Start med et synlig navne- og presentasjonsløft i weben, men behold dagens mapper, register og kapabilitetsmapping uendret. Det gir raskere samsvar med rammeverket uten å skape risiko for ødelagte lenker, uventet remapping eller stor filflytting.

Bruk de fire rammeverkskategoriene som målstruktur, og fjern `Andre ressurser` som synlig kategori i planen. De fleste eksisterende normerende ressurser bør som hovedregel ligge under `Standarder og veiledning`. `Økonomiske og juridiske rammer og virkemidler` bør innføres som egen kategori i målbildet, men ikke brukes til automatisk masseflytting før kriteriene er presisert.

## Foreslått begrepsmapping

| Dagens kategori | Ny rammeverkskategori | Første trygge grep |
|---|---|---|
| Operative løsninger og tjenester | Gjenbrukbare løsninger | Endre synlig tittel, beskrivelse og veiledningstekst. Behold eksisterende mappe og slugg i første runde. |
| Normerende ressurser | Standarder og veiledning | Endre synlig tittel og malnavn. Presiser at kategorien dekker standarder, veiledere, referansearkitektur, modeller og rammeverk som gir føringer. |
| Samarbeidsfora | Samhandlingsarenaer og organisering | Endre synlig tittel og malnavn. Utvid språk fra rene fora til arenaer, organisering, roller, styringslinjer og koordineringsmekanismer. |
| Ikke etablert som egen kategori | Økonomiske og juridiske rammer og virkemidler | Etabler som fjerde rammeverkskategori, men start med tydelige kriterier og manuell vurdering. Ikke masseflytt eksisterende ressurser før klassifiseringsregelen er presisert. |

## Prinsipper for trygg overgang

- `arkitektur/ressurser/produktnummerering.md` skal fortsatt være operativ master for ressurs-ID, dokumentlenke og registerstatus.
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` skal ikke endres bare fordi kategorinavn endres.
- Eksisterende ressursfiler skal ikke få ny versjon bare på grunn av kategorinavn.
- Eksisterende URL-er bør beholdes i første runde, særlig `ressursoversikt/produkter/...`.
- Nye kategorinavn skal først inn i webtekst, README, styringsregler, promptnavn og malnavn.
- `Andre ressurser` skal ikke videreføres som synlig målgruppekategori. Ressurser som ikke passer bør heller få avklart kategori før de publiseres i rammeverksstrukturen.
- Reell omplassering av ressurser skal være egen beslutning, med egen validering.

## Fase 0: Beslutt navnestandard

Målet er å bli enige om navn som skal brukes konsekvent i nettsiden, dokumentasjon og maler.

Anbefalt norsk visningsnavn:

- `Ressurser`
- `Gjenbrukbare løsninger`
- `Standarder og veiledning`
- `Samhandlingsarenaer og organisering`
- `Økonomiske og juridiske rammer og virkemidler`

Anbefalt teknisk slug dersom nye URL-er eller mapper senere innføres:

- `gjenbrukbare-losninger`
- `standarder-og-veiledning`
- `samhandlingsarenaer-og-organisering`
- `rammer-og-virkemidler`

`rammer-og-virkemidler` er kortere enn full tittel og tåler senere justering i visningstekst uten at URL må endres.

## Fase 1: Endre nettsiden uten å flytte innhold

Målet er å få nettsiden til å speile rammeverket med lav risiko.

Oppgaver:

- Oppdater `$resourceTypeDefinitions` i `web/hugo-prototype/scripts/generate-products.ps1` med nye synlige titler og beskrivelser.
- Fjern `Andre ressurser` som synlig kategori fra generatorens målstruktur.
- Legg inn fire målgrupper i weben:
  - `Gjenbrukbare løsninger`
  - `Standarder og veiledning`
  - `Samhandlingsarenaer og organisering`
  - `Økonomiske og juridiske rammer og virkemidler`
- Behold eksisterende slugger i første omgang:
  - `operative-losninger-og-tjenester`
  - `normerende-ressurser`
  - `samarbeidsfora`
- Bruk en ny teknisk slug for fjerde kategori når den får egen underside, fortrinnsvis `rammer-og-virkemidler`.
- Oppdater ingress og korttekster i `web/hugo-prototype/content/ressursoversikt/_index.md` via generator, ikke manuelt.
- Endre omtale fra `produkter` til `ressurser` der teksten er brukerrettet, men ikke nødvendigvis i tekniske stier ennå.
- Regenerer ressursoversikten og kontroller at antall ressurser per kategori er uendret.

Akseptansekriterier:

- Ressursoversikten viser nye kategorinavn.
- `Andre ressurser` vises ikke som egen kategori.
- Alle eksisterende ressurskort vises fortsatt.
- Kapabilitetssider peker fortsatt til samme ressursfiler.
- Ingen register- eller mappingendringer er nødvendige.

## Fase 2: Oppdater styringsspråk og malnavn

Målet er å gjøre repoets arbeidsmåte konsistent med rammeverket uten å bryte eksisterende automatisering.

Oppgaver:

- Oppdater `arkitektur/ressurser/styringsregler.md` med de nye kategorinavnene og en overgangstabell fra gamle til nye navn.
- Oppdater `arkitektur/ressurser/README.md`, `README.md`, `AGENTS.md` og `web/hugo-prototype/README.md` med ny begrepsbruk.
- Behold gamle prompt- og malfiler i første runde, men legg inn nye visningsnavn i tittel og bruksforklaring.
- Vurder senere teknisk omdøping av filer:
  - `operative-ressurs-template.md` kan bli `gjenbrukbar-losning-template.md`
  - `normerende-ressurs-template.md` kan bli `standarder-og-veiledning-template.md`
  - `samarbeidsforum-template.md` kan bli `samhandlingsarena-og-organisering-template.md`
  - en ny mal for `rammer-og-virkemidler` bør bare lages hvis kategorien blir egen primærkategori

Anbefaling:

Ikke rename prompt- og malfiler samtidig med webendringen. Først endres innhold og henvisninger. Selve filnavnene kan tas i en egen runde når alle verktøy, AGENTS-regler og gamle referanser er kartlagt.

## Fase 3: Presiser fjerde kategori

Målet er å gjøre `Økonomiske og juridiske rammer og virkemidler` til en reell rammeverkskategori uten å bruke den som ny restkategori.

Beslutningsspørsmål:

- Hvilke kriterier skiller denne kategorien fra `Standarder og veiledning`?
- Skal juridiske rammer som forskrifter, rundskriv og regelverksveiledere flyttes hit, eller fortsatt ligge under standarder og veiledning med juridisk type inntil videre?
- Skal økonomiske virkemidler beskrives som egne ressurser selv når de ikke er normerende dokumenter?
- Hvordan skal ressurser håndteres dersom de både er juridiske føringer og praktisk veiledning?

Foreslått midlertidig regel:

Bruk `Standarder og veiledning` for de fleste eksisterende normerende ressurser inntil videre. Ta `Økonomiske og juridiske rammer og virkemidler` inn som fjerde kategori i webstrukturen, men flytt bare ressurser dit etter eksplisitt vurdering mot kriterier i `styringsregler.md`.

## Fase 4: Eventuell URL- og mappestruktur

Målet er teknisk opprydding når begrepene er stabile.

Mulige senere endringer:

- Endre webstien fra `ressursoversikt/produkter/` til `ressursoversikt/ressurser/`.
- Innføre nye slugger for undersider.
- Legge inn aliaser eller redirect-regler fra gamle sider til nye sider.
- Vurdere om mapper i `arkitektur/ressurser/` skal omdøpes, eller om de bør beholdes som stabile tekniske mapper med nye visningsnavn.
- Sikre at det ikke finnes en publisert `andre-ressurser`-side etter overgangen.

Anbefaling:

Utsett URL- og mappeendringer til etter at webtekst, styringsregler og maler er oppdatert. URL-stabilitet er viktigere enn perfekt teknisk navnesamsvar i første overgang.

## Fase 5: Validering og publiseringskontroll

Kjør disse kontrollene etter hver gjennomføringsrunde:

```powershell
python tools/sync-resource-metadata.py
powershell -ExecutionPolicy Bypass -File web/hugo-prototype/scripts/generate-products.ps1
python tools/check-resource-version-sync.py
python web/hugo-prototype/scripts/validate-text-encoding.py
powershell -ExecutionPolicy Bypass -File tools/check-mojibake.ps1
```

Ved endringer i kapabilitetsvisning:

```powershell
python web/hugo-prototype/scripts/generate-capabilities.py
python web/hugo-prototype/scripts/sync-principles.py
```

Kontroller i tillegg:

- ressursantall før og etter generering
- at alle fire rammeverkskategorier er synlige eller bevisst håndtert
- at eksisterende lenker fra kapabilitetssider fortsatt fungerer
- at nye og gamle begreper ikke blandes forvirrende i samme brukerflate

## Risikoer og tiltak

| Risiko | Tiltak |
|---|---|
| Fjerde kategori skaper forventning om remapping før kriteriene finnes | Innfør den som egen rammeverkskategori, men flytt bare konkrete ressurser etter manuell vurdering. |
| Fjerning av `Andre ressurser` gjør at uklassifiserte ressurser forsvinner fra oversikten | Kjør kontroll som viser eventuelle uklassifiserte ressurser som avvik, ikke som egen publisert kategori. |
| Gamle URL-er brytes | Behold gamle slugger i første runde, og bruk aliaser ved senere URL-endring. |
| Malnavn endres før agenter og README-er er oppdatert | Endre innhold og omtale først, filnavn senere. |
| `produktnummerering.md` får misvisende navn i ny ressursmodell | Behold filnavnet inntil en egen beslutning om eventuell `ressursregister.md` er tatt. |
| Webgeneratoren får blandet ansvar for fagkategori og teknisk mappe | Skill mellom teknisk slug, visningsnavn og klassifiseringsregel i scriptet. |

## Anbefalt første gjennomføringsbolk

1. Oppdater `generate-products.ps1` med nye synlige kategorinavn og beskrivelser, fjern `Andre ressurser` og behold dagens slugger for de tre eksisterende kategoriene.
2. Regenerer ressursoversikten.
3. Legg inn `rammer-og-virkemidler` som teknisk mål for fjerde kategori, men uten automatisk flytting av eksisterende normerende ressurser.
4. Oppdater `arkitektur/ressurser/styringsregler.md` og relevante README-er med overgangstabell.
5. Oppdater prompt- og maltekster med nye visningsnavn, uten å rename filer.
6. Kjør validering og noter resultat i `briefs/next-step.md`.

Dette gir en trygg første leveranse som gjør nettsiden mer rammeverksnær uten å åpne en større migrering av alle ressursene.
