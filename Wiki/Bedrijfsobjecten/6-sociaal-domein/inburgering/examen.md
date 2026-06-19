---
type: bedrijfsobject
naam: Examen
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Examen
ggm_beleidsdomein: Inburgering
ggm_diagram: Inburgering
ggm_definitie: "Een Examen in de context van onderwijs is een formele toetsingsactiviteit waarmee de kennis, vaardigheden en competenties van een leerling of student worden beoordeeld ten opzichte van vooraf vastgestelde leerdoelen of eindtermen. Het examen kan schriftelijk, mondeling, digitaal of praktijkgericht zijn en vormt doorgaans een afsluiting van een cursus, module of opleiding. Het behalen van een examen kan leiden tot het verkrijgen van een diploma, certificaat of overgangsbewijs en is bedoeld om de voortgang en geschiktheid voor verdere studie of beroep te waarborgen."
gemma_definitie: "gelijk aan GGM"
gerelateerde_begrippen: [inburgering]
relaties:
  - type: associatie
    bedrijfsobject: Inburgeringstraject
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Inburgeringstraject wordt afgesloten met examens"
  - type: associatie
    bedrijfsobject: Leerroute
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Leerroute wordt afgerond met examens"
---

# Examen

Formele toetsing waarmee kennis, vaardigheden en competenties van de inburgeraar worden beoordeeld ten opzichte van de inburgeringseisen.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

Examenonderdeel is detail/classificatie van dit BO, geen apart bedrijfsobject. Het GGM modelleert Examenonderdeel als aparte entiteit met attributen als ExamenOnderdeelSpecificatie en Resultaat, maar op bedrijfsniveau is het onderscheid niet relevant — de gemeente volgt examens, niet individuele onderdelen.

## GGM-bron

> Een Examen in de context van onderwijs is een formele toetsingsactiviteit waarmee de kennis, vaardigheden en competenties van een leerling of student worden beoordeeld ten opzichte van vooraf vastgestelde leerdoelen of eindtermen. Het examen kan schriftelijk, mondeling, digitaal of praktijkgericht zijn en vormt doorgaans een afsluiting van een cursus, module of opleiding. Het behalen van een examen kan leiden tot het verkrijgen van een diploma, certificaat of overgangsbewijs en is bedoeld om de voortgang en geschiktheid voor verdere studie of beroep te waarborgen.

- **Entiteit:** Examen
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** ExamenResultaat
- **Matchsterkte:** exact

## Relaties

- ← [[inburgeringstraject]] — inburgeringstraject wordt afgesloten met examens [1]
- ← [[leerroute]] — leerroute wordt afgerond met examens [1]
