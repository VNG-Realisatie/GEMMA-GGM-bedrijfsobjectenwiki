---
type: element
naam: Ouderschap
onderwerp: [Basisregistraties, BRP, RSGBPlus]
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
bo_definitie: "Het verband tussen een kind en één van zijn of haar juridische ouders."
bo_toelichting: "Modelleert de BRP-categorieën 02 (Ouder 1), 03 (Ouder 2) en 09 (Kind). Ontstaat door geboorte, erkenning, gerechtelijke vaststelling van het ouderschap of adoptie; eindigt door ontkenning van het ouderschap. De BRP registreert per ouderschapsrelatie een datum ingang en datum einde familierechtelijke betrekking. Relevant voor gezag, erfrecht en naamgeving."
bo_subtypes: []
bo_via_kandidaten: []
bo_synoniemen:
  - naam: Ouder-kind-relatie
    context: "RSGB Deel II-objecttypenaam"
  - naam: Afstamming
    context: "BRP Logisch Ontwerp (groep 89, registratie afstamming)"
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon|Ingeschreven Persoon]]"
    richting: naar-dit-BO
    kardinaliteit: "2"
    beschrijving: "Betreft de ouder en het kind, beide ingeschreven personen"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Heeft betekenis binnen het onderwerp | ✅ Grondslag voor gezag, erfrecht, naamgeving en alimentatie |
| Herkenbaar voor domeinexperts | ✅ Burgerzaken/BRP-vaktaal: vaststelling, ontkenning en gerechtelijke vaststelling van ouderschap |
| Heeft een eigen bestaan binnen het onderwerp | ✅ Bestaat los van de twee betrokken personen, met een eigen ontstaans- en eindmoment |
| Kan in meervoud bestaan | ✅ Elk kind heeft (tot) twee ouderschapsrelaties |
| Heeft een eigen levenscyclus | ✅ Datum ingang/einde familierechtelijke betrekking |
| Heeft relaties met andere concepten | ✅ Twee Ingeschreven Personen (ouder en kind) |

6/6 — BO. Zelfde structuurpatroon als het al bestaande [[Wiki/Bedrijfsobjecten/99-kern/brp/huwelijk|Huwelijk]]: een relatie-objecttype tussen twee personen met een eigen levenscyclus, dat als zelfstandig BO is vastgelegd.

## Beschrijving

Ouderschap is het juridische verband tussen een kind en één van zijn of haar ouders, zoals vastgelegd in de BRP-categorieën Ouder 1, Ouder 2 en Kind. Het ontstaat door geboorte, erkenning, gerechtelijke vaststelling of adoptie, en kan eindigen door een gerechtelijke ontkenning van het ouderschap — met voor elk scenario een eigen set op te nemen gegevens op de persoonslijst van het kind (zie [[Wiki/Bronsamenvattingen/Standaarden/logisch-ontwerp-brp-2025q1|Logisch Ontwerp BRP 2025.Q1]] §2.1.5-2.1.6).

RSGB Deel II noemt dit objecttype "Ouder-kind-relatie"; de BRP-standaard zelf gebruikt consequent de term "ouderschap" (vaststelling ouderschap, ontkenning ouderschap) en "afstamming" (registratie afstamming, groep 89) — deze pagina volgt de BRP-terminologie omdat dat het gedragen juridische begrip is, niet het RSGB-informatiemodeljargon.

## Afleiding

Geen aparte GGM-klasse: de onderliggende gegevens (`ouder1`, `ouder2`, `gezinsrelatie`) zijn in de GGM-XMI al gemodelleerd als attributen op de bestaande entiteit IngeschrevenPersoon, niet als zelfstandige relatie-entiteit. Dit BO maakt die impliciete relatie expliciet als eigen object met een levenscyclus (datum ingang/einde familierechtelijke betrekking), zoals RSGB Deel II en het Logisch Ontwerp BRP dat allebei apart beschrijven.

## Relaties

| Relatie | Richting | BO | Beschrijving | Bron |
|---|---|---|---|---|
| betreft ouder | → | [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | De juridische ouder | RSGB Deel II / BRP |
| betreft kind | → | [[Wiki/Bedrijfsobjecten/99-kern/brp/ingeschreven-persoon\|Ingeschreven Persoon]] | Het kind | RSGB Deel II / BRP |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rsgb-deel-ii-specificaties]]
- [[Wiki/Bronsamenvattingen/Standaarden/logisch-ontwerp-brp-2025q1]]
