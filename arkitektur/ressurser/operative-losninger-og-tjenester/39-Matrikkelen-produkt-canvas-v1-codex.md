# Produkt-canvas: Matrikkelen

## Navn
Matrikkelen

## Ressurs ID
KART-001

## Status/Livsfase
**Produksjon** - etablert nasjonalt register og felleskomponent for eiendomsopplysninger, bygninger, adresser og grenser.

**Fakta:** Kartverket beskriver Matrikkelen som det offisielle registeret over norske eiendommer. Kartverket omtaler også Matrikkelen som en nasjonal fellesløsning og en av de tre statlige felleskomponentene, sammen med Folkeregisteret og Enhetsregisteret.

## Modenhet
**Høy modenhet** - innarbeidet og samfunnskritisk grunndataregister:
- Registeret brukes av et bredt spekter av offentlige og private aktører, blant annet kommuner, nødetater, banker, forsikringsselskaper og Skatteetaten.
- Kartverket forvalter Matrikkelen sentralt, mens kommunene har viktige roller som lokal matrikkelmyndighet og adressemyndighet.
- Produktet har både operative tilgangsløp, innsynsløsninger, attestert utskrift og dokumentert rolle- og tilgangsmodell.
- Kartverket arbeider aktivt med datakvalitet, føringsveiledning og samhandling med kommunesektoren.

**Deduksjon:** Modenheten er høy både fordi registeret er grunnleggende for mange samfunnsfunksjoner og fordi det har et tydelig forvaltningsregime. Samtidig er verdien avhengig av kvaliteten i føring og oppdatering hos kommunene og andre registrerende aktører.

## Kort beskrivelse
Matrikkelen er det nasjonale grunndataregisteret for eiendommer, bygninger, adresser og offisielle eiendomsidentifikatorer i Norge. Produktet gjør det mulig å registrere, forvalte og bruke autoritative opplysninger om fast eiendom og tilhørende objekter på tvers av sektorer og forvaltningsnivåer. Matrikkelen er derfor mer enn en innsynstjeneste: den er den sentrale registerløsningen som mange andre tjenester og beslutningsprosesser bygger på når de trenger pålitelig informasjon om eiendom, bygg og adresser.

## Kapabiliteter
- **Datakilder: Grunndata** er kjernefunksjonen ved at Matrikkelen fungerer som autoritativ kilde for sentrale opplysninger om eiendommer, bygninger og adresser.
- **Datautveksling og integrasjon: Dele data med andre** gjør opplysninger fra Matrikkelen tilgjengelige for mange andre virksomheter og tjenester som trenger eiendoms- og adressegrunnlag.

Grunnlag: Kapabilitetsnavn fra `arkitektur/kapabiliteter/capabilities.yaml`, vurdert mot Kartverkets beskrivelser av Matrikkelen som offisielt register, nasjonal fellesløsning og statlig felleskomponent.

## Produktmål
**Primærkilder:** Kartverkets side `Dette er matrikkelen`, tilgangssider for Matrikkelen og veiledningssider om bygninger og adresser i Matrikkelen.

Dokumenterte mål:
- Være det offisielle registeret over norske eiendommer.
- Gi oversikt over grenser, bygninger, adresser og eierforhold.
- Dekke behov på tvers av mange sektorer og forvaltningsnivåer.

Operative mål utledet fra de samme kildene:
- Gi samfunnet ett felles eiendoms- og adressegrunnlag i stedet for mange lokale eller sektorvise varianter.
- Støtte både offentlig myndighetsutøvelse og private tjenester som er avhengige av pålitelige eiendomsopplysninger.
- Legge grunnlag for sammenheng mellom lokal registrering i kommunene og nasjonal tilgjengeliggjøring av dataene.

## Brukerbehov
- Kommuner trenger et autoritativt register for å føre eiendoms-, adresse- og bygningsopplysninger som del av sine myndighetsoppgaver.
- Offentlige virksomheter trenger pålitelige eiendomsdata for saksbehandling, beredskap, planlegging og samordning.
- Private virksomheter trenger standardiserte og oppdaterte opplysninger om eiendommer og bygninger i egne tjenester.
- Innbyggere trenger innsyn i opplysninger om egne eiendommer og tilgang til dokumentasjon som matrikkelbrev.

## Hvem er brukerne og brukersegmentene
| Brukersegment | Primære behov | Bruksområde | Kommentar |
|---|---|---|---|
| Kommuner som lokal matrikkelmyndighet | Føre og oppdatere opplysninger korrekt | Matrikkelføring, adressering og bygningsoppdatering | Har en sentral rolle i datakvaliteten |
| Offentlige virksomheter | Bruke pålitelige eiendoms- og adresseopplysninger | Beredskap, saksbehandling, planlegging og forvaltning | Viktig tverrsektoriell brukergruppe |
| Private virksomheter | Tilgang til standardiserte eiendomsdata | Bank, forsikring, bygg, eiendomsmegling og logistikk | Bruker dataene i samfunnskritiske prosesser |
| Innbyggere og eiere | Innsyn og dokumentasjon | Oppslag i egne eiendommer og bestilling av matrikkelbrev | Møter produktet via innsynsløsninger og kommunale prosesser |
| Kartverket og fagmiljøer | Forvaltning, kvalitet og samordning | Sentral registerforvaltning, veiledning og utvikling | Kartverket er sentral matrikkelmyndighet |

## Hovedfunksjoner
### Primære funksjoner
**Autoritativ registrering av eiendom, bygninger og adresser.** Matrikkelen samler og forvalter nøkkelopplysninger om eiendommer, bygninger og adresser i ett nasjonalt register. Dette er produktets viktigste funksjon, og det gjør løsningen relevant når mange sektorer trenger samme grunnlag for identifikasjon og beskrivelse av eiendom.

**Nasjonalt felles adresse- og eiendomsgrunnlag.** Produktet gir et felles system for offisielle adresser og eiendomsidentifikatorer. Det gjør Matrikkelen sentral i samfunnsfunksjoner som beredskap, postlevering, byggesak, eiendomsomsetning og offentlig planlegging, der aktørene må kunne bruke samme referansegrunnlag.

**Tilgjengeliggjøring og innsyn i matrikkelopplysninger.** Kartverket beskriver både innsynsløsninger og matrikkelbrev som del av produktområdet. Det betyr at Matrikkelen ikke bare er et internt register for myndigheter, men også et grunnlag for innsyn, attestert dokumentasjon og videre bruk av opplysninger i andre tjenester.

**Samspill mellom sentral forvaltning og lokal føring.** Produktet forutsetter et operativt samspill mellom Kartverket som sentral matrikkelmyndighet og kommunene som fører og oppdaterer data. Veiledning, tilgangsroller, kurs og faglige samhandlingsarenaer er derfor en viktig del av hvordan produktet faktisk fungerer i praksis.

### Scope og avgrensning
| Inngår | Inngår ikke |
|---|---|
| Offisielt register over eiendommer, bygninger og adresser | Tinglysingsregisteret eller andre rettighetsregistre som egen ressurs |
| Felles identifikatorer og grunndata om eiendom | Full kartportal eller generell geodataplattform |
| Innsyn og dokumentasjon som bygger på matrikkeldata | Lokal saksbehandling utover det som registreres i Matrikkelen |
| Rolle- og tilgangsstyrt bruk for kommuner og andre aktører | Fritt tilgjengelig detaljinnsyn i alle skjermede opplysninger |
| Samspill mellom sentral forvaltning og lokal matrikkelføring | Full erstatning for andre registre som bruker matrikkeldata i egne domener |

## Veikart over kommende funksjonalitet
**Fakta fra Kartverket-kildene (kontrollert 2026-03-27):**
- Kartverket publiserer løpende tiltak knyttet til datakvalitet, modernisering og veiledning på matrikkelområdet.
- Det finnes egne sider om modernisering av informasjonsmodell, faggruppe for matrikkel og tiltak for økt datakvalitet.

**Ikke offentlig verifisert i denne arbeidsøkten:** Et samlet, tidsfestet veikart for hele Matrikkelen er ikke hentet ut.

**Deduksjon:** Videreutviklingen ser ut til å være rettet mot modernisering av registeret, høyere datakvalitet og bedre samspill mellom Kartverket og kommunesektoren.

## Forretningsverdi/Verdiforslag
### For offentlig sektor
- Gir ett felles og autoritativt eiendoms- og adressegrunnlag på tvers av sektorer.
- Reduserer behovet for lokale kopier og ulike definisjoner av samme eiendom eller adresse.
- Understøtter mer samordnet saksbehandling og bedre beredskap.

### For næringsliv og andre brukere
- Gjør det mulig å bygge tjenester på oppdaterte og standardiserte eiendomsdata.
- Gir mer forutsigbarhet i prosesser som lån, forsikring, eiendomsomsetning og bygging.
- Reduserer usikkerhet når flere aktører trenger samme fakta om en eiendom.

### For innbyggere
- Gir innsyn i egne eiendomsopplysninger og bedre dokumentasjon gjennom matrikkelbrev og innsynstjenester.
- Skaper større forutsigbarhet rundt grenser, adresser og registrerte forhold ved eiendom.

## Utfordringer og risiko
| Risikokategori | Konkret risiko | Håndtering |
|---|---|---|
| Datakvalitet | Ufullstendig eller feil føring i kommunene kan få store konsekvenser i mange sektorer | Veiledning, kontrollrutiner, kurs og datakvalitetstiltak |
| Juridisk og forvaltningsmessig | Feil rolleforståelse mellom sentral og lokal myndighet kan svekke kvalitet og ansvarslinjer | Tydelig regelverk, rolleavklaringer og samhandlingsarenaer |
| Tilgang og sikkerhet | Feil tilgang til skjermede eller sensitive opplysninger kan gi misbruk | Rollebasert tilgang, godkjenning og kontrollert utlevering |
| Teknisk | Endringer i register, informasjonsmodell eller tilgangsløsninger kan påvirke mange avhengige tjenester | Robust endringsforvaltning og god varsling til brukerne |
| Samfunnsavhengighet | Feil i Matrikkelen kan påvirke mange kritiske tjenester samtidig | Høy forvaltningskvalitet, redundans og tydelig prioritering av samfunnskritisk drift |

## Kanaler
- Om Matrikkelen: https://kartverket.no/eiendom/mine-eiendommer/om-matrikkelen
- Tilgang til Matrikkelen: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/matrikkelhjelp/tilgang-til-matrikkelen
- Adresser i Matrikkelen: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/adresser-i-matrikkelen
- Bygning i Matrikkelen: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/bygning-i-matrikkelen
- Matrikkelbrev: https://www.kartverket.no/en/property/mine-eiendommer/matrikkelbrev
- Faggruppe matrikkelen: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/faggruppe-matrikkelen

## Plattform
Matrikkelen er et nasjonalt register- og forvaltningssystem for eiendomsinformasjon, bygninger og adresser, levert og forvaltet av Kartverket i samspill med kommunesektoren.

**Fakta:** Kartverket beskriver både registerinnhold, innsynsløp, tilgangsstyring og føringsansvar som del av produktområdet. Produktet omfatter derfor både registerkjerne, tilgangsordninger og dokumenterte arbeidsprosesser for lokal og sentral forvaltning.

**Ikke offentlig dokumentert i brukte kilder:** Full intern systemarkitektur, detaljert teknologistakk og full driftsmodell for plattformen.

## Gjenbruk
**Høy gjenbruksverdi:**
- Produktet er laget for å være felles eiendoms- og adressegrunnlag på tvers av mange sektorer.
- Det er særlig relevant når behovet er autoritative opplysninger om eiendom, bygg eller adresse.
- Det er mindre relevant dersom behovet egentlig er en tematisk kartportal eller spesialisert geodatatjeneste som bygger videre på Matrikkelen.

## Støtter arkitekturprinsipper
- **P4: Del og gjenbruk data** realiseres ved at Matrikkelen tilbyr felles og autoritative grunndata om eiendom og adresser.
- **P5: Del og gjenbruk løsninger** styrkes ved at mange sektorer kan bygge på samme register i stedet for lokale varianter.
- **P6: Lag digitale løsninger som støtter samhandling** støttes fordi både sentrale og lokale aktører bruker samme registergrunnlag.
- **P7: Sørg for tillit til oppgaveløsningen** er sentralt fordi kvalitet, sporbarhet og kontrollert tilgang er avgjørende for et nasjonalt basisregister.

## Finansiering
- **Fakta:** Detaljert offentlig finansieringsmodell for hele Matrikkelen er ikke verifisert i denne arbeidsøkten.
- **Fakta:** Produktet forvaltes som nasjonal fellesløsning og basisregister med tydelig offentlig ansvar hos Kartverket og kommunene.
- **Deduksjon:** Finansieringen er trolig en kombinasjon av statlig registerforvaltning og ressursbruk hos kommunene som lokal matrikkelmyndighet.

## Forvaltning/eier
| Ansvarsområde | Organisasjon / vurdering | Grunnlag |
|---|---|---|
| Produktansvar | Kartverket | Kartverket beskriver seg som forvalter og sentral matrikkelmyndighet |
| Driftsansvar | Kartverket | Produktsider og tilgangssider peker til Kartverket som operativ forvalter |
| Budsjett- og forvaltningsansvar | Kartverket sentralt, med vesentlig rolle for kommunene i føring og oppdatering | Kartverket beskriver samspillet mellom sentral og lokal matrikkelmyndighet |
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
- Lokal fil: `arkitektur/produkter/produktnummerering.md`
- Lokal fil: `sources/links.md`
- Nettkilde: https://kartverket.no/eiendom/mine-eiendommer/om-matrikkelen (kontrollert 2026-03-27)
- Nettkilde: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/matrikkelhjelp/tilgang-til-matrikkelen (kontrollert 2026-03-27)
- Nettkilde: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/adresser-i-matrikkelen (kontrollert 2026-03-27)
- Nettkilde: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/bygning-i-matrikkelen (kontrollert 2026-03-27)
- Nettkilde: https://www.kartverket.no/en/property/mine-eiendommer/matrikkelbrev (kontrollert 2026-03-27)
- Nettkilde: https://www.kartverket.no/eiendom/lokal-matrikkelmyndighet/faggruppe-matrikkelen (kontrollert 2026-03-27)
- Nettkilde: https://kartverket.no/en/about-kartverket/nyheter/eiendom/2023/august/en-moderne-matrikkel (kontrollert 2026-03-27)
