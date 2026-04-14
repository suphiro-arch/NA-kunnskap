# Kapabilitesanalyse - flytting-elever-skolearet-mellom-kommuner-fylkeskommuner

## Metadata
- Løpenummer: 18
- Filnavn: 18-kapabilitesanalyse-flytting-elever-skolearet-mellom-kommuner-fylkeskommuner.md
- Dato: 2026-04-14
- Kilde/case: Brukerinnspill i chat om flytting av elever mellom kommuner/fylkeskommuner i skoleåret

## 1. Kort problembilde
Behovet er å sikre at elevinformasjon følger eleven raskt, sikkert og standardisert ved flytting i skoleåret, slik at ny skole kan gi riktig oppfølging fra første dag. Caset krever en hendelsesdrevet modell med autorisert datahenting, der sensitive opplysninger bare deles ved dokumentert behov og hjemmel. Samtidig må løsningen håndtere både et ønsket målbildespor (notifikasjon og API) og et overgangsspor der enkelte kommuner fortsatt trenger sikker filformidling.

## 2. Kapabilitetsmapping
| Kapabilitet | Rolle i helheten (kjerne/støtte) | Hvorfor relevant for problemet | Relevans (høy/middels) |
|---|---|---|---|
| Hendelsesdrevet | kjerne | Flyttehendelse i Folkeregisteret eller skoleinntak må trigge varsling og videre dataflyt uten manuell oppfølging. | høy |
| Dele data med andre | kjerne | Fraflyttingskommune må kunne dele elevopplysninger kontrollert til mottakende kommune/fylkeskommune. | høy |
| Bruke data fra andre | kjerne | Tilflyttingskommune må kunne hente og bruke grunnpakke og eventuelt utvidet pakke i eget fagsystem. | høy |
| Tilgangskontroll | kjerne | Deling av taushetsbelagte opplysninger krever presis kontroll av hvem som kan få tilgang til hva og til hvilket formål. | høy |
| Informasjonsarkitektur | kjerne | Standardisert elevmappe, felles begreper og semantikk er avgjørende for at data kan tolkes likt på tvers av systemer. | høy |
| Meldingsformidling | støtte | Overgangssporet for kommuner uten API-støtte trenger sikker og sporbar fil- eller meldingsutveksling. | middels |
| Organisatorisk samhandling | støtte | Kommuner, fylkeskommuner, leverandører og nasjonale aktører må samordne prosess, ansvar og implementeringstakt. | middels |

Retningslinje:
- 3-5 kjernekapabiliteter med høy relevans.
- 1-3 støttekapabiliteter med middels relevans.
- Kapabiliteter uten delkapabiliteter vurderes som fullverdige på lik linje med øvrige kapabiliteter.

## 3. Mulige gjenbrukbare ressurser
| Ressurs-ID | Ressursnavn | Relevans (høy/middels/lav) | Hvordan kan den gjenbrukes | Merknad/usikkerhet |
|---|---|---|---|---|
| `SKATT-001` | Folkeregisteret | høy | Kilde for flyttehendelse og identifikasjon av adresseendring som starter prosessen. | Krever avklaring av hvilke hendelser som skal trigge skoleflyt direkte. |
| `DIGDIR-010` | Altinn Events | høy | Hendelsesnotifikasjon mellom aktører i notification-first-mønster. | Krever felles hendelsestyper og livssyklus for elevflytting. |
| `DIGDIR-002` | Maskinporten | høy | Sikker maskin-til-maskin-autentisering ved API-oppslag av elevdata. | Må kombineres med tydelig tilgangs- og formålsstyring. |
| `DIGDIR-004` | Altinn Autorisasjon | høy | Håndtere rettigheter og representasjon der tilgang avhenger av rolle og mandat. | Behov for sektorprofil for skolekontekst må avklares. |
| `DIGDIR-008` | Altinn Formidling | middels | Overgangsspor for standardisert og sikker filutveksling når API-støtte mangler. | Bør brukes som overgangsmekanisme, ikke varig målarkitektur. |
| `DIGDIR-011` | Felles datakatalog | middels | Synliggjøre datasett, informasjonsmodeller og API-er som inngår i elevflyten. | Nytten avhenger av faktisk publisering og vedlikehold fra dataeiere. |
| `DIGDIR-012` | Begrepskatalog | høy | Standardisere sentrale begreper i elevmappe og flytteprosess. | Krever sektorforankring for felles definisjoner. |
| `NOVARI-003` | FINT Informasjonsmodell | middels | Kan brukes som grunnlag for semantisk harmonisering av elevdata på tvers av leverandører. | Relevans må vurderes opp mot SIKT/KS-standarder i videre arbeid. |

## 4. Foreløpig konklusjon
- mest dekkende kapabiliteter fra underlaget og de mest lovende gjenbrukbare ressurser: Hendelsesdrevet, Dele/Bruke data, Tilgangskontroll og Informasjonsarkitektur støttet av `SKATT-001`, `DIGDIR-010`, `DIGDIR-002` og `DIGDIR-004`.
- viktigste usikkerheter: juridisk hjemmelsavklaring, samtykkegrenser for sensitive opplysninger og modenhet for API-støtte i alle kommuner/fylkeskommuner.
- viktige avklaringer å ta stilling til: standard for elevmappeinnhold, nasjonal samordning av leverandørkrav, og tydelig overgangsmønster der API ikke er klart.
- eksplisitt vurdering av behov utover dagens grunnlag: `Datakvalitet ved kilden` og sterkere tverrsektoriell samordning vurderes som delvis dekket og bør avklares i full analyse.
- anbefaling: gå videre til full analyse.

## Begreper fra repo brukt i mapping
- Hendelsesdrevet
- Dele data med andre
- Bruke data fra andre
- Tilgangskontroll
- Informasjonsarkitektur
- Juridisk samhandling
- Meldingsformidling
- Datastyring
