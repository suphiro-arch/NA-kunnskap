# Produkt-canvas: Varslinger

Maalgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn Varslinger

## Ressurs ID
24 (Produktliste NA-kunnskap).
## Status/Livsfase
Produksjon med kontinuerlig videreutvikling.

## Modenhet
Middels til hoy:
- Etablert varslingsprodukt med API, kanalstoette og testprosedyrer.
- Integrert med nasjonale registre for oppslag av navn/kontaktinformasjon.
- Omraadet utvikles videre med planlagte utvidelser i kanalstoette.

## Kort beskrivelse
Altinn Varslinger er en tjeneste for enveis digital varsling til innbyggere og virksomheter via e-post og SMS. Produktet muliggjoer programmatisk utsending, mottakeroppslag, kanalprioritering og leveringsoppfolging i offentlig kommunikasjon.

## Kapabiliteter
- Proaktiv kommunikasjon: utsending av varsler paa riktige tidspunkter.
- Integrasjon: API-basert bestilling, oppfolging og status.
- Registerbasert databruk: oppslag av navn/kontaktdetaljer via nasjonale registre.
- Regelstyring: sendebetingelser og kanalpreferanser.
- Tillit og tilgang: samspill med Altinn autorisasjon for mottakeridentifikasjon i organisasjoner.

## Produktmaal
- Gjore det enkelt for offentlige aktorer aa sende driftssikre varsler i stor skala.
- Redusere feilutsendelser gjennom oppslag, deduplisering og betingelsesstyring.
- Styrke sluttbrukeropplevelse med rett kanal til rett mottaker.
- Tilby felles varslingskapabilitet som kan gjenbrukes i flere tjenester.

## Brukerbehov
- Tjenesteeiere trenger en felles, sikker og effektiv varslingsmotor.
- Sluttbrukere trenger tidsriktige varsler om hendelser som krever oppmerksomhet.
- Integrasjonsteam trenger robuste API-er for utsending og statushaandtering.

## Hvem er brukerne og brukersegmentene
- Offentlige tjenesteeiere og interne Altinn-systemer.
- Leverandoerer av fagsystem og tjenesteeiersystemer.
- Innbyggere og virksomheter som mottar varsler.
- Drifts- og sikkerhetsmiljoer som foelger opp levering og feilhaandtering.

## Hovedfunksjoner
- Utsending via e-post og SMS med kanalpreferanse og fallback.
- Mottakeroppslag (navn, kontaktinfo, reservasjonsstatus) basert paa foedselsnummer/organisasjonsnummer.
- Autorisasjonsbasert mottakeridentifikasjon for organisasjonskontekst.
- Sendebetingelser for paa-minnelse og hendelsesstyrt varsling.
- Status- og feilhendelser tilgjengelig via API.
- Teststoette for TT02 med kontrollerte mekanismer for SMS.

### Scope og avgrensning
- Inngaar:
  - enveis varsling (ikke full toveis dialog)
  - kanalstyring, oppslag, betingelser, status
  - integrasjon mot tjenesteeiersystemer og Altinn-tjenester
- Inngaar ikke:
  - vedlegg i e-postvarsler (ikke stoettet per dokumentasjon)
  - full meldingsboksfunksjonalitet (dekkes av andre produkter som Melding/Dialogporten)

## Veikart over kommende funksjonalitet
- Dokumentasjonen beskriver plan om bredere kanalstoette over tid.
- Videreutvikling av forklaringer/referanse for oppslag, betingelser og API-funksjoner.
- Konkrete leveransepunkter boer loepende avstemmes mot produktets offentlige backlog/status.

## Forretningsverdi/Verdiforslag
- Hoy nytte for tjenester med behov for rask brukeroppmerksomhet.
- Reduserer behov for virksomhetsspesifikke varslingsloesninger.
- Oeker treffsikkerhet i kommunikasjon gjennom register- og autorisasjonsbaserte oppslag.
- Bedre operasjonell kontroll via programmatisk status- og feilhaandtering.

## Utfordringer og risiko
- Personvern- og etterlevelsesrisiko knyttet til kontaktdata og varslingsinnhold.
- Leveringsrisiko i eksterne kanaler (spamfiltrering, teleoperatoerforhold, forsinkelse).
- Avhengighet til kvalitet/timeliness i registerdata.
- Risiko for feil konfigurasjon av sendebetingelser og kanalpolicy.

## Kanaler
- E-post
- SMS
- Kanalpreferansemodeller (e-post foretrukket / SMS foretrukket med fallback)

## Plattform
Skybasert API-tjeneste i Altinn-oekosystemet.
Detaljer om driftslokasjon/underliggende infrastruktur er ikke eksplisitt beskrevet i kildene brukt her.

## Gjenbruk
Svaert hoy gjenbruksverdi:
- felles API-basert varslingsmotor for flere offentlige tjenester
- felles moenster for kanalvalg, mottakeroppslag og betinget sending
- reduserer duplisering av varslingsfunksjon i enkeltprosjekter

## Stoette arkitekturprinsipper
Vurderes som sterk paa:
- gjenbruk av felleskomponenter
- standardiserte grensesnitt og automatisering
- innebygd sikkerhet og styring av tilgang/mottakeridentitet
- robust digital samhandling paa tvers av virksomheter

## Finansiering
Ikke spesifisert i kildene brukt her.
Forutsettes som del av offentlig finansiert nasjonal fellestjeneste.

## Forvaltning/eier
Ma kvalitetssikres mot formell styringsinformasjon:
- Produktansvar: Altinn-forvaltningen
- Driftsansvar: Altinn-forvaltningen
- Budsjettansvar: Usikkert i offentlig detaljnivaa
- Styringsmodell: Nasjonal forvaltning av felleslosning

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/notifications/
- https://docs.altinn.studio/nb/notifications/what-do-you-get/
- https://docs.altinn.studio/nb/notifications/getting-started/
- https://docs.altinn.studio/nb/notifications/reference/

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Nettkilder: Altinn Docs (hentet 2026-03-06)

