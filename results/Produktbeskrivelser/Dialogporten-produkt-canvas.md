# Produkt-canvas: Dialogporten

Maalgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Dialogporten

## Ressurs ID
22 (Produktliste NA-kunnskap).
## Status/Livsfase
Produksjon med aktiv videreutvikling og migrering fra eldre loesninger.

## Modenhet
Middels til hoy:
- Produktet er i ordinert bruk og har tydelig API- og integrasjonsmodell.
- Funksjonalitet og referansedokumentasjon er etablert (OpenAPI, GraphQL, entiteter, hendelser).
- Migrering fra Altinn 2/eldre data innebaar fortsatt endrings- og overgangsarbeid.

## Kort beskrivelse
Dialogporten er Altinns felles representasjons- og samhandlingslag for digitale dialoger mellom offentlig sektor og sluttbrukere. Produktet samler dialoger/meldinger paa tvers av tjenesteplattformer i et felles format, slik at samme dialog kan gjenbrukes i arbeidsflate, portaler og sluttbrukersystemer.

## Kapabiliteter
- Samhandling og sammenhengende tjenester: felles metadataformat for dialoger paa tvers av plattformer.
- Datautveksling og integrasjon: standardiserte API-er for oppslag, oppdatering og hendelser.
- Tillit og tilgangsstyring: integrasjon med Altinn Autorisasjon, ID-porten og Maskinporten.
- Hendelsesdrevet arkitektur: integrasjon med Altinn Events (pub/sub og endringsdeteksjon).
- Brukeropplevelse: enhetlig visning av kommunikasjon i arbeidsflater og eksterne sluttbrukersystemer.

## Produktmaal
- Etablere ett felles dialogformat for offentlig digital kommunikasjon.
- Redusere behov for plattformspesifikke integrasjoner hos tjenesteeiere og EUS-leverandoerer.
- Forbedre brukeropplevelse gjennom samlet oversikt over dialoger.
- Understoette overgang fra Altinn 2 til Altinn 3 med kontrollert migrering.

## Brukerbehov
- Offentlige virksomheter trenger en felles maate aa eksponere dialoger og meldinger paa.
- Sluttbrukersystemer trenger stabile, standardiserte grensesnitt for konsum av dialogdata.
- Sluttbrukere trenger samlet oversikt og konsistent presentasjon av kommunikasjon med offentlig sektor.

## Hvem er brukerne og brukersegmentene
- Tjenesteeiere i offentlig sektor (Altinn Studio og andre plattformer).
- Leverandoerer av sluttbrukersystemer (EUS).
- Innbyggere, virksomheter og representanter med behov for innsyn i dialoghistorikk.
- Arkitektur- og integrasjonsteam som bygger sammenhengende tjenester.

## Hovedfunksjoner
- Dialog som felles meta-representasjon uavhengig av underliggende plattform.
- API-er for sok, henting og oppdatering av dialoger.
- Hendelsesstroemmer for oppdagelse av endringer og asynkron integrasjon.
- Stotte for aktivitetslogg/sett-logg og relaterte entiteter.
- Front channel-embeds og klientstoette for presentasjon i brukerflater.

### Scope og avgrensning
- Inngaar:
  - metadata og livssyklusinformasjon for dialoger
  - felles API-lag og hendelsesintegrasjon
  - samspill med autorisasjon og arbeidsflate
- Inngaar ikke:
  - full forretningslogikk i hver enkelt sektortjeneste
  - lokal saksbehandling i avsendervirksomhetens fagsystem

## Veikart over kommende funksjonalitet
- Kontinuerlig migrering av data/funksjon fra Altinn 2/eldre loesninger.
- Videreutvikling av referansemodeller, API-er og integrasjonsmoenstre.
- Basert paa dokumentasjonen maa detaljert roadmap bekreftes loepende i produktets nyhets- og statussider.

## Forretningsverdi/Verdiforslag
- Lavere integrasjonskostnader gjennom standardisert dialogmodell.
- Raskere etablering av nye tjenester som maa eksponere meldinger/dialoger.
- Bedre sammenheng i brukerreiser paa tvers av offentlige aktorer.
- Mindre duplisering av sensitiv informasjon ved at data i storre grad forvaltes naer kilden.

## Utfordringer og risiko
- Migreringsrisiko knyttet til datakvalitet, semantikk og kompatibilitet fra eldre loesninger.
- Avhengighet til underliggende fellestjenester (autorisasjon, events, autentisering).
- Organisatorisk risiko ved uens implementering hos ulike tjenesteeiere.
- Endringsrisiko for integratorer ved versjonsutvikling i API-er/modeller.

## Kanaler
- API-er (OpenAPI, GraphQL).
- Altinn arbeidsflate/portalnaere flater.
- Sluttbrukersystemer og tredjepartsportaler via integrasjon.

## Plattform
Skybasert nasjonal fellestjeneste i Altinn-oekosystemet.
Noyaktig driftsmodell/lokasjon er ikke detaljert i kilder brukt her.

## Gjenbruk
Hoy gjenbruksverdi:
- felles dialogmodell paa tvers av sektorer
- standardiserte integrasjonspunkter
- reduserer behov for proprietaere punkt-til-punkt-integrasjoner

## Stoette arkitekturprinsipper
Vurderes som sterk paa:
- deling og gjenbruk av felleskomponenter
- loes kobling via API-er og hendelser
- standardisering av informasjonsutveksling
- innebygd sikkerhet gjennom tillitsinfrastruktur

## Finansiering
Ikke eksplisitt spesifisert i kildene brukt her.
Forutsettes forvaltet som nasjonal fellestjeneste med offentlig finansieringsmodell.

## Forvaltning/eier
Ma verifiseres mot formell styringsdokumentasjon:
- Produktansvar: Altinn-forvaltningen
- Driftsansvar: Altinn-forvaltningen
- Budsjettansvar: Usikkert i offentlig detaljnivaa
- Styringsmodell: Nasjonal forvaltning av felleslosning

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/dialogporten/
- https://docs.altinn.studio/nb/dialogporten/what-do-you-get/
- https://docs.altinn.studio/nb/dialogporten/reference/openapi/
- https://docs.altinn.studio/nb/dialogporten/reference/graphql/

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Nettkilder: Altinn Docs (hentet 2026-03-06)

