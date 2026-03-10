# Produkt-canvas: Altinn Portal

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn Portal

## Ressurs ID
21 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon, med gradvis modernisering i samspill med øvrige Altinn 3-komponenter.

## Modenhet
Høy funksjonell modenhet, men sammensatt teknisk modenhet:
- Etablert og bredt brukt inngang til Altinn-tjenester.
- Stabil i daglig drift med høy brukerforventning.
- Påvirkes av overgang mellom eldre portalmønstre og nyere arbeidsflater.
- **Usikkert:** Presis modenhetsvurdering per delkomponent er ikke offentlig dokumentert i detalj.

## Kort beskrivelse
Altinn Portal er den brukerrettede inngangen til digitale tjenester i Altinn-økosystemet. Portalen samler oppgaver, meldinger, innsyn og representasjon i én brukerflate, og kobler sluttbrukeropplevelse med underliggende felleskomponenter og tjenesteimplementasjoner.

## Kapabiliteter
- **Sluttbrukertjenester: Sammenhengende tjenester**  
  Portalopplevelsen samler flere tjenester i ett sammenhengende løp for innbygger og virksomhet.
- **Sluttbrukertjenester: Tjenestekjeder**  
  Brukeren kan gå fra varsling/melding til handling i samme tjenestekontekst.
- **Tillit: Representasjon**  
  Portalen støtter handling på vegne av virksomhet eller andre når representasjonsforhold foreligger.
- **Tillit: Tilgangsstyring**  
  Tilgang til funksjoner og data styres ut fra roller, rettigheter og kontekst.
- **Tillit: Sporbarhet og innsyn**  
  Brukerhandlinger og dialoger må kunne følges opp i forvaltning og kontroll.
- **Samarbeid: Tjenesteforvaltning**  
  Portalen er en felles leveranseflate for flere tjenesteeiere med behov for samordnet forvaltning.
- **Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling**  
  Portalnivået må ivareta sikker flyt mellom brukerflater og underliggende tjenester.

Grunnlag: Kapabilitetsnavn fra `index/capabilities.yaml`, vurdert opp mot produktets rolle.

## Produktmål
- Gi innbyggere og virksomheter én tydelig inngang til Altinn-relaterte tjenester.
- Redusere friksjon i brukerreiser ved å samle oppgaver, meldinger og status i samme arbeidsflate.
- Understøtte trygg representasjon og rollebasert handling på tvers av tjenester.
- Sikre konsistent brukeropplevelse selv om underliggende tjenester forvaltes av ulike aktører.
- Være en stabil overgangsflate i modernisering fra eldre til nyere Altinn-løsninger.

## Brukerbehov
- Brukere trenger oversikt over hva de må gjøre, hva som er mottatt, og hva som gjenstår.
- Virksomhetsrepresentanter trenger tydelig kontekst for hvem de handler på vegne av.
- Tjenesteeiere trenger en kanal med etablert trafikk, støttefunksjoner og felles innloggingsmønstre.
- Forvaltning trenger sporbarhet for å kunne svare på innsyn, klager og feilsituasjoner.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Typisk bruk |
|---|---|---|
| Innbyggere | Enkel tilgang til offentlige tjenester og meldinger | Innsending, oppfølging, innsyn |
| Virksomhetsrepresentanter | Sikker handling på vegne av virksomhet | Rapportering, dialog, oppgavehåndtering |
| Fullmaktshavere (f.eks. regnskapsfører) | Korrekt rolle- og rettighetsstyring | Oppfølging av flere virksomheter |
| Tjenesteeiere i offentlig sektor | Forutsigbar publiserings- og samhandlingsflate | Tilgjengeliggjøring av digitale tjenester |
| Forvaltnings- og supportmiljø | Innsyn i hendelser og brukerflyt | Feilhåndtering, veiledning, forbedring |

## Hovedfunksjoner
- Samlet oversikt over oppgaver, meldinger og tjenester.
- Inngang til innsending, statusoppfølging og dialog.
- Rolle- og representasjonsbytte i virksomhetskontekst.
- Navigasjon mellom tjenester og tilhørende dokumentasjon/støtte.
- Kobling mot underliggende autorisasjon, dialog- og varslingsmekanismer.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Brukerrettet portal/arbeidsflate for Altinn-tjenester | Sektorspesifikk faglogikk i hver enkelt tjeneste |
| Presentasjon av meldinger, oppgaver og handlinger | Full backend-orkestrering i eksterne fagsystemer |
| Rolle- og representasjonsstyrt brukerflyt | Erstatning av alle spesialiserte fagetatsflater |
| Samspill med underliggende Altinn-komponenter | Selvstendig identitetsforvaltning utenfor Altinns tillitskomponenter |

## Veikart over kommende funksjonalitet
- Videre harmonisering mellom portal og nyere Altinn-arbeidsflater.
- Forenkling av brukerreise på tvers av meldinger, dialog og oppgaver.
- Fortsatt forbedring av universell utforming og mobiltilpasning.
- **Ikke offentlig dokumentert:** Detaljert prioriteringsliste med tidslinje.
- **Deduksjon:** Gitt pågående modernisering i Altinn-porteføljen er gradvis funksjonsflytting sannsynlig.

## Forretningsverdi/Verdiforslag
- **For innbyggere:** Færre innganger å forholde seg til og bedre oversikt over egen dialog med offentlig sektor.
- **For virksomheter:** Mer effektiv oppgavehåndtering gjennom representasjon og samlet arbeidsflate.
- **For tjenesteeiere:** Lavere terskel for distribusjon av tjenester gjennom etablert nasjonal kanal.
- **For samfunnet:** Høyere gjenbruk av fellesløsninger og mindre fragmentering i offentlige digitale tjenester.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil i rolle-/fullmaktslogikk kan gi urettmessig tilgang eller handling | Tydelig regelverksforankring, revisjon av tilgangsregler, sporbarhet |
| Teknisk | Avhengigheter til mange underliggende komponenter gir sammensatte feilbilder | Tydelig feilhåndtering, kontraktstyrte integrasjoner, robust overvåking |
| Sikkerhet | Sesjons- og tilgangsfeil i portalnivå kan påvirke mange tjenester samtidig | Prinsipp for minste privilegium, sikkerhetstesting, hendelseshåndtering |
| Leverandør/forvaltning | Endringer i portefølje og arkitektur kan skape overgangsrisiko | Etappevis migrering, tydelig endringsstyring, felles veikart |
| Brukeropplevelse | Kompleks navigasjon kan redusere mestring og øke supportbehov | Brukertesting, klarspråk, forbedret informasjonsarkitektur |

## Kanaler
- Nettportal: https://www.altinn.no/
- Samarbeidskanal for forvaltning og utvikling: https://samarbeid.digdir.no/altinn/portalar-og-brukaroppleving/2485
- Teknisk dokumentasjon i Altinn-domenet: https://docs.altinn.studio/nb/

## Plattform
Portal-/arbeidsflatekomponent i Altinn-økosystemet, med samspill mellom etablerte og nyere komponenter.

**Usikkert:** Presis teknisk plattformavgrensning for hele portalflaten er ikke samlet i én offentlig kilde.

## Gjenbruk
Høy gjenbruksverdi:
- Felles inngang for mange tjenesteeiere reduserer behov for parallelle brukerflater.
- Felles mønstre for representasjon og tilgang kan brukes på tvers av tjenester.
- Standardisert inngang støtter mer enhetlig opplæring, support og forvaltning.

## Støtte arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov**  
  Samlet inngang og oppgavesentrert arbeidsflate reduserer kompleksitet for sluttbruker.
- **P5: Del og gjenbruk løsninger**  
  Portal som felles leveranseflate gir gjenbruk på tvers av virksomheter.
- **P6: Lag digitale løsninger som støtter samhandling**  
  Felles brukerflate og felles mønstre støtter samhandling mellom flere tjenesteeiere.
- **P7: Sørg for tillit til oppgaveløsningen**  
  Representasjon, tilgangsstyring og sporbarhet er sentrale tillitselementer.

## Finansiering
- Antas finansiert som del av Altinns nasjonale forvaltning og videreutvikling.
- **Ikke offentlig dokumentert:** Detaljert kostnadsfordeling mellom portal og øvrige Altinn-komponenter.

## Forvaltning/eier
| Ansvarsområde | Vurdering |
|---|---|
| Produktansvar | Altinn-forvaltningen i Digdir |
| Driftsansvar | Altinns drifts- og forvaltningsmiljø (Digdir med partnere) |
| Budsjettansvar | Digdir innenfor Altinn-porteføljen |
| Styringsmodell | Porteføljestyring i Altinn-løpet, med samhandling mot berørte tjenesteeiere |

## Lenke til dokumentasjon
- https://www.altinn.no/
- https://docs.altinn.studio/nb/
- https://samarbeid.digdir.no/altinn/portalar-og-brukaroppleving/2485
- https://www.digdir.no/felleslosninger/nasjonale-felleslosninger/750

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `results/Produktbeskrivelser/21-Altinn-Portal-produkt-canvas.md`
- Lokal fil: `results/templates/produkt-canvas-template.md`
- Lokal fil: `index/capabilities.yaml`
- Lokal fil: `sources/links.md`
- Nettkilder via lenkeliste over (hentedato: 2026-03-09)
