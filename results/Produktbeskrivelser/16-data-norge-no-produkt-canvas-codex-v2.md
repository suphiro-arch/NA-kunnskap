# Produkt-canvas: data.norge.no

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
data.norge.no

## Ressurs ID
16 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** - etablert nasjonal portal for datadeling og oppdagelse av dataressurser.

**Fakta:** Forsiden på data.norge.no beskriver løsningen som "Der Norge deler data" og viser at KI-søket omfatter data fra over 125 virksomheter og over 8000 datasett (hentet 2026-03-10).

## Modenhet
**Høy funksjonell modenhet** - etablert og bredt synlig løsning:
- data.norge.no tilbyr flere katalogtyper i samme brukerflate: datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser.
- Portalen har egen brukerveiledning, teknisk dokumentasjon og nettforumet Datalandsbyen.
- Digitaliseringsdirektoratet er ansvarlig for drift og utvikling av nettstedet, mens virksomhetene selv forvalter eget innhold i katalogene.

**Deduksjon:** Løsningen fremstår som moden som nasjonal inngang, men kvaliteten i katalogene vil variere med hvor godt den enkelte virksomhet publiserer og vedlikeholder metadata.

## Kort beskrivelse
data.norge.no er en nasjonal fellesløsning for å finne, forstå og viderebruke dataressurser. Portalen samler metadata om datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser, og gjør det enklere å oppdage hvilke data offentlig sektor har og kan dele med andre.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over datasett**
  Portalen gir nasjonal oversikt over publiserte datasett og gjør dem søkbare på tvers av virksomheter.
- **Informasjonsforvaltning: Oversikt over API**
  API-er synliggjøres som del av samme katalogstruktur, slik at datakonsumenter lettere kan finne maskinlesbare grensesnitt.
- **Informasjonsforvaltning: Oversikt over begreper**
  Begreper og definisjoner gjøres tilgjengelige for å støtte felles forståelse av data.
- **Informasjonsforvaltning: Oversikt over informasjonsmodeller**
  Informasjonsmodeller synliggjøres som egne ressurser og kan brukes til semantisk avklaring.
- **Informasjonsforvaltning: Oversikt over tjenester**
  Tjenester i offentlig sektor inngår som del av ressursbildet på portalen.
- **Informasjonsforvaltning: Oversikt over hendelser**
  Hendelser synliggjøres som egne ressurser som kan støtte videre digital samhandling.
- **Datautveksling og integrasjon: Dele data med andre**
  Datatilbydere får en nasjonal kanal for å gjøre dataressurser oppdagbare og forståelige.
- **Datautveksling og integrasjon: Bruke data fra andre**
  Datakonsumenter får ett sted å oppdage, vurdere og finne tilgangsinformasjon om dataressurser.
- **Standardisering: Forvaltningsstandarder**
  Portalen bygger på standardisert metadataforvaltning for å gi sammenlignbarhet og gjenfinnbarhet.

Grunnlag: Kapabilitetsnavn fra `index/capabilities.yaml`, vurdert mot dokumentert funksjon i data.norge.no og Samarbeidsportalen.

## Produktmål
**Primærkilder:** data.norge.no `Om Data.norge.no` og Samarbeidsportalen `data.norge.no`.

Dokumenterte mål:
- Gi oversikt over hvilke data offentlig sektor har og kan dele.
- Gi datakonsumenter enklere tilgang til dataressurser.
- Fremme viderebruk av data for både kommersielle og ikke-kommersielle formål.
- Vise hvilke data virksomheter har som de kan dele med andre.

Operative mål utledet fra de samme kildene:
- Gjøre det enklere å finne data gjennom standard søk, avanserte filtre og KI-søk.
- Hjelpe brukere med å oppdage, vurdere og ta i bruk data, inkludert beskyttede data.
- Synliggjøre informasjon om datatilbydere, tilgjengelighet, datakvalitet og hvordan ressurser henger sammen.

**Deduksjon:** data.norge.no har også et tydelig mål om å redusere fragmentering ved å samle flere katalogtyper i én nasjonal inngang, selv om dette ikke er formulert eksplisitt som et eget mål i kildene.

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
| Forskning og innovasjonsmiljø | Oppdage relevante dataressurser | Analyse, forskning og nye tjenester | Viderebruk er uttrykkelig støttet i kildene |
| Virksomheter og privat sektor | Finne data for viderebruk | Kommersielle og ikke-kommersielle formål | Fremmes eksplisitt på om-siden |

## Hovedfunksjoner
### Primære funksjoner
- Felles søk på tvers av datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser.
- KI-søk med naturlig språk, med eksplisitt forbehold om at søket kan være ufullstendig og inneholde feil.
- Standard tekstsøk med avanserte filtre.
- Metadata-visning med informasjon om datatilbyder, tilgjengelighet og datakvalitet.
- Oversikt over om data er åpne eller har begrenset tilgang.
- Brukerveiledning for å finne og dele data.
- Datalandsbyen som nettforum for spørsmål, erfaringsdeling og etterspørsel etter data.
- Verktøy og støttefunksjoner som virksomhetsoversikt, Etterspør data, Datajegeren og SPARQL-sandkasse.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonal portal for oppdagelse og vurdering av dataressurser | Drift av virksomhetenes egne datasett, API-er og kildeplattformer |
| Kataloger for datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser | Innholdsansvar for metadata hos hver enkelt virksomhet |
| Veiledning, dokumentasjon og fellesskapsarena | Selve tilgangsbehandlingen til hvert datasett |
| Informasjon om tilgjengelighet, datakvalitet og relasjoner mellom ressurser | Garantier for faktisk datakvalitet i kildesystemene |
| Etterspørsel og dialog gjennom Datalandsbyen | Full intern datastyring i publiserende virksomheter |

## Veikart over kommende funksjonalitet
**Fakta:**
- Produktsiden i Samarbeidsportalen viser egne innganger for `Kostnader`, `Ta i bruk`, `Statistikk`, `Utviklingsplan`, `Teknisk dokumentasjon` og `Driftsmeldinger`.
- Forsiden på data.norge.no fremhever KI-søk som en sentral og aktiv funksjon.

**Ikke offentlig verifisert i denne arbeidsøkten:** Selve innholdet i `Utviklingsplan` og eventuelle tidsfestede roadmap-punkter er ikke hentet ut.

**Deduksjon:** Videreutviklingen er sannsynligvis konsentrert om søkekvalitet, metadataforbedring og støtte til datadeling, men detaljer må bekreftes i utviklingsplanen.

## Forretningsverdi/Verdiforslag
### For datatilbydere
- Øker synlighet og gjenbruk av egne dataressurser gjennom en nasjonal inngang.
- Gjør det enklere å beskrive data i en struktur som er forståelig for andre aktører.

### For datakonsumenter
- Reduserer letetid og gjør det enklere å vurdere om eksisterende data kan brukes.
- Gir mer helhetlig grunnlag for å forstå data gjennom kobling til begreper, modeller og API-er.

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

**Fakta:** Portalen tilbyr søk, kataloger, veiledning, teknisk dokumentasjon og nettforum i samme løsningsområde.

**Ikke offentlig dokumentert i brukte kilder:** Full teknisk plattformbeskrivelse, skyvalg, intern søketeknologi og driftsarkitektur.

## Gjenbruk
**Høy gjenbruksverdi:**
- Én nasjonal inngang reduserer behovet for lokale katalogkopier og parallelle oversikter.
- Metadata om samme ressurs kan brukes av mange ulike datakonsumenter.
- Koblingen mellom datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser styrker gjenbruk på tvers av kontekster.
- Datalandsbyen bidrar til gjenbruk av erfaringer og kunnskap, ikke bare data.

## Støtter arkitekturprinsipper
- **P4 Del og gjenbruk data** - Portalen er direkte innrettet mot oppdagelse og viderebruk av data.
- **P5 Del og gjenbruk løsninger** - data.norge.no fungerer som en felles nasjonal løsning i stedet for mange lokale kataloger.
- **P6 Lag digitale løsninger som støtter samhandling** - Katalogene og veiledningen gir felles oversikt og språk på tvers av virksomheter.
- **P1 Ta utgangspunkt i brukernes behov** - Søk, veiledning og etterspørselsstøtte er tydelig utformet for å hjelpe brukere med å finne data.

## Finansiering
- Samarbeidsportalen viser at produktet har en egen side for `Kostnader`.
- **Ikke offentlig verifisert i denne arbeidsøkten:** Innholdet på kostnadssiden er ikke kontrollert, og offentlig tilgjengelig finansieringsmodell kan derfor ikke beskrives presist her.
- Det er imidlertid dokumentert at Digdir har ansvar for drift og utvikling av nettstedet.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | data.norge.no og Samarbeidsportalen |
| Driftsansvar | Digdir er ansvarlig for drift og utvikling av nettstedet | Om Data.norge.no |
| Budsjettansvar | Ikke offentlig spesifisert i brukte kilder | Kostnadsside finnes, men ikke verifisert |
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
- Lokal fil: `results/Produktbeskrivelser/16-data-norge-no-produkt-canvas.md`
- Lokal fil: `results/Produktbeskrivelser/16-data-norge-no-produkt-canvas-copilot.md`
- Lokal fil: `results/Produktbeskrivelser/16-data-norge-no-produkt-canvas-codex.md`
- Lokal fil: `results/templates/produkt-canvas-template.md`
- Lokal fil: `index/capabilities.yaml`
- Lokal fil: `index/produktnummerering.md`
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
- Utgangspunktet er flyttet fra basisfilen til den sist oppdaterte forbedringsfilen, `16-data-norge-no-produkt-canvas-copilot.md`, slik at vurderingen faktisk bygger videre på siste arbeid.
- Produktmål og produktkontekst er kontrollert mot både data.norge.no og Samarbeidsportalen, ikke bare mot generelle Digdir-lenker.
- Flere detaljerte påstander fra `-copilot`-versjonen er strammet inn eller fjernet fordi de ikke lot seg verifisere offentlig i brukte kilder, blant annet konkrete kostnadsestimater, Azure-hosting, spesifikk søketeknologi, EU-finansiering, oppetidsnivå og detaljerte roadmap-punkter.
- Samarbeidsportalen-lenkene for `Dette er Felles datakatalog` og `data.norge.no` er brukt som mer presise kilder enn den generelle `datadeling/2480`-lenken.

### Tekstlige forbedringer
- Innholdet er beholdt relativt omfattende, men gjort mer presist og mindre spekulativt enn forrige versjon.
- Kapabiliteter, mål, funksjoner og forvaltning er koblet tydeligere til dokumenterte kilder.
- Usikkerhet er flyttet fra implisitte antakelser til eksplisitte formuleringer der offentlig dokumentasjon mangler.
