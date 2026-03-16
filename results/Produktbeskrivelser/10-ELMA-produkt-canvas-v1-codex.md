# Produkt-canvas: ELMA

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
ELMA (Elektronisk mottakeradresseregister)

## Ressurs ID
10 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon som etablert registertjeneste for elektronisk samhandling i eFaktura/Peppol-økosystemet.

## Modenhet
Høy:
- Etablert nasjonal registerkapabilitet med lang brukstid.
- Sentral rolle i oppslag av mottakerinformasjon for elektroniske dokumentflyter.
- Tett kobling til Peppol/eDelivery-praksis i Norge.

## Kort beskrivelse
ELMA er et elektronisk mottakeradresseregister som brukes til å finne hvor og hvordan elektroniske forretningsdokumenter kan leveres til en virksomhet. Tjenesten understøtter korrekt ruting i digital samhandling og reduserer feil i utsendelse av elektroniske dokumenter.

## Kapabiliteter
- Informasjonsforvaltning: Oversikt over tjenester
- Informasjonsforvaltning: Oversikt over API
- Datautveksling og integrasjon: Dele data med andre
- Datautveksling og integrasjon: Bruke data fra andre
- Standardisering: Forvaltningsstandarder
- Samarbeid: Organisatorisk samhandling
- Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling

Grunnlag: kapabiliteter mappet mot `index/capabilities.yaml`.

## Produktmål
- Sikre korrekt elektronisk adressering i digital dokumentutveksling.
- Redusere feilruting, retur og manuell håndtering i dokumentprosesser.
- Understøtte nasjonal og internasjonal samhandling gjennom standardiserte adresseregistermønstre.

## Brukerbehov
- Avsendere trenger oppdatert informasjon om hvordan mottakere kan motta elektroniske dokumenter.
- Mottakere trenger riktig synlighet av sine mottakskanaler og profiler.
- Integrasjonsteam trenger stabile oppslagstjenester i transport- og fakturaflyter.

## Hvem er brukerne og brukersegmentene
- Offentlige og private virksomheter som sender elektroniske dokumenter.
- Tjenesteleverandører/access points i eDelivery-økosystemet.
- Økonomi/regnskapsmiljøer og systemleverandører.

## Hovedfunksjoner
- Oppslag av mottakeradresser og relevante tekniske endepunkter.
- Registerfunksjon for elektronisk samhandlingskapasitet.
- Støtte for standardisert samhandling i eFaktura/Peppol-prosesser.
- Integrasjonsvennlig bruk i automatisert dokumentflyt.

### Scope og avgrensning
- Inngår:
  - register/oppslag av mottakerinformasjon
  - støtte til elektronisk dokumentruting
- Inngår ikke:
  - selve transporten av dokumentet (handteres av eDelivery/access points)
  - full fakturabehandling i avsender/mottakersystem

## Veikart over kommende funksjonalitet
- Forventet løpende oppdatering av registerkvalitet og samspill med Peppol-regelverk.
- Konkrete roadmap-punkter må avstemmes med forvaltningsinformasjon hos relevante myndigheter.

## Forretningsverdi/Verdiforslag
- Høy verdi gjennom redusert feilruting og mindre manuell avviksbehandling.
- Bedre kvalitet i digital samhandling mellom virksomheter.
- Skalerbar gevinst i store transaksjonsvolum.

## Utfordringer og risiko
- Juridisk risiko: feil bruk av virksomhetsdata eller mangelfull oppdatering.
- Teknisk risiko: datakvalitetsfeil i register gir feilruting nedstrøms.
- Sikkerhetsrisiko: integrasjonspunkter må beskyttes mot misbruk.
- Leverandørrisiko: avhengighet til økosystemets samlede datakvalitet.
- Brukerrisiko: feil konfigurasjon hos avsender kan overstyre korrekt registerbruk.

## Kanaler
- Registeroppslag via integrasjon i faktura-/dokumentsystemer.
- Informasjon via Altinn/Brreg-sider.

## Plattform
Nasjonal registertjeneste i norsk økosystem for elektronisk samhandling.
Detaljert driftsarkitektur er ikke spesifisert i kildene brukt her.

## Gjenbruk
Høy gjenbruksverdi:
- felles adresseregister for mange sektorer og aktører
- reduserer behov for lokale mottakerregistre
- styrker standardisert samhandling i stor skala

## Støtte arkitekturprinsipper
Sterk støtte for:
- P4 Del og gjenbruk data
- P6 Lag digitale løsninger som støtter samhandling
- P5 Del og gjenbruk løsninger

## Finansiering
Ikke eksplisitt spesifisert i kildene brukt her.

## Forvaltning/eier
- Produktansvar: knyttet til nasjonal forvaltning av elektronisk samhandling (må avstemmes mot oppdatert eierinfo)
- Driftsansvar: usikkert i detalj i kildene brukt her
- Budsjettansvar: usikkert i offentlig detaljnivå
- Styringsmodell: nasjonal forvaltning i samspill med Peppol/eDelivery-rammer

## Lenke til dokumentasjon
- https://www.brreg.no/om-oss/vara-register/elektronisk-mottakeradresseregister-elma/
- https://www.altinn.no/tjenester/uten-innlogging/elma/

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Brreg/Altinn (hentet 2026-03-07)
