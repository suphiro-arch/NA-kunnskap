# Produkt-canvas: Felles datakatalog

## Navn
Felles datakatalog

## Ressurs ID
DIGDIR-011

## Status/Livsfase
**Produksjon** - etablert nasjonal felleslÃ¸sning for Ã¥ beskrive, publisere, hÃ¸ste og synliggjÃ¸re metadata om dataressurser.

**Fakta:** Digdir beskriver Felles datakatalog som oversikten over hvilke data virksomheter har, hvordan de henger sammen og hva de betyr. Samarbeidsportalen beskriver lÃ¸sningen som laget for Ã¥ vise hvilke data virksomheter har som de kan dele med andre, og forklarer at virksomheter enten kan registrere metadata selv eller gjÃ¸re dem tilgjengelige for hÃ¸sting.

## Modenhet
**HÃ¸y modenhet** - innarbeidet og tydelig forvaltet nasjonal felleslÃ¸sning:
- Produktet er etablert som nasjonal lÃ¸sning for oppdagelse og beskrivelse av dataressurser.
- Digdir publiserer bÃ¥de produktside, ta-i-bruk-lÃ¸p og stÃ¸tteinnhold for virksomheter som skal registrere eller hÃ¸ste metadata.
- LÃ¸sningen er tett koblet til data.norge.no som synlig brukerflate, men Felles datakatalog er bredere enn bare selve portalen.
- ProduktomrÃ¥det omfatter flere delkataloger og standardisert metadataforvaltning, ikke bare sÃ¸k i ett nettsted.

**Deduksjon:** Modenheten er hÃ¸y fordi produktet bÃ¥de er operativt i bruk og har fÃ¥tt en tydelig rolle i den nasjonale datadelingsmodellen. Samtidig er nytteverdien avhengig av at virksomheter faktisk publiserer og vedlikeholder metadata.

## Kort beskrivelse
Felles datakatalog er den nasjonale felleslÃ¸sningen for Ã¥ beskrive og synliggjÃ¸re dataressurser pÃ¥ en standardisert mÃ¥te. Produktet gjÃ¸r det mulig Ã¥ registrere eller hÃ¸ste metadata om datasett, API-er, begreper og informasjonsmodeller, og Ã¥ gjÃ¸re disse ressursene sÃ¸kbare og forstÃ¥elige pÃ¥ tvers av virksomheter. data.norge.no er den viktigste brukerflaten for Ã¥ oppdage innholdet, men Felles datakatalog er bredere enn portalen: det er et samlet produktomrÃ¥de for metadataforvaltning, publisering og gjenfinning av dataressurser.

## Kapabiliteter
- **Informasjonsforvaltning: Oversikt over API** gjÃ¸r maskinelle grensesnitt synlige som del av en felles nasjonal oversikt over tilgjengelige dataressurser.
- **Informasjonsforvaltning: Oversikt over begreper** kobler dataressurser til begrepsbeskrivelser og styrker felles forstÃ¥else av hva data betyr.
- **Informasjonsforvaltning: Oversikt over datasett** er en kjernefunksjon ved at datasett beskrives, publiseres og gjÃ¸res sÃ¸kbare pÃ¥ tvers av virksomheter.
- **Informasjonsforvaltning: Oversikt over informasjonsmodeller** gjÃ¸r det mulig Ã¥ synliggjÃ¸re modeller som forklarer struktur og sammenheng i dataene.
- **Standardisering: Forvaltningsstandarder** bygger pÃ¥ standardiserte metadataformater og felles publiseringspraksis som gjÃ¸r innholdet sammenlignbart og hÃ¸stbart.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Digdir-sidene for Felles datakatalog, Samarbeidsportalen og data.norge.no.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Digdir-siden for Felles datakatalog, Samarbeidsportalen og Digdirs kravside for registrering av datasett.

Dokumenterte mÃ¥l:
- Gi oversikt over hvilke data virksomheter har, hvordan de henger sammen og hva de betyr.
- GjÃ¸re det mulig Ã¥ oppdage, vurdere og fÃ¥ tilgang til data.
- Legge til rette for at virksomheter kan registrere eller hÃ¸ste metadata i en felles nasjonal lÃ¸sning.

Operative mÃ¥l utledet fra de samme kildene:
- Redusere fragmentering ved Ã¥ samle metadata om flere typer dataressurser i samme produktomrÃ¥de.
- GjÃ¸re det enklere for datakonsumenter Ã¥ finne relevante data uten Ã¥ starte i hver enkelt virksomhet.
- Styrke datadeling gjennom felles definisjoner, publiseringsmÃ¸nstre og metadata som kan brukes pÃ¥ tvers.

## Brukerbehov
- Datatilbydere trenger en felles lÃ¸sning for Ã¥ registrere eller hÃ¸ste metadata om egne dataressurser.
- Datakonsumenter trenger ett sted Ã¥ oppdage og vurdere hvilke data som finnes og hvordan de kan tas i bruk.
- Arkitekter og informasjonsforvaltere trenger oversikt over sammenhengen mellom datasett, API-er, begreper og modeller.
- ForvaltningsmiljÃ¸er trenger et produktomrÃ¥de som stÃ¸tter felles metadata-standarder og mer enhetlig praksis for datadeling.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige virksomheter som datatilbydere | Registrere eller hÃ¸ste metadata | SynliggjÃ¸re datasett, API-er, begreper og modeller | PrimÃ¦rbruker pÃ¥ publiseringssiden |
| Utviklere og datakonsumenter | Finne og vurdere relevante dataressurser | Integrasjon, analyse og tjenesteutvikling | MÃ¸ter ofte produktet via data.norge.no |
| Arkitekter og informasjonsforvaltere | Felles oversikt og semantisk sammenheng | Informasjonsforvaltning, styring og gjenbruk | Har behov for delkatalogene i sammenheng |
| Digdir og forvaltningsmiljÃ¸er | Forvalte standarder, innfÃ¸ring og veiledning | Videreutvikling, hÃ¸sting og kvalitet i metadata | BÃ¦rer produktansvaret |
| Privat sektor og forskningsmiljÃ¸er | Oppdage offentlige dataressurser | Viderebruk, innovasjon og analyse | Viktige brukere av den synlige katalogflaten |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
**Registrering og hÃ¸sting av metadata.** Produktet gjÃ¸r det mulig for virksomheter Ã¥ beskrive egne dataressurser enten ved Ã¥ registrere metadata direkte eller ved Ã¥ gjÃ¸re dem tilgjengelige for hÃ¸sting. Dette er viktig fordi Felles datakatalog ikke primÃ¦rt lagrer selve dataene, men beskriver ressursene slik at andre kan finne og forstÃ¥ dem.

**Samlet oversikt over flere typer dataressurser.** Felles datakatalog omfatter ikke bare datasett, men ogsÃ¥ API-er, begreper og informasjonsmodeller. Digdir beskriver ogsÃ¥ tjeneste- og hendelseskatalog som del av produktomrÃ¥det, men den mest etablerte kjernen er katalogene for datasett, API-er, begreper og modeller. Produktet fungerer derfor som en overbygning for flere delkataloger, ikke som Ã©n smal katalogfunksjon.

**SynliggjÃ¸ring og oppdagelse gjennom felles brukerflater.** Innholdet publiseres og synliggjÃ¸res blant annet pÃ¥ data.norge.no, som er den viktigste inngangen for sÃ¸k og oppdagelse. Dette gjÃ¸r at Felles datakatalog har bÃ¥de en publiseringsflate for datatilbydere og en oppdagelsesflate for datakonsumenter, selv om den synlige portalen er skilt ut som eget produkt i registeret.

**Standardisert metadataforvaltning og felles forstÃ¥else.** Produktets verdi ligger ogsÃ¥ i at metadata beskrives pÃ¥ en ensartet mÃ¥te. Det gjÃ¸r ressursene lettere Ã¥ sammenligne, hÃ¸ste og bruke videre, og det gir en felles ramme for hvordan offentlig sektor kan beskrive hvilke data som finnes og hvordan de henger sammen.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Registrering og hÃ¸sting av metadata om dataressurser | Lagring og forvaltning av de underliggende kildedataene |
| Delkataloger for datasett, API-er, begreper og informasjonsmodeller | Selve tilgangsbehandlingen til hvert datasett eller API |
| SynliggjÃ¸ring av metadata gjennom felles katalogflater | Full intern datastyring i hver virksomhet |
| Standardisert publisering og beskrivelse av dataressurser | Lokal faglig kvalitetssikring av hvert enkelt datasett |
| Overordnet produktomrÃ¥de som data.norge.no bygger pÃ¥ | data.norge.no som egen portalressurs |

## Veikart over kommende funksjonalitet
**Fakta fra Digdir og Samarbeidsportalen (kontrollert 2026-03-27):**
- Produktet har aktiv ta-i-bruk-side og lÃ¸pende publisert stÃ¸tte for virksomheter som vil registrere eller hÃ¸ste metadata.
- Digdir beskriver tjeneste- og hendelseskatalog som del av produktomrÃ¥det, noe som tyder pÃ¥ videre utvikling av bredden i katalogene.

**Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Et detaljert, tidsfestet veikart er ikke hentet ut fra de brukte kildene.

**Deduksjon:** Videreutviklingen vil trolig handle om bedre metadataflyt, hÃ¸yere publiseringsgrad, tydeligere sammenheng mellom delkatalogene og fortsatt forbedring av oppdagelse og bruk av dataressurser.

## Forretningsverdi/Verdiforslag
### For datatilbydere
- Gir en nasjonal kanal for Ã¥ gjÃ¸re egne dataressurser synlige.
- Reduserer behovet for lokale katalogoppsett som bare dekker egen virksomhet.
- StÃ¸tter mer enhetlig beskrivelse av dataressurser og enklere deling med andre.

### For datakonsumenter
- GjÃ¸r det enklere Ã¥ finne relevante datasett, API-er, begreper og modeller.
- Gir bedre grunnlag for Ã¥ vurdere om eksisterende data kan brukes videre.
- Reduserer letetid og usikkerhet ved at flere ressurskategorier kan oppdages i samme produktomrÃ¥de.

### For offentlig sektor
- UnderstÃ¸tter datadeling som nasjonal praksis i stedet for mange separate kataloglÃ¸p.
- Styrker gjenbruk av bÃ¥de metadata, begreper og publiseringsmÃ¸nstre.
- Bidrar til bedre felles forstÃ¥else av hva data er, hvor de finnes og hvordan de kan brukes.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Datakvalitet | Ufullstendige eller utdaterte metadata svekker nytteverdien av katalogen | Veiledning, standarder og bedre publiseringsrutiner hos datatilbydere |
| Organisatorisk | Lav deltakelse eller svak oppfÃ¸lging fra virksomhetene gir mangelfull nasjonal oversikt | InnfÃ¸ringsstÃ¸tte, krav/anbefalinger og forankring i styring |
| Semantisk | Uklare begreper og modeller gjÃ¸r ressursene vanskeligere Ã¥ forstÃ¥ og sammenligne | Kobling til begrepskatalog, modeller og felles definisjoner |
| Teknisk | Svikt i hÃ¸sting eller publiseringsflyt kan gi brutte eller ufullstendige metadata | Stabil integrasjonsforvaltning og oppfÃ¸lging av publiseringskanaler |
| Brukeropplevelse | Datakonsumenter kan forveksle katalog med faktisk datatilgang eller tro at metadata er selve tjenesten | Tydelig avgrensning mellom katalog, portal og underliggende datakilder |

## Kanaler
- Produktside hos Digdir: https://www.digdir.no/felleslosninger/felles-datakatalog/790
- Samarbeidsportalen, oversikt: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616
- Samarbeidsportalen, ta i bruk: https://samarbeid.digdir.no/felles-datakatalog/ta-i-bruk-felles-datakatalog/1619
- data.norge.no: https://data.norge.no/
- data.norge.no, om lÃ¸sningen: https://data.norge.no/nb/about
- Krav/anbefaling om registrering av datasett: https://www.digdir.no/krav-og-anbefalinger/registrer-datasett-i-felles-datakatalog/3088

## Plattform
Felles datakatalog er en nasjonal metadata- og publiseringslÃ¸sning for dataressurser, med bÃ¥de publiseringslÃ¸p for virksomheter og oppdagelsesflater for brukere.

**Fakta:** Samarbeidsportalen beskriver bÃ¥de registrering og hÃ¸sting som arbeidsmÃ¥ter. Digdir beskriver katalogen som en overordnet lÃ¸sning for Ã¥ vise hvilke data virksomheter har, hvordan de henger sammen og hva de betyr.

**Ikke offentlig dokumentert i brukte kilder:** Full teknisk plattformbeskrivelse, detaljert runtime-arkitektur og komplett komponentkart for alle delkatalogene.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet er laget for Ã¥ vÃ¦re en felles nasjonal lÃ¸sning som mange virksomheter publiserer inn i og mange brukere finner innhold gjennom.
- Det er sÃ¦rlig relevant nÃ¥r behovet er Ã¥ gjÃ¸re dataressurser synlige og forstÃ¥elige, ikke Ã¥ levere selve datatilgangen.
- Det har hÃ¸y verdi som overordnet felleslÃ¸sning fordi det binder sammen flere delkataloger i samme produktomrÃ¥de.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at dataressurser blir synlige og vurderbare for viderebruk.
- **P5: Del og gjenbruk lÃ¸sninger** styrkes ved at offentlig sektor kan bruke Ã©n felles kataloglÃ¸sning i stedet for mange parallelle oversikter.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** stÃ¸ttes fordi metadata, begreper og modeller blir beskrevet pÃ¥ en mÃ¥te som kan brukes av mange aktÃ¸rer.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** stÃ¸ttes indirekte gjennom mer standardisert og sporbar beskrivelse av dataressurser, men produktet er ikke i seg selv en autorisasjons- eller sikkerhetstjeneste.

## Finansiering
- **Fakta:** Digdir oppgir at etablering og bruk er gratis pÃ¥ produktsiden for Felles datakatalog.
- **Fakta:** Offentlig detaljert finansieringsmodell utover dette er ikke hentet ut i denne arbeidsÃ¸kten.
- **Deduksjon:** Finansieringen ser ut til Ã¥ vÃ¦re sentralt forankret hos Digdir, mens virksomhetene mÃ¥ dekke egne kostnader ved Ã¥ beskrive, publisere og vedlikeholde metadata i egne prosesser.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Digdir og Samarbeidsportalen |
| Drifts- og forvaltningsansvar | Digdir forvalter lÃ¸sningen og ta-i-bruk-lÃ¸pet | Digdir og Samarbeidsportalen |
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
- Beskrivelsen bygger nÃ¥ pÃ¥ oppdatert Digdir-kildegrunnlag og nyere sider i Samarbeidsportalen, ikke pÃ¥ spekulative antakelser om teknologi, veikart og finansiering.
- Produktet er avklart som en overordnet metadata- og publiseringslÃ¸sning, tydelig skilt fra `data.norge.no` som portal og fra delkatalogene under samme omrÃ¥de.
- Uverifiserte pÃ¥stander om kostnader, sÃ¸keteknologi, AI-planer og estimert samfunnsgevinst er tatt ut.

### Tekstlige forbedringer
- Dokumentet starter ikke lenger med mÃ¥lgruppelinje, og sprÃ¥ket er strammet inn mot nasjonal arkitektur og gjenbruksvurdering.
- `Hovedfunksjoner` beskriver nÃ¥ hele lÃ¸sningsbredden, inkludert registrering, hÃ¸sting, delkataloger og synlig brukerflate.
- Scope og avgrensning gjÃ¸r det tydeligere hva Felles datakatalog er, og hva som hÃ¸rer hjemme i data.norge.no eller i de underliggende kildesystemene.

