---
type: bedrijfsobject
naam: Hoofdfietsroute
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

gemma_definitie: "Aangewezen fietsroute met kwaliteitseisen in het stedelijk hoofdfietsnetwerk voor het spreiden en faciliteren van fietsstromen."
bronnen:
  - "[[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]"
relaties:
  - type: associatie
    bedrijfsobject: OV-knooppunt
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Hoofdfietsroute verbindt met OV-knooppunten
  - type: associatie
    bedrijfsobject: P+R-locatie
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Fietsroute naar P+R-locatie
bedrijfsprocessen: [Fietsbeleid, Beheer openbare ruimte, Verkeersmanagement]
bedrijfsfuncties: [Verkeersmanagement, Fietsbeleid]
---

# Hoofdfietsroute

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — centraal in het fietsbeleid voor het spreiden van fietsstromen
- ✅ Is herkenbaar voor domeinexperts — verkeerskundigen en fietsplanners werken met het hoofdfietsnetwerk
- ✅ Heeft een eigen bestaan binnen het domein — een route is een zelfstandig aangewezen traject met kwaliteitseisen
- ✅ Kan in meervoud bestaan — circa 50 routes in het Utrechtse hoofdfietsnetwerk
- ✅ Heeft een eigen levenscyclus — aanwijzing, inrichting, onderhoud, evaluatie, wijziging
- ✅ Heeft relaties met andere concepten — verbindt met OV-knooppunten, P+R-locaties en mobiliteitshubs

## Beschrijving

Een hoofdfietsroute is een aangewezen fietsverbinding in het stedelijk hoofdfietsnetwerk. Het Mobiliteitsplan 2040 onderscheidt snelle doorstroomroutes en rustige bestemmingsroutes. Per route gelden kwaliteitseisen voor doorstroming, comfort en veiligheid. Het netwerk moet de verwachte 75% fietsgroei tot 2040 opvangen door fietsstromen te spreiden.

## Procesbron

Afgeleid uit het gemeentelijk fietsbeleid. Het [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040]] definieert het hoofdfietsnetwerk en de kwaliteitseisen.

## Relaties

- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/ov-knooppunt|OV-knooppunt]] — fietsroute verbindt met OV-knooppunten [0..*]
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/p-r-locatie|P+R-locatie]] — fietsroute naar P+R-locatie [0..*]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor fietsroutes of het hoofdfietsnetwerk. Dit is een registratieobject: gemeenten wijzen routes aan met specifieke kenmerken (routetype, kwaliteitseisen, lengte, capaciteit). Past bij beleidsdomein Mobiliteit onder taakveld 2. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
