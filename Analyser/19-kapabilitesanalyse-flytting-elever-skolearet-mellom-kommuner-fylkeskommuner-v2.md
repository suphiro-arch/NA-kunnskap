# Kapabilitesanalyse - flytting-elever-skolearet-mellom-kommuner-fylkeskommuner-v2

## Metadata
- Løpenummer: 19
- Filnavn: 19-kapabilitesanalyse-flytting-elever-skolearet-mellom-kommuner-fylkeskommuner-v2.md
- Dato: 2026-04-14
- Utarbeidet av / språkmodell: GitHub Copilot / GPT-5.3-Codex
- Kilde/case: Brukerinnspill i chat om flytting av elever mellom kommuner/fylkeskommuner i skoleåret, analysert uten bruk av retningslinje om antall kapabiliteter

## 1. Kort problembilde
Behovet er å sikre at elevinformasjon følger eleven digitalt ved flytting i skoleåret, slik at ny skole raskt kan gi riktig oppfølging fra første dag. Caset forutsetter hendelsesstyrt varsling, sikker og rettighetsstyrt datahenting, og et robust overgangsspor der API-modenhet mangler. For å lykkes nasjonalt må løsningene være standardiserte på tvers av kommuner, fylkeskommuner og leverandører, samtidig som de håndterer samtykke, hjemmel, datakvalitet og samordning med andre tjenester rundt barnet.

## 2. Kapabilitetsmapping
| Kapabilitet | Rolle i helheten (kjerne/støtte) | Hvorfor relevant for problemet | Relevans (høy/middels) |
|---|---|---|---|
| Hendelsesdrevet | kjerne | Flyttehendelse fra Folkeregisteret eller skoleinntak må starte prosessen uten manuell koordinering. | høy |
| Dele data med andre | kjerne | Fraflyttingskommune må kunne dele elevdata strukturert og kontrollert med ny skoleeier. | høy |
| Bruke data fra andre | kjerne | Tilflyttingskommune må kunne hente og ta i bruk både grunnpakke og utvidet pakke i fagsystemene. | høy |
| Tilgangskontroll | kjerne | Sensitive elevopplysninger krever presis kontroll av roller, formål og tilgangsnivå. | høy |
| Informasjonsarkitektur | kjerne | Standardisert elevmappe og felles begreper er nødvendig for at data tolkes likt mellom systemer. | høy |
| Juridisk samhandling | kjerne | Deling mellom forvaltningsnivåer krever tydelig hjemmel, samtykkelogikk og ansvarslinjer for å fungere i praksis. | høy |
| Sikring av informasjonsflyt og datautveksling | kjerne | Flytting av sensitive elevopplysninger krever trygg transport, beskyttelse mot uautorisert innsyn og sporbar kontroll. | høy |
| Meldingsformidling | støtte | Ved manglende API-støtte trengs et sikkert og sporbart spor for standardisert filutveksling. | middels |
| Datastyring | støtte | Datakvalitet ved kilden, avvikshåndtering og ansvar for elevmappeinnhold må være tydelig definert. | middels |
| Organisatorisk samhandling | støtte | Kommuner, fylkeskommuner og leverandører må samordne innføring, ansvar og driftspraksis. | middels |
| Samtykke | støtte | Alternativløpet med foreldres samtykke gjør denne kapabiliteten relevant i deler av caset. | middels |
| Representasjon | støtte | Foreldre må i noen situasjoner kunne opptre digitalt på vegne av barnet i flytte- og samtykkeløpet. | middels |
| Forvaltningsstandarder | støtte | Felles standard for elevmappe, API-er og meldingsformater må forankres og forvaltes over tid. | middels |
| Samordning | støtte | Nasjonal innføring krever koordinering mellom kommuner, fylker, leverandører og statlige aktører. | middels |

Retningslinje:
- 3-6 kjernekapabiliteter med høy relevans.
- 1-3 støttekapabiliteter med middels relevans.
- Kapabiliteter uten delkapabiliteter vurderes som fullverdige på lik linje med øvrige kapabiliteter.
- Kritiske kapabiliteter skal ikke utelates kun for å treffe antall.

## 3. Mulige gjenbrukbare ressurser
| Ressurs-ID | Ressursnavn | Relevans (høy/middels/lav) | Hvordan kan den gjenbrukes | Merknad/usikkerhet |
|---|---|---|---|---|
| `KS-008` | Fiks folkeregister | høy | Kan brukes som kommunalt tilgangslag til Folkeregisteret for å oppdage og bruke flyttehendelser. | Må avklares hvordan hendelser og oppslag faktisk brukes i flytteløpet. |
| `KS-001` | FIKS-plattformen | høy | Kan være felles kommunal kjerne for integrasjon, tilgangsstyring og samhandling mellom aktørene. | Rollen må avklares mot nasjonale felleskomponenter i målbildet. |
| `DIGDIR-010` | Altinn Events | høy | Kan brukes til notification-first der mottaker varsles om at elevdata kan hentes. | Krever felles hendelsestyper og livssyklusregler. |
| `DIGDIR-002` | Maskinporten | høy | Sikrer maskin-til-maskin autentisering ved API-henting mellom systemer. | Avhenger av presis tilgangsstyring i sektoren. |
| `DIGDIR-004` | Altinn Autorisasjon | høy | Kan håndtere rettigheter og representasjon der tilgang avhenger av rolle og mandat. | Krever avklaring av sektorprofil for skoleområdet. |
| `KS-002` | Fiks melding | høy | Dekker Spor C for sikker og standardisert fil- eller meldingsutveksling når API ikke er tilgjengelig. | Bør være overgangsmekanisme, ikke varig målbilde. |
| `DIGDIR-012` | Begrepskatalog | høy | Støtter felles begrepsforvaltning for elevmappeinnhold på tvers av aktører. | Krever sektorforankring og aktiv forvaltning. |
| `DIGDIR-011` | Felles datakatalog | middels | Synliggjør datasett, modeller og API-er som inngår i flytteprosessen. | Nytten er avhengig av kvalitet og oppdatering i publisert metadata. |
| `DIGDIR-013` | API-katalog | middels | Gjør det enklere å oppdage og forstå standardiserte API-er mellom aktørene. | Avhenger av moden API-beskrivelse hos leverandørene. |
| `NOVARI-003` | FINT Informasjonsmodell | høy | Kan gi et felles semantisk utgangspunkt mellom leverandører i skolekontekst. | Må harmoniseres med SIKT- og KS-standarder i videre arbeid. |

| Ressurs-ID | Ressursnavn | Relevans (høy/middels/lav) | Hvordan kan den gjenbrukes | Merknad/usikkerhet |
|---|---|---|---|---|
| `DIGDIR-027` | Arkitektur for hendelser | høy | Gir et normerende mønster for notification-first og hendelsesdrevet samhandling. | Ikke operativ løsning, men viktig som referanseramme. |
| `DIGDIR-034` | Referansearkitektur forespørsel-svar (eOppslag) | høy | Understøtter mønsteret der mottaker henter detaljer etter en mottatt notifikasjon. | Må oversettes til konkrete sektor-API-er. |
| `DIGDIR-047` | Digitaliseringsvennlig regelverk | middels | Relevant for å vurdere hvordan hjemmel og samtykke kan støtte digital flyt. | Krever juridisk oppfølging, ikke bare arkitekturarbeid. |
| `KS-011` | Felles mal for innforing av digitale fellestjenester | middels | Kan støtte innføring og samordning når mange kommuner og leverandører skal ta i bruk samme mønster. | Ikke løsningskomponent, men relevant for skalerbar innføring. |

## 4. Foreløpig konklusjon
- mest lovende ressurser: Spor A+B støttes best av `KS-008`, `KS-001`, `DIGDIR-010`, `DIGDIR-002`, `DIGDIR-004`, `DIGDIR-012` og `NOVARI-003`, mens Spor C støttes tydelig av `KS-002`.
- viktigste usikkerheter: juridisk hjemmelsavklaring, samtykkegrenser, faktisk API-modenhet i alle kommuner/fylkeskommuner og hvor raskt leverandørene kan støtte felles standarder.
- viktige avklaringer å ta stilling til: tydelig rollefordeling mellom kommunal kjerne og nasjonale felleskomponenter, konkret standard for elevmappeinnhold, og hvordan kobling mot PPT/barnevern skal avgrenses eller fases inn.
- eksplisitt vurdering av behov utover dagens grunnlag: datakvalitet ved kilden og sterkere tverrsektoriell samordning fremstår fortsatt som delvis dekket, men den brede analysen viser at repoet allerede har flere relevante kapabiliteter og normerende ressurser enn den strammere versjonen synliggjorde.
