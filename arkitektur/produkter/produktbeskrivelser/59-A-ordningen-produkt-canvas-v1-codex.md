# Produkt-canvas: A-ordningen

## Navn
A-ordningen

## Ressurs ID
FLERE-001

## Status/Livsfase
**Produksjon** - etablert samordnet nasjonal rapporteringsordning for inntekts- og arbeidsforholdsopplysninger.

**Fakta:** Skatteetaten beskriver A-ordningen som en samordnet måte for arbeidsgivere å rapportere opplysninger om inntekt og ansatte til NAV, SSB og Skatteetaten. Ordningen er digital og forvaltes av Skatteetaten på vegne av de andre etatene.

## Modenhet
**Høy modenhet** - innarbeidet, storstilt og samfunnskritisk ordning:
- Ordningen har vært i drift siden 1. januar 2015.
- 260 000 arbeidsgivere rapporterer årlig opplysninger om 4,6 millioner ansatte og pensjonister.
- Over 99 prosent av opplysningene kommer via lønns- og personalsystemer.
- Opplysningene brukes av flere sentrale etater og viderebrukes også av andre virksomheter med hjemmel eller samtykke.

**Deduksjon:** Modenheten er svært høy fordi A-ordningen er blitt en grunnleggende nasjonal rapporterings- og datadelingsordning for arbeids- og inntektsforhold.

## Kort beskrivelse
A-ordningen er den samordnede nasjonale ordningen for at arbeidsgivere skal rapportere opplysninger om inntekt, arbeidsforhold, forskuddstrekk, utleggstrekk, arbeidsgiveravgift og finansskatt. Produktet erstatter flere tidligere skjema- og rapporteringsløp med én digital a-melding, og fungerer samtidig som en felles datakilde for Skatteetaten, NAV, SSB og andre aktører som har lovlig grunnlag for videre bruk. Verdien ligger både i forenklet rapportering og i at opplysningene kan gjenbrukes på tvers av etater og tjenester.

## Kapabiliteter
- **Datakilder: Grunndata** er relevant fordi ordningen produserer og vedlikeholder sentrale opplysninger om arbeidsforhold og inntekt som brukes bredt i offentlig forvaltning.
- **Datautveksling og integrasjon: Dele data med andre** er en kjernefunksjon ved at opplysningene distribueres videre til etater og andre aktører med hjemmel eller samtykke.
- **Samarbeid: Organisatorisk samhandling** er sentralt fordi ordningen forvaltes og brukes i et samspill mellom flere offentlige virksomheter.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Skatteetatens beskrivelse av ordningen, styringsmodellen og viderebruk av opplysningene.

## Produktmål
**Primærkilder:** Skatteetatens side `Om a-ordningen` og tilhørende informasjon om kontakt og bruk av opplysningene.

Dokumenterte mål:
- Forenkle og samordne arbeidsgivers rapportering ved å gå fra fem skjemaer til én a-melding.
- Gi NAV, SSB og Skatteetaten tilgang til samme rapporterte opplysninger gjennom én ordning.
- Gjøre opplysningene tilgjengelige for andre private og offentlige aktører som kan motta dem etter hjemmel eller samtykke.

Operative mål utledet fra de samme kildene:
- Redusere rapporteringsbyrde og dobbeltarbeid for arbeidsgivere.
- Skape et mer oppdatert og samordnet datagrunnlag om inntekt og arbeidsforhold.
- Understøtte bedre saksbehandling, statistikk, kontroll og tjenesteutvikling på tvers av sektorer.

## Brukerbehov
- Arbeidsgivere trenger én samlet og digital rapporteringskanal for lovpålagte opplysninger.
- NAV, SSB og Skatteetaten trenger et oppdatert og samordnet datagrunnlag.
- Andre virksomheter med hjemmel trenger viderebrukbare opplysninger om inntekt og arbeidsforhold.
- Systemleverandører trenger tydelige rapporteringskrav og stabil integrasjon mot a-meldingen.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Arbeidsgivere | Enkel og korrekt rapportering | Innsending av a-melding hver måned | Primær rapporterende brukergruppe |
| Lønns- og HR-systemleverandører | Integrasjon og regelverksnær støtte | Automatisert innsending fra fagsystemer | Over 99 prosent av volumet går via systemer |
| Skatteetaten | Datagrunnlag for skatt, trekk og avgift | Forvaltning, kontroll og innkreving | Forvalter ordningen på vegne av flere |
| NAV | Opplysninger om arbeidsforhold og inntekt | Saksbehandling og kontroll av ytelser | Tett kobling til Aa-registeret |
| SSB | Strukturerte opplysninger til statistikk | Lønns-, sysselsettings- og sykefraværsstatistikk | Viktig databruker |
| Andre offentlige og private aktører med hjemmel | Gjenbruk av opplysninger | Lån, pensjon, bolig og andre tjenester | Sekundær brukergruppe via videre deling |

## Hovedfunksjoner
### Primære funksjoner
**Samordnet digital rapportering fra arbeidsgivere.** A-ordningen samler flere tidligere rapporteringsløp i én a-melding og gjør det mulig å sende opplysninger elektronisk gjennom lønns- og personalsystemer eller via Altinn. Dette er produktets mest synlige funksjon.

**Felles datagrunnlag for flere etater.** Opplysningene som rapporteres inn brukes samtidig av Skatteetaten, NAV og SSB. Produktet er derfor ikke bare en rapporteringskanal, men en samordnet datainfrastruktur for flere offentlige formål.

**Viderebruk av opplysninger til andre aktører.** Skatteetaten beskriver at opplysningene også distribueres videre til private og offentlige virksomheter som kan motta dem med hjemmel eller samtykke. Dette gjør ordningen til en viktig kilde for videre datadeling.

**Grunnlag for oppdatering av arbeidsforholdsdata.** Opplysninger om arbeidsforhold legges inn i Arbeidsgiver- og arbeidstakerregisteret (Aa-registeret), som igjen brukes av flere offentlige aktører. Ordningen spiller derfor en sentral rolle i vedlikehold av viktige arbeidslivsdata.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Samordnet rapportering gjennom a-meldingen | Alle interne prosesser hos arbeidsgiver før innsending |
| Felles datagrunnlag for Skatteetaten, NAV og SSB | Full saksbehandling i etatene som bruker opplysningene |
| Viderebruk av opplysninger der hjemmel eller samtykke finnes | Alle avledede tjenester som bygger videre på dataene |
| Samforvaltning og koordinering mellom flere offentlige etater | Generell HR- eller lønnsfunksjonalitet i private systemer |
| Grunnlag for oppdatering av Aa-registeret | Hele Aa-registeret som eget produktområde |

## Veikart over kommende funksjonalitet
**Fakta fra kildene (kontrollert 2026-03-27):**
- Skatteetaten publiserer løpende nyheter og informasjonsmøter for A-ordningen.
- Skatteetaten varslet informasjonsmøte 12. mars 2026 med blant annet overgang til Altinn 3 som tema.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et samlet, datert veikart for hele A-ordningen er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til å handle om løpende regelverksendringer, systemstøtte og modernisering av rapporteringsflaten rundt Altinn 3.

## Forretningsverdi/Verdiforslag
### For arbeidsgivere
- Reduserer rapporteringsbyrde ved at flere innrapporteringer samles i én ordning.
- Gjør månedlig rapportering mer automatiserbar gjennom fagsystemer.

### For offentlig sektor
- Gir et oppdatert og samordnet grunnlag for skatt, ytelser, statistikk og kontroll.
- Reduserer duplisering mellom etater som ellers måtte innhentet lignende opplysninger hver for seg.

### For andre databrukere
- Gjør det mulig å gjenbruke kvalitetssikrede opplysninger når lovgrunnlaget er til stede.
- Skaper bedre forutsetninger for raskere og mer presise tjenester.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Feilrapportering fra arbeidsgivere kan forplante seg til mange brukere av opplysningene | Validering, veiledning og korreksjonsløp |
| Samforvaltning | Uklare prioriteringer mellom flere etater kan gjøre endringer tyngre | Tydelig felles styring og koordinering |
| Teknisk | Feil i innsending eller integrasjon kan ramme store volum samtidig | Stabil drift, god varsling og tett dialog med systemleverandører |
| Juridisk | Viderebruk av opplysninger må følge hjemmel, samtykke og klare formålsgrenser | Streng tilgangsstyring og tydelig regelverk |
| Samfunnsavhengighet | Mange tjenester og beslutninger er avhengige av opplysninger fra ordningen | Høy prioritet på robusthet og forvaltning |

## Kanaler
- Om a-ordningen: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/om-a-ordningen/om-a-ordningen/
- Kontakt a-ordningen: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/om-a-ordningen/kontakt-a-ordningen/
- A-ordningen informasjonsmøte 12. mars 2026: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/a-ordningen---informasjonsmote-12.-mars/

## Plattform
A-ordningen er en samordnet rapporterings- og datadelingsordning som fungerer på tvers av flere offentlige virksomheter.

**Fakta:** Ordningen er digital, forvaltes av Skatteetaten på vegne av NAV og SSB, og brukes hovedsakelig gjennom lønns- og personalsystemer samt Altinn.

**Ikke offentlig dokumentert i brukte kilder:** Full intern arkitektur, detaljert ansvarsdeling i alle tekniske komponenter og samlet plattformkart.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er bygget for å samle inn opplysninger én gang og bruke dem flere steder.
- Det er særlig relevant når behovet er samordnet rapportering og videre bruk av inntekts- og arbeidsforholdsdata.
- Det er mindre relevant som isolert sluttbrukertjeneste, siden hovedverdien ligger i datagrunnlaget og samordningen mellom aktører.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at rapporterte opplysninger brukes videre av flere etater og andre aktører.
- **P5: Del og gjenbruk løsninger** styrkes ved at flere rapporteringsløp er samlet i én felles ordning.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi ordningen knytter arbeidsgivere, systemleverandører og flere offentlige etater sammen i én digital flyt.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi mange beslutninger og tjenester er avhengige av at opplysningene er korrekte og sporbare.

## Finansiering
- **Fakta:** Kildene beskriver ikke en samlet offentlig finansieringsmodell for ordningen i denne arbeidsøkten.
- **Deduksjon:** A-ordningen finansieres som en samforvaltet offentlig ordning, kombinert med kostnader hos arbeidsgivere og systemleverandører knyttet til rapporteringsstøtte og integrasjon.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Flere virksomheter: Skatteetaten, NAV og SSB | Ordningen beskrives som samordnet mellom disse |
| Operativ forvaltning | Skatteetaten på vegne av NAV og SSB | Skatteetatens produktside |
| Drifts- og kanalansvar | Skatteetaten, i samspill med Altinn og systemleverandørmiljøene | Produktsiden og kontaktflaten |
| Styringsmodell | Samforvaltet ordning med Skatteetaten som synlig operativ forvalter | Om-siden for A-ordningen |

## Lenke til dokumentasjon
- https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/om-a-ordningen/om-a-ordningen/
- https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/om-a-ordningen/kontakt-a-ordningen/
- https://www.a-ordningen.no/
- https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/a-ordningen---informasjonsmote-12.-mars/

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/om-a-ordningen/om-a-ordningen/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/om-a-ordningen/kontakt-a-ordningen/ (kontrollert 2026-03-27)
- Nettkilde: https://www.a-ordningen.no/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/a-ordningen---informasjonsmote-12.-mars/ (kontrollert 2026-03-27)
