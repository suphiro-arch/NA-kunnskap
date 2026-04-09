# Produkt-canvas: Kontakt- og reservasjonsregisteret

## Navn
Kontakt- og reservasjonsregisteret

## Ressurs ID
DIGDIR-005

## Status/Livsfase
**Produksjon** - etablert nasjonal fellesløsning for kontaktopplysninger og reservasjonsstatus ved digital kommunikasjon.

**Fakta:** Digdir beskriver Kontakt- og reservasjonsregisteret som den felles løsningen offentlige virksomheter bruker for å hente kontaktopplysninger og reservasjonsstatus for innbyggere. Dokumentasjonen beskriver både overordnet bruk, tilgangsregler og retningslinjer for bruk av registeret.

## Modenhet
**Høy modenhet** - tydelig innarbeidet registertjeneste med sterk regelverksforankring:
- Produktet er dokumentert som en sentral del av offentlig sektors digitale kommunikasjon med innbyggere.
- Det finnes egne sider for ta i bruk, retningslinjer og kostnadsmodell.
- Registeret brukes som felles grunnlag i mange virksomheter og prosesser.
- Produktets funksjon er stabil og tydelig avgrenset: oppdatert kontaktinformasjon og reservasjon som felles kilde.

**Deduksjon:** Modenheten er høy både fordi registeret er innarbeidet i offentlig sektor, og fordi bruksområdet er så klart avgrenset at det kan gjenbrukes i svært mange kommunikasjonssituasjoner.

## Kort beskrivelse
Kontakt- og reservasjonsregisteret er den nasjonale fellesløsningen for å finne innbyggeres digitale kontaktopplysninger og kontrollere om en innbygger er reservert mot digital kommunikasjon. Produktet gir offentlige virksomheter én felles kilde før de sender digital post, varsler eller annen digital kommunikasjon. Løsningen er særlig relevant når en virksomhet trenger pålitelig grunnlag for kanalvalg, men den erstatter ikke selve utsendings- eller varslingsløsningen.

## Kapabiliteter
- **Datakilder: Grunndata** fungerer som en felles autoritativ kilde for kontaktopplysninger og reservasjonsstatus som andre offentlige løsninger kan bygge på.
- **Datautveksling og integrasjon: Dele data med andre** gjør grunndata tilgjengelig for offentlige virksomheter gjennom et standardisert oppslag og bruksløp.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i Digdir Docs og Samarbeidsportalen.

## Produktmål
**Primærkilder:** Digdir Docs for Kontaktregisteret og Samarbeidsportalen for produktområdet.

Dokumenterte mål:
- Gi offentlige virksomheter tilgang til oppdaterte digitale kontaktopplysninger.
- Gjøre det mulig å kontrollere reservasjonsstatus før digital kommunikasjon sendes.
- Understøtte digital kommunikasjon på en måte som følger gjeldende regler og retningslinjer.

Operative mål utledet fra de samme kildene:
- Redusere behovet for lokale kopier og manuell oppdatering av kontaktopplysninger.
- Gi virksomheter et felles grunnlag for kanalvalg før de sender meldinger eller dokumenter.
- Sikre at reservasjon håndteres likt på tvers av virksomheter.

## Brukerbehov
- Offentlige virksomheter trenger oppdaterte kontaktopplysninger og reservasjonsstatus før de kommuniserer digitalt med innbyggere.
- Integrasjonsteam trenger et forutsigbart oppslag som kan bygges inn i egne arbeidsflyter og fagsystemer.
- Innbyggere trenger at kontaktopplysninger og reservasjon brukes konsistent og på en måte som gir tillit til digital kommunikasjon.
- Forvaltningsmiljøer trenger en felles løsning som gjør det enklere å følge regler for digital kontakt med innbyggere.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter som sender digital kommunikasjon | Oppdaterte kontaktopplysninger og reservasjonsstatus | Utsending av vedtak, meldinger og varsler | Bruker registeret som oppslag før kanalvalg |
| Integrasjonsteam og systemleverandører | Standardisert oppslag og tydelige regler for bruk | Integrasjon i sakssystemer, post- og varslingsflyter | Trenger å forstå både teknisk bruk og regelverk |
| Innbyggere | Kontroll over kontaktopplysninger og reservasjon | Oppdatering av egne data og forventning om korrekt bruk | Møter produktet indirekte gjennom digital kommunikasjon |
| Forvaltnings- og sikkerhetsmiljøer | Sporbar og regelmessig bruk av registeret | Etterlevelse, tilgangsstyring og revisjon | Trenger tydelig avgrensning mellom register og utsending |
| Tjenesteeiere for kommunikasjonstjenester | Felles datagrunnlag for kanalvalg | Samspill med digital post, varsling og andre kanaler | Avhengige av at registeret er oppdatert og forutsigbart |

## Hovedfunksjoner
### Primære funksjoner
- **Oppslag av kontaktopplysninger.** Produktet gir virksomheter tilgang til innbyggeres registrerte digitale kontaktopplysninger når de trenger å kommunisere digitalt. Dette dekker behovet for ett felles grunnlag i stedet for at hver virksomhet må samle og vedlikeholde egne kontaktdata.
- **Kontroll av reservasjonsstatus.** Registeret gjør det mulig å kontrollere om en innbygger har reservert seg mot digital kommunikasjon. Det er en avgjørende funksjon når virksomheten skal velge kanal og sikre at kommunikasjonen følger gjeldende regler.
- **Felles datagrunnlag for kanalvalg.** Kontakt- og reservasjonsregisteret brukes som beslutningsgrunnlag før meldinger eller dokumenter sendes. Dette gjør produktet relevant i mange prosesser, men det er ikke selve løsningen for utsending, postkasse eller varsling.
- **Selvbetjent oppdatering og forvaltning for innbyggere.** Produktet omfatter også et løp der innbygger kan oppdatere egne kontaktopplysninger og reservasjon. Det gjør registeret til mer enn bare en intern datakilde for virksomheter.
- **Regelstyrt og dokumentert bruk.** Produktet har egne retningslinjer og innføringsløp. Det er viktig fordi verdien ikke bare ligger i dataene, men også i at bruken er normert og forutsigbar på tvers av offentlig sektor.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Kontaktopplysninger og reservasjonsstatus som felles oppslag | Selve utsendingsløsningen for meldinger eller dokumenter |
| Oppslag og regelstyrt bruk av registerdata | Innlogging for brukere eller systemer |
| Grunnlag for kanalvalg | Digital postkasse, varsling eller meldingsinnhold |
| Innbyggers forvaltning av egne kontaktdata og reservasjon | Lokal CRM- eller sakshistorikk i virksomheten |
| Felles retningslinjer for bruk av dataene | Full erstatning for andre produkter i digital kommunikasjon |

## Veikart over kommende funksjonalitet
**Fakta fra Samarbeidsportalen og Digdir Docs (hentet 2026-03-17):**
- Produktområdet har egne sider for ta i bruk, retningslinjer og kostnadsmodell, noe som viser at løsningen er i aktiv forvaltning.
- Dokumentasjonen peker på registeret som stabilt grunnlag for digital kommunikasjon, ikke som et produkt i grunnleggende omlegging.

**Deduksjon:** Veikartet handler trolig mer om datakvalitet, innføringsstøtte og regelverksnær videreutvikling enn om store funksjonelle skifter. Rollen som felles grunndatakilde ser stabil ut.

## Forretningsverdi/Verdiforslag
### For virksomheter
- Reduserer behovet for å vedlikeholde egne kopier av kontaktopplysninger.
- Gjør kanalvalg mer forutsigbart og regelmessig.
- Senker risiko for å sende digital kommunikasjon på feil grunnlag.

### For innbyggere
- Gir bedre forutsetning for å bli kontaktet i riktig kanal.
- Gjør det mulig å reservere seg og forvente at reservasjonen blir respektert på tvers av virksomheter.
- Bidrar til større tillit til digital kommunikasjon fra offentlig sektor.

### For offentlig sektor
- Styrker gjenbruk ved at mange kommunikasjonstjenester bygger på samme kontaktgrunnlag.
- Tydeliggjør skillet mellom grunndata, kanalvalg og selve meldings- eller varslingsløsningen.
- Gir et mer ensartet og styrbart grunnlag for digital kommunikasjon med innbyggere.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk og regelverk | Feil bruk av reservasjon eller kontaktopplysninger kan gi brudd på regelverk og tillit | Tydelige retningslinjer, tilgangsstyring og revisjon |
| Datakvalitet | Utdaterte eller mangelfulle kontaktopplysninger kan gi feil kanalvalg | Løpende vedlikehold og gode mekanismer for oppdatering |
| Teknisk | Feil integrasjon kan gjøre at virksomheten hopper over registeroppslag eller bruker gamle data | Integrasjonstesting og tydelig innføringsveiledning |
| Avhengigheter | Produktet kan bli forvekslet med varslings- eller utsendingsløsninger | Klare avgrensninger i arkitektur og dokumentasjon |
| Brukeropplevelse | Innbyggere kan miste tillit dersom kontaktdata eller reservasjon ikke håndteres konsekvent | Bedre informasjon og korrekt etterlevelse hos virksomhetene |

## Kanaler
- Produktside: https://docs.digdir.no/docs/Kontaktregisteret/
- Overordnet dokumentasjon: https://docs.digdir.no/docs/Kontaktregisteret/krr_overordnet
- Samarbeidsportal: https://samarbeid.digdir.no/kontaktregisteret/dette-er-kontaktregisteret/110
- Ta i bruk: https://samarbeid.digdir.no/kontaktregisteret/ta-i-bruk-kontaktregisteret/95
- Retningslinjer: https://samarbeid.digdir.no/kontaktregisteret/retningslinjer-bruk-av-kontakt-og-reservasjonsregisteret/143
- Kostnadsmodell: https://samarbeid.digdir.no/kontaktregisteret/kostnadsmodell-kontaktregisteret/577

## Plattform
Kontakt- og reservasjonsregisteret er en nasjonal registertjeneste som gir oppslag mot et felles datagrunnlag for kontaktinformasjon og reservasjon.

**Fakta:** Digdir Docs beskriver både teknisk bruk og overordnet funksjon, og Samarbeidsportalen beskriver ta-i-bruk-løp, retningslinjer og kostnadsmodell.

**Ikke offentlig dokumentert i brukte kilder:** Full runtime-arkitektur, detaljert driftsoppsett og konkret infrastrukturnivå.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er laget for å være en felles kilde som mange andre løsninger bygger på.
- Det er særlig relevant når behovet er korrekt kontaktgrunnlag og reservasjonskontroll før digital kommunikasjon.
- Det er mindre relevant dersom behovet egentlig er selve utsendingen, postkassen eller varslingskanalen.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at kontaktopplysninger og reservasjonsstatus tilbys som felles grunnlag for mange virksomheter.
- **P5: Del og gjenbruk løsninger** styrkes fordi offentlig sektor kan bygge på samme register i stedet for lokale kopier og særordninger.
- **P7: Sørg for tillit til oppgaveløsningen** støttes ved at reservasjon og kontaktdata håndteres mer konsistent og forutsigbart.

## Finansiering
- **Fakta:** Samarbeidsportalen har en egen kostnadsmodell for Kontakt- og reservasjonsregisteret.
- **Fakta:** Samarbeidsportalen beskriver at bruk av registeret er kostnadsfritt, mens virksomhetene dekker egne kostnader til integrasjon og innføring.
- **Deduksjon:** Finansieringsmodellen er derfor rettet mot felles nasjonal forvaltning av registeret, kombinert med lokale innføringskostnader hos brukerne.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Digdir Docs og Samarbeidsportalen |
| Driftsansvar | Ikke eksplisitt navngitt i brukte offentlige kilder | Offentlige kilder beskriver ikke detaljert leverandør- eller driftsmodell |
| Budsjett- og kostnadsmodell | Digdir forvalter registeret, med publisert kostnadsmodell | Samarbeidsportalen |
| Styringsmodell | Del av Digdirs portefølje for digital kommunikasjon | Samarbeidsportalen |

## Lenke til dokumentasjon
- https://docs.digdir.no/docs/Kontaktregisteret/
- https://docs.digdir.no/docs/Kontaktregisteret/krr_overordnet
- https://samarbeid.digdir.no/kontaktregisteret/dette-er-kontaktregisteret/110
- https://samarbeid.digdir.no/kontaktregisteret/ta-i-bruk-kontaktregisteret/95
- https://samarbeid.digdir.no/kontaktregisteret/retningslinjer-bruk-av-kontakt-og-reservasjonsregisteret/143
- https://samarbeid.digdir.no/kontaktregisteret/kostnadsmodell-kontaktregisteret/577

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/05-Kontakt-og-reservasjonsregisteret-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.digdir.no/docs/Kontaktregisteret/ (hentet 2026-03-17)
- Nettkilde: https://docs.digdir.no/docs/Kontaktregisteret/krr_overordnet (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/kontaktregisteret/dette-er-kontaktregisteret/110 (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/kontaktregisteret/ta-i-bruk-kontaktregisteret/95 (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/kontaktregisteret/retningslinjer-bruk-av-kontakt-og-reservasjonsregisteret/143 (hentet 2026-03-17)
- Nettkilde: https://samarbeid.digdir.no/kontaktregisteret/kostnadsmodell-kontaktregisteret/577 (hentet 2026-03-17)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Kapabilitetslisten er redusert til de direkte funksjonene registeret faktisk leverer, og indirekte koblinger til varsling, identifisering og andre løsninger er tatt ut.
- Produktet beskrives tydeligere som grunndatakilde og beslutningsgrunnlag for kanalvalg, ikke som selve kommunikasjonsløsningen.
- Finansieringsfeltet bygger nå på publisert kostnadsmodell og avklaringen om at bruk er kostnadsfri, mens integrasjon må dekkes lokalt.

### Tekstlige forbedringer
- Dokumentet starter ikke lenger med målgruppelinje, og `Ressurs ID` er skrevet uten parentesforklaring.
- Hovedfunksjoner og avgrensning gjør det tydeligere når Kontakt- og reservasjonsregisteret er riktig produkt for gjenbruk.
- Beskrivelsen bruker mer aktiv og målrettet språk for nasjonal arkitektur, i stedet for å liste opp tilgrensende produkter og funksjoner.


