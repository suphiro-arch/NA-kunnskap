# Produkt-canvas: Altinn Portal

Målgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn Portal

## Ressurs ID
21 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon, med gradvis utvikling i samspill med nye Altinn 3-baserte brukerflater.

## Modenhet
Middels til høy:
- Etablert som sentral brukerinngang for Altinn-tjenester.
- Har en historisk rolle fra tidligere Altinn-generasjoner, samtidig som nye komponenter og arbeidsflater utvikles videre.
- Modenhet påvirkes av overgang mellom eldre og nyere portal-/arbeidsflatemønstre.

## Kort beskrivelse
Altinn Portal er den brukerrettede inngangen til Altinn-tjenester for innbyggere, virksomheter og representanter. Portalen samler tilgang til skjema, meldinger, dialoger, roller og virksomhetsrettet oppgaveløsning, og fungerer som et viktig bindeledd mellom felleskomponenter og sluttbrukeropplevelse.

## Kapabiliteter
- Sluttbrukertjenester: Sammenhengende tjenester
- Sluttbrukertjenester: Tjenestekjeder
- Tillit: Representasjon
- Tillit: Tilgangsstyring
- Tillit: Sporbarhet og innsyn
- Samarbeid: Organisatorisk samhandling
- Tjenesteutvikling: Gjenbrukbare tjenester

Grunnlag: kapabiliteter mappet mot `arkitektur/kapabiliteter/capabilities.yaml`.

## Produktmål
- Tilby en samlet og brukervennlig inngang til offentlige digitale tjenester i Altinn-økosystemet.
- Gi brukere og virksomheter oversikt over oppgaver, meldinger og handlinger på tvers av tjenester.
- Understøtte representasjon og rollebruk for virksomhetskontekst.
- Sikre sammenheng mellom portalopplevelse og underliggende tjenestekomponenter.

## Brukerbehov
- Innbyggere og virksomheter trenger ett sted å finne, bruke og følge opp Altinn-relaterte tjenester.
- Representanter trenger tydelig håndtering av roller/fullmakter ved handling på vegne av andre.
- Tjenesteeiere trenger en etablert kanal for tilgjengeliggjøring av tjenester mot sluttbruker.

## Hvem er brukerne og brukersegmentene
- Innbyggere.
- Næringslivsbrukere og virksomhetsrepresentanter.
- Regnskapsforere/radgivere og andre fullmaktbaserte brukere.
- Offentlige tjenesteeiere som publiserer tjenester i Altinn-økosystemet.

## Hovedfunksjoner
- Tilgang til tjenester, skjema og brukeroppgaver.
- Oversikt over meldinger/dialoger og oppfølging av innsendinger.
- Rolle- og representasjonsstotte i virksomhetskontekst.
- Navigasjon til relevante Altinn-produkter og tjenesteflater.
- Portalnær samhandling med autorisasjon, melding, varsling og dialogkomponenter.

### Scope og avgrensning
- Inngår:
  - brukerrettet portal/arbeidsflatefunksjon i Altinn-økosystemet
  - samling av tjenester, meldinger og oppgaver for sluttbruker
  - representasjon/rollebasert brukerflyt
- Inngår ikke:
  - all underliggende faglogikk i den enkelte tjeneste
  - ren backend-integrasjon uten brukerflate

## Veikart over kommende funksjonalitet
- Videre modernisering av brukeropplevelse i samspill med nye Altinn 3-funksjoner.
- Forventet gradvis harmonisering mellom portal og nyere arbeidsflatemodeller.
- Konkrete roadmap-punkter må avstemmes med offentlige Altinn-kanaler og samarbeidssider.

## Forretningsverdi/Verdiforslag
- Bedre brukeropplevelse gjennom samlet tilgang til mange offentlige tjenester.
- Høyere effektivitet for virksomheter med mange oppgaver og representasjonsbehov.
- Redusert fragmentering ved at brukeren ikke må forholde seg til mange separate innganger.
- Styrker adopsjon av nasjonale fellestjenester ved tydelig sluttbrukerflate.

## Utfordringer og risiko
- Juridisk risiko: feil i rolle-/fullmaktsbruk kan gi uønsket handling på vegne av andre.
- Teknisk risiko: avhengighet til flere underliggende tjenester kan gi sammensatt feilbilde.
- Sikkerhetsrisiko: brukerflate med mange funksjoner krever sterk tilgangsstyring og robust sesjonshåndtering.
- Leverandørrisiko: overgang mellom gammel og ny funksjonalitet kan gi kompleks forvaltning.
- Brukerrisiko: informasjons- og navigasjonskompleksitet kan svekke opplevd brukervennlighet.

## Kanaler
- Altinn.no (portal-/arbeidsflateinngang).
- Tilknyttede tjenestesider og prosessflyter.
- Samarbeidssider for portal og brukeropplevelse.

## Plattform
Portal-/arbeidsflatekomponent i Altinn-økosystemet, med samspill mellom eldre og nyere løsningskomponenter.

## Gjenbruk
Høy gjenbruksverdi:
- felles brukerinngang for mange tjenester
- gjenbruk av representasjons- og tilgangsmønstre
- reduserer behovet for separate portaloppsett i hver virksomhet

## Støtte arkitekturprinsipper
Sterk støtte for:
- P1 Ta utgangspunkt i brukernes behov
- P5 Del og gjenbruk løsninger
- P6 Lag digitale løsninger som støtter samhandling
- P7 Sørg for tillit til oppgaveløsningen

## Finansiering
Ikke eksplisitt spesifisert i kildene brukt her.
Forutsettes som del av nasjonal finansiering av Altinn-fellesløsninger.

## Forvaltning/eier
- Produktansvar: Altinn-forvaltningen
- Driftsansvar: Altinn-forvaltningen
- Budsjettansvar: usikkert i offentlig detaljnivå
- Styringsmodell: nasjonal forvaltning i Altinn-porteføljen

## Lenke til dokumentasjon
- https://www.altinn.no/
- https://docs.altinn.studio/nb/
- https://samarbeid.digdir.no/altinn/portalar-og-brukaroppleving/2485

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Nettkilder: Altinn/Digdir-sider (hentet 2026-03-06)
