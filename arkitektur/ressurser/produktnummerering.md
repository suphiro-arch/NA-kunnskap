# Produktregister og ressurs-ID-er



Kilde: arbeidsregister bygget fra eksisterende produktliste, siste produktversjoner i repoet, `sources/links.md`, kuraterte eier- og navnevurderinger, oppslag i Enhetsregisteret og ekstra offisielle kilder verifisert i denne arbeidsøkten.



## Prinsipp

- `Løpenr` beholdes som stabil intern sortering og brukes fortsatt i filnavn, for eksempel `01-ID-porten-produkt-canvas-v3-codex.md`.

- `Ressurs-ID` er den nye, kanoniske identifikatoren som skal brukes i feltet `Ressurs ID` i produktbeskrivelser.

- `Ressurs-ID` bygges som `<EIERKODE>-<løpenummer hos eier>`, for eksempel `DIGDIR-001` eller `KS-003`.

- `Ressurskategori` skiller mellom hovedtyper ressurser, som felleskomponent, fellesløsning, register, portal, plattform, internasjonal fellesressurs og referanseressurs.

- Nye produkter skal få neste ledige nummer innenfor sin eierkode. Eksisterende `Ressurs-ID` skal ikke endres uten bevisst omnummerering.

- Rader uten egen produktbeskrivelse ennå er arbeidsutkast. Der står `Siste versjon` som `Ikke opprettet ennå` og dokumentfeltet er tomt.

- Eier, ressurskategori, merknad og kapabilitetstreff for nye ressurser er første arbeidsutkast og må kvalitetssikres når produktbeskrivelsene opprettes.

## Eierkoder

| Eierkode | Visningsnavn | Registrert navn (Enhetsregisteret) | Bruk |
|---|---|---|---|
| `DIGDIR` | Digdir | Digitaliseringsdirektoratet | Digitale fellesløsninger og Altinn-relaterte løsninger som forvaltes i Digdir-regi |
| `BRREG` | Brønnøysundregistrene | Registerenheten i Brønnøysund | Register- og samhandlingsløsninger som forvaltes av Brønnøysundregistrene |
| `KS` | KS Digital | KS-Digitale Fellestjenester AS | Kommunale fellesløsninger og KS-plattformtjenester |
| `SIKT` | Sikt | SIKT - Kunnskapssektorens tjenesteleverandør | Nasjonale fellesløsninger for utdanning og forskning |
| `HDIR` | Helsedirektoratet | Helsedirektoratet | Helsedirektoratets nasjonale ressurser og registre |
| `FHI` | Folkehelseinstituttet | Folkehelseinstituttet | Nasjonale helseregistre og smittevernrelaterte dataressurser |
| `NHN` | Norsk helsenett | Norsk helsenett SF | Nasjonale e-helseløsninger og helseinfrastruktur |
| `HELFO` | Helfo | Helfo | Refusjons- og oppgjørstjenester i helsesektoren |
| `NAV` | NAV | Arbeids- og velferdsetaten | NAVs fellesløsninger, registre og plattformer |
| `SKATT` | Skatteetaten | Skatteetaten | Fellesløsninger og datatjenester forvaltet av Skatteetaten |
| `KART` | Kartverket | Statens kartverk | Nasjonale geodata- og kartressurser |
| `SVV` | Statens vegvesen | Statens vegvesen | Nasjonale veg- og kjøretøyregistre og tilhørende dataplattformer |
| `SSB` | Statistisk sentralbyrå | Statistisk sentralbyrå | Felles datatjenester og analyseplattformer for statistikk og forskning |
| `FLERE` | Flere virksomheter | Ikke relevant | Samforvaltede eller tverrsektorielle løsninger med flere eiere |
| `NOVARI` | Novari IKS | Novari IKS | Fylkeskommunale fellesressurser og løsninger forvaltet av Novari |
| `OPP` | OpenPeppol | Ikke relevant | Internasjonale fellesressurser og styringsrammeverk for Peppol-økosystemet |
| `EU` | EU / Europakommisjonen | Ikke relevant | Relevante europeiske felleskomponenter og byggesteiner |
| `DTIL` | Datatilsynet | Datatilsynet | Personvernfaglige ressurser, veiledning og virkemidler forvaltet av Datatilsynet |

### Slik lages en ny eierkode

Hvis en ressurs har en eier som ikke står i tabellen over, skal ny eierkode opprettes i samme endringssett som ressursen. Følg denne rekkefølgen:

1. Bruk virksomhetens etablerte forkortelse når den finnes og er entydig, slik `NAV`, `KS`, `SSB`, `SVV`, `SIKT` og `FHI` er brukt.
2. Uten etablert forkortelse: lag en ASCII-kode på tre til seks store bokstaver av kjerneordet i navnet, slik `SKATT` for Skatteetaten, `KART` for Kartverket og `HDIR` for Helsedirektoratet.
3. Kontroller at koden er unik og ikke kan forveksles med en eksisterende kode.
4. Bruk `FLERE` i stedet for ny kode når forvaltningsansvaret faktisk er delt mellom flere virksomheter.
5. Legg inn raden med eierkode, visningsnavn, registrert navn fra Enhetsregisteret der virksomheten er registrert, og en kort setning om bruksområde.

En eierkode skal ikke endres etter at den er tatt i bruk, fordi den inngår i ressurs-ID-er som er brukt i register, kapabilitetsmapping og webgrunnlag.



## Digdir (`DIGDIR`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 1 | `DIGDIR-001` | ID-porten | Gjenbrukbare løsninger | Innlogging og identitet | Sikring av informasjonsflyt og datautveksling<br>Autentisering<br>Identifisering<br>Representasjon<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/01-ID-porten-produkt-canvas-v3-codex.md) |
| 2 | `DIGDIR-002` | Maskinporten | Gjenbrukbare løsninger | Maskinell tilgang | Bruke data fra andre<br>Dele data med andre<br>Sikring av informasjonsflyt og datautveksling<br>Autentisering<br>Tilgangskontroll | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/02-Maskinporten-produkt-canvas-v4-codex.md) |
| 3 | `DIGDIR-003` | eSignering | Gjenbrukbare løsninger | Signering | Sikring av informasjonsflyt og datautveksling<br>Autentisering<br>Signering | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/03-eSignering-produkt-canvas-v3-codex.md) |
| 4 | `DIGDIR-004` | Altinn Autorisasjon | Gjenbrukbare løsninger | Autorisasjon og delegering | Representasjon<br>Tilgangskontroll<br>Tilgangsstyring | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/04-Altinn-autorisasjon-produkt-canvas-v4-codex.md) |
| 5 | `DIGDIR-005` | Kontakt- og reservasjonsregisteret | Gjenbrukbare løsninger | Kontaktopplysninger og reservasjon | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/05-Kontakt-og-reservasjonsregisteret-produkt-canvas-v3-codex.md) |
| 6 | `DIGDIR-006` | eInnsyn | Gjenbrukbare løsninger | Innsyn og offentlighet | Organisatorisk samhandling<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/06-eInnsyn-produkt-canvas-v3-codex.md) |
| 7 | `DIGDIR-007` | eFormidling | Gjenbrukbare løsninger | Meldingsflyt | Bruke data fra andre<br>Dele data med andre<br>Meldingsutveksling<br>Sikring av informasjonsflyt og datautveksling<br>Organisatorisk samhandling<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/07-eFormidling-produkt-canvas-v3-codex.md) |
| 8 | `DIGDIR-008` | Altinn Formidling | Gjenbrukbare løsninger | Filformidling | Bruke data fra andre<br>Dele data med andre<br>Meldingsutveksling<br>Sikring av informasjonsflyt og datautveksling<br>Organisatorisk samhandling<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/08-Altinn-formidling-produkt-canvas-v3-codex.md) |
| 9 | `DIGDIR-009` | Digital postkasse | Gjenbrukbare løsninger | Utsending av post | Meldingsutveksling<br>Sikring av informasjonsflyt og datautveksling<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/09-Digital-postkasse-produkt-canvas-v3-codex.md) |
| 10 | `DIGDIR-023` | ELMA | Gjenbrukbare løsninger | Meldingsmottak og adresseregister | Meldingsutveksling<br>Identifisering | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/10-ELMA-produkt-canvas-v3-codex.md) |
| 12 | `DIGDIR-010` | Altinn Events | Gjenbrukbare løsninger | Hendelser og abonnement | Bruke data fra andre<br>Dele data med andre<br>Hendelsesdrevet<br>Sikring av informasjonsflyt og datautveksling<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/12-Altinn-events-produkt-canvas-v3-codex.md) |
| 13 | `DIGDIR-011` | Felles datakatalog | Gjenbrukbare løsninger | Metadata og kataloger | Oversikt over API<br>Oversikt over begreper<br>Oversikt over datasett<br>Oversikt over informasjonsmodeller<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/13-Felles-datakatalog-produkt-canvas-v3-codex.md) |
| 14 | `DIGDIR-012` | Begrepskatalog | Gjenbrukbare løsninger | Begreper | Datastyring<br>Informasjonsarkitektur<br>Oversikt over begreper<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/14-Begrepskatalog-produkt-canvas-v3-codex.md) |
| 15 | `DIGDIR-013` | API-katalog | Gjenbrukbare løsninger | API-katalog | Informasjonsarkitektur<br>Oversikt over API<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/15-API-katalog-produkt-canvas-v3-codex.md) |
| 16 | `DIGDIR-014` | data.norge.no | Gjenbrukbare løsninger | Åpne data | Oversikt over API<br>Oversikt over begreper<br>Oversikt over datasett<br>Oversikt over hendelser<br>Oversikt over informasjonsmodeller<br>Oversikt over tjenester<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/16-data-norge-no-produkt-canvas-v4-codex.md) |
| 17 | `DIGDIR-015` | data.altinn.no | Gjenbrukbare løsninger | Kontrollert datadeling | Sammenstilling av data<br>Bruke data fra andre<br>Dele data med andre<br>Sikring av informasjonsflyt og datautveksling<br>Forvaltningsstandarder<br>Autentisering<br>Samtykke<br>Tilgangskontroll<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/17-data-altinn-no-produkt-canvas-v4-codex.md) |
| 18 | `DIGDIR-016` | Norge.no | Gjenbrukbare løsninger | Innbyggerinformasjon | Oversikt over tjenester<br>Sammenhengende tjenester<br>Tjenestekjeder<br>Tjenestedesign | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/18-Norge-no-produkt-canvas-v3-codex.md) |
| 19 | `DIGDIR-017` | Altinn 3 plattform | Gjenbrukbare løsninger | Tjenesteplattform | Tjenesteforvaltning<br>Gjenbrukbare tjenester<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/19-Altinn-3-plattform-produkt-canvas-v3-codex.md) |
| 20 | `DIGDIR-018` | Altinn Studio | Gjenbrukbare løsninger | Tjenesteutvikling | Gjenbrukbare tjenester<br>Integrerbare tjenester<br>Tjenestedesign<br>Utviklings- og kjøretidsmiljø | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/20-Altinn-Studio-produkt-canvas-v3-codex.md) |
| 21 | `DIGDIR-019` | Altinn Portal | Gjenbrukbare løsninger | Brukerinngang og meldinger | Sammenhengende tjenester<br>Tjenestekjeder<br>Representasjon<br>Sporbarhet og innsyn<br>Tilgangsstyring | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/21-Altinn-Portal-produkt-canvas-v3-codex.md) |
| 22 | `DIGDIR-020` | Dialogporten | Gjenbrukbare løsninger | Dialog og representasjon | Bruke data fra andre<br>Hendelsesdrevet<br>Sammenhengende tjenester<br>Autentisering<br>Tilgangskontroll<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/22-Dialogporten-produkt-canvas-v5-codex.md) |
| 23 | `DIGDIR-021` | Altinn Melding | Gjenbrukbare løsninger | Korrespondanse og innsyn | Hendelsesdrevet<br>Meldingsutveksling<br>Sikring av informasjonsflyt og datautveksling<br>Sporbarhet og innsyn<br>Tilgangskontroll<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/23-Altinn-3-Melding-produkt-canvas-v5-codex.md) |
| 24 | `DIGDIR-022` | Altinn Varsling | Gjenbrukbare løsninger | Varsling | Sammenstilling av data<br>Meldingsutveksling<br>Sikring av informasjonsflyt og datautveksling<br>Proaktive tjenester<br>Tilgangskontroll<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/24-Varslinger-produkt-canvas-v5-codex.md) |
| 56 | `DIGDIR-024` | eIDAS-node (Norge) | Gjenbrukbare løsninger | Grensekryssende eID | Bruke data fra andre<br>Autentisering<br>Identifisering | - |
| 85 | `DIGDIR-025` | Rammeverk for digital samhandling | Standarder og veiledning | Rammeverk | Forvaltningsstandarder<br>Dele data med andre<br>Organisatorisk samhandling<br>Juridisk samhandling | [Åpne](../../arkitektur/ressurser/normerende-ressurser/85-Rammeverk-for-digital-samhandling-v2-codex.md) |
| 86 | `DIGDIR-026` | Referansekatalogen for IT-standarder | Standarder og veiledning | Standardkatalog | Forvaltningsstandarder<br>Informasjonsarkitektur | [Åpne](../../arkitektur/ressurser/normerende-ressurser/86-Referansekatalogen-for-IT-standarder-v1-codex.md) |
| 87 | `DIGDIR-027` | Arkitektur for hendelser | Standarder og veiledning | Referansearkitektur | Hendelsesdrevet<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/normerende-ressurser/87-Arkitektur-for-hendelser-v2-codex.md) |
| 88 | `DIGDIR-028` | Arkitektur- og standardiseringsrådet | Samhandlingsarenaer og organisering | Arkitekturråd | Samarbeidsarenaer og nettverk<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/samarbeidsfora/88-Arkitektur-og-standardiseringsradet-v1-codex.md) |
| 89 | `DIGDIR-029` | Rammeverk for informasjonsforvaltning | Standarder og veiledning | Rammeverk | Datastyring<br>Informasjonsarkitektur<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/normerende-ressurser/89-Rammeverk-for-informasjonsforvaltning-v2-codex.md) |
| 98 | `DIGDIR-030` | Overordnede arkitekturprinsipper for offentlig sektor | Standarder og veiledning | Prinsipper | Forvaltningsstandarder<br>Arkitekturstyring | [Åpne](../../arkitektur/ressurser/normerende-ressurser/98-Overordnede-arkitekturprinsipper-for-offentlig-sektor-v2-codex.md) |
| 99 | `DIGDIR-031` | Sjekkliste for sammenhengende tjenester | Standarder og veiledning | Veileder | Sammenhengende tjenester<br>Tjenestedesign<br>Veiledning | [Åpne](../../arkitektur/ressurser/normerende-ressurser/99-Sjekkliste-for-sammenhengende-tjenester-v1-codex.md) |
| 100 | `DIGDIR-032` | Kart for tjenestekjeder | Standarder og veiledning | Metodeverktøy | Tjenestekjeder<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/normerende-ressurser/100-Kart-for-tjenestekjeder-v1-codex.md) |
| 101 | `DIGDIR-033` | Referansearkitektur forsendelse (eMelding) | Standarder og veiledning | Referansearkitektur | Meldingsutveksling<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/normerende-ressurser/101-Referansearkitektur-forsendelse-eMelding-v2-codex.md) |
| 102 | `DIGDIR-034` | Referansearkitektur forespørsel-svar (eOppslag) | Standarder og veiledning | Referansearkitektur | Bruke data fra andre<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/normerende-ressurser/102-Referansearkitektur-foresporsel-svar-eOppslag-v2-codex.md) |
| 103 | `DIGDIR-035` | Nasjonalt veikart | Standarder og veiledning | Veikart | Samordning<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/normerende-ressurser/103-Nasjonalt-veikart-v2-codex.md) |
| 104 | `DIGDIR-036` | Orden i eget hus | Standarder og veiledning | Metodikk | Datastyring<br>Oversikt over datasett | [Åpne](../../arkitektur/ressurser/normerende-ressurser/104-Orden-i-eget-hus-v1-codex.md) |
| 105 | `DIGDIR-037` | Rammeverk for Nasjonale grunndata | Standarder og veiledning | Rammeverk | Grunndata<br>Samordning | [Åpne](../../arkitektur/ressurser/normerende-ressurser/105-Rammeverk-for-Nasjonale-grunndata-v2-codex.md) |
| 106 | `DIGDIR-038` | Nasjonal verktøykasse for deling av data | Standarder og veiledning | Veileder | Dele data med andre<br>Datastyring<br>Veiledning | [Åpne](../../arkitektur/ressurser/normerende-ressurser/106-Nasjonal-verktoykasse-for-deling-av-data-v1-codex.md) |
| 107 | `DIGDIR-039` | Kunnskapsgrunnlag og KPI-er datadeling | Standarder og veiledning | Kunnskapsgrunnlag | Samordning<br>Datastyring | [Åpne](../../arkitektur/ressurser/normerende-ressurser/107-Kunnskapsgrunnlag-og-KPI-er-datadeling-v1-codex.md) |
| 108 | `DIGDIR-040` | Kunnskapsgrunnlag - dataspaces | Standarder og veiledning | Kunnskapsgrunnlag | Forvaltningsstandarder<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/normerende-ressurser/108-Kunnskapsgrunnlag-dataspaces-v1-codex.md) |
| 109 | `DIGDIR-041` | Kapabilitetskart (planlagt) | Standarder og veiledning | Kapabilitetsmodell | Arkitekturstyring<br>Datastyring | [Åpne](../../arkitektur/ressurser/normerende-ressurser/109-Kapabilitetskart-planlagt-v2-codex.md) |
| 110 | `DIGDIR-042` | Skate | Samhandlingsarenaer og organisering | Tverrsektoriell samordningsarena | Samarbeidsarenaer og nettverk<br>Samordning | [Åpne](../../arkitektur/ressurser/samarbeidsfora/110-Skate-v1-codex.md) |
| 111 | `DIGDIR-043` | Digitaliseringsradet | Samhandlingsarenaer og organisering | Radgivende arena | Samarbeidsarenaer og nettverk<br>Arkitekturstyring | [Åpne](../../arkitektur/ressurser/samarbeidsfora/111-Digitaliseringsradet-v1-codex.md) |
| 112 | `DIGDIR-044` | Digitaliseringsrundskrivet | Økonomiske og juridiske rammer og virkemidler | Rundskriv | Samordning<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/rammer-og-virkemidler/112-Digitaliseringsrundskrivet-v2-copilot.md) |
| 113 | `DIGDIR-045` | Prosjektveiviseren | Standarder og veiledning | Prosjektmetodikk | Samordning<br>Tjenestedesign<br>Veiledning | [Åpne](../../arkitektur/ressurser/normerende-ressurser/113-Prosjektveiviseren-v1-codex.md) |
| 114 | `DIGDIR-046` | Klart språk | Standarder og veiledning | Veileder | Sammenhengende tjenester<br>Tjenestedesign<br>Veiledning | [Åpne](../../arkitektur/ressurser/normerende-ressurser/114-Klart-sprak-v1-codex.md) |
| 115 | `DIGDIR-047` | Digitaliseringsvennlig regelverk | Standarder og veiledning | Veileder | Forvaltningsstandarder<br>Arkitekturstyring<br>Juridisk samhandling<br>Veiledning | [Åpne](../../arkitektur/ressurser/normerende-ressurser/115-Digitaliseringsvennlig-regelverk-v1-codex.md) |
| 116 | `DIGDIR-048` | Rammeverk for innovasjon i offentlig sektor | Standarder og veiledning | Rammeverk | Samordning<br>Tjenestedesign | [Åpne](../../arkitektur/ressurser/normerende-ressurser/116-Rammeverk-for-innovasjon-i-offentlig-sektor-v2-codex.md) |
| 117 | `DIGDIR-049` | Kompetansemodell for digital transformasjon | Standarder og veiledning | Kompetansemodell | Samordning<br>Tjenestedesign | [Åpne](../../arkitektur/ressurser/normerende-ressurser/117-Kompetansemodell-for-digital-transformasjon-v1-codex.md) |
| 118 | `DIGDIR-050` | Felles designsystem | Gjenbrukbare løsninger | Designsystem | Sammenhengende tjenester<br>Gjenbrukbare tjenester<br>Tjenestedesign | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/118-Felles-designsystem-v2-codex.md) |
| 119 | `DIGDIR-051` | Ansattporten | Gjenbrukbare løsninger | Autentiseringstjeneste for ansatte | Sikring av informasjonsflyt og datautveksling<br>Autentisering<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/119-Ansattporten-v2-codex.md) |
| 120 | `DIGDIR-052` | Styringsråd forDigitaliseringsdirektoratets fellesløsninger | Samhandlingsarenaer og organisering | Styringsråd | Samarbeidsarenaer og nettverk<br>Samordning | [Åpne](../../arkitektur/ressurser/samarbeidsfora/120-Styringsradet-for-felleslosningene-v3-copilot.md) |
| 121 | `DIGDIR-053` | Faglig arena for informasjonsforvaltning og deling av data | Samhandlingsarenaer og organisering | Faglig forum | Datastyring<br>Samarbeidsarenaer og nettverk | [Åpne](../../arkitektur/ressurser/samarbeidsfora/121-Faglig-arena-for-informasjonsforvaltning-og-deling-av-data-v1-codex.md) |
| 122 | `DIGDIR-054` | NIFS | Samhandlingsarenaer og organisering | Nettverk for informasjonssikkerhet | Sikring av informasjonsflyt og datautveksling<br>Samarbeidsarenaer og nettverk | [Åpne](../../arkitektur/ressurser/samarbeidsfora/122-NIFS-v1-codex.md) |
| 123 | `DIGDIR-055` | DSOP-samarbeidet | Samhandlingsarenaer og organisering | Offentlig-privat samhandlingsarena | Dele data med andre<br>Samarbeidsarenaer og nettverk<br>Samordning | [Åpne](../../arkitektur/ressurser/samarbeidsfora/123-DSOP-samarbeidet-v1-codex.md) |
| 124 | `DIGDIR-056` | Felles sikkerhet i forvaltningen | Samhandlingsarenaer og organisering | Tverrsektorielt sikkerhetssamarbeid | Sikring av informasjonsflyt og datautveksling<br>Samarbeidsarenaer og nettverk<br>Samordning | [Åpne](../../arkitektur/ressurser/samarbeidsfora/124-Felles-sikkerhet-i-forvaltningen-v1-codex.md) |
| 125 | `DIGDIR-057` | KI Norge | Samhandlingsarenaer og organisering | Nasjonal arena for kunstig intelligens | Samarbeidsarenaer og nettverk<br>Samordning | [Åpne](../../arkitektur/ressurser/samarbeidsfora/125-KI-Norge-v1-codex.md) |
| 126 | `DIGDIR-058` | Nasjonal sandkasse for digital lommebok | Gjenbrukbare løsninger | Sandkasse og testmiljø for digital lommebok | Autentisering<br>Signering<br>Utviklings- og kjøretidsmiljø<br>Integrerbare tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/126-Nasjonal-sandkasse-for-digital-lommebok-produkt-canvas-v2-codex.md) |
| 127 | `DIGDIR-059` | Samarbeidsportalen | Gjenbrukbare løsninger | Portal for forvaltning, informasjon og ta-i-bruk av fellesløsninger | Oversikt over tjenester<br>Tjenesteforvaltning<br>Samarbeidsarenaer og nettverk | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/127-Samarbeidsportalen-produkt-canvas-v2-codex.md) |
| 137 | `DIGDIR-060` | Forskrift om IT-standarder i offentlig forvaltning | Økonomiske og juridiske rammer og virkemidler | Forskrift | Forvaltningsstandarder<br>Arkitekturstyring<br>Juridisk samhandling | [Åpne](../../arkitektur/ressurser/rammer-og-virkemidler/137-Forskrift-om-IT-standarder-i-offentlig-forvaltning-v2-copilot.md) |
| 138 | `DIGDIR-061` | Veileder for virksomhetsautentisering | Standarder og veiledning | Veileder | Autentisering<br>Sikring av informasjonsflyt og datautveksling<br>Veiledning | [Åpne](../../arkitektur/ressurser/normerende-ressurser/138-Veileder-for-virksomhetsautentisering-v1-codex.md) |
| 139 | `DIGDIR-062` | Datalandsbyen | Samhandlingsarenaer og organisering | Åpen digital samhandlingsarena | Samarbeidsarenaer og nettverk<br>Dele data med andre<br>Bruke data fra andre<br>Datastyring | [Åpne](../../arkitektur/ressurser/samarbeidsfora/139-Datalandsbyen-v1-codex.md) |
| 140 | `DIGDIR-063` | MinID | Gjenbrukbare løsninger | Personlig eID og autentiseringstjeneste | Sikring av informasjonsflyt og datautveksling<br>Autentisering<br>Identifisering | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/140-MinID-produkt-canvas-v1-codex.md) |
| 142 | `DIGDIR-064` | Medfinansieringsordningen | Økonomiske og juridiske rammer og virkemidler | Finansieringsordning / tilskuddsvirkemiddel | Finansiering<br>Samordning<br>Tjenestedesign | [Åpne](../../arkitektur/ressurser/rammer-og-virkemidler/142-Medfinansieringsordningen-v1-copilot.md) |
| 143 | `DIGDIR-065` | PPP(P)-nettverket | Samhandlingsarenaer og organisering | Fagnettverk for prosjekt-, program-, produkt- og porteføljestyring | Samarbeidsarenaer og nettverk<br>Samordning | [Åpne](../../arkitektur/ressurser/samarbeidsfora/143-PPP-P-nettverket-v1-claude.md) |
| 144 | `DIGDIR-066` | eForvaltningsforskriften | Økonomiske og juridiske rammer og virkemidler | Forskrift | Regelverkstolkning<br>Sikring av informasjonsflyt og datautveksling | [Åpne](../../arkitektur/ressurser/rammer-og-virkemidler/144-eForvaltningsforskriften-v2-copilot.md) |
| 145 | `DIGDIR-067` | Tilskudd til etablering av kommunale opplæringstilbud i digital kompetanse til innbyggerne | Økonomiske og juridiske rammer og virkemidler | Tilskuddsordning | Finansiering | [Åpne](../../arkitektur/ressurser/rammer-og-virkemidler/145-Tilskudd-til-kommunale-opplaeringstilbud-i-digital-kompetanse-v1-claude.md) |

## Brønnøysundregistrene (`BRREG`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 46 | `BRREG-003` | Enhetsregisteret | Gjenbrukbare løsninger | Virksomhetsregister | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/46-Enhetsregisteret-produkt-canvas-v1-codex.md) |
| 133 | `BRREG-004` | Register over reelle rettighetshavere | Gjenbrukbare løsninger | Register over faktisk eierskap og kontroll | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/133-Register-over-reelle-rettighetshavere-produkt-canvas-v1-codex.md) |



## KS Digital (`KS`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 25 | `KS-001` | Fiks-plattformen | Gjenbrukbare løsninger | Integrasjonsplattform | Organisatorisk samhandling<br>Integrerbare tjenester<br>Utviklings- og kjøretidsmiljø | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/25-FIKS-plattformen-produkt-canvas-v1-codex.md) |
| 26 | `KS-002` | Fiks melding | Gjenbrukbare løsninger | Meldingsutveksling | Meldingsutveksling<br>Sikring av informasjonsflyt og datautveksling<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/26-FIKS-Melding-produkt-canvas-v2-codex.md) |
| 27 | `KS-003` | Fiks SvarUt | Gjenbrukbare løsninger | Utsendingstjeneste for digital og fysisk post | Meldingsutveksling<br>Organisatorisk samhandling<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/27-FIKS-SvarUt-produkt-canvas-v3-codex.md) |
| 28 | `KS-004` | Fiks register | Gjenbrukbare løsninger | Registerfamilie og tilgangslag | Grunndata<br>Bruke data fra andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v3-codex.md) |
| 30 | `KS-006` | Fiks digiorden | Gjenbrukbare løsninger | Styrings- og oversiktsløsning | Datastyring<br>Oversikt over datasett<br>Oversikt over tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/30-FIKS-Digiorden-produkt-canvas-v1-codex.md) |
| 57 | `KS-007` | SvarInn | Gjenbrukbare løsninger | Inngående post | Meldingsutveksling<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/57-SvarInn-produkt-canvas-v1-codex.md) |
| 67 | `KS-008` | Fiks folkeregister | Gjenbrukbare løsninger | Tilgang til Folkeregisteret via Fiks | Grunndata<br>Bruke data fra andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/67-FIKS-Folkeregister-produkt-canvas-v2-codex.md) |
| 68 | `KS-009` | Fiks skatte- og inntektsopplysninger | Gjenbrukbare løsninger | Tilgang til skatte- og inntektsopplysninger via Fiks | Grunndata<br>Bruke data fra andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v2-codex.md) |
| 69 | `KS-010` | Fiks kjøretøyregister | Gjenbrukbare løsninger | Tilgang til kjøretøyopplysninger via Fiks | Grunndata<br>Bruke data fra andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/69-FIKS-Kjoretoyregister-produkt-canvas-v1-codex.md) |
| 74 | `KS-011` | Felles mal for innforing av digitale fellestjenester | Standarder og veiledning | Innforingsveileder | Organisatorisk samhandling<br>Forvaltningsstandarder | - |
| 93 | `KS-012` | Fiks Digisos | Gjenbrukbare løsninger | Tjeneste for digital sosialhjelp | Organisatorisk samhandling<br>Sammenhengende tjenester<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/93-Fiks-Digisos-produkt-canvas-v1-codex.md) |
| 94 | `KS-013` | Fiks Protokoll | Gjenbrukbare løsninger | Saks- og motestotte for politiske organer | Organisatorisk samhandling<br>Datastyring | - |
| 95 | `KS-014` | Fiks Vaksine | Gjenbrukbare løsninger | Kommunal vaksineforvaltning | Sammenhengende tjenester<br>Dele data med andre | - |
| 96 | `KS-015` | KS Bekymringsmelding | Gjenbrukbare løsninger | Digital meldingstjeneste for bekymringsmeldinger | Meldingsutveksling<br>Organisatorisk samhandling<br>Sammenhengende tjenester | [96-KS-Bekymringsmelding-produkt-canvas-v1-codex.md](operative-losninger-og-tjenester/96-KS-Bekymringsmelding-produkt-canvas-v1-codex.md) |
| 97 | `KS-016` | MinKommune | Gjenbrukbare løsninger | Innbyggerportal for kommunale tjenester | Sammenhengende tjenester<br>Tjenestekjeder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/97-MinKommune-produkt-canvas-v1-codex.md) |



## Sikt (`SIKT`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 47 | `SIKT-001` | Feide | Gjenbrukbare løsninger | Autentisering | Dele data med andre<br>Sikring av informasjonsflyt og datautveksling<br>Autentisering<br>Tilgangskontroll | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/47-Feide-produkt-canvas-v1-codex.md) |
| 48 | `SIKT-002` | Felles studentsystem (FS) | Gjenbrukbare løsninger | Studentdata | Bruke data fra andre<br>Dele data med andre<br>Datastyring<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/48-Felles-studentsystem-produkt-canvas-v1-codex.md) |
| 49 | `SIKT-003` | Opptaksløsninger | Gjenbrukbare løsninger | Opptaksløsning | Bruke data fra andre<br>Organisatorisk samhandling<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/49-Opptakslosninger-produkt-canvas-v2-codex.md) |
| 50 | `SIKT-004` | Nasjonal vitnemålsdatabase (NVB) | Gjenbrukbare løsninger | Vitnemål | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/50-Nasjonal-vitnemalsdatabase-produkt-canvas-v1-codex.md) |
| 51 | `SIKT-005` | Vitnemålsportalen | Gjenbrukbare løsninger | Deling av vitnemål | Dele data med andre<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/51-Vitnemalsportalen-produkt-canvas-v1-codex.md) |
| 52 | `SIKT-006` | Nasjonalt utdanningsregister | Gjenbrukbare løsninger | Register over utdanningstilbud og akkreditering | Grunndata<br>Dele data med andre<br>Datastyring | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/52-Nasjonalt-utdanningsregister-produkt-canvas-v2-codex.md) |



## Helsedirektoratet (`HDIR`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 31 | `HDIR-001` | Helsedata.no | Gjenbrukbare løsninger | Datatilgang | Oversikt over datasett<br>Datastyring<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/31-Helsedata-no-produkt-canvas-v2-codex.md) |
| 64 | `HDIR-002` | HPR | Gjenbrukbare løsninger | Register over helsepersonell | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/64-HPR-produkt-canvas-v2-codex.md) |



## Folkehelseinstituttet (`FHI`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 128 | `FHI-001` | SYSVAK | Gjenbrukbare løsninger | Vaksinasjonsregister | Grunndata<br>Dele data med andre<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/128-SYSVAK-produkt-canvas-v2-codex.md) |
| 129 | `FHI-002` | MSIS | Gjenbrukbare løsninger | Meldingssystem for smittsomme sykdommer | Grunndata<br>Dele data med andre<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/129-MSIS-produkt-canvas-v2-codex.md) |
| 130 | `FHI-003` | Dødsårsaksregisteret | Gjenbrukbare løsninger | Dødsårsaksregister | Grunndata<br>Dele data med andre<br>Datastyring | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/130-Dodsarsaksregisteret-produkt-canvas-v2-codex.md) |
| 131 | `FHI-004` | Reseptregisteret (NorPD) | Gjenbrukbare løsninger | Historisk legemiddelregister (2004-2021) | Grunndata<br>Dele data med andre<br>Datastyring | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/131-Reseptregisteret-NorPD-produkt-canvas-v2-codex.md) |
| 135 | `FHI-005` | Norsk pasientregister (NPR) | Gjenbrukbare løsninger | Nasjonalt helseregister for spesialisthelsetjenesten | Grunndata<br>Dele data med andre<br>Datastyring | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/135-Norsk-pasientregister-produkt-canvas-v2-codex.md) |
| 136 | `FHI-006` | Kommunalt pasient- og brukerregister (KPR) | Gjenbrukbare løsninger | Nasjonalt helseregister for kommunale helse- og omsorgstjenester | Grunndata<br>Dele data med andre<br>Datastyring | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/136-Kommunalt-pasient-og-brukerregister-produkt-canvas-v2-codex.md) |



## Norsk helsenett (`NHN`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 32 | `NHN-001` | Helsenorge | Gjenbrukbare løsninger | Innbyggerportal | Sammenhengende tjenester<br>Tjenestekjeder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/32-Helsenorge-produkt-canvas-v1-codex.md) |
| 33 | `NHN-002` | HelseID | Gjenbrukbare løsninger | Tillits- og autentiseringskomponent for helse | Bruke data fra andre<br>Sikring av informasjonsflyt og datautveksling<br>Autentisering<br>Tilgangskontroll | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/33-HelseID-produkt-canvas-v1-codex.md) |
| 34 | `NHN-003` | Kjernejournal | Gjenbrukbare løsninger | Pasientdata | Bruke data fra andre<br>Dele data med andre<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/34-Kjernejournal-produkt-canvas-v2-codex.md) |
| 35 | `NHN-004` | e-resept | Gjenbrukbare løsninger | Reseptsystem | Bruke data fra andre<br>Meldingsutveksling<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/35-e-resept-produkt-canvas-v1-codex.md) |
| 79 | `NHN-005` | Videokonsultasjon (VIO) | Gjenbrukbare løsninger | Digital konsultasjonstjeneste | Sammenhengende tjenester<br>Dele data med andre | - |



## HELFO (`HELFO`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 65 | `HELFO-001` | KUHR | Gjenbrukbare løsninger | Refusjonsdata | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/65-KUHR-produkt-canvas-v1-codex.md) |



## NAV (`NAV`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 36 | `NAV-001` | Aa-registeret | Gjenbrukbare løsninger | Arbeidsforholdsregister og delingstjeneste | Grunndata<br>Bruke data fra andre<br>Dele data med andre<br>Sammenhengende tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/36-Aa-registeret-produkt-canvas-v2-codex.md) |
| 66 | `NAV-002` | NAIS | Gjenbrukbare løsninger | Plattform for applikasjoner | Gjenbrukbare tjenester<br>Utviklings- og kjøretidsmiljø | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/66-NAIS-produkt-canvas-v2-codex.md) |



## Skatteetaten (`SKATT`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 37 | `SKATT-001` | Folkeregisteret | Gjenbrukbare løsninger | Persondata | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/37-Folkeregisteret-produkt-canvas-v1-codex.md) |
| 38 | `SKATT-002` | Skatteetatens delingstjenester | Gjenbrukbare løsninger | API-basert deling | Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/38-Skatteetatens-delingstjenester-produkt-canvas-v1-codex.md) |



## Kartverket (`KART`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 39 | `KART-001` | Matrikkelen | Gjenbrukbare løsninger | Eiendoms- og adresseregister | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/39-Matrikkelen-produkt-canvas-v1-codex.md) |
| 40 | `KART-002` | Geonorge | Gjenbrukbare løsninger | Geodataportal / metadata- og delingsplattform | Oversikt over datasett<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/40-Geonorge-produkt-canvas-v1-codex.md) |
| 132 | `KART-003` | Grunnboken | Gjenbrukbare løsninger | Rettighetsregister for fast eiendom | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/132-Grunnboken-produkt-canvas-v1-codex.md) |
| 134 | `KART-004` | Sentralt stedsnavnregister | Gjenbrukbare løsninger | Register for offisielle stedsnavn | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/134-Sentralt-stedsnavnregister-produkt-canvas-v1-codex.md) |



## Statens vegvesen (`SVV`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 60 | `SVV-001` | Motorvognregisteret | Gjenbrukbare løsninger | Kjøretøydata | Grunndata<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/60-Motorvognregisteret-produkt-canvas-v1-codex.md) |
| 61 | `SVV-002` | NVDB | Gjenbrukbare løsninger | Vegdata | Grunndata<br>Oversikt over datasett<br>Dele data med andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/61-NVDB-produkt-canvas-v1-codex.md) |



## SSB (`SSB`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 63 | `SSB-001` | microdata.no | Gjenbrukbare løsninger | Analyseplattform | Sammenstilling av data<br>Bruke data fra andre | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/63-microdata-no-produkt-canvas-v1-codex.md) |



## Flere virksomheter (`FLERE`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 59 | `FLERE-001` | A-ordningen | Gjenbrukbare løsninger | Felles rapportering | Grunndata<br>Dele data med andre<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/59-A-ordningen-produkt-canvas-v1-codex.md) |
| 62 | `FLERE-002` | DSOP-tjenester | Gjenbrukbare løsninger | Offentlig–privat datadeling | Dele data med andre<br>Organisatorisk samhandling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/62-DSOP-tjenester-produkt-canvas-v2-codex.md) |
| 141 | `FLERE-003` | Stimulab | Økonomiske og juridiske rammer og virkemidler | Stimuleringsordning / tilskudds- og utviklingsvirkemiddel | Innovasjon<br>Samordning<br>Tjenestedesign | [Åpne](../../arkitektur/ressurser/rammer-og-virkemidler/141-Stimulab-v1-copilot.md) |
| 146 | `FLERE-004` | Nasjonal indeks for digital inkludering | Standarder og veiledning | Måleverktøy og kunnskapsgrunnlag | Dataanalyse<br>Samordning | [Åpne](../../arkitektur/ressurser/normerende-ressurser/146-Nasjonal-indeks-for-digital-inkludering-v1-claude.md) |



## Novari (`NOVARI`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 70 | `NOVARI-001` | FINT Felleskomponent | Gjenbrukbare løsninger | Integrasjons- og datadelingstjeneste | Dele data med andre<br>Bruke data fra andre<br>Informasjonsarkitektur<br>Integrerbare tjenester<br>Gjenbrukbare tjenester<br>Sikring av informasjonsflyt og datautveksling | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/70-FINT-Felleskomponent-v1-codex.md) |
| 71 | `NOVARI-002` | FINT Arkiv | Gjenbrukbare løsninger | Arkiv- og integrasjonstjeneste | Dele data med andre<br>Bruke data fra andre<br>Informasjonsarkitektur<br>Integrerbare tjenester<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/71-FINT-Arkiv-v1-codex.md) |
| 72 | `NOVARI-003` | FINT Informasjonsmodell | Standarder og veiledning | Informasjonsmodell | Informasjonsarkitektur<br>Oversikt over informasjonsmodeller<br>Forvaltningsstandarder | [Åpne](../../arkitektur/ressurser/normerende-ressurser/72-FINT-Informasjonsmodell-v1-codex.md) |
| 73 | `NOVARI-004` | VIGO | Gjenbrukbare løsninger | Felles løsning for inntak og administrasjon i videregående opplæring | Organisatorisk samhandling<br>Sammenhengende tjenester<br>Dele data med andre<br>Datastyring<br>Oversikt over tjenester | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/73-VIGO-v2-codex.md) |
| 80 | `NOVARI-005` | VIGO-portalen | Gjenbrukbare løsninger | Brukerflate for VIGO-tjenester | Sammenhengende tjenester<br>Tjenestekjeder | [80-VIGO-portalen-v2-codex.md](operative-losninger-og-tjenester/80-VIGO-portalen-v2-codex.md) |
| 81 | `NOVARI-006` | VIGO Sentralbase | Gjenbrukbare løsninger | Felles datagrunnlag for VIGO | Grunndata<br>Datastyring<br>Dele data med andre | [81-VIGO-Sentralbase-v1-codex.md](operative-losninger-og-tjenester/81-VIGO-Sentralbase-v1-codex.md) |
| 82 | `NOVARI-007` | VIGO Kodeverk og kodeverksbase | Standarder og veiledning | Kodeverk | Informasjonsarkitektur<br>Forvaltningsstandarder | - |
| 83 | `NOVARI-008` | Arkivintegrasjoner | Gjenbrukbare løsninger | Integrasjonstjeneste for arkivflyt | Dele data med andre<br>Bruke data fra andre<br>Organisatorisk samhandling | - |
| 84 | `NOVARI-009` | vigo.no | Gjenbrukbare løsninger | Soknads- og informasjonstjeneste for videregaende opplaering | Sammenhengende tjenester<br>Tjenestekjeder | - |



## OpenPeppol (`OPP`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 11 | `OPP-001` | Peppol eDelivery | Gjenbrukbare løsninger | Internasjonalt samhandlingsrammeverk | Meldingsutveksling<br>Sikring av informasjonsflyt og datautveksling<br>Forvaltningsstandarder<br>Identifisering | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/11-Peppol-eDelivery-produkt-canvas-v3-codex.md) |



## EU / Europakommisjonen (`EU`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 41 | `EU-001` | European Digital Identity Wallet | Gjenbrukbare løsninger | Digital identitetslommebok | Autentisering<br>Signering | - |
| 42 | `EU-002` | eID Building Block | Gjenbrukbare løsninger | E-identifikasjonskomponent | Autentisering<br>Bruke data fra andre | - |
| 43 | `EU-003` | eDelivery Building Block | Gjenbrukbare løsninger | Byggestein / referanseramme for eDelivery | Meldingsutveksling<br>Sikring av informasjonsflyt og datautveksling | - |
| 44 | `EU-004` | eSignature Building Block | Gjenbrukbare løsninger | Signaturkomponent | Signering<br>Sikring av informasjonsflyt og datautveksling | - |
| 45 | `EU-005` | Once-Only Technical System (OOTS) | Gjenbrukbare løsninger | Grensekryssende datadelingsinfrastruktur | Dele data med andre<br>Organisatorisk samhandling | - |
| 53 | `EU-006` | EU Open Source Solutions Catalogue | Gjenbrukbare løsninger | Åpen kildekode-katalog for offentlig sektor | Gjenbrukbare tjenester<br>Integrerbare tjenester | - |
| 54 | `EU-007` | Interoperable Europe Solutions | Standarder og veiledning | Løsningskatalog for interoperabilitet | Samarbeidsarenaer og nettverk<br>Forvaltningsstandarder | - |
| 55 | `EU-008` | Core Vocabularies | Standarder og veiledning | Semantisk interoperabilitetsressurs | Informasjonsarkitektur<br>Forvaltningsstandarder | - |
| 90 | `EU-009` | Interoperable Europe Act | Økonomiske og juridiske rammer og virkemidler | Regulering og rammeverk | Samarbeidsarenaer og nettverk<br>Forvaltningsstandarder | - |
| 91 | `EU-010` | Assessment Toolbox | Standarder og veiledning | Vurderingsverktøy | Forvaltningsstandarder<br>Arkitekturstyring | - |
| 92 | `EU-011` | Assessment reports repository | Standarder og veiledning | Erfaringsbibliotek | Samarbeidsarenaer og nettverk<br>Samordning | - |



## Datatilsynet (`DTIL`)

| Løpenr | Ressurs-ID | Navn | Type | Emne | Kapabiliteter | Dokument |
|---:|---|---|---|---|---|---|
| 147 | `DTIL-001` | Regulatorisk sandkasse for kunstig intelligens | Standarder og veiledning | Veiledning om personvern i KI | Utvikling og formidling av veiledning<br>Regelverkstolkning | [Åpne](../../arkitektur/ressurser/normerende-ressurser/147-Regulatorisk-sandkasse-for-kunstig-intelligens-v1-claude.md) |



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


