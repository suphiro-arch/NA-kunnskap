# MSIS

## Navn
MSIS

## Ressurs ID
FHI-002

## Status/Livsfase
Produksjon

## Modenhet
Foreløpig vurdert som høy modenhet. Registeret brukes i nasjonal smitteovervåking og forvaltes i etablerte helseprosesser, men mer detaljert teknisk og forvaltningsmessig dokumentasjon bør innhentes før v1.

## Kort beskrivelse
MSIS er Meldingssystem for smittsomme sykdommer og fungerer som nasjonalt register- og varslingsgrunnlag for smittsomme sykdommer. Ressursen er sentral for smittevern, beredskap og samhandling fordi den muliggjør systematisk innsamling og oppfølging av meldingspliktig sykdomsinformasjon.

Dette er en v0-beskrivelse med begrenset kildegrunnlag. Neste løft bør tydeliggjøre avgrensning mot andre registre, samt mer konkret beskrive dataflyt, brukerroller og forvaltningsmodell.

## Kapabiliteter
- **Datakilder: Grunndata**
  MSIS forvalter sentrale data om smittsomme sykdommer i nasjonal sammenheng.
- **Datautveksling og integrasjon: Dele data med andre**
  Registeret brukes som felles datagrunnlag i samhandling mellom helseaktører og myndigheter.
- **Samarbeid: Organisatorisk samhandling**
  MSIS understøtter koordinering mellom helseforvaltning, beredskap og relevante tjenestemiljø.

## Produktmål
- gi nasjonal oversikt over meldingspliktige smittsomme sykdommer
- støtte tidlig oppdagelse, oppfølging og håndtering av smittehendelser
- sikre et felles og konsistent datagrunnlag for smittevern og beredskap

## Brukerbehov
- helsemyndigheter trenger oppdatert oversikt over smittesituasjon
- fagmiljøer trenger data for analyse, oppfølging og vurdering av tiltak
- helsetjenesten trenger tydelig meldings- og oppfølgingsgrunnlag

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Helsemyndigheter | Nasjonal smitteoversikt | Beredskap og styring | Kjernebrukere |
| Fagmiljø i smittevern | Oppdatert sykdomsdata | Analyse og oppfølging | Viktig i risikovurdering |
| Helsetjenesten | Meldings- og varslingsgrunnlag | Klinisk/forvaltningsnær oppfølging | Operativ bruk |

## Hovedfunksjoner
MSIS samler inn og forvalter meldinger om smittsomme sykdommer på nasjonalt nivå. Registeret gir et strukturert grunnlag for å forstå utvikling, omfang og mønstre i smittesituasjonen.

Ressursen er også en sentral del av beredskapsarbeidet ved at data kan brukes til løpende overvåking, risikovurdering og prioritering av tiltak. Dette gjør MSIS viktig i samhandlingen mellom ulike deler av helseforvaltningen.

I tillegg fungerer MSIS som referansepunkt for konsistent informasjonsgrunnlag i smittevernsarbeid. Det reduserer risiko for fragmentert situasjonsforståelse når flere aktører skal vurdere samme hendelsesbilde.

### Typiske brukssituasjoner (generisk)
- overvåking av meldingspliktige smittsomme sykdommer
- analysegrunnlag for smittevernstiltak
- beredskapsoppfølging ved endringer i sykdomsbilde

### Når MSIS normalt ikke er førstevalg
- når behovet gjelder generell helsedatakatalog eller søknad om sekundærbruk av helsedata
- når behovet er innbyggerrettet selvbetjening i helseportal
- når formålet er klinisk journalføring utover meldingspliktig sykdomsinformasjon

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonalt meldings- og registergrunnlag for smittsomme sykdommer | Generelle journalsystemfunksjoner |
| Data for smitteovervåking og beredskap | Helhetlig dataplattform for all helseinformasjon |
| Samhandlingsgrunnlag for smittevernarbeid | Overordnet politisk beslutningsarena |

## Veikart over kommende funksjonalitet
Ikke offentlig verifisert i denne arbeidsøkten.

## Forretningsverdi/Verdiforslag
- For myndigheter: bedre beslutningsgrunnlag i smittevern og beredskap.
- For fagmiljø: mer konsistent datagrunnlag for analyse og oppfølging.
- For samfunnet: styrket evne til tidlig oppdagelse og koordinert håndtering av smitteutfordringer.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Ulik rapporteringspraksis kan svekke sammenlignbarhet | Standardiserte rutiner og kvalitetssikring |
| Tidskritikalitet | Forsinket rapportering kan svekke beredskap | Tydelige krav til aktualitet og oppfølging |
| Samhandling | Ulik tolkning av data hos aktører | Felles definisjoner og veiledning |

## Kanaler
- https://www.fhi.no/om/organisasjon/helsedata/
- https://www.helsedirektoratet.no/helseregistre-og-helsedata

## Plattform
Nasjonalt helseregister-/meldingssystem (detaljert plattforminformasjon ikke verifisert i denne arbeidsøkten).

## Gjenbruk
Middels til høy gjenbruksverdi i helseberedskap og smittevern som felles datagrunnlag.

### Vanlige kombinasjoner med andre produkter
- `Helsedata.no`
- relevante beredskaps- og analysemiljø i helsesektoren

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
- **P6: Lag digitale løsninger som støtter samhandling**
- **P7: Sørg for tillit til oppgaveløsningen**

## Finansiering
Ikke offentlig detaljert verifisert i denne arbeidsøkten.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Faglig forvaltning | Folkehelseinstituttet (foreløpig vurdering) | helsedata-kilder |
| Driftsmodell | Ikke offentlig detaljert verifisert | - |

## Lenke til dokumentasjon
- https://www.fhi.no/om/organisasjon/helsedata/
- https://www.helsedirektoratet.no/helseregistre-og-helsedata

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-04-11
- https://www.fhi.no/om/organisasjon/helsedata/, kontrollert 2026-04-11
- https://www.helsedirektoratet.no/helseregistre-og-helsedata, kontrollert 2026-04-11
