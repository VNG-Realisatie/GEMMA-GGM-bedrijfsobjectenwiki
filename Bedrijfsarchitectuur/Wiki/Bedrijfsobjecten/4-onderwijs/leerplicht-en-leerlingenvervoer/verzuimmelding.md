---
type: element
naam: Verzuimmelding
domein: [onderwijs]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Verzuimmelding
ggm_guid: EAID_252C70B1_4E02_4033_B2B5_86F65496D7AB
ggm_uml_type: Class
ggm_beleidsdomein: Leerplicht en Leerlingenvervoer
ggm_taakveld: "4 Onderwijs"
ggm_diagram: [Diagram Beslissingen Leerplicht]
ggm_diagram_ids: [EAID_26A453D9_47AF_487e_854B_3B4BC6D6A308]
ggm_definitie: "Een melding dat een leerling niet op school verschijnt. De school moet actie ondernemen naar de leerling (en zijn ouders). Een school moet het verzuim melden bij de gemeente."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam: Verzuimmelding
ggm_gemma_guid: e623ef14-c4de-498b-9504-5bb6fa4ce0de
ggm_gemma_definitie: "Een melding dat een leerling niet op school verschijnt. De school moet actie ondernemen naar de leerling (en zijn ouders). Een school moet het verzuim melden bij de gemeente."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-e623ef14-c4de-498b-9504-5bb6fa4ce0de
ggm_gemma_bron:
ggm_gemma_alternate_name:

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Verzuimmelding** als directe tegenhanger.
bo_definitie: "Melding van een school aan de gemeente dat een leerling niet op school verschijnt."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Leerling]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Verzuimmelding betreft leerling"
  - type: associatie
    bedrijfsobject: "[[School]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Verzuimmelding komt van school"
bedrijfsprocessen: [Leerplichthandhaving]
bedrijfsfuncties: [Leerplicht]
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Wettelijk begrip in de leerplichtwet; startpunt van het handhavingsproces |
| Herkenbaar voor domeinexperts | ✅ Leerplichtambtenaren werken dagelijks met verzuimmeldingen |
| Heeft eigen bestaan | ✅ Melding bestaat als registratie met eigen kenmerken (datum, school, leerling) |
| Kan in meervoud bestaan | ✅ Honderden tot duizenden meldingen per gemeente per jaar |
| Heeft eigen levenscyclus | ✅ Ontvangst → beoordeling → onderzoek → afhandeling |
| Heeft relaties met andere concepten | ✅ Leerling, school, eventueel procesverbaal of vrijstelling |

**6/6 criteria van toepassing.**

## Beschrijving

Een verzuimmelding is een melding van een school aan de gemeente dat een leerling niet op school verschijnt. Scholen zijn wettelijk verplicht om ongeoorloofd verzuim te melden bij de leerplichtambtenaar van de gemeente. De leerplichtambtenaar onderzoekt de melding en kan verschillende vervolgacties ondernemen, van een gesprek met ouders tot het opmaken van een procesverbaal.

## GGM-bron

> "Een melding dat een leerling niet op school verschijnt. De school moet actie ondernemen naar de leerling (en zijn ouders). Een school moet het verzuim melden bij de gemeente."
> — GGM-entiteit: Verzuimmelding, beleidsdomein: Leerplicht en Leerlingenvervoer

**Matchsterkte: exact.** De GGM-entiteit beschrijft hetzelfde concept.

**GGM-attributen:** datumStart, datumEinde, voorstelSchool.

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Leerling]] | associatie | ← | 1 | GGM |
| [[School]] | associatie | ← | 1 | GGM |

## Bedrijfsprocessen

- **Leerplichthandhaving** — ontvangst en beoordeling van verzuimmeldingen, onderzoek door leerplichtambtenaar

## Bedrijfsfuncties

- Leerplicht

## Bronnen

- [[Wiki/Bronsamenvattingen/onderwijs/beleidsnota-onderwijshuisvesting-utrecht]]
- [[Wiki/Bronsamenvattingen/onderwijs/leerlingenvervoer]]
