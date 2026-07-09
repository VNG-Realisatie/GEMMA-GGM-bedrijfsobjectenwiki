---
type: element
naam: Grondstoffendepot
onderwerp: [Milieu]
archimate_type: "business-object"
grondslag: procesobject
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
bo_definitie: "Opslaglocatie voor vrijkomende materialen uit de openbare ruimte, bestemd voor hergebruik in projecten."
bo_toelichting:
bedrijfsprocessen: [Materiaalopslag, Materiaalmatch (vraag-aanbod), Circulair beheer openbare ruimte]
bedrijfsfuncties: [Beheer openbare ruimte, Circulaire economie]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Grondstofstroom]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: opslag van materiaalstromen
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Cruciaal voor circulair hergebruik van materialen |
| Herkenbaar voor domeinexperts | ✅ Herkenbaar als fysieke voorziening in circulair beleid |
| Heeft eigen bestaan | ✅ Zelfstandige fysieke locatie |
| Kan in meervoud bestaan | ✅ Meerdere depots mogelijk per gemeente |
| Heeft eigen levenscyclus | ✅ Locatieverwerving → inrichting → exploitatie → eventueel sluiting |
| Heeft relaties met andere concepten | ✅ Grondstofstromen, materiaalpasspoorten, projecten openbare ruimte |

**6/6 criteria van toepassing.**

## Beschrijving

Een grondstoffendepot is een opslaglocatie waar materialen uit projecten in de openbare ruimte (trottoirtegels, betonklinkers, zand, puin) worden opgeslagen voor hergebruik in andere projecten. In Utrecht is een locatie verworven op Lage Weide. Materialen worden klaargemaakt voor hergebruik (palletiseren, schonen). Het depot is verbonden met een digitaal platform voor het matchen van vraag en aanbod van materialen. Onderdeel van het principe 'hergebruik, tenzij'. Minimaliseert transportbewegingen.

> "Onze grondstoffendepots richten we zo in dat de materialen die daar worden opgeslagen, worden klaargemaakt voor hergebruik." (bron: [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-utrecht-circulair-2030|Beleidsnota Utrecht Circulair 2030]], par. B.4.2)

## Procesbron

Het grondstoffendepot ontstaat uit beleid voor circulaire gebiedsontwikkeling. Het GGM-domein Afval richt zich op huishoudelijk afval, niet op materiaalhergebruik uit de openbare ruimte.

## Relaties

- **[[Grondstofstroom]]** — het depot slaat materiaalstromen op voor hergebruik


## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-utrecht-circulair-2030]]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor grondstoffendepots. Het GGM-domein Afval richt zich op huishoudelijk afval, niet op materiaalhergebruik uit de openbare ruimte. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Bedrijfsprocessen

- Materiaalopslag
- Materiaalmatch (vraag-aanbod)
- Circulair beheer openbare ruimte

## Bedrijfsfuncties

- Beheer openbare ruimte
- Circulaire economie
