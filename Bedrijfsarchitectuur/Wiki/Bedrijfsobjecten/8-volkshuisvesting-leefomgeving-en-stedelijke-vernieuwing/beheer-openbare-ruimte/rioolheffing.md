---
type: element
naam: Rioolheffing
onderwerp: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "procesobject"
ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:
bo_definitie: "Gemeentelijke belasting voor de dekking van kosten van water- en rioleringsbeheer, geheven bij perceeleigenaren en grootverbruikers."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Afvalstoffenheffing]]"
    richting: bidirectioneel
    kardinaliteit:
    beschrijving: Vergelijkbare gemeentelijke heffing voor een ander domein
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioleringsgebied|Rioleringsgebied]]"
    richting: bidirectioneel
    kardinaliteit:
    beschrijving: Rioolheffing financiert het beheer van rioleringsgebieden
bedrijfsprocessen: [Tariefvaststelling rioolheffing, Heffing en inning, Kostentoerekening]
bedrijfsfuncties: [Beheer openbare ruimte, Belastingheffing]
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Financieringsbron voor alle gemeentelijke water- en rioleringtaken; bepaalt de tariefstelling |
| Is herkenbaar voor domeinexperts | ✅ | Standaardbegrip in gemeentelijke financien en rioleringsbeheer; wettelijk verankerd |
| Heeft een eigen bestaan binnen het domein | ✅ | Eigen verordening, tarief, heffingsgrondslag en egalisatiereserve |
| Kan in meervoud bestaan | ✅ | Circa 178.800 aansluitingen in 2025, groeiend met ~3.000/jaar |
| Heeft een eigen levenscyclus | ✅ | Tariefvaststelling → heffing → inning → verantwoording; jaarlijkse cyclus |
| Heeft relaties met andere concepten | ✅ | [[Afvalstoffenheffing]], [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioleringsgebied\|Rioleringsgebied]] |

Score: 6/6.

## Beschrijving

De rioolheffing financiert alle gemeentelijke taken op het gebied van water en riolering. De heffing bestaat uit twee componenten:

- **Eigenarenheffing**: EUR 254,13 per jaar per aansluiting (tarief 2025)
- **Grootverbruikersheffing**: EUR 1,86 per m3 (tarief 2025)

In 2025 zijn er circa 178.800 aansluitingen, groeiend met ongeveer 3.000 per jaar door stadsgroei. De egalisatiereserve riolering (maximaal EUR 4 miljoen) dempt tariefschommelingen. De jaarlijkse tariefstijging ligt binnen een bandbreedte van 1,5-2,5% exclusief inflatie.

De rioolheffing is vergelijkbaar met de afvalstoffenheffing: beide zijn gemeentelijke bestemmingsheffingen die een specifiek beheerdomein financieren. Vergelijk [[Afvalstoffenheffing]] die al als BO is vastgelegd.

## Procesbron

Bron: [[visie-water-riolering 1|Visie Water en Riolering Utrecht]] en [[programma-water-riolering-2025-2029 1|Programma Water en Riolering Utrecht 2025-2029]]

> De rioolheffing dekt de kosten van het gemeentelijk water- en rioleringsbeleid. Het tarief wordt jaarlijks vastgesteld op basis van kostendekkendheid, met een egalisatiereserve om schommelingen te dempen.

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| associatie | [[Afvalstoffenheffing]] | bidirectioneel | Beleidsbron |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioleringsgebied\|Rioleringsgebied]] | bidirectioneel | Beleidsbron |

## Bedrijfsprocessen

- **Tariefvaststelling rioolheffing**: jaarlijkse berekening en vaststelling van het heffingstarief op basis van kostendekkendheid
- **Heffing en inning**: opleggen en innen van de rioolheffing bij perceeleigenaren en grootverbruikers
- **Kostentoerekening**: toerekening van kosten van water- en rioleringsbeheer aan de rioolheffing


## Bronnen

- [[visie-water-riolering 1]]
- [[programma-water-riolering-2025-2029 1]]

## Terugmelding GGM

> **Rioolheffing** — Gemeentelijke belasting voor de dekking van kosten van water- en rioleringsbeheer. Het GGM kent geen entiteit voor rioolheffing, terwijl Afvalstoffenheffing (vergelijkbare bestemmingsheffing) wel als BO is vastgelegd. Het concept heeft eigen processen voor tariefvaststelling, heffing en kostentoerekening. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
