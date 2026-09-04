# Produkt-canvas: Fiks folkeregister

## Navn
Fiks folkeregister

## Ressurs ID
KS-008

## Status/Livsfase
**Produksjon** - etablert registertilgangstjeneste i KS Digital for oppslag og integrasjon mot Folkeregisteret i kommunal sektor.

**Fakta:** KS Digital beskriver Fiks folkeregister som en tjeneste som gir kommuner og fylkeskommuner tilgang til Folkeregisteret gjennom både nettsideløsning og maskin-til-maskin-integrasjon. Skatteetaten beskriver samtidig at tilgang til folkeregisterdata kan skje gjennom oppslag i nettleser, via systemleverandør eller gjennom standardiserte API-er, og at rettigheter må delegeres via Altinn ved bruk av systemleverandør.

## Modenhet
**Høy funksjonell modenhet** - løsningen har tydelig rolle- og hjemmelsmodell, publisert innføringsløp og både manuell og integrert bruk, men er fortsatt avhengig av Skatteetatens rettighetspakker, vilkår og grensesnitt.

- KS Digital opplyser at de fleste kommuner har avtale med KS om å bruke tjenesten.
- Produktsiden beskriver både nettsideløsning, systemintegrasjon, innbyggerlister og sentralisert brukerstyring.
- Skatteetatens tilgangssider viser at løsningen inngår i et bredere økosystem med Altinn-delegering, Maskinporten og testkrav før produksjonsbruk.

**Deduksjon:** Fiks folkeregister er modent som kommunalt tilgangslag, men må forstås som et kontrollert bruks- og forvaltningsmønster over Folkeregisteret, ikke som en egen alternativ folkeregistertjeneste.

## Kort beskrivelse
Fiks folkeregister gir kommuner og fylkeskommuner kontrollert tilgang til opplysninger fra Folkeregisteret gjennom Fiks. Produktet kan brukes både som oppslagsløsning i Fiks forvaltning og som maskin-til-maskin-integrasjon mot kommunale fagsystemer. Løsningen er særskilt relevant når kommunal sektor trenger oppdaterte person- og kontaktopplysninger i operative arbeidsprosesser, men ønsker å bruke et felles kommunalt tilgangslag med innebygd rolleforvaltning, dataminimering og hjemmelsstyring.

## Kapabiliteter
- **Datakilder: Grunndata** er direkte relevant fordi løsningen gjør autoritative folkeregisteropplysninger tilgjengelige for kommunal sektor gjennom et kontrollert tilgangslag.
- **Datautveksling og integrasjon: Bruke data fra andre** er kjernefunksjonen fordi kommunale fagsystemer og saksbehandlere bruker løsningen for å hente data fra en annen virksomhets register i egne prosesser.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals og Skatteetatens kilder kontrollert 2026-05-26.

## Produktmål
Dokumenterte mål:
- Gi kommuner og fylkeskommuner tilgang til Folkeregisteret gjennom Fiks.
- Tilby både oppslagsfunksjonalitet og maskin-til-maskin-integrasjon.
- Styrke riktig tilgang gjennom roller, dataminimering og tjenesteområdebasert bruk.

Operative mål utledet fra kildene:
- Gjøre bruk av folkeregisterdata enklere i kommunale arbeidsprosesser uten at hver kommune må etablere egne løp mot Skatteetaten.
- Gjøre det mulig å styre hvilke opplysninger ansatte og integrasjoner faktisk får se, basert på tjenstlig behov.
- Koble folkeregisterdata til kommunens identitets- og fagsystemlandskap på en mer ensartet måte.

## Brukerbehov
- Kommuner trenger oppdaterte folkeregisteropplysninger i saksbehandling og tjenesteproduksjon.
- Saksbehandlere trenger søk og oppslag som er tilpasset deres rolle og tjenesteområde.
- Fagsystemer trenger en standardisert integrasjon for å bruke folkeregisterdata maskinelt.
- Forvaltere trenger styring av roller, tilgang, Altinn-delegering og eventuelt sentralisert brukerstyring.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Tilgang til oppdaterte folkeregisteropplysninger | Saksbehandling, tjenesteproduksjon og oppslag | Primær målgruppe |
| Saksbehandlere | Oppslag i person- og kontaktinformasjon ved behov | Operativ bruk i enkeltsaker og bestilling av innbyggerlister | Bruker webgrensesnittet direkte |
| Fagsystemer og leverandører | Maskin-til-maskin-tilgang til folkeregisterdata | Integrasjon i kommunale arbeidsprosesser | Teknisk brukergruppe |
| Lokale forvaltere og identitetsmiljøer | Rolleforvaltning, dataminimering og synkronisering av tilgang | Oppsett av lokale roller og eventuelt sentralisert brukerstyring | Kritisk for etterlevelse |
| KS Digital | Forvalte tjenesten og samordne tilgangsvilkår | Produktforvaltning, videreutvikling og kundestøtte | Sentral tjenesteforvalter |

## Hovedfunksjoner
### Primære funksjoner
Fiks folkeregister sin kjernefunksjon er å gjøre folkeregisteropplysninger tilgjengelige for kommunal sektor gjennom et kontrollert tilgangslag. Produktet er derfor ikke en egen datakilde, men en operativ tjeneste som gjør det enklere å bruke autoritative personopplysninger i kommunale arbeidsprosesser uten å bygge og forvalte egne separate løp mot Skatteetaten.

Løsningen har to tydelige leveranseflater. Den ene er nettsideløsningen i Fiks forvaltning, der ansatte kan gjøre oppslag på enkeltpersoner og bestille innbyggerlister basert på rollen sin. Den andre er maskin-til-maskin-integrasjon mot fagsystemer og skjemaløsninger. Dette gjør at produktet dekker både manuell saksbehandlingsstøtte og teknisk integrasjon, og derfor må beskrives bredere enn et rent API.

En sentral del av funksjonen er rolle- og hjemmelsstyring. KS Digital beskriver at roller knyttes til tjenesteområder og lovhjemler, og at disse avgjør hvilke opplysninger ansatte eller integrasjoner får tilgang til. Produktsiden beskriver også sentralisert brukerstyring som et valgfritt mønster der kommunen kan styre tilgang fra eget identitetsstyringssystem, så lenge synkronisering mot Fiks er satt opp.

Skatteetatens tilgangssider viser at løsningen samtidig inngår i et bredere delingsregime med Altinn-delegering, Maskinporten og teknisk testing før produksjonsbruk. Fiks folkeregister skaper dermed verdi både som ferdig brukerflate og som kontrollert systemleverandørmønster for kommunal bruk av Folkeregisteret.

### Typiske brukssituasjoner (generisk)
- Når saksbehandlere trenger oppdaterte person- og kontaktopplysninger direkte i en operativ sak.
- Når kommunen vil gi fagsystemer tilgang til folkeregisterdata uten å bygge et eget integrasjonsløp mot Skatteetaten.
- Når kommunen trenger rollebasert innsyn og dataminimering tilpasset ulike tjenesteområder.

### Når Fiks folkeregister normalt ikke er førstevalg
- Når virksomheten ligger utenfor kommunesegmentet og ikke skal bruke KS Digitals tilgangs- og forvaltningsmodell.
- Når behovet er direkte bruk av Skatteetatens egne uttrekk, hendelseslister eller andre funksjoner som ikke er dokumentert som del av Fiks-løsningen.
- Når kommunen mangler hjemmel, rolleavklaring eller forvaltningskapasitet til å styre tilgang på en forsvarlig måte.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Oppslag i og integrasjon mot Folkeregisteret via Fiks | Eierskap til Folkeregisteret eller folkeregisterdataene |
| Rolle- og tilgangsstyrt bruk av folkeregisteropplysninger | Selvstendig kommunal registerforvaltning |
| Weboppslag, innbyggerlister og maskin-til-maskin-bruk i fagsystemer | Fri bruk uten hjemmel eller vilkår |
| Tilgangsforvaltning og eventuelt sentralisert brukerstyring | Full bruk av alle Folkeregisterets tekniske muligheter utenfor Fiks-løsningen |

## Veikart over kommende funksjonalitet
**Fakta:** Jeg fant ikke et samlet offentlig roadmap for Fiks folkeregister i denne arbeidsøkten. KS Digital beskriver derimot sentralisert brukerstyring som etablert funksjon og peker til tekniske veiledere og løpende veiledningsmateriell.

**Deduksjon:** Videreutviklingen vil trolig være knyttet til bedre tilgangsforvaltning, løpende tilpasning til Skatteetatens delingstjenester og videre modning av integrasjons- og brukerstyringsmønstre.

## Forretningsverdi/Verdiforslag
### For kommuner og fylkeskommuner
- Gjør tilgang til folkeregisteropplysninger enklere og mer standardisert.
- Reduserer behovet for egne kommunespesifikke tilkoblinger og lokale oppslagsløsninger.

### For saksbehandlere og fagmiljøer
- Gir rask tilgang til relevante opplysninger direkte i arbeidsprosessen.
- Støtter oppslag og innbyggerlister med innhold som er avgrenset av rolle og tjenstlig behov.

### For leverandører og sektoren
- Gir et felles integrasjonsmønster for bruk av folkeregisterdata i kommunale prosesser.
- Støtter mer ensartet bruk av nasjonale grunndata i kommunal sektor.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Bruk uten riktig hjemmel eller for bred tilgang kan gi alvorlige regelverksbrudd. | Tydelige vilkår, rollebasert tilgang, Altinn-delegering og lokal kontroll av behandlingsgrunnlag. |
| Teknisk | Endringer i Skatteetatens grensesnitt, rettighetspakker eller testkrav kan påvirke mange kommuner samtidig. | God endringshåndtering, testløp, teknisk dokumentasjon og koordinert dialog med leverandører. |
| Sikkerhet | Folkeregisteropplysninger er sensitive og må skjermes mot uautorisert bruk. | Streng tilgangsstyring, dataminimering, logging og sikker håndtering av integrasjoner. |
| Leverandør | Kommuner blir avhengige av KS Digital som tilgangslag og av Skatteetatens vilkår og tekniske rammer. | Tydelige avtaler, robust forvaltning og klar ansvarsdeling mellom aktørene. |
| Brukeropplevelse | Verdien faller hvis roller, innbyggerlister eller integrasjoner ikke passer lokale arbeidsprosesser. | Tydelige veiledere, god lokal rolleforvaltning og trinnvis innføring sammen med systemleverandør. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-register/fiks-folkeregister/
- https://ksdigital.no/tjenestene/fiks-register/
- https://forvaltning.fiks.ks.no/
- https://www.skatteetaten.no/nn/deling/folkeregisteret/intro/fa-tilgang/

## Plattform
Fiks folkeregister er en registertilgangstjeneste i KS Digital og inngår funksjonelt i Fiks register-familien (`KS-004`), der KS Digital beskriver Folkeregisteret som én av fire datakilder.

**Fakta:**
- Tjenesten tilbys både som nettsideløsning og maskin-til-maskin-integrasjon.
- Skatteetaten beskriver Altinn-delegering, Maskinporten og test som sentrale deler av tilgangsløpet ved systembruk.
- Produktsiden beskriver sentralisert brukerstyring som mulig tilleggsmønster for lokal tilgangsforvaltning.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full intern driftsarkitektur, detaljert teknologistakk og full prioritering av kommende leveranser.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme tjenestegrunnlag kan brukes av mange kommuner og fylkeskommuner med behov for folkeregisterdata.
- Gjenbruksverdien ligger i standardisert tilgangsmønster, rolleforvaltning og integrasjon, ikke i at KS Digital er eier av de underliggende dataene.

**Vanlige kombinasjoner med andre produkter:**
- Fiks forvaltning for oppslag, innbyggerlister og lokal administrasjon.
- Kommunens identitetsstyringssystem når sentralisert brukerstyring tas i bruk.
- Kommunale fagsystemer og skjemaløsninger som trenger personopplysninger i operative prosesser.

**Kildekode:** Ikke offentlig dokumentert.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** - løsningen gjør autoritative folkeregisterdata tilgjengelige for gjenbruk i kommunale arbeidsprosesser.
- **P7: Sørg for tillit til oppgaveløsningen** - tilgang styres etter roller, hjemmel og dataminimering, noe som er avgjørende for trygg bruk av personopplysninger.
- **Spenning og begrensning:** Det felles tilgangslaget forenkler bruk, men gjør kommunen avhengig av både KS Digital og Skatteetatens styrings- og tilgangsregime. Lokal identitets- og rolleforvaltning blir derfor en kritisk del av innføringen.

## Finansiering
**Fakta:** KS Digital beskriver at tilgangen forutsetter godkjenning av Skatteetatens vilkår, delegering av rettigheter via Altinn og signering av avtaler med KS. Offentlig tilgjengelig prisinformasjon er i praksis knyttet til innloggede avtalesider og overordnet prismodell for Fiks register-familien.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full prismodell og intern budsjettfordeling for Fiks folkeregister som separat tjeneste.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsiden og ta-i-bruk-løpet ligger hos KS Digital. |
| Driftsansvar | KS Digital | Tjenesten leveres på Fiks-plattformen, men full intern driftsmodell er ikke offentlig detaljert dokumentert. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Tilgangsløp og avtaler er publisert, men ikke full budsjettmodell. |
| Styringsmodell | KS Digital forvalter tjenesten i samspill med Skatteetatens tilgangsregime og vilkår | Fremgår av produktinformasjonen og Skatteetatens tilgangsmodell. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-register/fiks-folkeregister/
- https://ksdigital.no/tjenestene/fiks-register/
- https://forvaltning.fiks.ks.no/
- https://www.skatteetaten.no/nn/deling/folkeregisteret/intro/fa-tilgang/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/operative-ressurs-canvas.system.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/67-FIKS-Folkeregister-produkt-canvas-v1-codex.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/fiks-folkeregister/ (hentet 2026-05-26)
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/ (hentet 2026-05-26)
- Nettkilde: https://www.skatteetaten.no/nn/deling/folkeregisteret/intro/fa-tilgang/ (hentet 2026-05-26)

## Endringer fra forrige versjon
### Analyseforbedringer
- Oppdatert kildegrunnlaget med ny kontroll av KS-produktinformasjon og Skatteetatens tilgangsløp 2026-05-26.
- Presisert at tjenesten omfatter både weboppslag, innbyggerlister og systemintegrasjon, ikke bare personoppslag.
- Tydeliggjort samspillet mellom Fiks, Altinn-delegering, Maskinporten og lokal identitetsforvaltning.

### Tekstlige forbedringer
- Lagt inn tydeligere brukssituasjoner og avgrensning mot direkte bruk av Skatteetatens egne grensesnitt.
- Skjerpet gjenbruk, risiko og prinsippvurdering med tydeligere vekt på dataminimering og forvaltningsansvar.
- Strammet inn språk og struktur rundt hva produktet faktisk gjør, og hva det ikke er.
