---
type: bedrijfsobject
naam: Factuur
domein: [Financien]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Factuur
ggm_beleidsdomein: Financien
definitie: Schriftelijke rekening of nota voor de geleverde zaken of verrichte diensten
gerelateerde_begrippen: []
bedrijfsprocessen: [Facturering, Crediteuren- en debiteurenadministratie]
bedrijfsfuncties: [Financieel beheer]
status: concept
---

# Factuur

Schriftelijke rekening of nota voor de geleverde zaken of verrichte diensten.

## GGM-bron

> Schriftelijke rekening of nota voor de geleverde zaken of verrichte diensten.

- **Entiteit:** Factuur
- **Beleidsdomein:** Financien (taakveld 9 — Interne Organisatie)
- **Attributen:** datumFactuur, omschrijving, code, betaaltermijn, betaalbaarPer, factuurbedragExclusiefBTW, factuurbedragBTW

## Bedrijfsprocessen

- **Facturering** — opstellen en verzenden van facturen
- **Crediteuren- en debiteurenadministratie** — verwerking van inkomende en uitgaande facturen

## Bedrijfsfuncties

- **Financieel beheer** — financiële administratie

## Relaties

- Gericht aan een [[debiteur]]
- Gekoppeld aan een [[inkooporder]] (inkomende facturen) of aan een [[product]] (uitgaande facturen)
- Verschilt van een [[belastingaanslag]]: een factuur is een privaatrechtelijke vordering, een aanslag een publiekrechtelijke
