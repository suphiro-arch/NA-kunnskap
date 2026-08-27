# Repo-regler for assistenter

Denne fila beskriver generelle regler som skal gjelde ved arbeid i dette repoet.

## Generelt
- Skriv på norsk i dokumentinnhold, forklaringer og nye markdownfiler.
- Bruk vanlig norsk tegnsett i dokumentinnhold: `æ`, `ø` og `å`.
- Bruk ASCII bare der tekniske begrensninger krever det, for eksempel i filnavn, slugger, kode eller enkelte lokale git-hooker.
- Committer fra dette repoet skal bruke en eksplisitt Git-identitet med ønsket brukernavn og en `noreply`-adresse, ikke personlig jobbmail eller privatmail som eksponeres i commit-metadata.
- Bevar etablert struktur i repoet: `arkitektur/` for faglig arkitekturgrunnlag, `config/` for regler og maler, `web/` for Hugo-prototypen, `sources/` for kildegrunnlag, `analyser/` for analyser og `briefs/` for arbeidsstyring og handover.
- Tolking av mapper:
  - `arkitektur/` brukes for strukturert arkitekturgrunnlag, som kapabiliteter, mål, prinsipper og produktnummerering.
  - `arkitektur/ressurser/` brukes for styringsregler og struktur for ressursområdet utover klassiske produktbeskrivelser.
  - `analyser/` brukes for kapabilitetsanalyser, case-analyser og andre faglige leveranser som skal kunne gjenbrukes direkte.
  - `briefs/` brukes for arbeidsstyring, handover, beslutninger og mellomdokumenter.
  - `briefs/arbeidsstyring-og-handover/` brukes for større arbeidsnotater, MVP-skisser, handover-dokumenter og lignende som ikke er sluttleveranser.
  - `print/` brukes som lokal og gitignorert plass for presentasjoner og figurer.
  - `tmp-overordnet-malbilde/` brukes som lokal og gitignorert arbeidsflate for overordnet målbildeflyt.
  - `handover/` skal ikke brukes som egen varig struktur; filer derfra skal ligge i `briefs/arbeidsstyring-og-handover/`.
- Les `README.md` i aktuell mappe når oppgaven berører den delen av repoet, slik at lokal struktur og arbeidsmåte følges.
- Ved arbeid med nye ressurskategorier eller ressurser utover klassiske produkter, bruk `arkitektur/ressurser/styringsregler.md` som styrende klassifisering.
- Ved registerføring av nye ressurser i den brede ressursstrukturen, bruk fortsatt `arkitektur/ressurser/produktnummerering.md` som operativ master for ressurs-ID og registerstatus inntil annet er besluttet.
- Når nye ressursfiler opprettes etter at løpenummer er fastsatt i `arkitektur/ressurser/produktnummerering.md`, skal filnavnet følge samme nummererte mønster som øvrige beskrivelser i porteføljen.
- Før en ny ressursfil opprettes skal assistenten først sjekke eksisterende filnavn i samme kategori og bekrefte hvilket suffix som faktisk skal brukes i denne kjøringen.
- Hvis det er tvil om suffix, skal assistenten avklare det før filopprettelse og bruke suffixet som samsvarer med utførende verktøy i denne kjøringen, ikke suffixet som tilfeldigvis finnes på forrige versjon.
- Når en ny fil er opprettet, skal register, kapabilitetsmapping og eventuelle weblenker oppdateres i samme endringssett slik at filnavn, metadata og pekerne aldri blir stående midlertidig inkonsistente.
- Ved opprettelse eller revisjon av `standarder og veiledning`, bruk `config/prompts/normerende-ressurs-canvas.system.md` sammen med `config/templates/normerende-ressurs-template.md`.
- Ved opprettelse eller revisjon av `samhandlingsarenaer og organisering`, bruk `config/prompts/samarbeidsforum-canvas.system.md` sammen med `config/templates/samarbeidsforum-template.md`.
- Ved opprettelse eller revisjon av `økonomiske og juridiske rammer og virkemidler`, bruk `config/prompts/okonomiske-og-juridiske-rammer-og-virkemidler-canvas.system.md` sammen med `config/templates/okonomiske-og-juridiske-rammer-og-virkemidler-template.md`.
- Nye ressurser innen `standarder og veiledning` skal lagres i `arkitektur/ressurser/normerende-ressurser/`, og nye ressurser innen `samhandlingsarenaer og organisering` skal lagres i `arkitektur/ressurser/samarbeidsfora/`.
- Nye ressurser innen `økonomiske og juridiske rammer og virkemidler` skal lagres i `arkitektur/ressurser/rammer-og-virkemidler/` når klassifiseringen er vurdert mot styringsreglene.

## Produktbeskrivelser
- Bruk alltid høyeste eksisterende versjonsnummer for et produkt som primært utgangspunkt, uavhengig av om siste versjon er laget av `copilot`, `chatgpt`, `claude`, eller annet verktøy.
- Eldre versjoner skal bare brukes som supplement for historikk, sammenligning eller endringsforståelse.
- Filnavn skal reflektere hvilket verktøy som har opprettet filen: `-copilot` for GitHub Copilot, `-codex` for ChatGPT-genererte filer (historisk navnekonvensjon i dette repoet), `-claude` for Claude, `-manual` for manuell opprettelse osv. Sjekk alltid eksisterende filnavn i samme kategori før du oppretter nye filer for å bekrefte konvensjonen.
- Ved tvil om suffix skal assistenten stoppe og velge suffix ut fra **utførende verktøy i den aktuelle kjøringen**, ikke ut fra suffix i forrige versjon.
- `tools/check-resource-version-sync.py` håndhever suffix-regelen mekanisk ved å validere mønsteret `^(\d+)-(.+)-v(\d+)-(forfatter)\.md$` mot register og mapping.
- Før handover eller commit er det obligatorisk å verifisere at nytt filnavn, `produktnummerering.md` og `produkt-kapabilitet-koblinger.yaml` peker til samme versjon og samme suffix.
- Hvis suffix er feil, skal assistenten rette filnavn og alle pekere i samme endringssett. Det er ikke tillatt å avslutte kjøringen med inkonsistent suffix mellom fil og register/mapping.
- Følg metoden i [config/prompts/operative-ressurs-canvas.system.md](config/prompts/operative-ressurs-canvas.system.md) ved arbeid med gjenbrukbare løsninger.
- Ved opprettelse av nye beskrivelser av gjenbrukbare løsninger skal [config/prompts/operative-ressurs-canvas.system.md](config/prompts/operative-ressurs-canvas.system.md) alltid brukes som styrende instruks.
- Nye produktfiler skal følge gjeldende versjoneringsregel i promptfila.
- Når ny versjon av en ressurs opprettes, skal både `arkitektur/ressurser/produktnummerering.md` og `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` oppdateres hvis de peker til ressursen.
- Register og kapabilitetsmapping skal peke til siste versjon eksplisitt; ikke stol på at generatorer eller webskript retter dette automatisk.
- Nye eller oppdaterte produktbeskrivelser skal lagres som ren `UTF-8`.
- Etter opprettelse eller endring av produktbeskrivelser skal det gjøres en eksplisitt kontroll for tegnkodingsfeil, ikke bare en visuell sjekk i terminalen.
- Hvis tekst viser typiske tegnkodingsfeil med doble bokstavsekvenser eller ødelagte typografitegn, skal fila rettes før commit og før genererte oversikter oppdateres.
- Lokale hooks for encoding-kontroll skal være aktive (`tools/setup-git-hooks.ps1`) slik at både commit og push stoppes automatisk ved mojibake.
- I beskrivelser av standarder og veiledning skal `Status/Livsfase` beskrive status på selve ressursen, ikke status på dokumentutkastet eller ressursbeskrivelsen.
- Tidlige versjoner av beskrivelser for standarder og veiledning skal som hovedregel beholde hele malstrukturen, og uferdige felt skal merkes eksplisitt i teksten i stedet for å utelates.
- `v1` for standarder og veiledning, samhandlingsarenaer og organisering, og økonomiske eller juridiske rammer og virkemidler skal bare brukes når dokumentet er godt nok til å fungere som direkte analysegrunnlag, ikke bare som arbeidsutkast.
- `v1` for disse ikke-operative kategoriene krever at analysekritiske felt er substansielt utfylt, at påstander med høy betydning er kildeforankret, og at tydelig usikkerhet er markert der åpne kilder ikke er nok.
- I beskrivelser av samhandlingsarenaer og organisering skal det være eksplisitt om arenaen er rådgivende, koordinerende eller besluttende, hvilke ressurser den påvirker, og når den bør involveres i analyse- eller utviklingsløp.
- I seksjonen `Støtter arkitekturprinsipper` skal beskrivelser også vurdere tydelige svakheter, spenninger eller begrensninger mot viktige prinsipper når dette er relevant for mulig bruk.
- Kapabilitetsseksjoner i ressursbeskrivelser skal bruke rene, kanoniske kapabilitetsnavn. Utfyllende forklaring skal ligge i brødtekst, ikke bygges inn i selve navnelabelen.

## Kilder og analyse
- Bruk `sources/links.md` som førstevalg for eksterne kilder.
- Gå bredere enn lenkene i `sources/links.md` bare når de er utilstrekkelige, utdaterte eller utilgjengelige.
- Hvis arbeidet bruker bredere søk enn `sources/links.md`, skal de ekstra kildene nevnes eksplisitt i dokumentasjonen eller leveransen.
- Hvis arbeidet bruker nye stabile eksterne URL-er som er relevante for videre ressursarbeid, skal `sources/links.md` oppdateres i samme kjøring så lenge lenkene ikke bare er engangskilder uten gjenbruksverdi.
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
- Når `arkitektur/ressurser/produktnummerering.md` eller `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` oppdateres til å peke på en ny eller høyere ressursversjon, skal den aktuelle ressursfila være opprettet og sporet av Git i samme endringssett.
- Det skal ikke innføres pekere fra register eller kapabilitetsmapping til ressursfiler som fortsatt er `untracked`.
- Hvis nye generelle regler blir viktige for repoet, legg dem i denne fila heller enn å spre dem tilfeldig i enkeltfiler.
- `briefs/next-step.md` skal holdes i `.gitignore`, men brukes likevel som sporet arbeidsnotat i repoet fordi fila allerede er etablert som lokal statusflate og ikke skal publiseres.

## Automatiske kjøringer
- Automatiske kjøringer som oppretter eller endrer markdownfiler skal eksplisitt kjøre encoding-kontroll før de avsluttes, ikke bare stole på visuell sjekk eller at hooks eventuelt fanger feil senere.
- Hvis en automatisk kjøring endrer ressursbeskrivelser, `briefs/`, webgrunnlag eller andre tekstfiler som kan mates videre inn i ressursoversikten eller publiseringsflyten, skal mojibake rettes i samme kjøring før handover gis.
- Hvis en automatisk kjøring oppretter nye ressursfiler eller andre filer som register, mapping eller publiseringsgrunnlag peker til, skal filene legges til i Git i samme kjøring før handover gis.
- Hvis en automatisk kjøring bruker nye eksterne lenker som ikke allerede finnes i `sources/links.md`, skal kjøringen vurdere dem for opptak og normalt oppdatere `sources/links.md` i samme runde når lenkene er stabile, offisielle og relevante for senere ressursarbeid.
- Hvis kjøringsmiljøet ikke har direkte skrivetilgang til `.git`, skal automatiske kjøringer bruke minst mulig eskalering: gjør alt vanlig innholdsarbeid, alle valideringer og eventuell webgenerering uten eskalering først, og eskaler bare de nødvendige Git-stegene `git add`, `git commit` og `git push` helt til slutt når resultatet allerede er verifisert.
