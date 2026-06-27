---
type: bedrijfsobject
naam: Parkeerscan
domein: [mobiliteit]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Parkeerscan"
ggm_guid: EAID_653EEEA7_ED82_427d_BD72_86C847793AD6
ggm_uml_type: Class
ggm_beleidsdomein: "Parkeren"
ggm_taakveld: "2 Verkeer, Vervoer en Waterstaat"
ggm_diagram: [Model Parkeren]
ggm_diagram_ids: [EAID_84B6B75B_2B58_455d_B019_C9B1E71717C2]
ggm_definitie: "Waarneming van een parkeeractie door een scanauto"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Parkeerscan"
ggm_gemma_guid: "078d57f3-e8a0-485e-a175-c1b3de49eee0"
ggm_gemma_definitie: "Waarneming van een parkeeractie door een scanauto"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-078d57f3-e8a0-485e-a175-c1b3de49eee0"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
bo_definitie: "Waarneming van een parkeeractie door een scanauto"
bo_toelichting: ''
bedrijfsprocessen: [Parkeerbeleid, Parkeerhandhaving]
bedrijfsfuncties: [Parkeerbeleid]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Parkeervlak]]"
    richting: "van-dit-BO"
    kardinaliteit: 1..1
    beschrijving: Parkeerscan registreert een voertuig op een parkeervlak
  - type: associatie
    bedrijfsobject: "[[Voertuig]]"
    richting: "van-dit-BO"
    kardinaliteit: 1..1
    beschrijving: Parkeerscan betreft een voertuig
  - type: associatie
    bedrijfsobject: "[[Parkeerrecht]]"
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: Parkeerscan wordt getoetst aan een parkeerrecht
  - type: associatie
    bedrijfsobject: "[[Naheffing]]"
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: Parkeerscan kan leiden tot een naheffing
---

# Parkeerscan

Waarneming van een parkeeractie door een scanauto.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — basis voor geautomatiseerde parkeerhandhaving
- ✅ Is herkenbaar voor domeinexperts — scanauto's en scanresultaten zijn dagelijkse praktijk bij handhaving
- ✅ Heeft een eigen bestaan binnen het domein — individueel scanresultaat met tijdstip, locatie en kenteken
- ✅ Kan in meervoud bestaan — duizenden scans per dag per gemeente
- ✅ Heeft een eigen levenscyclus — scanmoment, toetsing aan parkeerrecht, afhandeling (geldig of naheffing)
- ✅ Heeft relaties met andere concepten — betreft een voertuig op een parkeervlak, toetst aan parkeerrecht, kan leiden tot naheffing

## Beschrijving

Een parkeerscan is een waarneming van een geparkeerd voertuig door een scanauto. De scan legt kenteken, locatie en tijdstip vast. Het resultaat wordt getoetst aan het parkeerrecht; bij ontbreken van een geldig recht kan een naheffing volgen.

## GGM-bron

> "Waarneming van een parkeeractie door een scanauto" — GGM, Parkeerscan (EAID_653EEEA7)

**Matchsterkte: exact.**

## Relaties

- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervlak|Parkeervlak]] — parkeerscan registreert een voertuig op een parkeervlak
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/voertuig|Voertuig]] — parkeerscan betreft een voertuig
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerrecht|Parkeerrecht]] — parkeerscan wordt getoetst aan een parkeerrecht
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/naheffing|Naheffing]] — parkeerscan kan leiden tot een naheffing

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
