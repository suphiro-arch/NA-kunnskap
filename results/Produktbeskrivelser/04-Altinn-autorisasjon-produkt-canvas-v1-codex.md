# Produkt-canvas: Altinn autorisasjon

Maalgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn autorisasjon

## Ressurs ID
4 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon med aktiv videreutvikling av API-er, tilgangsmodeller og policy-mekanismer.

## Modenhet
Hoy:
- Etablert som sentral autorisasjonskapabilitet i Altinn 3-plattformen.
- Dokumentert arkitektur med PDP/PEP, XACML 3.0 og policy-baserte mekanismer.
- I aktiv bruk for baade sluttbruker- og systemtilgang via ID-porten og Maskinporten.

## Kort beskrivelse
Altinn autorisasjon er den nasjonale mekanismen i Altinn for aa avgjoere og haandheve hvem som har tilgang til hvilke ressurser, handlinger og API-er. Loesningen kombinerer policy-basert tilgangskontroll (ABAC/XACML), rolle- og representasjonsmodeller, tilgangspakker og token-baserte integrasjonsflyter for aa muliggjoere sikker samhandling mellom personer, virksomheter og systemer.

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

## Produktmaal
- Tilby en felles autorisasjonsmotor for tjenester og API-er i Altinn-oekosystemet.
- Redusere fragmenterte tilgangsmodeller i offentlig sektor gjennom standardiserte policy-moenstre.
- Stoette sikker representasjon og delegering paa tvers av personer, virksomheter og systemer.
- Oeke gjenbruk og hastighet i tjenesteutvikling ved at autorisasjon tilbys som fellestjeneste.

## Brukerbehov
- Tjenesteeiere trenger en standard maate aa uttrykke og evaluere tilgangsregler paa.
- Integrasjonsteam trenger stabile autorisasjonsendepunkter for system-til-system-flyt.
- Sluttbrukere og virksomheter trenger tydelig og korrekt rettighetsforvaltning ved bruk av offentlige tjenester.

## Hvem er brukerne og brukersegmentene
- Offentlige tjenesteeiere som definerer policy og ressurstilgang.
- Integratorer og systemleverandoerer som bruker Authorization API-er.
- Virksomheter som delegerer rettigheter og forvalter tilgangspakker.
- Sluttbrukere/representanter som handler paa vegne av seg selv eller andre.

## Hovedfunksjoner
- Policy Decision Point (PDP) for autorisasjonsavgjoerelser.
- Policy Enforcement Point (PEP) for haandheving i apper/API-er.
- ABAC/XACML-basert evaluering av tilgang basert paa subject/resource/environment.
- API-er for autorisasjon med bruk av ID-porten- og Maskinporten-flyt.
- Stotte for tilgangspakker, roller og delegerbare scopes i tilgangsforvaltning.
- Kontekstberikelse i beslutningsforespoersler (context handler).

### Scope og avgrensning
- Inngaar:
  - autorisasjonsbeslutninger og haandheving i Altinn 3
  - policy-modellering, evaluering og API-stotte
  - integrasjon med autentiseringsleverandoerer (ID-porten/Maskinporten)
- Inngaar ikke:
  - full identitetsutstedelse (dette ligger i autentisering/eID)
  - virksomhetenes interne IAM utenfor Altinn-domene

## Veikart over kommende funksjonalitet
- Aktiv videreutvikling innen tilgangspakker, API-sikkerhet og policy-haandheving.
- Endringer i Altinns rolle-/representasjonsmodell (bl.a. utfasing av enkelte eldre rollemekanismer i dokumentasjonen) paavirker autorisasjonslandskapet framover.
- Detaljroadmap boer avstemmes loepende mot Altinn docs (sist oppdatert 2025 i flere autorisasjonssider).

## Forretningsverdi/Verdiforslag
- Reduserer risiko og kostnad ved aa sentralisere autorisasjon som fellestjeneste.
- Gir raskere innfoering av nye API-er/tjenester med ferdige sikkerhetsmoenstre.
- Oeker interoperabilitet mellom offentlige aktorer ved felles tilgangsmodell.
- Styrker tillit og etterproevbarhet i samhandling med sensitive data.

## Utfordringer og risiko
- Juridisk risiko: feil tolkning av hjemmelsgrunnlag for tilgangsregler i sektorspesifikke tjenester.
- Teknisk risiko: feil policykonfigurasjon eller manglende PEP-implementasjon kan gi over-/undertilgang.
- Sikkerhetsrisiko: tokenmisbruk, svak nøkkelforvaltning eller feil scopes kan gi uoensket API-tilgang.
- Leverandoerrisiko: avhengighet til flere felleskomponenter og oekosystemintegrasjoner.
- Brukerrisiko: kompleks representasjon/delegering kan gi feil i fullmaktshaandtering uten god UX og governance.

## Kanaler
- Authorization API-er i Altinn Docs (OpenAPI/Swagger).
- Plattformnaere utviklerbiblioteker og referansearkitektur for PEP/PDP.
- Tjenesteeiersystemer og API-gateways som konsumerer autorisasjonstjenesten.

## Plattform
Skybasert autorisasjonskapabilitet i Altinn 3-plattformen.
Arkitekturmessig bygget rundt PDP/PEP-moenster og policy-baserte beslutninger.

## Gjenbruk
Svaert hoy gjenbruksverdi:
- felles policy- og haandhevingsmoenster paa tvers av mange tjenester
- reduserer behov for lokale, proprietaere autorisasjonsmotorer
- muliggjoer skalerbar tilgangsstyring i nasjonale tjenestekjeder

## Stoette arkitekturprinsipper
Sterk stoette for:
- P5 Del og gjenbruk loesninger
- P6 Lag digitale loesninger som stoetter samhandling
- P7 Soerg for tillit til oppgaveloesningen
- P4 Del og gjenbruk data (sikker tilgang til delte data)

## Finansiering
Ikke eksplisitt spesifisert i tilgjengelige offentlige kilder brukt her.
Forutsettes forvaltet som del av nasjonal fellesloesning i Altinn-portefoljen.

## Forvaltning/eier
- Produktansvar: Altinn-forvaltningen
- Driftsansvar: Altinn-forvaltningen (detaljert driftsmodell ikke spesifisert i brukte kilder)
- Budsjettansvar: usikkert i offentlig detaljnivaa
- Styringsmodell: nasjonal forvaltning av fellesloesning, integrert i Altinns oekosystem

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

