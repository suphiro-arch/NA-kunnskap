# Repo-regler for assistenter

Denne fila beskriver generelle regler som skal gjelde ved arbeid i dette repoet.

## Generelt
- Skriv på norsk i dokumentinnhold, forklaringer og nye markdownfiler.
- Bruk vanlig norsk tegnsett i dokumentinnhold: `æ`, `ø` og `å`.
- Bruk ASCII bare der tekniske begrensninger krever det, for eksempel i filnavn, slugger, kode eller enkelte lokale git-hooker.
- Bevar etablert struktur i repoet: `arkitektur/` for faglig arkitekturgrunnlag, `config/` for regler og maler, `results/` for leveranser, `web/` for Hugo-prototypen, `sources/` for kildegrunnlag og `briefs/` for arbeidsstyring og handover.
- Tolking av mapper:
  - `arkitektur/` brukes for strukturert arkitekturgrunnlag, som kapabiliteter, mål, prinsipper og produktnummerering.
  - `arkitektur/ressurser/` brukes for styringsregler og struktur for ressursområdet utover klassiske produktbeskrivelser.
  - `results/` brukes for leveranser og innhold som skal kunne gjenbrukes direkte.
  - `briefs/` brukes for arbeidsstyring, handover, beslutninger og mellomdokumenter.
  - `briefs/arbeidsstyring-og-handover/` brukes for større arbeidsnotater, MVP-skisser, handover-dokumenter og lignende som ikke er sluttleveranser.
- Les `README.md` i aktuell mappe når oppgaven berører den delen av repoet, slik at lokal struktur og arbeidsmåte følges.
- Ved arbeid med nye ressurskategorier eller ressurser utover klassiske produkter, bruk `arkitektur/ressurser/styringsregler.md` som styrende klassifisering.
- Ved registerføring av nye ressurser i den brede ressursstrukturen, bruk fortsatt `arkitektur/ressurser/produktnummerering.md` som operativ master for ressurs-ID og registerstatus inntil annet er besluttet.
- Når nye ressursfiler opprettes etter at løpenummer er fastsatt i `arkitektur/ressurser/produktnummerering.md`, skal filnavnet følge samme nummererte mønster som øvrige beskrivelser i porteføljen.
- Ved opprettelse eller revisjon av `normerende ressurser` og `samarbeidsfora`, bruk `config/prompts/ressursbeskrivelser.system.md` sammen med riktig mal i `config/templates/`.

## Produktbeskrivelser
- Bruk alltid høyeste eksisterende versjonsnummer for et produkt som primært utgangspunkt, uavhengig av om siste versjon er laget av `codex`, `copilot` eller en person.
- Eldre versjoner skal bare brukes som supplement for historikk, sammenligning eller endringsforståelse.
- Følg metoden i [config/prompts/produkt-canvas.system.md](/c:/Users/HILROS/NA-kunnskap/config/prompts/produkt-canvas.system.md) ved arbeid med produkt-canvas.
- Ved opprettelse av nye produktbeskrivelser skal [config/prompts/produkt-canvas.system.md](/c:/Users/HILROS/NA-kunnskap/config/prompts/produkt-canvas.system.md) alltid brukes som styrende instruks.
- Nye produktfiler skal følge gjeldende versjoneringsregel i promptfila.
- Nye eller oppdaterte produktbeskrivelser skal lagres som ren `UTF-8`.
- Etter opprettelse eller endring av produktbeskrivelser skal det gjøres en eksplisitt kontroll for tegnkodingsfeil, ikke bare en visuell sjekk i terminalen.
- Hvis tekst viser typiske tegnkodingsfeil med doble bokstavsekvenser eller ødelagte typografitegn, skal fila rettes før commit og før genererte oversikter oppdateres.
- Lokal pre-commit hook for encoding-kontroll skal være aktiv (`tools/setup-git-hooks.ps1`) slik at commits stoppes automatisk ved mojibake.
- I normerende ressursbeskrivelser skal `Status/Livsfase` beskrive status på selve ressursen, ikke status på dokumentutkastet eller ressursbeskrivelsen.
- Tidlige versjoner av normerende ressursbeskrivelser skal som hovedregel beholde hele malstrukturen, og uferdige felt skal merkes eksplisitt i teksten i stedet for å utelates.
- I beskrivelser av samarbeidsfora skal det være eksplisitt om forumet er rådgivende, koordinerende eller besluttende, hvilke ressurser det påvirker, og når det bør involveres i analyse- eller utviklingsløp.

## Kilder og analyse
- Bruk `sources/links.md` som førstevalg for eksterne kilder.
- Gå bredere enn lenkene i `sources/links.md` bare når de er utilstrekkelige, utdaterte eller utilgjengelige.
- Hvis arbeidet bruker bredere søk enn `sources/links.md`, skal de ekstra kildene nevnes eksplisitt i dokumentasjonen eller leveransen.
- Skill tydelig mellom fakta, deduksjon og usikkerhet.
- Hvis en påstand ikke kan bekreftes i tilgjengelige kilder, skal dette sies tydelig i teksten.

## Innhold og språkføring
- Bruk `config/regler/sprakforing.md` som felles språkgrunnlag for dokumentinnhold, analyser og nye promptfiler.
- Skriv dokumentasjon for målgruppen for nasjonal arkitektur, med tydelig og direkte språk.
- Skriv i aktiv form når det er naturlig, ikke i passiv eller distansert referatform.
- Ved revisjon av eksisterende produktbeskrivelser skal etablert tone og språkføring bevares så langt det er faglig forsvarlig.
- Behold velfungerende formuleringer fra siste versjon, og unngå unødvendig full omskriving når målet er forbedring.
- Skriv selvstendige beskrivelser for målgruppen, ikke referat av nettsider eller dokumentasjon.
- Unngå formuleringer som `nettsiden sier`, `kilden beskriver` og lignende i hovedteksten.
- Gjenfortell og syntetiser kilder på en egnet måte for målgruppen, og legg heller ved lenker enn å vise til ordlyden andre steder.
- Syntetiser kilder til én samlet forklaring med sporbare henvisninger.

## Hugo-prototype
- Når produktbeskrivelser som mater web-oversikter endres, oppdater relevante genererte oversikter i `web/hugo-prototype/content/`.
- Bruk `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` som autoritativ masterfil for koblingen mellom produkter og kapabiliteter når weboversikter eller kapabilitetssider oppdateres.
- Bruk `arkitektur/prinsipper/principles.md` som kuratert kilde for prinsipper i analyser, produktbeskrivelser og webinnhold.
- Hugo-prototypen publiseres fra `web/hugo-prototype/` via GitHub Pages artifact-deploy, ikke ved å commite bygget HTML tilbake til repoet.
- Bevar nettstedet som en lettlest dokumentasjonsside med tydelig navigasjon og lesbar tekst.
- Unngå designgrep som gjør dokumentasjon vanskeligere å lese eller navigere.
- Publiseringsflyten skal validere tekstfiler for tegnkodingsfeil før Hugo-build kjøres.

## Arbeidsflyt
- Oppdater `briefs/next-step.md` når arbeid endrer hva som er gjort eller hva som gjenstår.
- Oppdater `briefs/decisions.md` når det tas varige metode- eller arkitekturvalg.
- Bruk `briefs/decisions.md` som felles beslutningslogg på tvers av prosesser og arbeidsløp, i stedet for å opprette nye beslutningsdokumenter med mindre det finnes et tydelig særskilt behov.
- Legg nye arbeidsdokumenter og handover-notater i `briefs/arbeidsstyring-og-handover/` når de ikke hører hjemme i `results/`.
- Hvis nye generelle regler blir viktige for repoet, legg dem i denne fila heller enn å spre dem tilfeldig i enkeltfiler.


