# Produkt-canvas: Digital postkasse

## Navn
Digital postkasse

## Ressurs ID
DIGDIR-009

## Status/Livsfase
**Produksjon** - etablert nasjonal felleskomponent for sending av digital post fra offentlige virksomheter til innbyggere.

**Fakta:** Digdir forvalter produktområdet, og Samarbeidsportalen beskriver både innføringsløp, kostnadsmodell, statistikk og løpende forvaltning. Digdir Docs beskriver samtidig den tekniske løsningen som `Digital postkasse til innbyggere` og spesifikasjonen for sikker digital post.

## Modenhet
**Høy modenhet** - innarbeidet og bredt forvaltet felleskomponent:
- Løsningen brukes som felles kanal for digital post til innbyggere på tvers av mange offentlige virksomheter.
- Produktet omfatter både integrasjon for avsendervirksomheter, mottak i postkasse hos innbygger og støtte for papirforsendelse når digital levering ikke kan brukes.
- Det finnes egne sider for ta i bruk, kostnadsmodell, statistikk og teknisk dokumentasjon.
- Samarbeidsportalen viser at løsningen er i aktiv drift og forvaltning, ikke i en tidlig innføringsfase.

**Deduksjon:** Modenheten er høy både fordi produktet er operativt i stor skala, og fordi rollefordelingen mellom Digdir, avsender, meldingsformidler og postkasseleverandører er tydelig dokumentert.

## Kort beskrivelse
Digital postkasse er den nasjonale felleskomponenten for å sende post sikkert fra offentlige virksomheter til innbyggere i en valgt digital postkasse. Produktet omfatter ikke bare selve mottakerens innboks, men hele leveranseløpet fra avsendersystem via meldingsformidling og postkasseleverandør til mottaker, med kvitteringer, varsling og støtte for utskrift og fysisk forsendelse når digital levering ikke er mulig eller ønskelig. Løsningen er derfor mer enn et API og mer enn en sluttbrukerportal: den er en felles kanal- og distribusjonstjeneste for offentlig post til innbyggere.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** gir en felles og standardisert kanal for å sende post og motta kvitteringer mellom offentlige avsendere, meldingsformidler og postkasseleverandører.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter dokumentpakker, metadata og kvitteringer gjennom krav til signering, kryptering og kontrollert utveksling.
- **Sluttbrukertjenester: Sammenhengende tjenester** gir innbygger én felles mottaksflate for post fra det offentlige, selv om avsenderne er mange og kanalvalget varierer.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Digdir Docs og Samarbeidsportalen for Digital postkasse.

## Produktmål
**Primærkilder:** Samarbeidsportalen for Digital postkasse og Digdir Docs for sikker digital post.

Dokumenterte mål:
- Gjøre det enkelt for offentlige virksomheter å kommunisere digitalt med innbyggere gjennom én felles løsning.
- Gi innbyggere en trygg løsning for å motta og lese post fra det offentlige i valgt digital postkasse.
- Støtte kanalvalg der digital post, varsling og eventuell utskrift inngår i samme overordnede leveranseløp.

Operative mål utledet fra de samme kildene:
- Redusere behovet for at hver virksomhet etablerer egne postkasse- og distribusjonsløsninger.
- Gjøre digital post til hovedkanal uten å bryte arbeidsflyten når mottaker mangler eller ikke bruker digital postkasse.
- Gi avsendervirksomheter sporbarhet gjennom leveringskvitteringer, åpningskvitteringer og feilmeldinger.

## Brukerbehov
- Offentlige virksomheter trenger en felles kanal for å sende brev og dokumenter sikkert til innbyggere uten å bygge hele distribusjonsløpet selv.
- Integrasjonsteam og systemleverandører trenger et tydelig teknisk grensesnitt og et innføringsløp som dekker test, produksjonssetting og virksomhetssertifikater.
- Innbyggere trenger én trygg mottaksflate for offentlig post, med varsling og enkel tilgang til mottatte dokumenter.
- Forvaltnings- og driftsmiljøer trenger sporbarhet, kostnadsmodell og tydelig ansvarsdeling mellom Digdir, meldingsformidler og postkasseleverandører.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige avsendervirksomheter | Sikker utsending, kanalvalg og sporbarhet | Utsending av vedtak, brev og annen offentlig post | Primærbruker på avsendersiden |
| Integrasjonsteam og systemleverandører | Dokumenterte grensesnitt og forutsigbar innføring | Integrasjon mot egne sakssystemer og fagsystemer | Må håndtere både digital og fysisk flyt |
| Innbyggere | Trygg mottaksflate og varsling | Mottak, lesing og oppbevaring av offentlig post | Velger postkasseleverandør og bruker løsningen indirekte og direkte |
| Digdir og drifts-/forvaltningsmiljøer | Stabil drift, statistikk og kostnadsoppfølging | Forvaltning, avvikshåndtering og videreutvikling | Forvalter fellesløsningen og innføringsløpet |
| Private aktører på vegne av det offentlige | Kontrollert bruk i offentlig oppdrag | Utsending når private utfører oppgaver på vegne av offentlige virksomheter | Omtales som begrenset, men mulig brukergruppe i statistikkgrunnlaget |

## Hovedfunksjoner
### Primære funksjoner
**Felles utsending av digital post til innbyggere.** Produktets kjerne er å gjøre det mulig for offentlige virksomheter å sende digital post gjennom ett nasjonalt løp i stedet for å forholde seg til hver enkelt postkasseleverandør. Dette gir en felles kanal for brev, vedtak og annen formell kommunikasjon til innbygger.

**Mottak i valgt digital postkasse med varsling.** Løsningen omfatter ikke bare avsendergrensesnittet, men også hvordan posten blir tilgjengeliggjort for mottaker i Digipost eller e-Boks. Varsling kan skje via e-post og eventuelt SMS, og varsling bygger på kontaktopplysninger fra Kontakt- og reservasjonsregisteret og mottakerens egne valg og innstillinger.

**Kvitteringer, sporbarhet og styrt leveranseløp.** Digdir Docs beskriver flere kvitteringstyper, blant annet leveringskvittering, åpningskvittering og varsling-feilet-kvittering. Det gjør produktet relevant når virksomheter trenger dokumentert leveringsstatus og ikke bare enkel meldingsoverføring.

**Papirfallback og utskrifts- og forsendelsestjeneste.** Produktområdet omfatter også en utskrifts- og forsendelsestjeneste for tilfeller der mottaker ikke kan eller skal motta posten digitalt. Digital postkasse er derfor ikke bare en ren digital innboks, men en samlet distribusjonsløsning som håndterer både digital og fysisk sluttleveranse innenfor samme tjenestefamilie.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Felles utsending av digital post fra offentlig sektor til innbyggere | Produksjon av innhold og dokumenter i avsenders fagsystem |
| Mottak i digital postkasse hos postkasseleverandør | Generell dialog- eller meldingsplattform utover post til innbyggere |
| Varsling, kvitteringer og sporbarhet i leveranseløpet | Full saksbehandling eller arkivering hos avsender |
| Utskrift og fysisk forsendelse som del av produktområdet | Kontaktregisteret som egen grunndatakilde |
| Innføringsløp, kostnadsmodell og forvaltningsstøtte | Generisk filutveksling eller datadeling utenfor postområdet |

## Veikart over kommende funksjonalitet
**Fakta fra Samarbeidsportalen og Digdir Docs (hentet 2026-03-27):**
- Produktområdet har egne sider for statistikk, kostnadsmodell og ta i bruk, noe som viser aktiv forvaltning og videreutvikling.
- Dokumentasjonen dekker både digital post, varsling, kvitteringer og utskrifts- og forsendelsestjeneste.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et tidsfestet, detaljert veikart for funksjonsutvikling er ikke hentet ut fra brukte kilder.

**Deduksjon:** Videreutviklingen vil trolig være knyttet til pris- og leveransemodeller, driftskvalitet, varsling og gradvis forbedring av kanal- og leveranseløpet, heller enn en grunnleggende omdefinering av produktet.

## Forretningsverdi/Verdiforslag
### For offentlige virksomheter
- Gir én felles kanal for utsending til innbyggere i stedet for flere separate avtaler og løsninger.
- Kombinerer digital levering, kvitteringer og papirfallback i samme produktområde.
- Gjør det enklere å skalere offentlig kommunikasjon med sporbarhet og forutsigbar kostnadsmodell.

### For innbyggere
- Samler post fra det offentlige i en trygg digital postkasse hos valgt leverandør.
- Gir varsling når ny post kommer og gjør viktige brev lettere å finne igjen.
- Reduserer behovet for papirpost når digital mottak er mulig.

### For offentlig sektor
- Styrker gjenbruk ved at mange virksomheter kan bygge på samme distribusjonsløsning.
- Bidrar til mer ensartet og sporbar digital kommunikasjon med innbyggere.
- Gir et nasjonalt produktområde der digital og fysisk utsending kan styres innenfor samme ramme.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk og regelverk | Feil forståelse av leveringspunkt, kvitteringer eller reservasjonsgrunnlag kan gi feil bruk i formelle prosesser | Tydelig dokumentasjon, retningslinjer og korrekt bruk av kvitteringstyper |
| Teknisk | Feil integrasjon i avsendersystem kan gi manglende utsending, feil varsling eller svikt i kvitteringsløpet | Testregime, innføringsløp og tydelige tekniske spesifikasjoner |
| Informasjonssikkerhet | Post og metadata må beskyttes gjennom hele leveranseløpet | Krav til signering, kryptering, sertifikater og kontrollert meldingsutveksling |
| Avhengigheter | Produktet er avhengig av samspill mellom Digdir, meldingsformidler, postkasseleverandører og kontaktdata | Klare roller, driftsoppfølging og publisert statistikk/status |
| Brukeropplevelse | Innbyggere kan få svakere opplevelse hvis varsling, tilgjengelighet eller overgang mellom digital og fysisk kanal oppleves uforutsigbar | Tydelig kommunikasjon, stabile leverandørflater og sammenhengende kanalstyring |

## Kanaler
- Produktside hos Digdir: https://www.digdir.no/felleskomponenter/digital-post/1483
- Samarbeidsportalen, oversikt: https://samarbeid.digdir.no/digital-postkasse/dette-er-digital-postkasse/105
- Samarbeidsportalen, ta i bruk: https://samarbeid.digdir.no/digital-postkasse/ta-i-bruk-digital-postkasse-til-innbyggar/107
- Samarbeidsportalen, kostnadsmodell: https://samarbeid.digdir.no/digital-postkasse/kostnadsmodell-digital-postkasse/106
- Samarbeidsportalen, statistikk: https://samarbeid.digdir.no/digital-postkasse/statistikk-digital-postkasse-til-innbyggar/3424
- Digdir Docs, teknisk dokumentasjon: https://docs.digdir.no/resources/begrep/sikkerDigitalPost/

## Plattform
Digital postkasse er en nasjonal distribusjonsløsning som kombinerer avsenderintegrasjon, meldingsformidling, levering til postkasseleverandør og mottak hos innbygger.

**Fakta:** Digdir Docs beskriver teknisk meldingsstruktur, sikkerhetsmekanismer, varsling, kvitteringer og utskriftsløp. Samarbeidsportalen beskriver samtidig innføringsløp, kostnadsmodell og driftsnær forvaltning.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsarkitektur, detaljert komponentkart og avtalestruktur mellom alle involverte leverandører.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er laget for felles bruk på tvers av offentlig sektor.
- Det er særlig relevant når behovet er sikker utsending av post til innbyggere med sporbar levering og kanalvalg.
- Det er mindre relevant dersom behovet egentlig er generell meldingsutveksling mellom virksomheter eller ren datadeling uten postkasse som mottaksflate.

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov** støttes ved at innbygger får én samlet mottaksflate for offentlig post, mens virksomheten får ett felles utsendingsløp.
- **P5: Del og gjenbruk løsninger** realiseres ved at offentlig sektor kan bruke samme nasjonale distribusjonsløsning i stedet for mange lokale ordninger.
- **P6: Lag digitale løsninger som støtter samhandling** styrkes ved at avsendere, meldingsformidler, postkasseleverandører og kontaktdata inngår i et felles samhandlingsmønster.
- **P7: Sørg for tillit til oppgaveløsningen** støttes gjennom sikkerhetskrav, kvitteringer og sporbarhet i leveranseløpet.

## Finansiering
- **Fakta:** Samarbeidsportalen publiserer en egen kostnadsmodell for Digital postkasse.
- **Fakta:** Avsendervirksomheter betaler brukspris per forsendelse, og dekker egne kostnader til tilpasning av egne systemer for å ta i bruk løsningen.
- **Fakta:** Kostnadsmodellen omfatter også elementer som postkassepris, utskrifts- og forsendelsestjeneste, ID-porten-innlogging, SMS-varsling og åpningskvittering.
- **Deduksjon:** Finansieringsmodellen er derfor en kombinasjon av sentral forvaltning hos Digdir og bruksavhengige kostnader hos virksomhetene som sender post.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Digdir.no, Samarbeidsportalen og Digdir Docs |
| Drifts- og forvaltningsansvar | Digdir forvalter produktområdet, mens løsningen bygger på samspill med meldingsformidler og postkasseleverandører | Samarbeidsportalen og teknisk dokumentasjon |
| Budsjett- og kostnadsmodell | Digdir publiserer kostnadsmodell, mens avsendervirksomheter betaler for bruk og egne tilpasninger | Samarbeidsportalen |
| Styringsmodell | Del av Digdirs portefølje for digital kommunikasjon med innbyggere | Samarbeidsportalen |

## Lenke til dokumentasjon
- https://www.digdir.no/felleskomponenter/digital-post/1483
- https://samarbeid.digdir.no/digital-postkasse/dette-er-digital-postkasse/105
- https://samarbeid.digdir.no/digital-postkasse/ta-i-bruk-digital-postkasse-til-innbyggar/107
- https://samarbeid.digdir.no/digital-postkasse/kostnadsmodell-digital-postkasse/106
- https://samarbeid.digdir.no/digital-postkasse/statistikk-digital-postkasse-til-innbyggar/3424
- https://docs.digdir.no/resources/begrep/sikkerDigitalPost/
- https://docs.digdir.no/resources/begrep/sikkerDigitalPost/forretningslag/Sikkerhet/
- https://docs.digdir.no/resources/begrep/sikkerDigitalPost/meldinger/
- https://docs.digdir.no/resources/begrep/sikkerDigitalPost/utskrift/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/09-Digital-postkasse-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.digdir.no/felleskomponenter/digital-post/1483 (kontrollert 2026-03-27)
- Nettkilde: https://samarbeid.digdir.no/digital-postkasse/dette-er-digital-postkasse/105 (kontrollert 2026-03-27)
- Nettkilde: https://samarbeid.digdir.no/digital-postkasse/ta-i-bruk-digital-postkasse-til-innbyggar/107 (kontrollert 2026-03-27)
- Nettkilde: https://samarbeid.digdir.no/digital-postkasse/kostnadsmodell-digital-postkasse/106 (kontrollert 2026-03-27)
- Nettkilde: https://samarbeid.digdir.no/digital-postkasse/statistikk-digital-postkasse-til-innbyggar/3424 (kontrollert 2026-03-27)
- Nettkilde: https://docs.digdir.no/resources/begrep/sikkerDigitalPost/ (kontrollert 2026-03-27)
- Nettkilde: https://docs.digdir.no/resources/begrep/sikkerDigitalPost/forretningslag/Sikkerhet/ (kontrollert 2026-03-27)
- Nettkilde: https://docs.digdir.no/resources/begrep/sikkerDigitalPost/meldinger/ (kontrollert 2026-03-27)
- Nettkilde: https://docs.digdir.no/resources/begrep/sikkerDigitalPost/utskrift/ (kontrollert 2026-03-27)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen bygger nå på oppdatert kildekontroll i både Digdir Docs og Samarbeidsportalen, ikke bare eldre, generelle antakelser.
- Produktet er strammet inn som en samlet distribusjons- og postkasseløsning med både digital levering, kvitteringer, varsling og papirfallback.
- Uverifiserte anslag om volum, teknisk plattform og finansiering er tatt ut eller erstattet med det som faktisk er offentlig dokumentert.
- Kapabilitetsvalget er redusert til de direkte funksjonene produktet faktisk leverer.

### Tekstlige forbedringer
- Dokumentet starter ikke lenger med målgruppelinje, og navnet er harmonisert mot dagens registerføring.
- `Hovedfunksjoner` beskriver nå hele løsningsbredden i stedet for å redusere produktet til én teknisk kanal.
- Scope og avgrensning tydeliggjør skillet mellom Digital postkasse, Kontakt- og reservasjonsregisteret og avsenders egne fagsystemer.


