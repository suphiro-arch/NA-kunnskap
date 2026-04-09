# Produkt-canvas: Fiks folkeregister

## Navn
Fiks folkeregister

## Ressurs ID
KS-008

## Status/Livsfase
**Produksjon** - etablert registertilgangstjeneste i KS Digital for oppslag og integrasjon mot Folkeregisteret i kommunal sektor.

**Fakta:** KS beskriver FIKS Folkeregister som en tjeneste som gir kommuner og fylkeskommuner tilgang til Folkeregisteret. Statussiden for FIKS viser `Folkeregister` som operativ komponent.

## Modenhet
**HÃ¸y funksjonell modenhet** - lÃ¸sningen er bredt tatt i bruk, har publiserte avtalevilkÃ¥r, tydelig rolle- og tilgangsmodell og egne oppdaterings- og endringssider.
- KS opplyser at de fleste kommuner har avtale om Ã¥ bruke tjenesten.
- Kildene viser bÃ¥de webbasert oppslagsfunksjon og maskin-til-maskin-integrasjon mot fagsystemer.
- Modenheten er hÃ¸y som tilgangstjeneste, men lÃ¸sningen er fortsatt avhengig av hjemler og vilkÃ¥r knyttet til Folkeregisteret som autoritativ kilde.

## Kort beskrivelse
Fiks folkeregister er en viktig integrasjon i kommunal sektor. LÃ¸sningen gir kommuner og fylkeskommuner tilgang til folkeregisteropplysninger gjennom Fiks, enten som oppslag i en nettsidelÃ¸sning eller som maskin-til-maskin-integrasjon mot fagsystemer. Produktet er sÃ¦rlig relevant nÃ¥r kommunal sektor trenger kontrollert tilgang til oppdaterte personopplysninger fra Folkeregisteret i operative arbeidsprosesser, uten Ã¥ etablere egne separate tilkoblings- og tilgangslÃ¸sninger mot Skatteetaten.

## Kapabiliteter
- **Datakilder: Grunndata** er direkte relevant fordi lÃ¸sningen gjÃ¸r autoritative folkeregisteropplysninger tilgjengelige for kommunal sektor gjennom et kontrollert tilgangslag.
- **Datautveksling og integrasjon: Bruke data fra andre** er kjernefunksjonen fordi kommunale fagsystemer og saksbehandlere bruker lÃ¸sningen for Ã¥ hente data fra en annen virksomhets register i egne prosesser.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals kilder brukt i denne arbeidsÃ¸kten.

## ProduktmÃ¥l
Dokumenterte mÃ¥l:
- Gi kommuner og fylkeskommuner tilgang til folkeregisteret gjennom FIKS.
- Tilby bÃ¥de oppslagsfunksjonalitet og maskin-til-maskin-integrasjon.
- Styrke riktig tilgang gjennom brukerstyring og rollebaserte innsynsmekanismer.

Operative mÃ¥l utledet fra kildene:
- GjÃ¸re bruk av folkeregisterdata enklere i kommunale arbeidsprosesser.
- Redusere behovet for separate tilkoblingsmÃ¸nstre mellom hver kommune og Folkeregisteret.
- Sikre at opplysninger brukes i trÃ¥d med hjemmel, rolle og tjenstlig behov.

## Brukerbehov
- Kommuner trenger oppdaterte folkeregisteropplysninger i saksbehandling og tjenesteproduksjon.
- Fagsystemer trenger en standardisert integrasjon for Ã¥ bruke folkeregisterdata maskinelt.
- Saksbehandlere trenger oppslagsfunksjon for Ã¥ hente relevant informasjon raskt i sine arbeidsprosesser.
- Forvaltere trenger styring av roller, tilgang og vilkÃ¥r for bruk av folkeregisterdata.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Tilgang til oppdaterte folkeregisteropplysninger | Saksbehandling, tjenesteproduksjon og oppslag | PrimÃ¦r mÃ¥lgruppe |
| Fagsystemer og leverandÃ¸rer | Maskin-til-maskin-tilgang til folkeregisterdata | Integrasjon i kommunale arbeidsprosesser | Teknisk brukergruppe |
| Saksbehandlere | Oppslag i person- og kontaktinformasjon ved behov | Operativ bruk i enkeltsaker | Bruker webgrensesnitt og fagstÃ¸tte |
| Forvaltere i kommunal sektor | Rolle- og tilgangsstyring | Administrasjon av hvem som kan se hva | Kritisk for etterlevelse |
| KS Digital | Forvalte tjenesten og samordne tilgangsvilkÃ¥r | Produktforvaltning, videreutvikling og kundestÃ¸tte | Sentral tjenesteforvalter |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- FIKS Folkeregister gir kommuner og fylkeskommuner tilgang til folkeregisteropplysninger gjennom FIKS. Dette gjÃ¸r lÃ¸sningen relevant nÃ¥r en kommune trenger direkte bruk av grunndata fra Folkeregisteret, men Ã¸nsker et felles kommunalt tilgangslag.
- Tjenesten er tilgjengelig bÃ¥de som nettsidelÃ¸sning med oppslagsfunksjonalitet og som maskin-til-maskin-integrasjon. Det skiller produktet fra en ren portal, fordi samme ressurs ogsÃ¥ dekker teknisk integrasjon i fagsystemer.
- LÃ¸sningen er brukerstyrt slik at saksbehandlere bare fÃ¥r tilgang til informasjon de har behov for. Det gjÃ¸r rolle- og tilgangsstyring til en del av funksjonsforstÃ¥elsen, ikke bare en administrativ detalj.
- Tjenesten er koblet til kontaktregisteret pÃ¥ oppslagsnivÃ¥. Det gjÃ¸r at den i praksis sammenstiller opplysninger som er nyttige i arbeidsprosesser, samtidig som kildedata fortsatt kommer direkte fra Folkeregisteret og tilhÃ¸rende autoritative kilder.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Oppslag i og integrasjon mot Folkeregisteret via FIKS | Eierskap til Folkeregisteret eller folkeregisterdataene |
| Rolle- og tilgangsstyrt bruk av folkeregisteropplysninger | Selvstendig kommunal registerforvaltning |
| Weboppslag og maskin-til-maskin-bruk i fagsystemer | Fri bruk uten hjemmel eller vilkÃ¥r |
| Sammenstilling for tjenstlig bruk i kommunale prosesser | Full lokal kopi eller alternativ autoritativ kilde |

## Veikart over kommende funksjonalitet
**Fakta:** Jeg fant ikke et samlet offentlig roadmap for FIKS Folkeregister i denne arbeidsÃ¸kten. KS publiserer derimot produktbeskrivelse, endringslogg for FIKS Register og lÃ¸pende informasjon om leveranser og endringer.

**Deduksjon:** Videreutviklingen vil trolig vÃ¦re knyttet til nye oppslags- og hendelsesfunksjoner, bedre rolleforvaltning og justeringer som fÃ¸lger endringer i Folkeregisteret og kommunale behov.

## Forretningsverdi/Verdiforslag
### For kommuner og fylkeskommuner
- GjÃ¸r tilgang til folkeregisteropplysninger enklere og mer standardisert.
- Reduserer behovet for Ã¥ etablere egne kommunespesifikke tilkoblinger og oppslagslÃ¸sninger.

### For fagsystemer og leverandÃ¸rer
- Gir et felles integrasjonsmÃ¸nster for bruk av folkeregisterdata i kommunale prosesser.
- Forenkler utvikling av systemstÃ¸tte der personopplysninger er en nÃ¸dvendig del av saksbehandlingen.

### For sektoren
- StÃ¸tter mer ensartet bruk av nasjonale grunndata i kommunal sektor.
- Bidrar til at autoritative persondata brukes direkte fra kilden i stedet for gjennom lokale mellomlag.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Bruk uten riktig hjemmel eller for bred tilgang kan gi alvorlige regelverksbrudd. | Tydelige vilkÃ¥r, rollebasert tilgang og lokal kontroll av behandlingsgrunnlag. |
| Teknisk | Endringer i underliggende register eller integrasjoner kan pÃ¥virke mange kommuner samtidig. | God endringshÃ¥ndtering, testlÃ¸p og tydelig informasjon om oppdateringer. |
| Sikkerhet | Folkeregisteropplysninger er sensitive og mÃ¥ skjermes mot uautorisert bruk. | Streng tilgangsstyring, logging og kontroll av hvem som fÃ¥r se hvilke data. |
| LeverandÃ¸r | Kommuner blir avhengige av KS Digital som tilgangslag og av Skatteetatens vilkÃ¥r for kildebruk. | Tydelige avtaler, robust forvaltning og klar ansvarsdeling mellom aktÃ¸rene. |
| Brukeropplevelse | LÃ¸sningen mister verdi hvis oppslag og integrasjon ikke passer lokale arbeidsprosesser. | Kombinere weboppslag og maskinell bruk, samt tydelig veiledning for oppsett og roller. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-register/fiks-folkeregister-2/
- https://ksdigital.no/tjenestene/fiks-register/
- https://status.fiks.ks.no

## Plattform
FIKS Folkeregister er en registertilgangstjeneste i KS Digital og inngÃ¥r funksjonelt i FIKS Register-familien.

**Fakta:**
- Tjenesten tilbys bÃ¥de som nettsidelÃ¸sning og maskin-til-maskin-integrasjon.
- Statussiden viser `Folkeregister` som operativ komponent.
- Avtaler og priser viser at bruk krever godkjenning av Skatteetatens bruksvilkÃ¥r og delegering av rettigheter via Altinn.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsarkitektur, detaljert teknologistakk og full prioritering av kommende leveranser.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Samme tjenestegrunnlag kan brukes av mange kommuner og fylkeskommuner med behov for folkeregisterdata.
- Gjenbruksverdien ligger i standardisert tilgangsmÃ¸nster, rolleforvaltning og integrasjon, ikke i at KS Digital er eier av de underliggende dataene.

## StÃ¸tter arkitekturprinsipper
- **P4 Del og gjenbruk data** - lÃ¸sningen gjÃ¸r autoritative folkeregisterdata tilgjengelige for gjenbruk i kommunale arbeidsprosesser.
- **P7 SÃ¸rg for tillit til oppgavelÃ¸sningen** - tilgang styres etter roller, hjemmel og dokumenterte vilkÃ¥r, noe som er avgjÃ¸rende for trygg bruk av personopplysninger.

## Finansiering
**Fakta:** KS opplyser at kommuner og fylkeskommuner mÃ¥ godkjenne Skatteetatens bruksvilkÃ¥r og delegere rettighet til KS for Ã¥ fÃ¥ tilgang til FIKS Folkeregister.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full prismodell for sentral forvaltning og videreutvikling av tjenesten.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsidene og avtaleinformasjonen ligger hos KS Digital. |
| Driftsansvar | Ikke offentlig detaljert spesifisert i brukte kilder | Statusside viser operativ drift, men ikke full intern driftsmodell. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Avtale- og vilkÃ¥rssiden sier noe om tilgangskrav, men ikke full finansieringsmodell. |
| Styringsmodell | KS Digital som forvalter i samspill med Skatteetatens vilkÃ¥r for kildebruk | FremgÃ¥r av produkt- og avtalesidene. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-register/fiks-folkeregister-2/
- https://ksdigital.no/tjenestene/fiks-register/
- https://status.fiks.ks.no

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/fiks-folkeregister-2/ (hentet 2026-03-19)
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/ (hentet 2026-03-19)
- Nettkilde: https://ksdigital.no/avtaler-og-priser/ (hentet 2026-03-19)
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/fiks_register_endringslogg/ (hentet 2026-03-19)
- Nettkilde: https://status.fiks.ks.no/ (hentet 2026-03-19)

