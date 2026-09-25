# Fiks protokoll

## Navn
Fiks protokoll

## Ressurs ID
KS-013

## Status/Livsfase
**Produksjon** - i drift med flere ferdige grensesnitt, samtidig som enkelte deler er utsatt eller bare delvis i produksjon.

**Fakta:** KS Digital oppgir status per grensesnitt: `Fiks arkiv` er ferdigstilt og klart, `Fiks matrikkelføring` er i produksjon, `Kostra-rapportering barnevern` er i produksjon, `Fiks plan` er delvis i produksjon, og `Fiks politisk behandling` er utsatt til tredje kvartal 2026 i påvente av at `Fiks arkiv` og `Fiks plan` blir ferdige.

**Deduksjon:** Ressursen er ikke ett produkt med én livsfase, men en familie av grensesnitt med hver sin status. En vurdering av bruk må derfor gjøres per grensesnitt, ikke for Fiks protokoll som helhet.

## Modenhet
**Moden som mønster, ujevn per grensesnitt.**

- Teknisk: mønsteret bygger på asynkron meldingsutveksling med ende-til-ende-kryptering, og samhandlingen styres gjennom Fiks-konfigurasjonen.
- Funksjonelt: tre av fem grensesnitt er i produksjon eller ferdigstilt, ett er delvis i produksjon, og ett er utsatt.
- Organisatorisk: modellen forutsetter at kommunen har hovedavtale med KS, og at leverandørene på begge sider har implementert det aktuelle grensesnittet.
- Markedsmessig: hele poenget er leverandøruavhengighet, men gevinsten oppstår først når flere leverandører faktisk har implementert samme grensesnitt.

**Deduksjon:** Det svakeste leddet er leverandørdekningen. Et standardisert grensesnitt gir ingen verdi før både fagsystemet og sak- og arkivsystemet støtter det. For en kommune er spørsmålet derfor ikke om Fiks protokoll finnes, men om begge dens leverandører har tatt i bruk det grensesnittet den trenger.

## Kort beskrivelse
Fiks protokoll er samlingen av standardiserte grensesnitt for samhandling mellom kommunale systemer på Fiks-plattformen. Der `Fiks melding` er selve transporten, er Fiks protokoll avtalen om hva som utveksles: hvilke meldinger som finnes, hva de inneholder, og hvordan et samhandlingsløp henger sammen.

Merk at navnet lett misforstås. Fiks protokoll er ikke møteprotokoller eller saksdokumenter for politiske organer; `Fiks politisk behandling` er bare ett av grensesnittene i familien. De andre dekker arkiv, matrikkelføring, plan og Kostra-rapportering for barnevern.

Formålet er leverandøruavhengighet. En kommune skal kunne kombinere fagsystem fra én leverandør med sak- og arkivsystem fra en annen, uten at det krever en egen integrasjon mellom nettopp de to produktene.

## Kapabiliteter
- **Standardisering: Forvaltningsstandarder**
  Fiks protokoll definerer og forvalter de felles grensesnittene som kommunal sektor faktisk utveksler etter, og gjør dem tilgjengelige for leverandørene. Uten denne ressursen ville hver leverandørkobling vært en egen avtale.

- **Tjenesteutvikling: Integrerbare tjenester**
  Grensesnittene er standardiserte og maskinlesbare, slik at et fagsystem kan oppdage og integrere mot arkiv, matrikkel eller plan uten å kjenne det enkelte produktet på motsatt side.

Koblingene er satt fordi ressursen selv eier grensesnittene og standardiseringen. Selve meldingsutvekslingen og sikringen av den leveres av `Fiks melding` og `Fiks-plattformen`, og de evnene hører hos dem. Avhengigheten er beskrevet under `Gjenbruk`.

## Produktmål
**Dokumenterte mål**, slik KS Digital beskriver tjenesten:
- Lette samspillet mellom ulike kommunale systemer og muliggjøre sikker datautveksling mellom dem.
- Gi standardisert kommunikasjon mellom systemer i kommunene.
- Gi kommunen fleksibilitet til å kombinere systemer fra forskjellige leverandører.
- Gi kontroll over samhandlingsprosessene gjennom Fiks-konfigurasjonen.

**Utledede operative mål:**
- Redusere antall punkt-til-punkt-integrasjoner en kommune må bestille og vedlikeholde.
- Gjøre leverandørbytte mulig uten at motpartssystemene må bygges om.

## Brukerbehov
- Kommuner trenger å kombinere fagsystem og sak- og arkivsystem fra ulike leverandører uten å betale for en egen integrasjon per kombinasjon.
- Saksbehandlere trenger at dokumenter havner i arkivet automatisk, uten manuell overføring mellom systemer.
- Leverandører trenger ett definert grensesnitt å implementere mot, framfor et sett kundespesifikke tilpasninger.
- Kommunens IKT-miljø trenger oversikt og kontroll over hvilke samhandlingsløp som er aktive.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Sømløs integrasjon mellom egne fagsystemer | Arkiv, matrikkel, plan, barnevernsrapportering | Målgruppen KS Digital oppgir |
| Leverandører av fagsystemer | Ett grensesnitt mot mange kommuner | Produktutvikling | Må implementere det aktuelle grensesnittet |
| Leverandører av sak- og arkivsystemer | Standardisert mottak fra mange fagsystemer | Noark-arkiv | `Fiks arkiv` er ferdigstilt |
| Kommunens IKT-forvaltning | Styre og følge opp samhandlingsløp | Fiks-konfigurasjonen | Konfigurasjon er en egen forvaltningsoppgave |
| KS Digital | Forvalte og videreutvikle grensesnittene | Standardisering | Eier ressursen |

## Hovedfunksjoner
Den første hovedfunksjonen er **standardiserte grensesnitt per domene**. Fiks protokoll består av flere adskilte standarder. `Fiks arkiv` dekker kommunikasjon mot Noark-arkiv og er ferdigstilt. `Fiks matrikkelføring` dekker overføring av matrikkeldata og er i produksjon. `Fiks plan` er en modernisering av kommunikasjonen mot planregister og er delvis i produksjon. `Kostra-rapportering barnevern` er i produksjon som nasjonalt informasjonssystem. `Fiks politisk behandling` er grensesnittet for saksbehandling i politiske organer, og er foreløpig utsatt til tredje kvartal 2026.

Den andre er **asynkron og sikret utveksling**. Meldingene utveksles asynkront med ende-til-ende-kryptering. Asynkroniteten er en viktig egenskap for den som skal bygge på ressursen: mottakersystemet trenger ikke være tilgjengelig i samme øyeblikk som avsenderen sender, og et samhandlingsløp kan gå over tid.

Den tredje er **styring gjennom Fiks-konfigurasjonen**. Kommunen styrer selv hvilke samhandlingsprosesser som er aktive, og mellom hvilke systemer. Dette er en operativ forvaltningsflate, ikke bare en teknisk innstilling, og den er kommunens kontrollpunkt over hva som faktisk utveksles.

Den fjerde er **leverandørnøytralitet i praksis**. Fordi begge sider forholder seg til grensesnittet framfor til hverandre, kan kommunen bytte ut ett system uten å bygge om det andre. Dette er den egenskapen som begrunner hele ressursen, og som samtidig gjør den avhengig av at leverandørene faktisk implementerer grensesnittet.

### Typiske brukssituasjoner (generisk)
- En kommune skal koble et fagsystem til sitt Noark-arkiv uten en leverandørspesifikk integrasjon.
- En kommune skal overføre matrikkeldata fra et fagsystem til matrikkelen.
- En kommune skal modernisere kommunikasjonen mot planregisteret.
- En kommune vurderer å bytte sak- og arkivsystem og vil vite hva det gjør med eksisterende integrasjoner.

### Når Fiks protokoll normalt ikke er førstevalg
- Når behovet er ren utsending av post til innbyggere eller virksomheter. Da er `Fiks SvarUt` riktig tjeneste.
- Når behovet er mottak av inngående post. Da er `SvarInn` riktig tjeneste.
- Når behovet er generell meldingsutveksling uten et definert domenegrensesnitt. Da er `Fiks melding` det riktige nivået.
- Når behovet er oppslag i et register. Da hører løsningen hos `Fiks register` og de tilhørende registertjenestene.
- Når det aktuelle grensesnittet ikke er ferdig. `Fiks politisk behandling` er utsatt til tredje kvartal 2026, og bør ikke legges til grunn i planer før det.

### Scope og avgrensning
Inngår: standardiserte grensesnitt for arkiv, matrikkelføring, plan, Kostra-rapportering barnevern og politisk behandling, samt konfigurasjonen som styrer hvilke samhandlingsprosesser som er aktive.

Inngår ikke: transporten, som leveres av `Fiks melding`; plattformen og driften, som leveres av `Fiks-plattformen`; selve fagsystemene og arkivsystemene; og innholdet i dokumentene som utveksles.

Avgrensningen mot navnet er verdt å skrive ut: `Fiks politisk behandling` dekker saks- og møtestøtte for politiske organer, mens Fiks protokoll som helhet dekker langt mer enn det.

## Veikart over kommende funksjonalitet
**Fakta:** `Fiks politisk behandling` er utsatt til tredje kvartal 2026, og utsettelsen er begrunnet med at både `Fiks arkiv` og `Fiks plan` må ferdigstilles først. KS anbefaler at `Fiks politisk behandling` brukes sammen med `Fiks arkiv`, fordi de to grensesnittene til sammen dekker behovet når fagsystem og sak- og arkivsystem kommer fra ulike leverandører.

**Fakta:** `Fiks plan` er delvis i produksjon, og er dermed under aktiv utrulling.

**Ikke offentlig dokumentert i denne arbeidsøkten:** om flere domenegrensesnitt er planlagt utover de fem som er beskrevet.

## Forretningsverdi/Verdiforslag
**For kommuner:** færre integrasjoner å bestille, betale for og vedlikeholde, og reell mulighet til å velge beste system per fagområde framfor å kjøpe alt fra én leverandør.

**For leverandører:** ett grensesnitt å implementere gir tilgang til hele kommunemarkedet, og reduserer kostnaden ved kundespesifikke tilpasninger.

**For saksbehandlere:** dokumenter og saksopplysninger flyter mellom systemer uten manuell overføring, som både sparer tid og reduserer risikoen for at noe ikke blir arkivert.

**For sektoren:** standardiserte grensesnitt gjør at erfaring og løsninger kan gjenbrukes mellom kommuner, og reduserer den samlede integrasjonskostnaden i kommunal sektor.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Leverandør | Gevinsten uteblir hvis leverandørene på begge sider ikke har implementert grensesnittet | Kontroller leverandørstøtte for det konkrete grensesnittet før løsningen planlegges |
| Tidsplan | `Fiks politisk behandling` er utsatt til tredje kvartal 2026 | Ikke legg grensesnittet til grunn i planer før det er i produksjon |
| Avhengighet | `Fiks politisk behandling` forutsetter at `Fiks arkiv` og `Fiks plan` er ferdige | Rekkefølgen er styrt av KS Digital og kan ikke påvirkes lokalt |
| Økonomi | Kostnaden består av engangsbetaling til Digifin og løpende fakturering fra KS, i tillegg til leverandørenes egne priser | Tre kostnadselementer må med i budsjettet, ikke bare KS-prisen |
| Organisatorisk | Fiks-konfigurasjonen må forvaltes aktivt i kommunen | Uavklart hvem som eier oppgaven i små kommuner |
| Navn | Navnet gir feil forventning om at ressursen gjelder politiske protokoller | Skriv ut avgrensningen når ressursen omtales i analyser |

## Kanaler
Fiks protokoll er en maskinell integrasjonsflate. Systemene utveksler meldinger asynkront gjennom Fiks-plattformen, og det finnes ingen egen brukerflate for sluttbrukere.

Ved siden av den maskinelle kanalen finnes en forvaltningsflate: Fiks-konfigurasjonen, der kommunen styrer hvilke samhandlingsprosesser som er aktive. Bestilling og tilgang forutsetter at kommunen har hovedavtale med KS.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** driftsmodell og plattformvalg. Det som er kjent, er at Fiks protokoll er en del av Fiks-plattformen, som driftes av KS Digital, og at kommunen ikke drifter noe selv utover sine egne systemer.

## Gjenbruk
Ressursen er i sin helhet et gjenbruksgrep: standardiserte grensesnitt gjør at samme integrasjon fungerer på tvers av kommuner og leverandører. En leverandør som implementerer `Fiks arkiv` én gang, kan levere til alle kommuner som bruker plattformen.

Avhengigheter som ikke er kapabiliteter her: `Fiks melding` leverer meldingsutvekslingen og sikringen av den, og `Fiks-plattformen` leverer plattform, drift og tilgangsmodell.

**Vanlige kombinasjoner med andre produkter:**
- `Fiks-plattformen` og `Fiks melding` som det underliggende laget.
- `Fiks SvarUt` og `SvarInn` for post ut og inn, som dekker et annet behov enn systemintegrasjon.
- Noark-baserte sak- og arkivsystemer i kommunen, som er motparten for `Fiks arkiv`.
- `FINT Arkivintegrasjoner` som den fylkeskommunale parallellen til det samme behovet.

**Kildekode:** Ikke offentlig dokumentert. Kildene i denne arbeidsøkten sier ikke om grensesnittspesifikasjonene eller implementasjonene er publisert som åpen kildekode.

**Lisens:** Ikke offentlig dokumentert.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger**
  Felles grensesnitt gjør at samme integrasjon gjenbrukes på tvers av alle kommuner framfor å bygges per kunde.
- **P6: Lag digitale løsninger som støtter samhandling**
  Hele ressursen finnes for at systemer fra ulike leverandører skal kunne samhandle.
- **P4: Del og gjenbruk data**
  Standardiserte grensesnitt for arkiv, matrikkel og plan gjør at data flyter mellom systemer framfor å legges inn på nytt.
- **P2: Ta arkitekturbeslutninger på rett nivå**
  Støttes ved at grensesnittet besluttes i sektoren, mens den enkelte kommunen velger systemer fritt innenfor det.

**Spenning og begrensning:** Ressursen støtter **P1: Ta utgangspunkt i brukernes behov** bare indirekte; den er infrastruktur, og brukernytten realiseres i fagsystemene. Den har også en reell spenning mot **P5** i praksis: standardisert gjenbruk forutsetter at markedet følger etter, og et grensesnitt uten leverandørstøtte gir kommunen en standard den ikke kan bruke. Den viktigste begrensningen ved vurdering av bruk er derfor ikke arkitektonisk, men markedsmessig, og bør avklares med begge leverandørene før et løp planlegges.

## Finansiering
**Fakta:** KS Digital oppgir at kommunen må ha hovedavtale, og at kostnaden består av en engangsbetaling til Digifin og løpende fakturering fra KS. Leverandørene kan i tillegg belaste for sine egne produkter.

**Deduksjon:** Modellen er en kombinasjon av felles finansiering gjennom Digifin og brukerbetaling fra den enkelte kommunen. Kildene i denne arbeidsøkten oppgir ikke satser.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital, formelt KS-Digitale Fellestjenester AS | KS Digitals tjenesteside for Fiks protokoll |
| Driftsansvar | KS Digital, som del av Fiks-plattformen | Samme |
| Budsjettansvar | Delt: Digifin ved engangsbetaling, KS ved løpende fakturering, kommunen ved leverandørkostnader | KS Digitals omtale av pris og avtale |
| Implementering i systemene | Den enkelte leverandøren | Følger av at grensesnittene er standarder, ikke ferdige koblinger |
| Styringsmodell | Ikke offentlig dokumentert i denne arbeidsøkten | - |

## Lenke til dokumentasjon
- Fiks protokoll hos KS Digital: https://ksdigital.no/tjenestene/fiks-protokoll/
- KS om Fiks politisk behandling: https://www.ks.no/fagomrader/digitalisering/felleslosninger/verktoykasse-plan--og-byggesak/verktoy/sammenhengende-tjenester---integrasjoner/fiks-politisk-behandling/
- KS Digital, tjenesteoversikt: https://ksdigital.no/tjenestene/

## Kildegrunnlag brukt i utfyllingen
- KS Digital, Fiks protokoll, hentet 25. september 2026.
- KS, Fiks politisk behandling, hentet 25. september 2026.
- Lokale kilder: `arkitektur/ressurser/produktnummerering.md`, `arkitektur/ressurser/operative-losninger-og-tjenester/26-FIKS-Melding-produkt-canvas-v3-claude.md`, `arkitektur/kapabiliteter/capabilities.yaml`, `arkitektur/prinsipper/principles.md`, `sources/links.md`.
