# Produkt-canvas: Altinn autorisasjon

## Navn
Altinn autorisasjon

## Ressurs ID
DIGDIR-004

## Status/Livsfase
**Produksjon** - etablert autorisasjonsprodukt i Altinn for tilgangsstyring, representasjon og tilgangsbeslutninger, med pÃ¥gÃ¥ende modernisering fra eldre Altinn-mekanismer til Altinn 3-plattformen.

**Fakta:** Offisiell dokumentasjon beskriver Altinn Authorization som komponenter og tjenester for tilgangsadministrasjon og tilgangskontroll for bÃ¥de digitale og analoge tjenester pÃ¥ og utenfor Altinn-plattformen. Dokumentasjonen viser ogsÃ¥ pÃ¥gÃ¥ende modernisering av autorisasjonsomrÃ¥det per 26. mars 2026.

## Modenhet
**HÃ¸y funksjonell modenhet** - produktet er en sentral og dokumentert kjernekomponent i Altinn:
- Dokumentasjonen dekker bÃ¥de brukerflate, API-er og arkitekturkomponenter som ressursregister, tilgangspakker og Policy Decision Point.
- Produktet brukes bÃ¥de av offentlige tjenesteeiere, systemleverandÃ¸rer, virksomheter og privatpersoner.
- LÃ¸sningen dekker bÃ¥de administrasjon av tilganger og maskinell evaluering av tilgangsbeslutninger.

**Deduksjon:** Produktet er modent som felles autorisasjonslag, men er fortsatt i endring fordi flere eldre Altinn-mekanismer moderniseres og flyttes inn i nyere plattformmÃ¸nstre.

## Kort beskrivelse
Altinn autorisasjon er Altinns felles produkt for Ã¥ definere, forvalte og evaluere hvem som kan gjÃ¸re hva, pÃ¥ vegne av hvem og under hvilke vilkÃ¥r. Produktet omfatter bÃ¥de brukerrettet tilgangsforvaltning, representasjon og delegering, og en integrasjonsflate for systemer og tjenester som trenger autorisasjonsbeslutninger.

Produktet er derfor bredere enn en ren tilgangskontrollmotor. Dokumentasjonen viser at Altinn autorisasjon bestÃ¥r av flere komponenter og arbeidsmÃ¥ter: ressursregister for Ã¥ beskrive ressurser og policyer, tilgangspakker og administrasjon av rettigheter, systembruker for finmasket maskinell tilgang og Policy Decision Point for evaluering av konkrete tilgangsforespÃ¸rsler. Dette gjÃ¸r produktet relevant bÃ¥de for menneskelige brukere og maskin-til-maskin-scenarier.

## Kapabiliteter
- **Tillit: Representasjon** gjÃ¸r det mulig Ã¥ opptre pÃ¥ vegne av virksomhet eller annen part gjennom delegering og valg av hvem man handler for.
- **Tillit: Tilgangskontroll** er produktets kjernefunksjon og avgjÃ¸r om brukere og systemer kan utfÃ¸re en operasjon pÃ¥ en ressurs.
- **Tillit: Tilgangsstyring** gir mekanismer for Ã¥ registrere ressurser, definere policyer, administrere rettigheter og forvalte tilganger over tid.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Altinn Authorization-dokumentasjonen, Â«AboutÂ», Â«What do you get?Â» og referansearkitektur.

Dokumenterte mÃ¥l:
- Gi offentlige virksomheter og systemleverandÃ¸rer et felles grunnlag for tilgangsadministrasjon og tilgangskontroll.
- StÃ¸tte tjenester bÃ¥de pÃ¥ Altinn-plattformen og utenfor Altinn-plattformen.
- Gi brukere og virksomheter mulighet til Ã¥ delegere, se og trekke tilbake rettigheter.
- GjÃ¸re det mulig for systemer Ã¥ bruke API-er for autorisasjon og representasjon i egne lÃ¸sninger.

Operative mÃ¥l utledet fra de samme kildene:
- Samle ressursbeskrivelse, policyforvaltning og tilgangsevaluering i et mer standardisert autorisasjonsmÃ¸nster.
- GjÃ¸re maskinell bruk mer presis gjennom systembruker og finmasket tilgangsstyring via Maskinporten.
- Erstatte eller modernisere eldre rolle- og delegeringsmÃ¸nstre med nyere tilgangspakker og mer eksplisitte policyer.

**Deduksjon:** Produktet har ogsÃ¥ en viktig rolle i Ã¥ gjÃ¸re autorisasjon til en gjenbrukbar nasjonal byggestein, slik at flere tjenester kan bruke samme grunnmodell for tilgang.

## Brukerbehov
- Tjenesteeiere trenger en felles modell for Ã¥ beskrive ressurser, policyer og tilgangsregler.
- Virksomheter og personer trenger en lÃ¸sning for Ã¥ se, delegere og trekke tilbake rettigheter.
- SystemleverandÃ¸rer trenger API-er for Ã¥ bruke autorisasjon og representasjon i egne lÃ¸sninger.
- Arkitektur- og sikkerhetsmiljÃ¸er trenger et tydelig skille mellom autentisering, tilgangsstyring og tilgangsbeslutning.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige tjenesteeiere | Definere ressurser og tilgangspolicyer | Tjenester pÃ¥ eller utenfor Altinn | Bruker ressursregister og policygrunnlag for egne tjenester |
| Virksomheter og privatpersoner | Delegere og forstÃ¥ rettigheter | Handle pÃ¥ vegne av seg selv eller andre | MÃ¸ter produktet gjennom brukerflate for representasjon og tilgang |
| SystemleverandÃ¸rer og sluttbrukersystemer | Integrere autorisasjon i egne lÃ¸sninger | Regnskapssystemer, fagsystemer og andre eksterne lÃ¸sninger | Bruker API-er og systembrukerfunksjonalitet |
| Utviklings- og integrasjonsteam | Programmatisk tilgangskontroll | Autorisasjonskall, policybruk og representasjon | Trenger tydelig samspill med ID-porten, Maskinporten og ressurser |
| Sikkerhets- og forvaltningsmiljÃ¸er | Kontroll og etterprÃ¸vbarhet | Styring av tilgangsmodell, policyer og delegasjoner | Viktig fordi feil oppsett kan gi brede konsekvenser |

## Hovedfunksjoner
Altinn autorisasjon gir fÃ¸rst en brukerflate og et forvaltningsmÃ¸nster for representasjon og delegering. Virksomheter og personer kan se hvem som har rettigheter pÃ¥ deres vegne, delegere rettigheter videre og trekke dem tilbake. Dette gjÃ¸r produktet relevant nÃ¥r en tjeneste mÃ¥ hÃ¥ndtere at noen opptrer pÃ¥ vegne av andre, ikke bare nÃ¥r en innlogget bruker skal sjekkes isolert.

Produktet gir ogsÃ¥ tjenesteeiere et ressurs- og policygrunnlag gjennom ressursregisteret. Der kan en tjeneste beskrives, og det kan opprettes regler for hvem som kan bruke tjenesten, til hvilket formÃ¥l og under hvilke vilkÃ¥r. Dette utvider produktet langt utover en enkel beslutningsmotor, fordi det ogsÃ¥ omfatter administrasjon av hva som faktisk skal beskyttes og hvordan tilgangsreglene uttrykkes.

En tredje sentral funksjon er selve tilgangsevalueringen gjennom Policy Decision Point. Dokumentasjonen beskriver PDP som komponenten som avgjÃ¸r om brukere og systemer er autorisert til Ã¥ utfÃ¸re en operasjon pÃ¥ en ressurs, basert pÃ¥ policyer og kontekst. Samtidig viser dokumentasjonen at Altinn autorisasjon stÃ¸tter maskinelle scenarier gjennom systembruker og Maskinporten, noe som gjÃ¸r produktet relevant for bÃ¥de sluttbrukersystemer og rene system-til-system-integrasjoner.

Produktet er likevel ikke en komplett tillitsplattform alene. Autentisering skjer fortsatt i samspill med ID-porten og Maskinporten, og faglig regelverk mÃ¥ fortsatt forstÃ¥s og modelleres riktig av tjenesteeier. Altinn autorisasjon er derfor riktig produkt nÃ¥r behovet gjelder tilgangsstyring, representasjon og tilgangsbeslutning, men ikke nÃ¥r behovet primÃ¦rt er identifisering, meldingsformidling eller datadeling som sÃ¥dan.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Representasjon, delegering og visning av rettigheter | Sluttbrukerinnlogging og identitetsbekreftelse som egen funksjon |
| Ressursregister og policygrunnlag for tjenester | Faglig sakslogikk i tjenestene som bruker autorisasjon |
| Tilgangspakker, tilgangsstyring og administrasjon | Meldingsutveksling, varsling eller datadeling som egne produktomrÃ¥der |
| Policy Decision Point for tilgangsevaluering | Full brukerportal utover det som trengs for tilgangsforvaltning |
| Systembruker og API-er for maskinell bruk | Erstatning for tjenesteeiers ansvar for Ã¥ modellere riktige regler |

### Typiske brukssituasjoner (generisk)
- NÃ¥r en tjeneste mÃ¥ hÃ¥ndtere representasjon, for eksempel at en person handler pÃ¥ vegne av virksomhet eller annen part.
- NÃ¥r en tjenesteeier trenger policybasert tilgangsstyring med tydelig ressursmodell i stedet for hardkodede roller.
- NÃ¥r flere tjenester trenger samme autorisasjonsmodell pÃ¥ tvers av plattformer.
- NÃ¥r maskin-til-maskin-scenarier krever finmasket tilgangsbeslutning i tillegg til autentisering.

### NÃ¥r Altinn autorisasjon normalt ikke er fÃ¸rstevalg
- NÃ¥r behovet kun er innlogging eller identitetsbekreftelse uten representasjon eller policybasert tilgangsstyring.
- NÃ¥r behovet primÃ¦rt er meldingsformidling, hendelser eller datadeling som produktomrÃ¥de.
- NÃ¥r lÃ¸sningen ikke har behov for sentral policyforvaltning eller gjenbruk av autorisasjonsmodell.

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-26):**
- Dokumentasjonen viser moderniseringslÃ¸p for Altinn autorisasjon fra Altinn 2 til Altinn 3-plattformen.
- Tilgangspakker er dokumentert som erstatning for roller, og deler av omrÃ¥det er markert som arbeid under utvikling.

**Deduksjon:** Veikartet er tydelig knyttet til modernisering av roller, tilgangspakker, API-er og flytting av funksjonalitet til nyere plattformmÃ¸nstre.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere
- Reduserer behovet for Ã¥ bygge egen autorisasjonsmodell i hver tjeneste.
- GjÃ¸r det mulig Ã¥ bruke et mer standardisert grunnlag for ressursbeskrivelse og tilgangspolitikk.

### For virksomheter og brukere
- Gir mer forutsigbar hÃ¥ndtering av rettigheter og representasjon pÃ¥ tvers av tjenester.
- GjÃ¸r det enklere Ã¥ handle i egne systemer pÃ¥ vegne av virksomhet eller annen part.

### For offentlig sektor
- Ã˜ker gjenbruk av Ã©n felles modell for tilgangsstyring og tilgangsbeslutninger.
- Styrker samhandling mellom tjenester pÃ¥ og utenfor Altinn gjennom et felles autorisasjonsgrunnlag.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk og regelverk | Feil oversettelse av hjemler og rettigheter til policyer kan gi feil tilgangsbeslutninger | Tett samspill mellom juss, fag og teknisk modellering |
| Teknisk | Komplekst samspill mellom ressurser, policyer, representasjon og systembruker kan gi feilimplementering | Referansearkitektur, tydelige API-er og gode utviklerguider |
| Sikkerhet | For brede delegasjoner eller feil policyer kan gi uÃ¸nsket tilgang | Minste privilegium, revisjon og tydelig ansvar hos tjenesteeier |
| Forvaltning | Overgang fra eldre roller til nyere tilgangspakker kan skape uklarhet i overgangsperioden | Tydelig moderniseringslÃ¸p og bedre begrepsavklaring |
| Brukeropplevelse | Rettighetsbildet kan bli vanskelig Ã¥ forstÃ¥ for brukere og virksomheter | Klare brukerflater, bedre forklaringer og enklere forvaltningsmÃ¸nstre |

## Kanaler
- Produktside: https://docs.altinn.studio/en/authorization/
- Om autorisasjon: https://docs.altinn.studio/en/authorization/about/
- Hva fÃ¥r du?: https://docs.altinn.studio/en/authorization/what-do-you-get/
- Ressursregister: https://docs.altinn.studio/en/authorization/what-do-you-get/resourceregistry/
- Tilgangspakker: https://docs.altinn.studio/en/authorization/what-do-you-get/accessgroups/
- Systembruker: https://docs.altinn.studio/en/authorization/what-do-you-get/systemuser/
- Referansearkitektur: https://docs.altinn.studio/en/authorization/reference/architecture/

## Plattform
Felles autorisasjonsprodukt i Altinn-portefÃ¸ljen med brukerflate, API-er og arkitekturkomponenter for tilgangsstyring og tilgangsbeslutninger.

**Fakta:** Dokumentasjonen viser at produktet omfatter ressursregister, policyadministrasjon, tilgangspakker, systembruker og Policy Decision Point, og at lÃ¸sningene kan brukes bÃ¥de pÃ¥ og utenfor Altinn-plattformen.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsmodell og separat kostnadsfordeling for produktet alene.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet gir en felles modell for tilgangsstyring og autorisasjon pÃ¥ tvers av tjenester.
- Det er relevant bÃ¥de for brukerrettede og maskinelle scenarier.
- Gjenbruksverdien er stÃ¸rst nÃ¥r behovet gjelder representasjon, policybasert tilgang og standardisert autorisasjon, ikke nÃ¥r behovet bare er innlogging.

**Vanlige kombinasjoner med andre produkter:**
- Altinn autorisasjon + ID-porten nÃ¥r brukerinnlogging mÃ¥ kobles til representasjon og tilgangsbeslutning.
- Altinn autorisasjon + Maskinporten nÃ¥r systemtilgang og policybasert autorisasjon mÃ¥ fungere sammen.
- Altinn autorisasjon + Dialogporten eller Altinn Melding nÃ¥r dialog- og meldingsflater trenger styrt tilgang pÃ¥ tvers av parter.

## StÃ¸tter arkitekturprinsipper
- **P5: Del og gjenbruk lÃ¸sninger** realiseres ved at flere tjenester kan bruke samme autorisasjonsgrunnlag.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** styrkes fordi tilgang kan forvaltes og evalueres pÃ¥ tvers av tjenester og systemer.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** er direkte relevant fordi produktet styrer hvem som kan gjÃ¸re hva pÃ¥ hvilket grunnlag.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Separat finansieringsmodell for Altinn autorisasjon isolert fra resten av Altinn-portefÃ¸ljen.
- **Deduksjon:** Produktet mÃ¥ forstÃ¥s som del av Altinns samlede portefÃ¸ljeforvaltning og Ã¸konomi.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir / Altinn-forvaltningen | Offisiell Altinn-dokumentasjon |
| Driftsansvar | Altinns forvaltnings- og driftsmiljÃ¸ | Dokumentasjonen beskriver produktet som del av Altinn-plattformen |
| Budsjettansvar | Del av Altinn-portefÃ¸ljen | Ingen separat offentlig kostnadsmodell verifisert |
| Styringsmodell | Produkt- og portefÃ¸ljeforvaltning i Altinn med pÃ¥gÃ¥ende moderniseringslÃ¸p | Dokumentert modernisering og referansearkitektur |

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
- Produktbredden er tydeligere beskrevet som bÃ¥de brukerflate, forvaltningsflate og integrasjonsflate.
- ModerniseringslÃ¸pet i autorisasjonsomrÃ¥det er tydeligere reflektert i status og veikart.

### Tekstlige forbedringer
- Hovedfunksjoner er skrevet om til forklarende avsnitt som viser nÃ¥r produktet faktisk er relevant.
- SprÃ¥ket er strammet inn og avgrensningen mot autentisering og andre Altinn-produkter er gjort tydeligere.
- Dokumentet er harmonisert med nyere canvas-struktur i repoet.

