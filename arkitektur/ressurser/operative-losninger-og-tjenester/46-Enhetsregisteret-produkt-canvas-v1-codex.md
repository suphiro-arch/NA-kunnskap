# Produkt-canvas: Enhetsregisteret

## Navn
Enhetsregisteret

## Ressurs ID
BRREG-003

## Status/Livsfase
**Produksjon** - etablert nasjonalt virksomhetsregister og felleskomponent for grunndata om virksomheter.

**Fakta:** Brønnøysundregistrene beskriver Enhetsregisteret som en viktig nasjonal felleskomponent som samler inn, tar vare på og tilgjengeliggjør grunndata om virksomheter. Registeret tildeler organisasjonsnummer og brukes i stor skala på tvers i forvaltningen og blant private aktører.

## Modenhet
**Høy modenhet** - innarbeidet og samfunnskritisk grunndataregister:
- Registeret er sentralt i etablering og drift av virksomheter i Norge.
- Enhetsregisteret er grunnlag for registrering i en rekke andre registre.
- Brønnøysundregistrene tilbyr både åpne søketjenester, abonnementsbasert maskinell tilgang og daglige oppdateringer.
- Registeret er tett integrert i digitale arbeidsprosesser i både offentlig og privat sektor.

**Deduksjon:** Modenheten er svært høy fordi Enhetsregisteret fungerer som en felles nøkkelressurs for identifisering og basisopplysninger om virksomheter, og fordi organisasjonsnummeret er en sentral identifikator i mange tjenester.

## Kort beskrivelse
Ressursen må i praksis forstås bredere enn selve registerkjernen. For analyse- og samhandlingsformål inngår også de viktigste delingsflatene rundt Enhetsregisteret, som åpne oppslag, nøkkelopplysninger, daglige endringer og maskinell tilgang.

Enhetsregisteret er det nasjonale grunndataregisteret for virksomheter i Norge. Produktet samler og tilgjengeliggjør basisopplysninger om juridiske enheter og andre virksomheter, og tildeler organisasjonsnummer som felles identifikator. Enhetsregisteret er derfor mer enn en registreringstjeneste: det er den sentrale virksomhetsressursen som mange andre registre, tjenester og integrasjoner bygger på når de trenger autoritative opplysninger om organisasjoner.

## Kapabiliteter
- **Datakilder: Grunndata** er kjernefunksjonen ved at Enhetsregisteret fungerer som autoritativ kilde for basisopplysninger om virksomheter.
- **Datautveksling og integrasjon: Dele data med andre** gjør grunndata tilgjengelige gjennom åpne tjenester, daglige endringer og maskinell tilgang for offentlig og privat sektor.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Brønnøysundregistrenes beskrivelser av Enhetsregisteret og maskinell tilgang.

## Produktmål
**Primærkilder:** Brønnøysundregistrenes sider `Om Enhetsregisteret`, `Om organisasjonsnummeret` og `Full tilgang Enhetsregisteret`.

Dokumenterte mål:
- Fremme effektiv utnyttelse og samordning av offentlige opplysninger om virksomheter.
- Registrere basisopplysninger om virksomheter på ett sted.
- Tilby en felles identifikator gjennom organisasjonsnummer.

Operative mål utledet fra de samme kildene:
- Redusere dobbeltrapportering og behovet for å sende samme opplysninger til flere etater.
- Gjøre gjenbruk og utveksling av virksomhetsopplysninger enklere på tvers av forvaltningen.
- Tilgjengeliggjøre virksomhetsdata i både åpne og mer avanserte maskinelle kanaler.

## Brukerbehov
- Offentlige virksomheter trenger et felles og autoritativt register over virksomheter.
- Private virksomheter trenger pålitelige opplysninger om organisasjoner i egne tjenester og prosesser.
- Registreringspliktige virksomheter trenger én grunnregistrering som kan gjenbrukes videre i andre registre.
- Forvaltningsmiljøer trenger en felles identifikator og standardiserte grunndata for organisasjoner.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter | Pålitelige virksomhetsopplysninger | Saksbehandling, samordning, kontroll og tjenesteutvikling | Alle offentlige etater skal som hovedregel gjenbruke opplysninger herfra |
| Private virksomheter | Oppdaterte opplysninger om organisasjoner | Bank, kreditt, handel, logistikk og analyse | Stor gjenbruk i privat sektor |
| Registreringspliktige virksomheter | Tildeling av organisasjonsnummer og basisregistrering | Oppstart og løpende oppdatering av virksomhetsopplysninger | Møter produktet som registreringstjeneste |
| Brønnøysundregistrene og registerforvaltning | Drift, kvalitet og tilgjengeliggjøring | Sentral registerforvaltning og distribusjon av grunndata | Operativ forvalter |
| Andre registre og fellesløsninger | Felles identifikator og grunnlag for videre registrering | Foretaksregisteret, Aa-registeret, Altinn m.fl. | Enhetsregisteret er inngang til mange andre registerløp |

## Hovedfunksjoner
### Primære funksjoner
**Autoritativ registrering av virksomhetsopplysninger.** Enhetsregisteret samler sentrale basisopplysninger om virksomheter og gjør dem tilgjengelige i én nasjonal kilde. Dette er produktets viktigste funksjon og gjør registeret relevant for mange sektorer og prosesser.

**Tildeling og forvaltning av organisasjonsnummer.** Produktet gir hver registrert virksomhet en felles identifikator som andre kan bygge videre på. Organisasjonsnummeret er selve nøkkelen til opplysningene i registeret og brukes bredt i digital samhandling.

**Tilgjengeliggjøring gjennom åpne og maskinelle tjenester.** Brønnøysundregistrene beskriver både åpne oppslagstjenester, daglige endringer og full maskinell tilgang. Produktet er derfor både registerkjerne og en aktiv delingsressurs for andre systemer.

**Grunnlag for videre registrering og samordning.** Registrering i Enhetsregisteret er et vilkår for registrering i mange andre registre. Produktet er derfor ikke bare en informasjonskilde, men også en sentral inngang til andre offentlige register- og samhandlingsløp.

### Scope og avgrensning
For analyseformål bør API-er, åpne oppslag, nøkkelopplysninger og annen maskinell tilgjengeliggjøring forstås som del av samme ressurs. De er ikke bare tekniske detaljer rundt registeret, men sentrale mekanismer for hvordan Enhetsregisteret faktisk brukes i digital samhandling.

| Inngår | Inngår ikke |
|---|---|
| Nasjonalt register over basisopplysninger om virksomheter | Fagspesifikke opplysninger som hører hjemme i andre registre |
| Organisasjonsnummer som felles identifikator | Full saksbehandling i tilknyttede registre |
| Åpne søk, daglige endringer og maskinell tilgang | Lokale CRM- og kundeopplysninger hos brukerne |
| Grunnlag for samordning mellom registre | Full intern virksomhetsforvaltning utenfor registrerte grunndata |
| Registrering som inngang til andre registerløp | Alle regulatoriske vurderinger som gjøres i andre registre |

## Veikart over kommende funksjonalitet
Presisering: Delingsflatene for Enhetsregisteret bør normalt beskrives som en del av denne ressursen, ikke som egne separate ressurser, med mindre det senere oppstår en tydelig selvstendig nasjonal ressurs med eget formål, egen styring og egen analyseverdi.

**Fakta fra Brønnøysundregistrenes kilder (kontrollert 2026-03-27):**
- Brønnøysundregistrene publiserer løpende endringer i API-er, åpne data og tilgangstjenester for Enhetsregisteret.
- Det finnes egne sider for full maskinell tilgang, statistikk og åpne data-varsler.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et samlet, tidsfestet veikart for hele Enhetsregisteret er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til å være rettet mot maskinell tilgjengeliggjøring, oppdateringsflyt og løpende tilpasning til regelverk og samordning med andre registre.

## Forretningsverdi/Verdiforslag
### For offentlig sektor
- Gir ett felles og autoritativt virksomhetsgrunnlag på tvers av etater.
- Reduserer dobbeltrapportering og behovet for lokale kopier.
- Gjør samordning og digital tjenesteutvikling enklere.

### For næringsliv og andre brukere
- Gir pålitelig grunnlag for oppslag, verifisering og integrasjon mot virksomhetsdata.
- Skaper større forutsigbarhet når mange aktører trenger samme fakta om en virksomhet.

### For virksomhetene selv
- Reduserer rapporteringsbyrde ved at basisopplysninger kan gjenbrukes av flere.
- Gir én grunnregistrering som kan brukes videre i andre registre og prosesser.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Feil eller forsinket oppdatering kan få store konsekvenser i mange tjenester | Løpende vedlikehold, kontrollrutiner og tydelig meldingsplikt |
| Juridisk og forvaltningsmessig | Feil samordning eller misforståelser om hvilke opplysninger som er autoritative kan skape uklarhet | Klare registregrenser, regelverk og informasjonsansvar |
| Teknisk | Feil i API-er eller oppdateringsleveranser kan påvirke mange brukere samtidig | Stabil integrasjonsforvaltning og varsling om endringer |
| Samfunnsavhengighet | Mange offentlige og private prosesser er avhengige av registeret | Høy forvaltningskvalitet og prioritering av kritiske tjenester |
| Brukeropplevelse | Brukere kan tolke registeropplysningene feil eller tro at de dekker mer enn grunndata | Tydelig dokumentasjon og klare avgrensninger mot andre registre |

## Kanaler
- Om Enhetsregisteret: https://www.brreg.no/om-oss/registrene-vare/om-enhetsregisteret/
- Om organisasjonsnummeret: https://www.brreg.no/om-oss/registrene-vare/om-enhetsregisteret/organisasjonsnummeret/
- Full tilgang til Enhetsregisteret: https://www.brreg.no/bruke-data-fra-bronnoysundregistrene/abonnement/full-tilgang-enhetsregisteret/
- Nøkkelopplysninger fra Enhetsregisteret: https://www.brreg.no/registersok/om-nokkelopplysninger-fra-enhetsregisteret/
- Åpne data-varsler: https://www.brreg.no/varslingskategori/apne-data-enhetsregisteret/

## Plattform
Enhetsregisteret er et nasjonalt register- og delingssystem for basisopplysninger om virksomheter, forvaltet av Brønnøysundregistrene.

**Fakta:** Brønnøysundregistrene beskriver både registerkjerne, åpne oppslag, maskinell tilgang og kobling til andre registre som del av produktområdet.

**Ikke offentlig dokumentert i brukte kilder:** Full intern systemarkitektur, detaljert teknologistakk og full driftsmodell for plattformen.

## Gjenbruk
Produktet er også relevant når behovet gjelder maskinell bruk av virksomhetsdata gjennom oppslag, nøkkelopplysninger, endringsflyt og andre delingsflater som er del av samme ressurs.

**Høy gjenbruksverdi:**
- Produktet er laget for å være felles virksomhetsgrunnlag i samfunnet.
- Det er særlig relevant når behovet er autoritative basisopplysninger om virksomheter og en felles identifikator.
- Det er mindre relevant dersom behovet gjelder fagspesifikke forhold som må hentes fra andre registre.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at Enhetsregisteret tilbyr felles virksomhetsgrunndata som kan brukes på tvers av sektorer.
- **P5: Del og gjenbruk løsninger** styrkes ved at samfunnet kan bygge på ett virksomhetsregister i stedet for parallelle varianter.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi mange tjenester kan bruke samme identifikator og grunnlag.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi registerkvalitet og entydig identifisering er avgjørende for tillit til virksomhetsdata.

## Finansiering
- **Fakta:** Offentlige aktører har gratis full maskinell tilgang til Enhetsregisteret, mens private aktører betaler for tilsvarende tjeneste.
- **Fakta:** Detaljert samlet finansieringsmodell for hele Enhetsregisteret er ikke verifisert i denne arbeidsøkten.
- **Deduksjon:** Produktet finansieres som nasjonal registerforvaltning, kombinert med betalingsmodeller for enkelte brukstyper og kostnader hos brukerne knyttet til integrasjon.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Brønnøysundregistrene | Brønnøysundregistrenes produktsider |
| Driftsansvar | Brønnøysundregistrene | Tilgangs- og registersidene peker til BRREG som operativ forvalter |
| Budsjett- og forvaltningsansvar | Brønnøysundregistrene | Registerforvaltning og publiserte tilgangsmodeller |
| Styringsmodell | Del av Brønnøysundregistrenes registerportefølje og nasjonale grunndataforvaltning | Produktsidene og tilgangssidene |

## Lenke til dokumentasjon
- https://www.brreg.no/om-oss/registrene-vare/om-enhetsregisteret/
- https://www.brreg.no/om-oss/registrene-vare/om-enhetsregisteret/organisasjonsnummeret/
- https://www.brreg.no/bruke-data-fra-bronnoysundregistrene/abonnement/full-tilgang-enhetsregisteret/
- https://www.brreg.no/registersok/om-nokkelopplysninger-fra-enhetsregisteret/
- https://www.brreg.no/varslingskategori/apne-data-enhetsregisteret/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.brreg.no/om-oss/registrene-vare/om-enhetsregisteret/ (kontrollert 2026-03-27)
- Nettkilde: https://www.brreg.no/om-oss/registrene-vare/om-enhetsregisteret/organisasjonsnummeret/ (kontrollert 2026-03-27)
- Nettkilde: https://www.brreg.no/bruke-data-fra-bronnoysundregistrene/abonnement/full-tilgang-enhetsregisteret/ (kontrollert 2026-03-27)
- Nettkilde: https://www.brreg.no/registersok/om-nokkelopplysninger-fra-enhetsregisteret/ (kontrollert 2026-03-27)
- Nettkilde: https://www.brreg.no/varslingskategori/apne-data-enhetsregisteret/ (kontrollert 2026-03-27)



