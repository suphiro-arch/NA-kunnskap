# Avviksrapport: Produktbeskrivelser mot kapabilitetsmaster

Dato: 2026-03-18  
Status: Oppdatert etter full synk av produktbeskrivelser mot masterfila.
Kildegrunnlag:
- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
- siste versjon av produktbeskrivelsene i `arkitektur/produkter/produktbeskrivelser/`

## Viktig avklaring

Masterfila for produkt-kapabilitet-koblinger bygger **ikke** p? operative ressurskoblinger fra XML-modellen.

?rsak:
- XML-kilden har bare generiske ressurskoblinger og ikke koblinger p? niv? med konkrete produkter og delkapabiliteter i repoet.
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` er derfor fortsatt autoritativ kilde for koblingen mellom produkter og kapabiliteter.

## Oppsummering

Kontrollen fant `0` avvik. Alle siste produktbeskrivelser er n? synket mot masterfila for produkt-kapabilitet-koblinger.

## Utf?rt opprydding

- Tidligere avvik i `08`, `09`, `12`, `13-16` og `19-24` er rettet.
- Rekkef?lgen p? kapabiliteter i ?vrige ber?rte produktfiler er ogs? normalisert til masterfila.
- Rapporten kan n? brukes som bekreftelse p? at produktbeskrivelser og masterkoblinger er i sync per 2026-03-18.
