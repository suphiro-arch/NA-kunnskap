# Referansearkitektur forsendelse (eMelding)

## Navn
Referansearkitektur forsendelse (eMelding)

## Ressurs ID
DIGDIR-033

## Ressurskategori
Normerende ressurs

## Type normerende ressurs
Referansearkitektur

## Status/Livsfase
Aktiv. Ressursen er publisert som en av Digdirs nasjonale referansearkitekturer for samhandling.

**Fakta:** Digdir beskriver referansearkitekturer som veiledning for utforming av arkitekturer og løsninger innen avgrensede områder, og omtaler eMelding som et generisk mønster for meldingsforsendelse fra en avsender til en kjent mottaker.

## Kort beskrivelse
Referansearkitektur forsendelse (eMelding) er en normerende ressurs for meldingsbasert forsendelse mellom avsender og kjent mottaker. Ressursen gir et felles arkitekturmønster for hvordan meldingsflyt kan beskrives, vurderes og kravstilles før virksomheter velger konkrete transporttjenester, plattformer eller integrasjonsløsninger.

Ressursen er særlig relevant når en samhandlingsløsning trenger asynkron, strukturert meldingsutveksling og tydelige avklaringer om roller, ansvar, grensesnitt og forsendelsesflyt. Den bidrar til å redusere lokale særmønstre og gjør det lettere å sammenligne eMelding med andre utvekslingsmønstre, som eOppslag og hendelsesdrevet samhandling.

## Formål og normerende rolle
Formålet er å etablere en felles arkitekturforståelse for meldingsbasert forsendelse, slik at virksomheter kan beskrive forsendelsesmønstre med lavere tolkningsrom og bedre sammenheng på tvers av tiltak.

Den normerende rollen er styrende og veiledende. Referansearkitekturen er ikke en operativ transporttjeneste, men et felles analyse- og designgrunnlag. Den bør brukes når virksomheter vurderer om meldingsutveksling er riktig samhandlingsmønster, når krav til meldingsflyt skal utformes, eller når eksisterende løsninger skal sammenlignes mot et felles mønster.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er anbefalt/styrende, ikke generelt obligatorisk som enkeltressurs. Referansearkitekturer brukes normalt som støtte i arkitekturarbeid, men kan få sterkere virkning når de inngår i virksomhetsinterne retningslinjer, sektorvise føringer, anskaffelseskrav eller nasjonale krav og anbefalinger.

**Fakta:** Digdir skriver at referansearkitekturer normalt ikke er pålagt alle å bruke, men at nasjonale føringer kan komme gjennom blant annet digitaliseringsrundskrivet eller Referansekatalogen. Digdirs referansearkitekturside viser også til at eMelding og eOppslag bør brukes ved nyutvikling av løsninger for informasjonsutveksling.

Etterlevelse skjer derfor primært gjennom arkitekturbeslutninger, kravarbeid, løsningsdesign og dokumenterte avvik. Hvis en løsning velger et annet mønster enn eMelding for tilsvarende forsendelsesbehov, bør valget begrunnes ut fra samhandlingsbehov, sikkerhet, ansvar, datamodell, meldingslivsløp og teknisk gjennomføring.

## Kapabiliteter
- **Meldingsutveksling**

  Referansearkitekturen støtter kapabiliteten ved å gi et felles mønster for strukturert meldingsutveksling mellom aktører. Den tydeliggjør at meldinger ikke bare er teknisk transport, men også krever avklarte roller, ansvar, standarder, informasjonsforståelse, sikkerhetskrav og mekanismer for forsendelsesflyt. Dette samsvarer med den oppdaterte kapabilitetsbeskrivelsen, der juridisk, organisatorisk, semantisk og teknisk samhandling alle er relevante.

- **Forvaltningsstandarder**

  Ressursen støtter forvaltningsstandarder ved å gi et felles referansegrunnlag som kan brukes i kravstilling, arkitekturvurdering og harmonisering av meldingsbaserte løsninger. Den standardiserer ikke alle tekniske detaljer alene, men gir et normerende mønster som andre standarder, operative tjenester og lokale krav kan bygge videre på.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Arkitekter og integrasjonsmiljøer | Felles mønster for meldingsbasert samhandling | Målarkitektur, løsningsdesign og mønstervalg | Kjernebrukere av ressursen |
| Prosjekt- og produktmiljøer | Tydeligere krav til meldingsflyt, roller og ansvar | Tidligfase, kravarbeid, anskaffelser og løsningsutvikling | Bør bruke ressursen før teknologivalg låses |
| Virksomheter som samhandler | Lavere tolkningsrom mellom avsender, mottaker og eventuelle formidlingsledd | Tverrvirksomhetlige informasjonsutvekslinger | Viktig når flere aktører må forstå samme meldingsflyt |
| Forvaltnings- og styringsmiljøer | Sammenlignbare vurderinger av meldingsløsninger | Porteføljestyring, standardisering og gjenbruksvurdering | Relevant når flere løsninger dekker tilgrensende behov |

## Normerende innhold
Ressursen beskriver meldingsforsendelse som et generisk mønster for enkeltstående meldinger fra en avsender til en kjent mottaker. Den gir et konseptuelt grunnlag for å beskrive roller, samspill og forsendelsesflyt, og den kan stå alene eller brukes som utgangspunkt for mer spesialiserte mønstre.

eMelding er særlig knyttet til en løsningsnær spesialisering av firehjørnersmodellen. Det betyr at ressursen ikke bare handler om en avsender og mottaker, men også om hvordan formidlingsledd, aksesspunkter eller tjenesteleverandører kan inngå i en strukturert samhandlingsmodell.

Det normerende innholdet bør derfor brukes til å avklare:
- om behovet faktisk gjelder meldingsforsendelse, eller om eOppslag, hendelser eller annen datadeling passer bedre
- hvilke aktører som har avsender-, mottaker- og formidlingsroller
- hvilke krav som må stilles til meldingsformat, sporbarhet, kvittering, sikkerhet og avvikshåndtering
- hvordan meldingsflyten skal dokumenteres slik at den kan forstås og gjenbrukes på tvers

## Bruksområde
Ressursen bør brukes når virksomheter vurderer asynkron meldingsflyt, behov for robust levering, tydelig separasjon mellom avsender og mottaker, eller meldingsbasert samhandling der mottakeren er kjent.

Den er særlig relevant i tverrvirksomhetlige løp der forutsigbar overføring, rolleforståelse og standardisert meldingsflyt er viktigere enn øyeblikkelig synkront svar. Typiske eksempler er forsendelser, dokumentutveksling, meldinger med krav til sporbarhet, og løp der flere virksomheter må forholde seg til samme forsendelsesmønster.

## Typiske analyse- og beslutningssituasjoner
- Når et tiltak må velge mellom meldingsutveksling, forespørsel-svar og hendelsesdrevet samhandling.
- Når avsender, mottaker og eventuelle formidlingsledd må beskrives før anskaffelse eller løsningsdesign.
- Når krav til kvittering, sporbarhet, sikkerhet, avvikshåndtering eller meldingsformat må formuleres på et felles nivå.
- Når eksisterende meldingsløsninger skal vurderes for gjenbruk eller harmonisering.
- Når flere virksomheter tolker meldingsflyt ulikt og trenger et felles begreps- og mønstergrunnlag.

## Når ressursen normalt ikke er tilstrekkelig alene
Ressursen er ikke tilstrekkelig alene for implementasjon eller drift. Den må suppleres med:
- konkrete operative løsninger, for eksempel eFormidling, Altinn Melding, Fiks Melding eller Peppol eDelivery der disse er relevante
- tekniske standarder og dokumentasjon for meldingsformat, grensesnitt, sikkerhet og transport
- juridiske avklaringer om behandlingsgrunnlag, taushetsplikt, arkiv, ansvar og avtaler
- organisatoriske avtaler om roller, tjenestenivå, mottaksansvar og feiloppfølging

Den er heller ikke førstevalg når behovet primært er synkront oppslag mot en datakilde, publisering av hendelser til ukjente abonnenter, generell portalbruk eller bred informasjonsforvaltning uten meldingsbasert forsendelsesbehov.

## Scope og avgrensning
Inngår:
- generisk mønster for meldingsbasert forsendelse fra avsender til kjent mottaker
- konseptuell støtte for roller, ansvar og samspill i forsendelsesflyt
- beslutningsstøtte for valg av meldingsutveksling som samhandlingsmønster
- arkitekturfaglig grunnlag for kravstilling og sammenligning av meldingsløsninger

Inngår ikke:
- valg av konkret plattform, produkt eller leverandør
- full teknisk spesifikasjon for protokoller, API-er, meldingsformat eller sikkerhetsmekanismer
- driftsdesign, overvåking eller operativ hendelseshåndtering
- komplett juridisk avtaleverk eller sektorvis styringsmodell

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | Digdir publiserer og vedlikeholder referansearkitekturen som del av nasjonale referansearkitekturer |
| Endringsprosess | Endringer må ses i sammenheng med videreutvikling av referansearkitekturer, samhandlingsmønstre og nasjonale krav/anbefalinger |
| Publiserings- og beslutningsarena | Digdir.no og tilhørende referansearkitekturgrunnlag |

**Usikkert:** Det er ikke kontrollert i denne arbeidsøkten om det finnes en egen offentlig endringslogg eller formell beslutningsprosess for eMelding-dokumentet utover publisering hos Digdir.

## Relasjon til andre ressurser
- **Referansearkitektur forespørsel-svar (eOppslag):** komplementært mønster når behovet er oppslag eller spørring mot en datakilde, heller enn forsendelse til kjent mottaker.
- **Arkitektur for hendelser:** relevant når behovet gjelder hendelsesdrevet varsling eller publisering, ikke nødvendigvis meldingsforsendelse.
- **Rammeverk for digital samhandling:** bredere ramme for juridisk, organisatorisk, semantisk og teknisk samhandling.
- **Forvaltningsstandarder og referansekatalog:** kan gi mer konkrete krav eller anbefalinger der eMelding-mønsteret må operasjonaliseres.
- **Operative meldingsløsninger:** eFormidling, Altinn Melding, Fiks Melding, SvarUt/SvarInn, Peppol eDelivery og andre kan være gjennomføringsflater, men de erstatter ikke behovet for mønstervalg og arkitekturbeslutning.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er mer forutsigbar samhandling, tydeligere ansvarsdeling og lavere risiko for at hver virksomhet lager egne lokale forsendelsesmønstre. Når flere aktører beskriver meldingsflyt på samme måte, blir det enklere å stille krav, sammenligne løsninger og forklare hva som må være på plass før en meldingsbasert samhandling kan fungere.

Arkitekturverdien ligger særlig i at ressursen kobler teknisk meldingsutveksling til organisatoriske og semantiske avklaringer. Den nye kapabilitetsbeskrivelsen for Meldingsutveksling gjør dette viktigere: et godt meldingsmønster må håndtere informasjonsmodeller, status, kvittering, ansvar og sikkerhet, ikke bare transport.

## Konsekvens ved manglende bruk eller avvik
Hvis ressursen ikke brukes, brukes for sent eller tolkes ulikt, øker risikoen for:
- lokale og usammenlignbare meldingsmønstre
- uklare rollegrenser mellom avsender, mottaker og formidlingsledd
- svakere krav til kvittering, avvikshåndtering og sporbarhet
- høyere integrasjonskostnader når flere virksomheter skal kobles sammen
- feil valg av samhandlingsmønster, for eksempel bruk av meldingsforsendelse der eOppslag eller hendelser ville vært mer egnet

Avvik kan være riktig i konkrete tilfeller, men bør begrunnes eksplisitt med samhandlingsbehov, sikkerhet, juridiske rammer, mottakermodell og teknisk gjennomførbarhet.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Mønstervalg | eMelding brukes der behovet egentlig er oppslag eller hendelser | Feil arkitektur og unødvendig kompleksitet | Sammenlign eksplisitt med eOppslag og hendelsesdrevet mønster i tidligfase |
| Juridisk og organisatorisk avklaring | Roller, behandlingsgrunnlag, ansvar og avtaler avklares for sent | Forsinket innføring og svak etterlevelse | Bruk referansearkitekturen sammen med juridisk og organisatorisk samhandlingsanalyse |
| Semantisk kvalitet | Meldingstyper, begreper og statusverdier tolkes ulikt | Lavere interoperabilitet og mer manuell oppfølging | Koble mønsteret til informasjonsmodeller, begreper og felles status-/kvitteringsforståelse |
| Teknisk realisering | Referansemønsteret forveksles med ferdig teknisk spesifikasjon | Mangelfulle krav til grensesnitt, sikkerhet og drift | Suppler med teknisk dokumentasjon, standarder og valgt operativ løsning |
| Adopsjon | Ressursen blir ikke brukt i kravstilling og anskaffelser | Lokale særmønstre og høyere integrasjonskostnad | Legg referansearkitekturen inn som fast sjekkpunkt i arkitekturbeslutninger |

## Publiseringsform og tilgjengelighet
Ressursen publiseres som del av Digdirs åpne referansearkitekturer. Hovedsiden gir kontekst for referansearkitekturer generelt og peker videre til eMelding-dokumentasjonen.

## Støtter arkitekturprinsipper
- **P2: Ta arkitekturbeslutninger på rett nivå** støttes ved at mønstervalg tas før løsning og plattform låses. Dette gjør det lettere å skille mellom behov for forsendelse, oppslag og hendelser.
- **P5: Del og gjenbruk løsninger** støttes ved at virksomheter kan gjenbruke et felles samhandlingsmønster og vurdere eksisterende meldingsløsninger mot samme grunnlag.
- **P6: Lag digitale løsninger som støtter samhandling** støttes tydelig, fordi ressursen beskriver hvordan meldingsbasert informasjonsflyt kan struktureres på tvers av aktører.

Vurdering av svakheter og spenninger:
- Ressursen kan gi for svak praktisk effekt hvis den brukes uten kobling til konkrete krav, standarder og operative løsninger.
- Den kan også bli for teknisk tolket hvis juridiske, organisatoriske og semantiske forhold ikke vurderes sammen med meldingsflyten.
- Ved bruk i analyser bør ressursen derfor behandles som mønster- og beslutningsgrunnlag, ikke som komplett implementasjonsoppskrift.

## Lenke til dokumentasjon
- https://www.digdir.no/digital-samhandling/referansearkitekturer/2131
- https://www.digdir.no/samhandling/referansearkitekturer/2131

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/normerende-ressurs-canvas.system.md`
- Lokal fil: `config/templates/normerende-ressurs-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.digdir.no/digital-samhandling/referansearkitekturer/2131, kontrollert 2026-06-18

## Endringer fra forrige versjon
- Analyseforbedringer: rekontrollert Digdirs referansearkitekturside 2026-06-18, tydeliggjort forpliktelsesnivå, eMelding som generisk meldingsforsendelsesmønster, forholdet til firehjørnersmodellen og avgrensning mot eOppslag/hendelser.
- Kapabilitetsforbedringer: utvidet kapabilitetsseksjonen i tråd med oppdatert kapabilitetsbeskrivelse for `Meldingsutveksling`, særlig juridisk, organisatorisk, semantisk og teknisk avklaring.
- Tekstlige forbedringer: gjort bruksområde, beslutningssituasjoner, risiko og prinsippvurdering mer direkte anvendelige i senere analyser.
