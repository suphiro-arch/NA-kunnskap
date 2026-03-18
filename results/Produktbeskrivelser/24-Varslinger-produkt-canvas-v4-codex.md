# Produkt-canvas: Varslinger

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn Varslinger

## Ressurs ID
DIGDIR-022

## Status/Livsfase
**Produksjon** - etablert varslingsprodukt med aktiv videreutvikling.

**Fakta:** Altinn Varslinger tilbyr enveis kommunikasjon med innbyggere og virksomheter, og støtter e-post og SMS med programmatisk utsending og leveringsstatus.

## Modenhet
**Middels til høy funksjonell modenhet** - produktet er etablert og dokumentert, men utvikles videre:
- Produktet har egne sider for funksjoner, forklaringer, feilkoder og statusverdier.
- Tjenesten brukes av tjenesteeiere, Altinn Apps og interne Altinn-tjenester.
- Varslingskanaler og forklaringsdokumentasjon er tydelig beskrevet, samtidig som videre kanalutvidelser er planlagt.

**Deduksjon:** Modenheten er høy for kjernefunksjonene rundt e-post, SMS, oppslag og betinget sending, mens bredden i kanalstøtte fortsatt er under utvikling.

## Kort beskrivelse
Altinn Varslinger er en fellesløsning for enveis digital varsling til innbyggere og virksomheter. Produktet gjør det mulig å sende varsler via e-post og SMS, slå opp mottakerens navn og kontaktinformasjon fra nasjonale registre, bruke autorisasjon for å finne riktige mottakere i organisasjoner og styre utsending basert på betingelser og kanalpreferanser.

## Kapabiliteter
- **Datadrevet: Sammenstilling av data** kombinerer kontaktdata, reservasjonsstatus og autorisasjonsinformasjon for å velge riktig mottaker og kanal.
- **Datautveksling og integrasjon: Meldingsformidling** brukes til programmatisk utsending og leveringsoppfølging av varsler.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** er nødvendig fordi kontaktinformasjon og varslingsinnhold behandles gjennom flere kanaler og oppslag.
- **Sluttbrukertjenester: Proaktive tjenester** gjør det mulig å varsle mottakere når en hendelse eller tilstand krever oppmerksomhet.
- **Tillit: Tilgangskontroll** bruker autorisasjon for å finne riktige mottakere i organisasjonskontekst.
- **Tjenesteutvikling: Integrerbare tjenester** tilbyr API-er for integrasjon med Altinn Apps, Altinn-tjenester og tjenesteeiersystemer.

## Produktmål
**Primærkilder:** Varslinger hovedside, `Om Varslinger`, `Hva får du?` og forklaringssider.

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
| Offentlige tjenesteeiere | Sende varsler i stor skala | Tjenester med behov for e-post og SMS-varsling | Kan bruke Altinn Varslinger i stedet for egen motor |
| Altinn Apps og interne Altinn-tjenester | Integrere varsling i arbeidsflyter | Hendelsesutløst eller planlagt varsling | Dokumentert som berettigede brukere |
| Tjenesteeiersystemer og systemleverandører | Koble egne systemer til utsending og status | API-integrasjon og automatisering | Viktig for robust prosessintegrasjon |
| Innbyggere og virksomheter | Motta tidsriktige varsler | Oppfølging av hendelser og kommunikasjon | Mottar via e-post eller SMS |
| Drifts-, sikkerhets- og forvaltningsmiljøer | Overvåke levering og feilhåndtering | Statuskontroll, oppslag og avvik | Krever kontroll på kanal- og registeravhengigheter |

## Hovedfunksjoner
### Primære funksjoner
- Varsling via e-post og SMS.
- Kanalpreferanser med fallback mellom e-post og SMS.
- Oppslag av navn, kontaktdetaljer og reservasjonsstatus ved bestilling og ved planlagt sendetidspunkt.
- Autorisasjonsbasert identifikasjon av riktige mottakere i organisasjoner.
- Betingede varsler der sending avhenger av resultatet av en betingelsessjekk.
- Programmatisk levering og oppfølging gjennom API-er og statusverdier.
- Støtte for planlagt sending og sendevinduer for SMS.
- Integrasjon med Altinn Apps, Altinn-tjenester og tjenesteeiersystemer.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Enveis varsling via e-post og SMS | Full toveis dialog eller meldingsboksfunksjonalitet |
| Oppslag av mottakere, kontaktdata og reservasjonsstatus | Vedlegg i e-postvarsler |
| Kanalstyring, fallback og betinget sending | Full saksbehandlingsflyt i avsendersystemet |
| Status, feilkoder og programmatisk oppfølging | Selvstendig identitetsforvaltning utenfor Altinn og tilknyttede registre |
| Integrasjon med Altinn Apps, Altinn-tjenester og tjenesteeiersystemer | Alle fremtidige kanaler som ennå ikke er lansert |

## Veikart over kommende funksjonalitet
**Fakta fra kilder (2026-03-10):**
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
- Hva får du?: https://docs.altinn.studio/nb/notifications/what-do-you-get/
- Mottakeroppslag: https://docs.altinn.studio/nb/notifications/explanation/recipient-lookup/
- Referanse: https://docs.altinn.studio/nb/notifications/reference/

## Plattform
API-basert varslingsløsning i Altinn-porteføljen med oppslag mot nasjonale registre og støtte for flere utsendingskanaler.

**Fakta:** Produktet benytter Register, Profil, Ressursregister og Autorisasjon for å hente og verifisere mottakerinformasjon.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur, intern kanalplattform og detaljert kostnadsmodell.

## Gjenbruk
**Høy gjenbruksverdi:**
- Én felles varslingsmotor kan brukes av mange tjenester.
- Felles mønster for oppslag, kanalvalg og status reduserer dobbeltarbeid.
- Integrasjon via API gjør produktet lett å gjenbruke både i Altinn Apps og andre tjenesteeiersystemer.

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov** støtter rettidig varsling i kanalene brukerne faktisk bruker.
- **P5: Del og gjenbruk løsninger** etablerer en felles varslingskapabilitet i stedet for mange lokale løsninger.
- **P6: Lag digitale løsninger som støtter samhandling** kobler sammen tjenester, registre og kanalutsending gjennom standardiserte API-er.
- **P7: Sørg for tillit til oppgaveløsningen** bygger på autorisasjon, registeroppslag og kontroll av mottakeridentitet.

## Finansiering
- Altinn Varslinger fremstår som del av Altinn-porteføljen under Digdir.
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
- https://docs.altinn.studio/nb/notifications/what-do-you-get/
- https://docs.altinn.studio/nb/notifications/explanation/recipient-lookup/
- https://docs.altinn.studio/nb/notifications/reference/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `results/Produktbeskrivelser/24-Varslinger-produkt-canvas-v1-codex.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.altinn.studio/nb/notifications/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/notifications/about/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/notifications/what-do-you-get/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/notifications/explanation/recipient-lookup/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/notifications/reference/ (hentet 2026-03-10)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Verifisert funksjoner, oppslag og kanalstøtte mot oppdatert Altinn-dokumentasjon.
- Lagt inn mer presis beskrivelse av mottakeroppslag, kanalpreferanser og betinget sending.
- Tydeliggjort hvilke Altinn-tjenester Varslinger faktisk bruker for oppslag og autorisasjon.

### Tekstlige forbedringer
- Skrevet om teksten til en mer selvstendig produktbeskrivelse for målgruppen.
- Strukturert brukersegmenter, scope, risiko og verdiforslag i samme standard som nyere produkter.
- Strammet inn innholdet til dokumenterte egenskaper og markert usikkerhet tydeligere der offentlig dokumentasjon mangler.