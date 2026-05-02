# Produkt-canvas: Kommunalt pasient- og brukerregister (KPR)

## Navn
Kommunalt pasient- og brukerregister (KPR)

## Ressurs ID
FHI-006

## Status/Livsfase
**Produksjon** - etablert nasjonalt helseregister for kommunale helse- og omsorgstjenester.

**Fakta:** FHI beskriver Kommunalt pasient- og brukerregister som registeret som inneholder data fra kommunene om personer som har søkt, mottar eller har mottatt helse- og omsorgstjenester. Registeret er hjemlet i forskrift om kommunalt pasient- og brukerregister (2017) og bygges trinnvis.

## Modenhet
**Høy modenhet for kjerneområdene, men under utbygging for øvrige tjenesteområder:**
- KPR KUHR (fastlege, legevakt og fysioterapi) har langvarig operativ rolle og høy modenhet.
- KPR KTT (kommunal tjenestetildeling), KPR HST (helsestasjon og skolehelsetjeneste) og KPR TANN (tannhelse) er under trinnvis utbygging.
- Registeret har klar hjemmel, etablert rapporteringsstruktur og aktivt forvaltningsteam.

**Presisering for NA-vurdering:** KPR er særlig relevant for samordning mellom kommunal og statlig helseforvaltning, men er et domeneregister for kommunale helse- og omsorgstjenester og ikke en bred tverrsektoriell felleskomponent.

## Kort beskrivelse
Kommunalt pasient- og brukerregister (KPR) er det nasjonale registeret for opplysninger om personer som mottar eller har mottatt helse- og omsorgstjenester fra kommunene i Norge. Registeret dekker et bredt spekter av kommunale tjenester, blant annet fastlege, legevakt, fysioterapi, helsestasjon, skolehelsetjeneste, tannhelse og kommunale omsorgstjenester, og er den sentrale datakilden for planlegging, styring, finansiering og evaluering av disse tjenestene.

I arkitektursammenheng er KPR særlig relevant i samhandlingssituasjoner der kommunale og statlige helsemyndigheter trenger et felles datagrunnlag for analyse og styring. Ressursen er avgrenset til kommunale helse- og omsorgstjenester og er ikke en generell tverrsektoriell felleskomponent.

## Kapabiliteter
- **Datakilder: Grunndata**
  KPR er den autoritative nasjonale datakilden for aktivitet og tjenestebruk i kommunale helse- og omsorgstjenester.
- **Datautveksling og integrasjon: Dele data med andre**
  Registeret gjør opplysninger tilgjengelige for forskning, analyse og styring gjennom kontrollerte tilgangskanaler.
- **Informasjonsforvaltning: Datastyring**
  KPR understøtter nasjonal styring og finansiering av kommunale helse- og omsorgstjenester gjennom systematisk dataforvaltning.

## Produktmål
**Primærkilder:** FHIs side `Om Kommunalt pasient- og brukerregister (KPR)` (kontrollert 2026-05-03).

Dokumentert hovedformål:
- Gi kommunale, regionale og sentrale helsemyndigheter grunnlag for planlegging, styring, finansiering og evaluering av helse- og omsorgstjenester i kommunene.
- Brukes som grunnlag for kvalitetsforbedring, forebyggende arbeid, beredskap, analyser og forskning.

## Brukerbehov
- Kommuner trenger et felles nasjonalt register for å rapportere og sammenlikne tjenesteproduksjon og tjenestekvalitet.
- Helsedirektoratet og helsemyndigheter trenger datagrunnlag for finansiering og evaluering av kommunale helse- og omsorgstjenester.
- Forskningsmiljøer trenger tilgang til nasjonale data om kommunale helsetjenester for forskning og analyse.
- Innbyggere trenger innsyn i egne opplysninger registrert i KPR.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Sentrale helsemyndigheter (HOD, Hdir) | Styring, finansiering og evaluering | Nasjonal politikk og ressursallokering for kommunale tjenester | Primær styringsbruker |
| Kommuner | Rapportering og sammenlikning | Lokalt planlegging, kvalitetsarbeid og innsyn i tjenesteproduksjon | Rapporteringspliktige aktører |
| Forskningsmiljøer | Tilgang til data om primærhelsetjenesten | Epidemiologisk forskning, helsetjenesteforskning | Søker tilgang via Helsedataservice |
| FHI og statistikkmiljøer | Registerforvaltning og statistikkpublisering | Nasjonal folkehelserolle og kommunestatistikk | FHI er databehandler og forvalter |
| Innbyggere | Innsyn i egne opplysninger | Personlig bruk og kontroll | Begrenset direkte brukergruppe |

## Hovedfunksjoner
KPRs viktigste funksjon er å samle og forvalte et nasjonalt datagrunnlag for helse- og omsorgstjenester i kommunene. Registeret dekker tjenester som fastlege, legevakt, fysioterapi, helsestasjon, skolehelsetjeneste, tannhelse og kommunal tjenestetildeling, og er derfor den eneste nasjonale datakilden som gir samlet innsyn i aktiviteten i den kommunale helse- og omsorgssektoren.

En sentral funksjon er å støtte finansiering og ressursallokering til kommunal sektor. I likhet med NPRs rolle i spesialisthelsetjenesten gir KPR grunnlag for at sentrale myndigheter kan vurdere tjenestevolum, kapasitet og behov i kommunene basert på faktiske aktivitetsdata.

KPR er et trinnvis bygget register, der ulike delregistre dekker ulike tjenesteområder. Det betyr at modenhet og datakvalitet varierer mellom delregistrene, og at ikke alle kommunale tjenester er like fullt dekket. Dette er viktig å ta hensyn til i arkitekturvurderinger der KPR brukes som datagrunnlag.

Registeret gir dessuten grunnlag for forskning på primærhelsetjenesten, og er særlig relevant når forskning eller analyse skal dekke begge nivåer i helsetjenesten (kommunalt og spesialisthelsetjeneste). KPR og NPR er komplementære i dette perspektivet.

### Typiske brukssituasjoner
- når helsemyndigheter trenger faktabasert grunnlag for styring, evaluering og finansiering av kommunale helse- og omsorgstjenester
- når et forskningsprosjekt trenger nasjonale data om fastlege, legevakt, tannhelse, helsestasjon eller kommunale omsorgstjenester
- når det er behov for å sammenlikne tjenesteproduksjon på tvers av kommuner
- når behovet gjelder kobling av aktivitetsdata fra kommunalt og statlig nivå i forskning eller analyse

### Når KPR normalt ikke er førstevalg
- når behovet gjelder spesialisthelsetjenesten (se NPR)
- når behovet gjelder generell datatilgang eller søknad om helsedata (se Helsedata.no)
- når behovet gjelder styrings- eller samordningsdata utenom helse- og omsorgssektoren
- når behovet er direkte teknisk integrasjon uten tilknytning til kommunale helse- og omsorgstjenester

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Data om kommunale helse- og omsorgstjenester | Data fra spesialisthelsetjenesten (se NPR) |
| Fastlege, legevakt, helsestasjon, tannhelse og kommunal omsorg | Kliniske journaler og detaljerte behandlingsdokumenter |
| Grunnlag for styring, finansiering og forskning innen kommunal sektor | Styrings- og analysebehov på tvers av sektorer |
| Trinnvis utbygging av delregistre for alle kommunale tjenester | Fullt datagrunnlag for alle tjenester (under utbygging) |

## Veikart over kommende funksjonalitet
Registeret bygges trinnvis, og det arbeides med å inkludere flere av de kommunale tjenestene som er nevnt i lov om kommunale helse- og omsorgstjenester. Rapporteringsplikten er nylig utvidet, og FHI holder webinarer om endringer i rapporteringskrav (jf. april 2026).

## Forretningsverdi/Verdiforslag
- For helsemyndigheter: ett felles nasjonalt datagrunnlag for kommunale helse- og omsorgstjenester gjør det mulig å styre og evaluere tjenestene uten å basere seg på lokale og sammenlignbare rapporteringer.
- For kommuner: felles nasjonalt register gir mulighet for å sammenlikne seg med andre kommuner og dokumentere tjenesteproduksjon overfor stat og innbyggere.
- For forskningsmiljøer: nasjonal dekning av primærhelsetjenestens aktivitet er nødvendig for å forstå folkehelse og helsetjenestebruk over livsløpet.
- For innbyggere og samfunn: bedre kunnskap om primærhelsetjenestens omfang og kvalitet bidrar til mer informerte prioriteringer.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Trinnvis utbygging | Ikke all tjenesteproduksjon er dekket ennå, som kan gi misvisende sammenlikninger | tydelig kommunikasjon om hvilke delregistre som er operative |
| Datakvalitet | Kommunal rapportering kan variere i kvalitet og konsistens | rapporteringsveiledere, validering og faglig oppfølging |
| Personvern | Sensitive personopplysninger om helsetjenestebruk krever robust sikkerhet | hjemmelsbasert tilgang og personvernvurderinger |
| Tverrsektoriell relevans | Verdien utenfor helsesektoren er begrenset | bevisst bruk som sektorregister med tydelig domenekobling |

## Kanaler
- https://www.fhi.no/he/kpr/
- https://www.fhi.no/he/kpr/om-kpr/
- https://www.fhi.no/he/kpr/sok-om-data-fra-kpr/
- https://helsedata.no/ (søknad om tilgang)

## Plattform
Nasjonalt helseregister forvaltet av Folkehelseinstituttet. Teknisk plattform ikke offentlig spesifisert i kildene brukt i denne arbeidsøkten.

## Gjenbruk
KPR har høy gjenbruksverdi innen helseforskning og styring av kommunale helse- og omsorgstjenester. Utenfor dette domenet er gjenbruksverdien begrenset.

**Vanlige kombinasjoner med andre produkter:**
- `Helsedata.no` – søknad om og tilgang til KPR-data via nasjonal tilgangsflate
- `NPR` – komplementært register for spesialisthelsetjenesten
- `KUHR` – KPR KUHR bygger på KUHR-data for fastlege, legevakt og fysioterapi
- `SYSVAK` – kan kombineres for folkehelsestudier der vaksinasjon og primærhelsetjeneste er tema

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** – KPR samler kommunale tjenestedata i ett nasjonalt register i stedet for at hvert statistikkbehov løses lokalt.
- **P6: Lag digitale løsninger som støtter samhandling** – registeret muliggjør samordnet styring og analyse på tvers av mange kommuner og forvaltningsnivåer.

**Svakhet:** KPR er et domeneregister for kommunale helse- og omsorgstjenester og er fremdeles under trinnvis utbygging. Ressursen er ikke en bred tverrsektoriell felleskomponent, og datadekning varierer mellom tjenesteområder.

## Finansiering
Offentlig finansiert nasjonalt helseregister, forvaltet av Folkehelseinstituttet.

## Forvaltning/eier
| Ansvarsområde | Organisasjon | Grunnlag |
|---|---|---|
| Dataforvalter og driftsansvar | Folkehelseinstituttet (FHI) | FHIs egne sider og registerforskriften |
| Faglig ansvar og statistikkpublisering | FHI | løpende statistikker og rapporter |
| Søknad om datatilgang for forskning | Helsedataservice (via helsedata.no) | helsedata.no og fhi.no |

## Lenke til dokumentasjon
- https://www.fhi.no/he/kpr/
- https://www.fhi.no/he/kpr/om-kpr/
- https://lovdata.no/forskrift/2017-08-25-1292

## Kildegrunnlag brukt i utfyllingen
- Nettkilde: https://www.fhi.no/he/kpr/ (kontrollert 2026-05-03)
- Nettkilde: https://www.fhi.no/he/kpr/om-kpr/ (kontrollert 2026-05-03)
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
