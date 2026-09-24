# eSignature Building Block

## Navn
eSignature Building Block

## Ressurs ID
EU-004

## Status/Livsfase
**Produksjon** - aktiv byggestein med forvaltet programvarebibliotek, tillitslistetjeneste og valideringsverktøy i løpende bruk.

**Fakta:** Europakommisjonen fører eSignature som aktiv byggestein i DIGITAL Building Blocks og beskriver den som et sett gratis standarder, verktøy og tjenester for å opprette og verifisere elektroniske signaturer som er rettslig gyldige i alle medlemsstater.

## Modenhet
**Høy teknisk og regulatorisk modenhet.**

- Regulatorisk: byggesteinen er direkte knyttet til eIDAS-forordningen, som gir rettslig anerkjennelse og grensekryssende interoperabilitet for signaturer og segl laget med løsninger bygget på byggesteinen.
- Teknisk: programvarebiblioteket Digital Signature Services, DSS, er åpen kildekode og støtter signaturformatene XAdES, CAdES, PAdES og JAdES.
- Operativt: Trusted List Browser gir oppslag i medlemsstatenes tillitslister over kvalifiserte tillitstjenestetilbydere, og et valideringsverktøy kontrollerer signaturer mot ETSI-standarder.
- Bruksmessig: byggesteinen har et eget navseks med dokumentasjon, veiledning og fellesskapsstøtte.

**Deduksjon:** Det svakeste leddet er ikke byggesteinen, men det organisatoriske rundt den. Å validere en signatur teknisk er løst; å avgjøre hvilket signaturnivå en gitt sak krever, og hvordan resultatet skal arkiveres og kunne etterprøves over tid, er fortsatt opp til den enkelte virksomheten.

## Kort beskrivelse
eSignature Building Block er Europakommisjonens felles byggestein for elektroniske signaturer og segl. Den leverer standarder, et åpent programvarebibliotek og tjenester som gjør det mulig å opprette signaturer som er rettslig gyldige i hele EU, og å verifisere signaturer laget i andre land uten bilaterale avtaler.

Byggesteinen består av tre praktiske deler: DSS-biblioteket for å bygge signatur- og valideringsfunksjonalitet inn i egne løsninger, Trusted List Browser for å slå opp kvalifiserte tillitstjenestetilbydere i Europa, og et valideringsverktøy som kontrollerer at en signatur er i samsvar med ETSI-standardene. Byggesteinen leverer ikke selve signeringstjenesten til sluttbrukere; den gir grunnlaget som slike tjenester bygges på.

## Kapabiliteter
- **Tillit: Signering**
  gir programvarekomponentene og tillitsgrunnlaget som gjør det mulig å opprette og verifisere avanserte og kvalifiserte elektroniske signaturer på tvers av land.

- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling**
  gjør det mulig å påvise at et dokument ikke er endret etter signering, og hvem som står bak det, uavhengig av hvilken kanal dokumentet er sendt gjennom.

- **Standardisering: EU standarder**
  forvalter og tilgjengeliggjør signaturformatene og valideringsreglene fra ETSI i en form som lar seg ta i bruk, med konformitetskontroll.

Koblingene er satt fordi byggesteinen selv leverer programvaren og tillitsoppslaget. Den enkelte signeringstjenesten og de kvalifiserte tillitstjenestetilbyderne er egne aktører, og evnen til å utstede kvalifiserte sertifikater hører hos dem.

## Produktmål
**Dokumenterte mål** slik Kommisjonen beskriver byggesteinen:
- Gjøre det raskere for offentlige virksomheter og næringsliv å opprette og verifisere elektroniske signaturer som er rettslig gyldige i alle medlemsstater.
- Sikre etterlevelse av eIDAS-forordningens krav, med rettslig anerkjennelse og grensekryssende interoperabilitet.
- Gi fri tilgang til standarder, verktøy og tjenester.

**Utledede operative mål:**
- Redusere behovet for at hver virksomhet implementerer ETSI-standardene fra bunnen.
- Gjøre det mulig å verifisere signaturer fra andre land uten å kjenne det enkelte landets tillitsstruktur.

## Brukerbehov
- Virksomheter trenger å kunne stole på en signatur laget i et annet land, uten å vurdere hvert lands ordning selv.
- Utviklingsmiljøer trenger et ferdig bibliotek for å opprette og validere signaturer i etablerte formater.
- Saksbehandlingsmiljøer trenger å kunne dokumentere at et signert dokument er uendret og at underskriveren er identifisert.
- Arkitekturmiljøer trenger å forstå skillet mellom avansert og kvalifisert signatur, og hva skillet betyr for rettslig virkning.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Utviklingsmiljøer | Bibliotek for signering og validering | Integrasjon i fagløsninger og portaler | Primærbruker av DSS |
| Offentlige virksomheter | Verifisere signaturer fra inn- og utland | Søknader, avtaler, vedtak | Bruker ofte byggesteinen gjennom en leverandørløsning |
| Leverandører av signeringstjenester | Bygge tjenester som oppfyller eIDAS | Produktutvikling | Bygger på DSS eller egen implementasjon |
| Tilsyns- og forvaltningsmiljøer | Slå opp kvalifiserte tillitstjenestetilbydere | Kontroll og vurdering | Bruker Trusted List Browser |
| Europakommisjonen | Forvalte standarder, bibliotek og tjenester | Spesifikasjon og drift | Eier byggesteinen |

## Hovedfunksjoner
Den første hovedfunksjonen er **signering og validering gjennom DSS**. Biblioteket dekker hele løpet fra å opprette en avansert elektronisk signatur til å utvide den med tidsstempel og valideringsdata, og til å kontrollere en mottatt signatur. Det støtter formatene XAdES for XML, CAdES for binære data, PAdES for PDF og JAdES for JSON, slik at samme komponent kan brukes uavhengig av dokumenttype.

Den andre er **oppslag i tillitslister**. Trusted List Browser gir tilgang til medlemsstatenes lister over kvalifiserte tillitstjenestetilbydere. Dette er det praktiske svaret på spørsmålet «kan jeg stole på sertifikatet som ligger bak denne signaturen», og det er en forutsetning for at en virksomhet skal kunne behandle signaturer fra land den ikke kjenner.

Den tredje er **konformitetskontroll**. Kommisjonen tilbyr et nettbasert valideringsverktøy som utfører en rekke kontroller mot ETSI-standardene. Verktøyet brukes både til feilsøking under utvikling og til å vurdere enkeltsignaturer i saksbehandling.

Den fjerde er **veiledning og fellesskap**. eSignature-navet samler dokumentasjon, innføringsveiledning og støtte. For en virksomhet er dette ofte like viktig som koden, fordi de vanskelige valgene gjelder hvilket signaturnivå som kreves, ikke hvordan biblioteket kalles.

### Typiske brukssituasjoner (generisk)
- En løsning skal ta imot signerte dokumenter fra virksomheter eller innbyggere i andre EØS-land.
- En virksomhet skal bygge signering inn i en egen fagløsning framfor å kjøpe en ferdig tjeneste.
- En saksbehandler må avgjøre om en mottatt signatur er kvalifisert, og om den er gyldig på signeringstidspunktet.

### Når eSignature Building Block normalt ikke er førstevalg
- Når behovet er signering i norsk offentlig sektor med norske brukere. Da er `eSignering` den etablerte fellesløsningen, og byggesteinen er underliggende teknologi snarere enn et eget valg.
- Når virksomheten ikke har utviklingskapasitet. DSS er et bibliotek, ikke en ferdig tjeneste, og krever egen implementasjon og drift.
- Når behovet egentlig er autentisering, ikke signering. Da hører løsningen hos `ID-porten` eller eID-byggesteinen.
- Når behovet er langtidsbevaring av signert materiale. Byggesteinen dekker signatur og validering, ikke arkivstrategi.

### Scope og avgrensning
Inngår: DSS-biblioteket, Trusted List Browser, valideringsverktøy, dokumentasjon og veiledning knyttet til eIDAS-signaturer og segl.

Inngår ikke: utstedelse av sertifikater, drift av signeringstjenester for sluttbrukere, identitetskontroll før signering, og arkivering av signerte dokumenter.

## Veikart over kommende funksjonalitet
**Fakta:** Byggesteinen er aktivt vedlikeholdt, med eSignature-navet som sentral ressurs for dokumentasjon og innføringsstøtte.

**Deduksjon:** Innføringen av eIDAS 2.0 og EUDI-lommeboka vil påvirke byggesteinen, fordi lommeboka selv skal kunne opprette rettslig bindende signaturer. Kildene i denne arbeidsøkten sier ikke hvordan ansvarsdelingen mellom byggesteinen og lommeboka skal se ut.

**Ikke offentlig dokumentert i denne arbeidsøkten:** en datofestet utgivelsesplan for DSS eller for tillitslistetjenestene.

## Forretningsverdi/Verdiforslag
**For utviklingsmiljøer:** et ferdig, vedlikeholdt bibliotek som dekker fire signaturformater, i stedet for egen implementasjon av ETSI-standardene.

**For virksomheter:** mulighet til å godta signaturer fra hele EØS uten å bygge opp kunnskap om hvert lands tillitsstruktur.

**For samfunnet:** felles grunnlag for rettslig gyldige digitale avtaler over landegrenser, som reduserer behovet for papir og fysisk frammøte.

**For forvaltningen:** etterprøvbar dokumentasjon på hvem som har signert hva, og at innholdet ikke er endret etterpå.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Juridisk | Feil valg av signaturnivå gir enten manglende rettsvirkning eller unødvendig høy terskel | eIDAS definerer nivåene; vurderingen ligger hos den enkelte virksomheten |
| Teknisk | DSS er et bibliotek som må integreres, driftes og oppgraderes lokalt | Krever utviklingskapasitet; byggesteinen leverer ikke tjenesten ferdig |
| Lisens | LGPL-2.1 stiller vilkår ved endring og distribusjon av biblioteket | Kontroller vilkårene mot repositoriet før biblioteket endres og distribueres videre |
| Bevaring | Signaturers gyldighet må kunne etterprøves lenge etter at sertifikatet er utløpt | Formatene støtter utvidelse med tidsstempel og valideringsdata; arkivstrategi er ikke dekket av byggesteinen |
| Overgang | eIDAS 2.0 og lommebok endrer signaturlandskapet | Ikke offentlig dokumentert i denne arbeidsøkten |

## Kanaler
Byggesteinen leveres gjennom tre flater. DSS lastes ned som programvarebibliotek og integreres i egne løsninger. Trusted List Browser og valideringsverktøyet er nettbaserte tjenester som brukes direkte i nettleser, uten innlogging. Dokumentasjon og veiledning ligger på eSignature-navet i Kommisjonens portal for DIGITAL Building Blocks.

Det finnes ingen sluttbrukerflate for signering. Sluttbrukeren møter byggesteinen bare gjennom tjenester som er bygget på den.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** driftsmodell for Kommisjonens nettbaserte tjenester. Det som er kjent, er at DSS er et Java-bibliotek som kjøres på brukerens egen plattform, og at Trusted List Browser og valideringsverktøyet driftes av Kommisjonen som nettjenester.

## Gjenbruk
Byggesteinen er i sin helhet innrettet mot gjenbruk: standardene er åpne, biblioteket er åpen kildekode, og tjenestene er gratis tilgjengelige. En virksomhet kan bruke DSS direkte, bygge sin egen implementasjon etter samme standarder, eller kjøpe en løsning fra en leverandør som selv bygger på biblioteket.

Avhengigheter som ikke er kapabiliteter her: kvalifiserte sertifikater utstedes av tillitstjenestetilbydere, og identitetskontrollen før signering skjer i andre løsninger.

**Vanlige kombinasjoner med andre produkter:**
- `eSignering` som norsk fellesløsning for signering, der byggesteinen er underliggende standardgrunnlag.
- `eID Building Block` og `ID-porten` for å identifisere den som skal signere.
- `eDelivery Building Block` når signerte dokumenter også skal utveksles etterprøvbart.
- `European Digital Identity Wallet`, som på sikt skal kunne opprette signaturer direkte fra lommeboka.

**Kildekode:** Åpen kildekode. DSS publiseres av Europakommisjonen.

**Lisens:** `LGPL-2.1`. Repositoriet oppgir at prosjektet leveres under Lesser General Public License, versjon 2.1.

**Repositorium:** https://github.com/esig/dss

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger**
  Åpen kildekode, åpne standarder og fritt tilgjengelige tjenester gjør at samme komponent kan brukes av alle medlemsstater og av private aktører.
- **P6: Lag digitale løsninger som støtter samhandling**
  Felles formater og felles tillitslister er det som gjør at en signatur laget i ett land kan brukes i et annet.
- **P7: Sørg for tillit til oppgaveløsningen**
  Kjernen i byggesteinen er nettopp etterprøvbar tillit: hvem signerte, når, og er innholdet uendret.

**Spenning og begrensning:** Byggesteinen støtter **P1: Ta utgangspunkt i brukernes behov** bare delvis. Den er rettet mot utviklere og forvaltere, ikke mot sluttbrukere, og brukeropplevelsen ved signering avgjøres av tjenesten som bygges oppå. Den er også i spenning mot **P2: Ta arkitekturbeslutninger på rett nivå** for virksomheter uten utviklingskapasitet: å velge et bibliotek framfor en ferdig tjeneste flytter en kompleks og sikkerhetskritisk oppgave inn i egen organisasjon. Lisensvilkårene i LGPL-2.1 bør vurderes eksplisitt når biblioteket skal endres og distribueres videre i et produkt.

## Finansiering
**Fakta:** Byggesteinen er beskrevet som gratis å bruke, og forvaltes og finansieres av Europakommisjonen som del av DIGITAL-programmet for byggesteiner.

**Deduksjon:** Kostnadene for en norsk virksomhet ligger i integrasjon, drift og eventuelle sertifikater fra tillitstjenestetilbydere, ikke i byggesteinen selv.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Europakommisjonen | DIGITAL Building Blocks, eSignature |
| Utvikling av DSS | Europakommisjonen, med åpen kildekode på GitHub | Repositoriet `esig/dss` |
| Drift av tillitslister | Medlemsstatene, samlet i Trusted List Browser | Kommisjonens beskrivelse av tjenesten |
| Regelverksgrunnlag | eIDAS-forordningen | Kommisjonens omtale av rettslig anerkjennelse |
| Budsjettansvar | Europakommisjonen | Deduksjon fra at byggesteinen tilbys gratis i DIGITAL-programmet |
| Styringsmodell | Ikke offentlig dokumentert i denne arbeidsøkten | - |

## Lenke til dokumentasjon
- eSignature Building Block: https://ec.europa.eu/digital-building-blocks/sites/display/DIGITAL/eSignature
- DSS-repositoriet: https://github.com/esig/dss
- DIGITAL Building Blocks, samleside: https://interoperable-europe.ec.europa.eu/collection/digital-building-blocks

## Kildegrunnlag brukt i utfyllingen
- Europakommisjonen, eSignature Building Block, hentet 24. september 2026.
- Europakommisjonen og ESIG, DSS-repositoriet på GitHub, lisens kontrollert 24. september 2026.
- Europakommisjonen, DIGITAL Building Blocks, hentet 24. september 2026.
- Lokale kilder: `arkitektur/ressurser/produktnummerering.md`, `arkitektur/kapabiliteter/capabilities.yaml`, `arkitektur/prinsipper/principles.md`, `sources/links.md`.
