# Produkt-canvas: Dialogporten

MÃ¥lgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Dialogporten

## Ressurs ID
DIGDIR-020

## Status/Livsfase
**Produksjon** - etablert felleslÃ¸sning med aktiv videreutvikling og pÃ¥gÃ¥ende migrering av historiske data.

**Fakta:** Dialogporten gjÃ¸r meldinger og dialoger fra Altinn 3 og andre digitale tjenesteplattformer tilgjengelige i et felles format, og livesynkronisering av endringer er aktiv.

## Modenhet
**Middels til hÃ¸y funksjonell modenhet** - kjernefunksjonen er etablert, men migreringen er fortsatt under utvikling:
- Dialogporten har etablert API-er, GraphQL, entitetsmodell og brukerhÃ¥ndbÃ¸ker.
- LÃ¸sningen brukes bÃ¥de for Altinn Studio, Altinn Melding og andre tjenesteplattformer.
- Historiske data fra Altinn 2 og eldre kilder migreres fortsatt i faser.

**Deduksjon:** Produktet er modent som felles representasjonslag for dialoger, men total modenhet pÃ¥virkes fortsatt av at hele historikken ikke er ferdig migrert.

## Kort beskrivelse
Dialogporten er Altinns felles representasjons- og samhandlingslag for digitale dialoger. Produktet gjÃ¸r meldinger og dialoger fra ulike tjenesteplattformer tilgjengelige i et felles format, slik at sluttbrukersystemer, arbeidsflater og portaler kan presentere den samme dialogen pÃ¥ en konsistent mÃ¥te.

## Kapabiliteter
- **Sluttbrukertjenester: Sammenhengende tjenester** gjÃ¸r dialoger fra flere plattformer tilgjengelige i samme representasjon og brukerreise.
- **Datautveksling og integrasjon: Bruke data fra andre** gir sluttbrukersystemer og portaler tilgang til dialogdata gjennom standardiserte API-er.
- **Datautveksling og integrasjon: Hendelsesdrevet** bruker hendelser og abonnementer for Ã¥ oppdage endringer uten kontinuerlig polling.
- **Tillit: Autentisering** stÃ¸tter sluttbruker- og systemtilgang gjennom ID-porten og Maskinporten.
- **Tillit: Tilgangskontroll** bygger pÃ¥ Altinn Autorisasjon, autoriserte parter og tjenesteressurser.
- **Tjenesteutvikling: Integrerbare tjenester** gir tjenesteeiere og plattformer et felles mÃ¸nster for Ã¥ eksponere dialoger.
- **Samarbeid: Tjenesteforvaltning** gjÃ¸r det mulig Ã¥ samordne digital dialog pÃ¥ tvers av ulike plattformer og tjenesteeiere.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot funksjoner dokumentert i Dialogporten.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Dialogportens hovedside, `Hva fÃ¥r du?` og `Status migrering`.

Dokumenterte mÃ¥l:
- GjÃ¸re meldinger og dialoger fra Altinn 3 og andre digitale tjenesteplattformer tilgjengelige for sluttbrukersystemer i et felles format.
- Forenkle integrasjoner pÃ¥ tvers av plattformer gjennom felles representasjon og API-er.
- GjÃ¸re det enklere for sluttbrukere Ã¥ holde oversikt over kommunikasjon med offentlige aktÃ¸rer.
- Migrere gamle data fra Altinn 2 og Altinn 3 til Dialogporten.

Operative mÃ¥l utledet fra de samme kildene:
- Redusere behovet for plattformspesifikke integrasjoner hos sluttbrukersystemer.
- GjÃ¸re det mulig Ã¥ bruke samme metadata og hendelser i arbeidsflate, portaler og eksterne sluttbrukersystemer.
- Synkronisere nye endringer og gradvis bygge opp historikk fra eldre lÃ¸sninger.

**Deduksjon:** Dialogporten er ogsÃ¥ et viktig standardiseringsgrep for Ã¥ skille brukerrepresentasjon av dialog fra underliggende tjenestelogikk og plattformvalg.

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
| Sluttbrukersystem-leverandÃ¸rer (EUS) | Hente dialoger og fÃ¸lge endringer | Integrasjon i arbeidsflater og sluttbrukersystemer | Felles format gjÃ¸r integrasjon enklere pÃ¥ tvers av plattform |
| Sluttbrukere | FÃ¥ oversikt over kommunikasjon | Lesing, oppfÃ¸lging og historikk | Samme dialog kan vises i flere flater |
| Arkitektur- og integrasjonsteam | Bruke standardiserte API-er og hendelser | Integrasjon, overvÃ¥king og sammenhengende tjenester | Pub/sub reduserer polling |
| Migrerings- og forvaltningsmiljÃ¸er | HÃ¥ndtere historiske data og synkronisering | Overgang fra Altinn 2 til nyere lÃ¸sninger | Viktig sÃ¥ lenge historiske data migreres i faser |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
- Dialogen som felles meta-representasjon av interaktive digitale dialogtjenester.
- API-er og GraphQL for sÃ¸k, detaljer og oppdatering av dialoger.
- Integrasjon med Altinn Autorisasjon, Maskinporten og ID-porten.
- Integrasjon med Altinn Events for endringsdeteksjon og abonnementer.
- Front channel embeds og klientstÃ¸tte for presentasjon i brukerflater.
- StÃ¸tte for aktivitetslogg, sett-logg og relaterte dialogentiteter.
- Livesynkronisering av nye endringer og gradvis migrering av historiske data.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Felles representasjon av dialoger og meldinger | Full forretningslogikk i hver sektortjeneste |
| API- og hendelseslag for oppslag og synkronisering | Lokal saksbehandling i avsenders fagsystem |
| Samspill med arbeidsflate og sluttbrukersystemer | Full erstatning for alle meldings- eller appprodukter |
| Migrering og livesynkronisering av dialogrelaterte data | Hele historikken fra alle kilder i Ã©n ferdig levert fase |
| Tillits- og autorisasjonskoblinger for korrekt tilgang | Selvstendig identitets- og autorisasjonsforvaltning utenfor Altinn |

## Veikart over kommende funksjonalitet
**Fakta fra kilder (2026-03-10):**
- Livesynkronisering viser alle nye endringer i Dialogporten.
- Historiske meldinger og appinstanser var per 24. februar 2026 migrert tilbake til 1. januar 2024.
- MÃ¥lbildet er Ã¥ migrere historiske data videre gjennom 2026.

**Deduksjon:** Den viktigste videreutviklingen er fortsatt Ã¥ gjÃ¸re datagrunnlaget mer komplett, samtidig som API- og integrasjonsmÃ¸nstrene viderefÃ¸res som felles standard.

## Forretningsverdi/Verdiforslag
### For tjenesteeiere
- Reduserer behovet for plattformspesifikke brukerrepresentasjoner av dialog.
- GjÃ¸r det lettere Ã¥ eksponere egne tjenester i arbeidsflate og eksterne sluttbrukersystemer.

### For sluttbrukersystemer
- Gir ett felles format for digitale dialoger og meldinger pÃ¥ tvers av plattformer.
- Reduserer integrasjonskostnader og gjÃ¸r endringsdeteksjon enklere.

### For brukere og offentlig sektor
- Gir bedre oversikt over kommunikasjon med offentlige aktÃ¸rer.
- Reduserer behovet for flere kopier av sensitiv informasjon ved at data kan oppbevares nÃ¦r kilden.
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
- Hva fÃ¥r du?: https://docs.altinn.studio/nb/dialogporten/what-do-you-get/
- Status migrering: https://docs.altinn.studio/nb/dialogporten/status-migration/
- OpenAPI: https://docs.altinn.studio/nb/dialogporten/reference/openapi/
- GraphQL: https://docs.altinn.studio/nb/dialogporten/reference/graphql/

## Plattform
Felles dialoglag i Altinn-portefÃ¸ljen med API-er, GraphQL, hendelser og integrasjon mot arbeidsflate og sluttbrukersystemer.

**Fakta:** Dialogporten er integrert med Altinn Autorisasjon, Maskinporten, ID-porten og Altinn Events, og kan brukes bÃ¥de av Altinn Studio og andre digitale tjenesteplattformer.

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
- https://docs.altinn.studio/nb/dialogporten/what-do-you-get/
- https://docs.altinn.studio/nb/dialogporten/status-migration/
- https://docs.altinn.studio/nb/dialogporten/reference/openapi/
- https://docs.altinn.studio/nb/dialogporten/reference/graphql/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `results/Produktbeskrivelser/22-Dialogporten-produkt-canvas-v1-codex.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/what-do-you-get/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/status-migration/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/reference/openapi/ (hentet 2026-03-10)
- Nettkilde: https://docs.altinn.studio/nb/dialogporten/reference/graphql/ (hentet 2026-03-10)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Verifisert produktmÃ¥l, funksjoner og migreringsstatus mot nyere Altinn-dokumentasjon.
- Lagt inn konkrete funn om livesynkronisering og historiske data tilbake til 1. januar 2024.
- Strammet inn pÃ¥stander om scope og rolle i Altinn til det som er dokumentert offentlig.

### Tekstlige forbedringer
- Skrevet om produktet til en tydeligere, selvstendig beskrivelse for mÃ¥lgruppen.
- InnfÃ¸rt full brukersegmentering, tydeligere kapabiliteter og mer presise risikoer.
- Knyttet verdiforslag og veikart nÃ¦rmere til dokumentert migrerings- og samhandlingsrolle.