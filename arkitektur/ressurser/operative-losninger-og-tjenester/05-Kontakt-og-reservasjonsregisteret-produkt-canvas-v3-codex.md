# Produkt-canvas: Kontakt- og reservasjonsregisteret

## Navn
Kontakt- og reservasjonsregisteret

## Ressurs ID
DIGDIR-005

## Status/Livsfase
**Produksjon** - etablert nasjonal felleslÃ¸sning for kontaktopplysninger og reservasjonsstatus ved digital kommunikasjon.

**Fakta:** Digdir beskriver Kontakt- og reservasjonsregisteret som den felles lÃ¸sningen offentlige virksomheter bruker for Ã¥ hente kontaktopplysninger og reservasjonsstatus for innbyggere. Dokumentasjonen beskriver bÃ¥de overordnet bruk, tilgangsregler og retningslinjer for bruk av registeret.

## Modenhet
**HÃ¸y modenhet** - tydelig innarbeidet registertjeneste med sterk regelverksforankring:
- Produktet er dokumentert som en sentral del av offentlig sektors digitale kommunikasjon med innbyggere.
- Det finnes egne sider for ta i bruk, retningslinjer og kostnadsmodell.
- Registeret brukes som felles grunnlag i mange virksomheter og prosesser.
- Produktets funksjon er stabil og tydelig avgrenset: oppdatert kontaktinformasjon og reservasjon som felles kilde.

**Deduksjon:** Modenheten er hÃ¸y bÃ¥de fordi registeret er innarbeidet i offentlig sektor, og fordi bruksomrÃ¥det er sÃ¥ klart avgrenset at det kan gjenbrukes i svÃ¦rt mange kommunikasjonssituasjoner.

## Kort beskrivelse
Kontakt- og reservasjonsregisteret er den nasjonale felleslÃ¸sningen for Ã¥ finne innbyggeres digitale kontaktopplysninger og kontrollere om en innbygger er reservert mot digital kommunikasjon. Produktet gir offentlige virksomheter Ã©n felles kilde fÃ¸r de sender digital post, varsler eller annen digital kommunikasjon. LÃ¸sningen er sÃ¦rlig relevant nÃ¥r en virksomhet trenger pÃ¥litelig grunnlag for kanalvalg, men den erstatter ikke selve utsendings- eller varslingslÃ¸sningen.

## Kapabiliteter
- **Datakilder: Grunndata** fungerer som en felles autoritativ kilde for kontaktopplysninger og reservasjonsstatus som andre offentlige lÃ¸sninger kan bygge pÃ¥.
- **Datautveksling og integrasjon: Dele data med andre** gjÃ¸r grunndata tilgjengelig for offentlige virksomheter gjennom et standardisert oppslag og brukslÃ¸p.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i Digdir Docs og Samarbeidsportalen.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Digdir Docs for Kontaktregisteret og Samarbeidsportalen for produktomrÃ¥det.

Dokumenterte mÃ¥l:
- Gi offentlige virksomheter tilgang til oppdaterte digitale kontaktopplysninger.
- GjÃ¸re det mulig Ã¥ kontrollere reservasjonsstatus fÃ¸r digital kommunikasjon sendes.
- UnderstÃ¸tte digital kommunikasjon pÃ¥ en mÃ¥te som fÃ¸lger gjeldende regler og retningslinjer.

Operative mÃ¥l utledet fra de samme kildene:
- Redusere behovet for lokale kopier og manuell oppdatering av kontaktopplysninger.
- Gi virksomheter et felles grunnlag for kanalvalg fÃ¸r de sender meldinger eller dokumenter.
- Sikre at reservasjon hÃ¥ndteres likt pÃ¥ tvers av virksomheter.

## Brukerbehov
- Offentlige virksomheter trenger oppdaterte kontaktopplysninger og reservasjonsstatus fÃ¸r de kommuniserer digitalt med innbyggere.
- Integrasjonsteam trenger et forutsigbart oppslag som kan bygges inn i egne arbeidsflyter og fagsystemer.
- Innbyggere trenger at kontaktopplysninger og reservasjon brukes konsistent og pÃ¥ en mÃ¥te som gir tillit til digital kommunikasjon.
- ForvaltningsmiljÃ¸er trenger en felles lÃ¸sning som gjÃ¸r det enklere Ã¥ fÃ¸lge regler for digital kontakt med innbyggere.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige virksomheter som sender digital kommunikasjon | Oppdaterte kontaktopplysninger og reservasjonsstatus | Utsending av vedtak, meldinger og varsler | Bruker registeret som oppslag fÃ¸r kanalvalg |
| Integrasjonsteam og systemleverandÃ¸rer | Standardisert oppslag og tydelige regler for bruk | Integrasjon i sakssystemer, post- og varslingsflyter | Trenger Ã¥ forstÃ¥ bÃ¥de teknisk bruk og regelverk |
| Innbyggere | Kontroll over kontaktopplysninger og reservasjon | Oppdatering av egne data og forventning om korrekt bruk | MÃ¸ter produktet indirekte gjennom digital kommunikasjon |
| Forvaltnings- og sikkerhetsmiljÃ¸er | Sporbar og regelmessig bruk av registeret | Etterlevelse, tilgangsstyring og revisjon | Trenger tydelig avgrensning mellom register og utsending |
| Tjenesteeiere for kommunikasjonstjenester | Felles datagrunnlag for kanalvalg | Samspill med digital post, varsling og andre kanaler | Avhengige av at registeret er oppdatert og forutsigbart |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- **Oppslag av kontaktopplysninger.** Produktet gir virksomheter tilgang til innbyggeres registrerte digitale kontaktopplysninger nÃ¥r de trenger Ã¥ kommunisere digitalt. Dette dekker behovet for ett felles grunnlag i stedet for at hver virksomhet mÃ¥ samle og vedlikeholde egne kontaktdata.
- **Kontroll av reservasjonsstatus.** Registeret gjÃ¸r det mulig Ã¥ kontrollere om en innbygger har reservert seg mot digital kommunikasjon. Det er en avgjÃ¸rende funksjon nÃ¥r virksomheten skal velge kanal og sikre at kommunikasjonen fÃ¸lger gjeldende regler.
- **Felles datagrunnlag for kanalvalg.** Kontakt- og reservasjonsregisteret brukes som beslutningsgrunnlag fÃ¸r meldinger eller dokumenter sendes. Dette gjÃ¸r produktet relevant i mange prosesser, men det er ikke selve lÃ¸sningen for utsending, postkasse eller varsling.
- **Selvbetjent oppdatering og forvaltning for innbyggere.** Produktet omfatter ogsÃ¥ et lÃ¸p der innbygger kan oppdatere egne kontaktopplysninger og reservasjon. Det gjÃ¸r registeret til mer enn bare en intern datakilde for virksomheter.
- **Regelstyrt og dokumentert bruk.** Produktet har egne retningslinjer og innfÃ¸ringslÃ¸p. Det er viktig fordi verdien ikke bare ligger i dataene, men ogsÃ¥ i at bruken er normert og forutsigbar pÃ¥ tvers av offentlig sektor.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Kontaktopplysninger og reservasjonsstatus som felles oppslag | Selve utsendingslÃ¸sningen for meldinger eller dokumenter |
| Oppslag og regelstyrt bruk av registerdata | Innlogging for brukere eller systemer |
| Grunnlag for kanalvalg | Digital postkasse, varsling eller meldingsinnhold |
| Innbyggers forvaltning av egne kontaktdata og reservasjon | Lokal CRM- eller sakshistorikk i virksomheten |
| Felles retningslinjer for bruk av dataene | Full erstatning for andre produkter i digital kommunikasjon |

## Veikart over kommende funksjonalitet
**Fakta fra Samarbeidsportalen og Digdir Docs (hentet 2026-03-17):**
- ProduktomrÃ¥det har egne sider for ta i bruk, retningslinjer og kostnadsmodell, noe som viser at lÃ¸sningen er i aktiv forvaltning.
- Dokumentasjonen peker pÃ¥ registeret som stabilt grunnlag for digital kommunikasjon, ikke som et produkt i grunnleggende omlegging.

**Deduksjon:** Veikartet handler trolig mer om datakvalitet, innfÃ¸ringsstÃ¸tte og regelverksnÃ¦r videreutvikling enn om store funksjonelle skifter. Rollen som felles grunndatakilde ser stabil ut.

## Forretningsverdi/Verdiforslag
### For virksomheter
- Reduserer behovet for Ã¥ vedlikeholde egne kopier av kontaktopplysninger.
- GjÃ¸r kanalvalg mer forutsigbart og regelmessig.
- Senker risiko for Ã¥ sende digital kommunikasjon pÃ¥ feil grunnlag.

### For innbyggere
- Gir bedre forutsetning for Ã¥ bli kontaktet i riktig kanal.
- GjÃ¸r det mulig Ã¥ reservere seg og forvente at reservasjonen blir respektert pÃ¥ tvers av virksomheter.
- Bidrar til stÃ¸rre tillit til digital kommunikasjon fra offentlig sektor.

### For offentlig sektor
- Styrker gjenbruk ved at mange kommunikasjonstjenester bygger pÃ¥ samme kontaktgrunnlag.
- TydeliggjÃ¸r skillet mellom grunndata, kanalvalg og selve meldings- eller varslingslÃ¸sningen.
- Gir et mer ensartet og styrbart grunnlag for digital kommunikasjon med innbyggere.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk og regelverk | Feil bruk av reservasjon eller kontaktopplysninger kan gi brudd pÃ¥ regelverk og tillit | Tydelige retningslinjer, tilgangsstyring og revisjon |
| Datakvalitet | Utdaterte eller mangelfulle kontaktopplysninger kan gi feil kanalvalg | LÃ¸pende vedlikehold og gode mekanismer for oppdatering |
| Teknisk | Feil integrasjon kan gjÃ¸re at virksomheten hopper over registeroppslag eller bruker gamle data | Integrasjonstesting og tydelig innfÃ¸ringsveiledning |
| Avhengigheter | Produktet kan bli forvekslet med varslings- eller utsendingslÃ¸sninger | Klare avgrensninger i arkitektur og dokumentasjon |
| Brukeropplevelse | Innbyggere kan miste tillit dersom kontaktdata eller reservasjon ikke hÃ¥ndteres konsekvent | Bedre informasjon og korrekt etterlevelse hos virksomhetene |

## Kanaler
- Produktside: https://docs.digdir.no/docs/Kontaktregisteret/
- Overordnet dokumentasjon: https://docs.digdir.no/docs/Kontaktregisteret/krr_overordnet
- Samarbeidsportal: https://samarbeid.digdir.no/kontaktregisteret/dette-er-kontaktregisteret/110
- Ta i bruk: https://samarbeid.digdir.no/kontaktregisteret/ta-i-bruk-kontaktregisteret/95
- Retningslinjer: https://samarbeid.digdir.no/kontaktregisteret/retningslinjer-bruk-av-kontakt-og-reservasjonsregisteret/143
- Kostnadsmodell: https://samarbeid.digdir.no/kontaktregisteret/kostnadsmodell-kontaktregisteret/577

## Plattform
Kontakt- og reservasjonsregisteret er en nasjonal registertjeneste som gir oppslag mot et felles datagrunnlag for kontaktinformasjon og reservasjon.

**Fakta:** Digdir Docs beskriver bÃ¥de teknisk bruk og overordnet funksjon, og Samarbeidsportalen beskriver ta-i-bruk-lÃ¸p, retningslinjer og kostnadsmodell.

**Ikke offentlig dokumentert i brukte kilder:** Full runtime-arkitektur, detaljert driftsoppsett og konkret infrastrukturnivÃ¥.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet er laget for Ã¥ vÃ¦re en felles kilde som mange andre lÃ¸sninger bygger pÃ¥.
- Det er sÃ¦rlig relevant nÃ¥r behovet er korrekt kontaktgrunnlag og reservasjonskontroll fÃ¸r digital kommunikasjon.
- Det er mindre relevant dersom behovet egentlig er selve utsendingen, postkassen eller varslingskanalen.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at kontaktopplysninger og reservasjonsstatus tilbys som felles grunnlag for mange virksomheter.
- **P5: Del og gjenbruk lÃ¸sninger** styrkes fordi offentlig sektor kan bygge pÃ¥ samme register i stedet for lokale kopier og sÃ¦rordninger.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** stÃ¸ttes ved at reservasjon og kontaktdata hÃ¥ndteres mer konsistent og forutsigbart.

## Finansiering
- **Fakta:** Samarbeidsportalen har en egen kostnadsmodell for Kontakt- og reservasjonsregisteret.
- **Fakta:** Samarbeidsportalen beskriver at bruk av registeret er kostnadsfritt, mens virksomhetene dekker egne kostnader til integrasjon og innfÃ¸ring.
- **Deduksjon:** Finansieringsmodellen er derfor rettet mot felles nasjonal forvaltning av registeret, kombinert med lokale innfÃ¸ringskostnader hos brukerne.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | Digdir Docs og Samarbeidsportalen |
| Driftsansvar | Ikke eksplisitt navngitt i brukte offentlige kilder | Offentlige kilder beskriver ikke detaljert leverandÃ¸r- eller driftsmodell |
| Budsjett- og kostnadsmodell | Digdir forvalter registeret, med publisert kostnadsmodell | Samarbeidsportalen |
| Styringsmodell | Del av Digdirs portefÃ¸lje for digital kommunikasjon | Samarbeidsportalen |

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
- Kapabilitetslisten er redusert til de direkte funksjonene registeret faktisk leverer, og indirekte koblinger til varsling, identifisering og andre lÃ¸sninger er tatt ut.
- Produktet beskrives tydeligere som grunndatakilde og beslutningsgrunnlag for kanalvalg, ikke som selve kommunikasjonslÃ¸sningen.
- Finansieringsfeltet bygger nÃ¥ pÃ¥ publisert kostnadsmodell og avklaringen om at bruk er kostnadsfri, mens integrasjon mÃ¥ dekkes lokalt.

### Tekstlige forbedringer
- Dokumentet starter ikke lenger med mÃ¥lgruppelinje, og `Ressurs ID` er skrevet uten parentesforklaring.
- Hovedfunksjoner og avgrensning gjÃ¸r det tydeligere nÃ¥r Kontakt- og reservasjonsregisteret er riktig produkt for gjenbruk.
- Beskrivelsen bruker mer aktiv og mÃ¥lrettet sprÃ¥k for nasjonal arkitektur, i stedet for Ã¥ liste opp tilgrensende produkter og funksjoner.

