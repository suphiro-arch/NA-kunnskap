# Produkt-canvas: NAIS

## Navn
NAIS

## Ressurs ID
NAV-002

## Status/Livsfase
**Produksjon** - etablert plattform for utvikling, utrulling og drift av applikasjoner.

**Fakta:** Nais beskriver seg som en plattform laget av Nav for å gi fart og flyt til utviklerne i offentlig sektor, med åpen dokumentasjon av plattformfunksjoner, ansvar og arbeidsmønstre.

## Modenhet
**Høy modenhet** - innarbeidet plattform med tydelige drifts- og utviklingsmønstre:
- moden dokumentasjon for utviklingsteam og plattformmiljøer
- etablert praksis for utrulling, observability og sikkerhet
- tydelig ansvarsmodell mellom plattformmiljø og applikasjonsteam

**Presisering:** Modenheten er høy som plattform. Ressursens status som formell nasjonal felleskomponent er ikke dokumentert på samme nivå som klassiske nasjonale fellesløsninger.

## Kort beskrivelse
NAIS er en plattform for utvikling, kjøring og forvaltning av applikasjoner, laget av Nav og gjort tilgjengelig som åpen plattformmodell for utviklingsteam i offentlig sektor. Løsningen samler sentrale byggeklosser for deploy, konfigurasjon, sikkerhet, observability og plattformnær drift.

Ressursen er først og fremst en gjenbrukbar plattformmodell, ikke en juridisk definert nasjonal felleskomponent. Den er relevant i arkitekturvurderinger når behovet er standardisert utviklings- og kjøretidsmiljø, men bør vurderes opp mot organisasjonens styringsbehov, kompetanse og ansvarsevne.

## Kapabiliteter
- **Tjenesteutvikling: Gjenbrukbare tjenester**  
  NAIS tilbyr felles plattformkapabiliteter og byggeklosser som reduserer behovet for lokale særvarianter i teamenes applikasjonsløp.

- **Tjenesteutvikling: Utviklings- og kjøretidsmiljø**  
  Ressursen gir et standardisert miljø for utvikling, utrulling og drift av applikasjoner, med støtte for gjennomgående livsløp i teamenes leveranser.

## Produktmål
- gi utviklingsteam raskere og tryggere vei fra kode til produksjon
- etablere et felles plattformgrunnlag med tydelige standarder og ansvar
- redusere operasjonell kompleksitet i appdrift gjennom delte byggeklosser
- gjøre plattformmønstre gjenbrukbare på tvers av team og virksomheter

## Brukerbehov
- utviklingsteam trenger et konsistent miljø for bygg, deploy og drift
- plattformmiljøer trenger standardiserte mekanismer for sikkerhet og observability
- virksomheter trenger grunnlag for gjenbruk i stedet for å bygge plattform på nytt
- arkitektur- og styringsmiljøer trenger tydelig avgrensning mellom plattformansvar og applikasjonsansvar

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Utviklingsteam | Felles runtime og deploy-mønstre | Bygging, utrulling og drift av applikasjoner | Primærbrukere |
| Plattform- og driftsteam | Standardisert plattformforvaltning | Videreutvikling, sikkerhet og operasjonell støtte | Kjerne i forvaltning |
| Arkitektur- og styringsmiljøer | Vurdering av gjenbrukbar plattformmodell | Portefølje- og løsningsvalg | Viktig for avgrensning |
| Offentlige virksomheter som vurderer gjenbruk | Dokumentert plattformtilnærming | Vurdering av samarbeid eller adopsjon | Sekundær målgruppe |

## Hovedfunksjoner
NAIS leverer et standardisert kjøretids- og driftsmiljø for applikasjoner. Plattformen gir teamene et felles fundament for å kjøre tjenester med konsistente mønstre for utrulling, konfigurasjon og operasjonell håndtering.

En sentral funksjon er å tilby gjenbrukbare plattformtjenester som ellers ofte bygges lokalt i hvert team. Dette gir mer enhetlig praksis for sikkerhet, logging, måling og hendelseshåndtering, og reduserer unødig duplisering av plattformarbeid.

Plattformen fungerer også som et styringsgrep ved å tydeliggjøre ansvar mellom plattformmiljø og applikasjonsteam. Denne ansvarsdelingen er viktig for skalerbar drift og forutsigbar videreutvikling i komplekse porteføljer.

Samtidig er NAIS avgrenset til plattformlaget. Ressursen er ikke en komplett fagløsning, og den overtar ikke virksomhetenes behov for lokal autorisasjonslogikk, domenevalg eller fagspesifikk prosessutforming.

### Typiske brukssituasjoner (generisk)
- når flere team trenger et felles og standardisert miljø for appdrift
- når virksomheten vil redusere lokal plattformgjeld og gjenbruke plattformmønstre
- når utviklingshastighet må kombineres med robuste sikkerhets- og driftsmekanismer
- når arkitekturarbeid trenger tydelig skille mellom plattformansvar og applikasjonsansvar

### Når NAIS normalt ikke er førstevalg
- når behovet primært er en nasjonal register- eller datadelingstjeneste
- når virksomheten trenger en ferdig fagløsning heller enn plattformgrunnlag
- når organisasjonen ikke har kapasitet til å forvalte teamansvar i samspill med plattformmodell

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Felles runtime og plattformtjenester | Fagspesifikke applikasjoner og prosesser |
| Deploy-, observability- og driftsmønstre | Full virksomhetsarkitektur for hele organisasjonen |
| Åpen dokumentert plattformmodell | Formell juridisk klassifisering som nasjonal felleskomponent |

## Veikart over kommende funksjonalitet
Ikke offentlig dokumentert som ett samlet, sentralt veikart i kildene brukt i denne revisjonen.

**Fakta:** Dokumentasjonen oppdateres løpende med funksjons- og driftsnær veiledning.

**Deduksjon:** Videreutvikling vil i praksis dreie seg om plattformforbedringer i sikkerhet, observability, driftseffektivitet og teamstøtte.

## Forretningsverdi/Verdiforslag
### For utviklingsteam
- kortere vei fra utvikling til stabil produksjon
- mindre tid brukt på grunnleggende plattformarbeid

### For virksomheter
- mer forutsigbar appdrift gjennom standardisert plattformgrunnlag
- redusert risiko for fragmentert plattformutvikling i parallelle team

### For plattform- og driftsmiljøer
- tydeligere styringsgrunnlag for sikkerhet og operasjonell kvalitet
- bedre skalerbarhet i forvaltning når felles mønstre brukes bredt

### For offentlig samhandling
- mulig gjenbruk av plattformmønstre i flere virksomheter der kontekst og ansvar tillater det
- bedre grunnlag for dialog om felles tekniske arbeidsmåter på tvers

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Styringsavgrensning | NAIS kan forveksles med formell nasjonal felleskomponent | Tydelig klassifisering som gjenbrukbar plattformmodell |
| Organisatorisk modenhet | Virksomheter kan undervurdere krav til teamansvar og driftsevne | Avklaring av roller og kompetanse før adopsjon |
| Leverandør- og teknologibinding | Plattformvalg kan skape bindinger i arbeidsmåter og verktøy | Bevisst arkitekturvurdering og dokumentert avgrensning |
| Sikkerhet og ansvar | Uklart skille mellom plattformansvar og appansvar kan gi svakheter | Etablert ansvarsmodell og tydelige driftsprinsipper |
| Overførbarhet | Mønstre som fungerer i én kontekst er ikke alltid direkte overførbare | Trinnvis innføring og lokal tilpasning med tydelig scope |

## Kanaler
- https://nais.io/
- https://doc.nais.io/
- https://github.com/navikt

## Plattform
NAIS er selv en plattformressurs for applikasjonsutvikling og drift, basert på gjenbrukbare tekniske byggeklosser og dokumenterte arbeidsmønstre.

## Gjenbruk
**Middels til høy gjenbruksverdi** som plattformmodell i offentlig sektor, avhengig av organisatorisk modenhet og ansvarsevne.

### Vanlige kombinasjoner med andre produkter
- NAIS + Maskinporten når applikasjoner trenger sikker maskin-til-maskin-kommunikasjon mot offentlige API-er
- NAIS + ID-porten/Ansattporten når plattformbaserte tjenester trenger standardisert innlogging
- NAIS + Altinn-økosystemet i løsninger som kombinerer plattformdrift med nasjonale samhandlingskomponenter

**Kildekode:** Åpen kildekode. Plattformen er publisert på [github.com/nais](https://github.com/nais), blant annet `naiserator`, `wonderwall` og `tokendings`, i hovedsak under MIT-lisens. Applikasjoner som kjører på plattformen ligger under [github.com/navikt](https://github.com/navikt).

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger** ved å tilby delte plattformkapabiliteter som kan gjenbrukes på tvers av team.
- **P6: Lag digitale løsninger som støtter samhandling** ved å standardisere tekniske arbeidsmønstre som gjør samarbeid mellom team enklere.

Spenning: Ressursen støtter gjenbruk sterkt, men kan samtidig gi høy terskel i organisasjoner uten moden plattformforvaltning.

## Finansiering
Ikke offentlig dokumentert i detalj i kildene brukt i denne revisjonen.

**Deduksjon:** Finansiering følger Navs plattformforvaltning, mens bruk i andre kontekster normalt krever egen organisatorisk og økonomisk avklaring.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Nav / NAIS-miljøet | Offentlig dokumentasjon |
| Driftsansvar | Nav / plattformmiljøet | Offentlig dokumentasjon |
| Bruksansvar for applikasjoner | De enkelte teamene | Publisert ansvarsmodell |
| Budsjettansvar | Ikke offentlig detaljert | Ikke eksplisitt oppgitt i åpne kilder |
| Styringsmodell | Plattformstyring med tydelig rollefordeling mellom plattform og team | Dokumenterte rollebeskrivelser |

## Lenke til dokumentasjon
- https://nais.io/
- https://doc.nais.io/
- https://doc.nais.io/explanations/nais/
- https://doc.nais.io/legal/roles-responsibilities/
- https://github.com/navikt

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Nettkilde: https://nais.io/ (kontrollert 2026-05-26)
- Nettkilde: https://doc.nais.io/ (kontrollert 2026-05-26)
- Nettkilde: https://doc.nais.io/explanations/nais/ (kontrollert 2026-05-26)
- Nettkilde: https://doc.nais.io/legal/roles-responsibilities/ (kontrollert 2026-05-26)
- Nettkilde: https://github.com/navikt (kontrollert 2026-05-26)

## Endringer fra forrige versjon
- Analyseforbedringer: tydeligere avgrensning mellom plattformmodenhet og formell felleskomponentstatus, samt skarpere risikovurdering av styring og overførbarhet.
- Tekstlige forbedringer: mer beslutningsstøttende beskrivelser av når NAIS er relevant, og når andre løsningsvalg bør vurderes.
