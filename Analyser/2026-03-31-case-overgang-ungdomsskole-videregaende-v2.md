---
date: 2026-03-31
author: copilot
status: "TEST av mal"
topic: arkitekturassistert-analyse-av-utviklingsbehov
sources:
  - arkitektur/kapabiliteter/capabilities.yaml
  - arkitektur/prinsipper/principles.md
  - arkitektur/ressurser/produktnummerering.md
  - arkitektur/ressurser/operative-losninger-og-tjenester/
  - config/templates/arkitekturassistert-analyse-av-utviklingsbehov-template.md
  - config/prompts/arkitekturassistert-analyse-av-utviklingsbehov.system.md
relatert: briefs/arbeidsstyring-og-handover/2026-03-31-case-tilgjengeliggjoring-resultater-videregaende-v1.md
---

# TEST-analyse - kortversjon

**Case:** Overgang fra ungdomsskole til videregÃ¥ende opplÃ¦ring

**Hovedfunn:**
Overgangen er et strukturelt brudd der informasjon om elevens behov, tilrettelegging og historikk verken flyter automatisk eller pÃ¥ en standardisert mÃ¥te. Ansvaret flyttes fra kommune til fylkeskommune, men systemene kommuniserer ikke. Tre barrierer dominerer: uavklart juridisk grunnlag for deling av pedagogisk dokumentasjon, manglende felles begreper og informasjonsmodell, og ingen orkestrert tjenestekjede over forvaltningsgrensen.

**Viktigste kapabilitetsgap:**
- Sammenhengende tjenester og tjenestekjeder: ingen nasjonal orkestrering av overgangen
- Juridisk samhandling: uavklart hjemmelsgrunnlag for pedagogisk dokumentasjon blokkerer deling
- Informasjonsforvaltning / Informasjonsarkitektur: ingen felles begrepssett for oppvekst og utdanning

**Mest relevante produkter for gjenbruk:**
- Feide (SIKT-001) â€“ autentisering for alle aktÃ¸rer i sektoren
- Altinn Events (DIGDIR-010) â€“ hendelsesdrevet overgang
- Dialogporten (DIGDIR-020) â€“ dialoglag pÃ¥ tvers av forvaltningsnivÃ¥
- FIKS-plattformen (KS-001) â€“ kommunal integrasjon mot nasjonale komponenter
- Maskinporten (DIGDIR-002) â€“ sikker maskin-til-maskin-overfÃ¸ring
- VIGO (NOVARI-004) â€“ sentral sektorlÃ¸sning for inntak og administrasjon i videregÃ¥ende
- FINT Felleskomponent (NOVARI-001) â€“ operativt integrasjonsmÃ¸nster i fylkeskommunal sektor

**Hva mangler:**
- Felles semantisk modell og overgangsprotokoll for pedagogisk dokumentasjon
- SamtykkehÃ¥ndtering tilpasset deling av sensitive opplysninger om barn
- Orkestrert tjenestekjede for hendelsesdrevet overgang
- Felles begrepsinnhold for oppvekst og utdanning i Begrepskatalogen

**Anbefalt prioritering:**
1. Juridisk avklaring av hjemmelsgrunnlag for elevdatadeling
2. Felles begrepssett og datamodell for overgangsdata
3. Pilot pÃ¥ hendelsesdrevet overgang med eksisterende felleskomponenter

---

# Arkitekturassistert analyse: overgang fra ungdomsskole til videregÃ¥ende opplÃ¦ring

## 1. FormÃ¥l

- AnalyseformÃ¥l: Vurdere hvilke kapabiliteter, prinsipper og produkter som er relevante for Ã¥ adressere informasjonsbrudd i overgangen mellom ungdomsskole og videregÃ¥ende opplÃ¦ring.
- Beslutning analysen skal understÃ¸tte: Prioritering av arkitekturtiltak og gjenbruksmuligheter i portefÃ¸ljearbeid for sektoren.
- Avgrensning: Analysen dekker nasjonalt og sektornivÃ¥. Virksomhetsinterne systemvalg i kommuner, fylkeskommuner eller direktorater er ikke i scope. For resultater etter fullfÃ¸rt videregÃ¥ende, se relatert analyse.

## 2. Input / casebeskrivelse

- Case-tittel: Overgang fra ungdomsskole til videregÃ¥ende opplÃ¦ring
- Kort casebeskrivelse: Overgangen fra ungdomsskole til videregÃ¥ende er en av de mest sentrale overgangene i barn og unges livslÃ¸p. Den innebÃ¦rer samtidig et skifte i forvaltningsansvar fra kommune til fylkeskommune. Relevant informasjon om elevens behov, tilrettelegging og historikk flyter i liten grad mellom de to nivÃ¥ene. Elever og foresatte fungerer som informasjonsbÃ¦rere i mangel av systemstÃ¸tte.
- BerÃ¸rte livshendelser: Avslutning av grunnskole, sÃ¸knad og opptak til videregÃ¥ende, oppstart og tilrettelegging i nytt skoleslag
- Hovedutfordring: Pedagogisk dokumentasjon og kunnskap om eleven nÃ¥r ikke frem til rett aktÃ¸r til rett tid. Ã…rsaken er en kombinasjon av uavklart hjemmelsgrunnlag, manglende felles begreper og usamordnede fagsystemer pÃ¥ tvers av forvaltningsgrensen.
- Kildemateriale: Innlevert casebeskrivelse og innledende problembeskrivelse fra sektoren

## 2.1 Inputgrunnlag og analysetillit

| Vurderingspunkt | Vurdering |
|---|---|
| Inputgrunnlag | Konseptuelt case med tydelig problembeskrivelse, men begrenset dokumentasjon av nÃ¥situasjon per aktÃ¸r |
| Datagrunnlag | Begrenset for presis effektmÃ¥ling; egnet for retningsvalg og identifisering av gap |
| Produktgrunnlag | Godt; basert pÃ¥ oppdatert produktkatalog og flere relevante sektor- og fellesprodukter |
| Samlet analysetillit | Middels |

Viktigste usikkerheter:
- Juridisk hjemmelsgrunnlag for deling av pedagogisk dokumentasjon mellom forvaltningsnivÃ¥
- Ulik modenhet i kommunale og fylkeskommunale systemlandskap
- Manglende felles begreps- og datamodell for overgangsdata

## 3. MÃ¥lgruppe og styringsnivÃ¥

- PrimÃ¦r mÃ¥lgruppe: Ungdom i overgangen fra grunnskole til videregÃ¥ende; sÃ¦rlig elever med behov for tilrettelegging
- SekundÃ¦r mÃ¥lgruppe: Foresatte, lÃ¦rere, rÃ¥dgivere, PPT og oppfÃ¸lgingstjenesten (OT), fagsystemleverandÃ¸rer
- StyringsnivÃ¥: Nasjonalt og sektornivÃ¥
- Viktig avgrensning: Tiltak skal adressere felles rammeverk, standarder og felleskomponenter â€“ ikke interne systemvalg i kommuner eller fylkeskommuner

## 4. Problembilde

### 4.1 Hovedproblem

Overgangen fra ungdomsskole til videregÃ¥ende er ikke stÃ¸ttet av sammenhengende informasjonsflyt. Ansvaret for eleven flyttes fra kommune til fylkeskommune, men informasjonen gjÃ¸r det ikke â€“ verken automatisk eller pÃ¥ en standardisert og sikker mÃ¥te. Fagsystemer pÃ¥ de to nivÃ¥ene deler verken datamodell, begreper eller integrasjonsflate. Usikkerhet rundt hjemmelsgrunnlag gjÃ¸r at aktÃ¸rene enten venter, innhenter informasjon pÃ¥ nytt, eller unnlater Ã¥ videresende relevant dokumentasjon. Resultatet er forsinkede tiltak, dobbeltarbeid og Ã¸kt risiko for frafall blant elever som trenger tett oppfÃ¸lging.

### 4.2 Konsekvenser for mÃ¥lgrupper

- Elever starter i ny skole uten at skolen kjenner til behov eller tidligere tiltak
- Elever med tilretteleggingsbehov mÃ¥ forklare sin situasjon pÃ¥ nytt, noe som oppleves stigmatiserende
- Foresatte fungerer som informasjonsbÃ¦rere mellom systemer som burde kommunisere direkte
- Unge som faller ut av videregÃ¥ende kan bli borte fra oppfÃ¸lgingstjenestene fordi informasjonsoverfÃ¸ringen til OT er manuell

### 4.3 Konsekvenser for forvaltning og tjenesteutÃ¸velse

- RÃ¥dgivere og spesialpedagoger bruker tid pÃ¥ gjeninnhenting av informasjon fremfor veiledning
- Kommuner og fylkeskommuner opererer med ulike begreper, noe som gir feil og forsinkelser
- Direktorater mangler systematisk grunnlag for Ã¥ vurdere om overgangsdata behandles i trÃ¥d med regelverket
- LeverandÃ¸rmarkedet er fragmentert og har ingen felles standard Ã¥ levere mot

## 5. Kapabilitetsanalyse

| Kapabilitet | Relevans | Hva finnes i dag | Identifisert gap | Konsekvens for caset |
|---|---|---|---|---|
| Sluttbrukertjenester: Sammenhengende tjenester | HÃ¸y | Sektortjenester finnes isolert | Ingen nasjonal tjenestekjede for overgang mellom skoleslag | Elever og foresatte opplever brudd og mÃ¥ koordinere selv |
| Sluttbrukertjenester: Tjenestekjeder | HÃ¸y | Ingen etablert pÃ¥ tvers av forvaltningsnivÃ¥ | Manglende orkestrering av informasjonsflyten | Videresending av pedagogisk dokumentasjon skjer manuelt |
| Sluttbrukertjenester: Proaktive tjenester | Middels | Ikke etablert i utdanning | Ingen automatisk varsling om rettigheter og frister ved overgang | Elever og foresatte oppdager ikke rettigheter og sÃ¸knadsfrister i tide |
| Datautveksling og integrasjon: Dele data med andre | HÃ¸y | Maskinporten finnes. Brukes ikke i utdanning pÃ¥ tvers av forvaltningsnivÃ¥ | Kommuner og fylkeskommuner deler ikke elevdata via felles API | Informasjon om elever gjeninnhentes eller mangler ved oppstart |
| Datautveksling og integrasjon: Hendelsesdrevet | HÃ¸y | Altinn Events finnes, ikke integrert i utdanning | Ingen hendelsesbasert varsling ved overgang | Overgangen skjer uten automatisk utlÃ¸st informasjonsflyt |
| Datautveksling og integrasjon: Meldingsformidling | Middels | FIKS Melding og Altinn Melding finnes | Ikke integrert i utdanningssektorens arbeidsflyt | Meldingsutveksling er manuell eller proprietÃ¦r |
| Informasjonsforvaltning: Informasjonsarkitektur | HÃ¸y | Begrepskatalog finnes som plattform | Ingen felles begrepssett for oppvekst og utdanning | Ulike begreper i systemene gir feiltolkning og samhandlingsproblemer |
| Informasjonsforvaltning: Datastyring | HÃ¸y | FIKS Digiorden finnes | Uklart hvem som eier og forvalter elevdata i overgangen | Ansvarsforvirring og risiko for regelverksbrudd |
| Tillit: Tilgangskontroll | HÃ¸y | Feide og Altinn Autorisasjon finnes separat | Ingen samlet tilgangsstyring pÃ¥ tvers av forvaltningsnivÃ¥ for elevdata | Riktige aktÃ¸rer mangler tilgang; ansvarsgrensen er uklar |
| Tillit: Representasjon | Middels | Altinn Autorisasjon finnes | Foreldreansvarsforhold er ikke koblet til utdanningstjenestene | Foresatte kan ikke alltid handle digitalt pÃ¥ vegne av barn |
| Tillit: Samtykke | HÃ¸y | Altinn Autorisasjon finnes | Ikke tilpasset sensitive opplysninger om barn under 18 | Usikkerhet om hva som krever samtykke blokkerer deling |
| Samarbeid: Organisatorisk samhandling | HÃ¸y | Faglige nettverk finnes | Ingen formalisert samhandlingsavtale for overgang mellom forvaltningsnivÃ¥ | Ansvarsovergangen er uformell og lokalt varierende |
| Juridisk samhandling | HÃ¸y | Nasjonalt rammeverk finnes | Uavklart hjemmelsgrunnlag for deling av pedagogisk dokumentasjon | AktÃ¸rene deler ikke informasjon av frykt for regelverksbrudd |
| Informasjonssikkerhet: Sikring av informasjonsflyt | HÃ¸y | Maskinporten finnes | Sensitiv elevdata overfÃ¸res i dag pÃ¥ ustrukturerte eller udokumenterte kanaler | Risiko for uautorisert tilgang til opplysninger om barn |

### Oppsummering av kapabilitetsgap

- Viktigste gap 1: Sammenhengende tjenester og tjenestekjeder â€“ ingen nasjonal orkestrering av informasjonsflyten ved overgang mellom skoleslag
- Viktigste gap 2: Juridisk samhandling og datastyring â€“ uavklart hjemmelsgrunnlag og uklart dataansvarsgrunnlag pÃ¥ tvers av forvaltningsnivÃ¥
- Viktigste gap 3: Informasjonsforvaltning / informasjonsarkitektur â€“ ingen felles begrepssett eller semantisk modell for overgangsdata i oppvekst og utdanning

## 6. Prinsippvurdering

| Prinsipp | Status | Hva finnes i dag | Hvordan caset utfordrer prinsippet |
|---|---|---|---|
| P1: Ta utgangspunkt i brukernes behov | Delvis | TjenestemÃ¥l er brukerrettede i intensjon | Systemene er bygget rundt organisatoriske siloer, ikke rundt elevens reise |
| P2: Ta arkitekturbeslutninger pÃ¥ rett nivÃ¥ | Brutt | Noen nasjonale rammer finnes | Beslutninger om dataflyt og integrasjon tas lokalt, uten nasjonalt rammeverk |
| P3: Bidra til digitaliseringsvennlige regelverk | Delvis | Digitaliseringsstrategien peker pÃ¥ behovet | Regelverket er ikke avklart nok til at aktÃ¸rene tÃ¸r dele relevant informasjon |
| P4: Del og gjenbruk data | Brutt | Folkeregisteret og grunndata finnes | Elevdata gjeninnhentes fremfor gjenbrukes. Ingen autoritative kilder for pedagogisk dokumentasjon |
| P5: Del og gjenbruk lÃ¸sninger | Brutt | Feide, Altinn Autorisasjon og FIKS finnes | Felleskomponentene er ikke integrert i sektorens arbeidsflyt. Parallelle sÃ¦rutviklinger dominerer |
| P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling | Brutt | FIKS, Dialogporten og Altinn Events finnes | Fagsystemer er ikke designet for samhandling pÃ¥ tvers av forvaltningsnivÃ¥ |
| P7: SÃ¸rg for tillit til oppgavelÃ¸sningen | Delvis | Maskinporten og Feide gir teknisk sikkerhet | Manglende juridisk avklaring undergraver tillit. Ansatte er usikre pÃ¥ hva de lovlig kan dele |

### Oppsummering av prinsippvurdering

P4, P5 og P6 er eksplisitt brutt. P3 og P7 er delvis oppfylt men blokkert av uavklart hjemmelsgrunnlag. Prinsippbruddene er gjensidig forsterkende: uklart regelverk (P3) hindrer datadeling (P4), som hindrer sammenhengende tjenester (P6).

## 7. Produktvurdering

### 7.1 Vurderte produkter fra katalogen

| Produkt | Produktkategori | Relevans | Kan brukes direkte | BÃ¸r videreutvikles | Ikke relevant | Begrunnelse |
|---|---|---|---|---|---|---|
| Feide (SIKT-001) | Felleskomponent â€“ autentisering | HÃ¸y | Ja | Nei | Nei | Etablert autentisering for hele utdanningssektoren. Dekker lÃ¦rere, elever og ansatte |
| ID-porten (DIGDIR-001) | Felleskomponent â€“ autentisering | HÃ¸y | Ja | Nei | Nei | Autentisering for foresatte og elever over 18 |
| Altinn Autorisasjon (DIGDIR-004) | Felleskomponent â€“ autorisasjon | HÃ¸y | Nei | Ja | Nei | Representasjon av barn er strukturelt nÃ¸dvendig, men sektorprofil for utdanning mangler |
| Maskinporten (DIGDIR-002) | Felleskomponent â€“ maskin-til-maskin | HÃ¸y | Ja | Nei | Nei | Sikrer maskin-til-maskin-kommunikasjon mellom fagsystemer i kommuner og fylkeskommuner |
| Altinn Events (DIGDIR-010) | Felleskomponent â€“ hendelsestjeneste | HÃ¸y | Ja | Nei | Nei | Hendelsesdrevet overgang (Â«elev avslutter ungdomsskoleÂ») er et sentralt behov som kan dekkes nÃ¥ |
| Dialogporten (DIGDIR-020) | FelleslÃ¸sning â€“ dialogtjeneste | HÃ¸y | Ja | Nei | Nei | Kan koble elev, foresatte, ungdomsskole og videregÃ¥ende i ett dialoglag |
| Altinn Melding (DIGDIR-021) | FelleslÃ¸sning â€“ korrespondansetjeneste | Middels | Ja | Nei | Nei | Strukturert meldingsutveksling mellom kommunale og fylkeskommunale systemer |
| Altinn Varsling (DIGDIR-022) | FelleslÃ¸sning â€“ varslingstjeneste | Middels | Ja | Nei | Nei | Varsle elever og foresatte om sÃ¸knadsfrister, vedtak og oppfÃ¸lging |
| Digital postkasse (DIGDIR-009) | Felleskomponent â€“ utsendingstjeneste | Middels | Ja | Nei | Nei | Kommunikasjon av vedtak og dokumentasjon til foresatte |
| Begrepskatalog (DIGDIR-012) | FelleslÃ¸sning â€“ begrepsbeskrivelse | HÃ¸y | Nei | Ja | Nei | Plattformen finnes, men innhold for oppvekst og utdanning er ikke etablert |
| FIKS-plattformen (KS-001) | Plattform â€“ kommunal integrasjon | HÃ¸y | Ja | Nei | Nei | Bindeledd mellom kommunale fagsystemer og nasjonale tjenester |
| VIGO (NOVARI-004) | FelleslÃ¸sning â€“ inntak og administrasjon i videregÃ¥ende | HÃ¸y | Ja | Nei | Nei | Sentralt sektorsystem i videregÃ¥ende som mÃ¥ inngÃ¥ i en sammenhengende overgangskjede |
| FINT Felleskomponent (NOVARI-001) | Felleskomponent â€“ fylkeskommunal integrasjon | HÃ¸y | Ja | Nei | Nei | Etablert operativt integrasjonsmÃ¸nster i fylkeskommunal sektor som kan redusere behovet for punkt-til-punkt |
| FINT Informasjonsmodell (NOVARI-003) | Referanseressurs â€“ informasjonsmodell | HÃ¸y | Nei | Ja | Nei | Gir semantisk grunnlag, men mÃ¥ suppleres med overgangsbegreper for ungdomsskole til videregÃ¥ende |
| FIKS Melding (KS-002) | FelleslÃ¸sning â€“ meldingsutveksling | Middels | Ja | Nei | Nei | Aktuell for utgÃ¥ende meldinger fra kommunale fagsystemer |
| FIKS Folkeregister (KS-008) | FelleslÃ¸sning â€“ registertilgang | HÃ¸y | Ja | Nei | Nei | Grunndata om elever og foresatte via kommunal integrasjon |
| Folkeregisteret (SKATT-001) | Register â€“ persondata | HÃ¸y | Ja | Nei | Nei | Autoritativ kilde for grunndata om elever og foresatte |
| Nasjonalt utdanningsregister (SIKT-006) | Register â€“ utdanningstilbud | Middels | Ja | Nei | Nei | Autoritativ kilde for skoler og tilbud, relevant for Ã¥ identifisere mottakende institusjon |
| Felles datakatalog (DIGDIR-011) | FelleslÃ¸sning â€“ metadataplattform | Middels | Ja | Nei | Nei | Kan brukes til Ã¥ beskrive og registrere overgangsdata som nasjonale datasett |
| Nasjonal vitnemÃ¥lsdatabase (SIKT-004) | Register â€“ vitnemÃ¥l | Lav | Nei | Nei | Ja | Relevant for avsluttet videregÃ¥ende, ikke for inngang til videregÃ¥ende |
| VitnemÃ¥lsportalen (SIKT-005) | Portal â€“ deling av vitnemÃ¥l | Lav | Nei | Nei | Ja | Gjelder resultater etter videregÃ¥ende â€“ se relatert analyse |
| OpptakslÃ¸sninger (SIKT-003) | FelleslÃ¸sning â€“ opptak | Lav | Nei | Nei | Ja | Gjelder hÃ¸yere utdanning â€“ se relatert analyse |
| Felles studentsystem (SIKT-002) | Plattform â€“ studentdata | Lav | Nei | Nei | Ja | Relevant for hÃ¸yere utdanning, ikke for overgangen inn i videregÃ¥ende |
| eInnsyn (DIGDIR-006) | FelleslÃ¸sning â€“ innsynslÃ¸sning | Lav | Nei | Nei | Ja | Lite relevant for operativ informasjonsflyt i overgangen |
| eSignering (DIGDIR-003) | Felleskomponent â€“ signering | Lav | Nei | Nei | Ja | Ikke sentralt for informasjonsflyten i overgangen |

### 7.2 Oppsummering

- Hva finnes: Autentisering (Feide, ID-porten), hendelsesinfrastruktur (Altinn Events), dialoglag (Dialogporten), meldingsformidling (Altinn Melding, FIKS Melding), kommunal/fylkeskommunal integrasjon (FIKS-plattformen, FINT Felleskomponent), sentral sektorlÃ¸sning for videregÃ¥ende (VIGO), grunndata (Folkeregisteret, FIKS Folkeregister), begrepskatalogen som plattform
- Hva kan gjenbrukes direkte: Feide, ID-porten, Maskinporten, Altinn Events, Dialogporten, Altinn Varsling, Altinn Melding, FIKS-plattformen, FINT Felleskomponent, VIGO, FIKS Folkeregister, Folkeregisteret, Nasjonalt utdanningsregister
- Hva mÃ¥ videreutvikles: Altinn Autorisasjon (sektorprofil for representasjon av barn), Begrepskatalog (innhold for oppvekst og utdanning), FINT Informasjonsmodell (utvidelser for overgangsdata)
- Ikke relevant for dette caset: Nasjonal vitnemÃ¥lsdatabase, VitnemÃ¥lsportalen, OpptakslÃ¸sninger, Felles studentsystem, eInnsyn, eSignering

### 7.3 Eksplisitte mangler

| Identifisert mangel | Hvorfor mangelen oppstÃ¥r | Konsekvens hvis ikke lÃ¸st | Forslag | Bygger pÃ¥ |
|---|---|---|---|---|
| Nasjonal overgangsprotokoll og semantisk modell for pedagogisk dokumentasjon | Ingen autoritativ kilde eller standardformat for IOP, tilretteleggingshistorikk og overgangsdata. Intet eksisterende produkt dekker dette innholdet | Tilretteleggingsinformasjon nÃ¥r ikke frem til ny skole â€“ Ã¸kt risiko for frafall | Felles informasjonsmodell og standardisering for overgangsdata, forvaltet som nasjonal ressurs | Begrepskatalog (DIGDIR-012), Felles datakatalog (DIGDIR-011), Maskinporten (DIGDIR-002) |
| SamtykkehÃ¥ndtering tilpasset sensitive opplysninger om barn | Altinn Autorisasjon er ikke tilpasset utdanningssektoren, sÃ¦rlig for barn under 18 og forholdet mellom barnets rettigheter og foreldreansvar | AktÃ¸rene deler ikke â€“ nÃ¸dvendig informasjon mangler i overgangen | Sektorprofil for samtykke og representasjon i utdanning | Altinn Autorisasjon (DIGDIR-004), ID-porten (DIGDIR-001), Feide (SIKT-001) |
| Orkestrert tjenestekjede for hendelsesdrevet overgang | Events, Dialogporten, VIGO og FINT finnes, men de er ikke koblet i en felles styrt flyt | Overgangen forblir manuell og lokalt ulik | Sammensatt tjenestekjede: Altinn Events som trigger, Dialogporten som dialoglag, Maskinporten for datautveksling, VIGO/FINT som sektornÃ¦re komponenter | Altinn Events (DIGDIR-010), Dialogporten (DIGDIR-020), Maskinporten (DIGDIR-002), VIGO (NOVARI-004), FINT Felleskomponent (NOVARI-001) |
| Felles begrepsmodell for oppvekst og utdanning | Begrepskatalogen finnes som plattform, men innholdet for sektoren er ikke etablert | Systemene forstÃ¥r ikke hverandre â€“ manuell oversettelse vedvarer | Etablering av autoritativt begrepssett for oppvekst og utdanning | Begrepskatalog (DIGDIR-012), Felles datakatalog (DIGDIR-011) |

## 8. Tiltak prioritert etter effekt

| Tiltak | Type | Effekt | Tidshorisont | Avhengigheter | Kobling | PrimÃ¦r gap-type |
|---|---|---|---|---|---|---|
| Avklare juridisk hjemmelsgrunnlag for deling av pedagogisk dokumentasjon | Avklaring | HÃ¸y | Kort | Utdanningsdirektorat, KDD, KS | Juridisk samhandling / P3 | Juridisk gap |
| Etablere felles begrepssett for oppvekst og utdanning i Begrepskatalogen | Nyutvikling (innhold) | HÃ¸y | Middels | Juridisk avklaring, sektoren, Digdir, SIKT | Informasjonsforvaltning: Oversikt over begreper / P4 / Begrepskatalog (DIGDIR-012) | Semantisk gap |
| Definere datamodell for overgangsdata | Avklaring + nyutvikling | HÃ¸y | Middels | Juridisk avklaring og begrepssett | Informasjonsforvaltning: Informasjonsarkitektur / P4 / Felles datakatalog (DIGDIR-011) | Semantisk gap |
| Pilotere hendelsesdrevet overgang med Altinn Events og Dialogporten | Gjenbruk + sammensatt | HÃ¸y | Middels | Datamodell og juridisk avklaring | Sluttbrukertjenester: Tjenestekjeder / P6 / Altinn Events + Dialogporten + Maskinporten | Samordningsgap |
| Integrere FIKS-plattformen og Maskinporten for elevdatadeling pÃ¥ tvers av forvaltningsnivÃ¥ | Gjenbruk | Middels | Middels | Datamodell | Datautveksling og integrasjon / P4, P5 / FIKS (KS-001) + Maskinporten (DIGDIR-002) | Samordningsgap |
| Etablere samordnet integrasjonsmÃ¸nster mellom VIGO, FINT og nasjonale felleskomponenter | Gjenbruk + samordning | HÃ¸y | Middels | Datamodell, juridisk avklaring, sektorsamordning | P5, P6 / VIGO (NOVARI-004) + FINT Felleskomponent (NOVARI-001) + Altinn Events (DIGDIR-010) | Samordningsgap |
| Etablere sektorprofil for representasjon av barn i Altinn Autorisasjon | Videreutvikling | Middels | Middels | Juridisk avklaring | Tillit: Representasjon og samtykke / P7 / Altinn Autorisasjon (DIGDIR-004) | Produktgap |

### Prioritert liste

1. Juridisk avklaring av hjemmelsgrunnlag â€“ forutsetning for alle tekniske tiltak
2. Felles begrepssett og datamodell â€“ nÃ¸dvendig premiss for integrasjon
3. Pilot pÃ¥ hendelsesdrevet overgang med VIGO/FINT i lÃ¸ypa â€“ demonstrerer at sektorlÃ¸sninger og nasjonale komponenter kan fungere sammen

## 9. Strategisk vurdering

- Betydning for portefÃ¸ljeprioritering: Caset viser at utdanningssektoren er underrepresentert i gjenbruk av nasjonale felleskomponenter. Rask effekt er mulig ved Ã¥ synliggjÃ¸re hva som kan hentes fra eksisterende produktkatalog.
- Betydning for nasjonal arkitektur: Peker pÃ¥ behovet for sektorvise arkitekturprofiler som bru mellom nasjonale felleskomponenter og sektorenes egne systemer.
- Behov for samordning: Utdanningsdirektorat (regelverk og standarder), KS og KS Digital (kommunal sektor og FIKS), Digdir (felleskomponenter), SIKT (utdanningsspesifikke produkter), fylkeskommunene som tjenesteytere.

## 10. Konklusjon

Overgangen fra ungdomsskole til videregÃ¥ende er et strukturert informasjonsbrudd som kan adresseres med produkter som allerede finnes i den nasjonale produktkatalogen. Det tekniske potensialet er til stede: Feide, Maskinporten, Altinn Events, Dialogporten, FIKS-plattformen, VIGO og FINT Felleskomponent kan tilsammen bygge en sammenhengende og hendelsesdrevet overgangsflyt. Men potensialet er ikke realiserbart fÃ¸r juridisk hjemmelsgrunnlag er avklart og en felles semantisk modell for overgangsdata er etablert. Disse to ikke-tekniske tiltakene er forutsetningen for alt annet. Uten dem vil kommuner og fylkeskommuner fortsette Ã¥ lÃ¸se overgangen lokalt, med ulike systemer og begreper, og informasjon om barn med tilretteleggingsbehov vil fortsette Ã¥ gÃ¥ tapt i overgangen.

