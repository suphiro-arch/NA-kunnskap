# eDelivery Building Block

## Navn
eDelivery Building Block

## Ressurs ID
EU-003

## Status/Livsfase
**Produksjon** - aktiv byggestein med forvaltede spesifikasjoner, referanseprogramvare og et stort antall økosystemer i bruk.

**Fakta:** Europakommisjonen fører eDelivery som aktiv byggestein i DIGITAL Building Blocks, sist oppdatert 4. mars 2026, og oppgir at om lag 39 digitale økosystemer gjenbruker eDelivery-infrastrukturen.

**Fakta:** eDelivery AS4 2.0-profilen er offisielt vedtatt, og Kommisjonen gjennomførte interoperabilitetstesting av den vedtatte versjonen i desember 2025 med en oppfølgende sesjon 22. januar 2026, der fire eksterne leverandører deltok ved siden av Kommisjonens egen referanseimplementasjon Domibus.

## Modenhet
**Høy modenhet som samhandlingsmønster, med tydelig leverandørmarked.**

- Teknisk: profilen bygger på etablerte, åpne spesifikasjoner, og Kommisjonen publiserer referanseprogramvaren Domibus som aksesspunkt og DomiSMP som tjenestemetadatapublisering. Domibus 5.2 og 5.1 er presentert i 2026.
- Organisatorisk: modellen er vendor- og plattformnøytral, og en virksomhet kan velge konform tredjepartsprogramvare, Kommisjonens referanseprogramvare eller en ekstern leverandør.
- Bruksmessig: om lag 39 økosystemer gjenbruker infrastrukturen, og profilen er grunnlaget for blant annet OOTS.
- Regulatorisk: byggesteinen er ikke i seg selv bindende, men er forutsatt i rettsakter som bygger på den.

**Deduksjon:** Det svakeste leddet er at eDelivery er et mønster, ikke en ferdig tjeneste. Verdien realiseres først når et konkret økosystem har definert sin egen profil, sine deltakere og sin tillitsmodell. En virksomhet som «tar i bruk eDelivery» uten å vite hvilket økosystem den skal delta i, har ikke tatt noe reelt arkitekturvalg.

## Kort beskrivelse
eDelivery Building Block er Europakommisjonens felles byggestein for sikker og etterprøvbar utveksling av dokumenter og data mellom virksomheter og myndigheter. Byggesteinen består av åpne spesifikasjoner, referanseprogramvare og støttetjenester som en organisasjon kan bruke til å sette opp og drifte sin egen meldingsutvekslingsinfrastruktur, framfor å bygge bilaterale integrasjoner mot hver motpart.

Modellen er føderert: deltakerne kommuniserer gjennom aksesspunkt som følger samme profil, og finner hverandre gjennom tjenestemetadata. Kommunikasjonen krever digitalt signerte kvitteringer for mottak, og bruker kryptering for å beskytte integritet og konfidensialitet. Byggesteinen er innholdsnøytral: den transporterer meldinger uten å definere hva som står i dem.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsutveksling**
  gir et felles mønster for å sende og motta meldinger mellom parter som ikke har avtale med hverandre fra før, gjennom aksesspunkt og dynamisk oppslag av mottakerens kapabiliteter.

- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling**
  leverer signerte mottakskvitteringer, kryptering og et sertifikatbasert tillitsoppsett som gjør utvekslingen etterprøvbar.

- **Standardisering: EU standarder**
  forvalter selve AS4-profilen og tjenestemetadataspesifikasjonene, og gjør dem tilgjengelige med konformitetstesting, slik at europeiske standarder faktisk kan tas i bruk.

Koblingene er satt fordi byggesteinen selv eier profilen, referanseprogramvaren og testregimet. Innholdet i meldingene og de forretningsmessige prosessene rundt dem leveres av de økosystemene som bruker byggesteinen, og hører ikke her.

## Produktmål
**Dokumenterte mål** slik Kommisjonen beskriver byggesteinen:
- Gi offentlige og private organisasjoner en sikker og interoperabel kanal for å overføre dokumenter og data seg imellom.
- Tilby spesifikasjoner, referanseprogramvare og støttetjenester slik at organisasjoner kan sette opp og drifte egen meldingsinfrastruktur.
- Være vendor- og plattformnøytral, med ikke-proprietære, åpne spesifikasjoner tilgjengelig i flere produkter.

**Utledede operative mål:**
- Redusere antall bilaterale integrasjoner ved å erstatte dem med ett felles mønster per økosystem.
- Gjøre det mulig å bytte leverandør av aksesspunkt uten å endre motpartenes oppsett.

## Brukerbehov
- Virksomheter trenger å utveksle dokumenter med mange motparter uten å avtale teknisk oppsett med hver enkelt.
- Myndigheter som etablerer et nytt utvekslingsøkosystem trenger et ferdig, prøvd mønster framfor å definere transport og tillit fra bunnen.
- Integrasjonsmiljøer trenger konformitetstesting for å vite at implementasjonen faktisk virker mot andre.
- Forvaltningsmiljøer trenger etterprøvbarhet: bevis for at en melding er sendt, mottatt og ikke endret underveis.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Eiere av digitale økosystemer | Ferdig transportmønster for et nytt utvekslingsnettverk | Definere egen profil og deltakermodell | Den viktigste brukergruppen; byggesteinen er laget for dem |
| Offentlige virksomheter | Sikker utveksling med kjente og ukjente motparter | Saksdokumenter, bevis, rapportering | Deltar oftest gjennom et etablert økosystem |
| Programvareleverandører | Bygge og sertifisere konforme aksesspunkt | Produktutvikling | Kan bruke Domibus eller egen implementasjon |
| Driftsmiljøer | Installere og drifte aksesspunkt og tjenestemetadata | Domibus, DomiSMP | Krever egen drift og sertifikatforvaltning |
| Europakommisjonen | Forvalte profil, programvare og testing | Spesifikasjon og konformitet | Eier byggesteinen |

## Hovedfunksjoner
Den bærende funksjonen er **transport mellom aksesspunkt**. To parter kommuniserer ikke direkte, men gjennom hvert sitt aksesspunkt som følger eDelivery AS4-profilen. Profilen definerer hvordan meldingen pakkes, signeres, krypteres og kvitteres for, uavhengig av hva meldingen inneholder. Dette gjør at samme infrastruktur kan brukes til fakturaer, bevis, saksdokumenter og strukturerte datasett.

Den andre funksjonen er **dynamisk oppslag av mottaker**. Tjenestemetadatapublisering, Service Metadata Publisher, gjør det mulig å slå opp hvilke dokumenttyper og prosesser en deltaker støtter, og hvor meldingen skal sendes. Uten dette laget måtte hver avsender vedlikeholde en egen liste over motparter og deres kapabiliteter.

Den tredje funksjonen er **referanseprogramvare**. Kommisjonen leverer Domibus som aksesspunktimplementasjon og DomiSMP for tjenestemetadata. Programvaren er ment som et utgangspunkt og som målestokk for andre implementasjoner, ikke som eneste vei inn i nettverket.

Den fjerde funksjonen er **konformitetstesting og innføringsstøtte**. Kommisjonen beskriver en firetrinns innføring: kartlegg behov, velg implementasjonsmåte, sett opp med tilgjengelige eDelivery-tjenester, og drift og skaler nettverket. Interoperabilitetsarrangementene, som testingen av AS4 2.0 i desember 2025 og januar 2026, er en del av dette.

### Typiske brukssituasjoner (generisk)
- Et nytt nasjonalt eller europeisk utvekslingsnettverk skal etableres, og transportmønsteret må velges.
- En virksomhet skal koble seg til et eksisterende økosystem som bygger på eDelivery, som OOTS.
- En løsning krever dokumenterbar levering med kvittering, ikke bare et kall mot et grensesnitt.

### Når eDelivery Building Block normalt ikke er førstevalg
- Når behovet er dokumentutveksling i norsk offentlig sektor. Da er `eFormidling` den etablerte nasjonale løsningen, og `Peppol eDelivery` det etablerte mønsteret for handelsdokumenter.
- Når behovet er synkront oppslag mot et register. Da er et API og `Maskinporten` en enklere vei enn asynkron meldingsutveksling.
- Når det bare er to parter som skal utveksle data, og begge er kjent. Kostnaden ved aksesspunkt og sertifikatforvaltning står da ikke i forhold til nytten.
- Når det ikke finnes et definert økosystem å delta i. Byggesteinen alene løser ikke hvem som er deltakere eller hvilke dokumenter som gjelder.

### Scope og avgrensning
Inngår: AS4-profilen, tjenestemetadataspesifikasjoner, referanseprogramvaren Domibus og DomiSMP, konformitetstesting og innføringsveiledning.

Inngår ikke: dokumentformater og forretningsinnhold, avtaleverk og deltakerforvaltning i det enkelte økosystemet, og drift av aksesspunkt.

Avgrensningen mot `Peppol eDelivery` er viktig. Peppol er et operativt, føderert økosystem med egen myndighetsstruktur, i bruk i norsk sammenheng gjennom blant annet `ELMA`. eDelivery Building Block er den bredere EU-byggesteinen med programvare, test og støttefunksjoner rundt samme problemområde. De to skal ikke behandles som samme ressurs.

## Veikart over kommende funksjonalitet
**Fakta:** AS4 2.0-profilen er vedtatt og testet gjennom interoperabilitetsarrangementer i desember 2025 og januar 2026. Domibus 5.2 og 5.1 er presentert i mars 2026, med endringer i teknisk plattform, konfigurasjon, utrulling og ytelse.

**Fakta:** Kommisjonen har publisert oppfordringer om å oppgradere etter sikkerhets- og feilrettingsutgivelser sent i 2025 og tidlig i 2026.

**Ikke offentlig dokumentert i denne arbeidsøkten:** en samlet, datofestet plan for byggesteinens videre utvikling utover profil- og programvareutgivelser.

## Forretningsverdi/Verdiforslag
**For eiere av økosystemer:** et ferdig, prøvd transportmønster med testregime, som sparer både utviklingstid og risikoen ved å definere egen sikkerhetsmodell.

**For virksomheter:** færre integrasjoner å vedlikeholde, og mulighet til å bytte leverandør uten at motpartene berøres.

**For samfunnet:** felles infrastruktur på tvers av sektorer og land, som gjør at nye samhandlingsbehov kan løses raskere enn om hver sektor bygger sitt eget.

**For forvaltningen:** dokumenterbar levering med signerte kvitteringer gir et etterprøvbart spor, som er nødvendig når utvekslingen har rettslige virkninger.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Teknisk | Sertifikat- og nøkkelforvaltning er en vedvarende driftsoppgave som ofte undervurderes | Følg Kommisjonens innføringstrinn; ingen automatisert løsning er dokumentert i denne arbeidsøkten |
| Organisatorisk | Byggesteinen løser ikke deltakerforvaltning og avtaleverk i økosystemet | Må avklares i det enkelte økosystemet før teknisk oppsett |
| Kompleksitet | Asynkron utveksling med aksesspunkt gir høyere terskel enn et vanlig API | Vurder om behovet faktisk krever etterprøvbar levering |
| Versjonsstyring | Overgang til AS4 2.0 krever koordinert oppgradering hos alle deltakere | Interoperabilitetstesting er gjennomført; tidsplan for utfasing av tidligere profil er ikke dokumentert i denne arbeidsøkten |
| Sikkerhet | Utdaterte versjoner av referanseprogramvaren gir kjent sårbarhet | Kommisjonen publiserer oppgraderingsoppfordringer ved hver utgivelse |
| Overlapp | Forveksling med `Peppol eDelivery` gir feil forventninger om hva som er i bruk i Norge | Skillet er logget i `briefs/decisions.md` 18. mars 2026 |

## Kanaler
Byggesteinen leveres som dokumentasjon, nedlastbar referanseprogramvare og testtjenester gjennom Kommisjonens portal for DIGITAL Building Blocks. Den har ingen sluttbrukerflate.

Den operative kanalen er maskinell: aksesspunkt som utveksler AS4-meldinger, med oppslag mot tjenestemetadata. En virksomhet møter byggesteinen enten ved å drifte eget aksesspunkt eller ved å kjøpe tilgang hos en leverandør.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** driftsmodell for deltakernes aksesspunkt. Det som er kjent, er at Domibus og DomiSMP er programvare som installeres og driftes av den enkelte organisasjonen, og at byggesteinen er beskrevet som plattformnøytral. Plattformvalget ligger dermed hos deltakeren, ikke i byggesteinen.

## Gjenbruk
Byggesteinen er laget for gjenbruk: spesifikasjonene er åpne og ikke-proprietære, referanseprogramvaren kan lastes ned, og konformitetstesting gjør det mulig å verifisere egen implementasjon mot andre. Kommisjonen oppgir at om lag 39 digitale økosystemer gjenbruker infrastrukturen.

Avhengigheter som ikke er kapabiliteter her: tillitsmodellen bygger på sertifikater fra tillitstjenester, og innholdet som transporteres er definert av det enkelte økosystemet.

**Vanlige kombinasjoner med andre produkter:**
- `Once-Only Technical System`, som bruker eDelivery som transportlag mellom myndigheter.
- `Peppol eDelivery` og `ELMA`, som dekker samme problemområde i det norske handelsdokumentsporet.
- `eFormidling`, som er den norske fellesløsningen for sikker dokumentutveksling i offentlig sektor.
- `eSignature Building Block`, når innholdet i meldingen også skal signeres og valideres.

**Kildekode:** Åpen kildekode. Domibus og DomiSMP publiseres av Europakommisjonen som referanseprogramvare.

**Lisens:** Ikke offentlig dokumentert. Lisensvilkårene er ikke kontrollert mot repositoriet i denne arbeidsøkten.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Et felles transportmønster senker terskelen for at data faktisk deles, fordi utvekslingen ikke må avtales teknisk per motpart.
- **P5: Del og gjenbruk løsninger**
  Åpne spesifikasjoner, referanseprogramvare og konformitetstesting er gjenbruk satt i system, og gjør det mulig for mange økosystemer å bygge på samme grunnlag.
- **P6: Lag digitale løsninger som støtter samhandling**
  Støttes tydelig: hele byggesteinen finnes for å gjøre samhandling mellom uavhengige parter mulig.
- **P7: Sørg for tillit til oppgaveløsningen**
  Signerte kvitteringer, kryptering og sertifikatbasert tillit gir etterprøvbar leveranse.

**Spenning og begrensning:** Byggesteinen støtter **P1: Ta utgangspunkt i brukernes behov** bare indirekte. Den er infrastruktur, og brukernytten oppstår først i tjenestene som bygger på den. Den står også i spenning mot **P2: Ta arkitekturbeslutninger på rett nivå**: for et lite utvekslingsbehov med få parter gir mønsteret merkostnad uten tilsvarende gevinst, og valget bør da tas på lavere nivå. I norsk sammenheng er den viktigste begrensningen at etablerte nasjonale løsninger allerede dekker mange av behovene, slik at byggesteinen oftest er relevant gjennom et europeisk økosystem framfor som selvstendig valg.

## Finansiering
**Fakta:** Byggesteinen forvaltes og finansieres av Europakommisjonen som del av DIGITAL-programmet for byggesteiner. Spesifikasjoner og referanseprogramvare er tilgjengelige uten lisenskostnad.

**Deduksjon:** Kostnaden for en deltaker ligger i drift av eget aksesspunkt eller i kjøp av tjenesten fra en leverandør, ikke i selve byggesteinen. Kildene i denne arbeidsøkten oppgir ikke priser.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Europakommisjonen | DIGITAL Building Blocks, eDelivery |
| Forvaltning av AS4-profilen | Europakommisjonen | Kommisjonens omtale av vedtatt AS4 2.0-profil |
| Drift av aksesspunkt | Den enkelte deltakeren eller dens leverandør | Kommisjonens innføringstrinn med valg av implementasjonsmåte |
| Budsjettansvar | Europakommisjonen for byggesteinen; deltakerne for egen drift | Deduksjon fra ansvarsdelingen over |
| Styringsmodell | Ikke offentlig dokumentert i denne arbeidsøkten | - |

## Lenke til dokumentasjon
- eDelivery Building Block: https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eDelivery
- DIGITAL Building Blocks, samleside: https://interoperable-europe.ec.europa.eu/collection/digital-building-blocks
- eDelivery AS4: https://ec.europa.eu/digital-building-blocks/sites/spaces/DIGITAL/pages/467117620/eDelivery+AS4

## Kildegrunnlag brukt i utfyllingen
- Europakommisjonen, eDelivery Building Block, hentet 24. september 2026.
- Europakommisjonen, DIGITAL Building Blocks, hentet 24. september 2026.
- Europakommisjonen, nyhetssaker om AS4 2.0-interoperabilitetstesting og Domibus 5.1 og 5.2, hentet 24. september 2026.
- Lokale kilder: `arkitektur/ressurser/produktnummerering.md`, `briefs/decisions.md`, `arkitektur/kapabiliteter/capabilities.yaml`, `arkitektur/prinsipper/principles.md`, `sources/links.md`.
