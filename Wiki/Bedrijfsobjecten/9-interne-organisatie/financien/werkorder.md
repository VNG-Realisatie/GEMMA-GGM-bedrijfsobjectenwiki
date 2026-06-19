---
type: bedrijfsobject
naam: Werkorder
domein: [Financien]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Werkorder
ggm_beleidsdomein: Financien
definitie: Opdracht voor de uitvoering van een activiteit of een stap in een proces
gerelateerde_begrippen: []
bedrijfsprocessen: [Operationeel beheer, Onderhoud]
bedrijfsfuncties: [Beheer openbare ruimte, Facilitair beheer]
status: concept
---

# Werkorder

Opdracht voor de uitvoering van een activiteit of een stap in een proces. In de gemeentelijke context: opdrachten voor onderhoud, inspectie of andere uitvoerende werkzaamheden.

## GGM-bron

> Opdracht voor de uitvoering van een activiteit of een stap in een proces.

- **Entiteit:** Werkorder
- **Beleidsdomein:** Financien (taakveld 9 — Interne Organisatie)
- **Attributen:** naam, omschrijving, code, werkordertype, documentnummer

## Bedrijfsprocessen

- **Operationeel beheer** — aansturen van uitvoerende werkzaamheden
- **Onderhoud** — planmatig en correctief onderhoud

## Bedrijfsfuncties

- **Beheer openbare ruimte** — werkorders voor onderhoud
- **Facilitair beheer** — werkorders voor interne diensten

## Relaties

- Gekoppeld aan een [[kostenplaats]]
- Kan leiden tot een [[inkooporder]] bij externe uitvoering
