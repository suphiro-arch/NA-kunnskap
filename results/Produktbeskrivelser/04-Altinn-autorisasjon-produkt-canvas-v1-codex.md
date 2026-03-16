# Produkt-canvas: Altinn autorisasjon

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn autorisasjon

## Ressurs ID
4 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon med aktiv videreutvikling av API-er, tilgangsmodeller og policy-mekanismer.

## Modenhet
Høy:
- Etablert som sentral autorisasjonskapabilitet i Altinn 3-plattformen.
- Dokumentert arkitektur med PDP/PEP, XACML 3.0 og policy-baserte mekanismer.
- I aktiv bruk for både sluttbruker- og systemtilgang via ID-porten og Maskinporten.

## Kort beskrivelse
Altinn autorisasjon er den nasjonale mekanismen i Altinn for å avgjøre og håndheve hvem som har tilgang til hvilke ressurser, handlinger og API-er. Løsningen kombinerer policy-basert tilgangskontroll (ABAC/XACML), rolle- og representasjonsmodeller, tilgangspakker og token-baserte integrasjonsflyter for å muliggjøre sikker samhandling mellom personer, virksomheter og systemer.

## Kapabiliteter
- Tillit: Tilgangskontroll
- Tillit: Tilgangsstyring
- Tillit: Representasjon
- Tillit: Autentisering
- Tillit: Identifisering
- Tillit: Sporbarhet og innsyn
- Datautveksling og integrasjon: Dele data med andre
- Datautveksling og integrasjon: Bruke data fra andre
- Tjenesteutvikling: Integrerbare tjenester
- Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling

Grunnlag: kapabiliteter mappet mot `index/capabilities.yaml`.

## Produktmål
- Tilby en felles autorisasjonsmotor for tjenester og API-er i Altinn-økosystemet.
- Redusere fragmenterte tilgangsmodeller i offentlig sektor gjennom standardiserte policy-mønstre.
- Støtte sikker representasjon og delegering på tvers av personer, virksomheter og systemer.
- Øke gjenbruk og hastighet i tjenesteutvikling ved at autorisasjon tilbys som fellestjeneste.

## Brukerbehov
- Tjenesteeiere trenger en standard måte å uttrykke og evaluere tilgangsregler på.
- Integrasjonsteam trenger stabile autorisasjonsendepunkter for system-til-system-flyt.
- Sluttbrukere og virksomheter trenger tydelig og korrekt rettighetsforvaltning ved bruk av offentlige tjenester.

## Hvem er brukerne og brukersegmentene
- Offentlige tjenesteeiere som definerer policy og ressurstilgang.
- Integratorer og systemleverandører som bruker Authorization API-er.
- Virksomheter som delegerer rettigheter og forvalter tilgangspakker.
- Sluttbrukere/representanter som handler på vegne av seg selv eller andre.

## Hovedfunksjoner
- Policy Decision Point (PDP) for autorisasjonsavgjørelser.
- Policy Enforcement Point (PEP) for håndheving i apper/API-er.
- ABAC/XACML-basert evaluering av tilgang basert på subject/resource/environment.
- API-er for autorisasjon med bruk av ID-porten- og Maskinporten-flyt.
- Støtte for tilgangspakker, roller og delegerbare scopes i tilgangsforvaltning.
- Kontekstberikelse i beslutningsforespørsler (context handler).

### Scope og avgrensning
- Inngår:
  - autorisasjonsbeslutninger og håndheving i Altinn 3
  - policy-modellering, evaluering og API-stotte
  - integrasjon med autentiseringsleverandører (ID-porten/Maskinporten)
- Inngår ikke:
  - full identitetsutstedelse (dette ligger i autentisering/eID)
  - virksomhetenes interne IAM utenfor Altinn-domene

## Veikart over kommende funksjonalitet
- Aktiv videreutvikling innen tilgangspakker, API-sikkerhet og policy-håndheving.
- Endringer i Altinns rolle-/representasjonsmodell (bl.a. utfasing av enkelte eldre rollemekanismer i dokumentasjonen) påvirker autorisasjonslandskapet framover.
- Detaljroadmap bør avstemmes løpende mot Altinn docs (sist oppdatert 2025 i flere autorisasjonssider).

## Forretningsverdi/Verdiforslag
- Reduserer risiko og kostnad ved å sentralisere autorisasjon som fellestjeneste.
- Gir raskere innføring av nye API-er/tjenester med ferdige sikkerhetsmønstre.
- Øker interoperabilitet mellom offentlige aktører ved felles tilgangsmodell.
- Styrker tillit og etterprøvbarhet i samhandling med sensitive data.

## Utfordringer og risiko
- Juridisk risiko: feil tolkning av hjemmelsgrunnlag for tilgangsregler i sektorspesifikke tjenester.
- Teknisk risiko: feil policykonfigurasjon eller manglende PEP-implementasjon kan gi over-/undertilgang.
- Sikkerhetsrisiko: tokenmisbruk, svak nøkkelforvaltning eller feil scopes kan gi uønsket API-tilgang.
- Leverandørrisiko: avhengighet til flere felleskomponenter og økosystemintegrasjoner.
- Brukerrisiko: kompleks representasjon/delegering kan gi feil i fullmaktshåndtering uten god UX og governance.

## Kanaler
- Authorization API-er i Altinn Docs (OpenAPI/Swagger).
- Plattformnære utviklerbiblioteker og referansearkitektur for PEP/PDP.
- Tjenesteeiersystemer og API-gateways som konsumerer autorisasjonstjenesten.

## Plattform
Skybasert autorisasjonskapabilitet i Altinn 3-plattformen.
Arkitekturmessig bygget rundt PDP/PEP-mønster og policy-baserte beslutninger.

## Gjenbruk
Svært høy gjenbruksverdi:
- felles policy- og håndhevingsmønster på tvers av mange tjenester
- reduserer behov for lokale, proprietære autorisasjonsmotorer
- muliggjør skalerbar tilgangsstyring i nasjonale tjenestekjeder

## Støtte arkitekturprinsipper
Sterk støtte for:
- P5 Del og gjenbruk løsninger
- P6 Lag digitale løsninger som støtter samhandling
- P7 Sørg for tillit til oppgaveløsningen
- P4 Del og gjenbruk data (sikker tilgang til delte data)

## Finansiering
Ikke eksplisitt spesifisert i tilgjengelige offentlige kilder brukt her.
Forutsettes forvaltet som del av nasjonal fellesløsning i Altinn-porteføljen.

## Forvaltning/eier
- Produktansvar: Altinn-forvaltningen
- Driftsansvar: Altinn-forvaltningen (detaljert driftsmodell ikke spesifisert i brukte kilder)
- Budsjettansvar: usikkert i offentlig detaljnivå
- Styringsmodell: nasjonal forvaltning av fellesløsning, integrert i Altinns økosystem

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/authorization/
- https://docs.altinn.studio/nb/technology/architecture/capabilities/runtime/security/authorization/
- https://docs.altinn.studio/nb/api/authorization/
- https://docs.altinn.studio/nb/authorization/reference/architecture/accesscontrol/pep/
- https://docs.altinn.studio/nb/authorization/what-do-you-get/pdp/

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Altinn Docs (hentet 2026-03-06)

