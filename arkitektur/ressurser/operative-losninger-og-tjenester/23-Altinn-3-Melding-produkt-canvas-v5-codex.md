# Produkt-canvas: Altinn Melding

## Navn
Altinn Melding

## Ressurs ID
DIGDIR-021

## Status/Livsfase
**Produksjon** - etablert meldingstjeneste med aktiv overgang og migrering fra Altinn 2 frem mot avvikling 19. juni 2026.

**Fakta:** Offisiell dokumentasjon beskriver Altinn 3 Melding som tjenesten for sikker utveksling av korrespondanse mellom offentlige virksomheter og mottakere. Meldingene blir automatisk dialoger i Dialogporten og tilgjengelige i Arbeidsflate.

## Modenhet
**Middels til hÃ¸y funksjonell modenhet** - produktet er etablert, men overgangsarbeidet preger fortsatt totalbildet:
- Produktet har dokumentert livssyklus, referansegrensesnitt, overgangslÃ¸p og tekniske begrensninger.
- Meldinger kan hÃ¥ndteres bÃ¥de av tjenesteeiere og sluttbrukersystemer.
- Migrering av tjenester, data og delegeringer fra Altinn 2 er fortsatt en vesentlig del av produktets operative kontekst.

**Deduksjon:** Kjernefunksjonene er modne, men modenheten pÃ¥virkes fortsatt av avhengigheten til overgangs- og migreringsarbeid frem mot avvikling av Altinn 2.

## Kort beskrivelse
Altinn Melding er Altinns meldingstjeneste for sikker digital utveksling av korrespondanse mellom offentlige virksomheter og mottakere i offentlig sektor, nÃ¦ringsliv og befolkning. Produktet stÃ¸tter livssyklus, tilgangsstyring, innhold og vedlegg, varsling og hendelser, og gjÃ¸r meldinger tilgjengelige i Arbeidsflate og Dialogporten som del av en sammenhengende digital kommunikasjon.

Produktet har bÃ¥de en tjenesteflate og en integrasjonsflate. Tjenesteflaten bestÃ¥r av selve meldingskanalen, med publisering, lesing, bekreftelse, vedlegg og oppfÃ¸lging. Integrasjonsflaten bestÃ¥r av API-er for sending, mottak, abonnement pÃ¥ hendelser og automatisert meldingshÃ¥ndtering. Dette gjÃ¸r produktet bredere enn en ren dokumenttransporttjeneste, men smalere enn en full saksbehandlingsplattform.

## Kapabiliteter
- **Datautveksling og integrasjon: Hendelsesdrevet** stÃ¸tter abonnementer og oppfÃ¸lging av hendelser knyttet til sendte meldinger.
- **Datautveksling og integrasjon: Meldingsformidling** hÃ¥ndterer sikker digital utsending og mottak av meldinger med status og livssyklus.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter innhold, vedlegg og overfÃ¸ringer i meldingsflyten.
- **Tillit: Sporbarhet og innsyn** understÃ¸ttes gjennom omfattende logging av hendelser og prosesser.
- **Tillit: Tilgangskontroll** sÃ¸rger for at kun autoriserte brukere og systemer fÃ¥r tilgang til meldinger og vedlegg.
- **Tjenesteutvikling: Integrerbare tjenester** tilbyr API-er for sending, mottak og automatisert meldingshÃ¥ndtering.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Altinn Melding hovedside, Â«Om Altinn MeldingÂ», Â«Hva fÃ¥r du?Â», livssyklus og overgangsdokumentasjon.

Dokumenterte mÃ¥l:
- Tilby sikker og effektiv digital meldingstjeneste for offentlige virksomheter.
- GjÃ¸re det mulig Ã¥ sende meldinger til innbyggere, nÃ¦ringsliv og andre offentlige virksomheter.
- Reetablere meldingstjenester fra Altinn II i Altinn 3 fÃ¸r avvikling av Altinn II.
- GjÃ¸re meldinger tilgjengelige i Arbeidsflate og Dialogporten.

Operative mÃ¥l utledet fra de samme kildene:
- StÃ¸tte API-basert sending, mottak og automatisert meldingshÃ¥ndtering.
- Gi sporbar statusflyt fra initialisering til publisering, lesing, bekreftelse og purging.
- Gi tjenesteeiere og sluttbrukersystemer ett felles mÃ¸nster for sikker korrespondanse.

**Deduksjon:** Produktet er ogsÃ¥ et sentralt virkemiddel for Ã¥ redusere behovet for mange sektorvise meldingslÃ¸sninger med ulik sikkerhets- og statushÃ¥ndtering.

## Brukerbehov
- Offentlige tjenesteeiere trenger en sikker kanal for digital korrespondanse med vedlegg og tydelig livssyklus.
- Mottakere trenger ett sted Ã¥ finne igjen kommunikasjon fra det offentlige.
- SystemleverandÃ¸rer trenger API-er for automatisert sending, statusoppfÃ¸lging og integrasjon.
- Arkiv-, sikkerhets- og juridiske miljÃ¸er trenger sporbarhet, sikkerhetsnivÃ¥ og kontroll med tilgang til meldinger og vedlegg.
- MigreringsmiljÃ¸er trenger et tydelig lÃ¸p for Ã¥ ta med tjenester og historiske data fra Altinn 2.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige tjenesteeiere | Sende sikker korrespondanse digitalt | Brev, dokumenter og meldinger til mottakere | MÃ¥ reetablere Altinn II-lÃ¸sninger i Altinn 3 |
| SystemleverandÃ¸rer | Integrere sending og oppfÃ¸lging | API-basert meldingsflyt og statusoppfÃ¸lging | Viktig for automatiserte prosesser |
| Mottakere i befolkning og nÃ¦ringsliv | Motta og finne igjen meldinger | Arbeidsflate, dialogoppfÃ¸lging og sluttbrukersystemer | Har innboks i Altinn Arbeidsflate |
| Sluttbrukersystemer | Vise meldinger i egne flater | Integrert brukeropplevelse og automatisering | Kan bruke Dialogporten for videre eksponering |
| Arkiv-, sikkerhets- og juridiske miljÃ¸er | EtterprÃ¸vbarhet og sikker hÃ¥ndtering | Logging, bekreftelse, vedlegg og sikkerhetsnivÃ¥er | Viktig for regelverksetterlevelse |

## Hovedfunksjoner
Altinn Melding tilbyr fÃ¸rst en nasjonal kanal for sikker digital korrespondanse. Tjenesteeiere kan opprette og publisere meldinger til innbyggere, virksomheter og offentlige mottakere, med stÃ¸tte for innhold, vedlegg, sikkerhetsnivÃ¥ og planlagt publisering. Dokumentasjonen beskriver en tydelig livssyklus fÃ¸r og etter publisering, med validering, vedleggsbehandling, virusskanning, publisering, lesing, bekreftelse og senere purging. Dette gjÃ¸r produktet relevant nÃ¥r behovet er sporbar og sikker korrespondanse, ikke bare enkel filoverfÃ¸ring.

Produktet gir ogsÃ¥ en bred integrasjonsflate. Tjenesteeiere kan sende meldinger via API, og sluttbrukersystemer kan bruke grensesnittene for Ã¥ vise og fÃ¸lge opp meldinger i egne flater. Hendelser gjÃ¸r det mulig Ã¥ abonnere pÃ¥ statusendringer, slik at avsender kan fÃ¸lge om en melding er publisert, hentet, lest eller bekreftet. Dermed er Altinn Melding ikke bare en digital postboks, men en meldingstjeneste med egen status- og samhandlingslogikk.

En viktig funksjon ved produktet er samspillet med andre Altinn-produkter. Dokumentasjonen viser at en melding automatisk blir en dialog i Dialogporten og gjÃ¸res tilgjengelig i Arbeidsflate. Varslinger brukes i tillegg for Ã¥ gjÃ¸re mottakeren oppmerksom pÃ¥ at noe ligger klart. Dette betyr at Melding mÃ¥ forstÃ¥s som selve korrespondansetjenesten, mens Dialogporten og Varslinger dekker representasjon og oppmerksomgjÃ¸ring rundt meldingen.

Produktet omfatter likevel ikke hele tjenesteforlÃ¸pet hos avsender. Faglig innhold, saksbehandling og eventuelle interne arkivprosesser ligger fortsatt hos virksomheten som sender meldingen eller i tilknyttede systemer. Altinn Melding er riktig produkt nÃ¥r behovet gjelder sikker digital korrespondanse med livssyklus og sporbarhet, ikke nÃ¥r behovet bare er varsel, hendelse eller generell filtransport.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Sikker formidling av korrespondanse | Full saksbehandlingslogikk i avsenders fagsystem |
| Meldingslivssyklus, status og logging | Generisk filutveksling utenfor meldingskontekst |
| Varsling, vedlegg og tilgangsstyring i meldingslÃ¸pet | Selvstendig brukerportal utenfor Altinns Arbeidsflate |
| Integrasjon mot Dialogporten og Arbeidsflate | Komplett autorisasjonsforvaltning utenfor Altinn-mekanismene |
| Overgangs- og migreringsstÃ¸tte fra Altinn 2 | Full harmonisering av alle historiske forskjeller mellom Altinn 2 og 3 i fÃ¸rste steg |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-26):**
- Tjenester fra Altinn II mÃ¥ reetableres i Altinn 3 fÃ¸r 19. juni 2026.
- Produktet har dokumenterte overgangslÃ¸p for tjenestemigrering, datamigrering og delegeringsmigrering.
- Dokumentasjonen viser fortsatt videreutvikling og forenklinger sammenlignet med Altinn 2.

**Deduksjon:** Veikartet er fortsatt i stor grad knyttet til overgang, migrering og videre harmonisering mellom Altinn 2 og Altinn 3.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere
- Reduserer behovet for Ã¥ etablere egne sikre meldingskanaler.
- GjÃ¸r det mulig Ã¥ sende dokumenter og meldinger i en nasjonal lÃ¸sning med etablert livssyklus og sikkerhetsmekanismer.

### For mottakere
- Gir ett sted Ã¥ motta og fÃ¸lge opp meldinger fra det offentlige.
- Gir bedre oversikt nÃ¥r meldinger blir del av dialog og arbeidsflate.

### For offentlig sektor
- Styrker etterprÃ¸vbarhet gjennom logging, status og bekreftelsesmekanismer.
- Standardiserer meldingshÃ¥ndtering pÃ¥ tvers av etater og systemleverandÃ¸rer.
- UnderstÃ¸tter overgang fra Altinn 2 uten Ã¥ miste meldingskapabiliteten som felleslÃ¸sning.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Feil sikkerhetsnivÃ¥ eller tilgangsstyring kan gi ulovlig tilgang til meldinger eller vedlegg | Tydelige regler, minste privilegium og revisjon av rettighetsoppsett |
| Teknisk | Migrering fra Altinn 2 kan gi avvik i datamodell, innhold og rettigheter | Dokumenterte overgangslÃ¸p, migreringsressurser og fasevis overgang |
| Sikkerhet | Meldinger og vedlegg kan inneholde sensitivt innhold | Kryptering, sterk autentisering og kontrollert tilgang |
| Forvaltning | Mange integrasjonspunkter og avhengigheter gjÃ¸r endringsstyring krevende | Klar referansedokumentasjon og koordinert produktforvaltning |
| Brukeropplevelse | Forskjeller mellom Altinn 2 og 3 kan skape usikkerhet hos tjenesteeiere og mottakere | Tydelig migreringsveiledning og sammenhengende eksponering i Arbeidsflate/Dialogporten |

## Kanaler
- Produktside: https://docs.altinn.studio/nb/correspondence/
- Om Altinn Melding: https://docs.altinn.studio/correspondence/about/
- Hva fÃ¥r du?: https://docs.altinn.studio/correspondence/what-do-you-get/
- Livssyklus: https://docs.altinn.studio/correspondence/explanation/status-lifecycle/
- Tjenestemigrering: https://docs.altinn.studio/nb/correspondence/transition/service-migration/
- LÃ¸sningsarkitektur: https://docs.altinn.studio/nb/correspondence/reference/solution-architecture/

## Plattform
Meldingstjeneste i Altinn-portefÃ¸ljen med API-er, vedleggshÃ¥ndtering, statusflyt, varsling og integrasjon mot Dialogporten og Arbeidsflate.

**Fakta:** Autentisering og autorisasjon stÃ¸ttes gjennom Dialogporten for sluttbrukere, Maskinporten for system-til-system og Altinn Autorisasjon. Produktet blir automatisk representert som dialog i Dialogporten.

**Ikke offentlig dokumentert i brukte kilder:** Full runtime-arkitektur, driftsplattform og kostnadsmodell i detalj.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Samme meldingstjeneste kan brukes av mange offentlige virksomheter.
- Felles mÃ¸nster for logging, status og vedlegg reduserer duplisering.
- Integrasjon med Dialogporten og Arbeidsflate gjÃ¸r produktet gjenbrukbart i flere brukerflater.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** gjÃ¸r meldingsstatus og hendelser tilgjengelige for videre bruk i prosesser.
- **P5: Del og gjenbruk lÃ¸sninger** tilbyr en felles meldingstjeneste i stedet for mange lokale varianter.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** kobler sammen tjenesteeiere, mottakere og sluttbrukersystemer gjennom standardiserte grensesnitt.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** bygger pÃ¥ sikkerhetsnivÃ¥er, logging og sterk autentisering/autorisasjon.

## Finansiering
- Altinn Melding fremstÃ¥r som del av Altinn-portefÃ¸ljen under Digdir.
- **Ikke offentlig dokumentert:** Separat finansieringsmodell eller kostnadsallokering for produktet alene.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Altinn-forvaltningen i Digdir | Offisiell produktdokumentasjon pÃ¥ Altinn Docs |
| Driftsansvar | Altinns drifts- og forvaltningsmiljÃ¸ | Dokumentert som del av Altinn-portefÃ¸ljen |
| Budsjettansvar | Ikke offentlig spesifisert i detalj | Ingen offentlig kostnadsmodell i brukte kilder |
| Styringsmodell | Produktforvaltning i Altinn med egen overgangs- og migreringsstyring | Egen overgangsdokumentasjon og referanselÃ¸p |

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
- Livssyklus fÃ¸r og etter publisering er tydeligere innarbeidet i produktforstÃ¥elsen.
- Samspillet mellom Melding, Dialogporten og Arbeidsflate er beskrevet mer eksplisitt.
- Status og overgangsbildet er oppdatert mot kilder kontrollert 26. mars 2026.

### Tekstlige forbedringer
- Dokumentet fÃ¸lger nÃ¥ oppdatert canvas-struktur uten egen mÃ¥lgruppelinje.
- Hovedfunksjoner er skrevet om til forklarende avsnitt i stedet for punktliste.
- Navn og beskrivelse er harmonisert tettere med operativ registerbruk og dagens Altinn-begreper.

