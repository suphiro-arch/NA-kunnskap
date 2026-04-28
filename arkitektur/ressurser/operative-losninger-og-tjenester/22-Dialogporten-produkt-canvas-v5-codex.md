# Produkt-canvas: Dialogporten

## Navn
Dialogporten

## Ressurs ID
DIGDIR-020

## Status/Livsfase
**Produksjon** - etablert fellesløsning for representasjon av dialoger med aktiv videreutvikling og pågående migrering av historiske data.

**Fakta:** Offisiell dokumentasjon beskriver Dialogporten som et felles API og metadata-lager for digitale dialoger. Produktet brukes for Altinn 3 og andre digitale tjenesteplattformer, og historiske data migreres fortsatt inn per 26. mars 2026.

## Modenhet
**Middels til høy funksjonell modenhet** - kjernefunksjonene er etablerte, men totalbildet påvirkes fortsatt av migrering og videre innføring:
- Produktet har etablert API-er, GraphQL, brukerhåndbøker og dialogmodell.
- Løsningen brukes som representasjonslag både for Altinn-baserte og andre digitale tjenesteplattformer.
- Dokumentasjonen viser fortsatt aktiv utvikling rundt arbeidsflate og migrering av historiske data.

**Deduksjon:** Dialogporten er moden som felles representasjonslag for dialoger, men ikke ferdig som komplett historikklager eller som full erstatning for alle eldre presentasjonsflater ennå.

## Kort beskrivelse
Dialogporten er Altinns felles representasjons- og samhandlingslag for digitale dialoger. Produktet gjør meldinger og dialoger fra ulike tjenesteplattformer tilgjengelige i et felles format, slik at sluttbrukersystemer, arbeidsflater og portaler kan presentere den samme dialogen på en konsistent måte.

Produktet er mer enn et teknisk API. Dokumentasjonen viser at Dialogporten også fungerer som et felles metadata-lager og brukerrettet dialogmodell, med kobling til arbeidsflate, sluttbrukersystemer og tjenesteplattformer som skriver til dialogene. Samtidig lagrer ikke Dialogporten selve faginnholdet eller vedleggene; den holder orden på representasjonen, statusen og brukerrelevant metadata rundt dialogen.

## Kapabiliteter
- **Datautveksling og integrasjon: Bruke data fra andre** gir sluttbrukersystemer og portaler tilgang til dialogdata gjennom standardiserte API-er.
- **Datautveksling og integrasjon: Hendelsesdrevet** bruker hendelser og abonnementer for å oppdage endringer uten kontinuerlig polling.
- **Sluttbrukertjenester: Sammenhengende tjenester** gjør dialoger fra flere plattformer tilgjengelige i samme representasjon og brukerreise.
- **Tillit: Autentisering** støtter sluttbruker- og systemtilgang gjennom ID-porten og Maskinporten.
- **Tillit: Tilgangskontroll** bygger på Altinn Autorisasjon, autoriserte parter og tjenesteressurser.
- **Tjenesteutvikling: Integrerbare tjenester** gir tjenesteeiere og plattformer et felles mønster for å eksponere dialoger.

## Produktmål
**Primærkilder:** Dialogportens hovedside, «Om Dialogporten», «Hva får du?» og status for migrering.

Dokumenterte mål:
- Gjøre meldinger og dialoger fra Altinn 3 og andre digitale tjenesteplattformer tilgjengelige i et felles format.
- Forenkle integrasjoner på tvers av plattformer gjennom felles representasjon, API-er og metadata.
- Gjøre det enklere for sluttbrukere å holde oversikt over kommunikasjon med offentlige aktører.
- Migrere gamle data fra Altinn 2 og Altinn 3 til Dialogporten.

Operative mål utledet fra de samme kildene:
- Redusere behovet for plattformspesifikke integrasjoner hos sluttbrukersystemer.
- Skille representasjon av dialog fra underliggende tjenestelogikk og lagring av faginnhold.
- Gjøre det mulig å bruke samme dialogmodell i arbeidsflate og i andre sluttbrukersystemer.

**Deduksjon:** Produktet har også et tydelig standardiseringsmål ved å gjøre dialog til et eget felles lag på tvers av tjenesteplattformer.

## Brukerbehov
- Tjenesteeiere trenger en felles måte å eksponere dialoger og meldinger på uten å bygge egne portalmodeller.
- Sluttbrukersystemer trenger et stabilt og standardisert format for oppslag, detaljer og endringsdeteksjon.
- Sluttbrukere trenger samlet oversikt over kommunikasjon fra flere offentlige aktører.
- Integrasjonsteam trenger API-er, GraphQL og hendelser som kan brukes i egne arbeidsflater og portaler.
- Forvaltningsmiljøer trenger en kontrollert migreringsmodell for historiske data.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige tjenesteeiere | Eksponere dialoger i felles format | Dialoger fra Altinn Studio og andre plattformer | Reduserer behov for egne representasjonsmodeller |
| Sluttbrukersystem-leverandører | Hente dialoger og følge endringer | Integrasjon i arbeidsflater og sluttbrukersystemer | Felles format gjør integrasjon enklere på tvers av plattform |
| Sluttbrukere | Få oversikt over kommunikasjon | Lesing, oppfølging og historikk | Samme dialog kan vises i flere flater |
| Arkitektur- og integrasjonsteam | Bruke standardiserte API-er og hendelser | Integrasjon, overvåking og sammenhengende tjenester | Hendelser reduserer polling |
| Migrerings- og forvaltningsmiljøer | Håndtere historiske data og synkronisering | Overgang fra Altinn 2 til nyere løsninger | Viktig så lenge historiske data migreres i faser |

## Hovedfunksjoner
Dialogporten tilbyr først en felles dialogmodell som representerer pågående eller fullført digital kommunikasjon mellom tjenesteeier og mottaker. Dokumentasjonen beskriver dette som et metadata-lager og en representasjon av dialogens tilstand, med opplysninger som avsender, mottaker, tittel, sammendrag, status, aktivitetshistorikk og tilgjengelige handlinger. Dette gjør produktet relevant når behovet er å vise og følge opp dialoger på tvers av plattformer, ikke når behovet er å lagre hele innholdet eller styre faglogikken i tjenesten.

Produktet gir også en felles integrasjonsflate for oppslag og synkronisering. Sluttbrukersystemer og arbeidsflater kan bruke API-er og GraphQL for å søke, lese og følge endringer i dialoger. Dokumentasjonen viser at endringer i dialoger genererer hendelser som autoriserte parter kan abonnere på. Dermed fungerer Dialogporten ikke bare som et passivt visningslag, men som et standardisert samhandlingslag for dialogdata.

En viktig avgrensning er at Dialogporten i hovedsak er skrivebeskyttet for sluttbrukere. Det er tjenesteplattformene som skriver til dialogen på vegne av tjenesteeiere, mens sluttbrukere hovedsakelig leser, organiserer og følger opp dialogene gjennom arbeidsflate eller andre sluttbrukersystemer. Selve faginnholdet, som skjema, vedlegg og brødtekst, ligger fortsatt i underliggende tjenesteplattformer og refereres inn i dialogen gjennom lenker og metadata.

Dialogporten har også en tydelig rolle i Altinns modernisering av arbeidsflate og meldingspresentasjon. Produktet brukes automatisk for Altinn Apps og Altinn Melding, og dokumentasjonen viser at samme modell skal kunne brukes av andre tjenesteplattformer. Produktet er derfor riktig når behovet gjelder felles dialogrepresentasjon og eksponering, men ikke når behovet gjelder selve meldingsinnholdet, varsling eller autorisasjonsforvaltning som egne produkter.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Felles representasjon av dialoger og meldinger | Full forretningslogikk i hver sektortjeneste |
| API- og hendelseslag for oppslag og synkronisering | Lagring av hele faginnholdet i meldinger, skjema og vedlegg |
| Samspill med arbeidsflate og sluttbrukersystemer | Lokal saksbehandling i avsenders fagsystem |
| Migrering og livesynkronisering av dialogrelaterte metadata | Full erstatning for alle meldings- eller appprodukter |
| Tillits- og autorisasjonskoblinger for korrekt tilgang | Selvstendig identitets- og autorisasjonsforvaltning utenfor Altinn |
### Typiske brukssituasjoner (generisk)
- Sluttbrukersystem eller arbeidsflate trenger felles tilgang til dialoger fra mange tjenesteplattformer uten separate integrasjoner mot hver.
- Tjenesteeier vil gjøre sin tjeneste synlig i innbyggerens eller virksomhetens arbeidsflate.
- Integrasjon mellom tjenesteplattform og sluttbrukersystem trenger en standardisert dialogmodell med hendelser og API.
- System trenger å abonnere på statusendringer i dialoger på tvers av tjenester.

### Når Dialogporten normalt ikke er førstevalg
- Når behovet kun er enkel varsling via e-post eller SMS – da er Altinn Varsling mer relevant.
- Når behovet er overføring av store filer – da er Altinn Formidling mer relevant.
- Når behovet er å produsere meldingsinnhold og skrive til dialoger – da er Altinn Melding eller Altinn Apps mer relevant, siden Dialogporten er skrivebeskyttet for sluttbrukere.
- Når tjenesteplattformen ikke er koblet til Dialogporten og det ikke er planer om det.

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-26):**
- Livesynkronisering viser nye endringer i Dialogporten.
- Historiske meldinger og appinstanser var per 24. februar 2026 migrert tilbake til 1. januar 2024.
- Neste generasjon av Altinn Arbeidsflate er fortsatt under utvikling.

**Deduksjon:** Den viktigste videreutviklingen er fortsatt å gjøre datagrunnlaget mer komplett og å videreutvikle samspillet mellom Dialogporten og arbeidsflate/sluttbrukersystemer.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere
- Reduserer behovet for plattformspesifikke brukerrepresentasjoner av dialog.
- Gjør det lettere å eksponere egne tjenester i arbeidsflate og eksterne sluttbrukersystemer.

### For sluttbrukersystemer
- Gir ett felles format for digitale dialoger og meldinger på tvers av plattformer.
- Reduserer integrasjonskostnader og gjør endringsdeteksjon enklere.

### For brukere og offentlig sektor
- Gir bedre oversikt over kommunikasjon med offentlige aktører.
- Reduserer behovet for flere kopier av sensitiv informasjon ved at innhold kan bli liggende nær kilden.
- Understøtter mer sammenhengende tjenester på tvers av etater og plattformer.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Historiske data og tilgangsregler kan tolkes ulikt mellom gamle og nye løsninger | Tydelige migreringsregler, autorisasjonsmodell og sporbarhet |
| Teknisk | Ufullstendig historikk eller migreringsfeil kan gi mangelfull dialogoversikt | Fasevis migrering, synlig status og kontroll av datakilder |
| Sikkerhet | Feil i autoriserte parter eller tokens kan gi feil tilgang til dialogdata | Sterk autentisering, Altinn Autorisasjon og minste privilegium |
| Forvaltning | Mange kilder og plattformer gjør felles representasjon krevende å forvalte | Tydelige standarder, referansemodeller og koordinert produktforvaltning |
| Brukeropplevelse | Ulik kompletthet mellom ny og historisk data kan skape forvirring hos sluttbruker | Åpen statusinformasjon og gradvis forbedring av historikkgrunnlaget |

## Kanaler
- Produktside: https://docs.altinn.studio/nb/dialogporten/
- Om Dialogporten: https://docs.altinn.studio/nb/dialogporten/about-dialogporten/
- Hva får du?: https://docs.altinn.studio/nb/dialogporten/what-do-you-get/
- Status migrering: https://docs.altinn.studio/nb/dialogporten/status-migration/
- OpenAPI: https://docs.altinn.studio/nb/dialogporten/reference/openapi/
- GraphQL: https://docs.altinn.studio/nb/dialogporten/reference/graphql/

## Plattform
Felles dialoglag i Altinn-porteføljen med API-er, GraphQL, hendelser og integrasjon mot arbeidsflate og sluttbrukersystemer.

**Fakta:** Dialogporten er integrert med Altinn Autorisasjon, Maskinporten, ID-porten og Altinn Events, og kan brukes både av Altinn-plattformen og andre digitale tjenesteplattformer. Arbeidsflate bruker Dialogportens sluttbruker-API-er for å søke etter og vise dialoger.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur, hostingdetaljer og intern plattformfordeling mellom komponenter.

## Gjenbruk
**Høy gjenbruksverdi:**
- Felles dialogformat reduserer behovet for proprietære integrasjoner.
- Samme dialog kan eksponeres i flere arbeidsflater uten å redefinere modellen.
- Hendelser og standardiserte API-er gjør løsningen gjenbrukbar både for nye og eksisterende tjenester.


### Vanlige kombinasjoner med andre produkter
- **Altinn Melding** – alle meldinger i Altinn Melding representeres automatisk som dialoger i Dialogporten.
- **Altinn Apps** – apper eksponeres via Dialogporten slik at brukerne ser dem i sin arbeidsflate.
- **Altinn Varsling** – varsler sendes parallelt med at dialog opprettes eller oppdateres.
- **Altinn Autorisasjon** – styrer hvem som har tilgang til å se og behandle dialoger.

**Kildekode:** Åpen kildekode. Lisens: MIT. Kildekode: [github.com/Altinn/dialogporten](https://github.com/Altinn/dialogporten).

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** gjør dialogmetadata tilgjengelig på tvers av løsninger.
- **P5: Del og gjenbruk løsninger** etablerer et felles representasjonslag i stedet for mange lokale varianter.
- **P6: Lag digitale løsninger som støtter samhandling** kobler sammen ulike plattformer gjennom felles format og hendelser.
- **P7: Sørg for tillit til oppgaveløsningen** bygger på Altinn Autorisasjon, ID-porten og Maskinporten.

## Finansiering
- Dialogporten fremstår som del av Altinn-porteføljen under Digdir.
- **Ikke offentlig dokumentert:** Detaljert finansieringsmodell eller separat kostnadsfordeling for produktet.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Altinn-forvaltningen i Digdir | Offisiell dokumentasjon under Altinn Docs |
| Driftsansvar | Altinns forvaltnings- og driftsmiljø | Produktet er dokumentert som del av Altinn |
| Budsjettansvar | Ikke offentlig spesifisert i detalj | Ingen offentlig kostnadsmodell i brukte kilder |
| Styringsmodell | Produktforvaltning i Altinn-porteføljen med sterk kobling til migrering og samhandling | Dokumentert migrerings- og integrasjonsfokus |

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
- Produktbredden er tydeligere beskrevet som både metadata-lager, representasjonslag og integrasjonsflate.
- Dokumentasjonen om dialogmodell, arbeidsflate og hva som faktisk lagres i Dialogporten er brukt mer eksplisitt i analysen.
- Veikart og status er oppdatert mot nyere migreringsinformasjon kontrollert 26. mars 2026.

### Tekstlige forbedringer
- Dokumentet følger nå oppdatert canvas-struktur uten egen målgruppelinje.
- Hovedfunksjoner er skrevet om til forklarende avsnitt i stedet for punktliste.
- Avgrensningen mot Melding, arbeidsflate og underliggende tjenesteplattformer er gjort tydeligere.



