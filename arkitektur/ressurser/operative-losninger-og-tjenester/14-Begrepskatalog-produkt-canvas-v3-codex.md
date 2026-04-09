# Produkt-canvas: Begrepskatalog

## Navn
Begrepskatalog

## Ressurs ID
DIGDIR-012

## Status/Livsfase
**Produksjon** - etablert nasjonal delkatalog for publisering, søk og sammenligning av begreper i offentlig sektor.

**Fakta:** data.norge.no beskriver Begrepskatalogen som en del av katalogtilbudet og forklarer at formålet er å gjøre data mer forståelige. Alle publiserte begreper følger forvaltningsstandarden `SKOS-AP-NO-Begrep`, og løsningen gjør det mulig å finne, lese og sammenligne begreper på tvers av virksomheter.

## Modenhet
**Høy modenhet** - tydelig avgrenset og innarbeidet del av Felles datakatalog:
- Produktet er i operativ bruk som nasjonal katalog for begrepsbeskrivelser.
- Det finnes både synlig brukerflate, teknisk dokumentasjon og publiseringsveiledning.
- Begrepskatalogen er tett integrert i Felles datakatalog, men har en tydelig egen rolle som semantisk delkatalog.
- Standarden for begrepsbeskrivelser er eksplisitt dokumentert og gir et mer stabilt grunnlag enn rene fritekstbeskrivelser.

**Deduksjon:** Modenheten er høy fordi produktet har en klar og varig funksjon i informasjonsforvaltning, men nytteverdien avhenger fortsatt av at virksomhetene faktisk beskriver egne begreper godt nok.

## Kort beskrivelse
Begrepskatalog er den nasjonale delkatalogen for å beskrive og synliggjøre begreper som brukes i offentlig sektor. Produktet gjør det mulig å publisere begrepsbeskrivelser etter en felles standard, søke i dem, sammenligne begreper og bruke dem som semantisk grunnlag for datasett, API-er og informasjonsmodeller. Løsningen er en del av Felles datakatalog, men skiller seg fra den overordnede katalogen ved å være spesialisert på begrepsforståelse og semantisk avklaring.

## Kapabiliteter
- **Informasjonsforvaltning: Datastyring** støtter forvaltning av begreper som en del av virksomhetenes samlede informasjonsforvaltning.
- **Informasjonsforvaltning: Informasjonsarkitektur** gir et semantisk grunnlag som kan brukes i modeller, API-er og databeskrivelser.
- **Informasjonsforvaltning: Oversikt over begreper** er produktets kjernefunksjon ved at begreper kan publiseres, søkes opp og sammenlignes.
- **Standardisering: Forvaltningsstandarder** bygger på felles standard for begrepsbeskrivelser og gjør innholdet mer sammenlignbart og gjenbrukbart.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot data.norge.no, teknisk dokumentasjon og Digdirs sider om Felles datakatalog.

## Produktmål
**Primærkilder:** Begrepskatalogen på data.norge.no, teknisk dokumentasjon for data.norge.no og Digdir-sidene for Felles datakatalog.

Dokumenterte mål:
- Gjøre data mer forståelige ved å gi begreper tydelige beskrivelser og definisjoner.
- Gjøre det mulig å publisere begreper etter en felles standard.
- Gjøre begreper søkbare og sammenlignbare på tvers av virksomheter.

Operative mål utledet fra de samme kildene:
- Redusere semantiske misforståelser når data deles eller brukes på tvers.
- Gi datatilbydere og arkitekter et felles sted for å beskrive hva sentrale termer betyr.
- Styrke koblingen mellom begreper og andre dataressurser i Felles datakatalog.

## Brukerbehov
- Virksomheter trenger en felles måte å publisere og vedlikeholde begrepsbeskrivelser på.
- Arkitekter og informasjonsforvaltere trenger semantisk avklaring når de lager modeller, API-er og databeskrivelser.
- Datakonsumenter trenger å forstå hva sentrale begreper betyr før de vurderer eller bruker data.
- Forvaltningsmiljøer trenger en løsning som gjør det lettere å etablere mer konsistent terminologi på tvers av virksomheter.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Begrepsansvarlige i virksomheter | Publisere og vedlikeholde begrepsbeskrivelser | Faglig og semantisk forvaltning | Primærbruker på publiseringssiden |
| Arkitekter og informasjonsforvaltere | Finne og sammenligne begreper | Informasjonsarkitektur, modellering og datadeling | Bruker katalogen som semantisk referanse |
| Utviklere og integrasjonsteam | Forstå sentrale termer i data og API-er | Implementasjon og integrasjon | Møter ofte produktet indirekte via andre kataloger |
| Datakonsumenter og analytikere | Tolke data riktig | Analyse, gjenbruk og vurdering av datakilder | Har behov for mer enn bare tekniske metadata |
| Digdir og forvaltningsmiljøer | Forvalte standard, veiledning og produktutvikling | Drift, dokumentasjon og videreutvikling | Bærer produktansvaret |

## Hovedfunksjoner
### Primære funksjoner
**Publisering av begrepsbeskrivelser etter felles standard.** Produktet gjør det mulig å beskrive begreper på en strukturert måte, med definisjon, term, gyldighet, kontaktinformasjon og andre relevante metadata. Dette er viktig fordi løsningen ikke bare er et oppslagsverk, men et standardisert publiseringsløp for semantisk informasjon.

**Søk, oppslag og sammenligning av begreper.** Begrepskatalogen gir en egen brukerflate for å finne begreper og sammenligne flere begreper ved siden av hverandre. Det gjør løsningen nyttig når ulike virksomheter bruker like eller lignende ord på forskjellige måter, og når brukeren trenger å avklare hvilket begrep som faktisk passer best.

**Maskinlesbar og gjenbrukbar semantikk.** Begrepsbeskrivelser følger `SKOS-AP-NO-Begrep`, som gjør dem mer egnet for gjenbruk i andre kataloger og løsninger. Produktet er derfor ikke bare laget for mennesker som leser definisjoner, men også for mer strukturert gjenbruk av begrepsinformasjon i det nasjonale dataøkosystemet.

**Semantisk kobling til resten av Felles datakatalog.** Begrepskatalogen er en spesialisert delkatalog innenfor et større produktområde. Den har verdi alene, men den får størst effekt når begrepene brukes sammen med datasett, API-er og informasjonsmodeller. Det gjør den til en semantisk grunnmur heller enn en fullstendig datakatalog i seg selv.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Publisering og søk i begrepsbeskrivelser | Full forvaltning av datasett, API-er eller informasjonsmodeller |
| Sammenligning av begreper og semantisk avklaring | Selve implementasjonen av begreper i lokale systemer |
| Bruk av forvaltningsstandard for begrepsbeskrivelser | Automatisk harmonisering av terminologi på tvers uten faglig arbeid |
| Delkatalog for begreper innenfor Felles datakatalog | Felles datakatalog som overordnet produktområde |
| Semantisk grunnlag for andre kataloger og beskrivelser | Juridisk autorisasjon eller styring av datatilgang |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-27):**
- Produktet har egen katalogflate, teknisk dokumentasjon og publiseringsstandard.
- data.norge.no viser at begrepskatalogen inngår i et bredere katalogområde med flere relaterte ressurskategorier.

**Ikke offentlig verifisert i denne arbeidsøkten:** Detaljert og tidsfestet veikart for ny funksjonalitet er ikke hentet ut.

**Deduksjon:** Videreutviklingen vil trolig dreie seg om bedre publiseringsflyt, sterkere sammenheng med andre kataloger og bedre støtte for sammenligning og gjenbruk av begreper.

## Forretningsverdi/Verdiforslag
### For virksomheter
- Gjør det enklere å beskrive sentrale fagbegreper på en måte andre kan forstå og gjenbruke.
- Reduserer behovet for at hver virksomhet bygger egne, isolerte begrepsoversikter.
- Gir bedre grunnlag for mer konsistent begrepsbruk i dokumentasjon og datadeling.

### For arkitektur- og utviklingsmiljøer
- Gir en felles semantisk referanse for modeller, API-er og dataressurser.
- Reduserer risikoen for misforståelser når like ord brukes forskjellig i ulike sammenhenger.
- Styrker koblingen mellom forretningsbegreper og tekniske beskrivelser.

### For offentlig sektor
- Understøtter mer sammenhengende informasjonsforvaltning på tvers av virksomheter.
- Bidrar til bedre forståelse av hva data betyr, ikke bare hvor de finnes.
- Styrker den semantiske delen av nasjonal datadeling og gjenbruk.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Semantisk kvalitet | Begreper kan være uklare, overlappende eller for svakt definert | Faglig kvalitetssikring, standard og sammenligningsmuligheter |
| Organisatorisk | Lav publiseringsgrad gir begrenset verdi på tvers av virksomheter | Innføringsstøtte, veiledning og bedre forankring hos datatilbydere |
| Datastyring | Begrepsforvaltning kan bli løsrevet fra øvrig informasjonsforvaltning | Tydelig kobling til modeller, datasett og API-er |
| Brukeropplevelse | Katalogen kan oppleves som for fagspesialisert eller teoretisk | Tydeligere beskrivelser, veiledning og god søkbarhet |
| Avgrensning | Brukere kan forveksle Begrepskatalog med hele Felles datakatalog eller med lokal terminologiforvaltning | Klar produktbeskrivelse og tydelig rolle i katalogfamilien |

## Kanaler
- Begrepskatalogen: https://data.norge.no/catalogs/concepts
- data.norge.no, om løsningen: https://data.norge.no/about
- data.norge.no, teknisk dokumentasjon: https://data.norge.no/nb/technical
- Digdir, Felles datakatalog: https://www.digdir.no/felleslosninger/felles-datakatalog/790
- Samarbeidsportalen, Felles datakatalog: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616

## Plattform
Begrepskatalog er en spesialisert delkatalog for standardisert publisering og oppslag av begreper, med synlig brukerflate på data.norge.no og plass i den samlede katalogarkitekturen til Felles datakatalog.

**Fakta:** Produktet bygger på en dokumentert standard for begrepsbeskrivelser og inngår i flyten fra registrering til portal som data.norge.no beskriver i sin tekniske dokumentasjon.

**Ikke offentlig dokumentert i brukte kilder:** Full intern teknisk arkitektur, driftsoppsett og detaljert komponentmodell for akkurat denne delkatalogen.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet kan brukes av mange virksomheter som felles semantisk referanse.
- Det er særlig relevant når behovet er å forklare og sammenligne begreper, ikke bare å finne datasett eller API-er.
- Verdien øker når begreper kobles til andre dataressurser i Felles datakatalog.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** støttes ved at data kan forstås bedre når begrepene er beskrevet og delbare.
- **P5: Del og gjenbruk løsninger** styrkes ved at mange virksomheter kan bruke samme begrepskatalog i stedet for lokale særordninger.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi felles begrepsforståelse er en forutsetning for samhandling på tvers.
- **P7: Sørg for tillit til oppgaveløsningen** styrkes indirekte ved at begreper blir tydeligere og mindre tvetydige, men produktet er ikke en sikkerhets- eller autorisasjonsløsning.

## Finansiering
- **Fakta:** Offentlig detaljert finansieringsmodell for Begrepskatalog som egen delkatalog er ikke verifisert i denne arbeidsøkten.
- **Fakta:** Produktet framstår som del av Digdirs forvaltning av Felles datakatalog og data.norge.no.
- **Deduksjon:** Finansieringen er trolig samlet under Digdirs produktområde for Felles datakatalog, mens virksomhetene dekker egne kostnader ved å etablere og vedlikeholde begrepsbeskrivelser.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | data.norge.no og Digdir |
| Drifts- og forvaltningsansvar | Digdir forvalter katalogområdet og nettstedet | data.norge.no og Digdir |
| Budsjett- og kostnadsmodell | Ikke offentlig spesifisert som egen delkatalog i brukte kilder | Ingen detaljert offentlig modell verifisert |
| Styringsmodell | Del av Felles datakatalog og Digdirs arbeid med informasjonsforvaltning | Digdir og data.norge.no |

## Lenke til dokumentasjon
- https://data.norge.no/catalogs/concepts
- https://data.norge.no/about
- https://data.norge.no/nb/technical
- https://www.digdir.no/felleslosninger/felles-datakatalog/790
- https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/produkter/produktbeskrivelser/14-Begrepskatalog-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://data.norge.no/catalogs/concepts (kontrollert 2026-03-27)
- Nettkilde: https://data.norge.no/about (kontrollert 2026-03-27)
- Nettkilde: https://data.norge.no/nb/technical (kontrollert 2026-03-27)
- Nettkilde: https://www.digdir.no/felleslosninger/felles-datakatalog/790 (kontrollert 2026-03-27)
- Nettkilde: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616 (kontrollert 2026-03-27)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen bygger nå på oppdatert kildekontroll i data.norge.no, teknisk dokumentasjon og Digdirs produktinformasjon.
- Produktet er tydelig avgrenset som delkatalog for begreper, ikke som hele Felles datakatalog eller som generell ontologiplattform.
- Uverifiserte påstander om kostnader, RDF-eksport, AI-planer og store gevinstanslag er tatt ut.

### Tekstlige forbedringer
- Dokumentet starter ikke lenger med målgruppelinje, og språket er strammet inn mot faktisk dokumentert produktrolle.
- `Hovedfunksjoner` forklarer nå både publisering, søk, sammenligning og rollen som semantisk grunnlag.
- Scope og avgrensning gjør skillet tydeligere mot Felles datakatalog, data.norge.no og lokale fagmiljøers begrepsarbeid.
