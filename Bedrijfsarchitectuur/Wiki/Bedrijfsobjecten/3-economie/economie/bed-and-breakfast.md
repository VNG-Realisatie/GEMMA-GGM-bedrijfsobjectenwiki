---
type: bedrijfsobject
naam: "Bed-and-breakfast"
domein: [Economie]
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
gemma_definitie: "Kleinschalige logiesaccommodatie met maximaal vier kamers, doorgaans in een woning, als aanvulling op het reguliere hotelaanbod."
bedrijfsprocessen: [logiesvergunningverlening, monitoring toeristisch aanbod]
bedrijfsfuncties: [vergunningverlening, economisch beleid]
bronnen: [Wiki/Bronsamenvattingen/Economie/actualisatie-marktruimte-hotelnota]
relaties:
  - type: associatie
    bedrijfsobject: "[[Horecabedrijf]]"
    richting: "naar-dit-BO"
    kardinaliteit: 1
    beschrijving: "Een B&B wordt geëxploiteerd door een horecabedrijf of particulier"
  - type: associatie
    bedrijfsobject: "[[Hotel]]"
    richting: bidirectioneel
    kardinaliteit: 
    beschrijving: "B&B en hotel zijn beide logiesaccommodaties maar met andere schaal en regelgeving"
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Expliciet benoemd in horecabeleid als aparte categorie |
| Is herkenbaar voor domeinexperts | ✅ | Herkenbaar begrip voor beleidsmakers en toerismeprofessionals |
| Heeft een eigen bestaan | ✅ | Fysieke accommodatie in een woning |
| Kan in meervoud bestaan | ✅ | Utrecht telt ca. 29 B&B-accommodaties |
| Heeft een eigen levenscyclus | ✅ | Start → exploitatie → eventueel beëindiging |
| Heeft relaties met andere concepten | ✅ | Hotel (verwant), horecabedrijf, woning |

6/6 criteria — BO.

## Beschrijving

Een bed-and-breakfast is een kleinschalige logiesaccommodatie met maximaal vier kamers, doorgaans geëxploiteerd vanuit een woning. De gemeente ziet B&B's als een welkome aanvulling op het reguliere hotelaanbod. Ze bedienen een eigen marktsegment en hebben beperkte invloed op de marktruimte voor hotels.

> "Bed-and-breakfastverstrekkers zijn in Utrecht een welkome aanvulling op het aanbod van reguliere hotels." — [[Wiki/Bronsamenvattingen/Economie/actualisatie-marktruimte-hotelnota|Actualisatie marktruimte hotelnota]]

## Procesbron

B&B's worden in het horecabeleid als aparte categorie benoemd naast hotels. Er is geen specifieke GGM-entiteit; het GGM modelleert alleen Hotel als specialisatie van Vestiging. Een B&B zou een vergelijkbare specialisatie van Vestiging zijn, maar ontbreekt in het model.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Horecabedrijf]] | associatie | Horecabedrijf → B&B | 1 | Beleid |
| [[Hotel]] | associatie | bidirectioneel | — | Beleid (verwante logiesaccommodaties) |

## Terugmelding GGM

**Bed-and-breakfast** — Registratieobject voor kleinschalige logiesaccommodatie (max 4 kamers, locatie, exploitant). Dataobject vergelijkbaar met Hotel maar met eigen schaal en regelgeving. Het GGM modelleert Hotel als Vestiging-specialisatie; B&B zou een vergelijkbare specialisatie kunnen zijn. Zou onder taakveld 3 Economie kunnen.
