---
type: element
naam: Beschikking Leerlingenvervoer
onderwerp: [onderwijs]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Beschikking Leerlingenvervoer
ggm_guid: EAID_81870665_768C_4fb2_8A4F_A9CB7989C884
ggm_uml_type: Class
ggm_beleidsdomein: Leerplicht en Leerlingenvervoer
ggm_taakveld: "4 Onderwijs"
ggm_diagram: [Diagram Beslissingen Leerplicht]
ggm_diagram_ids: [EAID_26A453D9_47AF_487e_854B_3B4BC6D6A308]
ggm_definitie: "Een formeel besluit dat genomen wordt door een bevoegde instantie over het al dan niet toekennen van leerlingenvervoer aan een bepaalde leerling."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: BeschikkingLeerlingenvervoer
ggm_gemma_guid: "3f048a6b-523c-4e8e-a581-0fcc089f1ec6"
ggm_gemma_definitie: "Een formeel besluit dat genomen wordt door een bevoegde instantie over het al dan niet toekennen van leerlingenvervoer aan een bepaalde leerling."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-3f048a6b-523c-4e8e-a581-0fcc089f1ec6"
ggm_gemma_bron:
ggm_gemma_alternate_name:

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Beschikking Leerlingenvervoer** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Beslissing** (detail) — Detailgegeven (geassocieerd met BO)
  - **HALT-verwijzing** (detail) — Te specifiek; justitie-subtype
bo_definitie: "Een formeel besluit dat genomen wordt door een bevoegde instantie over het al dan niet toekennen van leerlingenvervoer aan een bepaalde leerling."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Aanvraag Leerlingenvervoer]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Beschikking volgt op aanvraag"
  - type: associatie
    bedrijfsobject: "[[Leerling]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Beschikking betreft leerling"
bedrijfsprocessen: [Leerlingenvervoer]
bedrijfsfuncties: [Leerplicht]
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Formeel besluit dat het recht op leerlingenvervoer vastlegt |
| Herkenbaar voor domeinexperts | ✅ Elke aanvraag resulteert in een beschikking |
| Heeft eigen bestaan | ✅ Juridisch document met eigen kenmerken en rechtsgevolgen |
| Kan in meervoud bestaan | ✅ Tientallen tot honderden beschikkingen per gemeente per jaar |
| Heeft eigen levenscyclus | ✅ Opstellen → verlenen/afwijzen → eventueel bezwaar → eventueel intrekking |
| Heeft relaties met andere concepten | ✅ Aanvraag, leerling, vervoerder |

**6/6 criteria van toepassing.**

## Beschrijving

Een beschikking leerlingenvervoer is het formele besluit van de gemeente over het toekennen of afwijzen van leerlingenvervoer aan een leerling. De beschikking volgt op een aanvraag en bepaalt welke vervoersvoorziening wordt toegekend (aangepast vervoer, openbaar vervoer of een vergoeding). Tegen de beschikking kan bezwaar worden gemaakt.

## GGM-bron

> "Een formeel besluit dat genomen wordt door een bevoegde instantie over het al dan niet toekennen van leerlingenvervoer aan een bepaalde leerling."
> — GGM-entiteit: Beschikking Leerlingenvervoer, beleidsdomein: Leerplicht en Leerlingenvervoer

**Matchsterkte: exact.** De GGM-entiteit beschrijft hetzelfde concept.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Aanvraag Leerlingenvervoer]] | associatie | ← | 1 | GGM |
| [[Leerling]] | associatie | ← | 1 | GGM |

**GGM-relaties zonder BO-equivalent:**
- Vervoerder — partij die het vervoer uitvoert

## Bedrijfsprocessen

- **Leerlingenvervoer** — beschikken op aanvragen, toekennen vervoersvoorziening

## Bedrijfsfuncties

- Leerplicht

## Bronnen

- [[Wiki/Bronsamenvattingen/onderwijs/leerlingenvervoer]]
