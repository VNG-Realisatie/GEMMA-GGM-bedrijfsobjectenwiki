---
type: bedrijfsobject
naam: Laad- en Losplaats
domein: [mobiliteit]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: Mobiliteit
ggm_taakveld: "2 Verkeer, Vervoer en Waterstaat"
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

gemma_definitie: "Aangewezen locatie in de openbare ruimte voor het laden en lossen van goederen."
bronnen:
  - "[[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]"
relaties:
  - type: associatie
    bedrijfsobject: Logistieke Route
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Laad- en losplaats ligt aan een logistieke route
  - type: associatie
    bedrijfsobject: Zero-emissiezone
    richting: "naar-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: Laad- en losplaats kan binnen een zero-emissiezone liggen
bedrijfsprocessen: [Beheer openbare ruimte, Goederenvervoerbeleid, Handhaving]
bedrijfsfuncties: [Verkeersmanagement, Goederenvervoerbeleid]
---

# Laad- en Losplaats

Aangewezen locatie in de openbare ruimte voor het laden en lossen van goederen.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — essentieel voor stedelijke logistiek
- ✅ Is herkenbaar voor domeinexperts — verkeerskundigen en handhavers kennen laad-/losplekken
- ✅ Heeft een eigen bestaan binnen het domein — fysieke, aangewezen locatie in de openbare ruimte
- ✅ Kan in meervoud bestaan — tientallen locaties in een gemeente
- ✅ Heeft een eigen levenscyclus — aanwijzing, inrichting, beheer, opheffing
- ✅ Heeft relaties met andere concepten — relatie met routes, zones en handhaving

## Beschrijving

Een laad- en losplaats is een door de gemeente aangewezen locatie waar goederenvoertuigen mogen laden en lossen. Het Mobiliteitsplan 2040 zet in op efficienter gebruik van deze plekken via realtime data en IT-systemen, zoals dynamische tijdvensters en reserveringssystemen.

## Procesbron

Afgeleid uit het gemeentelijk verkeers- en goederenvervoerbeleid. Het [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040]] beschrijft de ambitie om laad-/losplekken efficienter te benutten met realtime data en IT-systemen.

## Relaties

- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/logistieke-route|Logistieke Route]] — laad- en losplaats ligt aan een logistieke route [0..*]
- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/zero-emissiezone|Zero-emissiezone]] — kan binnen een zero-emissiezone liggen [0..1]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor laad- en losplaatsen. Dit is een registratieobject: gemeenten wijzen locaties aan met eigenschappen als tijdvenster, capaciteit en locatiegegevens. Past bij beleidsdomein Mobiliteit onder taakveld 2. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
