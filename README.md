# NA-kunnskap

Repo for arbeid med nasjonal arkitektur, produktbeskrivelser, kapabiliteter, prinsipper og en Hugo-basert dokumentasjonsprototype.

## FormÃ¥l
- samle og videreutvikle produktbeskrivelser som grunnlag for arkitekturvurderinger
- strukturere kapabiliteter, prinsipper og ressursoversikter
- publisere en lettlest prototype pÃ¥ web med innhold fra repoet
- bruke AI-assistenter pÃ¥ en sporbar og konsistent mÃ¥te i analyse- og dokumentasjonsarbeid

## Viktigste mapper
- `results/`: leveranser, analyser og annet gjenbrukbart sluttinnhold
- `sources/`: kildegrunnlag, lenker og rÃ¥notater
- `briefs/`: arbeidsstyring, handover og beslutningsstÃ¸tte
- `config/`: prompts, maler og annen styrende konfigurasjon
- `arkitektur/`: strukturerte oversikter, blant annet kapabiliteter, produktregister og produktbeskrivelser
- `arkitektur/maal/`: kuratert mÃ¥lspor for arkitekturmodellen
- `web/hugo-prototype/`: Hugo-kildekode for dokumentasjonsprototypen

## Styrende filer
- [AGENTS.md](/c:/Users/HILROS/NA-kunnskap/AGENTS.md): generelle repo-regler for assistenter
- [produkt-canvas.system.md](/c:/Users/HILROS/NA-kunnskap/config/prompts/produkt-canvas.system.md): metode for produkt-canvas og forbedringsarbeid
- [briefs/README.md](/c:/Users/HILROS/NA-kunnskap/briefs/README.md): hvordan `briefs/` brukes til arbeidsstyring og handover
- [struktur-og-bearbeiding.md](/c:/Users/HILROS/NA-kunnskap/arkitektur/struktur-og-bearbeiding.md): hvordan rÃ¥kilder, kuraterte arbeidsfiler og videre bruk henger sammen i repoet

## Arbeidsflyt i korte trekk
1. Samle og verifiser kilder i `sources/` og offisielle dokumentasjonskilder.
2. Kurater rÃ¥modeller og strukturdata i `arkitektur/`, der `capabilities.yaml` og `principles.md` er arbeidsfilene som brukes videre.
3. Oppdater eller lag innhold i `results/` etter gjeldende metode og versjonering.
4. Oppdater eventuelle genererte oversikter i Hugo-prototypen nÃ¥r innholdet mater nettsiden.
5. Logg status i `briefs/next-step.md` og varige valg i `briefs/decisions.md`.

## RÃ¥data og bearbeiding
- `sources/` inneholder rÃ¥kilder, lenkelister og sammenligningsgrunnlag.
- `sources/2025-03-18-Nasjonal Arkitektur.xml` er rÃ¥modellen for kapabiliteter og prinsipper.
- `sources/2025-03-18-Nasjonal Arkitektur.xml` er ogsÃ¥ rÃ¥kilde for modellens mÃ¥lspor.
- `arkitektur/kapabiliteter/capabilities.yaml` er den kuraterte arbeidsfila for kapabilitetsstrukturen.
- `arkitektur/prinsipper/principles.md` er den kuraterte arbeidsfila for prinsipper og deres kobling til hovedkapabiliteter.
- `arkitektur/maal/maal.md` er den kuraterte arbeidsfila for mÃ¥l og overordnet mÃ¥lkobling i modellen.
- `arkitektur/ressurser/produktnummerering.md` er operativ master for produktregister, ressurs-ID-er og statusoversikt.
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` er operativ master for koblingen mellom produkter og kapabiliteter.
- `arkitektur/ressurser/operative-losninger-og-tjenester/` inneholder produktbeskrivelser som bygger pÃ¥ disse arbeidsfilene.
- Hugo-prototypen bruker de kuraterte arbeidsfilene og genererte oversiktene, ikke rÃ¥-XML direkte.

## Webprototype
- Hugo-prototypen bygges fra `web/hugo-prototype/`.
- Publisert base-URL er konfigurert til:
  - `https://suphiro-arch.github.io/NA-kunnskap/`
- GitHub Pages publiserer bygget direkte fra GitHub Actions som artifact-deploy.

## Prinsipper for innhold
- skriv pÃ¥ norsk i dokumentinnhold
- bruk `Ã¦`, `Ã¸` og `Ã¥` i vanlig tekst
- skriv for mÃ¥lgruppen for nasjonal arkitektur i aktiv form
- gjenfortell og syntetiser innholdet med egne formuleringer i stedet for Ã¥ referere til hva andre kilder sier
- legg ved lenker til kildene i stedet for Ã¥ skrive hovedteksten som henvisning til andre dokumenter
- bruk `sources/links.md` som fÃ¸rstevalg for eksterne kilder
- oppgi ekstra kilder eksplisitt nÃ¥r arbeidet gÃ¥r bredere enn den lokale lenkelista
- skill mellom fakta, deduksjon og usikkerhet

