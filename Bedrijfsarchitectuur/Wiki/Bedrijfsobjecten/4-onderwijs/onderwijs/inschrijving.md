---
type: bedrijfsobject
naam: Inschrijving
domein: [onderwijs]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Inschrijving
ggm_guid: EAID_CFFD5F20_5FA9_4d93_AD34_6867D64A58B9
ggm_uml_type: Class
ggm_beleidsdomein: Onderwijs
ggm_taakveld: "4 Onderwijs"
ggm_diagram: ["Onderwijs: Leerlingen"]
ggm_diagram_ids: [EAID_33E38059_C973_43ff_97EC_B629923074FF]
ggm_definitie: "Deelname van iemand aan een opleiding bij een onderwijsinstelling."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: Inschrijving
ggm_gemma_guid: 5e8930d4-8f06-4075-bf2b-31f45ee86dbc
ggm_gemma_definitie: "Deelname van iemand aan een opleiding bij een onderwijsinstelling."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-5e8930d4-8f06-4075-bf2b-31f45ee86dbc
ggm_gemma_bron: ""
ggm_gemma_alternate_name: "Inschrijving (Onderwijs)"

bo_definitie: "Registratie van de deelname van een leerling aan onderwijs bij een school."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[School]]"
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: Inschrijving is bij een school
  - type: associatie
    bedrijfsobject: "[[Leerling]]"
    richting: naar-dit-BO
    kardinaliteit: "1..1"
    beschrijving: Inschrijving betreft een leerling
bedrijfsprocessen: [Leerlingenadministratie]
bedrijfsfuncties: [Onderwijsbeleid]
---

## BO-criteria toetsing

6/6 criteria: heeft betekenis (ja), herkenbaar (ja), eigen bestaan (ja), meervoud (ja), levenscyclus (ja — inschrijving wordt aangemaakt bij aanmelding, is actief tijdens schoolbezoek, wordt beeindigd bij uitschrijving), relaties (ja — met school en leerling).

## Beschrijving

Een inschrijving registreert de deelname van een leerling aan onderwijs bij een school. De inschrijving legt het moment vast waarop een leerling start bij een school en vormt de basis voor leerplichtregistratie. Via inschrijvingen houdt de gemeente zicht op welke leerplichtige kinderen waar onderwijs volgen.

## GGM-bron

> "Deelname van iemand aan een opleiding bij een onderwijsinstelling." — GGM, entiteit Inschrijving, beleidsdomein Onderwijs

- **Entiteit:** Inschrijving
- **Beleidsdomein:** Onderwijs
- **Attributen:** datum
- **Matchsterkte:** exact

## Relaties

| Gerelateerd BO | Type | Richting | Kardinaliteit | Beschrijving |
|---|---|---|---|---|
| [[School]] | associatie | naar-dit-BO | 1..1 | Inschrijving is bij een school |
| [[Leerling]] | associatie | naar-dit-BO | 1..1 | Inschrijving betreft een leerling |

## Bedrijfsprocessen

- Leerlingenadministratie — registratie van deelname aan onderwijs

## Bedrijfsfuncties

- Onderwijsbeleid

## Bronnen

- [[Wiki/Bronsamenvattingen/onderwijs/passend-onderwijs]]
- [[Wiki/Bronsamenvattingen/onderwijs/beleidsnota-onderwijshuisvesting-utrecht]]
