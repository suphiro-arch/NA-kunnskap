# Produkt-canvas: Altinn Events

## Navn
Altinn Events

## Ressurs ID
DIGDIR-010

## Status/Livsfase
**Produksjon** - etablert hendelsestjeneste i Altinn for publisering, abonnement og asynkron levering av hendelser.

**Fakta:** Offisiell dokumentasjon beskriver Altinn Events som en publish/subscribe-tjeneste for hendelsesdrevet arkitektur. Hendelser kan publiseres av autoriserte kilder, pushes til autoriserte abonnenter og lagres i 90 dager per 26. mars 2026.

## Modenhet
**HÃ¸y funksjonell modenhet** - produktet har tydelig dokumenterte funksjoner og et stabilt grunnmÃ¸nster:
- Dokumentasjonen dekker bÃ¥de publisering, abonnement, tilgang og tekniske detaljer for hendelseslevering.
- Tjenesten bruker CloudEvents som standard og tilbyr filtrering, webhook-basert levering og retry-logikk.
- Produktet er tydelig avgrenset som hendelsestjeneste, ikke som generell filtransport eller sluttbrukerkommunikasjon.

**Deduksjon:** Altinn Events er modent som felles hendelsesinfrastruktur i Altinn, men mÃ¥ brukes med forstÃ¥else for at hendelser er lette notifikasjoner om tilstandsendringer, ikke komplette dokumentleveranser.

## Kort beskrivelse
Altinn Events er Altinns hendelsestjeneste for publisering og abonnement pÃ¥ hendelser pÃ¥ tvers av tjenester og systemer. Produktet gjÃ¸r det mulig Ã¥ koble systemer lÃ¸sere sammen ved at hendelser om tilstandsendringer kan produseres Ã©n gang og konsumeres av flere autoriserte mottakere uten polling eller tett synkron kobling.

Produktet har bÃ¥de en utgiverflate og en abonnentflate. Utgivere kan publisere hendelser nÃ¥r noe skjer i en tjeneste eller ressurs. Abonnenter kan registrere webhook-endepunkt og motta hendelser asynkront, med filtrering og retry-mekanisme. Dette gjÃ¸r lÃ¸sningen til en felles hendelsesinfrastruktur, ikke bare et enkelt API-kall eller et internt notifikasjonslag.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** gjÃ¸r det mulig for abonnenter Ã¥ motta og bruke hendelser fra andre tjenester.
- **Datautveksling og integrasjon: Dele data med andre** gjÃ¸r det mulig for utgivere Ã¥ publisere hendelser til autoriserte mottakere.
- **Datautveksling og integrasjon: Hendelsesdrevet** er produktets kjernefunksjon og dekker publish/subscribe-mÃ¸nsteret.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** stÃ¸ttes gjennom autorisasjon, tilgangspolicyer og kontrollert levering til webhook-endepunkter.
- **Tjenesteutvikling: Integrerbare tjenester** gjÃ¸r det mulig Ã¥ bruke standardiserte grensesnitt og hendelsesmÃ¸nstre i egne lÃ¸sninger.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Altinn Events-dokumentasjonen, publiserings- og abonnementsveiledningene.

Dokumenterte mÃ¥l:
- GjÃ¸re det enklere Ã¥ ta i bruk hendelsesdrevet arkitektur i Altinn-baserte og tilknyttede lÃ¸sninger.
- Redusere behovet for polling og databasekopiering mellom systemer.
- Tilby sikker, skalerbar og pÃ¥litelig levering av hendelser til autoriserte abonnenter.
- Standardisere hendelser gjennom bruk av CloudEvents.

Operative mÃ¥l utledet fra de samme kildene:
- Gi bÃ¥de app-hendelser og generiske hendelser et felles distribusjonsmÃ¸nster.
- GjÃ¸re det mulig Ã¥ etablere flere abonnenter uten Ã¥ endre utgivers grunnmodell.
- Gi mottakere mer robust levering gjennom retry-logikk og tilgang til hendelser i en begrenset lagringsperiode.

**Deduksjon:** Produktet har ogsÃ¥ en viktig rolle som felles mellomlag for asynkron samhandling i Altinn, sÃ¦rlig der flere mottakere trenger Ã¥ reagere pÃ¥ samme endring.

## Brukerbehov
- Tjenesteeiere trenger en standard mÃ¥te Ã¥ publisere hendelser om tilstandsendringer pÃ¥.
- Abonnenter trenger en sikker og forutsigbar mÃ¥te Ã¥ motta hendelser uten polling.
- Integrasjonsteam trenger filtrering, webhook-modell og tydelige autorisasjonsmekanismer.
- Forvaltnings- og sikkerhetsmiljÃ¸er trenger kontroll med hvem som kan publisere og abonnere pÃ¥ hvilke hendelser.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Tjenesteeiere og hendelsesutgivere | Publisere hendelser nÃ¥r noe skjer | App-hendelser og generiske hendelser fra egne ressurser | MÃ¥ registrere og beskytte hendelseskilder |
| Abonnent-systemer | Motta og reagere pÃ¥ hendelser | Automatisering, videre prosessering og oppfÃ¸lging | Bruker webhook og filtrering for egne behov |
| Utviklings- og integrasjonsteam | Standardisert hendelsesmodell | Oppsett av publisering, abonnement og mottak | Viktig for lÃ¸s kobling mellom systemer |
| Arkitektur- og produktmiljÃ¸er | Vurdere nÃ¥r hendelser er riktig mÃ¸nster | Samhandling og produktavgrensning | MÃ¥ skille Events fra Broker og andre produkter |
| Sikkerhets- og forvaltningsmiljÃ¸er | Kontroll over tilgang og leveringsflyt | Policyer, scopes og feilhÃ¥ndtering | SÃ¦rlig relevant ved hendelser med sensitiv kontekst |

## Hovedfunksjoner
Altinn Events gir utgivere en enkel mÃ¥te Ã¥ publisere hendelser nÃ¥r noe skjer i en tjeneste eller ressurs. Dokumentasjonen viser stÃ¸tte for bÃ¥de app-hendelser og generiske hendelser, og at hendelser publiseres i CloudEvents-format. Dette gjÃ¸r produktet relevant nÃ¥r behovet er Ã¥ varsle andre systemer om endringer eller operasjoner, ikke nÃ¥r behovet er Ã¥ sende komplette filer eller dokumentpayloads.

PÃ¥ abonnentsiden tilbyr produktet et publish/subscribe-mÃ¸nster der mottakere registrerer egne webhook-endepunkt for Ã¥ motta hendelser asynkront. Dokumentasjonen beskriver validering av endepunkt, filtrering pÃ¥ kilde og subjekt og en retry-mekanisme med opptil 12 forsÃ¸k. Dermed er produktet mer enn en enkel kÃ¸ eller notifikasjonsfunksjon; det er en hendelsestjeneste med egen leveringslogikk og kontroll over abonnement.

En viktig del av lÃ¸sningen er at hendelser lagres i 90 dager og kan vÃ¦re tilgjengelige bÃ¥de gjennom aktivt abonnement og API i denne perioden. Dette gir stÃ¸rre robusthet enn en ren Â«fire-and-forgetÂ»-modell, men endrer ikke hovedavgrensningen: hendelser er fortsatt lette meldinger om noe som har skjedd, ikke et fullverdig transportlag for store payloads. NÃ¥r behovet gjelder store filer eller styrt levering av dokumentinnhold, er Altinn Formidling et mer presist produktvalg.

Produktet er ogsÃ¥ tett koblet til Altinns autorisasjonsmodell. Dokumentasjonen viser at bÃ¥de publisering og abonnement styres gjennom ressurser, policyer og nÃ¸dvendige scopes. Dette gjÃ¸r Altinn Events til en sikker og gjenbrukbar byggestein for samhandling, men ikke til en komplett prosessmotor eller en erstatning for domenelogikk i systemene som bruker hendelsene.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Publisering av hendelser om tilstandsendringer og operasjoner | OverfÃ¸ring av store filer eller dokumentpayloads |
| Opprettelse og forvaltning av abonnementer | Full prosessorkestrering i mottakersystemene |
| Webhook-basert levering med retry-logikk | Sluttbrukerkommunikasjon via meldingsboks eller varsling |
| Filtrering, autorisasjon og tilgang til hendelseskilder | Langtidslagring av hendelser utover dokumentert retensjonsperiode |
| StÃ¸tte for CloudEvents-basert standardisering | Erstatning for fagspesifikk forretningslogikk |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-26):**
- Dokumentasjonen viser etablert stÃ¸tte for publisering, abonnement, filtrering, webhook-validering og retry-logikk.
- Produktet beskrives som aktiv del av Altinns videre arbeid med hendelsesdrevet arkitektur.

**Ikke offentlig dokumentert i brukte kilder:** En samlet og tidsfestet roadmap for videreutvikling av Altinn Events.

**Deduksjon:** Videreutviklingen vil sannsynligvis fortsette Ã¥ dreie seg om mer moden abonnementsforvaltning, bedre integrasjonsstÃ¸tte og videre bruk av hendelser i flere Altinn-produkter, men dette er ikke offentlig spesifisert i detalj.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere og abonnenter
- Reduserer behovet for polling og tett koblede integrasjoner.
- GjÃ¸r det enklere Ã¥ etablere flere mottakere for samme hendelse uten Ã¥ endre utgivers grunnmodell.

### For integrasjonsmiljÃ¸er
- Gir et standardisert mÃ¸nster for hendelsesdrevet samhandling med tydelig sikkerhet og leveringslogikk.
- StÃ¸tter mer robust automatisering gjennom retry og kontrollert abonnement.

### For offentlig sektor
- Ã˜ker gjenbruk av en felles hendelsestjeneste pÃ¥ tvers av produkter og sektorer.
- Legger til rette for mer sammenhengende og proaktive digitale tjenester.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Hendelser kan inneholde eller avslÃ¸re sensitiv kontekst hvis de modelleres for bredt | Stram modellering av hendelsesinnhold og tydelige tilgangspolicyer |
| Teknisk | Abonnenter kan behandle hendelser feil ved duplikater, rekkefÃ¸lgeutfordringer eller retry | Idempotent mottak, god klientlogikk og tydelig dokumentasjon |
| Sikkerhet | Feil policy eller webhook-oppsett kan gi uautorisert mottak eller sÃ¥rbar levering | HTTPS, tilgangspolicyer, validering av endepunkt og revisjon |
| Forvaltning | Uklart skille mellom hendelser og andre samhandlingsmÃ¸nstre kan gi feil produktvalg | Tydelig avgrensning mot Broker, Varsling og Melding |
| Brukeropplevelse | DÃ¥rlig kvalitet pÃ¥ hendelser kan gi svake eller misvisende automatiseringer hos mottaker | Standardisering, testing og tydelige kontrakter for hendelsesinnhold |

## Kanaler
- Produktside: https://docs.altinn.studio/en/events/
- Publiser hendelser: https://docs.altinn.studio/en/events/publish-events/
- Abonner pÃ¥ hendelser: https://docs.altinn.studio/en/events/subscribe-to-events/
- Kom i gang som abonnent: https://docs.altinn.studio/en/events/subscribe-to-events/get-started/

## Plattform
Felles hendelsesplattform i Altinn-portefÃ¸ljen med publish/subscribe-mÃ¸nster, webhook-levering og autorisasjonsstyrt tilgang.

**Fakta:** Produktet bruker CloudEvents, tilbyr webhook-basert levering, retry-mekanisme og 90 dagers lagring av publiserte hendelser. Publisering og abonnement styres gjennom ressurser, policyer og nÃ¸dvendige scopes.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsarkitektur og detaljert kostnadsmodell for produktet alene.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Samme hendelsestjeneste kan brukes av mange ulike produkter og tjenester.
- Produktet gir et felles mÃ¸nster for lÃ¸s kobling mellom utgivere og mottakere.
- Gjenbruksverdien er stÃ¸rst nÃ¥r behovet er hendelsesdrevet samhandling, ikke filoverfÃ¸ring eller sluttbrukerdialog.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** stÃ¸ttes ved at hendelser kan deles mellom autoriserte parter.
- **P5: Del og gjenbruk lÃ¸sninger** realiseres gjennom Ã©n felles hendelsestjeneste for flere brukstilfeller.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** er direkte relevant fordi produktet legger til rette for asynkron samhandling.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** stÃ¸ttes gjennom autorisasjon, kontrollert levering og sporbarhet i hendelsesflyten.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Separat finansieringsmodell eller kostnadsnivÃ¥ for Altinn Events isolert fra Altinn-portefÃ¸ljen.
- **Deduksjon:** Produktet mÃ¥ forstÃ¥s som del av den samlede Altinn-forvaltningen.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir / Altinn-forvaltningen | Offisiell Altinn-dokumentasjon |
| Driftsansvar | Altinns forvaltnings- og driftsmiljÃ¸ | Produktet beskrives som del av Altinn-plattformen |
| Budsjettansvar | Del av Altinn-portefÃ¸ljen | Ingen separat offentlig kostnadsmodell verifisert |
| Styringsmodell | Produktforvaltning i Altinn | FremgÃ¥r av dokumentasjon og produktstruktur |

## Lenke til dokumentasjon
- https://docs.altinn.studio/en/events/
- https://docs.altinn.studio/en/events/publish-events/
- https://docs.altinn.studio/en/events/subscribe-to-events/
- https://docs.altinn.studio/en/events/subscribe-to-events/get-started/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/12-Altinn-events-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.altinn.studio/en/events/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/en/events/publish-events/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/en/events/subscribe-to-events/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/en/events/subscribe-to-events/get-started/ (kontrollert 2026-03-26)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen er oppdatert mot dagens offisielle Events-dokumentasjon, inkludert CloudEvents, 90 dagers lagring og webhook-basert abonnement.
- Uverifiserte pÃ¥stander om volum, intern teknologistack, dead-letter-lÃ¸sninger og kostnader er fjernet eller tonet ned.
- Produktet er tydeligere avgrenset mot Formidling/Broker og andre Altinn-produkter.

### Tekstlige forbedringer
- Hovedfunksjoner forklarer nÃ¥ bÃ¥de utgiverflate og abonnentflate i stedet for bare korte punkt.
- SprÃ¥ket er gjort mer presist og mindre spekulativt.
- Produktets operative rolle som hendelsestjeneste er tydeligere for mÃ¥lgruppen.

