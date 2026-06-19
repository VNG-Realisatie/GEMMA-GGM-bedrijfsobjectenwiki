---
type: bedrijfsobject
naam: Inburgeringsplicht
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Inburgeringsplicht
ggm_beleidsdomein: Inburgering
ggm_diagram: Inburgering
ggm_definitie: "Bevat de uitkomst Leerbaarheidstoets dat een groot deel van de leerroutes bepaalt. Bevat mogelijk ook de Examenresultaten (nog toe te voegen als Ja). Dit zijn DUO berichten (Opvragen en per API beschikbaar stellen aan deze Entiteit/Attributen."
gemma_definitie: "De formele wettelijke verplichting van een inburgeraar om binnen de gestelde termijn te voldoen aan de eisen van de Wet inburgering 2021."
gerelateerde_begrippen: [inburgering]
relaties:
  - type: associatie
    bedrijfsobject: Asielstatushouder
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Asielstatushouder heeft een inburgeringsplicht"
  - type: associatie
    bedrijfsobject: Gezinsmigrant
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Gezinsmigrant heeft een inburgeringsplicht"
  - type: associatie
    bedrijfsobject: Inburgeringstermijn
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Heeft een inburgeringstermijn"
---

# Inburgeringsplicht

De formele wettelijke verplichting van een inburgeraar om binnen de gestelde termijn te voldoen aan de eisen van de Wet inburgering 2021.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

Ontheffing en Vrijstelling zijn attributen/statuswijzigingen van dit BO, geen aparte bedrijfsobjecten. Het GGM modelleert ze als aparte entiteiten met relaties naar Inburgeringsplicht, maar op bedrijfsniveau zijn ze statussen binnen de levenscyclus van de inburgeringsplicht.

## GGM-bron

> Bevat de uitkomst Leerbaarheidstoets dat een groot deel van de leerroutes bepaalt. Bevat mogelijk ook de Examenresultaten (nog toe te voegen als Ja). Dit zijn DUO berichten (Opvragen en per API beschikbaar stellen aan deze Entiteit/Attributen.

- **Entiteit:** Inburgeringsplicht
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** IndicatorInburgeringsplicht, UitkomstLeerbaarheidstoets, BeschikkingVoldaanInburgeringsplicht, V-nummer, InburgeraarSpecialisatie, DatumStart, DatumEind, RedenGeenInburgeringsplicht, DatumGewijzigdInburgeringsplicht, WordtBehandelsAls, DatumGewijzigdWordtBehandeldAls
- **Matchsterkte:** exact

## Relaties

- ← [[asielstatushouder]] / [[gezinsmigrant]] — inburgeraar heeft een inburgeringsplicht [1]
- → [[inburgeringstermijn]] — heeft een inburgeringstermijn [1]
