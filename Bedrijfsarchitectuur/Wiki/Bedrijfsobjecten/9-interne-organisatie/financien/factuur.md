---
type: bedrijfsobject
naam: Factuur
domein: [Financien]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Factuur"
ggm_guid: EAID_E1DA56C3_6ECA_4ec9_8CF4_FC57E1C43102
ggm_uml_type: Class
ggm_beleidsdomein: "Financien"
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Financien Verwerken Mutaties, Financien Verplichtingen en Facturen]
ggm_diagram_ids: [EAID_B758018F_CB22_420e_B4E4_E17EB5F71EDA, EAID_0723EB5C_4A2C_44d4_B15B_37AC71B5D711]
ggm_definitie: "Schriftelijke rekening of nota voor de geleverde zaken of verrichte diensten."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Factuur"
ggm_gemma_guid: "e3c92496-53d2-473e-9643-9774cdda2891"
ggm_gemma_definitie: "Schriftelijke rekening of nota voor de geleverde zaken of verrichte diensten."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-e3c92496-53d2-473e-9643-9774cdda2891"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Factuur** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Factuurregel** (onderdeel) — Onderdeel (naamindicatie)
bo_definitie: "Schriftelijke rekening of nota voor de geleverde zaken of verrichte diensten."
bo_toelichting: ''
definitie: Schriftelijke rekening of nota voor de geleverde zaken of verrichte diensten
bedrijfsprocessen: [Facturering, Crediteuren- en debiteurenadministratie]
bedrijfsfuncties: [Financieel beheer]
status: concept
---

# Factuur

Schriftelijke rekening of nota voor de geleverde zaken of verrichte diensten.

## GGM-bron

> Schriftelijke rekening of nota voor de geleverde zaken of verrichte diensten.

- **Entiteit:** Factuur
- **Beleidsdomein:** Financien (taakveld 9 — Interne Organisatie)
- **Attributen:** datumFactuur, omschrijving, code, betaaltermijn, betaalbaarPer, factuurbedragExclusiefBTW, factuurbedragBTW

## Bedrijfsprocessen

- **Facturering** — opstellen en verzenden van facturen
- **Crediteuren- en debiteurenadministratie** — verwerking van inkomende en uitgaande facturen

## Bedrijfsfuncties

- **Financieel beheer** — financiële administratie

## Relaties

- Gericht aan een [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/debiteur|debiteur]]
- Gekoppeld aan een [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/inkooporder|inkooporder]] (inkomende facturen) of aan een [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/product|product]] (uitgaande facturen)
- Verschilt van een belastingaanslag: een factuur is een privaatrechtelijke vordering, een aanslag een publiekrechtelijke

## Bronnen

- [[Wiki/Bronsamenvattingen/Financien/raadgever-inkomstenbronnen]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-gemeentebegroting]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-financiele-verordening]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-financiele-conditie]]
