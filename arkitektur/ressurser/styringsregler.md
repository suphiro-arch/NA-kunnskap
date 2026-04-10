# Styringsregler for ressurser

Denne fila definerer hvordan ressursområdet skal struktureres og klassifiseres i repoet.

## Formål
- gi tydelige kriterier for hva som skal inn i ressursområdet
- skille mellom ressurser som brukes operativt, ressurser som gir føringer, og arenaer for samordning
- gjøre klassifisering mer forutsigbar når nye ressurser legges inn i analyser, register eller webstruktur

## Hovedkategorier

### 1. Operative løsninger og tjenester
Brukes for ressurser som har en tydelig operativ rolle i bruk, integrasjon eller forvaltning.

Kjennetegn:
- tilbyr funksjonalitet som kan brukes direkte i et løsnings- eller samhandlingslandskap
- er noe man kan koble seg til, ta i bruk, bygge rundt eller være avhengig av i praksis
- kan være tekniske eller funksjonelle løsninger, men skal ha en tydelig operativ rolle utover ren veiledning eller styring

Typiske eksempler:
- felleskomponenter
- plattformer
- registre
- portaler
- API-er og datadelingstjenester
- sektorløsninger med varig og gjenbrukbar rolle i samhandling

Eksempler i denne logikken:
- `FINT Arkiv`
- `FINT Felleskomponent`
- `VIGO`

### 2. Normerende ressurser
Brukes for ressurser som primært gir føringer for hvordan løsninger skal forstås, beskrives, utformes eller samordnes.

Kjennetegn:
- brukes som grunnlag for utforming, vurdering, standardisering eller semantisk samordning
- er ikke primært en løsning i drift eller en operativ tjeneste
- beskriver begreper, modeller, standarder, mønstre, krav eller anbefalinger

Typiske eksempler:
- standarder
- veiledere
- referansearkitektur
- informasjonsmodeller
- begrepsmodeller

Eksempler i denne logikken:
- `FINT Informasjonsmodell`
- semantiske modeller og referansemodeller
- nasjonale eller europeiske standarder som brukes som styrende grunnlag

### 3. Samarbeidsfora
Brukes for arenaer som først og fremst støtter samordning, prioritering, forankring eller strategisk retning.

Kjennetegn:
- er ikke primært en løsning eller et normerende dokument
- samler aktører for koordinering, beslutningsstøtte eller forankring
- påvirker prioriteringer, veikart, retning eller samhandling på tvers

Typiske eksempler:
- råd
- nettverk
- samordningsarenaer
- faste tverrsektorielle samarbeidsfora

Eksempler i denne logikken:
- `Skate`
- arkitekturråd
- sektorvise samordningsfora

## Beslutningsregler for klassifisering
Bruk disse spørsmålene i rekkefølge:

1. Er dette noe man bruker direkte i drift, integrasjon eller løsningsdesign?
Da er det som hovedregel en `operativ løsning eller tjeneste`.

2. Er dette primært noe som gir føringer for begreper, struktur, design, standardisering eller vurdering?
Da er det som hovedregel en `normerende ressurs`.

3. Er dette primært en arena for koordinering, forankring eller prioritering?
Da er det som hovedregel et `samarbeidsforum`.

4. Hvis ressursen treffer flere kategorier:
Velg én primærkategori og beskriv øvrige trekk i metadata eller tekst, ikke ved dobbeltplassering.

## Minstekrav for å opprette en egen ressurs
En ressurs bør normalt bare opprettes som egen enhet når den:
- har tydelig navn og avgrensning
- har identifiserbar eier, forvalter, ansvarlig aktør eller ansvarlig arena
- har dokumentert relevans for arkitektur-, gjenbruks- eller caseanalyser
- kan beskrives selvstendig, ikke bare som et løst delbegrep i en annen ressurs

## Opptakskrav for å bli del av NA-oversikten
NA-oversikten skal være kuratert. Den skal ikke være en generell lenkesamling eller fullstendig katalog over alt som finnes i økosystemet.

En ressurs bør normalt bare tas inn i NA-oversikten når den oppfyller alle disse kravene:
- har tydelig og varig rolle i nasjonal eller tverrsektoriell digital samhandling, informasjonsforvaltning, tillit eller samordning
- kan påvirke arkitekturvalg, prioritering, gjenbruksvurdering eller anbefalinger i caseanalyser
- er tilstrekkelig avgrenset til å kunne stå som egen ressurs, ikke bare som underside, kanal, funksjon eller detalj i en større ressurs
- har identifiserbar eier, forvalter eller ansvarlig arena som gjør ressursen sporbar og forvaltningsmessig forståelig
- har et kildegrunnlag som er stabilt nok til at ressursen kan beskrives uten omfattende gjetting

For sektorspesifikke ressurser gjelder i tillegg en høyere terskel:
- ressursen bør normalt bare tas inn når den også har tydelig betydning for samhandling på tvers av sektorer eller mellom forvaltningsnivåer
- det er ikke tilstrekkelig at ressursen er viktig, stor eller mye brukt innen egen sektor alene

## Vurderingskriterier utover minstekravene
Når minstekravene er oppfylt, bør disse kriteriene brukes for å vurdere om ressursen faktisk bør prioriteres inn:
- brukes eller påvirker flere virksomheter, sektorer eller forvaltningsnivåer
- har tydelig kobling til en eller flere kapabiliteter i nasjonal arkitektur
- er relevant som gjenbrukbar byggestein, felles føring, felles informasjonsgrunnlag eller samordningsarena
- går igjen i case, analyser, arkitekturdiskusjoner eller behovsvurderinger
- representerer en viktig avhengighet, muliggjører eller begrensning i samhandlingslandskapet
- har tilstrekkelig modenhet eller varighet til å være nyttig også utover et kort tidsvindu

## Ressurser som normalt ikke skal inn
Følgende skal normalt ikke inn som egne ressurser i NA-oversikten:
- enkeltarrangementer, konferanser og kampanjer
- nyhetssaker, kunngjøringer og tidsavgrensede lanseringer
- generelle temaområder uten tydelig ressursavgrensning
- rene informasjonssider uten selvstendig ressursrolle
- interne arbeidsformer, programmer eller satsinger uten tydelig leveranse eller varig ressursform
- små delkomponenter som beskrives bedre som del av en større ressurs

## Praktisk beslutningstest ved nye kandidater
Bruk disse fem spørsmålene før en ny kandidat tas inn:
1. Er dette en tydelig ressurs, ikke bare et tema, tiltak eller en kommunikasjonsside?
2. Har ressursen en varig rolle i samhandlingslandskapet?
3. Kan ressursen påvirke vurderinger eller anbefalinger i et case?
4. Er ressursen viktig nok til å stå som egen oppføring, og ikke bare som del av en annen ressurs?
5. Har vi godt nok kildegrunnlag til å beskrive ressursen saklig?

Hvis svaret ikke er tydelig ja på minst fire av fem spørsmål, bør ressursen normalt ikke tas inn ennå.

## Forholdet til kapabiliteter
- kapabiliteter skal brukes som faglig kobling, ikke som primær mappeinndeling
- en ressurs kan ha én primærkapabilitet og flere sekundære kapabiliteter
- hvis en ressurs treffer mange kapabiliteter, skal den fortsatt ha én primær ressurskategori
- kapabiliteter egner seg godt til filtrering, webnavigasjon og analyse på tvers

## Forholdet til produkt-canvas
- dagens `produkt-canvas` passer fortsatt godt for operative løsninger og tjenester som beskrives som produkter, plattformer, registre eller felleskomponenter
- normerende ressurser og samarbeidsfora skal ikke presses inn i produkt-canvas uten bevisst tilpasning
- når repoet utvides videre, bør det vurderes egne maler for normerende ressurser og samarbeidsfora

## Vurdering av dagens mal som utgangspunkt
`config/templates/produkt-canvas-template.md` er et godt utgangspunkt for `operative løsninger og tjenester`, men ikke en ferdig universell mal for alle ressurstyper.

### Det som kan gjenbrukes bredt
- navn og identifikator
- kort beskrivelse
- kapabiliteter
- mål
- brukergrupper
- avgrensning
- forvaltning/eier
- lenker og kildegrunnlag

### Felt som passer best for operative løsninger og tjenester
- status/livsfase
- modenhet
- hovedfunksjoner
- kanaler
- plattform
- veikart
- gjenbruk
- finansiering

### Felt som normalt bør tilpasses for normerende ressurser
- `Hovedfunksjoner` bør ofte erstattes eller suppleres med `Normerende innhold`, `Bruksområde` og `Når ressursen bør brukes`
- `Kanaler` og `Plattform` er ofte mindre relevante eller bør erstattes med `Publiseringsform` og `Forvaltningsarena`
- `Gjenbruk` bør tolkes som faglig anvendelse og innarbeiding, ikke teknisk gjenbruk

### Felt som normalt bør tilpasses for samarbeidsfora
- `Hovedfunksjoner` bør ofte erstattes eller suppleres med `Mandat`, `Beslutningsmyndighet`, `Deltakere`, `Arbeidsform` og `Hvilke ressurser forumet påvirker`
- `Plattform`, `Kanaler` og deler av `Gjenbruk` er ofte lite relevante i sin nåværende form
- `Forvaltning/eier` bør utvides med sekretariat, medlemskap eller styringslinje når dette finnes
- `Når forumet bør involveres` og `Typiske saker og leveranser` er viktige felt for senere analysebruk

### Foreløpig arbeidsregel
- bruk dagens `produkt-canvas` direkte for operative løsninger og tjenester
- bruk egne avledede maler for normerende ressurser og samarbeidsfora
- bruk egen prompt for ikke-operative ressursbeskrivelser når slike ressurser skal opprettes eller revideres

### Tilgjengelige maler
- `config/templates/produkt-canvas-template.md` brukes direkte for operative løsninger og tjenester
- `config/templates/normerende-ressurs-template.md` brukes for normerende ressurser
- `config/templates/samarbeidsforum-template.md` brukes for samarbeidsfora
- `config/prompts/ressursbeskrivelser.system.md` brukes som styrende prompt for normerende ressurser og samarbeidsfora

## Første arbeidsklassifisering av omtalte ressurser
| Ressurs | Primærkategori | Kommentar |
|---|---|---|
| FINT Arkiv | Operative løsninger og tjenester | Operativ løsnings- og integrasjonsressurs |
| FINT Felleskomponent | Operative løsninger og tjenester | Operativ komponent i løsningslandskapet |
| FINT Informasjonsmodell | Normerende ressurs | Styrende modellgrunnlag, ikke primært løsning i drift |
| VIGO | Operative løsninger og tjenester | Operativ sektorressurs med funksjonell rolle i bruk |
| Skate | Samarbeidsforum | Samordnings- og prioriteringsarena |

## Praktisk styringsregel
Når en ny ressurs vurderes:
- klassifiser først ressursen etter funksjon og rolle
- vurder deretter hvilke kapabiliteter den støtter
- velg mappeplassering og mal ut fra ressurskategori, ikke bare ut fra sektor eller kapabilitet

## Filnavn og identifikator
- nye ressursfiler skal følge samme filnavnsmønster som øvrige nummererte beskrivelser i porteføljen
- bruk løpenummer fra `arkitektur/ressurser/produktnummerering.md` først i filnavnet når ressursen er registerført
- anbefalt mønster er `NN-Navn-vX-forfatter.md` for operative og normerende ressurser
- bruk ASCII i filnavn, men behold normal navngivning med store bokstaver der dette er etablert i produktnavnet, for eksempel `70-FINT-Felleskomponent-v1-codex.md`
- unngå unummererte særnavn for nye ressursfiler når ressursen allerede har fått fastsatt løpenummer og ressurs-ID

