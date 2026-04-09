---
date: 2026-03-16
author: codex
status: draft
topic: dokumentasjonsassistent-neste-steg
sources:
  - briefs/arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md
---

# Neste steg

## Hvordan lese denne fila

**Prioritet nå (uker 1-6):** Les "Hva gjenstår", "Strategiske forbedringer", "Konkrete neste oppgaver" og "Bekjente blokkere".

**Strukturelle forbedringer du kan gjøre parallelt:** Les "Strukturelle forbedringer –" Dagens repo".

**Framtidig videreutvikling (når det blir aktuelt):** Les hele "Assistenten på web –" Planlegging og MVP" på slutten.

---

## Hva er gjort
- Testet ny mal for arkitekturassistert analyse av utviklingsbehov på to separate case, splittet analysen i egne filer og oppdatert instruks med eksplisitt splittingsregel.
- Forbedret analysemalen med tidlig avklaring av ett/flere case, fast vurderingsrekkefølge for produktkategorier, gap-type per tiltak og seksjon for sammensatte løsningsmønstre.
- Oppdatert utvalgte produktbeskrivelser med generell beslutningsstøttefelt: typiske brukssituasjoner, når produktet normalt ikke er førstevalg og vanlige kombinasjoner med andre produkter.
- Definert målbildet for en åpen dokumentasjonsassistent på nettsiden.
- Avgrenset MVP til kun offentlig informasjon fra repoet.
- Beskrevet anbefalt arkitektur med Hugo-frontend, egen backend og OpenAI retrieval.
- Dokumentert lisens- og avtaleavklaringer som må på plass før bygging.
- Oppdatert produktbeskrivelsene for produkt `02-06` til nye `v3-codex`-versjoner med sterkere kildegrunnlag og strammere kapabilitetsvalg.
- Oppdatert prompt og mal for produkt-canvas slik at nye beskrivelser ikke skal starte med egen linje for målgruppe, og `Ressurs ID` ikke skal ha parentesforklaring.
- Strammet inn metodekravet for kapabiliteter: bare direkte og sterke koblinger til produktets egen funksjon skal tas med.
- Regenerert produktover­sikten i Hugo-prototypen slik at siste versjon for produkt `02-06` nå vises på nettsiden.
- Lagt om publiseringsmodellen for Hugo-prototypen til GitHub Pages artifact-deploy direkte fra `web/hugo-prototype/`.
- Standardisert repoet med `.editorconfig` og `.gitattributes` for å redusere risikoen for nye tegnkodings- og linjesluttfeil i tekstfiler.
- Utvidet encoding-validatoren slik at den også fanger typiske `?`-skader inne i norske ord, ikke bare klassisk mojibake.

- Kvalitetssjekket masterfila for produkt-kapabilitet-koblinger og strammet inn koblingene til et første manuelt arbeidsutkast basert på direkte og sterke koblinger.
- Lagt om produktregisteret til eierbasert `Ressurs ID`, med ekstra kolonner for ressurstype, kapabilitetstreff og lenke til siste dokumentversjon.
- Oppdatert siste versjon av produkt `01-24` slik at feltet `Ressurs ID` nå bruker eierbasert identifikator.
- Lagt inn første arbeidsutkast for ressurser fra `KS`, `HDIR`, `NAV` og `SKATT` i produktregisteret, basert på `sources/links.md`.
- Utvidet produktregisteret med kolonnen `Ressurskategori` og lagt inn flere verifiserte kandidater fra `KS`, `NHN`, `NAV`, `Skatteetaten`, `Kartverket` og relevante EU-byggesteiner.
- Utvidet produktregisteret videre med `SIKT` som egen eiergruppe og første arbeidsutkast for Feide, FS, opptaksløsninger, Nasjonal vitnemålsdatabase og Vitnemålsportalen som kandidater for tverrsektoriell samhandling.
- Kvalitetssikret første arbeidsutkast for `SIKT`-ressursene og utvidet registeret med `Nasjonalt utdanningsregister` som egen kandidat for tverrsektoriell samhandling i utdanningssektoren.
- Kvalitetssikret `BRREG` og `KS` i produktregisteret med strammere kapabilitetstreff og tydeligere skille mellom register, plattform og tilgangstjeneste.
- Kvalitetssikret `HDIR`, `NHN` og `NAV` i produktregisteret med tydeligere skille mellom portal, tillitstjeneste, delingsløsning og register.
- Kvalitetssikret `SKATT`, `KART` og `DIGDIR` i produktregisteret med mer direkte kapabilitetstreff, særlig for `eFormidling`, `Norge.no`, `Skatteetatens delingstjenester` og `Geonorge`.
- Opprettet første produktbeskrivelser for KS-ressursene `KS-001` til `KS-006` og synkronisert produktregister, masterfil for produkt-kapabilitet-koblinger og webgrunnlag mot de nye filene.
- Oppdatert lenkedokumentet med egne lenker for ELMA, OpenPeppol og EHF-/Peppol-veiledning, og opprettet nye `v3-codex`-beskrivelser for `ELMA` og `Peppol eDelivery`.
- Avklart at `EU-003 eDelivery Building Block` beholdes i registeret som egen EU-ressurs, men som referanseramme og byggestein rundt samme problemområde som `Peppol eDelivery`.
- Utvidet EU-delen med `EU Open Source Solutions Catalogue`, `Interoperable Europe Solutions` og `Core Vocabularies` som referanseressurser, og oppdatert lenkedokumentet med flere offisielle interoperabilitetskilder fra Interoperable Europe.
- Sammenlignet ny XML-kilde for nasjonal arkitektur med `capabilities.yaml`, laget avviksrapport i `sources/` og rettet manglende `P6`-kobling for `Datautveksling og integrasjon`.
- Fylte ut `arkitektur/prinsipper/principles.md` med operative prinsipper og synket prinsippkoblingene mot webversjonen.
- Knyttet `arkitektur/prinsipper/principles.md` direkte inn i videre bruk: som kilde for prinsipper i produktanalyser, som synkgrunnlag for webens prinsippside og som del av repoets dokumenterte arbeidsflyt.
- Dokumentert råkilder, kuraterte arbeidsfiler og videre prosessering i [struktur-og-bearbeiding.md](c:/Users/HILROS/NA-kunnskap/arkitektur/struktur-og-bearbeiding.md).
- Kartlagt mål- og ressursrelasjoner i XML-kilden, dokumentert at ressursrelasjonene ikke er på samme nivå som repoets produktmaster, og opprettet [maal.md](c:/Users/HILROS/NA-kunnskap/arkitektur/maal/maal.md) som første kuraterte måloversikt.
- Ryddet `capabilities.yaml` slik at den nå bare inneholder kapabilitetsstrukturen, mens prinsipptekst og målspor ligger i egne kuraterte filer.
- Utvidet `maal.md` med de få eksplisitte kapabilitet-til-mål-koblingene som faktisk finnes i XML-kilden, og markerte hvilke som er operative versus generiske.
- Kjørt avviksjekk mellom siste produktbeskrivelser og gjeldende produkt-kapabilitetsmaster, og dokumentert funnene i en egen rapport i `sources/`.
- Synket alle siste produktbeskrivelser mot gjeldende produkt-kapabilitetsmaster og oppdatert avviksrapporten slik at den nå viser `0` avvik.
- Opprettet første `SIKT`-produktbeskrivelser for `Feide` og `Vitnemålsportalen`, og synket produktregister, koblingsfil og genererte weboversikter mot de nye filene.
- Opprettet nye KS-produktbeskrivelser for `SvarInn` og `FIKS Folkeregister`, og synket produktregister, koblingsfil, lenkedokument og genererte weboversikter mot de nye filene.
- Opprettet nye KS-produktbeskrivelser for `Fiks skatte- og inntektsopplysninger` og `Fiks kjøretøyregister`, og fullført første gjennomgang av de registrerte KS-/KS Digital-produktene i produktregisteret.
- Opprettet `Fiks register v2` med oppdatert KS-kildegrunnlag og tydeligere avgrensning mellom den overordnede registerfamilien og undertjenestene under samme produktområde.
- Opprettet `Fiks melding v2` med oppdatert KS-kildegrunnlag og tydeligere beskrivelse av produktet som kanalplattform med flere undertjenester og bruksmåter.
- Opprettet ny versjon `v2-copilot` for `SvarUt` med oppdatert kildegrunnlag fra `sources/links.md` og ny verifisering av produktside, utviklerdokumentasjon, prisoversikt og driftsstatus.
- Justert språkføring i `SvarUt v2` tettere mot etablert tone i forrige versjon, og oppdatert instruksgrunnlaget slik at fremtidige revisjoner skal bevare velfungerende tone og unngå unødvendig full omskriving.
- Gjennomført ny sammenligning av `SvarUt v1` og `v2`, og harmonisert flere nøkkelseksjoner i `v2` til v1-tonen der innholdet fortsatt er korrekt.
- Oppdatert styringsprompten for produkt-canvas med tydelig krav om språk for både forretning og arkitektur: lett å forstå uten systemforståelse, men med nok funksjonsdetaljer for gjenbruksvurdering.
- Flyttet produktbeskrivelsene til `arkitektur/ressurser/operative-losninger-og-tjenester/` og avviklet duplikatoversiktene i `results/Produktregister/`, slik at `arkitektur/ressurser/produktnummerering.md` nå er eneste operative master for produktregisteret.
- Ryddet KS-delen i produktregisteret etter KS Digitals nåværende navngivning, fjernet `Felles tjenesteplattform` fra operativ ressursliste og la inn `Fiks skatte- og inntektsopplysninger` og `Fiks kjøretøyregister` som egne kandidater under samme logikk som `Fiks folkeregister`.
- Harmoniserte KS-produktnavn i berørte produktbeskrivelser og koblingsgrunnlag, og synket weboversiktene slik at `Fiks SvarUt` nå peker til siste versjon `v2 (copilot)`.
- Opprettet `SvarUt v3 (codex)` med oppdatert KS-kildegrunnlag, tydeligere API- og versjonsbilde, strammere scope og mer presis navnebruk før ekstern kvalitetssjekk hos KS.
- Standardiserte filnavn for FIKS-relaterte KS-beskrivelser slik at `FIKS` brukes konsekvent med store bokstaver i filnavn, blant annet for `FIKS SvarUt` og `FIKS Digiorden`.
- Oppdatert styringsprompten for produkt-canvas med eksplisitt kontroll av løsningsbredde, slik at nye beskrivelser må sjekke hele produktets operative rolle og ikke bare beskrive ett grensesnitt som API eller portal.
- Skjerpet prompten videre slik at `Hovedfunksjoner` normalt skal skrives som minst 3-4 forklarende avsnitt når kildene gir grunnlag for det, og oppdatert `FIKS SvarUt v3` i tråd med dette.
- Revidert Altinn-produktene `Altinn Autorisasjon`, `Altinn Formidling`, `Altinn Events`, `data.altinn.no`, `Altinn 3 plattform` og `Altinn Studio` til nye codex-versjoner med oppdatert kildegrunnlag, tydeligere løsningsbredde og strammere produktavgrensning.
- Revidert også `Dialogporten`, `Altinn Melding` og `Altinn Varsling` til nye codex-versjoner, slik at hele den operative Altinn-listen nå følger nyere instruks og oppdatert kildekontroll.
- Opprettet `Digital postkasse v3` med oppdatert Digdir-kildegrunnlag, tydeligere beskrivelse av hele leveranseløpet og strammere avgrensning mot kontaktregister, avsendersystem og generell meldingsutveksling.
- Oppdatert `sources/links.md` med flere konkrete Digdir-kilder for Digital postkasse, inkludert oversikt, ta i bruk, kostnadsmodell, statistikk og teknisk dokumentasjon.
- Opprettet `Felles datakatalog v3` med oppdatert Digdir-kildegrunnlag og tydeligere skille mellom den overordnede metadata- og publiseringsløsningen, `data.norge.no` som portal og delkatalogene under samme produktområde.
- Oppdatert `sources/links.md` med nyere og mer presise kilder for Felles datakatalog, inkludert ny Digdir-side, ta-i-bruk-løp og kravside for registrering av datasett.
- Opprettet `Begrepskatalog v3` med oppdatert Digdir-kildegrunnlag og tydeligere avgrensning som semantisk delkatalog under Felles datakatalog, ikke som egen generell ontologi- eller datakatalogplattform.
- Oppdatert `sources/links.md` med konkrete kilder for Begrepskatalogen, inkludert katalogflaten og teknisk dokumentasjon på data.norge.no.
- Opprettet `API-katalog v3` med oppdatert Digdir-kildegrunnlag og tydeligere avgrensning som delkatalog for API-beskrivelser, ikke som gateway, runtime-plattform eller generell utviklerportal.
- Oppdatert `sources/links.md` med konkrete kilder for API-katalogen, inkludert katalogflaten og teknisk API-dokumentasjon på data.norge.no.
- Opprettet første produktbeskrivelse for `HelseID` med oppdatert NHN-kildegrunnlag og tydelig beskrivelse av produktet som felles tillits- og autentiseringskomponent for helse- og omsorgssektoren.
- Oppdatert `sources/links.md` med flere konkrete NHN-kilder for HelseID, inkludert hvorfor bruke-løp, spørsmål og svar, personvern, utbredelse og utviklerportal.
- Opprettet første produktbeskrivelse for `Matrikkelen` med oppdatert Kartverket-kildegrunnlag og tydelig beskrivelse av produktet som nasjonalt grunndataregister og statlig felleskomponent.
- Oppdatert `sources/links.md` med flere konkrete Kartverket-kilder for Matrikkelen, inkludert om-side, tilgangsløp, føringsområder og faggruppe.
- Opprettet første produktbeskrivelse for `Folkeregisteret` med oppdatert Skatteetaten-kildegrunnlag og tydelig beskrivelse av produktet som nasjonalt personregister og statlig felleskomponent for persondata.
- Oppdatert `sources/links.md` med flere konkrete Skatteetaten-kilder for Folkeregisteret, inkludert om-side, tilgangsløp og håndbokssider for delingstjenester.
- Opprettet første produktbeskrivelse for `Enhetsregisteret` med oppdatert Brønnøysundregistrene-kildegrunnlag og tydelig beskrivelse av produktet som nasjonalt virksomhetsregister og felleskomponent for virksomhetsdata.
- Oppdatert `sources/links.md` med flere konkrete BRREG-kilder for Enhetsregisteret, inkludert organisasjonsnummer, full maskinell tilgang og åpne data-varsler.
- Opprettet første produktbeskrivelse for `Skatteetatens delingstjenester` med oppdatert Skatteetaten-kildegrunnlag og tydelig beskrivelse av produktet som samlet delingsflate for API-basert datadeling.
- Oppdatert `sources/links.md` med flere konkrete Skatteetaten-kilder for delingstjenestene, inkludert hvorfor-siden, kontaktløp og bruksvilkår.
- Opprettet første produktbeskrivelse for `A-ordningen` med oppdatert kildegrunnlag fra Skatteetaten og a-ordningen.no, og tydelig beskrivelse av produktet som samforvaltet rapporterings- og delingsordning.
- Oppdatert `sources/links.md` med flere konkrete kilder for A-ordningen, inkludert om-side, kontaktflate og informasjonsmøte 12. mars 2026.
- Opprettet første produktbeskrivelse for `Felles studentsystem (FS)` med oppdatert Sikt-kildegrunnlag og tydelig beskrivelse av produktet som nasjonal studieadministrativ plattform med databaser, brukerflater og integrasjoner.
- Oppdatert `sources/links.md` med flere konkrete Sikt-kilder for FS, inkludert `fs.sikt.no`, FS-API og API-katalogen for studieadministrasjon.
- Opprettet første produktbeskrivelse for `Nasjonal vitnemålsdatabase (NVB)` med oppdatert Sikt-kildegrunnlag og tydelig beskrivelse av produktet som nasjonal database- og delingstjeneste for elektroniske vitnemål.
- Oppdatert `sources/links.md` med flere konkrete Sikt-kilder for NVB, inkludert tjenestekatalog og moderniseringsretning mot bredere kompetanseregister.
- Opprettet første produktbeskrivelse for `Helsenorge` med oppdatert NHN-kildegrunnlag og tydelig beskrivelse av produktet som nasjonal innbyggerportal og sammenhengende tjenesteflate i helsesektoren.
- Vurdert `NVDB` opp mot `Geonorge` og valgt `Geonorge` som sterkere tverrsektoriell kandidat for denne runden.
- Opprettet første produktbeskrivelse for `Geonorge` med oppdatert Kartverket-/Geonorge-kildegrunnlag og tydelig beskrivelse av produktet som nasjonal metadata-, katalog- og delingsplattform for geodata.
- Oppdatert `sources/links.md` med flere konkrete kilder for Geonorge, inkludert om-side, API-er og distribusjonsmodell.
- Opprettet første produktbeskrivelse for `Helsedata.no` som nasjonal portal og tilgangsflate for helsedata.
- Opprettet første produktbeskrivelse for `HPR` som nasjonalt register over helsepersonell.
- Opprettet første produktbeskrivelse for `Kjernejournal` som nasjonal samhandlingsløsning for utvalgte helseopplysninger.
- Opprettet første produktbeskrivelse for `e-resept` som nasjonal løsning for elektronisk forskrivning og reseptformidling.
- Opprettet første produktbeskrivelse for `DSOP-tjenester` som samlet offentlig-privat delings- og samhandlingsflate.
- Opprettet første produktbeskrivelse for `Aa-registeret` som nasjonalt grunndataregister over arbeidsforhold.
- Opprettet første produktbeskrivelse for `NAIS` som åpent dokumentert plattformmodell og gjenbrukbart utviklings- og kjøremiljø, med tydeligere avgrensning enn klassiske nasjonale felleskomponenter.
- Opprettet første produktbeskrivelse for `Opptaksløsninger` som felles systemstøtte for samordnet opptak.
- Opprettet første produktbeskrivelse for `Nasjonalt utdanningsregister` som felles autoritativ kilde for utdanninger og læresteder.
- Opprettet første produktbeskrivelse for `KUHR` som sentralt register- og oppgjørssystem for helserefusjoner.
- Opprettet første produktbeskrivelse for `microdata.no` som nasjonal analyseplattform for kontrollert bruk av registerdata.
- Opprettet første produktbeskrivelse for `Motorvognregisteret` som nasjonal registerressurs for kjøretøyopplysninger.
- Kvalitetssikret den siste bolken med nye produktbeskrivelser og løftet særlig `HPR`, `e-resept`, `Opptaksløsninger` og `Nasjonalt utdanningsregister` til et mer forklarende nivå i tråd med gjeldende instruks.
- Oppdaget at filene for `KUHR`, `microdata.no` og `Motorvognregisteret` manglet i produktmappa selv om registeret pekte til dem, og opprettet dem på nytt med fullverdige beskrivelser.
- Presisert `NAIS` videre som en interessant og gjenbrukbar plattformmodell, men uten samme dokumenterte status som formell nasjonal fellesløsning eller klassisk felleskomponent.
- Etablert første styringsstruktur for et bredere ressursområde under `arkitektur/ressurser/`, med egen styringsfil for `operative løsninger og tjenester`, `normerende ressurser` og `samarbeidsfora`.
- Oppdatert `sources/links.md` med første Novari-kilder for `FINT Felleskomponent`, `FINT Arkiv`, `FINT Informasjonsmodell` og `VIGO`, og presisert at dagens `produkt-canvas` brukes direkte for operative ressurser men må avledes for normerende ressurser og samarbeidsfora.
- Opprettet første avledede mal for normerende ressurser i `config/templates/normerende-ressurs-template.md`, som grunnlag for blant annet `FINT Informasjonsmodell`.
- Opprettet første konkrete normerende ressursbeskrivelse for `FINT Informasjonsmodell` i `arkitektur/ressurser/normerende-ressurser/`, basert på Novari-kilder og ny avledet mal.
- Opprettet første operative ressursbeskrivelser for `FINT Felleskomponent` og `FINT Arkiv`, og ført `NOVARI`-ressursene inn i `arkitektur/ressurser/produktnummerering.md` slik at eksisterende nummerering og registerlogikk beholdes som én operativ master.
- Opprettet første operative ressursbeskrivelse for `VIGO` og laget en konkret migreringsplan for overgang fra dagens produktstruktur til bredere ressursstruktur i `briefs/arbeidsstyring-og-handover/2026-04-09-migreringsplan-ressursstruktur-v1.md`.
- Opprettet første operative ressursbeskrivelse for `VIGO` og oppdatert `NOVARI-004` i `produktnummerering.md` med kapabilitetstreff og dokumentlenke.

## Hva gjenstår –" Produktgrunnlag utvikling (neste 4-6 uker)

**Kjerneprioriteter –" disse skal gjøres først:**

- Fortsette revisjon av eldre produktbeskrivelser sektorvis etter samme metode som for KS- og Altinn-rundene.
- Vurdere om det fortsatt er behov for en ny harmoniseringsrunde på de nylig oppdaterte Digdir-katalogproduktene, eller om neste naturlige steg nå er å gå over til flere nye produkter i neste sektor.
- Ta stilling til om EU-kandidatene skal behandles som egne produktfiler eller fortsatt som referanseressurser, nå som den siste nasjonale restlista er fullført og kvalitetssikret.
- Følge opp kvaliteten i selve koblingene mellom produkter og kapabiliteter, særlig i eldre produktbeskrivelser der kapabilitetsseksjonen er svakere eller mindre presis.
- Ta inn de første ressursene fra KS, Helsedirektoratet, NAV og Skatteetaten i produktregisteret med samme ID-prinsipp.
- Kvalitetssikre de nye arbeidsutkastene for `KS`, `HDIR`, `NAV` og `SKATT`, særlig eierskap, ressurstype og kapabilitetstreff.
- Fortsette `SIKT`-sektoren med de neste ressursene etter `Feide` og `Vitnemålsportalen`, særlig `Felles studentsystem (FS)` og `Nasjonal vitnemålsdatabase`.
- Kjøre avviksjekk og synke produktbeskrivelsene kontinuerlig mot masterfila for produkt-kapabilitet-koblinger.

**Anbefalt liten oppfølgingsrunde før nye store bolker:**

- Ta en lett poleringsrunde på `DSOP-tjenester`, som fortsatt er kortere og mer komprimert enn de sterkere beskrivelsene i den siste nasjonale bolken.
- Vurdere om `Kjernejournal` bør få en tilsvarende språklig og strukturell utdyping, særlig i `Hovedfunksjoner` og avgrensning mot andre helseløsninger.
- Vurdere om `Helsedata.no` bør løftes ett hakk for å tydeliggjøre rollen som tilgangsflate, veiledningsflate og del av helsedataforvaltningen.
- Etter denne korte poleringsrunden: avgjøre om neste steg bør være EU-kandidater, flere nye nasjonale produkter eller ny revisjon av eldre beskrivelser.

**Produktregisteret –" konkrete valg som trengs:**

- Vurdere og avklare om `FIKS IO` skal inn som egen ressurs i produktregisteret, eller fortsatt behandles som teknisk komponent under `FIKS Melding` og tilhørende samhandlingsmønstre.
- Vurdere om `Fiks register`-beskrivelsen bør strammes inn ytterligere som overordnet registerfamilie i Fiks, nå som `Fiks folkeregister`, `Fiks skatte- og inntektsopplysninger` og `Fiks kjøretøyregister` er ført som egne ressurskandidater.
- Vurdere om flere KS Digital-tjenester utenfor dagens operative KS-liste bør inn som egne ressurser i produktregisteret, eller fortsatt behandles som sektorspesifikke løsninger utenfor første prioritet.

---

## Strategiske forbedringer –" Arbeidsflyt og kvalitetssikring

Disse skal tas inn *parallelt* med produktgrunnlag-arbeidet og vil gjøre det lettere å skalere:

### Forbedringsmulighet for analysemal basert på utprøving

**Funn fra utproving:** En samlet analyse med flere problemstillinger ga svakere presisjon i produktvurdering og tiltaksprioritering.

**Tiltak som er innført:**
- Tidlig sjekk av om innsendt underlag er ett case eller flere.
- Krav om splitting av analysen ved flere overganger/problemstillinger.
- Fast vurderingsrekkefølge for produktkategorier.
- Obligatorisk klassifisering av tiltak etter gap-type (produkt, semantisk, juridisk, samordning).
- Krav om minst ett sammensatt løsningsmønster for eksisterende produkter før nyutvikling foreslås.

**Neste forbedring som bør vurderes:**
- Legge inn en enkel evalueringsrubrikk i malen med score 1-5 for sporbarhet, gjenbrukbarhet, styringsrelevans og presisjon i produktvurdering.

### Modulær struktur for produktbeskrivelser

**Anledning:** Nåværende produktbeskrivelser blander kilder, KI-analyse og publiserbar tekst i ett lag. Dette gjør det uklart hva som er verifisert kilde, hva som er arbeidsgrunnlag, og hva som skal publiseres. Det gjør også vedlikehold vanskeligere når kilder endres.

**Forslag:** Etabler en tre-lags modell:
1. **Kildegrunnlag og arkitekturnotater** –" Strukturerte kilder, API-dokumentasjon, produktregisteret og prinsippmasterdata fra `arkitektur/`. Dette er input som står fast.
2. **Analyseblokker** –" KI-utledet innhold som koblingsvurderinger, risikoanalyse, gjenbruksmuligheter og målkobling. Disse genereres fra laget over og er arbeidsgrunnlag.
3. **Publiserbar tekst** –" Validert tekst for nett og arkitekturveiledning, satt sammen fra analyseblokker med faglig gjennomgang. Dette er sluttresultat.

**Praktisk gjennomføring (uten repo-omstrukturering):**
- Lag en systematisk annotasjonsstandard i produkt-canvas-prompten: hver analyseblokk merkes med kilde og type (f.eks. `[Analyse]`, `[Kilde]`, `[Utledet fra X]`).
- Oppdater canvas-template med eksempler på hvordan kildegrunnlag skal presenteres.
- Legg inn tydelig merking i alle beskrivelser: "**KI-støttet arbeidsgrunnlag** –" ikke faglig godkjent" inntil kvalitetssikring etableres.
- Bruk merkingen konsekvent, slik at værktøy og mennesker kan filtrere etter status.

**Hvorfor det er lurt:**
- **Transparens:** Alle ser hva som er kilde vs. analyse, og dermed grunnlag for påstander.
- **Gjenbruk:** Samme kildegrunnlag fôres inn i flere arbeitsflyter (produkt-canvas, web, API, KI-retrieval) uten duplikering.
- **Vedlikehold:** Når kilder oppdateres (ny API, ny kapabilitetsmapping), rettes bare på ett sted.
- **Kvalitetskontroll:** Merking muliggjør faglig godkjennelse før innhold publiseres.
- **KI-verktøy:** Gjør det mulig for later KI-assistenter å støttes av stabile inndata.

**Implementering:**
- Oppdater `produkt-canvas.system.md` med merking-standarden.
- Vurder om modulær merking skal prøves ut på neste større revisjonsrunde uten å forstyrre dagens canvas-format.
- Dokumenter læringa i `briefs/arbeidsstyring-og-handover/`.
- Etabler senere: status-field (`draft`, `review`, `published`), godkjennelsesprosess, filtrerbar liste.

---

## Konkrete neste oppgaver –" Prioritert rekkefølge

1. **Produktgrunnlag (uke 1-4):**
   - Implementer merkings-standard i `produkt-canvas.system.md`.
   - Velg neste sektor eller produktklynge for samme revisjonsløp etter at KS og Altinn er gjennomgått.
   - Kvalitetssikre `SIKT`-ressursene (`Feide`, `Vitnemålsportalen`) mot produkt-kapabilitet-master.

2. **Dokumentasjon av ny prosess:**
   - Lag en kort notat i `briefs/arbeidsstyring-og-handover/` som viser hvordan merking-standarden brukes i praksis.

3. **Produktregisteret (uke 2-4):**
   - Legg inn første ressurser fra `HDIR` og `NAV` med eierbasert ID-prinsipp.
   - Kvalitetssikre `KS`-ressurser mot gjeldende masterfil.
   - Gjør de konkrete FIKS-valgene (IO, Register).

4. **Web-synk:**
   - Kjør avviksjekk og oppdater genererte oversikter.

5. **Oppfølging (senere):**
   - Etabler status-felt og godkjennelsesprosess i produktbeskrivelser.

---

## Bekjente blokkere og risiko –" For nåværende arbeid

- Eldre produktbeskrivelser kan gi ujevn retrieval-kvalitet (må oppgraderes gradvis).
- Produktbeskrivelsene mangler tydelig merking av arbeidsgrunnlag vs. godkjent innhold (fikses med modulær struktur).

---

## Strukturelle forbedringer –" Dagens repo

Disse kan gjøres *når som helst* parallelt, men er ikke kritisk for produktgrunnlag-arbeidet:

**For organisering av kildegrunnlag og metadata:**
- Følge opp om `produktnummerering.md` senere bør få et mer presist navn, for eksempel `produktregister.md`, når strukturen ellers er stabil.
- Vurdere om `sources/links.md` på sikt bør flyttes nærmere produktområdet eller få egen struktur.

**For genererte beskrivelser:**
- Følge opp om produktbeskrivelser senere bør deles i understrukturer under `arkitektur/ressurser/operative-losninger-og-tjenester/`, for eksempel etter status, eier eller publiseringsnivå.

**For større omstrukturering (ikke nå):**
- Vurdere om og når deler av dagens produktområde gradvis bør flyttes eller speiles inn i den bredere ressursstrukturen under `arkitektur/ressurser/`.
- Lage første konkrete pilotklassifisering og innholdsstruktur for `FINT` og `VIGO` etter de nye styringsreglene under `arkitektur/ressurser/`.
- Vurdere om delressurser under `VIGO`, som `VIGO Sentralbase` og `VIGO Kodeverk og kodeverksbase`, bør beskrives som egne operative ressurser eller bare omtales under hovedressursen.
- Verifisere full Hugo-build når `hugo` er tilgjengelig i miljøet.
- Vurdere neste sektorbolk etter Digdir og KS, eller om det er riktig tidspunkt for et eget navneharmoniseringsløp.
- Forberede neste sektorvise flytteløp av eksisterende operative beskrivelser, med tydelig regel for hvilke filer som blir stående i gammel struktur gjennom overgangsperioden.
- Lage første avledede malutkast for `samarbeidsfora`, basert på feltene i dagens `produkt-canvas` som faktisk gir verdi uten å bli kunstige.

Status 2026-04-09:
- Første konkrete flytteløp er nå spesifisert for Digdir i `briefs/arbeidsstyring-og-handover/2026-04-09-digdir-flyttelop-v1.md`.
- Digdir-piloten er nå gjennomført: 22 siste Digdir-beskrivelser er flyttet til `arkitektur/ressurser/operative-losninger-og-tjenester/` og tilhørende register- og mappingpekere er oppdatert.
- KS-løpet er nå gjennomført: 9 siste KS-beskrivelser er flyttet til `arkitektur/ressurser/operative-losninger-og-tjenester/` og tilhørende register- og mappingpekere er oppdatert.
- SIKT-løpet er nå gjennomført: 6 siste SIKT-beskrivelser er flyttet til `arkitektur/ressurser/operative-losninger-og-tjenester/` og tilhørende register- og mappingpekere er oppdatert.
- Helse-løpet er nå gjennomført: 7 siste beskrivelser for `HDIR`, `NHN` og `HELFO` er flyttet til `arkitektur/ressurser/operative-losninger-og-tjenester/` og tilhørende register- og mappingpekere er oppdatert.
- Restbolken er nå gjennomført: 11 siste beskrivelser for `NAV`, `SKATT`, `KART`, `BRREG`, `SVV`, `SSB` og `FLERE` er flyttet til `arkitektur/ressurser/operative-losninger-og-tjenester/` og tilhørende register- og mappingpekere er oppdatert.
- Webgeneratoren for kapabilitetssider bygger nå lenker fra faktisk `relative_path`, slik at flyttede filer fortsatt peker riktig i generert innhold.
- De nye `NOVARI`-ressursene er harmonisert til samme nummererte filnavnsmønster som resten av porteføljen, og styringsreglene presiserer nå at nye ressursfiler skal følge dette når løpenummer er fastsatt.
- Webgeneratoren for ressursoversikten bygger nå egne undersider for ressursenes hovedtyper, slik at operative løsninger og tjenester, normerende ressurser og andre resterende ressurser kan navigeres separat i weben.
- Første hovedmigrering av siste operative beskrivelser er dermed i praksis fullført.
- Lokal Hugo-build er fortsatt ikke verifisert fordi `hugo` ikke er installert i dette miljøet.

---

## Assistenten på web –" Planlegging og MVP (framtidig videreutvikling)

Denne seksjonen handler om å bygge en åpen web-basert KI-dokumentasjonsassistent som beskrevet i [MVP-skisse](briefs/arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md). 

**Status:** Dette er *ide* og *planlegging*, ikke konkrete neste steg. Kun aktuelt hvis beslutning tas om å investere i web-assistenten.

### Backend og infrastruktur (når/hvis prosjekt startes)

- Avklar lisens for dokumentasjonsinnholdet i repoet.
- Velg backend-plattform (foreslått: Azure Functions).
- Lag første backend-skjelett for `/api/ask`.
- Lag første indeksjobb for repo-dokumentasjonen.
- Legg inn enkel chat-widget i Hugo-prototypen.

### Webgrunnlag –" Utvidelse av dagens publisering

- Verifiser at GitHub Pages bruker Actions-baserte deployments (ikke gammel `docs/`-publisering).
- Vurdere om weben også skal generere kapabilitets- og prinsippsammendrag direkte fra kuraterte filer i `arkitektur/`, slik at man unngår dobbelt vedlikehold av innledningstekster.
- Vurdere om weben også bør få en egen målside bygget fra `arkitektur/maal/maal.md`, slik at mål, prinsipper, kapabiliteter og ressurser kan leses i samme struktur.
- Vurdere om kapabilitetssidene på web også skal hente prinsippreferanser direkte fra `principles.md`, slik at all prinsipplogikk ligger ett sted.

### Assistenten –" Expanded scope (senere fase)

**Kjernefunksjonalitet (hvis MVP godkjennes):**
- Chat-interface som svarer spørsmål basert på produktregisteret, kapabiliteter og prinsipper.
- Retrieval fra repo-dokumentasjonen (produktbeskrivelser, arkitektur, veiledninger).
- Sporbare kilder –" assistenten skal vise hvilke dokumenter den hentet fra.

**Utvidelser som kan vente:**
- Vurdere om flere helse- og NAV-ressurser bør inn i registeret, særlig flere delingstjenester og nasjonale innbyggertjenester.
- Vurdere om flere EU-byggesteiner bør behandles som referanseressurser uten prioritering for egne produktbeskrivelser.
- Vurdere om noen EU-referanseressurser bør få korte oversiktsbeskrivelser i weben uden at de blir fullverdige produkt-canvas-filer.
- Gå gjennom avviksrapporten for XML mot kapabilitets- og prinsippgrunnlaget og avgjøre om flere beskrivelsestekster skal kurateres videre inn.
- Vurdere om det senere trengs en egen kuratert koblingsfil mellom hovedkapabiliteter og strategiske mål, dersom målsporet skal brukes operativt.
- Vurdere om `Altinn` som paraplyressurs skal beholdes eller splittes tydeligere fra underliggende Digdir-løsninger.

### Blokkere for assistenten-prosjektet

- Repoet har ingen eksplisitt lisens for dokumentasjonsinnholdet.
- Åpen internettflate krever moderering, rate limiting og tydelig avgrensning av datagrunnlag.
- GitHub Pages-oppsettet må verifiseres før live-publisering.
- Produktbeskrivelsene må ha høy og konsistent kvalitet før de brukes i retrieval.

---

## Referanser

- [MVP-skisse for dokumentasjonsassistent](briefs/arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md) –" Hele konseptet og arkitektur-ideen for assistenten.



