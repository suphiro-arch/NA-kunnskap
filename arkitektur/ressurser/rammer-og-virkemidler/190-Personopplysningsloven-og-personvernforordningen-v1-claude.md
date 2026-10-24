# Personopplysningsloven og personvernforordningen

## Navn
Lov om behandling av personopplysninger (personopplysningsloven), LOV-2018-06-15-38, med personvernforordningen, forordning (EU) 2016/679 (GDPR)

## Ressurs ID
DTIL-002

## Ressurskategori
Økonomiske og juridiske rammer og virkemidler

## Type virkemiddel
Lov som gjennomfører en EU-forordning

## Status/Livsfase
Aktiv.

**Fakta:** Loven trådte i kraft 20. juli 2018 og erstattet personopplysningsloven fra 2000. Den forvaltes av Justis- og beredskapsdepartementet. Lovdata oppgir siste endring som LOV-2021-06-18-124, i kraft fra 1. januar 2022. Personvernforordningen er tatt inn i EØS-avtalen vedlegg XI nr. 5e, og § 1 bestemmer at forordningen gjelder som norsk lov med de tilpasningene som følger av EØS-avtalen.

**Ikke offentlig dokumentert i denne arbeidsøkten:** status for eventuelle endringsforslag til personvernforordningen på EU-nivå og for innlemmelse av slike endringer i EØS-avtalen.

## Kort beskrivelse
Personopplysningsloven og personvernforordningen er det generelle regelverket for behandling av personopplysninger i Norge, både i offentlig og privat sektor. Forordningen inneholder hovedreglene: prinsippene for behandling, kravene til behandlingsgrunnlag, den registrertes rettigheter, pliktene for behandlingsansvarlig og databehandler, regler for overføring til land utenfor EØS og sanksjoner. Loven gjør forordningen til norsk lov, avgrenser virkeområdet, gir utfyllende nasjonale regler og organiserer tilsynet med Datatilsynet og Personvernnemnda.

Regelverket gjelder ved helt eller delvis automatisert behandling av personopplysninger, med mindre annet er bestemt i eller med hjemmel i lov (§ 2). Særlovgivning kan derfor gi mer spesifikke regler, men offentlige virksomheter må normalt ha et grunnlag i nasjonal rett for behandlingen.

## Formål og virkemiddelrolle
Regelverket skal beskytte den enkelte mot at personvernet krenkes gjennom behandling av personopplysninger, og samtidig legge til rette for fri flyt av opplysninger innenfor EØS når behandlingen er lovlig.

Hovedrollen er juridisk. Regelverket fastsetter når behandling er lovlig, hvilke krav som gjelder for utforming og drift av løsninger, og hvilke rettigheter den enkelte har. Det har også en institusjonell rolle ved at det etablerer Datatilsynet som uavhengig tilsynsmyndighet og Personvernnemnda som klageinstans.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er **juridisk bindende** for alle behandlingsansvarlige og databehandlere innenfor virkeområdet.

**Fakta:** De kravene som har størst betydning for digitale løsninger, er:

- **Behandlingsgrunnlag (artikkel 6):** behandling er bare lovlig når minst ett av vilkårene i nr. 1 er oppfylt. Offentlige myndigheter kan ikke bruke berettiget interesse (bokstav f) i utførelsen av sine oppgaver. Når grunnlaget er rettslig forpliktelse eller offentlig myndighetsutøvelse (bokstav c og e), skal grunnlaget være fastsatt i unionsretten eller nasjonal rett (nr. 3). For særlige kategorier av personopplysninger gjelder i tillegg artikkel 9.
- **Prinsippene (artikkel 5):** blant annet formålsbegrensning, dataminimering, riktighet, lagringsbegrensning og integritet og konfidensialitet. Den behandlingsansvarlige skal kunne påvise at prinsippene overholdes.
- **Innebygd personvern og personvern som standardinnstilling (artikkel 25):** egnede tekniske og organisatoriske tiltak skal gjennomføres både når midlene for behandlingen fastsettes og under behandlingen, og som standard skal bare nødvendige opplysninger behandles.
- **Vurdering av personvernkonsekvenser (artikkel 35):** skal gjøres før behandling som sannsynligvis gir høy risiko, blant annet ved systematisk vurdering basert på automatisert behandling som danner grunnlag for avgjørelser med rettsvirkning. Datatilsynet skal offentliggjøre en liste over behandlinger som krever vurdering. Gjenstår høy risiko, skal Datatilsynet rådspørres på forhånd (artikkel 36).
- **Sikkerhet (artikkel 32) og avviksmelding (artikkel 33):** tiltakene skal blant annet omfatte pseudonymisering og kryptering der det er egnet, og en prosess for regelmessig testing og vurdering av hvor effektive tiltakene er. Brudd på personopplysningssikkerheten skal meldes til Datatilsynet uten ugrunnet opphold og om mulig senest innen 72 timer.
- **Rett til dataportabilitet (artikkel 20):** gjelder bare behandling som bygger på samtykke eller avtale og skjer automatisert, og gjelder ikke behandling som er nødvendig for å utføre en oppgave i allmennhetens interesse eller utøve offentlig myndighet.
- **Automatiserte individuelle avgjørelser (artikkel 22):** den registrerte har rett til ikke å være gjenstand for en avgjørelse som utelukkende bygger på automatisert behandling og har rettsvirkning eller i betydelig grad påvirker vedkommende, med mindre avgjørelsen er nødvendig for en avtale, er tillatt i unionsretten eller nasjonal rett med egnede vernetiltak, eller bygger på uttrykkelig samtykke.
- **Personvernombud (artikkel 37):** offentlige myndigheter og organer skal utpeke personvernombud.

**Fakta:** Datatilsynet fører tilsyn, er et uavhengig forvaltningsorgan og kan ikke instrueres (§ 20). Datatilsynet kan ilegge offentlige myndigheter og organer overtredelsesgebyr (§ 26). Datatilsynets vedtak kan som hovedregel påklages til Personvernnemnda (§ 22).

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot lovteksten og forordningsteksten i Lovdata.

Regelverket realiserer kapabilitetene der det selv fastsetter kravene til hvordan behandlingen skal styres og sikres. `Tillit: Samtykke` er vurdert og ikke satt. Forordningen fastsetter vilkårene for et gyldig samtykke, men evnen til å innhente, registrere og trekke tilbake samtykker leveres av løsninger. `Juridisk samhandling: Regelverkstolkning` er ikke satt: regelverket er selv det som tolkes. Autoritative tolkninger og veiledning gis av Datatilsynet, blant annet gjennom den regulatoriske sandkassen (`DTIL-001`). `Informasjonsforvaltning: Datastyring` er vurdert og ikke satt, fordi rollene som behandlingsansvarlig og databehandler regulerer ansvar for personopplysninger, ikke forvaltning av dataressurser generelt.

- **Informasjonssikkerhet: Styringssystem**
  Artikkel 24 krever egnede tekniske og organisatoriske tiltak som skal gjennomgås og oppdateres ved behov, og artikkel 5 nr. 2 krever at den behandlingsansvarlige kan påvise etterlevelse. Artikkel 32 nr. 1 bokstav d krever en prosess for regelmessig testing og vurdering av hvor effektive sikkerhetstiltakene er, og artikkel 35 krever risikovurdering før behandling med høy risiko.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling**
  Artikkel 32 krever tiltak for konfidensialitet og integritet, med pseudonymisering og kryptering som eksempler, og artikkel 28 krever avtale som regulerer hva en databehandler kan gjøre med opplysningene. Kapittel V stiller vilkår for når personopplysninger kan overføres til land utenfor EØS.

## Målgruppe og berørte aktører
| Aktørsegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter som behandlingsansvarlige | Avklare behandlingsgrunnlag og krav til løsningene | Tjenesteutvikling, datadeling og automatisering | Må ha grunnlag i nasjonal rett ved myndighetsutøvelse, jf. artikkel 6 nr. 3 |
| Leverandører og databehandlere | Krav til sikkerhet og databehandleravtaler | Drift, skytjenester og utvikling | Artikkel 28 og 32 |
| Innbyggere som registrerte | Innsyn, retting, sletting, protest og vern mot automatiserte avgjørelser | Kontakt med offentlige og private tjenester | Artikkel 12–22 |
| Personvernombud | Uavhengig rådgivning internt | Vurdering av personvernkonsekvenser og internkontroll | Obligatorisk for offentlige myndigheter |
| Datatilsynet | Hjemmel for tilsyn, veiledning og sanksjoner | Tilsyn, forhåndsdrøftinger og avviksmeldinger | § 20 og artikkel 57–58 |
| Personvernnemnda | Klageinstans | Klager over Datatilsynets vedtak | § 22 |
| Departementer som lager særlovgivning | Utforme rettslig grunnlag for behandling | Regelverksutvikling | Artikkel 6 nr. 3 og artikkel 22 nr. 2 bokstav b |

## Virkemiddelmekanisme
**Fakta:** Regelverket virker gjennom fire mekanismer:

1. **Krav om grunnlag:** ingen behandling er lovlig uten behandlingsgrunnlag. For offentlige virksomheter betyr det at deling og gjenbruk av personopplysninger ofte forutsetter hjemmel i særlov eller i generelle regler som forvaltningsloven.
2. **Krav til utforming:** innebygd personvern og vurdering av personvernkonsekvenser legger krav inn i løsningsdesign før behandlingen starter.
3. **Rettigheter for den enkelte:** innsyn, retting, sletting, dataportabilitet og vern mot automatiserte avgjørelser må støttes av løsningene.
4. **Uavhengig tilsyn med sanksjoner:** Datatilsynet kan gi pålegg, forby behandling og ilegge overtredelsesgebyr, også overfor offentlige myndigheter.

**Deduksjon:** For offentlig sektor er kravet om grunnlag i nasjonal rett ofte det som avgjør om en digital tjeneste kan bygges som planlagt. Mange hindringer for datadeling som omtales som personvernhindringer, er i praksis mangel på hjemmel i særlovgivningen.

## Bruksområde
Regelverket må brukes i alle løsninger som behandler personopplysninger, og bør inn helt i starten av et utviklingsløp. Det utløser tidlig avklaring av behandlingsgrunnlag, formål, behov for vurdering av personvernkonsekvenser, rollefordeling mellom virksomheter og leverandører, og om avgjørelser skal automatiseres.

## Typiske analyse- og beslutningssituasjoner
- konseptvalg for tjenester som bygger på deling eller gjenbruk av personopplysninger på tvers av virksomheter, der behandlingsgrunnlaget må avklares før løsningen velges
- vurdering av om automatiserte avgjørelser er tillatt etter artikkel 22, og hvilke vernetiltak som må følge med
- vurdering av personvernkonsekvenser før nye løsninger, særlig ved profilering, store mengder særlige kategorier eller bruk av ny teknologi
- valg av sky- og driftsleverandør, der databehandleravtale og overføring til land utenfor EØS må vurderes
- fordeling av ansvar i tjenestekjeder: hvem som er behandlingsansvarlig, felles behandlingsansvarlig eller databehandler

## Når ressursen normalt ikke er tilstrekkelig alene
Regelverket sier ikke selv hvilke offentlige behandlinger som har grunnlag. Det må finnes i særlovgivningen eller i generelle regler som forvaltningsloven. Regelverket er også teknologinøytralt og må suppleres med veiledning fra Datatilsynet, tolkninger fra Det europeiske personvernrådet og rammeverk for informasjonssikkerhet.

## Økonomiske konsekvenser og insentiver
Regelverket inneholder ingen finansieringsordning.

**Fakta:** Overtredelsesgebyr kan ilegges etter artikkel 83, og etter § 26 også overfor offentlige myndigheter og organer.

**Deduksjon:** Kostnadene ligger i vurdering av personvernkonsekvenser, personvernombud, sikkerhetstiltak og løsninger for den registrertes rettigheter. Kostnaden ved å bygge inn kravene tidlig er normalt lavere enn ved å endre en løsning etter tilsyn eller avvik. Kildene tallfester ikke virkningene.

## Juridiske konsekvenser og handlingsrom
- **Må:** ha behandlingsgrunnlag, følge prinsippene i artikkel 5, bygge inn personvern, vurdere personvernkonsekvenser ved høy risiko, sikre opplysningene, melde avvik og ha personvernombud.
- **Kan:** velge tekniske og organisatoriske tiltak ut fra risiko og kostnad, og bruke godkjente sertifiseringsordninger og atferdsnormer for å vise etterlevelse.
- **Kan ikke:** bruke berettiget interesse som grunnlag for myndighetsutøvelse, eller treffe automatiserte avgjørelser omfattet av artikkel 22 uten grunnlag og vernetiltak.

De mest risikable avvikene er behandling uten gyldig grunnlag, gjenbruk av opplysninger til uforenlige formål, automatisering uten rettslig grunnlag og overføring til land utenfor EØS uten gyldig overføringsgrunnlag.

## Scope og avgrensning
Inngår:
- personopplysningsloven med utfyllende nasjonale regler, blant annet om barns samtykke, fødselsnummer (§ 12), forskning og arkiv, unntak fra rettigheter, tilsyn, klage og sanksjoner
- personvernforordningen, som gjelder som norsk lov

Inngår ikke:
- særlovgivning som gir behandlingsgrunnlag på enkeltområder
- behandling hos myndigheter som forebygger, etterforsker eller straffeforfølger straffbare forhold (forordningen artikkel 2 nr. 2 bokstav d), og saker etter rettspleielovene (§ 2)
- Datatilsynets veiledning og Personvernrådets retningslinjer, som tolker regelverket
- informasjonssikkerhet for systemer uten personopplysninger

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Justis- og beredskapsdepartementet for loven. Personvernforordningen vedtas i EU og tas inn i EØS-avtalen |
| Forvaltningsansvar | Justis- og beredskapsdepartementet. Datatilsynet er uavhengig tilsynsmyndighet og forvalter tilsyn, veiledning og forhåndsdrøftinger |
| Endringsprosess | Lovendring nasjonalt. Endringer i forordningen gjennom EUs regelverksprosess og EØS-komiteen |
| Publiserings- og beslutningsarena | Lovdata. Veiledning på datatilsynet.no |

## Relasjon til andre ressurser
- **Regulatorisk sandkasse for kunstig intelligens (`DTIL-001`)**
  Datatilsynets veiledningstilbud, som tolker regelverket i konkrete KI-prosjekter.
- **Forvaltningsloven (`JD-001`)**
  Den nye forvaltningsloven gir generelle regler om deling av taushetsbelagte opplysninger og automatiserte avgjørelser, og §§ 11 og 12 bygger direkte på personvernforordningen artikkel 22.
- **Digitalsikkerhetsloven (`NSM-002`)**
  Gjelder parallelt for tilbydere av samfunnsviktige tjenester, med egne sikkerhetskrav og egen varsling.
- **eForvaltningsforskriften (`DIGDIR-066`)**
  Regulerer elektronisk kommunikasjon med forvaltningen. Digdir er behandlingsansvarlig for Kontakt- og reservasjonsregisteret etter forskriften § 30.
- **Nasjonal verktøykasse for deling av data (`DIGDIR-038`)**
  Veiledning om datadeling, der avklaring av behandlingsgrunnlag er en sentral del.
- **Bruksvilkår for Digdirs fellesløsninger (`DIGDIR-073`)**
  Fordeler behandlingsansvar mellom Digdir og brukervirksomhetene for hver fellesløsning.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er felles og forutsigbare regler for personopplysninger i hele EØS, slik at virksomheter kan dele og bruke opplysninger lovlig når kravene er oppfylt.

Arkitekturverdien er at regelverket gjør personvern til et designkrav. Innebygd personvern, dataminimering og vurdering av personvernkonsekvenser påvirker hvilke data som samles inn, hvor de lagres, hvem som får tilgang og hvordan avgjørelser automatiseres.

## Konsekvens ved manglende bruk eller avvik
Brudd kan gi pålegg, forbud mot behandling og overtredelsesgebyr, og den registrerte kan kreve erstatning.

**Deduksjon:** Avklares behandlingsgrunnlaget for sent, kan en ferdig utviklet løsning måtte stanses eller bygges om. Ulik tolkning mellom virksomheter i samme tjenestekjede kan stoppe datadeling som ellers ville vært lovlig.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Tolkning og praktisering | Skjønnsmessige vilkår som nødvendighet, forenlige formål og høy risiko | Ulik praksis og risikoaversjon | Veiledning fra Datatilsynet og felles tolkninger i tjenestekjeden |
| Samspill med andre virkemidler | Behandlingsgrunnlag må finnes i særlovgivning | Tjenester stopper på manglende hjemmel | Avklare hjemmel tidlig og bruke regelverksutvikling ved behov |
| Endringshastighet | Forordningen endres i EU og må tas inn i EØS-avtalen | Usikkerhet om når endringer gjelder i Norge | Følge EØS-prosessen |
| Styring og forankring | Ansvar fordeles på mange behandlingsansvarlige i en kjede | Uklart ansvar for rettigheter og sikkerhet | Avtale om felles behandlingsansvar eller databehandleravtaler |

## Publiseringsform og tilgjengelighet
Loven og forordningen er publisert på Lovdata i én samlet tekst. Datatilsynet publiserer veiledning, blant annet om vurdering av personvernkonsekvenser.

## Støtter arkitekturprinsipper
- **P7: Sørg for tillit til oppgaveløsningen**
  Krav til grunnlag, åpenhet, sikkerhet og rettigheter gir den enkelte vern og grunnlag for tillit.
- **P4: Del og gjenbruk data**
  Regelverket setter rammene for når personopplysninger kan deles og viderebehandles.
- **P3: Bidra til digitaliseringsvennlige regelverk**
  Kravet om grunnlag i nasjonal rett gjør at særlovgivningen må utformes med deling og automatisering for øye.

Svakheter, spenninger og begrensninger mot prinsippene: kravet om grunnlag og formålsbegrensning kan gi friksjon mot `P4` når særlovgivningen ikke er tilpasset deling. Mange av vilkårene er skjønnsmessige, og ulik tolkning kan hemme samhandling selv der deling er lovlig.

## Lenke til dokumentasjon
- https://lovdata.no/dokument/NL/lov/2018-06-15-38
- https://www.datatilsynet.no/
- https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/vurdere-personvernkonsekvenser/

## Kildegrunnlag brukt i utfyllingen
- https://lovdata.no/dokument/NL/lov/2018-06-15-38 , med §§ 1, 2, 12 og 20–26 og forordningens artikler 2, 5, 6, 20, 22, 24, 25, 28, 32, 33, 35 og 37 lest enkeltvis, kontrollert 2026-10-25
- https://www.datatilsynet.no/rettigheter-og-plikter/virksomhetenes-plikter/vurdere-personvernkonsekvenser/ , kontrollert 2026-10-25
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-10-25
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-10-25
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-10-25
