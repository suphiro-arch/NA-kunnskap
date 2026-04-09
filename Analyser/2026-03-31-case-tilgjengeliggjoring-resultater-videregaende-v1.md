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
relatert: briefs/arbeidsstyring-og-handover/2026-03-31-case-overgang-ungdomsskole-videregaende-v2.md
---

# TEST-analyse - kortversjon

**Case:** TilgjengeliggjÃ¸ring av resultater fra videregÃ¥ende opplÃ¦ring

**Hovedfunn:**
Dette caset har bedre produktdekning enn case 1. Det finnes allerede nasjonale produkter for lagring, kvalitetssikring, deling og videre bruk av resultater fra videregÃ¥ende opplÃ¦ring. Hovedutfordringen er ikke primÃ¦rt mangel pÃ¥ produkter, men uklar kobling mellom eksisterende resultatinfrastruktur og aktÃ¸rer som trenger informasjonen videre, sÃ¦rlig oppfÃ¸lgingstjenester, arbeidsgivere og noen overgangslÃ¸p utenfor hÃ¸yere utdanning.

**Viktigste kapabilitetsgap:**
- Datautveksling og integrasjon: Bruke data fra andre / Dele data med andre
- Sluttbrukertjenester: Sammenhengende tjenester
- Tillit: Tilgangskontroll og representasjon

**Mest relevante produkter for gjenbruk:**
- Nasjonal vitnemÃ¥lsdatabase (SIKT-004)
- VitnemÃ¥lsportalen (SIKT-005)
- OpptakslÃ¸sninger (SIKT-003)
- VIGO (NOVARI-004)
- Feide (SIKT-001)
- ID-porten (DIGDIR-001)
- Altinn Autorisasjon (DIGDIR-004)

**Hva mangler:**
- Tydelig modell for viderebruk av resultatinformasjon utenfor etablerte opptakslÃ¸p
- Bedre tilgangs- og formÃ¥lsstyring for aktÃ¸rer som trenger resultatinformasjon i oppfÃ¸lging av unge
- Standardisert grenseflate mellom resultatinfrastruktur og oppfÃ¸lgingstjenester

**Anbefalt prioritering:**
1. Kartlegg og avklar hvilke aktÃ¸rer utenfor opptakslÃ¸p som skal ha tilgang til hvilke resultater og pÃ¥ hvilket grunnlag
2. Etabler standardisert delingsmÃ¸nster for resultatinformasjon til oppfÃ¸lgingstjenester
3. Vurder sektorprofil for autorisasjon og representasjon der foresatte eller andre handler pÃ¥ vegne av unge

---

# Arkitekturassistert analyse: tilgjengeliggjÃ¸ring av resultater fra videregÃ¥ende opplÃ¦ring

## 1. FormÃ¥l

- AnalyseformÃ¥l: Vurdere hvilke kapabiliteter, prinsipper og produkter som er relevante for Ã¥ gjÃ¸re resultater fra videregÃ¥ende opplÃ¦ring tilgjengelige pÃ¥ en bedre og mer sammenhengende mÃ¥te.
- Beslutning analysen skal understÃ¸tte: Prioritering av tiltak for gjenbruk og videreutvikling av eksisterende nasjonal resultatinfrastruktur.
- Avgrensning: Analysen fokuserer pÃ¥ tilgjengeliggjÃ¸ring og viderebruk av resultater fra videregÃ¥ende opplÃ¦ring. Selve overgangen fra ungdomsskole til videregÃ¥ende behandles i relatert analyse.

## 2. Input / casebeskrivelse

- Case-tittel: TilgjengeliggjÃ¸ring av resultater fra videregÃ¥ende opplÃ¦ring
- Kort casebeskrivelse: Caset handler om hvordan resultater fra videregÃ¥ende opplÃ¦ring kan gjÃ¸res tilgjengelige pÃ¥ en bedre og mer sammenhengende mÃ¥te for aktÃ¸rer som trenger informasjonen i videre oppfÃ¸lging av unge. Resultater omfatter status for gjennomfÃ¸rt opplÃ¦ring, fullfÃ¸ring, kompetanse, vurderinger og dokumentasjon av oppnÃ¥dd nivÃ¥.
- BerÃ¸rte livshendelser: Avslutning av videregÃ¥ende opplÃ¦ring, overgang til hÃ¸yere utdanning, arbeid eller oppfÃ¸lgingstjenester
- Hovedutfordring: Resultatinformasjon er spredt pÃ¥ flere systemer og tilgjengelig i ulike formater. Det er ikke alltid tydelig hvem som har tilgang til hvilken informasjon, eller hvordan den kan brukes videre i oppfÃ¸lging og veiledning.
- Kildemateriale: Innlevert casebeskrivelse og innledende problembeskrivelse fra sektoren

## 2.1 Inputgrunnlag og analysetillit

| Vurderingspunkt | Vurdering |
|---|---|
| Inputgrunnlag | Case med tydelig avgrensning og god kobling til etablerte produktomrÃ¥der |
| Datagrunnlag | Moderat; tilstrekkelig for strukturell vurdering, men begrenset for presis nytteestimering uten videre kartlegging |
| Produktgrunnlag | Sterkt; flere modne, operative produkter med hÃ¸y relevans i domenet |
| Samlet analysetillit | Middels til hÃ¸y |

Viktigste usikkerheter:
- Avgrensning av legitime formÃ¥l og aktÃ¸rtilgang utenfor etablerte opptakslÃ¸p
- Samordning mellom nasjonale og sektorspesifikke lÃ¸sninger for viderebruk
- Ulik begrepsforstÃ¥else for resultater, kompetanse og status pÃ¥ tvers av tjenester

## 3. MÃ¥lgruppe og styringsnivÃ¥

- PrimÃ¦r mÃ¥lgruppe: Unge som avslutter eller er i ferd med Ã¥ avslutte videregÃ¥ende opplÃ¦ring
- SekundÃ¦r mÃ¥lgruppe: Foresatte der relevant, ansatte i tjenester som veileder og fÃ¸lger opp unge, fagsystemleverandÃ¸rer
- StyringsnivÃ¥: Nasjonalt og sektornivÃ¥
- Viktig avgrensning: Tiltakene skal rette seg mot gjenbruk, standardisering og styring av nasjonal resultatinfrastruktur â€“ ikke lokale fagsystemanskaffelser

## 4. Problembilde

### 4.1 Hovedproblem

Resultater fra videregÃ¥ende opplÃ¦ring er i praksis tilgjengelige, men ikke nÃ¸dvendigvis tilgjengelige for riktig aktÃ¸r, til riktig tid og i riktig form. Det finnes nasjonale lÃ¸sninger for vitnemÃ¥l og opptak, men disse dekker ikke automatisk alle behov for oppfÃ¸lging, viderebruk og veiledning utenfor de mest etablerte lÃ¸pene. Ulike aktÃ¸rer har behov for samme informasjon til forskjellige formÃ¥l, men tilgangsgrunnlag, grensesnitt og forstÃ¥else av informasjonen er ikke samordnet nok. Dette skaper manuelle prosesser, usikkerhet og belastning for unge som selv mÃ¥ dokumentere eller forklare sin status flere ganger.

### 4.2 Konsekvenser for mÃ¥lgrupper

- Unge mÃ¥ selv dokumentere eller forklare egen status flere ganger i overgang til arbeid, hÃ¸yere utdanning eller oppfÃ¸lgingstjenester
- Foresatte fÃ¥r begrenset oversikt over hva som finnes av dokumentasjon og hvilke aktÃ¸rer som kan bruke den
- Unge i sÃ¥rbare overgangslÃ¸p kan oppleve forsinket eller mangelfull oppfÃ¸lging

### 4.3 Konsekvenser for forvaltning og tjenesteutÃ¸velse

- Ansatte i veilednings- og oppfÃ¸lgingstjenester mÃ¥ innhente eller verifisere informasjon manuelt
- AktÃ¸rer bruker de samme opplysningene til ulike formÃ¥l uten felles delingsmÃ¸nster
- Risiko for feil eller misforstÃ¥elser Ã¸ker nÃ¥r resultatinformasjon hentes fra ulike kilder og formater

## 5. Kapabilitetsanalyse

| Kapabilitet | Relevans | Hva finnes i dag | Identifisert gap | Konsekvens for caset |
|---|---|---|---|---|
| Datakilder: Grunndata | HÃ¸y | Nasjonal vitnemÃ¥lsdatabase gir autoritativ kilde for vitnemÃ¥l | Ikke alle resultatformer og all kompetansedokumentasjon er like tilgjengelig i ett samlet mÃ¸nster | Ulike aktÃ¸rer forholder seg til ulike kilder og formater |
| Datautveksling og integrasjon: Dele data med andre | HÃ¸y | NVB, VitnemÃ¥lsportalen og opptakslÃ¸sninger deler resultatinformasjon i etablerte lÃ¸p | Ikke tydelig standardisert delingsmÃ¸nster til alle relevante oppfÃ¸lgingstjenester | Informasjon mÃ¥ innhentes manuelt eller via sÃ¦rordninger |
| Datautveksling og integrasjon: Bruke data fra andre | HÃ¸y | HÃ¸yere utdanning bruker allerede resultatinformasjon maskinelt | Flere aktÃ¸rer utenfor opptakslÃ¸p mangler enkel og standardisert tilgang | Viderebruk utenfor etablerte lÃ¸p blir treg og usikker |
| Sluttbrukertjenester: Sammenhengende tjenester | HÃ¸y | VitnemÃ¥lsportalen gir sluttbrukerflate for deling av dokumentasjon | Ikke en sammenhengende brukerreise pÃ¥ tvers av utdanning, arbeid og oppfÃ¸lging | Unge opplever at de mÃ¥ starte pÃ¥ nytt i hvert nytt lÃ¸p |
| Tillit: Tilgangskontroll | HÃ¸y | Feide og Altinn Autorisasjon finnes | Ikke tydelig modell for hvem som skal ha tilgang til hvilke resultater til hvilke formÃ¥l | Usikkerhet gir enten for mye eller for lite deling |
| Tillit: Representasjon | Middels | ID-porten og Altinn Autorisasjon finnes | Uklart nÃ¥r foresatte skal kunne handle pÃ¥ vegne av unge i resultatlÃ¸p | Manglende stÃ¸tte for legitime representasjonsbehov |
| Juridisk samhandling | HÃ¸y | Etablerte opptakslÃ¸p har hjemler og praksis | Viderebruk i oppfÃ¸lging og arbeidsliv er ikke nÃ¸dvendigvis like tydelig avklart | AktÃ¸rer avstÃ¥r fra bruk av data de kunne hatt nytte av |
| Informasjonsforvaltning: Oversikt over begreper | Middels | Begrepskatalog og Felles datakatalog finnes | Resultatbegreper og formÃ¥l kan tolkes ulikt | Ã˜kt risiko for misforstÃ¥elser om hva resultatene betyr |

### Oppsummering av kapabilitetsgap

- Viktigste gap 1: Deling og viderebruk av resultatinformasjon utenfor etablerte opptakslÃ¸p
- Viktigste gap 2: Tilgangsstyring og juridisk avklaring for ulike formÃ¥l og aktÃ¸rer
- Viktigste gap 3: Sammenhengende brukerreise for unge som gÃ¥r videre til arbeid eller oppfÃ¸lgingstjenester

## 6. Prinsippvurdering

| Prinsipp | Status | Hva finnes i dag | Hvordan caset utfordrer prinsippet |
|---|---|---|---|
| P1: Ta utgangspunkt i brukernes behov | Delvis | VitnemÃ¥lsportalen er brukerrettet og gir tydelig sluttbrukerverdi | Brukerreisen er fortsatt fragmentert nÃ¥r unge gÃ¥r videre til andre lÃ¸p enn de mest etablerte |
| P2: Ta arkitekturbeslutninger pÃ¥ rett nivÃ¥ | Delvis | Nasjonale lÃ¸sninger er etablert for resultater og opptak | Noen beslutninger om viderebruk ser fortsatt ut til Ã¥ vÃ¦re spredt mellom flere aktÃ¸rer og formÃ¥l |
| P3: Bidra til digitaliseringsvennlige regelverk | Delvis | For hÃ¸yere utdanning er deling i stor grad avklart | For andre formÃ¥l er tilgangsgrunnlag og bruk mindre tydelig |
| P4: Del og gjenbruk data | Delvis | Resultater deles allerede gjennom NVB og VitnemÃ¥lsportalen | Gjenbruket stopper delvis ved sektorgrenser eller formÃ¥lsgrenser |
| P5: Del og gjenbruk lÃ¸sninger | Oppfylt/delvis | Flere nasjonale lÃ¸sninger finnes allerede og brukes | Gjenbrukspotensialet kan Ã¸kes ved Ã¥ bruke samme grunnlag i flere oppfÃ¸lgingslÃ¸p |
| P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling | Delvis | Produktene stÃ¸tter samhandling i etablerte lÃ¸p | Samhandlingen er mindre utviklet mot arbeid og oppfÃ¸lgingstjenester |
| P7: SÃ¸rg for tillit til oppgavelÃ¸sningen | Delvis | Kvalitetssikrede resultater og etablert identitetsinfrastruktur finnes | Tydeligere tilgangsregler og formÃ¥lsstyring trengs for flere brukstilfeller |

### Oppsummering av prinsippvurdering

Dette caset stÃ¥r sterkere enn case 1 pÃ¥ P4 og P5 fordi sentrale nasjonale lÃ¸sninger allerede finnes og brukes. Hovedutfordringen ligger i Ã¥ utvide gjenbruket kontrollert til flere formÃ¥l og aktÃ¸rer, uten Ã¥ svekke P7. Prinsippbruddene er derfor mindre grunnleggende enn i overgangscaset, men de er fortsatt tydelige i randsonene rundt eksisterende opptakslÃ¸p.

## 7. Produktvurdering

### 7.1 Vurderte produkter fra katalogen

| Produkt | Produktkategori | Relevans | Kan brukes direkte | BÃ¸r videreutvikles | Ikke relevant | Begrunnelse |
|---|---|---|---|---|---|---|
| Nasjonal vitnemÃ¥lsdatabase (SIKT-004) | Register â€“ vitnemÃ¥l | HÃ¸y | Ja | Nei | Nei | Autoritativ nasjonal kilde for resultater fra videregÃ¥ende opplÃ¦ring |
| VitnemÃ¥lsportalen (SIKT-005) | Portal â€“ deling av vitnemÃ¥l | HÃ¸y | Ja | Nei | Nei | Direkte relevant sluttbrukerflate for deling av dokumentasjon |
| OpptakslÃ¸sninger (SIKT-003) | FelleslÃ¸sning â€“ opptak | HÃ¸y | Ja | Nei | Nei | Etablert viderebruk av resultater i opptak til hÃ¸yere utdanning |
| VIGO (NOVARI-004) | FelleslÃ¸sning â€“ inntak og administrasjon i videregÃ¥ende | HÃ¸y | Ja | Nei | Nei | Sentralt sektorsystem for videregÃ¥ende med hÃ¸y relevans for resultatinformasjon og oppfÃ¸lging |
| Feide (SIKT-001) | Felleskomponent â€“ autentisering | Middels | Ja | Nei | Nei | Relevante brukergrupper i utdanning kan autentiseres gjennom etablert sektorlÃ¸sning |
| ID-porten (DIGDIR-001) | Felleskomponent â€“ autentisering | Middels | Ja | Nei | Nei | Relevante for unge over 18 og foresatte i noen lÃ¸p |
| Altinn Autorisasjon (DIGDIR-004) | Felleskomponent â€“ autorisasjon | Middels | Ja | Ja | Nei | Relevant der resultatinformasjon skal brukes av andre pÃ¥ vegne av den unge eller under tydelig tilgangsstyring |
| Begrepskatalog (DIGDIR-012) | FelleslÃ¸sning â€“ begrepsbeskrivelse | Middels | Nei | Ja | Nei | Kan gi semantisk ryddighet i forstÃ¥elsen av resultater og kompetanse, men innhold mÃ¥ etableres |
| FINT Informasjonsmodell (NOVARI-003) | Referanseressurs â€“ informasjonsmodell | Middels | Nei | Ja | Nei | Kan bidra til harmonisering av resultatrelaterte begreper, men krever tilpasning for nasjonal viderebruk |
| Felles datakatalog (DIGDIR-011) | FelleslÃ¸sning â€“ metadataplattform | Lav/middels | Ja | Nei | Nei | Kan synliggjÃ¸re datasett og beskrivelser, men er ikke i seg selv delingsmotoren |
| API-katalog (DIGDIR-013) | FelleslÃ¸sning â€“ API-oversikt | Lav/middels | Ja | Nei | Nei | Relevant hvis resultattjenester skal eksponeres som standardiserte API-er |
| data.altinn.no (DIGDIR-015) | FelleslÃ¸sning â€“ kontrollert datadeling | Middels | Ja | Nei | Nei | Aktuell som mÃ¸nster for kontrollert deling til autoriserte aktÃ¸rer utenfor dagens lÃ¸p |
| Dialogporten (DIGDIR-020) | FelleslÃ¸sning â€“ dialogtjeneste | Lav | Nei | Nei | Ja | Ikke kjerneprodukt for resultatinformasjon, som primÃ¦rt er register- og dokumentasjonsbasert |
| Altinn Events (DIGDIR-010) | Felleskomponent â€“ hendelsestjeneste | Lav/middels | Nei | Nei | Ja | Kan vÃ¦re nyttig som supplerende mÃ¸nster, men er ikke sentralt for selve resultatinformasjonen |
| FIKS-plattformen (KS-001) | Plattform â€“ kommunal integrasjon | Middels | Ja | Nei | Nei | Relevant hvis kommunale oppfÃ¸lgingstjenester skal bruke resultatinformasjon gjennom standardiserte integrasjoner |
| Felles studentsystem (SIKT-002) | Plattform â€“ studentdata | Lav | Nei | Nei | Ja | Relevant fÃ¸rst etter overgang til hÃ¸yere utdanning, ikke for selve resultatinformasjonen fra videregÃ¥ende |
| eInnsyn (DIGDIR-006) | FelleslÃ¸sning â€“ innsynslÃ¸sning | Lav | Nei | Nei | Ja | Ikke relevant for primÃ¦rbehovet |
| eSignering (DIGDIR-003) | Felleskomponent â€“ signering | Lav | Nei | Nei | Ja | Ikke sentral for dette caset |

### 7.2 Oppsummering

- Hva finnes: Det finnes allerede en sterk nasjonal kjerne for resultatinformasjon gjennom NVB, VitnemÃ¥lsportalen, OpptakslÃ¸sninger og VIGO
- Hva kan gjenbrukes direkte: NVB, VitnemÃ¥lsportalen, OpptakslÃ¸sninger, VIGO, Feide, ID-porten og i noen grad Altinn Autorisasjon og FIKS-plattformen
- Hva mÃ¥ videreutvikles: Altinn Autorisasjon for enkelte representasjons- og tilgangsscenarier, Begrepskatalog som semantisk grunnlag for resultater og kompetanse, samt semantisk harmonisering mot FINT Informasjonsmodell
- Hva er ikke relevant: Dialogporten, eInnsyn, eSignering og i stor grad Altinn Events for dette konkrete caset

### 7.3 Eksplisitte mangler

| Identifisert mangel | Hvorfor mangelen oppstÃ¥r | Konsekvens hvis ikke lÃ¸st | Forslag | Bygger pÃ¥ |
|---|---|---|---|---|
| Standardisert delingsmÃ¸nster til oppfÃ¸lgingstjenester | Eksisterende resultatinfrastruktur er sterkest mot opptak og dokumentasjon, ikke nÃ¸dvendigvis mot oppfÃ¸lging av unge | OppfÃ¸lgingstjenester mÃ¥ innhente eller verifisere informasjon manuelt | Etablere standardisert grenseflate og tilgangsmodell for oppfÃ¸lgingstjenester | NVB (SIKT-004), VIGO (NOVARI-004), FIKS-plattformen (KS-001), data.altinn.no (DIGDIR-015) |
| Tydelig formÃ¥lsstyring for viderebruk av resultater | Samme informasjon brukes til flere formÃ¥l, men tilgangsgrunnlag er ikke nÃ¸dvendigvis tydelig nok for alle aktÃ¸rer | Enten underbruk eller for risikofylt deling | Tydelig sektorprofil for tilgang og formÃ¥l | Altinn Autorisasjon (DIGDIR-004), ID-porten (DIGDIR-001), Feide (SIKT-001) |
| Felles begrepssett for resultater, kompetanse og status | Resultatbegreper kan tolkes ulikt i ulike tjenester og sektorer | MisforstÃ¥elser i viderebruk og dÃ¥rligere datakvalitet | Etablere begrepsarbeid i Begrepskatalogen og harmonisere med sektormodeller | Begrepskatalog (DIGDIR-012), Felles datakatalog (DIGDIR-011), FINT Informasjonsmodell (NOVARI-003) |

## 8. Tiltak prioritert etter effekt

| Tiltak | Type | Effekt | Tidshorisont | Avhengigheter | Kobling | PrimÃ¦r gap-type |
|---|---|---|---|---|---|---|
| Kartlegg hvilke aktÃ¸rer og formÃ¥l utenfor opptakslÃ¸p som trenger resultatinformasjon | Avklaring | HÃ¸y | Kort | Utdanningsdirektorat, SIKT, relevante sektorer | Juridisk samhandling / P3 | Juridisk gap |
| Etabler standardisert delingsmÃ¸nster for resultatinformasjon til oppfÃ¸lgingstjenester | Gjenbruk + videreutvikling | HÃ¸y | Middels | Kartlegging og juridisk avklaring | Datautveksling og integrasjon / P4 / NVB + VIGO + FIKS + data.altinn.no | Samordningsgap |
| Vurder sektorprofil for autorisasjon og representasjon | Videreutvikling | Middels | Middels | Juridisk avklaring | Tillit / P7 / Altinn Autorisasjon | Produktgap |
| Etabler felles begrepssett for resultater og kompetanse | Nyutvikling (innhold) | Middels | Middels | Sektorfaglig forankring | Informasjonsforvaltning / P4 / Begrepskatalog + FINT Informasjonsmodell | Semantisk gap |
| Etabler samordnet forvaltningslÃ¸p mellom SIKT- og fylkeskommunale produkter | Gjenbruk + samordning | Middels | Middels | Samordning mellom SIKT, Novari og fylkeskommuner | P5, P6 / NVB + VitnemÃ¥lsportalen + VIGO | Samordningsgap |
| GjÃ¸r resultatinfrastruktur mer synlig som gjenbrukbar nasjonal byggestein utover opptakslÃ¸p | Gjenbruk | Middels | Kort | Samordning mellom SIKT og nasjonale aktÃ¸rer | P5 / NVB, VitnemÃ¥lsportalen, OpptakslÃ¸sninger | Samordningsgap |

### Prioritert liste

1. Avklar hvilke aktÃ¸rer og formÃ¥l som faktisk trenger resultatinformasjon utenfor dagens etablerte opptakslÃ¸p
2. Etabler standardisert og hjemlet delingsmÃ¸nster til oppfÃ¸lgingstjenester og andre legitime brukere
3. Bruk Begrepskatalog og autorisasjonsprofilering til Ã¥ rydde i semantikk og tilgangsregler

## 9. Strategisk vurdering

- Betydning for portefÃ¸ljeprioritering: Dette caset viser at sektoren allerede har nasjonal resultatinfrastruktur med hÃ¸y verdi. Prioriteringen bÃ¸r derfor vÃ¦re Ã¥ utvide og synliggjÃ¸re gjenbruk, ikke Ã¥ starte med nye grunnlÃ¸sninger.
- Betydning for nasjonal arkitektur: Caset er et godt eksempel pÃ¥ et omrÃ¥de der produktkatalogen faktisk gir sterke treff. Det viser verdien av Ã¥ bygge videre pÃ¥ eksisterende register- og delingsressurser fremfor Ã¥ tenke nytt fra bunnen.
- Behov for samordning: Krever sÃ¦rlig samspill mellom SIKT, Utdanningsdirektorat, oppfÃ¸lgingstjenester, eventuelle arbeidslivsaktÃ¸rer og Digdir der tilgangsstyring og kontrollert deling blir aktuelt.

## 10. Konklusjon

TilgjengeliggjÃ¸ring av resultater fra videregÃ¥ende opplÃ¦ring er et case der den nasjonale produktkatalogen treffer godt. Nasjonal vitnemÃ¥lsdatabase, VitnemÃ¥lsportalen, OpptakslÃ¸sninger og VIGO dekker allerede sentrale behov for kvalitetssikring, deling og viderebruk av resultatinformasjon. Det viktigste forbedringsbehovet er derfor ikke Ã¥ etablere nye grunnprodukter, men Ã¥ utvide viderebruken kontrollert til flere legitime formÃ¥l og aktÃ¸rer. Det krever sÃ¦rlig avklaring av tilgangsgrunnlag, tydeligere formÃ¥lsstyring og et standardisert mÃ¸nster for deling til oppfÃ¸lgingstjenester og andre mottakere utenfor etablerte opptakslÃ¸p. Samlet sett viser caset at oppsettet fungerer godt nÃ¥r produktkatalogen faktisk har modne og tydelige produkter i domenet, men at samordningen mellom nasjonale og sektorspesifikke lÃ¸sninger mÃ¥ styrkes.

