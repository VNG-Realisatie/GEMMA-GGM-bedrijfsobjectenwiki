---
type: bedrijfsobject
naam: "P+R-locatie"
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
gemma_definitie: "Parkeer-en-reisvoorziening aan de rand van de stad of in de regio voor overstap van auto naar openbaar vervoer of fiets."
bedrijfsprocessen: [Parkeerbeleid, Mobiliteitsmanagement, OV-beleid]
bedrijfsfuncties: [Verkeersmanagement, Parkeerbeleid]
bronnen: [Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]
relaties:
  - type: associatie
    bedrijfsobject: "OV-knooppunt"
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: "P+R-locatie bij OV-knooppunt"
  - type: associatie
    bedrijfsobject: Mobiliteitshub
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: "P+R-locatie kan onderdeel zijn van een mobiliteitshub"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeergarage|Parkeergarage]]"
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: "P+R-locatie kan een parkeergarage bevatten"
  - type: associatie
    bedrijfsobject: Hoofdfietsroute
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Fietsroute verbindt met P+R-locatie"
---

# P+R-locatie

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — centraal instrument voor het terugdringen van autoverkeer in de stad
- ✅ Is herkenbaar voor domeinexperts — verkeerskundigen, parkeer- en OV-beleidsmakers werken met P+R-locaties
- ✅ Heeft een eigen bestaan binnen het domein — een P+R is een zelfstandige voorziening met locatie, capaciteit en OV-aansluiting
- ✅ Kan in meervoud bestaan — meerdere P+R-locaties rond Utrecht (Westraven, USP, regionale locaties)
- ✅ Heeft een eigen levenscyclus — aanwijzing, realisatie, exploitatie, uitbreiding, opheffing
- ✅ Heeft relaties met andere concepten — verbindt met OV-knooppunten, mobiliteitshubs, parkeergarages en fietsroutes

## Beschrijving

Een P+R-locatie is een parkeer-en-reisvoorziening aan de rand van de stad of in de regio waar automobilisten overstappen op openbaar vervoer of fiets. Het Mobiliteitsplan 2040 stelt dat P+R-locaties voor de Ring Utrecht moeten liggen, met een frequente OV-verbinding naar de economische kerngebieden. Voorbeelden zijn P+R Westraven, P+R USP en regionale P+R-locaties.

## Procesbron

Afgeleid uit het gemeentelijk parkeer- en mobiliteitsbeleid. Het [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040]] beschrijft de strategie voor P+R-locaties als onderdeel van de multimodale bereikbaarheid.

## Relaties

- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/ov-knooppunt|OV-knooppunt]] — P+R-locatie bij knooppunt [0..1]
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/mobiliteitshub|Mobiliteitshub]] — P+R kan onderdeel zijn van een hub [0..1]
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeergarage|Parkeergarage]] — P+R kan een parkeergarage bevatten [0..1]
- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/hoofdfietsroute|Hoofdfietsroute]] — fietsroute verbindt met P+R [0..*]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor P+R-locaties. Dit is een registratieobject: gemeenten registreren P+R-locaties met locatie, capaciteit, OV-aansluiting en tarieven. Hoewel het GGM wel Parkeergarage kent (beleidsdomein Parkeren), ontbreekt het specifieke concept van een parkeer-en-reisvoorziening met overstapfunctie. Past bij beleidsdomein Mobiliteit onder taakveld 2. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
