---
type: bedrijfsobject
naam: Leerroute
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Leerroute
ggm_beleidsdomein: Inburgering
ggm_diagram: Inburgering
ggm_definitie: "Een Leerroute is het door de gemeente vastgestelde traject dat een inburgeringsplichtige volgt om te voldoen aan de inburgeringsplicht, bestaande uit taallessen, participatieactiviteiten en aanvullende modules, afgestemd op het leervermogen en het hoofddoel van de inburgeraar."
gemma_definitie: "gelijk aan GGM"
gerelateerde_begrippen: [inburgering]
relaties:
  - type: associatie
    bedrijfsobject: PIP
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Wordt afgesproken in het PIP"
  - type: associatie
    bedrijfsobject: MAP
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Bevat de module arbeidsmarkt en participatie"
  - type: associatie
    bedrijfsobject: PVT
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Bevat het participatieverklaringstraject"
  - type: associatie
    bedrijfsobject: Examen
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Wordt afgerond met examens"
---

# Leerroute

Het door de gemeente vastgestelde traject dat een inburgeringsplichtige volgt om te voldoen aan de inburgeringsplicht, bestaande uit taallessen, participatieactiviteiten en modules (MAP, PVT).

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

B1-route en Z-route zijn classificaties van dit BO, geen aparte bedrijfsobjecten. Het GGM modelleert ze als aparte entiteiten maar op bedrijfsniveau is het onderscheid een attribuut (LeerrouteType) van Leerroute.

## GGM-bron

> Een Leerroute is het door de gemeente vastgestelde traject dat een inburgeringsplichtige volgt om te voldoen aan de inburgeringsplicht, bestaande uit taallessen, participatieactiviteiten en aanvullende modules, afgestemd op het leervermogen en het hoofddoel van de inburgeraar.

- **Entiteit:** Leerroute
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** LeerrouteType, Niveau, GeschatteIntensiteitB1Route, IndicatorAlfabetisering, IndicatorToestemmingExamenA2, IndicatorMagOpleidingAfmaken, geenLeerbaarheidstoetsZB, ExamenA2
- **Matchsterkte:** exact

## Relaties

- ← [[pip]] — wordt afgesproken in het PIP [1]
- → [[map]] — bevat de module arbeidsmarkt en participatie [0..1]
- → [[pvt]] — bevat het participatieverklaringstraject [0..1]
- → [[examen]] — wordt afgerond met examens [0..*]
