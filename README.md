# NA-kunnskap

Repo for arbeid med nasjonal arkitektur, produktbeskrivelser, kapabiliteter, prinsipper og en Hugo-basert dokumentasjonsprototype.

## Formål
- samle og videreutvikle produktbeskrivelser som grunnlag for arkitekturvurderinger
- strukturere kapabiliteter, prinsipper og ressursoversikter
- publisere en lettlest prototype på web med innhold fra repoet
- bruke AI-assistenter på en sporbar og konsistent måte i analyse- og dokumentasjonsarbeid

## Viktigste mapper
- `results/`: leveranser, analyser og annet gjenbrukbart sluttinnhold
- `sources/`: kildegrunnlag, lenker og rånotater
- `briefs/`: arbeidsstyring, handover og beslutningsstøtte
- `config/`: prompts, maler og annen styrende konfigurasjon
- `arkitektur/`: strukturerte oversikter, blant annet kapabiliteter, produktregister og produktbeskrivelser
- `arkitektur/maal/`: kuratert målspor for arkitekturmodellen
- `web/hugo-prototype/`: Hugo-kildekode for dokumentasjonsprototypen

## Styrende filer
- [AGENTS.md](/c:/Users/HILROS/NA-kunnskap/AGENTS.md): generelle repo-regler for assistenter
- [produkt-canvas.system.md](/c:/Users/HILROS/NA-kunnskap/config/prompts/produkt-canvas.system.md): metode for produkt-canvas og forbedringsarbeid
- [briefs/README.md](/c:/Users/HILROS/NA-kunnskap/briefs/README.md): hvordan `briefs/` brukes til arbeidsstyring og handover
- [struktur-og-bearbeiding.md](/c:/Users/HILROS/NA-kunnskap/arkitektur/struktur-og-bearbeiding.md): hvordan råkilder, kuraterte arbeidsfiler og videre bruk henger sammen i repoet

## Arbeidsflyt i korte trekk
1. Samle og verifiser kilder i `sources/` og offisielle dokumentasjonskilder.
2. Kurater råmodeller og strukturdata i `arkitektur/`, der `capabilities.yaml` og `principles.md` er arbeidsfilene som brukes videre.
3. Oppdater eller lag innhold i `results/` etter gjeldende metode og versjonering.
4. Oppdater eventuelle genererte oversikter i Hugo-prototypen når innholdet mater nettsiden.
5. Logg status i `briefs/next-step.md` og varige valg i `briefs/decisions.md`.

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
- bruk `tools/safe_bulk_text_repair.py` ved større oppryddinger i språk/encoding

Anbefalt bruk av sikker reparasjon:

1. Kjor alltid dry-run forst:
  `python tools/safe_bulk_text_repair.py`
2. Vurder diff for filene scriptet foreslar.
3. Kjor apply med backup:
  `python tools/safe_bulk_text_repair.py --apply`
4. Valider etterpa:
  `python web/hugo-prototype/scripts/validate-text-encoding.py`

Scriptet lager automatisk backup under `.backups/encoding/<timestamp>/` ved `--apply`.


