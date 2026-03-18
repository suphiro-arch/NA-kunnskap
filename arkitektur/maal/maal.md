# Mål for nasjonal arkitektur

Kildegrunnlag:
- `sources/2025-03-18-Nasjonal Arkitektur.xml`

Denne fila samler de operative målene som faktisk er modellert i XML-kilden, og beskriver hvordan de er koblet til den overordnede arkitekturmodellen.

## Hovedmål i modellen

### Overordnet mål

| Mål | Beskrivelse |
|---|---|
| **Et velfungerende felles digitalt økosystem for samhandling og tjenesteutvikling i offentlig sektor** | Overordnet mål for den nasjonale arkitekturmodellen. Dette er målet som `Nasjonal arkitektur for samhandling` realiserer i XML-modellen. |

### Strategiske mål som påvirkes

| Mål | Rolle i modellen |
|---|---|
| **Sterkere styring og samordning av digitalisering på tvers av sektorer** | Påvirkes av det overordnede målet for nasjonal arkitektur. |
| **Vi skal ha en offentlig sektor som tilbyr bedre, mer sammenhengende digitale tjenester til innbyggere og næringsliv** | Påvirkes av det overordnede målet for nasjonal arkitektur. |
| **Norge skal være ledende på verdiskaping med data og på datadrevet forskning og innovasjon** | Påvirkes av det overordnede målet for nasjonal arkitektur. |
| **Vi skal delta i EUs satsing på dataområder der det er relevant** | Påvirkes av det overordnede målet for nasjonal arkitektur. |
| **Få på plass en nasjonal infrastruktur for kunstig intelligens (KI)** | Påvirkes av det overordnede målet for nasjonal arkitektur. |
| **Næringslivet skal ha gode rammevilkår for å utvikle og bruke KI. Offentlig sektor skal anvende KI for å utvikle bedre tjenester og løse oppgaver mer effektivt** | Påvirkes av det overordnede målet for nasjonal arkitektur. |
| **Sørge for at alle har et tilbud om en elektronisk identitet** | Påvirkes av det overordnede målet for nasjonal arkitektur. |
| **Næringslivets konkurranseevne styrkes gjennom innovativ bruk av data og digitalisering** | Påvirkes av det overordnede målet for nasjonal arkitektur. |

## Kobling mellom arkitektur og mål

XML-modellen viser disse eksplisitte koblingene:

1. `Nasjonal arkitektur for samhandling` realiserer målet `Et velfungerende felles digitalt økosystem for samhandling og tjenesteutvikling i offentlig sektor`.
2. Dette overordnede målet påvirker de åtte strategiske målene listet over.

## Viktig avgrensning

XML-kilden viser ikke en full operativ kobling fra hver hovedkapabilitet til hvert strategiske mål.

Det betyr:
- modellen kan brukes som grunnlag for et eget målspor i repoet
- men den kan ikke brukes direkte som autoritativ detaljkobling mellom hver kapabilitet og hvert mål uten videre kuratering

## Anbefalt bruk i repoet

- Bruk denne fila som kuratert oversikt over målsporet i arkitekturmodellen.
- Behold `capabilities.yaml` som kuratert kapabilitetsmaster.
- Hvis repoet senere trenger eksplisitt kobling mellom kapabiliteter og mål, bør det opprettes en egen kuratert fil for dette, ikke bygges direkte fra rå XML.
