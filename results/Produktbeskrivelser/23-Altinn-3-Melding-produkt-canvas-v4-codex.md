# Produkt-canvas: Altinn 3 Melding

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn 3 Melding (Correspondence)

## Ressurs ID
DIGDIR-021

## Status/Livsfase
**Produksjon** - etablert meldingstjeneste med aktiv overgang og migrering fra Altinn 2.

**Fakta:** Altinn 3 Melding brukes for sikker utveksling av korrespondanse mellom offentlige etater og enkeltpersoner eller bedrifter, og Altinn II mÃ¥tte reetableres i Altinn 3 fÃ¸r 19. juni 2026.

## Modenhet
**Middels til hÃ¸y funksjonell modenhet** - produktet er etablert, men overgangsarbeidet pÃ¥virker totalbildet:
- Produktet har dokumentert arkitektur, livssyklus, referansegrensesnitt og migreringslÃ¸p.
- Meldinger kan hÃ¥ndteres bÃ¥de av tjenesteeiere og sluttbrukersystemer.
- Migrering av tjenester, data og delegeringer fra Altinn 2 er en vesentlig del av produktets nÃ¥vÃ¦rende kontekst.

**Deduksjon:** Kjernefunksjonene er modne, men modenheten pÃ¥virkes fortsatt av avhengigheten til overgangs- og migreringsarbeid frem mot avvikling av Altinn 2.

## Kort beskrivelse
Altinn 3 Melding er en nasjonal meldingstjeneste for sikker digital utveksling av korrespondanse mellom offentlige virksomheter og mottakere i offentlig sektor, nÃ¦ringsliv og befolkning. Produktet stÃ¸tter livssyklus, tilgangsstyring, vedlegg, varsling og hendelser, og gjÃ¸r meldinger tilgjengelige i arbeidsflate og Dialogporten som del av en mer sammenhengende digital kommunikasjon.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** hÃ¥ndterer sikker digital utsending og mottak av meldinger med status og livssyklus.
- **Tillit: Tilgangskontroll** sÃ¸rger for at kun autoriserte brukere og systemer fÃ¥r tilgang til meldinger og vedlegg.
- **Tillit: Sporbarhet og innsyn** understÃ¸ttes gjennom omfattende logging av hendelser og prosesser.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter innhold, vedlegg og overfÃ¸ringer i meldingsflyten.
- **Datautveksling og integrasjon: Hendelsesdrevet** stÃ¸tter abonnementer og oppfÃ¸lging av hendelser knyttet til sendte meldinger.
- **Sluttbrukertjenester: Sammenhengende tjenester** gjÃ¸r meldinger tilgjengelige i Altinn Arbeidsflate og som dialoger i Dialogporten.
- **Tjenesteutvikling: Integrerbare tjenester** tilbyr API-er for sending, mottak og automatisert meldingshÃ¥ndtering.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Altinn Melding-dokumentasjonen.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Altinn Melding hovedside, `Hva fÃ¥r du?`, livssyklus og overgangsdokumentasjon.

Dokumenterte mÃ¥l:
- Tilby sikker og effektiv digital meldingstjeneste for offentlige virksomheter.
- GjÃ¸re det mulig Ã¥ sende meldinger til innbyggere, nÃ¦ringsliv og andre offentlige virksomheter.
- Reetablere meldingstjenester fra Altinn II i Altinn 3 fÃ¸r avvikling av Altinn II.
- GjÃ¸re meldinger tilgjengelige i Altinn Arbeidsflate og Dialogporten.

Operative mÃ¥l utledet fra de samme kildene:
- StÃ¸tte API-basert sending, mottak og automatisert meldingshÃ¥ndtering.
- Gi sporbar statusflyt fra opprettelse til lesing, bekreftelse og sletting.
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
| Mottakere i befolkning og nÃ¦ringsliv | Motta og finne igjen meldinger | Innboks, arbeidsflate og dialogoppfÃ¸lging | Har innboks i Altinn Arbeidsflate |
| Sluttbrukersystemer | Vise meldinger i egne flater | Integrert brukeropplevelse og automatisering | Kan bruke meldinger som del av sluttbrukerreise |
| Arkiv-, sikkerhets- og juridiske miljÃ¸er | EtterprÃ¸vbarhet og sikker hÃ¥ndtering | Logging, bekreftelse, vedlegg og sikkerhetsnivÃ¥er | Viktig for regelverksetterlevelse |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- Sikker meldingsutveksling for brev, varsler og andre dokumenter.
- Logging av alle hendelser og prosesser for etterprÃ¸vbarhet.
- Varsling via e-post eller SMS ved nye meldinger, inkludert re-varsling og tilpassede innstillinger.
- Hendelsesabonnementer som gjÃ¸r det mulig Ã¥ fÃ¸lge leverings- og Ã¥pningsstatus.
- Tilgangsstyring med ulike sikkerhetsnivÃ¥er.
- StÃ¸tte for meldingsinnhold, vedlegg, lenker og utlÃ¸psdato for vedlegg.
- API-er for sending, mottak og automatisert meldingshÃ¥ndtering.
- Automatisk representasjon av meldinger som dialoger i Dialogporten.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Sikker formidling av korrespondanse | Full saksbehandlingslogikk i avsenders fagsystem |
| Meldingslivssyklus, status og logging | Generisk filutveksling utenfor meldingskontekst |
| Varsling, vedlegg og tilgangsstyring | Selvstendig brukerportal utenfor Altinns arbeidsflate |
| Integrasjon mot Dialogporten og arbeidsflate | Komplett autorisasjonsforvaltning utenfor Altinn-mekanismene |
| Overgangs- og migreringsstÃ¸tte fra Altinn 2 | Full harmonisering av alle historiske forskjeller mellom Altinn 2 og 3 i fÃ¸rste steg |

## Veikart over kommende funksjonalitet
**Fakta fra kilder (2026-03-10):**
- Tjenester fra Altinn II mÃ¥tte reetableres i Altinn 3 fÃ¸r 19. juni 2026.
- Produktet har egne dokumenterte overgangslÃ¸p for tjenestemigrering, datamigrering og delegeringsmigrering.
- Dokumentasjonen viser at Altinn 3 Melding fortsatt videreutvikles gjennom forenklinger og forbedringer sammenlignet med Altinn 2.

**Deduksjon:** Veikartet er i stor grad knyttet til overgang, migrering og harmonisering av funksjonalitet mellom Altinn 2 og Altinn 3.

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
| Brukeropplevelse | Forskjeller mellom Altinn 2 og 3 kan skape usikkerhet hos tjenesteeiere og mottakere | Tydelig migreringsveiledning og sammenhengende eksponering i arbeidsflate/Dialogporten |

## Kanaler
- Produktside: https://docs.altinn.studio/nb/correspondence/
- Hva fÃ¥r du?: https://docs.altinn.studio/nb/correspondence/what-do-you-get/
- Livssyklus: https://docs.altinn.studio/nb/correspondence/explanation/status-lifecycle/
- Tjenestemigrering: https://docs.altinn.studio/nb/correspondence/transition/service-migration/
- LÃ¸sningsarkitektur: https://docs.altinn.studio/nb/correspondence/reference/solution-architecture/

## Plattform
Meldingstjeneste i Altinn-portefÃ¸ljen med API-er, vedleggshÃ¥ndtering, statusflyt, varsling og integrasjon mot Dialogporten og arbeidsflate.

**Fakta:** Autentisering og autorisasjon stÃ¸ttes gjennom Dialogporten for sluttbrukere, Maskinporten for system-til-system og Altinn Autorisasjon.

**Ikke offentlig dokumentert i brukte kilder:** Full runtime-arkitektur, driftsplattform og kostnadsmodell i detalj.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Samme meldingstjeneste kan brukes av mange offentlige virksomheter.
- Felles mÃ¸nster for logging, status og vedlegg reduserer duplisering.
- Integrasjon med Dialogporten og arbeidsflate gjÃ¸r produktet gjenbrukbart i flere brukerflater.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** gjÃ¸r meldingsstatus og hendelser tilgjengelige for videre bruk i prosesser.
- **P5: Del og gjenbruk lÃ¸sninger** tilbyr en felles meldingstjeneste i stedet for mange lokale varianter.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** kobler sammen tjenesteeiere, mottakere og sluttbrukersystemer gjennom standardiserte grensesnitt.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** bygger pÃ¥ sikkerhetsnivÃ¥er, logging og sterk autentisering/autorisasjon.

## Finansiering
- Altinn 3 Melding fremstÃ¥r som del av Altinn-portefÃ¸ljen under Digdir.
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
- https://docs.altinn.studio/nb/correspondence/what-do-you-get/
- https://docs.altinn.studio/nb/correspondence/explanation/status-lifecycle/
- https://docs.altinn.studio/nb/correspondence/transition/service-migration/
- https://docs.altinn.studio/nb/correspondence/reference/solution-architecture/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `results/Produktbeskrivelser/23-Altinn-3-Melding-produkt-canvas-v1-codex.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.altinn.studio/nb/correspondence/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/correspondence/what-do-you-get/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/correspondence/explanation/status-lifecycle/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/correspondence/transition/service-migration/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/correspondence/reference/solution-architecture/ (hentet 2026-03-10)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Verifisert mÃ¥l, funksjoner, livssyklus og migreringskontekst mot oppdatert Altinn-dokumentasjon.
- Lagt inn mer presise opplysninger om sikkerhetskontroller, meldingsstatus og overgang fra Altinn 2.
- Fjernet eller tonet ned generelle antakelser til fordel for dokumenterte produktegenskaper.

### Tekstlige forbedringer
- Gjort produktteksten mer selvstendig og mÃ¥lgruppetilpasset.
- Strukturert brukersegmenter, scope og risiko i samme format som nyere canvases.
- Tydeliggjort forholdet mellom Melding, Dialogporten og arbeidsflate.