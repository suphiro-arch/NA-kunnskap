# FINT Arkivintegrasjoner

## Navn
FINT Arkivintegrasjoner

Registeret fører ressursen som `Arkivintegrasjoner`. Novari bruker `FINT Arkivintegrasjoner` som tjenestenavn, og det navnet er lagt til grunn her.

## Ressurs ID
NOVARI-008

## Status/Livsfase
**Produksjon** - tjenesten er i drift, og antall integrasjoner mot arkiv er under utvidelse.

**Fakta:** Novari fører FINT Arkivintegrasjoner som en egen tjeneste i sin tjenesteoversikt, bygget på integrasjonsplattformen FINT Flyt. Novari oppgir at veikartet for FINT Flyt er rettet mot å øke antall integrasjoner mot arkiv og å utvikle et nytt, mer brukervennlig grensesnitt.

**Fakta:** Novari oppgir integrasjon mellom arkiv og `eGrunnerverv` som et konkret eksempel på bruk.

## Modenhet
**Moden plattform, voksende integrasjonsbredde.**

- Teknisk: FINT Flyt er en etablert integrasjonsplattform der integrasjoner settes opp gjennom konfigurasjon framfor programmering, med overvåking av dataoverføringer og feilretting innebygd.
- Funksjonelt: bredden avgjøres av hvilke arkivintegrasjoner som er ferdigstilt, og den er under utvidelse ifølge Novaris eget veikart.
- Organisatorisk: tjenesten er innrettet mot at domeneeksperter kan etablere og vedlikeholde integrasjoner uten å involvere utviklere, noe som flytter arbeidet fra IKT-miljøet til fagmiljøet.
- Brukermessig: Novari oppgir selv at et nytt og mer brukervennlig grensesnitt er under utvikling, som er et signal om at dagens flate er et forbedringspunkt.

**Deduksjon:** Det svakeste leddet er dekningen per fagsystem. Plattformen er generell, men verdien for en gitt fylkeskommune avhenger av om nettopp dens fagsystem er støttet. En vurdering bør derfor starte med hvilke integrasjoner som faktisk finnes, ikke med plattformens egenskaper.

## Kort beskrivelse
FINT Arkivintegrasjoner er Novaris tjeneste for å koble fagsystemer mot sak- og arkivsystemer i fylkeskommunene, bygget på integrasjonsplattformen FINT Flyt. Tjenesten dekker selve arbeidsflyten: hvordan et dokument eller en sak beveger seg fra et fagsystem og inn i arkivet, med dataomforming underveis.

Tjenesten skiller seg fra `FINT Arkiv` ved å ligge et nivå over. `FINT Arkiv` er grensesnittet mot arkivsystemene, med felles informasjonsmodell og API. FINT Arkivintegrasjoner er de konkrete integrasjonsløpene som bruker dette grensesnittet, satt opp og forvaltet gjennom konfigurasjon.

Den sentrale egenskapen er at integrasjoner kan settes opp uten utviklere. Domeneeksperter oppretter integrasjoner mellom støttede fagsystemer og konfigurerer dataomforming selv, og kan følge med på dataoverføringene og rette feil.

## Kapabiliteter
- **Samarbeid: Organisatorisk samhandling**
  Tjenesten effektiviserer arbeidsprosessene mellom fagområde og arkiv ved at dokumenter og saksopplysninger flyter automatisk inn i arkivet, framfor at saksbehandleren overfører dem manuelt mellom to systemer.

- **Tjenesteutvikling: Gjenbrukbare tjenester**
  Et integrasjonsoppsett som er laget én gang, kan brukes av flere fylkeskommuner med samme fagsystem, og plattformen reduserer dermed antallet integrasjoner som må bygges i sektoren samlet.

Koblingene er satt fordi tjenesten selv leverer arbeidsflyten og gjenbruket av integrasjonsoppsett. Selve tilgangen til arkivinformasjon leveres av `FINT Arkiv` gjennom felles API og informasjonsmodell, og evnene til å dele og bruke arkivdata hører hos den ressursen. Avhengigheten er beskrevet under `Gjenbruk`.

## Produktmål
**Dokumenterte mål**, slik Novari beskriver FINT Flyt og arkivintegrasjonene:
- Forenkle og redusere antall integrasjoner mellom fagsystemer.
- Gi store tids- og kostnadsbesparelser ved oppsett og vedlikehold av nye integrasjoner, sammenlignet med å programmere dem.
- Gjøre det mulig for domeneeksperter å etablere og vedlikeholde integrasjoner uten teknisk personell.
- Øke informasjonsflyten og styrke leverandøruavhengigheten.

**Utledede operative mål:**
- Sikre at dokumenter faktisk blir arkivert, ved å gjøre arkivering til en del av arbeidsflyten framfor et eget steg.
- Gjøre det mulig å endre en integrasjon uten et utviklingsprosjekt.

## Brukerbehov
- Fylkeskommuner trenger at saksdokumenter fra fagsystemer havner i arkivet uten manuell overføring.
- Fagmiljøer trenger å kunne endre en integrasjon når arbeidsprosessen endres, uten å vente på utviklerkapasitet.
- Arkivmiljøer trenger at det som arkiveres følger en kjent struktur, slik at arkivet holder kvalitet.
- IKT-miljøer trenger å redusere antallet punkt-til-punkt-integrasjoner de må forvalte.
- Fylkeskommuner trenger å kunne bytte fagsystem eller arkivsystem uten å bygge om alt annet.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Fylkeskommuner | Automatisk arkivering fra fagsystemer | Saksbehandling og dokumentflyt | Primærmålgruppen for FINT-tjenestene |
| Domeneeksperter i fagmiljøet | Sette opp og endre integrasjoner selv | Konfigurasjon og dataomforming | Den egenskapen som skiller plattformen fra programmerte integrasjoner |
| Arkivmiljøet | Riktig og fullstendig arkivering | Kvalitetssikring av arkivet | Har interesse av strukturen, ikke av oppsettet |
| IKT-forvaltning i fylkeskommunen | Færre integrasjoner å drifte | Systemforvaltning | Avlastes, men må fortsatt eie plattformtilknytningen |
| Novari IKS | Forvalte og utvide plattformen | Tjenesteutvikling | Eier tjenesten |

## Hovedfunksjoner
Den første hovedfunksjonen er **konfigurerbare integrasjonsløp**. En integrasjon settes opp mellom støttede fagsystemer gjennom konfigurasjon framfor koding. Det er dette som gjør at oppsettet kan gjøres av noen som kjenner arbeidsprosessen, ikke bare av noen som kjenner systemene teknisk.

Den andre er **dataomforming**. Data fra et fagsystem har sjelden samme struktur som arkivet forventer. Plattformen konverterer mellom formene som del av integrasjonsløpet, slik at det ikke kreves en egen tilpasning i hvert av systemene.

Den tredje er **overvåking og feilretting**. Brukerne kan følge med på dataoverføringene og rette feil når noe stopper. For arkivflyt er dette en vesentlig funksjon: en feilet overføring betyr at et dokument ikke er arkivert, og det må oppdages, ikke bli stående ubemerket.

Den fjerde er **arkivspesifikke integrasjoner**. Arkivsporet er skilt ut som en egen tjeneste fordi arkiv er det største og mest gjentakende integrasjonsbehovet i fylkeskommunene. Novari oppgir integrasjon mellom arkiv og `eGrunnerverv` som et eksempel, og veikartet peker mot flere slike integrasjoner.

### Typiske brukssituasjoner (generisk)
- En fylkeskommune skal sørge for at dokumenter fra et fagsystem automatisk arkiveres i sak- og arkivsystemet.
- En arbeidsprosess endres, og integrasjonen må justeres uten et utviklingsprosjekt.
- En fylkeskommune skal koble et nytt fagsystem til eksisterende arkiv.
- En fylkeskommune vurderer å bytte arkivsystem og vil vite hva det gjør med integrasjonene.

### Når FINT Arkivintegrasjoner normalt ikke er førstevalg
- Når behovet er tilgang til arkivinformasjon gjennom et API, ikke en arbeidsflyt. Da er `FINT Arkiv` riktig nivå.
- Når behovet gjelder kommunal sektor. Da er `Fiks protokoll` med grensesnittet `Fiks arkiv` den tilsvarende løsningen.
- Når behovet er generell datadeling mellom fylkeskommunale systemer uten arkiv involvert. Da hører løsningen hos `FINT Felleskomponent` eller FINT Flyt generelt.
- Når fagsystemet ikke er støttet av plattformen. Da må dekningen avklares med Novari før løsningen planlegges.

### Scope og avgrensning
Inngår: oppsett, konfigurasjon, dataomforming, overvåking og feilretting av integrasjonsløp mellom fagsystemer og sak- og arkivsystemer i fylkeskommunal sektor.

Inngår ikke: selve arkivgrensesnittet og informasjonsmodellen, som leveres av `FINT Arkiv` og `FINT Informasjonsmodell`; fagsystemene og arkivsystemene; og arkivfaglige vurderinger av hva som skal arkiveres.

FINT Flyt som generell integrasjonsplattform er ikke registrert som egen ressurs i oversikten. Denne beskrivelsen dekker arkivsporet, som er det Novari selv har skilt ut som egen tjeneste.

## Veikart over kommende funksjonalitet
**Fakta:** Novari oppgir at veikartet for FINT Flyt er rettet mot å øke antall integrasjoner mot arkiv og å utvikle et nytt, mer brukervennlig grensesnitt.

**Ikke offentlig dokumentert i denne arbeidsøkten:** hvilke konkrete fagsystemer som står for tur, og når det nye grensesnittet kommer.

## Forretningsverdi/Verdiforslag
**For fylkeskommunene:** lavere kostnad ved å etablere og vedlikeholde integrasjoner, og kortere tid fra behov til fungerende løsning.

**For fagmiljøene:** de kan endre integrasjonen når arbeidsprosessen endres, uten å stå i kø hos et utviklingsmiljø. Det er den mest konkrete gevinsten plattformen gir.

**For arkivmiljøene:** dokumenter arkiveres som del av arbeidsflyten, som gir bedre arkivkvalitet enn manuell overføring og reduserer risikoen for at noe ikke blir arkivert i det hele tatt.

**For sektoren:** leverandøruavhengighet og færre integrasjoner samlet sett, fordi et oppsett kan gjenbrukes på tvers av fylkeskommuner med samme fagsystem.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Dekning | Verdien avhenger av om det aktuelle fagsystemet er støttet | Avklar støtte med Novari før løsningen planlegges; veikartet peker mot flere integrasjoner |
| Organisatorisk | Konfigurasjon uten utviklere flytter ansvar til fagmiljøet, som må ha kapasitet og kompetanse til å eie det | Uavklart hvem som eier oppgaven når fagpersonen slutter |
| Arkivkvalitet | Feil i dataomforming gir feil i arkivet, ikke bare en feilmelding | Overvåking og feilretting er innebygd, men må faktisk følges opp |
| Bruker | Novari oppgir selv at et nytt og mer brukervennlig grensesnitt er under utvikling | Dagens flate er et kjent forbedringspunkt |
| Avhengighet | Tjenesten forutsetter `FINT Arkiv` og den felles informasjonsmodellen | Endringer i modellen slår gjennom i integrasjonene |
| Leverandør | Plattformen er Novaris egen | Leverandøruavhengighet mot fagsystemene, men avhengighet til Novari som plattformeier |

## Kanaler
Tjenesten har to flater. Den ene er en konfigurasjonsflate der integrasjoner opprettes, dataomforming settes opp, og overføringer overvåkes. Den andre er den maskinelle flaten, der integrasjonene faktisk kjører mellom fagsystem og arkiv.

Det finnes ingen sluttbrukerflate. En saksbehandler merker tjenesten ved at dokumentet havner i arkivet, ikke ved å bruke den.

Novari tilbyr kundestøtte gjennom sin kundeportal, der brukerne kan melde feil eller foreslå endringer.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** driftsmodell, lokasjon og teknisk plattform. Det som er kjent, er at FINT Flyt driftes av Novari IKS som en felles plattform for eierne, og at fylkeskommunene ikke drifter integrasjonsplattformen selv.

## Gjenbruk
Gjenbruket skjer på to nivåer. Plattformen gjenbrukes på tvers av alle integrasjoner, og det enkelte integrasjonsoppsettet kan gjenbrukes av flere fylkeskommuner med samme fagsystem. Dette er den samme logikken som ligger til grunn for hele FINT-økosystemet: felles modell, felles API-er og leverandøruavhengige koblinger.

Avhengigheter som ikke er kapabiliteter her: `FINT Arkiv` leverer arkivgrensesnittet, og `FINT Informasjonsmodell` leverer den felles strukturen. Evnene til å dele og bruke arkivdata og til å forvalte informasjonsmodellen hører hos dem.

**Vanlige kombinasjoner med andre produkter:**
- `FINT Arkiv` som grensesnittet mot sak- og arkivsystemene.
- `FINT Informasjonsmodell` som den felles strukturen integrasjonene omformer til.
- `FINT Felleskomponent` for standardiserte integrasjoner utenfor arkivområdet.
- `eGrunnerverv`, som Novari oppgir som et konkret eksempel på arkivintegrasjon.
- `Fiks protokoll` som den kommunale parallellen til samme behov.

**Kildekode:** Ikke offentlig dokumentert. Kildene i denne arbeidsøkten sier ikke om FINT Flyt eller arkivintegrasjonene er publisert som åpen kildekode. Flere andre FINT-komponenter er publisert åpent, men det er ikke kontrollert mot repositoriet for denne tjenesten.

**Lisens:** Ikke offentlig dokumentert.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger**
  En felles integrasjonsplattform erstatter programmerte punkt-til-punkt-integrasjoner, og oppsett kan gjenbrukes mellom fylkeskommuner.
- **P4: Del og gjenbruk data**
  Data flyter fra fagsystem til arkiv uten manuell overføring, som er forutsetningen for at de i det hele tatt blir tilgjengelige videre.
- **P6: Lag digitale løsninger som støtter samhandling**
  Tjenesten kobler systemer med ulike leverandører gjennom en felles modell framfor gjennom bilaterale koblinger.
- **P2: Ta arkitekturbeslutninger på rett nivå**
  Støttes ved at integrasjonen settes opp av dem som kjenner arbeidsprosessen, framfor at den må gjennom et teknisk prosjekt.

**Spenning og begrensning:** Tjenesten står i spenning mot **P5: Del og gjenbruk løsninger** på plattformnivå: den reduserer avhengigheten til fagsystemleverandørene, men øker avhengigheten til Novari som plattformeier. Den er også i praktisk spenning mot **P2**: å flytte integrasjonsansvar til fagmiljøet gir raskere endringer, men forutsetter en kompetanse og en kontinuitet som ikke alle fagmiljøer har, og som kildene ikke sier noe om hvordan sikres. Ved vurdering av bruk bør det avklares hvem som eier integrasjonene over tid, ikke bare hvem som setter dem opp.

## Finansiering
**Ikke offentlig dokumentert i denne arbeidsøkten:** prismodell for FINT Arkivintegrasjoner. Det som er kjent, er at Novari IKS er et interkommunalt selskap eid av fylkeskommunene, og at tjenestene inngår i selskapets tjenesteportefølje med budsjett vedtatt av representantskapet.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Novari IKS | Novaris tjenesteoversikt og tjenesteside for FINT Flyt |
| Driftsansvar | Novari IKS | Samme |
| Oppsett og forvaltning av den enkelte integrasjonen | Den enkelte fylkeskommunen, ved domeneeksperter | Novari om at integrasjoner settes opp uten utviklere |
| Arkivgrensesnitt og informasjonsmodell | Novari IKS, gjennom `FINT Arkiv` og `FINT Informasjonsmodell` | Registeroppføringene `NOVARI-002` og `NOVARI-003` |
| Budsjettansvar | Novari IKS, med representantskapet som besluttende organ | Novaris budsjettdokumenter |
| Styringsmodell | Ikke offentlig dokumentert i denne arbeidsøkten utover selskapsformen | - |

## Lenke til dokumentasjon
- FINT Flyt hos Novari: https://novari.no/tjenester/fint-flyt/
- Novari, tjenesteoversikt: https://novari.no/tjenester/
- FINT Arkiv hos Novari: https://novari.no/tjenester/fint-arkiv/

## Kildegrunnlag brukt i utfyllingen
- Novari IKS, FINT Flyt, hentet 25. september 2026.
- Novari IKS, tjenesteoversikt med FINT Arkivintegrasjoner, hentet 25. september 2026.
- Lokale kilder: `arkitektur/ressurser/produktnummerering.md`, `arkitektur/ressurser/operative-losninger-og-tjenester/71-FINT-Arkiv-v1-codex.md`, `arkitektur/kapabiliteter/capabilities.yaml`, `arkitektur/prinsipper/principles.md`, `sources/links.md`.
