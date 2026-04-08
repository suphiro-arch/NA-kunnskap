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
relatert: briefs/arbeidsstyring-og-handover/2026-03-31-case-overgang-ungdomsskole-videregaende-v2.md
---

# TEST-analyse - kortversjon

**Case:** Tilgjengeliggjøring av resultater fra videregående opplæring

**Hovedfunn:**
Dette caset har bedre produktdekning enn case 1. Det finnes allerede nasjonale produkter for lagring, kvalitetssikring, deling og videre bruk av resultater fra videregående opplæring. Hovedutfordringen er ikke primært mangel på produkter, men uklar kobling mellom eksisterende resultatinfrastruktur og aktører som trenger informasjonen videre, særlig oppfølgingstjenester, arbeidsgivere og noen overgangsløp utenfor høyere utdanning.

**Viktigste kapabilitetsgap:**
- Datautveksling og integrasjon: Bruke data fra andre / Dele data med andre
- Sluttbrukertjenester: Sammenhengende tjenester
- Tillit: Tilgangskontroll og representasjon

**Mest relevante produkter for gjenbruk:**
- Nasjonal vitnemålsdatabase (SIKT-004)
- Vitnemålsportalen (SIKT-005)
- Opptaksløsninger (SIKT-003)
- Feide (SIKT-001)
- ID-porten (DIGDIR-001)
- Altinn Autorisasjon (DIGDIR-004)

**Hva mangler:**
- Tydelig modell for viderebruk av resultatinformasjon utenfor etablerte opptaksløp
- Bedre tilgangs- og formålsstyring for aktører som trenger resultatinformasjon i oppfølging av unge
- Standardisert grenseflate mellom resultatinfrastruktur og oppfølgingstjenester

**Anbefalt prioritering:**
1. Kartlegg og avklar hvilke aktører utenfor opptaksløp som skal ha tilgang til hvilke resultater og på hvilket grunnlag
2. Etabler standardisert delingsmønster for resultatinformasjon til oppfølgingstjenester
3. Vurder sektorprofil for autorisasjon og representasjon der foresatte eller andre handler på vegne av unge

---

# Arkitekturassistert analyse: tilgjengeliggjøring av resultater fra videregående opplæring

## 1. Formål

- Analyseformål: Vurdere hvilke kapabiliteter, prinsipper og produkter som er relevante for å gjøre resultater fra videregående opplæring tilgjengelige på en bedre og mer sammenhengende måte.
- Beslutning analysen skal understøtte: Prioritering av tiltak for gjenbruk og videreutvikling av eksisterende nasjonal resultatinfrastruktur.
- Avgrensning: Analysen fokuserer på tilgjengeliggjøring og viderebruk av resultater fra videregående opplæring. Selve overgangen fra ungdomsskole til videregående behandles i relatert analyse.

## 2. Input / casebeskrivelse

- Case-tittel: Tilgjengeliggjøring av resultater fra videregående opplæring
- Kort casebeskrivelse: Caset handler om hvordan resultater fra videregående opplæring kan gjøres tilgjengelige på en bedre og mer sammenhengende måte for aktører som trenger informasjonen i videre oppfølging av unge. Resultater omfatter status for gjennomført opplæring, fullføring, kompetanse, vurderinger og dokumentasjon av oppnådd nivå.
- Berørte livshendelser: Avslutning av videregående opplæring, overgang til høyere utdanning, arbeid eller oppfølgingstjenester
- Hovedutfordring: Resultatinformasjon er spredt på flere systemer og tilgjengelig i ulike formater. Det er ikke alltid tydelig hvem som har tilgang til hvilken informasjon, eller hvordan den kan brukes videre i oppfølging og veiledning.
- Kildemateriale: Innlevert casebeskrivelse og innledende problembeskrivelse fra sektoren

## 3. Målgruppe og styringsnivå

- Primær målgruppe: Unge som avslutter eller er i ferd med å avslutte videregående opplæring
- Sekundær målgruppe: Foresatte der relevant, ansatte i tjenester som veileder og følger opp unge, fagsystemleverandører
- Styringsnivå: Nasjonalt og sektornivå
- Viktig avgrensning: Tiltakene skal rette seg mot gjenbruk, standardisering og styring av nasjonal resultatinfrastruktur – ikke lokale fagsystemanskaffelser

## 4. Problembilde

### 4.1 Hovedproblem

Resultater fra videregående opplæring er i praksis tilgjengelige, men ikke nødvendigvis tilgjengelige for riktig aktør, til riktig tid og i riktig form. Det finnes nasjonale løsninger for vitnemål og opptak, men disse dekker ikke automatisk alle behov for oppfølging, viderebruk og veiledning utenfor de mest etablerte løpene. Ulike aktører har behov for samme informasjon til forskjellige formål, men tilgangsgrunnlag, grensesnitt og forståelse av informasjonen er ikke samordnet nok. Dette skaper manuelle prosesser, usikkerhet og belastning for unge som selv må dokumentere eller forklare sin status flere ganger.

### 4.2 Konsekvenser for målgrupper

- Unge må selv dokumentere eller forklare egen status flere ganger i overgang til arbeid, høyere utdanning eller oppfølgingstjenester
- Foresatte får begrenset oversikt over hva som finnes av dokumentasjon og hvilke aktører som kan bruke den
- Unge i sårbare overgangsløp kan oppleve forsinket eller mangelfull oppfølging

### 4.3 Konsekvenser for forvaltning og tjenesteutøvelse

- Ansatte i veilednings- og oppfølgingstjenester må innhente eller verifisere informasjon manuelt
- Aktører bruker de samme opplysningene til ulike formål uten felles delingsmønster
- Risiko for feil eller misforståelser øker når resultatinformasjon hentes fra ulike kilder og formater

## 5. Kapabilitetsanalyse

| Kapabilitet | Relevans | Hva finnes i dag | Identifisert gap | Konsekvens for caset |
|---|---|---|---|---|
| Datakilder: Grunndata | Høy | Nasjonal vitnemålsdatabase gir autoritativ kilde for vitnemål | Ikke alle resultatformer og all kompetansedokumentasjon er like tilgjengelig i ett samlet mønster | Ulike aktører forholder seg til ulike kilder og formater |
| Datautveksling og integrasjon: Dele data med andre | Høy | NVB, Vitnemålsportalen og opptaksløsninger deler resultatinformasjon i etablerte løp | Ikke tydelig standardisert delingsmønster til alle relevante oppfølgingstjenester | Informasjon må innhentes manuelt eller via særordninger |
| Datautveksling og integrasjon: Bruke data fra andre | Høy | Høyere utdanning bruker allerede resultatinformasjon maskinelt | Flere aktører utenfor opptaksløp mangler enkel og standardisert tilgang | Viderebruk utenfor etablerte løp blir treg og usikker |
| Sluttbrukertjenester: Sammenhengende tjenester | Høy | Vitnemålsportalen gir sluttbrukerflate for deling av dokumentasjon | Ikke en sammenhengende brukerreise på tvers av utdanning, arbeid og oppfølging | Unge opplever at de må starte på nytt i hvert nytt løp |
| Tillit: Tilgangskontroll | Høy | Feide og Altinn Autorisasjon finnes | Ikke tydelig modell for hvem som skal ha tilgang til hvilke resultater til hvilke formål | Usikkerhet gir enten for mye eller for lite deling |
| Tillit: Representasjon | Middels | ID-porten og Altinn Autorisasjon finnes | Uklart når foresatte skal kunne handle på vegne av unge i resultatløp | Manglende støtte for legitime representasjonsbehov |
| Juridisk samhandling | Høy | Etablerte opptaksløp har hjemler og praksis | Viderebruk i oppfølging og arbeidsliv er ikke nødvendigvis like tydelig avklart | Aktører avstår fra bruk av data de kunne hatt nytte av |
| Informasjonsforvaltning: Oversikt over begreper | Middels | Begrepskatalog og Felles datakatalog finnes | Resultatbegreper og formål kan tolkes ulikt | Økt risiko for misforståelser om hva resultatene betyr |

### Oppsummering av kapabilitetsgap

- Viktigste gap 1: Deling og viderebruk av resultatinformasjon utenfor etablerte opptaksløp
- Viktigste gap 2: Tilgangsstyring og juridisk avklaring for ulike formål og aktører
- Viktigste gap 3: Sammenhengende brukerreise for unge som går videre til arbeid eller oppfølgingstjenester

## 6. Prinsippvurdering

| Prinsipp | Status | Hva finnes i dag | Hvordan caset utfordrer prinsippet |
|---|---|---|---|
| P1: Ta utgangspunkt i brukernes behov | Delvis | Vitnemålsportalen er brukerrettet og gir tydelig sluttbrukerverdi | Brukerreisen er fortsatt fragmentert når unge går videre til andre løp enn de mest etablerte |
| P2: Ta arkitekturbeslutninger på rett nivå | Delvis | Nasjonale løsninger er etablert for resultater og opptak | Noen beslutninger om viderebruk ser fortsatt ut til å være spredt mellom flere aktører og formål |
| P3: Bidra til digitaliseringsvennlige regelverk | Delvis | For høyere utdanning er deling i stor grad avklart | For andre formål er tilgangsgrunnlag og bruk mindre tydelig |
| P4: Del og gjenbruk data | Delvis | Resultater deles allerede gjennom NVB og Vitnemålsportalen | Gjenbruket stopper delvis ved sektorgrenser eller formålsgrenser |
| P5: Del og gjenbruk løsninger | Oppfylt/delvis | Flere nasjonale løsninger finnes allerede og brukes | Gjenbrukspotensialet kan økes ved å bruke samme grunnlag i flere oppfølgingsløp |
| P6: Lag digitale løsninger som støtter samhandling | Delvis | Produktene støtter samhandling i etablerte løp | Samhandlingen er mindre utviklet mot arbeid og oppfølgingstjenester |
| P7: Sørg for tillit til oppgaveløsningen | Delvis | Kvalitetssikrede resultater og etablert identitetsinfrastruktur finnes | Tydeligere tilgangsregler og formålsstyring trengs for flere brukstilfeller |

### Oppsummering av prinsippvurdering

Dette caset står sterkere enn case 1 på P4 og P5 fordi sentrale nasjonale løsninger allerede finnes og brukes. Hovedutfordringen ligger i å utvide gjenbruket kontrollert til flere formål og aktører, uten å svekke P7. Prinsippbruddene er derfor mindre grunnleggende enn i overgangscaset, men de er fortsatt tydelige i randsonene rundt eksisterende opptaksløp.

## 7. Produktvurdering

### 7.1 Vurderte produkter fra katalogen

| Produkt | Produktkategori | Relevans | Kan brukes direkte | Bør videreutvikles | Ikke relevant | Begrunnelse |
|---|---|---|---|---|---|---|
| Nasjonal vitnemålsdatabase (SIKT-004) | Register – vitnemål | Høy | Ja | Nei | Nei | Autoritativ nasjonal kilde for resultater fra videregående opplæring |
| Vitnemålsportalen (SIKT-005) | Portal – deling av vitnemål | Høy | Ja | Nei | Nei | Direkte relevant sluttbrukerflate for deling av dokumentasjon |
| Opptaksløsninger (SIKT-003) | Fellesløsning – opptak | Høy | Ja | Nei | Nei | Etablert viderebruk av resultater i opptak til høyere utdanning |
| Feide (SIKT-001) | Felleskomponent – autentisering | Middels | Ja | Nei | Nei | Relevante brukergrupper i utdanning kan autentiseres gjennom etablert sektorløsning |
| ID-porten (DIGDIR-001) | Felleskomponent – autentisering | Middels | Ja | Nei | Nei | Relevante for unge over 18 og foresatte i noen løp |
| Altinn Autorisasjon (DIGDIR-004) | Felleskomponent – autorisasjon | Middels | Ja | Ja | Nei | Relevant der resultatinformasjon skal brukes av andre på vegne av den unge eller under tydelig tilgangsstyring |
| Begrepskatalog (DIGDIR-012) | Fellesløsning – begrepsbeskrivelse | Middels | Nei | Ja | Nei | Kan gi semantisk ryddighet i forståelsen av resultater og kompetanse, men innhold må etableres |
| Felles datakatalog (DIGDIR-011) | Fellesløsning – metadataplattform | Lav/middels | Ja | Nei | Nei | Kan synliggjøre datasett og beskrivelser, men er ikke i seg selv delingsmotoren |
| API-katalog (DIGDIR-013) | Fellesløsning – API-oversikt | Lav/middels | Ja | Nei | Nei | Relevant hvis resultattjenester skal eksponeres som standardiserte API-er |
| data.altinn.no (DIGDIR-015) | Fellesløsning – kontrollert datadeling | Middels | Ja | Nei | Nei | Aktuell som mønster for kontrollert deling til autoriserte aktører utenfor dagens løp |
| Dialogporten (DIGDIR-020) | Fellesløsning – dialogtjeneste | Lav | Nei | Nei | Ja | Ikke kjerneprodukt for resultatinformasjon, som primært er register- og dokumentasjonsbasert |
| Altinn Events (DIGDIR-010) | Felleskomponent – hendelsestjeneste | Lav/middels | Nei | Nei | Ja | Kan være nyttig som supplerende mønster, men er ikke sentralt for selve resultatinformasjonen |
| FIKS-plattformen (KS-001) | Plattform – kommunal integrasjon | Middels | Ja | Nei | Nei | Relevant hvis kommunale oppfølgingstjenester skal bruke resultatinformasjon gjennom standardiserte integrasjoner |
| Felles studentsystem (SIKT-002) | Plattform – studentdata | Lav | Nei | Nei | Ja | Relevant først etter overgang til høyere utdanning, ikke for selve resultatinformasjonen fra videregående |
| eInnsyn (DIGDIR-006) | Fellesløsning – innsynsløsning | Lav | Nei | Nei | Ja | Ikke relevant for primærbehovet |
| eSignering (DIGDIR-003) | Felleskomponent – signering | Lav | Nei | Nei | Ja | Ikke sentral for dette caset |

### 7.2 Oppsummering

- Hva finnes: Det finnes allerede en sterk nasjonal kjerne for resultatinformasjon gjennom NVB, Vitnemålsportalen og Opptaksløsninger
- Hva kan gjenbrukes direkte: NVB, Vitnemålsportalen, Opptaksløsninger, Feide, ID-porten og i noen grad Altinn Autorisasjon og FIKS-plattformen
- Hva må videreutvikles: Altinn Autorisasjon for enkelte representasjons- og tilgangsscenarier, Begrepskatalog som semantisk grunnlag for resultater og kompetanse
- Hva er ikke relevant: Dialogporten, eInnsyn, eSignering og i stor grad Altinn Events for dette konkrete caset

### 7.3 Eksplisitte mangler

| Identifisert mangel | Hvorfor mangelen oppstår | Konsekvens hvis ikke løst | Forslag | Bygger på |
|---|---|---|---|---|
| Standardisert delingsmønster til oppfølgingstjenester | Eksisterende resultatinfrastruktur er sterkest mot opptak og dokumentasjon, ikke nødvendigvis mot oppfølging av unge | Oppfølgingstjenester må innhente eller verifisere informasjon manuelt | Etablere standardisert grenseflate og tilgangsmodell for oppfølgingstjenester | NVB (SIKT-004), FIKS-plattformen (KS-001), data.altinn.no (DIGDIR-015) |
| Tydelig formålsstyring for viderebruk av resultater | Samme informasjon brukes til flere formål, men tilgangsgrunnlag er ikke nødvendigvis tydelig nok for alle aktører | Enten underbruk eller for risikofylt deling | Tydelig sektorprofil for tilgang og formål | Altinn Autorisasjon (DIGDIR-004), ID-porten (DIGDIR-001), Feide (SIKT-001) |
| Felles begrepssett for resultater, kompetanse og status | Resultatbegreper kan tolkes ulikt i ulike tjenester og sektorer | Misforståelser i viderebruk og dårligere datakvalitet | Etablere begrepsarbeid i Begrepskatalogen | Begrepskatalog (DIGDIR-012), Felles datakatalog (DIGDIR-011) |

## 8. Tiltak prioritert etter effekt

| Tiltak | Type | Effekt | Tidshorisont | Avhengigheter | Kobling |
|---|---|---|---|---|---|
| Kartlegg hvilke aktører og formål utenfor opptaksløp som trenger resultatinformasjon | Avklaring | Høy | Kort | Utdanningsdirektorat, SIKT, relevante sektorer | Juridisk samhandling / P3 |
| Etabler standardisert delingsmønster for resultatinformasjon til oppfølgingstjenester | Gjenbruk + videreutvikling | Høy | Middels | Kartlegging og juridisk avklaring | Datautveksling og integrasjon / P4 / NVB + FIKS + data.altinn.no |
| Vurder sektorprofil for autorisasjon og representasjon | Videreutvikling | Middels | Middels | Juridisk avklaring | Tillit / P7 / Altinn Autorisasjon |
| Etabler felles begrepssett for resultater og kompetanse | Nyutvikling (innhold) | Middels | Middels | Sektorfaglig forankring | Informasjonsforvaltning / P4 / Begrepskatalog |
| Gjør resultatinfrastruktur mer synlig som gjenbrukbar nasjonal byggestein utover opptaksløp | Gjenbruk | Middels | Kort | Samordning mellom SIKT og nasjonale aktører | P5 / NVB, Vitnemålsportalen, Opptaksløsninger |

### Prioritert liste

1. Avklar hvilke aktører og formål som faktisk trenger resultatinformasjon utenfor dagens etablerte opptaksløp
2. Etabler standardisert og hjemlet delingsmønster til oppfølgingstjenester og andre legitime brukere
3. Bruk Begrepskatalog og autorisasjonsprofilering til å rydde i semantikk og tilgangsregler

## 9. Strategisk vurdering

- Betydning for porteføljeprioritering: Dette caset viser at sektoren allerede har nasjonal resultatinfrastruktur med høy verdi. Prioriteringen bør derfor være å utvide og synliggjøre gjenbruk, ikke å starte med nye grunnløsninger.
- Betydning for nasjonal arkitektur: Caset er et godt eksempel på et område der produktkatalogen faktisk gir sterke treff. Det viser verdien av å bygge videre på eksisterende register- og delingsressurser fremfor å tenke nytt fra bunnen.
- Behov for samordning: Krever særlig samspill mellom SIKT, Utdanningsdirektorat, oppfølgingstjenester, eventuelle arbeidslivsaktører og Digdir der tilgangsstyring og kontrollert deling blir aktuelt.

## 10. Konklusjon

Tilgjengeliggjøring av resultater fra videregående opplæring er et case der den nasjonale produktkatalogen treffer godt. Nasjonal vitnemålsdatabase, Vitnemålsportalen og Opptaksløsninger dekker allerede sentrale behov for kvalitetssikring, deling og viderebruk av resultatinformasjon. Det viktigste forbedringsbehovet er derfor ikke å etablere nye grunnprodukter, men å utvide viderebruken kontrollert til flere legitime formål og aktører. Det krever særlig avklaring av tilgangsgrunnlag, tydeligere formålsstyring og et standardisert mønster for deling til oppfølgingstjenester og andre mottakere utenfor etablerte opptaksløp. Samlet sett viser caset at oppsettet fungerer godt når produktkatalogen faktisk har modne og tydelige produkter i domenet.
