---
type: bedrijfsobject
naam: Parkeervlak
domein: [mobiliteit]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Parkeervlak"
ggm_guid: EAID_5E5C58AD_1634_4656_A183_EBA00F18F30E
ggm_uml_type: Class
ggm_beleidsdomein: "Parkeren"
ggm_taakveld: "2 Verkeer, Vervoer en Waterstaat"
ggm_diagram: [Model Parkeren]
ggm_diagram_ids: [EAID_84B6B75B_2B58_455d_B019_C9B1E71717C2]
ggm_definitie: "Parkeergelegenheid bestemd voor het parkeren van een of meerdere voertuigen direct langs de doorgaande weg gelegen."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Parkeervlak"
ggm_gemma_guid: "30d7e3ac-081c-4ef6-a09e-90437b5a4349"
ggm_gemma_definitie: "Parkeergelegenheid bestemd voor het parkeren van een of meerdere voertuigen direct langs de doorgaande weg gelegen."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-30d7e3ac-081c-4ef6-a09e-90437b5a4349"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Parkeervlak** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Straatsectie** (classificatie) — Administratieve indeling, geen zelfstandig object
bo_definitie: "Parkeergelegenheid bestemd voor het parkeren van een of meerdere voertuigen direct langs de doorgaande weg gelegen."
bo_toelichting: ''
bedrijfsprocessen: [Parkeerbeleid, Parkeerhandhaving]
bedrijfsfuncties: [Parkeerbeleid]
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[Parkeerzone]]"
    richting: "naar-dit-BO"
    kardinaliteit: 1..1
    beschrijving: Parkeervlak is onderdeel van een parkeerzone
  - type: associatie
    bedrijfsobject: "[[Laadpaal]]"
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: Parkeervlak kan een laadpaal bevatten
---

# Parkeervlak

Parkeergelegenheid bestemd voor het parkeren van een of meerdere voertuigen direct langs de openbare weg.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — kleinste eenheid van parkeercapaciteit in de openbare ruimte
- ✅ Is herkenbaar voor domeinexperts — handhavers en wegbeheerders werken op het niveau van individuele vakken
- ✅ Heeft een eigen bestaan binnen het domein — fysiek afgebakende plek met eigen locatie en type
- ✅ Kan in meervoud bestaan — straatparkeerplaats, gehandicaptenplek, laadplek
- ✅ Heeft een eigen levenscyclus — aanleg, markering, herinrichting (bijv. naar groen of fietsenstalling), opheffing
- ✅ Heeft relaties met andere concepten — onderdeel van parkeerzone, kan een laadpaal bevatten

## Beschrijving

Een parkeervlak is een individuele parkeergelegenheid langs de openbare weg. Het Mobiliteitsplan 2040 beschrijft de transformatie van parkeerplaatsen naar groen en fietsenstalling als onderdeel van de herinrichting van de openbare ruimte. Parkeervlakken worden geregistreerd met locatie, type en eventuele beperkingen.

## GGM-bron

> "Parkeergelegenheid bestemd voor het parkeren van een of meerdere voertuigen direct langs de doorgaande weg gelegen." — GGM, Parkeervlak (EAID_5E5C58AD)

**Matchsterkte: exact.**

## Relaties

- ◆ ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerzone|Parkeerzone]] — parkeervlak is onderdeel van een parkeerzone
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/laadpaal|Laadpaal]] — parkeervlak kan een laadpaal bevatten

## Bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/kwaliteitsnet-goederenvervoer-2007]]
- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]
- [[Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-fiets-2021]]
- [[Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-auto-2021]]
- [[Wiki/Bronsamenvattingen/mobiliteit/module-parkeernormen]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeerhubs]]
- [[Wiki/Bronsamenvattingen/mobiliteit/rapportage-routekaart-parkeerhubs]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-fietsparkeren]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeren-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-toegankelijkheid]]
- [[Wiki/Bronsamenvattingen/mobiliteit/parkeervisie]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitvoeringsprogramma-betaald-parkeren]]
