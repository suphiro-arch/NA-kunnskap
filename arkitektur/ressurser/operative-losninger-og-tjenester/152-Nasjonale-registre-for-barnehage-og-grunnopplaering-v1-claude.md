# Produkt-canvas: Nasjonale registre for barnehage og grunnopplæring

## Navn
Nasjonale registre for barnehage og grunnopplæring

## Ressurs ID
UDIR-002

## Status/Livsfase
**Produksjon** — etablert registerfamilie i drift hos Utdanningsdirektoratet, med åpne REST-API-er per register.

**Fakta:** Utdanningsdirektoratet tilbyr REST-API med data fra seks nasjonale registre. `NSR` ligger på `data-nsr.udir.no/v3` og `NBR` på `data-nbr.udir.no/v3`, og begge er åpne uten autentisering. Registeret for lærebedrifter krever nøkkel.

## Modenhet
**Høy modenhet** — registrene er i operativ bruk som autoritativt grunnlag for hvilke barnehager, skoler og tilhørende virksomheter som finnes.

- Hvert register har eget versjonert REST-endepunkt med Swagger- og OpenAPI-dokumentasjon.
- Datasettene er publisert i Felles datakatalog og lisensiert under Norsk lisens for offentlige data.
- Registrene bygger på Enhetsregisteret framfor på egne virksomhetslister, og legger til opplysninger som Enhetsregisteret ikke har.
- Utdanningsdirektoratet opplyser at `GSI` får ny teknisk løsning før datainnsamlingen høsten 2026, noe som tyder på pågående modernisering i det omkringliggende systemlandskapet.

**Deduksjon:** Modenheten er høy som datakilde. Brukskvaliteten for den enkelte konsumenten avhenger likevel av at ulike registre i familien har ulik tilgangsmodell, siden ett av dem krever nøkkel og resten er åpne.

## Kort beskrivelse
Nasjonale registre for barnehage og grunnopplæring er Utdanningsdirektoratets familie av autoritative registre over virksomhetene i barnehage- og skolesektoren. Familien består av Nasjonalt barnehageregister, Nasjonalt skoleregister, Nasjonalt register for opplæringskontorer, Register for lærebedrifter, Nasjonalt register for PP-tjenester og Nasjonalt register for skolefritidsordningen.

Registrene svarer på hvilke barnehager, skoler, opplæringskontorer, lærebedrifter, PP-tjenester og skolefritidsordninger som finnes, hvem som eier dem, og hvor de hører hjemme geografisk og administrativt. Grunnlaget er Enhetsregisteret, supplert med opplysninger som er spesifikke for sektoren.

Registerfamilien beskriver hvor opplæringen skjer og hvem som har ansvaret, mens `Grep` (`UDIR-001`) beskriver hva som læres. Sammen utgjør de grunndatalaget som resten av sektorens løsninger bygger på.

## Kapabiliteter
- **Datakilder: Grunndata**
  Registrene er den autoritative kilden til hvilke barnehager, skoler og tilhørende virksomheter som finnes, med eier- og ansvarsforhold.
- **Datautveksling og integrasjon: Dele data med andre**
  Hvert register eksponeres som eget versjonert REST-API som andre virksomheter og leverandører konsumerer direkte.
- **Datakilder: Åpne data**
  Datasettene er lisensiert under Norsk lisens for offentlige data, og de fleste registrene er tilgjengelige uten autentisering.

## Produktmål
Dokumenterte mål:
- Gjøre data om barnehager, skoler og tilhørende virksomheter tilgjengelig for viderebruk gjennom åpne API-er.
- Supplere Enhetsregisteret med de opplysningene sektoren trenger, framfor at hver aktør bygger egne virksomhetslister.
- Tilby felles geografiske oppslag for fylke, kommune, bydel, postnummer og KOSTRA-gruppe gjennom en delt tjeneste i registerfamilien.

Operative mål utledet fra kildene:
- Redusere dobbeltregistrering av virksomhetsopplysninger i utdanningssektoren.
- Gi statistikk-, tilsyns- og forvaltningsmiljøer et felles og oppdatert virksomhetsgrunnlag.
- Gjøre det mulig for nettsteder og fagsystemer å presentere korrekte opplysninger om barnehager og skoler.

## Brukerbehov
- Skoleeiere og barnehagemyndigheter trenger et oppdatert bilde av virksomhetene de har ansvar for.
- Leverandører av fagsystemer trenger en autoritativ virksomhetsliste framfor å vedlikeholde egne.
- Statistikk- og analysemiljøer trenger stabile virksomhetsidentifikatorer over tid.
- Foresatte og elever trenger korrekte opplysninger om barnehager og skoler i tjenester som presenterer dem.
- Fylkeskommunene trenger oversikt over godkjente opplæringskontorer og lærebedrifter i fagopplæringen.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Utdanningsdirektoratet | Felles virksomhetsgrunnlag for egen forvaltning | Statistikk, tilsyn og datainnsamling | Både forvalter og konsument |
| Kommuner som barnehagemyndighet | Oversikt over barnehager og eierforhold | Tilsyn, tilskudd og forvaltning | `NBR` er den sentrale flaten |
| Skoleeiere i kommune og fylkeskommune | Oversikt over egne og andres skoler | Planlegging, rapportering og samhandling | `NSR` dekker også norske skoler i utlandet |
| Fylkeskommunene og Novari | Godkjente opplæringskontorer og lærebedrifter | Fagopplæring og inntak | `NOR` og `NLR` hentes fra VIGO |
| Leverandører av fagsystemer | Maskinlesbar virksomhetsliste | Integrasjon i skole- og barnehagesystemer | Åpne API-er uten autentisering for de fleste registrene |
| Statistikk- og forskningsmiljøer | Stabile identifikatorer og historikk | Sammenstilling og tidsserier | NLOD-lisens gir vid gjenbruksrett |
| PP-tjenesten og SFO-sektoren | Oversikt over egne virksomheter | Forvaltning og samhandling | `NPR` og `NFR` er de smaleste registrene i familien |

## Hovedfunksjoner
### Primære funksjoner
Kjernefunksjonen er å gjøre virksomhetsdata i barnehage- og grunnopplæringssektoren tilgjengelig som maskinlesbare, autoritative registre. Hvert av de seks registrene har eget REST-endepunkt, og konsumenten henter opplysninger om virksomheter og deres eiere derfra framfor å bygge og vedlikeholde egne lister.

Registrene er ikke selvstendige virksomhetsregistre. De bygger på Enhetsregisteret og legger til det sektoren trenger utover det. `NSR` viser enheter i Enhetsregisteret som hører til grunnopplæringen, og tar i tillegg med norske skoler i utlandet som ikke finnes der. `NBR` viser enheter registrert med næringskode 88.911 Barnehager, og supplerer med opplysninger fra `BASIL`, rapporteringssystemet for barnehager. Denne lagdelingen er viktig å forstå: den autoritative kilden til at en virksomhet finnes, er Enhetsregisteret, mens den autoritative kilden til at den er en barnehage eller skole med bestemte sektoregenskaper, er disse registrene.

To av registrene har en annen opprinnelse. `NOR` inneholder godkjente opplæringskontorer og `NLR` godkjente lærebedrifter med løpende kontrakter, og begge hentes fra VIGO. Det betyr at fagopplæringsdelen av registerfamilien i praksis er en nasjonal publisering av fylkeskommunale data, ikke data Utdanningsdirektoratet selv fører.

Familien har også en delt geografitjeneste som dekker fylke, kommune, bydel, postnummer og KOSTRA-gruppe. Den gjør at konsumenter kan slå opp administrativ og geografisk tilhørighet i samme løp som virksomhetsdataene, framfor å kombinere med en separat kilde.

### Typiske brukssituasjoner (generisk)
- Når et fagsystem trenger en oppdatert liste over skoler eller barnehager med organisasjonsnummer og eierforhold.
- Når en kommune som barnehagemyndighet skal ha oversikt over barnehagene den har tilsynsansvar for.
- Når en fylkeskommune skal kontrollere om en lærebedrift er godkjent og har løpende kontrakter.
- Når statistikk skal grupperes på fylke, kommune, bydel eller KOSTRA-gruppe.
- Når et nettsted skal presentere korrekte opplysninger om en barnehage eller skole til foresatte.
- Når norske skoler i utlandet må med i oversikten, siden de ikke ligger i Enhetsregisteret.

### Når Nasjonale registre for barnehage og grunnopplæring normalt ikke er førstevalg
- Når behovet er generelle virksomhetsopplysninger uten sektorkontekst. Da er `Enhetsregisteret` (`BRREG-003`) den riktige kilden.
- Når behovet gjelder fag, læreplaner eller opplæringstilbud. Det dekkes av `Grep` (`UDIR-001`).
- Når behovet gjelder den enkelte eleven, barnet eller ansatte. Registrene inneholder virksomheter, ikke personer.
- Når behovet gjelder statistikk om aktivitet framfor virksomhetsopplysninger. Da er statistikkbanken og `GSI` mer relevante.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Seks nasjonale registre over virksomheter i barnehage- og grunnopplæringssektoren | Personopplysninger om barn, elever, lærlinger eller ansatte |
| Supplerende sektoropplysninger utover Enhetsregisteret | Rollen som autoritativ kilde til at en virksomhet eksisterer, som ligger i Enhetsregisteret |
| Norske skoler i utlandet, som mangler i Enhetsregisteret | Fag, læreplaner og opplæringstilbud, som ligger i Grep |
| Delt geografitjeneste for fylke, kommune, bydel, postnummer og KOSTRA-gruppe | Aktivitets- og resultatstatistikk, som ligger i statistikkbanken og GSI |
| Åpne REST-API-er per register, i hovedsak uten autentisering | Godkjenningsvedtakene selv for lærebedrifter og opplæringskontorer, som fattes i fylkeskommunen |

## Veikart over kommende funksjonalitet
Kildene beskriver ikke et samlet veikart for registerfamilien. Utdanningsdirektoratet opplyser at `GSI` får ny teknisk løsning før datainnsamlingen høsten 2026. `GSI` er et tilgrensende system og ikke del av denne registerfamilien, så konsekvensen for registrene er ikke dokumentert.

## Forretningsverdi/Verdiforslag
- For sektoren: ett felles og oppdatert virksomhetsgrunnlag framfor mange lokale lister som må vedlikeholdes hver for seg.
- For kommuner og fylkeskommuner: lavere kostnad ved forvaltning, tilsyn og rapportering fordi virksomhetsopplysningene er tilgjengelige maskinelt.
- For leverandører: et åpent og dokumentert integrasjonspunkt som kan gjenbrukes på tvers av kunder.
- For statistikk og forskning: stabile identifikatorer og NLOD-lisens som gir vid gjenbruksrett.
- For innbyggere: korrekte opplysninger om barnehager og skoler i de tjenestene de faktisk bruker.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Avhengigheter | Registrene bygger på Enhetsregisteret, og feil eller forsinkelser der forplanter seg | Forstå lagdelingen og melde feil til rett kilde framfor å korrigere lokalt |
| Avhengigheter | `NOR` og `NLR` hentes fra VIGO, slik at nasjonal publisering avhenger av fylkeskommunal registreringspraksis | Tydelig ansvarsdeling mellom Novari, fylkeskommunene og Utdanningsdirektoratet |
| Tilgangsmodell | Registeret for lærebedrifter krever nøkkel, mens de øvrige er åpne | Dokumentere den ulike tilgangsmodellen i integrasjonsarbeidet framfor å anta at hele familien er åpen |
| Datakvalitet | Barnehageopplysninger suppleres fra `BASIL`, som er et rapporteringssystem med egne frister | Kontrollere aktualitet ved bruk i tidskritiske sammenhenger |
| Avgrensning | Familien består av seks registre med ulik bredde og ulik brukergruppe | Beskrive hvilket register som faktisk dekker behovet, framfor å vise til familien samlet |

## Kanaler
- https://www.udir.no/om-udir/data/nxr/
- https://data-nsr.udir.no/v3
- https://data-nbr.udir.no/v3
- https://www.udir.no/om-udir/data/

## Plattform
Åpne REST-API-er per register, med egne versjonerte endepunkter og Swagger- og OpenAPI-dokumentasjon. Datasettene er publisert i Felles datakatalog.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme registerdata brukes av statlige myndigheter, kommuner, fylkeskommuner, leverandører og forskningsmiljøer.
- Gjenbruksverdien ligger i at registrene er autoritative og åpent tilgjengelige, slik at ingen konsument trenger å bygge egen virksomhetsliste.
- NLOD-lisensen gir vid rett til viderebruk, også kommersielt.
- Gjenbruket gjelder virksomhetsdataene, ikke fagsystemfunksjonalitet.

**Vanlige kombinasjoner med andre produkter:**
- `Enhetsregisteret` (`BRREG-003`) er grunnlaget registrene bygger på.
- `Grep` (`UDIR-001`) for fag, læreplaner og opplæringstilbud, som utfyller virksomhetsdataene.
- `VIGO` (`NOVARI-004`) er kilden til opplysningene om opplæringskontorer og lærebedrifter.
- `Felles datakatalog` (`DIGDIR-011`) der datasettene er beskrevet og gjort finnbare.
- `Maskinporten` (`DIGDIR-002`) er relevant der en konsument trenger autentisert maskinell tilgang. Kildene beskriver ikke Maskinporten som del av tilgangsmodellen, så dette er en vurdering og ikke dokumentert praksis.

**Kildekode:** Ikke offentlig dokumentert. Selve registerløsningene er ikke publisert, men Utdanningsdirektoratet publiserer teknisk dokumentasjon og kode for tilgrensende dataressurser på [github.com/Utdanningsdirektoratet](https://github.com/Utdanningsdirektoratet).

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Direkte og sterk støtte. Registrene er åpne, autoritative og lisensiert for viderebruk under NLOD.
- **P5: Del og gjenbruk løsninger**
  Støttes indirekte. Det som gjenbrukes er data og integrasjonsmønster, ikke løsningskomponenter.
- **P6: Lag digitale løsninger som støtter samhandling**
  Felles virksomhetsidentifikatorer på tvers av stat, kommune og fylkeskommune er en forutsetning for samhandling i sektoren.
- **P2: Ta arkitekturbeslutninger på rett nivå**
  Registrene bygger videre på Enhetsregisteret framfor å etablere en parallell virksomhetskilde, og legger bare til det sektoren faktisk trenger.

Spenning og begrensning: familien har ulik tilgangsmodell mellom registrene, og to av registrene er nasjonal publisering av fylkeskommunale data. Det gir en delt ansvarslinje som ikke er synlig fra API-et alene, og som bør forstås før registrene brukes som fasit i tilsyn eller rapportering.

## Finansiering
Kildene beskriver ingen egen finansieringsmodell eller vederlag for bruk. Registrene tilbys som åpne data under NLOD, og forvaltningen inngår i Utdanningsdirektoratets ordinære virksomhet.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Registerforvaltning og API-drift | Utdanningsdirektoratet | udir.no og API-dokumentasjonen |
| Autoritativ virksomhetskilde | Brønnøysundregistrene gjennom Enhetsregisteret | NSR og NBR bygger på Enhetsregisteret |
| Godkjenning av lærebedrifter og opplæringskontorer | Fylkeskommunene, med VIGO som system | NOR og NLR hentes fra VIGO |
| Barnehagerapportering | Kommunene, gjennom BASIL | NBR suppleres med BASIL-opplysninger |

## Lenke til dokumentasjon
- https://www.udir.no/om-udir/data/nxr/
- https://www.udir.no/om-udir/data/
- https://data-nsr.udir.no/v3
- https://data-nbr.udir.no/v3

## Kildegrunnlag brukt i utfyllingen
- https://www.udir.no/om-udir/data/nxr/, kontrollert 2026-09-07
- https://www.udir.no/om-udir/data/, kontrollert 2026-09-07
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-07
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-07
- `arkitektur/ressurser/styringsregler.md`, kontrollert 2026-09-07
