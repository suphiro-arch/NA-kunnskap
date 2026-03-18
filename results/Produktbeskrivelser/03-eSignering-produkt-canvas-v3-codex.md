# Produkt-canvas: eSignering

## Navn
eSignering

## Ressurs ID
DIGDIR-003

## Status/Livsfase
**Produksjon** - etablert nasjonal fellesløsning for digital signering i offentlig sektor.

**Fakta:** Digdir beskriver eSignering som en felles løsning for elektronisk signering, og dokumentasjonen viser et etablert integrasjonsløp for virksomheter som skal sende dokumenter til signering. Samarbeidsportalen beskriver både innføring, kostnadsmodell og brukstall for tjenesten.

## Modenhet
**Høy modenhet** - innarbeidet tjeneste med tydelig funksjon og etablert leveransemodell:
- Produktet har dokumentert API, kom-i-gang-løp og beskrivelse av roller og ansvar.
- Samarbeidsportalen viser at løsningen er i aktiv bruk og har egen statistikk- og kostnadsmodell.
- Digdir forvalter produktet, mens den tekniske leveransen skjer i samspill med Posten Norge AS.
- Produktet er modent både som tjeneste for virksomheter og som gjennomføringsmønster for sikre signeringsprosesser.

**Deduksjon:** Modenheten er høy fordi løsningen fyller en tydelig nasjonal funksjon og kan gjenbrukes i mange forskjellige prosesser uten at hver virksomhet må etablere egen signeringsinfrastruktur.

## Kort beskrivelse
eSignering er den nasjonale fellesløsningen for digital innhenting av underskrifter i offentlige prosesser. Produktet gjør det mulig å sende dokumenter til signering, følge status på signeringsoppdrag og motta ferdig signerte dokumenter tilbake i en kontrollert digital flyt. Løsningen er særlig relevant når en virksomhet trenger juridisk og prosessmessig sikker signering uten å bygge hele signeringsløpet selv.

## Kapabiliteter
- **Tillit: Signering** er produktets kjernefunksjon og gjør det mulig å gjennomføre elektronisk signering av dokumenter i en nasjonal fellestjeneste.
- **Tillit: Autentisering** brukes for å sikre at den som signerer identifiserer seg med støttet eID før signeringen gjennomføres.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter dokumenter, signeringsoppdrag og statusmeldinger gjennom hele signeringsprosessen.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i Digdir Docs og Samarbeidsportalen.

## Produktmål
**Primærkilder:** Digdir Docs for eSignering og Samarbeidsportalen for produktområdet.

Dokumenterte mål:
- Gi offentlige virksomheter en felles løsning for sikker elektronisk signering.
- Forenkle digital gjennomføring av signeringsprosesser.
- Redusere behovet for papir, manuell oppfølging og lokale spesialløsninger.
- Gjøre det enklere å ta i bruk digital signering i flere typer offentlige prosesser.

Operative mål utledet fra de samme kildene:
- Gi virksomheter en standardisert måte å sende dokumenter til signering og hente dem tilbake.
- Gjøre det mulig å bygge signering inn i egne saks- og tjenesteforløp gjennom dokumenterte API-er.
- Sikre at signeringsflyten er tydelig nok til å kunne brukes i store og små prosesser uten mye lokal tilpasning.

## Brukerbehov
- Offentlige virksomheter trenger en sikker og gjenbrukbar løsning for å hente inn underskrifter digitalt.
- Fagsystemer og integrasjonsteam trenger API-er og hendelsesløp som gjør det mulig å bygge signering inn i eksisterende prosesser.
- Sluttbrukere trenger en signeringsopplevelse som er forståelig og trygg, og som bruker kjente eID-er.
- Forvaltnings- og sikkerhetsmiljøer trenger en løsning som gir kontroll over signeringsoppdrag, status og sporbar dokumentflyt.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter som sender til signering | Enkel etablering av sikre signeringsløp | Vedtak, avtaler, erklæringer og samtykker | Bruker eSignering som en felleskomponent i stedet for egen løsning |
| Integrasjonsteam og systemleverandører | Dokumenterte API-er og testløp | Integrasjon i sakssystemer, portaler og arbeidsflyter | Trenger tydelig modell for oppdrag, status og retur |
| Personer som skal signere | Trygg og forståelig signeringsprosess | Signering via digital kanal med eID | Møter løsningen som del av virksomhetens tjeneste |
| Saksbehandlings- og forvaltningsmiljøer | Sporbarhet og kontroll | Oppfølging av utsendte og fullførte signeringsoppdrag | Viktig for prosesskontroll og dokumenthåndtering |
| Sikkerhets- og driftsmiljøer | Stabil tjeneste og hendelsesoppfølging | Overvåking, feilretting og forvaltning | Avhenger av tydelig rollefordeling mellom Digdir og leverandør |

## Hovedfunksjoner
### Primære funksjoner
- **Opprettelse og utsending av signeringsoppdrag.** Virksomheten kan sende dokumenter inn til eSignering og opprette et konkret signeringsløp for en eller flere signatarer. Dette dekker behovet for å håndtere hele signeringsoppdraget som en digital prosess, ikke bare selve underskriften.
- **Sikker signering med eID.** Løsningen kobler signeringen til støttet elektronisk identitet, slik at den som signerer må autentisere seg før oppdraget fullføres. Det gjør produktet relevant når det er behov for tillit til både signeringshandlingen og hvem som gjennomførte den.
- **Status og oppfølging av signeringsprosess.** eSignering gir virksomheten mulighet til å følge fremdrift, hente status og motta ferdig signert dokument tilbake. Dette er viktig når signering inngår som del av en større saks- eller arbeidsflyt som må kunne styres og spores.
- **Integrasjon i virksomhetens egne prosesser.** Produktet tilbyr et standardisert integrasjonsmønster som gjør at virksomheten kan bruke samme signeringstjeneste i mange sammenhenger. Det skiller eSignering fra mer manuelle eller enkeltstående signeringsverktøy som ikke er laget for gjenbruk i offentlig forvaltning.
- **Felles nasjonal leveransemodell.** Samarbeidsportalen beskriver ta-i-bruk-løp, statistikk og kostnadsmodell. Det gjør løsningen relevant også organisatorisk, fordi den gir virksomheten et etablert løp for innføring og videre bruk.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Utsending, gjennomføring og oppfølging av signeringsoppdrag | Full saksbehandling før og etter signering |
| Signering med støttet eID | Generell innlogging til offentlige tjenester |
| Retur av ferdig signert dokument og statusinformasjon | Lokal arkiv- eller dokumentforvaltning hos virksomheten |
| Integrasjon i virksomhetens egne prosesser | Faglig beslutning om hvem som skal signere og hvorfor |
| Felles innførings- og forvaltningsløp | Full erstatning for andre tillitstjenester som ID-porten eller Maskinporten |

## Veikart over kommende funksjonalitet
**Fakta fra Samarbeidsportalen og Digdir Docs (hentet 2026-03-17):**
- Produktområdet videreutvikles innenfor Digdirs tillitstjenester.
- Samarbeidsportalen viser at løsningen har både statistikkoppfølging og egen kostnadsmodell, noe som tyder på fortsatt aktiv forvaltning og videreutvikling.

**Deduksjon:** Veikartet peker mot videre forbedring av innføring, brukeropplevelse og integrasjonsløp, heller enn at produktet skal skifte rolle. eSignering fremstår som en stabil felleskomponent som gradvis forbedres, ikke som et produkt i omlegging.

## Forretningsverdi/Verdiforslag
### For virksomheter
- Reduserer behovet for å bygge og vedlikeholde egne signeringsløsninger.
- Gjør det enklere å digitalisere prosesser som tidligere krevde papir eller manuell oppfølging.
- Gir en mer forutsigbar måte å gjennomføre signering på tvers av mange prosesser og systemer.

### For sluttbrukere
- Gir en gjenkjennelig og trygg digital signeringsopplevelse.
- Reduserer behovet for fysisk oppmøte, utskrift og manuell retur av dokumenter.

### For offentlig sektor
- Øker gjenbruk ved at samme signeringsmønster kan brukes av mange virksomheter.
- Gjør det lettere å digitalisere dokumenttunge prosesser uten å duplisere funksjonalitet.
- Tydeliggjør skillet mellom signering som behov og andre tilgrensende behov som innlogging, autorisasjon og varsling.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Virksomheten kan bruke signering uten å ha avklart riktig juridisk behov eller signaturtype | Tydeligere faglig veiledning og vurdering før innføring |
| Teknisk | Feil integrasjon kan gi tapte eller hengende signeringsoppdrag | Testløp, dokumentasjon og tydelig statushåndtering |
| Sikkerhet | Svak håndtering av dokumenter før eller etter signering kan svekke totalprosessen | God ende-til-ende-prosess i virksomheten og tydelig rolleavgrensning |
| Avhengigheter | Virksomheten kan forveksle eSignering med full dokumentprosess eller arkivløsning | Klare avgrensninger i design og innføringsveiledning |
| Brukeropplevelse | Signeringsflyten kan oppleves uklar hvis virksomheten bygger dårlig kontekst rundt den | Bedre prosessdesign og tydelig kommunikasjon til signatarer |

## Kanaler
- Produktside: https://www.digdir.no/digital-sikkerhet/esignering/1487
- Teknisk dokumentasjon: https://docs.digdir.no/docs/eSignering/index.html
- Kom i gang: https://docs.digdir.no/docs/eSignering/esign_komigang
- Samarbeidsportal: https://samarbeid.digdir.no/esignering/dette-er-esignering/102
- Ta i bruk: https://samarbeid.digdir.no/esignering/ta-i-bruk-esignering/104
- Kostnadsmodell: https://samarbeid.digdir.no/esignering/kostnadsmodell-esignering/103
- Statistikk: https://samarbeid.digdir.no/esignering/statistikk-esignering/3428

## Plattform
eSignering er en nasjonal plattform for digital gjennomføring av signeringsoppdrag.

**Fakta:** Digdir forvalter produktet, og dokumentasjonen beskriver en leveransemodell der Posten Norge AS står for den tekniske leveransen av tjenesten. Produktet er dokumentert som API-basert tjeneste for virksomheter som skal integrere signering i egne prosesser.

**Ikke offentlig dokumentert i brukte kilder:** Full detalj om driftsplattform, runtime-arkitektur og konkret skylokasjon.

## Gjenbruk
**Høy gjenbruksverdi:**
- Løsningen er laget for å kunne brukes på tvers av mange typer offentlige prosesser.
- Den er spesielt relevant når behovet er digital signering som del av en arbeidsflyt.
- Den er mindre relevant dersom behovet egentlig er ren autentisering, varsling eller dokumentforvaltning uten signering.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger** realiseres ved at signering tilbys som nasjonal fellestjeneste i stedet for lokale særvarianter.
- **P6: Lag digitale løsninger som støtter samhandling** styrkes fordi virksomheter kan bygge signering inn i tverrgående prosesser på en standardisert måte.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi løsningen gir kontrollert gjennomføring av digital signering med identitetsbekreftelse.

## Finansiering
- **Fakta:** Samarbeidsportalen beskriver en egen kostnadsmodell for eSignering.
- **Fakta:** Samarbeidsportalen opplyser at oppstartsavgiften ble fjernet 12. april 2024.
- **Ikke fullt offentlig dokumentert i brukte kilder:** Full prisstruktur og samlet kostnadsnivå for hele tjenesten.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
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
- Lokal fil: `results/Produktbeskrivelser/03-eSignering-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
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
- Plattform- og forvaltningsdelen bygger nå på dokumenterte forhold om Digdir og Posten Norge AS, i stedet for bredere antakelser om drift og kostnadsnivå.
- Finansieringsfeltet er oppdatert med det som faktisk er publisert om kostnadsmodell og endring i oppstartsavgift.

### Tekstlige forbedringer
- Dokumentet starter ikke lenger med målgruppelinje, og `Ressurs ID` er skrevet uten parentesforklaring.
- Funksjonsbeskrivelsen er skrevet tydeligere som veiledning for når eSignering er riktig valg.
- Verdibeskrivelse og avgrensning skiller klarere mellom signering og tilgrensende behov som autentisering, dokumentforvaltning og varsling.
