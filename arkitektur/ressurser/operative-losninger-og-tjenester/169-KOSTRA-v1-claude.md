# KOSTRA

## Navn
KOSTRA – Kommune-Stat-Rapportering

## Ressurs ID
SSB-002

## Status/Livsfase
**Produksjon** – årlig rapporterings- og publiseringsløp i ordinær drift.

**Fakta:** KOSTRA-forskriften (FOR-2019-10-18-1412) gjelder fra 1. januar 2020 og er fastsatt av Kommunal- og distriktsdepartementet med hjemmel i kommuneloven § 16-1 og IKS-loven § 42. SSB publiserte sist KOSTRA-tall 15. juni 2026, og neste publisering er varslet til 15. mars 2027.

**Fakta:** For rapporteringsåret 2026 åpner portalen for rapportering 1. desember 2026, med testperiode 2.–20. november, frist for regnskapsfiler 22. februar 2027 og foreløpige tall 15. mars 2027.

## Modenhet
**Høy modenhet som rapporterings- og statistikksystem, middels modenhet som moderne datadelingsløsning.**

- Rapporteringsplikten, fristene og regnskapsstrukturen er forskriftsfestet, med vedlegg som fastsetter arter, funksjoner og balanseposter (Lovdata).
- Rapporteringen har et fast årshjul med test, innsending, kontroll, foreløpig publisering og revidert publisering (SSB, innrapporteringssiden).
- Data kontrolleres maskinelt før innsending med SSBs kontrollprogram, som er publisert som åpen kildekode og vedlikeholdes aktivt (GitHub, siste endring oktober 2026).
- Styringen er etablert med Samordningsrådet for KOSTRA og faste arbeidsgrupper per tjenesteområde (SSB).
- Innsendingen er fortsatt i hovedsak skjema- og filbasert. SSB flytter skjemaer gradvis til Altinn, men for 2026 gjelder det bare to skjemaer (SSB, innrapporteringssiden).

**Deduksjon:** Det svakeste leddet er innsamlingsmønsteret. Rapporteringen er periodisk og bygger på uttrekk og skjemaer, ikke på løpende maskinell deling fra kommunenes fagsystemer. Unntaket er barnevern, der rapporteringen er flyttet til `BUFDIR-001` Barnevernsregisteret med automatisk overføring for kommuner med nye fagsystemer. Den som vurderer KOSTRA som grunnlag for tettere eller hyppigere oppfølging, må regne med årsrytmen.

## Kort beskrivelse
KOSTRA er det nasjonale systemet for rapportering av styringsinformasjon fra kommuner og fylkeskommuner til staten. Kommunesektoren rapporterer tjenestedata, ressursbruk og regnskap til Statistisk sentralbyrå (SSB) hvert år. SSB kontrollerer dataene, sammenstiller dem med befolkningsdata og publiserer nøkkeltall som gjør det mulig å sammenligne kommuner over tid og på tvers av tjenesteområder.

Tallene brukes både lokalt og nasjonalt: kommunene bruker dem til egen styring og sammenligning, departementene til oppfølging av sektorpolitikk, og de er åpent tilgjengelige for alle i Statistikkbanken. KDD formulerer et sentralt mål som at data skal rapporteres én gang, men kunne brukes flere ganger til ulike formål.

KOSTRA er både en rapporteringskanal, et felles klassifikasjons- og kontrollregime for kommunale data og en publiseringsflate for statistikk. Ressursen omfatter ikke de enkelte fagregistrene som mottar data fra kommunene på egne hjemler.

## Kapabiliteter
KOSTRA realiserer evnen til å gjøre kommunale data sammenlignbare og åpent tilgjengelige på tvers av alle kommuner. Forsvant KOSTRA, ville ingen annen ressurs levert et felles, kontrollert og offentlig tallgrunnlag for kommunesektoren. Samordningsrådet er vurdert mot `Strategisk styring: Samordning`, men uttalelsene er rådgivende og bygger på konsensus, mens beslutningene ligger hos fagdepartementene. Det gir ikke det forpliktende mandatet kapabiliteten krever. Innsendingen bruker Altinn og ID-porten for deler av rapporteringen; det er avhengigheter, ikke egne kapabiliteter.

- **Datadrevet: Sammenstilling av data**
  KOSTRA henter tjeneste-, ressurs- og regnskapsdata fra alle kommuner og fylkeskommuner, kombinerer dem med befolkningsdata og foredler dem til nøkkeltall. Forskriftens felles kontoplan med arter og funksjoner gjør at regnskap fra ulike kommuner kan tolkes samlet, og resultatet er et helhetlig beslutningsgrunnlag for kommunene og departementene.

- **Datakilder: Åpne data**
  KOSTRA-tallene publiseres åpent i Statistikkbanken, ordnet etter tjenesteområde og kommune, med fast publiseringsplan i mars og juni. Dataene er tilgjengelige for innbyggere, forskere, presse og næringsliv uten tilgangskontroll, og kan hentes maskinelt gjennom SSBs API for statistikktabeller.

## Produktmål
**Fakta:** KDD beskriver KOSTRA som et nasjonalt informasjonssystem som skal gi styringsinformasjon om kommunal og fylkeskommunal virksomhet til beslutningstakere i kommunene, fylkeskommunene og staten. Et uttalt mål er å forenkle rapporteringen ved at data rapporteres én gang og brukes til flere formål.

**Fakta:** Samordningsrådet skal samordne rapporteringen av geografiske data, fagdata, personelldata og økonomi- og tjenestedata, med mål om felles strukturer, sammenlignbarhet mellom kommuner, effektiv datautveksling og forenklet rapportering (SSB).

**Deduksjon:** Et operativt mål er å holde rapporteringsbyrden nede samtidig som datakvaliteten er god nok til sammenligning. Det følger av at kontrollprogrammet skal fange feil før innsending, og at SSB etter forskriften § 3 kan avvise vesentlig feilaktige data.

## Brukerbehov
Staten trenger sammenlignbar informasjon om hvordan kommunene bruker ressursene og hva de leverer, for å følge opp sektorpolitikk, fordele midler og vurdere effekten av reformer. Kommunene trenger det samme grunnlaget for å sammenligne seg med andre og styre egen virksomhet.

Uten et felles system ville hvert departement og direktorat samlet inn egne data med egne definisjoner og frister, og kommunene ville rapportert det samme flere ganger i ulike formater. Tallene ville heller ikke vært sammenlignbare på tvers av kommuner.

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Oppfylle rapporteringsplikten, sammenligne seg med andre | Innsending av skjemaer og regnskapsfiler, bruk av nøkkeltall i egen styring | Rapporteringspliktige etter forskriften |
| Kommunale foretak, IKS, interkommunale politiske råd og oppgavefellesskap | Rapportere egen del av tjenesteproduksjon og regnskap | Innsending etter tildelte skjemaer | Omfattet av forskriften § 1 |
| Departementer og direktorater | Styringsdata for egen sektor | Oppfølging av sektorpolitikk, fastsetting av rapporteringskrav innen eget område | Fagdepartementene bestemmer innholdet i tjenesterapporteringen |
| KDD | Oversikt over kommuneøkonomi, forvaltning av forskriften | Kommuneøkonomi, inntektssystem, leder Samordningsrådet | Fastsetter forskriften |
| Forskere, presse og innbyggere | Åpne, sammenlignbare tall om kommunene | Analyse, journalistikk, innsyn | Bruker Statistikkbanken |
| Leverandører av kommunale fagsystemer | Lage korrekte filuttrekk | Integrasjon mot filformater og kontrollprogram | Kontrollprogrammet er åpent tilgjengelig |

## Hovedfunksjoner
Den første hovedfunksjonen er **innsamling av rapportering fra kommunesektoren**. Kommunene sender inn tjenestedata gjennom elektroniske skjemaer og regnskapsdata som filuttrekk fra egne økonomi- og fagsystemer. Hoveddelen går gjennom SSBs KOSTRA-portal. SSB flytter skjemaer gradvis til Altinn, og for 2026 gjelder det skjema 17 om ungdomsarbeid og støtte til frivillige organisasjoner og skjema 60 om lokale folkeavstemninger. Filuttrekk krypteres med SSBs eget verktøy før innsending. Forskriften fastsetter at rapporteringen skal skje elektronisk på den måten SSB bestemmer.

Den andre er **kontroll og retting før publisering**. Kommunene kjører filuttrekkene gjennom SSBs kontrollprogram, som sjekker at dataene er fullstendige og konsistente før de sendes inn. Etter innsending kan SSB avvise data som er vesentlig feil, og kommunene får en egen frist for å sende rettede tall mellom foreløpig og endelig publisering. Kontrollprogrammet er publisert som åpen kildekode, slik at leverandører kan bygge kontrollene inn i egne systemer.

Den tredje er **felles klassifisering av kommunale data**. Forskriften fastsetter en felles kontoplan med arter, funksjoner og balanseposter, og regnskapene rapporteres etter denne. Innholdet i tjenesterapporteringen fastsettes av fagdepartementene innen eget område, og SSB publiserer oversikt over hva som skal rapporteres. Arbeidsgruppene per tjenesteområde utvikler statistikken innenfor årlige mandater godkjent av Samordningsrådet.

Den fjerde er **sammenstilling og publisering**. SSB kombinerer de innrapporterte dataene med befolkningsdata og publiserer nøkkeltall og grunnlagsdata i Statistikkbanken. Foreløpige tall kommer 15. mars og reviderte tall 15. juni. Tallene er ordnet etter tjenesteområde og kan sammenlignes mellom kommuner og over tid.

Den femte er **samordning av rapporteringskrav**. Samordningsrådet for KOSTRA, ledet av KDD med SSB som sekretariat, behandler prinsipielle spørsmål om rapporteringen og avgir uttalelser til fagdepartementene. Brønnøysundregistrene forvalter Kommunalt rapporteringsregister (KOR), som gir oversikt over alle rapporteringsplikter kommunesektoren har til staten, og som beskrives som et verktøy for samordningsfunksjonene i KOSTRA.

### Typiske brukssituasjoner (generisk)
- sammenligne ressursbruk og tjenesteomfang mellom kommuner i samme kommunegruppe
- hente kommunale nøkkeltall som grunnlag for statlig styring, utredning eller evaluering av reformer
- vurdere om en ny statlig rapporteringsplikt overlapper data kommunene allerede rapporterer
- bygge analyser eller tjenester på åpne kommunedata gjennom Statistikkbanken

### Når KOSTRA normalt ikke er førstevalg
KOSTRA er ikke førstevalg når behovet er løpende eller hendelsesnær informasjon. Rapporteringen er årlig, med kvartalsvis rapportering bare for kommunekassens regnskap, og tallene publiseres måneder etter rapporteringsåret.

KOSTRA er heller ikke en kanal for data på individnivå eller for saksbehandling. Der staten trenger opplysninger om enkeltpersoner, går det gjennom egne registre med egne hjemler, slik barnevernsrapporteringen nå går gjennom `BUFDIR-001` Barnevernsregisteret.

For statistikk på mikrodata, der forskere trenger å koble kommunale data med andre registre, er `SSB-001` microdata.no mer relevant.

### Scope og avgrensning
Inngår:
- rapporteringsplikten etter KOSTRA-forskriften for kommuner, fylkeskommuner, kommunale foretak, IKS, interkommunale politiske råd og kommunale oppgavefellesskap
- innsending gjennom KOSTRA-portalen, Altinn og filuttrekk
- kontrollprogram, kontroll og retting
- publisering av nøkkeltall og grunnlagsdata i Statistikkbanken
- Samordningsrådet og arbeidsgruppene som styringsstruktur

Inngår ikke:
- fagregistre som mottar kommunale data på egne hjemler, som Barnevernsregisteret og de nasjonale registrene for barnehage og grunnopplæring
- Kommunalt rapporteringsregister, som forvaltes av Brønnøysundregistrene
- statistikk utenfor KOSTRA som SSB produserer om kommunesektoren

## Veikart over kommende funksjonalitet
**Fakta:** SSB flytter KOSTRA-skjemaer gradvis til Altinn. For rapporteringsåret 2026 gjelder det skjema 17 og 60.

**Fakta:** Barnevernsrapporteringen er flyttet ut av de ordinære KOSTRA-skjemaene for kommuner som er fullt over på Barnevernsregisteret, og KS Digital oppgir `Kostra-rapportering barnevern` som et grensesnitt i produksjon i `KS-013` Fiks protokoll.

**Ikke offentlig dokumentert i denne arbeidsøkten:** En samlet plan for modernisering av KOSTRA, for eksempel overgang fra skjema og filuttrekk til maskinell henting fra kommunenes fagsystemer, eller en tidsplan for når resten av skjemaene skal over til Altinn.

## Forretningsverdi/Verdiforslag
For kommunene ligger verdien i at én rapportering dekker flere statlige behov, og at de får sammenlignbare tall tilbake som kan brukes i egen styring. Uten KOSTRA måtte kommunene håndtert flere parallelle rapporteringsløp med ulike definisjoner.

For staten ligger verdien i et felles, kontrollert tallgrunnlag for hele kommunesektoren. Det gjør det mulig å følge opp sektorpolitikk, beregne kommuneøkonomi og vurdere reformer på et grunnlag alle parter kjenner.

For samfunnet ligger verdien i åpenhet. Innbyggere, presse og forskere kan se hva kommunene bruker penger på og hva de leverer, og sammenligne egen kommune med andre.

For leverandørmarkedet ligger verdien i at rapporteringskravene og kontrollene er felles og publisert. Leverandørene kan bygge korrekte uttrekk én gang for alle kunder, og kontrollprogrammet er åpent tilgjengelig.

## Utfordringer og risiko

| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Rapporteringsbyrde | Mange skjemaer og frister gir høy arbeidsbelastning i kommunene rundt årsskiftet | Samordningsrådet og KOR skal begrense nye krav. Effekten er ikke målt i kildene |
| Teknisk | Innsending bygger på skjemaer og filuttrekk, ikke løpende maskinell deling | Gradvis flytting til Altinn. Ingen samlet moderniseringsplan funnet |
| Datakvalitet | Ulik praksis i føring og uttrekk gir tall som ikke er helt sammenlignbare | Felles kontoplan, kontrollprogram og frist for retting |
| Aktualitet | Tallene publiseres tre til seks måneder etter rapporteringsåret | Ligger i modellen. Kvartalsrapportering finnes bare for kommunekassens regnskap |
| Styring | Samordningsrådet er rådgivende, og fagdepartementene kan innføre krav på egne hjemler | Uavklart. Kildene viser ikke hvordan uenighet om nye krav håndteres |
| Strukturendringer | Kommunesammenslåinger og endret oppgavefordeling bryter tidsserier | SSB dokumenterer effekten av kommunereformen 2020 særskilt |

## Kanaler
Rapporteringen skjer gjennom SSBs KOSTRA-portal på `skjema.ssb.no`, som krever innlogging, og gjennom Altinn for skjemaene som er flyttet dit. Regnskapsdata sendes som krypterte filuttrekk fra kommunenes systemer.

Publiseringen skjer åpent på `ssb.no` gjennom Statistikkbanken og KOSTRA-tabeller etter emne, uten innlogging.

**Deduksjon:** Tabellene i Statistikkbanken kan hentes maskinelt gjennom SSBs API for statistikktabeller, som gjelder Statistikkbanken generelt. Det er ikke kontrollert tabell for tabell for KOSTRA i denne arbeidsøkten.

## Plattform
**Fakta:** Kontrollprogrammet er skrevet i Kotlin og publisert på GitHub.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Driftsmodell og plattform for KOSTRA-portalen og SSBs mottaks- og publiseringssystemer.

## Gjenbruk
KOSTRA er i seg selv et gjenbruksmønster: én rapportering fra kommunene gjenbrukes av flere departementer, direktorater og kommunene selv. Den felles kontoplanen og tjenesteinndelingen brukes også utenfor KOSTRA, blant annet som grupperingsgrunnlag i andre nasjonale registre.

Rapporteringen bygger på andre ressurser i porteføljen:
- **Altinn** brukes for skjemaene som er flyttet fra KOSTRA-portalen.
- **ID-porten** brukes for innlogging i Altinn.

### Vanlige kombinasjoner med andre produkter
- `BUFDIR-001` Barnevernsregisteret, som har overtatt barnevernsrapporteringen fra de ordinære KOSTRA-skjemaene.
- `KS-013` Fiks protokoll, med grensesnittet `Kostra-rapportering barnevern`.
- `UDIR-002` Nasjonale registre for barnehage og grunnopplæring, som tilbyr KOSTRA-gruppe som geografisk oppslag.
- `SSB-001` microdata.no, når analyser trenger mikrodata framfor publiserte nøkkeltall.
- Kommunalt rapporteringsregister hos Brønnøysundregistrene, ved vurdering av nye rapporteringskrav.

**Kildekode:** Åpen kildekode for kontrollprogrammet. Selve KOSTRA-portalen og SSBs produksjonssystemer for KOSTRA er ikke publisert.

**Lisens:** `MIT` for kontrollprogrammet, kontrollert mot `LICENSE.md` i repositoriet 2026-10-07. SSBs Python-pakke for KOSTRA-statistikk, `ssb-kostra-python`, er også `MIT`.

**Repositorium:** https://github.com/statisticsnorway/kostra-kontrollprogram

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov**
  Støttes delvis. Tallene er laget for kommunenes og statens styringsbehov, og publiseres i en form der kommuner kan sammenlignes. Rapporteringen er derimot utformet ut fra statens behov, og byrden ligger hos kommunene.

- **P4: Del og gjenbruk data**
  KOSTRA er bygget på at data rapporteres én gang og brukes til flere formål, og tallene publiseres åpent for alle.

- **P5: Del og gjenbruk løsninger**
  Kontrollprogrammet og den felles kontoplanen gjenbrukes av alle kommuner og leverandører, i stedet for at hver mottaker definerer egne krav.

- **P6: Lag digitale løsninger som støtter samhandling**
  Støttes delvis. KOSTRA gir en felles struktur for rapportering mellom forvaltningsnivåene, men samhandlingen er periodisk og skjemabasert.

Spenningen ligger i samhandlingsmønsteret. KOSTRA oppfyller målet om at data rapporteres én gang, men gjør det gjennom årlige skjemaer og filuttrekk som kommunene må produsere særskilt. Det trekker mot retningen i P4 og P6 om at data skal kunne hentes maskinelt fra kilden når det trengs. Styringsmodellen begrenser også samordningen: fagdepartementene beslutter rapporteringskrav innen egne områder, mens Samordningsrådet bare kan gi råd.

## Finansiering
**Ikke offentlig dokumentert i denne arbeidsøkten:** Hvordan KOSTRA finansieres. Kildene skiller ikke KOSTRA ut fra SSBs øvrige virksomhet.

**Deduksjon:** Kommunene bærer kostnaden ved egen rapportering, og rapporteringen er ikke brukerbetalt.

## Forvaltning/eier

| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Statistisk sentralbyrå (SSB) mottar, kontrollerer og publiserer dataene | KOSTRA-forskriften § 2–3, ssb.no |
| Driftsansvar | SSB, for KOSTRA-portalen, kontrollprogrammet og publiseringen | ssb.no, GitHub |
| Regelverk | Kommunal- og distriktsdepartementet fastsetter KOSTRA-forskriften | Lovdata |
| Innhold i tjenesterapporteringen | Fagdepartementene innen eget område | KOSTRA-forskriften § 4 |
| Styringsmodell | Samordningsrådet for KOSTRA, ledet av KDD med SSB som sekretariat og rundt 30 medlemsorganisasjoner, blant dem KS. Rådgivende, med uttalelser basert på konsensus | ssb.no, Samordningsrådet |
| Faglig utvikling | Arbeidsgrupper per tjenesteområde med årlige mandater fra Samordningsrådet. KDD leder regnskapsgruppa | ssb.no, organisering av arbeidet |
| Budsjettansvar | Ikke offentlig dokumentert i denne arbeidsøkten | – |

SSBs egne sider oppgir både 18 og 19 arbeidsgrupper. Tallet er derfor ikke oppgitt eksakt her.

## Lenke til dokumentasjon
- KOSTRA hos SSB: https://www.ssb.no/offentlig-sektor/kostra
- Om KOSTRA: https://www.ssb.no/offentlig-sektor/kostra/statistikk/kostra-kommune-stat-rapportering/om-kostra
- Innrapportering: https://www.ssb.no/innrapportering/kostra-innrapportering
- Statistikkbanken, KOSTRA: https://www.ssb.no/statbank?subject=kostrahoved
- KOSTRA-forskriften: https://lovdata.no/dokument/SF/forskrift/2019-10-18-1412
- Kontrollprogrammet: https://github.com/statisticsnorway/kostra-kontrollprogram

## Kildegrunnlag brukt i utfyllingen
Hentet 2026-10-07:
- SSB, KOSTRA: https://www.ssb.no/offentlig-sektor/kostra
- SSB, Om KOSTRA: https://www.ssb.no/offentlig-sektor/kostra/statistikk/kostra-kommune-stat-rapportering/om-kostra
- SSB, KOSTRA-innrapportering: https://www.ssb.no/innrapportering/kostra-innrapportering
- SSB, Organisering av arbeidet i KOSTRA: https://www.ssb.no/kostra/om-kostra/organisering-av-arbeidet-i-kostra
- SSB, Samordningsrådet for KOSTRA: https://www.ssb.no/kostra/om-kostra/samordningsradet-for-kostra
- Lovdata, KOSTRA-forskriften: https://lovdata.no/dokument/SF/forskrift/2019-10-18-1412
- Regjeringen, Veileder til KOSTRA-forskriften: https://www.regjeringen.no/no/dokumenter/veileder-til-kostra-forskriften/id2703425/
- Regjeringen, KOSTRA: https://www.regjeringen.no/no/tema/kommuner-og-regioner/kommuneokonomi/kostra/id1233/
- Brønnøysundregistrene, Kommunalt rapporteringsregister: https://www.brreg.no/offentlig-sektor/rapporteringsplikt/kommunalt-rapporteringsregister/
- GitHub, kostra-kontrollprogram: https://github.com/statisticsnorway/kostra-kontrollprogram

Lokale kilder:
- `arkitektur/ressurser/operative-losninger-og-tjenester/94-Fiks-protokoll-v1-claude.md`
- `arkitektur/ressurser/operative-losninger-og-tjenester/153-Barnevernsregisteret-v1-claude.md`
- `arkitektur/ressurser/operative-losninger-og-tjenester/152-Nasjonale-registre-for-barnehage-og-grunnopplaering-v1-claude.md`
