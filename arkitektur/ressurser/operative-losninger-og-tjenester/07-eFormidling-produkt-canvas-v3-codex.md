# Produkt-canvas: eFormidling

## Navn
eFormidling

## Ressurs ID
DIGDIR-007

## Status/Livsfase
**Produksjon** - etablert nasjonal fellesløsning for sikker meldingsutveksling mellom virksomheter og innbyggere.

**Fakta:** Den tekniske dokumentasjonen beskriver eFormidling som en løsning for innføring og bruk i offentlige virksomheter og hos deres leverandører. Samarbeidsportalen viser løpende statistikk, tilknyttede virksomheter og oppetidskrav for løsningen i 2025.

## Modenhet
**Høy funksjonell modenhet** - etablert løsning med tydelig bruksområde og forvaltningsspor:
- Produktet brukes til meldingsutveksling i offentlig sektor og har egen teknisk dokumentasjon, innføringsløp og statistikkvisning.
- Løsningen dekker flere meldingssammenhenger, blant annet kommunikasjon med offentlige virksomheter, innbyggere og virksomheter gjennom foretrukne kanaler.
- Dokumentasjonen viser et modent funksjonssett med meldingsflyt, dokumenttyper, sikkerhetsegenskaper og konkrete brukseksempler.

**Deduksjon:** Modenheten er høy for selve formidlingsmønsteret. Modenheten i hver enkelt brukskontekst vil variere med hvordan virksomhetene har tatt i bruk integrasjonspunkt, dokumenttyper og lokale fagsystemer.

## Kort beskrivelse
eFormidling er Digdirs fellesløsning for standardisert og sikker meldingsutveksling. Produktet gjør det mulig å sende og motta digitale meldinger uten å bygge egne punkt-til-punkt-integrasjoner for hver mottaker, og skjuler samtidig forskjeller mellom ulike mottakerkanaler. Løsningen er særlig relevant når offentlige virksomheter trenger pålitelig og sporbar utveksling av dokumenter og meldinger på tvers av organisatoriske grenser.

## Kapabiliteter
- **Datautveksling og integrasjon: Dele data med andre** gjør det mulig å sende digitale meldinger og dokumenter sikkert til andre virksomheter og mottakere gjennom et felles formidlingsmønster.
- **Datautveksling og integrasjon: Bruke data fra andre** gjør det mulig å motta innkommende meldinger i ønsket kanal og integrere dem videre i egne arbeidsprosesser og fagsystemer.
- **Datautveksling og integrasjon: Meldingsformidling** er selve kjernefunksjonen i produktet, fordi løsningen pakker, ruter og leverer meldinger mellom avsender og mottaker.
- **Samarbeid: Organisatorisk samhandling** støtter samhandling mellom virksomheter ved at samme løsning kan brukes på tvers av organisatoriske grenser og ulike mottakergrupper.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** ivaretar krav til sikker, sporbar og kontrollert meldingsutveksling.
- **Standardisering: Forvaltningsstandarder** bygger på standardiserte dokument- og meldingsmønstre, blant annet Peppol og AS4.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i Digdir Docs og Samarbeidsportalen.

## Produktmål
**Primærkilder:** Digdir Docs `Om eFormidling`, `Introduksjon`, `Egenskaper` og Samarbeidsportalen `Dette er eFormidling`.

Dokumenterte mål:
- Bidra til sikker, samordnet og effektiv meldingsutveksling.
- Gjøre det enkelt å kommunisere uten å ta hensyn til om mottakeren er en privat virksomhet, offentlig virksomhet eller innbygger.
- Dekke virksomhetenes behov for å sende og motta meldinger med de kravene de har til meldingsinnhold og funksjon.

Operative mål utledet fra de samme kildene:
- Redusere behovet for bilaterale integrasjoner mellom hver avsender og mottaker.
- Gjøre det mulig å nå mottakerens foretrukne kanal gjennom ett felles integrasjonsmønster.
- Støtte digitale arbeidsprosesser som krever sikker og sporbar meldingsutveksling.

## Brukerbehov
- Offentlige virksomheter trenger en felles måte å sende og motta digitale meldinger på uten å bygge unike koblinger mot hver mottaker.
- Integrasjonsteam trenger et teknisk mønster som kan kobles til lokale fagsystemer og sak-/arkivløsninger.
- Virksomheter trenger sikker overføring av dokumenter og meldinger der både sporbarhet og leveringsstatus er viktige.
- Leverandører trenger et forutsigbart innføringsmønster med dokumenterte dokumenttyper, prosesser og tekniske krav.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter som avsendere | Sende meldinger sikkert og standardisert | Utgående meldinger og dokumentflyt | Bruker løsningen som felles formidlingskanal |
| Offentlige virksomheter som mottakere | Motta meldinger i riktig kanal | Inngående dokumenter og prosessflyt | Trenger kontroll på kanal, status og mottak |
| Integrasjonsteam og systemleverandører | Koble fagsystemer til et standardmønster | Implementasjon, drift og vedlikehold | Teknisk dokumentasjon er sentral |
| Saksbehandlings- og forvaltningsmiljøer | Sporbar og pålitelig meldingsutveksling | Dokument- og meldingsbaserte arbeidsprosesser | Bruker verdien, men forvalter ikke nødvendigvis teknikken |
| Digdir som forvalter | Stabil drift og innføring i flere virksomheter | Forvaltning, dokumentasjon og videreutvikling | Synlig i både docs og Samarbeidsportalen |

## Hovedfunksjoner
### Primære funksjoner
- eFormidling sender meldinger til mottakerens foretrukne kanal. Det gjør løsningen relevant når avsender ikke skal trenge å håndtere ulike tekniske kanaler selv.
- eFormidling mottar innkommende meldinger på ønsket kanal. Produktet er derfor ikke bare en utgående transportmekanisme, men også en del av en standardisert mottaksmodell.
- eFormidling bruker et integrasjonspunkt og dokumenterte dokumenttyper og prosesser. Det gir et tydelig konseptuelt skille mellom fagsystemet som produserer innholdet og formidlingslaget som transporterer det.
- eFormidling støtter flere bruksscenarier, blant annet saksbehandling, taushetsbelagt saksbehandling, informasjon og vedtak til innbygger, samt meldingsutveksling mot eInnsyn og KS FIKS IO. Dette gjør løsningen bred innen meldingsutveksling, men fortsatt tydelig avgrenset til formidling fremfor saksbehandling.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Sikker og standardisert meldingsformidling | Saksbehandling i fagsystemene |
| Ruting til mottakerens foretrukne kanal | Langtidsarkivering av innhold |
| Mottak og levering av meldinger | Forretningslogikk i hver enkelt tjeneste |
| Dokumenterte prosesser, dokumenttyper og integrasjonsmønstre | Full erstatning for lokale sak-/arkiv- eller fagsystemer |
### Typiske brukssituasjoner (generisk)
- Offentlig virksomhet sender saksrelaterte meldinger til en annen offentlig virksomhet og trenger et felles formidlingsledd.
- Fagsystem trenger å sende og motta meldinger uten å håndtere kanalvalg og mottakeroppslag selv.
- Saksbehandlingsflyt krever digital kommunikasjon mellom etater med dokumentert levering.
- Virksomhet sender til eInnsyn som en del av journalføringen.

### Når eFormidling normalt ikke er førstevalg
- Når behovet er kommunikasjon med innbygger via postkasse – da er Digital postkasse mer relevant.
- Når behovet er interaktiv dialog med innbygger – da er Altinn Melding og Dialogporten mer relevant.
- Når behovet er stor filoverføring mellom systemer – da er Altinn Formidling mer relevant.
- Når behovet er hendelsesdrevet varsling uten meldingsinnhold – da er Altinn Events mer relevant.

## Veikart over kommende funksjonalitet
**Fakta:** Samarbeidsportalen viser statistikk, oppetid og kundetall, men jeg fant ikke en offentlig tidsfestet utviklingsplan i kildene brukt i denne arbeidsøkten.

**Ikke offentlig verifisert i denne arbeidsøkten:** Konkrete roadmap-punkter, prioriterte nye meldingstyper eller planlagt funksjonsutvidelse.

**Deduksjon:** Videreutviklingen vil sannsynligvis dreie seg om flere støttede prosesser, enklere innføring og videre forbedring av drift, men dette må bekreftes i egne veikartkilder.

## Forretningsverdi/Verdiforslag
### For virksomheter
- Reduserer behovet for mange bilaterale integrasjoner.
- Gjør meldingsutveksling mer forutsigbar gjennom ett felles teknisk mønster.

### For utviklings- og integrasjonsmiljøer
- Gir én dokumentert modell for flere typer meldingsutveksling.
- Reduserer kompleksitet ved å skille formidling fra lokal forretningslogikk.

### For offentlig sektor og samfunn
- Støtter mer effektiv digital samhandling mellom virksomheter og mot innbyggere.
- Legger til rette for gjenbruk av standarder og felles infrastruktur i stedet for lokale spesialløsninger.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Meldinger kan inneholde sensitivt eller taushetsbelagt innhold | Tydelige prosesskrav, riktig kanalvalg og styrt bruk av dokumenttyper |
| Teknisk | Lokale integrasjoner og mottakssystemer kan gi ulik faktisk kvalitet i bruk | God innføringsstøtte, testløp og tydelig teknisk dokumentasjon |
| Sikkerhet | Feil konfigurasjon kan gi feil leveringskanal eller utilstrekkelig beskyttelse | Standardiserte sikkerhetsmekanismer, overvåking og kontroll av meldingsflyt |
| Leverandør/forvaltning | Virksomheter blir avhengige av felles formidlingsmønster og sentral forvaltning | Tydelig forvaltningsmodell, dokumentasjon og stabil drift |
| Brukeropplevelse | Gevinsten kan utebli hvis meldingsflyten ikke er godt integrert i lokale arbeidsprosesser | Bedre innføring, eksempler og tilpasning til faktiske bruksscenarier |

## Kanaler
- Digdir om eFormidling: https://www.digdir.no/eformidling/om-eformidling/2182
- Teknisk dokumentasjon: https://docs.digdir.no/docs/eFormidling/
- Introduksjon: https://docs.digdir.no/docs/eFormidling/Introduksjon/
- Egenskaper: https://docs.digdir.no/docs/eFormidling/Egenskaper/
- Samarbeidsportalen: https://samarbeid.digdir.no/eformidling/dette-er-eformidling/46
- Statistikk: https://samarbeid.digdir.no/eformidling/statistikk-eformidling/3425

## Plattform
eFormidling er en formidlingstjeneste med et tydelig teknisk skille mellom virksomhetens egne systemer og den nasjonale meldingsinfrastrukturen.

**Fakta:**
- Dokumentasjonen beskriver et integrasjonspunkt og standardiserte dokumenttyper, prosesser og meldingsmønstre.
- Løsningen kan rute meldinger til mottakerens foretrukne kanal.
- eFormidling støtter flere meldingssammenhenger, inkludert meldingsutveksling mot offentlige virksomheter, innbyggere og KS FIKS IO.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur, konkret hostingoppsett og detaljert intern plattformbeskrivelse.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme formidlingsmønster kan brukes av mange virksomheter og prosesser.
- Standardene og dokumenttypene gjør det lettere å koble nye bruksscenarier til samme grunnløsning.
- Produktet reduserer behovet for å bygge egne meldingsløyper for hver samhandlingsrelasjon.


### Vanlige kombinasjoner med andre produkter
- **eInnsyn** – eFormidling brukes for å sende journalposter og dokumenter til eInnsyn.
- **FIKS SvarUt/SvarInn** – mange kommuner og statlige virksomheter bruker disse i samme meldingsflyt, med eFormidling på statssiden.
- **Digital postkasse** – eFormidling kan formidle post til innbyggers digitale postkasse som del av avsenderens kanalvalg.
- **Kontakt- og reservasjonsregisteret** – brukes for å avklare om mottakeren kan nås digitalt.

**Kildekode:** Åpen kildekode. Lisens: MIT/EUPL. Kildekode: [github.com/felleslosninger/efm-integrasjonspunkt](https://github.com/felleslosninger/efm-integrasjonspunkt).

## Støtter arkitekturprinsipper
- **P5 Del og gjenbruk løsninger** - eFormidling er en felles formidlingstjeneste som kan brukes av mange virksomheter.
- **P6 Lag digitale løsninger som støtter samhandling** - produktet er direkte laget for samhandling gjennom meldingsutveksling.
- **P7 Sørg for tillit til oppgaveløsningen** - sikker og sporbar meldingsflyt er en sentral del av produktets verdi.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Jeg fant ikke en presis offentlig beskrivelse av finansieringsmodell eller budsjettansvar i denne arbeidsøkten.
- **Deduksjon:** Produktet framstår som en forvaltet nasjonal Digdir-løsning, men finansieringsmodellen må bekreftes i egne forvaltnings- eller budsjettkilder.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Digdir Docs og Digdir-sider om eFormidling |
| Driftsansvar | Digdir forvalter løsningen, men konkret driftsmodell er ikke offentlig spesifisert i brukte kilder | Docs og Samarbeidsportalen |
| Budsjettansvar | Ikke offentlig spesifisert i brukte kilder | Ikke verifisert i denne arbeidsøkten |
| Styringsmodell | Forvaltet som nasjonal fellesløsning med teknisk dokumentasjon, innføring og statistikkspor | Digdir Docs og Samarbeidsportalen |

## Lenke til dokumentasjon
- https://www.digdir.no/eformidling/om-eformidling/2182
- https://docs.digdir.no/docs/eFormidling/
- https://docs.digdir.no/docs/eFormidling/Introduksjon/
- https://docs.digdir.no/docs/eFormidling/Egenskaper/
- https://samarbeid.digdir.no/eformidling/dette-er-eformidling/46
- https://samarbeid.digdir.no/eformidling/statistikk-eformidling/3425

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/07-eFormidling-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.digdir.no/eformidling/om-eformidling/2182 (hentet 2026-03-18)
- Nettkilde: https://docs.digdir.no/docs/eFormidling/ (hentet 2026-03-18)
- Nettkilde: https://docs.digdir.no/docs/eFormidling/Introduksjon/ (hentet 2026-03-18)
- Nettkilde: https://docs.digdir.no/docs/eFormidling/Egenskaper/ (hentet 2026-03-18)
- Nettkilde: https://samarbeid.digdir.no/eformidling/dette-er-eformidling/46 (hentet 2026-03-18)
- Nettkilde: https://samarbeid.digdir.no/eformidling/statistikk-eformidling/3425 (hentet 2026-03-18)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Vurderingen bygger videre på `07-eFormidling-produkt-canvas-v2-copilot.md`, men er kontrollert mot oppdaterte offisielle kilder fra Digdir Docs og Samarbeidsportalen.
- Kapabilitetene er strammet inn til direkte og sterke koblinger som nå er synkronisert med produktregisteret og masterfila for produkt-kapabilitet-koblinger.
- Funksjonsbeskrivelsen er ryddet til et tydeligere konseptnivå, slik at eFormidling lettere kan skilles fra andre formidlings- og meldingsløsninger.

### Tekstlige forbedringer
- Norsk tegnsett og språk er ryddet opp.
- Hovedteksten er skrevet om til en selvstendig produktbeskrivelse for målgruppen.
- Risiko, scope og brukersegmenter er gjort tydeligere og mer sammenlignbare.


