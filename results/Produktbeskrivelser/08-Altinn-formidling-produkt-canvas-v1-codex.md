# Produkt-canvas: Altinn formidling

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn formidling

## Ressurs ID
8 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon med løpende videreutvikling av API-er, køer, monitorering og migreringsstøtte.

## Modenhet
Høy:
- Etablert som del av Altinn 3-produktporteføljen.
- Dokumentert API-modell for asynkron datautveksling mellom systemer.
- Brukes for robust formidling med skalerbarhet, sikkerhet og sporbarhet.

## Kort beskrivelse
Altinn formidling (Broker) er en nasjonal formidlingstjeneste for sikker, asynkron datautveksling mellom virksomheter og systemer. Tjenesten er designet for scenarier der data må overføres pålitelig uten tett synkron kobling mellom avsender og mottaker.

## Kapabiliteter
- Datautveksling og integrasjon: Meldingsformidling
- Datautveksling og integrasjon: Dele data med andre
- Datautveksling og integrasjon: Bruke data fra andre
- Tjenesteutvikling: Integrerbare tjenester
- Samarbeid: Organisatorisk samhandling
- Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling
- Tillit: Sporbarhet og innsyn

Grunnlag: kapabiliteter mappet mot `index/capabilities.yaml`.

## Produktmål
- Tilby en felles nasjonal tjeneste for robust asynkron dataformidling.
- Redusere punkt-til-punkt-integrasjoner og proprietære transportmønstre.
- Øke leveringssikkerhet, skalerbarhet og observability i samhandling.
- Understøtte sammenhengende tjenester med standardiserte integrasjonsmønstre.

## Brukerbehov
- Virksomheter trenger sikker og pålitelig dataoverføring med lav kopling.
- Integrasjonsteam trenger standard API-er for innlegging, uthenting og oppfølging av leveranser.
- Forvaltning/drift trenger bedre sporbarhet og kontroll i transportleddet.

## Hvem er brukerne og brukersegmentene
- Offentlige virksomheter som avsendere/mottakere av data.
- Systemleverandører og integrasjonsteam.
- Tjenesteeiere med behov for robust B2B/B2G-formidling.
- Drifts- og sikkerhetsmiljøer som følger opp flyt, feil og SLA.

## Hovedfunksjoner
- Asynkron meldings-/dataformidling via broker-prinsipp.
- Kø- og leveringsmekanismer med statusoppfølging.
- API-er for opplasting, uthenting og kvitteringshåndtering.
- Integrasjon med autentisering/autorisasjon i Altinn-økosystemet.
- Støtte for hendelses- og prosessdrevet samhandling der avsender/mottaker er løst koblet.

### Scope og avgrensning
- Inngår:
  - transport/formidling av payload mellom aktører
  - status, kvittering og kontrollmekanismer i formidlingsleddet
  - standardiserte API-er for integrasjon
- Inngår ikke:
  - full faglogikk i avsender/mottakersystem
  - universell publisering/abonnement av domenehendelser (dekkes primært av events-produkt)

## Veikart over kommende funksjonalitet
- Forventet videreutvikling av API-kvalitet, monitorering og operasjonell robusthet.
- Løpende harmonisering med øvrige Altinn-produkter (events, melding, autorisasjon).
- Konkrete prioriteringer må avstemmes med produktets offentlige dokumentasjon.

## Forretningsverdi/Verdiforslag
- Lavere integrasjonskostnader gjennom gjenbruk av felles formidlingstjeneste.
- Bedre leveringskvalitet og mindre operasjonell risiko i kritisk dataflyt.
- Raskere etablering av nye samhandlingsprosesser på tvers av virksomheter.
- Mindre behov for lokale transportløsninger med varierende sikkerhetsnivå.

## Utfordringer og risiko
- Juridisk risiko: feil håndtering av datatyper og behandlingsgrunnlag i transportflyten.
- Teknisk risiko: feilhåndtering ved store volum og timeout/retry-scenarier.
- Sikkerhetsrisiko: feil tilgangsstyring kan gi uønsket datapassasje.
- Leverandørrisiko: avhengighet til korrekt implementering hos avsender og mottaker.
- Brukerrisiko: liten synlighet i asynkrone prosesser kan gi treg feiloppdagelse uten god monitorering.

## Kanaler
- API-er i Altinn docs.
- Integrasjon fra virksomhetenes fagsystem/integrasjonsplattform.
- Teknisk dokumentasjon, referanser og kom-i-gang i Altinn Docs.

## Plattform
Skybasert felleskomponent i Altinn 3-plattformen.
Detaljert infrastruktur/lokasjon er ikke spesifisert i kildene brukt her.

## Gjenbruk
Svært høy gjenbruksverdi:
- felles transport- og formidlingskapabilitet for mange sektorer
- reduserer duplisering av integrasjonsinfrastruktur
- fremmer standardiserte, løst koblede samhandlingsmønstre

## Støtte arkitekturprinsipper
Sterk støtte for:
- P4 Del og gjenbruk data
- P5 Del og gjenbruk løsninger
- P6 Lag digitale løsninger som støtter samhandling
- P7 Sørg for tillit til oppgaveløsningen

## Finansiering
Ikke eksplisitt spesifisert i kildene brukt her.
Forutsettes forvaltet som del av Altinns nasjonale fellesløsninger.

## Forvaltning/eier
- Produktansvar: Altinn-forvaltningen
- Driftsansvar: Altinn-forvaltningen
- Budsjettansvar: usikkert i offentlig detaljnivå
- Styringsmodell: nasjonal forvaltning i Altinn-porteføljen

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/broker/
- https://docs.altinn.studio/nb/broker/what-do-you-get/
- https://docs.altinn.studio/nb/broker/getting-started/
- https://docs.altinn.studio/nb/broker/reference/

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Altinn Docs (hentet 2026-03-06)
