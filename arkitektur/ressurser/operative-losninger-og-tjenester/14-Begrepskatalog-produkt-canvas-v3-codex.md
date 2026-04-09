# Produkt-canvas: Begrepskatalog

## Navn
Begrepskatalog

## Ressurs ID
DIGDIR-012

## Status/Livsfase
**Produksjon** - etablert nasjonal delkatalog for publisering, sÃ¸k og sammenligning av begreper i offentlig sektor.

**Fakta:** data.norge.no beskriver Begrepskatalogen som en del av katalogtilbudet og forklarer at formÃ¥let er Ã¥ gjÃ¸re data mer forstÃ¥elige. Alle publiserte begreper fÃ¸lger forvaltningsstandarden `SKOS-AP-NO-Begrep`, og lÃ¸sningen gjÃ¸r det mulig Ã¥ finne, lese og sammenligne begreper pÃ¥ tvers av virksomheter.

## Modenhet
**HÃ¸y modenhet** - tydelig avgrenset og innarbeidet del av Felles datakatalog:
- Produktet er i operativ bruk som nasjonal katalog for begrepsbeskrivelser.
- Det finnes bÃ¥de synlig brukerflate, teknisk dokumentasjon og publiseringsveiledning.
- Begrepskatalogen er tett integrert i Felles datakatalog, men har en tydelig egen rolle som semantisk delkatalog.
- Standarden for begrepsbeskrivelser er eksplisitt dokumentert og gir et mer stabilt grunnlag enn rene fritekstbeskrivelser.

**Deduksjon:** Modenheten er hÃ¸y fordi produktet har en klar og varig funksjon i informasjonsforvaltning, men nytteverdien avhenger fortsatt av at virksomhetene faktisk beskriver egne begreper godt nok.

## Kort beskrivelse
Begrepskatalog er den nasjonale delkatalogen for Ã¥ beskrive og synliggjÃ¸re begreper som brukes i offentlig sektor. Produktet gjÃ¸r det mulig Ã¥ publisere begrepsbeskrivelser etter en felles standard, sÃ¸ke i dem, sammenligne begreper og bruke dem som semantisk grunnlag for datasett, API-er og informasjonsmodeller. LÃ¸sningen er en del av Felles datakatalog, men skiller seg fra den overordnede katalogen ved Ã¥ vÃ¦re spesialisert pÃ¥ begrepsforstÃ¥else og semantisk avklaring.

## Kapabiliteter
- **Informasjonsforvaltning: Datastyring** stÃ¸tter forvaltning av begreper som en del av virksomhetenes samlede informasjonsforvaltning.
- **Informasjonsforvaltning: Informasjonsarkitektur** gir et semantisk grunnlag som kan brukes i modeller, API-er og databeskrivelser.
- **Informasjonsforvaltning: Oversikt over begreper** er produktets kjernefunksjon ved at begreper kan publiseres, sÃ¸kes opp og sammenlignes.
- **Standardisering: Forvaltningsstandarder** bygger pÃ¥ felles standard for begrepsbeskrivelser og gjÃ¸r innholdet mer sammenlignbart og gjenbrukbart.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot data.norge.no, teknisk dokumentasjon og Digdirs sider om Felles datakatalog.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Begrepskatalogen pÃ¥ data.norge.no, teknisk dokumentasjon for data.norge.no og Digdir-sidene for Felles datakatalog.

Dokumenterte mÃ¥l:
- GjÃ¸re data mer forstÃ¥elige ved Ã¥ gi begreper tydelige beskrivelser og definisjoner.
- GjÃ¸re det mulig Ã¥ publisere begreper etter en felles standard.
- GjÃ¸re begreper sÃ¸kbare og sammenlignbare pÃ¥ tvers av virksomheter.

Operative mÃ¥l utledet fra de samme kildene:
- Redusere semantiske misforstÃ¥elser nÃ¥r data deles eller brukes pÃ¥ tvers.
- Gi datatilbydere og arkitekter et felles sted for Ã¥ beskrive hva sentrale termer betyr.
- Styrke koblingen mellom begreper og andre dataressurser i Felles datakatalog.

## Brukerbehov
- Virksomheter trenger en felles mÃ¥te Ã¥ publisere og vedlikeholde begrepsbeskrivelser pÃ¥.
- Arkitekter og informasjonsforvaltere trenger semantisk avklaring nÃ¥r de lager modeller, API-er og databeskrivelser.
- Datakonsumenter trenger Ã¥ forstÃ¥ hva sentrale begreper betyr fÃ¸r de vurderer eller bruker data.
- ForvaltningsmiljÃ¸er trenger en lÃ¸sning som gjÃ¸r det lettere Ã¥ etablere mer konsistent terminologi pÃ¥ tvers av virksomheter.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Begrepsansvarlige i virksomheter | Publisere og vedlikeholde begrepsbeskrivelser | Faglig og semantisk forvaltning | PrimÃ¦rbruker pÃ¥ publiseringssiden |
| Arkitekter og informasjonsforvaltere | Finne og sammenligne begreper | Informasjonsarkitektur, modellering og datadeling | Bruker katalogen som semantisk referanse |
| Utviklere og integrasjonsteam | ForstÃ¥ sentrale termer i data og API-er | Implementasjon og integrasjon | MÃ¸ter ofte produktet indirekte via andre kataloger |
| Datakonsumenter og analytikere | Tolke data riktig | Analyse, gjenbruk og vurdering av datakilder | Har behov for mer enn bare tekniske metadata |
| Digdir og forvaltningsmiljÃ¸er | Forvalte standard, veiledning og produktutvikling | Drift, dokumentasjon og videreutvikling | BÃ¦rer produktansvaret |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
**Publisering av begrepsbeskrivelser etter felles standard.** Produktet gjÃ¸r det mulig Ã¥ beskrive begreper pÃ¥ en strukturert mÃ¥te, med definisjon, term, gyldighet, kontaktinformasjon og andre relevante metadata. Dette er viktig fordi lÃ¸sningen ikke bare er et oppslagsverk, men et standardisert publiseringslÃ¸p for semantisk informasjon.

**SÃ¸k, oppslag og sammenligning av begreper.** Begrepskatalogen gir en egen brukerflate for Ã¥ finne begreper og sammenligne flere begreper ved siden av hverandre. Det gjÃ¸r lÃ¸sningen nyttig nÃ¥r ulike virksomheter bruker like eller lignende ord pÃ¥ forskjellige mÃ¥ter, og nÃ¥r brukeren trenger Ã¥ avklare hvilket begrep som faktisk passer best.

**Maskinlesbar og gjenbrukbar semantikk.** Begrepsbeskrivelser fÃ¸lger `SKOS-AP-NO-Begrep`, som gjÃ¸r dem mer egnet for gjenbruk i andre kataloger og lÃ¸sninger. Produktet er derfor ikke bare laget for mennesker som leser definisjoner, men ogsÃ¥ for mer strukturert gjenbruk av begrepsinformasjon i det nasjonale dataÃ¸kosystemet.

**Semantisk kobling til resten av Felles datakatalog.** Begrepskatalogen er en spesialisert delkatalog innenfor et stÃ¸rre produktomrÃ¥de. Den har verdi alene, men den fÃ¥r stÃ¸rst effekt nÃ¥r begrepene brukes sammen med datasett, API-er og informasjonsmodeller. Det gjÃ¸r den til en semantisk grunnmur heller enn en fullstendig datakatalog i seg selv.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Publisering og sÃ¸k i begrepsbeskrivelser | Full forvaltning av datasett, API-er eller informasjonsmodeller |
| Sammenligning av begreper og semantisk avklaring | Selve implementasjonen av begreper i lokale systemer |
| Bruk av forvaltningsstandard for begrepsbeskrivelser | Automatisk harmonisering av terminologi pÃ¥ tvers uten faglig arbeid |
| Delkatalog for begreper innenfor Felles datakatalog | Felles datakatalog som overordnet produktomrÃ¥de |
| Semantisk grunnlag for andre kataloger og beskrivelser | Juridisk autorisasjon eller styring av datatilgang |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-27):**
- Produktet har egen katalogflate, teknisk dokumentasjon og publiseringsstandard.
- data.norge.no viser at begrepskatalogen inngÃ¥r i et bredere katalogomrÃ¥de med flere relaterte ressurskategorier.

**Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Detaljert og tidsfestet veikart for ny funksjonalitet er ikke hentet ut.

**Deduksjon:** Videreutviklingen vil trolig dreie seg om bedre publiseringsflyt, sterkere sammenheng med andre kataloger og bedre stÃ¸tte for sammenligning og gjenbruk av begreper.

## Forretningsverdi/Verdiforslag
### For virksomheter
- GjÃ¸r det enklere Ã¥ beskrive sentrale fagbegreper pÃ¥ en mÃ¥te andre kan forstÃ¥ og gjenbruke.
- Reduserer behovet for at hver virksomhet bygger egne, isolerte begrepsoversikter.
- Gir bedre grunnlag for mer konsistent begrepsbruk i dokumentasjon og datadeling.

### For arkitektur- og utviklingsmiljÃ¸er
- Gir en felles semantisk referanse for modeller, API-er og dataressurser.
- Reduserer risikoen for misforstÃ¥elser nÃ¥r like ord brukes forskjellig i ulike sammenhenger.
- Styrker koblingen mellom forretningsbegreper og tekniske beskrivelser.

### For offentlig sektor
- UnderstÃ¸tter mer sammenhengende informasjonsforvaltning pÃ¥ tvers av virksomheter.
- Bidrar til bedre forstÃ¥else av hva data betyr, ikke bare hvor de finnes.
- Styrker den semantiske delen av nasjonal datadeling og gjenbruk.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Semantisk kvalitet | Begreper kan vÃ¦re uklare, overlappende eller for svakt definert | Faglig kvalitetssikring, standard og sammenligningsmuligheter |
| Organisatorisk | Lav publiseringsgrad gir begrenset verdi pÃ¥ tvers av virksomheter | InnfÃ¸ringsstÃ¸tte, veiledning og bedre forankring hos datatilbydere |
| Datastyring | Begrepsforvaltning kan bli lÃ¸srevet fra Ã¸vrig informasjonsforvaltning | Tydelig kobling til modeller, datasett og API-er |
| Brukeropplevelse | Katalogen kan oppleves som for fagspesialisert eller teoretisk | Tydeligere beskrivelser, veiledning og god sÃ¸kbarhet |
| Avgrensning | Brukere kan forveksle Begrepskatalog med hele Felles datakatalog eller med lokal terminologiforvaltning | Klar produktbeskrivelse og tydelig rolle i katalogfamilien |

## Kanaler
- Begrepskatalogen: https://data.norge.no/catalogs/concepts
- data.norge.no, om lÃ¸sningen: https://data.norge.no/about
- data.norge.no, teknisk dokumentasjon: https://data.norge.no/nb/technical
- Digdir, Felles datakatalog: https://www.digdir.no/felleslosninger/felles-datakatalog/790
- Samarbeidsportalen, Felles datakatalog: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616

## Plattform
Begrepskatalog er en spesialisert delkatalog for standardisert publisering og oppslag av begreper, med synlig brukerflate pÃ¥ data.norge.no og plass i den samlede katalogarkitekturen til Felles datakatalog.

**Fakta:** Produktet bygger pÃ¥ en dokumentert standard for begrepsbeskrivelser og inngÃ¥r i flyten fra registrering til portal som data.norge.no beskriver i sin tekniske dokumentasjon.

**Ikke offentlig dokumentert i brukte kilder:** Full intern teknisk arkitektur, driftsoppsett og detaljert komponentmodell for akkurat denne delkatalogen.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet kan brukes av mange virksomheter som felles semantisk referanse.
- Det er sÃ¦rlig relevant nÃ¥r behovet er Ã¥ forklare og sammenligne begreper, ikke bare Ã¥ finne datasett eller API-er.
- Verdien Ã¸ker nÃ¥r begreper kobles til andre dataressurser i Felles datakatalog.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** stÃ¸ttes ved at data kan forstÃ¥s bedre nÃ¥r begrepene er beskrevet og delbare.
- **P5: Del og gjenbruk lÃ¸sninger** styrkes ved at mange virksomheter kan bruke samme begrepskatalog i stedet for lokale sÃ¦rordninger.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** stÃ¸ttes fordi felles begrepsforstÃ¥else er en forutsetning for samhandling pÃ¥ tvers.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** styrkes indirekte ved at begreper blir tydeligere og mindre tvetydige, men produktet er ikke en sikkerhets- eller autorisasjonslÃ¸sning.

## Finansiering
- **Fakta:** Offentlig detaljert finansieringsmodell for Begrepskatalog som egen delkatalog er ikke verifisert i denne arbeidsÃ¸kten.
- **Fakta:** Produktet framstÃ¥r som del av Digdirs forvaltning av Felles datakatalog og data.norge.no.
- **Deduksjon:** Finansieringen er trolig samlet under Digdirs produktomrÃ¥de for Felles datakatalog, mens virksomhetene dekker egne kostnader ved Ã¥ etablere og vedlikeholde begrepsbeskrivelser.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | data.norge.no og Digdir |
| Drifts- og forvaltningsansvar | Digdir forvalter katalogomrÃ¥det og nettstedet | data.norge.no og Digdir |
| Budsjett- og kostnadsmodell | Ikke offentlig spesifisert som egen delkatalog i brukte kilder | Ingen detaljert offentlig modell verifisert |
| Styringsmodell | Del av Felles datakatalog og Digdirs arbeid med informasjonsforvaltning | Digdir og data.norge.no |

## Lenke til dokumentasjon
- https://data.norge.no/catalogs/concepts
- https://data.norge.no/about
- https://data.norge.no/nb/technical
- https://www.digdir.no/felleslosninger/felles-datakatalog/790
- https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/14-Begrepskatalog-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://data.norge.no/catalogs/concepts (kontrollert 2026-03-27)
- Nettkilde: https://data.norge.no/about (kontrollert 2026-03-27)
- Nettkilde: https://data.norge.no/nb/technical (kontrollert 2026-03-27)
- Nettkilde: https://www.digdir.no/felleslosninger/felles-datakatalog/790 (kontrollert 2026-03-27)
- Nettkilde: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616 (kontrollert 2026-03-27)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen bygger nÃ¥ pÃ¥ oppdatert kildekontroll i data.norge.no, teknisk dokumentasjon og Digdirs produktinformasjon.
- Produktet er tydelig avgrenset som delkatalog for begreper, ikke som hele Felles datakatalog eller som generell ontologiplattform.
- Uverifiserte pÃ¥stander om kostnader, RDF-eksport, AI-planer og store gevinstanslag er tatt ut.

### Tekstlige forbedringer
- Dokumentet starter ikke lenger med mÃ¥lgruppelinje, og sprÃ¥ket er strammet inn mot faktisk dokumentert produktrolle.
- `Hovedfunksjoner` forklarer nÃ¥ bÃ¥de publisering, sÃ¸k, sammenligning og rollen som semantisk grunnlag.
- Scope og avgrensning gjÃ¸r skillet tydeligere mot Felles datakatalog, data.norge.no og lokale fagmiljÃ¸ers begrepsarbeid.

