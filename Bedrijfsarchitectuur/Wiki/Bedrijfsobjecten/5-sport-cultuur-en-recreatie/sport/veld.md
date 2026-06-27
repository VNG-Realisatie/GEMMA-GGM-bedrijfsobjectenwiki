---
type: bedrijfsobject
naam: Veld
domein: [Sport en Bewegen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Veld"
ggm_guid: EAID_D1889096_CC76_48a8_A9DF_8151FFF1E0AC
ggm_uml_type: Class
ggm_beleidsdomein: "Sport"
ggm_taakveld: "5 Sport, Cultuur en Recreatie"
ggm_diagram: [Diagram Sportbeleid, Diagram Sportbeleid Locaties]
ggm_diagram_ids: [EAID_25BCAA7D_6255_4f3a_8408_DF91881FE29F, EAID_BA23F316_FE48_49a8_A26D_9B1D14713F76]
ggm_definitie: "Een stuk land dat speciaal voor het bedrijven van een veldsport gereedgemaakt is"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Veld"
ggm_gemma_guid: "0f53081c-01f9-4c0a-b049-77d310a0ea33"
ggm_gemma_definitie: "Een stuk land dat speciaal voor het bedrijven van een veldsport gereedgemaakt is"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-0f53081c-01f9-4c0a-b049-77d310a0ea33"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
bo_definitie: "Stuk land dat specifiek is ingericht voor het bedrijven van een veldsport."
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[Sportpark]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..1"
    beschrijving: "Een veld ligt op een sportpark"
bedrijfsprocessen: [Capaciteitsplanning sport, Kunstgrasconversie, Sportveldbeheer]
bedrijfsfuncties: [Sportaccommodatiebeheer]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis (capaciteitsberekeningen per sporttype), herkenbaar (voetbalveld, hockeyveld), eigen bestaan (fysiek terrein), meervoud (tientallen in Utrecht), levenscyclus (aanleg, gras-naar-kunstgras conversie, onderhoud), relaties met [[Sportpark]], Belijning, OverigBenoemdTerrein.

## Beschrijving

Een sportveld is een stuk land dat speciaal voor het bedrijven van een veldsport is ingericht. De gemeente voert capaciteitsberekeningen uit per sporttype (voetbal, hockey, tennis, rugby) en stuurt op conversie van natuurgras naar kunstgras om capaciteit te verhogen. Er zijn tekorten bij hockey, tennis en rugby, en een zaterdagpiek bij voetbal.

## GGM-bron

> "Een stuk land dat speciaal voor het bedrijven van een veldsport gereedgemaakt is" (GGM, entiteit Veld, beleidsdomein Sport)

- **Entiteit:** Veld
- **Beleidsdomein:** Sport
- **Attributen:** *(geen)*
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Sportpark]] | onderdeel van | 0..1 | GGM |
| Belijning | heeft | 0..* | GGM |
| OverigBenoemdTerrein (BAG) | ligt op | 1 | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Sport en Bewegen/beleidsnota-sport-en-bewegen-2025-2032]]
