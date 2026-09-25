# Veileder for virksomhetsautentisering

## Navn
Veileder for virksomhetsautentisering

## Ressurs ID
DIGDIR-061

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Veileder

## Status/Livsfase
Aktiv. Veilederen er publisert på digdir.no under deling av data, og er også oppført i Digdirs oversikt over veiledere og hjelpemidler for elektronisk identitet.

**Fakta:** Delsidene ble opprettet i april 2021. Sidene om identifisering, autentisering og juridiske vurderinger ble sist endret 11. august 2022, og sidene om adressering og om sertifikatbehandling, logging og sporing 15. februar 2024.

**Deduksjon:** Veilederen er vedlikeholdt, men innholdet er i hovedsak fra 2021–2022. Den omtaler ikke den europeiske identitetslommeboka eller eIDAS 2, som Digdir behandler i andre veiledere på samme oversiktsside.

## Kort beskrivelse
Veileder for virksomhetsautentisering beskriver beste praksis for å identifisere, adressere og autentisere rett mottaker når data deles mellom virksomheter og sektorer.

**Fakta:** Utgangspunktet er at virksomhetssertifikat er den vanligste måten å kontrollere en virksomhets identitet på, men at det ikke finnes noen standardisert måte å autentisere deler av en virksomhet. Veilederen beskriver særlig hva som er god praksis når data skal deles med mottakere som ikke kan registreres i Enhetsregisteret. Digdir kaller disse `virksomhet uten registreringsrett`, og eksempler er offentlige utvalg, flerårige prosjekter med deltakere fra flere organisasjoner og sentre i høyere utdanning.

## Formål og normerende rolle
Formålet er gode og forutsigbare prosesser for identifisering og adressering av rett mottaker på tvers av virksomheter og sektorer.

**Fakta:** Veilederen beskriver et konkret problem med dagens praksis: fordi virksomhetssertifikatet ikke har mekanismer for å begrense bruksområdet, kan et sertifikat anskaffet til ett formål brukes mot alle andre systemer som stoler på virksomhetssertifikat. Digdir kaller dette en «universalnøkkel»-utfordring. Den gir også opphav til flere parallelle adresseringsløsninger med samme funksjon.

Den normerende rollen er å gi anbefalinger til tre roller, datakonsument, datatilbyder og forvalter av fellesløsning, om hvordan de bør identifisere, adressere og autentisere hverandre. Anbefalingene er formulert som `bør` og `må` per rolle.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er **anbefalt**, uten rettslig forankring i veilederen selv.

**Fakta:** Veilederen er ikke hjemlet i lov eller forskrift. Den tilhørende juridiske vurderingen konkluderer med at rettskildene «tilsynelatende» gir få spesifikke føringer for presisjonsnivå ved autentisering. Personvernforordningen artikkel 32 om sikkerhet ved behandlingen er den mest relevante bestemmelsen, men den krever en konkret risikovurdering og kan ikke leses som et generelt krav om presis autentisering. Vurderingen finner heller ikke krav i eForvaltningsforskriften eller lov om elektroniske tillitstjenester som står i veien for anbefalingene.

**Fakta:** Sikkerhetslovgivningen er uttrykkelig ikke vurdert i den juridiske gjennomgangen.

**Deduksjon:** Veilederen kan brukes som dokumentasjon på hva som er egnede tekniske og organisatoriske tiltak etter artikkel 32, men plikten følger av personvernregelverket og gjelder uansett om veilederen brukes. For virksomheter under sikkerhetsloven er det et åpent spørsmål om det gjelder strengere krav.

Etterlevelse skjer gjennom design av delingstjenester, sertifikatforvaltning og risikovurderinger. Avvik er ikke brudd, men bør begrunnes der dataene er rettslig regulerte og feil mottaker gir høy risiko.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot veilederens fire deler og den juridiske vurderingen.

Veilederen er ikke rettslig forankret, og `Juridisk samhandling` er derfor ikke aktuell. Den juridiske vurderingen er en del av veilederen, men gir ikke autoritativ tolkning utover å konstatere at rettskildene gir få føringer. `Veiledning: Anvendelse av veiledning` er tatt ut, fordi det er evnen til å bruke veiledere i egne prosjekter, som realiseres hos brukerne. `Tillit: Tilgangsstyring` er vurdert og ikke satt, fordi veilederen uttrykkelig holder autorisering hos mottakeren utenfor.

- **Tillit: Identifisering** normeres direkte i veilederens første del. Den gir anbefalinger for hvordan virksomheter uten registreringsrett kan få en identitet som kan brukes flere ganger og på tvers av sektorer, for eksempel ved å identifisere personer med en bemyndiget rolle i et autoritativt register, eller ved å bruke sertifikater på sektor- eller hovedenhetsnivå.
- **Tillit: Autentisering** normeres i veilederens del om autentisering: systemspesifikke asymmetriske nøkler som førstevalg for å unngå universalnøkkel-problemet, ingen statiske hemmeligheter, hyppig nøkkelrotasjon og kontroll av samhandlingspartens identitet mot aktuelle registre.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** normeres gjennom delene om adressering og om sertifikatbehandling, logging og sporing. Veilederen beskriver hvordan data kan begrenses til riktig del av mottakerens organisasjon, hvordan virksomhetssertifikatet skal beskyttes, og hvordan sporing skal sikres. Det er trafikkstyringen og kontrollen med hvem som mottar data, som kapabiliteten omfatter.
- **Veiledning: Utvikling og formidling av veiledning**
  Veilederen er Digdirs publiserte veiledning for virksomhetsautentisering, med anbefalinger i fire deler og en egen juridisk vurdering.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Datatilbydere | Sikker identifisering og adressering av mottaker | Deling av rettslig regulerte data | Tilbyderen svarer for at data kommer fram til riktig virksomhet |
| Datakonsumenter | Trygg håndtering av egne sertifikater og brukere | Lokal tilgangsstyring og nøkkelforvaltning | Veilederen retter egne anbefalinger mot denne rollen |
| Forvaltere av fellesløsninger | Mønstre for token, selvbetjening og delegering | Utforming av tillitstjenester | Maskinporten brukes som eksempel |
| Virksomheter uten registreringsrett | Egen identitet for samhandling | Utvalg, prosjekter og sentre uten organisasjonsnummer | Få løsninger dekker denne gruppen i dag |
| Sikkerhets- og personvernmiljøer | Sammenheng mellom tiltak og rettslige rammer | Risiko- og personvernvurderinger | Artikkel 32 krever konkret vurdering |

## Normerende innhold
**Fakta:** Veilederen har fire deler, supplert med en beskrivelse av utfordringsbildet og en juridisk vurdering:

1. **Identifisering** – virksomheter uten registreringsrett må kunne få en egen identitet. For virksomheter med organisasjonsnummer anbefales sertifikat utstedt til virksomheten. For fysiske personer anbefales eID på nivå betydelig eller høyt gjennom ID-porten, og eIDAS-knutepunktet for personer fra EU/EØS.
2. **Adressering** – adresser på så detaljert nivå som nødvendig, for eksempel på underenhetsnivå når dataminimering krever det. Bruk eksisterende adresseregistre og fellesløsninger, og foretrekk tilgangsstyring på tjenesteområde hos konsumenten framfor å forholde seg til konsumentens organisasjonshierarki.
3. **Sertifikatbehandling, logging og sporing** – ikke gjenbruk samme virksomhetssertifikat i mange systemer, ikke gi sertifikatet til underleverandører uten dedikert sertifikat og avtale, oppbevar det helst i en sikker maskinvaremodul, og lag en loggpolicy. Full ikke-benekting er ikke mulig å oppnå i praksis.
4. **Autentisering** – systemspesifikke nøkler, ingen statiske hemmeligheter, nøkkelrotasjon, «tynne» token med få attributter og tydelig semantikk for identifikatorer.

Det sentrale skillet i veilederen er mellom autentisering og autorisering. **Fakta:** Den juridiske vurderingen sier at tilbyderen ikke skal vurdere rettsgrunnlaget for mottakerens behandling. Selv om tilbyderen kan autentisere en underenhet presist, er det mottakeren som må vurdere om underenheten er autorisert.

## Bruksområde
Veilederen bør brukes når en delingsløsning skal utformes eller vurderes og det er viktig å treffe rett mottaker presist: når dataene er personopplysninger eller taushetsbelagte, når mottakeren er en underenhet, eller når mottakeren ikke har organisasjonsnummer.

Den er også relevant i daglig forvaltning av virksomhetssertifikater, der anbefalingene om nøkkelbehandling og sporing gjelder uavhengig av om en ny løsning utvikles.

## Typiske analyse- og beslutningssituasjoner
- når en datatilbyder må vite hvilken del av en virksomhet som faktisk er mottaker
- når mottakeren er et utvalg, et prosjekt eller et senter uten organisasjonsnummer
- når samme virksomhetssertifikat brukes i mange systemer eller hos underleverandører
- når autentisering og autorisering må skilles i løsningsdesign og ansvarsfordeling
- når en fellesløsning skal vurdere hvilke attributter den skal ta inn i token

## Når ressursen normalt ikke er tilstrekkelig alene
Veilederen er ikke tilstrekkelig alene for å etablere en delingsløsning. Den må suppleres med vurdering av rettsgrunnlaget for delingen, tilgangsstyring hos mottakeren, operative tillitstjenester og konkrete tekniske løsninger.

Den er heller ikke en erstatning for Maskinporten, virksomhetssertifikater eller andre autentiseringsmekanismer. **Fakta:** Veilederen sier selv at det finnes få løsninger som adresserer og autentiserer virksomheter uten organisasjonsnummer, og at virksomheten må vurdere å opprette nødvendige løsninger selv der ingen fellesløsning dekker behovet.

## Scope og avgrensning
Inngår:
- identifisering, adressering og autentisering av mottaker ved deling mellom virksomheter
- virksomheter uten registreringsrett i Enhetsregisteret
- sertifikatbehandling, logging og sporing i daglig forvaltning
- juridisk vurdering av om rettskildene stiller krav til presisjonsnivå

Inngår ikke:
- autorisering og tilgangskontroll hos mottakeren
- vurdering av rettsgrunnlaget for den enkelte deling
- sikkerhetslovgivningen
- spesifikasjon av en nasjonal teknisk løsning

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | Digdir publiserer veilederen under deling av data |
| Endringsprosess | **Ikke offentlig dokumentert i denne arbeidsøkten:** hvordan og når veilederen revideres. Sidene er sist endret i 2022 og 2024 |
| Publiserings- og beslutningsarena | Digdir.no |

## Relasjon til andre ressurser
- **Maskinporten (`DIGDIR-002`)**: operativ tillitstjeneste for maskin-til-maskin-autentisering, og veilederens eksempel på en løsning som ikke tillater statiske hemmeligheter. Autentiseringsevnen leveres av Maskinporten; veilederen gir anbefalinger for hvordan den brukes.
- **ID-porten (`DIGDIR-001`)**: anbefalt for identifisering av fysiske personer med fødsels- eller D-nummer, og for personer fra EU/EØS gjennom eIDAS-knutepunktet.
- **Enhetsregisteret (`BRREG-003`)**: grunnlaget for virksomhetsidentitet. Veilederen handler i stor grad om mottakere som faller utenfor registeret.
- **Feide (`SIKT-001`)**: nevnt som eksempel på eksisterende fellesløsning for identifikasjon og adressering av samhandlingspartnere.
- **eForvaltningsforskriften (`DIGDIR-066`)**: vurdert i veilederens juridiske del, uten at den gir krav som står i veien for anbefalingene.
- **Nasjonal verktøykasse for deling av data (`DIGDIR-038`)**: bredere samling av veiledning for datadeling som veilederen lenker til.
- **Veileder for identifikasjon og sporbarhet i elektronisk kommunikasjon med og i offentlig sektor**: står på samme oversiktsside hos Digdir og gir risikobasert valg av sikkerhetsnivå. Den er ikke egen ressurs i registeret.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er tryggere deling og mindre risiko for at data havner hos feil virksomhet eller feil enhet, særlig der dataene er sensitive. Anbefalingene om nøkkelbehandling reduserer også risikoen ved at samme sertifikat sprer seg til mange systemer og leverandører.

Arkitekturverdien ligger i at veilederen skiller identitet, adressering, autentisering og autorisering, og plasserer ansvaret for hver av dem. Den peker også på en strukturell svakhet i dagens bruk av virksomhetssertifikat som mange delingsløsninger bygger på.

## Konsekvens ved manglende bruk eller avvik
Hvis veilederen ikke brukes der presis mottakeridentifikasjon er viktig, øker risikoen for at data går til feil virksomhet eller feil enhet. Det kan gi sikkerhetsbrudd, personvernkonsekvenser og svakere tillit mellom delingsaktørene.

Hvis autentisering og autorisering blandes sammen, kan tilbyderen tro at teknisk identifisering er nok til å legitimere delingen, eller påta seg en vurdering av mottakerens behandling som ligger hos mottakeren.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Aktualitet | Innholdet er i hovedsak fra 2021–2022 og omtaler ikke eIDAS 2 | Anbefalingene kan bli ufullstendige når nye identitetsløsninger tas i bruk | Lese veilederen sammen med Digdirs nyere veiledere for eID |
| Løsningsdekning | Få løsninger dekker virksomheter uten organisasjonsnummer | Egne, parallelle løsninger | Bruke eksisterende registre og samarbeide med fellesløsningene om videreutvikling |
| Juridisk | Sikkerhetslovgivningen er ikke vurdert | Uavklarte krav for virksomheter under sikkerhetsloven | Egen vurdering der sikkerhetsloven gjelder |
| Forvaltning | Granulert adressering gir økt forvaltningsbehov hos begge parter | Høyere kostnad og feilrisiko | Veilederens anbefaling om tilgangsstyring på tjenesteområde |

## Publiseringsform og tilgjengelighet
Ressursen publiseres som åpne nettsider på digdir.no under deling av data, med én side per del og egne sider for utfordringsbildet og den juridiske vurderingen. Den er også oppført på Digdirs oversiktsside over veiledere og hjelpemidler for elektronisk identitet.

## Støtter arkitekturprinsipper
- **P7: Sørg for tillit til oppgaveløsningen**
  Veilederen styrker tilliten til hvem som mottar data, og krever sporing og loggpolicy som gjør det mulig å etterprøve delingen.
- **P6: Lag digitale løsninger som støtter samhandling**
  Den gjør deling mulig også med mottakere som i dag faller utenfor ordinær virksomhetsidentifikasjon.
- **P4: Del og gjenbruk data**
  Anbefalingene om adressering på riktig nivå og dataminimering gjør det mulig å dele sensitive data uten å gi bredere tilgang enn nødvendig.

Svakheter, spenninger og begrensninger mot prinsippene: Veilederen gir anbefalinger, men få løsninger som realiserer dem. Mot `P5: Del og gjenbruk løsninger` ligger en spenning i at veilederen, der ingen fellesløsning finnes, åpner for at virksomheten oppretter egne løsninger for adressering. Det kan forsterke de parallelle adresseringsløsningene veilederen selv beskriver som et problem.

## Lenke til dokumentasjon
- https://www.digdir.no/datadeling/veileder-virksomhetsautentisering/2435
- https://www.digdir.no/datadeling/utfordringsbildet-ved-bruk-av-virksomhetssertifikat/2482
- https://www.digdir.no/datadeling/identifisering/2436
- https://www.digdir.no/datadeling/adressering/2437
- https://www.digdir.no/datadeling/sertifikatbehandling-logging-og-sporing/2438
- https://www.digdir.no/datadeling/autentisering/2439
- https://www.digdir.no/datadeling/juridiske-vurderinger-relevante-virksomhetsautentisering/2488
- https://www.digdir.no/digital-identitet/veiledere-og-hjelpemidler/7311

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-09-25
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-25
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-25
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-09-25
- https://www.digdir.no/datadeling/veileder-virksomhetsautentisering/2435 , kontrollert 2026-09-25
- https://www.digdir.no/datadeling/utfordringsbildet-ved-bruk-av-virksomhetssertifikat/2482 , sist endret 11. august 2022, kontrollert 2026-09-25
- https://www.digdir.no/datadeling/identifisering/2436 , sist endret 11. august 2022, kontrollert 2026-09-25
- https://www.digdir.no/datadeling/adressering/2437 , sist endret 15. februar 2024, kontrollert 2026-09-25
- https://www.digdir.no/datadeling/sertifikatbehandling-logging-og-sporing/2438 , sist endret 15. februar 2024, kontrollert 2026-09-25
- https://www.digdir.no/datadeling/autentisering/2439 , sist endret 11. august 2022, kontrollert 2026-09-25
- https://www.digdir.no/datadeling/juridiske-vurderinger-relevante-virksomhetsautentisering/2488 , sist endret 11. august 2022, kontrollert 2026-09-25
- https://www.digdir.no/digital-identitet/veiledere-og-hjelpemidler/7311 , kontrollert 2026-09-25

## Endringer fra forrige versjon

### Analyseforbedringer
- `Normerende innhold` gjengir nå de konkrete anbefalingene i veilederens fire deler. `v1` listet temaene, men ikke hva veilederen anbefaler.
- Forpliktelsesnivået er avklart etter regelen fra 2026-09-13, med det den juridiske vurderingen faktisk konkluderer: rettskildene gir få spesifikke føringer, personvernforordningen artikkel 32 krever konkret vurdering, og sikkerhetslovgivningen er ikke vurdert.
- Kapabilitetene er prøvd mot definisjonene. `Tillit: Identifisering` er lagt til, fordi identifisering av virksomheter uten registreringsrett er veilederens første og mest særegne del. `Veiledning: Anvendelse av veiledning` og `Veiledning: Utvikling og formidling av veiledning` er tatt ut, fordi den første realiseres hos brukerne og den andre hos Digdir som utgiver. `v1` oppga hovedkapabiliteten `Veiledning`, som ikke er laveste nivå.
- Kapabilitetspunktene har fått hver sin forklaring. I `v1` sto forklaringen etter kulelista, og mappingen hadde derfor samme sammenslåtte tekst under flere koblinger.
- `Status/Livsfase` oppgir nå når sidene sist ble endret, og at innholdet ikke omtaler eIDAS 2.
- `Relasjon til andre ressurser` har fått ressurs-ID-er. Den juridiske vurderingen er beskrevet som en del av veilederen, ikke som egen ressurs.

### Tekstlige forbedringer
- Formuleringen «Ressursen er særlig viktig der …» er fjernet fra `Kort beskrivelse`, sammen med «høy praktisk relevans» i forpliktelsesfeltet.
- Fakta, deduksjon og manglende dokumentasjon er merket etter malen.
- Den egne seksjonen `Svakheter, spenninger og begrensninger mot prinsippene` er slått inn i `Støtter arkitekturprinsipper`.
