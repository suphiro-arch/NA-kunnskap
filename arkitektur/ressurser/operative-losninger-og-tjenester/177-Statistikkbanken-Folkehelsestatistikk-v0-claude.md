# Statistikkbanken Folkehelsestatistikk

## Navn
Statistikkbanken Folkehelsestatistikk

## Ressurs ID
HDIR-003

## Status/Livsfase
**Produksjon** – statistikkbanken er i drift og har erstattet Kommunehelsa og Norgeshelsa.

**Fakta:** Helsedirektoratet oppgir at statistikkbankene Kommunehelsa og Norgeshelsa er erstattet av Statistikkbanken Folkehelsestatistikk. De gamle bankene er ikke oppdatert siden våren 2024 og ble stengt 10. november 2025 (helsedirektoratet.no, side først publisert 8. september 2025).

**Fakta:** Statistikkbanken oppdateres løpende etter hvert som nye data foreligger (helsedirektoratet.no, Bruk av statistikkbanken).

## Modenhet
**Middels til høy modenhet: etablert innhold på en ny publiseringsflate.**

- Statistikkbanken er grunnlaget for folkehelseprofilene og oppvekstprofilene, som publiseres årlig for kommuner, bydeler og fylker (helsedirektoratet.no).
- Data kan hentes maskinelt gjennom FHI Statistikk Open API, med dokumentasjon i Swagger og på GitHub (fhi.no; statistikk-data.fhi.no).
- Tabellene har metadata om innsamling, kilde, betydning og feilkilder (helsedirektoratet.no, Bruk av statistikkbanken).
- Veiledningen for banken ble først publisert i februar 2025, og de gamle bankene kunne ikke viderekobles fra gamle bokmerker (helsedirektoratet.no).

**Deduksjon:** Det svakeste leddet er at ansvaret er delt mellom to virksomheter uten at fordelingen er beskrevet samlet. Helsedirektoratet står for innholdet, mens publiseringsflaten og API-et er FHIs. For den som skal bygge varige integrasjoner, er det derfor uklart hvem som svarer for tilgjengelighet og endringer i grensesnittet.

## Kort beskrivelse
Statistikkbanken Folkehelsestatistikk er den nasjonale statistikkbanken for folkehelse, med statistikk om befolkning, oppvekst og levekår, fysisk og sosialt miljø, skader og ulykker, helserelatert atferd og helsetilstand. Statistikken finnes for kommuner, fylker og hele landet, og for bydeler i de fire største byene.

Banken erstatter Kommunehelsa og Norgeshelsa, og er grunnlaget for folkehelseprofilene og oppvekstprofilene som kommuner og fylker bruker i oversiktsarbeidet etter folkehelseloven.

Helsedirektoratet står for innholdet. Banken publiseres på FHIs plattform FHI Statistikk (statistikk.fhi.no), der den er én av flere kilder, og kan hentes maskinelt gjennom FHI Statistikk Open API.

## Kapabiliteter
Helsedirektoratet publiserer folkehelsestatistikken åpent, og ingen annen ressurs gir den samme samlede statistikken for kommuner, bydeler og fylker. Publiseringsplattformen og API-et driftes av FHI; det er en avhengighet, ikke en egen kapabilitet.

- **Datakilder: Åpne data** Statistikkbanken gjør folkehelsestatistikk for kommuner, bydeler, fylker og hele landet åpent tilgjengelig i tabeller, figurer, nedlastbare filer og et åpent API.

## Produktmål
**Fakta:** Folkehelseprofilene skal gi kommuner og fylker oppdatert og relevant statistikk om helse, levekår og oppvekstforhold (Helsedirektoratets årsrapport 2024). Profilene bygger på statistikkbanken (helsedirektoratet.no, Bruk av statistikkbanken).

**Deduksjon:** Statistikkbanken skal støtte kommunenes og fylkenes plikt til å ha oversikt over helsetilstanden og faktorer som påvirker den. Det følger av at profilene og veiledningen er rettet mot oversiktsarbeidet etter folkehelseloven.

## Brukerbehov
Kommuner og fylkeskommuner skal ha oversikt over helsetilstanden i befolkningen og over faktorer som påvirker den. De trenger sammenlignbar statistikk for eget område, over tid og mot andre kommuner og landet, uten å sette sammen tall fra mange kilder selv.

Statistikkbanken dekker dette med ferdig tilrettelagte indikatorer på tvers av temaer, med metadata som forklarer hva tallene betyr og hvilke feilkilder de har.

## Hvem er brukerne og brukersegmentene

| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Lokale folkehelsetall over tid og mot andre | Oversiktsarbeid etter folkehelseloven, planarbeid | Profilene bygger på banken |
| Bydeler i de fire største byene | Tall for bydelen | Lokalt folkehelsearbeid | Bydelsnivå finnes for de fire største byene |
| Statlige myndigheter | Nasjonalt bilde av folkehelseutviklingen | Styring, oppfølging, rapportering | – |
| Forskere og analysemiljøer | Tidsserier på aggregert nivå | Forskning og evaluering | Data på individnivå går gjennom andre kanaler |
| Utviklere og analysemiljøer i virksomheter | Maskinell henting | Egne dashbord og systemer | Gjennom FHI Statistikk Open API |

## Hovedfunksjoner
Den første hovedfunksjonen er **statistikk på tvers av folkehelsetemaer**. Banken samler indikatorer om befolkning, oppvekst og levekår, miljø, skader, helserelatert atferd og helsetilstand, som tidligere lå i Kommunehelsa og Norgeshelsa. Statistikken er tilrettelagt for kommuner, fylker, hele landet og bydeler i de fire største byene.

Den andre er **visning, filtrering og nedlasting**. Brukeren velger utvalg etter geografi, år, kjønn, alder og andre tilvalg, og ser resultatet som tabell eller figur. Tabeller kan deles med lenke eller lastes ned som CSV eller Excel. Under hver tabell finnes metadata om innsamling, kilde, betydning og feilkilder.

Den tredje er **grunnlag for folkehelse- og oppvekstprofilene**. Profilene bygger på statistikkbanken og viser rundt 30 nøkkelindikatorer. De lastes ned fra Helsedirektoratets nettsider.

Den fjerde er **maskinell henting gjennom FHI Statistikk Open API**. Folkehelsestatistikken er publisert som egen kilde i API-et, med Helsedirektoratet som utgiver. API-et gir endepunkter for kilder, tabeller, dimensjoner, data og metadata, og leverer JSON-stat2, CSV og Parquet.

### Typiske brukssituasjoner (generisk)
- hente tall om helse, levekår og oppvekst for egen kommune som grunnlag for oversiktsarbeid og planarbeid
- sammenligne kommuner, bydeler eller fylker over tid på samme indikatorer
- hente folkehelseindikatorer maskinelt inn i egne dashbord
- finne bakgrunnstall for indikatorene i folkehelseprofilene

### Når Statistikkbanken Folkehelsestatistikk normalt ikke er førstevalg
Banken er ikke førstevalg når analysen trenger data på individnivå eller fra enkeltregistre. Da går veien gjennom registerforvalterne og søknadsløpet som `HDIR-001` Helsedata.no gir inngang til.

Den er heller ikke førstevalg for generell befolknings- og samfunnsstatistikk utenfor folkehelseområdet. Den finnes i `SSB-003` Statistikkbanken hos SSB.

For statistikk fra enkeltregistre hos FHI, som Dødsårsaksregisteret, er FHIs egne kilder på samme plattform mer relevante.

### Scope og avgrensning
Inngår:
- Statistikkbanken Folkehelsestatistikk med indikatorer for kommuner, bydeler, fylker og hele landet
- visning, filtrering, nedlasting og metadata
- kilden «Folkehelsestatistikk» i FHI Statistikk Open API

Inngår ikke:
- folkehelse- og oppvekstprofilene som egne dokumenter, selv om de bygger på banken
- FHI Statistikk som plattform, og FHIs andre kilder på plattformen
- de nedlagte bankene Kommunehelsa og Norgeshelsa
- data på individnivå og søknad om tilgang til helsedata

## Veikart over kommende funksjonalitet
**Ikke offentlig dokumentert:** Planer for videreutvikling av statistikkbanken eller av FHI Statistikk Open API. FHI oppgir at flere statistikker vil bli lagt til fortløpende på plattformen, men ikke hva som gjelder for folkehelsestatistikken.

## Forretningsverdi/Verdiforslag
For kommuner og fylkeskommuner ligger verdien i ferdig tilrettelagt, sammenlignbar statistikk for oversiktsarbeidet, med samme indikatorer som i folkehelseprofilene.

For staten ligger verdien i et felles tallgrunnlag for å følge folkehelseutviklingen nasjonalt og regionalt.

For forskning og analyse ligger verdien i åpne tidsserier med metadata, som kan hentes maskinelt.

For innbyggere og presse ligger verdien i innsyn i helse- og levekårsforhold der de bor.

## Utfordringer og risiko

| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Ansvarsdeling | Innhold og plattform har ulike forvaltere, og fordelingen er ikke beskrevet samlet | Uavklart |
| Juridisk | Lisensvilkår for dataene er ikke oppgitt | Ikke offentlig dokumentert |
| Kontinuitet | Gamle lenker og bokmerker til Kommunehelsa og Norgeshelsa virker ikke | Helsedirektoratet oppgir at viderekobling ikke er mulig |
| Teknisk | Datauttrekk over en angitt radgrense gir feil i API-et | Filtrene må avgrenses eller grensen økes i forespørselen |
| Leveransesikkerhet | Ingen tjenestenivåavtale er funnet | Ikke offentlig dokumentert |

## Kanaler
Statistikkbanken er tilgjengelig uten innlogging på statistikk.fhi.no/nokkel, og via helsedirektoratet.no/folkehelsestatistikk. Maskinell henting skjer gjennom FHI Statistikk Open API, uten oppgitt krav om registrering. Folkehelse- og oppvekstprofilene lastes ned fra helsedirektoratet.no. Henvendelser om folkehelsestatistikken går til Helsedirektoratets avdeling for folkehelsestatistikk.

## Plattform
**Fakta:** Statistikkbanken publiseres på FHI Statistikk, FHIs felles plattform for statistikk, der folkehelsestatistikken er én av flere kilder (statistikk-data.fhi.no).

**Ikke offentlig dokumentert:** Driftsmodell og infrastruktur for FHI Statistikk.

## Gjenbruk
Statistikken kan gjenbrukes gjennom nedlasting og gjennom FHI Statistikk Open API, som er felles for alle kilder på plattformen. En klient laget for folkehelsestatistikken kan derfor også brukes mot FHIs andre statistikkilder.

Ressursen er avhengig av FHI Statistikk som publiserings- og API-plattform.

### Vanlige kombinasjoner med andre produkter
- `HDIR-001` Helsedata.no, når analysen trenger helsedata på individnivå i tillegg til aggregert statistikk.
- `SSB-003` Statistikkbanken og PxWebApi, for befolknings- og samfunnsstatistikk utenfor folkehelseområdet.
- `FHI-003` Dødsårsaksregisteret, som også publiserer statistikk på FHI Statistikk.
- `SSB-002` KOSTRA, når folkehelsetall skal ses sammen med kommunale tjenestedata.

**Kildekode:** Ikke offentlig dokumentert. FHI har publisert dokumentasjon og kodeeksempler for API-et på GitHub, men ikke kildekoden til statistikkbanken eller plattformen.

**Lisens:** Ikke offentlig dokumentert.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Folkehelsestatistikken deles åpent i nettgrensesnitt, som nedlastbare filer og gjennom et åpent API, med metadata om kilde og feilkilder.

- **P5: Del og gjenbruk løsninger**
  Helsedirektoratet publiserer på FHIs felles statistikkplattform i stedet for å drive en egen løsning.

- **P1: Ta utgangspunkt i brukernes behov**
  Støttes delvis. Banken er tilrettelagt for kommunenes oversiktsarbeid, men overgangen fra de gamle bankene skjedde uten viderekobling av eksisterende lenker.

Spenningen ligger i ansvarsdelingen og vilkårene. Innhold og plattform har ulike forvaltere, og lisensvilkårene for dataene er ikke oppgitt. Det svekker forutsigbarheten for P4: dataene er åpent tilgjengelige, men den som vil gjenbruke dem i egne tjenester, finner ikke oppgitt på hvilke vilkår.

## Finansiering
**Ikke offentlig dokumentert:** Hvordan statistikkbanken og FHI Statistikk finansieres, og hvordan kostnadene er fordelt mellom Helsedirektoratet og FHI.

## Forvaltning/eier

| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Faglig ansvar og innhold | Helsedirektoratet, avdeling for folkehelsestatistikk | helsedirektoratet.no; kilden «Folkehelsestatistikk» i FHI Statistikk oppgir Helsedirektoratet som utgiver |
| Ansvar for folkehelse- og oppvekstprofilene | Helsedirektoratet, fra 1. januar 2024 | Helsedirektoratets årsrapport 2024 |
| Publiseringsplattform og API | Folkehelseinstituttet (FHI), gjennom FHI Statistikk | fhi.no, Åpen API og statistikk; statistikk-data.fhi.no |
| Driftsansvar | **Deduksjon:** FHI, som eier av plattformen. Ikke offentlig dokumentert | – |
| Budsjettansvar | Ikke offentlig dokumentert | – |
| Styringsmodell | Ikke offentlig dokumentert for samarbeidet mellom Helsedirektoratet og FHI | – |

FHIs tidligere side for folkehelseprofilene viderekobles til Helsedirektoratet.

## Lenke til dokumentasjon
- Statistikkbanken: https://statistikk.fhi.no/nokkel/
- Folkehelsestatistikk og profiler: https://www.helsedirektoratet.no/forebygging-diagnose-og-behandling/forebygging-og-levevaner/folkehelsestatistikk-og-profiler
- Bruk av statistikkbanken: https://www.helsedirektoratet.no/forebygging-diagnose-og-behandling/forebygging-og-levevaner/folkehelsestatistikk-og-profiler/bruk-av-statistikkbanken
- FHI Statistikk Open API: https://www.fhi.no/ta/statistikkalender_og_statistikk/apen-api-og-statistikk/
- API-dokumentasjon: https://github.com/folkehelseinstituttet/Fhi.Statistikk.OpenAPI

## Kildegrunnlag brukt i utfyllingen
Hentet 2026-10-23:
- Helsedirektoratet, Statistikkbanken Folkehelsestatistikk erstatter Kommunehelsa og Norgeshelsa: https://www.helsedirektoratet.no/forebygging-diagnose-og-behandling/forebygging-og-levevaner/folkehelsestatistikk-og-profiler/statistikkbanken-folkehelsestatistikk-erstatter-kommunehelsa-og-norgeshelsa
- Helsedirektoratet, Folkehelsestatistikk og profiler: https://www.helsedirektoratet.no/forebygging-diagnose-og-behandling/forebygging-og-levevaner/folkehelsestatistikk-og-profiler
- Helsedirektoratet, Bruk av statistikkbanken: https://www.helsedirektoratet.no/forebygging-diagnose-og-behandling/forebygging-og-levevaner/folkehelsestatistikk-og-profiler/bruk-av-statistikkbanken
- Helsedirektoratet, Årsrapport 2024, folkehelsearbeidet: https://www.helsedirektoratet.no/rapporter/helsedirektoratets-arsrapport-2024/arets-resultater-og-aktiviteter/folkehelsearbeidet-er-kunnskapsbasert-og-tverrsektorielt
- FHI, Åpen API og statistikk: https://www.fhi.no/ta/statistikkalender_og_statistikk/apen-api-og-statistikk/
- FHI Statistikk Open API, liste over kilder: https://statistikk-data.fhi.no/api/open/v1/Common/source
- GitHub, Fhi.Statistikk.OpenAPI: https://github.com/folkehelseinstituttet/Fhi.Statistikk.OpenAPI
- FHI, tidligere side for folkehelseprofilene (viderekoblet): https://www.fhi.no/he/folkehelse/folkehelseprofil/

Lokale kilder:
- `arkitektur/ressurser/operative-losninger-og-tjenester/31-Helsedata-no-produkt-canvas-v2-codex.md`

## Endringer fra forrige versjon
Dette er første publiserte versjon av ressursbeskrivelsen.
