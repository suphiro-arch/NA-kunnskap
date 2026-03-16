# Produkt-canvas: Dialogporten

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Dialogporten

## Ressurs ID
22 (Produktliste NA-kunnskap).
## Status/Livsfase
Produksjon med aktiv videreutvikling og migrering fra eldre løsninger.

## Modenhet
Middels til høy:
- Produktet er i ordinert bruk og har tydelig API- og integrasjonsmodell.
- Funksjonalitet og referansedokumentasjon er etablert (OpenAPI, GraphQL, entiteter, hendelser).
- Migrering fra Altinn 2/eldre data innebærer fortsatt endrings- og overgangsarbeid.

## Kort beskrivelse
Dialogporten er Altinns felles representasjons- og samhandlingslag for digitale dialoger mellom offentlig sektor og sluttbrukere. Produktet samler dialoger/meldinger på tvers av tjenesteplattformer i et felles format, slik at samme dialog kan gjenbrukes i arbeidsflate, portaler og sluttbrukersystemer.

## Kapabiliteter
- Samhandling og sammenhengende tjenester: felles metadataformat for dialoger på tvers av plattformer.
- Datautveksling og integrasjon: standardiserte API-er for oppslag, oppdatering og hendelser.
- Tillit og tilgangsstyring: integrasjon med Altinn Autorisasjon, ID-porten og Maskinporten.
- Hendelsesdrevet arkitektur: integrasjon med Altinn Events (pub/sub og endringsdeteksjon).
- Brukeropplevelse: enhetlig visning av kommunikasjon i arbeidsflater og eksterne sluttbrukersystemer.

## Produktmål
- Etablere ett felles dialogformat for offentlig digital kommunikasjon.
- Redusere behov for plattformspesifikke integrasjoner hos tjenesteeiere og EUS-leverandører.
- Forbedre brukeropplevelse gjennom samlet oversikt over dialoger.
- Understøtte overgang fra Altinn 2 til Altinn 3 med kontrollert migrering.

## Brukerbehov
- Offentlige virksomheter trenger en felles måte å eksponere dialoger og meldinger på.
- Sluttbrukersystemer trenger stabile, standardiserte grensesnitt for konsum av dialogdata.
- Sluttbrukere trenger samlet oversikt og konsistent presentasjon av kommunikasjon med offentlig sektor.

## Hvem er brukerne og brukersegmentene
- Tjenesteeiere i offentlig sektor (Altinn Studio og andre plattformer).
- Leverandører av sluttbrukersystemer (EUS).
- Innbyggere, virksomheter og representanter med behov for innsyn i dialoghistorikk.
- Arkitektur- og integrasjonsteam som bygger sammenhengende tjenester.

## Hovedfunksjoner
- Dialog som felles meta-representasjon uavhengig av underliggende plattform.
- API-er for sok, henting og oppdatering av dialoger.
- Hendelsesstrømmer for oppdagelse av endringer og asynkron integrasjon.
- Støtte for aktivitetslogg/sett-logg og relaterte entiteter.
- Front channel-embeds og klientstøtte for presentasjon i brukerflater.

### Scope og avgrensning
- Inngår:
  - metadata og livssyklusinformasjon for dialoger
  - felles API-lag og hendelsesintegrasjon
  - samspill med autorisasjon og arbeidsflate
- Inngår ikke:
  - full forretningslogikk i hver enkelt sektortjeneste
  - lokal saksbehandling i avsendervirksomhetens fagsystem

## Veikart over kommende funksjonalitet
- Kontinuerlig migrering av data/funksjon fra Altinn 2/eldre løsninger.
- Videreutvikling av referansemodeller, API-er og integrasjonsmønstre.
- Basert på dokumentasjonen må detaljert roadmap bekreftes løpende i produktets nyhets- og statussider.

## Forretningsverdi/Verdiforslag
- Lavere integrasjonskostnader gjennom standardisert dialogmodell.
- Raskere etablering av nye tjenester som må eksponere meldinger/dialoger.
- Bedre sammenheng i brukerreiser på tvers av offentlige aktører.
- Mindre duplisering av sensitiv informasjon ved at data i storre grad forvaltes når kilden.

## Utfordringer og risiko
- Migreringsrisiko knyttet til datakvalitet, semantikk og kompatibilitet fra eldre løsninger.
- Avhengighet til underliggende fellestjenester (autorisasjon, events, autentisering).
- Organisatorisk risiko ved uens implementering hos ulike tjenesteeiere.
- Endringsrisiko for integratorer ved versjonsutvikling i API-er/modeller.

## Kanaler
- API-er (OpenAPI, GraphQL).
- Altinn arbeidsflate/portalnære flater.
- Sluttbrukersystemer og tredjepartsportaler via integrasjon.

## Plattform
Skybasert nasjonal fellestjeneste i Altinn-økosystemet.
Noyaktig driftsmodell/lokasjon er ikke detaljert i kilder brukt her.

## Gjenbruk
Høy gjenbruksverdi:
- felles dialogmodell på tvers av sektorer
- standardiserte integrasjonspunkter
- reduserer behov for proprietære punkt-til-punkt-integrasjoner

## Støtte arkitekturprinsipper
Vurderes som sterk på:
- deling og gjenbruk av felleskomponenter
- løs kobling via API-er og hendelser
- standardisering av informasjonsutveksling
- innebygd sikkerhet gjennom tillitsinfrastruktur

## Finansiering
Ikke eksplisitt spesifisert i kildene brukt her.
Forutsettes forvaltet som nasjonal fellestjeneste med offentlig finansieringsmodell.

## Forvaltning/eier
Ma verifiseres mot formell styringsdokumentasjon:
- Produktansvar: Altinn-forvaltningen
- Driftsansvar: Altinn-forvaltningen
- Budsjettansvar: Usikkert i offentlig detaljnivå
- Styringsmodell: Nasjonal forvaltning av fellesløsning

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/dialogporten/
- https://docs.altinn.studio/nb/dialogporten/what-do-you-get/
- https://docs.altinn.studio/nb/dialogporten/reference/openapi/
- https://docs.altinn.studio/nb/dialogporten/reference/graphql/

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Nettkilder: Altinn Docs (hentet 2026-03-06)

