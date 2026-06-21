---
type: bedrijfsobject
naam: Bouwlogistiek Centrum
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
gemma_definitie: "Tijdelijke hub voor gebundelde aanvoer van bouwmaterialen en -personeel naar bouwlocaties."
bedrijfsprocessen: [Bouwlogistiek, Vergunningverlening]
bedrijfsfuncties: [Goederenvervoerbeleid, Bouwtoezicht]
relaties:
  - type: associatie
    bedrijfsobject: Logistieke Route
    richting: "naar-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: Bouwlogistiek centrum wordt ontsloten door logistieke routes
---

# Bouwlogistiek Centrum

Tijdelijke hub voor gebundelde aanvoer van bouwmaterialen en -personeel naar bouwlocaties.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — vermindert bouwverkeer en hinder in de stad
- ✅ Is herkenbaar voor domeinexperts — bouwlogistiek managers en vergunningverleners kennen het concept
- ✅ Heeft een eigen bestaan binnen het domein — fysieke, tijdelijke locatie met specifieke functie
- ✅ Kan in meervoud bestaan — meerdere centra bij grote bouwprojecten
- ✅ Heeft een eigen levenscyclus — oprichting bij projectstart, exploitatie, opheffing bij projecteinde
- ✅ Heeft relaties met andere concepten — ontsloten door logistieke routes, gekoppeld aan bouwvergunningen

## Beschrijving

Een bouwlogistiek centrum is een tijdelijke hub waar bouwmaterialen en -personeel worden gebundeld voor just-in-time levering aan bouwlocaties. Dit vermindert het aantal vrachtbewegingen in de stad, beperkt hinder voor de omgeving en biedt tijdelijke opslagcapaciteit. Het centrum is gekoppeld aan een bouwproject of gebiedsontwikkeling.

## Procesbron

Afgeleid uit het gemeentelijk bouwlogistiek beleid. Het [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040]] beschrijft bouwlogistieke centra als instrument om bouwverkeer te bundelen en hinder te beperken bij grote bouwprojecten.

## Relaties

- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/logistieke-route|Logistieke Route]] — wordt ontsloten door logistieke routes [1..*]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor bouwlogistieke centra. Dit is een registratieobject: gemeenten kennen locaties toe met eigenschappen als looptijd, capaciteit en gekoppeld bouwproject. Past bij beleidsdomein Mobiliteit onder taakveld 2. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
