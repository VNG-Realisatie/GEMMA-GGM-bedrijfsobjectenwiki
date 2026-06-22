---
type: bedrijfsobject
naam: Stadsdistributiepunt
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
gemma_definitie: "Aangewezen locatie voor overslag en bundeling van goederen ten behoeve van stadsdistributie."
bedrijfsprocessen: [Goederenvervoerbeleid, Ruimtelijke ordening]
bedrijfsfuncties: [Goederenvervoerbeleid, Economisch beleid]
bronnen: [Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]
relaties:
  - type: associatie
    bedrijfsobject: Logistieke Route
    richting: "naar-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: Stadsdistributiepunt wordt ontsloten door logistieke routes
  - type: associatie
    bedrijfsobject: Overslagpunt
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Stadsdistributiepunt ontvangt goederen van overslagpunten
---

# Stadsdistributiepunt

Aangewezen locatie voor overslag en bundeling van goederen ten behoeve van stadsdistributie.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — centraal in de keten van stedelijke goederenlogistiek
- ✅ Is herkenbaar voor domeinexperts — logistiek planners en beleidsmakers kennen deze hubs
- ✅ Heeft een eigen bestaan binnen het domein — fysieke locatie met specifieke functie
- ✅ Kan in meervoud bestaan — meerdere punten per gemeente (bijv. Lage Weide, Liesbosch, Laagraven, Strijkviertel)
- ✅ Heeft een eigen levenscyclus — aanwijzing, inrichting, exploitatie, herontwikkeling
- ✅ Heeft relaties met andere concepten — ontsloten door logistieke routes, ontvangt van overslagpunten

## Beschrijving

Een stadsdistributiepunt is een locatie waar goederen worden gebundeld en overgeslagen voor distributie naar bestemmingen in de stad. Het fungeert als schakel tussen regionaal goederentransport en last-mile levering. Voorbeelden in Utrecht zijn Lage Weide, Liesbosch, Laagraven en Strijkviertel.

## Procesbron

Afgeleid uit het gemeentelijk goederenvervoerbeleid. Het [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040 - Jouw straat en onze stad gezond, aantrekkelijk en bereikbaar voor iedereen]] beschrijft stadsdistributiepunten als hubs voor gebundelde last-mile distributie, passend bij de transitie naar zero-emissie stadslogistiek.

## Relaties

- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/logistieke-route|Logistieke Route]] — wordt ontsloten door logistieke routes [1..*]
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/overslagpunt|Overslagpunt]] — ontvangt goederen van overslagpunten [0..*]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor stadsdistributiepunten. Dit is een registratieobject: gemeenten wijzen locaties aan met eigenschappen als capaciteit, modaliteiten en ruimtelijke bestemming. Past bij beleidsdomein Mobiliteit onder taakveld 2. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
