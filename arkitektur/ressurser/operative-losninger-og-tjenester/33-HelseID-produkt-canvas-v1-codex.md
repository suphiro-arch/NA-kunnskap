# Produkt-canvas: HelseID

## Navn
HelseID

## Ressurs ID
NHN-002

## Status/Livsfase
**Produksjon** - etablert nasjonal felleskomponent for pålogging og sikring av digital samhandling i helse- og omsorgssektoren.

**Fakta:** Norsk helsenett beskriver HelseID som en felles påloggingsløsning for helse- og omsorgssektoren. Tjenesten har vært operativ siden 2017, og NHN beskriver den som brukt både til brukerpålogging, sikring av API-er og maskin-til-maskin-samhandling i sektoren.

## Modenhet
**Høy modenhet** - innarbeidet og tydelig sektorforankret tillitskomponent:
- HelseID er etablert som teknisk felleskomponent i Helsenettet og er også tilgjengelig via internett i relevante bruksløp.
- Produktet dekker både autentisering av helsepersonell, sikring av systemer og beskyttelse av API-er.
- NHN publiserer både overordnet tjenestebeskrivelse, tjenestetilbud, spørsmål og svar, utviklerportal og planlagte endringer.
- Løsningen er tett koblet til nasjonale registre og sentrale e-helseløsninger, noe som gir høy verdi utover ren innlogging.

**Deduksjon:** Modenheten er høy både teknisk og organisatorisk, men nytteverdien for den enkelte virksomhet avhenger av lokal identitetsforvaltning, tilgang til egnet eID og riktig integrasjon mot sektorløsningene.

## Kort beskrivelse
HelseID er den nasjonale felleskomponenten for pålogging, tillit og sikring av digital samhandling i helse- og omsorgssektoren. Produktet gjør det mulig å autentisere helsepersonell, systemer og virksomheter, beskytte API-er og berike identitetsinformasjon med opplysninger fra nasjonale registre som Helsepersonellregisteret og Personregisteret. HelseID er derfor mer enn en innloggingsløsning: det er en felles tillitsinfrastruktur for sikker tilgang til helseopplysninger og digitale helsetjenester på tvers av virksomheter og forvaltningsnivåer.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** gjør det mulig å bruke sektorfelles API-er og informasjonstjenester gjennom et felles tillits- og autentiseringsmønster.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter innloggingsflyt, tokenbruk og deling av identitets- og tilgangsinformasjon i digital samhandling.
- **Tillit: Autentisering** er en kjernefunksjon ved at HelseID bekrefter identiteten til helsepersonell, systemer og virksomheter.
- **Tillit: Tilgangskontroll** gir grunnlag for at tjenestetilbydere kan etablere regler for hvem og hva som får tilgang til beskyttede tjenester og API-er.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot NHNs beskrivelse av HelseID, tjenestetilbudet og utviklerportalen.

## Produktmål
**Primærkilder:** NHNs sider `Hva er HelseID`, `Tjenestetilbud`, `Hvorfor bruke HelseID` og `Spørsmål og svar`.

Dokumenterte mål:
- Støtte elektronisk kommunikasjon mellom aktører i helse- og omsorgssektoren.
- Gjøre det enklere for virksomheter å ha tillit til hverandre og dele informasjon på en sikker måte.
- Tilby autentisering av brukere, systemer og virksomheter, samt beskyttelse av tjenestetilbyderes API-er.

Operative mål utledet fra de samme kildene:
- Forenkle tilgang til nødvendige helseopplysninger for helsepersonell gjennom mer enhetlig og sikker pålogging.
- Redusere behovet for at hver virksomhet etablerer egne sikkerhetsløsninger for samhandling og API-beskyttelse.
- Berike identitetsgrunnlaget med informasjon fra nasjonale registre slik at tilgangsbeslutninger kan bygge på bedre og mer pålitelig informasjon.

## Brukerbehov
- Helsepersonell trenger trygg og gjenkjennelig pålogging til nasjonale og lokale helsetjenester.
- Tjenestetilbydere trenger en felles løsning for å beskytte API-er og informasjonstjenester.
- Virksomheter i sektoren trenger et tillitsgrunnlag som gjør sikker informasjonsdeling mulig på tvers av organisatoriske grenser.
- Integrasjonsteam trenger dokumenterte bruksmønstre for både brukerpålogging og sikring av API-er.
- Forvaltnings- og sikkerhetsmiljøer trenger bedre kontroll på hvordan identitet og tilgang brukes i digital samhandling.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Helsepersonell og andre ansatte i sektoren | Trygg og enkel pålogging | Tilgang til fagsystemer og nasjonale informasjonstjenester | Viktigste sluttbrukergruppe |
| Tjenestetilbydere | Sikre API-er og tilgang til egne tjenester | Beskyttelse av nasjonale og lokale informasjonstjenester | Bruker HelseID som tillits- og beskyttelseskomponent |
| Tjenestekonsumenter og medlemsvirksomheter | Tilgang til beskyttede sektortjenester | Samhandling med nasjonale e-helseløsninger og andre virksomheter | Må være medlem i Helsenettet eller godkjent tredjepartsleverandør i relevante løp |
| Integrasjonsteam og leverandører | Standardiserte protokoller og selvbetjening | Utvikling, test og produksjonssetting | Bruker utviklerportal og selvbetjeningsløsning |
| NHN og sektorfelles forvaltningsmiljøer | Drift, styring og videreutvikling | Felles tillitsinfrastruktur i sektoren | NHN leverer og forvalter tjenesten |

## Hovedfunksjoner
### Primære funksjoner
**Pålogging for helsepersonell og andre ansatte.** HelseID tilbyr brukerautentisering for helsepersonell og andre ansatte, i samspill med valgte identitetstilbydere. Dette gjør løsningen relevant når sektoren trenger sikker innlogging til fagsystemer og informasjonstjenester, ikke bare generell eID-bruk for innbyggere.

**Sikring av API-er og informasjonstjenester.** HelseID brukes også til å beskytte API-er og andre digitale tjenester som håndterer helseopplysninger eller annen sensitiv informasjon. Produktet er derfor ikke bare en brukerinnloggingsløsning, men også en komponent for teknisk tilgangskontroll og sikker samhandling mellom systemer.

**Berikelse av identitetsgrunnlag med nasjonale registre.** NHN beskriver at HelseID som eneste aktør i sektoren beriker identitetsdetaljer med informasjon fra blant annet Helsepersonellregisteret og Personregisteret. Dette gir tjenestene et rikere og mer sektorrelevant identitetsgrunnlag enn det en ren eID-verifisering ville gjort alene.

**Felles tillitsinfrastruktur og selvbetjent innføring.** HelseID omfatter også selvbetjeningsløsning, leverandør- og medlemsmodell, portal for identitetstilbydere og dokumenterte bruksmønstre i utviklerportalen. Det gjør produktet til en felles sektorinfrastruktur for tillit og tilgang, ikke bare en teknisk innloggingskomponent i smal forstand.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Autentisering av helsepersonell, systemer og virksomheter | Innbyggerportal eller sluttbrukerflate for pasienter |
| Sikring av API-er og informasjonstjenester | Faglig autorisasjonslogikk i hver enkelt helsetjeneste |
| Berikelse av identitetsinformasjon fra nasjonale registre | Selve registrene som brukes til identitetsberikelse |
| Selvbetjening, utviklerportal og dokumenterte bruksmønstre | Lokal brukerkatalogforvaltning i hver virksomhet |
| Felles tillitsgrunnlag for sektorsamhandling | Full erstatning for alle lokale sikkerhets- og tilgangsløsninger |

## Veikart over kommende funksjonalitet
**Fakta fra NHN-kildene (kontrollert 2026-03-27):**
- NHNs utviklerportal publiserer planlagte endringer som egen del av produktområdet.
- Tjenestetilbudet og spørsmål-og-svar-sidene viser at produktet utvikles videre både for brukerpålogging, API-sikring og sektorsamhandling.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et detaljert, samlet veikart med tidsfestede leveranser er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til å være knyttet til mer utbredt bruk i sektoren, sterkere samspill mellom aktører og videre modning av sikkerhets- og tilgangsmønstre.

## Forretningsverdi/Verdiforslag
### For helsepersonell og virksomheter
- Gir mer enhetlig og sikker tilgang til nødvendige helseopplysninger.
- Reduserer behovet for mange separate påloggings- og tillitsløsninger i sektoren.
- Støtter bedre brukeropplevelse gjennom mer gjenkjennelig og effektiv pålogging.

### For tjenestetilbydere og integrasjonsmiljøer
- Gir et felles mønster for å beskytte API-er og informasjonstjenester.
- Reduserer kostnad og kompleksitet ved å bygge på en etablert sektorkomponent i stedet for lokale særordninger.
- Gir tilgang til selvbetjening, dokumenterte bruksmønstre og utviklerstøtte.

### For sektoren som helhet
- Styrker informasjonssikkerheten ved digital samhandling.
- Bidrar til bedre tillit mellom virksomheter og mer kontrollert deling av helseopplysninger.
- Understøtter gjenbruk av sikkerhetsløsninger som del av den digitale grunnmuren i helse- og omsorgssektoren.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk og personvern | Feil bruk av identitets- og registeropplysninger kan gi personvern- og tilgangsproblemer | Tydelige behandlingsregler, rolleavklaringer og minst mulig deling |
| Teknisk | Feil i integrasjon eller feil valg av bruksmønster kan gi utilgjengelige eller usikre tjenester | Dokumenterte bruksmønstre, testmiljø og bedre innføringsstøtte |
| Sikkerhet | Kompromitterte identiteter, svak eID eller feil beskyttelse av API-er kan gi uautorisert tilgang | Sterke sikkerhetsprofiler, kontrollert tilgang og kontinuerlig sikkerhetsforvaltning |
| Avhengigheter | Tjenesten er avhengig av identitetstilbydere, nasjonale registre og samspill mellom mange aktører | Tydelig rollefordeling, robust forvaltning og standardiserte integrasjoner |
| Organisatorisk | Ujevn innføring og ulik modenhet i virksomhetene kan redusere gevinsten av fellesløsningen | Medlemsmodell, veiledning og sektorforankret videreutvikling |

## Kanaler
- Produktside: https://www.nhn.no/tjenester/helseid
- Hva er HelseID: https://www.nhn.no/tjenester/helseid/hva-er-helseid
- Tjenestetilbud: https://www.nhn.no/tjenester/helseid/tjenestetilbud
- Hvorfor bruke HelseID: https://www.nhn.no/tjenester/helseid/hvorfor-bruke-helseid
- Spørsmål og svar: https://www.nhn.no/tjenester/helseid/sporsmal-og-svar
- Utviklerportal: https://utviklerportal.nhn.no/information-services/helseid

## Plattform
HelseID er en felles tillits- og autentiseringsplattform for helse- og omsorgssektoren, levert av Norsk helsenett SF.

**Fakta:** NHN beskriver støtte for både brukerpålogging, API-beskyttelse og maskin-til-maskin-scenarier. Utviklerportalen viser at produktet har dokumenterte protokoller, sikkerhetsprofil, nettverksforutsetninger og planlagte endringer.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsarkitektur, detaljert plattformtopologi og komplett oversikt over alle sikkerhetsmekanismer i produksjonsoppsettet.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er laget for å være en felles sikkerhets- og tillitskomponent i sektoren.
- Det er særlig relevant når behovet er pålogging og sikring av tilgang til helseopplysninger og sektorfelles API-er.
- Det er mindre relevant dersom behovet er generell innbyggerinnlogging eller en ren lokal tilgangsløsning uten samhandling på tvers.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger** realiseres ved at sektoren kan bruke én felles tillitskomponent i stedet for mange lokale ordninger.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi HelseID gjør trygg samhandling mellom mange virksomheter og systemer mulig.
- **P7: Sørg for tillit til oppgaveløsningen** er en kjerneegenskap, siden produktet etablerer grunnlaget for sikker autentisering, kontrollert tilgang og pålitelig identitetsinformasjon.

## Finansiering
- **Fakta:** NHN oppgir at primær bruk av HelseID for medlemsvirksomheter for tiden inngår i medlemsavgiften i Helsenettet.
- **Fakta:** Enkelte tilleggstjenester kan være prislagt, og det kan oppstå indirekte kostnader for virksomhetene knyttet til eID, integrasjon og bruk av egne leverandører.
- **Deduksjon:** Finansieringsmodellen er derfor en kombinasjon av medlemsfinansiert grunnbruk og virksomhetsspesifikke kostnader ved innføring og tilpasning.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Norsk helsenett SF | NHNs produktsider og spørsmål og svar |
| Driftsansvar | Norsk helsenett SF | NHN beskriver HelseID som levert og driftet av NHN |
| Budsjett- og kostnadsmodell | NHN, med medlemsavgift og eventuelle tilleggstjenester | NHNs beskrivelser av juridisk og økonomisk modell |
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


