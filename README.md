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
- [AGENTS.md](/c:/Users/HILROS/NA-kunnskap/AGENTS.md): generelle repo-regler for assistenter
- [operative-ressurs-canvas.system.md](/c:/Users/HILROS/NA-kunnskap/config/prompts/operative-ressurs-canvas.system.md): metode for operative ressursbeskrivelser og forbedringsarbeid
- [normerende-ressurs-canvas.system.md](/c:/Users/HILROS/NA-kunnskap/config/prompts/normerende-ressurs-canvas.system.md): metode for normerende ressursbeskrivelser (standarder, veiledere, rammeverk)
- [samarbeidsforum-canvas.system.md](/c:/Users/HILROS/NA-kunnskap/config/prompts/samarbeidsforum-canvas.system.md): metode for beskrivelser av samarbeidsfora og koordineringsarenaer
- [briefs/README.md](/c:/Users/HILROS/NA-kunnskap/briefs/README.md): hvordan `briefs/` brukes til arbeidsstyring og handover
- [struktur-og-bearbeiding.md](/c:/Users/HILROS/NA-kunnskap/arkitektur/struktur-og-bearbeiding.md): hvordan råkilder, kuraterte arbeidsfiler og videre bruk henger sammen i repoet

## Arbeidsflyt

### Ressursbeskrivelser
1. Samle og verifiser kilder i `sources/` og offisielle dokumentasjonskilder.
2. Last riktig systempromt (operativ, normerende eller samarbeidsforum) og lag eller oppdater ressursbeskrivelsen.
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

## Rådata og bearbeiding
- `sources/` inneholder råkilder, lenkelister og sammenligningsgrunnlag.
- `sources/2025-03-18-Nasjonal Arkitektur.xml` er råmodellen for kapabiliteter og prinsipper.
- `sources/2025-03-18-Nasjonal Arkitektur.xml` er også råkilde for modellens målspor.
- `arkitektur/kapabiliteter/capabilities.yaml` er den kuraterte arbeidsfila for kapabilitetsstrukturen.
- `arkitektur/prinsipper/principles.md` er den kuraterte arbeidsfila for prinsipper og deres kobling til hovedkapabiliteter.
- `arkitektur/maal/maal.md` er den kuraterte arbeidsfila for mål og overordnet målkobling i modellen.
- `arkitektur/ressurser/produktnummerering.md` er operativ master for produktregister, ressurs-ID-er og statusoversikt.
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` er operativ master for koblingen mellom produkter og kapabiliteter.
- `arkitektur/ressurser/operative-losninger-og-tjenester/` inneholder produktbeskrivelser som bygger på disse arbeidsfilene.
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
