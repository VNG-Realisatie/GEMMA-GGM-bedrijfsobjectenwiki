---
type: bedrijfsobject
naam: Bestuursovereenkomst
domein: [Asiel en Integratie]
archimate_type: contract
grondslag: governance-object
ggm_entiteit: ""
ggm_beleidsdomein: ""
ggm_diagram: ""
ggm_definitie:
gemma_definitie: "Formele overeenkomst tussen gemeente en COA over de exploitatie, financiering en verantwoordelijkheden bij een specifieke opvanglocatie."
gerelateerde_begrippen: [bestuursovereenkomst, asielopvang]
relaties:
  - type: associatie
    bedrijfsobject: Opvanglocatie
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Regelt de afspraken voor een opvanglocatie"
---

# Bestuursovereenkomst

Formele overeenkomst tussen gemeente en COA over de exploitatie, financiering en verantwoordelijkheden bij een specifieke opvanglocatie.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

Geen GGM-match. Governance-objecten vallen structureel buiten GGM-scope. Het GGM modelleert data-objecten, niet juridische kaders of overeenkomsten tussen bestuursorganen. Dit is geen incidenteel hiaat maar een structureel patroon (zie [[ggm-dekkingspatroon]]).

## Relaties

- ← [[opvanglocatie]] — regelt de afspraken voor een opvanglocatie [1]
