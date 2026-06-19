---
type: bedrijfsobject
naam: Voorbereiding op Inburgering
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Voorbereiding op Inburgering
ggm_beleidsdomein: Inburgering
ggm_diagram: Inburgering
ggm_definitie: "Voorbereiding op inburgering omvat de activiteiten die worden aangeboden aan asielstatushouders voor de start van de formele inburgeringsplicht, gericht op orientatie op de Nederlandse samenleving, taal en het inburgeringsstelsel."
gemma_definitie: "gelijk aan GGM"
gerelateerde_begrippen: [voorinburgering]
relaties:
  - type: associatie
    bedrijfsobject: Asielstatushouder
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Asielstatushouder neemt deel aan voorbereiding op inburgering"
---

# Voorbereiding op Inburgering

Activiteiten aangeboden aan asielstatushouders voor de start van de formele inburgeringsplicht, gericht op orientatie op de Nederlandse samenleving en het inburgeringsstelsel.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

> Voorbereiding op inburgering omvat de activiteiten die worden aangeboden aan asielstatushouders voor de start van de formele inburgeringsplicht, gericht op orientatie op de Nederlandse samenleving, taal en het inburgeringsstelsel.

- **Entiteit:** Voorbereiding op Inburgering
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** InstemmingDeelnameVoorinburgering, DatumInstemming, Reden
- **Matchsterkte:** exact

## Relaties

- ← [[asielstatushouder]] — asielstatushouder neemt deel aan voorbereiding op inburgering [1]
