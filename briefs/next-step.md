---
date: 2026-04-28
author: copilot
status: aktiv
topic: neste-steg
---

# Neste steg

## Foreslått neste prioritering

- `Matrikkelen` bør prioriteres videre som tversgående grunnlagsressurs for eiendom, adresser og bygninger, med tydelig verdi for planlegging, beredskap og samordning mellom nivåer.
- `Folkeregisteret` bør holdes høyt som sentral grunndataressurs med bred verdi i samhandling på tvers av sektorer og forvaltningsnivåer.
- `Helsedata.no` kan prioriteres videre som tversgående tilgangs- og oversiktsflate for data, men med bevisst skille mot rent sektorinterne helselsøsninger.
- `HPR` kan være aktuell når behovet gjelder autoritative opplysninger om helsepersonell på tvers av virksomheter og nivåer, men bør vurderes strengere enn de tre over.
- `Motorvognregisteret` er fortsatt relevant, men noe smalere enn `NVDB` som tversgående datagrunnlag og kan derfor ligge ett hakk lavere i prioriteringen.
- `Videokonsultasjon`, `Kjernejournal` og `e-resept` bør foreløpig ikke prioriteres opp som nye kandidater for NA-oversikten uten tydeligere verdi på tvers av sektorer.

## Mulige tidligere oversette kandidater

### Høy prioritet for ny vurdering

- `Grunnboken` bør vurderes som egen ressurs eller som tydeligere tvillingressurs til `Matrikkelen`, fordi kombinasjonen av eiendomsdata og tinglyste rettigheter har klar verdi på tvers i blant annet beredskap, sikkerhet, planlegging, kontroll og offentlig saksbehandling.
- `Register over reelle rettighetshavere` bør vurderes som ny kandidat fordi det gir et nasjonalt datagrunnlag om faktisk kontroll over virksomheter, med mulig verdi på tvers i kontroll, tilsyn, anskaffelser, økonomisk kriminalitet og samordnet offentlig oppfølging.

### Middels prioritet for ny vurdering

- `Norsk pasientregister (NPR)` bør vurderes videre, men med streng terskel. Registeret er viktig og nasjonalt, men tversgående verdi må begrunnes tydelig utover helsesektoren alene.
- `Kommunalt pasient- og brukerregister (KPR)` bør vurderes videre av samme grunn. Det kan være relevant for styring og samordning mellom nivåer, men er ikke automatisk en NA-ressurs uten klarere tversgående analyseverdi.
- `Sentralt stedsnavnregister` kan vurderes som mulig støttekandidat dersom vi senere ønsker å løfte flere geodataressurser som brukes bredt på tvers, men det ligger foreløpig bak `Geonorge`, `Matrikkelen`, `Grunnboken` og `NVDB`.

### Lav prioritet akkurat nå

- Flere helseinterne registre bør foreløpig ikke løftes videre bare fordi de er store eller viktige i egen sektor.
- Flere sektorinterne tjenester med svak eller indirekte dataverdi på tvers bør holdes utenfor listen inntil vi ser tydeligere casebehov.

---

## Hva gjenstår – Produktgrunnlag

**Kjerneprioriteter:**

- Fortsette revisjon av eldre produktbeskrivelser sektorvis etter samme metode som for KS- og Altinn-rundene.
- Ta stilling til om EU-kandidatene skal behandles som egne produktfiler eller fortsatt som referanseressurser.
- Følge opp kvaliteten i koblingene mellom produkter og kapabiliteter, særlig i eldre produktbeskrivelser der kapabilitetsseksjonen er svakere.
- Vurdere om de normerende Digdir-ressursene som fortsatt er på `v0` bør få utfylt analysefeltene (`Forpliktelsesnivå og etterlevelse`, `Typiske analyse- og beslutningssituasjoner`, `Konsekvens ved manglende bruk`) før neste større bolk legges inn.
- Vurdere om FHI-sektoren skal utvides med flere kandidater, f.eks. Norsk pasientregister (NPR) eller Kreftregisteret.

**Produktregisteret – konkrete valg som trengs:**

- Avklare om `FIKS IO` skal inn som egen ressurs, eller fortsatt behandles som teknisk komponent under `FIKS Melding`.
- Stramme inn `Fiks register`-beskrivelsen som overordnet registerfamilie nå som undertjenestene er ført som egne ressurskandidater.
- Vurdere om `DIGDIR-048 Rammeverk for innovasjon i offentlig sektor` skal stå som normerende ressurs, eller avgrenses tydeligere.

---

## Strategiske forbedringer – Arbeidsflyt og kvalitetssikring

### Evalueringsrubrikk i analysemalen
Neste forbedring som bør vurderes: legge inn en enkel evalueringsrubrikk i malen med score 1–5 for sporbarhet, gjenbrukbarhet, styringsrelevans og presisjon i produktvurdering.

### Modulær struktur for produktbeskrivelser
Nåværende produktbeskrivelser blander kilder, KI-analyse og publiserbar tekst i ett lag. Dette gjør det uklart hva som er verifisert kilde, hva som er arbeidsgrunnlag, og hva som skal publiseres.

**Forslag – tre-lags modell:**
1. **Kildegrunnlag og arkitekturnotater** – strukturerte kilder og masterdata fra `arkitektur/`
2. **Analyseblokker** – KI-utledet innhold som koblingsvurderinger og gjenbruksmuligheter
3. **Publiserbar tekst** – validert tekst for nett og arkitekturveiledning

**Praktisk gjennomføring:**
- Lag en annotasjonsstandard i produkt-canvas-prompten: `[Analyse]`, `[Kilde]`, `[Utledet fra X]`.
- Legg inn tydelig merking: «KI-støttet arbeidsgrunnlag – ikke faglig godkjent» inntil kvalitetssikring etableres.

---

## Bekjente blokkere og risiko

- Eldre produktbeskrivelser kan gi ujevn retrieval-kvalitet (må oppgraderes gradvis).
- Produktbeskrivelsene mangler tydelig merking av arbeidsgrunnlag vs. godkjent innhold (fikses med modulær struktur).
- Lokal Hugo-build er ikke verifisert fordi `hugo` ikke er installert i dette miljøet.

---

## Strukturelle forbedringer – Dagens repo

Kan gjøres parallelt, men er ikke kritisk for produktgrunnlag-arbeidet:

- Vurdere om `produktnummerering.md` bør omdøpes til `produktregister.md` når strukturen ellers er stabil.
- Vurdere om `sources/links.md` på sikt bør flyttes nærmere produktområdet.
- Vurdere om delressurser under `VIGO` bør beskrives som egne operative ressurser.
- Vurdere om neste sektorbolk etter Digdir og KS er EU-kandidater, nye nasjonale produkter eller ny revisjon av eldre beskrivelser.

---

## Assistenten på web – Planlegging og MVP (framtidig)

**Status:** Kun aktuelt hvis beslutning tas om å investere. Se [MVP-skisse](arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md) for detaljer.

**Blokkere:**
- Repoet har ingen eksplisitt lisens for dokumentasjonsinnholdet.
- Åpen internettflate krever moderering, rate limiting og tydelig avgrensning av datagrunnlag.
- Produktbeskrivelsene må ha høy og konsistent kvalitet før de brukes i retrieval.

**Neste steg hvis prosjekt startes:**
- Avklar lisens for dokumentasjonsinnholdet.
- Velg backend-plattform (foreslått: Azure Functions).
- Lag første backend-skjelett for `/api/ask` og første indeksjobb for repo-dokumentasjonen.
- Legg inn enkel chat-widget i Hugo-prototypen.
