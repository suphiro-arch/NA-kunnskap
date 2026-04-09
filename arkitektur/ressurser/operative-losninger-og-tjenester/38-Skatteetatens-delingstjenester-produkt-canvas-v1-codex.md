# Produkt-canvas: Skatteetatens delingstjenester

## Navn
Skatteetatens delingstjenester

## Ressurs ID
SKATT-002

## Status/Livsfase
**Produksjon** - etablert delingsflate for API-basert utlevering av data fra Skatteetaten til offentlige og private virksomheter.

**Fakta:** Skatteetaten beskriver deling av data som en viktig del av samfunnsoppdraget, og tilbyr kontrollerte delingstjenester for blant annet folkeregisteropplysninger, inntekt, skatt, avgift, eiendom og aksjonÃ¦rdata. Tilgangen skjer gjennom API-er, avtaler, vilkÃ¥r og etablerte samarbeidsmodeller.

## Modenhet
**HÃ¸y modenhet** - operativ delingsflate med tydelig forvaltningsmodell:
- Skatteetaten har egne sider for deling, kontaktpunkt, bruksvilkÃ¥r og driftsstatus.
- Delingstjenestene brukes av bÃ¥de offentlige og private virksomheter.
- ProduktomrÃ¥det er organisert med bÃ¥de enkeltstÃ¥ende konsumenter og segmentsamarbeid.
- API-basert datadeling er tydelig etablert som hovedmÃ¸nster.

**Deduksjon:** Modenheten er hÃ¸y fordi dette ikke er et enkelt API, men en vedvarende nasjonal delingskapasitet med etablerte prosesser for tilgang, brukerstÃ¸tte, endringshÃ¥ndtering og samarbeidsstyring.

## Kort beskrivelse
Skatteetatens delingstjenester er den samlede produktflaten for kontrollert viderebruk av data fra Skatteetaten. Produktet gjÃ¸r det mulig for andre virksomheter Ã¥ hente ut opplysninger gjennom API-er og tilhÃ¸rende avtale- og tilgangslÃ¸p, i stedet for Ã¥ basere seg pÃ¥ manuelle bestillinger eller punktvise filutvekslinger. Verdien ligger ikke bare i de enkelte datasettene, men i at Skatteetaten tilbyr en felles og styrt delingsmodell for datakonsumenter pÃ¥ tvers av sektorer og bransjer.

## Kapabiliteter
- **Datautveksling og integrasjon: Dele data med andre** er kjernefunksjonen ved at produktet er laget for Ã¥ tilgjengeliggjÃ¸re data fra Skatteetaten til andre virksomheter gjennom API-er og kontrollerte tilgangslÃ¸p.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Skatteetatens sider for deling, bruksvilkÃ¥r og kontakt-/samhandlingsmodell.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Skatteetatens sider `Bruke data fra Skatteetaten`, `Hvorfor vi deler data`, `Kontakt oss om deling av data` og `BruksvilkÃ¥r for delingstjenester om inntekt, skatt og restanser`.

Dokumenterte mÃ¥l:
- GjÃ¸re data fra Skatteetaten tilgjengelige for andre virksomheter.
- Forenkle, forbedre og effektivisere hverdagen for virksomheter og enkeltpersoner gjennom datadeling.
- Tilby API-basert tilgang til delingsdata gjennom avtalte og kontrollerte rammer.

Operative mÃ¥l utledet fra de samme kildene:
- Redusere behovet for manuell innhenting og bilateral spesialtilpasning mellom etaten og hver enkelt datakonsument.
- Gi virksomheter med like behov en mer samordnet vei inn gjennom segmentsamarbeid.
- Skape en mer forutsigbar og styrbar modell for teknisk og juridisk datadeling fra Skatteetaten.

## Brukerbehov
- Offentlige virksomheter trenger autoritativ tilgang til data fra Skatteetaten i egne tjenester og saksprosesser.
- Private virksomheter trenger kontrollerte opplysninger nÃ¥r lovgrunnlag eller samtykke Ã¥pner for det.
- IntegratÃ¸rer og systemleverandÃ¸rer trenger dokumenterte API-er, rettighetspakker og tydelig driftsinformasjon.
- SamarbeidsmiljÃ¸er i sektor eller bransje trenger en koordinert modell for tilgang og videre dialog med Skatteetaten.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige virksomheter | Tilgang til skatte- og inntektsdata, folkeregisterdata eller andre relevante opplysninger | Saksbehandling, kontroll, automatisering og tjenesteutvikling | Viktigste tverrsektorielle brukergruppe |
| Private virksomheter med hjemmel eller samtykkegrunnlag | Opplysninger til lÃ¥n, kreditt, pensjon, arbeidsgiverprosesser eller andre regulerte tjenester | Integrerte oppslag og automatisert saksstÃ¸tte | Bruk styres av vilkÃ¥r og rettsgrunnlag |
| Segmentansvarlige og samarbeidsgrupper | Samordnet tilgang og koordinering mot Skatteetaten | Finans, kommune, helse, kraft og andre delingsmiljÃ¸er | Viktig del av produktets samarbeidsmodell |
| SystemleverandÃ¸rer og integratÃ¸rer | Dokumentasjon, API-er og stÃ¸tte i innfÃ¸ringslÃ¸pet | Utvikling og drift av sluttbrukersystemer | Teknisk kanal inn til produktet |
| Skatteetaten som forvalter | Styring, vilkÃ¥r, drift og oppfÃ¸lging | Delingsforvaltning, kontaktpunkt og endringshÃ¥ndtering | Operativ forvalter av hele produktomrÃ¥det |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
**Kontrollert tilgjengeliggjÃ¸ring av data gjennom API-er.** Skatteetatens delingstjenester tilbyr maskinell tilgang til data for virksomheter som oppfyller vilkÃ¥r og har rettslig grunnlag. Produktet er derfor fÃ¸rst og fremst en nasjonal delingsflate, ikke et enkelt datasett.

**Felles tilgangs- og samarbeidsmodell.** Produktet omfatter ikke bare API-er, men ogsÃ¥ etablerte lÃ¸p for kontakt, avtaler, bruksvilkÃ¥r, driftsstatus og oppfÃ¸lging. Dette gjÃ¸r delingstjenestene til en helhetlig produktflate for viderebruk av data.

**Segmentsamarbeid for virksomheter med like behov.** Skatteetaten beskriver egne segmenter og segmentansvarlige for grupper av virksomheter med felles behov. Det gir en mer skalerbar modell for samhandling enn individuell oppfÃ¸lging av hver enkelt konsument.

**Teknisk og operativ stÃ¸tte til viderebruk.** Produktet omfatter dokumentasjon, rettighetspakker, vilkÃ¥r og stÃ¸ttefunksjoner som gjÃ¸r det mulig Ã¥ ta tjenestene i bruk og forvalte integrasjonene over tid.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Den samlede delingsflaten for data fra Skatteetaten | Selve fagsystemene og grunnregistrene som produserer dataene |
| API-basert tilgang til utvalgte datatyper | Lokal saksbehandling hos datakonsumentene |
| AvtalelÃ¸p, bruksvilkÃ¥r, kontaktpunkt og stÃ¸ttefunksjoner | Hver enkelt virksomhets interne autorisasjons- og prosesslogikk |
| Segmentsamarbeid og samordnet dialog med konsumentgrupper | Full erstatning for sektorvise integrasjonslÃ¸sninger hos brukerne |
| Driftsstatus og endringskommunikasjon for delingstjenestene | Alle tjenester Skatteetaten tilbyr utenfor datadeling |

## Veikart over kommende funksjonalitet
**Fakta fra Skatteetatens kilder (kontrollert 2026-03-27):**
- Skatteetaten publiserer lÃ¸pende driftsinformasjon, oppdaterte bruksvilkÃ¥r og kontaktinformasjon for delingstjenestene.
- BruksvilkÃ¥rene for inntekt, skatt og restanser er oppdatert med virkning fra 1. september 2024.

**Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Et samlet, tidsfestet veikart for hele produktomrÃ¥det er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til Ã¥ dreie seg om videre standardisering av API-tilgang, bedre operativ stÃ¸tte og samordning pÃ¥ tvers av virksomhetssegmenter.

## Forretningsverdi/Verdiforslag
### For offentlig sektor
- GjÃ¸r det mulig Ã¥ bruke data fra Skatteetaten direkte i digitale tjenester og saksprosesser.
- Reduserer behovet for manuelle bestillinger og lokale spesiallÃ¸sninger.
- StÃ¸tter mer sammenhengende og datadrevne tjenester pÃ¥ tvers av etater.

### For private virksomheter
- GjÃ¸r det mulig Ã¥ bygge regulerte tjenester pÃ¥ oppdaterte data fra Skatteetaten nÃ¥r rettsgrunnlaget er pÃ¥ plass.
- Skaper stÃ¸rre forutsigbarhet gjennom standardiserte tilgangs- og samarbeidslÃ¸p.

### For samfunnet
- Bidrar til bedre gjenbruk av offentlige data.
- GjÃ¸r at data fra Skatteetaten kan skape verdi i flere tjenester enn etaten selv leverer direkte.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk og personvern | Feil tilgang eller for bred bruk av delte opplysninger kan fÃ¥ store konsekvenser | Tydelige vilkÃ¥r, hjemmelsvurdering og tilgangsstyring |
| Teknisk | Endringer i API-er eller driftsforstyrrelser kan ramme mange konsumenter samtidig | God endringsforvaltning, dokumentasjon og statusside |
| Samhandlingsmodell | Uklare roller mellom Skatteetaten, segmentansvarlige og konsumenter kan gi treg innfÃ¸ring | Klare kontaktpunkter og standardiserte samarbeidslÃ¸p |
| Avhengighet | Mange tjenester kan bli avhengige av dataflyt fra Skatteetaten | Robust drift og tydelig prioritering av kritiske delingslÃ¸p |
| ForstÃ¥else og bruk | Konsumenter kan undervurdere juridiske og faglige vilkÃ¥r for gjenbruk | Tydelig dokumentasjon, bruksvilkÃ¥r og stÃ¸ttefunksjoner |

## Kanaler
- Bruke data fra Skatteetaten: https://www.skatteetaten.no/deling/
- Hvorfor vi deler data: https://www.skatteetaten.no/deling/hvorfor-vi-deler-data/
- Kontakt oss om deling av data: https://www.skatteetaten.no/deling/kontakt/
- BruksvilkÃ¥r for delingstjenester om inntekt, skatt og restanser: https://www.skatteetaten.no/deling/bruksvilkar-for-delingstjenester/

## Plattform
Skatteetatens delingstjenester er en felles delings- og integrasjonsflate for data fra Skatteetaten.

**Fakta:** Kildene beskriver produktomrÃ¥det som API-basert datadeling med tilhÃ¸rende avtalemodell, kontaktlÃ¸p, driftsvarsling og teknisk dokumentasjon.

**Ikke offentlig dokumentert i brukte kilder:** Full intern plattformarkitektur, detaljer om underliggende systemlandskap og samlet teknologistakk.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet er laget for viderebruk av data i andre virksomheters prosesser og tjenester.
- Det er sÃ¦rlig relevant nÃ¥r behovet er kontrollert og autoritativ datadeling fra Skatteetaten.
- Det er mindre relevant som selvstendig sluttbrukertjeneste, siden hovedverdien ligger i integrasjon og viderebruk.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres direkte ved at produktet er bygget for Ã¥ dele data fra Skatteetaten med andre.
- **P5: Del og gjenbruk lÃ¸sninger** styrkes ved at datadeling skjer gjennom en felles modell framfor mange bilaterale opplegg.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** stÃ¸ttes fordi produktet kobler Skatteetatens data inn i andre virksomheters tjenester.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** er sentralt fordi delingen mÃ¥ vÃ¦re styrt, sporbar og basert pÃ¥ tydelige vilkÃ¥r.

## Finansiering
- **Fakta:** Kildene beskriver vilkÃ¥r, avtaler og segmentmodeller, men gir ikke en samlet offentlig finansieringsmodell for hele produktet i denne arbeidsÃ¸kten.
- **Deduksjon:** Produktet finansieres som del av Skatteetatens delings- og forvaltningsoppdrag, kombinert med innfÃ¸rings- og integrasjonskostnader hos konsumentene.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Skatteetaten | Delingssidene og kontaktflatene peker til Skatteetaten som ansvarlig virksomhet |
| Driftsansvar | Skatteetaten | ProduktomrÃ¥det har egen driftsstatus og operativ oppfÃ¸lging hos etaten |
| Budsjett- og forvaltningsansvar | Skatteetaten | Deling beskrives som del av samfunnsoppdraget |
| Styringsmodell | Skatteetaten, med samhandling mot segmentansvarlige og konsumentmiljÃ¸er | Delingssidene og kontaktmodellen |

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
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.skatteetaten.no/deling/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/deling/hvorfor-vi-deler-data/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/deling/kontakt/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/deling/bruksvilkar-for-delingstjenester/ (kontrollert 2026-03-27)

