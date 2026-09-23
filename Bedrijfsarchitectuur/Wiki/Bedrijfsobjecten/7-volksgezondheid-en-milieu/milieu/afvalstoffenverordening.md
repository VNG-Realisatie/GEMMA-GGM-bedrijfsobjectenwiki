---
type: element
naam: Afvalstoffenverordening
onderwerp: [Milieu]
archimate_type: "business-object"
grondslag: "governance-object"
ggm_entiteit:
ggm_beleidsdomein:
ggm_guid:
ggm_uml_type:
ggm_taakveld:
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
bo_definitie: "Gemeentelijke verordening met regels voor inzameling en beheer van huishoudelijke afvalstoffen."
bo_toelichting:
bedrijfsprocessen: [Verordeningsvaststelling, Handhaving afvalbeleid]
bedrijfsfuncties: [Afvalbeheer, Regelgeving]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Grondstofstroom]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: regelt inzameling per stroom
  - type: associatie
    bedrijfsobject: "[[Afvalstoffenheffing]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: grondslag voor heffing
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Juridisch kader voor afvalbeheer |
| Herkenbaar voor domeinexperts | ✅ Elke gemeente heeft een afvalstoffenverordening |
| Heeft eigen bestaan | ✅ Zelfstandig juridisch document |
| Kan in meervoud bestaan | ✅ Per gemeente |
| Heeft eigen levenscyclus | ✅ Vaststelling → wijziging → intrekking |
| Heeft relaties met andere concepten | ✅ Grondstofstromen, afvalstoffenheffing, handhaving |

**5/6 criteria van toepassing.** Besluit: BO gehouden — zelfde patroon als het al vastgestelde BO [[Wiki/Bedrijfsobjecten/99-kern/heffingsverordening|Heffingsverordening]] (verordening als juridische grondslag naast de operationele heffing zelf); governance-instrumenten van dit type (regeling/verordening) zijn volgens de BO-methodiek expliciet BO-waardig.

## Beschrijving

De afvalstoffenverordening is een gemeentelijke verordening op grond van de Wet Milieubeheer. De verordening stelt regels voor hoe huishoudelijk afval moet worden ingezameld, welke stromen gescheiden worden en de frequentie van inzameling. De verordening kan gebieden aanwijzen met alternatieve inzamelmethoden (bijv. binnenstad). Het opt-in systeem voor ongeadresseerd reclamedrukwerk is via deze verordening geimplementeerd.

## Juridische bron

De Wet Milieubeheer verplicht gemeenten tot vaststelling van een afvalstoffenverordening. De verordening vormt de juridische grondslag voor de [[Afvalstoffenheffing]] en regelt de inzameling per [[Grondstofstroom]].

## Relaties

- **[[Grondstofstroom]]** — de verordening regelt de inzameling per afvalstroom
- **[[Afvalstoffenheffing]]** — de verordening vormt de grondslag voor de heffing


## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/grondstoffennota-utrecht-2020]]

## Terugmelding GGM

GGM-hiaat. De afvalstoffenverordening is een governance-object; governance-objecten zijn in het GGM niet compleet gedekt. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Bedrijfsprocessen

- Verordeningsvaststelling
- Handhaving afvalbeleid

## Bedrijfsfuncties

- Afvalbeheer
- Regelgeving
