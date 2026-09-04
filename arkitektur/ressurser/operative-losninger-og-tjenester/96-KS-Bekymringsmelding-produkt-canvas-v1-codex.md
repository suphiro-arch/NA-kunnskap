# Produkt-canvas: KS Bekymringsmelding

## Navn
KS Bekymringsmelding

## Ressurs ID
KS-015

## Status/Livsfase
**Produksjon** - etablert nasjonal løsning i drift for innsending av bekymringsmeldinger til barnevernet.

**Fakta:** KS Digital beskriver tjenesten som en digital løsning utviklet av KS og Bufdir for trygg innsending av bekymringsmeldinger fra privatpersoner og offentlige ansatte. Fiks-dokumentasjonen beskriver både portal og maskin-til-maskin-integrasjon.

## Modenhet
**Høy modenhet** - etablert operativ løsning med flere leveransemåter og tydelig teknisk dokumentasjon:
- Støtter både webportal og API-integrasjon.
- Kan levere direkte til fagsystem, som PDF for manuell nedlasting eller via brevpost ved manglende digital mottak.
- Har versjonert API med bakoverkompatibilitet og dokumentert sikkerhetsmodell.

**Deduksjon:** Produktet er modent for operativ bruk i barneverndomenet, men verdi og effekt avhenger av kommunenes integrasjon og forvaltningspraksis.

## Kort beskrivelse
KS Bekymringsmelding er en nasjonal digital meldingstjeneste for innsending av bekymringsmeldinger til kommunale barnevernstjenester. Løsningen gir privatpersoner og offentlige ansatte en sikker kanal for innsending, og gjør det mulig for kommuner å motta meldinger strukturert i fagsystem eller gjennom alternative mottaksløp.

Produktet har tydelig NA-relevans fordi det kobler flere aktører i en kritisk samfunnsprosess: melder, kommunal barnevernstjeneste, fagsystemleverandører og nasjonale forvaltere. Tjenesten reduserer manuell håndtering og styrker både kvalitet og sporbarhet i meldingsflyten.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsutveksling**
  Produktets kjerne er trygg transport og levering av bekymringsmeldinger mellom avsender og riktig mottak i kommunen.
- **Samarbeid: Organisatorisk samhandling**
  Løsningen støtter samhandling mellom innbyggere, offentlige meldere, barnevern og systemleverandører i samme prosess.
- **Sluttbrukertjenester: Sammenhengende tjenester**
  Tjenesten gir én digital inngang for innsending, veiledning og mottak, med fallback til alternative kanaler ved behov.

## Produktmål
Dokumenterte mål:
- Gjøre det enklere og tryggere å sende bekymringsmeldinger til barnevernet.
- Bedre kvaliteten i meldingene gjennom struktur, veiledning og klart språk.
- Sikre rask og effektiv håndtering i kommunale barnevernstjenester.

Operative mål utledet fra kildene:
- Redusere tidstap og feil i manuell håndtering av sensitive meldinger.
- Tilrettelegge for både integrert og ikke-integrert mottak i kommunene.
- Styrke personvern og rettssikkerhet i hele meldingsløpet.

## Brukerbehov
- Innbyggere og offentlige meldere trenger en enkel og sikker måte å melde bekymring på.
- Barnevernstjenester trenger rask tilgang til gode og komplette meldinger.
- Kommuner trenger fleksibel mottaksmodell som fungerer både med og uten full API-integrasjon.
- Fagsystemleverandører trenger tydelige standarder og versjonerte API-er for stabil integrasjon.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Innbyggere (privat melder) | Sikker og enkel innsending | Innsending av bekymringsmelding | Sluttbruker via portal |
| Offentlige ansatte (meldepliktige) | Strukturert innsending med veiledning | Innsending via skjema eller API | Viktig meldergruppe |
| Kommunale barnevernstjenester | Raskt og korrekt mottak | Mottak i fagsystem, manuell nedlasting eller brev | Primær virksomhetsbruker |
| Fagsystemleverandører | Stabil integrasjon mot Fiks | Produksjon og konsum av meldinger | Teknisk brukergruppe |
| KS Digital og Bufdir | Forvaltning og videreutvikling | KS Digital har produktforvaltning; Bufdir er faglig samarbeidspartner | Felles forvaltningsansvar |

## Hovedfunksjoner
KS Bekymringsmelding tilbyr to hovedinnganger for innsending: ett skjema for privatpersoner og ett for offentlige ansatte. Begge løpene er utviklet for å gi mer komplett informasjon og bedre kvalitet i meldingene.

Løsningen transformerer innhold til både strukturert data (JSON) og ustrukturert dokumentformat (PDF), slik at kommunene kan motta meldinger gjennom ulike mottaksløp avhengig av teknisk modenhet.

Produktet støtter direkte maskin-til-maskin-integrasjon med kommunale fagsystem gjennom API, men har samtidig alternative leveringsformer med manuell nedlasting og brevpost dersom digital bekreftelse uteblir.

Sikkerhet er en sentral del av funksjonsdesignet, med kryptering i transport og lagring, samt tydelig versjonering for å ivareta kompatibilitet mellom avsendere og mottakere.

### Typiske brukssituasjoner
- når en privatperson sender bekymringsmelding til barnevernstjenesten i sin kommune
- når en offentlig ansatt med meldeplikt sender melding fra eget fagsystem via API
- når kommunen mottar strukturert melding direkte i fagsystem for rask saksbehandling
- når kommunen uten full integrasjon henter melding manuelt eller mottar brevpost som fallback

### Når KS Bekymringsmelding normalt ikke er førstevalg
- når behovet gjelder generisk meldingstrafikk utenfor barneverndomenet
- når virksomheten trenger intern saksbehandling, ikke selve innsending/mottak av bekymringsmelding
- når prosessen gjelder andre velferdsområder med egne domeneplattformer og regelverk

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Innsending og mottak av bekymringsmeldinger til barnevern | Full barnevernfaglig saksbehandling i fagsystem |
| Portal og API for private/offentlige meldere | Generell meldingsplattform for alle kommunale prosesser |
| Sikker transport, strukturering og fallback-leveranse | Erstatning for kommunens interne arbeidsflater |
| Integrasjon mot kommunale fagsystem der støttet | Faglige vedtak og oppfølging etter mottatt melding |

## Veikart over kommende funksjonalitet
Kildene viser løpende videreutvikling av skjema og innhold (blant annet felter for samtykke), i dialog med brukerråd, Bufdir og leverandører. Ingen samlet offentlig veikartsplan med tidfestede leveranser er hentet i denne arbeidsøkten.

## Forretningsverdi/Verdiforslag
- For innbyggere og meldere: lavere terskel for å melde bekymring og bedre veiledning i en sensitiv prosess.
- For kommunalt barnevern: raskere mottak, bedre datakvalitet og mer effektiv prioritering av saker.
- For offentlig sektor: mer standardisert og trygg nasjonal praksis for en lovpålagt samhandlingsprosess.
- For leverandørøkosystemet: tydelig API-basert modell som reduserer punkt-til-punkt-variasjon.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Integrasjonsvariasjon | Ulik fagsystemstøtte gir ulik grad av automatisering i kommunene | Beholde fallback-løp og styrke integrasjonsstøtte |
| Personvern | Høy sensitivitet i meldingsinnhold | Kryptering, tilgangskontroll og ROS/DPIA-malverk |
| Prosesskvalitet | Ulik forståelse hos meldere kan påvirke kvalitet | Veiledning, klart språk og strukturert skjema |
| Leveringssikkerhet | Melding kan bli forsinket ved manglende digital bekreftelse | Automatisk alternativ kanal (brevpost) ved behov |

## Kanaler
- https://ksdigital.no/tjenestene/ks-bekymringsmelding/
- https://developers.fiks.ks.no/tjenester/bekymringsmelding/
- https://bekymringsmelding.fiks.ks.no/

## Plattform
Fiks-plattformen med webportal og API-grensesnitt mot kommunale fagsystemer.

## Gjenbruk
Produktet har høy gjenbruksverdi i barneverndomenet på tvers av kommuner, fordi samme innsendings- og mottaksmodell kan brukes nasjonalt. Gjenbruk utenfor domenet er begrenset.

**Vanlige kombinasjoner med andre produkter:**
- `Fiks-plattformen`
- `Fiks IO`
- kommunale barnevernsfagsystemer
- relaterte Fiks-meldings- og dokumenttjenester

**Kildekode:** Ikke offentlig dokumentert for selve tjenesten. KS Digital publiserer klientbibliotek og SDK-er for Fiks-plattformen på [github.com/ks-no](https://github.com/ks-no), flere av dem under MIT-lisens.

## Støtter arkitekturprinsipper
- **P6: Lag digitale løsninger som støtter samhandling**
  Produktet binder sammen melder, kommune og fagsystem i et felles, nasjonalt samhandlingsløp.
- **P4: Del og gjenbruk data**
  Strukturert informasjonsutveksling reduserer dobbeltregistrering og forbedrer datakvalitet i mottaket.

Svakhet: Løsningen er domenespesifikk og krever lokal prosess- og systemtilpasning for å gi full gevinst.

## Finansiering
Tjenesten tas i bruk gjennom KS Digital sine avtale- og prismodeller, og forvaltes i samarbeid med relevante nasjonale aktører i barnevernsområdet.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktforvaltning | KS Digital | ksdigital.no og developers.fiks |
| Faglig samarbeid | Bufdir (omtalt samarbeidspartner i tjenestebeskrivelse) | ksdigital.no omtale |
| Lokal tjenestebruk | Kommunal barnevernstjeneste | ta-i-bruk og fagsystemintegrasjon |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/ks-bekymringsmelding/
- https://developers.fiks.ks.no/tjenester/bekymringsmelding/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://ksdigital.no/tjenestene/ks-bekymringsmelding/ (kontrollert 2026-05-03)
- Nettkilde: https://developers.fiks.ks.no/tjenester/bekymringsmelding/ (kontrollert 2026-05-03)
