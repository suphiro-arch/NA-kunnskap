# Produkt-canvas: FIKS Melding

## Navn
FIKS Melding

## Ressurs ID
KS-002

## Status/Livsfase
**Produksjon** - etablert meldingstjeneste i KS Digital med flere operative kanaler og publisert veilednings- og sikkerhetsgrunnlag.

**Fakta:** KS beskriver FIKS Melding som en plattform for å sende informasjon gjennom ulike kanaler, der kommunen selv velger hvilke kanaler som tas i bruk og betaler for faktisk bruk.

## Modenhet
**Høy funksjonell modenhet** - løsningen har et tydelig kanalsett, publisert innføringsløp, sikkerhetsdokumentasjon og avtalegrunnlag.
- Tjenesten tilbyr konkrete kanaler for SMS, dokumentdeling, e-dialog og utsending av brev.
- Dokumentasjonen viser at produktet er i aktiv bruk og at kommunene får veiledere og underlag for ROS og DPIA.
- Modenheten er høy for meldingsfunksjonene som er publisert, men vil variere mellom kanalene og hvordan de tas i bruk i lokale arbeidsprosesser.

## Kort beskrivelse
FIKS Melding er KS Digitals meldingstjeneste for sikker og fleksibel informasjonsflyt mellom kommuner, innbyggere og andre virksomheter. Løsningen gjør det mulig å sende informasjon gjennom flere kanaler fra samme tjenestegrunnlag, slik at kommunen kan velge utsendingsmåte etter behov og bruke samme løsning til både enkle og mer sensitive meldingsløp. Produktet er særlig relevant når virksomheten trenger en felles kanalplattform for meldinger, dokumentdeling og sikker innsendelse, uten å etablere separate løsninger for hver kommunikasjonstype.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** er produktets kjernefunksjon fordi løsningen pakker, sender og leverer meldinger og dokumenter gjennom flere valgbare kanaler.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** er direkte relevant fordi produktet brukes til sikker kommunikasjon og KS publiserer eget sikkerhetsunderlag for ROS og DPIA for flere kanaler.
- **Samarbeid: Organisatorisk samhandling** støtter samhandling mellom kommuner, innbyggere og virksomheter ved å gi en felles meldingstjeneste for utgående og inngående kommunikasjon.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals kilder brukt i denne arbeidsøkten.

## Produktmål
Dokumenterte mål:
- Gi kommunene kontroll over informasjonsflyten fra avsender til mottaker.
- Gjøre det mulig å sende informasjon gjennom ulike kanaler fra samme løsning.
- Forenkle masseutsendelser, dokumentdeling og sikker kommunikasjon.

Operative mål utledet fra kildene:
- Redusere behovet for separate løsninger for SMS, dokumentdeling og sikker dialog.
- Gjøre kommunikasjon mer fleksibel og kanalstyrt.
- Gi kommunene et grunnlag for sikker meldingsutveksling med dokumenterte sikkerhetsvurderinger.

## Brukerbehov
- Kommuner trenger ett sted å håndtere flere typer meldingsløp i stedet for å forvalte mange små kanalløsninger.
- Fagmiljøer trenger sikre kanaler for å sende sensitiv eller viktig informasjon.
- Kommuner trenger effektive verktøy for masseutsendelser og deling av store dokumenter.
- Innbyggere og virksomheter trenger en sikker kanal inn til kommunen i relevante sammenhenger.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Sende informasjon gjennom flere kanaler fra samme tjeneste | Varsling, dokumentdeling, brev og e-dialog | Primærbrukere av tjenesten |
| Fag- og tjenestemiljøer | Sikker kanal for konkrete saks- og tjenesteløp | Dialog og utsending i kommunale tjenester | Bruker verdien i daglig tjenesteproduksjon |
| Innbyggere og virksomheter | Motta eller sende informasjon gjennom sikker kanal | Mottak av meldinger eller innsending via e-dialog | Sekundærbrukere |
| Tekniske forvaltere og leverandører | Integrere og konfigurere kanalbruk | Oppsett, integrasjon og sikkerhetsvurdering | Trenger teknisk dokumentasjon og veiledere |
| KS Digital | Forvalte kanalene og støtte innføring | Produktforvaltning, sikkerhetsstøtte og videreutvikling | Forvalter tjenesten sentralt |

## Hovedfunksjoner
### Primære funksjoner
- FIKS Melding lar kommunen sende SMS til mange mottakere, enten via adresselister eller ved oppslag mot identitets- og kontaktgrunnlag. Dette gjør løsningen relevant når kommunen trenger effektiv og styrbar massekommunikasjon.
- Tjenesten kan dele dokumenter og filer på opptil 5 GB med tidsstyrt tilgjengelighet. Det skiller produktet fra en ren meldingstjeneste, fordi det også dekker sikker deling av større dokumentinnhold.
- E-dialog gir en sikker kanal inn til kommunen eller virksomheten. Denne funksjonen gjør produktet egnet også for innkommende kommunikasjon og ikke bare utsending.
- Send brev gjør det mulig å håndtere masseutsendelser av samme eller ulike dokumenter til flere mottakere. Produktet dekker dermed både digitale og mer tradisjonelle utsendingsbehov i samme tjenestegrunnlag.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| SMS, dokumentdeling, e-dialog og brevutsending | Lokal saksbehandling og arbeidsflyt |
| Kanalvalg og styring av utsending | Full erstatning for kommunens fagsystemer |
| Veiledere og sikkerhetsunderlag for bruk | Automatisk semantisk behandling av innhold |
| Sikker kommunikasjon og meldingskanaler | Nasjonal autoritativ datakilde eller register |

## Veikart over kommende funksjonalitet
**Fakta:** KS publiserer løpende aktuelle saker om endringer i FIKS Melding og FIKS SvarUt. Produktsiden viser aktive veiledere, sikkerhetsdokumentasjon og nyhetsløp, men jeg fant ikke et samlet offentlig roadmap med tidsfestede milepæler.

**Deduksjon:** Videreutviklingen vil trolig være kanalnær og bruksscenarionær, med forbedringer i eksisterende kanaler og støtte for nye meldingsbehov.

## Forretningsverdi/Verdiforslag
### For kommuner
- Samler flere meldingskanaler i én fellestjeneste.
- Gjør det lettere å velge kanal etter behov og risiko.

### For fagmiljøer
- Forenkler kommunikasjon med innbyggere og andre virksomheter.
- Gir støtte for både enkle meldinger og mer sensitive eller dokumenttunge løp.

### For sektoren
- Reduserer behovet for mange parallelle kommunikasjonsløsninger.
- Gir mer standardisert og styrbar meldingsutveksling.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil kanalvalg eller feil bruk av personopplysninger kan gi brudd på krav til konfidensialitet og personvern. | Bruke kanalene etter formål, og gjøre lokale ROS- og DPIA-vurderinger. |
| Teknisk | Avhengighet til flere kanaler og lokale integrasjoner kan gi variasjon i faktisk leveransekvalitet. | Teste lokale oppsett og bruke dokumenterte integrasjonsmønstre og veiledere. |
| Sikkerhet | Meldings- og dokumentløp kan inneholde sensitiv informasjon. | Bygge på sikker kanalbruk, kryptering og dokumenterte sikkerhetsvurderinger. |
| Leverandør | Kommunen blir avhengig av sentral tjenesteforvaltning og kanaltilbud i FIKS Melding. | Tydelige avtaler, kjent prismodell og forutsigbar videreutvikling. |
| Brukeropplevelse | Kommunikasjonen kan bli fragmentert hvis kanalene ikke brukes konsekvent eller forståelig. | Tydelig tjenestedesign og bevisst valg av kanal per brukssituasjon. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-melding/
- https://status.fiks.ks.no

## Plattform
FIKS Melding er en sentralt forvaltet fellestjeneste i KS Digital.

**Fakta:**
- Tjenesten tilbyr flere kanaler for meldingsutveksling og dokumentdeling.
- KS publiserer veiledere og sikkerhetsunderlag for deler av funksjonssettet.
- Løsningen inngår i FIKS-universet, men er selv en spesifikk kommunikasjonstjeneste og ikke selve plattformgrunnlaget.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur og detaljert teknologistakk per kanal.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme tjeneste kan brukes til flere kommunikasjonsbehov i ulike kommuner.
- Kanalene kan kombineres og styres innenfor samme produkt i stedet for å bygges hver for seg.
- Produktet er mest gjenbrukbart som felles kommunikasjonstjeneste, ikke som lokal spesialfunksjon.

## Støtter arkitekturprinsipper
- **P6 Lag digitale løsninger som støtter samhandling** - produktet er laget for sikker utveksling av meldinger og dokumenter mellom aktører.
- **P7 Sørg for tillit til oppgaveløsningen** - sikker kommunikasjon og publisert sikkerhetsunderlag er en sentral del av produktets verdi.

## Finansiering
**Fakta:** Kommunen må signere tjenestevedlegg i tillegg til hovedavtale for å ta i bruk FIKS Melding, og KS opplyser at brukeren velger kanaler og betaler for faktisk bruk.

**Ikke offentlig dokumentert i brukte kilder:** Full finansieringsmodell for videreutvikling og sentral forvaltning.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsiden og avtalegrunnlaget ligger hos KS Digital. |
| Driftsansvar | Ikke offentlig spesifisert i brukte kilder | Må avklares i mer tekniske eller kontraktsnære kilder. |
| Budsjettansvar | Kombinasjon av sentral forvaltning og bruksbasert kundegrunnlag | Delvis utledet fra avtale- og prismodell på produktsiden. |
| Styringsmodell | KS Digital med tjenesteforvaltning, veiledere og sikkerhetsunderlag | Synlig på produktsiden og i tilhørende veiledningsløp. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-melding/
- https://status.fiks.ks.no

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-melding/ (hentet 2026-03-18)
