# Avviksrapport: XML mot kapabilitets- og prinsippgrunnlag

Dato: 2026-03-18  
Kildegrunnlag:
- `sources/2025-03-18-Nasjonal Arkitektur.xml`
- `arkitektur/kapabiliteter/capabilities.yaml`
- `arkitektur/prinsipper/principles.md`

## Formål

Denne rapporten sammenligner den nye XML-kilden med dagens kuraterte kapabilitetsfil og prinsippgrunnlag i repoet. Den gamle HTML-fila som YAML-en opprinnelig ble laget fra ligger ikke i repoet, så sammenligningen er gjort direkte mot XML-modellen.

## Kort oppsummering

- Hierarkiet for kapabiliteter stemmer i hovedsak.
- XML og YAML har begge `13` hovedkapabiliteter.
- XML og YAML har begge `45` delkapabiliteter.
- Prinsippkoblingene stemmer i all hovedsak, men ett faktisk avvik ble funnet og rettet.

## Hva som stemmer

### Hovedkapabiliteter

Følgende hovedkapabiliteter finnes i begge kilder:

- `Strategisk styring`
- `Samarbeid`
- `Sluttbrukertjenester`
- `Datautveksling og integrasjon`
- `Tillit`
- `Datadrevet`
- `Informasjonssikkerhet`
- `Tjenesteutvikling`
- `Informasjonsforvaltning`
- `Standardisering`
- `Juridisk samhandling`
- `Veiledning`
- `Datakilder`

### Delkapabiliteter

De `45` delkapabilitetene i YAML samsvarer med de operative delkapabilitetene i XML-modellen.

## Faktisk avvik

### Prinsippkobling for `Datautveksling og integrasjon`

XML-modellen kobler `Datautveksling og integrasjon` til:

- `P4: Del og gjenbruk data`
- `P6: Lag digitale løsninger som støtter samhandling`

I `capabilities.yaml` var bare `P4` med. `P6` manglet.

Status:
- Rettet i [capabilities.yaml](c:/Users/HILROS/NA-kunnskap/arkitektur/kapabiliteter/capabilities.yaml)
- Synket i [principles.md](c:/Users/HILROS/NA-kunnskap/arkitektur/prinsipper/principles.md)
- Synket i [prinsipper/_index.md](c:/Users/HILROS/NA-kunnskap/web/hugo-prototype/content/prinsipper/_index.md)

## Bevisste avgrensninger i YAML

XML-kilden inneholder også hjelpeelementer, generiske modellobjekter og duplikater som ikke bør inn i den ryddede kapabilitetsfila:

- `Strategisk kapabilitet (overordnet)`
- `Kapabilitet (Operasjonell)`
- `Veiledning og standardisering (copy)`
- `Prinsipper Nasjonal Arkitektur`
- `Prinsipp`
- `Kun en gang`
- `FAIR`
- `NSM`
- `P3: Bidra til digitaliseringsvennlige regelverk (copy)`

Disse elementene er ikke brukt som operative hoved- eller delkapabiliteter i repoets kuraterte struktur.

## Målkoblinger i XML

XML-kilden inneholder også et målspor som ikke tidligere var representert i repoet.

Det viktigste som faktisk er modellert er:

- `Nasjonal arkitektur for samhandling` realiserer målet `Et velfungerende felles digitalt økosystem for samhandling og tjenesteutvikling i offentlig sektor`
- dette målet påvirker åtte strategiske mål videre

Det er derimot ikke modellert en full, operativ kobling fra hver hovedkapabilitet til hvert mål.

Konsekvens:
- målsporet bør håndteres i en egen kuratert fil
- det bør ikke blandes inn i `capabilities.yaml` uten videre

Status:
- opprettet [maal.md](c:/Users/HILROS/NA-kunnskap/arkitektur/maal/maal.md) som første kuraterte måloversikt

## Ressurskoblinger i XML

XML-kilden beskriver ikke ressurskoblinger på samme nivå som repoets ressursoversikt og produktmaster.

Eksplisitte koblinger i XML:

- `Ressurs` -> `Strategisk kapabilitet (overordnet)`
- `Sektorarkitektur` -> `Sektorarkitektur`

Dette er modelltekniske eller generiske relasjoner, ikke operative koblinger mellom konkrete produkter og kapabiliteter.

Konsekvens:
- XML-kilden kan ikke brukes som erstatning for [produkt-kapabilitet-koblinger.yaml](c:/Users/HILROS/NA-kunnskap/arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml)
- repoets eksisterende masterfil for produkter og kapabiliteter må fortsatt være autoritativ for denne koblingen

## Utførte endringer i denne runden

- La inn manglende `P6`-kobling på `Datautveksling og integrasjon` i `capabilities.yaml`.
- Fylte ut `arkitektur/prinsipper/principles.md` med de sju operative prinsippene og koblingene til hovedkapabiliteter.
- Oppdaterte web-versjonen av prinsippsiden slik at den følger samme koblinger.
- Opprettet `arkitektur/maal/maal.md` som første kuraterte måloversikt basert på XML-kilden.

## Anbefalt videre arbeid

1. Bruk `capabilities.yaml` som kuratert master for kapabilitetsstrukturen.
2. Bruk `principles.md` som tilsvarende kildefil for prinsippene.
3. Behold XML-fila som råkilde og dokumenter avvik eksplisitt når modellen blir videre kuratert.
