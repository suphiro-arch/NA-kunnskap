# Ressursregister og ressurs-ID-er

> Status: Midlertidig arbeidsnotat fra overgangsfasen. Denne fila er ikke operativ master. Nye ressurser og ressurs-ID-er skal nå føres i `arkitektur/produkter/produktnummerering.md`.

Kilde: overgangsregister bygget fra eksisterende produktregister, nye ressursbeskrivelser under `arkitektur/ressurser/`, `sources/links.md` og styringsreglene i `arkitektur/ressurser/styringsregler.md`.

## Formål
- være nytt felles register for hele ressursområdet, ikke bare klassiske produktbeskrivelser
- gi én framtidig master for operative løsninger og tjenester, normerende ressurser og samarbeidsfora
- gjøre overgangen fra `arkitektur/produkter/` til `arkitektur/ressurser/` mulig uten å miste sporbarhet

## Overgangsstatus
- dette er et første arbeidsutkast til ny registerstruktur
- dagens operative produktregister ligger fortsatt i `arkitektur/produkter/produktnummerering.md`
- nye ressurser skal nå føres i `arkitektur/produkter/produktnummerering.md`
- eksisterende operative ressursrader skal senere migreres inn hit i samlet flytteløp

## Prinsipp
- `Løpenr` beholdes som stabil intern sortering for operative løsninger og tjenester som allerede har etablert nummerering
- `Ressurs-ID` er kanonisk identifikator og brukes på tvers av ressurskategorier
- `Ressursområde` skiller mellom `operative løsninger og tjenester`, `normerende ressurser` og `samarbeidsfora`
- `Ressurskategori` beskriver ressursen på første funksjonelle nivå, for eksempel `felleskomponent`, `plattform`, `informasjonsmodell` eller `samarbeidsforum`
- `Type ressurs` beskriver ressursen mer presist på neste nivå
- `Merknad` brukes til korte avgrensninger eller viktige vurderinger som bør følge ressursen videre
- nye ressurser får neste ledige nummer innenfor sin eierkode når ressursen er tydelig nok avgrenset til å stå som egen enhet
- rader uten full beskrivelse kan stå som arbeidsutkast med `Ikke opprettet ennå`

## Foreslåtte eierkoder
| Eierkode | Eier | Bruk |
|---|---|---|
| `DIGDIR` | Digdir | Digitale fellesløsninger og Altinn-relaterte løsninger forvaltet i Digdir-regi |
| `BRREG` | Brønnøysundregistrene | Register- og samhandlingsløsninger forvaltet av Brønnøysundregistrene |
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
| `EU` | EU / Europakommisjonen | Relevante europeiske felleskomponenter, byggesteiner og normerende ressurser |
| `NOVARI` | Novari IKS | Fylkeskommunale fellesressurser og relaterte modeller og løsninger |

## Første rader i ny struktur

## Novari (`NOVARI`)
| Løpenr | Ressurs-ID | Navn | Ressursområde | Ressurskategori | Type ressurs | Merknad | Kapabilitetstreff | Siste versjon | Dokument |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | `NOVARI-001` | FINT Felleskomponent | Operative løsninger og tjenester | Felleskomponent | Integrasjons- og datadelingstjeneste | Operativ kjernekomponent i FINT-økosystemet | Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Bruke data fra andre<br>Informasjonsforvaltning: Informasjonsarkitektur<br>Tjenesteutvikling: Integrerbare tjenester<br>Tjenesteutvikling: Gjenbrukbare tjenester<br>Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling | v1 (codex) | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/fint-felleskomponent-v1-codex.md) |
| 2 | `NOVARI-002` | FINT Arkiv | Operative løsninger og tjenester | Fellesløsning | Arkiv- og integrasjonstjeneste | Operativ spesialressurs for standardisert utveksling av arkivinformasjon | Datautveksling og integrasjon: Dele data med andre<br>Datautveksling og integrasjon: Bruke data fra andre<br>Informasjonsforvaltning: Informasjonsarkitektur<br>Tjenesteutvikling: Integrerbare tjenester<br>Standardisering: Forvaltningsstandarder | v1 (codex) | [Åpne](../../arkitektur/ressurser/operative-losninger-og-tjenester/fint-arkiv-v1-codex.md) |
| 3 | `NOVARI-003` | FINT Informasjonsmodell | Normerende ressurser | Normerende ressurs | Informasjonsmodell | Semantisk og strukturelt grunnlag for FINT-økosystemet | Informasjonsforvaltning: Informasjonsarkitektur<br>Informasjonsforvaltning: Oversikt over informasjonsmodeller<br>Standardisering: Forvaltningsstandarder | v1 (codex) | [Åpne](../../arkitektur/ressurser/normerende-ressurser/fint-informasjonsmodell-v1-codex.md) |
| 4 | `NOVARI-004` | VIGO | Operative løsninger og tjenester | Sektorløsning | Felles løsning for inntak og administrasjon i videregående opplæring | Bør avgrenses tydelig mot delressurser som VIGO-portalen og Sentralbase når beskrivelsen lages | Ikke kvalitetssikret ennå | Ikke opprettet ennå | - |

## Merknad
Denne fila ble laget for å teste en bredere ressursstruktur før endelig avklaring. Etter avklaringen om å beholde én operativ master videreføres registerføringen i `arkitektur/produkter/produktnummerering.md`.

## Neste naturlige utvidelser
- migrere hele Digdir-delen inn i dette registeret som første store operative bolk
- opprette første operative beskrivelse for `FINT Arkiv`
- opprette første operative beskrivelse for `VIGO`
- vurdere om `VIGO-portalen` og `VIGO Sentralbase` skal være egne ressurser eller delressurser under `VIGO`

## Nye kandidater lagt inn i masterregisteret (2026-04-09)

Nye forslag fra `sources/links.md` er lagt inn i `arkitektur/produkter/produktnummerering.md` som arbeidsutkast med `Ikke opprettet ennå`.

Omfang i denne runden:
- KS: `KS-011` til `KS-015`
- NHN: `NHN-005`
- NOVARI: `NOVARI-005` til `NOVARI-009`

Disse beholdes i masterregisteret inntil videre, i tråd med overgangsregelen for denne fila.
