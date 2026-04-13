# MSIS

## Navn
MSIS

## Ressurs ID
FHI-002

## Status/Livsfase
Produksjon

## Modenhet
Høy modenhet i bruk. MSIS er en etablert nasjonal løsning for meldingspliktig informasjon om smittsomme sykdommer.

Kildene i denne arbeidsøkten gir godt grunnlag for overordnet funksjon og rolle, men ikke full detaljering av teknisk driftsarkitektur og styringslinjer. Dette bør kompletteres i senere revisjon.

## Kort beskrivelse
MSIS er nasjonalt meldings- og registergrunnlag for smittsomme sykdommer og brukes til overvåking, oppfølging og beredskapsstøtte. Ressursen gir et strukturert og sammenlignbart datagrunnlag for vurdering av smittesituasjon.

Løsningen bidrar til samhandling mellom helsetjeneste, fagmiljø og myndigheter ved at meldingspliktig informasjon samles og forvaltes i en felles nasjonal struktur. Dette reduserer risiko for fragmentert situasjonsforståelse.

I arkitektursammenheng bør MSIS avgrenses som register- og varslingsgrunnlag for smittsomme sykdommer, ikke som generell helsedataportal eller klinisk journalsystem.

## Kapabiliteter
- **Datakilder: Grunndata**
  MSIS forvalter sentrale nasjonale data om meldingspliktige smittsomme sykdommer.
- **Datautveksling og integrasjon: Dele data med andre**
  Registergrunnlaget muliggjør deling og koordinert bruk av sykdomsdata i relevante analyser og oppfølgingsløp.
- **Samarbeid: Organisatorisk samhandling**
  MSIS understøtter koordinering mellom helsemyndigheter, smittevernmiljø og tjenesteaktører i beredskapsarbeid.

## Produktmål
- gi oppdatert nasjonal oversikt over meldingspliktige smittsomme sykdommer
- støtte tidlig oppdagelse, oppfølging og håndtering av smitteutvikling
- sikre felles og konsistent datagrunnlag for smittevern og beredskap

## Brukerbehov
- helsemyndigheter trenger pålitelig situasjonsgrunnlag for styring og tiltak
- smittevernmiljø trenger konsistente data for analyse og risikovurdering
- helsetjenesten trenger tydelig meldingsgrunnlag i relevante oppfølgingsprosesser

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Helsemyndigheter | Nasjonal oversikt over smitteutvikling | Styring, beredskap og prioritering | Kjernebrukere |
| Smittevern- og analysemiljø | Kvalitetssikrede sykdomsdata | Analyse, overvåking og vurdering | Kritisk fagbruk |
| Helsetjenesten | Klart meldings- og oppfølgingsgrunnlag | Operativ oppfølging av meldingsplikt | Tjenestenær bruk |

## Hovedfunksjoner
MSIS samler inn meldinger om smittsomme sykdommer i en nasjonal struktur som gjør data sammenlignbare over tid og på tvers av aktører. Dette er grunnlaget for løpende overvåking av smittebildet.

Ressursen brukes til å følge utvikling og identifisere endringer som kan kreve tiltak. Ved å samle meldingspliktig informasjon i én nasjonal løsning styrkes muligheten for tidlig varsling og koordinert håndtering.

MSIS fungerer også som felles referansepunkt i samhandling mellom forvaltningsnivåer og fagmiljø. Et felles datagrunnlag reduserer risikoen for ulik tolkning av situasjonsbildet i kritiske perioder.

Løsningen er avgrenset til smittevernets meldings- og registerbehov. Den erstatter ikke bredere datatilgangsporter eller journalsystemenes kliniske kjernefunksjoner.

### Typiske brukssituasjoner (generisk)
- overvåking av meldingspliktige smittsomme sykdommer
- analysegrunnlag for vurdering av smittevernstiltak
- beredskapsoppfølging ved endring i sykdomsbilde

### Når MSIS normalt ikke er førstevalg
- når behovet er generell katalog og veiledning for helsedatatilgang
- når formålet er innbyggerrettet selvbetjening i nasjonal portal
- når behovet gjelder klinisk journalføring utover meldingspliktig informasjon

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonalt meldings- og registergrunnlag for smittsomme sykdommer | Kliniske journalsystemfunksjoner |
| Datagrunnlag for smitteovervåking og beredskapsvurdering | Generell dataplattform for alle helsedomener |
| Samhandlingsgrunnlag mellom relevante helseaktører | Overordnet politisk beslutningsarena |

## Veikart over kommende funksjonalitet
Ikke offentlig detaljert verifisert i denne arbeidsøkten.

## Forretningsverdi/Verdiforslag
- For helsemyndigheter: styrket beslutningsgrunnlag i smittevern og beredskap.
- For fagmiljø og analyse: mer konsistent og sammenlignbart grunnlag for overvåking og risikovurdering.
- For samfunnet: bedre forutsetninger for tidlig og koordinert håndtering av smitteutfordringer.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Varierende rapporteringspraksis kan svekke sammenlignbarhet | Standardisering, kvalitetssikring og tydelig veiledning |
| Tidskritikalitet | Forsinket rapportering kan redusere nytte i beredskap | Klare krav til aktualitet og oppfølging |
| Samhandling | Ulike tolkninger av data kan gi sprik i tiltaksvurderinger | Felles definisjoner, metodegrunnlag og samordning |
| Tillit og personvern | Feil håndtering av sensitive opplysninger kan svekke tillit | Strenge kontrollmekanismer for tilgang og bruk |

## Kanaler
- https://www.fhi.no/sv/smittsomme-sykdommer/msis/
- https://www.helsedirektoratet.no/helseregistre-og-helsedata
- https://helsedata.no/

## Plattform
Nasjonalt meldings- og registersystem for smittsomme sykdommer. Teknisk driftsarkitektur er ikke fullt offentlig spesifisert i kildene brukt her.

## Gjenbruk
Høy gjenbruksverdi i smittevern og beredskapskontekst som felles nasjonalt registergrunnlag.

### Vanlige kombinasjoner med andre produkter
- `Helsedata.no`
- relevante beredskaps- og analysemiljø i helsesektoren
- øvrige komplementære helseregistre ved behov for bredere analysegrunnlag

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  MSIS muliggjør felles bruk av smittedata i relevante forvaltnings- og analysekontekster.
- **P6: Lag digitale løsninger som støtter samhandling**
  Registeret bidrar til koordinert situasjonsforståelse og samarbeid på tvers av aktører.
- **P7: Sørg for tillit til oppgaveløsningen**
  Krav til datakvalitet, sporbarhet og kontrollert tilgang er sentralt for løsningens nytte.

Mulig prinsippspenning:
- Ved varierende datakvalitet eller ulik rapporteringspraksis kan tillit og sammenlignbarhet svekkes, selv om den overordnede samhandlingsmodellen er sterk.

## Finansiering
Ikke offentlig detaljert verifisert i denne arbeidsøkten.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar (faglig) | Folkehelseinstituttet | FHI-kilde om MSIS/helsedata |
| Driftsansvar | Ikke offentlig detaljert verifisert | Ikke eksplisitt i åpne kilder brukt her |
| Budsjettansvar | Ikke offentlig detaljert verifisert | Ikke eksplisitt i åpne kilder brukt her |
| Styringsmodell | Nasjonal register- og meldingsforvaltning i smittevernkontekst (overordnet vurdering) | FHI- og helsedata-kilder |

## Lenke til dokumentasjon
- https://www.fhi.no/sv/smittsomme-sykdommer/msis/
- https://www.helsedirektoratet.no/helseregistre-og-helsedata
- https://helsedata.no/
- https://www.fhi.no/om/organisasjon/helsedata/

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-04-13
- https://www.fhi.no/sv/smittsomme-sykdommer/msis/, kontrollert 2026-04-13
- https://www.helsedirektoratet.no/helseregistre-og-helsedata, kontrollert 2026-04-13
- https://helsedata.no/, kontrollert 2026-04-13
- https://www.fhi.no/om/organisasjon/helsedata/, kontrollert 2026-04-13

## Merknad om kvalitetsforbedringer
- Analyseforbedringer: tydeligere kildeforankring mot MSIS-spesifikk FHI-kilde og helseforvaltningskontekst.
- Tekstlige forbedringer: sterkere avgrensning av produktrolle, mer presis beslutningsstøtte og utvidet forvaltningsseksjon.
