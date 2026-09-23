---
type: element
naam: OndersteunendWaterdeel
onderwerp: [Basisregistraties, BGT]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: OndersteunendWaterdeel
ggm_guid: EAID_7B92809F_CFAE_4be8_BE3A_4E4B94E83F52
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: ["Hoofdobjecten IMGeo en Beheerobjecten", "Overige geo objecten op hoofdlijnen", "Overige geo objecten met attributen", "ONDERSTEUNEND WATERDEEL"]
ggm_diagram_ids: ["EAID_4896574A_C4DD_4b27_A3B9_4481F4B29CCB", "EAID_66FB74D4_C7D8_40b2_8512_B690FC8B2575", "EAID_AF86D21D_8F8E_4f0d_A1FA_FE7824E99EAD", "EAID_16EB735F_475C_469b_9654_1569A13B8F31"]
ggm_definitie: "Object dat in het kader van de waterhuishouding periodiek gedeeltelijk of geheel met water is bedekt."
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
  Dit BO heeft de GGM-entiteit **OndersteunendWaterdeel** als directe tegenhanger.
bo_definitie: "Object dat in het kader van de waterhuishouding periodiek gedeeltelijk of geheel met water is bedekt."
bo_toelichting:
bo_relaties: []
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis binnen de BGT (afzonderlijk objecttype naast Waterdeel), herkenbaar voor domeinexperts (bijv. een periodiek overstromend bergingsgebied), eigen bestaan (zelfstandig geregistreerd vlak), meervoud (meerdere per gemeente), eigen levenscyclus (datumBeginGeldigheid/datumEindeGeldigheid), relaties (type, geometrie).

## Beschrijving

Een ondersteunend waterdeel is een object dat in het kader van de waterhuishouding periodiek — niet permanent — geheel of gedeeltelijk met water bedekt is, en wordt in de BGT onderscheiden van het permanent waterbedekte [[Wiki/Bedrijfsobjecten/99-kern/bgt/waterdeel|Waterdeel]].

## GGM-bron

> "Object dat in het kader van de waterhuishouding periodiek gedeeltelijk of geheel met water is bedekt." (GGM, entiteit OndersteunendWaterdeel, beleidsdomein RSGBPlus)

- **Entiteit:** OndersteunendWaterdeel
- **Beleidsdomein:** RSGBPlus (taakveld 99 Kern)
- **Attributen:** identificatie, status, geometrie, relatieveHoogteligging, type, plusType, datumBeginGeldigheid, datumEindeGeldigheid
- **Matchsterkte:** exact

## Relaties

Geen relaties met andere BO's in de wiki op dit moment, buiten het onderscheid met [[Wiki/Bedrijfsobjecten/99-kern/bgt/waterdeel|Waterdeel]].

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2]]
