---
type: element
naam: Verwerkingscontract
onderwerp: [Milieu]
archimate_type: contract
grondslag: procesobject
ggm_entiteit:
ggm_beleidsdomein:
ggm_guid:
ggm_uml_type:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:
bo_definitie: "Overeenkomst met een verwerker voor de inzameling of verwerking van afval- en grondstofstromen."
bo_toelichting:
bedrijfsprocessen: [Aanbesteding afvalverwerking, Contractbeheer]
bedrijfsfuncties: [Afvalbeheer, Inkoop]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Grondstofstroom]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: betreft verwerking van grondstofstromen
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Bepaalt hoe en tegen welke kosten afval wordt verwerkt |
| Herkenbaar voor domeinexperts | ✅ AVU-contract, AVR-nascheiding zijn bekende begrippen |
| Heeft eigen bestaan | ✅ Zelfstandige overeenkomst met eigen looptijd en voorwaarden |
| Kan in meervoud bestaan | ✅ Per stroom en per verwerker aparte contracten |
| Heeft eigen levenscyclus | ✅ Aanbesteding → gunning → looptijd → vernieuwing |
| Heeft relaties met andere concepten | ✅ Grondstofstromen, afvalstoffenheffing, verwerkers |

**6/6 criteria van toepassing.**

## Beschrijving

Een verwerkingscontract is een overeenkomst tussen de gemeente (vaak via de Gemeenschappelijke Regeling AVU) en afvalverwerkingsbedrijven voor de inzameling of verwerking van specifieke afval- en grondstofstromen. Belangrijke contracten: restafvalverwerking (via AVU), PBP-sortering (Combinatie Oost), GFT-compostering (via Cirkelwaarde). Contracten bepalen de kostenstructuur van de [[Afvalstoffenheffing]]. Steeds vaker is circulaire verwerking een selectiecriterium bij aanbesteding.

> "De gemeente neemt deel aan de Gemeenschappelijke Regeling AVU voor de verwerking van het meeste huishoudelijk afval." (bron: [[Wiki/Bronsamenvattingen/Milieu/grondstoffennota-utrecht-2020|Grondstoffennota 2020]])

## Procesbron

Verwerkingscontracten ontstaan uit de gemeentelijke zorgplicht onder de Wet Milieubeheer om afvalverwerking te waarborgen. De meeste stromen worden beheerd via de GR AVU (Afvalverwijdering Utrecht). De gemeente sluit contracten af via aanbesteding of via de gemeenschappelijke regeling.

Het GGM modelleert Prijsafspraak als dichtstbijzijnde concept, maar een verwerkingscontract is een overeenkomst, geen prijsafspraak. Contracten zijn niet gemodelleerd in het GGM Afval-domein — dit is een procesobject.

## Relaties

- **[[Grondstofstroom]]** — elk verwerkingscontract betreft de verwerking van een of meer grondstofstromen

## Bedrijfsprocessen

- **Aanbesteding afvalverwerking** — selectie en gunning van verwerkers
- **Contractbeheer** — monitoren van prestaties, kosten en looptijd

## Bedrijfsfuncties

- Afvalbeheer
- Inkoop

## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/grondstoffennota-utrecht-2020]]
