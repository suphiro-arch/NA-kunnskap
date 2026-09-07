# VIGO Kodeverk og kodeverksbase

## Navn
VIGO Kodeverk og kodeverksbase

## Ressurs ID
NOVARI-007

## Ressurskategori
Normerende ressurs

## Type standard eller veiledning
Kodeverk, med åpen kodeverksbase for oppslag

## Status/Livsfase
Aktiv. Kodeverket er i løpende bruk i videregående opplæring, og kodeverksbasen er publisert som åpent oppslagsverk. Forvaltningen skjer gjennom en fast faggruppe med deltakere fra flere virksomheter.

## Kort beskrivelse
VIGO Kodeverk er det samlede kodeverket for videregående opplæring. Det kombinerer nasjonale koder for fag, læreplaner og opplæringstilbud fra `Grep`, skoleopplysninger fra Nasjonalt skoleregister, og VIGO-spesifikke koder som fylkeskommunene trenger i inntak, fagopplæring og dokumentasjon.

Kodeverksbasen er den offentlige flaten: et felles, oppdatert og kvalitetssikret oppslagsverk som er åpent for alle.

Kodeverket er satt sammen av tre kilder med ulikt eierskap. Den nasjonale semantikken kommer fra Utdanningsdirektoratet, virksomhetsopplysningene fra det nasjonale skoleregisteret, og det fylkeskommunale påbygget legges til der de nasjonale kildene ikke dekker behovet. Sammensetningen forvaltes i et samarbeid mellom flere virksomheter framfor hos én eier.

## Formål og normerende rolle
Formålet er å gi videregående opplæring ett omforent kodeverk, slik at fag, tilbud og skoler refereres likt på tvers av fylkeskommuner, nasjonale myndigheter og de virksomhetene som bruker utdanningsdata videre.

Den normerende rollen er sammenstillende. VIGO Kodeverk fastsetter ikke læreplaner eller fagkoder — det gjør Utdanningsdirektoratet gjennom `Grep`. Det VIGO Kodeverk normerer, er hvordan de nasjonale kodene brukes sammen med skoleopplysninger og fylkeskommunale koder i det operative arbeidet med inntak, fagopplæring, dokumentasjon og statistikk.

Det gjør ressursen til et bindeledd mer enn en selvstendig standard. Verdien ligger i at sammenstillingen er gjort én gang, kvalitetssikret, og gjort tilgjengelig for alle framfor at hver fylkeskommune bygger sin egen.

## Forpliktelsesnivå og etterlevelse
Kodeverket er styrende i praksis innenfor videregående opplæring, uten at kildene beskriver et formelt krav om bruk.

Bindingen kommer av at kodeverket er forutsetningen for at VIGO-systemet og de tilhørende tjenestene virker. Inntak, føring av opplæring og dokumentasjon bygger på de samme kodene, og en fylkeskommune som avviker, får data som ikke lar seg behandle nasjonalt eller sammenligne med andre fylker.

Etterlevelse skjer gjennom to kanaler. Den ene er systemene selv: kodene er bygget inn i VIGO og de løsningene som henter fra kodeverksbasen. Den andre er faggruppen, der endringer diskuteres og besluttes i fellesskap før de settes i verk.

Kildene beskriver ingen kontroll- eller avviksordning. Nivået er dermed styrende gjennom bruk, ikke gjennom regelverk eller tilsyn.

## Kapabiliteter
- **Informasjonsforvaltning: Informasjonsarkitektur**
  Kodeverket strukturerer fag, tilbud, skoler og VIGO-spesifikke begreper i en samlet modell som brukes likt på tvers av fylkeskommunene.

- **Informasjonsforvaltning: Oversikt over begreper**
  Kodeverksbasen er et åpent og kvalitetssikret oppslagsverk for begrepene som brukes i videregående opplæring.

- **Standardisering: Forvaltningsstandarder**
  Ressursen operasjonaliserer nasjonale koder fra Grep og Nasjonalt skoleregister til en felles praksis i fylkeskommunal sektor.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Fylkeskommunene | Felles koder for inntak og fagopplæring | Inntak, fagopplæring, dokumentasjon | Primærbrukerne, og samtidig deltakere i forvaltningen |
| Novari | Kodegrunnlag for VIGO-tjenestene | Drift og videreutvikling av VIGO | Forvalter kodeverksbasen |
| Lånekassen | Koder for utdanningstilbud i saksbehandling | Vurdering av støtterett | Deltar i faggruppen |
| Statistisk sentralbyrå | Stabile koder for statistikk | Utdanningsstatistikk | Deltar i faggruppen |
| Utdanningsdirektoratet | Sammenheng mellom nasjonale koder og operativ bruk | Læreplanverk og nasjonale registre | Deltar i faggruppen og eier kildekodene i Grep |
| Skoler og opplæringskontorer | Riktige koder ved føring av opplæring | Dokumentasjon og rapportering | Møter kodeverket gjennom fagsystemene |
| Leverandører av skoleadministrative systemer | Maskinlesbart og oppdatert kodegrunnlag | Integrasjon i fagsystem | Kodeverksbasen er åpen for oppslag |

## Normerende innhold
Kodeverket består av tre lag med ulik opprinnelse.

**Nasjonale koder fra Grep.** Fag, læreplaner og opplæringstilbud i Kunnskapsløftet hentes fra Utdanningsdirektoratets database. Dette laget er ikke VIGO sitt eget, og endringer her følger læreplanarbeidet nasjonalt.

**Skoleopplysninger fra Nasjonalt skoleregister.** Hvilke skoler som finnes, og hvem som eier dem, hentes fra det nasjonale registeret framfor å føres lokalt.

**VIGO-spesifikke koder.** Der de nasjonale kildene ikke dekker behovet, legger kodeverket til egne elementer. Kildene nevner skolenumre og varianter av utdanningskoder som eksempler. Dette laget er det fylkeskommunale påbygget, og det er her forvaltningen i faggruppen har reelt handlingsrom.

Kodeverksbasen er publiseringsflaten for hele sammenstillingen, beskrevet som et felles, oppdatert og kvalitetssikret oppslagsverk som er åpent for alle.

## Bruksområde
Kodeverket bør brukes i all systemutvikling og saksbehandling som berører videregående opplæring: inntak, føring av fag og karakterer, fagopplæring, dokumentasjon av oppnådd kompetanse, og statistikkproduksjon.

Det er også relevant i arkitekturarbeid som inngang til semantikken i videregående opplæring, siden det viser hva som er nasjonalt fastsatt og hva som er fylkeskommunalt påbygg.

Ressursen er mindre relevant utenfor videregående opplæring. For grunnskole og barnehage er `Grep` (`UDIR-001`) og `Nasjonale registre for barnehage og grunnopplæring` (`UDIR-002`) de riktige kildene, uten VIGO-påbygget.

## Typiske analyse- og beslutningssituasjoner
- Anskaffelse eller utvikling av skoleadministrativt system for videregående, der støtte for kodeverket bør være et krav
- Vurdering av om et informasjonsbehov i videregående opplæring alt er dekket av eksisterende kodeverk
- Utforming av integrasjoner mellom fylkeskommune, nasjonale myndigheter og virksomheter som bruker utdanningsdata
- Avklaring av hvilket lag en kode hører til, når noe skal endres: nasjonalt i Grep, i skoleregisteret, eller i VIGO-påbygget
- Planlegging ved læreplanreform, der de nasjonale kodene endres og påbygget må følge etter
- Vurdering av hvor et nytt kodebehov bør løses, og om det egentlig hører nasjonalt framfor i sektorpåbygget

## Når ressursen normalt ikke er tilstrekkelig alene
Kodeverket gir begreper, ikke funksjonalitet. Inntak, saksbehandling og dokumentasjon krever `VIGO` (`NOVARI-004`) og de tilhørende tjenestene.

Ved endringer i selve læreplanverket er ikke VIGO Kodeverk kilden. Der må `Grep` (`UDIR-001`) brukes, og VIGO Kodeverk følger etter.

Kodeverket sier heller ingenting om personopplysninger, behandlingsgrunnlag eller tilgangsstyring i de systemene som bruker kodene.

## Scope og avgrensning
Inngår:
- nasjonale koder for fag, læreplaner og opplæringstilbud, hentet fra Grep
- skoleopplysninger hentet fra Nasjonalt skoleregister
- VIGO-spesifikke koder, som skolenumre og varianter av utdanningskoder
- åpen kodeverksbase for oppslag
- felles forvaltning gjennom faggruppe med flere virksomheter

Inngår ikke:
- fastsettelse av læreplaner og nasjonale fagkoder, som skjer hos Utdanningsdirektoratet
- rollen som autoritativ kilde til skoleopplysninger, som ligger i Nasjonalt skoleregister
- personopplysninger om søkere, elever eller lærlinger
- inntaksbehandling, saksbehandling eller dokumentasjonsfunksjonalitet
- kodeverk for grunnskole og barnehage utenfor det videregående løpet

Grensen mot `Grep` (`UDIR-001`) er den viktigste å holde klar: Grep er den nasjonale kilden, VIGO Kodeverk er den fylkeskommunale sammenstillingen og bruken av den. Ved uenighet om en nasjonal fagkode er Grep fasit.

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Faggruppe med deltakere fra fylkeskommunene, Novari IKS, Lånekassen, Statistisk sentralbyrå og Utdanningsdirektoratet |
| Forvaltningsansvar | Novari IKS, som drifter og publiserer kodeverksbasen |
| Endringsprosess | Endringer i det nasjonale laget følger læreplanarbeidet hos Utdanningsdirektoratet. Endringer i VIGO-påbygget behandles i faggruppen. Kildene beskriver ikke frekvens eller formell beslutningsordning nærmere |
| Publiserings- og beslutningsarena | Kodeverksbasen er åpent tilgjengelig for oppslag, og Novari publiserer tjenestebeskrivelsen på egne sider |

## Relasjon til andre ressurser
- **Grep (`UDIR-001`)**
  Kilden til de nasjonale fag- og læreplankodene. Den viktigste avhengigheten oppover.

- **Nasjonale registre for barnehage og grunnopplæring (`UDIR-002`)**
  Nasjonalt skoleregister i denne familien er kilden til skoleopplysningene i kodeverket.

- **VIGO (`NOVARI-004`)**
  Systemet som bruker kodeverket operativt i inntak og fagopplæring.

- **vigo.no (`NOVARI-009`)**
  Søkerflaten bygger på fag- og tilbudskodene fra kodeverket.

- **VIGO Sentralbase (`NOVARI-006`)**
  Datagrunnlaget for videregående opplæring, som bruker de samme kodene.

- **Nasjonal vitnemålsdatabase (`SIKT-004`)** og **Vitnemålsportalen (`SIKT-005`)**
  Dokumentasjon av videregående opplæring viser til de samme fag- og vitnemålskodene. Koblingen er deduksjon ut fra hva dokumentasjonen inneholder, ikke noe kildene beskriver eksplisitt.

- **Felles informasjonsmodeller (`DIGDIR-069`)**
  Prinsippet om å bygge på eksisterende begreper og definisjoner er nettopp det VIGO Kodeverk gjør i praksis, ved å hente fra Grep og skoleregisteret framfor å definere på nytt.

## Forretningsverdi og arkitekturverdi
Forretningsverdien er at fylkeskommunene slipper å bygge og vedlikeholde nitten parallelle kodeverk. Sammenstillingen mot Grep og skoleregisteret er gjort én gang, kvalitetssikret i fellesskap, og publisert åpent.

Arkitekturverdien ligger i lagdelingen. Kodeverket viser tydelig hva som er nasjonalt fastsatt og hva som er sektorpåbygg, og det gjør det mulig å plassere et endringsbehov på riktig nivå framfor å løse alt lokalt. Den felles forvaltningen med Lånekassen, SSB og Utdanningsdirektoratet i samme faggruppe gir også kodeverket bredere legitimitet enn en rent fylkeskommunal løsning ville hatt.

## Konsekvens ved manglende bruk eller avvik
Uten et felles kodeverk ville hver fylkeskommune brukt egne koder for fag, tilbud og skoler. Konsekvensen ville vært at søknader, inntak og dokumentasjon ikke kunne behandles nasjonalt, at statistikk ikke kunne sammenstilles, og at en elev som flytter mellom fylker fikk opplæringen sin feiltolket.

Brukes kodeverket for sent i en systemanskaffelse, må kodene ettermonteres i en løsning som alt er bygget på lokale begreper. Det er varig oversettelsesarbeid framfor en engangskostnad.

Tolkes lagdelingen ulikt, oppstår den mest sannsynlige avviksformen: et behov løses som lokal VIGO-kode når det egentlig burde vært løftet til Grep nasjonalt. Da får sektoren et påbygg som vokser, og en nasjonal kilde som blir mindre dekkende enn den kunne vært.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Endringsstyring | Kodeverket avhenger av endringer i Grep og i skoleregisteret, som forvaltes andre steder | Endringer må følges opp i to eller tre ledd før de er operative | Tydelig ansvarsdeling og forutsigbar oppfølging i faggruppen |
| Semantisk kvalitet | VIGO-påbygget kan vokse med koder som egentlig burde vært nasjonale | Nasjonal kilde blir mindre dekkende, og påbygget mer komplekst | Vurdere for hvert nytt kodebehov om det hører nasjonalt |
| Forankring | Kodeverket er styrende i praksis, men uten regelverk eller kontrollordning | Uklart forpliktelsesnivå for nye aktører og leverandører | Beskrive kodeverket som forutsetning i arkitekturkrav og anskaffelser |
| Adopsjon | Verdien avhenger av at fagsystemene faktisk konsumerer kodeverksbasen | Lokale kodetabeller lever videre i eldre systemer | Stille krav om bruk av kodeverksbasen i anskaffelser |
| Sammenheng med gjenbrukbare løsninger | Kodeverket er tett bundet til VIGO-systemet, som Novari har varslet modernisering av | Endringer i systemlandskapet kan påvirke publiseringsform | Følge Novaris arbeid med nytt VIGO-system |

## Publiseringsform og tilgjengelighet
Kodeverksbasen er publisert som et åpent oppslagsverk, beskrevet som felles, oppdatert og kvalitetssikret og tilgjengelig for alle. Novari publiserer tjenestebeskrivelsen på egne tjenestesider. Kildene beskriver ikke om basen også tilbys som API med versjonerte endepunkter, og det bør kontrolleres ved integrasjonsarbeid.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Kodeverksbasen er åpen for alle, og kodene gjenbrukes av fylkeskommuner, nasjonale myndigheter og leverandører.

- **P6: Lag digitale løsninger som støtter samhandling**
  Felles koder er forutsetningen for at søknad, inntak, dokumentasjon og statistikk henger sammen på tvers av forvaltningsnivå.

- **P2: Ta arkitekturbeslutninger på rett nivå**
  Lagdelingen mellom nasjonale koder, skoleregister og VIGO-påbygg gjør det mulig å plassere endringer der de hører.

- **P5: Del og gjenbruk løsninger**
  Støttes indirekte. Det som gjenbrukes er kodeverket og sammenstillingen, ikke løsningskomponenter.

Begrensninger og spenninger: ressursen er et påbygg på nasjonale kilder, og verdien avhenger av at både Grep og skoleregisteret holdes oppdatert. Det gir en avhengighetskjede i tre ledd som er sårbar for treghet. Forpliktelsesnivået er styrende i praksis men uten hjemmel, og det er uklart for nye aktører. Og fordi påbygget forvaltes i sektoren selv, finnes det en innebygd risiko for at kodebehov løses lokalt framfor å løftes nasjonalt — noe som svekker P2 over tid selv om strukturen i utgangspunktet støtter prinsippet.

## Lenke til dokumentasjon
- https://novari.no/tjenester/vigo-kodeverk-og-kodeverkbase/
- https://novari.no/tjenester/vigosystemet
- https://www.udir.no/om-udir/data/kl06-grep/
- https://www.udir.no/om-udir/data/nxr/

## Kildegrunnlag brukt i utfyllingen
- https://novari.no/tjenester/vigo-kodeverk-og-kodeverkbase/, kontrollert 2026-09-07
- https://novari.no/tjenester/vigosystemet, kontrollert 2026-09-07
- https://www.udir.no/om-udir/data/kl06-grep/, kontrollert 2026-09-07
- https://www.udir.no/om-udir/data/nxr/, kontrollert 2026-09-07
- `arkitektur/kapabiliteter/capabilities.yaml`, kontrollert 2026-09-07
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-09-07
- `arkitektur/ressurser/styringsregler.md`, kontrollert 2026-09-07
