# Produkt-canvas: Fiks kjÃ¸retÃ¸yregister

## Navn
Fiks kjÃ¸retÃ¸yregister

## Ressurs ID
KS-010

## Status/Livsfase
**Produksjon** - etablert registertilgangstjeneste i KS Digital for oppslag i Statens vegvesens kjÃ¸retÃ¸yregister fra kommunale fagsystemer.

**Fakta:** KS Digital beskriver tjenesten som et API for kommunens fagsystemer, og utviklerdokumentasjonen viser operative endepunkter for bÃ¥de test og produksjon pÃ¥ Fiks-plattformen.

## Modenhet
**Middels til hÃ¸y funksjonell modenhet** - lÃ¸sningen har tydelig teknisk avgrensning, publisert integrasjonsmÃ¸nster og konkret bruk i kommunale arbeidsprosesser, men er smalere enn de bredere registertjenestene i Fiks register.

- Produktsiden beskriver tjenesten som et eget API med krav om integrasjon i fagsystem.
- Teknisk dokumentasjon viser konkrete oppslagsmetoder, URL-struktur og autentiseringskrav.
- KS Digital opplyser at et administrativt grensesnitt kan bli vurdert senere, noe som tyder pÃ¥ at dagens tjeneste primÃ¦rt er laget for integrert bruk.

**Deduksjon:** Produktet er modent som maskin-til-maskin-tjeneste for oppslag i kjÃ¸retÃ¸ydata, men mindre modent som bred brukerflate siden det forelÃ¸pig ikke tilbys som ordinÃ¦r portal for saksbehandlere.

## Kort beskrivelse
Fiks kjÃ¸retÃ¸yregister er KS Digitals API-baserte tilgangstjeneste til Statens vegvesens kjÃ¸retÃ¸yregister via Fiks-plattformen. Produktet gjÃ¸r det mulig for kommunale fagsystemer Ã¥ slÃ¥ opp kjÃ¸retÃ¸y og eierforhold uten Ã¥ etablere egne separate tilkoblinger mot Statens vegvesens grensesnitt. LÃ¸sningen speiler sentrale oppslagstjenester fra kilden, men legger dem inn i Fiks sitt autentiserings- og integrasjonsmÃ¸nster. Produktet er sÃ¦rlig relevant der kommuner trenger kjÃ¸retÃ¸yopplysninger som del av operative prosesser som parkering, gebyrhÃ¥ndtering, feilparkering, brÃ¸yting og andre oppgaver knyttet til kjÃ¸retÃ¸y i kommunal forvaltning.

## Kapabiliteter
- **Datakilder: Grunndata** er direkte relevant fordi lÃ¸sningen gjÃ¸r autoritative kjÃ¸retÃ¸yopplysninger fra Statens vegvesen tilgjengelige for kommunal sektor gjennom et kontrollert tilgangslag.
- **Datautveksling og integrasjon: Bruke data fra andre** er kjernefunksjonen fordi kommunale fagsystemer bruker lÃ¸sningen til Ã¥ hente data fra en annen virksomhets register i egne operative prosesser.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals produkt- og utviklerdokumentasjon kontrollert 2026-03-26.

## ProduktmÃ¥l
Dokumenterte mÃ¥l:
- Gi kommunale fagsystemer tilgang til Statens vegvesens kjÃ¸retÃ¸yregister via Fiks-plattformen.
- Speile utvalgte oppslags- og sÃ¸ketjenester fra kilden i et standardisert kommunalt integrasjonsmÃ¸nster.
- Forenkle bruk av kjÃ¸retÃ¸ydata i kommunale arbeidsprosesser.

Operative mÃ¥l utledet fra kildene:
- Redusere behovet for egne punkt-til-punkt-integrasjoner mot Statens vegvesen for hver kommune eller leverandÃ¸r.
- GjÃ¸re det enklere Ã¥ bruke oppdaterte kjÃ¸retÃ¸y- og eieropplysninger i kommunale fagsystemer.
- Sikre at tilgang til data fÃ¸lger Fiks-plattformens autentiserings- og oppsettsmodell.

## Brukerbehov
- Kommuner trenger kjÃ¸retÃ¸yopplysninger i operative prosesser som parkering, gebyrer og hÃ¥ndtering av kjÃ¸retÃ¸y pÃ¥ kommunal grunn.
- FagsystemleverandÃ¸rer trenger et tydelig og stabilt integrasjonsmÃ¸nster for oppslag mot kjÃ¸retÃ¸ydata.
- Lokale administratorer trenger en enkel mÃ¥te Ã¥ konfigurere integrasjon, tilgang og organisasjonsknytning i Fiks.
- Kommunal sektor trenger tilgang til oppdaterte opplysninger direkte fra kilden, ikke via manuelle mellomledd.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Tilgang til oppdaterte kjÃ¸retÃ¸yopplysninger i operative prosesser | Parkeringsforvaltning, gebyrer, kjÃ¸retÃ¸yrelaterte oppgaver i kommunen | PrimÃ¦r mÃ¥lgruppe |
| Fagsystemer og leverandÃ¸rer | API-tilgang og standardisert autentisering | Integrasjon i systemer for parkering, gebyr og annen kommunal saksbehandling | Teknisk brukergruppe |
| Fiks-administratorer | Oppsett av integrasjon, tilgang og organisasjonskobling | Konfigurasjon i Fiks forvaltning og deling av integrasjonsdata til leverandÃ¸r | Lokal forvaltningsrolle |
| KS Digital | Forvalte produktet og integrasjonsmÃ¸nsteret | Produktforvaltning, dokumentasjon og kundestÃ¸tte | Sentral tjenesteforvalter |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
Fiks kjÃ¸retÃ¸yregister sin kjernefunksjon er Ã¥ gjÃ¸re oppslag i Statens vegvesens kjÃ¸retÃ¸yregister tilgjengelig gjennom Fiks-plattformen. Produktet er derfor en spesialisert registertilgangstjeneste for maskin-til-maskin-bruk, ikke en generell kjÃ¸retÃ¸yportal eller en egen kommunal datakilde.

LÃ¸sningen speiler sentrale oppslags- og sÃ¸kemuligheter fra kilden, blant annet oppslag pÃ¥ kjennemerke, kuid og understellsnummer, samt sÃ¸k i kjÃ¸retÃ¸ydata. Den gjÃ¸r det ogsÃ¥ mulig Ã¥ hente informasjon pÃ¥ et bestemt tidspunkt. Dette er viktig i kommunale arbeidsprosesser der tidspunktet for oppslaget har betydning, for eksempel nÃ¥r kommunen skal fÃ¸lge opp parkering eller annen hendelsesbasert saksbehandling.

Produktet har en tydelig teknisk avgrensning: det brukes gjennom integrasjon i fagsystemer. KS Digital oppgir at webportal ikke stÃ¸ttes i dag, og utviklerdokumentasjonen beskriver tjenesten som maskin-til-maskin-integrasjon. Samtidig er produktet ikke bare et rÃ¥tt videresendt API, fordi Fiks legger pÃ¥ eget autentiserings- og konfigurasjonsmÃ¸nster med Maskinporten, Fiks-organisasjons-ID og integrasjonspassord.

En viktig del av funksjonen ligger derfor i standardiseringen av tilgangslÃ¸pet for kommunal sektor. Kommunen eller leverandÃ¸ren forholder seg til Fiks-konfigurasjon, Fiks-autentisering og et kjent oppsettsmÃ¸nster, mens de underliggende kjÃ¸retÃ¸ydataene fortsatt kommer direkte fra Statens vegvesen. Produktet skaper dermed verdi som kommunalt tilgangslag og ikke som alternativ kilde til kjÃ¸retÃ¸yinformasjon.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| API-basert oppslag i Statens vegvesens kjÃ¸retÃ¸yregister via Fiks | Eierskap til kjÃ¸retÃ¸yregisteret eller dataene i kilden |
| Standardisert autentisering og integrasjonsmÃ¸nster pÃ¥ Fiks-plattformen | Generell webportal for saksbehandlere |
| Oppslag pÃ¥ blant annet kjennemerke, kuid og understellsnummer | Lokal saksbehandling, vedtakslogikk eller gebyrbehandling |
| Bruk i kommunale fagsystemer for operative kjÃ¸retÃ¸yrelaterte behov | Full erstatning for Statens vegvesens faglige dokumentasjon og kildeansvar |

## Veikart over kommende funksjonalitet
**Fakta:** Utviklerdokumentasjonen opplyser at det pÃ¥ sikt vil bli vurdert Ã¥ utvikle et administrativt grensesnitt mot Fiks kjÃ¸retÃ¸yregister for kommuneansatte. Jeg fant ikke et samlet offentlig veikart med tidsfestede milepÃ¦ler utover dette i denne arbeidsÃ¸kten.

**Deduksjon:** Videreutviklingen vil trolig handle om forbedret administrativ stÃ¸tte og lÃ¸pende tilpasning til endringer i Statens vegvesens grensesnitt og kommunale behov.

## Forretningsverdi/Verdiforslag
### For kommuner og fylkeskommuner
- GjÃ¸r det enklere Ã¥ bruke oppdaterte kjÃ¸retÃ¸yopplysninger i operative prosesser uten egne spesialintegrasjoner mot Statens vegvesen.
- Reduserer innfÃ¸ringsarbeidet for kommuner som allerede bruker Fiks-plattformen.

### For leverandÃ¸rer
- Gir et kjent kommunalt integrasjonsmÃ¸nster med standard autentisering og oppsett.
- Forenkler utvikling av fagsystemstÃ¸tte for kjÃ¸retÃ¸yrelaterte arbeidsprosesser.

### For sektoren
- Bidrar til mer ensartet bruk av kjÃ¸retÃ¸ydata i kommunal sektor.
- Styrker gjenbruk av felles infrastruktur i stedet for parallelle lokale oppkoblinger.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Feil bruk av eier- og kjÃ¸retÃ¸yopplysninger kan gi brudd pÃ¥ regelverk eller bruksvilkÃ¥r. | Tydelige avtaler, lokal kontroll av behandlingsgrunnlag og avgrenset bruk til tjenstlig behov. |
| Teknisk | Endringer i underliggende Swagger-spesifikasjon eller hos Statens vegvesen kan pÃ¥virke integrasjonene raskt. | VersjonsoppfÃ¸lging, testmiljÃ¸ og koordinert dialog med leverandÃ¸rer og KS Digital. |
| Sikkerhet | Feil hÃ¥ndtering av token, integrasjonsdata eller oppslagsrettigheter kan gi uautorisert tilgang. | Maskinporten-basert autentisering, kontrollert konfigurasjon og sikker hÃ¥ndtering av integrasjonspassord. |
| LeverandÃ¸r | Kommunen er avhengig av bÃ¥de KS Digital som tilgangslag og Statens vegvesen som datakilde. | Tydelig dokumentasjon, robust forvaltning og kjent ansvarsdeling mellom aktÃ¸rene. |
| Brukeropplevelse | Verdien faller hvis fagsystemet ikke stÃ¸tter tjenesten eller integrasjonen settes opp feil. | Kreve leverandÃ¸rstÃ¸tte, bruke Fiks-konfigurasjon riktig og gi tydelige veiledere for oppsett. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-kjoretoyregister/
- https://developers.fiks.ks.no/tjenester/kjoretoyregister/
- https://ksdigital.no/tjenestene/fiks-register/
- https://ksdigital.no/avtaler-og-priser/fakturalinjer/

## Plattform
Fiks kjÃ¸retÃ¸yregister er en registertilgangstjeneste pÃ¥ KS Digitals Fiks-plattform og fungerer som et kommunalt tilgangslag mot Statens vegvesens kjÃ¸retÃ¸yregister.

**Fakta:**
- Tjenesten brukes i dag som maskin-til-maskin-integrasjon og har ikke ordinÃ¦r webportal i produksjon.
- Autentisering skjer pÃ¥ Fiks-plattformen med access token fra Maskinporten og egne Fiks-integrasjonsopplysninger.
- Det finnes egne URL-er for test- og produksjonsmiljÃ¸ pÃ¥ Fiks-plattformen.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full intern driftsarkitektur, intern prioritering av videreutvikling og detaljer om overvÃ¥kning og SLA utover det som fÃ¸lger av Fiks-plattformen generelt.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet kan brukes av mange kommuner med likeartede behov for kjÃ¸retÃ¸yopplysninger i operative arbeidsprosesser.
- Gjenbruksverdien ligger i felles autentiserings- og integrasjonsmÃ¸nster, ikke i at KS Digital eier de underliggende dataene.
- LÃ¸sningen er sÃ¦rlig relevant nÃ¥r flere kommuner eller leverandÃ¸rer trenger samme type oppslag uten Ã¥ bygge egne tilkoblinger mot kilden.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** - lÃ¸sningen gjÃ¸r autoritative kjÃ¸retÃ¸yopplysninger tilgjengelige for gjenbruk i kommunale systemer gjennom et felles tilgangslag.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** - produktet bygger pÃ¥ standard autentisering fra Maskinporten og kontrollert oppsett i Fiks-plattformen fÃ¸r data kan brukes.

## Finansiering
**Fakta:** KS Digitals fakturalinjer viser at Fiks kjÃ¸retÃ¸yregister har fastpris, innbyggerpris og Digifin prosjektavgift.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full prisdifferensiering mellom ulike kundegrupper og full intern finansieringsmodell for sentral forvaltning og drift.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktside, veiledning og teknisk dokumentasjon ligger hos KS Digital. |
| Driftsansvar | KS Digital | Tjenesten leveres pÃ¥ Fiks-plattformen, men full intern driftsmodell er ikke offentlig detaljert dokumentert. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Fakturalinjer viser prismodell, men ikke full budsjettstyring. |
| Styringsmodell | KS Digital som tjenesteforvalter i samspill med Statens vegvesens kildetjenester | FremgÃ¥r av produktside og teknisk dokumentasjon. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-kjoretoyregister/
- https://developers.fiks.ks.no/tjenester/kjoretoyregister/
- https://ksdigital.no/tjenestene/fiks-register/
- https://ksdigital.no/avtaler-og-priser/fakturalinjer/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v1-codex.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-kjoretoyregister/ (hentet 2026-03-26)
- Nettkilde: https://developers.fiks.ks.no/tjenester/kjoretoyregister/ (hentet 2026-03-26)
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/ (hentet 2026-03-26)
- Nettkilde: https://ksdigital.no/avtaler-og-priser/fakturalinjer/ (hentet 2026-03-26)

