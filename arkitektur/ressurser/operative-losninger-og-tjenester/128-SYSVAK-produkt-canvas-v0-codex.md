# SYSVAK

## Navn
SYSVAK

## Ressurs ID
FHI-001

## Status/Livsfase
Produksjon

## Modenhet
Foreløpig vurdert som høy modenhet. Registeret er etablert nasjonalt og brukes i løpende helseforvaltning, men detaljnivå for teknisk plattform og forvaltningsmodell må verifiseres bedre i neste revisjon.

## Kort beskrivelse
SYSVAK er det nasjonale vaksinasjonsregisteret og brukes til registrering, oppfølging og dokumentasjon av vaksinasjon i Norge. Ressursen er sentral i samhandling mellom innbyggerflater, helsepersonell og myndigheter fordi den gir et felles grunnlag for vaksinasjonsstatus og oppfølging.

Dette er en v0-beskrivelse med begrenset kildegrunnlag. Nivået skal løftes til v1 med tydeligere avgrensning, mer presis kapabilitetskobling og verifisert forvaltningsinformasjon.

## Kapabiliteter
- **Datakilder: Grunndata**
  SYSVAK fungerer som autoritativ kilde for vaksinasjonsopplysninger.
- **Datautveksling og integrasjon: Dele data med andre**
  Registeret brukes som felles datagrunnlag i samhandling mellom helsetjenester og innbyggertjenester.
- **Sluttbrukertjenester: Sammenhengende tjenester**
  Opplysninger fra SYSVAK inngår i sammenhengende brukerreiser for innbygger og helsepersonell.

## Produktmål
- sikre nasjonal oversikt over vaksinasjonsstatus
- støtte oppfølging av vaksinasjonsprogram og smittevernarbeid
- gi et felles datagrunnlag for relevante tjenester og myndighetsoppfølging

## Brukerbehov
- helsepersonell trenger oppdaterte vaksinasjonsopplysninger i behandlings- og oppfølgingsarbeid
- innbyggere trenger tilgang til egen vaksinasjonshistorikk i nasjonale tjenester
- myndigheter trenger data for planlegging, beredskap og rapportering

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Helsepersonell | Oppdatert vaksinasjonsstatus | Behandling og oppfølging | Kjernebrukere |
| Innbyggere | Innsyn i egne vaksiner | Egenoppfølging | Typisk via Helsenorge |
| Myndigheter | Nasjonal oversikt og analyse | Styring og beredskap | Viktig i smittevern |

## Hovedfunksjoner
SYSVAK lagrer og forvalter vaksinasjonsopplysninger som brukes i flere deler av helsesektoren. Registeret fungerer som et nasjonalt fellesgrunnlag for hvem som er vaksinert, når vaksinering er utført og hvilke vaksiner som er registrert.

Ressursen har også en samhandlingsrolle ved at opplysninger brukes i ulike tjenester og arbeidsprosesser på tvers av virksomheter. Dette reduserer behovet for lokale kopier og manuelle kontrollrutiner.

I tillegg gir SYSVAK grunnlag for oppfølging og analyse i smittevernarbeid. Dette er særlig relevant i situasjoner der myndigheter trenger raskt og konsistent datagrunnlag.

### Typiske brukssituasjoner (generisk)
- oppslag i vaksinasjonsstatus i kliniske arbeidsprosesser
- innbyggerinnsyn i vaksiner gjennom nasjonale helsetjenester
- rapportering og oppfølging av vaksinasjonsprogrammer

### Når SYSVAK normalt ikke er førstevalg
- når behovet gjelder bred helsedatakatalog eller søknad om datatilgang
- når behovet gjelder klinisk journalføring utover vaksinasjonsdata
- når formålet er generell statistikkplattform uten registerspesifikk avgrensning

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonalt register for vaksinasjonsopplysninger | Generell journalsystemfunksjonalitet |
| Felles datagrunnlag for vaksinasjonsstatus | Full analyseplattform for alle helsedata |
| Samhandlingsgrunnlag for relevante helsetjenester | Overordnet styringsarena for helseprioriteringer |

## Veikart over kommende funksjonalitet
Ikke offentlig verifisert i denne arbeidsøkten.

## Forretningsverdi/Verdiforslag
- For helsepersonell: raskere og tryggere tilgang til vaksinasjonsstatus.
- For innbyggere: enklere innsikt i egen vaksinehistorikk.
- For myndigheter: bedre grunnlag for planlegging og beredskap.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Ufullstendig registrering kan gi feil beslutningsgrunnlag | Tydelige registreringsrutiner og kvalitetssikring |
| Samhandling | Ulik bruk av registerdata i ulike løsninger | Felles begrepsbruk og dokumentasjon |
| Tillit | Feil eller forsinkede data svekker tillit | Sporbar oppdatering og tydelig avvikshåndtering |

## Kanaler
- https://www.helsenorge.no/helseopplysninger-som-deles
- https://www.fhi.no/om/organisasjon/helsedata/

## Plattform
Nasjonalt helseregister (detaljert plattforminformasjon ikke verifisert i denne arbeidsøkten).

## Gjenbruk
Middels til høy gjenbruksverdi i helsesektoren som felles registergrunnlag for vaksinasjonsdata.

### Vanlige kombinasjoner med andre produkter
- `Helsenorge`
- `Helsedata.no`
- kliniske fagsystemer i helsetjenesten

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
- https://www.helsenorge.no/helseopplysninger-som-deles
- https://www.fhi.no/om/organisasjon/helsedata/

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-04-11
- https://www.helsenorge.no/helseopplysninger-som-deles, kontrollert 2026-04-11
- https://www.fhi.no/om/organisasjon/helsedata/, kontrollert 2026-04-11
