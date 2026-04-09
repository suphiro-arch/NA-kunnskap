# Produkt-canvas: NAIS

## Navn
NAIS

## Ressurs ID
NAV-002

## Status/Livsfase
**Produksjon** - etablert plattform for utvikling og drift av applikasjoner, bygget av Nav og dokumentert for bruk utover ett enkelt team- eller virksomhetsmiljø.

**Fakta:** Nais beskriver seg som en plattform laget av Nav for å gi fart og flyt til utviklerne av det offentlige Norge. Dokumentasjonen beskriver plattformen som et sett tjenester og byggeklosser for utvikling, kjøring, observability, sikkerhet og plattformnær drift.

**Presisering:** Produktet har ikke samme dokumenterte status som nasjonal fellesløsning eller formell felleskomponent som de klassiske fellestjenestene i registeret. Det er likevel en relevant og interessant plattform å vurdere for gjenbruk, og ved behov som passer denne typen plattform bør det være aktuelt å gå i dialog med eier om mulig samarbeid og bruk.

## Modenhet
**Høy modenhet** - innarbeidet plattform med omfattende dokumentasjon og åpent miljø:
- har moden utviklerdokumentasjon og tydelig ansvarsmodell
- bygger på åpne og dokumenterte plattformmønstre
- framstår som åpen for bruk også utenfor ett enkelt NAV-team

**Deduksjon:** Modenheten er høy som plattform, men dens status som nasjonal fellesressurs er svakere dokumentert enn for klassiske felleskomponenter. Produktet bør derfor beskrives som en gjenbrukbar offentlig plattformmodell, ikke som en formell nasjonal felleskomponent.

## Kort beskrivelse
NAIS er en plattform for utvikling, kjøring og forvaltning av applikasjoner, laget av Nav og videreført som et åpent plattformmiljø for utviklingsteam i offentlig sektor. Produktet samler funksjoner for utrulling, sikkerhet, observability, konfigurasjon og drift, slik at team kan fokusere mer på applikasjonene sine og mindre på grunnleggende plattformarbeid. NAIS er derfor først og fremst en gjenbrukbar plattformmodell og et felles utviklingsmiljø, ikke et register eller en sektorfelles datatjeneste.

## Kapabiliteter
- **Tjenesteutvikling: Gjenbrukbare tjenester**
- **Tjenesteutvikling: Utviklings- og kjøretidsmiljø**

## Produktmål
- gjøre det lettere å utvikle og drifte applikasjoner på en trygg måte
- tilby felles plattformkapabiliteter som utviklingsteam kan bygge på
- redusere kompleksitet i utviklings- og driftsarbeidet

## Brukerbehov
- utviklingsteam trenger et standardisert plattformgrunnlag
- virksomheter trenger sikker og effektiv applikasjonsdrift
- plattformmiljøer trenger gjenbrukbare byggeklosser framfor mange lokale oppsett

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Utviklingsteam | Standardisert plattform og verktøy | Bygging, utrulling og drift | Primærbrukere |
| Plattform- og driftsteam | Felles plattformmodell | Forvaltning og videreutvikling | Viktig intern brukergruppe |
| Offentlige virksomheter som vurderer gjenbruk | Dokumentert plattformmodell | Vurdering og eventuell adopsjon | Mer potensiell enn fullt verifisert brukergruppe |

## Hovedfunksjoner
### Primære funksjoner
**Felles runtime og plattformtjenester.** NAIS gir team et robust og sikkert kjøretidsmiljø for applikasjoner.

**Standardiserte byggeklosser for utvikling og drift.** Plattformen tilbyr verktøy og mønstre for deploy, observability, sikkerhet og konfigurasjon.

**Åpent dokumentert plattformmodell.** Dokumentasjonen og den åpne profilen gjør NAIS relevant som gjenbrukbar modell også utenfor NAV.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Plattformtjenester og runtime for applikasjoner | Alle applikasjonene som kjører på plattformen |
| Felles verktøy for deploy, drift og observability | Formelle nasjonale felleskomponenter i juridisk forstand |
| Åpen plattformmodell og dokumentasjon | Hele NAVs virksomhetsarkitektur |

## Veikart over kommende funksjonalitet
**Fakta fra kildene (kontrollert 2026-03-27):**
- Dokumentasjonen er aktiv og oppdatert.
- Ansvars- og rollebeskrivelser er publisert som del av plattformstyringen.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et samlet veikart for plattformen er ikke hentet ut.

## Forretningsverdi/Verdiforslag
- gir raskere og mer standardisert utvikling og drift
- reduserer behovet for at hvert team bygger sitt eget plattformgrunnlag
- styrker sikkerhet og observability gjennom felles mønstre

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Gjenbruksstatus | det er uklart hvor bredt den faktisk er tatt i bruk utenfor NAV | tydelig avgrensning i beskrivelsen |
| Styring | plattformens styringsmodell er knyttet til egne team og miljøer | beskrive den som plattformmodell, ikke formell felleskomponent |
| Juridikk og ansvar | ansvar ligger tydelig hos team og plattformmiljø, ikke i en generell offentlig styringsmodell | bruke publisert ansvarsmodell som grunnlag |

## Kanaler
- https://nais.io/
- https://doc.nais.io/
- https://doc.nais.io/explanations/nais/
- https://doc.nais.io/legal/roles-responsibilities/
- https://github.com/navikt

## Plattform
NAIS er selv en plattform for utvikling, utrulling og drift av applikasjoner.

## Gjenbruk
**Middels gjenbruksverdi** som offentlig plattformmodell. Den er tydelig gjenbrukbar og åpent dokumentert, men svakere som formell nasjonal fellesressurs enn de klassiske register- og delingsløsningene.

## Støtter arkitekturprinsipper
- **P5: Del og gjenbruk løsninger**
- **P6: Lag digitale løsninger som støtter samhandling**

## Finansiering
Ikke samlet verifisert i denne arbeidsøkten.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Plattformansvar | Nav / NAIS-teamet | dokumentasjonen |
| Bruksansvar for applikasjoner | De enkelte teamene | publisert ansvarsmodell |

## Lenke til dokumentasjon
- https://nais.io/
- https://doc.nais.io/
- https://doc.nais.io/explanations/nais/
- https://doc.nais.io/legal/roles-responsibilities/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://nais.io/ (kontrollert 2026-03-27)
- Nettkilde: https://doc.nais.io/ (kontrollert 2026-03-27)
- Nettkilde: https://doc.nais.io/explanations/nais/ (kontrollert 2026-03-27)
- Nettkilde: https://doc.nais.io/legal/roles-responsibilities/ (kontrollert 2026-03-27)



