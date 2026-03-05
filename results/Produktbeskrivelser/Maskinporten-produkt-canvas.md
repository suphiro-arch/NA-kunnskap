# Produkt-canvas: Maskinporten

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Maskinporten

## Ressurs ID
Usikkert: Ressurs-ID fra intern excel er ikke tilgjengelig i repoet.

## Status/Livsfase
Produksjon.

## Modenhet
Høy. Maskinporten er etablert nasjonal felleskomponent for maskin-til-maskin autentisering og autorisasjon i offentlig sektor.

## Kort beskrivelse
Maskinporten er en nasjonal tillits- og autorisasjonstjeneste for API-kall mellom virksomheter og systemer.

## Kapabiliteter
- Tillit: Autentisering
- Tillit: Tilgangsstyring
- Tillit: Tilgangskontroll
- Tillit: Sporbarhet og innsyn
- Datautveksling og integrasjon: Dele data med andre
- Datautveksling og integrasjon: Bruke data fra andre
- Tjenesteutvikling: Integrerbare tjenester

## Produktmål
- Standardisere sikker maskinell samhandling i offentlig sektor
- Redusere behov for proprietære punkt-til-punkt sikkerhetsløsninger
- Øke tempo i datadeling ved gjenbruk av felles tillitsinfrastruktur

## Brukerbehov
Virksomheter trenger en felles, sikker og skalerbar måte å autentisere systemkall og håndtere rettigheter mellom datatilbydere og datakonsumenter.

## Hvem er brukerne og brukersegmentene
- Offentlige virksomheter som datatilbydere
- Offentlige og private virksomheter som konsumenter av offentlige API-er
- Leverandører/integrasjonsteam som bygger API-klienter

## Hovedfunksjoner
- Klientautentisering for maskin-til-maskin trafikk
- Utstedelse/bruk av tokens for tilgang til API-er
- Støtte for delegert tilgang mellom aktører
- Integrasjon med API-økosystemer og tilgangskontroll

### Scope og avgrensning
- Inngår: maskinell autentisering/autorisasjon og tillit for API-tilgang
- Inngår ikke: sluttbrukerinnlogging (dekkes typisk av ID-porten)

## Veikart over kommende funksjonalitet
Usikkert i detalj: Ikke dokumentert konkret roadmap i repoet. Forventet retning er videreutvikling av sikkerhet, skalerbarhet og forenklet integrasjon.

## Forretningsverdi/Verdiforslag
- Raskere etablering av sikre API-samarbeid
- Lavere integrasjonskostnader gjennom felles mønster
- Økt etterlevelse av nasjonale prinsipper for samhandling og datadeling

## Utfordringer og risiko
- Feilkonfigurasjon av klienter/tilganger hos konsumenter
- Kompleksitet i fullmakter/delegering på tvers av virksomheter
- Avhengighet til sentral felleskomponent for kritisk integrasjonsflyt

## Kanaler
- Dokumentasjon og utviklerressurser via Digdir
- API-baserte integrasjoner i virksomhetenes egne løsninger

## Plattform
Forvaltet som nasjonal felleskomponent (detaljert plattforminformasjon ikke eksplisitt dokumentert i repoet).

## Gjenbruk
Høy gjenbruksverdi:
- Kan brukes bredt på tvers av API-er og sektorer
- Bidrar til standardisering av sikkerhetsmønster for maskinell samhandling

## Støtte arkitekturprinsipper
Støtter særlig:
- Gjenbruk av fellesløsninger
- Standardisering
- Sikkerhet og personvern ved datadeling

## Finansiering
Usikkert i detalj: Finansieringsmodell er ikke dokumentert i repoet.

## Forvaltning/eier
Indikasjon i kilder peker mot nasjonal forvaltning hos Digdir, men intern rollefordeling er ikke dokumentert her:
- Produktansvar: usikkert
- Driftsansvar: usikkert
- Budsjettansvar: usikkert
- Styringsmodell: usikkert

## Lenke til dokumentasjon
- https://www.digdir.no/om-tjenesten/maskinporten/1558
- https://docs.digdir.no/

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Lokal fil: `sources/test.md`
