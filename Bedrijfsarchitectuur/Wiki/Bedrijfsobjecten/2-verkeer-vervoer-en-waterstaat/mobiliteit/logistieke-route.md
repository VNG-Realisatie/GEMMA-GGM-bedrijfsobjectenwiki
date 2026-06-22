---
type: bedrijfsobject
naam: Logistieke Route
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
gemma_definitie: "Aangewezen voorkeursroute voor goederenvervoer over de weg, met specifieke kwaliteitseisen voor doorstroming, veiligheid en leefbaarheid."
bedrijfsprocessen: [Routering goederenvervoer, Verkeersmanagement, Ruimtelijke ordening]
bedrijfsfuncties: [Verkeersmanagement, Goederenvervoerbeleid]
relaties:
  - type: associatie
    bedrijfsobject: Overslagpunt
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Route verbindt overslagpunten
  - type: associatie
    bedrijfsobject: Stadsdistributiepunt
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Route ontsluit stadsdistributiepunten
  - type: associatie
    bedrijfsobject: "Laad- en Losplaats"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Route geeft toegang tot laad- en losplaatsen"
---

# Logistieke Route

Aangewezen voorkeursroute voor goederenvervoer over de weg, met specifieke kwaliteitseisen voor doorstroming, veiligheid en leefbaarheid.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — routes zijn centraal in het goederenvervoerbeleid
- ✅ Is herkenbaar voor domeinexperts — verkeerskundigen en beleidsmakers werken met het routenetwerk
- ✅ Heeft een eigen bestaan binnen het domein — een route is een zelfstandig aangewezen traject
- ✅ Kan in meervoud bestaan — circa 50 routes in het Utrechtse netwerk
- ✅ Heeft een eigen levenscyclus — aanwijzing, driejaarlijkse evaluatie, wijziging, opheffing
- ✅ Heeft relaties met andere concepten — verbindt overslagpunten, stadsdistributiepunten en laad-/losplaatsen

## Beschrijving

Een logistieke route is een door de gemeente aangewezen voorkeursweg voor vrachtverkeer. Het Kwaliteitsnet Goederenvervoer onderscheidt Route I (doorgaand, naar economische centra) en Route II (aansluitend, naar centra buiten het doorgaande net). Per route gelden kwaliteitseisen voor doorstroming, veiligheid en leefbaarheid. Het netwerk wordt driejaarlijks geactualiseerd.

## Specialisaties

| Subtype | Omschrijving |
|---|---|
| Route I | Doorgaande route naar economische centra |
| Route II | Aansluitende route naar centra buiten het doorgaande net |

## Procesbron

Afgeleid uit het gemeentelijk goederenvervoerbeleid. Het Kwaliteitsnet Goederenvervoer (2007) definieert het routenetwerk en de kwaliteitscriteria; het [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040 - Jouw straat en onze stad gezond, aantrekkelijk en bereikbaar voor iedereen]] bevestigt het belang van logistieke routes voor de transitie naar zero-emissie stadslogistiek.

## Relaties

- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/overslagpunt|Overslagpunt]] — route verbindt overslagpunten [0..*]
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/stadsdistributiepunt|Stadsdistributiepunt]] — route ontsluit stadsdistributiepunten [0..*]
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/laad-en-losplaats|Laad- en Losplaats]] — route geeft toegang tot laad- en losplaatsen [0..*]


## Bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor logistieke routes of het kwaliteitsnet goederenvervoer. Dit is een registratieobject: gemeenten wijzen routes aan met specifieke kenmerken (classificatie, kwaliteitseisen, beperkingen). Past bij beleidsdomein Mobiliteit onder taakveld 2. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
