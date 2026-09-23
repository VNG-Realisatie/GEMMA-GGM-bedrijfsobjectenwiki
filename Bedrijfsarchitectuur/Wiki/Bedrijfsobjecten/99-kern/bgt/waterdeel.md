---
type: element
naam: Waterdeel
onderwerp: [Basisregistraties, BGT]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Waterdeel
ggm_guid: EAID_FD0B5F4D_AE9B_47bd_8C60_031D21AC24B1
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: ["Objecten bij Vergunningaanvraag", "Hoofdobjecten IMGeo en Beheerobjecten", "Overige geo objecten op hoofdlijnen", "Overige geo objecten met attributen", "WATERDEEL"]
ggm_diagram_ids: ["EAID_C9CE09B7_32EF_40eb_9C82_7FD6EDEA1D9E", "EAID_4896574A_C4DD_4b27_A3B9_4481F4B29CCB", "EAID_66FB74D4_C7D8_40b2_8512_B690FC8B2575", "EAID_AF86D21D_8F8E_4f0d_A1FA_FE7824E99EAD", "EAID_455B32ED_E912_4f10_B9FB_849DBC63AF2B"]
ggm_definitie: "Kleinste functioneel onafhankelijk stukje water met gelijkblijvende, homogene eigenschappen en relaties dat er binnen het objecttype Water van NEN 3610 wordt onderscheiden en dat permanent met water bedekt is."
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
  Dit BO heeft de GGM-entiteit **Waterdeel** als directe tegenhanger.
bo_definitie: "Kleinste functioneel onafhankelijk stukje water dat permanent met water is bedekt."
bo_toelichting:
bo_relaties: []
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis binnen de BGT (kernobjecttype voor permanent water), herkenbaar voor domeinexperts (sloot, gracht, vijver als waterdeel), eigen bestaan (zelfstandig geregistreerd vlak), meervoud (talrijke waterdelen per gemeente), eigen levenscyclus (datumBeginGeldigheid/datumEindeGeldigheid), relaties (type, geometrie).

## Beschrijving

Een waterdeel is het kleinste, homogene stuk permanent water dat binnen de BGT-categorie Water wordt onderscheiden — bijvoorbeeld een gracht, sloot of vijver. Complementair aan [[Wiki/Bedrijfsobjecten/99-kern/bgt/ondersteunend-waterdeel|OndersteunendWaterdeel]] (periodiek water).

Dit is een topografisch registratieobject, niet hetzelfde als het IMBOR-beheerobject [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/waterobject|Waterobject]] waarmee de gemeente waterbeheer plant.

## GGM-bron

> "Kleinste functioneel onafhankelijk stukje water met gelijkblijvende, homogene eigenschappen en relaties dat er binnen het objecttype Water van NEN 3610 wordt onderscheiden en dat permanent met water bedekt is." (GGM, entiteit Waterdeel, beleidsdomein RSGBPlus)

- **Entiteit:** Waterdeel
- **Beleidsdomein:** RSGBPlus (taakveld 99 Kern)
- **Attributen:** identificatieWaterdeel, statusWaterdeel, relatieveHoogteliggingWaterdeel, geometrieWaterdeel, typeWaterdeel, plusTypeWaterdeel, datumBeginGeldigheidWaterdeel, datumEindeGeldigheidWaterdeel
- **Matchsterkte:** exact

## Relaties

Geen relaties met andere BO's in de wiki op dit moment, buiten het onderscheid met [[Wiki/Bedrijfsobjecten/99-kern/bgt/ondersteunend-waterdeel|OndersteunendWaterdeel]] en [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/waterobject|Waterobject]].

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2]]
