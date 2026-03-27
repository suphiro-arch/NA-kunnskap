# Produkt-canvas: API-katalog

## Navn
API-katalog

## Ressurs ID
DIGDIR-013

## Status/Livsfase
**Produksjon** - etablert nasjonal delkatalog for publisering, søk og gjenfinning av API-beskrivelser i offentlig sektor.

**Fakta:** data.norge.no beskriver API-katalogen som del av Felles datakatalog og forklarer at den gir tilgang til maskinlesbare opplysninger om adressene som iverksetter et spesifikt API. Katalogen viser blant annet beskrivelse av API-et, formater, informasjon om bruk, kontaktinformasjon til eier og relasjon til datasett og informasjonsmodeller.

## Modenhet
**Høy modenhet** - tydelig avgrenset og operativ delkatalog:
- Produktet er i bruk som nasjonal oversikt over publiserte API-beskrivelser.
- Det finnes både synlig katalogflate og teknisk dokumentasjon for data.norge.no-området.
- API-katalogen er en del av Felles datakatalog, men har en tydelig egen rolle som delkatalog for datatjenester og grensesnitt.
- Innholdet bygger på standardisert metadataforvaltning, ikke bare lenkesamling til teknisk dokumentasjon.

**Deduksjon:** Modenheten er høy fordi produktet har en klar funksjon i oppdagelse og gjenbruk av API-er, men verdien er avhengig av at virksomhetene publiserer tilstrekkelig gode og oppdaterte API-beskrivelser.

## Kort beskrivelse
API-katalog er den nasjonale delkatalogen for å beskrive og synliggjøre API-er i offentlig sektor. Produktet gjør det mulig å publisere standardiserte beskrivelser av datatjenester, søke i dem og se hvordan API-er henger sammen med datasett og informasjonsmodeller. Løsningen er en del av Felles datakatalog, men skiller seg fra den overordnede katalogen ved å være spesialisert på maskinelle grensesnitt og datatjenester, ikke på hele bredden av dataressurser.

## Kapabiliteter
- **Informasjonsforvaltning: Informasjonsarkitektur** gjør API-er synlige som del av en større struktur av dataressurser, modeller og sammenhenger.
- **Informasjonsforvaltning: Oversikt over API** er produktets kjernefunksjon ved at API-beskrivelser kan publiseres, søkes opp og vurderes.
- **Standardisering: Forvaltningsstandarder** bygger på standardisert beskrivelse av datatjenester og gjør API-metadata mer sammenlignbare og gjenbrukbare.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot API-katalogen på data.norge.no, teknisk dokumentasjon og Digdirs sider om Felles datakatalog.

## Produktmål
**Primærkilder:** API-katalogen på data.norge.no, data.norge.no `About` og teknisk dokumentasjon for data.norge.no.

Dokumenterte mål:
- Sikre enkel tilgang til distribuerte data gjennom en nasjonal API-katalog.
- Gjøre det mulig å hente ut maskinlesbare opplysninger om adressene som iverksetter et spesifikt API.
- Gi oversikt over beskrivelser av grensesnittene til data og standarder som virksomheter har gjort tilgjengelige.

Operative mål utledet fra de samme kildene:
- Gjøre det enklere å finne relevante API-er før nye integrasjoner bygges.
- Koble API-beskrivelser til datasett og informasjonsmodeller slik at datatjenester blir lettere å forstå.
- Styrke gjenbruk av eksisterende API-er gjennom bedre synlighet og mer standardisert dokumentasjon.

## Brukerbehov
- API-forvaltere trenger en felles måte å publisere beskrivelser av egne datatjenester på.
- Utviklere og integrasjonsteam trenger ett sted å finne og vurdere relevante API-er.
- Arkitekter og informasjonsforvaltere trenger oversikt over hvilke grensesnitt som finnes og hvordan de henger sammen med andre dataressurser.
- Datakonsumenter trenger å forstå hva et API gir tilgang til, hvordan det brukes og hvem som eier det.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| API-forvaltere i virksomheter | Publisere og vedlikeholde API-beskrivelser | Synliggjøring av datatjenester | Primærbruker på publiseringssiden |
| Utviklere og integrasjonsteam | Finne og vurdere relevante API-er | Integrasjon, tjenesteutvikling og analyse | Møter ofte produktet via data.norge.no |
| Arkitekter og informasjonsforvaltere | Se sammenheng mellom API-er, datasett og modeller | Kartlegging, gjenbruk og styring | Viktig for helhetsforståelse |
| Datakonsumenter i offentlig og privat sektor | Forstå bruk, kontaktpunkt og tilknyttede datasett | Viderebruk av data og tjenester | Trenger mer enn bare lenke til Swagger |
| Digdir og forvaltningsmiljøer | Forvalte standard, katalogområde og videreutvikling | Drift, dokumentasjon og produktutvikling | Bærer produktansvaret |

## Hovedfunksjoner
### Primære funksjoner
**Publisering av API-beskrivelser.** Produktet gjør det mulig å beskrive API-er som dataressurser i en felles katalog. Det er viktig fordi API-katalogen ikke er en gateway eller kjøretidsplattform, men en nasjonal løsning for å gjøre API-er oppdagbare og forståelige.

**Søk og oppdagelse av API-er.** API-katalogen gir en egen inngang for å finne publiserte API-er og se sentrale metadata om dem. Dette hjelper brukere som trenger å vite hvilke datatjenester som finnes før de etablerer nye integrasjoner eller utvikler parallelle løsninger.

**Kobling til datasett og informasjonsmodeller.** data.norge.no beskriver at API-er kan kobles til ett eller flere datasett, og at informasjonsmodell kan være oppgitt i API-beskrivelsen. Produktet gir dermed mer enn bare teknisk oppslag; det bidrar til å plassere API-et i en større informasjonskontekst.

**Standardisert metadata om datatjenester.** API-katalogen bygger på standardiserte beskrivelser av datatjenester i Felles datakatalog. Det gjør innholdet mer sammenlignbart og gjenbrukbart, og gjør det enklere å bruke API-beskrivelser som del av nasjonal informasjonsforvaltning.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Publisering og søk i API-beskrivelser | Kjøretidsstyring, gateway og trafikkontroll for API-er |
| Synliggjøring av datatjenester og tilknyttede metadata | Selve implementasjonen av API-et hos virksomheten |
| Kobling mellom API-er, datasett og informasjonsmodeller | Autorisasjon, autentisering eller tilgangskontroll i API-et |
| Delkatalog for API-er innenfor Felles datakatalog | Hele Felles datakatalog som overordnet produktområde |
| Standardisert beskrivelse av API-er som dataressurser | Full utviklerportal med testmiljø, supportløp og driftsovervåking |

## Veikart over kommende funksjonalitet
**Fakta fra brukte kilder (kontrollert 2026-03-27):**
- Produktet inngår i et bredere katalogområde på data.norge.no med teknisk dokumentasjon og flere relaterte delkataloger.
- API-katalogen beskrives eksplisitt i sammenheng med datasett og informasjonsmodeller.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et detaljert og tidsfestet veikart for API-katalogen er ikke hentet ut.

**Deduksjon:** Videreutviklingen vil trolig dreie seg om bedre sammenheng mellom API-beskrivelser og øvrige dataressurser, samt bedre kvalitet og publiseringsgrad i metadataene.

## Forretningsverdi/Verdiforslag
### For virksomheter
- Gjør det enklere å synliggjøre egne API-er i en nasjonal katalog.
- Reduserer behovet for at hver virksomhet bygger separate oversikter som er vanskelige å finne.
- Styrker gjenbruk av eksisterende datatjenester fremfor ny utvikling av parallelle grensesnitt.

### For utviklings- og integrasjonsmiljøer
- Gir raskere oversikt over hvilke API-er som finnes og hva de brukes til.
- Gjør det enklere å forstå forholdet mellom API-er og tilknyttede datasett eller modeller.
- Reduserer letetid og usikkerhet når nye behov skal løses.

### For offentlig sektor
- Understøtter mer sammenhengende datadeling gjennom bedre synlighet av eksisterende datatjenester.
- Bidrar til mer standardisert og sammenlignbar beskrivelse av API-er.
- Styrker informasjonsforvaltningen ved å knytte tekniske grensesnitt til resten av dataøkosystemet.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | API-beskrivelser kan være ufullstendige eller utdaterte | Publiseringsrutiner, veiledning og bedre oppfølging av metadata |
| Organisatorisk | Lav publiseringsgrad gir ufullstendig oversikt over tilgjengelige API-er | Forankring, innføringsstøtte og tydelig nytte for virksomhetene |
| Avgrensning | Brukere kan tro at katalogen også leverer runtime-funksjoner eller selve API-et | Klare beskrivelser av rollen som delkatalog og metadataressurs |
| Informasjonsarkitektur | Svake koblinger til datasett og modeller reduserer forståelsen av hva API-et faktisk representerer | Bedre bruk av relasjoner i katalogene |
| Brukeropplevelse | Katalogen kan oppleves som for teknisk eller for tynn hvis metadataene bare peker videre | Tydeligere beskrivelser og bedre kvalitet i publiserte oppføringer |

## Kanaler
- API-katalogen: https://data.norge.no/catalogs/data-services
- data.norge.no, om løsningen: https://data.norge.no/about
- data.norge.no, teknisk dokumentasjon for API: https://data.norge.no/nb/technical/api
- Digdir, Felles datakatalog: https://www.digdir.no/felleslosninger/felles-datakatalog/790
- Samarbeidsportalen, Felles datakatalog: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616

## Plattform
API-katalog er en spesialisert delkatalog for publisering og oppdagelse av API-beskrivelser, med brukerflate på data.norge.no og plass i den samlede katalogarkitekturen til Felles datakatalog.

**Fakta:** data.norge.no beskriver både brukerflate for API-katalogen og teknisk dokumentasjon for data.norge.no-området. Produktet er rettet mot API-beskrivelser som metadata, ikke mot kjøretid eller styring av API-trafikk.

**Ikke offentlig dokumentert i brukte kilder:** Full intern teknisk arkitektur og detaljert plattformoppsett for akkurat denne delkatalogen.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet kan brukes av mange virksomheter som felles oversikt over publiserte API-er.
- Det er særlig relevant når behovet er å finne og forstå eksisterende API-er, ikke å drifte eller sikre dem.
- Verdien øker når API-beskrivelser kobles til øvrige dataressurser i Felles datakatalog.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** støttes ved at API-er synliggjøres som kanal for gjenbruk av data.
- **P5: Del og gjenbruk løsninger** styrkes ved at flere virksomheter kan bruke samme nasjonale katalog for API-beskrivelser.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi API-katalogen gjør samhandlingsgrensesnitt synlige og lettere å finne.
- **P7: Sørg for tillit til oppgaveløsningen** støttes indirekte gjennom mer standardisert og tydelig beskrivelse av API-er, men produktet er ikke selv en tillitstjeneste.

## Finansiering
- **Fakta:** Offentlig detaljert finansieringsmodell for API-katalog som egen delkatalog er ikke verifisert i denne arbeidsøkten.
- **Fakta:** Produktet framstår som del av Digdirs forvaltning av Felles datakatalog og data.norge.no.
- **Deduksjon:** Finansieringen er trolig samlet under Digdirs produktområde for Felles datakatalog, mens virksomhetene dekker egne kostnader ved å etablere og vedlikeholde gode API-beskrivelser.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Digitaliseringsdirektoratet (Digdir) | data.norge.no og Digdir |
| Drifts- og forvaltningsansvar | Digdir forvalter katalogområdet og nettstedet | data.norge.no og Digdir |
| Budsjett- og kostnadsmodell | Ikke offentlig spesifisert som egen delkatalog i brukte kilder | Ingen detaljert offentlig modell verifisert |
| Styringsmodell | Del av Felles datakatalog og Digdirs arbeid med informasjonsforvaltning | Digdir og data.norge.no |

## Lenke til dokumentasjon
- https://data.norge.no/catalogs/data-services
- https://data.norge.no/about
- https://data.norge.no/nb/technical/api
- https://www.digdir.no/felleslosninger/felles-datakatalog/790
- https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `arkitektur/produkter/produktbeskrivelser/15-API-katalog-produkt-canvas-v2-copilot.md`
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://data.norge.no/catalogs/data-services (kontrollert 2026-03-27)
- Nettkilde: https://data.norge.no/about (kontrollert 2026-03-27)
- Nettkilde: https://data.norge.no/nb/technical/api (kontrollert 2026-03-27)
- Nettkilde: https://www.digdir.no/felleslosninger/felles-datakatalog/790 (kontrollert 2026-03-27)
- Nettkilde: https://samarbeid.digdir.no/felles-datakatalog/dette-er-felles-datakatalog/1616 (kontrollert 2026-03-27)

---

## Endringer fra forrige versjon

### Analyseforbedringer
- Beskrivelsen bygger nå på oppdatert kildekontroll i API-katalogen på data.norge.no og teknisk dokumentasjon, ikke på spekulative antakelser om OpenAPI-flyt, kostnader og runtime-styring.
- Produktet er tydelig avgrenset som delkatalog for API-beskrivelser, ikke som API-gateway, utviklerportal eller generell integrasjonsplattform.
- Uverifiserte påstander om bruksstatistikk, gevinstanslag og detaljert veikart er tatt ut.

### Tekstlige forbedringer
- Dokumentet starter ikke lenger med målgruppelinje, og språket er strammet inn mot faktisk produktrolle og gjenbruksvurdering.
- `Hovedfunksjoner` forklarer nå både publisering, søk, relasjoner og standardisert metadataforvaltning.
- Scope og avgrensning gjør skillet tydeligere mot Felles datakatalog, data.norge.no og selve API-implementasjonene hos virksomhetene.
