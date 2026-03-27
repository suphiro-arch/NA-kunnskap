# Produkt-canvas: Skatteetatens delingstjenester

## Navn
Skatteetatens delingstjenester

## Ressurs ID
SKATT-002

## Status/Livsfase
**Produksjon** - etablert delingsflate for API-basert utlevering av data fra Skatteetaten til offentlige og private virksomheter.

**Fakta:** Skatteetaten beskriver deling av data som en viktig del av samfunnsoppdraget, og tilbyr kontrollerte delingstjenester for blant annet folkeregisteropplysninger, inntekt, skatt, avgift, eiendom og aksjonærdata. Tilgangen skjer gjennom API-er, avtaler, vilkår og etablerte samarbeidsmodeller.

## Modenhet
**Høy modenhet** - operativ delingsflate med tydelig forvaltningsmodell:
- Skatteetaten har egne sider for deling, kontaktpunkt, bruksvilkår og driftsstatus.
- Delingstjenestene brukes av både offentlige og private virksomheter.
- Produktområdet er organisert med både enkeltstående konsumenter og segmentsamarbeid.
- API-basert datadeling er tydelig etablert som hovedmønster.

**Deduksjon:** Modenheten er høy fordi dette ikke er et enkelt API, men en vedvarende nasjonal delingskapasitet med etablerte prosesser for tilgang, brukerstøtte, endringshåndtering og samarbeidsstyring.

## Kort beskrivelse
Skatteetatens delingstjenester er den samlede produktflaten for kontrollert viderebruk av data fra Skatteetaten. Produktet gjør det mulig for andre virksomheter å hente ut opplysninger gjennom API-er og tilhørende avtale- og tilgangsløp, i stedet for å basere seg på manuelle bestillinger eller punktvise filutvekslinger. Verdien ligger ikke bare i de enkelte datasettene, men i at Skatteetaten tilbyr en felles og styrt delingsmodell for datakonsumenter på tvers av sektorer og bransjer.

## Kapabiliteter
- **Datautveksling og integrasjon: Dele data med andre** er kjernefunksjonen ved at produktet er laget for å tilgjengeliggjøre data fra Skatteetaten til andre virksomheter gjennom API-er og kontrollerte tilgangsløp.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Skatteetatens sider for deling, bruksvilkår og kontakt-/samhandlingsmodell.

## Produktmål
**Primærkilder:** Skatteetatens sider `Bruke data fra Skatteetaten`, `Hvorfor vi deler data`, `Kontakt oss om deling av data` og `Bruksvilkår for delingstjenester om inntekt, skatt og restanser`.

Dokumenterte mål:
- Gjøre data fra Skatteetaten tilgjengelige for andre virksomheter.
- Forenkle, forbedre og effektivisere hverdagen for virksomheter og enkeltpersoner gjennom datadeling.
- Tilby API-basert tilgang til delingsdata gjennom avtalte og kontrollerte rammer.

Operative mål utledet fra de samme kildene:
- Redusere behovet for manuell innhenting og bilateral spesialtilpasning mellom etaten og hver enkelt datakonsument.
- Gi virksomheter med like behov en mer samordnet vei inn gjennom segmentsamarbeid.
- Skape en mer forutsigbar og styrbar modell for teknisk og juridisk datadeling fra Skatteetaten.

## Brukerbehov
- Offentlige virksomheter trenger autoritativ tilgang til data fra Skatteetaten i egne tjenester og saksprosesser.
- Private virksomheter trenger kontrollerte opplysninger når lovgrunnlag eller samtykke åpner for det.
- Integratører og systemleverandører trenger dokumenterte API-er, rettighetspakker og tydelig driftsinformasjon.
- Samarbeidsmiljøer i sektor eller bransje trenger en koordinert modell for tilgang og videre dialog med Skatteetaten.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter | Tilgang til skatte- og inntektsdata, folkeregisterdata eller andre relevante opplysninger | Saksbehandling, kontroll, automatisering og tjenesteutvikling | Viktigste tverrsektorielle brukergruppe |
| Private virksomheter med hjemmel eller samtykkegrunnlag | Opplysninger til lån, kreditt, pensjon, arbeidsgiverprosesser eller andre regulerte tjenester | Integrerte oppslag og automatisert saksstøtte | Bruk styres av vilkår og rettsgrunnlag |
| Segmentansvarlige og samarbeidsgrupper | Samordnet tilgang og koordinering mot Skatteetaten | Finans, kommune, helse, kraft og andre delingsmiljøer | Viktig del av produktets samarbeidsmodell |
| Systemleverandører og integratører | Dokumentasjon, API-er og støtte i innføringsløpet | Utvikling og drift av sluttbrukersystemer | Teknisk kanal inn til produktet |
| Skatteetaten som forvalter | Styring, vilkår, drift og oppfølging | Delingsforvaltning, kontaktpunkt og endringshåndtering | Operativ forvalter av hele produktområdet |

## Hovedfunksjoner
### Primære funksjoner
**Kontrollert tilgjengeliggjøring av data gjennom API-er.** Skatteetatens delingstjenester tilbyr maskinell tilgang til data for virksomheter som oppfyller vilkår og har rettslig grunnlag. Produktet er derfor først og fremst en nasjonal delingsflate, ikke et enkelt datasett.

**Felles tilgangs- og samarbeidsmodell.** Produktet omfatter ikke bare API-er, men også etablerte løp for kontakt, avtaler, bruksvilkår, driftsstatus og oppfølging. Dette gjør delingstjenestene til en helhetlig produktflate for viderebruk av data.

**Segmentsamarbeid for virksomheter med like behov.** Skatteetaten beskriver egne segmenter og segmentansvarlige for grupper av virksomheter med felles behov. Det gir en mer skalerbar modell for samhandling enn individuell oppfølging av hver enkelt konsument.

**Teknisk og operativ støtte til viderebruk.** Produktet omfatter dokumentasjon, rettighetspakker, vilkår og støttefunksjoner som gjør det mulig å ta tjenestene i bruk og forvalte integrasjonene over tid.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Den samlede delingsflaten for data fra Skatteetaten | Selve fagsystemene og grunnregistrene som produserer dataene |
| API-basert tilgang til utvalgte datatyper | Lokal saksbehandling hos datakonsumentene |
| Avtaleløp, bruksvilkår, kontaktpunkt og støttefunksjoner | Hver enkelt virksomhets interne autorisasjons- og prosesslogikk |
| Segmentsamarbeid og samordnet dialog med konsumentgrupper | Full erstatning for sektorvise integrasjonsløsninger hos brukerne |
| Driftsstatus og endringskommunikasjon for delingstjenestene | Alle tjenester Skatteetaten tilbyr utenfor datadeling |

## Veikart over kommende funksjonalitet
**Fakta fra Skatteetatens kilder (kontrollert 2026-03-27):**
- Skatteetaten publiserer løpende driftsinformasjon, oppdaterte bruksvilkår og kontaktinformasjon for delingstjenestene.
- Bruksvilkårene for inntekt, skatt og restanser er oppdatert med virkning fra 1. september 2024.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et samlet, tidsfestet veikart for hele produktområdet er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til å dreie seg om videre standardisering av API-tilgang, bedre operativ støtte og samordning på tvers av virksomhetssegmenter.

## Forretningsverdi/Verdiforslag
### For offentlig sektor
- Gjør det mulig å bruke data fra Skatteetaten direkte i digitale tjenester og saksprosesser.
- Reduserer behovet for manuelle bestillinger og lokale spesialløsninger.
- Støtter mer sammenhengende og datadrevne tjenester på tvers av etater.

### For private virksomheter
- Gjør det mulig å bygge regulerte tjenester på oppdaterte data fra Skatteetaten når rettsgrunnlaget er på plass.
- Skaper større forutsigbarhet gjennom standardiserte tilgangs- og samarbeidsløp.

### For samfunnet
- Bidrar til bedre gjenbruk av offentlige data.
- Gjør at data fra Skatteetaten kan skape verdi i flere tjenester enn etaten selv leverer direkte.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk og personvern | Feil tilgang eller for bred bruk av delte opplysninger kan få store konsekvenser | Tydelige vilkår, hjemmelsvurdering og tilgangsstyring |
| Teknisk | Endringer i API-er eller driftsforstyrrelser kan ramme mange konsumenter samtidig | God endringsforvaltning, dokumentasjon og statusside |
| Samhandlingsmodell | Uklare roller mellom Skatteetaten, segmentansvarlige og konsumenter kan gi treg innføring | Klare kontaktpunkter og standardiserte samarbeidsløp |
| Avhengighet | Mange tjenester kan bli avhengige av dataflyt fra Skatteetaten | Robust drift og tydelig prioritering av kritiske delingsløp |
| Forståelse og bruk | Konsumenter kan undervurdere juridiske og faglige vilkår for gjenbruk | Tydelig dokumentasjon, bruksvilkår og støttefunksjoner |

## Kanaler
- Bruke data fra Skatteetaten: https://www.skatteetaten.no/deling/
- Hvorfor vi deler data: https://www.skatteetaten.no/deling/hvorfor-vi-deler-data/
- Kontakt oss om deling av data: https://www.skatteetaten.no/deling/kontakt/
- Bruksvilkår for delingstjenester om inntekt, skatt og restanser: https://www.skatteetaten.no/deling/bruksvilkar-for-delingstjenester/

## Plattform
Skatteetatens delingstjenester er en felles delings- og integrasjonsflate for data fra Skatteetaten.

**Fakta:** Kildene beskriver produktområdet som API-basert datadeling med tilhørende avtalemodell, kontaktløp, driftsvarsling og teknisk dokumentasjon.

**Ikke offentlig dokumentert i brukte kilder:** Full intern plattformarkitektur, detaljer om underliggende systemlandskap og samlet teknologistakk.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er laget for viderebruk av data i andre virksomheters prosesser og tjenester.
- Det er særlig relevant når behovet er kontrollert og autoritativ datadeling fra Skatteetaten.
- Det er mindre relevant som selvstendig sluttbrukertjeneste, siden hovedverdien ligger i integrasjon og viderebruk.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres direkte ved at produktet er bygget for å dele data fra Skatteetaten med andre.
- **P5: Del og gjenbruk løsninger** styrkes ved at datadeling skjer gjennom en felles modell framfor mange bilaterale opplegg.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi produktet kobler Skatteetatens data inn i andre virksomheters tjenester.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi delingen må være styrt, sporbar og basert på tydelige vilkår.

## Finansiering
- **Fakta:** Kildene beskriver vilkår, avtaler og segmentmodeller, men gir ikke en samlet offentlig finansieringsmodell for hele produktet i denne arbeidsøkten.
- **Deduksjon:** Produktet finansieres som del av Skatteetatens delings- og forvaltningsoppdrag, kombinert med innførings- og integrasjonskostnader hos konsumentene.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Skatteetaten | Delingssidene og kontaktflatene peker til Skatteetaten som ansvarlig virksomhet |
| Driftsansvar | Skatteetaten | Produktområdet har egen driftsstatus og operativ oppfølging hos etaten |
| Budsjett- og forvaltningsansvar | Skatteetaten | Deling beskrives som del av samfunnsoppdraget |
| Styringsmodell | Skatteetaten, med samhandling mot segmentansvarlige og konsumentmiljøer | Delingssidene og kontaktmodellen |

## Lenke til dokumentasjon
- https://www.skatteetaten.no/deling/
- https://www.skatteetaten.no/deling/hvorfor-vi-deler-data/
- https://www.skatteetaten.no/deling/kontakt/
- https://www.skatteetaten.no/deling/bruksvilkar-for-delingstjenester/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.skatteetaten.no/deling/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/deling/hvorfor-vi-deler-data/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/deling/kontakt/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/deling/bruksvilkar-for-delingstjenester/ (kontrollert 2026-03-27)
