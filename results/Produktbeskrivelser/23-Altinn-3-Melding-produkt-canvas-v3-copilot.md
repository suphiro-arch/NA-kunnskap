# Produkt-canvas: Altinn 3 Melding

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn 3 Melding (Correspondence)

## Ressurs ID
23 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon

## Modenhet
**Middels til høy funksjonell modenhet** - produktet er etablert, men overgangsarbeidet påvirker totalbildet:
- Produktet har dokumentert arkitektur, livssyklus, referansegrensesnitt og migreringsløp.
- Meldinger kan håndteres både av tjenesteeiere og sluttbrukersystemer.
- Migrering av tjenester, data og delegeringer fra Altinn 2 er en vesentlig del av produktets nåværende kontekst.

**Deduksjon:** Kjernefunksjonene er modne, men modenheten påvirkes fortsatt av avhengigheten til overgangs- og migreringsarbeid frem mot avvikling av Altinn 2.

## Kort beskrivelse
Altinn 3 Melding er en nasjonal meldingstjeneste for sikker digital utveksling av korrespondanse mellom offentlige virksomheter og mottakere i offentlig sektor, næringsliv og befolkning. Produktet støtter livssyklus, tilgangsstyring, vedlegg, varsling og hendelser, og gjør meldinger tilgjengelige i arbeidsflate og Dialogporten som del av en mer sammenhengende digital kommunikasjon.

Produktet er i aktiv produksjon og inngår i overgangsløpet fra Altinn 2, der tjenester og data reetableres og migreres til Altinn 3.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** håndterer sikker digital utsending og mottak av meldinger med status og livssyklus.
- **Tillit: Tilgangskontroll** sørger for at kun autoriserte brukere og systemer får tilgang til meldinger og vedlegg.
- **Tillit: Sporbarhet og innsyn** understøttes gjennom omfattende logging av hendelser og prosesser.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter innhold, vedlegg og overføringer i meldingsflyten.
- **Datautveksling og integrasjon: Hendelsesdrevet** støtter abonnementer og oppfølging av hendelser knyttet til sendte meldinger.
- **Sluttbrukertjenester: Sammenhengende tjenester** gjør meldinger tilgjengelige i Altinn Arbeidsflate og som dialoger i Dialogporten.
- **Tjenesteutvikling: Integrerbare tjenester** tilbyr API-er for sending, mottak og automatisert meldingshåndtering.

Grunnlag: Kapabilitetsnavn fra `index/capabilities.yaml`, vurdert mot Altinn Melding-dokumentasjonen.

## Produktmål
**Primærkilder:** Altinn Melding hovedside, `Hva får du?`, livssyklus og overgangsdokumentasjon.

Dokumenterte mål:
- Tilby sikker og effektiv digital meldingstjeneste for offentlige virksomheter.
- Gjøre det mulig å sende meldinger til innbyggere, næringsliv og andre offentlige virksomheter.
- Reetablere meldingstjenester fra Altinn II i Altinn 3 før avvikling av Altinn II.
- Gjøre meldinger tilgjengelige i Altinn Arbeidsflate og Dialogporten.

Operative mål utledet fra de samme kildene:
- Støtte API-basert sending, mottak og automatisert meldingshåndtering.
- Gi sporbar statusflyt fra opprettelse til lesing, bekreftelse og sletting.
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
| Mottakere i befolkning og næringsliv | Motta og finne igjen meldinger | Innboks, arbeidsflate og dialogoppfølging | Har innboks i Altinn Arbeidsflate |
| Sluttbrukersystemer | Vise meldinger i egne flater | Integrert brukeropplevelse og automatisering | Kan bruke meldinger som del av sluttbrukerreise |
| Arkiv-, sikkerhets- og juridiske miljøer | Etterprøvbarhet og sikker håndtering | Logging, bekreftelse, vedlegg og sikkerhetsnivåer | Viktig for regelverksetterlevelse |

## Hovedfunksjoner
### Primære funksjoner
- Sikker meldingsutveksling for brev, varsler og andre dokumenter.
- Logging av alle hendelser og prosesser for etterprøvbarhet.
- Varsling via e-post eller SMS ved nye meldinger, inkludert re-varsling og tilpassede innstillinger.
- Hendelsesabonnementer som gjør det mulig å følge leverings- og åpningsstatus.
- Tilgangsstyring med ulike sikkerhetsnivåer.
- Støtte for meldingsinnhold, vedlegg, lenker og utløpsdato for vedlegg.
- API-er for sending, mottak og automatisert meldingshåndtering.
- Automatisk representasjon av meldinger som dialoger i Dialogporten.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Sikker formidling av korrespondanse | Full saksbehandlingslogikk i avsenders fagsystem |
| Meldingslivssyklus, status og logging | Generisk filutveksling utenfor meldingskontekst |
| Varsling, vedlegg og tilgangsstyring | Selvstendig brukerportal utenfor Altinns arbeidsflate |
| Integrasjon mot Dialogporten og arbeidsflate | Komplett autorisasjonsforvaltning utenfor Altinn-mekanismene |
| Overgangs- og migreringsstøtte fra Altinn 2 | Full harmonisering av alle historiske forskjeller mellom Altinn 2 og 3 i første steg |

## Veikart over kommende funksjonalitet
**Fakta fra kilder (2026-03-10):**
- Tjenester fra Altinn II måtte reetableres i Altinn 3 før 19. juni 2026.
- Produktet har egne dokumenterte overgangsløp for tjenestemigrering, datamigrering og delegeringsmigrering.
- Dokumentasjonen viser at Altinn 3 Melding fortsatt videreutvikles gjennom forenklinger og forbedringer sammenlignet med Altinn 2.

**Deduksjon:** Veikartet er i stor grad knyttet til overgang, migrering og harmonisering av funksjonalitet mellom Altinn 2 og Altinn 3.

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
| Brukeropplevelse | Forskjeller mellom Altinn 2 og 3 kan skape usikkerhet hos tjenesteeiere og mottakere | Tydelig migreringsveiledning og sammenhengende eksponering i arbeidsflate/Dialogporten |

## Kanaler
- Produktside: https://docs.altinn.studio/nb/correspondence/
- Hva får du?: https://docs.altinn.studio/nb/correspondence/what-do-you-get/
- Livssyklus: https://docs.altinn.studio/nb/correspondence/explanation/status-lifecycle/
- Tjenestemigrering: https://docs.altinn.studio/nb/correspondence/transition/service-migration/
- Løsningsarkitektur: https://docs.altinn.studio/nb/correspondence/reference/solution-architecture/

## Plattform
Meldingstjeneste i Altinn-porteføljen med API-er, vedleggshåndtering, statusflyt, varsling og integrasjon mot Dialogporten og arbeidsflate.

**Fakta:** Autentisering og autorisasjon støttes gjennom Dialogporten for sluttbrukere, Maskinporten for system-til-system og Altinn Autorisasjon.

**Ikke offentlig dokumentert i brukte kilder:** Full runtime-arkitektur, driftsplattform og kostnadsmodell i detalj.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme meldingstjeneste kan brukes av mange offentlige virksomheter.
- Felles mønster for logging, status og vedlegg reduserer duplisering.
- Integrasjon med Dialogporten og arbeidsflate gjør produktet gjenbrukbart i flere brukerflater.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** gjør meldingsstatus og hendelser tilgjengelige for videre bruk i prosesser.
- **P5: Del og gjenbruk løsninger** tilbyr en felles meldingstjeneste i stedet for mange lokale varianter.
- **P6: Lag digitale løsninger som støtter samhandling** kobler sammen tjenesteeiere, mottakere og sluttbrukersystemer gjennom standardiserte grensesnitt.
- **P7: Sørg for tillit til oppgaveløsningen** bygger på sikkerhetsnivåer, logging og sterk autentisering/autorisasjon.

## Finansiering
- Altinn 3 Melding fremstår som del av Altinn-porteføljen under Digdir.
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
- https://docs.altinn.studio/nb/correspondence/what-do-you-get/
- https://docs.altinn.studio/nb/correspondence/explanation/status-lifecycle/
- https://docs.altinn.studio/nb/correspondence/transition/service-migration/
- https://docs.altinn.studio/nb/correspondence/reference/solution-architecture/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `results/Produktbeskrivelser/23-Altinn-3-Melding-produkt-canvas-v2-codex.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `index/capabilities.yaml`
- Lokal fil: `index/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.altinn.studio/nb/correspondence/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/correspondence/what-do-you-get/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/correspondence/explanation/status-lifecycle/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/correspondence/transition/service-migration/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/correspondence/reference/solution-architecture/ (hentet 2026-03-10)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Verifisert mål, funksjoner, livssyklus og migreringskontekst mot oppdatert Altinn-dokumentasjon.
- Lagt inn mer presise opplysninger om sikkerhetskontroller, meldingsstatus og overgang fra Altinn 2.
- Fjernet eller tonet ned generelle antakelser til fordel for dokumenterte produktegenskaper.

### Tekstlige forbedringer
- Gjort produktteksten mer selvstendig og målgruppetilpasset.
- Strukturert brukersegmenter, scope og risiko i samme format som nyere canvases.
- Tydeliggjort forholdet mellom Melding, Dialogporten og arbeidsflate.
- Flyttet fakta om overgang og migrering fra `Status/Livsfase` til `Kort beskrivelse` i tråd med oppdatert instruks.