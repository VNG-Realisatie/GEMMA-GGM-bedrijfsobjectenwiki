---
type: bedrijfsobject
naam: Leerroute
domein: [Asiel en Integratie]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Leerroute"
ggm_guid: EAID_51285531_9529_4b2d_9EC6_B6BAEA729D9A
ggm_uml_type: Class
ggm_beleidsdomein: "Inburgering"
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: [Inburgering, Leerroute]
ggm_diagram_ids: [EAID_96927C60_9F7B_4e67_806A_02EE0191983D, EAID_1B629406_49FC_4622_9F65_EF0B8F33CCF8]
ggm_definitie: "<font color=\"#0e0e0e\">Een </font><font color=\"#0e0e0e\"><b>Leerroute</b></font><font color=\"#0e0e0e\"> is het door de gemeente vastgestelde traject dat een inburgeringsplichtige volgt om te voldoen aan de inburgeringsplicht, bestaande uit taallessen, participatieactiviteiten en aanvullende modules, afgestemd op het leervermogen en het hoofddoel van de inburgeraar.</font> "
ggm_toelichting: "•	De leerroute wordt bepaald op basis van de brede intake en de leerbaarheidstoets, zoals vastgelegd in artikelen 15 en 16 van de Wet inburgering 2021."
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Leerroute"
ggm_gemma_guid: "ab441c2e-d5a6-4546-b1b8-a08d3bee1c07"
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA2/0.9/id-ab441c2e-d5a6-4546-b1b8-a08d3bee1c07"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Het door de gemeente vastgestelde onderwijstraject dat de inburgeraar volgt richting het inburgeringsdiploma."
relaties:
  - type: associatie
    bedrijfsobject: PIP
    richting: "naar-dit-BO"
    kardinaliteit: 1
    beschrijving: Wordt afgesproken in het PIP
  - type: associatie
    bedrijfsobject: MAP
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: Bevat de module arbeidsmarkt en participatie
  - type: associatie
    bedrijfsobject: PVT
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: Bevat het participatieverklaringstraject
  - type: associatie
    bedrijfsobject: Examen
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Wordt afgerond met examens
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

- ← [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pip|pip]] — wordt afgesproken in het PIP [1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/map|map]] — bevat de module arbeidsmarkt en participatie [0..1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pvt|pvt]] — bevat het participatieverklaringstraject [0..1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/examen|examen]] — wordt afgerond met examens [0..*]

## Bronnen

- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer]]
- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/coa-dienstverleningsgids]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-asielopvang]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-inburgering]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-opvang-oekraine]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-rubriek-asiel]]
