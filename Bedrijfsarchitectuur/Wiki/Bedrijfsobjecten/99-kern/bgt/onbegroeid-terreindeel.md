---
type: element
naam: OnbegroeidTerreindeel
onderwerp: [Basisregistraties, BGT]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: OnbegroeidTerreindeel
ggm_guid: EAID_C32F1546_F793_4f13_91A4_2047E6DE6E91
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: ["Hoofdobjecten IMGeo en Beheerobjecten", "Kern:Overige geo objecten op hoofdlijnen", "Overige geo objecten op hoofdlijnen", "Overige geo objecten met attributen", "ONBEGROEID TERREINDEEL"]
ggm_diagram_ids: ["EAID_4896574A_C4DD_4b27_A3B9_4481F4B29CCB", "EAID_4BDFAFE0_D36A_40b7_B839_6742165859A7", "EAID_66FB74D4_C7D8_40b2_8512_B690FC8B2575", "EAID_AF86D21D_8F8E_4f0d_A1FA_FE7824E99EAD", "EAID_7DCBF509_0E31_4ff7_B343_65E435AB38B8"]
ggm_definitie: "Kleinste functioneel onafhankelijk stukje van een terrein, dat er binnen het objecttype Terrein van NEN 3610 wordt onderscheiden, zonder aaneengesloten vegetatie."
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
  Dit BO heeft de GGM-entiteit **OnbegroeidTerreindeel** als directe tegenhanger.
bo_definitie: "Kleinste functioneel onafhankelijk stukje terrein zonder aaneengesloten vegetatie, dat geen (ondersteunend) wegdeel, waterdeel of bouwwerk is."
bo_toelichting:
bo_relaties: []
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis binnen de BGT (kernobjecttype voor onbegroeid terrein), herkenbaar voor domeinexperts (verharde/onverharde terreinvlakken zonder vegetatie), eigen bestaan (zelfstandig geregistreerd vlak), meervoud (talrijke terreindelen per gemeente), eigen levenscyclus (datumBeginGeldigheid/datumEindeGeldigheid), relaties (fysiek voorkomen, talud, geometrie).

## Beschrijving

Een onbegroeid terreindeel is het kleinste, homogene stuk terrein zonder aaneengesloten vegetatie dat niet al als wegdeel, waterdeel of bouwwerk is geregistreerd — bijvoorbeeld een zandvlakte, een bouwterrein of een onverharde parkeerplaats. Het vormt samen met [[Wiki/Bedrijfsobjecten/99-kern/bgt/begroeid-terreindeel|BegroeidTerreindeel]] de BGT-categorie Terrein.

## GGM-bron

> "Kleinste functioneel onafhankelijk stukje van een terrein, dat er binnen het objecttype Terrein van NEN 3610 wordt onderscheiden, zonder aaneengesloten vegetatie." (GGM, entiteit OnbegroeidTerreindeel, beleidsdomein RSGBPlus)

- **Entiteit:** OnbegroeidTerreindeel
- **Beleidsdomein:** RSGBPlus (taakveld 99 Kern)
- **Attributen:** identificatie, status, relatieveHoogteligging, fysiekVoorkomen, plusFysiekVoorkomen, geometrie, kruinlijngeometrie, onbegroeidTerreindeelOpTalud, datumBeginGeldigheid, datumEindeGeldigheid
- **Matchsterkte:** exact

## Relaties

Geen relaties met andere BO's in de wiki op dit moment, buiten het onderscheid met [[Wiki/Bedrijfsobjecten/99-kern/bgt/begroeid-terreindeel|BegroeidTerreindeel]].

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2]]
