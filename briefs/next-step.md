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
- Oppdatert produktbeskrivelsene for produkt `02-06` til nye `v3-codex`-versjoner med sterkere kildegrunnlag og strammere kapabilitetsvalg.
- Oppdatert prompt og mal for produkt-canvas slik at nye beskrivelser ikke skal starte med egen linje for målgruppe, og `Ressurs ID` ikke skal ha parentesforklaring.
- Strammet inn metodekravet for kapabiliteter: bare direkte og sterke koblinger til produktets egen funksjon skal tas med.
- Regenerert produktover­sikten i Hugo-prototypen slik at siste versjon for produkt `02-06` nå vises på nettsiden.
- Lagt om publiseringsmodellen for Hugo-prototypen til GitHub Pages artifact-deploy direkte fra `web/hugo-prototype/`.

## Hva gjenstår
- Velge lisens for dokumentasjonsinnholdet i repoet.
- Velge backend-plattform for assistenten.
- Lage teknisk skjelett for backend og indeksering.
- Koble enkel chatflate til Hugo-prototypen.
- Oppdatere de neste produktbeskrivelsene i stigende rekkefølge etter samme metode som for `02-06`.

## Blokkere/risiko
- Repoet har ingen eksplisitt lisens for dokumentasjonsinnholdet.
- Åpen internettflate krever moderering, rate limiting og tydelig avgrensning av datagrunnlag.
- Eldre produktbeskrivelser kan gi ujevn retrieval-kvalitet.
- GitHub Pages-oppsettet må verifiseres i repo-innstillingene slik at artifact-deploy faktisk er valgt som publiseringskilde.

## Konkrete neste oppgaver
1. Avklar lisens for offentlig dokumentasjonsinnhold.
2. Velg backend-plattform, helst Azure Functions.
3. Lag første backend-skjelett for `/api/ask`.
4. Lag første indeksjobb for repo-dokumentasjonen.
5. Legg inn enkel chat-widget i Hugo-prototypen.
6. Fortsett revisjon av produktbeskrivelser med samme regler for direkte kapabilitetskobling og ryddigere metadata.
7. Verifiser at GitHub Pages bruker Actions-baserte deployments og ikke gammel `docs/`-publisering.

## Referanser
- [MVP-skisse for dokumentasjonsassistent](c:/Users/HILROS/NA-kunnskap/briefs/arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md)

## Strukturforslag som er utsatt
- Vurdere ? samle produktrelatert grunnlag i en tydeligere mappe under `arkitektur/`, for eksempel `arkitektur/produkter/`.
- Vurdere om produktbeskrivelser p? sikt b?r flyttes til en egen undermappe for genererte beskrivelser, i stedet for ? ligge direkte under `results/Produktbeskrivelser/`.
- Vurdere om `sources/links.md` p? sikt b?r flyttes n?rmere produktomr?det.
- Vurdere om en bredere mappe som `ressurser/` senere b?r samle produkter, standarder, veiledninger og andre virkemidler.
