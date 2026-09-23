---
type: element
naam: Overbruggingsdeel
onderwerp: [Basisregistraties, BGT]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Overbruggingsdeel
ggm_guid: EAID_2E45A5F3_A685_48c5_98D4_794BE382891E
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: ["Hoofdobjecten IMGeo en Beheerobjecten", "Overige geo objecten op hoofdlijnen", "Overige geo objecten met attributen", "OVERBRUGGINSDEEL"]
ggm_diagram_ids: ["EAID_4896574A_C4DD_4b27_A3B9_4481F4B29CCB", "EAID_66FB74D4_C7D8_40b2_8512_B690FC8B2575", "EAID_AF86D21D_8F8E_4f0d_A1FA_FE7824E99EAD", "EAID_FE76A77C_8D9C_4741_948C_B59D7B918FE3"]
ggm_definitie: "Onderdeel van een beweegbare of vaste verbinding tussen twee punten, die door water, een weg of anderszins gescheiden zijn, dat essentieel is voor de constructie."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: BGT

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
  Dit BO heeft de GGM-entiteit **Overbruggingsdeel** als directe tegenhanger.
bo_definitie: "Onderdeel van een beweegbare of vaste verbinding tussen twee door water, een weg of anderszins gescheiden punten, essentieel voor de constructie — bijvoorbeeld een brugdek."
bo_toelichting:
bo_relaties: []
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis binnen de BGT (registratie van brugconstructies), herkenbaar voor domeinexperts (brugdek, viaductdeel), eigen bestaan (zelfstandig geregistreerd bouwwerkdeel), meervoud (meerdere bruggen per gemeente), eigen levenscyclus (datumBeginGeldigheid/datumEindeGeldigheid), relaties (type, beweegbaarheid, geometrie).

## Beschrijving

Een overbruggingsdeel is een essentieel onderdeel van een beweegbare of vaste verbinding (brug, viaduct) tussen twee punten die door water, een weg of anderszins gescheiden zijn. Het is een concreet subtype van het abstracte BGT-objecttype OverigeConstructie, naast [[Wiki/Bedrijfsobjecten/99-kern/bgt/tunneldeel|Tunneldeel]] en [[Wiki/Bedrijfsobjecten/99-kern/bgt/kunstwerkdeel|Kunstwerkdeel]].

## GGM-bron

> "Onderdeel van een beweegbare of vaste verbinding tussen twee punten, die door water, een weg of anderszins gescheiden zijn, dat essentieel is voor de constructie." (GGM, entiteit Overbruggingsdeel, beleidsdomein RSGBPlus)

- **Entiteit:** Overbruggingsdeel
- **Beleidsdomein:** RSGBPlus (taakveld 99 Kern)
- **Attributen:** identificatieOverbruggingsdeel, statusOverbruggingsdeel, relatieveHoogteliggingOverbruggingsdeel, typeOverbruggingsdeel, hoortBijTypeOverbrugging, overbruggingIsBeweegbaar, geometrieOverbruggingsdeel, datumBeginGeldigheidOverbruggingsdeel, datumEindeGeldigheidOverbruggingsdeel
- **Matchsterkte:** exact

## Relaties

Geen relaties met andere BO's in de wiki op dit moment, buiten de gedeelde afkomst uit het abstracte objecttype OverigeConstructie.

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2]]
