# Grep

## Navn
Grep

## Ressurs ID
UDIR-001

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Nasjonal kodeverks- og læreplandatabase, tilgjengelig som API

## Status/Livsfase
Aktiv. Grep er i drift og er den autoritative kilden til fastsatte læreplaner og fagkoder i Kunnskapsløftet. Databasen dekker både LK06 og LK20, og REST-tilgangen ble lagt om til nøkkelbasert autentisering med virkning fra 1. september 2026.

## Kort beskrivelse
Grep er Utdanningsdirektoratets nasjonale database for fag, læreplaner og opplæringstilbud i grunnopplæringen. Alle fastsatte læreplaner i Kunnskapsløftet legges inn i Grep, sammen med fagkoder, tilbudsstruktur, vurderingsordninger og de merknadene som brukes når opplæring skal dokumenteres på et vitnemål eller kompetansebevis.

Grep er ikke en nettside for sluttbrukere. Det er en datakilde andre løsninger henter fra og presenterer videre. Det gjør ressursen til et infrastrukturelt kodeverk framfor et publiseringsverktøy.

Grep er det semantiske navet i utdanningsdomenet. Når en elev søker seg inn i videregående, når karakterer skal føres, når et vitnemål skal utstedes og når statistikk skal sammenstilles, viser alle disse løpene til de samme fagkodene. Uten en felles og autoritativ kilde til hva et fag er, måtte hvert ledd i kjeden vedlikeholdt sin egen oversettelse.

## Formål og normerende rolle
Formålet er å gi én autoritativ representasjon av læreplanverket, slik at fag, læreplaner og opplæringstilbud kan refereres entydig på tvers av systemer og forvaltningsnivåer.

Den normerende rollen er sterk, men indirekte. Grep fastsetter ikke læreplaner — det gjør Kunnskapsdepartementet og Utdanningsdirektoratet gjennom ordinære vedtak. Grep er den maskinlesbare representasjonen av vedtakene. Normeringen ligger i at det finnes én kode per fag, og at alle som skal dokumentere eller behandle opplæring bruker den koden.

Det gjør at Grep i praksis binder sterkere enn en veileder gjør, uten å være et regelverk. En løsning som bruker egne fagkoder, blir ikke ulovlig, men den blir ubrukelig i samhandling.

## Forpliktelsesnivå og etterlevelse
Grep er styrende i praksis, uten å være formelt obligatorisk gjennom eget regelverk.

Bindingen oppstår gjennom bruk. Vitnemål og kompetansebevis skal dokumentere opplæring med de fastsatte fagkodene og merknadene, og statistikk og inntak bygger på samme koder. En skoleeier eller leverandør som ikke følger Grep, får dokumentasjon som ikke lar seg lese av mottakerne, og data som ikke lar seg sammenstille nasjonalt.

Etterlevelse skjer teknisk framfor gjennom kontroll. Fagsystemer og administrative løsninger konsumerer Grep-data direkte gjennom API, og feil koder gir feil i påfølgende ledd. Kildene beskriver ingen tilsyns- eller avviksordning knyttet til selve databasen.

En praktisk endring bør merkes: fra 1. september 2026 krever REST-tilgangen API-nøkkel, med en registreringsordning som åpnet 1. juni 2026. Anonyme kall er ratebegrenset. Det gjør at etterlevelse nå også innebærer et registreringsforhold til Utdanningsdirektoratet, ikke bare korrekt bruk av kodene.

## Kapabiliteter
- **Informasjonsforvaltning: Informasjonsarkitektur**
  Grep strukturerer og modellerer læreplanverket slik at fag, læreplaner og tilbudsstruktur kan tolkes likt på tvers av virksomheter og systemer.

- **Informasjonsforvaltning: Oversikt over begreper**
  Databasen er den autoritative begrepsoversikten for fag, læreplaner, vurderingsordninger og vitnemålsmerknader i grunnopplæringen.

- **Standardisering: Forvaltningsstandarder**
  Fagkodene fungerer som nasjonal forvaltningsstandard i utdanningsdomenet, og gjenbrukes av kodeverk og løsninger utenfor Utdanningsdirektoratet.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Leverandører av skoleadministrative systemer | Autoritative fagkoder og læreplandata | Karakterføring, vitnemål, timeplanlegging | Konsumerer Grep gjennom API |
| Fylkeskommunene og Novari | Nasjonale koder som grunnlag for eget kodeverk | Inntak og fagopplæring i videregående | `VIGO Kodeverk og kodeverksbase` (`NOVARI-007`) bygger direkte på Grep |
| Sikt | Fagkoder for dokumentasjon og verifisering | Nasjonal vitnemålsdatabase og Vitnemålsportalen | Deduksjon: koblingen følger av at vitnemålsdata bruker fastsatte fagkoder, men kildene beskriver den ikke eksplisitt |
| Statistikk- og analysemiljøer | Stabile koder over tid | Sammenstilling og tidsserier | Versjonering av læreplanverket er avgjørende her |
| Utdanningsdirektoratet | Egen dataforvaltning og publisering | Både forvalter og konsument av Grep | Kildene omtaler direktoratet som bruker av sine egne data |
| Nettsteder for elever og søkere | Presentasjon av tilbud og fag | `vilbli.no` og tilsvarende | Grep har ingen egen sluttbrukerflate |

## Normerende innhold
Grep inneholder de fastsatte læreplanene i Kunnskapsløftet, både LK06 og LK20, og skiller mellom dem i egne endepunkter. Ut over læreplantekstene selv inneholder databasen fagkoderegisteret, tilbudsstrukturen for videregående opplæring, vurderingsordninger, og de fag- og vitnemålsmerknadene som brukes ved dokumentasjon av opplæring.

Data er tilgjengelig i to former. REST-endepunktene følger mønsteret `https://data.udir.no/kl06/<versjon>/<type i flertall>/<kode>` og returnerer JSON og XML. I tillegg finnes et RDF- og SPARQL-endepunkt som gjør det mulig å spørre på grafstrukturen framfor å hente enkeltressurser. Det siste er relevant for semantisk arbeid, fordi relasjonene mellom læreplan, fag, kompetansemål og tilbud da kan traverseres direkte.

Versjonering er en del av det normerende innholdet. Endepunktene er versjonert i selve URL-en, slik at en konsument kan låse seg til en kjent versjon av datamodellen framfor å følge endringer fortløpende.

## Bruksområde
Grep bør brukes hver gang et fag, en læreplan eller et opplæringstilbud skal refereres i en løsning. Det gjelder skoleadministrative systemer, inntaks- og dokumentasjonsløsninger, statistikkproduksjon og nettsteder som presenterer utdanningstilbud.

Ressursen er også relevant i arkitekturarbeid som utgangspunkt for semantikk: den viser hvilke begreper som allerede er nasjonalt fastsatt i utdanningsdomenet, og hva som derfor ikke bør modelleres lokalt på nytt.

Den er mindre relevant når behovet gjelder den enkelte elevens opplysninger. Grep beskriver strukturen i opplæringen, ikke personene i den.

## Typiske analyse- og beslutningssituasjoner
- Anskaffelse av skoleadministrativt system, der støtte for Grep-koder bør være et krav framfor et ønske
- Vurdering av om et informasjonsbehov i utdanningsdomenet alt er dekket av nasjonalt kodeverk
- Utforming av integrasjoner mellom skoleeier, fylkeskommune og nasjonale løsninger
- Planlegging av overgang ved læreplanreform, der både gammel og ny læreplan må støttes samtidig
- Vurdering av konsekvensen av API-nøkkelkravet fra 1. september 2026 for eksisterende integrasjoner
- Semantisk modellering der SPARQL-endepunktet gir en rikere inngang enn REST

## Når ressursen normalt ikke er tilstrekkelig alene
Grep beskriver læreplanverket, ikke gjennomføringen. For elevdata, karakterer, fravær og inntak må ressursen suppleres med skoleadministrative systemer, `VIGO` (`NOVARI-004`) i videregående, og for dokumentasjon `Nasjonal vitnemålsdatabase` (`SIKT-004`).

For opplysninger om selve skolene og barnehagene gir Grep ingenting. Der er `Nasjonale registre for barnehage og grunnopplæring` (`UDIR-002`) den riktige kilden.

Grep løser heller ingen juridiske spørsmål om behandling av elevopplysninger, siden databasen ikke inneholder personopplysninger.

## Scope og avgrensning
Inngår:
- fastsatte læreplaner i Kunnskapsløftet, både LK06 og LK20
- fagkoder, tilbudsstruktur og vurderingsordninger
- fag- og vitnemålsmerknader for dokumentasjon av opplæring
- REST-API og RDF- og SPARQL-tilgang, med versjonerte endepunkter

Inngår ikke:
- personopplysninger om elever, lærlinger eller ansatte
- karakterer, fravær eller annen gjennomføringsdata
- opplysninger om skoler, barnehager eller skoleeiere
- sluttbrukerflate for elever, foresatte eller lærere
- fastsettelse av læreplaner, som skjer gjennom ordinære vedtak

Grensen mot `VIGO Kodeverk og kodeverksbase` (`NOVARI-007`) er verdt å merke: VIGO Kodeverk gjenbruker Grep-koder og kombinerer dem med skoleopplysninger og VIGO-spesifikke koder for videregående. Grep er kilden, VIGO Kodeverk er den fylkeskommunale sammenstillingen.

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Utdanningsdirektoratet. Selve læreplanene fastsettes gjennom ordinære vedtak, og Grep representerer vedtakene maskinlesbart |
| Forvaltningsansvar | Utdanningsdirektoratet, med eget Grep-team oppgitt som kontaktpunkt i dokumentasjonen |
| Endringsprosess | Endringer følger læreplanarbeidet. Datamodellen er versjonert i endepunktene, slik at konsumenter kan låse seg til en kjent versjon |
| Publiserings- og beslutningsarena | Utdanningsdirektoratets datasider, med teknisk dokumentasjon i to offentlige wikier og kildekode for SPARQL-endepunktet på GitHub |

## Relasjon til andre ressurser
- **Nasjonale registre for barnehage og grunnopplæring (`UDIR-002`)**
  Nærmeste nabo hos samme eier. Grep beskriver hva som læres, registrene beskriver hvor. De brukes normalt sammen.

- **VIGO Kodeverk og kodeverksbase (`NOVARI-007`)**
  Bygger direkte på Grep. Den viktigste videre bruken av Grep-kodene utenfor Utdanningsdirektoratet.

- **VIGO (`NOVARI-004`)** og **vigo.no (`NOVARI-009`)**
  Inntak og søknad i videregående bruker fag- og tilbudskodene som stammer fra Grep.

- **Nasjonal vitnemålsdatabase (`SIKT-004`)** og **Vitnemålsportalen (`SIKT-005`)**
  Dokumentasjon av fullført opplæring viser til fastsatte fagkoder. Koblingen er deduksjon ut fra hva vitnemål inneholder, ikke noe kildene sier direkte.

- **Felles datakatalog (`DIGDIR-011`)** og **Begrepskatalog (`DIGDIR-012`)**
  Grep er et etablert nasjonalt kodeverk og en naturlig kandidat for synliggjøring i den nasjonale katalogstrukturen.

- **Felles informasjonsmodeller (`DIGDIR-069`)**
  Prinsippet om å bygge på eksisterende begreper og definisjoner peker mot Grep for alle som modellerer i utdanningsdomenet.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er at opplæring kan dokumenteres og gjenkjennes på tvers av skoleeiere, fylkeskommuner og nasjonale løsninger. En elev som flytter mellom fylker, eller søker seg videre til høyere utdanning, får opplæringen sin lest riktig fordi kodene er de samme.

Arkitekturverdien er semantisk. Grep gjør at fag ikke må modelleres lokalt, og at hver integrasjon i utdanningskjeden kan vise til samme autoritative kilde framfor å avtale sin egen oversettelse. Versjonerte endepunkter og et SPARQL-grensesnitt gjør ressursen brukbar både for enkel oppslagsbruk og for semantisk arbeid.

## Konsekvens ved manglende bruk eller avvik
Uten Grep måtte hver skoleeier og hver leverandør vedlikeholdt egne fagkoder. Konsekvensen ville vært oversettelsestabeller i hvert integrasjonspunkt, og dokumentasjon som måtte tolkes manuelt ved flytting og videre opptak.

Brukt feil er konsekvensen konkret og synlig: en feil fagkode på et vitnemål gir feil i inntaket eller i opptaket til høyere utdanning, og treffer den enkelte eleven direkte.

Tolkes versjoneringen ulikt, oppstår problemer ved læreplanreform. To parter som ligger på ulik versjon, kan utveksle data som validerer teknisk men beskriver ulike fag.

For virksomheter som ikke har fulgt opp API-nøkkelkravet fra 1. september 2026, er konsekvensen ratebegrensning eller brudd i integrasjonen.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Endringsstyring | Læreplanreform gir parallelle kodeverk, som LK06 og LK20 samtidig | Konsumenter må håndtere to strukturer i en overgangsperiode | Bruke de versjonerte endepunktene og planlegge overgangen eksplisitt |
| Adopsjon | Grep har ingen sluttbrukerflate, og verdien avhenger av at leverandører faktisk konsumerer API-et | Lokale fagkodetabeller lever videre i eldre systemer | Stille krav om Grep-støtte i anskaffelser |
| Sammenheng med gjenbrukbare løsninger | Kravet om API-nøkkel fra 1. september 2026 er en ny forutsetning for eksisterende integrasjoner | Ratebegrensning eller brudd for dem som ikke har registrert seg | Kontrollere registreringsstatus for alle integrasjoner mot Grep |
| Semantisk kvalitet | Kodeverket beskriver struktur, ikke lokal praksis for hvordan fag tilbys | Ulik lokal tolkning av samme tilbud | Kombinere med `VIGO Kodeverk` for videregående og lokal dokumentasjon |
| Forankring | Grep er styrende i praksis, men uten eget regelverk eller kontrollordning | Uklart for virksomheter hvor forpliktende bruken er | Beskrive Grep som forutsetning i arkitekturkrav framfor som anbefaling |

## Publiseringsform og tilgjengelighet
Grep publiseres som API, ikke som nettsted. REST-endepunktene ligger under `data.udir.no/kl06/`, med versjon i URL-en, og returnerer JSON og XML. Et RDF- og SPARQL-endepunkt gir grafbasert tilgang. Teknisk dokumentasjon ligger i to offentlige wikier, og Utdanningsdirektoratet har publisert beskrivelsen av SPARQL-endepunktet på GitHub. Datasettene er lisensiert under Norsk lisens for offentlige data. Fra 1. september 2026 kreves API-nøkkel for REST-kall, med registrering åpnet 1. juni 2026, og anonyme kall er ratebegrenset til om lag hundre kall per minutt.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Direkte og sterk støtte. Grep er en autoritativ nasjonal datakilde som deles åpent under NLOD og gjenbrukes bredt i sektoren.

- **P6: Lag digitale løsninger som støtter samhandling**
  Felles fagkoder er en forutsetning for at opplæringsdata kan flyte mellom skoleeier, fylkeskommune og nasjonale løsninger.

- **P2: Ta arkitekturbeslutninger på rett nivå**
  Semantikken i læreplanverket er løftet til nasjonalt nivå framfor å løses lokalt i hver virksomhet.

- **P1: Ta utgangspunkt i brukernes behov**
  Støttes indirekte. Eleven møter aldri Grep, men riktige koder er det som gjør at vitnemålet leses riktig videre.

Begrensninger og spenninger: Grep er styrende i praksis uten å være hjemlet som krav, og det gir et uklart forpliktelsesnivå som virksomheter må tolke selv. Ressursen har ingen sluttbrukerflate, så nytten avhenger fullt ut av at leverandører bygger den inn. Innføringen av API-nøkkel fra 1. september 2026 strammer inn en tidligere åpen tilgang, og det bør vurderes som en reell endring i tilgjengelighet for eksisterende integrasjoner, ikke bare som en teknisk detalj.

## Lenke til dokumentasjon
- https://www.udir.no/om-udir/data/kl06-grep/
- https://www.udir.no/om-udir/data/
- https://grepwiki.udir.no/index.php?title=Hovedside
- https://github.com/Utdanningsdirektoratet/KL06-LK20-public/wiki
- https://github.com/Utdanningsdirektoratet/Grep_SPARQL

## Kildegrunnlag brukt i utfyllingen
- https://www.udir.no/om-udir/data/kl06-grep/, kontrollert 2026-09-07
- https://www.udir.no/om-udir/data/, kontrollert 2026-09-07
- https://github.com/Utdanningsdirektoratet, kontrollert 2026-09-07
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-07
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-07
- `arkitektur/ressurser/styringsregler.md`, kontrollert 2026-09-07
