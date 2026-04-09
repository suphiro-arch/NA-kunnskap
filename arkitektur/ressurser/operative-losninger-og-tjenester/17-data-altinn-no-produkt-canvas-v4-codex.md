# Produkt-canvas: data.altinn.no

## Navn
data.altinn.no

## Ressurs ID
DIGDIR-015

## Status/Livsfase
**Produksjon** - etablert felleslÃ¸sning i Altinn for kontrollert datadeling mellom virksomheter gjennom en felles API-modell.

**Fakta:** Offisiell dokumentasjon beskriver data.altinn.no som en generisk lÃ¸sning for Ã¥ forenkle deling og gjenbruk av informasjon direkte fra kilden. Tjenestekatalogen omfatter blant annet eBevis, DrosjelÃ¸yve, Advokatregisteret, Tilda og BITS kontrollinformasjon per 26. mars 2026.

## Modenhet
**HÃ¸y funksjonell modenhet** - produktet fremstÃ¥r som et etablert mÃ¸nster for datadeling i Altinn:
- Dokumentasjonen dekker bÃ¥de overordnet produktforstÃ¥else, teknisk API-bruk og tjenestespesifikke eksempler.
- Flere ulike datadelingstjenester bruker samme grunnmodell for forespÃ¸rsel, tilgang og uthenting.
- Produktet er tydelig avgrenset som kontrollert datadelingstjeneste, ikke som Ã¥pen datakatalog eller generell portal.

**Deduksjon:** Modenheten er hÃ¸y for den generiske delingsmodellen, mens hver enkelt domenetjeneste fortsatt kan ha ulik modenhet og kompleksitet.

## Kort beskrivelse
data.altinn.no er Altinns felleslÃ¸sning for kontrollert datadeling mellom virksomheter. Produktet gjÃ¸r det mulig Ã¥ hente informasjon direkte fra autoritative kilder i en definert tjenestekontekst, med en felles API-modell for forespÃ¸rsler, tilgangskontroll og uthenting av datasett.

Produktet har bÃ¥de en tjenesteflate og en integrasjonsflate. Tjenesteflaten bestÃ¥r av konkrete datadelingstjenester som eBevis, DrosjelÃ¸yve, Advokatregisteret, Tilda og BITS kontrollinformasjon. Integrasjonsflaten bestÃ¥r av den generiske API-modellen, API-nÃ¸kler, Maskinporten-tilgang og tjenestekontekst som styrer hvilke data som kan hentes og pÃ¥ hvilket grunnlag. Dette gjÃ¸r produktet bredere enn en enkelt API-endepunktssamling, men smalere enn en generell nasjonal datakatalog.

## Kapabiliteter
- **Datadrevet: Sammenstilling av data** stÃ¸ttes nÃ¥r flere datasett og datakilder kombineres i samme tjenestekontekst.
- **Datautveksling og integrasjon: Bruke data fra andre** gjÃ¸r det mulig for konsumenter Ã¥ hente data direkte fra kilder gjennom en standardisert modell.
- **Datautveksling og integrasjon: Dele data med andre** gjÃ¸r det mulig for datatilbydere Ã¥ eksponere data gjennom en felles Altinn-lÃ¸sning.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** er sentral fordi produktet hÃ¥ndterer kontrollert tilgang til ikke-Ã¥pne data og personopplysninger.
- **Standardisering: Forvaltningsstandarder** realiseres gjennom en generisk og gjenbrukbar API-modell pÃ¥ tvers av flere tjenester.
- **Tillit: Autentisering** stÃ¸ttes gjennom bruk av Maskinporten og API-nÃ¸kler i produktets integrasjonsmodell.
- **Tillit: Samtykke** er relevant fordi enkelte tjenester bruker samtykke som grunnlag for datadeling.
- **Tillit: Tilgangskontroll** er sentral fordi tjenestekontekst og regler styrer hvilke data som kan hentes.
- **Tjenesteutvikling: Integrerbare tjenester** gjÃ¸r det mulig Ã¥ etablere flere datadelingstjenester innenfor samme grunnmÃ¸nster.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** data.altinn.no, tjenestesidene og teknisk dokumentasjon.

Dokumenterte mÃ¥l:
- Forenkle deling av data fra virksomheter og gjenbruk av informasjon direkte fra kilden.
- GjÃ¸re det enklere Ã¥ komme i gang med datadeling bÃ¥de for datakilder og konsumenter.
- Tilby et enkelt, generisk API for utveksling av datasett pÃ¥ en sikker mÃ¥te.
- Styre datadeling gjennom tjenestekontekst, autorisasjonsregler og eventuelt samtykke.

Operative mÃ¥l utledet fra de samme kildene:
- GjÃ¸re det mulig Ã¥ gjenbruke samme delingsmodell pÃ¥ flere forretningsomrÃ¥der og tjenester.
- Minimere behovet for at hver datadelingstjeneste lager sitt eget tekniske grunnmÃ¸nster.
- Gi konsumenter en mer forutsigbar integrasjonsopplevelse pÃ¥ tvers av ulike domenetjenester.

**Deduksjon:** Produktet har ogsÃ¥ en viktig rolle som standardiseringslag for kontrollert datadeling i Altinn-Ã¸kosystemet.

## Brukerbehov
- Datatilbydere trenger en felles modell for Ã¥ tilgjengeliggjÃ¸re data uten Ã¥ bygge unik infrastruktur for hver konsument.
- Konsumentsystemer trenger en standard mÃ¥te Ã¥ hente data i riktig tjenestekontekst pÃ¥.
- Juridiske og forvaltningsmessige miljÃ¸er trenger tydelig styring av samtykke, hjemler og tilgangsregler.
- Integrasjonsteam trenger dokumentasjon, API-nÃ¸kler og autentiseringsmÃ¸nstre som kan brukes pÃ¥ tvers av flere tjenester.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige og andre datatilbydere | Dele data kontrollert gjennom en felles modell | Eksponering av datasett og tjenester | Beholder data hos kilden og bruker tjenestekontekst for styring |
| Konsumentsystemer i offentlig og privat sektor | Hente data fra autoritative kilder | Automatiserte oppslag og datagjenbruk | MÃ¥ bruke bÃ¥de API-nÃ¸kkel og autentisering etter produktets modell |
| Tjenesteeiere for domenetjenester | Etablere nye datadelingstjenester | eBevis, Tilda og andre tjenestekontekster | Bruker samme grunnmÃ¸nster med ulike regler |
| Juridiske og forvaltningsmessige miljÃ¸er | Styring av grunnlag for deling | Samtykke, hjemler og autorisasjon | Viktig fordi samme datasett kan brukes i ulike kontekster |
| Utviklings- og integrasjonsteam | Forutsigbar teknisk modell | Implementasjon, test og drift av integrasjoner | MÃ¸ter produktet som API- og tilgangsmodell, ikke bare som portal |

## Hovedfunksjoner
data.altinn.no gir en generisk modell for Ã¥ be om og hente datasett direkte fra kilden. Dokumentasjonen beskriver at alle uthentinger skjer i kontekst av en tjeneste, og at tjenesten regulerer autorisasjon og hvilke datasett som kan brukes. Dette betyr at produktet ikke bare er en teknisk API-gateway, men en struktur for kontrollert datadeling der samme datasett kan brukes under ulike regler avhengig av tjenestekontekst.

En sentral funksjon ved produktet er at det kobler sammen flere konkrete datadelingstjenester innenfor samme tekniske mÃ¸nster. eBevis, DrosjelÃ¸yve, Advokatregisteret, Tilda og BITS kontrollinformasjon fremstÃ¥r som ulike tjenester oppÃ¥ samme grunnmodell. Det gjÃ¸r lÃ¸sningen relevant nÃ¥r behovet er Ã¥ etablere eller bruke kontrollert datadeling uten Ã¥ oppfinne nye integrasjonsmÃ¸nstre for hver tjeneste.

Produktet har ogsÃ¥ en tydelig tillits- og tilgangsflate. Dokumentasjonen viser bruk av Maskinporten, API-nÃ¸kler og i noen tilfeller samtykke eller annet rettsgrunnlag. Dermed dekker lÃ¸sningen mer enn bare transport av data; den tilbyr et mÃ¸nster for sikker og styrt datatilgang direkte fra kilden. Samtidig inngÃ¥r ikke eierskap til kildedataene eller faglig kvalitetssikring av innholdet som produktets hovedansvar.

data.altinn.no er derfor riktig produkt nÃ¥r vurderingen gjelder kontrollert datadeling i Altinn-Ã¸kosystemet. Det er mindre presist nÃ¥r behovet primÃ¦rt er Ã¥ publisere Ã¥pne data, katalogisere metadata eller bygge sluttbrukerrettede portaler. Produktet er heller ikke en erstatning for de konkrete domenetjenestene som bruker lÃ¸sningen; det er den felles delingsmodellen og tjenesteflaten rundt disse.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Generisk API-modell for kontrollert datadeling | Ã…pen datakatalog for hele offentlig sektor |
| Tjenestekontekst som styrer regler og tilgang | Full eierskap til eller forvaltning av alle underliggende kildedata |
| Maskinporten- og API-nÃ¸kkelbasert integrasjon | Sluttbrukerportal for innbyggere som hovedflate |
| Flere domenetjenester bygget pÃ¥ samme mÃ¸nster | Generell metadataforvaltning som eget hovedformÃ¥l |
| Henting av data direkte fra kilden | Erstatning for juridiske vurderinger hos tjenesteeier og datatilbyder |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-26):**
- Dokumentasjonen viser en etablert tjenestekatalog og flere produktiserte datadelingstjenester.
- Kildene viser videre at nye tjenester kan legges til innenfor samme generiske modell.

**Ikke offentlig dokumentert i brukte kilder:** En samlet, tidsfestet roadmap for produktet.

**Deduksjon:** Videreutviklingen vil trolig bestÃ¥ i flere tjenester, videreutvikling av dokumentasjon og fortsatt forbedring av tilgangs- og integrasjonsmÃ¸nstre, men dette er ikke konkret offentlig tidsfestet.

## Forretningsverdi/Verdiforslag
### For datatilbydere
- Reduserer behovet for egne tekniske delingslÃ¸sninger for hver enkelt konsument.
- GjÃ¸r det mulig Ã¥ dele data gjennom en etablert og dokumentert modell for kontrollert tilgang.

### For datakonsumenter
- Gir en mer forutsigbar integrasjonsopplevelse pÃ¥ tvers av flere datadelingstjenester.
- GjÃ¸r det mulig Ã¥ hente oppdaterte data direkte fra kilden i stedet for Ã¥ basere seg pÃ¥ lokale kopier.

### For offentlig sektor
- Ã˜ker gjenbruk av Ã©n felles modell for kontrollert datadeling.
- StÃ¸tter mer sammenhengende tjenester gjennom sikker gjenbruk av informasjon som allerede finnes.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Feil forstÃ¥else av tjenestekontekst, hjemmel eller samtykke kan gi ulovlig datadeling | Tydelig regelmodell, juridisk avklaring og god dokumentasjon |
| Teknisk | Avhengighet til underliggende datakilder kan pÃ¥virke tilgjengelighet og svartid | Robust feilbehandling, overvÃ¥king og tydelige forventninger til kildesystemer |
| Sikkerhet | Feil tilgangskontroll eller feil bruk av API-nÃ¸kler og tokens kan gi uÃ¸nsket datatilgang | Streng tilgangsstyring, minst mulig deling og god nÃ¸kkelhÃ¥ndtering |
| Forvaltning | Uklare grenser mellom den generiske lÃ¸sningen og de konkrete domenetjenestene kan gi feil ansvarsbilde | Tydelig produktavgrensning og klar dokumentasjon av tjenestekontekst |
| Brukeropplevelse | Oppstart kan oppleves krevende nÃ¥r flere mekanismer mÃ¥ vÃ¦re pÃ¥ plass samtidig | Bedre onboarding, tydelige eksempler og tjenestespesifikk dokumentasjon |

## Kanaler
- Produktside: https://data.altinn.no/
- Tjenesteoversikt: https://data.altinn.no/products
- Teknisk dokumentasjon: https://docs.data.altinn.no/
- Tjenester: https://docs.data.altinn.no/tjenester/

## Plattform
Felles datadelingslÃ¸sning i Altinn-portefÃ¸ljen med generisk API-modell, tjenestekontekst og tilgangsstyring for kontrollert datadeling.

**Fakta:** Dokumentasjonen viser at produktet bruker tjenestekontekst for Ã¥ styre hvilke datasett som kan hentes, og at kall typisk krever bÃ¥de API-nÃ¸kkel og autentisering gjennom Maskinporten. LÃ¸sningen er bygget for gjenbruk pÃ¥ tvers av flere domenetjenester.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsmodell, detaljert plattformarkitektur og separat kostnadsmodell for produktet alene.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Samme delingsmodell kan brukes pÃ¥ flere ulike forretningsomrÃ¥der.
- Produktet reduserer behovet for lokale sÃ¦rintegrasjoner for kontrollert datadeling.
- Gjenbruksverdien er stÃ¸rst nÃ¥r behovet gjelder sikker og styrt datadeling direkte fra kilden, ikke Ã¥pen publisering eller metadataoversikt.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** er direkte relevant fordi produktet er laget for Ã¥ hente og gjenbruke data fra kilden.
- **P5: Del og gjenbruk lÃ¸sninger** realiseres ved at flere tjenester bygger pÃ¥ samme tekniske delingsmodell.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** styrkes fordi datadeling kan skje gjennom et felles mÃ¸nster mellom virksomheter.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** stÃ¸ttes gjennom kontrollert tilgang, autentisering og samtykkemekanismer.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Separat finansieringsmodell eller kostnadsnivÃ¥ for data.altinn.no isolert fra Ã¸vrig Altinn-portefÃ¸lje.
- **Deduksjon:** Produktet mÃ¥ forstÃ¥s som del av Altinns samlede forvaltning og finansiering.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digdir / Altinn-forvaltningen | Offisiell dokumentasjon pÃ¥ data.altinn.no og docs.data.altinn.no |
| Driftsansvar | Altinns forvaltnings- og driftsmiljÃ¸ | Produktet beskrives som del av Altinn-Ã¸kosystemet |
| Budsjettansvar | Del av Altinn-portefÃ¸ljen | Ingen separat offentlig kostnadsmodell verifisert |
| Styringsmodell | Produktforvaltning i Altinn med flere tjenestekontekster | FremgÃ¥r av produkt- og tjenestestrukturen |

## Lenke til dokumentasjon
- https://data.altinn.no/
- https://data.altinn.no/products
- https://docs.data.altinn.no/
- https://docs.data.altinn.no/tjenester/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/17-data-altinn-no-produkt-canvas-v3-codex.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://data.altinn.no/ (kontrollert 2026-03-26)
- Nettkilde: https://data.altinn.no/products (kontrollert 2026-03-26)
- Nettkilde: https://docs.data.altinn.no/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.data.altinn.no/tjenester/ (kontrollert 2026-03-26)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen er oppdatert med kontroll mot gjeldende tjenestekatalog og teknisk dokumentasjon for data.altinn.no.
- Produktets bredde som bÃ¥de tjenesteflate og integrasjonsflate er tydeligere beskrevet.
- Avgrensningen mot Ã¥pne datakataloger og rene portalprodukter er strammet inn.

### Tekstlige forbedringer
- Hovedfunksjoner er skrevet om til mer forklarende avsnitt i trÃ¥d med oppdatert instruks.
- SprÃ¥ket er harmonisert med nyere canvas-filer og tydeligere mÃ¥lrettet mot nasjonal arkitektur.
- Gjenbruk og scope er gjort mer presist for Ã¥ stÃ¸tte produktvalg i senere analyser.

