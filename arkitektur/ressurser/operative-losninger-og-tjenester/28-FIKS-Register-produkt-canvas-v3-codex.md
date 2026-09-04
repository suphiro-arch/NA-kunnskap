# Produkt-canvas: Fiks register

## Navn
Fiks register

## Ressurs ID
KS-004

## Status/Livsfase
**Produksjon** - etablert registerfamilie og tilgangslag i KS Digital for kommunal bruk av flere nasjonale registre gjennom samme forvaltnings- og integrasjonsmønster.

**Fakta:** KS Digital beskriver Fiks register som en løsning der kommuner og fylkeskommuner kan gjøre oppslag via Fiks forvaltning eller gjennom integrasjon mot fagsystemer. Produktsiden viser folkeregister, skatte- og inntektsopplysninger og kjøretøyregister som aktive undertjenester, og opplyser at flere registre er under vurdering.

## Modenhet
**Middels til høy funksjonell modenhet** - produktområdet er tydelig etablert som felles kommunalt tilgangslag, med operative undertjenester, publisert prismodell og eksplisitt tilgangsstyring, men modenheten varierer mellom undertjenestene og deres kildeavhengigheter.

- Løsningen er dokumentert både som nettsideløsning og som maskin-til-maskin-integrasjon.
- KS Digital beskriver egen tilgangsstyring i tillegg til brukeradministrasjonen på Fiks-plattformen.
- Produktsiden viser at registerfamilien både sammenstiller opplysninger etter tjenstlig behov og arbeider med å koble på flere kilder.

**Deduksjon:** Den overordnede modenheten er høy nok til å brukes som standard kommunalt mønster for registertilgang, men produktet må fortsatt vurderes som et forvaltnings- og tilgangslag, ikke som en selvstendig datakilde eller fullverdig erstatning for hvert enkelt kildegrensesnitt.

## Kort beskrivelse
Fiks register er KS Digitals overordnede registerfamilie for kommunal tilgang til nasjonale registerdata. Løsningen samler flere kilder og undertjenester i samme tjenesteområde, slik at kommuner og fylkeskommuner kan bruke et felles oppslags- og integrasjonsmønster i stedet for å etablere separate løp mot hver datakilde. Produktet kan brukes både gjennom Fiks forvaltning for saksbehandlere og gjennom integrasjon mot kommunale fagsystemer. Verdien ligger derfor i tilgangslaget, styringen og den felles forvaltningen av registerbruk, ikke i eierskap til de underliggende dataene.

## Kapabiliteter
- **Datakilder: Grunndata** er relevant fordi Fiks register gjør flere autoritative datakilder operative i kommunal sektor gjennom ett samlet og kontrollert tilgangslag.
- **Datautveksling og integrasjon: Bruke data fra andre** er kjernefunksjonen fordi produktet gir kommuner og fylkeskommuner et standardisert løp for å hente og bruke data fra andre virksomheters registre.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot KS Digitals produkt- og prismateriale kontrollert 2026-05-26.

## Produktmål
Dokumenterte mål:
- Gi kommuner og fylkeskommuner tilgang til flere nasjonale registre gjennom én samlet tjeneste.
- Tilby både oppslagsfunksjonalitet i Fiks forvaltning og maskin-til-maskin-integrasjon mot fagsystemer.
- Ivareta datasikkerhet, personvern og tjenstlig behov gjennom egen tilgangsstyring.

Operative mål utledet fra kildene:
- Redusere behovet for separate kommunale integrasjonsløp mot hver datakilde.
- Gjøre det enklere å bruke oppdaterte registeropplysninger direkte i kommunale arbeidsprosesser.
- Skape et mer ensartet kommunalt forvaltningsmønster for hjemmel, roller og dataminimering når nasjonale registerdata tas i bruk.

## Brukerbehov
- Kommuner og fylkeskommuner trenger én samlet inngang til flere nasjonale registerkilder.
- Saksbehandlere trenger rask tilgang til relevante opplysninger uten å forlate sine operative arbeidsprosesser.
- Fagsystemer trenger et standardisert integrasjonsmønster for bruk av registerdata maskinelt.
- Lokale og sentrale forvaltere trenger styring med roller, tilgang og hvilke opplysninger som faktisk skal brukes i ulike tjenesteområder.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Samlet tilgang til flere nasjonale registerkilder | Oppslag, saksbehandling og integrert bruk i kommunale tjenester | Primær målgruppe |
| Saksbehandlere | Effektiv oppslagsfunksjon med riktig avgrensede data | Bruk i Fiks forvaltning i operative arbeidsprosesser | Bruker webflaten direkte |
| Fagsystemer og leverandører | Standardisert maskin-til-maskin-tilgang | Integrasjon i kommunale arbeidsprosesser og tjenesteløsninger | Teknisk brukergruppe |
| Fiks-administratorer og forvaltere | Rolle-, tilgangs- og tjenesteområdestyring | Oppsett, lokal forvaltning og etterlevelse | Kritisk for kontroll |
| KS Digital | Samordne kilder, avtaler og tjenesteutvikling | Produktforvaltning, teknisk drift og koordinering mot kilder | Sentral forvaltningsrolle |

## Hovedfunksjoner
### Primære funksjoner
Fiks register sin viktigste funksjon er å samle tilgang til flere nasjonale registre i ett felles kommunalt tjenesteområde. Produktet er derfor ikke ett selvstendig register, men et overordnet tilgangslag og en registerfamilie som gjør autoritative data fra andre virksomheter operative i kommunale prosesser. Dette er et viktig avgrensningspunkt: verdien ligger i det felles kommunale bruks- og styringsmønsteret, ikke i egne kildedata.

Løsningen har to tydelige leveranseflater som må forstås samlet. Den ene er nettsideløsningen i Fiks forvaltning, der saksbehandlere kan gjøre oppslag direkte i arbeidshverdagen. Den andre er maskin-til-maskin-integrasjon mot kommunale fagsystemer. Fiks register er derfor bredere enn en administrativ portal, men også bredere enn et rent API. Produktet fungerer som et operativt mellomlag mellom kommunal bruk og eksterne datakilder.

En sentral funksjon er å standardisere hvordan kommunal sektor får tilgang til registeropplysninger fra flere kilder. KS Digital beskriver at opplysningene kommer direkte fra kilden, men at løsningen sammenstiller data etter tjenstlige behov og forvalter tilgang gjennom egne roller. Produktet legger dermed på styring, avgrensning og et felles kontrollnivå som kommunene kan bygge videre på i egne arbeidsprosesser.

Produktområdet rommer flere undertjenester med ulik karakter, blant annet Fiks folkeregister, Fiks skatte- og inntektsopplysninger, kontaktregistertilgang og Fiks kjøretøyregister. Disse må forstås som del av samme overordnede registerfamilie, men ikke som identiske tjenester. Fiks register beskriver derfor den samlede produktrollen: et felles tilgangs- og forvaltningsmønster for nasjonale registerdata i kommunal sektor.

### Typiske brukssituasjoner (generisk)
- Når kommunen ønsker ett felles løp for oppslag og integrasjon mot flere nasjonale registerkilder.
- Når både saksbehandlere og fagsystemer trenger tilgang til samme type grunndata, men med forskjellig brukerflate.
- Når kommunen vil gjenbruke etablerte roller, tilgangsstyring og forvaltningsmønstre i stedet for å bygge egne ordninger for hver datakilde.

### Når Fiks register normalt ikke er førstevalg
- Når behovet gjelder én spesifikk kilde med særlige krav som best løses gjennom datakildens egne grensesnitt eller avtaler.
- Når virksomheten trenger full teknisk kontroll over direkte integrasjon mot kilden, uten mellomliggende tilgangslag.
- Når behovet primært gjelder hendelsesstrømmer, masseuttrekk eller andre datatyper som ikke er dokumentert som del av Fiks register-familien.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Samlet tilgang til flere nasjonale registre gjennom ett felles tjenesteområde | Eierskap til de underliggende registrene eller kildedataene |
| Oppslag i Fiks forvaltning og integrasjon mot fagsystemer | Full lokal datalagring eller kommunal registerforvaltning |
| Egen tilgangsstyring og sammenstilling etter tjenstlig behov | Ubegrenset bruk av data uten hjemmel, rolle og behov |
| Overordnet registerfamilie for undertjenester som folkeregister, skatte- og inntektsopplysninger og kjøretøyregister | Detaljert faglogikk, hjemmel og integrasjonsmønster for hver undertjeneste |

## Veikart over kommende funksjonalitet
**Fakta:** KS Digital opplyser at de jobber med å koble på flere registre og sammenstille informasjon på tvers. Jeg fant ikke et samlet offentlig roadmap med tidsfestede milepæler utover dette i denne arbeidsøkten.

**Deduksjon:** Videreutviklingen vil trolig være knyttet til nye registerkoblinger, mer finmasket sammenstilling av data og videre modning av undertjenestene i samme produktfamilie.

## Forretningsverdi/Verdiforslag
### For kommuner og fylkeskommuner
- Gjør nasjonale registeropplysninger lettere tilgjengelige gjennom ett felles kommunalt tilgangsmønster.
- Reduserer behovet for å etablere og forvalte mange ulike oppkoblinger mot hver datakilde.

### For saksbehandlere og fagmiljøer
- Gir raskere tilgang til relevante opplysninger i konkrete arbeidsprosesser.
- Gjør at registerdata i større grad kan brukes direkte fra kilden og i riktig kontekst.

### For leverandører og sektoren
- Gir et mer ensartet integrasjonspunkt for kommunal bruk av registerdata.
- Støtter gjenbruk av felles tilgangs- og forvaltningsmønstre i stedet for parallelle lokale løsninger.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Tilgang til registerdata krever riktig hjemmel, riktig tjenesteområde og korrekt bruk i lokale prosesser. | Tydelig tilgangsstyring, lokal kontroll av behandlingsgrunnlag og kobling til datatilbydernes vilkår. |
| Teknisk | Endringer i én datakilde eller ett registerløp kan påvirke flere kommuner og flere undertjenester samtidig. | Robust endringshåndtering, testmiljø, tydelig dokumentasjon og trinnvis innføring. |
| Sikkerhet | Samlet tilgang til flere typer registerdata øker konsekvensen av feil i oppsett eller tilgangsstyring. | Rollebasert styring, dataminimering, logging og klare rutiner for lokal forvaltning. |
| Leverandør | Kommunene blir avhengige av KS Digital som tilgangslag og av eksterne datakilder som kan endre vilkår og grensesnitt. | Tydelige avtaler, dokumenterte grensesnitt og aktiv koordinering med datatilbyderne. |
| Brukeropplevelse | Verdien svekkes hvis registeropplysninger ikke er godt tilpasset lokale arbeidsprosesser eller blir for fragmentert mellom undertjenestene. | God veiledning, tydelig produktavgrensning og separate beskrivelser av de viktigste undertjenestene. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-register/
- https://forvaltning.fiks.ks.no/
- https://ksdigital.no/avtaler-og-priser/fakturalinjer/
- https://ksdigital.no/tjenestene/segmentsamarbeid/

## Plattform
Fiks register er en fellestjeneste på KS Digitals Fiks-plattform og fungerer som overordnet registerfamilie for kommunal bruk av nasjonale registerdata.

**Fakta:**
- Tjenesten kan brukes både via nettsideløsning i Fiks forvaltning og gjennom integrasjon mot fagsystemer.
- KS Digital beskriver egen tilgangsstyring i tillegg til brukeradministrasjonen på Fiks-plattformen.
- Produktområdet omfatter flere undertjenester med egne kilder, avtaler og prismodeller.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full teknisk driftsarkitektur, detaljert implementasjonsmodell per registerløp og intern prioritering av hvilke nye registre som kobles på først.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme tjenestegrunnlag kan brukes av mange kommuner og fylkeskommuner med likeartede behov for registerdata.
- Gjenbruksverdien ligger i samlet tilgangsmønster, tilgangsstyring og felles forvaltning av registerbruk.
- Produktet er mer gjenbrukbart som registerfamilie og tilgangslag enn som selvstendig dataløsning.

**Vanlige kombinasjoner med andre produkter:**
- Fiks-plattformen for felles identitets-, integrasjons- og forvaltningsmønster.
- Fiks forvaltning for manuelle oppslag og lokal administrasjon.
- Undertjenester som Fiks folkeregister og Fiks skatte- og inntektsopplysninger når kommunen trenger spesifikke datakilder og hjemmelsløp.

**Kildekode:** Ikke offentlig dokumentert for selve tjenesten. KS Digital publiserer klientbibliotek og SDK-er for Fiks-plattformen på [github.com/ks-no](https://github.com/ks-no), flere av dem under MIT-lisens.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** - produktet gjør det enklere for kommunal sektor å bruke autoritative registerdata fra andre virksomheter på en kontrollert måte.
- **P6: Lag digitale løsninger som støtter samhandling** - løsningen gir et mer standardisert samhandlingsmønster for registeroppslag og bruk av nasjonale datakilder på tvers av aktører.
- **Spenning og begrensning:** Det felles tilgangslaget gir god samordning, men innebærer også avhengighet til KS Digital som mellomledd og stiller høye krav til lokal rolleforvaltning og avgrensning av tjenstlig behov.

## Finansiering
**Fakta:** KS Digital opplyser at Fiks register har en fastpris, og at det i tillegg finnes egne fastpriser for skatte- og inntektsopplysninger og kjøretøyregisteret. KS beskriver også at segmentsamarbeidet med Skatteetaten inngår i grunnfinansieringen som kommunene betaler for tjenestene.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full finansieringsmodell for hele registerfamilien, inkludert hvordan kostnader fordeles mellom grunnprodukt, undertjenester og sentralt segmentansvar utover det som fremgår av publiserte fakturalinjer.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsiden, tjenesteplasseringen og prisinformasjonen ligger hos KS Digital. |
| Driftsansvar | KS Digital | Tjenesten leveres på Fiks-plattformen, men full intern driftsmodell er ikke offentlig detaljert dokumentert. |
| Budsjettansvar | KS Digital, delvis offentlig dokumentert | Grunnfinansiering og prismodell er omtalt, men full budsjettstyring er ikke publisert. |
| Styringsmodell | KS Digital forvalter og drifter løsningen, med strategisk forankring i KS | Fremgår av produktsidene og siden om segmentsamarbeid. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-register/
- https://ksdigital.no/avtaler-og-priser/fakturalinjer/
- https://ksdigital.no/tjenestene/segmentsamarbeid/
- https://forvaltning.fiks.ks.no/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/operative-ressurs-canvas.system.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v2-codex.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/67-FIKS-Folkeregister-produkt-canvas-v2-codex.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v2-codex.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/ (hentet 2026-05-26)
- Nettkilde: https://ksdigital.no/avtaler-og-priser/fakturalinjer/ (hentet 2026-05-26)
- Nettkilde: https://ksdigital.no/tjenestene/segmentsamarbeid/ (hentet 2026-05-26)

## Endringer fra forrige versjon
### Analyseforbedringer
- Oppdatert kildegrunnlaget med ny kontroll av produktside, prismodell og segmentsamarbeid 2026-05-26.
- Presisert at Fiks register må forstås som overordnet registerfamilie med felles tilgangsstyring, ikke som ett enkelt register.
- Tydeliggjort KS Digital som operativ eier, forvalter og driftsansvarlig for løsningen.

### Tekstlige forbedringer
- Utvidet beslutningsstøtten med typiske brukssituasjoner og når produktet normalt ikke er førstevalg.
- Strammet inn avgrensningen mot undertjenester og underliggende datakilder.
- Lagt til tydeligere gjenbruks- og prinsippvurderinger, inkludert sentrale spenninger og begrensninger.
