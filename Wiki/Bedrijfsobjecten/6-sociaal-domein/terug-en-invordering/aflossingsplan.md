---
type: bedrijfsobject
naam: Aflossingsplan
domein: [Terug-en-invordering]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Aflossingsplan
ggm_beleidsdomein: Terug-en-invordering
definitie: Alle afspraken tussen de gemeente en de debiteur over op welke vordering per wanneer welk bedrag wordt afgelost
gerelateerde_begrippen: [kwijtschelding]
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

- Hoort bij een [[debiteur]]
- Betreft een of meer [[vordering]]en
- Bevat [[aflossing]]en als concrete betalingen
- Bij 36 maanden aflossingsdicipline: mogelijkheid tot [[kwijtschelding]]
- Bij achterstalligheid: [[interventie]]
