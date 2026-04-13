# Reseptregisteret (NorPD)

## Navn
Reseptregisteret (NorPD)

## Ressurs ID
FHI-004

## Status/Livsfase
Produksjon

## Modenhet
Høy modenhet i bruk. Reseptregisteret (NorPD) er et etablert nasjonalt helseregister med langvarig rolle i legemiddelovervåking, farmakoepidemologi og forvaltningsoppfølging.

Detaljer om driftsmodell og teknisk plattformarkitektur er ikke fullt offentlig spesifisert i kildene brukt i denne arbeidsøkten, og bør utdypes i en senere revisjon.

## Kort beskrivelse
Reseptregisteret (NorPD – Norwegian Prescription Database) er det nasjonale registeret for reseptutskrivning og legemiddelutlevering i Norge. Registeret gir et konsistent og historisk datagrunnlag for å følge legemiddelbruk, bruksmønster og utvikling over tid.

Ressursen er sentral for farmakoepidemologi, legemiddelovervåking og kunnskapsbasert forvaltning fordi den muliggjør analyse av legemiddelbruk på tvers av grupper, regioner og tidsperioder. Et felles og standardisert grunnlag reduserer risikoen for divergerende konklusjoner i tiltaksvurderinger.

I arkitektursammenheng bør Reseptregisteret forstås som en avgrenset autoritativ datakilde innen legemiddeldomenet, ikke som en klinisk beslutningsstøtteplattform eller generell helsedataportal. Datatilgang for analyse skjer gjennom etablerte søknadskanaler som Helsedata.no.

## Kapabiliteter
- **Datakilder: Grunndata**
  Registeret er nasjonal autoritativ kilde for data om reseptutskriving og legemiddelutlevering, og gir et konsistent grunnlag for tverrsektoriell bruk.
- **Datautveksling og integrasjon: Dele data med andre**
  Data fra registeret gjøres tilgjengelig for forskning og analyse gjennom etablerte tilgangskanaler, etter søknad og godkjenning.
- **Informasjonsforvaltning: Datastyring**
  Registeret understøtter nasjonal styring av legemiddeldomenet ved å tilby standardiserte, dokumenterte og kvalitetssikrede data.

## Produktmål
- gi nasjonal og konsistent oversikt over legemiddelutlevering og reseptmønster
- støtte analyse og kunnskapsgrunnlag for helse- og legemiddelforvaltning
- bidra til bedre grunnlag for vurdering av legemiddelbruk, bivirkninger og tiltakseffekter

## Brukerbehov
- analyse- og forskningsmiljø trenger konsistente og historiske reseptdata for farmakoepidemologisk arbeid
- helsemyndigheter trenger stabilt nasjonalt grunnlag for oppfølging og kunnskapsstyring
- forvaltning trenger data for overvåking av legemiddelbruk og vurdering av inngrep

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Helsemyndigheter | Nasjonal oversikt over legemiddelbruk | Styring, overvåking og tiltaksvurdering | Viktig brukergruppe |
| Analyse- og forskningsmiljø | Konsistente resept- og legemiddeldata | Farmakoepidemologi og helseanalyse | Kjernebrukere |
| Legemiddelforvaltning | Grunnlag for overvåking og regulatorisk oppfølging | Kunnskapsstøtte og rapportering | Sekundærbrukere |

## Hovedfunksjoner
Reseptregisteret samler inn og forvalter data om alle resepter utskrevet og utlevert i Norge, med informasjon om legemiddel, pasientgruppe, forskriver og utleveringssted. Registeret gir et strukturert og historisk dokumentert grunnlag for farmakoepidemologisk analyse.

Ressursen understøtter analyse av legemiddelbruksmønstre, trender over tid og variasjon mellom grupper. Dette er et viktig grunnlag for legemiddelovervåking, vurdering av foreskrivningspraksis og effektvurdering av tiltak.

Registeret inngår i et bredere nasjonal helsedataøkosystem. Data gjøres tilgjengelig for godkjente forskningsmiljø og forvaltningsaktører gjennom søknadsbaserte tilgangskanaler. Helsedata.no er den primære inngangsporten for tilgang til datagrunnlaget for analyse.

Reseptregisteret er avgrenset til resept- og utleveringsdomenet. Det er ikke en klinisk beslutningsstøtteplattform og erstatter ikke reseptformidlingssystemer som e-resept eller kliniske journalsystemer.

### Typiske brukssituasjoner (generisk)
- analyse av legemiddelbruk og utvikling over tid og på tvers av grupper
- farmakoepidemologisk forskning med behov for nasjonale reseptdata
- kunnskapsgrunnlag for legemiddelrelaterte tiltak og forvaltningsbeslutninger

### Når Reseptregisteret (NorPD) normalt ikke er førstevalg
- når behovet er innbyggerrettet oppslag i egne resepter (da er Helsenorge riktig kanal)
- når behovet er generell oversikt over tilgjengelige helsedata og søknadskanaler (da er Helsedata.no mer relevant)
- når oppgaven gjelder operativ reseptformidling eller klinisk beslutningsstøtte i sanntid (da er e-resept mer relevant)

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonalt registergrunnlag for reseptutskriving og legemiddelutlevering | Kliniske journalsystemer og operativ reseptformidling |
| Data for farmakoepidemologi, overvåking og analyse | Generell analyseplattform for alle helsedata |
| Autoritativ kilde innen legemiddeldomenet | Overordnet styringsarena for helsepolitikk |

## Veikart over kommende funksjonalitet
Ikke offentlig detaljert verifisert i denne arbeidsøkten.

## Forretningsverdi/Verdiforslag
- For helsemyndigheter: styrket grunnlag for overvåking av legemiddelbruk og vurdering av tiltak.
- For analyse- og forskningsmiljø: mer konsistent og historisk grunnlag for farmakoepidemologisk forskning og helseanalyse.
- For samfunnet: bedre forutsetninger for kunnskapsbaserte beslutninger i legemiddelforvaltningen.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Ulik registreringspraksis kan påvirke sammenlignbarhet | Standardisering, kodeverk og kvalitetssikringsrutiner |
| Tolkningsrisiko | Feiltolkning av legemiddeldata kan gi svake eller misvisende konklusjoner | Tydelig dokumentasjon, metodestøtte og metadata |
| Personvern | Reseptdata er sensitive opplysninger som krever streng tilgangsstyring | Søknadsbasert tilgang, regulatorisk etterlevelse og sporbarhet |
| Tilgangsforsinkelse | Søknadsbehandling kan forsinke tilgang for forskningsmiljø | Tydelige saksbehandlingsrutiner og veiledning fra Helsedata.no |

## Kanaler
- https://www.fhi.no/hn/helseregistre-og-registre/reseptregisteret/
- https://helsedata.no/
- https://www.helsedirektoratet.no/helseregistre-og-helsedata

## Plattform
Nasjonalt helseregister. Detaljer om underliggende plattformarkitektur er ikke fullt offentlig spesifisert i kildene brukt her.

## Gjenbruk
Høy gjenbruksverdi i legemiddel- og helseanalyse som nasjonal autoritativ kilde for reseptdata.

### Vanlige kombinasjoner med andre produkter
- `Helsedata.no` (tilgangsflate og søknadskanal for analysedata)
- `microdata.no` (kontrollert statistisk analyse under sikre betingelser)
- øvrige nasjonale helseregistre i komparativ farmakoepidemologi og helseanalyse

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Registeret legger til rette for at samme legemiddelgrunnlag kan brukes av flere aktører til ulike formål.
- **P6: Lag digitale løsninger som støtter samhandling**
  Et felles nasjonalt register reduserer fragmentering og styrker samordnet kunnskapsgrunnlag.
- **P7: Sørg for tillit til oppgaveløsningen**
  Kontrollert tilgang, sterk personvernhåndtering og sporbarhet er forutsetninger for tillit.

Mulig prinsippspenning:
- Søknadsbasert tilgang med behandlingstid kan bremse bruk og gjøre registeret mindre tilgjengelig for raske analyseformål. Balansen mellom åpenhet og personvern er en reell spenning som forvaltningen må håndtere aktivt.

## Finansiering
Ikke offentlig detaljert verifisert i denne arbeidsøkten.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar (faglig) | Folkehelseinstituttet | FHI-kilde om Reseptregisteret/NorPD |
| Driftsansvar | Ikke offentlig detaljert verifisert | Ikke eksplisitt i åpne kilder brukt her |
| Budsjettansvar | Ikke offentlig detaljert verifisert | Ikke eksplisitt i åpne kilder brukt her |
| Styringsmodell | Registerforvaltning i nasjonalt helsedataregime (overordnet vurdering) | FHI- og helsedata-kilder |

## Lenke til dokumentasjon
- https://www.fhi.no/hn/helseregistre-og-registre/reseptregisteret/
- https://helsedata.no/
- https://www.helsedirektoratet.no/helseregistre-og-helsedata
- https://www.fhi.no/om/organisasjon/helsedata/

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-04-13
- https://www.fhi.no/hn/helseregistre-og-registre/reseptregisteret/, kontrollert 2026-04-13
- https://helsedata.no/, kontrollert 2026-04-13
- https://www.helsedirektoratet.no/helseregistre-og-helsedata, kontrollert 2026-04-13

## Merknad om kvalitetsforbedringer
- Analyseforbedringer: tydeligere kildeforankring mot register-spesifikk FHI-kilde, avgrensning mot e-resept og Helsenorge, og tydeliggjøring av tilgangsmodell.
- Tekstlige forbedringer: fjernet v0-forbehold, styrket rolleavgrensning, mer presis kapabilitetsforklaring og utvidet forvaltningsseksjon.
