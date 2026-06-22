---
type: bedrijfsobject
naam: Inburgeringsplicht
domein: [Asiel en Integratie]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Inburgeringsplicht"
ggm_guid: EAID_E2C66E88_930E_460f_93F8_8CD160DCEE15
ggm_uml_type: Class
ggm_beleidsdomein: "Inburgering"
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: [Inburgering]
ggm_diagram_ids: [EAID_96927C60_9F7B_4e67_806A_02EE0191983D]
ggm_definitie: "Bevat de uitkomst Leerbaarheidstoets dat een groot deel van de leerroutes bepaalt. Bevat mogelijk ook de Examenresultaten (nog toe te voegen als Ja). Dit zijn DUO berichten (Opvragen en per API beschikbaar stellen aan deze Entiteit/Attributen."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "De formele wettelijke verplichting van een inburgeraar om binnen de gestelde termijn te voldoen aan de eisen van de Wet inburgering 2021."
bronnen: [Wiki/Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer, Wiki/Bronsamenvattingen/Inburgering en Asielopvang/coa-dienstverleningsgids, Wiki/Bronsamenvattingen/Asiel en Integratie/vng-asielopvang, Wiki/Bronsamenvattingen/Asiel en Integratie/vng-inburgering, Wiki/Bronsamenvattingen/Asiel en Integratie/vng-opvang-oekraine, Wiki/Bronsamenvattingen/Asiel en Integratie/vng-rubriek-asiel]
relaties:
  - type: associatie
    bedrijfsobject: Asielstatushouder
    richting: "naar-dit-BO"
    kardinaliteit: 1
    beschrijving: Asielstatushouder heeft een inburgeringsplicht
  - type: associatie
    bedrijfsobject: Gezinsmigrant
    richting: "naar-dit-BO"
    kardinaliteit: 1
    beschrijving: Gezinsmigrant heeft een inburgeringsplicht
  - type: associatie
    bedrijfsobject: Inburgeringstermijn
    richting: "van-dit-BO"
    kardinaliteit: 1
    beschrijving: Heeft een inburgeringstermijn
---

# Inburgeringsplicht

De formele wettelijke verplichting van een inburgeraar om binnen de gestelde termijn te voldoen aan de eisen van de Wet inburgering 2021.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

Ontheffing en Vrijstelling zijn attributen/statuswijzigingen van dit BO, geen aparte bedrijfsobjecten. Het GGM modelleert ze als aparte entiteiten met relaties naar Inburgeringsplicht, maar op bedrijfsniveau zijn ze statussen binnen de levenscyclus van de inburgeringsplicht.

## GGM-bron

> Bevat de uitkomst Leerbaarheidstoets dat een groot deel van de leerroutes bepaalt. Bevat mogelijk ook de Examenresultaten (nog toe te voegen als Ja). Dit zijn DUO berichten (Opvragen en per API beschikbaar stellen aan deze Entiteit/Attributen.

- **Entiteit:** Inburgeringsplicht
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** IndicatorInburgeringsplicht, UitkomstLeerbaarheidstoets, BeschikkingVoldaanInburgeringsplicht, V-nummer, InburgeraarSpecialisatie, DatumStart, DatumEind, RedenGeenInburgeringsplicht, DatumGewijzigdInburgeringsplicht, WordtBehandelsAls, DatumGewijzigdWordtBehandeldAls
- **Matchsterkte:** exact

## Relaties

- ← [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/asielstatushouder|asielstatushouder]] / [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/gezinsmigrant|gezinsmigrant]] — inburgeraar heeft een inburgeringsplicht [1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringstermijn|inburgeringstermijn]] — heeft een inburgeringstermijn [1]
