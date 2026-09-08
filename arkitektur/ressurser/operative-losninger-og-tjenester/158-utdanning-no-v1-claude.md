# Produkt-canvas: utdanning.no

## Navn
utdanning.no

## Ressurs ID
HKDIR-001

## Status/Livsfase
**Produksjon** — etablert nasjonal nettportal i løpende drift, med redaksjonelt vedlikeholdt innhold og publiserte API-er.

**Fakta:** Tjenesten eies av Kunnskapsdepartementet og forvaltes av Direktoratet for høyere utdanning og kompetanse. Innholdet omfatter beskrivelser av rundt 600 yrker og over 350 utdanninger, og deler av datagrunnlaget er publisert som åpne data under NLOD.

## Modenhet
**Høy modenhet** — tjenesten har avklart eierskap, stabilt redaksjonelt apparat og et datagrunnlag som er beskrevet, versjonert og gjort tilgjengelig for andre.

- Eierskapet ligger hos Kunnskapsdepartementet, og forvaltningen hos HK-dir. Rollefordelingen er dokumentert på direktoratets egne sider.
- Yrkesbeskrivelsene kvalitetssikres jevnlig av over 200 organisasjoner i arbeidslivet, ifølge datasettbeskrivelsen i Felles datakatalog.
- Innholdet er klassifisert mot etablerte nasjonale standarder: STYRK-98 og STYRK-08 for yrker og NUS for utdanning.
- Beskrivelsene har persistente identifikatorer, og API-ene er publiserte og dokumentert i Felles datakatalog med NLOD som lisens.

**Deduksjon:** Modenheten er høy både som innbyggerflate og som datakilde. Den svakeste siden er at tjenesten er avhengig av at andre aktører leverer og oppdaterer opptaks-, tilbuds- og arbeidsmarkedsdata, siden utdanning.no i stor grad sammenstiller framfor å eie kildedataene selv.

## Kort beskrivelse
utdanning.no er den nasjonale nettportalen for informasjon om utdanning og yrker. Tjenesten samler kvalitetssikrede beskrivelser av det norske utdanningstilbudet og av yrkene utdanningene leder til, og kobler dette til data om lønn, arbeidsledighet og arbeidsmarkedsutvikling.

Tjenesten har tre lag. Det første er redaksjonelt innhold: yrkesbeskrivelser, utdanningsbeskrivelser og en visualisering av utdanningssystemet. Det andre er beslutningsverktøy — karakterkalkulator, interessevelger, studievelger, fagskolevelger og sammenligning av yrker på lønn og arbeidsledighet. Det tredje er et sett åpne API-er som gjør at andre tjenester kan gjenbruke innholdet framfor å skrive sine egne yrkes- og utdanningsbeskrivelser.

For elever i ungdomsskolen og videregående er tjenesten den nasjonale flaten for å orientere seg om hva et utdanningsvalg faktisk fører til. Den brukes også av karriereveiledere som arbeidsverktøy, og av utviklere som datakilde.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over begreper**
  Tjenesten forvalter et redaksjonelt begrepsapparat for yrker og utdanninger med persistente identifikatorer, klassifisert mot STYRK og NUS.
- **Datakilder: Åpne data**
  Yrkes- og utdanningsbeskrivelsene er publisert som åpne data under NLOD, med dokumenterte API-er i Felles datakatalog.
- **Datadrevet: Sammenstilling av data**
  Tjenesten kobler redaksjonelt innhold med arbeidsmarkedsdata, lønnsdata og opptaksdata, slik at et utdanningsvalg kan vurderes mot utfall.
- **Sluttbrukertjenester: Sammenhengende tjenester**
  Utdanningstilbud, opptakskrav, yrkesutfall og veiledning samles i én flate, uavhengig av hvilket organ som forvalter hvilken del.

## Produktmål
Dokumenterte mål:
- Være nasjonal nettportal for informasjon om utdanning og yrke, med oversikt over det norske utdanningstilbudet.
- Gi offentlig og kvalitetssikret informasjon om utdanninger og om yrkene de leder til.
- Gjøre innholdet tilgjengelig som åpne data under NLOD.

Operative mål utledet fra kildene:
- Gjøre konsekvensen av et utdanningsvalg synlig ved å koble utdanning til yrke, lønn og arbeidsmarked.
- Redusere behovet for at hver enkelt aktør skriver egne yrkes- og utdanningsbeskrivelser.
- Støtte karriereveiledningen med et felles faktagrunnlag framfor lokale framstillinger.

## Brukerbehov
- Elever og unge trenger å forstå hva et utdanningsvalg fører til, ikke bare hvilke tilbud som finnes.
- Elever trenger å vite om de har poeng nok, og hvilke veier som er mulige med karakterene de har.
- Karriereveiledere trenger et oppdatert og felles faktagrunnlag de kan bruke i veiledningssamtaler.
- Voksne som vurderer omskolering trenger å se sammenhengen mellom utdanning og arbeidsmarked.
- Andre offentlige og private tjenester trenger å kunne gjenbruke yrkes- og utdanningsbeskrivelser uten å produsere dem selv.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Elever i ungdomsskolen | Forstå hvilke utdanningsprogram som finnes og hva de leder til | Faget utdanningsvalg og forberedelse til søknad om videregående | Møter tjenesten før de søker i `vigo.no` |
| Elever i videregående | Se poengkrav, studieveier og yrkesutfall | Valg av programfag og videre utdanning | Karakterkalkulator og studievelger er sentrale verktøy |
| Voksne søkere og omstillingssøkende | Se hvilke utdanningsveier som er åpne, og hva arbeidsmarkedet ser ut som | Vurdering av omskolering og videreutdanning | Bredere målgruppe enn barn og unge |
| Karriereveiledere og rådgivere | Felles og oppdatert faktagrunnlag | Veiledningssamtaler i skole og karrieresenter | Tjenesten er arbeidsverktøy, ikke bare oppslagsverk |
| Utdanningsinstitusjoner | Bli synlige med korrekt tilbudsinformasjon | Presentasjon av eget utdanningstilbud | Leverer data inn i tjenesten |
| Utviklere og datakonsumenter | Maskinlesbare beskrivelser med stabile identifikatorer | Integrasjon i egne veilednings- og søketjenester | Bruker API-ene under NLOD |
| Arbeidslivets organisasjoner | Riktig framstilling av yrkene de representerer | Kvalitetssikring av yrkesbeskrivelser | Over 200 organisasjoner bidrar i kvalitetssikringen |

## Hovedfunksjoner

### Primære funksjoner
Tjenesten forvalter og publiserer redaksjonelle beskrivelser av yrker og utdanninger. Hver beskrivelse har en persistent identifikator og er klassifisert mot nasjonale standarder, slik at innholdet kan kobles til statistikk og til andre datakilder framfor å stå isolert som løpende tekst.

Tjenesten sammenstiller redaksjonelt innhold med data om lønn, arbeidsledighet og geografisk arbeidsmarkedsutvikling. Det er denne koblingen som skiller utdanning.no fra et rent tilbudsregister: brukeren ser ikke bare hvilke utdanninger som finnes, men hva de statistisk sett fører til.

Tjenesten tilbyr beslutningsverktøy som opererer på dette grunnlaget. Karakterkalkulatoren regner ut poeng og viser hvilke studier som er innenfor rekkevidde. Interessevelgeren går motsatt vei og kobler interesser til utdanninger og yrker. Studievelger, fagskolevelger og sammenligningstjenesten støtter mer avgrensede valg.

Tjenesten publiserer datagrunnlaget som åpne API-er. Yrkesbeskrivelser og utdanningsbeskrivelser er beskrevet som datasett i Felles datakatalog, lisensiert under NLOD, og tilgjengelige i JSON uten avtale eller autentisering.

### Typiske brukssituasjoner (generisk)
- En elev i tiende klasse skal velge utdanningsprogram og trenger å vite hva de ulike programmene leder til.
- En elev i Vg3 vil vite om poengsummen holder til et bestemt studium.
- En rådgiver forbereder en veiledningssamtale og trenger oppdatert informasjon om et yrke.
- En kommune eller en organisasjon skal bygge en egen veiledningstjeneste og vil gjenbruke yrkesbeskrivelsene framfor å skrive dem.
- En analytiker skal koble utdanningsdata til yrkesklassifikasjon og trenger en mapping mot STYRK og NUS.

### Når utdanning.no normalt ikke er førstevalg
- Når behovet er å søke om skoleplass. Søknaden skjer i `vigo.no` for videregående og i Samordna opptak for høyere utdanning.
- Når behovet er de fylkesspesifikke detaljene om videregående opplæring. `vilbli.no` er den flaten som dekker dette.
- Når behovet er læreplanverket, fagkoder eller opplæringstilbud som normerende grunnlag. Da er `Grep` kilden.
- Når behovet er autoritative registerdata om skoler og barnehager. Da er de nasjonale registrene for barnehage og grunnopplæring kilden.
- Når behovet er offisiell statistikk om høyere utdanning. Da er DBH hos HK-dir den direkte kilden.

### Scope og avgrensning
Inngår:
- Redaksjonelle beskrivelser av yrker og utdanninger, med klassifisering og persistente identifikatorer.
- Sammenstilling av arbeidsmarkeds- og lønnsdata knyttet til yrker.
- Beslutningsverktøy for utdanningsvalg og poengberegning.
- Åpne API-er for gjenbruk av beskrivelsene.
- Henvisning til karriereveiledning gjennom chat, telefon og karrieresentrene.

Inngår ikke:
- Søknadsbehandling, opptak og tildeling av skoleplass eller studieplass.
- Forvaltning av læreplaner og fagkoder.
- Autoritativ registerføring av utdanningsvirksomheter.
- Formell godkjenning av utenlandsk utdanning, som er en egen HK-dir-oppgave utenfor denne tjenesten.

## Veikart over kommende funksjonalitet
**Fakta:** Jeg fant ikke et offentlig, tidsfestet veikart for utdanning.no i kildene brukt i denne arbeidsøkten.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Planlagte funksjonsutvidelser, tidsplaner for nye datasett, og om og når klassifiseringen skal mappes mot europeiske rammeverk som ESCO.

## Forretningsverdi/Verdiforslag
- For elever og unge: valget blir mindre tilfeldig. Sammenhengen mellom utdanning, yrke og arbeidsmarked blir synlig på ett sted, i stedet for å måtte settes sammen fra spredte kilder.
- For skolen og karriereveiledningen: et felles faktagrunnlag som gjør veiledningen mindre avhengig av den enkelte rådgiverens oversikt.
- For utdanningsinstitusjonene: én nasjonal flate der tilbudet blir synlig for søkere som ennå ikke har valgt institusjon.
- For andre tjenesteutviklere: ferdig kvalitetssikret innhold under NLOD, som fjerner et betydelig redaksjonelt arbeid fra egne prosjekter.
- For samfunnet: bedre informerte utdanningsvalg reduserer feilvalg og frafall, som er en direkte kostnad både for den enkelte og for det offentlige.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Datakvalitet | Tjenesten sammenstiller data den ikke eier. Feil eller forsinkelser hos leverandørene av opptaks- og arbeidsmarkedsdata slår ut i brukerflaten | Redaksjonell kvalitetssikring og klassifisering mot standarder gir sporbarhet, men fjerner ikke avhengigheten |
| Aktualitet | Yrkesbeskrivelser kan bli utdaterte når arbeidsmarkedet endrer seg raskere enn den redaksjonelle syklusen | Kvalitetssikring med over 200 organisasjoner i arbeidslivet er tiltaket kildene beskriver |
| Brukeropplevelse | Karakterkalkulator og poengberegning kan oppfattes som en garanti, ikke et anslag | Forutsetter tydelig framstilling av at beregningen er veiledende |
| Semantisk avstand | Klassifiseringen bruker nasjonale standarder (STYRK, NUS). Kobling mot europeiske rammeverk for yrker og kvalifikasjoner er ikke dokumentert i kildene | Uavklart. Blir relevant hvis norske kvalifikasjonsdata skal utveksles over landegrenser |
| Fragmentert utdanningsløp | Informasjon, søknad og støtte ligger i tre forskjellige tjenester med forskjellige eiere | Tjenesten henviser videre, men eier ikke helheten |

## Kanaler
- Nettstedet https://utdanning.no/ som primærkanal, tilgjengelig uten innlogging.
- Åpne API-er under https://utdanning.no/api/ for maskinell tilgang.
- Karriereveiledning gjennom chat og telefon, og henvisning videre til karrieresentrene i fylkene.
- Datasettbeskrivelser og API-referanser publisert i Felles datakatalog.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten.** Kildene beskriver ikke driftsplattform, skylokasjon eller teknisk arkitektur for tjenesten. Tjenesten er tilgjengelig som offentlig nettsted med publiserte JSON-API-er.

## Gjenbruk
**Høy gjenbruksverdi:**
- Yrkes- og utdanningsbeskrivelsene er publisert som åpne data under NLOD, uten krav om avtale eller autentisering.
- Beskrivelsene har persistente identifikatorer, slik at eksterne løsninger kan referere stabilt til dem over tid.
- Klassifiseringen mot STYRK-98, STYRK-08 og NUS gjør innholdet koblingsbart mot offisiell statistikk og andre registre.
- API-ene er beskrevet i Felles datakatalog og leverer JSON, som gjør terskelen for gjenbruk lav.

**Vanlige kombinasjoner med andre produkter:**
- `Grep` (`UDIR-001`) forvalter læreplanverket og fagkodene som utdanning.no beskriver i redaksjonell form.
- `vilbli.no` (`NOVARI-010`) dekker de fylkesspesifikke detaljene om videregående opplæring som utdanning.no ikke går inn i.
- `vigo.no` (`NOVARI-009`) er søknadsflaten som følger etter informasjonsinnhentingen på utdanning.no.
- `Utdanningsstøtte fra Lånekassen` (`LANE-001`) er ordningen som avgjør om et utdanningsvalg er økonomisk mulig.
- `ung.no` (`BUFDIR-002`) dekker det bredere informasjonsbehovet hos ungdom og henviser videre til utdanningsvalget.
- `Felles datakatalog` (`DIGDIR-011`) der datasettene og API-ene er beskrevet.

**Kildekode:** Ikke offentlig dokumentert. Kildene beskriver ikke om nettstedets eller API-enes kode er publisert. Innholdet er derimot åpne data under NLOD 2.0.

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov**
  Tjenesten er organisert etter valget brukeren står i, ikke etter hvilket organ som forvalter hvilken del av utdanningssystemet.
- **P4: Del og gjenbruk data**
  Datagrunnlaget er publisert som åpne data under NLOD, beskrevet i Felles datakatalog og utstyrt med persistente identifikatorer.
- **P5: Del og gjenbruk løsninger**
  Én nasjonal flate for utdannings- og yrkesinformasjon framfor at hver aktør bygger sin egen.
- **P6: Lag digitale løsninger som støtter samhandling**
  Støttes delvis. Tjenesten sammenstiller data fra flere sektorer, men koblingen til søknads- og støtteløsningene skjer ved henvisning, ikke ved dataflyt.

Spenning og begrensning: tjenesten er sterk på informasjon og svak på handling. Den forteller eleven hva et valg fører til, men når valget skal gjennomføres, må hen over i `vigo.no` eller Samordna opptak og deretter til Lånekassen. Utdanningsløpet er dermed sammenhengende i informasjonen og oppstykket i utførelsen. Klassifiseringen er en styrke nasjonalt, men bindingen til STYRK og NUS uten dokumentert mapping mot europeiske rammeverk gjør at kvalifikasjonsdata ikke uten videre kan forstås utenfor Norge.

## Finansiering
Tjenesten forvaltes av HK-dir som del av direktoratets ordinære virksomhet, med Kunnskapsdepartementet som eier. Kildene beskriver ikke en egen finansieringsmodell for tjenesten.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Eierskap | Kunnskapsdepartementet | Omtalt som eier av tjenesten |
| Produkt- og redaksjonelt ansvar | Direktoratet for høyere utdanning og kompetanse | hkdir.no |
| Utgiver av datasettene | Direktoratet for høyere utdanning og kompetanse | Felles datakatalog |
| Kvalitetssikring av yrkesbeskrivelser | Over 200 organisasjoner i arbeidslivet | Datasettbeskrivelse i Felles datakatalog |
| Driftsansvar | Ikke offentlig dokumentert i denne arbeidsøkten | — |
| Styringsmodell | Ikke offentlig dokumentert i denne arbeidsøkten | — |

## Lenke til dokumentasjon
- https://utdanning.no/
- https://hkdir.no/ressurser/utdanning-no
- https://utdanning.no/api/v1/data_norge--yrkesbeskrivelse
- https://utdanning.no/api/v1/data_norge--utdanningsbeskrivelse
- https://data.norge.no/nb/datasets/7bf25d6c-d25d-3d68-b721-86ddd512bfbe/yrkesbeskrivelser-fra-utdanningno
- https://data.norge.no/en/datasets/eff568d2-8409-48f6-824c-cd93f42fa3ac/utdanningsbeskrivelser-fra-utdanningno

## Kildegrunnlag brukt i utfyllingen
- https://utdanning.no/, kontrollert 2026-09-08
- https://hkdir.no/ressurser/utdanning-no, kontrollert 2026-09-08
- https://data.norge.no/en/datasets/eff568d2-8409-48f6-824c-cd93f42fa3ac/utdanningsbeskrivelser-fra-utdanningno, kontrollert 2026-09-08
- https://data.norge.no/nb/datasets/7bf25d6c-d25d-3d68-b721-86ddd512bfbe/yrkesbeskrivelser-fra-utdanningno, kontrollert 2026-09-08
- `arkitektur/ressurser/normerende-ressurser/151-Grep-v1-claude.md`, kontrollert 2026-09-08
- `arkitektur/ressurser/operative-losninger-og-tjenester/154-vilbli-no-v1-claude.md`, kontrollert 2026-09-08
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-08
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-08
