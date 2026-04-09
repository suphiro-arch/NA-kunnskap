# Produkt-canvas: Altinn Varsling

## Navn
Altinn Varsling

## Ressurs ID
DIGDIR-022

## Status/Livsfase
**Produksjon** - etablert varslingsprodukt med aktiv videreutvikling av kanalbruk, oppslag og styring av utsending.

**Fakta:** Offisiell dokumentasjon beskriver Altinn Notifications som en tjeneste for tilpassede varsler til personer og virksomheter via e-post og SMS, med oppslag av navn og kontaktinformasjon fra nasjonale registre og identifikasjon av riktige mottakere i organisasjoner per 26. mars 2026.

## Modenhet
**Middels til hÃ¸y funksjonell modenhet** - kjernefunksjonene er etablerte og dokumenterte, men produktet utvikles videre:
- Produktet har egne sider for funksjoner, forklaringer, feilkoder og statusverdier.
- Tjenesten brukes av tjenesteeiere, Altinn Apps og interne Altinn-tjenester.
- Dokumentasjonen viser stÃ¸tte for kanalpreferanser, fallback, betingede varsler og planlagt utsending, samtidig som flere kanaler er planlagt.

**Deduksjon:** Modenheten er hÃ¸y for dagens kjernefunksjoner rundt e-post, SMS, oppslag og betinget sending, mens bredden i kanalstÃ¸tte fortsatt er under utvikling.

## Kort beskrivelse
Altinn Varsling er Altinns felleslÃ¸sning for enveis digital varsling til innbyggere og virksomheter. Produktet gjÃ¸r det mulig Ã¥ sende varsler via e-post og SMS, slÃ¥ opp mottakerens navn og kontaktinformasjon fra nasjonale registre, bruke autorisasjon for Ã¥ finne riktige mottakere i organisasjoner og styre utsending basert pÃ¥ betingelser og kanalpreferanser.

Produktet har bÃ¥de en tjenesteflate og en integrasjonsflate. Tjenesteflaten bestÃ¥r av selve varslingsmotoren med oppslag, kanalvalg, fallback, planlagt utsending og status. Integrasjonsflaten bestÃ¥r av API-er som kan brukes av Altinn Apps, Altinn-tjenester og tjenesteeiersystemer. Dette gjÃ¸r produktet bredere enn en enkel SMS- eller e-postgateway, men smalere enn en full meldingsboks eller dialogtjeneste.

## Kapabiliteter
- **Datadrevet: Sammenstilling av data** kombinerer kontaktdata, reservasjonsstatus og autorisasjonsinformasjon for Ã¥ velge riktig mottaker og kanal.
- **Datautveksling og integrasjon: Meldingsformidling** brukes til programmatisk utsending og leveringsoppfÃ¸lging av varsler.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** er nÃ¸dvendig fordi kontaktinformasjon og varslingsinnhold behandles gjennom flere kanaler og oppslag.
- **Sluttbrukertjenester: Proaktive tjenester** gjÃ¸r det mulig Ã¥ varsle mottakere nÃ¥r en hendelse eller tilstand krever oppmerksomhet.
- **Tillit: Tilgangskontroll** bruker autorisasjon for Ã¥ finne riktige mottakere i organisasjonskontekst.
- **Tjenesteutvikling: Integrerbare tjenester** tilbyr API-er for integrasjon med Altinn Apps, Altinn-tjenester og tjenesteeiersystemer.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Varslinger hovedside, Â«Om VarslingerÂ», Â«Hva fÃ¥r du?Â» og forklaringssider.

Dokumenterte mÃ¥l:
- Tilby effektiv enveis kommunikasjon med sluttbrukere via flere kanaler.
- GjÃ¸re det mulig Ã¥ sende varsler programmatisk og spore leveringsstatus.
- Hente oppdatert kontaktinformasjon og navn fra nasjonale registre ved hjelp av fÃ¸dselsnummer eller organisasjonsnummer.
- Identifisere autoriserte mottakere i organisasjoner.

Operative mÃ¥l utledet fra de samme kildene:
- Redusere feilutsendelser gjennom oppslag ved bestilling og ved planlagt sendetidspunkt.
- StÃ¸tte kanalpreferanser og fallback mellom e-post og SMS.
- GjÃ¸re det mulig Ã¥ sende varsler bare nÃ¥r bestemte kriterier er oppfylt.

**Deduksjon:** Produktet har ogsÃ¥ en viktig rolle i Ã¥ redusere behovet for separate varslingsmotorer i hver enkelt offentlig tjeneste.

## Brukerbehov
- Tjenesteeiere trenger en felles og robust varslingsmotor som kan integreres i egne tjenester.
- Integrasjonsteam trenger API-er for utsending, status og planlagt eller betinget varsling.
- Sluttbrukere trenger varsler i rett kanal og til oppdatert kontaktpunkt.
- Virksomheter trenger at riktige mottakere identifiseres basert pÃ¥ organisasjonskontekst og autorisasjon.
- Drifts- og sikkerhetsmiljÃ¸er trenger kontroll pÃ¥ oppslag, levering og feiltilstander.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige tjenesteeiere | Sende varsler i stor skala | Tjenester med behov for e-post- og SMS-varsling | Kan bruke Altinn Varsling i stedet for egen motor |
| Altinn Apps og interne Altinn-tjenester | Integrere varsling i arbeidsflyter | HendelsesutlÃ¸st eller planlagt varsling | Dokumentert som berettigede brukere |
| Tjenesteeiersystemer og systemleverandÃ¸rer | Koble egne systemer til utsending og status | API-integrasjon og automatisering | Viktig for robust prosessintegrasjon |
| Innbyggere og virksomheter | Motta tidsriktige varsler | OppfÃ¸lging av hendelser og kommunikasjon | Mottar via e-post eller SMS |
| Drifts-, sikkerhets- og forvaltningsmiljÃ¸er | OvervÃ¥ke levering og feilhÃ¥ndtering | Statuskontroll, oppslag og avvik | Krever kontroll pÃ¥ kanal- og registeravhengigheter |

## Hovedfunksjoner
Altinn Varsling tilbyr fÃ¸rst en felles varslingsmotor for enveis kommunikasjon via e-post og SMS. Dokumentasjonen beskriver stÃ¸tte for tilpasset innhold, kanalpreferanser, fallback og pÃ¥minnelser. Dette gjÃ¸r produktet relevant nÃ¥r behovet er Ã¥ gjÃ¸re mottakere oppmerksomme pÃ¥ noe som krever handling eller oppfÃ¸lging, ikke nÃ¥r behovet er Ã¥ levere hele dokumenter eller tilby full toveis dialog.

Produktet kombinerer utsending med oppslag og beslutningslogikk. Mottakerens navn, kontaktinformasjon og reservasjonsstatus kan hentes fra nasjonale registre, og autorisasjon brukes for Ã¥ identifisere riktige mottakere i organisasjoner. Dette betyr at lÃ¸sningen ikke bare sender til en kjent adresse; den hjelper ogsÃ¥ tjenesteeier med Ã¥ finne riktig mottaker og riktig kanal i det Ã¸yeblikket varselet skal sendes.

En tredje viktig funksjon er styrt utsending gjennom betingelser og planlegging. Dokumentasjonen viser stÃ¸tte for betingede varsler, planlagt sending og sendevinduer for SMS. Dette gjÃ¸r produktet mer avansert enn en enkel kanalproxy, fordi det lar tjenesteeier styre nÃ¥r et varsel faktisk skal gÃ¥ ut og om det fortsatt er relevant nÃ¥r sendetidspunktet kommer.

Produktet er likevel avgrenset til varsling og oppmerksomgjÃ¸ring. Det erstatter ikke Altinn Melding som korrespondansetjeneste eller Dialogporten som representasjonslag for dialoger. Altinn Varsling er riktig produkt nÃ¥r behovet gjelder kanalstyrt varsling og mottakeroppslag, ikke nÃ¥r behovet gjelder sikker meldingsboks, dokumentlagring eller sluttbrukerdialog.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Enveis varsling via e-post og SMS | Full toveis dialog eller meldingsboksfunksjonalitet |
| Oppslag av mottakere, kontaktdata og reservasjonsstatus | Vedlegg i e-postvarsler |
| Kanalstyring, fallback, planlagt og betinget sending | Full saksbehandlingsflyt i avsendersystemet |
| Status, feilkoder og programmatisk oppfÃ¸lging | Selvstendig identitetsforvaltning utenfor Altinn og tilknyttede registre |
| Integrasjon med Altinn Apps, Altinn-tjenester og tjenesteeiersystemer | Alle fremtidige kanaler som ennÃ¥ ikke er lansert |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-26):**
- Produktet beskriver stÃ¸tte for e-post og SMS, inkludert kanalpreferanser og fallback.
- Dokumentasjonen sier at Altinn planlegger Ã¥ utvide varslingskanalene til et bredere spekter av kommunikasjonsplattformer.

**Deduksjon:** Videreutviklingen vil sannsynligvis handle om flere kanaler og mer fleksibel styring av betingelser og utsending, men detaljerte leveranseplaner er ikke offentlig verifisert i brukte kilder.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere
- Reduserer behovet for Ã¥ bygge og drifte egne varslingsmotorer.
- Gir en felles modell for kanalvalg, mottakeroppslag og status.

### For brukere
- Ã˜ker sannsynligheten for at viktige varsler nÃ¥r frem i rett kanal.
- Reduserer feilutsendelser ved at kontaktdata hentes fra oppdaterte kilder.

### For offentlig sektor
- Skaper gjenbruk av Ã©n nasjonal varslingskapabilitet pÃ¥ tvers av mange tjenester.
- Gir bedre kontroll og standardisering av hvordan varsler sendes og fÃ¸lges opp.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Feil bruk av kontaktdata eller reservasjonsstatus kan gi etterlevelsesbrudd | Tydelig rollefordeling, dokumenterte oppslag og kontroll av bruksvilkÃ¥r |
| Teknisk | Eksterne kanal- og registeravhengigheter kan pÃ¥virke levering og svartid | Robust feil- og statushÃ¥ndtering, overvÃ¥king og fallback |
| Sikkerhet | Varslingsinnhold eller mottakeridentitet kan hÃ¥ndteres feil ved svak kontroll | Autorisasjon, minst mulig innhold i kanal og tydelig tilgangsstyring |
| Forvaltning | Mange integrasjonstyper og utsendingsmÃ¸nstre kan gi ulik brukskvalitet | Felles dokumentasjon, standard API og tydelige forklaringssider |
| Brukeropplevelse | Feil kanalvalg eller forsinket oppslag kan gi at varsler ikke oppfattes som relevante | Kanalpreferanser, oppslag ved sendetidspunkt og tydelig sendestatus |

## Kanaler
- Produktside: https://docs.altinn.studio/nb/notifications/
- Om Varslinger: https://docs.altinn.studio/nb/notifications/about/
- Hva fÃ¥r du?: https://docs.altinn.studio/en/notifications/what-do-you-get/
- Mottakeroppslag: https://docs.altinn.studio/nb/notifications/explanation/recipient-lookup/
- Referanse: https://docs.altinn.studio/nb/notifications/reference/

## Plattform
API-basert varslingslÃ¸sning i Altinn-portefÃ¸ljen med oppslag mot nasjonale registre og stÃ¸tte for flere utsendingskanaler.

**Fakta:** Produktet benytter Register, Profil, Ressursregister og Autorisasjon for Ã¥ hente og verifisere mottakerinformasjon. Dokumentasjonen viser ogsÃ¥ stÃ¸tte for betingede varsler, planlagt utsending og fallback mellom kanaler.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur, intern kanalplattform og detaljert kostnadsmodell.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Ã‰n felles varslingsmotor kan brukes av mange tjenester.
- Felles mÃ¸nster for oppslag, kanalvalg og status reduserer dobbeltarbeid.
- Integrasjon via API gjÃ¸r produktet lett Ã¥ gjenbruke bÃ¥de i Altinn Apps og andre tjenesteeiersystemer.

## StÃ¸tter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov** stÃ¸tter rettidig varsling i kanalene brukerne faktisk bruker.
- **P5: Del og gjenbruk lÃ¸sninger** etablerer en felles varslingskapabilitet i stedet for mange lokale lÃ¸sninger.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** kobler sammen tjenester, registre og kanalutsending gjennom standardiserte API-er.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** bygger pÃ¥ autorisasjon, registeroppslag og kontroll av mottakeridentitet.

## Finansiering
- Altinn Varsling fremstÃ¥r som del av Altinn-portefÃ¸ljen under Digdir.
- **Ikke offentlig dokumentert:** Egen finansieringsmodell eller separat kostnadsfordeling for produktet.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Altinn-forvaltningen i Digdir | Offisiell Altinn-dokumentasjon |
| Driftsansvar | Altinns forvaltnings- og driftsmiljÃ¸ | Dokumentert som del av Altinns produktsider |
| Budsjettansvar | Ikke offentlig spesifisert i detalj | Ingen offentlig kostnadsmodell i brukte kilder |
| Styringsmodell | Produktforvaltning i Altinn-portefÃ¸ljen med kobling til flere interne og eksterne integrasjoner | Dokumentert integrasjonsflate og brukerkretser |

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/notifications/
- https://docs.altinn.studio/nb/notifications/about/
- https://docs.altinn.studio/en/notifications/what-do-you-get/
- https://docs.altinn.studio/nb/notifications/explanation/recipient-lookup/
- https://docs.altinn.studio/nb/notifications/reference/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/24-Varslinger-produkt-canvas-v4-codex.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.altinn.studio/nb/notifications/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/notifications/about/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/en/notifications/what-do-you-get/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/notifications/explanation/recipient-lookup/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/notifications/reference/ (kontrollert 2026-03-26)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Produktbredden er tydeligere beskrevet som bÃ¥de varslingsmotor, oppslagslÃ¸sning og integrasjonsflate.
- Dokumenterte funksjoner for planlagt sending, betingede varsler og kanalstyring er tydeligere innarbeidet.
- Kildene er kontrollert pÃ¥ nytt 26. mars 2026.

### Tekstlige forbedringer
- Dokumentet fÃ¸lger nÃ¥ oppdatert canvas-struktur uten egen mÃ¥lgruppelinje.
- Hovedfunksjoner er skrevet om til forklarende avsnitt i stedet for punktliste.
- Avgrensningen mot Altinn Melding og Dialogporten er gjort tydeligere.

