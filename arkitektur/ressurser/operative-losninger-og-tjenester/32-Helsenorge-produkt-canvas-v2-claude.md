# Produkt-canvas: Helsenorge

## Navn
Helsenorge

## Ressurs ID
NHN-001

## Status/Livsfase
**Produksjon** - etablert nasjonal innbyggerportal for informasjon om og tilgang til digitale helsetjenester.

**Fakta:** Helsenorge beskrives som den offentlige nettportalen for informasjon om og tilgang til helsetjenester for innbyggere i Norge. Norsk helsenett har ansvar for drift og utvikling av nettstedet, mens innhold og tjenester leveres av flere aktører i helsesektoren.

## Modenhet
**Høy modenhet** - nasjonal og bredt innarbeidet innbyggertjeneste:
- Helsenorge er etablert som den felles inngangen til mange digitale helsetjenester for innbyggere.
- Produktet kombinerer informasjonstjenester og innloggede selvbetjeningsløsninger.
- Innhold og funksjoner kommer fra flere offentlige helseaktører og sykehus.
- Portalen brukes som felles presentasjonslag for flere nasjonale e-helseløsninger.

**Deduksjon:** Modenheten er høy fordi Helsenorge er en stabil og sentral innbyggerflate i helsesektoren, men gjenbruksverdien ligger mer i samordnet tjenestetilgang enn i tekniske byggeklosser for andre sektorer.

## Kort beskrivelse
Helsenorge er den nasjonale portalen der innbyggere finner kvalitetssikret helseinformasjon og får tilgang til digitale selvbetjeningsløsninger i helse- og omsorgssektoren. Produktet samler tjenester fra flere aktører i én felles inngang, slik at brukeren kan orientere seg, logge inn og utføre helseadministrative oppgaver uten å forholde seg til hvert enkelt underliggende system. Helsenorge er derfor først og fremst en sammenhengende tjenesteflate for innbyggere, ikke en generell delingsplattform.

Portalen er også stedet der innbyggeren styrer sitt eget personvern i helsesektoren. Herfra gis og trekkes samtykke, gis fullmakt til andre, og settes sperring og blokkering av helsepersonells tilgang til opplysninger i andre nasjonale helseløsninger. Denne styringsflaten er en selvstendig funksjon i produktet, ikke bare en presentasjon av innstillinger som forvaltes andre steder.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Helsenorges om-side, personverninnstillingene og NHNs rollebeskrivelse. Tillitskapabilitetene er knyttet til personverninnstillingene, der innbyggeren selv forvalter rettigheter. Håndhevingen av de samme rettighetene skjer i de underliggende løsningene, blant annet `Kjernejournal`.

- **Sluttbrukertjenester: Sammenhengende tjenester** samler flere helsetjenester og informasjonsløp i én felles inngang for innbyggere.
- **Sluttbrukertjenester: Tjenestekjeder** lar brukeren bevege seg mellom informasjon, innlogging og flere ulike helserelaterte tjenester innen samme overordnede produktflate.
- **Tillit: Representasjon** gjør det mulig å opptre på vegne av andre gjennom fullmakt med selvvalgt omfang, og gir foreldre representasjon for barn under 16 år.
- **Tillit: Samtykke** er stedet innbyggeren gir, endrer og trekker tilbake samtykke, blant annet samtykke til at barn mellom 13 og 16 år kan bruke enkelte tjenester, og samtykke til at apotek kan hente ut reseptvarer.
- **Tillit: Tilgangsstyring** lar innbyggeren definere, avgrense og trekke tilbake hvem som skal ha tilgang til egne helseopplysninger, gjennom fullmakter, sperring og blokkering av utvalgte helsepersonell.

## Produktmål
**Primærkilder:** Helsenorges side `Om Helsenorge` og NHNs overordnede tjenestebeskrivelser.

Dokumenterte mål:
- Gi innbyggere tilgang til informasjon om helse, livsstil, sykdom, behandling og rettigheter.
- Gi innbyggere tilgang til digitale selvbetjeningsløsninger og helseopplysninger som er registrert om dem.
- Samle innhold og tjenester fra ulike aktører i helsesektoren på ett sted.

Operative mål utledet fra de samme kildene:
- Gjøre digitale helsetjenester enklere å finne og bruke for innbyggerne.
- Skape en felles og gjenkjennelig inngang til nasjonale og sektorvise helsetjenester.
- Redusere behovet for at innbyggerne må orientere seg i mange ulike portaler og virksomhetsflater.

## Brukerbehov
- Innbyggere trenger én samlet inngang til helseinformasjon og digitale helsetjenester.
- Brukere trenger trygg tilgang til egne helseopplysninger og selvbetjeningsfunksjoner.
- Offentlige helseaktører trenger en felles innbyggerflate for å presentere innhold og tjenester.
- Helseforvaltningen trenger en kanal som kan gjøre sektoren mer sammenhengende og brukervennlig.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Innbyggere | Oversikt, informasjon og digital tilgang til helsetjenester | Informasjon, innsyn og selvbetjening | Hovedmålgruppen |
| Pasienter og pårørende | Tilgang til egne eller relevante helseopplysninger | Oppfølging, planlegging og kommunikasjon | Viktig brukergruppe for innloggede tjenester |
| Offentlige helseaktører | Felles kanal mot innbygger | Publisering av tjenester og innhold | Leverer innhold og funksjoner inn i produktet |
| Norsk helsenett | Drift, utvikling og forvaltning | Nasjonal produkt- og plattformforvaltning | Operativ hovedforvalter |

## Hovedfunksjoner
### Primære funksjoner
**Samlet innbyggerinngang til helsetjenester.** Helsenorge gir innbyggerne ett sted å gå til for både informasjon og digitale tjenester i helsesektoren. Dette er produktets hovedverdi og viktigste avgrensning.

**Kvalitetssikret helseinformasjon.** Portalen publiserer informasjon om helse, behandling, rettigheter og livsstil som leveres og kvalitetssikres av offentlige helseaktører og sykehus. Helsenorge er derfor også en nasjonal informasjonskanal.

**Innlogget selvbetjening og innsyn.** Ved innlogging får brukeren tilgang til selvbetjeningsløsninger og innsyn i helseopplysninger. Helsenorge fungerer dermed som presentasjons- og tilgangsflate for flere underliggende tjenester.

**Innbyggerstyrt personvern og fullmakt.** Under personverninnstillingene forvalter innbyggeren selv hvem som får se hva. Her gis og trekkes samtykke, her gis fullmakt til andre personer med selvvalgt omfang fra innsyn til oppgaveutførelse, og her sperres eller blokkeres helsepersonells tilgang til kjernejournalen, enten helt eller for utvalgte deler og utvalgte personer. Innbyggeren kan også velge tjenestenivå, reservere seg mot digitale henvendelser som gjelder andre formål enn helsehjelp, og sperre sin egen tilgang til portalen.

**Sammenkobling av tjenester fra flere aktører.** Produktet samler bidrag fra flere virksomheter i helsesektoren i en felles brukerflate. Dette gjør Helsenorge til en sammenhengende tjenesteflate heller enn en enkeltstående applikasjon.

### Typiske brukssituasjoner (generisk)
- når innbyggere trenger én samlet inngang til informasjon, innlogging og selvbetjening i helsesektoren
- når virksomheter skal vurdere hvordan flere helsetjenester kan presenteres i en sammenhengende innbyggerreise
- når analyser trenger å vurdere om et behov allerede dekkes av eksisterende nasjonal innbyggerflate, før ny kanal etableres
- når det er behov for en felles kanal som kombinerer kvalitetssikret informasjon med tilgang til underliggende digitale tjenester

### Når Helsenorge normalt ikke er førstevalg
- når behovet gjelder teknisk datadeling eller API-integrasjon mellom systemer uten innbyggerflate
- når oppgaven er intern arbeidsstøtte for helsepersonell, ikke innbyggerrettede tjenester
- når man trenger direkte funksjonalitet i et underliggende fagsystem, ikke presentasjons- og tilgangslaget
- når saken primært gjelder overordnet styring eller prioriteringsbeslutninger som hører hjemme i styringsfora

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonal portal for helseinformasjon og digitale helsetjenester | De underliggende fagsystemene og registrene som leverer data |
| Innlogget innbyggerflate for selvbetjening og innsyn | Teknisk API-plattform for generell datadeling på tvers av sektorer |
| Presentasjon og sammenkobling av tjenester fra flere helseaktører | Alle nasjonale e-helseløsninger som egne produkter |
| Kvalitetssikret innhold for innbyggere | Helsepersonellflater og rent interne arbeidsverktøy |
| Innbyggerstyrt samtykke, fullmakt, sperring og blokkering | Håndhevingen av de samme rettighetene i underliggende løsninger |

## Veikart over kommende funksjonalitet
**Fakta fra kildene (kontrollert 2026-03-27):**
- Helsenorge framstår som en løpende utviklet portal med stadig nye selvbetjeningsløsninger.
- NHN beskriver flere nasjonale tjenester som eksponeres mot innbyggere via Helsenorge.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et samlet og tidsfestet veikart for hele Helsenorge er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til å dreie seg om flere innbyggernære tjenester, sterkere sammenkobling med nasjonale e-helseløsninger og gradvis utvidelse av selvbetjeningsområdet.

## Forretningsverdi/Verdiforslag
### For innbyggere
- Gir én gjenkjennelig inngang til informasjon og digitale helsetjenester.
- Gjør det enklere å finne og bruke relevante tjenester i helsesektoren.

### For helseaktører
- Gir en felles kanal mot innbygger i stedet for mange separate innganger.
- Styrker muligheten for sammenhengende tjenester på tvers av virksomheter.

### For sektoren
- Bidrar til mer samordnet digital brukeropplevelse.
- Reduserer fragmentering i møteflaten mot innbygger.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Kompleksitet | Mange aktører og tjenester i samme portal kan gjøre styring og prioritering krevende | Tydelig produktforvaltning og sektorstyring |
| Brukeropplevelse | Ujevn kvalitet mellom underliggende tjenester kan slå ut i den samlede opplevelsen | Felles design- og tjenestekrav |
| Teknisk avhengighet | Feil i underliggende løsninger kan merkes direkte i Helsenorge | Robust integrasjon og tydelig ansvar mellom aktørene |
| Personvern og tillit | Portalen håndterer innsyn i sensitive helseopplysninger | Høy sikkerhet, tydelig tilgangsstyring og god informasjon |
| Scope-glidning | Helsenorge kan oppfattes som én løsning selv om mange produkter ligger under | Tydelig produktavgrensning og sporbarhet til underliggende tjenester |

## Kanaler
- Helsenorge: https://www.helsenorge.no/
- Om Helsenorge: https://www.helsenorge.no/om-helsenorge-no/
- Norsk helsenett - tjenesteoversikt: https://www.nhn.no/tjenester/
- Personverninnstillinger: https://www.helsenorge.no/personverninnstillinger/
- Om innstillinger på Helsenorge: https://www.helsenorge.no/innstillinger/om-innstillinger/

## Plattform
Helsenorge er en nasjonal portal- og tjenesteflate for innbyggere i helsesektoren.

**Fakta:** Produktet består av både åpne informasjonssider og innloggede selvbetjeningsløsninger, og brukes som felles møteflate mellom innbygger og flere underliggende helsetjenester.

**Ikke offentlig dokumentert i brukte kilder:** Full intern plattformarkitektur, samlet komponentkart og detaljert oversikt over alle underliggende tekniske grensesnitt.

## Gjenbruk
**Middels til høy gjenbruksverdi:**
- Produktet har høy verdi som felles innbyggerflate i helsesektoren.
- Det er særlig relevant når behovet er sammenhengende brukeropplevelse og felles kanal mot innbyggere.
- Det er mindre relevant som generell teknisk byggekloss for andre sektorer, fordi hovedverdien ligger i sluttbrukerflaten.

### Vanlige kombinasjoner med andre produkter
- `Kjernejournal`
- `e-resept`
- `HelseID`
- `Helsedata.no` (når innbyggerrettet tjenesteflate og datatilgangsløp må ses i sammenheng)

**Kildekode:** Ikke offentlig dokumentert.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger** styrkes ved at flere helseaktører bruker samme innbyggerflate.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi Helsenorge binder sammen tjenester fra flere aktører i én brukerreise.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi produktet må håndtere sensitive helseopplysninger og høy brukerforventning.

## Finansiering
- **Fakta:** Kildene beskriver NHN som ansvarlig for drift og utvikling, men gir ikke en samlet offentlig finansieringsmodell i denne arbeidsøkten.
- **Deduksjon:** Helsenorge finansieres som en nasjonal fellestjeneste i helsesektoren, kombinert med bidrag og tilknytning fra flere tjenesteeiere.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Norsk helsenett | Om-siden for Helsenorge |
| Drifts- og utviklingsansvar | Norsk helsenett | Om-siden beskriver dette eksplisitt |
| Innholds- og tjenestebidrag | Flere offentlige helseaktører og sykehus | Helsenorge beskriver dette eksplisitt |
| Styringsmodell | Felles innbyggerflate i helsesektoren med NHN som operativ forvalter | Om-siden og tjenestebeskrivelsen |

## Lenke til dokumentasjon
- https://www.helsenorge.no/
- https://www.helsenorge.no/om-helsenorge-no/
- https://www.nhn.no/tjenester/
- https://www.helsenorge.no/personverninnstillinger/
- https://www.helsenorge.no/innstillinger/om-innstillinger/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.helsenorge.no/ (kontrollert 2026-03-27)
- Nettkilde: https://www.helsenorge.no/om-helsenorge-no/ (kontrollert 2026-03-27)
- Nettkilde: https://www.nhn.no/tjenester/ (kontrollert 2026-03-27)
- Nettkilde: https://www.helsenorge.no/personverninnstillinger/ (kontrollert 2026-09-14)
- Nettkilde: https://www.helsenorge.no/innstillinger/om-innstillinger/ (kontrollert 2026-09-14)

## Endringer fra forrige versjon

### Analyseforbedringer
- Tre tillitskapabiliteter er lagt til etter kildesjekk av personverninnstillingene: `Tillit: Samtykke`, `Tillit: Representasjon` og `Tillit: Tilgangsstyring`. `v1` beskrev Helsenorge utelukkende som presentasjonsflate og nevnte ikke samtykke, fullmakt eller sperring med ett ord, selv om dette er dokumenterte funksjoner i produktet.
- Skillet mot `Kjernejournal` er gjort eksplisitt: Helsenorge er stedet rettigheten forvaltes, mens håndhevingen og loggføringen skjer i den underliggende løsningen. Derfor er `Tillit: Sporbarhet og innsyn` ikke satt her, selv om bruksloggen vises i portalen.
- `Hovedfunksjoner` har fått en egen primærfunksjon for innbyggerstyrt personvern og fullmakt, og `Scope og avgrensning` skiller nå forvaltning av rettigheten fra håndhevingen av den.

### Tekstlige forbedringer
- `Kort beskrivelse` sier nå at portalen også er innbyggerens styringsflate for eget personvern, ikke bare en samlet inngang til tjenester.
- `Grunnlag`-teksten i `Kapabiliteter` er flyttet foran kulelista, slik AGENTS.md krever, så den ikke trekkes inn i forklaringen for siste kapabilitet ved metadatasynk.
- Kanaler, dokumentasjonslenker og kildegrunnlag er utvidet med de to sidene som dokumenterer personverninnstillingene.
