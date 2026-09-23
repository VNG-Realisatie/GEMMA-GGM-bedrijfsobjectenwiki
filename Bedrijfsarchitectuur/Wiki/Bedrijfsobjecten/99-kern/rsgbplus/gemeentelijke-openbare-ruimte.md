---
type: element
naam: Gemeentelijke Openbare Ruimte
onderwerp: [Basisregistraties, RSGBPlus]
archimate_type: business-object
grondslag: ggm-afgeleid

# GGM-velden
ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

# GEMMA-waarden
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

analyse_ggm_dekking: ""
bo_definitie: "Door het bevoegde gemeentelijke orgaan aangewezen openbaar gedeelte van het gemeentelijk grondgebied, vastgelegd als geo-object met een eigen geometrie."
bo_toelichting: "Anders dan de BAG-Openbare Ruimte (benaming, gedefinieerd binnen één woonplaats) is een Gemeentelijke Openbare Ruimte een geo-object dat zich over meerdere woonplaatsen kan uitstrekken. De gemeente moet bij een openbareruimtebesluit een kaart als bijlage voegen; die geometrie en de gedeelde brondocumentgegevens worden bij dit object vastgelegd in plaats van bij elke afzonderlijke BAG-Openbare Ruimte."
bo_subtypes: []
bo_via_kandidaten: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/bag/gemeente|Gemeente]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Ligt in een gemeente"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/bag/openbare-ruimte|Openbare Ruimte]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Groepeert een of meer BAG-openbare ruimten die samen dezelfde gegevens delen (naam, brondocument)"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Heeft betekenis binnen het onderwerp | ✅ Draagt het formele openbareruimtebesluit en de bijbehorende geometrie |
| Herkenbaar voor domeinexperts | ✅ Geo-/basisregistratie-afdelingen onderscheiden expliciet de BAG-benaming van het gemeentelijk aangewezen gebied |
| Heeft een eigen bestaan binnen het onderwerp | ✅ Bestaat op een ander abstractieniveau dan de BAG-Openbare Ruimte: één gemeentelijke openbare ruimte kan meerdere BAG-woonplaatsen overspannen |
| Kan in meervoud bestaan | ✅ Elke gemeente kent er meerdere |
| Heeft een eigen levenscyclus | ✅ Datum begin/einde geldigheid, eigen brondocument (het openbareruimtebesluit) |
| Heeft relaties met andere concepten | ✅ Gemeente, (BAG-)Openbare Ruimte |

6/6 — BO. Geen directe GGM-entiteit gevonden (ook niet als attribuut); afgeleid van de bestaande GGM/BAG-entiteit OpenbareRuimte als het aggregatieniveau dat RSGB er expliciet bovenop modelleert.

## Beschrijving

Een Gemeentelijke Openbare Ruimte is het openbaar gedeelte van het gemeentelijk grondgebied zoals dat formeel wordt aangewezen door het bevoegde gemeentelijke orgaan — met een eigen geometrie, omdat een openbareruimtebesluit verplicht een kaart als bijlage heeft. Dit is een ander object dan de al bestaande [[Wiki/Bedrijfsobjecten/99-kern/bag/openbare-ruimte|Openbare Ruimte]] uit de BAG: die laatste is een *benaming* die per definitie binnen één woonplaats ligt, terwijl de Gemeentelijke Openbare Ruimte een *geo-object* is dat zich over meerdere woonplaatsen kan uitstrekken.

Omdat alle BAG-openbare ruimten die samen één gemeentelijke openbare ruimte vormen dezelfde naam en brondocumentgegevens delen, modelleert RSGB deze gedeelde gegevens op dit hogere niveau in plaats van ze bij elke BAG-Openbare Ruimte te herhalen.

## GGM-bron

Geen directe GGM-entiteit: dit objecttype komt alleen in RSGB Deel II voor, niet als aparte klasse in de GGM-XMI. Grondslag `ggm-afgeleid`: het aggregeert de al bestaande GGM/BAG-entiteit OpenbareRuimte (zie [[Wiki/Bedrijfsobjecten/99-kern/bag/openbare-ruimte|Openbare Ruimte]]) tot het niveau waarop de gemeente een openbareruimtebesluit neemt.

> "Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen openbaar gedeelte van het gemeentelijk grondgebied." (RSGB Deel II, objecttype Gemeentelijke Openbare Ruimte)

- **Attributen (RSGB Deel II):** identificatiecode, naam openbare ruimte, type openbare ruimte, status openbare ruimte, geometrie, datum begin/einde geldigheid

## Relaties

| Relatie | Richting | BO | Beschrijving | Bron |
|---|---|---|---|---|
| ligt in | → | [[Wiki/Bedrijfsobjecten/99-kern/bag/gemeente\|Gemeente]] | | RSGB Deel II |
| heeft | → | [[Wiki/Bedrijfsobjecten/99-kern/bag/openbare-ruimte\|Openbare Ruimte]] | Groepeert een of meer BAG-openbare ruimten | RSGB Deel II |

## Terugmelding GGM

Geen GGM-entiteit voor een reëel, herkenbaar registratieobject — mogelijk hiaat. Zie [[Wiki/Analyses/ggm-terugmeldingen]].

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rsgb-deel-ii-specificaties]]
