---
type: bedrijfsobject
naam: Grondwatermeetpunt
domein: [Milieu]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit: ""
ggm_beleidsdomein: ""
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
gemma_definitie: "Fysiek meetpunt in een monitoringsnetwerk voor het meten van grondwaterkwaliteit en -stand."
bedrijfsprocessen: [gebiedsgericht grondwaterbeheer, milieumonitoring, bodemsanering]
bedrijfsfuncties: [milieubeheer]
relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemverontreiniging|Bodemverontreiniging]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: Meetpunten monitoren de verspreiding van verontreinigingen
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/saneringsplan|Saneringsplan]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Saneringsplannen schrijven monitoring via meetpunten voor
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Essentieel voor monitoring grondwaterkwaliteit |
| Herkenbaar voor domeinexperts | ✅ Fysieke peilbuizen met meetgegevens |
| Heeft eigen bestaan | ✅ Individueel punt met locatie, diepte, filter |
| Kan in meervoud bestaan | ✅ Tientallen tot honderden per beheergebied |
| Heeft eigen levenscyclus | ✅ Installatie → bemonstering → vervanging → verwijdering |
| Heeft relaties met andere concepten | ✅ Verontreiniging, saneringsplan |

**6/6 criteria van toepassing.**

## Beschrijving

Een grondwatermeetpunt is een fysiek punt (peilbuis) in het monitoringsnetwerk van de gemeente, bedoeld voor het meten van grondwaterkwaliteit en grondwaterstand. Elk meetpunt heeft een locatie, diepte, filterdiepte en wordt periodiek bemonsterd.

In het Utrechtse gebiedsplan vormen de meetpunten een netwerk dat de verspreiding van grondwaterverontreinigingen bewaakt. Het netwerk monitort of verontreinigingen binnen de beheergrens blijven en of de grondwaterkwaliteit verbetert.

> "Door uitvoering en toepassing van het Saneringsplan ondergrond Utrecht is door de aanleg van een meetnet meer inzicht verkregen in bodemopbouw, grondwater en grondwaterverontreiniging." (bron: [[Wiki/Bronsamenvattingen/Milieu/gebiedsplan-grondwaterbeheer|Gebiedsplan gebiedsgericht grondwaterbeheer en visie op duurzaam gebruik van de ondergrond]])

## Procesbron

Meetpunten worden geïnstalleerd als onderdeel van het monitoringsprogramma dat voortvloeit uit saneringsplannen en het gebiedsplan. De gemeente beheert het netwerk en de meetgegevens.

## Relaties

- **[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemverontreiniging|Bodemverontreiniging]]** — meetpunten bewaken verspreiding van verontreinigingspluimen
- **[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/saneringsplan|Saneringsplan]]** — saneringsplannen schrijven monitoring voor


## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/gebiedsplan-grondwaterbeheer]]

## Terugmelding GGM

Het GGM heeft wel Filterput (Beheer Openbare Ruimte) als fysiek object, maar dat is een ander concept (drainageput, niet een milieumeetpunt). Grondwatermeetpunt als milieu-registratieobject ontbreekt. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
