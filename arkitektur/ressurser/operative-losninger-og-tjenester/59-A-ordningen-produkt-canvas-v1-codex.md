# Produkt-canvas: A-ordningen

## Navn
A-ordningen

## Ressurs ID
FLERE-001

## Status/Livsfase
**Produksjon** - etablert samordnet nasjonal rapporteringsordning for inntekts- og arbeidsforholdsopplysninger.

**Fakta:** Skatteetaten beskriver A-ordningen som en samordnet mÃ¥te for arbeidsgivere Ã¥ rapportere opplysninger om inntekt og ansatte til NAV, SSB og Skatteetaten. Ordningen er digital og forvaltes av Skatteetaten pÃ¥ vegne av de andre etatene.

## Modenhet
**HÃ¸y modenhet** - innarbeidet, storstilt og samfunnskritisk ordning:
- Ordningen har vÃ¦rt i drift siden 1. januar 2015.
- 260 000 arbeidsgivere rapporterer Ã¥rlig opplysninger om 4,6 millioner ansatte og pensjonister.
- Over 99 prosent av opplysningene kommer via lÃ¸nns- og personalsystemer.
- Opplysningene brukes av flere sentrale etater og viderebrukes ogsÃ¥ av andre virksomheter med hjemmel eller samtykke.

**Deduksjon:** Modenheten er svÃ¦rt hÃ¸y fordi A-ordningen er blitt en grunnleggende nasjonal rapporterings- og datadelingsordning for arbeids- og inntektsforhold.

## Kort beskrivelse
A-ordningen er den samordnede nasjonale ordningen for at arbeidsgivere skal rapportere opplysninger om inntekt, arbeidsforhold, forskuddstrekk, utleggstrekk, arbeidsgiveravgift og finansskatt. Produktet erstatter flere tidligere skjema- og rapporteringslÃ¸p med Ã©n digital a-melding, og fungerer samtidig som en felles datakilde for Skatteetaten, NAV, SSB og andre aktÃ¸rer som har lovlig grunnlag for videre bruk. Verdien ligger bÃ¥de i forenklet rapportering og i at opplysningene kan gjenbrukes pÃ¥ tvers av etater og tjenester.

## Kapabiliteter
- **Datakilder: Grunndata** er relevant fordi ordningen produserer og vedlikeholder sentrale opplysninger om arbeidsforhold og inntekt som brukes bredt i offentlig forvaltning.
- **Datautveksling og integrasjon: Dele data med andre** er en kjernefunksjon ved at opplysningene distribueres videre til etater og andre aktÃ¸rer med hjemmel eller samtykke.
- **Samarbeid: Organisatorisk samhandling** er sentralt fordi ordningen forvaltes og brukes i et samspill mellom flere offentlige virksomheter.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Skatteetatens beskrivelse av ordningen, styringsmodellen og viderebruk av opplysningene.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Skatteetatens side `Om a-ordningen` og tilhÃ¸rende informasjon om kontakt og bruk av opplysningene.

Dokumenterte mÃ¥l:
- Forenkle og samordne arbeidsgivers rapportering ved Ã¥ gÃ¥ fra fem skjemaer til Ã©n a-melding.
- Gi NAV, SSB og Skatteetaten tilgang til samme rapporterte opplysninger gjennom Ã©n ordning.
- GjÃ¸re opplysningene tilgjengelige for andre private og offentlige aktÃ¸rer som kan motta dem etter hjemmel eller samtykke.

Operative mÃ¥l utledet fra de samme kildene:
- Redusere rapporteringsbyrde og dobbeltarbeid for arbeidsgivere.
- Skape et mer oppdatert og samordnet datagrunnlag om inntekt og arbeidsforhold.
- UnderstÃ¸tte bedre saksbehandling, statistikk, kontroll og tjenesteutvikling pÃ¥ tvers av sektorer.

## Brukerbehov
- Arbeidsgivere trenger Ã©n samlet og digital rapporteringskanal for lovpÃ¥lagte opplysninger.
- NAV, SSB og Skatteetaten trenger et oppdatert og samordnet datagrunnlag.
- Andre virksomheter med hjemmel trenger viderebrukbare opplysninger om inntekt og arbeidsforhold.
- SystemleverandÃ¸rer trenger tydelige rapporteringskrav og stabil integrasjon mot a-meldingen.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Arbeidsgivere | Enkel og korrekt rapportering | Innsending av a-melding hver mÃ¥ned | PrimÃ¦r rapporterende brukergruppe |
| LÃ¸nns- og HR-systemleverandÃ¸rer | Integrasjon og regelverksnÃ¦r stÃ¸tte | Automatisert innsending fra fagsystemer | Over 99 prosent av volumet gÃ¥r via systemer |
| Skatteetaten | Datagrunnlag for skatt, trekk og avgift | Forvaltning, kontroll og innkreving | Forvalter ordningen pÃ¥ vegne av flere |
| NAV | Opplysninger om arbeidsforhold og inntekt | Saksbehandling og kontroll av ytelser | Tett kobling til Aa-registeret |
| SSB | Strukturerte opplysninger til statistikk | LÃ¸nns-, sysselsettings- og sykefravÃ¦rsstatistikk | Viktig databruker |
| Andre offentlige og private aktÃ¸rer med hjemmel | Gjenbruk av opplysninger | LÃ¥n, pensjon, bolig og andre tjenester | SekundÃ¦r brukergruppe via videre deling |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
**Samordnet digital rapportering fra arbeidsgivere.** A-ordningen samler flere tidligere rapporteringslÃ¸p i Ã©n a-melding og gjÃ¸r det mulig Ã¥ sende opplysninger elektronisk gjennom lÃ¸nns- og personalsystemer eller via Altinn. Dette er produktets mest synlige funksjon.

**Felles datagrunnlag for flere etater.** Opplysningene som rapporteres inn brukes samtidig av Skatteetaten, NAV og SSB. Produktet er derfor ikke bare en rapporteringskanal, men en samordnet datainfrastruktur for flere offentlige formÃ¥l.

**Viderebruk av opplysninger til andre aktÃ¸rer.** Skatteetaten beskriver at opplysningene ogsÃ¥ distribueres videre til private og offentlige virksomheter som kan motta dem med hjemmel eller samtykke. Dette gjÃ¸r ordningen til en viktig kilde for videre datadeling.

**Grunnlag for oppdatering av arbeidsforholdsdata.** Opplysninger om arbeidsforhold legges inn i Arbeidsgiver- og arbeidstakerregisteret (Aa-registeret), som igjen brukes av flere offentlige aktÃ¸rer. Ordningen spiller derfor en sentral rolle i vedlikehold av viktige arbeidslivsdata.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Samordnet rapportering gjennom a-meldingen | Alle interne prosesser hos arbeidsgiver fÃ¸r innsending |
| Felles datagrunnlag for Skatteetaten, NAV og SSB | Full saksbehandling i etatene som bruker opplysningene |
| Viderebruk av opplysninger der hjemmel eller samtykke finnes | Alle avledede tjenester som bygger videre pÃ¥ dataene |
| Samforvaltning og koordinering mellom flere offentlige etater | Generell HR- eller lÃ¸nnsfunksjonalitet i private systemer |
| Grunnlag for oppdatering av Aa-registeret | Hele Aa-registeret som eget produktomrÃ¥de |

## Veikart over kommende funksjonalitet
**Fakta fra kildene (kontrollert 2026-03-27):**
- Skatteetaten publiserer lÃ¸pende nyheter og informasjonsmÃ¸ter for A-ordningen.
- Skatteetaten varslet informasjonsmÃ¸te 12. mars 2026 med blant annet overgang til Altinn 3 som tema.

**Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Et samlet, datert veikart for hele A-ordningen er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til Ã¥ handle om lÃ¸pende regelverksendringer, systemstÃ¸tte og modernisering av rapporteringsflaten rundt Altinn 3.

## Forretningsverdi/Verdiforslag
### For arbeidsgivere
- Reduserer rapporteringsbyrde ved at flere innrapporteringer samles i Ã©n ordning.
- GjÃ¸r mÃ¥nedlig rapportering mer automatiserbar gjennom fagsystemer.

### For offentlig sektor
- Gir et oppdatert og samordnet grunnlag for skatt, ytelser, statistikk og kontroll.
- Reduserer duplisering mellom etater som ellers mÃ¥tte innhentet lignende opplysninger hver for seg.

### For andre databrukere
- GjÃ¸r det mulig Ã¥ gjenbruke kvalitetssikrede opplysninger nÃ¥r lovgrunnlaget er til stede.
- Skaper bedre forutsetninger for raskere og mer presise tjenester.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Datakvalitet | Feilrapportering fra arbeidsgivere kan forplante seg til mange brukere av opplysningene | Validering, veiledning og korreksjonslÃ¸p |
| Samforvaltning | Uklare prioriteringer mellom flere etater kan gjÃ¸re endringer tyngre | Tydelig felles styring og koordinering |
| Teknisk | Feil i innsending eller integrasjon kan ramme store volum samtidig | Stabil drift, god varsling og tett dialog med systemleverandÃ¸rer |
| Juridisk | Viderebruk av opplysninger mÃ¥ fÃ¸lge hjemmel, samtykke og klare formÃ¥lsgrenser | Streng tilgangsstyring og tydelig regelverk |
| Samfunnsavhengighet | Mange tjenester og beslutninger er avhengige av opplysninger fra ordningen | HÃ¸y prioritet pÃ¥ robusthet og forvaltning |

## Kanaler
- Om a-ordningen: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/om-a-ordningen/om-a-ordningen/
- Kontakt a-ordningen: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/om-a-ordningen/kontakt-a-ordningen/
- A-ordningen informasjonsmÃ¸te 12. mars 2026: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/a-ordningen---informasjonsmote-12.-mars/

## Plattform
A-ordningen er en samordnet rapporterings- og datadelingsordning som fungerer pÃ¥ tvers av flere offentlige virksomheter.

**Fakta:** Ordningen er digital, forvaltes av Skatteetaten pÃ¥ vegne av NAV og SSB, og brukes hovedsakelig gjennom lÃ¸nns- og personalsystemer samt Altinn.

**Ikke offentlig dokumentert i brukte kilder:** Full intern arkitektur, detaljert ansvarsdeling i alle tekniske komponenter og samlet plattformkart.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet er bygget for Ã¥ samle inn opplysninger Ã©n gang og bruke dem flere steder.
- Det er sÃ¦rlig relevant nÃ¥r behovet er samordnet rapportering og videre bruk av inntekts- og arbeidsforholdsdata.
- Det er mindre relevant som isolert sluttbrukertjeneste, siden hovedverdien ligger i datagrunnlaget og samordningen mellom aktÃ¸rer.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at rapporterte opplysninger brukes videre av flere etater og andre aktÃ¸rer.
- **P5: Del og gjenbruk lÃ¸sninger** styrkes ved at flere rapporteringslÃ¸p er samlet i Ã©n felles ordning.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** stÃ¸ttes fordi ordningen knytter arbeidsgivere, systemleverandÃ¸rer og flere offentlige etater sammen i Ã©n digital flyt.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** er sentralt fordi mange beslutninger og tjenester er avhengige av at opplysningene er korrekte og sporbare.

## Finansiering
- **Fakta:** Kildene beskriver ikke en samlet offentlig finansieringsmodell for ordningen i denne arbeidsÃ¸kten.
- **Deduksjon:** A-ordningen finansieres som en samforvaltet offentlig ordning, kombinert med kostnader hos arbeidsgivere og systemleverandÃ¸rer knyttet til rapporteringsstÃ¸tte og integrasjon.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Flere virksomheter: Skatteetaten, NAV og SSB | Ordningen beskrives som samordnet mellom disse |
| Operativ forvaltning | Skatteetaten pÃ¥ vegne av NAV og SSB | Skatteetatens produktside |
| Drifts- og kanalansvar | Skatteetaten, i samspill med Altinn og systemleverandÃ¸rmiljÃ¸ene | Produktsiden og kontaktflaten |
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
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/om-a-ordningen/om-a-ordningen/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/om-a-ordningen/kontakt-a-ordningen/ (kontrollert 2026-03-27)
- Nettkilde: https://www.a-ordningen.no/ (kontrollert 2026-03-27)
- Nettkilde: https://www.skatteetaten.no/samarbeidspartnere/sluttbrukersystemer/sbs-nyheter/a-ordningen---informasjonsmote-12.-mars/ (kontrollert 2026-03-27)

