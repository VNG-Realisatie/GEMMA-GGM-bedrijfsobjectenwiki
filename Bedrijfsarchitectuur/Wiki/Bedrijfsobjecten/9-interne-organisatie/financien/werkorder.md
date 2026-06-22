---
type: bedrijfsobject
naam: Werkorder
domein: [Financien]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Werkorder"
ggm_guid: EAID_4AF7FA48_DFB0_474f_B797_A13D5FD37530
ggm_uml_type: Class
ggm_beleidsdomein: "Financien"
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Financien Verwerken Mutaties]
ggm_diagram_ids: [EAID_B758018F_CB22_420e_B4E4_E17EB5F71EDA]
ggm_definitie: "Opdracht voor de uitvoering van een activiteit of een stap in een proces."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Werkorder"
ggm_gemma_guid: "5029f2d1-bad6-4813-8f59-d3f7981849e3"
ggm_gemma_definitie: "Opdracht voor de uitvoering van een activiteit of een stap in een proces."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-5029f2d1-bad6-4813-8f59-d3f7981849e3"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Opdracht voor de uitvoering van een specifieke activiteit of onderhoudstaak binnen de gemeente."
definitie: Opdracht voor de uitvoering van een activiteit of een stap in een proces
bedrijfsprocessen: [Operationeel beheer, Onderhoud]
bronnen: [Wiki/Bronsamenvattingen/Financien/raadgever-inkomstenbronnen, Wiki/Bronsamenvattingen/Financien/raadgever-gemeentebegroting, Wiki/Bronsamenvattingen/Financien/raadgever-financiele-verordening, Wiki/Bronsamenvattingen/Financien/raadgever-financiele-conditie]
bedrijfsfuncties: [Beheer openbare ruimte, Facilitair beheer]
status: concept
---

# Werkorder

Opdracht voor de uitvoering van een activiteit of een stap in een proces. In de gemeentelijke context: opdrachten voor onderhoud, inspectie of andere uitvoerende werkzaamheden.

## GGM-bron

> Opdracht voor de uitvoering van een activiteit of een stap in een proces.

- **Entiteit:** Werkorder
- **Beleidsdomein:** Financien (taakveld 9 — Interne Organisatie)
- **Attributen:** naam, omschrijving, code, werkordertype, documentnummer

## Bedrijfsprocessen

- **Operationeel beheer** — aansturen van uitvoerende werkzaamheden
- **Onderhoud** — planmatig en correctief onderhoud

## Bedrijfsfuncties

- **Beheer openbare ruimte** — werkorders voor onderhoud
- **Facilitair beheer** — werkorders voor interne diensten

## Relaties

- Gekoppeld aan een [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats|kostenplaats]]
- Kan leiden tot een [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/inkooporder|inkooporder]] bij externe uitvoering
