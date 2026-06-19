---
type: bedrijfsobject
naam: Kwijtschelding
domein: [Terug-en-invordering, Belastingen]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Kwijtschelding
ggm_beleidsdomein: Terug-en-invordering
definitie: Het kwijtschelden van het restant van de vordering
gerelateerde_begrippen: [kwijtschelding]
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

Het GGM modelleert kwijtschelding in het kader van terugvordering bijstand (Participatiewet). In het belastingdomein wordt kwijtschelding verleend op grond van de Invorderingswet 1990 aan belastingplichtigen die niet anders dan met buitengewoon bezwaar kunnen betalen. Zie begrip [[kwijtschelding]] voor de belastingcontext.

De structuur (bedrag, reden, boekingsdatum) is in beide contexten vergelijkbaar — een kandidaat voor generalisatie in het GGM.

## Bedrijfsprocessen

- **Invordering** — kwijtschelding als uitkomst van het invorderingsproces
- **Kwijtscheldingsbeoordeling** — toetsing op vermogen en betalingscapaciteit

## Bedrijfsfuncties

- **Inning en invordering** — kwijtscheldingsverlening

## Relaties

- Beëindigt (restant van) een [[vordering]]
- Betreft een [[debiteur]]
- In belastingcontext: verleend door de [[invorderingsambtenaar]]
- In belastingcontext: betreft een [[belastingaanslag]]
