# Produkt-canvas: Varslinger

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn Varslinger

## Ressurs ID
24 (Produktliste NA-kunnskap).
## Status/Livsfase
Produksjon med kontinuerlig videreutvikling.

## Modenhet
Middels til høy:
- Etablert varslingsprodukt med API, kanalstøtte og testprosedyrer.
- Integrert med nasjonale registre for oppslag av navn/kontaktinformasjon.
- Området utvikles videre med planlagte utvidelser i kanalstøtte.

## Kort beskrivelse
Altinn Varslinger er en tjeneste for enveis digital varsling til innbyggere og virksomheter via e-post og SMS. Produktet muliggjør programmatisk utsending, mottakeroppslag, kanalprioritering og leveringsoppfølging i offentlig kommunikasjon.

## Kapabiliteter
- Proaktiv kommunikasjon: utsending av varsler på riktige tidspunkter.
- Integrasjon: API-basert bestilling, oppfølging og status.
- Registerbasert databruk: oppslag av navn/kontaktdetaljer via nasjonale registre.
- Regelstyring: sendebetingelser og kanalpreferanser.
- Tillit og tilgang: samspill med Altinn autorisasjon for mottakeridentifikasjon i organisasjoner.

## Produktmål
- Gjøre det enkelt for offentlige aktører å sende driftssikre varsler i stor skala.
- Redusere feilutsendelser gjennom oppslag, deduplisering og betingelsesstyring.
- Styrke sluttbrukeropplevelse med rett kanal til rett mottaker.
- Tilby felles varslingskapabilitet som kan gjenbrukes i flere tjenester.

## Brukerbehov
- Tjenesteeiere trenger en felles, sikker og effektiv varslingsmotor.
- Sluttbrukere trenger tidsriktige varsler om hendelser som krever oppmerksomhet.
- Integrasjonsteam trenger robuste API-er for utsending og statushåndtering.

## Hvem er brukerne og brukersegmentene
- Offentlige tjenesteeiere og interne Altinn-systemer.
- Leverandører av fagsystem og tjenesteeiersystemer.
- Innbyggere og virksomheter som mottar varsler.
- Drifts- og sikkerhetsmiljøer som følger opp levering og feilhåndtering.

## Hovedfunksjoner
- Utsending via e-post og SMS med kanalpreferanse og fallback.
- Mottakeroppslag (navn, kontaktinfo, reservasjonsstatus) basert på fødselsnummer/organisasjonsnummer.
- Autorisasjonsbasert mottakeridentifikasjon for organisasjonskontekst.
- Sendebetingelser for på-minnelse og hendelsesstyrt varsling.
- Status- og feilhendelser tilgjengelig via API.
- Teststøtte for TT02 med kontrollerte mekanismer for SMS.

### Scope og avgrensning
- Inngår:
  - enveis varsling (ikke full toveis dialog)
  - kanalstyring, oppslag, betingelser, status
  - integrasjon mot tjenesteeiersystemer og Altinn-tjenester
- Inngår ikke:
  - vedlegg i e-postvarsler (ikke støttet per dokumentasjon)
  - full meldingsboksfunksjonalitet (dekkes av andre produkter som Melding/Dialogporten)

## Veikart over kommende funksjonalitet
- Dokumentasjonen beskriver plan om bredere kanalstøtte over tid.
- Videreutvikling av forklaringer/referanse for oppslag, betingelser og API-funksjoner.
- Konkrete leveransepunkter bør løpende avstemmes mot produktets offentlige backlog/status.

## Forretningsverdi/Verdiforslag
- Høy nytte for tjenester med behov for rask brukeroppmerksomhet.
- Reduserer behov for virksomhetsspesifikke varslingsløsninger.
- Øker treffsikkerhet i kommunikasjon gjennom register- og autorisasjonsbaserte oppslag.
- Bedre operasjonell kontroll via programmatisk status- og feilhåndtering.

## Utfordringer og risiko
- Personvern- og etterlevelsesrisiko knyttet til kontaktdata og varslingsinnhold.
- Leveringsrisiko i eksterne kanaler (spamfiltrering, teleoperatørforhold, forsinkelse).
- Avhengighet til kvalitet/timeliness i registerdata.
- Risiko for feil konfigurasjon av sendebetingelser og kanalpolicy.

## Kanaler
- E-post
- SMS
- Kanalpreferansemodeller (e-post foretrukket / SMS foretrukket med fallback)

## Plattform
Skybasert API-tjeneste i Altinn-økosystemet.
Detaljer om driftslokasjon/underliggende infrastruktur er ikke eksplisitt beskrevet i kildene brukt her.

## Gjenbruk
Svært høy gjenbruksverdi:
- felles API-basert varslingsmotor for flere offentlige tjenester
- felles mønster for kanalvalg, mottakeroppslag og betinget sending
- reduserer duplisering av varslingsfunksjon i enkeltprosjekter

## Støtte arkitekturprinsipper
Vurderes som sterk på:
- gjenbruk av felleskomponenter
- standardiserte grensesnitt og automatisering
- innebygd sikkerhet og styring av tilgang/mottakeridentitet
- robust digital samhandling på tvers av virksomheter

## Finansiering
Ikke spesifisert i kildene brukt her.
Forutsettes som del av offentlig finansiert nasjonal fellestjeneste.

## Forvaltning/eier
Ma kvalitetssikres mot formell styringsinformasjon:
- Produktansvar: Altinn-forvaltningen
- Driftsansvar: Altinn-forvaltningen
- Budsjettansvar: Usikkert i offentlig detaljnivå
- Styringsmodell: Nasjonal forvaltning av fellesløsning

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/notifications/
- https://docs.altinn.studio/nb/notifications/what-do-you-get/
- https://docs.altinn.studio/nb/notifications/getting-started/
- https://docs.altinn.studio/nb/notifications/reference/

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Nettkilder: Altinn Docs (hentet 2026-03-06)

