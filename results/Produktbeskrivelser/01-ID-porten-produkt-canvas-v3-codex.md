# Produkt-canvas: ID-porten

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
ID-porten

## Ressurs ID
DIGDIR-001

## Status/Livsfase
**Produksjon** - etablert nasjonal felleslÃ¸sning for innlogging til offentlige digitale tjenester.

**Fakta:** Digdir beskriver ID-porten som den nasjonale felleslÃ¸sningen for innlogging til offentlige tjenester. LÃ¸sningen brukes av over 4,6 millioner brukere og mer enn 1700 offentlige tjenester, og statlige virksomheter skal som hovedregel bruke ID-porten nÃ¥r de trenger innlogging for brukere.

## Modenhet
**HÃ¸y modenhet** - innarbeidet felleskomponent med stor utbredelse og tydelig forvaltningsregime:
- ID-porten er en etablert del av den nasjonale tillitsinfrastrukturen og brukes bredt i offentlig sektor.
- LÃ¸sningen har oppdatert teknisk dokumentasjon for OpenID Connect, OAuth 2.0-baserte API-er og eldre SAML-integrasjoner.
- Det finnes tydelige lÃ¸p for avtale, test, produksjonssetting og brukerstÃ¸tte for tjenesteeiere.
- Samarbeidsportalen beskriver et eget produktomrÃ¥de med mÃ¥l, fokusomrÃ¥der og prismodell.

**Deduksjon:** Modenheten er hÃ¸y bÃ¥de funksjonelt og organisatorisk. Samtidig er produktet i lÃ¸pende utvikling, sÃ¦rlig for standardisering, brukeropplevelse og bedre stÃ¸tte for API-er i bruker-kontekst.

## Kort beskrivelse
ID-porten er den nasjonale felleslÃ¸sningen for sikker innlogging til offentlige digitale tjenester. LÃ¸sningen gir innbyggere Ã©n gjenkjennelig inngang til tjenester pÃ¥ tvers av virksomheter, og gir tjenesteeiere en felles autentiseringskomponent i stedet for lokale innloggingslÃ¸sninger. ID-porten er sÃ¦rlig relevant nÃ¥r en tjeneste trenger sikker identitetsbekreftelse av en bruker, og nÃ¥r samme innloggingsmÃ¸nster skal gjenbrukes pÃ¥ tvers av mange offentlige tjenester.

## Kapabiliteter
- **Tillit: Autentisering** verifiserer brukerens identitet gjennom godkjente eID-er og gir et felles sikkerhetsnivÃ¥ pÃ¥ tvers av offentlige tjenester.
- **Tillit: Identifisering** kobler innloggingen til en entydig digital identitet som tjenesteeier kan bruke videre i sin saks- og tjenestelogikk.
- **Tillit: Representasjon** stÃ¸tter innlogging i bruker-kontekst ogsÃ¥ nÃ¥r en innbygger handler med valgt virksomhet eller i delegert kontekst, i samspill med andre tillitstjenester og representasjonsgrunnlag.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter innloggingsflyt, tokenutstedelse og overfÃ¸ring av identitetsinformasjon mellom ID-porten og tjenesteeier.
- **Tjenesteutvikling: Integrerbare tjenester** gjÃ¸r autentisering gjenbrukbar gjennom standardiserte grensesnitt og dokumenterte integrasjonsmÃ¸nstre.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i Digdir Docs, Digdirs produktside og Samarbeidsportalen.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Digdirs produktside for ID-porten og Samarbeidsportalen for tillitstjenester.

Dokumenterte mÃ¥l:
- Sikre identifisering og autentisering for digitale tjenester for bÃ¥de virksomheter og innbyggere.
- Tilby en nasjonal innloggingslÃ¸sning som kan gjenbrukes pÃ¥ tvers av offentlig sektor.
- Gi sikker og enkel bruk av offentlige tjenester gjennom stÃ¸tte for anerkjente eID-er.
- Videreutvikle lÃ¸sningen slik at den blir sikker som standard, enklere Ã¥ bruke og bedre tilpasset moderne API-behov.

Operative mÃ¥l utledet fra de samme kildene:
- Redusere behovet for lokale autentiseringslÃ¸sninger hos tjenesteeiere.
- Gi tjenesteeiere tydelige integrasjonslÃ¸p for test, produksjon og videre forvaltning.
- Sikre at brukerinnlogging og identitetsinformasjon kan brukes i bÃ¥de nettjenester og API-er i bruker-kontekst.

**Deduksjon:** Produktet har ogsÃ¥ en viktig styringsrolle som normerende lÃ¸sning for brukervendt autentisering i staten, fordi bruk av ID-porten er hovedregelen nÃ¥r statlige tjenester trenger innlogging.

## Brukerbehov
- Innbyggere trenger en trygg og gjenkjennelig mÃ¥te Ã¥ logge inn pÃ¥ offentlige tjenester uten Ã¥ mÃ¸te ulike lokale autentiseringslÃ¸sninger.
- Tjenesteeiere trenger en felles innloggingskomponent som er juridisk, sikkerhetsmessig og teknisk innarbeidet.
- Integrasjonsteam trenger standardiserte protokoller og tydelig dokumentasjon for Ã¥ koble egne tjenester til nasjonal autentisering.
- Tjenester med bruker-kontekst i API-er trenger tilgangstoken og identitetsinformasjon som kan brukes videre i egne tjenester.
- Tjenester der brukeren opptrer i en virksomhetskontekst trenger stÃ¸tte for innlogging med valgt virksomhet eller delegert sammenheng.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Innbyggere | Enkel og sikker innlogging | Tilgang til offentlige nettjenester | MÃ¸ter ID-porten som del av tjenestens innloggingsflyt |
| Tjenesteeiere i offentlig sektor | Felles autentiseringskomponent | Innlogging i egne tjenester og portaler | Statlige virksomheter skal som hovedregel bruke ID-porten nÃ¥r innlogging trengs |
| Integrasjonsteam og systemleverandÃ¸rer | Standardiserte grensesnitt og testlÃ¸p | Integrasjon via OpenID Connect, OAuth 2.0 og eventuelt SAML | Trenger dokumentasjon, testmiljÃ¸ og avtaleprosess |
| API- og plattformteam | Bruker-kontekst i API-er | Tokenutstedelse og validering i egne lÃ¸sninger | Relevante der autentisert bruker skal brukes videre i API-kall |
| Forvaltnings- og sikkerhetsmiljÃ¸er | Sporbar og styrbar autentiseringslÃ¸sning | RisikooppfÃ¸lging, tilgangsregimer og livssyklus | Avhenger av tydelig rollefordeling og leverandÃ¸rsamspill |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- **Sikker innlogging for innbyggere til offentlige tjenester.** ID-porten hÃ¥ndterer selve autentiseringen og lar brukeren logge inn med stÃ¸ttede eID-er som BankID, Buypass og Commfides. Dette dekker behovet for en felles, nasjonal innloggingsmekanisme nÃ¥r en offentlig tjeneste trenger Ã¥ vite hvem brukeren er.
- **Standardisert integrasjon for tjenesteeiere.** Produktet tilbyr dokumenterte integrasjonsmÃ¸nstre med OpenID Connect som anbefalt lÃ¸sning, og stÃ¸tter ogsÃ¥ SAML for eldre eller eksisterende integrasjoner. Dette gjÃ¸r at tjenesteeiere kan gjenbruke etablerte sikkerhetsmÃ¸nstre i stedet for Ã¥ bygge autentisering selv.
- **Token- og identitetsgrunnlag for videre bruk i tjenestelogikk.** ID-porten utsteder grunnlaget tjenesteeier trenger for Ã¥ kjenne igjen brukeren i egne lÃ¸sninger og, ved behov, for Ã¥ bruke autentisert bruker-kontekst videre i API-er. Dette er viktig for tjenester som ikke bare trenger en innloggingsknapp, men ogsÃ¥ sikker videre bruk av identiteten i egne prosesser.
- **StÃ¸tte for bruker-kontekst i virksomhetssammenheng.** Dokumentasjonen viser at ID-porten kan brukes i scenarier der en innbygger opptrer med valgt virksomhet. Dette gjÃ¸r lÃ¸sningen relevant i grenseflaten mellom personinnlogging og handling pÃ¥ vegne av virksomhet, men ikke som full erstatning for egne autorisasjons- og representasjonslÃ¸sninger.
- **Kontrollert innfÃ¸ring og forvaltning.** Tjenesteeiere fÃ¥r stÃ¸tte gjennom avtale, testmiljÃ¸ og produksjonssetting. Det gjÃ¸r produktet egnet som nasjonal felleskomponent ogsÃ¥ organisatorisk, ikke bare teknisk.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Autentisering av brukere mot offentlige tjenester | Full autorisasjon til faglige ressurser i hver enkelt tjeneste |
| Standardiserte integrasjoner for innlogging | Maskin-til-maskin-autentisering uten bruker-kontekst |
| Token- og identitetsgrunnlag for videre bruk hos tjenesteeier | Signering av dokumenter eller transaksjoner |
| StÃ¸tte for bruker-kontekst i enkelte virksomhetsscenarier | Fagspesifikk tilgangsstyring og vedtak om rettigheter |
| Test, avtale og produksjonslÃ¸p for tilkobling | Erstatning for alle andre tillitstjenester i Digdir-portefÃ¸ljen |

## Veikart over kommende funksjonalitet
**Fakta fra Samarbeidsportalen og Digdir Docs (hentet 2026-03-17):**
- Viktige fokusomrÃ¥der for de kommende Ã¥rene er bedre stÃ¸tte for alle typer API-er med bruker-kontekst, tett samarbeid med leverandÃ¸rmarkedet, sikkerhet som standard og sÃ¸mlÃ¸s brukeropplevelse.
- Digdir peker ogsÃ¥ pÃ¥ behov for enklere og mer fleksibel integrasjon for tjenesteeiere.

**Deduksjon:** Veikartet peker mot videre modernisering av ID-porten som plattform for brukerautentisering i API-drevne tjenester, ikke bare klassiske nettbaserte innloggingslÃ¸p.

## Forretningsverdi/Verdiforslag
### For innbyggere
- Gir en gjenkjennelig og trygg innloggingsopplevelse pÃ¥ tvers av offentlige tjenester.
- Reduserer friksjon ved at brukeren kan forholde seg til kjente eID-er i stedet for ulike lokale lÃ¸sninger.

### For tjenesteeiere
- Reduserer behovet for Ã¥ etablere og forvalte egen autentiseringslÃ¸sning.
- Gir raskere vei til sikker produksjonssetting gjennom etablerte protokoller, testmiljÃ¸ og felles forvaltning.
- Senker risiko ved at autentisering hÃ¥ndteres av en nasjonal felleslÃ¸sning med tydelig sikkerhets- og styringsregime.

### For offentlig sektor og Ã¸kosystemet
- Styrker gjenbruk ved at mange tjenester kan bygge pÃ¥ samme autentiseringsmÃ¸nster.
- Bidrar til mer konsistent brukeropplevelse og mindre fragmentert identitetsforvaltning pÃ¥ tvers av sektorer.
- UnderstÃ¸tter nasjonal styring av tillitstjenester og samhandling.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Feil bruk av autentiseringsnivÃ¥ eller identitetsgrunnlag i tjenesteeiers egen lÃ¸sning | Tydelig veiledning, krav til tjenesteeier og riktig valg av sikkerhetsnivÃ¥ |
| Teknisk | Feil i integrasjon hos tjenesteeier kan gi avbrutt innlogging eller feil hÃ¥ndtering av token | TestmiljÃ¸, dokumenterte integrasjonsmÃ¸nstre og validering fÃ¸r produksjon |
| Sikkerhet | Phishing, feilkonfigurasjon eller svak implementasjon i klientlÃ¸sningen kan svekke sikkerheten i hele brukerreisen | Sikkerhet som standard, anbefalte protokoller og tydelig leverandÃ¸rveiledning |
| LeverandÃ¸r og Ã¸kosystem | Avhengighet til eID-leverandÃ¸rer og tilpasning hos markedet kan pÃ¥virke brukeropplevelse og fremdrift | Samarbeid med leverandÃ¸rmarkedet og flere stÃ¸ttede eID-er |
| Brukeropplevelse | Innloggingsopplevelsen kan oppleves som tung hvis tjenesteeier velger feil flyt eller dÃ¥rlig kontekstskifte | Mer sÃ¸mlÃ¸se integrasjoner og tydeligere mÃ¸nstre for tjenestedesign |

## Kanaler
- Produktside: https://www.digdir.no/id-porten/om-id-porten/1507
- Teknisk dokumentasjon: https://docs.digdir.no/docs/idporten/
- Samarbeidsportal: https://samarbeid.digdir.no/id-porten/tillitstenester/2479
- Ta i bruk: https://samarbeid.digdir.no/id-porten/ta-i-bruk-id-porten/477
- Prismodell: https://samarbeid.digdir.no/id-porten/id-portens-prismodell/78

## Plattform
ID-porten er en nasjonal autentiseringsplattform bygget rundt fÃ¸derering mot eksterne eID-er og standardiserte integrasjonsgrensesnitt mot tjenesteeiere.

**Fakta:** Digdir anbefaler OpenID Connect for nye integrasjoner, stÃ¸tter SAML for eksisterende bruk, og tilbyr API-stÃ¸tte for bruk av ID-porten i bruker-kontekst.

**Ikke offentlig dokumentert i brukte kilder:** Full runtime-arkitektur, detaljert driftsplattform og konkret skylokasjon.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet er laget nettopp for Ã¥ vÃ¦re en felles innloggingskomponent pÃ¥ tvers av mange tjenester.
- Gjenbruket er organisatorisk sÃ¥ vel som teknisk, fordi bÃ¥de avtaleprosess, testlÃ¸p og dokumentasjon er standardisert.
- ID-porten er sÃ¦rlig relevant nÃ¥r behovet er brukervendt autentisering. Den er mindre relevant dersom behovet egentlig er maskin-til-maskin-autentisering eller fagspesifikk autorisasjon, der andre produkter er mer treffende.

## StÃ¸tter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov** gir en gjenkjennelig innloggingsopplevelse pÃ¥ tvers av tjenester.
- **P5: Del og gjenbruk lÃ¸sninger** er en kjerneegenskap, fordi autentisering tilbys som nasjonal felleskomponent i stedet for lokale sÃ¦rvarianter.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** gjÃ¸r det mulig for mange virksomheter Ã¥ samhandle om samme identitetsgrunnlag og integrasjonsmÃ¸nster.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** er sentralt fordi produktet etablerer grunnlaget for sikker identifisering og innlogging.

## Finansiering
- **Fakta:** Samarbeidsportalen beskriver en prismodell med Ã¥rlig fastavgift for bruk av ID-porten.
- **Fakta:** Enkelte kostnadselementer, som bruk av utenlandske eID-er, belastes den enkelte tjenesteeier.
- **Deduksjon:** Finansieringsmodellen er derfor ikke ren sentral gratisbruk for alle, men en kombinasjon av nasjonal forvaltning og kostnader knyttet til bruk og integrasjon.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Digdirs produktside og Samarbeidsportalen |
| Driftsansvar | Ikke eksplisitt navngitt i brukte offentlige kilder | Offentlige kilder bekrefter ikke detaljert leverandÃ¸r- eller driftsmodell |
| Budsjett- og prismodell | Digdir forvalter produktet, med dokumentert prismodell for bruk | Samarbeidsportalen |
| Styringsmodell | Del av produktomrÃ¥det for tillitstjenester | Samarbeidsportalen |

## Lenke til dokumentasjon
- https://www.digdir.no/id-porten/om-id-porten/1507
- https://docs.digdir.no/docs/idporten/
- https://samarbeid.digdir.no/id-porten/tillitstenester/2479
- https://samarbeid.digdir.no/id-porten/ta-i-bruk-id-porten/477
- https://samarbeid.digdir.no/id-porten/id-portens-prismodell/78

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `results/Produktbeskrivelser/01-ID-porten-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
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
- Finansiering er korrigert fra antatt gratis bruk til dokumentert prismodell med Ã¥rlig fastavgift og enkelte brukeravhengige kostnader.
- Funksjonsbeskrivelsen er strammet inn slik at ID-porten beskrives som autentiserings- og tokenlÃ¸sning, ikke som generell autorisasjonskomponent.
- Veikartet er oppdatert med dokumenterte fokusomrÃ¥der fra Samarbeidsportalen i stedet for antatte fremtidstemaer.
- Forvaltning og drift er skilt tydeligere, og ikke-offentlig dokumenterte forhold er markert som slike i stedet for Ã¥ bli fylt med antakelser.

### Tekstlige forbedringer
- Brukersegmenter, hovedfunksjoner og avgrensning er skrevet om til en mer selvstendig produktbeskrivelse for mÃ¥lgruppen.
- Kapabiliteter er redusert til de som er best dokumentert og forklart med tydeligere sammenheng til produktets faktiske rolle.
- Gjenbruksvurderingen skiller tydeligere mellom nÃ¥r ID-porten er riktig lÃ¸sning, og nÃ¥r andre tillitstjenester er mer relevante.
