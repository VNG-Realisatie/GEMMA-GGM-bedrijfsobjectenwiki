---
type: bedrijfsobject
naam: Inburgeringsaanbod
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: InburgeringsAanbod
ggm_beleidsdomein: Inburgering
ggm_diagram: Inburgering
ggm_definitie: "Het Inburgeringsaanbod is het geheel van activiteiten, voorzieningen en ondersteuning dat door de gemeente wordt aangeboden aan de inburgeringsplichtige om de inburgeringsdoelen te behalen, zoals vastgelegd in het persoonlijk plan inburgering en participatie (PIP)."
gemma_definitie: "gelijk aan GGM"
gerelateerde_begrippen: [inburgering]
relaties:
  - type: associatie
    bedrijfsobject: PIP
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "PIP bevat het inburgeringsaanbod"
  - type: associatie
    bedrijfsobject: Leerroute
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Wordt geconcretiseerd in een leerroute"
---

# Inburgeringsaanbod

Het geheel van activiteiten, voorzieningen en ondersteuning dat door de gemeente wordt aangeboden aan de inburgeringsplichtige om de inburgeringsdoelen te behalen.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

> Het Inburgeringsaanbod is het geheel van activiteiten, voorzieningen en ondersteuning dat door de gemeente wordt aangeboden aan de inburgeringsplichtige om de inburgeringsdoelen te behalen, zoals vastgelegd in het persoonlijk plan inburgering en participatie (PIP).

- **Entiteit:** InburgeringsAanbod
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** DatumInburgeringsAanbod, DatumAanvangTaalschakelTraject, DatumEindeCursus, CursusInstelling, IndicatorAlfabetisering, TaalschakelTraject, DatumTaalschakelDiploma, ParticipatieDeelname, ContractId
- **Matchsterkte:** exact

## Relaties

- ← [[pip]] — PIP bevat het inburgeringsaanbod [1]
- → [[leerroute]] — wordt geconcretiseerd in een leerroute [1]
