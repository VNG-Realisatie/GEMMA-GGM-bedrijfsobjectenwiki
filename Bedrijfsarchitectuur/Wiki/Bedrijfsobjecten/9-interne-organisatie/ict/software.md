---
type: element
naam: Software
onderwerp: [Informatiesystemen]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Software
ggm_guid: EAID_0B3C37DD_42A1_4b6b_B534_CD276112FD3B
ggm_uml_type: Class
ggm_beleidsdomein: ICT
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Basismodel CMDB-Items Diversen]
ggm_diagram_ids: [EAID_A255BB0C_A1DB_43a5_88B1_C638F6E64B0B]
ggm_definitie: "Een geheel van computerprogramma's met bijbehorende data, die bewerkingen en taken uitvoeren"
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

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Software** als directe tegenhanger.
bo_definitie: "Computerprogrammatuur met bijbehorende data die bewerkingen en taken uitvoert."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/licentie|Licentie]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Software wordt gebruikt op basis van licenties"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server|Server]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Software draait op servers"
bedrijfsprocessen: [Softwarebeheer, Licentiebeheer, Wijzigingsbeheer]
bedrijfsfuncties: [ICT-beheer]
---

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Betekenis | Programmatuur die niet direct eindgebruikers ondersteunt maar infrastructureel nodig is |
| Herkenbaarheid | "het besturingssysteem", "de middleware", "de databasesoftware" |
| Eigen bestaan | Subtype van CMDB-item; onderscheiden van Applicatie (die eindgebruikers ondersteunt) |
| Meervoud | Tientallen per gemeente |
| Levenscyclus | Installatie → configuratie → updates/upgrades → end-of-life |
| Relaties | Licentie, Server |

Resultaat: 5/6 — BO. Geen eigen attributen in GGM maar voldoende criteria.

## Beschrijving

Software is computerprogrammatuur die niet direct op eindgebruikers is gericht, maar infrastructureel noodzakelijk is: besturingssystemen, middleware, databasemanagementsystemen, beveiligingssoftware. In het GGM is Software een subtype van CMDB-item, onderscheiden van [[Applicatie]] (die via Linkbaar CMDB-item loopt en gericht is op eindgebruikers).

De GIBIT 2025 onderscheidt drie typen programmatuur: Standaardprogrammatuur (voor algemeen gebruik), Maatwerkprogrammatuur (specifiek voor de opdrachtgever ontwikkeld) en Derdenprogrammatuur (intellectueel eigendom niet bij leverancier).

## Subtypes

Herkende specialisaties van Software. Gevonden in GIBIT 2025. Geen apart BO.

- **Standaardprogrammatuur** — voor algemeen gebruik ontwikkelde programmatuur
- **Maatwerkprogrammatuur** — specifiek ten behoeve van opdrachtgever ontwikkeld of aangepast
- **Derdenprogrammatuur** — programmatuur waarvan het intellectueel eigendom niet bij de leverancier rust

## GGM-bron

> "Een geheel van computerprogramma's met bijbehorende data, die bewerkingen en taken uitvoeren"
> — GGM, beleidsdomein ICT, taakveld 9 Interne Organisatie

Entiteit: Software | Matchsterkte: **exact** | Attributen: *(geen in GGM)*

## Relaties

| Relatie | Richting | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/licentie\|Licentie]] | van-dit-BO | Software wordt gebruikt op basis van licenties |
| [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/server\|Server]] | naar-dit-BO | Software draait op servers |

## Bedrijfsprocessen

- **Softwarebeheer** — installatie, updates, upgrades, end-of-life management
- **Licentiebeheer** — licentiecompliancy voor softwareproducten
- **Wijzigingsbeheer** — impactanalyse bij softwarewijzigingen

## Bedrijfsfuncties

- **ICT-beheer** — technisch softwarebeheer

## Bronnen

- [[Wiki/Bronsamenvattingen/Informatiesystemen/gibit-2025]]
- [[Wiki/Bronsamenvattingen/Informatiesystemen/cmdb-en-informatiebeheer]]
