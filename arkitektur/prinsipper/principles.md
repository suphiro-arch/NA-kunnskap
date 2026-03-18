# Prinsipper for nasjonal arkitektur

Kildegrunnlag:
- `sources/2025-03-18-Nasjonal Arkitektur.xml`
- `arkitektur/kapabiliteter/capabilities.yaml`

Denne fila samler de sju arkitekturprinsippene som faktisk er koblet til kapabilitetsmodellen, og viser hvilke hovedkapabiliteter som realiserer hvert prinsipp.

Denne fila erstatter de tidligere dupliserte blokkene for prinsippnavn, strategiske mål og prinsipp-kapabilitet-begrunnelser som tidligere lå nederst i `arkitektur/kapabiliteter/capabilities.yaml`.

## Prinsipper

| Prinsipp | Hva det betyr i praksis |
|---|---|
| **P1: Ta utgangspunkt i brukernes behov** | Løsninger skal formes ut fra reelle behov hos innbyggere, virksomheter og forvaltning, ikke ut fra organisatoriske siloer. |
| **P2: Ta arkitekturbeslutninger på rett nivå** | Beslutninger skal tas så nær problemet som mulig, men løftes når konsekvensene går på tvers av flere aktører. |
| **P3: Bidra til digitaliseringsvennlige regelverk** | Regelverk skal støtte digital samhandling, automatisering og sammenhengende tjenester. |
| **P4: Del og gjenbruk data** | Data skal kunne beskrives, finnes og brukes på tvers når det er hjemmel og behov for det. |
| **P5: Del og gjenbruk løsninger** | Felles behov skal dekkes med gjenbrukbare byggeklosser framfor parallelle særutviklede løsninger. |
| **P6: Lag digitale løsninger som støtter samhandling** | Tjenester skal bygges slik at de kan inngå i større sammenhenger med andre tjenester og aktører. |
| **P7: Sørg for tillit til oppgaveløsningen** | Sikkerhet, sporbarhet og dokumenterbarhet skal være integrert i løsningene. |

## Kobling mellom prinsipper og kapabiliteter

| Prinsipp | Hovedkapabiliteter |
|---|---|
| **P1: Ta utgangspunkt i brukernes behov** | `Sluttbrukertjenester`, `Tjenesteutvikling` |
| **P2: Ta arkitekturbeslutninger på rett nivå** | `Strategisk styring`, `Samarbeid` |
| **P3: Bidra til digitaliseringsvennlige regelverk** | `Juridisk samhandling` |
| **P4: Del og gjenbruk data** | `Datakilder`, `Datautveksling og integrasjon`, `Datadrevet` |
| **P5: Del og gjenbruk løsninger** | `Sluttbrukertjenester`, `Tjenesteutvikling` |
| **P6: Lag digitale løsninger som støtter samhandling** | `Samarbeid`, `Datautveksling og integrasjon`, `Informasjonsforvaltning`, `Standardisering`, `Veiledning` |
| **P7: Sørg for tillit til oppgaveløsningen** | `Tillit`, `Informasjonssikkerhet`, `Juridisk samhandling` |

## Avgrensning

Denne fila bruker de prinsippene som er aktivt koblet til top-level-kapabiliteter i modellen. XML-kilden inneholder også generiske eller sideordnede principelementer, som `Prinsipp`, `Kun en gang`, `FAIR` og `NSM`, men disse er ikke modellert som del av den operative koblingen mellom prinsipper og kapabiliteter.
