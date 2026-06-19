# Referansearkitektur forespørsel-svar (eOppslag)

## Navn
Referansearkitektur forespørsel-svar (eOppslag)

## Ressurs ID
DIGDIR-034

## Ressurskategori
Standarder og veiledning

## Type normerende ressurs
Referansearkitektur

## Status/Livsfase
Aktiv. Ressursen er publisert som en av Digdirs nasjonale referansearkitekturer for samhandling.

**Fakta:** Digdir beskriver forespørsel-svar som et generisk mønster for spørring og oppslag, der datakonsument henter eller slår opp data hos en datatilbyder. Digdir beskriver eOppslag som synkrone API-kall mot datatilbyder med tilgangsstyring ved bruk av sikkerhetsbilletter.

## Kort beskrivelse
Referansearkitektur forespørsel-svar (eOppslag) er en normerende ressurs for oppslagsbasert datadeling mellom datakonsument og datatilbyder. Ressursen gir et felles arkitekturmønster for når data bør hentes ved forespørsel, hvordan rollene bør forstås, og hvilke avklaringer som må på plass før virksomheter låser teknisk API-design eller velger operativ løsning.

Ressursen er særlig relevant når en løsning trenger et direkte svar fra en datakilde, for eksempel ved validering, saksbehandling, kontroll, innsyn eller sammenstilling av data fra andre. Den gjør det lettere å skille oppslag fra meldingsforsendelse og hendelsesdrevet samhandling.

## Formål og normerende rolle
Formålet er å etablere en felles arkitekturforståelse for forespørsel-svar som samhandlingsmønster, slik at virksomheter kan kravstille og vurdere oppslagsbasert datadeling på en mer konsistent måte.

Den normerende rollen er styrende og veiledende. Referansearkitekturen er ikke et konkret API eller en ferdig sikkerhetsprofil, men et analyse- og designgrunnlag. Den bør brukes når virksomheter vurderer om synkront oppslag er riktig mønster, når ansvar mellom datatilbyder og datakonsument må avklares, eller når API-baserte samhandlingsløsninger skal sammenlignes mot nasjonale mønstre.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er anbefalt/styrende, ikke generelt obligatorisk som enkeltressurs. Referansearkitekturer brukes normalt som støtte i arkitekturarbeid, men kan få sterkere virkning når de inngår i virksomhetsinterne retningslinjer, sektorvise føringer, anskaffelseskrav eller nasjonale krav og anbefalinger.

**Fakta:** Digdirs referansearkitekturside viser til at referansearkitekturer normalt ikke er pålagt alle å bruke, men at nasjonale føringer kan komme gjennom blant annet digitaliseringsrundskrivet eller Referansekatalogen. Samme side viser til at eMelding og eOppslag bør brukes ved nyutvikling av løsninger for informasjonsutveksling.

Etterlevelse skjer primært gjennom arkitekturbeslutninger, kravarbeid, løsningsdesign, dokumenterte avvik og forvaltning av API-er og datatilganger. Hvis en løsning velger et annet mønster enn eOppslag for et oppslagsbehov, bør valget begrunnes ut fra behov for svartid, robusthet, dataminimering, tilgangsstyring, sporbarhet, ansvar og teknisk gjennomførbarhet.

## Kapabiliteter
- **Bruke data fra andre**

  Referansearkitekturen støtter kapabiliteten ved å beskrive hvordan en datakonsument kan bruke data fra en datatilbyder gjennom et avklart oppslagsmønster. Den gjør det tydelig at bruk av data fra andre ikke bare handler om teknisk API-tilgang, men også om formål, hjemmel eller behandlingsgrunnlag, tilgangsstyring, datakvalitet, svartid, ansvar og sporbarhet.

- **Forvaltningsstandarder**

  Ressursen støtter forvaltningsstandarder ved å gi et felles referansegrunnlag for kravstilling og arkitekturvurdering av oppslagsbasert samhandling. Den standardiserer ikke alle API-kontrakter alene, men gir et normerende mønster som tekniske standarder, sikkerhetsprofiler og operative datadelingstjenester kan bygge videre på.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Arkitekter og integrasjonsmiljøer | Felles mønster for oppslag og API-basert datadeling | Målarkitektur, løsningsdesign og mønstervalg | Kjernebrukere av ressursen |
| Prosjekt- og produktmiljøer | Tydeligere krav til datatilgang, svartid og ansvar | Tidligfase, kravarbeid, anskaffelser og løsningsutvikling | Bør bruke ressursen før API-design låses |
| Datatilbydere | Forutsigbare krav fra konsumenter | Eksponering av data og forvaltning av tilgang | Viktig for kvalitet, kapasitet og ansvar |
| Datakonsumenter | Avklart bruk av data fra andre | Saksbehandling, validering, kontroll, innsyn og tjenestekjeder | Må forstå både tekniske og juridiske vilkår |
| Forvaltnings- og styringsmiljøer | Sammenlignbare vurderinger av oppslagsløsninger | Porteføljestyring, standardisering og gjenbruksvurdering | Relevant når flere løsninger dekker tilgrensende behov |

## Normerende innhold
Ressursen beskriver forespørsel-svar som et generisk mønster for spørring og oppslag. Mønsteret omfatter tilgjengeliggjøring av data og oppslag i data, sett fra henholdsvis datatilbyder og datakonsument.

Digdir beskriver at det generiske mønsteret dekker både asynkrone og synkrone oppslag og ikke tar stilling til kommunikasjonsprotokoll. eOppslag er en mer løsningsnær spesialisering for synkrone API-kall mot en datatilbyder med tilgangsstyring.

Det normerende innholdet bør brukes til å avklare:
- om behovet faktisk gjelder oppslag i data, eller om meldingsutveksling, hendelser, bulkdeling eller annen datadeling passer bedre
- hvilke roller datatilbyder og datakonsument har, og hvem som eier datakvalitet, tilgang og endringer
- hvilke krav som må stilles til formål, hjemmel, tilgangsstyring, sikkerhetsbilletter, logging og sporbarhet
- hvilke krav som gjelder for svartid, tilgjengelighet, feilhåndtering, dataminimering og robusthet
- hvordan API-er, metadata og datakontrakter skal dokumenteres slik at de kan forstås og gjenbrukes

## Bruksområde
Ressursen bør brukes når virksomheter vurderer synkront eller oppslagsbasert samspill med en datatilbyder. Den er særlig relevant når en prosess må hente oppdaterte data før den kan fortsette, eller når en brukerrettet tjeneste trenger sikker og avklart tilgang til data fra andre virksomheter.

Typiske bruksområder er sanntidsvalidering, kontroll av rettigheter eller status, oppslag i registerdata, innhenting av opplysninger til saksbehandling og integrasjon der datakonsument må få et direkte svar fra datatilbyder.

## Typiske analyse- og beslutningssituasjoner
- Når et tiltak må velge mellom forespørsel-svar, meldingsutveksling og hendelsesdrevet samhandling.
- Når en datakonsument trenger tilgang til oppdaterte data fra en datatilbyder.
- Når API-krav, sikkerhetsbilletter, tilgangsstyring og logging må beskrives før anskaffelse eller løsningsdesign.
- Når avhengighet til ekstern datatilbyder påvirker brukeropplevelse, robusthet eller tjenestenivå.
- Når eksisterende API- eller oppslagsløsninger skal vurderes for gjenbruk eller harmonisering.

## Når ressursen normalt ikke er tilstrekkelig alene
Ressursen er ikke tilstrekkelig alene for implementasjon eller drift. Den må suppleres med:
- konkrete API-kontrakter, informasjonsmodeller, begreper og metadata
- tekniske sikkerhetsprofiler, tilgangsstyring, logging og driftskrav
- juridiske avklaringer om formål, behandlingsgrunnlag, taushetsplikt, databehandlerroller og avtaler
- organisatoriske avtaler om datakvalitet, responstid, forvaltningsansvar og feilhåndtering
- operative datadelingstjenester eller API-plattformer der slike er valgt

Den er heller ikke førstevalg når behovet primært er dokument- eller meldingsforsendelse til kjent mottaker, publisering av hendelser til abonnenter, periodisk bulkdeling, generell portalvisning eller bred informasjonsforvaltning uten oppslagsbehov.

## Scope og avgrensning
Inngår:
- generisk mønster for forespørsel-svar og oppslag i data
- beslutningsstøtte for valg av oppslagsbasert samhandling
- konseptuell støtte for roller, ansvar og samspill mellom datatilbyder og datakonsument
- arkitekturfaglig grunnlag for kravstilling og sammenligning av oppslagsløsninger

Inngår ikke:
- komplett API-spesifikasjon eller datakontrakt
- valg av konkret plattform, produkt eller leverandør
- full teknisk sikkerhetsarkitektur
- komplett juridisk avtaleverk eller sektorvis styringsmodell
- operativ drift, overvåking eller hendelseshåndtering

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | Digdir publiserer og vedlikeholder referansearkitekturen som del av nasjonale referansearkitekturer |
| Endringsprosess | Endringer må ses i sammenheng med videreutvikling av referansearkitekturer, datadelingsmønstre og nasjonale krav/anbefalinger |
| Publiserings- og beslutningsarena | Digdir.no og tilhørende referansearkitekturgrunnlag |

**Usikkert:** Det er ikke kontrollert i denne arbeidsøkten om det finnes en egen offentlig endringslogg eller formell beslutningsprosess for eOppslag-dokumentet utover publisering hos Digdir.

## Relasjon til andre ressurser
- **Referansearkitektur forsendelse (eMelding):** komplementært mønster når behovet er meldingsforsendelse til kjent mottaker, heller enn oppslag mot en datatilbyder.
- **Arkitektur for hendelser:** relevant når behovet gjelder publisering av noe som har skjedd, og når én tilbyder ikke bør være tett koblet til kjente konsumenter.
- **Rammeverk for digital samhandling:** bredere ramme for juridisk, organisatorisk, semantisk og teknisk samhandling.
- **Forvaltningsstandarder og referansekatalog:** kan gi mer konkrete krav eller anbefalinger der eOppslag-mønsteret må operasjonaliseres.
- **API-katalog og Felles datakatalog:** relevante oversikter når API-er og datakilder skal beskrives og gjenbrukes.
- **Tillitstjenester:** ID-porten, Maskinporten og andre sikkerhetsmekanismer kan være nødvendige for autentisering, autorisasjon og sikker API-bruk.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er mer forutsigbar tilgang til oppdaterte data i tjenester og prosesser som krever direkte svar. Når datakonsument og datatilbyder beskriver forventninger på samme måte, blir det enklere å avklare ansvar, kvalitet, sikkerhet og tjenestenivå.

Arkitekturverdien ligger særlig i at ressursen kobler teknisk API-bruk til juridiske, organisatoriske og semantiske avklaringer. Den oppdaterte kapabilitetsbeskrivelsen for `Bruke data fra andre` gjør dette viktigere: et godt oppslagsmønster må håndtere formål, datakvalitet, tilgang, metadata, sporbarhet og driftsmessig robusthet, ikke bare teknisk kall og svar.

## Konsekvens ved manglende bruk eller avvik
Hvis ressursen ikke brukes, brukes for sent eller tolkes ulikt, øker risikoen for:
- lokale og usammenlignbare oppslagsmønstre
- uklare rollegrenser mellom datatilbyder og datakonsument
- svakere krav til formål, tilgangsstyring, logging og sporbarhet
- sårbare avhengigheter til eksterne API-er
- feil valg av samhandlingsmønster, for eksempel synkront oppslag der meldingsforsendelse, hendelser eller periodisk datadeling ville vært mer egnet

Avvik kan være riktig i konkrete tilfeller, men bør begrunnes eksplisitt med samhandlingsbehov, sikkerhet, juridiske rammer, brukeropplevelse, robusthet og teknisk gjennomførbarhet.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Mønstervalg | eOppslag brukes der behovet egentlig er forsendelse, hendelser eller bulkdeling | Feil arkitektur, tette avhengigheter og unødvendig last | Sammenlign eksplisitt med eMelding og hendelsesdrevet mønster i tidligfase |
| Juridisk avklaring | Formål, behandlingsgrunnlag eller taushetsplikt avklares for sent | Forsinket innføring og svak etterlevelse | Gjør juridisk samhandlingsanalyse før API-tilgang etableres |
| Organisatorisk ansvar | Datatilbyder og datakonsument har ulik forståelse av kvalitet, responstid og feilhåndtering | Uforutsigbare tjenester og konflikter om ansvar | Etabler tydelige avtaler om tjenestenivå, datakvalitet og endringsvarsling |
| Semantisk kvalitet | Dataelementer, begreper og koder tolkes ulikt | Feil bruk av data og manuell oppfølging | Koble API-et til begreper, informasjonsmodeller og metadata |
| Teknisk robusthet | Synkrone kall gir sterke avhengigheter til ekstern tilbyder | Dårlig brukeropplevelse og sårbarhet ved feil | Vurder caching, feilhåndtering, nedbrytningsstrategi og alternative mønstre |
| Adopsjon | Ressursen blir ikke brukt i kravstilling og anskaffelser | Lokale særmønstre og høyere integrasjonskostnad | Legg referansearkitekturen inn som fast sjekkpunkt i arkitekturbeslutninger |

## Publiseringsform og tilgjengelighet
Ressursen publiseres som del av Digdirs åpne referansearkitekturer. Hovedsiden gir kontekst for referansearkitekturer generelt og peker videre til eOppslag-dokumentasjonen.

## Støtter arkitekturprinsipper
- **P2: Ta arkitekturbeslutninger på rett nivå** støttes ved at mønstervalg tas før API-design og plattformvalg låses.
- **P4: Del og gjenbruk data** støttes tydelig ved at ressursen gir mønsterstøtte for trygg og avklart bruk av data fra andre.
- **P5: Del og gjenbruk løsninger** støttes ved at virksomheter kan gjenbruke et felles oppslagsmønster og sammenligne løsninger mot samme grunnlag.
- **P6: Lag digitale løsninger som støtter samhandling** støttes ved at ressursen beskriver hvordan datakonsument og datatilbyder kan samhandle mer forutsigbart.

Vurdering av svakheter og spenninger:
- Ressursen kan gi for svak praktisk effekt hvis den brukes uten konkrete API-kontrakter, metadata, sikkerhetskrav og forvaltningsavtaler.
- Synkrone oppslag kan skape sterkere runtime-avhengigheter enn meldings- eller hendelsesmønstre. I analyser bør ressursen derfor brukes sammen med vurdering av robusthet, responstid, feilstrategi og tjenestekritikalitet.
- Ved bruk i analyser bør ressursen behandles som mønster- og beslutningsgrunnlag, ikke som komplett implementasjonsoppskrift.

## Lenke til dokumentasjon
- https://www.digdir.no/digital-samhandling/referansearkitekturer/2131
- https://www.digdir.no/samhandling/referansearkitekturer/2131

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/normerende-ressurs-canvas.system.md`
- Lokal fil: `config/templates/normerende-ressurs-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.digdir.no/digital-samhandling/referansearkitekturer/2131, kontrollert 2026-06-19

## Endringer fra forrige versjon
- Analyseforbedringer: rekontrollert Digdirs referansearkitekturside 2026-06-19, tydeliggjort eOppslag som synkront oppslagsmønster, forholdet mellom datakonsument og datatilbyder og avgrensning mot eMelding/hendelser.
- Kapabilitetsforbedringer: utvidet kapabilitetsseksjonen i tråd med oppdatert kapabilitetsbeskrivelse for `Bruke data fra andre`, særlig juridisk, organisatorisk, semantisk og teknisk vurdering.
- Tekstlige forbedringer: gjort bruksområde, beslutningssituasjoner, risiko og prinsippvurdering mer direkte anvendelige i senere analyser.
