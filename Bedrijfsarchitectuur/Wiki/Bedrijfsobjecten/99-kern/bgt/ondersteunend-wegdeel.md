---
type: element
naam: OndersteunendWegdeel
onderwerp: [Basisregistraties, BGT]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: OndersteunendWegdeel
ggm_guid: EAID_F55A5977_7E3B_4cf4_B8D1_CFCEECA0DEA1
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: ["Hoofdobjecten IMGeo en Beheerobjecten", "Overige geo objecten op hoofdlijnen", "Overige geo objecten met attributen", "ONDERSTEUNEND WEGDEEL"]
ggm_diagram_ids: ["EAID_4896574A_C4DD_4b27_A3B9_4481F4B29CCB", "EAID_66FB74D4_C7D8_40b2_8512_B690FC8B2575", "EAID_AF86D21D_8F8E_4f0d_A1FA_FE7824E99EAD", "EAID_FEE365FC_F7EF_4271_977B_6F9A29FB9474"]
ggm_definitie: "Een deel van de weg dat niet primair bedoeld is voor gebruik door het verkeer."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: CityGML

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
  Dit BO heeft de GGM-entiteit **OndersteunendWegdeel** als directe tegenhanger.
bo_definitie: "Een deel van de weg dat niet primair bedoeld is voor gebruik door het verkeer, zoals een berm of trottoirband."
bo_toelichting:
bo_relaties: []
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis binnen de BGT (afzonderlijk objecttype naast Wegdeel), herkenbaar voor domeinexperts (berm, trottoirband), eigen bestaan (zelfstandig geregistreerd vlak), meervoud (elke weg heeft doorgaans meerdere ondersteunende wegdelen), eigen levenscyclus (datumBeginGeldigheid/datumEindeGeldigheid), relaties (functie, fysiek voorkomen, talud).

## Beschrijving

Een ondersteunend wegdeel is het deel van een weg dat niet primair bedoeld is voor verkeer — bijvoorbeeld een berm of een trottoirband — maar wel bij de weg hoort en in de BGT als eigen objecttype wordt onderscheiden van [[Wiki/Bedrijfsobjecten/99-kern/bgt/wegdeel|Wegdeel]].

## GGM-bron

> "Een deel van de weg dat niet primair bedoeld is voor gebruik door het verkeer." (GGM, entiteit OndersteunendWegdeel, beleidsdomein RSGBPlus)

- **Entiteit:** OndersteunendWegdeel
- **Beleidsdomein:** RSGBPlus (taakveld 99 Kern)
- **Attributen:** identificatie, status, geometrie, relatieveHoogteligging, kruinlijngeometrie, functie, plusFunctie, fysiekVoorkomen, plusFysiekVoorkomen, opTalud, datumBeginGeldigheid, datumEindeGeldigheid
- **Matchsterkte:** exact

## Relaties

Geen relaties met andere BO's in de wiki op dit moment, buiten het onderscheid met [[Wiki/Bedrijfsobjecten/99-kern/bgt/wegdeel|Wegdeel]].

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2]]
