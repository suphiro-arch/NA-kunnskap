# Produkt-canvas: Fiks skatte- og inntektsopplysninger

## Navn
Fiks skatte- og inntektsopplysninger

## Ressurs ID
KS-009

## Status/Livsfase
**Produksjon** - etablert registertilgangstjeneste i KS Digital for kommunal bruk av skatte- og inntektsopplysninger fra Skatteetaten.

**Fakta:** KS Digital beskriver tjenesten som en operativ lÃ¸sning som kan brukes bÃ¥de via Fiks forvaltning og som integrasjon i kommunens egne fagsystemer. Produktsiden beskriver konkrete tjenesteomrÃ¥der i bruk, og utviklerdokumentasjonen viser egne API-er i test- og produksjonsmiljÃ¸.

## Modenhet
**HÃ¸y funksjonell modenhet** - lÃ¸sningen har tydelige tjenesteomrÃ¥der, publisert teknisk dokumentasjon og en etablert rolle- og hjemmelsmodell for bruk i kommunal sektor.

- Kildene viser bÃ¥de webbasert oppslag for saksbehandlere og maskin-til-maskin-integrasjon mot fagsystemer.
- KS Digital beskriver konkrete bruksomrÃ¥der for redusert foreldrebetaling, praktisk bistand og langtidsopphold i institusjon.
- Produktet bygger videre pÃ¥ strukturer fra Fiks folkeregister og inngÃ¥r tydelig i Fiks register-familien.

**Deduksjon:** Modenheten er hÃ¸y som spesialisert tilgangstjeneste og beregningsstÃ¸tte, men lÃ¸sningen er fortsatt avhengig av Skatteetatens kilder, hjemler og segmentforvaltning for Ã¥ fungere som forutsatt.

## Kort beskrivelse
Fiks skatte- og inntektsopplysninger er KS Digitals tilgangstjeneste for kommunal bruk av skatte- og inntektsdata fra Skatteetaten gjennom Fiks. LÃ¸sningen er laget for konkrete kommunale tjenesteomrÃ¥der der saksbehandlere trenger oppdatert og relevant inntektsgrunnlag som del av vedtak og beregninger. Produktet kan brukes bÃ¥de i en nettsidelÃ¸sning for oppslag i Fiks forvaltning og som integrert tjeneste i kommunens egne fagsystemer. I praksis fungerer det som et spesialisert tilgangslag og beregningsnÃ¦rt overbygg over Skatteetatens delingstjenester, med innebygd dataminimering, rollebasert tilgang og tjenesteomrÃ¥debasert hjemmelsstyring.

## Kapabiliteter
- **Datakilder: Grunndata** er direkte relevant fordi lÃ¸sningen gjÃ¸r autoritative skatte- og inntektsopplysninger fra Skatteetaten anvendbare i kommunale prosesser gjennom et kontrollert tilgangslag.
- **Datautveksling og integrasjon: Bruke data fra andre** er kjernefunksjonen fordi kommuner og kommunale fagsystemer bruker lÃ¸sningen for Ã¥ hente og anvende data fra en annen virksomhets delingstjenester i egne arbeidsprosesser.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals produkt- og utviklerdokumentasjon kontrollert 2026-03-26.

## ProduktmÃ¥l
Dokumenterte mÃ¥l:
- Gi kommunal sektor tilgang til skatte- og inntektsopplysninger fra Skatteetaten gjennom Fiks.
- StÃ¸tte konkrete kommunale tjenesteomrÃ¥der som redusert foreldrebetaling, praktisk bistand og langtidsopphold i institusjon.
- GjÃ¸re tjenesten tilgjengelig bÃ¥de som nettsidelÃ¸sning og som API for kommunale fagsystemer.

Operative mÃ¥l utledet fra kildene:
- Redusere behovet for manuell innhenting og dokumentkontroll fra innbyggere i saker der kommunen trenger oppdatert inntektsgrunnlag.
- Gi mer ensartet behandling pÃ¥ tvers av kommuner ved Ã¥ bruke samme datagrunnlag, tjenesteomrÃ¥der og oppslagsmÃ¸nster.
- Begrense innsyn til relevante opplysninger gjennom roller, dataminimering og hjemmelsstyrte tjenesteomrÃ¥der.

## Brukerbehov
- Kommunale saksbehandlere trenger rask tilgang til relevant inntektsgrunnlag i saker om egenandeler og redusert betaling.
- Kommuner trenger Ã¥ hente data direkte fra kilden uten Ã¥ be innbyggere sende inn skatteoppgjÃ¸r manuelt.
- Fagsystemer trenger et standardisert API-lÃ¸p for Ã¥ bruke skatte- og inntektsopplysninger maskinelt.
- Forvaltere trenger tydelig rolle- og tjenesteomrÃ¥dekontroll for Ã¥ sikre at innsyn skjer med korrekt hjemmel.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Tilgang til relevant inntektsgrunnlag i lovregulerte tjenester | Saksbehandling og beregning av egenandeler og redusert betaling | PrimÃ¦r mÃ¥lgruppe |
| Saksbehandlere | Enkelt oppslag med riktig avgrensede data | Bruk i Fiks forvaltning ved behandling av enkeltsaker | Bruker webgrensesnitt og beregningsstÃ¸tte |
| Fagsystemer og leverandÃ¸rer | Maskinell tilgang til data og beregningsnÃ¦re API-er | Integrasjon mot sÃ¸knadslÃ¸sninger og kommunale fagsystemer | Teknisk brukergruppe |
| Forvaltere og Fiks-administratorer | Rolleoppsett, dataminimering og tilgangsstyring | Oppsett av tjenesteomrÃ¥der og kontroll av bruk | Viktig for etterlevelse |
| KS Digital | Produktforvaltning, segmentoppfÃ¸lging og videreutvikling | Forvaltning av tjenesten og samspill med Skatteetaten | Sentral tjenesteforvalter |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
Fiks skatte- og inntektsopplysninger gir kommunal sektor kontrollert tilgang til skatte- og inntektsdata fra Skatteetaten for konkrete saksbehandlingsformÃ¥l. Produktet er derfor ikke en generell delingstjeneste for alle typer Ã¸konomiske opplysninger, men en mÃ¥lrettet lÃ¸sning for bestemte kommunale tjenesteomrÃ¥der der oppdatert inntektsgrunnlag er nÃ¸dvendig for vedtak og beregning.

LÃ¸sningen har to operative flater som mÃ¥ forstÃ¥s samlet. Den ene er en nettsidelÃ¸sning i Fiks forvaltning der saksbehandlere kan gjÃ¸re oppslag, legge inn nÃ¸dvendige parametere og laste ned resultat som PDF. Den andre er et API-lÃ¸p for integrasjon i kommunale fagsystemer og skjemalÃ¸sninger. Produktet skal derfor ikke beskrives bare som et API, fordi en vesentlig del av verdien ogsÃ¥ ligger i den ferdige arbeidsflaten for saksbehandlere.

Tjenesten stÃ¸tter flere konkrete beregnings- og vurderingslÃ¸p. KS Digital beskriver blant annet redusert foreldrebetaling i barnehage og SFO, praktisk bistand og opplÃ¦ring, og langtidsopphold i institusjon. I utviklerdokumentasjonen beskrives et eget overbygg som kan sÃ¸ke pÃ¥ flere personer, sammenstille poster fra Skatteetatens API-er og bruke beregningstyper tilpasset tjenesteomrÃ¥det. Dette betyr at produktet ikke bare videresender rÃ¥data, men ogsÃ¥ tilrettelegger dem for kommunal bruk innenfor definerte rammer.

En sentral del av funksjonen er tilgangsstyring og dataminimering. Brukere er knyttet til tjenesteomrÃ¥der og hjemler, og KS Digital anbefaler egne roller for de ulike tjenestene. Produktet bygger ogsÃ¥ pÃ¥ strukturer fra Fiks folkeregister og inngÃ¥r i det bredere segmentsamarbeidet med Skatteetaten. Det gjÃ¸r at produktets operative rolle omfatter bÃ¥de teknisk tilgang, organisatorisk forvaltning og sikker bruk av taushetsbelagte opplysninger.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Tilgang til skatte- og inntektsopplysninger fra Skatteetaten via Fiks | Eierskap til kildedata eller Skatteetatens delingstjenester |
| NettsidelÃ¸sning for oppslag i Fiks forvaltning | Generell Ã¸konomisk saksbehandling utenfor de definerte tjenesteomrÃ¥dene |
| API-er og overbygg for integrasjon i kommunale systemer | Fri tilgang til data uten lovhjemmel, rolle og tjenstlig behov |
| Dataminimering, rolleoppsett og tjenesteomrÃ¥debasert bruk | Full kommunal kopiforvaltning av underliggende data |
| BeregningsnÃ¦r tilrettelegging for bestemte kommunale tjenester | Full erstatning for kommunens egne fagsystemer og vedtakslÃ¸sninger |

## Veikart over kommende funksjonalitet
**Fakta:** KS Digital opplyser at Fiks-tjenestene videreutvikles kontinuerlig og viser til egen endringslogg for hva som er gjort i tjenestene. Jeg fant ikke et samlet offentlig veikart med tidsfestede milepÃ¦ler for denne tjenesten i denne arbeidsÃ¸kten.

**Deduksjon:** Videreutviklingen vil trolig vÃ¦re knyttet til flere tjenesteomrÃ¥der, justeringer i beregningslogikk og tilpasninger til endringer i Skatteetatens delingstjenester og segmentforvaltning.

## Forretningsverdi/Verdiforslag
### For kommuner og fylkeskommuner
- Reduserer manuell dokumentinnhenting og kontroll i saker der inntektsgrunnlag er nÃ¸dvendig.
- Gir et mer standardisert og etterprÃ¸vbart oppslags- og integrasjonslÃ¸p enn lokale sÃ¦rtilpasninger.

### For saksbehandlere
- GjÃ¸r det mulig Ã¥ hente relevant og avgrenset inntektsgrunnlag direkte i arbeidsprosessen.
- StÃ¸tter vurdering og beregning uten Ã¥ bygge egne manuelle oppslag mot flere kilder.

### For sektoren
- Bidrar til mer ensartet behandling pÃ¥ tvers av kommuner nÃ¥r samme datagrunnlag og tjenestelogikk brukes.
- Styrker kontrollen med personvern og hjemmelsbruk gjennom felles roller og dataminimering.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Bruk uten riktig hjemmel eller feil tjenesteomrÃ¥de kan gi urettmessig innsyn i taushetsbelagte opplysninger. | Tydelig kobling mellom rolle, tjenesteomrÃ¥de og hjemmel, samt lokal kontroll av behandlingsgrunnlag. |
| Teknisk | Endringer i Skatteetatens API-er eller i Fiks-overbygget kan pÃ¥virke kommunale beregningslÃ¸p. | Versjonsstyring, testmiljÃ¸, endringslogg og koordinert innfÃ¸ring i fagsystemer. |
| Sikkerhet | Tjenesten hÃ¥ndterer sensitive opplysninger som mÃ¥ begrenses til riktig bruker og kontekst. | Rollebasert tilgang, dataminimering, logging og sikker integrasjon via Fiks-plattformen. |
| LeverandÃ¸r | Kommunene blir avhengige av bÃ¥de KS Digital som segment- og tjenesteforvalter og Skatteetatens underliggende delingstjenester. | Tydelige avtaler, dokumenterte grensesnitt og lÃ¸pende koordinering mellom aktÃ¸rene. |
| Brukeropplevelse | LÃ¸sningen gir lav verdi hvis tjenesteomrÃ¥der, roller eller integrasjoner settes opp feil lokalt. | Gode veiledere, tydelig oppsett i Fiks forvaltning og tett samspill med systemleverandÃ¸rer. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-register/fiks-skatte-og-inntektsopplysninger/
- https://developers.fiks.ks.no/tjenester/register/skatteoginntektsopplysninger_ny/
- https://developers.fiks.ks.no/tjenester/register/skatteoginntektsopplysninger_proxy/
- https://ksdigital.no/tjenestene/segmentsamarbeid/
- https://ksdigital.no/avtaler-og-priser/fakturalinjer/

## Plattform
Fiks skatte- og inntektsopplysninger er en registertilgangstjeneste i KS Digital og en undertjeneste under Fiks register.

**Fakta:**
- Tjenesten tilbys bÃ¥de som nettsidelÃ¸sning og maskin-til-maskin-integrasjon.
- Utviklerdokumentasjonen viser test- og produksjonsmiljÃ¸ pÃ¥ Fiks-plattformen og et eget overbygg i tillegg til proxy mot Skatteetatens API-er.
- Produktet er knyttet til segmentsamarbeidet mellom KS, KS Digital og Skatteetaten for kommunal tilgang til delte opplysninger.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full intern driftsarkitektur, detaljer om intern prioritering i veikartet og full finansieringsmodell bak sentral forvaltning.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Samme tjenestegrunnlag kan brukes av mange kommuner med lignende behov for inntektsgrunnlag i lovregulerte tjenester.
- Gjenbruksverdien ligger i felles tilgangsmÃ¸nster, beregningsnÃ¦rt overbygg og felles styring av hjemmel og roller.
- Produktet kan gjenbrukes pÃ¥ tvers av flere tjenesteomrÃ¥der, men bare der hjemmelsgrunnlaget og tjenstlig behov faktisk er pÃ¥ plass.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** - lÃ¸sningen gjÃ¸r autoritative skatte- og inntektsopplysninger tilgjengelige for gjenbruk i kommunale arbeidsprosesser der det finnes hjemmel og behov.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** - produktet bygger pÃ¥ rollebasert tilgang, dataminimering og tjenesteomrÃ¥debasert hjemmelsstyring for Ã¥ begrense innsyn til det som er nÃ¸dvendig.

## Finansiering
**Fakta:** KS Digitals fakturalinjer viser at Fiks register har egen fastpris og innbyggerpris for undertjenestene Folkeregister og Skatte- og inntektsopplysninger, og at tjenesten ogsÃ¥ har en Digifin prosjektavgift for kommuner.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full prismodell per kundetype og full intern budsjettfordeling mellom KS, KS Digital og tilknyttede aktÃ¸rer.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktside, utviklerdokumentasjon og avtaleinformasjon ligger hos KS Digital. |
| Driftsansvar | KS Digital | Tjenesten forvaltes pÃ¥ Fiks-plattformen, men full intern driftsmodell er ikke offentlig detaljert dokumentert. |
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
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v1-codex.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/67-FIKS-Folkeregister-produkt-canvas-v1-codex.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/fiks-skatte-og-inntektsopplysninger/ (hentet 2026-03-26)
- Nettkilde: https://developers.fiks.ks.no/tjenester/register/skatteoginntektsopplysninger_ny/ (hentet 2026-03-26)
- Nettkilde: https://developers.fiks.ks.no/tjenester/register/skatteoginntektsopplysninger_proxy/ (hentet 2026-03-26)
- Nettkilde: https://ksdigital.no/tjenestene/segmentsamarbeid/ (hentet 2026-03-26)
- Nettkilde: https://ksdigital.no/avtaler-og-priser/fakturalinjer/ (hentet 2026-03-26)

