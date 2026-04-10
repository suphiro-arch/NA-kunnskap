# Ansattporten

## Ressurs ID
DIGDIR-051

## Status/Livsfase
Produksjon. Ressursen framstår som en etablert tillitstjeneste med dokumenterte produksjons- og testmiljøer.

## Modenhet
Ansattporten framstår som en moden operativ felleskomponent for pålogging for ansatte. Åpne kilder viser dokumentert bruk, standardisert metadataflyt og etablert miljøstruktur.

## Kort beskrivelse
Ansattporten er en operativ autentiseringstjeneste for ansatte i offentlig sektor. Ressursen er viktig fordi den gir et felles tillitsmønster for pålogging i ansattkontekst, og dermed kan redusere behovet for at hver virksomhet etablerer egne løsninger for samme formål.

Dokumentasjonen viser at Ansattporten ligger tett på ID-portens protokollstøtte, men med egne endepunkt og støtte for ansattkontekst. Det gjør ressursen til en spesialisert fellestjeneste, ikke bare en variant av ordinær innbyggerpålogging.

## Kapabiliteter
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling**  
  Ressursen beskytter innloggingsflyt og metadatautveksling i ansattpålogging.

- **Tillit: Autentisering**  
  Ansattporten verifiserer identitet i ansattkontekst og er kjernefunksjonen i ressursen.

- **Tjenesteutvikling: Integrerbare tjenester**  
  Tjenesten tilbyr standardiserte metadata og integrasjonspunkter som andre løsninger kan koble seg til.

## Produktmål
Målet er å gi offentlig sektor en felles og forutsigbar løsning for pålogging for ansatte, med bedre sikkerhet og mindre dobbeltarbeid.

## Brukerbehov
Ressursen dekker behovet for en standardisert og sikker innloggingsløsning for ansatte i offentlige virksomheter.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter | Felles ansattpålogging | Tilgang til interne eller sektorielle tjenester | Kjernebrukere |
| Utviklingsmiljøer | Integrerbar autentisering | Integrasjon mot egne løsninger | Viktig for raskere innføring |
| Ansatte | Sikker og forutsigbar innlogging | Bruk av tjenester i ansattrolle | Sluttbrukere av autentiseringsflyten |

## Hovedfunksjoner
Ansattporten tilbyr pålogging i ansattkontekst gjennom standardiserte metadata og tilhørende sikkerhetsoppsett. Ressursen fungerer som en felles inngang til autentisering for løsninger som krever ansattrolle.

Den operative verdien ligger i at tjenesten kan brukes som et felles mønster på tvers av flere løsninger, i stedet for at hver virksomhet må etablere og forvalte egne varianter.

Åpne tekniske kilder viser også at ressursen har egne endepunkt og støtte for ulike autentiseringsnivåer og identitetskilder. Det gjør den relevant som byggestein i løsninger som trenger mer enn bare enkel innlogging, men fortsatt først og fremst i rollen som autentiseringstjeneste.

### Typiske brukssituasjoner (generisk)
- når en løsning trenger sikker pålogging for ansatte
- når flere offentlige tjenester skal bruke samme autentiseringsmønster
- når en virksomhet vil bygge på en nasjonal tillitstjeneste i stedet for lokal spesialløsning

### Når Ansattporten normalt ikke er førstevalg
- når behovet gjelder innlogging for innbyggere eller virksomheter i andre kontekster
- når løsningen primært trenger autorisasjon eller representasjon, ikke bare autentisering

## Scope og avgrensning
Inngår:
- autentisering i ansattkontekst
- standardiserte metadata for integrasjon
- test- og produksjonsmiljøer

Inngår ikke:
- full autorisasjonsmodell
- generell innbyggerpålogging
- komplette fag- eller saksløsninger

## Veikart over kommende funksjonalitet
Foreløpig ikke fylt ut i detalj i denne v1-beskrivelsen. Åpne kilder brukt her dokumenterer dagens protokoll og miljøstruktur, men ikke et nærmere offentlig veikart.

## Forretningsverdi/Verdiforslag
Ressursen gir verdi ved å gjøre ansattpålogging enklere å ta i bruk, mer standardisert og mer sikker på tvers av offentlige løsninger.

## Utfordringer og risiko
| Kategori | Konkret risiko | Håndtering |
|---|---|---|
| Avgrensning | Kan forveksles med andre tillitstjenester som dekker andre kontekster | Tydeliggjøre rolle og målgruppe |
| Innføring | Virksomheter kan ha ulik modenhet for integrasjon | Bruke dokumentasjon og standard metadata aktivt |
| Samspill | Behov for autorisasjon og rolleforvaltning kan ligge utenfor ressursen | Kombinere med andre relevante tillitstjenester |

## Kanaler
Ressursen tilbys gjennom teknisk dokumentasjon, metadataendepunkter og tilhørende integrasjonsmønstre.

## Plattform
Skybasert fellestjeneste med dokumenterte test- og produksjonsmiljøer.

## Gjenbruk
Ressursen har høy gjenbruksverdi fordi den er laget for å kunne integreres i mange løsninger som trenger ansattpålogging.

### Vanlige kombinasjoner med andre produkter
- andre tillitstjenester i Digdir-porteføljen
- interne virksomhetsløsninger som trenger ansattpålogging

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger**  
  Ressursen gjør autentisering gjenbrukbar på tvers av løsninger.

- **P7: Sørg for tillit til oppgaveløsningen**  
  Ansattporten bidrar til sikker og forutsigbar identitetsbekreftelse i ansattkontekst.

## Finansiering
Foreløpig ikke fylt ut i detalj i denne v1-beskrivelsen.

## Forvaltning/eier
| Område | Beskrivelse |
|---|---|
| Produktansvar | Digitaliseringsdirektoratet |
| Driftsansvar | Digitaliseringsdirektoratet |
| Budsjettansvar | Foreløpig ikke fylt ut i detalj i denne v1-beskrivelsen |
| Styringsmodell | Foreløpig ikke fylt ut i detalj i denne v1-beskrivelsen |

## Lenke til dokumentasjon
- https://docs.digdir.no/docs/ansattporten/ansattporten_wellknown.html
- https://docs.digdir.no/docs/ansattporten/ansattporten_protocol.html

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-04-10
- `sources/2026-04-10-digdir-virkemiddeloversikt-raw.md`, kontrollert 2026-04-10
- https://docs.digdir.no/docs/ansattporten/ansattporten_wellknown.html , kontrollert 2026-04-10
- https://docs.digdir.no/docs/ansattporten/ansattporten_protocol.html , kontrollert 2026-04-10
