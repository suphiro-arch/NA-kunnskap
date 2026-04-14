# Kapabilitesanalyse - flytting-elever-skolearet-mellom-kommuner-fylkeskommuner-v2

## Metadata
- Løpenummer: 19
- Filnavn: 19-kapabilitesanalyse-flytting-elever-skolearet-mellom-kommuner-fylkeskommuner-v2.md
- Dato: 2026-04-14
- Utarbeidet av / språkmodell: GitHub Copilot / GPT-5.3-Codex
- Kilde/case: Brukerinnspill i chat om flytting av elever mellom kommuner/fylkeskommuner i skoleåret

## 1. Kort problembilde
Behovet er å sikre at elevinformasjon følger eleven digitalt ved flytting i skoleåret, slik at ny skole raskt kan gi riktig oppfølging. Caset forutsetter hendelsesstyrt varsling, sikker og rettighetsstyrt datahenting, og et robust overgangsspor der API-modenhet mangler. For å lykkes nasjonalt må løsningene være standardiserte på tvers av kommuner, fylkeskommuner og leverandører.

## 2. Kapabilitetsmapping
| Kapabilitet | Rolle i helheten (kjerne/støtte) | Hvorfor relevant for problemet | Relevans (høy/middels) |
|---|---|---|---|
| Hendelsesdrevet | kjerne | Flyttehendelse fra Folkeregisteret eller skoleinntak må starte prosessen uten manuell koordinering. | høy |
| Dele data med andre | kjerne | Fraflyttingskommune må kunne dele elevdata strukturert og kontrollert med ny skoleeier. | høy |
| Bruke data fra andre | kjerne | Tilflyttingskommune må kunne hente og ta i bruk både grunnpakke og utvidet pakke i fagsystemene. | høy |
| Tilgangskontroll | kjerne | Sensitive elevopplysninger krever presis kontroll av roller, formål og tilgangsnivå. | høy |
| Informasjonsarkitektur | kjerne | Standardisert elevmappe og felles begreper er nødvendig for at data tolkes likt mellom systemer. | høy |
| Juridisk samhandling | kjerne | Deling mellom forvaltningsnivåer krever tydelig hjemmel, samtykkelogikk og ansvarslinjer for å fungere i praksis. | høy |
| Meldingsformidling | støtte | Ved manglende API-støtte trengs et sikkert og sporbart spor for standardisert filutveksling. | middels |
| Organisatorisk samhandling | støtte | Kommuner, fylkeskommuner og leverandører må samordne innføring, ansvar og driftspraksis. | middels |

Retningslinje:
- 3-6 kjernekapabiliteter med høy relevans.
- 1-3 støttekapabiliteter med middels relevans.
- Kapabiliteter uten delkapabiliteter vurderes som fullverdige på lik linje med øvrige kapabiliteter.
- Kritiske kapabiliteter skal ikke utelates kun for å treffe antall.

## 3. Mulige gjenbrukbare ressurser
| Ressurs-ID | Ressursnavn | Relevans (høy/middels/lav) | Hvordan kan den gjenbrukes | Merknad/usikkerhet |
|---|---|---|---|---|
| `SKATT-001` | Folkeregisteret | høy | Leverer flyttehendelse/adresseendring som trigger videre prosess for skoleflytting. | Krever avklaring av hvilke hendelser som skal trigge automatisk flyt. |
| `DIGDIR-010` | Altinn Events | høy | Brukes til notification-first for å varsle mottaker om at elevdata kan hentes. | Krever enhetlige hendelsestyper og livssyklusregler. |
| `DIGDIR-002` | Maskinporten | høy | Sikrer maskin-til-maskin autentisering ved API-henting mellom systemer. | Avhenger av presis tilgangsstyring i sektoren. |
| `DIGDIR-004` | Altinn Autorisasjon | høy | Kan håndtere rettigheter/representasjon der tilgang avhenger av rolle og mandat. | Krever avklaring av sektorprofil for skoleområdet. |
| `DIGDIR-008` | Altinn Formidling | middels | Dekker overgangsspor for standardisert filutveksling når API ikke er tilgjengelig. | Bør være overgangsmekanisme, ikke varig målbilde. |
| `DIGDIR-012` | Begrepskatalog | høy | Støtter felles begrepsforvaltning for elevmappeinnhold på tvers av aktører. | Krever sektorforankring og aktiv forvaltning. |
| `DIGDIR-011` | Felles datakatalog | middels | Synliggjør datasett, modeller og API-er som inngår i flytteprosessen. | Nytten er avhengig av kvalitet og oppdatering i publisert metadata. |
| `NOVARI-003` | FINT Informasjonsmodell | middels | Kan gi et felles semantisk utgangspunkt mellom leverandører i skolekontekst. | Må harmoniseres med SIKT/KS-standarder i videre arbeid. |

## 4. Foreløpig konklusjon
- mest dekkende kapabiliteter fra underlaget og de mest lovende gjenbrukbare ressurser: Hendelsesdrevet, Dele/Bruke data, Tilgangskontroll, Informasjonsarkitektur og Juridisk samhandling støttet av `SKATT-001`, `DIGDIR-010`, `DIGDIR-002` og `DIGDIR-004`.
- viktigste usikkerheter: juridisk avklaring for automatisert deling av sensitive elevdata, samtykkegrenser, og faktisk API-modenhet i alle kommuner/fylkeskommuner.
- viktige avklaringer å ta stilling til: standard for innhold i elevmappe, felles leverandørkrav, og tydelig grense mellom målarkitektur og overgangsspor.
- eksplisitt vurdering av behov utover dagens grunnlag: datakvalitet ved kilden og sterkere tverrsektoriell samordning (inkludert kobling mot PPT/barnevern) vurderes som delvis dekket og må konkretiseres videre.
