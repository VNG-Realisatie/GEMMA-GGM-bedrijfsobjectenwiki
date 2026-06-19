---
type: bedrijfsobject
naam: PIP
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: PIP
ggm_beleidsdomein: Inburgering
ggm_diagram: Inburgering
ggm_definitie: "Het Persoonlijk Plan Inburgering en Participatie (PIP) is een individueel plan dat door de gemeente wordt vastgesteld in overleg met de inburgeringsplichtige, waarin het leerrouteadvies, het inburgeringsaanbod, het hoofddoel en de begeleidingsafspraken zijn vastgelegd, met als doel het succesvol afronden van de inburgering binnen de gestelde termijn."
gemma_definitie: "gelijk aan GGM"
gerelateerde_begrippen: [inburgering]
relaties:
  - type: associatie
    bedrijfsobject: Brede Intake
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Wordt opgesteld naar aanleiding van de brede intake"
  - type: associatie
    bedrijfsobject: Leerroute
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Bevat de afgesproken leerroute"
  - type: associatie
    bedrijfsobject: Inburgeringstraject
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Stuurt het inburgeringstraject aan"
---

# PIP

Persoonlijk Plan Inburgering en Participatie — individueel plan vastgesteld door de gemeente met de inburgeraar, bevat leerrouteadvies, inburgeringsaanbod, hoofddoel en begeleidingsafspraken.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

> Het Persoonlijk Plan Inburgering en Participatie (PIP) is een individueel plan dat door de gemeente wordt vastgesteld in overleg met de inburgeringsplichtige, waarin het leerrouteadvies, het inburgeringsaanbod, het hoofddoel en de begeleidingsafspraken zijn vastgelegd, met als doel het succesvol afronden van de inburgering binnen de gestelde termijn.

- **Entiteit:** PIP
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** DagtekeningInitielePIP, DagtekeningPIP, NaamContactPersoon, EmailContactPersoon, IndicatorMagOpleidingAfmaken
- **Matchsterkte:** exact

## Relaties

- ← [[brede-intake]] — wordt opgesteld naar aanleiding van de brede intake [1]
- → [[leerroute]] — bevat de afgesproken leerroute [1]
- → [[inburgeringstraject]] — stuurt het inburgeringstraject aan [1]
