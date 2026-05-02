# Produkt-canvas: Norsk pasientregister (NPR)

## Navn
Norsk pasientregister (NPR)

## Ressurs ID
FHI-005

## Status/Livsfase
**Produksjon** - etablert nasjonalt helseregister for spesialisthelsetjenesten.

**Fakta:** FHI beskriver Norsk pasientregister som registeret som inneholder helseopplysninger om alle personer som har fått behandling, eller som venter på behandling i spesialisthelsetjenesten. Registeret er hjemlet i Norsk pasientregisterforskriften (2007).

## Modenhet
**Høy modenhet** - langvarig og innarbeidet nasjonalt helseregister:
- Alle offentlige helseforetak og private aktører i den offentlige spesialisthelsetjenesten har rapporteringsplikt til NPR.
- Registeret brukes som grunnlag for administrasjon, styring, finansiering og kvalitetssikring av spesialisthelsetjenesten.
- Data er tilgjengelige for forskning via søknad gjennom Helsedataservice.
- Statistikk og rapporter publiseres løpende av FHI.

**Presisering for NA-vurdering:** NPR er viktig og nasjonalt, men den primære verdien er innen spesialisthelsetjenesten. Tversgående verdi for nasjonal arkitektur gjelder særlig der registeret støtter styring og analyse på tvers av nivåer, ikke som generell felleskomponent.

## Kort beskrivelse
Norsk pasientregister (NPR) er det nasjonale registeret over alle pasienter som har fått eller venter på behandling i spesialisthelsetjenesten i Norge. Registeret samler opplysninger om pasienter, behandlende institusjoner, diagnoser, prosedyrer, pasientrettigheter, ventetider og kostnader, og er den sentrale datakilden for styring, finansiering, kvalitetssikring og forskning innen spesialisthelsetjenesten.

I arkitektursammenheng er NPR relevant når behov gjelder analyse, styring og samordning på tvers av helseforetak og mellom stat og sektor, men ressursen er avgrenset til spesialisthelsetjenestens domene og er ikke en bred tverrsektoriell felleskomponent.

## Kapabiliteter
- **Datakilder: Grunndata**
  NPR er den autoritative nasjonale datakilden for opplysninger om aktivitet og pasienter i spesialisthelsetjenesten.
- **Datautveksling og integrasjon: Dele data med andre**
  Registeret gjør opplysninger tilgjengelige for forskning, analyse og styring gjennom kontrollerte tilgangskanaler.
- **Informasjonsforvaltning: Datastyring**
  NPR understøtter nasjonal styring og finansiering av spesialisthelsetjenesten gjennom systematisk innsamling og forvaltning av aktivitetsdata.

## Produktmål
**Primærkilder:** FHIs side `Om NPR` (kontrollert 2026-05-03).

Dokumenterte mål:
- Gi grunnlag for administrasjon, styring, finansiering og kvalitetssikring av spesialisthelsetjenesten.
- Brukes som grunnlag for medisinsk og helsefaglig forskning.
- Danne grunnlag for etablering og kvalitetssikring av sykdoms- og kvalitetsregistre.
- Avgi informasjon til kjernejournalen.
- Bidra til kunnskap som forebygger ulykker og skader.

## Brukerbehov
- Helsemyndigheter og regionale helseforetak trenger et autoritativt datagrunnlag for styring, finansiering og planlegging av spesialisthelsetjenesten.
- Forskningsmiljøer trenger tilgang til nasjonale pasientdata for medisinsk og helsefaglig forskning.
- Statistikk- og analysemiljøer trenger systematiske data for rapportering og oppfølging av tjenestekvalitet.
- Innbyggere trenger innsyn i egne opplysninger registrert i NPR.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Helsemyndigheter og HOD | Styring, finansiering og planlegging | Administrasjon av spesialisthelsetjenesten | Primær styringsbruker |
| Regionale helseforetak | Aktivitetsoversikt og kapasitetsplanlegging | Regional styring og ressursallokering | Rapporteringspliktige og brukere |
| Helseforetak og private avtaleparter | Rapportering og oppfølging av egne data | Intern kvalitetssikring og kontroll | Rapporteringspliktige aktører |
| Forskningsmiljøer | Tilgang til pasientdata for analyse | Medisinsk forskning og helseøkonomi | Søker tilgang via Helsedataservice |
| FHI og statistikkmiljøer | Registerforvaltning og analyse | Statistikk, rapporter og kunnskapsgrunnlag | FHI er databehandler og forvalter |
| Innbyggere | Innsyn i egne opplysninger | Personlig bruk og kontroll | Begrenset direkte brukergruppe |

## Hovedfunksjoner
NPRs viktigste funksjon er å samle og forvalte et komplett og entydig datagrunnlag for alle pasientkontakter i spesialisthelsetjenesten. Registeret gjør det mulig å styre og finansiere tjenestene på et faktabasert grunnlag fordi aktivitetsdata fra alle helseforetak samles i ett nasjonalt register.

Registeret har en sentral rolle i finansieringen av spesialisthelsetjenesten gjennom aktivitetsbasert finansiering (ISF/DRG). Fordi NPR samler takstkoder, diagnose- og prosedyrekoder for alle opphold og polikliniske konsultasjoner, er det grunnlaget som bestemmer hvilke midler helseforetakene mottar. Det gjør NPR til mer enn et analyseregister – det er en direkte del av styringsinfrastrukturen.

NPR gir dessuten nasjonal oversikt over ventetider og pasientrettigheter, noe som er sentralt for kontroll av om spesialisthelsetjenesten ivaretar lovpålagte rettigheter og for rapportering til Storting og regjering.

Data fra NPR brukes som kilde til medisinsk og helsefaglig forskning, blant annet gjennom Helsedataservice og Helsedata.no. Registeret inngår i et større nasjonalt helsedataøkosystem der opplysningene kobles mot andre registre for forskning og analyse.

### Typiske brukssituasjoner
- når helsemyndigheter trenger faktabasert grunnlag for budsjettering og styring av spesialisthelsetjenesten
- når et forskningsprosjekt trenger nasjonale data om behandlingsaktivitet, diagnoser eller pasientforløp i spesialisthelsetjenesten
- når det er behov for nasjoal statistikk over ventetider, pasientvolumer eller behandlingsresultater
- når et kvalitetsregister skal etableres eller kobles mot aktivitetsdata for oppfølging og evaluering

### Når NPR normalt ikke er førstevalg
- når behovet gjelder primærhelsetjenesten eller kommunale helse- og omsorgstjenester (se KPR)
- når behovet gjelder tilgang til person- eller identitetsdata på tvers av sektorer (se Folkeregisteret)
- når behovet er generell datatilgang eller søknad om helsedata (se Helsedata.no)
- når behovet gjelder styrings- eller samordningsdata som ikke er knyttet til aktivitet i spesialisthelsetjenesten

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Data om behandling og pasienter i spesialisthelsetjenesten | Data fra primærhelsetjenesten og kommunale tjenester |
| Nasjonal aktivitetsstatistikk og ventetidsdata | Kliniske journaler og detaljerte behandlingsdokumenter |
| Grunnlag for styring, finansiering og forskning | Full klinisk beslutningstøtte eller pasientjournalsystem |
| Rapporteringspliktige institusjoners aktivitetsdata | Opplysninger utenfor spesialisthelsetjenestens definisjon |

## Veikart over kommende funksjonalitet
Ikke samlet offentlig verifisert i denne arbeidsøkten. Registeret videreutvikles løpende av FHI, og det er kjent at rapporteringsplikten nylig er utvidet til å gjelde privatfinansierte helsetjenester (jf. webinar april 2026).

## Forretningsverdi/Verdiforslag
- For helsemyndigheter: ett felles nasjonalt faktagrunnlag for styring og finansiering av spesialisthelsetjenesten erstatter mange separate datakilder hos helseforetakene.
- For forskningsmiljøer: tilgang til store nasjonale kohorter gjør det mulig å gjennomføre forskning av høy kvalitet som ikke er mulig med lokale data alene.
- For pasienter og samfunn: systematisk registrering gir bedre kunnskap om behandlingskvalitet, ventetider og helsetilstand i befolkningen.
- For planleggings- og styringsmiljøer: registeret gir grunnlag for prioriteringer, behovsanalyser og oppfølging av helsetjenestens kapasitet og resultater.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | feil eller ufullstendig rapportering kan påvirke finansiering og statistikk | tydelig rapporteringsveileder, revisjon og kvalitetskontroll |
| Personvern | store mengder sensitive personopplysninger krever robust informasjonssikkerhet | hjemmelsbasert tilgang, strenge tilgangsregler og personvernvurderinger |
| Tverrsektoriell relevans | verdien utenfor helsesektoren er begrenset | bevisst bruk som sektorregister, ikke som generell NA-ressurs |
| Tilgang | lange søknadsprosesser kan forsinke forskning og analyse | Helsedataservice og helsedata.no som koordinerende tilgangsflate |

## Kanaler
- https://www.fhi.no/he/npr/
- https://www.fhi.no/he/npr/innhold-i-norsk-pasientregister/
- https://www.fhi.no/he/npr/sok-om-data-fra-npr/
- https://helsedata.no/ (søknad om tilgang)

## Plattform
Nasjonalt helseregister forvaltet av Folkehelseinstituttet. Teknisk plattform ikke offentlig spesifisert i kildene brukt i denne arbeidsøkten.

## Gjenbruk
NPR har høy gjenbruksverdi innen helseforskning og styring av spesialisthelsetjenesten. Utenfor dette domenet er gjenbruksverdien begrenset.

**Vanlige kombinasjoner med andre produkter:**
- `Helsedata.no` – søknad om og tilgang til NPR-data via nasjonal tilgangsflate
- `KPR` – komplementært register for kommunale helse- og omsorgstjenester
- `KUHR` – takst- og refusjonsdata som supplerer NPR i helseøkonomiske analyser
- `Kjernejournal` – NPR kan avgi informasjon til kjernejournalen

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** – NPR er autoritativ datakilde som gjøres tilgjengelig for forskning og styring i stedet for at hvert foretak holder egne oppsummerte data.
- **P6: Lag digitale løsninger som støtter samhandling** – registeret muliggjør koordinert styring på tvers av mange helseforetak og nivåer.

**Svakhet:** NPR er et domeneregister for spesialisthelsetjenesten og støtter i begrenset grad bredere tverrsektoriell samhandling.

## Finansiering
Offentlig finansiert nasjonalt helseregister, forvaltet av Folkehelseinstituttet.

## Forvaltning/eier
| Ansvarsområde | Organisasjon | Grunnlag |
|---|---|---|
| Dataforvalter og driftsansvar | Folkehelseinstituttet (FHI) | FHIs egne sider og registerforskriften |
| Faglig ansvar og statistikkpublisering | FHI | løpende statistikker og rapporter |
| Søknad om datatilgang for forskning | Helsedataservice (via helsedata.no) | helsedata.no og fhi.no |

## Lenke til dokumentasjon
- https://www.fhi.no/he/npr/
- https://www.fhi.no/he/npr/innhold-i-norsk-pasientregister/
- https://lovdata.no/forskrift/2007-12-07-1389

## Kildegrunnlag brukt i utfyllingen
- Nettkilde: https://www.fhi.no/he/npr/ (kontrollert 2026-05-03)
- Nettkilde: https://www.fhi.no/he/npr/innhold-i-norsk-pasientregister/ (kontrollert 2026-05-03)
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
