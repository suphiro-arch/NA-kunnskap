# Produkt-canvas: Kjernejournal

## Navn
Kjernejournal

## Ressurs ID
NHN-003

## Status/Livsfase
**Produksjon** - etablert nasjonal fellesløsning for deling av utvalgte helseopplysninger på tvers av behandlingssteder.

**Fakta:** Den gjeldende ressursbeskrivelsen og repoets tilhørende helsefiler beskriver Kjernejournal som en nasjonal løsning som gir helsepersonell tilgang til sentrale og relevante helseopplysninger når behandlingssituasjonen krever det.

## Modenhet
**Høy modenhet** - innarbeidet samhandlingsløsning med tydelig rolle i nasjonal informasjonsdeling i helsesektoren.

**Deduksjon:** Modenheten er høy som nasjonal løsning, men verdien i praksis avhenger av at kildesystemer, tilgangsstyring og lokale arbeidsprosesser fungerer sammen med løsningen.

## Kort beskrivelse
Kjernejournal er den nasjonale fellesløsningen for å gjøre utvalgte og viktige helseopplysninger tilgjengelige på tvers av behandlingssteder. Løsningen gir helsepersonell en felles oppslagsflate for informasjon som ellers blir fragmentert mellom virksomheter, journalløsninger og behandlingsnivåer. Tilgangen er avgrenset til helsepersonell med tjenstlig behov, med roller fastsatt av Helsedirektoratet, som også er dataansvarlig.

Alle oppslag dokumenteres i en bruksslogg som pasienten selv kan se på `Helsenorge`. Retten til innsyn i egne opplysninger og i hvem som har gjort oppslag følger av kjernejournalforskriften § 6. Pasienten kan i tillegg reservere seg mot løsningen, sperre den helt, eller blokkere utvalgte deler eller utvalgte helsepersonell.

Kjernejournal skal ikke forstås som en fullverdig erstatning for pasientjournal i den enkelte virksomhet. Den er snarere et nasjonalt delings- og oppslagsspor for opplysninger som må kunne brukes på tvers når kontinuitet, pasientsikkerhet og rask tilgang er viktigere enn lokal journaldybde.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot NHNs tjenestebeskrivelse og Helsenorges beskrivelse av kjernejournal. De tre første koblingene er beholdt fra `v2`. De to tillitskoblingene er lagt til etter kildesjekk av personvern- og loggfunksjonene. Innbyggeren forvalter selv sperring, blokkering og reservasjon på `Helsenorge`; Kjernejournal er stedet disse valgene håndheves og hvert oppslag loggføres.

- **Datautveksling og integrasjon: Bruke data fra andre** gjør det mulig å sammenstille og bruke relevante helseopplysninger fra flere kilder i én behandlingssituasjon.
- **Datautveksling og integrasjon: Dele data med andre** gjør utvalgte opplysninger tilgjengelige for andre behandlingssteder som trenger dem for å yte helsehjelp.
- **Samarbeid: Organisatorisk samhandling** støtter samhandling mellom helsevirksomheter som ellers ville vært avhengige av mer fragmentert informasjonsdeling.
- **Tillit: Sporbarhet og innsyn** dokumenterer hvert oppslag i en bruksslogg som pasienten har rett til å se etter kjernejournalforskriften § 6, slik at bruken av opplysningene kan etterprøves.
- **Tillit: Tilgangskontroll** håndhever ved hvert oppslag at bare helsepersonell med tjenstlig behov får tilgang, og at pasientens sperring eller blokkering av bestemte deler eller bestemte personer respekteres.

## Produktmål
Dokumenterte og tydelig utledbare mål for ressursen er å:
- gi helsepersonell rask tilgang til sentrale opplysninger når pasienten mottar helsehjelp et annet sted enn der informasjonen opprinnelig ble registrert
- redusere risikoen for informasjonsbrudd i behandlingsforløp som går på tvers av virksomheter og nivåer
- styrke pasientsikkerhet og bedre beslutningsgrunnlag i situasjoner der tid og helhetsoverblikk er viktig
- støtte en mer sammenhengende nasjonal informasjonsdeling uten å erstatte lokale journalløsninger

## Brukerbehov
- Helsepersonell trenger rask tilgang til pålitelig og relevant informasjon når pasienten behandles utenfor egen virksomhet.
- Helsevirksomheter trenger et nasjonalt delingsspor som reduserer behovet for punkt-til-punkt-oppslag og manuell informasjonsinnhenting.
- Pasienter trenger tryggere og mer sammenhengende behandling, særlig når de møter flere behandlingssteder i samme forløp.
- Forvaltnings- og integrasjonsmiljøer trenger en felles løsning som kan brukes sammen med andre helsetjenester og nasjonale felleskomponenter.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Helsepersonell | Rask tilgang til relevante helseopplysninger | Behandling, oppfølging og vurdering i ulike behandlingssituasjoner | Primærbrukere av løsningen |
| Helsevirksomheter | Bedre samhandling om informasjon på tvers av virksomheter | Akuttforløp, planlagte forløp og samhandling mellom nivåer | Avhengige av gode integrasjoner og tilgangsstyring |
| Pasienter | Tryggere og mer sammenhengende helsehjelp | Indirekte nytte, og i noen sammenhenger innsyn via tilknyttede tjenester | Sluttbrukerperspektivet er viktig selv om pasienten ikke er hovedoperatørbruker |
| Forvaltnings- og integrasjonsmiljøer | Stabil drift, tilgangskontroll og samspill med andre sektorløsninger | Innføring, videreutvikling og drift | Må forstå både tekniske og juridiske avgrensninger |

## Hovedfunksjoner
### Primære funksjoner
**Nasjonal oppslagsflate for utvalgte helseopplysninger.** Kjernejournal gjør det mulig å hente fram relevante helseopplysninger i behandlingssituasjoner der helsepersonell trenger raskt overblikk på tvers av virksomhetsgrenser. Det er denne oppslagsfunksjonen som skiller løsningen fra lokale journalsystemer: den skal gi tilgang til utvalgt, delt informasjon når pasienten beveger seg mellom behandlingssteder.

**Deling på tvers av behandlingssteder uten å erstatte lokal journal.** Løsningen støtter samhandling ved å gjøre bestemte opplysninger tilgjengelige der de trengs, men den er ikke ment å romme hele den kliniske dokumentasjonen eller alle arbeidsprosessene i et pasientjournalsystem. Dette gjør Kjernejournal særlig relevant som nasjonal samhandlingsløsning, ikke som komplett arbeidsflate for all journalføring.

**Støtte for mer sammenhengende behandlingsforløp.** Verdien oppstår når pasienten mottar helsehjelp fra flere virksomheter, og informasjon ellers risikerer å bli spredt, forsinket eller utilgjengelig. Kjernejournal bidrar derfor både til bedre beslutningsgrunnlag og til at flere aktører kan handle på et mer felles informasjonsbilde.

**Håndheving av pasientens personvernvalg og logging av oppslag.** Reservasjon, sperring og blokkering settes av pasienten på `Helsenorge`, men det er Kjernejournal som håndhever dem i selve oppslagssituasjonen. Samtidig loggføres hvert oppslag, og loggen gjøres tilgjengelig for pasienten. Dette gjør personvernvalgene etterprøvbare i praksis og ikke bare en innstilling i en portal.

**Samspill med andre helseressurser og brukerflater.** Kjernejournal må også forstås i sammenheng med andre nasjonale helseressurser som `HelseID`, `Helsenorge` og `e-resept`. Det er dette samspillet som gjør løsningen nyttig i praksis: tilgang, innsyn, behandlingsprosesser og tilgrensende informasjonsløp henger sammen selv om ressursene har ulike roller.

### Typiske brukssituasjoner (generisk)
- Når helsepersonell trenger rask tilgang til sentrale opplysninger om en pasient som behandles utenfor egen virksomhet eller utenfor ordinært kjent behandlingsforløp.
- Når et behandlingsforløp går på tvers av nivåer eller organisasjoner, og manglende informasjonsdeling kan gi dårligere beslutningsgrunnlag eller høyere pasientsikkerhetsrisiko.
- Når en nasjonal oppslagsløsning er mer hensiktsmessig enn å forsøke å hente samme informasjon manuelt fra mange ulike journalsystemer.

### Når Kjernejournal normalt ikke er førstevalg
- Når behovet er full klinisk dokumentasjon, lokal arbeidsflyt eller detaljert journalføring. Da er lokale EPJ-løsninger og tilgrensende fagsystemer riktigere primærverktøy.
- Når oppgaven primært handler om innbyggerflate eller generell pasientdialog. Da er `Helsenorge` normalt en mer relevant førsteflate.
- Når behovet gjelder identitets- og tilgangsstyring snarere enn selve helseopplysningene. Da er `HelseID` eller lokale tilgangsløsninger mer direkte relevante.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonal deling og oppslag av utvalgte helseopplysninger | Full pasientjournal og komplett klinisk arbeidsflate |
| Samhandlingsstøtte mellom behandlingssteder | Lokal journalføring, oppgavehåndtering og intern arbeidslogikk i hvert system |
| Tilgang til relevant informasjon når helsehjelp ytes på tvers | Generell innbyggerdialog eller bred selvbetjeningsflate |
| Samspill med andre nasjonale helseløsninger | Erstatning for alle kildesystemer som produserer eller forvalter informasjonen |
| Håndheving av sperring og blokkering, og logg over oppslag | Innbyggerflaten der de samme valgene settes og loggen leses |

## Veikart over kommende funksjonalitet
**Fakta:** Dagens lokale kildespor bekrefter at Kjernejournal er en etablert løsning i bruk, men gir ikke et detaljert og samlet offentlig veikart i denne arbeidsøkten.

**Ikke offentlig verifisert i denne arbeidsøkten:** Tidsfestede leveranser, planlagt funksjonsutvidelse og prioriterte utviklingsspor er ikke rekontrollert direkte nå.

**Deduksjon:** Videreutviklingen vil sannsynligvis dreie seg om bedre samspill med andre nasjonale helseløsninger, mer presis tilgangsstyring og videre forbedring av hvilke opplysninger som er mest nyttige i tverrgående behandlingssituasjoner.

## Forretningsverdi/Verdiforslag
### For helsepersonell og helsevirksomheter
- Gir raskere tilgang til viktig informasjon i situasjoner der tid og helhetsoverblikk betyr mye.
- Reduserer behovet for manuell innhenting fra flere behandlingssteder når pasienten beveger seg i sektoren.
- Styrker muligheten for mer sammenhengende behandling og bedre samhandling mellom virksomheter.

### For pasienter
- Reduserer risikoen for at viktig informasjon ikke er tilgjengelig når pasienten trenger helsehjelp et nytt sted.
- Støtter tryggere og mer forutsigbar behandling på tvers av nivåer og virksomheter.
- Kan bidra til bedre opplevd sammenheng i helsetjenesten, særlig når flere aktører er involvert i samme forløp.

### For sektoren som helhet
- Gir en felles nasjonal løsning for et informasjonsbehov som ellers lett blir løst fragmentert.
- Reduserer behovet for mange punkt-til-punkt-løp for samme type informasjonsdeling.
- Understøtter nasjonal samhandling uten å presse alle virksomheter inn i samme journalsystem.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Personvern og tilgang | For bred tilgang eller feil bruk av opplysninger kan gi alvorlige personvernkonsekvenser | Tydelig tilgangsstyring, sporbarhet, opplæring og kontroll |
| Datakvalitet | Opplysninger kan være utdaterte, mangelfulle eller misforstås uten riktig kontekst | Klare kildereferanser, gode oppdateringsrutiner og tydelig ansvar for kildesystemene |
| Arbeidsprosess | Helsepersonell kan forvente at løsningen dekker mer enn den faktisk gjør | Tydelig avgrensning mot EPJ og andre sektorløsninger, samt opplæring i riktig bruk |
| Integrasjon og avhengigheter | Nytten svekkes hvis samspillet med kildesystemer, tilgangsløsninger eller andre fellestjenester er svakt | Robust integrasjon, forvaltningsoppfølging og tydelig ansvarslinje |
| Samhandling og styring | Ulik lokal modenhet kan gjøre nasjonal bruk ujevn | Videreutvikle innføringsstøtte, samordning og forventningsstyring |

## Kanaler
- Norsk helsenett: https://www.nhn.no/tjenester/kjernejournal/om-tjenesten
- Helsenorge: https://www.helsenorge.no/helseopplysninger-som-deles/kjernejournal/
- Norsk helsenett - spørsmål og svar: https://www.nhn.no/tjenester/kjernejournal/sporsmal-og-svar

## Plattform
Kjernejournal er en nasjonal delings- og oppslagsløsning i helsesektoren. Plattformverdien ligger i at flere virksomheter kan bruke samme nasjonale informasjonsløp for utvalgte opplysninger, selv om de fortsatt har egne journalsystemer og arbeidsflater.

## Gjenbruk
**Middels til høy gjenbruksverdi:**
- Høy verdi i helsesektoren der behovet er tverrgående tilgang til utvalgte helseopplysninger.
- Lavere verdi utenfor sektoren, fordi løsningen er tett knyttet til helsefaglige behov, sensitiv informasjon og sektorens egne samhandlingskrav.

### Vanlige kombinasjoner med andre produkter
- `Helsenorge`
- `HelseID`
- `e-resept`

**Kildekode:** Ikke offentlig dokumentert.

**Lisens:** Ikke offentlig dokumentert.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** styrkes ved at relevante opplysninger kan brukes der behovet oppstår i stedet for å gjenskapes manuelt flere steder.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi Kjernejournal er laget nettopp for behandlingssituasjoner som går på tvers av virksomheter og nivåer.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi løsningen må kombinere høy tilgjengelighet for riktig helsepersonell med strenge krav til personvern og kontroll.

Vurdering av svakheter og spenninger:
- Løsningen må balansere rask tilgang mot strenge krav til tilgangsstyring og dataminimering. Denne spenningen er en del av selve verdiforslaget, ikke bare en randrisiko.
- Kjernejournal kan også gi falsk trygghet hvis brukerne tror løsningen alltid gir et fullstendig bilde. Tydelig avgrensning mot lokale journalsystemer er derfor prinsippmessig viktig.

## Finansiering
**Fakta:** En samlet og detaljert offentlig finansieringsmodell er ikke dokumentert i de lokale kildene som er brukt i denne økten.

**Deduksjon:** Kjernejournal framstår som en nasjonal fellestjeneste i helsesektoren, der kostnader til drift og videreutvikling må bæres gjennom sektorens felles styrings- og finansieringsmekanismer snarere enn som en ren lokal tjeneste.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Norsk helsenett | Gjeldende ressursbeskrivelse og lenkegrunnlag i repoet |
| Driftsansvar | Norsk helsenett | Gjeldende ressursbeskrivelse og lenkegrunnlag i repoet |
| Budsjett- og kostnadsmodell | Ikke samlet offentlig dokumentert i denne økten | Ikke bekreftet lokalt |
| Styringskontekst | Del av nasjonale fellesløsninger i helsesektoren | Utledet fra rollen som tverrgående nasjonal løsning |

## Lenke til dokumentasjon
- https://www.nhn.no/tjenester/kjernejournal/om-tjenesten
- https://www.helsenorge.no/helseopplysninger-som-deles/kjernejournal/
- https://www.nhn.no/tjenester/kjernejournal/sporsmal-og-svar

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/operative-ressurs-canvas.system.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/32-Helsenorge-produkt-canvas-v1-codex.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/33-HelseID-produkt-canvas-v1-codex.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/135-Norsk-pasientregister-produkt-canvas-v1-codex.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.nhn.no/tjenester/kjernejournal/om-tjenesten (kontrollert 2026-09-14)
- Nettkilde: https://www.helsenorge.no/helseopplysninger-som-deles/kjernejournal/ (kontrollert 2026-09-14)
- Nettkilde: https://www.nhn.no/tjenester/kjernejournal/sporsmal-og-svar (kontrollert 2026-09-14)

## Endringer fra forrige versjon

### Analyseforbedringer
- `Tillit: Sporbarhet og innsyn` og `Tillit: Tilgangskontroll` er lagt til etter kildesjekk. `v2` beskrev verken bruksloggen, pasientens innsynsrett etter kjernejournalforskriften § 6, eller sperring og blokkering, selv om dette er sentrale egenskaper ved løsningen.
- Arbeidsdelingen mot `Helsenorge` er gjort eksplisitt: personvernvalgene settes i portalen, men håndheves og loggføres her. Det er grunnen til at tillitskoblingene hører hjemme i denne fila og ikke bare i innbyggerflaten.
- `Kort beskrivelse` slår nå fast at Helsedirektoratet er dataansvarlig og fastsetter hvilke roller som har tilgang, som er en forutsetning for å forstå tilgangsmodellen.
- `Hovedfunksjoner` og `Scope og avgrensning` skiller nå håndheving og logging fra flaten der valgene settes.

### Tekstlige forbedringer
- Formuleringen `Ressursen er viktig fordi` er fjernet fra `Kort beskrivelse`. AGENTS.md krever at beskrivelsen sier hva ressursen gjør i sitt eget domene, ikke hvorfor den er interessant.
- `Grunnlag`-teksten i `Kapabiliteter` er flyttet foran kulelista, slik AGENTS.md krever, så den ikke trekkes inn i forklaringen for siste kapabilitet ved metadatasynk.
- Kildegrunnlaget er oppdatert fra `ikke rekontrollert` til faktisk kontrollert 2026-09-14, og utvidet med NHNs side med spørsmål og svar.
