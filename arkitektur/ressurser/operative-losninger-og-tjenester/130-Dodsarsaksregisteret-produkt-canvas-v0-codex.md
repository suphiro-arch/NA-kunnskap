# Dødsårsaksregisteret

## Navn
Dødsårsaksregisteret

## Ressurs ID
FHI-003

## Status/Livsfase
Produksjon

## Modenhet
Foreløpig vurdert som høy modenhet. Registeret er etablert nasjonalt og har varig rolle i helseforvaltning, statistikk og analyse, men detaljnivå for teknisk grensesnitt og forvaltningsmodell må styrkes i neste revisjon.

## Kort beskrivelse
Dødsårsaksregisteret er et nasjonalt helseregister som samler informasjon om dødsfall og dødsårsaker i Norge. Ressursen er viktig for helseanalyse, folkehelsearbeid og styringsinformasjon fordi den gir et konsistent datagrunnlag for overvåking av dødelighet, sykdomsbyrde og utvikling over tid.

Dette er en v0-beskrivelse med begrenset kildegrunnlag. I v1 bør det avklares tydeligere hvordan registeret samspiller med Helsedata.no, analysemiljø og øvrige helseregistre.

## Kapabiliteter
- **Datakilder: Grunndata**
  Registeret forvalter sentrale nasjonale data om dødsårsaker.
- **Datautveksling og integrasjon: Dele data med andre**
  Data fra registeret brukes i analyse og statistikk på tvers av helseaktører.
- **Informasjonsforvaltning: Datastyring**
  Registeret understøtter nasjonal datastyring av et viktig folkehelseområde.

## Produktmål
- sikre nasjonal oversikt over dødsårsaker og dødelighetsutvikling
- gi grunnlag for helseanalyse, prioritering og kunnskapsstyring
- støtte sammenlignbar statistikk over tid

## Brukerbehov
- myndigheter trenger pålitelig grunnlag for folkehelseoppfølging
- analysemiljø trenger konsistente data for statistikk og forskning
- helseforvaltning trenger felles referansegrunnlag ved vurdering av tiltak

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Helsemyndigheter | Nasjonal dødelighetsoversikt | Styring og prioritering | Kjernebrukere |
| Analyse- og forskningsmiljø | Tilgang til historiske og konsistente data | Forskning og analyse | Viktig brukergruppe |
| Forvaltning og statistikktjenester | Sammenlignbar rapportering | Oppfølging og offentlig statistikk | Sekundærbrukere |

## Hovedfunksjoner
Dødsårsaksregisteret samler og forvalter nasjonale opplysninger om dødsfall og dødsårsaker. Registeret gir et enhetlig datagrunnlag som gjør det mulig å følge utvikling i dødelighet over tid.

Ressursen brukes som grunnlag for analyse, statistikk og prioriteringsarbeid i helseforvaltningen. Den operative verdien ligger i at samme kilde brukes på tvers av aktører, noe som reduserer risiko for ulike tolkninger av datagrunnlaget.

Registeret inngår i et større helsedataøkosystem der data brukes videre gjennom etablerte tilgangsløp. Rollen er primært å være autoritativ datakilde, ikke å være selvstendig analyseplattform.

### Typiske brukssituasjoner (generisk)
- analyse av dødelighetsutvikling over tid
- folkehelsevurderinger og prioriteringsarbeid
- statistikkproduksjon og forskningsgrunnlag

### Når Dødsårsaksregisteret normalt ikke er førstevalg
- når behovet er innbyggerrettet selvbetjening
- når behovet er generell oversikt over mange datakilder (da er Helsedata.no mer relevant)
- når oppgaven gjelder klinisk pasientoppfølging i sanntid

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonalt registergrunnlag for dødsårsaker | Kliniske journalsystemer |
| Grunnlag for statistikk, analyse og folkehelseoppfølging | Generell analyseplattform |
| Autoritativ datakilde innen avgrenset domene | Overordnet styringsarena |

## Veikart over kommende funksjonalitet
Ikke offentlig verifisert i denne arbeidsøkten.

## Forretningsverdi/Verdiforslag
- For myndigheter: bedre beslutningsgrunnlag for folkehelsetiltak.
- For analysemiljø: mer sammenlignbart og stabilt datagrunnlag.
- For samfunnet: styrket kunnskapsgrunnlag for helsepolitikk og ressursprioritering.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Ulik rapporteringspraksis kan påvirke kvalitet | Standardisert registrering og kvalitetssikring |
| Tidsforsinkelse | Forsinket oppdatering kan svekke aktualitet | Tydelige rutiner for oppdatering |
| Tolkning | Ulike tolkninger av årsakskoder kan gi støy i analyser | Klare definisjoner og dokumentasjon |

## Kanaler
- https://www.helsedirektoratet.no/helseregistre-og-helsedata
- https://www.fhi.no/om/organisasjon/helsedata/

## Plattform
Nasjonalt helseregister (detaljert plattforminformasjon ikke verifisert i denne arbeidsøkten).

## Gjenbruk
Middels til høy gjenbruksverdi som nasjonal datakilde for dødelighetsanalyse.

### Vanlige kombinasjoner med andre produkter
- `Helsedata.no`
- `microdata.no`
- øvrige relevante helseregistre i analysearbeid

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
- https://www.helsedirektoratet.no/helseregistre-og-helsedata
- https://www.fhi.no/om/organisasjon/helsedata/

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-04-11
- https://www.helsedirektoratet.no/helseregistre-og-helsedata, kontrollert 2026-04-11
- https://www.fhi.no/om/organisasjon/helsedata/, kontrollert 2026-04-11
