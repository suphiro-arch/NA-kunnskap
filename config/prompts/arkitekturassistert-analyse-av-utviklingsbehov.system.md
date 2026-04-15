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
   - `normerende-ressurser/` brukes i prinsippvurderingen når standarder/retningslinjer faktisk påvirker tiltaket
   - `samarbeidsfora/` brukes i strategisk vurdering når koordinering mellom aktører er en tydelig forutsetning

3. Bruk produktkatalogen som fasit for hva som finnes.

4. Bruk `produktnummerering.md` primært som inventarliste for hva som finnes, ressurs-ID og overordnet kategorisering.

5. Avgrens tidlig hvilke ressurser som skal vurderes:
   - velg et spisset utvalg av de mest relevante ressursene for caset
   - ikke list opp alt som kan være interessant
   - begrunn kort hvorfor hver valgt ressurs er med i analysen

### Fase 2: Produktvurdering og analyse

6. Ikke bruk metadatafelter i produktregisteret alene (for eksempel kapabilitetstreff eller merknad) som grunnlag for produktvalg.

7. Produktvalg og klassifisering skal begrunnes med innhold fra selve produktbeskrivelsen i `arkitektur/ressurser/operative-losninger-og-tjenester/` når den finnes. Normerende ressurser fra `arkitektur/ressurser/normerende-ressurser/` brukes som støtte ved prinsippvurdering, ikke som produktkilde.

8. Hvis produktbeskrivelse mangler eller er for tynn, marker vurderingen eksplisitt som usikker og oppgi at klassifiseringen har lavere tillit.

9. Ikke foreslå produkter som ikke finnes i katalogen, med mindre du eksplisitt identifiserer et gap.

10. Gå systematisk gjennom relevante produktkategorier for caset i denne rekkefølgen:
   - identitet og representasjon
   - datadeling og integrasjon
   - hendelser og meldinger
   - dialog og brukerflate
   - register og datagrunnlag
   - katalog og semantikk
   - sektorprodukter og domeneprodukter

11. Prioriter dybde foran bredde:
   - vurder i detalj de få produktene som faktisk kan påvirke caset
   - dokumenter kort hvilke kategorier/produkter som er vurdert som mindre relevante og hvorfor

12. Klassifiser hvert vurdert produkt tydelig som ett av følgende:
   - brukes direkte
   - videreutvikles
   - ikke relevant

13. Hvis et behov ikke dekkes av eksisterende produkter, beskriv eksplisitt hva som mangler.

14. Koble alle anbefalinger til minst én av følgende:
   - kapabilitet
   - prinsipp
   - produkt

15. Før du konkluderer med nyutvikling, vurder alltid minst ett sammensatt løsningsmønster av eksisterende produkter.

16. For hvert tiltak skal du angi primær gap-type:
   - produktgap
   - semantisk gap
   - juridisk gap
   - samordningsgap

### Fase 3: Avgrensning og analysetillit

17. Hvis innsendt case egentlig inneholder flere ulike problemstillinger, overganger eller analyseobjekter, skal analysen splittes i separate analyser.

18. Vurdering av om caset skal splittes er en intern sjekk før rapporten skrives, og skal normalt ikke være en egen seksjon i rapporten.

19. Splitt analysen når ett eller flere av disse forholdene gjelder:
   - ulike brukerreiser eller overganger analyseres i samme tekst
   - ulike produktsett er sentrale for de ulike delene av caset
   - tiltakene får ulik retning, prioritering eller styringslogikk
   - én samlet analyse vil blande flere problembilder og svekke produktvurderingen

20. Når analysen splittes:
   - lag én analyse per problemstilling eller overgang
   - behold en kort henvisning mellom analysene dersom de er faglig relaterte
   - ikke bland produktvurdering, tiltaksprioritering eller konklusjon på tvers av separate case

21. Vurder og dokumenter inputgrunnlag og analysetillit i alle analyser.

22. Angi analysetillit eksplisitt som én av følgende:
   - høy
   - middels
   - lav

23. Oppgi minst tre viktigste usikkerheter som påvirker konklusjonen.

24. Skill tydelig mellom usikkerhet som skyldes:
   - svakt inputgrunnlag
   - manglende eller tynne produktbeskrivelser
   - uavklarte juridiske eller organisatoriske forhold

### Fase 4: Leveranse og lagring

25. Skriv analysen iht. `config/templates/arkitekturassistert-analyse-av-utviklingsbehov-template.md`.

26. Lagre analysen i `analyser/`.

27. Navnestandard for nye analyser:
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

1. Kort oppsummering
2. Formål
3. Input / casebeskrivelse
3.1 Inputgrunnlag og analysetillit
4. Problembilde
5. Kapabilitetsanalyse
6. Prinsippvurdering
7. Produktvurdering
8. Tiltak prioritert etter effekt
9. Strategisk vurdering
10. Konklusjon

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
- viser at eventuell splitting av case er vurdert internt før rapportskriving
- viser minst ett sammensatt løsningsmønster basert på eksisterende produkter
- klassifiserer tiltak med primær gap-type
- peker på tydelige prioriterte tiltak med effektvurdering
- inneholder 3-7 konkrete spørsmål som bør avklares i videre diskusjon
- kan brukes både som rask analyse og som beslutningsgrunnlag


