---
title: "Informasjonssikkerhet"
weight: 7
description: "Evne til Ã¥ ha tilstrekkelig sikkerhet i tjenester og lÃ¸sninger som benyttes i felles Ã¸kosystem."
cardMeta: "2 delkapabiliteter / 15 produkter"
productsMarkdown: |
  ## Relaterte produkter
  
  | Produkt | Produktbeskrivelse | Koblet via | Hvorfor relevant |
  | --- | --- | --- | --- |
  | ID-porten | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/01-ID-porten-produkt-canvas-v3-codex.md) | Sikring av informasjonsflyt og datautveksling | beskytter innloggingsflyt, tokenutstedelse og overfÃ¸ring av identitetsinformasjon mellom ID-porten og tjenesteeier |
  | Maskinporten | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/02-Maskinporten-produkt-canvas-v3-codex.md) | Sikring av informasjonsflyt og datautveksling | beskytter tokenutstedelse, klientautentisering og overfÃ¸ring av tilgangsgrunnlag i integrasjonsflyten |
  | eSignering | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/03-eSignering-produkt-canvas-v3-codex.md) | Sikring av informasjonsflyt og datautveksling | beskytter dokumenter, signeringsoppdrag og statusmeldinger gjennom hele signeringsprosessen |
  | eFormidling | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/07-eFormidling-produkt-canvas-v3-codex.md) | Sikring av informasjonsflyt og datautveksling | Kryptering, integritet og sporbarhet i meldingsflyten. |
  | Altinn Formidling | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/08-Altinn-formidling-produkt-canvas-v3-codex.md) | Sikring av informasjonsflyt og datautveksling | Kryptering, autentisering, tilgangskontroll |
  | Digital postkasse | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/09-Digital-postkasse-produkt-canvas-v3-codex.md) | Sikring av informasjonsflyt og datautveksling | beskytter dokumentpakker, metadata og kvitteringer gjennom krav til signering, kryptering og kontrollert utveksling |
  | Peppol eDelivery | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/11-Peppol-eDelivery-produkt-canvas-v3-codex.md) | Sikring av informasjonsflyt og datautveksling | bruker sertifikater og tillitsrammeverk for Ã¥ sikre transport og validering i nettverket |
  | Altinn Events | [v3 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/12-Altinn-events-produkt-canvas-v3-codex.md) | Sikring av informasjonsflyt og datautveksling | â€“ Sikret transport; tilgangskontroll pÃ¥ abonnement |
  | data.altinn.no | [v4 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/17-data-altinn-no-produkt-canvas-v4-codex.md) | Sikring av informasjonsflyt og datautveksling | legger til rette for sikker utveksling ogsÃ¥ nÃ¥r data ikke er Ã¥pne eller inneholder personopplysninger |
  | Altinn Melding | [v5 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/23-Altinn-3-Melding-produkt-canvas-v5-codex.md) | Sikring av informasjonsflyt og datautveksling | beskytter innhold, vedlegg og overfÃ¸ringer i meldingsflyten |
  | Altinn Varsling | [v5 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/24-Varslinger-produkt-canvas-v5-codex.md) | Sikring av informasjonsflyt og datautveksling | er nÃ¸dvendig fordi kontaktinformasjon og varslingsinnhold behandles gjennom flere kanaler og oppslag |
  | Fiks melding | [v2 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/26-FIKS-Melding-produkt-canvas-v2-codex.md) | Sikring av informasjonsflyt og datautveksling | stÃ¸tter sikre meldingslÃ¸p og publiserer sikkerhetsunderlag for bruk av flere kanaler. |
  | HelseID | [v1 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/33-HelseID-produkt-canvas-v1-codex.md) | Sikring av informasjonsflyt og datautveksling | beskytter innloggingsflyt, tokenbruk og deling av identitets- og tilgangsinformasjon i digital samhandling |
  | Feide | [v1 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/47-Feide-produkt-canvas-v1-codex.md) | Sikring av informasjonsflyt og datautveksling | beskytter pÃ¥loggingsflyt, tokenutstedelse og overfÃ¸ring av brukeropplysninger mellom vertsorganisasjoner og tjenesteleverandÃ¸rer |
  | FINT Felleskomponent | [v1 (codex)](https://github.com/suphiro-arch/NA-kunnskap/blob/main/arkitektur/ressurser/operative-losninger-og-tjenester/70-FINT-Felleskomponent-v1-codex.md) | Sikring av informasjonsflyt og datautveksling | understÃ¸tter trygg dataflyt, integritet og tilgjengelighet i det fylkeskommunale integrasjonslÃ¸pet. |
---

Evne til Ã¥ ha tilstrekkelig sikkerhet i tjenester og lÃ¸sninger som benyttes i felles Ã¸kosystem.

