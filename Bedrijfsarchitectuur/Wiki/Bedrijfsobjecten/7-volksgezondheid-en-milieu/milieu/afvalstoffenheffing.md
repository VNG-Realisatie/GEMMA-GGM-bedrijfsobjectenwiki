---
type: element
naam: Afvalstoffenheffing
onderwerp: [Milieu]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Prijsafspraak"
ggm_guid: EAID_21BBA828_AAE0_4785_9E44_45C1B866C882
ggm_uml_type: Class
ggm_beleidsdomein: "Afval"
ggm_taakveld: "7 Volksgezondheid en Milieu"
ggm_diagram: [Diagram Afval Ophalen]
ggm_diagram_ids: [EAID_D98AA96C_2EB0_4b46_9E9C_09D55E02FE38]
ggm_definitie: "Overeenkomst tussen concurrenten met betrekking tot de prijs van goederen of diensten. "
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam: "Prijsafspraak"
ggm_gemma_guid: "343e027e-16c9-43d7-8b90-891aaf9c4b70"
ggm_gemma_definitie: "Overeenkomst tussen concurrenten met betrekking tot de prijs van goederen of diensten."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-343e027e-16c9-43d7-8b90-891aaf9c4b70"
ggm_gemma_bron:
ggm_gemma_alternate_name:
analyse_ggm_dekking: |
  Dit BO is de hernoeming van GGM-entiteit **Prijsafspraak**.
bo_definitie: "Gemeentelijke bestemmingsbelasting ter dekking van de kosten voor huishoudelijk afvalbeheer."
bo_toelichting:
bo_via_kandidaten:
  - ggm_entiteit: "Prijsregel"
    ggm_guid: "EAID_E79C6C20_3D05_49fb_96ED_105B5CD0ABA5"
    reden: "Een prijsregel binnen een tariefstructuur hoort bij de afvalstoffenheffing, niet bij de fysieke grondstofstroom."
bedrijfsprocessen: [Tariefvaststelling, Belastinginning, Kostenverdeling afvalbeheer]
bedrijfsfuncties: [Afvalbeheer, Belastingheffing]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Grondstofstroom]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: kosten per grondstofstroom
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Centraal financieel instrument voor afvalbeheer |
| Herkenbaar voor domeinexperts | ✅ Bekend bij elke inwoner en elke gemeente |
| Heeft eigen bestaan | ✅ Zelfstandige gemeentelijke belasting met eigen grondslag |
| Kan in meervoud bestaan | ✅ Per gemeente, per jaar een eigen tarief |
| Heeft eigen levenscyclus | ✅ Vaststelling → inning → verantwoording |
| Heeft relaties met andere concepten | ✅ Afvalverwerkingskosten, grondstofstromen, verwerkingscontracten |

**6/6 criteria van toepassing.**

## Beschrijving

De afvalstoffenheffing is de gemeentelijke belasting die de kosten van huishoudelijk afvalbeheer dekt. Utrecht hanteert 100% kostendekkende afvalstoffenheffing (geen subsidie uit de algemene middelen). De heffing is historisch laag vergeleken met andere G4-gemeenten. De hoogte wordt beinvloed door de verbrandingsbelasting (EUR 32,12/ton in 2019), verwerkingscontracten en scheidingsresultaten — betere scheiding verlaagt de kosten doordat minder restafval tegen hogere tarieven verbrand hoeft te worden.

> "De afvalstoffenheffing in Utrecht is kostendekkend. Betere scheiding leidt tot lagere verwerkingskosten en daarmee tot een lagere afvalstoffenheffing." (bron: [[Wiki/Bronsamenvattingen/Milieu/grondstoffennota-utrecht-2020|Grondstoffennota 2020]])

Cross-domein met Belastingen: de afvalstoffenheffing is formeel een gemeentelijke bestemmingsbelasting maar wordt operationeel aangestuurd vanuit het afvaldomein.

## GGM-bron

> **Prijsafspraak**: Overeenkomst tussen concurrenten met betrekking tot de prijs van goederen of diensten.
> — *GGM, Afval (taakveld 7 Volksgezondheid en Milieu)*

**Entiteit:** Prijsafspraak
**Matchsterkte:** partieel — het GGM modelleert Prijsafspraak/Prijsregel als generieke prijsstructuren. De afvalstoffenheffing is een bestemmingsbelasting en daarmee breder dan alleen een prijsafspraak. Het GGM-concept dekt het tariefaspect maar niet de belastinggrondslag, de inning en de verantwoording.

## BO-definitie

Het bedrijfsobject **Afvalstoffenheffing** wijkt af van de GGM-entiteit **Prijsafspraak**. Het GGM definieert Prijsafspraak als een generieke overeenkomst over prijzen. De afvalstoffenheffing is een bestemmingsbelasting met wettelijke grondslag (Gemeentewet art. 229a), eigen tariefvaststelling door de raad, en een verplicht kostendekkingspercentage.

## Relaties

- **[[Grondstofstroom]]** — de kosten per grondstofstroom bepalen mede de hoogte van de heffing

## Bedrijfsprocessen

- **Tariefvaststelling** — jaarlijkse berekening en vaststelling van het tarief door de raad
- **Belastinginning** — inning via de gemeentelijke belastingen
- **Kostenverdeling afvalbeheer** — toerekening van inzamel- en verwerkingskosten aan de heffing

## Bedrijfsfuncties

- Afvalbeheer
- Belastingheffing

## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/grondstoffennota-utrecht-2020]]
