# Produkt-canvas: Fiks skatte- og inntektsopplysninger

## Navn
Fiks skatte- og inntektsopplysninger

## Ressurs ID
KS-009

## Status/Livsfase
**Produksjon** - etablert registertilgangstjeneste i KS Digital for kommunal bruk av skatte- og inntektsopplysninger fra Skatteetaten.

**Fakta:** KS Digital beskriver tjenesten som en operativ løsning som kan brukes både via Fiks forvaltning og som integrasjon i kommunens egne fagsystemer. Produktsiden beskriver konkrete tjenesteområder i bruk, og utviklerdokumentasjonen viser egne API-er i test- og produksjonsmiljø.

## Modenhet
**Høy funksjonell modenhet** - løsningen har tydelige tjenesteområder, publisert teknisk dokumentasjon og en etablert rolle- og hjemmelsmodell for bruk i kommunal sektor.

- Kildene viser både webbasert oppslag for saksbehandlere og maskin-til-maskin-integrasjon mot fagsystemer.
- KS Digital beskriver konkrete bruksområder for redusert foreldrebetaling, praktisk bistand og langtidsopphold i institusjon.
- Produktet bygger videre på strukturer fra Fiks folkeregister og inngår tydelig i Fiks register-familien.

**Deduksjon:** Modenheten er høy som spesialisert tilgangstjeneste og beregningsstøtte, men løsningen er fortsatt avhengig av Skatteetatens kilder, hjemler og segmentforvaltning for å fungere som forutsatt.

## Kort beskrivelse
Fiks skatte- og inntektsopplysninger er KS Digitals tilgangstjeneste for kommunal bruk av skatte- og inntektsdata fra Skatteetaten gjennom Fiks. Løsningen er laget for konkrete kommunale tjenesteområder der saksbehandlere trenger oppdatert og relevant inntektsgrunnlag som del av vedtak og beregninger. Produktet kan brukes både i en nettsideløsning for oppslag i Fiks forvaltning og som integrert tjeneste i kommunens egne fagsystemer. I praksis fungerer det som et spesialisert tilgangslag og beregningsnært overbygg over Skatteetatens delingstjenester, med innebygd dataminimering, rollebasert tilgang og tjenesteområdebasert hjemmelsstyring.

## Kapabiliteter
- **Datakilder: Grunndata** er direkte relevant fordi løsningen gjør autoritative skatte- og inntektsopplysninger fra Skatteetaten anvendbare i kommunale prosesser gjennom et kontrollert tilgangslag.
- **Datautveksling og integrasjon: Bruke data fra andre** er kjernefunksjonen fordi kommuner og kommunale fagsystemer bruker løsningen for å hente og anvende data fra en annen virksomhets delingstjenester i egne arbeidsprosesser.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals produkt- og utviklerdokumentasjon kontrollert 2026-03-26.

## Produktmål
Dokumenterte mål:
- Gi kommunal sektor tilgang til skatte- og inntektsopplysninger fra Skatteetaten gjennom Fiks.
- Støtte konkrete kommunale tjenesteområder som redusert foreldrebetaling, praktisk bistand og langtidsopphold i institusjon.
- Gjøre tjenesten tilgjengelig både som nettsideløsning og som API for kommunale fagsystemer.

Operative mål utledet fra kildene:
- Redusere behovet for manuell innhenting og dokumentkontroll fra innbyggere i saker der kommunen trenger oppdatert inntektsgrunnlag.
- Gi mer ensartet behandling på tvers av kommuner ved å bruke samme datagrunnlag, tjenesteområder og oppslagsmønster.
- Begrense innsyn til relevante opplysninger gjennom roller, dataminimering og hjemmelsstyrte tjenesteområder.

## Brukerbehov
- Kommunale saksbehandlere trenger rask tilgang til relevant inntektsgrunnlag i saker om egenandeler og redusert betaling.
- Kommuner trenger å hente data direkte fra kilden uten å be innbyggere sende inn skatteoppgjør manuelt.
- Fagsystemer trenger et standardisert API-løp for å bruke skatte- og inntektsopplysninger maskinelt.
- Forvaltere trenger tydelig rolle- og tjenesteområdekontroll for å sikre at innsyn skjer med korrekt hjemmel.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Tilgang til relevant inntektsgrunnlag i lovregulerte tjenester | Saksbehandling og beregning av egenandeler og redusert betaling | Primær målgruppe |
| Saksbehandlere | Enkelt oppslag med riktig avgrensede data | Bruk i Fiks forvaltning ved behandling av enkeltsaker | Bruker webgrensesnitt og beregningsstøtte |
| Fagsystemer og leverandører | Maskinell tilgang til data og beregningsnære API-er | Integrasjon mot søknadsløsninger og kommunale fagsystemer | Teknisk brukergruppe |
| Forvaltere og Fiks-administratorer | Rolleoppsett, dataminimering og tilgangsstyring | Oppsett av tjenesteområder og kontroll av bruk | Viktig for etterlevelse |
| KS Digital | Produktforvaltning, segmentoppfølging og videreutvikling | Forvaltning av tjenesten og samspill med Skatteetaten | Sentral tjenesteforvalter |

## Hovedfunksjoner
### Primære funksjoner
Fiks skatte- og inntektsopplysninger gir kommunal sektor kontrollert tilgang til skatte- og inntektsdata fra Skatteetaten for konkrete saksbehandlingsformål. Produktet er derfor ikke en generell delingstjeneste for alle typer økonomiske opplysninger, men en målrettet løsning for bestemte kommunale tjenesteområder der oppdatert inntektsgrunnlag er nødvendig for vedtak og beregning.

Løsningen har to operative flater som må forstås samlet. Den ene er en nettsideløsning i Fiks forvaltning der saksbehandlere kan gjøre oppslag, legge inn nødvendige parametere og laste ned resultat som PDF. Den andre er et API-løp for integrasjon i kommunale fagsystemer og skjemaløsninger. Produktet skal derfor ikke beskrives bare som et API, fordi en vesentlig del av verdien også ligger i den ferdige arbeidsflaten for saksbehandlere.

Tjenesten støtter flere konkrete beregnings- og vurderingsløp. KS Digital beskriver blant annet redusert foreldrebetaling i barnehage og SFO, praktisk bistand og opplæring, og langtidsopphold i institusjon. I utviklerdokumentasjonen beskrives et eget overbygg som kan søke på flere personer, sammenstille poster fra Skatteetatens API-er og bruke beregningstyper tilpasset tjenesteområdet. Dette betyr at produktet ikke bare videresender rådata, men også tilrettelegger dem for kommunal bruk innenfor definerte rammer.

En sentral del av funksjonen er tilgangsstyring og dataminimering. Brukere er knyttet til tjenesteområder og hjemler, og KS Digital anbefaler egne roller for de ulike tjenestene. Produktet bygger også på strukturer fra Fiks folkeregister og inngår i det bredere segmentsamarbeidet med Skatteetaten. Det gjør at produktets operative rolle omfatter både teknisk tilgang, organisatorisk forvaltning og sikker bruk av taushetsbelagte opplysninger.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Tilgang til skatte- og inntektsopplysninger fra Skatteetaten via Fiks | Eierskap til kildedata eller Skatteetatens delingstjenester |
| Nettsideløsning for oppslag i Fiks forvaltning | Generell økonomisk saksbehandling utenfor de definerte tjenesteområdene |
| API-er og overbygg for integrasjon i kommunale systemer | Fri tilgang til data uten lovhjemmel, rolle og tjenstlig behov |
| Dataminimering, rolleoppsett og tjenesteområdebasert bruk | Full kommunal kopiforvaltning av underliggende data |
| Beregningsnær tilrettelegging for bestemte kommunale tjenester | Full erstatning for kommunens egne fagsystemer og vedtaksløsninger |

## Veikart over kommende funksjonalitet
**Fakta:** KS Digital opplyser at Fiks-tjenestene videreutvikles kontinuerlig og viser til egen endringslogg for hva som er gjort i tjenestene. Jeg fant ikke et samlet offentlig veikart med tidsfestede milepæler for denne tjenesten i denne arbeidsøkten.

**Deduksjon:** Videreutviklingen vil trolig være knyttet til flere tjenesteområder, justeringer i beregningslogikk og tilpasninger til endringer i Skatteetatens delingstjenester og segmentforvaltning.

## Forretningsverdi/Verdiforslag
### For kommuner og fylkeskommuner
- Reduserer manuell dokumentinnhenting og kontroll i saker der inntektsgrunnlag er nødvendig.
- Gir et mer standardisert og etterprøvbart oppslags- og integrasjonsløp enn lokale særtilpasninger.

### For saksbehandlere
- Gjør det mulig å hente relevant og avgrenset inntektsgrunnlag direkte i arbeidsprosessen.
- Støtter vurdering og beregning uten å bygge egne manuelle oppslag mot flere kilder.

### For sektoren
- Bidrar til mer ensartet behandling på tvers av kommuner når samme datagrunnlag og tjenestelogikk brukes.
- Styrker kontrollen med personvern og hjemmelsbruk gjennom felles roller og dataminimering.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Bruk uten riktig hjemmel eller feil tjenesteområde kan gi urettmessig innsyn i taushetsbelagte opplysninger. | Tydelig kobling mellom rolle, tjenesteområde og hjemmel, samt lokal kontroll av behandlingsgrunnlag. |
| Teknisk | Endringer i Skatteetatens API-er eller i Fiks-overbygget kan påvirke kommunale beregningsløp. | Versjonsstyring, testmiljø, endringslogg og koordinert innføring i fagsystemer. |
| Sikkerhet | Tjenesten håndterer sensitive opplysninger som må begrenses til riktig bruker og kontekst. | Rollebasert tilgang, dataminimering, logging og sikker integrasjon via Fiks-plattformen. |
| Leverandør | Kommunene blir avhengige av både KS Digital som segment- og tjenesteforvalter og Skatteetatens underliggende delingstjenester. | Tydelige avtaler, dokumenterte grensesnitt og løpende koordinering mellom aktørene. |
| Brukeropplevelse | Løsningen gir lav verdi hvis tjenesteområder, roller eller integrasjoner settes opp feil lokalt. | Gode veiledere, tydelig oppsett i Fiks forvaltning og tett samspill med systemleverandører. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-register/fiks-skatte-og-inntektsopplysninger/
- https://developers.fiks.ks.no/tjenester/register/skatteoginntektsopplysninger_ny/
- https://developers.fiks.ks.no/tjenester/register/skatteoginntektsopplysninger_proxy/
- https://ksdigital.no/tjenestene/segmentsamarbeid/
- https://ksdigital.no/avtaler-og-priser/fakturalinjer/

## Plattform
Fiks skatte- og inntektsopplysninger er en registertilgangstjeneste i KS Digital og en undertjeneste under Fiks register.

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

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** - løsningen gjør autoritative skatte- og inntektsopplysninger tilgjengelige for gjenbruk i kommunale arbeidsprosesser der det finnes hjemmel og behov.
- **P7: Sørg for tillit til oppgaveløsningen** - produktet bygger på rollebasert tilgang, dataminimering og tjenesteområdebasert hjemmelsstyring for å begrense innsyn til det som er nødvendig.

## Finansiering
**Fakta:** KS Digitals fakturalinjer viser at Fiks register har egen fastpris og innbyggerpris for undertjenestene Folkeregister og Skatte- og inntektsopplysninger, og at tjenesten også har en Digifin prosjektavgift for kommuner.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full prismodell per kundetype og full intern budsjettfordeling mellom KS, KS Digital og tilknyttede aktører.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktside, utviklerdokumentasjon og avtaleinformasjon ligger hos KS Digital. |
| Driftsansvar | KS Digital | Tjenesten forvaltes på Fiks-plattformen, men full intern driftsmodell er ikke offentlig detaljert dokumentert. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Fakturalinjer viser prismodell, men ikke full budsjettstyring. |
| Styringsmodell | KS og KS Digital i segmentsamarbeid med Skatteetaten | Produktsiden beskriver segmentansvar og formalisert fordeling mellom KS og KS Digital. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-register/fiks-skatte-og-inntektsopplysninger/
- https://developers.fiks.ks.no/tjenester/register/skatteoginntektsopplysninger_ny/
- https://developers.fiks.ks.no/tjenester/register/skatteoginntektsopplysninger_proxy/
- https://ksdigital.no/tjenestene/segmentsamarbeid/
- https://ksdigital.no/avtaler-og-priser/fakturalinjer/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/produkter/produktbeskrivelser/28-FIKS-Register-produkt-canvas-v1-codex.md`
- Lokal fil: `arkitektur/produkter/produktbeskrivelser/67-FIKS-Folkeregister-produkt-canvas-v1-codex.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/fiks-skatte-og-inntektsopplysninger/ (hentet 2026-03-26)
- Nettkilde: https://developers.fiks.ks.no/tjenester/register/skatteoginntektsopplysninger_ny/ (hentet 2026-03-26)
- Nettkilde: https://developers.fiks.ks.no/tjenester/register/skatteoginntektsopplysninger_proxy/ (hentet 2026-03-26)
- Nettkilde: https://ksdigital.no/tjenestene/segmentsamarbeid/ (hentet 2026-03-26)
- Nettkilde: https://ksdigital.no/avtaler-og-priser/fakturalinjer/ (hentet 2026-03-26)
