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
| `FHI` | Folkehelseinstituttet | Nasjonale helseregistre og smittevernrelaterte dataressurser |
| `NHN` | Norsk helsenett | Nasjonale e-helseløsninger og helseinfrastruktur |
| `HELFO` | Helfo | Refusjons- og oppgjørstjenester i helsesektoren |
| `NAV` | NAV | NAVs fellesløsninger, registre og plattformer |
| `SKATT` | Skatteetaten | Fellesløsninger og datatjenester forvaltet av Skatteetaten |
| `KART` | Kartverket | Nasjonale geodata- og kartressurser |
| `SVV` | Statens vegvesen | Nasjonale veg- og kjøretøyregistre og tilhørende dataplattformer |
| `SSB` | Statistisk sentralbyrå | Felles datatjenester og analyseplattformer for statistikk og forskning |
| `FLERE` | Flere virksomheter | Samforvaltede eller tverrsektorielle løsninger med flere eiere |
| `NOVARI` | Novari IKS | Fylkeskommunale fellesressurser og løsninger forvaltet av Novari |
| `OPP` | OpenPeppol | Internasjonale fellesressurser og styringsrammeverk for Peppol-økosystemet |
| `EU` | EU / Europakommisjonen | Relevante europeiske felleskomponenter og byggesteiner |



## Digdir (`DIGDIR`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 1 | `DIGDIR-001` | ID-porten | Autentiseringstjeneste | Sikring av informasjonsflyt og datautveksling<br>Autentisering<br>Identifisering<br>Representasjon<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/01-ID-porten-produkt-canvas-v3-codex.md) |
| 2 | `DIGDIR-002` | Maskinporten | Maskin-til-maskin autentisering | Bruke data fra andre<br>Dele data med andre<br>Sikring av informasjonsflyt og datautveksling<br>Autentisering<br>Tilgangskontroll | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/02-Maskinporten-produkt-canvas-v3-codex.md) |
| 3 | `DIGDIR-003` | eSignering | Digital signering | Sikring av informasjonsflyt og datautveksling<br>Autentisering<br>Signering | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/03-eSignering-produkt-canvas-v3-codex.md) |
| 4 | `DIGDIR-004` | Altinn Autorisasjon | Autorisasjonstjeneste for representasjon og tilgang | Representasjon<br>Tilgangskontroll<br>Tilgangsstyring | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/04-Altinn-autorisasjon-produkt-canvas-v4-codex.md) |
| 5 | `DIGDIR-005` | Kontakt- og reservasjonsregisteret | Kontaktinformasjon og reservasjon | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/05-Kontakt-og-reservasjonsregisteret-produkt-canvas-v3-codex.md) |
| 6 | `DIGDIR-006` | eInnsyn | Innsynsløsning | Organisatorisk samhandling<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/06-eInnsyn-produkt-canvas-v3-codex.md) |
| 7 | `DIGDIR-007` | eFormidling | Meldingsutveksling / transportlag | Bruke data fra andre<br>Dele data med andre<br>Meldingsformidling<br>Sikring av informasjonsflyt og datautveksling<br>Organisatorisk samhandling<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/07-eFormidling-produkt-canvas-v3-codex.md) |
| 8 | `DIGDIR-008` | Altinn Formidling | Formidlingstjeneste for filer | Bruke data fra andre<br>Dele data med andre<br>Meldingsformidling<br>Sikring av informasjonsflyt og datautveksling<br>Organisatorisk samhandling<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/08-Altinn-formidling-produkt-canvas-v3-codex.md) |
| 9 | `DIGDIR-009` | Digital postkasse | Utsendingstjeneste for digital og fysisk post til innbyggere | Meldingsformidling<br>Sikring av informasjonsflyt og datautveksling<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/09-Digital-postkasse-produkt-canvas-v3-codex.md) |
| 10 | `DIGDIR-023` | ELMA | Adresseregister for eFaktura og EHF | Meldingsformidling<br>Identifisering | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/10-ELMA-produkt-canvas-v3-codex.md) |
| 12 | `DIGDIR-010` | Altinn Events | Hendelsestjeneste | Bruke data fra andre<br>Dele data med andre<br>Hendelsesdrevet<br>Sikring av informasjonsflyt og datautveksling<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/12-Altinn-events-produkt-canvas-v3-codex.md) |
| 13 | `DIGDIR-011` | Felles datakatalog | Metadata- og publiseringsløsning for dataressurser | Oversikt over API<br>Oversikt over begreper<br>Oversikt over datasett<br>Oversikt over informasjonsmodeller<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/13-Felles-datakatalog-produkt-canvas-v3-codex.md) |
| 14 | `DIGDIR-012` | Begrepskatalog | Delkatalog for begrepsbeskrivelser | Datastyring<br>Informasjonsarkitektur<br>Oversikt over begreper<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/14-Begrepskatalog-produkt-canvas-v3-codex.md) |
| 15 | `DIGDIR-013` | API-katalog | Delkatalog for API-beskrivelser | Informasjonsarkitektur<br>Oversikt over API<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/15-API-katalog-produkt-canvas-v3-codex.md) |
| 16 | `DIGDIR-014` | data.norge.no | Portal for åpne data | Oversikt over API<br>Oversikt over begreper<br>Oversikt over datasett<br>Oversikt over hendelser<br>Oversikt over informasjonsmodeller<br>Oversikt over tjenester<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/16-data-norge-no-produkt-canvas-v4-codex.md) |
| 17 | `DIGDIR-015` | data.altinn.no | Kontrollert datadelingstjeneste | Sammenstilling av data<br>Bruke data fra andre<br>Dele data med andre<br>Sikring av informasjonsflyt og datautveksling<br>Forvaltningsstandarder<br>Autentisering<br>Samtykke<br>Tilgangskontroll<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/17-data-altinn-no-produkt-canvas-v4-codex.md) |
| 18 | `DIGDIR-016` | Norge.no | Innbyggerportal | Oversikt over tjenester<br>Sammenhengende tjenester<br>Tjenestekjeder<br>Tjenestedesign | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/18-Norge-no-produkt-canvas-v3-codex.md) |
| 19 | `DIGDIR-017` | Altinn 3 plattform | Plattform for utvikling, kjøring og samhandling | Tjenesteforvaltning<br>Gjenbrukbare tjenester<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/19-Altinn-produkt-canvas-v3-codex.md) |
| 20 | `DIGDIR-018` | Altinn Studio | Utviklingsflate for tjenester | Gjenbrukbare tjenester<br>Integrerbare tjenester<br>Tjenestedesign<br>Utviklings- og kjøretidsmiljø | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/20-Altinn-Studio-produkt-canvas-v3-codex.md) |
| 22 | `DIGDIR-020` | Dialogporten | Dialogtjeneste og representasjonslag | Bruke data fra andre<br>Hendelsesdrevet<br>Sammenhengende tjenester<br>Autentisering<br>Tilgangskontroll<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/22-Dialogporten-produkt-canvas-v5-codex.md) |
| 23 | `DIGDIR-021` | Altinn Melding | Korrespondansetjeneste | Hendelsesdrevet<br>Meldingsformidling<br>Sikring av informasjonsflyt og datautveksling<br>Sporbarhet og innsyn<br>Tilgangskontroll<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/23-Altinn-3-Melding-produkt-canvas-v5-codex.md) |
| 24 | `DIGDIR-022` | Altinn Varsling | Varslingstjeneste (SMS/e-post) | Sammenstilling av data<br>Meldingsformidling<br>Sikring av informasjonsflyt og datautveksling<br>Proaktive tjenester<br>Tilgangskontroll<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/24-Varslinger-produkt-canvas-v5-codex.md) |
| 56 | `DIGDIR-024` | eIDAS-node (Norge) | Grensekryssende eID | Bruke data fra andre<br>Autentisering<br>Identifisering | - |
| 85 | `DIGDIR-025` | Rammeverk for digital samhandling | Rammeverk | Forvaltningsstandarder<br>Dele data med andre<br>Organisatorisk samhandling | - |
| 86 | `DIGDIR-026` | Referansekatalogen for IT-standarder | Standardkatalog | Forvaltningsstandarder<br>Informasjonsarkitektur | - |
| 87 | `DIGDIR-027` | Arkitektur for hendelser | Referansearkitektur | Hendelsesdrevet<br>Forvaltningsstandarder | - |
| 88 | `DIGDIR-028` | Arkitektur- og standardiseringsrådet | Arkitekturråd | Samarbeidsarenaer og nettverk<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/samarbeidsfora/88-Arkitektur-og-standardiseringsradet-v1-codex.md) |
| 89 | `DIGDIR-029` | Rammeverk for informasjonsforvaltning | Rammeverk | Datastyring<br>Informasjonsarkitektur<br>Forvaltningsstandarder | - |
| 98 | `DIGDIR-030` | Overordnede arkitekturprinsipper for offentlig sektor | Prinsipper | Forvaltningsstandarder<br>Arkitekturstyring | [Åpne](../../arkitektur/ressurser/normerende-ressurser/98-Overordnede-arkitekturprinsipper-for-offentlig-sektor-v0-codex.md) |
| 99 | `DIGDIR-031` | Sjekkliste for sammenhengende tjenester | Veileder | Sammenhengende tjenester<br>Tjenestedesign | [Åpne](../../arkitektur/ressurser/normerende-ressurser/99-Sjekkliste-for-sammenhengende-tjenester-v0-codex.md) |
| 100 | `DIGDIR-032` | Kart for tjenestekjeder | Metodeverktøy | Tjenestekjeder<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/normerende-ressurser/100-Kart-for-tjenestekjeder-v0-codex.md) |
| 101 | `DIGDIR-033` | Referansearkitektur forsendelse (eMelding) | Referansearkitektur | Meldingsformidling<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/normerende-ressurser/101-Referansearkitektur-forsendelse-eMelding-v0-codex.md) |
| 102 | `DIGDIR-034` | Referansearkitektur forespørsel-svar (eOppslag) | Referansearkitektur | Bruke data fra andre<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/normerende-ressurser/102-Referansearkitektur-foresporsel-svar-eOppslag-v0-codex.md) |
| 103 | `DIGDIR-035` | Nasjonalt veikart | Veikart | Samordning<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/normerende-ressurser/103-Nasjonalt-veikart-v0-codex.md) |
| 104 | `DIGDIR-036` | Orden i eget hus | Metodikk | Datastyring<br>Oversikt over datasett | [Åpne](../../arkitektur/ressurser/normerende-ressurser/104-Orden-i-eget-hus-v0-codex.md) |
| 105 | `DIGDIR-037` | Rammeverk - nasjonale grunndata | Rammeverk | Grunndata<br>Samordning | [Åpne](../../arkitektur/ressurser/normerende-ressurser/105-Rammeverk-nasjonale-grunndata-v0-codex.md) |
| 106 | `DIGDIR-038` | Nasjonal verktøykasse for deling av data | Veileder | Dele data med andre<br>Datastyring | [Åpne](../../arkitektur/ressurser/normerende-ressurser/106-Nasjonal-verktoykasse-for-deling-av-data-v0-codex.md) |
| 107 | `DIGDIR-039` | Kunnskapsgrunnlag og KPI-er datadeling | Kunnskapsgrunnlag | Samordning<br>Datastyring | [Åpne](../../arkitektur/ressurser/normerende-ressurser/107-Kunnskapsgrunnlag-og-KPI-er-datadeling-v0-codex.md) |
| 108 | `DIGDIR-040` | Kunnskapsgrunnlag - dataspaces | Kunnskapsgrunnlag | Samarbeidsarenaer og nettverk<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/normerende-ressurser/108-Kunnskapsgrunnlag-dataspaces-v0-codex.md) |
| 109 | `DIGDIR-041` | Kapabilitetskart (planlagt) | Kapabilitetsmodell | Arkitekturstyring<br>Datastyring | [Åpne](../../arkitektur/ressurser/normerende-ressurser/109-Kapabilitetskart-planlagt-v0-codex.md) |
| 110 | `DIGDIR-042` | Skate | Tverrsektoriell samordningsarena | Samarbeidsarenaer og nettverk<br>Samordning | [Åpne](../../arkitektur/ressurser/samarbeidsfora/110-Skate-v1-codex.md) |
| 111 | `DIGDIR-043` | Digitaliseringsradet | Radgivende arena | Samarbeidsarenaer og nettverk<br>Arkitekturstyring | [Åpne](../../arkitektur/ressurser/samarbeidsfora/111-Digitaliseringsradet-v1-codex.md) |
| 112 | `DIGDIR-044` | Digitaliseringsrundskrivet | Rundskriv | Samordning<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/normerende-ressurser/112-Digitaliseringsrundskrivet-v1-codex.md) |
| 113 | `DIGDIR-045` | Prosjektveiviseren | Prosjektmetodikk | Samordning<br>Tjenestedesign | [Åpne](../../arkitektur/ressurser/normerende-ressurser/113-Prosjektveiviseren-v1-codex.md) |
| 114 | `DIGDIR-046` | Klart språk | Veileder | Sammenhengende tjenester<br>Tjenestedesign | [Åpne](../../arkitektur/ressurser/normerende-ressurser/114-Klart-sprak-v0-codex.md) |
| 115 | `DIGDIR-047` | Digitaliseringsvennlig regelverk | Veileder | Forvaltningsstandarder<br>Arkitekturstyring | [Åpne](../../arkitektur/ressurser/normerende-ressurser/115-Digitaliseringsvennlig-regelverk-v0-codex.md) |
| 116 | `DIGDIR-048` | Rammeverk for innovasjon i offentlig sektor | Rammeverk | Samordning<br>Tjenestedesign | [Åpne](../../arkitektur/ressurser/normerende-ressurser/116-Rammeverk-for-innovasjon-i-offentlig-sektor-v0-codex.md) |
| 117 | `DIGDIR-049` | Kompetansemodell for digital transformasjon | Kompetansemodell | Samordning<br>Tjenestedesign | [Åpne](../../arkitektur/ressurser/normerende-ressurser/117-Kompetansemodell-for-digital-transformasjon-v0-codex.md) |
| 118 | `DIGDIR-050` | Felles designsystem | Designsystem | Sammenhengende tjenester<br>Gjenbrukbare tjenester<br>Tjenestedesign | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/118-Felles-designsystem-v1-codex.md) |
| 119 | `DIGDIR-051` | Ansattporten | Autentiseringstjeneste for ansatte | Sikring av informasjonsflyt og datautveksling<br>Autentisering<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/119-Ansattporten-v1-codex.md) |
| 120 | `DIGDIR-052` | Styringsrådet for fellesløsningene | Styringsråd | Samarbeidsarenaer og nettverk<br>Samordning | [Åpne](../../arkitektur/ressurser/samarbeidsfora/120-Styringsradet-for-felleslosningene-v1-codex.md) |
| 121 | `DIGDIR-053` | Faglig arena for informasjonsforvaltning og deling av data | Faglig forum | Datastyring<br>Samarbeidsarenaer og nettverk | [Åpne](../../arkitektur/ressurser/samarbeidsfora/121-Faglig-arena-for-informasjonsforvaltning-og-deling-av-data-v1-codex.md) |
| 122 | `DIGDIR-054` | NIFS | Nettverk for informasjonssikkerhet | Sikring av informasjonsflyt og datautveksling<br>Samarbeidsarenaer og nettverk | [Åpne](../../arkitektur/ressurser/samarbeidsfora/122-NIFS-v0-codex.md) |
| 123 | `DIGDIR-055` | DSOP-samarbeidet | Offentlig-privat samhandlingsarena | Dele data med andre<br>Samarbeidsarenaer og nettverk | [Åpne](../../arkitektur/ressurser/samarbeidsfora/123-DSOP-samarbeidet-v0-codex.md) |
| 124 | `DIGDIR-056` | Felles sikkerhet i forvaltningen | Tverrsektorielt sikkerhetssamarbeid | Sikring av informasjonsflyt og datautveksling<br>Samarbeidsarenaer og nettverk<br>Samordning | [Åpne](../../arkitektur/ressurser/samarbeidsfora/124-Felles-sikkerhet-i-forvaltningen-v0-codex.md) |
| 125 | `DIGDIR-057` | KI Norge | Nasjonal arena for kunstig intelligens | Samarbeidsarenaer og nettverk<br>Samordning | [Åpne](../../arkitektur/ressurser/samarbeidsfora/125-KI-Norge-v0-codex.md) |
| 126 | `DIGDIR-058` | Nasjonal sandkasse for digital lommebok | Sandkasse og testmiljø for digital lommebok | Autentisering<br>Signering<br>Utviklings- og kjøretidsmiljø<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/126-Nasjonal-sandkasse-for-digital-lommebok-produkt-canvas-v1-codex.md) |
| 127 | `DIGDIR-059` | Samarbeidsportalen | Portal for forvaltning, informasjon og ta-i-bruk av fellesløsninger | Oversikt over tjenester<br>Tjenesteforvaltning<br>Samarbeidsarenaer og nettverk | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/127-Samarbeidsportalen-produkt-canvas-v1-codex.md) |

## Brønnøysundregistrene (`BRREG`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 46 | `BRREG-003` | Enhetsregisteret | Virksomhetsregister | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/46-Enhetsregisteret-produkt-canvas-v1-codex.md) |



## KS Digital (`KS`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 25 | `KS-001` | Fiks-plattformen | Integrasjonsplattform | Organisatorisk samhandling<br>Integrerbare tjenester<br>Utviklings- og kjøretidsmiljø | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/25-FIKS-plattformen-produkt-canvas-v1-codex.md) |
| 26 | `KS-002` | Fiks melding | Meldingsutveksling | Meldingsformidling<br>Sikring av informasjonsflyt og datautveksling<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/26-FIKS-Melding-produkt-canvas-v2-codex.md) |
| 27 | `KS-003` | Fiks SvarUt | Utsendingstjeneste for digital og fysisk post | Meldingsformidling<br>Organisatorisk samhandling<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/27-FIKS-SvarUt-produkt-canvas-v3-codex.md) |
| 28 | `KS-004` | Fiks register | Registertilgang | Grunndata<br>Bruke data fra andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v2-codex.md) |
| 30 | `KS-006` | Fiks digiorden | Styrings- og oversiktsløsning | Datastyring<br>Oversikt over datasett<br>Oversikt over tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/30-FIKS-Digiorden-produkt-canvas-v1-codex.md) |
| 57 | `KS-007` | SvarInn | Inngående post | Meldingsformidling<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/57-SvarInn-produkt-canvas-v1-codex.md) |
| 67 | `KS-008` | Fiks folkeregister | Tilgang til Folkeregisteret via Fiks | Grunndata<br>Bruke data fra andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/67-FIKS-Folkeregister-produkt-canvas-v1-codex.md) |
| 68 | `KS-009` | Fiks skatte- og inntektsopplysninger | Tilgang til skatte- og inntektsopplysninger via Fiks | Grunndata<br>Bruke data fra andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v1-codex.md) |
| 69 | `KS-010` | Fiks kjøretøyregister | Tilgang til kjøretøyopplysninger via Fiks | Grunndata<br>Bruke data fra andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/69-FIKS-Kjoretoyregister-produkt-canvas-v1-codex.md) |
| 74 | `KS-011` | Felles mal for innforing av digitale fellestjenester | Innforingsveileder | Organisatorisk samhandling<br>Forvaltningsstandarder | - |
| 93 | `KS-012` | Fiks Digisos | Tjeneste for digital sosialhjelp | Organisatorisk samhandling<br>Sammenhengende tjenester<br>Dele data med andre | - |
| 94 | `KS-013` | Fiks Protokoll | Saks- og motestotte for politiske organer | Organisatorisk samhandling<br>Datastyring | - |
| 95 | `KS-014` | Fiks Vaksine | Kommunal vaksineforvaltning | Sammenhengende tjenester<br>Dele data med andre | - |
| 96 | `KS-015` | KS Bekymringsmelding | Digital meldingstjeneste for bekymringsmeldinger | Meldingsformidling<br>Organisatorisk samhandling<br>Sammenhengende tjenester | - |
| 97 | `KS-016` | MinKommune | Innbyggerportal for kommunale tjenester | Sammenhengende tjenester<br>Tjenestekjeder | - |



## Sikt (`SIKT`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 47 | `SIKT-001` | Feide | Autentisering | Dele data med andre<br>Sikring av informasjonsflyt og datautveksling<br>Autentisering<br>Tilgangskontroll | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/47-Feide-produkt-canvas-v1-codex.md) |
| 48 | `SIKT-002` | Felles studentsystem (FS) | Studentdata | Bruke data fra andre<br>Dele data med andre<br>Datastyring<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/48-Felles-studentsystem-produkt-canvas-v1-codex.md) |
| 49 | `SIKT-003` | Opptaksløsninger | Opptaksløsning | Bruke data fra andre<br>Organisatorisk samhandling<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/49-Opptakslosninger-produkt-canvas-v1-codex.md) |
| 50 | `SIKT-004` | Nasjonal vitnemålsdatabase (NVB) | Vitnemål | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/50-Nasjonal-vitnemalsdatabase-produkt-canvas-v1-codex.md) |
| 51 | `SIKT-005` | Vitnemålsportalen | Deling av vitnemål | Dele data med andre<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/51-Vitnemalsportalen-produkt-canvas-v1-codex.md) |
| 52 | `SIKT-006` | Nasjonalt utdanningsregister | Register over utdanningstilbud og akkreditering | Grunndata<br>Dele data med andre<br>Datastyring | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/52-Nasjonalt-utdanningsregister-produkt-canvas-v1-codex.md) |



## Helsedirektoratet (`HDIR`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 31 | `HDIR-001` | Helsedata.no | Datatilgang | Oversikt over datasett<br>Datastyring<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/31-Helsedata-no-produkt-canvas-v1-codex.md) |
| 64 | `HDIR-002` | HPR | Register over helsepersonell | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/64-HPR-produkt-canvas-v1-codex.md) |



## Folkehelseinstituttet (`FHI`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 128 | `FHI-001` | SYSVAK | Vaksinasjonsregister | Grunndata<br>Dele data med andre<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/128-SYSVAK-produkt-canvas-v1-codex.md) |
| 129 | `FHI-002` | MSIS | Meldingssystem for smittsomme sykdommer | Grunndata<br>Dele data med andre<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/129-MSIS-produkt-canvas-v1-codex.md) |
| 130 | `FHI-003` | Dødsårsaksregisteret | Dødsårsaksregister | Grunndata<br>Dele data med andre<br>Datastyring | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/130-Dodsarsaksregisteret-produkt-canvas-v1-codex.md) |
| 131 | `FHI-004` | Reseptregisteret (NorPD) | Legemiddelregister | Grunndata<br>Dele data med andre<br>Datastyring | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/131-Reseptregisteret-NorPD-produkt-canvas-v1-codex.md) |



## Norsk helsenett (`NHN`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 32 | `NHN-001` | Helsenorge | Innbyggerportal | Sammenhengende tjenester<br>Tjenestekjeder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/32-Helsenorge-produkt-canvas-v1-codex.md) |
| 33 | `NHN-002` | HelseID | Tillits- og autentiseringskomponent for helse | Bruke data fra andre<br>Sikring av informasjonsflyt og datautveksling<br>Autentisering<br>Tilgangskontroll | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/33-HelseID-produkt-canvas-v1-codex.md) |
| 34 | `NHN-003` | Kjernejournal | Pasientdata | Bruke data fra andre<br>Dele data med andre<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/34-Kjernejournal-produkt-canvas-v1-codex.md) |
| 35 | `NHN-004` | e-resept | Reseptsystem | Bruke data fra andre<br>Meldingsformidling<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/35-e-resept-produkt-canvas-v1-codex.md) |
| 79 | `NHN-005` | Videokonsultasjon (VIO) | Digital konsultasjonstjeneste | Sammenhengende tjenester<br>Dele data med andre | - |



## HELFO (`HELFO`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 65 | `HELFO-001` | KUHR | Refusjonsdata | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/65-KUHR-produkt-canvas-v1-codex.md) |



## NAV (`NAV`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 36 | `NAV-001` | Aa-registeret | Arbeidsforhold | Grunndata<br>Bruke data fra andre<br>Dele data med andre<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/36-Aa-registeret-produkt-canvas-v1-codex.md) |
| 66 | `NAV-002` | NAIS | Plattform for applikasjoner | Gjenbrukbare tjenester<br>Utviklings- og kjøretidsmiljø | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/66-NAIS-produkt-canvas-v1-codex.md) |



## Skatteetaten (`SKATT`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 37 | `SKATT-001` | Folkeregisteret | Persondata | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/37-Folkeregisteret-produkt-canvas-v1-codex.md) |
| 38 | `SKATT-002` | Skatteetatens delingstjenester | API-basert deling | Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/38-Skatteetatens-delingstjenester-produkt-canvas-v1-codex.md) |



## Kartverket (`KART`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 39 | `KART-001` | Matrikkelen | Eiendoms- og adresseregister | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/39-Matrikkelen-produkt-canvas-v1-codex.md) |
| 40 | `KART-002` | Geonorge | Geodataportal / metadata- og delingsplattform | Oversikt over datasett<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/40-Geonorge-produkt-canvas-v1-codex.md) |



## Statens vegvesen (`SVV`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 60 | `SVV-001` | Motorvognregisteret | Kjøretøydata | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/60-Motorvognregisteret-produkt-canvas-v1-codex.md) |
| 61 | `SVV-002` | NVDB | Vegdata | Grunndata<br>Oversikt over datasett | - |



## SSB (`SSB`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 63 | `SSB-001` | microdata.no | Analyseplattform | Sammenstilling av data<br>Bruke data fra andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/63-microdata-no-produkt-canvas-v1-codex.md) |



## Flere virksomheter (`FLERE`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 59 | `FLERE-001` | A-ordningen | Felles rapportering | Grunndata<br>Dele data med andre<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/59-A-ordningen-produkt-canvas-v1-codex.md) |
| 62 | `FLERE-002` | DSOP-tjenester | Offentlig–privat datadeling | Dele data med andre<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/62-DSOP-tjenester-produkt-canvas-v1-codex.md) |



## Novari (`NOVARI`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 70 | `NOVARI-001` | FINT Felleskomponent | Integrasjons- og datadelingstjeneste | Dele data med andre<br>Bruke data fra andre<br>Informasjonsarkitektur<br>Integrerbare tjenester<br>Gjenbrukbare tjenester<br>Sikring av informasjonsflyt og datautveksling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/70-FINT-Felleskomponent-v1-codex.md) |
| 71 | `NOVARI-002` | FINT Arkiv | Arkiv- og integrasjonstjeneste | Dele data med andre<br>Bruke data fra andre<br>Informasjonsarkitektur<br>Integrerbare tjenester<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/71-FINT-Arkiv-v1-codex.md) |
| 72 | `NOVARI-003` | FINT Informasjonsmodell | Informasjonsmodell | Informasjonsarkitektur<br>Oversikt over informasjonsmodeller<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/normerende-ressurser/72-FINT-Informasjonsmodell-v1-codex.md) |
| 73 | `NOVARI-004` | VIGO | Felles løsning for inntak og administrasjon i videregående opplæring | Organisatorisk samhandling<br>Sammenhengende tjenester<br>Dele data med andre<br>Datastyring<br>Oversikt over tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/73-VIGO-v1-codex.md) |
| 80 | `NOVARI-005` | VIGO-portalen | Brukerflate for VIGO-tjenester | Sammenhengende tjenester<br>Tjenestekjeder | - |
| 81 | `NOVARI-006` | VIGO Sentralbase | Felles datagrunnlag for VIGO | Grunndata<br>Datastyring<br>Dele data med andre | - |
| 82 | `NOVARI-007` | VIGO Kodeverk og kodeverksbase | Kodeverk | Informasjonsarkitektur<br>Forvaltningsstandarder | - |
| 83 | `NOVARI-008` | Arkivintegrasjoner | Integrasjonstjeneste for arkivflyt | Dele data med andre<br>Bruke data fra andre<br>Organisatorisk samhandling | - |
| 84 | `NOVARI-009` | vigo.no | Soknads- og informasjonstjeneste for videregaende opplaering | Sammenhengende tjenester<br>Tjenestekjeder | - |



## OpenPeppol (`OPP`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 11 | `OPP-001` | Peppol eDelivery | Internasjonalt samhandlingsrammeverk | Meldingsformidling<br>Sikring av informasjonsflyt og datautveksling<br>Forvaltningsstandarder<br>Identifisering | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/11-Peppol-eDelivery-produkt-canvas-v3-codex.md) |



## EU / Europakommisjonen (`EU`)

| Løpenr | Ressurs-ID | Navn | Type | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|
| 41 | `EU-001` | European Digital Identity Wallet | Digital identitetslommebok | Autentisering<br>Signering | - |
| 42 | `EU-002` | eID Building Block | E-identifikasjonskomponent | Autentisering<br>Bruke data fra andre | - |
| 43 | `EU-003` | eDelivery Building Block | Byggestein / referanseramme for eDelivery | Meldingsformidling<br>Sikring av informasjonsflyt og datautveksling | - |
| 44 | `EU-004` | eSignature Building Block | Signaturkomponent | Signering<br>Sikring av informasjonsflyt og datautveksling | - |
| 45 | `EU-005` | Once-Only Technical System (OOTS) | Grensekryssende datadelingsinfrastruktur | Dele data med andre<br>Organisatorisk samhandling | - |
| 53 | `EU-006` | EU Open Source Solutions Catalogue | Åpen kildekode-katalog for offentlig sektor | Gjenbrukbare tjenester<br>Integrerbare tjenester | - |
| 54 | `EU-007` | Interoperable Europe Solutions | Løsningskatalog for interoperabilitet | Samarbeidsarenaer og nettverk<br>Forvaltningsstandarder | - |
| 55 | `EU-008` | Core Vocabularies | Semantisk interoperabilitetsressurs | Informasjonsarkitektur<br>Forvaltningsstandarder | - |
| 90 | `EU-009` | Interoperable Europe Act | Regulering og rammeverk | Samarbeidsarenaer og nettverk<br>Forvaltningsstandarder | - |
| 91 | `EU-010` | Assessment Toolbox | Vurderingsverktøy | Forvaltningsstandarder<br>Arkitekturstyring | - |
| 92 | `EU-011` | Assessment reports repository | Erfaringsbibliotek | Samarbeidsarenaer og nettverk<br>Samordning | - |



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

