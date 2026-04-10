# Mal for normerende ressurs (Markdown)

Bruk denne malen for ressurser som primært gir føringer for hvordan løsninger skal forstås, beskrives, utformes eller samordnes.

Eksempler:
- informasjonsmodeller
- begrepsmodeller
- standarder
- veiledere
- referansearkitektur

Se også:
- `arkitektur/ressurser/styringsregler.md`
- `sources/links.md`

## Arbeidsregel for v0.1
- behold hele malstrukturen også i tidlige versjoner
- fyll ut det som kan bekreftes
- skriv `Foreløpig ikke fylt ut i v0.1.` i felt som ennå ikke er gode nok
- bruk `Status/Livsfase` bare for status på selve ressursen, ikke for status på dokumentet eller beskrivelsen

## Forventning til v1
- `v1` skal være egnet som direkte arbeidsgrunnlag i analyser, ikke bare som notat.
- Følgende felt skal normalt være substansielt utfylt i `v1`:
  - `Kort beskrivelse`
  - `Formål og normerende rolle`
  - `Forpliktelsesnivå og etterlevelse`
  - `Kapabiliteter`
  - `Målgruppe og brukere`
  - `Normerende innhold`
  - `Bruksområde`
  - `Typiske analyse- og beslutningssituasjoner`
  - `Scope og avgrensning`
  - `Relasjon til andre ressurser`
  - `Forretningsverdi og arkitekturverdi`
  - `Lenke til dokumentasjon`
  - `Kildegrunnlag brukt i utfyllingen`
- Hvis flere av disse feltene fortsatt er for svake eller tomme, bør dokumentet normalt beholdes som `v0.x`.

## Navn
Det offisielle navnet på den normerende ressursen.

## Ressurs ID
Kanonisk ressurs-ID når dette er etablert.
Hvis egen ID ikke er etablert ennå, skriv `Ikke fastsatt ennå`.

## Ressurskategori
Normerende ressurs

## Type normerende ressurs
For eksempel:
- informasjonsmodell
- begrepsmodell
- standard
- veileder
- referansearkitektur

## Status/Livsfase
Beskriv status på ressursen, for eksempel:
- planlagt
- under utvikling
- aktiv
- under revisjon
- under utfasing

Ikke bruk dette feltet til å beskrive modenhet eller dokumentstatus.

## Kort beskrivelse
Kort og selvstendig beskrivelse av hva ressursen er, hva den brukes til, og hvorfor den er viktig i arkitektur- og analysearbeid.

## Formål og normerende rolle
Beskriv:
- hva ressursen skal skape av felles forståelse eller styring
- hvilke valg, modeller eller arbeidsmåter den er ment å påvirke
- om den er anbefalt, styrende, obligatorisk eller veiledende

## Forpliktelsesnivå og etterlevelse
Beskriv eksplisitt:
- hvor bindende ressursen er i praksis
- hvem som forventes å følge den
- om avvik må begrunnes, godkjennes eller bare vurderes
- hvordan etterlevelse normalt skjer, for eksempel gjennom styring, arkitekturarbeid, anskaffelser eller faglig veiledning

## Kapabiliteter
Hvilke kapabiliteter i Nasjonal arkitektur støtter ressursen direkte?
Bruk bare kapabiliteter med tydelig og sterk kobling.

## Målgruppe og brukere
Beskriv brukerbildet eksplisitt i segmenter.
Bruk gjerne tabell med:
`Brukersegment | Primært behov | Bruksområde | Kommentar`

## Normerende innhold
Beskriv hva ressursen faktisk inneholder og strukturerer.

Aktuelle vinkler:
- sentrale begreper eller modellobjekter
- anbefalte mønstre eller prinsipper
- avgrensninger og definisjoner
- hva som standardiseres eller harmoniseres

## Bruksområde
Beskriv når ressursen bør brukes i praksis.

Aktuelle vinkler:
- i hvilke typer analyser, prosjekter eller løsningsløp den er relevant
- hvilke problemer den hjelper med å løse
- hvilke avklaringer den støtter

## Typiske analyse- og beslutningssituasjoner
Beskriv når ressursen er særlig viktig som beslutningsstøtte.

Aktuelle vinkler:
- tidligfase og konseptvalg
- utforming av målbilde eller referansearkitektur
- anskaffelser og kravstilling
- samordning på tvers av virksomheter
- vurdering av om eksisterende løsninger og data kan gjenbrukes

## Når ressursen normalt ikke er tilstrekkelig alene
Beskriv når ressursen må suppleres av andre styrende eller operative ressurser.

## Scope og avgrensning
Beskriv konkret:
- hva ressursen omfatter
- hva den ikke omfatter
- hvor grensene går mot tilgrensende modeller, veiledere, standarder eller løsninger

## Forvaltningsmodell
Fordel på:
- faglig ansvar
- forvaltningsansvar
- endringsprosess
- publiserings- eller beslutningsarena

## Relasjon til andre ressurser
Beskriv relevante koblinger til:
- operative løsninger og tjenester
- andre normerende ressurser
- samarbeidsfora

## Forretningsverdi og arkitekturverdi
Beskriv hvilken verdi ressursen gir for:
- felles forståelse
- samordning
- sammenlignbarhet
- gjenbruk
- lavere tolkningsrom og mindre fragmentering

## Konsekvens ved manglende bruk eller avvik
Beskriv hva som typisk skjer hvis ressursen ikke brukes, brukes for sent eller tolkes ulikt.

Aktuelle vinkler:
- økt tolkningsrom
- svakere samordning
- høyere integrasjonskostnad
- større risiko i anskaffelser eller gjennomføring
- vanskeligere sammenlignbarhet på tvers

## Utfordringer og risiko
Bruk gjerne tabell med:
`Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering`

Aktuelle kategorier:
- forankring
- semantisk kvalitet
- endringsstyring
- adopsjon
- sammenheng med operative løsninger

## Publiseringsform og tilgjengelighet
Beskriv hvordan ressursen publiseres og brukes.

For eksempel:
- nettside
- dokumentasjonsside
- modellverktøy
- repository
- prosjekt- eller samarbeidsflate

## Støtter arkitekturprinsipper
Beskriv hvordan ressursen støtter prinsippene i `arkitektur/prinsipper/principles.md`.

Vurder også om det finnes tydelige svakheter, spenninger eller begrensninger knyttet til viktige prinsipper som bør tas med i analyse ved mulig bruk.

Aktuelle vinkler:
- prinsipper ressursen støtter tydelig
- prinsipper ressursen bare støtter delvis
- prinsipper der ressursen kan skape avhengighet, friksjon eller økt kompleksitet
- hva dette betyr for vurdering av bruk i konkrete case

## Lenke til dokumentasjon
Oppgi hovedlenker til dokumentasjon, eventuelle prosjektsider, publiseringsflater og relevante støttekilder.

## Kildegrunnlag brukt i utfyllingen
Oppgi konkrete URL-er og lokale filer, med hentedato der det er relevant.
