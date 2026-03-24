# Produkt-canvas: Altinn Portal

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn Portal

## Ressurs ID
21 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon, med pågående modernisering.

**Fakta:** Digdir beskriver at «Nye Altinn» (ny brukerflate/plattform) ble lansert 4. mars 2026 i beta, med gradvis overgang fra eksisterende løsninger fram til 19. juni 2026.

## Modenhet
Middels til høy, med todelt modenhetsbilde:
- Høy modenhet i etablert drift og brukeradopsjon i Altinns portalfunksjoner.
- Middels modenhet i nye portalnære funksjoner som fortsatt er i beta i mars 2026.
- Overgangsperioden fram til 19. juni 2026 innebærer samtidig bruk av gammel og ny arbeidsflate.

## Kort beskrivelse
Altinn Portal er den sentrale brukerinngangen til skjema, tjenester, innboks og tilgangsstyring i Altinn-økosystemet. Portalen knytter sammen sluttbrukeropplevelse og underliggende felleskomponenter, og støtter både innbygger- og virksomhetsrettet oppgaveløsning.

## Kapabiliteter
- **Sluttbrukertjenester: Sammenhengende tjenester**
  Portalen samler flere tjenester i én arbeidsflate med sammenhengende brukerreise.
- **Sluttbrukertjenester: Tjenestekjeder**
  Bruker kan bevege seg fra varsel/melding til konkret handling i tjeneste.
- **Tillit: Representasjon**
  Brukere kan opptre på vegne av virksomhet når rettigheter/roller er satt.
- **Tillit: Tilgangsstyring**
  Tilgang til innhold og handlinger styres av rolle, fullmakt og tilgangspakker.
- **Tillit: Sporbarhet og innsyn**
  Portalbruk må kunne følges opp ved innsyn, support og kontrollbehov.
- **Samarbeid: Tjenesteforvaltning**
  Felles portalflate muliggjør samordnet forvaltning for mange tjenesteeiere.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling**
  Portalen må ivareta trygg flyt mellom brukerflate, innboks og underliggende tjenester.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i Altinn-kilder.

## Produktmål
- Gi en samlet og brukervennlig inngang til offentlige digitale tjenester i Altinn.
- Redusere friksjon ved å samle søk, skjema/tjenester, innboks og tilgangsstyring.
- Understøtte sikker representasjon for virksomhetsbrukere.
- Gjennomføre kontrollert modernisering fra gammel til ny portalopplevelse uten tjenestebrudd.

## Brukerbehov
- Innbyggere og virksomheter trenger ett sted å finne riktig skjema eller tjeneste.
- Brukere trenger tydelig oversikt over meldinger og oppgaver i innboks.
- Virksomhetsrepresentanter trenger presis tilgangsstyring for å handle på vegne av andre.
- Tjenesteeiere trenger en etablert, felles kanal med stor brukerflate.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Typisk bruk |
|---|---|---|
| Innbyggere | Finne og bruke riktige tjenester | Søke, sende inn, følge opp |
| Virksomhetsrepresentanter | Handle på vegne av virksomhet | Innsending, oppfølging, delegering |
| Fullmaktshavere (f.eks. regnskapsfører) | Korrekte roller/rettigheter | Arbeid for flere virksomheter |
| Offentlige tjenesteeiere | Synliggjøre og tilgjengeliggjøre tjenester | Publisering av skjema og tjenesteløp |
| Forvaltning/support | Innsyn i brukerflyt og feil | Veiledning, avvikshåndtering |

## Hovedfunksjoner
- Startside med søk etter skjema, tjenester og offentlig informasjon.
- Oversikt over «Skjema og tjenester» med kategorier og etater.
- Innboks for meldinger/oppgaver (ny innboks i beta samt eksisterende innboks i overgang).
- Tilgangsstyring for roller, enkeltrettigheter og tilgangspakker.
- Portalnær inngang til innlogging og representasjonskontekst.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Brukerrettet portalflate for søk, innboks, tilgangsstyring og tjenesteinngang | Sektorspesifikk faglogikk i hver tjeneste |
| Presentasjon av oppgaver/meldinger mot sluttbruker | Full backend-orkestrering i eksterne fagsystemer |
| Rolle- og representasjonsstyrt tilgang i portalflate | Lokal autorisasjonsforvaltning utenfor Altinns mekanismer |
| Navigasjon og samordning på tvers av mange etater | Erstatning av alle etaters egne domeneportaler |

## Veikart over kommende funksjonalitet
**Fakta fra kilder (2026-03-10):**
- 4. mars 2026: Ny Altinn-plattform lansert i beta.
- 4. mars 2026: Ny innboks og ny tilgangsstyring lansert i beta.
- 11. mars 2026: Innlogging med e-post innføres.
- April 2026: Ny Altinn-melding i beta.
- Fram til 19. juni 2026: Eksisterende Altinn-løsninger er tilgjengelige parallelt.

**Deduksjon:** Portalen vil i perioden ha økt kompleksitet i brukerkommunikasjon og support, fordi gammel og ny arbeidsflate lever side om side.

## Forretningsverdi/Verdiforslag
- **For innbyggere:** Raskere vei til riktig skjema/tjeneste gjennom samlet portal og søk.
- **For virksomheter:** Effektiv oppgaveutførelse med representasjon og tilgangsstyring i samme kontekst.
- **For tjenesteeiere:** Høy distribusjonsverdi via etablert nasjonal brukerkanal.
- **For samfunnet:** Redusert fragmentering og høyere gjenbruk av nasjonale fellesløsninger.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil i rolle/fullmakt kan gi urettmessig handling på vegne av andre | Tydelig regelverksforankring, revisjon av tilgangsregler, sporbarhet |
| Teknisk | Feil i overgang mellom gammel og ny portal/infrastrukturløp | Etappevis innføring, fallback-løsninger, tett overvåking |
| Sikkerhet | Konto- og tilgangsfeil i portalnivå påvirker mange tjenester samtidig | Sterk autentisering, minste privilegium, sikkerhetstesting |
| Forvaltning | Uklare grensesnitt mellom gammel og ny brukerflate kan gi forvaltningsstøy | Tydelig ansvarskart, kommunisert overgangsplan, koordinert release |
| Brukeropplevelse | Brukerforvirring i overgangsperioden mellom løsninger | Klarspråk, synlig veiledning, målrettet support |

## Kanaler
- Altinn startside: https://info.altinn.no/
- Skjema og tjenester: https://info.altinn.no/no/Skjema-og-tjenester/
- Ny innboks (beta): https://af.altinn.no/ui/messages/inbox
- Eksisterende innboks (overgang): https://am.ui.altinn.no/messages/inbox
- Tilgangsstyring: https://info.altinn.no/hjelp/profil/tilgangsstyring/om-tilgangsstyring/
- Digdir nyhet om nye Altinn (4. mars 2026): https://www.digdir.no/digitalisering-og-samordning/nye-altinn-enklere-tryggere-og-mer-moderne/6997
- Digdir nyhet om overgang fram til 19. juni 2026: https://www.digdir.no/digitalisering-og-samordning/nye-altinn-gjort-enklere-og-mer-intuitiv/7000

## Plattform
Portal-/arbeidsflatekomponent i Altinn-økosystemet, i overgang mellom etablert løsning og ny plattform i beta (mars-juni 2026).

**Ikke offentlig dokumentert:** Full teknisk detaljering av portalens totale plattformavgrensning i én samlet offentlig spesifikasjon.

## Gjenbruk
Høy gjenbruksverdi:
- Felles inngang for mange etater reduserer behov for parallelle portaler.
- Felles tilgangs- og representasjonsmønstre kan brukes på tvers av tjenester.
- Ett felles kontaktpunkt for brukere gir mer effektiv opplæring og support.

## Støtte arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov**
  Samlet inngang med søk, innboks og tilgangsstyring gir enklere brukerreise.
- **P5: Del og gjenbruk løsninger**
  Felles portalflate gjenbrukes av mange tjenesteeiere.
- **P6: Lag digitale løsninger som støtter samhandling**
  Felles kanal muliggjør samhandling mellom etater og tjenester.
- **P7: Sørg for tillit til oppgaveløsningen**
  Tilgangsstyring, representasjon og sporbarhet understøtter tillit.

## Finansiering
- Altinn Portal inngår i Altinn-porteføljen under Digdir-forvaltning.
- **Ikke offentlig dokumentert:** Detaljert kostnadsfordeling for portal isolert fra øvrige Altinn-komponenter.

## Forvaltning/eier
| Ansvarsområde | Vurdering |
|---|---|
| Produktansvar | Altinn-forvaltningen i Digdir |
| Driftsansvar | Altinns drifts- og forvaltningsmiljø (Digdir med partnere) |
| Budsjettansvar | Digdir innenfor Altinn-porteføljen |
| Styringsmodell | Porteføljestyring i Altinn-løpet med koordinering mot tjenesteeiere |

## Lenke til dokumentasjon
- https://info.altinn.no/
- https://info.altinn.no/no/Skjema-og-tjenester/
- https://info.altinn.no/hjelp/profil/tilgangsstyring/om-tilgangsstyring/
- https://www.digdir.no/digitalisering-og-samordning/nye-altinn-enklere-tryggere-og-mer-moderne/6997
- https://www.digdir.no/digitalisering-og-samordning/nye-altinn-gjort-enklere-og-mer-intuitiv/7000
- https://www.digdir.no/felleslosninger/nasjonale-felleslosninger/750

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/produkter/produktbeskrivelser/21-Altinn-Portal-produkt-canvas.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `sources/links.md`
- Nettkilde: Altinn startside (hentedato 2026-03-10)
- Nettkilde: Altinn hjelp, tilgangsstyring/innboks (hentedato 2026-03-10)
- Nettkilde: Digdir nyheter om nye Altinn (publisert 2026-03-04 og 2026-03-07, hentet 2026-03-10)

---

## Endringer fra forrige codex-versjon (2026-03-10)

### Analyseforbedringer
- Lagt inn ny kildeanalyse av eksterne kilder med konkrete datoer for overgang til ny Altinn-plattform.
- Verifisert og dokumentert at ny innboks/tilgangsstyring er i beta og at parallelldrift går til 19. juni 2026.
- Skilt tydeligere mellom fakta, deduksjon og ikke-offentlig dokumentert informasjon.

### Tekstlige forbedringer
- Strammet språk og begrepsbruk med konsekvent norsk terminologi.
- Konkretisert veikart, kanaler og risiko med høyere presisjon.
- Forbedret sammenheng mellom produktmål, brukerbehov og kapabiliteter.
