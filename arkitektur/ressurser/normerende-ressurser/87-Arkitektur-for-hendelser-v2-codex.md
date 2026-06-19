# Arkitektur for hendelser

## Navn
Arkitektur for hendelser

## Ressurs ID
DIGDIR-027

## Ressurskategori
Standarder og veiledning

## Type normerende ressurs
Referansearkitektur / beste praksis

## Status/Livsfase
Aktiv. Ressursen er publisert som del av Digdirs samhandlings- og arkitekturarbeid for hendelser i felles økosystem.

**Fakta:** Digdir beskriver Arkitektur for hendelser i felles økosystem som et grunnlag for å utveksle og agere på hendelser på tvers av virksomheter og tjenester. Ressursen beskrives som konsept og beste praksis, ikke som teknisk løsningsarkitektur.

## Kort beskrivelse
Arkitektur for hendelser er en normerende ressurs for hendelsesdrevet samhandling i offentlig sektor. Ressursen gir et felles grunnlag for hvordan hendelser kan beskrives, publiseres, oppdages, abonneres på og brukes av andre aktører uten at tilbyder og konsument må være tett koblet.

Ressursen er særlig relevant når flere aktører må kunne reagere på at noe har skjedd, for eksempel i tjenestekjeder, registerendringer, proaktive tjenester eller samhandling der polling og punkt-til-punkt-integrasjoner gir for høy kompleksitet. Den bidrar til å skille hendelser fra kommandoer, synkrone oppslag og meldingsforsendelse.

## Formål og normerende rolle
Formålet er å redusere ulik praksis i hendelsesbasert integrasjon og gi virksomheter en tydeligere struktur for valg av mønster, ansvar, begreper, metadata og samspill.

Den normerende rollen er styrende og veiledende. Ressursen er ikke en operativ hendelsesplattform, men et referansegrunnlag for analyse, arkitekturvalg, kravstilling og design av samhandlingsløsninger. Den bør brukes når virksomheter vurderer om hendelser er riktig mønster, når hendelsestyper skal beskrives, eller når flere aktører skal kunne abonnere på eller agere på samme hendelser.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er anbefalt/styrende, ikke generelt obligatorisk som enkeltressurs. Ressursen bør likevel brukes som fast vurderingsgrunnlag når tiltak etablerer hendelsesdrevet samhandling, særlig der hendelser skal deles på tvers av virksomheter eller sektorer.

Etterlevelse skjer gjennom arkitekturbeslutninger, hendelsesmodellering, kravarbeid, løsningsdesign, dokumenterte avvik og forvaltning av hendelsestyper, abonnementer og tilganger. Hvis en løsning velger et annet mønster enn hendelser for et behov der flere aktører skal reagere på endring, bør valget begrunnes ut fra kobling, tid, ansvar, sikkerhet, dataminimering og teknisk gjennomførbarhet.

## Kapabiliteter
- **Hendelsesdrevet**

  Ressursen støtter kapabiliteten ved å beskrive hvordan virksomheter kan publisere og reagere på digitale hendelser når de inntreffer. Den gjør det tydelig at hendelsesdrevet samhandling ikke bare handler om teknologi, men også om hvem som eier hendelsen, hvem som kan abonnere, hvilke metadata og begreper som brukes, hvordan tilgang styres, og hvordan konsumenter håndterer duplikater, rekkefølge, feil og videre prosess.

- **Forvaltningsstandarder**

  Ressursen støtter forvaltningsstandarder ved å gi et felles referansegrunnlag for kravstilling, arkitekturvurdering og harmonisering av hendelsesbaserte løsninger. Den standardiserer ikke alle tekniske detaljer alene, men gir et normerende mønster som hendelsesplattformer, kataloger, API-er og sikkerhetsmekanismer kan bygge videre på.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Arkitekter og integrasjonsmiljøer | Felles mønster for hendelsesdrevet samhandling | Målarkitektur, løsningsdesign og mønstervalg | Kjernebrukere av ressursen |
| Produkt- og prosjektmiljøer | Klarere valg i integrasjonsløp | Tidligfase, kravarbeid, anskaffelser og løsningsutvikling | Bør bruke ressursen før teknisk plattform låses |
| Hendelsestilbydere | Beskrive og publisere hendelser på en forutsigbar måte | Hendelsesmodellering, metadata, tilgang og forvaltning | Må eie kvalitet og endringsvarsling for hendelser |
| Hendelseskonsumenter | Abonnere på og reagere på relevante hendelser | Automatisering, proaktive tjenester og tjenestekjeder | Må håndtere feil, duplikater og egen prosess |
| Forvaltnings- og styringsmiljøer | Sammenlignbare vurderinger av hendelsesløsninger | Porteføljestyring, standardisering og gjenbruksvurdering | Relevant når flere løsninger dekker tilgrensende behov |

## Normerende innhold
Ressursen beskriver hendelser som informasjon om noe som har skjedd, typisk en endring i tilstand. Dette skiller hendelser fra kommandoer, som uttrykker noe som skal gjøres og der mottaker forventes å utføre en handling og gi respons.

Digdir beskriver hovedprinsippet som at hendelser sendes ut når en tilstand endrer seg. Tilbyder publiserer hendelsen, og én eller flere konsumenter kan agere på hendelsen når de gjenkjenner den. Dette gir løsere kobling, énveis kommunikasjon og mindre behov for styrende kommandoer.

Det normerende innholdet bør brukes til å avklare:
- om behovet faktisk gjelder en hendelse, eller om forespørsel-svar, meldingsforsendelse eller annen datadeling passer bedre
- hvem som eier hendelsen, og hvem som kan publisere, abonnere på og bruke hendelsen
- hvilke metadata, begreper, hendelsestyper og informasjonsinnhold som må standardiseres
- hvordan tilgangsstyring, avtaler, sikkerhet, logging og dataminimering skal ivaretas
- hvordan konsumenter skal håndtere idempotens, rekkefølge, duplikater, retry, feil og eventuell forsinket behandling
- hvordan hendelser skal beskrives og gjøres oppdagbare for andre aktører

## Bruksområde
Ressursen bør brukes når virksomheter vurderer hendelsesbasert integrasjon, abonnementsmønstre, publisering av tilstandsendringer eller behov for mer løst koblet samhandling enn klassiske forespørsel-svar-mønstre gir.

Den er særlig relevant når flere aktører kan ha interesse av samme hendelse, når tilbyder ikke bør ha tett kjennskap til alle konsumenter, eller når tjenestekjeder bør kunne utvikles mer dynamisk. Ressursen er også relevant når hendelser skal støtte proaktive tjenester, dataminimering eller reduksjon av polling.

## Typiske analyse- og beslutningssituasjoner
- Når et tiltak må velge mellom hendelsesdrevet samhandling, forespørsel-svar og meldingsutveksling.
- Når flere aktører må kunne reagere på samme tilstandsendring.
- Når tjenestekjeder bør bygges med løs kobling og koreografi heller enn tung orkestrering.
- Når hendelsestyper, metadata, tilgang og abonnement må beskrives før anskaffelse eller løsningsdesign.
- Når polling, punkt-til-punkt-integrasjoner eller tette runtime-avhengigheter gir for høy kompleksitet.
- Når hendelser må gjøres oppdagbare gjennom katalog, dokumentasjon eller felles begreper.

## Når ressursen normalt ikke er tilstrekkelig alene
Ressursen er ikke tilstrekkelig alene for implementasjon eller drift. Den må suppleres med:
- konkrete hendelsesplattformer, meldingsinfrastruktur, API-er eller katalogløsninger der slike er valgt
- tekniske standarder for hendelsesformat, metadata, grensesnitt, sikkerhet og abonnement
- juridiske avklaringer om formål, behandlingsgrunnlag, taushetsplikt, avtaler og tilgang til hendelser
- organisatoriske avtaler om hendelseseierskap, tjenestenivå, endringsvarsling, feilhåndtering og konsumentansvar
- operativ dokumentasjon for retry, duplikathåndtering, overvåking, logging og hendelseslivsløp

Den er heller ikke førstevalg når behovet primært er synkront oppslag mot en datakilde, dokument- eller meldingsforsendelse til kjent mottaker, eller styrende kommandoer der én bestemt mottaker skal utføre en handling.

## Scope og avgrensning
Inngår:
- konseptuelt og arkitekturfaglig grunnlag for hendelsesdrevet samhandling
- støtte til å skille hendelser fra kommandoer, oppslag og meldingsforsendelse
- beslutningsstøtte for publisering, abonnement, roller og ansvar
- vurderingspunkter for metadata, tilgang, sikkerhet, dataminimering og oppdagbarhet
- grunnlag for samordning mellom hendelsestilbydere, konsumenter og plattformmiljøer

Inngår ikke:
- drift av hendelsesinfrastruktur
- full teknisk spesifikasjon for konkrete produkter eller protokoller
- komplett hendelseskatalog eller operativ plattform
- ferdig juridisk avtaleverk
- full metode for prosjektgjennomføring eller porteføljestyring

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | Digdir publiserer og vedlikeholder ressursen som del av samhandlings- og arkitekturgrunnlaget |
| Endringsprosess | Endringer må ses i sammenheng med videreutvikling av felles økosystem, referansearkitekturer og nasjonale krav/anbefalinger |
| Publiserings- og beslutningsarena | Digdir.no og tilhørende arkitekturgrunnlag |

**Usikkert:** Det er ikke kontrollert i denne arbeidsøkten om ressursen har en egen offentlig endringslogg eller formell beslutningsprosess utover publisering hos Digdir.

## Relasjon til andre ressurser
- **Referansearkitektur forespørsel-svar (eOppslag):** komplementært mønster når behovet er direkte oppslag eller spørring mot datatilbyder.
- **Referansearkitektur forsendelse (eMelding):** komplementært mønster når behovet er meldingsforsendelse til kjent mottaker.
- **Rammeverk for digital samhandling:** bredere ramme for juridisk, organisatorisk, semantisk og teknisk samhandling.
- **Felles datakatalog / data.norge.no:** relevant når hendelser og relasjoner til tjenester, datasett og API-er skal beskrives og gjøres oppdagbare.
- **Operative hendelsestjenester:** Altinn Events, Dialogporten-hendelser og andre hendelsesflater kan være gjennomføringsflater, men de erstatter ikke behovet for mønstervalg og arkitekturbeslutning.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er raskere og mer fleksibel reaksjon på endringer i data, tjenester eller livsløp. Hendelser kan gjøre det mulig å tilby mer proaktive tjenester, redusere manuell oppfølging og la flere aktører bruke samme hendelse uten at tilbyder må bygge egne integrasjoner til hver konsument.

Arkitekturverdien ligger særlig i løsere kobling, mindre polling, bedre oppdagbarhet og mer dynamiske tjenestekjeder. Den oppdaterte kapabilitetsbeskrivelsen for `Hendelsesdrevet` gjør dette viktigere: et godt hendelsesmønster må håndtere juridisk tilgang, organisatorisk ansvar, semantisk presisjon og teknisk robusthet, ikke bare publisering av tekniske meldinger.

## Konsekvens ved manglende bruk eller avvik
Hvis ressursen ikke brukes, brukes for sent eller tolkes ulikt, øker risikoen for:
- lokale og usammenlignbare hendelsesmønstre
- at aktiviteter, kommandoer og hendelser blandes sammen
- uklart eierskap til hendelsestyper, metadata, tilgang og endringsvarsling
- svakere oppdagbarhet og gjenbruk av hendelser
- tette punkt-til-punkt-integrasjoner og unødvendig polling
- feil valg av samhandlingsmønster, for eksempel hendelser der synkront oppslag eller meldingsforsendelse ville vært mer egnet

Avvik kan være riktig i konkrete tilfeller, men bør begrunnes eksplisitt med samhandlingsbehov, sikkerhet, juridiske rammer, konsumentmodell, hendelseskritikalitet og teknisk gjennomførbarhet.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Mønstervalg | Hendelser brukes der behovet egentlig er oppslag, kommando eller forsendelse | Feil arkitektur og unødvendig kompleksitet | Sammenlign eksplisitt med eOppslag og eMelding i tidligfase |
| Begrepsforståelse | Aktiviteter, kommandoer og hendelser blandes sammen | Uklar integrasjon og feil forventninger hos konsumenter | Definer hendelser som tilstandsendringer i fortid, med tydelig hendelseseier |
| Juridisk tilgang | Hendelser inneholder eller indikerer beskyttede opplysninger | Brudd på regelverk eller for bred tilgang | Avklar formål, hjemmel, avtaler og dataminimering før publisering |
| Organisatorisk ansvar | Tilbyder og konsument har ulik forståelse av ansvar, levetid og kvalitet | Feil bruk av hendelser og manglende oppfølging | Etabler forvaltning av hendelsestyper, metadata og endringsvarsling |
| Semantisk kvalitet | Hendelsestyper og payload tolkes ulikt | Lav interoperabilitet og manuell oppfølging | Koble hendelser til begreper, informasjonsmodeller og katalogbeskrivelser |
| Teknisk robusthet | Konsumenter håndterer duplikater, rekkefølge eller retry feil | Feil prosessering og ustabil tjenestekjede | Still krav til idempotens, feilhåndtering, logging og overvåking |
| Adopsjon | Ressursen blir ikke brukt i kravstilling og anskaffelser | Lokale særmønstre og høyere integrasjonskostnad | Legg hendelsesmønster inn som fast sjekkpunkt i arkitekturbeslutninger |

## Publiseringsform og tilgjengelighet
Ressursen publiseres som åpen samhandlings- og arkitekturressurs på digdir.no. Sidene gir både innledning, arkitekturbeskrivelse, samspill, eksempler, business case og kilder.

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov** støttes ved at hendelser kan gjøre tjenester mer proaktive og bedre tilpasset faktiske endringer i brukerens situasjon.
- **P2: Ta arkitekturbeslutninger på rett nivå** støttes ved at mønstervalg, hendelseseierskap og samhandlingsform vurderes før teknisk plattform låses.
- **P5: Del og gjenbruk løsninger** støttes ved at hendelser og samhandlingsmønstre kan gjenbrukes på tvers av tjenester og konsumenter.
- **P6: Lag digitale løsninger som støtter samhandling** støttes tydelig, fordi ressursen beskriver hvordan virksomheter kan samhandle gjennom løsere koblede hendelser.

Vurdering av svakheter og spenninger:
- Ressursen kan gi for svak praktisk effekt hvis den ikke kobles til konkrete hendelsesplattformer, kataloger, sikkerhetsmekanismer og forvaltningsavtaler.
- Hendelser kan gi utydelig ansvar hvis tilbyder publiserer uten tydelige metadata, tilgangskontroll og konsumentforventninger.
- Ved bruk i analyser bør ressursen behandles som mønster- og beslutningsgrunnlag, ikke som komplett implementasjonsoppskrift.

## Lenke til dokumentasjon
- https://www.digdir.no/digital-samhandling/innledning/4169
- https://www.digdir.no/samhandling/arkitektur-hendelser/4691
- https://www.digdir.no/digital-samhandling/referansearkitekturer/2131

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/normerende-ressurs-canvas.system.md`
- Lokal fil: `config/templates/normerende-ressurs-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.digdir.no/digital-samhandling/innledning/4169, kontrollert 2026-06-19
- Nettkilde: https://www.digdir.no/digital-samhandling/referansearkitekturer/2131, kontrollert 2026-06-19

## Endringer fra forrige versjon
- Analyseforbedringer: rekontrollert Digdirs hendelsesarkitektursider 2026-06-19, tydeliggjort hendelser som tilstandsendringer, forskjellen mellom hendelser og kommandoer, og avgrensning mot eOppslag/eMelding.
- Kapabilitetsforbedringer: utvidet kapabilitetsseksjonen i tråd med oppdatert kapabilitetsbeskrivelse for `Hendelsesdrevet`, særlig juridisk, organisatorisk, semantisk og teknisk vurdering.
- Tekstlige forbedringer: gjort bruksområde, beslutningssituasjoner, risiko og prinsippvurdering mer direkte anvendelige i senere analyser.
