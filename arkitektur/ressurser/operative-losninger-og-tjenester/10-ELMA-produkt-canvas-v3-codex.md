# Produkt-canvas: ELMA

## Navn
ELMA

## Ressurs ID
DIGDIR-023

## Status/Livsfase
**Produksjon** - etablert nasjonal komponent for oppslag av elektroniske mottakeradresser og mottakskapasiteter i EHF- og Peppol-Ã¸kosystemet.

**Fakta:** Digdir omtaler ELMA som elektronisk mottakerregister. Digdir Docs beskriver lÃ¸sningen som den norske SMP-tjenesten som brukes i oppslag fÃ¸r dokumenter sendes i Peppol-nettverket.

## Modenhet
**HÃ¸y funksjonell modenhet** - etablert og avgrenset komponent med tydelig rolle i samhandlingsmÃ¸nsteret:
- ELMA brukes i ordinÃ¦r drift som en del av norsk infrastruktur for EHF og Peppol.
- Funksjonen er smal og tydelig: oppslag av mottaker, dokumenttyper og tilknyttet aksesspunkt.
- Kildene viser en stabil rollefordeling mellom Digdir som tjenesteleverandÃ¸r, DFÃ˜ som norsk Peppol-myndighet og OpenPeppol som internasjonalt rammeverk.

**Deduksjon:** ELMA er moden som felleskomponent, men avgrenset i funksjon. Produktet lÃ¸ser ikke hele meldingsutvekslingen alene, og bÃ¸r derfor ikke beskrives som full samhandlingsplattform.

## Kort beskrivelse
ELMA er den norske oppslagstjenesten som gjÃ¸r det mulig Ã¥ finne riktig elektronisk mottakeradresse og hvilke dokumenttyper en virksomhet kan motta i EHF- og Peppol-samhandling. Produktet er relevant nÃ¥r en avsender eller et aksesspunkt mÃ¥ avklare hvor et dokument skal sendes og hvilke profiler mottakeren stÃ¸tter. ELMA er derfor en sentral norsk felleskomponent i Peppol-sammenheng, men ikke selve transportnettet eller standardforvaltningen rundt det.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** stÃ¸tter ruting av meldinger ved Ã¥ gi nÃ¸dvendig oppslagsgrunnlag fÃ¸r dokumentet sendes til riktig mottaker og aksesspunkt.
- **Tillit: Identifisering** knytter virksomheter og deltakere til entydige identifikatorer som kan brukes i adressering og oppslag i meldingsÃ¸kosystemet.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Digdirs produkt- og dokumentasjonssider for ELMA og mot rollen ELMA har i norsk Peppol-infrastruktur.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Digdirs produktside for ELMA, Digdir Docs for ELMA og bruksvilkÃ¥r for ELMA.

Dokumenterte mÃ¥l:
- Gi et felles, nasjonalt oppslagspunkt for elektroniske mottakere i EHF- og Peppol-samhandling.
- GjÃ¸re det mulig Ã¥ finne korrekt mottakerinformasjon og stÃ¸ttede dokumentprofiler fÃ¸r sending.
- UnderstÃ¸tte et standardisert norsk samhandlingsmÃ¸nster basert pÃ¥ Peppol.

Operative mÃ¥l utledet fra de samme kildene:
- Redusere feilruting og mislykket levering i dokumentutveksling.
- GjÃ¸re onboarding av virksomheter og mottakskapasiteter mer forutsigbar.
- Skille oppslagsfunksjonen tydelig fra bÃ¥de transport, standardforvaltning og forretningsprosessene i avsender- og mottakersystemer.

## Brukerbehov
- AksesspunktleverandÃ¸rer trenger en autoritativ oppslagstjeneste for Ã¥ finne korrekt mottaker og riktig mottakskapasitet.
- Avsendervirksomheter og deres systemleverandÃ¸rer trenger et felles grunnlag for Ã¥ vite om mottaker kan motta et gitt dokumentformat.
- Mottakervirksomheter trenger en standardisert mÃ¥te Ã¥ registrere og vedlikeholde mottaksinformasjon pÃ¥.
- ForvaltningsmiljÃ¸er trenger en komponent som gjÃ¸r nasjonal EHF- og Peppol-bruk praktisk gjennomfÃ¸rbar uten bilaterale avtaler med hver enkelt mottaker.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| AksesspunktleverandÃ¸rer | Oppslag av mottaker og dokumentkapasitet | Ruting av dokumenter i Peppol | Viktigste direkte tekniske brukere |
| SystemleverandÃ¸rer og integrasjonsteam | Korrekt oppslag fÃ¸r sending | Integrasjon mot EHF- og Peppol-flyt | Bruker ELMA indirekte eller via aksesspunkt |
| Virksomheter som mottakere | Registrere og vedlikeholde mottaksinformasjon | Mottak av EHF- og BIS-dokumenter | Bruker verdien, men ikke alltid grensesnittet direkte |
| Digdir som forvalter | Stabil drift og oppdatert mottakerregister | Forvaltning og tjenesteleveranse | Har den operative produktrollen |
| DFÃ˜ som norsk Peppol-myndighet | Regelverk og nasjonal tilslutning | Styring av norsk Peppol-bruk | Eier ikke ELMA som tjeneste, men setter nasjonale rammer |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- ELMA gjÃ¸r det mulig Ã¥ slÃ¥ opp hvilken elektronisk adresse og hvilket aksesspunkt en mottaker bruker. Denne funksjonen er avgjÃ¸rende for at et dokument skal rutes riktig i meldingsÃ¸kosystemet.
- ELMA gjÃ¸r det mulig Ã¥ se hvilke dokumenttyper og profiler mottakeren stÃ¸tter. Produktet bidrar derfor til at avsender ikke bare finner en mottaker, men ogsÃ¥ vet om mottakeren faktisk kan motta den aktuelle dokumenttypen.
- ELMA samler norsk mottakerinformasjon i et standardisert oppslagsmÃ¸nster. Det gjÃ¸r lÃ¸sningen gjenbrukbar for mange aktÃ¸rer uten at hver avsender mÃ¥ etablere egne mottakerregistre.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Oppslag av mottakeradresse og mottakskapasitet | Selve transporten av dokumentet mellom avsender og mottaker |
| Registrering og vedlikehold av mottaksinformasjon | Utstedelse av sertifikater og tillitsrammeverk |
| Norsk SMP-rolle i Peppol-sammenheng | Forvaltning av EHF-standarden eller OpenPeppol-regelverket |
| Oppslag som stÃ¸tter EHF- og Peppol-ruting | Saksbehandling, bestilling, fakturering eller annen forretningslogikk |

## Veikart over kommende funksjonalitet
**Fakta:** Jeg fant ikke et offentlig, tidsfestet veikart for ELMA i kildene brukt i denne arbeidsÃ¸kten.

**Ikke offentlig dokumentert i denne arbeidsÃ¸kten:** Konkrete roadmap-punkter, planlagte funksjonsutvidelser eller tidsplaner for endringer i ELMA.

**Deduksjon:** Videreutviklingen vil sannsynligvis fÃ¸lge endringer i EHF, Peppol og nasjonale samhandlingsbehov, men dette bÃ¸r bekreftes i egne veikart- eller forvaltningskilder.

## Forretningsverdi/Verdiforslag
### For virksomheter og leverandÃ¸rer
- Reduserer usikkerhet om hvor dokumenter skal sendes.
- Gir et felles og forutsigbart grunnlag for mottakeroppslag i stedet for lokale oversikter og manuelle avklaringer.

### For nasjonal samhandling
- GjÃ¸r EHF- og Peppol-bruk mer skalerbar fordi mange aktÃ¸rer kan stÃ¸tte seg pÃ¥ samme oppslagstjeneste.
- Senker terskelen for standardisert dokumentutveksling mellom virksomheter.

### For arkitektur og gjenbruk
- TydeliggjÃ¸r et viktig skille mellom oppslag, transport og standardforvaltning.
- Er en gjenbrukbar komponent som kan brukes av mange avsendere og leverandÃ¸rer uten at den selv mÃ¥ bygges pÃ¥ nytt i hver lÃ¸sning.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Feil eller utdatert registrering kan gi feil mottaker eller feil dokumentflyt | Tydelige registreringsregler, ansvar for vedlikehold og nasjonale bruksvilkÃ¥r |
| Teknisk | Feil i oppslag eller integrasjon kan stoppe dokumentflyt | Standardisert API-bruk, testregimer og tydelig dokumentasjon |
| Sikkerhet | Feil kobling mellom identifikator og mottaker kan fÃ¥ direkte effekt pÃ¥ leveransen | Kontrollert registrering, sporbarhet og samspill med Peppol-regelverk |
| Forvaltning | Rollefordelingen mellom Digdir, DFÃ˜ og OpenPeppol kan vÃ¦re uklar for brukerne | Tydelig dokumentasjon av nasjonal og internasjonal rollefordeling |
| Brukeropplevelse | ELMA kan feilaktig oppfattes som hele lÃ¸sningen for dokumentutveksling | Klare avgrensninger i dokumentasjon og produktbeskrivelse |

## Kanaler
- Digdir produktside: https://www.digdir.no/felleslosninger/elektronisk-mottakerregister-elma/784
- Digdir Docs: https://docs.digdir.no/docs/ELMA/
- Samarbeidsportalen: https://samarbeid.digdir.no/elma/dette-er-elma/108
- BruksvilkÃ¥r: https://samarbeid.digdir.no/elma/bruksvilkar-elma/2072

## Plattform
ELMA er en norsk oppslagstjeneste i Peppol-sammenheng, og fungerer som nasjonal SMP-komponent.

**Fakta:**
- Digdir Docs beskriver ELMA som norsk SMP.
- ELMA brukes i oppslag fÃ¸r dokumentet sendes videre i Peppol-nettverket.
- LÃ¸sningen henger sammen med internasjonale Peppol-komponenter, men er selv en nasjonal tjeneste.

**Viktig avgrensning:** ELMA er ikke selve transportnettet, ikke aksesspunktet og ikke standardsettet. Produktet er en spesialisert oppslagstjeneste i en stÃ¸rre fÃ¸derert arkitektur.

## Gjenbruk
**HÃ¸y gjenbruksverdi innen sitt avgrensede formÃ¥l:**
- Mange avsendere, leverandÃ¸rer og aksesspunktaktÃ¸rer kan bruke samme nasjonale oppslagstjeneste.
- ELMA gjÃ¸r det unÃ¸dvendig Ã¥ bygge egne mottakerregistre for hver lÃ¸sning.
- Gjenbruksverdien er hÃ¸y i EHF- og Peppol-sammenheng, men lav utenfor dette Ã¸kosystemet.

## StÃ¸tter arkitekturprinsipper
- **P5 Del og gjenbruk lÃ¸sninger** - ELMA er en nasjonal komponent som kan brukes av mange aktÃ¸rer i samme samhandlingsmÃ¸nster.
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** - produktet er laget for Ã¥ muliggjÃ¸re standardisert samhandling mellom avsendere, mottakere og aksesspunkt.
- **P7 SÃ¸rg for tillit til oppgavelÃ¸sningen** - entydig identifisering og kontrollert registrering av mottaksinformasjon er en sentral del av verdien.

## Finansiering
- **Ikke fullstendig offentlig dokumentert i brukte kilder:** Jeg fant ikke en detaljert offentlig finansieringsmodell for ELMA i denne arbeidsÃ¸kten.
- **Deduksjon:** ELMA framstÃ¥r som en forvaltet nasjonal Digdir-tjeneste, mens nasjonal styring og bruksvilkÃ¥r ogsÃ¥ pÃ¥virkes av rollen til DFÃ˜ som norsk Peppol-myndighet.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir | Digdirs produktside og Digdir Docs |
| Driftsansvar | Digdir som tjenesteleverandÃ¸r for ELMA | Digdir Docs |
| Budsjettansvar | Ikke eksplisitt offentlig dokumentert i brukte kilder | Ikke verifisert i denne arbeidsÃ¸kten |
| Styringsmodell | Digdir forvalter tjenesten, DFÃ˜ har nasjonal myndighetsrolle for Peppol, og OpenPeppol setter internasjonale rammer | Digdir Docs, bruksvilkÃ¥r for ELMA og EHF/Peppol-kilder |

## Lenke til dokumentasjon
- https://www.digdir.no/felleslosninger/elektronisk-mottakerregister-elma/784
- https://docs.digdir.no/docs/ELMA/
- https://samarbeid.digdir.no/elma/dette-er-elma/108
- https://samarbeid.digdir.no/elma/bruksvilkar-elma/2072

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/10-ELMA-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.digdir.no/felleslosninger/elektronisk-mottakerregister-elma/784 (hentet 2026-03-18)
- Nettkilde: https://docs.digdir.no/docs/ELMA/ (hentet 2026-03-18)
- Nettkilde: https://samarbeid.digdir.no/elma/dette-er-elma/108 (hentet 2026-03-18)
- Nettkilde: https://samarbeid.digdir.no/elma/bruksvilkar-elma/2072 (hentet 2026-03-18)
- Nettkilde: https://www.anskaffelser.no/hva-skal-du-kjope/fagsystemer-digitale-anskaffelser/elektronisk-handelsformat-ehf (hentet 2026-03-18)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen bygger videre pÃ¥ `10-ELMA-produkt-canvas-v2-copilot.md`, men er strammet inn mot offisielle kilder fra Digdir og anskaffelser.no.
- Produktet er tydelig skilt fra standarder, transportnett og veiledningsmateriell.
- Eier- og styringsbildet er ryddet slik at Digdir, DFÃ˜ og OpenPeppol har ulike roller i teksten.

### Tekstlige forbedringer
- Produktet beskrives nÃ¥ pÃ¥ samme nivÃ¥ som andre ressurser i registeret.
- Kapabilitetsvalget er redusert til direkte og sterke koblinger.
- Hovedfunksjoner og avgrensning er skrevet om slik at ELMA lettere kan skilles fra Peppol eDelivery og andre meldingsressurser.

