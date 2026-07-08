---
type: element
naam: Binnenlocatie
domein: [Sport en Bewegen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Binnenlocatie"
ggm_guid: EAID_6508657D_7C3F_4261_B647_5D3B077A20F9
ggm_uml_type: Class
ggm_beleidsdomein: "Sport"
ggm_taakveld: "5 Sport, Cultuur en Recreatie"
ggm_diagram: [Diagram Sportbeleid, Diagram Sportbeleid Locaties]
ggm_diagram_ids: [EAID_25BCAA7D_6255_4f3a_8408_DF91881FE29F, EAID_BA23F316_FE48_49a8_A26D_9B1D14713F76]
ggm_definitie: "Locatie binnen een gebouw"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Binnenlocatie"
ggm_gemma_guid: "cda4149f-f0a0-44d9-b893-25bcce04d20d"
ggm_gemma_definitie: "Locatie binnen een gebouw"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-cda4149f-f0a0-44d9-b893-25bcce04d20d"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Binnenlocatie** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Belijning** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Binnensportaccommodatie zoals een sporthal of gymzaal, met eigen capaciteitsberekening en bezettingsgraad."
bo_toelichting: ''
bo_subtypes:
  - naam: sporthal
    omschrijving: "Grote binnensportaccommodatie voor meerdere sporten en verenigingen"
    ggm_entiteit: "Binnenlocatie"
    ggm_guid: EAID_6508657D_7C3F_4261_B647_5D3B077A20F9
    ggm_attribuut: "sporthal"
  - naam: gymzaal
    omschrijving: "Kleinere binnensportruimte, vaak gekoppeld aan onderwijs"
    ggm_entiteit: "Binnenlocatie"
    ggm_guid: EAID_6508657D_7C3F_4261_B647_5D3B077A20F9
    ggm_attribuut: "gymzaal"
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Sportlocatie]]"
    richting: "naar-dit-BO"
    kardinaliteit: ""
    beschrijving: "Binnenlocatie is een specialisatie van Sportlocatie"
  - type: associatie
    bedrijfsobject: "[[Sportmateriaal]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: "Een binnenlocatie heeft sportmateriaal"
bedrijfsprocessen: [Zaalverdeling binnensport, Capaciteitsplanning sport, Zelfbeheer binnensportaccommodaties, Groot onderhoud en vervanging]
bedrijfsfuncties: [Sportaccommodatiebeheer, Sportbeleid]
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis (centraal in binnensportbeleid), herkenbaar (sporthal, gymzaal), eigen bestaan, meervoud (richtlijn 1 sporthal per 15.000 inwoners), levenscyclus (bouw, exploitatie, renovatie, zelfbeheer), relaties met [[Sportlocatie]], [[Sportmateriaal]], Verblijfsobject.

## Beschrijving

Een binnenlocatie is een binnensportaccommodatie — een sporthal of gymzaal — waar verenigingen, scholen en andere gebruikers binnensport beoefenen. De gemeente exploiteert binnensportaccommodaties, verdeelt zaalcapaciteit, en stuurt op bezettingsgraad. De richtlijn is 1 sporthal per 15.000 inwoners. Zelfbeheer door sportverenigingen is mogelijk in drie vormen: sleutelbeheer, beheer ontmoetingsruimte, of volledige overname van beheer en exploitatie.

## GGM-bron

> "Locatie binnen een gebouw" (GGM, entiteit Binnenlocatie, beleidsdomein Sport)

- **Entiteit:** Binnenlocatie
- **Beleidsdomein:** Sport
- **Attributen:** bouwjaar, vloeroppervlakte, klokurenOnderwijs, klokurenVerenigingen, onderhoudsstatus, onderhoudsniveau, geschatteKostenPerJaar, locatie, adres, sporthal, gymzaal, gemeentelijk
- **Matchsterkte:** exact

## BO-definitie

De GGM-definitie ("Locatie binnen een gebouw") is generiek. De GEMMA-definitie verduidelijkt de sportcontext: "Binnensportaccommodatie zoals een sporthal of gymzaal, met eigen capaciteitsberekening en bezettingsgraad."

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Sporthal | Grote binnensportaccommodatie voor meerdere sporten en verenigingen | Binnenlocatie |
| Gymzaal | Kleinere binnensportruimte, vaak gekoppeld aan onderwijs | Binnenlocatie |

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|
| [[Sportlocatie]] | generaliseert | | GGM |
| [[Sportmateriaal]] | heeft | 0..* | GGM |
| Verblijfsobject (BAG) | is gevestigd in | 0..1 | GGM |
| Wijk | bedient | 1 | GGM |
| Belijning | heeft | 0..* | GGM |


## Subtypes

- **sporthal** — Grote binnensportaccommodatie voor meerdere sporten en verenigingen
- **gymzaal** — Kleinere binnensportruimte, vaak gekoppeld aan onderwijs

## Bronnen

- [[Wiki/Bronsamenvattingen/Sport en Bewegen/beleidsnota-sport-en-bewegen-2025-2032]]
- [[Wiki/Bronsamenvattingen/Sport en Bewegen/uitvoeringsprogramma-sport-en-bewegen-2025]]
