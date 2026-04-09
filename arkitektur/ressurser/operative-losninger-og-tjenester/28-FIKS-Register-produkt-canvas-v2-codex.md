# Produkt-canvas: Fiks register

## Navn
Fiks register

## Ressurs ID
KS-004

## Status/Livsfase
**Produksjon** - etablert registertilgangstjeneste i KS Digital for kommunal bruk av flere nasjonale registre gjennom felles oppslag og integrasjon.

**Fakta:** KS Digital beskriver Fiks register som en lÃ¸sning som deler informasjon fra flere nasjonale registre, og at kommuner og fylkeskommuner kan gjÃ¸re oppslag via Fiks forvaltning eller gjennom integrasjon mot fagsystem. Produktsiden viser folkeregister, skatte- og inntektsopplysninger og kjÃ¸retÃ¸yregister som konkrete tjenester i produktfamilien.

## Modenhet
**Middels til hÃ¸y funksjonell modenhet** - tjenesten har tydelig produktrolle, publisert forvaltnings- og integrasjonsmÃ¸nster og flere operative undertjenester i bruk, men fungerer fÃ¸rst og fremst som et tilgangslag og ikke som egen datakilde.

- Produktsiden viser at lÃ¸sningen er tilgjengelig bÃ¥de som nettsidelÃ¸sning med oppslagsfunksjonalitet og som maskin-til-maskin-integrasjon.
- KS Digital beskriver bÃ¥de sammenstilling av data etter tjenstlig behov og egen tilgangsstyring i tillegg til den generelle brukeradministrasjonen pÃ¥ Fiks-plattformen.
- Pris- og avtaleinformasjonen viser at produktomrÃ¥det er i ordinÃ¦r forvaltning, med egne prismodeller for sentrale undertjenester.

**Deduksjon:** Modenheten er hÃ¸y for felles tilgangsmÃ¸nster, rolleforvaltning og praktisk bruk i kommunal sektor. Samtidig varierer detaljmodenheten i de enkelte registerlÃ¸pene, fordi noen undertjenester har mer spesialisert funksjon, regelverk og integrasjonslogikk enn andre.

## Kort beskrivelse
Fiks register er KS Digitals overordnede registertilgangstjeneste for kommunal sektor. LÃ¸sningen samler tilgang til flere nasjonale registre i samme tjenesteomrÃ¥de, slik at kommuner og fylkeskommuner kan bruke et felles oppslags- og integrasjonsmÃ¸nster i stedet for Ã¥ etablere separate lÃ¸p mot hver datakilde. Produktet kan brukes bÃ¥de gjennom Fiks forvaltning for saksbehandlere og gjennom integrasjon mot kommunale fagsystemer. I praksis er Fiks register derfor ikke ett enkelt register, men en registerfamilie og et kontrollert tilgangslag som gjÃ¸r autoritative data fra andre virksomheter operative i kommunale arbeidsprosesser.

## Kapabiliteter
- **Datakilder: Grunndata** er relevant fordi lÃ¸sningen gjÃ¸r flere autoritative datakilder anvendbare i kommunal sektor gjennom et samlet og kontrollert tilgangslag.
- **Datautveksling og integrasjon: Bruke data fra andre** er kjernefunksjonen fordi produktet gir kommuner og fylkeskommuner et standardisert lÃ¸p for Ã¥ hente og bruke data fra andre virksomheters registre.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals produkt- og prismateriale kontrollert 2026-03-26.

## ProduktmÃ¥l
Dokumenterte mÃ¥l:
- Gi kommuner og fylkeskommuner tilgang til flere nasjonale registre gjennom Fiks.
- Tilby bÃ¥de oppslagsfunksjonalitet i nettsidelÃ¸sning og maskin-til-maskin-integrasjon mot fagsystemer.
- Samle registertilganger i et felles tjenestegrunnlag med kontroll pÃ¥ tilgang og tjenstlig behov.

Operative mÃ¥l utledet fra kildene:
- Redusere behovet for separate oppkoblinger og ulike lokale integrasjonsmÃ¸nstre mot hver nasjonal datakilde.
- GjÃ¸re det enklere for saksbehandlere og fagsystemer Ã¥ bruke oppdaterte grunndata direkte fra kilden.
- Skape mer ensartet tilgangsstyring, dataminimering og forvaltningspraksis rundt kommunal bruk av registerdata.

## Brukerbehov
- Kommuner trenger Ã©n samlet inngang til flere nasjonale registre i stedet for ulike oppslags- og integrasjonslÃ¸sninger.
- Saksbehandlere trenger rask tilgang til relevant registerinformasjon i egne arbeidsprosesser.
- Fagsystemer trenger et standardisert maskin-til-maskin-mÃ¸nster for bruk av registerdata.
- Forvaltere trenger kontroll over tjenesteomrÃ¥der, tilgangsstyring og hvilke opplysninger som faktisk brukes i kommunen.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Kommuner og fylkeskommuner | Tilgang til flere nasjonale registerdata gjennom ett felles opplegg | Oppslag, saksbehandling og integrert bruk i kommunale tjenester | PrimÃ¦r mÃ¥lgruppe |
| Saksbehandlere | Effektiv oppslagsfunksjon med riktig avgrensede data | Bruk i Fiks forvaltning i operative arbeidsprosesser | Bruker webflaten direkte |
| Fagsystemer og leverandÃ¸rer | Standardisert integrasjon mot registerdata | Integrasjon i kommunale arbeidsprosesser og tjenestelÃ¸sninger | Teknisk brukergruppe |
| Fiks-administratorer og forvaltere | Styring av tilgang, roller og bruksmÃ¸nstre | Oppsett, tilgangsstyring og lokal forvaltning | Viktig for etterlevelse |
| KS Digital | Forvalte registerfamilien og samspillet med eksterne datakilder | Produktforvaltning, avtaler og videreutvikling | Sentral tjenesteforvalter |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
Fiks register sin viktigste funksjon er Ã¥ samle tilgang til flere nasjonale registre i ett felles kommunalt tjenesteomrÃ¥de. Produktet fungerer derfor ikke som en selvstendig datakilde, men som en overbygning og registerfamilie som gjÃ¸r det enklere Ã¥ bruke data fra andre virksomheter i kommunale prosesser. Dette er et viktig skille: verdien ligger i tilgangslaget og i det felles bruksmÃ¸nsteret, ikke i eierskap til dataene.

LÃ¸sningen har to tydelige leveranseflater som mÃ¥ beskrives samlet. Den ene er nettsidelÃ¸sningen med oppslagsfunksjonalitet i Fiks forvaltning, der saksbehandlere kan hente informasjon direkte i arbeidshverdagen. Den andre er maskin-til-maskin-integrasjon mot fagsystemer. Produktet er derfor bredere enn en administrativ portal, men ogsÃ¥ bredere enn et rent API. Det er et operativt tilgangslag som stÃ¸tter bÃ¥de manuell og integrert bruk.

En sentral funksjon er Ã¥ skjerme kommunene fra Ã¥ mÃ¥tte etablere helt ulike oppkoblinger mot hver datakilde. KS Digital beskriver at informasjonen kommer direkte fra kilden, men at lÃ¸sningen sammenstiller data etter tjenstlige behov. Produktet tilbyr ogsÃ¥ egen tilgangsstyring i tillegg til den generelle brukeradministrasjonen pÃ¥ Fiks-plattformen. Det betyr at Fiks register ikke bare videresender oppslag, men ogsÃ¥ legger pÃ¥ styring, avgrensning og et felles kommunalt kontrollnivÃ¥.

ProduktomrÃ¥det rommer flere undertjenester med ulik karakter, blant annet folkeregister, skatte- og inntektsopplysninger og kjÃ¸retÃ¸yregister. Disse mÃ¥ forstÃ¥s som del av samme overordnede registerfamilie, men ikke som identiske tjenester. Fiks register beskriver derfor den samlede produktrollen: et felles tilgangs- og forvaltningsmÃ¸nster for nasjonale registerdata i kommunal sektor. Undertjenestene beskriver den spesifikke funksjonen, hjemmelen og arbeidsbruken for hver datakilde.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Samlet tilgang til flere nasjonale registre gjennom ett felles tjenesteomrÃ¥de | Eierskap til de underliggende registrene eller kildedataene |
| Oppslag i Fiks forvaltning og integrasjon mot fagsystemer | Full lokal datalagring eller kommunal registerforvaltning |
| Egen tilgangsstyring og sammenstilling etter tjenstlig behov | Ubegrenset bruk av data uten hjemmel, rolle og behov |
| Overordnet registerfamilie for undertjenester som folkeregister, skatte- og inntektsopplysninger og kjÃ¸retÃ¸yregister | Detaljert faglogikk for hver enkelt undertjeneste, som beskrives i egne produktfiler |

## Veikart over kommende funksjonalitet
**Fakta:** KS Digital opplyser at de jobber med Ã¥ koble pÃ¥ flere registre og sammenstille informasjon pÃ¥ tvers. Jeg fant ikke et samlet offentlig roadmap med tidsfestede milepÃ¦ler utover dette i denne arbeidsÃ¸kten.

**Deduksjon:** Videreutviklingen vil trolig vÃ¦re knyttet til flere registerkoblinger, mer finmasket sammenstilling av data og videre modning av de enkelte undertjenestene i samme produktfamilie.

## Forretningsverdi/Verdiforslag
### For kommuner og fylkeskommuner
- GjÃ¸r nasjonale registeropplysninger lettere tilgjengelige gjennom ett felles kommunalt tilgangsmÃ¸nster.
- Reduserer behovet for Ã¥ etablere og forvalte mange ulike oppkoblinger mot hver datakilde.

### For saksbehandlere og fagmiljÃ¸er
- Gir raskere tilgang til relevante opplysninger i konkrete arbeidsprosesser.
- GjÃ¸r at registerdata i stÃ¸rre grad kan brukes direkte fra kilden og i riktig kontekst.

### For leverandÃ¸rer og sektoren
- Gir et mer ensartet integrasjonspunkt for kommunal bruk av registerdata.
- StÃ¸tter gjenbruk av felles tilgangs- og forvaltningsmÃ¸nstre i stedet for parallelle lokale lÃ¸sninger.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Juridisk | Tilgang til registerdata krever riktig hjemmel, riktig tjenesteomrÃ¥de og korrekt bruk i lokale prosesser. | Tydelig tilgangsstyring, lokal kontroll av behandlingsgrunnlag og kobling til datatilbydernes vilkÃ¥r. |
| Teknisk | Endringer i Ã©n datakilde eller ett registerlÃ¸p kan pÃ¥virke flere kommuner og flere undertjenester samtidig. | Robust endringshÃ¥ndtering, testmiljÃ¸, tydelig dokumentasjon og trinnvis innfÃ¸ring. |
| Sikkerhet | Samlet tilgang til flere typer registerdata Ã¸ker konsekvensen av feil i oppsett eller tilgangsstyring. | Rollebasert styring, dataminimering, logging og klare rutiner for lokal forvaltning. |
| LeverandÃ¸r | Kommunene blir avhengige av KS Digital som tilgangslag og av eksterne datakilder som kan endre vilkÃ¥r og grensesnitt. | Tydelige avtaler, dokumenterte grensesnitt og aktiv koordinering med datatilbyderne. |
| Brukeropplevelse | Verdien svekkes hvis registeropplysninger ikke er godt tilpasset lokale arbeidsprosesser eller blir for fragmentert mellom undertjenestene. | God veiledning, tydelig produktavgrensning og separate beskrivelser av de viktigste undertjenestene. |

## Kanaler
- https://ksdigital.no/tjenestene/fiks-register/
- https://forvaltning.fiks.ks.no/
- https://ksdigital.no/avtaler-og-priser/fakturalinjer/

## Plattform
Fiks register er en fellestjeneste pÃ¥ KS Digitals Fiks-grunnlag og fungerer som overordnet registerfamilie for kommunal bruk av nasjonale registerdata.

**Fakta:**
- Tjenesten kan brukes bÃ¥de via nettsidelÃ¸sning i Fiks forvaltning og gjennom integrasjon mot fagsystemer.
- KS Digital beskriver egen tilgangsstyring i tillegg til brukeradministrasjonen pÃ¥ Fiks-plattformen.
- ProduktomrÃ¥det omfatter flere undertjenester med egne datakilder og egne prismodeller.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full teknisk driftsarkitektur, detaljert implementasjonsmodell per registerlÃ¸p og intern prioritering av hvilke nye registre som kobles pÃ¥ fÃ¸rst.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Samme tjenestegrunnlag kan brukes av mange kommuner og fylkeskommuner med likeartede behov for registerdata.
- Gjenbruksverdien ligger i samlet tilgangsmÃ¸nster, tilgangsstyring og felles forvaltning av registerbruk.
- Produktet er mer gjenbrukbart som registerfamilie og tilgangslag enn som selvstendig datalÃ¸sning.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** - produktet gjÃ¸r det enklere for kommunal sektor Ã¥ bruke autoritative registerdata fra andre virksomheter pÃ¥ en kontrollert mÃ¥te.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** - lÃ¸sningen gir et mer standardisert samhandlingsmÃ¸nster for registeroppslag og bruk av nasjonale datakilder pÃ¥ tvers av aktÃ¸rer.

## Finansiering
**Fakta:** KS Digitals fakturalinjer viser at Fiks register har en innbyggerpris for (fylkes)kommuner, og at undertjenestene Folkeregister og Skatte- og inntektsopplysninger har egne fastpriser. Produktsiden opplyser ogsÃ¥ at enkelte tilganger krever avtaler utover dem som inngÃ¥s med KS Digital.

**Ikke offentlig detaljert dokumentert i brukte kilder:** Full finansieringsmodell for hele registerfamilien, inkludert hvordan kostnader fordeles mellom grunnprodukt og undertjenester utover det som fremgÃ¥r av publiserte fakturalinjer.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktsiden, tjenesteplasseringen og prisinformasjonen ligger hos KS Digital. |
| Driftsansvar | Ikke offentlig detaljert spesifisert i brukte kilder | MÃ¥ verifiseres i mer tekniske eller kontraktsnÃ¦re kilder. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Fakturalinjer viser prismodell, men ikke full budsjettstyring. |
| Styringsmodell | KS Digital som felles forvalter av registerfamilien i samspill med eksterne datatilbydere | FremgÃ¥r av produktsiden, tilgangsmodellen og avtaleavhengighetene mot datakildene. |

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
- Presisert at Fiks register nÃ¥ mÃ¥ forstÃ¥s som overordnet registerfamilie med egne undertjenester, ikke bare som en generell oppslagstjeneste.
- Tydeliggjort at lÃ¸sningen har bÃ¥de nettsidelÃ¸sning og maskin-til-maskin-integrasjon, og at egen tilgangsstyring er en del av produktrollen.

### Tekstlige forbedringer
- Strammet inn avgrensningen mot undertjenestene `Fiks folkeregister`, `Fiks skatte- og inntektsopplysninger` og `Fiks kjÃ¸retÃ¸yregister`.
- Skrevet `Hovedfunksjoner` om til forklarende avsnitt som tydeligere beskriver hele produktets operative rolle.
- Gjort produktbeskrivelsen mer presis om hva som inngÃ¥r i overordnet produkt og hva som bÃ¸r ligge i de egne undertjenestebeskrivelsene.

