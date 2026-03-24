# Arkitektur

Denne mappa samler det strukturerte arkitekturgrunnlaget i repoet.

## Innhold
- `kapabiliteter/`: kapabilitetskart og tilhørende strukturdata
- `maal/`: kuraterte mål og kobling til arkitekturmodellen
- `prinsipper/`: arkitekturprinsipper og føringer
- `produkter/`: produktnummerering, produktbeskrivelser og andre strukturer som gjelder produktområdet

## Kilde og kuratering
- `sources/2025-03-18-Nasjonal Arkitektur.xml` er råkilde for kapabilitets- og prinsippmodellen.
- `kapabiliteter/capabilities.yaml` er repoets kuraterte arbeidsfil for kapabilitetsstrukturen.
- `prinsipper/principles.md` er repoets kuraterte arbeidsfil for prinsipper og koblingen til hovedkapabiliteter.
- `maal/maal.md` er repoets kuraterte arbeidsfil for målsporet i modellen.

## Videre bruk i repoet
- `capabilities.yaml` brukes videre av generatorer, analyser og webgrunnlag som trenger kapabilitetsnavn, hierarki og prinsippreferanser.
- `principles.md` brukes videre som kuratert kilde for prinsippnavn og prinsipp-kapabilitetskoblinger i analyser, produktbeskrivelser og prinsippsiden i weben.
- `maal/maal.md` brukes videre som kuratert referanse når analyser eller dokumentasjon trenger kobling mellom nasjonal arkitektur og strategiske mål.
- Webens prinsippside synkes fra `prinsipper/principles.md`, slik at repoet har én styrende fil for prinsippinnholdet.

## Avgrensning mellom filer
- `capabilities.yaml` skal beskrive kapabilitetsstrukturen, ikke være en samlefil for mål- og prinsipptekst.
- `principles.md` skal samle prinsippnavn, prinsippforklaringer og prinsipp-kapabilitetskoblinger.
- `maal/maal.md` skal samle målsporet fra modellen.

## Koblinger mellom produkter og kapabiliteter
- `kapabiliteter/produkt-kapabilitet-koblinger.yaml` er masterfila for koblingen mellom produkter og kapabiliteter.
- Fila vedlikeholdes manuelt i repoet og er autoritativ kilde for koblingen mellom produkter og kapabiliteter.
- Fila ligger foreløpig i JSON-kompatibel YAML for å kunne leses uten ekstra parseravhengigheter i generatorene.
- Hugo-generatorene skal bruke denne fila som felles grunnlag begge veier:
  - fra produkter til kapabiliteter i produktoverblikket
  - fra kapabiliteter til produkter i kapabilitetssidene

Mappa brukes som faglig kildeområde. Produktbeskrivelser ligger i `produkter/produktbeskrivelser/`, mens øvrige leveranser fortsatt kan ligge i `results/`.

Innenfor `produkter/` er `produktnummerering.md` den operative masterfila for produktregister, ressurs-ID-er og statusoversikt.

