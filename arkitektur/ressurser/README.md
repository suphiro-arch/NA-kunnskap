# Ressurser

Denne mappa samler styringsgrunnlag og videre struktur for ressursområdet i repoet.

## Formål
- gi én felles inngang til ressurser som ikke bare er klassiske produktbeskrivelser
- skille tydelig mellom operative løsninger og tjenester, normerende ressurser og samarbeidsfora
- gjøre det lettere å utvide repoet med nye ressursfamilier uten å blande sammen løsning, styring og normering

## Innhold
- `styringsregler.md`: definisjoner, opptakskriterier og klassifiseringsregler for ressursområdet
- `ressursregister.md`: midlertidig arbeidsnotat fra tidlig overgangsfase, ikke operativ master
- `operative-losninger-og-tjenester/`: operative løsninger, tjenester, plattformer, registre, portaler og lignende ressurser i bruk
- `normerende-ressurser/`: standarder, veiledere, referansearkitektur, informasjonsmodeller og andre styrende ressurser
- `samarbeidsfora/`: fora, råd, nettverk og samordningsarenaer som påvirker retning og prioritering

## Forhold til produktområdet
- `arkitektur/ressurser/` er operativt hjem for registerføring og ressursbeskrivelser.
- `arkitektur/ressurser/produktnummerering.md` er master for ressurs-ID-er og dokumentkoblinger.
- nye ressursbeskrivelser opprettes direkte i riktig undermappe under `arkitektur/ressurser/`.

## Praktisk bruk
- bruk `styringsregler.md` før nye ressurskategorier eller nye ressurser opprettes
- bruk `arkitektur/ressurser/produktnummerering.md` som operativ master for registerføring og ressurs-ID-er
- velg én primær ressurskategori per ressurs
- bruk kapabiliteter som kobling og metadata, ikke som primær mappeinndeling
