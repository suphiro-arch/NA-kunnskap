# Produkt-canvas: Fiks folkeregister

## Navn
Fiks folkeregister

## Ressurs ID
KS-008

## Status/Livsfase
**Produksjon** - etablert registertilgangstjeneste i KS Digital for oppslag og integrasjon mot Folkeregisteret i kommunal sektor.

**Fakta:** KS beskriver FIKS Folkeregister som en tjeneste som gir kommuner og fylkeskommuner tilgang til Folkeregisteret. Statussiden for FIKS viser `Folkeregister` som operativ komponent.

## Modenhet
**Høy funksjonell modenhet** - løsningen er bredt tatt i bruk, har publiserte avtalevilkår, tydelig rolle- og tilgangsmodell og egne oppdaterings- og endringssider.
- KS opplyser at de fleste kommuner har avtale om å bruke tjenesten.
- Kildene viser både webbasert oppslagsfunksjon og maskin-til-maskin-integrasjon mot fagsystemer.
- Modenheten er høy som tilgangstjeneste, men løsningen er fortsatt avhengig av hjemler og vilkår knyttet til Folkeregisteret som autoritativ kilde.

## Kort beskrivelse
Fiks folkeregister er en viktig integrasjon i kommunal sektor. Løsningen gir kommuner og fylkeskommuner tilgang til folkeregisteropplysninger gjennom Fiks, enten som oppslag i en nettsideløsning eller som maskin-til-maskin-integrasjon mot fagsystemer. Produktet er særlig relevant når kommunal sektor trenger kontrollert tilgang til oppdaterte personopplysninger fra Folkeregisteret i operative arbeidsprosesser, uten å etablere egne separate tilkoblings- og tilgangsløsninger mot Skatteetaten.

## Kapabiliteter
- **Datakilder: Grunndata** er direkte relevant fordi løsningen gjør autoritative folkeregisteropplysninger tilgjengelige for kommunal sektor gjennom et kontrollert tilgangslag.
- **Datautveksling og integrasjon: Bruke data fra andre** er kjernefunksjonen fordi kommunale fagsystemer og saksbehandlere bruker løsningen for å hente data fra en annen virksomhets register i egne prosesser.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals kilder brukt i denne arbeidsøkten.

## Produktmål
Dokumenterte mål:
- Gi kommuner og fylkeskommuner tilgang til folkeregisteret gjennom FIKS.
- Tilby både oppslagsfunksjonalitet og maskin-til-maskin-integrasjon.
- Styrke riktig tilgang gjennom brukerstyring og rollebaserte innsynsmekanismer.

Operative mål utledet fra kildene:
- Gjøre bruk av folkeregisterdata enklere i kommunale arbeidsprosesser.
- Redusere behovet for separate tilkoblingsmønstre mellom hver kommune og Folkeregisteret.
- Sikre at opplysninger brukes i tråd med hjemmel, rolle og tjenstlig behov.

## Brukerbehov
- Kommuner trenger oppdaterte folkeregisteropplysninger i saksbehandling og tjenesteproduksjon.
- Fagsystemer trenger en standardisert integrasjon for å bruke folkeregisterdata maskinelt.
- Saksbehandlere trenger oppslagsfunksjon for å hente relevant informasjon raskt i sine arbeidsprosesser.
- Forvaltere trenger styring av roller, tilgang og vilkår for bruk av folkeregisterdata.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Tilgang til oppdaterte folkeregisteropplysninger | Saksbehandling, tjenesteproduksjon og oppslag | Primær målgruppe |
| Fagsystemer og leverandører | Maskin-til-maskin-tilgang til folkeregisterdata | Integrasjon i kommunale arbeidsprosesser | Teknisk brukergruppe |
| Saksbehandlere | Oppslag i person- og kontaktinformasjon ved behov | Operativ bruk i enkeltsaker | Bruker webgrensesnitt og fagstøtte |
| Forvaltere i kommunal sektor | Rolle- og tilgangsstyring | Administrasjon av hvem som kan se hva | Kritisk for etterlevelse |
| KS Digital | Forvalte tjenesten og samordne tilgangsvilkår | Produktforvaltning, videreutvikling og kundestøtte | Sentral tjenesteforvalter |

## Hovedfunksjoner
### Primære funksjoner
- FIKS Folkeregister gir kommuner og fylkeskommuner tilgang til folkeregisteropplysninger gjennom FIKS. Dette gjør løsningen relevant når en kommune trenger direkte bruk av grunndata fra Folkeregisteret, men ønsker et felles kommunalt tilgangslag.
- Tjenesten er tilgjengelig både som nettsideløsning med oppslagsfunksjonalitet og som maskin-til-maskin-integrasjon. Det skiller produktet fra en ren portal, fordi samme ressurs også dekker teknisk integrasjon i fagsystemer.
- Løsningen er brukerstyrt slik at saksbehandlere bare får tilgang til informasjon de har behov for. Det gjør rolle- og tilgangsstyring til en del av funksjonsforståelsen, ikke bare en administrativ detalj.
- Tjenesten er koblet til kontaktregisteret på oppslagsnivå. Det gjør at den i praksis sammenstiller opplysninger som er nyttige i arbeidsprosesser, samtidig som kildedata fortsatt kommer direkte fra Folkeregisteret og tilhørende autoritative kilder.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Oppslag i og integrasjon mot Folkeregisteret via FIKS | Eierskap til Folkeregisteret eller folkeregisterdataene |
| Rolle- og tilgangsstyrt bruk av folkeregisteropplysninger | Selvstendig kommunal registerforvaltning |
| Weboppslag og maskin-til-maskin-bruk i fagsystemer | Fri bruk uten hjemmel eller vilkår |
| Sammenstilling for tjenstlig bruk i kommunale prosesser | Full lokal kopi eller alternativ autoritativ kilde |

## Veikart over kommende funksjonalitet
**Fakta:** Jeg fant ikke et samlet offentlig roadmap for FIKS Folkeregister i denne arbeidsøkten. KS publiserer derimot produktbeskrivelse, endringslogg for FIKS Register og løpende informasjon om leveranser og endringer.

**Deduksjon:** Videreutviklingen vil trolig være knyttet til nye oppslags- og hendelsesfunksjoner, bedre rolleforvaltning og justeringer som følger endringer i Folkeregisteret og kommunale behov.

## Forretningsverdi/Verdiforslag
### For kommuner og fylkeskommuner
- Gjør tilgang til folkeregisteropplysninger enklere og mer standardisert.
- Reduserer behovet for å etablere egne kommunespesifikke tilkoblinger og oppslagsløsninger.

### For fagsystemer og leverandører
- Gir et felles integrasjonsmønster for bruk av folkeregisterdata i kommunale prosesser.
- Forenkler utvikling av systemstøtte der personopplysninger er en nødvendig del av saksbehandlingen.

### For sektoren
- Støtter mer ensartet bruk av nasjonale grunndata i kommunal sektor.
- Bidrar til at autoritative persondata brukes direkte fra kilden i stedet for gjennom lokale mellomlag.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Bruk uten riktig hjemmel eller for bred tilgang kan gi alvorlige regelverksbrudd. | Tydelige vilkår, rollebasert tilgang og lokal kontroll av behandlingsgrunnlag. |
| Teknisk | Endringer i underliggende register eller integrasjoner kan påvirke mange kommuner samtidig. | God endringshåndtering, testløp og tydelig informasjon om oppdateringer. |
| Sikkerhet | Folkeregisteropplysninger er sensitive og må skjermes mot uautorisert bruk. | Streng tilgangsstyring, logging og kontroll av hvem som får se hvilke data. |
| Leverandør | Kommuner blir avhengige av KS Digital som tilgangslag og av Skatteetatens vilkår for kildebruk. | Tydelige avtaler, robust forvaltning og klar ansvarsdeling mellom aktørene. |
| Brukeropplevelse | Løsningen mister verdi hvis oppslag og integrasjon ikke passer lokale arbeidsprosesser. | Kombinere weboppslag og maskinell bruk, samt tydelig veiledning for oppsett og roller. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-register/fiks-folkeregister-2/
- https://ksdigital.no/tjenestene/fiks-register/
- https://status.fiks.ks.no

## Plattform
FIKS Folkeregister er en registertilgangstjeneste i KS Digital og inngår funksjonelt i FIKS Register-familien.

**Fakta:**
- Tjenesten tilbys både som nettsideløsning og maskin-til-maskin-integrasjon.
- Statussiden viser `Folkeregister` som operativ komponent.
- Avtaler og priser viser at bruk krever godkjenning av Skatteetatens bruksvilkår og delegering av rettigheter via Altinn.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsarkitektur, detaljert teknologistakk og full prioritering av kommende leveranser.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme tjenestegrunnlag kan brukes av mange kommuner og fylkeskommuner med behov for folkeregisterdata.
- Gjenbruksverdien ligger i standardisert tilgangsmønster, rolleforvaltning og integrasjon, ikke i at KS Digital er eier av de underliggende dataene.

## Støtter arkitekturprinsipper
- **P4 Del og gjenbruk data** - løsningen gjør autoritative folkeregisterdata tilgjengelige for gjenbruk i kommunale arbeidsprosesser.
- **P7 Sørg for tillit til oppgaveløsningen** - tilgang styres etter roller, hjemmel og dokumenterte vilkår, noe som er avgjørende for trygg bruk av personopplysninger.

## Finansiering
**Fakta:** KS opplyser at kommuner og fylkeskommuner må godkjenne Skatteetatens bruksvilkår og delegere rettighet til KS for å få tilgang til FIKS Folkeregister.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full prismodell for sentral forvaltning og videreutvikling av tjenesten.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsidene og avtaleinformasjonen ligger hos KS Digital. |
| Driftsansvar | Ikke offentlig detaljert spesifisert i brukte kilder | Statusside viser operativ drift, men ikke full intern driftsmodell. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Avtale- og vilkårssiden sier noe om tilgangskrav, men ikke full finansieringsmodell. |
| Styringsmodell | KS Digital som forvalter i samspill med Skatteetatens vilkår for kildebruk | Fremgår av produkt- og avtalesidene. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-register/fiks-folkeregister-2/
- https://ksdigital.no/tjenestene/fiks-register/
- https://status.fiks.ks.no

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/fiks-folkeregister-2/ (hentet 2026-03-19)
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/ (hentet 2026-03-19)
- Nettkilde: https://ksdigital.no/avtaler-og-priser/ (hentet 2026-03-19)
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/fiks_register_endringslogg/ (hentet 2026-03-19)
- Nettkilde: https://status.fiks.ks.no/ (hentet 2026-03-19)
