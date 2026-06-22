---
type: bedrijfsobject
naam: Parkeergarage
domein: [mobiliteit]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Parkeergarage"
ggm_guid: EAID_8F492648_6EF2_4f8a_87C9_2440230D4137
ggm_uml_type: Class
ggm_beleidsdomein: "Parkeren"
ggm_taakveld: "2 Verkeer, Vervoer en Waterstaat"
ggm_diagram: [Model Parkeren]
ggm_diagram_ids: [EAID_84B6B75B_2B58_455d_B019_C9B1E71717C2]
ggm_definitie: "Open constructie die geheel of gedeeltelijk in gebruik is als voorziening voor het parkeren van voertuigen"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Parkeergarage"
ggm_gemma_guid: "3aed2196-8ba9-4441-a27f-15a1f76d3fda"
ggm_gemma_definitie: "Open constructie die geheel of gedeeltelijk in gebruik is als voorziening voor het parkeren van voertuigen"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-3aed2196-8ba9-4441-a27f-15a1f76d3fda"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Constructie bestemd voor het parkeren van voertuigen, al dan niet in gemeentelijk eigendom of beheer."
bedrijfsprocessen: [Parkeerbeleid, Parkeerhandhaving]
bedrijfsfuncties: [Parkeerbeleid]
bronnen: [Wiki/Bronsamenvattingen/mobiliteit/kwaliteitsnet-goederenvervoer-2007, Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040, Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-fiets-2021, Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-auto-2021, Wiki/Bronsamenvattingen/mobiliteit/module-parkeernormen, Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeerhubs, Wiki/Bronsamenvattingen/mobiliteit/rapportage-routekaart-parkeerhubs, Wiki/Bronsamenvattingen/mobiliteit/uitwerking-fietsparkeren, Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeren-openbare-ruimte, Wiki/Bronsamenvattingen/mobiliteit/uitwerking-toegankelijkheid, Wiki/Bronsamenvattingen/mobiliteit/parkeervisie, Wiki/Bronsamenvattingen/mobiliteit/uitvoeringsprogramma-betaald-parkeren]
relaties:
  - type: generalisatie
    bedrijfsobject: "[[Parkeerzone]]"
    richting: "van-dit-BO"
    kardinaliteit: 
    beschrijving: Parkeergarage is specialisatie van Parkeerzone
  - type: associatie
    bedrijfsobject: "[[P+R-locatie]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Parkeergarage kan fungeren als P+R-locatie"
---

# Parkeergarage

Open constructie die geheel of gedeeltelijk in gebruik is als voorziening voor het parkeren van voertuigen.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — fysieke parkeervoorziening met eigen capaciteit en exploitatie
- ✅ Is herkenbaar voor domeinexperts — beleidsmakers en exploitanten kennen elke garage bij naam
- ✅ Heeft een eigen bestaan binnen het domein — gebouw met eigen locatie, capaciteit en tariefsysteem
- ✅ Kan in meervoud bestaan — Jaarbeurs, Springweg, P+R Westraven
- ✅ Heeft een eigen levenscyclus — planning, bouw, exploitatie, renovatie, sloop
- ✅ Heeft relaties met andere concepten — specialisatie van parkeerzone, kan fungeren als P+R-locatie

## Beschrijving

Een parkeergarage is een constructie bestemd voor het parkeren van voertuigen. Het Mobiliteitsplan 2040 noemt binnenstadsgarages en P+R-garages als onderdeel van de parkeerstrategie. Garages hebben eigen tarieven, openingstijden en een vastgestelde capaciteit.

## GGM-bron

> "Open constructie die geheel of gedeeltelijk in gebruik is als voorziening voor het parkeren van voertuigen" — GGM, Parkeergarage (EAID_8F492648)

**Matchsterkte: exact.**

## Relaties

- ▲ → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerzone|Parkeerzone]] — parkeergarage is specialisatie van parkeerzone
- → [[P+R-locatie]] — parkeergarage kan fungeren als P+R-locatie
