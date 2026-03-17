# Produkt-canvas: Altinn autorisasjon

## Navn
Altinn autorisasjon

## Ressurs ID
4

## Status/Livsfase
**Produksjon** - etablert autorisasjonskomponent i Altinn for styring av tilganger, roller og representasjon.

**Fakta:** Altinn-dokumentasjonen beskriver autorisasjon som grunnlaget for tilgang til ressurser og handlinger i Altinn. Dokumentasjonen dekker både overordnet modell, API-er og systembruker i samspill med andre Altinn-komponenter.

## Modenhet
**Høy modenhet** - innarbeidet kjernekomponent med tydelig rolle i Altinns tilgangsmodell:
- Løsningen er dokumentert som en sentral del av Altinns sikkerhets- og tilgangsarkitektur.
- Den støtter både brukerrettigheter, representasjon og API-basert bruk av autorisasjon.
- Den er moden nok til å være et gjenbrukbart mønster for tjenester som bygges i eller tett mot Altinn.
- Samtidig er produktet avhengig av samspillet med andre Altinn-komponenter for autentisering og tjenesteflyt.

**Deduksjon:** Produktet er organisatorisk og teknisk modent, men må forstås som autorisasjonslag i en større Altinn-sammenheng, ikke som en komplett tillitsplattform alene.

## Kort beskrivelse
Altinn autorisasjon er komponenten som avgjør hvem som kan gjøre hva i Altinn, og på hvilket grunnlag. Produktet brukes til å styre tilganger til ressurser, handlinger og tjenester gjennom roller, rettigheter, delegering og representasjon. Løsningen er særlig relevant når behovet er å kontrollere tilgang på vegne av person eller virksomhet i Altinn-sammenheng, ikke når behovet primært er autentisering eller ren datadeling.

## Kapabiliteter
- **Tillit: Tilgangskontroll** er kjernefunksjonen og avgjør om en bruker, virksomhet eller system får utføre en bestemt handling eller bruke en bestemt ressurs.
- **Tillit: Tilgangsstyring** gjør det mulig å forvalte roller, rettigheter og delegeringer som grunnlag for autorisasjonsbeslutninger.
- **Tillit: Representasjon** gjør det mulig å opptre på vegne av virksomhet eller annen part når dette er definert i Altinns rettighetsmodell.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i Altinn-dokumentasjonen og Samarbeidsportalen.

## Produktmål
**Primærkilder:** Altinn-dokumentasjon for autorisasjon og Samarbeidsportalen for Altinn.

Dokumenterte mål:
- Gi Altinn-tjenester et felles grunnlag for tilgangsbeslutninger.
- Støtte roller, rettigheter og representasjon i tjenester og API-er.
- Gjøre det mulig å styre tilganger uten å bygge særskilte lokale autorisasjonsmotorer for hver tjeneste.

Operative mål utledet fra de samme kildene:
- Gjøre autorisasjon gjenbrukbar for flere tjenester i Altinn-porteføljen.
- Gi tjenesteutviklere API-er og mønstre for å kontrollere tilgang i egne løsninger.
- Sikre at representasjon og rettighetsgrunnlag kan brukes konsekvent på tvers av tjenester.

## Brukerbehov
- Tjenesteeiere trenger et felles grunnlag for å avgjøre hvem som har tilgang til hvilke ressurser og handlinger.
- Utviklingsteam trenger dokumenterte API-er og mønstre for autorisasjon i Altinn-baserte tjenester.
- Virksomheter og personer trenger at rettigheter og representasjon håndteres konsistent på tvers av tjenester.
- Forvaltningsmiljøer trenger en løsning som gjør tilgangsregler mer styrbare og mindre avhengige av lokal spesiallogikk.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Tjenesteeiere i Altinn | Felles modell for tilgangsbeslutninger | Tilgang til egne ressurser, skjema og tjenester | Bruker autorisasjon som felles byggestein i stedet for lokal særlogikk |
| Utviklings- og integrasjonsteam | API-er og mønstre for autorisasjon | Implementasjon i tjenester og integrasjoner | Trenger å forstå samspillet mellom autentisering, representasjon og tilgang |
| Virksomheter som bruker Altinn-tjenester | Korrekte roller og rettigheter | Handling på vegne av virksomhet | Møter produktet indirekte gjennom tjenestene |
| Personer med delegert rolle | Representasjon og rettighetsgrunnlag | Utførelse av oppgaver på vegne av andre | Særlig viktig der flere parter inngår i samme prosess |
| Forvaltnings- og sikkerhetsmiljøer | Oversikt og kontroll | Oppfølging av tilgangsmodell og endringer i rettigheter | Avhenger av tydelig rolle- og ansvarsdeling |

## Hovedfunksjoner
### Primære funksjoner
- **Avgjøre tilgang til ressurser og handlinger.** Altinn autorisasjon vurderer om en aktør har rett til å utføre en bestemt handling eller bruke en bestemt ressurs. Dette er kjernen i produktet og dekker behovet for konsekvent tilgangskontroll i Altinn-baserte tjenester.
- **Forvalte roller og rettigheter som grunnlag for tilgang.** Løsningen gir et felles mønster for å uttrykke hvilke rettigheter som finnes, og hvordan de skal brukes i tilgangsvurderinger. Det gjør den relevant når tjenester trenger en felles autorisasjonsmodell, men mindre relevant når behovet bare er enkel autentisering.
- **Håndtere representasjon og delegering.** Produktet gjør det mulig å bruke rettigheter i situasjoner der en person eller et system handler på vegne av en virksomhet eller annen part. Dette skiller Altinn autorisasjon fra enklere tilgangsløsninger som bare vurderer den innloggede brukeren isolert.
- **Tilby API-er og gjenbrukbare autorisasjonsmønstre.** Dokumentasjonen viser hvordan autorisasjon kan brukes programmatisk i tjenester og integrasjoner. Det gjør produktet relevant som byggestein i Altinn-porteføljen, ikke bare som intern funksjon i ett enkelt system.
- **Samvirke med andre tillitskomponenter i Altinn.** Autorisasjon bygger videre på autentisering og andre grunnlagsdata fra omkringliggende løsninger. Det er viktig for å forstå både styrken og avgrensningen i produktet: det avgjør tilgang, men leverer ikke hele tillitskjeden alene.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Tilgangsbeslutninger for ressurser og handlinger | Sluttbrukerinnlogging og identitetsbekreftelse |
| Roller, rettigheter og representasjon | Selve tjenestelogikken i den enkelte fagapplikasjon |
| API-er for autorisasjon i Altinn-sammenheng | Generell nasjonal autentisering for tjenester utenfor Altinn |
| Gjenbrukbare mønstre for tilgang i Altinn | Full erstatning for lokal prosess- og sakslogikk |
| Samspill med andre Altinn-komponenter | Dokumentsignering eller egen varslingsfunksjon |

## Veikart over kommende funksjonalitet
**Fakta fra Altinn-dokumentasjon og Samarbeidsportalen (hentet 2026-03-17):**
- Dokumentasjonen viser fortsatt utvikling av API-er, systembruker og autorisasjonsmønstre.
- Samarbeidsportalen for Altinn viser at produktområdet inngår i en løpende porteføljeforvaltning med kostnads- og tjenesteinformasjon.

**Deduksjon:** Veikartet peker mot videre forbedring av gjenbrukbare autorisasjonsmønstre i Altinn, særlig der tjenester trenger tydeligere samspill mellom roller, representasjon og maskinell bruk.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere
- Reduserer behovet for å bygge egne autorisasjonsmekanismer i hver tjeneste.
- Gjør det lettere å bygge tjenester som håndterer rettigheter og representasjon konsekvent.
- Senker risiko for ulik praksis mellom tjenester som ellers ville løst tilgang på forskjellige måter.

### For virksomheter og brukere
- Gir mer forutsigbar bruk av rettigheter på tvers av Altinn-tjenester.
- Gjør det enklere å opptre på vegne av virksomhet der dette er del av tjenestens behov.

### For offentlig sektor og porteføljen
- Styrker gjenbruk i Altinn-porteføljen ved at tjenester kan bygge på samme autorisasjonsmodell.
- Gjør det lettere å skille mellom behov for autentisering, autorisasjon og representasjon når nye løsninger vurderes.
- Bidrar til mer konsistente tilgangsregler i tjenester som ellers kunne utviklet forskjellige lokale løsninger.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk og regelverk | Feil oversettelse av rettslige krav til roller og tilganger kan gi feil autorisasjonsbeslutninger | Tett samspill mellom fag, juss og teknisk modellering |
| Teknisk | Feil bruk av API-er eller uklare integrasjonsmønstre kan gi feil tilgang eller avvisning | Tydelig dokumentasjon, test og referansemønstre |
| Sikkerhet | For bred delegering eller feil representasjonsoppsett kan gi større tilgang enn ønsket | Begrensede rettigheter, revisjon av oppsett og tydelig ansvar hos tjenesteeier |
| Avhengigheter | Feil forståelse av samspillet med ID-porten og Maskinporten kan føre til at produktet brukes til feil behov | Klar avgrensning mellom autentisering og autorisasjon |
| Brukbarhet | Komplekse rettighetsmodeller kan bli vanskelig å forstå og forvalte | Enklere forvaltningsmønstre og tydeligere begrepsbruk |

## Kanaler
- Samarbeidsportal: https://samarbeid.digdir.no/altinn/autorisasjon/2344
- Overordnet dokumentasjon: https://docs.altinn.studio/en/authorization/about/
- API-dokumentasjon: https://docs.altinn.studio/en/api/authorization/
- Systembruker: https://docs.altinn.studio/en/authorization/what-do-you-get/systemuser/
- Kostnader i Altinn-porteføljen: https://samarbeid.digdir.no/altinn/kostnader/2627

## Plattform
Altinn autorisasjon er en felles autorisasjonsplattform i Altinn som brukes av tjenester og API-er som trenger tilgangsstyring, rettighetsvurdering og representasjon.

**Fakta:** Dokumentasjonen beskriver produktet gjennom autorisasjons-API-er, rettighetsmodell og systembruker-scenarier. Det viser at produktet er laget for å inngå som del av en større Altinn-arkitektur.

**Ikke offentlig dokumentert i brukte kilder:** Full detalj om runtime-arkitektur, driftsplattform og detaljert kostnadsfordeling per komponent.

## Gjenbruk
**Høy gjenbruksverdi innenfor Altinn-sammenheng:**
- Produktet er relevant når behovet er å styre tilganger og representasjon på tvers av tjenester i Altinn.
- Det er mindre relevant dersom behovet bare er innlogging eller enkel API-autentisering, der andre produkter er mer presise.
- Den viktigste gjenbruksverdien ligger i å standardisere tilgangsmodellen på tvers av flere tjenester, ikke i å være en generell løsning for alle typer tilgangsproblemer utenfor Altinn.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger** realiseres ved at autorisasjon tilbys som felles byggestein for flere tjenester.
- **P6: Lag digitale løsninger som støtter samhandling** styrkes fordi flere tjenester kan bygge på samme rettighets- og representasjonsmodell.
- **P7: Sørg for tillit til oppgaveløsningen** støttes gjennom konsistente tilgangsbeslutninger og tydelig rollegrunnlag.

## Finansiering
- **Fakta:** Samarbeidsportalen beskriver kostnader for Altinn-porteføljen.
- **Ikke fullt offentlig dokumentert i brukte kilder:** Separat kostnadsnivå og finansieringsmodell for Altinn autorisasjon isolert fra resten av Altinn.
- **Deduksjon:** Produktet må forstås som del av en større porteføljeøkonomi i Altinn, ikke som et separat produkt med helt egen offentlig prisstruktur.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) / Altinn | Altinn-dokumentasjon og Samarbeidsportalen |
| Driftsansvar | Ikke eksplisitt navngitt i brukte offentlige kilder på komponentnivå | Offentlige kilder beskriver ikke detaljert driftsmodell for denne komponenten alene |
| Budsjett- og kostnadsmodell | Del av Altinn-porteføljen | Samarbeidsportalen |
| Styringsmodell | Del av Altinns løpende porteføljeforvaltning | Samarbeidsportalen |

## Lenke til dokumentasjon
- https://samarbeid.digdir.no/altinn/autorisasjon/2344
- https://docs.altinn.studio/en/authorization/about/
- https://docs.altinn.studio/en/api/authorization/
- https://docs.altinn.studio/en/authorization/what-do-you-get/systemuser/
- https://samarbeid.digdir.no/altinn/kostnader/2627

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `results/Produktbeskrivelser/04-Altinn-autorisasjon-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://samarbeid.digdir.no/altinn/autorisasjon/2344 (hentet 2026-03-17)
- Nettkilde: https://docs.altinn.studio/en/authorization/about/ (hentet 2026-03-17)
- Nettkilde: https://docs.altinn.studio/en/api/authorization/ (hentet 2026-03-17)
- Nettkilde: https://docs.altinn.studio/en/authorization/what-do-you-get/systemuser/ (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/altinn/kostnader/2627 (hentet 2026-03-17)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Kapabilitetslisten er redusert til direkte funksjoner i produktet, og autentisering, datadeling og andre indirekte koblinger er tatt ut.
- Produktet beskrives tydeligere som autorisasjonslag i Altinn, ikke som generell tillitsplattform eller full sikkerhetsarkitektur alene.
- Finansiering og plattform er skrevet om slik at porteføljekontekst og usikre forhold skilles tydeligere.

### Tekstlige forbedringer
- Dokumentet starter ikke lenger med målgruppelinje, og `Ressurs ID` er skrevet uten parentesforklaring.
- Hovedfunksjoner og avgrensning gjør det tydeligere når Altinn autorisasjon er riktig produkt for gjenbruk.
- Beskrivelsen bruker mer aktiv og målrettet språk for nasjonal arkitektur, i stedet for teknisk oppramsing.
