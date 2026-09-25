# Kart for tjenestekjeder

## Navn
Kart for tjenestekjeder

## Ressurs ID
DIGDIR-032

## Ressurskategori
Standarder og veiledning

## Type standard eller veiledning
Metodeverktøy

## Status/Livsfase
Aktiv. Verktøyet er publisert på digdir.no som støtte for kartlegging av tjenestekjeder og samhandling.

## Kort beskrivelse
Kart for tjenestekjeder er et metodeverktøy for å identifisere tjenestekjeder og tjenester, og for å synliggjøre sammenhenger, avhengigheter og overgangspunkter i tverrvirksomhetlige tjenesteforløp.

**Fakta:** Digdir beskriver formålet som å «bryte opp kompleksiteten gjennom å vise hvilke tjenester som trigges av en hendelse, og hvilke data som opprettes eller endres». Kartet tar utgangspunkt i brukerreisen, og viser i tillegg hvor det er «brudd/hindringer på juridisk, organisatorisk, semantisk eller teknisk nivå».

**Fakta:** Kartet viser aktørene som er tjenesteleverandører, men uttrykkelig ikke prosessene for å levere tjenesten. Det er den viktigste avgrensningen mot et prosesskart.

Det er hendelsen som binder radene sammen. Kartet leses ikke som et prosesskart over én virksomhets arbeidsflyt, men som en kjede der en hendelse i brukerreisen utløser tjenester hos flere aktører, som i sin tur leser eller endrer data i bestemte kilder.

Kartet er ikke en selvstendig publikasjon. Det tilbys som mal i verktøyet bak `Sjekkliste for sammenhengende tjenester`, der tjenestekjede-området omtales som kjernen i verktøyet.

## Formål og normerende rolle
Formålet er å gi virksomheter et felles grep for å kartlegge hvordan tjenester henger sammen, hvor friksjon oppstår, og hvilke avklaringer som trengs for å forbedre helheten.

Den normerende rollen er metodisk. Verktøyet er ikke en operativ løsning, men en analyse- og designramme som bør brukes i tidligfase og samordningsarbeid.

**Deduksjon:** Det normerende ligger i radinndelingen, ikke i et pålegg om å bruke verktøyet. Når flere virksomheter kartlegger etter samme inndeling, blir kartene sammenlignbare, og gap kan diskuteres på samme grunnlag. Effekten forsvinner hvis hver aktør velger sin egen inndeling.

## Forpliktelsesnivå og etterlevelse
Forpliktelsesnivået er **anbefalt**. Verktøyet er ikke rettslig bindende, og det finnes ingen hjemmel som pålegger virksomheter å bruke det.

**Fakta:** Kildene oppgir ingen rettslig forankring. Kartet er utgitt av Digitaliseringsdirektoratet og presenteres som en frivillig arbeidsmetode for virksomheter som skal utvikle sammenhengende tjenester på tvers.

**Deduksjon:** Binding kan likevel oppstå indirekte. Digitaliseringsrundskrivet og krav i medfinansieringsordningen stiller forventninger til utredning av tverrgående tiltak, og kartlegging av tjenestekjeden er en praktisk måte å møte dem. Det er ikke det samme som at verktøyet er pålagt, og koblingen er ikke dokumentert i kildene som er brukt her.

Etterlevelse skjer gjennom tjenestedesign, arkitekturanalyse, konseptutredning og porteføljestyring. Fordi nivået er anbefalt, er avvik ikke brudd, men svekker helhetsforståelsen i tverrgående tiltak.

## Kapabiliteter
Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Digdirs side for kart for tjenestekjeder og mot malen i verktøydokumentasjonen.

- **Sluttbrukertjenester: Tjenestekjeder** normeres i designfasen. Kapabiliteten er evnen til å sette sammen, koordinere og automatisere informasjonsflyt og prosesser på tvers av uavhengige tjenester. Kartet foreskriver hvordan en slik kjede skal beskrives før den kan koordineres: hvilken hendelse som utløser tjenester hos hvilke aktører, hvilke data som opprettes eller endres i hvilke kilder, og hvor flyten brytes på juridisk, organisatorisk, semantisk eller teknisk nivå. Det er samme inndeling som definisjonen bruker for hva kapabiliteten innebærer. Kartet normerer ikke selve integrasjonen eller automatiseringen, som hører hjemme i operative løsninger og i `Arkitektur for hendelser`.
- **Samarbeid: Organisatorisk samhandling** normeres gjennom at kartet navngir aktører og tjenesteleverandører per tjeneste. Ansvarsovergangene blir synlige, og det er dem samordningen må håndtere.

**Deduksjon:** `Strategisk styring: Samordning` ble oppgitt i `v1`, men er tatt ut. Kartet gir et bedre grunnlag for samordning, men normerer ikke selve samordningen: det er hverken styringsmodell, mandat eller beslutningsprosess. Samordning er en effekt av å bruke verktøyet, ikke en evne verktøyet foreskriver.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Arkitekter og designmiljøer | Strukturert kartlegging av samspill | Analyse av tjenestekjeder | Kjernebrukere |
| Prosjekt- og produktmiljøer | Felles situasjonsforståelse | Tidligfase og konseptarbeid | Relevans før løsningsvalg |
| Ledelse og samordningsmiljøer | Bedre beslutningsgrunnlag | Prioritering og koordinering | Viktig ved tverrgående initiativ |
| Tjenesteutviklere | Oversikt over hvilke data som berøres | Design av tjenester i kjeden | Malen har egne rader for data/register og applikasjon |

## Normerende innhold
Det normerende innholdet er radinndelingen malen krever, og fasene den leses i.

**Fakta:** Malen har én kolonne per fase, og følgende rader:

1. **Brukerreise** – aktivitetene brukeren utfører.
2. **Hendelse** – hva som oppstår i eller utløses av reisen.
3. **Tjeneste levert av** – én rad per aktør, slik at det går fram hvem som leverer hva.
4. **Data/register** – hvilke data som opprettes eller endres, og i hvilke kilder.
5. **Applikasjon** – løsningene som understøtter tjenestene.

**Fakta:** I tillegg skal kartet vise hvor det er brudd eller hindringer på juridisk, organisatorisk, semantisk eller teknisk nivå. Det er de fire samhandlingsnivåene fra `Rammeverk for digital samhandling`.

Den normerende verdien ligger i to valg. Det første er at hendelsen er bindeleddet: ved å gjøre den til eget rad tvinger malen fram spørsmålet om hva som faktisk utløser noe hos en annen aktør, framfor å beskrive hver virksomhets prosess for seg. Det andre er at aktørene får én rad hver, men at prosessene deres holdes utenfor. Kartet skal vise ansvarsfordeling og overganger, ikke intern arbeidsflyt.

**Deduksjon:** Brudd-dimensjonen er det som skiller kartet fra en ren oversikt. Uten den blir kartet en beskrivelse av hvordan kjeden ser ut; med den blir det et analyseverktøy som peker ut hvor kjeden svikter og på hvilket nivå problemet må løses.

## Bruksområde
Verktøyet bør brukes ved etablering eller forbedring av sammenhengende tjenester, særlig når flere forvaltningsnivåer eller virksomheter må koordinere innsats.

Det er spesielt nyttig i tidlig fase for å avklare hva som faktisk er den samlede tjenestekjeden, før prioriteringer og løsningsvalg låses.

## Typiske analyse- og beslutningssituasjoner
- når et tverrvirksomhetlig tjenesteforløp skal avgrenses
- når ansvarsoverganger og avhengigheter er uklare
- når flaskehalser og dobbeltarbeid må identifiseres
- når styringsnivå trenger et felles bilde av kjeden før prioritering
- når det er uklart hvilke registre og datakilder som berøres av en endring i kjeden

## Når ressursen normalt ikke er tilstrekkelig alene
Verktøyet er ikke tilstrekkelig alene for realisering. Det må suppleres med tjenestedesign, arkitekturprinsipper, prosjektmetodikk, juridiske vurderinger og operative løsninger.

Kartet sier hva som henger sammen, ikke hva som bør gjøres med det. Prioritering og gjennomføring hører i styrings- og prosjektløpet.

## Scope og avgrensning
Inngår:
- kartlegging av brukerreise, hendelser, tjenester per aktør, data og applikasjoner, fordelt på faser
- markering av brudd og hindringer på juridisk, organisatorisk, semantisk og teknisk nivå
- støtte til analyse og samordning i tidligfase
- grunnlag for prioritering av forbedringstiltak

Inngår ikke:
- prosessene aktørene bruker for å levere tjenestene sine
- detaljert teknisk design av integrasjoner
- full prosessmetodikk for prosjektgjennomføring
- operativ drift av tjenester
- styringsmodell eller beslutningsmandat for samordningen kartet peker på

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | Digdir publiserer og vedlikeholder metodeinnholdet |
| Endringsprosess | Oppdateres ved videreutvikling av samhandlingsarbeid og veiledning |
| Publiserings- og beslutningsarena | Digdir.no |

## Relasjon til andre ressurser
- **Sjekkliste for sammenhengende tjenester**: verktøyet som tilbyr denne malen. Kartet er et arbeidsområde inne i det verktøyet, ikke en frittstående publikasjon.
- **Rammeverk for digital samhandling**: leverer de fire samhandlingsnivåene kartet bruker for å klassifisere brudd og hindringer.
- **Prosjektveiviseren**: støtter hvordan innsikt fra kartleggingen omsettes i styrte tiltak.
- **Arkitektur for hendelser**: dekker den tekniske siden av hendelsene som utgjør nivå to i kartet.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er bedre koordinering, færre blindsoner og mer treffsikre prioriteringer i komplekse forløp. Arkitekturverdien er tydeligere avhengighetsbilde, bedre samhandlingsdesign og mindre risiko for lokal suboptimalisering.

## Konsekvens ved manglende bruk eller avvik
Uten kartlegging av tjenestekjeder kan virksomheter gjøre forbedringer isolert, med risiko for at problemer flyttes i stedet for løses. Dette gir ofte fragmentering, lavere brukeropplevelse og svakere samordning.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Forankring | Kartleggingen blir engangsøvelse | Lite varig effekt | Koble innsikt til styring og prioritering |
| Avgrensning | Kjedegrensene settes for snevert | Viktige avhengigheter overses | Validere kart med flere aktører |
| Adopsjon | Ulik metodebruk mellom miljøer | Lav sammenlignbarhet | Bruke felles mal og begrepsbruk |
| Detaljnivå | Kartet fylles med prosessdetaljer per virksomhet | Nivåinndelingen mister funksjonen | Holde nivå tre på tjeneste, ikke på arbeidsflyt |
| Ferskhet | Kartet speiler kjeden slik den var ved kartleggingen | Beslutninger på utdatert bilde | Angi kartleggingstidspunkt og revurdere ved endring |

## Publiseringsform og tilgjengelighet
Verktøyet publiseres som åpen metode- og veiledningsressurs på digdir.no.

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov** ved at nivå én er brukerreisen, ikke virksomhetens prosess.
- **P2: Ta arkitekturbeslutninger på rett nivå** ved å løfte tverrgående avhengigheter tidlig.
- **P6: Lag digitale løsninger som støtter samhandling** ved å synliggjøre samspill mellom aktører og løsninger.

Svakheter, spenninger og begrensninger mot prinsippene: Verktøyet må brukes sammen med andre virkemidler for at kartlegging faktisk fører til gjennomførte forbedringer. Det ligger også en spenning mot `P2`: kartet gjør avhengigheter synlige, men peker ikke ut hvilket nivå som skal beslutte noe om dem. Et kart som avdekker at ansvaret ligger spredt, gir ingen mekanisme for å samle det, og uten et styringsspor kan kartleggingen ende som dokumentasjon av et problem framfor et grunnlag for å løse det.

## Lenke til dokumentasjon
- https://www.digdir.no/samhandling/kart-tjenestekjeder/4168
- https://www.digdir.no/samhandling/nasjonal-arkitektur/2150

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-09-17
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-17
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-17
- https://www.digdir.no/samhandling/kart-tjenestekjeder/4168 , kontrollert 2026-09-17
- https://www.digdir.no/samhandling/nasjonal-arkitektur/2150 , kontrollert 2026-04-30, ikke rekontrollert i denne kjøringen
- https://www.digdir.no/media/1850/download , malen og avgrensningene er hentet fra lysbildene `Kart for tjenestekjeder`, `Om verktøyet` og malarket i verktøydokumentasjonen, kontrollert 2026-09-17

## Endringer fra forrige versjon

### Analyseforbedringer
- Radinndelingen i malen er skrevet inn under `Normerende innhold`, med hendelsen som bindeledd. `v1` beskrev at ressursen «gir metode for å kartlegge aktører, prosessledd, avhengigheter og informasjonsoverganger», men gjenga ikke selve inndelingen. Det er inndelingen som er det normerende, og uten den var beskrivelsen ikke etterprøvbar. Merk at nettsiden oppgir fire nivåer, mens malen i verktøydokumentasjonen har fem rader og i tillegg er delt i faser. Beskrivelsen følger malen.
- Brudd-dimensjonen er lagt inn. Kartet skal vise hvor det er brudd eller hindringer på juridisk, organisatorisk, semantisk eller teknisk nivå, altså de fire samhandlingsnivåene fra `Rammeverk for digital samhandling`. Dette manglet helt i `v1`, og er det som gjør kartet til et analyseverktøy framfor en oversikt.
- Avgrensningen mot prosess er skrevet inn: kartet viser aktørene som er tjenesteleverandører, men uttrykkelig ikke prosessene for å levere tjenesten.
- Forholdet til `Sjekkliste for sammenhengende tjenester` er rettet. `v1` framstilte sjekklista som noe som kommer etter kartleggingen. I virkeligheten er kartet en mal som tilbys inne i sjekkliste-verktøyet, der tjenestekjede-området omtales som kjernen i verktøyet.
- Rettslig forankring er avklart etter regelen fra 2026-09-13. `v1` oppgav `anbefalt/styrende` uten å si hva styringen bygde på. `v2` sier eksplisitt at det ikke finnes hjemmel, og skiller ut som deduksjon at binding kan oppstå indirekte gjennom digitaliseringsrundskrivet og medfinansieringsordningen, uten at kildene her dokumenterer den koblingen.
- `Strategisk styring: Samordning` er tatt ut. Koblingen sto i `v1`, men fantes verken i registeret eller kapabilitetsmappingen. Avviket er ryddet i konservativ retning: kartet gir grunnlag for samordning, men er hverken styringsmodell, mandat eller beslutningsprosess, så samordning er en effekt av bruk framfor en evne verktøyet foreskriver.
- Kapabilitetspunktene har fått forklaring i selve fila, slik malen krever. `v1` listet bare navn, mens forklaringene bare fantes i kapabilitetsmappingen.
- `Utfordringer og risiko` er utvidet med to reelle feilmåter: at nivå tre fylles med prosessdetaljer per virksomhet slik at inndelingen mister funksjonen, og at kartet speiler kjeden slik den var ved kartleggingen.
- Prinsippvurderingen har fått avsnittet om spenning og begrensning som malen ber om, med spenningen mot `P2`: kartet synliggjør spredt ansvar men gir ingen mekanisme for å samle det.

### Tekstlige forbedringer
- Formuleringen «Ressursen er viktig fordi» er fjernet fra `Kort beskrivelse`. AGENTS.md krever at beskrivelsen sier hva ressursen gjør, ikke hvorfor den er interessant.
- Brødteksten som sto etter kulelista i `Kapabiliteter` er fjernet. AGENTS.md krever at avsluttende tekst står før lista, fordi `sync-resource-metadata.py` ellers trekker den inn i forklaringen for den siste kapabiliteten.
- Fakta og deduksjon er merket gjennom dokumentet. `v1` hadde ingen slike merker.
- `Arkitektur for hendelser` er lagt til under `Relasjon til andre ressurser`, siden den dekker den tekniske siden av nivå to.
