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

- Kvalitetssjekket masterfila for produkt-kapabilitet-koblinger og strammet inn koblingene til et første manuelt arbeidsutkast basert på direkte og sterke koblinger.
- Lagt om produktregisteret til eierbasert `Ressurs ID`, med ekstra kolonner for ressurstype, kapabilitetstreff og lenke til siste dokumentversjon.
- Oppdatert siste versjon av produkt `01-24` slik at feltet `Ressurs ID` nå bruker eierbasert identifikator.
- Lagt inn første arbeidsutkast for ressurser fra `KS`, `HDIR`, `NAV` og `SKATT` i produktregisteret, basert på `sources/links.md`.
- Utvidet produktregisteret med kolonnen `Ressurskategori` og lagt inn flere verifiserte kandidater fra `KS`, `NHN`, `NAV`, `Skatteetaten`, `Kartverket` og relevante EU-byggesteiner.
- Utvidet produktregisteret videre med `SIKT` som egen eiergruppe og første arbeidsutkast for Feide, FS, opptaksløsninger, Nasjonal vitnemålsdatabase og Vitnemålsportalen som kandidater for tverrsektoriell samhandling.
- Kvalitetssikret første arbeidsutkast for `SIKT`-ressursene og utvidet registeret med `Nasjonalt utdanningsregister` som egen kandidat for tverrsektoriell samhandling i utdanningssektoren.
- Kvalitetssikret `BRREG` og `KS` i produktregisteret med strammere kapabilitetstreff og tydeligere skille mellom register, plattform og tilgangstjeneste.

## Hva gjenstår
- Velge lisens for dokumentasjonsinnholdet i repoet.
- Velge backend-plattform for assistenten.
- Lage teknisk skjelett for backend og indeksering.
- Koble enkel chatflate til Hugo-prototypen.
- Oppdatere de neste produktbeskrivelsene i stigende rekkefølge etter samme metode som for `02-06`.
- Følge opp kvaliteten i selve koblingene mellom produkter og kapabiliteter, særlig i eldre produktbeskrivelser der kapabilitetsseksjonen er svakere eller mindre presis.
- Ta inn de første ressursene fra KS, Helsedirektoratet, NAV og Skatteetaten i produktregisteret med samme ID-prinsipp.
- Kvalitetssikre de nye arbeidsutkastene for `KS`, `HDIR`, `NAV` og `SKATT`, særlig eierskap, ressurstype og kapabilitetstreff.
- Ta eksplisitt stilling til om `Peppol eDelivery` fortsatt skal ligge under `BRREG`, eller om den bør få egen eierkode i registeret.
- Lage første produktbeskrivelser for de mest sentrale `SIKT`-ressursene, særlig Feide og Vitnemålsportalen.
- Kvalitetssikre de nye arbeidsutkastene for `NHN`, `KART` og `EU`, særlig om de bør stå som egne ressurser i registeret eller omtales som referanseøkosystem rundt norske løsninger.

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
8. Kvalitetssikre koblingene i masterfila mot eldre produktbeskrivelser, slik at begge retninger i webprototypen blir faglig konsistente.

## Referanser
- [MVP-skisse for dokumentasjonsassistent](c:/Users/HILROS/NA-kunnskap/briefs/arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md)

## Strukturforslag som er utsatt
- Vurdere å samle produktrelatert grunnlag i en tydeligere mappe under `arkitektur/`, for eksempel `arkitektur/produkter/`.
- Vurdere om produktbeskrivelser på sikt bør flyttes til en egen undermappe for genererte beskrivelser, i stedet for å ligge direkte under `results/Produktbeskrivelser/`.
- Vurdere om `sources/links.md` på sikt bør flyttes nærmere produktområdet.
- Vurdere om en bredere mappe som `ressurser/` senere bør samle produkter, standarder, veiledninger og andre virkemidler.


