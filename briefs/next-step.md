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

**Prioritet nÃ¥ (uker 1-6):** Les "Hva gjenstÃ¥r", "Strategiske forbedringer", "Konkrete neste oppgaver" og "Bekjente blokkere".

**Strukturelle forbedringer du kan gjÃ¸re parallelt:** Les "Strukturelle forbedringer â€” Dagens repo".

**Framtidig videreutvikling (nÃ¥r det blir aktuelt):** Les hele "Assistenten pÃ¥ web â€” Planlegging og MVP" pÃ¥ slutten.

---

## Hva er gjort
- Testet ny mal for arkitekturassistert analyse av utviklingsbehov pÃ¥ to separate case, splittet analysen i egne filer og oppdatert instruks med eksplisitt splittingsregel.
- Forbedret analysemalen med tidlig avklaring av ett/flere case, fast vurderingsrekkefÃ¸lge for produktkategorier, gap-type per tiltak og seksjon for sammensatte lÃ¸sningsmÃ¸nstre.
- Oppdatert utvalgte produktbeskrivelser med generell beslutningsstÃ¸ttefelt: typiske brukssituasjoner, nÃ¥r produktet normalt ikke er fÃ¸rstevalg og vanlige kombinasjoner med andre produkter.
- Definert mÃ¥lbildet for en Ã¥pen dokumentasjonsassistent pÃ¥ nettsiden.
- Avgrenset MVP til kun offentlig informasjon fra repoet.
- Beskrevet anbefalt arkitektur med Hugo-frontend, egen backend og OpenAI retrieval.
- Dokumentert lisens- og avtaleavklaringer som mÃ¥ pÃ¥ plass fÃ¸r bygging.
- Oppdatert produktbeskrivelsene for produkt `02-06` til nye `v3-codex`-versjoner med sterkere kildegrunnlag og strammere kapabilitetsvalg.
- Oppdatert prompt og mal for produkt-canvas slik at nye beskrivelser ikke skal starte med egen linje for mÃ¥lgruppe, og `Ressurs ID` ikke skal ha parentesforklaring.
- Strammet inn metodekravet for kapabiliteter: bare direkte og sterke koblinger til produktets egen funksjon skal tas med.
- Regenerert produktoverÂ­sikten i Hugo-prototypen slik at siste versjon for produkt `02-06` nÃ¥ vises pÃ¥ nettsiden.
- Lagt om publiseringsmodellen for Hugo-prototypen til GitHub Pages artifact-deploy direkte fra `web/hugo-prototype/`.
- Standardisert repoet med `.editorconfig` og `.gitattributes` for Ã¥ redusere risikoen for nye tegnkodings- og linjesluttfeil i tekstfiler.
- Utvidet encoding-validatoren slik at den ogsÃ¥ fanger typiske `?`-skader inne i norske ord, ikke bare klassisk mojibake.

- Kvalitetssjekket masterfila for produkt-kapabilitet-koblinger og strammet inn koblingene til et fÃ¸rste manuelt arbeidsutkast basert pÃ¥ direkte og sterke koblinger.
- Lagt om produktregisteret til eierbasert `Ressurs ID`, med ekstra kolonner for ressurstype, kapabilitetstreff og lenke til siste dokumentversjon.
- Oppdatert siste versjon av produkt `01-24` slik at feltet `Ressurs ID` nÃ¥ bruker eierbasert identifikator.
- Lagt inn fÃ¸rste arbeidsutkast for ressurser fra `KS`, `HDIR`, `NAV` og `SKATT` i produktregisteret, basert pÃ¥ `sources/links.md`.
- Utvidet produktregisteret med kolonnen `Ressurskategori` og lagt inn flere verifiserte kandidater fra `KS`, `NHN`, `NAV`, `Skatteetaten`, `Kartverket` og relevante EU-byggesteiner.
- Utvidet produktregisteret videre med `SIKT` som egen eiergruppe og fÃ¸rste arbeidsutkast for Feide, FS, opptakslÃ¸sninger, Nasjonal vitnemÃ¥lsdatabase og VitnemÃ¥lsportalen som kandidater for tverrsektoriell samhandling.
- Kvalitetssikret fÃ¸rste arbeidsutkast for `SIKT`-ressursene og utvidet registeret med `Nasjonalt utdanningsregister` som egen kandidat for tverrsektoriell samhandling i utdanningssektoren.
- Kvalitetssikret `BRREG` og `KS` i produktregisteret med strammere kapabilitetstreff og tydeligere skille mellom register, plattform og tilgangstjeneste.
- Kvalitetssikret `HDIR`, `NHN` og `NAV` i produktregisteret med tydeligere skille mellom portal, tillitstjeneste, delingslÃ¸sning og register.
- Kvalitetssikret `SKATT`, `KART` og `DIGDIR` i produktregisteret med mer direkte kapabilitetstreff, sÃ¦rlig for `eFormidling`, `Norge.no`, `Skatteetatens delingstjenester` og `Geonorge`.
- Opprettet fÃ¸rste produktbeskrivelser for KS-ressursene `KS-001` til `KS-006` og synkronisert produktregister, masterfil for produkt-kapabilitet-koblinger og webgrunnlag mot de nye filene.
- Oppdatert lenkedokumentet med egne lenker for ELMA, OpenPeppol og EHF-/Peppol-veiledning, og opprettet nye `v3-codex`-beskrivelser for `ELMA` og `Peppol eDelivery`.
- Avklart at `EU-003 eDelivery Building Block` beholdes i registeret som egen EU-ressurs, men som referanseramme og byggestein rundt samme problemomrÃ¥de som `Peppol eDelivery`.
- Utvidet EU-delen med `EU Open Source Solutions Catalogue`, `Interoperable Europe Solutions` og `Core Vocabularies` som referanseressurser, og oppdatert lenkedokumentet med flere offisielle interoperabilitetskilder fra Interoperable Europe.
- Sammenlignet ny XML-kilde for nasjonal arkitektur med `capabilities.yaml`, laget avviksrapport i `sources/` og rettet manglende `P6`-kobling for `Datautveksling og integrasjon`.
- Fylte ut `arkitektur/prinsipper/principles.md` med operative prinsipper og synket prinsippkoblingene mot webversjonen.
- Knyttet `arkitektur/prinsipper/principles.md` direkte inn i videre bruk: som kilde for prinsipper i produktanalyser, som synkgrunnlag for webens prinsippside og som del av repoets dokumenterte arbeidsflyt.
- Dokumentert rÃ¥kilder, kuraterte arbeidsfiler og videre prosessering i [struktur-og-bearbeiding.md](c:/Users/HILROS/NA-kunnskap/arkitektur/struktur-og-bearbeiding.md).
- Kartlagt mÃ¥l- og ressursrelasjoner i XML-kilden, dokumentert at ressursrelasjonene ikke er pÃ¥ samme nivÃ¥ som repoets produktmaster, og opprettet [maal.md](c:/Users/HILROS/NA-kunnskap/arkitektur/maal/maal.md) som fÃ¸rste kuraterte mÃ¥loversikt.
- Ryddet `capabilities.yaml` slik at den nÃ¥ bare inneholder kapabilitetsstrukturen, mens prinsipptekst og mÃ¥lspor ligger i egne kuraterte filer.
- Utvidet `maal.md` med de fÃ¥ eksplisitte kapabilitet-til-mÃ¥l-koblingene som faktisk finnes i XML-kilden, og markerte hvilke som er operative versus generiske.
- KjÃ¸rt avviksjekk mellom siste produktbeskrivelser og gjeldende produkt-kapabilitetsmaster, og dokumentert funnene i en egen rapport i `sources/`.
- Synket alle siste produktbeskrivelser mot gjeldende produkt-kapabilitetsmaster og oppdatert avviksrapporten slik at den nÃ¥ viser `0` avvik.
- Opprettet fÃ¸rste `SIKT`-produktbeskrivelser for `Feide` og `VitnemÃ¥lsportalen`, og synket produktregister, koblingsfil og genererte weboversikter mot de nye filene.
- Opprettet nye KS-produktbeskrivelser for `SvarInn` og `FIKS Folkeregister`, og synket produktregister, koblingsfil, lenkedokument og genererte weboversikter mot de nye filene.
- Opprettet nye KS-produktbeskrivelser for `Fiks skatte- og inntektsopplysninger` og `Fiks kjÃ¸retÃ¸yregister`, og fullfÃ¸rt fÃ¸rste gjennomgang av de registrerte KS-/KS Digital-produktene i produktregisteret.
- Opprettet `Fiks register v2` med oppdatert KS-kildegrunnlag og tydeligere avgrensning mellom den overordnede registerfamilien og undertjenestene under samme produktomrÃ¥de.
- Opprettet `Fiks melding v2` med oppdatert KS-kildegrunnlag og tydeligere beskrivelse av produktet som kanalplattform med flere undertjenester og bruksmÃ¥ter.
- Opprettet ny versjon `v2-copilot` for `SvarUt` med oppdatert kildegrunnlag fra `sources/links.md` og ny verifisering av produktside, utviklerdokumentasjon, prisoversikt og driftsstatus.
- Justert sprÃ¥kfÃ¸ring i `SvarUt v2` tettere mot etablert tone i forrige versjon, og oppdatert instruksgrunnlaget slik at fremtidige revisjoner skal bevare velfungerende tone og unngÃ¥ unÃ¸dvendig full omskriving.
- GjennomfÃ¸rt ny sammenligning av `SvarUt v1` og `v2`, og harmonisert flere nÃ¸kkelseksjoner i `v2` til v1-tonen der innholdet fortsatt er korrekt.
- Oppdatert styringsprompten for produkt-canvas med tydelig krav om sprÃ¥k for bÃ¥de forretning og arkitektur: lett Ã¥ forstÃ¥ uten systemforstÃ¥else, men med nok funksjonsdetaljer for gjenbruksvurdering.
- Flyttet produktbeskrivelsene til `arkitektur/ressurser/operative-losninger-og-tjenester/` og avviklet duplikatoversiktene i `results/Produktregister/`, slik at `arkitektur/ressurser/produktnummerering.md` nÃ¥ er eneste operative master for produktregisteret.
- Ryddet KS-delen i produktregisteret etter KS Digitals nÃ¥vÃ¦rende navngivning, fjernet `Felles tjenesteplattform` fra operativ ressursliste og la inn `Fiks skatte- og inntektsopplysninger` og `Fiks kjÃ¸retÃ¸yregister` som egne kandidater under samme logikk som `Fiks folkeregister`.
- Harmoniserte KS-produktnavn i berÃ¸rte produktbeskrivelser og koblingsgrunnlag, og synket weboversiktene slik at `Fiks SvarUt` nÃ¥ peker til siste versjon `v2 (copilot)`.
- Opprettet `SvarUt v3 (codex)` med oppdatert KS-kildegrunnlag, tydeligere API- og versjonsbilde, strammere scope og mer presis navnebruk fÃ¸r ekstern kvalitetssjekk hos KS.
- Standardiserte filnavn for FIKS-relaterte KS-beskrivelser slik at `FIKS` brukes konsekvent med store bokstaver i filnavn, blant annet for `FIKS SvarUt` og `FIKS Digiorden`.
- Oppdatert styringsprompten for produkt-canvas med eksplisitt kontroll av lÃ¸sningsbredde, slik at nye beskrivelser mÃ¥ sjekke hele produktets operative rolle og ikke bare beskrive ett grensesnitt som API eller portal.
- Skjerpet prompten videre slik at `Hovedfunksjoner` normalt skal skrives som minst 3-4 forklarende avsnitt nÃ¥r kildene gir grunnlag for det, og oppdatert `FIKS SvarUt v3` i trÃ¥d med dette.
- Revidert Altinn-produktene `Altinn Autorisasjon`, `Altinn Formidling`, `Altinn Events`, `data.altinn.no`, `Altinn 3 plattform` og `Altinn Studio` til nye codex-versjoner med oppdatert kildegrunnlag, tydeligere lÃ¸sningsbredde og strammere produktavgrensning.
- Revidert ogsÃ¥ `Dialogporten`, `Altinn Melding` og `Altinn Varsling` til nye codex-versjoner, slik at hele den operative Altinn-listen nÃ¥ fÃ¸lger nyere instruks og oppdatert kildekontroll.
- Opprettet `Digital postkasse v3` med oppdatert Digdir-kildegrunnlag, tydeligere beskrivelse av hele leveranselÃ¸pet og strammere avgrensning mot kontaktregister, avsendersystem og generell meldingsutveksling.
- Oppdatert `sources/links.md` med flere konkrete Digdir-kilder for Digital postkasse, inkludert oversikt, ta i bruk, kostnadsmodell, statistikk og teknisk dokumentasjon.
- Opprettet `Felles datakatalog v3` med oppdatert Digdir-kildegrunnlag og tydeligere skille mellom den overordnede metadata- og publiseringslÃ¸sningen, `data.norge.no` som portal og delkatalogene under samme produktomrÃ¥de.
- Oppdatert `sources/links.md` med nyere og mer presise kilder for Felles datakatalog, inkludert ny Digdir-side, ta-i-bruk-lÃ¸p og kravside for registrering av datasett.
- Opprettet `Begrepskatalog v3` med oppdatert Digdir-kildegrunnlag og tydeligere avgrensning som semantisk delkatalog under Felles datakatalog, ikke som egen generell ontologi- eller datakatalogplattform.
- Oppdatert `sources/links.md` med konkrete kilder for Begrepskatalogen, inkludert katalogflaten og teknisk dokumentasjon pÃ¥ data.norge.no.
- Opprettet `API-katalog v3` med oppdatert Digdir-kildegrunnlag og tydeligere avgrensning som delkatalog for API-beskrivelser, ikke som gateway, runtime-plattform eller generell utviklerportal.
- Oppdatert `sources/links.md` med konkrete kilder for API-katalogen, inkludert katalogflaten og teknisk API-dokumentasjon pÃ¥ data.norge.no.
- Opprettet fÃ¸rste produktbeskrivelse for `HelseID` med oppdatert NHN-kildegrunnlag og tydelig beskrivelse av produktet som felles tillits- og autentiseringskomponent for helse- og omsorgssektoren.
- Oppdatert `sources/links.md` med flere konkrete NHN-kilder for HelseID, inkludert hvorfor bruke-lÃ¸p, spÃ¸rsmÃ¥l og svar, personvern, utbredelse og utviklerportal.
- Opprettet fÃ¸rste produktbeskrivelse for `Matrikkelen` med oppdatert Kartverket-kildegrunnlag og tydelig beskrivelse av produktet som nasjonalt grunndataregister og statlig felleskomponent.
- Oppdatert `sources/links.md` med flere konkrete Kartverket-kilder for Matrikkelen, inkludert om-side, tilgangslÃ¸p, fÃ¸ringsomrÃ¥der og faggruppe.
- Opprettet fÃ¸rste produktbeskrivelse for `Folkeregisteret` med oppdatert Skatteetaten-kildegrunnlag og tydelig beskrivelse av produktet som nasjonalt personregister og statlig felleskomponent for persondata.
- Oppdatert `sources/links.md` med flere konkrete Skatteetaten-kilder for Folkeregisteret, inkludert om-side, tilgangslÃ¸p og hÃ¥ndbokssider for delingstjenester.
- Opprettet fÃ¸rste produktbeskrivelse for `Enhetsregisteret` med oppdatert BrÃ¸nnÃ¸ysundregistrene-kildegrunnlag og tydelig beskrivelse av produktet som nasjonalt virksomhetsregister og felleskomponent for virksomhetsdata.
- Oppdatert `sources/links.md` med flere konkrete BRREG-kilder for Enhetsregisteret, inkludert organisasjonsnummer, full maskinell tilgang og Ã¥pne data-varsler.
- Opprettet fÃ¸rste produktbeskrivelse for `Skatteetatens delingstjenester` med oppdatert Skatteetaten-kildegrunnlag og tydelig beskrivelse av produktet som samlet delingsflate for API-basert datadeling.
- Oppdatert `sources/links.md` med flere konkrete Skatteetaten-kilder for delingstjenestene, inkludert hvorfor-siden, kontaktlÃ¸p og bruksvilkÃ¥r.
- Opprettet fÃ¸rste produktbeskrivelse for `A-ordningen` med oppdatert kildegrunnlag fra Skatteetaten og a-ordningen.no, og tydelig beskrivelse av produktet som samforvaltet rapporterings- og delingsordning.
- Oppdatert `sources/links.md` med flere konkrete kilder for A-ordningen, inkludert om-side, kontaktflate og informasjonsmÃ¸te 12. mars 2026.
- Opprettet fÃ¸rste produktbeskrivelse for `Felles studentsystem (FS)` med oppdatert Sikt-kildegrunnlag og tydelig beskrivelse av produktet som nasjonal studieadministrativ plattform med databaser, brukerflater og integrasjoner.
- Oppdatert `sources/links.md` med flere konkrete Sikt-kilder for FS, inkludert `fs.sikt.no`, FS-API og API-katalogen for studieadministrasjon.
- Opprettet fÃ¸rste produktbeskrivelse for `Nasjonal vitnemÃ¥lsdatabase (NVB)` med oppdatert Sikt-kildegrunnlag og tydelig beskrivelse av produktet som nasjonal database- og delingstjeneste for elektroniske vitnemÃ¥l.
- Oppdatert `sources/links.md` med flere konkrete Sikt-kilder for NVB, inkludert tjenestekatalog og moderniseringsretning mot bredere kompetanseregister.
- Opprettet fÃ¸rste produktbeskrivelse for `Helsenorge` med oppdatert NHN-kildegrunnlag og tydelig beskrivelse av produktet som nasjonal innbyggerportal og sammenhengende tjenesteflate i helsesektoren.
- Vurdert `NVDB` opp mot `Geonorge` og valgt `Geonorge` som sterkere tverrsektoriell kandidat for denne runden.
- Opprettet fÃ¸rste produktbeskrivelse for `Geonorge` med oppdatert Kartverket-/Geonorge-kildegrunnlag og tydelig beskrivelse av produktet som nasjonal metadata-, katalog- og delingsplattform for geodata.
- Oppdatert `sources/links.md` med flere konkrete kilder for Geonorge, inkludert om-side, API-er og distribusjonsmodell.
- Opprettet fÃ¸rste produktbeskrivelse for `Helsedata.no` som nasjonal portal og tilgangsflate for helsedata.
- Opprettet fÃ¸rste produktbeskrivelse for `HPR` som nasjonalt register over helsepersonell.
- Opprettet fÃ¸rste produktbeskrivelse for `Kjernejournal` som nasjonal samhandlingslÃ¸sning for utvalgte helseopplysninger.
- Opprettet fÃ¸rste produktbeskrivelse for `e-resept` som nasjonal lÃ¸sning for elektronisk forskrivning og reseptformidling.
- Opprettet fÃ¸rste produktbeskrivelse for `DSOP-tjenester` som samlet offentlig-privat delings- og samhandlingsflate.
- Opprettet fÃ¸rste produktbeskrivelse for `Aa-registeret` som nasjonalt grunndataregister over arbeidsforhold.
- Opprettet fÃ¸rste produktbeskrivelse for `NAIS` som Ã¥pent dokumentert plattformmodell og gjenbrukbart utviklings- og kjÃ¸remiljÃ¸, med tydeligere avgrensning enn klassiske nasjonale felleskomponenter.
- Opprettet fÃ¸rste produktbeskrivelse for `OpptakslÃ¸sninger` som felles systemstÃ¸tte for samordnet opptak.
- Opprettet fÃ¸rste produktbeskrivelse for `Nasjonalt utdanningsregister` som felles autoritativ kilde for utdanninger og lÃ¦resteder.
- Opprettet fÃ¸rste produktbeskrivelse for `KUHR` som sentralt register- og oppgjÃ¸rssystem for helserefusjoner.
- Opprettet fÃ¸rste produktbeskrivelse for `microdata.no` som nasjonal analyseplattform for kontrollert bruk av registerdata.
- Opprettet fÃ¸rste produktbeskrivelse for `Motorvognregisteret` som nasjonal registerressurs for kjÃ¸retÃ¸yopplysninger.
- Kvalitetssikret den siste bolken med nye produktbeskrivelser og lÃ¸ftet sÃ¦rlig `HPR`, `e-resept`, `OpptakslÃ¸sninger` og `Nasjonalt utdanningsregister` til et mer forklarende nivÃ¥ i trÃ¥d med gjeldende instruks.
- Oppdaget at filene for `KUHR`, `microdata.no` og `Motorvognregisteret` manglet i produktmappa selv om registeret pekte til dem, og opprettet dem pÃ¥ nytt med fullverdige beskrivelser.
- Presisert `NAIS` videre som en interessant og gjenbrukbar plattformmodell, men uten samme dokumenterte status som formell nasjonal felleslÃ¸sning eller klassisk felleskomponent.
- Etablert fÃ¸rste styringsstruktur for et bredere ressursomrÃ¥de under `arkitektur/ressurser/`, med egen styringsfil for `operative lÃ¸sninger og tjenester`, `normerende ressurser` og `samarbeidsfora`.
- Oppdatert `sources/links.md` med fÃ¸rste Novari-kilder for `FINT Felleskomponent`, `FINT Arkiv`, `FINT Informasjonsmodell` og `VIGO`, og presisert at dagens `produkt-canvas` brukes direkte for operative ressurser men mÃ¥ avledes for normerende ressurser og samarbeidsfora.
- Opprettet fÃ¸rste avledede mal for normerende ressurser i `config/templates/normerende-ressurs-template.md`, som grunnlag for blant annet `FINT Informasjonsmodell`.
- Opprettet fÃ¸rste konkrete normerende ressursbeskrivelse for `FINT Informasjonsmodell` i `arkitektur/ressurser/normerende-ressurser/`, basert pÃ¥ Novari-kilder og ny avledet mal.
- Opprettet fÃ¸rste operative ressursbeskrivelser for `FINT Felleskomponent` og `FINT Arkiv`, og fÃ¸rt `NOVARI`-ressursene inn i `arkitektur/ressurser/produktnummerering.md` slik at eksisterende nummerering og registerlogikk beholdes som Ã©n operativ master.
- Opprettet fÃ¸rste operative ressursbeskrivelse for `VIGO` og laget en konkret migreringsplan for overgang fra dagens produktstruktur til bredere ressursstruktur i `briefs/arbeidsstyring-og-handover/2026-04-09-migreringsplan-ressursstruktur-v1.md`.
- Opprettet fÃ¸rste operative ressursbeskrivelse for `VIGO` og oppdatert `NOVARI-004` i `produktnummerering.md` med kapabilitetstreff og dokumentlenke.

## Hva gjenstÃ¥r â€” Produktgrunnlag utvikling (neste 4-6 uker)

**Kjerneprioriteter â€” disse skal gjÃ¸res fÃ¸rst:**

- Fortsette revisjon av eldre produktbeskrivelser sektorvis etter samme metode som for KS- og Altinn-rundene.
- Vurdere om det fortsatt er behov for en ny harmoniseringsrunde pÃ¥ de nylig oppdaterte Digdir-katalogproduktene, eller om neste naturlige steg nÃ¥ er Ã¥ gÃ¥ over til flere nye produkter i neste sektor.
- Ta stilling til om EU-kandidatene skal behandles som egne produktfiler eller fortsatt som referanseressurser, nÃ¥ som den siste nasjonale restlista er fullfÃ¸rt og kvalitetssikret.
- FÃ¸lge opp kvaliteten i selve koblingene mellom produkter og kapabiliteter, sÃ¦rlig i eldre produktbeskrivelser der kapabilitetsseksjonen er svakere eller mindre presis.
- Ta inn de fÃ¸rste ressursene fra KS, Helsedirektoratet, NAV og Skatteetaten i produktregisteret med samme ID-prinsipp.
- Kvalitetssikre de nye arbeidsutkastene for `KS`, `HDIR`, `NAV` og `SKATT`, sÃ¦rlig eierskap, ressurstype og kapabilitetstreff.
- Fortsette `SIKT`-sektoren med de neste ressursene etter `Feide` og `VitnemÃ¥lsportalen`, sÃ¦rlig `Felles studentsystem (FS)` og `Nasjonal vitnemÃ¥lsdatabase`.
- KjÃ¸re avviksjekk og synke produktbeskrivelsene kontinuerlig mot masterfila for produkt-kapabilitet-koblinger.

**Anbefalt liten oppfÃ¸lgingsrunde fÃ¸r nye store bolker:**

- Ta en lett poleringsrunde pÃ¥ `DSOP-tjenester`, som fortsatt er kortere og mer komprimert enn de sterkere beskrivelsene i den siste nasjonale bolken.
- Vurdere om `Kjernejournal` bÃ¸r fÃ¥ en tilsvarende sprÃ¥klig og strukturell utdyping, sÃ¦rlig i `Hovedfunksjoner` og avgrensning mot andre helselÃ¸sninger.
- Vurdere om `Helsedata.no` bÃ¸r lÃ¸ftes ett hakk for Ã¥ tydeliggjÃ¸re rollen som tilgangsflate, veiledningsflate og del av helsedataforvaltningen.
- Etter denne korte poleringsrunden: avgjÃ¸re om neste steg bÃ¸r vÃ¦re EU-kandidater, flere nye nasjonale produkter eller ny revisjon av eldre beskrivelser.

**Produktregisteret â€” konkrete valg som trengs:**

- Vurdere og avklare om `FIKS IO` skal inn som egen ressurs i produktregisteret, eller fortsatt behandles som teknisk komponent under `FIKS Melding` og tilhÃ¸rende samhandlingsmÃ¸nstre.
- Vurdere om `Fiks register`-beskrivelsen bÃ¸r strammes inn ytterligere som overordnet registerfamilie i Fiks, nÃ¥ som `Fiks folkeregister`, `Fiks skatte- og inntektsopplysninger` og `Fiks kjÃ¸retÃ¸yregister` er fÃ¸rt som egne ressurskandidater.
- Vurdere om flere KS Digital-tjenester utenfor dagens operative KS-liste bÃ¸r inn som egne ressurser i produktregisteret, eller fortsatt behandles som sektorspesifikke lÃ¸sninger utenfor fÃ¸rste prioritet.

---

## Strategiske forbedringer â€” Arbeidsflyt og kvalitetssikring

Disse skal tas inn *parallelt* med produktgrunnlag-arbeidet og vil gjÃ¸re det lettere Ã¥ skalere:

### Forbedringsmulighet for analysemal basert pÃ¥ utprÃ¸ving

**Funn fra utproving:** En samlet analyse med flere problemstillinger ga svakere presisjon i produktvurdering og tiltaksprioritering.

**Tiltak som er innfÃ¸rt:**
- Tidlig sjekk av om innsendt underlag er ett case eller flere.
- Krav om splitting av analysen ved flere overganger/problemstillinger.
- Fast vurderingsrekkefÃ¸lge for produktkategorier.
- Obligatorisk klassifisering av tiltak etter gap-type (produkt, semantisk, juridisk, samordning).
- Krav om minst ett sammensatt lÃ¸sningsmÃ¸nster for eksisterende produkter fÃ¸r nyutvikling foreslÃ¥s.

**Neste forbedring som bÃ¸r vurderes:**
- Legge inn en enkel evalueringsrubrikk i malen med score 1-5 for sporbarhet, gjenbrukbarhet, styringsrelevans og presisjon i produktvurdering.

### ModulÃ¦r struktur for produktbeskrivelser

**Anledning:** NÃ¥vÃ¦rende produktbeskrivelser blander kilder, KI-analyse og publiserbar tekst i ett lag. Dette gjÃ¸r det uklart hva som er verifisert kilde, hva som er arbeidsgrunnlag, og hva som skal publiseres. Det gjÃ¸r ogsÃ¥ vedlikehold vanskeligere nÃ¥r kilder endres.

**Forslag:** Etabler en tre-lags modell:
1. **Kildegrunnlag og arkitekturnotater** â€” Strukturerte kilder, API-dokumentasjon, produktregisteret og prinsippmasterdata fra `arkitektur/`. Dette er input som stÃ¥r fast.
2. **Analyseblokker** â€” KI-utledet innhold som koblingsvurderinger, risikoanalyse, gjenbruksmuligheter og mÃ¥lkobling. Disse genereres fra laget over og er arbeidsgrunnlag.
3. **Publiserbar tekst** â€” Validert tekst for nett og arkitekturveiledning, satt sammen fra analyseblokker med faglig gjennomgang. Dette er sluttresultat.

**Praktisk gjennomfÃ¸ring (uten repo-omstrukturering):**
- Lag en systematisk annotasjonsstandard i produkt-canvas-prompten: hver analyseblokk merkes med kilde og type (f.eks. `[Analyse]`, `[Kilde]`, `[Utledet fra X]`).
- Oppdater canvas-template med eksempler pÃ¥ hvordan kildegrunnlag skal presenteres.
- Legg inn tydelig merking i alle beskrivelser: "**KI-stÃ¸ttet arbeidsgrunnlag** â€” ikke faglig godkjent" inntil kvalitetssikring etableres.
- Bruk merkingen konsekvent, slik at vÃ¦rktÃ¸y og mennesker kan filtrere etter status.

**Hvorfor det er lurt:**
- **Transparens:** Alle ser hva som er kilde vs. analyse, og dermed grunnlag for pÃ¥stander.
- **Gjenbruk:** Samme kildegrunnlag fÃ´res inn i flere arbeitsflyter (produkt-canvas, web, API, KI-retrieval) uten duplikering.
- **Vedlikehold:** NÃ¥r kilder oppdateres (ny API, ny kapabilitetsmapping), rettes bare pÃ¥ ett sted.
- **Kvalitetskontroll:** Merking muliggjÃ¸r faglig godkjennelse fÃ¸r innhold publiseres.
- **KI-verktÃ¸y:** GjÃ¸r det mulig for later KI-assistenter Ã¥ stÃ¸ttes av stabile inndata.

**Implementering:**
- Oppdater `produkt-canvas.system.md` med merking-standarden.
- Vurder om modulÃ¦r merking skal prÃ¸ves ut pÃ¥ neste stÃ¸rre revisjonsrunde uten Ã¥ forstyrre dagens canvas-format.
- Dokumenter lÃ¦ringa i `briefs/arbeidsstyring-og-handover/`.
- Etabler senere: status-field (`draft`, `review`, `published`), godkjennelsesprosess, filtrerbar liste.

---

## Konkrete neste oppgaver â€” Prioritert rekkefÃ¸lge

1. **Produktgrunnlag (uke 1-4):**
   - Implementer merkings-standard i `produkt-canvas.system.md`.
   - Velg neste sektor eller produktklynge for samme revisjonslÃ¸p etter at KS og Altinn er gjennomgÃ¥tt.
   - Kvalitetssikre `SIKT`-ressursene (`Feide`, `VitnemÃ¥lsportalen`) mot produkt-kapabilitet-master.

2. **Dokumentasjon av ny prosess:**
   - Lag en kort notat i `briefs/arbeidsstyring-og-handover/` som viser hvordan merking-standarden brukes i praksis.

3. **Produktregisteret (uke 2-4):**
   - Legg inn fÃ¸rste ressurser fra `HDIR` og `NAV` med eierbasert ID-prinsipp.
   - Kvalitetssikre `KS`-ressurser mot gjeldende masterfil.
   - GjÃ¸r de konkrete FIKS-valgene (IO, Register).

4. **Web-synk:**
   - KjÃ¸r avviksjekk og oppdater genererte oversikter.

5. **OppfÃ¸lging (senere):**
   - Etabler status-felt og godkjennelsesprosess i produktbeskrivelser.

---

## Bekjente blokkere og risiko â€” For nÃ¥vÃ¦rende arbeid

- Eldre produktbeskrivelser kan gi ujevn retrieval-kvalitet (mÃ¥ oppgraderes gradvis).
- Produktbeskrivelsene mangler tydelig merking av arbeidsgrunnlag vs. godkjent innhold (fikses med modulÃ¦r struktur).

---

## Strukturelle forbedringer â€” Dagens repo

Disse kan gjÃ¸res *nÃ¥r som helst* parallelt, men er ikke kritisk for produktgrunnlag-arbeidet:

**For organisering av kildegrunnlag og metadata:**
- FÃ¸lge opp om `produktnummerering.md` senere bÃ¸r fÃ¥ et mer presist navn, for eksempel `produktregister.md`, nÃ¥r strukturen ellers er stabil.
- Vurdere om `sources/links.md` pÃ¥ sikt bÃ¸r flyttes nÃ¦rmere produktomrÃ¥det eller fÃ¥ egen struktur.

**For genererte beskrivelser:**
- FÃ¸lge opp om produktbeskrivelser senere bÃ¸r deles i understrukturer under `arkitektur/ressurser/operative-losninger-og-tjenester/`, for eksempel etter status, eier eller publiseringsnivÃ¥.

**For stÃ¸rre omstrukturering (ikke nÃ¥):**
- Vurdere om og nÃ¥r deler av dagens produktomrÃ¥de gradvis bÃ¸r flyttes eller speiles inn i den bredere ressursstrukturen under `arkitektur/ressurser/`.
- Lage fÃ¸rste konkrete pilotklassifisering og innholdsstruktur for `FINT` og `VIGO` etter de nye styringsreglene under `arkitektur/ressurser/`.
- Vurdere om delressurser under `VIGO`, som `VIGO Sentralbase` og `VIGO Kodeverk og kodeverksbase`, bÃ¸r beskrives som egne operative ressurser eller bare omtales under hovedressursen.
- Verifisere full Hugo-build nÃ¥r `hugo` er tilgjengelig i miljÃ¸et.
- Vurdere neste sektorbolk etter Digdir og KS, eller om det er riktig tidspunkt for et eget navneharmoniseringslÃ¸p.
- Forberede neste sektorvise flyttelÃ¸p av eksisterende operative beskrivelser, med tydelig regel for hvilke filer som blir stÃ¥ende i gammel struktur gjennom overgangsperioden.
- Lage fÃ¸rste avledede malutkast for `samarbeidsfora`, basert pÃ¥ feltene i dagens `produkt-canvas` som faktisk gir verdi uten Ã¥ bli kunstige.

Status 2026-04-09:
- FÃ¸rste konkrete flyttelÃ¸p er nÃ¥ spesifisert for Digdir i `briefs/arbeidsstyring-og-handover/2026-04-09-digdir-flyttelop-v1.md`.
- Digdir-piloten er nÃ¥ gjennomfÃ¸rt: 22 siste Digdir-beskrivelser er flyttet til `arkitektur/ressurser/operative-losninger-og-tjenester/` og tilhÃ¸rende register- og mappingpekere er oppdatert.
- KS-lÃ¸pet er nÃ¥ gjennomfÃ¸rt: 9 siste KS-beskrivelser er flyttet til `arkitektur/ressurser/operative-losninger-og-tjenester/` og tilhÃ¸rende register- og mappingpekere er oppdatert.
- SIKT-lÃ¸pet er nÃ¥ gjennomfÃ¸rt: 6 siste SIKT-beskrivelser er flyttet til `arkitektur/ressurser/operative-losninger-og-tjenester/` og tilhÃ¸rende register- og mappingpekere er oppdatert.
- Helse-lÃ¸pet er nÃ¥ gjennomfÃ¸rt: 7 siste beskrivelser for `HDIR`, `NHN` og `HELFO` er flyttet til `arkitektur/ressurser/operative-losninger-og-tjenester/` og tilhÃ¸rende register- og mappingpekere er oppdatert.
- Restbolken er nÃ¥ gjennomfÃ¸rt: 11 siste beskrivelser for `NAV`, `SKATT`, `KART`, `BRREG`, `SVV`, `SSB` og `FLERE` er flyttet til `arkitektur/ressurser/operative-losninger-og-tjenester/` og tilhÃ¸rende register- og mappingpekere er oppdatert.
- Webgeneratoren for kapabilitetssider bygger nÃ¥ lenker fra faktisk `relative_path`, slik at flyttede filer fortsatt peker riktig i generert innhold.
- De nye `NOVARI`-ressursene er harmonisert til samme nummererte filnavnsmÃ¸nster som resten av portefÃ¸ljen, og styringsreglene presiserer nÃ¥ at nye ressursfiler skal fÃ¸lge dette nÃ¥r lÃ¸penummer er fastsatt.
- Webgeneratoren for ressursoversikten bygger nÃ¥ egne undersider for ressursenes hovedtyper, slik at operative lÃ¸sninger og tjenester, normerende ressurser og andre resterende ressurser kan navigeres separat i weben.
- FÃ¸rste hovedmigrering av siste operative beskrivelser er dermed i praksis fullfÃ¸rt.
- Lokal Hugo-build er fortsatt ikke verifisert fordi `hugo` ikke er installert i dette miljÃ¸et.

---

## Assistenten pÃ¥ web â€” Planlegging og MVP (framtidig videreutvikling)

Denne seksjonen handler om Ã¥ bygge en Ã¥pen web-basert KI-dokumentasjonsassistent som beskrevet i [MVP-skisse](briefs/arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md). 

**Status:** Dette er *ide* og *planlegging*, ikke konkrete neste steg. Kun aktuelt hvis beslutning tas om Ã¥ investere i web-assistenten.

### Backend og infrastruktur (nÃ¥r/hvis prosjekt startes)

- Avklar lisens for dokumentasjonsinnholdet i repoet.
- Velg backend-plattform (foreslÃ¥tt: Azure Functions).
- Lag fÃ¸rste backend-skjelett for `/api/ask`.
- Lag fÃ¸rste indeksjobb for repo-dokumentasjonen.
- Legg inn enkel chat-widget i Hugo-prototypen.

### Webgrunnlag â€” Utvidelse av dagens publisering

- Verifiser at GitHub Pages bruker Actions-baserte deployments (ikke gammel `docs/`-publisering).
- Vurdere om weben ogsÃ¥ skal generere kapabilitets- og prinsippsammendrag direkte fra kuraterte filer i `arkitektur/`, slik at man unngÃ¥r dobbelt vedlikehold av innledningstekster.
- Vurdere om weben ogsÃ¥ bÃ¸r fÃ¥ en egen mÃ¥lside bygget fra `arkitektur/maal/maal.md`, slik at mÃ¥l, prinsipper, kapabiliteter og ressurser kan leses i samme struktur.
- Vurdere om kapabilitetssidene pÃ¥ web ogsÃ¥ skal hente prinsippreferanser direkte fra `principles.md`, slik at all prinsipplogikk ligger ett sted.

### Assistenten â€” Expanded scope (senere fase)

**Kjernefunksjonalitet (hvis MVP godkjennes):**
- Chat-interface som svarer spÃ¸rsmÃ¥l basert pÃ¥ produktregisteret, kapabiliteter og prinsipper.
- Retrieval fra repo-dokumentasjonen (produktbeskrivelser, arkitektur, veiledninger).
- Sporbare kilder â€” assistenten skal vise hvilke dokumenter den hentet fra.

**Utvidelser som kan vente:**
- Vurdere om flere helse- og NAV-ressurser bÃ¸r inn i registeret, sÃ¦rlig flere delingstjenester og nasjonale innbyggertjenester.
- Vurdere om flere EU-byggesteiner bÃ¸r behandles som referanseressurser uten prioritering for egne produktbeskrivelser.
- Vurdere om noen EU-referanseressurser bÃ¸r fÃ¥ korte oversiktsbeskrivelser i weben uden at de blir fullverdige produkt-canvas-filer.
- GÃ¥ gjennom avviksrapporten for XML mot kapabilitets- og prinsippgrunnlaget og avgjÃ¸re om flere beskrivelsestekster skal kurateres videre inn.
- Vurdere om det senere trengs en egen kuratert koblingsfil mellom hovedkapabiliteter og strategiske mÃ¥l, dersom mÃ¥lsporet skal brukes operativt.
- Vurdere om `Altinn` som paraplyressurs skal beholdes eller splittes tydeligere fra underliggende Digdir-lÃ¸sninger.

### Blokkere for assistenten-prosjektet

- Repoet har ingen eksplisitt lisens for dokumentasjonsinnholdet.
- Ã…pen internettflate krever moderering, rate limiting og tydelig avgrensning av datagrunnlag.
- GitHub Pages-oppsettet mÃ¥ verifiseres fÃ¸r live-publisering.
- Produktbeskrivelsene mÃ¥ ha hÃ¸y og konsistent kvalitet fÃ¸r de brukes i retrieval.

---

## Referanser

- [MVP-skisse for dokumentasjonsassistent](briefs/arbeidsstyring-og-handover/2026-03-16-dokumentasjonsassistent-mvp-v1.md) â€” Hele konseptet og arkitektur-ideen for assistenten.

