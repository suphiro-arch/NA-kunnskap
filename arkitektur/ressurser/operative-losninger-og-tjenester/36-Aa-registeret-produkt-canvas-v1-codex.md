# Produkt-canvas: Aa-registeret

## Navn
Aa-registeret

## Ressurs ID
NAV-001

## Status/Livsfase
**Produksjon** - etablert nasjonalt grunndataregister over arbeidsforhold i Norge.

**Fakta:** Nav beskriver Arbeidsgiver- og arbeidstakerregisteret som et register over arbeidsforhold i Norge som Nav eier og forvalter. Registeret er tilgjengelig for offentlige etater og noen private aktører med hjemmel.

## Modenhet
**Høy modenhet** - innarbeidet og samfunnskritisk register:
- opprettet i 1978 og videreutviklet gjennom flere reformer
- utvidet betydelig med A-ordningen fra 2015
- brukes av de fleste offentlige etater, mange kommuner og fylker samt noen private aktører
- tilbyr både API, weboppslag og spesialtilpassede uttrekk

**Deduksjon:** Modenheten er høy fordi registeret er en sentral nasjonal kilde for arbeidsforholdsdata og inngår i mange rettighets-, kontroll- og analyseprosesser.

## Kort beskrivelse
Aa-registeret er det nasjonale grunndataregisteret over arbeidsforhold i Norge. Produktet forvalter opplysninger om ordinære og maritime arbeidsforhold, frilansoppdrag og andre relevante relasjoner mellom arbeidsgivere og arbeidstakere. Registeret er både en autoritativ datakilde og en delt informasjonsressurs som brukes av Nav, andre offentlige etater og enkelte private aktører med hjemmel.

## Kapabiliteter
- **Datakilder: Grunndata**
- **Datautveksling og integrasjon: Bruke data fra andre**
- **Datautveksling og integrasjon: Dele data med andre**
- **Sluttbrukertjenester: Sammenhengende tjenester**

## Produktmål
- være nasjonal kilde for arbeidsforholdsopplysninger
- støtte offentlige oppgaver og enkelte private lovpålagte behov
- gjøre arbeidsforholdsdata tilgjengelige gjennom standardiserte tjenester

## Brukerbehov
- offentlige etater trenger oppdaterte arbeidsforholdsdata
- arbeidsgivere og arbeidstakere trenger innsyn i egne rapporterte forhold
- private pensjonsaktører og enkelte andre trenger nødvendige opplysninger innenfor rettslige rammer

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Nav og andre offentlige etater | Arbeidsforholdsdata | Ytelser, kontroll, statistikk og tilsyn | Hovedbrukere |
| Arbeidsgivere | Innsyn i rapporterte forhold | Oppfølging og kontroll | Viktig selvbetjeningsbruk |
| Arbeidstakere og frilansere | Innsyn i egne arbeidsforhold | Rettigheter og kontroll | Sluttbrukerperspektiv |
| Private aktører med hjemmel | Nødvendige opplysninger | OTP, AFP og forskning | Begrenset, men viktig brukergruppe |

## Hovedfunksjoner
### Primære funksjoner
**Autoritativt register over arbeidsforhold.** Aa-registeret samler og vedlikeholder sentrale opplysninger om arbeidsforhold i Norge.

**Tilgjengeliggjøring gjennom flere tjenester.** Nav tilbyr integrert oppslag via API, weboppslag og uttrekk. Produktet er derfor både register og delingsflate.

**Innsyn og selvbetjening.** Arbeidsgivere og arbeidstakere kan se egne opplysninger, noe som gir produktet en tydelig sluttbrukerdimensjon i tillegg til maskinell deling.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Nasjonalt register over arbeidsforhold | Hele A-ordningen som bredere rapporteringsordning |
| API, oppslag og uttrekk fra registeret | All lokal HR-forvaltning hos virksomheter |
| Innsyn for arbeidsgivere og arbeidstakere | Alle avledede ytelser og tjenester som bruker dataene |

## Veikart over kommende funksjonalitet
**Fakta fra kildene (kontrollert 2026-03-27):**
- Nav publiserer løpende oppdaterte tilgangs- og brukerstøttesider.
- Tilgangssiden er oppdatert 10. mars 2026.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et samlet, tidsfestet veikart er ikke hentet ut.

## Forretningsverdi/Verdiforslag
- gir én nasjonal kilde for arbeidsforholdsdata
- reduserer behovet for lokale kopier og manuelle forespørsler
- gjør viktige arbeidslivsdata tilgjengelige for mange offentlige oppgaver

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | feil rapportering kan påvirke mange prosesser samtidig | tydelig rapporterings- og korrigeringsløp |
| Juridikk | tilgang må være presist hjemlet | streng tilgangsforvaltning |
| Samfunnsavhengighet | mange tjenester er avhengige av registeret | robust drift og tydelig prioritering |

## Kanaler
- https://www.nav.no/arbeidsgiver/aa-registeret
- https://www.nav.no/samarbeidspartner/tilgang-aa-registeret
- https://www.nav.no/aa-registeret/arbeidsforhold
- https://www.nav.no/samarbeidspartner/brukerstotte-aa-registeret

## Plattform
Aa-registeret er et nasjonalt register- og delingssystem for arbeidsforholdsdata.

## Gjenbruk
**Høy gjenbruksverdi** som nasjonal grunndatakilde for arbeidsforhold.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
- **P5: Del og gjenbruk løsninger**
- **P7: Sørg for tillit til oppgaveløsningen**

## Finansiering
Ikke samlet verifisert i denne arbeidsøkten.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Nav | produktsidene |

## Lenke til dokumentasjon
- https://www.nav.no/arbeidsgiver/aa-registeret
- https://www.nav.no/samarbeidspartner/tilgang-aa-registeret
- https://www.nav.no/aa-registeret/arbeidsforhold
- https://www.nav.no/samarbeidspartner/brukerstotte-aa-registeret

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.nav.no/arbeidsgiver/aa-registeret (kontrollert 2026-03-27)
- Nettkilde: https://www.nav.no/samarbeidspartner/tilgang-aa-registeret (kontrollert 2026-03-27)
- Nettkilde: https://www.nav.no/aa-registeret/arbeidsforhold (kontrollert 2026-03-27)
- Nettkilde: https://www.nav.no/samarbeidspartner/brukerstotte-aa-registeret (kontrollert 2026-03-27)


