# Produkt-canvas: data.norge.no

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
data.norge.no

## Ressurs ID
DIGDIR-014

## Status/Livsfase
**Produksjon** - etablert nasjonal portal for datadeling og oppdagelse av dataressurser.

**Fakta:** data.norge.no samler data fra over 125 virksomheter og over 8000 datasett, og tilbyr bÃ¥de ordinÃ¦rt sÃ¸k og KI-sÃ¸k (hentet 2026-03-10).

## Modenhet
**HÃ¸y funksjonell modenhet** - etablert og bredt synlig lÃ¸sning:
- data.norge.no samler flere katalogtyper i samme brukerflate: datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser.
- LÃ¸sningen har egen brukerveiledning, teknisk dokumentasjon og nettforumet Datalandsbyen.
- Digitaliseringsdirektoratet har ansvar for drift og utvikling av nettstedet, mens virksomhetene selv forvalter eget innhold i katalogene.

**Deduksjon:** LÃ¸sningen er moden som nasjonal inngang til dataoppdagelse, men den faktiske nytteverdien vil variere med kvaliteten pÃ¥ metadataene virksomhetene publiserer.

## Kort beskrivelse
data.norge.no er en nasjonal felleslÃ¸sning for Ã¥ finne, forstÃ¥ og viderebruke dataressurser. Portalen samler metadata om datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser, og gjÃ¸r det enklere Ã¥ oppdage hvilke data offentlig sektor har og kan dele med andre.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over datasett** gir nasjonal oversikt over publiserte datasett og gjÃ¸r dem sÃ¸kbare pÃ¥ tvers av virksomheter.
- **Informasjonsforvaltning: Oversikt over API** synliggjÃ¸r maskinlesbare grensesnitt i samme katalogstruktur som Ã¸vrige dataressurser.
- **Informasjonsforvaltning: Oversikt over begreper** gjÃ¸r definisjoner tilgjengelige og stÃ¸tter felles forstÃ¥else av data.
- **Informasjonsforvaltning: Oversikt over informasjonsmodeller** synliggjÃ¸r modeller som kan brukes til semantisk avklaring og bedre tolkning.
- **Informasjonsforvaltning: Oversikt over tjenester** viser relevante offentlige tjenester som del av ressursbildet.
- **Informasjonsforvaltning: Oversikt over hendelser** gjÃ¸r hendelser synlige som egne ressurser som kan stÃ¸tte videre digital samhandling.
- **Datautveksling og integrasjon: Dele data med andre** gir datatilbydere en nasjonal kanal for Ã¥ gjÃ¸re dataressurser oppdagbare og forstÃ¥elige.
- **Datautveksling og integrasjon: Bruke data fra andre** gir datakonsumenter ett sted Ã¥ oppdage, vurdere og finne tilgangsinformasjon om dataressurser.
- **Standardisering: Forvaltningsstandarder** bygger pÃ¥ standardisert metadataforvaltning som gir sammenlignbarhet og bedre gjenfinning.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i data.norge.no og Samarbeidsportalen.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** data.norge.no `Om Data.norge.no` og Samarbeidsportalen `data.norge.no`.

Dokumenterte mÃ¥l:
- Gi oversikt over hvilke data offentlig sektor har og kan dele.
- Gi datakonsumenter enklere tilgang til dataressurser.
- Fremme viderebruk av data for bÃ¥de kommersielle og ikke-kommersielle formÃ¥l.
- SynliggjÃ¸re hvilke data virksomheter har som de kan dele med andre.

Operative mÃ¥l utledet fra de samme kildene:
- GjÃ¸re det enklere Ã¥ finne data gjennom sÃ¸k, filtre og KI-stÃ¸ttet oppdagelse.
- Hjelpe brukere med Ã¥ oppdage, vurdere og ta i bruk data, inkludert beskyttede data.
- SynliggjÃ¸re informasjon om datatilbydere, tilgjengelighet, datakvalitet og sammenhenger mellom ressurser.

**Deduksjon:** data.norge.no har ogsÃ¥ en tydelig rolle i Ã¥ redusere fragmentering ved Ã¥ samle flere katalogtyper i Ã©n nasjonal inngang, selv om dette ikke er formulert som et eget mÃ¥l i kildene.

## Brukerbehov
- Datakonsumenter trenger ett sted Ã¥ finne relevante data uten Ã¥ lete gjennom mange separate nettsteder.
- Datatilbydere trenger en nasjonal kanal som gjÃ¸r egne dataressurser synlige og forstÃ¥elige.
- Arkitekter og informasjonsforvaltere trenger oversikt over sammenhenger mellom datasett, API-er, begreper, modeller, tjenester og hendelser.
- Brukere trenger tydelig informasjon om ressurser er Ã¥pne, begrensede eller beskyttede, og hvordan tilgang kan oppnÃ¥s.
- Brukere som ikke finner data, trenger et sted for Ã¥ etterspÃ¸rre datasett og fÃ¥ hjelp videre.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige datatilbydere | Publisere og vedlikeholde metadata | Datasett, API-er, begreper og modeller | Innholdet leveres og forvaltes av virksomhetene selv |
| Utviklere og integrasjonsteam | Finne data og API-er raskt | Integrasjon, analyse og tjenesteutvikling | Benytter sÃ¸k, filtre og dokumentasjon |
| Arkitekter og informasjonsforvaltere | Felles oversikt og semantisk avklaring | Kartlegging, gjenbruk, styring | Har nytte av flere katalogtyper i sammenheng |
| Forskning og innovasjonsmiljÃ¸ | Oppdage relevante dataressurser | Analyse, forskning og nye tjenester | Viderebruk er del av produktets dokumenterte formÃ¥l |
| Virksomheter og privat sektor | Finne data for viderebruk | Kommersielle og ikke-kommersielle formÃ¥l | Nytten er stÃ¸rst nÃ¥r metadata er oppdaterte og forstÃ¥elige |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- Felles sÃ¸k pÃ¥ tvers av datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser.
- KI-sÃ¸k med naturlig sprÃ¥k. Produktet opplyser samtidig at sÃ¸ket kan vÃ¦re ufullstendig og inneholde feil.
- Standard tekstsÃ¸k med avanserte filtre.
- Metadata-visning med informasjon om datatilbyder, tilgjengelighet og datakvalitet.
- Oversikt over om data er Ã¥pne eller har begrenset tilgang.
- Brukerveiledning for Ã¥ finne og dele data.
- Datalandsbyen som nettforum for spÃ¸rsmÃ¥l, erfaringsdeling og etterspÃ¸rsel etter data.
- StÃ¸ttefunksjoner som virksomhetsoversikt, EtterspÃ¸r data, Datajegeren og SPARQL-sandkasse.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Nasjonal portal for oppdagelse og vurdering av dataressurser | Drift av virksomhetenes egne datasett, API-er og kildeplattformer |
| Kataloger for datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser | Innholdsansvar for metadata hos hver enkelt virksomhet |
| Veiledning, dokumentasjon og fellesskapsarena | Selve tilgangsbehandlingen til hvert datasett |
| Informasjon om tilgjengelighet, datakvalitet og relasjoner mellom ressurser | Garantier for faktisk datakvalitet i kildesystemene |
| EtterspÃ¸rsel og dialog gjennom Datalandsbyen | Full intern datastyring i publiserende virksomheter |

## Veikart over kommende funksjonalitet
**Fakta:**
- Produktet har dokumenterte innganger for `Kostnader`, `Ta i bruk`, `Statistikk`, `Utviklingsplan`, `Teknisk dokumentasjon` og `Driftsmeldinger`.
- KI-sÃ¸k er allerede en synlig og aktiv funksjon i lÃ¸sningen.

**Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Selve innholdet i `Utviklingsplan` og eventuelle tidsfestede roadmap-punkter er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til Ã¥ vÃ¦re konsentrert om sÃ¸kekvalitet, metadataforbedring og stÃ¸tte til datadeling, men detaljer mÃ¥ bekreftes i utviklingsplanen.

## Forretningsverdi/Verdiforslag
### For datatilbydere
- Ã˜ker synlighet og gjenbruk av egne dataressurser gjennom en nasjonal inngang.
- GjÃ¸r det enklere Ã¥ beskrive data i en struktur som er forstÃ¥elig for andre aktÃ¸rer.

### For datakonsumenter
- Reduserer letetid og gjÃ¸r det enklere Ã¥ vurdere om eksisterende data kan brukes.
- Gir bedre grunnlag for Ã¥ forstÃ¥ data gjennom kobling til begreper, modeller og API-er.

### For offentlig sektor og samfunn
- UnderstÃ¸tter datadeling som felles praksis i stedet for mange parallelle kataloglÃ¸sninger.
- Legger til rette for viderebruk i bÃ¥de kommersielle og ikke-kommersielle formÃ¥l.
- StÃ¸tter mer sammenhengende og datadrevet tjenesteutvikling.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Feil eller ufullstendig informasjon om tilgang og bruksvilkÃ¥r kan gi feil viderebruk | Tydelige metadatafelt, veiledning og kvalitetssikring hos datatilbyder |
| Teknisk | Ujevn metadata-kvalitet og brutte lenker reduserer sÃ¸keverdi og gjenfinning | Validering, vedlikeholdsrutiner og oppfÃ¸lging av publiserende virksomheter |
| Sikkerhet | Feil publisering av metadata om beskyttede eller begrensede ressurser kan gi uÃ¸nsket eksponering | Klare publiseringsregler, klassifisering og kontroll |
| LeverandÃ¸r/forvaltning | Portalen er avhengig av at mange virksomheter holder innholdet sitt oppdatert | Felles forvaltningsregime, veiledning og koordinering fra Digdir |
| Brukeropplevelse | KI-sÃ¸ket kan gi ufullstendige eller feil svar som brukere overvurderer | Tydelig forbehold, standard sÃ¸k som alternativ og stÃ¸tte via veiledning |

## Kanaler
- Webportal: https://data.norge.no/
- Om lÃ¸sningen: https://data.norge.no/nb/about
- Brukerveiledning: https://data.norge.no/nb/docs
- Nettforum / Datalandsbyen: https://data.norge.no/nb/docs/community
- Samarbeidsportalen for produktet: https://samarbeid.digdir.no/felles-datakatalog/datanorgeno/1617
- Samarbeidsportalen for Felles datakatalog: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616

## Plattform
Nasjonal webportal for oppdagelse, metadataforvaltning, veiledning og fellesskapsstÃ¸tte knyttet til datadeling.

**Fakta:** LÃ¸sningen kombinerer sÃ¸k, kataloger, veiledning, teknisk dokumentasjon og nettforum i samme produktomrÃ¥de.

**Ikke offentlig dokumentert i brukte kilder:** Full teknisk plattformbeskrivelse, skyvalg, intern sÃ¸keteknologi og driftsarkitektur.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Ã‰n nasjonal inngang reduserer behovet for lokale katalogkopier og parallelle oversikter.
- Metadata om samme ressurs kan brukes av mange ulike datakonsumenter.
- Koblingen mellom datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser styrker gjenbruk pÃ¥ tvers av kontekster.
- Datalandsbyen bidrar til gjenbruk av erfaringer og kunnskap, ikke bare data.

## StÃ¸tter arkitekturprinsipper
- **P4 Del og gjenbruk data** - Portalen er direkte innrettet mot oppdagelse og viderebruk av data.
- **P5 Del og gjenbruk lÃ¸sninger** - data.norge.no fungerer som en felles nasjonal lÃ¸sning i stedet for mange lokale kataloger.
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** - Katalogene og veiledningen gir felles oversikt og sprÃ¥k pÃ¥ tvers av virksomheter.
- **P1 Ta utgangspunkt i brukernes behov** - sÃ¸k, veiledning og etterspÃ¸rselsstÃ¸tte er utformet for Ã¥ hjelpe brukere med Ã¥ finne data.

## Finansiering
- **Fakta:** Offentlig kostnadsinformasjon er strukturert som eget tema i forvaltningsmaterialet.
- **Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Innholdet pÃ¥ kostnadssiden er ikke kontrollert, og offentlig tilgjengelig finansieringsmodell kan derfor ikke beskrives presist her.
- Det er dokumentert at Digdir har ansvar for drift og utvikling av nettstedet.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | data.norge.no og Samarbeidsportalen |
| Driftsansvar | Digdir har ansvar for drift og utvikling av nettstedet | Om Data.norge.no |
| Budsjettansvar | Ikke offentlig spesifisert i brukte kilder | Kostnadsside finnes, men er ikke verifisert i denne arbeidsÃ¸kten |
| Styringsmodell | Digdir forvalter lÃ¸sningen, mens virksomhetene selv forvalter eget kataloginnhold | Om Data.norge.no |

## Lenke til dokumentasjon
- https://data.norge.no/
- https://data.norge.no/nb/about
- https://data.norge.no/nb/docs
- https://data.norge.no/nb/docs/community
- https://samarbeid.digdir.no/felles-datakatalog/datanorgeno/1617
- https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616
- https://www.digdir.no/felles-datakatalog/om-felles-datakatalog/2274

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `results/Produktbeskrivelser/16-data-norge-no-produkt-canvas.md`
- Lokal fil: `results/Produktbeskrivelser/16-data-norge-no-produkt-canvas-copilot.md`
- Lokal fil: `results/Produktbeskrivelser/16-data-norge-no-produkt-canvas-codex.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://data.norge.no/ (hentet 2026-03-10)
- Nettkilde: https://data.norge.no/nb/about (hentet 2026-03-10)
- Nettkilde: https://data.norge.no/nb/docs (hentet 2026-03-10)
- Nettkilde: https://data.norge.no/nb/docs/community (hentet 2026-03-10)
- Nettkilde: https://samarbeid.digdir.no/felles-datakatalog/datanorgeno/1617 (hentet 2026-03-10)
- Nettkilde: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616 (hentet 2026-03-10)

---

## Endringer fra forrige versjoner

### Analyseforbedringer
- Utgangspunktet er fortsatt siste forbedringsfil, `16-data-norge-no-produkt-canvas-copilot.md`, men innholdet er strammet inn mot det som lot seg verifisere offentlig i brukt kildegrunnlag.
- ProduktmÃ¥l og produktkontekst er kontrollert mot bÃ¥de data.norge.no og Samarbeidsportalen.
- Flere detaljerte pÃ¥stander fra tidligere forbedringsversjoner er fortsatt holdt tilbake eller markert som ikke offentlig verifisert nÃ¥r offentlig dokumentasjon mangler.

### Tekstlige forbedringer
- Hovedteksten er skrevet om til en selvstendig produktbeskrivelse i stedet for Ã¥ beskrive hva nettsider eller kilder viser.
- Kapabiliteter og brukersegmenter fÃ¸lger den nye standarden med tydeligere oppdeling og mer direkte sprÃ¥k.
- Fakta, deduksjon og manglende offentlig dokumentasjon er beholdt, men formulert mer konsekvent for mÃ¥lgruppen.
