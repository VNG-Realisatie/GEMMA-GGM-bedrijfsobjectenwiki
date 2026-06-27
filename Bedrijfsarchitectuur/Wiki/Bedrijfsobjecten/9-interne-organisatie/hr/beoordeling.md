---
type: bedrijfsobject
naam: Beoordeling
domein: [Arbeidszaken]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Beoordeling
ggm_guid: EAID_2A0CC803_9017_4fad_99B5_9347623090F5
ggm_uml_type: Class
ggm_beleidsdomein: HR
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Domain Objects, Documenten]
ggm_diagram_ids: [EAID_891372E6_27FB_442d_9CC4_08C2659E8C53, EAID_E8C1CCDA_FF3C_498a_8FC9_FD6E461092FA]
ggm_definitie: "Beoordeling is het oordeel van de professional over het functioneren van een leerling"
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

bo_definitie: "Beoordeling is het oordeel van de professional over het functioneren van een leerling"
bo_toelichting: ''
bo_subtypes:
  - naam: Planningsgesprek
    omschrijving: "Gesprek aan het begin van de cyclus waarin doelstellingen en verwachtingen worden vastgelegd"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Functioneringsgesprek
    omschrijving: "Tussentijds gesprek over voortgang, knelpunten en bijstelling van afspraken"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
  - naam: Beoordelingsgesprek
    omschrijving: "Eindgesprek met formeel oordeel over functioneren, basis voor periodieke verhoging of promotie"
    ggm_entiteit:
    ggm_guid:
    ggm_attribuut:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Werknemer]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Beoordeling van werknemer"
  - type: associatie
    bedrijfsobject: "[[Dienstverband]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Beoordeling kan leiden tot schaalwijziging op dienstverband"
bedrijfsprocessen: [Gesprekscyclus, Personeelsontwikkeling]
bedrijfsfuncties: [Personeelsbeheer]
---

## BO-criteria toetsing

| Criterium | Score |
|---|---|
| Heeft betekenis binnen het domein | ✅ Kern van de gesprekscyclus |
| Herkenbaar voor domeinexperts | ✅ Elke leidinggevende voert beoordelingsgesprekken |
| Heeft eigen bestaan binnen het domein | ✅ Elk gesprek/oordeel is een zelfstandig record |
| Kan in meervoud bestaan | ✅ Meerdere per werknemer per jaar |
| Heeft eigen levenscyclus | ✅ Gepland → gevoerd → vastgelegd |
| Heeft relaties met andere concepten | ✅ Werknemer, Dienstverband (schaalconsequentie) |

Score: **6/6**

## Beschrijving

De beoordeling omvat de volledige gesprekscyclus waarmee de gemeente het functioneren van werknemers begeleidt en evalueert. De cyclus kent drie fases: het planningsgesprek (doelen en verwachtingen), het functioneringsgesprek (tussentijdse evaluatie) en het beoordelingsgesprek (formeel eindoordeel). De uitkomst kan leiden tot een periodieke verhoging, promotie of een verbetertraject.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Planningsgesprek | Doelstellingen en verwachtingen vastleggen | — |
| Functioneringsgesprek | Tussentijdse evaluatie en bijstelling | — |
| Beoordelingsgesprek | Formeel eindoordeel, basis voor periodiek/promotie | — |

## GGM-bron

> "Beoordeling is het oordeel van de professional over het functioneren van een leerling"

- **Entiteit:** Beoordeling
- **Beleidsdomein:** HR (taakveld 9 Interne Organisatie)
- **Attributen:** datum, oordeel, omschrijving
- **Matchsterkte:** exact (maar definitie incorrect — "leerling" moet "werknemer" zijn)

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| Beoordeling van [[Werknemer]] | naar dit BO | 1 | GGM |

## Terugmelding GGM

**Beoordeling** — Definitie verwijst naar "leerling" maar entiteit staat in HR-domein met relatie naar Werknemer. Voorgestelde correctie: "Het oordeel over het functioneren van een werknemer." Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].


## Subtypes

- **Planningsgesprek** — Gesprek aan het begin van de cyclus waarin doelstellingen en verwachtingen worden vastgelegd
- **Functioneringsgesprek** — Tussentijds gesprek over voortgang, knelpunten en bijstelling van afspraken
- **Beoordelingsgesprek** — Eindgesprek met formeel oordeel over functioneren, basis voor periodieke verhoging of promotie

## Bronnen

- [[Wiki/Bronsamenvattingen/Arbeidszaken/cva-beleidsplan-2023-2026]]
