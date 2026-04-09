---
date: 2026-03-31
author: copilot
status: "TEST av mal"
topic: arkitekturassistert-analyse-av-utviklingsbehov
sources:
  - arkitektur/kapabiliteter/capabilities.yaml
  - arkitektur/prinsipper/principles.md
  - arkitektur/produkter/produktnummerering.md
  - arkitektur/produkter/produktbeskrivelser/
  - config/templates/arkitekturassistert-analyse-av-utviklingsbehov-template.md
  - config/prompts/arkitekturassistert-analyse-av-utviklingsbehov.system.md
relatert: briefs/arbeidsstyring-og-handover/2026-03-31-case-tilgjengeliggjoring-resultater-videregaende-v1.md
---

# TEST-analyse - kortversjon

**Case:** Overgang fra ungdomsskole til videregående opplæring

**Hovedfunn:**
Overgangen er et strukturelt brudd der informasjon om elevens behov, tilrettelegging og historikk verken flyter automatisk eller på en standardisert måte. Ansvaret flyttes fra kommune til fylkeskommune, men systemene kommuniserer ikke. Tre barrierer dominerer: uavklart juridisk grunnlag for deling av pedagogisk dokumentasjon, manglende felles begreper og informasjonsmodell, og ingen orkestrert tjenestekjede over forvaltningsgrensen.

**Viktigste kapabilitetsgap:**
- Sammenhengende tjenester og tjenestekjeder: ingen nasjonal orkestrering av overgangen
- Juridisk samhandling: uavklart hjemmelsgrunnlag for pedagogisk dokumentasjon blokkerer deling
- Informasjonsforvaltning / Informasjonsarkitektur: ingen felles begrepssett for oppvekst og utdanning

**Mest relevante produkter for gjenbruk:**
- Feide (SIKT-001) – autentisering for alle aktører i sektoren
- Altinn Events (DIGDIR-010) – hendelsesdrevet overgang
- Dialogporten (DIGDIR-020) – dialoglag på tvers av forvaltningsnivå
- FIKS-plattformen (KS-001) – kommunal integrasjon mot nasjonale komponenter
- Maskinporten (DIGDIR-002) – sikker maskin-til-maskin-overføring
- VIGO (NOVARI-004) – sentral sektorløsning for inntak og administrasjon i videregående
- FINT Felleskomponent (NOVARI-001) – operativt integrasjonsmønster i fylkeskommunal sektor

**Hva mangler:**
- Felles semantisk modell og overgangsprotokoll for pedagogisk dokumentasjon
- Samtykkehåndtering tilpasset deling av sensitive opplysninger om barn
- Orkestrert tjenestekjede for hendelsesdrevet overgang
- Felles begrepsinnhold for oppvekst og utdanning i Begrepskatalogen

**Anbefalt prioritering:**
1. Juridisk avklaring av hjemmelsgrunnlag for elevdatadeling
2. Felles begrepssett og datamodell for overgangsdata
3. Pilot på hendelsesdrevet overgang med eksisterende felleskomponenter

---

# Arkitekturassistert analyse: overgang fra ungdomsskole til videregående opplæring

## 1. Formål

- Analyseformål: Vurdere hvilke kapabiliteter, prinsipper og produkter som er relevante for å adressere informasjonsbrudd i overgangen mellom ungdomsskole og videregående opplæring.
- Beslutning analysen skal understøtte: Prioritering av arkitekturtiltak og gjenbruksmuligheter i porteføljearbeid for sektoren.
- Avgrensning: Analysen dekker nasjonalt og sektornivå. Virksomhetsinterne systemvalg i kommuner, fylkeskommuner eller direktorater er ikke i scope. For resultater etter fullført videregående, se relatert analyse.

## 2. Input / casebeskrivelse

- Case-tittel: Overgang fra ungdomsskole til videregående opplæring
- Kort casebeskrivelse: Overgangen fra ungdomsskole til videregående er en av de mest sentrale overgangene i barn og unges livsløp. Den innebærer samtidig et skifte i forvaltningsansvar fra kommune til fylkeskommune. Relevant informasjon om elevens behov, tilrettelegging og historikk flyter i liten grad mellom de to nivåene. Elever og foresatte fungerer som informasjonsbærere i mangel av systemstøtte.
- Berørte livshendelser: Avslutning av grunnskole, søknad og opptak til videregående, oppstart og tilrettelegging i nytt skoleslag
- Hovedutfordring: Pedagogisk dokumentasjon og kunnskap om eleven når ikke frem til rett aktør til rett tid. Årsaken er en kombinasjon av uavklart hjemmelsgrunnlag, manglende felles begreper og usamordnede fagsystemer på tvers av forvaltningsgrensen.
- Kildemateriale: Innlevert casebeskrivelse og innledende problembeskrivelse fra sektoren

## 2.1 Inputgrunnlag og analysetillit

| Vurderingspunkt | Vurdering |
|---|---|
| Inputgrunnlag | Konseptuelt case med tydelig problembeskrivelse, men begrenset dokumentasjon av nåsituasjon per aktør |
| Datagrunnlag | Begrenset for presis effektmåling; egnet for retningsvalg og identifisering av gap |
| Produktgrunnlag | Godt; basert på oppdatert produktkatalog og flere relevante sektor- og fellesprodukter |
| Samlet analysetillit | Middels |

Viktigste usikkerheter:
- Juridisk hjemmelsgrunnlag for deling av pedagogisk dokumentasjon mellom forvaltningsnivå
- Ulik modenhet i kommunale og fylkeskommunale systemlandskap
- Manglende felles begreps- og datamodell for overgangsdata

## 3. Målgruppe og styringsnivå

- Primær målgruppe: Ungdom i overgangen fra grunnskole til videregående; særlig elever med behov for tilrettelegging
- Sekundær målgruppe: Foresatte, lærere, rådgivere, PPT og oppfølgingstjenesten (OT), fagsystemleverandører
- Styringsnivå: Nasjonalt og sektornivå
- Viktig avgrensning: Tiltak skal adressere felles rammeverk, standarder og felleskomponenter – ikke interne systemvalg i kommuner eller fylkeskommuner

## 4. Problembilde

### 4.1 Hovedproblem

Overgangen fra ungdomsskole til videregående er ikke støttet av sammenhengende informasjonsflyt. Ansvaret for eleven flyttes fra kommune til fylkeskommune, men informasjonen gjør det ikke – verken automatisk eller på en standardisert og sikker måte. Fagsystemer på de to nivåene deler verken datamodell, begreper eller integrasjonsflate. Usikkerhet rundt hjemmelsgrunnlag gjør at aktørene enten venter, innhenter informasjon på nytt, eller unnlater å videresende relevant dokumentasjon. Resultatet er forsinkede tiltak, dobbeltarbeid og økt risiko for frafall blant elever som trenger tett oppfølging.

### 4.2 Konsekvenser for målgrupper

- Elever starter i ny skole uten at skolen kjenner til behov eller tidligere tiltak
- Elever med tilretteleggingsbehov må forklare sin situasjon på nytt, noe som oppleves stigmatiserende
- Foresatte fungerer som informasjonsbærere mellom systemer som burde kommunisere direkte
- Unge som faller ut av videregående kan bli borte fra oppfølgingstjenestene fordi informasjonsoverføringen til OT er manuell

### 4.3 Konsekvenser for forvaltning og tjenesteutøvelse

- Rådgivere og spesialpedagoger bruker tid på gjeninnhenting av informasjon fremfor veiledning
- Kommuner og fylkeskommuner opererer med ulike begreper, noe som gir feil og forsinkelser
- Direktorater mangler systematisk grunnlag for å vurdere om overgangsdata behandles i tråd med regelverket
- Leverandørmarkedet er fragmentert og har ingen felles standard å levere mot

## 5. Kapabilitetsanalyse

| Kapabilitet | Relevans | Hva finnes i dag | Identifisert gap | Konsekvens for caset |
|---|---|---|---|---|
| Sluttbrukertjenester: Sammenhengende tjenester | Høy | Sektortjenester finnes isolert | Ingen nasjonal tjenestekjede for overgang mellom skoleslag | Elever og foresatte opplever brudd og må koordinere selv |
| Sluttbrukertjenester: Tjenestekjeder | Høy | Ingen etablert på tvers av forvaltningsnivå | Manglende orkestrering av informasjonsflyten | Videresending av pedagogisk dokumentasjon skjer manuelt |
| Sluttbrukertjenester: Proaktive tjenester | Middels | Ikke etablert i utdanning | Ingen automatisk varsling om rettigheter og frister ved overgang | Elever og foresatte oppdager ikke rettigheter og søknadsfrister i tide |
| Datautveksling og integrasjon: Dele data med andre | Høy | Maskinporten finnes. Brukes ikke i utdanning på tvers av forvaltningsnivå | Kommuner og fylkeskommuner deler ikke elevdata via felles API | Informasjon om elever gjeninnhentes eller mangler ved oppstart |
| Datautveksling og integrasjon: Hendelsesdrevet | Høy | Altinn Events finnes, ikke integrert i utdanning | Ingen hendelsesbasert varsling ved overgang | Overgangen skjer uten automatisk utløst informasjonsflyt |
| Datautveksling og integrasjon: Meldingsformidling | Middels | FIKS Melding og Altinn Melding finnes | Ikke integrert i utdanningssektorens arbeidsflyt | Meldingsutveksling er manuell eller proprietær |
| Informasjonsforvaltning: Informasjonsarkitektur | Høy | Begrepskatalog finnes som plattform | Ingen felles begrepssett for oppvekst og utdanning | Ulike begreper i systemene gir feiltolkning og samhandlingsproblemer |
| Informasjonsforvaltning: Datastyring | Høy | FIKS Digiorden finnes | Uklart hvem som eier og forvalter elevdata i overgangen | Ansvarsforvirring og risiko for regelverksbrudd |
| Tillit: Tilgangskontroll | Høy | Feide og Altinn Autorisasjon finnes separat | Ingen samlet tilgangsstyring på tvers av forvaltningsnivå for elevdata | Riktige aktører mangler tilgang; ansvarsgrensen er uklar |
| Tillit: Representasjon | Middels | Altinn Autorisasjon finnes | Foreldreansvarsforhold er ikke koblet til utdanningstjenestene | Foresatte kan ikke alltid handle digitalt på vegne av barn |
| Tillit: Samtykke | Høy | Altinn Autorisasjon finnes | Ikke tilpasset sensitive opplysninger om barn under 18 | Usikkerhet om hva som krever samtykke blokkerer deling |
| Samarbeid: Organisatorisk samhandling | Høy | Faglige nettverk finnes | Ingen formalisert samhandlingsavtale for overgang mellom forvaltningsnivå | Ansvarsovergangen er uformell og lokalt varierende |
| Juridisk samhandling | Høy | Nasjonalt rammeverk finnes | Uavklart hjemmelsgrunnlag for deling av pedagogisk dokumentasjon | Aktørene deler ikke informasjon av frykt for regelverksbrudd |
| Informasjonssikkerhet: Sikring av informasjonsflyt | Høy | Maskinporten finnes | Sensitiv elevdata overføres i dag på ustrukturerte eller udokumenterte kanaler | Risiko for uautorisert tilgang til opplysninger om barn |

### Oppsummering av kapabilitetsgap

- Viktigste gap 1: Sammenhengende tjenester og tjenestekjeder – ingen nasjonal orkestrering av informasjonsflyten ved overgang mellom skoleslag
- Viktigste gap 2: Juridisk samhandling og datastyring – uavklart hjemmelsgrunnlag og uklart dataansvarsgrunnlag på tvers av forvaltningsnivå
- Viktigste gap 3: Informasjonsforvaltning / informasjonsarkitektur – ingen felles begrepssett eller semantisk modell for overgangsdata i oppvekst og utdanning

## 6. Prinsippvurdering

| Prinsipp | Status | Hva finnes i dag | Hvordan caset utfordrer prinsippet |
|---|---|---|---|
| P1: Ta utgangspunkt i brukernes behov | Delvis | Tjenestemål er brukerrettede i intensjon | Systemene er bygget rundt organisatoriske siloer, ikke rundt elevens reise |
| P2: Ta arkitekturbeslutninger på rett nivå | Brutt | Noen nasjonale rammer finnes | Beslutninger om dataflyt og integrasjon tas lokalt, uten nasjonalt rammeverk |
| P3: Bidra til digitaliseringsvennlige regelverk | Delvis | Digitaliseringsstrategien peker på behovet | Regelverket er ikke avklart nok til at aktørene tør dele relevant informasjon |
| P4: Del og gjenbruk data | Brutt | Folkeregisteret og grunndata finnes | Elevdata gjeninnhentes fremfor gjenbrukes. Ingen autoritative kilder for pedagogisk dokumentasjon |
| P5: Del og gjenbruk løsninger | Brutt | Feide, Altinn Autorisasjon og FIKS finnes | Felleskomponentene er ikke integrert i sektorens arbeidsflyt. Parallelle særutviklinger dominerer |
| P6: Lag digitale løsninger som støtter samhandling | Brutt | FIKS, Dialogporten og Altinn Events finnes | Fagsystemer er ikke designet for samhandling på tvers av forvaltningsnivå |
| P7: Sørg for tillit til oppgaveløsningen | Delvis | Maskinporten og Feide gir teknisk sikkerhet | Manglende juridisk avklaring undergraver tillit. Ansatte er usikre på hva de lovlig kan dele |

### Oppsummering av prinsippvurdering

P4, P5 og P6 er eksplisitt brutt. P3 og P7 er delvis oppfylt men blokkert av uavklart hjemmelsgrunnlag. Prinsippbruddene er gjensidig forsterkende: uklart regelverk (P3) hindrer datadeling (P4), som hindrer sammenhengende tjenester (P6).

## 7. Produktvurdering

### 7.1 Vurderte produkter fra katalogen

| Produkt | Produktkategori | Relevans | Kan brukes direkte | Bør videreutvikles | Ikke relevant | Begrunnelse |
|---|---|---|---|---|---|---|
| Feide (SIKT-001) | Felleskomponent – autentisering | Høy | Ja | Nei | Nei | Etablert autentisering for hele utdanningssektoren. Dekker lærere, elever og ansatte |
| ID-porten (DIGDIR-001) | Felleskomponent – autentisering | Høy | Ja | Nei | Nei | Autentisering for foresatte og elever over 18 |
| Altinn Autorisasjon (DIGDIR-004) | Felleskomponent – autorisasjon | Høy | Nei | Ja | Nei | Representasjon av barn er strukturelt nødvendig, men sektorprofil for utdanning mangler |
| Maskinporten (DIGDIR-002) | Felleskomponent – maskin-til-maskin | Høy | Ja | Nei | Nei | Sikrer maskin-til-maskin-kommunikasjon mellom fagsystemer i kommuner og fylkeskommuner |
| Altinn Events (DIGDIR-010) | Felleskomponent – hendelsestjeneste | Høy | Ja | Nei | Nei | Hendelsesdrevet overgang («elev avslutter ungdomsskole») er et sentralt behov som kan dekkes nå |
| Dialogporten (DIGDIR-020) | Fellesløsning – dialogtjeneste | Høy | Ja | Nei | Nei | Kan koble elev, foresatte, ungdomsskole og videregående i ett dialoglag |
| Altinn Melding (DIGDIR-021) | Fellesløsning – korrespondansetjeneste | Middels | Ja | Nei | Nei | Strukturert meldingsutveksling mellom kommunale og fylkeskommunale systemer |
| Altinn Varsling (DIGDIR-022) | Fellesløsning – varslingstjeneste | Middels | Ja | Nei | Nei | Varsle elever og foresatte om søknadsfrister, vedtak og oppfølging |
| Digital postkasse (DIGDIR-009) | Felleskomponent – utsendingstjeneste | Middels | Ja | Nei | Nei | Kommunikasjon av vedtak og dokumentasjon til foresatte |
| Begrepskatalog (DIGDIR-012) | Fellesløsning – begrepsbeskrivelse | Høy | Nei | Ja | Nei | Plattformen finnes, men innhold for oppvekst og utdanning er ikke etablert |
| FIKS-plattformen (KS-001) | Plattform – kommunal integrasjon | Høy | Ja | Nei | Nei | Bindeledd mellom kommunale fagsystemer og nasjonale tjenester |
| VIGO (NOVARI-004) | Fellesløsning – inntak og administrasjon i videregående | Høy | Ja | Nei | Nei | Sentralt sektorsystem i videregående som må inngå i en sammenhengende overgangskjede |
| FINT Felleskomponent (NOVARI-001) | Felleskomponent – fylkeskommunal integrasjon | Høy | Ja | Nei | Nei | Etablert operativt integrasjonsmønster i fylkeskommunal sektor som kan redusere behovet for punkt-til-punkt |
| FINT Informasjonsmodell (NOVARI-003) | Referanseressurs – informasjonsmodell | Høy | Nei | Ja | Nei | Gir semantisk grunnlag, men må suppleres med overgangsbegreper for ungdomsskole til videregående |
| FIKS Melding (KS-002) | Fellesløsning – meldingsutveksling | Middels | Ja | Nei | Nei | Aktuell for utgående meldinger fra kommunale fagsystemer |
| FIKS Folkeregister (KS-008) | Fellesløsning – registertilgang | Høy | Ja | Nei | Nei | Grunndata om elever og foresatte via kommunal integrasjon |
| Folkeregisteret (SKATT-001) | Register – persondata | Høy | Ja | Nei | Nei | Autoritativ kilde for grunndata om elever og foresatte |
| Nasjonalt utdanningsregister (SIKT-006) | Register – utdanningstilbud | Middels | Ja | Nei | Nei | Autoritativ kilde for skoler og tilbud, relevant for å identifisere mottakende institusjon |
| Felles datakatalog (DIGDIR-011) | Fellesløsning – metadataplattform | Middels | Ja | Nei | Nei | Kan brukes til å beskrive og registrere overgangsdata som nasjonale datasett |
| Nasjonal vitnemålsdatabase (SIKT-004) | Register – vitnemål | Lav | Nei | Nei | Ja | Relevant for avsluttet videregående, ikke for inngang til videregående |
| Vitnemålsportalen (SIKT-005) | Portal – deling av vitnemål | Lav | Nei | Nei | Ja | Gjelder resultater etter videregående – se relatert analyse |
| Opptaksløsninger (SIKT-003) | Fellesløsning – opptak | Lav | Nei | Nei | Ja | Gjelder høyere utdanning – se relatert analyse |
| Felles studentsystem (SIKT-002) | Plattform – studentdata | Lav | Nei | Nei | Ja | Relevant for høyere utdanning, ikke for overgangen inn i videregående |
| eInnsyn (DIGDIR-006) | Fellesløsning – innsynsløsning | Lav | Nei | Nei | Ja | Lite relevant for operativ informasjonsflyt i overgangen |
| eSignering (DIGDIR-003) | Felleskomponent – signering | Lav | Nei | Nei | Ja | Ikke sentralt for informasjonsflyten i overgangen |

### 7.2 Oppsummering

- Hva finnes: Autentisering (Feide, ID-porten), hendelsesinfrastruktur (Altinn Events), dialoglag (Dialogporten), meldingsformidling (Altinn Melding, FIKS Melding), kommunal/fylkeskommunal integrasjon (FIKS-plattformen, FINT Felleskomponent), sentral sektorløsning for videregående (VIGO), grunndata (Folkeregisteret, FIKS Folkeregister), begrepskatalogen som plattform
- Hva kan gjenbrukes direkte: Feide, ID-porten, Maskinporten, Altinn Events, Dialogporten, Altinn Varsling, Altinn Melding, FIKS-plattformen, FINT Felleskomponent, VIGO, FIKS Folkeregister, Folkeregisteret, Nasjonalt utdanningsregister
- Hva må videreutvikles: Altinn Autorisasjon (sektorprofil for representasjon av barn), Begrepskatalog (innhold for oppvekst og utdanning), FINT Informasjonsmodell (utvidelser for overgangsdata)
- Ikke relevant for dette caset: Nasjonal vitnemålsdatabase, Vitnemålsportalen, Opptaksløsninger, Felles studentsystem, eInnsyn, eSignering

### 7.3 Eksplisitte mangler

| Identifisert mangel | Hvorfor mangelen oppstår | Konsekvens hvis ikke løst | Forslag | Bygger på |
|---|---|---|---|---|
| Nasjonal overgangsprotokoll og semantisk modell for pedagogisk dokumentasjon | Ingen autoritativ kilde eller standardformat for IOP, tilretteleggingshistorikk og overgangsdata. Intet eksisterende produkt dekker dette innholdet | Tilretteleggingsinformasjon når ikke frem til ny skole – økt risiko for frafall | Felles informasjonsmodell og standardisering for overgangsdata, forvaltet som nasjonal ressurs | Begrepskatalog (DIGDIR-012), Felles datakatalog (DIGDIR-011), Maskinporten (DIGDIR-002) |
| Samtykkehåndtering tilpasset sensitive opplysninger om barn | Altinn Autorisasjon er ikke tilpasset utdanningssektoren, særlig for barn under 18 og forholdet mellom barnets rettigheter og foreldreansvar | Aktørene deler ikke – nødvendig informasjon mangler i overgangen | Sektorprofil for samtykke og representasjon i utdanning | Altinn Autorisasjon (DIGDIR-004), ID-porten (DIGDIR-001), Feide (SIKT-001) |
| Orkestrert tjenestekjede for hendelsesdrevet overgang | Events, Dialogporten, VIGO og FINT finnes, men de er ikke koblet i en felles styrt flyt | Overgangen forblir manuell og lokalt ulik | Sammensatt tjenestekjede: Altinn Events som trigger, Dialogporten som dialoglag, Maskinporten for datautveksling, VIGO/FINT som sektornære komponenter | Altinn Events (DIGDIR-010), Dialogporten (DIGDIR-020), Maskinporten (DIGDIR-002), VIGO (NOVARI-004), FINT Felleskomponent (NOVARI-001) |
| Felles begrepsmodell for oppvekst og utdanning | Begrepskatalogen finnes som plattform, men innholdet for sektoren er ikke etablert | Systemene forstår ikke hverandre – manuell oversettelse vedvarer | Etablering av autoritativt begrepssett for oppvekst og utdanning | Begrepskatalog (DIGDIR-012), Felles datakatalog (DIGDIR-011) |

## 8. Tiltak prioritert etter effekt

| Tiltak | Type | Effekt | Tidshorisont | Avhengigheter | Kobling | Primær gap-type |
|---|---|---|---|---|---|---|
| Avklare juridisk hjemmelsgrunnlag for deling av pedagogisk dokumentasjon | Avklaring | Høy | Kort | Utdanningsdirektorat, KDD, KS | Juridisk samhandling / P3 | Juridisk gap |
| Etablere felles begrepssett for oppvekst og utdanning i Begrepskatalogen | Nyutvikling (innhold) | Høy | Middels | Juridisk avklaring, sektoren, Digdir, SIKT | Informasjonsforvaltning: Oversikt over begreper / P4 / Begrepskatalog (DIGDIR-012) | Semantisk gap |
| Definere datamodell for overgangsdata | Avklaring + nyutvikling | Høy | Middels | Juridisk avklaring og begrepssett | Informasjonsforvaltning: Informasjonsarkitektur / P4 / Felles datakatalog (DIGDIR-011) | Semantisk gap |
| Pilotere hendelsesdrevet overgang med Altinn Events og Dialogporten | Gjenbruk + sammensatt | Høy | Middels | Datamodell og juridisk avklaring | Sluttbrukertjenester: Tjenestekjeder / P6 / Altinn Events + Dialogporten + Maskinporten | Samordningsgap |
| Integrere FIKS-plattformen og Maskinporten for elevdatadeling på tvers av forvaltningsnivå | Gjenbruk | Middels | Middels | Datamodell | Datautveksling og integrasjon / P4, P5 / FIKS (KS-001) + Maskinporten (DIGDIR-002) | Samordningsgap |
| Etablere samordnet integrasjonsmønster mellom VIGO, FINT og nasjonale felleskomponenter | Gjenbruk + samordning | Høy | Middels | Datamodell, juridisk avklaring, sektorsamordning | P5, P6 / VIGO (NOVARI-004) + FINT Felleskomponent (NOVARI-001) + Altinn Events (DIGDIR-010) | Samordningsgap |
| Etablere sektorprofil for representasjon av barn i Altinn Autorisasjon | Videreutvikling | Middels | Middels | Juridisk avklaring | Tillit: Representasjon og samtykke / P7 / Altinn Autorisasjon (DIGDIR-004) | Produktgap |

### Prioritert liste

1. Juridisk avklaring av hjemmelsgrunnlag – forutsetning for alle tekniske tiltak
2. Felles begrepssett og datamodell – nødvendig premiss for integrasjon
3. Pilot på hendelsesdrevet overgang med VIGO/FINT i løypa – demonstrerer at sektorløsninger og nasjonale komponenter kan fungere sammen

## 9. Strategisk vurdering

- Betydning for porteføljeprioritering: Caset viser at utdanningssektoren er underrepresentert i gjenbruk av nasjonale felleskomponenter. Rask effekt er mulig ved å synliggjøre hva som kan hentes fra eksisterende produktkatalog.
- Betydning for nasjonal arkitektur: Peker på behovet for sektorvise arkitekturprofiler som bru mellom nasjonale felleskomponenter og sektorenes egne systemer.
- Behov for samordning: Utdanningsdirektorat (regelverk og standarder), KS og KS Digital (kommunal sektor og FIKS), Digdir (felleskomponenter), SIKT (utdanningsspesifikke produkter), fylkeskommunene som tjenesteytere.

## 10. Konklusjon

Overgangen fra ungdomsskole til videregående er et strukturert informasjonsbrudd som kan adresseres med produkter som allerede finnes i den nasjonale produktkatalogen. Det tekniske potensialet er til stede: Feide, Maskinporten, Altinn Events, Dialogporten, FIKS-plattformen, VIGO og FINT Felleskomponent kan tilsammen bygge en sammenhengende og hendelsesdrevet overgangsflyt. Men potensialet er ikke realiserbart før juridisk hjemmelsgrunnlag er avklart og en felles semantisk modell for overgangsdata er etablert. Disse to ikke-tekniske tiltakene er forutsetningen for alt annet. Uten dem vil kommuner og fylkeskommuner fortsette å løse overgangen lokalt, med ulike systemer og begreper, og informasjon om barn med tilretteleggingsbehov vil fortsette å gå tapt i overgangen.
