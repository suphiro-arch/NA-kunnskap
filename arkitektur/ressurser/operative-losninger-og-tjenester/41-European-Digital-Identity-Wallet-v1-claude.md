# European Digital Identity Wallet

## Navn
European Digital Identity Wallet (EUDI-lommebok)

## Ressurs ID
EU-001

## Status/Livsfase
**Under utvikling** - rettsakten er vedtatt i EU og storskalapiloter er gjennomført, men lommeboka er ikke satt i ordinær drift i Norge.

**Fakta:** Europakommisjonen opplyser at medlemsstatene skal gjøre lommebøker tilgjengelige for alle innbyggere, personer med opphold og virksomheter innen utgangen av 2026. Rammeverket bygger på endringsforordningen til eIDAS, og teknisk grunnlag er beskrevet i Architecture and Reference Framework (ARF). Over 550 organisasjoner i 26 medlemsstater, i tillegg til Norge, Island og Ukraina, har deltatt i storskalapilotene.

**Fakta:** Digdir opplyser at eIDAS 2.0 trådte i kraft i 2024 for EU-landene, at det gjenstår omfattende arbeid med gjennomføringsforordninger, og at Digdirs videre framdrift med den digitale lommeboka avhenger av når eIDAS 2.0 blir norsk lov. Inntil videre gjelder bestemmelsene i eIDAS 1 i Norge.

**Deduksjon:** Livsfasen er ulik i EU og i Norge. For EU som helhet er ressursen i overgang fra utvikling til innføring med frist i 2026. For norsk bruk er den fortsatt under utvikling, fordi det rettslige grunnlaget ikke er på plass.

## Modenhet
**Regulatorisk moden, teknisk under stabilisering, organisatorisk umoden i Norge.**

- Regulatorisk: forordningen er vedtatt i EU, og ARF er publisert som felles teknisk referanseramme. Det gjenstår gjennomføringsforordninger som fastsetter detaljer.
- Teknisk: Kommisjonen publiserer en referanseimplementasjon med åpne kodebiblioteker og modulære komponenter, og fire storskalapiloter er avsluttet mens to pågår.
- Organisatorisk: Digdir har etablert en norsk sandkasse for digitale lommebøker for å bygge kompetanse før regelverket gjelder i Norge, med et eget tillitsrammeverk driftet av Digdir fordi de sentrale EU-registrene ikke er klare og eIDAS 2.0 ennå ikke er norsk rett.
- Markedsmessig: utstedere av attributter, brukersteder og lommebokleverandører er i tidlig fase, og volumet av reelle transaksjoner er lavt sammenlignet med etablerte nasjonale eID-er.

**Deduksjon:** Det svakeste leddet er ikke teknologien, men rekkefølgen mellom norsk regelverk, tilgjengelige attributtutstedere og brukersteder som faktisk godtar lommeboka. En virksomhet som planlegger å bygge på EUDI-lommebok i dag, må regne med at både hjemmel og økosystem kommer etter løsningen.

## Kort beskrivelse
European Digital Identity Wallet er en personlig digital lommebok som innbyggere og virksomheter i EU og EØS skal kunne bruke til å identifisere seg, oppbevare og dele elektroniske attester og signere elektronisk. Lommeboka er en felles europeisk byggestein: rammeverket, tillitsmodellen og grensesnittene er felles, mens selve lommebokløsningene utstedes nasjonalt av eller på vegne av den enkelte staten. Bruken spenner fra offentlige tjenester og bankåpning til førerkort, resepter, utdanningsbevis og representasjon på vegne av en virksomhet.

Lommeboka er brukerstyrt. Innbyggeren har selv kontroll over hvilke opplysninger som deles med hvilket brukersted, og kan dele utvalgte attributter framfor hele dokumenter.

## Kapabiliteter
- **Tillit: Autentisering**
  gir en felles europeisk mekanisme for å verifisere en digital identitet på høyt sikkerhetsnivå, uavhengig av hvilket land brukeren kommer fra. Lommeboka leverer evnen selv, og er ikke avhengig av at brukerstedet har egen innloggingsløsning.

- **Tillit: Signering**
  gjør det mulig for innbyggeren å opprette rettslig bindende elektroniske signaturer direkte fra lommeboka, innenfor det samme tillitsrammeverket.

Koblingene er satt fordi lommeboka selv utsteder og presenterer identitetsbevis og signaturer. Evnen til å bekrefte identitet på tvers av landegrenser ville ikke blitt levert av noen annen ressurs i porteføljen hvis lommeboka ble borte. Lommeboka bruker samtidig attributter fra nasjonale registre og utstedere; den avhengigheten er beskrevet under `Gjenbruk`, ikke som egen kapabilitet.

## Produktmål
**Dokumenterte mål**, slik Europakommisjonen beskriver rammeverket:
- Gi alle innbyggere, personer med opphold og virksomheter i EU tilgang til en digital lommebok innen utgangen av 2026.
- Gjøre det mulig å identifisere seg og dele dokumenterte opplysninger på tvers av landegrenser og sektorer, i både offentlig og privat sektor.
- Gi brukeren kontroll over egne opplysninger gjennom selektiv deling.
- Sikre rettslig gyldighet for elektroniske signaturer og segl i hele EU.

**Utledede operative mål** for norsk sammenheng:
- Redusere behovet for at hver enkelt tjeneste bygger egne mekanismer for å godta utenlandske identiteter.
- Gi et felles format for å dele attester som i dag krever manuell dokumentasjon, som vitnemål, fullmakter og bevis for yrkeskvalifikasjoner.

**Ikke offentlig dokumentert i denne arbeidsøkten:** hvilke norske attributtutstedere som skal prioriteres først, og i hvilken rekkefølge norske tjenester skal ta lommeboka i bruk.

## Brukerbehov
- Innbyggere trenger å kunne bruke sin nasjonale eID og sine dokumenter i andre land uten å møte manuelle prosesser eller papirbaserte bekreftelser.
- Innbyggere trenger å kunne dele bare den opplysningen et brukersted faktisk trenger, framfor å vise fram et helt dokument.
- Virksomheter trenger en forutsigbar måte å godta identiteter og attester fra hele EØS-området på, uten bilaterale avtaler med hver utsteder.
- Offentlige tjenester trenger å kunne betjene EØS-borgere som ikke har norsk fødselsnummer eller norsk eID.
- Utstedere av attester trenger et felles format og en felles tillitsmodell, slik at attesten kan brukes hos mange brukersteder.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Innbyggere i EØS | Identifisere seg og dele attester på tvers av land | Offentlige tjenester, bank, reise, utdanning | Primærbruker; har kontroll over delingen |
| Virksomheter som brukersted | Godta identitet og attester uten egne avtaler per utsteder | Innlogging, kundekontroll, kvalifikasjonskontroll | Må registrere seg som brukersted i tillitsrammeverket |
| Utstedere av attributter og attester | Utstede verifiserbare bevis i felles format | Vitnemål, førerkort, fullmakter, resepter | Krever tilpasning av registre og utstedelsesløp |
| Digdir som nasjonal koordinator | Samordne norsk innføring og tillitsrammeverk | Sandkasse, tillitsliste, veiledning | Koordinerer, men eier ikke rammeverket |
| Digitaliserings- og forvaltningsdepartementet | Gjennomføre eIDAS 2.0 i norsk rett | Regelverksarbeid | Avgjør når løsningen kan tas i ordinær bruk i Norge |
| Lommebokleverandører | Bygge og drifte lommebokapplikasjoner | Mobilapp og bakenforliggende tjenester | Nasjonalt utpekt, ikke fritt marked |

## Hovedfunksjoner
Lommeboka har tre operative hovedfunksjoner. Den første er **identifisering og autentisering**: brukeren viser fram et personidentifikasjonsbevis fra lommeboka, og brukerstedet kan verifisere at beviset er utstedt av en godkjent utsteder og ikke er tilbakekalt. Dette erstatter ikke nasjonale eID-er, men gir en felles europeisk vei inn for brukere som ikke har lokal eID i landet de bruker tjenesten i.

Den andre er **oppbevaring og selektiv deling av attester**. Lommeboka lagrer elektroniske attester om attributter, for eksempel alder, førerkort, utdanningsbevis eller yrkeskvalifikasjon. Brukeren kan dele enkeltattributter framfor hele dokumentet, slik at et brukersted som bare trenger å vite at brukeren er over 18 år, ikke får fødselsdato og navn på kjøpet.

Den tredje er **signering**. Lommeboka skal kunne opprette elektroniske signaturer med rettslig virkning i hele EU, slik at avtaleinngåelse kan skje i samme flate som identifiseringen.

Rundt disse funksjonene ligger et felles tillitsrammeverk med registre over utstedere og brukersteder, og et sett tekniske grensesnitt beskrevet i ARF. For en norsk virksomhet betyr det at både brukerflaten, integrasjonsflaten mot lommeboka og registreringen som brukersted må håndteres, ikke bare det tekniske grensesnittet.

### Typiske brukssituasjoner (generisk)
- En EØS-borger uten norsk eID skal logge inn på en norsk offentlig tjeneste.
- En innbygger skal dokumentere en yrkeskvalifikasjon eller et vitnemål fra et annet land i en norsk søknadsprosess.
- Et brukersted skal kontrollere en enkeltopplysning, som aldersgrense, uten å samle inn flere personopplysninger enn nødvendig.
- En innbygger skal signere en avtale digitalt på tvers av landegrenser.

### Når European Digital Identity Wallet normalt ikke er førstevalg
- Når brukeren har norsk eID og tjenesten bare betjener norske brukere. Da er `ID-porten` fortsatt den enkleste og mest modne veien.
- Når løsningen skal settes i drift før eIDAS 2.0 er gjennomført i norsk rett, fordi tillitsrammeverket da ikke har rettslig forankring i Norge.
- Når behovet er maskin-til-maskin-tilgang uten en person i løkka. Lommeboka forutsetter en brukerstyrt handling, og `Maskinporten` dekker det maskinelle behovet.
- Når behovet er rettigheter og roller på vegne av en virksomhet i norsk kontekst. Dette dekkes i dag av `Altinn Autorisasjon`, og virksomhetslommebøker er fortsatt under regelverksarbeid i EU.

### Scope og avgrensning
Inngår: felles rammeverk for lommebok, tillitsmodell, formater for elektroniske attester, referanseimplementasjon og krav til nasjonal utstedelse.

Inngår ikke: den enkelte nasjonale lommebokapplikasjonen, som utstedes nasjonalt; innholdet i attestene, som eies av den enkelte utsteder; og norsk tilgangsstyring for virksomheter, som ligger i `Altinn Autorisasjon`.

Ressursen beskriver det europeiske rammeverket. Den norske implementeringen, inkludert sandkassen og en eventuell norsk lommebok, er et eget spor som ikke er registrert som egen ressurs i denne oversikten.

## Veikart over kommende funksjonalitet
**Fakta:** Kommisjonen har satt utgangen av 2026 som frist for at medlemsstatene skal tilby lommebok. Arbeidet med gjennomføringsforordninger pågår, og Kommisjonen har lagt fram lovforslag om virksomhetslommebøker.

**Fakta:** Digdir knytter norsk framdrift til når eIDAS 2.0 blir norsk lov, og har etablert en sandkasse i mellomtiden.

**Ikke offentlig dokumentert i denne arbeidsøkten:** en samlet, datofestet norsk innføringsplan med rekkefølge for attributtutstedere og brukersteder.

## Forretningsverdi/Verdiforslag
**For innbyggere:** færre manuelle dokumentbekreftelser ved flytting, studier, arbeid og reise i EØS, og bedre personvern gjennom at bare nødvendige opplysninger deles.

**For virksomheter og tjenesteeiere:** én felles vei for å godta identiteter og attester fra hele EØS, i stedet for landsspesifikke løsninger eller manuell saksbehandling av utenlandsk dokumentasjon.

**For samfunnet:** lavere terskel for arbeidsmobilitet og grensekryssende tjenester, og en felles tillitsinfrastruktur som reduserer rommet for dokumentforfalskning.

**For offentlig forvaltning:** mulighet til å betjene EØS-borgere uten norsk fødselsnummer i digitale løp, som i dag ofte krever manuelle unntak.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Juridisk | eIDAS 2.0 er ikke gjennomført i norsk rett, og tillitsrammeverket mangler derfor norsk hjemmel | Digdir driver sandkasse med eget tillitsrammeverk i mellomtiden; ordinær bruk avventer lovarbeidet i Digitaliserings- og forvaltningsdepartementet |
| Tidsplan | Fristen i EU er utgangen av 2026, mens norsk framdrift avhenger av lovarbeid som ikke er datofestet | Uavklart. Virksomheter bør ikke planlegge kritiske leveranser mot EU-fristen alene |
| Teknisk | Gjennomføringsforordninger og ARF er fortsatt i endring, slik at integrasjoner kan måtte bygges om | Følg referanseimplementasjonen og sandkassen framfor å bygge mot tidlige utkast |
| Personvern | Selektiv deling er et krav, men brukersteder kan be om mer enn de trenger | Registrering av brukersteder og angivelse av formål er del av rammeverket; praktisk håndheving er ikke dokumentert i denne arbeidsøkten |
| Bruker | Lav utbredelse i starten gir få brukersteder, som igjen gir lav bruk | Uavklart. Verdien avhenger av at både utstedere og brukersteder kommer på plass |
| Leverandør | Nasjonalt utpekte lommebokleverandører kan gi avhengighet til få aktører | Ikke offentlig dokumentert i denne arbeidsøkten for norsk del |

## Kanaler
Lommeboka er først og fremst en mobilapplikasjon for sluttbruker, utstedt nasjonalt. Brukerstedet integrerer gjennom standardiserte grensesnitt beskrevet i ARF og må være registrert i tillitsrammeverket. Det finnes ingen ren maskinell kanal uten brukerhandling: framvisning av attester forutsetter at innbyggeren godkjenner delingen i lommeboka.

Kommisjonen publiserer i tillegg en referanseimplementasjon som utviklingskanal for dem som skal bygge eller teste komponenter.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** driftsmodell og plattformvalg for de nasjonale lommebokløsningene. Det som er kjent, er at lommeboka er en brukerstyrt applikasjon på brukerens egen enhet, at tillitsregistre driftes sentralt i EU-regi, og at Digdir i sandkasseperioden drifter et eget norsk tillitsrammeverk fordi de sentrale registrene ikke er klare.

## Gjenbruk
Rammeverket er bygget for gjenbruk på tvers av land og sektorer: attester utstedt i ett land skal kunne verifiseres i et annet uten bilaterale avtaler. Grensesnittene er åpent spesifisert i ARF, og Kommisjonen publiserer en referanseimplementasjon med åpne kodebiblioteker og modulære komponenter.

Avhengigheter som ikke er kapabiliteter i denne ressursen: lommeboka henter attributter fra nasjonale registre og utstedere, og bygger i norsk sammenheng på at identiteter kan knyttes til Folkeregisteret. Evnen til å levere grunndata hører hos de registrene, ikke her.

**Vanlige kombinasjoner med andre produkter:**
- `ID-porten` for nasjonal innlogging, der lommeboka er alternativet for brukere uten norsk eID.
- `eIDAS-node (Norge)` som dagens mekanisme for grensekryssende eID etter eIDAS 1, og som lommeboka på sikt utfyller.
- `Once-Only Technical System` for utveksling av dokumentasjon mellom myndigheter, der lommeboka dekker det brukerstyrte alternativet.
- `Altinn Autorisasjon` for rettigheter på vegne av virksomhet i norsk kontekst.

**Kildekode:** Åpen kildekode. Kommisjonen publiserer en referanseimplementasjon med kodebiblioteker og modulære komponenter.

**Lisens:** Ikke offentlig dokumentert. Lisensvilkårene for referanseimplementasjonen er ikke kontrollert mot repositoriet i denne arbeidsøkten.

## Støtter arkitekturprinsipper
- **P1: Ta utgangspunkt i brukernes behov**
  Lommeboka er brukerstyrt og gir innbyggeren kontroll over hvilke opplysninger som deles. Selektiv deling er utformet for å redusere unødvendig dokumentasjon i møtet med offentlige og private tjenester.
- **P5: Del og gjenbruk løsninger**
  Rammeverket er felles for hele EØS, med åpne spesifikasjoner og en referanseimplementasjon som medlemsstatene kan bygge på framfor å utvikle hver sin modell.
- **P6: Lag digitale løsninger som støtter samhandling**
  Støttes tydelig ved at identitet og attester kan brukes på tvers av landegrenser og sektorer innenfor samme tillitsmodell.
- **P7: Sørg for tillit til oppgaveløsningen**
  Tillitsrammeverket med registre over utstedere og brukersteder gir et kontrollerbart grunnlag for å stole på attester fra andre land.

**Spenning og begrensning:** Lommeboka står i spenning mot **P2: Ta arkitekturbeslutninger på rett nivå**. Rammeverket er besluttet på europeisk nivå, og nasjonalt handlingsrom er begrenset til gjennomføring. For norske virksomheter betyr det at viktige valg om formater, tillitsmodell og frister er tatt et sted de ikke deltar direkte i. Den er også i praktisk spenning mot **P1: Ta utgangspunkt i brukernes behov** på kort sikt: så lenge få utstedere og brukersteder er på plass, gir lommeboka merarbeid uten tilsvarende brukernytte. En vurdering av bruk bør derfor skille mellom rammeverkets langsiktige verdi og det som faktisk er tilgjengelig i dag.

## Finansiering
**Fakta:** Storskalapilotene er finansiert gjennom EU-programmer, med deltakelse fra over 550 organisasjoner.

**Ikke offentlig dokumentert i denne arbeidsøkten:** finansieringsmodellen for norsk innføring, drift av en norsk lommebok og eventuell brukerbetaling for brukersteder. Digdir opplyser at lommeboka skal være gratis for innbyggere å bruke, men kildene i denne arbeidsøkten sier ikke hvordan drift og utstedelse finansieres.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Regelverk og rammeverk | Europakommisjonen | Kommisjonens sider om European Digital Identity og ARF |
| Nasjonal utstedelse av lommebok | Den enkelte medlemsstaten; for Norge ikke endelig avklart | Kommisjonen om at medlemsstatene skal gjøre lommebøker tilgjengelige |
| Norsk koordinering | Digdir | Digdirs sider om digital lommebok og implementering av eIDAS 2.0 |
| Norsk regelverksansvar | Digitaliserings- og forvaltningsdepartementet | Digdir om at gjennomføringen går gjennom departementets lovarbeid |
| Drift av norsk sandkasse | Digdir | Digdirs dokumentasjon av sandkasse for digitale lommebøker |
| Budsjettansvar for norsk innføring | Ikke offentlig dokumentert i denne arbeidsøkten | - |

## Lenke til dokumentasjon
- Europakommisjonen om European Digital Identity: https://commission.europa.eu/topics/digital-economy-and-society/european-digital-identity_en
- Digdir om implementering av eIDAS 2.0: https://samarbeid.digdir.no/digital-lommebok/implementering-av-eidas-20/2921
- Digdirs dokumentasjon av norsk sandkasse for digitale lommebøker: https://docs.digdir.no/docs/lommebok/wallet_sandbox_summary.html
- Digdir om tre EU-regelverk og én digital infrastruktur: https://www.digdir.no/digitalisering-og-samordning/tre-eu-regelverk-en-digital-infrastruktur/8120

## Kildegrunnlag brukt i utfyllingen
- Europakommisjonen, European Digital Identity, hentet 24. september 2026.
- Digdir, Implementering av eIDAS 2.0, Samarbeidsportalen, hentet 24. september 2026.
- Digdir, Norwegian sandbox for digital wallets, docs.digdir.no, hentet 24. september 2026.
- Digdir, Tre EU-regelverk, én digital infrastruktur, hentet 24. september 2026.
- Lokale kilder: `arkitektur/ressurser/produktnummerering.md`, `arkitektur/kapabiliteter/capabilities.yaml`, `arkitektur/prinsipper/principles.md`, `sources/links.md`.
