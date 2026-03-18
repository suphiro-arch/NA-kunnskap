---
date: 2026-03-06
author: codex
status: draft
topic: beslutningslogg
sources: []
---

# Beslutningslogg

| Dato | Tema | Beslutning | Begrunnelse | Eier |
|---|---|---|---|---|
| 2026-03-06 | Struktur | Opprettet standardmaler | Bedre handoff mellom assistenter | team |
| 2026-03-16 | Dokumentasjonsassistent | Første versjon skal være en åpen dokumentasjonsassistent på internett | Tydelig avgrenset MVP med lavere risiko enn full agent | team |
| 2026-03-16 | Datagrunnlag | MVP skal bare bruke offentlig informasjon fra repoet | Reduserer lisens- og personvernrisiko | team |
| 2026-03-16 | Scope | MVP skal bare svare og veilede, ikke utføre handlinger | Gir enklere arkitektur og lavere risiko | team |
| 2026-03-16 | Retrieval | MVP skal bruke repoet som eneste kunnskapskilde | Sikrer sporbarhet og kildekontroll | team |
| 2026-03-16 | Formål | Assistenten skal hjelpe prosjekter å finne relevante kapabiliteter, produkter, prinsipper og mulige gap | Passer målbildet for en arkitekturassistent | team |
| 2026-03-17 | Produktbeskrivelser | Nye produktbeskrivelser skal ikke starte med egen linje for målgruppe, og `Ressurs ID` skal skrives uten parentesforklaring | Gjør dokumentene lettere å lese og enklere å skanne på tvers av produkter | team |
| 2026-03-18 | Produktregister | `Ressurs ID` skal være eierbasert, for eksempel `DIGDIR-001`, mens internt løpenummer beholdes for filnavn og sortering | Gir en mer skalerbar identifikator når repoet utvides med flere ressurseiere som KS, Helsedirektoratet, NAV og Skatteetaten | team |
| 2026-03-18 | Produktregister | Produktregisteret skal ha en egen kolonne for `Ressurskategori` og kunne romme både norske fellesløsninger og relevante europeiske byggesteiner | Gjør registeret bedre egnet som felles oversikt når repoet senere skal utvides med flere ressurstyper som veiledere, standarder og andre virkemidler | team |
| 2026-03-18 | Produktregister | Produktregisteret skal utvides sektorvis med nasjonale løsninger som er relevante for tverrsektoriell samhandling, også utenfor Digdir-porteføljen | Gir et bredere og mer nyttig arbeidsregister når nye produktbeskrivelser skal prioriteres og sammenlignes på tvers av sektorer | team |
| 2026-03-17 | Kapabilitetsmapping | Produktbeskrivelser skal bare ta med kapabiliteter med sterk og direkte kobling til produktets egen funksjon | Reduserer støy og gjør det lettere å skille overlappende løsninger ved gjenbruksvurdering | team |
| 2026-03-17 | Webpublisering | Hugo-prototypen skal publiseres med GitHub Pages artifact-deploy direkte fra `web/hugo-prototype/` | Fjerner den skjøre synken via `docs/prototype` og gjør publiseringen mer forutsigbar | team |
| 2026-03-17 | Deploy-trigger | Publiseringsworkflowen skal også trigges ved endringer i `arkitektur/**`, `config/prompts/**` og `config/templates/**` | Innholdsgrunnlag og styrende konfigurasjon påvirker nettsiden og må kunne publiseres uten manuell workflow-kjøring | team |
| 2026-03-17 | Produkt-kapabilitet-koblinger | Repoet skal ha en eksplisitt, manuelt vedlikeholdt masterfil for koblingen mellom produkter og kapabiliteter i `arkitektur/kapabiliteter/produkt-kapabilitet-koblinger.yaml` | Gir én felles sannhetskilde for begge retninger i webprototypen og reduserer avvik mellom produktoverblikk og kapabilitetssider | team |
| 2026-03-18 | Peppol-oversikt | `ELMA` skal behandles som den tydelige norske felleskomponenten i Peppol-økosystemet og føres under Digdir, mens `Peppol eDelivery` skal behandles som en internasjonal fellesressurs eid av OpenPeppol | Skiller den nasjonale komponenten fra det fødererte internasjonale økosystemet og gjør eierskap og ressursnivå mer presist i registeret | team |
| 2026-03-18 | Produktregister | Standarder, sertifiseringsordninger, implementasjonsguider og onboardingløp skal ikke føres som egne produkter i produktregisteret | Holder registeret på samme ressursnivå som øvrige fellesløsninger og skiller produkter tydelig fra veiledning og standardforvaltning | team |
| 2026-03-18 | Ressursliste | `ELMA` og `Peppol eDelivery` skal beholdes i ressurslisten, men beskrives på ulikt nivå: `ELMA` som norsk felleskomponent og `Peppol eDelivery` som internasjonalt samhandlingsrammeverk | Begge er viktige arkitekturvalg i samhandling, men de må skilles tydelig fra hverandre og fra standarder og veiledningsmateriell | team |
| 2026-03-18 | EU-byggesteiner | `EU-003 eDelivery Building Block` skal beholdes som egen EU-ressurs i registeret, men forstås som referanseramme og byggestein rundt samme problemområde som `Peppol eDelivery`, ikke som samme ressurs | Skiller mellom et operativt samhandlingsøkosystem i bruk i norsk kontekst og en bredere EU-byggestein med programvare, test og støttefunksjoner | team |
| 2026-03-18 | EU-referanser | `EU Open Source Solutions Catalogue`, `Interoperable Europe Solutions` og `Core Vocabularies` kan stå som egne EU-referanseressurser i registeret, men skal ikke prioriteres som produktbeskrivelser på lik linje med operative fellesløsninger | De er relevante for gjenbruk, interoperabilitet og semantikk, men fungerer først og fremst som kataloger, rammeverk og referanseressurser | team |
| 2026-03-18 | Kapabilitetsgrunnlag | `sources/2025-03-18-Nasjonal Arkitektur.xml` skal behandles som råkilde, mens `arkitektur/kapabiliteter/capabilities.yaml` og `arkitektur/prinsipper/principles.md` er de kuraterte arbeidsfilene i repoet | XML-modellen inneholder også hjelpeelementer, kopier og generiske prinsippreferanser som ikke skal inn i den operative dokumentasjonsstrukturen | team |
| 2026-03-18 | Prinsippgrunnlag | `arkitektur/prinsipper/principles.md` skal brukes som styrende kilde for prinsipper i videre analyser, produktbeskrivelser og webprototypen | Gir ett kuratert prinsippgrunnlag i repoet og unngår at analyser og web bygger direkte på rå XML eller manuelle avskrifter | team |
| 2026-03-18 | Målspor | Målene fra XML-kilden skal håndteres i en egen kuratert fil `arkitektur/maal/maal.md`, ikke bygges inn direkte i kapabilitets- eller ressursmasterne | XML-modellen har et eget målspor, men viser ikke full operativ kobling mellom hver kapabilitet, hvert mål og hver ressurs på et nivå som kan brukes direkte videre | team |
| 2026-03-18 | Ressurskoblinger | XML-kilden skal ikke brukes som autoritativ kilde for kobling mellom konkrete produkter og kapabiliteter | Ressursrelasjonene i XML er generiske og modelltekniske, og samsvarer ikke med repoets produktnivå i `produkt-kapabilitet-koblinger.yaml` | team |
| 2026-03-18 | Filansvar i arkitekturgrunnlaget | `capabilities.yaml` skal bare beskrive kapabilitetsstrukturen, mens prinsipptekst, prinsippbegrunnelser og målspor skal ligge i egne kuraterte filer | Reduserer duplisering, gjør filansvaret tydeligere og hindrer at samme innhold vedlikeholdes flere steder | team |
| 2026-03-18 | Produkt-kapabilitet-master | `produkt-kapabilitet-koblinger.yaml` skal eksplisitt behandles som manuelt kuratert masterfil og ikke som avledning fra rå XML-modellen | XML-kilden har ikke operative koblinger mellom konkrete produkter og kapabiliteter på det nivået repoet bruker videre | team |
