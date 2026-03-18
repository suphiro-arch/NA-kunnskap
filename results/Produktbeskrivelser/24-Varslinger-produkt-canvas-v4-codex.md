# Produkt-canvas: Varslinger

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn Varslinger

## Ressurs ID
DIGDIR-022

## Status/Livsfase
**Produksjon** - etablert varslingsprodukt med aktiv videreutvikling.

**Fakta:** Altinn Varslinger tilbyr enveis kommunikasjon med innbyggere og virksomheter, og stÃ¸tter e-post og SMS med programmatisk utsending og leveringsstatus.

## Modenhet
**Middels til hÃ¸y funksjonell modenhet** - produktet er etablert og dokumentert, men utvikles videre:
- Produktet har egne sider for funksjoner, forklaringer, feilkoder og statusverdier.
- Tjenesten brukes av tjenesteeiere, Altinn Apps og interne Altinn-tjenester.
- Varslingskanaler og forklaringsdokumentasjon er tydelig beskrevet, samtidig som videre kanalutvidelser er planlagt.

**Deduksjon:** Modenheten er hÃ¸y for kjernefunksjonene rundt e-post, SMS, oppslag og betinget sending, mens bredden i kanalstÃ¸tte fortsatt er under utvikling.

## Kort beskrivelse
Altinn Varslinger er en felleslÃ¸sning for enveis digital varsling til innbyggere og virksomheter. Produktet gjÃ¸r det mulig Ã¥ sende varsler via e-post og SMS, slÃ¥ opp mottakerens navn og kontaktinformasjon fra nasjonale registre, bruke autorisasjon for Ã¥ finne riktige mottakere i organisasjoner og styre utsending basert pÃ¥ betingelser og kanalpreferanser.

## Kapabiliteter
- **Sluttbrukertjenester: Proaktive tjenester** gjÃ¸r det mulig Ã¥ varsle mottakere nÃ¥r en hendelse eller tilstand krever oppmerksomhet.
- **Datautveksling og integrasjon: Meldingsformidling** brukes til programmatisk utsending og leveringsoppfÃ¸lging av varsler.
- **Tjenesteutvikling: Integrerbare tjenester** tilbyr API-er for integrasjon med Altinn Apps, Altinn-tjenester og tjenesteeiersystemer.
- **Tillit: Tilgangskontroll** bruker autorisasjon for Ã¥ finne riktige mottakere i organisasjonskontekst.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** er nÃ¸dvendig fordi kontaktinformasjon og varslingsinnhold behandles gjennom flere kanaler og oppslag.
- **Datadrevet: Sammenstilling av data** kombinerer kontaktdata, reservasjonsstatus og autorisasjonsinformasjon for Ã¥ velge riktig mottaker og kanal.
- **Standardisering: Forvaltningsstandarder** gir tjenesteeiere et felles mÃ¸nster for kanalvalg, oppslag og status i stedet for lokale varslingsmotorer.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i Altinn Varslinger.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Varslinger hovedside, `Om Varslinger`, `Hva fÃ¥r du?` og forklaringssider.

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
| Offentlige tjenesteeiere | Sende varsler i stor skala | Tjenester med behov for e-post og SMS-varsling | Kan bruke Altinn Varslinger i stedet for egen motor |
| Altinn Apps og interne Altinn-tjenester | Integrere varsling i arbeidsflyter | HendelsesutlÃ¸st eller planlagt varsling | Dokumentert som berettigede brukere |
| Tjenesteeiersystemer og systemleverandÃ¸rer | Koble egne systemer til utsending og status | API-integrasjon og automatisering | Viktig for robust prosessintegrasjon |
| Innbyggere og virksomheter | Motta tidsriktige varsler | OppfÃ¸lging av hendelser og kommunikasjon | Mottar via e-post eller SMS |
| Drifts-, sikkerhets- og forvaltningsmiljÃ¸er | OvervÃ¥ke levering og feilhÃ¥ndtering | Statuskontroll, oppslag og avvik | Krever kontroll pÃ¥ kanal- og registeravhengigheter |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- Varsling via e-post og SMS.
- Kanalpreferanser med fallback mellom e-post og SMS.
- Oppslag av navn, kontaktdetaljer og reservasjonsstatus ved bestilling og ved planlagt sendetidspunkt.
- Autorisasjonsbasert identifikasjon av riktige mottakere i organisasjoner.
- Betingede varsler der sending avhenger av resultatet av en betingelsessjekk.
- Programmatisk levering og oppfÃ¸lging gjennom API-er og statusverdier.
- StÃ¸tte for planlagt sending og sendevinduer for SMS.
- Integrasjon med Altinn Apps, Altinn-tjenester og tjenesteeiersystemer.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Enveis varsling via e-post og SMS | Full toveis dialog eller meldingsboksfunksjonalitet |
| Oppslag av mottakere, kontaktdata og reservasjonsstatus | Vedlegg i e-postvarsler |
| Kanalstyring, fallback og betinget sending | Full saksbehandlingsflyt i avsendersystemet |
| Status, feilkoder og programmatisk oppfÃ¸lging | Selvstendig identitetsforvaltning utenfor Altinn og tilknyttede registre |
| Integrasjon med Altinn Apps, Altinn-tjenester og tjenesteeiersystemer | Alle fremtidige kanaler som ennÃ¥ ikke er lansert |

## Veikart over kommende funksjonalitet
**Fakta fra kilder (2026-03-10):**
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
- Hva fÃ¥r du?: https://docs.altinn.studio/nb/notifications/what-do-you-get/
- Mottakeroppslag: https://docs.altinn.studio/nb/notifications/explanation/recipient-lookup/
- Referanse: https://docs.altinn.studio/nb/notifications/reference/

## Plattform
API-basert varslingslÃ¸sning i Altinn-portefÃ¸ljen med oppslag mot nasjonale registre og stÃ¸tte for flere utsendingskanaler.

**Fakta:** Produktet benytter Register, Profil, Ressursregister og Autorisasjon for Ã¥ hente og verifisere mottakerinformasjon.

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
- Altinn Varslinger fremstÃ¥r som del av Altinn-portefÃ¸ljen under Digdir.
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
- Verifisert funksjoner, oppslag og kanalstÃ¸tte mot oppdatert Altinn-dokumentasjon.
- Lagt inn mer presis beskrivelse av mottakeroppslag, kanalpreferanser og betinget sending.
- Tydeliggjort hvilke Altinn-tjenester Varslinger faktisk bruker for oppslag og autorisasjon.

### Tekstlige forbedringer
- Skrevet om teksten til en mer selvstendig produktbeskrivelse for mÃ¥lgruppen.
- Strukturert brukersegmenter, scope, risiko og verdiforslag i samme standard som nyere produkter.
- Strammet inn innholdet til dokumenterte egenskaper og markert usikkerhet tydeligere der offentlig dokumentasjon mangler.