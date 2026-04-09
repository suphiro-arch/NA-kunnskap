# Produkt-canvas: Altinn Melding

## Navn
Altinn Melding

## Ressurs ID
DIGDIR-021

## Status/Livsfase
**Produksjon** - etablert meldingstjeneste med aktiv overgang og migrering fra Altinn 2 frem mot avvikling 19. juni 2026.

**Fakta:** Offisiell dokumentasjon beskriver Altinn 3 Melding som tjenesten for sikker utveksling av korrespondanse mellom offentlige virksomheter og mottakere. Meldingene blir automatisk dialoger i Dialogporten og tilgjengelige i Arbeidsflate.

## Modenhet
**Middels til høy funksjonell modenhet** - produktet er etablert, men overgangsarbeidet preger fortsatt totalbildet:
- Produktet har dokumentert livssyklus, referansegrensesnitt, overgangsløp og tekniske begrensninger.
- Meldinger kan håndteres både av tjenesteeiere og sluttbrukersystemer.
- Migrering av tjenester, data og delegeringer fra Altinn 2 er fortsatt en vesentlig del av produktets operative kontekst.

**Deduksjon:** Kjernefunksjonene er modne, men modenheten påvirkes fortsatt av avhengigheten til overgangs- og migreringsarbeid frem mot avvikling av Altinn 2.

## Kort beskrivelse
Altinn Melding er Altinns meldingstjeneste for sikker digital utveksling av korrespondanse mellom offentlige virksomheter og mottakere i offentlig sektor, næringsliv og befolkning. Produktet støtter livssyklus, tilgangsstyring, innhold og vedlegg, varsling og hendelser, og gjør meldinger tilgjengelige i Arbeidsflate og Dialogporten som del av en sammenhengende digital kommunikasjon.

Produktet har både en tjenesteflate og en integrasjonsflate. Tjenesteflaten består av selve meldingskanalen, med publisering, lesing, bekreftelse, vedlegg og oppfølging. Integrasjonsflaten består av API-er for sending, mottak, abonnement på hendelser og automatisert meldingshåndtering. Dette gjør produktet bredere enn en ren dokumenttransporttjeneste, men smalere enn en full saksbehandlingsplattform.

## Kapabiliteter
- **Datautveksling og integrasjon: Hendelsesdrevet** støtter abonnementer og oppfølging av hendelser knyttet til sendte meldinger.
- **Datautveksling og integrasjon: Meldingsformidling** håndterer sikker digital utsending og mottak av meldinger med status og livssyklus.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter innhold, vedlegg og overføringer i meldingsflyten.
- **Tillit: Sporbarhet og innsyn** understøttes gjennom omfattende logging av hendelser og prosesser.
- **Tillit: Tilgangskontroll** sørger for at kun autoriserte brukere og systemer får tilgang til meldinger og vedlegg.
- **Tjenesteutvikling: Integrerbare tjenester** tilbyr API-er for sending, mottak og automatisert meldingshåndtering.

## Produktmål
**Primærkilder:** Altinn Melding hovedside, «Om Altinn Melding», «Hva får du?», livssyklus og overgangsdokumentasjon.

Dokumenterte mål:
- Tilby sikker og effektiv digital meldingstjeneste for offentlige virksomheter.
- Gjøre det mulig å sende meldinger til innbyggere, næringsliv og andre offentlige virksomheter.
- Reetablere meldingstjenester fra Altinn II i Altinn 3 før avvikling av Altinn II.
- Gjøre meldinger tilgjengelige i Arbeidsflate og Dialogporten.

Operative mål utledet fra de samme kildene:
- Støtte API-basert sending, mottak og automatisert meldingshåndtering.
- Gi sporbar statusflyt fra initialisering til publisering, lesing, bekreftelse og purging.
- Gi tjenesteeiere og sluttbrukersystemer ett felles mønster for sikker korrespondanse.

**Deduksjon:** Produktet er også et sentralt virkemiddel for å redusere behovet for mange sektorvise meldingsløsninger med ulik sikkerhets- og statushåndtering.

## Brukerbehov
- Offentlige tjenesteeiere trenger en sikker kanal for digital korrespondanse med vedlegg og tydelig livssyklus.
- Mottakere trenger ett sted å finne igjen kommunikasjon fra det offentlige.
- Systemleverandører trenger API-er for automatisert sending, statusoppfølging og integrasjon.
- Arkiv-, sikkerhets- og juridiske miljøer trenger sporbarhet, sikkerhetsnivå og kontroll med tilgang til meldinger og vedlegg.
- Migreringsmiljøer trenger et tydelig løp for å ta med tjenester og historiske data fra Altinn 2.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige tjenesteeiere | Sende sikker korrespondanse digitalt | Brev, dokumenter og meldinger til mottakere | Må reetablere Altinn II-løsninger i Altinn 3 |
| Systemleverandører | Integrere sending og oppfølging | API-basert meldingsflyt og statusoppfølging | Viktig for automatiserte prosesser |
| Mottakere i befolkning og næringsliv | Motta og finne igjen meldinger | Arbeidsflate, dialogoppfølging og sluttbrukersystemer | Har innboks i Altinn Arbeidsflate |
| Sluttbrukersystemer | Vise meldinger i egne flater | Integrert brukeropplevelse og automatisering | Kan bruke Dialogporten for videre eksponering |
| Arkiv-, sikkerhets- og juridiske miljøer | Etterprøvbarhet og sikker håndtering | Logging, bekreftelse, vedlegg og sikkerhetsnivåer | Viktig for regelverksetterlevelse |

## Hovedfunksjoner
Altinn Melding tilbyr først en nasjonal kanal for sikker digital korrespondanse. Tjenesteeiere kan opprette og publisere meldinger til innbyggere, virksomheter og offentlige mottakere, med støtte for innhold, vedlegg, sikkerhetsnivå og planlagt publisering. Dokumentasjonen beskriver en tydelig livssyklus før og etter publisering, med validering, vedleggsbehandling, virusskanning, publisering, lesing, bekreftelse og senere purging. Dette gjør produktet relevant når behovet er sporbar og sikker korrespondanse, ikke bare enkel filoverføring.

Produktet gir også en bred integrasjonsflate. Tjenesteeiere kan sende meldinger via API, og sluttbrukersystemer kan bruke grensesnittene for å vise og følge opp meldinger i egne flater. Hendelser gjør det mulig å abonnere på statusendringer, slik at avsender kan følge om en melding er publisert, hentet, lest eller bekreftet. Dermed er Altinn Melding ikke bare en digital postboks, men en meldingstjeneste med egen status- og samhandlingslogikk.

En viktig funksjon ved produktet er samspillet med andre Altinn-produkter. Dokumentasjonen viser at en melding automatisk blir en dialog i Dialogporten og gjøres tilgjengelig i Arbeidsflate. Varslinger brukes i tillegg for å gjøre mottakeren oppmerksom på at noe ligger klart. Dette betyr at Melding må forstås som selve korrespondansetjenesten, mens Dialogporten og Varslinger dekker representasjon og oppmerksomgjøring rundt meldingen.

Produktet omfatter likevel ikke hele tjenesteforløpet hos avsender. Faglig innhold, saksbehandling og eventuelle interne arkivprosesser ligger fortsatt hos virksomheten som sender meldingen eller i tilknyttede systemer. Altinn Melding er riktig produkt når behovet gjelder sikker digital korrespondanse med livssyklus og sporbarhet, ikke når behovet bare er varsel, hendelse eller generell filtransport.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Sikker formidling av korrespondanse | Full saksbehandlingslogikk i avsenders fagsystem |
| Meldingslivssyklus, status og logging | Generisk filutveksling utenfor meldingskontekst |
| Varsling, vedlegg og tilgangsstyring i meldingsløpet | Selvstendig brukerportal utenfor Altinns Arbeidsflate |
| Integrasjon mot Dialogporten og Arbeidsflate | Komplett autorisasjonsforvaltning utenfor Altinn-mekanismene |
| Overgangs- og migreringsstøtte fra Altinn 2 | Full harmonisering av alle historiske forskjeller mellom Altinn 2 og 3 i første steg |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-26):**
- Tjenester fra Altinn II må reetableres i Altinn 3 før 19. juni 2026.
- Produktet har dokumenterte overgangsløp for tjenestemigrering, datamigrering og delegeringsmigrering.
- Dokumentasjonen viser fortsatt videreutvikling og forenklinger sammenlignet med Altinn 2.

**Deduksjon:** Veikartet er fortsatt i stor grad knyttet til overgang, migrering og videre harmonisering mellom Altinn 2 og Altinn 3.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere
- Reduserer behovet for å etablere egne sikre meldingskanaler.
- Gjør det mulig å sende dokumenter og meldinger i en nasjonal løsning med etablert livssyklus og sikkerhetsmekanismer.

### For mottakere
- Gir ett sted å motta og følge opp meldinger fra det offentlige.
- Gir bedre oversikt når meldinger blir del av dialog og arbeidsflate.

### For offentlig sektor
- Styrker etterprøvbarhet gjennom logging, status og bekreftelsesmekanismer.
- Standardiserer meldingshåndtering på tvers av etater og systemleverandører.
- Understøtter overgang fra Altinn 2 uten å miste meldingskapabiliteten som fellesløsning.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil sikkerhetsnivå eller tilgangsstyring kan gi ulovlig tilgang til meldinger eller vedlegg | Tydelige regler, minste privilegium og revisjon av rettighetsoppsett |
| Teknisk | Migrering fra Altinn 2 kan gi avvik i datamodell, innhold og rettigheter | Dokumenterte overgangsløp, migreringsressurser og fasevis overgang |
| Sikkerhet | Meldinger og vedlegg kan inneholde sensitivt innhold | Kryptering, sterk autentisering og kontrollert tilgang |
| Forvaltning | Mange integrasjonspunkter og avhengigheter gjør endringsstyring krevende | Klar referansedokumentasjon og koordinert produktforvaltning |
| Brukeropplevelse | Forskjeller mellom Altinn 2 og 3 kan skape usikkerhet hos tjenesteeiere og mottakere | Tydelig migreringsveiledning og sammenhengende eksponering i Arbeidsflate/Dialogporten |

## Kanaler
- Produktside: https://docs.altinn.studio/nb/correspondence/
- Om Altinn Melding: https://docs.altinn.studio/correspondence/about/
- Hva får du?: https://docs.altinn.studio/correspondence/what-do-you-get/
- Livssyklus: https://docs.altinn.studio/correspondence/explanation/status-lifecycle/
- Tjenestemigrering: https://docs.altinn.studio/nb/correspondence/transition/service-migration/
- Løsningsarkitektur: https://docs.altinn.studio/nb/correspondence/reference/solution-architecture/

## Plattform
Meldingstjeneste i Altinn-porteføljen med API-er, vedleggshåndtering, statusflyt, varsling og integrasjon mot Dialogporten og Arbeidsflate.

**Fakta:** Autentisering og autorisasjon støttes gjennom Dialogporten for sluttbrukere, Maskinporten for system-til-system og Altinn Autorisasjon. Produktet blir automatisk representert som dialog i Dialogporten.

**Ikke offentlig dokumentert i brukte kilder:** Full runtime-arkitektur, driftsplattform og kostnadsmodell i detalj.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme meldingstjeneste kan brukes av mange offentlige virksomheter.
- Felles mønster for logging, status og vedlegg reduserer duplisering.
- Integrasjon med Dialogporten og Arbeidsflate gjør produktet gjenbrukbart i flere brukerflater.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** gjør meldingsstatus og hendelser tilgjengelige for videre bruk i prosesser.
- **P5: Del og gjenbruk løsninger** tilbyr en felles meldingstjeneste i stedet for mange lokale varianter.
- **P6: Lag digitale løsninger som støtter samhandling** kobler sammen tjenesteeiere, mottakere og sluttbrukersystemer gjennom standardiserte grensesnitt.
- **P7: Sørg for tillit til oppgaveløsningen** bygger på sikkerhetsnivåer, logging og sterk autentisering/autorisasjon.

## Finansiering
- Altinn Melding fremstår som del av Altinn-porteføljen under Digdir.
- **Ikke offentlig dokumentert:** Separat finansieringsmodell eller kostnadsallokering for produktet alene.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Altinn-forvaltningen i Digdir | Offisiell produktdokumentasjon på Altinn Docs |
| Driftsansvar | Altinns drifts- og forvaltningsmiljø | Dokumentert som del av Altinn-porteføljen |
| Budsjettansvar | Ikke offentlig spesifisert i detalj | Ingen offentlig kostnadsmodell i brukte kilder |
| Styringsmodell | Produktforvaltning i Altinn med egen overgangs- og migreringsstyring | Egen overgangsdokumentasjon og referanseløp |

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/correspondence/
- https://docs.altinn.studio/correspondence/about/
- https://docs.altinn.studio/correspondence/what-do-you-get/
- https://docs.altinn.studio/correspondence/explanation/status-lifecycle/
- https://docs.altinn.studio/nb/correspondence/transition/service-migration/
- https://docs.altinn.studio/nb/correspondence/reference/solution-architecture/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/23-Altinn-3-Melding-produkt-canvas-v4-codex.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.altinn.studio/nb/correspondence/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/correspondence/about/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/correspondence/what-do-you-get/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/correspondence/explanation/status-lifecycle/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/correspondence/transition/service-migration/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/correspondence/reference/solution-architecture/ (kontrollert 2026-03-26)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Livssyklus før og etter publisering er tydeligere innarbeidet i produktforståelsen.
- Samspillet mellom Melding, Dialogporten og Arbeidsflate er beskrevet mer eksplisitt.
- Status og overgangsbildet er oppdatert mot kilder kontrollert 26. mars 2026.

### Tekstlige forbedringer
- Dokumentet følger nå oppdatert canvas-struktur uten egen målgruppelinje.
- Hovedfunksjoner er skrevet om til forklarende avsnitt i stedet for punktliste.
- Navn og beskrivelse er harmonisert tettere med operativ registerbruk og dagens Altinn-begreper.


