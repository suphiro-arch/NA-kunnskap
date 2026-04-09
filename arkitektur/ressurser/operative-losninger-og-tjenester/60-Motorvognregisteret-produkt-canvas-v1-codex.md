# Produkt-canvas: Motorvognregisteret

## Navn
Motorvognregisteret

## Ressurs ID
SVV-001

## Status/Livsfase
**Produksjon** - etablert nasjonalt register for opplysninger om kjøretøy og tilknyttede forhold.

**Fakta:** Statens vegvesen tilbyr opplysninger om kjøretøy gjennom flere tjenester og API-er, og bruker i offentlig informasjon ofte betegnelsen kjøretøyopplysninger eller kjøretøyregisteret. I produktregisteret brukes her betegnelsen Motorvognregisteret som samlet ressursnavn.

## Modenhet
**Høy modenhet** - etablert sektorregister med bred operativ bruk og flere tilgjengeliggjøringsformer.

Produktet framstår som modent både som registerressurs og som datakilde for oppslag og deling. Offentlige kilder viser at opplysningene brukes gjennom flere kanaler, blant annet oppslagstjenester og API-er, noe som tilsier at løsningen ikke bare er et internt register, men en innarbeidet nasjonal kilde for kjøretøyinformasjon.

## Kort beskrivelse
Motorvognregisteret er den nasjonale registerressursen for grunnleggende opplysninger om kjøretøy og tilhørende forhold som Statens vegvesen gjør tilgjengelig gjennom oppslag og datatjenester. Produktet fungerer som en autoritativ kilde for tekniske kjøretøyopplysninger og utvalgte eierrelaterte opplysninger innenfor gjeldende vilkår, og brukes som grunnlag for kontroll, forvaltning, oppslag og videre datadeling.

## Kapabiliteter
- **Datakilder: Grunndata**
  Motorvognregisteret fungerer som nasjonal grunndatakilde for sentrale opplysninger om registrerte kjøretøy.
- **Datautveksling og integrasjon: Dele data med andre**
  Produktet gjør kjøretøyopplysninger tilgjengelige gjennom flere delings- og oppslagsformer for andre brukere og systemer.

## Produktmål
- være en autoritativ kilde for opplysninger om kjøretøy i Norge
- gjøre relevante kjøretøyopplysninger tilgjengelige for oppslag, kontroll og datadeling
- støtte forvaltningsprosesser, innbyggerbehov og maskinell bruk av kjøretøydata
- bidra til at flere aktører kan bruke samme grunnlag i stedet for lokale kopier og uensartede kilder

## Brukerbehov
- innbyggere og virksomheter trenger tilgang til korrekte opplysninger om kjøretøy
- offentlige og private aktører trenger et felles registergrunnlag for kontroll, oppslag og integrasjoner
- digitale tjenester trenger maskinelt tilgjengelige kjøretøydata for automatiserte prosesser
- forvaltningen trenger en autoritativ kilde som kan brukes på tvers av ulike arbeidsprosesser

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Innbyggere og virksomheter | Oppslag i kjøretøyopplysninger | Kontroll, kjøp, salg og generell informasjon | Tydelig offentlig brukergruppe |
| Offentlige aktører | Autoritative kjøretøydata | Forvaltning, kontroll og saksbehandling | Viktige gjenbrukere |
| Private systemleverandører og virksomheter | Maskinell tilgang til data | Integrasjoner, tjenester og automatiserte prosesser | Typiske API-brukere |
| Statens vegvesen | Registerforvaltning og tilgjengeliggjøring | Drift, kvalitet og videre deling | Produktforvalter |

## Hovedfunksjoner
Motorvognregisterets viktigste funksjon er å være den autoritative kilden for sentrale opplysninger om kjøretøy. Det omfatter blant annet tekniske opplysninger og andre grunnleggende registerdata som må kunne legges til grunn i oppslag, kontroll og videre bruk. Produktets verdi ligger derfor først og fremst i at mange aktører kan forholde seg til samme registergrunnlag.

Produktet har også en tydelig tilgjengeliggjøringsfunksjon. Statens vegvesen tilbyr opplysninger både gjennom brukerrettede oppslag og gjennom API-er for maskinell bruk. Det betyr at ressursen ikke bare er et internt register, men en registertilgangstjeneste med flere flater, der både manuelle og integrerte bruksmåter er en del av den operative rollen.

En viktig del av produktbildet er at ulike typer opplysninger gjøres tilgjengelige med ulike vilkår og avgrensninger. Offentlige kilder skiller blant annet mellom tekniske kjøretøyopplysninger og utvidede opplysninger som inkluderer eierinformasjon. Produktet må derfor forstås som en samlet registerressurs der dataeksponeringen varierer etter formål, tilgang og regelverk, ikke som én ensartet åpen datakilde.

Samtidig er Motorvognregisteret ikke hele økosystemet av tjenester rundt kjøretøyforvaltning. Lokale fagsystemer, saksbehandlingsløsninger, salgsprosesser og andre tjenester bruker eller bygger på registerdataene, men er ikke del av selve produktet. Registerets rolle er å være den nasjonale kilden og tilgjengeliggjøringsflaten for opplysningene, ikke å dekke alle arbeidsprosessene der kjøretøydata inngår.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Register over sentrale opplysninger om kjøretøy | Alle øvrige tjenester for kjøretøyforvaltning, salg og saksbehandling |
| Oppslag og deling av kjøretøydata gjennom tilgjengelige flater | Lokale fagsystemer hos brukervirksomheter |
| Tekniske kjøretøyopplysninger og utvalgte andre registeropplysninger | Hele tjenesteløpet rundt kjøretøy utenfor register- og delingsrollen |
| API-er og andre mekanismer for tilgjengeliggjøring av data | Enhver bruk av dataene i eksterne tjenester og applikasjoner |

## Veikart over kommende funksjonalitet
Ikke offentlig samlet verifisert i denne arbeidsøkten.

## Forretningsverdi/Verdiforslag
- gir én autoritativ kilde for kjøretøyopplysninger som kan brukes på tvers av mange behov og aktører
- gjør maskinell og manuell bruk av kjøretøydata enklere enn om hver aktør måtte etablere egne datagrunnlag
- styrker kvalitet og konsistens i kontroll, oppslag og integrasjoner
- reduserer risiko for ulike versjoner av samme kjøretøyinformasjon i forskjellige løsninger

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | feil i registeropplysninger kan påvirke mange oppslag og integrasjoner samtidig | tydelig registerforvaltning, kvalitetssikring og sporbar retting |
| Tilgang og regelverk | ulike typer data krever ulike vilkår og tilgangsnivåer | presise tilgangsregler, tydelig dokumentasjon og differensierte grensesnitt |
| Tilgjengelighet | driftsavvik kan påvirke både oppslagstjenester og maskinelle integrasjoner | robust drift, overvåkning og beredskap |
| Brukerforståelse | brukere kan misforstå hvilke opplysninger som er åpne, betingede eller begrensede | tydelig forklaring av datatyper, vilkår og avgrensninger |
| Avhengighet | mange tjenester kan bli sterkt avhengige av samme registerkilde | forutsigbar forvaltning og tydelig håndtering av endringer i grensesnitt og datatilbud |

## Kanaler
- https://www.vegvesen.no/kjoretoy/kjop-og-salg/kjoretoyopplysninger/om-utlevering-av-kjoretoyopplysninger/
- https://www.vegvesen.no/fag/teknologi/apne-data/et-utvalg-apne-data/api-for-tekniske-kjoretoyopplysninger/
- https://www.vegvesen.no/fag/teknologi/apne-data/et-utvalg-apne-data/api-for-tekniske-kjoretoyopplysninger-med-eierinformasjon/
- https://www.vegvesen.no/om-oss/om-organisasjonen/apne-data/et-utvalg-apne-data/api-for-kjoretoyopplysninger/

## Plattform
Motorvognregisteret er et nasjonalt register- og delingsprodukt for kjøretøyopplysninger.

## Gjenbruk
**Høy gjenbruksverdi** som nasjonal kilde for kjøretøydata i oppslag, kontroll og integrasjoner.

Produktet er særlig relevant når flere aktører trenger samme grunnlag om kjøretøy og det er viktig at opplysningene kommer fra en autoritativ kilde med tydelige delingsformer.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
- **P7: Sørg for tillit til oppgaveløsningen**

## Finansiering
Ikke offentlig samlet verifisert i denne arbeidsøkten.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Statens vegvesen | produktsidene |
| Registerforvaltning | Statens vegvesen | register- og API-kildene |

## Lenke til dokumentasjon
- https://www.vegvesen.no/kjoretoy/kjop-og-salg/kjoretoyopplysninger/om-utlevering-av-kjoretoyopplysninger/
- https://www.vegvesen.no/fag/teknologi/apne-data/et-utvalg-apne-data/api-for-tekniske-kjoretoyopplysninger/
- https://www.vegvesen.no/fag/teknologi/apne-data/et-utvalg-apne-data/api-for-tekniske-kjoretoyopplysninger-med-eierinformasjon/
- https://www.vegvesen.no/om-oss/om-organisasjonen/apne-data/et-utvalg-apne-data/api-for-kjoretoyopplysninger/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.vegvesen.no/kjoretoy/kjop-og-salg/kjoretoyopplysninger/om-utlevering-av-kjoretoyopplysninger/ (kontrollert 2026-03-27)
- Nettkilde: https://www.vegvesen.no/fag/teknologi/apne-data/et-utvalg-apne-data/api-for-tekniske-kjoretoyopplysninger/ (kontrollert 2026-03-27)
- Nettkilde: https://www.vegvesen.no/fag/teknologi/apne-data/et-utvalg-apne-data/api-for-tekniske-kjoretoyopplysninger-med-eierinformasjon/ (kontrollert 2026-03-27)
- Nettkilde: https://www.vegvesen.no/om-oss/om-organisasjonen/apne-data/et-utvalg-apne-data/api-for-kjoretoyopplysninger/ (kontrollert 2026-03-27)

## Endringer i denne revisjonen
- Opprettet manglende `v1`-fil for Motorvognregisteret og skrevet den på samme detaljeringsnivå som de sterkere produktbeskrivelsene
- Tydeliggjort at produktet består av både registerrolle, oppslag og API-basert tilgjengeliggjøring
- Presisert avgrensning mellom selve registerressursen og øvrige kjøretøytjenester og arbeidsprosesser


