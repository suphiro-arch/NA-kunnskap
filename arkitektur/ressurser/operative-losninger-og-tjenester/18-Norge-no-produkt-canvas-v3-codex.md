# Produkt-canvas: Norge.no

## Navn
Norge.no

## Ressurs ID
DIGDIR-016

## Status/Livsfase
**Produksjon** - etablert nasjonal veiviser og informasjonsportal for digitale offentlige tjenester.

**Fakta:** Om-siden beskriver Norge.no som en guide til digitale offentlige tjenester i Norge. Portalen presenterer tjenester fra statlige og kommunale virksomheter og gir samtidig informasjon om digital kommunikasjon mellom offentlige myndigheter og innbyggere.

## Modenhet
**Høy funksjonell modenhet** - etablert innbyggerrettet løsning med tydelig rolle:
- Norge.no er en fast inngang til digitale tjenester og offentlig informasjon på tvers av stat og kommune.
- Løsningen kombinerer søk, temastruktur, livssituasjoner og veiledning om digital kommunikasjon.
- Portalen har varig nasjonal rolle som veiviser, ikke bare som kampanje- eller informasjonsside.

**Deduksjon:** Modenheten er høy som veiviser og inngangsflate, mens nytteverdien for den enkelte bruker vil avhenge av kvaliteten på informasjonen og tjenestelenkene som publiseres fra underliggende virksomheter.

## Kort beskrivelse
Norge.no er en nasjonal veivisertjeneste som hjelper innbyggere med å finne fram i digitale offentlige tjenester. Produktet samler tjenester og informasjon fra statlige og kommunale virksomheter i ett brukerrettet inngangspunkt, og gjør det enklere å orientere seg gjennom søk, temaområder og livssituasjoner. Løsningen er særlig relevant når målet er å gjøre offentlig sektor mer forståelig og tilgjengelig for innbyggere som ikke kjenner den interne organiseringen.

## Kapabiliteter
- **Sluttbrukertjenester: Sammenhengende tjenester** gir innbyggeren en mer helhetlig brukerreise på tvers av mange offentlige tjenester og informasjonskilder.
- **Sluttbrukertjenester: Tjenestekjeder** lenker sammen relevante tjenester i livssituasjoner og gjør det lettere å gå videre fra behov til konkret tjeneste.
- **Tjenesteutvikling: Tjenestedesign** viser seg i behovsbasert navigasjon, livssituasjoner og en struktur som tar utgangspunkt i hva brukeren prøver å få gjort.
- **Informasjonsforvaltning: Oversikt over tjenester** gjør offentlige tjenester og informasjon oppdagbare i en felles katalog- og veiviserflate.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon på Norge.no.

## Produktmål
**Primærkilder:** Norge.no `About Norge.no` og forsiden.

Dokumenterte mål:
- Være en veiviser til digitale offentlige tjenester i Norge.
- Presentere tjenester fra nasjonale og lokale offentlige virksomheter.
- Gi informasjon om hvordan offentlige myndigheter kommuniserer digitalt med innbyggere.

Operative mål utledet fra de samme kildene:
- Gjøre det enklere å finne relevante tjenester via søk, tema og livssituasjoner.
- Samle informasjon om digital postkasse, kontaktregister og digital kommunikasjon i en felles brukerflate.
- Gi innbyggerne én tydelig inngang til en ellers fragmentert offentlig tjenestestruktur.

## Brukerbehov
- Innbyggere trenger én forståelig inngang til digitale offentlige tjenester uten å kjenne hvilke virksomheter som har ansvar for hva.
- Brukere med lavere digital modenhet trenger tydelig navigasjon og veiledning i hvordan offentlig digital kommunikasjon fungerer.
- Virksomheter trenger en nasjonal kanal som gjør egne tjenester synlige i en større sammenheng.
- Innbyggere trenger et sted der de både kan finne tjenester og forstå praktiske forhold som digital postkasse, eID og kontaktinformasjon.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Innbyggere som leter etter tjenester | Finne riktig tjeneste raskt | Søk, tema og livssituasjoner | Hovedmålgruppen for portalen |
| Innbyggere som trenger veiledning om digital kontakt med det offentlige | Forstå digital post, kontaktregister og eID | Informasjon og egenoppdatering | Viktig for digital inkludering |
| Brukere med lav eller varierende digitalkompetanse | Enklere navigasjon og tydelig språk | Veiviser og oversikt | Løsningen demper kompleksiteten i offentlig sektor |
| Offentlige virksomheter som publiserer tjenester | Synlighet og korrekt presentasjon | Tjenesteoppføring og lenking | Er innholdsleverandører, ikke primærsluttbrukere |

## Hovedfunksjoner
### Primære funksjoner
- Norge.no fungerer som en felles inngang til digitale offentlige tjenester. Det er produktets tydeligste funksjon og skiller det fra portaler som primært leverer én bestemt tjeneste.
- Norge.no organiserer innhold gjennom søk, tema og livssituasjoner. Det gjør løsningen relevant når brukeren vet behovet sitt, men ikke kjenner ansvarlig virksomhet eller riktig tjenestenavn.
- Norge.no samler informasjon om digital kommunikasjon med det offentlige, blant annet digital postkasse, kontaktinformasjon og reservasjon. Dette gjør portalen mer enn en ren katalog over tjenester.
- Norge.no gir virksomheter en felles brukerflate for å bli oppdaget i en nasjonal sammenheng. Produktet er derfor også en veiviser mellom tjenester, ikke bare en informasjonsside.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Veiviser til digitale offentlige tjenester | Selve utførelsen av de underliggende tjenestene |
| Søkbart og behovsbasert tjenesteinnhold | Saksbehandling hos ansvarlige virksomheter |
| Informasjon om digital postkasse, kontaktregister og digital kommunikasjon | Felles innlogging for alle tjenester |
| Livssituasjoner, tema og lenking til andre tjenester | Full eierskap til innholdet hos alle underliggende tjenesteeiere |

## Veikart over kommende funksjonalitet
**Fakta:** Jeg fant ikke en offentlig tidsfestet utviklingsplan i kildene brukt i denne arbeidsøkten.

**Ikke offentlig verifisert i denne arbeidsøkten:** Konkrete roadmap-punkter, planlagte nye funksjoner eller prioriterte brukerforbedringer.

**Deduksjon:** Videreutviklingen vil sannsynligvis dreie seg om bedre søk, bedre livssituasjonsnavigasjon og videre forbedring av informasjon om digital kommunikasjon, men dette må bekreftes i egne veikartkilder.

## Forretningsverdi/Verdiforslag
### For innbyggere
- Reduserer letetid og gjør det enklere å finne fram til riktige offentlige tjenester.
- Gir mer forståelig inngang til offentlig sektor gjennom tema og livssituasjoner.

### For offentlige virksomheter
- Øker synligheten til egne tjenester i en nasjonal kanal.
- Setter virksomhetenes tjenester inn i en større sammenheng som er lettere å forstå for brukeren.

### For offentlig sektor og samfunn
- Bidrar til mer sammenhengende brukeropplevelse på tvers av virksomheter.
- Gjør offentlig digital kommunikasjon lettere å forstå og ta i bruk.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil eller utdatert informasjon om digitale rettigheter og kommunikasjonsvalg kan gi feil veiledning | Tydelig redaksjonelt ansvar og oppdatert innholdsforvaltning |
| Teknisk | Brutte lenker eller svak søkekvalitet reduserer nytteverdien | Løpende vedlikehold, søkeforbedring og oppfølging av tjenestelenker |
| Sikkerhet | Brukerne kan forveksle veiviserrollen med behandlingen av egne opplysninger i underliggende tjenester | Tydelig grensesnitt mellom veiledning, innlogging og tjenesteutførelse |
| Leverandør/forvaltning | Nytten avhenger av at mange virksomheter holder egne oppføringer relevante | Koordinert innholdsforvaltning og tydelige samarbeidsflater |
| Brukeropplevelse | Portalen kan fortsatt oppleves som kompleks hvis strukturen ikke treffer brukernes behov | Brukerinnsikt, tjenestedesign og tydelig språk |

## Kanaler
- Portal: https://www.norge.no/
- Om Norge.no: https://www.norge.no/om-norge-no
- Om Norge.no (engelsk): https://www.norge.no/en/about-norgeno

## Plattform
Norge.no er en nasjonal portal- og veiviserløsning for digitale offentlige tjenester og digital kommunikasjon med innbyggere.

**Fakta:**
- Tjenestene kan finnes via søkefunksjon eller temameny.
- Portalen organiserer innhold både etter emner og livssituasjoner.
- Norge.no gir også tilgang til informasjon om digital postkasse og kontaktregister.

**Ikke offentlig dokumentert i brukte kilder:** Full teknisk plattformbeskrivelse, intern søketeknologi og driftsarkitektur.

## Gjenbruk
**Høy gjenbruksverdi:**
- Norge.no gjenbruker tjenesteinformasjon i en felles nasjonal inngang i stedet for at brukeren må starte hos hver enkelt virksomhet.
- Livssituasjoner og tematisk navigasjon gir et gjenbrukbart mønster for hvordan tjenester kan presenteres brukerrettet.
- Portalen gir også gjenbruk av felles veiledning om digital kommunikasjon og kontaktinformasjon.

## Støtter arkitekturprinsipper
- **P1 Ta utgangspunkt i brukernes behov** - løsningen er bygget som en brukerrettet veiviser til tjenester.
- **P5 Del og gjenbruk løsninger** - Norge.no gir én nasjonal inngang i stedet for mange parallelle veiviserflater.
- **P6 Lag digitale løsninger som støtter samhandling** - løsningen gjør tjenester fra mange virksomheter tilgjengelige i samme brukerreise.

## Finansiering
- **Ikke offentlig dokumentert i brukte kilder:** Jeg fant ikke en presis offentlig beskrivelse av finansieringsmodell eller budsjettansvar i denne arbeidsøkten.
- **Deduksjon:** Norge.no framstår som en forvaltet nasjonal Digdir-løsning, men finansieringsmodellen må bekreftes i egne styrings- eller budsjettkilder.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Om-siden for Norge.no |
| Driftsansvar | Digdir framstår som ansvarlig for den samlede løsningen | Om-siden for Norge.no |
| Budsjettansvar | Ikke offentlig spesifisert i brukte kilder | Ikke verifisert i denne arbeidsøkten |
| Styringsmodell | Nasjonal veiviser som samler tjenester fra mange virksomheter | Om-siden og portalstrukturen |

## Lenke til dokumentasjon
- https://www.norge.no/
- https://www.norge.no/om-norge-no
- https://www.norge.no/en/about-norgeno

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/18-Norge-no-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.norge.no/ (hentet 2026-03-18)
- Nettkilde: https://www.norge.no/en/about-norgeno (hentet 2026-03-18)
- Nettkilde: https://www.norge.no/om-norge-no (oppført i lokale lenker, ikke verifisert direkte i denne arbeidsøkten)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Vurderingen bygger videre på `18-Norge-no-produkt-canvas-v2-copilot.md`, men er kontrollert mot oppdatert offentlig beskrivelse av Norge.no.
- Kapabilitetene er strammet inn til direkte koblinger og synkronisert med produktregisteret og masterfila for produkt-kapabilitet-koblinger.
- Produktets rolle som veiviser og inngangsflate er tydeligere skilt fra underliggende tjenesteleveranse.

### Tekstlige forbedringer
- Norsk tegnsett og språk er ryddet opp.
- Hovedfunksjoner er beskrevet tydeligere på konseptnivå.
- Produktets scope og avgrensning er gjort skarpere for å gjøre sammenligning enklere.



