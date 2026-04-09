# Avviksrapport: Produktbeskrivelser mot kapabilitetsmaster

Dato: 2026-03-18  
Status: Oppdatert etter full synk av produktbeskrivelser mot masterfila.
Kildegrunnlag:
- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
- siste versjon av produktbeskrivelsene i `arkitektur/ressurser/operative-losninger-og-tjenester/`

## Viktig avklaring

Masterfila for produkt-kapabilitet-koblinger bygger **ikke** pÃ¥ operative ressurskoblinger fra XML-modellen.

Ã…rsak:
- XML-kilden har bare generiske ressurskoblinger og ikke koblinger pÃ¥ nivÃ¥ med konkrete produkter og delkapabiliteter i repoet.
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` er derfor fortsatt autoritativ kilde for koblingen mellom produkter og kapabiliteter.

## Oppsummering

Kontrollen fant `0` avvik. Alle siste produktbeskrivelser er nÃ¥ synket mot masterfila for produkt-kapabilitet-koblinger.

## UtfÃ¸rt opprydding

- Tidligere avvik i `08`, `09`, `12`, `13-16` og `19-24` er rettet.
- RekkefÃ¸lgen pÃ¥ kapabiliteter i Ã¸vrige berÃ¸rte produktfiler er ogsÃ¥ normalisert til masterfila.
- Rapporten kan nÃ¥ brukes som bekreftelse pÃ¥ at produktbeskrivelser og masterkoblinger er i sync per 2026-03-18.

