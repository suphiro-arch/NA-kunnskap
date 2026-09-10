# Gjenbrukbar løsning-canvas mal (Markdown)

Kilde: konvertert fra `sources/Mal - Produkt canvas.docx`.

## Minstekrav for v1
- `Hovedfunksjoner` bør normalt ha minst 3-4 forklarende avsnitt.
- `Hovedfunksjoner` bør inkludere:
	- `Typiske brukssituasjoner (generisk)`
	- `Når <produktet> normalt ikke er førstevalg`
- `Kapabiliteter` bør forklares med hvordan produktet bidrar per kapabilitet (ikke bare opplisting).
- `Forretningsverdi/Verdiforslag` bør beskrive verdi for minst 3 målgrupper/interessenter.
- `Gjenbruk` bør inkludere `Vanlige kombinasjoner med andre produkter` når relevant.

Hvis kildegrunnlaget ikke er godt nok for dette nivået, behold dokumentet som `v0.x`.

## Merking av fakta, deduksjon og usikkerhet
Skill aktivt mellom det som er bekreftet og det som er tolket. Bruk disse merkene som delfelt i
teksten, ikke som egne overskrifter:

- `**Fakta:**` — bekreftet i åpne kilder eller i repoets egne kilder. Oppgi hvem som sier det.
- `**Deduksjon:**` — rimelig tolkning ut fra kjent kontekst. Skal kunne etterprøves av leseren, og
  skal ikke framstilles som bekreftet.
- `**Ikke offentlig dokumentert i denne arbeidsøkten:**` — forhold som ikke ble funnet i kildene.
  Si hva som mangler, ikke bare at noe mangler.

Merkene brukes særlig i `Status/Livsfase`, `Modenhet`, `Veikart over kommende funksjonalitet`,
`Plattform` og `Forvaltning/eier`, der kildene ofte er ufullstendige. Usikkerhet er ikke en grunn til å
hoppe over en seksjon: skriv det som er kjent, og merk resten.

### Aksepterte seksjoner utenfor feltlista
Noen seksjoner er i utstrakt bruk uten å stå i feltlista under. De er godtatt av
`tools/check-resource-structure.py`, og skal skrives med disse navnene:

- `Endringer fra forrige versjon` — obligatorisk i revisjoner, utelates i `v1`. Bruk dette navnet
  uten versjonsnummer i parentes. `Endringer i denne revisjonen` finnes i noen eldre filer, men
  skal ikke brukes i nye.
- `Scope og avgrensning` — malen har denne som underseksjon av `Hovedfunksjoner`. Atten gjeldende
  filer har løftet den til egen seksjon, og begge plasseringer er godtatt. Velg én per fil.


## Navn
Det offisielle navnet på produktet eller løsningen.

H1-tittelen øverst i fila er den korte visningstittelen, og skal følge filnavnet. Dette feltet er
det offisielle navnet. De to kan avvike når det offisielle navnet er langt: `# BASIL` med
`## Navn` satt til `BASIL — Barnehage-Statistikk-InnrapporteringsLøsning` er riktig bruk, ikke et
avvik som skal rettes.

## Ressurs ID
Kanonisk ressurs-ID fra `arkitektur/ressurser/produktnummerering.md`, for eksempel `DIGDIR-001`.
Ikke bruk bare internt løpenummer i dette feltet.

## Status/Livsfase
Planlagt / Under utvikling / Pilot / Produksjon / Utfasing

Skriv statusen først, i fet skrift, med en kort begrunnelse på samme linje. Følg opp med et
`**Fakta:**`-avsnitt som viser hva statusen bygger på. Er statusen ikke eksplisitt dokumentert,
utled den og merk avsnittet `**Deduksjon:**`.

## Modenhet
Teknisk tilstand, teknologisk stabilitet og brukermodenhet.
Vurder teknisk, organisatorisk, markedsmessig og regulatorisk modenhet.

Skriv en samlet vurdering først, i fet skrift, og bygg den opp med punkter som hver kan spores til
en kilde. Avslutt med et `**Deduksjon:**`-avsnitt som sier hva modenheten faktisk betyr for den som
vurderer bruk, inkludert det svakeste leddet. En modenhetsvurdering uten et svakt punkt er sjelden
etterprøvbar.

## Kort beskrivelse
Kort om produktet sett fra et forretningsperspektiv.
Skriv som en selvstendig beskrivelse for målgruppen, ikke som referat av hva en nettside eller kilde sier.
Bruk eventuell `Merknad` fra `arkitektur/ressurser/produktnummerering.md` som en kort standard presisering eller avgrensning tidlig i teksten.

## Kapabiliteter
Hvilke kapabiliteter i Nasjonal arkitektur bidrar produktet til å realisere eller forbedre?
Bruk formatet:
`- **Kapabilitet**` etterfulgt av forklaring i vanlig skrift.
Ta bare med kapabiliteter med sterk, direkte kobling til produktets egen funksjon.

## Produktmål
Strategiske og operative mål. Hva skal produktet oppnå?

Skill mellom dokumenterte mål og mål som er utledet av kildene, og merk hvilke som er hva. Det gjør
det mulig for leseren å se hva forvalteren selv har sagt, og hva som er vår tolkning.

## Brukerbehov
Hvilket problem eller behov løser produktet?

## Hvem er brukerne og brukersegmentene
Beskriv brukerbildet eksplisitt i segmenter.
Bruk som hovedregel en tabell med kolonnene:
`Brukersegment | Primære behov | Bruksområde | Kommentar`
Ta med både primærbrukere, sekundærbrukere og forvaltnings-/støttemiljø når det er relevant.

## Hovedfunksjoner
Viktigste funksjoner og nøkkelfunksjoner.
Beskriv de operative hovedfunksjonene først.
For produkter der det er relevant for valg og fravalg i analyser, legg deretter inn egne underseksjoner for:
- `Typiske brukssituasjoner (generisk)`
- `Når <produktet> normalt ikke er førstevalg`
Disse feltene er beslutningsstøtte og skal hjelpe leseren å forstå når produktet bør velges, og når andre produkter eller løsningsmønstre er mer relevante.
Disse feltene skal ikke i seg selv utvide produktets scope eller føre til nye kapabiliteter uten at dette er forankret i produktets faktiske funksjonelle rolle.

### Scope og avgrensning
Hva inngår og hva inngår ikke.

## Veikart over kommende funksjonalitet
Beskrivelse av kjent eller antatt veikart.

## Forretningsverdi/Verdiforslag
Forretnings- og samfunnsverdi, inkludert brukeropplevd verdi.

## Utfordringer og risiko
Juridisk, teknisk, sikkerhet, leverandør- og brukerrisiko.

Bruk tabell med kolonnene `Område | Risiko | Håndtering eller observasjon`. Vær konkret: en risiko
som «integrasjonsrisiko» uten innhold er ikke beslutningsstøtte. Skriv `Uavklart` eller
`Ikke offentlig dokumentert i denne arbeidsøkten` i håndteringskolonnen framfor å oppgi et tiltak
kildene ikke viser.

## Kanaler
Leveransekanaler og tilgjengelighet.
Ta med om kanalen krever innlogging, hvilken påloggingsmekanisme som brukes, og om det finnes en
maskinell kanal ved siden av brukerflaten.

## Plattform
Sky (lokasjon), on-prem eller hybrid.
Er dette ikke dokumentert i kildene, skriv `Ikke offentlig dokumentert i denne arbeidsøkten` og si
hva som faktisk er kjent. Ikke utled skyleverandør eller driftsmodell fra indisier.

## Gjenbruk
Vurder gjenbruksvennlighet av API-er, standarder og lisensiering.
Legg inn `Vanlige kombinasjoner med andre produkter` når dette gjør produktet lettere å bruke i arkitekturvurderinger.

Avslutt seksjonen med kildekodefeltene under, i denne rekkefølgen og etter
`Vanlige kombinasjoner med andre produkter`. De er merkede delfelt i `Gjenbruk`, ikke egne
overskrifter, slik at de kan leses maskinelt uten å bli påkrevde seksjoner i hele kategorien.

**Kildekode:** Status for kildekoden. Bruk én av verdiene `Åpen kildekode`, `Proprietær` eller
`Ikke offentlig dokumentert`, og skriv den først i feltet. Er statusen ukjent, skriv
`Ikke offentlig dokumentert` — ikke gjett.

**Lisens:** Vilkårene koden er gjort tilgjengelig under. Bruk SPDX-identifikatoren når lisensen er
kjent, for eksempel `MIT`, `Apache-2.0` eller `EUPL-1.2`. Skriv `Ikke relevant` når kildekoden er
proprietær, og `Ikke offentlig dokumentert` når lisensen ikke er oppgitt eller ikke er funnet.
Kontroller lisensen mot repositoriet selv, ikke mot omtale i tredjepartskilder.

**Repositorium:** Lenke til repositoriet ved åpen kildekode. Utelates når kildekoden ikke er åpen.

`Kildekode` og `Lisens` skal alltid være utfylt, og de er uavhengige av hverandre. `Åpen kildekode`
sammen med `Ikke offentlig dokumentert` som lisens er et gyldig og meningsbærende funn: koden er
publisert, men vilkårene er ikke oppgitt, og den kan derfor ikke trygt gjenbrukes.

## Støtter arkitekturprinsipper
I hvilken grad støttes nasjonale arkitekturprinsipper?
Bruk `arkitektur/prinsipper/principles.md` som kilde for prinsippnavn og koblinger.

Skriv `- **PN: Prinsippnavn**` med forklaringen i vanlig skrift under, og si hvordan produktet
faktisk støtter prinsippet. Bruk `Støttes delvis` når koblingen er reell men begrenset.

Avslutt seksjonen med et avsnitt om spenning og begrensning: hvilke prinsipper produktet står i
strid med eller bare delvis oppfyller, og hvorfor. Dette er den delen av seksjonen som gir mest
beslutningsstøtte, og den skal ikke utelates fordi produktet framstår velfungerende.

## Finansiering
Type finansiering for utvikling og drift.
Skill mellom finansiering av utvikling og av drift når kildene gjør det, og mellom
bevilgningsfinansiering, brukerbetaling og tjenesteeierfinansiering. Er modellen ikke dokumentert,
skriv det framfor å beskrive den generelt.

## Forvaltning/eier
Del opp i produktansvar, driftsansvar, budsjettansvar og styringsmodell.

Bruk tabell med kolonnene `Ansvarsområde | Organisasjon / vurdering | Grunnlag`. Grunnlagskolonnen
skal si hvor opplysningen kommer fra, slik at en leser kan etterprøve ansvarsfordelingen. Er et
ansvar ukjent, ta raden med og skriv `Ikke offentlig dokumentert i denne arbeidsøkten` framfor å
utelate raden.

## Lenke til dokumentasjon
Hoveddokumentasjon, kom i gang, vilkår/pris (om relevant), status/drift.

## Kildegrunnlag brukt i utfyllingen
Oppgi konkrete URL-er og lokale filer.
