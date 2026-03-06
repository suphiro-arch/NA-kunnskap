# Produkt-canvas: Altinn Portal

Maalgruppe: Hovedfokus er forretningssiden og strategisk arkitektur.

## Navn
Altinn Portal

## Ressurs ID
21 (Produktliste NA-kunnskap).

## Status/Livsfase
Produksjon, med gradvis utvikling i samspill med nye Altinn 3-baserte brukerflater.

## Modenhet
Middels til hoy:
- Etablert som sentral brukerinngang for Altinn-tjenester.
- Har en historisk rolle fra tidligere Altinn-generasjoner, samtidig som nye komponenter og arbeidsflater utvikles videre.
- Modenhet paavirkes av overgang mellom eldre og nyere portal-/arbeidsflatemoenstre.

## Kort beskrivelse
Altinn Portal er den brukerrettede inngangen til Altinn-tjenester for innbyggere, virksomheter og representanter. Portalen samler tilgang til skjema, meldinger, dialoger, roller og virksomhetsrettet oppgavelosning, og fungerer som et viktig bindeledd mellom felleskomponenter og sluttbrukeropplevelse.

## Kapabiliteter
- Sluttbrukertjenester: Sammenhengende tjenester
- Sluttbrukertjenester: Tjenestekjeder
- Tillit: Representasjon
- Tillit: Tilgangsstyring
- Tillit: Sporbarhet og innsyn
- Samarbeid: Organisatorisk samhandling
- Tjenesteutvikling: Gjenbrukbare tjenester

Grunnlag: kapabiliteter mappet mot `index/capabilities.yaml`.

## Produktmaal
- Tilby en samlet og brukervennlig inngang til offentlige digitale tjenester i Altinn-oekosystemet.
- Gi brukere og virksomheter oversikt over oppgaver, meldinger og handlinger paa tvers av tjenester.
- Understoette representasjon og rollebruk for virksomhetskontekst.
- Sikre sammenheng mellom portalopplevelse og underliggende tjenestekomponenter.

## Brukerbehov
- Innbyggere og virksomheter trenger ett sted aa finne, bruke og foelge opp Altinn-relaterte tjenester.
- Representanter trenger tydelig haandtering av roller/fullmakter ved handling paa vegne av andre.
- Tjenesteeiere trenger en etablert kanal for tilgjengeliggjoering av tjenester mot sluttbruker.

## Hvem er brukerne og brukersegmentene
- Innbyggere.
- Naeringslivsbrukere og virksomhetsrepresentanter.
- Regnskapsforere/radgivere og andre fullmaktbaserte brukere.
- Offentlige tjenesteeiere som publiserer tjenester i Altinn-oekosystemet.

## Hovedfunksjoner
- Tilgang til tjenester, skjema og brukeroppgaver.
- Oversikt over meldinger/dialoger og oppfoelging av innsendinger.
- Rolle- og representasjonsstotte i virksomhetskontekst.
- Navigasjon til relevante Altinn-produkter og tjenesteflater.
- Portalnaer samhandling med autorisasjon, melding, varsling og dialogkomponenter.

### Scope og avgrensning
- Inngaar:
  - brukerrettet portal/arbeidsflatefunksjon i Altinn-oekosystemet
  - samling av tjenester, meldinger og oppgaver for sluttbruker
  - representasjon/rollebasert brukerflyt
- Inngaar ikke:
  - all underliggende faglogikk i den enkelte tjeneste
  - ren backend-integrasjon uten brukerflate

## Veikart over kommende funksjonalitet
- Videre modernisering av brukeropplevelse i samspill med nye Altinn 3-funksjoner.
- Forventet gradvis harmonisering mellom portal og nyere arbeidsflatemodeller.
- Konkrete roadmap-punkter ma avstemmes med offentlige Altinn-kanaler og samarbeidssider.

## Forretningsverdi/Verdiforslag
- Bedre brukeropplevelse gjennom samlet tilgang til mange offentlige tjenester.
- Hoyere effektivitet for virksomheter med mange oppgaver og representasjonsbehov.
- Redusert fragmentering ved at brukeren ikke maa forholde seg til mange separate innganger.
- Styrker adopsjon av nasjonale fellestjenester ved tydelig sluttbrukerflate.

## Utfordringer og risiko
- Juridisk risiko: feil i rolle-/fullmaktsbruk kan gi uoensket handling paa vegne av andre.
- Teknisk risiko: avhengighet til flere underliggende tjenester kan gi sammensatt feilbilde.
- Sikkerhetsrisiko: brukerflate med mange funksjoner krever sterk tilgangsstyring og robust sesjonshaandtering.
- Leverandoerrisiko: overgang mellom gammel og ny funksjonalitet kan gi kompleks forvaltning.
- Brukerrisiko: informasjons- og navigasjonskompleksitet kan svekke opplevd brukervennlighet.

## Kanaler
- Altinn.no (portal-/arbeidsflateinngang).
- Tilknyttede tjenestesider og prosessflyter.
- Samarbeidssider for portal og brukeropplevelse.

## Plattform
Portal-/arbeidsflatekomponent i Altinn-oekosystemet, med samspill mellom eldre og nyere loesningskomponenter.

## Gjenbruk
Hoy gjenbruksverdi:
- felles brukerinngang for mange tjenester
- gjenbruk av representasjons- og tilgangsmoenstre
- reduserer behovet for separate portaloppsett i hver virksomhet

## Stoette arkitekturprinsipper
Sterk stoette for:
- P1 Ta utgangspunkt i brukernes behov
- P5 Del og gjenbruk loesninger
- P6 Lag digitale loesninger som stoetter samhandling
- P7 Soerg for tillit til oppgaveloesningen

## Finansiering
Ikke eksplisitt spesifisert i kildene brukt her.
Forutsettes som del av nasjonal finansiering av Altinn-fellesloesninger.

## Forvaltning/eier
- Produktansvar: Altinn-forvaltningen
- Driftsansvar: Altinn-forvaltningen
- Budsjettansvar: usikkert i offentlig detaljnivaa
- Styringsmodell: nasjonal forvaltning i Altinn-portefoljen

## Lenke til dokumentasjon
- https://www.altinn.no/
- https://docs.altinn.studio/nb/
- https://samarbeid.digdir.no/altinn/portalar-og-brukaroppleving/2485

## Kildegrunnlag brukt i denne utfyllingen
- Lokal fil: `sources/links.md`
- Lokal fil: `index/capabilities.yaml`
- Nettkilder: Altinn/Digdir-sider (hentet 2026-03-06)
