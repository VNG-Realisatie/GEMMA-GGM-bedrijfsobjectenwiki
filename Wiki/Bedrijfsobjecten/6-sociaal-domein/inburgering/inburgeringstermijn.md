---
type: bedrijfsobject
naam: Inburgeringstermijn
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Inburgeringstermijn
ggm_beleidsdomein: Inburgering
ggm_diagram: Inburgering
ggm_definitie: "De Inburgeringstermijn is de wettelijke periode waarbinnen een inburgeringsplichtige moet voldoen aan de inburgeringsplicht, gerekend vanaf de startdatum van de verplichting zoals vastgesteld door DUO of de gemeente."
gemma_definitie: "gelijk aan GGM"
gerelateerde_begrippen: [inburgering]
relaties:
  - type: associatie
    bedrijfsobject: Inburgeringsplicht
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Inburgeringsplicht heeft een termijn"
---

# Inburgeringstermijn

De wettelijke periode waarbinnen een inburgeringsplichtige moet voldoen aan de inburgeringsplicht, inclusief eventuele verlengingen en boetebevoegdheid.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

Aanvraag verlenging is een processtap, geen apart bedrijfsobject. Het GGM modelleert "Aanvraag verlenging Inburgeringstermijn" als aparte entiteit, maar op bedrijfsniveau is het een gebeurtenis in de levenscyclus van de inburgeringstermijn.

## GGM-bron

> De Inburgeringstermijn is de wettelijke periode waarbinnen een inburgeringsplichtige moet voldoen aan de inburgeringsplicht, gerekend vanaf de startdatum van de verplichting zoals vastgesteld door DUO of de gemeente.

- **Entiteit:** Inburgeringstermijn
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** DatumAanvangInburgeringstermijn, DatumEindeInburgeringstermijn, VooraankondigingBoete, BoeteBedrag, DatumBoete
- **Matchsterkte:** exact

## Relaties

- ← [[inburgeringsplicht]] — inburgeringsplicht heeft een termijn [1]
