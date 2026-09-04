# VIGO Sentralbase

## Ressurs ID
NOVARI-006

## Status/Livsfase
**Produksjon** - etablert sentral database i drift for videregående opplæring.

**Fakta:** Novari beskriver VIGO Sentralbase som felles database for videregående opplæring med både historiske og aktuelle data, og som grunnlag for alle webapplikasjoner i VIGO-familien.

## Modenhet
VIGO Sentralbase fremstår som en moden, sektorbærende datakjerne med høy operativ betydning:
- Benyttes som felles datagrunnlag på tvers av fylkeskommuner.
- Leverer statistikkgrunnlag til blant annet Utdanningsdirektoratet og Statistisk sentralbyrå.
- Understøtter likebehandling og sømløse tjenester på tvers av fylkesgrenser.

Samtidig er den tekniske modenheten indirekte knyttet til overordnet modernisering av VIGO-systemet. Kildene beskriver funksjon og rolle tydeligere enn detaljert teknisk arkitektur.

## Kort beskrivelse
VIGO Sentralbase er den felles databaseressursen for videregående opplæring i Norge, forvaltet i Novari-samarbeidet. Ressursen samler historiske og løpende data og fungerer som kildelag for webapplikasjoner og sentrale leveranser i VIGO-økosystemet.

Ressursen er viktig i nasjonal arkitektur fordi den gir et standardisert og felles datagrunnlag for fylkeskommunenes forvaltning av videregående opplæring. Den bidrar til likere praksis, enklere tilgang til opplysninger på tvers av geografi og mer konsistente leveranser til nasjonale myndigheter.

## Kapabiliteter
- **Datakilder: Grunndata**
  VIGO Sentralbase fungerer som autoritativ felles datakilde for sentrale opplysninger i videregående opplæring.
- **Informasjonsforvaltning: Datastyring**
  Ressursen legger grunnlag for strukturert forvaltning av data, historikk og leveranser på tvers av fylkeskommuner.
- **Datautveksling og integrasjon: Dele data med andre**
  Sentralbasen muliggjør felles datautlevering og statistikkleveranser til nasjonale myndigheter og andre aktører med hjemmel.

## Produktmål
- Være felles datagrunnlag for webapplikasjonene i VIGO-systemet.
- Sikre konsistente data og likebehandling på tvers av fylkeskommuner.
- Understøtte felles leveranser av statistikk og styringsinformasjon til nasjonale myndigheter.

## Brukerbehov
- Fylkeskommunene trenger ett felles datagrunnlag i stedet for separate regionale datamodeller.
- Administrative brukere trenger enkel tilgang til korrekte opplysninger uavhengig av bosted og arbeidssted.
- Myndigheter trenger konsistente datauttrekk for statistikk og styringsformål.
- VIGO-applikasjoner trenger stabil og standardisert datakilde.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Fylkeskommunale administrasjoner | Felles og konsistent datagrunnlag | Inntak, oppfølging og administrasjon | Primær brukergruppe |
| VIGO-applikasjoner | Stabil datakilde for funksjoner | Drift av webapplikasjoner i VIGO-familien | Teknisk kjerneavhengighet |
| Myndigheter og analysemiljø | Pålitelig statistikkgrunnlag | Leveranser til Udir/SSB og styringsformål | Viktig sekundærbruker |
| Novari forvaltningsmiljø | Datastyring og kvalitet | Forvaltning, utvikling og leveransekontroll | Eierskap og porteføljestyring |

## Hovedfunksjoner
VIGO Sentralbase lagrer og forvalter sentrale data for videregående opplæring, inkludert historiske og løpende opplysninger. Den er fundamentet som øvrige VIGO-applikasjoner bygger på.

Ressursen muliggjør felles tilgang til opplysninger for ansatte i fylkeskommuner, lærebedrifter, samarbeidsorganer og andre aktører med rettmessig behov. Dette reduserer regionale forskjeller i datatilgang og praksis.

Sentralbasen har også en tydelig leveransefunksjon ved å være kilde for fylkeskommunenes statistikk til nasjonale myndigheter. Dette gir mer enhetlig rapportering og bedre sammenlignbarhet over tid.

Som felles datagrunnlag støtter sentralbasen sømløse tjenester og samhandling i videregående opplæring, men den er ikke i seg selv en sluttbrukerportal. Sluttbrukeropplevelser håndteres i tilknyttede tjenester som VIGO-portalen og vigo.no.

### Typiske brukssituasjoner (generisk)
- når en VIGO-applikasjon trenger felles elev-, tilbuds- eller prosessdata
- når fylkeskommunene trenger konsistente data for administrasjon og oppfølging
- når data skal leveres samlet til nasjonale myndigheter for statistikk og styring

### Når VIGO Sentralbase normalt ikke er førstevalg
- når behovet gjelder innbyggernær brukerflate og veiledning (se vigo.no og portalflater)
- når oppgaven gjelder kun navigasjon mellom moduler (se VIGO-portalen)
- når behovet gjelder normerende modellarbeid uten operativ databehandling

## Scope og avgrensning
Inngår:
- sentral datalagring og forvaltning av historiske/løpende VIGO-data
- datagrunnlag for VIGO-webapplikasjoner
- felles dataleveranser og statistikkgrunnlag

Inngår ikke:
- full sluttbrukerportal eller søknadsflate for innbyggere
- hele VIGO-systemfamilien som helhet (beskrives i VIGO overordnet)
- normerende kodeverkforvaltning som egen delressurs (VIGO Kodeverk)

## Veikart over kommende funksjonalitet
Ingen egen samlet offentlig veikartsplan for sentralbasen er hentet i denne arbeidsøkten. Ressursen forventes å påvirkes av moderniseringen av VIGO-systemet.

## Forretningsverdi/Verdiforslag
- For fylkeskommunene: felles datagrunnlag reduserer dobbeltarbeid og forbedrer datakvalitet på tvers av regioner.
- For myndigheter: bedre grunnlag for nasjonal statistikk og styringsinformasjon.
- For systemforvaltning: sentralisert datakjerne forenkler samordnet utvikling av VIGO-familien.

## Utfordringer og risiko
| Kategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Feil i sentralbasen kan påvirke mange tjenester samtidig | Tydelig datastyring og kvalitetssikring i forvaltningen |
| Avhengighet | Mange applikasjoner er avhengige av samme kjerne | Robust drift, endringskontroll og prioritert beredskap |
| Modernisering | Endringer i kjernearkitektur kan påvirke kompatibilitet | Trinnvis modernisering og koordinert migrering |

## Kanaler
- https://novari.no/tjenester/vigo-sentralbase/
- https://www.vigo.no/nyvigo/portalen/portalen.html (tilknyttet portalinngang)

## Plattform
Felles sentral database i VIGO-økosystemet, forvaltet av Novari for fylkeskommunene og Oslo kommune.

## Gjenbruk
Ressursen har svært høy gjenbruksverdi i fylkeskommunal utdanningsforvaltning, fordi samme datagrunnlag betjener mange tjenester og aktører.

### Vanlige kombinasjoner med andre produkter
- `VIGO`
- `VIGO-portalen`
- `VIGO Kodeverk og kodeverksbase`
- `vigo.no`

**Kildekode:** Ikke offentlig dokumentert. Sentralbasen er ikke publisert. Enkelte VIGO-relaterte komponenter er publisert på [github.com/FINTLabs](https://github.com/FINTLabs).

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Sentralbasen muliggjør felles datadeling og gjenbruk på tvers av fylkeskommuner og myndigheter.
- **P5: Del og gjenbruk løsninger**
  Én felles datakjerne erstatter parallelle regionale dataløsninger.
- **P6: Lag digitale løsninger som støtter samhandling**
  Felles datagrunnlag gjør samhandling mellom tjenester og aktører mer konsistent.

## Finansiering
Forvaltet gjennom felles fylkeskommunal finansiering i Novari-samarbeidet.

## Forvaltning/eier
| Område | Beskrivelse |
|---|---|
| Produktansvar | Novari IKS |
| Driftsansvar | IST drifter og utvikler VIGO på vegne av Novari |
| Budsjettansvar | Fylkeskommunene og Oslo kommune i fellesskap |

## Lenke til dokumentasjon
- https://novari.no/tjenester/vigo-sentralbase/
- https://novari.no/tjenester/vigo/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://novari.no/tjenester/vigo-sentralbase/ (kontrollert 2026-05-03)
- Nettkilde: https://novari.no/tjenester/vigo-2/ (kontrollert 2026-05-03)
- Nettkilde: https://novari.no/tjenester/vigo/ (kontrollert 2026-05-03)
