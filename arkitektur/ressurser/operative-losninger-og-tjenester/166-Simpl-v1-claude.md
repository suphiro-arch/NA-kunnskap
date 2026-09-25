# Simpl

## Navn
Simpl

## Ressurs ID
EU-012

## Status/Livsfase
**Under utvikling** - kildekoden er publisert og flere dataområder tar plattformen i bruk, men den er fortsatt i oppbygging.

**Fakta:** Europakommisjonen tildelte en kontrakt på 41 millioner euro til et konsortium ledet av Eviden Belgium, med Aruba, Capgemini Nederland, Engineering International Belgium, IONOS og COSMOTE Global Solutions som partnere. Programmet er omtalt med en samlet ramme på 150 millioner euro over en treårig gjennomføringsperiode, finansiert gjennom DIGITAL Europe-programmet, arbeidsprogrammets tema 2.1.1.

**Fakta:** En proof-of-concept ble publisert i juni 2024, repositoriet for Simpl-Open ble åpnet i slutten av juni 2024, og en minimum levedyktig plattform var planlagt til utgangen av 2024. Kommisjonens policyside er sist oppdatert 22. juni 2026.

**Deduksjon:** Plattformen er forbi utprøvingsstadiet og inne i utrulling mot konkrete dataområder, men er ikke en ferdig og stabil komponent en norsk virksomhet kan bygge på uten videre. Kildene i denne arbeidsøkten oppgir ikke et gjeldende versjonsnummer.

## Modenhet
**Politisk og finansielt godt forankret, teknisk under oppbygging.**

- Finansielt: 150 millioner euro over tre år gjennom DIGITAL Europe-programmet er en betydelig og forutsigbar ramme, ikke et forprosjekt.
- Teknisk: kildekoden er publisert åpent på `code.europa.eu` under European Union Public Licence 1.2, med installasjonsveiledning og bidragsretningslinjer.
- Funksjonelt: plattformen er modulær og bygget for å integrere eksisterende løsninger framfor å erstatte dem, noe som senker terskelen for å ta den i bruk gradvis.
- Organisatorisk: leveransen skjer gjennom et leverandørkonsortium på kontrakt, ikke gjennom et etablert forvaltningsmiljø med langsiktig driftsansvar.
- Bruksmessig: Simpl-Live er satt opp for utvalgte europeiske dataområder, men kildene i denne arbeidsøkten navngir ikke hvilke på en måte som kan kontrolleres.

**Deduksjon:** Det svakeste leddet er forvaltningsmodellen etter kontraktsperioden. En plattform som skal bære felles europeiske dataområder, trenger en langsiktig eier, og kildene i denne arbeidsøkten sier ikke hvem det blir når den treårige gjennomføringen er over. For norske virksomheter er dette den vesentligste usikkerheten, viktigere enn teknisk modenhet.

## Kort beskrivelse
Simpl er Europakommisjonens åpne mellomvareplattform for felles europeiske dataområder og for føderasjoner fra sky til kant. Plattformen skal gjøre det mulig å dele data på tvers av datainfrastrukturer og tjenester uten at dataeieren gir fra seg kontrollen over hvem som får tilgang til hva.

Simpl er modulær og bygget for å integrere eksisterende løsninger framfor å erstatte dem. Komponentene følger EU-standarder for datakvalitet og datadeling, og plattformen er tenkt som et gjenbrukbart fundament som det enkelte dataområdet bygger videre på.

Plattformen leveres i tre former. **Simpl-Open** er selve programvarestakken, publisert som åpen kildekode. **Simpl-Labs** er et testmiljø der et dataområde kan prøve ut komponentene og vurdere hvor godt de passer mot en eksisterende løsning før den tas i bruk. **Simpl-Live** er konkrete instanser av Simpl-Open satt i drift for utvalgte dataområder, der Kommisjonen selv deltar i forvaltningen.

## Kapabiliteter
- **Datautveksling og integrasjon: Dele data med andre**
  Simpl gir mekanismen for å gjøre data tilgjengelige for andre deltakere i et dataområde, med tilgangsstyring som blir hos den som eier dataene. Uten plattformen måtte hvert dataområde bygge sin egen delingsmekanisme.

- **Tjenesteutvikling: Gjenbrukbare tjenester**
  Plattformen er modulær og publisert som åpen kildekode under European Union Public Licence 1.2, slik at komponentene kan brukes i nye sammenhenger på tvers av sektorer og land framfor å utvikles på nytt per dataområde.

- **Standardisering: EU standarder**
  Komponentene er bygget for å følge EU-standarder for datakvalitet og datadeling, og gjør dem dermed praktisk anvendelige i konkrete løsninger framfor bare dokumenterte.

Koblingene er satt fordi plattformen selv leverer delingsmekanismen, komponentene og standardetterlevelsen. De enkelte dataområdene som bygger på Simpl, leverer sine egne evner innenfor sine fagområder, og de hører ikke her.

## Produktmål
**Dokumenterte mål**, slik Kommisjonen beskriver programmet:
- Anskaffe en storskala, modulær og interoperabel åpen europeisk mellomvareplattform fra sky til kant.
- Gjøre det mulig å integrere datainfrastrukturer og tjenester som dekker behovene i de ulike dataområdene.
- Realisere den europeiske skyføderasjonen.
- Gi samfunnet mellomvare for å bygge dataøkosystemer og skytjenester som støtter europeiske verdier om datasuverenitet, personvern og rettferdige markeder.

**Utledede operative mål:**
- Gjøre det mulig for et nytt dataområde å komme i gang uten å definere egen tillits- og delingsmodell.
- Redusere risikoen for at hvert sektorielle dataområde utvikler uforenlige løsninger.

## Brukerbehov
- Dataområder trenger en felles mekanisme for deling, slik at deltakerne ikke må avtale teknisk oppsett bilateralt.
- Dataeiere trenger å dele data uten å gi fra seg kontrollen over hvem som får tilgang og til hva.
- Virksomheter som vurderer å delta i et europeisk dataområde, trenger å prøve ut kompatibiliteten med egen løsning før de forplikter seg.
- Europeiske forvaltninger trenger infrastruktur som ikke låser dem til én skyleverandør.
- Utviklingsmiljøer trenger komponenter med kjent lisens som kan bygges videre på.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Sektorielle dataområder | Felles mellomvare framfor egen utvikling | Oppbygging av dataområde | Den primære målgruppen |
| Dataeiere og datatilbydere | Dele data med bevart kontroll over tilgang | Tilgjengeliggjøring av datasett | Kontrollen blir hos eieren |
| Virksomheter som vurderer deltakelse | Teste kompatibilitet før forpliktelse | Simpl-Labs | Testmiljøet finnes nettopp for dette |
| Utviklings- og integrasjonsmiljøer | Komponenter med kjent lisens å bygge på | Simpl-Open | EUPL-1.2 gir forutsigbare vilkår |
| Europakommisjonen | Realisere felles europeiske dataområder og skyføderasjon | Program- og forvaltningsansvar | Deltar selv i forvaltningen av Simpl-Live |
| Leverandørkonsortiet | Utvikle og levere plattformen | Kontraktsleveranse | Ledet av Eviden Belgium |

## Hovedfunksjoner
Den første hovedfunksjonen er **mellomvare for datadeling i et dataområde**. Simpl håndterer koblingen mellom deltakere som ikke har et forhold til hverandre fra før: hvordan de finner hverandre, hvordan tilgang avtales, og hvordan data faktisk utveksles. Det avgjørende trekket er at tilgangsstyringen blir hos dataeieren, slik at deling ikke forutsetter at dataene flyttes ut av eierens kontroll.

Den andre er **modulær integrasjon av eksisterende løsninger**. Plattformen er utformet for å integrere det som allerede finnes, ikke for å erstatte det. For en virksomhet som allerede har en datadelingsløsning, betyr det at Simpl kan tas i bruk gradvis, og det er sannsynligvis den viktigste egenskapen for praktisk innføring.

Den tredje er **testmiljøet Simpl-Labs**. Et dataområde kan prøve ut komponentene og vurdere interoperabiliteten mot sin egen løsning før den tas i bruk. Dette er en eksplisitt del av leveransen, ikke en tilleggstjeneste, og senker terskelen for å vurdere plattformen.

Den fjerde er **driftssatte instanser gjennom Simpl-Live**. For utvalgte dataområder settes Simpl-Open opp som en dedikert instans der Kommisjonen deltar i forvaltningen. Skillet mot Simpl-Open er praktisk viktig: en virksomhet kan enten laste ned koden og drifte selv, eller koble seg til et dataområde som allerede har en Simpl-Live-instans.

### Typiske brukssituasjoner (generisk)
- Et nytt sektorielt dataområde skal etableres, og delingsmekanismen må velges.
- En norsk virksomhet vurderer å delta i et europeisk dataområde og må avklare hva det krever teknisk.
- En eksisterende datadelingsløsning skal vurderes for interoperabilitet mot europeiske dataområder.
- Et miljø leter etter åpne komponenter for datadeling med kjent lisens.

### Når Simpl normalt ikke er førstevalg
- Når behovet er datadeling innenfor Norge. Da er `Felles datakatalog`, `Maskinporten` og de nasjonale delingsmekanismene etablert og modne, og Simpl gir ingen tilleggsverdi.
- Når løsningen skal settes i drift nå og kreve stabilitet. Plattformen er under oppbygging, og forvaltningsmodellen etter kontraktsperioden er ikke avklart.
- Når behovet er dokumentutveksling mellom kjente parter. Da er `eDelivery Building Block` og `Peppol eDelivery` riktig mønster.
- Når behovet er å hente dokumentasjon fra myndigheter i andre land i en definert prosedyre. Da er `Once-Only Technical System` riktig.
- Når virksomheten ikke deltar i, eller planlegger å delta i, et europeisk dataområde. Simpl gir da en infrastruktur uten motparter.

### Scope og avgrensning
Inngår: mellomvarekomponentene i Simpl-Open, testmiljøet Simpl-Labs, driftssatte instanser gjennom Simpl-Live, og den åpne kildekoden med tilhørende installasjonsveiledning og bidragsretningslinjer.

Inngår ikke: de sektorielle dataområdene selv, som er egne initiativer med egne styringsmodeller; innholdet i dataene; skyinfrastrukturen plattformen kjører på; og det regelverket som regulerer datadelingen i det enkelte dataområdet.

Simpl-Open, Simpl-Labs og Simpl-Live er behandlet som tre leveranseformer av samme ressurs, ikke som tre ressurser. Begrunnelsen er logget i `briefs/decisions.md`.

## Veikart over kommende funksjonalitet
**Fakta:** Proof-of-concept ble publisert i juni 2024, og en minimum levedyktig plattform var planlagt til utgangen av 2024. Gjennomføringsperioden er treårig.

**Fakta:** Kommisjonen vedtok i juni 2026 et forslag til Cloud and AI Development Act, med mål om minst å tredoble EUs datasenterkapasitet i løpet av fem til sju år. Simpl er omtalt som infrastruktur som understøtter dette bredere sky- og dataområdearbeidet.

**Ikke offentlig dokumentert i denne arbeidsøkten:** gjeldende versjonsnummer, en datofestet utgivelsesplan, og hvem som overtar forvaltningen når kontraktsperioden er over.

## Forretningsverdi/Verdiforslag
**For dataområder:** et ferdig, finansiert fundament for deling, i stedet for å utvikle egen tillits- og delingsmodell. Det er den mest konkrete gevinsten, og den er størst for dataområder som ennå ikke har valgt løsning.

**For dataeiere:** mulighet til å dele data uten å gi fra seg kontrollen over tilgangen, som er forutsetningen for at mange offentlige datasett i det hele tatt kan deles.

**For samfunnet:** europeisk datasuverenitet og redusert avhengighet av enkeltleverandører i skymarkedet, som er det uttalte politiske formålet.

**For norske virksomheter:** en kjent inngang til europeiske dataområder, og åpne komponenter under EUPL-1.2 som kan vurderes for gjenbruk uavhengig av om Norge deltar i et gitt dataområde.

## Utfordringer og risiko
| Område | Risiko | Håndtering eller observasjon |
|---|---|---|
| Forvaltning | Leveransen skjer på kontrakt, og langsiktig eierskap etter treårsperioden er ikke avklart | Ikke offentlig dokumentert i denne arbeidsøkten. Den vesentligste usikkerheten for den som vurderer å bygge på plattformen |
| Modenhet | Plattformen er under oppbygging, uten oppgitt gjeldende versjon | Bruk Simpl-Labs til å vurdere modenhet mot eget behov framfor å planlegge mot en dato |
| Adopsjon | Verdien avhenger av at dataområdene faktisk tar plattformen i bruk | Simpl-Live er satt opp for utvalgte dataområder, men kildene i denne arbeidsøkten navngir dem ikke kontrollerbart |
| Norsk tilknytning | Kildene sier ikke om eller hvordan norske aktører deltar | Bør avklares med Digdir før plattformen legges til grunn i norske planer |
| Leverandør | Utviklingen ligger hos ett konsortium | Åpen kildekode under EUPL-1.2 demper innelåsingen, men kompetansen sitter hos konsortiet |
| Kompleksitet | Mellomvare for føderert datadeling er krevende å drifte | Simpl-Live er alternativet for dem som ikke vil drifte selv |

## Kanaler
Simpl har tre flater. Kildekoden hentes fra `code.europa.eu`, med installasjonsveiledning og bidragsretningslinjer. Simpl-Labs brukes som testmiljø for å prøve ut komponentene. Simpl-Live er driftssatte instanser knyttet til et konkret dataområde, som en deltaker kobler seg til framfor å drifte selv.

Det finnes ingen sluttbrukerflate. Simpl er infrastruktur, og brukeren møter den gjennom tjenestene i det aktuelle dataområdet.

Kommisjonens programside fungerer som informasjons- og deltakelseskanal, med egen veiledning for hvordan aktører kan delta.

## Plattform
**Ikke offentlig dokumentert i denne arbeidsøkten:** driftsmodell og lokasjon for Simpl-Live-instansene. Det som er kjent, er at Simpl er utformet som mellomvare for føderasjoner fra sky til kant, at den er ment å være leverandørnøytral, og at Simpl-Open kan installeres og driftes av den enkelte aktøren selv.

## Gjenbruk
Gjenbruk er hele poenget med ressursen. Simpl-Open er publisert som åpen kildekode under European Union Public Licence 1.2, med installasjonsveiledning og bidragsretningslinjer, slik at komponentene kan brukes, endres og videreutvikles av andre. Modulariteten gjør at et miljø kan ta i bruk deler av plattformen uten å bytte ut det som allerede virker.

Avhengigheter som ikke er kapabiliteter her: plattformen bygger på skyinfrastruktur levert av andre, og på de standardene for datakvalitet og datadeling som forvaltes i EU-regi.

**Vanlige kombinasjoner med andre produkter:**
- `Interoperable Europe Solutions` og `Core Vocabularies` for de semantiske modellene data beskrives med.
- `eDelivery Building Block` for dokumentutveksling, som dekker et annet og mer avgrenset behov.
- `Once-Only Technical System` for bevisutveksling mellom myndigheter i definerte prosedyrer.
- `Kunnskapsgrunnlag dataspaces` som det norske analysegrunnlaget for dataområder.
- `Interoperable Europe Act`, som gir vurderingsplikten når norske krav berører grensekryssende interoperabilitet.

**Kildekode:** Åpen kildekode. Simpl-Open er publisert på `code.europa.eu`, og repositoriet ble åpnet i slutten av juni 2024.

**Lisens:** `EUPL-1.2`. European Union Public Licence versjon 1.2 er oppgitt som lisens for Simpl-Open. Lisensen er ikke kontrollert mot lisensfila i repositoriet i denne arbeidsøkten, og bør bekreftes der før koden gjenbrukes.

**Repositorium:** https://code.europa.eu/simpl/simpl-open

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data**
  Plattformen er bygget nettopp for å gjøre datadeling mulig på tvers av virksomheter, sektorer og land, med kontroll hos dataeieren.
- **P5: Del og gjenbruk løsninger**
  Åpen kildekode under EUPL-1.2, modulær oppbygging og et eget testmiljø gjør plattformen gjenbrukbar i praksis, ikke bare i prinsippet.
- **P6: Lag digitale løsninger som støtter samhandling**
  Formålet er å gjøre uavhengige datainfrastrukturer interoperable innenfor felles dataområder.
- **P7: Sørg for tillit til oppgaveløsningen**
  Datasuverenitet og bevart tilgangskontroll hos dataeieren er utformet som grunnleggende egenskaper, ikke som tillegg.

**Spenning og begrensning:** Simpl støtter **P1: Ta utgangspunkt i brukernes behov** bare indirekte. Den er infrastruktur, og verdien for en sluttbruker oppstår først i tjenestene som bygger på den. Den står også i spenning mot **P2: Ta arkitekturbeslutninger på rett nivå**: plattformen er valgt og finansiert på europeisk nivå, mens et norsk miljø som velger å bygge på den, tar på seg en avhengighet til en forvaltningsmodell som ennå ikke er avklart. Den mest konkrete begrensningen i dag er derfor tidsmessig, ikke arkitektonisk: plattformen er verdt å følge og teste, men ikke å låse en norsk leveranse til før eierskapet etter kontraktsperioden er kjent.

## Finansiering
**Fakta:** Simpl finansieres gjennom DIGITAL Europe-programmet, arbeidsprogrammets tema 2.1.1. Programmet er omtalt med en samlet ramme på 150 millioner euro over tre år, og den første spesifikke kontrakten på 41 millioner euro ble tildelt konsortiet ledet av Eviden Belgium.

**Deduksjon:** Finansieringen dekker utvikling og oppbygging. Kildene i denne arbeidsøkten sier ikke hvordan drift og forvaltning finansieres etter gjennomføringsperioden, og det er den samme usikkerheten som gjelder eierskapet.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Programansvar | Europakommisjonen | Kommisjonens policyside for Simpl |
| Utvikling | Konsortium ledet av Eviden Belgium, med Aruba, Capgemini Nederland, Engineering International Belgium, IONOS og COSMOTE Global Solutions | Kommisjonens omtale av kontraktstildelingen |
| Forvaltning av Simpl-Live-instanser | Europakommisjonen deltar aktivt i forvaltningen | Kommisjonens beskrivelse av Simpl-Live |
| Drift av egen installasjon | Den aktøren som installerer Simpl-Open | Følger av at koden er publisert med installasjonsveiledning |
| Budsjettansvar | Europakommisjonen, gjennom DIGITAL Europe-programmet | Kommisjonens omtale av finansiering |
| Langsiktig forvaltningsmodell | Ikke offentlig dokumentert i denne arbeidsøkten | - |

## Lenke til dokumentasjon
- Kommisjonens policyside for Simpl: https://digital-strategy.ec.europa.eu/en/policies/simpl
- Simpl-programmets egen side: https://simpl-programme.ec.europa.eu/
- Simpl-Open i EUs kodeplattform: https://code.europa.eu/simpl/simpl-open
- Kommisjonens omtale av kontraktstildelingen: https://digital-strategy.ec.europa.eu/en/news/commission-awards-eu41-million-contract-develop-infrastructure-common-european-data-spaces-0

## Kildegrunnlag brukt i utfyllingen
- Europakommisjonen, Simpl: Cloud-to-edge federations empowering EU data spaces, hentet 25. september 2026.
- Simpl-programmets egen nettside, hentet 25. september 2026.
- Europakommisjonen, nyhetssak om kontrakt på 41 millioner euro, hentet 25. september 2026.
- Simpl-Open på `code.europa.eu`, hentet 25. september 2026. Lisensen `EUPL-1.2` er oppgitt i omtale av repositoriet, ikke lest ut av lisensfila i denne arbeidsøkten.
- Lokale kilder: `arkitektur/ressurser/produktnummerering.md`, `arkitektur/ressurser/normerende-ressurser/108-Kunnskapsgrunnlag-dataspaces-v1-codex.md`, `arkitektur/kapabiliteter/capabilities.yaml`, `arkitektur/prinsipper/principles.md`, `sources/links.md`.
