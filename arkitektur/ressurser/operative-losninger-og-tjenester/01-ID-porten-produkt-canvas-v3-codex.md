# Produkt-canvas: ID-porten

## Navn
ID-porten

## Ressurs ID
DIGDIR-001

## Status/Livsfase
**Produksjon** - etablert nasjonal fellesløsning for innlogging til offentlige digitale tjenester.

**Fakta:** Digdir beskriver ID-porten som den nasjonale fellesløsningen for innlogging til offentlige tjenester. Løsningen brukes av over 4,6 millioner brukere og mer enn 1700 offentlige tjenester, og statlige virksomheter skal som hovedregel bruke ID-porten når de trenger innlogging for brukere.

## Modenhet
**Høy modenhet** - innarbeidet felleskomponent med stor utbredelse og tydelig forvaltningsregime:
- ID-porten er en etablert del av den nasjonale tillitsinfrastrukturen og brukes bredt i offentlig sektor.
- Løsningen har oppdatert teknisk dokumentasjon for OpenID Connect, OAuth 2.0-baserte API-er og eldre SAML-integrasjoner.
- Det finnes tydelige løp for avtale, test, produksjonssetting og brukerstøtte for tjenesteeiere.
- Samarbeidsportalen beskriver et eget produktområde med mål, fokusområder og prismodell.

**Deduksjon:** Modenheten er høy både funksjonelt og organisatorisk. Samtidig er produktet i løpende utvikling, særlig for standardisering, brukeropplevelse og bedre støtte for API-er i bruker-kontekst.

## Kort beskrivelse
ID-porten er den nasjonale fellesløsningen for sikker innlogging til offentlige digitale tjenester. Løsningen gir innbyggere én gjenkjennelig inngang til tjenester på tvers av virksomheter, og gir tjenesteeiere en felles autentiseringskomponent i stedet for lokale innloggingsløsninger. ID-porten er særlig relevant når en tjeneste trenger sikker identitetsbekreftelse av en bruker, og når samme innloggingsmønster skal gjenbrukes på tvers av mange offentlige tjenester.

## Kapabiliteter
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter innloggingsflyt, tokenutstedelse og overføring av identitetsinformasjon mellom ID-porten og tjenesteeier.
- **Tillit: Autentisering** verifiserer brukerens identitet gjennom godkjente eID-er og gir et felles sikkerhetsnivå på tvers av offentlige tjenester.
- **Tillit: Identifisering** kobler innloggingen til en entydig digital identitet som tjenesteeier kan bruke videre i sin saks- og tjenestelogikk.
- **Tillit: Representasjon** støtter innlogging i bruker-kontekst også når en innbygger handler med valgt virksomhet eller i delegert kontekst, i samspill med andre tillitstjenester og representasjonsgrunnlag.
- **Tjenesteutvikling: Integrerbare tjenester** gjør autentisering gjenbrukbar gjennom standardiserte grensesnitt og dokumenterte integrasjonsmønstre.

## Produktmål
**Primærkilder:** Digdirs produktside for ID-porten og Samarbeidsportalen for tillitstjenester.

Dokumenterte mål:
- Sikre identifisering og autentisering for digitale tjenester for både virksomheter og innbyggere.
- Tilby en nasjonal innloggingsløsning som kan gjenbrukes på tvers av offentlig sektor.
- Gi sikker og enkel bruk av offentlige tjenester gjennom støtte for anerkjente eID-er.
- Videreutvikle løsningen slik at den blir sikker som standard, enklere å bruke og bedre tilpasset moderne API-behov.

Operative mål utledet fra de samme kildene:
- Redusere behovet for lokale autentiseringsløsninger hos tjenesteeiere.
- Gi tjenesteeiere tydelige integrasjonsløp for test, produksjon og videre forvaltning.
- Sikre at brukerinnlogging og identitetsinformasjon kan brukes i både nettjenester og API-er i bruker-kontekst.

**Deduksjon:** Produktet har også en viktig styringsrolle som normerende løsning for brukervendt autentisering i staten, fordi bruk av ID-porten er hovedregelen når statlige tjenester trenger innlogging.

## Brukerbehov
- Innbyggere trenger en trygg og gjenkjennelig måte å logge inn på offentlige tjenester uten å møte ulike lokale autentiseringsløsninger.
- Tjenesteeiere trenger en felles innloggingskomponent som er juridisk, sikkerhetsmessig og teknisk innarbeidet.
- Integrasjonsteam trenger standardiserte protokoller og tydelig dokumentasjon for å koble egne tjenester til nasjonal autentisering.
- Tjenester med bruker-kontekst i API-er trenger tilgangstoken og identitetsinformasjon som kan brukes videre i egne tjenester.
- Tjenester der brukeren opptrer i en virksomhetskontekst trenger støtte for innlogging med valgt virksomhet eller delegert sammenheng.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Innbyggere | Enkel og sikker innlogging | Tilgang til offentlige nettjenester | Møter ID-porten som del av tjenestens innloggingsflyt |
| Tjenesteeiere i offentlig sektor | Felles autentiseringskomponent | Innlogging i egne tjenester og portaler | Statlige virksomheter skal som hovedregel bruke ID-porten når innlogging trengs |
| Integrasjonsteam og systemleverandører | Standardiserte grensesnitt og testløp | Integrasjon via OpenID Connect, OAuth 2.0 og eventuelt SAML | Trenger dokumentasjon, testmiljø og avtaleprosess |
| API- og plattformteam | Bruker-kontekst i API-er | Tokenutstedelse og validering i egne løsninger | Relevante der autentisert bruker skal brukes videre i API-kall |
| Forvaltnings- og sikkerhetsmiljøer | Sporbar og styrbar autentiseringsløsning | Risikooppfølging, tilgangsregimer og livssyklus | Avhenger av tydelig rollefordeling og leverandørsamspill |

## Hovedfunksjoner
### Primære funksjoner
- **Sikker innlogging for innbyggere til offentlige tjenester.** ID-porten håndterer selve autentiseringen og lar brukeren logge inn med støttede eID-er som BankID, Buypass og Commfides. Dette dekker behovet for en felles, nasjonal innloggingsmekanisme når en offentlig tjeneste trenger å vite hvem brukeren er.
- **Standardisert integrasjon for tjenesteeiere.** Produktet tilbyr dokumenterte integrasjonsmønstre med OpenID Connect som anbefalt løsning, og støtter også SAML for eldre eller eksisterende integrasjoner. Dette gjør at tjenesteeiere kan gjenbruke etablerte sikkerhetsmønstre i stedet for å bygge autentisering selv.
- **Token- og identitetsgrunnlag for videre bruk i tjenestelogikk.** ID-porten utsteder grunnlaget tjenesteeier trenger for å kjenne igjen brukeren i egne løsninger og, ved behov, for å bruke autentisert bruker-kontekst videre i API-er. Dette er viktig for tjenester som ikke bare trenger en innloggingsknapp, men også sikker videre bruk av identiteten i egne prosesser.
- **Støtte for bruker-kontekst i virksomhetssammenheng.** Dokumentasjonen viser at ID-porten kan brukes i scenarier der en innbygger opptrer med valgt virksomhet. Dette gjør løsningen relevant i grenseflaten mellom personinnlogging og handling på vegne av virksomhet, men ikke som full erstatning for egne autorisasjons- og representasjonsløsninger.
- **Kontrollert innføring og forvaltning.** Tjenesteeiere får støtte gjennom avtale, testmiljø og produksjonssetting. Det gjør produktet egnet som nasjonal felleskomponent også organisatorisk, ikke bare teknisk.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Autentisering av brukere mot offentlige tjenester | Full autorisasjon til faglige ressurser i hver enkelt tjeneste |
| Standardiserte integrasjoner for innlogging | Maskin-til-maskin-autentisering uten bruker-kontekst |
| Token- og identitetsgrunnlag for videre bruk hos tjenesteeier | Signering av dokumenter eller transaksjoner |
| Støtte for bruker-kontekst i enkelte virksomhetsscenarier | Fagspesifikk tilgangsstyring og vedtak om rettigheter |
| Test, avtale og produksjonsløp for tilkobling | Erstatning for alle andre tillitstjenester i Digdir-porteføljen |

## Veikart over kommende funksjonalitet
**Fakta fra Samarbeidsportalen og Digdir Docs (hentet 2026-03-17):**
- Viktige fokusområder for de kommende årene er bedre støtte for alle typer API-er med bruker-kontekst, tett samarbeid med leverandørmarkedet, sikkerhet som standard og sømløs brukeropplevelse.
- Digdir peker også på behov for enklere og mer fleksibel integrasjon for tjenesteeiere.

**Deduksjon:** Veikartet peker mot videre modernisering av ID-porten som plattform for brukerautentisering i API-drevne tjenester, ikke bare klassiske nettbaserte innloggingsløp.

## Forretningsverdi/Verdiforslag
### For innbyggere
- Gir en gjenkjennelig og trygg innloggingsopplevelse på tvers av offentlige tjenester.
- Reduserer friksjon ved at brukeren kan forholde seg til kjente eID-er i stedet for ulike lokale løsninger.

### For tjenesteeiere
- Reduserer behovet for å etablere og forvalte egen autentiseringsløsning.
- Gir raskere vei til sikker produksjonssetting gjennom etablerte protokoller, testmiljø og felles forvaltning.
- Senker risiko ved at autentisering håndteres av en nasjonal fellesløsning med tydelig sikkerhets- og styringsregime.

### For offentlig sektor og økosystemet
- Styrker gjenbruk ved at mange tjenester kan bygge på samme autentiseringsmønster.
- Bidrar til mer konsistent brukeropplevelse og mindre fragmentert identitetsforvaltning på tvers av sektorer.
- Understøtter nasjonal styring av tillitstjenester og samhandling.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil bruk av autentiseringsnivå eller identitetsgrunnlag i tjenesteeiers egen løsning | Tydelig veiledning, krav til tjenesteeier og riktig valg av sikkerhetsnivå |
| Teknisk | Feil i integrasjon hos tjenesteeier kan gi avbrutt innlogging eller feil håndtering av token | Testmiljø, dokumenterte integrasjonsmønstre og validering før produksjon |
| Sikkerhet | Phishing, feilkonfigurasjon eller svak implementasjon i klientløsningen kan svekke sikkerheten i hele brukerreisen | Sikkerhet som standard, anbefalte protokoller og tydelig leverandørveiledning |
| Leverandør og økosystem | Avhengighet til eID-leverandører og tilpasning hos markedet kan påvirke brukeropplevelse og fremdrift | Samarbeid med leverandørmarkedet og flere støttede eID-er |
| Brukeropplevelse | Innloggingsopplevelsen kan oppleves som tung hvis tjenesteeier velger feil flyt eller dårlig kontekstskifte | Mer sømløse integrasjoner og tydeligere mønstre for tjenestedesign |

## Kanaler
- Produktside: https://www.digdir.no/id-porten/om-id-porten/1507
- Teknisk dokumentasjon: https://docs.digdir.no/docs/idporten/
- Samarbeidsportal: https://samarbeid.digdir.no/id-porten/tillitstenester/2479
- Ta i bruk: https://samarbeid.digdir.no/id-porten/ta-i-bruk-id-porten/477
- Prismodell: https://samarbeid.digdir.no/id-porten/id-portens-prismodell/78

## Plattform
ID-porten er en nasjonal autentiseringsplattform bygget rundt føderering mot eksterne eID-er og standardiserte integrasjonsgrensesnitt mot tjenesteeiere.

**Fakta:** Digdir anbefaler OpenID Connect for nye integrasjoner, støtter SAML for eksisterende bruk, og tilbyr API-støtte for bruk av ID-porten i bruker-kontekst.

**Ikke offentlig dokumentert i brukte kilder:** Full runtime-arkitektur, detaljert driftsplattform og konkret skylokasjon.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er laget nettopp for å være en felles innloggingskomponent på tvers av mange tjenester.
- Gjenbruket er organisatorisk så vel som teknisk, fordi både avtaleprosess, testløp og dokumentasjon er standardisert.
- ID-porten er særlig relevant når behovet er brukervendt autentisering. Den er mindre relevant dersom behovet egentlig er maskin-til-maskin-autentisering eller fagspesifikk autorisasjon, der andre produkter er mer treffende.

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov** gir en gjenkjennelig innloggingsopplevelse på tvers av tjenester.
- **P5: Del og gjenbruk løsninger** er en kjerneegenskap, fordi autentisering tilbys som nasjonal felleskomponent i stedet for lokale særvarianter.
- **P6: Lag digitale løsninger som støtter samhandling** gjør det mulig for mange virksomheter å samhandle om samme identitetsgrunnlag og integrasjonsmønster.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi produktet etablerer grunnlaget for sikker identifisering og innlogging.

## Finansiering
- **Fakta:** Samarbeidsportalen beskriver en prismodell med årlig fastavgift for bruk av ID-porten.
- **Fakta:** Enkelte kostnadselementer, som bruk av utenlandske eID-er, belastes den enkelte tjenesteeier.
- **Deduksjon:** Finansieringsmodellen er derfor ikke ren sentral gratisbruk for alle, men en kombinasjon av nasjonal forvaltning og kostnader knyttet til bruk og integrasjon.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Digdirs produktside og Samarbeidsportalen |
| Driftsansvar | Ikke eksplisitt navngitt i brukte offentlige kilder | Offentlige kilder bekrefter ikke detaljert leverandør- eller driftsmodell |
| Budsjett- og prismodell | Digdir forvalter produktet, med dokumentert prismodell for bruk | Samarbeidsportalen |
| Styringsmodell | Del av produktområdet for tillitstjenester | Samarbeidsportalen |

## Lenke til dokumentasjon
- https://www.digdir.no/id-porten/om-id-porten/1507
- https://docs.digdir.no/docs/idporten/
- https://samarbeid.digdir.no/id-porten/tillitstenester/2479
- https://samarbeid.digdir.no/id-porten/ta-i-bruk-id-porten/477
- https://samarbeid.digdir.no/id-porten/id-portens-prismodell/78

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/01-ID-porten-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.digdir.no/id-porten/om-id-porten/1507 (hentet 2026-03-17)
- Nettkilde: https://docs.digdir.no/docs/idporten/ (hentet 2026-03-17)
- Nettkilde: https://docs.digdir.no/docs/idporten/oidc/oidc_protocol_token/ (hentet 2026-03-17)
- Nettkilde: https://docs.digdir.no/docs/idporten/oidc/oidc_func_oauth2/ (hentet 2026-03-17)
- Nettkilde: https://docs.digdir.no/docs/idporten/saml/saml_overview_old/ (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/id-porten/tillitstenester/2479 (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/id-porten/ta-i-bruk-id-porten/477 (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/id-porten/id-portens-prismodell/78 (hentet 2026-03-17)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Finansiering er korrigert fra antatt gratis bruk til dokumentert prismodell med årlig fastavgift og enkelte brukeravhengige kostnader.
- Funksjonsbeskrivelsen er strammet inn slik at ID-porten beskrives som autentiserings- og tokenløsning, ikke som generell autorisasjonskomponent.
- Veikartet er oppdatert med dokumenterte fokusområder fra Samarbeidsportalen i stedet for antatte fremtidstemaer.
- Forvaltning og drift er skilt tydeligere, og ikke-offentlig dokumenterte forhold er markert som slike i stedet for å bli fylt med antakelser.

### Tekstlige forbedringer
- Brukersegmenter, hovedfunksjoner og avgrensning er skrevet om til en mer selvstendig produktbeskrivelse for målgruppen.
- Kapabiliteter er redusert til de som er best dokumentert og forklart med tydeligere sammenheng til produktets faktiske rolle.
- Gjenbruksvurderingen skiller tydeligere mellom når ID-porten er riktig løsning, og når andre tillitstjenester er mer relevante.


