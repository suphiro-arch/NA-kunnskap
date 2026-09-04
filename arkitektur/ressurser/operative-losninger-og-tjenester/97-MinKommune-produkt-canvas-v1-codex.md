# Produkt-canvas: KS Min kommune

## Navn
KS Min kommune

## Ressurs ID
KS-016

## Status/Livsfase
**Produksjon** - etablert innbyggerportal i KS Digital med aktiv forvaltning og videreutvikling.

**Fakta:** KS Digital beskriver KS Min kommune som en tjeneste som samler post, skjema, faktura, eiendomsinformasjon og byggesaker på ett sted for innbyggere og virksomheter. Fiks-dokumentasjonen beskriver min.kommune.no som portal for innbyggerrettede tjenester på Fiks-plattformen, med ID-porten-autentisering.

## Modenhet
**Høy modenhet** - etablert portal med konkrete deltjenester og operativt ta-i-bruk-løp:
- Tjenesten har publisert teknisk dokumentasjon og tydelige konfigurasjonsløp i Fiks forvaltning.
- Portalmodellen bygger på eksisterende operative felleskomponenter, blant annet ID-porten, KRR, SvarUt og matrikkeldata.
- KS Digital beskriver tjenesten som i stadig utvikling, med aktiv produktforvaltning.

**Deduksjon:** Modenheten er høy for kjernefunksjoner knyttet til innsyn og kommunikasjon med kommunen. Omfang og brukeropplevelse vil samtidig variere etter hvilke delfunksjoner den enkelte kommune aktiverer.

## Kort beskrivelse
KS Min kommune, tidligere omtalt som MinKommune, er en innbyggerportal som samler kommunale digitale tjenester i en felles brukerflate på min.kommune.no. Tjenesten gir innbyggere ett sted å finne og følge post, faktura, eiendommer, byggesaker, skjema og andre kommunale oppgaver, med autentisering via ID-porten og kobling til flere datakilder og kommunale fagsystem.

I NA-sammenheng er MinKommune relevant fordi den representerer et kommunalt innbyggergrensesnitt bygget på gjenbruk av nasjonale og kommunale felleskomponenter. Tjenesten kan sees som en kommunal portalmotpart til statlige innbyggertjenester der målet er sammenhengende brukerreiser på tvers av virksomheter og forvaltningsnivå.

## Kapabiliteter
- **Sluttbrukertjenester: Sammenhengende tjenester**
  MinKommune samler flere kommunale tjenester i en felles innbyggerreise fremfor separate innlogginger og grensesnitt.
- **Sluttbrukertjenester: Tjenestekjeder**
  Portalen kobler sammen post, faktura, eiendom, byggesak og skjema i kjeder som understøtter oppgave- og saksoppfølging over tid.

## Produktmål
Dokumenterte mål:
- Gi innbygger et lett navigerbart grensesnitt der sentral kommunal informasjon er samlet på ett sted.
- Forenkle kommunens administrasjon gjennom en samlet plattform for innsyn og samhandling.
- Legge til rette for trygg håndtering av offentlig informasjon gjennom avtaler og konfigurasjon.

Operative mål utledet fra kildene:
- Redusere fragmentering i kommunale innbyggertjenester.
- Styrke digital dialog mellom kommune, innbygger og næringsliv.
- Utnytte eksisterende felleskomponenter bedre i kommunal sektor.

## Brukerbehov
- Innbyggere trenger enkel tilgang til kommunal post, oppgaver og informasjon uten å navigere i mange ulike systemer.
- Kommuner trenger en portal som reduserer administrativ oppfølging og forenkler tjenestetilgang.
- Kommunale fagmiljøer trenger en kanal som kan kobles til fagsystem via standardiserte integrasjoner.
- Næringsliv og organisasjoner trenger oversikt over relevante kommunale saker og informasjon de er part i.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Innbyggere | Samlet oversikt over kommunal informasjon og oppgaver | Post, faktura, eiendom, byggesak, skjema | Primær sluttbruker |
| Kommunale tjenesteeiere | Felles innbyggerflate for flere tjenester | Publisering av data og oppgaver fra fagsystem | Primær virksomhetsbruker |
| Kommunal forvaltning/IKT | Konfigurasjon og drift av tjenesteflate | Aktivering av funksjoner og integrasjoner | Krever lokal forvaltning |
| Næringsliv og organisasjoner | Tilgang til relevante kommunale opplysninger | Innsyn i saker, faktura, post og oppgaver | Sekundær brukergruppe |
| KS Digital | Plattformforvaltning og videreutvikling | Produktansvar, dokumentasjon og støtte | Sentral forvalter |

## Hovedfunksjoner
MinKommune sin kjernefunksjon er å samle kommunale innbyggerrettede tjenester i en felles portal med sikker innlogging. Tjenesten gjør at innbyggeren kan starte i ett grensesnitt og finne relevant informasjon og handlinger uten å gå via mange separate kommunale løsninger.

Portalen tilbyr flere funksjonsområder som post fra kommunen, faktura, eiendomsoversikt, byggesaker, skjema og oppgaver. Disse funksjonene bygger på integrasjoner mot kommunale fagsystemer og nasjonale fellesressurser, blant annet matrikkeldata og kontaktinformasjon.

MinKommune har en tydelig konfigurasjonsmodell der kommunene aktiverer og tilpasser funksjoner i Fiks forvaltning. Det betyr at tjenesten er en felles plattform med lokal tilpasning, ikke en helt lik tjeneste i alle kommuner.

Tjenesten har også en viktig nav- og orienteringsfunksjon mot nasjonale tjenester og skatt/avgift, som hjelper innbyggere med å navigere mellom kommunale og statlige tjenester fra ett kommunalt utgangspunkt.

### Typiske brukssituasjoner
- når innbygger vil se post fra kommunen, fakturaer og status på egne kommunale saker på ett sted
- når innbygger vil finne eiendomsinformasjon og tilhørende byggesaker
- når kommunen vil tilby ett felles innbyggergrensesnitt i stedet for mange separate fagsystemflater
- når kommunen vil koble lokale tjenester med nasjonale innganger i en mer sammenhengende brukerreise

### Når MinKommune normalt ikke er førstevalg
- når behovet er rene maskin-til-maskin-integrasjoner uten sluttbrukerflate
- når behovet er fagsystemintern saksbehandling uten innbyggerinteraksjon
- når virksomheten trenger en ren statlig portalflate fremfor kommunal inngang
- når kommunen ikke har grunnleggende integrasjoner og konfigurasjon på plass

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Portal for innbyggerrettede kommunale tjenester | Full kommunal saksbehandling i fagsystemene |
| Samlet innsyn i post, faktura, eiendom og utvalgte saker | Erstatning for alle kommunale fagapplikasjoner |
| Integrasjoner mot Fiks-tjenester og utvalgte nasjonale kilder | Generell nasjonal portal for hele offentlig sektor |
| Konfigurerbar tjenesteflate per kommune | Standardisert, identisk funksjonsomfang i alle kommuner |

## Veikart over kommende funksjonalitet
KS Digital beskriver tjenesten som i kontinuerlig utvikling. Ingen samlet offentlig veikartsplan med tidfestede leveranser er hentet i denne arbeidsøkten.

## Forretningsverdi/Verdiforslag
- For innbyggere: enklere tilgang til kommunal informasjon og oppgaver i ett brukergrensesnitt.
- For kommuner: redusert fragmentering og mindre administrativ belastning gjennom en samlet portalflate.
- For offentlig sektor: bedre grunnlag for sammenhengende tjenester mellom kommunale og statlige løsninger.
- For leverandører og utviklingsmiljøer: tydeligere integrasjonspunkt for innbyggernære funksjoner.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Variasjon mellom kommuner | Ulik konfigurasjon kan gi ulik brukeropplevelse og forventningsbrudd | Tydelig produktbeskrivelse lokalt og aktiv forvaltningspraksis |
| Integrasjonskvalitet | Mangelfulle koblinger mot fagsystem kan redusere nytte | Standardiserte API-er og tydelig innføringsløp |
| Sikkerhet og personvern | Aggregasjon av flere datatyper i en portal krever sterk tilgangsstyring | ID-porten, avtaler, ROS/DPIA og sikkerhetsdokumentasjon |
| Avhengigheter | Tjenesten avhenger av flere underliggende løsninger | Robust drift, statusovervåkning og tydelige fallback-rutiner |

## Kanaler
- https://ksdigital.no/tjenestene/minkommune/
- https://min.kommune.no/
- https://developers.fiks.ks.no/tjenester/minkommune/

## Plattform
Webportal på Fiks-plattformen med ID-porten-autentisering og integrasjon mot kommunale fagsystem og utvalgte nasjonale kilder.

## Gjenbruk
MinKommune har høy gjenbruksverdi for kommuner som vil etablere en samlet innbyggerflate basert på fellesløsninger. Gjenbrukbarheten ligger i plattform- og integrasjonsmodellen, mens konkret funksjonsomfang styres lokalt.

**Vanlige kombinasjoner med andre produkter:**
- `ID-porten`
- `Fiks SvarUt` / `SvarInn`
- `Kontakt- og reservasjonsregisteret`
- `Matrikkelen`
- kommunale fagsystemløsninger via Fiks-integrasjoner

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger**
  MinKommune gjenbruker felleskomponenter og etablerte integrasjonsmønstre i stedet for kommunevis nyutvikling av portalgrunnlag.
- **P6: Lag digitale løsninger som støtter samhandling**
  Tjenesten kobler kommunale tjenester og relevante nasjonale innganger i en mer sammenhengende innbyggerreise.

Svakhet: Effekten avhenger av lokal implementering og hvilke deltjenester kommunen faktisk aktiverer.

## Finansiering
Tjenesten tas i bruk gjennom KS Digital sine avtale- og prismodeller for kommuner og fylkeskommuner.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produkt- og plattformforvaltning | KS Digital | ksdigital.no og developers.fiks |
| Lokal tjenestekonfigurasjon og bruk | Kommuner og fylkeskommuner | ta-i-bruk-løp i Fiks forvaltning |
| Underliggende datakilder/integrasjoner | Flere (kommunale og nasjonale) | tjenestedokumentasjon |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/minkommune/
- https://developers.fiks.ks.no/tjenester/minkommune/
- https://min.kommune.no/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://ksdigital.no/tjenestene/minkommune/ (kontrollert 2026-05-03)
- Nettkilde: https://developers.fiks.ks.no/tjenester/minkommune/ (kontrollert 2026-05-03)
- Nettkilde: https://min.kommune.no/ (kontrollert 2026-05-03)
