---
type: element
naam: BegroeidTerreindeel
onderwerp: [Basisregistraties, BGT]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: BegroeidTerreindeel
ggm_guid: EAID_D872C213_09D7_4dca_A020_EA363480FC7D
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: ["Hoofdobjecten IMGeo en Beheerobjecten", "Kern:Overige geo objecten op hoofdlijnen", "Overige geo objecten op hoofdlijnen", "Overige geo objecten met attributen", "BEGROEID TERREINDEEL"]
ggm_diagram_ids: ["EAID_4896574A_C4DD_4b27_A3B9_4481F4B29CCB", "EAID_4BDFAFE0_D36A_40b7_B839_6742165859A7", "EAID_66FB74D4_C7D8_40b2_8512_B690FC8B2575", "EAID_AF86D21D_8F8E_4f0d_A1FA_FE7824E99EAD", "EAID_1947D48F_6D4E_4943_B313_091CF7B56117"]
ggm_definitie: "Kleinste functioneel onafhankelijk stukje van een terrein dat er binnen het objecttype Terrein van NEN 3610 wordt onderscheiden, met aaneengesloten homogene vegetatie."
ggm_toelichting: "Vlakvormig groenobject."
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
  Dit BO heeft de GGM-entiteit **BegroeidTerreindeel** als directe tegenhanger.
bo_definitie: "Kleinste functioneel onafhankelijk stukje terrein met aaneengesloten vegetatie — een vlakvormig groenobject."
bo_toelichting:
bo_relaties: []
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis binnen de BGT (kernobjecttype voor begroeid terrein), herkenbaar voor domeinexperts (plantsoen, gazon, bosschage als begroeid terreindeel), eigen bestaan (zelfstandig geregistreerd vlak), meervoud (talrijke terreindelen per gemeente), eigen levenscyclus (datumBeginGeldigheid/datumEindeGeldigheid), relaties (fysiek voorkomen, talud, geometrie).

## Beschrijving

Een begroeid terreindeel is het kleinste, homogene stuk terrein met aaneengesloten vegetatie — een vlakvormig groenobject zoals een plantsoen, gazon of bosschage — geregistreerd binnen de BGT-categorie Terrein, complementair aan [[Wiki/Bedrijfsobjecten/99-kern/bgt/onbegroeid-terreindeel|OnbegroeidTerreindeel]].

Dit is een topografisch registratieobject (wat op de kaart als groen wordt weergegeven), niet hetzelfde als het IMBOR-beheerobject [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/groenobject|Groenobject]] waarmee de gemeente onderhoud plant — beide bestaan naast elkaar als aparte GGM-beleidsdomeinen voor dezelfde fysieke werkelijkheid.

## GGM-bron

> "Kleinste functioneel onafhankelijk stukje van een terrein dat er binnen het objecttype Terrein van NEN 3610 wordt onderscheiden, met aaneengesloten homogene vegetatie." (GGM, entiteit BegroeidTerreindeel, beleidsdomein RSGBPlus)

- **Entiteit:** BegroeidTerreindeel
- **Beleidsdomein:** RSGBPlus (taakveld 99 Kern)
- **Attributen:** identificatie, status, relatieveHoogteligging, fysiekVoorkomen, plusFysiekVoorkomen, kruinlijngeometrie, geometrie, LOD0Geometrie, opTalud, datumBeginGeldigheid, datumEindeGeldigheid
- **Matchsterkte:** exact

## Relaties

Geen relaties met andere BO's in de wiki op dit moment, buiten het onderscheid met [[Wiki/Bedrijfsobjecten/99-kern/bgt/onbegroeid-terreindeel|OnbegroeidTerreindeel]] en [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/groenobject|Groenobject]].

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2]]
