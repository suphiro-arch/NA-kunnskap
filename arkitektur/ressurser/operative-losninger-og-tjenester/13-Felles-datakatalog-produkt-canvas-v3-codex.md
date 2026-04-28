# Produkt-canvas: Felles datakatalog

## Navn
Felles datakatalog

## Ressurs ID
DIGDIR-011

## Status/Livsfase
**Produksjon** - etablert nasjonal fellesløsning for å beskrive, publisere, høste og synliggjøre metadata om dataressurser.

**Fakta:** Digdir beskriver Felles datakatalog som oversikten over hvilke data virksomheter har, hvordan de henger sammen og hva de betyr. Samarbeidsportalen beskriver løsningen som laget for å vise hvilke data virksomheter har som de kan dele med andre, og forklarer at virksomheter enten kan registrere metadata selv eller gjøre dem tilgjengelige for høsting.

## Modenhet
**Høy modenhet** - innarbeidet og tydelig forvaltet nasjonal fellesløsning:
- Produktet er etablert som nasjonal løsning for oppdagelse og beskrivelse av dataressurser.
- Digdir publiserer både produktside, ta-i-bruk-løp og støtteinnhold for virksomheter som skal registrere eller høste metadata.
- Løsningen er tett koblet til data.norge.no som synlig brukerflate, men Felles datakatalog er bredere enn bare selve portalen.
- Produktområdet omfatter flere delkataloger og standardisert metadataforvaltning, ikke bare søk i ett nettsted.

**Deduksjon:** Modenheten er høy fordi produktet både er operativt i bruk og har fått en tydelig rolle i den nasjonale datadelingsmodellen. Samtidig er nytteverdien avhengig av at virksomheter faktisk publiserer og vedlikeholder metadata.

## Kort beskrivelse
Felles datakatalog er den nasjonale fellesløsningen for å beskrive og synliggjøre dataressurser på en standardisert måte. Produktet gjør det mulig å registrere eller høste metadata om datasett, API-er, begreper og informasjonsmodeller, og å gjøre disse ressursene søkbare og forståelige på tvers av virksomheter. data.norge.no er den viktigste brukerflaten for å oppdage innholdet, men Felles datakatalog er bredere enn portalen: det er et samlet produktområde for metadataforvaltning, publisering og gjenfinning av dataressurser.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over API** gjør maskinelle grensesnitt synlige som del av en felles nasjonal oversikt over tilgjengelige dataressurser.
- **Informasjonsforvaltning: Oversikt over begreper** kobler dataressurser til begrepsbeskrivelser og styrker felles forståelse av hva data betyr.
- **Informasjonsforvaltning: Oversikt over datasett** er en kjernefunksjon ved at datasett beskrives, publiseres og gjøres søkbare på tvers av virksomheter.
- **Informasjonsforvaltning: Oversikt over informasjonsmodeller** gjør det mulig å synliggjøre modeller som forklarer struktur og sammenheng i dataene.
- **Standardisering: Forvaltningsstandarder** bygger på standardiserte metadataformater og felles publiseringspraksis som gjør innholdet sammenlignbart og høstbart.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Digdir-sidene for Felles datakatalog, Samarbeidsportalen og data.norge.no.

## Produktmål
**Primærkilder:** Digdir-siden for Felles datakatalog, Samarbeidsportalen og Digdirs kravside for registrering av datasett.

Dokumenterte mål:
- Gi oversikt over hvilke data virksomheter har, hvordan de henger sammen og hva de betyr.
- Gjøre det mulig å oppdage, vurdere og få tilgang til data.
- Legge til rette for at virksomheter kan registrere eller høste metadata i en felles nasjonal løsning.

Operative mål utledet fra de samme kildene:
- Redusere fragmentering ved å samle metadata om flere typer dataressurser i samme produktområde.
- Gjøre det enklere for datakonsumenter å finne relevante data uten å starte i hver enkelt virksomhet.
- Styrke datadeling gjennom felles definisjoner, publiseringsmønstre og metadata som kan brukes på tvers.

## Brukerbehov
- Datatilbydere trenger en felles løsning for å registrere eller høste metadata om egne dataressurser.
- Datakonsumenter trenger ett sted å oppdage og vurdere hvilke data som finnes og hvordan de kan tas i bruk.
- Arkitekter og informasjonsforvaltere trenger oversikt over sammenhengen mellom datasett, API-er, begreper og modeller.
- Forvaltningsmiljøer trenger et produktområde som støtter felles metadata-standarder og mer enhetlig praksis for datadeling.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter som datatilbydere | Registrere eller høste metadata | Synliggjøre datasett, API-er, begreper og modeller | Primærbruker på publiseringssiden |
| Utviklere og datakonsumenter | Finne og vurdere relevante dataressurser | Integrasjon, analyse og tjenesteutvikling | Møter ofte produktet via data.norge.no |
| Arkitekter og informasjonsforvaltere | Felles oversikt og semantisk sammenheng | Informasjonsforvaltning, styring og gjenbruk | Har behov for delkatalogene i sammenheng |
| Digdir og forvaltningsmiljøer | Forvalte standarder, innføring og veiledning | Videreutvikling, høsting og kvalitet i metadata | Bærer produktansvaret |
| Privat sektor og forskningsmiljøer | Oppdage offentlige dataressurser | Viderebruk, innovasjon og analyse | Viktige brukere av den synlige katalogflaten |

## Hovedfunksjoner
### Primære funksjoner
**Registrering og høsting av metadata.** Produktet gjør det mulig for virksomheter å beskrive egne dataressurser enten ved å registrere metadata direkte eller ved å gjøre dem tilgjengelige for høsting. Dette er viktig fordi Felles datakatalog ikke primært lagrer selve dataene, men beskriver ressursene slik at andre kan finne og forstå dem.

**Samlet oversikt over flere typer dataressurser.** Felles datakatalog omfatter ikke bare datasett, men også API-er, begreper og informasjonsmodeller. Digdir beskriver også tjeneste- og hendelseskatalog som del av produktområdet, men den mest etablerte kjernen er katalogene for datasett, API-er, begreper og modeller. Produktet fungerer derfor som en overbygning for flere delkataloger, ikke som én smal katalogfunksjon.

**Synliggjøring og oppdagelse gjennom felles brukerflater.** Innholdet publiseres og synliggjøres blant annet på data.norge.no, som er den viktigste inngangen for søk og oppdagelse. Dette gjør at Felles datakatalog har både en publiseringsflate for datatilbydere og en oppdagelsesflate for datakonsumenter, selv om den synlige portalen er skilt ut som eget produkt i registeret.

**Standardisert metadataforvaltning og felles forståelse.** Produktets verdi ligger også i at metadata beskrives på en ensartet måte. Det gjør ressursene lettere å sammenligne, høste og bruke videre, og det gir en felles ramme for hvordan offentlig sektor kan beskrive hvilke data som finnes og hvordan de henger sammen.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Registrering og høsting av metadata om dataressurser | Lagring og forvaltning av de underliggende kildedataene |
| Delkataloger for datasett, API-er, begreper og informasjonsmodeller | Selve tilgangsbehandlingen til hvert datasett eller API |
| Synliggjøring av metadata gjennom felles katalogflater | Full intern datastyring i hver virksomhet |
| Standardisert publisering og beskrivelse av dataressurser | Lokal faglig kvalitetssikring av hvert enkelt datasett |
| Overordnet produktområde som data.norge.no bygger på | data.norge.no som egen portalressurs |
### Typiske brukssituasjoner (generisk)
- Virksomhet vil registrere sine dataressurser og gjøre dem oppdagbare for datakonsumenter på tvers av offentlig sektor.
- Prosjekt eller sektorsatsing skal dokumentere og publisere datadelingstilbud som del av åpenhetskrav eller digitaliseringsarbeid.
- Datakonsument vil søke på tvers av datasett, API-er og begreper for å finne om relevant informasjon allerede er tilgjengelig.

### Når Felles datakatalog normalt ikke er førstevalg
- Når behovet er selve datadelingsmekanismen og tilgangsstyringen – da er Maskinporten eller data.altinn.no mer relevant.
- Når behovet er intern datastyring og forvaltning uten publiseringsplikt.
- Når behovet er å finne og bruke API-er direkte, ikke bare oppdage dem – da er API-ets eget grensesnitt mer relevant.

## Veikart over kommende funksjonalitet
**Fakta fra Digdir og Samarbeidsportalen (kontrollert 2026-03-27):**
- Produktet har aktiv ta-i-bruk-side og løpende publisert støtte for virksomheter som vil registrere eller høste metadata.
- Digdir beskriver tjeneste- og hendelseskatalog som del av produktområdet, noe som tyder på videre utvikling av bredden i katalogene.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et detaljert, tidsfestet veikart er ikke hentet ut fra de brukte kildene.

**Deduksjon:** Videreutviklingen vil trolig handle om bedre metadataflyt, høyere publiseringsgrad, tydeligere sammenheng mellom delkatalogene og fortsatt forbedring av oppdagelse og bruk av dataressurser.

## Forretningsverdi/Verdiforslag
### For datatilbydere
- Gir en nasjonal kanal for å gjøre egne dataressurser synlige.
- Reduserer behovet for lokale katalogoppsett som bare dekker egen virksomhet.
- Støtter mer enhetlig beskrivelse av dataressurser og enklere deling med andre.

### For datakonsumenter
- Gjør det enklere å finne relevante datasett, API-er, begreper og modeller.
- Gir bedre grunnlag for å vurdere om eksisterende data kan brukes videre.
- Reduserer letetid og usikkerhet ved at flere ressurskategorier kan oppdages i samme produktområde.

### For offentlig sektor
- Understøtter datadeling som nasjonal praksis i stedet for mange separate katalogløp.
- Styrker gjenbruk av både metadata, begreper og publiseringsmønstre.
- Bidrar til bedre felles forståelse av hva data er, hvor de finnes og hvordan de kan brukes.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Ufullstendige eller utdaterte metadata svekker nytteverdien av katalogen | Veiledning, standarder og bedre publiseringsrutiner hos datatilbydere |
| Organisatorisk | Lav deltakelse eller svak oppfølging fra virksomhetene gir mangelfull nasjonal oversikt | Innføringsstøtte, krav/anbefalinger og forankring i styring |
| Semantisk | Uklare begreper og modeller gjør ressursene vanskeligere å forstå og sammenligne | Kobling til begrepskatalog, modeller og felles definisjoner |
| Teknisk | Svikt i høsting eller publiseringsflyt kan gi brutte eller ufullstendige metadata | Stabil integrasjonsforvaltning og oppfølging av publiseringskanaler |
| Brukeropplevelse | Datakonsumenter kan forveksle katalog med faktisk datatilgang eller tro at metadata er selve tjenesten | Tydelig avgrensning mellom katalog, portal og underliggende datakilder |

## Kanaler
- Produktside hos Digdir: https://www.digdir.no/felleslosninger/felles-datakatalog/790
- Samarbeidsportalen, oversikt: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616
- Samarbeidsportalen, ta i bruk: https://samarbeid.digdir.no/felles-datakatalog/ta-i-bruk-felles-datakatalog/1619
- data.norge.no: https://data.norge.no/
- data.norge.no, om løsningen: https://data.norge.no/nb/about
- Krav/anbefaling om registrering av datasett: https://www.digdir.no/krav-og-anbefalinger/registrer-datasett-i-felles-datakatalog/3088

## Plattform
Felles datakatalog er en nasjonal metadata- og publiseringsløsning for dataressurser, med både publiseringsløp for virksomheter og oppdagelsesflater for brukere.

**Fakta:** Samarbeidsportalen beskriver både registrering og høsting som arbeidsmåter. Digdir beskriver katalogen som en overordnet løsning for å vise hvilke data virksomheter har, hvordan de henger sammen og hva de betyr.

**Ikke offentlig dokumentert i brukte kilder:** Full teknisk plattformbeskrivelse, detaljert runtime-arkitektur og komplett komponentkart for alle delkatalogene.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er laget for å være en felles nasjonal løsning som mange virksomheter publiserer inn i og mange brukere finner innhold gjennom.
- Det er særlig relevant når behovet er å gjøre dataressurser synlige og forståelige, ikke å levere selve datatilgangen.
- Det har høy verdi som overordnet fellesløsning fordi det binder sammen flere delkataloger i samme produktområde.


### Vanlige kombinasjoner med andre produkter
- **data.norge.no** – er portalen som synliggjør innholdet i Felles datakatalog for søk og oppdagelse.
- **Begrepskatalog og API-katalog** – er spesialiserte delkataloger under Felles datakatalog.
- **Maskinporten** – API-er som er beskrevet i katalogen er gjerne beskyttet av Maskinporten.
- **data.altinn.no** – tilbyr kontrollert datadeling for de dataressursene som er dokumentert i katalogen.

**Kildekode:** Åpen kildekode. Lisens: Apache-2.0. Kildekode: [github.com/Informasjonsforvaltning](https://github.com/Informasjonsforvaltning).

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at dataressurser blir synlige og vurderbare for viderebruk.
- **P5: Del og gjenbruk løsninger** styrkes ved at offentlig sektor kan bruke én felles katalogløsning i stedet for mange parallelle oversikter.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi metadata, begreper og modeller blir beskrevet på en måte som kan brukes av mange aktører.
- **P7: Sørg for tillit til oppgaveløsningen** støttes indirekte gjennom mer standardisert og sporbar beskrivelse av dataressurser, men produktet er ikke i seg selv en autorisasjons- eller sikkerhetstjeneste.

## Finansiering
- **Fakta:** Digdir oppgir at etablering og bruk er gratis på produktsiden for Felles datakatalog.
- **Fakta:** Offentlig detaljert finansieringsmodell utover dette er ikke hentet ut i denne arbeidsøkten.
- **Deduksjon:** Finansieringen ser ut til å være sentralt forankret hos Digdir, mens virksomhetene må dekke egne kostnader ved å beskrive, publisere og vedlikeholde metadata i egne prosesser.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Digdir og Samarbeidsportalen |
| Drifts- og forvaltningsansvar | Digdir forvalter løsningen og ta-i-bruk-løpet | Digdir og Samarbeidsportalen |
| Budsjett- og kostnadsmodell | Digdir oppgir gratis etablering og bruk, men detaljert modell er ikke verifisert her | Digdir |
| Styringsmodell | Del av Digdirs arbeid med informasjonsforvaltning og datadeling | Digdir og Samarbeidsportalen |

## Lenke til dokumentasjon
- https://www.digdir.no/felleslosninger/felles-datakatalog/790
- https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616
- https://samarbeid.digdir.no/felles-datakatalog/ta-i-bruk-felles-datakatalog/1619
- https://data.norge.no/
- https://data.norge.no/nb/about
- https://www.digdir.no/krav-og-anbefalinger/registrer-datasett-i-felles-datakatalog/3088

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/13-Felles-datakatalog-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.digdir.no/felleslosninger/felles-datakatalog/790 (kontrollert 2026-03-27)
- Nettkilde: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616 (kontrollert 2026-03-27)
- Nettkilde: https://samarbeid.digdir.no/felles-datakatalog/ta-i-bruk-felles-datakatalog/1619 (kontrollert 2026-03-27)
- Nettkilde: https://data.norge.no/nb/about (kontrollert 2026-03-27)
- Nettkilde: https://www.digdir.no/krav-og-anbefalinger/registrer-datasett-i-felles-datakatalog/3088 (kontrollert 2026-03-27)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen bygger nå på oppdatert Digdir-kildegrunnlag og nyere sider i Samarbeidsportalen, ikke på spekulative antakelser om teknologi, veikart og finansiering.
- Produktet er avklart som en overordnet metadata- og publiseringsløsning, tydelig skilt fra `data.norge.no` som portal og fra delkatalogene under samme område.
- Uverifiserte påstander om kostnader, søketeknologi, AI-planer og estimert samfunnsgevinst er tatt ut.

### Tekstlige forbedringer
- Dokumentet starter ikke lenger med målgruppelinje, og språket er strammet inn mot nasjonal arkitektur og gjenbruksvurdering.
- `Hovedfunksjoner` beskriver nå hele løsningsbredden, inkludert registrering, høsting, delkataloger og synlig brukerflate.
- Scope og avgrensning gjør det tydeligere hva Felles datakatalog er, og hva som hører hjemme i data.norge.no eller i de underliggende kildesystemene.


