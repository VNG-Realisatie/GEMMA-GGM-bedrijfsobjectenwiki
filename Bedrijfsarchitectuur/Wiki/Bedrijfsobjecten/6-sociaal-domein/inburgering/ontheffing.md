---
type: bedrijfsobject
naam: Ontheffing
onderwerp:
- Asiel en Integratie
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Ontheffing
ggm_guid: EAID_3F5932BD_C721_402d_8154_74A1CE097825
ggm_uml_type: Class
ggm_beleidsdomein: Inburgering
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- Inburgering
ggm_diagram_ids:
- EAID_96927C60_9F7B_4e67_806A_02EE0191983D
ggm_definitie: Een Ontheffing is een formeel besluit van de gemeente of van DUO waarbij een inburgeringsplichtige geheel of gedeeltelijk wordt vrijgesteld van onderdelen van de inburgeringsplicht, op grond van persoonlijke omstandigheden zoals medische beperkingen, psychische problematiek of aantoonbare inspanning.
ggm_toelichting: ''
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: ''
ggm_gemma_guid: ''
ggm_gemma_definitie: ''
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: ''
ggm_gemma_url: ''
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
ggm_duplicaat_entiteiten: []
bo_definitie: Formeel besluit waarbij een inburgeringsplichtige geheel of gedeeltelijk wordt ontheven van de inburgeringsplicht op grond van medische of bijzondere individuele omstandigheden.
bo_toelichting: Ontheffing vereist een medische deskundigenverklaring door een arts conform protocol (bijlage 1 Regeling inburgering 2021). Kosten €225, terugbetaald bij toewijzing. Arts adviseert ontheffing wanneer voorbereiding binnen vijf jaar met lichte aanpassingen niet mogelijk is.
bo_synoniemen: []
bo_homoniemen:
- bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/werk/ontheffing|Ontheffing (Werk)]]"
  ggm_entiteit: Ontheffing
  ggm_guid: EAID_8EE515EA_11F9_4f56_B9AA_F7B0904B39E7
  ggm_beleidsdomein: Werk
  toelichting: Ontheffing van arbeidsverplichtingen (Participatiewet) is een ander concept dan ontheffing van de inburgeringsplicht (Wi2021)
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht|Inburgeringsplicht]]'
  richting: naar-dit-BO
  kardinaliteit: 0..*
  beschrijving: Inburgeringsplicht kan leiden tot ontheffing(en)
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/examen|Examen]]'
  richting: van-dit-BO
  kardinaliteit: 0..*
  beschrijving: Ontheffing kan gelden voor specifieke examenonderdelen
bedrijfsprocessen:
- Beoordeling ontheffingsaanvraag inburgering
bedrijfsfuncties:
- Inburgering
---

# Ontheffing

Formeel besluit waarmee een inburgeringsplichtige geheel of gedeeltelijk wordt ontheven van onderdelen van de inburgeringsplicht, op grond van persoonlijke omstandigheden.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus (aanvraag → medisch onderzoek → advies → beschikking)
- ✅ Heeft relaties met andere concepten

De ontheffing wijzigt de scope van de [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht|Inburgeringsplicht]], net als [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/vrijstelling|Vrijstelling]], maar op andere gronden (persoonlijke omstandigheden vs. behaalde diploma's).

## GGM-bron

> Een Ontheffing is een formeel besluit van de gemeente of van DUO waarbij een inburgeringsplichtige geheel of gedeeltelijk wordt vrijgesteld van onderdelen van de inburgeringsplicht, op grond van persoonlijke omstandigheden zoals medische beperkingen, psychische problematiek of aantoonbare inspanning.

- **Entiteit:** Ontheffing
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** BeslissingOntheffing, DatumOntheffing
- **Matchsterkte:** exact

## Beschrijving

De Regeling inburgering 2021 onderscheidt twee ontheffingsgronden:

**Medische ontheffing** (art. 2.5): op basis van een deskundigenverklaring door een arts. De arts beoordeelt of de inburgeringsplichtige in staat is zich met lichte aanpassingen binnen vijf jaar voor te bereiden. Protocol conform bijlage 1. Kosten €225, terugbetaald bij advies tot (gedeeltelijke) ontheffing of advies aangepaste examenomstandigheden.

**Bijzondere individuele omstandigheden** (art. 2.6): de inburgeringsplichtige onderbouwt dat de omstandigheden het onmogelijk of uiterst moeilijk maken aan de plicht te voldoen, dat deze niet verwijtbaar zijn, en dat zonder ontheffing een zeer schrijnende situatie ontstaat. Bij medische component: medische machtiging vereist.

Gedeeltelijke ontheffing is mogelijk per examenonderdeel.

## Relaties

| Relatie | BO | Beschrijving |
|---|---|---|
| ← | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht\|Inburgeringsplicht]] | Inburgeringsplicht kan leiden tot ontheffing(en) |
| → | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/examen\|Examen]] | Ontheffing kan gelden voor specifieke examenonderdelen |

## Bronnen

- [[Wiki/Bronsamenvattingen/Asiel en Integratie/regeling-inburgering-2021]]
