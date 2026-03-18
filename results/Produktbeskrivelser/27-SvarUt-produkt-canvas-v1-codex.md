# Produkt-canvas: SvarUt

## Navn
SvarUt

## Ressurs ID
KS-003

## Status/Livsfase
**Produksjon** - etablert sentralisert utsendingstjeneste for kommuner og andre offentlige virksomheter.

**Fakta:** KS beskriver SvarUt som en sentralisert løsning som formidler dokumenter mellom avsender og mottaker via ulike kanaler, inkludert Altinn, SvarInn, Digipost, e-Boks og brevpost.

## Modenhet
**Høy funksjonell modenhet** - tjenesten har et tydelig og avgrenset formål, kjent kanalmodell og bruk i offentlig sektor.
- Produktet er smalere og tydeligere avgrenset enn FIKS Melding, noe som øker forutsigbarheten i bruk.
- Løsningen er modent nok til å beskrives som en etablert distribusjonstjeneste, men den er fortsatt avhengig av hvordan lokale systemer og mottakerkanaler er satt opp.

**Deduksjon:** SvarUt har høy modenhet som utsendingstjeneste, men ikke som full kommunikasjonsplattform for alle dialogbehov.

## Kort beskrivelse
SvarUt er KS Digitals sentraliserte løsning for å sende dokumenter fra offentlige virksomheter til riktig mottakerkanal. Tjenesten gjør det mulig å formidle utgående post videre til blant annet Altinn, SvarInn, Digipost, e-Boks eller fysisk brev, uten at avsender må bygge separate distribusjonsløp mot hver kanal. Produktet er særlig relevant når virksomheten trenger kontrollert dokumentutsending til mange mottakergrupper gjennom én felles distribusjonsmekanisme.

## Kapabiliteter
- **Datautveksling og integrasjon: Meldingsformidling** er kjernefunksjonen fordi produktet distribuerer dokumenter videre til riktige mottakerkanaler.
- **Samarbeid: Organisatorisk samhandling** er relevant fordi samme løsning brukes av kommuner og andre offentlige virksomheter for samordnet dokumentutsending.
- **Sluttbrukertjenester: Sammenhengende tjenester** er relevant fordi mottakeren kan nås gjennom ulike kanaler via ett samlet utsendingsløp, i stedet for å møte ulike løsninger per avsender.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot dokumentert funksjon i KS Digitals kilder brukt i denne arbeidsøkten.

## Produktmål
Dokumenterte mål:
- Formidle dokumenter mellom avsender og mottaker via ulike kanaler.
- Gjøre SvarUt tilgjengelig for kommuner og andre offentlige virksomheter.
- Håndtere utgående post gjennom et sentralisert tjenesteløp.

Operative mål utledet fra kildene:
- Redusere behovet for lokale kanalspesifikke integrasjoner.
- Sørge for at utgående dokumenter kan nå mottaker via passende kanal.
- Gjøre distribusjon av dokumenter mer standardisert og enklere å forvalte.

## Brukerbehov
- Offentlige virksomheter trenger én tjeneste for dokumentutsending til flere kanaler.
- Fagsystemer trenger et standardisert distribusjonsløp for utgående post.
- Virksomheter trenger å nå både digitale og ikke-digitale mottakere uten å bygge alt selv.
- Innbyggere og virksomheter trenger å motta dokumenter i kanaler som allerede brukes i offentlig sektor.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner og offentlige virksomheter | Standardisert utsending av dokumenter | Utgående post og dokumentdistribusjon | Primærbrukere av tjenesten |
| Fagsystemer og leverandører | Integrere utsending mot én sentral tjeneste | Automatisert utsending fra sak- og fagsystemer | Teknisk brukergruppe |
| Innbyggere og virksomheter som mottakere | Motta dokumenter i kjent kanal | Mottak via Digipost, e-Boks, Altinn eller brev | Bruker effekten av tjenesten |
| KS Digital | Forvalte kanaloppsett og tjenesteløp | Produktforvaltning og videreutvikling | Forvalter løsningen |

## Hovedfunksjoner
### Primære funksjoner
- SvarUt tar imot utgående dokumenter fra avsender og sender dem videre til riktig mottakerkanal. Det gjør løsningen relevant når dokumentdistribusjon er viktigere enn bred dialogfunksjonalitet.
- Tjenesten kan formidle dokumenter til flere etablerte kanaler i offentlig sektor, blant annet Altinn, SvarInn, Digipost og e-Boks, eller videre til fysisk brev. Dette gjør at produktet fungerer som et kanalnøytralt distribusjonsledd.
- SvarUt er sentralisert. Det er et viktig skille fra lokale utsendingsrutiner, fordi produktet samler distribusjonslogikken i én fellestjeneste.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Sentralisert utsending av dokumenter | Full dialogplattform for mange kommunikasjonstyper |
| Distribusjon til flere mottakerkanaler | Lokal produksjon av dokumentinnhold |
| Kanalhåndtering for utgående post | Saksbehandling og oppfølging i fagsystemene |
| Felles tjenesteløp for dokumentutsending | Autoritativ datakilde eller register |

## Veikart over kommende funksjonalitet
**Fakta:** Produktsiden viser at løsningen er i bruk og peker videre til teknisk dokumentasjon om hvordan tjenesten fungerer, men jeg fant ikke et offentlig samlet roadmap i kildene brukt i denne arbeidsøkten.

**Deduksjon:** Videreutviklingen vil trolig handle om kanaltilpasning, integrasjonsforbedringer og bedre samspill med øvrige FIKS-tjenester.

## Forretningsverdi/Verdiforslag
### For virksomheter
- Gir én vei ut til flere mottakerkanaler.
- Reduserer behovet for å bygge og forvalte kanalspesifikke utsendingsløsninger.

### For mottakere
- Gir mer konsistent mottak av dokumenter gjennom kjente kanaler.

### For sektoren
- Støtter mer standardisert og skalerbar dokumentutsending i offentlig sektor.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Juridisk | Feil kanal eller feil mottaker kan gi brudd på taushetsplikt eller feil utsending. | Tydelig mottakergrunnlag og kontroll av kanalregler i lokale prosesser. |
| Teknisk | Avhengighet til flere eksterne mottakerkanaler kan gi feil eller forsinkelser i leveransen. | Overvåking, robust kanalhåndtering og god feilhåndtering i avsenderløpet. |
| Sikkerhet | Dokumentutsending kan omfatte sensitivt innhold. | Sikre transportmekanismer og korrekt klassifisering av innhold før utsending. |
| Leverandør | Avsenderne blir avhengige av sentral fellestjeneste for distribusjon. | Forutsigbar forvaltning, teknisk dokumentasjon og tydelige avtaler. |
| Brukeropplevelse | Mottakere kan oppleve ulikhet hvis kanalvalget ikke passer situasjonen. | Bevisst bruk av kanalstrategi og gode lokale rutiner. |

## Kanaler
- https://ksdigital.no/tjenestene/svarut-tjenesten/
- https://status.fiks.ks.no

## Plattform
SvarUt er en sentralt forvaltet utsendingstjeneste som inngår i KS Digitals tjenesteportefølje.

**Fakta:**
- Tjenesten formidler dokumenter mellom avsender og mottaker via flere kanaler.
- Produktet er avgrenset til dokumentdistribusjon og bygger på et sentralisert tjenesteløp.

**Ikke offentlig dokumentert i brukte kilder:** Full driftsmodell, detaljert hostingoppsett og intern teknisk arkitektur.

## Gjenbruk
**Høy gjenbruksverdi:**
- Tjenesten kan brukes av mange offentlige virksomheter med samme distribusjonsbehov.
- Gjenbruksverdien ligger i felles kanalhåndtering og standardisert utsending, ikke i lokal forretningslogikk.

## Støtter arkitekturprinsipper
- **P6 Lag digitale løsninger som støtter samhandling** - SvarUt gjør dokumentutsending på tvers av kanaler og aktører enklere og mer standardisert.
- **P1 Ta utgangspunkt i brukernes behov** - mottakeren kan nås gjennom kanaler som allerede brukes i offentlig sektor, uten at avsender må bygge ulike lokale spesialløsninger.

## Finansiering
**Ikke offentlig detaljert dokumentert i brukte kilder:** Jeg fant ikke full finansieringsmodell for SvarUt i denne arbeidsøkten.

**Deduksjon:** Tjenesten forvaltes som en KS Digital-løsning og er sannsynligvis knyttet til sektorfelles tjenestefinansiering og avtaler, men dette må bekreftes i egne pris- og avtaledokumenter.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | KS Digital | Produktene presenteres og forvaltes av KS Digital. |
| Driftsansvar | Ikke offentlig spesifisert i brukte kilder | Må verifiseres i teknisk dokumentasjon eller driftskilder. |
| Budsjettansvar | Ikke offentlig detaljert dokumentert i brukte kilder | Krever egne pris- eller styringskilder. |
| Styringsmodell | KS Digital som sentral forvalter av fellestjenesten | Fremgår av produktsiden og tjenesteplasseringen i porteføljen. |

## Lenke til dokumentasjon
- https://ksdigital.no/tjenestene/svarut-tjenesten/
- https://status.fiks.ks.no

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://ksdigital.no/tjenestene/svarut-tjenesten/ (hentet 2026-03-18)
