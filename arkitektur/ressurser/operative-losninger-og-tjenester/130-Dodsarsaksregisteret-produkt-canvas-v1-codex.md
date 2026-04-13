# Dødsårsaksregisteret

## Navn
Dødsårsaksregisteret

## Ressurs ID
FHI-003

## Status/Livsfase
Produksjon

## Modenhet
Høy modenhet i bruk. Dødsårsaksregisteret er et nasjonalt helseregister med langvarig rolle i folkehelseovervåking og statistikkproduksjon.

Detaljer om driftsmodell og teknisk plattformarkitektur er ikke fullt offentlig spesifisert i kildene brukt i denne arbeidsøkten, og bør utdypes i en senere revisjon.

## Kort beskrivelse
Dødsårsaksregisteret er det nasjonale registeret for informasjon om dødsfall og dødsårsaker i Norge. Registeret gir et konsistent og sammenlignbart datagrunnlag for overvåking av dødelighet, sykdomsbyrde og utvikling over tid.

Ressursen er sentral for helseanalyse, folkehelsearbeid og styringsinformasjon fordi den samler meldinger fra helsetjeneste og legger til rette for bruk av samme grunnlag på tvers av aktører. Dette reduserer risikoen for ulik tolkning av et viktig datadomene.

I arkitektursammenheng bør Dødsårsaksregisteret forstås som en avgrenset autoritativ datakilde innen mortalitetsdomenet, ikke som en generell helsedataplattform eller analyseportal. Tilgang til data for analyse skjer typisk gjennom etablerte helsdatakanaler som Helsedata.no eller microdata.no.

## Kapabiliteter
- **Datakilder: Grunndata**
  Registeret er nasjonal autoritativ kilde for opplysninger om dødsfall og dødsårsaker, og gir et konsistent grunnlag for videre bruk på tvers av virksomheter.
- **Datautveksling og integrasjon: Dele data med andre**
  Data fra registeret gjøres tilgjengelig for analyse og statistikk gjennom etablerte helsedatakanaler og etter søknad om datatilgang.
- **Informasjonsforvaltning: Datastyring**
  Registeret understøtter nasjonal styring av et kritisk folkehelsedomene ved å tilby standardiserte, dokumenterte og kvalitetssikrede data.

## Produktmål
- sikre nasjonal og konsistent oversikt over dødsårsaker og dødelighetsutvikling
- gi grunnlag for helseanalyse, tiltaksprioritering og kunnskapsstyring
- støtte sammenlignbar statistikk over tid og på tvers av grupper og regioner

## Brukerbehov
- myndigheter trenger pålitelig grunnlag for folkehelseoppfølging og prioritering av tiltak
- analyse- og forskningsmiljø trenger konsistente, historiske data for statistikk og epidemiologi
- helseforvaltning trenger felles referansegrunnlag for rapportering og vurdering av utvikling

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Helsemyndigheter | Nasjonal dødelighetsoversikt | Styring, prioritering og tiltaksvurdering | Kjernebrukere |
| Analyse- og forskningsmiljø | Historiske og konsistente mortalitetsdata | Forskning, epidemiologi og statistikk | Viktig fagbruk |
| Statistikkprodusenter (f.eks. SSB og FHI) | Sammenlignbar rapportering | Offentlig statistikk og helseovervåking | Systemisk bruk |

## Hovedfunksjoner
Dødsårsaksregisteret samler inn og forvalter meldinger om dødsfall og registrerte dødsårsaker fra helsetjenesten i Norge. Registeret gir et enhetlig og konsistent datagrunnlag som muliggjør overvåking av dødelighetsmønstre og utvikling over tid.

Ressursen er grunnlag for epidemiologisk analyse, prioritering av helsetiltak og sammenlignbar statistikkproduksjon. Den operative verdien ligger i at alle relevante aktører kan støtte seg på samme kilde, noe som reduserer risiko for divergerende tolkninger i beslutningssituasjoner.

Registeret samspiller med andre nasjonale helseregistre og tilgangstjenester. Tilgang for analytisk bruk skjer gjennom etablerte søknadsløp, typisk via Helsedata.no eller ved tilgang gjennom microdata.no for statistisk analyse under kontrollerte betingelser.

Rollen er avgrenset til mortalitetsdomenet. Registeret er ikke en generell analyseplattform og forutsetter tilgangskoordinering med andre løsninger for full nytte.

### Typiske brukssituasjoner (generisk)
- analyse av dødelighetsutvikling og trender over tid
- folkehelsevurderinger og prioriteringsarbeid basert på sykdomsbyrde
- statistikkproduksjon og forskning på nasjonalnivå

### Når Dødsårsaksregisteret normalt ikke er førstevalg
- når behovet er innbyggerrettet selvbetjening eller oppslag i kliniske systemer
- når behovet er generell oversikt over tilgjengelige helsedata og søknadsløp (da er Helsedata.no riktigere inngangspunkt)
- når oppgaven gjelder klinisk pasientoppfølging i sanntid

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonalt registergrunnlag for dødsfall og dødsårsaker | Kliniske journalsystemer |
| Grunnlag for statistikk, analyse og folkehelseoppfølging | Generell analyseplattform eller selvbetjeningsportal |
| Autoritativ datakilde innen mortalitetsdomenet | Overordnet styringsarena for helsepolitikk |

## Veikart over kommende funksjonalitet
Ikke offentlig detaljert verifisert i denne arbeidsøkten.

## Forretningsverdi/Verdiforslag
- For helsemyndigheter: styrket beslutningsgrunnlag for prioritering av folkehelsetiltak og ressurser.
- For analyse- og forskningsmiljø: mer sammenlignbart og stabilt grunnlag for epidemiologi og statistikk.
- For samfunnet: bedre kunnskapsgrunnlag for helsepolitikk og vurdering av tiltak over tid.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Ulik rapporteringspraksis eller kodefeil kan påvirke sammenlignbarhet | Standardisert registrering, kodeopplæring og kvalitetssikringsrutiner |
| Tidsforsinkelse | Forsinket innregistrering kan redusere aktualitet | Tydelige frister og oppfølgingsrutiner for innsendere |
| Tolkningsrisiko | Ulike tolkninger av årsaksklassifikasjon kan gi støy i analyser | Klare definisjoner, dokumentasjon og metodenotater |
| Tilgang og personvern | Sensitive opplysninger krever kontrollert tilgangsstyring | Søknadsbasert tilgang, datatilsynsoverholdelse og sporbarhet |

## Kanaler
- https://www.fhi.no/hn/helseregistre-og-registre/dodsarsaksregisteret/
- https://helsedata.no/
- https://www.helsedirektoratet.no/helseregistre-og-helsedata

## Plattform
Nasjonalt helseregister. Detaljer om underliggende plattformarkitektur er ikke fullt offentlig spesifisert i kildene brukt her.

## Gjenbruk
Høy gjenbruksverdi som nasjonal autoritativ kilde innen mortalitetsdomenet.

### Vanlige kombinasjoner med andre produkter
- `Helsedata.no` (tilgangsflate og søknadskanal for analysedata)
- `microdata.no` (kontrollert statistisk analyse under sikre betingelser)
- øvrige nasjonale helseregistre i komparativ epidemiologi

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Registeret legger til rette for at samme mortalitetsgrunnlag kan brukes på tvers av aktører og formål.
- **P6: Lag digitale løsninger som støtter samhandling**
  Felles datakilde styrker samordnet situasjonsforståelse i folkehelsearbeid.
- **P7: Sørg for tillit til oppgaveløsningen**
  Datakvalitet, enhetlig klassifikasjon og kontrollert tilgang er forutsetninger for tillit til registerets funn.

Mulig prinsippspenning:
- Varierende rapporteringspraksis og kodekvalitet kan svekke sammenlignbarheten selv om infrastrukturen er nasjonal. Dette er en reell risiko som bør håndteres aktivt i forvaltningsmodellen.

## Finansiering
Ikke offentlig detaljert verifisert i denne arbeidsøkten.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar (faglig) | Folkehelseinstituttet | FHI-kilde om Dødsårsaksregisteret |
| Driftsansvar | Ikke offentlig detaljert verifisert | Ikke eksplisitt i åpne kilder brukt her |
| Budsjettansvar | Ikke offentlig detaljert verifisert | Ikke eksplisitt i åpne kilder brukt her |
| Styringsmodell | Registerforvaltning i nasjonalt helsedataregime (overordnet vurdering) | FHI- og helsedata-kilder |

## Lenke til dokumentasjon
- https://www.fhi.no/hn/helseregistre-og-registre/dodsarsaksregisteret/
- https://helsedata.no/
- https://www.helsedirektoratet.no/helseregistre-og-helsedata
- https://www.fhi.no/om/organisasjon/helsedata/

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-04-13
- https://www.fhi.no/hn/helseregistre-og-registre/dodsarsaksregisteret/, kontrollert 2026-04-13
- https://helsedata.no/, kontrollert 2026-04-13
- https://www.helsedirektoratet.no/helseregistre-og-helsedata, kontrollert 2026-04-13

## Merknad om kvalitetsforbedringer
- Analyseforbedringer: tydeligere kildeforankring mot register-spesifikk FHI-kilde og samspill med Helsedata.no/microdata.no.
- Tekstlige forbedringer: fjernet v0-forbehold, styrket rolleavgrensning, mer presis kapabilitetsforklaring og utvidet forvaltningsseksjon.
