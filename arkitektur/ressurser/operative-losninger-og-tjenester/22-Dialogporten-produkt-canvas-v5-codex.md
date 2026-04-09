# Produkt-canvas: Dialogporten

## Navn
Dialogporten

## Ressurs ID
DIGDIR-020

## Status/Livsfase
**Produksjon** - etablert felleslÃ¸sning for representasjon av dialoger med aktiv videreutvikling og pÃ¥gÃ¥ende migrering av historiske data.

**Fakta:** Offisiell dokumentasjon beskriver Dialogporten som et felles API og metadata-lager for digitale dialoger. Produktet brukes for Altinn 3 og andre digitale tjenesteplattformer, og historiske data migreres fortsatt inn per 26. mars 2026.

## Modenhet
**Middels til hÃ¸y funksjonell modenhet** - kjernefunksjonene er etablerte, men totalbildet pÃ¥virkes fortsatt av migrering og videre innfÃ¸ring:
- Produktet har etablert API-er, GraphQL, brukerhÃ¥ndbÃ¸ker og dialogmodell.
- LÃ¸sningen brukes som representasjonslag bÃ¥de for Altinn-baserte og andre digitale tjenesteplattformer.
- Dokumentasjonen viser fortsatt aktiv utvikling rundt arbeidsflate og migrering av historiske data.

**Deduksjon:** Dialogporten er moden som felles representasjonslag for dialoger, men ikke ferdig som komplett historikklager eller som full erstatning for alle eldre presentasjonsflater ennÃ¥.

## Kort beskrivelse
Dialogporten er Altinns felles representasjons- og samhandlingslag for digitale dialoger. Produktet gjÃ¸r meldinger og dialoger fra ulike tjenesteplattformer tilgjengelige i et felles format, slik at sluttbrukersystemer, arbeidsflater og portaler kan presentere den samme dialogen pÃ¥ en konsistent mÃ¥te.

Produktet er mer enn et teknisk API. Dokumentasjonen viser at Dialogporten ogsÃ¥ fungerer som et felles metadata-lager og brukerrettet dialogmodell, med kobling til arbeidsflate, sluttbrukersystemer og tjenesteplattformer som skriver til dialogene. Samtidig lagrer ikke Dialogporten selve faginnholdet eller vedleggene; den holder orden pÃ¥ representasjonen, statusen og brukerrelevant metadata rundt dialogen.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** gir sluttbrukersystemer og portaler tilgang til dialogdata gjennom standardiserte API-er.
- **Datautveksling og integrasjon: Hendelsesdrevet** bruker hendelser og abonnementer for Ã¥ oppdage endringer uten kontinuerlig polling.
- **Sluttbrukertjenester: Sammenhengende tjenester** gjÃ¸r dialoger fra flere plattformer tilgjengelige i samme representasjon og brukerreise.
- **Tillit: Autentisering** stÃ¸tter sluttbruker- og systemtilgang gjennom ID-porten og Maskinporten.
- **Tillit: Tilgangskontroll** bygger pÃ¥ Altinn Autorisasjon, autoriserte parter og tjenesteressurser.
- **Tjenesteutvikling: Integrerbare tjenester** gir tjenesteeiere og plattformer et felles mÃ¸nster for Ã¥ eksponere dialoger.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Dialogportens hovedside, Â«Om DialogportenÂ», Â«Hva fÃ¥r du?Â» og status for migrering.

Dokumenterte mÃ¥l:
- GjÃ¸re meldinger og dialoger fra Altinn 3 og andre digitale tjenesteplattformer tilgjengelige i et felles format.
- Forenkle integrasjoner pÃ¥ tvers av plattformer gjennom felles representasjon, API-er og metadata.
- GjÃ¸re det enklere for sluttbrukere Ã¥ holde oversikt over kommunikasjon med offentlige aktÃ¸rer.
- Migrere gamle data fra Altinn 2 og Altinn 3 til Dialogporten.

Operative mÃ¥l utledet fra de samme kildene:
- Redusere behovet for plattformspesifikke integrasjoner hos sluttbrukersystemer.
- Skille representasjon av dialog fra underliggende tjenestelogikk og lagring av faginnhold.
- GjÃ¸re det mulig Ã¥ bruke samme dialogmodell i arbeidsflate og i andre sluttbrukersystemer.

**Deduksjon:** Produktet har ogsÃ¥ et tydelig standardiseringsmÃ¥l ved Ã¥ gjÃ¸re dialog til et eget felles lag pÃ¥ tvers av tjenesteplattformer.

## Brukerbehov
- Tjenesteeiere trenger en felles mÃ¥te Ã¥ eksponere dialoger og meldinger pÃ¥ uten Ã¥ bygge egne portalmodeller.
- Sluttbrukersystemer trenger et stabilt og standardisert format for oppslag, detaljer og endringsdeteksjon.
- Sluttbrukere trenger samlet oversikt over kommunikasjon fra flere offentlige aktÃ¸rer.
- Integrasjonsteam trenger API-er, GraphQL og hendelser som kan brukes i egne arbeidsflater og portaler.
- ForvaltningsmiljÃ¸er trenger en kontrollert migreringsmodell for historiske data.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige tjenesteeiere | Eksponere dialoger i felles format | Dialoger fra Altinn Studio og andre plattformer | Reduserer behov for egne representasjonsmodeller |
| Sluttbrukersystem-leverandÃ¸rer | Hente dialoger og fÃ¸lge endringer | Integrasjon i arbeidsflater og sluttbrukersystemer | Felles format gjÃ¸r integrasjon enklere pÃ¥ tvers av plattform |
| Sluttbrukere | FÃ¥ oversikt over kommunikasjon | Lesing, oppfÃ¸lging og historikk | Samme dialog kan vises i flere flater |
| Arkitektur- og integrasjonsteam | Bruke standardiserte API-er og hendelser | Integrasjon, overvÃ¥king og sammenhengende tjenester | Hendelser reduserer polling |
| Migrerings- og forvaltningsmiljÃ¸er | HÃ¥ndtere historiske data og synkronisering | Overgang fra Altinn 2 til nyere lÃ¸sninger | Viktig sÃ¥ lenge historiske data migreres i faser |

## Hovedfunksjoner
Dialogporten tilbyr fÃ¸rst en felles dialogmodell som representerer pÃ¥gÃ¥ende eller fullfÃ¸rt digital kommunikasjon mellom tjenesteeier og mottaker. Dokumentasjonen beskriver dette som et metadata-lager og en representasjon av dialogens tilstand, med opplysninger som avsender, mottaker, tittel, sammendrag, status, aktivitetshistorikk og tilgjengelige handlinger. Dette gjÃ¸r produktet relevant nÃ¥r behovet er Ã¥ vise og fÃ¸lge opp dialoger pÃ¥ tvers av plattformer, ikke nÃ¥r behovet er Ã¥ lagre hele innholdet eller styre faglogikken i tjenesten.

Produktet gir ogsÃ¥ en felles integrasjonsflate for oppslag og synkronisering. Sluttbrukersystemer og arbeidsflater kan bruke API-er og GraphQL for Ã¥ sÃ¸ke, lese og fÃ¸lge endringer i dialoger. Dokumentasjonen viser at endringer i dialoger genererer hendelser som autoriserte parter kan abonnere pÃ¥. Dermed fungerer Dialogporten ikke bare som et passivt visningslag, men som et standardisert samhandlingslag for dialogdata.

En viktig avgrensning er at Dialogporten i hovedsak er skrivebeskyttet for sluttbrukere. Det er tjenesteplattformene som skriver til dialogen pÃ¥ vegne av tjenesteeiere, mens sluttbrukere hovedsakelig leser, organiserer og fÃ¸lger opp dialogene gjennom arbeidsflate eller andre sluttbrukersystemer. Selve faginnholdet, som skjema, vedlegg og brÃ¸dtekst, ligger fortsatt i underliggende tjenesteplattformer og refereres inn i dialogen gjennom lenker og metadata.

Dialogporten har ogsÃ¥ en tydelig rolle i Altinns modernisering av arbeidsflate og meldingspresentasjon. Produktet brukes automatisk for Altinn Apps og Altinn Melding, og dokumentasjonen viser at samme modell skal kunne brukes av andre tjenesteplattformer. Produktet er derfor riktig nÃ¥r behovet gjelder felles dialogrepresentasjon og eksponering, men ikke nÃ¥r behovet gjelder selve meldingsinnholdet, varsling eller autorisasjonsforvaltning som egne produkter.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Felles representasjon av dialoger og meldinger | Full forretningslogikk i hver sektortjeneste |
| API- og hendelseslag for oppslag og synkronisering | Lagring av hele faginnholdet i meldinger, skjema og vedlegg |
| Samspill med arbeidsflate og sluttbrukersystemer | Lokal saksbehandling i avsenders fagsystem |
| Migrering og livesynkronisering av dialogrelaterte metadata | Full erstatning for alle meldings- eller appprodukter |
| Tillits- og autorisasjonskoblinger for korrekt tilgang | Selvstendig identitets- og autorisasjonsforvaltning utenfor Altinn |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-26):**
- Livesynkronisering viser nye endringer i Dialogporten.
- Historiske meldinger og appinstanser var per 24. februar 2026 migrert tilbake til 1. januar 2024.
- Neste generasjon av Altinn Arbeidsflate er fortsatt under utvikling.

**Deduksjon:** Den viktigste videreutviklingen er fortsatt Ã¥ gjÃ¸re datagrunnlaget mer komplett og Ã¥ videreutvikle samspillet mellom Dialogporten og arbeidsflate/sluttbrukersystemer.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere
- Reduserer behovet for plattformspesifikke brukerrepresentasjoner av dialog.
- GjÃ¸r det lettere Ã¥ eksponere egne tjenester i arbeidsflate og eksterne sluttbrukersystemer.

### For sluttbrukersystemer
- Gir ett felles format for digitale dialoger og meldinger pÃ¥ tvers av plattformer.
- Reduserer integrasjonskostnader og gjÃ¸r endringsdeteksjon enklere.

### For brukere og offentlig sektor
- Gir bedre oversikt over kommunikasjon med offentlige aktÃ¸rer.
- Reduserer behovet for flere kopier av sensitiv informasjon ved at innhold kan bli liggende nÃ¦r kilden.
- UnderstÃ¸tter mer sammenhengende tjenester pÃ¥ tvers av etater og plattformer.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Historiske data og tilgangsregler kan tolkes ulikt mellom gamle og nye lÃ¸sninger | Tydelige migreringsregler, autorisasjonsmodell og sporbarhet |
| Teknisk | Ufullstendig historikk eller migreringsfeil kan gi mangelfull dialogoversikt | Fasevis migrering, synlig status og kontroll av datakilder |
| Sikkerhet | Feil i autoriserte parter eller tokens kan gi feil tilgang til dialogdata | Sterk autentisering, Altinn Autorisasjon og minste privilegium |
| Forvaltning | Mange kilder og plattformer gjÃ¸r felles representasjon krevende Ã¥ forvalte | Tydelige standarder, referansemodeller og koordinert produktforvaltning |
| Brukeropplevelse | Ulik kompletthet mellom ny og historisk data kan skape forvirring hos sluttbruker | Ã…pen statusinformasjon og gradvis forbedring av historikkgrunnlaget |

## Kanaler
- Produktside: https://docs.altinn.studio/nb/dialogporten/
- Om Dialogporten: https://docs.altinn.studio/nb/dialogporten/about-dialogporten/
- Hva fÃ¥r du?: https://docs.altinn.studio/nb/dialogporten/what-do-you-get/
- Status migrering: https://docs.altinn.studio/nb/dialogporten/status-migration/
- OpenAPI: https://docs.altinn.studio/nb/dialogporten/reference/openapi/
- GraphQL: https://docs.altinn.studio/nb/dialogporten/reference/graphql/

## Plattform
Felles dialoglag i Altinn-portefÃ¸ljen med API-er, GraphQL, hendelser og integrasjon mot arbeidsflate og sluttbrukersystemer.

**Fakta:** Dialogporten er integrert med Altinn Autorisasjon, Maskinporten, ID-porten og Altinn Events, og kan brukes bÃ¥de av Altinn-plattformen og andre digitale tjenesteplattformer. Arbeidsflate bruker Dialogportens sluttbruker-API-er for Ã¥ sÃ¸ke etter og vise dialoger.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur, hostingdetaljer og intern plattformfordeling mellom komponenter.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Felles dialogformat reduserer behovet for proprietÃ¦re integrasjoner.
- Samme dialog kan eksponeres i flere arbeidsflater uten Ã¥ redefinere modellen.
- Hendelser og standardiserte API-er gjÃ¸r lÃ¸sningen gjenbrukbar bÃ¥de for nye og eksisterende tjenester.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** gjÃ¸r dialogmetadata tilgjengelig pÃ¥ tvers av lÃ¸sninger.
- **P5: Del og gjenbruk lÃ¸sninger** etablerer et felles representasjonslag i stedet for mange lokale varianter.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** kobler sammen ulike plattformer gjennom felles format og hendelser.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** bygger pÃ¥ Altinn Autorisasjon, ID-porten og Maskinporten.

## Finansiering
- Dialogporten fremstÃ¥r som del av Altinn-portefÃ¸ljen under Digdir.
- **Ikke offentlig dokumentert:** Detaljert finansieringsmodell eller separat kostnadsfordeling for produktet.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Altinn-forvaltningen i Digdir | Offisiell dokumentasjon under Altinn Docs |
| Driftsansvar | Altinns forvaltnings- og driftsmiljÃ¸ | Produktet er dokumentert som del av Altinn |
| Budsjettansvar | Ikke offentlig spesifisert i detalj | Ingen offentlig kostnadsmodell i brukte kilder |
| Styringsmodell | Produktforvaltning i Altinn-portefÃ¸ljen med sterk kobling til migrering og samhandling | Dokumentert migrerings- og integrasjonsfokus |

## Lenke til dokumentasjon
- https://docs.altinn.studio/nb/dialogporten/
- https://docs.altinn.studio/nb/dialogporten/about-dialogporten/
- https://docs.altinn.studio/nb/dialogporten/what-do-you-get/
- https://docs.altinn.studio/nb/dialogporten/status-migration/
- https://docs.altinn.studio/nb/dialogporten/reference/openapi/
- https://docs.altinn.studio/nb/dialogporten/reference/graphql/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/22-Dialogporten-produkt-canvas-v4-codex.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/about-dialogporten/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/what-do-you-get/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/status-migration/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/reference/openapi/ (kontrollert 2026-03-26)
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/reference/graphql/ (kontrollert 2026-03-26)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Produktbredden er tydeligere beskrevet som bÃ¥de metadata-lager, representasjonslag og integrasjonsflate.
- Dokumentasjonen om dialogmodell, arbeidsflate og hva som faktisk lagres i Dialogporten er brukt mer eksplisitt i analysen.
- Veikart og status er oppdatert mot nyere migreringsinformasjon kontrollert 26. mars 2026.

### Tekstlige forbedringer
- Dokumentet fÃ¸lger nÃ¥ oppdatert canvas-struktur uten egen mÃ¥lgruppelinje.
- Hovedfunksjoner er skrevet om til forklarende avsnitt i stedet for punktliste.
- Avgrensningen mot Melding, arbeidsflate og underliggende tjenesteplattformer er gjort tydeligere.

