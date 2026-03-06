# Produkt-canvas: Altinn formidling

Maalgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn formidling

## Ressurs ID
8 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon med loepende videreutvikling av API-er, koeer, monitorering og migreringsstoette.

## Modenhet
Hoy:
- Etablert som del av Altinn 3-produktportefoljen.
- Dokumentert API-modell for asynkron datautveksling mellom systemer.
- Brukes for robust formidling med skalerbarhet, sikkerhet og sporbarhet.

## Kort beskrivelse
Altinn formidling (Broker) er en nasjonal formidlingstjeneste for sikker, asynkron datautveksling mellom virksomheter og systemer. Tjenesten er designet for scenarioer der data maa overfoeres paalitelig uten tett synkron kobling mellom avsender og mottaker.

## Kapabiliteter
- Datautveksling og integrasjon: Meldingsformidling
- Datautveksling og integrasjon: Dele data med andre
- Datautveksling og integrasjon: Bruke data fra andre
- Tjenesteutvikling: Integrerbare tjenester
- Samarbeid: Organisatorisk samhandling
- Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling
- Tillit: Sporbarhet og innsyn

Grunnlag: kapabiliteter mappet mot `index/capabilities.yaml`.

## Produktmaal
- Tilby en felles nasjonal tjeneste for robust asynkron dataformidling.
- Redusere punkt-til-punkt-integrasjoner og proprietaere transportmoenstre.
- Oeke leveringssikkerhet, skalerbarhet og observability i samhandling.
- Understoette sammenhengende tjenester med standardiserte integrasjonsmoenstre.

## Brukerbehov
- Virksomheter trenger sikker og paalitelig dataoverfoering med lav kopling.
- Integrasjonsteam trenger standard API-er for innlegging, uthenting og oppfoelging av leveranser.
- Forvaltning/drift trenger bedre sporbarhet og kontroll i transportleddet.

## Hvem er brukerne og brukersegmentene
- Offentlige virksomheter som avsendere/mottakere av data.
- Systemleverandoerer og integrasjonsteam.
- Tjenesteeiere med behov for robust B2B/B2G-formidling.
- Drifts- og sikkerhetsmiljoer som foelger opp flyt, feil og SLA.

## Hovedfunksjoner
- Asynkron meldings-/dataformidling via broker-prinsipp.
- Koe- og leveringsmekanismer med statusoppfoelging.
- API-er for opplasting, uthenting og kvitteringshaandtering.
- Integrasjon med autentisering/autorisasjon i Altinn-oekosystemet.
- Stotte for hendelses- og prosessdrevet samhandling der avsender/mottaker er loest koblet.

### Scope og avgrensning
- Inngaar:
  - transport/formidling av payload mellom aktorer
  - status, kvittering og kontrollmekanismer i formidlingsleddet
  - standardiserte API-er for integrasjon
- Inngaar ikke:
  - full faglogikk i avsender/mottakersystem
  - universell publisering/abonnement av domenehendelser (dekkes primaert av events-produkt)

## Veikart over kommende funksjonalitet
- Forventet videreutvikling av API-kvalitet, monitorering og operasjonell robusthet.
- Loepende harmonisering med øvrige Altinn-produkter (events, melding, autorisasjon).
- Konkrete prioriteringer ma avstemmes med produktets offentlige dokumentasjon.

## Forretningsverdi/Verdiforslag
- Lavere integrasjonskostnader gjennom gjenbruk av felles formidlingstjeneste.
- Bedre leveringskvalitet og mindre operasjonell risiko i kritisk dataflyt.
- Raskere etablering av nye samhandlingsprosesser paa tvers av virksomheter.
- Mindre behov for lokale transportloesninger med varierende sikkerhetsnivaa.

## Utfordringer og risiko
- Juridisk risiko: feil haandtering av datatyper og behandlingsgrunnlag i transportflyten.
- Teknisk risiko: feilhaandtering ved store volum og timeout/retry-scenarioer.
- Sikkerhetsrisiko: feil tilgangsstyring kan gi uoensket datapassasje.
- Leverandoerrisiko: avhengighet til korrekt implementering hos avsender og mottaker.
- Brukerrisiko: liten synlighet i asynkrone prosesser kan gi treg feiloppdagelse uten god monitorering.

## Kanaler
- API-er i Altinn docs.
- Integrasjon fra virksomhetenes fagsystem/integrasjonsplattform.
- Teknisk dokumentasjon, referanser og kom-i-gang i Altinn Docs.

## Plattform
Skybasert felleskomponent i Altinn 3-plattformen.
Detaljert infrastruktur/lokasjon er ikke spesifisert i kildene brukt her.

## Gjenbruk
Svaert hoy gjenbruksverdi:
- felles transport- og formidlingskapabilitet for mange sektorer
- reduserer duplisering av integrasjonsinfrastruktur
- fremmer standardiserte, loest koblede samhandlingsmoenstre

## Stoette arkitekturprinsipper
Sterk stoette for:
- P4 Del og gjenbruk data
- P5 Del og gjenbruk loesninger
- P6 Lag digitale loesninger som stoetter samhandling
- P7 Soerg for tillit til oppgaveloesningen

## Finansiering
Ikke eksplisitt spesifisert i kildene brukt her.
Forutsettes forvaltet som del av Altinns nasjonale fellesloesninger.

## Forvaltning/eier
- Produktansvar: Altinn-forvaltningen
- Driftsansvar: Altinn-forvaltningen
- Budsjettansvar: usikkert i offentlig detaljnivaa
- Styringsmodell: nasjonal forvaltning i Altinn-portefoljen

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/broker/
- https://docs.altinn.studio/nb/broker/what-do-you-get/
- https://docs.altinn.studio/nb/broker/getting-started/
- https://docs.altinn.studio/nb/broker/reference/

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Altinn Docs (hentet 2026-03-06)
