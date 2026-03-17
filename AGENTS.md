# Repo-regler for assistenter

Denne fila beskriver generelle regler som skal gjelde ved arbeid i dette repoet.

## Generelt
- Skriv på norsk i dokumentinnhold, forklaringer og nye markdownfiler.
- Bruk vanlig norsk tegnsett i dokumentinnhold: `æ`, `ø` og `å`.
- Bruk ASCII bare der tekniske begrensninger krever det, for eksempel i filnavn, slugger, kode eller enkelte lokale git-hooker.
- Bevar etablert struktur i repoet: `arkitektur/` for faglig arkitekturgrunnlag, `config/` for regler og maler, `results/` for leveranser, `web/` for Hugo-prototypen, `sources/` for kildegrunnlag og `briefs/` for arbeidsstyring og handover.
- Tolking av mapper:
  - `arkitektur/` brukes for strukturert arkitekturgrunnlag, som kapabiliteter, prinsipper og produktnummerering.
  - `results/` brukes for leveranser og innhold som skal kunne gjenbrukes direkte.
  - `briefs/` brukes for arbeidsstyring, handover, beslutninger og mellomdokumenter.
  - `briefs/arbeidsstyring-og-handover/` brukes for større arbeidsnotater, MVP-skisser, handover-dokumenter og lignende som ikke er sluttleveranser.
- Les `README.md` i aktuell mappe når oppgaven berører den delen av repoet, slik at lokal struktur og arbeidsmåte følges.

## Produktbeskrivelser
- Bruk alltid høyeste eksisterende versjonsnummer for et produkt som primært utgangspunkt, uavhengig av om siste versjon er laget av `codex`, `copilot` eller en person.
- Eldre versjoner skal bare brukes som supplement for historikk, sammenligning eller endringsforståelse.
- Følg metoden i [config/prompts/produkt-canvas.system.md](/c:/Users/HILROS/NA-kunnskap/config/prompts/produkt-canvas.system.md) ved arbeid med produkt-canvas.
- Ved opprettelse av nye produktbeskrivelser skal [config/prompts/produkt-canvas.system.md](/c:/Users/HILROS/NA-kunnskap/config/prompts/produkt-canvas.system.md) alltid brukes som styrende instruks.
- Nye produktfiler skal følge gjeldende versjoneringsregel i promptfila.

## Kilder og analyse
- Bruk `sources/links.md` som førstevalg for eksterne kilder.
- Gå bredere enn lenkene i `sources/links.md` bare når de er utilstrekkelige, utdaterte eller utilgjengelige.
- Hvis arbeidet bruker bredere søk enn `sources/links.md`, skal de ekstra kildene nevnes eksplisitt i dokumentasjonen eller leveransen.
- Skill tydelig mellom fakta, deduksjon og usikkerhet.
- Hvis en påstand ikke kan bekreftes i tilgjengelige kilder, skal dette sies tydelig i teksten.

## Innhold og språkføring
- Skriv dokumentasjon for målgruppen for nasjonal arkitektur, med tydelig og direkte språk.
- Skriv i aktiv form når det er naturlig, ikke i passiv eller distansert referatform.
- Skriv selvstendige beskrivelser for målgruppen, ikke referat av nettsider eller dokumentasjon.
- Unngå formuleringer som `nettsiden sier`, `kilden beskriver` og lignende i hovedteksten.
- Gjenfortell og syntetiser kilder på en egnet måte for målgruppen, og legg heller ved lenker enn å vise til ordlyden andre steder.
- Syntetiser kilder til én samlet forklaring med sporbare henvisninger.

## Hugo-prototype
- Når produktbeskrivelser som mater web-oversikter endres, oppdater relevante genererte oversikter i `web/hugo-prototype/content/`.
- Bevar nettstedet som en lettlest dokumentasjonsside med tydelig navigasjon og lesbar tekst.
- Unngå designgrep som gjør dokumentasjon vanskeligere å lese eller navigere.

## Arbeidsflyt
- Oppdater `briefs/next-step.md` når arbeid endrer hva som er gjort eller hva som gjenstår.
- Oppdater `briefs/decisions.md` når det tas varige metode- eller arkitekturvalg.
- Legg nye arbeidsdokumenter og handover-notater i `briefs/arbeidsstyring-og-handover/` når de ikke hører hjemme i `results/`.
- Hvis nye generelle regler blir viktige for repoet, legg dem i denne fila heller enn å spre dem tilfeldig i enkeltfiler.
