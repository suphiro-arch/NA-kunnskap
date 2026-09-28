# Arkitektur for hendelser

## Navn
Arkitektur for hendelser i felles økosystem

## Ressurs ID
DIGDIR-027

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Beste praksis for hendelsesbasert samhandling, publisert ved siden av referansearkitekturene

## Status/Livsfase
Aktiv.

**Fakta:** Digdir publiserer ressursen som en samling på fem temasider på digdir.no, opprettet i 2023. Innledningen ble sist endret 8. desember 2023, arkitekturbeskrivelsen 14. oktober 2024, siden om samspill 1. november 2024, business case 9. desember 2024 og leselista 6. desember 2024. Digdir kaller ressursen beste praksis, og siden om referansearkitekturer lenker til den som relatert ressurs.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Hvem som har utarbeidet innholdet utover Digdir, og om det har vært på høring eller er behandlet i Skate eller Arkitektur- og standardiseringsrådet.

## Kort beskrivelse
Arkitektur for hendelser i felles økosystem er et grunnlag for å utveksle og agere på hendelser på tvers av virksomheter og tjenester. Den beskriver konsept og beste praksis for hendelsesformidling, ikke en teknisk løsningsarkitektur.

Ressursen definerer en hendelse som en endring i tilstand, noe som har skjedd og beskrives i fortid, med én tilbyder og potensielt mange konsumenter. Det skiller hendelser fra kommandoer, som krever en handling og en respons fra én mottaker. Tilbyderen publiserer hendelsen, og konsumenter som abonnerer, bestemmer selv hvordan de agerer. Ressursen skiller også mellom koreografi, der ingen sentral prosess styrer samspillet i en tjenestekjede, og orkestrering, der en sentral prosess gjør det.

## Formål og normerende rolle
Formålet er at tjenester som inngår i sammenhengende tjenester, skal kunne kobles løst og utvikles mer dynamisk og uavhengig av hverandre ved hjelp av hendelser. Ressursen skal redusere ulik praksis i hendelsesbasert integrasjon og gi virksomheter en felles struktur for valg av mønster, roller, metadata og formater.

Den normerende rollen er veiledende. Ressursen er ikke en operativ hendelsesplattform, men et referansegrunnlag for analyse, arkitekturvalg, kravstilling og design av samhandlingsløsninger.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er **veiledende**, uten rettslig forankring i kildene.

**Fakta:** Ressursen er ikke hjemlet i lov eller forskrift. Digitaliseringsrundskrivet (D-2/25) punkt 1.11 anbefaler referansearkitekturene for eMelding og eOppslag, men nevner ikke Arkitektur for hendelser. Digdirs anbefaling om å bruke gjeldende referansearkitekturer ved utvikling av løsninger for informasjonsutveksling omtaler også bare eMelding og eOppslag. Digdir betegner selv ressursen som beste praksis.

**Deduksjon:** Ressursen har dermed svakere forankring enn eMelding og eOppslag, selv om den tar for seg samme type valg. En virksomhet som velger et annet hendelsesmønster, avviker ikke fra noen anbefaling i rundskrivet.

Etterlevelse skjer gjennom arkitekturbeslutninger, hendelsesmodellering, kravarbeid og forvaltning av hendelsestyper, abonnementer og tilganger. Avvik er ikke brudd, men valg av et annet mønster der flere aktører skal reagere på samme endring bør begrunnes ut fra kobling, ansvar, sikkerhet og dataminimering.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Digdirs sider om ressursen.

`Standardisering: Forvaltningsstandarder` er fjernet. Ressursen anbefaler CloudEvents og CPSV-AP-NO, men er selv beste praksis uten plass i Digitaliseringsrundskrivet, og standardvalget hører til Referansekatalogen (`DIGDIR-026`). `Informasjonsforvaltning: Oversikt over hendelser` er vurdert og ikke koblet: ressursen sier at hendelser må beskrives maskinlesbart i en katalog, men oversikten leveres av Felles datakatalog (`DIGDIR-011`). Ressursen er ikke rettslig forankret, og `Juridisk samhandling` er ikke aktuell.

- **Datautveksling og integrasjon: Hendelsesdrevet**
  Ressursen normerer evnen direkte. Den definerer rollene tilbyder og konsument og mekanismen for hendelseshåndtering, beskriver tre utvekslingsmønstre (Event Notification, Event-Carried State Transfer og Event Sourcing) og to måter å få tilgang på (push til abonnenter og pull fra en hendelsesstrøm), og sier at abonnement enten er selvbetjent eller styrt gjennom tilgangsstyring.
- **Sluttbrukertjenester: Tjenestekjeder**
  Ressursen normerer hvordan uavhengige tjenester koordineres til en kjede uten tette koblinger: den skiller koreografi fra orkestrering og anbefaler en kombinasjon der det passer, og samspillsiden sier at tjenesteresultater beskrevet etter CPSV-AP-NO skal utløse hendelser andre tjenester kan reagere på. Business case fra forsøket Born Digital viser hvordan én registreringshendelse i Brønnøysundregistrene starter parallelle prosesser i Skatteetaten og Oslo kommune uten sentral orkestrering. Det er den automatiserte og løst koblede sammensetningen på tvers av virksomheter definisjonen beskriver, mens `DIGDIR-032` Kart for tjenestekjeder normerer beskrivelsen av kjeden.
- **Veiledning: Utvikling og formidling av veiledning**
  Ressursen er Digdirs publiserte beste praksis for hendelser, og hovedkapabiliteten `Veiledning` regner beste praksis uttrykkelig med i det evnen innebærer.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Arkitekter og integrasjonsmiljøer | Felles mønster for hendelsesdrevet samhandling | Målarkitektur, løsningsdesign og mønstervalg | Kjernebrukere av ressursen |
| Produkt- og prosjektmiljøer | Klarere valg i integrasjonsløp | Tidligfase, kravarbeid, anskaffelser og løsningsutvikling | Bør bruke ressursen før teknisk plattform låses |
| Hendelsestilbydere | Beskrive og publisere hendelser forutsigbart | Hendelsesmodellering, metadata, tilgang og forvaltning | Eier kvalitet og endringsvarsling for hendelser |
| Hendelseskonsumenter | Abonnere på og reagere på relevante hendelser | Automatisering, proaktive tjenester og tjenestekjeder | Business case peker på at konsumenten best vet hvordan egen virksomhet skal reagere |
| Tjenesteeiere i sammenhengende tjenester | Koordinere egne tjenester med andres uten felles orkestrering | Livshendelser og brukerreiser på tvers | Eksemplene er byggesøknad, oppgjør etter dødsfall og det å starte en restaurant i Oslo |

## Normerende innhold
Ressursen består av fem temasider.

**Innledning.** Definerer hendelser og kommandoer, tilbyder og konsument, og koreografi og orkestrering, og beskriver hvordan hendelser fra én tjeneste kan utløse andre tjenester automatisk. Eksemplene er byggesøknad, oppgjør etter dødsfall og eBevis, og viser hendelser i sanntid, som at en advokat mister bevilgningen, og hendelser etter pull-modell, som Folkeregisterets hendelsesliste.

**Arkitektur for hendelser.** Beskriver hendelsesdrevet arkitektur som et designparadigma der en tjeneste kjøres etter å ha mottatt en hendelse. Byggeklossene er tilbyder, konsument, hendelseshåndtering og hendelsesobjekt, som er den maskinlesbare representasjonen av hendelsen. Siden beskriver tre utvekslingsmønstre:

- **Event Notification** publiserer bare at en endring har skjedd.
- **Event-Carried State Transfer** tar med innholdet i endringen.
- **Event Sourcing** lagrer alle endringer i en hendelseslogg.

I tillegg kommer to tilgangsmønstre: meldingsorientert push til abonnenter og pull fra en persistent hendelsesstrøm.

**Samspill i felles økosystem.** Anbefaler CPSV-AP-NO for beskrivelse av tjenester og tjenesteresultater, og CloudEvents-spesifikasjonen for hendelsesformatet. Virksomheter kan bygge egne løsninger eller bruke delte løsninger som Altinn Events.

**Eksempler på behov og scenarier** og **Business case.** Business case bygger på forsøket Born Digital med Brønnøysundregistrene, Skatteetaten, Oslo kommune og Digdir, om det å starte en restaurant i Oslo. I forsøket reduserte Event-Carried State Transfer behovet for oppslag hos mottakerne. Business case inneholder ingen tallfestet gevinst.

## Bruksområde
Ressursen bør brukes når virksomheter vurderer hendelsesbasert integrasjon, abonnementsmønstre, publisering av tilstandsendringer eller behov for løsere kobling enn forespørsel-svar gir.

Den passer når flere aktører kan ha interesse av samme hendelse, når tilbyderen ikke bør kjenne alle konsumenter, eller når tjenestekjeder skal kunne utvikles uten sentral orkestrering. Den er også aktuell når hendelser skal støtte proaktive tjenester eller erstatte polling.

## Typiske analyse- og beslutningssituasjoner
- Når et tiltak må velge mellom hendelsesdrevet samhandling, forespørsel-svar og meldingsutveksling.
- Når flere aktører må kunne reagere på samme tilstandsendring.
- Når en tjenestekjede skal bygges med koreografi, orkestrering eller en kombinasjon.
- Når en tilbyder må velge mellom å publisere bare at noe har skjedd, eller også innholdet i endringen.
- Når hendelsestyper, metadata, tilgang og abonnement må beskrives før anskaffelse eller løsningsdesign.

## Når ressursen normalt ikke er tilstrekkelig alene
Ressursen er ikke tilstrekkelig alene for implementasjon eller drift. Den må suppleres med:
- hendelsesplattformer, for eksempel Altinn Events, der slike er valgt
- tekniske standarder for hendelsesformat, metadata, sikkerhet og abonnement
- juridiske avklaringer om formål, behandlingsgrunnlag, taushetsplikt og tilgang til hendelser
- organisatoriske avtaler om hendelseseierskap, tjenestenivå, endringsvarsling og konsumentansvar
- kataloger der hendelser og tjenester kan beskrives og oppdages

Den er heller ikke førstevalg når behovet primært er synkront oppslag mot en datakilde, forsendelse til kjent mottaker, eller kommandoer der én bestemt mottaker skal utføre en handling. Ressursen gir ingen konkrete sikkerhetsstandarder.

## Scope og avgrensning
Inngår:
- begreper og mønstre for hendelsesdrevet samhandling
- skillet mellom hendelser og kommandoer, og mellom koreografi og orkestrering
- utvekslings- og tilgangsmønstre
- anbefalte formater for tjenestebeskrivelse og hendelser
- eksempler og business case

Inngår ikke:
- drift av hendelsesinfrastruktur
- teknisk spesifikasjon for konkrete produkter eller protokoller
- hendelseskatalog eller operativ plattform
- sikkerhetsprofil eller juridisk avtaleverk

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | Digdir publiserer og oppdaterer temasidene; sidene har egne endringsdatoer, sist i desember 2024 |
| Endringsprosess | **Ikke offentlig dokumentert i denne arbeidsøkten:** Versjonering, endringslogg eller beslutningsprosess |
| Publiserings- og beslutningsarena | digdir.no |

## Relasjon til andre ressurser
- **Referansearkitektur forespørsel-svar (eOppslag) (`DIGDIR-034`):** komplementært mønster når behovet er direkte oppslag hos en datatilbyder.
- **Referansearkitektur forsendelse (eMelding) (`DIGDIR-033`):** komplementært mønster når behovet er forsendelse til kjent mottaker.
- **Rammeverk for digital samhandling (`DIGDIR-025`):** bredere ramme for juridisk, organisatorisk, semantisk og teknisk samhandling.
- **Kart for tjenestekjeder (`DIGDIR-032`):** normerer beskrivelsen av tjenestekjeden, mens denne ressursen normerer hvordan tjenestene i kjeden koordineres gjennom hendelser.
- **Felles datakatalog (`DIGDIR-011`):** der tjenester og hendelser beskrives etter CPSV-AP-NO og gjøres oppdagbare.
- **Altinn Events (`DIGDIR-010`) og Dialogporten (`DIGDIR-020`):** operative løsninger som inngår i business case, og som kan være gjennomføringsflater.
- **Folkeregisteret (`SKATT-001`) og Enhetsregisteret (`BRREG-003`):** hendelsestilbydere i eksemplene.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er raskere og mer fleksibel reaksjon på endringer. Business case viser at én hendelse kan starte prosesser hos flere virksomheter parallelt, og at en hendelse med innhold reduserer oppslagene mottakerne må gjøre. En hendelse kan publiseres én gang og brukes av flere, uten at tilbyderen bygger egne integrasjoner til hver konsument.

Arkitekturverdien ligger i løsere kobling, mindre polling og tjenestekjeder som kan endres uten at alle deltakerne må endres samtidig.

## Konsekvens ved manglende bruk eller avvik
Hvis ressursen ikke brukes, brukes for sent eller tolkes ulikt, øker risikoen for:
- lokale og usammenlignbare hendelsesmønstre og formater
- at hendelser og kommandoer blandes sammen
- uklart eierskap til hendelsestyper, metadata, tilgang og endringsvarsling
- tette punkt-til-punkt-integrasjoner og unødvendig polling
- tjenestekjeder som bare kan endres samlet

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Forankring | Ressursen er beste praksis og nevnes ikke i Digitaliseringsrundskrivet | Svakere gjennomslag enn eMelding og eOppslag | Bruk ressursen eksplisitt i arkitekturbeslutninger og kravstilling |
| Mønstervalg | Hendelser brukes der behovet egentlig er oppslag, kommando eller forsendelse | Feil arkitektur og unødvendig kompleksitet | Sammenlign eksplisitt med eOppslag og eMelding i tidligfase |
| Juridisk tilgang | Hendelser inneholder eller røper beskyttede opplysninger | For bred tilgang | Avklar formål, hjemmel og dataminimering før publisering, særlig ved Event-Carried State Transfer |
| Semantisk kvalitet | Hendelsestyper og innhold tolkes ulikt | Lav interoperabilitet | Bruk CPSV-AP-NO og CloudEvents slik ressursen anbefaler |
| Teknisk robusthet | Konsumenter håndterer duplikater, rekkefølge eller nye forsøk feil | Feil prosessering og ustabil tjenestekjede | Still krav til idempotens, feilhåndtering og overvåking |

## Publiseringsform og tilgjengelighet
Ressursen publiseres som fem åpne temasider på digdir.no: innledning, arkitektur, samspill, eksempler og business case, i tillegg til en leseliste.

## Støtter arkitekturprinsipper
- **P6: Lag digitale løsninger som støtter samhandling** støttes tydelig, fordi ressursen beskriver hvordan virksomheter samhandler gjennom løst koblede hendelser.
- **P1: Ta utgangspunkt i brukernes behov** støttes ved at hendelser knyttes til livshendelser og brukerreiser, som byggesøknad, dødsfall og det å starte en restaurant.
- **P4: Del og gjenbruk data** støttes ved at samme hendelse kan brukes av mange konsumenter, og ved at hendelser med innhold reduserer behovet for nye oppslag.
- **P5: Del og gjenbruk løsninger** støttes ved at ressursen peker på delte løsninger som Altinn Events.

Hendelser kan gi utydelig ansvar hvis tilbyderen publiserer uten tydelige metadata, tilgangskontroll og konsumentforventninger. Event-Carried State Transfer gir en spenning mot **P7: Sørg for tillit til oppgaveløsningen**, fordi opplysninger spres til flere enn ved oppslag, og ressursen gir ingen konkrete sikkerhetsstandarder for dette.

## Lenke til dokumentasjon
- https://www.digdir.no/digital-samhandling/innledning/4169
- https://www.digdir.no/digital-samhandling/arkitektur-hendelser-i-felles-okosystem/4692
- https://www.digdir.no/digital-samhandling/samspill-i-felles-okosystem/4693
- https://www.digdir.no/digital-samhandling/eksempler-pa-behov-og-scenarier/4694
- https://www.digdir.no/digital-samhandling/business-case/6470
- https://www.digdir.no/digital-samhandling/leseliste-og-kilder/4696

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-09-25
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-09-25
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-25
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/innledning/4169 , kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/arkitektur-hendelser-i-felles-okosystem/4692 , kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/samspill-i-felles-okosystem/4693 , kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/business-case/6470 , kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/leseliste-og-kilder/4696 , kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/eksempler-pa-behov-og-scenarier/4694 , svarte 2026-09-25, innholdet ikke lest i denne kjøringen
- https://www.digdir.no/digital-samhandling/referansearkitekturer/2131 , kontrollert 2026-09-25
- https://www.digdir.no/digitalisering-og-samordning/bruk-gjeldande-referansearkitekturar-ved-utvikling-av-loysingar-informasjonsutveksling/3114 , kontrollert 2026-09-25
- https://www.regjeringen.no/no/dokumenter/digitaliseringsrundskrivet/id3103320/ , punkt 1.11, kontrollert 2026-09-25

## Endringer fra forrige versjon

### Analyseforbedringer
- Fire av de fem temasidene og leselista er lest; siden med eksempler er bare kontrollert for tilgjengelighet. `v2` bygde på innledningen og samlesiden for referansearkitekturer. `Normerende innhold` gjengir nå de tre utvekslingsmønstrene, de to tilgangsmønstrene, anbefalingen av CPSV-AP-NO og CloudEvents, og business case fra Born Digital.
- Forpliktelsesnivået er avklart etter regelen fra 2026-09-13, som `briefs/next-step.md` pekte på. `v2` oppga `anbefalt/styrende` uten å si hva styringen bygget på. `v3` sier at ressursen er veiledende uten hjemmel, og at Digitaliseringsrundskrivet punkt 1.11 nevner eMelding og eOppslag, men ikke denne ressursen.
- `Type` og `Navn` følger nå Digdirs egen betegnelse: beste praksis for hendelser i felles økosystem. `v2` kalte den referansearkitektur.
- `Sluttbrukertjenester: Tjenestekjeder` er lagt til. Ressursen normerer koordineringen av uavhengige tjenester gjennom koreografi og hendelser, og business case viser det i praksis. Det er en annen side av kapabiliteten enn den `100` Kart for tjenestekjeder dekker.
- `Standardisering: Forvaltningsstandarder` er fjernet, fordi ressursen er beste praksis uten plass i rundskrivet, og standardvalget hører til Referansekatalogen. `Veiledning: Utvikling og formidling av veiledning` er lagt til etter regelen fra 2026-09-25. `Oversikt over hendelser` er vurdert og ikke koblet.
- Kapabilitetspunktene har fullt navn med hovedkapabilitet, slik at `sync-resource-metadata.py` gjenkjenner dem.
- `Relasjon til andre ressurser` har fått ressurs-ID-er, og Kart for tjenestekjeder, Folkeregisteret og Enhetsregisteret er lagt til.

### Tekstlige forbedringer
- Formuleringene «Ressursen er særlig relevant når», henvisningen til «den oppdaterte kapabilitetsbeskrivelsen» og «Ved bruk i analyser bør ressursen behandles som …» er fjernet, etter regelen i AGENTS.md.
- Fakta, deduksjon og det som ikke er offentlig dokumentert, er merket.
- Den eldre kortlenken `/samhandling/arkitektur-hendelser/4691` er erstattet av lenker til hver temaside.
