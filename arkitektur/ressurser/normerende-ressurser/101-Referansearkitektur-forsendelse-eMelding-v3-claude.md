# Referansearkitektur forsendelse (eMelding)

## Navn
Referansearkitektur forsendelse (eMelding)

## Ressurs ID
DIGDIR-033

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Referansearkitektur

## Status/Livsfase
Aktiv, men med innhold som ikke er oppdatert på flere år.

**Fakta:** Digdir publiserer eMelding som ett av to dokumenter på siden om referansearkitekturer, som sist ble oppdatert 18. februar 2025. Selve dokumentet er en udatert PDF. Det beskriver bruken av eDelivery i Norge slik den var «så langt (2020)», med e-handel i Peppol-nettverket som eneste domene.

**Deduksjon:** Innholdet i PDF-en er trolig ikke revidert siden omkring 2020. Senere endringer i meldingsinfrastrukturen, for eksempel ny transportinfrastruktur for digital postkasse, som dokumentet bare viser til som videre lesning, er ikke innarbeidet.

## Kort beskrivelse
Referansearkitektur forsendelse (eMelding) beskriver meldingsutveksling i form av enkeltstående meldinger fra en avsender til en kjent mottaker. Den gir et felles arkitekturmønster for hvordan en aktør klargjør seg for meldingsforsendelse, sender og mottar meldinger, før virksomheter velger konkrete transporttjenester, plattformer eller integrasjonsløsninger.

Dokumentet har to nivåer: et generisk, konseptuelt mønster som kan stå alene, og et løsningsmønster der eMelding framstilles som en norsk variant av EUs eDelivery og en løsningsnær spesialisering av firehjørnersmodellen. Mønsteret skiller meldingsforsendelse fra oppslag (eOppslag) og hendelsesdrevet samhandling.

## Formål og normerende rolle
Formålet er å etablere en felles arkitekturforståelse for meldingsbasert forsendelse, slik at virksomheter kan beskrive forsendelsesmønstre med lavere tolkningsrom og bedre sammenheng på tvers av tiltak.

Den normerende rollen er anbefalt. Referansearkitekturen er ikke en operativ transporttjeneste, men et felles analyse- og designgrunnlag. Den skal brukes når virksomheter vurderer om meldingsutveksling er riktig samhandlingsmønster, når krav til meldingsflyt skal utformes, eller når eksisterende løsninger skal sammenlignes mot et felles mønster.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er **anbefalt**, forankret som anbefaling i Digitaliseringsrundskrivet. Ingen lov eller forskrift pålegger bruk av referansearkitekturen.

**Fakta:** Digdir skriver at referansearkitekturer normalt ikke er pålagt, men at nasjonale føringer kan komme gjennom Digitaliseringsrundskrivet eller Referansekatalogen. Digitaliseringsrundskrivet (D-2/25) punkt 1.11 sier at referansearkitekturene for eMelding og eOppslag bør benyttes ved nyutvikling av løsninger for informasjonsutveksling. Rundskrivet gjelder statlig sektor. Digdir fører anbefalingen for både stat og kommune i sin oversikt over krav og anbefalinger.

**Fakta:** Digdirs side om referansearkitekturer viser til Digitaliseringsrundskrivet fra 2024. Gjeldende rundskriv er D-2/25 av 27. mai 2025, som har samme anbefaling.

Etterlevelse skjer primært gjennom arkitekturbeslutninger, kravarbeid, løsningsdesign og dokumenterte avvik. Rundskrivet krever ikke at avvik fra en anbefaling begrunnes, men et valg av et annet mønster for tilsvarende forsendelsesbehov bør begrunnes ut fra samhandlingsbehov, sikkerhet, ansvar, datamodell og teknisk gjennomføring.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot eMelding-dokumentet og Digdirs side om referansearkitekturer.

`Standardisering: EU standarder` er vurdert og ikke koblet. eMelding bygger på EUs eDelivery, men selve eDelivery-standardene realiseres i Norge gjennom Peppol eDelivery (`OPP-001`), og eMelding omsetter dem til et nasjonalt mønster framfor å ta dem i bruk selv. Referansearkitekturen er ikke rettslig forankret, og `Juridisk samhandling` er ikke aktuell.

- **Datautveksling og integrasjon: Meldingsutveksling**
  Referansearkitekturen normerer evnen direkte. Den beskriver prosessene klargjør for melding, send melding og motta melding, med avtaler mellom avsender og mottaker, registrering av kapabiliteter, adresser og sertifikater, kryptering, signering med elektronisk segl, sporing og validering av forsendelsen. Det er de avtalte prosessene, sikkerhetskravene og kvitterings- og valideringsmekanismene definisjonen av meldingsutveksling omfatter.
- **Standardisering: Forvaltningsstandarder**
  Digitaliseringsrundskrivet punkt 1.11 plasserer eMelding blant arkitektur- og standardkravene og sier at den bør benyttes ved nyutvikling av løsninger for informasjonsutveksling. Referansearkitekturen angir samtidig standarder og tekniske spesifikasjoner fra eDelivery og Peppol som løsningene skal bygge på, slik at en virksomhet som følger den, tar i bruk nasjonalt anbefalte spesifikasjoner.
- **Veiledning: Utvikling og formidling av veiledning**
  Referansearkitekturen er publisert veiledning fra Digdir, og Digdir beskriver referansearkitekturer som veiledning til utforming av arkitekturer og løsninger innen et avgrenset område.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Arkitekter og integrasjonsmiljøer | Felles mønster for meldingsbasert samhandling | Målarkitektur, løsningsdesign og mønstervalg | Kjernebrukere av ressursen |
| Prosjekt- og produktmiljøer | Tydeligere krav til meldingsflyt, roller og ansvar | Tidligfase, kravarbeid, anskaffelser og løsningsutvikling | Bør bruke ressursen før teknologivalg låses |
| Virksomheter som samhandler | Lavere tolkningsrom mellom avsender, mottaker og aksesspunkter | Tverrvirksomhetlige informasjonsutvekslinger | Viktig når flere aktører må forstå samme meldingsflyt |
| Forvaltnings- og styringsmiljøer | Sammenlignbare vurderinger av meldingsløsninger | Porteføljestyring, standardisering og gjenbruksvurdering | Når flere løsninger dekker tilgrensende behov |

## Normerende innhold
Det generiske mønsteret beskriver meldingsforsendelse til kjent mottaker, med eksempler som meldinger om hendelser og data mellom to kjente parter i tverrgående saksbehandling. Det gjør et minimum av konkrete spesifikasjoner, men forutsetter:

- **Avtaler.** Avsender og mottaker må ha avtaler som ivaretar interoperabilitet og informasjonssikkerhet. Avtalene kan være bilaterale, registrert hos partene eller hos en tiltrodd tredjepart, eller inngå i et avtalefellesskap. Et fellesskap er mulig, men ikke en forutsetning.
- **Samhandlingsspesifikasjoner** på tre nivåer: tekniske spesifikasjoner for transport, formater og feilhåndtering, semantiske spesifikasjoner for metadata og datamodeller, og organisatoriske spesifikasjoner for meldingsflyten på tvers av prosessteg (koreografi).
- **Korrelering.** Meldinger i sammenhengende prosesser må kunne korreleres, med en parameter kalt `ConversationId` eller tilsvarende.
- **Tre prosesser.** Klargjøring for meldingsforsendelse (inngå avtaler, registrere kapabiliteter, adresser og sertifikater), send melding (kontrollere mottakers kapabiliteter, formatere, kryptere, adressere, signere og ekspedere) og motta melding (kontrollere, dekryptere og validere forsendelsen).

Løsningsmønsteret bygger på firehjørnersmodellen fra EUs eDelivery. Avsenders og mottakers fagsystemer (hjørne 1 og 4) kommuniserer gjennom hvert sitt aksesspunkt (hjørne 2 og 3), og aksesspunktene er noder i et tillitsfellesskap. Modellen gir løs kobling, avtaleforvaltning gjennom tiltrodd tredjepart og mulighet til å oppdage mottakere når meldingen sendes. Ved løs kobling mellom fagsystem og aksesspunkt skal hjørne 1 kryptere og bare hjørne 4 dekryptere, slik at aksesspunktene bare ruter. Løsningseksemplet bruker Peppol, ELMA og CEF SML som registre og oppslagstjenester.

## Bruksområde
Ressursen bør brukes når virksomheter vurderer asynkron meldingsflyt, behov for robust levering, tydelig separasjon mellom avsender og mottaker, eller meldingsbasert samhandling der mottakeren er kjent.

Den passer der forutsigbar overføring, rolleforståelse og standardisert meldingsflyt er viktigere enn et øyeblikkelig synkront svar: forsendelser, dokumentutveksling, meldinger med krav til sporbarhet, og løp der flere virksomheter må forholde seg til samme forsendelsesmønster.

## Typiske analyse- og beslutningssituasjoner
- Når et tiltak må velge mellom meldingsutveksling, forespørsel-svar og hendelsesdrevet samhandling.
- Når avsender, mottaker og aksesspunkter må beskrives før anskaffelse eller løsningsdesign.
- Når krav til kvittering, sporbarhet, sikkerhet, avvikshåndtering eller meldingsformat må formuleres på et felles nivå.
- Når en virksomhet må velge mellom bilaterale avtaler og deltakelse i et avtalefellesskap.
- Når eksisterende meldingsløsninger skal vurderes for gjenbruk eller harmonisering.

## Når ressursen normalt ikke er tilstrekkelig alene
Ressursen er ikke tilstrekkelig alene for implementasjon eller drift. Den må suppleres med:
- operative løsninger, for eksempel eFormidling, Altinn Melding, Fiks melding eller Peppol eDelivery der disse er relevante
- tekniske standarder og dokumentasjon for meldingsformat, grensesnitt, sikkerhet og transport
- juridiske avklaringer om behandlingsgrunnlag, taushetsplikt, arkiv, ansvar og avtaler
- organisatoriske avtaler om roller, tjenestenivå, mottaksansvar og feiloppfølging

Den er heller ikke førstevalg når behovet primært er synkront oppslag mot en datakilde, publisering av hendelser til ukjente abonnenter eller bred informasjonsforvaltning uten forsendelsesbehov. Fordi innholdet ikke er oppdatert siden omkring 2020, må løsningseksemplene kontrolleres mot dagens infrastruktur.

## Scope og avgrensning
Inngår:
- generisk mønster for meldingsbasert forsendelse fra avsender til kjent mottaker
- prosessene for klargjøring, sending og mottak
- firehjørnersmodellen og måter å integrere aksesspunktet på
- løsningsmønster basert på eDelivery og Peppol

Inngår ikke:
- valg av konkret plattform, produkt eller leverandør
- full teknisk spesifikasjon for protokoller, meldingsformat eller sikkerhetsmekanismer
- driftsdesign, overvåking eller operativ hendelseshåndtering
- juridisk avtaleverk eller sektorvis styringsmodell

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | Digdir publiserer referansearkitekturen som PDF på siden om referansearkitekturer |
| Endringsprosess | **Ikke offentlig dokumentert i denne arbeidsøkten:** Endringslogg, versjonsnummer eller beslutningsprosess for dokumentet |
| Publiserings- og beslutningsarena | digdir.no |

## Relasjon til andre ressurser
- **Referansearkitektur forespørsel-svar (eOppslag) (`DIGDIR-034`):** komplementært mønster når behovet er oppslag i data hos en datatilbyder.
- **Arkitektur for hendelser (`DIGDIR-027`):** mønsteret når noe som har skjedd skal publiseres til konsumenter tilbyderen ikke nødvendigvis kjenner.
- **Rammeverk for digital samhandling (`DIGDIR-025`):** bredere ramme for juridisk, organisatorisk, semantisk og teknisk samhandling.
- **Digitaliseringsrundskrivet (`DIGDIR-044`):** punkt 1.11 anbefaler eMelding ved nyutvikling av løsninger for informasjonsutveksling.
- **Referansekatalogen for IT-standarder (`DIGDIR-026`):** kan gi mer konkrete standardkrav der mønsteret skal operasjonaliseres.
- **Peppol eDelivery (`OPP-001`) og ELMA (`DIGDIR-023`):** komponentene løsningsmønsteret bygger på.
- **eFormidling (`DIGDIR-007`), Altinn Melding (`DIGDIR-021`), Fiks melding (`KS-002`) og Fiks SvarUt (`KS-003`):** operative meldingsløsninger som kan være gjennomføringsflater, men som ikke erstatter mønstervalget.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er mer forutsigbar samhandling, tydeligere ansvarsdeling og lavere risiko for at hver virksomhet lager egne forsendelsesmønstre. Med et avtalefellesskap kan en aktør sende til andre i fellesskapet uten å inngå bilaterale avtaler med hver enkelt.

Arkitekturverdien ligger i at mønsteret kobler teknisk meldingsutveksling til avtaler, semantiske spesifikasjoner og organisatorisk meldingsflyt, og i at det bygger på en europeisk byggekloss slik at norske løsninger kan samhandle med europeiske.

## Konsekvens ved manglende bruk eller avvik
Hvis ressursen ikke brukes, brukes for sent eller tolkes ulikt, øker risikoen for:
- lokale og usammenlignbare meldingsmønstre
- uklare rollegrenser mellom avsender, mottaker og aksesspunkter
- svakere krav til kvittering, avvikshåndtering og sporbarhet
- høyere integrasjonskostnader når flere virksomheter skal kobles sammen
- feil valg av samhandlingsmønster, for eksempel meldingsforsendelse der eOppslag eller hendelser ville vært mer egnet

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Aktualitet | Dokumentet beskriver situasjonen omkring 2020 | Løsningseksemplene kan være utdaterte | Kontroller mot dagens meldingsinfrastruktur før bruk |
| Mønstervalg | eMelding brukes der behovet egentlig er oppslag eller hendelser | Feil arkitektur og unødvendig kompleksitet | Sammenlign eksplisitt med eOppslag og Arkitektur for hendelser i tidligfase |
| Juridisk og organisatorisk avklaring | Avtaler, behandlingsgrunnlag og ansvar avklares for sent | Forsinket innføring og svak etterlevelse | Avklar avtaleform tidlig, bilateralt eller i fellesskap |
| Semantisk kvalitet | Meldingstyper, begreper og statusverdier tolkes ulikt | Lavere interoperabilitet og mer manuell oppfølging | Koble mønsteret til informasjonsmodeller og felles kvitteringsforståelse |
| Teknisk realisering | Referansemønsteret forveksles med ferdig teknisk spesifikasjon | Mangelfulle krav til grensesnitt, sikkerhet og drift | Suppler med teknisk dokumentasjon, standarder og valgt operativ løsning |

## Publiseringsform og tilgjengelighet
Ressursen publiseres som en åpen PDF på Digdirs side om referansearkitekturer, sammen med eOppslag.

## Støtter arkitekturprinsipper
- **P6: Lag digitale løsninger som støtter samhandling** støttes tydelig, fordi ressursen beskriver hvordan meldingsbasert informasjonsflyt struktureres på tvers av aktører, med avtaler og spesifikasjoner på flere nivåer.
- **P5: Del og gjenbruk løsninger** støttes ved at mønsteret bygger på felles registre og aksesspunkter framfor bilaterale integrasjoner.
- **P2: Ta arkitekturbeslutninger på rett nivå** støttes ved at mønstervalget tas før løsning og plattform låses.
- **P7: Sørg for tillit til oppgaveløsningen** støttes ved krav om kryptering, elektronisk segl, validering og sporing av forsendelsen.

Mønsteret gir svak praktisk effekt hvis det brukes uten kobling til konkrete krav, standarder og operative løsninger, og det kan bli tolket for teknisk hvis avtaler og semantikk ikke vurderes sammen med meldingsflyten. At dokumentet ikke er oppdatert siden omkring 2020, svekker det som grunnlag for valg av konkrete komponenter.

## Lenke til dokumentasjon
- https://www.digdir.no/digital-samhandling/referansearkitekturer/2131
- https://www.digdir.no/media/3739/download
- https://www.digdir.no/digitalisering-og-samordning/bruk-gjeldande-referansearkitekturar-ved-utvikling-av-loysingar-informasjonsutveksling/3114
- https://www.regjeringen.no/no/dokumenter/digitaliseringsrundskrivet/id3103320/

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-09-25
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-09-25
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-25
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/referansearkitekturer/2131 , kontrollert 2026-09-25
- https://www.digdir.no/media/3739/download , eMelding-dokumentet, lest 2026-09-25
- https://www.digdir.no/digitalisering-og-samordning/bruk-gjeldande-referansearkitekturar-ved-utvikling-av-loysingar-informasjonsutveksling/3114 , kontrollert 2026-09-25
- https://www.regjeringen.no/no/dokumenter/digitaliseringsrundskrivet/id3103320/ , punkt 1.11, kontrollert 2026-09-25

## Endringer fra forrige versjon

### Analyseforbedringer
- Selve eMelding-dokumentet er lest. `v2` bygde på samlesiden for referansearkitekturer alene. `Normerende innhold` gjengir nå avtaleformene, samhandlingsspesifikasjonene på tre nivåer, kravet om korrelering, de tre prosessene og firehjørnersmodellen med krav til ende-til-ende-kryptering.
- `Status/Livsfase` sier nå at dokumentet er udatert og beskriver situasjonen «så langt (2020)». Aktualitet er lagt inn som risiko.
- Forpliktelsesnivået er presisert. `v2` var riktig i substans, men skrev `anbefalt/styrende` og viste til Digdirs side for anbefalingen. `v3` navngir kilden, Digitaliseringsrundskrivet D-2/25 punkt 1.11, sier at det er en anbefaling og ikke et krav, at rundskrivet gjelder staten, og at Digdirs side viser til rundskrivet fra 2024.
- Kapabilitetspunktene har fullt navn med hovedkapabilitet, slik at `sync-resource-metadata.py` gjenkjenner dem, og forklaringene er skrevet om mot definisjonene. `Veiledning: Utvikling og formidling av veiledning` er lagt til etter regelen fra 2026-09-25. `Standardisering: EU standarder` er vurdert og ikke koblet, med begrunnelse før lista.
- `Relasjon til andre ressurser` har fått ressurs-ID-er, og Digitaliseringsrundskrivet, Peppol eDelivery og ELMA er lagt til.

### Tekstlige forbedringer
- Formuleringene «Ressursen er særlig relevant når», henvisningen til «den nye kapabilitetsbeskrivelsen» og «Ved bruk i analyser bør ressursen derfor behandles som …» er fjernet, etter regelen i AGENTS.md.
- Fakta, deduksjon og det som ikke er offentlig dokumentert, er merket.
- Den gamle kortadressen under `/samhandling/` er fjernet fra lenkelista; den videresender til samme side.
