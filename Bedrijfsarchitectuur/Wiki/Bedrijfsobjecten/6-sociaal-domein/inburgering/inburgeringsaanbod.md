---
type: bedrijfsobject
naam: Inburgeringsaanbod
domein:
- Asiel en Integratie
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: InburgeringsAanbod
ggm_guid: EAID_D9FAEFEC_2B8E_48dc_A1E8_E134754E9943
ggm_uml_type: Class
ggm_beleidsdomein: Inburgering
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- Inburgering
ggm_diagram_ids:
- EAID_96927C60_9F7B_4e67_806A_02EE0191983D
ggm_definitie: <font color="#0e0e0e">Het </font><font color="#0e0e0e"><b>Inburgeringsaanbod</b></font><font color="#0e0e0e"> is het geheel van activiteiten, voorzieningen en ondersteuning dat door de gemeente
  wordt aangeboden aan de inburgeringsplichtige om de inburgeringsdoelen te behalen, zoals vastgelegd in het persoonlijk plan inburgering en participatie (PIP).</font>
ggm_toelichting: ''
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: ''
ggm_gemma_guid: ''
ggm_gemma_definitie: ''
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: ''
ggm_gemma_url: ''
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
bo_definitie: Het door de gemeente vastgestelde aanbod van inburgeringsvoorzieningen waaruit de inburgeraar een passend traject volgt.
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pip|PIP]]'
  richting: naar-dit-BO
  kardinaliteit: 1
  beschrijving: PIP bevat het inburgeringsaanbod
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/leerroute|Leerroute]]'
  richting: van-dit-BO
  kardinaliteit: 1
  beschrijving: Wordt geconcretiseerd in een leerroute
---

# Inburgeringsaanbod

Het geheel van activiteiten, voorzieningen en ondersteuning dat door de gemeente wordt aangeboden aan de inburgeringsplichtige om de inburgeringsdoelen te behalen.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

## GGM-bron

> Het Inburgeringsaanbod is het geheel van activiteiten, voorzieningen en ondersteuning dat door de gemeente wordt aangeboden aan de inburgeringsplichtige om de inburgeringsdoelen te behalen, zoals vastgelegd in het persoonlijk plan inburgering en participatie (PIP).

- **Entiteit:** InburgeringsAanbod
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** DatumInburgeringsAanbod, DatumAanvangTaalschakelTraject, DatumEindeCursus, CursusInstelling, IndicatorAlfabetisering, TaalschakelTraject, DatumTaalschakelDiploma, ParticipatieDeelname, ContractId
- **Matchsterkte:** exact

## Relaties

- ← [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/pip|pip]] — PIP bevat het inburgeringsaanbod [1]
- → [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/leerroute|leerroute]] — wordt geconcretiseerd in een leerroute [1]

## Bronnen

- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer]]
- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/coa-dienstverleningsgids]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-asielopvang]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-inburgering]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-opvang-oekraine]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-rubriek-asiel]]
