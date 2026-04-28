# Produkt-canvas: NVDB

## Navn
NVDB

## Ressurs ID
SVV-002

## Status/Livsfase
**Produksjon** - etablert nasjonal datakilde og delingsressurs for vegdata.

**Fakta:** Statens vegvesen beskriver NVDB som Nasjonal vegdatabank. Ressursen brukes til å samle, forvalte og tilgjengeliggjøre data om vegnettet og objekter knyttet til veg.

## Modenhet
**Høy modenhet** - etablert nasjonal fellesressurs for vegdata:
- NVDB er innarbeidet som sentralt informasjonsgrunnlag i vegforvaltning og samferdsel.
- Ressursen brukes av mange aktører som trenger oppdatert informasjon om vegnett og vegobjekter.
- Den har verdi både som datakilde, analysegrunnlag og delingsressurs.

**Deduksjon:** Modenheten er høy fordi NVDB ikke framstår som en avgrenset intern sektorløsning, men som en varig og gjenbrukbar nasjonal datainfrastruktur for vegrelatert informasjon.

## Kort beskrivelse
NVDB er den nasjonale datakilden for informasjon om vegnettet og en lang rekke vegrelaterte objekter i Norge. Ressursen samler, forvalter og tilgjengeliggjør vegdata som brukes i forvaltning, analyse, planlegging og digital samhandling. NVDB er derfor ikke bare et fagregister for samferdsel, men et nasjonalt informasjonsgrunnlag med verdi på tvers, blant annet for beredskap, sikkerhet, klima- og bærekraftsarbeid, arealplanlegging og samordning mellom stat, fylke og kommune.

## Kapabiliteter
- **Datakilder: Grunndata** er relevant fordi NVDB fungerer som en autoritativ kilde til sentrale vegdata som andre aktører kan bygge videre på.
- **Informasjonsforvaltning: Oversikt over datasett** er relevant fordi ressursen gjør vegdata forståelige og tilgjengelige som et felles informasjonsgrunnlag.
- **Datautveksling og integrasjon: Dele data med andre** er relevant fordi verdien av NVDB nettopp ligger i at data kan brukes og gjenbrukes av mange ulike aktører og løsninger.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot NVDB som nasjonal datakilde og delingsressurs for vegrelatert informasjon.

## Produktmål
**Primærkilde:** Statens vegvesens side om Nasjonal vegdatabank.

Dokumenterte mål og tydelige formål i kildene:
- samle og forvalte vegdata nasjonalt
- gi tilgang til oppdatert informasjon om vegnettet og vegobjekter
- støtte forvaltning, drift og utvikling av vegsystemet

Operative mål utledet fra de samme kildene:
- gi et felles datagrunnlag for aktører som trenger veginformasjon på tvers av forvaltningsnivåer
- redusere behovet for lokale kopier og parallelle datagrunnlag om veg og vegobjekter
- gjøre det enklere å bruke samme informasjon i analyse, planlegging, beredskap og tjenesteutvikling

## Brukerbehov
- Offentlige virksomheter trenger et pålitelig og felles datagrunnlag om veg og vegobjekter.
- Fylkeskommuner og kommuner trenger tilgang til samme oppdaterte informasjon som statlige aktører når de planlegger, forvalter eller samordner tiltak.
- Beredskaps- og sikkerhetsmiljøer trenger vegdata som kan brukes i situasjonsforståelse, analyse og koordinering.
- Utviklere og analysemiljøer trenger et autoritativt grunnlag for kart, analyser, modeller og digitale tjenester.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Statlige virksomheter | Felles og oppdaterte vegdata | Forvaltning, analyse, beredskap og samordning | Viktig brukergruppe på tvers av sektorer |
| Fylkeskommuner og kommuner | Felles informasjonsgrunnlag om veg og objekter | Planlegging, drift, beredskap og arealforvaltning | Tydelig verdi mellom forvaltningsnivåer |
| Beredskaps- og sikkerhetsmiljøer | Situasjonsforståelse og oppdatert veginformasjon | Krisehåndtering, risiko- og sårbarhetsarbeid | Viser tydelig tverrgående relevans |
| Utviklere og analysemiljøer | Autoritative data til viderebruk | Integrasjoner, analyser, kart og beslutningsstøtte | Typisk teknisk og analytisk brukergruppe |
| Statens vegvesen | Forvaltning, kvalitet og tilgjengeliggjøring | Operativ forvalter av ressursen | Eier- og forvalterrolle |

## Hovedfunksjoner
### Primære funksjoner
**Nasjonalt grunnlag for vegdata.** NVDB samler og forvalter informasjon om vegnett og vegrelaterte objekter i én nasjonal ressurs. Dette gjør at mange aktører kan bygge på samme datagrunnlag i stedet for å etablere egne, delvis overlappende varianter.

**Felles informasjonsgrunnlag på tvers av nivåer og sektorer.** Selv om ressursen springer ut av samferdselsområdet, har den verdi utover egen sektor. Vegdata er relevante i blant annet beredskap, arealplanlegging, samfunnssikkerhet, logistikk, klima- og bærekraftsarbeid og annen samordning der geografi og infrastruktur er viktige innsatsfaktorer.

**Tilgjengeliggjøring for videre bruk.** NVDB har verdi fordi dataene ikke bare forvaltes, men også brukes videre i andre sammenhenger. Ressursen må derfor forstås som både registergrunnlag og delingsressurs, der oppdatert veginformasjon kan inngå i analyser, kartgrunnlag og digitale tjenester.

**Støtte for samordning og beslutningsgrunnlag.** Når flere aktører trenger samme informasjon om vegnettet, gir NVDB et mer konsistent grunnlag for prioritering, vurdering og koordinering. Det er særlig viktig i saker som går på tvers av nivåer, fagområder eller beredskapslinjer.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonal forvaltning og tilgjengeliggjøring av vegdata | Hele økosystemet av karttjenester og fagsystemer som bruker dataene |
| Data om vegnett og vegrelaterte objekter | Alle analyser, modeller og lokale beslutningsstøttesystemer bygget på dataene |
| Felles datagrunnlag for videre bruk og samordning | Hver enkelt sektors eller virksomhets lokale tilpasninger og avledede datasett |
| Nasjonal ressurs med verdi i beredskap, planlegging og forvaltning | Hele transportsektorens øvrige løsninger utenfor selve datagrunnlaget |

## Veikart over kommende funksjonalitet
**Fakta fra tilgjengelige kilder:** Det er ikke hentet ut et samlet, tidsfestet offentlig veikart for NVDB i denne arbeidsøkten.

**Deduksjon:** Videreutvikling vil sannsynligvis være tett knyttet til datakvalitet, tilgjengeliggjøring og samspill med andre løsninger som bruker vegdata i analyse og samhandling.

## Forretningsverdi/Verdiforslag
### For offentlig sektor
- Gir ett felles og autoritativt grunnlag for veginformasjon.
- Styrker samordning mellom stat, fylke og kommune.
- Reduserer behovet for lokale kopier og parallelle datagrunnlag.

### For tverrsektorielle behov
- Gjør vegdata tilgjengelige for beredskap, sikkerhet, bærekraft og planlegging.
- Styrker beslutningsgrunnlaget i saker der infrastruktur og geografi spiller inn.

### For utviklere og analysemiljøer
- Gir en nasjonal kilde som kan brukes i kart, analyser og digitale tjenester.
- Gjør det enklere å bygge videre på et felles og sporbart datagrunnlag.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Feil eller utdatert informasjon kan få konsekvenser i mange analyser og beslutninger | Tydelig forvaltning, kvalitetsarbeid og sporbar retting |
| Samordning | Ulik tolkning eller ulik bruk av vegdata hos ulike aktører kan svekke felles verdi | Standardisert forvaltning og tydelig dokumentasjon |
| Tilgjengelighet | Mange avhengigheter kan gjøre driftsavvik eller utilgjengelighet mer kritisk | Robust drift og forutsigbar forvaltning |
| Scope-forståelse | Brukere kan tro at NVDB dekker alle behov rundt transport- og veginformasjon | Tydelig avgrensning mot andre tjenester og analyser |
| Tverrsektoriell bruk | Ressursen kan undervurderes som fellesressurs hvis den beskrives for smalt | Beskrive og bruke den eksplisitt som delt nasjonalt datagrunnlag |

## Kanaler
- https://www.vegvesen.no/fag/fokusomrader/nasjonal-vegdatabank/

## Plattform
NVDB er en nasjonal data- og delingsressurs for veginformasjon, forvaltet av Statens vegvesen.

**Fakta:** Tilgjengelige kilder beskriver NVDB som nasjonal vegdatabank og som et felles grunnlag for data om veg og vegobjekter.

**Ikke offentlig dokumentert i brukte kilder:** Full teknisk plattformarkitektur, detaljert teknologistakk og samlet oversikt over alle grensesnitt er ikke verifisert i denne arbeidsøkten.

## Gjenbruk
**Høy gjenbruksverdi:**
- Ressursen er særlig relevant når flere aktører trenger samme grunnlag om vegnett og vegobjekter.
- Den er viktig i situasjoner der vegdata må brukes sammen med andre datakilder i tverrgående analyser og tjenester.
- Den er mindre relevant dersom behovet gjelder rent interne prosesser uten kobling til delt veginformasjon.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** støttes tydelig ved at NVDB gjør vegdata tilgjengelige som felles datagrunnlag for flere aktører.
- **P5: Del og gjenbruk løsninger** støttes delvis ved at mange kan bygge videre på samme nasjonale informasjonsgrunnlag i stedet for å etablere egne varianter.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi ressursen muliggjør samordning og felles beslutningsgrunnlag på tvers av nivåer og sektorer.
- **P7: Sørg for tillit til oppgaveløsningen** er viktig fordi autoritative og oppdaterte vegdata er en forutsetning for å kunne bruke ressursen sikkert i planlegging, beredskap og andre viktige oppgaver.

Samtidig er det en viktig svakhet at ressursen lett kan bli tolket som bare samferdselsintern hvis den beskrives for smalt. Ved mulig bruk bør det derfor vurderes aktivt om tverrsektorielle avhengigheter og behov er sterke nok til å gjøre NVDB til relevant fellesgrunnlag i caset.

## Finansiering
Ikke offentlig samlet verifisert i denne arbeidsøkten.

**Deduksjon:** Ressursen framstår som en del av Statens vegvesens nasjonale forvaltningsansvar for vegdata og digital informasjonsinfrastruktur.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Statens vegvesen | Produktsiden for NVDB |
| Forvaltning | Statens vegvesen | Produktsiden beskriver NVDB som nasjonal vegdatabank |
| Styringsmodell | Del av Statens vegvesens nasjonale forvaltning av vegdata | Utledet fra samme kilder |

## Lenke til dokumentasjon
- https://www.vegvesen.no/fag/fokusomrader/nasjonal-vegdatabank/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Lokal fil: `briefs/arbeidsstyring-og-handover/2026-04-11-vurdering-av-nye-ressurskandidater-v1.md`
- Nettkilde: https://www.vegvesen.no/fag/fokusomrader/nasjonal-vegdatabank/ (kontrollert 2026-04-28)
