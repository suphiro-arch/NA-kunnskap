# Produkt-canvas: Geonorge

## Navn
Geonorge

## Ressurs ID
KART-002

## Status/Livsfase
**Produksjon** - etablert nasjonal geodataportal og felleslÃ¸sning for metadata, sÃ¸k, deling og distribusjon av stedfestet informasjon.

**Fakta:** Kartverket beskriver Geonorge som det nasjonale nettstedet for kartdata og annen stedfestet informasjon i Norge. Geonorge er en del av Norge digitalt, utvikles og driftes av Kartverket pÃ¥ vegne av partene, og beskrives som kjernen i den nasjonale geografiske infrastrukturen.

## Modenhet
**HÃ¸y modenhet** - etablert nasjonal felleslÃ¸sning for geodata:
- Geonorge brukes som felles katalog og tilgangspunkt for kartdata og andre geodata fra mange offentlige aktÃ¸rer.
- Produktet tilbyr bÃ¥de metadata, datasettoversikter, distribusjonslÃ¸sninger og API-er.
- Geonorge er integrert i den nasjonale geografiske infrastrukturen og Norge digitalt-samarbeidet.
- Metadata hÃ¸stes videre til Felles kartkatalog pÃ¥ data.norge.no.

**Deduksjon:** Modenheten er hÃ¸y fordi Geonorge er mer enn en portalvisning. Produktet er en nasjonal delings- og samordningslÃ¸sning med etablert rolle i bÃ¥de forvaltning, utvikling og gjenbruk av geodata pÃ¥ tvers av sektorer.

## Kort beskrivelse
Geonorge er den nasjonale felleslÃ¸sningen for Ã¥ finne, beskrive, registrere og distribuere kartdata og annen stedfestet informasjon i Norge. Produktet samler metadata om datasett og tjenester, tilbyr sÃ¸k og API-er, og stÃ¸tter flere distribusjonsmÃ¥ter for geodata fra mange offentlige datatilbydere. Geonorge er derfor bÃ¥de en portal, en metadata- og kataloglÃ¸sning og en delingsinfrastruktur for geodata pÃ¥ tvers av sektorer.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over datasett** er kjernefunksjon ved at Geonorge gir nasjonal oversikt over tilgjengelige geodata og metadata.
- **Datautveksling og integrasjon: Dele data med andre** er relevant fordi Geonorge stÃ¸tter distribusjon, API-er og tilgjengeliggjÃ¸ring av geodata fra mange aktÃ¸rer.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Kartverkets og Geonorges beskrivelser av katalog, API-er og distribusjon.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Sidene `Om Geonorge`, `Geografisk infrastruktur`, `Distribuere data gjennom Geonorge` og utviklersidene for API-er.

Dokumenterte mÃ¥l:
- Gi brukere av kartdata mulighet til Ã¥ sÃ¸ke etter og fÃ¥ tilgang til tilgjengelig stedfestet informasjon.
- StÃ¸tte registrering av metadata og distribusjon av geodata i den nasjonale geografiske infrastrukturen.
- VÃ¦re en del av Norge digitalt og den nasjonale samordningen av geodata.

Operative mÃ¥l utledet fra de samme kildene:
- GjÃ¸re geodata lettere Ã¥ oppdage, forstÃ¥ og gjenbruke pÃ¥ tvers av sektorer.
- Gi datatilbydere en felles nasjonal kanal for metadata og distribusjon.
- UnderstÃ¸tte standardisert og mer effektiv deling av geodata gjennom katalog, API-er og nedlastingslÃ¸sninger.

## Brukerbehov
- Offentlige virksomheter trenger en felles nasjonal oversikt over tilgjengelige geodata.
- Datatilbydere trenger en felles lÃ¸sning for Ã¥ registrere metadata og gjÃ¸re data synlige og distribuerbare.
- Utviklere trenger API-er og standardiserte metadata- og sÃ¸kegrensesnitt.
- Analytikere, planleggere og andre brukere trenger enkel tilgang til geodata fra mange sektorer.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige virksomheter | Oversikt og tilgang til geodata | Planlegging, analyse, samhandling og tjenesteutvikling | Viktigste tverrsektorielle brukergruppe |
| Datatilbydere i Norge digitalt | Metadataregistrering og distribusjon | SynliggjÃ¸ring og deling av datasett og tjenester | Viktig kildeside inn i produktet |
| Utviklere og integratÃ¸rer | API-er og metadata-tilgang | SÃ¸k, nedlasting, validering og integrasjon | Tydelig teknisk brukergruppe |
| Kart- og geodatabrukere | Enkel oppdagelse og tilgang | Analyse, karttjenester og saksstÃ¸tte | Bred brukergruppe pÃ¥ tvers av sektorer |
| Kartverket | Drift, utvikling og samordning | Nasjonal forvaltning av geodatainfrastruktur | Operativ hovedforvalter |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
**Nasjonal katalog over geodata og tjenester.** Geonorge gir brukerne en samlet oversikt over datasett, tjenester og metadata om kartdata og annen stedfestet informasjon. Dette er produktets mest sentrale funksjon.

**Felles metadata- og registreringslÃ¸sning.** Produktet gjÃ¸r det mulig for offentlige virksomheter Ã¥ registrere og forvalte metadata om geodata i en felles nasjonal struktur. Geonorge er dermed en viktig informasjonsforvaltningsressurs, ikke bare en sÃ¸keside.

**Distribusjon og tilgjengeliggjÃ¸ring av geodata.** Geonorge stÃ¸tter flere modeller for distribusjon av data, fra lenking til eksterne nedlastingslÃ¸sninger til integrert distribusjon gjennom egne API-er og nedlastingslÃ¸sninger.

**API-er og tekniske grensesnitt for viderebruk.** Geonorge tilbyr API-er for metadata, katalog, registre og validering. Produktet har dermed tydelig verdi som teknisk byggekloss og ikke bare som brukerrettet portal.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Nasjonal geodataportal og metadata-katalog | Alle underliggende primÃ¦rregistre og originale fagsystemer |
| Registrering, sÃ¸k og oversikt over geodata og tjenester | Full erstatning for hver enkelt dataeiers egne fagsider |
| API-er, metadata-tilgang og distribusjonsstÃ¸tte | Alle spesialiserte geodataprodukter som leveres utenfor Geonorge |
| Del av den nasjonale geografiske infrastrukturen | Hele Kartverkets Ã¸vrige portefÃ¸lje utenfor dette produktomrÃ¥det |

## Veikart over kommende funksjonalitet
**Fakta fra kildene (kontrollert 2026-03-27):**
- Geonorge publiserer lÃ¸pende API-er og utviklergrensesnitt for metadata, katalog og registre.
- Produktet framstÃ¥r som en videreutviklet og levende del av den nasjonale geodatainfrastrukturen.

**Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Et samlet, tidsfestet veikart for hele Geonorge er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til Ã¥ dreie seg om bedre metadatahÃ¥ndtering, videre API-utvikling, distribusjonsstÃ¸tte og samspill med nasjonale kataloger og standarder.

## Forretningsverdi/Verdiforslag
### For offentlig sektor
- Gir Ã©n felles nasjonal inngang til geodata pÃ¥ tvers av mange sektorer.
- GjÃ¸r det enklere Ã¥ finne, forstÃ¥ og bruke stedfestet informasjon i planlegging, analyse og tjenesteutvikling.

### For datatilbydere
- Gir en felles kanal for Ã¥ synliggjÃ¸re og distribuere geodata.
- Reduserer behovet for Ã¥ bygge hele oppdagelses- og katalogfunksjonen alene.

### For utviklere og brukere
- GjÃ¸r geodata mer tilgjengelige gjennom metadata, sÃ¸k og API-er.
- Styrker grunnlaget for videre gjenbruk i digitale tjenester og analyser.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Datakvalitet og metadata | Svake eller ufullstendige metadata reduserer gjenbruksverdien | Tydelige krav, standarder og validering |
| Samordning | Mange datatilbydere og sektorer kan gi ulik praksis og kvalitet | Felles forvaltning og nasjonale standarder |
| Teknisk kompleksitet | API-er, distribusjon og katalogtjenester mÃ¥ fungere stabilt for mange brukere | Robust drift og tydelig dokumentasjon |
| Scope-forstÃ¥else | Brukere kan tro at Geonorge er kilden til alle data, ikke katalog- og delingslaget | Tydelig produktbeskrivelse og sporbarhet til dataeier |
| Avhengighet | Mange tjenester kan bli avhengige av Geonorge som oppdagelses- og tilgangspunkt | HÃ¸y prioritet pÃ¥ tilgjengelighet og endringsforvaltning |

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
**HÃ¸y gjenbruksverdi:**
- Produktet er laget for Ã¥ stÃ¸tte oppdagelse og deling av geodata pÃ¥ tvers av mange sektorer.
- Det er sÃ¦rlig relevant nÃ¥r behovet er oversikt over datasett, metadata og tilgang til stedfestet informasjon.
- Det er klart mer tverrsektorielt som fellesressurs enn smalere, sektorspesifikke vegdatatjenester.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at Geonorge gjÃ¸r geodata oppdagbare og delbare pÃ¥ tvers av virksomheter.
- **P5: Del og gjenbruk lÃ¸sninger** styrkes ved at mange datatilbydere bruker samme nasjonale katalog- og delingslÃ¸sning.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** stÃ¸ttes fordi Geonorge kobler dataeiere, utviklere og brukere gjennom felles metadata- og API-mÃ¸nstre.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** er sentralt fordi standarder, metadata og validering er avgjÃ¸rende for at geodata skal kunne gjenbrukes korrekt.

## Finansiering
- **Fakta:** Kildene beskriver Geonorge som del av Norge digitalt og Kartverkets nasjonale felleslÃ¸sninger, men gir ikke en samlet offentlig finansieringsmodell i denne arbeidsÃ¸kten.
- **Deduksjon:** Geonorge finansieres som nasjonal felleslÃ¸sning i geodatainfrastrukturen, med Kartverket som hovedforvalter pÃ¥ vegne av samarbeidspartene.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
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

