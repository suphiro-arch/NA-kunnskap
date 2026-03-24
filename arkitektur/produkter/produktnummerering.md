# Produktregister og ressurs-ID-er

Kilde: arbeidsregister bygget fra eksisterende produktliste, siste produktversjoner i repoet, `sources/links.md`, kuraterte eier- og navnevurderinger og ekstra offisielle kilder verifisert i denne arbeidsøkten.

## Prinsipp
- `Løpenr` beholdes som stabil intern sortering og brukes fortsatt i filnavn, for eksempel `01-ID-porten-produkt-canvas-v3-codex.md`.
- `Ressurs-ID` er den nye, kanoniske identifikatoren som skal brukes i feltet `Ressurs ID` i produktbeskrivelser.
- `Ressurs-ID` bygges som `<EIERKODE>-<løpenummer hos eier>`, for eksempel `DIGDIR-001` eller `KS-003`.
- `Ressurskategori` skiller mellom hovedtyper ressurser, som felleskomponent, fellesløsning, register, portal, plattform, internasjonal fellesressurs og referanseressurs.
- `Type ressurs` beskriver ressursen mer presist på neste nivå.
- `Merknad` brukes til korte avgrensninger, presiseringer eller viktige vurderinger som skal følge ressursen videre i analyse og produktbeskrivelse.
- Nye produkter skal få neste ledige nummer innenfor sin eierkode. Eksisterende `Ressurs-ID` skal ikke endres uten bevisst omnummerering.
- Rader uten egen produktbeskrivelse ennå er arbeidsutkast. Der står `Siste versjon` som `Ikke opprettet ennå` og dokumentfeltet er tomt.
- Eier, ressurskategori, type ressurs, merknad og kapabilitetstreff for nye ressurser er første arbeidsutkast og må kvalitetssikres når produktbeskrivelsene opprettes.

## Eierkoder
| Eierkode | Eier | Bruk |
|---|---|---|
| `DIGDIR` | Digdir | Digitale fellesløsninger og Altinn-relaterte løsninger som forvaltes i Digdir-regi |
| `BRREG` | Brønnøysundregistrene | Register- og samhandlingsløsninger som forvaltes av Brønnøysundregistrene |
| `KS` | KS Digital | Kommunale fellesløsninger og KS-plattformtjenester |
| `SIKT` | Sikt | Nasjonale fellesløsninger for utdanning og forskning |
| `HDIR` | Helsedirektoratet | Helsedirektoratets nasjonale ressurser og registre |
| `NHN` | Norsk helsenett | Nasjonale e-helseløsninger og helseinfrastruktur |
| `HELFO` | Helfo | Refusjons- og oppgjørstjenester i helsesektoren |
| `NAV` | NAV | NAVs fellesløsninger, registre og plattformer |
| `SKATT` | Skatteetaten | Fellesløsninger og datatjenester forvaltet av Skatteetaten |
| `KART` | Kartverket | Nasjonale geodata- og kartressurser |
| `SVV` | Statens vegvesen | Nasjonale veg- og kjøretøyregistre og tilhørende dataplattformer |
| `SSB` | Statistisk sentralbyrå | Felles datatjenester og analyseplattformer for statistikk og forskning |
| `FLERE` | Flere virksomheter | Samforvaltede eller tverrsektorielle løsninger med flere eiere |
| `OPP` | OpenPeppol | Internasjonale fellesressurser og styringsrammeverk for Peppol-økosystemet |
| `EU` | EU / Europakommisjonen | Relevante europeiske felleskomponenter og byggesteiner |

## Digdir (`DIGDIR`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 1 | `DIGDIR-001` | ID-porten | Felleskomponent | Autentiseringstjeneste | Kjerne felleskomponent | Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Autentisering<br>Tillit: Identifisering<br>Tillit: Representasjon<br>Tjenesteutvikling: Integrerbare tjenester | v3 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/01-ID-porten-produkt-canvas-v3-codex.md) |
| 2 | `DIGDIR-002` | Maskinporten | Felleskomponent | Maskin-til-maskin autentisering | Kjerne for API-økosystem | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Autentisering<br>Tillit: Tilgangskontroll | v3 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/02-Maskinporten-produkt-canvas-v3-codex.md) |
| 3 | `DIGDIR-003` | eSignering | Felleskomponent | Digital signering | - | Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Autentisering<br>Tillit: Signering | v3 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/03-eSignering-produkt-canvas-v3-codex.md) |
| 4 | `DIGDIR-004` | Altinn Autorisasjon | Felleskomponent | Tilgangsstyring for virksomheter | Sentral for nåringsliv | Tillit: Representasjon<br>Tillit: Tilgangskontroll<br>Tillit: Tilgangsstyring | v3 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v3-codex.md) |
| 5 | `DIGDIR-005` | Kontakt- og reservasjonsregisteret | Register | Kontaktinformasjon og reservasjon | - | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | v3 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/05-Kontakt-og-reservasjonsregisteret-produkt-canvas-v3-codex.md) |
| 6 | `DIGDIR-006` | eInnsyn | Fellesløsning | Innsynsløsning | Brukerrettet løsning med begrenset teknisk gjenbruksverdi | Samarbeid: Organisatorisk samhandling<br>Sluttbrukertjenester: Sammenhengende tjenester | v3 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/06-eInnsyn-produkt-canvas-v3-codex.md) |
| 7 | `DIGDIR-007` | eFormidling | Fellesløsning | Meldingsutveksling / transportlag | Standardisert transportlag | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Samarbeid: Organisatorisk samhandling<br>Standardisering: Forvaltningsstandarder | v3 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/07-eFormidling-produkt-canvas-v3-codex.md) |
| 8 | `DIGDIR-008` | Altinn Formidling | Fellesløsning | Meldingsbroker | Alternativ til eFormidling | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Samarbeid: Organisatorisk samhandling<br>Tjenesteutvikling: Integrerbare tjenester | v2 (copilot) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/08-Altinn-formidling-produkt-canvas-v2-copilot.md) |
| 9 | `DIGDIR-009` | Digital postkasse | Felleskomponent | Innsending av digital post | Avhenger av Digipost/e-Boks | Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Sluttbrukertjenester: Sammenhengende tjenester | v2 (copilot) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/09-Digital-postkasse-produkt-canvas-v2-copilot.md) |
| 10 | `DIGDIR-023` | ELMA | Felleskomponent | Adresseregister for eFaktura og EHF | Peppol | Datautveksling og integrasjon: Meldingsformidling<br>Tillit: Identifisering | v3 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/10-ELMA-produkt-canvas-v3-codex.md) |
| 12 | `DIGDIR-010` | Altinn Events | Felleskomponent | Hendelsestjeneste | - | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Hendelsesdrevet<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tjenesteutvikling: Integrerbare tjenester | v2 (copilot) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/12-Altinn-events-produkt-canvas-v2-copilot.md) |
| 13 | `DIGDIR-011` | Felles datakatalog | Fellesløsning | Metadata for datasett og API-er | - | Informasjonsforvaltning: Oversikt over API<br>Informasjonsforvaltning: Oversikt over begreper<br>Informasjonsforvaltning: Oversikt over datasett<br>Informasjonsforvaltning: Oversikt over informasjonsmodeller<br>Standardisering: Forvaltningsstandarder | v2 (copilot) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/13-Felles-datakatalog-produkt-canvas-v2-copilot.md) |
| 14 | `DIGDIR-012` | Begrepskatalog | Fellesløsning | Felles begreper | Del av datakatalog | Informasjonsforvaltning: Datastyring<br>Informasjonsforvaltning: Informasjonsarkitektur<br>Informasjonsforvaltning: Oversikt over begreper<br>Standardisering: Forvaltningsstandarder | v2 (copilot) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/14-Begrepskatalog-produkt-canvas-v2-copilot.md) |
| 15 | `DIGDIR-013` | API-katalog | Fellesløsning | Oversikt over API-er | Del av datakatalog | Informasjonsforvaltning: Informasjonsarkitektur<br>Informasjonsforvaltning: Oversikt over API<br>Standardisering: Forvaltningsstandarder | v2 (copilot) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/15-API-katalog-produkt-canvas-v2-copilot.md) |
| 16 | `DIGDIR-014` | data.norge.no | Portal | Portal for åpne data | Frontend til kataloger | Informasjonsforvaltning: Oversikt over API<br>Informasjonsforvaltning: Oversikt over begreper<br>Informasjonsforvaltning: Oversikt over datasett<br>Informasjonsforvaltning: Oversikt over hendelser<br>Informasjonsforvaltning: Oversikt over informasjonsmodeller<br>Informasjonsforvaltning: Oversikt over tjenester<br>Standardisering: Forvaltningsstandarder | v4 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/16-data-norge-no-produkt-canvas-v4-codex.md) |
| 17 | `DIGDIR-015` | data.altinn.no | Fellesløsning | Portal for deling i Altinn-økosystemet | API- og delingsflate i Altinn-økosystemet | Datadrevet: Sammenstilling av data<br>Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Standardisering: Forvaltningsstandarder<br>Tillit: Autentisering<br>Tillit: Samtykke<br>Tillit: Tilgangskontroll<br>Tjenesteutvikling: Integrerbare tjenester | v3 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/17-data-altinn-no-produkt-canvas-v3-codex.md) |
| 18 | `DIGDIR-016` | Norge.no | Portal | Innbyggerportal | Informasjonskanal | Informasjonsforvaltning: Oversikt over tjenester<br>Sluttbrukertjenester: Sammenhengende tjenester<br>Sluttbrukertjenester: Tjenestekjeder<br>Tjenesteutvikling: Tjenestedesign | v3 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/18-Norge-no-produkt-canvas-v3-codex.md) |
| 19 | `DIGDIR-017` | Altinn 3 plattform | Plattform | Plattform for tjenester og samhandling | Erstatter «Altinn» som operativ plattformbetegnelse | Samarbeid: Tjenesteforvaltning<br>Tjenesteutvikling: Gjenbrukbare tjenester<br>Tjenesteutvikling: Integrerbare tjenester | v2 (copilot) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/19-Altinn-produkt-canvas-v2-copilot.md) |
| 20 | `DIGDIR-018` | Altinn Studio | Plattform | Utviklingsverktøy | - | Tjenesteutvikling: Gjenbrukbare tjenester<br>Tjenesteutvikling: Integrerbare tjenester<br>Tjenesteutvikling: Tjenestedesign<br>Tjenesteutvikling: Utviklings- og kjøretidsmiljø | v2 (copilot) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/20-Altinn-Studio-produkt-canvas-v2-copilot.md) |
| 22 | `DIGDIR-020` | Dialogporten | Fellesløsning | Dialog-API | Tverrgående dialogmodell | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Hendelsesdrevet<br>Sluttbrukertjenester: Sammenhengende tjenester<br>Tillit: Autentisering<br>Tillit: Tilgangskontroll<br>Tjenesteutvikling: Integrerbare tjenester | v4 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/22-Dialogporten-produkt-canvas-v4-codex.md) |
| 23 | `DIGDIR-021` | Altinn Melding | Fellesløsning | Digital meldingsboks | Correspondence | Datautveksling og integrasjon: Hendelsesdrevet<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Sporbarhet og innsyn<br>Tillit: Tilgangskontroll<br>Tjenesteutvikling: Integrerbare tjenester | v4 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/23-Altinn-3-Melding-produkt-canvas-v4-codex.md) |
| 24 | `DIGDIR-022` | Altinn Varsling | Fellesløsning | Varsling (SMS/e-post) | - | Datadrevet: Sammenstilling av data<br>Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Sluttbrukertjenester: Proaktive tjenester<br>Tillit: Tilgangskontroll<br>Tjenesteutvikling: Integrerbare tjenester | v4 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/24-Varslinger-produkt-canvas-v4-codex.md) |
| 56 | `DIGDIR-024` | eIDAS-node (Norge) | Felleskomponent | Grensekryssende eID | EU-integrasjon | Datautveksling og integrasjon: Bruke data fra andre<br>Tillit: Autentisering<br>Tillit: Identifisering | Ikke opprettet ennå | - |

## Br?nn?ysundregistrene (`BRREG`)
| L?penr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 46 | `BRREG-003` | Enhetsregisteret | Register | Virksomhetsregister | Grunndata | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet enn? | - |

## KS Digital (`KS`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 25 | `KS-001` | FIKS-plattformen | Plattform | Integrasjonsplattform | Kommunal fellesplattform | Samarbeid: Organisatorisk samhandling<br>Tjenesteutvikling: Integrerbare tjenester<br>Tjenesteutvikling: Utviklings- og kjøretidsmiljø | v1 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/25-FIKS-plattformen-produkt-canvas-v1-codex.md) |
| 26 | `KS-002` | FIKS Melding | Fellesløsning | Meldingsutveksling | - | Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Samarbeid: Organisatorisk samhandling | v1 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/26-FIKS-Melding-produkt-canvas-v1-codex.md) |
| 27 | `KS-003` | SvarUt | Fellesløsning | Utgående post | API-basert tjeneste | Datautveksling og integrasjon: Meldingsformidling<br>Samarbeid: Organisatorisk samhandling<br>Sluttbrukertjenester: Sammenhengende tjenester | v2 (copilot) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/27-SvarUt-produkt-canvas-v2-copilot.md) |
| 28 | `KS-004` | FIKS Register | Fellesløsning | Oppslagsregister | Overordnet registerfamilie i FIKS | Datakilder: Grunndata<br>Datautveksling og integrasjon: Bruke data fra andre | v1 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/28-FIKS-Register-produkt-canvas-v1-codex.md) |
| 29 | `KS-005` | Felles tjenesteplattform | Plattform | Kommunal tjenesteplattform | Under utvikling | Samarbeid: Organisatorisk samhandling<br>Tjenesteutvikling: Gjenbrukbare tjenester<br>Tjenesteutvikling: Utviklings- og kjøretidsmiljø | v1 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/29-Felles-tjenesteplattform-produkt-canvas-v1-codex.md) |
| 30 | `KS-006` | Fiks Digiorden | Fellesløsning | Digital bestilling | Sektorspesifikk | Informasjonsforvaltning: Datastyring<br>Informasjonsforvaltning: Oversikt over datasett<br>Informasjonsforvaltning: Oversikt over tjenester | v1 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/30-Fiks-Digiorden-produkt-canvas-v1-codex.md) |
| 57 | `KS-007` | SvarInn | Fellesløsning | Inngående post | API-basert tjeneste; komplement til SvarUt | Datautveksling og integrasjon: Meldingsformidling<br>Samarbeid: Organisatorisk samhandling | v1 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/57-SvarInn-produkt-canvas-v1-codex.md) |
| 67 | `KS-008` | FIKS Folkeregister | Fellesløsning | Tilgang til Folkeregisteret via FIKS | Viktig integrasjon i kommunal sektor | Datakilder: Grunndata<br>Datautveksling og integrasjon: Bruke data fra andre | v1 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/67-FIKS-Folkeregister-produkt-canvas-v1-codex.md) |

## Sikt (`SIKT`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 47 | `SIKT-001` | Feide | Felleskomponent | Autentisering | - | Datautveksling og integrasjon: Dele data med andre<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Autentisering<br>Tillit: Tilgangskontroll | v1 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/47-Feide-produkt-canvas-v1-codex.md) |
| 48 | `SIKT-002` | Felles studentsystem (FS) | Plattform | Studentdata | - | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Informasjonsforvaltning: Datastyring<br>Samarbeid: Organisatorisk samhandling | Ikke opprettet ennå | - |
| 49 | `SIKT-003` | Opptaksløsninger | Fellesløsning | Opptaksløsning | - | Datautveksling og integrasjon: Bruke data fra andre<br>Samarbeid: Organisatorisk samhandling<br>Sluttbrukertjenester: Sammenhengende tjenester | Ikke opprettet ennå | - |
| 50 | `SIKT-004` | Nasjonal vitnemålsdatabase (NVB) | Register | Vitnemål | Backend | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |
| 51 | `SIKT-005` | Vitnemålsportalen | Portal | Deling av vitnemål | - | Datautveksling og integrasjon: Dele data med andre<br>Sluttbrukertjenester: Sammenhengende tjenester | v1 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/51-Vitnemalsportalen-produkt-canvas-v1-codex.md) |
| 52 | `SIKT-006` | Nasjonalt utdanningsregister | Register | Register over utdanningstilbud og akkreditering | - | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre<br>Informasjonsforvaltning: Datastyring | Ikke opprettet ennå | - |

## Helsedirektoratet (`HDIR`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 31 | `HDIR-001` | Helsedata.no | Portal | Datatilgang | Erstatter HAP | Informasjonsforvaltning: Oversikt over datasett<br>Informasjonsforvaltning: Datastyring<br>Sluttbrukertjenester: Sammenhengende tjenester | Ikke opprettet ennå | - |
| 64 | `HDIR-002` | HPR | Register | Register over helsepersonell | - | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |

## Norsk helsenett (`NHN`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 32 | `NHN-001` | Helsenorge | Portal | Innbyggerportal | - | Sluttbrukertjenester: Sammenhengende tjenester<br>Sluttbrukertjenester: Tjenestekjeder | Ikke opprettet ennå | - |
| 33 | `NHN-002` | HelseID | Felleskomponent | Autentisering i helse | - | Datautveksling og integrasjon: Bruke data fra andre<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Tillit: Autentisering<br>Tillit: Tilgangskontroll | Ikke opprettet ennå | - |
| 34 | `NHN-003` | Kjernejournal | Fellesløsning | Pasientdata | - | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Samarbeid: Organisatorisk samhandling | Ikke opprettet ennå | - |
| 35 | `NHN-004` | e-resept | Fellesløsning | Reseptsystem | - | Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Meldingsformidling<br>Samarbeid: Organisatorisk samhandling | Ikke opprettet ennå | - |

## HELFO (`HELFO`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 65 | `HELFO-001` | KUHR | Register | Refusjonsdata | - | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |

## NAV (`NAV`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 36 | `NAV-001` | Aa-registeret | Register | Arbeidsforhold | Del av A-ordningen | Datakilder: Grunndata<br>Datautveksling og integrasjon: Bruke data fra andre<br>Datautveksling og integrasjon: Dele data med andre<br>Sluttbrukertjenester: Sammenhengende tjenester | Ikke opprettet ennå | - |
| 66 | `NAV-002` | NAIS | Plattform | Plattform for applikasjoner | Kubernetes-basert, gjenbrukbar modell | Tjenesteutvikling: Gjenbrukbare tjenester<br>Tjenesteutvikling: Utviklings- og kjøretidsmiljø | Ikke opprettet ennå | - |

## Skatteetaten (`SKATT`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 37 | `SKATT-001` | Folkeregisteret | Register | Persondata | Grunndata | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |
| 38 | `SKATT-002` | Skatteetatens delingstjenester | Fellesløsning | API-basert deling | - | Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |

## Kartverket (`KART`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 39 | `KART-001` | Matrikkelen | Register | Eiendom | Grunndata | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |
| 40 | `KART-002` | Geonorge | Portal | Geodataportal / metadata- og delingsplattform | - | Informasjonsforvaltning: Oversikt over datasett<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |

## Statens vegvesen (`SVV`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 60 | `SVV-001` | Motorvognregisteret | Register | Kjøretøydata | Viktig sektorregister | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre | Ikke opprettet ennå | - |
| 61 | `SVV-002` | NVDB | Fellesløsning | Vegdata | Dataplattform | Datakilder: Grunndata<br>Informasjonsforvaltning: Oversikt over datasett | Ikke opprettet ennå | - |

## SSB (`SSB`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 63 | `SSB-001` | microdata.no | Fellesløsning | Analyseplattform | Forskning | Datadrevet: Sammenstilling av data<br>Datautveksling og integrasjon: Bruke data fra andre | Ikke opprettet ennå | - |

## Flere virksomheter (`FLERE`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 59 | `FLERE-001` | A-ordningen | Fellesløsning | Felles rapportering | Kritisk datakilde | Datakilder: Grunndata<br>Datautveksling og integrasjon: Dele data med andre<br>Samarbeid: Organisatorisk samhandling | Ikke opprettet ennå | - |
| 62 | `FLERE-002` | DSOP-tjenester | Fellesløsning | Offentlig–privat datadeling | Bank/offentlig samarbeid | Datautveksling og integrasjon: Dele data med andre<br>Samarbeid: Organisatorisk samhandling | Ikke opprettet ennå | - |

## OpenPeppol (`OPP`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 11 | `OPP-001` | Peppol eDelivery | Internasjonal fellesressurs | Internasjonalt samhandlingsrammeverk | Internasjonal standard; Digdir er nasjonal Peppol Authority | Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling<br>Standardisering: Forvaltningsstandarder<br>Tillit: Identifisering | v3 (codex) | [Åpne](../../arkitektur/produkter/produktbeskrivelser/11-Peppol-eDelivery-produkt-canvas-v3-codex.md) |

## EU / Europakommisjonen (`EU`)
| Løpenr | Ressurs-ID | Navn | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|
| 41 | `EU-001` | European Digital Identity Wallet | EU-felleskomponent | Digital identitetslommebok | - | Tillit: Autentisering<br>Tillit: Signering | Ikke opprettet ennå | - |
| 42 | `EU-002` | eID Building Block | EU-felleskomponent | E-identifikasjonskomponent | - | Tillit: Autentisering<br>Datautveksling og integrasjon: Bruke data fra andre | Ikke opprettet ennå | - |
| 43 | `EU-003` | eDelivery Building Block | EU-felleskomponent | Byggestein / referanseramme for eDelivery | - | Datautveksling og integrasjon: Meldingsformidling<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling | Ikke opprettet ennå | - |
| 44 | `EU-004` | eSignature Building Block | EU-felleskomponent | Signaturkomponent | - | Tillit: Signering<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling | Ikke opprettet ennå | - |
| 45 | `EU-005` | Once-Only Technical System (OOTS) | EU-felleskomponent | Grensekryssende datadelingsinfrastruktur | - | Datautveksling og integrasjon: Dele data med andre<br>Samarbeid: Organisatorisk samhandling | Ikke opprettet ennå | - |
| 53 | `EU-006` | EU Open Source Solutions Catalogue | Referanseressurs | Åpen kildekode-katalog for offentlig sektor | - | Tjenesteutvikling: Gjenbrukbare tjenester<br>Tjenesteutvikling: Integrerbare tjenester | Ikke opprettet ennå | - |
| 54 | `EU-007` | Interoperable Europe Solutions | Referanseressurs | Løsningskatalog for interoperabilitet | - | Samarbeid: Samarbeidsarenaer og nettverk<br>Standardisering: Forvaltningsstandarder | Ikke opprettet ennå | - |
| 55 | `EU-008` | Core Vocabularies | Referanseressurs | Semantisk interoperabilitetsressurs | - | Informasjonsforvaltning: Informasjonsarkitektur<br>Standardisering: Forvaltningsstandarder | Ikke opprettet ennå | - |

## Ekstra verifiserte kilder brukt i denne utvidelsen
- Digdir: https://www.digdir.no/digital-identitet/eidas/
- KS Digital: https://ksdigital.no/tjenester/svarinn/
- NAV / NAIS: https://nais.io/
- A-ordningen: https://www.a-ordningen.no/
- Statens vegvesen - Motorvognregisteret: https://www.vegvesen.no/kjoretoy/kjop-og-salg/kjoretoyopplysninger/
- Statens vegvesen - NVDB: https://www.vegvesen.no/fag/fokusomrader/nasjonal-vegdatabank/
- microdata.no: https://www.microdata.no/
- Helsedirektoratet - HPR: https://www.helsedirektoratet.no/tema/autorisasjon-og-spesialistutdanning/helsepersonellregisteret
- Helfo - KUHR: https://www.helfo.no/om-helfo/kuhr
- FS: https://www.fs.no/
- Vitnemålsportalen: https://www.vitnemalsportalen.no/
