# Produkt-canvas: Register over reelle rettighetshavere

## Navn
Register over reelle rettighetshavere

## Ressurs ID
BRREG-004

## Status/Livsfase
**Produksjon** - etablert nasjonalt register for opplysninger om faktisk eierskap og kontroll i registreringspliktige virksomheter.

**Fakta:** Brønnøysundregistrene beskriver reelle rettighetshavere som fysiske personer som i siste instans eier eller kontrollerer en virksomhet. Registreringspliktige virksomheter må sende inn opplysninger til registeret, og det finnes egen maskinell tilgang til data om registrerte virksomheter og deres reelle rettighetshavere.

## Modenhet
**Middels til høy modenhet** - etablert register med tydelig lovforankring og avgrenset tilgangsmodell:
- Registeret er i aktiv bruk og har konkrete plikter, frister og sanksjoner knyttet til registrering.
- Brønnøysundregistrene tilbyr maskinell tilgang via API for definerte brukergrupper og hjemler.
- Registeret har høy verdi for kontroll og etterprøvbarhet, men er ikke en generelt åpen grunnlagsressurs på samme måte som Enhetsregisteret.
- Tilgangen er avgrenset til bestemte offentlige myndigheter, rapporteringspliktige, medier, sivilsamfunnsorganisasjoner og enkelte forskningsmiljøer.

**Deduksjon:** Modenheten er høy nok til at registeret kan beskrives som egen ressurs, men analysebruk må være bevisst på at verdien ligger i kontrollert tilgang og etterlevelse, ikke bred allmenn bruk.

## Kort beskrivelse
Register over reelle rettighetshavere er den nasjonale ressursen for opplysninger om hvilke fysiske personer som i siste instans eier eller kontrollerer en registreringspliktig virksomhet. Produktet gjør det mulig å avdekke faktisk kontroll bak juridiske enheter og er derfor særlig relevant i analyser og samhandling som handler om kontroll, tilsyn, økonomisk kriminalitet, anskaffelser, sikkerhet og andre situasjoner der formell registrering alene ikke er tilstrekkelig.

## Kapabiliteter
- **Datakilder: Grunndata** er kjernefunksjonen ved at registeret gir autoritative opplysninger om faktisk eierskap og kontroll for registrerte virksomheter.
- **Datautveksling og integrasjon: Dele data med andre** er en direkte og sterk kapabilitet fordi registeret har egen API-basert tilgjengeliggjøring for definerte brukergrupper og hjemler.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Brønnøysundregistrenes sider om registeret og API-tilgang til data om reelle rettighetshavere.

## Produktmål
**Primærkilder:** Brønnøysundregistrenes sider `Reelle rettighetshavere` og `Data om reelle rettighetshavere`.

Dokumenterte mål:
- Samle inn opplysninger om hvem som i siste instans eier eller kontrollerer en virksomhet.
- Gjøre slike opplysninger tilgjengelige gjennom maskinelt grensesnitt for brukergrupper med hjemmel.
- Understøtte krav og kontroll knyttet til hvitvasking, tilsyn og andre formål med hjemlet tilgang.

Operative mål utledet fra de samme kildene:
- Gi offentlig sektor og andre hjemlede aktører bedre grunnlag for å forstå faktisk kontroll bak virksomheter.
- Styrke muligheten for samordnet oppfølging, kontroll og risikovurdering på tvers av virksomheter og sektorer.
- Redusere forskjellen mellom formell organisasjonsstruktur og faktisk kontroll i datadrevne vurderinger.

## Brukerbehov
- Offentlige myndigheter trenger kontrollert tilgang til opplysninger om faktisk eierskap og kontroll i virksomheter.
- Rapporteringspliktige etter hvitvaskingsregelverket trenger et kontrollgrunnlag i kundetiltak og løpende oppfølging.
- Medier, sivilsamfunn og forskningsmiljøer med hjemmel trenger etterprøvbare data om eier- og kontrollforhold.
- Virksomheter trenger en nasjonal, forpliktende registreringsordning for å rapportere reelle rettighetshavere.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige kontroll- og tilsynsmyndigheter | Opplysninger om faktisk kontroll i virksomheter | Kontroll, tilsyn, etterforskning, sikkerhet og oppfølging | Registeret har særlig verdi her |
| Rapporteringspliktige etter hvitvaskingsloven | Kontrollert tilgang til eier- og kontrollinformasjon | Kundetiltak og løpende oppfølging | Tilgang er hjemmelsstyrt |
| Medier og sivilsamfunn med hjemmel | Innsikt i eierskap og kontrollforhold | Undersøkelser, transparens og oppfølging | Ikke generell fri tilgang |
| Høyere utdanningsinstitusjoner med hjemmel | Datagrunnlag til forskning | Forskning og analyse | Tilgang er avgrenset og regulert |
| Registreringspliktige virksomheter | Innsending og vedlikehold av opplysninger | Etterlevelse av registreringsplikt | Møter produktet som registrerings- og rapporteringsordning |

## Hovedfunksjoner
### Primære funksjoner
**Registrering av faktisk eierskap og kontroll.** Registeret samler opplysninger om hvilke fysiske personer som i siste instans eier eller kontrollerer en virksomhet. Dette er produktets kjernefunksjon og årsaken til at det skiller seg fra mer generelle virksomhetsregistre.

**Kontrollert tilgjengeliggjøring gjennom API.** Brønnøysundregistrene beskriver at data bare er tilgjengelig gjennom maskinelt grensesnitt/API, og at tilgangen er avgrenset til brukergrupper med definert hjemmel. Produktet er derfor både et register og en kontrollert delingsressurs.

**Støtte for kontroll, tilsyn og risikovurdering.** Registeret er særlig relevant når offentlige og private aktører må vurdere hvem som faktisk står bak en virksomhet, ikke bare hvem som formelt er registrert. Dette gir produktet tydelig tverrgående verdi i samhandlings- og kontrollsammenhenger.

**Etterlevelse og oppfølging av registreringsplikt.** Produktet omfatter også registreringsplikt, frister og tvangsmulkt ved manglende oppfølging. Det betyr at registeret ikke bare er et passivt oppslagsregister, men et aktivt virkemiddel i styring og etterlevelse.

### Typiske brukssituasjoner (generisk)
- Når en offentlig myndighet må kontrollere faktisk eierskap eller kontroll bak en virksomhet i tilsyn, anskaffelser eller sikkerhetsvurderinger.
- Når rapporteringspliktige må gjennomføre kundetiltak og vurdere reelle rettighetshavere etter hvitvaskingsregelverket.
- Når samordning mellom flere myndigheter krever et mer presist bilde av hvem som faktisk kontrollerer en virksomhet.

### Når registeret normalt ikke er førstevalg
- Når behovet bare gjelder basisopplysninger om virksomheter som navn, organisasjonsnummer eller registreringsstatus; da er Enhetsregisteret normalt mer naturlig førstevalg.
- Når brukeren ikke har hjemmel til tilgang eller trenger generell åpen datatilgang.
- Når formålet er bred næringslivsstatistikk eller katalogoversikt, heller enn kontroll av faktisk eierskap og kontroll.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Opplysninger om faktisk eierskap og kontroll i registreringspliktige virksomheter | Full erstatning for Enhetsregisteret som generelt virksomhetsregister |
| API-basert tilgjengeliggjøring for hjemlede brukergrupper | Åpen masseutlevering til alle brukere |
| Registreringsplikt, frister og oppfølging | Generell selskapsanalyse utenfor registerets definerte informasjonsgrunnlag |
| Kontroll- og etterlevelsesrelevant virksomhetsinformasjon | Frie oppslag på fødselsnummer for ordinære brukere |

## Veikart over kommende funksjonalitet
**Fakta fra Brønnøysundregistrenes kilder (kontrollert 2026-04-30):**
- Registeret har etablerte frister, sanksjoner og digitale innsending- og tilgangsløp.
- Brønnøysundregistrene publiserer teknisk beskrivelse og tilgangsinformasjon for API-et.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et samlet, tidsfestet veikart for videre funksjonsutvikling er ikke hentet ut.

**Deduksjon:** Videreutvikling vil trolig være tett knyttet til regelverksoppfølging, tilgangsstyring og bedre datakvalitet og brukbarhet for hjemlede brukergrupper.

## Forretningsverdi/Verdiforslag
### For offentlig sektor
- Gir et mer presist kontrollgrunnlag om faktisk eierskap og kontroll enn generelle virksomhetsregistre alene.
- Styrker samordnet oppfølging i tilsyn, sikkerhet, økonomisk kriminalitet og anskaffelser.
- Reduserer behovet for at hver virksomhet bygger egne parallelle oversikter over kontrollforhold.

### For hjemlede private og samfunnsmessige brukere
- Gjør kundetiltak og risikovurdering mer treffsikre for rapporteringspliktige.
- Styrker transparens og etterprøvbarhet for medier, sivilsamfunn og forskning innenfor rammene for tilgang.

### For registreringspliktige virksomheter
- Gir én nasjonal ordning for rapportering av reelle rettighetshavere.
- Tydeliggjør forventninger, frister og oppfølgingsansvar knyttet til etterlevelse.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Opplysninger kan være mangelfulle eller utdaterte hvis registreringsplikten ikke følges opp riktig | Frister, sanksjoner, veiledning og tydelig registreringsansvar |
| Tilgang og personvern | Opplysninger om faktisk kontroll krever streng hjemmels- og tilgangsstyring | Avgrensede tilgangsgrupper og API-basert kontrollert utlevering |
| Brukerforståelse | Registeret kan forveksles med generelle virksomhetsregistre | Tydelig avgrensning mot Enhetsregisteret og andre registre |
| Tverrsektoriell bruk | Ulik praksis hos brukere kan gi ujevn utnyttelse av verdien i registeret | Bedre veiledning, teknisk dokumentasjon og samordnet bruk |

## Kanaler
- Reelle rettighetshavere: https://www.brreg.no/reelle-rettighetshavere/
- Data om reelle rettighetshavere: https://www.brreg.no/bruke-data-fra-bronnoysundregistrene/datasett-og-api/data-om-reelle-rettighetshavere/
- Teknisk beskrivelse: https://brreg.github.io/bo-registeret-api/

## Plattform
Register over reelle rettighetshavere er et nasjonalt register- og delingssystem for opplysninger om faktisk eierskap og kontroll, forvaltet av Brønnøysundregistrene.

**Fakta:** Brønnøysundregistrene beskriver både registreringsløp, API-tilgang og målgrupper for datautlevering som del av produktområdet.

**Ikke offentlig dokumentert i brukte kilder:** Full intern systemarkitektur, detaljert teknologistakk og komplett driftsmodell.

## Gjenbruk
**Høy gjenbruksverdi i avgrensede kontroll- og samhandlingsløp:**
- Produktet er særlig relevant når behovet er å forstå faktisk kontroll bak en virksomhet, ikke bare formell registrering.
- Det er mest verdifullt i kombinasjon med Enhetsregisteret og eventuelt andre kontroll- og tilsynsdata, når flere sider av en virksomhet må vurderes samlet.
- Det er mindre relevant i åpne, generelle informasjonsbehov uten hjemmel eller når vanlig virksomhetsidentifikasjon er tilstrekkelig.

### Vanlige kombinasjoner med andre produkter
- **Enhetsregisteret** når basisopplysninger om virksomheten må suppleres med informasjon om faktisk eierskap og kontroll.
- **Skatteetatens delingstjenester** eller andre kontrollrettede delingsressurser når flere datagrunnlag må vurderes sammen i samordnet oppfølging.

**Kildekode:** Ikke offentlig dokumentert. Registerløsningen er ikke publisert. Brønnøysundregistrene publiserer API-spesifikasjoner på [github.com/brreg](https://github.com/brreg).

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at registeret samler og tilgjengeliggjør ett nasjonalt datagrunnlag om faktisk eierskap og kontroll.
- **P5: Del og gjenbruk løsninger** styrkes ved at flere hjemlede aktører kan bruke samme kontrollgrunnlag i stedet for egne, parallelle oppsett.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi registeret muliggjør mer samordnet oppfølging og kontroll på tvers av virksomheter.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi registeret bidrar til bedre sporbarhet og forståelse av hvem som faktisk kontrollerer en virksomhet.

## Finansiering
- **Fakta:** Detaljert samlet finansieringsmodell for registeret er ikke verifisert i denne arbeidsøkten.
- **Fakta:** Produktet forvaltes av Brønnøysundregistrene som nasjonal registerressurs med kontrollert tilgang.
- **Deduksjon:** Finansieringen er trolig del av offentlig registerforvaltning, kombinert med styring og prioritering knyttet til tilgangsordninger og regelverksetterlevelse.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Brønnøysundregistrene | Produktsidene om registeret og datautlevering |
| Driftsansvar | Brønnøysundregistrene | Brønnøysundregistrene framstår som operativ forvalter |
| Budsjett- og forvaltningsansvar | Brønnøysundregistrene | Registeret inngår i BRREGs nasjonale registerforvaltning |
| Styringsmodell | Lov- og forskriftsforankret registerforvaltning med avgrenset tilgang | Produktsidene, forskriftshenvisningene og tilgangsbeskrivelsen |

## Lenke til dokumentasjon
- https://www.brreg.no/reelle-rettighetshavere/
- https://www.brreg.no/bruke-data-fra-bronnoysundregistrene/datasett-og-api/data-om-reelle-rettighetshavere/
- https://brreg.github.io/bo-registeret-api/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.brreg.no/reelle-rettighetshavere/ (kontrollert 2026-04-30)
- Nettkilde: https://www.brreg.no/bruke-data-fra-bronnoysundregistrene/datasett-og-api/data-om-reelle-rettighetshavere/ (kontrollert 2026-04-30)
- Nettkilde: https://brreg.github.io/bo-registeret-api/ (kontrollert 2026-04-30)
