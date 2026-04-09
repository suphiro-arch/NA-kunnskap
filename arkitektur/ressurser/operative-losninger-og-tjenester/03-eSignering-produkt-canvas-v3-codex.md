# Produkt-canvas: eSignering

## Navn
eSignering

## Ressurs ID
DIGDIR-003

## Status/Livsfase
**Produksjon** - etablert nasjonal felleslÃ¸sning for digital signering i offentlig sektor.

**Fakta:** Digdir beskriver eSignering som en felles lÃ¸sning for elektronisk signering, og dokumentasjonen viser et etablert integrasjonslÃ¸p for virksomheter som skal sende dokumenter til signering. Samarbeidsportalen beskriver bÃ¥de innfÃ¸ring, kostnadsmodell og brukstall for tjenesten.

## Modenhet
**HÃ¸y modenhet** - innarbeidet tjeneste med tydelig funksjon og etablert leveransemodell:
- Produktet har dokumentert API, kom-i-gang-lÃ¸p og beskrivelse av roller og ansvar.
- Samarbeidsportalen viser at lÃ¸sningen er i aktiv bruk og har egen statistikk- og kostnadsmodell.
- Digdir forvalter produktet, mens den tekniske leveransen skjer i samspill med Posten Norge AS.
- Produktet er modent bÃ¥de som tjeneste for virksomheter og som gjennomfÃ¸ringsmÃ¸nster for sikre signeringsprosesser.

**Deduksjon:** Modenheten er hÃ¸y fordi lÃ¸sningen fyller en tydelig nasjonal funksjon og kan gjenbrukes i mange forskjellige prosesser uten at hver virksomhet mÃ¥ etablere egen signeringsinfrastruktur.

## Kort beskrivelse
eSignering er den nasjonale felleslÃ¸sningen for digital innhenting av underskrifter i offentlige prosesser. Produktet gjÃ¸r det mulig Ã¥ sende dokumenter til signering, fÃ¸lge status pÃ¥ signeringsoppdrag og motta ferdig signerte dokumenter tilbake i en kontrollert digital flyt. LÃ¸sningen er sÃ¦rlig relevant nÃ¥r en virksomhet trenger juridisk og prosessmessig sikker signering uten Ã¥ bygge hele signeringslÃ¸pet selv.

## Kapabiliteter
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter dokumenter, signeringsoppdrag og statusmeldinger gjennom hele signeringsprosessen.
- **Tillit: Autentisering** brukes for Ã¥ sikre at den som signerer identifiserer seg med stÃ¸ttet eID fÃ¸r signeringen gjennomfÃ¸res.
- **Tillit: Signering** er produktets kjernefunksjon og gjÃ¸r det mulig Ã¥ gjennomfÃ¸re elektronisk signering av dokumenter i en nasjonal fellestjeneste.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Digdir Docs for eSignering og Samarbeidsportalen for produktomrÃ¥det.

Dokumenterte mÃ¥l:
- Gi offentlige virksomheter en felles lÃ¸sning for sikker elektronisk signering.
- Forenkle digital gjennomfÃ¸ring av signeringsprosesser.
- Redusere behovet for papir, manuell oppfÃ¸lging og lokale spesiallÃ¸sninger.
- GjÃ¸re det enklere Ã¥ ta i bruk digital signering i flere typer offentlige prosesser.

Operative mÃ¥l utledet fra de samme kildene:
- Gi virksomheter en standardisert mÃ¥te Ã¥ sende dokumenter til signering og hente dem tilbake.
- GjÃ¸re det mulig Ã¥ bygge signering inn i egne saks- og tjenesteforlÃ¸p gjennom dokumenterte API-er.
- Sikre at signeringsflyten er tydelig nok til Ã¥ kunne brukes i store og smÃ¥ prosesser uten mye lokal tilpasning.

## Brukerbehov
- Offentlige virksomheter trenger en sikker og gjenbrukbar lÃ¸sning for Ã¥ hente inn underskrifter digitalt.
- Fagsystemer og integrasjonsteam trenger API-er og hendelseslÃ¸p som gjÃ¸r det mulig Ã¥ bygge signering inn i eksisterende prosesser.
- Sluttbrukere trenger en signeringsopplevelse som er forstÃ¥elig og trygg, og som bruker kjente eID-er.
- Forvaltnings- og sikkerhetsmiljÃ¸er trenger en lÃ¸sning som gir kontroll over signeringsoppdrag, status og sporbar dokumentflyt.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige virksomheter som sender til signering | Enkel etablering av sikre signeringslÃ¸p | Vedtak, avtaler, erklÃ¦ringer og samtykker | Bruker eSignering som en felleskomponent i stedet for egen lÃ¸sning |
| Integrasjonsteam og systemleverandÃ¸rer | Dokumenterte API-er og testlÃ¸p | Integrasjon i sakssystemer, portaler og arbeidsflyter | Trenger tydelig modell for oppdrag, status og retur |
| Personer som skal signere | Trygg og forstÃ¥elig signeringsprosess | Signering via digital kanal med eID | MÃ¸ter lÃ¸sningen som del av virksomhetens tjeneste |
| Saksbehandlings- og forvaltningsmiljÃ¸er | Sporbarhet og kontroll | OppfÃ¸lging av utsendte og fullfÃ¸rte signeringsoppdrag | Viktig for prosesskontroll og dokumenthÃ¥ndtering |
| Sikkerhets- og driftsmiljÃ¸er | Stabil tjeneste og hendelsesoppfÃ¸lging | OvervÃ¥king, feilretting og forvaltning | Avhenger av tydelig rollefordeling mellom Digdir og leverandÃ¸r |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- **Opprettelse og utsending av signeringsoppdrag.** Virksomheten kan sende dokumenter inn til eSignering og opprette et konkret signeringslÃ¸p for en eller flere signatarer. Dette dekker behovet for Ã¥ hÃ¥ndtere hele signeringsoppdraget som en digital prosess, ikke bare selve underskriften.
- **Sikker signering med eID.** LÃ¸sningen kobler signeringen til stÃ¸ttet elektronisk identitet, slik at den som signerer mÃ¥ autentisere seg fÃ¸r oppdraget fullfÃ¸res. Det gjÃ¸r produktet relevant nÃ¥r det er behov for tillit til bÃ¥de signeringshandlingen og hvem som gjennomfÃ¸rte den.
- **Status og oppfÃ¸lging av signeringsprosess.** eSignering gir virksomheten mulighet til Ã¥ fÃ¸lge fremdrift, hente status og motta ferdig signert dokument tilbake. Dette er viktig nÃ¥r signering inngÃ¥r som del av en stÃ¸rre saks- eller arbeidsflyt som mÃ¥ kunne styres og spores.
- **Integrasjon i virksomhetens egne prosesser.** Produktet tilbyr et standardisert integrasjonsmÃ¸nster som gjÃ¸r at virksomheten kan bruke samme signeringstjeneste i mange sammenhenger. Det skiller eSignering fra mer manuelle eller enkeltstÃ¥ende signeringsverktÃ¸y som ikke er laget for gjenbruk i offentlig forvaltning.
- **Felles nasjonal leveransemodell.** Samarbeidsportalen beskriver ta-i-bruk-lÃ¸p, statistikk og kostnadsmodell. Det gjÃ¸r lÃ¸sningen relevant ogsÃ¥ organisatorisk, fordi den gir virksomheten et etablert lÃ¸p for innfÃ¸ring og videre bruk.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Utsending, gjennomfÃ¸ring og oppfÃ¸lging av signeringsoppdrag | Full saksbehandling fÃ¸r og etter signering |
| Signering med stÃ¸ttet eID | Generell innlogging til offentlige tjenester |
| Retur av ferdig signert dokument og statusinformasjon | Lokal arkiv- eller dokumentforvaltning hos virksomheten |
| Integrasjon i virksomhetens egne prosesser | Faglig beslutning om hvem som skal signere og hvorfor |
| Felles innfÃ¸rings- og forvaltningslÃ¸p | Full erstatning for andre tillitstjenester som ID-porten eller Maskinporten |

## Veikart over kommende funksjonalitet
**Fakta fra Samarbeidsportalen og Digdir Docs (hentet 2026-03-17):**
- ProduktomrÃ¥det videreutvikles innenfor Digdirs tillitstjenester.
- Samarbeidsportalen viser at lÃ¸sningen har bÃ¥de statistikkoppfÃ¸lging og egen kostnadsmodell, noe som tyder pÃ¥ fortsatt aktiv forvaltning og videreutvikling.

**Deduksjon:** Veikartet peker mot videre forbedring av innfÃ¸ring, brukeropplevelse og integrasjonslÃ¸p, heller enn at produktet skal skifte rolle. eSignering fremstÃ¥r som en stabil felleskomponent som gradvis forbedres, ikke som et produkt i omlegging.

## Forretningsverdi/Verdiforslag
### For virksomheter
- Reduserer behovet for Ã¥ bygge og vedlikeholde egne signeringslÃ¸sninger.
- GjÃ¸r det enklere Ã¥ digitalisere prosesser som tidligere krevde papir eller manuell oppfÃ¸lging.
- Gir en mer forutsigbar mÃ¥te Ã¥ gjennomfÃ¸re signering pÃ¥ tvers av mange prosesser og systemer.

### For sluttbrukere
- Gir en gjenkjennelig og trygg digital signeringsopplevelse.
- Reduserer behovet for fysisk oppmÃ¸te, utskrift og manuell retur av dokumenter.

### For offentlig sektor
- Ã˜ker gjenbruk ved at samme signeringsmÃ¸nster kan brukes av mange virksomheter.
- GjÃ¸r det lettere Ã¥ digitalisere dokumenttunge prosesser uten Ã¥ duplisere funksjonalitet.
- TydeliggjÃ¸r skillet mellom signering som behov og andre tilgrensende behov som innlogging, autorisasjon og varsling.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Virksomheten kan bruke signering uten Ã¥ ha avklart riktig juridisk behov eller signaturtype | Tydeligere faglig veiledning og vurdering fÃ¸r innfÃ¸ring |
| Teknisk | Feil integrasjon kan gi tapte eller hengende signeringsoppdrag | TestlÃ¸p, dokumentasjon og tydelig statushÃ¥ndtering |
| Sikkerhet | Svak hÃ¥ndtering av dokumenter fÃ¸r eller etter signering kan svekke totalprosessen | God ende-til-ende-prosess i virksomheten og tydelig rolleavgrensning |
| Avhengigheter | Virksomheten kan forveksle eSignering med full dokumentprosess eller arkivlÃ¸sning | Klare avgrensninger i design og innfÃ¸ringsveiledning |
| Brukeropplevelse | Signeringsflyten kan oppleves uklar hvis virksomheten bygger dÃ¥rlig kontekst rundt den | Bedre prosessdesign og tydelig kommunikasjon til signatarer |

## Kanaler
- Produktside: https://www.digdir.no/digital-sikkerhet/esignering/1487
- Teknisk dokumentasjon: https://docs.digdir.no/docs/eSignering/index.html
- Kom i gang: https://docs.digdir.no/docs/eSignering/esign_komigang
- Samarbeidsportal: https://samarbeid.digdir.no/esignering/dette-er-esignering/102
- Ta i bruk: https://samarbeid.digdir.no/esignering/ta-i-bruk-esignering/104
- Kostnadsmodell: https://samarbeid.digdir.no/esignering/kostnadsmodell-esignering/103
- Statistikk: https://samarbeid.digdir.no/esignering/statistikk-esignering/3428

## Plattform
eSignering er en nasjonal plattform for digital gjennomfÃ¸ring av signeringsoppdrag.

**Fakta:** Digdir forvalter produktet, og dokumentasjonen beskriver en leveransemodell der Posten Norge AS stÃ¥r for den tekniske leveransen av tjenesten. Produktet er dokumentert som API-basert tjeneste for virksomheter som skal integrere signering i egne prosesser.

**Ikke offentlig dokumentert i brukte kilder:** Full detalj om driftsplattform, runtime-arkitektur og konkret skylokasjon.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- LÃ¸sningen er laget for Ã¥ kunne brukes pÃ¥ tvers av mange typer offentlige prosesser.
- Den er spesielt relevant nÃ¥r behovet er digital signering som del av en arbeidsflyt.
- Den er mindre relevant dersom behovet egentlig er ren autentisering, varsling eller dokumentforvaltning uten signering.

## StÃ¸tter arkitekturprinsipper
- **P5: Del og gjenbruk lÃ¸sninger** realiseres ved at signering tilbys som nasjonal fellestjeneste i stedet for lokale sÃ¦rvarianter.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** styrkes fordi virksomheter kan bygge signering inn i tverrgÃ¥ende prosesser pÃ¥ en standardisert mÃ¥te.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** er sentralt fordi lÃ¸sningen gir kontrollert gjennomfÃ¸ring av digital signering med identitetsbekreftelse.

## Finansiering
- **Fakta:** Samarbeidsportalen beskriver en egen kostnadsmodell for eSignering.
- **Fakta:** Samarbeidsportalen opplyser at oppstartsavgiften ble fjernet 12. april 2024.
- **Ikke fullt offentlig dokumentert i brukte kilder:** Full prisstruktur og samlet kostnadsnivÃ¥ for hele tjenesten.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Digdirs produktside og Samarbeidsportalen |
| Teknisk leveranse | Posten Norge AS | Digdir Docs |
| Budsjett- og kostnadsmodell | Digdir forvalter produktet, med publisert kostnadsmodell | Samarbeidsportalen |
| Styringsmodell | Del av Digdirs tillitstjenester | Samarbeidsportalen |

## Lenke til dokumentasjon
- https://www.digdir.no/digital-sikkerhet/esignering/1487
- https://docs.digdir.no/docs/eSignering/index.html
- https://docs.digdir.no/docs/eSignering/esign_komigang
- https://samarbeid.digdir.no/esignering/dette-er-esignering/102
- https://samarbeid.digdir.no/esignering/ta-i-bruk-esignering/104
- https://samarbeid.digdir.no/esignering/kostnadsmodell-esignering/103
- https://samarbeid.digdir.no/esignering/statistikk-esignering/3428

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/03-eSignering-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.digdir.no/digital-sikkerhet/esignering/1487 (hentet 2026-03-17)
- Nettkilde: https://docs.digdir.no/docs/eSignering/index.html (hentet 2026-03-17)
- Nettkilde: https://docs.digdir.no/docs/eSignering/esign_komigang (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/esignering/dette-er-esignering/102 (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/esignering/ta-i-bruk-esignering/104 (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/esignering/kostnadsmodell-esignering/103 (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/esignering/statistikk-esignering/3428 (hentet 2026-03-17)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Kapabilitetsvurderingen er strammet inn til de direkte funksjonene eSignering faktisk leverer, og bredere koblinger til identifisering, samtykke og generelle integrasjonskapabiliteter er tatt ut.
- Plattform- og forvaltningsdelen bygger nÃ¥ pÃ¥ dokumenterte forhold om Digdir og Posten Norge AS, i stedet for bredere antakelser om drift og kostnadsnivÃ¥.
- Finansieringsfeltet er oppdatert med det som faktisk er publisert om kostnadsmodell og endring i oppstartsavgift.

### Tekstlige forbedringer
- Dokumentet starter ikke lenger med mÃ¥lgruppelinje, og `Ressurs ID` er skrevet uten parentesforklaring.
- Funksjonsbeskrivelsen er skrevet tydeligere som veiledning for nÃ¥r eSignering er riktig valg.
- Verdibeskrivelse og avgrensning skiller klarere mellom signering og tilgrensende behov som autentisering, dokumentforvaltning og varsling.

