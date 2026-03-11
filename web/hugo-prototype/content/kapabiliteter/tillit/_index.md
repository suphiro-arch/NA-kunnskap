---
title: "Tillit"
weight: 5
description: "Evne å tilby tillitstjenester som muliggjør autentisering og autorisasjon på tvers av tjenestekjeder, og støtte en distribuert arkitektur og føderering mellom ulike domener og tjenester."
cardMeta: "8 delkapabiliteter · 6 produkter"
---

# Tillit

Evne å tilby tillitstjenester som muliggjør autentisering og autorisasjon på tvers av tjenestekjeder, og støtte en distribuert arkitektur og føderering mellom ulike domener og tjenester.

## Delkapabiliteter

| Delkapabilitet | Beskrivelse | Produkter |
| --- | --- | --- |
| [Autentisering](autentisering/) | Evne til å på en sikker og entydig måte verifisere den digitale identiteten til brukere og systemer. | 4 |
| [Tilgangskontroll](tilgangskontroll/) | Evne til å kontrollere at en bruker har rettighet til å benytte angitt ressurs eller tjeneste på vegne av andre eller seg selv. | 2 |
| [Tilgangsstyring](tilgangsstyring/) | Evne til å styre og gi tilgang til hvem som har rettighet til å benytte en ressurs (tjeneste, system, API, opplysning) på vegne av seg selv, andre personer eller virksomheter. | 2 |
| [Representasjon](representasjon/) | Evne til til å kunne opptre eller utføre handlinger digitalt på vegne av andre. | 2 |
| [Sporbarhet og innsyn](sporbarhet-og-innsyn/) | Dokumentasjon og logging av opplysninger for bruk i innsyn, forvaltning og kontroll av tillitstjenester. | 5 |
| [Signering](signering/) | Evne til juridisk bindende signering av dokumenter eller transaksjoner. | 1 |
| [Samtykke](samtykke/) | Evne til å akseptere, godkjenne eller gi tillatelse på vegne av seg selv eller andre, der det foreligger et representasjonsforhold. | 1 |
| [Identifisering](identifisering/) | Evne til entydig å fastslå og registrere identiteter (personer, virksomheter eller systemer) gjennom pålitelige metoder og kilder. | 3 |

## Relevante prinsipper

| Prinsipp | Begrunnelse |
| --- | --- |
| P7: Sørg for tillit til oppgaveløsningen | Autentisering, autorisasjon og samtykke legger det tekniske tillitsgrunnlaget for digital interaksjon. |

## Relaterte produkter

| Produkt | Versjon | Koblet via | Hvorfor relevant | Fil |
| --- | --- | --- | --- | --- |
| ID-porten | v2 (copilot) | Tillit | Minimering av uautorisert tilgang til tjenester | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/01-ID-porten-produkt-canvas-v2-copilot.md) |
| ID-porten | v2 (copilot) | Autentisering | Sikker identifikasjon og autentisering av brukere | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/01-ID-porten-produkt-canvas-v2-copilot.md) |
| ID-porten | v2 (copilot) | Identifisering | Påvisning av bruker-identitet via godkjente eID-hjemler | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/01-ID-porten-produkt-canvas-v2-copilot.md) |
| ID-porten | v2 (copilot) | Representasjon | Støtte for virksomhetsrepresentanter som logger inn på vegne av organisasjoner | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/01-ID-porten-produkt-canvas-v2-copilot.md) |
| ID-porten | v2 (copilot) | Sporbarhet og innsyn | Loggføring av innloggingshendelser | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/01-ID-porten-produkt-canvas-v2-copilot.md) |
| Maskinporten | v2 (copilot) | Tillit | Støtte for eksplisitte tillatelser og revokasjon av tilgang | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/02-Maskinporten-produkt-canvas-v2-copilot.md) |
| Maskinporten | v2 (copilot) | Autentisering | Sikker identifikasjon av API-klienter (systemkonto, virksomhetskonto) | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/02-Maskinporten-produkt-canvas-v2-copilot.md) |
| Maskinporten | v2 (copilot) | Sporbarhet og innsyn | Loggføring og revisjon av alle API-kall med autentisering | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/02-Maskinporten-produkt-canvas-v2-copilot.md) |
| Maskinporten | v2 (copilot) | Tilgangskontroll | Minimering av uautorisert tilgang til API-er og sensitive data | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/02-Maskinporten-produkt-canvas-v2-copilot.md) |
| Maskinporten | v2 (copilot) | Tilgangsstyring | Håndtering av fullmakter og delegering mellom virksomheter | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/02-Maskinporten-produkt-canvas-v2-copilot.md) |
| eSignering | v2 (copilot) | Tillit | Logging av all signering; innbygger-innsyn | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/03-eSignering-produkt-canvas-v2-copilot.md) |
| eSignering | v2 (copilot) | Autentisering | Verifikasjon av signeringsperson via eID | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/03-eSignering-produkt-canvas-v2-copilot.md) |
| eSignering | v2 (copilot) | Identifisering | Sikker identifikasjon basert på fnr./personnavn | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/03-eSignering-produkt-canvas-v2-copilot.md) |
| eSignering | v2 (copilot) | Samtykke | Mulighet for konsent-håndtering i signeringsprosess | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/03-eSignering-produkt-canvas-v2-copilot.md) |
| eSignering | v2 (copilot) | Signering | Digital signering av dokumenter | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/03-eSignering-produkt-canvas-v2-copilot.md) |
| Altinn autorisasjon | v2 (copilot) | Autentisering | Kobling til eID-løsninger (ID-porten, Maskinporten) | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v2-copilot.md) |
| Altinn autorisasjon | v2 (copilot) | Identifisering | Sikker identitetsverifisering for tilgangsavgjørelse | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v2-copilot.md) |
| Altinn autorisasjon | v2 (copilot) | Representasjon | Mulighet for personer/virksomheter å representere andre | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v2-copilot.md) |
| Altinn autorisasjon | v2 (copilot) | Sporbarhet og innsyn | Logging av alle tilgangsavgjørelser | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v2-copilot.md) |
| Altinn autorisasjon | v2 (copilot) | Tilgangskontroll | Policy-basert avgjørelse av hvem som får tilgang | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v2-copilot.md) |
| Altinn autorisasjon | v2 (copilot) | Tilgangsstyring | Administrasjon av roller, representasjon, delegering | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v2-copilot.md) |
| eInnsyn | v2 (copilot) | Tillit | Implementering av Offentlighetsloven | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/06-eInnsyn-produkt-canvas-v2-copilot.md) |
| eInnsyn | v2 (copilot) | Tillit | Kontrollert tilgjengeliggjøring av dokumenter og informasjon | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/06-eInnsyn-produkt-canvas-v2-copilot.md) |
| eInnsyn | v2 (copilot) | Sporbarhet og innsyn | Innbyggeres tilgang til hvordan offentlig sektor treffer beslutninger | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/06-eInnsyn-produkt-canvas-v2-copilot.md) |
| Altinn formidling (Broker) | v2 (copilot) | Sporbarhet og innsyn | Logging av all formidling og leveringsstatus | [Fil](https://github.com/suphiro-arch/NA-kunnskap/blob/main/results/Produktbeskrivelser/08-Altinn-formidling-produkt-canvas-v2-copilot.md) |
