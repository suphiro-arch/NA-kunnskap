# NSMs grunnprinsipper for IKT-sikkerhet

## Navn
NSMs grunnprinsipper for IKT-sikkerhet

## Ressurs ID
NSM-001

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Veileder, publisert som prinsipper med anbefalte tiltak

## Status/Livsfase
Aktiv. Gjeldende versjon er 2.1.

**Fakta:** NSM oppgir at versjon 2.1 ble publisert 4. juni 2024, og at siden ble sist oppdatert 28. oktober 2024. Siden om historikk viser tre tidligere utgaver, 1.0, 1.1 og 2.0. NSM gjør dem ikke lenger tilgjengelige hver for seg, men tiltakene fra dem er samlet i et eget regneark under støtteproduktene.

**Ikke offentlig dokumentert:** Når de enkelte tidligere versjonene kom, og hva som ble endret fra 2.0 til 2.1, går ikke fram av historikksiden.

## Kort beskrivelse
NSMs grunnprinsipper for IKT-sikkerhet er Nasjonal sikkerhetsmyndighets samling av prinsipper og anbefalte tiltak for å beskytte informasjonssystemer mot uautorisert tilgang, skade og misbruk. Prinsippene er ordnet i fire kategorier, og hvert prinsipp har mål, begrunnelse og anbefalte tiltak.

**Fakta:** NSM oppgir at prinsippene bygger på egne erfaringer og på tilbakemeldinger fra offentlige og private virksomheter. NSM understreker at prinsippene gir et godt forsvar mot digitale trusler, men ingen garanti mot å bli rammet.

## Formål og normerende rolle
Formålet er å gi virksomheter et felles og konkret grunnlag for å velge tekniske og organisatoriske sikkerhetstiltak for egne informasjonssystemer.

**Fakta:** NSM anbefaler alle virksomheter å følge prinsippene. Virksomheten skal selv vurdere og tilpasse dem, og valget av tiltak skal bygge på virksomhetens ordinære risikoarbeid, der prinsippene er et hjelpemiddel. Gjennomføres ikke et anbefalt tiltak, skal risikoen vurderes mot virksomhetens risikotoleranse og mot lov-, bransje- og kontraktskrav, og kompenserende tiltak skal vurderes hvis risikoen ikke er akseptabel.

Den normerende rollen er derfor **anbefalt**: prinsippene gir retning for hvilke tiltak som bør vurderes, men pålegger ikke noe selv.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er **anbefalt**, uten rettslig forankring i grunnprinsippene selv.

**Fakta:** NSM omtaler prinsippene som anbefalinger. NSM oppgir også at sikkerhetsloven har flere og strengere krav enn grunnprinsippene, og at det å følge prinsippene ikke i seg selv betyr at en virksomhet oppfyller sikkerhetsloven. Prinsippene kan være en nyttig første byggekloss for IKT-systemer som er, eller kan bli, omfattet av loven.

**Fakta:** eForvaltningsforskriften § 15 krever at forvaltningsorganer som bruker elektronisk kommunikasjon, har internkontroll som bygger på anerkjente standarder for styringssystem for informasjonssikkerhet. Forskriften nevner ikke NSMs grunnprinsipper.

**Deduksjon:** En virksomhet kan bruke grunnprinsippene som del av grunnlaget for internkontrollen etter § 15, men plikten følger av forskriften og kan oppfylles uten grunnprinsippene. Forskriften gjør dem ikke bindende.

Etterlevelse skjer gjennom virksomhetens egen sikkerhetsstyring og risikovurdering. Avvik fra et anbefalt tiltak er ikke brudd, men skal etter NSMs egen metode vurderes mot risikotoleranse og kompenseres der risikoen ikke er akseptabel.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot de 21 prinsippene og støtteproduktene. Grunnprinsippene er ikke rettslig forankret, og `Juridisk samhandling` er derfor ikke aktuell. `Tillit: Tilgangsstyring` er vurdert og ikke satt: prinsipp 2.6 om identiteter og tilganger er ett av 21 prinsipper og gir anbefalinger for virksomhetens egne systemer, ikke en evne andre kan ta i bruk.

- **Informasjonssikkerhet: Styringssystem** grunnprinsippene og støtteproduktene gir en tiltakskatalog med prioriteringsforslag, kobling til ISO/IEC 27002 og et verktøy for risikovurdering som virksomheter bruker når de vurderer og forbedrer egne sikkerhetstiltak. NSM sier selv at prinsippene ikke erstatter virksomhetens sikkerhetsstyring.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** normeres direkte i prinsipp 2.5 «Kontroller dataflyt» og 2.7 «Beskytt data i ro og i transitt», som gir anbefalte tiltak for kontroll med hvor data flyter og for beskyttelse av data under overføring.
- **Veiledning: Utvikling og formidling av veiledning** grunnprinsippene er NSMs publiserte veiledning for IKT-sikkerhet, utgitt i versjoner, med støtteprodukter, engelsk utgave og et eget e-læringskurs.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Virksomheter med samfunnskritiske funksjoner eller kritisk infrastruktur | Et samlet grunnlag for sikkerhetstiltak | Etablering og forbedring av IKT-sikkerhet | NSM oppgir at prinsippene er utviklet med disse som hovedmålgruppe |
| Andre offentlige og private virksomheter | Konkrete anbefalte tiltak | Prioritering av sikkerhetsarbeid | NSM oppgir at prinsippene er relevante for alle, uavhengig av om sikkerhetsloven gjelder |
| Virksomhets- og IKT-ledelse | Bindeledd mellom toppledelse og drift | Retningslinjer, budsjett og rapportering av risikobilde | NSM oppgir dette som primær målgruppe, blant annet systemeiere, sikkerhetsledere og prosesseiere |
| Gjennomføring og drift | Konkrete tiltak å etablere og vedlikeholde | Konfigurasjon, overvåking og hendelseshåndtering | Rapporterer status og endringer til ledelsen |
| Virksomheter med tjenesteutsetting eller skytjenester | Sikkerhet når drift er satt ut | Krav til leverandører | NSM oppgir at prinsippene gjelder også når én eller flere IKT-tjenester driftes av tredjepart |

## Normerende innhold
**Fakta:** Versjon 2.1 har 21 prinsipper fordelt på fire kategorier:

| Kategori | Antall | Prinsipper |
|---|---:|---|
| 1. Identifisere og kartlegge | 3 | Kartlegg styringsstrukturer, leveranser og understøttende systemer; kartlegg enheter og programvare; kartlegg brukere og behov for tilgang |
| 2. Beskytte og opprettholde | 10 | Sikkerhet i anskaffelses- og utviklingsprosesser; sikker IKT-arkitektur; sikker konfigurasjon; beskytt nettverk; kontroller dataflyt; kontroll på identiteter og tilganger; beskytt data i ro og i transitt; beskytt e-post og nettleser; evne til gjenoppretting av data; sikkerhet i endringshåndtering |
| 3. Oppdage | 4 | Oppdag og fjern kjente sårbarheter og trusler; etabler sikkerhetsovervåkning; analyser data fra sikkerhetsovervåkning; gjennomfør inntrengningstester |
| 4. Håndtere og gjenopprette | 4 | Forbered håndtering av hendelser; vurder og klassifiser hendelser; kontroller og håndter hendelser; evaluer og lær av hendelser |

**Fakta:** Hvert prinsipp er bygd opp med selve grunnprinsippet, mål, hvorfor det er viktig, anbefalte tiltak og utdypende informasjon. Hvert prinsipp er ment som en kontinuerlig aktivitet gjennom hele informasjonssystemets levetid. Prinsippene konsentrerer seg om tekniske og organisatoriske tiltak, mens fysisk sikkerhet og det menneskelige perspektivet bare omtales kort. Tiltakene retter seg mot både utilsiktede og tilsiktede handlinger, med hovedvekt på tilsiktede.

**Fakta:** Introduksjonen har egne sider om målgruppe, de fire kategoriene, forholdet mellom kategori, prinsipp og tiltak, andre relevante råd, begreper og bruk av tjenesteutsetting og skytjenester.

**Fakta:** NSM publiserer disse støtteproduktene:
- regneark med alle tiltakene, forslag til prioritering og kobling til ISO/IEC 27002
- veileder for risikovurdering av IKT-systemer, et enkelt verktøy for ugraderte IT-, OT- og understøttende systemer, med tilhørende mal i regneark
- engelsk utgave, «NSM ICT Security Principles»
- e-læringskurs på om lag tre timer

## Bruksområde
Grunnprinsippene bør brukes når en virksomhet skal etablere, vurdere eller prioritere sikkerhetstiltak for egne informasjonssystemer, og når sikkerhetskrav skal stilles i anskaffelser, utvikling eller tjenesteutsetting.

De er også egnet som felles referanse når flere virksomheter skal sammenligne sikkerhetsnivå eller avtale tiltak, fordi prinsippene er nummerert og tiltakene er samlet i ett regneark.

## Typiske analyse- og beslutningssituasjoner
- når en virksomhet skal velge og prioritere sikkerhetstiltak ut fra egen risikovurdering
- når sikkerhetskrav skal formuleres i anskaffelser og utviklingsprosjekter (prinsipp 2.1)
- når IKT-arkitekturen, nettverkssegmentering eller kontroll med dataflyt skal vurderes (prinsipp 2.2, 2.4 og 2.5)
- når drift settes ut eller skytjenester tas i bruk
- når evne til å oppdage og håndtere hendelser skal etableres eller evalueres
- når et system kan komme inn under sikkerhetsloven, og en virksomhet trenger et første grunnlag før de strengere kravene vurderes

## Når ressursen normalt ikke er tilstrekkelig alene
Grunnprinsippene er ikke tilstrekkelige alene for virksomheter under sikkerhetsloven, der loven og forskriftene stiller flere og strengere krav. De erstatter heller ikke virksomhetens styringssystem for informasjonssikkerhet: NSM peker selv på ledelsesforankring, sikkerhetskompetanse og etablerte styrings- og rapporteringslinjer som nøkkelfaktorer.

De må også suppleres med personvernregelverket der personopplysninger behandles, med sektorregelverk og bransjenormer, som Normen i helse- og omsorgssektoren, og med fysisk og personellmessig sikkerhet, som prinsippene bare omtaler kort.

## Scope og avgrensning
Inngår:
- tekniske og organisatoriske sikkerhetstiltak for informasjonssystemer
- kartlegging, beskyttelse, deteksjon og hendelseshåndtering
- sikkerhet ved anskaffelse, utvikling, endringshåndtering og tjenesteutsetting
- støtteprodukter for tiltaksoversikt og risikovurdering

Inngår ikke:
- krav etter sikkerhetsloven
- fysisk sikkerhet og personellsikkerhet utover en kort omtale
- personvernregelverket
- et komplett styringssystem for informasjonssikkerhet
- en sertifiseringsordning

Grensen mot ISO/IEC 27001 og 27002 er at grunnprinsippene er en nasjonal anbefaling uten sertifisering, mens regnearket kobler tiltakene til ISO/IEC 27002. Grensen mot sikkert.no er at portalen formidler råd fra flere myndigheter, mens grunnprinsippene er NSMs eget faglige tiltaksgrunnlag.

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Nasjonal sikkerhetsmyndighet (NSM) |
| Forvaltningsansvar | NSM, som publiserer og versjonerer prinsippene og støtteproduktene på nsm.no |
| Endringsprosess | **Fakta:** Prinsippene er revidert i versjonene 1.0, 1.1, 2.0 og 2.1, og bygger på NSMs erfaringer og tilbakemeldinger fra virksomheter. **Ikke offentlig dokumentert:** fast revisjonssyklus eller formell prosess for innspill og høring |
| Publiserings- og beslutningsarena | nsm.no |

## Relasjon til andre ressurser
- **eForvaltningsforskriften (`DIGDIR-066`)**: § 15 krever internkontroll basert på anerkjente standarder for styringssystem for informasjonssikkerhet. Forskriften nevner ikke grunnprinsippene, se `Forpliktelsesnivå og etterlevelse`.
- **Sikkert.no (`FLERE-007`)**: felles myndighetsportal for digital sikkerhet der NSM er en av avsenderne. Portalen formidler råd, mens grunnprinsippene er NSMs underliggende tiltaksgrunnlag.
- **Felles sikkerhet i forvaltningen (`DIGDIR-056`)**: tverrsektorielt sikkerhetssamarbeid der NSM deltar sammen med Datatilsynet, KS, DFØ, Helsedirektoratet og Digdir.
- **Sikkerhetsloven**: stiller flere og strengere krav enn grunnprinsippene for virksomheter som er omfattet. Loven er ikke egen ressurs i registeret.
- **Normen**: bransjenormen for informasjonssikkerhet og personvern i helse- og omsorgssektoren. Helsedirektoratet publiserer en mapping mellom Normens krav og NSMs grunnprinsipper versjon 2.0, og omtaler den selv som en grovanalyse som ikke må tolkes som uttømmende. Normen er ikke egen ressurs i registeret.
- **ISO/IEC 27002**: tiltakene i grunnprinsippene er koblet til ISO/IEC 27002 i NSMs regneark.
- **Cybersjekk**: NSMs tjeneste for å vurdere egen sikkerhetstilstand, som bygger på grunnprinsippene. Tjenesten er ikke egen ressurs i registeret.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er at virksomheter får et konkret og prioriterbart tiltaksgrunnlag, slik at de ikke må bygge egen tiltakskatalog fra bunnen av. Regnearket og veilederen for risikovurdering gjør det mulig å gå fra prinsipp til tiltak og dokumentere valgene.

Arkitekturverdien er et felles, nummerert vokabular for sikkerhetstiltak som kan brukes i kravstilling, avtaler og sammenligning mellom virksomheter. Prinsippene om sikker IKT-arkitektur, nettverksbeskyttelse og kontroll med dataflyt gir føringer for hvordan løsninger bør bygges og kobles sammen.

## Konsekvens ved manglende bruk eller avvik
Brukes ikke grunnprinsippene eller et tilsvarende tiltaksgrunnlag, øker risikoen for at sikkerhetsarbeidet blir ufullstendig, at viktige tiltak mangler, og at virksomheten ikke kan dokumentere hvorfor tiltak er valgt eller valgt bort.

**Deduksjon:** Leses prinsippene som tilstrekkelig for virksomheter under sikkerhetsloven, kan virksomheten tro at kravene er oppfylt når de ikke er det. NSM advarer selv mot denne tolkningen.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Forankring | Prinsippene er anbefalinger uten rettslig forankring | Ujevn bruk mellom virksomheter | Knytte tiltaksvalg til virksomhetens risikovurdering og internkontroll |
| Tolkning | Prinsippene kan forveksles med oppfyllelse av sikkerhetsloven | Falsk trygghet hos virksomheter som er omfattet av loven | Vurdere sikkerhetsloven særskilt, slik NSM anbefaler |
| Endringsstyring | Endringer mellom versjoner er ikke beskrevet på historikksiden | Vanskelig å se hva som må oppdateres ved ny versjon | Bruke regnearket med tiltak fra tidligere versjoner til sammenligning |
| Sammenheng med andre rammeverk | Mappinger mot Normen og NIST CSF finnes hos andre aktører, mot ulike versjoner | Mappingene kan bli utdaterte | Kontrollere versjonen mappingen bygger på |
| Adopsjon | Omfanget kan være krevende for små virksomheter | Tiltak prioriteres ulikt | Bruke prioriteringsforslagene i regnearket |

## Publiseringsform og tilgjengelighet
Ressursen publiseres som åpne nettsider på nsm.no, med én side per prinsipp, og som nedlastbar PDF for versjon 2.1. Støtteproduktene er regneark med tiltak, veileder og mal for risikovurdering, en engelsk utgave og et e-læringskurs. NSM lister også ressurser fra andre aktører, blant annet en mapping mot NIST CSF 2.0 og Normen-mappingen, men oppgir at NSM ikke har ansvar for innholdet i dem.

## Støtter arkitekturprinsipper
- **P7: Sørg for tillit til oppgaveløsningen**
  Grunnprinsippene gir konkrete tiltak for å beskytte informasjonssystemer og for å oppdage og håndtere hendelser, som er forutsetninger for tillit til digitale tjenester.
- **P6: Lag digitale løsninger som støtter samhandling**
  Prinsippene om kontroll med dataflyt og beskyttelse av data i transitt støtter sikker samhandling mellom virksomheter.
- **P2: Ta arkitekturbeslutninger på rett nivå**
  Prinsippene legger valget av tiltak til den enkelte virksomhetens risikovurdering, i stedet for å fastsette ett nivå for alle.

Svakheter, spenninger og begrensninger mot prinsippene: Grunnprinsippene er laget for den enkelte virksomhetens egne systemer. De sier lite om sikkerhet i tjenestekjeder der ansvaret er delt mellom flere virksomheter, og mot `P5: Del og gjenbruk løsninger` gir de ingen anbefaling om felles sikkerhetsløsninger. At tiltakene velges ut fra hver virksomhets egen risikotoleranse, kan gi ulikt sikkerhetsnivå i samme kjede.

## Lenke til dokumentasjon
- https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/
- https://nsm.no/getfile.php/1313975-1717589722/NSM/Filer/Dokumenter/Veiledere/NSMs%20Grunnprinsipper%20for%20IKT-sikkerhet%20v2.1.pdf
- https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/stotteprodukter/stotteprodukter-til-nsms-grunnprinsipper-for-ikt-sikkerhet
- https://nsm.no/getfile.php/136603-1718717207/NSM/Filer/Bildegalleri/Bilder%20til%20grunnprinsipper/Risikovurdering%20av%20IKT-systemer.pdf
- https://nsm.no/advice-and-guidance/publications/nsm-ict-security-principles

## Kildegrunnlag brukt i utfyllingen
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-10-23
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-10-23
- `arkitektur/ressurser/produktnummerering.md`, kontrollert 2026-10-23
- https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/grunnprinsipper-for-ikt-sikkerhet/ , publisert 4. juni 2024, sist oppdatert 28. oktober 2024, kontrollert 2026-10-23
- https://nsm.no/getfile.php/1313975-1717589722/NSM/Filer/Dokumenter/Veiledere/NSMs%20Grunnprinsipper%20for%20IKT-sikkerhet%20v2.1.pdf , kontrollert 2026-10-23
- https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/introduksjon/hva-er-nsms-grunnprinsipper-for-ikt-sikkerhet/ , kontrollert 2026-10-23
- https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/introduksjon/malgruppe/ , sist oppdatert 30. april 2024, kontrollert 2026-10-23
- https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/introduksjon/forholdet-mellom-kategori-prinsipp-og-tiltak/ , kontrollert 2026-10-23
- https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/historikk-og-eldre-versjoner/ , sist oppdatert 5. juni 2024, kontrollert 2026-10-23
- https://nsm.no/regelverk-og-hjelp/rad-og-anbefalinger/stotteprodukter/stotteprodukter-til-nsms-grunnprinsipper-for-ikt-sikkerhet , sist oppdatert 8. november 2024, kontrollert 2026-10-23
- https://nsm.no/getfile.php/136603-1718717207/NSM/Filer/Bildegalleri/Bilder%20til%20grunnprinsipper/Risikovurdering%20av%20IKT-systemer.pdf , kontrollert 2026-10-23
- https://www.helsedirektoratet.no/digitalisering-og-e-helse/normen-personvern-og-informasjonssikkerhet/normen/oversikt-over-normens-krav-og-mapping-mellom-nsms-grunnprinsipper-iso-og-ccm , sist faglig oppdatert 18. desember 2024, kontrollert 2026-10-23
- https://nsm.no/aktuelt/cybersjekk-sjekker-virksomhetens-digitale-sikkerhetstilstand , kontrollert 2026-10-23
- `arkitektur/ressurser/rammer-og-virkemidler/144-eForvaltningsforskriften-v3-claude.md`, for innholdet i § 15, kontrollert 2026-10-23

## Endringer fra forrige versjon
Dette er første publiserte versjon av ressursbeskrivelsen.
