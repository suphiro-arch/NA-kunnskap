# Handover: Kontroll av produktkoblinger til kapabiliteten Samarbeid

Dato: 2026-04-09

## Konklusjon

Råmodellen bekrefter kapabilitetsstruktur for Samarbeid, men ikke direkte produkt-til-kapabilitet-koblinger.

Det er derfor ikke mulig å verifisere 1:1 fra råfilen at alle løsningene under faktisk mapper til Samarbeid. Dagens produktmapping må fortsatt regnes som kuratert og autoritativ i masterfila for koblinger.

## Kildegrunnlag

- Råmodell: [sources/2025-03-18-Nasjonal Arkitektur.xml](../sources/2025-03-18-Nasjonal%20Arkitektur.xml)
- Kapabilitetsmaster: [arkitektur/kapabiliteter/capabilities.yaml](../arkitektur/kapabiliteter/capabilities.yaml)
- Produktmapping (autoritativ): [arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml)
- Tidligere avklaring: [sources/2026-03-18-avviksrapport-produktbeskrivelser-og-kapabiliteter.md](../sources/2026-03-18-avviksrapport-produktbeskrivelser-og-kapabiliteter.md)

## Kontroll av ny XML-eksport (2025-04-09)

En fullstendig analyse av [2025-04-09-Nasjonal Arkitektur.xml](C:/Users/HILROS/OneDrive%20-%20Digitaliseringsdirektoratet/Prosjekt_Regvil%2041%20Nasjonal%20Arkitektur%20-%20General/05.%20Arbeidsdokumenter/Kapabilitetsarbeid/Archi-modell/Eksport/2025-04-09-Nasjonal%20Arkitektur.xml) over alle 54 kapabiliteter bekrefter:

- **Ingen kapabiliteter** har direkte relasjoner til navngitte løsninger/produkter (elementtype `Resource`).
- To kapabiliteter (`Domenekapabilitet`, `Strategisk kapabilitet (overordnet)`) peker til generiske ressursplassholdere uten produktnavn.
- Alle kapabiliteter er utelukkende koblet til andre kapabiliteter, prinsipper, mål og grupperinger.

**Konklusjon:** Råmodellen i begge XML-eksporter er en ren struktur- og kapabilitetsmodell. Det finnes ingen kildedekning i Archi-modellen for produktnivå-mappinger. Alle koblinger fra konkrete løsninger til kapabiliteter i `produkt-kapabilitet-koblinger.yaml` er kuraterte.

## Hva råfila faktisk viser

- Samarbeid finnes som egen kapabilitet: [sources/2025-03-18-Nasjonal Arkitektur.xml](../sources/2025-03-18-Nasjonal%20Arkitektur.xml#L527)
- Samarbeid aggregerer delkapabiliteter:
  - Organisatorisk samhandling: [sources/2025-03-18-Nasjonal Arkitektur.xml](../sources/2025-03-18-Nasjonal%20Arkitektur.xml#L1094)
  - Samarbeidsarenaer og nettverk: [sources/2025-03-18-Nasjonal Arkitektur.xml](../sources/2025-03-18-Nasjonal%20Arkitektur.xml#L1095)
  - Tjenesteforvaltning: [sources/2025-03-18-Nasjonal Arkitektur.xml](../sources/2025-03-18-Nasjonal%20Arkitektur.xml#L1096)
- Råfilen viser ikke eksplisitte relasjoner fra konkrete produkter/ressurser til disse delkapabilitetene.

## Kontroll av dagens Samarbeid-mapping

Tabellen under viser alle produkter som i dag er mappet til Samarbeid i masterfila.

- Feltet `Navn funnet i rå XML` er kun et navnetreff (tekstforekomst), ikke relasjonsbevis.
- Feltet `Råfil bekrefter mapping` er derfor `Nei (kuratert)` for alle.

| Produkt-ID | Produkt | Delkapabilitet | Navn funnet i rå XML | Råfil bekrefter mapping |
|---|---|---|---|---|
| 6 | eInnsyn | Organisatorisk samhandling | Ja | Nei (kuratert) |
| 7 | eFormidling | Organisatorisk samhandling | Ja | Nei (kuratert) |
| 8 | Altinn Formidling | Organisatorisk samhandling | Ja | Nei (kuratert) |
| 19 | Altinn 3 plattform | Tjenesteforvaltning | Nei | Nei (kuratert) |
| 25 | Fiks-plattformen | Organisatorisk samhandling | Nei | Nei (kuratert) |
| 26 | Fiks melding | Organisatorisk samhandling | Ja | Nei (kuratert) |
| 27 | Fiks SvarUt | Organisatorisk samhandling | Ja | Nei (kuratert) |
| 34 | Kjernejournal | Organisatorisk samhandling | Nei | Nei (kuratert) |
| 35 | e-resept | Organisatorisk samhandling | Nei | Nei (kuratert) |
| 48 | Felles studentsystem (FS) | Organisatorisk samhandling | Nei | Nei (kuratert) |
| 49 | OpptakslÃ¸sninger | Organisatorisk samhandling | Nei | Nei (kuratert) |
| 57 | SvarInn | Organisatorisk samhandling | Nei | Nei (kuratert) |
| 59 | A-ordningen | Organisatorisk samhandling | Nei | Nei (kuratert) |
| 62 | DSOP-tjenester | Organisatorisk samhandling | Nei | Nei (kuratert) |
| 73 | VIGO | Organisatorisk samhandling | Nei | Nei (kuratert) |

## Anbefalt videre bruk

- Bruk produktmapping-fila som sannhetskilde for hvilke løsninger som støtter Samarbeid:
  [arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml](../arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml)
- Bruk rå XML til å validere struktur (kapabilitet, delkapabilitet, prinsipper), ikke produktnivå-mapping.
