# Produkt-canvas: Barnevernsregisteret

## Navn
Barnevernsregisteret

## Ressurs ID
BUFDIR-001

## Status/Livsfase
**Produksjon** — nasjonalt rapporteringsregister i drift, med rapporteringsplikt for alle kommunale barnevernstjenester fra 1. januar 2023.

**Fakta:** Bufdir er behandlingsansvarlig for registeret, og Statistisk sentralbyrå drifter og vedlikeholder det på Bufdirs vegne. Rapporteringsplikten er hjemlet i barnevernsloven, i § 2-3 i loven av 1992 og § 16-2 i loven av 2021.

## Modenhet
**Middels til høy modenhet** — registeret er etablert og i drift, men kommunene er på ulikt nivå i innføringen.

- Kravene til hva som skal rapporteres er publisert som en `Barnevernsregister-xsd` på Bufdirs datasider.
- Kommuner med nye fagsystemer rapporterer automatisk og daglig, med automatisk kvalitetssikring.
- Kommuner med eldre fagsystemer rapporterer fortsatt manuelt to ganger i året gjennom KOSTRA-portalen og internettskjema.
- Kommunene går gjennom validering, migreringstest og statistiske kontroller før full overgang.

**Deduksjon:** Modenheten som register er høy, mens modenheten i rapporteringskjeden varierer med hvilket fagsystem den enkelte kommunen har. Det gir en overgangsperiode der to rapporteringsformer lever side om side, med ulik ferskhet på dataene.

## Kort beskrivelse
Barnevernsregisteret er det nasjonale registeret der alle kommunale barnevernstjenester rapporterer data om sin virksomhet. Registeret erstatter rapportering som tidligere gikk i separate løp til Statistisk sentralbyrå og Bufdir, og samler KOSTRA-rapporteringen og kommunenes halvårsrapporter i én ordning.

Bufdir er behandlingsansvarlig, mens Statistisk sentralbyrå drifter registeret. Rapporteringen er lovpålagt, og kravene til innhold er publisert som et maskinlesbart skjema kommunene og leverandørene kan bygge mot.

Registeret er et av resultatene fra DigiBarnevern, samarbeidet mellom Bufdir, KS og åtte kommuner som gikk fra 2016 til 2022. Den statlige delen av leveransene er nå tilgjengelig for kommunene gjennom nye fagsystemer i markedet.

## Kapabiliteter
- **Datautveksling og integrasjon: Dele data med andre**
  Registeret er kanalen der kommunale barnevernstjenester deler data med staten, i nye fagsystemer automatisk og daglig framfor gjennom periodiske manuelle innsendinger.
- **Datadrevet: Dataanalyse**
  Dataene brukes til å utvikle statistikk, styringsinformasjon og analyser om barnevernstjenesten.
- **Standardisering: Forvaltningsstandarder**
  Rapporteringskravene er publisert som et maskinlesbart skjema som fagsystemleverandørene må implementere, og som dermed fungerer som nasjonal rapporteringsstandard på området.

## Produktmål
Dokumenterte mål:
- Samle rapportering som tidligere gikk separat til Statistisk sentralbyrå og Bufdir i ett register.
- Forenkle og effektivisere kommunenes rapportering til staten.
- Forbedre data- og kunnskapsgrunnlaget om barnevernstjenesten.
- Gjøre rapporteringen automatisk, forenklet og løpende gjennom nye fagsystemer.

Operative mål utledet fra kildene:
- Fjerne behovet for separate KOSTRA-skjema og halvårsrapporter når kommunen er fullt over.
- Heve datakvaliteten gjennom automatisk kvalitetssikring i rapporteringsløpet.
- Gi mer aktuelle data ved daglig framfor halvårlig rapportering.

## Brukerbehov
- Kommunale barnevernstjenester trenger å oppfylle rapporteringsplikten uten dobbeltarbeid i flere skjema.
- Saksbehandlere trenger at rapporteringen skjer som en følge av arbeidet i fagsystemet, ikke som en separat oppgave.
- Bufdir trenger et samlet og oppdatert kunnskapsgrunnlag om barnevernstjenesten.
- Statistisk sentralbyrå trenger data i en form som kan brukes til offisiell statistikk.
- Statsforvalterne trenger grunnlag for tilsyn og oppfølging av kommunene.
- Fagsystemleverandører trenger entydige og maskinlesbare rapporteringskrav.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommunale barnevernstjenester | Oppfylle rapporteringsplikten med minst mulig merarbeid | Løpende rapportering fra fagsystem | Rapporteringsplikten gjelder alle kommuner |
| Bufdir | Samlet kunnskapsgrunnlag og styringsinformasjon | Statistikk, analyse og fagutvikling | Behandlingsansvarlig for registeret |
| Statistisk sentralbyrå | Data egnet for offisiell statistikk | Drift av registeret og statistikkproduksjon | Drifter registeret på Bufdirs vegne |
| Fagsystemleverandører | Entydige rapporteringskrav | Implementasjon mot registeret | Visma Flyt Barnevern og Modulus Barn støtter automatisk rapportering |
| Statsforvalterne | Grunnlag for tilsyn og oppfølging | Kontroll med kommunal barnevernstjeneste | Deduksjon: kildene omtaler statsforvalterne som målgruppe for informasjon om digitaliseringen, ikke eksplisitt som brukere av registerdata |
| Forsknings- og analysemiljøer | Data om barnevernstjenesten over tid | Kunnskapsutvikling | Kildene beskriver ikke tilgangsordning for eksterne forskere |

## Hovedfunksjoner
### Primære funksjoner
Kjernefunksjonen er å motta og samle rapportering fra alle kommunale barnevernstjenester i ett register. Der kommunene tidligere sendte data i separate løp til Statistisk sentralbyrå gjennom KOSTRA og til Bufdir gjennom halvårsrapporter, går rapporteringen nå til ett sted.

Rapporteringsveien avhenger av hvilket fagsystem kommunen har, og det er den viktigste operative forskjellen i dagens bilde. Kommuner som har tatt i bruk nye fagsystemer, rapporterer automatisk og daglig, med automatisk kvalitetssikring i løpet. Kommuner som fortsatt bruker eldre fagsystemer, rapporterer manuelt to ganger i året gjennom KOSTRA-portalen og internettskjema. Det betyr at registeret i praksis mottar data med svært ulik ferskhet fra ulike kommuner i overgangsperioden.

Rapporteringskravene er gjort maskinlesbare. Bufdir publiserer et `Barnevernsregister-xsd` som definerer hva som skal rapporteres, og dette er grunnlaget leverandørene bygger mot. Innholdet dekker det som tidligere var krevd gjennom KOSTRA årlig og gjennom kommunenes halvårsrapporter.

Overgangen for den enkelte kommunen skjer trinnvis. Kommunen går gjennom validering, migreringstest og statistiske kontroller før den er fullt integrert, og først etter det bortfaller de separate KOSTRA-skjemaene og halvårsrapportene.

Dataene brukes videre til statistikk, styringsinformasjon og analyser om barnevernstjenesten. Registeret er dermed et rapporterings- og kunnskapsregister, ikke et operativt saksbehandlingssystem eller en kilde fagsystemene henter fra.

### Typiske brukssituasjoner (generisk)
- Når en kommunal barnevernstjeneste skal oppfylle den lovpålagte rapporteringsplikten.
- Når en kommune går over til nytt fagsystem og skal etablere automatisk daglig rapportering.
- Når Bufdir eller Statistisk sentralbyrå skal produsere statistikk om barnevernstjenesten.
- Når en fagsystemleverandør skal implementere rapportering etter det publiserte skjemaet.
- Når en kommune skal gjennom validering og migreringstest før full overgang.
- Når nasjonale myndigheter trenger styringsinformasjon om utviklingen i barnevernet.

### Når Barnevernsregisteret normalt ikke er førstevalg
- Når behovet er operativ saksbehandling i en barnevernssak. Det skjer i kommunens fagsystem, ikke i registeret.
- Når behovet er å motta en bekymringsmelding. Det dekkes av `KS Bekymringsmelding` (`KS-015`).
- Når behovet er innsyn for parter i en barnevernssak. Registeret er et rapporteringsregister, ikke en innsynsløsning.
- Når data må være ferske fra alle kommuner. I overgangsperioden rapporterer kommuner med eldre fagsystemer bare halvårlig.
- Når behovet gjelder andre deler av oppvekstfeltet enn kommunalt barnevern.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Lovpålagt rapportering fra alle kommunale barnevernstjenester | Operativ saksbehandling i barnevernssaker |
| Samling av tidligere KOSTRA-rapportering og kommunale halvårsrapporter | Mottak av bekymringsmeldinger |
| Maskinlesbare rapporteringskrav gjennom publisert xsd | Fagsystemfunksjonalitet for barnevernstjenesten |
| Grunnlag for statistikk, styringsinformasjon og analyser | Innsyns- og dialogtjenester for parter i barnevernssaker |
| Automatisk daglig rapportering fra nye fagsystemer | Rollen som datakilde fagsystemene henter opplysninger fra |

## Veikart over kommende funksjonalitet
Kildene beskriver ikke et samlet veikart for registeret. Det som er dokumentert, er at kommunene går over trinnvis etter hvilket fagsystem de har, og at de separate KOSTRA-skjemaene og halvårsrapportene bortfaller når en kommune er fullt integrert. Innføringstakten avhenger dermed av kommunenes anskaffelse av nye fagsystemer.

## Forretningsverdi/Verdiforslag
- For kommunene: én rapporteringsvei framfor to, og rapportering som følger av arbeidet i fagsystemet framfor som en separat skjemaoppgave.
- For staten: et samlet og mer aktuelt kunnskapsgrunnlag om barnevernstjenesten, med automatisk kvalitetssikring i rapporteringsløpet.
- For barn og unge i barnevernet: bedre kunnskapsgrunnlag gir bedre grunnlag for å styre og utvikle tjenesten de mottar. Effekten er indirekte, siden registeret er et rapporteringsregister og ikke en tjeneste barnet møter.
- For leverandørmarkedet: entydige og publiserte rapporteringskrav som kan implementeres én gang og selges til mange kommuner.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Innføring | Kommuner med eldre fagsystemer rapporterer fortsatt halvårlig og manuelt | Følge kommunenes overgang til nye fagsystemer, og være tydelig på datakvalitet i overgangsperioden |
| Datakvalitet | Data har ulik ferskhet avhengig av kommunens fagsystem | Angi rapporteringsvei og periode når registerdata brukes i analyse |
| Personvern | Registeret behandler opplysninger om barn i en særlig sårbar situasjon | Tydelig behandlingsansvar hos Bufdir og databehandlerrolle hos Statistisk sentralbyrå |
| Leverandøravhengighet | Automatisk rapportering forutsetter fagsystem som støtter det, og markedet har få leverandører | Publiserte og entydige krav som senker terskelen for nye leverandører |
| Ansvarsdeling | Bufdir er behandlingsansvarlig mens Statistisk sentralbyrå drifter | Tydelig avtale- og ansvarsbeskrivelse mellom de to |
| Endringsstyring | Endringer i rapporteringskravene treffer alle fagsystemer samtidig | Versjonering og forutsigbar varsling av endringer i skjemaet |

## Kanaler
- https://www.bufdir.no/fagstotte/barnevern-oppvekst/barnevernsregisteret/
- https://data.bufdir.no/
- https://www.bufdir.no/prosjekter/digibarnevern/

## Plattform
Sentralt rapporteringsregister driftet av Statistisk sentralbyrå på Bufdirs vegne. Rapportering skjer maskinelt fra kommunale fagsystemer etter et publisert xsd-skjema, og for kommuner med eldre fagsystemer gjennom KOSTRA-portalen og internettskjema.

## Gjenbruk
**Middels gjenbruksverdi:**
- Registeret er én nasjonal ordning som erstatter to tidligere rapporteringsløp, og gjenbruket ligger i at alle kommuner rapporterer etter samme krav.
- Det publiserte rapporteringsskjemaet har direkte gjenbruksverdi for leverandører, som implementerer det én gang for mange kommuner.
- Registeret er ikke en komponent andre virksomheter kan ta i bruk i egne løsninger, og gjenbruket gjelder derfor ordningen og kravene, ikke teknologien.

**Vanlige kombinasjoner med andre produkter:**
- `KS Bekymringsmelding` (`KS-015`) er den andre nasjonale løsningen fra DigiBarnevern-samarbeidet, og dekker inngangen til barnevernstjenesten der registeret dekker rapporteringen ut.
- Kommunale barnevernsfagsystemer er kilden til rapporteringen, i praksis Visma Flyt Barnevern og Modulus Barn for automatisk rapportering.
- `Folkeregisteret` (`SKATT-001`) er den autoritative kilden til personopplysningene barnevernssaker bygger på. Kildene beskriver ikke koblingen direkte, så dette er en vurdering.
- `Fiks-plattformen` (`KS-001`) er kommunal integrasjonsinfrastruktur som kan være relevant i rapporteringskjeden. Kildene bekrefter ikke slik bruk.

**Kildekode:** Ikke offentlig dokumentert. Selve registeret er ikke publisert som kildekode. Bufdir publiserer rapporteringskravene som maskinlesbart skjema på [data.bufdir.no](https://data.bufdir.no/).

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Registeret samler rapportering som tidligere gikk i to separate løp, slik at kommunen leverer data én gang og flere statlige aktører bruker dem.
- **P6: Lag digitale løsninger som støtter samhandling**
  Maskinlesbare rapporteringskrav gjør at data kan gå automatisk fra kommunalt fagsystem til statlig register uten manuell mellomstasjon.
- **P2: Ta arkitekturbeslutninger på rett nivå**
  Rapporteringskravene er fastsatt nasjonalt og publisert, framfor at hver statlig etat definerer sitt eget innsamlingsbehov mot kommunene.
- **P7: Sørg for tillit til oppgaveløsningen**
  Tydelig plassert behandlingsansvar og automatisk kvalitetssikring i rapporteringsløpet styrker etterprøvbarheten.

Spenning og begrensning: registeret behandler opplysninger om barn i en sårbar situasjon, og gevinsten ved mer og ferskere data må veies mot personvernhensyn i hver bruk. Overgangsperioden er en reell svakhet: så lenge en del kommuner rapporterer halvårlig og manuelt, er registeret ikke et ensartet datagrunnlag, og analyser må ta høyde for det. Automatisk rapportering forutsetter også fagsystem som støtter det, og det gjør gevinsten avhengig av kommunale anskaffelser registeret selv ikke styrer.

## Finansiering
Kildene beskriver ingen egen finansieringsmodell eller brukerbetaling. Registeret er en lovpålagt ordning, og forvaltningen inngår i Bufdirs virksomhet med Statistisk sentralbyrå som driftsansvarlig.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Behandlingsansvar og faglig eierskap | Bufdir | bufdir.no |
| Drift og vedlikehold av registeret | Statistisk sentralbyrå, på Bufdirs vegne | bufdir.no |
| Rapporteringsplikt | Kommunale barnevernstjenester | Barnevernsloven § 2-3 (1992) og § 16-2 (2021) |
| Rapporteringskrav og skjema | Bufdir, publisert på data.bufdir.no | Barnevernsregister-xsd |
| Videre utvikling og forvaltning av DigiBarnevern-leveransene | Bufdir og KS i samarbeid | Samarbeidet fortsatte etter at prosjektet ble avsluttet |

## Lenke til dokumentasjon
- https://www.bufdir.no/fagstotte/barnevern-oppvekst/barnevernsregisteret/
- https://data.bufdir.no/
- https://www.bufdir.no/prosjekter/digibarnevern/
- https://www.ks.no/fagomrader/digitalisering/felleslosninger/digibarnevern/

## Kildegrunnlag brukt i utfyllingen
- https://www.bufdir.no/fagstotte/barnevern-oppvekst/barnevernsregisteret/, kontrollert 2026-09-07
- https://www.bufdir.no/prosjekter/digibarnevern/, kontrollert 2026-09-07
- https://www.ks.no/fagomrader/digitalisering/felleslosninger/digibarnevern/, kontrollert 2026-09-07
- `arkitektur/ressurser/operative-losninger-og-tjenester/96-KS-Bekymringsmelding-produkt-canvas-v1-codex.md`, kontrollert 2026-09-07
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-07
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-07
