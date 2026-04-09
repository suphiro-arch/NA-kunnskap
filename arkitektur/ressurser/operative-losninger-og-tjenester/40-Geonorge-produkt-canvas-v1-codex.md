# Produkt-canvas: Geonorge

## Navn
Geonorge

## Ressurs ID
KART-002

## Status/Livsfase
**Produksjon** - etablert nasjonal geodataportal og fellesløsning for metadata, søk, deling og distribusjon av stedfestet informasjon.

**Fakta:** Kartverket beskriver Geonorge som det nasjonale nettstedet for kartdata og annen stedfestet informasjon i Norge. Geonorge er en del av Norge digitalt, utvikles og driftes av Kartverket på vegne av partene, og beskrives som kjernen i den nasjonale geografiske infrastrukturen.

## Modenhet
**Høy modenhet** - etablert nasjonal fellesløsning for geodata:
- Geonorge brukes som felles katalog og tilgangspunkt for kartdata og andre geodata fra mange offentlige aktører.
- Produktet tilbyr både metadata, datasettoversikter, distribusjonsløsninger og API-er.
- Geonorge er integrert i den nasjonale geografiske infrastrukturen og Norge digitalt-samarbeidet.
- Metadata høstes videre til Felles kartkatalog på data.norge.no.

**Deduksjon:** Modenheten er høy fordi Geonorge er mer enn en portalvisning. Produktet er en nasjonal delings- og samordningsløsning med etablert rolle i både forvaltning, utvikling og gjenbruk av geodata på tvers av sektorer.

## Kort beskrivelse
Geonorge er den nasjonale fellesløsningen for å finne, beskrive, registrere og distribuere kartdata og annen stedfestet informasjon i Norge. Produktet samler metadata om datasett og tjenester, tilbyr søk og API-er, og støtter flere distribusjonsmåter for geodata fra mange offentlige datatilbydere. Geonorge er derfor både en portal, en metadata- og katalogløsning og en delingsinfrastruktur for geodata på tvers av sektorer.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over datasett** er kjernefunksjon ved at Geonorge gir nasjonal oversikt over tilgjengelige geodata og metadata.
- **Datautveksling og integrasjon: Dele data med andre** er relevant fordi Geonorge støtter distribusjon, API-er og tilgjengeliggjøring av geodata fra mange aktører.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Kartverkets og Geonorges beskrivelser av katalog, API-er og distribusjon.

## Produktmål
**Primærkilder:** Sidene `Om Geonorge`, `Geografisk infrastruktur`, `Distribuere data gjennom Geonorge` og utviklersidene for API-er.

Dokumenterte mål:
- Gi brukere av kartdata mulighet til å søke etter og få tilgang til tilgjengelig stedfestet informasjon.
- Støtte registrering av metadata og distribusjon av geodata i den nasjonale geografiske infrastrukturen.
- Være en del av Norge digitalt og den nasjonale samordningen av geodata.

Operative mål utledet fra de samme kildene:
- Gjøre geodata lettere å oppdage, forstå og gjenbruke på tvers av sektorer.
- Gi datatilbydere en felles nasjonal kanal for metadata og distribusjon.
- Understøtte standardisert og mer effektiv deling av geodata gjennom katalog, API-er og nedlastingsløsninger.

## Brukerbehov
- Offentlige virksomheter trenger en felles nasjonal oversikt over tilgjengelige geodata.
- Datatilbydere trenger en felles løsning for å registrere metadata og gjøre data synlige og distribuerbare.
- Utviklere trenger API-er og standardiserte metadata- og søkegrensesnitt.
- Analytikere, planleggere og andre brukere trenger enkel tilgang til geodata fra mange sektorer.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter | Oversikt og tilgang til geodata | Planlegging, analyse, samhandling og tjenesteutvikling | Viktigste tverrsektorielle brukergruppe |
| Datatilbydere i Norge digitalt | Metadataregistrering og distribusjon | Synliggjøring og deling av datasett og tjenester | Viktig kildeside inn i produktet |
| Utviklere og integratører | API-er og metadata-tilgang | Søk, nedlasting, validering og integrasjon | Tydelig teknisk brukergruppe |
| Kart- og geodatabrukere | Enkel oppdagelse og tilgang | Analyse, karttjenester og saksstøtte | Bred brukergruppe på tvers av sektorer |
| Kartverket | Drift, utvikling og samordning | Nasjonal forvaltning av geodatainfrastruktur | Operativ hovedforvalter |

## Hovedfunksjoner
### Primære funksjoner
**Nasjonal katalog over geodata og tjenester.** Geonorge gir brukerne en samlet oversikt over datasett, tjenester og metadata om kartdata og annen stedfestet informasjon. Dette er produktets mest sentrale funksjon.

**Felles metadata- og registreringsløsning.** Produktet gjør det mulig for offentlige virksomheter å registrere og forvalte metadata om geodata i en felles nasjonal struktur. Geonorge er dermed en viktig informasjonsforvaltningsressurs, ikke bare en søkeside.

**Distribusjon og tilgjengeliggjøring av geodata.** Geonorge støtter flere modeller for distribusjon av data, fra lenking til eksterne nedlastingsløsninger til integrert distribusjon gjennom egne API-er og nedlastingsløsninger.

**API-er og tekniske grensesnitt for viderebruk.** Geonorge tilbyr API-er for metadata, katalog, registre og validering. Produktet har dermed tydelig verdi som teknisk byggekloss og ikke bare som brukerrettet portal.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonal geodataportal og metadata-katalog | Alle underliggende primærregistre og originale fagsystemer |
| Registrering, søk og oversikt over geodata og tjenester | Full erstatning for hver enkelt dataeiers egne fagsider |
| API-er, metadata-tilgang og distribusjonsstøtte | Alle spesialiserte geodataprodukter som leveres utenfor Geonorge |
| Del av den nasjonale geografiske infrastrukturen | Hele Kartverkets øvrige portefølje utenfor dette produktområdet |

## Veikart over kommende funksjonalitet
**Fakta fra kildene (kontrollert 2026-03-27):**
- Geonorge publiserer løpende API-er og utviklergrensesnitt for metadata, katalog og registre.
- Produktet framstår som en videreutviklet og levende del av den nasjonale geodatainfrastrukturen.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et samlet, tidsfestet veikart for hele Geonorge er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til å dreie seg om bedre metadatahåndtering, videre API-utvikling, distribusjonsstøtte og samspill med nasjonale kataloger og standarder.

## Forretningsverdi/Verdiforslag
### For offentlig sektor
- Gir én felles nasjonal inngang til geodata på tvers av mange sektorer.
- Gjør det enklere å finne, forstå og bruke stedfestet informasjon i planlegging, analyse og tjenesteutvikling.

### For datatilbydere
- Gir en felles kanal for å synliggjøre og distribuere geodata.
- Reduserer behovet for å bygge hele oppdagelses- og katalogfunksjonen alene.

### For utviklere og brukere
- Gjør geodata mer tilgjengelige gjennom metadata, søk og API-er.
- Styrker grunnlaget for videre gjenbruk i digitale tjenester og analyser.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet og metadata | Svake eller ufullstendige metadata reduserer gjenbruksverdien | Tydelige krav, standarder og validering |
| Samordning | Mange datatilbydere og sektorer kan gi ulik praksis og kvalitet | Felles forvaltning og nasjonale standarder |
| Teknisk kompleksitet | API-er, distribusjon og katalogtjenester må fungere stabilt for mange brukere | Robust drift og tydelig dokumentasjon |
| Scope-forståelse | Brukere kan tro at Geonorge er kilden til alle data, ikke katalog- og delingslaget | Tydelig produktbeskrivelse og sporbarhet til dataeier |
| Avhengighet | Mange tjenester kan bli avhengige av Geonorge som oppdagelses- og tilgangspunkt | Høy prioritet på tilgjengelighet og endringsforvaltning |

## Kanaler
- Om Geonorge: https://www.geonorge.no/aktuelt/om-geonorge/
- Geografisk infrastruktur: https://www.geonorge.no/Geodataarbeid/geografisk-infrastruktur/
- Distribuere data gjennom Geonorge: https://www.geonorge.no/aktuelt/om-geonorge/slik-bruker-du-geonorge/distribuere-data-gjennom-geonorge/
- API-er: https://www.geonorge.no/en/for-developers/apis/
- API-er for kartkatalogen: https://www.geonorge.no/verktoy/APIer-og-grensesnitt/apier-for-kartkatalogen/

## Plattform
Geonorge er en nasjonal katalog-, metadata- og delingsplattform for geodata.

**Fakta:** Produktet kombinerer portalflate, metadataforvaltning, distribusjon og API-er, og er en sentral del av den nasjonale geografiske infrastrukturen.

**Ikke offentlig dokumentert i brukte kilder:** Full intern plattformarkitektur, samlet komponentkart og detaljert teknologistakk utover det som beskrives i API- og infrastruktursidene.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er laget for å støtte oppdagelse og deling av geodata på tvers av mange sektorer.
- Det er særlig relevant når behovet er oversikt over datasett, metadata og tilgang til stedfestet informasjon.
- Det er klart mer tverrsektorielt som fellesressurs enn smalere, sektorspesifikke vegdatatjenester.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at Geonorge gjør geodata oppdagbare og delbare på tvers av virksomheter.
- **P5: Del og gjenbruk løsninger** styrkes ved at mange datatilbydere bruker samme nasjonale katalog- og delingsløsning.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi Geonorge kobler dataeiere, utviklere og brukere gjennom felles metadata- og API-mønstre.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi standarder, metadata og validering er avgjørende for at geodata skal kunne gjenbrukes korrekt.

## Finansiering
- **Fakta:** Kildene beskriver Geonorge som del av Norge digitalt og Kartverkets nasjonale fellesløsninger, men gir ikke en samlet offentlig finansieringsmodell i denne arbeidsøkten.
- **Deduksjon:** Geonorge finansieres som nasjonal fellesløsning i geodatainfrastrukturen, med Kartverket som hovedforvalter på vegne av samarbeidspartene.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Kartverket | Om-siden for Geonorge |
| Drift og utvikling | Kartverket | Om-siden beskriver dette eksplisitt |
| Samstyring | Partene i Norge digitalt | Geonorge beskrives som del av dette samarbeidet |
| Styringsmodell | Nasjonal geodatainfrastruktur med Kartverket som operativ forvalter | Om-siden og infrastruktursiden |

## Lenke til dokumentasjon
- https://www.geonorge.no/aktuelt/om-geonorge/
- https://www.geonorge.no/Geodataarbeid/geografisk-infrastruktur/
- https://www.geonorge.no/aktuelt/om-geonorge/slik-bruker-du-geonorge/distribuere-data-gjennom-geonorge/
- https://www.geonorge.no/en/for-developers/apis/
- https://www.geonorge.no/verktoy/APIer-og-grensesnitt/apier-for-kartkatalogen/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.geonorge.no/aktuelt/om-geonorge/ (kontrollert 2026-03-27)
- Nettkilde: https://www.geonorge.no/Geodataarbeid/geografisk-infrastruktur/ (kontrollert 2026-03-27)
- Nettkilde: https://www.geonorge.no/aktuelt/om-geonorge/slik-bruker-du-geonorge/distribuere-data-gjennom-geonorge/ (kontrollert 2026-03-27)
- Nettkilde: https://www.geonorge.no/en/for-developers/apis/ (kontrollert 2026-03-27)
- Nettkilde: https://www.geonorge.no/verktoy/APIer-og-grensesnitt/apier-for-kartkatalogen/ (kontrollert 2026-03-27)


