---
type: element
naam: Sportlocatie
domein: [Sport en Bewegen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Sportlocatie"
ggm_guid: EAID_BE5E10D0_FD83_4b0a_B5D2_4A7EE6B9C53B
ggm_uml_type: Class
ggm_beleidsdomein: "Sport"
ggm_taakveld: "5 Sport, Cultuur en Recreatie"
ggm_diagram: [Diagram Sportbeleid, Diagram Sportbeleid Locaties]
ggm_diagram_ids: [EAID_25BCAA7D_6255_4f3a_8408_DF91881FE29F, EAID_BA23F316_FE48_49a8_A26D_9B1D14713F76]
ggm_definitie: "Locatie waar de betreffende sport plaatsvindt"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Sportlocatie"
ggm_gemma_guid: "a7a350a2-a9aa-4437-b67b-016fec0d048d"
ggm_gemma_definitie: "Locatie waar de betreffende sport plaatsvindt"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-a7a350a2-a9aa-4437-b67b-016fec0d048d"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Sportlocatie** als directe tegenhanger.
bo_definitie: "Locatie waar sportbeoefening plaatsvindt, als overkoepelend begrip voor binnen- en buitensportaccommodaties."
bo_toelichting: ''
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Sportpark]]"
    richting: "van-dit-BO"
    kardinaliteit: ""
    beschrijving: "Sportpark is een specialisatie van Sportlocatie"
  - type: generalisatie
    bedrijfsobject: "[[Binnenlocatie]]"
    richting: "van-dit-BO"
    kardinaliteit: ""
    beschrijving: "Binnenlocatie is een specialisatie van Sportlocatie"
  - type: associatie
    bedrijfsobject: "[[Sportvereniging]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Sportverenigingen gebruiken sportlocaties"
bedrijfsprocessen: [Capaciteitsplanning sport, Ingebruikgeving sportaccommodaties]
bedrijfsfuncties: [Sportaccommodatiebeheer]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis (overkoepelend voor alle plekken waar sport plaatsvindt), herkenbaar, eigen bestaan (als categorie), meervoud, levenscyclus (via subtypes), relaties met [[Sportvereniging]], School. Abstract niveau dat de 6 criteria zelf haalt; specialisaties ([[Sportpark]], [[Binnenlocatie]]) zijn herkenbaar en hebben eigen processen, dus zijn ook BO.

## Beschrijving

Een sportlocatie is een locatie waar sport plaatsvindt. Het is het overkoepelende begrip voor [[Binnenlocatie]] (sporthallen, gymzalen) en [[Sportpark]] (buitensportaccommodaties). In het GGM is Sportlocatie gemodelleerd als generalisatie met deze twee specialisaties. Scholen gebruiken sportlocaties (GGM-relatie School ↔ Sportlocatie).

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| [[Sportpark]] | Buitensportaccommodatie met terreinen, gebouwen en voorzieningen | [Sportpark](Wiki/GGM/5-sport-cultuur-en-recreatie/sport.md) |
| [[Binnenlocatie]] | Binnensportaccommodatie (sporthal, gymzaal) | [Binnenlocatie](Wiki/GGM/5-sport-cultuur-en-recreatie/sport.md) |

## GGM-bron

> "Locatie waar de betreffende sport plaatsvindt" (GGM, entiteit Sportlocatie, beleidsdomein Sport)

- **Entiteit:** Sportlocatie
- **Beleidsdomein:** Sport
- **Attributen:** naam
- **Matchsterkte:** exact

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Sportpark]] | specialisatie | | GGM |
| [[Binnenlocatie]] | specialisatie | | GGM |
| [[Sportvereniging]] | wordt gebruikt door | 0..* | GGM |
| School | wordt gebruikt door | 0..* | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Sport en Bewegen/beleidsnota-sport-en-bewegen-2025-2032]]
