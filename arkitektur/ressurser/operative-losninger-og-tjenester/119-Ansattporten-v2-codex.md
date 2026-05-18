# Ansattporten

## Ressurs ID
DIGDIR-051

## Status/Livsfase
**Produksjon** - etablert tillitstjeneste i ordinær drift for innlogging i ansattkontekst.

**Fakta:** Digdir Docs beskriver Ansattporten som en egen innloggingstjeneste tilpasset bruk som ansatt eller i andre situasjoner der sluttbruker må opptre på vegne av en virksomhet. Dokumentasjonen oppgir også at tjenesten fra 2025 går over i mer ordinær drift med samme SLA for oppetid som ID-porten.

## Modenhet
**Høy modenhet** - operativ fellestjeneste med tydelige integrasjonsmønstre, selvbetjening og synlig bruksvekst.

**Fakta:** Offisielle statistikk- og dokumentsider viser at Ansattporten håndterer store mengder innlogginger og tilgangsforespørsler, og at antall kunder og tjenester følges opp løpende i Samarbeidsportalen.

**Deduksjon:** Modenheten er høy som operativ autentiseringstjeneste, men enkelte funksjoner rundt Entra ID og videre tilgangsstyring er fortsatt i utvikling eller pilotnær videreføring.

## Kort beskrivelse
Ansattporten er Digdirs autentiseringstjeneste for ansatte og andre brukssituasjoner der en sluttbruker må opptre i en representasjonskontekst på vegne av virksomhet. Ressursen gir et eget innloggingsløp for ansattbruk, med egne endepunkt, egen utstederidentitet og støtte for representasjon gjennom autoritative kilder.

Ressursen må ikke forstås som en ren kopi av ID-porten. Ansattporten er en egen tjeneste med isolert sesjonsmodell, egen selvbetjening og funksjoner som er laget for bruk i virksomhetskontekst. Den operative verdien ligger derfor både i sikker innlogging og i at tjenesten kan inngå i løsninger der virksomhetsrepresentasjon og datadeling på vegne av virksomhet er sentralt.

## Kapabiliteter
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling**
  Ansattporten beskytter innloggingsflyt, tokenutstedelse og metadatautveksling i løsninger der ansatte eller virksomhetsrepresentanter skal få sikker tilgang.

- **Tillit: Autentisering**
  Ressursen verifiserer identiteten til sluttbrukeren i ansattkontekst og tilbyr et felles nasjonalt mønster for sikker innlogging i slike tjenester.

- **Tjenesteutvikling: Integrerbare tjenester**
  Ansattporten gjør innlogging og representasjonsnær autentisering gjenbrukbar gjennom standardiserte protokoller, metadata og selvbetjeningsoppsett som andre løsninger kan integrere mot.

## Produktmål
Dokumenterte og tydelig utledbare mål for ressursen er å:
- gi offentlig sektor en felles innloggingstjeneste for ansatte og representasjonsnære brukerreiser
- redusere behovet for lokale spesialløsninger for ansattpålogging og virksomhetskontekst
- støtte sikre og standardiserte integrasjoner mellom tjenesteeiere og Digdirs tillitsinfrastruktur
- gjøre det enklere å kombinere innlogging, representasjon og datadeling på vegne av virksomhet når behovet tilsier det

## Brukerbehov
- Offentlige virksomheter trenger en felles og sikker løsning for innlogging i tjenester for ansatte.
- Tjenesteeiere trenger et standardisert mønster for å koble innlogging til representasjonsforhold når brukeren opptrer på vegne av virksomhet.
- Integrasjonsmiljøer trenger stabile metadata, endepunkt og selvbetjeningsløp for å sette opp og drifte integrasjoner.
- Ansatte trenger en innlogging som er tydelig avgrenset fra innbyggerkontekst og som fungerer i tjenester der jobbrolle og virksomhetsforhold er sentrale.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter og tjenesteeiere | Sikker innlogging i ansattkontekst | Egne tjenester og API-er for ansatte eller virksomhetsrepresentanter | Kjernebrukere |
| Integrasjons- og utviklingsmiljøer | Standardiserte endepunkt, metadata og klientoppsett | Innføring, vedlikehold og feilsøking | Viktig teknisk målgruppe |
| Ansatte og virksomhetsrepresentanter | Forutsigbar og sikker innlogging | Bruk av tjenester i jobb- eller representasjonsrolle | Sluttbrukere |
| Digdirs forvaltnings- og servicedeskmiljøer | Kundeoppfølging, selvbetjening og drift | Forvaltning av integrasjoner og støtte | Operativ intern brukergruppe |
| Arbeidsgivere og identitetsforvaltere | Kontroll med hvem som kan representere virksomheten | Entra ID, Virksomhetsbroen og representasjonsstyring | Strategisk viktig sekundærbruker |

## Hovedfunksjoner
Ansattporten tilbyr en egen innloggingstjeneste for bruk i ansattkontekst. Tjenesten er en separat OpenID Provider med egne endepunkt og egen `issuer`, og den er bevisst skilt fra ID-porten. Det gjør det mulig å håndtere innlogging for ansatte og virksomhetsrepresentanter uten å blande dette sammen med innbyggerpålogging.

En viktig funksjon er støtte for representasjonsnære brukerreiser. Ansattporten kan brukes både til vanlig punktinnlogging og i situasjoner der brukeren må opptre på vegne av en virksomhet. Tjenesten angir representasjonsgrunnlag, men utfører ikke selve tilgangskontrollen i den underliggende tjenesten. Denne avgrensningen er viktig for å forstå hva Ansattporten gjør og hva den ikke gjør.

Ressursen har også en tydelig operativ integrasjonsfunksjon. Metadata, `.well-known`-endepunkt, signeringssertifikater og selvbetjening gjør at tjenesteeiere kan sette opp og vedlikeholde integrasjoner på en mer standardisert måte. Dokumentasjonen anbefaler dynamisk konfigurasjon via metadata for å sikre kontinuerlig tjenesteleveranse ved sertifikatbytte.

Videre er Ansattporten i utvikling på enkelte områder, særlig rundt Entra ID. Dokumentasjonen viser at støtte for Microsoft Entra ID brukes for å utforske hvordan jobbkontoer, representasjon og tilgangsstyring kan håndteres mer sømløst. Samtidig er dette fremdeles et område der tjenesteeiere må forvente løpende endringer, noe som gjør veikart og avgrensning ekstra viktig i arkitekturvurderinger.

### Typiske brukssituasjoner (generisk)
- når en offentlig tjeneste trenger sikker innlogging for ansatte i stedet for innbyggerpålogging
- når en tjenesteeier trenger at en innlogget bruker skal kunne opptre på vegne av virksomhet
- når en løsning trenger standardiserte metadata og selvbetjening for å sette opp ansattpålogging raskt
- når datadeling eller brukerreiser krever kobling mellom autentisering og representasjonsforhold

### Når Ansattporten normalt ikke er førstevalg
- når behovet gjelder ordinær innbyggerpålogging uten ansatt- eller virksomhetskontekst
- når løsningen først og fremst trenger autorisasjon, rolleforvaltning eller representasjonsstyring i seg selv, ikke autentiseringstjenesten som inngang
- når tjenesten ikke har behov for virksomhetskontekst eller ansattrolle og derfor kan bruke enklere eller mer direkte mønstre

## Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Autentisering i ansattkontekst | Full autorisasjonsmodell i den underliggende tjenesten |
| Egne metadata, endepunkt og signeringssertifikater | Innbyggerpålogging via ID-porten |
| Selvbetjening for klientadministrasjon og integrasjonsoppsett | Full representasjonsforvaltning uavhengig av autoritative kilder |
| Støtte for representasjonsnære brukerreiser og datadeling på vegne av virksomhet | Komplette fag- eller saksløsninger |

## Veikart over kommende funksjonalitet
**Fakta:** Kildene kontrollert 18. mai 2026 viser at Ansattporten er i ordinær drift, men at Entra ID-funksjonalitet fortsatt omtales som del av pilotfase og videre utforsking i 2025/2026.

**Fakta:** Dokumentasjonen oppgir også at finansieringsmodellen trolig vil endres i fremtiden, uten at detaljene er offentlig beskrevet i kildene brukt her.

**Deduksjon:** Det mest sannsynlige videreutviklingssporet ligger i bedre støtte for jobbkontoer, representasjonsnære brukerreiser, tilgangsstyring i samspill med andre tillitstjenester og modning av selvbetjening og kundeoppsett.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere og offentlige virksomheter
- Ett nasjonalt mønster for ansattpålogging reduserer behovet for lokale autentiseringsoppsett og gir mer forutsigbar innføring.
- Samme grunnlag kan brukes i flere tjenester som trenger virksomhetskontekst eller representasjonsnære brukerreiser.

### For ansatte og virksomhetsrepresentanter
- Tydelig skille mellom innbygger- og ansattkontekst kan gi mindre forvirring og mer presis tilgang til riktige tjenester.
- Standardisert innlogging gjør det enklere å bruke flere offentlige tjenester med lignende sikkerhetsmønster.

### For Digdir og offentlig sektor som helhet
- Felles tillitsinfrastruktur gir bedre grunnlag for samordning, drift og sikkerhet enn mange separate løsninger.
- Synlig statistikk for kunder, tjenester og trafikk gir bedre grunnlag for prioritering, forvaltning og videreutvikling.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Rolleforvirring | Ansattporten kan forveksles med ID-porten, Altinn Autorisasjon eller full autorisasjonsløsning | Tydeligere kommunikasjon om ansvar og avgrensning i dokumentasjon og innføring |
| Innføring | Virksomheter kan undervurdere integrasjons- og representasjonskrav | Bruke selvbetjening, metadata og teknisk dokumentasjon aktivt tidlig i innføringen |
| Tilgangsstyring | Tjenesteeiere kan tro at representasjonsgrunnlag automatisk løser all tilgangskontroll | Kreve lokal evaluering av representasjon og tydelig samspill med autorisasjonskomponenter |
| Endringsrisiko | Pilotnære funksjoner som Entra ID kan endre seg raskt | Skille mellom moden kjernefunksjon og funksjoner i videre utforsking |
| Avhengighet | Feil i tillitstjenesten kan ramme mange tjenester samtidig | Ordinær drift, SLA, metadata for robust konfigurasjon og tydelig driftsvarsling |

## Kanaler
- Teknisk dokumentasjon på `docs.digdir.no`
- Selvbetjening via Digdirs kundeløsning i Samarbeidsportalen
- Driftsmeldinger på `status.digdir.no`
- Statistikk på `samarbeid.digdir.no`

## Plattform
Ansattporten er en skybasert fellestjeneste for ansattautentisering med egne protokollendepunkt, metadata, signeringssertifikater og selvbetjeningsoppsett. Plattformrollen ligger i å gjøre autentisering og representasjonsnær innlogging gjenbrukbar på tvers av tjenester, ikke i å overta den underliggende tjenestens autorisasjon eller faglogikk.

## Gjenbruk
**Høy gjenbruksverdi** i tjenester som trenger ansattpålogging eller virksomhetskontekst:
- høy verdi når flere offentlige tjenester trenger samme sikkerhetsmønster i ansattkontekst
- særlig nyttig når autentisering må kunne kombineres med representasjon og datadeling på vegne av virksomhet
- mindre relevant når behovet bare gjelder ordinær innbyggerpålogging eller ren lokal tilgangsstyring

### Vanlige kombinasjoner med andre produkter
- `ID-porten`
- `Altinn Autorisasjon`
- `Maskinporten`
- `Samarbeidsportalen`

**Kildekode:** Ikke offentlig dokumentert.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger** støttes ved at ansattpålogging tilbys som én felles fellestjeneste i stedet for mange lokale varianter.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi Ansattporten gjør det lettere å samordne autentisering i tjenester der flere virksomheter og representasjonsforhold må spille sammen.
- **P7: Sørg for tillit til oppgaveløsningen** er kjerneprinsippet fordi tjenesten skal sikre trygg identitetsbekreftelse og robust innloggingsflyt i virksomhetskontekst.

Vurdering av svakheter og spenninger:
- Ansattporten støtter ikke alene full tilgangsstyring, og det er en viktig spenning mellom enkel innføring og behovet for korrekt lokal autorisasjonslogikk.
- Tjenesten kan også utfordre P1 dersom virksomheter bygger for komplekse representasjonsløp uten å ivareta brukervennlighet for ansatte og virksomhetsrepresentanter.
- Videreutvikling i pilotnære funksjoner som Entra ID gjør at ikke alle deler av ressursen har samme modenhet samtidig.

## Finansiering
**Fakta:** Dokumentasjonen oppgir at Ansattporten per i dag har samme finansieringsmodell som ID-porten, og at kvoten på 200 000 innlogginger er felles for de to portene.

**Fakta:** Samme side oppgir også at finansieringsmodellen trolig vil endres i fremtiden.

**Ikke offentlig verifisert i denne arbeidsøkten:** En samlet oppdatert kostnadsmodell utover denne beskrivelsen er ikke funnet i kildene brukt her.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Offisiell dokumentasjon og Samarbeidsportalen |
| Driftsansvar | Digdir som del av ordinære rutiner for fellesløsningene | Dokumentasjon om ordinær drift og samme SLA som ID-porten |
| Klient- og integrasjonsforvaltning | Digdir via selvbetjening i Samarbeidsportalen | Administrasjonssiden for Ansattporten |
| Autoritativ representasjonskilde | Altinn Autorisasjon er støttet autoritativ kilde for representasjon per i dag | `Hva er Ansattporten?` |
| Budsjett- og finansieringsmodell | Samme hovedmodell som ID-porten, men ikke fullt detaljert offentlig dokumentert | `Hva koster Ansattporten?` |
| Styringsmodell | Del av Digdirs fellestjenesteforvaltning og kundeoppfølging, ikke eget separat styringsorgan i kildene brukt her | Samlet vurdering av docs, statistikk og selvbetjening |

## Lenke til dokumentasjon
- https://docs.digdir.no/docs/ansattporten/ansattporten_om.html
- https://docs.digdir.no/docs/ansattporten/ansattporten_wellknown.html
- https://docs.digdir.no/docs/ansattporten/ansattporten_protocol.html
- https://docs.digdir.no/docs/ansattporten/ansattporten_admin.html
- https://docs.digdir.no/docs/ansattporten/ansattporten_entraid.html
- https://samarbeid.digdir.no/ansattporten/statistikk-ansattporten/3430

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `sources/links.md`
- Lokal fil: `sources/2026-04-10-digdir-virkemiddeloversikt-raw.md`
- Nettkilde: https://docs.digdir.no/docs/ansattporten/ansattporten_om.html (kontrollert 2026-05-18)
- Nettkilde: https://docs.digdir.no/docs/ansattporten/ansattporten_wellknown.html (kontrollert 2026-05-18)
- Nettkilde: https://docs.digdir.no/docs/ansattporten/ansattporten_protocol.html (kontrollert 2026-05-18)
- Nettkilde: https://docs.digdir.no/docs/ansattporten/ansattporten_admin.html (kontrollert 2026-05-18)
- Nettkilde: https://docs.digdir.no/docs/ansattporten/ansattporten_entraid.html (kontrollert 2026-05-18)
- Nettkilde: https://samarbeid.digdir.no/ansattporten/statistikk-ansattporten/3430 (kontrollert 2026-05-18)

## Endringer fra forrige versjon
- Analyseforbedringer: la inn oppdatert grunnlag om ordinær drift, finansieringsmodell, statistikk, selvbetjening, metadata og Entra ID-sporet.
- Tekstlige forbedringer: tydeliggjorde avgrensningen mot ID-porten, Altinn Autorisasjon og lokal autorisasjonslogikk, og løftet styrings- og prinsippvurderingen.
