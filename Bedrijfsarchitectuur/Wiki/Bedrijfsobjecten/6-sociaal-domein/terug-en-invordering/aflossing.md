---
type: bedrijfsobject
naam: Aflossing
domein: [Terug-en-invordering]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Aflossing"
ggm_guid: EAID_196161F4_8372_6334_AF08_263C236F7A38
ggm_uml_type: Class
ggm_beleidsdomein: "Terug- en invordering"
ggm_taakveld: "Inkomen"
ggm_diagram: [Diagram Terug- en invordering]
ggm_diagram_ids: [EAID_CE436DEE_AB15_4f23_B191_FA8A63FB488D]
ggm_definitie: "Een aflossing is de betaling van een afgesproken of opgelegd bedrag op een vordering. Een aflossing gebeurt in het kader van een aflossingsafspraak gemaakt bij een vordering of wordt eenzijdig opgelegd. De aflossing wordt geadministreerd als een vorderingscomponent onder die vordering. Afgesproken is minnelijk maar kan ook opgelegd worden, bijv 5% verrekening of beslag op loon."
ggm_toelichting: ""
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
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Aflossing** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Aflossingsafspraak** (detail) — Detailgegeven (geassocieerd met BO)
  - **Loonbeslagafspraak** (detail) — Detailgegeven (weinig attributen)
bo_definitie: "Een aflossing is de betaling van een afgesproken of opgelegd bedrag op een vordering."
bo_toelichting: "Een aflossing gebeurt in het kader van een aflossingsafspraak gemaakt bij een vordering of wordt eenzijdig opgelegd. De aflossing wordt geadministreerd als een vorderingscomponent onder die vordering. Afgesproken is minnelijk maar kan ook opgelegd worden, bijv. 5% verrekening of beslag op loon."
definitie: De betaling van een afgesproken of opgelegd bedrag op een vordering
bedrijfsprocessen: [Invordering, Betalingsverwerking]
bedrijfsfuncties: [Inning en invordering]
status: concept
---

# Aflossing

De betaling van een afgesproken of opgelegd bedrag op een vordering. Een aflossing gebeurt in het kader van een aflossingsafspraak of wordt eenzijdig opgelegd (bijv. 5% verrekening of beslag op loon).

## GGM-bron

> Een aflossing is de betaling van een afgesproken of opgelegd bedrag op een vordering. Een aflossing gebeurt in het kader van een aflossingsafspraak gemaakt bij een vordering of wordt eenzijdig opgelegd. De aflossing wordt geadministreerd als een vorderingscomponent onder die vordering. Afgesproken is minnelijk maar kan ook opgelegd worden, bijv 5% verrekening of beslag op loon.

- **Entiteit:** Aflossing
- **Beleidsdomein:** Terug-en-invordering (taakveld 6 — Sociaal Domein → Inkomen)
- **Attributen:** Aflossingskenmerk, Bedrag, Boekingsdatum, Ontvangstdatum

## Bedrijfsprocessen

- **Invordering** — ontvangst van betalingen
- **Betalingsverwerking** — administratieve verwerking

## Bedrijfsfuncties

- **Inning en invordering** — betalingen bijhouden

## Relaties

- Onderdeel van een [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/aflossingsplan|aflossingsplan]]
- Betaling op een [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering|vordering]]
- Bij te veel ontvangen: leidt tot [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/restitutie|restitutie]]

## Bronnen

- [[Wiki/Bronsamenvattingen/Belastingen/invordering-en-kwijtschelding]]
