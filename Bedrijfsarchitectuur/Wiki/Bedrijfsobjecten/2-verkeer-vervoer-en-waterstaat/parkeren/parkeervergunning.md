---
type: bedrijfsobject
naam: Parkeervergunning
domein: [mobiliteit]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Parkeervergunning"
ggm_guid: EAID_FF448272_AB9D_4ec9_B4BE_E60E2552817A
ggm_uml_type: Class
ggm_beleidsdomein: "Parkeren"
ggm_taakveld: "2 Verkeer, Vervoer en Waterstaat"
ggm_diagram: [Model Parkeren]
ggm_diagram_ids: [EAID_84B6B75B_2B58_455d_B019_C9B1E71717C2]
ggm_definitie: "Officiele toestemming dat je op een bepaalde plek mag parkeren"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Parkeervergunning"
ggm_gemma_guid: "1486de79-ad71-4dce-8473-f23f1e9c436c"
ggm_gemma_definitie: "Officiele toestemming dat je op een bepaalde plek mag parkeren"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-1486de79-ad71-4dce-8473-f23f1e9c436c"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Door de gemeente verleende toestemming om op een bepaalde locatie of in een bepaalde zone te parkeren."
bedrijfsprocessen: [Parkeerbeleid, Parkeerhandhaving]
bedrijfsfuncties: [Parkeerbeleid]
relaties:
  - type: generalisatie
    bedrijfsobject: "[[Vergunningen en ontheffingen]]"
    richting: van-dit-BO
    kardinaliteit: ""
    beschrijving: Parkeervergunning is een specialisatie van Vergunningen en ontheffingen
  - type: associatie
    bedrijfsobject: "[[Parkeerzone]]"
    richting: "van-dit-BO"
    kardinaliteit: 1..1
    beschrijving: Parkeervergunning geldt binnen een parkeerzone
  - type: associatie
    bedrijfsobject: "[[Parkeerrecht]]"
    richting: "van-dit-BO"
    kardinaliteit: 1..1
    beschrijving: Parkeervergunning verleent een parkeerrecht
  - type: associatie
    bedrijfsobject: "[[Voertuig]]"
    richting: "van-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: Parkeervergunning is gekoppeld aan een voertuig
---

# Parkeervergunning

Officiele toestemming dat je op een bepaalde plek mag parkeren.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — juridisch instrument waarmee de gemeente parkeertoegang regelt
- ✅ Is herkenbaar voor domeinexperts — bewonersvergunning en bezoekersvergunning zijn dagelijkse begrippen
- ✅ Heeft een eigen bestaan binnen het domein — document met eigen kenmerken (zone, geldigheid, voertuig)
- ✅ Kan in meervoud bestaan — bewonersvergunning, bezoekersvergunning, bedrijfsvergunning
- ✅ Heeft een eigen levenscyclus — aanvraag, verlening, verlenging, intrekking
- ✅ Heeft relaties met andere concepten — geldt binnen een parkeerzone, verleent een parkeerrecht, gekoppeld aan voertuig

## Beschrijving

Een parkeervergunning is een officiele toestemming om op een bepaalde plek te parkeren. Het Mobiliteitsplan 2040 noemt bewonersvergunningen en benoemt deelmobiliteitsvergunningen als nieuw type. De vergunning is altijd gebonden aan een specifieke zone en een of meer voertuigen.

## GGM-bron

> "Officiele toestemming dat je op een bepaalde plek mag parkeren" — GGM, Parkeervergunning (EAID_FF448272)

**Matchsterkte: exact.**

## Relaties

- ↑ [[Vergunningen en ontheffingen]] — specialisatie
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerzone|Parkeerzone]] — parkeervergunning geldt binnen een parkeerzone
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerrecht|Parkeerrecht]] — parkeervergunning verleent een parkeerrecht
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/voertuig|Voertuig]] — parkeervergunning is gekoppeld aan een voertuig

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
