# NA-kunnskap

Repo for arbeid med nasjonal arkitektur, produktbeskrivelser, kapabiliteter, prinsipper og en Hugo-basert dokumentasjonsprototype.

## Formål
- samle og videreutvikle produktbeskrivelser som grunnlag for arkitekturvurderinger
- strukturere kapabiliteter, prinsipper og ressursoversikter
- publisere en lettlest prototype på web med innhold fra repoet
- bruke AI-assistenter på en sporbar og konsistent måte i analyse- og dokumentasjonsarbeid

## Viktigste mapper
- `analyser/`: kapabilitetsanalyser, case-analyser og gjenbrukbare faglige leveranser
- `sources/`: kildegrunnlag, lenker og rånotater
- `briefs/`: arbeidsstyring, handover og beslutningsstøtte
- `config/`: prompts, maler og annen styrende konfigurasjon
- `arkitektur/`: strukturerte oversikter, blant annet kapabiliteter, produktregister og ressursbeskrivelser
- `arkitektur/maal/`: kuratert målspor for arkitekturmodellen
- `web/hugo-prototype/`: Hugo-kildekode for dokumentasjonsprototypen

## Styrende filer
- [AGENTS.md](AGENTS.md): generelle repo-regler for assistenter
- [styringsregler.md](arkitektur/ressurser/styringsregler.md): avgjør hvilken rammeverkskategori en kandidat tilhører – les denne først
- [operative-ressurs-canvas.system.md](config/prompts/operative-ressurs-canvas.system.md): metode for gjenbrukbare løsninger og forbedringsarbeid
- [normerende-ressurs-canvas.system.md](config/prompts/normerende-ressurs-canvas.system.md): metode for standarder og veiledning
- [samarbeidsforum-canvas.system.md](config/prompts/samarbeidsforum-canvas.system.md): metode for samhandlingsarenaer og organisering
- [designprofil-rapporter-og-presentasjoner.system.md](config/prompts/designprofil-rapporter-og-presentasjoner.system.md): felles designprofil for rapporter, presentasjoner og figurer
- [briefs/README.md](briefs/README.md): hvordan `briefs/` brukes til arbeidsstyring og handover
- [struktur-og-bearbeiding.md](arkitektur/struktur-og-bearbeiding.md): hvordan råkilder, kuraterte arbeidsfiler og videre bruk henger sammen i repoet

## Arbeidsflyt

### Ressursbeskrivelser
1. Samle og verifiser kilder i `sources/` og offisielle dokumentasjonskilder.
2. Bruk `arkitektur/ressurser/styringsregler.md` til å avgjøre rammeverkskategori, last deretter riktig systempromt og lag eller oppdater ressursbeskrivelsen.
3. Oppdater `arkitektur/ressurser/produktnummerering.md` med ny versjonspeker.
4. Kjør `python tools/sync-resource-metadata.py --apply` og `python tools/check-resource-version-sync.py` for å verifisere register og kapabilitetsmapping.
5. Logg status i `briefs/next-step.md` og varige valg i `briefs/decisions.md`.

### Analyser
1. Bruk ressursbeskrivelser, `capabilities.yaml` og `principles.md` som grunnlag.
2. Lag analyse i `analyser/` med versjonert filnavn etter gjeldende navnekonvensjon.
3. Logg funn eller metodiske valg i `briefs/` ved behov.

### Webprototype
1. Oppdater relevante genererte oversikter i `web/hugo-prototype/content/` når ressursbeskrivelser eller kapabilitetsmapping endres.
2. Bruk `web/hugo-prototype/scripts/validate-text-encoding.py` for å validere encoding før build.
3. GitHub Actions bygger og publiserer automatisk ved push til main.

## Slik bruke innholdet med KI (utkast)

Dette er en enkel oppskrift du kan bruke for å kombinere innholdet i repoet med din egen problemstilling, uten egen backend eller ekstra infrastruktur.

Kort forklart: du beskriver problemet ditt, gir KI-en tilgang til relevant innhold, og ber den koble problemet til kapabiliteter og mulig gjenbruk i eksisterende løsninger.

### Mål
- gjøre repoet lett å bruke som åpen kunnskapskilde i vanlige KI-verktøy
- sikre sporbarhet til konkrete filer i repoet
- kombinere repoets innhold med annen relevant informasjon på en kontrollert måte

### Hvem dette er for
- deg som jobber med utviklingsbehov, prioritering eller arkitekturvalg
- deg som ikke nødvendigvis bruker GitHub til daglig
- deg som vil bruke KI til rask orientering før mer formell vurdering

### Hva du gjør i praksis
1. Skriv problemstillingen din så konkret du kan.
2. Legg ved relevant innhold fra repoet på én av disse måtene:
  - lim inn tekstutdrag direkte i KI-verktøyet
  - legg ved lenke til nettsiden (Hugo-prototypen)
  - legg ved lenke til fil i GitHub hvis du har den
  - start gjerne med registerfila arkitektur/ressurser/produktnummerering.md for oversikt over ressurser og gjeldende versjoner
3. Be KI-en peke ut hvilke kapabiliteter som er nødvendige for å løse behovet.
4. Be KI-en foreslå hvilke eksisterende ressurser/løsninger som kan gjenbrukes.
5. Be KI-en vise hva som mangler (gap), og hva du bør gjøre først med lav terskel og lav kost.

### Lavterskel oppskrift (uten særlige kostnader)
1. Beskriv behovet ditt så detaljert som mulig: mål, kontekst, aktører, dagens løsning, begrensninger, avhengigheter, risiko og hva du ønsker å beslutte.
2. Be KI-en bruke repoet som hovedkilde, og bare supplere med annen informasjon når dette merkes tydelig.
3. Be KI-en eksplisitt koble problemstillingen til hvilke kapabiliteter som må styrkes eller etableres.
4. Be KI-en foreslå hvilke eksisterende ressurser/løsninger som kan gjenbrukes for hver nødvendig kapabilitet.
5. Be KI-en vise gap mellom nødvendig kapabilitet og dagens ressursdekning, med forslag til lavterskel neste steg.

### Anbefalt prompt-mal

```text
Du er faglig rådgiver for [sett inn virksomhet, sektor eller problemområde].
Du henvender deg direkte til meg som bruker.

Bruk innhold fra dette repoet som hovedgrunnlag:
- arkitektur/ressurser/
- arkitektur/ressurser/produktnummerering.md
- arkitektur/kapabiliteter/capabilities.yaml
- arkitektur/prinsipper/principles.md
- arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml

Oppgave:
[Lim inn problemstilling, målgruppe og ønsket beslutning]

Innhold du skal bruke:
[Lim inn tekstutdrag, nettsidelenker eller fil-lenker her]

Svarformat:
1. Kort oppsummering av behov
2. Nødvendige kapabiliteter for å løse behovet (med begrunnelse)
3. Mulig gjenbruk: hvilke eksisterende ressurser/løsninger støtter hver kapabilitet
4. Foreslåtte kombinasjoner av løsninger og hvorfor de henger sammen
5. Gap og avklaringer før beslutning
6. Konkrete neste steg (lav terskel, lav kost)

Krav:
- Skill mellom fakta, deduksjon og usikkerhet.
- Henvis til konkrete filstier i repoet.
- Forklar alltid hvordan kildene henger sammen med repoet (for eksempel registermaster -> ressursfil -> kapabilitetskobling).
- Når det er nyttig for deling utenfor repoet, bruk full URL til fil (for eksempel https://github.com/<org>/<repo>/blob/main/<sti>) i tillegg til filsti.
- Hvis du bruker ekstern informasjon, merk den eksplisitt som ekstern.
```

### Lenker og sporbarhet
- Primærinngang for KI-bruk: https://github.com/suphiro-arch/NA-kunnskap/tree/main
- Sekundær inngang for lesing og oversikt: https://suphiro-arch.github.io/NA-kunnskap/
- Mange KI-verktøy forstår relative filstier godt når de har repoet tilgjengelig i samme kontekst.
- Når svaret skal deles utenfor repo-kontekst, bruk fullstendige URL-er i tillegg til filstier.
- Anbefaling: oppgi alltid begge deler når mottaker er ukjent:
  - filsti i repo (for eksempel arkitektur/ressurser/produktnummerering.md)
  - full URL til samme fil i GitHub

Hvis du ikke bruker GitHub selv:
- bruk nettsiden som enkel inngang for å finne tema og begreper
- lim deretter inn GitHub-lenken over i KI-verktøyet og be verktøyet bruke repoet som hovedkilde
- be KI-en oppgi hvilke filer og lenker den faktisk bygger rådene på

For minst mulig manuell jobb:
- start med én felles lenke til repoet (tree/main)
- legg bare ved ekstra tekst hvis KI-svaret blir for generelt eller treffer dårlig

### Minimumskrav for kvalitet
- Ikke gi råd uten kildepeker til repoet.
- Unngå generiske svar: anbefalinger skal forankres i konkret kobling mellom problemstilling -> kapabilitet -> mulig gjenbruk i løsninger.
- Beskriv alltid hva som mangler for å kunne gi et tryggere svar.

### Når denne metoden passer best
- tidlig fase av problemavklaring
- vurdering av gjenbruk før man lager nye tiltak
- behov for rask oversikt med sporbare kilder

### Når den ikke er nok alene
- formelle juridiske vurderinger
- anskaffelser eller styringsvedtak som krever kvalitetssikret beslutningsgrunnlag
- saker med sensitivt eller ikke-offentlig datagrunnlag

## Rådata og bearbeiding
- `sources/` inneholder råkilder, lenkelister og sammenligningsgrunnlag.
- `sources/Nasjonal Arkitektur kapabilitetsmodell-2026-05-20.archimate` er råmodellen for kapabiliteter, prinsipper og modellens målspor.
- `arkitektur/kapabiliteter/capabilities.yaml` er den kuraterte arbeidsfila for kapabilitetsstrukturen.
- `arkitektur/prinsipper/principles.md` er den kuraterte arbeidsfila for prinsipper og deres kobling til hovedkapabiliteter.
- `arkitektur/maal/maal.md` er den kuraterte arbeidsfila for mål og overordnet målkobling i modellen.
- `arkitektur/ressurser/produktnummerering.md` er operativ master for produktregister, ressurs-ID-er og statusoversikt.
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` er operativ master for koblingen mellom produkter og kapabiliteter.
- `arkitektur/ressurser/` inneholder alle ressursbeskrivelser etter rammeverkskategoriene: gjenbrukbare løsninger, standarder og veiledning, samhandlingsarenaer og organisering, og økonomiske eller juridiske rammer og virkemidler.
- Hugo-prototypen bruker de kuraterte arbeidsfilene og genererte oversiktene, ikke rå-XML direkte.

## Webprototype
- Hugo-prototypen bygges fra `web/hugo-prototype/`.
- Publisert base-URL er konfigurert til:
  - `https://suphiro-arch.github.io/NA-kunnskap/`
- GitHub Pages publiserer bygget direkte fra GitHub Actions som artifact-deploy.

## Prinsipper for innhold
- skriv på norsk i dokumentinnhold
- bruk `æ`, `ø` og `å` i vanlig tekst
- skriv for målgruppen for nasjonal arkitektur i aktiv form
- gjenfortell og syntetiser innholdet med egne formuleringer i stedet for å referere til hva andre kilder sier
- legg ved lenker til kildene i stedet for å skrive hovedteksten som henvisning til andre dokumenter
- bruk `sources/links.md` som førstevalg for eksterne kilder
- oppgi ekstra kilder eksplisitt når arbeidet går bredere enn den lokale lenkelista
- skill mellom fakta, deduksjon og usikkerhet

## Robust tegnsettingsvern
- bruk `web/hugo-prototype/scripts/validate-text-encoding.py` for å stoppe mistenkelige tegnkodingsfeil og BOM i validerte tekstfiler
- bruk `tools/check-resource-version-sync.py` for å stoppe utdaterte register- og kapabilitetslenker til eldre ressursversjoner
- bruk `tools/sync-resource-metadata.py --apply` for å oppdatere mapping-metadata og opprette manglende mappingoppføringer som førsteutkast
- bruk `tools/safe_bulk_text_repair.py` ved større oppryddinger i språk/encoding
- aktiver lokal pre-commit guard én gang per klone:
  `powershell -ExecutionPolicy Bypass -File tools/setup-git-hooks.ps1`
- setup-scriptet aktiverer både `pre-commit` (staged sjekk) og `pre-push` (full sjekk)
- lokal guard kan kjøres manuelt ved behov:
  `powershell -ExecutionPolicy Bypass -File tools/check-mojibake.ps1 -Root .`
  `python tools/check-resource-version-sync.py`
  `python tools/sync-resource-metadata.py --apply`

Anbefalt bruk av sikker reparasjon:

1. Kjor alltid dry-run forst:
  `python tools/safe_bulk_text_repair.py`
2. Vurder diff for filene scriptet foreslar.
3. Kjor apply med backup:
  `python tools/safe_bulk_text_repair.py --apply`
4. Valider etterpa:
  `python web/hugo-prototype/scripts/validate-text-encoding.py`

Scriptet lager automatisk backup under `.backups/encoding/<timestamp>/` ved `--apply`.
