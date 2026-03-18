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
- Kvalitetssikret `HDIR`, `NHN` og `NAV` i produktregisteret med tydeligere skille mellom portal, tillitstjeneste, delingsløsning og register.
- Kvalitetssikret `SKATT`, `KART` og `DIGDIR` i produktregisteret med mer direkte kapabilitetstreff, særlig for `eFormidling`, `Norge.no`, `Skatteetatens delingstjenester` og `Geonorge`.
- Opprettet første produktbeskrivelser for KS-ressursene `KS-001` til `KS-006` og synkronisert produktregister, masterfil for produkt-kapabilitet-koblinger og webgrunnlag mot de nye filene.
- Oppdatert lenkedokumentet med egne lenker for ELMA, OpenPeppol og EHF-/Peppol-veiledning, og opprettet nye `v3-codex`-beskrivelser for `ELMA` og `Peppol eDelivery`.
- Avklart at `EU-003 eDelivery Building Block` beholdes i registeret som egen EU-ressurs, men som referanseramme og byggestein rundt samme problemområde som `Peppol eDelivery`.
- Utvidet EU-delen med `EU Open Source Solutions Catalogue`, `Interoperable Europe Solutions` og `Core Vocabularies` som referanseressurser, og oppdatert lenkedokumentet med flere offisielle interoperabilitetskilder fra Interoperable Europe.
- Sammenlignet ny XML-kilde for nasjonal arkitektur med `capabilities.yaml`, laget avviksrapport i `sources/` og rettet manglende `P6`-kobling for `Datautveksling og integrasjon`.
- Fylte ut `arkitektur/prinsipper/principles.md` med operative prinsipper og synket prinsippkoblingene mot webversjonen.
- Knyttet `arkitektur/prinsipper/principles.md` direkte inn i videre bruk: som kilde for prinsipper i produktanalyser, som synkgrunnlag for webens prinsippside og som del av repoets dokumenterte arbeidsflyt.
- Dokumentert råkilder, kuraterte arbeidsfiler og videre prosessering i [struktur-og-bearbeiding.md](c:/Users/HILROS/NA-kunnskap/arkitektur/struktur-og-bearbeiding.md).
- Kartlagt mål- og ressursrelasjoner i XML-kilden, dokumentert at ressursrelasjonene ikke er på samme nivå som repoets produktmaster, og opprettet [maal.md](c:/Users/HILROS/NA-kunnskap/arkitektur/maal/maal.md) som første kuraterte måloversikt.
- Ryddet `capabilities.yaml` slik at den nå bare inneholder kapabilitetsstrukturen, mens prinsipptekst og målspor ligger i egne kuraterte filer.
- Utvidet `maal.md` med de få eksplisitte kapabilitet-til-mål-koblingene som faktisk finnes i XML-kilden, og markerte hvilke som er operative versus generiske.

## Hva gjenstår
- Velge lisens for dokumentasjonsinnholdet i repoet.
- Velge backend-plattform for assistenten.
- Lage teknisk skjelett for backend og indeksering.
- Koble enkel chatflate til Hugo-prototypen.
- Oppdatere de neste produktbeskrivelsene i stigende rekkefølge etter samme metode som for `02-06`.
- Følge opp kvaliteten i selve koblingene mellom produkter og kapabiliteter, særlig i eldre produktbeskrivelser der kapabilitetsseksjonen er svakere eller mindre presis.
- Ta inn de første ressursene fra KS, Helsedirektoratet, NAV og Skatteetaten i produktregisteret med samme ID-prinsipp.
- Kvalitetssikre de nye arbeidsutkastene for `KS`, `HDIR`, `NAV` og `SKATT`, særlig eierskap, ressurstype og kapabilitetstreff.
- Vurdere om flere helse- og NAV-ressurser bør inn i registeret, særlig flere delingstjenester og nasjonale innbyggertjenester.
- Vurdere om flere EU-byggesteiner bør behandles som referanseressurser i registeret uten at de prioriteres for egne produktbeskrivelser med en gang.
- Vurdere om noen av EU-referanseressursene bør få korte oversiktsbeskrivelser i weben uten at de blir fullverdige produkt-canvas-filer.
- Gå gjennom avviksrapporten for XML mot kapabilitets- og prinsippgrunnlaget og avgjøre om flere beskrivelsestekster eller hjelpeelementer skal kurateres videre inn i repoet.
- Vurdere om weben også skal generere kapabilitets- og prinsippsammendrag direkte fra kuraterte filer i `arkitektur/`, slik at man unngår dobbelt vedlikehold av innledningstekster.
- Vurdere om weben også bør få en egen målside bygget fra `arkitektur/maal/maal.md`, slik at mål, prinsipper, kapabiliteter og ressurser kan leses i samme struktur.
- Vurdere om det senere trengs en egen kuratert koblingsfil mellom hovedkapabiliteter og strategiske mål, dersom målsporet skal brukes mer operativt i analyser og veiledning.
- Vurdere om kapabilitetssidene på web også skal hente prinsippreferanser direkte fra `principles.md`, slik at all prinsipplogikk ligger ett sted.
- Lage første produktbeskrivelser for de mest sentrale `SIKT`-ressursene, særlig Feide og Vitnemålsportalen.
- Kvalitetssikre de nye arbeidsutkastene for `EU`, særlig om de bør stå som egne ressurser i registeret eller omtales som referanseøkosystem rundt norske løsninger.
- Vurdere om `Altinn` som paraplyressurs skal beholdes med dagens stramme plattformkoblinger, eller deles tydeligere fra underliggende Digdir-løsninger i registeret.

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


