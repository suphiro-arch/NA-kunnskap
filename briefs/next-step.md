---
date: 2026-03-16
author: codex
status: draft
topic: dokumentasjonsassistent-neste-steg
sources:
  - briefs/arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md
---

# Neste steg

## Hva er gjort
- Definert målbildet for en åpen dokumentasjonsassistent på nettsiden.
- Avgrenset MVP til kun offentlig informasjon fra repoet.
- Beskrevet anbefalt arkitektur med Hugo-frontend, egen backend og OpenAI retrieval.
- Dokumentert lisens- og avtaleavklaringer som må på plass før bygging.

## Hva gjenstår
- Velge lisens for dokumentasjonsinnholdet i repoet.
- Velge backend-plattform for assistenten.
- Lage teknisk skjelett for backend og indeksering.
- Koble enkel chatflate til Hugo-prototypen.

## Blokkere/risiko
- Repoet har ingen eksplisitt lisens for dokumentasjonsinnholdet.
- Åpen internettflate krever moderering, rate limiting og tydelig avgrensning av datagrunnlag.
- Eldre produktbeskrivelser kan gi ujevn retrieval-kvalitet.

## Konkrete neste oppgaver
1. Avklar lisens for offentlig dokumentasjonsinnhold.
2. Velg backend-plattform, helst Azure Functions.
3. Lag første backend-skjelett for `/api/ask`.
4. Lag første indeksjobb for repo-dokumentasjonen.
5. Legg inn enkel chat-widget i Hugo-prototypen.

## Referanser
- [MVP-skisse for dokumentasjonsassistent](c:/Users/HILROS/NA-kunnskap/briefs/arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md)

## Strukturforslag som er utsatt
- Vurdere ? samle produktrelatert grunnlag i en tydeligere mappe under `arkitektur/`, for eksempel `arkitektur/produkter/`.
- Vurdere om produktbeskrivelser p? sikt b?r flyttes til en egen undermappe for genererte beskrivelser, i stedet for ? ligge direkte under `results/Produktbeskrivelser/`.
- Vurdere om `sources/links.md` p? sikt b?r flyttes n?rmere produktomr?det.
- Vurdere om en bredere mappe som `ressurser/` senere b?r samle produkter, standarder, veiledninger og andre virkemidler.
