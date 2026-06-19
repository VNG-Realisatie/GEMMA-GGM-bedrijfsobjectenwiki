---
type: bedrijfsobject
naam: Vordering
domein: [Terug-en-invordering]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Vordering
ggm_beleidsdomein: Terug-en-invordering
definitie: Een eis op een persoon die een zeker bedrag (terug) moet betalen aan de gemeente
gerelateerde_begrippen: [belastingaanslag, kwijtschelding]
bedrijfsprocessen: [Terugvordering, Invordering]
bedrijfsfuncties: [Inning en invordering]
status: concept
---

# Vordering

Een eis op een persoon (debiteur) die een zeker bedrag (terug) moet betalen aan de gemeente. Kernobject van het invorderingsproces.

## GGM-bron

> Een vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag (terug) moet betalen aan de gemeente in het kader van de bijstand of een bijstandsgerelateerde uitkering. De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling. Vorderingen kunnen uit meerdere componenten bestaan. Vorderingen kunnen ook onderling in relatie staan.

- **Entiteit:** Vordering
- **Beleidsdomein:** Terug-en-invordering (taakveld 6 — Sociaal Domein → Inkomen)
- **Attributen:** Categorie, Fiscaal, Periode einddatum, Periode startdatum, Priotype, Regeling, Stuitingsvoortgangsindicator, Subcategorie, Titel, Vaststeldatum terugvordering, Verjaringsdatum, Verwerkingsstatus

**Specialisaties in GGM (niet als apart bedrijfsobject):** Boetevordering, Incassokostenvordering, Rentevordering, Verwijtbare vordering, Krediethypotheekvordering, Leenbijstandvordering.

## Bo-definitie (afwijkend)

De GGM-definitie beperkt zich tot bijstand; de bedrijfsobjectdefinitie is breder: "Een eis op een persoon die een zeker bedrag (terug) moet betalen aan de gemeente" — dekt ook belastingvorderingen en overige vorderingen.

## Bedrijfsprocessen

- **Terugvordering** — vaststellen van de vordering na constatering
- **Invordering** — innen van de vordering

## Bedrijfsfuncties

- **Inning en invordering** — beheer van vorderingen

## Relaties

- Gericht aan een [[debiteur]]
- Kan leiden tot een [[aflossingsplan]]
- Kan worden beëindigd door [[aflossing]], [[kwijtschelding]] of [[afschrijving]]
- Kan aanleiding geven tot [[interventie]] bij niet-betaling
- Kan resulteren in [[restitutie]] bij te veel ontvangen aflossing
- Verwant aan [[belastingaanslag]] — maar de GGM-vordering is specifiek sociaal domein, terwijl een belastingaanslag publiekrechtelijk is op grond van de belastingverordening
