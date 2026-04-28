# Produkt-canvas: data.norge.no

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
data.norge.no

## Ressurs ID
DIGDIR-014

## Status/Livsfase
**Produksjon** - etablert nasjonal portal for datadeling og oppdagelse av dataressurser.

**Fakta:** data.norge.no samler data fra over 125 virksomheter og over 8000 datasett, og tilbyr både ordinært søk og KI-søk (hentet 2026-03-10).

## Modenhet
**Høy funksjonell modenhet** - etablert og bredt synlig løsning:
- data.norge.no samler flere katalogtyper i samme brukerflate: datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser.
- Løsningen har egen brukerveiledning, teknisk dokumentasjon og nettforumet Datalandsbyen.
- Digitaliseringsdirektoratet har ansvar for drift og utvikling av nettstedet, mens virksomhetene selv forvalter eget innhold i katalogene.

**Deduksjon:** Løsningen er moden som nasjonal inngang til dataoppdagelse, men den faktiske nytteverdien vil variere med kvaliteten på metadataene virksomhetene publiserer.

## Kort beskrivelse
data.norge.no er en nasjonal fellesløsning for å finne, forstå og viderebruke dataressurser. Portalen samler metadata om datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser, og gjør det enklere å oppdage hvilke data offentlig sektor har og kan dele med andre.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over API** synliggjør maskinlesbare grensesnitt i samme katalogstruktur som øvrige dataressurser.
- **Informasjonsforvaltning: Oversikt over begreper** gjør definisjoner tilgjengelige og støtter felles forståelse av data.
- **Informasjonsforvaltning: Oversikt over datasett** gir nasjonal oversikt over publiserte datasett og gjør dem søkbare på tvers av virksomheter.
- **Informasjonsforvaltning: Oversikt over hendelser** gjør hendelser synlige som egne ressurser som kan støtte videre digital samhandling.
- **Informasjonsforvaltning: Oversikt over informasjonsmodeller** synliggjør modeller som kan brukes til semantisk avklaring og bedre tolkning.
- **Informasjonsforvaltning: Oversikt over tjenester** viser relevante offentlige tjenester som del av ressursbildet.
- **Standardisering: Forvaltningsstandarder** bygger på standardisert metadataforvaltning som gir sammenlignbarhet og bedre gjenfinning.

## Produktmål
**Primærkilder:** data.norge.no `Om Data.norge.no` og Samarbeidsportalen `data.norge.no`.

Dokumenterte mål:
- Gi oversikt over hvilke data offentlig sektor har og kan dele.
- Gi datakonsumenter enklere tilgang til dataressurser.
- Fremme viderebruk av data for både kommersielle og ikke-kommersielle formål.
- Synliggjøre hvilke data virksomheter har som de kan dele med andre.

Operative mål utledet fra de samme kildene:
- Gjøre det enklere å finne data gjennom søk, filtre og KI-støttet oppdagelse.
- Hjelpe brukere med å oppdage, vurdere og ta i bruk data, inkludert beskyttede data.
- Synliggjøre informasjon om datatilbydere, tilgjengelighet, datakvalitet og sammenhenger mellom ressurser.

**Deduksjon:** data.norge.no har også en tydelig rolle i å redusere fragmentering ved å samle flere katalogtyper i én nasjonal inngang, selv om dette ikke er formulert som et eget mål i kildene.

## Brukerbehov
- Datakonsumenter trenger ett sted å finne relevante data uten å lete gjennom mange separate nettsteder.
- Datatilbydere trenger en nasjonal kanal som gjør egne dataressurser synlige og forståelige.
- Arkitekter og informasjonsforvaltere trenger oversikt over sammenhenger mellom datasett, API-er, begreper, modeller, tjenester og hendelser.
- Brukere trenger tydelig informasjon om ressurser er åpne, begrensede eller beskyttede, og hvordan tilgang kan oppnås.
- Brukere som ikke finner data, trenger et sted for å etterspørre datasett og få hjelp videre.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige datatilbydere | Publisere og vedlikeholde metadata | Datasett, API-er, begreper og modeller | Innholdet leveres og forvaltes av virksomhetene selv |
| Utviklere og integrasjonsteam | Finne data og API-er raskt | Integrasjon, analyse og tjenesteutvikling | Benytter søk, filtre og dokumentasjon |
| Arkitekter og informasjonsforvaltere | Felles oversikt og semantisk avklaring | Kartlegging, gjenbruk, styring | Har nytte av flere katalogtyper i sammenheng |
| Forskning og innovasjonsmiljø | Oppdage relevante dataressurser | Analyse, forskning og nye tjenester | Viderebruk er del av produktets dokumenterte formål |
| Virksomheter og privat sektor | Finne data for viderebruk | Kommersielle og ikke-kommersielle formål | Nytten er størst når metadata er oppdaterte og forståelige |

## Hovedfunksjoner
### Primære funksjoner
- Felles søk på tvers av datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser.
- KI-søk med naturlig språk. Produktet opplyser samtidig at søket kan være ufullstendig og inneholde feil.
- Standard tekstsøk med avanserte filtre.
- Metadata-visning med informasjon om datatilbyder, tilgjengelighet og datakvalitet.
- Oversikt over om data er åpne eller har begrenset tilgang.
- Brukerveiledning for å finne og dele data.
- Datalandsbyen som nettforum for spørsmål, erfaringsdeling og etterspørsel etter data.
- Støttefunksjoner som virksomhetsoversikt, Etterspør data, Datajegeren og SPARQL-sandkasse.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonal portal for oppdagelse og vurdering av dataressurser | Drift av virksomhetenes egne datasett, API-er og kildeplattformer |
| Kataloger for datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser | Innholdsansvar for metadata hos hver enkelt virksomhet |
| Veiledning, dokumentasjon og fellesskapsarena | Selve tilgangsbehandlingen til hvert datasett |
| Informasjon om tilgjengelighet, datakvalitet og relasjoner mellom ressurser | Garantier for faktisk datakvalitet i kildesystemene |
| Etterspørsel og dialog gjennom Datalandsbyen | Full intern datastyring i publiserende virksomheter |
### Typiske brukssituasjoner (generisk)
- Datakonsument søker etter offentlige dataressurser på tvers av virksomheter og trenger ett sted å starte.
- Analytiker vil forstå tilgjengelighet, datakvalitet og omfang av datasett før videre forespørsel.
- Arkitekt eller prosjekt kartlegger hvilke dataressurser som finnes i et domene for vurdering av gjenbruk.
- Innbygger eller virksomhet ønsker å stille etterspørsel om manglende data via Datalandsbyen.

### Når data.norge.no normalt ikke er førstevalg
- Når behovet er selve datatilgangen – da er Maskinporten eller data.altinn.no mer relevant.
- Når behovet er intern datastyring og katalogisering uten nasjonal publisering.
- Når behovet er å integrere mot et spesifikt API – da er API-ets eget grensesnitt det primære utgangspunktet.

## Veikart over kommende funksjonalitet
**Fakta:**
- Produktet har dokumenterte innganger for `Kostnader`, `Ta i bruk`, `Statistikk`, `Utviklingsplan`, `Teknisk dokumentasjon` og `Driftsmeldinger`.
- KI-søk er allerede en synlig og aktiv funksjon i løsningen.

**Ikke offentlig verifisert i denne arbeidsøkten:** Selve innholdet i `Utviklingsplan` og eventuelle tidsfestede roadmap-punkter er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til å være konsentrert om søkekvalitet, metadataforbedring og støtte til datadeling, men detaljer må bekreftes i utviklingsplanen.

## Forretningsverdi/Verdiforslag
### For datatilbydere
- Øker synlighet og gjenbruk av egne dataressurser gjennom en nasjonal inngang.
- Gjør det enklere å beskrive data i en struktur som er forståelig for andre aktører.

### For datakonsumenter
- Reduserer letetid og gjør det enklere å vurdere om eksisterende data kan brukes.
- Gir bedre grunnlag for å forstå data gjennom kobling til begreper, modeller og API-er.

### For offentlig sektor og samfunn
- Understøtter datadeling som felles praksis i stedet for mange parallelle katalogløsninger.
- Legger til rette for viderebruk i både kommersielle og ikke-kommersielle formål.
- Støtter mer sammenhengende og datadrevet tjenesteutvikling.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil eller ufullstendig informasjon om tilgang og bruksvilkår kan gi feil viderebruk | Tydelige metadatafelt, veiledning og kvalitetssikring hos datatilbyder |
| Teknisk | Ujevn metadata-kvalitet og brutte lenker reduserer søkeverdi og gjenfinning | Validering, vedlikeholdsrutiner og oppfølging av publiserende virksomheter |
| Sikkerhet | Feil publisering av metadata om beskyttede eller begrensede ressurser kan gi uønsket eksponering | Klare publiseringsregler, klassifisering og kontroll |
| Leverandør/forvaltning | Portalen er avhengig av at mange virksomheter holder innholdet sitt oppdatert | Felles forvaltningsregime, veiledning og koordinering fra Digdir |
| Brukeropplevelse | KI-søket kan gi ufullstendige eller feil svar som brukere overvurderer | Tydelig forbehold, standard søk som alternativ og støtte via veiledning |

## Kanaler
- Webportal: https://data.norge.no/
- Om løsningen: https://data.norge.no/nb/about
- Brukerveiledning: https://data.norge.no/nb/docs
- Nettforum / Datalandsbyen: https://data.norge.no/nb/docs/community
- Samarbeidsportalen for produktet: https://samarbeid.digdir.no/felles-datakatalog/datanorgeno/1617
- Samarbeidsportalen for Felles datakatalog: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616

## Plattform
Nasjonal webportal for oppdagelse, metadataforvaltning, veiledning og fellesskapsstøtte knyttet til datadeling.

**Fakta:** Løsningen kombinerer søk, kataloger, veiledning, teknisk dokumentasjon og nettforum i samme produktområde.

**Ikke offentlig dokumentert i brukte kilder:** Full teknisk plattformbeskrivelse, skyvalg, intern søketeknologi og driftsarkitektur.

## Gjenbruk
**Høy gjenbruksverdi:**
- ån nasjonal inngang reduserer behovet for lokale katalogkopier og parallelle oversikter.
- Metadata om samme ressurs kan brukes av mange ulike datakonsumenter.
- Koblingen mellom datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser styrker gjenbruk på tvers av kontekster.
- Datalandsbyen bidrar til gjenbruk av erfaringer og kunnskap, ikke bare data.


### Vanlige kombinasjoner med andre produkter
- **Felles datakatalog** – data.norge.no er portalen som synliggjør innholdet i Felles datakatalog.
- **Begrepskatalog og API-katalog** – deler av innholdet på data.norge.no stammer fra disse.
- **Maskinporten** – etter å ha funnet et API på data.norge.no er Maskinporten neste steg for å skaffe tilgang.
- **data.altinn.no** – noen datasett dokumentert her er tilgjengelige for deling via data.altinn.no.

**Kildekode:** Åpen kildekode. Lisens: Apache-2.0. Kildekode: [github.com/Informasjonsforvaltning/fdk-portal](https://github.com/Informasjonsforvaltning/fdk-portal).

## Støtter arkitekturprinsipper
- **P4 Del og gjenbruk data** - Portalen er direkte innrettet mot oppdagelse og viderebruk av data.
- **P5 Del og gjenbruk løsninger** - data.norge.no fungerer som en felles nasjonal løsning i stedet for mange lokale kataloger.
- **P6 Lag digitale løsninger som støtter samhandling** - Katalogene og veiledningen gir felles oversikt og språk på tvers av virksomheter.
- **P1 Ta utgangspunkt i brukernes behov** - søk, veiledning og etterspørselsstøtte er utformet for å hjelpe brukere med å finne data.

## Finansiering
- **Fakta:** Offentlig kostnadsinformasjon er strukturert som eget tema i forvaltningsmaterialet.
- **Ikke offentlig verifisert i denne arbeidsøkten:** Innholdet på kostnadssiden er ikke kontrollert, og offentlig tilgjengelig finansieringsmodell kan derfor ikke beskrives presist her.
- Det er dokumentert at Digdir har ansvar for drift og utvikling av nettstedet.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | data.norge.no og Samarbeidsportalen |
| Driftsansvar | Digdir har ansvar for drift og utvikling av nettstedet | Om Data.norge.no |
| Budsjettansvar | Ikke offentlig spesifisert i brukte kilder | Kostnadsside finnes, men er ikke verifisert i denne arbeidsøkten |
| Styringsmodell | Digdir forvalter løsningen, mens virksomhetene selv forvalter eget kataloginnhold | Om Data.norge.no |

## Lenke til dokumentasjon
- https://data.norge.no/
- https://data.norge.no/nb/about
- https://data.norge.no/nb/docs
- https://data.norge.no/nb/docs/community
- https://samarbeid.digdir.no/felles-datakatalog/datanorgeno/1617
- https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616
- https://www.digdir.no/felles-datakatalog/om-felles-datakatalog/2274

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/16-data-norge-no-produkt-canvas.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/16-data-norge-no-produkt-canvas-copilot.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/16-data-norge-no-produkt-canvas-codex.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
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
- Produktmål og produktkontekst er kontrollert mot både data.norge.no og Samarbeidsportalen.
- Flere detaljerte påstander fra tidligere forbedringsversjoner er fortsatt holdt tilbake eller markert som ikke offentlig verifisert når offentlig dokumentasjon mangler.

### Tekstlige forbedringer
- Hovedteksten er skrevet om til en selvstendig produktbeskrivelse i stedet for å beskrive hva nettsider eller kilder viser.
- Kapabiliteter og brukersegmenter følger den nye standarden med tydeligere oppdeling og mer direkte språk.
- Fakta, deduksjon og manglende offentlig dokumentasjon er beholdt, men formulert mer konsekvent for målgruppen.



