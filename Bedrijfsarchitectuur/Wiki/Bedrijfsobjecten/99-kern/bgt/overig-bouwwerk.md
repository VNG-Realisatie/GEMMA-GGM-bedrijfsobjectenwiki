---
type: element
naam: OverigBouwwerk
onderwerp: [Basisregistraties, BGT]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: OverigBouwwerk
ggm_guid: EAID_1DA7BC25_CF02_4161_B9A2_DE0BE27C5254
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: ["Hoofdobjecten IMGeo en Beheerobjecten", "Kern:Overige geo objecten op hoofdlijnen", "Overige geo objecten op hoofdlijnen", "Overige geo objecten met attributen", "OVERIG GEBOUWD OBJECT", "OVERIG BOUWWERK"]
ggm_diagram_ids: ["EAID_4896574A_C4DD_4b27_A3B9_4481F4B29CCB", "EAID_4BDFAFE0_D36A_40b7_B839_6742165859A7", "EAID_66FB74D4_C7D8_40b2_8512_B690FC8B2575", "EAID_AF86D21D_8F8E_4f0d_A1FA_FE7824E99EAD", "EAID_4700DBC7_34E9_4ff1_A6E1_A37CBA99EC28", "EAID_38A8E6E9_1B62_4e6c_9EB6_1B09B369928C"]
ggm_definitie: "Met de aarde verbonden duurzaam bouwwerk, dat niet valt onder de definities van een pand of kunstwerk."
ggm_toelichting: "Een Overig Bouwwerk heeft in de BGT altijd vlakgeometrie. Een overkapping heeft multivlakgeometrie."
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
  Dit BO heeft de GGM-entiteit **OverigBouwwerk** als directe tegenhanger.
bo_definitie: "Met de aarde verbonden duurzaam bouwwerk dat niet valt onder de definities van een pand of kunstwerk, bijvoorbeeld een overkapping."
bo_toelichting:
bo_relaties: []
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis binnen de BGT (restcategorie bouwwerken), herkenbaar voor domeinexperts (overkapping, silo e.d.), eigen bestaan (zelfstandig geregistreerd bouwwerk), meervoud (meerdere per gemeente), eigen levenscyclus (datumBeginGeldigheid/datumEindeGeldigheid), relaties (subtype van OverigeConstructie, geometrie).

## Beschrijving

Een overig bouwwerk is een duurzaam met de aarde verbonden bouwwerk dat geen [[Wiki/Bedrijfsobjecten/99-kern/bag/pand|Pand]] is en ook geen kunstwerk — bijvoorbeeld een overkapping. Het is één van de concrete subtypes van het abstracte BGT-objecttype OverigeConstructie, samen met [[Wiki/Bedrijfsobjecten/99-kern/bgt/overbruggingsdeel|Overbruggingsdeel]], [[Wiki/Bedrijfsobjecten/99-kern/bgt/tunneldeel|Tunneldeel]], [[Wiki/Bedrijfsobjecten/99-kern/bgt/kunstwerkdeel|Kunstwerkdeel]] en [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/scheiding|Scheiding]].

## GGM-bron

> "Met de aarde verbonden duurzaam bouwwerk, dat niet valt onder de definities van een pand of kunstwerk." (GGM, entiteit OverigBouwwerk, beleidsdomein RSGBPlus)

- **Entiteit:** OverigBouwwerk
- **Beleidsdomein:** RSGBPlus (taakveld 99 Kern)
- **Attributen:** identificatieOverigBouwwerk, statusOverigBouwwerk, relatieveHoogteliggingOverigBouwwerk, geometrieOverigBouwwerk, datumBeginGeldigheidOverigBouwwerk, datumEindeGeldigheidOverigBouwwerk
- **Matchsterkte:** exact

## Relaties

Geen relaties met andere BO's in de wiki op dit moment, buiten de gedeelde afkomst uit het abstracte objecttype OverigeConstructie (zie Beschrijving).

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2]]
