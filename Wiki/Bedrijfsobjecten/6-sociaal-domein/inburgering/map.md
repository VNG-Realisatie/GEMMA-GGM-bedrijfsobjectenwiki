---
type: bedrijfsobject
naam: MAP
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: MAP
ggm_beleidsdomein: Inburgering
ggm_diagram: Inburgering
ggm_definitie: "De Module Arbeidsmarkt en Participatie (MAP) is een verplicht onderdeel van het inburgeringstraject waarin de inburgeringsplichtige wordt voorbereid op deelname aan de Nederlandse arbeidsmarkt, door middel van voorlichting, orientatie en arbeidsmarktgerichte activiteiten."
gemma_definitie: "gelijk aan GGM"
gerelateerde_begrippen: [inburgering]
relaties:
  - type: associatie
    bedrijfsobject: Leerroute
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Is onderdeel van de leerroute"
---

# MAP

Module Arbeidsmarkt en Participatie — verplicht onderdeel van het inburgeringstraject waarin de inburgeraar wordt voorbereid op deelname aan de arbeidsmarkt.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

> De Module Arbeidsmarkt en Participatie (MAP) is een verplicht onderdeel van het inburgeringstraject waarin de inburgeringsplichtige wordt voorbereid op deelname aan de Nederlandse arbeidsmarkt, door middel van voorlichting, orientatie en arbeidsmarktgerichte activiteiten.

- **Entiteit:** MAP
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** Resultaat, DatumEindgesprekMAP, RedenNietSuccesvolVoltooid, IndicatorVerwijtbaar
- **Matchsterkte:** exact

## Relaties

- ← [[leerroute]] — is onderdeel van de leerroute [1]
