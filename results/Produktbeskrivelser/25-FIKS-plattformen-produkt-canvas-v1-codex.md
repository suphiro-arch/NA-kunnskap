# Produkt-canvas: FIKS-plattformen

## Navn
FIKS-plattformen

## Ressurs ID
KS-001

## Status/Livsfase
**Produksjon** - etablert felles plattform for kommunal sektor med aktive fellestjenester, integrasjoner og selvbetjent forvaltning.

**Fakta:** KS Digital beskriver FIKS-plattformen som en sentral felles tjenesteplattform for norske kommuner og fylkeskommuner. Plattformen er i ordinær bruk, og drift leveres som tjeneste fra Intility.

## Modenhet
**Høy funksjonell modenhet** - plattformen er i drift, har dokumentert tilgangsstyring, tekniske grensesnitt og et etablert sett med tjenester og komponenter.
- Plattformen brukes som grunnlag for flere kommunale fellestjenester og har både administrativt grensesnitt, API-lag og innbyggerrettede flater.
- Den tekniske beskrivelsen viser moden håndtering av autentisering, autorisering, integrasjoner, testmiljø og sikker kommunikasjon.
- Modenheten er høy for plattformgrunnlaget, men vil variere i de enkelte tjenestene som bygges på toppen.

## Kort beskrivelse
FIKS-plattformen er KS Digitals felles plattform for digital samhandling i kommunal sektor. Plattformen gir kommuner, fylkeskommuner og leverandører et felles teknisk rammeverk for å utvikle, integrere, forvalte og bruke digitale tjenester på en mer standardisert måte. Produktet er særlig relevant når kommunal sektor trenger felles byggeklosser, API-er og styring av tilgang på tvers av mange virksomheter, uten at hver kommune må etablere hele plattformgrunnlaget selv.

## Kapabiliteter
- **Tjenesteutvikling: Utviklings- og kjøretidsmiljø** gir kommunal sektor en felles plattform for utvikling, drift, test og forvaltning av digitale tjenester i stedet for mange lokale plattformløp.
- **Tjenesteutvikling: Integrerbare tjenester** tilbyr API-lag, komponenter og integrasjonsmønstre som gjør det mulig å koble kommunale fagsystemer og fellestjenester sammen gjennom standardiserte grensesnitt.
- **Samarbeid: Organisatorisk samhandling** legger til rette for samhandling mellom kommuner, fylkeskommuner, leverandører og statlige aktører gjennom et felles plattformgrunnlag og felles styringsmønstre.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals kilder brukt i denne arbeidsøkten.

## Produktmål
Dokumenterte mål:
- Gi kommunal sektor en sentral felles tjenesteplattform med felleskomponenter og digitale tjenester.
- Gjøre det mulig for leverandører å forholde seg til et standardisert rammeverk for kommunal sektor.
- Understøtte nasjonalt økosystem for digital samhandling og gjenbruk av nasjonale felleskomponenter der de finnes.

Operative mål utledet fra kildene:
- Redusere lokal kompleksitet i kommunal digitalisering.
- Gi bedre skalering og gjenbruk mellom kommuner og fylkeskommuner.
- Gi et mer forutsigbart grunnlag for integrasjoner og tilgangsstyring.

## Brukerbehov
- Kommuner trenger et felles plattformgrunnlag som reduserer behovet for å bygge opp samme tekniske evner hver for seg.
- Leverandører trenger stabile og dokumenterte grensesnitt som kan brukes på tvers av mange kommuner.
- Forvaltningsmiljøer trenger selvbetjent administrasjon av brukere, integrasjoner og tilganger.
- Sektoren trenger et felles sted å koble sammen tjenester, data og innbyggerflater.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Felles plattform for drift, integrasjon og tjenesteforvaltning | Tar i bruk tjenester og komponenter på plattformen | Primær målgruppe for plattformen |
| Systemleverandører | Standardiserte grensesnitt og integrasjonsmønstre | Utvikler og integrerer tjenester mot plattformen | Viktige for skalering på tvers av sektoren |
| Forvaltere og administratorer | Selvbetjent styring av brukere, roller og integrasjoner | Administrasjon i forvaltning.fiks.ks.no | Har ansvar for oppsett og tilgangsstyring |
| Innbyggere | Tilgang til kommunale tjenester gjennom løsninger som bygges på plattformen | Bruk av innbyggerrettede flater | Bruker effekten av plattformen mer enn plattformen direkte |
| KS Digital | Forvalte felles plattform og legge til rette for gjenbruk | Produktforvaltning, videreutvikling og drift | Eier og utvikler plattformen |

## Hovedfunksjoner
### Primære funksjoner
- FIKS-plattformen gir et felles API-lag for integrasjon mellom kommunale løsninger og fellestjenester. Det gjør plattformen relevant når mange aktører skal koble seg til samme tjenestegrunnlag uten å håndtere ulike lokale integrasjonsmønstre.
- Plattformen tilbyr selvbetjent bruker- og tilgangsstyring på system- og individnivå. Dette er viktig fordi produktet ikke bare er et teknisk kjøretidsmiljø, men også et forvaltningsgrunnlag for hvem som kan bruke hvilke tjenester.
- Plattformen tilbyr komponenter som dokumentlager, Fiks IO, innsynskomponenter og testmiljø. Disse funksjonene gjør det mulig å bygge nye tjenester raskere, og skiller plattformen fra enkeltstående sluttbrukertjenester.
- Plattformen støtter autentisering og autorisering for personer, forvaltere og integrasjoner. Det gjør at både manuelle brukerflater og maskin-til-maskin-integrasjoner kan bruke samme plattformgrunnlag.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Felles plattformkomponenter, API-er og integrasjonsmønstre | Kommunenes lokale fagsystemer |
| Bruker- og tilgangsstyring i plattformen | Lokal saksbehandling og domeneprosess |
| Teknisk grunnlag for dokumentlagring, meldinger og innsyn | Hele tjenestekjeden alene uten fagsystemer og lokale prosesser |
| Testmiljø og felles administrasjon | Full erstatning for alle sektorspesifikke løsninger |

## Veikart over kommende funksjonalitet
**Fakta:** KS beskriver FIKS-plattformen som en etablert plattform som fortsatt utvikles. Den tekniske beskrivelsen legger vekt på at nye tjenester kan bygges på samme grunnlag, og plattformen inngår også som eksisterende hovedkomponent i arbeidet med Felles tjenesteplattform i kommunal sektor.

**Deduksjon:** Videreutviklingen vil trolig være tett knyttet til nye fellestjenester, sterkere integrasjoner og videre standardisering av felles plattformkomponenter.

## Forretningsverdi/Verdiforslag
### For kommuner og fylkeskommuner
- Reduserer behovet for å bygge og drifte like plattformfunksjoner lokalt.
- Gjør det enklere å ta i bruk nye fellestjenester og integrasjoner.

### For leverandører
- Gir ett teknisk rammeverk å forholde seg til for kommunal sektor.
- Reduserer variasjon i integrasjonsmønstre mellom kommuner.

### For sektoren samlet
- Støtter mer samordnet tjenesteutvikling og gjenbruk.
- Senker kompleksitet og legger til rette for bedre samhandling på tvers av forvaltningsnivåer.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Tilgangsstyring og datatilgang må være riktig avgrenset når plattformen brukes på tvers av mange tjenester og virksomheter. | Tydelig rollemodell, eksplisitte privilegier og tjenestespesifikke vurderinger. |
| Teknisk | Feil eller endringer i plattformkomponenter kan påvirke flere kommunale tjenester samtidig. | Modulær forvaltning, testmiljø og kontrollert endringshåndtering. |
| Sikkerhet | Plattformen er et attraktivt mål fordi den samler mange tjenester, integrasjoner og dataflyter. | Sterk autentisering, kryptering, audit-logging og sentral sikkerhetsforvaltning. |
| Leverandør | Kommuner og leverandører blir avhengige av felles plattformvalg og forvaltningsbeslutninger. | Åpen dokumentasjon, standardiserte grensesnitt og tydelig styring av videreutvikling. |
| Brukeropplevelse | Verdien blir svak hvis plattformen ikke oversettes til konkrete, brukbare tjenester i kommunene. | Koble plattformarbeid til reelle tjenestebehov og brukerrettede løsninger. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-plattformen/
- https://developers.fiks.ks.no/fiks-plattformen.pdf
- https://forvaltning.fiks.ks.no/
- https://status.fiks.ks.no

## Plattform
FIKS-plattformen er en felles plattformtjeneste levert for kommunal sektor.

**Fakta:**
- Plattformen består av flere hoveddeler, blant annet administrasjonsflate, API-lag og digitale tjenester.
- Den tekniske dokumentasjonen beskriver egne komponenter for dokumentlager, asynkron integrasjon, innsyn og testmiljø.
- Driften leveres som tjeneste fra Intility.

**Ikke offentlig dokumentert i brukte kilder:** Full detaljarkitektur for alle underliggende driftssoner og teknologivalg per komponent.

## Gjenbruk
**Høy gjenbruksverdi:**
- Plattformen er laget nettopp for at flere kommuner og leverandører skal bruke samme byggeklosser.
- API-er, integrasjonsmønstre og felles administrasjon gjør det mulig å bygge nye tjenester på eksisterende grunnlag.
- Produktet er mer gjenbrukbart som plattformgrunnlag enn som ferdig brukerflate.

## Støtter arkitekturprinsipper
- **P5 Del og gjenbruk løsninger** - plattformen samler felles tekniske byggeklosser som kan brukes på tvers av kommunal sektor.
- **P6 Lag digitale løsninger som støtter samhandling** - plattformen er laget for å koble tjenester, aktører og data sammen gjennom felles grensesnitt og forvaltningsmønstre.

## Finansiering
**Ikke offentlig detaljert dokumentert i brukte kilder:** Jeg fant ikke en full offentlig finansieringsmodell for FIKS-plattformen i denne arbeidsøkten.

**Deduksjon:** Plattformen forvaltes som en KS Digital-tjeneste og finansieringen er trolig knyttet til KS Digitals tjenestemodell og sektorfelles prioriteringer, men dette må bekreftes i egne styrings- eller prismodellkilder.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | KS Digital presenterer og forvalter plattformen som egen fellestjeneste. |
| Driftsansvar | Intility leverer drift som tjeneste; KS Digital forvalter produktet | Eksplisitt oppgitt på produktsiden for FIKS-plattformen. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Må verifiseres i egne styrings- eller prismodellkilder. |
| Styringsmodell | KS Digital med sektorrettet videreutvikling og brukermedvirkning | PDF-en beskriver tett samarbeid med sektoren og brukermedvirkning i utviklingen. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-plattformen/
- https://developers.fiks.ks.no/fiks-plattformen.pdf
- https://forvaltning.fiks.ks.no/
- https://status.fiks.ks.no

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-plattformen/ (hentet 2026-03-18)
- Nettkilde: https://developers.fiks.ks.no/fiks-plattformen.pdf (hentet 2026-03-18)
