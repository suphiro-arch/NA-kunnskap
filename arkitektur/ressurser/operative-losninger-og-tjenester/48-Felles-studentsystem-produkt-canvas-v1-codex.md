# Produkt-canvas: Felles studentsystem (FS)

## Navn
Felles studentsystem (FS)

## Ressurs ID
SIKT-002

## Status/Livsfase
**Produksjon** - etablert nasjonal studieadministrativ plattform for universiteter, hÃ¸gskoler og fagskoler.

**Fakta:** Sikt beskriver FS som et studentinformasjonssystem som brukes til studieadministrasjon ved de fleste universiteter og hÃ¸gskoler i Norge. Produktet bestÃ¥r av databaser, integrasjoner og brukerapplikasjoner, og omtales ogsÃ¥ som en nasjonal digital grunnmur for hÃ¸yere utdanning.

## Modenhet
**HÃ¸y modenhet** - langvarig og innarbeidet sektorlÃ¸sning:
- FS har vÃ¦rt et informasjonsnav i norsk hÃ¸yere utdanning siden 1996.
- Produktet brukes i sentrale studieadministrative prosesser gjennom hele studielÃ¸pet.
- FS har bÃ¥de etablerte brukerflater og et voksende API- og integrasjonslandskap.
- Sikt publiserer nÃ¥ ogsÃ¥ et modernisert produktomrÃ¥de pÃ¥ `fs.sikt.no` med tjenestekatalog, API-katalog og utviklerinformasjon.

**Deduksjon:** Modenheten er hÃ¸y fordi FS bÃ¥de er en operativ kjerneplattform i sektoren og en videreutviklet digital plattform med tydelige grensesnitt for integrasjon og modernisering.

## Kort beskrivelse
Felles studentsystem (FS) er den nasjonale plattformen for studieadministrative data og prosesser i hÃ¸yere utdanning. Produktet forvalter og tilgjengeliggjÃ¸r informasjon om studenter, studier, opptak, resultater og kvalifikasjoner, og fungerer som informasjonsnav for bÃ¥de interne arbeidsprosesser, studentnÃ¦re tjenester og maskinell datadeling. FS er derfor mer enn ett administrativt system: det er den felles sektorlÃ¸sningen som gjÃ¸r det mulig Ã¥ bygge sammenheng mellom studieadministrasjon, opptak, resultatutveksling og videre bruk av studentdata.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** er relevant fordi FS inngÃ¥r i flere samhandlingslÃ¸p og mottar opplysninger i studieadministrative prosesser.
- **Datautveksling og integrasjon: Dele data med andre** er en kjernefunksjon ved at FS tilbyr API-er, meldingskÃ¸er og andre integrasjonsflater for videre bruk av data.
- **Informasjonsforvaltning: Datastyring** er sentralt fordi FS forvalter, strukturerer og vedlikeholder store mengder studie- og studentdata som grunnlag for mange prosesser.
- **Samarbeid: Organisatorisk samhandling** er relevant fordi FS er en felles sektorlÃ¸sning som brukes av mange institusjoner med Sikt som felles forvalter.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Sikts tjenestesider, FS-dokumentasjonen og API-katalogen.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Sikts sider for `Felles studentsystem`, `fs.sikt.no` og teknisk dokumentasjon for FS-API.

Dokumenterte mÃ¥l:
- StÃ¸tte studieadministrasjon ved universiteter og hÃ¸gskoler.
- Forvalte, foredle og formidle prosesser og data om studier og studenter.
- Legge til rette for digitalisering og effektivisering i offentlig sektor gjennom lÃ¸sninger for studenter, ansatte og utviklere.

Operative mÃ¥l utledet fra de samme kildene:
- Gi sektoren et felles og sammenhengende datagrunnlag for studieadministrative prosesser.
- GjÃ¸re student- og studiedata tilgjengelige i standardiserte og mer moderne grensesnitt.
- UnderstÃ¸tte samspill mellom institusjonenes lokale behov og felles nasjonale prosesser og tjenester.

## Brukerbehov
- Universiteter, hÃ¸gskoler og fagskoler trenger en felles plattform for studieadministrative prosesser.
- Studieadministrative og vitenskapelige ansatte trenger arbeidsflater for registrering, vedlikehold og saksbehandling.
- Studenter og sÃ¸kere trenger digitale tjenester som bygger pÃ¥ oppdaterte studie- og studentdata.
- Utviklere og integrasjonsmiljÃ¸er trenger API-er og dokumenterte tilgangslÃ¸p til data i FS.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Utdanningsinstitusjoner | Felles studieadministrativ plattform | Studieplanlegging, studentoppfÃ¸lging, opptak og resultatforvaltning | Hovedbrukere av produktet |
| Studieadministrative ansatte | ArbeidsverktÃ¸y og saksstÃ¸tte | Registrering, vedlikehold og behandling av studiesaker | Bruker FS-klient og nye arbeidsflater |
| Studenter og sÃ¸kere | Digitale tjenester basert pÃ¥ egne data | StudentforlÃ¸p, resultater og andre selvbetjeningslÃ¸p | MÃ¸ter produktet via tilknyttede tjenester |
| Utviklere og integratÃ¸rer | API-er og teknisk dokumentasjon | Integrasjon, datadeling og hendelsesnÃ¦re lÃ¸sninger | Viktig for gjenbruksverdi |
| Sikt og sektorfellesskapet | Felles forvaltning og modernisering | Videreutvikling, standardisering og drift | Produktet er felles sektorinfrastruktur |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
**Forvaltning av student- og studiedata.** FS holder orden pÃ¥ sentrale data om studenter, utdanningstilbud, opptak, studieforlÃ¸p, resultater og kvalifikasjoner. Dette gjÃ¸r produktet til sektorens sentrale informasjonsnav for studieadministrasjon.

**StÃ¸tte for studieadministrative prosesser.** Produktet dekker arbeidsprosesser innen studieplanlegging, studiegjennomfÃ¸ring, studentoppfÃ¸lging, opptak og resultatforvaltning. FS er derfor ikke bare en database, men en operativ plattform for lÃ¸pende saks- og prosessarbeid.

**TilgjengeliggjÃ¸ring gjennom API-er og integrasjoner.** Sikt beskriver bÃ¥de et felles REST API, ny API-katalog og moderniserte grensesnitt. Produktet har dermed en tydelig rolle som delings- og integrasjonsplattform, ikke bare som intern sektorapplikasjon.

**Felles sektorplattform med modernisering og overgang til nye tjenester.** `fs.sikt.no` viser at FS utvikles videre med nye brukerflater, nasjonale registre og API-er. Produktet omfatter derfor bÃ¥de etablert kjernefunksjonalitet og et modernisert mÃ¥lbilde for sektoren.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Felles studentinformasjonssystem for hÃ¸yere utdanning | Hele utdanningssektorens Ã¸vrige portefÃ¸lje utenfor studieadministrasjon |
| Databaser, integrasjoner og brukerapplikasjoner i FS | Alle lokale arbeidsprosesser som institusjonene lÃ¸ser utenfor FS |
| API-er og tekniske grensesnitt for viderebruk av data | Rene sluttbrukerportaler som ikke er del av FS-produktomrÃ¥det |
| Sentrale studieadministrative prosesser gjennom studielÃ¸pet | Hele opptaksomrÃ¥det som selvstendig produktfamilie utover det FS faktisk dekker |
| Felles modernisering av studieadministrative tjenester | Alle nasjonale registre i utdanningssektoren som ikke forvaltes som del av FS |

## Veikart over kommende funksjonalitet
**Fakta fra Sikt-kildene (kontrollert 2026-03-27):**
- `fs.sikt.no` beskriver et modernisert produktomrÃ¥de med nye brukerflater, API-er og nasjonale registre.
- API-katalogen viser at eldre FS-API-er fases ut i trinn, med flere avviklingsdatoer fram mot 31. mars 2027.

**Deduksjon:** Videreutviklingen gÃ¥r tydelig i retning av moderniserte API-er, nye arbeidsflater og gradvis overgang fra eldre REST-grensesnitt til nyere plattformmÃ¸nstre.

## Forretningsverdi/Verdiforslag
### For utdanningsinstitusjoner
- Gir en felles plattform i stedet for mange lokale studieadministrative lÃ¸sninger.
- Reduserer fragmentering og styrker samordning pÃ¥ tvers av institusjoner.

### For sektoren som helhet
- GjÃ¸r student- og studiedata mer gjenbrukbare og sammenhengende.
- UnderstÃ¸tter nasjonale tjenester, rapportering og resultatutveksling.

### For studenter og sÃ¸kere
- Bidrar til mer sammenhengende og digitale studieadministrative tjenester.
- GjÃ¸r at data kan brukes pÃ¥ tvers av flere tjenester gjennom samme grunnlag.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Kompleksitet | Produktet spenner over mange prosesser, brukergrupper og tekniske flater | Tydelig produktavgrensning og gradvis modernisering |
| Datakvalitet | Feil i student- eller studiedata kan pÃ¥virke mange tjenester samtidig | Sterk datastyring og gode forvaltningsrutiner |
| Teknisk overgang | Overgang fra eldre API-er og flater kan gi migrasjonsutfordringer | Tydelig livssyklusinformasjon og god dokumentasjon |
| Samstyring i sektor | Mange institusjoner og behov kan gjÃ¸re prioriteringer krevende | Felles forvaltning og tydelig sektordialog |
| Avhengighet | Tilknyttede tjenester kan bli tett avhengige av FS-data og endringer i grensesnitt | Stabil integrasjonsforvaltning og varsling |

## Kanaler
- Felles studentsystem: https://sikt.no/nb/tjenester/felles-studentsystem
- FS.sikt.no: https://fs.sikt.no/
- FS-API: https://docs.sikt.no/docs/datadeling/teknisk-plattform/api/fs/
- API-katalog for studieadministrasjon: https://fs.sikt.no/tjenester/api/

## Plattform
FS er en nasjonal studieadministrativ plattform med databaser, integrasjoner, API-er og brukerflater.

**Fakta:** Kildene beskriver bÃ¥de eksisterende databaser og arbeidsflater, samt et modernisert produktomrÃ¥de med nye API-er og nasjonale registre.

**Ikke offentlig dokumentert i brukte kilder:** Full intern teknologistakk, samlet systemkart og full ansvarsdeling mellom alle delkomponenter.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet er bygget for felles bruk pÃ¥ tvers av mange utdanningsinstitusjoner.
- Det er sÃ¦rlig relevant nÃ¥r behovet er deling og forvaltning av studieadministrative data og prosesser.
- Det er mindre relevant utenfor kontekster som faktisk trenger data og prosesser fra hÃ¸yere utdanning, men innen sektoren er gjenbruksverdien svÃ¦rt hÃ¸y.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at studie- og studentdata kan brukes i flere tjenester og prosesser.
- **P5: Del og gjenbruk lÃ¸sninger** styrkes ved at sektoren bruker en felles plattform i stedet for mange lokale varianter.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** stÃ¸ttes fordi FS kobler institusjoner, tjenester og integrasjoner sammen gjennom felles data og grensesnitt.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** er sentralt fordi produktet hÃ¥ndterer kritiske data om studier, resultater og kvalifikasjoner.

## Finansiering
- **Fakta:** Kildene beskriver produktet som en felles sektortjeneste, men gir ikke en samlet offentlig finansieringsmodell i denne arbeidsÃ¸kten.
- **Deduksjon:** FS finansieres som en felles sektorressurs gjennom Sikts tjenestemodell og institusjonenes bruk, kombinert med kostnader til lokal innfÃ¸ring og integrasjon.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Sikt | Produktsidene pÃ¥ sikt.no og fs.sikt.no |
| Drifts- og forvaltningsansvar | Sikt | Teknisk dokumentasjon og tjenestekatalog |
| Budsjett- og tjenesteforvaltning | Sikt i samspill med sektoren | Beskrivelsen av FS som fellestjeneste |
| Styringsmodell | Felles sektorlÃ¸sning for universiteter, hÃ¸gskoler og fagskoler | Produktsidene og API-dokumentasjonen |

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

