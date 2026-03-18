# Produkt-canvas: ELMA

## Navn
ELMA

## Ressurs ID
DIGDIR-023

## Status/Livsfase
**Produksjon** - etablert nasjonal komponent for oppslag av elektroniske mottakeradresser og mottakskapasiteter i EHF- og Peppol-økosystemet.

**Fakta:** Digdir omtaler ELMA som elektronisk mottakerregister. Digdir Docs beskriver løsningen som den norske SMP-tjenesten som brukes i oppslag før dokumenter sendes i Peppol-nettverket.

## Modenhet
**Høy funksjonell modenhet** - etablert og avgrenset komponent med tydelig rolle i samhandlingsmønsteret:
- ELMA brukes i ordinær drift som en del av norsk infrastruktur for EHF og Peppol.
- Funksjonen er smal og tydelig: oppslag av mottaker, dokumenttyper og tilknyttet aksesspunkt.
- Kildene viser en stabil rollefordeling mellom Digdir som tjenesteleverandør, DFØ som norsk Peppol-myndighet og OpenPeppol som internasjonalt rammeverk.

**Deduksjon:** ELMA er moden som felleskomponent, men avgrenset i funksjon. Produktet løser ikke hele meldingsutvekslingen alene, og bør derfor ikke beskrives som full samhandlingsplattform.

## Kort beskrivelse
ELMA er den norske oppslagstjenesten som gjør det mulig å finne riktig elektronisk mottakeradresse og hvilke dokumenttyper en virksomhet kan motta i EHF- og Peppol-samhandling. Produktet er relevant når en avsender eller et aksesspunkt må avklare hvor et dokument skal sendes og hvilke profiler mottakeren støtter. ELMA er derfor en sentral norsk felleskomponent i Peppol-sammenheng, men ikke selve transportnettet eller standardforvaltningen rundt det.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** støtter ruting av meldinger ved å gi nødvendig oppslagsgrunnlag før dokumentet sendes til riktig mottaker og aksesspunkt.
- **Tillit: Identifisering** knytter virksomheter og deltakere til entydige identifikatorer som kan brukes i adressering og oppslag i meldingsøkosystemet.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Digdirs produkt- og dokumentasjonssider for ELMA og mot rollen ELMA har i norsk Peppol-infrastruktur.

## Produktmål
**Primærkilder:** Digdirs produktside for ELMA, Digdir Docs for ELMA og bruksvilkår for ELMA.

Dokumenterte mål:
- Gi et felles, nasjonalt oppslagspunkt for elektroniske mottakere i EHF- og Peppol-samhandling.
- Gjøre det mulig å finne korrekt mottakerinformasjon og støttede dokumentprofiler før sending.
- Understøtte et standardisert norsk samhandlingsmønster basert på Peppol.

Operative mål utledet fra de samme kildene:
- Redusere feilruting og mislykket levering i dokumentutveksling.
- Gjøre onboarding av virksomheter og mottakskapasiteter mer forutsigbar.
- Skille oppslagsfunksjonen tydelig fra både transport, standardforvaltning og forretningsprosessene i avsender- og mottakersystemer.

## Brukerbehov
- Aksesspunktleverandører trenger en autoritativ oppslagstjeneste for å finne korrekt mottaker og riktig mottakskapasitet.
- Avsendervirksomheter og deres systemleverandører trenger et felles grunnlag for å vite om mottaker kan motta et gitt dokumentformat.
- Mottakervirksomheter trenger en standardisert måte å registrere og vedlikeholde mottaksinformasjon på.
- Forvaltningsmiljøer trenger en komponent som gjør nasjonal EHF- og Peppol-bruk praktisk gjennomførbar uten bilaterale avtaler med hver enkelt mottaker.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Aksesspunktleverandører | Oppslag av mottaker og dokumentkapasitet | Ruting av dokumenter i Peppol | Viktigste direkte tekniske brukere |
| Systemleverandører og integrasjonsteam | Korrekt oppslag før sending | Integrasjon mot EHF- og Peppol-flyt | Bruker ELMA indirekte eller via aksesspunkt |
| Virksomheter som mottakere | Registrere og vedlikeholde mottaksinformasjon | Mottak av EHF- og BIS-dokumenter | Bruker verdien, men ikke alltid grensesnittet direkte |
| Digdir som forvalter | Stabil drift og oppdatert mottakerregister | Forvaltning og tjenesteleveranse | Har den operative produktrollen |
| DFØ som norsk Peppol-myndighet | Regelverk og nasjonal tilslutning | Styring av norsk Peppol-bruk | Eier ikke ELMA som tjeneste, men setter nasjonale rammer |

## Hovedfunksjoner
### Primære funksjoner
- ELMA gjør det mulig å slå opp hvilken elektronisk adresse og hvilket aksesspunkt en mottaker bruker. Denne funksjonen er avgjørende for at et dokument skal rutes riktig i meldingsøkosystemet.
- ELMA gjør det mulig å se hvilke dokumenttyper og profiler mottakeren støtter. Produktet bidrar derfor til at avsender ikke bare finner en mottaker, men også vet om mottakeren faktisk kan motta den aktuelle dokumenttypen.
- ELMA samler norsk mottakerinformasjon i et standardisert oppslagsmønster. Det gjør løsningen gjenbrukbar for mange aktører uten at hver avsender må etablere egne mottakerregistre.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Oppslag av mottakeradresse og mottakskapasitet | Selve transporten av dokumentet mellom avsender og mottaker |
| Registrering og vedlikehold av mottaksinformasjon | Utstedelse av sertifikater og tillitsrammeverk |
| Norsk SMP-rolle i Peppol-sammenheng | Forvaltning av EHF-standarden eller OpenPeppol-regelverket |
| Oppslag som støtter EHF- og Peppol-ruting | Saksbehandling, bestilling, fakturering eller annen forretningslogikk |

## Veikart over kommende funksjonalitet
**Fakta:** Jeg fant ikke et offentlig, tidsfestet veikart for ELMA i kildene brukt i denne arbeidsøkten.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Konkrete roadmap-punkter, planlagte funksjonsutvidelser eller tidsplaner for endringer i ELMA.

**Deduksjon:** Videreutviklingen vil sannsynligvis følge endringer i EHF, Peppol og nasjonale samhandlingsbehov, men dette bør bekreftes i egne veikart- eller forvaltningskilder.

## Forretningsverdi/Verdiforslag
### For virksomheter og leverandører
- Reduserer usikkerhet om hvor dokumenter skal sendes.
- Gir et felles og forutsigbart grunnlag for mottakeroppslag i stedet for lokale oversikter og manuelle avklaringer.

### For nasjonal samhandling
- Gjør EHF- og Peppol-bruk mer skalerbar fordi mange aktører kan støtte seg på samme oppslagstjeneste.
- Senker terskelen for standardisert dokumentutveksling mellom virksomheter.

### For arkitektur og gjenbruk
- Tydeliggjør et viktig skille mellom oppslag, transport og standardforvaltning.
- Er en gjenbrukbar komponent som kan brukes av mange avsendere og leverandører uten at den selv må bygges på nytt i hver løsning.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil eller utdatert registrering kan gi feil mottaker eller feil dokumentflyt | Tydelige registreringsregler, ansvar for vedlikehold og nasjonale bruksvilkår |
| Teknisk | Feil i oppslag eller integrasjon kan stoppe dokumentflyt | Standardisert API-bruk, testregimer og tydelig dokumentasjon |
| Sikkerhet | Feil kobling mellom identifikator og mottaker kan få direkte effekt på leveransen | Kontrollert registrering, sporbarhet og samspill med Peppol-regelverk |
| Forvaltning | Rollefordelingen mellom Digdir, DFØ og OpenPeppol kan være uklar for brukerne | Tydelig dokumentasjon av nasjonal og internasjonal rollefordeling |
| Brukeropplevelse | ELMA kan feilaktig oppfattes som hele løsningen for dokumentutveksling | Klare avgrensninger i dokumentasjon og produktbeskrivelse |

## Kanaler
- Digdir produktside: https://www.digdir.no/felleslosninger/elektronisk-mottakerregister-elma/784
- Digdir Docs: https://docs.digdir.no/docs/ELMA/
- Samarbeidsportalen: https://samarbeid.digdir.no/elma/dette-er-elma/108
- Bruksvilkår: https://samarbeid.digdir.no/elma/bruksvilkar-elma/2072

## Plattform
ELMA er en norsk oppslagstjeneste i Peppol-sammenheng, og fungerer som nasjonal SMP-komponent.

**Fakta:**
- Digdir Docs beskriver ELMA som norsk SMP.
- ELMA brukes i oppslag før dokumentet sendes videre i Peppol-nettverket.
- Løsningen henger sammen med internasjonale Peppol-komponenter, men er selv en nasjonal tjeneste.

**Viktig avgrensning:** ELMA er ikke selve transportnettet, ikke aksesspunktet og ikke standardsettet. Produktet er en spesialisert oppslagstjeneste i en større føderert arkitektur.

## Gjenbruk
**Høy gjenbruksverdi innen sitt avgrensede formål:**
- Mange avsendere, leverandører og aksesspunktaktører kan bruke samme nasjonale oppslagstjeneste.
- ELMA gjør det unødvendig å bygge egne mottakerregistre for hver løsning.
- Gjenbruksverdien er høy i EHF- og Peppol-sammenheng, men lav utenfor dette økosystemet.

## Støtter arkitekturprinsipper
- **P5 Del og gjenbruk løsninger** - ELMA er en nasjonal komponent som kan brukes av mange aktører i samme samhandlingsmønster.
- **P6 Lag digitale løsninger som støtter samhandling** - produktet er laget for å muliggjøre standardisert samhandling mellom avsendere, mottakere og aksesspunkt.
- **P7 Sørg for tillit til oppgaveløsningen** - entydig identifisering og kontrollert registrering av mottaksinformasjon er en sentral del av verdien.

## Finansiering
- **Ikke fullstendig offentlig dokumentert i brukte kilder:** Jeg fant ikke en detaljert offentlig finansieringsmodell for ELMA i denne arbeidsøkten.
- **Deduksjon:** ELMA framstår som en forvaltet nasjonal Digdir-tjeneste, mens nasjonal styring og bruksvilkår også påvirkes av rollen til DFØ som norsk Peppol-myndighet.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir | Digdirs produktside og Digdir Docs |
| Driftsansvar | Digdir som tjenesteleverandør for ELMA | Digdir Docs |
| Budsjettansvar | Ikke eksplisitt offentlig dokumentert i brukte kilder | Ikke verifisert i denne arbeidsøkten |
| Styringsmodell | Digdir forvalter tjenesten, DFØ har nasjonal myndighetsrolle for Peppol, og OpenPeppol setter internasjonale rammer | Digdir Docs, bruksvilkår for ELMA og EHF/Peppol-kilder |

## Lenke til dokumentasjon
- https://www.digdir.no/felleslosninger/elektronisk-mottakerregister-elma/784
- https://docs.digdir.no/docs/ELMA/
- https://samarbeid.digdir.no/elma/dette-er-elma/108
- https://samarbeid.digdir.no/elma/bruksvilkar-elma/2072

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `results/Produktbeskrivelser/10-ELMA-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.digdir.no/felleslosninger/elektronisk-mottakerregister-elma/784 (hentet 2026-03-18)
- Nettkilde: https://docs.digdir.no/docs/ELMA/ (hentet 2026-03-18)
- Nettkilde: https://samarbeid.digdir.no/elma/dette-er-elma/108 (hentet 2026-03-18)
- Nettkilde: https://samarbeid.digdir.no/elma/bruksvilkar-elma/2072 (hentet 2026-03-18)
- Nettkilde: https://www.anskaffelser.no/hva-skal-du-kjope/fagsystemer-digitale-anskaffelser/elektronisk-handelsformat-ehf (hentet 2026-03-18)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen bygger videre på `10-ELMA-produkt-canvas-v2-copilot.md`, men er strammet inn mot offisielle kilder fra Digdir og anskaffelser.no.
- Produktet er tydelig skilt fra standarder, transportnett og veiledningsmateriell.
- Eier- og styringsbildet er ryddet slik at Digdir, DFØ og OpenPeppol har ulike roller i teksten.

### Tekstlige forbedringer
- Produktet beskrives nå på samme nivå som andre ressurser i registeret.
- Kapabilitetsvalget er redusert til direkte og sterke koblinger.
- Hovedfunksjoner og avgrensning er skrevet om slik at ELMA lettere kan skilles fra Peppol eDelivery og andre meldingsressurser.
