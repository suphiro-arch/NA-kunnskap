# Produkt-canvas: Dialogporten

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Dialogporten

## Ressurs ID
22 (Produktliste NA-kunnskap).

## Status/Livsfase
**Produksjon** - etablert fellesløsning med aktiv videreutvikling og pågående migrering av historiske data.

**Fakta:** Dialogporten gjør meldinger og dialoger fra Altinn 3 og andre digitale tjenesteplattformer tilgjengelige i et felles format, og livesynkronisering av endringer er aktiv.

## Modenhet
**Middels til høy funksjonell modenhet** - kjernefunksjonen er etablert, men migreringen er fortsatt under utvikling:
- Dialogporten har etablert API-er, GraphQL, entitetsmodell og brukerhåndbøker.
- Løsningen brukes både for Altinn Studio, Altinn Melding og andre tjenesteplattformer.
- Historiske data fra Altinn 2 og eldre kilder migreres fortsatt i faser.

**Deduksjon:** Produktet er modent som felles representasjonslag for dialoger, men total modenhet påvirkes fortsatt av at hele historikken ikke er ferdig migrert.

## Kort beskrivelse
Dialogporten er Altinns felles representasjons- og samhandlingslag for digitale dialoger. Produktet gjør meldinger og dialoger fra ulike tjenesteplattformer tilgjengelige i et felles format, slik at sluttbrukersystemer, arbeidsflater og portaler kan presentere den samme dialogen på en konsistent måte.

## Kapabiliteter
- **Sluttbrukertjenester: Sammenhengende tjenester** gjør dialoger fra flere plattformer tilgjengelige i samme representasjon og brukerreise.
- **Datautveksling og integrasjon: Bruke data fra andre** gir sluttbrukersystemer og portaler tilgang til dialogdata gjennom standardiserte API-er.
- **Datautveksling og integrasjon: Hendelsesdrevet** bruker hendelser og abonnementer for å oppdage endringer uten kontinuerlig polling.
- **Tillit: Autentisering** støtter sluttbruker- og systemtilgang gjennom ID-porten og Maskinporten.
- **Tillit: Tilgangskontroll** bygger på Altinn Autorisasjon, autoriserte parter og tjenesteressurser.
- **Tjenesteutvikling: Integrerbare tjenester** gir tjenesteeiere og plattformer et felles mønster for å eksponere dialoger.
- **Samarbeid: Tjenesteforvaltning** gjør det mulig å samordne digital dialog på tvers av ulike plattformer og tjenesteeiere.

Grunnlag: Kapabilitetsnavn fra `index/capabilities.yaml`, vurdert mot funksjoner dokumentert i Dialogporten.

## Produktmål
**Primærkilder:** Dialogportens hovedside, `Hva får du?` og `Status migrering`.

Dokumenterte mål:
- Gjøre meldinger og dialoger fra Altinn 3 og andre digitale tjenesteplattformer tilgjengelige for sluttbrukersystemer i et felles format.
- Forenkle integrasjoner på tvers av plattformer gjennom felles representasjon og API-er.
- Gjøre det enklere for sluttbrukere å holde oversikt over kommunikasjon med offentlige aktører.
- Migrere gamle data fra Altinn 2 og Altinn 3 til Dialogporten.

Operative mål utledet fra de samme kildene:
- Redusere behovet for plattformspesifikke integrasjoner hos sluttbrukersystemer.
- Gjøre det mulig å bruke samme metadata og hendelser i arbeidsflate, portaler og eksterne sluttbrukersystemer.
- Synkronisere nye endringer og gradvis bygge opp historikk fra eldre løsninger.

**Deduksjon:** Dialogporten er også et viktig standardiseringsgrep for å skille brukerrepresentasjon av dialog fra underliggende tjenestelogikk og plattformvalg.

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
| Sluttbrukersystem-leverandører (EUS) | Hente dialoger og følge endringer | Integrasjon i arbeidsflater og sluttbrukersystemer | Felles format gjør integrasjon enklere på tvers av plattform |
| Sluttbrukere | Få oversikt over kommunikasjon | Lesing, oppfølging og historikk | Samme dialog kan vises i flere flater |
| Arkitektur- og integrasjonsteam | Bruke standardiserte API-er og hendelser | Integrasjon, overvåking og sammenhengende tjenester | Pub/sub reduserer polling |
| Migrerings- og forvaltningsmiljøer | Håndtere historiske data og synkronisering | Overgang fra Altinn 2 til nyere løsninger | Viktig så lenge historiske data migreres i faser |

## Hovedfunksjoner
### Primære funksjoner
- Dialogen som felles meta-representasjon av interaktive digitale dialogtjenester.
- API-er og GraphQL for søk, detaljer og oppdatering av dialoger.
- Integrasjon med Altinn Autorisasjon, Maskinporten og ID-porten.
- Integrasjon med Altinn Events for endringsdeteksjon og abonnementer.
- Front channel embeds og klientstøtte for presentasjon i brukerflater.
- Støtte for aktivitetslogg, sett-logg og relaterte dialogentiteter.
- Livesynkronisering av nye endringer og gradvis migrering av historiske data.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Felles representasjon av dialoger og meldinger | Full forretningslogikk i hver sektortjeneste |
| API- og hendelseslag for oppslag og synkronisering | Lokal saksbehandling i avsenders fagsystem |
| Samspill med arbeidsflate og sluttbrukersystemer | Full erstatning for alle meldings- eller appprodukter |
| Migrering og livesynkronisering av dialogrelaterte data | Hele historikken fra alle kilder i én ferdig levert fase |
| Tillits- og autorisasjonskoblinger for korrekt tilgang | Selvstendig identitets- og autorisasjonsforvaltning utenfor Altinn |

## Veikart over kommende funksjonalitet
**Fakta fra kilder (2026-03-10):**
- Livesynkronisering viser alle nye endringer i Dialogporten.
- Historiske meldinger og appinstanser var per 24. februar 2026 migrert tilbake til 1. januar 2024.
- Målbildet er å migrere historiske data videre gjennom 2026.

**Deduksjon:** Den viktigste videreutviklingen er fortsatt å gjøre datagrunnlaget mer komplett, samtidig som API- og integrasjonsmønstrene videreføres som felles standard.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere
- Reduserer behovet for plattformspesifikke brukerrepresentasjoner av dialog.
- Gjør det lettere å eksponere egne tjenester i arbeidsflate og eksterne sluttbrukersystemer.

### For sluttbrukersystemer
- Gir ett felles format for digitale dialoger og meldinger på tvers av plattformer.
- Reduserer integrasjonskostnader og gjør endringsdeteksjon enklere.

### For brukere og offentlig sektor
- Gir bedre oversikt over kommunikasjon med offentlige aktører.
- Reduserer behovet for flere kopier av sensitiv informasjon ved at data kan oppbevares nær kilden.
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
- Hva får du?: https://docs.altinn.studio/nb/dialogporten/what-do-you-get/
- Status migrering: https://docs.altinn.studio/nb/dialogporten/status-migration/
- OpenAPI: https://docs.altinn.studio/nb/dialogporten/reference/openapi/
- GraphQL: https://docs.altinn.studio/nb/dialogporten/reference/graphql/

## Plattform
Felles dialoglag i Altinn-porteføljen med API-er, GraphQL, hendelser og integrasjon mot arbeidsflate og sluttbrukersystemer.

**Fakta:** Dialogporten er integrert med Altinn Autorisasjon, Maskinporten, ID-porten og Altinn Events, og kan brukes både av Altinn Studio og andre digitale tjenesteplattformer.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsarkitektur, hostingdetaljer og intern plattformfordeling mellom komponenter.

## Gjenbruk
**Høy gjenbruksverdi:**
- Felles dialogformat reduserer behovet for proprietære integrasjoner.
- Samme dialog kan eksponeres i flere arbeidsflater uten å redefinere modellen.
- Hendelser og standardiserte API-er gjør løsningen gjenbrukbar både for nye og eksisterende tjenester.

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
- https://docs.altinn.studio/nb/dialogporten/what-do-you-get/
- https://docs.altinn.studio/nb/dialogporten/status-migration/
- https://docs.altinn.studio/nb/dialogporten/reference/openapi/
- https://docs.altinn.studio/nb/dialogporten/reference/graphql/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `results/Produktbeskrivelser/22-Dialogporten-produkt-canvas-v1-codex.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `index/capabilities.yaml`
- Lokal fil: `index/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/what-do-you-get/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/status-migration/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/reference/openapi/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/reference/graphql/ (hentet 2026-03-10)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Verifisert produktmål, funksjoner og migreringsstatus mot nyere Altinn-dokumentasjon.
- Lagt inn konkrete funn om livesynkronisering og historiske data tilbake til 1. januar 2024.
- Strammet inn påstander om scope og rolle i Altinn til det som er dokumentert offentlig.

### Tekstlige forbedringer
- Skrevet om produktet til en tydeligere, selvstendig beskrivelse for målgruppen.
- Innført full brukersegmentering, tydeligere kapabiliteter og mer presise risikoer.
- Knyttet verdiforslag og veikart nærmere til dokumentert migrerings- og samhandlingsrolle.