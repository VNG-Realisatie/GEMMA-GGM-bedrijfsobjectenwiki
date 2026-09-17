---
type: element
naam: Product
onderwerp: [Financien]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Product"
ggm_guid: EAID_04439F81_75DB_45cf_BE7A_352A54A95D73
ggm_uml_type: Class
ggm_beleidsdomein: "Financien"
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Financien Begroting en Budgetverantwoordelijkheid]
ggm_diagram_ids: [EAID_42C2960F_FED7_467e_AAB1_5195BED59A39]
ggm_definitie: "Het resultaat van een proces dat in het economisch verkeer een waarde bezit."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam: "Product"
ggm_gemma_guid: "d7ab242e-b050-4af7-a400-d87ce1eceb43"
ggm_gemma_definitie: "Het resultaat van een proces dat in het economisch verkeer een waarde bezit."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-d7ab242e-b050-4af7-a400-d87ce1eceb43"
ggm_gemma_bron:
ggm_gemma_alternate_name: "Product (Financien)"

ggm_duplicaat_entiteiten:
  - entiteit: Product
    guid: EAID_FF566C6B_077B_4914_8AF7_40EB1EDD388A
    beleidsdomein: Musea
    taakveld: "5 Sport, Cultuur en Recreatie"
    afwijkende_attributen:
  - entiteit: Product
    guid: EAID_D5DD2F67_6A1F_46b0_972E_795ECC4B2E4F
    beleidsdomein: ICT
    taakveld: "9 Interne Organisatie"
    afwijkende_attributen:

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Product** als directe tegenhanger. Daarnaast is **Product** (beleidsdomein Musea) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten. Daarnaast is **Product** (beleidsdomein ICT) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Balieverkoop** (detail) — Detailgegeven (geassocieerd met BO)
  - **Balieverkoop Entreekaart** (detail) — Detailgegeven (weinig attributen)
  - **Dienst** (detail) — Detailgegeven (geassocieerd met BO)
  - **Domein/Taakveld** (detail) — Detailgegeven (geassocieerd met BO)
  - **Entreekaart** (detail) — Detailgegeven (weinig attributen)
  - **Omzetgroep** (detail) — Detailgegeven (geassocieerd met BO)
  - **Onderwerp** (detail) — Detailgegeven (weinig attributen)
  - **Prijs** (detail) — Detailgegeven (geassocieerd met BO)
  - **Prijzenboek** (detail) — Detailgegeven (geassocieerd met BO)
  - **Productgroep** (classificatie) — Administratieve classificatie
  - **Winkelvoorraaditem** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Het resultaat van een proces dat in het economisch verkeer een waarde bezit."
bo_toelichting:
definitie: Het resultaat van een proces dat in het economisch verkeer een waarde bezit
bedrijfsprocessen: [Dienstverlening, Producten- en dienstencatalogus beheer]
bedrijfsfuncties: [Dienstverlening, Financieel beheer]
status: concept
---

# Product

Het resultaat van een proces dat in het economisch verkeer een waarde bezit. In de gemeentelijke context: de producten en diensten die de gemeente levert aan inwoners en bedrijven.

## GGM-bron

> Het resultaat van een proces dat in het economisch verkeer een waarde bezit.

- **Entiteit:** Product
- **Beleidsdomein:** Financien (taakveld 9 — Interne Organisatie)
- **Attributen:** naam, omschrijving, nummer

## Bedrijfsprocessen

- **Dienstverlening** — producten die de gemeente levert
- **Producten- en dienstencatalogus beheer** — beheer van het productaanbod

## Bedrijfsfuncties

- **Dienstverlening** — uitvoering
- **Financieel beheer** — kostprijsberekening per product

## Relaties

- leges worden geheven voor specifieke producten/diensten
- Gekoppeld aan [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/kostenplaats|kostenplaats]] voor kostentoerekening
- Onderdeel van een [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/taakveld|taakveld]]

## Bronnen

- [[Wiki/Bronsamenvattingen/Financien/raadgever-inkomstenbronnen]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-gemeentebegroting]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-financiele-verordening]]
- [[Wiki/Bronsamenvattingen/Financien/raadgever-financiele-conditie]]
