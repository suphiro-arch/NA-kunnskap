# Standardinstruks: enkel kapabilitetsmapping for problembeskrivelser

Formål:
- gi en rask og enkel førstesjekk av nye problembeskrivelser
- peke ut relevante kapabiliteter og mulige gjenbrukbare ressurser fra underlaget i Arkitektur i repo
- lage et kort notat som kan brukes for å kvalitetssjekke om riktige kapabaliliteter er mappet og gi 

## Når denne instruksen skal brukes
- når behovet er tidlig sortering eller screening
- når du vil ha rask retning, ikke fullstendig anbefaling
- når casegrunnlaget er kort eller foreløpig

Bruk ikke denne instruksen alene når beslutningen krever juridisk vurdering, prioritering av tiltak eller styringsforankring. Da brukes full analyseinstruks i tillegg.

## Mal og filnavn
- Bruk kortmalen i `config/templates/kapabilitesanalyse-template.md`.
- Nye analyser lagres med filnavn:
  - `NN-kapabilitesanalyse-<problemtittel>.md`
- Krav til filnavn:
  - `NN` er neste ledige løpenummer (to eller tre siffer).
  - `kapabilitesanalyse` skal alltid være med i filnavnet.
  - `<problemtittel>` skrives kort og beskrivende i kebab-case.

## Kilder som alltid skal brukes
1. `arkitektur/kapabiliteter/capabilities.yaml`
2. `arkitektur/ressurser/produktnummerering.md`
3. `arkitektur/ressurser/operative-losninger-og-tjenester/`
4. `config/regler/sprakforing.md`

Ved behov kan du supplere med:
- `arkitektur/ressurser/normerende-ressurser/`
- `arkitektur/ressurser/samarbeidsfora/`

## Enkel arbeidsmåte (maks 15-20 min per case)
1. Les problembeskrivelsen og oppsummer behovet i 2-4 setninger.
2. Velg kapabilitetene med sterkest kobling til behovet.
3. For hver kapabilitet: forklar kort hvorfor den er relevant.
4. Finn de mest gjenbrukbare ressursene fra katalogen å gjenbruke.
5. Klassifiser ressursene som:
   - `høy relevans`
   - `middels relevans`
   - `lav relevans / usikker`
6. Marker tydelig hva som er usikkert i mappingen.
7. Vurder eksplisitt om problemet peker på behov for andre kapabiliteter enn de som er dekket i dagens grunnlag.

## Regler for mapping
- Prioriter sterke og direkte koblinger, ikke brede assosiasjoner.
- Ikke foreslå ressurser som ikke finnes i katalogen, med mindre du markerer et eksplisitt gap.
- Bruk ressursbeskrivelser som hovedgrunnlag, ikke bare metadata i registeret.
- Hvis produktbeskrivelse mangler eller er tynn: marker `tynt beskrevet i underlag`.
- Behandle kapabiliteter med tom `delkapabiliteter`-liste som fullverdige kapabiliteter.
- Ikke bruk antall delkapabiliteter som kriterium for viktighet eller prioritet.
- Skill tydelig mellom:
  - kapabiliteter som finnes i dagens grunnlag og dekker behovet
  - kapabiliteter som mangler i grunnlaget, men som virker nødvendige for caset
- Svar skal skrives på norsk og med begreper fra repoet. Disse legges i eget avsnitt til slutt

## Rapportformat (obligatorisk)

### 1. Kort problembilde
- 2-4 setninger om hva behovet faktisk er.

## 2. Kapabilitetsmapping
| Kapabilitet | Hvorfor relevant for problemet | Relevans (høy/middels) |
|---|---|---|
| ... | ... | ... |

### 3. Mulige gjenbrukbare ressurser
| Ressurs-ID | Ressursnavn | Relevans (høy/middels/lav) | Hvordan kan den gjenbrukes | Merknad/usikkerhet |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |



### 4. Foreløpig konklusjon
- 3-5 punkt med:
  - mest dekkende kapabilitetre fra underlaget og de mest lovende gjenbrukbare ressurser
  - viktigste usikkerheter
  - om det er viktige problemstillinger som prosjektet bør stille seg for å kartlegge videre alternative løsninger

  ### 5. Ekstra sjekk: Behov for andre kapabiliteter enn dagens grunnlag
| Foreslått kapabilitet | Hvorfor den trengs i caset | Finnes i dagens grunnlag (ja/nei/delvis) | Konsekvens hvis den mangler |
|---|---|---|---|
| ... | ... | ... | ... |

Hvis ingen ekstra kapabiliteter er identifisert, skriv eksplisitt: `Ingen tydelige nye kapabilitetsbehov utover dagens grunnlag`.

## Kvalitetskontroll for leveranse
Sjekk at rapporten:
- inneholder minst 3-6 kapabiliteter med forklaringer
- inneholder 3-8 konkrete ressurser fra katalogen dersom det finnes relevante gjenbrukbare ressurser
- skiller tydelig mellom høy, middels og lav relevans
- inneholder eksplisitt vurdering av behov for kapabiliteter utover dagens grunnlag
- har eksplisitt usikkerhet knyttet til underlaget
- avslutter med klar anbefaling: `gå videre til full analyse` eller `avklar mer input først`
