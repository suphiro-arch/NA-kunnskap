---
title: "Tillit"
weight: 5
description: "Evne å tilby tillitstjenester som muliggjør autentisering og autorisasjon på tvers av tjenestekjeder, og støtte en distribuert arkitektur og føderering mellom ulike domener og tjenester."
cardMeta: "8 delkapabiliteter / 11 produkter"
productsMarkdown: |
  ## Relaterte produkter
  
  | Produkt | Produktbeskrivelse | Koblet via | Hvorfor relevant |
  | --- | --- | --- | --- |
  | ID-porten | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/01-ID-porten-produkt-canvas-v3-codex.md) | Autentisering | verifiserer brukerens identitet gjennom godkjente eID-er og gir et felles sikkerhetsnivå på tvers av offentlige tjenester |
  | ID-porten | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/01-ID-porten-produkt-canvas-v3-codex.md) | Identifisering | kobler innloggingen til en entydig digital identitet som tjenesteeier kan bruke videre i sin saks- og tjenestelogikk |
  | ID-porten | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/01-ID-porten-produkt-canvas-v3-codex.md) | Representasjon | støtter innlogging i bruker-kontekst også når en innbygger handler med valgt virksomhet eller i delegert kontekst, i samspill med andre tillitstjenester og representasjonsgrunnlag |
  | Maskinporten | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/02-Maskinporten-produkt-canvas-v3-codex.md) | Autentisering | bekrefter identiteten til virksomheter og systemer som skal bruke API-er eller hente data maskinelt |
  | Maskinporten | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/02-Maskinporten-produkt-canvas-v3-codex.md) | Tilgangskontroll | gir grunnlag for å slippe inn bare systemer som har riktig token, scope og godkjent tilgang til den aktuelle ressursen |
  | eSignering | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/03-eSignering-produkt-canvas-v3-codex.md) | Autentisering | brukes for å sikre at den som signerer identifiserer seg med støttet eID før signeringen gjennomføres |
  | eSignering | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/03-eSignering-produkt-canvas-v3-codex.md) | Signering | er produktets kjernefunksjon og gjør det mulig å gjennomføre elektronisk signering av dokumenter i en nasjonal fellestjeneste |
  | Altinn autorisasjon | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v3-codex.md) | Representasjon | gjør det mulig å opptre på vegne av virksomhet eller annen part når dette er definert i Altinns rettighetsmodell |
  | Altinn autorisasjon | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v3-codex.md) | Tilgangskontroll | er kjernefunksjonen og avgjør om en bruker, virksomhet eller system får utføre en bestemt handling eller bruke en bestemt ressurs |
  | Altinn autorisasjon | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v3-codex.md) | Tilgangsstyring | gjør det mulig å forvalte roller, rettigheter og delegeringer som grunnlag for autorisasjonsbeslutninger |
  | Altinn formidling (Broker) | [v2 (copilot)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/08-Altinn-formidling-produkt-canvas-v2-copilot.md) | Sporbarhet og innsyn | Logging av all formidling og leveringsstatus |
  | Digital postkasse (felleskomponent) | [v2 (copilot)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/09-Digital-postkasse-produkt-canvas-v2-copilot.md) | Tillit | Sporbarhet og innsyn – Loggering av all post og leveringsstatus |
  | data.altinn.no | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/17-data-altinn-no-produkt-canvas-v3-codex.md) | Autentisering | støtter maskin-til-maskin-tilgang gjennom virksomhetssertifikat eller Maskinporten |
  | data.altinn.no | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/17-data-altinn-no-produkt-canvas-v3-codex.md) | Samtykke | muliggjør datadeling når bruk av data forutsetter et gyldig samtykke |
  | data.altinn.no | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/17-data-altinn-no-produkt-canvas-v3-codex.md) | Tilgangskontroll | håndterer tilgang gjennom tjenestekontekst, rettigheter og definerte datakilder |
  | Altinn Portal | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/21-Altinn-Portal-produkt-canvas-v3-codex.md) | Representasjon | gjør det mulig å opptre på vegne av virksomhet eller andre når fullmakter og rettigheter er etablert |
  | Altinn Portal | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/21-Altinn-Portal-produkt-canvas-v3-codex.md) | Sporbarhet og innsyn | understøttes gjennom meldingshistorikk, status og administrasjon av fullmakter og tilganger |
  | Altinn Portal | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/21-Altinn-Portal-produkt-canvas-v3-codex.md) | Tilgangsstyring | gir oversikt over hvem som kan gjøre hva, både for virksomheter og privatpersoner |
  | Dialogporten | [v4 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/22-Dialogporten-produkt-canvas-v4-codex.md) | Autentisering | støtter sluttbruker- og systemtilgang gjennom ID-porten og Maskinporten |
  | Dialogporten | [v4 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/22-Dialogporten-produkt-canvas-v4-codex.md) | Tilgangskontroll | bygger på Altinn Autorisasjon, autoriserte parter og tjenesteressurser |
  | Altinn 3 Melding (Correspondence) | [v4 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/23-Altinn-3-Melding-produkt-canvas-v4-codex.md) | Sporbarhet og innsyn | understøttes gjennom omfattende logging av hendelser og prosesser |
  | Altinn 3 Melding (Correspondence) | [v4 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/23-Altinn-3-Melding-produkt-canvas-v4-codex.md) | Tilgangskontroll | sørger for at kun autoriserte brukere og systemer får tilgang til meldinger og vedlegg |
  | Altinn Varslinger | [v4 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/24-Varslinger-produkt-canvas-v4-codex.md) | Tilgangskontroll | bruker autorisasjon for å finne riktige mottakere i organisasjonskontekst |
---

Evne å tilby tillitstjenester som muliggjør autentisering og autorisasjon på tvers av tjenestekjeder, og støtte en distribuert arkitektur og føderering mellom ulike domener og tjenester.
