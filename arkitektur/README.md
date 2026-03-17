# Arkitektur

Denne mappa samler det strukturerte arkitekturgrunnlaget i repoet.

## Innhold
- `kapabiliteter/`: kapabilitetskart og tilhørende strukturdata
- `prinsipper/`: arkitekturprinsipper og føringer
- `produkter/`: produktnummerering og andre strukturer som gjelder produktområdet

## Koblinger mellom produkter og kapabiliteter
- `kapabiliteter/produkt-kapabilitet-koblinger.yaml` er masterfila for koblingen mellom produkter og kapabiliteter.
- Fila vedlikeholdes manuelt i repoet og er autoritativ kilde for koblingen mellom produkter og kapabiliteter.
- Fila ligger foreløpig i JSON-kompatibel YAML for å kunne leses uten ekstra parseravhengigheter i generatorene.
- Hugo-generatorene skal bruke denne fila som felles grunnlag begge veier:
  - fra produkter til kapabiliteter i produktoverblikket
  - fra kapabiliteter til produkter i kapabilitetssidene

Mappa brukes som faglig kildeområde. Leveranser og genererte beskrivelser hører fortsatt hjemme i `results/`.

