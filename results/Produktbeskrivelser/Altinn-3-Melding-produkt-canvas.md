# Produkt-canvas: Altinn 3 Melding

Maalgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn 3 Melding (Correspondence)

## Ressurs ID
23 (Produktliste NA-kunnskap).
## Status/Livsfase
Produksjon med aktiv migrerings- og overgangsfase fra Altinn 2.

## Modenhet
Middels til hoy:
- Etablert tjeneste med referansedokumentasjon og tydelige integrasjonsmoenstre.
- Brukes for sikker meldingsutveksling mellom offentlig sektor og mottakere.
- Modenhet paavirkes av overgang fra Altinn 2 med tidskritisk migrering.

## Kort beskrivelse
Altinn 3 Melding er en nasjonal meldingstjeneste for sikker digital utveksling av korrespondanse (for eksempel brev, varselrelatert informasjon og dokumenter) mellom offentlige virksomheter og innbyggere/naeringsliv. En melding kan inngaa i en dialog og eksponeres videre gjennom Dialogporten.

## Kapabiliteter
- Sikker digital kommunikasjon mellom offentlig sektor og mottakere.
- Meldingslivssyklus med logging, sporing og status.
- Integrasjon med varslingskapabilitet (e-post/SMS) for oppmerksomhet rundt nye meldinger.
- Hendelsesbasert oppfolging via abonnementer.
- Integrasjon med Dialogporten og Arbeidsflate for samlet brukeropplevelse.

## Produktmaal
- Erstatte/migrere meldingstjenester fra Altinn 2 til Altinn 3 innen overgangsvindu.
- Tilby sikker og sporbar meldingstjeneste med hoy grad av automatisering.
- Understoette offentlig sektors behov for digital, etterproevbar korrespondanse.
- Bidra til enhetlig tilgang til meldinger i Altinns arbeidsflateoekosystem.

## Brukerbehov
- Avsendervirksomheter trenger sikker kanal for meldinger med vedlegg og tilgangsstyring.
- Mottakere trenger ett sted aa motta og finne igjen kommunikasjon fra offentlig sektor.
- Integratorer trenger API-er for automatisert sending, statusoppfolging og prosessintegrasjon.

## Hvem er brukerne og brukersegmentene
- Offentlige tjenesteeiere (etat/kommune/virksomhet).
- Systemleverandoerer som integrerer meldingsfunksjoner i fagsystem.
- Innbyggere og virksomheter som mottar meldinger.
- Arkiv-, juridiske og sikkerhetsmiljoer med krav til sporbarhet/etterlevelse.

## Hovedfunksjoner
- Sikker meldingsutsendelse med stoette for ulike formater og vedlegg.
- Hendelseslogging og statusinformasjon for levert/aapnet med mer.
- Varslingsfunksjon knyttet til nye meldinger og re-varsling.
- API-er for system-til-system og automatisert arbeidsflyt.
- Integrasjon der melding automatisk blir representert som dialog.
- Stoette for tilgangsstyring og ulike sikkerhetsnivaer.

### Scope og avgrensning
- Inngaar:
  - sikker formidling av korrespondanse
  - melding med vedlegg/lenker, status og livssyklus
  - integrasjon mot varsling, hendelser og dialog
- Inngaar ikke:
  - full saksbehandlingsflyt i avsenderens fagsystem
  - generisk filutveksling utenfor meldingskontekst

## Veikart over kommende funksjonalitet
- Sterkt fokus paa migrering og overfoering av tjenester/data/delegeringer fra Altinn 2.
- Videre harmonisering mot Dialogporten/Arbeidsflate.
- Prioriteringer maa bekreftes fortloepende i produktets overgangs- og nyhetsdokumentasjon.

## Forretningsverdi/Verdiforslag
- Reduserer behovet for usikre kanaler i sensitiv offentlig kommunikasjon.
- Oeker automatisering og reduserer manuelle feil i utsendelsesprosesser.
- Styrker etterproevbarhet gjennom logging og status i livssyklus.
- Gir mer enhetlig mottakeropplevelse og bedre oppfolging i offentlige prosesser.

## Utfordringer og risiko
- Tidsrisiko knyttet til migreringsfrist fra Altinn 2.
- Kravrisiko rundt sikkerhetsnivaa, personvern og tilgangsstyring.
- Integrasjonsrisiko ved store volum, store vedlegg og avhengighet til flere fellestjenester.
- Operasjonell risiko ved feil i varslingskjede eller mottakerdata.

## Kanaler
- API-er for tjenesteeiersystem/systemleverandoerer.
- Altinn arbeidsflate og tilknyttede brukerflater.
- Varslingskanaler (e-post/SMS) som stoettekanal.

## Plattform
Skybasert tjeneste i Altinn 3-plattformen med API-orientert samhandling.
Detaljert infrastruktur/lokasjon ikke dokumentert i kildene brukt her.

## Gjenbruk
Hoy gjenbruksverdi i offentlig sektor:
- standardisert meldingstjeneste som kan brukes paa tvers av etater
- etablert integrasjonsmodell med Dialogporten, Events og varsling
- reduserer behov for parallelle sektorvise meldingsloesninger

## Stoette arkitekturprinsipper
Vurderes som sterk paa:
- gjenbruk av nasjonale felleskomponenter
- sikker digital samhandling
- standardiserte grensesnitt og loes kobling
- sporbarhet og innebygd kontroll

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
- https://docs.altinn.studio/nb/correspondence/
- https://docs.altinn.studio/nb/correspondence/what-do-you-get/
- https://docs.altinn.studio/nb/correspondence/getting-started/
- https://docs.altinn.studio/nb/correspondence/reference/

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Nettkilder: Altinn Docs (hentet 2026-03-06)

