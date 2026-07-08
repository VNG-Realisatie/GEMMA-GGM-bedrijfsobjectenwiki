---
type: element
naam: Aanvraag Leerlingenvervoer
domein: [onderwijs]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Aanvraag Leerlingenvervoer
ggm_guid: EAID_07F40D10_74AC_4f56_8B71_A236A63C2122
ggm_uml_type: Class
ggm_beleidsdomein: Leerplicht en Leerlingenvervoer
ggm_taakveld: "4 Onderwijs"
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: "Een aanvraag voor een leerling die recht heeft op vervoer van en naar onderwijs."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: AanvraagLeerlingenvervoer
ggm_gemma_guid: 41c1c340-9952-4bd9-8f45-fec2c0a1ddd7
ggm_gemma_definitie: "Een aanvraag voor een leerling die recht heeft op vervoer van en naar onderwijs."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-41c1c340-9952-4bd9-8f45-fec2c0a1ddd7
ggm_gemma_bron:
ggm_gemma_alternate_name:

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Aanvraag Leerlingenvervoer** als directe tegenhanger.
bo_definitie: "Verzoek van ouders aan de gemeente om een vervoersvoorziening voor hun kind."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Leerling]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Aanvraag betreft leerling"
  - type: associatie
    bedrijfsobject: "[[Beschikking Leerlingenvervoer]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Aanvraag leidt tot beschikking"
bedrijfsprocessen: [Leerlingenvervoer]
bedrijfsfuncties: [Leerplicht]
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Startpunt van het leerlingenvervoerproces |
| Herkenbaar voor domeinexperts | ✅ Ouders dienen aanvragen in; gemeente beoordeelt ze |
| Heeft eigen bestaan | ✅ Aanvraag bestaat als registratie met eigen kenmerken |
| Kan in meervoud bestaan | ✅ Tientallen tot honderden aanvragen per gemeente per jaar |
| Heeft eigen levenscyclus | ✅ Indienen → beoordelen → beschikken |
| Heeft relaties met andere concepten | ✅ Leerling, beschikking leerlingenvervoer |

**6/6 criteria van toepassing.**

## Beschrijving

Een aanvraag leerlingenvervoer is een verzoek van ouders aan de gemeente om een vervoersvoorziening voor hun kind. De gemeente is op grond van de Wet op het primair onderwijs verplicht een regeling te treffen voor het vervoer van leerlingen die door afstand, handicap of schoolkeuze niet zelfstandig naar school kunnen reizen. De aanvraag wordt beoordeeld en leidt tot een beschikking waarin de gemeente het vervoer toekent of afwijst.

## GGM-bron

> "Een aanvraag voor een leerling die recht heeft op vervoer van en naar onderwijs."
> — GGM-entiteit: Aanvraag Leerlingenvervoer, beleidsdomein: Leerplicht en Leerlingenvervoer

**Matchsterkte: exact.** De GGM-entiteit beschrijft hetzelfde concept.

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Leerling]] | associatie | ← | 1 | GGM |
| [[Beschikking Leerlingenvervoer]] | associatie | → | 0..1 | GGM |

## Bedrijfsprocessen

- **Leerlingenvervoer** — ontvangst en beoordeling van aanvragen voor leerlingenvervoer

## Bedrijfsfuncties

- Leerplicht

## Bronnen

- [[Wiki/Bronsamenvattingen/onderwijs/leerlingenvervoer]]
