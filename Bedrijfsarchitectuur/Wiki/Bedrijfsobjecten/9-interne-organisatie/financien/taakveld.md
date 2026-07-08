---
type: element
naam: Taakveld
domein: [Financien]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Taakveld"
ggm_guid: EAID_E81C0FA0_2203_489a_98E9_32F1CB200E75
ggm_uml_type: Class
ggm_beleidsdomein: "Financien"
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Financien Begroting en Budgetverantwoordelijkheid]
ggm_diagram_ids: [EAID_42C2960F_FED7_467e_AAB1_5195BED59A39]
ggm_definitie: "Een samenhangend geheel van activiteiten en taken en hangt onder een programma."
ggm_toelichting: "Een taakveld kan verbonden zijn aan een strategische opgave. Dat betekent dat het budget voor de activiteiten die nodig zijn om de opgave uit te voeren daar te vinden zijn."
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

ggm_duplicaat_entiteiten:
  - "EAID_01E83CEC_D69D_47eb_9BAB_252AABADDD18"

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Taakveld** als directe tegenhanger. Daarnaast is **Taakveld** (beleidsdomein Griffie) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten.
bo_definitie: "Een samenhangend geheel van activiteiten en taken en hangt onder een programma."
bo_toelichting: ''
definitie: Een samenhangend geheel van activiteiten en taken dat onder een programma hangt
bedrijfsprocessen: [Begrotingscyclus, IV3-verantwoording]
bedrijfsfuncties: [Planning en control, Financieel beheer]
status: concept
---

# Taakveld

Een samenhangend geheel van activiteiten en taken en hangt onder een programma. Taakvelden zijn afgeleid van de IV3-standaard (Informatie voor Derden) en vormen de structuur van zowel de gemeentebegroting als het GGM.

## GGM-bron

> Een samenhangend geheel van activiteiten en taken en hangt onder een programma.

- **Entiteit:** Taakveld
- **Beleidsdomein:** Financien (taakveld 9 — Interne Organisatie)
- **Attributen:** hoofdfunctie, hoofdfunctieOmschrijving, functiecodeIV3, functieomschrijvingIV3, taakveldcode, taakveldOmschrijving, subtaakveldCode, subtaakveldOmschrijving

## Bedrijfsprocessen

- **Begrotingscyclus** — taakvelden structureren de begroting
- **IV3-verantwoording** — verplichte rapportage aan CBS/BZK

## Bedrijfsfuncties

- **Planning en control** — taakvelden als indelingsprincipe

## Relaties

- Structureert de [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/begroting|begroting]]
- Het GGM is opgebouwd uit taakvelden met daaronder beleidsdomeinen (zie [[GGM-indeling]])
- Belastingopbrengsten zijn verdeeld over taakvelden; er is geen apart belastingtaakveld (zie [[Wiki/Analyses/ggm-hiaten-belastingendomein|ggm-hiaten-belastingendomein]])

## Bronnen

- [[Wiki/Bronsamenvattingen/Financien/raadgever-inkomstenbronnen]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-gemeentebegroting]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-financiele-verordening]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-financiele-conditie]]
