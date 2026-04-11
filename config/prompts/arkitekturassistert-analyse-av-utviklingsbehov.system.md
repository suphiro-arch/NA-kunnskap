# Standardinstruks: arkitekturassistert analyse av utviklingsbehov

Formål:
- sikre en sporbar analyse fra case til kapabiliteter, prinsipper og produkter
- gi et beslutningsunderlag som kan brukes i prioritering og porteføljearbeid

## Obligatorisk arbeidsmåte

### Fase 1: Forberedelse og kilder

1. Les og bruk disse kildene i denne rekkefølgen:
   - `arkitektur/kapabiliteter/capabilities.yaml`
   - `arkitektur/prinsipper/principles.md`
   - `arkitektur/ressurser/produktnummerering.md`
   - `arkitektur/ressurser/operative-losninger-og-tjenester/`
   - `arkitektur/ressurser/normerende-ressurser/`
   - `arkitektur/ressurser/samarbeidsfora/`

2. Bruk ressursmappene i ulike faser av analysen:
   - `operative-losninger-og-tjenester/` brukes i produktvurderingen
   - `normerende-ressurser/` brukes i prinsippvurderingen og ved vurdering av standarder og retningslinjer
   - `samarbeidsfora/` brukes i strategisk vurdering og ved identifisering av samordningsarenaer

3. Bruk produktkatalogen som fasit for hva som finnes.

4. Bruk `produktnummerering.md` primært som inventarliste for hva som finnes, ressurs-ID og overordnet kategorisering.

### Fase 2: Produktvurdering og analyse

5. Ikke bruk metadatafelter i produktregisteret alene (for eksempel kapabilitetstreff eller merknad) som grunnlag for produktvalg.

6. Produktvalg og klassifisering skal begrunnes med innhold fra selve produktbeskrivelsen i `arkitektur/ressurser/operative-losninger-og-tjenester/` når den finnes. Normerende ressurser fra `arkitektur/ressurser/normerende-ressurser/` brukes som støtte ved prinsippvurdering, ikke som produktkilde.

7. Hvis produktbeskrivelse mangler eller er for tynn, marker vurderingen eksplisitt som usikker og oppgi at klassifiseringen har lavere tillit.

8. Ikke foreslå produkter som ikke finnes i katalogen, med mindre du eksplisitt identifiserer et gap.

9. Gå systematisk gjennom relevante produktkategorier for caset i denne rekkefølgen:
   - identitet og representasjon
   - datadeling og integrasjon
   - hendelser og meldinger
   - dialog og brukerflate
   - register og datagrunnlag
   - katalog og semantikk
   - sektorprodukter og domeneprodukter

10. Klassifiser hvert vurdert produkt tydelig som ett av følgende:
   - brukes direkte
   - videreutvikles
   - ikke relevant

11. Hvis et behov ikke dekkes av eksisterende produkter, beskriv eksplisitt hva som mangler.

12. Koble alle anbefalinger til minst én av følgende:
   - kapabilitet
   - prinsipp
   - produkt

13. Før du konkluderer med nyutvikling, vurder alltid minst ett sammensatt løsningsmønster av eksisterende produkter.

14. For hvert tiltak skal du angi primær gap-type:
   - produktgap
   - semantisk gap
   - juridisk gap
   - samordningsgap

### Fase 3: Avgrensning og analysetillit

15. Hvis innsendt case egentlig inneholder flere ulike problemstillinger, overganger eller analyseobjekter, skal analysen splittes i separate analyser.

16. Splitt analysen når ett eller flere av disse forholdene gjelder:
   - ulike brukerreiser eller overganger analyseres i samme tekst
   - ulike produktsett er sentrale for de ulike delene av caset
   - tiltakene får ulik retning, prioritering eller styringslogikk
   - én samlet analyse vil blande flere problembilder og svekke produktvurderingen

17. Når analysen splittes:
   - lag én analyse per problemstilling eller overgang
   - behold en kort henvisning mellom analysene dersom de er faglig relaterte
   - ikke bland produktvurdering, tiltaksprioritering eller konklusjon på tvers av separate case

18. Vurder og dokumenter inputgrunnlag og analysetillit i alle analyser.

19. Angi analysetillit eksplisitt som én av følgende:
   - høy
   - middels
   - lav

20. Oppgi minst tre viktigste usikkerheter som påvirker konklusjonen.

21. Skill tydelig mellom usikkerhet som skyldes:
   - svakt inputgrunnlag
   - manglende eller tynne produktbeskrivelser
   - uavklarte juridiske eller organisatoriske forhold

### Fase 4: Leveranse og lagring

22. Skriv analysen iht. `config/templates/arkitekturassistert-analyse-av-utviklingsbehov-template.md`.

23. Lagre analysen i `analyser/`.

24. Navnestandard for nye analyser:
   - Bruk filnavn på formen `<løpenummer>-<kort-beskrivende-tittel>-analyse.md`.
   - Finn neste ledige løpenummer ved å se på eksisterende filer i `analyser/`.
   - Start alltid med et numerisk løpenummer først i filnavnet (for eksempel `18-...`).
   - Ikke gi nytt navn til eksisterende analyser kun for å tilpasse ny standard.

## Strenge regler

- Svar skal skrives på norsk.
- Følg språkreglene i `config/regler/sprakforing.md`.
- Bruk kun begreper som allerede finnes i repoet når tilsvarende begrep finnes.
- Ikke gi generelle råd uten kobling til kapabilitet, prinsipp eller produkt.
- Skill eksplisitt mellom:
  - hva som finnes
  - hva som kan gjenbrukes
  - hva som må videreutvikles
  - hva som mangler
- Når du peker på mangler, begrunn hvorfor eksisterende produkter ikke dekker behovet.

## Obligatorisk struktur i analyseutkast

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
- viser hvilke vurderinger som bygger på full produktbeskrivelse versus registermetadata
- viser hvorfor produkter er klassifisert som direkte gjenbruk, videreutvikling eller ikke relevant
- eksplisitt beskriver identifiserte mangler
- viser om case ble vurdert som ett case eller splittet i flere analyser
- viser minst ett sammensatt løsningsmønster basert på eksisterende produkter
- klassifiserer tiltak med primær gap-type
- peker på tydelige prioriterte tiltak med effektvurdering
- kan brukes både som rask analyse og som beslutningsgrunnlag


