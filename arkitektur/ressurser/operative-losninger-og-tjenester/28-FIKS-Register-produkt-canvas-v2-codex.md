# Produkt-canvas: Fiks register

## Navn
Fiks register

## Ressurs ID
KS-004

## Status/Livsfase
**Produksjon** - etablert registertilgangstjeneste i KS Digital for kommunal bruk av flere nasjonale registre gjennom felles oppslag og integrasjon.

**Fakta:** KS Digital beskriver Fiks register som en løsning som deler informasjon fra flere nasjonale registre, og at kommuner og fylkeskommuner kan gjøre oppslag via Fiks forvaltning eller gjennom integrasjon mot fagsystem. Produktsiden viser folkeregister, skatte- og inntektsopplysninger og kjøretøyregister som konkrete tjenester i produktfamilien.

## Modenhet
**Middels til høy funksjonell modenhet** - tjenesten har tydelig produktrolle, publisert forvaltnings- og integrasjonsmønster og flere operative undertjenester i bruk, men fungerer først og fremst som et tilgangslag og ikke som egen datakilde.

- Produktsiden viser at løsningen er tilgjengelig både som nettsideløsning med oppslagsfunksjonalitet og som maskin-til-maskin-integrasjon.
- KS Digital beskriver både sammenstilling av data etter tjenstlig behov og egen tilgangsstyring i tillegg til den generelle brukeradministrasjonen på Fiks-plattformen.
- Pris- og avtaleinformasjonen viser at produktområdet er i ordinær forvaltning, med egne prismodeller for sentrale undertjenester.

**Deduksjon:** Modenheten er høy for felles tilgangsmønster, rolleforvaltning og praktisk bruk i kommunal sektor. Samtidig varierer detaljmodenheten i de enkelte registerløpene, fordi noen undertjenester har mer spesialisert funksjon, regelverk og integrasjonslogikk enn andre.

## Kort beskrivelse
Fiks register er KS Digitals overordnede registertilgangstjeneste for kommunal sektor. Løsningen samler tilgang til flere nasjonale registre i samme tjenesteområde, slik at kommuner og fylkeskommuner kan bruke et felles oppslags- og integrasjonsmønster i stedet for å etablere separate løp mot hver datakilde. Produktet kan brukes både gjennom Fiks forvaltning for saksbehandlere og gjennom integrasjon mot kommunale fagsystemer. I praksis er Fiks register derfor ikke ett enkelt register, men en registerfamilie og et kontrollert tilgangslag som gjør autoritative data fra andre virksomheter operative i kommunale arbeidsprosesser.

## Kapabiliteter
- **Datakilder: Grunndata** er relevant fordi løsningen gjør flere autoritative datakilder anvendbare i kommunal sektor gjennom et samlet og kontrollert tilgangslag.
- **Datautveksling og integrasjon: Bruke data fra andre** er kjernefunksjonen fordi produktet gir kommuner og fylkeskommuner et standardisert løp for å hente og bruke data fra andre virksomheters registre.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals produkt- og prismateriale kontrollert 2026-03-26.

## Produktmål
Dokumenterte mål:
- Gi kommuner og fylkeskommuner tilgang til flere nasjonale registre gjennom Fiks.
- Tilby både oppslagsfunksjonalitet i nettsideløsning og maskin-til-maskin-integrasjon mot fagsystemer.
- Samle registertilganger i et felles tjenestegrunnlag med kontroll på tilgang og tjenstlig behov.

Operative mål utledet fra kildene:
- Redusere behovet for separate oppkoblinger og ulike lokale integrasjonsmønstre mot hver nasjonal datakilde.
- Gjøre det enklere for saksbehandlere og fagsystemer å bruke oppdaterte grunndata direkte fra kilden.
- Skape mer ensartet tilgangsstyring, dataminimering og forvaltningspraksis rundt kommunal bruk av registerdata.

## Brukerbehov
- Kommuner trenger én samlet inngang til flere nasjonale registre i stedet for ulike oppslags- og integrasjonsløsninger.
- Saksbehandlere trenger rask tilgang til relevant registerinformasjon i egne arbeidsprosesser.
- Fagsystemer trenger et standardisert maskin-til-maskin-mønster for bruk av registerdata.
- Forvaltere trenger kontroll over tjenesteområder, tilgangsstyring og hvilke opplysninger som faktisk brukes i kommunen.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Tilgang til flere nasjonale registerdata gjennom ett felles opplegg | Oppslag, saksbehandling og integrert bruk i kommunale tjenester | Primær målgruppe |
| Saksbehandlere | Effektiv oppslagsfunksjon med riktig avgrensede data | Bruk i Fiks forvaltning i operative arbeidsprosesser | Bruker webflaten direkte |
| Fagsystemer og leverandører | Standardisert integrasjon mot registerdata | Integrasjon i kommunale arbeidsprosesser og tjenesteløsninger | Teknisk brukergruppe |
| Fiks-administratorer og forvaltere | Styring av tilgang, roller og bruksmønstre | Oppsett, tilgangsstyring og lokal forvaltning | Viktig for etterlevelse |
| KS Digital | Forvalte registerfamilien og samspillet med eksterne datakilder | Produktforvaltning, avtaler og videreutvikling | Sentral tjenesteforvalter |

## Hovedfunksjoner
### Primære funksjoner
Fiks register sin viktigste funksjon er å samle tilgang til flere nasjonale registre i ett felles kommunalt tjenesteområde. Produktet fungerer derfor ikke som en selvstendig datakilde, men som en overbygning og registerfamilie som gjør det enklere å bruke data fra andre virksomheter i kommunale prosesser. Dette er et viktig skille: verdien ligger i tilgangslaget og i det felles bruksmønsteret, ikke i eierskap til dataene.

Løsningen har to tydelige leveranseflater som må beskrives samlet. Den ene er nettsideløsningen med oppslagsfunksjonalitet i Fiks forvaltning, der saksbehandlere kan hente informasjon direkte i arbeidshverdagen. Den andre er maskin-til-maskin-integrasjon mot fagsystemer. Produktet er derfor bredere enn en administrativ portal, men også bredere enn et rent API. Det er et operativt tilgangslag som støtter både manuell og integrert bruk.

En sentral funksjon er å skjerme kommunene fra å måtte etablere helt ulike oppkoblinger mot hver datakilde. KS Digital beskriver at informasjonen kommer direkte fra kilden, men at løsningen sammenstiller data etter tjenstlige behov. Produktet tilbyr også egen tilgangsstyring i tillegg til den generelle brukeradministrasjonen på Fiks-plattformen. Det betyr at Fiks register ikke bare videresender oppslag, men også legger på styring, avgrensning og et felles kommunalt kontrollnivå.

Produktområdet rommer flere undertjenester med ulik karakter, blant annet folkeregister, skatte- og inntektsopplysninger og kjøretøyregister. Disse må forstås som del av samme overordnede registerfamilie, men ikke som identiske tjenester. Fiks register beskriver derfor den samlede produktrollen: et felles tilgangs- og forvaltningsmønster for nasjonale registerdata i kommunal sektor. Undertjenestene beskriver den spesifikke funksjonen, hjemmelen og arbeidsbruken for hver datakilde.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Samlet tilgang til flere nasjonale registre gjennom ett felles tjenesteområde | Eierskap til de underliggende registrene eller kildedataene |
| Oppslag i Fiks forvaltning og integrasjon mot fagsystemer | Full lokal datalagring eller kommunal registerforvaltning |
| Egen tilgangsstyring og sammenstilling etter tjenstlig behov | Ubegrenset bruk av data uten hjemmel, rolle og behov |
| Overordnet registerfamilie for undertjenester som folkeregister, skatte- og inntektsopplysninger og kjøretøyregister | Detaljert faglogikk for hver enkelt undertjeneste, som beskrives i egne produktfiler |

## Veikart over kommende funksjonalitet
**Fakta:** KS Digital opplyser at de jobber med å koble på flere registre og sammenstille informasjon på tvers. Jeg fant ikke et samlet offentlig roadmap med tidsfestede milepæler utover dette i denne arbeidsøkten.

**Deduksjon:** Videreutviklingen vil trolig være knyttet til flere registerkoblinger, mer finmasket sammenstilling av data og videre modning av de enkelte undertjenestene i samme produktfamilie.

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

## Plattform
Fiks register er en fellestjeneste på KS Digitals Fiks-grunnlag og fungerer som overordnet registerfamilie for kommunal bruk av nasjonale registerdata.

**Fakta:**
- Tjenesten kan brukes både via nettsideløsning i Fiks forvaltning og gjennom integrasjon mot fagsystemer.
- KS Digital beskriver egen tilgangsstyring i tillegg til brukeradministrasjonen på Fiks-plattformen.
- Produktområdet omfatter flere undertjenester med egne datakilder og egne prismodeller.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full teknisk driftsarkitektur, detaljert implementasjonsmodell per registerløp og intern prioritering av hvilke nye registre som kobles på først.

## Gjenbruk
**Høy gjenbruksverdi:**
- Samme tjenestegrunnlag kan brukes av mange kommuner og fylkeskommuner med likeartede behov for registerdata.
- Gjenbruksverdien ligger i samlet tilgangsmønster, tilgangsstyring og felles forvaltning av registerbruk.
- Produktet er mer gjenbrukbart som registerfamilie og tilgangslag enn som selvstendig dataløsning.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** - produktet gjør det enklere for kommunal sektor å bruke autoritative registerdata fra andre virksomheter på en kontrollert måte.
- **P6: Lag digitale løsninger som støtter samhandling** - løsningen gir et mer standardisert samhandlingsmønster for registeroppslag og bruk av nasjonale datakilder på tvers av aktører.

## Finansiering
**Fakta:** KS Digitals fakturalinjer viser at Fiks register har en innbyggerpris for (fylkes)kommuner, og at undertjenestene Folkeregister og Skatte- og inntektsopplysninger har egne fastpriser. Produktsiden opplyser også at enkelte tilganger krever avtaler utover dem som inngås med KS Digital.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full finansieringsmodell for hele registerfamilien, inkludert hvordan kostnader fordeles mellom grunnprodukt og undertjenester utover det som fremgår av publiserte fakturalinjer.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsiden, tjenesteplasseringen og prisinformasjonen ligger hos KS Digital. |
| Driftsansvar | Ikke offentlig detaljert spesifisert i brukte kilder | Må verifiseres i mer tekniske eller kontraktsnære kilder. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Fakturalinjer viser prismodell, men ikke full budsjettstyring. |
| Styringsmodell | KS Digital som felles forvalter av registerfamilien i samspill med eksterne datatilbydere | Fremgår av produktsiden, tilgangsmodellen og avtaleavhengighetene mot datakildene. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/fiks-register/
- https://forvaltning.fiks.ks.no/
- https://ksdigital.no/avtaler-og-priser/fakturalinjer/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/28-FIKS-Register-produkt-canvas-v1-codex.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/67-FIKS-Folkeregister-produkt-canvas-v1-codex.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/68-FIKS-Skatte-og-inntektsopplysninger-produkt-canvas-v1-codex.md`
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/69-FIKS-Kjoretoyregister-produkt-canvas-v1-codex.md`
- Nettkilde: https://ksdigital.no/tjenestene/fiks-register/ (hentet 2026-03-26)
- Nettkilde: https://ksdigital.no/avtaler-og-priser/fakturalinjer/ (hentet 2026-03-26)

## Endringer fra forrige versjon
### Analyseforbedringer
- Oppdatert kildegrunnlag med ny kontroll av produktside og fakturalinjer 2026-03-26.
- Presisert at Fiks register nå må forstås som overordnet registerfamilie med egne undertjenester, ikke bare som en generell oppslagstjeneste.
- Tydeliggjort at løsningen har både nettsideløsning og maskin-til-maskin-integrasjon, og at egen tilgangsstyring er en del av produktrollen.

### Tekstlige forbedringer
- Strammet inn avgrensningen mot undertjenestene `Fiks folkeregister`, `Fiks skatte- og inntektsopplysninger` og `Fiks kjøretøyregister`.
- Skrevet `Hovedfunksjoner` om til forklarende avsnitt som tydeligere beskriver hele produktets operative rolle.
- Gjort produktbeskrivelsen mer presis om hva som inngår i overordnet produkt og hva som bør ligge i de egne undertjenestebeskrivelsene.


