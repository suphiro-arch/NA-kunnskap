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

Avgrensningen mot tilgangskontroll er uttrykkelig i dokumentasjonen. HelseID avgjør ikke spørsmål om tilgang til helseopplysninger eller tjenester, og avgjør heller ikke om det foreligger tjenstlig behov. Det er tjenestetilbyderne som setter krav til og utfører tilgangskontrollen, og helsevirksomheten selv som har ansvaret for at tjenstlig behov foreligger. HelseID leverer det verifiserte identitets- og tillitsgrunnlaget de bygger avgjørelsen på.

Tilgangen til selve API-ene styres derimot i HelseID. Tjenestetilbyderne definerer scopes for API-ene sine i HelseID Selvbetjening, klienter ber om tilgang til scopes der, og HelseID sjekker ved tokenutstedelse om klienten har tilgang til scopene den ber om. Et scope er nødvendig, men ikke alltid tilstrekkelig: hver tjeneste har fortsatt sin egen tilgangskontroll til opplysningene.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot NHNs beskrivelse av HelseID, tjenestetilbudet, utviklerportalen og dokumentasjonen i HelseID Selvbetjening.

- **Datautveksling og integrasjon: Bruke data fra andre** gjør det mulig å bruke sektorfelles API-er og informasjonstjenester gjennom et felles tillits- og autentiseringsmønster.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling** beskytter innloggingsflyt, tokenbruk og deling av identitets- og tilgangsinformasjon i digital samhandling.
- **Tillit: Autentisering** er en kjernefunksjon ved at HelseID bekrefter identiteten til helsepersonell, systemer og virksomheter.
- **Tillit: Tilgangsstyring** forvalter tilgangen til API-ressurser i helse- og omsorgssektoren: tjenestetilbydere definerer scopes for API-ene sine i HelseID Selvbetjening, klienter ber om tilgang der, scopes er enten åpne, godkjennes av tjenestetilbyderen eller godkjennes automatisk når bruksvilkår er signert, og HelseID utsteder bare token med scopes klienten har tilgang til. Koblingen gjelder tilgang til API-er og systemer, ikke tilgang til helseopplysninger, som tjenestetilbyderne selv avgjør.

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
- Hva er HelseID: https://www.nhn.no/tjenester/helseid
- Tjenestetilbud: https://www.nhn.no/tjenester/helseid/ta-i-bruk
- Hvorfor bruke HelseID: https://www.nhn.no/tjenester/helseid/hvorfor-bruke-helseid
- Spørsmål og svar: https://www.nhn.no/tjenester/helseid/sporsmal-og-svar
- Utviklerportal: https://utviklerportal.nhn.no/en/information-services/helseid
- HelseID Selvbetjening, dokumentasjon: https://selvbetjening.nhn.no/docs

## Plattform
HelseID er en felles tillits- og autentiseringsplattform for helse- og omsorgssektoren, levert av Norsk helsenett SF.

**Fakta:** NHN beskriver støtte for både brukerpålogging, API-beskyttelse og maskin-til-maskin-scenarier. Utviklerportalen viser at produktet har dokumenterte protokoller, sikkerhetsprofil, nettverksforutsetninger og planlagte endringer.

**Ikke offentlig dokumentert i brukte kilder:** Full intern driftsarkitektur, detaljert plattformtopologi og komplett oversikt over alle sikkerhetsmekanismer i produksjonsoppsettet.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er laget for å være en felles sikkerhets- og tillitskomponent i sektoren.
- Det er særlig relevant når behovet er pålogging og sikring av tilgang til helseopplysninger og sektorfelles API-er.
- Det er mindre relevant dersom behovet er generell innbyggerinnlogging eller en ren lokal tilgangsløsning uten samhandling på tvers.

**Kildekode:** Ikke offentlig dokumentert. Selve tjenesten er ikke publisert, men Norsk helsenett publiserer klientbibliotek og eksempelkode på [github.com/NorskHelsenett](https://github.com/NorskHelsenett), blant annet `HelseID.Library.Java`.

**Lisens:** Ikke offentlig dokumentert for selve tjenesten. Klientbibliotekene `HelseID.Library.Java` og `HelseID.Library` har MIT, kontrollert mot repositoriene 2026-09-25.

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
- https://www.nhn.no/tjenester/helseid
- https://www.nhn.no/tjenester/helseid/ta-i-bruk
- https://www.nhn.no/tjenester/helseid/hvorfor-bruke-helseid
- https://www.nhn.no/tjenester/helseid/sporsmal-og-svar
- https://www.nhn.no/tjenester/helseid/personvern-i-helseid
- https://www.nhn.no/tjenester/helseid
- https://utviklerportal.nhn.no/en/information-services/helseid
- https://selvbetjening.nhn.no/docs
- https://selvbetjening.nhn.no/docs/api

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.nhn.no/tjenester/helseid (kontrollert 2026-03-27)
- Nettkilde: https://www.nhn.no/tjenester/helseid (kontrollert 2026-09-30)
- Nettkilde: https://www.nhn.no/tjenester/helseid/ta-i-bruk (kontrollert 2026-09-30)
- Nettkilde: https://www.nhn.no/tjenester/helseid/hvorfor-bruke-helseid (kontrollert 2026-03-27)
- Nettkilde: https://www.nhn.no/tjenester/helseid/sporsmal-og-svar (rekontrollert 2026-09-16) (kontrollert 2026-03-27)
- Nettkilde: https://www.nhn.no/tjenester/helseid/personvern-i-helseid (kontrollert 2026-03-27)
- Nettkilde: https://www.nhn.no/tjenester/helseid (kontrollert 2026-09-30)
- Nettkilde: https://utviklerportal.nhn.no/en/information-services/helseid (kontrollert 2026-09-30)
- Nettkilde: https://selvbetjening.nhn.no/docs (kontrollert 2026-10-25)
- Nettkilde: https://selvbetjening.nhn.no/docs/api (kontrollert 2026-10-25)
- Nettkilde: https://utviklerportal.nhn.no/no/informasjonstjenester/pasientens-maaledata (kontrollert 2026-10-25)

## Endringer fra forrige versjon

### Analyseforbedringer
- `Tillit: Tilgangsstyring` er lagt til. Dokumentasjonen i HelseID Selvbetjening (https://selvbetjening.nhn.no/docs, kontrollert 2026-10-25) beskriver at API-tilbydere bruker scopes for å styre hvilke klienter som har tilgang til endepunktene i API-et, at noen scopes er åpne, mens «Andre krever godkjenning fra tjenesteleverandør, mens noen blir automatisk godkjent», og at «HelseID vil sjekke om klienten har tilgang til disse scopene». Pasientens måledata viser en slik godkjenning i praksis: tilgangen konfigureres i HelseID Selvbetjening og godkjennes manuelt av tjenesten.
- Koblingen er avgrenset til tilgang til API-er og systemer. Avgrensningen fra `v2` står: HelseID avgjør ikke tilgang til helseopplysninger, og `Tillit: Tilgangskontroll` er fortsatt ikke satt. Selvbetjeningsdokumentasjonen sier selv at «enhver tjeneste har sin egen tilgangskontroll».
- Grunnlagslinjen i `Kapabiliteter` er flyttet over kulelista.

### Tekstlige forbedringer
- Et avsnitt om scope-basert tilgang til API-er er lagt til i `Kort beskrivelse`, og HelseID Selvbetjening er lagt til i `Kanaler`, `Lenke til dokumentasjon` og `Kildegrunnlag brukt i utfyllingen`. Øvrig tekst fra `v2` er beholdt.
