---
type: bedrijfsobject
naam: Kwijtschelding
domein: [Terug-en-invordering, Belastingen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Kwijtschelding"
ggm_guid: EAID_1127D07A_473D_2912_29AE_2ABDF0E8A586
ggm_uml_type: Class
ggm_beleidsdomein: "Terug- en invordering"
ggm_taakveld: "Inkomen"
ggm_diagram: [Diagram Terug- en invordering]
ggm_diagram_ids: [EAID_CE436DEE_AB15_4f23_B191_FA8A63FB488D]
ggm_definitie: "Het kwijtschelden van het restant van de vordering.RedenenDit kan om diverse redenen gebeuren, waaronder redenen uit het beleid.Als een debiteur zijn 36 maanden lang houdt aan de betaalafspraken, dan komt de debiteur in aanmerking voor kwijtschelding. Enkele noties hierbij:Het gaat hier om het houden van de afspraken.Hieronder vallen ook afspraken om tijdelijk niet af te lossen.In principe zal een enkele maand opschorten vanwege een maand niet betalen niet de betaaldiscipline verbreken, omdat de gemeente niet heeft ingegrepen via een interventie.Als de debiteur ineens de helft of meer aflost op de vordering.BedragHet bedrag in de kwijtschelding heeft die hoogte dat de totale restant van de vordering op nul komt."
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
  Dit BO heeft de GGM-entiteit **Kwijtschelding** als directe tegenhanger.
bo_definitie: "Het kwijtschelden van het restant van de vordering."
bo_toelichting: "Dit kan om diverse redenen gebeuren, waaronder redenen uit het beleid. Als een debiteur 36 maanden lang houdt aan de betaalafspraken, komt de debiteur in aanmerking voor kwijtschelding. Hieronder vallen ook afspraken om tijdelijk niet af te lossen. Als de debiteur ineens de helft of meer aflost op de vordering. Het bedrag in de kwijtschelding heeft die hoogte dat de totale restant van de vordering op nul komt."
definitie: Het kwijtschelden van het restant van de vordering
bedrijfsprocessen: [Invordering, Kwijtscheldingsbeoordeling]
bedrijfsfuncties: [Inning en invordering]
status: concept
---

# Kwijtschelding (bedrijfsobject)

Het kwijtschelden van het restant van de vordering. Kan om diverse redenen plaatsvinden, waaronder beleid (bijv. 36 maanden aflossingsdicipline) of het ineens aflossen van de helft of meer.

## GGM-bron

> Het kwijtschelden van het restant van de vordering. Dit kan om diverse redenen gebeuren, waaronder redenen uit het beleid. Als een debiteur zijn 36 maanden lang houdt aan de betaalafspraken, dan komt de debiteur in aanmerking voor kwijtschelding. Als de debiteur ineens de helft of meer aflost op de vordering. Het bedrag in de kwijtschelding heeft die hoogte dat de totale restant van de vordering op nul komt.

- **Entiteit:** Kwijtschelding
- **Beleidsdomein:** Terug-en-invordering (taakveld 6 — Sociaal Domein → Inkomen)
- **Attributen:** Bedrag, Boekingsdatum, Reden

## Contextverschil GGM vs. belastingdomein

Het GGM modelleert kwijtschelding in het kader van terugvordering bijstand (Participatiewet). In het belastingdomein wordt kwijtschelding verleend op grond van de Invorderingswet 1990 aan belastingplichtigen die niet anders dan met buitengewoon bezwaar kunnen betalen. Zie begrip kwijtschelding voor de belastingcontext.

De structuur (bedrag, reden, boekingsdatum) is in beide contexten vergelijkbaar — een kandidaat voor generalisatie in het GGM.

## Bedrijfsprocessen

- **Invordering** — kwijtschelding als uitkomst van het invorderingsproces
- **Kwijtscheldingsbeoordeling** — toetsing op vermogen en betalingscapaciteit

## Bedrijfsfuncties

- **Inning en invordering** — kwijtscheldingsverlening

## Relaties

- Beëindigt (restant van) een [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering|vordering]]
- Betreft een [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/debiteur|debiteur]]
- In belastingcontext: verleend door de invorderingsambtenaar
- In belastingcontext: betreft een belastingaanslag

## Bronnen

- [[Wiki/Bronsamenvattingen/Belastingen/invordering-en-kwijtschelding]]
