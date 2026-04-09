# Produkt-canvas: Folkeregisteret

## Navn
Folkeregisteret

## Ressurs ID
SKATT-001

## Status/Livsfase
**Produksjon** - etablert nasjonalt personregister og statlig felleskomponent for grunndata om personer.

**Fakta:** Skatteetaten beskriver Folkeregisteret som samfunnets sentrale register over personer som er eller har vært bosatt i Norge, eller som har en tilknytning til Norge som gjør at de trenger administrativt identifikasjonsnummer. Folkeregisteret omtales også som en nasjonal felleskomponent på linje med Enhetsregisteret og Matrikkelen.

## Modenhet
**Høy modenhet** - innarbeidet og samfunnskritisk grunndataregister:
- Registeret danner grunnlag for blant annet skattemanntall, valgmanntall og befolkningsstatistikk.
- Både offentlige og private virksomheter bruker opplysninger fra Folkeregisteret i stor skala.
- Skatteetaten tilbyr både brukerrettede oppslag og delingstjenester for virksomheter med hjemmel.
- Registeret er tett knyttet til sentrale rettigheter, plikter og identitetsforvaltning i samfunnet.

**Deduksjon:** Modenheten er svært høy fordi Folkeregisteret er en grunnforutsetning for mange digitale og administrative prosesser. Samtidig er verdien avhengig av at registrerte opplysninger er korrekte og oppdaterte.

## Kort beskrivelse
Folkeregisteret er det nasjonale grunndataregisteret for personopplysninger i Norge. Produktet forvalter autoritative opplysninger om identitet, navn, adresse, statsborgerskap, familierelasjoner, sivilstand og andre sentrale forhold som mange offentlige og private aktører bygger sine tjenester på. Folkeregisteret er derfor mer enn en innbyggertjeneste for oppdatering og attester: det er den sentrale registerressursen som gir samfunnet ett felles og pålitelig persongrunnlag.

## Kapabiliteter
- **Datakilder: Grunndata** er kjernefunksjonen ved at Folkeregisteret er den autoritative kilden for sentrale personopplysninger i Norge.
- **Datautveksling og integrasjon: Dele data med andre** gjør opplysninger tilgjengelige for andre virksomheter gjennom kontrollerte delingstjenester og oppslag basert på hjemmel.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Skatteetatens beskrivelser av Folkeregisteret og delingstjenestene.

## Produktmål
**Primærkilder:** Skatteetatens sider `Dette er Folkeregisteret`, `Folkeregister` og informasjon om delingstjenestene.

Dokumenterte mål:
- Være samfunnets sentrale register over personer.
- Gi grunnlag for sentrale offentlige funksjoner som skatt, valg og statistikk.
- Gjøre folkeregisteropplysninger tilgjengelige for virksomheter som har rettslig grunnlag for å bruke dem.

Operative mål utledet fra de samme kildene:
- Gi samfunnet ett felles persongrunnlag i stedet for mange parallelle kopier og identitetsvarianter.
- Bidra til at rettigheter og plikter kan ivaretas på et mer korrekt og effektivt grunnlag.
- Støtte digital samhandling ved at opplysninger kan deles og brukes i kontrollerte grensesnitt.

## Brukerbehov
- Offentlige virksomheter trenger et felles og autoritativt register for personopplysninger.
- Private virksomheter med hjemmel trenger pålitelig persongrunnlag i tjenester som bank, forsikring og arbeidsliv.
- Innbyggere trenger tilgang til egne opplysninger og mulighet til å melde endringer og be om attester.
- Forvaltningsmiljøer trenger et register som kan støtte både løpende drift, deling og kontroll.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Offentlige virksomheter | Pålitelige personopplysninger | Saksbehandling, rettighetsforvaltning, statistikk og beredskap | Største og viktigste gjenbrukergruppe |
| Private virksomheter med hjemmel | Verifiserte personopplysninger | Bank, forsikring, arbeidsliv og andre regulerte tjenester | Må ha rettslig grunnlag for bruk |
| Innbyggere | Innsyn og oppdatering av egne opplysninger | Flytting, attester, navneendring og kontroll av egne data | Møter produktet også som sluttbrukertjeneste |
| Skatteetaten og registerforvaltning | Drift, kvalitet og deling | Sentral registerforvaltning og tilgangsstyring | Folkeregistermyndigheten ligger hos Skatteetaten |
| Forskning og analyseaktører | Korrekt persongrunnlag der hjemmel finnes | Statistikker, analyser og forskning | Bruk styres av hjemmel og tilgangsvilkår |

## Hovedfunksjoner
### Primære funksjoner
**Autoritativ registrering av personopplysninger.** Folkeregisteret forvalter sentrale personopplysninger som mange andre tjenester og registre bygger videre på. Dette er produktets viktigste funksjon og gjør registeret relevant i nesten alle sektorer som trenger sikker og entydig identifisering av personer.

**Nasjonalt felles identitets- og persongrunnlag.** Registeret gir samfunnet én felles kilde for navn, adresse, statsborgerskap, sivilstand, fødsel, dødsfall og relasjoner. Det gjør Folkeregisteret til en grunnmur for både offentlig forvaltning og deler av privat sektor.

**Tilgjengeliggjøring gjennom delingstjenester og oppslag.** Skatteetaten beskriver at folkeregisteropplysninger hovedsakelig deles elektronisk gjennom delingstjenester som API-er, og at det også finnes brukergrensesnitt for oppslag. Produktet er derfor både registerkjerne og delt informasjonsressurs for andre aktører.

**Innbyggernær forvaltning av egne opplysninger.** Folkeregisteret omfatter også brukerrettede løp for å melde flytting, se egne opplysninger, få attester og endre registrerte forhold. Det gjør produktet til mer enn et backend-register, men den tverrsektorielle verdien ligger først og fremst i registerfunksjonen og delingen av grunndata.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Sentralt personregister for Norge | Faglige beslutninger om rettigheter i andre tjenester |
| Autoritative grunndata om personer | Lokal saksbehandling hos virksomheter som bruker registeret |
| Delingstjenester og oppslag for virksomheter med hjemmel | Full erstatning for lokale kundedata eller fagsystemdata |
| Innbyggerrettede løp for oppdatering og attester | Generell identitetsbekreftelse utover det Folkeregisteret registrerer |
| Historikk og oppdatering av registrerte forhold | Autorisasjonsregler i tjenestene som bruker opplysningene |

## Veikart over kommende funksjonalitet
**Fakta fra Skatteetatens kilder (kontrollert 2026-03-27):**
- Skatteetaten publiserer løpende informasjon om delingstjenester, oppslag og rettslige rammer i Folkeregisterhåndboken og delingssidene.
- Registeret beskrives som dynamisk og løpende oppdatert, med stor betydning for mange tjenester.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et samlet, tidsfestet veikart for hele Folkeregisteret er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til å være rettet mot bedre delingstjenester, høy datakvalitet og tydeligere samspill mellom register, oppslag og digital bruk hos andre aktører.

## Forretningsverdi/Verdiforslag
### For offentlig sektor
- Gir ett felles og autoritativt persongrunnlag på tvers av sektorer.
- Reduserer behovet for lokale kopier og motstridende personopplysninger.
- Understøtter mer korrekt og effektiv saksbehandling og rettighetsforvaltning.

### For private virksomheter
- Gjør det mulig å bygge regulerte tjenester på pålitelige personopplysninger der hjemmel finnes.
- Reduserer feil og usikkerhet knyttet til identitet og adresseopplysninger.

### For innbyggere
- Gir bedre forutsigbarhet når offentlige og private aktører bygger på samme registergrunnlag.
- Gir mulighet til å se og rette egne opplysninger og å få dokumentasjon ved behov.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Feil i registeret kan påvirke mange tjenester og rettigheter samtidig | Løpende oppdatering, retting og tydelige ansvarslinjer |
| Juridisk og personvern | Feil utlevering eller bruk uten hjemmel kan gi alvorlige personvernbrudd | Streng tilgangsstyring, hjemmelsvurdering og kontrollert deling |
| Teknisk | Endringer i delingstjenester eller integrasjoner kan ramme mange brukere samtidig | Robust endringsforvaltning og god varsling til brukerne |
| Samfunnsavhengighet | Store deler av forvaltningen og privat sektor er avhengige av opplysningene | Høy forvaltningskvalitet og tydelig prioritering av samfunnskritisk drift |
| Brukeropplevelse | Feil eller forsinkelser i oppdatering kan gi mistillit til registeret | Bedre innsyn, tydelig veiledning og effektive retteløp |

## Kanaler
- Folkeregisteret: https://www.skatteetaten.no/person/folkeregister/
- Dette er Folkeregisteret: https://www.skatteetaten.no/person/folkeregister/om/om/
- Bruke data fra Skatteetaten: https://www.skatteetaten.no/deling/
- Få tilgang til data fra Folkeregisteret: https://www.skatteetaten.no/nn/deling/folkeregisteret/intro/fa-tilgang/
- Delingstjenestene: https://www.skatteetaten.no/en/rettskilder/type/handboker/folkeregisterhandboken/gjeldende/kapittel10-utlevering-av-opplysninger-fra-registeret/ID-10-1.001/ID-10-1.003/
- Mine opplysninger i Folkeregisteret: https://www.skatteetaten.no/nn/skjema/opplysninger-i-folkeregisteret/

## Plattform
Folkeregisteret er et nasjonalt register- og delingssystem for personopplysninger, forvaltet av Skatteetaten som folkeregistermyndighet.

**Fakta:** Skatteetaten beskriver både registerkjerne, innbyggerløp og elektroniske delingstjenester som del av produktområdet. Produktet omfatter derfor både sentral registerforvaltning, oppslag og API-basert tilgjengeliggjøring av data.

**Ikke offentlig dokumentert i brukte kilder:** Full intern systemarkitektur, detaljert teknologistakk og full driftsmodell for plattformen.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er laget for å være felles persongrunnlag for hele samfunnet.
- Det er særlig relevant når behovet er autoritative personopplysninger og kontrollert datadeling.
- Det er mindre relevant dersom behovet gjelder fagspesifikke vurderinger som bygger videre på folkeregisterdata, men som må løses i andre tjenester.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at Folkeregisteret tilbyr autoritative persondata som kan brukes på tvers av sektorer.
- **P5: Del og gjenbruk løsninger** styrkes ved at samfunnet bygger på samme register i stedet for parallelle personregistre.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi mange aktører kan bruke samme persongrunnlag gjennom kontrollerte delingsløp.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi registerkvalitet, sporbarhet og kontrollert tilgang er avgjørende for tillit til bruk av personopplysninger.

## Finansiering
- **Fakta:** Delingstjenestene fra folkeregistermyndigheten beskrives som vederlagsfrie.
- **Fakta:** Detaljert samlet finansieringsmodell for hele Folkeregisteret er ikke verifisert i denne arbeidsøkten.
- **Deduksjon:** Produktet finansieres i hovedsak som nasjonal registerforvaltning, kombinert med kostnader hos brukerne knyttet til egen innføring og integrasjon.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Skatteetaten | Skatteetaten beskriver Folkeregisteret som egen registerressurs og folkeregistermyndighet |
| Driftsansvar | Skatteetaten | Delings- og forvaltningssidene peker til Skatteetaten som operativ forvalter |
| Budsjett- og forvaltningsansvar | Skatteetaten | Registeret er del av Skatteetatens samfunnsoppdrag og delingsforvaltning |
| Styringsmodell | Skatteetaten som folkeregistermyndighet, med bred bruk på tvers av sektorer | Produktsidene og Folkeregisterhåndboken |

## Lenke til dokumentasjon
- https://www.skatteetaten.no/person/folkeregister/
- https://www.skatteetaten.no/person/folkeregister/om/om/
- https://www.skatteetaten.no/deling/
- https://www.skatteetaten.no/nn/deling/folkeregisteret/intro/fa-tilgang/
- https://www.skatteetaten.no/en/rettskilder/type/handboker/folkeregisterhandboken/gjeldende/kapittel10-utlevering-av-opplysninger-fra-registeret/ID-10-1.001/ID-10-1.003/
- https://www.skatteetaten.no/nn/skjema/opplysninger-i-folkeregisteret/
- https://www.skatteetaten.no/rettskilder/type/handboker/folkeregisterhandboken/gjeldende/kapittel1-innledende-bestemmelser/ID-1-1.001/ID-1-1.002/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.skatteetaten.no/person/folkeregister/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/person/folkeregister/om/om/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/deling/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/nn/deling/folkeregisteret/intro/fa-tilgang/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/en/rettskilder/type/handboker/folkeregisterhandboken/gjeldende/kapittel10-utlevering-av-opplysninger-fra-registeret/ID-10-1.001/ID-10-1.003/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/rettskilder/type/handboker/folkeregisterhandboken/gjeldende/kapittel1-innledende-bestemmelser/ID-1-1.001/ID-1-1.002/ (kontrollert 2026-03-27)


