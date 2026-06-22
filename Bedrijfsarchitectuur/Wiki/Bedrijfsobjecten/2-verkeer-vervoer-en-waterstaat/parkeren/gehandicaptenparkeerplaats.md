---
type: bedrijfsobject
naam: Gehandicaptenparkeerplaats
domein: [mobiliteit]
archimate_type: "business-object"
grondslag: "procesobject"
ggm_entiteit: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: "Parkeren"
ggm_taakveld: "2 Verkeer, Vervoer en Waterstaat"
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ""
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Parkeerplaats gereserveerd voor houders van een gehandicaptenparkeerkaart, met specifieke inrichting en beheerregime."
gemma_toelichting: "Twee typen: algemene gehandicaptenparkeerplaatsen (voor alle GPK-houders) en individuele (op kenteken, bij specifiek adres). De gemeente heeft een aparte Beleidsregel aanleg gehandicaptenparkeerplaatsen."
gemma_subtypes:
  - naam: "Algemene gehandicaptenparkeerplaats"
    omschrijving: "Beschikbaar voor iedereen met een GPK"
    ggm_entiteit: "Parkeervlak"
    ggm_guid: "EAID_5E5C58AD_1634_4656_A183_EBA00F18F30E"
    ggm_attribuut: "doelgroep"
  - naam: "Individuele gehandicaptenparkeerplaats"
    omschrijving: "Op kenteken, bij woon-/werk-/studieadres, met venstertijden"
    ggm_entiteit: "Parkeervlak"
    ggm_guid: "EAID_5E5C58AD_1634_4656_A183_EBA00F18F30E"
    ggm_attribuut: "doelgroep"
bronnen: [Wiki/Bronsamenvattingen/mobiliteit/uitwerking-toegankelijkheid]
relaties:
  - type: generalisatie
    bedrijfsobject: "[[Parkeervlak]]"
    richting: "naar-dit-BO"
    kardinaliteit: ""
    beschrijving: Gehandicaptenparkeerplaats is een specialisatie van Parkeervlak
  - type: associatie
    bedrijfsobject: "[[Gehandicaptenparkeerkaart]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Mag gebruikt worden door houders van een GPK
  - type: associatie
    bedrijfsobject: "[[Voertuig]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: Individuele gehandicaptenparkeerplaats is gekoppeld aan een kenteken
bedrijfsprocessen: [Gehandicaptenparkeerplaats aanleggen, Gehandicaptenparkeerplaats toewijzen, Parkeerhandhaving]
bedrijfsfuncties: [Parkeerbeleid, Beheer openbare ruimte]
---

# Gehandicaptenparkeerplaats

Parkeerplaats gereserveerd voor houders van een gehandicaptenparkeerkaart, met specifieke inrichting en beheerregime.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — centraal in toegankelijkheidsbeleid, eigen module en beleidsregel
- ✅ Is herkenbaar voor domeinexperts — het blauwe bord met rolstoelsymbool is universeel herkenbaar
- ✅ Heeft een eigen bestaan — fysieke plek met eigen bord, inrichting en beheerproces
- ✅ Kan in meervoud bestaan — honderden in Utrecht (50 met sensoren in proef)
- ✅ Heeft een eigen levenscyclus — aanvraag/initiatief → aanleg → in gebruik → afzakken → opheffen
- ✅ Heeft relaties — GPK, kenteken, sensor, persoon, beleidsregel

## Beschrijving

Een gehandicaptenparkeerplaats is een parkeerplaats gereserveerd voor mensen met een [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/gehandicaptenparkeerkaart|gehandicaptenparkeerkaart (GPK)]]. De gemeente onderscheidt twee typen:

**Algemene gehandicaptenparkeerplaatsen** zijn beschikbaar voor iedereen met een GPK. De gemeente legt deze aan op basis van richtlijnen in de Beleidsregel aanleg gehandicaptenparkeerplaatsen, met aandacht voor aantallen, kwaliteit, spreiding en clustering. Sensoren monitoren de bezetting in realtime.

**Individuele gehandicaptenparkeerplaatsen** zijn op kenteken gereserveerd bij het woon-, werk- of studieadres van de aanvrager. Kenmerken: venstertijden (plek beschikbaar op momenten dat aanvrager wil parkeren), afzakprocedure (bord wordt afgezakt bij langdurig niet-gebruik), maatwerk in inrichting (bijv. uitstapstrook). De aanvrager betaalt een bijdrage in de aanlegkosten.

⚠️ **Ter discussie:** dit BO is een specialisatie van [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervlak|Parkeervlak]]. In het GGM is het een attribuutwaarde (`doelgroep`) op Parkeervlak. De eigen processen, beleidsregel, sensoren en kentekenkoppeling rechtvaardigen een zelfstandig BO.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Algemene gehandicaptenparkeerplaats | Beschikbaar voor alle GPK-houders | [Parkeervlak](Sources/GGM/2-verkeer-vervoer-en-waterstaat/parkeren.md) (doelgroep) |
| Individuele gehandicaptenparkeerplaats | Op kenteken, bij specifiek adres, met venstertijden | [Parkeervlak](Sources/GGM/2-verkeer-vervoer-en-waterstaat/parkeren.md) (doelgroep) |

## GGM-bron

Geen directe GGM-entiteit. Het concept valt onder **Parkeervlak** (EAID_5E5C58AD) als attribuutwaarde van `doelgroep`.

> "Parkeergelegenheid bestemd voor het parkeren van een of meerdere voertuigen direct langs de doorgaande weg gelegen." — GGM, Parkeervlak

**Matchsterkte: partieel** — het GGM modelleert gehandicaptenparkeerplaatsen niet als apart type. De eigen levenscyclus, beleidsregel en relaties (GPK, kenteken, sensor) worden niet gedekt.

## Procesbron

Bron: [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-toegankelijkheid|Uitwerking Parkeren en toegankelijkheid]]

> "Parkeren vormt geen fysieke belemmering voor de toegankelijkheid van bestemmingen in Utrecht voor mensen met een beperking en andere doelgroepen."

> "Daarom moet binnen 100 meter een gehandicaptenparkeerplaats in de openbare ruimte gerealiseerd kunnen worden."

## Relaties

- ↑ [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervlak|Parkeervlak]] — generalisatie (gehandicaptenparkeerplaats is een specialisatie)
- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/gehandicaptenparkeerkaart|Gehandicaptenparkeerkaart]] — GPK geeft recht tot gebruik
- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/voertuig|Voertuig]] — individuele plek gekoppeld aan kenteken

## Terugmelding GGM

> **Gehandicaptenparkeerplaats** — Specialisatie van Parkeervlak met eigen aanvraag-/toewijzingsproces, kentekenkoppeling, venstertijden en sensormonitoring. Het GGM modelleert dit als attribuut `doelgroep` op Parkeervlak, maar de eigen processen rechtvaardigen een apart entiteittype. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
