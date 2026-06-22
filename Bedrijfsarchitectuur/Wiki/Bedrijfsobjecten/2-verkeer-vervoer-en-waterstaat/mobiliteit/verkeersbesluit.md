---
type: bedrijfsobject
naam: Verkeersbesluit
domein: [mobiliteit]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Verkeersbesluit"
ggm_guid: EAID_3F83DAA3_C37F_42b2_8D35_D75B840172F8
ggm_uml_type: Class
ggm_beleidsdomein: "Mobiliteit"
ggm_taakveld: "2 Verkeer, Vervoer en Waterstaat"
ggm_diagram: [Verkeersbesluiten]
ggm_diagram_ids: [EAID_280799E6_5FC1_4cd0_90E6_F4DB9C7A78A3]
ggm_definitie: "Een besluit van een wegbeheerder om een bepaald verkeersteken te plaatsen, te wijzigen of in te trekken of een bepaalde fysieke maatregel te treffen. "
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Verkeersbesluit"
ggm_gemma_guid: "833312cc-f7d8-4b4c-9e79-b21c8e7597cb"
ggm_gemma_definitie: "Een besluit van een wegbeheerder om een bepaald verkeersteken te plaatsen, te wijzigen of in te trekken of een bepaalde fysieke maatregel te treffen."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-833312cc-f7d8-4b4c-9e79-b21c8e7597cb"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "gelijk aan GGM"
bedrijfsprocessen: [Verkeersmanagement, Wegbeheer]
bedrijfsfuncties: [Verkeersmanagement]
bronnen: [Wiki/Bronsamenvattingen/mobiliteit/kwaliteitsnet-goederenvervoer-2007, Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040, Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-fiets-2021, Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-auto-2021, Wiki/Bronsamenvattingen/mobiliteit/module-parkeernormen, Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeerhubs, Wiki/Bronsamenvattingen/mobiliteit/rapportage-routekaart-parkeerhubs, Wiki/Bronsamenvattingen/mobiliteit/uitwerking-fietsparkeren, Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeren-openbare-ruimte, Wiki/Bronsamenvattingen/mobiliteit/uitwerking-toegankelijkheid, Wiki/Bronsamenvattingen/mobiliteit/parkeervisie, Wiki/Bronsamenvattingen/mobiliteit/uitvoeringsprogramma-betaald-parkeren]
relaties:
  - type: associatie
    bedrijfsobject: "Zero-emissiezone"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Verkeersbesluit vormt de juridische grondslag voor instelling van een zero-emissiezone"
---

# Verkeersbesluit

Een besluit van een wegbeheerder om een bepaald verkeersteken te plaatsen, te wijzigen of in te trekken of een bepaalde fysieke maatregel te treffen.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — formeel besluit dat verkeersmaatregelen juridisch grondvest
- ✅ Is herkenbaar voor domeinexperts — verkeerskundigen en juristen werken dagelijks met verkeersbesluiten
- ✅ Heeft een eigen bestaan binnen het domein — zelfstandig juridisch document, onafhankelijk van de fysieke maatregel
- ✅ Kan in meervoud bestaan — 30 km/u-zone, eenrichtingsverkeer, geslotenverklaring vrachtverkeer
- ✅ Heeft een eigen levenscyclus — ontwerp, inspraak, publicatie, inwerkingtreding, intrekking
- ✅ Heeft relaties met andere concepten — grondslag voor zero-emissiezones, verkeerstekens, fysieke maatregelen

## Beschrijving

Een verkeersbesluit is een formeel besluit van de gemeente als wegbeheerder om verkeerstekens te plaatsen, te wijzigen of in te trekken, of om fysieke verkeersmaatregelen te treffen. In Utrecht onderbouwen verkeersbesluiten onder meer de 30 km/u-invoering, compartimentering van de binnenstad en instelling van zero-emissiezones.

## GGM-bron

> "Een besluit van een wegbeheerder om een bepaald verkeersteken te plaatsen, te wijzigen of in te trekken of een bepaalde fysieke maatregel te treffen."
> — GGM, Verkeersbesluit (EAID_3F83DAA3), beleidsdomein Mobiliteit

Matchsterkte: exact.

## Relaties

- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/zero-emissiezone|Zero-emissiezone]] — juridische grondslag voor instelling van de zone [0..*]
