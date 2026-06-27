---
type: bedrijfsobject
naam: Examen
domein:
- Asiel en Integratie
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Examen
ggm_guid: EAID_DCE46ABA_613D_4204_86F4_35F517FF680F
ggm_uml_type: Class
ggm_beleidsdomein: Inburgering
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- Inburgering
ggm_diagram_ids:
- EAID_96927C60_9F7B_4e67_806A_02EE0191983D
ggm_definitie: Een Examen in de context van onderwijs is een formele toetsingsactiviteit waarmee de kennis, vaardigheden en competenties van een leerling of student worden beoordeeld ten opzichte van vooraf
  vastgestelde leerdoelen of eindtermen. Het examen kan schriftelijk, mondeling, digitaal of praktijkgericht zijn en vormt doorgaans een afsluiting van een cursus, module of opleiding. Het behalen van een
  examen kan leiden tot het verkrijgen van een diploma, certificaat of overgangsbewijs en is bedoeld om de voortgang en geschiktheid voor verdere studie of beroep te waarborgen.
ggm_toelichting: ''
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: Examen
ggm_gemma_guid: ccce5500-2140-4928-9716-0132a31e9686
ggm_gemma_definitie: ''
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-ccce5500-2140-4928-9716-0132a31e9686
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
bo_definitie: Formele toets waarmee een inburgeraar aantoont te voldoen aan de eisen van de Wet inburgering.
bo_toelichting: ''
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringstraject|Inburgeringstraject]]'
  richting: naar-dit-BO
  kardinaliteit: 1
  beschrijving: Inburgeringstraject wordt afgesloten met examens
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/leerroute|Leerroute]]'
  richting: naar-dit-BO
  kardinaliteit: 1
  beschrijving: Leerroute wordt afgerond met examens
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

## BO-definitie

De GGM-definitie beschrijft een generiek onderwijsexamen ("leerling of student", "cursus, module of opleiding"). Dit BO betreft specifiek het inburgeringsexamen onder de Wet inburgering 2021, afgelegd door inburgeraars bij DUO.

## Relaties

- ← [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringstraject|inburgeringstraject]] — inburgeringstraject wordt afgesloten met examens [1]
- ← [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/leerroute|leerroute]] — leerroute wordt afgerond met examens [1]

## Bronnen

- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer]]
- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/coa-dienstverleningsgids]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-asielopvang]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-inburgering]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-opvang-oekraine]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-rubriek-asiel]]
