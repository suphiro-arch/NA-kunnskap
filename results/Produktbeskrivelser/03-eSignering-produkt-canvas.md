# Produkt-canvas: eSignering

Maalgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
eSignering

## Ressurs ID
3 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon med loepende videreutvikling av sikkerhet, vilkaar og driftsoppfoelging.

## Modenhet
Hoy:
- Etablert nasjonal fellesloesning i ordinert bruk i offentlig sektor.
- Tydelig tjenestemodell med dokumentert tilgangsprosess, bruksvilkaar, statistikk og driftsoppfoelging.
- Loesningen inngaar i Digdirs produktgruppe for tillitstjenester sammen med ID-porten og Maskinporten.

## Kort beskrivelse
eSignering er en nasjonal fellesloesning som lar offentlige virksomheter gjennomfoere sikker, brukervennlig og effektiv digital signering av dokumenter med elektronisk ID. Tjenesten reduserer manuell haandtering av signeringsoppdrag, sikrer integriteten til signerte dokumenter, og legger til rette for videre arkivering og prosessautomatisering.

## Kapabiliteter
- Tillit: Signering
- Tillit: Autentisering
- Tillit: Identifisering
- Tillit: Sporbarhet og innsyn
- Tillit: Samtykke
- Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling
- Tjenesteutvikling: Integrerbare tjenester

Grunnlag: Kapabiliteter er mappet mot navn i `index/capabilities.yaml`.

## Produktmaal
- Tilby en felles nasjonal signeringstjeneste som kan gjenbrukes paa tvers av offentlig sektor.
- Redusere tidsbruk og manuell oppfoelging i signeringsprosesser.
- Oeke rettslig og teknisk trygghet i digital dokumenthaandtering.
- Standardisere integrasjon og forvaltning av signeringsprosesser i offentlige tjenester.

## Brukerbehov
- Offentlige virksomheter trenger sikker innhenting av underskrift uten papirflyt.
- Innbyggere trenger enkel og troverdig signering via kjent eID.
- Fagsystem og arkivmiljoer trenger sporbar, maskinell flyt fra oppdrag til ferdig signert dokument.

## Hvem er brukerne og brukersegmentene
- Offentlige virksomheter som avsendere av signeringsoppdrag.
- Innbyggere som signerer dokumenter.
- Leverandoerer/integrasjonsteam som bygger kobling mot tjenesten.
- Arkiv- og saksbehandlingsmiljoer med krav til etterproevbarhet.

## Hovedfunksjoner
- Digital signering med eID for dokumenter som krever underskrift.
- Stoette for enkeltsignatur og multisignatur.
- Signeringsoppdrag med statusoppfoelging (trafikk, oppetid, driftsovervaking).
- Integrasjon mot varslingsmoenstre (e-post/SMS) og offentlig kommunikasjonsflyt.
- Produksjon av dokumentasjon som er egnet for videre arkivering i sak-/arkivsystem.

### Scope og avgrensning
- Inngaar:
  - signeringstjeneste som felleskomponent
  - funksjoner for signeringsoppdrag og innbyggerflyt
  - forvaltning av bruksvilkaar, kostnadsmodell og tilgangsprosess
- Inngaar ikke:
  - full saksbehandlingsprosess i avsendervirksomhetens fagsystem
  - lokal dokumentproduksjon og intern arkitektur hos hver virksomhet

## Veikart over kommende funksjonalitet
- Produktgruppen for tillitstjenester har et felles strategisk veikart (oppdatert i Samarbeidsportalen).
- Dokumenterte endringer i 2025 viser aktiv videreutvikling av sikkerhet (bl.a. lenkefri varsling) og oppdaterte bruksvilkaar.
- Detaljprioriteringer ma avstemmes loepende med produktgruppestrategi og driftsinformasjon.

## Forretningsverdi/Verdiforslag
- Hoey samfunnsnytte ved raskere og mer sikker signeringsprosess i offentlig sektor.
- Reduserer kostnader knyttet til papir, manuell oppfoelging og fragmenterte signaturlosninger.
- Oeker kvalitet, sporbarhet og tillit i prosesser med rettslig betydning.
- Gir skalerbarhet ved at flere virksomheter kan bruke samme fellesloesning fremfor aa utvikle egne loesninger.

## Utfordringer og risiko
- Juridisk risiko: feil anvendelse av signaturtype eller prosesskrav i fagomraader med strenge rettsvirkninger.
- Teknisk risiko: integrasjonsfeil mellom fagsystem, varslingsflyt og signeringsgrensesnitt.
- Sikkerhetsrisiko: phishing/social engineering i brukerkommunikasjon; krever tydelige varslingsmoenstre og brukeropplaering.
- Leverandoerrisiko: tjenesten leveres i samspill mellom Digdir (forvaltning) og ekstern driftsleverandoer.
- Brukerrisiko: frafall i signeringsloep ved utydelig UX, feil timing i varsling eller kompleks representasjonsflyt.

## Kanaler
- API/integrasjon fra offentlige virksomheters fagsystem.
- Signeringsportal/-flyt for sluttbruker.
- Varslingskanaler (e-post/SMS) for oppmerksomhet rundt signeringsoppdrag.
- Informasjonskanaler via Samarbeidsportalen (om, ta i bruk, statistikk, driftsmeldinger).

## Plattform
Nasjonal skybasert fellestjeneste i Digdirs portefolje for tillitstjenester.
Driftsleveranse skjer i samarbeid med Posten Norge AS.

## Gjenbruk
Svaert hoy gjenbruksverdi:
- standardisert signeringskapabilitet paa tvers av etater
- reduserer behov for sektorvise spesialloesninger
- egnet som byggestein i sammenhengende tjenester med ID-porten, Maskinporten og meldings-/dialogprodukter

## Stoette arkitekturprinsipper
Sterk stoette for:
- P5 Del og gjenbruk loesninger
- P6 Lag digitale loesninger som stoetter samhandling
- P7 Soerg for tillit til oppgaveloesningen
- P1 Ta utgangspunkt i brukernes behov (forenklet signering for innbygger)

## Finansiering
Dokumentert kostnadsmodell med brukspris og kvartalsvis fakturering.
Prismodellen er oppdatert (bl.a. ny modell fra april 2024), og detaljer for pris ma leses i gjeldende kostnadsside.

## Forvaltning/eier
- Produktansvar: Digitaliseringsdirektoratet (Digdir)
- Driftsansvar: levert i samarbeid med Posten Norge AS
- Budsjettansvar: Digdir (detaljert intern modell ikke offentlig spesifisert i kildene)
- Styringsmodell: inngaar i produktgruppe Tillitstjenester med felles strategisk retning og veikart

## Lenke til dokumentasjon
- https://www.digdir.no/digital-sikkerhet/esignering/1487
- https://docs.digdir.no/docs/esignering/
- https://docs.digdir.no/docs/esignering/esign_komigang
- https://samarbeid.digdir.no/esignering/esignering/22
- https://samarbeid.digdir.no/esignering/kostnadsmodell-esignering/103
- https://samarbeid.digdir.no/id-porten/produktgruppestrategi-tillitstjenester/2138

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Digdir Docs og Samarbeidsportalen (hentet 2026-03-06)

