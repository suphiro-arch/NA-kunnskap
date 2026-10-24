# MET Frost API

## Navn
Frost og MET Weather API (api.met.no) – Meteorologisk institutts åpne API-er for vær- og klimadata

## Ressurs ID
MET-001

## Status/Livsfase
**Produksjon** – begge API-ene er i ordinær, åpen drift.

**Fakta:** Frost ble lansert i 2018 og er fortsatt i API-versjon v0. Meteorologisk institutt (MET) oppgir at de vil unngå endringer som bryter bakoverkompatibiliteten (frost.met.no). MET Weather API på api.met.no tilbyr i dag et tjuetalls produkter i versjonert form, blant dem Locationforecast 2.0, Nowcast 2.0 og MetAlerts 2.0, og Frost er oppført som ett av produktene (api.met.no).

**Fakta:** Ingen av tjenestene har tjenestenivåavtale. Vilkårene for begge sier at det ikke gis leveransegaranti (api.met.no, Terms of Service; frost.met.no, Terms of use).

## Modenhet
**Høy teknisk og organisatorisk modenhet, men uten forpliktende leveransenivå.**

- Tjenestene har publiserte vilkår for bruk, med krav til identifikasjon, mellomlagring og trafikkmønster (api.met.no, Terms of Service; frost.met.no, Terms of use).
- Produktene i api.met.no er versjonert. Gamle versjoner markeres som utgående med HTTP-status 203 før de avvikles, vanligvis etter om lag en måned (api.met.no, Terms of Service).
- Lisensvilkårene er avklart og publisert: NLOD 2.0 og CC BY 4.0 (met.no, Licensing and Crediting).
- Programvaren for værikonene er publisert som åpen kildekode under MIT-lisens (api.met.no, License).
- Frost står fortsatt i API-versjon v0 åtte år etter lansering (frost.met.no).

**Deduksjon:** Det svakeste leddet er fraværet av leveransegaranti. Tjenestene er stabile og mye brukt, men den som bygger kritiske prosesser på dem, har ingen avtale å vise til. MET henviser selv til ECOMET-katalogen for garanterte eller tilpassede leveranser (api.met.no, Terms of Service).

## Kort beskrivelse
Meteorologisk institutt er statens etat for værvarsling, klimaovervåking og meteorologisk forskning, underlagt Klima- og miljødepartementet. MET gjør dataene sine fritt tilgjengelige gjennom to maskinelle API-er.

**Frost** er API-et mot METs arkiv over historiske vær- og klimadata: kvalitetskontrollerte målinger fra stasjonsnettet, metadata om stasjonene, klimanormaler, nedbørsstatistikk og lynregistreringer.

**MET Weather API** (api.met.no) er API-et for prognoser, farevarsler og bildeprodukter: punktvarsler for hele jorda, korttidsvarsel for nedbør i Norden basert på radar, farevarsler, radar- og satellittbilder, havvarsler, tidevann og produkter for luftfart og forsvar.

Begge er åpne for alle. Dataene er lisensiert under NLOD 2.0 og CC BY 4.0, og MET Norway skal krediteres som kilde. Unntak fra fri bruk gjelder tilpassede leveranser og data produsert av partnere.

## Kapabiliteter
Tjenestene leverer METs egne observasjoner, prognoser og varsler. Ingen annen ressurs leverer det nasjonale, autoritative vær- og klimagrunnlaget, så evnene ville blitt borte hvis tjenestene forsvant. Sanntidsdata er knyttet til api.met.no, ikke til Frost, som er et arkiv. Kanalen er spørrebasert med mellomlagring, ikke en strømmetjeneste.

- **Datakilder: Åpne data** MET publiserer egne observasjoner, prognoser og varsler maskinlesbart under NLOD 2.0 og CC BY 4.0, slik at alle kan bruke og dele dem mot kreditering.
- **Datakilder: Sanntidsdata** api.met.no distribuerer kontinuerlig oppdaterte data fra METs radarnett, med korttidsvarsel for nedbør hvert femte minutt, radarbilder hvert femte minutt og løpende farevarsler.
- **Datautveksling og integrasjon: Dele data med andre** MET tilgjengeliggjør egne data gjennom dokumenterte og versjonerte REST-API-er med publiserte vilkår, slik at andre kan bygge dem inn i egne tjenester.

## Produktmål
**Fakta:** MET oppgir at hovedmålet for all virksomheten er å bidra til å beskytte liv og verdier, og at instituttet har en fri og åpen datapolitikk der hvem som helst kan bruke materialet til samfunnets beste (met.no, About MET Norway).

**Fakta:** Frost skal gi fri tilgang til METs arkiv over historiske vær- og klimadata, og er laget for utviklere som bygger skript og applikasjoner mot arkivet (frost.met.no).

**Deduksjon:** Det operative målet for API-ene er å la mange brukere hente data uten individuell oppfølging fra MET. Det følger av at vilkårene legger vekt på mellomlagring, identifikasjon og fordeling av trafikk, og av at tilpassede leveranser er skilt ut som egen, betalt ordning.

## Brukerbehov
Virksomheter som planlegger, varsler eller dimensjonerer etter vær, trenger både prognoser og historiske måleserier fra en autoritativ kilde. Uten åpne API-er måtte hver virksomhet inngått egne leveranseavtaler eller etablert egne målinger, og ulike tjenester ville bygget på ulike tallgrunnlag.

Behovene er todelte. Det ene er oppdaterte prognoser og varsler for et sted eller område, ofte for direkte visning til sluttbrukere. Det andre er kvalitetskontrollerte tidsserier for analyse, dimensjonering og forskning, der historikk og metadata om målestedet er viktigere enn aktualitet.

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter med værfølsomme oppgaver | Prognoser, farevarsler og historiske måleserier | Beredskap, samferdsel, landbruk, planlegging | MetAlerts gir METs farevarsler maskinelt |
| Utviklere av apper og nettjenester | Punktvarsler og bildeprodukter for visning | Værvisning i egne tjenester | Krever identifiserende User-Agent og mellomlagring |
| Forskere og analysemiljøer | Kvalitetskontrollerte tidsserier, klimanormaler, stasjonsmetadata | Klimaanalyse, evaluering, modellvalidering | Frost er primærkanalen |
| Kommersielle aktører | Værdata som del av egne produkter | Energi, forsikring, logistikk, media | Fri bruk mot kreditering; tilpassede leveranser er betalt |
| Luftfart og forsvar | Spesialiserte værprodukter | Flyværtjeneste, militær planlegging | Egne produkter i api.met.no |
| Yr | Data til Yrs værvarsler | Værtjeneste for publikum | Yr er et samarbeid mellom MET og NRK, der MET leverer dataene |

## Hovedfunksjoner
Den første hovedfunksjonen er **tilgang til observasjonsarkivet gjennom Frost**. Brukeren finner målestasjoner for et område, ser hvilke værelementer som finnes for en stasjon og tidsperiode, og henter observasjoner med kvalitetskoder. Frost gir i tillegg klimanormaler, nedbørsstatistikk for intensitet og varighet, lynregistreringer, ekstremverdier per fylke og kodetabeller for elementene. Dataene leveres som JSON, unntatt lyndata, som leveres i eget format.

Den andre er **prognoser og varsler gjennom api.met.no**. Locationforecast gir punktvarsel for hele jorda. Nowcast gir to timers varsel for Norge, Sverige, Finland og Danmark, oppdateres hvert femte minutt og er avhengig av radardekning. MetAlerts leverer METs farevarsler. Tekstvarsler, langtidsvarsler, luftkvalitetsvarsler, havvarsler og tidevann er egne produkter.

Den tredje er **bildeprodukter**. Radar gir sammensatte radarbilder for Norden og norske regioner, som enkeltbilder eller animasjon av de siste tre timene. Satellittprodukter gir bilder fra geostasjonære og polare satellitter.

Den fjerde er **styrt åpen tilgang**. api.met.no krever ingen registrering, men hver forespørsel skal identifisere applikasjonen med navn og kontaktinformasjon. Frost krever en klient-ID knyttet til en e-postadresse. Begge tjenestene forventer at klienten mellomlagrer svar og respekterer utløpstider, og kan strupe eller blokkere klienter som bryter vilkårene. Over 20 forespørsler per sekund mot api.met.no krever særskilt avtale.

### Typiske brukssituasjoner (generisk)
- vise punktvarsel og farevarsler for et sted i en offentlig eller kommersiell tjeneste
- hente kvalitetskontrollerte tidsserier for temperatur, nedbør og vind til analyse eller dimensjonering
- bruke klimanormaler og nedbørsstatistikk som grunnlag for planlegging av infrastruktur
- vise radarbilder og korttidsvarsel for nedbør i beredskaps- og driftssituasjoner

### Når MET Frost API normalt ikke er førstevalg
Frost er ikke førstevalg for oppdaterte varsler eller radardata. Frost er et arkiv over historiske, kvalitetskontrollerte data; prognoser, korttidsvarsler og radar hentes fra api.met.no.

Ingen av API-ene er førstevalg når leveransen må være garantert eller tilpasset. Tjenestene har ingen tjenestenivåavtale, og MET henviser slike behov til tilpassede, betalte leveranser.

For værdata fra målestasjoner langs vegnettet er `SVV-003` DATEX II trafikkinformasjon fra Statens vegvesen mer relevant, og for kartdata og geografiske grunnlagsdata er `KART-002` Geonorge rett inngang.

### Scope og avgrensning
Inngår:
- Frost: METs arkiv over observasjoner, stasjonsmetadata, klimanormaler, nedbørsstatistikk og lyndata
- api.met.no: prognoser, korttidsvarsel, farevarsler, radar- og satellittbilder, hav- og tidevannsdata og spesialprodukter
- vilkår for bruk, lisens og krediteringskrav

Inngår ikke:
- Yr som publikumstjeneste, som drives i samarbeid mellom MET og NRK
- tilpassede eller garanterte leveranser, som er egne betalte avtaler
- data produsert av partnere, som er unntatt fra den frie lisensen
- METs datasettarkiv (THREDDS), som er oppført i api.met.no som eget produkt, men ikke er beskrevet her

## Veikart over kommende funksjonalitet
**Fakta:** Endringer i api.met.no varsles på e-postlista api-users og i RSS-strømmen for endringer. MET oppgir e-postlista som eneste kanal for å varsle planlagte endringer utenom API-et selv (api.met.no). Frost har egen endringslogg (frost.met.no).

**Ikke offentlig dokumentert:** En samlet plan for videreutvikling av Frost eller api.met.no, eller plan for når Frost skal ut av versjon v0.

## Forretningsverdi/Verdiforslag
For offentlige virksomheter ligger verdien i at alle bygger på samme autoritative vær- og klimagrunnlag uten egne avtaler med MET. Beredskap, samferdsel og planlegging kan bruke de samme farevarslene og måleseriene.

For næringslivet ligger verdien i at dataene kan brukes kommersielt mot kreditering. Det gjør vær- og klimadata til et råstoff for tjenester innen blant annet energi, forsikring og media.

For forskning ligger verdien i lange, kvalitetskontrollerte tidsserier med metadata om målested og kvalitet, hentet maskinelt og reproduserbart.

For innbyggere ligger verdien i at værvarsler i mange ulike tjenester, også Yr, bygger på samme offentlige kilde.

## Utfordringer og risiko

| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Leveransesikkerhet | Ingen tjenestenivåavtale eller leveransegaranti | MET henviser til ECOMET for garanterte eller tilpassede leveranser |
| Teknisk | Klienter som ikke mellomlagrer eller fordeler trafikk, blir strupet med HTTP 429 eller blokkert | Vilkårene beskriver krav til mellomlagring, utløpstider og trafikkmønster |
| Versjonering | Utgående produktversjoner avvikles vanligvis om lag en måned etter varsel | Varsles med HTTP 203, på api-users og i RSS-strømmen |
| Juridisk | Partnerdata og enkelte illustrasjoner har andre vilkår enn NLOD og CC BY 4.0 | Lisensen følger med i hvert svar fra Frost; bildeillustrasjoner har egne vilkår |
| Datakvalitet | Radarbaserte produkter faller ut der radardekningen svikter | Nowcast oppgir radardekning per punkt |

## Kanaler
Begge tjenestene er maskinelle REST-API-er uten egen brukerflate. api.met.no krever ingen innlogging, men hver forespørsel skal ha en identifiserende User-Agent med applikasjonsnavn og kontaktinformasjon. Frost krever en klient-ID som sendes med forespørselen. Klienthemmelighet og OAuth2 brukes bare for data som ikke er åpne.

Dokumentasjonen ligger på api.met.no og frost.met.no. Endringsvarsler går gjennom e-postlista api-users og RSS-strømmen, og MET anbefaler sterkt at faste brukere abonnerer. Spørsmål om Frost går til observasjon@met.no.

## Plattform
**Ikke offentlig dokumentert:** Driftsmodell og plattform for Frost og api.met.no.

**Fakta:** api.met.no har et eget endepunkt for helsestatus (api.met.no).

## Gjenbruk
Dataene er laget for gjenbruk: åpen lisens, dokumenterte API-er, versjonering og publiserte trafikkregler. Krediteringskravet er enkelt, for eksempel «Data fra MET Norway».

Gjenbruket har tre vilkår brukeren må ta inn i egen løsning: identifisering av klienten, mellomlagring av svar og kreditering av MET Norway.

### Vanlige kombinasjoner med andre produkter
- `KART-002` Geonorge, for kart og geografiske grunndata som værdataene vises eller analyseres mot.
- `ENTUR-001` Entur sanntids- og rutedata og `SVV-003` DATEX II trafikkinformasjon, når værdata skal ses sammen med kollektiv- eller trafikkdata.
- `DIGDIR-014` data.norge.no, som felles katalog for å finne åpne offentlige datasett.

**Kildekode:** Ikke offentlig dokumentert. Værikonene som brukes i api.met.no, er publisert som åpen kildekode; kildekoden for Frost og api.met.no er ikke funnet publisert.

**Lisens:** Ikke offentlig dokumentert for tjenestenes kildekode. Værikonene er lisensiert under `MIT` (api.met.no, License). Dataene er lisensiert under NLOD 2.0 og CC BY 4.0, som gjelder data, ikke kildekode.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  MET deler egne observasjoner, prognoser og varsler åpent og maskinlesbart, med en lisens som også tillater kommersiell bruk.

- **P5: Del og gjenbruk løsninger**
  Støttes delvis. Mange tjenester, også Yr, bygger på samme API-er i stedet for egne datakilder. Selve programvaren er ikke publisert for gjenbruk.

- **P6: Lag digitale løsninger som støtter samhandling**
  Støttes delvis. Dokumenterte og versjonerte API-er gjør dataene lette å bygge inn, men samhandlingen er enveis og uten avtalefestet leveransenivå.

Spenningen ligger i forholdet mellom åpenhet og forpliktelse. Tjenestene er fritt tilgjengelige, men MET gir ingen garanti for leveranse og kan strupe eller blokkere klienter. For virksomheter med samfunnskritiske prosesser betyr det at gratis tilgang ikke erstatter en avtale om leveranse. Frost har i tillegg stått i versjon v0 siden 2018, noe som gjør det uklart hvilken stabilitet brukerne kan forvente på lang sikt.

## Finansiering
**Fakta:** Data og produkter fra de selvbetjente nedlastingstjenestene er gratis. Tilpassede dataleveranser har oppstartsgebyr og årlig forvaltningsgebyr (met.no, Free meteorological data).

**Ikke offentlig dokumentert:** Hvordan utvikling og drift av Frost og api.met.no finansieres. Kildene skiller ikke API-ene ut fra METs øvrige virksomhet.

## Forvaltning/eier

| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Meteorologisk institutt (MET Norway) | api.met.no, frost.met.no |
| Driftsansvar | Meteorologisk institutt | api.met.no, Terms of Service |
| Budsjettansvar | Ikke offentlig dokumentert | – |
| Styringsmodell | MET er statlig etat underlagt Klima- og miljødepartementet | met.no, About MET Norway |
| Lisens og vilkår | MET fastsetter lisens, krediteringskrav og bruksvilkår | met.no, Licensing and Crediting |

## Lenke til dokumentasjon
- Frost: https://frost.met.no/index.html
- Frost, kom i gang: https://frost.met.no/howto.html
- Frost, bruksvilkår: https://frost.met.no/termsofuse2.html
- MET Weather API: https://api.met.no/
- MET Weather API, vilkår for bruk: https://api.met.no/doc/TermsOfService
- MET Weather API, lisens: https://api.met.no/doc/License
- Lisens og kreditering: https://www.met.no/en/Free-Meteorological-Data/Licensing-And-Crediting

## Kildegrunnlag brukt i utfyllingen
Hentet 2026-10-23:
- MET, Frost: https://frost.met.no/index.html
- MET, Frost, How to use: https://frost.met.no/howto.html
- MET, Frost, Terms of use: https://frost.met.no/termsofuse2.html
- MET, Frost, API-spesifikasjon: https://frost.met.no/swagger.json
- MET, MET Weather API: https://api.met.no/
- MET, Terms of Service: https://api.met.no/doc/TermsOfService
- MET, License: https://api.met.no/doc/License
- MET, Nowcast 2.0: https://api.met.no/weatherapi/nowcast/2.0/documentation
- MET, Radar 2.0: https://api.met.no/weatherapi/radar/2.0/documentation
- MET, Licensing and Crediting: https://www.met.no/en/Free-Meteorological-Data/Licensing-And-Crediting
- MET, Free meteorological data: https://www.met.no/en/free-meteorological-data
- MET, About MET Norway: https://www.met.no/en/About-us/About-MET-Norway
- Yr, bunntekst om samarbeidet mellom NRK og Meteorologisk institutt: https://www.yr.no/
