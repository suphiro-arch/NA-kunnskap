# Produkt-canvas: Felles studentsystem (FS)

## Navn
Felles studentsystem (FS)

## Ressurs ID
SIKT-002

## Status/Livsfase
**Produksjon** - etablert nasjonal studieadministrativ plattform for universiteter, høgskoler og fagskoler.

**Fakta:** Sikt beskriver FS som et studentinformasjonssystem som brukes til studieadministrasjon ved de fleste universiteter og høgskoler i Norge. Produktet består av databaser, integrasjoner og brukerapplikasjoner, og omtales også som en nasjonal digital grunnmur for høyere utdanning.

## Modenhet
**Høy modenhet** - langvarig og innarbeidet sektorløsning:
- FS har vært et informasjonsnav i norsk høyere utdanning siden 1996.
- Produktet brukes i sentrale studieadministrative prosesser gjennom hele studieløpet.
- FS har både etablerte brukerflater og et voksende API- og integrasjonslandskap.
- Sikt publiserer nå også et modernisert produktområde på `fs.sikt.no` med tjenestekatalog, API-katalog og utviklerinformasjon.

**Deduksjon:** Modenheten er høy fordi FS både er en operativ kjerneplattform i sektoren og en videreutviklet digital plattform med tydelige grensesnitt for integrasjon og modernisering.

## Kort beskrivelse
Felles studentsystem (FS) er den nasjonale plattformen for studieadministrative data og prosesser i høyere utdanning. Produktet forvalter og tilgjengeliggjør informasjon om studenter, studier, opptak, resultater og kvalifikasjoner, og fungerer som informasjonsnav for både interne arbeidsprosesser, studentnære tjenester og maskinell datadeling. FS er derfor mer enn ett administrativt system: det er den felles sektorløsningen som gjør det mulig å bygge sammenheng mellom studieadministrasjon, opptak, resultatutveksling og videre bruk av studentdata.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** er relevant fordi FS inngår i flere samhandlingsløp og mottar opplysninger i studieadministrative prosesser.
- **Datautveksling og integrasjon: Dele data med andre** er en kjernefunksjon ved at FS tilbyr API-er, meldingskøer og andre integrasjonsflater for videre bruk av data.
- **Informasjonsforvaltning: Datastyring** er sentralt fordi FS forvalter, strukturerer og vedlikeholder store mengder studie- og studentdata som grunnlag for mange prosesser.
- **Samarbeid: Organisatorisk samhandling** er relevant fordi FS er en felles sektorløsning som brukes av mange institusjoner med Sikt som felles forvalter.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Sikts tjenestesider, FS-dokumentasjonen og API-katalogen.

## Produktmål
**Primærkilder:** Sikts sider for `Felles studentsystem`, `fs.sikt.no` og teknisk dokumentasjon for FS-API.

Dokumenterte mål:
- Støtte studieadministrasjon ved universiteter og høgskoler.
- Forvalte, foredle og formidle prosesser og data om studier og studenter.
- Legge til rette for digitalisering og effektivisering i offentlig sektor gjennom løsninger for studenter, ansatte og utviklere.

Operative mål utledet fra de samme kildene:
- Gi sektoren et felles og sammenhengende datagrunnlag for studieadministrative prosesser.
- Gjøre student- og studiedata tilgjengelige i standardiserte og mer moderne grensesnitt.
- Understøtte samspill mellom institusjonenes lokale behov og felles nasjonale prosesser og tjenester.

## Brukerbehov
- Universiteter, høgskoler og fagskoler trenger en felles plattform for studieadministrative prosesser.
- Studieadministrative og vitenskapelige ansatte trenger arbeidsflater for registrering, vedlikehold og saksbehandling.
- Studenter og søkere trenger digitale tjenester som bygger på oppdaterte studie- og studentdata.
- Utviklere og integrasjonsmiljøer trenger API-er og dokumenterte tilgangsløp til data i FS.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Utdanningsinstitusjoner | Felles studieadministrativ plattform | Studieplanlegging, studentoppfølging, opptak og resultatforvaltning | Hovedbrukere av produktet |
| Studieadministrative ansatte | Arbeidsverktøy og saksstøtte | Registrering, vedlikehold og behandling av studiesaker | Bruker FS-klient og nye arbeidsflater |
| Studenter og søkere | Digitale tjenester basert på egne data | Studentforløp, resultater og andre selvbetjeningsløp | Møter produktet via tilknyttede tjenester |
| Utviklere og integratører | API-er og teknisk dokumentasjon | Integrasjon, datadeling og hendelsesnære løsninger | Viktig for gjenbruksverdi |
| Sikt og sektorfellesskapet | Felles forvaltning og modernisering | Videreutvikling, standardisering og drift | Produktet er felles sektorinfrastruktur |

## Hovedfunksjoner
### Primære funksjoner
**Forvaltning av student- og studiedata.** FS holder orden på sentrale data om studenter, utdanningstilbud, opptak, studieforløp, resultater og kvalifikasjoner. Dette gjør produktet til sektorens sentrale informasjonsnav for studieadministrasjon.

**Støtte for studieadministrative prosesser.** Produktet dekker arbeidsprosesser innen studieplanlegging, studiegjennomføring, studentoppfølging, opptak og resultatforvaltning. FS er derfor ikke bare en database, men en operativ plattform for løpende saks- og prosessarbeid.

**Tilgjengeliggjøring gjennom API-er og integrasjoner.** Sikt beskriver både et felles REST API, ny API-katalog og moderniserte grensesnitt. Produktet har dermed en tydelig rolle som delings- og integrasjonsplattform, ikke bare som intern sektorapplikasjon.

**Felles sektorplattform med modernisering og overgang til nye tjenester.** `fs.sikt.no` viser at FS utvikles videre med nye brukerflater, nasjonale registre og API-er. Produktet omfatter derfor både etablert kjernefunksjonalitet og et modernisert målbilde for sektoren.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Felles studentinformasjonssystem for høyere utdanning | Hele utdanningssektorens øvrige portefølje utenfor studieadministrasjon |
| Databaser, integrasjoner og brukerapplikasjoner i FS | Alle lokale arbeidsprosesser som institusjonene løser utenfor FS |
| API-er og tekniske grensesnitt for viderebruk av data | Rene sluttbrukerportaler som ikke er del av FS-produktområdet |
| Sentrale studieadministrative prosesser gjennom studieløpet | Hele opptaksområdet som selvstendig produktfamilie utover det FS faktisk dekker |
| Felles modernisering av studieadministrative tjenester | Alle nasjonale registre i utdanningssektoren som ikke forvaltes som del av FS |

## Veikart over kommende funksjonalitet
**Fakta fra Sikt-kildene (kontrollert 2026-03-27):**
- `fs.sikt.no` beskriver et modernisert produktområde med nye brukerflater, API-er og nasjonale registre.
- API-katalogen viser at eldre FS-API-er fases ut i trinn, med flere avviklingsdatoer fram mot 31. mars 2027.

**Deduksjon:** Videreutviklingen går tydelig i retning av moderniserte API-er, nye arbeidsflater og gradvis overgang fra eldre REST-grensesnitt til nyere plattformmønstre.

## Forretningsverdi/Verdiforslag
### For utdanningsinstitusjoner
- Gir en felles plattform i stedet for mange lokale studieadministrative løsninger.
- Reduserer fragmentering og styrker samordning på tvers av institusjoner.

### For sektoren som helhet
- Gjør student- og studiedata mer gjenbrukbare og sammenhengende.
- Understøtter nasjonale tjenester, rapportering og resultatutveksling.

### For studenter og søkere
- Bidrar til mer sammenhengende og digitale studieadministrative tjenester.
- Gjør at data kan brukes på tvers av flere tjenester gjennom samme grunnlag.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Kompleksitet | Produktet spenner over mange prosesser, brukergrupper og tekniske flater | Tydelig produktavgrensning og gradvis modernisering |
| Datakvalitet | Feil i student- eller studiedata kan påvirke mange tjenester samtidig | Sterk datastyring og gode forvaltningsrutiner |
| Teknisk overgang | Overgang fra eldre API-er og flater kan gi migrasjonsutfordringer | Tydelig livssyklusinformasjon og god dokumentasjon |
| Samstyring i sektor | Mange institusjoner og behov kan gjøre prioriteringer krevende | Felles forvaltning og tydelig sektordialog |
| Avhengighet | Tilknyttede tjenester kan bli tett avhengige av FS-data og endringer i grensesnitt | Stabil integrasjonsforvaltning og varsling |

## Kanaler
- Felles studentsystem: https://sikt.no/nb/tjenester/felles-studentsystem
- FS.sikt.no: https://fs.sikt.no/
- FS-API: https://docs.sikt.no/docs/datadeling/teknisk-plattform/api/fs/
- API-katalog for studieadministrasjon: https://fs.sikt.no/tjenester/api/

## Plattform
FS er en nasjonal studieadministrativ plattform med databaser, integrasjoner, API-er og brukerflater.

**Fakta:** Kildene beskriver både eksisterende databaser og arbeidsflater, samt et modernisert produktområde med nye API-er og nasjonale registre.

**Ikke offentlig dokumentert i brukte kilder:** Full intern teknologistakk, samlet systemkart og full ansvarsdeling mellom alle delkomponenter.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er bygget for felles bruk på tvers av mange utdanningsinstitusjoner.
- Det er særlig relevant når behovet er deling og forvaltning av studieadministrative data og prosesser.
- Det er mindre relevant utenfor kontekster som faktisk trenger data og prosesser fra høyere utdanning, men innen sektoren er gjenbruksverdien svært høy.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at studie- og studentdata kan brukes i flere tjenester og prosesser.
- **P5: Del og gjenbruk løsninger** styrkes ved at sektoren bruker en felles plattform i stedet for mange lokale varianter.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi FS kobler institusjoner, tjenester og integrasjoner sammen gjennom felles data og grensesnitt.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi produktet håndterer kritiske data om studier, resultater og kvalifikasjoner.

## Finansiering
- **Fakta:** Kildene beskriver produktet som en felles sektortjeneste, men gir ikke en samlet offentlig finansieringsmodell i denne arbeidsøkten.
- **Deduksjon:** FS finansieres som en felles sektorressurs gjennom Sikts tjenestemodell og institusjonenes bruk, kombinert med kostnader til lokal innføring og integrasjon.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Sikt | Produktsidene på sikt.no og fs.sikt.no |
| Drifts- og forvaltningsansvar | Sikt | Teknisk dokumentasjon og tjenestekatalog |
| Budsjett- og tjenesteforvaltning | Sikt i samspill med sektoren | Beskrivelsen av FS som fellestjeneste |
| Styringsmodell | Felles sektorløsning for universiteter, høgskoler og fagskoler | Produktsidene og API-dokumentasjonen |

## Lenke til dokumentasjon
- https://sikt.no/nb/tjenester/felles-studentsystem
- https://fs.sikt.no/
- https://docs.sikt.no/docs/datadeling/teknisk-plattform/api/fs/
- https://fs.sikt.no/tjenester/api/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://sikt.no/nb/tjenester/felles-studentsystem (kontrollert 2026-03-27)
- Nettkilde: https://fs.sikt.no/ (kontrollert 2026-03-27)
- Nettkilde: https://docs.sikt.no/docs/datadeling/teknisk-plattform/api/fs/ (kontrollert 2026-03-27)
- Nettkilde: https://fs.sikt.no/tjenester/api/ (kontrollert 2026-03-27)


