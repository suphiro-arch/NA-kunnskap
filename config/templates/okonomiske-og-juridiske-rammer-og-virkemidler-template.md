# Mal for økonomiske og juridiske rammer og virkemidler (Markdown)

Bruk denne malen for ressurser som primært setter juridiske, økonomiske eller styringsmessige rammer for digital samhandling og gjennomføring.

Eksempler:
- forskrifter
- rundskriv
- finansieringsordninger
- styrings- og budsjettvirkemidler
- andre regulative eller økonomiske virkemidler

Se også:
- `arkitektur/ressurser/styringsregler.md`
- `sources/links.md`

## Arbeidsregel for v0.1
- behold hele malstrukturen også i tidlige versjoner
- fyll ut det som kan bekreftes
- skriv `Foreløpig ikke fylt ut i v0.1.` i felt som ennå ikke er gode nok
- bruk `Status/Livsfase` bare for status på selve virkemiddelet, ikke for status på dokumentet eller beskrivelsen

## Forventning til v1
- `v1` skal være egnet som direkte arbeidsgrunnlag i analyser, styringsvurderinger og prioriteringsarbeid, ikke bare som omtale.
- Følgende felt skal normalt være substansielt utfylt i `v1`:
  - `Kort beskrivelse`
  - `Formål og virkemiddelrolle`
  - `Forpliktelsesnivå og etterlevelse`
  - `Kapabiliteter`
  - `Målgruppe og berørte aktører`
  - `Virkemiddelmekanisme`
  - `Bruksområde`
  - `Typiske analyse- og beslutningssituasjoner`
  - `Økonomiske konsekvenser og insentiver`
  - `Juridiske konsekvenser og handlingsrom`
  - `Scope og avgrensning`
  - `Relasjon til andre ressurser`
  - `Forretningsverdi og arkitekturverdi`
  - `Lenke til dokumentasjon`
  - `Kildegrunnlag brukt i utfyllingen`
- Hvis flere av disse feltene fortsatt er for svake eller tomme, bør dokumentet normalt beholdes som `v0.x`.

## Kort v1-sjekkliste
- Er virkemiddelets rolle, binding og handlingsrom tydelig nok til direkte analysebruk?
- Er viktige påstander forankret i kilder, eller tydelig merket som deduksjon/usikkerhet?
- Er det tydelig hva som er juridisk krav, styringsforventning og anbefalt praksis?
- Er økonomiske virkninger, etterlevelseskonsekvenser og behov for supplement konkret beskrevet?
- Er kapabilitetslisten skrevet med rene, kanoniske kapabilitetsnavn?

## Navn
Det offisielle navnet på ressursen.

## Ressurs ID
Kanonisk ressurs-ID når dette er etablert.
Hvis egen ID ikke er etablert ennå, skriv `Ikke fastsatt ennå`.

## Ressurskategori
Økonomisk eller juridisk ramme og virkemiddel

## Type virkemiddel
For eksempel:
- forskrift
- rundskriv
- finansieringsordning
- tilskuddsordning
- styringsmekanisme

## Status/Livsfase
Beskriv status på ressursen, for eksempel:
- planlagt
- aktiv
- under revisjon
- erstattet
- under utfasing

Ikke bruk dette feltet til å beskrive modenhet eller dokumentstatus.

## Kort beskrivelse
Kort og selvstendig beskrivelse av hva ressursen er, hvordan den virker, og hvorfor den er viktig i arkitektur- og analysearbeid.

## Formål og virkemiddelrolle
Beskriv:
- hva ressursen skal oppnå
- hvilken type atferd, styring eller prioritering den skal påvirke
- om hovedrollen er juridisk, økonomisk, styringsmessig eller en kombinasjon

## Forpliktelsesnivå og etterlevelse
Beskriv eksplisitt:
- hvor bindende ressursen er i praksis
- hvem som forventes å følge den
- om avvik må begrunnes, godkjennes eller kan håndteres med skjønn
- hvordan etterlevelse normalt skjer, for eksempel gjennom styringsdialog, anskaffelser, tilsyn, budsjettprosesser eller porteføljestyring

## Kapabiliteter
Hvilke kapabiliteter i Nasjonal arkitektur støtter ressursen direkte?
Bruk bare kapabiliteter med tydelig og sterk kobling.
Bruk bare rene kapabilitetsnavn i listen. Legg forklaring i tilhørende tekst, ikke i selve navnelabelen.

## Målgruppe og berørte aktører
Beskriv bruker- og aktørbildet eksplisitt i segmenter.
Bruk gjerne tabell med:
`Aktørsegment | Primært behov | Bruksområde | Kommentar`

## Virkemiddelmekanisme
Beskriv hvordan ressursen faktisk påvirker prioriteringer, valg eller gjennomføring.

Aktuelle vinkler:
- juridisk plikt, hjemmel eller begrensning
- økonomisk insentiv, finansieringskrav eller prioriteringssignal
- styringskrav i portefølje, budsjett eller rapportering
- samspill mellom krav, anbefaling og veiledning

## Bruksområde
Beskriv når ressursen bør brukes i praksis.

Aktuelle vinkler:
- i hvilke typer analyser, styringsløp, anskaffelser eller prosjektfaser den er relevant
- hvilke avklaringer den bør utløse tidlig
- hvilke beslutninger den bør påvirke før detaljdesign

## Typiske analyse- og beslutningssituasjoner
Beskriv når ressursen er særlig viktig som beslutningsstøtte.

Aktuelle vinkler:
- tidligfase og konseptvalg
- porteføljeprioritering og styringsdialog
- anskaffelser og kravstilling
- vurdering av handlingsrom og avvik
- vurdering av tverrsektorielle konsekvenser

## Når ressursen normalt ikke er tilstrekkelig alene
Beskriv når ressursen må suppleres av andre styrende ressurser, veiledning eller gjenbrukbare løsninger.

## Økonomiske konsekvenser og insentiver
Beskriv hvordan ressursen påvirker:
- finansiering
- prioritering
- kostnads- og gevinstvurderinger
- insentiver for samordning og gjenbruk

## Juridiske konsekvenser og handlingsrom
Beskriv:
- hvilke juridiske rammer ressursen etablerer
- hva som er handlingsrom innenfor rammen
- hvilke typer avvik som er særlig risikable

## Scope og avgrensning
Beskriv konkret:
- hva ressursen omfatter
- hva den ikke omfatter
- hvor grensene går mot standarder, veiledere, fora og operative løsninger

## Forvaltningsmodell
Fordel på:
- faglig ansvar
- forvaltningsansvar
- endringsprosess
- publiserings- eller beslutningsarena

## Relasjon til andre ressurser
Beskriv relevante koblinger til:
- gjenbrukbare løsninger
- standarder og veiledning
- samhandlingsarenaer og organisering
- andre økonomiske og juridiske rammer og virkemidler

## Forretningsverdi og arkitekturverdi
Beskriv hvilken verdi ressursen gir for:
- tydeligere styring og prioritering
- mer forutsigbar etterlevelse
- samordning og gjenbruk
- lavere risiko ved tiltak som går på tvers av virksomheter

## Konsekvens ved manglende bruk eller avvik
Beskriv hva som typisk skjer hvis ressursen ikke brukes, brukes for sent eller tolkes ulikt.

Aktuelle vinkler:
- rettslig risiko
- svak styring og lavere måloppnåelse
- høyere kostnad ved omarbeiding
- fragmentering og svakere samhandling

## Utfordringer og risiko
Bruk gjerne tabell med:
`Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering`

Aktuelle kategorier:
- tolkning og praktisering
- styring og forankring
- endringshastighet
- samspill med andre virkemidler

## Publiseringsform og tilgjengelighet
Beskriv hvordan ressursen publiseres og brukes.

For eksempel:
- Lovdata
- rundskrivspublisering på regjeringen.no
- veiledningssider
- styringsdokumenter i virksomheter

## Støtter arkitekturprinsipper
Beskriv hvordan ressursen støtter prinsippene i `arkitektur/prinsipper/principles.md`.

Vurder også om det finnes tydelige svakheter, spenninger eller begrensninger knyttet til viktige prinsipper som bør tas med i analyse ved mulig bruk.

Aktuelle vinkler:
- prinsipper ressursen støtter tydelig
- prinsipper ressursen bare støtter delvis
- prinsipper der ressursen kan gi friksjon, treghet eller økt kompleksitet
- hva dette betyr for vurdering av bruk i konkrete case

## Lenke til dokumentasjon
Oppgi hovedlenker til dokumentasjon, eventuelle prosjektsider, publiseringsflater og relevante støttekilder.

## Kildegrunnlag brukt i utfyllingen
Oppgi konkrete URL-er og lokale filer, med hentedato der det er relevant.