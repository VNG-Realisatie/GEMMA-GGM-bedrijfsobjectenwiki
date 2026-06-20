---
type: bedrijfsobject
naam: Aflossingsplan
domein: [Terug-en-invordering]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Aflossingsplan"
ggm_guid: EAID_234EB82E_9EC6_5904_2634_263C0A957ADF
ggm_uml_type: Class
ggm_beleidsdomein: "Terug- en invordering"
ggm_taakveld: "Inkomen"
ggm_diagram: [Diagram Terug- en invordering]
ggm_diagram_ids: [EAID_CE436DEE_AB15_4f23_B191_FA8A63FB488D]
ggm_definitie: "Een aflossingsplan bevat alle afspraken tussen de gemeente en de debiteur over op welke vordering hij/zij per wanneer welk bedrag aflost.Verder geldt dat er bijzondere afspraken kunnen worden vastgelegd, bijvoorbeeld Dwangbevel. In zulke gevallen wordt de gehele schuld in één keer weer opeisbaar gesteld."
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
gemma_definitie: ""
definitie: Alle afspraken tussen de gemeente en de debiteur over op welke vordering per wanneer welk bedrag wordt afgelost
bedrijfsprocessen: [Invordering, Schuldbeheer]
bedrijfsfuncties: [Inning en invordering]
status: concept
---

# Aflossingsplan

Alle afspraken tussen de gemeente en de debiteur over op welke vordering hij/zij per wanneer welk bedrag aflost. Kan bijzondere afspraken bevatten, zoals bij een dwangbevel.

## GGM-bron

> Een aflossingsplan bevat alle afspraken tussen de gemeente en de debiteur over op welke vordering hij/zij per wanneer welk bedrag aflost. Verder geldt dat er bijzondere afspraken kunnen worden vastgelegd, bijvoorbeeld Dwangbevel. In zulke gevallen wordt de gehele schuld in één keer weer opeisbaar gesteld.

- **Entiteit:** Aflossingsplan
- **Beleidsdomein:** Terug-en-invordering (taakveld 6 — Sociaal Domein → Inkomen)
- **Attributen:** Aflossingskenmerk, Einddatum, Startdatum

**Gerelateerde GGM-entiteiten (niet als apart bedrijfsobject):** Aflossingsafspraak (individuele afspraak binnen het plan), Uitstel aflossing, Loonbeslagafspraak.

## Bedrijfsprocessen

- **Invordering** — afspraken maken over aflossing
- **Schuldbeheer** — monitoring van aflossingsdiscipline

## Bedrijfsfuncties

- **Inning en invordering** — aflossingsafspraken beheren

## Relaties

- Hoort bij een [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/debiteur|debiteur]]
- Betreft een of meer [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering|vordering]]en
- Bevat [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/aflossing|aflossing]]en als concrete betalingen
- Bij 36 maanden aflossingsdicipline: mogelijkheid tot kwijtschelding
- Bij achterstalligheid: [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/interventie|interventie]]
