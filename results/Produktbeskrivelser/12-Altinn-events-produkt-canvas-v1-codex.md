# Produkt-canvas: Altinn events

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn events

## Ressurs ID
12 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon med løpende videreutvikling av abonnementer, filtrering og hendelsesflyt.

## Modenhet
Høy:
- Etablert hendelsestjeneste i Altinn 3-økosystemet.
- Dokumentert API-modell og mønstre for publisering/abonnement.
- Brukes for løst koblet samhandling mellom tjenester og systemer.

## Kort beskrivelse
Altinn events er en nasjonal hendelsestjeneste som muliggjør publisering og konsum av hendelser når de inntreffer. Løsningen understøtter hendelsesdrevet arkitektur, der tjenester kan reagere raskt uten tett synkron avhengighet.

## Kapabiliteter
- Datautveksling og integrasjon: Hendelsesdrevet
- Datautveksling og integrasjon: Dele data med andre
- Datautveksling og integrasjon: Bruke data fra andre
- Sluttbrukertjenester: Proaktive tjenester
- Tjenesteutvikling: Integrerbare tjenester
- Informasjonsforvaltning: Oversikt over hendelser
- Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling

Grunnlag: kapabiliteter mappet mot `index/capabilities.yaml`.

## Produktmål
- Tilby felles infrastruktur for hendelsesdrevet samhandling i offentlig sektor.
- Redusere behov for polling og tett synkrone integrasjoner.
- Øke reaksjonsevne, automatisering og proaktiv tjenesteleveranse.
- Standardisere mønstre for hendelsesdeling på tvers av tjenester.

## Brukerbehov
- Tjenesteeiere trenger en robust måte å varsle andre systemer om endringer.
- Integrasjonsteam trenger standard API-er for abonnement, mottak og oppfølging.
- Virksomheter trenger nærmere sanntidsflyt for bedre beslutning og prosessautomatisering.

## Hvem er brukerne og brukersegmentene
- Offentlige virksomheter som publiserer hendelser.
- Offentlige/private aktører som abonnerer på hendelser.
- Integrasjonsteam, utviklere og plattformforvaltere.
- Analyse- og prosessmiljøer som bruker hendelser for innsikt og automatisering.

## Hovedfunksjoner
- Publisering av hendelser fra tjenester og systemer.
- Abonnementsmodell for mottakere.
- Filtrering/ruting av relevante hendelser.
- Integrasjon med øvrige Altinn-produkter og API-økosystem.
- Støtte for løst koblet, asynkron informasjonsflyt.

### Scope og avgrensning
- Inngår:
  - hendelsespublisering og abonnement
  - asynkron varsling om tilstandsendringer
  - standardiserte grensesnitt for hendelsesflyt
- Inngår ikke:
  - full transport av store dokumentpayloads (dekkes bedre av formidling/melding)
  - komplett forretningsprosessorkestrering i ett produkt

## Veikart over kommende funksjonalitet
- Forventet videreutvikling innen filtermønstre, observability og skalerbarhet.
- Løpende justering i samspill med dialog, melding, varsling og formidling.
- Konkrete roadmap-punkter må bekreftes i oppdatert produktdokumentasjon.

## Forretningsverdi/Verdiforslag
- Raskere tverretatlig samhandling gjennom hendelsesdrevet integrasjon.
- Bedre automatisering med mindre manuell oppfølging.
- Redusert integrasjonskompleksitet i store tjenestekjeder.
- Bedre grunnlag for proaktive tjenester og datadrevne prosesser.

## Utfordringer og risiko
- Juridisk risiko: deling av hendelsesdata uten korrekt hjemmel/avgrensning.
- Teknisk risiko: duplikater, rekkefølge og idempotens må håndteres korrekt hos konsumenter.
- Sikkerhetsrisiko: feil adgang til hendelsesstrømmer kan lekke sensitiv kontekst.
- Leverandørrisiko: varierende modenhet hos aktører som publiserer og konsumerer hendelser.
- Brukerrisiko: feil kvalitet i hendelsesdata kan trigge feil nedstrømsprosesser.

## Kanaler
- API-er og teknisk dokumentasjon i Altinn Docs.
- Integrasjoner i virksomhetenes backend/integrasjonsplattform.
- Hendelsesstrømmer til konsumenter med abonnementslogikk.

## Plattform
Skybasert fellestjeneste i Altinn 3.
Detaljert infrastruktur er ikke spesifisert i kildene brukt her.

## Gjenbruk
Svært høy gjenbruksverdi:
- felles hendelseskapabilitet på tvers av mange tjenester
- muliggjør standardiserte, løst koblede arkitekturer
- reduserer behov for proprietær event-infrastruktur i hvert prosjekt

## Støtte arkitekturprinsipper
Sterk støtte for:
- P4 Del og gjenbruk data
- P5 Del og gjenbruk løsninger
- P6 Lag digitale løsninger som støtter samhandling
- P1 Ta utgangspunkt i brukernes behov (hurtigere og mer sammenhengende tjenester)

## Finansiering
Ikke eksplisitt spesifisert i kildene brukt her.
Forutsettes forvaltet som del av Altinns nasjonale fellesløsninger.

## Forvaltning/eier
- Produktansvar: Altinn-forvaltningen
- Driftsansvar: Altinn-forvaltningen
- Budsjettansvar: usikkert i offentlig detaljnivå
- Styringsmodell: nasjonal forvaltning i Altinn-porteføljen

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/events/
- https://docs.altinn.studio/nb/events/what-do-you-get/
- https://docs.altinn.studio/nb/events/getting-started/
- https://docs.altinn.studio/nb/events/reference/

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Altinn Docs (hentet 2026-03-06)
