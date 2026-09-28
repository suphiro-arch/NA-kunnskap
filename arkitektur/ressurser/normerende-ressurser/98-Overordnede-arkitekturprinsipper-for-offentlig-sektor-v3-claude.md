# Overordnede arkitekturprinsipper for offentlig sektor

## Navn
Overordnede arkitekturprinsipper for offentlig sektor

## Ressurs ID
DIGDIR-030

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Prinsipper

## Status/Livsfase
Aktiv.

**Fakta:** Gjeldende versjon er 3.0, publisert 14. januar 2020, med engelsk versjon 22. juni 2020. Endringsloggen på digdir.no viser justeringer i lenker og ressurser under enkeltprinsipper fram til januar 2021, uten ny hovedversjon.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Om en revisjon av prinsippene er planlagt.

## Kort beskrivelse
Overordnede arkitekturprinsipper for offentlig sektor, i rundskrivet omtalt som de overordnede arkitekturprinsippene for digitalisering av offentlig sektor, er sju prinsipper som gir retning for hvordan digitale løsninger bør planlegges, styres, utvikles og forvaltes på tvers av virksomheter. Prinsippene er en støtte til arbeid med virksomhetsarkitektur og skal bidra til økt samhandlingsevne på tvers av virksomheter og sektorer.

Prinsippene binder lokale arkitekturvalg til felles mål. De gir virksomheter kriterier for å vurdere om et tiltak bare løser et lokalt behov, eller om det også bidrar til samhandling, gjenbruk og sammenhengende tjenester i offentlig sektor.

## Formål og normerende rolle
Formålet er å sikre at arkitekturbeslutninger tas med hensyn til helheten i offentlig sektor, ikke isolert i enkeltvirksomheter. Prinsippene skal støtte langsiktige valg som gir sammenhengende tjenester, mer effektiv datadeling, mer bærekraftig gjenbruk og større tillit.

Den normerende rollen er styrende for statlig sektor og anbefalt for kommunesektoren. Ressursen er ikke en operativ løsning eller detaljert metode, men et felles referansegrunnlag for analyse, styring, prioritering, kravstilling, kvalitetssikring og avviksbegrunnelse.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er **obligatorisk for statlig sektor** og **anbefalt for kommunesektoren**.

**Fakta:** Hjemmelen for statlig sektor er Digitaliseringsrundskrivet (D-2/25) punkt 1.11, fastsatt av Digitaliserings- og forvaltningsdepartementet: virksomheten skal følge den til enhver tid gjeldende versjonen av de overordnede arkitekturprinsippene, og må kunne dokumentere og begrunne eventuelle avvik. Rundskrivet gjelder departementene, statens ordinære forvaltningsorganer, forvaltningsorganer med særskilte fullmakter og forvaltningsbedrifter. Digdir fører prinsippene som `Krav` for stat og `Anbefaling` for kommune.

**Fakta:** Kravet gjelder prinsippene som helhet, men hvert prinsipp skiller selv mellom minimumskrav og ytterligere anbefalinger for etterlevelse. For prinsipp 2 er for eksempel 2.1–2.2 minimumskrav og 2.3–2.4 ytterligere anbefalinger.

**Deduksjon:** For statlige virksomheter er avvik tillatt, men må kunne dokumenteres og begrunnes. Rundskrivet sier ikke hvem avviksbegrunnelsen skal legges fram for, og det er ikke offentlig dokumentert i denne arbeidsøkten at det føres kontroll med etterlevelsen. Formuleringen «den til enhver tid gjeldende versjon» gjør at en ny versjon av prinsippene blir bindende uten at rundskrivet endres.

Etterlevelse skjer gjennom virksomhetsarkitektur, porteføljestyring, konseptvalg, anskaffelser og kvalitetssikring i prosjektløp.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot prinsippene på digdir.no og Digitaliseringsrundskrivet punkt 1.11.

`Standardisering: Forvaltningsstandarder` er tatt ut. Prinsipp 6 ber om bruk av standarder, men plikten til å ta i bruk nasjonale standarder følger av forskrift om IT-standarder i offentlig forvaltning og av Referansekatalogen, ikke av prinsippene. `Juridisk samhandling: Regelverksutvikling` er vurdert og ikke satt: prinsipp 3 ber virksomheter bidra til digitaliseringsvennlig regelverk, men veiledningen for hvordan det gjøres, ligger i Digitaliseringsvennlig regelverk. `Regelverkstolkning` er heller ikke satt, fordi prinsippene ikke tolker regelverk.

- **Strategisk styring: Arkitekturstyring**
  Prinsippene er de felles arkitekturprinsippene kapabiliteten bygger på, og rundskrivet gjør dem forpliktende for statlig sektor med krav om begrunnede avvik. Kapabilitetsdefinisjonen nevner selv oppfølging av arkitekturkravene i Digitaliseringsrundskrivet, og det er dette kravet prinsippene utgjør.
- **Veiledning: Utvikling og formidling av veiledning**
  Prinsippene er publisert veiledning av den typen hovedkapabiliteten nevner uttrykkelig: omforente prinsipper for hvordan løsninger skal bygges. Hvert prinsipp har begrunnelse, anbefalinger for etterlevelse og lenker til veiledning og ressurser.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Statlige virksomheter | Oppfylle kravet i rundskrivet | Virksomhetsarkitektur, konseptvalg og avviksbegrunnelse | Obligatorisk |
| Kommuner og fylkeskommuner | Felles retning for arkitekturvalg | Virksomhetsarkitektur og samhandling med staten | Anbefalt |
| Ledelse og porteføljestyring | Felles kriterier for prioritering og avvik | Styring, investering og porteføljeoppfølging | Bør brukes før beslutning om løsningsretning |
| Arkitekter og fagansvarlige | Felles prinsipper og kvalitetsgrunnlag | Arkitekturvurderinger, målbilder og kvalitetssikring | Kjernebrukere |
| Prosjekt- og produktmiljøer | Føringer for krav, design og samhandling | Konseptvalg, anskaffelser og utviklingsløp | Bør kobles til konkrete krav og akseptansekriterier |

## Normerende innhold
**Fakta:** Ressursen består av sju prinsipper:

1. **Ta utgangspunkt i brukernes behov:** offentlige tjenester skal ta utgangspunkt i brukernes behov og perspektiver og kunne brukes av alle.
2. **Ta arkitekturbeslutninger på rett nivå:** beslutninger bør tas så nær oppgaveløsningen som mulig, men enkelte må løftes for å øke samhandlingsevnen og ivareta felles mål.
3. **Bidra til digitaliseringsvennlige regelverk:** regelverk må videreutvikles kontinuerlig slik at det er tilpasset dagens og morgendagens muligheter.
4. **Del og gjenbruk data:** virksomheter skal legge til rette for deling og gjenbruk av data.
5. **Del og gjenbruk løsninger:** omfatter arkitekturprodukter, løsningskomponenter og tjenester.
6. **Lag digitale løsninger som støtter samhandling:** løsninger skal kunne samhandle med andre løsninger i offentlig og privat sektor.
7. **Sørg for tillit til oppgaveløsningen:** innbyggere, næringsliv og frivillige organisasjoner skal ha tillit til at offentlige virksomheter løser oppgavene på en god og sikker måte.

Hvert prinsipp har en egen side med begrunnelse, nummererte anbefalinger for etterlevelse delt i minimumskrav og ytterligere anbefalinger, og veiledning og ressurser.

Prinsippene gir et felles språk for arkitekturkvalitet. De kan brukes til å stille spørsmål som:
- Hvilke brukerbehov og tjenestekjeder påvirkes av tiltaket?
- Hvilke beslutninger må tas lokalt, sektorvis eller nasjonalt?
- Hindrer regelverk, organisering eller finansiering digital samhandling?
- Hvilke data og løsninger kan deles eller gjenbrukes?
- Hvordan ivaretas tillit, sikkerhet og etterlevelse?
- Hvilke avvik er nødvendige, og hvordan begrunnes de?

## Bruksområde
Prinsippene bør brukes i tidligfase, konseptutredning, målarkitektur, porteføljestyring, anskaffelser og styringsdialog når tiltak skal vurderes opp mot samhandling, datadeling, gjenbruk og tillit. For statlige virksomheter er de også grunnlaget for å dokumentere og begrunne avvik etter rundskrivet.

De er særlig aktuelle der flere aktører påvirkes av samme valg, der lokale beslutninger kan gi følger for andre, eller der tiltaket kan skape varig teknisk, organisatorisk eller juridisk gjeld.

## Typiske analyse- og beslutningssituasjoner
- Når flere alternative løsningsretninger skal vurderes.
- Når styringsgruppe eller portefølje trenger kriterier for prioritering.
- Når kravgrunnlag for anskaffelser skal utformes.
- Når en statlig virksomhet vurderer å avvike fra prinsippene og må dokumentere begrunnelsen.
- Når et lokalt tiltak kan påvirke tverrsektoriell samhandling eller nasjonale fellesløsninger.

## Når ressursen normalt ikke er tilstrekkelig alene
Ressursen er ikke tilstrekkelig alene for detaljert implementasjon eller metodisk gjennomføring. Den må suppleres med:
- Rammeverk for digital samhandling
- Referansekatalogen for IT-standarder og forskrift om IT-standarder
- referansearkitekturer for eMelding og eOppslag
- veiledere for sammenhengende tjenester, informasjonsforvaltning og digitaliseringsvennlig regelverk
- virksomhetens egne styringsprosesser og beslutningsfora

## Scope og avgrensning
Inngår:
- sju overordnede prinsipper for digitalisering av offentlig sektor
- begrunnelse og anbefalinger for etterlevelse per prinsipp, delt i minimumskrav og ytterligere anbefalinger
- lenker til veiledning og ressurser per prinsipp

Inngår ikke:
- detaljert metode for prosjektgjennomføring
- tekniske spesifikasjoner for enkeltløsninger
- valg av standarder, som reguleres av forskrift om IT-standarder og Referansekatalogen
- prosess for behandling av avviksbegrunnelser

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | **Fakta:** Digdir forvalter prinsippene i overensstemmelse med departementet. Siden oppgir fortsatt Kommunal- og moderniseringsdepartementet, som var ansvarlig departement da versjon 3.0 kom |
| Endringsprosess | **Fakta:** Prinsippene er forankret i Arkitektur- og standardiseringsrådet og Skates arbeidsutvalg. Ved vesentlige endringer gjennomføres offentlig høring. Endringslogg og tidligere versjoner i pdf publiseres på digdir.no |
| Publiserings- og beslutningsarena | digdir.no for prinsippene. Forpliktelsen fastsettes av Digitaliserings- og forvaltningsdepartementet i Digitaliseringsrundskrivet |

## Relasjon til andre ressurser
- **Digitaliseringsrundskrivet (`DIGDIR-044`):** hjemmelen som gjør prinsippene obligatoriske for statlig sektor, i punkt 1.11.
- **Arkitektur- og standardiseringsrådet (`DIGDIR-028`) og Skate (`DIGDIR-042`):** arenaene prinsippene er forankret i.
- **Rammeverk for digital samhandling (`DIGDIR-025`):** operasjonaliserer samhandlingsprinsippet og anbefales i samme punkt i rundskrivet.
- **Referansekatalogen for IT-standarder (`DIGDIR-026`) og forskrift om IT-standarder i offentlig forvaltning (`DIGDIR-060`):** regulerer standardvalget som prinsipp 6 forutsetter.
- **Digitaliseringsvennlig regelverk (`DIGDIR-047`):** veiledning for prinsipp 3.
- **Rammeverk for informasjonsforvaltning (`DIGDIR-029`) og Rammeverk for Nasjonale grunndata (`DIGDIR-037`):** operasjonaliserer prinsipp 4. Grunndatarammeverket følger formen til prinsippene i sin egen prinsippdel.
- **Prosjektveiviseren (`DIGDIR-045`):** støtter innarbeiding av prinsippene i prosjekt- og anskaffelsesløp.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er bedre styring, mer sammenlignbare beslutninger og lavere risiko for feilinvesteringer. Prinsippene gjør det lettere å begrunne hvorfor tiltak bør bruke fellesløsninger, dele data, samordne seg eller avklare regelverk før utvikling.

Arkitekturverdien er redusert fragmentering, sterkere samhandlingsevne og tydeligere kvalitet i løsninger som går på tvers av virksomheter. Kravet om dokumenterte avvik gjør avveiingene synlige.

## Konsekvens ved manglende bruk eller avvik
Hvis prinsippene ikke brukes, brukes for sent eller tolkes for generelt, øker risikoen for:
- lokale særvalg som svekker samhandling
- høyere integrasjonskostnader og mer teknisk gjeld
- svakere brukeropplevelse på tvers av tjenester
- manglende gjenbruk av data og løsninger
- ubegrunnede avvik, som for statlige virksomheter er brudd på rundskrivet

Avvik kan være riktig i konkrete tilfeller, men for statlige virksomheter må de dokumenteres og begrunnes.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Forankring | Prinsippene brukes for sent eller bare som etterpåklok dokumentasjon | Lav effekt på reelle valg | Ta dem inn i tidligfase, porteføljestyring og beslutningsgrunnlag |
| Tolkning | Ulik forståelse på tvers av virksomheter | Ujevne avviksbegrunnelser | Bruke minimumskravene per prinsipp som felles vurderingsgrunnlag |
| Endringsstyring | Versjon 3.0 er fra 2020, og forvaltningssiden viser til et departement som ikke lenger har ansvaret | Usikkerhet om prinsippene er oppdatert mot nyere strategi og regelverk | Følge med på endringsloggen; en ny versjon blir bindende uten endring i rundskrivet |
| Etterlevelse | Det er ikke dokumentert hvem som følger opp avviksbegrunnelser | Kravet får svak konsekvens | Knytte avvik til porteføljestyring og styringsdialog |
| Balansering | Prinsipper kan trekke i ulike retninger i konkrete saker | Uklare beslutninger | Gjøre avveiingen eksplisitt, særlig mellom brukerbehov, gjenbruk, tillit og kostnad |

## Publiseringsform og tilgjengelighet
Prinsippene publiseres åpent på digdir.no, med én side per prinsipp, en side om føringer for bruk og en side med endringshistorikk og tidligere versjoner i pdf. Engelsk versjon finnes.

## Støtter arkitekturprinsipper
Ressursen er selve prinsippgrunnlaget som `arkitektur/prinsipper/principles.md` bygger på, og dekker derfor alle sju:
- **P1: Ta utgangspunkt i brukernes behov**
- **P2: Ta arkitekturbeslutninger på rett nivå**
- **P3: Bidra til digitaliseringsvennlige regelverk**
- **P4: Del og gjenbruk data**
- **P5: Del og gjenbruk løsninger**
- **P6: Lag digitale løsninger som støtter samhandling**
- **P7: Sørg for tillit til oppgaveløsningen**

Svakheter og spenninger: Prinsippene gir ikke alene tilstrekkelig beslutningsstøtte uten kobling til standarder, referansearkitekturer og styringsarenaer, og de kan trekke i ulike retninger i en konkret sak. Kravet om dokumenterte avvik gjelder bare statlig sektor. I tiltak på tvers av stat og kommune kan partene derfor være bundet ulikt av de samme prinsippene.

## Lenke til dokumentasjon
- https://www.digdir.no/digital-samhandling/overordnede-arkitekturprinsipper/1065
- https://www.digdir.no/digital-samhandling/endringshistorikk-og-versjonslogg/1070
- https://www.digdir.no/krav-og-anbefalinger/folg-dei-overordna-arkitekturprinsippa/3074
- https://www.regjeringen.no/no/dokumenter/digitaliseringsrundskrivet/id3103320/

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-09-25
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-25
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-25
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/overordnede-arkitekturprinsipper/1065 , kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/prinsipp-2-ta-arkitekturbeslutninger-pa-rett-niva/1056 , kontrollert 2026-09-25 som eksempel på oppbygningen av prinsippsidene
- https://www.digdir.no/digital-samhandling/endringshistorikk-og-versjonslogg/1070 , kontrollert 2026-09-25
- https://www.digdir.no/krav-og-anbefalinger/folg-dei-overordna-arkitekturprinsippa/3074 , kontrollert 2026-09-25
- https://www.digdir.no/krav-og-anbefalinger/krav-og-anbefalingar-innan-digitalisering/2617 , kontrollert 2026-09-25
- https://www.regjeringen.no/no/dokumenter/digitaliseringsrundskrivet/id3103320/ , Digitaliseringsrundskrivet D-2/25 punkt 1.11, kontrollert 2026-09-25

## Endringer fra forrige versjon

### Analyseforbedringer
- Forpliktelsesnivået er rettet etter regelen fra 2026-09-13. `v2` kalte prinsippene «primært styrende/anbefalt» og skrev at avvik «bør begrunnes». Kildene viser at prinsippene er obligatoriske for statlig sektor etter Digitaliseringsrundskrivet punkt 1.11, med krav om dokumenterte og begrunnede avvik, og anbefalte for kommunesektoren. Hjemmelen er oppgitt med navn og punkt.
- `Status/Livsfase` oppgir nå versjon 3.0 fra 14. januar 2020 og endringsloggen. `v2` hadde ingen versjon.
- `Forvaltningsmodell` bygger nå på Digdirs egen forvaltningsside: forankring i Arkitektur- og standardiseringsrådet og Skates arbeidsutvalg, og offentlig høring ved vesentlige endringer. `v2` hadde en usikkerhetsmerknad om at dette ikke var kontrollert.
- `Normerende innhold` gjengir nå de sju prinsippene og oppbygningen av prinsippsidene, med skillet mellom minimumskrav og ytterligere anbefalinger.
- `Standardisering: Forvaltningsstandarder` er tatt ut etter regelen fra 2026-09-25 om at å nevne et tema ikke er å realisere kapabiliteten. `Veiledning: Utvikling og formidling av veiledning` er lagt til etter regelen fra samme dag. Kapabilitetspunktene har fått fullt navn, og vurderingen av `Juridisk samhandling` er skrevet ut.
- `Relasjon til andre ressurser` har fått ressurs-ID-er. Digitaliseringsrundskrivet, Skate, forskrift om IT-standarder, Digitaliseringsvennlig regelverk og Rammeverk for Nasjonale grunndata er lagt til, og dubletten av Rammeverk for digital samhandling er fjernet. Kapabilitetsmodellen er tatt ut som relasjon fordi den ikke er omtalt i kildene om prinsippene.
- Risikotabellen har fått rader om at versjonen er fra 2020 og om at oppfølging av avvik ikke er dokumentert.

### Tekstlige forbedringer
- Formuleringen «Ressursen er særlig viktig fordi» og setningen om hvordan prinsippene bør brukes «i analyser» er fjernet, fordi de begrunner verdien framfor å beskrive ressursen.
- Den tomme `**Fakta:**`-merknaden i `Status/Livsfase` om at prinsippene må brukes sammen med andre ressurser er flyttet til `Når ressursen normalt ikke er tilstrekkelig alene`, der den hører hjemme.
- Den gjentatte begrunnelsen per prinsipp under `Støtter arkitekturprinsipper` er fjernet, siden prinsippene er gjengitt i `Normerende innhold`.
