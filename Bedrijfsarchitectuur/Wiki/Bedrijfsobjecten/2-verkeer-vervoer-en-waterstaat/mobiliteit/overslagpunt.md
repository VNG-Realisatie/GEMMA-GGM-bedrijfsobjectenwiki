---
type: bedrijfsobject
naam: Overslagpunt
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
bo_definitie: Fysieke locatie voor overslag van goederen tussen verschillende vervoersmodaliteiten (weg, water, spoor).
bedrijfsprocessen:
- Goederenvervoerbeleid
- Havenbeheer
bedrijfsfuncties:
- Goederenvervoerbeleid
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/logistieke-route|Logistieke Route]]'
  richting: naar-dit-BO
  kardinaliteit: 1..*
  beschrijving: Overslagpunt wordt ontsloten door logistieke routes
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/stadsdistributiepunt|Stadsdistributiepunt]]'
  richting: naar-dit-BO
  kardinaliteit: 0..*
  beschrijving: Overslagpunt levert goederen aan stadsdistributiepunten
---

# Overslagpunt

Fysieke locatie voor overslag van goederen tussen verschillende vervoersmodaliteiten (weg, water, spoor).

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — knooppunt in de multimodale goederenlogistiek
- ✅ Is herkenbaar voor domeinexperts — havenbeheerders en logistiek planners kennen deze locaties
- ✅ Heeft een eigen bestaan binnen het domein — fysieke locatie met specifieke infrastructuur
- ✅ Kan in meervoud bestaan — meerdere punten per gemeente (bijv. Zeehavenkade, Grifthoek, Vaartsche Rijn, Lage Weide)
- ✅ Heeft een eigen levenscyclus — aanleg, exploitatie, onderhoud, herontwikkeling
- ✅ Heeft relaties met andere concepten — ontsloten door logistieke routes, levert aan stadsdistributiepunten

## Beschrijving

Een overslagpunt is een locatie waar goederen worden overgeladen tussen vervoersmodaliteiten zoals weg, water en spoor. Dit maakt multimodaal goederentransport mogelijk en vermindert vrachtverkeer in de stad. Voorbeelden in Utrecht zijn Zeehavenkade, Grifthoek, Vaartsche Rijn en Lage Weide.

## Procesbron

Afgeleid uit het gemeentelijk goederenvervoer- en havenbeleid. Het [[Wiki/Bronsamenvattingen/mobiliteit/kwaliteitsnet-goederenvervoer-2007|Kwaliteitsnet Goederenvervoer binnen de gemeente Utrecht]] beschrijft overslagpunten als knooppunten in het logistieke netwerk; het [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040 - Jouw straat en onze stad gezond, aantrekkelijk en bereikbaar voor iedereen]] benadrukt hun rol bij de modal shift naar vervoer over water.

## Relaties

- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/logistieke-route|Logistieke Route]] — wordt ontsloten door logistieke routes [1..*]
- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/stadsdistributiepunt|Stadsdistributiepunt]] — levert goederen aan stadsdistributiepunten [0..*]


## Bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/kwaliteitsnet-goederenvervoer-2007]]
- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor overslagpunten of multimodale knooppunten. Dit is een registratieobject: gemeenten beheren locaties met eigenschappen als modaliteiten, capaciteit en ligging. Past bij beleidsdomein Mobiliteit onder taakveld 2. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
