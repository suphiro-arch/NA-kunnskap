# Produktregister og ressurs-ID-er

Kilde: arbeidsregister bygget fra eksisterende produktliste, siste produktversjoner i repoet og første arbeidsutkast for nye ressurseiere fra `sources/links.md`.

## Prinsipp
- `Løpenr` beholdes som stabil intern sortering og brukes fortsatt i filnavn, for eksempel `01-ID-porten-produkt-canvas-v3-codex.md`.
- `Ressurs-ID` er den nye, kanoniske identifikatoren som skal brukes i feltet `Ressurs ID` i produktbeskrivelser.
- `Ressurs-ID` bygges som `<EIERKODE>-<løpenummer hos eier>`, for eksempel `DIGDIR-001` eller `KS-003`.
- Nye produkter skal få neste ledige nummer innenfor sin eierkode. Eksisterende `Ressurs-ID` skal ikke endres uten bevisst omnummerering.
- Rader uten egen produktbeskrivelse ennå er arbeidsutkast. Der står `Siste versjon` som `Ikke opprettet ennå` og dokumentfeltet er tomt.
- Eier, type ressurs og kapabilitetstreff for nye ressurser er første arbeidsutkast og må kvalitetssikres når produktbeskrivelsene opprettes.

## Eierkoder
| Eierkode | Eier | Bruk |
|---|---|---|
| `DIGDIR` | Digdir | Digitale fellesløsninger og Altinn-relaterte løsninger som forvaltes i Digdir-regi |
| `BRREG` | Brønnøysundregistrene | Register- og samhandlingsløsninger som forvaltes av Brønnøysundregistrene |
| `KS` | KS Digital | Kommunale fellesløsninger og KS-plattformtjenester |
| `HDIR` | Helsedirektoratet | Helsedirektoratets nasjonale ressurser |
| `NAV` | NAV | NAVs fellesløsninger og API-/datatjenester |
| `SKATT` | Skatteetaten | Fellesløsninger og datatjenester forvaltet av Skatteetaten |

## Digdir (`DIGDIR`)
| Løpenr | Ressurs-ID | Navn | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|
| 1 | `DIGDIR-001` | ID-porten | Tillitstjeneste | Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Autentisering<br>Tillit: Identifisering<br>Tillit: Representasjon<br>Tjenesteutvikling: Integrerbare tjenester | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/01-ID-porten-produkt-canvas-v3-codex.md) |
| 2 | `DIGDIR-002` | Maskinporten | Tillitstjeneste | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Autentisering<br>Tillit: Tilgangskontroll | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/02-Maskinporten-produkt-canvas-v3-codex.md) |
| 3 | `DIGDIR-003` | eSignering | Tillitstjeneste | Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Autentisering<br>Tillit: Signering | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/03-eSignering-produkt-canvas-v3-codex.md) |
| 4 | `DIGDIR-004` | Altinn autorisasjon | Autorisasjonstjeneste | Tillit: Representasjon<br>Tillit: Tilgangskontroll<br>Tillit: Tilgangsstyring | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v3-codex.md) |
| 5 | `DIGDIR-005` | Kontakt- og reservasjonsregisteret | Register / grunndata | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/05-Kontakt-og-reservasjonsregisteret-produkt-canvas-v3-codex.md) |
| 6 | `DIGDIR-006` | eInnsyn | Innsynstjeneste | Samarbeid: Organisatorisk samhandling<br>Sluttbrukertjenester: Sammenhengende tjenester | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/06-eInnsyn-produkt-canvas-v3-codex.md) |
| 7 | `DIGDIR-007` | eFormidling | Formidlingstjeneste | Datautveksling: Bruke data fra andre<br>Datautveksling: Dele data med andre<br>Datautveksling: Meldingsformidling<br>Sikring av informasjonsflyt og datautveksling<br>Samhandling: Organisatorisk samhandling<br>Forvaltningsstandarder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/07-eFormidling-produkt-canvas-v2-copilot.md) |
| 8 | `DIGDIR-008` | Altinn formidling (Broker) | Formidlingstjeneste | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Samarbeid: Organisatorisk samhandling<br>Tjenesteutvikling: Integrerbare tjenester | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/08-Altinn-formidling-produkt-canvas-v2-copilot.md) |
| 9 | `DIGDIR-009` | Digital postkasse (felleskomponent) | Meldingstjeneste / innbyggerkanal | Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Sluttbrukertjenester: Sammenhengende tjenester | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/09-Digital-postkasse-produkt-canvas-v2-copilot.md) |
| 12 | `DIGDIR-010` | Altinn events (Hendelsestjeneste) | Hendelsestjeneste | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Hendelsesdrevet<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tjenesteutvikling: Integrerbare tjenester | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/12-Altinn-events-produkt-canvas-v2-copilot.md) |
| 13 | `DIGDIR-011` | Felles datakatalog | Datakatalog | Informasjonsforvaltning: Oversikt over API<br>Informasjonsforvaltning: Oversikt over begreper<br>Informasjonsforvaltning: Oversikt over datasett<br>Informasjonsforvaltning: Oversikt over informasjonsmodeller<br>Standardisering: Forvaltningsstandarder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/13-Felles-datakatalog-produkt-canvas-v2-copilot.md) |
| 14 | `DIGDIR-012` | Begrepskatalog | Begrepskatalog | Informasjonsforvaltning: Datastyring<br>Informasjonsforvaltning: Informasjonsarkitektur<br>Informasjonsforvaltning: Oversikt over begreper<br>Standardisering: Forvaltningsstandarder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/14-Begrepskatalog-produkt-canvas-v2-copilot.md) |
| 15 | `DIGDIR-013` | API-katalog | API-katalog | Informasjonsforvaltning: Informasjonsarkitektur<br>Informasjonsforvaltning: Oversikt over API<br>Standardisering: Forvaltningsstandarder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/15-API-katalog-produkt-canvas-v2-copilot.md) |
| 16 | `DIGDIR-014` | data.norge.no | Metadataportal | Informasjonsforvaltning: Oversikt over API<br>Informasjonsforvaltning: Oversikt over begreper<br>Informasjonsforvaltning: Oversikt over datasett<br>Informasjonsforvaltning: Oversikt over hendelser<br>Informasjonsforvaltning: Oversikt over informasjonsmodeller<br>Informasjonsforvaltning: Oversikt over tjenester<br>Standardisering: Forvaltningsstandarder | v4 (codex) | [Åpne](../../results/Produktbeskrivelser/16-data-norge-no-produkt-canvas-v4-codex.md) |
| 17 | `DIGDIR-015` | data.altinn.no | Datadelingsløsning | Datadrevet: Sammenstilling av data<br>Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Standardisering: Forvaltningsstandarder<br>Tillit: Autentisering<br>Tillit: Samtykke<br>Tillit: Tilgangskontroll<br>Tjenesteutvikling: Integrerbare tjenester | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/17-data-altinn-no-produkt-canvas-v3-codex.md) |
| 18 | `DIGDIR-016` | Norge.no | Veiviser / portal | Informasjonsforvaltning: Oversikt over tjenester<br>Samarbeid: Organisatorisk samhandling<br>Sluttbrukertjenester: Sammenhengende tjenester<br>Sluttbrukertjenester: Tjenestekjeder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/18-Norge-no-produkt-canvas-v2-copilot.md) |
| 19 | `DIGDIR-017` | Altinn | Plattform / portal | Samarbeid: Tjenesteforvaltning<br>Tjenesteutvikling: Gjenbrukbare tjenester<br>Tjenesteutvikling: Integrerbare tjenester | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/19-Altinn-produkt-canvas-v2-copilot.md) |
| 20 | `DIGDIR-018` | Altinn Studio | Utviklingsplattform | Tjenesteutvikling: Gjenbrukbare tjenester<br>Tjenesteutvikling: Integrerbare tjenester<br>Tjenesteutvikling: Tjenestedesign<br>Tjenesteutvikling: Utviklings- og kjÃ¸retidsmiljÃ¸ | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/20-Altinn-Studio-produkt-canvas-v2-copilot.md) |
| 21 | `DIGDIR-019` | Altinn Portal | Portal | Sluttbrukertjenester: Sammenhengende tjenester<br>Sluttbrukertjenester: Tjenestekjeder<br>Tillit: Representasjon<br>Tillit: Sporbarhet og innsyn<br>Tillit: Tilgangsstyring | v3 (codex) | [Åpne](../../results/Produktbeskrivelser/21-Altinn-Portal-produkt-canvas-v3-codex.md) |
| 22 | `DIGDIR-020` | Dialogporten | Dialogtjeneste | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Hendelsesdrevet<br>Sluttbrukertjenester: Sammenhengende tjenester<br>Tillit: Autentisering<br>Tillit: Tilgangskontroll<br>Tjenesteutvikling: Integrerbare tjenester | v4 (codex) | [Åpne](../../results/Produktbeskrivelser/22-Dialogporten-produkt-canvas-v4-codex.md) |
| 23 | `DIGDIR-021` | Altinn 3 Melding (Correspondence) | Meldingstjeneste | Datautveksling og integrasjon: Hendelsesdrevet<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Sporbarhet og innsyn<br>Tillit: Tilgangskontroll<br>Tjenesteutvikling: Integrerbare tjenester | v4 (codex) | [Åpne](../../results/Produktbeskrivelser/23-Altinn-3-Melding-produkt-canvas-v4-codex.md) |
| 24 | `DIGDIR-022` | Altinn Varslinger | Varslingstjeneste | Datadrevet: Sammenstilling av data<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Sluttbrukertjenester: Proaktive tjenester<br>Tillit: Tilgangskontroll<br>Tjenesteutvikling: Integrerbare tjenester | v4 (codex) | [Åpne](../../results/Produktbeskrivelser/24-Varslinger-produkt-canvas-v4-codex.md) |

## Brønnøysundregistrene (`BRREG`)
| Løpenr | Ressurs-ID | Navn | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|
| 10 | `BRREG-001` | ELMA (Elektronisk mottakeradresseregister) | Adresseregister | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Informasjonsforvaltning: Oversikt over tjenester<br>Standardisering: Forvaltningsstandarder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/10-ELMA-produkt-canvas-v2-copilot.md) |
| 11 | `BRREG-002` | Peppol eDelivery | Meldingsinfrastruktur | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Standardisering: EU-standarder<br>Standardisering: Forvaltningsstandarder | v2 (copilot) | [Åpne](../../results/Produktbeskrivelser/11-Peppol-eDelivery-produkt-canvas-v2-copilot.md) |

## KS Digital (`KS`)
| Løpenr | Ressurs-ID | Navn | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|
| 25 | `KS-001` | FIKS-plattformen | Samhandlingsplattform | Samarbeid: Organisatorisk samhandling<br>Tjenesteutvikling: Integrerbare tjenester | Ikke opprettet ennå | - |
| 26 | `KS-002` | FIKS Melding | Formidlingstjeneste | Datautveksling og integrasjon: Meldingsformidling<br>Samarbeid: Organisatorisk samhandling | Ikke opprettet ennå | - |
| 27 | `KS-003` | SvarUt | Utsendingstjeneste | Datautveksling og integrasjon: Meldingsformidling<br>Sluttbrukertjenester: Sammenhengende tjenester | Ikke opprettet ennå | - |
| 28 | `KS-004` | FIKS Register | Registertjeneste | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |

## Helsedirektoratet (`HDIR`)
| Løpenr | Ressurs-ID | Navn | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|
| 29 | `HDIR-001` | Helsedata.no | Datatilgangsportal | Informasjonsforvaltning: Oversikt over datasett<br>Informasjonsforvaltning: Oversikt over tjenester | Ikke opprettet ennå | - |

## NAV (`NAV`)
| Løpenr | Ressurs-ID | Navn | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|
| 30 | `NAV-001` | NAV registre og statistikk | Data- og registeroversikt | Informasjonsforvaltning: Oversikt over datasett<br>Datakilder: Grunndata | Ikke opprettet ennå | - |

## Skatteetaten (`SKATT`)
| Løpenr | Ressurs-ID | Navn | Type ressurs | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|
| 31 | `SKATT-001` | Folkeregisteret | Register / grunndata | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |
| 32 | `SKATT-002` | Digital plattforminformasjon (DPI) | Rapporterings- og datadelingstjeneste | Datautveksling og integrasjon: Dele data med andre<br>Standardisering: Forvaltningsstandarder | Ikke opprettet ennå | - |

