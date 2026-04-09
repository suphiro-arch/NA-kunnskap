# Produkt-canvas: Helsenorge

## Navn
Helsenorge

## Ressurs ID
NHN-001

## Status/Livsfase
**Produksjon** - etablert nasjonal innbyggerportal for informasjon om og tilgang til digitale helsetjenester.

**Fakta:** Helsenorge beskrives som den offentlige nettportalen for informasjon om og tilgang til helsetjenester for innbyggere i Norge. Norsk helsenett har ansvar for drift og utvikling av nettstedet, mens innhold og tjenester leveres av flere aktÃ¸rer i helsesektoren.

## Modenhet
**HÃ¸y modenhet** - nasjonal og bredt innarbeidet innbyggertjeneste:
- Helsenorge er etablert som den felles inngangen til mange digitale helsetjenester for innbyggere.
- Produktet kombinerer informasjonstjenester og innloggede selvbetjeningslÃ¸sninger.
- Innhold og funksjoner kommer fra flere offentlige helseaktÃ¸rer og sykehus.
- Portalen brukes som felles presentasjonslag for flere nasjonale e-helselÃ¸sninger.

**Deduksjon:** Modenheten er hÃ¸y fordi Helsenorge er en stabil og sentral innbyggerflate i helsesektoren, men gjenbruksverdien ligger mer i samordnet tjenestetilgang enn i tekniske byggeklosser for andre sektorer.

## Kort beskrivelse
Helsenorge er den nasjonale portalen der innbyggere finner kvalitetssikret helseinformasjon og fÃ¥r tilgang til digitale selvbetjeningslÃ¸sninger i helse- og omsorgssektoren. Produktet samler tjenester fra flere aktÃ¸rer i Ã©n felles inngang, slik at brukeren kan orientere seg, logge inn og utfÃ¸re helseadministrative oppgaver uten Ã¥ forholde seg til hvert enkelt underliggende system. Helsenorge er derfor fÃ¸rst og fremst en sammenhengende tjenesteflate for innbyggere, ikke en generell delingsplattform.

## Kapabiliteter
- **Sluttbrukertjenester: Sammenhengende tjenester** er relevant fordi Helsenorge samler flere helsetjenester og informasjonslÃ¸p i Ã©n felles inngang for innbyggere.
- **Sluttbrukertjenester: Tjenestekjeder** er relevant fordi brukeren kan bevege seg mellom informasjon, innlogging og flere ulike helserelaterte tjenester innen samme overordnede produktflate.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Helsenorges egen om-side og NHNs rollebeskrivelse.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Helsenorges side `Om Helsenorge` og NHNs overordnede tjenestebeskrivelser.

Dokumenterte mÃ¥l:
- Gi innbyggere tilgang til informasjon om helse, livsstil, sykdom, behandling og rettigheter.
- Gi innbyggere tilgang til digitale selvbetjeningslÃ¸sninger og helseopplysninger som er registrert om dem.
- Samle innhold og tjenester fra ulike aktÃ¸rer i helsesektoren pÃ¥ ett sted.

Operative mÃ¥l utledet fra de samme kildene:
- GjÃ¸re digitale helsetjenester enklere Ã¥ finne og bruke for innbyggerne.
- Skape en felles og gjenkjennelig inngang til nasjonale og sektorvise helsetjenester.
- Redusere behovet for at innbyggerne mÃ¥ orientere seg i mange ulike portaler og virksomhetsflater.

## Brukerbehov
- Innbyggere trenger Ã©n samlet inngang til helseinformasjon og digitale helsetjenester.
- Brukere trenger trygg tilgang til egne helseopplysninger og selvbetjeningsfunksjoner.
- Offentlige helseaktÃ¸rer trenger en felles innbyggerflate for Ã¥ presentere innhold og tjenester.
- Helseforvaltningen trenger en kanal som kan gjÃ¸re sektoren mer sammenhengende og brukervennlig.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Innbyggere | Oversikt, informasjon og digital tilgang til helsetjenester | Informasjon, innsyn og selvbetjening | HovedmÃ¥lgruppen |
| Pasienter og pÃ¥rÃ¸rende | Tilgang til egne eller relevante helseopplysninger | OppfÃ¸lging, planlegging og kommunikasjon | Viktig brukergruppe for innloggede tjenester |
| Offentlige helseaktÃ¸rer | Felles kanal mot innbygger | Publisering av tjenester og innhold | Leverer innhold og funksjoner inn i produktet |
| Norsk helsenett | Drift, utvikling og forvaltning | Nasjonal produkt- og plattformforvaltning | Operativ hovedforvalter |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
**Samlet innbyggerinngang til helsetjenester.** Helsenorge gir innbyggerne ett sted Ã¥ gÃ¥ til for bÃ¥de informasjon og digitale tjenester i helsesektoren. Dette er produktets hovedverdi og viktigste avgrensning.

**Kvalitetssikret helseinformasjon.** Portalen publiserer informasjon om helse, behandling, rettigheter og livsstil som leveres og kvalitetssikres av offentlige helseaktÃ¸rer og sykehus. Helsenorge er derfor ogsÃ¥ en nasjonal informasjonskanal.

**Innlogget selvbetjening og innsyn.** Ved innlogging fÃ¥r brukeren tilgang til selvbetjeningslÃ¸sninger og innsyn i helseopplysninger. Helsenorge fungerer dermed som presentasjons- og tilgangsflate for flere underliggende tjenester.

**Sammenkobling av tjenester fra flere aktÃ¸rer.** Produktet samler bidrag fra flere virksomheter i helsesektoren i en felles brukerflate. Dette gjÃ¸r Helsenorge til en sammenhengende tjenesteflate heller enn en enkeltstÃ¥ende applikasjon.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Nasjonal portal for helseinformasjon og digitale helsetjenester | De underliggende fagsystemene og registrene som leverer data |
| Innlogget innbyggerflate for selvbetjening og innsyn | Teknisk API-plattform for generell datadeling pÃ¥ tvers av sektorer |
| Presentasjon og sammenkobling av tjenester fra flere helseaktÃ¸rer | Alle nasjonale e-helselÃ¸sninger som egne produkter |
| Kvalitetssikret innhold for innbyggere | Helsepersonellflater og rent interne arbeidsverktÃ¸y |

## Veikart over kommende funksjonalitet
**Fakta fra kildene (kontrollert 2026-03-27):**
- Helsenorge framstÃ¥r som en lÃ¸pende utviklet portal med stadig nye selvbetjeningslÃ¸sninger.
- NHN beskriver flere nasjonale tjenester som eksponeres mot innbyggere via Helsenorge.

**Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Et samlet og tidsfestet veikart for hele Helsenorge er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til Ã¥ dreie seg om flere innbyggernÃ¦re tjenester, sterkere sammenkobling med nasjonale e-helselÃ¸sninger og gradvis utvidelse av selvbetjeningsomrÃ¥det.

## Forretningsverdi/Verdiforslag
### For innbyggere
- Gir Ã©n gjenkjennelig inngang til informasjon og digitale helsetjenester.
- GjÃ¸r det enklere Ã¥ finne og bruke relevante tjenester i helsesektoren.

### For helseaktÃ¸rer
- Gir en felles kanal mot innbygger i stedet for mange separate innganger.
- Styrker muligheten for sammenhengende tjenester pÃ¥ tvers av virksomheter.

### For sektoren
- Bidrar til mer samordnet digital brukeropplevelse.
- Reduserer fragmentering i mÃ¸teflaten mot innbygger.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Kompleksitet | Mange aktÃ¸rer og tjenester i samme portal kan gjÃ¸re styring og prioritering krevende | Tydelig produktforvaltning og sektorstyring |
| Brukeropplevelse | Ujevn kvalitet mellom underliggende tjenester kan slÃ¥ ut i den samlede opplevelsen | Felles design- og tjenestekrav |
| Teknisk avhengighet | Feil i underliggende lÃ¸sninger kan merkes direkte i Helsenorge | Robust integrasjon og tydelig ansvar mellom aktÃ¸rene |
| Personvern og tillit | Portalen hÃ¥ndterer innsyn i sensitive helseopplysninger | HÃ¸y sikkerhet, tydelig tilgangsstyring og god informasjon |
| Scope-glidning | Helsenorge kan oppfattes som Ã©n lÃ¸sning selv om mange produkter ligger under | Tydelig produktavgrensning og sporbarhet til underliggende tjenester |

## Kanaler
- Helsenorge: https://www.helsenorge.no/
- Om Helsenorge: https://www.helsenorge.no/om-helsenorge-no/
- Norsk helsenett - tjenesteoversikt: https://www.nhn.no/tjenester/

## Plattform
Helsenorge er en nasjonal portal- og tjenesteflate for innbyggere i helsesektoren.

**Fakta:** Produktet bestÃ¥r av bÃ¥de Ã¥pne informasjonssider og innloggede selvbetjeningslÃ¸sninger, og brukes som felles mÃ¸teflate mellom innbygger og flere underliggende helsetjenester.

**Ikke offentlig dokumentert i brukte kilder:** Full intern plattformarkitektur, samlet komponentkart og detaljert oversikt over alle underliggende tekniske grensesnitt.

## Gjenbruk
**Middels til hÃ¸y gjenbruksverdi:**
- Produktet har hÃ¸y verdi som felles innbyggerflate i helsesektoren.
- Det er sÃ¦rlig relevant nÃ¥r behovet er sammenhengende brukeropplevelse og felles kanal mot innbyggere.
- Det er mindre relevant som generell teknisk byggekloss for andre sektorer, fordi hovedverdien ligger i sluttbrukerflaten.

## StÃ¸tter arkitekturprinsipper
- **P5: Del og gjenbruk lÃ¸sninger** styrkes ved at flere helseaktÃ¸rer bruker samme innbyggerflate.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** stÃ¸ttes fordi Helsenorge binder sammen tjenester fra flere aktÃ¸rer i Ã©n brukerreise.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** er sentralt fordi produktet mÃ¥ hÃ¥ndtere sensitive helseopplysninger og hÃ¸y brukerforventning.

## Finansiering
- **Fakta:** Kildene beskriver NHN som ansvarlig for drift og utvikling, men gir ikke en samlet offentlig finansieringsmodell i denne arbeidsÃ¸kten.
- **Deduksjon:** Helsenorge finansieres som en nasjonal fellestjeneste i helsesektoren, kombinert med bidrag og tilknytning fra flere tjenesteeiere.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Norsk helsenett | Om-siden for Helsenorge |
| Drifts- og utviklingsansvar | Norsk helsenett | Om-siden beskriver dette eksplisitt |
| Innholds- og tjenestebidrag | Flere offentlige helseaktÃ¸rer og sykehus | Helsenorge beskriver dette eksplisitt |
| Styringsmodell | Felles innbyggerflate i helsesektoren med NHN som operativ forvalter | Om-siden og tjenestebeskrivelsen |

## Lenke til dokumentasjon
- https://www.helsenorge.no/
- https://www.helsenorge.no/om-helsenorge-no/
- https://www.nhn.no/tjenester/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.helsenorge.no/ (kontrollert 2026-03-27)
- Nettkilde: https://www.helsenorge.no/om-helsenorge-no/ (kontrollert 2026-03-27)
- Nettkilde: https://www.nhn.no/tjenester/ (kontrollert 2026-03-27)

