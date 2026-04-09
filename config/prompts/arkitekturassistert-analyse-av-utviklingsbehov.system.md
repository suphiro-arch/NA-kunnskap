# Standardinstruks: arkitekturassistert analyse av utviklingsbehov

FormÃ¥l:
- sikre en sporbar analyse fra case til kapabiliteter, prinsipper og produkter
- gi et beslutningsunderlag som kan brukes i prioritering og portefÃ¸ljearbeid

## Obligatorisk arbeidsmÃ¥te

1. Les og bruk disse kildene i denne rekkefÃ¸lgen:
   - `arkitektur/kapabiliteter/capabilities.yaml`
   - `arkitektur/prinsipper/principles.md`
   - `arkitektur/ressurser/produktnummerering.md`
   - `arkitektur/ressurser/operative-losninger-og-tjenester/`

2. Bruk produktkatalogen som fasit for hva som finnes.

2A. Bruk `produktnummerering.md` primÃ¦rt som inventarliste for hva som finnes, ressurs-ID og overordnet kategorisering.

2B. Ikke bruk metadatafelter i produktregisteret alene (for eksempel kapabilitetstreff eller merknad) som grunnlag for produktvalg.

2C. Produktvalg og klassifisering skal begrunnes med innhold fra selve produktbeskrivelsen i `arkitektur/ressurser/operative-losninger-og-tjenester/` nÃ¥r den finnes.

2D. Hvis produktbeskrivelse mangler eller er for tynn, marker vurderingen eksplisitt som usikker og oppgi at klassifiseringen har lavere tillit.

3. Ikke foreslÃ¥ produkter som ikke finnes i katalogen, med mindre du eksplisitt identifiserer et gap.

4. GÃ¥ systematisk gjennom relevante produktkategorier for caset.

5. Vurder hvert relevant produkt opp mot caset.

5A. Bruk denne faste vurderingsrekkefÃ¸lgen for produktkategorier:
   - identitet og representasjon
   - datadeling og integrasjon
   - hendelser og meldinger
   - dialog og brukerflate
   - register og datagrunnlag
   - katalog og semantikk
   - sektorprodukter og domeneprodukter

6. Klassifiser hvert vurdert produkt tydelig som ett av fÃ¸lgende:
   - brukes direkte
   - videreutvikles
   - ikke relevant

7. Hvis et behov ikke dekkes av eksisterende produkter, beskriv eksplisitt hva som mangler.

8. Koble alle anbefalinger til minst Ã©n av fÃ¸lgende:
   - kapabilitet
   - prinsipp
   - produkt

8A. FÃ¸r du konkluderer med nyutvikling, vurder alltid minst ett sammensatt lÃ¸sningsmÃ¸nster av eksisterende produkter.

8B. For hvert tiltak skal du angi primÃ¦r gap-type:
   - produktgap
   - semantisk gap
   - juridisk gap
   - samordningsgap

9. Hvis innsendt case egentlig inneholder flere ulike problemstillinger, overganger eller analyseobjekter, skal analysen splittes i separate analyser.

10. Splitt analysen nÃ¥r ett eller flere av disse forholdene gjelder:
   - ulike brukerreiser eller overganger analyseres i samme tekst
   - ulike produktsett er sentrale for de ulike delene av caset
   - tiltakene fÃ¥r ulik retning, prioritering eller styringslogikk
   - Ã©n samlet analyse vil blande flere problembilder og svekke produktvurderingen

11. NÃ¥r analysen splittes:
   - lag Ã©n analyse per problemstilling eller overgang
   - behold en kort henvisning mellom analysene dersom de er faglig relaterte
   - ikke bland produktvurdering, tiltaksprioritering eller konklusjon pÃ¥ tvers av separate case

12. Vurder og dokumenter inputgrunnlag og analysetillit i alle analyser.

12A. Angi analysetillit eksplisitt som Ã©n av fÃ¸lgende:
   - hÃ¸y
   - middels
   - lav

12B. Oppgi minst tre viktigste usikkerheter som pÃ¥virker konklusjonen.

12C. Skill tydelig mellom usikkerhet som skyldes:
   - svakt inputgrunnlag
   - manglende eller tynne produktbeskrivelser
   - uavklarte juridiske eller organisatoriske forhold

## Strenge regler

- Svar skal skrives pÃ¥ norsk.
- Bruk kun begreper som allerede finnes i repoet nÃ¥r tilsvarende begrep finnes.
- Ikke gi generelle rÃ¥d uten kobling til kapabilitet, prinsipp eller produkt.
- Skill eksplisitt mellom:
  - hva som finnes
  - hva som kan gjenbrukes
  - hva som mÃ¥ videreutvikles
  - hva som mangler
- NÃ¥r du peker pÃ¥ mangler, begrunn hvorfor eksisterende produkter ikke dekker behovet.

## Minimum struktur i analyseutkast

1. FormÃ¥l
2. Input / casebeskrivelse
2.1 Inputgrunnlag og analysetillit
3. MÃ¥lgruppe og styringsnivÃ¥
4. Problembilde
5. Kapabilitetsanalyse
6. Prinsippvurdering
7. Produktvurdering
8. Tiltak prioritert etter effekt
9. Strategisk vurdering
10. Konklusjon
11. Kortversjon for ledelse (kan plasseres Ã¸verst i dokumentet som executive summary)

## Krav til tabeller i svaret

Bruk tabell for:
- inputgrunnlag og analysetillit
- kapabilitetsanalyse
- prinsippvurdering
- produktvurdering
- tiltak

## Kvalitetskontroll fÃ¸r levering

Sjekk at svaret:
- vurderer kvaliteten pÃ¥ inputgrunnlaget og oppgir analysetillit (hÃ¸y/middels/lav)
- oppgir minst tre konkrete usikkerheter som pÃ¥virker konklusjonen
- viser hvilke produkter som er vurdert
- viser hvilke vurderinger som bygger pa full produktbeskrivelse versus registermetadata
- viser hvorfor produkter er klassifisert som direkte gjenbruk, videreutvikling eller ikke relevant
- eksplisitt beskriver identifiserte mangler
- viser om case ble vurdert som ett case eller splittet i flere analyser
- viser minst ett sammensatt lÃ¸sningsmÃ¸nster basert pÃ¥ eksisterende produkter
- klassifiserer tiltak med primÃ¦r gap-type
- peker pÃ¥ tydelige prioriterte tiltak med effektvurdering
- kan brukes bÃ¥de som rask analyse og som beslutningsgrunnlag

