# Produkt-canvas: Nasjonal vitnemålsdatabase (NVB)

## Navn
Nasjonal vitnemålsdatabase (NVB)

## Ressurs ID
SIKT-004

## Status/Livsfase
**Produksjon** - etablert nasjonal database- og delingstjeneste for elektroniske vitnemål fra videregående opplæring.

**Fakta:** Sikt beskriver NVB som en tjeneste for kvalitetssikring og lagring av elektroniske vitnemål fra fullført og bestått videregående opplæring i Norge. Tjenesten inneholder de fleste elektroniske vitnemål utstedt i år 2000 eller senere.

## Modenhet
**Høy modenhet** - etablert nasjonal løsning med bred bruk:
- NVB brukes i opptak til universiteter, høgskoler og fagskoler.
- Tjenesten brukes også til statistikk, forskning og dokumentasjon av kompetanse.
- Sikt har administrativt, teknisk og forvaltningsansvar for løsningen.
- Tjenestekatalogen på `fs.sikt.no` viser NVB som stabil tjeneste.

**Deduksjon:** Modenheten er høy fordi NVB er en innarbeidet nasjonal datakilde som brukes i flere viktige beslutnings- og dokumentasjonsløp, samtidig som den er i ferd med å utvides og moderniseres.

## Kort beskrivelse
Nasjonal vitnemålsdatabase (NVB) er den nasjonale databasen for elektroniske vitnemål fra videregående opplæring. Produktet lagrer og kvalitetssikrer vitnemål og gjør dem tilgjengelige for opptak, dokumentasjon, statistikk og forskning. NVB er derfor mer enn et arkiv: det er en nasjonal register- og delingsressurs som gjør at samme vitnemålsgrunnlag kan brukes på tvers av skoler, opptaksprosesser og analyseformål.

## Kapabiliteter
- **Datakilder: Grunndata** er relevant fordi NVB forvalter autoritative vitnemålsopplysninger som mange andre prosesser bygger videre på.
- **Datautveksling og integrasjon: Dele data med andre** er en kjernefunksjon ved at opplysningene brukes i opptak, dokumentasjon, statistikk og forskning.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Sikts beskrivelser av NVB som database, kvalitetsmekanisme og delingsressurs.

## Produktmål
**Primærkilder:** Sikts sider for `Nasjonal vitnemålsdatabase` og NVB i tjenestekatalogen.

Dokumenterte mål:
- Kvalitetssikre og lagre elektroniske vitnemål fra videregående opplæring.
- Effektivisere og kvalitetssikre saksbehandling av søknader ved opptak til høyere utdanning og høyere yrkesfaglig utdanning.
- Bidra til dokumentasjon av kompetanse og gi data til statistikk og forskning.

Operative mål utledet fra de samme kildene:
- Gi én nasjonal kilde for elektroniske vitnemål i stedet for manuell håndtering av dokumentasjon.
- Redusere feil og friksjon i opptaksløp ved at vitnemål kan leses og brukes maskinelt.
- Utvide produktet mot et bredere register over oppnådd kompetanse og mer typer utdanningsdokumentasjon.

## Brukerbehov
- Videregående skoler og skoleeiere trenger et nasjonalt system for innsending og kvalitetssikring av vitnemål.
- Saksbehandlere i opptak trenger rask og pålitelig tilgang til vitnemålsdata.
- Vitnemålseiere trenger at dokumentasjonen deres kan brukes effektivt og korrekt i videre utdanningsløp.
- Analyse- og forskningsmiljøer trenger et kvalitetssikret datagrunnlag.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Videregående skoler | Innsending og kvalitetssikring av vitnemål | Produksjon og overføring av vitnemålsdata | Viktig kildeledd inn i produktet |
| Fylkeskommuner og skoleeiere | Oversikt og kvalitet i vitnemålsforvaltning | Oppfølging og forvaltning | Eierperspektiv i videregående opplæring |
| Opptaksmiljøer | Effektiv tilgang til vitnemål | Saksbehandling for høyere utdanning og høyere yrkesfaglig utdanning | Tydelig hovedbruker av delte data |
| Vitnemålseiere | Korrekt dokumentasjon av egen kompetanse | Søknader og dokumentasjon | Indirekte sluttbruker av tjenesten |
| Statistikk- og forskningsmiljøer | Kvalitetssikrede data | Analyse og kunnskapsgrunnlag | Sekundær, men viktig brukergruppe |
| Sikt og samarbeidende forvaltere | Drift, modernisering og forvaltning | Nasjonal forvaltning av løsningen | Sikt er tydelig hovedforvalter |

## Hovedfunksjoner
### Primære funksjoner
**Lagring og kvalitetssikring av elektroniske vitnemål.** NVB samler inn og forvalter vitnemål fra videregående skoler i en felles nasjonal database. Dette er produktets kjerne og gjør løsningen til en autoritativ kilde for vitnemålsdata.

**Datagrunnlag for opptak og dokumentasjon.** Produktet brukes i opptak til universiteter, høgskoler og fagskoler, og bidrar til raskere og mer korrekt saksbehandling. NVB reduserer dermed behovet for manuell dokumenthåndtering og lokal verifisering.

**Viderebruk til statistikk og forskning.** Sikt beskriver NVB som en viktig datakilde for statistikk og forskning. Produktet er derfor ikke bare en operativ opptaksressurs, men også en del av nasjonal kunnskapsinfrastruktur.

**Modernisering mot bredere kompetanseregister.** Sikts nyere beskrivelser viser at NVB er i ferd med å bli erstattet eller utvidet til et mer generelt register over oppnådd kompetanse. Produktet har dermed både en etablert kjernefunksjon og en tydelig overgang til bredere dokumentasjonsformål.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonal database for elektroniske vitnemål fra videregående opplæring | Hele opptakssystemet som sådan |
| Kvalitetssikring og lagring av vitnemålsdata | All dokumentasjon om utdanning utenfor det NVB faktisk dekker |
| Deling av vitnemålsdata til opptak, statistikk og forskning | Sluttbrukerportaler som bare viser eller deler dokumentasjon |
| Modernisering mot bredere kompetansedokumentasjon | Hele sektorens øvrige studieadministrative plattform |
| Forvaltnings- og driftsansvar hos Sikt | Lokal dokumenthåndtering hos hver enkelt skole eller institusjon |

## Veikart over kommende funksjonalitet
**Fakta fra Sikt-kildene (kontrollert 2026-03-27):**
- Sikt beskriver at NVB etter endring i opplæringsloven skal inneholde alle vitnemål og kan inneholde annen type utdanningsdokumentasjon.
- Tjenestekatalogen beskriver at NVB er i ferd med å moderniseres og bli et mer generelt register over oppnådd kompetanse, med planlagt erstatning klar for bruk fra 1. september 2026.

**Deduksjon:** Veikartet peker tydelig mot overgang fra dagens vitnemålsdatabase til en bredere og mer generell nasjonal kompetanseregisterløsning.

## Forretningsverdi/Verdiforslag
### For opptaksmiljøer og utdanningssektoren
- Gir én nasjonal og kvalitetssikret kilde for vitnemålsdata.
- Effektiviserer opptaksprosesser og reduserer manuell dokumenthåndtering.

### For analyse og forskning
- Gir et strukturert og kvalitetssikret datagrunnlag om videregående opplæring.
- Støtter bedre innsikt og beslutningsgrunnlag i sektoren.

### For vitnemålseiere
- Gjør at dokumentasjon av kompetanse kan brukes mer effektivt og korrekt i videre utdanningsløp.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Feil i vitnemålsdata kan slå direkte ut i opptak og dokumentasjon | Kvalitetssikring ved innsending og tydelige forvaltningsløp |
| Avgrensning | Produktet kan oppfattes som bredere enn det faktisk er i dagens form | Tydelig skille mellom NVB, vitnemålsportaler og andre utdanningssystemer |
| Teknisk overgang | Modernisering og overgang til nytt register kan gi usikkerhet i integrasjoner og forvaltning | Gradvis overgang og klar informasjon om erstatning |
| Samfunnsavhengighet | Feil eller utilgjengelighet kan påvirke opptak og dokumentasjon i stor skala | Stabil drift og høy prioritet på kritiske perioder |
| Juridisk og personvern | Deling av vitnemålsdata må være korrekt avgrenset og hjemlet | Streng tilgangsstyring og tydelig formålsstyring |

## Kanaler
- Nasjonal vitnemålsdatabase: https://sikt.no/nb/tjenester/nasjonal-vitnemalsdatabase
- NVB i tjenestekatalogen: https://fs.sikt.no/tjenestekatalog/nvb/
- Tjenestekatalog studieadministrasjon: https://fs.sikt.no/tjenestekatalog/

## Plattform
NVB er en nasjonal register- og delingsløsning for elektroniske vitnemålsdata.

**Fakta:** Kildene beskriver både databasen, brukergruppene, organiseringen og moderniseringsretningen. Produktet framstår som en operativ dataplattform med tydelig forvaltningsansvar hos Sikt.

**Ikke offentlig dokumentert i brukte kilder:** Full teknisk arkitektur, detaljert grensesnittoversikt og samlet driftsmodell utover det som står i tjenestekatalogen.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er laget for at samme vitnemålsopplysninger skal kunne brukes i flere prosesser og av flere aktører.
- Det er særlig relevant når behovet er nasjonalt kvalitetssikrede vitnemålsdata.
- Det er mindre relevant utenfor kontekster som faktisk trenger dokumentasjon eller analyse av videregående opplæring.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at vitnemålsopplysninger kan brukes i flere formål og prosesser.
- **P5: Del og gjenbruk løsninger** styrkes ved at sektoren kan bygge på én felles database i stedet for mange lokale varianter.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi skoler, opptaksmiljøer, Sikt og analysemiljøer bruker samme datagrunnlag.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi vitnemålsdata må være korrekte, sporbare og kvalitetssikrede.

## Finansiering
- **Fakta:** Kildene beskriver organisering og forvaltning, men gir ikke en samlet offentlig finansieringsmodell i denne arbeidsøkten.
- **Deduksjon:** NVB finansieres som en nasjonal sektortjeneste under Sikt, kombinert med kostnader til innføring og bruk hos sektoraktørene.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Sikt | Produktsiden for NVB |
| Administrativt, teknisk og forvaltningsansvar | Sikt | Produktsiden beskriver dette eksplisitt |
| Saksbehandlingsansvar for vitnemål og søknader | HK-dir | Produktsiden beskriver HK-dir sin rolle |
| Styringsmodell | Sikt som hovedforvalter i samspill med HK-dir og skoleeiermiljøer | Produktsiden og tjenestekatalogen |

## Lenke til dokumentasjon
- https://sikt.no/nb/tjenester/nasjonal-vitnemalsdatabase
- https://fs.sikt.no/tjenestekatalog/nvb/
- https://fs.sikt.no/tjenestekatalog/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://sikt.no/nb/tjenester/nasjonal-vitnemalsdatabase (kontrollert 2026-03-27)
- Nettkilde: https://fs.sikt.no/tjenestekatalog/nvb/ (kontrollert 2026-03-27)
- Nettkilde: https://fs.sikt.no/tjenestekatalog/ (kontrollert 2026-03-27)
