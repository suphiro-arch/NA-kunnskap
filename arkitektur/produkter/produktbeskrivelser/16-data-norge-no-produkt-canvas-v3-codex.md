# Produkt-canvas: data.norge.no

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
data.norge.no

## Ressurs ID
16 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon.

**Fakta:** data.norge.no beskriver seg som Norges offisielle portal for deling av data fra offentlige og private virksomheter. Forsiden viser aktiv drift med KI-søk og innhold fra over 125 virksomheter og over 8000 datasett (hentet 2026-03-10).

## Modenhet
Høy funksjonell modenhet, med noen forvaltningsmessige avhengigheter:
- Etablert nasjonal portal med egne kataloger for datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser.
- Egen brukerveiledning, teknisk dokumentasjon og nettforum for brukere og datatilbydere.
- Drift og utvikling ligger hos Digitaliseringsdirektoratet, mens virksomhetene selv er ansvarlige for innholdet i katalogene.

**Deduksjon:** Løsningen fremstår som moden som felles inngang og oppdagbarhetsportal, men kvaliteten i kataloginnholdet vil variere med virksomhetenes publiserings- og vedlikeholdsevne.

## Kort beskrivelse
data.norge.no er den nasjonale portalen for å finne, forstå og ta i bruk dataressurser i offentlig sektor. Løsningen samler metadata om datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser, og hjelper datakonsumenter med å vurdere tilgjengelighet, datakvalitet og sammenhenger mellom ressursene.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over datasett**
  Portalen gjør datasett søkbare og sammenlignbare på tvers av virksomheter.
- **Informasjonsforvaltning: Oversikt over API**
  API-er synliggjøres som del av samme nasjonale katalogstruktur.
- **Informasjonsforvaltning: Oversikt over begreper**
  Begreper publiseres og kobles til dataressurser for å styrke felles forståelse.
- **Informasjonsforvaltning: Oversikt over informasjonsmodeller**
  Informasjonsmodeller beskrives som egne ressurser og kan brukes for semantisk avklaring.
- **Informasjonsforvaltning: Oversikt over tjenester**
  Tjenester som tilbys av eller på vegne av offentlig sektor inngår i katalogbildet.
- **Informasjonsforvaltning: Oversikt over hendelser**
  Hendelser eksponeres som egne ressurser som kan støtte samhandling og videre automatisering.
- **Datautveksling og integrasjon: Dele data med andre**
  Datatilbydere får en nasjonal kanal for å publisere metadata om delbare ressurser.
- **Datautveksling og integrasjon: Bruke data fra andre**
  Datakonsumenter får ett sted å oppdage og vurdere relevante dataressurser.
- **Standardisering: Forvaltningsstandarder**
  Portalen forutsetter strukturert og standardisert beskrivelse av ressurser for å sikre gjenfinning og samhandling.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert opp mot dokumenterte funksjoner på data.norge.no.

## Produktmål
**Primærkilde:** `Om Data.norge.no` på data.norge.no.

Dokumenterte mål:
- Gi oversikt over hvilke data offentlig sektor har og kan dele.
- Gi datakonsumenter enklere tilgang til dataressurser.
- Fremme viderebruk av data for både kommersielle og ikke-kommersielle formål.
- Hjelpe brukere med å oppdage, vurdere og ta i bruk data.

Operasjonelle mål utledet fra samme kilde og brukerveiledningen:
- Gjøre søk på tvers av datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser enklere.
- Synliggjøre informasjon om datatilbyder, tilgjengelighet, datakvalitet og tilgangsnivå.
- Støtte både datatilbydere og datakonsumenter med veiledning, nettforum og etterspørsel etter data.

**Usikkert:** Samarbeidsportalen for Felles datakatalog var midlertidig utilgjengelig (502) ved henting 2026-03-10, så produktmål er ikke kontrollert mot den kilden i denne arbeidsøkten.

## Brukerbehov
- Datakonsumenter trenger ett sted å finne relevante data uten å lete gjennom mange separate nettsteder.
- Datatilbydere trenger en nasjonal kanal for å gjøre egne dataressurser oppdagbare.
- Arkitekter og informasjonsforvaltere trenger oversikt over begreper, modeller, API-er og relasjoner mellom ressursene.
- Brukere trenger tydelig informasjon om data er åpne, begrensede eller beskyttede, og hvordan tilgang oppnås.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Typisk bruk |
|---|---|---|
| Offentlige datatilbydere | Publisere og vedlikeholde metadata | Datasett, API-er, begreper og modeller |
| Utviklere og integrasjonsteam | Finne data og API-er raskt | Integrasjon, analyse og tjenesteutvikling |
| Arkitekter og informasjonsforvaltere | Felles oversikt og semantisk avklaring | Kartlegging, gjenbruk, styring |
| Forskning og innovasjonsmiljø | Oppdage relevante dataressurser | Analyse, forskning og nye tjenester |
| Virksomheter og privat sektor | Vurdere viderebruk av offentlige data | Kommersiell og ikke-kommersiell bruk |

## Hovedfunksjoner
- Felles søk på tvers av datasett, API-er, begreper, informasjonsmodeller, tjenester og hendelser.
- KI-søk med naturlig språk, med eksplisitt forbehold om at treff kan være ufullstendige eller feil.
- Standard tekstsøk med avanserte filtre.
- Visning av metadata om datatilbyder, tilgjengelighet, datakvalitet og tilgangsnivå.
- Brukerveiledning for å finne og dele data.
- Nettforumet Datalandsbyen for spørsmål, etterspørsel og erfaringsdeling.
- Verktøy og hjelpefunksjoner som virksomhetsoversikt, etterspør data, Datajegeren og SPARQL-sandkasse.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonal katalog- og søkeportal for metadata | Drift av virksomhetenes egne datasett, API-er og kildeplattformer |
| Veiledning for å finne og dele data | Innholdsansvar for metadata hos hver enkelt virksomhet |
| Oppdagbarhet på tvers av flere katalogtyper | Garanti for faktisk datakvalitet i kildene |
| Informasjon om tilgang, åpenhet og relasjoner | Selve tilgangsbehandlingen til hvert datasett |
| Nettforum og støtte for etterspørsel etter data | Full intern datastyring i publiserende virksomheter |

## Veikart over kommende funksjonalitet
**Fakta:** Tilgjengelige kilder i denne arbeidsøkten viser eksisterende funksjoner som KI-søk, standard søk, flere katalogtyper, brukerveiledning og fellesskapsforum.

**Ikke offentlig dokumentert i tilgjengelige kilder:** Et detaljert offentlig veikart med tidsfestede leveranser.

**Deduksjon:** Gitt at portalen allerede fremhever KI-søk, metadatakvalitet og hjelp til deling, er det sannsynlig at videreutvikling prioriterer søkekvalitet, metadataforbedring og støtte til datadeling fremfor helt nye produktområder.

## Forretningsverdi/Verdiforslag
- **For datakonsumenter:** Reduserer letetid og gjør det enklere å vurdere om eksisterende data kan gjenbrukes.
- **For datatilbydere:** Øker synlighet og gjenbruk av egne dataressurser gjennom en nasjonal inngang.
- **For Digdir og offentlig sektor:** Understøtter datadeling som felles praksis i stedet for mange parallelle kataloger.
- **For samfunnet:** Fremmer viderebruk av data for forskning, innovasjon og nye tjenester.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil eller ufullstendig informasjon om tilgang og bruksvilkår kan gi feil viderebruk | Tydelige metadatafelter, kvalitetssikring og veiledning til datatilbydere |
| Teknisk | Ujevn metadata-kvalitet og brutte lenker reduserer søke- og gjenfinningsverdi | Validering, vedlikeholdsrutiner og oppfølging av datatilbydere |
| Sikkerhet | Feil klassifisering av beskyttede eller begrensede ressurser kan gi uønsket eksponering | Klare publiseringsregler, kontroll av metadata og sikkerhetsvurderinger |
| Leverandør/forvaltning | Portalen er avhengig av at mange virksomheter holder eget innhold oppdatert | Felles forvaltningsregime, veiledning og oppfølging fra Digdir |
| Brukeropplevelse | KI-søk kan gi ufullstendige eller feil svar, og brukere kan overvurdere treffkvaliteten | Tydelig brukerkommunikasjon, standard søk som alternativ og veiledning |

## Kanaler
- Portal og søk: https://data.norge.no/
- Om løsningen: https://data.norge.no/nb/about
- Brukerveiledning: https://data.norge.no/nb/docs
- Nettforum / Datalandsbyen: https://data.norge.no/nb/docs/community

## Plattform
Nasjonal webportal for oppdagelse, metadataforvaltning og veiledning knyttet til datadeling.

**Fakta:** Portalen tilbyr søk, flere katalogtyper, veiledning og nettforum som del av samme brukerflate.

**Ikke offentlig dokumentert i tilgjengelige kilder:** Full teknisk plattformbeskrivelse, skyvalg og detaljert arkitektur.

## Gjenbruk
Høy gjenbruksverdi:
- Én nasjonal inngang reduserer behovet for lokale kopier av katalogoversikter.
- Samme metadata kan gjenbrukes av mange datakonsumenter, ikke bare én målgruppe.
- Begreper, API-er, modeller og datasett kan sees i sammenheng og støtte videre gjenbruk i andre løsninger.

## Støtte arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Portalen er direkte innrettet mot oppdagelse og viderebruk av data.
- **P5: Del og gjenbruk løsninger**
  data.norge.no fungerer som en felles nasjonal løsning i stedet for mange lokale kataloger.
- **P6: Lag digitale løsninger som støtter samhandling**
  Katalogene og veiledningen gir felles begreper og oversikt som støtter samhandling på tvers.
- **P1: Ta utgangspunkt i brukernes behov**
  Søke- og veiledningsfunksjonene er utformet for å gjøre det enklere å finne og bruke relevante data.

## Finansiering
- Drift og utvikling ligger hos Digitaliseringsdirektoratet.
- **Ikke offentlig dokumentert i tilgjengelige kilder:** Presis finansieringsmodell, budsjettfordeling og eventuelle kostnadskomponenter per delprodukt.

## Forvaltning/eier
| Ansvarsområde | Vurdering |
|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) |
| Driftsansvar | Digdir er ansvarlig for drift og utvikling av nettstedet |
| Budsjettansvar | Antatt Digdir, men ikke offentlig spesifisert i tilgjengelige kilder |
| Styringsmodell | Digdir forvalter løsningen, mens virksomhetene selv forvalter eget kataloginnhold |

## Lenke til dokumentasjon
- https://data.norge.no/
- https://data.norge.no/nb/about
- https://data.norge.no/nb/docs
- https://data.norge.no/nb/docs/community
- https://www.digdir.no/felles-datakatalog/om-felles-datakatalog/2274
- https://samarbeid.digdir.no/felles-datakatalog/datadeling/2480

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/produkter/produktbeskrivelser/16-data-norge-no-produkt-canvas.md`
- Lokal fil: `arkitektur/produkter/produktbeskrivelser/16-data-norge-no-produkt-canvas-copilot.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://data.norge.no/ (hentet 2026-03-10)
- Nettkilde: https://data.norge.no/nb/about (hentet 2026-03-10)
- Nettkilde: https://data.norge.no/nb/docs (hentet 2026-03-10)
- Nettkilde: https://data.norge.no/nb/docs/community (hentet 2026-03-10)
- Nettkilde fra `sources/links.md`: https://www.digdir.no/felles-datakatalog/om-felles-datakatalog/2274 svarte `502` ved henting 2026-03-10
- Nettkilde fra `sources/links.md`: https://samarbeid.digdir.no/felles-datakatalog/datadeling/2480 svarte `502` ved henting 2026-03-10

---

## Endringer fra tidligere versjoner

### Analyseforbedringer
- Produktbeskrivelsen er oppdatert med konkrete fakta fra data.norge.no om formål, katalogtyper, søkefunksjoner, innholdsansvar og driftsansvar.
- Det er lagt inn verifiserte opplysninger om omfanget på forsiden: over 125 virksomheter og over 8000 datasett.
- Risiko er justert basert på dokumenterte forhold i løsningen, blant annet at KI-søk kan være ufullstendig eller feil, og at virksomhetene selv er ansvarlige for innholdet.
- Digdir- og Samarbeidsportalen-lenkene fra `sources/links.md` er forsøkt brukt som primærkilder, men er markert som midlertidig utilgjengelige i denne arbeidsøkten.

### Tekstlige forbedringer
- Innholdet er strammet opp med tydeligere skille mellom fakta, deduksjon og usikkerhet.
- Produktmål, brukerbehov, hovedfunksjoner og forvaltning er gjort mer konkrete og sporbare.
- Risiko, brukersegmenter og avgrensninger er strukturert i tabeller for bedre sammenlignbarhet med andre produkt-canvas-filer.
