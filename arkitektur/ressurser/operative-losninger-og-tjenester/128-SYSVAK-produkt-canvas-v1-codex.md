# SYSVAK

## Navn
SYSVAK

## Ressurs ID
FHI-001

## Status/Livsfase
Produksjon

## Modenhet
Høy modenhet i bruk. SYSVAK er et etablert nasjonalt vaksinasjonsregister med langvarig operativ rolle i helsesektoren.

Samtidig er enkelte detaljer om driftsmodell, styringslinjer og teknisk plattform fortsatt ikke fullt offentlig spesifisert i kildene brukt i denne arbeidsøkten. Disse punktene bør utdypes i en senere revisjon.

## Kort beskrivelse
SYSVAK er nasjonalt register for vaksinasjonsopplysninger og brukes som autoritativ kilde for registrering, oppfølging og dokumentasjon av vaksinasjon. Registeret understøtter både innbyggerrettede og profesjonsrettede tjenester ved at samme grunnlag kan brukes på tvers av aktører.

Ressursen bidrar til at vaksinasjonsinformasjon kan deles og brukes konsistent mellom helsepersonell, innbyggerflater og myndighetsoppfølging. Dette reduserer behovet for lokale parallelle oversikter og gir bedre samordning i vaksinasjonsarbeidet.

I arkitektursammenheng bør SYSVAK forstås som et domeneavgrenset registergrunnlag for vaksinasjonsdata, ikke som en generell helsedataplattform eller bred portal for tilgang til alle helsedata.

## Kapabiliteter
- **Datakilder: Grunndata**
  SYSVAK fungerer som nasjonal grunndatakilde for vaksinasjonsopplysninger og gir et felles, autoritativt datagrunnlag.
- **Datautveksling og integrasjon: Dele data med andre**
  Registeret muliggjør deling og bruk av vaksinasjonsdata i relevante tjenester og arbeidsprosesser på tvers av virksomheter.
- **Sluttbrukertjenester: Sammenhengende tjenester**
  SYSVAK-data inngår i sammenhengende tjenesteforløp der innbygger og helsepersonell møter samme oppdaterte vaksinasjonsgrunnlag.

## Produktmål
- sikre nasjonal og konsistent oversikt over vaksinasjonsstatus
- støtte oppfølging av vaksinasjonsprogram og smittevernarbeid
- gi beslutningsgrunnlag for planlegging, beredskap og målrettede tiltak

## Brukerbehov
- helsepersonell trenger oppdatert vaksinasjonsstatus i klinisk arbeid og oppfølging
- innbyggere trenger innsyn i egne vaksinasjonsopplysninger i nasjonale tjenester
- myndigheter trenger robust datagrunnlag for styring, analyse og beredskap

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Helsepersonell | Oppdatert vaksinasjonsstatus | Behandling, kontroll og oppfølging | Kjernebrukere |
| Innbyggere | Innsyn i egne vaksiner | Egenoppfølging og dokumentasjon | Typisk via Helsenorge |
| Helsemyndigheter og folkehelsemiljø | Nasjonal oversikt og analyse | Programoppfølging, beredskap og planlegging | Viktig styringsbruk |

## Hovedfunksjoner
SYSVAK samler inn og forvalter vaksinasjonsopplysninger som registreres i helsetjenesten. Registeret gir en felles referanse for vaksinestatus og historikk, slik at relevante aktører kan basere seg på samme datagrunnlag.

Ressursen støtter operative arbeidsprosesser der vaksinasjonsstatus må verifiseres, dokumenteres eller følges opp. Dette gjelder både i planlagte vaksinasjonsløp og i situasjoner der rask tilgang til oppdatert informasjon er viktig.

SYSVAK har også en sentral rolle i samordning mellom forvaltningsbehov og tjenestebehov. Registeret gir data som kan brukes i oppfølging av vaksinasjonsprogram og i vurdering av utvikling over tid.

Rollen er avgrenset til vaksinasjonsdomene og registerforvaltning. SYSVAK er ikke en generell dataanalyseplattform, men en autoritativ kilde som andre løsninger bygger videre på.

### Typiske brukssituasjoner (generisk)
- oppslag i vaksinasjonsstatus i kliniske arbeidsprosesser
- innbyggerinnsyn i vaksiner i nasjonale helsetjenester
- oppfølging av vaksinasjonsprogram og smittevernberedskap

### Når SYSVAK normalt ikke er førstevalg
- når behovet er bred katalog over mange helsedatakilder og tilgangsløp
- når formålet er generell analyseplattform for flere registre samtidig
- når behovet gjelder klinisk journalføring utover vaksinasjonsinformasjon

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonalt registergrunnlag for vaksinasjonsopplysninger | Generell journalsystemfunksjonalitet |
| Felles datakilde for vaksinasjonsstatus og historikk | Full analyseplattform for alle helsedata |
| Datagrunnlag for programoppfølging og beredskapsstøtte | Overordnet politisk beslutningsarena |

## Veikart over kommende funksjonalitet
Ikke offentlig detaljert verifisert i denne arbeidsøkten.

## Forretningsverdi/Verdiforslag
- For helsepersonell: raskere tilgang til pålitelig vaksinasjonsstatus og mindre behov for manuell avklaring.
- For innbyggere: bedre innsyn i egen vaksinasjonshistorikk og enklere dokumentasjon ved behov.
- For myndigheter og folkehelsearbeid: mer konsistent grunnlag for planlegging, oppfølging og beredskap.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Mangelfull eller forsinket registrering kan gi feil vurderingsgrunnlag | Standardiserte registreringsrutiner og kvalitetssikring |
| Samhandling | Ulik bruk og tolkning av vaksinasjonsdata i ulike løsninger | Tydelige begreper, datadefinisjoner og forvaltningsveiledning |
| Tillit og personvern | Feil eller utilstrekkelig tilgangskontroll kan svekke tillit | Streng tilgangsstyring, sporbarhet og etterlevelse |
| Operasjonell robusthet | Avhengighet av registertilgjengelighet i kritiske prosesser | Etablerte driftsrutiner og beredskapsmekanismer |

## Kanaler
- https://www.fhi.no/hn/helseregistre-og-registre/sysvak/
- https://www.helsenorge.no/helseopplysninger-som-deles
- https://helsedata.no/

## Plattform
Nasjonalt helseregister. Detaljer om underliggende plattformarkitektur er ikke fullt offentlig spesifisert i kildene brukt her.

## Gjenbruk
Høy gjenbruksverdi i helsesektoren som autoritativt grunnregister for vaksinasjonsopplysninger.

### Vanlige kombinasjoner med andre produkter
- `Helsenorge`
- `Helsedata.no`
- relevante journalsystemer og fagsystemer i helsetjenesten

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  SYSVAK legger til rette for at samme vaksinasjonsgrunnlag kan brukes av flere aktører.
- **P6: Lag digitale løsninger som støtter samhandling**
  Registeret bidrar til felles informasjonsgrunnlag på tvers av tjenesteflater og virksomheter.
- **P7: Sørg for tillit til oppgaveløsningen**
  Korrekt og oppdatert registrering, sammen med kontrollert tilgang, er avgjørende for tillit.

Mulig prinsippspenning:
- Dersom registreringskvalitet eller tilgangsforvaltning varierer mellom aktører, kan prinsippene om tillit og samhandling svekkes i praksis.

## Finansiering
Ikke offentlig detaljert verifisert i denne arbeidsøkten.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar (faglig) | Folkehelseinstituttet | FHI-kilde om SYSVAK/helsedata |
| Driftsansvar | Ikke offentlig detaljert verifisert | Ikke eksplisitt i åpne kilder brukt her |
| Budsjettansvar | Ikke offentlig detaljert verifisert | Ikke eksplisitt i åpne kilder brukt her |
| Styringsmodell | Registerforvaltning i nasjonalt helsedataregime (overordnet vurdering) | FHI- og helsedata-kilder |

## Lenke til dokumentasjon
- https://www.fhi.no/hn/helseregistre-og-registre/sysvak/
- https://www.helsenorge.no/helseopplysninger-som-deles
- https://helsedata.no/
- https://www.helsedirektoratet.no/helseregistre-og-helsedata

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-04-13
- https://www.fhi.no/hn/helseregistre-og-registre/sysvak/, kontrollert 2026-04-13
- https://www.helsenorge.no/helseopplysninger-som-deles, kontrollert 2026-04-13
- https://helsedata.no/, kontrollert 2026-04-13
- https://www.helsedirektoratet.no/helseregistre-og-helsedata, kontrollert 2026-04-13

## Merknad om kvalitetsforbedringer
- Analyseforbedringer: tydeligere kildeforankring mot SYSVAK-spesifikk FHI-kilde og helsedata-kontekst.
- Tekstlige forbedringer: tydeligere rolleavgrensning, mer beslutningsstøtte og styrket seksjon for forvaltning/eier.
