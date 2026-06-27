---
type: bedrijfsobject
naam: Schuldregeling
onderwerp: [schulden en armoede]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Schuldregeling
ggm_guid: EAID_652A68C3_618E_4050_AD4C_E43469A7558C
ggm_uml_type: Class
ggm_beleidsdomein: Schuldhulpverlening
ggm_taakveld: "Schulden"
ggm_diagram: [Schuldhulpproces]
ggm_definitie: "De schuldregeling heeft als doel een overeenkomst te sluiten tussen iemand met problematische schulden en zijn schuldeisers. Op basis van eventueel ingezet vermogen en de berekende afloscapaciteit lost de schuldenaar in maximaal 18 maanden zo veel mogelijk van de schuld af. Daarna schelden de schuldeisers de rest van hun vordering kwijt."
ggm_herkomst: GGM

bo_definitie: "Overeenkomst tussen een inwoner met problematische schulden en de schuldeisers, gericht op aflossing binnen 18 maanden met kwijtschelding van het restant."
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[schuldhulptraject]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Onderdeel van een schuldhulptraject"
bedrijfsprocessen: [schuldhulpverlening]
bedrijfsfuncties: [financiële hulpverlening]
---

## BO-criteria toetsing

6/6 criteria. Overeenkomst met eigen datum, status (toegekend/afgewezen/ingetrokken), mogelijkheid tot dwangakkoord. Eigen levenscyclus: voorstel → acceptatie/weigering → uitvoering → afronding.

## Beschrijving

De schuldregeling is de overeenkomst tussen schuldenaar en schuldeisers. Er zijn twee vormen:

- **Minnelijke schuldregeling** — vrijwillige overeenkomst, begeleid door schuldhulpverlener, zonder tussenkomst van de rechter.
- **Wettelijke schuldregeling (WSNP)** — formeel proces onder toezicht van de rechter, via het [[wsnp-traject|WSNP-traject]].

Binnen de minnelijke regeling zijn er twee uitvoeringsvormen:
- **Saneringskrediet** — GKB verstrekt krediet waarmee alle schuldeisers in één keer worden afbetaald. Den Haag streeft naar ≥90%.
- **Schuldbemiddeling** — schuldenaar lost periodiek af aan schuldeisers gedurende de looptijd.

Bij weigering door schuldeisers kan een dwangakkoord (art. 287a Fw) worden aangevraagd.

## GGM-bron

> "De schuldregeling heeft als doel een overeenkomst te sluiten tussen iemand met problematische schulden en zijn schuldeisers."

- **Entiteit:** Schuldregeling
- **Beleidsdomein:** Schuldhulpverlening
- **Attributen:** datum, toegekend, afgewezen, ingetrokken, dwangakkoord, datumVerzoekDwangakkoord
- **Matchsterkte:** exact

## Relaties

| Type | Bedrijfsobject | Kardinaliteit | Beschrijving |
|---|---|---|---|
| associatie | [[schuldhulptraject\|Schuldhulptraject]] | 0..1 | Onderdeel van traject |

## Bronnen
- [[Wiki/Bronsamenvattingen/Schulden en Armoede/beleidsplan-schuldhulpverlening-den-haag-2024-2028]]
