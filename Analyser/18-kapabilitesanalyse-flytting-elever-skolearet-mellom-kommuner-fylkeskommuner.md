# Kapabilitesanalyse - flytting-elever-skolearet-mellom-kommuner-fylkeskommuner

## Metadata
- Løpenummer: 18
- Filnavn: 18-kapabilitesanalyse-flytting-elever-skolearet-mellom-kommuner-fylkeskommuner.md
- Dato: 2026-04-14
- Utarbeidet av / språkmodell: GitHub Copilot / GPT-5.3-Codex
- Kilde/case: Brukerinnspill i chat om flytting av elever mellom kommuner/fylkeskommuner i skoleåret

## 1. Kort problembilde
Behovet er å sikre at elevinformasjon følger eleven digitalt og automatisk ved flytting i skoleåret, slik at ny skole raskt kan gi et riktig og tilrettelagt tilbud. Caset bygger på et hovedmønster der flyttehendelse utløser varsling og rettighetsstyrt datahenting, men krever også et overgangsspor for kommuner som ennå ikke har API-støtte. For å lykkes må både hjemmel, semantikk og teknisk samhandling være tydelig avklart.

## 2. Kapabilitetsmapping
| Kapabilitet | Rolle i helheten (kjerne/støtte) | Hvorfor relevant for problemet | Relevans (høy/middels) |
|---|---|---|---|
| Hendelsesdrevet | kjerne | Flyttehendelse fra Folkeregisteret eller skoleinntak må starte flyten uten manuell koordinering. | høy |
| Dele data med andre | kjerne | Fraflyttingskommune må kunne dele elevopplysninger kontrollert med ny skoleeier. | høy |
| Bruke data fra andre | kjerne | Tilflyttingskommune må kunne hente og bruke grunnpakke og utvidet pakke i egne fagsystem. | høy |
| Tilgangskontroll | kjerne | Sensitive elevopplysninger krever presis kontroll av roller, formål og tilgangsnivå. | høy |
| Informasjonsarkitektur | kjerne | Standardisert elevmappe og felles begreper er nødvendig for at data tolkes likt mellom systemer. | høy |
| Juridisk samhandling | kjerne | Deling mellom forvaltningsnivåer krever tydelig hjemmel, samtykkelogikk og ansvarslinjer. | høy |
| Meldingsformidling | støtte | Spor C for manglende API-støtte krever sikker og sporbar fil- eller meldingsutveksling. | middels |
| Organisatorisk samhandling | støtte | Kommuner, fylkeskommuner og leverandører må samordne prosess og innføring. | middels |

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
| `DIGDIR-002` | Maskinporten | høy | Sikrer maskin-til-maskin autentisering ved API-henting mellom systemer. | Avhenger av presis tilgangsstyring og hjemmel. |
| `DIGDIR-004` | Altinn Autorisasjon | høy | Kan håndtere rettigheter og representasjon der tilgang avhenger av rolle og mandat. | Krever sektorprofil for skoleområdet. |
| `KS-002` | Fiks melding | høy | Dekker Spor C for sikker og standardisert fil- eller meldingsutveksling når API ikke er tilgjengelig. | Bør være overgangsmekanisme, ikke varig målbilde. |
| `DIGDIR-012` | Begrepskatalog | middels | Støtter felles begrepsforvaltning for innholdet i elevmappen. | Krever sektorforankring og aktiv forvaltning. |
| `NOVARI-003` | FINT Informasjonsmodell | middels | Kan gi et semantisk utgangspunkt mellom leverandører og skolefagsystemer. | Må harmoniseres med SIKT- og KS-standarder i videre arbeid. |

## 4. Foreløpig konklusjon
- mest lovende ressurser: et hovedmønster med `KS-008`, `KS-001`, `DIGDIR-010`, `DIGDIR-002` og `DIGDIR-004` dekker Spor A+B, mens `KS-002` er en sterk kandidat for Spor C.
- viktigste usikkerheter: juridisk hjemmelsavklaring, samtykkegrenser, og hvor moden API-støtten faktisk er hos kommuner og leverandører.
- viktige avklaringer å ta stilling til: standard for innhold i elevmappe, tydelig rollefordeling mellom kommunal kjerne og nasjonale felleskomponenter, og hvordan samtykkesporet skal løses digitalt.
- eksplisitt vurdering av behov utover dagens grunnlag: datakvalitet ved kilden og sterkere tverrsektoriell samordning rundt barn med sammensatte behov fremstår som delvis dekket og må konkretiseres videre.