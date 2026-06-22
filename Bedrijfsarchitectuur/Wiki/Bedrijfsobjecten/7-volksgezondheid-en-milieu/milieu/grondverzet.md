---
type: bedrijfsobject
naam: Grondverzet
domein: [Milieu]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit: ""
ggm_beleidsdomein: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_taakveld: ""
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ""
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
gemma_definitie: "Registratie van een grondverplaatsing met herkomstlocatie, bestemmingslocatie, kwaliteit en volume."
bedrijfsprocessen: [grondverzet beoordelen, milieuhandhaving, bodembeheer]
bedrijfsfuncties: [milieubeheer, vergunningverlening]
relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemkwaliteitskaart|Bodemkwaliteitskaart]]"
    richting: "naar-dit-BO"
    kardinaliteit: 1
    beschrijving: Grondverzet wordt getoetst aan de bodemkwaliteitskaart
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Meldingsplichtige activiteit bij grondverplaatsing |
| Herkenbaar voor domeinexperts | ✅ Centraal concept in bodembeheer |
| Heeft eigen bestaan | ✅ Individuele melding met eigen registratie |
| Kan in meervoud bestaan | ✅ Honderden meldingen per jaar per gemeente |
| Heeft eigen levenscyclus | ✅ Melding → beoordeling → uitvoering → controle |
| Heeft relaties met andere concepten | ✅ Bodemkwaliteitskaart, herkomst- en bestemmingslocatie |

**6/6 criteria van toepassing.**

## Beschrijving

Een grondverzet is een registratie van het verplaatsen van grond of baggerspecie. Elke verplaatsing heeft een herkomstlocatie, bestemmingslocatie, kwaliteit van de grond, volume, en wordt beoordeeld aan de hand van de [[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemkwaliteitskaart|bodemkwaliteitskaart]]. De initiatiefnemer is verplicht het grondverzet te melden bij de gemeente.

De gemeente toetst of de kwaliteit van de grond past bij de bodemfunctie op de bestemmingslocatie. Schone grond mag overal worden toegepast; licht verontreinigde grond mag onder voorwaarden worden hergebruikt voor wonen of industrie.

> "Het vastgestelde kwaliteitsniveau van de grond en de functie (landbouw, woningbouw of industrie) waarvoor de grond bedoeld is, bepalen of en waar de grond hergebruikt mag worden." (bron: [[Wiki/Bronsamenvattingen/Milieu/nota-bodembeheer|Nota Bodembeheer 2017-2027 (Grondig Werken 4)]])

## Procesbron

Grondverzet ontstaat bij bouw- en infraprojecten. Melding is verplicht op grond van het Besluit bodemkwaliteit. De gemeente beoordeelt de melding en houdt toezicht op de uitvoering.

## Relaties

- **[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemkwaliteitskaart|Bodemkwaliteitskaart]]** — toetsing van hergebruik op basis van kwaliteitszone en bodemfunctie


## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/nota-bodembeheer]]

## Terugmelding GGM

Grondverzet is een registratie-object dat gemeenten bijhouden als bevoegd gezag bodembeheer. Het GGM heeft geen equivalent. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
