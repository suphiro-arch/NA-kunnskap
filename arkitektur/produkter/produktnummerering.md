# Produktregister og ressurs-ID-er

Kilde: arbeidsregister bygget fra eksisterende produktliste, siste produktversjoner i repoet, `sources/links.md` og ekstra offisielle kilder verifisert i denne arbeidsøkten.

## Prinsipp
- `Løpenr` beholdes som stabil intern sortering og brukes fortsatt i filnavn, for eksempel `01-ID-porten-produkt-canvas-v3-codex.md`.
- `Ressurs-ID` er den nye, kanoniske identifikatoren som skal brukes i feltet `Ressurs ID` i produktbeskrivelser.
- `Ressurs-ID` bygges som `<EIERKODE>-<løpenummer hos eier>`, for eksempel `DIGDIR-001` eller `KS-003`.
- `Ressurskategori` skiller mellom hovedtyper ressurser, som felleskomponent, fellesløsning, register, portal, plattform og EU-felleskomponent.
- `Type ressurs` beskriver ressursen mer presist på neste nivå.
- Nye produkter skal få neste ledige nummer innenfor sin eierkode. Eksisterende `Ressurs-ID` skal ikke endres uten bevisst omnummerering.
- Rader uten egen produktbeskrivelse ennå er arbeidsutkast. Der står `Siste versjon` som `Ikke opprettet ennå` og dokumentfeltet er tomt.
- Eier, ressurskategori, type ressurs og kapabilitetstreff for nye ressurser er første arbeidsutkast og må kvalitetssikres når produktbeskrivelsene opprettes.

## Eierkoder
| Eierkode | Eier | Bruk |
|---|---|---|
| `DIGDIR` | Digdir | Digitale fellesløsninger og Altinn-relaterte løsninger som forvaltes i Digdir-regi |
| `BRREG` | Brønnøysundregistrene | Register- og samhandlingsløsninger som forvaltes av Brønnøysundregistrene |
| `KS` | KS Digital | Kommunale fellesløsninger og KS-plattformtjenester |
| `SIKT` | Sikt | Nasjonale fellesløsninger for utdanning og forskning |
| `HDIR` | Helsedirektoratet | Helsedirektoratets nasjonale ressurser |
| `NHN` | Norsk helsenett | Nasjonale e-helseløsninger og helseinfrastruktur |
| `NAV` | NAV | NAVs fellesløsninger og registre |
| `SKATT` | Skatteetaten | Fellesløsninger og datatjenester forvaltet av Skatteetaten |
| `KART` | Kartverket | Nasjonale geodata- og kartressurser |
| `EU` | EU / Europakommisjonen | Relevante europeiske felleskomponenter og byggesteiner |

## Digdir (`DIGDIR`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|
| 1 | `DIGDIR-001` | ID-porten | Felleskomponent | Tillitstjeneste | Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Autentisering<br>Tillit: Identifisering<br>Tillit: Representasjon<br>Tjenesteutvikling: Integrerbare tjenester | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/01-ID-porten-produkt-canvas-v3-codex.md) |
| 2 | `DIGDIR-002` | Maskinporten | Felleskomponent | Tillitstjeneste | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Autentisering<br>Tillit: Tilgangskontroll | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/02-Maskinporten-produkt-canvas-v3-codex.md) |
| 3 | `DIGDIR-003` | eSignering | Felleskomponent | Tillitstjeneste | Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Autentisering<br>Tillit: Signering | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/03-eSignering-produkt-canvas-v3-codex.md) |
| 4 | `DIGDIR-004` | Altinn autorisasjon | Felleskomponent | Autorisasjonstjeneste | Tillit: Representasjon<br>Tillit: Tilgangskontroll<br>Tillit: Tilgangsstyring | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v3-codex.md) |
| 5 | `DIGDIR-005` | Kontakt- og reservasjonsregisteret | Register | Register / grunndata | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/05-Kontakt-og-reservasjonsregisteret-produkt-canvas-v3-codex.md) |
| 6 | `DIGDIR-006` | eInnsyn | Fellesløsning | Innsynstjeneste | Samarbeid: Organisatorisk samhandling<br>Sluttbrukertjenester: Sammenhengende tjenester | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/06-eInnsyn-produkt-canvas-v3-codex.md) |
| 7 | `DIGDIR-007` | eFormidling | Fellesløsning | Formidlingstjeneste | Datautveksling: Bruke data fra andre<br>Datautveksling: Dele data med andre<br>Datautveksling: Meldingsformidling<br>Sikring av informasjonsflyt og datautveksling<br>Samhandling: Organisatorisk samhandling<br>Forvaltningsstandarder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/07-eFormidling-produkt-canvas-v2-copilot.md) |
| 8 | `DIGDIR-008` | Altinn formidling (Broker) | Fellesløsning | Formidlingstjeneste | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Samarbeid: Organisatorisk samhandling<br>Tjenesteutvikling: Integrerbare tjenester | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/08-Altinn-formidling-produkt-canvas-v2-copilot.md) |
| 9 | `DIGDIR-009` | Digital postkasse (felleskomponent) | Felleskomponent | Meldingstjeneste / innbyggerkanal | Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Sluttbrukertjenester: Sammenhengende tjenester | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/09-Digital-postkasse-produkt-canvas-v2-copilot.md) |
| 12 | `DIGDIR-010` | Altinn events (Hendelsestjeneste) | Felleskomponent | Hendelsestjeneste | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Hendelsesdrevet<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tjenesteutvikling: Integrerbare tjenester | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/12-Altinn-events-produkt-canvas-v2-copilot.md) |
| 13 | `DIGDIR-011` | Felles datakatalog | Fellesløsning | Datakatalog | Informasjonsforvaltning: Oversikt over API<br>Informasjonsforvaltning: Oversikt over begreper<br>Informasjonsforvaltning: Oversikt over datasett<br>Informasjonsforvaltning: Oversikt over informasjonsmodeller<br>Standardisering: Forvaltningsstandarder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/13-Felles-datakatalog-produkt-canvas-v2-copilot.md) |
| 14 | `DIGDIR-012` | Begrepskatalog | Fellesløsning | Begrepskatalog | Informasjonsforvaltning: Datastyring<br>Informasjonsforvaltning: Informasjonsarkitektur<br>Informasjonsforvaltning: Oversikt over begreper<br>Standardisering: Forvaltningsstandarder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/14-Begrepskatalog-produkt-canvas-v2-copilot.md) |
| 15 | `DIGDIR-013` | API-katalog | Fellesløsning | API-katalog | Informasjonsforvaltning: Informasjonsarkitektur<br>Informasjonsforvaltning: Oversikt over API<br>Standardisering: Forvaltningsstandarder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/15-API-katalog-produkt-canvas-v2-copilot.md) |
| 16 | `DIGDIR-014` | data.norge.no | Portal | Metadataportal | Informasjonsforvaltning: Oversikt over API<br>Informasjonsforvaltning: Oversikt over begreper<br>Informasjonsforvaltning: Oversikt over datasett<br>Informasjonsforvaltning: Oversikt over hendelser<br>Informasjonsforvaltning: Oversikt over informasjonsmodeller<br>Informasjonsforvaltning: Oversikt over tjenester<br>Standardisering: Forvaltningsstandarder | v4 (codex) | [Åpne](../../results/Produktbeskrivelser/16-data-norge-no-produkt-canvas-v4-codex.md) |
| 17 | `DIGDIR-015` | data.altinn.no | Fellesløsning | Datadelingsløsning | Datadrevet: Sammenstilling av data<br>Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Standardisering: Forvaltningsstandarder<br>Tillit: Autentisering<br>Tillit: Samtykke<br>Tillit: Tilgangskontroll<br>Tjenesteutvikling: Integrerbare tjenester | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/17-data-altinn-no-produkt-canvas-v3-codex.md) |
| 18 | `DIGDIR-016` | Norge.no | Portal | Veiviser / portal | Informasjonsforvaltning: Oversikt over tjenester<br>Samarbeid: Organisatorisk samhandling<br>Sluttbrukertjenester: Sammenhengende tjenester<br>Sluttbrukertjenester: Tjenestekjeder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/18-Norge-no-produkt-canvas-v2-copilot.md) |
| 19 | `DIGDIR-017` | Altinn | Plattform | Plattform / portal | Samarbeid: Tjenesteforvaltning<br>Tjenesteutvikling: Gjenbrukbare tjenester<br>Tjenesteutvikling: Integrerbare tjenester | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/19-Altinn-produkt-canvas-v2-copilot.md) |
| 20 | `DIGDIR-018` | Altinn Studio | Plattform | Utviklingsplattform | Tjenesteutvikling: Gjenbrukbare tjenester<br>Tjenesteutvikling: Integrerbare tjenester<br>Tjenesteutvikling: Tjenestedesign<br>Tjenesteutvikling: Utviklings- og kjÃ¸retidsmiljÃ¸ | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/20-Altinn-Studio-produkt-canvas-v2-copilot.md) |
| 21 | `DIGDIR-019` | Altinn Portal | Portal | Portal | Sluttbrukertjenester: Sammenhengende tjenester<br>Sluttbrukertjenester: Tjenestekjeder<br>Tillit: Representasjon<br>Tillit: Sporbarhet og innsyn<br>Tillit: Tilgangsstyring | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/21-Altinn-Portal-produkt-canvas-v3-codex.md) |
| 22 | `DIGDIR-020` | Dialogporten | Fellesløsning | Dialogtjeneste | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Hendelsesdrevet<br>Sluttbrukertjenester: Sammenhengende tjenester<br>Tillit: Autentisering<br>Tillit: Tilgangskontroll<br>Tjenesteutvikling: Integrerbare tjenester | v4 (codex) | [Åpne](../../results/Produktbeskrivelser/22-Dialogporten-produkt-canvas-v4-codex.md) |
| 23 | `DIGDIR-021` | Altinn 3 Melding (Correspondence) | Fellesløsning | Meldingstjeneste | Datautveksling og integrasjon: Hendelsesdrevet<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Sporbarhet og innsyn<br>Tillit: Tilgangskontroll<br>Tjenesteutvikling: Integrerbare tjenester | v4 (codex) | [Åpne](../../results/Produktbeskrivelser/23-Altinn-3-Melding-produkt-canvas-v4-codex.md) |
| 24 | `DIGDIR-022` | Altinn Varslinger | Fellesløsning | Varslingstjeneste | Datadrevet: Sammenstilling av data<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Sluttbrukertjenester: Proaktive tjenester<br>Tillit: Tilgangskontroll<br>Tjenesteutvikling: Integrerbare tjenester | v4 (codex) | [Åpne](../../results/Produktbeskrivelser/24-Varslinger-produkt-canvas-v4-codex.md) |

## Brønnøysundregistrene (`BRREG`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|
| 10 | `BRREG-001` | ELMA (Elektronisk mottakeradresseregister) | Register | Adresseregister | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Informasjonsforvaltning: Oversikt over tjenester<br>Standardisering: Forvaltningsstandarder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/10-ELMA-produkt-canvas-v2-copilot.md) |
| 11 | `BRREG-002` | Peppol eDelivery | Felleskomponent | Meldingsinfrastruktur | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Standardisering: EU-standarder<br>Standardisering: Forvaltningsstandarder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/11-Peppol-eDelivery-produkt-canvas-v2-copilot.md) |
| 46 | `BRREG-003` | Enhetsregisteret | Register | Register / grunndata | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |

## KS Digital (`KS`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|
| 25 | `KS-001` | FIKS-plattformen | Plattform | Samhandlingsplattform | Samarbeid: Organisatorisk samhandling<br>Tjenesteutvikling: Integrerbare tjenester | Ikke opprettet ennå | - |
| 26 | `KS-002` | FIKS Melding | Fellesløsning | Formidlingstjeneste | Datautveksling og integrasjon: Meldingsformidling<br>Samarbeid: Organisatorisk samhandling | Ikke opprettet ennå | - |
| 27 | `KS-003` | SvarUt | Fellesløsning | Utsendingstjeneste | Datautveksling og integrasjon: Meldingsformidling<br>Sluttbrukertjenester: Sammenhengende tjenester | Ikke opprettet ennå | - |
| 28 | `KS-004` | FIKS Register | Register | Registertjeneste | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |
| 29 | `KS-005` | Felles tjenesteplattform | Plattform | Kommunal tjenesteplattform | Samarbeid: Organisatorisk samhandling<br>Tjenesteutvikling: Gjenbrukbare tjenester | Ikke opprettet ennå | - |
| 30 | `KS-006` | Fiks Digiorden | Fellesløsning | Styrings- og oversiktsløsning | Informasjonsforvaltning: Datastyring<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling | Ikke opprettet ennå | - |

## Sikt (`SIKT`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|
| 47 | `SIKT-001` | Feide | Felleskomponent | Innloggings- og datadelingstjeneste | Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Autentisering<br>Tillit: Tilgangskontroll | Ikke opprettet ennå | - |
| 48 | `SIKT-002` | Felles studentsystem (FS) | Fellesløsning | Studentinformasjonssystem | Datautveksling og integrasjon: Dele data med andre<br>Informasjonsforvaltning: Datastyring<br>Samarbeid: Organisatorisk samhandling | Ikke opprettet ennå | - |
| 49 | `SIKT-003` | Opptaksløsninger | Fellesløsning | Opptaks- og saksbehandlingsløsning | Datautveksling og integrasjon: Bruke data fra andre<br>Samarbeid: Organisatorisk samhandling<br>Sluttbrukertjenester: Sammenhengende tjenester | Ikke opprettet ennå | - |
| 50 | `SIKT-004` | Nasjonal vitnemålsdatabase (NVB) | Register | Resultat- og vitnemålsdatabase | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |
| 51 | `SIKT-005` | Vitnemålsportalen | Fellesløsning | Delingsportal for resultater og vitnemål | Datautveksling og integrasjon: Dele data med andre<br>Sluttbrukertjenester: Sammenhengende tjenester | Ikke opprettet ennå | - |

## Helsedirektoratet (`HDIR`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|
| 31 | `HDIR-001` | Helsedata.no | Portal | Datatilgangsportal | Informasjonsforvaltning: Oversikt over datasett<br>Informasjonsforvaltning: Oversikt over tjenester | Ikke opprettet ennå | - |

## Norsk helsenett (`NHN`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|
| 32 | `NHN-001` | Helsenorge | Portal | Innbyggerportal | Sluttbrukertjenester: Sammenhengende tjenester<br>Samarbeid: Organisatorisk samhandling | Ikke opprettet ennå | - |
| 33 | `NHN-002` | HelseID | Felleskomponent | Tillitstjeneste for helse | Tillit: Autentisering<br>Tillit: Tilgangskontroll<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling | Ikke opprettet ennå | - |
| 34 | `NHN-003` | Kjernejournal | Fellesløsning | Helseopplysningsdeling | Datautveksling og integrasjon: Bruke data fra andre<br>Samarbeid: Organisatorisk samhandling | Ikke opprettet ennå | - |
| 35 | `NHN-004` | e-resept | Fellesløsning | Samhandlingsløsning for legemidler | Datautveksling og integrasjon: Meldingsformidling<br>Samarbeid: Organisatorisk samhandling | Ikke opprettet ennå | - |

## NAV (`NAV`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|
| 36 | `NAV-001` | Aa-registeret | Register | Register / grunndata | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |

## Skatteetaten (`SKATT`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|
| 37 | `SKATT-001` | Folkeregisteret | Register | Register / grunndata | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |
| 38 | `SKATT-002` | Skatteetatens delingstjenester | Fellesløsning | Datadelingsløsning | Datautveksling og integrasjon: Dele data med andre<br>Informasjonsforvaltning: Informasjonsarkitektur | Ikke opprettet ennå | - |

## Kartverket (`KART`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|
| 39 | `KART-001` | Matrikkelen | Register | Register / grunndata | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |
| 40 | `KART-002` | Geonorge | Portal | Geodataportal / delingsplattform | Informasjonsforvaltning: Oversikt over datasett<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |

## EU / Europakommisjonen (`EU`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|
| 41 | `EU-001` | European Digital Identity Wallet | EU-felleskomponent | Digital identitetslommebok | Tillit: Autentisering<br>Tillit: Signering | Ikke opprettet ennå | - |
| 42 | `EU-002` | eID Building Block | EU-felleskomponent | E-identifikasjonskomponent | Tillit: Autentisering<br>Datautveksling og integrasjon: Bruke data fra andre | Ikke opprettet ennå | - |
| 43 | `EU-003` | eDelivery Building Block | EU-felleskomponent | Meldings- og dokumentutveksling | Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling | Ikke opprettet ennå | - |
| 44 | `EU-004` | eSignature Building Block | EU-felleskomponent | Signaturkomponent | Tillit: Signering<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling | Ikke opprettet ennå | - |
| 45 | `EU-005` | Once-Only Technical System (OOTS) | EU-felleskomponent | Grensekryssende datadelingsinfrastruktur | Datautveksling og integrasjon: Dele data med andre<br>Samarbeid: Organisatorisk samhandling | Ikke opprettet ennå | - |

## Ekstra verifiserte kilder brukt i denne utvidelsen
- KS Digital: https://ksdigital.no/tjenestene/fiks-plattformen/
- KS Digital: https://ksdigital.no/tjenestene/utviklingsprosjekter/felles-tjenesteplattform/
- KS Digital: https://ksdigital.no/2022/06/14/nyheter-om-fiks-digiorden/
- Feide: https://www.feide.no/om-feide
- Sikt: https://sikt.no/tjenester/felles-studentsystem-fs
- Sikt: https://sikt.no/tjenester/opptakslosninger
- Sikt: https://sikt.no/nb/tjenester/nasjonal-vitnemalsdatabase
- Sikt: https://sikt.no/tjenester/vitnemalsportalen
- Norsk helsenett: https://www.nhn.no/tjenester/helseid/hva-er-helseid
- Helsenorge: https://www.helsenorge.no/om-helsenorge-no/
- Norsk helsenett: https://www.nhn.no/tjenester/kjernejournal/om-tjenesten
- Norsk helsenett: https://www.nhn.no/tjenester/e-resept/om-e-resept
- NAV: https://www.nav.no/arbeidsgiver/aa-registeret
- NAV: https://www.nav.no/samarbeidspartner/tilgang-aa-registeret
- Skatteetaten: https://www.skatteetaten.no/deling/
- Kartverket / Geonorge: https://www.geonorge.no/Geodataarbeid/nasjonal-geodatastrategi/handlingsplanens-arsrapporter/hovedmal-2/
- Interoperable Europe: https://interoperable-europe.ec.europa.eu/collection/digital-building-blocks/solution/edelivery
- Interoperable Europe: https://interoperable-europe.ec.europa.eu/collection/digital-building-blocks/solution/esignature
- Interoperable Europe: https://interoperable-europe.ec.europa.eu/collection/digital-building-blocks/solution/eid
- Interoperable Europe: https://interoperable-europe.ec.europa.eu/collection/digital-building-blocks/solution/once-only-technical-system-oots
- Europakommisjonen: https://commission.europa.eu/topics/digital-economy-and-society/european-digital-identity_en
