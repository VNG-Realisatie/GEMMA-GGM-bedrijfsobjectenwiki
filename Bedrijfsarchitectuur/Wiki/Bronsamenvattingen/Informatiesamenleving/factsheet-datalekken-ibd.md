---
type: bronsamenvatting
titel: "Factsheet Datalekken — IBD"
onderwerp: [Informatiesamenleving]
datum_ingest: 2026-06-26
---

# Factsheet Datalekken — IBD

Factsheet van de Informatiebeveiligingsdienst voor gemeenten (IBD, versie 2.0, augustus 2024) over datalekken: definitie, meldplicht, registratieplicht en risicoafweging. Specifiek geschreven voor gemeenten.

## Samenvatting

### Definitie

Een datalek is een inbreuk in verband met persoonsgegevens (art. 4 lid 12 AVG): ongeoorloofde toegang, verstrekking, verlies, vernietiging of wijziging van persoonsgegevens. Voorbeelden: e-mail naar verkeerd adres, kwijtgeraakte USB-stick, laptopdiefsal, inzage door onbevoegde medewerker, onbeschikbaarheid door systeemstoring.

### Meldplicht AP (art. 33 AVG)

Bij een datalek dat risico oplevert voor rechten en vrijheden van betrokkenen: melding bij de AP binnen 72 uur na ontdekking. Bij lopend onderzoek: voorlopige melding binnen 72 uur. De AP houdt een niet-openbaar register bij; boetebesluiten zijn wel openbaar.

### Melding betrokkenen (art. 34 AVG)

Alleen verplicht bij hoog risico voor rechten en vrijheden. Melding bevat:
- naam en contactgegevens FG of ander contactpunt
- waarschijnlijke gevolgen van de inbreuk
- genomen/voorgestelde maatregelen inclusief maatregelen ter beperking nadelige gevolgen

Niet verplicht als passende technische beschermingsmaatregelen de gegevens onbegrijpelijk of ontoegankelijk hebben gemaakt.

### Registratieplicht

De gemeente is verplicht een administratie bij te houden van **alle** datalekken, ook niet-gemelde. Per incident vastleggen:
- feiten en aard van de inbreuk
- oorzaak
- betrokken gegevens
- ontdekkingsmoment
- wijze van dichten
- meldtekst aan betrokkenen (indien gemeld)

Minimale bewaartermijn: 1 jaar.

### Risicoafweging

Kans × impact matrix met vier niveaus (verwaarloosbaar, beperkt, aanzienlijk, ernstig). De verwerkingsverantwoordelijke schat zelf het risico in; de FG of IBD privacy-adviseur kan helpen.

### Ketenpartners

Bij datalek bij een verwerker (externe partij): de gemeente als verwerkingsverantwoordelijke is verantwoordelijk voor de meldplicht. Afspraken hierover in verwerkersovereenkomst.

## Kernbegrippen

- **Datalek** — inbreuk in verband met persoonsgegevens: ongeoorloofde toegang, verstrekking, verlies, vernietiging of wijziging. Meldplicht AP (72u), registratieplicht (alle incidenten, min. 1 jaar bewaring). Eigen levenscyclus (ontdekking → onderzoek → risico-inschatting → melding → afsluiting).
- **Beveiligingsincident** — breder dan datalek; niet elk incident betreft persoonsgegevens. Een beveiligingsincident met persoonsgegevens is een datalek.
- **Meldplicht datalekken** — wettelijke verplichting om datalekken te melden bij AP (art. 33) en betrokkenen (art. 34).
- **Verwerkersovereenkomst** — schriftelijke afspraken met verwerker over o.a. tijdig informeren bij datalekken.

## Relevantie voor bedrijfsarchitectuur

De bron maakt **Datalek** concreet als BO-kandidaat:
- Verplichte attributen per incident (feiten, aard, oorzaak, gegevens, ontdekking, maatregelen, meldtekst)
- Eigen levenscyclus (ontdekking → onderzoek → risico-inschatting → melding AP → evt. melding betrokkenen → afsluiting → bewaring)
- Verplichte relaties (AP als ontvanger melding, betrokkenen als geïnformeerden, FG als adviseur)
- Registratieplicht voor alle incidenten (niet alleen gemelde)
- Risicoafwegingskader (kans × impact)

Het begrip is verwant aan **Ernstig incident** (AI-verordening art. 3 lid 49) maar breder: datalek betreft alle persoonsgegevens, ernstig incident is specifiek voor AI-systemen.

## Citaten

> "De gemeente is verplicht om een administratie bij te houden van alle datalekken, dus ook van de datalekken die niet gemeld hoeven te worden." (bron: IBD factsheet)

> "Per incident moet een gemeente in ieder geval de feiten en de gegevens over de aard van de inbreuk vastleggen. Bijvoorbeeld de oorzaak, om welke gegevens het gaat, het moment dat het lek is ontdekt en op welke wijze het lek gedicht is." (bron: IBD factsheet)

> "Indien een datalek een risico oplevert voor de rechten en vrijheden van de betrokkene(n) moet het datalek binnen 72 uur na ontdekking bij de Autoriteit Persoonsgegevens (AP) gemeld worden." (bron: IBD factsheet)

## Bronnen
- [[Sources/Onderwerpen/Informatiesamenleving/factsheet-datalekken-ibd]]
