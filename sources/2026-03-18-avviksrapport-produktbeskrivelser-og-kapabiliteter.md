# Avviksrapport: Produktbeskrivelser mot kapabilitetsmaster

Dato: 2026-03-18  
Kildegrunnlag:
- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml`
- siste versjon av produktbeskrivelsene i `results/Produktbeskrivelser/`

## Formål

Denne rapporten viser avvik mellom:

- kapabilitetsseksjonen i siste versjon av hver produktbeskrivelse
- den kuraterte masterfila for produkt-kapabilitet-koblinger

Rapporten er laget etter at den nye nasjonale arkitekturmodellen ble kuratert videre i repoet.

## Viktig avklaring

Masterfila for produkt-kapabilitet-koblinger bygger **ikke** på operative ressurskoblinger fra XML-modellen.

Årsak:
- XML-kilden har bare to generiske ressurskoblinger:
  - `Ressurs -> Strategisk kapabilitet (overordnet)`
  - `Sektorarkitektur -> Sektorarkitektur`
- disse er ikke på nivå med konkrete produkter og delkapabiliteter i repoet

Konsekvens:
- `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` er fortsatt autoritativ kilde for koblingen mellom produkter og kapabiliteter
- avvik må derfor håndteres ved å oppdatere produktbeskrivelsene eller masterfila, ikke ved å lene seg på XML

## Oppsummering

Ved kontroll mot siste produktversjon ble det funnet avvik i `13` produktbeskrivelser.

Avvikene er av tre typer:

1. produktbeskrivelsen bruker eldre eller for brede koblinger
2. produktbeskrivelsen bruker eldre formulering av en delkapabilitet
3. produktbeskrivelsen har formateringsfeil i kapabilitetsseksjonen

## Avvik som bør rettes

### Høy prioritet

#### `08 Altinn formidling`
- bruker `Informasjonssikkerhet: Sikring av informasjonsflyt`
- bør bruke `Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling`
- har også `Tillit: Sporbarhet og innsyn` i dokumentet, men ikke i masterfila

#### `09 Digital postkasse`
- kapabilitetsseksjonen er delvis ødelagt i selve dokumentet
- viser bare hovedkapabiliteter med kolon, ikke gyldige delkapabilitetsnavn
- bør oppdateres først av avviksfilene

#### `12 Altinn events`
- bruker eldre formulering for informasjonssikkerhet
- har i tillegg `Sluttbrukertjenester: Proaktive tjenester` og `Informasjonsforvaltning: Oversikt over hendelser` i dokumentet, men ikke i masterfila

### Middels prioritet

#### `13 Felles datakatalog`
- dokumentet har fortsatt `Datautveksling og integrasjon: Dele data med andre`
- masterfila har strammere avgrensning uten denne koblingen

#### `14 Begrepskatalog`
- dokumentet har fortsatt:
  - `Datautveksling og integrasjon: Dele data med andre`
  - `Samarbeid: Organisatorisk samhandling`
- masterfila har strammere avgrensning uten disse koblingene

#### `15 API-katalog`
- dokumentet har fortsatt:
  - `Datautveksling og integrasjon: Dele data med andre`
  - `Datautveksling og integrasjon: Bruke data fra andre`
  - `Tjenesteutvikling: Integrerbare tjenester`
- masterfila har strammere avgrensning uten disse koblingene

#### `16 data.norge.no`
- dokumentet har fortsatt:
  - `Datautveksling og integrasjon: Dele data med andre`
  - `Datautveksling og integrasjon: Bruke data fra andre`
- masterfila har strammere avgrensning uten disse koblingene

### Lavere prioritet, men bør synkes

#### `19 Altinn`
- dokumentet er bredere enn masterfila og bør strammes inn

#### `20 Altinn Studio`
- dokumentet er bredere enn masterfila og bør strammes inn

#### `21 Altinn Portal`
- dokumentet har fortsatt:
  - `Samarbeid: Tjenesteforvaltning`
  - `Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling`
- masterfila er strammere

#### `22 Dialogporten`
- dokumentet har fortsatt `Samarbeid: Tjenesteforvaltning`
- masterfila er strammere

#### `23 Altinn 3 Melding`
- dokumentet har fortsatt `Sluttbrukertjenester: Sammenhengende tjenester`
- masterfila er strammere

#### `24 Varslinger`
- dokumentet har fortsatt `Standardisering: Forvaltningsstandarder`
- masterfila er strammere

## Anbefalt rekkefølge for opprydding

1. `09 Digital postkasse`
2. `08 Altinn formidling`
3. `12 Altinn events`
4. `13-16` som samlet informasjonsforvaltningsrunde
5. `19-24` som samlet Altinn-runde

## Forslag til neste sektor for nye produktbeskrivelser

Når avvikene over er håndtert, er `SIKT` den mest naturlige neste sektoren.

Begrunnelse:
- sektoren er allerede lagt inn og kvalitetssikret i produktregisteret
- den har flere tydelige fellesressurser med tverrsektoriell relevans
- de mest naturlige første kandidatene er:
  - `Feide`
  - `Vitnemålsportalen`
