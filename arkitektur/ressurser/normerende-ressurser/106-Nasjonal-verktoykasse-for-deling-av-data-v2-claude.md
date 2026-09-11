# Nasjonal verktøykasse for deling av data

## Navn
Nasjonal verktøykasse for deling av data

## Ressurs ID
DIGDIR-038

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Veileder

## Status/Livsfase
Aktiv. Ressursen er publisert som del av Digdirs datadelingsveiledning og brukes som praktisk støtte for virksomheter som skal tilby data.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Veilederen oppgir ikke revisjonsdato eller versjonsnummer, så det er ikke mulig å se hvor gammelt det enkelte rådet er.

## Kort beskrivelse
Nasjonal verktøykasse for deling av data er en normerende veiledningsressurs for virksomheter som skal gjøre data tilgjengelige på en trygg, dokumentert og gjenbrukbar måte.

Ressursen samler praktiske steg fra dataoversikt og tilgjengeliggjøring til beskrivelse, tilgangsvilkår, drift og forvaltning. Den er bygget som en rekkefølge av spørsmål datatilbyderen må svare på: hva har jeg, hvordan bør jeg tilby det, hvordan beskriver jeg det, hvem skal få tilgang, og hvordan holder jeg det i live.

## Formål og normerende rolle
Formålet er å gi virksomheter et operativt veiledningsgrunnlag for å etablere god delingspraksis over tid.

Ressursen er normerende ved at den anbefaler standarder, minimumsbeskrivelser, tilgangskategorier og forvaltningsrutiner som gir bedre samhandling mellom datatilbydere og datakonsumenter.

**Fakta:** Retningslinjene bygger på W3Cs `Data on the Web Best Practices` og på regjeringens retningslinjer ved tilgjengeliggjøring av offentlige data. Veilederen henter altså normeringen fra etablerte rammeverk framfor å etablere egne krav.

**Deduksjon:** Det gir ressursen en annen rolle enn en standard. Den fastsetter ikke nye krav, men oversetter krav og god praksis som allerede finnes, til en arbeidsrekkefølge en virksomhet kan følge. Verdien ligger i rekkefølgen og i at spredte føringer samles ett sted, ikke i nytt normativt innhold.

## Kapabiliteter
- **Datautveksling og integrasjon: Dele data med andre**
  Veilederen er skrevet for rollen som datatilbyder, og beskriver hele løpet fra valg av distribusjonsform til drift av delingstjenesten.
- **Informasjonsforvaltning: Oversikt over datasett**
  Veilederen fastslår at offentlige virksomheter skal synliggjøre egne datasett og datatjenester på `data.norge.no` (`DIGDIR-014`), enten ved registrering direkte, gjennom Geonorge, eller ved å publisere en katalog som høstes.
- **Informasjonsforvaltning: Datastyring**
  Veilederen stiller krav til hvilke opplysninger et datasett skal beskrives med, og til at beskrivelsene holdes oppdatert over tid.
- **Standardisering: Forvaltningsstandarder**
  Veilederen peker på konkrete standarder for hvordan data og datatjenester skal tilbys og beskrives, blant annet OpenAPI Specification og GraphQL for datatjenester.
- **Veiledning: Utvikling og formidling av veiledning**
  Ressursen samler og formidler praktiske veiledere for virksomheter som skal etablere, beskrive og forvalte datadeling på en mer standardisert og samhandlingsorientert måte.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Datatilbydere i offentlige virksomheter | Praktisk oppskrift for deling | Etablering og forbedring av datadeling | Primær målgruppe |
| Arkitekter og dataforvaltere | Felles metode og standarder | Dokumentasjon, API og katalogarbeid | Viktig i gjennomføring |
| Drift- og forvaltningsmiljøer | Rutiner for kvalitet og endring | SLA, avtaler og vedlikehold | Kritisk for varig kvalitet |

## Normerende innhold
Ressursen beskriver hvordan virksomheter bør skaffe oversikt over egne data, velge passende distribusjonsform og bruke standardiserte grensesnitt.

**Fakta:** Veilederen er organisert i syv ledd: oversikt over egne data, valg av hvordan data bør tilbys, beskrivelse og synliggjøring, grunnleggende opplysninger om datasett og datatjenester, plikten til å synliggjøre data, tilgang og vilkår, og forvaltning av henholdsvis løsninger og avtaler og av data og databeskrivelser. Den avsluttes med en sjekkliste.

Ressursen vektlegger at både data og datatjenester må beskrives og synliggjøres. **Fakta:** Som grunnleggende opplysninger oppgir veilederen tittel, nøkkelord og beskrivelse, lenke til begrepsdefinisjon, ansvarlig utgiver med kontaktinformasjon, publiserings- og endringsdato, kategorisering av tilgangsnivå, og lenke til distribusjoner og endepunkt for datatjenester.

**Fakta:** Tilgang kategoriseres i tre nivåer: data med allmenn tilgang, data med betinget tilgang, og data som ikke har allmenn tilgang. Inndelingen er standardisert av EU og brukes ved utveksling til data.europa.eu.

**Deduksjon:** Tilgangskategorien er det feltet som binder beskrivelsen til teknisk løsning. Betinget tilgang forutsetter at tilbyderen har en mekanisme for å autorisere den enkelte konsumenten, og det er der fellesløsningene veilederen peker på kommer inn: `Maskinporten` (`DIGDIR-002`) for maskinell tilgang, `ID-porten` og Altinn autorisasjon for tilgang knyttet til person og virksomhet. Kategoriseringen er derfor ikke bare et metadatafelt, men et valg som avgjør hvilken infrastruktur som må på plass.

Ressursen tydeliggjør også behov for god forvaltning av avtaler, drift, sikkerhet og vedlikehold av datasettbeskrivelser. **Fakta:** Veilederen anbefaler tjenesteavtaler (SLA) med konsumentene, at konfidensialitet, integritet og tilgjengelighet sikres, og at databeskrivelser oppdateres jevnlig slik at katalogen ikke viser utdatert informasjon.

## Forpliktelsesnivå og etterlevelse
Ressursen er veiledende. Etterlevelse er forventet i praksis for virksomheter som tilbyr data til andre aktører, spesielt der deling påvirker flere tjenesteløp.

**Fakta:** Ett av punktene er likevel mer forpliktende enn resten. Plikten til å synliggjøre egne datasett og datatjenester på `data.norge.no` følger av Digitaliseringsrundskrivet (`DIGDIR-044`), ikke av veilederen selv.

**Deduksjon:** Forpliktelsesnivået i ressursen er derfor blandet. Det meste er anbefalinger en virksomhet kan avvike fra med saklig grunn, mens synliggjøringskravet er en føring virksomheten allerede er bundet av gjennom rundskrivet. Den som bruker veilederen som sjekkliste, bør skille mellom de to.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Kildene beskriver ingen ordning for å kontrollere at veiledningen faktisk følges, og ingen frist for når synliggjøringen skal være gjennomført.

## Typiske analyse- og beslutningssituasjoner
- når en virksomhet skal etablere seg som datatilbyder
- når data skal dokumenteres og synliggjøres i datakatalog
- når tilgangsvilkår og driftsrutiner for datadeling må formaliseres
- når det skal avgjøres hvilken tilgangskategori et datasett hører i, og dermed hvilken autorisasjonsløsning som må på plass

## Bruksområde
Ressursen brukes i planlegging, etablering og forvaltning av delingstjenester, fra første publisering til løpende vedlikehold.

## Når ressursen normalt ikke er tilstrekkelig alene
Ressursen må suppleres med juridiske vurderinger, sikkerhetsarbeid og konkrete tekniske valg i den enkelte virksomhet.

Den forutsetter også at virksomheten allerede har oversikt over egne data. Er den oversikten ikke på plass, hører arbeidet først i `Orden i eget hus` (`DIGDIR-036`) og i `Rammeverk for informasjonsforvaltning` (`DIGDIR-029`).

## Scope og avgrensning
Inngår:
- praktiske steg for å tilby data
- anbefalinger for dokumentasjon, tilgang og forvaltning
- kobling til relevante nasjonale standarder og støtteressurser

Inngår ikke:
- detaljert design av hvert enkelt API eller integrasjonsløp
- full juridisk behandling av enkelttilfeller
- rollen som datakonsument; veilederen er skrevet fra tilbydersiden

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse | Grunnlag |
|---|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet | Oppgitt utgiver på digdir.no |
| Forvaltningsansvar | Digdir forvalter verktøykassen i datadelingsområdet | Oppgitt utgiver på digdir.no |
| Endringsprosess | Oppdateres løpende i tråd med veiledningsbehov og praksis | **Deduksjon:** veilederen er publisert som løpende nettinnhold uten versjonsmerking |
| Publiserings- og beslutningsarena | digdir.no | Publiseringsformen |

## Relasjon til andre ressurser
- `Rammeverk for informasjonsforvaltning` (`DIGDIR-029`), som gir det overordnede metodegrunnlaget veilederen operasjonaliserer
- `Orden i eget hus` (`DIGDIR-036`), som dekker steget før deling: oversikt og styring av egne data
- `data.norge.no` (`DIGDIR-014`) og `Felles datakatalog` (`DIGDIR-011`), som er flatene beskrivelsene publiseres på
- `Maskinporten` (`DIGDIR-002`), som er den anbefalte mekanismen for betinget maskinell tilgang
- `Digitaliseringsrundskrivet` (`DIGDIR-044`), som er hjemmelen bak kravet om å synliggjøre data

## Forretningsverdi og arkitekturverdi
Ressursen gir verdi ved å redusere oppstartskostnad og usikkerhet for datatilbydere, og ved å øke kvaliteten i delingspraksis.

Arkitekturverdien er økt interoperabilitet gjennom mer standardisert beskrivelse, tilgjengeliggjøring og forvaltning av data.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Modenhet | Virksomheter mangler grunnleggende dataoversikt | Svak delingskvalitet | Prioritere orden i eget hus før skalering |
| Dokumentasjon | Mangelfulle metadata og API-beskrivelser | Lav oppdagbarhet og feil bruk | Bruke anbefalte minimumsbeskrivelser |
| Forvaltning | Rutiner for endring og drift er uklare | Ustabil datadeling | Etablere SLA, ansvar og vedlikeholdsrutiner |
| Aktualitet | Veilederen er publisert uten versjonsmerking eller revisjonsdato | Leseren kan ikke se om et råd er nytt eller foreldet | Kontrollere konkrete standardvalg mot Referansekatalogen før de legges til grunn |

## Konsekvens ved manglende bruk eller avvik
Datadeling kan bli uforutsigbar og lite skalerbar, med svak kvalitet i beskrivelser, tilgangsstyring og forvaltning over tid.

Der veilederen gjengir synliggjøringskravet i Digitaliseringsrundskrivet, er avvik ikke bare et kvalitetsproblem: data som ikke er registrert i katalogen, er i praksis usynlige for andre virksomheter uansett hvor godt de er tilrettelagt teknisk.

## Publiseringsform og tilgjengelighet
Ressursen publiseres åpent på digdir.no i datadelingssporet, som nettinnhold uten innlogging.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**  
  Ressursen gir praktiske mekanismer for deling og gjenbruk av data.
- **P5: Del og gjenbruk løsninger**  
  Veilederen anviser etablerte fellesløsninger for tilgangsstyring og katalogisering framfor lokale varianter.
- **P7: Sørg for tillit til oppgaveløsningen**  
  Ressursen støtter trygg deling gjennom tydelig dokumentasjon, vilkår og forvaltningsrutiner.

## Svakheter, spenninger og begrensninger mot prinsippene
Ressursen forutsetter at virksomheten faktisk prioriterer forvaltning over tid. Uten dette kan deling bli teknisk mulig, men organisatorisk skjør.

**Deduksjon:** Det ligger også en spenning mellom P4 og P7 i selve tilgangskategoriseringen. Veilederen gir tre kategorier, men ingen metode for å avgjøre hvilken et datasett hører i. Den vurderingen er rettslig og forvaltningsfaglig, og overlates til virksomheten. Der kompetansen mangler, er den enkleste utveien å velge en strengere kategori enn nødvendig, og resultatet blir data som formelt er delt, men i praksis ikke tilgjengelige.

## Lenke til dokumentasjon
- https://www.digdir.no/datadeling/slik-blir-du-en-god-datatilbyder/2248

## Kildegrunnlag brukt i utfyllingen
- sources/links.md, kontrollert 2026-09-11
- arkitektur/ressurser/produktnummerering.md, kontrollert 2026-09-11
- arkitektur/prinsipper/principles.md, kontrollert 2026-09-11
- https://www.digdir.no/datadeling/slik-blir-du-en-god-datatilbyder/2248, kontrollert 2026-09-11
