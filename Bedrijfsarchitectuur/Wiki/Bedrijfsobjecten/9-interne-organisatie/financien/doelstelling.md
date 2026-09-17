---
type: element
naam: Doelstelling
onderwerp: [Financien]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Doelstelling"
ggm_guid: EAID_2FFE3BAD_CB0E_43ea_A435_FD693B9255C3
ggm_uml_type: Class
ggm_beleidsdomein: "Financien"
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Financien Begroting en Budgetverantwoordelijkheid]
ggm_diagram_ids: [EAID_42C2960F_FED7_467e_AAB1_5195BED59A39]
ggm_definitie: "Een op korte of middellange termijn nagestreefde situatie"
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam: "Doelstelling"
ggm_gemma_guid: "2bd07fb4-4cfb-4d89-ac99-cb2377decd2d"
ggm_gemma_definitie: "Een op korte of middellange termijn nagestreefde situatie"
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-2bd07fb4-4cfb-4d89-ac99-cb2377decd2d"
ggm_gemma_bron:
ggm_gemma_alternate_name: "Doelstelling (Financien)"

ggm_duplicaat_entiteiten:
  - entiteit: Doelstelling
    guid: EAID_28C572B5_C147_4b99_B920_00062C843FDE
    beleidsdomein: Sociale Teams
    taakveld: "6 Sociaal Domein"
    afwijkende_attributen:

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Doelstelling** als directe tegenhanger. Daarnaast is **Doelstelling** (beleidsdomein Sociale Teams) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Doelstellingsoort** (classificatie) — Typering/referentietabel
  - **Hoofdstuk** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Een op korte of middellange termijn nagestreefde situatie"
bo_toelichting:
definitie: Een op korte of middellange termijn nagestreefde situatie
bedrijfsprocessen: [Begrotingscyclus, Beleidsvorming]
bedrijfsfuncties: [Planning en control, Bestuur]
status: concept
---

# Doelstelling

Een op korte of middellange termijn nagestreefde situatie. Doelstellingen koppelen beleid aan begroting en verantwoording.

## GGM-bron

> Een op korte of middellange termijn nagestreefde situatie

- **Entiteit:** Doelstelling
- **Beleidsdomein:** Financien (taakveld 9 — Interne Organisatie)
- **Attributen:** naam, omschrijving, nummer

## Bedrijfsprocessen

- **Begrotingscyclus** — doelstellingen als onderbouwing van begrotingsposten
- **Beleidsvorming** — doelstellingen als vertaling van beleid naar meetbare resultaten

## Bedrijfsfuncties

- **Planning en control** — monitoring voortgang
- **Bestuur** — raad stelt doelstellingen vast

## Relaties

- Onderdeel van de [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting|begroting]]
- Kan gekoppeld zijn aan een [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/taakveld|taakveld]]

## Bronnen

- [[Wiki/Bronsamenvattingen/Financien/raadgever-inkomstenbronnen]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-gemeentebegroting]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-financiele-verordening]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-financiele-conditie]]
