# Produkt-canvas: Felles tjenesteplattform

## Navn
Felles tjenesteplattform

## Ressurs ID
KS-005

## Status/Livsfase
**Under utvikling** - prosjekt for ny kommunal tjenesteplattform med finansiert første fase og publisert konseptretning.

**Fakta:** KS Digital beskriver Felles tjenesteplattform som et prosjekt i utvikling. Digdir omtaler at KS Digital har fått finansiering til en første fase via Digifin og at første steg går ut 2025 for å utforske og validere konsept og løsningsforslag.

## Modenhet
**Middels modenhet** - konsept, hovedkomponenter og mål er beskrevet offentlig, men løsningen er fortsatt i prosjekt- og utprøvingsfase.
- Det finnes et tydelig målbilde og en komponentmodell med applikasjonsplattform, dataplattform, Allmenningen og FIKS-plattformen.
- Samtidig er flere deler fortsatt under utvikling, og Digdirs anbefalingsbrev viser at målbildet, rollen mot markedet og utprøvingsløpet fortsatt må modnes.

**Deduksjon:** Modenheten er høyere på konsept og retning enn på ferdig operativ løsning. Produktet bør derfor vurderes som under utvikling, ikke som etablert fellestjeneste i full drift.

## Kort beskrivelse
Felles tjenesteplattform er KS Digitals program for å etablere et bredere felles plattformgrunnlag for tjenesteutvikling i kommunal sektor. Løsningen skal samle applikasjonsplattform, dataplattform, Allmenningen og den eksisterende FIKS-plattformen i et mer helhetlig økosystem for deling, utvikling og samordning. Produktet er særlig relevant når kommunal sektor trenger et nasjonalt rammeverk for raskere tjenesteutvikling, større gjenbruk og bedre samhandling med både leverandørmarkedet og andre offentlige aktører.

## Kapabiliteter
- **Samarbeid: Organisatorisk samhandling** er direkte relevant fordi prosjektet skal samordne tjenesteutvikling på tvers av kommuner, fylkeskommuner og andre offentlige aktører.
- **Tjenesteutvikling: Gjenbrukbare tjenester** er sentral fordi plattformen er laget for deling, gjenbruk og en kommunal app store-lignende modell.
- **Tjenesteutvikling: Utviklings- og kjøretidsmiljø** er direkte relevant fordi applikasjonsplattform og dataplattform er hovedkomponenter i den planlagte løsningen.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals kilder brukt i denne arbeidsøkten.

## Produktmål
Dokumenterte mål:
- Tilrettelegge for god, trygg og effektiv tjenesteutvikling med og for kommunal sektor.
- Øke fart på tjenesteutvikling i kommuner og fylkeskommuner.
- Øke grad av deling og gjenbruk, og øke grad av standardiserte og sammenhengende tjenester.

Operative mål utledet fra kildene:
- Redusere dobbeltarbeid og kostnader.
- Gjøre det lettere å utvikle og dele løsninger på tvers av sektoren.
- Skape et tydeligere samspill mellom felles plattform, leverandørmarkedet og lokale behov.

## Brukerbehov
- Kommunal sektor trenger høyere gjennomføringskraft i digitalisering.
- Kommuner trenger lettere tilgang til gjenbrukbare komponenter og mer standardiserte utviklingsløp.
- Leverandørmarkedet trenger tydeligere rammer for hva som skal være felles og hva som skal være lokalt.
- Sektoren trenger et bedre samspill mellom applikasjoner, data og felles støttefunksjoner.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Raskere og tryggere tjenesteutvikling | Bruk av plattformgrunnlag og felles komponenter | Primær målgruppe for prosjektet |
| Leverandører | Tydelige grensesnitt og rammer for hva som skal utvikles og deles | Utvikling og integrasjon mot felles plattformkomponenter | Viktig målgruppe for utbredelse |
| KS Digital | Etablere og forvalte et sektorfelles plattformgrunnlag | Programstyring, utprøving og videreutvikling | Eier prosjektet |
| Andre offentlige aktører | Samordning og samhandling med kommunal sektor | Samarbeid rundt delte løsninger og felles standarder | Sekundær målgruppe |

## Hovedfunksjoner
### Primære funksjoner
- Felles tjenesteplattform skal samle flere hovedkomponenter i én helhetlig struktur. Det gjør produktet relevant som plattformstrategi og ikke bare som enkelttjeneste.
- Applikasjonsplattformen skal gi tilgang til gjenbrukbare komponenter, standardiserte grensesnitt og verktøy for utvikling og drift. Dette gjør løsningen aktuell når sektoren trenger et felles teknisk grunnlag for nye digitale tjenester.
- Dataplattformen skal støtte deling og bruk av data på tvers av kommuner. Det skiller løsningen fra en ren applikasjonsplattform, fordi dataforvaltning og deling er en egen hovedkomponent.
- Allmenningen skal samle oversikter, ressurser og støtte til digitaliseringsarbeid. Felles tjenesteplattform handler dermed også om styring og samordning, ikke bare om runtime og API-er.
- Den eksisterende FIKS-plattformen skal være integrasjonsgrunnlaget som får applikasjoner og data til å snakke sammen. Dette er et viktig skille mot FIKS-plattformen alene, som allerede er i drift som operativ plattform.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Applikasjonsplattform, dataplattform, Allmenningen og FIKS-plattformen som helhetlig konsept | Fullt ferdig produksjonsplattform for alle deler i dag |
| Felles retning for utvikling, deling og samordning | Erstatning av alle fagsystemer i kommunal sektor |
| Prosjekt, utprøving og validering av konsept | Lokal tjenesteutvikling utenfor felles rammer |
| Plattformgrunnlag for gjenbrukbare løsninger | Ferdig implementert nasjonal minimumsløsning på alle områder |

## Veikart over kommende funksjonalitet
**Fakta:** KS Digital beskriver tjenesteplattformen som et prosjekt i utvikling, og Digdir opplyser at første steg går ut 2025 for å utforske og validere konseptet. Produktsiden viser løpende prosjektinformasjon og siste nytt.

**Fakta:** Offentlig publiserte milepæler i denne arbeidsøkten handler primært om konseptfase, mål, gevinst og utprøving, ikke om ferdig utrullingsplan.

**Deduksjon:** Veikartet vil sannsynligvis bevege seg fra utprøving og pilotering til gradvis produksjonssetting av delkomponenter og sektorutbredelse.

## Forretningsverdi/Verdiforslag
### For kommunal sektor
- Kan redusere dobbeltarbeid og gi raskere verdi av investeringer.
- Kan øke farten i tjenesteutvikling og gjøre det enklere å gjenbruke løsninger.

### For leverandørmarkedet
- Kan gi klarere tekniske og organisatoriske rammer for samspill med sektoren.

### For offentlig sektor samlet
- Kan styrke samordning mellom kommunal og statlig digitalisering.
- Kan legge grunnlag for mer standardiserte og sammenhengende tjenester.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Uklart handlingsrom og rollefordeling kan gjøre felles anskaffelser og samstyring krevende. | Avklare fullmakter, roller og spilleregler tidlig. |
| Teknisk | Kompleksitet øker når flere hovedkomponenter og mange målgrupper skal bindes sammen. | Stegvis utprøving, tydelig avgrensning og pilotering før bred utrulling. |
| Sikkerhet | Plattformen skal bli et sentralt grunnlag for mange tjenester og må derfor ha innebygd sikkerhet fra start. | Bygge trygg digitalisering inn i konsept, datahåndtering og videre arkitekturvalg. |
| Leverandør | Uklar rolle mot markedet kan skape motstand eller lav utbredelse. | Tydeliggjøre hva som er felles, hva som er lokalt og hvordan leverandørene skal samhandle med plattformen. |
| Brukeropplevelse | Kommunene får liten gevinst hvis plattformen forblir et uklart konsept uten tydelige nytteeksempler. | Ta utprøvingen helt ut i produksjon og dokumentere konkrete gevinster. |

## Kanaler
- https://ksdigital.no/tjenestene/utviklingsprosjekter/felles-tjenesteplattform/
- https://www.digdir.no/digitaliseringsradet/ks-digital-tiltaket-felles-tjenesteplattform/7556

## Plattform
Felles tjenesteplattform er et utviklingsprosjekt for et fremtidig plattformøkosystem i kommunal sektor.

**Fakta:**
- Prosjektet skal bestå av fire hovedkomponenter: applikasjonsplattform, dataplattform, Allmenningen og FIKS-plattformen.
- Applikasjonsplattformen og dataplattformen beskrives som sentrale byggeklosser for utvikling, drift, deling og bruk av data.

**Ikke offentlig dokumentert i brukte kilder:** Endelig teknisk arkitektur, valg av konkrete plattformteknologier og full produksjonsmodell.

## Gjenbruk
**Høy forventet gjenbruksverdi:**
- Prosjektet er direkte innrettet mot deling og gjenbruk av løsninger, komponenter og data.
- Gjenbruksverdien er foreløpig mest dokumentert som mål og retning, ikke som fullt realisert funksjonssett.

## Støtter arkitekturprinsipper
- **P5 Del og gjenbruk løsninger** - gjenbruk er et eksplisitt mål for plattformen og omtales som en kommunal app store-lignende tilnærming.
- **P6 Lag digitale løsninger som støtter samhandling** - plattformen er laget for å støtte standardiserte og sammenhengende tjenester på tvers av sektoren.
- **P2 Ta arkitektur-beslutninger på rett nivå** - prosjektet handler om å løfte noen kapabiliteter til et felles kommunalt nivå i stedet for å løse alt lokalt.

## Finansiering
**Fakta:** Digdir opplyser at KS Digital har fått finansiering til en første fase gjennom Digifin-ordningen.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Langsiktig finansieringsmodell for full etablering og drift av hele tjenesteplattformen.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | KS Digital eier og driver prosjektet. |
| Driftsansvar | Ikke relevant som full drift i nåværende fase | Løsningen er fortsatt prosjekt under utvikling. |
| Budsjettansvar | KS Digital med finansiering til første fase via Digifin | Oppgitt i Digdirs anbefalingsbrev. |
| Styringsmodell | Prosjektstyring i KS Digital med sektorsamspill og samstyringsforankring | Både KS-siden og Digdir beskriver samspill med kommunesektoren og samstyringsorganer. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/utviklingsprosjekter/felles-tjenesteplattform/
- https://www.digdir.no/digitaliseringsradet/ks-digital-tiltaket-felles-tjenesteplattform/7556

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://ksdigital.no/tjenestene/utviklingsprosjekter/felles-tjenesteplattform/ (hentet 2026-03-18)
- Nettkilde: https://www.digdir.no/digitaliseringsradet/ks-digital-tiltaket-felles-tjenesteplattform/7556 (hentet 2026-03-18)
