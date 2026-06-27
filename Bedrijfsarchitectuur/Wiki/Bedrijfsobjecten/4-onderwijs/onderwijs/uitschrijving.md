---
type: bedrijfsobject
naam: Uitschrijving
domein: [onderwijs]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Uitschrijving
ggm_guid: EAID_133AF611_9FA0_4a09_BF12_74C5FA5F6F60
ggm_uml_type: Class
ggm_beleidsdomein: Onderwijs
ggm_taakveld: "4 Onderwijs"
ggm_diagram: ["Onderwijs: Leerlingen"]
ggm_diagram_ids: [EAID_33E38059_C973_43ff_97EC_B629923074FF]
ggm_definitie: "Beeindiging van een inschrijving van een leerling bij een school"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: Uitschrijving
ggm_gemma_guid: b83efc57-9184-4405-8c23-fbcabe7577b4
ggm_gemma_definitie: "Beeindiging van een inschrijving van een leerling bij een school"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-b83efc57-9184-4405-8c23-fbcabe7577b4
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

bo_definitie: "Beeindiging van de inschrijving van een leerling bij een school."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[School]]"
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: Uitschrijving betreft een school
  - type: associatie
    bedrijfsobject: "[[Leerling]]"
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: Uitschrijving betreft een leerling
bedrijfsprocessen: [Leerlingenadministratie, Leerplichthandhaving]
bedrijfsfuncties: [Onderwijsbeleid, Leerplicht]
---

## BO-criteria toetsing

6/6 criteria: heeft betekenis (ja), herkenbaar (ja), eigen bestaan (ja), meervoud (ja), levenscyclus (ja — uitschrijving wordt geregistreerd, verwerkt, eventueel gevolgd door leerplichtactie), relaties (ja — met school en leerling).

## Beschrijving

Een uitschrijving registreert de beeindiging van de inschrijving van een leerling bij een school. Uitschrijvingen zijn relevant voor leerplichthandhaving: wanneer een leerplichtige leerling wordt uitgeschreven zonder dat er een nieuwe inschrijving is, signaleert dit mogelijk voortijdig schoolverlaten. Het attribuut diplomaBehaald geeft aan of de leerling de school met een startkwalificatie heeft verlaten.

## GGM-bron

> "Beeindiging van een inschrijving van een leerling bij een school" — GGM, entiteit Uitschrijving, beleidsdomein Onderwijs

- **Entiteit:** Uitschrijving
- **Beleidsdomein:** Onderwijs
- **Attributen:** datum, diplomaBehaald
- **Matchsterkte:** exact

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Beschrijving |
|---|---|---|---|---|
| [[School]] | associatie | naar-dit-BO | 1..1 | Uitschrijving betreft een school |
| [[Leerling]] | associatie | naar-dit-BO | 1..1 | Uitschrijving betreft een leerling |

## Bedrijfsprocessen

- Leerlingenadministratie — registratie van beeindiging deelname
- Leerplichthandhaving — signalering voortijdig schoolverlaten bij uitschrijving zonder nieuwe inschrijving

## Bedrijfsfuncties

- Onderwijsbeleid
- Leerplicht

## Bronnen

- [[Wiki/Bronsamenvattingen/onderwijs/passend-onderwijs]]
- [[Wiki/Bronsamenvattingen/onderwijs/leerlingenvervoer]]
