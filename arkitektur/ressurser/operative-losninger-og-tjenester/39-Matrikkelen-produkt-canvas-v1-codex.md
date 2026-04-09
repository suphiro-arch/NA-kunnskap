# Produkt-canvas: Matrikkelen

## Navn
Matrikkelen

## Ressurs ID
KART-001

## Status/Livsfase
**Produksjon** - etablert nasjonalt register og felleskomponent for eiendomsopplysninger, bygninger, adresser og grenser.

**Fakta:** Kartverket beskriver Matrikkelen som det offisielle registeret over norske eiendommer. Kartverket omtaler ogsÃ¥ Matrikkelen som en nasjonal felleslÃ¸sning og en av de tre statlige felleskomponentene, sammen med Folkeregisteret og Enhetsregisteret.

## Modenhet
**HÃ¸y modenhet** - innarbeidet og samfunnskritisk grunndataregister:
- Registeret brukes av et bredt spekter av offentlige og private aktÃ¸rer, blant annet kommuner, nÃ¸detater, banker, forsikringsselskaper og Skatteetaten.
- Kartverket forvalter Matrikkelen sentralt, mens kommunene har viktige roller som lokal matrikkelmyndighet og adressemyndighet.
- Produktet har bÃ¥de operative tilgangslÃ¸p, innsynslÃ¸sninger, attestert utskrift og dokumentert rolle- og tilgangsmodell.
- Kartverket arbeider aktivt med datakvalitet, fÃ¸ringsveiledning og samhandling med kommunesektoren.

**Deduksjon:** Modenheten er hÃ¸y bÃ¥de fordi registeret er grunnleggende for mange samfunnsfunksjoner og fordi det har et tydelig forvaltningsregime. Samtidig er verdien avhengig av kvaliteten i fÃ¸ring og oppdatering hos kommunene og andre registrerende aktÃ¸rer.

## Kort beskrivelse
Matrikkelen er det nasjonale grunndataregisteret for eiendommer, bygninger, adresser og offisielle eiendomsidentifikatorer i Norge. Produktet gjÃ¸r det mulig Ã¥ registrere, forvalte og bruke autoritative opplysninger om fast eiendom og tilhÃ¸rende objekter pÃ¥ tvers av sektorer og forvaltningsnivÃ¥er. Matrikkelen er derfor mer enn en innsynstjeneste: den er den sentrale registerlÃ¸sningen som mange andre tjenester og beslutningsprosesser bygger pÃ¥ nÃ¥r de trenger pÃ¥litelig informasjon om eiendom, bygg og adresser.

## Kapabiliteter
- **Datakilder: Grunndata** er kjernefunksjonen ved at Matrikkelen fungerer som autoritativ kilde for sentrale opplysninger om eiendommer, bygninger og adresser.
- **Datautveksling og integrasjon: Dele data med andre** gjÃ¸r opplysninger fra Matrikkelen tilgjengelige for mange andre virksomheter og tjenester som trenger eiendoms- og adressegrunnlag.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Kartverkets beskrivelser av Matrikkelen som offisielt register, nasjonal felleslÃ¸sning og statlig felleskomponent.

## ProduktmÃ¥l
**PrimÃ¦rkilder:** Kartverkets side `Dette er matrikkelen`, tilgangssider for Matrikkelen og veiledningssider om bygninger og adresser i Matrikkelen.

Dokumenterte mÃ¥l:
- VÃ¦re det offisielle registeret over norske eiendommer.
- Gi oversikt over grenser, bygninger, adresser og eierforhold.
- Dekke behov pÃ¥ tvers av mange sektorer og forvaltningsnivÃ¥er.

Operative mÃ¥l utledet fra de samme kildene:
- Gi samfunnet ett felles eiendoms- og adressegrunnlag i stedet for mange lokale eller sektorvise varianter.
- StÃ¸tte bÃ¥de offentlig myndighetsutÃ¸velse og private tjenester som er avhengige av pÃ¥litelige eiendomsopplysninger.
- Legge grunnlag for sammenheng mellom lokal registrering i kommunene og nasjonal tilgjengeliggjÃ¸ring av dataene.

## Brukerbehov
- Kommuner trenger et autoritativt register for Ã¥ fÃ¸re eiendoms-, adresse- og bygningsopplysninger som del av sine myndighetsoppgaver.
- Offentlige virksomheter trenger pÃ¥litelige eiendomsdata for saksbehandling, beredskap, planlegging og samordning.
- Private virksomheter trenger standardiserte og oppdaterte opplysninger om eiendommer og bygninger i egne tjenester.
- Innbyggere trenger innsyn i opplysninger om egne eiendommer og tilgang til dokumentasjon som matrikkelbrev.

## Hvem er brukerne og brukersegmentene
| Brukersegment | PrimÃ¦re behov | BruksomrÃ¥de | Kommentar |
|---|---|---|---|
| Kommuner som lokal matrikkelmyndighet | FÃ¸re og oppdatere opplysninger korrekt | MatrikkelfÃ¸ring, adressering og bygningsoppdatering | Har en sentral rolle i datakvaliteten |
| Offentlige virksomheter | Bruke pÃ¥litelige eiendoms- og adresseopplysninger | Beredskap, saksbehandling, planlegging og forvaltning | Viktig tverrsektoriell brukergruppe |
| Private virksomheter | Tilgang til standardiserte eiendomsdata | Bank, forsikring, bygg, eiendomsmegling og logistikk | Bruker dataene i samfunnskritiske prosesser |
| Innbyggere og eiere | Innsyn og dokumentasjon | Oppslag i egne eiendommer og bestilling av matrikkelbrev | MÃ¸ter produktet via innsynslÃ¸sninger og kommunale prosesser |
| Kartverket og fagmiljÃ¸er | Forvaltning, kvalitet og samordning | Sentral registerforvaltning, veiledning og utvikling | Kartverket er sentral matrikkelmyndighet |

## Hovedfunksjoner
### PrimÃ¦re funksjoner
**Autoritativ registrering av eiendom, bygninger og adresser.** Matrikkelen samler og forvalter nÃ¸kkelopplysninger om eiendommer, bygninger og adresser i ett nasjonalt register. Dette er produktets viktigste funksjon, og det gjÃ¸r lÃ¸sningen relevant nÃ¥r mange sektorer trenger samme grunnlag for identifikasjon og beskrivelse av eiendom.

**Nasjonalt felles adresse- og eiendomsgrunnlag.** Produktet gir et felles system for offisielle adresser og eiendomsidentifikatorer. Det gjÃ¸r Matrikkelen sentral i samfunnsfunksjoner som beredskap, postlevering, byggesak, eiendomsomsetning og offentlig planlegging, der aktÃ¸rene mÃ¥ kunne bruke samme referansegrunnlag.

**TilgjengeliggjÃ¸ring og innsyn i matrikkelopplysninger.** Kartverket beskriver bÃ¥de innsynslÃ¸sninger og matrikkelbrev som del av produktomrÃ¥det. Det betyr at Matrikkelen ikke bare er et internt register for myndigheter, men ogsÃ¥ et grunnlag for innsyn, attestert dokumentasjon og videre bruk av opplysninger i andre tjenester.

**Samspill mellom sentral forvaltning og lokal fÃ¸ring.** Produktet forutsetter et operativt samspill mellom Kartverket som sentral matrikkelmyndighet og kommunene som fÃ¸rer og oppdaterer data. Veiledning, tilgangsroller, kurs og faglige samhandlingsarenaer er derfor en viktig del av hvordan produktet faktisk fungerer i praksis.

### Scope og avgrensning
| InngÃ¥r | InngÃ¥r ikke |
|---|---|
| Offisielt register over eiendommer, bygninger og adresser | Tinglysingsregisteret eller andre rettighetsregistre som egen ressurs |
| Felles identifikatorer og grunndata om eiendom | Full kartportal eller generell geodataplattform |
| Innsyn og dokumentasjon som bygger pÃ¥ matrikkeldata | Lokal saksbehandling utover det som registreres i Matrikkelen |
| Rolle- og tilgangsstyrt bruk for kommuner og andre aktÃ¸rer | Fritt tilgjengelig detaljinnsyn i alle skjermede opplysninger |
| Samspill mellom sentral forvaltning og lokal matrikkelfÃ¸ring | Full erstatning for andre registre som bruker matrikkeldata i egne domener |

## Veikart over kommende funksjonalitet
**Fakta fra Kartverket-kildene (kontrollert 2026-03-27):**
- Kartverket publiserer lÃ¸pende tiltak knyttet til datakvalitet, modernisering og veiledning pÃ¥ matrikkelomrÃ¥det.
- Det finnes egne sider om modernisering av informasjonsmodell, faggruppe for matrikkel og tiltak for Ã¸kt datakvalitet.

**Ikke offentlig verifisert i denne arbeidsÃ¸kten:** Et samlet, tidsfestet veikart for hele Matrikkelen er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til Ã¥ vÃ¦re rettet mot modernisering av registeret, hÃ¸yere datakvalitet og bedre samspill mellom Kartverket og kommunesektoren.

## Forretningsverdi/Verdiforslag
### For offentlig sektor
- Gir ett felles og autoritativt eiendoms- og adressegrunnlag pÃ¥ tvers av sektorer.
- Reduserer behovet for lokale kopier og ulike definisjoner av samme eiendom eller adresse.
- UnderstÃ¸tter mer samordnet saksbehandling og bedre beredskap.

### For nÃ¦ringsliv og andre brukere
- GjÃ¸r det mulig Ã¥ bygge tjenester pÃ¥ oppdaterte og standardiserte eiendomsdata.
- Gir mer forutsigbarhet i prosesser som lÃ¥n, forsikring, eiendomsomsetning og bygging.
- Reduserer usikkerhet nÃ¥r flere aktÃ¸rer trenger samme fakta om en eiendom.

### For innbyggere
- Gir innsyn i egne eiendomsopplysninger og bedre dokumentasjon gjennom matrikkelbrev og innsynstjenester.
- Skaper stÃ¸rre forutsigbarhet rundt grenser, adresser og registrerte forhold ved eiendom.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | HÃ¥ndtering |
|---|---|---|
| Datakvalitet | Ufullstendig eller feil fÃ¸ring i kommunene kan fÃ¥ store konsekvenser i mange sektorer | Veiledning, kontrollrutiner, kurs og datakvalitetstiltak |
| Juridisk og forvaltningsmessig | Feil rolleforstÃ¥else mellom sentral og lokal myndighet kan svekke kvalitet og ansvarslinjer | Tydelig regelverk, rolleavklaringer og samhandlingsarenaer |
| Tilgang og sikkerhet | Feil tilgang til skjermede eller sensitive opplysninger kan gi misbruk | Rollebasert tilgang, godkjenning og kontrollert utlevering |
| Teknisk | Endringer i register, informasjonsmodell eller tilgangslÃ¸sninger kan pÃ¥virke mange avhengige tjenester | Robust endringsforvaltning og god varsling til brukerne |
| Samfunnsavhengighet | Feil i Matrikkelen kan pÃ¥virke mange kritiske tjenester samtidig | HÃ¸y forvaltningskvalitet, redundans og tydelig prioritering av samfunnskritisk drift |

## Kanaler
- Om Matrikkelen: https://kartverket.no/eiendom/mine-eiendommer/om-matrikkelen
- Tilgang til Matrikkelen: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/matrikkelhjelp/tilgang-til-matrikkelen
- Adresser i Matrikkelen: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/adresser-i-matrikkelen
- Bygning i Matrikkelen: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/bygning-i-matrikkelen
- Matrikkelbrev: https://www.kartverket.no/en/property/mine-eiendommer/matrikkelbrev
- Faggruppe matrikkelen: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/faggruppe-matrikkelen

## Plattform
Matrikkelen er et nasjonalt register- og forvaltningssystem for eiendomsinformasjon, bygninger og adresser, levert og forvaltet av Kartverket i samspill med kommunesektoren.

**Fakta:** Kartverket beskriver bÃ¥de registerinnhold, innsynslÃ¸p, tilgangsstyring og fÃ¸ringsansvar som del av produktomrÃ¥det. Produktet omfatter derfor bÃ¥de registerkjerne, tilgangsordninger og dokumenterte arbeidsprosesser for lokal og sentral forvaltning.

**Ikke offentlig dokumentert i brukte kilder:** Full intern systemarkitektur, detaljert teknologistakk og full driftsmodell for plattformen.

## Gjenbruk
**HÃ¸y gjenbruksverdi:**
- Produktet er laget for Ã¥ vÃ¦re felles eiendoms- og adressegrunnlag pÃ¥ tvers av mange sektorer.
- Det er sÃ¦rlig relevant nÃ¥r behovet er autoritative opplysninger om eiendom, bygg eller adresse.
- Det er mindre relevant dersom behovet egentlig er en tematisk kartportal eller spesialisert geodatatjeneste som bygger videre pÃ¥ Matrikkelen.

## StÃ¸tter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at Matrikkelen tilbyr felles og autoritative grunndata om eiendom og adresser.
- **P5: Del og gjenbruk lÃ¸sninger** styrkes ved at mange sektorer kan bygge pÃ¥ samme register i stedet for lokale varianter.
- **P6: Lag digitale lÃ¸sninger som stÃ¸tter samhandling** stÃ¸ttes fordi bÃ¥de sentrale og lokale aktÃ¸rer bruker samme registergrunnlag.
- **P7: SÃ¸rg for tillit til oppgavelÃ¸sningen** er sentralt fordi kvalitet, sporbarhet og kontrollert tilgang er avgjÃ¸rende for et nasjonalt basisregister.

## Finansiering
- **Fakta:** Detaljert offentlig finansieringsmodell for hele Matrikkelen er ikke verifisert i denne arbeidsÃ¸kten.
- **Fakta:** Produktet forvaltes som nasjonal felleslÃ¸sning og basisregister med tydelig offentlig ansvar hos Kartverket og kommunene.
- **Deduksjon:** Finansieringen er trolig en kombinasjon av statlig registerforvaltning og ressursbruk hos kommunene som lokal matrikkelmyndighet.

## Forvaltning/eier
| AnsvarsomrÃ¥de | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Kartverket | Kartverket beskriver seg som forvalter og sentral matrikkelmyndighet |
| Driftsansvar | Kartverket | Produktsider og tilgangssider peker til Kartverket som operativ forvalter |
| Budsjett- og forvaltningsansvar | Kartverket sentralt, med vesentlig rolle for kommunene i fÃ¸ring og oppdatering | Kartverket beskriver samspillet mellom sentral og lokal matrikkelmyndighet |
| Styringsmodell | Kartverket som sentral matrikkelmyndighet i samspill med kommunene og KS | Faggruppe matrikkel og veiledningssider |

## Lenke til dokumentasjon
- https://kartverket.no/eiendom/mine-eiendommer/om-matrikkelen
- https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/matrikkelhjelp/tilgang-til-matrikkelen
- https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/adresser-i-matrikkelen
- https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/bygning-i-matrikkelen
- https://www.kartverket.no/en/property/mine-eiendommer/matrikkelbrev
- https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/faggruppe-matrikkelen
- https://kartverket.no/en/about-kartverket/nyheter/eiendom/2023/august/en-moderne-matrikkel

## Kildegrunnlag brukt i utfyllingen
- Lokal fil: `config/prompts/produkt-canvas.system.md`
- Lokal fil: `config/templates/produkt-canvas-template.md`
- Lokal fil: `arkitektur/kapabiliteter/capabilities.yaml`
- Lokal fil: `arkitektur/prinsipper/principles.md`
- Lokal fil: `arkitektur/ressurser/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://kartverket.no/eiendom/mine-eiendommer/om-matrikkelen (kontrollert 2026-03-27)
- Nettkilde: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/matrikkelhjelp/tilgang-til-matrikkelen (kontrollert 2026-03-27)
- Nettkilde: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/adresser-i-matrikkelen (kontrollert 2026-03-27)
- Nettkilde: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/bygning-i-matrikkelen (kontrollert 2026-03-27)
- Nettkilde: https://www.kartverket.no/en/property/mine-eiendommer/matrikkelbrev (kontrollert 2026-03-27)
- Nettkilde: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/faggruppe-matrikkelen (kontrollert 2026-03-27)
- Nettkilde: https://kartverket.no/en/about-kartverket/nyheter/eiendom/2023/august/en-moderne-matrikkel (kontrollert 2026-03-27)

