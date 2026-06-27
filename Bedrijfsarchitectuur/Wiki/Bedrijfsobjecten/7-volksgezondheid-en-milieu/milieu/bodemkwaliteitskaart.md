---
type: bedrijfsobject
naam: Bodemkwaliteitskaart
domein: [Milieu]
archimate_type: "business-object"
grondslag: "governance-object"
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
bo_definitie: "Kaart met de vastgestelde bodemkwaliteit per zone, op basis waarvan grondhergebruik wordt beoordeeld."
bo_toelichting: ''
bedrijfsprocessen: [bodembeheer, grondverzet beoordelen, bodemonderzoek]
bedrijfsfuncties: [milieubeheer, vergunningverlening]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondverzet|Grondverzet]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Grondverzet wordt getoetst aan de bodemkwaliteitskaart
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemverontreiniging|Bodemverontreiniging]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: Bekende verontreinigingen worden uitgesloten van de kaart (puntbronnen)
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Centraal instrument in bodembeheer |
| Herkenbaar voor domeinexperts | ✅ Wettelijk verplicht instrument |
| Heeft eigen bestaan | ✅ Zelfstandig kaartproduct met eigen vaststelling |
| Kan in meervoud bestaan | ✅ Per gemeente, per zone, per stofgroep |
| Heeft eigen levenscyclus | ✅ Wordt opgesteld, vastgesteld, geactualiseerd (geldigheid max 10 jaar) |
| Heeft relaties met andere concepten | ✅ Grondverzet, bodemfunctieklasse, verontreiniging |

**6/6 criteria van toepassing.**

## Beschrijving

Een bodemkwaliteitskaart geeft de vastgestelde bodemkwaliteit weer per zone binnen een gemeente. De kaart vervangt de noodzaak voor bodemonderzoek per individueel geval bij grondverzet: het vastgestelde kwaliteitsniveau en de bodemfunctie (landbouw, woningbouw, industrie) bepalen of en waar grond hergebruikt mag worden.

De kaart bevat ontgravingskwaliteit (wat zit er in de grond?) en toepassingseisen (wat mag er worden toegepast?). Zones met bekende verontreinigingen (puntbronnen) worden uitgesloten. De gemeente kan gebiedsspecifiek beleid voeren met Lokale Maximale Waarden die afwijken van landelijke normen.

## Juridische bron

Wettelijke basis in het Besluit kwaliteit leefomgeving (voorheen Besluit bodemkwaliteit):

> "In het Besluit kwaliteit leefomgeving staat dat een gemeente een bodemkwaliteitskaart en een bodembeheerplan kan hebben." (bron: [[Wiki/Bronsamenvattingen/Milieu/beleid-bodem-grondwater-en-ondergrond|Beleid voor bodem, grondwater en ondergrond]])

> "Belangrijk onderdeel van de nota zijn de bodemkwaliteitskaarten, waarin de kwaliteit van de grond in alle wijken van de gemeente Utrecht is beschreven." (bron: [[Wiki/Bronsamenvattingen/Milieu/nota-bodembeheer|Nota Bodembeheer 2017-2027 (Grondig Werken 4)]])

## Relaties

- **[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondverzet|Grondverzet]]** — grondverzet wordt beoordeeld op basis van de bodemkwaliteitskaart
- **[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemverontreiniging|Bodemverontreiniging]]** — bekende verontreinigingen (puntbronnen) worden van de kaart uitgesloten

## Bedrijfsprocessen

- **Bodembeheer** — de kaart is het centrale instrument
- **Grondverzet beoordelen** — toetsing hergebruik op basis van kwaliteitszone
- **Bodemonderzoek** — data uit onderzoek voedt de kaart


## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/beleid-bodem-grondwater-en-ondergrond]]
- [[Wiki/Bronsamenvattingen/Milieu/nota-bodembeheer]]

## Terugmelding GGM

Het GGM heeft geen beleidsdomein voor bodem of milieu (buiten Afval). De bodemkwaliteitskaart is een wettelijk verplicht ruimtelijk instrument dat elke gemeente kan opstellen. Dit is een structureel GGM-hiaat in taakveld 7 (Volksgezondheid en Milieu). Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
