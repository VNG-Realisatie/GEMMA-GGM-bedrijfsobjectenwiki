---
type: bedrijfsobject
naam: Halte
domein: [mobiliteit]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit: ""
ggm_beleidsdomein: "Mobiliteit"
ggm_guid: ""
ggm_uml_type: ""
ggm_taakveld: ""
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ""
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
gemma_definitie: "Fysieke voorziening in de openbare ruimte waar reizigers in- en uitstappen voor openbaar vervoer."
bedrijfsprocessen: [OV-beleid, Beheer openbare ruimte]
bedrijfsfuncties: [Openbaar vervoer]
bronnen: [Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]
relaties:
  - type: compositie
    bedrijfsobject: "OV-lijn"
    richting: "naar-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: "Halte hoort bij een of meer OV-lijnen"
  - type: associatie
    bedrijfsobject: "OV-knooppunt"
    richting: "naar-dit-BO"
    kardinaliteit: 0..1
    beschrijving: "Halte kan onderdeel zijn van een OV-knooppunt"
---

# Halte

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — basisvoorziening voor de toegankelijkheid van het OV
- ✅ Is herkenbaar voor domeinexperts — OV-beleidsmakers en beheerders werken met haltes
- ✅ Heeft een eigen bestaan binnen het domein — een halte is een zelfstandige fysieke voorziening met locatie en inrichting
- ✅ Kan in meervoud bestaan — honderden haltes in het stedelijk OV-netwerk
- ✅ Heeft een eigen levenscyclus — aanwijzing, inrichting, onderhoud, verplaatsing, opheffing
- ✅ Heeft relaties met andere concepten — hoort bij OV-lijnen en kan onderdeel zijn van een OV-knooppunt

## Beschrijving

Een halte is een fysieke voorziening in de openbare ruimte waar reizigers in- en uitstappen voor tram of bus. De gemeente is verantwoordelijk voor de halte-infrastructuur (perron, abri, toegankelijkheid). Haltes vormen samen met OV-lijnen het OV-netwerk en kunnen onderdeel zijn van een OV-knooppunt.

## Procesbron

Afgeleid uit het gemeentelijk OV-beleid en beheer openbare ruimte. Het [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040]] beschrijft de gewenste kwaliteit en toegankelijkheid van haltes.

## Relaties

- ◆ [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/ov-lijn|OV-lijn]] — halte hoort bij OV-lijnen [1..*]
- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/ov-knooppunt|OV-knooppunt]] — halte kan onderdeel zijn van een knooppunt [0..1]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor OV-haltes. Dit is een registratieobject: gemeenten registreren haltes met locatie, type (tram/bus), toegankelijkheid en inrichting. Past bij beleidsdomein Mobiliteit onder taakveld 2. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
