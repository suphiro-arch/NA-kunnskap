# Entur sanntids- og rutedata

## Navn
Entur sanntids- og rutedata (åpne data og åpne tjenester fra Entur AS)

## Ressurs ID
ENTUR-001

## Status/Livsfase
**Produksjon** - åpne datastrømmer og API-er i drift for kollektivtrafikken i hele Norge.

**Fakta:** Entur publiserer sanntidsdata i SIRI 2.0, SIRI Lite og GTFS-RT, rutedata i NeTEx og GTFS, og tilbyr reiseplanleggeren Journey Planner v3 som åpen tjeneste på developer.entur.no. Entur oppgir at det nasjonale registeret samler data fra 60 kollektivoperatører, med om lag 21 000 daglige avganger på 3 000 ruter.

## Modenhet
**Høy teknisk modenhet, med ujevn dekning per dataleverandør:**
- Dataene leveres i etablerte europeiske og internasjonale formater: SIRI og NeTEx for sanntid og rutedata, GTFS og GTFS-RT som forenklede varianter.
- Sanntidsdata kan hentes både ved abonnement (publish/subscribe for SIRI) og ved oppslag (SIRI Lite og GTFS-RT), med dokumenterte begrensninger på kallfrekvens.
- Rutedata valideres og eksporteres på nytt hver natt.
- Bruksvilkårene er publisert, med NLOD som lisens for Enturs åpne data og krav om at hver klient identifiserer seg med headeren `ET-Client-Name`.
- Dekningen varierer: oversikten over dataleverandører viser at noen leverer bare ET, VM eller SX, og noen bare SIRI eller GTFS-RT.

**Deduksjon:** Ressursen er moden nok til å bygge produksjonstjenester på. Det svakeste leddet er at kvaliteten på sanntidsdataene avhenger av hver enkelt operatørs leveranse, og at Entur ikke tilbyr noen garantert oppetid for de åpne tjenestene.

## Kort beskrivelse
Entur AS er et statlig eid selskap under Samferdselsdepartementet som drifter det nasjonale registeret for kollektivtrafikk i Norge. Ressursen her er de åpne data og åpne tjenestene Entur gjør tilgjengelige fra dette registeret: sanntidsinformasjon om avganger, forsinkelser, innstillinger, kjøretøyposisjoner og avviksmeldinger for buss, tog, trikk, T-bane og ferje, rutedata og stoppestedsdata, og en reiseplanlegger som beregner reiser på tvers av operatører. Dataene er samlet fra fylkeskommunale kollektivselskaper, jernbaneselskaper og kommersielle operatører, og gjort tilgjengelige i ett sett med standardiserte grensesnitt. Salgs- og billettsystemene Entur også leverer, inngår ikke i denne ressursen.

## Kapabiliteter
- **Datakilder: Sanntidsdata** Entur samler sanntidsdata fra kollektivoperatørene i hele landet og distribuerer dem videre som kontinuerlige strømmer i SIRI ET, VM og SX og i GTFS-RT, oppdatert hvert 15. sekund i GTFS-RT.
- **Datakilder: Åpne data** Entur publiserer rute-, stoppesteds- og sanntidsdata som åpne data under NLOD, gratis og uten avtale, i maskinlesbare standardformater med offentlig dokumentasjon.
- **Datautveksling og integrasjon: Dele data med andre** Entur gjør data fra 60 operatører tilgjengelige for andre gjennom dokumenterte grensesnitt for abonnement, oppslag og nedlasting, slik at mottakeren ikke må hente data fra hver operatør.

## Produktmål
**Dokumenterte mål:**
- Entur oppgir at selskapet vil dele dataene sine med alle som ønsker det, gratis (developer.entur.no).
- Samferdselsdepartementet beskriver at Entur tilbyr tjenester som gjør det mulig å planlegge, sammenligne og bestille sømløse reiser på tvers av alle kollektivselskaper i Norge (regjeringen.no).

**Deduksjon:** Det operative målet for de åpne dataene er at reiseinformasjon på tvers av operatører og fylker skal kunne bygges på ett felles og standardisert datagrunnlag, i stedet for at hver tjenesteleverandør henter data fra hvert kollektivselskap.

## Brukerbehov
- Utviklere av reiseapper og informasjonstjenester trenger oppdaterte avganger, forsinkelser og avvik for hele landet i ett grensesnitt.
- Kollektivselskaper og operatører trenger at egne rute- og sanntidsdata blir tilgjengelige for reisende også i tjenester de ikke drifter selv.
- Virksomheter som analyserer eller planlegger transport trenger rutedata og stoppestedsdata i et standardisert format.
- Reisende trenger reiseinformasjon som henger sammen på tvers av operatører og fylkesgrenser.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Tredjepartsutviklere og reiseapper | Sanntidsavganger, avvik og reiseforslag | Reiseplanleggere, avgangstavler og sanntidsvisninger | Bruker åpne tjenester uten avtale, men må oppgi `ET-Client-Name` |
| Kollektivselskaper og operatører | Distribusjon av egne rute- og sanntidsdata | Leverer data inn til Entur og får dem videreformidlet | Oppført som dataleverandører med egne kodeområder |
| Offentlige virksomheter og analysemiljøer | Rute- og stoppestedsdata i standardformat | Transportanalyse, planlegging | **Ikke offentlig dokumentert:** omfanget av slik bruk |
| Reisende | Sammenhengende reiseinformasjon | Møter dataene indirekte gjennom apper og skjermer | Ikke direkte brukere av API-ene |
| Entur AS | Drift, validering og forvaltning av data og grensesnitt | Nasjonalt register for kollektivtrafikk | Forvalter ressursen |

## Hovedfunksjoner
**Sanntidsdata i SIRI.** Entur distribuerer sanntidsdata i tre SIRI-profiler: Estimated Timetable (ET) med forventede og faktiske avgangstider, innstillinger og endrede stoppmønstre, Vehicle Monitoring (VM) med kjøretøyposisjoner og avvik fra ruteplanen, og Situation Exchange (SX) med tekstmeldinger knyttet til avganger, linjer eller stoppesteder. Mottakeren kan abonnere (publish/subscribe), der Entur først sender et fullt datasett og deretter fortløpende endringer til mottakerens endepunkt, eller hente data ved oppslag.

**Forenklede sanntidsformater.** SIRI Lite gir de samme tre datatypene over enkle HTTP GET-kall, begrenset til fire kall i minuttet. GTFS-RT gir tilsvarende innhold som Trip Updates, Vehicle Positions og Service Alerts, oppdatert hvert 15. sekund. Begge kan filtreres per dataleverandør. For hyppigere oppdatering anbefaler Entur abonnement i SIRI.

**Rute- og stoppestedsdata.** Rutedata eksporteres i NeTEx, som er det offisielle norske formatet og det mest komplette, og i GTFS som et forenklet utvalg. Stoppestedsdata oppdateres hver natt, rutedata når en dataeier laster opp nye data, og alle datasett valideres og eksporteres på nytt hver natt. Stoppestedsregisteret kan også ses i en egen nettflate uten innlogging.

**Reiseplanlegging og andre åpne tjenester.** Journey Planner v3 er et GraphQL-API for reisesøk og avgangstavler på tvers av alle operatører. I tillegg tilbyr Entur åpne tjenester for geokoding av adresser og stoppesteder, kjøretøyposisjoner og sanntidsdata for delte sykler og sparkesykler.

### Typiske brukssituasjoner (generisk)
- En tjeneste skal vise avganger og forsinkelser for kollektivtrafikk i hele eller deler av landet.
- En virksomhet trenger reiseforslag på tvers av operatører uten å bygge egen ruteberegning.
- En analyse trenger rute- og stoppestedsdata for hele landet i ett format.
- En tjeneste skal varsle om innstillinger og avvik i kollektivtrafikken.

### Når Entur sanntids- og rutedata normalt ikke er førstevalg
- Når behovet er sanntidsinformasjon om vegtrafikk, trafikkhendelser eller føreforhold, som Statens vegvesen publiserer gjennom DATEX II.
- Når behovet er billettsalg eller betalingsløsninger; de tjenestene er partnertjenester med egen avtale, ikke åpne data.
- Når behovet er historiske sanntidsdata over tid; **Ikke offentlig dokumentert:** de åpne tjenestene beskriver ikke et historisk arkiv.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Sanntidsdata i SIRI ET, VM og SX, SIRI Lite og GTFS-RT | Salgs- og billettsystemer (partnertjenester) |
| Rutedata i NeTEx og GTFS | Selve ruteplanleggingen hos fylkeskommunene og operatørene |
| Stoppestedsdata og stoppestedsregister | Kvalitetssikring av dataene i operatørenes egne systemer |
| Journey Planner v3, geokoder, kjøretøyposisjoner og mobilitetsdata | Garantert oppetid for åpne tjenester |

## Veikart over kommende funksjonalitet
**Fakta:** Entur oppgir at publish/subscribe også skal komme for GTFS-RT. Utviklerportalen er flyttet fra developer.entur.org til developer.entur.no, og den gamle portalen skal fases ut når innholdet er flyttet.

**Ikke offentlig dokumentert i denne arbeidsøkten:** et samlet, tidfestet veikart for de åpne dataene.

## Forretningsverdi/Verdiforslag
### For tjenesteutviklere og næringsliv
- Ett sett grensesnitt for hele landet i stedet for egne integrasjoner mot hvert kollektivselskap.
- Fri bruk, også kommersielt, under NLOD.

### For kollektivselskaper og fylkeskommuner
- Egne rute- og sanntidsdata når flere kanaler enn deres egne apper og skjermer.

### For reisende
- **Deduksjon:** Mer sammenhengende reiseinformasjon når tjenester fra ulike leverandører bygger på samme datagrunnlag.

### For offentlig sektor og analyse
- Rute- og stoppestedsdata i et standardformat som kan brukes i transportanalyse og planlegging.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Datakvalitet | Sanntidsdataene er avhengige av at hver operatør leverer korrekte og fullstendige data til Entur | Entur oppgir at ikke alle aktører ennå leverer NeTEx etter den norske profilen; dekningen per datatype varierer per leverandør |
| Tilgjengelighet | Mange tredjepartstjenester avhenger av at de åpne tjenestene er stabile | Vilkårene gir ingen garanti for oppetid, og Entur kan stanse tilgang ved misbruk eller stor belastning |
| Juridisk | Bruk uten riktig kildeangivelse bryter NLOD-vilkårene | Vilkårene oppgir standardtekst for kildeangivelse |
| Teknisk | Oppslag med høy frekvens kan bli strupet | SIRI Lite er begrenset til fire kall i minuttet; klienter uten `ET-Client-Name` får lavere grenser |
| Endring | Utviklerportalen er i overgang fra developer.entur.org til developer.entur.no | Lenker og dokumentasjon kan flytte; endringsvarsler publiseres fortsatt på den gamle portalen |

## Kanaler
- Maskinelle grensesnitt: SIRI 2.0 (abonnement og oppslag), SIRI Lite og GTFS-RT for sanntid, NeTEx- og GTFS-filer for rutedata, GraphQL for Journey Planner v3 og kjøretøyposisjoner.
- Åpne tjenester krever ikke innlogging. Partnertjenester krever OAuth2-klientlegitimasjon. Alle kall skal ha headeren `ET-Client-Name`, som identifiserer applikasjonen.
- Utviklerdokumentasjon på developer.entur.no. Stoppestedsregisteret kan ses i nettleser uten innlogging.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** driftsmodell, skyleverandør og vertsplassering for Enturs tjenester. Kjent er at tjenestene eksponeres over internett under Enturs domener.

## Gjenbruk
Ressursen er laget for gjenbruk: dataene er åpne under NLOD, tilgjengelige uten avtale og levert i standardformater (SIRI, NeTEx, GTFS, GTFS-RT) som støttes av internasjonale verktøy. Gjenbruk forutsetter kildeangivelse og at klienten identifiserer seg.

### Vanlige kombinasjoner med andre produkter
- **Deduksjon:** DATEX II trafikkinformasjon fra Statens vegvesen, når en tjeneste skal kombinere kollektivinformasjon med trafikkhendelser og føreforhold på vegnettet.
- **Deduksjon:** Kartdata fra Geonorge, når rute- og stoppestedsdata skal vises eller analyseres i kart.

**Kildekode:** Ikke offentlig dokumentert. Entur publiserer flere komponenter på GitHub, blant annet `anshar`, en hub for publisering og abonnement på SIRI-data, men det er ikke dokumentert hvilke komponenter som utgjør tjenestene som er i drift.

**Lisens:** Ikke offentlig dokumentert for tjenesten som helhet. Repositoriet `entur/anshar` oppgir `EUPL-1.2`. Dataene er lisensiert under NLOD, som gjelder data og ikke kildekode.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Entur deler rute- og sanntidsdata fra hele landet som åpne data under NLOD, i standardformater.
- **P5: Del og gjenbruk løsninger**
  Støttes delvis. Journey Planner v3 og geokoderen kan brukes av andre i stedet for egne løsninger, men tjenestene gis uten garantert oppetid.
- **P6: Lag digitale løsninger som støtter samhandling**
  Dataene samles fra mange operatører og distribueres gjennom felles grensesnitt basert på europeiske standarder.

**Spenning og begrensning:** Ressursen er ikke sterkere enn dataene operatørene leverer, og kvaliteten varierer per leverandør. At Entur forbeholder seg retten til å stanse tilgang og ikke garanterer oppetid, gjør det krevende å bygge kritiske tjenester alene på de åpne grensesnittene.

## Finansiering
**Fakta:** De åpne dataene og tjenestene er gratis for brukerne.

**Ikke offentlig dokumentert i denne arbeidsøkten:** hvordan utvikling og drift av de åpne dataene finansieres, og om det skjer gjennom statlige tilskudd, inntekter fra salgstjenester eller betaling fra dataleverandører.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Entur AS | developer.entur.no |
| Driftsansvar | Entur AS | Vilkårene for bruk på developer.entur.no |
| Budsjettansvar | Ikke offentlig dokumentert i denne arbeidsøkten | - |
| Eierskap og styringsmodell | Entur AS er et aksjeselskap eid av Samferdselsdepartementet | regjeringen.no, side om Entur AS |
| Dataansvar | Fylkeskommuner, jernbaneselskaper og kommersielle operatører leverer data; Entur validerer og distribuerer | developer.entur.no, rute- og stoppestedsdata |

## Lenke til dokumentasjon
- Sanntidsdata: https://developer.entur.no/open-data/realtime
- Åpne data: https://developer.entur.no/open-data
- Åpne tjenester: https://developer.entur.no/docs/open-services
- Autentisering og `ET-Client-Name`: https://developer.entur.no/docs/authentication
- Vilkår for bruk: https://developer.entur.no/terms-of-service
- Rute- og stoppestedsdata (gammel portal): https://developer.entur.org/stops-and-timetable-data

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/operative-ressurs-canvas.system.md`
- Lokal fil: `config/templates/operative-ressurs-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Nettkilde: https://developer.entur.no/open-data/realtime (kontrollert 2026-10-23)
- Nettkilde: https://developer.entur.no/open-data (kontrollert 2026-10-23)
- Nettkilde: https://developer.entur.no/docs/open-services (kontrollert 2026-10-23)
- Nettkilde: https://developer.entur.no/docs/authentication (kontrollert 2026-10-23)
- Nettkilde: https://developer.entur.no/terms-of-service (kontrollert 2026-10-23)
- Nettkilde: https://developer.entur.org/stops-and-timetable-data (kontrollert 2026-10-23)
- Nettkilde: https://www.regjeringen.no/no/dep/sd/org/selskaper/entur-as/id2550682 (kontrollert 2026-10-23)
- Nettkilde: https://github.com/entur/anshar (kontrollert 2026-10-23)

## Endringer fra forrige versjon
Første publiserte versjon. Det finnes ingen tidligere versjon av ressursen i repoet.
