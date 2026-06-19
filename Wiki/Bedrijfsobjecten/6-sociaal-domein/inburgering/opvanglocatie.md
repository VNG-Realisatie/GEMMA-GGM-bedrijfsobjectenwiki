---
type: bedrijfsobject
naam: Opvanglocatie
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: procesobject
ggm_entiteit: ""
ggm_beleidsdomein: ""
ggm_diagram: ""
ggm_definitie:
gemma_definitie: "Fysieke locatie voor opvang van asielzoekers of ontheemden, in diverse vormen en schaalgroottes, door gemeente gefaciliteerd of geexploiteerd."
gerelateerde_begrippen: [opvanglocatie, asielopvang, duurzame-gemeentelijke-opvang, spreidingswet]
relaties:
  - type: associatie
    bedrijfsobject: Bestuursovereenkomst
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Wordt geregeld door een bestuursovereenkomst met het COA"
---

# Opvanglocatie

Fysieke locatie voor opvang van asielzoekers of ontheemden, in diverse vormen en schaalgroottes, door gemeente gefaciliteerd of geexploiteerd.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

Geen GGM-match. Asielopvang is structureel niet gemodelleerd in het GGM. Het beleidsdomein Inburgering begint pas bij de inburgeringsplicht; de opvangfase die daaraan voorafgaat valt buiten scope. Dit is een hiaat dat als terugmelding aan het GGM kan worden voorgelegd.

## Relaties

- → [[bestuursovereenkomst]] — wordt geregeld door een bestuursovereenkomst met het COA [0..1]
