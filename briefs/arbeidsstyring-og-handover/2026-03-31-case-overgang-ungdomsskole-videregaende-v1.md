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
---

# TEST-analyse - kortversjon

**Case:** Overgang fra ungdomsskole til videregående og tilgjengeliggjøring av resultater fra videregående opplæring.

**Hovedfunn:**
Tre strukturelle barrierer dominerer: fragmenterte og usamordnede fagsystemer, uklart juridisk grunnlag for deling av elevdata på tvers av forvaltningsnivå, og manglende felles begreper og informasjonsmodell for sektoren. Konsekvensen er dobbeltarbeid, informasjonsbrudd i overgangen, og økt risiko for frafall særlig blant elever med tilretteleggingsbehov.

**Viktigste kapabilitetsgap:**
- Sammenhengende tjenester: overgangen er et strukturert brudd, ikke et sømløst hendelsesforløp
- Informasjonsforvaltning / Datastyring: ingen felles modell for hvem som eier og deler elevdata på tvers av forvaltningsnivå
- Juridisk samhandling: usikkerhet i sektoren om hjemmelsgrunnlag for deling av pedagogisk dokumentasjon

**Mest relevante produkter for gjenbruk:**
- Feide (SIKT-001) – autentisering for alle aktører i utdanning
- Altinn Autorisasjon (DIGDIR-004) – representasjon foresatte, tilgangsstyring
- Altinn Events (DIGDIR-010) – hendelsesdrevet overgang
- Dialogporten (DIGDIR-020) – tverrgående dialog mellom skole og forvaltningsnivåer
- Nasjonal vitnemålsdatabase (SIKT-004) og Vitnemålsportalen (SIKT-005) – direkte gjenbruk for case 2
- FIKS-plattformen (KS-001) – kommunal integrasjon

**Hva mangler:**
- Felles semantisk modell og overgangsprotokoll for pedagogisk dokumentasjon
- Samtykkehåndtering tilpasset utdanningssektoren og personvern for barn
- Felles begrepssett for oppvekst og utdanning (innhold i Begrepskatalogen)
- Hendelsesbasert overgangsflyt (orkestrering på tvers av eksisterende produkter)

**Anbefalt prioritering:**
1. Avklaring og harmonisering av juridisk grunnlag for elevdatadeling på tvers av forvaltningsnivå
2. Etabler felles semantisk modell: felles begreper og informasjonsmodell for overgangsdata, med Begrepskatalogen som plattform
3. Pilot på hendelsesdrevet overgang basert på Altinn Events og Dialogporten som orkestrerende lag

---

# Arkitekturassistert analyse av utviklingsbehov

## 1. Formål

- Analyseformål: Vurdere hvilke kapabiliteter, prinsipper og produkter som er relevante for å adressere strukturelle samhandlingsbarrierer i overgangen mellom skolenivåer innen oppvekst og utdanning.
- Beslutning analysen skal understøtte: Prioritering av arkitekturtiltak og gjenbruksmuligheter i porteføljearbeid for sektoren.
- Avgrensning: Analysen dekker nasjonalt og sektornivå. Virksomhetsinterne tiltak i kommuner, fylkeskommuner eller direktorater er ikke i scope.

## 2. Input / casebeskrivelse

- Case-tittel: Overgang fra ungdomsskole til videregående og tilgjengeliggjøring av resultater fra videregående opplæring
- Kort casebeskrivelse: To komplementære caser som begge handler om brudd i informasjonsflyt i sentrale overganger for barn og unge. Case 1 adresserer overgangen fra ungdomsskole til videregående, som også innebærer skifte i forvaltningsansvar fra kommune til fylkeskommune. Case 2 adresserer tilgjengeliggjøring av resultater fra videregående, særlig inn mot videre utdanning, arbeid og oppfølgingstjenester.
- Berørte livshendelser / tjenester / overganger: Overgang grunnskole–videregående, overgang videregående–høyere utdanning/arbeid/oppfølging, pedagogisk dokumentasjon og tilrettelegging, oppfølgingstjenesten (OT)
- Hovedutfordring i caset: Relevant informasjon følger ikke eleven ved overgang mellom skoleslag og forvaltningsnivå. Dette skyldes fragmenterte fagsystemer, uklare ansvarslinjer, manglende felles begreper og usikkerhet om hjemmelsgrunnlag for informasjonsdeling.
- Kildemateriale brukt: Innlevert casebeskrivelse og innledende problembeskrivelse fra sektoren

## 3. Målgruppe og styringsnivå

- Primær målgruppe: Ungdom i overgangen mellom skoleslag; elever med behov for tilrettelegging
- Sekundær målgruppe: Foresatte, ansatte i skole og støtteapparat (PPT, OT), fagsystemleverandører
- Styringsnivå: Nasjonalt og sektornivå
- Viktig avgrensning for tiltak: Tiltakene skal adressere felles rammeverk, standarder og felleskomponenter – ikke interne systemvalg i kommuner eller fylkeskommuner

## 4. Problembilde

### 4.1 Hovedproblem

Overganger mellom ungdomsskole og videregående, og videre fra videregående til neste fase, er ikke støttet av sammenhengende informasjonsflyt. Ansvar for eleven skifter fra kommune til fylkeskommune, men informasjonen om eleven gjør det ikke – verken automatisk eller på en standardisert og sikker måte. Fagsystemer i de to nivåene deler ikke datamodell, begreper eller integrasjonsflate. Usikkerhet rundt juridisk grunnlag for deling gjør at aktørene enten venter, innhenter informasjon på nytt, eller unnlater å videresende relevant dokumentasjon. Konsekvensen er forsinkede tiltak, dobbeltarbeid og økt risiko for frafall, særlig blant elever med tilretteleggingsbehov.

### 4.2 Konsekvenser for målgrupper

- Ungdom starter i ny skole uten at skolen kjenner til behov eller tidligere tiltak
- Elever med tilretteleggingsbehov må forklare sin situasjon på nytt, noe som oppleves som stigmatiserende og slitsomt
- Foresatte fungerer som informasjonsbærere mellom systemer som burde snakke sammen
- Unge som slutter i videregående kan bli borte fra oppfølgingstjenestene fordi overføring av informasjon til OT er manuell og tidkrevende

### 4.3 Konsekvenser for forvaltning og tjenesteutøvelse

- Rådgivere og spesialpedagoger bruker tid på gjeninnhenting av informasjon fremfor veiledning
- Kommuner og fylkeskommuner har ulike systemer og begreper, noe som gir feil og forsinkelser i samhandlingen
- Direktorater og departement mangler systematisk grunnlag for å vurdere om overgangspraksisen er i tråd med regelverket
- Leverandørmarkedet er fragmentert, og det er ingen felles standard å levere mot

## 5. Kapabilitetsanalyse

| Kapabilitet | Relevans | Hva finnes i dag | Identifisert gap | Konsekvens for caset |
|---|---|---|---|---|
| Sluttbrukertjenester: Sammenhengende tjenester | Høy | Sektortjenester finnes fragmentert | Ingen nasjonal tjenestekjede for overgang mellom skoleslag | Elever og foresatte opplever brudd og må koordinere selv |
| Sluttbrukertjenester: Tjenestekjeder | Høy | Ingen etablert på tvers av forvaltningsnivå | Manglende orkestrering av informasjonsflyten | Videresending av pedagogisk dokumentasjon skjer manuelt |
| Sluttbrukertjenester: Proaktive tjenester | Middels | Ikke etablert i utdanning | Ingen automatisk varsling eller handlingstilbud ved overgang | Elever og foresatte informeres ikke proaktivt om rettigheter og frister |
| Datautveksling og integrasjon: Dele data med andre | Høy | eFormidling og Maskinporten finnes. Brukes ikke i utdanning | Kommuner og fylkeskommuner deler ikke elevdata via felles API | Informasjon om elever gjeninnhentes eller mangler ved oppstart |
| Datautveksling og integrasjon: Hendelsesdrevet | Høy | Altinn Events finnes men er ikke integrert i utdanning | Ingen hendelsesbasert varsling ved overgang (f.eks. «elev avslutter ungdomsskole») | Overgangen skjer uten automatisk utløst informasjonsflyt |
| Datautveksling og integrasjon: Meldingsformidling | Middels | eFormidling og FIKS Melding finnes | Ikke integrert i utdanningssektorens arbeidsflyt | Meldingsutveksling er manuell eller proprietær per system |
| Informasjonsforvaltning: Datastyring | Høy | FIKS Digiorden finnes. Ingen felles sektormodell | Uklart hvem som eier og forvalter elevdata i overgangen | Ansvarsforvirring og risiko for personvernbrudd |
| Informasjonsforvaltning: Informasjonsarkitektur | Høy | Begrepskatalogen finnes som plattform | Ingen omforent begrepssett for oppvekst og utdanning er etablert | Ulike begreper i systemene gir feiltolkning og manglende samhandlingsevne |
| Informasjonsforvaltning: Oversikt over datasett | Middels | data.norge.no og Felles datakatalog finnes | Elevrelaterte datasett er ikke registrert og beskrevet nasjonalt | Aktørene kjenner ikke til hvilke data som finnes og kan gjenbrukes |
| Tillit: Tilgangskontroll | Høy | Altinn Autorisasjon og Feide finnes separat | Ingen samlet tilgangsstyring på tvers av forvaltningsnivå for elevdata | Feil aktører kan få tilgang; riktige aktører mangler tilgang |
| Tillit: Samtykke | Høy | Altinn Samtykke finnes | Ikke tilpasset utdanningssektoren eller personvern for barn | Usikkerhet om hva som krever samtykke og hva som kan deles på annet grunnlag |
| Tillit: Representasjon | Middels | Altinn Autorisasjon finnes | Foreldreansvarsforhold er ikke systematisk koblet til utdanningstjenestene | Foresatte kan ikke alltid handle digitalt på vegne av barn i tjenestene |
| Samarbeid: Organisatorisk samhandling | Høy | Faglige nettverk og SLA-rammeverk finnes | Ingen formalisert samhandlingsavtale for overgang mellom kommune og fylkeskommune | Ansvarsovergangen er uformell og avhengig av lokal praksis |
| Juridisk samhandling | Høy | Nasjonalt rammeverk finnes | Uavklart hjemmelsgrunnlag for deling av pedagogisk dokumentasjon på tvers | Aktørene deler ikke informasjon av frykt for regelverksbrudd |
| Strategisk styring: Samordning | Middels | KS og Digdir samarbeider | Ingen tverrsektoriell arkitekturavklaring for utdanningssektoren | Løsninger utvikles ukoordinert lokalt fremfor som felles ressurser |
| Informasjonssikkerhet: Sikring av informasjonsflyt | Høy | Maskinporten og eFormidling finnes | Sensitiv elevdata overføres i dag ofte på usikre eller udokumenterte kanaler | Risiko for uautorisert tilgang eller tap av sensitive opplysninger om barn |

### Oppsummering av kapabilitetsgap

- Viktigste gap 1: Sammenhengende tjenester og tjenestekjeder – ingen nasjonal orkestrering av informasjonsflyten ved overgang mellom skoleslag
- Viktigste gap 2: Juridisk samhandling og datastyring – uavklart hjemmelsgrunnlag og manglende eierskap til elevdata på tvers av forvaltningsnivå
- Viktigste gap 3: Informasjonsforvaltning / informasjonsarkitektur – ingen felles begrepssett eller semantisk modell for oppvekst og utdanning

## 6. Prinsippvurdering

| Prinsipp | Status | Hva finnes i dag | Hvordan caset utfordrer prinsippet |
|---|---|---|---|
| P1: Ta utgangspunkt i brukernes behov | Delvis | Tjenestemål i sektoren er brukerrettede i intensjon | Systemene er bygget rundt organisatoriske siloer, ikke rundt elevens reise. Eleven må tilpasse seg systemene, ikke omvendt |
| P2: Ta arkitekturbeslutninger på rett nivå | Brutt | Noen nasjonale rammer finnes | Avgjørelser om dataflyt og systemintegrasjon tas lokalt av kommuner og fylkeskommuner uten felles rammeverk. Beslutninger som burde løftes til nasjonalt nivå, løses som lokale særtilpasninger |
| P3: Bidra til digitaliseringsvennlige regelverk | Delvis | Digitaliserings- og oppvekststrategier peker på behovet | Regleverket er ikke avklart nok til at aktørene tør dele relevant informasjon. Usikkerhet om hjemmel blokkerer digital samhandling |
| P4: Del og gjenbruk data | Brutt | Folkeregisteret og vitnemålsregistre finnes | Elevdata gjeninnhentes fremfor å gjenbrukes. Ingen godkjente autoritative kilder for pedagogisk dokumentasjon. Kommuner kan ikke effektivt hente data de trenger fra nasjonale kilder |
| P5: Del og gjenbruk løsninger | Brutt | Feide, Altinn Autorisasjon og FIKS-plattformen finnes | Kommuner kjøper fagsystemer ukoordinert. Felleskomponentene er ikke integrert i utdanningssektorens arbeidsflyt. Parallelle særutviklede løsninger dominerer |
| P6: Lag digitale løsninger som støtter samhandling | Brutt | eFormidling, Dialogporten og FIKS finnes | Fagsystemer i grunnskole og videregående er ikke designet for samhandling på tvers. Grensesnittene er proprietære og ikke standardiserte |
| P7: Sørg for tillit til oppgaveløsningen | Delvis | Maskinporten og Feide gir teknisk sikkerhet | Manglende juridisk avklaring og oversikt over informasjonsflyt undergraver tillit. Ansatte er usikre på hva de lovlig kan dele og logge |

### Oppsummering av prinsippvurdering

P4, P5 og P6 er eksplisitt brutt i begge caser. Sektoren preges av lokale særutviklinger, manglende gjenbruk av data og fellesløsninger, og systemer som ikke er designet for samhandling. P3 og P7 er delvis oppfylt, men blokkert av uavklart hjemmelsgrunnlag. Prinsippbruddene er gjensidig forsterkende: uklart regelverk (P3) hindrer datadeling (P4), som igjen hindrer sammenhengende tjenester (P6).

## 7. Produktvurdering

### 7.1 Vurderte produkter fra katalogen

| Produkt | Produktkategori | Relevans for caset | Kan brukes direkte | Bør videreutvikles | Ikke relevant | Begrunnelse |
|---|---|---|---|---|---|---|
| Feide (SIKT-001) | Felleskomponent – autentisering | Høy | Ja | Nei | Nei | Etablert autentiseringsløsning for hele utdanningssektoren. Dekker lærere, elever og ansatte i grunnskole og videregående |
| ID-porten (DIGDIR-001) | Felleskomponent – autentisering | Høy | Ja | Nei | Nei | Autentisering for foresatte og voksne elever over 18. Kobles mot Feide der begge er i bruk |
| Altinn Autorisasjon (DIGDIR-004) | Felleskomponent – autorisasjon | Høy | Ja | Ja | Nei | Representasjon av barn ved foresatte er strukturelt viktig. Tilgangsstyring på tvers av forvaltningsnivå krever tilpasning til sektoren |
| Maskinporten (DIGDIR-002) | Felleskomponent – maskin-til-maskin | Høy | Ja | Nei | Nei | Sikrer maskin-til-maskin-kommunikasjon mellom fagsystemer i kommuner og fylkeskommuner ved datadeling |
| Altinn Events (DIGDIR-010) | Felleskomponent – hendelsestjeneste | Høy | Ja | Nei | Nei | Hendelsesdrevet overgang («elev avslutter ungdomsskole», «opptak bekreftet») er et sentralt behov som kan dekkes av Events |
| Dialogporten (DIGDIR-020) | Fellesløsning – dialogtjeneste | Høy | Ja | Nei | Nei | Tverrgående dialogmodell som kan koble elev, foresatte, ungdomsskole og videregående i ett felles dialoglag |
| Altinn Melding (DIGDIR-021) | Fellesløsning – korrespondansetjeneste | Middels | Ja | Nei | Nei | Strukturert meldingsutveksling mellom kommunale og fylkeskommunale systemer |
| Altinn Varsling (DIGDIR-022) | Fellesløsning – varslingstjeneste | Middels | Ja | Nei | Nei | Varsle elever og foresatte om søknadsfrister, vedtak og oppfølging |
| Digital postkasse (DIGDIR-009) | Felleskomponent – utsendingstjeneste | Middels | Ja | Nei | Nei | Kommunikasjon av vedtak og dokumentasjon til elever og foresatte |
| Begrepskatalog (DIGDIR-012) | Fellesløsning – begrepsbeskrivelse | Høy | Nei | Ja | Nei | Plattformen finnes, men felles begrepssett for oppvekst og utdanning er ikke etablert som innhold. Sektoren bør bidra til å fylle innholdet |
| Felles datakatalog (DIGDIR-011) | Fellesløsning – metadataplattform | Middels | Ja | Nei | Nei | Kan brukes til å beskrive og registrere elevrelaterte datasett på tvers av aktører |
| API-katalog (DIGDIR-015) | Fellesløsning – API-oversikt | Middels | Ja | Nei | Nei | Kan brukes til å registrere og publisere API-er for elevdatadeling |
| data.altinn.no (DIGDIR-015) | Fellesløsning – kontrollert datadeling | Middels | Ja | Nei | Nei | Kontrollert deling av elevdata med hjemmel mellom autoriserte aktører |
| FIKS-plattformen (KS-001) | Plattform – kommunal integrasjon | Høy | Ja | Nei | Nei | Kommunal integrasjonsplattform som kobler fagsystemer mot nasjonale tjenester |
| FIKS Melding (KS-002) | Fellesløsning – meldingsutveksling | Middels | Ja | Nei | Nei | Aktuell for meldingsutveksling fra kommunale fagsystemer |
| FIKS Folkeregister (KS-008) | Fellesløsning – registertilgang | Høy | Ja | Nei | Nei | Kommunal tilgang til Folkeregisteret for grunndata om elever og foresatte |
| Folkeregisteret (SKATT-001) | Register – persondata | Høy | Ja | Nei | Nei | Autoritativ kilde for grunndata om elever og foresatte |
| Nasjonal vitnemålsdatabase (SIKT-004) | Register – vitnemål | Høy (case 2) | Ja | Nei | Nei | Direkte relevant for case 2: autorisert kilde for resultater fra videregående |
| Vitnemålsportalen (SIKT-005) | Portal – deling av vitnemål | Høy (case 2) | Ja | Nei | Nei | Direkte relevant for case 2: elever kan dele dokumentasjon med arbeidsgivere og høyere utdanning |
| Opptaksløsninger (SIKT-003) | Fellesløsning – opptak | Høy (case 2) | Ja | Nei | Nei | Direkte relevant for case 2: tar imot resultater fra videregående som grunnlag for opptak til høyere utdanning |
| Nasjonalt utdanningsregister (SIKT-006) | Register – utdanningstilbud | Middels | Ja | Nei | Nei | Autoritativ kilde for skoler og utdanningstilbud – relevant for å identifisere mottakende institusjon |
| Felles studentsystem (SIKT-002) | Plattform – studentdata | Lav (case 2) | Nei | Nei | Ja | Relevant for høyere utdanning, men ikke for overgangen fra videregående i seg selv |
| eFormidling (DIGDIR-007) | Fellesløsning – transportlag | Middels | Nei | Ja | Nei | Kan være aktuelt som transportlag mellom fagsystemer, men er ikke integrert i utdanning og er ikke alene tilstrekkelig |
| eInnsyn (DIGDIR-006) | Fellesløsning – innsynsløsning | Lav | Nei | Nei | Ja | Ikke relevant for den operative informasjonsflyten i overgangen |
| Norge.no (DIGDIR-016) | Portal – innbyggerportal | Lav | Nei | Nei | Ja | Generell informasjonskanal med begrenset relevans for dataflyt |
| eSignering (DIGDIR-003) | Felleskomponent – signering | Lav | Nei | Nei | Ja | Ikke sentralt for informasjonsflyten i overgangen |

### 7.2 Oppsummering: hva finnes, hva kan gjenbrukes, hva må videreutvikles

- Hva finnes: Autentisering (Feide, ID-porten), autorisasjon og representasjon (Altinn Autorisasjon), hendelsesdrevet infrastruktur (Altinn Events), dialoglag (Dialogporten), meldingsformidling (Altinn Melding, FIKS Melding), kommunal integrasjon (FIKS-plattformen), grunndata (Folkeregisteret, FIKS Folkeregister), vitnemål og opptaksinfrastruktur (SIKT-produktene for case 2)
- Hva kan gjenbrukes direkte: Feide, ID-porten, Maskinporten, Altinn Events, Dialogporten, Altinn Varsling, Altinn Melding, FIKS-plattformen, FIKS Folkeregister, Nasjonal vitnemålsdatabase, Vitnemålsportalen, Opptaksløsninger
- Hva må videreutvikles: Altinn Autorisasjon (tilpasning til representasjon av barn i utdanning), Begrepskatalog (innhold for oppvekst og utdanning må etableres)
- Hva er ikke relevant i dette caset: Felles studentsystem (FS), eInnsyn, Norge.no, eSignering

### 7.3 Eksplisitte mangler og behov for nye/sammensatte løsninger

| Identifisert mangel | Hvorfor mangelen oppstår | Konsekvens hvis ikke løst | Forslag til ny/sammensatt løsning | Kan bygge på eksisterende produkter |
|---|---|---|---|---|
| Nasjonal overgangsprotokoll og semantisk modell for pedagogisk dokumentasjon | Ingen autoritativ kilde eller standardisert format for overføring av tilretteleggingsdokumenter, IOP og historikk mellom skoleslag. Ingen eksisterende produkt dekker dette innholdet | Informasjon om tilrettelegging når ikke frem til ny skole – økt risiko for frafall | Felles informasjonsmodell og datastandardisering for overgang, forvaltet som nasjonal ressurs | Begrepskatalog (plattform), Felles datakatalog, Maskinporten, Altinn Events |
| Samtykkehåndtering tilpasset deling av sensitive opplysninger om barn | Altinn samtykke og Altinn Autorisasjon er ikke tilpasset utdanningssektorens behov, særlig for sensitive opplysninger om barn under 18 og forholdet mellom barnets rettigheter og foreldreansvar | Aktørene er usikre og velger ikke å dele – nødvendig informasjon mangler i overgangen | Sektorprofil for samtykke og representasjon i utdanning, bygget på Altinn Autorisasjon | Altinn Autorisasjon (DIGDIR-004), ID-porten (DIGDIR-001), Feide (SIKT-001) |
| Hendelsesbasert overgangsflyt (orkestrering) | Det finnes hendelsesinfrastruktur (Altinn Events) og dialoglag (Dialogporten), men ingen sammenhengende tjenestekjede er orkestrert for overgangen | Overgangen forblir manuell – informasjon flyter ikke automatisk ved kjent hendelse | Sammensatt tjenestekjede basert på Altinn Events som trigger, Dialogporten som dialoglag, Maskinporten for sikker datautveksling | Altinn Events (DIGDIR-010), Dialogporten (DIGDIR-020), Maskinporten (DIGDIR-002), Altinn Autorisasjon (DIGDIR-004) |
| Felles begrepsmodell for oppvekst og utdanning | Begrepskatalogen finnes som plattform, men innholdet for sektoren er ikke etablert. Hvert fagsystem bruker egne termer | Systemene forstår ikke hverandre – manuell oversettelse og feiltolkning vedvarer | Etablering av autoritativt begrepssett for oppvekst og utdanning i nasjonal Begrepskatalog | Begrepskatalog (DIGDIR-012), Felles datakatalog (DIGDIR-011) |

## 8. Tiltak prioritert etter effekt

| Tiltak | Type | Forventet effekt | Tidshorisont | Avhengigheter | Kobling til kapabilitet/prinsipp/produkt |
|---|---|---|---|---|---|
| Avklare juridisk hjemmelsgrunnlag for deling av pedagogisk dokumentasjon | Avklaring | Høy | Kort | Utdanningsdirektorat, KDD, KS | Juridisk samhandling / P3 / Altinn Autorisasjon |
| Etablere felles begrepssett for oppvekst og utdanning i Begrepskatalogen | Nyutvikling (innhold) | Høy | Middels | Sektoren, Digdir, SIKT | Informasjonsforvaltning: Oversikt over begreper / P4 / Begrepskatalog (DIGDIR-012) |
| Definere og standardisere datamodell for overgangsdata | Avklaring + nyutvikling | Høy | Middels | Juridisk avklaring først | Informasjonsforvaltning: Informasjonsarkitektur / P4 / Felles datakatalog (DIGDIR-011) |
| Pilotere hendelsesdrevet overgang med Altinn Events og Dialogporten | Gjenbruk + sammensatt | Høy | Middels | Datamodell og juridisk avklaring | Sluttbrukertjenester: Tjenestekjeder / P6 / Altinn Events (DIGDIR-010) + Dialogporten (DIGDIR-020) + Maskinporten (DIGDIR-002) |
| Integrere FIKS-plattformen og Maskinporten for sikker elevdatadeling mellom kommuner og fylkeskommuner | Gjenbruk | Middels | Middels | Datamodell | Datautveksling og integrasjon / P4, P5 / FIKS-plattformen (KS-001) + Maskinporten (DIGDIR-002) |
| Etablere sektorprofil for representasjon av barn i Altinn Autorisasjon | Videreutvikling | Middels | Middels | Juridisk avklaring | Tillit: Representasjon og samtykke / P7 / Altinn Autorisasjon (DIGDIR-004) |
| Koble Nasjonal vitnemålsdatabase og Vitnemålsportalen mot oppfølgingstjenestene (OT) (case 2) | Gjenbruk | Middels | Kort | Juridisk grunnlag for OT-tilgang | Datautveksling og integrasjon / P4 / SIKT-004 + SIKT-005 |
| Integrere resultater fra videregående i Opptaksløsninger via standard API (case 2) | Gjenbruk | Høy | Kort | Allerede delvis etablert | Sluttbrukertjenester: Sammenhengende tjenester / P4, P5 / Opptaksløsninger (SIKT-003) + NVB (SIKT-004) |

### Prioritert liste

1. Juridisk avklaring av hjemmelsgrunnlag for deling av pedagogisk dokumentasjon – dette blokkerer alle tekniske tiltak og er forutsetning for å komme videre. Gjennomføres som sektorspesifikk avklaring med Utdanningsdirektorat, KDD og KS.
2. Felles begrepssett og datamodell for overgangsdata – uten en semantisk modell kan ikke systemer integreres meningsfullt. Grunnleggende premiss for all videre samhandling.
3. Pilotere hendelsesdrevet overgang med eksisterende felleskomponenter – demonstrerer at orkestrering er mulig med det som finnes, gir lærdom og bygger tillit til tilnærmingen.

## 9. Strategisk vurdering

- Betydning for porteføljeprioritering: Begge case synliggjør at utdanningssektoren er underrepresentert i gjenbruk av nasjonale felleskomponenter. En arkitekturavklaring for sektoren vil kunne gi rask effekt ved å synliggjøre hva som kan hentes ned fra eksisterende produktkatalog.
- Betydning for nasjonal arkitektur / felles retning: Caset er et typisk eksempel på at kapabiliteter finnes (Events, Dialogporten, Maskinporten), men at sektormangel på felles semantikk og juridisk avklaring blokkerer gjenbruk. Det peker på behovet for sektorvise arkitekturprofiler som bru mellom nasjonale felleskomponenter og sektorenes egne systemer og behov.
- Behov for samordning mellom aktører: Krever samordning mellom Utdanningsdirektorat (regelverk og standarder), KS (kommunal sektor og FIKS-plattformen), Digdir (felleskomponenter), SIKT (utdanningsspesifikke produkter) og fylkeskommunene som tjenesteytere.

## 10. Konklusjon

Begge caser er rotfestet i de samme tre strukturelle barrierene: fragmentert datainfrastruktur, manglende felles begreper og semantisk modell, og uavklart juridisk grunnlag for informasjonsdeling. Det finnes allerede et godt sett med felleskomponenter i produktkatalogen som kan løse det tekniske laget – Feide, Maskinporten, Altinn Events, Dialogporten, FIKS-plattformen og SIKT-produktene for resultatdeling – men potensialet er ikke realisert fordi de to ikke-tekniske barrierene ikke er adressert. Det viktigste første steget er juridisk og semantisk avklaring, ikke teknisk nyutvikling. For case 2 er gjenbruksmulighetene sterkest og mest umiddelbare: Nasjonal vitnemålsdatabase, Vitnemålsportalen og Opptaksløsninger er allerede operative og kan kobles tettere mot oppfølgingstjenestene med relativt begrenset innsats. For case 1 er orkestrering av overgangen en mer sammensatt oppgave som krever en felles semantisk modell og juridisk avklaring som fundament, og deretter en pilot på hendelsesdrevet tjenestekjede som demonstrerer at det er mulig å realisere sømløs overgang med eksisterende felleskomponenter.
