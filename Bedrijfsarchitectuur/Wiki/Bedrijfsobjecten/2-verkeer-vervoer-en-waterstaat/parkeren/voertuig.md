---
type: bedrijfsobject
naam: Voertuig
domein: [mobiliteit]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Voertuig"
ggm_guid: EAID_6AD98160_FFE6_4105_A724_5D5733C87CD8
ggm_uml_type: Class
ggm_beleidsdomein: "Parkeren"
ggm_taakveld: "2 Verkeer, Vervoer en Waterstaat"
ggm_diagram: [Objecten bij Vergunningaanvraag, Model Parkeren]
ggm_diagram_ids: [EAID_C9CE09B7_32EF_40eb_9C82_7FD6EDEA1D9E, EAID_84B6B75B_2B58_455d_B019_C9B1E71717C2]
ggm_definitie: "Vervoermiddel bestemd voor het verkeer over wegen"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Voertuig"
ggm_gemma_guid: "b083bd60-0137-40b0-ad72-4602b3c1d754"
ggm_gemma_definitie: "Vervoermiddel bestemd voor het verkeer over wegen"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-b083bd60-0137-40b0-ad72-4602b3c1d754"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Vervoermiddel bestemd voor het wegverkeer, in de parkeercontext geïdentificeerd door kenteken."
bedrijfsprocessen: [Parkeerbeleid, Parkeerhandhaving]
bedrijfsfuncties: [Parkeerbeleid]
relaties:
  - type: associatie
    bedrijfsobject: "[[Parkeerrecht]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Voertuig heeft parkeerrechten
  - type: associatie
    bedrijfsobject: "[[Parkeerscan]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Voertuig wordt waargenomen door parkeerscan
---

# Voertuig

Vervoermiddel bestemd voor het verkeer over wegen.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — het voertuig is het object waaraan parkeerrechten worden gekoppeld
- ✅ Is herkenbaar voor domeinexperts — kenteken is de primaire identificatie bij handhaving
- ✅ Heeft een eigen bestaan binnen het domein — geidentificeerd door kenteken, onafhankelijk van eigenaar of parkeeractie
- ✅ Kan in meervoud bestaan — personenauto, bestelbus, vrachtwagen
- ✅ Heeft een eigen levenscyclus — registratie (RDW), kentekenwijziging, uitschrijving
- ✅ Heeft relaties met andere concepten — gekoppeld aan parkeerrechten, waargenomen door parkeerscan

## Beschrijving

Een voertuig is een vervoermiddel bestemd voor het verkeer over wegen. In de context van parkeren is het voertuig het object waaraan parkeerrechten en -vergunningen worden gekoppeld via het kenteken. Het Mobiliteitsplan 2040 maakt het onderscheid tussen elektrische en fossiele voertuigen steeds relevanter voor parkeerbeleid.

## GGM-bron

> "Vervoermiddel bestemd voor het verkeer over wegen" — GGM, Voertuig (EAID_6AD98160)

**Matchsterkte: exact.**

## Relaties

- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerrecht|Parkeerrecht]] — voertuig heeft parkeerrechten
- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerscan|Parkeerscan]] — voertuig wordt waargenomen door parkeerscan

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
