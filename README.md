# NA-kunnskap

Åpent arbeidsrepo for nasjonal arkitektur: ressursbeskrivelser, kapabiliteter, prinsipper, mål og
analyser, publisert som en lettlest dokumentasjonsprototype.

- Nettsted: <https://suphiro-arch.github.io/NA-kunnskap/>
- Repo: <https://github.com/suphiro-arch/NA-kunnskap>

Innholdet er arbeidsmateriale bygget på åpne kilder, ikke vedtatt styringsdokumentasjon. Det egner
seg til tidlig problemavklaring og til å finne mulig gjenbruk før nye tiltak settes i gang. Det er
ikke tilstrekkelig alene som grunnlag for juridiske vurderinger, anskaffelser eller styringsvedtak.

Beskrivelsene skiller mellom fakta, deduksjon og usikkerhet. Der åpne kilder ikke dekker et forhold,
skal det stå i teksten framfor å fylles med sannsynlige antakelser.

Vil du bruke innholdet mot din egen problemstilling i et KI-verktøy, står oppskriften i
[Bruke innholdet med KI](#bruke-innholdet-med-ki) nederst.

## Hva du finner her

| Mappe | Innhold |
| --- | --- |
| `arkitektur/ressurser/` | ressursbeskrivelser, fordelt på gjenbrukbare løsninger, standarder og veiledning, samhandlingsarenaer og organisering, og økonomiske eller juridiske rammer og virkemidler |
| `arkitektur/kapabiliteter/` | kapabilitetsstrukturen og koblingen mellom ressurser og kapabiliteter |
| `arkitektur/prinsipper/` | arkitekturprinsipper og hvordan de henger på hovedkapabilitetene |
| `arkitektur/maal/` | kuratert målspor for arkitekturmodellen |
| `analyser/` | kapabilitetsanalyser, case-analyser og modenhetsanalyser |
| `sources/` | råkilder og lenkelister, blant annet kapabilitetsmodellen i ArchiMate-format |
| `briefs/` | arbeidsstyring, beslutningslogg og handover |
| `config/` | systempromter, maler og språkregler som styrer innholdsarbeidet |
| `web/hugo-prototype/` | Hugo-kildekoden bak nettstedet |

## Mastergrunnlag

Fire filer er operativ master. Endres noe annet, skal disse følge etter i samme endringssett.

- [produktnummerering.md](arkitektur/ressurser/produktnummerering.md): register over ressurser,
  ressurs-ID-er, eierkoder og gjeldende versjon. Start her for å få oversikt.
- [capabilities.yaml](arkitektur/kapabiliteter/capabilities.yaml): kuratert kapabilitetsstruktur.
- [produkt-kapabilitet-koblinger.yaml](arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml):
  koblingen mellom ressurser og kapabiliteter, med faglig begrunnelse per kobling.
- [principles.md](arkitektur/prinsipper/principles.md): prinsipper og kobling til hovedkapabiliteter.

Kapabiliteter, prinsipper og målspor er kuratert fra
`sources/Nasjonal Arkitektur kapabilitetsmodell-2026-05-20.archimate`, som er modellversjonen
arbeidet så langt bygger på. Masterkilde for videre oppdatering av modellen er Digdirs rammeverk for
nasjonal arkitektur: <https://digdir.github.io/nasjonal-arkitektur/>. Ved avvik er rammeverket
autoritativt, og de kuraterte filene her skal justeres etter det.

[struktur-og-bearbeiding.md](arkitektur/struktur-og-bearbeiding.md) forklarer hvordan råkilder,
kuraterte arbeidsfiler og generert webinnhold henger sammen.
[styringsregler.md](arkitektur/ressurser/styringsregler.md) avgjør hvilken rammeverkskategori en
kandidat tilhører.

## Arbeide i repoet

[AGENTS.md](AGENTS.md) er den autoritative regelfila for alt arbeid her, uansett om det gjøres
manuelt eller med KI-assistent. Den inneholder også kontrollene som skal kjøres før commit.
[briefs/README.md](briefs/README.md) forklarer arbeidsstyringen. Verktøyspesifikke tillegg ligger i
egne filer, som `CLAUDE.md` for Claude på Windows. De utvider AGENTS.md og erstatter den ikke.

Innholdsarbeidet startes manuelt. Det finnes ingen planlagte kjøringer som oppdaterer register,
ressursbeskrivelser eller webinnhold av seg selv.

Kontrollene i `tools/` kjøres eksplisitt i det arbeidet som endrer noe: tegnkoding, versjonssynk
mellom register og mapping, seksjonsstruktur mot malen, kildelenker og innebygd JavaScript i
Hugo-malene. Lokale git-hooks (`tools/setup-git-hooks.ps1`) stopper commit og push ved
tegnkodingsfeil.

To workflows kjører automatisk ved push til `main`: `encoding-guard` validerer tegnkoding, og
`publish-hugo-prototype` bygger nettstedet og publiserer det til GitHub Pages som artifact-deploy.
Bygget HTML committes ikke tilbake til repoet, og genererte oversikter under
`web/hugo-prototype/content/` skal oppdateres fra kildene i `arkitektur/`, ikke håndredigeres.

## Språk og form

- dokumentinnhold skrives på norsk, med `æ`, `ø` og `å`
- ASCII bare der teknikken krever det: filnavn, slugger og kode
- skriv selvstendig og i aktiv form for målgruppen for nasjonal arkitektur, ikke som referat av andre
  dokumenter
- legg ved lenke til kilden framfor å skrive hovedteksten som henvisning
- [sources/links.md](sources/links.md) er førstevalget for eksterne kilder, og oppdateres når nye
  stabile lenker med gjenbruksverdi tas i bruk

## Bruke innholdet med KI

Du kan kombinere innholdet her med din egen problemstilling i et vanlig KI-verktøy, uten backend
eller ekstra oppsett. Poenget er å finne ut hva som allerede finnes før du beskriver noe nytt:
hvilke eksisterende ressurser dekker behovet helt eller delvis, hva står igjen når de er tatt i
bruk, og hva er det da som faktisk mangler.

Kapabilitetsmodellen kan brukes som en veileder inn til gjenbrukbare ressurser. Når du finner hvilke
kapabiliteter behovet ditt handler om, får du samtidig beskrevet behovet i et felles språk som andre
kjenner igjen, og du kan bruke `produkt-kapabilitet-koblinger.yaml` til å gå fra kapabilitet til
ressurser som allerede dekker den. Det gir både et mulighetsrom for gjenbruk, og en struktur
du kan planlegge videre etter: hvilke kapabiliteter du trenger, hvilke ressurser som kan støtte opp
om dem, og hva som mangler i dag.

1. Beskriv behovet konkret: mål, kontekst, aktører, dagens løsning, begrensninger, avhengigheter,
   risiko og hva du ønsker å beslutte.
2. Gi verktøyet tilgang til innholdet — lim inn lenken <https://github.com/suphiro-arch/NA-kunnskap>,
   pek på enkeltfiler, eller lim inn tekstutdrag fra nettstedet.
3. Be det bruke repoet som hovedkilde og merke all annen informasjon eksplisitt som ekstern.
4. Be det finne kandidater til gjenbruk på to måter: via kapabilitetene behovet berører, og ved å
   søke direkte i registeret. Deretter gap, og til slutt lavterskel neste steg.
5. Be det oppgi hvilke filer og versjoner rådene bygger på. Uten kildepeker til repoet er svaret
   ikke etterprøvbart.

### Slik får du en analyse som holder

Forskjellen mellom et generisk og et brukbart svar ligger som regel i disse grepene:

- **Krev at gjenbruk vurderes før nye tiltak.** Uten den rekkefølgen foreslår verktøyet gjerne noe
  nytt som allerede finnes under et annet navn.
- **Krev at ressursbeskrivelsen leses, ikke bare registerlinja.** Registeret sier at en ressurs
  finnes; beskrivelsen sier hva den dekker, hvem som eier den og hvor moden den er.
- **Be om avgrensning i tillegg til treff.** En ressurs som dekker halve behovet er nyttig først når
  det står hva den ikke dekker.
- **Spør etter alle ressurstypene, ikke bare tekniske løsninger.** En løsning er bare én av fire
  kategorier her. Standarder og veiledning, samhandlingsarenaer og organisering, og økonomiske eller
  juridiske rammer og virkemidler er også ressurser som kan dekke behovet, helt eller delvis. Ofte er
  svaret på et behov en standard som allerede finnes eller en arena som allerede har mandatet, ikke
  noe som skal bygges.
- **Be verktøyet si hva det ikke fant.** Registeret er ikke komplett. At en ressurs mangler her,
  betyr ikke at den ikke finnes, og forskjellen mellom «finnes ikke» og «ikke beskrevet her» må stå
  i svaret.
- **Ikke be om beslutningen.** Be om hva som må avklares før du kan beslutte, og hvem som må
  involveres.

### Prompt-mal

```text
Du er faglig rådgiver for [sett inn virksomhet, sektor eller problemområde].
Du henvender deg direkte til meg som bruker.

Bruk innhold fra dette repoet som hovedgrunnlag:
- arkitektur/ressurser/produktnummerering.md (register: start her)
- arkitektur/ressurser/ (ressursbeskrivelsene selv)
- arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml
- arkitektur/kapabiliteter/capabilities.yaml
- arkitektur/prinsipper/principles.md

Oppgave:
[Lim inn problemstilling, målgruppe og ønsket beslutning]

Innhold du skal bruke:
[Lim inn tekstutdrag, nettsidelenker eller fil-lenker her]

Svarformat:
1. Kort oppsummering av behovet slik du forstår det
2. Mulig gjenbruk: eksisterende ressurser som dekker behovet helt eller delvis, med hva hver av dem
   dekker og hva den ikke dekker
3. Restbehov etter gjenbruk, uttrykt som kapabiliteter som må styrkes eller etableres
4. Prinsipper som er relevante for retningen, og hva de krever av løsningen
5. Relevante ressurser i de øvrige kategoriene: standarder og veiledning, samhandlingsarenaer og
   organisering, og økonomiske eller juridiske rammer og virkemidler
6. Gap og avklaringer før beslutning, inkludert hva du ikke fant grunnlag for i repoet
7. Konkrete neste steg med lav terskel og lav kost

Krav:
- Vurder gjenbruk før du foreslår noe nytt.
- Les ressursbeskrivelsen, ikke bare registerlinja, før du vurderer en ressurs som treff.
- Skill mellom fakta, deduksjon og usikkerhet.
- Henvis til konkrete filstier og versjoner i repoet.
- Forklar hvordan kildene henger sammen (register -> ressursfil -> kapabilitetskobling).
- Si eksplisitt hva du ikke fant, og skill "finnes ikke" fra "ikke beskrevet i repoet".
- Bruk full URL i tillegg til filsti når svaret skal deles utenfor repo-kontekst.
- Merk ekstern informasjon eksplisitt som ekstern.
- Ikke konkluder på min beslutning. Vis hva som må avklares før den kan tas.
```
