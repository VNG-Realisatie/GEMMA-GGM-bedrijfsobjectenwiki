---
type: domein
naam: Dienstverlening
bronnen_count: 2
begrippen_count: 8
---

# Domein: Dienstverlening

Gemeentelijke dienstverlening — zaakgericht werken, zaaktypecatalogi, informatieobjecten en de informatiestandaarden die het dienstverleningsproces ondersteunen. Dit domein is domeinoverstijgend: het levert de generieke structuur waarmee alle gemeentelijke domeinen hun dienstverlening organiseren.

## GGM-taakvelden

Dit wiki-domein raakt twee GGM-taakvelden:
- **Taakveld 10 Dienstverlening** — meldingen, aanvragen, baliecontacten, telefonische afhandeling en digitale interacties
- **Taakveld 99 Kern / RGBZPlus** — de zaakgerichte kern: Zaak, Status, Besluit, Document, Betrokkene, Medewerker (25 entiteiten)

De ZTC2-configuratielaag (CATALOGUS, RESULTAATTYPE, EIGENSCHAP, ROLTYPE, ZAAKOBJECTTYPE) is niet in het GGM gemodelleerd.

## Begrippen

### Thema
- [[zaakgericht-werken]] — werkwijze: dienstverlening organiseren rond zaken
- [[gemeentelijke-inkoop]] — het geheel van inkoopactiviteiten (€40+ mrd)

### Instrumenten
- [[aanbesteding]] — verplichte inkoopprocedure boven drempelbedragen
- [[mvoi]] — maatschappelijk verantwoord opdrachtgeven en inkopen

### Objecten
- [[zaaktypecatalogus]] — verzameling zaaktypen met configuratie per domein
- [[informatieobject]] — geheel van gegevens ongeacht vorm (breder dan "document")
- [[zaakdossier]] — zaakkenmerken + informatieobjecten, basis voor archivering
- [[resultaattype]] — mogelijke uitkomsten per zaaktype, bepaalt archiefregime

## Bedrijfsobjecten

*(Nog geen bedrijfsobjecten aangemaakt voor dit domein. De GGM-entiteiten in RGBZPlus — Zaak, Status, Besluit, Document, Betrokkene — zijn kandidaten.)*

## Informatiestandaarden

| Standaard | Versie | Scope |
|---|---|---|
| **RGBZ** | 1.0 (2010) | Runtime-datamodel: zaakgegevens, betrokkenen, documenten, statussen, besluiten |
| **ZTC2** | 2.1 (2014) | Configuratielaag: zaaktypen, statustypes, resultaattypes, roltypes, eigenschappen |
| **RSGB** | 2.02 (2018) | Basisgegevens: de objecten waarop zaken betrekking hebben |
| **StUF-Zaken** | 3.10 (2010) | Berichtenstandaard afgeleid van het RGBZ |

## Verwerkte bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]] — RGBZ 1.0 + Introductie: referentiemodel zaakgegevens, berichtenarchitectuur, evolutie naar ZGW API's
- [[Wiki/Bronsamenvattingen/Standaarden/ztc2-informatiemodel]] — ZTC2 v2.1: informatiemodel zaaktypecatalogus
- [[Sources/Onderwerpen VNG/Dienstverlening/raadgever-inkoop-en-aanbesteden]] — VNG Raadgever: inkoop, aanbestedingsregels en MVOI

## Evolutie

Het RGBZ 1.0 (2010) is de huidige officiële standaard. RGBZ 2.0 heeft nooit een officiële status bereikt, maar concepten eruit zijn overgenomen in de **ZGW API's** (REST/JSON), die wél officieel zijn. De ZGW API's zijn de opvolger van de StUF-ZKN berichtenstandaard.

## Openstaande vragen

- GGM taakveld 10 Dienstverlening (beleidsdomein "Model Dienstverlening") is nog niet als GGM-bronbestand geëxtraheerd — welke entiteiten zitten daar?
- De ZTC2-configuratielaag ontbreekt in het GGM. Is dit een bewuste keuze (de ZTC2 is een apart informatiemodel) of een hiaat?
- Hoe actueel is het GGM-beleidsdomein RGBZPlus gezien de evolutie RGBZ 1.0 → RGBZ 2.0 (concept) → ZGW API's?
