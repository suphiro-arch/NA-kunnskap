# Modenhetsanalyse: Kapabilitetsmodenhet for nasjonale fellesløsninger

**Dato:** 2026-05-05  
**Utarbeidet av:** KI-assistert analyse (GitHub Copilot / MCP-server NA-kunnskap)  
**Grunnlag:** Kapabilitetsmodellen v.2026-02-27, SSB IKT-statistikk 2025, Digdirs samarbeidsportal

---

## Formål

Analysen kartlegger hvilke kapabiliteter i Nasjonal arkitektur for samhandling som har lav modenhet og adopsjon i norsk offentlig sektor, basert på tilgjengelige SSB-indikatorer og Digdirs statistikk for fellesløsningene. Analysen er ikke en fullstendig modenhetsmodell, men en første datadrevet prioritering.

> **Tolkningsregel:** Kapabiliteter uten delkapabiliteter arver seg selv som operativ enhet. Dette gjelder **Juridisk samhandling** og **Veiledning**.

---

## Datagrunnlag

### SSB: Hindringer for utvikling av digitale tjenester, 2025
Kilde: SSB tabell 10611 ([IktBruks12c](https://www.ssb.no/statbank/table/10611)) – statlige virksomheter, «er i stor eller svært stor grad en hindring».

| Hindring | % stor/svært stor hindring | Relatert kapabilitet |
|---|---|---|
| Vanskelig å frigjøre ressurser til utvikling | **62 %** | Strategisk styring → Finansiering |
| IKT-utgifter høyere enn forventet | **54 %** | Strategisk styring → Finansiering |
| Avhengig av utvikling hos andre aktører | **54 %** | Samarbeid → Tjenesteforvaltning |
| Manglende kompetanse i virksomheten | **40 %** | Tjenesteutvikling (bredt) |
| Lovgivning og regler mangler tilpasning | **37 %** | Juridisk samhandling *(arver seg selv)* |
| Mangel på felles offentlige løsninger og infrastruktur | **37 %** | Sluttbrukertjenester → Sammenhengende tjenester |
| Vanskelig å integrere eksisterende IT- og fagsystemer | **32 %** | Datautveksling og integrasjon → Bruke data fra andre |
| Mangel på felles standarder for datautveksling | **24 %** | Datautveksling og integrasjon → Dele data med andre |
| Mangel på politiske føringer | **10 %** | Strategisk styring → Arkitekturstyring |
| Mangel på engasjement hos ledelsen | **6 %** | Strategisk styring → Samordning |

### SSB: Bruk av nettskytjenester i statlige virksomheter, 2019–2024
Kilde: SSB tabell 10609 ([IktBruks05c](https://www.ssb.no/statbank/table/10609)) – andel som bruker minst én nettskytjeneste.

| År | Andel (%) |
|---|---|
| 2019 | 84,4 |
| 2020 | 85,8 |
| 2021 | 92,2 |
| 2022 | 96,2 |
| 2023 | 95,2 |
| 2024 | **96,7** |

Tolkning: Nettsky-adopsjon er høy og stabil. Støtter kapabiliteten **Tjenesteutvikling → Utviklings- og kjøretidsmiljø** som moden teknologisk infrastruktur.

### SSB: IKT-outsourcing statlige virksomheter, 2025
Kilde: SSB tabell 12031 ([IktBruks26](https://www.ssb.no/statbank/table/12031)).

Drift av enhetens servere er i stor grad outsourcet til eksterne. Interne ressurser dominerer på strategiutvikling og prosjektledelse for digitalisering, men en betydelig andel (ca. 25 %) fordeler arbeidet likt. Dette indikerer at kapabiliteten **Strategisk styring → Arkitekturstyring** er internt forankret, men ujevnt distribuert.

### Digdirs statistikk for fellesløsninger (kvalitativ, 2025)
Kilde: [Samarbeidsportalen – Statistikk](https://samarbeid.digdir.no/statistikk/statistikk/15) og [Årsrapport 2025](https://samarbeid.digdir.no/felleslosninger/arsrapport-2025/3523).

- **ID-porten:** Bredt tatt i bruk, stabil trafikk, høy oppetid (krav: 99,90 %). Brukes av de fleste statlige virksomheter. Representasjon og fullmakter er under videre utvikling (produkteier-sitat 2025). Se [ID-porten statistikk](https://samarbeid.digdir.no/id-porten/statistikk-id-porten/3419) og [ID-porten 2025](https://samarbeid.digdir.no/id-porten/id-porten-2025/3524).
- **Maskinporten:** Voksende antall aktive konsumenter og API-tilbydere. Fortsatt i en tidlig adopsjons- og vekstfase. Se [Maskinporten statistikk](https://samarbeid.digdir.no/maskinporten/statistikk-maskinporten/3423) og [Maskinporten 2025](https://samarbeid.digdir.no/maskinporten/maskinporten-2025/3526).
- **Digital postkasse:** Stabil infrastruktur, men penetrasjonen blant innbyggere er ikke universell. Se [statistikk digital postkasse](https://samarbeid.digdir.no/digital-postkasse/statistikk-digital-postkasse-til-innbyggar/3424).
- **eFormidling/eInnsyn:** Bredt tatt i bruk i statlig sektor, men innholdsog kvalitets-aspekter varierer. Se [årsrapport eFormidling 2025](https://samarbeid.digdir.no/eformidling/eformidling-2025/3513) og [eInnsyn 2025](https://samarbeid.digdir.no/einnsyn/einnsyn-2025/3518).
- **Ansattporten:** Relativt ny, fortsatt i tidlig adopsjonsfase. Se [Ansattporten statistikk](https://samarbeid.digdir.no/ansattporten/statistikk-ansattporten/3430).

### Eurostat: E-forvaltning hos individer, 2023–2025
Kilde: Eurostat tabell `isoc_ciegi_ac` – individers bruk av offentlige nettsteder/apper, andel av alle individer (16–74 år). Data hentet via Eurostat Statistics API (`get_eurostat_statistics`, 2026-05-05).

| Indikator | NO 2023 | EU27 2023 | NO 2024 | EU27 2024 | NO 2025 | EU27 2025 |
|---|---|---|---|---|---|---|
| Bruker offentlige nettsider/apper (ett eller flere formål) | **97,7 %** | 69,3 % | **98,5 %** | 70,0 % | **97,8 %** | 71,9 % |
| Generell samhandling med offentlige myndigheter | **91,7 %** | 54,3 % | **90,4 %** | 56,2 % | **90,8 %** | 57,6 % |
| Tilgang til personlig informasjon hos offentlig myndighet | **86,2 %** | 39,1 % | **82,9 %** | 40,0 % | **83,8 %** | 41,3 % |
| Mottar offisiell kommunikasjon/dokumenter digitalt | 57,6 % | 36,6 % | **91,4 %** | 36,2 % | **90,3 %** | 36,6 % |
| Leverer selvangivelse digitalt | — | — | **91,7 %** | 37,2 % | **91,6 %** | 38,2 % |
| Henter informasjon om tjenester, rettigheter, åpningstider | **72,6 %** | 41,6 % | **73,5 %** | 44,1 % | **74,2 %** | 44,2 % |
| Ber om ytelser eller trygderettigheter digitalt | 34,2 % | 17,5 % | **36,1 %** | 17,6 % | **36,4 %** | 18,1 % |
| Tilgang til offentlige databaser eller registre | **38,3 %** | 19,0 % | **41,6 %** | 19,9 % | **43,9 %** | 20,7 % |
| Laster ned/skriver ut skjemaer | 45,2 % | 39,9 % | 43,5 % | 38,1 % | 45,2 % | 36,8 % |
| Timebestilling eller reservasjon | 33,3 % | 37,4 % | 34,7 % | 34,9 % | 39,3 % | 38,1 % |
| Brukte nettsider, men fikk ikke det de trengte¹ | **8,1 %** | 38,0 % | **8,8 %** | 37,5 % | **8,1 %** | 36,6 % |

¹ Lav prosentandel er positivt — viser at brukerne finner det de leter etter.

Tolkning: Norge har nær universell bruk av offentlige digitale tjenester (98,5 % i 2024), og kun 8 % av brukerne forlater uten å ha funnet det de trengte, mot 38 % i EU27. Mottak av offisielle dokumenter digitalt doblet seg fra 57,6 % (2023) til 91,4 % (2024), trolig drevet av sterk vekst i digital post. EU-dataene bekrefter at **Tillit → Autentisering**, **Datautveksling → Meldingsformidling** og **Sluttbrukertjenester → Sammenhengende tjenester** fungerer godt på innbyggerrettede flater, selv der SSB-dataene viser svakheter på produksjons- og infrastruktursiden.

---

## Vurdering per kapabilitet

> **Skala:** 🔴 Lav modenhet/adopsjon — 🟡 Middels — 🟢 Høy modenhet/adopsjon  
> Vurderingen er basert på hindringsindikatorer (høy hindringsprosent = lav modenhet) og kjent adopsjon av fellesløsninger.

### Strategisk styring
| Delkapabilitet | Modenhet | Begrunnelse |
|---|---|---|
| Finansiering | 🔴 Lav | 62 % sliter med å frigjøre ressurser; 54 % opplever uventet høye kostnader. To uavhengige SSB-indikatorer peker mot samme problem. |
| Arkitekturstyring | 🟡 Middels | 10 % opplever mangel på politiske føringer som stor hindring – relativt lavt, men arkitekturforankring er ujevnt fordelt på tvers av virksomheter. |
| Samordning | 🟡 Middels | 6 % opplever ledelsesforankring som hindring, men 54 % er «avhengig av andre aktørers utvikling» – indikerer svak tverrgående samordning i praksis. |

### Samarbeid
| Delkapabilitet | Modenhet | Begrunnelse |
|---|---|---|
| Organisatorisk samhandling | 🟡 Middels | Fellesarenaer finnes (Digitaliseringsrådet, sektornettverk), men tverrsektoriell prosesskoordinering er lite formalisert. |
| Samarbeidsarenaer og nettverk | 🟡 Middels | Strukturer er på plass (f.eks. NIFS, Faglig arena for informasjonsforvaltning), men bruken er ujevn. |
| Tjenesteforvaltning | 🔴 Lav | 54 % oppgir avhengighet av andre aktørers utvikling som stor hindring. Mangler formelle styringsmodeller for tverrgående tjenester. |

### Sluttbrukertjenester
| Delkapabilitet | Modenhet | Begrunnelse |
|---|---|---|
| Sammenhengende tjenester | 🟡 Middels | 37 % opplever mangel på felles infrastruktur som hindring (SSB) — dette gjelder produksjonssiden. Eurostat viser at sluttbrukersiden er sterk: 91 % har generell samhandling med offentlige myndigheter (+33pp over EU27), og 36 % ber om ytelser digitalt (EU27: 18 %). Infrastruktur for livshendelsesorienterte kjeder mangler fortsatt, men eksisterende tjenester fungerer godt i praksis. |
| Tjenestekjeder | 🔴 Lav | Ingen nasjonale standardiserte mekanismer for dynamisk tjenestekomposisjon. Avhengig av punkt-til-punkt integrasjoner. Høy generell samhandlingsrate (NO 91 % vs EU27 57 %) viser at kjeder fungerer i praksis, men uten formell arkitektur. |
| Proaktive tjenester | 🔴 Lav | Svært tidlig fase. Krever moden datadeling og hendelsesdrevet arkitektur som begge er i lav adopsjon. |

### Datautveksling og integrasjon
| Delkapabilitet | Modenhet | Begrunnelse |
|---|---|---|
| Dele data med andre | 🟡 Middels | 24 % opplever manglende standarder som hindring. Maskinporten vokser, men utbredelsen er fortsatt begrenset sammenlignet med potensialet. |
| Bruke data fra andre | 🔴 Lav | 32 % sliter med systemintegrasjon. Fragmentert fagsystemlandskap gjør gjenbruk av andres data krevende. |
| Meldingsformidling | 🟢 Høy | eFormidling er bredt tatt i bruk i statlig sektor. Eurostat: mottak av offisielle dokumenter digitalt økte fra 57,6 % (2023) til 91,4 % (2024) — +55pp over EU27. En av Norges sterkeste posisjoner i europeisk sammenligning. |
| Hendelsesdrevet | 🔴 Lav | Svært begrenset adopsjon av hendelsesorienterte mønstre i offentlig sektor per i dag. |

### Tillit
| Delkapabilitet | Modenhet | Begrunnelse |
|---|---|---|
| Autentisering | 🟢 Høy | ID-porten er bredt og stabilt i bruk. eID-adopsjon er høy. Eurostat bekrefter: 84 % av norske individer har tilgang til personlig informasjon hos offentlige myndigheter (EU27: 41 %). |
| Tilgangskontroll | 🟡 Middels | Teknisk er dette på plass via ID-porten/Maskinporten, men implementeringspraksis varierer. Eurostat: kun 8 % av brukerne mislykkes med å finne det de trenger (EU27: 38 %), som indikerer at tilgangskontroll fungerer i praksis. |
| Tilgangsstyring | 🟡 Middels | Maskinporten gir maskin-til-maskin tilgangsstyring, men er fortsatt i vekstfase. |
| Representasjon | 🔴 Lav | Aktivt under utvikling (Altinn Autorisasjon, fullmaktsfunksjonalitet). Produkteier ID-porten identifiserer dette som prioritert utviklingsområde for 2025+. |
| Sporbarhet og innsyn | 🟡 Middels | eInnsyn dekker journalinnsyn, men helhetlig logging på tvers av tjenestekjeder mangler. |
| Signering | 🟡 Middels | eSignering er tilgjengelig, men adopsjon er begrenset til spesifikke brukssituasjoner. |
| Samtykke | 🔴 Lav | 37 % opplever lovgivning som hindring – dette rammer spesielt samtykkebasert deling, som krever juridisk klarhet. Fellesløsning for samtykke er ikke etablert. |
| Identifisering | 🟢 Høy | ID-porten og Enhetsregisteret (BRREG) gir sterk identifiseringsevne for både personer og virksomheter. |

### Datadrevet
| Delkapabilitet | Modenhet | Begrunnelse |
|---|---|---|
| Dataanalyse | 🟡 Middels | Analytisk kapasitet varierer sterkt mellom store og små virksomheter. |
| Sammenstilling av data | 🔴 Lav | 32 % sliter med systemintegrasjon; grunndata er ikke tilgjengelig som strukturerte APIer på tvers. |
| Visualisering | 🟡 Middels | Designsystemet tilbyr komponenter, men ingen nasjonale standarder for datavisualisering. |

### Informasjonssikkerhet
| Delkapabilitet | Modenhet | Begrunnelse |
|---|---|---|
| Styringssystem | 🟡 Middels | NIFS-nettverket og NSMs veiledning finnes, men implementering er ujevn. |
| Sikring av informasjonsflyt og datautveksling | 🟡 Middels | TLS og Maskinporten adresserer dette teknisk, men praksis for ende-til-ende sikkerhet på tvers varierer. |

### Tjenesteutvikling
| Delkapabilitet | Modenhet | Begrunnelse |
|---|---|---|
| Utviklings- og kjøretidsmiljø | 🟢 Høy | 96,7 % av statlige virksomheter bruker nettskytjenester (SSB 2024). NAIS (NAV), Altinn Studio og liknende plattformer etablert. |
| Integrerbare tjenester | 🟡 Middels | API-katalogen finnes (data.norge.no), men API-kvalitet og -standardisering er ujevn. |
| Gjenbrukbare tjenester | 🔴 Lav | Designsystemet er et godt eksempel, men gjenbruk på tvers av sektor er begrenset. 40 % mangler kompetanse til å realisere gjenbruk. |
| Tjenestedesign | 🟡 Middels | Veiledere og Designsystemet er på plass, men kapasitet til brukerorientert tjenestedesign er ujevnt fordelt. |

### Informasjonsforvaltning
| Delkapabilitet | Modenhet | Begrunnelse |
|---|---|---|
| Informasjonsarkitektur | 🟡 Middels | Felles datakatalog og begrepskatalog finnes, men dekningsgraden er lav. |
| Oversikt over informasjonsmodeller | 🔴 Lav | Lite koordinert nasjonalt. Informasjonsmodeller eksisterer i siloer. |
| Oversikt over datasett | 🟡 Middels | data.norge.no gir oversikt, men registreringen er frivillig og ufullstendig. Eurostat: 44 % av norske individer bruker offentlige databaser/registre (EU27: 21 %) — brukertilgangen er god, men registerkvaliteten varierer. |
| Oversikt over hendelser | 🔴 Lav | Ingen nasjonal oversikt. Hendelsesorientert integrasjon er tidlig fase. |
| Oversikt over API | 🟡 Middels | API-katalogen på data.norge.no er etablert, men mange APIer er ikke registrert. |
| Oversikt over begreper | 🟡 Middels | Begrepskatalog finnes (data.norge.no/concepts), men dekningen er fragmentert og virksomhetsavhengig. |
| Oversikt over tjenester | 🔴 Lav | Norge.no gir en viss oversikt, men ingen maskinlesbar, komplett tjenestekatalog. |
| Datastyring | 🔴 Lav | Felles rammeverk for datastyring på nasjonalt nivå er ikke operativt. |

### Standardisering
| Delkapabilitet | Modenhet | Begrunnelse |
|---|---|---|
| EU-standarder | 🟡 Middels | eIDAS, EHDS, Data Governance Act følges, men norsk implementering har forsinkelser. |
| Forvaltningsstandarder | 🟡 Middels | Forskrift om IT-standarder finnes ([Lovdata](https://lovdata.no/forskrift/2013-04-05-959)), men etterlevelse er ujevn – under evaluering av Digdir. |

### Juridisk samhandling *(ingen delkapabiliteter – arver seg selv)*
| Kapabilitet | Modenhet | Begrunnelse |
|---|---|---|
| Juridisk samhandling | 🔴 Lav | 37 % opplever lovgivning og regler som manglende tilpasning som stor hindring. Digitaliseringsvennlig regelverk er et politisk mål, men langt fra operativt realisert på tvers av sektorer. |

### Veiledning *(ingen delkapabiliteter – arver seg selv)*
| Kapabilitet | Modenhet | Begrunnelse |
|---|---|---|
| Veiledning | 🟡 Middels | Prosjektveiviseren, Digdirs veiledere og Designsystemet er tilgjengelige, men bruken er ikke systematisk og kompetansen til å anvende dem er ujevnt fordelt (40 % oppgir manglende kompetanse). |

### Datakilder
| Delkapabilitet | Modenhet | Begrunnelse |
|---|---|---|
| Grunndata | 🟡 Middels | Folkeregisteret, Enhetsregisteret og Matrikkelen er autoritative, men tilgang via API er varierende. |
| Sanntidsdata | 🔴 Lav | Svært begrenset nasjonal kapasitet. Hendelsesdrevne mønstre er tidlig fase. |
| Åpne data | 🟡 Middels | data.norge.no og SSB tilbyr åpne data, men registrering og kvalitet er ujevn. |
| Testdata | 🔴 Lav | Syntetisk Folkeregister finnes, men helhetlig nasjonal testdata-infrastruktur mangler. |
| Ustrukturerte data | 🔴 Lav | Ingen nasjonal kapabilitet etablert for forvaltning av ustrukturerte data. |

---

## Oppsummering: Kapabiliteter med lav modenhet/adopsjon

Følgende kapabiliteter vurderes som **lav modenhet** basert på datagrunnlaget:

| Prioritet | Kapabilitet | Kjerneindikator |
|---|---|---|
| 🔴 1 | Strategisk styring → **Finansiering** | 62 % ressurshindring, 54 % kostnadshindring (SSB 2025) |
| 🔴 2 | Samarbeid → **Tjenesteforvaltning** | 54 % avhengig av andre aktørers utvikling (SSB 2025) |
| 🔴 3 | **Juridisk samhandling** | 37 % lovgivningshindring; digitaliseringsvennlig regelverk ikke operativt (SSB 2025) |
| 🟡 4 | Sluttbrukertjenester → **Sammenhengende tjenester** | Svak produksjonside (37 % SSB), men sterk brukerside (NO 91 % samhandling, +33pp over EU27) |
| 🔴 5 | Datautveksling → **Bruke data fra andre** | 32 % systemintegrasjonshindring (SSB 2025) |
| 🔴 6 | Tillit → **Representasjon + Samtykke** | Under utvikling; juridisk og teknisk umodent |
| 🔴 7 | Informasjonsforvaltning → **Datastyring + Oversikt over hendelser + Tjenester** | Ingen nasjonale løsninger operativt |
| 🔴 8 | Datakilder → **Sanntidsdata + Testdata + Ustrukturerte data** | Infrastruktur mangler |

---

## EU-sammenligning: Norsk styrke sett utenfra

Eurostat-dataene (2024–2025) gir et komplementært bilde til SSB-hindringene. Der SSB dokumenterer svakheter internt (finansiering, integrasjon, juridisk), viser Eurostat at Norge allerede leverer langt over EU-snittet på de fleste innbyggerrettede e-forvaltningsindikatorer.

| Kapabilitet | Vurdering internt (SSB) | Posisjon mot EU27 (Eurostat) | Tolkning |
|---|---|---|---|
| Tillit → Autentisering | 🟢 Høy | +43 pp på personlig informasjonstilgang; 98,5 % bruker offentlige tjenester | Sterk på begge akser |
| Datautveksling → Meldingsformidling | 🟢 Høy | +55 pp på mottak av offisielle dokumenter; sterk vekst 2023→2024 | Sterk på begge akser |
| Sluttbrukertjenester → Sammenhengende tjenester | 🟡 Middels | +33 pp på generell samhandling; +18 pp på ytelsesforespørsler | Svak produksjonside, sterk brukerside — oppgradert til 🟡 |
| Tillit → Tilgangskontroll | 🟡 Middels | Kun 8 % av brukerne mislykkes (EU27: 38 %) | Teknisk fungerer, praksis varierer |
| Informasjonsforvaltning → Datasett | 🟡 Middels | +23 pp på databasetilgang | Brukertilgang god, register-kvalitet ujevn |
| Tillit → Representasjon/Samtykke | 🔴 Lav | Ikke direkte målbart i Eurostat | Intern svakhet, usikkert EU-bilde |
| Strategisk styring → Finansiering | 🔴 Lav | Ikke direkte målbart i Eurostat | Intern systemsvakhet |
| Datautveksling → Bruke data fra andre | 🔴 Lav | +22 pp på registertilgang fra brukersiden | Infrastruktur svak, men brukertilgang god |

Dette mønsteret – god sluttbrukerflate, svak bakside – er karakteristisk for norsk digital forvaltning og bør reflekteres i prioritering: tiltak som styrker baksiden (datastyring, integrasjon, juridisk ramme) vil utnytte den gode posisjonen på sluttbrukersiden.

---

## Begrensninger og forbehold

- SSB-dataene måler **statlige virksomheter**, ikke kommuner eller fylkeskommuner direkte.
- Hindringsprosenter er en **proxy for modenhet**, ikke et direkte mål på kapabilitetsrealisering.
- Digdirs statistikk er grafisk publisert og ikke maskinlesbar; eksakte tall for antall virksomheter/brukere er ikke hentet inn i denne analysen.
- Kapabilitetsvurderingene er basert på tilgjengelige åpne data per 2025–2026. En fullstendig modenhetsvurdering ville kreve strukturerte intervjuer og egenvurderinger fra virksomheter.

---

## Kilder

| Kilde | Lenke |
|---|---|
| SSB tabell 10611 – Hindringer for digitale tjenester, statlige virksomheter | https://www.ssb.no/statbank/table/10611 |
| SSB tabell 10609 – Nettskytjenester, statlige virksomheter | https://www.ssb.no/statbank/table/10609 |
| SSB tabell 12031 – Ivaretakelse av IKT-funksjoner | https://www.ssb.no/statbank/table/12031 |
| Digdir – Statistikk for fellesløsningene | https://samarbeid.digdir.no/statistikk/statistikk/15 |
| Digdir – Årsrapport 2025 | https://samarbeid.digdir.no/felleslosninger/arsrapport-2025/3523 |
| Digdir – ID-porten statistikk | https://samarbeid.digdir.no/id-porten/statistikk-id-porten/3419 |
| Digdir – ID-porten 2025 | https://samarbeid.digdir.no/id-porten/id-porten-2025/3524 |
| Digdir – Maskinporten statistikk | https://samarbeid.digdir.no/maskinporten/statistikk-maskinporten/3423 |
| Digdir – Maskinporten 2025 | https://samarbeid.digdir.no/maskinporten/maskinporten-2025/3526 |
| Digdir – Statistikk digital postkasse | https://samarbeid.digdir.no/digital-postkasse/statistikk-digital-postkasse-til-innbyggar/3424 |
| Digdir – eFormidling 2025 | https://samarbeid.digdir.no/eformidling/eformidling-2025/3513 |
| Digdir – eInnsyn 2025 | https://samarbeid.digdir.no/einnsyn/einnsyn-2025/3518 |
| Digdir – Ansattporten statistikk | https://samarbeid.digdir.no/ansattporten/statistikk-ansattporten/3430 |
| Digdir – Nasjonale fellesløsninger (oversikt) | https://www.digdir.no/felleslosninger/nasjonale-felleslosninger/750 |
| Digdir – Digitaliseringsrundskrivet | https://www.regjeringen.no/no/dokumenter/digitaliseringsrundskrivet/id3103320/ |
| Digdir – Forskrift om IT-standarder (Lovdata) | https://lovdata.no/forskrift/2013-04-05-959 |
| Digdir – Evaluering av IT-standardforskriften | https://www.digdir.no/standarder/evaluering-av-forskrift-om-it-standarder-i-offentlig-forvaltning/3365 |
| Kapabilitetsmodell NA-kunnskap | /arkitektur/kapabiliteter/capabilities.yaml |
| SSB API | https://data.ssb.no/api/v0/no/table/ |
| Felles datakatalog (data.norge.no) | https://data.norge.no/ |
| Eurostat – E-forvaltning individer (isoc_ciegi_ac) | https://ec.europa.eu/eurostat/databrowser/product/view/ISOC_CIEGI_AC |
| Eurostat Statistics API | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/ |
