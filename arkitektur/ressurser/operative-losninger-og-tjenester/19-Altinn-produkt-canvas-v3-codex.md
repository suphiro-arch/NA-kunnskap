# Produkt-canvas: Altinn 3 plattform

## Navn
Altinn 3 plattform

## Ressurs ID
DIGDIR-017

## Status/Livsfase
**Produksjon** - etablert plattform for utvikling, kjøring og samhandling i Altinn-porteføljen, med aktiv modernisering og videre overgang fra Altinn 2.

**Fakta:** Offisiell Altinn-dokumentasjon beskriver en samlet plattform rundt Altinn Studio, Altinn Apps og tilhørende plattformtjenester. Dokumentasjonen viser også at moderniseringen fortsatt pågår på flere produktområder per 26. mars 2026.

## Modenhet
**Middels til høy funksjonell modenhet** - kjerneplattformen er etablert og i aktiv bruk, men totalbildet preges fortsatt av modernisering og samspill med eldre Altinn-løsninger:
- Altinn Studio og Altinn Apps er etablert som hovedmønster for nye tjenester.
- Plattformen tilbyr felles byggesteiner for autentisering, autorisasjon, lagring, hendelser, varsling og innsending.
- Flere tilgrensende produktområder er dokumentert som egne produkter med egne modenhetsløp.

**Deduksjon:** Plattformen er moden som felles fundament for nye Altinn-tjenester, men bør forstås som en paraply for plattformkapabiliteter, ikke som ett enkelt sluttbrukerprodukt med én brukerflate.

## Kort beskrivelse
Altinn 3 plattform er den operative plattformen for å utvikle, kjøre og forvalte digitale tjenester i Altinn. Produktet omfatter både utviklingsflaten i Altinn Studio, kjøretidsmiljøet i Altinn Apps og et sett felles plattformtjenester som gir tjenester standardiserte mønstre for autentisering, autorisasjon, datalagring, innsending, hendelser og integrasjon.

Produktet er derfor mer enn en utviklerplattform i snever forstand. Det er også et felles kjøretids- og samhandlingsgrunnlag for tjenester som skal brukes av innbyggere, virksomheter og offentlige tjenesteeiere. Merknaden i produktregisteret om at dette erstatter «Altinn» som operativ plattformbetegnelse er fortsatt dekkende.

## Kapabiliteter
- **Samarbeid: Tjenesteforvaltning** støtter felles plattformforvaltning, livsløp og styring av tjenester som bygges og kjøres i Altinn.
- **Tjenesteutvikling: Gjenbrukbare tjenester** gir standardiserte byggeklosser og plattformmønstre som kan brukes på tvers av mange tjenester.
- **Tjenesteutvikling: Integrerbare tjenester** gjør det mulig å koble tjenester til andre Altinn-produkter og eksterne systemer gjennom standardiserte API-er og plattformtjenester.

## Produktmål
**Primærkilder:** Altinn Studio-dokumentasjonen, arkitekturdokumentasjon for Altinn Apps og overordnet Altinn-dokumentasjon.

Dokumenterte mål:
- Gi tjenesteeiere et felles grunnlag for å utvikle og kjøre digitale tjenester i Altinn.
- Gjøre det enklere å bygge tjenester med universell utforming, standardiserte komponenter og støtte for både skjema- og API-basert innsending.
- Tilby felles plattformtjenester som reduserer behovet for lokal utvikling av grunnleggende funksjoner.

Operative mål utledet fra de samme kildene:
- Skille tydeligere mellom utviklingsflate, kjøretidsmiljø og tilgrensende fellestjenester i Altinn-porteføljen.
- Gi tjenester et mer standardisert drifts- og deploymønster gjennom Altinn Apps og tilhørende plattformkapabiliteter.
- Understøtte modernisering fra eldre Altinn-løsninger til nyere plattformmønstre.

**Deduksjon:** Plattformen har også en viktig strategisk rolle som standardiseringslag i Altinn, slik at nye tjenester i mindre grad må etablere egne tekniske grunnmønstre fra bunnen av.

## Brukerbehov
- Tjenesteeiere trenger en plattform som reduserer tiden fra behov til digital tjeneste i produksjon.
- Utviklingsteam trenger et konsistent utviklings- og deploymønster for tjenester som skal kjøre i Altinn.
- Arkitektur- og forvaltningsmiljøer trenger en tydeligere avgrensning mellom plattformen og de spesialiserte produktene som bruker den.
- Sluttbrukere trenger tjenester som fremstår mer konsistente på tvers av virksomheter fordi de bygger på samme plattformmønstre.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige tjenesteeiere | Etablere og forvalte digitale tjenester raskere | Planlegging, utvikling og livsløpsforvaltning av Altinn-tjenester | Bruker plattformen som felles grunnlag i stedet for egen teknisk grunnmur |
| Utviklings- og integrasjonsteam | Standardiserte utviklings- og deploymønstre | Bygging av tjenester i Altinn Studio og kjøring i Altinn Apps | Trenger både utviklerflate og plattformtjenester |
| Arkitektur- og produktmiljøer | Tydelig produkt- og plattformavgrensning | Porteføljestyring, modernisering og gjenbruksvurderinger | Viktig fordi flere Altinn-produkter ligger oppå samme plattform |
| Drifts- og forvaltningsmiljøer | Forutsigbar drift og skalerbare kjøretidsmønstre | Forvaltning av kjøretidsmiljø, deploy og plattformtjenester | Møter produktet som drifts- og plattformgrunnlag |
| Sluttbrukere indirekte gjennom tjenestene | Mer sammenhengende og konsistente tjenester | Innsending, dialog og bruk av tjenester bygget på Altinn | Bruker ikke plattformen direkte, men påvirkes av den |

## Hovedfunksjoner
Altinn 3 plattform gir først og fremst et felles teknisk og operativt fundament for digitale tjenester. Den ene hovedflaten er utviklingsflaten i Altinn Studio, der tjenesteeiere og utviklere kan modellere skjema, data, prosess og integrasjoner. Den andre hovedflaten er kjøretidsmiljøet i Altinn Apps, der de ferdige tjenestene deployes og kjøres. Produktet må derfor beskrives som både utviklingsplattform og kjøretidsplattform, ikke bare som en IDE eller bare som en samling API-er.

Plattformen dekker også mer enn rene utviklerverktøy. Dokumentasjonen viser at tjenester bygget i Altinn kan få støtte for universell utforming, standardkomponenter, innsending via både skjema og API, integrasjon med eksterne datakilder og bruk av felles sikkerhets- og plattformtjenester. Dette gjør plattformen relevant når målet er å etablere komplette digitale tjenester med et standardisert grunnmønster, ikke bare når man trenger et verktøy for å kode.

En viktig funksjon ved produktet er å gi tjenester et felles deploy- og driftsmønster. Altinn Apps beskrives som kjøretidsmiljøet der hver app kjøres som egne containere i Kubernetes-baserte miljøer. Dette gir en tydeligere operativ plattformrolle enn i de eldre Altinn-beskrivelsene, og skiller produktet fra mer sluttbrukernære løsninger som Dialogporten, Melding og Varsling.

Produktet omfatter samtidig ikke alle Altinn-funksjoner som egne innebygde delprodukter. Autorisasjon, Melding, Varsling, Dialogporten og andre tilgrensende områder bør fortsatt beskrives som egne produkter når behovet gjelder deres spesifikke funksjon. Altinn 3 plattform er riktig ressurs når vurderingen gjelder det samlede fundamentet for tjenesteutvikling, kjøring og plattformsamhandling i Altinn.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Utviklingsflate for Altinn-tjenester gjennom Altinn Studio | Fagspesifikk forretningslogikk i den enkelte tjeneste |
| Kjøretidsmiljø for apper og tjenester gjennom Altinn Apps | Egen beskrivelse av alle spesialiserte Altinn-produkter som Melding, Varsling og Dialogporten |
| Standardiserte plattformtjenester og integrasjonsmønstre | Altinn 2 som separat produktbetegnelse |
| Grunnlag for innsending, prosess, data og integrasjon i tjenester | Full brukerportalbeskrivelse som egen ressurs |
| Moderniserings- og standardiseringsgrunnlag for nye Altinn-tjenester | Alle sektorinterne systemer som kobles til plattformen |
### Typiske brukssituasjoner (generisk)
- Offentlig virksomhet vil etablere en ny digital tjeneste med skjema, prosessflyt og datautveksling på Altinn-plattformen.
- Eksisterende tjeneste migreres fra Altinn 2 til ny plattform og trenger det nye kjøretids- og utviklingsrammeverket.
- Tjeneste trenger tilgang til felles infrastruktur for innlogging, autorisasjon, melding og varsling som plattformtjenester.

### Når Altinn (plattform) normalt ikke er førstevalg
- Når behovet kun gjelder ett spesialisert produkt som Altinn Melding, Dialogporten eller Altinn Autorisasjon – da er det aktuelle enkeltproduktet mer treffende.
- Når tjenesten ikke skal bygge i Altinn, men i en annen tjenesteplattform.
- Når behovet er generell applikasjonsutvikling utenfor Altinn-rammeverket.

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 26. mars 2026):**
- Dokumentasjonen viser løpende videreutvikling av Altinn Studio, Altinn Apps og tilgrensende plattformkapabiliteter.
- Flere produktområder i Altinn har egne overgangs- og moderniseringsløp, noe som viser at plattformen fortsatt utvikles som samlet fundament.

**Ikke offentlig dokumentert i brukte kilder:** En samlet, detaljert offentlig roadmap for hele Altinn 3 plattform som ett eget dokument.

**Deduksjon:** Videreutviklingen vil trolig fortsatt handle om bedre utviklerstøtte, mer moden kjøretidsforvaltning og videre modernisering av samspillet mellom plattformen og de spesialiserte Altinn-produktene.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere
- Reduserer behovet for å bygge egen teknisk grunnmur for digitale tjenester.
- Gir raskere etablering av tjenester gjennom gjenbruk av standardkomponenter og plattformmønstre.

### For utviklings- og forvaltningsmiljøer
- Gir et mer forutsigbart utviklings-, deploy- og driftsmønster for tjenester i Altinn.
- Gjør det enklere å skille mellom hva som er plattformansvar og hva som er tjenestespesifikt ansvar.

### For offentlig sektor
- Øker gjenbruk av nasjonale løsninger og reduserer variasjon i tekniske grunnmønstre.
- Støtter mer sammenhengende digitalisering ved at flere tjenester bygges på samme plattformgrunnlag.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk og styring | Tjenesteeiere kan forutsette at plattformen alene løser regelverkskrav som egentlig må håndteres i tjenesten | Tydelig ansvarsdeling mellom plattform og tjenesteeier |
| Teknisk | Avhengighet til felles plattformmønstre kan gjøre endringer mer krevende for mange tjenester samtidig | Versjonering, tydelig dokumentasjon og kontrollert innføring av endringer |
| Sikkerhet | Feil bruk av felles sikkerhets- og plattformtjenester kan gi svakere tjenestebeskyttelse enn forutsatt | Standardmønstre, referanseimplementasjoner og tydelige integrasjonskrav |
| Forvaltning | Uklare grenser mellom plattformen og tilgrensende Altinn-produkter kan gi feil produktvalg | Tydeligere produktbeskrivelser og bedre avgrensning i porteføljen |
| Brukeropplevelse | Standardisert plattformbruk gir ikke automatisk god tjenestekvalitet hvis tjenestedesign og innhold er svakt | Kombinere plattformgjenbruk med god tjenesteutforming og kvalitetssikring |

## Kanaler
- Altinn Studio dokumentasjon: https://docs.altinn.studio/nb/
- Hva får du med Altinn Studio: https://docs.altinn.studio/nb/altinn-studio/v8/what-do-you-get/
- Altinn Apps arkitektur: https://docs.altinn.studio/en/technology/architecture/capabilities/runtime/appdeploy/
- Altinn.no: https://www.altinn.no/

## Plattform
Altinn 3 plattform er selv plattformlaget i denne produktbeskrivelsen, og omfatter både utviklingsflate, kjøretidsmiljø og felles tekniske kapabiliteter i Altinn.

**Fakta:** Offentlig dokumentasjon beskriver Altinn Apps som kjøretidsmiljø for apper utviklet i Altinn Studio, med deploy og kjøring i Kubernetes-baserte miljøer. Dokumentasjonen viser også standard støtte for både skjemabasert og API-basert innsending.

**Ikke offentlig dokumentert i brukte kilder:** Full samlet driftsmodell, intern kostnadsfordeling og alle detaljer om intern plattformorganisering på tvers av hele Altinn-porteføljen.

## Gjenbruk
**Høy gjenbruksverdi:**
- Plattformen gir et felles grunnmønster som kan brukes av mange offentlige tjenester.
- Samme utviklings- og kjøretidsmodell kan gjenbrukes på tvers av sektorer og tjenestetyper.
- Produktet er særlig relevant når behovet gjelder etablering av nye Altinn-baserte tjenester, ikke når behovet gjelder én spesialisert funksjon som varsling eller meldingsboks.


### Vanlige kombinasjoner med andre produkter
- **Altinn Studio** – er utviklingsflaten som brukes til å bygge tjenester som kjøres på plattformen.
- **Altinn Autorisasjon** – integreres tett med tjenester som trenger representasjon og tilgangsstyring.
- **Altinn Melding og Dialogporten** – brukes for korrespondanse og dialogeksponering fra apper på plattformen.
- **ID-porten** – brukes for innlogging i tjenester som er deployet på Altinn.

**Kildekode:** Åpen kildekode. Lisens: MIT. Kildekode: [github.com/Altinn](https://github.com/Altinn) (flere repositorier).

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger** realiseres ved at flere tjenester kan bygge på samme plattformgrunnlag.
- **P6: Lag digitale løsninger som støtter samhandling** styrkes fordi plattformen tilbyr standardiserte mønstre for integrasjon og samspill med andre produkter.
- **P7: Sørg for tillit til oppgaveløsningen** støttes indirekte gjennom felles sikkerhets- og plattformkapabiliteter som tjenester kan bygge på.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Separat finansieringsmodell for Altinn 3 plattform isolert fra øvrig Altinn-portefølje.
- **Deduksjon:** Plattformen må forstås som del av den samlede Altinn-forvaltningen og porteføljeøkonomien, ikke som et helt separat finansiert sluttbrukerprodukt.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir / Altinn-forvaltningen | Offisiell Altinn-dokumentasjon |
| Driftsansvar | Altinns forvaltnings- og driftsmiljø | Altinn Apps og plattformdokumentasjon beskriver felles kjøretids- og plattformmodell |
| Budsjettansvar | Del av Altinn-porteføljen | Offentlige kilder beskriver porteføljeforvaltning, men ikke separat kostnadsmodell for denne ressursen |
| Styringsmodell | Produkt- og porteføljeforvaltning i Altinn | Fremgår indirekte av produktstrukturen og dokumentasjonen |

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/
- https://docs.altinn.studio/nb/altinn-studio/v8/what-do-you-get/
- https://docs.altinn.studio/en/technology/architecture/capabilities/runtime/appdeploy/
- https://www.altinn.no/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/19-Altinn-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.altinn.studio/nb/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/altinn-studio/v8/what-do-you-get/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/en/technology/architecture/capabilities/runtime/appdeploy/ (kontrollert 2026-03-26)
- Nettkilde: https://www.altinn.no/ (kontrollert 2026-03-26)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Plattformbeskrivelsen er strammet inn mot offentlig dokumenterte plattformflater i Altinn Studio og Altinn Apps.
- Uverifiserte påstander om volum, kostnader, AI/ML, drift og eksakte styringsforhold er tatt ut.
- Produktet er tydeligere avgrenset mot spesialiserte Altinn-produkter som Melding, Varsling og Dialogporten.

### Tekstlige forbedringer
- Navn, kort beskrivelse og hovedfunksjoner beskriver nå hele plattformens operative rolle, ikke en uklar blanding av «Altinn» som merkevare og flere delprodukter.
- Hovedfunksjoner er skrevet om til forklarende avsnitt i tråd med oppdatert instruks.
- Språket er gjort mer presist og sammenlignbart med nyere produkt-canvas i repoet.



