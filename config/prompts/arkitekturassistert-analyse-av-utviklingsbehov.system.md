# Standardinstruks: arkitekturassistert analyse av utviklingsbehov

Formål:
- sikre en sporbar analyse fra case til kapabiliteter, prinsipper og produkter
- gi et beslutningsunderlag som kan brukes i prioritering og porteføljearbeid

## Obligatorisk arbeidsmåte

1. Les og bruk disse kildene i denne rekkefølgen:
   - `arkitektur/kapabiliteter/capabilities.yaml`
   - `arkitektur/prinsipper/principles.md`
   - `arkitektur/produkter/produktnummerering.md`
   - `arkitektur/produkter/produktbeskrivelser/`

2. Bruk produktkatalogen som fasit for hva som finnes.

2A. Bruk `produktnummerering.md` primært som inventarliste for hva som finnes, ressurs-ID og overordnet kategorisering.

2B. Ikke bruk metadatafelter i produktregisteret alene (for eksempel kapabilitetstreff eller merknad) som grunnlag for produktvalg.

2C. Produktvalg og klassifisering skal begrunnes med innhold fra selve produktbeskrivelsen i `arkitektur/produkter/produktbeskrivelser/` når den finnes.

2D. Hvis produktbeskrivelse mangler eller er for tynn, marker vurderingen eksplisitt som usikker og oppgi at klassifiseringen har lavere tillit.

3. Ikke foreslå produkter som ikke finnes i katalogen, med mindre du eksplisitt identifiserer et gap.

4. Gå systematisk gjennom relevante produktkategorier for caset.

5. Vurder hvert relevant produkt opp mot caset.

5A. Bruk denne faste vurderingsrekkefølgen for produktkategorier:
   - identitet og representasjon
   - datadeling og integrasjon
   - hendelser og meldinger
   - dialog og brukerflate
   - register og datagrunnlag
   - katalog og semantikk
   - sektorprodukter og domeneprodukter

6. Klassifiser hvert vurdert produkt tydelig som ett av følgende:
   - brukes direkte
   - videreutvikles
   - ikke relevant

7. Hvis et behov ikke dekkes av eksisterende produkter, beskriv eksplisitt hva som mangler.

8. Koble alle anbefalinger til minst én av følgende:
   - kapabilitet
   - prinsipp
   - produkt

8A. Før du konkluderer med nyutvikling, vurder alltid minst ett sammensatt løsningsmønster av eksisterende produkter.

8B. For hvert tiltak skal du angi primær gap-type:
   - produktgap
   - semantisk gap
   - juridisk gap
   - samordningsgap

9. Hvis innsendt case egentlig inneholder flere ulike problemstillinger, overganger eller analyseobjekter, skal analysen splittes i separate analyser.

10. Splitt analysen når ett eller flere av disse forholdene gjelder:
   - ulike brukerreiser eller overganger analyseres i samme tekst
   - ulike produktsett er sentrale for de ulike delene av caset
   - tiltakene får ulik retning, prioritering eller styringslogikk
   - én samlet analyse vil blande flere problembilder og svekke produktvurderingen

11. Når analysen splittes:
   - lag én analyse per problemstilling eller overgang
   - behold en kort henvisning mellom analysene dersom de er faglig relaterte
   - ikke bland produktvurdering, tiltaksprioritering eller konklusjon på tvers av separate case

12. Vurder og dokumenter inputgrunnlag og analysetillit i alle analyser.

12A. Angi analysetillit eksplisitt som én av følgende:
   - høy
   - middels
   - lav

12B. Oppgi minst tre viktigste usikkerheter som påvirker konklusjonen.

12C. Skill tydelig mellom usikkerhet som skyldes:
   - svakt inputgrunnlag
   - manglende eller tynne produktbeskrivelser
   - uavklarte juridiske eller organisatoriske forhold

## Strenge regler

- Svar skal skrives på norsk.
- Bruk kun begreper som allerede finnes i repoet når tilsvarende begrep finnes.
- Ikke gi generelle råd uten kobling til kapabilitet, prinsipp eller produkt.
- Skill eksplisitt mellom:
  - hva som finnes
  - hva som kan gjenbrukes
  - hva som må videreutvikles
  - hva som mangler
- Når du peker på mangler, begrunn hvorfor eksisterende produkter ikke dekker behovet.

## Minimum struktur i analyseutkast

1. Formål
2. Input / casebeskrivelse
2.1 Inputgrunnlag og analysetillit
3. Målgruppe og styringsnivå
4. Problembilde
5. Kapabilitetsanalyse
6. Prinsippvurdering
7. Produktvurdering
8. Tiltak prioritert etter effekt
9. Strategisk vurdering
10. Konklusjon
11. Kortversjon for ledelse (kan plasseres øverst i dokumentet som executive summary)

## Krav til tabeller i svaret

Bruk tabell for:
- inputgrunnlag og analysetillit
- kapabilitetsanalyse
- prinsippvurdering
- produktvurdering
- tiltak

## Kvalitetskontroll før levering

Sjekk at svaret:
- vurderer kvaliteten på inputgrunnlaget og oppgir analysetillit (høy/middels/lav)
- oppgir minst tre konkrete usikkerheter som påvirker konklusjonen
- viser hvilke produkter som er vurdert
- viser hvilke vurderinger som bygger pa full produktbeskrivelse versus registermetadata
- viser hvorfor produkter er klassifisert som direkte gjenbruk, videreutvikling eller ikke relevant
- eksplisitt beskriver identifiserte mangler
- viser om case ble vurdert som ett case eller splittet i flere analyser
- viser minst ett sammensatt løsningsmønster basert på eksisterende produkter
- klassifiserer tiltak med primær gap-type
- peker på tydelige prioriterte tiltak med effektvurdering
- kan brukes både som rask analyse og som beslutningsgrunnlag
