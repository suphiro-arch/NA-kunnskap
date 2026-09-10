# Mal for samhandlingsarenaer og organisering (Markdown)

Bruk denne malen for ressurser som primært er arenaer, roller eller organiseringsformer for samordning, prioritering, forankring, faglig dialog eller strategisk retning.

Eksempler:
- råd
- nettverk
- åpne digitale samhandlingsarenaer
- nettfora
- faste fagfora
- styringsfora
- samordningsarenaer

Se også:
- `arkitektur/ressurser/styringsregler.md`
- `sources/links.md`

## Arbeidsregel for v0.1
- behold hovedstrukturen også i tidlige versjoner
- fyll ut det som kan bekreftes
- skriv `Foreløpig ikke fylt ut i v0.1.` i felt som ennå ikke er gode nok
- skriv `Ikke relevant` når feltet ikke passer for ressurstypen, for eksempel formell saksinnmelding i et åpent nettforum
- bruk `Status/Livsfase` bare for status på selve forumet, ikke for status på dokumentet eller beskrivelsen

## Forventning til v1
- `v1` skal være egnet som direkte arbeidsgrunnlag i analyser og samordningsvurderinger, ikke bare som omtale av forumet.
- Følgende felt skal normalt være substansielt utfylt i `v1`:
  - `Kort beskrivelse`
  - `Mandat og rolle`
  - `Beslutningsmyndighet og forpliktelse`
  - `Kapabiliteter`
  - `Deltakere og målgruppe`
  - `Hvilke ressurser forumet påvirker`
  - `Arbeidsform og møtearena`
  - `Slik melder du inn en sak`
  - `Typiske saker og leveranser`
  - `Når forumet bør involveres`
  - `Scope og avgrensning`
  - `Grensesnitt mot andre fora`
  - `Relasjon til andre ressurser`
  - `Forretningsverdi og arkitekturverdi`
  - `Lenke til dokumentasjon`
  - `Kildegrunnlag brukt i utfyllingen`
- Hvis forumets rolle, påvirkning, grensesnitt mot andre fora og involveringstidspunkt fortsatt er for uklart, bør dokumentet normalt beholdes som `v0.x`.

## Kort v1-sjekkliste
- Er mandat, rolle og beslutningsmyndighet tydelig nok til direkte analysebruk?
- Er påvirkning på ressurser, involveringstidspunkt og saksbildet konkret beskrevet?
- Er viktige påstander forankret i kilder, eller tydelig merket som deduksjon/usikkerhet?
- Er grensesnitt mot andre fora tydelig nok til å unngå feil bruk av forumet?
- Er kapabilitetslisten skrevet med rene, kanoniske kapabilitetsnavn?

## Merking av fakta, deduksjon og usikkerhet
Skill aktivt mellom det som er bekreftet og det som er tolket. Bruk disse merkene som delfelt i
teksten, ikke som egne overskrifter:

- `**Fakta:**` — bekreftet i åpne kilder eller i repoets egne kilder. Oppgi hvem som sier det.
- `**Deduksjon:**` — rimelig tolkning ut fra kjent kontekst. Skal kunne etterprøves av leseren, og
  skal ikke framstilles som bekreftet.
- `**Ikke offentlig dokumentert i denne arbeidsøkten:**` — forhold som ikke ble funnet i kildene.
  Si hva som mangler, ikke bare at noe mangler.

Merkene brukes særlig i `Status/Livsfase`, `Beslutningsmyndighet og forpliktelse`,
`Arbeidsform og møtearena`, `Slik melder du inn en sak` og `Forvaltningsmodell`, der kildene ofte er
ufullstendige. Usikkerhet er ikke en grunn til å
hoppe over en seksjon: skriv det som er kjent, og merk resten.

### Aksepterte seksjoner utenfor feltlista
Noen seksjoner er i utstrakt bruk uten å stå i feltlista under. De er godtatt av
`tools/check-resource-structure.py`, og skal skrives med disse navnene:

- `Endringer fra forrige versjon` — obligatorisk i revisjoner, utelates i `v1`. Bruk dette navnet
  uten versjonsnummer i parentes. `Endringer i denne revisjonen` finnes i noen eldre filer, men
  skal ikke brukes i nye.


## To typer arenaer i samme mal
Kategorien rommer både formelle organer og åpne arenaer, og malen skal dekke begge uten at noen av
dem må dikte opp felt de ikke har.

- **Formelt organ**: råd, styringsråd, utvalg, fageierforum. Har vedtatt mandat, definert
  medlemskap, møtesyklus og et sekretariat. Alle mandat- og deltakerfeltene skal normalt fylles ut.
- **Åpen arena**: nettforum, fagfellesskap, lavterskelnettverk, praksisfellesskap. Har ofte ingen
  vedtatt mandat, ingen fast medlemsliste og ingen møtesyklus. Da skal feltene beskrive hvordan
  arenaen faktisk virker, ikke et formelt apparat den ikke har.

Skriv `Ikke relevant for denne arenatypen` med én setning om hvorfor, framfor å presse inn en
mandatformulering, en medlemsliste eller en møtesyklus som ikke finnes. En oppdiktet mandattekst er
en verre feil enn et tomt felt, fordi den gir inntrykk av forpliktelse arenaen ikke har.

Hvilken av de to typene arenaen er, skal framgå av `Type arena eller forum`.

## Navn
Det offisielle navnet på samhandlingsarenaen, forumet eller organiseringsressursen.

H1-tittelen øverst i fila er den korte visningstittelen, og skal følge filnavnet. Dette feltet er
det offisielle navnet. De to kan avvike når det offisielle navnet er langt: `# BASIL` med
`## Navn` satt til `BASIL — Barnehage-Statistikk-InnrapporteringsLøsning` er riktig bruk, ikke et
avvik som skal rettes.

## Ressurs ID
Kanonisk ressurs-ID når dette er etablert.
Hvis egen ID ikke er etablert ennå, skriv `Ikke fastsatt ennå`.

## Ressurskategori
Samhandlingsarenaer og organisering

Bruk rammeverkskategorien ordrett, slik den står i `Type`-kolonnen i
`arkitektur/ressurser/produktnummerering.md`. De fire gyldige verdiene er `Gjenbrukbare løsninger`,
`Standarder og veiledning`, `Samhandlingsarenaer og organisering` og
`Økonomiske og juridiske rammer og virkemidler`.

## Type arena eller forum
For eksempel:
- styringsråd
- faglig forum
- nettverk
- åpen digital samhandlingsarena
- nettforum
- fagfellesskap
- samordningsarena
- råd

## Status/Livsfase
Beskriv status på forumet, for eksempel:
- planlagt
- etablert
- aktiv
- under omlegging
- avviklet

Ikke bruk dette feltet til å beskrive modenhet eller dokumentstatus.

## Kort beskrivelse
Kort og selvstendig beskrivelse av hva forumet er, hvorfor det finnes, og hvilken rolle det har i styring, samordning eller forankring.
Ikke begrunn hvorfor forumet er interessant for arkitekturarbeid, analysearbeid eller ressursoversikten. Se regelen i `AGENTS.md`.

## Mandat og rolle
Beskriv:
- hva forumet skal oppnå
- hvilken rolle det har i styring, samordning eller forankring
- om det er rådgivende, koordinerende, besluttende eller forankrende

For en åpen arena uten vedtatt mandat: beskriv formålet arenaen faktisk fyller, og si eksplisitt at
det ikke finnes et vedtatt mandat. Skill mellom det arenaen er ment å være og det den er i praksis
når kildene viser forskjell.

## Beslutningsmyndighet og forpliktelse
Beskriv eksplisitt:
- om forumet kan fatte beslutninger, gi råd, fasilitere dialog eller bare dele erfaringer
- hvem som forventes å følge opp det som kommer ut av forumet
- om føringer, anbefalinger eller beslutninger er bindende, styrende eller veiledende

`Ingen beslutningsmyndighet` er et gyldig og informativt svar, og gjelder de fleste åpne arenaer.
Det skal skrives eksplisitt framfor å utelates, fordi fravær av myndighet er nettopp det en leser
trenger å vite før hen bringer en sak dit. Er myndigheten uavklart i kildene, skriv det, og ikke
gjett i noen av retningene.

## Kapabiliteter
Hvilke kapabiliteter i Nasjonal arkitektur støtter forumet direkte?
Bruk bare kapabiliteter med tydelig og sterk kobling.
Bruk bare rene kapabilitetsnavn i listen. Legg forklaring i tilhørende tekst, ikke i selve navnelabelen.

## Deltakere og målgruppe
Beskriv deltakerbildet eksplisitt i segmenter.
For en åpen arena uten fast medlemskap: beskriv hvem arenaen er åpen for og hvem som faktisk
deltar, framfor å konstruere en medlemsliste. Si om deltakelsen er personlig eller på vegne av en
virksomhet, siden det avgjør hvor forpliktende innspill derfra er.
Bruk gjerne tabell med:
`Deltakersegment | Primært behov | Rolle i forumet | Kommentar`

## Hvilke ressurser forumet påvirker
Beskriv hvilke typer ressurser forumet typisk påvirker eller samordner.

Aktuelle vinkler:
- gjenbrukbare løsninger
- standarder og veiledning
- økonomiske og juridiske rammer og virkemidler
- prioriteringer, veikart eller investeringer
- tverrsektorielle samhandlingsløp

## Arbeidsform og møtearena
Beskriv hvordan forumet faktisk arbeider.
For en åpen arena uten møtesyklus: beskriv kanalen arbeidet skjer i, og hvordan aktiviteten faktisk
oppstår. En arena som lever i en kanal og ikke i møter, skal beskrives slik, ikke tvinges inn i en
møtestruktur.

Aktuelle vinkler:
- møtesyklus
- saksforberedelse
- arbeidsgrupper
- høringer eller innspill
- forankring mellom møtene

## Slik melder du inn en sak
Beskriv den praktiske inngangen for den som ønsker å bringe noe til forumet.

Aktuelle vinkler:
- hvem kan melde inn saker (åpen for alle, bare deltakere, bare sekretariat, bare spesifikke virksomheter)
- hvilken kanal brukes (e-post, skjema, kontakt med sekretariat, gjennom representant, på møte)
- hvilken type saker tas imot (faglige spørsmål, prioriteringsinnspill, konfliktsaker, samordningsbehov)
- hva bør en innmelding inneholde for å behandles effektivt
- hva skjer etter innmelding (hvem besvarer, tidslinje, mulig utfall)
- om det finnes alternativ rute for hastesaker eller lavterskelspørsmål

## Typiske saker og leveranser
Beskriv hva forumet typisk behandler eller utløser.

Aktuelle vinkler:
- prioriteringsinnspill
- anbefalinger
- veivalg
- samordningsbehov
- mandat, referater, beslutninger eller faglige anbefalinger

## Når forumet bør involveres
Beskriv i hvilke situasjoner forumet er særlig relevant i analyse- og utviklingsløp.

Aktuelle vinkler:
- behov for samordning på tvers
- forankring av større tiltak
- konflikt mellom aktører eller prioriteringer
- behov for felles retning eller modenhetsløft

## Scope og avgrensning
Beskriv konkret:
- hva forumet omfatter
- hva det ikke omfatter
- hvor grensene går mot andre fora, linjeorganisasjon eller fagmiljø

## Forvaltningsmodell
Fordel på:
- eier eller oppdragsgiver
- sekretariat
- deltakelse eller medlemskap
- publiserings- eller beslutningsarena

## Grensesnitt mot andre fora
Beskriv eksplisitt hvordan dette forumet skiller seg fra og utfyller andre fora det er naturlig å forveksle eller kombinere med.

Bruk tabell med:
`Forum | Rolle-fordekling | Når dette forumet, når det andre | Typisk samspill`

Aktuelle vinkler:
- hvilke fora adresserer lignende tematikk, men på ulikt nivå (strategisk vs. faglig, tverrsektoriell vs. sektoriell)
- hvilke fora bør involveres i sekvens (f.eks. fagforum først, råd deretter)
- hvilke fora kan ta over en sak hvis dette forumet ikke er riktig inngang
- hva skjer i skjæringspunktet mellom to fora med overlappende mandat

## Relasjon til andre ressurser
Beskriv relevante koblinger til:
- gjenbrukbare løsninger
- standarder og veiledning
- andre samhandlingsarenaer og organiseringsressurser
- økonomiske og juridiske rammer og virkemidler

## Forretningsverdi og arkitekturverdi
Beskriv hvilken verdi forumet gir for:
- samordning
- forankring
- prioritering
- felles retning
- lavere risiko for dobbeltarbeid eller fragmentering

## Konsekvens ved manglende involvering eller svak forankring
Beskriv hva som typisk skjer hvis forumet ikke brukes når det burde vært involvert.

Aktuelle vinkler:
- svakere forankring
- lavere etterlevelse
- parallelle løp
- dårligere prioritering
- økt konflikt eller fragmentering

## Utfordringer og risiko
Bruk gjerne tabell med:
`Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering`

Aktuelle kategorier:
- forankring
- representasjon
- beslutningskraft
- kapasitet
- samspill med linje og forvaltning

## Publiseringsform og tilgjengelighet
Beskriv hvordan forumet er synlig og tilgjengelig.

For eksempel:
- mandat
- nettside
- referater
- invitasjons- eller medlemsbasert arena

## Støtter arkitekturprinsipper
Beskriv hvordan forumet støtter prinsippene i `arkitektur/prinsipper/principles.md`.

Vurder også om det finnes tydelige svakheter, spenninger eller begrensninger knyttet til viktige prinsipper som bør tas med i analyse ved mulig bruk eller involvering.

Aktuelle vinkler:
- prinsipper forumet styrker gjennom samordning eller forankring
- prinsipper forumet bare støtter indirekte eller ujevnt
- prinsipper som kan svekkes dersom forumet har svak representasjon, lav beslutningskraft eller uklar oppfølging
- hva dette betyr for vurdering av om forumet bør involveres i et konkret løp

## Lenke til dokumentasjon
Oppgi hovedlenker til mandat, omtalesider, referater eller andre åpne kilder.

## Kildegrunnlag brukt i utfyllingen
Oppgi konkrete URL-er og lokale filer, med hentedato der det er relevant.
