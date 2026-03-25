# Produkt-canvas: Fiks register

## Navn
Fiks register

## Ressurs ID
KS-004

## Status/Livsfase
**Produksjon** - etablert oppslags- og tilgangstjeneste for nasjonale registre i kommunal sektor.

**Fakta:** KS beskriver FIKS Register som en samling av nasjonale registre som kommuner og fylkeskommuner kan slå opp i via Fiks forvaltning eller gjennom integrasjon mot fagsystem.

## Modenhet
**Middels til høy funksjonell modenhet** - tjenesten har et tydelig formål og konkrete registerløp i drift, men er avgrenset til tilgang og oppslag snarere enn full registerforvaltning.
- Produktsiden viser konkrete registertilbud som skatte- og inntektsopplysninger, folkeregister og kjøretøyregister.
- Modenheten er høy for selve oppslagsmønsteret, men avhenger også av de underliggende nasjonale datakildene og tilgangsvilkårene derfra.

**Deduksjon:** Produktet er modent som tilgangslag til registre, men ikke et eget register i samme betydning som de autoritative kildene det gir tilgang til.

## Kort beskrivelse
FIKS Register er KS Digitals fellestjeneste for oppslag i nasjonale registre fra kommunal sektor. Løsningen gjør det mulig å bruke samme tilgangs- og integrasjonsmønster mot flere datakilder, slik at kommuner og fylkeskommuner kan hente opplysninger i egne arbeidsprosesser uten å etablere separate løsninger for hvert register. Produktet er særlig relevant når kommunal sektor trenger kontrollert og forenklet tilgang til nasjonale grunndata gjennom fagsystemer eller forvaltningsgrensesnitt.

## Kapabiliteter
- **Datakilder: Grunndata** er relevant fordi løsningen brukes for oppslag i nasjonale registre og gjør autoritative datakilder anvendbare i kommunale prosesser.
- **Datautveksling og integrasjon: Bruke data fra andre** er kjernefunksjonen fordi produktet gir kommuner og fylkeskommuner et standardisert løp for å hente data fra andre virksomheters registre.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals kilder brukt i denne arbeidsøkten.

## Produktmål
Dokumenterte mål:
- Gi kommuner og fylkeskommuner tilgang til nasjonale registre via Fiks forvaltning eller integrasjon.
- Samle flere registertilganger i samme tjenestegrunnlag.

Operative mål utledet fra kildene:
- Forenkle bruk av nasjonale registerdata i kommunale fagsystemer.
- Redusere behovet for separate tilkoblinger mot hvert enkelt register.
- Gjøre tilgang til grunndata mer forutsigbar og lettere å forvalte i kommunal sektor.

## Brukerbehov
- Kommuner trenger enkel tilgang til oppdaterte nasjonale registeropplysninger.
- Fagsystemer trenger standardiserte integrasjoner mot sentrale datakilder.
- Kommunal sektor trenger mindre fragmentert tilgang til registre som forvaltes av andre virksomheter.
- Forvaltere trenger ett sted å administrere og forstå hvilke registertilganger som er tilgjengelige.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Tilgang til nasjonale registeropplysninger | Oppslag i registre via forvaltning eller integrasjon | Primær målgruppe |
| Fagsystemer og leverandører | Maskinell tilgang til registerdata | Integrasjon mot registertjenester i kommunale arbeidsprosesser | Viktige for effektiv bruk |
| Forvaltere i kommunal sektor | Oversikt over tilgjengelige registerløp og oppsett | Administrasjon og tilgangsstyring | Bruker forvaltningsgrensesnittet |
| KS Digital | Forvalte registertilgangstjenesten og koordinere samhandlingen mot eksterne datakilder | Produktforvaltning og videreutvikling | Tjenesteforvalter |

## Hovedfunksjoner
### Primære funksjoner
- FIKS Register samler flere registertilganger i én fellestjeneste. Dette gjør løsningen relevant når kommunen trenger tilgang til flere nasjonale datakilder, men ønsker et mer samlet tilkoblingsmønster.
- Tjenesten kan brukes både via Fiks forvaltning og gjennom integrasjon mot fagsystem. Det skiller produktet fra en ren administrativ portal, fordi det også er laget for operativ bruk i lokale systemer.
- Produktet gir tilgang til konkrete registerløp, blant annet skatte- og inntektsopplysninger, folkeregister og kjøretøyregister. Løsningen fungerer derfor som et tilgangslag til grunndata, ikke som registereier for selve dataene.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Oppslag i nasjonale registre via ett felles tjenestelag | Eierskap til de underliggende registrene |
| Integrasjon mot fagsystemer og bruk via Fiks forvaltning | Full lokal datalagring og forvaltning av registerdata |
| Samlet tilgang til flere registerløp | Full informasjonsforvaltning av kildedataene |
| Kommunal bruk av nasjonale grunndata | Registerproduksjon eller selvstendig datakilde |

## Veikart over kommende funksjonalitet
**Fakta:** Produktsiden viser flere konkrete registerløp og peker til løpende informasjon om tjenestene i løsningen. Jeg fant ikke et samlet offentlig roadmap med tidsfestede milepæler i denne arbeidsøkten.

**Deduksjon:** Videreutviklingen vil trolig handle om flere registerkoblinger og mer standardisert tilgang til delte data for kommunal sektor.

## Forretningsverdi/Verdiforslag
### For kommuner og fylkeskommuner
- Gjør nasjonale registeropplysninger lettere tilgjengelige i kommunale arbeidsprosesser.
- Reduserer behovet for å etablere og forvalte mange ulike registertilkoblinger.

### For leverandører
- Gir et mer samlet integrasjonspunkt mot kommunal bruk av registerdata.

### For sektoren
- Støtter mer ensartet bruk av nasjonale grunndata i kommunal sektor.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Tilgang til registerdata krever korrekt hjemmel og riktig bruk i lokale prosesser. | Tydelig tilgangsstyring og kobling til de underliggende datatilbydernes vilkår. |
| Teknisk | Feil i integrasjon eller endringer hos underliggende datakilder kan påvirke flere kommuner samtidig. | Robust endringshåndtering og tydelig dokumentasjon av registerløpene. |
| Sikkerhet | Registerdata kan være sensitive eller underlagt strenge tilgangskrav. | Streng autentisering, autorisasjon og logging av bruk. |
| Leverandør | Kommunene blir avhengige av et felles tilgangslag for registerbruk. | God dokumentasjon og tydelig forvaltning av avhengigheter. |
| Brukeropplevelse | Verdien svekkes hvis oppslag ikke er godt integrert i fagsystemene. | Fokus på gode integrasjoner og tydelige oppslagsmønstre. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-register/
- https://forvaltning.fiks.ks.no/
- https://status.fiks.ks.no

## Plattform
FIKS Register er en fellestjeneste på KS Digitals FIKS-grunnlag, brukt for oppslag og tilgang til nasjonale registerdata.

**Fakta:**
- Tjenesten kan brukes via forvaltningsflate eller gjennom integrasjon mot fagsystem.
- Den samler tilgang til flere ulike nasjonale registre i samme produktområde.

**Ikke offentlig dokumentert i brukte kilder:** Full teknisk driftsarkitektur og detaljert implementasjonsmodell per registerløp.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme tjenestegrunnlag kan brukes av mange kommuner og fylkeskommuner.
- Gjenbruksverdien ligger i samlet tilgangsmønster og felles integrasjon mot flere registre, ikke i at produktet selv eier dataene.

## Støtter arkitekturprinsipper
- **P4 Del og gjenbruk data** - produktet gjør det enklere for kommunal sektor å bruke delte registerdata fra andre virksomheter.
- **P6 Lag digitale løsninger som støtter samhandling** - produktet gir et mer standardisert samhandlingsmønster for registeroppslag på tvers av aktører.

## Finansiering
**Ikke offentlig detaljert dokumentert i brukte kilder:** Jeg fant ikke full finansieringsmodell for FIKS Register i denne arbeidsøkten.

**Deduksjon:** Tjenesten inngår i KS Digitals fellestjenesteportefølje og må vurderes nærmere mot avtale- og prismodell for kommunal sektor.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsiden og tjenesteplasseringen ligger hos KS Digital. |
| Driftsansvar | Ikke offentlig spesifisert i brukte kilder | Må verifiseres i tekniske eller kontraktsnære kilder. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Krever egne styrings- eller prismodellkilder. |
| Styringsmodell | KS Digital som felles forvalter av tilgangstjenesten | Fremgår av produktsiden og tjenesteporteføljen. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-register/
- https://forvaltning.fiks.ks.no/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/ (hentet 2026-03-18)
