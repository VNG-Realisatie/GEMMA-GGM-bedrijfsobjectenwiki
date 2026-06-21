---
type: bedrijfsobject
naam: Afvalstoffenverordening
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
gemma_definitie: "Gemeentelijke verordening met regels voor inzameling en beheer van huishoudelijke afvalstoffen."
bedrijfsprocessen: [Verordeningsvaststelling, Handhaving afvalbeleid]
bedrijfsfuncties: [Afvalbeheer, Regelgeving]
relaties:
  - type: associatie
    bedrijfsobject: "[[Grondstofstroom]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: regelt inzameling per stroom
  - type: associatie
    bedrijfsobject: "[[Afvalstoffenheffing]]"
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: grondslag voor heffing
---

> **ter discussie** — Type is governance-object. Het team moet beoordelen of governance-instrumenten als BO worden opgenomen.

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Juridisch kader voor afvalbeheer |
| Herkenbaar voor domeinexperts | ✅ Elke gemeente heeft een afvalstoffenverordening |
| Heeft eigen bestaan | ✅ Zelfstandig juridisch document |
| Kan in meervoud bestaan | ✅ Per gemeente |
| Heeft eigen levenscyclus | ✅ Vaststelling → wijziging → intrekking |
| Heeft relaties met andere concepten | ✅ Grondstofstromen, afvalstoffenheffing, handhaving |

**5/6 criteria van toepassing.** Kanttekening: het is een verordening, geen 'ding' in operationele zin.

## Beschrijving

De afvalstoffenverordening is een gemeentelijke verordening op grond van de Wet Milieubeheer. De verordening stelt regels voor hoe huishoudelijk afval moet worden ingezameld, welke stromen gescheiden worden en de frequentie van inzameling. De verordening kan gebieden aanwijzen met alternatieve inzamelmethoden (bijv. binnenstad). Het opt-in systeem voor ongeadresseerd reclamedrukwerk is via deze verordening geimplementeerd.

## Juridische bron

De Wet Milieubeheer verplicht gemeenten tot vaststelling van een afvalstoffenverordening. De verordening vormt de juridische grondslag voor de [[Afvalstoffenheffing]] en regelt de inzameling per [[Grondstofstroom]].

## Relaties

- **[[Grondstofstroom]]** — de verordening regelt de inzameling per afvalstroom
- **[[Afvalstoffenheffing]]** — de verordening vormt de grondslag voor de heffing

## Terugmelding GGM

GGM-hiaat. Als governance-object valt de afvalstoffenverordening structureel buiten de GGM-scope (het GGM modelleert data, niet governance). Zie [[Wiki/Analyses/ggm-terugmeldingen]].

## Bedrijfsprocessen

- Verordeningsvaststelling
- Handhaving afvalbeleid

## Bedrijfsfuncties

- Afvalbeheer
- Regelgeving
