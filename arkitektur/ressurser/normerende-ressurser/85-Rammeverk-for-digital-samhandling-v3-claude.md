# Rammeverk for digital samhandling

## Navn
Rammeverk for digital samhandling

## Ressurs ID
DIGDIR-025

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Rammeverk

## Status/Livsfase
Aktiv.

**Fakta:** Digdir publiserer rammeverket på digdir.no, med siste endring 21. august 2025. Rammeverket er Norges nasjonale rammeverk for interoperabilitet (NIF), som Norge forpliktet seg til å etablere da Tallinn-erklæringen ble undertegnet i 2017, og det ble først utarbeidet som Skate-tiltak i 2018. Veiledningen for praktisk bruk og modellen for felles økosystem ble sist endret i august 2025.

**Ikke offentlig dokumentert i denne arbeidsøkten:** Versjonsnummer, endringslogg og hva som ble endret i 2025.

## Kort beskrivelse
Rammeverk for digital samhandling viser hvordan offentlige virksomheter kan arbeide systematisk for at digitale tjenester skal kunne integreres, gjenbrukes og inngå i sammenhengende tjenester på tvers av virksomheter, sektorer og forvaltningsnivåer. Det er den norske utgaven av European Interoperability Framework (EIF).

Rammeverket gjør digital samhandling bredere enn teknisk integrasjon. Det beskriver fem samhandlingsområder: juridisk, organisatorisk, semantisk og teknisk samhandling, og styring og forvaltning, som går på tvers av de fire andre. Rammeverket består av de overordnede arkitekturprinsippene med anbefalinger, en lagdelt modell for digital samhandling, en konseptuell modell for styring og forvaltning og en veiledning for praktisk bruk.

## Formål og normerende rolle
Formålet er å gi offentlig sektor et felles strukturgrunnlag for digital samhandling. Rammeverket skal redusere fragmentering, lokale særmønstre og uklare ansvarsforhold ved å gi virksomheter et felles språk for behov, avhengigheter, prinsipper og arkitekturvalg.

Den normerende rollen er veiledende. Rammeverket er ikke en teknisk spesifikasjon og velger ikke standarder eller løsninger. Det skal brukes når en ny eller endret tjeneste kan få juridiske, organisatoriske, semantiske eller tekniske konsekvenser for andre aktører.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er **anbefalt**, med delvis forankring i Digitaliseringsrundskrivet. Ingen lov eller forskrift pålegger bruk av rammeverket.

**Fakta:** Digitaliseringsrundskrivet (D-2/25) punkt 1.11 anbefaler at statlige virksomheter bruker norsk arkitekturrammeverk for samhandling ved utvikling av samhandlingsløsninger. Digdir fører dette som en anbefaling for både stat og kommune i sin oversikt over krav og anbefalinger. Samme punkt krever at virksomheten følger de overordnede arkitekturprinsippene, som Digdir regner som en del av rammeverket, og at avvik dokumenteres og begrunnes.

**Deduksjon:** Rammeverket har dermed to forpliktelsesnivåer. Prinsippdelen er et krav for statlige forvaltningsorganer gjennom rundskrivet, som er en instruks og ikke lov eller forskrift. Resten av rammeverket, med lagmodellen, styringsmodellen og framgangsmåten, er anbefalt. For kommunesektoren er begge delene anbefalinger. Prinsippene er beskrevet som egen ressurs, se `DIGDIR-030`.

Etterlevelse skjer gjennom virksomhetsarkitektur, porteføljestyring, konseptvalg og tverrvirksomhetlige arkitekturbeslutninger. Avvik fra den anbefalte delen er ikke brudd, men bør begrunnes når tiltaket påvirker samhandlingsevne, gjenbruk eller sammenhengende tjenester.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Digdirs sider om rammeverket, modellen for felles økosystem og veiledningen for praktisk bruk.

`Juridisk samhandling: Regelverkstolkning` er vurdert og ikke koblet. Rammeverket sier at det rettslige grunnlaget må være på plass før aktører samhandler, men tilbyr ingen tolkning av regelverk selv. `Datautveksling og integrasjon: Dele data med andre` og `Standardisering: Forvaltningsstandarder` er heller ikke koblet: rammeverket omtaler datadeling og standardisering som hensyn i lagmodellen, men tilgjengeliggjør ikke data og velger ikke standarder. Standardvalget hører til Referansekatalogen (`DIGDIR-026`).

- **Strategisk styring: Arkitekturstyring**
  Rammeverket er det felles nasjonale rammeverket som binder de overordnede arkitekturprinsippene, lagmodellen for samhandling og modellen for styring og forvaltning sammen, og som norsk implementering av EIF er det rammeverket nasjonal arkitektur skal bygges innenfor. Koblingen gjelder rammeverket som felles arkitekturgrunnlag; styringen av etterlevelse skjer gjennom Digitaliseringsrundskrivet og arkitekturrådene.
- **Samarbeid: Organisatorisk samhandling**
  Organisatorisk samhandling er ett av de fem samhandlingsområdene i lagmodellen, og rammeverket beskriver den som tilpasning av tjenestekjeder og forretningsprosesser på tvers av virksomheter. Framgangsmåten for praktisk bruk krever at konsekvensene for samarbeidende virksomheter kartlegges og forankres hos tredjeparter før endringen gjennomføres.
- **Veiledning: Utvikling og formidling av veiledning**
  Rammeverket er Digdirs publiserte veiledning for digital samhandling, med prinsipper, modeller og en framgangsmåte i fire steg for å bruke dem i konkrete endringer.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Ledelse og porteføljestyring | Bedre beslutningsgrunnlag for tiltak som berører flere aktører | Prioritering, styring og samordning | Bør brukes tidlig, før løsningsretning låses |
| Arkitekter og fagmiljøer | Felles struktur for juridisk, organisatorisk, semantisk og teknisk samhandling | Målarkitektur og kvalitetssikring | Kjernebrukere |
| Prosjekt- og produktmiljøer | Tydelig retning for krav og løsningsvalg | Konseptvalg, anskaffelser og utviklingsløp | Må kobles til konkrete referansearkitekturer og standarder |
| Juridiske og sikkerhetsfaglige miljøer | Felles inngang til ansvar, hjemmel, risiko og etterlevelse | Tidligfase, kravarbeid og avviksvurdering | Særlig ved deling av data og tverrvirksomhetlige prosesser |
| Samhandlingsarenaer og forvaltningsmiljøer | Felles språk for koordinering og videreutvikling | Styringsdialog, felles veikart og porteføljeoppfølging | Ved varig forvaltning |

## Normerende innhold
Rammeverket består av fire deler:

- **Overordnede arkitekturprinsipper med anbefalinger.** De sju prinsippene er beskrevet som egen ressurs (`DIGDIR-030`).
- **Lagdelt modell for digital samhandling.** Modellen har fem samhandlingsområder. Juridisk samhandling skal sikre at virksomheter som arbeider under ulikt regelverk kan samhandle, og at det rettslige grunnlaget er på plass. Organisatorisk samhandling gjelder tilpasning av tjenestekjeder og forretningsprosesser. Semantisk samhandlingsevne gjelder betydningen av data og formater. Teknisk samhandlingsevne gjelder systemintegrasjon og standardisering. Styring og forvaltning går på tvers av de fire.
- **Modell for felles økosystem.** Modellen viser aktører, rammebetingelser og delte ressurser som tekniske løsninger og standarder, og hvordan kommunal, statlig, privat og frivillig sektor må samspille for å levere integrerte tjenester. Den legger til grunn at styring bare kan skje gjennom rammebetingelsene.
- **Veiledning for praktisk bruk.** Framgangsmåten har fire steg: vurdere om endringen krever samhandling på tvers, kartlegge behov, utfordringer og muligheter på de fire nivåene, bekrefte og forankre effekter hos tredjeparter som KS Digital, regionale digitaliseringsnettverk og Arkitektur- og standardiseringsrådet, og utvikle et felles kunnskapsgrunnlag. Veiledningen viser til Kart for tjenestekjeder (`DIGDIR-032`) som verktøy i første steg og til EUs metode for vurdering av interoperabilitet.

## Bruksområde
Rammeverket bør brukes når virksomheter planlegger nye eller endrede tjenester som krever samhandling med andre aktører, deling av data, felles brukerreiser eller koordinert forvaltning på tvers.

Det er særlig nyttig i tidligfase, ved utforming av målarkitektur, når flere virksomheter må etablere felles forståelse av ansvar og retning, eller når lokale tiltak kan få følger for andre.

## Typiske analyse- og beslutningssituasjoner
- Når en endring må vurderes for konsekvenser hos samarbeidende virksomheter, slik første steg i framgangsmåten krever.
- Når flere aktører trenger felles beslutningsgrunnlag for roller, ansvar, data og tekniske mønstre.
- Når et tiltak må velge mellom referansearkitekturer, fellesløsninger eller lokale løsninger.
- Når juridiske, organisatoriske, semantiske og tekniske forhold må vurderes samlet.
- Når risiko for fragmentering, særutvikling eller utydelig forvaltning må vurderes tidlig.

## Når ressursen normalt ikke er tilstrekkelig alene
Rammeverket er ikke tilstrekkelig alene for detaljert metode, implementasjon eller drift. Det må normalt suppleres med:
- referansearkitekturer, for eksempel eMelding, eOppslag og Arkitektur for hendelser
- Referansekatalogen for IT-standarder og tekniske profiler
- juridiske vurderinger og avtaler for datadeling, behandling og ansvar
- metodeverktøy som Kart for tjenestekjeder og Sjekkliste for sammenhengende tjenester
- operative fellesløsninger eller sektorvise løsninger der gjennomføringen krever en konkret plattform

## Scope og avgrensning
Inngår:
- overordnede prinsipper og samhandlingsområder for digital samhandling
- modell for felles økosystem og for styring og forvaltning
- framgangsmåte for å vurdere samhandlingskonsekvenser av en endring

Inngår ikke:
- detaljert teknisk design eller tekniske spesifikasjoner
- valg av standarder, som ligger i Referansekatalogen
- operativ forvaltning av enkeltløsninger
- juridisk avtaleverk eller tolkning av regelverk

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | Digdir publiserer og vedlikeholder rammeverket |
| Endringsprosess | **Fakta:** Rammeverket ble først utarbeidet som Skate-tiltak i 2018. **Ikke offentlig dokumentert i denne arbeidsøkten:** Hvordan endringer i dag besluttes, og om Skate eller Arkitektur- og standardiseringsrådet behandler dem |
| Publiserings- og beslutningsarena | digdir.no |

## Relasjon til andre ressurser
- **Overordnede arkitekturprinsipper for offentlig sektor (`DIGDIR-030`):** del av rammeverket, og den delen som er et krav etter Digitaliseringsrundskrivet.
- **Digitaliseringsrundskrivet (`DIGDIR-044`):** punkt 1.11 anbefaler rammeverket og krever at prinsippene følges.
- **Referansearkitektur forsendelse (eMelding) (`DIGDIR-033`), forespørsel-svar (eOppslag) (`DIGDIR-034`) og Arkitektur for hendelser (`DIGDIR-027`):** samhandlingsmønstre som konkretiserer den tekniske og semantiske samhandlingen.
- **Rammeverk for informasjonsforvaltning (`DIGDIR-029`):** utfyller den semantiske samhandlingen med føringer for data, begreper og metadata.
- **Referansekatalogen for IT-standarder (`DIGDIR-026`):** standardgrunnlaget for den tekniske samhandlingen.
- **Kart for tjenestekjeder (`DIGDIR-032`) og Sjekkliste for sammenhengende tjenester (`DIGDIR-031`):** metodeverktøy, der kartet er verktøyet framgangsmåten viser til i første steg.
- **Skate (`DIGDIR-042`) og Arkitektur- og standardiseringsrådet (`DIGDIR-028`):** Skate var arenaen der rammeverket ble utarbeidet, og rådet er en av tredjepartene framgangsmåten nevner for forankring.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er bedre samordning, mer forutsigbare beslutninger og lavere risiko for at virksomheter utvikler løsninger som ikke virker sammen. Rammeverket kan redusere koordinasjonskostnad og gjøre det tydelig hvilke felles avklaringer som må gjøres før investeringer låses.

Arkitekturverdien er et felles språk for samhandlingsevne som er i samsvar med EIF, slik at norske vurderinger av interoperabilitet kan sammenlignes med europeiske.

## Konsekvens ved manglende bruk eller avvik
Hvis rammeverket ikke brukes, brukes for sent eller tolkes for smalt, øker risikoen for:
- at samhandling vurderes som teknisk integrasjon alene
- uklart eierskap til tjenester, data, beslutninger og forvaltning
- at juridiske og organisatoriske forhold avklares for sent
- lokale mønstre som ikke lar seg gjenbruke eller samordne
- parallelle løsninger, høyere integrasjonskostnader og svakere sammenhengende tjenester

Avvik fra prinsippdelen skal dokumenteres og begrunnes etter Digitaliseringsrundskrivet. Avvik fra resten bør begrunnes når tiltaket påvirker flere aktører, fellesløsninger, datadeling eller brukeropplevelse på tvers.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Forankring | Rammeverket brukes ikke tidlig nok i styringsløp | Sen samordning og svakere effekt | Bruk rammeverket i konseptvalg, porteføljestyring og arkitekturbeslutninger |
| Tolkning | Samhandling tolkes for teknisk | Juridiske, organisatoriske og semantiske forhold avklares for sent | Bruk de fire samhandlingsnivåene som fast sjekkliste |
| Ansvar | Roller og forvaltning mellom aktører er uklare | Uforutsigbar drift, endring og oppfølging | Etabler ansvarskart og forvaltningsmodell før løsning låses |
| Standardisering | Rammeverket brukes uten kobling til konkrete standarder | Uklar gjennomføring | Koble til Referansekatalogen og referansearkitekturene |
| Forpliktelse | Bare prinsippdelen er et krav, og bare for staten | Resten av rammeverket kan velges bort uten begrunnelse | Etterspør dokumentert vurdering i styringsdialog og kvalitetssikring |

## Publiseringsform og tilgjengelighet
Rammeverket publiseres som åpne temasider på digdir.no, med undersider for prinsippene, modellen for felles økosystem og praktisk bruk.

## Støtter arkitekturprinsipper
Rammeverket inneholder selv de sju overordnede arkitekturprinsippene. De tydeligste koblingene utover det er:

- **P6: Lag digitale løsninger som støtter samhandling** er rammeverkets kjerneformål.
- **P2: Ta arkitekturbeslutninger på rett nivå** støttes ved at samhandlingskonsekvenser skal vurderes og forankres hos andre aktører før lokale valg låses.
- **P3: Bidra til digitaliseringsvennlige regelverk** støttes ved at juridisk samhandling er ett av samhandlingsområdene.
- **P4: Del og gjenbruk data** og **P5: Del og gjenbruk løsninger** støttes ved at semantisk og teknisk samhandling er rettet mot felles data, standarder og byggeklosser.

Rammeverket kan bli for overordnet hvis det ikke kobles til konkrete beslutninger, referansearkitekturer, standarder og forvaltningsansvar. Det kan også bli for tungt hvis det brukes likt på små lokale tiltak og store tverrsektorielle programmer; framgangsmåten starter derfor med å vurdere om endringen i det hele tatt berører andre.

## Lenke til dokumentasjon
- https://www.digdir.no/digital-samhandling/rammeverk-digital-samhandling/2148
- https://www.digdir.no/digital-samhandling/slik-anvender-du-rammeverket-digital-samhandling-i-praksis/1689
- https://www.digdir.no/digital-samhandling/modell-felles-okosystem/4167
- https://www.digdir.no/krav-og-anbefalinger/bruk-rammeverk-digital-samhandling-digitale-loysingar-som-skal-samhandle-med-andre/3111
- https://www.regjeringen.no/no/dokumenter/digitaliseringsrundskrivet/id3103320/

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-09-25
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-09-25
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-25
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/rammeverk-digital-samhandling/2148 , kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/slik-anvender-du-rammeverket-digital-samhandling-i-praksis/1689 , kontrollert 2026-09-25
- https://www.digdir.no/digital-samhandling/modell-felles-okosystem/4167 , kontrollert 2026-09-25
- https://www.digdir.no/krav-og-anbefalinger/bruk-rammeverk-digital-samhandling-digitale-loysingar-som-skal-samhandle-med-andre/3111 , kontrollert 2026-09-25
- https://www.regjeringen.no/no/dokumenter/digitaliseringsrundskrivet/id3103320/ , punkt 1.11, kontrollert 2026-09-25

## Endringer fra forrige versjon

### Analyseforbedringer
- Hovedkilden er byttet. Adressen `v2` brukte (`/rammeverk-digital-samhandling/2149`, både under `/digital-samhandling/` og `/samhandling/`), svarer 404. Rammeverket ligger nå på `/rammeverk-digital-samhandling/2148`.
- `Kort beskrivelse` og `Normerende innhold` gjengir nå rammeverkets faktiske oppbygning: de fire delene, de fem samhandlingsområdene og framgangsmåten i fire steg. `v2` beskrev rammeverket med generelle vurderingspunkter uten å si hva det inneholdt, og nevnte ikke EIF.
- Forpliktelsesnivået er avklart etter regelen fra 2026-09-13. `v2` oppga `anbefalt/styrende` uten hjemmel. `v3` skiller mellom prinsippdelen, som Digitaliseringsrundskrivet punkt 1.11 gjør til krav for statlige virksomheter, og resten av rammeverket, som samme punkt anbefaler.
- Kapabilitetene er prøvd mot definisjonene. `Juridisk samhandling: Regelverkstolkning` er fjernet, fordi rammeverket krever at det rettslige grunnlaget er avklart, men ikke tolker regelverk selv, samme vurdering som for `137` og `EU-009`. `Dele data med andre` og `Forvaltningsstandarder` er fjernet, fordi rammeverket omtaler datadeling og standardisering uten å realisere dem. `Strategisk styring: Arkitekturstyring` er lagt til, fordi rammeverket er det felles nasjonale arkitekturrammeverket. `Veiledning: Utvikling og formidling av veiledning` er lagt til etter regelen fra 2026-09-25.
- Kapabilitetspunktene har fullt navn med hovedkapabilitet, slik at `sync-resource-metadata.py` gjenkjenner dem.
- `Relasjon til andre ressurser` har fått ressurs-ID-er, og Digitaliseringsrundskrivet, Skate og Arkitektur- og standardiseringsrådet er lagt til.

### Tekstlige forbedringer
- Formuleringene «Ressursen er særlig viktig fordi», «fungerer som et felles referansegrunnlag i nasjonal arkitektur» og henvisningen til «den oppdaterte kapabilitetsmodellen» er fjernet, etter regelen i AGENTS.md.
- Fakta, deduksjon og det som ikke er offentlig dokumentert, er merket.
- Den døde adressen er fjernet fra `Lenke til dokumentasjon`, og samlesiden for nasjonal arkitektur er erstattet av rammeverkets egne undersider.
