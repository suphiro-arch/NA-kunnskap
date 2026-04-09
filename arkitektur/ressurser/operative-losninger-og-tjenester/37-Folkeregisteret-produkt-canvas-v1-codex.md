# Produkt-canvas: Folkeregisteret

## Navn
Folkeregisteret

## Ressurs ID
SKATT-001

## Status/Livsfase
**Produksjon** - etablert nasjonalt personregister og statlig felleskomponent for grunndata om personer.

**Fakta:** Skatteetaten beskriver Folkeregisteret som samfunnets sentrale register over personer som er eller har vÃ¦rt bosatt i Norge, eller som har en tilknytning til Norge som gjÃ¸r at de trenger administrativt identifikasjonsnummer. Folkeregisteret omtales ogsÃ¥ som en nasjonal felleskomponent pÃ¥ linje med Enhetsregisteret og Matrikkelen.

## Modenhet
**HÃ¸y modenhet** - innarbeidet og samfunnskritisk grunndataregister:
- Registeret danner grunnlag for blant annet skattemanntall, valgmanntall og befolkningsstatistikk.
- BÃ¥de offentlige og private virksomheter bruker opplysninger fra Folkeregisteret i stor skala.
- Skatteetaten tilbyr bÃ¥de brukerrettede oppslag og delingstjenester for virksomheter med hjemmel.
- Registeret er tett knyttet til sentrale rettigheter, plikter og identitetsforvaltning i samfunnet.

**Deduksjon:** Modenheten er svÃ¦rt hÃ¸y fordi Folkeregisteret er en grunnforutsetning for mange digitale og administrative prosesser. Samtidig er verdien avhengig av at registrerte opplysninger er korrekte og oppdaterte.

## Kort beskrivelse
Folkeregisteret er det nasjonale grunndataregisteret for personopplysninger i Norge. Produktet forvalter autoritative opplysninger om identitet, navn, adresse, statsborgerskap, familierelasjoner, sivilstand og andre sentrale forhold som mange offentlige og private aktÃ¸rer bygger sine tjenester pÃ¥. Folkeregisteret er derfor mer enn en innbyggertjeneste for oppdatering og attester: det er den sentrale registerressursen som gir samfunnet ett felles og pÃ¥litelig persongrunnlag.

## Kapabiliteter
- **Datakilder: Grunndata** er kjernefunksjonen ved at Folkeregisteret er den autoritative kilden for sentrale personopplysninger i Norge.
- **Datautveksling og integrasjon: Dele data med andre** gjÃ¸r opplysninger tilgjengelige for andre virksomheter gjennom kontrollerte delingstjenester og oppslag basert pÃ¥ hjemmel.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Skatteetatens beskrivelser av Folkeregisteret og delingstjenestene.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Skatteetatens sider `Dette er Folkeregisteret`, `Folkeregister` og informasjon om delingstjenestene.

Dokumenterte mÃ¥l:
- VÃ¦re samfunnets sentrale register over personer.
- Gi grunnlag for sentrale offentlige funksjoner som skatt, valg og statistikk.
- GjÃ¸re folkeregisteropplysninger tilgjengelige for virksomheter som har rettslig grunnlag for Ã¥ bruke dem.

Operative mÃ¥l utledet fra de samme kildene:
- Gi samfunnet ett felles persongrunnlag i stedet for mange parallelle kopier og identitetsvarianter.
- Bidra til at rettigheter og plikter kan ivaretas pÃ¥ et mer korrekt og effektivt grunnlag.
- StÃ¸tte digital samhandling ved at opplysninger kan deles og brukes i kontrollerte grensesnitt.

## Brukerbehov
- Offentlige virksomheter trenger et felles og autoritativt register for personopplysninger.
- Private virksomheter med hjemmel trenger pÃ¥litelig persongrunnlag i tjenester som bank, forsikring og arbeidsliv.
- Innbyggere trenger tilgang til egne opplysninger og mulighet til Ã¥ melde endringer og be om attester.
- ForvaltningsmiljÃ¸er trenger et register som kan stÃ¸tte bÃ¥de lÃ¸pende drift, deling og kontroll.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Offentlige virksomheter | PÃ¥litelige personopplysninger | Saksbehandling, rettighetsforvaltning, statistikk og beredskap | StÃ¸rste og viktigste gjenbrukergruppe |
| Private virksomheter med hjemmel | Verifiserte personopplysninger | Bank, forsikring, arbeidsliv og andre regulerte tjenester | MÃ¥ ha rettslig grunnlag for bruk |
| Innbyggere | Innsyn og oppdatering av egne opplysninger | Flytting, attester, navneendring og kontroll av egne data | MÃ¸ter produktet ogsÃ¥ som sluttbrukertjeneste |
| Skatteetaten og registerforvaltning | Drift, kvalitet og deling | Sentral registerforvaltning og tilgangsstyring | Folkeregistermyndigheten ligger hos Skatteetaten |
| Forskning og analyseaktÃ¸rer | Korrekt persongrunnlag der hjemmel finnes | Statistikker, analyser og forskning | Bruk styres av hjemmel og tilgangsvilkÃ¥r |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
**Autoritativ registrering av personopplysninger.** Folkeregisteret forvalter sentrale personopplysninger som mange andre tjenester og registre bygger videre pÃ¥. Dette er produktets viktigste funksjon og gjÃ¸r registeret relevant i nesten alle sektorer som trenger sikker og entydig identifisering av personer.

**Nasjonalt felles identitets- og persongrunnlag.** Registeret gir samfunnet Ã©n felles kilde for navn, adresse, statsborgerskap, sivilstand, fÃ¸dsel, dÃ¸dsfall og relasjoner. Det gjÃ¸r Folkeregisteret til en grunnmur for bÃ¥de offentlig forvaltning og deler av privat sektor.

**TilgjengeliggjÃ¸ring gjennom delingstjenester og oppslag.** Skatteetaten beskriver at folkeregisteropplysninger hovedsakelig deles elektronisk gjennom delingstjenester som API-er, og at det ogsÃ¥ finnes brukergrensesnitt for oppslag. Produktet er derfor bÃ¥de registerkjerne og delt informasjonsressurs for andre aktÃ¸rer.

**InnbyggernÃ¦r forvaltning av egne opplysninger.** Folkeregisteret omfatter ogsÃ¥ brukerrettede lÃ¸p for Ã¥ melde flytting, se egne opplysninger, fÃ¥ attester og endre registrerte forhold. Det gjÃ¸r produktet til mer enn et backend-register, men den tverrsektorielle verdien ligger fÃ¸rst og fremst i registerfunksjonen og delingen av grunndata.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Sentralt personregister for Norge | Faglige beslutninger om rettigheter i andre tjenester |
| Autoritative grunndata om personer | Lokal saksbehandling hos virksomheter som bruker registeret |
| Delingstjenester og oppslag for virksomheter med hjemmel | Full erstatning for lokale kundedata eller fagsystemdata |
| Innbyggerrettede lÃ¸p for oppdatering og attester | Generell identitetsbekreftelse utover det Folkeregisteret registrerer |
| Historikk og oppdatering av registrerte forhold | Autorisasjonsregler i tjenestene som bruker opplysningene |

## Veikart over kommende funksjonalitet
**Fakta fra Skatteetatens kilder (kontrollert 2026-03-27):**
- Skatteetaten publiserer lÃ¸pende informasjon om delingstjenester, oppslag og rettslige rammer i FolkeregisterhÃ¥ndboken og delingssidene.
- Registeret beskrives som dynamisk og lÃ¸pende oppdatert, med stor betydning for mange tjenester.

**Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Et samlet, tidsfestet veikart for hele Folkeregisteret er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til Ã¥ vÃ¦re rettet mot bedre delingstjenester, hÃ¸y datakvalitet og tydeligere samspill mellom register, oppslag og digital bruk hos andre aktÃ¸rer.

## Forretningsverdi/Verdiforslag
### For offentlig sektor
- Gir ett felles og autoritativt persongrunnlag pÃ¥ tvers av sektorer.
- Reduserer behovet for lokale kopier og motstridende personopplysninger.
- UnderstÃ¸tter mer korrekt og effektiv saksbehandling og rettighetsforvaltning.

### For private virksomheter
- GjÃ¸r det mulig Ã¥ bygge regulerte tjenester pÃ¥ pÃ¥litelige personopplysninger der hjemmel finnes.
- Reduserer feil og usikkerhet knyttet til identitet og adresseopplysninger.

### For innbyggere
- Gir bedre forutsigbarhet nÃ¥r offentlige og private aktÃ¸rer bygger pÃ¥ samme registergrunnlag.
- Gir mulighet til Ã¥ se og rette egne opplysninger og Ã¥ fÃ¥ dokumentasjon ved behov.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Datakvalitet | Feil i registeret kan pÃ¥virke mange tjenester og rettigheter samtidig | LÃ¸pende oppdatering, retting og tydelige ansvarslinjer |
| Juridisk og personvern | Feil utlevering eller bruk uten hjemmel kan gi alvorlige personvernbrudd | Streng tilgangsstyring, hjemmelsvurdering og kontrollert deling |
| Teknisk | Endringer i delingstjenester eller integrasjoner kan ramme mange brukere samtidig | Robust endringsforvaltning og god varsling til brukerne |
| Samfunnsavhengighet | Store deler av forvaltningen og privat sektor er avhengige av opplysningene | HÃ¸y forvaltningskvalitet og tydelig prioritering av samfunnskritisk drift |
| Brukeropplevelse | Feil eller forsinkelser i oppdatering kan gi mistillit til registeret | Bedre innsyn, tydelig veiledning og effektive rettelÃ¸p |

## Kanaler
- Folkeregisteret: https://www.skatteetaten.no/person/folkeregister/
- Dette er Folkeregisteret: https://www.skatteetaten.no/person/folkeregister/om/om/
- Bruke data fra Skatteetaten: https://www.skatteetaten.no/deling/
- FÃ¥ tilgang til data fra Folkeregisteret: https://www.skatteetaten.no/nn/deling/folkeregisteret/intro/fa-tilgang/
- Delingstjenestene: https://www.skatteetaten.no/en/rettskilder/type/handboker/folkeregisterhandboken/gjeldende/kapittel10-utlevering-av-opplysninger-fra-registeret/ID-10-1.001/ID-10-1.003/
- Mine opplysninger i Folkeregisteret: https://www.skatteetaten.no/nn/skjema/opplysninger-i-folkeregisteret/

## Plattform
Folkeregisteret er et nasjonalt register- og delingssystem for personopplysninger, forvaltet av Skatteetaten som folkeregistermyndighet.

**Fakta:** Skatteetaten beskriver bÃ¥de registerkjerne, innbyggerlÃ¸p og elektroniske delingstjenester som del av produktomrÃ¥det. Produktet omfatter derfor bÃ¥de sentral registerforvaltning, oppslag og API-basert tilgjengeliggjÃ¸ring av data.

**Ikke offentlig dokumentert i brukte kilder:** Full intern systemarkitektur, detaljert teknologistakk og full driftsmodell for plattformen.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet er laget for Ã¥ vÃ¦re felles persongrunnlag for hele samfunnet.
- Det er sÃ¦rlig relevant nÃ¥r behovet er autoritative personopplysninger og kontrollert datadeling.
- Det er mindre relevant dersom behovet gjelder fagspesifikke vurderinger som bygger videre pÃ¥ folkeregisterdata, men som mÃ¥ lÃ¸ses i andre tjenester.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at Folkeregisteret tilbyr autoritative persondata som kan brukes pÃ¥ tvers av sektorer.
- **P5: Del og gjenbruk lÃ¸sninger** styrkes ved at samfunnet bygger pÃ¥ samme register i stedet for parallelle personregistre.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** stÃ¸ttes fordi mange aktÃ¸rer kan bruke samme persongrunnlag gjennom kontrollerte delingslÃ¸p.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** er sentralt fordi registerkvalitet, sporbarhet og kontrollert tilgang er avgjÃ¸rende for tillit til bruk av personopplysninger.

## Finansiering
- **Fakta:** Delingstjenestene fra folkeregistermyndigheten beskrives som vederlagsfrie.
- **Fakta:** Detaljert samlet finansieringsmodell for hele Folkeregisteret er ikke verifisert i denne arbeidsÃ¸kten.
- **Deduksjon:** Produktet finansieres i hovedsak som nasjonal registerforvaltning, kombinert med kostnader hos brukerne knyttet til egen innfÃ¸ring og integrasjon.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Skatteetaten | Skatteetaten beskriver Folkeregisteret som egen registerressurs og folkeregistermyndighet |
| Driftsansvar | Skatteetaten | Delings- og forvaltningssidene peker til Skatteetaten som operativ forvalter |
| Budsjett- og forvaltningsansvar | Skatteetaten | Registeret er del av Skatteetatens samfunnsoppdrag og delingsforvaltning |
| Styringsmodell | Skatteetaten som folkeregistermyndighet, med bred bruk pÃ¥ tvers av sektorer | Produktsidene og FolkeregisterhÃ¥ndboken |

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

