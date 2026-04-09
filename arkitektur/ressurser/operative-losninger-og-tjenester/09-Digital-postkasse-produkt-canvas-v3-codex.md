# Produkt-canvas: Digital postkasse

## Navn
Digital postkasse

## Ressurs ID
DIGDIR-009

## Status/Livsfase
**Produksjon** - etablert nasjonal felleskomponent for sending av digital post fra offentlige virksomheter til innbyggere.

**Fakta:** Digdir forvalter produktomrÃ¥det, og Samarbeidsportalen beskriver bÃ¥de innfÃ¸ringslÃ¸p, kostnadsmodell, statistikk og lÃ¸pende forvaltning. Digdir Docs beskriver samtidig den tekniske lÃ¸sningen som `Digital postkasse til innbyggere` og spesifikasjonen for sikker digital post.

## Modenhet
**HÃ¸y modenhet** - innarbeidet og bredt forvaltet felleskomponent:
- LÃ¸sningen brukes som felles kanal for digital post til innbyggere pÃ¥ tvers av mange offentlige virksomheter.
- Produktet omfatter bÃ¥de integrasjon for avsendervirksomheter, mottak i postkasse hos innbygger og stÃ¸tte for papirforsendelse nÃ¥r digital levering ikke kan brukes.
- Det finnes egne sider for ta i bruk, kostnadsmodell, statistikk og teknisk dokumentasjon.
- Samarbeidsportalen viser at lÃ¸sningen er i aktiv drift og forvaltning, ikke i en tidlig innfÃ¸ringsfase.

**Deduksjon:** Modenheten er hÃ¸y bÃ¥de fordi produktet er operativt i stor skala, og fordi rollefordelingen mellom Digdir, avsender, meldingsformidler og postkasseleverandÃ¸rer er tydelig dokumentert.

## Kort beskrivelse
Digital postkasse er den nasjonale felleskomponenten for Ã¥ sende post sikkert fra offentlige virksomheter til innbyggere i en valgt digital postkasse. Produktet omfatter ikke bare selve mottakerens innboks, men hele leveranselÃ¸pet fra avsendersystem via meldingsformidling og postkasseleverandÃ¸r til mottaker, med kvitteringer, varsling og stÃ¸tte for utskrift og fysisk forsendelse nÃ¥r digital levering ikke er mulig eller Ã¸nskelig. LÃ¸sningen er derfor mer enn et API og mer enn en sluttbrukerportal: den er en felles kanal- og distribusjonstjeneste for offentlig post til innbyggere.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** gir en felles og standardisert kanal for Ã¥ sende post og motta kvitteringer mellom offentlige avsendere, meldingsformidler og postkasseleverandÃ¸rer.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter dokumentpakker, metadata og kvitteringer gjennom krav til signering, kryptering og kontrollert utveksling.
- **Sluttbrukertjenester: Sammenhengende tjenester** gir innbygger Ã©n felles mottaksflate for post fra det offentlige, selv om avsenderne er mange og kanalvalget varierer.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Digdir Docs og Samarbeidsportalen for Digital postkasse.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Samarbeidsportalen for Digital postkasse og Digdir Docs for sikker digital post.

Dokumenterte mÃ¥l:
- GjÃ¸re det enkelt for offentlige virksomheter Ã¥ kommunisere digitalt med innbyggere gjennom Ã©n felles lÃ¸sning.
- Gi innbyggere en trygg lÃ¸sning for Ã¥ motta og lese post fra det offentlige i valgt digital postkasse.
- StÃ¸tte kanalvalg der digital post, varsling og eventuell utskrift inngÃ¥r i samme overordnede leveranselÃ¸p.

Operative mÃ¥l utledet fra de samme kildene:
- Redusere behovet for at hver virksomhet etablerer egne postkasse- og distribusjonslÃ¸sninger.
- GjÃ¸re digital post til hovedkanal uten Ã¥ bryte arbeidsflyten nÃ¥r mottaker mangler eller ikke bruker digital postkasse.
- Gi avsendervirksomheter sporbarhet gjennom leveringskvitteringer, Ã¥pningskvitteringer og feilmeldinger.

## Brukerbehov
- Offentlige virksomheter trenger en felles kanal for Ã¥ sende brev og dokumenter sikkert til innbyggere uten Ã¥ bygge hele distribusjonslÃ¸pet selv.
- Integrasjonsteam og systemleverandÃ¸rer trenger et tydelig teknisk grensesnitt og et innfÃ¸ringslÃ¸p som dekker test, produksjonssetting og virksomhetssertifikater.
- Innbyggere trenger Ã©n trygg mottaksflate for offentlig post, med varsling og enkel tilgang til mottatte dokumenter.
- Forvaltnings- og driftsmiljÃ¸er trenger sporbarhet, kostnadsmodell og tydelig ansvarsdeling mellom Digdir, meldingsformidler og postkasseleverandÃ¸rer.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige avsendervirksomheter | Sikker utsending, kanalvalg og sporbarhet | Utsending av vedtak, brev og annen offentlig post | PrimÃ¦rbruker pÃ¥ avsendersiden |
| Integrasjonsteam og systemleverandÃ¸rer | Dokumenterte grensesnitt og forutsigbar innfÃ¸ring | Integrasjon mot egne sakssystemer og fagsystemer | MÃ¥ hÃ¥ndtere bÃ¥de digital og fysisk flyt |
| Innbyggere | Trygg mottaksflate og varsling | Mottak, lesing og oppbevaring av offentlig post | Velger postkasseleverandÃ¸r og bruker lÃ¸sningen indirekte og direkte |
| Digdir og drifts-/forvaltningsmiljÃ¸er | Stabil drift, statistikk og kostnadsoppfÃ¸lging | Forvaltning, avvikshÃ¥ndtering og videreutvikling | Forvalter felleslÃ¸sningen og innfÃ¸ringslÃ¸pet |
| Private aktÃ¸rer pÃ¥ vegne av det offentlige | Kontrollert bruk i offentlig oppdrag | Utsending nÃ¥r private utfÃ¸rer oppgaver pÃ¥ vegne av offentlige virksomheter | Omtales som begrenset, men mulig brukergruppe i statistikkgrunnlaget |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
**Felles utsending av digital post til innbyggere.** Produktets kjerne er Ã¥ gjÃ¸re det mulig for offentlige virksomheter Ã¥ sende digital post gjennom ett nasjonalt lÃ¸p i stedet for Ã¥ forholde seg til hver enkelt postkasseleverandÃ¸r. Dette gir en felles kanal for brev, vedtak og annen formell kommunikasjon til innbygger.

**Mottak i valgt digital postkasse med varsling.** LÃ¸sningen omfatter ikke bare avsendergrensesnittet, men ogsÃ¥ hvordan posten blir tilgjengeliggjort for mottaker i Digipost eller e-Boks. Varsling kan skje via e-post og eventuelt SMS, og varsling bygger pÃ¥ kontaktopplysninger fra Kontakt- og reservasjonsregisteret og mottakerens egne valg og innstillinger.

**Kvitteringer, sporbarhet og styrt leveranselÃ¸p.** Digdir Docs beskriver flere kvitteringstyper, blant annet leveringskvittering, Ã¥pningskvittering og varsling-feilet-kvittering. Det gjÃ¸r produktet relevant nÃ¥r virksomheter trenger dokumentert leveringsstatus og ikke bare enkel meldingsoverfÃ¸ring.

**Papirfallback og utskrifts- og forsendelsestjeneste.** ProduktomrÃ¥det omfatter ogsÃ¥ en utskrifts- og forsendelsestjeneste for tilfeller der mottaker ikke kan eller skal motta posten digitalt. Digital postkasse er derfor ikke bare en ren digital innboks, men en samlet distribusjonslÃ¸sning som hÃ¥ndterer bÃ¥de digital og fysisk sluttleveranse innenfor samme tjenestefamilie.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Felles utsending av digital post fra offentlig sektor til innbyggere | Produksjon av innhold og dokumenter i avsenders fagsystem |
| Mottak i digital postkasse hos postkasseleverandÃ¸r | Generell dialog- eller meldingsplattform utover post til innbyggere |
| Varsling, kvitteringer og sporbarhet i leveranselÃ¸pet | Full saksbehandling eller arkivering hos avsender |
| Utskrift og fysisk forsendelse som del av produktomrÃ¥det | Kontaktregisteret som egen grunndatakilde |
| InnfÃ¸ringslÃ¸p, kostnadsmodell og forvaltningsstÃ¸tte | Generisk filutveksling eller datadeling utenfor postomrÃ¥det |

## Veikart over kommende funksjonalitet
**Fakta fra Samarbeidsportalen og Digdir Docs (hentet 2026-03-27):**
- ProduktomrÃ¥det har egne sider for statistikk, kostnadsmodell og ta i bruk, noe som viser aktiv forvaltning og videreutvikling.
- Dokumentasjonen dekker bÃ¥de digital post, varsling, kvitteringer og utskrifts- og forsendelsestjeneste.

**Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Et tidsfestet, detaljert veikart for funksjonsutvikling er ikke hentet ut fra brukte kilder.

**Deduksjon:** Videreutviklingen vil trolig vÃ¦re knyttet til pris- og leveransemodeller, driftskvalitet, varsling og gradvis forbedring av kanal- og leveranselÃ¸pet, heller enn en grunnleggende omdefinering av produktet.

## Forretningsverdi/Verdiforslag
### For offentlige virksomheter
- Gir Ã©n felles kanal for utsending til innbyggere i stedet for flere separate avtaler og lÃ¸sninger.
- Kombinerer digital levering, kvitteringer og papirfallback i samme produktomrÃ¥de.
- GjÃ¸r det enklere Ã¥ skalere offentlig kommunikasjon med sporbarhet og forutsigbar kostnadsmodell.

### For innbyggere
- Samler post fra det offentlige i en trygg digital postkasse hos valgt leverandÃ¸r.
- Gir varsling nÃ¥r ny post kommer og gjÃ¸r viktige brev lettere Ã¥ finne igjen.
- Reduserer behovet for papirpost nÃ¥r digital mottak er mulig.

### For offentlig sektor
- Styrker gjenbruk ved at mange virksomheter kan bygge pÃ¥ samme distribusjonslÃ¸sning.
- Bidrar til mer ensartet og sporbar digital kommunikasjon med innbyggere.
- Gir et nasjonalt produktomrÃ¥de der digital og fysisk utsending kan styres innenfor samme ramme.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk og regelverk | Feil forstÃ¥else av leveringspunkt, kvitteringer eller reservasjonsgrunnlag kan gi feil bruk i formelle prosesser | Tydelig dokumentasjon, retningslinjer og korrekt bruk av kvitteringstyper |
| Teknisk | Feil integrasjon i avsendersystem kan gi manglende utsending, feil varsling eller svikt i kvitteringslÃ¸pet | Testregime, innfÃ¸ringslÃ¸p og tydelige tekniske spesifikasjoner |
| Informasjonssikkerhet | Post og metadata mÃ¥ beskyttes gjennom hele leveranselÃ¸pet | Krav til signering, kryptering, sertifikater og kontrollert meldingsutveksling |
| Avhengigheter | Produktet er avhengig av samspill mellom Digdir, meldingsformidler, postkasseleverandÃ¸rer og kontaktdata | Klare roller, driftsoppfÃ¸lging og publisert statistikk/status |
| Brukeropplevelse | Innbyggere kan fÃ¥ svakere opplevelse hvis varsling, tilgjengelighet eller overgang mellom digital og fysisk kanal oppleves uforutsigbar | Tydelig kommunikasjon, stabile leverandÃ¸rflater og sammenhengende kanalstyring |

## Kanaler
- Produktside hos Digdir: https://www.digdir.no/felleskomponenter/digital-post/1483
- Samarbeidsportalen, oversikt: https://samarbeid.digdir.no/digital-postkasse/dette-er-digital-postkasse/105
- Samarbeidsportalen, ta i bruk: https://samarbeid.digdir.no/digital-postkasse/ta-i-bruk-digital-postkasse-til-innbyggar/107
- Samarbeidsportalen, kostnadsmodell: https://samarbeid.digdir.no/digital-postkasse/kostnadsmodell-digital-postkasse/106
- Samarbeidsportalen, statistikk: https://samarbeid.digdir.no/digital-postkasse/statistikk-digital-postkasse-til-innbyggar/3424
- Digdir Docs, teknisk dokumentasjon: https://docs.digdir.no/resources/begrep/sikkerDigitalPost/

## Plattform
Digital postkasse er en nasjonal distribusjonslÃ¸sning som kombinerer avsenderintegrasjon, meldingsformidling, levering til postkasseleverandÃ¸r og mottak hos innbygger.

**Fakta:** Digdir Docs beskriver teknisk meldingsstruktur, sikkerhetsmekanismer, varsling, kvitteringer og utskriftslÃ¸p. Samarbeidsportalen beskriver samtidig innfÃ¸ringslÃ¸p, kostnadsmodell og driftsnÃ¦r forvaltning.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsarkitektur, detaljert komponentkart og avtalestruktur mellom alle involverte leverandÃ¸rer.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet er laget for felles bruk pÃ¥ tvers av offentlig sektor.
- Det er sÃ¦rlig relevant nÃ¥r behovet er sikker utsending av post til innbyggere med sporbar levering og kanalvalg.
- Det er mindre relevant dersom behovet egentlig er generell meldingsutveksling mellom virksomheter eller ren datadeling uten postkasse som mottaksflate.

## StÃ¸tter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov** stÃ¸ttes ved at innbygger fÃ¥r Ã©n samlet mottaksflate for offentlig post, mens virksomheten fÃ¥r ett felles utsendingslÃ¸p.
- **P5: Del og gjenbruk lÃ¸sninger** realiseres ved at offentlig sektor kan bruke samme nasjonale distribusjonslÃ¸sning i stedet for mange lokale ordninger.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** styrkes ved at avsendere, meldingsformidler, postkasseleverandÃ¸rer og kontaktdata inngÃ¥r i et felles samhandlingsmÃ¸nster.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** stÃ¸ttes gjennom sikkerhetskrav, kvitteringer og sporbarhet i leveranselÃ¸pet.

## Finansiering
- **Fakta:** Samarbeidsportalen publiserer en egen kostnadsmodell for Digital postkasse.
- **Fakta:** Avsendervirksomheter betaler brukspris per forsendelse, og dekker egne kostnader til tilpasning av egne systemer for Ã¥ ta i bruk lÃ¸sningen.
- **Fakta:** Kostnadsmodellen omfatter ogsÃ¥ elementer som postkassepris, utskrifts- og forsendelsestjeneste, ID-porten-innlogging, SMS-varsling og Ã¥pningskvittering.
- **Deduksjon:** Finansieringsmodellen er derfor en kombinasjon av sentral forvaltning hos Digdir og bruksavhengige kostnader hos virksomhetene som sender post.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Digdir.no, Samarbeidsportalen og Digdir Docs |
| Drifts- og forvaltningsansvar | Digdir forvalter produktomrÃ¥det, mens lÃ¸sningen bygger pÃ¥ samspill med meldingsformidler og postkasseleverandÃ¸rer | Samarbeidsportalen og teknisk dokumentasjon |
| Budsjett- og kostnadsmodell | Digdir publiserer kostnadsmodell, mens avsendervirksomheter betaler for bruk og egne tilpasninger | Samarbeidsportalen |
| Styringsmodell | Del av Digdirs portefÃ¸lje for digital kommunikasjon med innbyggere | Samarbeidsportalen |

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
- Beskrivelsen bygger nÃ¥ pÃ¥ oppdatert kildekontroll i bÃ¥de Digdir Docs og Samarbeidsportalen, ikke bare eldre, generelle antakelser.
- Produktet er strammet inn som en samlet distribusjons- og postkasselÃ¸sning med bÃ¥de digital levering, kvitteringer, varsling og papirfallback.
- Uverifiserte anslag om volum, teknisk plattform og finansiering er tatt ut eller erstattet med det som faktisk er offentlig dokumentert.
- Kapabilitetsvalget er redusert til de direkte funksjonene produktet faktisk leverer.

### Tekstlige forbedringer
- Dokumentet starter ikke lenger med mÃ¥lgruppelinje, og navnet er harmonisert mot dagens registerfÃ¸ring.
- `Hovedfunksjoner` beskriver nÃ¥ hele lÃ¸sningsbredden i stedet for Ã¥ redusere produktet til Ã©n teknisk kanal.
- Scope og avgrensning tydeliggjÃ¸r skillet mellom Digital postkasse, Kontakt- og reservasjonsregisteret og avsenders egne fagsystemer.

