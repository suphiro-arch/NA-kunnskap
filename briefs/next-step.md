---
date: 2026-05-15
author: codex
status: aktiv
topic: neste-steg
---

# Neste steg

## Siste oppdateringer

### Tillegg 2026-08-28 (justering av filterrad og kontaktknapper)

- Emnefilteret er fjernet igjen etter vurdering av nytteverdien. 122 ressurser fordelte seg på 111 emneverdier, og over 90 av dem traff nøyaktig én ressurs. Filteret avgrenset i praksis ingenting.
- Emneverdien er beholdt som `data-emne` på hvert kort og som del av fritekstsøket, slik at søk på emneord fortsatt treffer. Filterboksen kan settes inn igjen uten nytt arbeid hvis emnevokabularet senere konsolideres til et titalls grupper.
- Søk, Eier, Type og Kapabilitet ligger nå på én rad, med søkefeltet bredest. Under 60rem brytes raden fortsatt, siden fire felt ikke får plass på smale skjermer.
- Kontakt- og kildelenkene er gjort om fra understrekede tekstlenker til knapper med gjennomsiktig bakgrunn og tynn farget ramme, etter tilbakemelding om at knappene fungerte bedre.
- Knappeteksten er endret fra «Kontakt oss» til «Send mail til oss», slik at det går fram at lenken åpner e-post og ikke et skjema eller en annen løsning.
- Knappene ligger nå øverst til høyre i overskriftsboksen på alle sider, forsiden inkludert. Tidligere lå de under ingressen på forsiden.

### Tillegg 2026-08-28 (byggefeil i mal-JS, ny syntakskontroll)

- Hugo-byggingen feilet på alle sider etter commit `d0b5670`. Escape-sekvensene i e-postteksten i [baseof.html](../web/hugo-prototype/layouts/_default/baseof.html) ble til faktiske linjeskift da fila ble skrevet, slik at strengliteralen var uterminert. Skriptet ligger i den delte malen, derfor slo én feil ut på hver eneste side.
- Rettet i `0ac3f52` ved å skrive teksten ferdig prosentkodet i stedet. Malfila trenger da ingen escape-sekvenser i det hele tatt, og feilklassen kan ikke oppstå på nytt samme sted.
- Opprettet [check-inline-js.py](../tools/check-inline-js.py). Kontrollen henter ut hver `<script>`-blokk i `layouts/` og `content/` og lar `node --check` parse den. Ingenting kjøres, bare syntaksen valideres.
- Verifisert mot den faktiske byggefeilen: kontrollen kjørt mot `baseof.html` fra `d0b5670` gir `SyntaxError: Invalid or unexpected token` og feilkode 1. Gjeldende versjon er grønn med 10 blokker kontrollert.
- Blokker med Hugo-syntaks kan ikke parses som ren JavaScript og hoppes over. Antallet rapporteres eksplisitt, slik at det ikke ser ut som full dekning når noe er utelatt. I dag hoppes ingen blokker over.
- Koblet inn i begge git-hooks og begge CI-arbeidsflyter, rett før byggesteget.
- Lærdom notert i [AGENTS.md](../AGENTS.md): unngå escape-sekvenser i innebygd JavaScript når teksten kan skrives ferdig prosentkodet. De overlever dårlig gjennom verktøy som skriver malfilene.
- Verdt å merke: alle åtte kontrollene før byggesteget var grønne da feilen ble pusht. Tegnkoding, versjonssynk, strukturkontroll, kildelenker og frontmatter ser ingen av dem på om JavaScript i malene er gyldig.

### Tillegg 2026-08-28 (plassering av kontaktlenker, emnefilter, søkefelt)

- Kontakt- og kildelenkene er flyttet ut av toppheaderen og inn dit de hører hjemme faglig: på forsiden rett under setningen om at vi ønsker tilbakemeldinger, og øverst til høyre i overskriftsboksen på seksjons- og detaljsider. Ny partial [feedback-links.html](../web/hugo-prototype/layouts/partials/feedback-links.html) brukes begge steder, slik at markupen finnes ett sted.
- Fjernet CTA-boksene som var lagt inn i forsideinnholdet og i den genererte ressursoversikten. Ressursoversikten er generert, så en håndredigert boks der ville uansett blitt overskrevet ved neste generering.
- Emnefilteret manglet fordi det aldri har vært generert. `Emne` leses fra registeret inn i feltet `Category` i [generate-products.ps1](../web/hugo-prototype/scripts/generate-products.ps1), men ble ikke skrevet ut som dataattributt eller filterboks. Commit `befadcd` med meldingen «Forbedre emnefilter i ressursoversikt» endret emneverdier i registeret og regenererte oversikten, men la aldri inn et filter.
- Lagt inn `Emne` som siste filterboks, med `data-emne` på hvert ressurskort og emneverdien med i fritekstsøket.
- Verdt å merke: 122 ressurser fordeler seg på 111 ulike emneverdier. Over 90 av dem treffer nøyaktig én ressurs. Filteret fungerer derfor som oppslag, ikke som avgrensning. En konsolidering av emnevokabularet til et titalls grupper vil gi vesentlig mer nytte enn filteret gir i dag.
- Søkefeltet er gitt egen farge, ramme og fokusmarkering slik at det skiller seg fra de fire nedtrekkslistene.
- Ikke gjort: ingen visuell verifisering. `hugo` er ikke installert i dette miljøet.

### Tillegg 2026-08-28 (strukturkontroll av ressursbeskrivelser, opprydding i død webkode)

- Opprettet [check-resource-structure.py](../tools/check-resource-structure.py). Kontrollen sammenligner seksjonene i hver ressursfil med malen for kategorien og lukker hullet som lot en halv ressursfil bli committet, publisert og generert videre uten at noen kontroll reagerte.
- Kontrollen skiller mellom feil og advarsel. Feil er manglende h1-tittel, manglende kjernefelt eller tom seksjon, og gir feilkode med `--strict`. Advarsel er malseksjoner som mangler og overskrifter utenfor malen, og stopper ikke arbeidet.
- Kjernefeltene er utledet mekanisk, ikke skjønnsmessig: for hver kategori er de snittet av overskriftene i samtlige eksisterende ressursfiler. Det gjør at kontrollen er grønn på dagens portefølje samtidig som den slår ut umiddelbart når en fil faller under nivået alt annet ligger på. Settet kan strammes inn når eldre `v0`-filer fylles ut.
- Verifisert mot den faktiske skaden: den ødelagte versjonen av [144-eForvaltningsforskriften-v1-claude.md](../arkitektur/ressurser/rammer-og-virkemidler/144-eForvaltningsforskriften-v1-claude.md) fra commit `befadcd` gir feilkode 1 med alle åtte tapte seksjoner listet. Gjeldende versjon er grønn.
- Status på dagens portefølje: 191 ressursfiler grønne på kjernestruktur, 72 advarsler i 60 filer. Advarslene er reell gjeld, hovedsakelig `v0`-filer uten `Navn`, `Forpliktelsesnivå og etterlevelse`, `Typiske analyse- og beslutningssituasjoner` og `Konsekvens ved manglende bruk eller avvik`, samt noen få filer med overskrifter som avviker fra malen.
- Koblet kontrollen inn i begge git-hookene ([pre-commit](../.githooks/pre-commit) med `--new-only`, [pre-push](../.githooks/pre-push) full), begge CI-arbeidsflytene ([encoding-guard.yml](../.github/workflows/encoding-guard.yml), [publish-hugo-prototype.yml](../.github/workflows/publish-hugo-prototype.yml)) og dokumentasjonen i [AGENTS.md](../AGENTS.md), [CLAUDE.md](../CLAUDE.md) og [README.md](../README.md).
- Lagt inn to nye regler i [AGENTS.md](../AGENTS.md): malstrukturen skal beholdes i sin helhet også i tidlige versjoner, og tapt innhold skal hentes tilbake med `git show <commit>:<sti>` framfor å skrives på nytt fra hukommelsen.
- Fjernet død kode etter at tilbakemeldingsboksen ble erstattet av verktøylenker i headeren: `layouts/partials/feedback-cta.html`, `layouts/shortcodes/feedback-cta.html` og reglene `.content-card--feedback`, `.feedback-cta*` og `.home-feedback*` i [main.css](../web/hugo-prototype/assets/css/main.css). Parameteren `feedbackEmail` i `hugo.toml` er beholdt fordi headeren fortsatt bruker den.
- Mappa `layouts/shortcodes/` er nå tom og fjernet. Ingen innholdsfiler kalte shortcodes.
- Ikke gjort: den nye headeren er fortsatt ikke visuelt verifisert, fordi `hugo` ikke er installert i dette miljøet.

### Tillegg 2026-08-28 (kontakt- og kildelenker i header, gjenoppretting av skadet ressursfil)

- Flyttet tilbakemeldings- og kildelenkene til headeren som verktøylenker: `Kontakt oss` og `Se kildekoden på GitHub` ligger nå under hovedmenyen, synlig på alle sider. Begrunnelse for plassering: hovedmenyen skal være ren innholdsnavigasjon mellom seksjoner, og venstremenyen er kontekstuell navigasjon nedover i innholdstreet. Verktøylenker hører hjemme i headeren, der de er synlige uten å konkurrere med navigasjonen.
- Fjernet de tre tidligere plasseringene: knappen i helten på forsiden med tilhørende skript i `list.html`, shortcoden `{{< feedback-cta >}}` i `content/_index.md`, og det ubetingede partial-kallet i `baseof.html`. Sistnevnte ga tilbakemeldingskortet på alle sider, i tillegg til shortcoden på forsiden.
- E-postadressen settes fortsatt sammen i nettleseren framfor å ligge som `mailto:` i kildekoden, men leses nå fra `feedbackEmail` i `hugo.toml` i stedet for å være hardkodet i malen.
- La inn lenke til repoet i brødteksten under `Hvordan ressursoversikten bygges`, og tok med kontrollskriptene i verktøylista der.
- `feedback-cta.html` i `layouts/partials/` og `layouts/shortcodes/`, samt CSS-reglene `.feedback-cta*` og `.home-feedback*`, er nå ubrukt. Ikke fjernet.

Gjenoppretting etter utilsiktet sletting:
- [144-eForvaltningsforskriften-v1-claude.md](../arkitektur/ressurser/rammer-og-virkemidler/144-eForvaltningsforskriften-v1-claude.md) mistet åtte seksjoner i arbeidskopien, blant annet `Navn`, `Ressurs ID`, `Status/Livsfase` og `Kort beskrivelse`, erstattet av tegnene `ne`. Den skadede versjonen rakk å bli committet og pushet i `befadcd`. Fila er gjenopprettet fra `ba13e93` og kontrollert mot malen: alle 26 seksjoner er tilbake.
- Følgeskade i webgrunnlaget: ressurskortet for `DIGDIR-066` fikk tittelen `eForvaltningsforskriften` og teksten `Kort beskrivelse er ikke oppgitt`, fordi generatoren ble kjørt mens fila var ødelagt. Rettet ved å kjøre `generate-products.ps1` på nytt etter gjenopprettingen.
- Ingen av kontrollskriptene fanget dette. Encoding-, versjons- og lenkekontrollene ser ikke at en ressursfil mangler obligatoriske seksjoner. En strukturkontroll mot malene ville fanget det, og bør vurderes.

### Tillegg 2026-08-28 (restpunkter fra batch 1 og 2 lukket)

- Opprettet `DTIL-001` Regulatorisk sandkasse for kunstig intelligens som løpenr 147 i [147-Regulatorisk-sandkasse-for-kunstig-intelligens-v1-claude.md](../arkitektur/ressurser/normerende-ressurser/147-Regulatorisk-sandkasse-for-kunstig-intelligens-v1-claude.md), etter at eierkoden `DTIL` var på plass. Klassifisert som `standarder og veiledning` framfor samhandlingsarena: sandkassen er en veiledningstjeneste som publiserer sluttrapporter, ikke en arena for koordinering mellom aktører. Nye søk mot Datatilsynets egne sider ga tilstrekkelig grunnlag for `v1`, i motsetning til første forsøk der treffene i hovedsak gjaldt den danske sandkassen.
- Registerført `DIGDIR-019` Altinn Portal som løpenr 21 og `KS-010` Fiks kjøretøyregister som løpenr 69. Begge hadde ressursfil, men manglet rad i registeret, og registeret hoppet fra 20 til 22 og fra 68 til 74. Altinn Portal manglet også oppføring i kapabilitetsmappingen, og er lagt inn der med de fem kapabilitetene fra canvaset.
- Flyttet `FLERE-003` Stimulab fra Digdir-seksjonen til `## Flere virksomheter (FLERE)` der den hører hjemme.
- Konsoliderte de ti dupliserte lenkene i `sources/links.md` til én oppføring per URL med dekkende etikett. De fleste var samme URL registrert flere ganger fordi ulike ressurser siterte den. Fila har nå null duplikater.
- Bekreftet at ressursoversikten på web allerede inneholder `DIGDIR-065` til `DIGDIR-067` og `FLERE-004`. Generatoren er kjørt av et annet arbeidsløp etter at ressursene kom inn, så webpunktet fra forrige runde er dekket. `DTIL-001` må med i neste regenerering.

Restpunkt fra denne runden:
- **Registerendringene er gjort i arbeidskopien, men ikke committet.** `produktnummerering.md` inneholdt samtidig en pågående `Emne`-omskriving fra et annet arbeidsløp, og fila ble derfor holdt utenfor denne commiten for ikke å committe andres uferdige arbeid. Det betyr at `DTIL-001`, `DIGDIR-019`, `KS-010`, eierkoden `DTIL`, regelen for nye eierkoder og flyttingen av `FLERE-003` ligger usporet inntil registerfila committes. Kapabilitetsmappingen og ressursfilene peker allerede til dem.
- `check-resource-version-sync.py` går grønt også uten disse registerradene. Kontrollen sammenligner register mot mapping og web, men fanger ikke mapping-oppføringer som mangler rad i registeret. Dette er samme blindsone som gjorde at løpenr 21 og 69 kunne mangle uoppdaget, og bør utvides.
- `sources/links.md` bør regenereres eller kontrolleres på nytt etter at `Emne`-omskrivingen i registeret er ferdig, siden etikettene på de 99 tilførte lenkene er hentet fra registerets navnekolonne.

### Tillegg 2026-08-28 (batch 2: rammer og kunnskapsgrunnlag)

Tre nye ressurser opprettet, én kandidat stoppet:

- `DIGDIR-066` eForvaltningsforskriften som løpenr 144 i [144-eForvaltningsforskriften-v1-claude.md](../arkitektur/ressurser/rammer-og-virkemidler/144-eForvaltningsforskriften-v1-claude.md). FOR-2004-06-25-988, i kraft siden 2004, forvaltet av Digitaliserings- og forvaltningsdepartementet. Kapittel 7 er det rettslige grunnlaget for Kontakt- og reservasjonsregisteret (`DIGDIR-005`).
- `DIGDIR-067` Tilskudd til etablering av kommunale opplæringstilbud i digital kompetanse til innbyggerne som løpenr 145 i [145-Tilskudd-til-kommunale-opplaeringstilbud-i-digital-kompetanse-v1-claude.md](../arkitektur/ressurser/rammer-og-virkemidler/145-Tilskudd-til-kommunale-opplaeringstilbud-i-digital-kompetanse-v1-claude.md). Dette avklarer den åpne vurderingen om `Tilskudd til digital inkludering`: det er én navngitt ordning forvaltet av Digdir, ikke flere beslektede virkemidler.
- `FLERE-004` Nasjonal indeks for digital inkludering som løpenr 146 i [146-Nasjonal-indeks-for-digital-inkludering-v1-claude.md](../arkitektur/ressurser/normerende-ressurser/146-Nasjonal-indeks-for-digital-inkludering-v1-claude.md). Klassifisert som `standarder og veiledning` etter samme logikk som `DIGDIR-039` Kunnskapsgrunnlag og KPI-er for datadeling. Eierkode `FLERE` fordi indeksen forvaltes i samarbeid mellom Uu-tilsynet og Nkom.
- `Regulatorisk sandkasse for KI` ble ikke opprettet. To hindre: ordningen eies av Datatilsynet, som ikke har eierkode i registeret, og åpne kilder ga for tynt grunnlag på flere `v1`-kritiske felt. Krever avklaring av ny eierkode før den kan tas inn.

- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md), [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) og [sources/links.md](../sources/links.md) med fem nye stabile lenker i samme endringssett.
- Malfølging kontrollert maskinelt for alle tre filene mot henholdsvis `okonomiske-og-juridiske-rammer-og-virkemidler-template.md` og `normerende-ressurs-template.md`. Alle overskrifter og rekkefølge stemmer.
- `sync-resource-metadata.py` foreslo ingen endringer, altså samsvarer kapabilitetsforklaringene i canvasene med mappingen.
- Bekreftet grønn `check-resource-version-sync.py`, `check-mojibake.ps1` og `validate-text-encoding.py`.

Lenkegjeld ryddet og kontroll etablert:
- Kontrollerte alle eksterne lenker i de 194 ressursfilene mot `sources/links.md` og fant 160 unike URL-er som ikke var registrert. Dette var eldre gjeld fra tidligere kjøringer, ikke fra denne batchen.
- Delte gjelden i to: 99 stabile offisielle sider og landingssider, og 61 tekniske dyplenker til API-dokumentasjon og kodebaser. De 99 er lagt inn i `sources/links.md`, og de 61 er bevisst holdt utenfor siden `AGENTS.md` sier at engangskilder uten gjenbruksverdi ikke skal registreres.
- Lenkene er fordelt på filas etablerte seksjonsstruktur i stedet for å samles i én ny liste: eierseksjonene under `Fellesløsninger` for ressurskilder, `Juridisk og rettslig infrastruktur` for alle Lovdata-kilder, og ny seksjon `Digital inkludering` under `Standarder og veiledninger` for inkluderingssporet.
- Kontrollert at ingen av tilleggene ble duplikater. Fila har ti URL-er som forekommer flere ganger fra før, alle fra tidligere kjøringer. Ikke ryddet i denne runden.
- Opprettet [check-source-links.py](../tools/check-source-links.py) som kontrollerer at eksterne lenker i ressursbeskrivelser er registrert. Skriptet har `--new-only` for å begrense til endrede filer og `--strict` for feilkode, og unntar de samme tekniske dokumentasjonsdomenene som ryddingen. Kontrollen er nå grønn på alle 1361 lenkeforekomster.
- Presisert i `AGENTS.md` hvor skillet går mellom lenker som skal registreres og lenker som bare hører hjemme i ressursfilas eget kildegrunnlag, og lagt inn henvisning til den nye kontrollen.

Statuskontroll av hjemmelsgrunnlaget for `DIGDIR-066`:
- Forvaltningsloven av 10. februar 1967, som eForvaltningsforskriften er hjemlet i gjennom § 15a, blir opphevet av lov 20. juni 2025 nr. 81 om saksbehandlingen i offentlig forvaltning. Ikrafttredelsen fastsettes av Kongen og er ikke bestemt. Loven av 1967 ble sist endret ved LOV-2025-04-25-12 med virkning fra 1. januar 2026.
- Oppdatert ressursbeskrivelsen med dette i `Status/Livsfase`, `Forvaltningsmodell` og som egen rad i risikotabellen. Forskriften er fortsatt i kraft, så `v1` og statusen `aktiv` står, men hjemmelsgrunnlaget må kontrolleres på nytt når ny forvaltningslov settes i kraft.

Eierkoder:
- Registeret hadde ingen regel for hvordan nye eierkoder lages, bare en liste over de 17 eksisterende. La inn seksjonen `Slik lages en ny eierkode` i [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md), utledet av mønsteret i kodene som allerede er i bruk: etablert forkortelse når den finnes, ellers tre til seks store bokstaver fra kjerneordet i navnet, `FLERE` ved delt forvaltning, og ingen endring av koden etter at den er tatt i bruk.
- Opprettet `DTIL` for Datatilsynet, som manglet og blokkerte `Regulatorisk sandkasse for KI`.
- Lagt inn regel i `AGENTS.md` om at manglende eierkode skal opprettes i samme endringssett som ressursen, og ikke er grunn til å utsette ressursen eller plassere den på feil eier.

Nytt funn under lenkeryddingen:
- Løpenr 21 `Altinn Portal` og løpenr 69 `Fiks Kjøretøyregister` har ressursfiler, men ingen rad i [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md). `check-resource-version-sync.py` fanger ikke dette, fordi den validerer at pekere fra registeret stemmer, ikke at alle ressursfiler er registerført. Bør følges opp: enten registerføres, eller avklares om filene er utdaterte.

### Tillegg 2026-08-27 (PPP(P)-nettverket opprettet, batch 1)

- Opprettet `DIGDIR-065` PPP(P)-nettverket som løpenr 143 i [143-PPP-P-nettverket-v1-claude.md](../arkitektur/ressurser/samarbeidsfora/143-PPP-P-nettverket-v1-claude.md). Første ressursfil i repoet med suffix `-claude`.
- Avklart det åpne eierskapsspørsmålet: eierkode `DIGDIR`, fordi sekretariat, påmelding og publiseringsflate forvaltes i Digdir-regi. Den brukerdrevne arbeidsformen og de eksternt ledede delnettverkene er et trekk ved arbeidsformen, ikke et delt forvaltningsansvar som ville tilsagt `FLERE`.
- Kontrollert mot eksisterende samarbeidsfora: nettverket er ikke dekket av Skate, Digitaliseringsrådet, Arkitektur- og standardiseringsrådet eller Styringsrådet for fellesløsningene. Grensesnittet mot de fire er beskrevet eksplisitt i canvaset.
- Kapabiliteter satt til `Samarbeidsarenaer og nettverk` og `Samordning`. `Tjenesteforvaltning` og `Arkitekturstyring` ble vurdert og valgt bort som for svake koblinger.
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md), [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) og [sources/links.md](../sources/links.md) med tre nye stabile Digdir-lenker i samme endringssett.
- Bekreftet grønn `check-resource-version-sync.py`, grønn `check-mojibake.ps1` og grønn `validate-text-encoding.py`.
- Gjenstår i denne runden: regenerere ressursoversikten i `web/hugo-prototype/content/ressursoversikt/` slik at den nye ressursen vises. Regenerering ble utsatt fordi arbeidskopien samtidig har uferdige endringer i `generate-products.ps1` og genererte ressurssider fra et annet arbeidsløp (fjerning av `Emne` fra ressurskort og filtre).

- Revidert beskrivelsen etter tilbakemelding: fjernet vurderinger fra arbeidsprosessen (hvilke kapabiliteter som ble valgt bort, begrunnelse for eierkode), fjernet innhold som var utledet fra hva som er vanlig for denne typen nettverk, og kuttet deduksjoner. Felt der åpne kilder ikke strekker til, sier nå kort at kildene ikke beskriver forholdet.
- Skjerpet [AGENTS.md](../AGENTS.md) med nye regler for ressursbeskrivelser som følge av dette: beskrivelsen skal handle om ressursen og ikke om arbeidsprosessen bak den, faglig begrunnelse for koblingene som faktisk er valgt skal likevel stå i ressursfila fordi kapabilitetsforklaringene hentes videre til mappingen, klassifiseringsbeslutninger som eierkodevalg logges her i `next-step.md` i stedet, felt skal ikke fylles med det som er sannsynlig for ressurstypen, deduksjon skal brukes sparsomt, kort er bedre enn utfylt med usikkert innhold, og avsluttende brødtekst i `Kapabiliteter` skal stå før kulelista fordi `sync-resource-metadata.py` ellers trekker den inn i siste kapabilitetsforklaring.
- Malfølging kontrollert: overskriftene i ressursfila er diffet mot `config/templates/samarbeidsforum-template.md` og stemmer på alle 26 seksjoner, i samme rekkefølge og med malens egen ordlyd.

- Rettet to feil i [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md): Digdir-tabellen manglet kolonneoverskriften `Emne`, slik at alle 65 rader hadde ett felt mer enn overskriften og siste kolonne falt bort ved markdown-visning. Fjernet også beskrivelsen av en `Merknad`-kolonne som ikke fantes i noen av de 17 tabellene. Alle 135 registerrader har nå riktig feltantall.
- Besluttet å ikke innføre egen kolonne for klassifiseringsbeslutninger. Klassifiseringen er selvforklarende fra `Type` og ressurskategori for de aller fleste ressursene, og en kolonne som står tom på nesten alle rader gir vedlikeholdsgjeld uten gevinst. Batchloggen her i `next-step.md` beholdes som sporet for de tilfellene der valget faktisk var tvilsomt.

Ett funn som bør følges opp separat:
- `FLERE-003` Stimulab står i Digdir-seksjonen i `produktnummerering.md` i stedet for under `## Flere virksomheter (FLERE)`. Kontrollskriptene fanger ikke seksjonsplassering, bare versjons- og stikonsistens.

### Tillegg 2026-08-27 (opprydding i repo-regler og struktur)

- Oppdatert [AGENTS.md](../AGENTS.md) og de sentrale README-filene slik at de beskriver dagens struktur uten `results/` som aktiv leveransemappe.
- Presisert at leveranser nå rutes etter type til `analyser/`, `arkitektur/ressurser/`, `briefs/`, `sources/`, `web/` og `print/`, og at `handover/` er en reststruktur som ikke skal brukes for nye filer.
- Flyttet eksisterende handover-notat til `briefs/arbeidsstyring-og-handover/` og logget at `results/` er avviklet som aktiv struktur.
- Latt `briefs/next-step.md` bli stående i `.gitignore`, men gjort det eksplisitt at fila brukes som sporet lokal arbeidsflate likevel.
- Fullført kontroll av eldre stier: `results/` og `produkter/produktbeskrivelser/` finnes ikke lenger som aktive stier i regler eller README-filer, bare som historikk i [decisions.md](./decisions.md). Siste aktive referanse ble rettet i `AGENTS.md`, slik at arbeidsdokumenter nå avgrenses mot `analyser/` og `arkitektur/`.
- Bekreftet grønn `check-mojibake.ps1` og grønn `check-resource-version-sync.py` etter oppryddingen. Restpunktet fra denne runden er dermed lukket.
- Opprettet [CLAUDE.md](../CLAUDE.md) som peker til `AGENTS.md` som autoritativ regelfil og legger til det som er Claude-spesifikt: suffix `-claude`, PowerShell-kommandoer for encoding- og registerkontroll, og kjente fallgruver i repoet.

### Tillegg 2026-08-19 (virkemiddel- og internasjonalt spor)

- Gjennomgang av dagens `Neste steg` opp mot det nye oppdraget viser at planen allerede har et delspor for flytting til `økonomiske og juridiske rammer og virkemidler`, men at den ikke ennå dekker hele gap-analysen for nasjonale virkemidler, samhandlingsarenaer og internasjonale ressurser.
- Instruksen peker nå på en kuratert ressursoversikt som skal favne forvaltede, felles, planlagte og internasjonale ressurser med tydelig betydning for nasjonal arkitektur. Det betyr at `FELLES` må vurderes eksplisitt der styringen er delt, og at ressursunder etablering kan registreres når status og plan er dokumentert.
- Første vurdering av oppdraget tilsier at `PPP(P)` bør behandles som høyprioritert kandidat i samhandlingssporet, og at de økonomiske kandidatene `Medfinansieringsordningen`, `Stimulab` og ordningen for digital inkludering/digital kompetanse bør håndteres som første batch for nasjonal virkemiddelgjennomgang.
- Det nye internasjonale vurderingssporet må være separat og eksplisitt, med fokus på ressurser og arenaer der Norge eller Digdir deltar og som faktisk påvirker arkitektur, styring, finansiering, standardisering eller implementering.
- Kapabilitetsgjennomgangen skal kjøres på nytt mot hele `produkt-kapabilitet-koblinger.yaml` etter sommerens oppdaterte rammeverksbeskrivelser og det nye ressursgrunnlaget, slik at vi kan verifisere både manglende dekning og koblinger som nå bør justeres.

Første batch skal derfor avklare fire konkrete kandidater først:
1. `Medfinansieringsordningen`: kontrollere kanonisk navn, status, forvaltning og om ressursen skal opprettes som `DIGDIR` eller `FELLES`.
2. `Stimulab`: kontrollere om dagens ressursdekning allerede er tilstrekkelig gjennom innovasjonsrammeverket, eller om ordningen trenger egen ressurs med tydelig virkemiddelprofil.
3. Tilskuddsordning for digital inkludering / digital kompetanse: avklare om det er én ressurs eller flere nært beslektede virkemidler, og om status bør være aktiv, under etablering eller avgrenset som del av en annen ressurs.
4. `PPP(P)`-nettverket: kontrollere om nettverket allerede er dekket av eksisterende samarbeidsfora, og ellers beskrive det som en egen samhandlingsressurs med hovednettverk og eventuelle undernettverk som del av samme ressurs.

Foreløpig status etter første kildesjekk:
- `Stimulab` er allerede tydelig beskrevet på Digdir-siden som en aktiv stimuleringsordning for innovasjon og tjenestedesign, og den er også faglig dekket indirekte i `Rammeverk for innovasjon i offentlig sektor`. Den ser derfor ut som en kandidat for `DEL_AV_EKSISTERENDE_RESSURS` eller eventuelt en egen oppføring bare hvis vi trenger et tydelig virkemiddelspor.
- `Medfinansieringsordningen` er fortsatt ikke fanget opp i dagens ressursoversikt, og må behandles som en åpen kandidat med høy prioritet.
- `PPP(P)`-nettverket er eksplisitt navngitt i virkemiddeloversikten, men finnes ikke som egen ressurs i registeret; dette peker mot egen samhandlingsressurs dersom status og varighet kan dokumenteres.
- Tilskuddsordningen for digital inkludering / digital kompetanse er foreløpig bare identifisert i rålista og må avklares nærmere før vi bestemmer om det er én eller flere kandidater.
- Opprettet første nye ressurs i batch 1: `Stimulab` som `FLERE-003` i [141-Stimulab-v1-copilot.md](../arkitektur/ressurser/rammer-og-virkemidler/141-Stimulab-v1-copilot.md), og oppdaterte [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) og [sources/links.md](../sources/links.md).
- Opprettet også `Medfinansieringsordningen` som `DIGDIR-064` i [142-Medfinansieringsordningen-v1-copilot.md](../arkitektur/ressurser/rammer-og-virkemidler/142-Medfinansieringsordningen-v1-copilot.md), og synket register og kapabilitetsmapping for den nye virkemiddelressursen.

Arbeidsrekkefølge for batch 1:
1. Kontrollere åpne kilder og avklare dagens status for hver kandidat.
2. Avgøre om kandidatene er `NY_KANDIDAT_HOY`, `NY_KANDIDAT_MIDDELS`, `DEL_AV_EKSISTERENDE_RESSURS` eller `GENERISK_VIRKEMIDDELTYPE`.
3. Hvis kandidaten holder: opprette eller oppdatere canvas i riktig kategori, med korrekt eiermodell og status.
4. Oppdatere `produktnummerering.md`, `produkt-kapabilitet-koblinger.yaml`, relevante kilder og webgrunnlag før neste batch vurderes.

Plan for videre arbeid:
1. Oppdatere ressursgrunnlaget mot oppdraget ved å bruke Digdirs virkemiddeloversikt, [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md), eksisterende ressursfiler, styringsregler og oppdaterte kilder som felles kontrollgrunnlag. Råfila i [sources/2026-04-10-digdir-virkemiddeloversikt-raw.md](../sources/2026-04-10-digdir-virkemiddeloversikt-raw.md) skal behandles som den vedtatte og faglig forankrede grunnlista for virkemidler, og brukes som hovedutgangspunkt når vi lager listen over nye ressurser.
2. Gjennomføre en første kuratert gap-analyse og klassifisere kandidater med en av kodene `ALLEREDE_REGISTRERT`, `NY_KANDIDAT_HOY`, `NY_KANDIDAT_MIDDELS`, `UNDER_ETABLERING_KANDIDAT`, `DEL_AV_EKSISTERENDE_RESSURS`, `GENERISK_VIRKEMIDDELTYPE`, `IKKE_TILSTREKKELIG_RELEVANT` eller `MÅ_AVKLARES`.
3. Kjør batch 1 med åpenbare nasjonale gap: `Medfinansieringsordningen`, `Stimulab`, tilskuddsordning for digital inkludering/digital kompetanse og `PPP(P)`-nettverket, samtidig som kapabilitetskoblingene revalideres mot oppdatert modell.
4. Kjør batch 2 med rammer og ressurser under etablering: `eForvaltningsforskriften`, kunnskapsgrunnlag om digitaliseringstiltak, nasjonal portefølje, regulatorisk sandkasse for KI og nasjonal indeks for digital inkludering.
5. Kjør batch 3 med internasjonal arkitekturpåvirkning: `Digital Europe Programme`, `NOBID`, `European Digital Identity Cooperation Group`, `OECD OPSI` og konkrete nordisk-baltiske samarbeidsmekanismer, samt et eget vurderingsspor for `eIDAS 2.0`, `Single Digital Gateway`, `OOTS`, `Interoperable Europe Act` og `European Digital Identity Wallet`.
6. Etter hver batch: oppdatere canvas der det trengs, synke register og kapabilitetsmapping, oppdatere kilder og regenerere webgrunnlaget før neste batch vurderes.
7. Gjøre en avsluttende manuell kontroll av om noen av de identifiserte kapabilitetssvakhetene fortsatt mangler ressurs, og om noen tidligere operative koblinger nå bør flyttes til normerende dekning.

Første operativ kandidatliste fra råfila, sortert etter sannsynlig behov for nye ressursfiler:
1. `PPP(P)`-nettverket: sannsynlig ny samhandlingsressurs hvis status, varighet og eier kan dokumenteres.
2. `eForvaltningsforskriften`: tydelig regulativ kandidat som bør vurderes som egen ressurs dersom vi finner tilstrekkelig kildeforankring.
3. `Tilskudd til digital inkludering`: må avklares om dette er én samlet ordning eller flere nært beslektede virkemidler.
4. `Konkurranseevnefondet (EKF)`: foreløpig lavere prioritet, men bør vurderes om ordningen har tydelig NA-verdi og stabil forankring.
5. `Nasjonal portefølje`: må avklares om dette er en konkret ressurs eller primært et styringsprinsipp/arbeidsform.
6. `Regulatorisk sandkasse for KI`: mulig samhandlingsressurs, men krever særlig avklaring av varighet og avgrensning.
7. `Nasjonal indeks for digital inkludering`: mulig ny ressurs hvis den har en tydelig og varig rolle i styring eller analyse.

Allerede registrerte eller delvis dekkede kandidater som ikke skal behandles som nye førstegangskandidater:
1. `Stimulab`: allerede registrert som egen virkemiddelressurs.
2. `Medfinansieringsordningen`: allerede registrert som egen virkemiddelressurs.
3. `Rammeverk for innovasjon i offentlig sektor`: dekker deler av virkemiddel- og innovasjonssporet og må vurderes som alternativ eller komplement til flere av de pedagogiske og økonomiske kandidatene.
4. `Forskrift om IT-standarder i offentlig forvaltning`: allerede registrert som `DIGDIR-060` i [137-Forskrift-om-IT-standarder-i-offentlig-forvaltning-v2-copilot.md](../arkitektur/ressurser/rammer-og-virkemidler/137-Forskrift-om-IT-standarder-i-offentlig-forvaltning-v2-copilot.md). Sto feilaktig oppført som ny kandidat; eventuell videre innsats er revisjon av eksisterende beskrivelse, ikke opprettelse.

Åpne vurderinger:
- Om `PPP(P)` skal eies av `DIGDIR` eller `FELLES` må avklares mot faktisk styringsmodell.
- Om `Digital Europe Programme` og `OECD OPSI` skal registreres som egne ressurser, eller kun som del av en bredere økonomisk/juridisk eller samhandlingsressurs, må avgjøres på grunnlag av konkret relevans.
- Om `NOBID` er en selvstendig ressurs eller først og fremst et prosjekt-/programspor må vurderes mot dagens status og koblingen til europeisk digital identitetslommebok.
- For regelverk og infrastruktur på EU-nivå må det skilles tydelig mellom juridisk ramme, felles internasjonal infrastruktur, norsk implementering og norsk løsning, slik at registeret ikke får duplikater.

### Tillegg 2026-06-25 (Maskinporten spisset med nye kilder)

- Opprettet [02-Maskinporten-produkt-canvas-v4-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/02-Maskinporten-produkt-canvas-v4-codex.md) som ny aktiv versjon for `DIGDIR-002`.
- Spisset beskrivelsen fra generell API-sikkerhet til fire tydelige mønstre: vanlig scope-basert tilgang, API-delegering, systembruker og samtykketoken.
- Brukt nye Digdir-kilder for delegering, systembruker og samtykke, og lagt dem inn i [sources/links.md](../sources/links.md) for videre gjenbruk.
- Tydeliggjort at Maskinporten alene dekker virksomhetsautentisering og tokenutstedelse, mens Altinn Autorisasjon tilfører delegasjon, finmasket rettighetskontroll eller samtykkegrunnlag avhengig av scenario.
- Gjenstående oppfølging i denne runden: synke register, kapabilitetsmapping og generert webgrunnlag til `v4`, og verifisere grønn kvalitetsport etter regenerering.

### Tillegg 2026-06-23 (stabilisering av kapabilitetspublisering)

- Rettet publiseringslogikken for kapabilitetssider slik at korte evnebeskrivelser fortsatt vises i Hugo-oversikter uten at de blir tomme ved feil i template-behandling.
- Identifisert at underkapabiliteter manglet relaterte ressurser i nettvisningen fordi generatoren la disse i brødteksten, mens `list.html` viser `productsMarkdown` for kapabilitetssider. Oppdatert `generate-capabilities.py` slik at underkapabiliteter nå også får `productsMarkdown`.
- Regenerert kapabilitetssidene i `web/hugo-prototype/content/kapabiliteter/` slik at underkapabiliteter som `Tjenestekjeder` og `Anvendelse av veiledning` igjen har relaterte ressurser tilgjengelig i presentasjonslaget.
- Lagt til ny build-kontroll i `Publish Hugo Prototype to GitHub Pages`: `web/hugo-prototype/scripts/validate-built-prototype.py` skal stoppe deploy hvis kapabilitetsintroer eller delkapabilitetskort blir tomme i bygget HTML.
- Gjenstående oppfølging: verifisere grønn deploy og kontrollere live-visning av minst én hovedkapabilitet og to underkapabiliteter etter neste push.

### Tillegg 2026-06-22 (MinID manglet i ressursoversikten)

- Kontrollert Samarbeidsportalen-siden for MinID: https://samarbeid.digdir.no/minid/minid/3634.
- Bekreftet at MinID manglet som egen ressurs i `arkitektur/ressurser/produktnummerering.md`, `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`, `sources/links.md` og generert webgrunnlag.
- Opprettet MinID som ny Digdir-ressurs `DIGDIR-063` med løpenummer `140`: [140-MinID-produkt-canvas-v1-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/140-MinID-produkt-canvas-v1-codex.md).
- Avgrenset MinID som personlig eID og autentiseringstjeneste, ikke som generell innloggingsplattform eller autorisasjonstjeneste. Ressursen kobles derfor smalt til `Sikring av informasjonsflyt og datautveksling`, `Autentisering` og `Identifisering`.
- Videre plan: vurdere om andre selvstendige tillitstjenester som i dag bare er omtalt indirekte gjennom ID-porten, også bør inn som egne ressurser eller eksplisitt avgrenses i ID-porten-canvaset.

### Tillegg 2026-06-22 (forbedret publiseringskontroll for Hugo)

- Undersøkt gjentatte røde `Publish Hugo Prototype to GitHub Pages`-kjøringer i GitHub Actions. `Encoding Guard` var grønn, mens publiseringsjobben feilet i steget `Build prototype`.
- Feilen startet med modell-/kapabilitetssynken i commit `de2cc5e`, da kapabilitetsgeneratoren begynte å skrive lange modellbeskrivelser inn i Hugo-frontmatter.
- Rotårsak: generatoren skrev `description: "..."` uten å escape vanlige anførselstegn i tekst, for eksempel `"Tillit"` og `"se"`. Dette ga ugyldig frontmatter og stoppet Hugo-build.
- Rettet `web/hugo-prototype/scripts/generate-capabilities.py` slik at frontmatter-strenger skrives med trygg escaping.
- Lagt til `web/hugo-prototype/scripts/validate-hugo-frontmatter.py` og koblet den inn i både `Encoding Guard` og `Publish Hugo Prototype to GitHub Pages`, slik at tilsvarende feil fanges tydeligere før Hugo-build.

### Tillegg 2026-06-18 (status etter modelloppdatering og kapabilitetsendringer)

- Kontrollert siste commits etter ChatGPT-oppdateringen av arkitekturmodellen:
  - `de2cc5e` synket råmodellen fra Digdir, oppdaterte [capabilities.yaml](../arkitektur/kapabiliteter/capabilities.yaml), oppdaterte [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) og regenererte kapabilitetssider.
  - `a1d2e02` ryddet kildelister i tre ressursbeskrivelser.
  - `77e5f88` oppdaterte kapabilitetslabeler fra `Meldingsformidling` til `Meldingsutveksling` i berørte ressursbeskrivelser og [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md).
- Fulgt opp et restpunkt i denne runden: regenerert ressursoversikten med `web/hugo-prototype/scripts/generate-products.ps1`, slik at webvisningen nå henter `Meldingsutveksling` fra oppdatert register og mapping.
- Fjernet foreldet generert kapabilitetsside for `meldingsformidling`, slik at webgrunnlaget ikke lenger har en parallell, utgått delkapabilitetsside ved siden av `meldingsutveksling`.
- Foreløpig vurdering av modellstatus: Oppdateringen av kuratert kapabilitetsmodell, aktiv mapping, registerlabeler og avledede webvisninger er fullført for denne konkrete modellendringen. Arbeidet med en varig synkpipeline, Turtle/grafspor og mer automatisk differanserapportering står fortsatt som videreutvikling.
- Foreløpig vurdering av konsekvens for ressursbeskrivelser/canvaser:
  - Den direkte navne- og ID-effekten er håndtert for `Meldingsutveksling` i mapping, register og berørte aktive ressursbeskrivelser.
  - Det er ikke gjennomført en full faglig konsekvensanalyse av alle nye kapabilitetsbeskrivelser mot innholdet i ressurscanvasene.
  - De nye kapabilitetsbeskrivelsene er betydelig rikere enn tidligere og kan påvirke hvordan canvasene bør fylle ut særlig `Kapabiliteter`, `Støtter arkitekturprinsipper`, avgrensning, styring/forvaltning og eventuell gap-/modenhetsvurdering.
  - Brødtekst som bruker ordet `meldingsformidling` som vanlig fagbegrep trenger ikke automatisk endres, men kapabilitetsseksjoner skal bruke kanonisk navn `Meldingsutveksling`.

Plan videre etter statuskontrollen:
1. Lage en liten endringsanalyse av kapabilitetsbeskrivelsene som har størst semantisk endring, ikke bare navneendring.
2. Prioritere ressurscanvaser som er tett koblet til disse kapabilitetene eller som har svak/tynn kapabilitetsbegrunnelse.
3. Gjøre et målrettet kvalitetsløft i canvasene der nye kapabilitetsbeskrivelser gir tydeligere krav til juridisk, organisatorisk, semantisk eller teknisk vurdering.
4. Utvide kontrollskript eller egen rapport slik at foreldede kapabilitetsslugger i genererte webfiler og avledede mappingseksjoner fanges automatisk.

Status 2026-06-18 etter gjennomføring av denne planen:
1. Opprettet [2026-06-18-kapabilitetsendringer-konsekvensanalyse-v1.md](./arbeidsstyring-og-handover/2026-06-18-kapabilitetsendringer-konsekvensanalyse-v1.md) med endringsanalyse, prioritert canvaskø og videre anbefalinger.
2. Prioriterte første batch mot normerende ressurser med tynn kapabilitetsseksjon, særlig `DIGDIR-033`, `DIGDIR-034`, `DIGDIR-035`, `DIGDIR-025`, `DIGDIR-030`, `DIGDIR-031`, `DIGDIR-032` og `DIGDIR-041`.
3. Løftet `DIGDIR-033` Referansearkitektur forsendelse (eMelding) til [101-Referansearkitektur-forsendelse-eMelding-v2-codex.md](../arkitektur/ressurser/normerende-ressurser/101-Referansearkitektur-forsendelse-eMelding-v2-codex.md), med styrket vurdering av `Meldingsutveksling`, forpliktelsesnivå, bruksområde, risiko og avgrensning mot eOppslag/hendelser.
4. Utvidet [check-resource-version-sync.py](../tools/check-resource-version-sync.py) slik at kontrollen også fanger avledede produktreferanser i mappingen, ukjente kapabilitetsslugger/ID-er og foreldede genererte kapabilitetssider.
5. Kanoniserte eldre `capability_id`/`subcapability_id` og foreldrekoblinger i avledede mappingseksjoner mot dagens [capabilities.yaml](../arkitektur/kapabiliteter/capabilities.yaml), slik at kontrollen ikke bare fanger, men også tåler semantiske flyttinger i modellen.
6. Synket register, mapping og webgrunnlag slik at `DIGDIR-033` peker til `v2`, og slik at avledede mappingreferanser ikke blir liggende på eldre ressursversjoner.
7. Committet og pushet første oppfølging som `fb517a5` (`Følg opp kapabilitetsendringer i ressursgrunnlag`) 2026-06-19.

Status 2026-06-19 etter neste canvasløft:
1. Løftet `DIGDIR-034` Referansearkitektur forespørsel-svar (eOppslag) til [102-Referansearkitektur-foresporsel-svar-eOppslag-v2-codex.md](../arkitektur/ressurser/normerende-ressurser/102-Referansearkitektur-foresporsel-svar-eOppslag-v2-codex.md), med styrket vurdering av `Bruke data fra andre`, formål, tilgang, ansvar, datakvalitet, sporbarhet og robusthet.
2. Korrigert planreferansen fra `DIGDIR-035` til `DIGDIR-027` for Arkitektur for hendelser, siden registeret viser at `DIGDIR-035` er `Nasjonalt veikart`.
3. Løftet `DIGDIR-027` Arkitektur for hendelser til [87-Arkitektur-for-hendelser-v2-codex.md](../arkitektur/ressurser/normerende-ressurser/87-Arkitektur-for-hendelser-v2-codex.md), med styrket vurdering av `Hendelsesdrevet`, hendelseseierskap, publisering, abonnement, metadata, tilgang, idempotens, rekkefølge og avgrensning mot kommandoer/oppslag/meldingsforsendelse.
4. Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md), [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml), [sources/links.md](../sources/links.md) og konsekvensanalysen slik at de peker til de nye `v2`-filene og dagens kanoniske Digdir-lenker.

Status 2026-06-19 etter webfeil og tredje canvasløft:
1. Kontrollert at lokalt generert Hugo-innhold allerede viser `DIGDIR-034` eOppslag som `v2`; skjermbildet fra nett skyldes derfor publiseringsforsinkelse, cache eller en tidligere Pages-deploy. Ny push av denne batchen vil trigge ny Hugo/Pages-publisering.
2. Løftet `DIGDIR-025` Rammeverk for digital samhandling til [85-Rammeverk-for-digital-samhandling-v2-codex.md](../arkitektur/ressurser/normerende-ressurser/85-Rammeverk-for-digital-samhandling-v2-codex.md), med sterkere vurdering av juridisk, organisatorisk, semantisk og teknisk samhandling.
3. Løftet `DIGDIR-030` Overordnede arkitekturprinsipper for offentlig sektor til [98-Overordnede-arkitekturprinsipper-for-offentlig-sektor-v2-codex.md](../arkitektur/ressurser/normerende-ressurser/98-Overordnede-arkitekturprinsipper-for-offentlig-sektor-v2-codex.md), med sterkere kobling til `Arkitekturstyring`, portefølje, avvik og oppfølging av nasjonale byggeklosser.
4. Neste naturlige kandidater er `DIGDIR-031` Sjekkliste for sammenhengende tjenester og `DIGDIR-032` Kart for tjenestekjeder.

### Tillegg 2026-06-17 (plan for oppdatering av rammeverksmodell fra Digdir)

- Bekreftet at endringene i mastermodellen ikke bare gjelder definisjonstekst: det er også strukturelle forskjeller (blant annet opprydding av copy-elementer, navneendring i delkapabilitet og justerte view-navn).
- Bekreftet at kapabilitetsbeskrivelser er endret bredt i modellen, og at oppdatering av beskrivelser derfor skal inngå som en eksplisitt del av oppdateringsløpet, ikke bare indirekte følge av teknisk synk.
- Besluttet arbeidsformat for oppdatering nå:
  1. Autoritativ kilde: ArchiMate fra Digdir-repoet `digdir/nasjonal-arkitektur`.
  2. Operativ arbeidsfil i dette repoet: [arkitektur/kapabiliteter/capabilities.yaml](../arkitektur/kapabiliteter/capabilities.yaml) (kuratert struktur for analyser og ressurskobling).
  3. Turtle beholdes som senere spor (phase 2) for kunnskapsgraf/SPARQL, ikke som blokkering for neste oppdateringsrunde.

Plan for gjennomføring (modelloppdatering):
1. Hente ny mastermodell (ArchiMate + YAML) fra `digdir/nasjonal-arkitektur` og lage maskinell differanse mot lokal råmodell i `sources/`.
2. Dele differansen i tre spor:
	- Beskrivelsesendringer på kapabiliteter/prinsipper/mål.
	- Strukturelle endringer i elementer, relasjoner og navngivning.
	- Endringer som påvirker ID-stabilitet (potensiell effekt på mapping og historikk).
3. Oppdatere [arkitektur/kapabiliteter/capabilities.yaml](../arkitektur/kapabiliteter/capabilities.yaml), [arkitektur/prinsipper/principles.md](../arkitektur/prinsipper/principles.md) og [arkitektur/maal/maal.md](../arkitektur/maal/maal.md) i samme endringssett.
4. Kjøring av sammenhengs- og websjekk før merge:
	- `python tools/check-resource-version-sync.py`
	- `python web/hugo-prototype/scripts/validate-text-encoding.py`
	- `powershell -ExecutionPolicy Bypass -File tools/check-mojibake.ps1 -Root .`
	- Regenerering av relevante sider i `web/hugo-prototype/content/` som avhenger av kapabiliteter/prinsipper/mål.
5. Publiseringskontroll etter regenerering:
	- Verifisere at kapabilitetssider, prinsippsider og ressursoversikt viser samme navn/beskrivelse som kildene over.
	- Kontrollere at lenker og referanser i webinnhold ikke peker til utgåtte kapabilitetsnavn.

Status kjøring 2026-06-17 (påbegynt gjennomføring):
1. Oppdatert råkilde [Nasjonal Arkitektur kapabilitetsmodell-2026-05-20.archimate](../sources/Nasjonal%20Arkitektur%20kapabilitetsmodell-2026-05-20.archimate) mot siste master fra Digdir.
2. Oppdatert [capabilities.yaml](../arkitektur/kapabiliteter/capabilities.yaml) med nye kapabilitetsbeskrivelser fra master, inkludert strukturell endring fra `Meldingsformidling` til `Meldingsutveksling`.
3. Oppdatert [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) slik at delkapabilitets-ID/navn/slug/mapping-label peker til `Meldingsutveksling`.
4. Regenerert kapabilitetssider i `web/hugo-prototype/content/kapabiliteter/` og synket prinsippsiden via eksisterende script.
5. Verifisert grønn validering etter oppdatering:
	- `python tools/check-resource-version-sync.py`
	- `python web/hugo-prototype/scripts/validate-text-encoding.py`
	- `powershell -ExecutionPolicy Bypass -File tools/check-mojibake.ps1 -Root .`

Plan for nye analyser etter oppdatering:
1. Endringsanalyse av ressurskoblinger i [arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) for kapabiliteter med navne- eller ID-endring.
2. Hurtig kvalitetsanalyse av ressursbeskrivelser som nevner berørte kapabiliteter direkte i tekst (for å unngå semantisk drift).
3. Oppdatert gap-analyse mot aktive case i `analyser/` der nye beskrivelser kan gi annen prioritering av kapabilitetsbehov.

### Tillegg 2026-06-17 (forslag til målarkitektur og migreringsplan mellom repo)

Målbildet er todelt:
1. `digdir/nasjonal-arkitektur` forblir autoritativ kilde for rammeverksmodellen.
2. `NA-kunnskap` forblir faglig underlag for ressursbeskrivelser, analyser, webvisninger og KI-arbeidsflyt.

Foreslått ny komponent under Digdir:
- Nytt repo under Digdir, foreslått navn: `digdir/na-sync-pipeline`.
- Formål: automatisert synk mellom modellrepoet og underlagsrepoet, med validering, differanserapport og PR-automasjon.

Faseplan for migrering:
1. Fase A (nå, lav risiko):
	- Etablere `digdir/na-sync-pipeline`.
	- Lage planlagt jobb (ukentlig + ved modellendring) som henter siste modell fra `digdir/nasjonal-arkitektur`.
	- Generere forslag til oppdatering av kuraterte arbeidsfiler for `NA-kunnskap` og opprette PR med differanserapport.
2. Fase B (stabilisering):
	- Legge inn obligatoriske kontroller i pipeline: versjonssynk, encoding/mojibake og webregenerering.
	- Stoppe automerge ved ID-brudd eller større strukturelle avvik som krever manuell vurdering.
3. Fase C (videreutvikling):
	- Legge til valgfri Turtle-eksport og grafanalyse som separat jobb, uten å blokkere ordinær synk.
	- Etablere måleparametere (oppdateringstid, avvikstype, andel automatisk godkjente oppdateringer).

Vedlikeholdsregime for videre utvikling:
1. Rammeverksendringer (Digdir):
	- Eies og forvaltes i `digdir/nasjonal-arkitektur`.
	- Endringer trigges videre via webhook/schedule til `digdir/na-sync-pipeline`.
2. Ressurser, visninger og KI-underlag (NA-kunnskap):
	- Eies og forvaltes i `NA-kunnskap`.
	- Oppdateringer fra modell kommer som sporbare PR-er, med krav om grønn validering før merge.
3. KI-søk og analyseforbedringer:
	- Holdes i `NA-kunnskap` (dataforberedelse, kuraterte filer, analyser, webinnhold).
	- Eventuelle graf-/SPARQL-søk fra Turtle legges som tilleggsspor etter at fase A/B er stabil.

Hvorfor ikke full sammenslåing i ett repo nå:
- Ulike livssykluser og arbeidsprosesser for modellering (Digdir) og kunnskapsforvaltning/analyse (NA-kunnskap).
- Høyere operasjonell risiko ved å blande publiseringsflyter og kvalitetssikring i ett repo i tidlig fase.
- Federert oppsett med automatisk synk gir profesjonalisering nå, uten å låse fremtidig strukturvalg.

### Tillegg 2026-06-17 (ukentlig ressursbatch: helsedata og pasientregistre)

- Opprettet nye `v2`-versjoner for [31-Helsedata-no-produkt-canvas-v2-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/31-Helsedata-no-produkt-canvas-v2-codex.md), [135-Norsk-pasientregister-produkt-canvas-v2-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/135-Norsk-pasientregister-produkt-canvas-v2-codex.md) og [136-Kommunalt-pasient-og-brukerregister-produkt-canvas-v2-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/136-Kommunalt-pasient-og-brukerregister-produkt-canvas-v2-codex.md).
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md), [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) og relevante genererte kapabilitets- og ressurssider i `web/hugo-prototype/content/` slik at aktive pekere nå viser til `v2`.
- La inn nye stabile helsedatalenker i [sources/links.md](../sources/links.md) for Helsedataservice, `Om NPR`, `Søk om data fra NPR` og `Om KPR`.
- Bekreftet grønn `check-resource-version-sync.py`, grønn `validate-text-encoding.py` og grønn mojibake-sjekk etter endringene.
- Vurderte også `DIGDIR-039` og `DIGDIR-040`, men lot dem stå til neste batch fordi helsedatasporet ga tydeligere og mer presis gevinst i denne runden.
- Opprettet batchrapporten [2026-06-17-ukentlig-ressursbatch-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-06-17-ukentlig-ressursbatch-v1.md).

### Tillegg 2026-06-17 (ukentlig kvalitetsrapport for ressursbeskrivelser)

- Opprettet [2026-06-17-kvalitetsrapport-ressursbeskrivelser-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-06-17-kvalitetsrapport-ressursbeskrivelser-v1.md) med oppdatert revisjonskø etter at flere tidligere toppkandidater er løftet til `v2`.
- Bekreftet at aktive registerpekere fortsatt ikke peker til `v0`, og at sterkeste restgjeld nå ligger i `DIGDIR-039`, `DIGDIR-040`, `DIGDIR-055`, en liten helsebatch rundt `FHI-005` og `FHI-006`, samt `HELFO-001`.
- Bekreftet at `DIGDIR-041`, `HDIR-002` og `DIGDIR-029` har falt ut av øverste revisjonskø fordi registeret nå peker til `v2`.

### Tillegg 2026-06-17 (ukentlig avviksvakt)

- Opprettet [2026-06-17-ukentlig-avviksvakt-na-kunnskap-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-06-17-ukentlig-avviksvakt-na-kunnskap-v1.md) for ny kontroll av ressursregister, kapabilitetsmapping og valideringsskript.
- Bekreftet fortsatt grønn aktiv versjonssynk, grønn metadata-kontroll uten foreslåtte endringer, grønn UTF-8-validering og grønn mojibake-sjekk.
- Fant ett skjult vedlikeholdsavvik i [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml): avledede produktlister under kapabilitetsseksjonene inneholder eldre metadata for 12 produkter selv om toppnivået i samme fil er korrekt.
- Registrerte samtidig et lavt prosessavvik: dagens kontrollskript fanger ikke denne interne inkonsistensen fordi de bare validerer toppnivået i `products`.

### Tillegg 2026-06-08 (ukentlig avviksvakt, oppfolgingskjoring)

- Opprettet [2026-06-08-ukentlig-avviksvakt-na-kunnskap-v2.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-06-08-ukentlig-avviksvakt-na-kunnskap-v2.md) for en ny kontrollrunde samme dag, basert på siste automasjonsvindu.
- Bekreftet på nytt grønn versjonssynk, grønn metadata-kontroll uten foreslåtte endringer, grønn UTF-8-validering og grønn mojibake-sjekk.
- Verifisert at det ikke finnes nye commits eller ressursendringer i relevant område siden forrige kjøring.
- Registrerte bare ett lavt prosessforhold utenfor ressurskontrollen: arbeidskopien har lokale endringer i `AGENTS.md`, `briefs/decisions.md` og `briefs/arbeidsstyring-og-handover/automatiske-rapporter/README.md`.

### Tillegg 2026-06-08 (ukentlig avviksvakt)

- Opprettet [2026-06-08-ukentlig-avviksvakt-na-kunnskap-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-06-08-ukentlig-avviksvakt-na-kunnskap-v1.md) for ukentlig kontroll av register, kapabilitetsmapping og valideringsskript.
- Bekreftet grønn versjonssynk, grønn metadata-kontroll uten foreslåtte endringer, grønn UTF-8-validering og grønn mojibake-sjekk.
- Verifisert at ressursløftene fra 2026-06-07 for `HDIR-002`, `DIGDIR-029` og `DIGDIR-041` allerede er korrekt registerført og synkronisert i aktiv mapping.
- Fant ingen nye avvik mellom ressursfiler, register og kapabilitetsmapping i denne kontrollrunden.

### Tillegg 2026-06-07 (ukentlig ressursbatch: HPR + informasjonsforvaltning + kapabilitetskart)

- Opprettet nye `v2`-versjoner for `HDIR-002` HPR, `DIGDIR-029` Rammeverk for informasjonsforvaltning og `DIGDIR-041` Kapabilitetskart (planlagt): [64-HPR-produkt-canvas-v2-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/64-HPR-produkt-canvas-v2-codex.md), [89-Rammeverk-for-informasjonsforvaltning-v2-codex.md](../arkitektur/ressurser/normerende-ressurser/89-Rammeverk-for-informasjonsforvaltning-v2-codex.md) og [109-Kapabilitetskart-planlagt-v2-codex.md](../arkitektur/ressurser/normerende-ressurser/109-Kapabilitetskart-planlagt-v2-codex.md).
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) og [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) slik at aktive pekere nå viser til `v2`, og erstattet foreløpige automapping-tekster for `DIGDIR-029` med faglig begrunnede forklaringer.
- Regenererte relevante kapabilitets- og ressursoversikter i `web/hugo-prototype/content/` og bekreftet grønn `check-resource-version-sync.py`, grønn `validate-text-encoding.py` og grønn mojibake-sjekk.
- Vurderte også `DIGDIR-039` og `DIGDIR-040`, men lot dem stå til neste batch fordi nyere åpne kilder ga størst gevinst på de tre ressursene over.
- Opprettet batchrapporten [2026-06-07-ukentlig-ressursbatch-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-06-07-ukentlig-ressursbatch-v1.md).

### Tillegg 2026-06-06 (ukentlig kvalitetsrapport for ressursbeskrivelser)

- Opprettet [2026-06-06-kvalitetsrapport-ressursbeskrivelser-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-06-06-kvalitetsrapport-ressursbeskrivelser-v1.md) med oppdatert revisjonskø for svake eller ujevne ressursbeskrivelser.
- Bekreftet at aktive registerpekere fortsatt ikke peker til `v0`, men at revisjonsgjelden nå særlig ligger i aktive `v1`-filer og utforskende normeringsspor med svak beslutningsstøtte.
- Ny toppkø fra denne runden: `DIGDIR-041` Kapabilitetskart (planlagt), `HDIR-002` HPR, `DIGDIR-039` Kunnskapsgrunnlag og KPI-er for datadeling, `DIGDIR-040` Kunnskapsgrunnlag dataspaces og `DIGDIR-029` Rammeverk for informasjonsforvaltning.
- Bekreftet at `DIGDIR-037`, `DIGDIR-048` og `SIKT-006` har falt ut av øverste revisjonskø etter løft til `v2`.

### Tillegg 2026-06-04 (kilde for rammeverkskategorier)

- Dokumenterte i [styringsregler.md](../arkitektur/ressurser/styringsregler.md) at de fire ressurskategoriene kommer fra rammeverket for nasjonal arkitektur og brukes som repoets operative ressursinndeling.
- Speilet forklaringen i [arkitektur/ressurser/README.md](../arkitektur/ressurser/README.md), med intern beslutningsreferanse og ekstern lenke til rammeverket for nasjonal arkitektur.
- Presiserte beslutningsloggen slik at raden om ressurskategorier eksplisitt sier at kategoriene kommer fra rammeverket.

### Tillegg 2026-06-01 (ukentlig avviksvakt)

- Opprettet [2026-06-01-ukentlig-avviksvakt-na-kunnskap-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-06-01-ukentlig-avviksvakt-na-kunnskap-v1.md) for ukentlig kontroll av register, kapabilitetsmapping og valideringsskript.
- Bekreftet grønn versjonssynk, grønn metadata-kontroll uten foreslåtte endringer, grønn UTF-8-validering og grønn mojibake-sjekk.
- Fant først ett prosessavvik: `DIGDIR-037`, `DIGDIR-048` og `SIKT-006` pekte til nye `v2`-filer som fortsatt var `untracked` i Git.
- Avviket ble deretter rettet ved å legge de tre filene inn i Git-indeksen med eskalert `git add`.
- Årsaken ser ut til å være automasjonsrammen: vanlig filskriving i repoet fungerte, men skriving til `.git` krevde eksplisitt eskalering.

### Tillegg 2026-06-01 (statusjustering for DIGDIR-041 og DIGDIR-037)

- Oppdatert [109-Kapabilitetskart-planlagt-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/109-Kapabilitetskart-planlagt-v1-codex.md) slik at `DIGDIR-041` nå beskrives som `under etablering`, ikke bare planlagt.
- Presisert i samme ressursbeskrivelse at dette er et foreløpig utkast, og at videre oppdateringer bør gjøres manuelt i løpet av 2026 når styringsforankring og faktisk bruk er mer moden.
- Oppdatert aktiv fil for `DIGDIR-037`, [105-Rammeverk-for-Nasjonale-grunndata-v2-codex.md](../arkitektur/ressurser/normerende-ressurser/105-Rammeverk-for-Nasjonale-grunndata-v2-codex.md), fra `aktiv` til `under etablering` etter kontroll mot nyere Digdir-kilder.
- Begrunnelse: Digdir beskriver arbeidet med nasjonale grunndata som utforskende og trinnvis, og statusrapporten fra 2025 legger opp til videre piloter før roller og ansvar formelt etableres bredt.

### Tillegg 2026-05-31 (ukentlig ressursbatch: normering + utdanningsregister)

- Opprettet nye `v2`-versjoner for `DIGDIR-037`, `DIGDIR-048` og `SIKT-006`: [105-Rammeverk-for-Nasjonale-grunndata-v2-codex.md](../arkitektur/ressurser/normerende-ressurser/105-Rammeverk-for-Nasjonale-grunndata-v2-codex.md), [116-Rammeverk-for-innovasjon-i-offentlig-sektor-v2-codex.md](../arkitektur/ressurser/normerende-ressurser/116-Rammeverk-for-innovasjon-i-offentlig-sektor-v2-codex.md) og [52-Nasjonalt-utdanningsregister-produkt-canvas-v2-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/52-Nasjonalt-utdanningsregister-produkt-canvas-v2-codex.md).
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) og [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) slik at aktive pekere nå viser til `v2`, og normalisert navnet for `DIGDIR-037` til `Rammeverk for Nasjonale grunndata`.
- Regenererte relevante kapabilitets- og ressursoversikter i `web/hugo-prototype/content/` etter endringene.
- Vurderte også `DIGDIR-058` Nasjonal sandkasse for digital lommebok og `DIGDIR-041` Kapabilitetskart (planlagt), men løftet dem ikke i denne runden:
- `DIGDIR-058` peker allerede til `v2` og ble nedprioritert bak eldre aktive `v1`-filer med svakere sporbarhet.
- `DIGDIR-041` ble stående fordi videre kvalitetsløft fortsatt er avhengig av tydeligere offentlig styringsforankring enn det åpne kildene viser i dag.
- Opprettet batchrapporten [2026-05-31-ukentlig-ressursbatch-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-05-31-ukentlig-ressursbatch-v1.md).

### Tillegg 2026-05-30 (ukentlig kvalitetsrapport for ressursbeskrivelser)

- Opprettet [2026-05-30-kvalitetsrapport-ressursbeskrivelser-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-05-30-kvalitetsrapport-ressursbeskrivelser-v1.md) med ny prioriteringskø for svake, gamle eller ujevne ressursbeskrivelser.
- Bekreftet at aktive registerpekere fortsatt ikke peker til `v0`, og at revisjonsgjelden nå særlig ligger i enkelte `v1`-filer med tynn prinsippvurdering, svak styringsbeskrivelse eller for lite beslutningsstøtte.
- Ny toppkø fra denne runden: `DIGDIR-037` Rammeverk nasjonale grunndata, `DIGDIR-058` Nasjonal sandkasse for digital lommebok, `SIKT-006` Nasjonalt utdanningsregister, `DIGDIR-048` Rammeverk for innovasjon i offentlig sektor og `DIGDIR-041` Kapabilitetskart (planlagt).
- Bekreftet at `SIKT-003` Opptaksløsninger og `NAV-002` NAIS ikke lenger hører til i første revisjonskø etter at registeret nå peker til `v2`.

### Tillegg 2026-05-29 (mulig webvisning av ressursbeskrivelser)

- Vurder enkel løsning for å vise ressursbeskrivelsene som egne nettsider i Hugo-prototypen, uten å flytte kildemarkdownfilene fra `arkitektur/ressurser/`.
- Anbefalt retning er statisk generering: generatoren leser siste registrerte ressursfil fra `produktnummerering.md`, lager en avledet Hugo-side under `web/hugo-prototype/content/ressursoversikt/ressurser/`, og ressurskortene lenker til denne siden.
- Kilden bør fortsatt være den opprinnelige markdownfila i repoet. De genererte websidene skal behandles som publiseringsformat, på samme måte som dagens ressursoversikt og kapabilitetssider.
- Enkel versjon bør bare ta med siste aktive registerpeker per ressurs, vise markdowninnholdet med standard Hugo-layout og legge inn lenke tilbake til originalfil på GitHub. Historiske versjoner, avansert intern lenkerydding og full arkivvisning kan vente.
- Foreløpig anslag med Codex-hjelp: ca. 0,5-1 arbeidsdag for enkel versjon, avhengig av hvor mye vi vil pusse URL-struktur, tittel/front matter og lenker i første runde.

### Tillegg 2026-05-29 (ressurskort: type og emne)

- Oppdatert ressurskortene i webgeneratoren slik at `Type` viser rammeverkskategorien ressursen ligger under, for eksempel `Gjenbrukbare løsninger`.
- Endret tidligere `Type`-felt fra registeret til `Emne`, slik at innholdet beholdes uten å blande rammeverkskategori og mer konkret ressursbeskrivelse.
- Regenererte hele ressursoversikten med ny visning på toppnivå og kategorisidene.

### Tillegg 2026-05-29 (Datalandsbyen som samhandlingsressurs)

- Opprettet [139-Datalandsbyen-v1-codex.md](../arkitektur/ressurser/samarbeidsfora/139-Datalandsbyen-v1-codex.md) som første eksempel på åpen digital samhandlingsarena / nettforum under `Samhandlingsarenaer og organisering`.
- Registrerte ressursen som `DIGDIR-062` i [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md), med kapabilitetene `Samarbeidsarenaer og nettverk`, `Dele data med andre`, `Bruke data fra andre` og `Datastyring`.
- Justerte mal, prompt og styringsregler slik at åpne nettfora kan beskrives uten å konstruere formelt mandat, beslutningsmyndighet eller saksbehandling der dette ikke er relevant.
- La Datalandsbyen-kildene inn i [sources/links.md](../sources/links.md).

### Tillegg 2026-05-28 (kategoritekster og flytteplan)

- Synkroniserte kategoriordlyd i styringsgrunnlaget med oppdatert begrepsbruk fra `nasjonal-arkitektur.yaml`, med samme fire kategorier som i weben.
- Kortet ned kategoritekstene på nettsiden til maks én introduksjonssetning per kategoriside.
- Gjennomført første flyttevurdering av eksisterende normerende ressurser mot kategorien `Økonomiske og juridiske rammer og virkemidler`.
- Etablerte ny systeminstruks `config/prompts/okonomiske-og-juridiske-rammer-og-virkemidler-canvas.system.md` og ny mal `config/templates/okonomiske-og-juridiske-rammer-og-virkemidler-template.md` for denne kategorien.
- Opprettet nye versjoner [112-Digitaliseringsrundskrivet-v2-copilot.md](../arkitektur/ressurser/rammer-og-virkemidler/112-Digitaliseringsrundskrivet-v2-copilot.md) og [137-Forskrift-om-IT-standarder-i-offentlig-forvaltning-v2-copilot.md](../arkitektur/ressurser/rammer-og-virkemidler/137-Forskrift-om-IT-standarder-i-offentlig-forvaltning-v2-copilot.md), og oppdaterte register og mapping til å peke på disse.

Forslag til flytting i neste endringsrunde:
- `DIGDIR-044` Digitaliseringsrundskrivet: flyttes fra `standarder og veiledning` til `økonomiske og juridiske rammer og virkemidler` (regulativt styringsvirkemiddel).
- `DIGDIR-060` Forskrift om IT-standarder i offentlig forvaltning: flyttes fra `standarder og veiledning` til `økonomiske og juridiske rammer og virkemidler` (bindende forskrift).

Plan for gjennomføring:
1. Opprette nye versjoner av de to ressursfilene i `arkitektur/ressurser/rammer-og-virkemidler/` med samme løpenummer, oppdatert kategori og tydelig ramme-/virkemiddelprofil.
2. Oppdatere pekere i `produktnummerering.md` til nye filstier og versjoner.
3. Oppdatere metadata i `produkt-kapabilitet-koblinger.yaml` (`relative_path`, `product_url`, `version`, `author`) uten å endre kapabilitetsvalg i samme runde.
4. Regenerere ressursoversikt og validere versjonssynk/encoding før eventuell videre flyttebatch.

### Tillegg 2026-05-28 (opprydding eierlinje KS/FIKS)

- Verifisert KS/FIKS-eierskap mot kildelenker i `sources/links.md` og oppdatert eierlinjer i [28-FIKS-Register-produkt-canvas-v3-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v3-codex.md) og [68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v2-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v2-codex.md).
- Standardisert omtale til at KS Digital står som operativ eier, forvalter og driftsansvarlig i de oppdaterte ressursbeskrivelsene, med KS omtalt som strategisk forankring der relevant.
- Harmonisert siste blandede eierformuleringer i [93-Fiks-Digisos-produkt-canvas-v1-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/93-Fiks-Digisos-produkt-canvas-v1-codex.md) og [96-KS-Bekymringsmelding-produkt-canvas-v1-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/96-KS-Bekymringsmelding-produkt-canvas-v1-codex.md), slik at KS Digital er tydelig i forvalterrollen også i brukersegmentbeskrivelsene.

### Tillegg 2026-05-28 (start på nye ressurskategorier)

- Startet overgang til fire rammeverkskategorier i webgrunnlag, styringsregler og mal-/promptgrunnlag: `Gjenbrukbare løsninger`, `Standarder og veiledning`, `Samhandlingsarenaer og organisering` og `Økonomiske og juridiske rammer og virkemidler`.
- Fjernet `Andre ressurser` som målstruktur i webgeneratoren og la opp til at uklassifiserte ressursstier skal være avvik.
- Opprettet teknisk mappe for `rammer-og-virkemidler/`, foreløpig uten aktive ressursbeskrivelser.
- Regenererte ressursoversikten: `Gjenbrukbare løsninger` har 77 ressurser, `Standarder og veiledning` har 25, `Samhandlingsarenaer og organisering` har 9 og `Økonomiske og juridiske rammer og virkemidler` har 0.
- Kjørte `sync-resource-metadata.py`, `check-resource-version-sync.py`, `validate-text-encoding.py` og mojibake-sjekk med grønt resultat. Lokal Hugo-build ble ikke kjørt fordi `hugo` ikke er installert i miljøet.

### Tillegg 2026-05-27 (plan for rammeverkskategorier)

- Opprettet [2026-05-27-overgang-til-rammeverkskategorier-v1.md](./arbeidsstyring-og-handover/2026-05-27-overgang-til-rammeverkskategorier-v1.md) med trygg overgangsplan for å legge ressursoversikten tettere på rammeverksmodellen.
- Anbefalt første steg er å endre synlige kategorinavn og veiledningstekst i weben uten å flytte ressursfiler, endre registerpeking eller remappe kapabiliteter.
- Oppdatert planpremiss: `Andre ressurser` skal fjernes som synlig kategori, de fire rammeverkskategoriene skal være målstrukturen, og de fleste normerende ressurser bør foreløpig ligge under `Standarder og veiledning`.

### Tillegg 2026-05-26 (lavprioritetsvurdering og handover-opprydding)

- Gjennomført lavprioritetsvurdering i tidligere plannotat for koblingsanalysen (nå slettet) for `DIGDIR-033`, `DIGDIR-034`, `DIGDIR-035`, `DIGDIR-036` og `DIGDIR-044`.
- Beslutning: ingen nye mappingkoblinger nå; `DIGDIR-035` og `DIGDIR-044` følges opp i egen styrings-/normeringsrunde ved behov.
- Ryddet handover for prosessen i tidligere handover-notat (nå slettet), med samlet dekning av høy, middels og lav prioritet før opprydding.

### Tillegg 2026-05-26 (ny operativ batch: SIKT-003 og NAV-002)

- Opprettet [49-Opptakslosninger-produkt-canvas-v2-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/49-Opptakslosninger-produkt-canvas-v2-codex.md) med styrket beslutningsstøtte for styringsmodell, sesongkritisk risiko, avgrensning og gjenbruk.
- Opprettet [66-NAIS-produkt-canvas-v2-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/66-NAIS-produkt-canvas-v2-codex.md) med tydeligere avgrensning mellom plattformmodenhet og formell felleskomponentstatus, samt skarpere risikovurdering.
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) og [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) slik at `SIKT-003` og `NAV-002` peker til `v2`.
- Kjørt `sync-resource-metadata.py --apply`, `check-resource-version-sync.py`, `generate-capabilities.py`, `validate-text-encoding.py` og mojibake-sjekk med grønt resultat.

### Tillegg 2026-05-26 (sluttforing koblingsplan batch 1 og 2)

- Presisert [137-Forskrift-om-IT-standarder-i-offentlig-forvaltning-v1-codex.md](../arkitektur/ressurser/normerende-ressurser/137-Forskrift-om-IT-standarder-i-offentlig-forvaltning-v1-codex.md) slik at `Regelverkstolkning` fremgår som primær kobling i tråd med vedtatt mapping for `DIGDIR-060`.
- Oppdatert tidligere plannotat (nå slettet) med korrigert beslutningsrad for `DIGDIR-060` og markert fullført status for validering og handover.
- Opprettet handover-notat (nå slettet) med samlet beslutningstabell, valideringsresultater og avgrensninger.

### Tillegg 2026-05-26 (videreforing batch 2 i koblingsplan)

- Erstattet foreløpige autotekster med faglige begrunnelser i [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) for `DIGDIR-032` (tjenestekjeder og organisatorisk samhandling) og `DIGDIR-038` (dele data med andre og datastyring).
- Oppdatert tidligere plannotat (nå slettet) med status for middels-prioritert batch og konkretisert valideringssteg som gjenstår.
- Beholdt eksisterende delkapabilitetskoblinger for `DIGDIR-045` og `DIGDIR-046` i denne runden (ingen nye delkapabiliteter lagt til).

### Tillegg 2026-05-26 (oppfolging koblingsplan)

- Oppdatert hoy-prioritert femmer i [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) med faglig begrunnede tekster der foreløpige forklaringer sto igjen (`DIGDIR-025` og `DIGDIR-031`).
- Lagt til manglende delkapabiliteter for `DIGDIR-047` (Regelverkstolkning og Anvendelse av veiledning) og `DIGDIR-061` (Utvikling og formidling av veiledning) i samme mappingfil.
- Oppdatert planstatus og beslutningstabell i tidligere plannotat (nå slettet) med Ja/Nei-beslutning per kandidat.
- Verifisert kandidatfiler med filvis kompletthetssjekk (`0 mangler / 0 advarsler` for alle fem).

### Tillegg 2026-05-26 (KS/Fiks-batch)

- Gjennomført avgrenset KS/Fiks-batch med oppdatering av `KS-004`, `KS-008` og `KS-009` til nye versjoner: [28-FIKS-Register-produkt-canvas-v3-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v3-codex.md), [67-FIKS-Folkeregister-produkt-canvas-v2-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/67-FIKS-Folkeregister-produkt-canvas-v2-codex.md) og [68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v2-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v2-codex.md).
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) slik at KS-sporet peker til siste versjoner, og strammet inn typebeskrivelsen for `KS-004` til registerfamilie og tilgangslag.
- Tydeliggjort skillet mellom overordnet `Fiks register` og undertjenestene for folkeregister og skatte-/inntektsopplysninger, inkludert segmentansvar, Altinn-delegering og avhengighet til Skatteetatens endringsløp.
- `KS-010` Fiks kjøretøyregister ble vurdert i samme spor, men ikke oppdatert fordi ressursen fortsatt ikke er ført i aktivt produktregister eller kapabilitetsmapping.

### Tillegg 2026-05-26

- Opprettet ny kvalitetsrapport for ressursbeskrivelser i [2026-05-26-kvalitetsrapport-ressursbeskrivelser-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-05-26-kvalitetsrapport-ressursbeskrivelser-v1.md).
- Reprioritert revisjonskøen: `SIKT-003` Opptaksløsninger, `NAV-002` NAIS, `NOVARI-005` VIGO-portalen, `DIGDIR-058` Nasjonal sandkasse for digital lommebok og `DIGDIR-037` Rammeverk nasjonale grunndata.
- Bekreftet at `DIGDIR-050` Felles designsystem og `DIGDIR-051` Ansattporten har falt ut av toppkøen etter løft til `v2`.

- Kjørt ukentlig avviksvakt og opprettet statusrapporten [2026-05-26-ukentlig-avviksvakt-na-kunnskap-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-05-26-ukentlig-avviksvakt-na-kunnskap-v1.md).
- Bekreftet grønn versjonssynk, grønn metadata-sjekk uten foreslåtte endringer, grønn UTF-8-validering og grønn mojibake-sjekk.
- Fant ingen nye avvik mellom ressursfiler, register og kapabilitetsmapping i denne kontrollrunden.

### Tillegg 2026-05-21 (målbilde-slide)

- Opprettet ny visuell versjon av «Overordnet målbilde for tiltaket» i [2026-05-21-overordnet-malbildet-for-tiltaket-v2-final.pptx](../print/presentasjoner/2026-05-21-overordnet-malbildet-for-tiltaket-v2-final.pptx), med PNG-forhåndsvisning i [2026-05-21-overordnet-malbildet-for-tiltaket-v2-final.png](../print/presentasjoner/2026-05-21-overordnet-malbildet-for-tiltaket-v2-final.png).
- Endret omtalen av operasjonell nytte til «fellesløsninger og andre ressurser» og strammet inn tekst, hierarki og layout etter designprofilen for rapporter og presentasjoner.
- Kjørte layoutkontroll for den genererte sliden med 0 feil og 0 advarsler.

### Tillegg 2026-05-21 (batch 2 gjennomfort)

- Gjennomfort middels-prioritert batch med oppdatering av `DIGDIR-032`, `DIGDIR-038`, `DIGDIR-045` og `DIGDIR-046`.
- Lagt inn manglende `## Navn` i de fire normerende ressursfilene og presisert delkapabilitetsrelevans for veiledningssporet.
- Oppdatert [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) slik at veiledningskoblinger for `DIGDIR-038`, `DIGDIR-045` og `DIGDIR-046` peker på delkapabilitetene `Utvikling og formidling av veiledning` eller `Anvendelse av veiledning`.
- Kjørt `sync-resource-metadata.py --apply`, regenerert kapabilitetssider, synket prinsipper og verifisert grønn `check-resource-version-sync.py` + grønn `validate-text-encoding.py`.

### Tillegg 2026-05-21 (batch 1 gjennomfort)

- Gjennomfort oppdatering av hoy-prioritert femmer for nye delkapabiliteter: `DIGDIR-025`, `DIGDIR-031`, `DIGDIR-047`, `DIGDIR-060` og `DIGDIR-061`.
- Oppdatert kapabilitetskoblinger i [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) med delkapabiliteter for Juridisk samhandling (`Regelverksutvikling`, `Regelverkstolkning`) og Veiledning (`Utvikling og formidling av veiledning`, `Anvendelse av veiledning`).
- Lagt inn manglende `## Navn` i de fem normerende ressursfilene og bekreftet 0 mangler / 0 advarsler i kompletthetssjekk for alle fem.
- Kjørt `tools/sync-resource-metadata.py --apply`, regenerert kapabilitetssider og synket prinsippside i web-prototypen.
- Bekreftet grønn `check-resource-version-sync.py` og grønn `validate-text-encoding.py` etter endringene.

### Tillegg 2026-05-21 (analyse av nye koblinger)

- Opprettet plan- og prioriteringsnotat for vurdering av ressurskoblinger mot nye delkapabiliteter (notatet er senere slettet i opprydding).
- Definerte høy-prioritert førstebatch for vurdering av `DIGDIR-025`, `DIGDIR-031`, `DIGDIR-047`, `DIGDIR-060` og `DIGDIR-061` før bredere oppfølging i mellomprioritert gruppe.
- Kjørte porteføljevis fullstendighetskontroll (siste versjon per ressurs-ID) for å støtte trinnvis analyse- og oppdateringsløp.

### Tillegg 2026-05-21

- Synkroniserte modell-utledede masterfiler mot [Nasjonal Arkitektur kapabilitetsmodell-2026-05-20.archimate](../sources/Nasjonal%20Arkitektur%20kapabilitetsmodell-2026-05-20.archimate): oppdatert [capabilities.yaml](../arkitektur/kapabiliteter/capabilities.yaml), [principles.md](../arkitektur/prinsipper/principles.md) og [maal.md](../arkitektur/maal/maal.md).
- Lagt inn nye delkapabiliteter under `Juridisk samhandling` og `Veiledning`, samt ny prinsippkobling (P6) for `Sluttbrukertjenester` i kuratert kapabilitetsstruktur.
- Oppdatert dokumentasjonsreferanser til ny råmodell i [README.md](../README.md), [arkitektur/README.md](../arkitektur/README.md) og [struktur-og-bearbeiding.md](../arkitektur/struktur-og-bearbeiding.md).
- Regenererte avledet webinnhold for kapabiliteter og prinsipper, og bekreftet at `validate-text-encoding.py` er grønn etter endringen.

### Tillegg 2026-05-19

- Reparerte [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) etter strukturfeil i duplikatopprydding, og bekreftet at fila igjen er gyldig JSON-kompatibel YAML.
- Utvidet `DIGDIR-025` Rammeverk for digital samhandling og `DIGDIR-047` Digitaliseringsvennlig regelverk med kapabiliteten `Juridisk samhandling` i ressursfilene, registeret og kapabilitetsmappingen.
- Regenererte kapabilitetssider og ressursoversikt i `web/hugo-prototype/content/` fra oppdatert register og mapping, slik at webgrunnlaget igjen stemmer med siste gyldige kildefiler.
- Bekreftet at `python tools/check-resource-version-sync.py` og `python web/hugo-prototype/scripts/validate-text-encoding.py` er grønne etter reparasjonen.

### Tillegg 2026-05-18

- Kjørt ukentlig avviksvakt og oppdatert statusrapporten [2026-05-18-ukentlig-avviksvakt-na-kunnskap-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-05-18-ukentlig-avviksvakt-na-kunnskap-v1.md).
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md), [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml), [tools/check-resource-version-sync.py](../tools/check-resource-version-sync.py) og relevante genererte kapabilitets- og ressurssider slik at `128`, `129` og `130` peker til `v2`, og `Altinn Portal` ikke lenger ligger i aktiv kapabilitetsmapping.
- Bekreftet at versjonssynk, UTF-8-validering og mojibake-sjekk er grønne etter oppfølgingen.
- Gjenstående publiseringsblokk er praktisk, ikke faglig: de tre nye `v2`-filene er fortsatt `untracked` fordi denne kjøringen ikke kunne skrive til Git-indeksen.

### Tillegg 2026-05-17

- Løftet `FHI-001` SYSVAK, `FHI-002` MSIS og `FHI-003` Dødsårsaksregisteret fra tidlige `v1`-beskrivelser til nye `v2`-filer med tydeligere lovhjemmel, datatilgang, åpne data, innbygger-/meldingsflater og skarpere avgrensning mot andre helseressurser.
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md), [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml), relevante genererte ressurs- og kapabilitetssider og batchrapporten [2026-05-17-ukentlig-ressursbatch-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-05-17-ukentlig-ressursbatch-v1.md).
- Bekreftet at `python tools/sync-resource-metadata.py --apply` ikke foreslo flere metadataendringer før regenerering av webgrunnlaget.

### Tillegg 2026-05-16

- Lagt inn ny kvalitetskø i [2026-05-16-kvalitetsrapport-ressursbeskrivelser-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-05-16-kvalitetsrapport-ressursbeskrivelser-v1.md).
- Bekreftet at aktive registerpekere ikke lenger peker på `v0`-beskrivelser; hovedgjelden ligger nå i enkelte operative `v1`-filer med svake styrings- og finansieringsfelt.
- Opprettet [118-Felles-designsystem-v2-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/118-Felles-designsystem-v2-codex.md) og [119-Ansattporten-v2-codex.md](../arkitektur/ressurser/operative-losninger-og-tjenester/119-Ansattporten-v2-codex.md).
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md) og [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) slik at de peker til `v2`.

### Tillegg 2026-05-15

- Lagt inn automatisk kandidatrapport for neste arbeidsbolk i [2026-05-15-ukentlig-kandidatplukk-na-ressurser-v1.md](./arbeidsstyring-og-handover/automatiske-rapporter/2026-05-15-ukentlig-kandidatplukk-na-ressurser-v1.md) med prioritert ukesliste for helse- og KS-sporet.

### Tillegg 2026-05-13

- Opprettet [120-Styringsradet-for-felleslosningene-v3-copilot.md](../arkitektur/ressurser/samarbeidsfora/120-Styringsradet-for-felleslosningene-v3-copilot.md) som navnejustert og faglig skjerpet versjon av `DIGDIR-052` Styringsrådet for Digitaliseringsdirektoratets fellesløsninger.
- Oppdatert [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md), [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml) og relevante websider slik at de peker til `v3`.
- Justert [88-Arkitektur-og-standardiseringsradet-v1-codex.md](../arkitektur/ressurser/samarbeidsfora/88-Arkitektur-og-standardiseringsradet-v1-codex.md), [121-Faglig-arena-for-informasjonsforvaltning-og-deling-av-data-v1-codex.md](../arkitektur/ressurser/samarbeidsfora/121-Faglig-arena-for-informasjonsforvaltning-og-deling-av-data-v1-codex.md) og [123-DSOP-samarbeidet-v1-codex.md](../arkitektur/ressurser/samarbeidsfora/123-DSOP-samarbeidet-v1-codex.md) for bedre kryssreferanser og tydeligere rolleavgrensning.
- Oppdatert styrende promptfiler for ressursbeskrivelser og analysearbeid i `config/prompts/` for å stramme inn metode, kildehygiene og forventet analysepresisjon.

### Tillegg 2026-05-12

- Opprettet felles designprofil for leveranser i [designprofil-rapporter-og-presentasjoner.system.md](../config/prompts/designprofil-rapporter-og-presentasjoner.system.md).
- Oppdatert [README.md](../README.md) og forankret praksisen i [decisions.md](../briefs/decisions.md).
- Opprettet [24-kapabilitesanalyse-gapanalyse-kapabiliteter-test-mal.md](../analyser/24-kapabilitesanalyse-gapanalyse-kapabiliteter-test-mal.md) som test av analysemal og visuell profil.

### Tillegg 2026-05-11

- Lagt inn nye `v1`- og `v2`-versjoner for `107`, `108`, `109`, `62`, `34`, `36`, `127`, `131` og `120`.
- Oppdatert register, kapabilitetsmapping og relevante genererte sider i `web/hugo-prototype/content/`.
- Bekreftet at `tools/check-resource-version-sync.py`, `tools/sync-resource-metadata.py` og `web/hugo-prototype/scripts/validate-text-encoding.py` var grønne i arbeidskopien på dette tidspunktet.

### Tillegg 2026-05-07

- Opprettet analysen [23-valg-av-utdanningsloep-analyse.md](../Analyser/23-valg-av-utdanningsloep-analyse.md).

## Hva som nå er gjennomført

- Modelloppdateringen fra Digdir er fulgt opp i `NA-kunnskap` for dagens omfang: råmodell, `capabilities.yaml`, aktiv kapabilitetsmapping, kapabilitetssider, ressursoversikt og berørte `Meldingsutveksling`-labeler er synket.
- Direkte konsekvens av navne-/ID-endringen fra `Meldingsformidling` til `Meldingsutveksling` er håndtert i aktive register- og mappingflater. Bred faglig vurdering av alle nye kapabilitetsbeskrivelser mot ressurscanvasene gjenstår.
- Oppgraderingen av `FLERE-002` DSOP-tjenester, `NHN-003` Kjernejournal og `DIGDIR-052` Styringsrådet for fellesløsningene er fullført.
- Oppgraderingen av `FHI-001`, `FHI-002` og `FHI-003` er nå fullført som samlet helseregisterbatch.
- Oppgraderingen av `KS-004` Fiks register, `KS-008` Fiks folkeregister og `KS-009` Fiks skatte- og inntektsopplysninger er nå fullført som en avgrenset KS/Fiks-batch.
- De nye normerende ressursene `DIGDIR-039`, `DIGDIR-040` og `DIGDIR-041` finnes nå som `v1` og skal ikke lenger følges opp som etableringsløft, men som vanlig kvalitetsrevisjon ved behov.
- Tidligere risiko om at flere nye ressursfiler var `untracked` er ikke lenger den riktige statusbeskrivelsen.

## Foreslått neste prioritering

### Ressursarbeid

- Før neste store ressursbatch bør det gjennomføres en målrettet canvas-konsekvensanalyse av de nye kapabilitetsbeskrivelsene. Start med kapabiliteter der beskrivelsen nå tydeliggjør juridisk, organisatorisk, semantisk eller teknisk vekt på en måte som kan endre vurderingen av ressursenes rolle.
- Prioriter ressursbeskrivelser som enten er koblet til mange kapabiliteter, har gamle/tynne kapabilitetsbegrunnelser eller brukes som sentrale byggeklosser i analyser og weboversikt. Første praktiske batch kan være meldings-/datautvekslingsressursene, der `Meldingsutveksling` nå er kanonisk navn.
- Neste spørsmål om helse:
- Skal `Legemiddelregisteret` opprettes som egen ressurs i denne runden, eller avvente til tydeligere avgrensning mot eksisterende FHI-spor?
- Skal `FHI-005` Norsk pasientregister og `FHI-006` Kommunalt pasient- og brukerregister tas samlet i én batch, eller deles for raskere kvalitetssikring?
- Hvilke minimumskilder må være på plass før helsebolken kan regnes som beslutningsklar i ressursregister og mapping?

- Vurdere `Legemiddelregisteret` som ny egen ressurs i neste helsebolk, siden `FHI-004` nå er avgrenset som historisk registerspor og `FHI-001` til `FHI-003` er løftet.
- Avklare om `KS-010` Fiks kjøretøyregister skal inn som egen registrert ressurs eller behandles annerledes i KS-sporet, siden fila finnes men mangler aktiv register- og mappingpeker.
- Vurdere `DHIS2` som mulig kandidat til ressursoversikten, med eksplisitt opptaksvurdering mot styringsreglene for sektorspesifikke ressurser (tverrsektoriell relevans, varighet, eierforankring og analyseverdi i norske case).
- Vurdere `SIMPL` (Smart Middleware Platform) som mulig kandidat til ressursoversikten, med avklaring av norsk anvendbarhet (EØS-kontekst, governance-behov, juridiske rammer og operativ modenhet for bruk i norske datasamarbeid).
- Vurdere `FHI-005` Norsk pasientregister og `FHI-006` Kommunalt pasient- og brukerregister som neste naturlige helsepar når Legemiddelregisteret er avklart.
- Status mot kvalitetsrapport 2026-05-26: `SIKT-003`, `NAV-002`, `NOVARI-005` og `DIGDIR-058` ble løftet til `v2` i dag og er ikke lenger førsteprioritet i revisjonskøen.
- Prioritet videre fra samme kvalitetsspor: `DIGDIR-037`, `DIGDIR-048` og `SIKT-006` er nå løftet til `v2`; neste naturlige kandidater er `DIGDIR-041` Kapabilitetskart (planlagt), `HDIR-002` HPR og `DIGDIR-029` Rammeverk for informasjonsforvaltning.
- Oppdatert status 2026-06-07: `DIGDIR-041`, `HDIR-002` og `DIGDIR-029` er nå løftet til `v2`; neste naturlige kandidater er `DIGDIR-039`, `DIGDIR-040` og deretter en liten helsebatch med `FHI-005` og `FHI-006`.
- Oppdatert status 2026-06-17: `HDIR-001`, `FHI-005` og `FHI-006` er nå løftet til `v2`; neste naturlige kandidater er `DIGDIR-039`, `DIGDIR-040` og deretter `HELFO-001` KUHR eller en egen avklaring av eier-/forvaltningslinjen for `HDIR-001`.
- Følge opp `DIGDIR-039`, `DIGDIR-040` og `DIGDIR-041` med vanlig kvalitetsrevisjon hvis de viser svak kildeforankring, for tynn kapabilitetskobling eller ujevn beslutningsstøtte.

### Produktregister og avgrensning

- Legge inn kontroll for foreldede kapabilitetsnavn og slugger i generert webinnhold, slik at gamle sider som `meldingsformidling` ikke blir liggende etter modellendringer.
- Planlegge trinnvis innføring av feltet `Type` i ressursbeskrivelser, med samme kategorier som i [produktnummerering.md](../arkitektur/ressurser/produktnummerering.md), slik at koblingen mellom register og enkeltbeskrivelser blir tydelig og konsistent.
- Legge inn en vedlikeholdsforbedring for [produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml): rydde eller regenerere interne, avledede produktlister slik at de ikke har eldre versjonsmetadata enn toppnivåets `products`.
- Utvide [check-resource-version-sync.py](../tools/check-resource-version-sync.py) eller tilstøtende kontrollskript slik at intern inkonsistens i mappingfila også blir fanget i kvalitetsporten, ikke bare utdaterte toppnivåpekere.
- Avklare om `FIKS IO` skal inn som egen ressurs eller fortsatt behandles som teknisk komponent under `FIKS Melding`.
- Vurdere om KS-sporet trenger egen, mer eksplisitt struktur for overordnet registerfamilie versus underliggende undertjenester, nå som `Fiks register` er strammet inn som tilgangslag.
- Vurdere om `DIGDIR-048 Rammeverk for innovasjon i offentlig sektor` bør stå som normerende ressurs eller avgrenses tydeligere.
- Vurdere om FHI-sektoren senere skal utvides med flere tverrgående kandidater, for eksempel `Kreftregisteret`, hvis det kommer tydeligere casebehov.

## Strategiske forbedringer

- Vurdere en enkel evalueringsrubrikk i analysemalen med score for sporbarhet, gjenbrukbarhet, styringsrelevans og presisjon.
- Videreføre arbeidet med tydeligere skille mellom kildegrunnlag, analyse og publiserbar tekst i ressursbeskrivelsene.
- Beholde tydelig merking av KI-støttet arbeidsgrunnlag inntil faglig godkjenningsløp er etablert.
- Vurdere eiernavn i ressursregisteret i to lag: lesbart visningsnavn og registrert navn fra Enhetsregisteret, før eventuell større navneharmonisering.

## Bekjente blokkere og risiko

- Eldre ressursbeskrivelser kan fortsatt gi ujevn retrieval-kvalitet og må forbedres gradvis.
- Produktbeskrivelsene mangler fortsatt helt tydelig skille mellom arbeidsgrunnlag og godkjent innhold flere steder.
- Lokal Hugo-build er ikke verifisert i dette miljøet fordi `hugo` ikke er installert.

## Åpent vurderingsspor for KI-bruk av repoet

**Status:** Ingen beslutning om egen assistent-MVP. Tidligere skisse beholdes som arbeidsnotat: [2026-03-16-dokumentasjonsassistent-mvp-v1.md](./arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md).

**Lavterskelspor som fortsatt er relevant:**

- Bruke GitHub-repoet som åpen kunnskapskilde med tydelig README, struktur og kildepekere.
- Publisere enkel veiledning for bruk av repoet med KI, med krav om kildehenvisning tilbake til repo-filer.
- Prioritere jevn kvalitet i ressursfiler fordi dette gir størst effekt for gjenbruk i eksterne KI-verktøy.
