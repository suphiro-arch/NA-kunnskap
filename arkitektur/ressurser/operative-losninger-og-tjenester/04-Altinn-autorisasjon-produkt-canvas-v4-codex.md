# Produkt-canvas: Altinn autorisasjon

## Navn
Altinn autorisasjon

## Ressurs ID
DIGDIR-004

## Status/Livsfase
**Produksjon** - etablert autorisasjonsprodukt i Altinn for tilgangsstyring, representasjon og tilgangsbeslutninger, med pågående modernisering fra eldre Altinn-mekanismer til Altinn 3-plattformen.

**Fakta:** Offisiell dokumentasjon beskriver Altinn Authorization som komponenter og tjenester for tilgangsadministrasjon og tilgangskontroll for både digitale og analoge tjenester på og utenfor Altinn-plattformen. Dokumentasjonen viser også pågående modernisering av autorisasjonsområdet per 26. mars 2026.

## Modenhet
**Høy funksjonell modenhet** - produktet er en sentral og dokumentert kjernekomponent i Altinn:
- Dokumentasjonen dekker både brukerflate, API-er og arkitekturkomponenter som ressursregister, tilgangspakker og Policy Decision Point.
- Produktet brukes både av offentlige tjenesteeiere, systemleverandører, virksomheter og privatpersoner.
- Løsningen dekker både administrasjon av tilganger og maskinell evaluering av tilgangsbeslutninger.

**Deduksjon:** Produktet er modent som felles autorisasjonslag, men er fortsatt i endring fordi flere eldre Altinn-mekanismer moderniseres og flyttes inn i nyere plattformmønstre.

## Kort beskrivelse
Altinn autorisasjon er Altinns felles produkt for å definere, forvalte og evaluere hvem som kan gjøre hva, på vegne av hvem og under hvilke vilkår. Produktet omfatter både brukerrettet tilgangsforvaltning, representasjon og delegering, og en integrasjonsflate for systemer og tjenester som trenger autorisasjonsbeslutninger.

Produktet er derfor bredere enn en ren tilgangskontrollmotor. Dokumentasjonen viser at Altinn autorisasjon består av flere komponenter og arbeidsmåter: ressursregister for å beskrive ressurser og policyer, tilgangspakker og administrasjon av rettigheter, systembruker for finmasket maskinell tilgang og Policy Decision Point for evaluering av konkrete tilgangsforespørsler. Dette gjør produktet relevant både for menneskelige brukere og maskin-til-maskin-scenarier.

## Kapabiliteter
- **Tillit: Representasjon** gjør det mulig å opptre på vegne av virksomhet eller annen part gjennom delegering og valg av hvem man handler for.
- **Tillit: Tilgangskontroll** er produktets kjernefunksjon og avgjør om brukere og systemer kan utføre en operasjon på en ressurs.
- **Tillit: Tilgangsstyring** gir mekanismer for å registrere ressurser, definere policyer, administrere rettigheter og forvalte tilganger over tid.

## Produktmål
**Primærkilder:** Altinn Authorization-dokumentasjonen, «About», «What do you get?» og referansearkitektur.

Dokumenterte mål:
- Gi offentlige virksomheter og systemleverandører et felles grunnlag for tilgangsadministrasjon og tilgangskontroll.
- Støtte tjenester både på Altinn-plattformen og utenfor Altinn-plattformen.
- Gi brukere og virksomheter mulighet til å delegere, se og trekke tilbake rettigheter.
- Gjøre det mulig for systemer å bruke API-er for autorisasjon og representasjon i egne løsninger.

Operative mål utledet fra de samme kildene:
- Samle ressursbeskrivelse, policyforvaltning og tilgangsevaluering i et mer standardisert autorisasjonsmønster.
- Gjøre maskinell bruk mer presis gjennom systembruker og finmasket tilgangsstyring via Maskinporten.
- Erstatte eller modernisere eldre rolle- og delegeringsmønstre med nyere tilgangspakker og mer eksplisitte policyer.

**Deduksjon:** Produktet har også en viktig rolle i å gjøre autorisasjon til en gjenbrukbar nasjonal byggestein, slik at flere tjenester kan bruke samme grunnmodell for tilgang.

## Brukerbehov
- Tjenesteeiere trenger en felles modell for å beskrive ressurser, policyer og tilgangsregler.
- Virksomheter og personer trenger en løsning for å se, delegere og trekke tilbake rettigheter.
- Systemleverandører trenger API-er for å bruke autorisasjon og representasjon i egne løsninger.
- Arkitektur- og sikkerhetsmiljøer trenger et tydelig skille mellom autentisering, tilgangsstyring og tilgangsbeslutning.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige tjenesteeiere | Definere ressurser og tilgangspolicyer | Tjenester på eller utenfor Altinn | Bruker ressursregister og policygrunnlag for egne tjenester |
| Virksomheter og privatpersoner | Delegere og forstå rettigheter | Handle på vegne av seg selv eller andre | Møter produktet gjennom brukerflate for representasjon og tilgang |
| Systemleverandører og sluttbrukersystemer | Integrere autorisasjon i egne løsninger | Regnskapssystemer, fagsystemer og andre eksterne løsninger | Bruker API-er og systembrukerfunksjonalitet |
| Utviklings- og integrasjonsteam | Programmatisk tilgangskontroll | Autorisasjonskall, policybruk og representasjon | Trenger tydelig samspill med ID-porten, Maskinporten og ressurser |
| Sikkerhets- og forvaltningsmiljøer | Kontroll og etterprøvbarhet | Styring av tilgangsmodell, policyer og delegasjoner | Viktig fordi feil oppsett kan gi brede konsekvenser |

## Hovedfunksjoner
Altinn autorisasjon gir først en brukerflate og et forvaltningsmønster for representasjon og delegering. Virksomheter og personer kan se hvem som har rettigheter på deres vegne, delegere rettigheter videre og trekke dem tilbake. Dette gjør produktet relevant når en tjeneste må håndtere at noen opptrer på vegne av andre, ikke bare når en innlogget bruker skal sjekkes isolert.

Produktet gir også tjenesteeiere et ressurs- og policygrunnlag gjennom ressursregisteret. Der kan en tjeneste beskrives, og det kan opprettes regler for hvem som kan bruke tjenesten, til hvilket formål og under hvilke vilkår. Dette utvider produktet langt utover en enkel beslutningsmotor, fordi det også omfatter administrasjon av hva som faktisk skal beskyttes og hvordan tilgangsreglene uttrykkes.

En tredje sentral funksjon er selve tilgangsevalueringen gjennom Policy Decision Point. Dokumentasjonen beskriver PDP som komponenten som avgjør om brukere og systemer er autorisert til å utføre en operasjon på en ressurs, basert på policyer og kontekst. Samtidig viser dokumentasjonen at Altinn autorisasjon støtter maskinelle scenarier gjennom systembruker og Maskinporten, noe som gjør produktet relevant for både sluttbrukersystemer og rene system-til-system-integrasjoner.

Produktet er likevel ikke en komplett tillitsplattform alene. Autentisering skjer fortsatt i samspill med ID-porten og Maskinporten, og faglig regelverk må fortsatt forstås og modelleres riktig av tjenesteeier. Altinn autorisasjon er derfor riktig produkt når behovet gjelder tilgangsstyring, representasjon og tilgangsbeslutning, men ikke når behovet primært er identifisering, meldingsformidling eller datadeling som sådan.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Representasjon, delegering og visning av rettigheter | Sluttbrukerinnlogging og identitetsbekreftelse som egen funksjon |
| Ressursregister og policygrunnlag for tjenester | Faglig sakslogikk i tjenestene som bruker autorisasjon |
| Tilgangspakker, tilgangsstyring og administrasjon | Meldingsutveksling, varsling eller datadeling som egne produktområder |
| Policy Decision Point for tilgangsevaluering | Full brukerportal utover det som trengs for tilgangsforvaltning |
| Systembruker og API-er for maskinell bruk | Erstatning for tjenesteeiers ansvar for å modellere riktige regler |

### Typiske brukssituasjoner (generisk)
- Når en tjeneste må håndtere representasjon, for eksempel at en person handler på vegne av virksomhet eller annen part.
- Når en tjenesteeier trenger policybasert tilgangsstyring med tydelig ressursmodell i stedet for hardkodede roller.
- Når flere tjenester trenger samme autorisasjonsmodell på tvers av plattformer.
- Når maskin-til-maskin-scenarier krever finmasket tilgangsbeslutning i tillegg til autentisering.

### Når Altinn autorisasjon normalt ikke er førstevalg
- Når behovet kun er innlogging eller identitetsbekreftelse uten representasjon eller policybasert tilgangsstyring.
- Når behovet primært er meldingsformidling, hendelser eller datadeling som produktområde.
- Når løsningen ikke har behov for sentral policyforvaltning eller gjenbruk av autorisasjonsmodell.

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-26):**
- Dokumentasjonen viser moderniseringsløp for Altinn autorisasjon fra Altinn 2 til Altinn 3-plattformen.
- Tilgangspakker er dokumentert som erstatning for roller, og deler av området er markert som arbeid under utvikling.

**Deduksjon:** Veikartet er tydelig knyttet til modernisering av roller, tilgangspakker, API-er og flytting av funksjonalitet til nyere plattformmønstre.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere
- Reduserer behovet for å bygge egen autorisasjonsmodell i hver tjeneste.
- Gjør det mulig å bruke et mer standardisert grunnlag for ressursbeskrivelse og tilgangspolitikk.

### For virksomheter og brukere
- Gir mer forutsigbar håndtering av rettigheter og representasjon på tvers av tjenester.
- Gjør det enklere å handle i egne systemer på vegne av virksomhet eller annen part.

### For offentlig sektor
- Øker gjenbruk av én felles modell for tilgangsstyring og tilgangsbeslutninger.
- Styrker samhandling mellom tjenester på og utenfor Altinn gjennom et felles autorisasjonsgrunnlag.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk og regelverk | Feil oversettelse av hjemler og rettigheter til policyer kan gi feil tilgangsbeslutninger | Tett samspill mellom juss, fag og teknisk modellering |
| Teknisk | Komplekst samspill mellom ressurser, policyer, representasjon og systembruker kan gi feilimplementering | Referansearkitektur, tydelige API-er og gode utviklerguider |
| Sikkerhet | For brede delegasjoner eller feil policyer kan gi uønsket tilgang | Minste privilegium, revisjon og tydelig ansvar hos tjenesteeier |
| Forvaltning | Overgang fra eldre roller til nyere tilgangspakker kan skape uklarhet i overgangsperioden | Tydelig moderniseringsløp og bedre begrepsavklaring |
| Brukeropplevelse | Rettighetsbildet kan bli vanskelig å forstå for brukere og virksomheter | Klare brukerflater, bedre forklaringer og enklere forvaltningsmønstre |

## Kanaler
- Produktside: https://docs.altinn.studio/en/authorization/
- Om autorisasjon: https://docs.altinn.studio/en/authorization/about/
- Hva får du?: https://docs.altinn.studio/en/authorization/what-do-you-get/
- Ressursregister: https://docs.altinn.studio/en/authorization/what-do-you-get/resourceregistry/
- Tilgangspakker: https://docs.altinn.studio/en/authorization/what-do-you-get/accessgroups/
- Systembruker: https://docs.altinn.studio/en/authorization/what-do-you-get/systemuser/
- Referansearkitektur: https://docs.altinn.studio/en/authorization/reference/architecture/

## Plattform
Felles autorisasjonsprodukt i Altinn-porteføljen med brukerflate, API-er og arkitekturkomponenter for tilgangsstyring og tilgangsbeslutninger.

**Fakta:** Dokumentasjonen viser at produktet omfatter ressursregister, policyadministrasjon, tilgangspakker, systembruker og Policy Decision Point, og at løsningene kan brukes både på og utenfor Altinn-plattformen.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsmodell og separat kostnadsfordeling for produktet alene.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet gir en felles modell for tilgangsstyring og autorisasjon på tvers av tjenester.
- Det er relevant både for brukerrettede og maskinelle scenarier.
- Gjenbruksverdien er størst når behovet gjelder representasjon, policybasert tilgang og standardisert autorisasjon, ikke når behovet bare er innlogging.

**Vanlige kombinasjoner med andre produkter:**
- Altinn autorisasjon + ID-porten når brukerinnlogging må kobles til representasjon og tilgangsbeslutning.
- Altinn autorisasjon + Maskinporten når systemtilgang og policybasert autorisasjon må fungere sammen.
- Altinn autorisasjon + Dialogporten eller Altinn Melding når dialog- og meldingsflater trenger styrt tilgang på tvers av parter.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger** realiseres ved at flere tjenester kan bruke samme autorisasjonsgrunnlag.
- **P6: Lag digitale løsninger som støtter samhandling** styrkes fordi tilgang kan forvaltes og evalueres på tvers av tjenester og systemer.
- **P7: Sørg for tillit til oppgaveløsningen** er direkte relevant fordi produktet styrer hvem som kan gjøre hva på hvilket grunnlag.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Separat finansieringsmodell for Altinn autorisasjon isolert fra resten av Altinn-porteføljen.
- **Deduksjon:** Produktet må forstås som del av Altinns samlede porteføljeforvaltning og økonomi.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir / Altinn-forvaltningen | Offisiell Altinn-dokumentasjon |
| Driftsansvar | Altinns forvaltnings- og driftsmiljø | Dokumentasjonen beskriver produktet som del av Altinn-plattformen |
| Budsjettansvar | Del av Altinn-porteføljen | Ingen separat offentlig kostnadsmodell verifisert |
| Styringsmodell | Produkt- og porteføljeforvaltning i Altinn med pågående moderniseringsløp | Dokumentert modernisering og referansearkitektur |

## Lenke til dokumentasjon
- https://docs.altinn.studio/en/authorization/
- https://docs.altinn.studio/en/authorization/about/
- https://docs.altinn.studio/en/authorization/what-do-you-get/
- https://docs.altinn.studio/en/authorization/what-do-you-get/resourceregistry/
- https://docs.altinn.studio/en/authorization/what-do-you-get/accessgroups/
- https://docs.altinn.studio/en/authorization/what-do-you-get/systemuser/
- https://docs.altinn.studio/en/authorization/reference/architecture/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/04-Altinn-autorisasjon-produkt-canvas-v3-codex.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.altinn.studio/en/authorization/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/en/authorization/about/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/en/authorization/what-do-you-get/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/en/authorization/what-do-you-get/resourceregistry/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/en/authorization/what-do-you-get/accessgroups/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/en/authorization/what-do-you-get/systemuser/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/en/authorization/reference/architecture/ (kontrollert 2026-03-26)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen er utvidet med oppdatert dokumentasjon om ressursregister, tilgangspakker, systembruker og PDP.
- Produktbredden er tydeligere beskrevet som både brukerflate, forvaltningsflate og integrasjonsflate.
- Moderniseringsløpet i autorisasjonsområdet er tydeligere reflektert i status og veikart.

### Tekstlige forbedringer
- Hovedfunksjoner er skrevet om til forklarende avsnitt som viser når produktet faktisk er relevant.
- Språket er strammet inn og avgrensningen mot autentisering og andre Altinn-produkter er gjort tydeligere.
- Dokumentet er harmonisert med nyere canvas-struktur i repoet.



