---
type: element
naam: Kunstwerkdeel
onderwerp: [Basisregistraties, BGT]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Kunstwerkdeel
ggm_guid: EAID_2EC96974_F21E_4bdb_AF4D_30D7091F5645
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: ["Objecten bij Vergunningaanvraag", "Hoofdobjecten IMGeo en Beheerobjecten", "Overige geo objecten op hoofdlijnen", "Overige geo objecten met attributen", "KUNSTWERKDEEL"]
ggm_diagram_ids: ["EAID_C9CE09B7_32EF_40eb_9C82_7FD6EDEA1D9E", "EAID_4896574A_C4DD_4b27_A3B9_4481F4B29CCB", "EAID_66FB74D4_C7D8_40b2_8512_B690FC8B2575", "EAID_AF86D21D_8F8E_4f0d_A1FA_FE7824E99EAD", "EAID_7DAF1FEF_4AF9_4aa7_B736_337DEF09C972"]
ggm_definitie: "Onderdeel van een civiel-technisch werk voor de infrastructuur van wegen, water, spoorbanen, waterkeringen en/of leidingen."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: "IMGeo 1.0"

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
  Dit BO heeft de GGM-entiteit **Kunstwerkdeel** als directe tegenhanger.
bo_definitie: "Onderdeel van een civiel-technisch werk voor de infrastructuur van wegen, water, spoorbanen, waterkeringen en/of leidingen."
bo_toelichting:
bo_relaties: []
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis binnen de BGT (registratie van civieltechnische infrastructuuronderdelen), herkenbaar voor domeinexperts (sluisdeel, stuwdeel, keermuurdeel), eigen bestaan (zelfstandig geregistreerd bouwwerkdeel), meervoud (meerdere kunstwerkdelen per gemeente), eigen levenscyclus (datumBeginGeldigheid/datumEindeGeldigheid), relaties (type, geometrie).

## Beschrijving

Een kunstwerkdeel is een onderdeel van een civieltechnisch werk voor de infrastructuur van wegen, water, spoorbanen, waterkeringen en/of leidingen. Het is een concreet subtype van het abstracte BGT-objecttype OverigeConstructie, naast [[Wiki/Bedrijfsobjecten/99-kern/bgt/overbruggingsdeel|Overbruggingsdeel]] en [[Wiki/Bedrijfsobjecten/99-kern/bgt/tunneldeel|Tunneldeel]].

Dit is een topografisch registratieobject, niet hetzelfde als het IMBOR-beheerobject [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/kunstwerk|Kunstwerk]] waarmee de gemeente onderhoud van civiele constructies plant.

## GGM-bron

> "Onderdeel van een civiel-technisch werk voor de infrastructuur van wegen, water, spoorbanen, waterkeringen en/of leidingen." (GGM, entiteit Kunstwerkdeel, beleidsdomein RSGBPlus)

- **Entiteit:** Kunstwerkdeel
- **Beleidsdomein:** RSGBPlus (taakveld 99 Kern)
- **Attributen:** identificatieKunstwerkdeel, statusKunstwerkdeel, relatieveHoogteliggingKunstwerkdeel, geometrieKunstwerkdeel, datumBeginGeldigheidKunstwerkdeel, datumEindeGeldigheidKunstwerkdeel
- **Matchsterkte:** exact

## Relaties

Geen relaties met andere BO's in de wiki op dit moment, buiten de gedeelde afkomst uit het abstracte objecttype OverigeConstructie en het onderscheid met [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/kunstwerk|Kunstwerk]].

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2]]
