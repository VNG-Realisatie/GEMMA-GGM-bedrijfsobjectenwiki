---
type: bedrijfsobject
naam: Mobiliteitshub
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
gemma_definitie: "Multimodaal overstappunt met deelvoertuigen, voorzieningen en diensten voor het faciliteren van ketenreizen."
bedrijfsprocessen: [Mobiliteitsmanagement, Deelmobiliteitsbeleid, Ruimtelijke ordening]
bedrijfsfuncties: [Verkeersmanagement, Mobiliteitsbeleid]
relaties:
  - type: associatie
    bedrijfsobject: "[[P+R-locatie]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "hub kan geïntegreerd zijn in P+R-locatie"
  - type: associatie
    bedrijfsobject: "[[OV-knooppunt]]"
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: "hub ligt bij OV-knooppunt"
  - type: associatie
    bedrijfsobject: "[[Hoofdfietsroute]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: fietsroutes sluiten aan op hub
---

## BO-criteria toetsing

- **Betekenis**: centraal concept in multimodaal mobiliteitsbeleid
- **Herkenbaar**: benoemd in Mobiliteitsplan, herkenbaar voor beleidsmakers en reizigers
- **Eigen bestaan**: fysieke locatie met voorzieningen en diensten
- **Meervoud**: Mobiliteitshub XL Papendorp, buurthubs in wijken
- **Levenscyclus**: oprichting, uitbreiding, herinrichting
- **Relaties**: met [[P+R-locatie]], [[OV-knooppunt]], [[Hoofdfietsroute]]

## Beschrijving

Een Mobiliteitshub is een fysieke locatie waar verschillende vervoersmodaliteiten samenkomen en reizigers kunnen overstappen tussen deelvoertuigen, OV, fiets en auto. Hubs bieden aanvullende voorzieningen zoals afhaalpunten, werkplekken, horeca en kleinschalige retail. Het Mobiliteitsplan onderscheidt grote hubs (Mobiliteitshub XL bij economische kerngebieden) en kleinschalige buurthubs.

## Procesbron

Afgeleid uit [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040 - Jouw straat en onze stad gezond, aantrekkelijk en bereikbaar voor iedereen]], §6.5 Multimodale reis.

## Relaties

- [[P+R-locatie]] — hub kan geïntegreerd zijn in P+R-voorziening
- [[OV-knooppunt]] — hub ligt bij of vormt onderdeel van OV-knooppunt
- [[Hoofdfietsroute]] — fietsroutes sluiten aan op hub


## Bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]

## Terugmelding GGM

GGM-hiaat. De Mobiliteitshub is een dataobject dat gemeenten registreren: locatie, type, aangeboden modaliteiten, voorzieningen, capaciteit. Past in GGM beleidsdomein Mobiliteit als nieuw concept dat de multimodale transitie ondersteunt.
