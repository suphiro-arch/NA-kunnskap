# Produkt-canvas: HelseID

## Navn
HelseID

## Ressurs ID
NHN-002

## Status/Livsfase
**Produksjon** - etablert nasjonal felleskomponent for pÃ¥logging og sikring av digital samhandling i helse- og omsorgssektoren.

**Fakta:** Norsk helsenett beskriver HelseID som en felles pÃ¥loggingslÃ¸sning for helse- og omsorgssektoren. Tjenesten har vÃ¦rt operativ siden 2017, og NHN beskriver den som brukt bÃ¥de til brukerpÃ¥logging, sikring av API-er og maskin-til-maskin-samhandling i sektoren.

## Modenhet
**HÃ¸y modenhet** - innarbeidet og tydelig sektorforankret tillitskomponent:
- HelseID er etablert som teknisk felleskomponent i Helsenettet og er ogsÃ¥ tilgjengelig via internett i relevante brukslÃ¸p.
- Produktet dekker bÃ¥de autentisering av helsepersonell, sikring av systemer og beskyttelse av API-er.
- NHN publiserer bÃ¥de overordnet tjenestebeskrivelse, tjenestetilbud, spÃ¸rsmÃ¥l og svar, utviklerportal og planlagte endringer.
- LÃ¸sningen er tett koblet til nasjonale registre og sentrale e-helselÃ¸sninger, noe som gir hÃ¸y verdi utover ren innlogging.

**Deduksjon:** Modenheten er hÃ¸y bÃ¥de teknisk og organisatorisk, men nytteverdien for den enkelte virksomhet avhenger av lokal identitetsforvaltning, tilgang til egnet eID og riktig integrasjon mot sektorlÃ¸sningene.

## Kort beskrivelse
HelseID er den nasjonale felleskomponenten for pÃ¥logging, tillit og sikring av digital samhandling i helse- og omsorgssektoren. Produktet gjÃ¸r det mulig Ã¥ autentisere helsepersonell, systemer og virksomheter, beskytte API-er og berike identitetsinformasjon med opplysninger fra nasjonale registre som Helsepersonellregisteret og Personregisteret. HelseID er derfor mer enn en innloggingslÃ¸sning: det er en felles tillitsinfrastruktur for sikker tilgang til helseopplysninger og digitale helsetjenester pÃ¥ tvers av virksomheter og forvaltningsnivÃ¥er.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** gjÃ¸r det mulig Ã¥ bruke sektorfelles API-er og informasjonstjenester gjennom et felles tillits- og autentiseringsmÃ¸nster.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter innloggingsflyt, tokenbruk og deling av identitets- og tilgangsinformasjon i digital samhandling.
- **Tillit: Autentisering** er en kjernefunksjon ved at HelseID bekrefter identiteten til helsepersonell, systemer og virksomheter.
- **Tillit: Tilgangskontroll** gir grunnlag for at tjenestetilbydere kan etablere regler for hvem og hva som fÃ¥r tilgang til beskyttede tjenester og API-er.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot NHNs beskrivelse av HelseID, tjenestetilbudet og utviklerportalen.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** NHNs sider `Hva er HelseID`, `Tjenestetilbud`, `Hvorfor bruke HelseID` og `SpÃ¸rsmÃ¥l og svar`.

Dokumenterte mÃ¥l:
- StÃ¸tte elektronisk kommunikasjon mellom aktÃ¸rer i helse- og omsorgssektoren.
- GjÃ¸re det enklere for virksomheter Ã¥ ha tillit til hverandre og dele informasjon pÃ¥ en sikker mÃ¥te.
- Tilby autentisering av brukere, systemer og virksomheter, samt beskyttelse av tjenestetilbyderes API-er.

Operative mÃ¥l utledet fra de samme kildene:
- Forenkle tilgang til nÃ¸dvendige helseopplysninger for helsepersonell gjennom mer enhetlig og sikker pÃ¥logging.
- Redusere behovet for at hver virksomhet etablerer egne sikkerhetslÃ¸sninger for samhandling og API-beskyttelse.
- Berike identitetsgrunnlaget med informasjon fra nasjonale registre slik at tilgangsbeslutninger kan bygge pÃ¥ bedre og mer pÃ¥litelig informasjon.

## Brukerbehov
- Helsepersonell trenger trygg og gjenkjennelig pÃ¥logging til nasjonale og lokale helsetjenester.
- Tjenestetilbydere trenger en felles lÃ¸sning for Ã¥ beskytte API-er og informasjonstjenester.
- Virksomheter i sektoren trenger et tillitsgrunnlag som gjÃ¸r sikker informasjonsdeling mulig pÃ¥ tvers av organisatoriske grenser.
- Integrasjonsteam trenger dokumenterte bruksmÃ¸nstre for bÃ¥de brukerpÃ¥logging og sikring av API-er.
- Forvaltnings- og sikkerhetsmiljÃ¸er trenger bedre kontroll pÃ¥ hvordan identitet og tilgang brukes i digital samhandling.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Helsepersonell og andre ansatte i sektoren | Trygg og enkel pÃ¥logging | Tilgang til fagsystemer og nasjonale informasjonstjenester | Viktigste sluttbrukergruppe |
| Tjenestetilbydere | Sikre API-er og tilgang til egne tjenester | Beskyttelse av nasjonale og lokale informasjonstjenester | Bruker HelseID som tillits- og beskyttelseskomponent |
| Tjenestekonsumenter og medlemsvirksomheter | Tilgang til beskyttede sektortjenester | Samhandling med nasjonale e-helselÃ¸sninger og andre virksomheter | MÃ¥ vÃ¦re medlem i Helsenettet eller godkjent tredjepartsleverandÃ¸r i relevante lÃ¸p |
| Integrasjonsteam og leverandÃ¸rer | Standardiserte protokoller og selvbetjening | Utvikling, test og produksjonssetting | Bruker utviklerportal og selvbetjeningslÃ¸sning |
| NHN og sektorfelles forvaltningsmiljÃ¸er | Drift, styring og videreutvikling | Felles tillitsinfrastruktur i sektoren | NHN leverer og forvalter tjenesten |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
**PÃ¥logging for helsepersonell og andre ansatte.** HelseID tilbyr brukerautentisering for helsepersonell og andre ansatte, i samspill med valgte identitetstilbydere. Dette gjÃ¸r lÃ¸sningen relevant nÃ¥r sektoren trenger sikker innlogging til fagsystemer og informasjonstjenester, ikke bare generell eID-bruk for innbyggere.

**Sikring av API-er og informasjonstjenester.** HelseID brukes ogsÃ¥ til Ã¥ beskytte API-er og andre digitale tjenester som hÃ¥ndterer helseopplysninger eller annen sensitiv informasjon. Produktet er derfor ikke bare en brukerinnloggingslÃ¸sning, men ogsÃ¥ en komponent for teknisk tilgangskontroll og sikker samhandling mellom systemer.

**Berikelse av identitetsgrunnlag med nasjonale registre.** NHN beskriver at HelseID som eneste aktÃ¸r i sektoren beriker identitetsdetaljer med informasjon fra blant annet Helsepersonellregisteret og Personregisteret. Dette gir tjenestene et rikere og mer sektorrelevant identitetsgrunnlag enn det en ren eID-verifisering ville gjort alene.

**Felles tillitsinfrastruktur og selvbetjent innfÃ¸ring.** HelseID omfatter ogsÃ¥ selvbetjeningslÃ¸sning, leverandÃ¸r- og medlemsmodell, portal for identitetstilbydere og dokumenterte bruksmÃ¸nstre i utviklerportalen. Det gjÃ¸r produktet til en felles sektorinfrastruktur for tillit og tilgang, ikke bare en teknisk innloggingskomponent i smal forstand.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Autentisering av helsepersonell, systemer og virksomheter | Innbyggerportal eller sluttbrukerflate for pasienter |
| Sikring av API-er og informasjonstjenester | Faglig autorisasjonslogikk i hver enkelt helsetjeneste |
| Berikelse av identitetsinformasjon fra nasjonale registre | Selve registrene som brukes til identitetsberikelse |
| Selvbetjening, utviklerportal og dokumenterte bruksmÃ¸nstre | Lokal brukerkatalogforvaltning i hver virksomhet |
| Felles tillitsgrunnlag for sektorsamhandling | Full erstatning for alle lokale sikkerhets- og tilgangslÃ¸sninger |

## Veikart over kommende funksjonalitet
**Fakta fra NHN-kildene (kontrollert 2026-03-27):**
- NHNs utviklerportal publiserer planlagte endringer som egen del av produktomrÃ¥det.
- Tjenestetilbudet og spÃ¸rsmÃ¥l-og-svar-sidene viser at produktet utvikles videre bÃ¥de for brukerpÃ¥logging, API-sikring og sektorsamhandling.

**Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Et detaljert, samlet veikart med tidsfestede leveranser er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til Ã¥ vÃ¦re knyttet til mer utbredt bruk i sektoren, sterkere samspill mellom aktÃ¸rer og videre modning av sikkerhets- og tilgangsmÃ¸nstre.

## Forretningsverdi/Verdiforslag
### For helsepersonell og virksomheter
- Gir mer enhetlig og sikker tilgang til nÃ¸dvendige helseopplysninger.
- Reduserer behovet for mange separate pÃ¥loggings- og tillitslÃ¸sninger i sektoren.
- StÃ¸tter bedre brukeropplevelse gjennom mer gjenkjennelig og effektiv pÃ¥logging.

### For tjenestetilbydere og integrasjonsmiljÃ¸er
- Gir et felles mÃ¸nster for Ã¥ beskytte API-er og informasjonstjenester.
- Reduserer kostnad og kompleksitet ved Ã¥ bygge pÃ¥ en etablert sektorkomponent i stedet for lokale sÃ¦rordninger.
- Gir tilgang til selvbetjening, dokumenterte bruksmÃ¸nstre og utviklerstÃ¸tte.

### For sektoren som helhet
- Styrker informasjonssikkerheten ved digital samhandling.
- Bidrar til bedre tillit mellom virksomheter og mer kontrollert deling av helseopplysninger.
- UnderstÃ¸tter gjenbruk av sikkerhetslÃ¸sninger som del av den digitale grunnmuren i helse- og omsorgssektoren.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk og personvern | Feil bruk av identitets- og registeropplysninger kan gi personvern- og tilgangsproblemer | Tydelige behandlingsregler, rolleavklaringer og minst mulig deling |
| Teknisk | Feil i integrasjon eller feil valg av bruksmÃ¸nster kan gi utilgjengelige eller usikre tjenester | Dokumenterte bruksmÃ¸nstre, testmiljÃ¸ og bedre innfÃ¸ringsstÃ¸tte |
| Sikkerhet | Kompromitterte identiteter, svak eID eller feil beskyttelse av API-er kan gi uautorisert tilgang | Sterke sikkerhetsprofiler, kontrollert tilgang og kontinuerlig sikkerhetsforvaltning |
| Avhengigheter | Tjenesten er avhengig av identitetstilbydere, nasjonale registre og samspill mellom mange aktÃ¸rer | Tydelig rollefordeling, robust forvaltning og standardiserte integrasjoner |
| Organisatorisk | Ujevn innfÃ¸ring og ulik modenhet i virksomhetene kan redusere gevinsten av felleslÃ¸sningen | Medlemsmodell, veiledning og sektorforankret videreutvikling |

## Kanaler
- Produktside: https://www.nhn.no/tjenester/helseid
- Hva er HelseID: https://www.nhn.no/tjenester/helseid/hva-er-helseid
- Tjenestetilbud: https://www.nhn.no/tjenester/helseid/tjenestetilbud
- Hvorfor bruke HelseID: https://www.nhn.no/tjenester/helseid/hvorfor-bruke-helseid
- SpÃ¸rsmÃ¥l og svar: https://www.nhn.no/tjenester/helseid/sporsmal-og-svar
- Utviklerportal: https://utviklerportal.nhn.no/information-services/helseid

## Plattform
HelseID er en felles tillits- og autentiseringsplattform for helse- og omsorgssektoren, levert av Norsk helsenett SF.

**Fakta:** NHN beskriver stÃ¸tte for bÃ¥de brukerpÃ¥logging, API-beskyttelse og maskin-til-maskin-scenarier. Utviklerportalen viser at produktet har dokumenterte protokoller, sikkerhetsprofil, nettverksforutsetninger og planlagte endringer.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsarkitektur, detaljert plattformtopologi og komplett oversikt over alle sikkerhetsmekanismer i produksjonsoppsettet.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet er laget for Ã¥ vÃ¦re en felles sikkerhets- og tillitskomponent i sektoren.
- Det er sÃ¦rlig relevant nÃ¥r behovet er pÃ¥logging og sikring av tilgang til helseopplysninger og sektorfelles API-er.
- Det er mindre relevant dersom behovet er generell innbyggerinnlogging eller en ren lokal tilgangslÃ¸sning uten samhandling pÃ¥ tvers.

## StÃ¸tter arkitekturprinsipper
- **P5: Del og gjenbruk lÃ¸sninger** realiseres ved at sektoren kan bruke Ã©n felles tillitskomponent i stedet for mange lokale ordninger.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** stÃ¸ttes fordi HelseID gjÃ¸r trygg samhandling mellom mange virksomheter og systemer mulig.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** er en kjerneegenskap, siden produktet etablerer grunnlaget for sikker autentisering, kontrollert tilgang og pÃ¥litelig identitetsinformasjon.

## Finansiering
- **Fakta:** NHN oppgir at primÃ¦r bruk av HelseID for medlemsvirksomheter for tiden inngÃ¥r i medlemsavgiften i Helsenettet.
- **Fakta:** Enkelte tilleggstjenester kan vÃ¦re prislagt, og det kan oppstÃ¥ indirekte kostnader for virksomhetene knyttet til eID, integrasjon og bruk av egne leverandÃ¸rer.
- **Deduksjon:** Finansieringsmodellen er derfor en kombinasjon av medlemsfinansiert grunnbruk og virksomhetsspesifikke kostnader ved innfÃ¸ring og tilpasning.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Norsk helsenett SF | NHNs produktsider og spÃ¸rsmÃ¥l og svar |
| Driftsansvar | Norsk helsenett SF | NHN beskriver HelseID som levert og driftet av NHN |
| Budsjett- og kostnadsmodell | NHN, med medlemsavgift og eventuelle tilleggstjenester | NHNs beskrivelser av juridisk og Ã¸konomisk modell |
| Styringsmodell | Del av Helsenettets og sektorens felles grunnmur for digitale tjenester | NHNs produktsider |

## Lenke til dokumentasjon
- https://www.nhn.no/tjenester/helseid
- https://www.nhn.no/tjenester/helseid/hva-er-helseid
- https://www.nhn.no/tjenester/helseid/tjenestetilbud
- https://www.nhn.no/tjenester/helseid/hvorfor-bruke-helseid
- https://www.nhn.no/tjenester/helseid/sporsmal-og-svar
- https://www.nhn.no/tjenester/helseid/personvern-i-helseid
- https://www.nhn.no/tjenester/helseid/tjenestetilbud/utbredelse-av-tjenesten
- https://utviklerportal.nhn.no/information-services/helseid

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.nhn.no/tjenester/helseid (kontrollert 2026-03-27)
- Nettkilde: https://www.nhn.no/tjenester/helseid/hva-er-helseid (kontrollert 2026-03-27)
- Nettkilde: https://www.nhn.no/tjenester/helseid/tjenestetilbud (kontrollert 2026-03-27)
- Nettkilde: https://www.nhn.no/tjenester/helseid/hvorfor-bruke-helseid (kontrollert 2026-03-27)
- Nettkilde: https://www.nhn.no/tjenester/helseid/sporsmal-og-svar (kontrollert 2026-03-27)
- Nettkilde: https://www.nhn.no/tjenester/helseid/personvern-i-helseid (kontrollert 2026-03-27)
- Nettkilde: https://www.nhn.no/tjenester/helseid/tjenestetilbud/utbredelse-av-tjenesten (kontrollert 2026-03-27)
- Nettkilde: https://utviklerportal.nhn.no/information-services/helseid (kontrollert 2026-03-27)

