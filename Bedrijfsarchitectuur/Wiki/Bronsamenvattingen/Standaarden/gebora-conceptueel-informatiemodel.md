---
type: bronsamenvatting
titel: "GEBORA: Gebouwde Omgeving Referentie Architectuur — Conceptueel Informatiemodel"
onderwerp: [Standaarden, Vastgoed]
datum_ingest: 2026-09-24
---

## Samenvatting

GEBORA (Gebouwde Omgeving Referentie Architectuur) is een conceptueel informatiemodel van digiGO (v1.0, 30-04-2025) dat de belangrijkste bedrijfsobjecten in de gebouwde omgeving en hun onderlinge relaties beschrijft. Het is opgesteld met input van meerdere ketenpartijen (o.a. Aedes, Rijksvastgoedbedrijf) en aangesloten op externe bronnen (MKGO/ISSO, Aedes Woning Informatie Model, MiniBIM, RVB Gegevensmodel). Het model volgt NEN 2660/ArchiMate-conventies: een bedrijfsobject is een concept binnen een informatiedomein, passief (initieert geen processen), en herkenbaar als zelfstandig naamwoord.

Het model onderscheidt 12 informatiedomeinen met in totaal ~35 bedrijfsobjecten:
1. **Bouwwerk** — Bouwwerk, Bouwdeel, Ruimte, Installatie
2. **Ontwerp en Model** — Functie, Ontwerp, Model (incl. BIM)
3. **Omgeving** — Zone, Bestemming, Gebied, Object, Infrastructuur
4. **Product en Materiaal** — Product, Materiaal
5. **Kwaliteit, vergunning en registratie** — Vergunning, Kwaliteit, Risico, Registratie
6. **Realisatie** — Activiteit, Project, Werkcontract, Order
7. **Middel** — Personeel, Materieel
8. **Logistiek** — Logistiek, Transport
9. **Gebruik en Prestatie** — Gebruik, Prestatie, Beleving
10. **Instandhouding en onderhoud** — Conditie, Instandhouding, Onderhoud
11. **Asset management** — Asset, Assetplan, Assetinitiatief
12. **Organisatie en Transactie** — Koop/Verkoop, Huur/Verhuur, Boekhouding, Overeenkomst, Organisatie

Het document bevat een uitgebreide FAQ-sectie waarin modelleurskeuzes worden toegelicht (bijv. het onderscheid Asset vs. Object vs. Bouwwerk: Asset is de boekhoudkundige/administratieve representatie, Object het fysieke ding, Bouwwerk de specialisatie van Object met alle fysieke eigenschappen).

**Relevantie voor het gemeentelijk perspectief:** een substantieel deel van het model (Product, Materiaal, Materieel, Personeel, Werkcontract, Order, Transport, Logistiek, individuele bouwcomponenten) beschrijft de bedrijfsvoering van bouw-/onderhoudsketenpartners — dit valt buiten scope (ketenpartnerprocessen, [WC5]). De domeinen 5 (Kwaliteit/vergunning/registratie), 10 (Instandhouding en onderhoud), 11 (Asset management) en delen van 3 (Omgeving) en 12 (Organisatie en Transactie) raken wel het gemeentelijk vastgoedbeheerperspectief.

## Kernbegrippen

- **Bouwwerk/Object** — GGM-vergelijkbaar met de bestaande BO [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject|Vastgoedobject]] (perceel, gebouw of terrein). GEBORA's onderscheid Object (fysiek, geen bouwwerk) vs. Bouwwerk (specialisatie van Object) vs. Asset (boekhoudkundige representatie) is fijnmaziger dan de wiki's huidige model.
- **Asset, Assetplan, Assetinitiatief** — sluit aan bij bestaande BO's [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedobject|Vastgoedobject]] en [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/mjop|MJOP]] (Assetplan ≈ MJOP). Assetinitiatief (aanvang van een ontwikkeling/verbetering) heeft geen directe tegenhanger.
- **Instandhouding, Onderhoud, Conditie** — sluit aan bij bestaande BO's [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/werkbon|Werkbon]] en [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/inspectie|Inspectie]] en het niet-BO-begrip conditiescore.
- **Vergunning** — generiek begrip, sluit aan bij bestaande BO [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/vergunningen-en-ontheffingen|Vergunningen en ontheffingen]].
- **Zone, Bestemming, Gebied** — ruimtelijke-ordeningsbegrippen die overlappen met reeds ge-ingeste BGT/Omgevingswet-objecten.
- **Koop/Verkoop, Huur/Verhuur, Overeenkomst** — Huur/Verhuur sluit aan bij bestaande BO [[Wiki/Bedrijfsobjecten/9-interne-organisatie/vastgoed/vastgoedcontract|Vastgoedcontract]]. Koop/Verkoop (eigendomsoverdracht) heeft geen directe tegenhanger in het Vastgoed-domein.

## Relevantie voor bedrijfsarchitectuur

GEBORA is geen wettelijke basisregistratie maar een vrijwillig ketenbreed referentiemodel; het dient hier als verificatiebron voor de bestaande, reeds afgeronde BO's in het Vastgoed-domein. Het bevestigt grotendeels het bestaande model (Vastgoedobject, MJOP, Werkbon, Inspectie, Vastgoedcontract) en scherpt het onderscheid Object/Bouwwerk/Asset aan. IMWO ([[Wiki/Bronsamenvattingen/Standaarden/imwo-informatiemodel-woongebouwen|digiGO Informatiemodel Woongebouwen]]) is een detailuitwerking van GEBORA's domein 1 (Bouwwerk), specifiek voor woning en woongebouw.

> "Een bedrijfsobject vertegenwoordigt een concept dat binnen een bepaald informatiedomein wordt gebruikt. [...] Bedrijfsobjecten zijn passief in de zin dat ze geen processen in gang zetten of uitvoeren." (bron: gebora-conceptueel-informatiemodel.md)

> "Met asset wordt hier de administratieve of boekhoudkundige entiteit met een bepaalde waarde, die in stand moet worden gehouden, bedoeld. Met object wordt bedoeld een fysiek object in de omgeving, die geen bouwwerk is; een bouwwerk is strikt genomen een specialisatie van 'object'." (bron: gebora-conceptueel-informatiemodel.md, FAQ)

## Bronnen

- [[Sources/Standaarden/gebora-conceptueel-informatiemodel]]
