---
type: element
naam: Wegdeel
onderwerp: [Basisregistraties, BGT]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Wegdeel
ggm_guid: EAID_9B0F3F8B_B79B_46f7_BF81_96E4C63B9AC2
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram: ["Verkeer en Vervoer: Stremmingen", "Hoofdobjecten IMGeo en Beheerobjecten", "Overige geo objecten op hoofdlijnen", "Overige geo objecten met attributen", "WEGDEEL"]
ggm_diagram_ids: ["EAID_72A4FC74_EE1B_4bc1_B5BB_540FCE4D04B1", "EAID_4896574A_C4DD_4b27_A3B9_4481F4B29CCB", "EAID_66FB74D4_C7D8_40b2_8512_B690FC8B2575", "EAID_AF86D21D_8F8E_4f0d_A1FA_FE7824E99EAD", "EAID_3A41FD49_9827_4ed2_A7B6_7CD41A4A0B9B"]
ggm_definitie: "Kleinste functioneel onafhankelijk stukje van een NEN 3610 Weg, met gelijkblijvende homogene eigenschappen en relaties en primair bedoeld voor gebruik door weg-, spoor- en vliegverkeer te land."
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
  Dit BO heeft de GGM-entiteit **Wegdeel** als directe tegenhanger.
bo_definitie: "Kleinste functioneel onafhankelijk stukje van een weg, met gelijkblijvende eigenschappen, primair bedoeld voor weg-, spoor- of vliegverkeer te land."
bo_toelichting: "Onderscheiden naar functie (rijbaan, fietspad, voetpad e.d.) en fysiek voorkomen (verhard/onverhard) via de attributen functieWegdeel en fysiekVoorkomenWegdeel."
bo_relaties: []
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis binnen de topografische basisregistratie (kernobject van de BGT-wegcategorie), herkenbaar voor domeinexperts (rijbaan/fietspad/voetpad als wegdeel), eigen bestaan (zelfstandig geregistreerd vlak met identificatie), meervoud (elke gemeente registreert duizenden wegdelen), eigen levenscyclus (datumBeginGeldigheid/datumEindeGeldigheid, wijziging bij herinrichting), relaties (functie, fysiek voorkomen, talud, geometrie).

## Beschrijving

Een wegdeel is het kleinste, functioneel homogene stuk van een weg zoals geregistreerd in de Basisregistratie Grootschalige Topografie (BGT): een aaneengesloten vlak met dezelfde functie (bijv. rijbaan of fietspad) en hetzelfde fysieke voorkomen (bijv. verhard of onverhard). Een fysieke weg bestaat doorgaans uit meerdere wegdelen naast elkaar (rijbaan, fietspad, voetpad).

Wegdeel is een van de 18 objecttypen van de BGT en valt onder de groep topografische objecten die de fysieke werkelijkheid van de openbare ruimte in kaart brengen — complementair aan, maar niet hetzelfde als, de IMBOR-beheerobjecten waarmee de gemeente onderhoud plant (zie [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/verhardingsobject|Verhardingsobject]]).

## GGM-bron

> "Kleinste functioneel onafhankelijk stukje van een NEN 3610 Weg, met gelijkblijvende homogene eigenschappen en relaties en primair bedoeld voor gebruik door weg-, spoor- en vliegverkeer te land." (GGM, entiteit Wegdeel, beleidsdomein RSGBPlus)

- **Entiteit:** Wegdeel
- **Beleidsdomein:** RSGBPlus (taakveld 99 Kern)
- **Attributen:** identificatieWegdeel, statusWegdeel, relatieveHoogteliggingWegdeel, geometrieWegdeel, kruinlijngeometrieWegdeel, functieWegdeel, plusFunctieWegdeel, fysiekVoorkomenWegdeel, plusFysiekVoorkomenWegdeel, wegdeelOpTalud, datumBeginGeldigheidWegdeel, datumEindeGeldigheidWegdeel
- **Matchsterkte:** exact

## Relaties

Geen relaties met andere BO's in de wiki op dit moment.

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2]]
