# Produkt-canvas: Altinn Varsling

## Navn
Altinn Varsling

## Ressurs ID
DIGDIR-022

## Status/Livsfase
**Produksjon** - etablert varslingsprodukt med aktiv videreutvikling av kanalbruk, oppslag og styring av utsending.

**Fakta:** Offisiell dokumentasjon beskriver Altinn Notifications som en tjeneste for tilpassede varsler til personer og virksomheter via e-post og SMS, med oppslag av navn og kontaktinformasjon fra nasjonale registre og identifikasjon av riktige mottakere i organisasjoner per 26. mars 2026.

## Modenhet
**Middels til høy funksjonell modenhet** - kjernefunksjonene er etablerte og dokumenterte, men produktet utvikles videre:
- Produktet har egne sider for funksjoner, forklaringer, feilkoder og statusverdier.
- Tjenesten brukes av tjenesteeiere, Altinn Apps og interne Altinn-tjenester.
- Dokumentasjonen viser støtte for kanalpreferanser, fallback, betingede varsler og planlagt utsending, samtidig som flere kanaler er planlagt.

**Deduksjon:** Modenheten er høy for dagens kjernefunksjoner rundt e-post, SMS, oppslag og betinget sending, mens bredden i kanalstøtte fortsatt er under utvikling.

## Kort beskrivelse
Altinn Varsling er Altinns fellesløsning for enveis digital varsling til innbyggere og virksomheter. Produktet gjør det mulig å sende varsler via e-post og SMS, slå opp mottakerens navn og kontaktinformasjon fra nasjonale registre, bruke autorisasjon for å finne riktige mottakere i organisasjoner og styre utsending basert på betingelser og kanalpreferanser.

Produktet har både en tjenesteflate og en integrasjonsflate. Tjenesteflaten består av selve varslingsmotoren med oppslag, kanalvalg, fallback, planlagt utsending og status. Integrasjonsflaten består av API-er som kan brukes av Altinn Apps, Altinn-tjenester og tjenesteeiersystemer. Dette gjør produktet bredere enn en enkel SMS- eller e-postgateway, men smalere enn en full meldingsboks eller dialogtjeneste.

## Kapabiliteter
- **Datadrevet: Sammenstilling av data** kombinerer kontaktdata, reservasjonsstatus og autorisasjonsinformasjon for å velge riktig mottaker og kanal.
- **Datautveksling og integrasjon: Meldingsformidling** brukes til programmatisk utsending og leveringsoppfølging av varsler.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** er nødvendig fordi kontaktinformasjon og varslingsinnhold behandles gjennom flere kanaler og oppslag.
- **Sluttbrukertjenester: Proaktive tjenester** gjør det mulig å varsle mottakere når en hendelse eller tilstand krever oppmerksomhet.
- **Tillit: Tilgangskontroll** bruker autorisasjon for å finne riktige mottakere i organisasjonskontekst.
- **Tjenesteutvikling: Integrerbare tjenester** tilbyr API-er for integrasjon med Altinn Apps, Altinn-tjenester og tjenesteeiersystemer.

## Produktmål
**Primærkilder:** Varslinger hovedside, «Om Varslinger», «Hva får du?» og forklaringssider.

Dokumenterte mål:
- Tilby effektiv enveis kommunikasjon med sluttbrukere via flere kanaler.
- Gjøre det mulig å sende varsler programmatisk og spore leveringsstatus.
- Hente oppdatert kontaktinformasjon og navn fra nasjonale registre ved hjelp av fødselsnummer eller organisasjonsnummer.
- Identifisere autoriserte mottakere i organisasjoner.

Operative mål utledet fra de samme kildene:
- Redusere feilutsendelser gjennom oppslag ved bestilling og ved planlagt sendetidspunkt.
- Støtte kanalpreferanser og fallback mellom e-post og SMS.
- Gjøre det mulig å sende varsler bare når bestemte kriterier er oppfylt.

**Deduksjon:** Produktet har også en viktig rolle i å redusere behovet for separate varslingsmotorer i hver enkelt offentlig tjeneste.

## Brukerbehov
- Tjenesteeiere trenger en felles og robust varslingsmotor som kan integreres i egne tjenester.
- Integrasjonsteam trenger API-er for utsending, status og planlagt eller betinget varsling.
- Sluttbrukere trenger varsler i rett kanal og til oppdatert kontaktpunkt.
- Virksomheter trenger at riktige mottakere identifiseres basert på organisasjonskontekst og autorisasjon.
- Drifts- og sikkerhetsmiljøer trenger kontroll på oppslag, levering og feiltilstander.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige tjenesteeiere | Sende varsler i stor skala | Tjenester med behov for e-post- og SMS-varsling | Kan bruke Altinn Varsling i stedet for egen motor |
| Altinn Apps og interne Altinn-tjenester | Integrere varsling i arbeidsflyter | Hendelsesutløst eller planlagt varsling | Dokumentert som berettigede brukere |
| Tjenesteeiersystemer og systemleverandører | Koble egne systemer til utsending og status | API-integrasjon og automatisering | Viktig for robust prosessintegrasjon |
| Innbyggere og virksomheter | Motta tidsriktige varsler | Oppfølging av hendelser og kommunikasjon | Mottar via e-post eller SMS |
| Drifts-, sikkerhets- og forvaltningsmiljøer | Overvåke levering og feilhåndtering | Statuskontroll, oppslag og avvik | Krever kontroll på kanal- og registeravhengigheter |

## Hovedfunksjoner
Altinn Varsling tilbyr først en felles varslingsmotor for enveis kommunikasjon via e-post og SMS. Dokumentasjonen beskriver støtte for tilpasset innhold, kanalpreferanser, fallback og påminnelser. Dette gjør produktet relevant når behovet er å gjøre mottakere oppmerksomme på noe som krever handling eller oppfølging, ikke når behovet er å levere hele dokumenter eller tilby full toveis dialog.

Produktet kombinerer utsending med oppslag og beslutningslogikk. Mottakerens navn, kontaktinformasjon og reservasjonsstatus kan hentes fra nasjonale registre, og autorisasjon brukes for å identifisere riktige mottakere i organisasjoner. Dette betyr at løsningen ikke bare sender til en kjent adresse; den hjelper også tjenesteeier med å finne riktig mottaker og riktig kanal i det øyeblikket varselet skal sendes.

En tredje viktig funksjon er styrt utsending gjennom betingelser og planlegging. Dokumentasjonen viser støtte for betingede varsler, planlagt sending og sendevinduer for SMS. Dette gjør produktet mer avansert enn en enkel kanalproxy, fordi det lar tjenesteeier styre når et varsel faktisk skal gå ut og om det fortsatt er relevant når sendetidspunktet kommer.

Produktet er likevel avgrenset til varsling og oppmerksomgjøring. Det erstatter ikke Altinn Melding som korrespondansetjeneste eller Dialogporten som representasjonslag for dialoger. Altinn Varsling er riktig produkt når behovet gjelder kanalstyrt varsling og mottakeroppslag, ikke når behovet gjelder sikker meldingsboks, dokumentlagring eller sluttbrukerdialog.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Enveis varsling via e-post og SMS | Full toveis dialog eller meldingsboksfunksjonalitet |
| Oppslag av mottakere, kontaktdata og reservasjonsstatus | Vedlegg i e-postvarsler |
| Kanalstyring, fallback, planlagt og betinget sending | Full saksbehandlingsflyt i avsendersystemet |
| Status, feilkoder og programmatisk oppfølging | Selvstendig identitetsforvaltning utenfor Altinn og tilknyttede registre |
| Integrasjon med Altinn Apps, Altinn-tjenester og tjenesteeiersystemer | Alle fremtidige kanaler som ennå ikke er lansert |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-26):**
- Produktet beskriver støtte for e-post og SMS, inkludert kanalpreferanser og fallback.
- Dokumentasjonen sier at Altinn planlegger å utvide varslingskanalene til et bredere spekter av kommunikasjonsplattformer.

**Deduksjon:** Videreutviklingen vil sannsynligvis handle om flere kanaler og mer fleksibel styring av betingelser og utsending, men detaljerte leveranseplaner er ikke offentlig verifisert i brukte kilder.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere
- Reduserer behovet for å bygge og drifte egne varslingsmotorer.
- Gir en felles modell for kanalvalg, mottakeroppslag og status.

### For brukere
- Øker sannsynligheten for at viktige varsler når frem i rett kanal.
- Reduserer feilutsendelser ved at kontaktdata hentes fra oppdaterte kilder.

### For offentlig sektor
- Skaper gjenbruk av én nasjonal varslingskapabilitet på tvers av mange tjenester.
- Gir bedre kontroll og standardisering av hvordan varsler sendes og følges opp.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil bruk av kontaktdata eller reservasjonsstatus kan gi etterlevelsesbrudd | Tydelig rollefordeling, dokumenterte oppslag og kontroll av bruksvilkår |
| Teknisk | Eksterne kanal- og registeravhengigheter kan påvirke levering og svartid | Robust feil- og statushåndtering, overvåking og fallback |
| Sikkerhet | Varslingsinnhold eller mottakeridentitet kan håndteres feil ved svak kontroll | Autorisasjon, minst mulig innhold i kanal og tydelig tilgangsstyring |
| Forvaltning | Mange integrasjonstyper og utsendingsmønstre kan gi ulik brukskvalitet | Felles dokumentasjon, standard API og tydelige forklaringssider |
| Brukeropplevelse | Feil kanalvalg eller forsinket oppslag kan gi at varsler ikke oppfattes som relevante | Kanalpreferanser, oppslag ved sendetidspunkt og tydelig sendestatus |

## Kanaler
- Produktside: https://docs.altinn.studio/nb/notifications/
- Om Varslinger: https://docs.altinn.studio/nb/notifications/about/
- Hva får du?: https://docs.altinn.studio/en/notifications/what-do-you-get/
- Mottakeroppslag: https://docs.altinn.studio/nb/notifications/explanation/recipient-lookup/
- Referanse: https://docs.altinn.studio/nb/notifications/reference/

## Plattform
API-basert varslingsløsning i Altinn-porteføljen med oppslag mot nasjonale registre og støtte for flere utsendingskanaler.

**Fakta:** Produktet benytter Register, Profil, Ressursregister og Autorisasjon for å hente og verifisere mottakerinformasjon. Dokumentasjonen viser også støtte for betingede varsler, planlagt utsending og fallback mellom kanaler.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur, intern kanalplattform og detaljert kostnadsmodell.

## Gjenbruk
**Høy gjenbruksverdi:**
- ån felles varslingsmotor kan brukes av mange tjenester.
- Felles mønster for oppslag, kanalvalg og status reduserer dobbeltarbeid.
- Integrasjon via API gjør produktet lett å gjenbruke både i Altinn Apps og andre tjenesteeiersystemer.

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov** støtter rettidig varsling i kanalene brukerne faktisk bruker.
- **P5: Del og gjenbruk løsninger** etablerer en felles varslingskapabilitet i stedet for mange lokale løsninger.
- **P6: Lag digitale løsninger som støtter samhandling** kobler sammen tjenester, registre og kanalutsending gjennom standardiserte API-er.
- **P7: Sørg for tillit til oppgaveløsningen** bygger på autorisasjon, registeroppslag og kontroll av mottakeridentitet.

## Finansiering
- Altinn Varsling fremstår som del av Altinn-porteføljen under Digdir.
- **Ikke offentlig dokumentert:** Egen finansieringsmodell eller separat kostnadsfordeling for produktet.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Altinn-forvaltningen i Digdir | Offisiell Altinn-dokumentasjon |
| Driftsansvar | Altinns forvaltnings- og driftsmiljø | Dokumentert som del av Altinns produktsider |
| Budsjettansvar | Ikke offentlig spesifisert i detalj | Ingen offentlig kostnadsmodell i brukte kilder |
| Styringsmodell | Produktforvaltning i Altinn-porteføljen med kobling til flere interne og eksterne integrasjoner | Dokumentert integrasjonsflate og brukerkretser |

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
- Produktbredden er tydeligere beskrevet som både varslingsmotor, oppslagsløsning og integrasjonsflate.
- Dokumenterte funksjoner for planlagt sending, betingede varsler og kanalstyring er tydeligere innarbeidet.
- Kildene er kontrollert på nytt 26. mars 2026.

### Tekstlige forbedringer
- Dokumentet følger nå oppdatert canvas-struktur uten egen målgruppelinje.
- Hovedfunksjoner er skrevet om til forklarende avsnitt i stedet for punktliste.
- Avgrensningen mot Altinn Melding og Dialogporten er gjort tydeligere.



