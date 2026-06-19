---
type: bedrijfsobject
naam: Brede Intake
domein: [Asiel en Integratie]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Brede Intake
ggm_beleidsdomein: Inburgering
ggm_diagram: Inburgering
ggm_definitie: "De Brede Intake in het sociaal domein is een gestructureerd proces waarbij een hulpverlener samen met een inwoner diens situatie, behoeften, en problemen in kaart brengt om tot een integraal beeld te komen van wat nodig is om passende ondersteuning te bieden. Hierbij wordt niet alleen gekeken naar specifieke hulpvragen, zoals schulden of werkloosheid, maar ook naar onderliggende factoren, zoals gezondheidsproblemen, woonsituatie, en sociaal netwerk. Het doel is om vanuit een holistisch perspectief samenhangende oplossingen te vinden en de inwoner te ondersteunen bij het versterken van zelfredzaamheid en participatie."
gemma_definitie: "gelijk aan GGM"
gerelateerde_begrippen: [inburgering]
relaties:
  - type: associatie
    bedrijfsobject: Asielstatushouder
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Asielstatushouder doorloopt een brede intake"
  - type: associatie
    bedrijfsobject: Gezinsmigrant
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Gezinsmigrant doorloopt een brede intake"
  - type: associatie
    bedrijfsobject: PIP
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Resulteert in een PIP"
---

# Brede Intake

Gestructureerd proces waarbij de gemeente samen met de inburgeraar diens situatie, behoeften en problemen in kaart brengt voor een integraal beeld en passende ondersteuning.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

> De Brede Intake in het sociaal domein is een gestructureerd proces waarbij een hulpverlener samen met een inwoner diens situatie, behoeften, en problemen in kaart brengt om tot een integraal beeld te komen van wat nodig is om passende ondersteuning te bieden. Hierbij wordt niet alleen gekeken naar specifieke hulpvragen, zoals schulden of werkloosheid, maar ook naar onderliggende factoren, zoals gezondheidsproblemen, woonsituatie, en sociaal netwerk. Het doel is om vanuit een holistisch perspectief samenhangende oplossingen te vinden en de inwoner te ondersteunen bij het versterken van zelfredzaamheid en participatie.

- **Entiteit:** Brede Intake
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** GevolgdeUrenKNMenTaalles, UrenGeoorloofdVerzuim, UrenOngeoorloofdVerzuim, DatumTot(Peildatum), AantalUrenAlfabetiseringsOnderwijs, startdatum, einddatum
- **Matchsterkte:** exact

## Relaties

- ← [[asielstatushouder]] / [[gezinsmigrant]] — inburgeraar doorloopt een brede intake [1]
- → [[pip]] — resulteert in een PIP [1]
