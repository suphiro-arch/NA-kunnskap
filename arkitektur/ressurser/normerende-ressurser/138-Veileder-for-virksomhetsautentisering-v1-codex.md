# Veileder for virksomhetsautentisering

## Ressurs ID
DIGDIR-061

## Ressurskategori
Normerende ressurs

## Type normerende ressurs
Veileder

## Status/Livsfase
Aktiv. Ressursen publiseres som veiledning fra Digdir og brukes som støtte i arbeid med sikker identifisering av mottakere ved datadeling.

## Kort beskrivelse
Veileder for virksomhetsautentisering er en normerende ressurs som beskriver hvordan virksomheter kan identifisere og adressere rett mottaker når data skal deles på tvers av virksomheter og sektorer.

Ressursen er særlig viktig der virksomhetssertifikat alene ikke gir tilstrekkelig presisjon, for eksempel når samhandlingen må avgrenses til en bestemt del av en virksomhet eller til mottakere som ikke kan registreres i Enhetsregisteret. Veilederen gir dermed et felles språk og en praktisk vurderingsramme for å gjøre datadeling tryggere og mer forutsigbar.

## Formål og normerende rolle
Formålet er å bidra til gode og forutsigbare prosesser for identifisering, adressering, sertifikatbehandling, logging, sporing og autentisering ved deling av data.

Ressursen er normerende som veileder. Den er ikke juridisk bindende, men den gir anbefalt praksis for hvordan virksomheter bør arbeide når de må være sikre på at opplysninger går til riktig mottaker. Den har også en tydelig grenseflate mot juridiske vurderinger, fordi presis autentisering må ses i sammenheng med behandlingsgrunnlag, taushetsplikt og mottakeransvar.

## Forpliktelsesnivå og etterlevelse
Veilederen er veiledende, ikke bindende. Likevel har den høy praktisk relevans fordi den beskriver anbefalt fremgangsmåte i situasjoner der feil identifisering eller adressering kan gi sikkerhets- og personvernkonsekvenser.

Etterlevelse skjer normalt gjennom arkitekturarbeid, design av datadelingstjenester, tilgangsmodeller, sikkerhetsvurderinger og praktisk forvaltning av sertifikater og mottakerinformasjon. Kildene tilsier også at veilederen bør brukes sammen med juridiske vurderinger, ikke som erstatning for dem.

## Kapabiliteter
- Tillit: Autentisering
- Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling
- Veiledning

Veilederen støtter `Tillit: Autentisering` ved å beskrive hvordan mottakerens identitet kan fastslås mer presist enn på virksomhetsnivå alene. Den støtter `Informasjonssikkerhet: Sikring av informasjonsflyt og datautveksling` ved å knytte identifisering, adressering, sertifikatbehandling, logging og sporing til trygg praktisk gjennomføring av datadeling.

## Målgruppe og brukere
| Brukersegment | Primært behov | Bruksområde | Kommentar |
|---|---|---|---|
| Datatilbydere | Sikker identifisering av mottaker | Deling av data til andre virksomheter | Viktig når feil mottaker kan gi alvorlige konsekvenser |
| Arkitekter og integrasjonsmiljøer | Felles vurderingsramme for identitet og adressering | Design av delings- og integrasjonsløsninger | Relevans i tidligfase og detaljutforming |
| Sikkerhets- og personvernmiljøer | Bedre sammenheng mellom sikkerhetstiltak og rettslige rammer | Risiko- og personvernvurderinger | Må brukes sammen med juridisk grunnlag |
| Virksomheter som mottar data | Tydeligere krav til intern håndtering og tilgangsstyring | Mottak og videre behandling av opplysninger | Særlig viktig ved underenheter og følsomme opplysninger |
| Digdir og samordningsmiljøer | Felles praksis for virksomhetsautentisering | Veiledning og modenhetsbygging | Binder sammen datadeling og tillitsarbeid |

## Normerende innhold
Veilederen strukturerer virksomhetsautentisering i flere temaer:

- identifisering av mottaker
- adressering til rett enhet eller underenhet
- sertifikatbehandling, logging og sporing
- autentisering som kontrollmekanisme i datadeling
- sammenheng mellom tekniske tiltak og juridiske rammer

Det normerende innholdet ligger i at veilederen beskriver hva som er god praksis når standard virksomhetsidentifikasjon ikke er nok. Den gjør det også tydelig at autentisering og autorisering ikke er det samme: veilederen handler om å være sikker på hvem mottakeren er, mens mottakerens rett til å behandle opplysningene må vurderes særskilt.

## Bruksområde
Veilederen bør brukes når virksomheter skal designe eller vurdere datadeling der det er viktig å identifisere rett mottaker presist, særlig når dataene er rettslig regulerte eller når mottakeren ikke enkelt kan identifiseres gjennom ordinære virksomhetssertifikater.

Den er særlig relevant i løsninger for datadeling på tvers av sektorer, ved behov for underenhetsnivå i mottakerbildet, og når sikkerhets- og juridiske vurderinger må henge tett sammen.

## Typiske analyse- og beslutningssituasjoner
- når en datatilbyder må vite hvilken del av en virksomhet som faktisk er mottaker
- når mottaker ikke kan registreres i Enhetsregisteret og standard virksomhetsidentifikasjon ikke er tilstrekkelig
- når rettslig regulerte opplysninger deles og feil mottaker vil gi betydelig risiko
- når autentisering og autorisering må skilles tydelig i løsningsdesign og styring
- når virksomheter vurderer om høyere presisjonsnivå på autentisering er et egnet sikkerhetstiltak

## Når ressursen normalt ikke er tilstrekkelig alene
Veilederen er ikke tilstrekkelig alene for å etablere en komplett delingsløsning. Den må suppleres med juridisk vurdering, tilgangsstyring, operative tillitstjenester og konkrete tekniske løsninger.

Den er heller ikke en erstatning for Maskinporten, virksomhetssertifikater eller andre operative autentiseringsmekanismer. Den beskriver hvordan slike mekanismer bør vurderes og brukes, ikke hvordan de alene realiserer hele behovet.

## Scope og avgrensning
Inngår:
- veiledning om identifisering og adressering av mottaker
- vurdering av presisjonsnivå ved virksomhetsautentisering
- praktiske temaer som sertifikatbehandling, logging og sporing
- sammenheng mellom autentisering, sikkerhet og juridiske rammer

Inngår ikke:
- juridisk bindende regulering
- full vurdering av autorisering hos mottakeren
- detaljert spesifikasjon av en nasjonal teknisk løsning
- erstatning for operative tillitstjenester som Maskinporten

## Forvaltningsmodell
| Ansvarsområde | Beskrivelse |
|---|---|
| Faglig ansvar | Digitaliseringsdirektoratet |
| Forvaltningsansvar | Digdir publiserer og vedlikeholder veilederen som del av sitt arbeid med datadeling og digital identitet |
| Endringsprosess | Oppdateres ved behov når praksis, regelverk eller veiledningsbehov endrer seg |
| Publiserings- og beslutningsarena | Digdir.no |

## Relasjon til andre ressurser
- **Maskinporten**  
  Maskinporten er en operativ tillitstjeneste for maskin-til-maskin-autentisering, mens denne veilederen beskriver hvordan virksomheter bør tenke om identifisering og adressering av mottakere.

- **Nasjonal verktøykasse for deling av data**  
  Veilederen inngår i et bredere sett av ressurser for trygg og forutsigbar datadeling.

- **Juridiske vurderinger relevante for virksomhetsautentisering**  
  Utfyller veilederen med mer eksplisitte vurderinger av behandlingsgrunnlag, taushetsplikt, mottakeransvar og skillet mellom autentisering og autorisering.

- **Veileder for identifikasjon og sporbarhet i elektronisk kommunikasjon med og i offentlig sektor**  
  Ligger nær denne ressursen tematisk, men har et bredere sikkerhets- og risikoperspektiv enn veilederen for virksomhetsautentisering alene.

## Forretningsverdi og arkitekturverdi
Forretningsverdien ligger i tryggere og mer forutsigbar datadeling, særlig når samhandlingen er kompleks eller krever presis identifisering av mottaker. Veilederen kan redusere risiko for feil deling, misforståelser om ansvar og kostbar omarbeiding senere i løpene.

Arkitekturverdien ligger i at ressursen tydeliggjør skillet mellom identitet, adressering, autentisering og autorisering. Den gjør det lettere å velge riktige mekanismer og å koble juridiske og sikkerhetsmessige vurderinger til løsningsdesign.

## Konsekvens ved manglende bruk eller avvik
Hvis veilederen ikke brukes når presis mottakeridentifikasjon er viktig, øker risikoen for at data går til feil virksomhet eller feil enhet hos mottakeren. Dette kan gi sikkerhetsbrudd, personvernkonsekvenser og svakere tillit mellom delingsaktører.

Hvis autentisering og autorisering blandes sammen, kan virksomheter tro at teknisk identifisering alene er nok til å legitimere delingen. Det kan føre til feil designbeslutninger og utilstrekkelig styring av tilgang.

## Utfordringer og risiko
| Kategori | Risiko eller utfordring | Konsekvens | Mulig håndtering |
|---|---|---|---|
| Avgrensning | Veilederen forveksles med selve teknologiløsningen | Feil forventninger til hva ressursen løser | Tydelig skille mellom normerende veiledning og operative tillitstjenester |
| Juridisk forståelse | Teknisk autentisering tolkes som tilstrekkelig rettslig grunnlag | Feil deling og svak etterlevelse | Bruke veilederen sammen med juridiske vurderinger |
| Adopsjon | Veilederen brukes for sent i utviklingsløpet | Høyere risiko og dyrere omarbeiding | Trekke den inn tidlig i design og risikovurdering |
| Modenhet | Ulik modenhet i virksomhetenes håndtering av underenheter og mottakerbilder | Ujevn praksis og svakere samhandling | Styrke felles begrepsbruk og veiledning |

## Publiseringsform og tilgjengelighet
Ressursen publiseres som åpen veileder på digdir.no. Den inngår også i Digdirs bredere oversikt over veiledere og hjelpemidler innen digital identitet.

## Støtter arkitekturprinsipper
- **P6: Lag digitale løsninger som støtter samhandling**  
  Veilederen støtter prinsippet ved å gjøre samhandlingen tryggere og mer presis når data deles mellom virksomheter.

- **P7: Sørg for tillit til oppgaveløsningen**  
  Ressursen styrker tillit ved å tydeliggjøre hvordan mottakerens identitet kan bekreftes og hvordan sikkerhetsmekanismer bør kombineres med logging og sporing.

## Svakheter, spenninger og begrensninger mot prinsippene
Veilederen er avhengig av at virksomhetene faktisk omsetter rådene til operative mekanismer, styring og juridiske vurderinger. Uten dette kan ressursen gi god begrepsforståelse, men begrenset effekt i praksis.

## Lenke til dokumentasjon
- https://www.digdir.no/datadeling/veileder-virksomhetsautentisering/2435
- https://www.digdir.no/datadeling/juridiske-vurderinger-relevante-virksomhetsautentisering/2488
- https://www.digdir.no/digital-identitet/veiledere-og-hjelpemidler/7311

## Kildegrunnlag brukt i utfyllingen
- `sources/links.md`, kontrollert 2026-05-05
- https://www.digdir.no/datadeling/veileder-virksomhetsautentisering/2435, kontrollert 2026-05-05
- https://www.digdir.no/datadeling/juridiske-vurderinger-relevante-virksomhetsautentisering/2488, kontrollert 2026-05-05
- https://www.digdir.no/digital-identitet/veiledere-og-hjelpemidler/7311, kontrollert 2026-05-05
- `arkitektur/prinsipper/principles.md`, kontrollert 2026-05-05
