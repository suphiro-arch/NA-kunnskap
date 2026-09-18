# Altinn.no

## Navn
Altinn.no

Portalen omtales også som `Altinn informasjonsportal` i Altinns egen innholdsstrategi. Registeret brukte tidligere navnet `Altinn Portal`, som ble endret i `v4` fordi det dekket et bredere produkt enn det som står igjen etter at innboks og tilgangsstyring ble skilt ut.

## Ressurs ID
DIGDIR-019

## Status/Livsfase
**Produksjon** - etablert nasjonal inngangsportal, med et scope som er smalere etter at Altinn II ble avviklet.

**Fakta:** Altinn II ble avviklet 19. juni 2026, og den parallelle driften av gammel og ny brukerflate er over. Portalen er dermed ute av overgangsfasen som preget `v3`.

**Fakta:** Innboks og tilgangsstyring er egne flater som portalen lenker videre til. Startsiden på `info.altinn.no` har `Sjekk innboks` og `Tilgangsstyring` som innganger, og de peker til `af.altinn.no` og `am.ui.altinn.no`. Altinn oppgir selv at neste generasjon av altinn.no utvikles av flere produktteam, blant dem Team Portal, Team Arbeidsflate og Team Authorization.

## Modenhet
**Høy modenhet** - innarbeidet nasjonal portal med stabil rolle og åpen kildekode.

- Portalen er en veletablert og godt kjent inngang til offentlige skjema og tjenester for både privatpersoner og næringsliv.
- Kildekoden er publisert under MIT-lisens i `Altinn/info.altinn.no`, med Astro i frontend og Umbraco som publiseringsløsning.
- Overgangsrisikoen fra `v3` er borte: gammel løsning er avviklet, og portalens ansvarsområde er avklart mot de andre Altinn-produktene.

**Deduksjon:** Det svakeste leddet er ikke lenger teknisk, men rollemessig. Portalen er inngangen til flater som forvaltes av andre produktteam, og brukeropplevelsen avhenger derfor av at overgangene mellom `info.altinn.no`, `af.altinn.no` og `am.ui.altinn.no` oppleves som én tjeneste. Det er et koordineringsansvar mer enn et utviklingsansvar.

## Kort beskrivelse
Altinn.no er den offentlige inngangsportalen til Altinn. Portalen gjør det mulig å finne fram til skjema, tjenester og offentlig informasjon på tvers av etater, gir veiledning om hva brukeren må gjøre, og er stedet brukeren starter innloggingen fra.

Portalen er den åpne, uinnloggede delen av Altinn. Etter innlogging tar andre produkter over: innboksen og dialogoversikten i Arbeidsflate, og administrasjon av fullmakter og tilganger i brukerflaten til Altinn Autorisasjon. Denne arbeidsdelingen er sentral for å forstå hva produktet er i dag, og er en endring fra `v3`, der innboks og tilgangsstyring ble beskrevet som deler av portalen.

Portalen er samtidig mer enn en lenkesamling. Den forvalter og publiserer oversikten over skjema og tjenester fra mange offentlige virksomheter, driver et hjelpesenter, og samler veiledning rettet mot dem som skal starte eller drive virksomhet. Det er dette redaksjonelle og katalogmessige arbeidet som er portalens egen leveranse.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over tjenester**
  Portalen registrerer, kvalitetssikrer og publiserer oversikten over skjema og tjenester fra mange offentlige virksomheter, med søk som dekker både tjenester og tilhørende informasjon. Uten portalen ville denne oversikten ikke finnes samlet for Altinn-tjenestene.

- **Sluttbrukertjenester: Sammenhengende tjenester**
  Portalen gir én inngang til offentlige tjenester på tvers av etatsgrenser, og skjuler hvilken virksomhet som står bak den enkelte tjenesten. Bidraget ligger i å finne fram og komme i gang, ikke i å følge en sak gjennom flere virksomheter.

## Produktmål
Dokumenterte mål:
- Gjøre det enklere for brukere å finne skjema, tjenester og offentlig informasjon fra det offentlige.
- Gi en enklere, tryggere og mer moderne inngang til Altinn.
- Samle veiledning for næringsdrivende på ett sted, slik at brukeren slipper å lete på tvers av etater.

Operative mål utledet fra kildene:
- Være et stabilt utgangspunkt for innlogging og videre navigasjon til Arbeidsflate og til tilgangsstyringen.
- Holde tjenesteoversikten oppdatert etter hvert som tjenesteeiere flytter tjenester inn i Altinn 3.
- Sørge for at overgangene mellom portalens flater oppleves som én sammenhengende tjeneste, selv om de utvikles av ulike produktteam.

## Brukerbehov
- Privatpersoner trenger ett sted å finne ut hvilken offentlig tjeneste som gjelder deres situasjon, og hvordan de kommer i gang.
- Næringsdrivende trenger samlet veiledning om hva som kreves for å starte og drive virksomhet, på tvers av etatene som stiller kravene.
- Brukere som allerede vet hva de skal, trenger en rask og forutsigbar vei til innlogging, innboks og tilgangsstyring.
- Tjenesteeiere trenger at tjenestene deres er synlige og mulige å finne i en nasjonal kanal med høy trafikk.
- Support- og veiledningsmiljøer trenger et hjelpesenter de kan vise til, framfor å svare på det samme gjentatte ganger.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Privatpersoner | Finne riktig tjeneste og forstå hva som kreves | Søk, tjenesteoversikt, hjelpesenter og innlogging | Primærbrukere av den uinnloggede flaten |
| Næringsdrivende og virksomheter | Samlet veiledning om å starte og drive virksomhet | Veiledningssidene og inngangen til skjema og innsending | Eget, uttalt målgruppespor på startsiden |
| Tjenesteeiere | Bli funnet av riktige brukere | Publisering og vedlikehold av tjenestebeskrivelser | Portalens distribusjonsverdi er høy fordi den er felles |
| Support- og veiledningsmiljøer | Vise til felles, oppdatert forklaring | Hjelpesenter og nyheter | Reduserer behovet for lokal veiledning om Altinn |
| Profesjonelle brukere og fullmektige | Komme raskt videre til riktig innlogget flate | Inngang til Arbeidsflate og til tilgangsstyringen | Selve arbeidet skjer i de innloggede flatene, ikke i portalen |

## Hovedfunksjoner
Portalens bærende funksjon er søk og tjenesteoversikt. Brukeren kan søke etter skjema, tjenester og offentlig informasjon på tvers av virksomheter, og finner tjenester fra blant andre Brønnøysundregistrene, Helsedirektoratet og Landbruksdirektoratet i samme oversikt. Dette forutsetter et løpende redaksjonelt arbeid med å registrere, beskrive og vedlikeholde tjenestene, ikke bare en teknisk søkefunksjon.

Portalen er også veiledningsflate. Området `Starte og drive bedrift` dekker oppstart, drift og avvikling med samlet informasjon om hva som kreves på tvers av etatene som stiller kravene, og innholdsstrategien legger dit også statlige støtteordninger og virkemidler. I tillegg driftes et hjelpesenter for spørsmål om bruk av Altinn, og en nyhetsflate som forklarer endringer i løsningen. Portalen har i tillegg en formell rolle som nasjonalt kontaktpunkt for EU-direktiver, noe som binder den til krav utenfor Altinn-porteføljen.

Den tredje funksjonen er navigasjon videre. Startsiden har `Sjekk innboks` og `Tilgangsstyring` som tydelige innganger, men begge lenker videre til egne flater: innboksen ligger i Arbeidsflate på `af.altinn.no`, og fullmakter og tilganger administreres i brukerflaten til Altinn Autorisasjon på `am.ui.altinn.no`. Portalen eier inngangen og sammenhengen, ikke funksjonaliteten på den andre siden.

Det fjerde er selve inngangen til innlogging. Portalen er der brukeren starter autentiseringen som gir tilgang til de innloggede flatene. Autentiseringen utføres av ID-porten, og portalen er startpunktet, ikke kontrollpunktet.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Åpen inngangsportal med søk etter skjema, tjenester og offentlig informasjon | Innboks, dialogoversikt og arkiv, som ligger i Arbeidsflate |
| Forvaltning og publisering av tjenesteoversikten | Administrasjon av fullmakter, tilgangspakker og klientforhold, som ligger i Altinn Autorisasjon |
| Veiledning for næringsdrivende og hjelpesenter | Innlogging og identitetsverifisering, som ligger i ID-porten |
| Nyheter og endringsinformasjon om Altinn | Faglogikken i den enkelte tjenesten eller etaten |
| Inngang til innlogging og videre navigasjon til de innloggede flatene | Utforming og kjøring av skjema og tjenester, som ligger i Altinn Studio og Altinn Apps |

Avgrensningen mot Norge.no er dokumentert, ikke bare praktisk. Altinns innholdsstrategi for informasjonsportalen slår fast at Norge.no er primæradressen for informasjon til privatpersoner om overordnede emner, mens Altinn.no retter seg mot virksomheter og bare dekker privatpersoninformasjon for tjenester som er realisert i Altinn. Strategien sier også at portalen skal peke videre til andre kilder framfor å gjenta innholdet deres, nettopp for å unngå duplisering. Digdir uttrykker den næringsrettede siden av arbeidsdelingen slik: `Altinn.no er hovudkanal frå offentleg forvaltning for overordna informasjon om rettar og plikter for etablerarar og næringsdrivande`.

Det som ikke er avklart i kildene, er hvor grensen går i praksis for privatpersoner. Begge portalene publiserer tjenesteoversikter for innbyggere, og en Altinn-tjeneste rettet mot privatpersoner hører etter strategien hjemme begge steder: på Altinn.no fordi den er realisert i Altinn, og på Norge.no fordi den er en offentlig tjeneste for innbyggere. Kildene beskriver heller ikke hvem som avgjør enkelttilfellene, eller hvordan de to redaksjonene samordner seg. Innholdsstrategien peker i tillegg på at Altinn og Norge.no i framtiden kan slås sammen til én nasjonal portal etter prinsippet om én inngang, uten at det er oppgitt beslutning, tidspunkt eller mandat for et slikt arbeid.

### Typiske brukssituasjoner (generisk)
- En bruker vet hva som skal gjøres, men ikke hvilken tjeneste eller hvilket skjema som gjelder.
- En som skal starte virksomhet, trenger samlet oversikt over kravene før noe sendes inn.
- En tjenesteeier vil at tjenesten skal være synlig og mulig å finne i en nasjonal kanal.
- En bruker trenger en kjent og forutsigbar inngang til innlogging, innboks og tilgangsstyring.

### Når Altinn.no normalt ikke er førstevalg
- Når behovet gjelder innboks, dialogoversikt eller arkiv. Da er Arbeidsflate riktig produkt.
- Når behovet gjelder fullmakter, tilgangspakker eller representasjon. Da er Altinn Autorisasjon riktig produkt.
- Når behovet er informasjon til privatpersoner om overordnede emner. Innholdsstrategien legger dette til Norge.no, og Altinn.no dekker privatpersoner bare for tjenester som er realisert i Altinn.
- Når behovet er ren maskinell integrasjon uten brukergrensesnitt.
- Når en sektorspesifikk portal med egne arbeidsprosesser er nødvendig, og brukeren aldri skal innom Altinn selv.

## Veikart over kommende funksjonalitet
**Fakta:** Altinn oppgir at neste generasjon av altinn.no utvikles av flere produktteam i fellesskap, med et uttalt mål om en sammenhengende opplevelse for sluttbrukeren på tvers av flatene. Team Portal, Team Arbeidsflate og Team Authorization er navngitt.

**Fakta:** Milepælene som preget `v3` er gjennomført: ny innboks, ny profil og nye sider for tilgangsstyring kom som førstevalg 1. desember 2025, nye fullmakts- og tilgangsfunksjoner i mars 2026, og Altinn II ble avviklet 19. juni 2026.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Et eget, tidfestet veikart for portalen som produkt er ikke funnet. Veikartene som er publisert, gjelder de tilstøtende produktene.

## Forretningsverdi/Verdiforslag
### For brukere
Portalen reduserer letetiden. En bruker som ikke vet hvilken etat som eier problemet, kan likevel finne fram til riktig tjeneste, og får forklart hva som kreves før noe sendes inn. For næringsdrivende er den samlede veiledningen særlig verdifull, fordi kravene ved oppstart kommer fra flere etater samtidig.

### For tjenesteeiere
Tjenesteeiere får synlighet i en nasjonal kanal med høy trafikk, uten å bygge egen publiseringsflate. Tjenesten blir søkbar og beskrevet i samme form som andre offentlige tjenester, noe som gjør den lettere å finne for brukere som ikke kjenner virksomheten fra før.

### For offentlig sektor
Verdien er en felles inngang framfor mange parallelle. Én portal som holdes oppdatert, med åpen kildekode og felles redaksjonell praksis, er billigere å forvalte enn tilsvarende flater hos hver enkelt virksomhet. Portalen bidrar også til at moderniseringen av Altinn framstår som én løsning for brukeren, selv om den er delt mellom flere produkter.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Sammenheng mellom flater | Portalen, Arbeidsflate og tilgangsstyringen er tre flater med hver sin adresse og hvert sitt produktteam. Brukeren kan oppleve bytter som brudd | Altinn oppgir at teamene arbeider mot et felles mål om sammenhengende opplevelse; hvordan dette styres i praksis er ikke offentlig beskrevet |
| Innholdsforvaltning | Tjenesteoversikten er bare så god som vedlikeholdet. Utdaterte eller manglende tjenestebeskrivelser gjør portalen mindre nyttig uten at noe framstår som ødelagt | Ikke offentlig dokumentert i denne arbeidsøkten hvilke rutiner som sikrer at tjenesteeiere holder beskrivelsene oppdatert |
| Rolleforståelse | Portalen oppfattes fortsatt som «hele Altinn», også internt i forvaltningen, slik `v3` av denne beskrivelsen viste | Skillet må skrives ut eksplisitt i beskrivelser og veiledning, ikke forutsettes kjent |
| Overlapp mot Norge.no | To nasjonale portaler viser vei til offentlige tjenester for innbyggere, og en Altinn-tjeneste rettet mot privatpersoner hører etter innholdsstrategien hjemme begge steder | Arbeidsdelingen er dokumentert på overordnet nivå i Altinns innholdsstrategi: Norge.no er primæradresse for privatpersoner, Altinn.no for virksomheter. Kildene sier ikke hvem som avgjør enkelttilfeller, eller hvordan redaksjonene samordner seg. Strategien nevner mulig framtidig sammenslåing uten at beslutning eller tidspunkt er oppgitt |
| Universell utforming | En nasjonal inngangsportal har stort nedslagsfelt hvis tilgjengelighetsfeil oppstår | Ikke offentlig dokumentert i denne arbeidsøkten ut over Altinns samlede tilgjengelighetserklæring |

## Kanaler
Portalen er en åpen webflate uten krav om innlogging, med `info.altinn.no` som adresse. Den er inngang til de innloggede flatene, men er selv tilgjengelig for alle.

De innloggede flatene portalen lenker til, er egne produkter: Arbeidsflate på `af.altinn.no` og brukerflaten for tilgangsstyring på `am.ui.altinn.no`. Portalen har ingen egen maskinell kanal.

## Plattform
**Fakta:** Portalen er bygget med Astro i frontend og Umbraco som publiseringsløsning, med kildekode og infrastrukturkode i `Altinn/info.altinn.no`.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Driftsmodell, skyleverandør og fordeling mellom frontend-, API- og plattformkomponenter i produksjon.

## Gjenbruk
Gjenbruksverdien ligger først og fremst i at portalen er en felles kanal. Tjenesteeiere slipper å bygge egne publiseringsflater for å bli funnet, og offentlig sektor slipper parallelle innganger til det samme tjenestetilbudet.

Kildekoden er dessuten åpen. Det gjør publiseringsløsningen mulig å studere og gjenbruke, selv om verdien for andre virksomheter er begrenset så lenge innholdet og tjenesteoversikten er spesifikk for Altinn. Den mest praktiske gjenbruken av Altinns frontend-arbeid ligger i `Altinn/altinn-components` og i Felles designsystem, ikke i portalen som helhet.

### Vanlige kombinasjoner med andre produkter
- **ID-porten** utfører innloggingen som portalen er inngang til.
- **Arbeidsflate** overtar når brukeren er logget inn og skal se innboks, dialoger og arkiv.
- **Altinn Autorisasjon** overtar når brukeren skal administrere fullmakter, tilgangspakker eller klientforhold.
- **Altinn Studio og Altinn Apps** produserer tjenestene som portalen viser og lenker til.
- **Felles designsystem** leverer komponenter og mønstre til brukergrensesnittet.
- **Norge.no** er den nærmeste naboen. Innholdsstrategien setter arbeidsdelingen slik at Norge.no er primæradresse for privatpersoner og Altinn.no for virksomheter, og at portalene skal peke videre til hverandre framfor å duplisere innhold.

**Kildekode:** Åpen kildekode

**Lisens:** MIT

**Repositorium:** https://github.com/Altinn/info.altinn.no

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov**
  Portalen er organisert etter hva brukeren skal gjøre, ikke etter hvilken etat som eier tjenesten, og samler veiledningen for næringsdrivende på tvers av kravstillerne.

- **P5: Del og gjenbruk løsninger**
  Én felles publiserings- og inngangsflate med åpen kildekode erstatter behovet for at hver virksomhet bygger sin egen.

- **P6: Lag digitale løsninger som støtter samhandling**
  Tjenesteoversikten gjør tilbudet fra mange virksomheter søkbart i samme form, slik at brukeren kan finne fram uten å kjenne forvaltningsstrukturen.

Spenninger og begrensninger: den tydeligste spenningen går mot **P1**. Portalen er brukerorientert i utforming, men arkitekturen deler brukerreisen mellom tre flater med hver sin adresse og hvert sitt produktteam. Brukeren skal oppleve én tjeneste, mens ansvaret er delt, og det er portalen som bærer det koordineringsansvaret uten å eie flatene den sender brukeren til. Den andre begrensningen gjelder **P5**: to nasjonale portaler viser fortsatt vei til offentlige tjenester. Arbeidsdelingen er dokumentert på overordnet nivå, men gjenbruket er ikke fullført så lenge en innbyggerrettet Altinn-tjeneste skal beskrives begge steder. Innholdsstrategien peker selv på sammenslåing som et mulig framtidig grep, noe som er en erkjennelse av at dagens deling koster.

## Finansiering
**Ikke offentlig dokumentert i denne arbeidsøkten:** Kostnadsmodell og budsjettfordeling for portalen isolert fra de øvrige Altinn-produktene. Portalen inngår i Digdirs portefølje av fellesløsninger, som forvaltes under Styringsrådet for Digitaliseringsdirektoratets fellesløsninger.

**Fakta:** Digdir har et pågående arbeid med ny finansieringsmodell for fellesløsningene. Utfallet kan påvirke hvordan portalen finansieres framover.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir, med Team Portal som produktteam i produktgruppen `Portalar og brukaroppleving` | Altinns egen omtale av produktteamene bak neste generasjon altinn.no, og Samarbeidsportalens produktgruppeside |
| Driftsansvar | Digdir, som del av Altinn | Portalen leveres på `info.altinn.no`, med infrastrukturkode i `Altinn/info.altinn.no` |
| Budsjettansvar | Digdir innenfor Altinn-porteføljen | Porteføljekontekst; detaljert kostnadsdeling er ikke offentlig |
| Styringsmodell | Styringsrådet for Digitaliseringsdirektoratets fellesløsninger er styringsarena. Produktutviklingen koordineres på tvers av flere produktteam i Altinn-porteføljen | Samarbeidsportalens sider om styringsrådet, og Altinns omtale av samarbeidet mellom produktteamene |

## Lenke til dokumentasjon
- Startside: https://info.altinn.no/
- Skjema og tjenester: https://info.altinn.no/no/Skjema-og-tjenester/
- Om nye Altinn: https://info.altinn.no/nyheter/om-nye-altinn/
- Innholdsstrategi for Altinn informasjonsportal: https://info.altinn.no/om-altinn/innholdsstrategi-altinn-informasjonsportal/
- Altinn som kanal for etablerere og næringsdrivende: https://www.digdir.no/digitalisering-og-samordning/bruk-altinn-som-kanal-etablerarar-og-naeringsdrivande/3117
- Produktgruppe portaler og brukeropplevelse: https://samarbeid.digdir.no/altinn/portalar-og-brukaroppleving/2485
- Kildekode: https://github.com/Altinn/info.altinn.no
- Gjenbrukbare grensesnittkomponenter: https://github.com/Altinn/altinn-components

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/21-Altinn-Portal-produkt-canvas-v3-codex.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/165-Arbeidsflate-v1-claude.md`
- Lokal fil: `config/templates/operative-ressurs-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- https://info.altinn.no/, kontrollert 2026-09-17
- https://info.altinn.no/om-altinn/innholdsstrategi-altinn-informasjonsportal/, kontrollert 2026-09-18
- https://www.digdir.no/digitalisering-og-samordning/bruk-altinn-som-kanal-etablerarar-og-naeringsdrivande/3117, kontrollert 2026-09-18
- https://samarbeid.digdir.no/altinn/portalar-og-brukaroppleving/2485, kontrollert 2026-09-17
- https://samarbeid.digdir.no/felleslosninger/felleslosninger/1309, kontrollert 2026-09-17
- https://github.com/Altinn/info.altinn.no, kontrollert 2026-09-17
- https://github.com/Altinn/altinn-components, kontrollert 2026-09-17

## Endringer fra forrige versjon

### Navneendring
Produktet heter `Altinn.no` fra `v4`, mot `Altinn Portal` i `v1` til `v3`. Digdir bruker `altinn.no` i fellesløsningsoversikten og i produktgruppen `Portalar og brukaroppleving`, og Altinns egen innholdsstrategi kaller portalen `Altinn informasjonsportal`. Ingen av kildene bruker `Altinn Portal`. Navnet ble misvisende da innboks og tilgangsstyring ble skilt ut, fordi `portal` da dekket mer enn produktet faktisk er. Skrivemåten `Altinn.no` med stor forbokstav følger `Norge.no` i samme register. Filnavnet er endret tilsvarende til `21-Altinn-no-v4-claude.md`.

### Kapabilitetsendringer
Tre koblinger er fjernet og én er lagt til. Ingen kapabilitet forsvinner fra porteføljen; alle er dekket av produktet som faktisk realiserer dem.

- `Tillit: Sporbarhet og innsyn` er fjernet. Meldingshistorikk, status og arkiv ligger i `165` Arbeidsflate, som har fått koblingen.
- `Tillit: Representasjon` og `Tillit: Tilgangsstyring` er fjernet. Fullmakter, tilgangspakker og klientadministrasjon forvaltes i `4` Altinn Autorisasjon, som har begge koblingene fra før. Portalen lenker til flaten på `am.ui.altinn.no`, men eier den ikke.
- `Sluttbrukertjenester: Tjenestekjeder` er fjernet. Kapabiliteten gjelder å sette sammen, koordinere og automatisere informasjonsflyt på tvers av uavhengige tjenester. Portalen viser vei til tjenester; den kobler dem ikke sammen.
- `Informasjonsforvaltning: Oversikt over tjenester` er lagt til. Portalen forvalter og publiserer oversikten over skjema og tjenester fra mange virksomheter, med søk. Dette var portalens mest åpenbare kapabilitet og manglet i `v3`.
- `Sluttbrukertjenester: Sammenhengende tjenester` er beholdt, men forklaringen er skrevet om fra å gjelde innboks og tilgangsstyring til å gjelde det portalen faktisk gjør: én inngang på tvers av etatsgrenser.

### Analyseforbedringer
- Scopet er avgrenset mot `165` Arbeidsflate og mot `4` Altinn Autorisasjon. `v3` beskrev innboks, profil og tilgangsstyring som portalens egne funksjoner, og arbeidsflaten som en intern overgangsfase. Startsiden viser at begge er egne flater som portalen lenker videre til.
- Overgangsfasen er avsluttet i teksten. Altinn II ble avviklet 19. juni 2026, og beskrivelsen av parallell drift av gammel og ny løsning er erstattet av dagens situasjon.
- Kildekodestatus er rettet fra `Ikke offentlig dokumentert` til `Åpen kildekode` under MIT, med `Altinn/info.altinn.no` som repositorium. `Lisens` manglet som felt i `v3`.
- `Plattform` er konkretisert med Astro og Umbraco framfor en generell beskrivelse av portalkomponenten.
- Tjenesteoversikten, veiledningssporet for næringsdrivende og hjelpesenteret er beskrevet som portalens egne leveranser. `v3` behandlet dem som underordnede sider ved brukerflaten.
- Overlappen mot Norge.no er dokumentert med kilde, ikke bare konstatert. Altinns innholdsstrategi for informasjonsportalen setter arbeidsdelingen: Norge.no er primæradresse for privatpersoner, Altinn.no for virksomheter, og portalene skal peke videre til hverandre framfor å duplisere. Det som ikke er avklart i kildene, er hvor grensen går for innbyggerrettede Altinn-tjenester, hvem som avgjør enkelttilfeller, og statusen for den mulige sammenslåingen strategien nevner. Dette er skrevet ut under `Scope og avgrensning`, i risikotabellen og under arkitekturprinsippene.
- Innholdsstrategien gav også et funn som ikke var med i `v3`: portalen er nasjonalt kontaktpunkt for EU-direktiver, og skal dekke statlige støtteordninger og virkemidler i tillegg til skjemakatalogen.

### Tekstlige forbedringer
- Linja `Målgruppe:` øverst er fjernet, i tråd med regelen om at målgruppe ikke skal stå som metadata i ressursbeskrivelsen.
- Tegnfeilen `ån felles portalflate` under `Gjenbruk` er rettet. Feilen var en strippet `É` som ingen av tegnkodingskontrollene fanger.
- Filnavnet følger det gjeldende mønsteret `NNN-Navn-vN-forfatter.md` uten `-produkt-canvas-`.
- `Hovedfunksjoner` er skrevet om fra kulepunkter til forklarende avsnitt, i tråd med kravet i malen.
