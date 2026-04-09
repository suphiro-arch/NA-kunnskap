# Produkt-canvas: Altinn Events

## Navn
Altinn Events

## Ressurs ID
DIGDIR-010

## Status/Livsfase
**Produksjon** - etablert hendelsestjeneste i Altinn for publisering, abonnement og asynkron levering av hendelser.

**Fakta:** Offisiell dokumentasjon beskriver Altinn Events som en publish/subscribe-tjeneste for hendelsesdrevet arkitektur. Hendelser kan publiseres av autoriserte kilder, pushes til autoriserte abonnenter og lagres i 90 dager per 26. mars 2026.

## Modenhet
**Høy funksjonell modenhet** - produktet har tydelig dokumenterte funksjoner og et stabilt grunnmønster:
- Dokumentasjonen dekker både publisering, abonnement, tilgang og tekniske detaljer for hendelseslevering.
- Tjenesten bruker CloudEvents som standard og tilbyr filtrering, webhook-basert levering og retry-logikk.
- Produktet er tydelig avgrenset som hendelsestjeneste, ikke som generell filtransport eller sluttbrukerkommunikasjon.

**Deduksjon:** Altinn Events er modent som felles hendelsesinfrastruktur i Altinn, men må brukes med forståelse for at hendelser er lette notifikasjoner om tilstandsendringer, ikke komplette dokumentleveranser.

## Kort beskrivelse
Altinn Events er Altinns hendelsestjeneste for publisering og abonnement på hendelser på tvers av tjenester og systemer. Produktet gjør det mulig å koble systemer løsere sammen ved at hendelser om tilstandsendringer kan produseres én gang og konsumeres av flere autoriserte mottakere uten polling eller tett synkron kobling.

Produktet har både en utgiverflate og en abonnentflate. Utgivere kan publisere hendelser når noe skjer i en tjeneste eller ressurs. Abonnenter kan registrere webhook-endepunkt og motta hendelser asynkront, med filtrering og retry-mekanisme. Dette gjør løsningen til en felles hendelsesinfrastruktur, ikke bare et enkelt API-kall eller et internt notifikasjonslag.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** gjør det mulig for abonnenter å motta og bruke hendelser fra andre tjenester.
- **Datautveksling og integrasjon: Dele data med andre** gjør det mulig for utgivere å publisere hendelser til autoriserte mottakere.
- **Datautveksling og integrasjon: Hendelsesdrevet** er produktets kjernefunksjon og dekker publish/subscribe-mønsteret.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** støttes gjennom autorisasjon, tilgangspolicyer og kontrollert levering til webhook-endepunkter.
- **Tjenesteutvikling: Integrerbare tjenester** gjør det mulig å bruke standardiserte grensesnitt og hendelsesmønstre i egne løsninger.

## Produktmål
**Primærkilder:** Altinn Events-dokumentasjonen, publiserings- og abonnementsveiledningene.

Dokumenterte mål:
- Gjøre det enklere å ta i bruk hendelsesdrevet arkitektur i Altinn-baserte og tilknyttede løsninger.
- Redusere behovet for polling og databasekopiering mellom systemer.
- Tilby sikker, skalerbar og pålitelig levering av hendelser til autoriserte abonnenter.
- Standardisere hendelser gjennom bruk av CloudEvents.

Operative mål utledet fra de samme kildene:
- Gi både app-hendelser og generiske hendelser et felles distribusjonsmønster.
- Gjøre det mulig å etablere flere abonnenter uten å endre utgivers grunnmodell.
- Gi mottakere mer robust levering gjennom retry-logikk og tilgang til hendelser i en begrenset lagringsperiode.

**Deduksjon:** Produktet har også en viktig rolle som felles mellomlag for asynkron samhandling i Altinn, særlig der flere mottakere trenger å reagere på samme endring.

## Brukerbehov
- Tjenesteeiere trenger en standard måte å publisere hendelser om tilstandsendringer på.
- Abonnenter trenger en sikker og forutsigbar måte å motta hendelser uten polling.
- Integrasjonsteam trenger filtrering, webhook-modell og tydelige autorisasjonsmekanismer.
- Forvaltnings- og sikkerhetsmiljøer trenger kontroll med hvem som kan publisere og abonnere på hvilke hendelser.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Tjenesteeiere og hendelsesutgivere | Publisere hendelser når noe skjer | App-hendelser og generiske hendelser fra egne ressurser | Må registrere og beskytte hendelseskilder |
| Abonnent-systemer | Motta og reagere på hendelser | Automatisering, videre prosessering og oppfølging | Bruker webhook og filtrering for egne behov |
| Utviklings- og integrasjonsteam | Standardisert hendelsesmodell | Oppsett av publisering, abonnement og mottak | Viktig for løs kobling mellom systemer |
| Arkitektur- og produktmiljøer | Vurdere når hendelser er riktig mønster | Samhandling og produktavgrensning | Må skille Events fra Broker og andre produkter |
| Sikkerhets- og forvaltningsmiljøer | Kontroll over tilgang og leveringsflyt | Policyer, scopes og feilhåndtering | Særlig relevant ved hendelser med sensitiv kontekst |

## Hovedfunksjoner
Altinn Events gir utgivere en enkel måte å publisere hendelser når noe skjer i en tjeneste eller ressurs. Dokumentasjonen viser støtte for både app-hendelser og generiske hendelser, og at hendelser publiseres i CloudEvents-format. Dette gjør produktet relevant når behovet er å varsle andre systemer om endringer eller operasjoner, ikke når behovet er å sende komplette filer eller dokumentpayloads.

På abonnentsiden tilbyr produktet et publish/subscribe-mønster der mottakere registrerer egne webhook-endepunkt for å motta hendelser asynkront. Dokumentasjonen beskriver validering av endepunkt, filtrering på kilde og subjekt og en retry-mekanisme med opptil 12 forsøk. Dermed er produktet mer enn en enkel kø eller notifikasjonsfunksjon; det er en hendelsestjeneste med egen leveringslogikk og kontroll over abonnement.

En viktig del av løsningen er at hendelser lagres i 90 dager og kan være tilgjengelige både gjennom aktivt abonnement og API i denne perioden. Dette gir større robusthet enn en ren «fire-and-forget»-modell, men endrer ikke hovedavgrensningen: hendelser er fortsatt lette meldinger om noe som har skjedd, ikke et fullverdig transportlag for store payloads. Når behovet gjelder store filer eller styrt levering av dokumentinnhold, er Altinn Formidling et mer presist produktvalg.

Produktet er også tett koblet til Altinns autorisasjonsmodell. Dokumentasjonen viser at både publisering og abonnement styres gjennom ressurser, policyer og nødvendige scopes. Dette gjør Altinn Events til en sikker og gjenbrukbar byggestein for samhandling, men ikke til en komplett prosessmotor eller en erstatning for domenelogikk i systemene som bruker hendelsene.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Publisering av hendelser om tilstandsendringer og operasjoner | Overføring av store filer eller dokumentpayloads |
| Opprettelse og forvaltning av abonnementer | Full prosessorkestrering i mottakersystemene |
| Webhook-basert levering med retry-logikk | Sluttbrukerkommunikasjon via meldingsboks eller varsling |
| Filtrering, autorisasjon og tilgang til hendelseskilder | Langtidslagring av hendelser utover dokumentert retensjonsperiode |
| Støtte for CloudEvents-basert standardisering | Erstatning for fagspesifikk forretningslogikk |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-26):**
- Dokumentasjonen viser etablert støtte for publisering, abonnement, filtrering, webhook-validering og retry-logikk.
- Produktet beskrives som aktiv del av Altinns videre arbeid med hendelsesdrevet arkitektur.

**Ikke offentlig dokumentert i brukte kilder:** En samlet og tidsfestet roadmap for videreutvikling av Altinn Events.

**Deduksjon:** Videreutviklingen vil sannsynligvis fortsette å dreie seg om mer moden abonnementsforvaltning, bedre integrasjonsstøtte og videre bruk av hendelser i flere Altinn-produkter, men dette er ikke offentlig spesifisert i detalj.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere og abonnenter
- Reduserer behovet for polling og tett koblede integrasjoner.
- Gjør det enklere å etablere flere mottakere for samme hendelse uten å endre utgivers grunnmodell.

### For integrasjonsmiljøer
- Gir et standardisert mønster for hendelsesdrevet samhandling med tydelig sikkerhet og leveringslogikk.
- Støtter mer robust automatisering gjennom retry og kontrollert abonnement.

### For offentlig sektor
- Øker gjenbruk av en felles hendelsestjeneste på tvers av produkter og sektorer.
- Legger til rette for mer sammenhengende og proaktive digitale tjenester.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Hendelser kan inneholde eller avsløre sensitiv kontekst hvis de modelleres for bredt | Stram modellering av hendelsesinnhold og tydelige tilgangspolicyer |
| Teknisk | Abonnenter kan behandle hendelser feil ved duplikater, rekkefølgeutfordringer eller retry | Idempotent mottak, god klientlogikk og tydelig dokumentasjon |
| Sikkerhet | Feil policy eller webhook-oppsett kan gi uautorisert mottak eller sårbar levering | HTTPS, tilgangspolicyer, validering av endepunkt og revisjon |
| Forvaltning | Uklart skille mellom hendelser og andre samhandlingsmønstre kan gi feil produktvalg | Tydelig avgrensning mot Broker, Varsling og Melding |
| Brukeropplevelse | Dårlig kvalitet på hendelser kan gi svake eller misvisende automatiseringer hos mottaker | Standardisering, testing og tydelige kontrakter for hendelsesinnhold |

## Kanaler
- Produktside: https://docs.altinn.studio/en/events/
- Publiser hendelser: https://docs.altinn.studio/en/events/publish-events/
- Abonner på hendelser: https://docs.altinn.studio/en/events/subscribe-to-events/
- Kom i gang som abonnent: https://docs.altinn.studio/en/events/subscribe-to-events/get-started/

## Plattform
Felles hendelsesplattform i Altinn-porteføljen med publish/subscribe-mønster, webhook-levering og autorisasjonsstyrt tilgang.

**Fakta:** Produktet bruker CloudEvents, tilbyr webhook-basert levering, retry-mekanisme og 90 dagers lagring av publiserte hendelser. Publisering og abonnement styres gjennom ressurser, policyer og nødvendige scopes.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsarkitektur og detaljert kostnadsmodell for produktet alene.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme hendelsestjeneste kan brukes av mange ulike produkter og tjenester.
- Produktet gir et felles mønster for løs kobling mellom utgivere og mottakere.
- Gjenbruksverdien er størst når behovet er hendelsesdrevet samhandling, ikke filoverføring eller sluttbrukerdialog.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** støttes ved at hendelser kan deles mellom autoriserte parter.
- **P5: Del og gjenbruk løsninger** realiseres gjennom én felles hendelsestjeneste for flere brukstilfeller.
- **P6: Lag digitale løsninger som støtter samhandling** er direkte relevant fordi produktet legger til rette for asynkron samhandling.
- **P7: Sørg for tillit til oppgaveløsningen** støttes gjennom autorisasjon, kontrollert levering og sporbarhet i hendelsesflyten.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Separat finansieringsmodell eller kostnadsnivå for Altinn Events isolert fra Altinn-porteføljen.
- **Deduksjon:** Produktet må forstås som del av den samlede Altinn-forvaltningen.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir / Altinn-forvaltningen | Offisiell Altinn-dokumentasjon |
| Driftsansvar | Altinns forvaltnings- og driftsmiljø | Produktet beskrives som del av Altinn-plattformen |
| Budsjettansvar | Del av Altinn-porteføljen | Ingen separat offentlig kostnadsmodell verifisert |
| Styringsmodell | Produktforvaltning i Altinn | Fremgår av dokumentasjon og produktstruktur |

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
- Uverifiserte påstander om volum, intern teknologistack, dead-letter-løsninger og kostnader er fjernet eller tonet ned.
- Produktet er tydeligere avgrenset mot Formidling/Broker og andre Altinn-produkter.

### Tekstlige forbedringer
- Hovedfunksjoner forklarer nå både utgiverflate og abonnentflate i stedet for bare korte punkt.
- Språket er gjort mer presist og mindre spekulativt.
- Produktets operative rolle som hendelsestjeneste er tydeligere for målgruppen.



