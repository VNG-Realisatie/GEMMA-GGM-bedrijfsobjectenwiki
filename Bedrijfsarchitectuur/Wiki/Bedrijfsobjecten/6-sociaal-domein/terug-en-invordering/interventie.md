---
type: bedrijfsobject
naam: Interventie
domein: [Terug-en-invordering]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Interventie"
ggm_guid: EAID_1BCE2533_656D_D59B_6ECD_28FC06D8D601
ggm_uml_type: Class
ggm_beleidsdomein: "Terug- en invordering"
ggm_taakveld: "Inkomen"
ggm_diagram: [Diagram Terug- en invordering]
ggm_diagram_ids: [EAID_CE436DEE_AB15_4f23_B191_FA8A63FB488D]
ggm_definitie: "De daadwerkelijke interventie, die wordt ondernomen naar aanleiding van een interventieverzoek."
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
  Dit BO heeft de GGM-entiteit **Interventie** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Interventieverzoek** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Actie die de gemeente onderneemt om betaling op een openstaande vordering te bewerkstelligen."
bo_toelichting: ''
definitie: Daadwerkelijke interventie die wordt ondernomen naar aanleiding van een interventieverzoek bij het achterwege blijven van aflossingen
bedrijfsprocessen: [Invordering, Handhaving]
bedrijfsfuncties: [Inning en invordering]
status: concept
---

# Interventie

De daadwerkelijke interventie die wordt ondernomen naar aanleiding van achterblijvende aflossingen. Interventies volgen een interventieladder (escalatie), maar een medewerker kan daar gemotiveerd van afwijken.

## GGM-bron

> De daadwerkelijke interventie, die wordt ondernomen naar aanleiding van een interventieverzoek.

- **Entiteit:** Interventie
- **Beleidsdomein:** Terug-en-invordering (taakveld 6 — Sociaal Domein → Inkomen)
- **Attributen:** Beslisdatum, Ingangsdatum, Interventietype

**Gerelateerde GGM-entiteit (niet als apart bedrijfsobject):** Interventieverzoek — signaal bij achterblijvende aflossingen dat tot interventie leidt.

## Bedrijfsprocessen

- **Invordering** — escalatie bij niet-betaling
- **Handhaving** — dwangmaatregelen

## Bedrijfsfuncties

- **Inning en invordering** — interventieladder

## BO-definitie

De GGM-definitie klopt grotendeels maar is aangepast voor de gemeentelijke context en leesbaarheid.

## Relaties

- Betreft een [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering|vordering]] via een [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/aflossingsplan|aflossingsplan]]
- Gericht aan een [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/debiteur|debiteur]]
- In belastingcontext vergelijkbaar: de invorderingsambtenaar kan aanmaningen en dwangbevelen inzetten als interventies

## Bronnen

- [[Wiki/Bronsamenvattingen/Belastingen/invordering-en-kwijtschelding]]
