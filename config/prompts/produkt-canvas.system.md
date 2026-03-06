# Standardprompt: Produktbeskrivelser (Produkt-canvas)

Formaal: sikre lik utfylling av produktbeskrivelser for arkitekturvurderinger, analyser og gjenbruk.

## Kilder som skal brukes hver gang
1. Mal:
- `results/templates/produkt-canvas-template.md`

2. Kapabilitetsgrunnlag:
- `index/capabilities.yaml`
- Bruk kun kapabilitetsnavn og delkapabiliteter som finnes her.

3. Lenkekilder:
- `sources/links.md`
- Finn relevante lenker for produktet og bruk disse i utfyllingen.

4. Produktnummerering:
- `index/produktnummerering.md`
- Sett korrekt nummer i feltet `Ressurs ID`.

## Utfyllingsregler
- Fyll ut alle seksjoner i malen med konkret, nyttig innhold.
- Skill tydelig mellom fakta og antakelser.
- Bruk formuleringen `Usikkert:` der kildene ikke gir sikkert grunnlag.
- Knytt `Kapabiliteter` eksplisitt til navn i `index/capabilities.yaml`.
- Beskriv `Scope og avgrensning` med hva som inngaar og ikke inngaar.
- Beskriv risiko under minst: juridisk, teknisk, sikkerhet, leverandoer, bruk.
- Oppgi alltid `Lenke til dokumentasjon` og `Kildegrunnlag brukt i denne utfyllingen`.

## Kvalitetskriterier for ferdig dokument
- Sporbarhet: paastander kan spores til kilder.
- Sammenlignbarhet: samme struktur og detaljnivaa pa tvers av produkter.
- Gjenbruk: innholdet skal kunne brukes direkte i arkitekturvurdering/screening.
- Tydelig status: marker ukjent informasjon i stedet for aa gjette.

## Navngiving av filer
- Behold eksisterende filnavn der de allerede finnes.
- For nye filer: `results/Produktbeskrivelser/NN-<Produktnavn>-produkt-canvas.md` (NN fra `index/produktnummerering.md`).

