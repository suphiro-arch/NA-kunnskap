# Produkt-canvas: Fiks skatte- og inntektsopplysninger

## Navn
Fiks skatte- og inntektsopplysninger

## Ressurs ID
KS-009

## Status/Livsfase
**Produksjon** - etablert registertilgangstjeneste i KS Digital for kommunal bruk av skatte- og inntektsopplysninger fra Skatteetaten.

**Fakta:** KS Digital beskriver tjenesten som en operativ løsning som kan brukes både via Fiks forvaltning og som integrasjon i kommunens egne fagsystemer. Produktsiden beskriver konkrete tjenesteområder i bruk, og KS Digitals utviklerdokumentasjon viser egne API-er og overbygg på Fiks-plattformen. KS omtaler segmentsamarbeidet mot Skatteetaten, mens den operative forvaltningen er lagt til KS Digital.

## Modenhet
**Høy funksjonell modenhet** - løsningen har tydelige tjenesteområder, publisert teknisk dokumentasjon, etablert segmentstyring og løpende håndtering av årsrevisjoner i Skatteetatens API-er.

- Kildene viser både webbasert oppslag for saksbehandlere og maskin-til-maskin-integrasjon mot fagsystemer.
- KS Digital beskriver konkrete bruksområder for redusert foreldrebetaling, praktisk bistand og langtidsopphold i institusjon.
- Siden om segmentsamarbeid viser at løsningen inngår i et etablert forvaltningsregime der endringer i Skatteetatens API-er analyseres og kommuniseres til kommuner og leverandører.

**Deduksjon:** Produktet er modent som spesialisert tilgangstjeneste og beregningsnært overbygg, men er fortsatt sterkt avhengig av Skatteetatens rettighetspakker, bruksvilkår og endringsløp.

## Kort beskrivelse
Fiks skatte- og inntektsopplysninger er KS Digitals tilgangstjeneste for kommunal bruk av skatte- og inntektsdata fra Skatteetaten gjennom Fiks. Løsningen er laget for konkrete kommunale tjenesteområder der saksbehandlere trenger oppdatert og relevant inntektsgrunnlag som del av vedtak og beregninger. Produktet kan brukes både i en nettsideløsning for oppslag i Fiks forvaltning og som integrert tjeneste i kommunens egne fagsystemer. I praksis fungerer det som et spesialisert tilgangslag og beregningsnært overbygg over Skatteetatens delingstjenester, med innebygd dataminimering, rollebasert tilgang og hjemmelsstyring per tjenesteområde.

## Kapabiliteter
- **Datakilder: Grunndata** er direkte relevant fordi løsningen gjør autoritative skatte- og inntektsopplysninger fra Skatteetaten anvendbare i kommunale prosesser gjennom et kontrollert tilgangslag.
- **Datautveksling og integrasjon: Bruke data fra andre** er kjernefunksjonen fordi kommuner og kommunale fagsystemer bruker løsningen for å hente og anvende data fra en annen virksomhets delingstjenester i egne arbeidsprosesser.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot KS Digitals produkt-, utvikler- og segmentsider samt Skatteetatens bruksvilkår kontrollert 2026-05-26.

## Produktmål
Dokumenterte mål:
- Gi kommunal sektor tilgang til skatte- og inntektsopplysninger fra Skatteetaten gjennom Fiks.
- Støtte konkrete kommunale tjenesteområder som redusert foreldrebetaling, praktisk bistand og langtidsopphold i institusjon.
- Gjøre tjenesten tilgjengelig både som nettsideløsning og som API for kommunale fagsystemer.

Operative mål utledet fra kildene:
- Redusere behovet for manuell innhenting og dokumentkontroll fra innbyggere i saker der kommunen trenger oppdatert inntektsgrunnlag.
- Gi mer ensartet behandling på tvers av kommuner ved å bruke samme datagrunnlag, tjenesteområder og oppslagsmønster.
- Begrense innsyn til relevante opplysninger gjennom roller, dataminimering og hjemmelsstyrte rettighetspakker.

## Brukerbehov
- Kommunale saksbehandlere trenger rask tilgang til relevant inntektsgrunnlag i saker om egenandeler og redusert betaling.
- Kommuner trenger å hente data direkte fra kilden uten å be innbyggere sende inn skatteoppgjør manuelt.
- Fagsystemer trenger et standardisert API-løp for å bruke skatte- og inntektsopplysninger maskinelt.
- Forvaltere trenger tydelig rolle-, tjenesteområde- og endringskontroll når Skatteetatens delingstjenester oppdateres.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Tilgang til relevant inntektsgrunnlag i lovregulerte tjenester | Saksbehandling og beregning av egenandeler og redusert betaling | Primær målgruppe |
| Saksbehandlere | Enkelt oppslag med riktig avgrensede data | Bruk i Fiks forvaltning ved behandling av enkeltsaker | Bruker webgrensesnitt og beregningsstøtte |
| Fagsystemer og leverandører | Maskinell tilgang til data og beregningsnære API-er | Integrasjon mot søknadsløsninger og kommunale fagsystemer | Teknisk brukergruppe |
| Forvaltere og Fiks-administratorer | Rolleoppsett, dataminimering og endringsoppfølging | Oppsett av tjenesteområder og kontroll av bruk | Viktig for etterlevelse |
| KS Digital | Segmentkoordinering, veiledning og teknisk forvaltning | Koordinering mot Skatteetaten, endringshåndtering og tjenesteutvikling | Sentral forvaltningsrolle |

## Hovedfunksjoner
### Primære funksjoner
Fiks skatte- og inntektsopplysninger gir kommunal sektor kontrollert tilgang til skatte- og inntektsdata fra Skatteetaten for bestemte saksbehandlingsformål. Produktet er derfor ikke en generell delingstjeneste for alle typer økonomiske opplysninger, men en målrettet løsning for tjenesteområder der oppdatert inntektsgrunnlag er nødvendig for vedtak og beregning.

Løsningen har to operative flater som må forstås samlet. Den ene er en nettsideløsning i Fiks forvaltning der saksbehandlere kan gjøre oppslag og bruke resultatene i konkrete saker. Den andre er et API-løp for integrasjon i kommunale fagsystemer og skjemaløsninger. Utviklerdokumentasjonen viser at KS Digital både tilbyr proxy mot Skatteetatens API-er og et eget overbygg som kan søke på flere personer, håndtere beregningstyper og returnere et mer tilrettelagt svar.

Tjenesten er tett koblet til tjenesteområder og hjemler. KS Digital beskriver blant annet redusert foreldrebetaling i barnehage og SFO, praktisk bistand og opplæring og egenandel ved langtidsopphold i institusjon. I praksis betyr dette at produktet ikke bare videreformidler rådata, men tilpasser tilgang og visning til kommunale arbeidsprosesser som er definert i segmentet.

En sentral del av funksjonen er endrings- og forvaltningsarbeidet rundt Skatteetatens delingstjenester. KS Digital ivaretar dette i praksis gjennom koordinering mot Skatteetaten, og siden om segmentsamarbeid viser hvordan årsrevisjoner, endringer i poster og konsekvenser håndteres for leverandører og kommuner. Produktets operative rolle omfatter derfor både teknisk tilgang, beregningsnær tilrettelegging og koordinert forvaltning av et endringsutsatt kildegrunnlag.

### Typiske brukssituasjoner (generisk)
- Når kommunen skal beregne redusert foreldrebetaling eller andre egenandeler basert på oppdatert inntektsgrunnlag.
- Når saksbehandlere trenger kontrollert oppslag i skatte- og inntektsopplysninger i Fiks forvaltning.
- Når kommunale fagsystemer skal hente og bruke skatteopplysninger gjennom et standardisert segmentmønster i stedet for direkte egne integrasjoner.

### Når Fiks skatte- og inntektsopplysninger normalt ikke er førstevalg
- Når behovet gjelder generell økonomisk saksbehandling uten dokumentert hjemmel eller utenfor de etablerte tjenesteområdene.
- Når virksomheten ikke inngår i kommunesegmentet eller trenger et helt annet avtale- og forvaltningsregime enn det KS tilbyr.
- Når behovet er direkte bruk av Skatteetatens egne API-er uten KS Digital sitt overbygg, rollemodell eller endringshåndtering.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Tilgang til skatte- og inntektsopplysninger fra Skatteetaten via Fiks | Eierskap til kildedata eller Skatteetatens delingstjenester |
| Nettsideløsning for oppslag i Fiks forvaltning | Generell økonomisk saksbehandling utenfor de definerte tjenesteområdene |
| API-er og overbygg for integrasjon i kommunale systemer | Fri tilgang til data uten lovhjemmel, rolle og tjenstlig behov |
| Dataminimering, rolleoppsett og tjenesteområdebasert bruk | Full kommunal kopiforvaltning av underliggende data |
| Beregningsnær tilrettelegging for bestemte kommunale tjenester | Full erstatning for kommunens egne fagsystemer og vedtaksløsninger |

## Veikart over kommende funksjonalitet
**Fakta:** KS Digital opplyser at Fiks-tjenestene videreutvikles kontinuerlig og viser til egen endringslogg for hva som er gjort i de forskjellige tjenestene. Jeg fant ikke et samlet offentlig veikart med tidsfestede milepæler for denne tjenesten i denne arbeidsøkten.

**Deduksjon:** Videreutviklingen vil trolig være knyttet til flere tjenesteområder, justeringer i beregningslogikk og løpende tilpasninger til Skatteetatens årsrevisjoner og andre endringer i delingstjenestene.

## Forretningsverdi/Verdiforslag
### For kommuner og fylkeskommuner
- Reduserer manuell dokumentinnhenting og kontroll i saker der inntektsgrunnlag er nødvendig.
- Gir et mer standardisert og etterprøvbart oppslags- og integrasjonsløp enn lokale særtilpasninger.

### For saksbehandlere
- Gjør det mulig å hente relevant og avgrenset inntektsgrunnlag direkte i arbeidsprosessen.
- Støtter vurdering og beregning uten å bygge egne manuelle oppslag mot flere kilder.

### For sektoren og leverandørmiljøet
- Bidrar til mer ensartet behandling på tvers av kommuner når samme datagrunnlag og tjenestelogikk brukes.
- Styrker kontrollen med personvern, hjemmelsbruk og endringshåndtering gjennom felles segmentforvaltning.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Bruk uten riktig hjemmel eller feil tjenesteområde kan gi urettmessig innsyn i taushetsbelagte opplysninger. | Tydelig kobling mellom rolle, tjenesteområde og hjemmel, samt lokal kontroll av behandlingsgrunnlag. |
| Teknisk | Endringer i Skatteetatens API-er eller i KS Digitals overbygg kan påvirke kommunale beregningsløp og integrasjoner. | Versjonsoppfølging, testmiljø, endringslogg og koordinert innføring i fagsystemer. |
| Sikkerhet | Tjenesten håndterer sensitive opplysninger som må begrenses til riktig bruker og kontekst. | Rollebasert tilgang, dataminimering, logging og sikker integrasjon via Fiks-plattformen. |
| Leverandør | Kommunene blir avhengige av både KS Digital som segment- og tjenesteforvalter og Skatteetatens underliggende delingstjenester. | Tydelige avtaler, dokumenterte grensesnitt og løpende koordinering mellom aktørene. |
| Brukeropplevelse | Løsningen gir lav verdi hvis tjenesteområder, roller eller integrasjoner settes opp feil lokalt. | Gode veiledere, tydelig oppsett i Fiks forvaltning og tett samspill med systemleverandører. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-register/fiks-skatte-og-inntektsopplysninger/
- https://developers.fiks.ks.no/tjenester/register/skatteoginntektsopplysninger_ny/
- https://ksdigital.no/tjenestene/segmentsamarbeid/
- https://www.skatteetaten.no/deling/bruksvilkar-for-delingstjenester/

## Plattform
Fiks skatte- og inntektsopplysninger er en registertilgangstjeneste i KS Digital og en undertjeneste under Fiks register (`KS-004`), der KS Digital beskriver skatte- og inntektsopplysninger som én av fire datakilder.

**Fakta:**
- Tjenesten tilbys både som nettsideløsning og maskin-til-maskin-integrasjon.
- Utviklerdokumentasjonen viser test- og produksjonsmiljø på Fiks-plattformen og et eget overbygg i tillegg til proxy mot Skatteetatens API-er.
- Produktet er knyttet til segmentsamarbeidet mellom KS, KS Digital og Skatteetaten for kommunal tilgang til delte opplysninger.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full intern driftsarkitektur, detaljer om intern prioritering i veikartet og full finansieringsmodell bak sentral forvaltning.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme tjenestegrunnlag kan brukes av mange kommuner med lignende behov for inntektsgrunnlag i lovregulerte tjenester.
- Gjenbruksverdien ligger i felles tilgangsmønster, beregningsnært overbygg og felles styring av hjemmel og roller.
- Produktet kan gjenbrukes på tvers av flere tjenesteområder, men bare der hjemmelsgrunnlaget og tjenstlig behov faktisk er på plass.

**Vanlige kombinasjoner med andre produkter:**
- Fiks folkeregister, siden tjenesten er avhengig av fødsels- og personnummer fra dette løpet.
- Fiks forvaltning for manuelle oppslag og saksbehandlerstøtte.
- Kommunale fagsystemer og søknadsløsninger som trenger maskinell bruk av inntektsgrunnlag.

**Kildekode:** Ikke offentlig dokumentert for selve tjenesten. KS Digital publiserer klientbibliotek og SDK-er for Fiks-plattformen på [github.com/ks-no](https://github.com/ks-no), flere av dem under MIT-lisens.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** - løsningen gjør autoritative skatte- og inntektsopplysninger tilgjengelige for gjenbruk i kommunale arbeidsprosesser der det finnes hjemmel og behov.
- **P7: Sørg for tillit til oppgaveløsningen** - produktet bygger på rollebasert tilgang, dataminimering og tjenesteområdebasert hjemmelsstyring for å begrense innsyn til det som er nødvendig.
- **Spenning og begrensning:** Den felles segmentmodellen gir stordriftsfordeler og ensartet styring, men gjør også tjenesten følsom for endringer i Skatteetatens API-er og stiller høye krav til lokal forståelse av hjemmel og oppsettsvalg.

## Finansiering
**Fakta:** KS Digital viser til prisinformasjon for tjenesten fra produktsiden og publiserer overordnet prismodell for Fiks-familien. Skatteetatens bruksvilkår skiller mellom enkeltstående konsumenter og segmentsamarbeid, noe som understøtter at kommunesektoren bruker et segmentbasert avtale- og forvaltningsopplegg.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full prismodell per kundetype og full intern budsjettfordeling mellom KS, KS Digital og tilknyttede aktører.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktside, utviklerdokumentasjon og veiledningsmateriell ligger hos KS Digital. |
| Driftsansvar | KS Digital | Tjenesten forvaltes på Fiks-plattformen, men full intern driftsmodell er ikke offentlig detaljert dokumentert. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Prismodell og avtalespor er synlige, men ikke full budsjettstyring. |
| Styringsmodell | KS Digital forvalter og drifter løsningen, med strategisk forankring i KS | Fremgår av siden om segmentsamarbeid og produktets ta-i-bruk- og utviklerspor. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-register/fiks-skatte-og-inntektsopplysninger/
- https://developers.fiks.ks.no/tjenester/register/skatteoginntektsopplysninger_ny/
- https://ksdigital.no/tjenestene/segmentsamarbeid/
- https://www.skatteetaten.no/deling/bruksvilkar-for-delingstjenester/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/operative-ressurs-canvas.system.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v1-codex.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/fiks-skatte-og-inntektsopplysninger/ (hentet 2026-05-26)
- Nettkilde: https://developers.fiks.ks.no/tjenester/register/skatteoginntektsopplysninger_ny/ (hentet 2026-05-26)
- Nettkilde: https://ksdigital.no/tjenestene/segmentsamarbeid/ (hentet 2026-05-26)
- Nettkilde: https://www.skatteetaten.no/deling/bruksvilkar-for-delingstjenester/ (hentet 2026-05-26)

## Endringer fra forrige versjon
### Analyseforbedringer
- Oppdatert kildegrunnlaget med ny kontroll av KS-produktinformasjon, utviklerdokumentasjon, segmentsamarbeid og Skatteetatens bruksvilkår 2026-05-26.
- Presisert avhengigheten til Fiks folkeregister, segmentansvar og årlige API-endringer fra Skatteetaten.
- Tydeliggjort at produktet både er et tilgangslag og et beregningsnært overbygg, ikke bare et enkelt API-oppslag.

### Tekstlige forbedringer
- Lagt inn tydeligere brukssituasjoner og skarpere avgrensning mot generell økonomisk saksbehandling og direkte Skatteetaten-integrasjon.
- Forbedret gjenbruk, risiko og prinsippvurdering med mer eksplisitt vekt på hjemmel, roller og endringshåndtering.
- Strammet inn språk og struktur slik at produktets operative rolle fremstår tydeligere for både fag- og arkitekturmålgruppen.
