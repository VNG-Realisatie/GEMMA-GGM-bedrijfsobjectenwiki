---
type: bedrijfsobject
naam: Naheffing
domein: [mobiliteit]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Naheffing"
ggm_guid: EAID_4957AC99_3F36_4959_A210_9EC6759B87F8
ggm_uml_type: Class
ggm_beleidsdomein: "Parkeren"
ggm_taakveld: "2 Verkeer, Vervoer en Waterstaat"
ggm_diagram: [Model Parkeren]
ggm_diagram_ids: [EAID_84B6B75B_2B58_455d_B019_C9B1E71717C2]
ggm_definitie: "Het achteraf vorderen van te weinig betaalde belasting "
ggm_toelichting: ""
ggm_synoniemen: "Navordering"
ggm_herkomst: ""
ggm_gemma_naam: "Naheffing"
ggm_gemma_guid: "d10d2101-2e16-4f56-bcce-43783fd256be"
ggm_gemma_definitie: "Het achteraf vorderen van te weinig betaalde belasting"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: "Navordering"
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-d10d2101-2e16-4f56-bcce-43783fd256be"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Achteraf vorderen van parkeerbelasting wanneer bij controle geen geldig parkeerrecht wordt aangetroffen."
bedrijfsprocessen: [Parkeerbeleid, Parkeerhandhaving]
bedrijfsfuncties: [Parkeerbeleid]
relaties:
  - type: associatie
    bedrijfsobject: "[[Parkeerscan]]"
    richting: "naar-dit-BO"
    kardinaliteit: 1..1
    beschrijving: Naheffing volgt uit een parkeerscan
---

# Naheffing

Het achteraf vorderen van te weinig betaalde parkeerbelasting.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — financieel handhavingsinstrument bij ontbrekend parkeerrecht
- ✅ Is herkenbaar voor domeinexperts — parkeernaheffing is een vaststaand begrip in gemeentelijke handhaving
- ✅ Heeft een eigen bestaan binnen het domein — beschikking met eigen bedrag, datum en beschikkingsnummer
- ✅ Kan in meervoud bestaan — duizenden naheffingen per jaar per gemeente
- ✅ Heeft een eigen levenscyclus — constatering, oplegging, bezwaar, betaling of invordering
- ✅ Heeft relaties met andere concepten — volgt uit een parkeerscan zonder geldig parkeerrecht

## Beschrijving

Een naheffing is het achteraf vorderen van parkeerbelasting wanneer bij een parkeerscan geen geldig parkeerrecht wordt aangetroffen. De naheffing wordt als beschikking opgelegd aan de kentekenhouder. Ook wel navordering genoemd.

## GGM-bron

> "Het achteraf vorderen van te weinig betaalde belasting" — GGM, Naheffing (EAID_4957AC99)

**Matchsterkte: exact.**

## Relaties

- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerscan|Parkeerscan]] — naheffing volgt uit een parkeerscan

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
