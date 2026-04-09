# Produkt-canvas: FIKS-plattformen

## Navn
FIKS-plattformen

## Ressurs ID
KS-001

## Status/Livsfase
**Produksjon** - etablert felles plattform for kommunal sektor med aktive fellestjenester, integrasjoner og selvbetjent forvaltning.

**Fakta:** KS Digital beskriver FIKS-plattformen som en sentral felles tjenesteplattform for norske kommuner og fylkeskommuner. Plattformen er i ordinÃ¦r bruk, og drift leveres som tjeneste fra Intility.

## Modenhet
**HÃ¸y funksjonell modenhet** - plattformen er i drift, har dokumentert tilgangsstyring, tekniske grensesnitt og et etablert sett med tjenester og komponenter.
- Plattformen brukes som grunnlag for flere kommunale fellestjenester og har bÃ¥de administrativt grensesnitt, API-lag og innbyggerrettede flater.
- Den tekniske beskrivelsen viser moden hÃ¥ndtering av autentisering, autorisering, integrasjoner, testmiljÃ¸ og sikker kommunikasjon.
- Modenheten er hÃ¸y for plattformgrunnlaget, men vil variere i de enkelte tjenestene som bygges pÃ¥ toppen.

## Kort beskrivelse
FIKS-plattformen er KS Digitals felles plattform for digital samhandling i kommunal sektor. Plattformen gir kommuner, fylkeskommuner og leverandÃ¸rer et felles teknisk rammeverk for Ã¥ utvikle, integrere, forvalte og bruke digitale tjenester pÃ¥ en mer standardisert mÃ¥te. Produktet er sÃ¦rlig relevant nÃ¥r kommunal sektor trenger felles byggeklosser, API-er og styring av tilgang pÃ¥ tvers av mange virksomheter, uten at hver kommune mÃ¥ etablere hele plattformgrunnlaget selv.

## Kapabiliteter
- **Samarbeid: Organisatorisk samhandling** gir kommunal sektor et felles plattformgrunnlag for samhandling pÃ¥ tvers av kommuner, fylkeskommuner, leverandÃ¸rer og statlige aktÃ¸rer.
- **Tjenesteutvikling: Integrerbare tjenester** tilbyr felles API-er og integrasjonskomponenter som gjÃ¸r det lettere Ã¥ koble systemer og tjenester sammen.
- **Tjenesteutvikling: Utviklings- og kjÃ¸retidsmiljÃ¸** gir et felles miljÃ¸ for utvikling, test, drift og forvaltning av kommunale digitale tjenester.

## ProduktmÃ¥l
Dokumenterte mÃ¥l:
- Gi kommunal sektor en sentral felles tjenesteplattform med felleskomponenter og digitale tjenester.
- GjÃ¸re det mulig for leverandÃ¸rer Ã¥ forholde seg til et standardisert rammeverk for kommunal sektor.
- UnderstÃ¸tte nasjonalt Ã¸kosystem for digital samhandling og gjenbruk av nasjonale felleskomponenter der de finnes.

Operative mÃ¥l utledet fra kildene:
- Redusere lokal kompleksitet i kommunal digitalisering.
- Gi bedre skalering og gjenbruk mellom kommuner og fylkeskommuner.
- Gi et mer forutsigbart grunnlag for integrasjoner og tilgangsstyring.

## Brukerbehov
- Kommuner trenger et felles plattformgrunnlag som reduserer behovet for Ã¥ bygge opp samme tekniske evner hver for seg.
- LeverandÃ¸rer trenger stabile og dokumenterte grensesnitt som kan brukes pÃ¥ tvers av mange kommuner.
- ForvaltningsmiljÃ¸er trenger selvbetjent administrasjon av brukere, integrasjoner og tilganger.
- Sektoren trenger et felles sted Ã¥ koble sammen tjenester, data og innbyggerflater.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Felles plattform for drift, integrasjon og tjenesteforvaltning | Tar i bruk tjenester og komponenter pÃ¥ plattformen | PrimÃ¦r mÃ¥lgruppe for plattformen |
| SystemleverandÃ¸rer | Standardiserte grensesnitt og integrasjonsmÃ¸nstre | Utvikler og integrerer tjenester mot plattformen | Viktige for skalering pÃ¥ tvers av sektoren |
| Forvaltere og administratorer | Selvbetjent styring av brukere, roller og integrasjoner | Administrasjon i forvaltning.fiks.ks.no | Har ansvar for oppsett og tilgangsstyring |
| Innbyggere | Tilgang til kommunale tjenester gjennom lÃ¸sninger som bygges pÃ¥ plattformen | Bruk av innbyggerrettede flater | Bruker effekten av plattformen mer enn plattformen direkte |
| KS Digital | Forvalte felles plattform og legge til rette for gjenbruk | Produktforvaltning, videreutvikling og drift | Eier og utvikler plattformen |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- FIKS-plattformen gir et felles API-lag for integrasjon mellom kommunale lÃ¸sninger og fellestjenester. Det gjÃ¸r plattformen relevant nÃ¥r mange aktÃ¸rer skal koble seg til samme tjenestegrunnlag uten Ã¥ hÃ¥ndtere ulike lokale integrasjonsmÃ¸nstre.
- Plattformen tilbyr selvbetjent bruker- og tilgangsstyring pÃ¥ system- og individnivÃ¥. Dette er viktig fordi produktet ikke bare er et teknisk kjÃ¸retidsmiljÃ¸, men ogsÃ¥ et forvaltningsgrunnlag for hvem som kan bruke hvilke tjenester.
- Plattformen tilbyr komponenter som dokumentlager, Fiks IO, innsynskomponenter og testmiljÃ¸. Disse funksjonene gjÃ¸r det mulig Ã¥ bygge nye tjenester raskere, og skiller plattformen fra enkeltstÃ¥ende sluttbrukertjenester.
- Plattformen stÃ¸tter autentisering og autorisering for personer, forvaltere og integrasjoner. Det gjÃ¸r at bÃ¥de manuelle brukerflater og maskin-til-maskin-integrasjoner kan bruke samme plattformgrunnlag.

### Typiske brukssituasjoner (generisk)
- Kommuner og fylkeskommuner trenger et felles integrasjons- og forvaltningslag for mange tjenester samtidig.
- Flere leverandÃ¸rer skal levere mot samme kommunale mÃ¥larkitektur og trenger standardiserte grensesnitt.
- En tjeneste krever bÃ¥de administrativ forvaltning, teknisk integrasjon og sikker tilgangsstyring i samme plattformnÃ¦re lÃ¸p.
- Sektoren trenger raskere innfÃ¸ring av fellestjenester uten at hver virksomhet bygger alt lokalt.

### NÃ¥r FIKS-plattformen normalt ikke er fÃ¸rstevalg
- NÃ¥r behovet er en spesifikk nasjonal felleskomponent med tydelig funksjon, som autentisering, signering eller digital post til innbyggere.
- NÃ¥r behovet er rent virksomhetsinternt uten krav om samhandling pÃ¥ tvers av kommuner, fylkeskommuner eller felles sektorlÃ¸sninger.
- NÃ¥r oppgaven primÃ¦rt handler om faglig saksbehandling og ikke om plattform, integrasjon eller felles forvaltningsmÃ¸nster.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Felles plattformkomponenter, API-er og integrasjonsmÃ¸nstre | Kommunenes lokale fagsystemer |
| Bruker- og tilgangsstyring i plattformen | Lokal saksbehandling og domeneprosess |
| Teknisk grunnlag for dokumentlagring, meldinger og innsyn | Hele tjenestekjeden alene uten fagsystemer og lokale prosesser |
| TestmiljÃ¸ og felles administrasjon | Full erstatning for alle sektorspesifikke lÃ¸sninger |

## Veikart over kommende funksjonalitet
**Fakta:** KS beskriver FIKS-plattformen som en etablert plattform som fortsatt utvikles. Den tekniske beskrivelsen legger vekt pÃ¥ at nye tjenester kan bygges pÃ¥ samme grunnlag, og plattformen inngÃ¥r ogsÃ¥ som eksisterende hovedkomponent i arbeidet med Felles tjenesteplattform i kommunal sektor.

**Deduksjon:** Videreutviklingen vil trolig vÃ¦re tett knyttet til nye fellestjenester, sterkere integrasjoner og videre standardisering av felles plattformkomponenter.

## Forretningsverdi/Verdiforslag
### For kommuner og fylkeskommuner
- Reduserer behovet for Ã¥ bygge og drifte like plattformfunksjoner lokalt.
- GjÃ¸r det enklere Ã¥ ta i bruk nye fellestjenester og integrasjoner.

### For leverandÃ¸rer
- Gir ett teknisk rammeverk Ã¥ forholde seg til for kommunal sektor.
- Reduserer variasjon i integrasjonsmÃ¸nstre mellom kommuner.

### For sektoren samlet
- StÃ¸tter mer samordnet tjenesteutvikling og gjenbruk.
- Senker kompleksitet og legger til rette for bedre samhandling pÃ¥ tvers av forvaltningsnivÃ¥er.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Tilgangsstyring og datatilgang mÃ¥ vÃ¦re riktig avgrenset nÃ¥r plattformen brukes pÃ¥ tvers av mange tjenester og virksomheter. | Tydelig rollemodell, eksplisitte privilegier og tjenestespesifikke vurderinger. |
| Teknisk | Feil eller endringer i plattformkomponenter kan pÃ¥virke flere kommunale tjenester samtidig. | ModulÃ¦r forvaltning, testmiljÃ¸ og kontrollert endringshÃ¥ndtering. |
| Sikkerhet | Plattformen er et attraktivt mÃ¥l fordi den samler mange tjenester, integrasjoner og dataflyter. | Sterk autentisering, kryptering, audit-logging og sentral sikkerhetsforvaltning. |
| LeverandÃ¸r | Kommuner og leverandÃ¸rer blir avhengige av felles plattformvalg og forvaltningsbeslutninger. | Ã…pen dokumentasjon, standardiserte grensesnitt og tydelig styring av videreutvikling. |
| Brukeropplevelse | Verdien blir svak hvis plattformen ikke oversettes til konkrete, brukbare tjenester i kommunene. | Koble plattformarbeid til reelle tjenestebehov og brukerrettede lÃ¸sninger. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-plattformen/
- https://developers.fiks.ks.no/fiks-plattformen.pdf
- https://forvaltning.fiks.ks.no/
- https://status.fiks.ks.no

## Plattform
FIKS-plattformen er en felles plattformtjeneste levert for kommunal sektor.

**Fakta:**
- Plattformen bestÃ¥r av flere hoveddeler, blant annet administrasjonsflate, API-lag og digitale tjenester.
- Den tekniske dokumentasjonen beskriver egne komponenter for dokumentlager, asynkron integrasjon, innsyn og testmiljÃ¸.
- Driften leveres som tjeneste fra Intility.

**Ikke offentlig dokumentert i brukte kilder:** Full detaljarkitektur for alle underliggende driftssoner og teknologivalg per komponent.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Plattformen er laget nettopp for at flere kommuner og leverandÃ¸rer skal bruke samme byggeklosser.
- API-er, integrasjonsmÃ¸nstre og felles administrasjon gjÃ¸r det mulig Ã¥ bygge nye tjenester pÃ¥ eksisterende grunnlag.
- Produktet er mer gjenbrukbart som plattformgrunnlag enn som ferdig brukerflate.

**Vanlige kombinasjoner med andre produkter:**
- FIKS-plattformen + Maskinporten der kommunale tjenester trenger sikker maskin-til-maskin-autentisering mot statlige API-er.
- FIKS-plattformen + Folkeregisterrelaterte oppslagstjenester der kommunale tjenester trenger autoritative grunndata.
- FIKS-plattformen + sektorspesifikke fagsystemer der plattformen gir standardisert integrasjons- og forvaltningslag.

## StÃ¸tter arkitekturprinsipper
- **P5 Del og gjenbruk lÃ¸sninger** - plattformen samler felles tekniske byggeklosser som kan brukes pÃ¥ tvers av kommunal sektor.
- **P6 Lag digitale lÃ¸sninger som stÃ¸tter samhandling** - plattformen er laget for Ã¥ koble tjenester, aktÃ¸rer og data sammen gjennom felles grensesnitt og forvaltningsmÃ¸nstre.

## Finansiering
**Ikke offentlig detaljert dokumentert i brukte kilder:** Jeg fant ikke en full offentlig finansieringsmodell for FIKS-plattformen i denne arbeidsÃ¸kten.

**Deduksjon:** Plattformen forvaltes som en KS Digital-tjeneste og finansieringen er trolig knyttet til KS Digitals tjenestemodell og sektorfelles prioriteringer, men dette mÃ¥ bekreftes i egne styrings- eller prismodellkilder.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | KS Digital presenterer og forvalter plattformen som egen fellestjeneste. |
| Driftsansvar | Intility leverer drift som tjeneste; KS Digital forvalter produktet | Eksplisitt oppgitt pÃ¥ produktsiden for FIKS-plattformen. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | MÃ¥ verifiseres i egne styrings- eller prismodellkilder. |
| Styringsmodell | KS Digital med sektorrettet videreutvikling og brukermedvirkning | PDF-en beskriver tett samarbeid med sektoren og brukermedvirkning i utviklingen. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-plattformen/
- https://developers.fiks.ks.no/fiks-plattformen.pdf
- https://forvaltning.fiks.ks.no/
- https://status.fiks.ks.no

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-plattformen/ (hentet 2026-03-18)
- Nettkilde: https://developers.fiks.ks.no/fiks-plattformen.pdf (hentet 2026-03-18)

