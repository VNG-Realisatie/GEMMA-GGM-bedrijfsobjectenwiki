---
type: bedrijfsobject
naam: Brede Intake
domein: [Asiel en Integratie]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Brede Intake"
ggm_guid: EAID_8B394DCE_C3C4_4262_9460_8EF130E90D83
ggm_uml_type: Class
ggm_beleidsdomein: "Inburgering"
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: [Inburgering]
ggm_diagram_ids: [EAID_96927C60_9F7B_4e67_806A_02EE0191983D]
ggm_definitie: "De Brede Intake in het sociaal domein is een gestructureerd proces waarbij een hulpverlener samen met een inwoner diens situatie, behoeften, en problemen in kaart brengt om tot een integraal beeld te komen van wat nodig is om passende ondersteuning te bieden. Hierbij wordt niet alleen gekeken naar specifieke hulpvragen, zoals schulden of werkloosheid, maar ook naar onderliggende factoren, zoals gezondheidsproblemen, woonsituatie, en sociaal netwerk. Het doel is om vanuit een holistisch perspectief samenhangende oplossingen te vinden en de inwoner te ondersteunen bij het versterken van zelfredzaamheid en participatie."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Brede Intake"
ggm_gemma_guid: "2d7f4231-96e8-4424-a656-c52473ea36dc"
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-2d7f4231-96e8-4424-a656-c52473ea36dc"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Gestructureerd gesprek waarin de gemeente samen met de inburgeraar diens leefsituatie, vaardigheden en ondersteuningsbehoefte in kaart brengt."
relaties:
  - type: associatie
    bedrijfsobject: Asielstatushouder
    richting: "naar-dit-BO"
    kardinaliteit: 1
    beschrijving: Asielstatushouder doorloopt een brede intake
  - type: associatie
    bedrijfsobject: Gezinsmigrant
    richting: "naar-dit-BO"
    kardinaliteit: 1
    beschrijving: Gezinsmigrant doorloopt een brede intake
  - type: associatie
    bedrijfsobject: PIP
    richting: "van-dit-BO"
    kardinaliteit: 1
    beschrijving: Resulteert in een PIP
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

- ← [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/asielstatushouder|asielstatushouder]] / [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/gezinsmigrant|gezinsmigrant]] — inburgeraar doorloopt een brede intake [1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pip|pip]] — resulteert in een PIP [1]

## Bronnen

- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer]]
- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/coa-dienstverleningsgids]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-asielopvang]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-inburgering]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-opvang-oekraine]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-rubriek-asiel]]
