# Produkt-canvas: API-katalog

## Navn
API-katalog

## Ressurs ID
DIGDIR-013

## Status/Livsfase
**Produksjon** - etablert nasjonal delkatalog for publisering, sÃ¸k og gjenfinning av API-beskrivelser i offentlig sektor.

**Fakta:** data.norge.no beskriver API-katalogen som del av Felles datakatalog og forklarer at den gir tilgang til maskinlesbare opplysninger om adressene som iverksetter et spesifikt API. Katalogen viser blant annet beskrivelse av API-et, formater, informasjon om bruk, kontaktinformasjon til eier og relasjon til datasett og informasjonsmodeller.

## Modenhet
**HÃ¸y modenhet** - tydelig avgrenset og operativ delkatalog:
- Produktet er i bruk som nasjonal oversikt over publiserte API-beskrivelser.
- Det finnes bÃ¥de synlig katalogflate og teknisk dokumentasjon for data.norge.no-omrÃ¥det.
- API-katalogen er en del av Felles datakatalog, men har en tydelig egen rolle som delkatalog for datatjenester og grensesnitt.
- Innholdet bygger pÃ¥ standardisert metadataforvaltning, ikke bare lenkesamling til teknisk dokumentasjon.

**Deduksjon:** Modenheten er hÃ¸y fordi produktet har en klar funksjon i oppdagelse og gjenbruk av API-er, men verdien er avhengig av at virksomhetene publiserer tilstrekkelig gode og oppdaterte API-beskrivelser.

## Kort beskrivelse
API-katalog er den nasjonale delkatalogen for Ã¥ beskrive og synliggjÃ¸re API-er i offentlig sektor. Produktet gjÃ¸r det mulig Ã¥ publisere standardiserte beskrivelser av datatjenester, sÃ¸ke i dem og se hvordan API-er henger sammen med datasett og informasjonsmodeller. LÃ¸sningen er en del av Felles datakatalog, men skiller seg fra den overordnede katalogen ved Ã¥ vÃ¦re spesialisert pÃ¥ maskinelle grensesnitt og datatjenester, ikke pÃ¥ hele bredden av dataressurser.

## Kapabiliteter
- **Informasjonsforvaltning: Informasjonsarkitektur** gjÃ¸r API-er synlige som del av en stÃ¸rre struktur av dataressurser, modeller og sammenhenger.
- **Informasjonsforvaltning: Oversikt over API** er produktets kjernefunksjon ved at API-beskrivelser kan publiseres, sÃ¸kes opp og vurderes.
- **Standardisering: Forvaltningsstandarder** bygger pÃ¥ standardisert beskrivelse av datatjenester og gjÃ¸r API-metadata mer sammenlignbare og gjenbrukbare.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot API-katalogen pÃ¥ data.norge.no, teknisk dokumentasjon og Digdirs sider om Felles datakatalog.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** API-katalogen pÃ¥ data.norge.no, data.norge.no `About` og teknisk dokumentasjon for data.norge.no.

Dokumenterte mÃ¥l:
- Sikre enkel tilgang til distribuerte data gjennom en nasjonal API-katalog.
- GjÃ¸re det mulig Ã¥ hente ut maskinlesbare opplysninger om adressene som iverksetter et spesifikt API.
- Gi oversikt over beskrivelser av grensesnittene til data og standarder som virksomheter har gjort tilgjengelige.

Operative mÃ¥l utledet fra de samme kildene:
- GjÃ¸re det enklere Ã¥ finne relevante API-er fÃ¸r nye integrasjoner bygges.
- Koble API-beskrivelser til datasett og informasjonsmodeller slik at datatjenester blir lettere Ã¥ forstÃ¥.
- Styrke gjenbruk av eksisterende API-er gjennom bedre synlighet og mer standardisert dokumentasjon.

## Brukerbehov
- API-forvaltere trenger en felles mÃ¥te Ã¥ publisere beskrivelser av egne datatjenester pÃ¥.
- Utviklere og integrasjonsteam trenger ett sted Ã¥ finne og vurdere relevante API-er.
- Arkitekter og informasjonsforvaltere trenger oversikt over hvilke grensesnitt som finnes og hvordan de henger sammen med andre dataressurser.
- Datakonsumenter trenger Ã¥ forstÃ¥ hva et API gir tilgang til, hvordan det brukes og hvem som eier det.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| API-forvaltere i virksomheter | Publisere og vedlikeholde API-beskrivelser | SynliggjÃ¸ring av datatjenester | PrimÃ¦rbruker pÃ¥ publiseringssiden |
| Utviklere og integrasjonsteam | Finne og vurdere relevante API-er | Integrasjon, tjenesteutvikling og analyse | MÃ¸ter ofte produktet via data.norge.no |
| Arkitekter og informasjonsforvaltere | Se sammenheng mellom API-er, datasett og modeller | Kartlegging, gjenbruk og styring | Viktig for helhetsforstÃ¥else |
| Datakonsumenter i offentlig og privat sektor | ForstÃ¥ bruk, kontaktpunkt og tilknyttede datasett | Viderebruk av data og tjenester | Trenger mer enn bare lenke til Swagger |
| Digdir og forvaltningsmiljÃ¸er | Forvalte standard, katalogomrÃ¥de og videreutvikling | Drift, dokumentasjon og produktutvikling | BÃ¦rer produktansvaret |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
**Publisering av API-beskrivelser.** Produktet gjÃ¸r det mulig Ã¥ beskrive API-er som dataressurser i en felles katalog. Det er viktig fordi API-katalogen ikke er en gateway eller kjÃ¸retidsplattform, men en nasjonal lÃ¸sning for Ã¥ gjÃ¸re API-er oppdagbare og forstÃ¥elige.

**SÃ¸k og oppdagelse av API-er.** API-katalogen gir en egen inngang for Ã¥ finne publiserte API-er og se sentrale metadata om dem. Dette hjelper brukere som trenger Ã¥ vite hvilke datatjenester som finnes fÃ¸r de etablerer nye integrasjoner eller utvikler parallelle lÃ¸sninger.

**Kobling til datasett og informasjonsmodeller.** data.norge.no beskriver at API-er kan kobles til ett eller flere datasett, og at informasjonsmodell kan vÃ¦re oppgitt i API-beskrivelsen. Produktet gir dermed mer enn bare teknisk oppslag; det bidrar til Ã¥ plassere API-et i en stÃ¸rre informasjonskontekst.

**Standardisert metadata om datatjenester.** API-katalogen bygger pÃ¥ standardiserte beskrivelser av datatjenester i Felles datakatalog. Det gjÃ¸r innholdet mer sammenlignbart og gjenbrukbart, og gjÃ¸r det enklere Ã¥ bruke API-beskrivelser som del av nasjonal informasjonsforvaltning.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Publisering og sÃ¸k i API-beskrivelser | KjÃ¸retidsstyring, gateway og trafikkontroll for API-er |
| SynliggjÃ¸ring av datatjenester og tilknyttede metadata | Selve implementasjonen av API-et hos virksomheten |
| Kobling mellom API-er, datasett og informasjonsmodeller | Autorisasjon, autentisering eller tilgangskontroll i API-et |
| Delkatalog for API-er innenfor Felles datakatalog | Hele Felles datakatalog som overordnet produktomrÃ¥de |
| Standardisert beskrivelse av API-er som dataressurser | Full utviklerportal med testmiljÃ¸, supportlÃ¸p og driftsovervÃ¥king |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-27):**
- Produktet inngÃ¥r i et bredere katalogomrÃ¥de pÃ¥ data.norge.no med teknisk dokumentasjon og flere relaterte delkataloger.
- API-katalogen beskrives eksplisitt i sammenheng med datasett og informasjonsmodeller.

**Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Et detaljert og tidsfestet veikart for API-katalogen er ikke hentet ut.

**Deduksjon:** Videreutviklingen vil trolig dreie seg om bedre sammenheng mellom API-beskrivelser og Ã¸vrige dataressurser, samt bedre kvalitet og publiseringsgrad i metadataene.

## Forretningsverdi/Verdiforslag
### For virksomheter
- GjÃ¸r det enklere Ã¥ synliggjÃ¸re egne API-er i en nasjonal katalog.
- Reduserer behovet for at hver virksomhet bygger separate oversikter som er vanskelige Ã¥ finne.
- Styrker gjenbruk av eksisterende datatjenester fremfor ny utvikling av parallelle grensesnitt.

### For utviklings- og integrasjonsmiljÃ¸er
- Gir raskere oversikt over hvilke API-er som finnes og hva de brukes til.
- GjÃ¸r det enklere Ã¥ forstÃ¥ forholdet mellom API-er og tilknyttede datasett eller modeller.
- Reduserer letetid og usikkerhet nÃ¥r nye behov skal lÃ¸ses.

### For offentlig sektor
- UnderstÃ¸tter mer sammenhengende datadeling gjennom bedre synlighet av eksisterende datatjenester.
- Bidrar til mer standardisert og sammenlignbar beskrivelse av API-er.
- Styrker informasjonsforvaltningen ved Ã¥ knytte tekniske grensesnitt til resten av dataÃ¸kosystemet.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Datakvalitet | API-beskrivelser kan vÃ¦re ufullstendige eller utdaterte | Publiseringsrutiner, veiledning og bedre oppfÃ¸lging av metadata |
| Organisatorisk | Lav publiseringsgrad gir ufullstendig oversikt over tilgjengelige API-er | Forankring, innfÃ¸ringsstÃ¸tte og tydelig nytte for virksomhetene |
| Avgrensning | Brukere kan tro at katalogen ogsÃ¥ leverer runtime-funksjoner eller selve API-et | Klare beskrivelser av rollen som delkatalog og metadataressurs |
| Informasjonsarkitektur | Svake koblinger til datasett og modeller reduserer forstÃ¥elsen av hva API-et faktisk representerer | Bedre bruk av relasjoner i katalogene |
| Brukeropplevelse | Katalogen kan oppleves som for teknisk eller for tynn hvis metadataene bare peker videre | Tydeligere beskrivelser og bedre kvalitet i publiserte oppfÃ¸ringer |

## Kanaler
- API-katalogen: https://data.norge.no/catalogs/data-services
- data.norge.no, om lÃ¸sningen: https://data.norge.no/about
- data.norge.no, teknisk dokumentasjon for API: https://data.norge.no/nb/technical/api
- Digdir, Felles datakatalog: https://www.digdir.no/felleslosninger/felles-datakatalog/790
- Samarbeidsportalen, Felles datakatalog: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616

## Plattform
API-katalog er en spesialisert delkatalog for publisering og oppdagelse av API-beskrivelser, med brukerflate pÃ¥ data.norge.no og plass i den samlede katalogarkitekturen til Felles datakatalog.

**Fakta:** data.norge.no beskriver bÃ¥de brukerflate for API-katalogen og teknisk dokumentasjon for data.norge.no-omrÃ¥det. Produktet er rettet mot API-beskrivelser som metadata, ikke mot kjÃ¸retid eller styring av API-trafikk.

**Ikke offentlig dokumentert i brukte kilder:** Full intern teknisk arkitektur og detaljert plattformoppsett for akkurat denne delkatalogen.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet kan brukes av mange virksomheter som felles oversikt over publiserte API-er.
- Det er sÃ¦rlig relevant nÃ¥r behovet er Ã¥ finne og forstÃ¥ eksisterende API-er, ikke Ã¥ drifte eller sikre dem.
- Verdien Ã¸ker nÃ¥r API-beskrivelser kobles til Ã¸vrige dataressurser i Felles datakatalog.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** stÃ¸ttes ved at API-er synliggjÃ¸res som kanal for gjenbruk av data.
- **P5: Del og gjenbruk lÃ¸sninger** styrkes ved at flere virksomheter kan bruke samme nasjonale katalog for API-beskrivelser.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** stÃ¸ttes fordi API-katalogen gjÃ¸r samhandlingsgrensesnitt synlige og lettere Ã¥ finne.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** stÃ¸ttes indirekte gjennom mer standardisert og tydelig beskrivelse av API-er, men produktet er ikke selv en tillitstjeneste.

## Finansiering
- **Fakta:** Offentlig detaljert finansieringsmodell for API-katalog som egen delkatalog er ikke verifisert i denne arbeidsÃ¸kten.
- **Fakta:** Produktet framstÃ¥r som del av Digdirs forvaltning av Felles datakatalog og data.norge.no.
- **Deduksjon:** Finansieringen er trolig samlet under Digdirs produktomrÃ¥de for Felles datakatalog, mens virksomhetene dekker egne kostnader ved Ã¥ etablere og vedlikeholde gode API-beskrivelser.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | data.norge.no og Digdir |
| Drifts- og forvaltningsansvar | Digdir forvalter katalogomrÃ¥det og nettstedet | data.norge.no og Digdir |
| Budsjett- og kostnadsmodell | Ikke offentlig spesifisert som egen delkatalog i brukte kilder | Ingen detaljert offentlig modell verifisert |
| Styringsmodell | Del av Felles datakatalog og Digdirs arbeid med informasjonsforvaltning | Digdir og data.norge.no |

## Lenke til dokumentasjon
- https://data.norge.no/catalogs/data-services
- https://data.norge.no/about
- https://data.norge.no/nb/technical/api
- https://www.digdir.no/felleslosninger/felles-datakatalog/790
- https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/ressurser/operative-losninger-og-tjenester/15-API-katalog-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://data.norge.no/catalogs/data-services (kontrollert 2026-03-27)
- Nettkilde: https://data.norge.no/about (kontrollert 2026-03-27)
- Nettkilde: https://data.norge.no/nb/technical/api (kontrollert 2026-03-27)
- Nettkilde: https://www.digdir.no/felleslosninger/felles-datakatalog/790 (kontrollert 2026-03-27)
- Nettkilde: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616 (kontrollert 2026-03-27)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen bygger nÃ¥ pÃ¥ oppdatert kildekontroll i API-katalogen pÃ¥ data.norge.no og teknisk dokumentasjon, ikke pÃ¥ spekulative antakelser om OpenAPI-flyt, kostnader og runtime-styring.
- Produktet er tydelig avgrenset som delkatalog for API-beskrivelser, ikke som API-gateway, utviklerportal eller generell integrasjonsplattform.
- Uverifiserte pÃ¥stander om bruksstatistikk, gevinstanslag og detaljert veikart er tatt ut.

### Tekstlige forbedringer
- Dokumentet starter ikke lenger med mÃ¥lgruppelinje, og sprÃ¥ket er strammet inn mot faktisk produktrolle og gjenbruksvurdering.
- `Hovedfunksjoner` forklarer nÃ¥ bÃ¥de publisering, sÃ¸k, relasjoner og standardisert metadataforvaltning.
- Scope og avgrensning gjÃ¸r skillet tydeligere mot Felles datakatalog, data.norge.no og selve API-implementasjonene hos virksomhetene.

