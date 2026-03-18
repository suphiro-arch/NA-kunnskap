# NA-kunnskap

Repo for arbeid med nasjonal arkitektur, produktbeskrivelser, kapabiliteter, prinsipper og en Hugo-basert dokumentasjonsprototype.

## Formål
- samle og videreutvikle produktbeskrivelser som grunnlag for arkitekturvurderinger
- strukturere kapabiliteter, prinsipper og ressursoversikter
- publisere en lettlest prototype på web med innhold fra repoet
- bruke AI-assistenter på en sporbar og konsistent måte i analyse- og dokumentasjonsarbeid

## Viktigste mapper
- `results/`: leveranser og produktbeskrivelser som brukes videre som kunnskapsgrunnlag
- `sources/`: kildegrunnlag, lenker og rånotater
- `briefs/`: arbeidsstyring, handover og beslutningsstøtte
- `config/`: prompts, maler og annen styrende konfigurasjon
- `arkitektur/`: strukturerte oversikter, blant annet kapabiliteter og produktnummerering
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
- `arkitektur/produkter/produktnummerering.md` og `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` er kuraterte arbeidsfiler for ressurser og koblinger.
- `results/Produktbeskrivelser/` inneholder analyse- og leveransefiler som bygger på disse arbeidsfilene.
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
