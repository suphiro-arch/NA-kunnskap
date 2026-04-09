# Produkt-canvas: Altinn Studio

## Navn
Altinn Studio

## Ressurs ID
DIGDIR-018

## Status/Livsfase
**Produksjon** - etablert utviklingsflate i Altinn med aktiv videreutvikling av verktøy, maler og utviklerstøtte.

**Fakta:** Offisiell dokumentasjon beskriver Altinn Studio som inngangen for å utvikle tjenester i Altinn, med støtte for blant annet tilgjengelige tjenester, både skjema- og API-basert innsending, skjemakomponenter, prosessflyt, integrasjon med eksterne datakilder og støtte for lokal utvikling per 26. mars 2026.

## Modenhet
**Høy funksjonell modenhet** - produktet er tydelig etablert som hovedflate for tjenesteutvikling i Altinn:
- Dokumentasjonen dekker både oppstart, daglig utvikling, lokal test og teknisk referanse.
- Løsningen tilbyr et bredt sett av standardfunksjoner som kan brukes uten å bygge alt fra bunnen av.
- Produktet er tett koblet til Altinn Apps som kjøretidsmiljø, men har en tydelig egen rolle som utviklings- og designflate.

**Deduksjon:** Altinn Studio er modent som utviklingsprodukt, men må beskrives sammen med sin kobling til kjøretidsmiljøet for at helheten skal forstås riktig.

## Kort beskrivelse
Altinn Studio er Altinns utviklingsflate for å bygge digitale tjenester. Produktet gir tjenesteeiere og utviklingsteam et felles miljø for å modellere skjema, data, prosess, validering og integrasjoner, og for å klargjøre tjenester for kjøring i Altinn Apps.

Produktet er bredere enn en enkel editor eller et low-code-verktøy. Dokumentasjonen viser at Altinn Studio også fungerer som et samlet arbeidsmønster for tjenesteutvikling, med støtte for universell utforming, standardkomponenter, både skjema- og API-basert innsending, integrasjon med eksterne datakilder og lokal utvikling. Det gjør produktet relevant når behovet er å utvikle Altinn-tjenester innenfor et standardisert rammeverk, ikke når behovet bare er drift eller bare én enkelt integrasjon.

## Kapabiliteter
- **Tjenesteutvikling: Gjenbrukbare tjenester** støttes gjennom standardkomponenter, maler og mønstre som kan brukes i flere tjenester.
- **Tjenesteutvikling: Integrerbare tjenester** gjør det mulig å bygge tjenester som bruker eksterne datakilder, API-er og andre Altinn-komponenter.
- **Tjenesteutvikling: Tjenestedesign** støttes gjennom modellering av skjema, prosess og brukerrettet flyt.
- **Tjenesteutvikling: Utviklings- og kjøretidsmiljø** er en sterk kobling fordi Studio er utviklingsflaten som leder videre til kjøring i Altinn Apps.

## Produktmål
**Primærkilder:** Altinn Studio-dokumentasjonen, «Hva får du?» og kom-i-gang-materialet.

Dokumenterte mål:
- Gjøre det enklere å utvikle tjenester i Altinn.
- Tilby standard støtte for tilgjengelige og responsive tjenester.
- Støtte både skjema- og API-basert innsending med samme datamodell og valideringsregler.
- Gi utviklere funksjoner for skjema, prosess, datamodell og integrasjon i én samlet utviklingsflate.

Operative mål utledet fra de samme kildene:
- Redusere behovet for at hver tjenesteeier etablerer egne grunnmønstre for utvikling av Altinn-tjenester.
- Gjøre det enklere å kombinere visuell modellering og mer teknisk utvikling innenfor samme plattform.
- Støtte hele løpet fra oppstart og lokal utvikling til deploy i kjøretidsmiljøet.

**Deduksjon:** Produktet har også et tydelig standardiseringsmål ved at flere tjenester kan bygges innenfor samme utviklingsmønster og dermed bli mer sammenlignbare og lettere å forvalte.

## Brukerbehov
- Tjenesteeiere trenger et felles rammeverk for å utvikle digitale tjenester raskere.
- Utviklingsteam trenger et miljø som samler skjema, data, prosess og integrasjoner.
- Arkitektur- og forvaltningsmiljøer trenger et standardisert utviklingsmønster som passer sammen med øvrige Altinn-produkter.
- Test- og driftsnære miljøer trenger tydelig samspill mellom lokal utvikling, test og kjøring i Altinn Apps.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige tjenesteeiere | Etablere og videreutvikle tjenester raskere | Planlegging og utvikling av nye Altinn-tjenester | Bruker Studio som hovedinngang til tjenesteutvikling |
| Utviklings- og integrasjonsteam | Modellering, koding og integrasjon | Skjema, data, logikk, API-er og eksterne kilder | Trenger både visuell støtte og teknisk fleksibilitet |
| Design- og fagmiljøer | Tilgjengelige og brukervennlige tjenester | Utforming av skjema, prosess og tjenesteflyt | Møter produktet gjennom standardkomponenter og rammer |
| Test- og forvaltningsmiljøer | Forutsigbart utviklings- og testløp | Lokal utvikling, test og klargjøring for deploy | Viktig for kvalitet og kontroll før produksjon |
| Arkitektur- og produktmiljøer | Standardisert plattformbruk | Gjenbruk, produktavgrensning og styring | Må skille Studio fra plattformen som helhet og fra kjøretidslaget |

## Hovedfunksjoner
Altinn Studio gir en samlet utviklingsflate for å bygge tjenester i Altinn. Dokumentasjonen viser støtte for skjemakomponenter, prosessflyt, datamodell og valideringsregler. Dette gjør produktet relevant når behovet er å etablere eller videreutvikle komplette digitale tjenester, ikke bare redigere enkeltstående skjema eller kodefragmenter.

Et viktig kjennetegn ved produktet er at det kombinerer brukerrettet modellering med mer teknisk utvikling. Tjenester kan utvikles med støtte for både skjema- og API-basert innsending, basert på samme datamodell og valideringsregler. Studio er dermed ikke bare et visuelt verktøy; det er også et utviklingsprodukt som binder sammen data, logikk og integrasjoner i tjenesten.

Dokumentasjonen viser også at Altinn Studio støtter integrasjon med eksterne datakilder og lokal utvikling. Dette utvider produktets rolle fra å være en ren nettflate til å være del av et større utviklingsløp. Tjenesteeiere og utviklere kan bruke produktet til å komme i gang, arbeide lokalt, teste og klargjøre tjenesten før den kjøres i Altinn Apps. Koblingen til kjøretidsmiljøet er derfor sentral for å forstå hva produktet faktisk leverer.

Samtidig dekker ikke Altinn Studio alt som trengs for å levere en komplett tjeneste alene. Produktet erstatter ikke kjøretidsmiljøet, autorisasjonsproduktet eller spesialiserte samhandlingsprodukter som Melding og Varsling. Det er riktig produkt når vurderingen gjelder selve utviklingsflaten og utviklingsmønsteret for Altinn-tjenester.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Utviklingsflate for skjema, data, prosess og validering | Selve kjøretidsmiljøet som eget produkt |
| Støtte for både skjema- og API-basert innsending | Faglig innhold og regelverk i den enkelte tjeneste |
| Standardkomponenter og mønstre for tjenesteutvikling | Full separat beskrivelse av øvrige Altinn-produkter |
| Integrasjon med eksterne datakilder og lokal utvikling | Drift og forvaltning av alle produksjonsmiljøer som egen funksjon |
| Klargjøring for deploy til Altinn Apps | Alle typer applikasjonsutvikling utenfor Altinn-rammeverket |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-26):**
- Dokumentasjonen viser at Altinn Studio videreutvikles gjennom oppdaterte guider, referanser og støtte for flere utviklingsoppgaver.
- Altinn Studio beskrives som gjeldende utviklingsmodell for nye tjenester i Altinn.

**Ikke offentlig dokumentert i brukte kilder:** En samlet, detaljert roadmap med tidsfestede leveranser for produktet.

**Deduksjon:** Videreutviklingen vil sannsynligvis fortsette å styrke utvikleropplevelse, komponentstøtte og sammenhengen mellom Studio og kjøretidsmiljøet, men dette bør ikke detaljbeskrives utover det som er offentlig dokumentert.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere
- Reduserer terskelen for å etablere tjenester i Altinn ved å tilby et ferdig utviklingsmønster.
- Gjør det enklere å bygge tjenester som følger samme grunnstruktur og kvalitetskrav.

### For utviklings- og fagmiljøer
- Samler skjema, data, prosess og integrasjon i én utviklingsflate.
- Gjør det mulig å kombinere standardisering og fleksibilitet i utviklingsarbeidet.

### For offentlig sektor
- Øker gjenbruk av standardkomponenter og utviklingsmønstre på tvers av virksomheter.
- Støtter mer konsistente digitale tjenester gjennom en felles utviklingsplattform.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk og faglig | Tjenesteeiere kan forveksle teknisk støtte i Studio med ferdig ivaretakelse av faglige og rettslige krav | Tydelig ansvar for tjenesteinnhold og regelverk hos tjenesteeier |
| Teknisk | Feil bruk av mønstre, datamodell eller integrasjoner kan gi svake tjenester selv om plattformen er god | Referanseguider, test og tydelig dokumentasjon |
| Sikkerhet | Tjenester kan implementeres med utilstrekkelig forståelse for samspill med sikkerhetskomponenter | Standardmønstre og klar veiledning for integrasjon med andre Altinn-produkter |
| Forvaltning | Uklart skille mellom Studio, plattformen og kjøretidsmiljøet kan skape feil forventninger | Tydelig produktavgrensning og god porteføljebeskrivelse |
| Brukeropplevelse | Standardkomponenter gir ikke automatisk god tjenestedesign eller godt innhold | Kombinere plattformgjenbruk med aktiv kvalitetssikring og tjenestedesign |

## Kanaler
- Produktside og dokumentasjon: https://docs.altinn.studio/nb/
- Hva får du?: https://docs.altinn.studio/nb/altinn-studio/v8/what-do-you-get/
- Kom i gang: https://docs.altinn.studio/en/altinn-studio/v8/getting-started/
- Lokal utvikling og test: https://docs.altinn.studio/nb/altinn-studio/guides/development/setup/developer-guides/local-test/

## Plattform
Utviklingsflate i Altinn-porteføljen som leder videre til deploy og kjøring i Altinn Apps.

**Fakta:** Dokumentasjonen viser støtte for tilgjengelige tjenester, skjemakomponenter, prosessflyt, integrasjon med eksterne datakilder, både skjema- og API-basert innsending og lokal utvikling. Produktet er dermed både en utviklerflate og en standardisert utviklingsmodell.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsmodell og detaljert kostnadsmodell for Studio alene.

## Gjenbruk
**Høy gjenbruksverdi:**
- Studio gjør det mulig å gjenbruke standardkomponenter og mønstre på tvers av mange tjenester.
- Samme utviklingsgrunnlag kan brukes av flere virksomheter i Altinn.
- Gjenbruksverdien er størst når behovet er å bygge tjenester innenfor Altinns modell, ikke når behovet gjelder generell applikasjonsutvikling utenfor Altinn.

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov** støttes gjennom vekt på tilgjengelige og brukervennlige tjenester.
- **P5: Del og gjenbruk løsninger** realiseres gjennom felles komponenter og utviklingsmønstre.
- **P6: Lag digitale løsninger som støtter samhandling** styrkes ved at tjenester bygges for samspill med andre Altinn-produkter og eksterne datakilder.
- **P7: Sørg for tillit til oppgaveløsningen** støttes indirekte gjennom standardiserte utviklingsmønstre og kobling til øvrige sikkerhetsmekanismer i Altinn.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Separat finansieringsmodell eller kostnadsnivå for Altinn Studio isolert fra den øvrige Altinn-porteføljen.
- **Deduksjon:** Produktet må forstås som del av Altinns samlede plattformforvaltning og finansiering.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir / Altinn-forvaltningen | Offisiell Altinn-dokumentasjon |
| Driftsansvar | Altinns forvaltnings- og driftsmiljø | Studio og Altinn Apps er dokumentert som del av samme portefølje |
| Budsjettansvar | Del av Altinn-porteføljen | Ingen separat offentlig kostnadsmodell verifisert |
| Styringsmodell | Produktforvaltning i Altinn | Fremgår av dokumentasjon og produktstruktur |

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/
- https://docs.altinn.studio/nb/altinn-studio/v8/what-do-you-get/
- https://docs.altinn.studio/en/altinn-studio/v8/getting-started/
- https://docs.altinn.studio/nb/altinn-studio/guides/development/setup/developer-guides/local-test/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/produkter/produktbeskrivelser/20-Altinn-Studio-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.altinn.studio/nb/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/altinn-studio/v8/what-do-you-get/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/en/altinn-studio/v8/getting-started/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/altinn-studio/guides/development/setup/developer-guides/local-test/ (kontrollert 2026-03-26)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen er oppdatert mot gjeldende Altinn Studio-dokumentasjon og nyere veiledning for utvikling og lokal test.
- Uverifiserte påstander om volum, kostnader, AI-assistanse og intern plattformteknologi er fjernet.
- Produktet er tydeligere avgrenset mot Altinn 3 plattform som helhet og mot Altinn Apps som kjøretidsmiljø.

### Tekstlige forbedringer
- Hovedfunksjoner forklarer nå Studio som samlet utviklingsflate og arbeidsmønster, ikke bare som IDE.
- Språket er gjort mer presist og målrettet mot nasjonal arkitektur.
- Dokumentet følger nå nyere struktur og presisjonsnivå i repoet.
