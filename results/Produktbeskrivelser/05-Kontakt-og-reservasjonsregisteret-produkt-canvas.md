# Produkt-canvas: Kontakt- og reservasjonsregisteret

Maalgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Kontakt- og reservasjonsregisteret (KRR)

## Ressurs ID
5 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon med loepende videreutvikling av datakvalitet, grensesnitt og regelverksforankret bruk.

## Modenhet
Hoy:
- Etablert nasjonal felleskomponent i ordinert bruk i offentlig sektor.
- Bred bruk som grunnlag for digital kontakt med innbyggere.
- Tydelig rolle i oekosystemet for digital kommunikasjon, varsling og postdistribusjon.

## Kort beskrivelse
Kontakt- og reservasjonsregisteret er en nasjonal felleskomponent som gir offentlige virksomheter tilgang til oppdaterte digitale kontaktopplysninger for innbyggere, samt informasjon om reservasjon mot digital kommunikasjon. KRR er en kjernebyggestein for at offentlig sektor skal kunne kommunisere sikkert, effektivt og kanalriktig med innbyggerne.

## Kapabiliteter
- Datautveksling og integrasjon: Bruke data fra andre
- Datautveksling og integrasjon: Dele data med andre
- Sluttbrukertjenester: Proaktive tjenester
- Informasjonsforvaltning: Oversikt over datasett
- Tillit: Identifisering
- Tillit: Sporbarhet og innsyn
- Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling

Grunnlag: kapabiliteter mappet mot `index/capabilities.yaml`.

## Produktmaal
- Sikre at offentlige virksomheter kommuniserer i riktig kanal til riktig mottaker.
- Redusere feilutsendelser og kostnader ved manuell kontaktdatahaandtering.
- Understoette etterlevelse av reservasjon mot digital kommunikasjon.
- Bidra til mer sammenhengende og proaktive offentlige tjenester.

## Brukerbehov
- Virksomheter trenger en felles, oppdatert kilde for digital kontaktinformasjon.
- Innbyggere trenger forutsigbar haandtering av reservasjon og kontaktpreferanser.
- Integrasjonsteam trenger stabile oppslagstjenester med sporbar og sikker dataflyt.

## Hvem er brukerne og brukersegmentene
- Offentlige virksomheter som sender informasjon, vedtak og varsler til innbyggere.
- Fagsystemleverandoerer og integrasjonsmiljoer som konsumerer KRR-oppslag.
- Innbyggere som er registrert med kontaktopplysninger og ev. reservasjon.
- Forvaltnings- og sikkerhetsmiljoer med ansvar for korrekt bruk av kontaktdata.

## Hovedfunksjoner
- Oppslag av kontaktopplysninger for innbyggere (for eksempel digital adresse/kontaktkanal).
- Oppslag av reservasjonsstatus for digital kommunikasjon.
- Tilrettelegging for korrekt kanalvalg i utsendelsesprosesser.
- Integrasjon som støtte for digital post, varsling og meldingsprosesser.
- Forvaltningsgrensesnitt for registrering/oppdatering i tråd med gjeldende modell.

### Scope og avgrensning
- Inngaar:
  - nasjonalt register for kontaktopplysninger og reservasjon
  - oppslagstjenester for offentlige virksomheter
  - støtte til kanalvalg i offentlige kommunikasjonstjenester
- Inngaar ikke:
  - selve meldingsinnholdet eller distribusjonstjenesten (dekkes av andre produkter)
  - virksomhetenes interne CRM/sakssystemlogikk

## Veikart over kommende funksjonalitet
- Forventet kontinuerlig forbedring av datakvalitet, integrasjonsflyt og driftsovervaking.
- Videre harmonisering med øvrige felleskomponenter for post, varsling og samhandling.
- Konkrete roadmap-punkter ma avstemmes loepende mot Digdir docs og forvaltningsinfo.

## Forretningsverdi/Verdiforslag
- Oeker treffsikkerhet i offentlig kommunikasjon.
- Reduserer kostnader ved feil kanalbruk og returhaandtering.
- Gir bedre brukeropplevelse gjennom mer relevant og tidsriktig kommunikasjon.
- Understoetter storskala gjenbruk paa tvers av sektorer med ett felles datagrunnlag.

## Utfordringer og risiko
- Juridisk risiko: feil bruk av kontakt-/reservasjonsdata uten tilstrekkelig behandlingsgrunnlag.
- Teknisk risiko: avhengighet til oppetid/datakvalitet i felles register for kritiske prosesser.
- Sikkerhetsrisiko: personvernbrudd ved feil tilgangsstyring eller logging.
- Leverandoerrisiko: integrasjonskvalitet varierer mellom konsumerende systemer.
- Brukerrisiko: utdatert kontaktinfo kan gi feil varsling/levering og svekket tillit.

## Kanaler
- API-baserte oppslag fra virksomhetenes fagsystemer.
- Indirekte kanalstoette for digital postkasse, varsling og andre kommunikasjonstjenester.
- Dokumentasjon og forvaltningsinformasjon via Digdir docs.

## Plattform
Nasjonal felleskomponent forvaltet av Digdir (detaljert teknisk driftsarkitektur ikke spesifisert i kildene brukt her).

## Gjenbruk
Svaert hoy gjenbruksverdi:
- felles kontakt-/reservasjonsgrunnlag for hele offentlig sektor
- reduserer duplisering av registerfunksjonalitet i enkeltvirksomheter
- muliggjør standardisert kanalvalg og mer sammenhengende tjenester

## Stoette arkitekturprinsipper
Sterk stoette for:
- P4 Del og gjenbruk data
- P5 Del og gjenbruk loesninger
- P6 Lag digitale loesninger som stoetter samhandling
- P7 Soerg for tillit til oppgaveloesningen

## Finansiering
Ikke eksplisitt spesifisert i kildene brukt her.
Forutsettes som offentlig finansiert nasjonal felleskomponent.

## Forvaltning/eier
- Produktansvar: Digitaliseringsdirektoratet (Digdir)
- Driftsansvar: nasjonal forvaltning (detaljert driftsoppsett ikke spesifisert her)
- Budsjettansvar: usikkert i offentlig detaljnivaa
- Styringsmodell: forvaltning som nasjonal felleskomponent

## Lenke til dokumentasjon
- https://docs.digdir.no/docs/Kontaktregisteret/
- https://docs.digdir.no/docs/Kontaktregisteret/krr_overordnet
- https://www.digdir.no/felleskomponenter/digital-post/1483

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Digdir docs og Digdir.no (hentet 2026-03-06)
