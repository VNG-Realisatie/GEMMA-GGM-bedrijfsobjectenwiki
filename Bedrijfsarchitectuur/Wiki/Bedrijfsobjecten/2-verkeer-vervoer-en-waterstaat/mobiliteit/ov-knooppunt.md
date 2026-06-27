---
type: bedrijfsobject
naam: OV-knooppunt
domein:
- mobiliteit
archimate_type: business-object
grondslag: procesobject
ggm_entiteit: ''
ggm_beleidsdomein: Mobiliteit
ggm_guid: ''
ggm_uml_type: ''
ggm_taakveld: ''
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ''
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
bo_definitie: Multimodaal overstappunt op een kruising van openbaar-vervoerverbindingen waar reizigers overstappen tussen lijnen, modaliteiten en/of vervoerwijzen.
bo_toelichting: ''
bedrijfsprocessen:
- OV-beleid
- Verkeersmanagement
- Ruimtelijke ordening
bedrijfsfuncties:
- Openbaar vervoer
- Verkeersmanagement
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/ov-lijn|OV-lijn]]'
  richting: van-dit-BO
  kardinaliteit: 1..*
  beschrijving: Knooppunt is kruising van OV-lijnen
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/halte|Halte]]'
  richting: van-dit-BO
  kardinaliteit: 1..*
  beschrijving: Knooppunt bevat een of meer haltes
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/p-r-locatie|P+R-locatie]]'
  richting: van-dit-BO
  kardinaliteit: 0..*
  beschrijving: P+R-locatie bij OV-knooppunt
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/mobiliteitshub|Mobiliteitshub]]'
  richting: van-dit-BO
  kardinaliteit: 0..*
  beschrijving: Mobiliteitshub bij OV-knooppunt
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/hoofdfietsroute|Hoofdfietsroute]]'
  richting: naar-dit-BO
  kardinaliteit: 0..*
  beschrijving: Fietsroute verbindt met knooppunt
---

# OV-knooppunt

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — centraal concept in het OV-beleid en de knooppuntontwikkeling
- ✅ Is herkenbaar voor domeinexperts — verkeerskundigen, OV-beleidsmakers en ruimtelijk planners werken met OV-knooppunten
- ✅ Heeft een eigen bestaan binnen het domein — een knooppunt is een zelfstandige multimodale locatie
- ✅ Kan in meervoud bestaan — meerdere knooppunten in de stad (Overvecht, Lunetten, Leidsche Rijn Centrum, USP, Westraven, Papendorp)
- ✅ Heeft een eigen levenscyclus — aanwijzing, ontwikkeling, inrichting, exploitatie, herontwikkeling
- ✅ Heeft relaties met andere concepten — verbindt OV-lijnen, haltes, P+R-locaties, mobiliteitshubs en fietsroutes

## Beschrijving

Een OV-knooppunt is een multimodaal overstappunt waar openbaar-vervoerlijnen samenkomen en reizigers overstappen tussen lijnen, modaliteiten en vervoerwijzen. Knooppunten zijn tevens locaties voor ruimtelijke verdichting (knooppuntontwikkeling). Het Mobiliteitsplan 2040 benoemt onder meer Overvecht, Lunetten-Koningsweg, Leidsche Rijn Centrum, USP, Westraven en Papendorp als strategische knooppunten.

## Procesbron

Afgeleid uit het gemeentelijk OV-beleid en de knooppuntstrategie. Het [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040 - Jouw straat en onze stad gezond, aantrekkelijk en bereikbaar voor iedereen]] beschrijft de rol van OV-knooppunten in het multimodale netwerk.

## Relaties

- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/ov-lijn|OV-lijn]] — knooppunt is kruising van OV-lijnen [1..*]
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/halte|Halte]] — knooppunt bevat haltes [1..*]
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/p-r-locatie|P+R-locatie]] — P+R-locatie bij knooppunt [0..*]
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/mobiliteitshub|Mobiliteitshub]] — mobiliteitshub bij knooppunt [0..*]
- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/hoofdfietsroute|Hoofdfietsroute]] — fietsroute verbindt met knooppunt [0..*]


## Bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor OV-knooppunten. Dit is een registratieobject: gemeenten registreren knooppunten met locatie, modaliteiten, capaciteit en ontwikkelstatus. Past bij beleidsdomein Mobiliteit onder taakveld 2. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
