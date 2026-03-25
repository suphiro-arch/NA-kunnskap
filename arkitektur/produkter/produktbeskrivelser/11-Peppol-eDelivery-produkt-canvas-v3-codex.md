# Produkt-canvas: Peppol eDelivery

## Navn
Peppol eDelivery

## Ressurs ID
OPP-001

## Status/Livsfase
**Produksjon** - modent internasjonalt samhandlingsrammeverk i aktiv bruk for standardisert dokumentutveksling mellom virksomheter.

**Fakta:** OpenPeppol beskriver eDelivery som del av transportinfrastrukturen i Peppol-nettverket. Norske kilder for EHF beskriver hvordan virksomheter kobler seg til dette mønsteret gjennom aksesspunkt, identifikatorer og nasjonale støttekomponenter.

## Modenhet
**Høy funksjonell modenhet** - etablert internasjonalt økosystem med tydelig rollefordeling:
- Peppol eDelivery brukes på tvers av land og leverandører og bygger på et dokumentert samspill mellom aksesspunkt, oppslagstjenester, identifikatorer og tillitsmekanismer.
- Løsningen er moden som samhandlingsmønster, ikke som én sentral plattform eid og driftet av én aktør.
- Norske kilder viser en stabil nasjonal rollefordeling der DFØ er norsk Peppol-myndighet, Digdir leverer ELMA, og private leverandører tilbyr aksesspunkt.

**Deduksjon:** Modenheten er høy fordi mønsteret er mye brukt og tydelig regulert. Samtidig krever det mer forklaring enn klassiske norske felleskomponenter fordi økosystemet er føderert og fordelt på flere aktører.

## Kort beskrivelse
Peppol eDelivery er et internasjonalt samhandlingsrammeverk for sikker og standardisert utveksling av elektroniske dokumenter mellom virksomheter. Ressursen er relevant når en løsning trenger et felles transport- og adresseringsmønster for dokumentutveksling, særlig i sammenheng med EHF og andre Peppol-baserte dokumentformater. Peppol eDelivery bør forstås som et føderert økosystem med standarder, tillitsmekanismer og leverandørdrevne aksesspunkt, ikke som én norsk fellesløsning eller én sentral driftstjeneste.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** gir et føderert mønster for standardisert dokumentutveksling mellom virksomheter.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** bruker sertifikater og tillitsrammeverk for å sikre transport og validering i nettverket.
- **Standardisering: Forvaltningsstandarder** bygger på forvaltede samhandlingsregler, meldingsprofiler og transportspesifikasjoner.
- **Tillit: Identifisering** baserer ruting og adressering på entydige deltakeridentifikatorer.

## Produktmål
**Primærkilder:** OpenPeppol dokumentasjon og norske EHF-/Peppol-kilder på anskaffelser.no.

Dokumenterte mål:
- Gi et felles transportmønster for dokumentutveksling mellom virksomheter.
- Gjøre interoperabel dokumentutveksling mulig på tvers av leverandører, land og sektorer.
- Understøtte standardisert bruk av elektroniske dokumentformater som EHF og Peppol BIS.

Operative mål utledet fra de samme kildene:
- Redusere behovet for bilaterale meldingsoppsett mellom hver avsender og mottaker.
- Gjøre det mulig å kombinere private leverandører og nasjonale komponenter innenfor samme samhandlingsmønster.
- Skille mellom selve nettverksmønsteret og nasjonale komponenter som ELMA, EHF-veiledning og myndighetsrolle.

## Brukerbehov
- Virksomheter trenger et standardisert mønster for sikker dokumentutveksling uten å forhandle egne integrasjoner med hver enkelt motpart.
- Systemleverandører og integrasjonsteam trenger dokumenterte transport- og adresseringsregler som fungerer på tvers av mange aktører.
- Myndigheter og forvaltningsmiljøer trenger et felles økosystem som gjør EHF og lignende standarder praktisk brukbare i markedet.
- Leverandører av aksesspunkt trenger et felles sett med regler og tekniske spesifikasjoner for å kunne operere i samme nettverk.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Private aksesspunktleverandører | Koble virksomheter til Peppol-nettverket | Drift av endepunkter og transport | Viktigste operative infrastrukturaktører |
| Systemleverandører og integrasjonsteam | Bygge løsninger som kan sende og motta standardiserte dokumenter | ERP, økonomisystemer, meldingsflyt | Bruker mønsteret gjennom API-er og integrasjoner |
| Virksomheter som sender og mottar dokumenter | Standardisert og forutsigbar samhandling | Faktura, ordre og andre strukturerte dokumenter | Nyter verdien, men forvalter ikke økosystemet |
| DFØ som norsk Peppol-myndighet | Nasjonal styring og etterlevelse | Forvaltning av norsk tilknytning til Peppol | Har ikke hele tjenesten alene |
| Digdir som leverandør av ELMA | Nasjonal støttekomponent for oppslag | Norsk infrastruktur rundt Peppol | Viktig nasjonal rolle, men ikke hele eDelivery |
| OpenPeppol | Internasjonalt rammeverk og regelverk | Forvaltning av nettverk, avtaler og spesifikasjoner | Overordnet økosystemeier |

## Hovedfunksjoner
### Primære funksjoner
- Peppol eDelivery gir et standardisert mønster for hvordan elektroniske dokumenter sendes mellom virksomheter gjennom aksesspunkt. Det er derfor primært en samhandlingsarkitektur for transport og adressering.
- Peppol eDelivery gjør det mulig å kombinere flere aktører i samme nettverk. Produktets verdi ligger i at avsender og mottaker ikke trenger å bruke samme leverandør så lenge de følger de samme reglene.
- Peppol eDelivery bruker identifikatorer, oppslag og tillitsmekanismer for å sikre at dokumentet kommer fram til riktig mottaker på en kontrollert måte. Dette skiller det fra rene filoverføringsløsninger eller lukkede punkt-til-punkt-oppsett.
- Peppol eDelivery legger grunnlaget for bruk av dokumentstandarder, men er ikke det samme som dokumentformatene eller de nasjonale profilene. Det gjør det mulig å skille transportlaget fra innholdsstandardene.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Samhandlingsmønster for transport, adressering og tillit | Norsk myndighetsrolle alene |
| Regler og tekniske spesifikasjoner for deltakelse i nettverket | ELMA som egen nasjonal oppslagstjeneste |
| Føderert bruk av aksesspunkt, identifikatorer og oppslag | EHF som nasjonal innholdsstandard i seg selv |
| Internasjonalt økosystem for dokumentutveksling | Ett sentralt nasjonalt driftssystem eid av én norsk aktør |

## Veikart over kommende funksjonalitet
**Fakta:** OpenPeppol og de norske kildene viser løpende dokumentasjons- og regelverksforvaltning, men jeg fant ikke ett samlet offentlig roadmap-dokument for Peppol eDelivery i denne arbeidsøkten.

**Ikke offentlig verifisert i denne arbeidsøkten:** En samlet tidslinje for kommende endringer i hele økosystemet.

**Deduksjon:** Videreutviklingen skjer sannsynligvis gjennom oppdaterte transportspesifikasjoner, avtaler og dokumentprofiler heller enn gjennom et tradisjonelt produktroadmap.

## Forretningsverdi/Verdiforslag
### For virksomheter
- Gjør det mulig å delta i standardisert dokumentutveksling uten å avtale egen teknisk tilkobling med hver motpart.
- Gir større valgfrihet i leverandørmarkedet fordi flere aksesspunkt kan operere innenfor samme mønster.

### For marked og økosystem
- Støtter interoperabilitet på tvers av sektorer og landegrenser.
- Gjør det lettere å ta i bruk standardiserte dokumentformater og nasjonale profiler som EHF.

### For arkitektur og gjenbruk
- Gir et tydelig gjenbrukbart transportmønster som mange løsninger kan bygge videre på.
- Bidrar til å skille mellom internasjonalt rammeverk, nasjonale støttekomponenter og lokale forretningssystemer.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Ulike nasjonale krav og avtaleverk kan gjøre innføring mer krevende | Tydelige nasjonale veiledere og etterlevelse av Peppol-regelverk |
| Teknisk | Feil i aksesspunkt, oppslag eller profilstøtte kan gi avvist eller feilsendt dokument | Sertifisering, testregimer og dokumenterte spesifikasjoner |
| Sikkerhet | Tillitsmekanismer må fungere likt hos mange aktører | Sertifikater, avtaler og kontrollert deltakelse i nettverket |
| Forvaltning | Økosystemet kan misforstås som én tjeneste med én eier | Tydelig dokumentasjon av rollefordeling mellom OpenPeppol, DFØ, Digdir og leverandørmarkedet |
| Brukeropplevelse | Virksomheter kan tro at valg av Peppol automatisk løser alt rundt dokumentflyt og innhold | Klare avgrensninger mellom transport, oppslag, standarder og lokale prosesser |

## Kanaler
- OpenPeppol: https://peppol.org/
- OpenPeppol dokumentasjon: https://peppol.org/documentation/
- Peppol eDelivery-dokumentasjon: https://docs.peppol.eu/edelivery/
- EHF: https://www.anskaffelser.no/hva-skal-du-kjope/fagsystemer-digitale-anskaffelser/elektronisk-handelsformat-ehf
- Aksesspunkt: https://www.anskaffelser.no/verktoy/veiledere/aksesspunkt

## Plattform
Peppol eDelivery er ikke én sentral plattform, men et føderert meldingsøkosystem.

**Fakta:**
- OpenPeppol dokumentasjon beskriver en transportinfrastruktur med flere komponenter og roller.
- Norske kilder beskriver hvordan virksomheter kobler seg til gjennom aksesspunkt og hvordan nasjonale komponenter og myndighetsroller inngår i økosystemet.
- Nettverket er bygget slik at flere leverandører kan operere innenfor samme regelsett.

**Viktig avgrensning:** Peppol eDelivery er ikke det samme som ELMA, EHF eller én konkret leverandørtjeneste. Det er samhandlingsrammeverket som gjør at disse delene kan virke sammen.

## Gjenbruk
**Høy gjenbruksverdi som samhandlingsmønster:**
- Mange løsninger kan bruke samme transport- og adresseringsmønster.
- Ressursen reduserer behovet for bilaterale tilpasninger mellom hver avsender og mottaker.
- Gjenbruksverdien ligger i felles regelsett og interoperabilitet, ikke i at én aktør tilbyr én sentral tjeneste til alle.

## Støtter arkitekturprinsipper
- **P5 Del og gjenbruk løsninger** - Peppol eDelivery gir et felles mønster som mange aktører kan bruke i stedet for lokale spesialløsninger.
- **P6 Lag digitale løsninger som støtter samhandling** - ressursen er direkte rettet mot standardisert samhandling mellom virksomheter.
- **P7 Sørg for tillit til oppgaveløsningen** - tillitsmekanismer, identifikatorer og kontrollert deltakelse er grunnleggende for bruken.

## Finansiering
- **Ikke fullstendig offentlig dokumentert i brukte kilder:** Jeg fant ikke en enkel, samlet offentlig finansieringsmodell for hele Peppol eDelivery-økosystemet i denne arbeidsøkten.
- **Deduksjon:** Kostnader og finansiering er fordelt mellom OpenPeppol, nasjonale myndighetsaktører, Digdirs nasjonale støttekomponenter og private leverandører som driver aksesspunkt.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | OpenPeppol for det internasjonale rammeverket | OpenPeppol dokumentasjon |
| Driftsansvar | Føderert mellom sertifiserte aksesspunktleverandører og andre økosystemaktører | OpenPeppol dokumentasjon og norske EHF-kilder |
| Budsjettansvar | Ikke samlet offentlig spesifisert for hele økosystemet | Ikke verifisert som én modell i denne arbeidsøkten |
| Styringsmodell | OpenPeppol forvalter rammeverket, DFØ er norsk Peppol-myndighet og Digdir leverer den norske ELMA-komponenten | OpenPeppol dokumentasjon, EHF-kilder og Digdir-kilder |

## Lenke til dokumentasjon
- https://peppol.org/
- https://peppol.org/documentation/
- https://docs.peppol.eu/edelivery/
- https://www.anskaffelser.no/hva-skal-du-kjope/fagsystemer-digitale-anskaffelser/elektronisk-handelsformat-ehf
- https://www.anskaffelser.no/verktoy/veiledere/aksesspunkt

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/produkter/produktbeskrivelser/11-Peppol-eDelivery-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://peppol.org/ (hentet 2026-03-18)
- Nettkilde: https://peppol.org/documentation/ (hentet 2026-03-18)
- Nettkilde: https://docs.peppol.eu/edelivery/ (hentet 2026-03-18)
- Nettkilde: https://www.anskaffelser.no/hva-skal-du-kjope/fagsystemer-digitale-anskaffelser/elektronisk-handelsformat-ehf (hentet 2026-03-18)
- Nettkilde: https://www.anskaffelser.no/verktoy/veiledere/aksesspunkt (hentet 2026-03-18)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen bygger videre på `11-Peppol-eDelivery-produkt-canvas-v2-copilot.md`, men er omarbeidet mot offisielle OpenPeppol- og EHF-kilder.
- Ressursen er tydelig skilt fra ELMA, EHF-veiledning, sertifiseringsordninger og enkeltleverandører.
- Eier- og styringsbildet er ryddet slik at OpenPeppol, DFØ, Digdir og private aksesspunktleverandører har ulike roller i teksten.

### Tekstlige forbedringer
- Produktet er skrevet om som en selvstendig arkitekturbeskrivelse på samme nivå som andre ressurser i registeret.
- Kapabilitetene er strammet inn til de direkte koblingene som forklarer hvorfor ressursen er relevant.
- Teksten bruker aktiv form og forklarer tydelig at Peppol eDelivery er et føderert samhandlingsrammeverk, ikke én norsk felleskomponent.
