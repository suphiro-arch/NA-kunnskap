# Videokonsultasjon

## Navn
Videokonsultasjon

Registeret fører ressursen som `Videokonsultasjon (VIO)`. Forkortelsen `VIO` er ikke funnet i åpne kilder i denne arbeidsøkten, verken hos Norsk helsenett eller Helsenorge, og er derfor ikke brukt i denne beskrivelsen. Navnet i registeret er beholdt uendret inntil forkortelsen er avklart.

## Ressurs ID
NHN-005

## Status/Livsfase
**Produksjon** - i bruk i tre av fire regionale helseforetak.

**Fakta:** Norsk helsenett oppgir at videokonsultasjon er i bruk hos Helse Vest, Helse Sør-Øst og Helse Midt-Norge. Løsningen er integrert med Helsenorge og med helseforetakenes EPJ-systemer, og bestilles gjennom den aktuelle IKT-leverandøren.

**Deduksjon:** Helse Nord er ikke nevnt blant de regionene som bruker løsningen. Kildene i denne arbeidsøkten sier ikke om det skyldes at innføringen ikke er gjennomført, eller at regionen bruker en annen løsning.

## Modenhet
**Høy teknisk og regulatorisk modenhet, ujevn dekning.**

- Teknisk: løsningen kjører direkte i nettleseren uten nedlasting eller installasjon, og håndterer opptil 50 deltakere i samme møte.
- Regulatorisk: Norsk helsenett oppgir at løsningen oppfyller kravene i Normen og personvernforordningen, og følger WCAG for universell utforming.
- Organisatorisk: løsningen forutsetter medlemskap i Helsenettet og et EPJ-system som kan integreres, og videoavtalen må opprettes i EPJ-systemet og knyttes til timeboken der.
- Bruksmessig: tre regionale helseforetak bruker den, og den inngår i en bredere familie av videotjenester rettet mot fem målgrupper.

**Deduksjon:** Det svakeste leddet er EPJ-avhengigheten. Løsningen er ikke en frittstående videotjeneste en virksomhet kan ta i bruk på egen hånd; den forutsetter at EPJ-leverandøren har bygget integrasjonen og at timeboken brukes som utgangspunkt. En virksomhet uten slik integrasjon får ikke tilgang til tjenesten slik den er utformet.

## Kort beskrivelse
Videokonsultasjon er Norsk helsenetts videoløsning for spesialisthelsetjenesten, og et alternativ til fysisk oppmøte. Konsultasjonen startes fra timeboken i EPJ-systemet og gjennomføres i nettleseren, uten at pasient eller behandler må installere noe. Opptil 50 deltakere kan være med i samme møte, slik at pasient, pårørende, tolk og flere helsepersonell kan delta samtidig.

Tjenesten er én av flere videotjenester Norsk helsenett tilbyr. Plattformen er felles og nasjonal for helsesektoren, med egne tilbud rettet mot spesialisthelsetjenesten, kommuner, fastleger, avtalespesialister og private aktører. Denne beskrivelsen dekker videokonsultasjon for spesialisthelsetjenesten.

Plattformen er tilgjengelig både over internett og over helsenettet, slik at kommunikasjonen kan opprettholdes selv om internettforbindelsen faller ut.

## Kapabiliteter
- **Sluttbrukertjenester: Sammenhengende tjenester**
  Pasienten starter videotimen fra Helsenorge, mens behandleren starter den fra timeboken i EPJ-systemet. Konsultasjonen blir dermed ett sammenhengende løp på tvers av innbyggerflate og fagsystem, framfor to separate handlinger som brukeren selv må knytte sammen.

- **Tjenesteutvikling: Integrerbare tjenester**
  Løsningen eksponeres som en integrerbar tjeneste mot EPJ-systemene, slik at videokonsultasjon kan bygges inn i det arbeidsløpet helsepersonellet allerede bruker, uten en egen applikasjon ved siden av.

Koblingene er satt fordi tjenesten selv leverer både det sammenhengende løpet og integrasjonsflaten. Autentiseringen skjer med HelseID, og den evnen hører hos `HelseID`; avhengigheten er beskrevet under `Gjenbruk`.

## Produktmål
**Dokumenterte mål**, slik Norsk helsenett beskriver tjenesten:
- Gi spesialisthelsetjenesten en sikker videoløsning som alternativ til fysisk konsultasjon.
- Gjøre videokonsultasjon tilgjengelig direkte i nettleseren, uten nedlasting eller installasjon.
- Gjøre det enkelt å inkludere pasient, pårørende, tolk og helsepersonell i samme møte.
- Oppfylle kravene i Normen og personvernforordningen, og følge universell utforming.

**Utledede operative mål:**
- Redusere reisebelastning for pasienter som ellers måtte møte fysisk.
- Gjøre videokonsultasjon til en ordinær timetype i EPJ-systemet framfor en særordning.

## Brukerbehov
- Pasienter trenger å kunne møte behandleren uten å reise, særlig ved lang reisevei, nedsatt funksjonsevne eller korte oppfølgingssamtaler.
- Pasienter trenger å komme inn i konsultasjonen uten å installere programvare eller opprette en ny konto.
- Helsepersonell trenger å starte videotimen fra det systemet de allerede arbeider i, ikke fra en løsning ved siden av.
- Tolker og pårørende trenger å kunne delta i samme møte som pasienten.
- Virksomheten trenger at løsningen oppfyller Normen, slik at bruken ikke krever en egen juridisk vurdering per tilfelle.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Pasienter | Delta i konsultasjon uten å reise eller installere noe | Videotime startet fra Helsenorge | Identifiseres gjennom Helsenorge-innloggingen |
| Helsepersonell i spesialisthelsetjenesten | Starte videotime fra timeboken i EPJ | Poliklinikk, oppfølging, tverrfaglige møter | Primær arbeidsflate; enkeltinnlogging tilbys |
| Pårørende og tolker | Delta i samme møte som pasienten | Samtaler med behov for støtte eller språkhjelp | Opptil 50 deltakere i samme møte |
| Helseforetakenes IKT-miljø | Integrere løsningen mot EPJ | Innføring og drift | Bestilling går gjennom IKT-leverandøren |
| Norsk helsenett | Drifte og forvalte den nasjonale videoplattformen | Plattformdrift | Eier tjenesten |

## Hovedfunksjoner
Den første hovedfunksjonen er **videokonsultasjon i nettleseren**. Møtet gjennomføres uten nedlasting eller installasjon, som er avgjørende for at pasienter skal komme seg inn uten teknisk støtte. Opptil 50 deltakere kan være med samtidig, slik at løsningen også dekker tverrfaglige møter og samtaler med tolk og pårørende, ikke bare tomannssamtaler.

Den andre er **integrasjon mot EPJ og timebok**. Videoavtalen opprettes i EPJ-systemet og knyttes til timeboken der. Det betyr at videokonsultasjon behandles som en ordinær time i planleggingen, og at helsepersonellet ikke må holde orden på møtelenker ved siden av pasientadministrasjonen. Samtidig gjør det at løsningen forutsetter et EPJ-system som kan integreres.

Den tredje er **pasientinngangen via Helsenorge**. Pasienten starter videotimen fra Helsenorge, der hun allerede er innlogget og ser sine timer. Dette er det som knytter behandlerens timebok og pasientens egen oversikt sammen til ett løp.

Den fjerde er **sikker pålogging og etterlevelse**. HelseID brukes som standard for autentisering, og enkeltinnlogging tilbys for ansatte. Norsk helsenett oppgir at løsningen oppfyller Normen og personvernforordningen og følger WCAG. For virksomheten betyr det at etterlevelsesvurderingen i stor grad er gjort på plattformnivå.

### Typiske brukssituasjoner (generisk)
- En poliklinisk oppfølgingssamtale der fysisk oppmøte ikke er nødvendig.
- En konsultasjon der pasienten har lang reisevei eller vansker med å møte fysisk.
- En samtale som krever tolk, der tolken deltar uten å måtte være i samme rom.
- Et tverrfaglig møte om en pasient, der flere behandlere og pårørende deltar.

### Når Videokonsultasjon normalt ikke er førstevalg
- Når undersøkelsen krever fysisk tilstedeværelse. Løsningen er et alternativ til oppmøte, ikke en erstatning for undersøkelser som må gjøres fysisk.
- Når virksomheten ikke har et EPJ-system som kan integreres. Da er tjenesten i praksis ikke tilgjengelig slik den er utformet.
- Når behovet er et internt møte uten pasient. Da hører behovet hos de øvrige videotjenestene, som virtuelle møterom.
- Når virksomheten ikke er medlem av Helsenettet. Medlemskap er en forutsetning for videotjenestene.
- Når målgruppen er fastleger, avtalespesialister eller kommuner. Norsk helsenett tilbyr egne videotjenester for hver av disse, og denne ressursen dekker spesialisthelsetjenesten.

### Scope og avgrensning
Inngår: videokonsultasjon for spesialisthelsetjenesten, integrasjon mot EPJ og timebok, pasientinngang via Helsenorge, og de sikkerhets- og tilgjengelighetskravene plattformen oppfyller.

Inngår ikke: journalføring av konsultasjonen, som skjer i EPJ; timebestilling, som ligger i EPJ og Helsenorge; autentisering, som leveres av HelseID; og de øvrige videotjenestene rettet mot kommuner, fastleger, avtalespesialister og private aktører.

## Veikart over kommende funksjonalitet
**Fakta:** Norsk helsenett har varslet at virtuelle møterom på `join.nhn.no` utfases for fastleger og avtalespesialister. Dette gjelder en annen tjeneste i samme familie, ikke videokonsultasjon for spesialisthelsetjenesten.

**Ikke offentlig dokumentert i denne arbeidsøkten:** en publisert utviklingsplan for videokonsultasjon, og om og når Helse Nord tar løsningen i bruk.

## Forretningsverdi/Verdiforslag
**For pasienter:** færre reiser, mindre fravær fra arbeid og skole, og lavere terskel for å gjennomføre oppfølgingssamtaler. Pasienter med lang reisevei eller nedsatt funksjonsevne får den største gevinsten.

**For helsepersonell:** videotimen ligger i den ordinære timeboken, slik at planlegging og gjennomføring ikke krever et eget system eller egen møtelenkeadministrasjon.

**For helseforetakene:** bedre kapasitetsutnyttelse ved at konsultasjoner som ikke krever fysisk undersøkelse kan gjennomføres digitalt, og en felles nasjonal plattform framfor regionale løsninger.

**For samfunnet:** reduserte pasientreiser med tilhørende kostnader og utslipp, og likere tilgang til spesialisthelsetjenester uavhengig av bosted.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Teknisk avhengighet | Tjenesten forutsetter et EPJ-system som kan integreres, og at videoavtalen knyttes til timeboken | Bestilling går gjennom IKT-leverandøren; virksomheter uten slik integrasjon kan ikke ta den i bruk |
| Dekning | Helse Nord er ikke nevnt blant brukerne | Ikke offentlig dokumentert i denne arbeidsøkten om det skyldes manglende innføring eller et annet valg |
| Bruker | Pasienter med lav digital kompetanse eller dårlig nett kan falle av | Nettleserbasert løsning uten installasjon senker terskelen, men fjerner den ikke |
| Klinisk | Videokonsultasjon egner seg ikke for alle problemstillinger | Vurderingen ligger hos behandleren; løsningen er et alternativ, ikke en erstatning |
| Juridisk | Behandling av helseopplysninger i video stiller krav etter Normen og personvernforordningen | Norsk helsenett oppgir at løsningen oppfyller begge; virksomheten har fortsatt eget behandlingsansvar |
| Tilgjengelighet | Kravet om medlemskap i Helsenettet avgrenser hvem som kan bruke tjenesten | Følger av plattformmodellen |

## Kanaler
Tjenesten har to brukerflater. Helsepersonell starter konsultasjonen fra timeboken i EPJ-systemet, med HelseID som standard pålogging og enkeltinnlogging tilgjengelig for ansatte. Pasienten starter videotimen fra Helsenorge, der hun er innlogget fra før.

Selve møtet gjennomføres i nettleseren, uten nedlasting eller installasjon. Plattformen er tilgjengelig både over internett og over helsenettet.

Integrasjonsflaten mot EPJ er den tredje kanalen, og den bestilles gjennom virksomhetens IKT-leverandør framfor direkte hos Norsk helsenett.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** driftsmodell, skyleverandør og lokasjon. Det som er kjent, er at løsningen kjører på en nasjonal videoplattform driftet av Norsk helsenett, og at den er tilgjengelig både via internett og via helsenettet, slik at kommunikasjonen kan opprettholdes ved bortfall av internett.

## Gjenbruk
Plattformen er felles og nasjonal, og de samme grunnkomponentene brukes på tvers av tjenestene rettet mot spesialisthelsetjenesten, kommuner, fastleger, avtalespesialister og private aktører. Det er plattformgjenbruk framfor gjenbruk av kode.

Avhengigheter som ikke er kapabiliteter her: `HelseID` leverer autentisering, `Helsenorge` leverer pasientflaten, og EPJ-systemene leverer timebok og journalføring. Evnene hører hos de ressursene.

**Vanlige kombinasjoner med andre produkter:**
- `Helsenorge` som pasientens inngang til videotimen.
- `HelseID` for autentisering av helsepersonell og virksomhet.
- EPJ-systemene i helseforetakene, som eier timeboken og journalen.
- `Helsenettet` som infrastruktur og som forutsetning for tilgang.

**Kildekode:** Ikke offentlig dokumentert. Kildene i denne arbeidsøkten sier ikke om løsningen er utviklet internt eller bygger på en kommersiell videoplattform.

**Lisens:** Ikke offentlig dokumentert.

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov**
  Løsningen er utviklet i tett samarbeid med helsepersonell, krever ingen installasjon for pasienten, og følger WCAG for universell utforming.
- **P6: Lag digitale løsninger som støtter samhandling**
  Integrasjonen mellom EPJ, Helsenorge og videoplattformen gjør at tre systemer med ulike eiere inngår i samme konsultasjonsløp.
- **P5: Del og gjenbruk løsninger**
  En nasjonal plattform dekker fem målgrupper i helsesektoren framfor at hver region eller aktør bygger sitt eget.
- **P7: Sørg for tillit til oppgaveløsningen**
  Etterlevelse av Normen og personvernforordningen, og autentisering med HelseID, gir et dokumentert grunnlag for å behandle helseopplysninger i kanalen.

**Spenning og begrensning:** Løsningen står i spenning mot **P5: Del og gjenbruk løsninger** på ett punkt: den forutsetter en EPJ-integrasjon som må bygges av den enkelte leverandøren, slik at gjenbruket stopper ved plattformen og ikke når helt ut til virksomheten. Den er også i praktisk spenning mot **P1** for pasientgrupper med lav digital kompetanse eller ustabilt nett, der det digitale alternativet kan bli en barriere framfor en forenkling. Ved vurdering av bruk bør det derfor være avklart hva som skjer når videokonsultasjonen ikke lar seg gjennomføre, og hvem som fanger opp pasienten da.

## Finansiering
**Ikke offentlig dokumentert i denne arbeidsøkten:** finansieringsmodell og pris. Norsk helsenetts tjenesteside oppgir ingen prisopplysninger. Det som er kjent, er at bruk forutsetter medlemskap i Helsenettet, og at bestilling går gjennom virksomhetens IKT-leverandør.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Norsk helsenett SF | NHNs tjenestesider for video |
| Driftsansvar | Norsk helsenett SF, som nasjonal videoplattform | Samme |
| EPJ-integrasjon | Helseforetakets IKT-leverandør | NHN om at bestilling gjøres via relevant IKT-leverandør |
| Behandlingsansvar for helseopplysninger | Den enkelte virksomheten | Følger av helselovgivningen; NHN leverer plattformen |
| Budsjettansvar | Ikke offentlig dokumentert i denne arbeidsøkten | - |
| Styringsmodell | Ikke offentlig dokumentert i denne arbeidsøkten | - |

## Lenke til dokumentasjon
- Videokonsultasjon for spesialisthelsetjenesten: https://www.nhn.no/tjenester/video/for-spesialisthelsetjenesten/videokonsultasjon
- Videotjenester hos Norsk helsenett: https://www.nhn.no/tjenester/video
- Video for spesialisthelsetjenesten: https://www.nhn.no/tjenester/video/for-spesialisthelsetjenesten
- Videokonsultasjon via Helsenorge: https://www.helsenorge.no/en/about-services-on-helsenorge/video-consultations-via-Helsenorge/

## Kildegrunnlag brukt i utfyllingen
- Norsk helsenett, Videokonsultasjon for spesialisthelsetjenesten, hentet 25. september 2026.
- Norsk helsenett, Videotjenester, hentet 25. september 2026.
- Lokale kilder: `arkitektur/ressurser/produktnummerering.md`, `arkitektur/kapabiliteter/capabilities.yaml`, `arkitektur/prinsipper/principles.md`, `sources/links.md`.
