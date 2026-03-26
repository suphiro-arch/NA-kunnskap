# Produkt-canvas: Fiks kjøretøyregister

## Navn
Fiks kjøretøyregister

## Ressurs ID
KS-010

## Status/Livsfase
**Produksjon** - etablert registertilgangstjeneste i KS Digital for oppslag i Statens vegvesens kjøretøyregister fra kommunale fagsystemer.

**Fakta:** KS Digital beskriver tjenesten som et API for kommunens fagsystemer, og utviklerdokumentasjonen viser operative endepunkter for både test og produksjon på Fiks-plattformen.

## Modenhet
**Middels til høy funksjonell modenhet** - løsningen har tydelig teknisk avgrensning, publisert integrasjonsmønster og konkret bruk i kommunale arbeidsprosesser, men er smalere enn de bredere registertjenestene i Fiks register.

- Produktsiden beskriver tjenesten som et eget API med krav om integrasjon i fagsystem.
- Teknisk dokumentasjon viser konkrete oppslagsmetoder, URL-struktur og autentiseringskrav.
- KS Digital opplyser at et administrativt grensesnitt kan bli vurdert senere, noe som tyder på at dagens tjeneste primært er laget for integrert bruk.

**Deduksjon:** Produktet er modent som maskin-til-maskin-tjeneste for oppslag i kjøretøydata, men mindre modent som bred brukerflate siden det foreløpig ikke tilbys som ordinær portal for saksbehandlere.

## Kort beskrivelse
Fiks kjøretøyregister er KS Digitals API-baserte tilgangstjeneste til Statens vegvesens kjøretøyregister via Fiks-plattformen. Produktet gjør det mulig for kommunale fagsystemer å slå opp kjøretøy og eierforhold uten å etablere egne separate tilkoblinger mot Statens vegvesens grensesnitt. Løsningen speiler sentrale oppslagstjenester fra kilden, men legger dem inn i Fiks sitt autentiserings- og integrasjonsmønster. Produktet er særlig relevant der kommuner trenger kjøretøyopplysninger som del av operative prosesser som parkering, gebyrhåndtering, feilparkering, brøyting og andre oppgaver knyttet til kjøretøy i kommunal forvaltning.

## Kapabiliteter
- **Datakilder: Grunndata** er direkte relevant fordi løsningen gjør autoritative kjøretøyopplysninger fra Statens vegvesen tilgjengelige for kommunal sektor gjennom et kontrollert tilgangslag.
- **Datautveksling og integrasjon: Bruke data fra andre** er kjernefunksjonen fordi kommunale fagsystemer bruker løsningen til å hente data fra en annen virksomhets register i egne operative prosesser.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals produkt- og utviklerdokumentasjon kontrollert 2026-03-26.

## Produktmål
Dokumenterte mål:
- Gi kommunale fagsystemer tilgang til Statens vegvesens kjøretøyregister via Fiks-plattformen.
- Speile utvalgte oppslags- og søketjenester fra kilden i et standardisert kommunalt integrasjonsmønster.
- Forenkle bruk av kjøretøydata i kommunale arbeidsprosesser.

Operative mål utledet fra kildene:
- Redusere behovet for egne punkt-til-punkt-integrasjoner mot Statens vegvesen for hver kommune eller leverandør.
- Gjøre det enklere å bruke oppdaterte kjøretøy- og eieropplysninger i kommunale fagsystemer.
- Sikre at tilgang til data følger Fiks-plattformens autentiserings- og oppsettsmodell.

## Brukerbehov
- Kommuner trenger kjøretøyopplysninger i operative prosesser som parkering, gebyrer og håndtering av kjøretøy på kommunal grunn.
- Fagsystemleverandører trenger et tydelig og stabilt integrasjonsmønster for oppslag mot kjøretøydata.
- Lokale administratorer trenger en enkel måte å konfigurere integrasjon, tilgang og organisasjonsknytning i Fiks.
- Kommunal sektor trenger tilgang til oppdaterte opplysninger direkte fra kilden, ikke via manuelle mellomledd.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Tilgang til oppdaterte kjøretøyopplysninger i operative prosesser | Parkeringsforvaltning, gebyrer, kjøretøyrelaterte oppgaver i kommunen | Primær målgruppe |
| Fagsystemer og leverandører | API-tilgang og standardisert autentisering | Integrasjon i systemer for parkering, gebyr og annen kommunal saksbehandling | Teknisk brukergruppe |
| Fiks-administratorer | Oppsett av integrasjon, tilgang og organisasjonskobling | Konfigurasjon i Fiks forvaltning og deling av integrasjonsdata til leverandør | Lokal forvaltningsrolle |
| KS Digital | Forvalte produktet og integrasjonsmønsteret | Produktforvaltning, dokumentasjon og kundestøtte | Sentral tjenesteforvalter |

## Hovedfunksjoner
### Primære funksjoner
Fiks kjøretøyregister sin kjernefunksjon er å gjøre oppslag i Statens vegvesens kjøretøyregister tilgjengelig gjennom Fiks-plattformen. Produktet er derfor en spesialisert registertilgangstjeneste for maskin-til-maskin-bruk, ikke en generell kjøretøyportal eller en egen kommunal datakilde.

Løsningen speiler sentrale oppslags- og søkemuligheter fra kilden, blant annet oppslag på kjennemerke, kuid og understellsnummer, samt søk i kjøretøydata. Den gjør det også mulig å hente informasjon på et bestemt tidspunkt. Dette er viktig i kommunale arbeidsprosesser der tidspunktet for oppslaget har betydning, for eksempel når kommunen skal følge opp parkering eller annen hendelsesbasert saksbehandling.

Produktet har en tydelig teknisk avgrensning: det brukes gjennom integrasjon i fagsystemer. KS Digital oppgir at webportal ikke støttes i dag, og utviklerdokumentasjonen beskriver tjenesten som maskin-til-maskin-integrasjon. Samtidig er produktet ikke bare et rått videresendt API, fordi Fiks legger på eget autentiserings- og konfigurasjonsmønster med Maskinporten, Fiks-organisasjons-ID og integrasjonspassord.

En viktig del av funksjonen ligger derfor i standardiseringen av tilgangsløpet for kommunal sektor. Kommunen eller leverandøren forholder seg til Fiks-konfigurasjon, Fiks-autentisering og et kjent oppsettsmønster, mens de underliggende kjøretøydataene fortsatt kommer direkte fra Statens vegvesen. Produktet skaper dermed verdi som kommunalt tilgangslag og ikke som alternativ kilde til kjøretøyinformasjon.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| API-basert oppslag i Statens vegvesens kjøretøyregister via Fiks | Eierskap til kjøretøyregisteret eller dataene i kilden |
| Standardisert autentisering og integrasjonsmønster på Fiks-plattformen | Generell webportal for saksbehandlere |
| Oppslag på blant annet kjennemerke, kuid og understellsnummer | Lokal saksbehandling, vedtakslogikk eller gebyrbehandling |
| Bruk i kommunale fagsystemer for operative kjøretøyrelaterte behov | Full erstatning for Statens vegvesens faglige dokumentasjon og kildeansvar |

## Veikart over kommende funksjonalitet
**Fakta:** Utviklerdokumentasjonen opplyser at det på sikt vil bli vurdert å utvikle et administrativt grensesnitt mot Fiks kjøretøyregister for kommuneansatte. Jeg fant ikke et samlet offentlig veikart med tidsfestede milepæler utover dette i denne arbeidsøkten.

**Deduksjon:** Videreutviklingen vil trolig handle om forbedret administrativ støtte og løpende tilpasning til endringer i Statens vegvesens grensesnitt og kommunale behov.

## Forretningsverdi/Verdiforslag
### For kommuner og fylkeskommuner
- Gjør det enklere å bruke oppdaterte kjøretøyopplysninger i operative prosesser uten egne spesialintegrasjoner mot Statens vegvesen.
- Reduserer innføringsarbeidet for kommuner som allerede bruker Fiks-plattformen.

### For leverandører
- Gir et kjent kommunalt integrasjonsmønster med standard autentisering og oppsett.
- Forenkler utvikling av fagsystemstøtte for kjøretøyrelaterte arbeidsprosesser.

### For sektoren
- Bidrar til mer ensartet bruk av kjøretøydata i kommunal sektor.
- Styrker gjenbruk av felles infrastruktur i stedet for parallelle lokale oppkoblinger.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil bruk av eier- og kjøretøyopplysninger kan gi brudd på regelverk eller bruksvilkår. | Tydelige avtaler, lokal kontroll av behandlingsgrunnlag og avgrenset bruk til tjenstlig behov. |
| Teknisk | Endringer i underliggende Swagger-spesifikasjon eller hos Statens vegvesen kan påvirke integrasjonene raskt. | Versjonsoppfølging, testmiljø og koordinert dialog med leverandører og KS Digital. |
| Sikkerhet | Feil håndtering av token, integrasjonsdata eller oppslagsrettigheter kan gi uautorisert tilgang. | Maskinporten-basert autentisering, kontrollert konfigurasjon og sikker håndtering av integrasjonspassord. |
| Leverandør | Kommunen er avhengig av både KS Digital som tilgangslag og Statens vegvesen som datakilde. | Tydelig dokumentasjon, robust forvaltning og kjent ansvarsdeling mellom aktørene. |
| Brukeropplevelse | Verdien faller hvis fagsystemet ikke støtter tjenesten eller integrasjonen settes opp feil. | Kreve leverandørstøtte, bruke Fiks-konfigurasjon riktig og gi tydelige veiledere for oppsett. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-kjoretoyregister/
- https://developers.fiks.ks.no/tjenester/kjoretoyregister/
- https://ksdigital.no/tjenestene/fiks-register/
- https://ksdigital.no/avtaler-og-priser/fakturalinjer/

## Plattform
Fiks kjøretøyregister er en registertilgangstjeneste på KS Digitals Fiks-plattform og fungerer som et kommunalt tilgangslag mot Statens vegvesens kjøretøyregister.

**Fakta:**
- Tjenesten brukes i dag som maskin-til-maskin-integrasjon og har ikke ordinær webportal i produksjon.
- Autentisering skjer på Fiks-plattformen med access token fra Maskinporten og egne Fiks-integrasjonsopplysninger.
- Det finnes egne URL-er for test- og produksjonsmiljø på Fiks-plattformen.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full intern driftsarkitektur, intern prioritering av videreutvikling og detaljer om overvåkning og SLA utover det som følger av Fiks-plattformen generelt.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet kan brukes av mange kommuner med likeartede behov for kjøretøyopplysninger i operative arbeidsprosesser.
- Gjenbruksverdien ligger i felles autentiserings- og integrasjonsmønster, ikke i at KS Digital eier de underliggende dataene.
- Løsningen er særlig relevant når flere kommuner eller leverandører trenger samme type oppslag uten å bygge egne tilkoblinger mot kilden.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** - løsningen gjør autoritative kjøretøyopplysninger tilgjengelige for gjenbruk i kommunale systemer gjennom et felles tilgangslag.
- **P7: Sørg for tillit til oppgaveløsningen** - produktet bygger på standard autentisering fra Maskinporten og kontrollert oppsett i Fiks-plattformen før data kan brukes.

## Finansiering
**Fakta:** KS Digitals fakturalinjer viser at Fiks kjøretøyregister har fastpris, innbyggerpris og Digifin prosjektavgift.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full prisdifferensiering mellom ulike kundegrupper og full intern finansieringsmodell for sentral forvaltning og drift.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktside, veiledning og teknisk dokumentasjon ligger hos KS Digital. |
| Driftsansvar | KS Digital | Tjenesten leveres på Fiks-plattformen, men full intern driftsmodell er ikke offentlig detaljert dokumentert. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Fakturalinjer viser prismodell, men ikke full budsjettstyring. |
| Styringsmodell | KS Digital som tjenesteforvalter i samspill med Statens vegvesens kildetjenester | Fremgår av produktside og teknisk dokumentasjon. |

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
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/produkter/produktbeskrivelser/28-FIKS-Register-produkt-canvas-v1-codex.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-kjoretoyregister/ (hentet 2026-03-26)
- Nettkilde: https://developers.fiks.ks.no/tjenester/kjoretoyregister/ (hentet 2026-03-26)
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/ (hentet 2026-03-26)
- Nettkilde: https://ksdigital.no/avtaler-og-priser/fakturalinjer/ (hentet 2026-03-26)
