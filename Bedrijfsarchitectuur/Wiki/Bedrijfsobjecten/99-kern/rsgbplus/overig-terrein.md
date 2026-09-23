---
type: element
naam: Overig Terrein
onderwerp: [Basisregistraties, RSGBPlus]
archimate_type: business-object
grondslag: ggm-entiteit

# GGM-velden
ggm_entiteit: OverigBenoemdTerrein
ggm_guid: EAID_CFA3D54E_C8E0_4559_9475_29D31AF2DECD
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram:
  - "Diagram Sportbeleid Locaties"
  - "Ruimte Adressen, gebouwen en terreinen"
  - "Vastgoed verankering RSGB IMBAG"
  - "Detaillering adressen, gebouwen en terreinen op hoofdlijnen"
ggm_diagram_ids: []
ggm_definitie: "Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen onbebouwd terrein of een gedeelte daarvan, geen standplaats of gedeelte van een ligplaats zijnde, dat bestemd is voor het gedurende langere tijd verrichten van een maatschappelijke activiteit."
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
bo_definitie: "Door de gemeente aangewezen onbebouwd terrein, geen standplaats of ligplaats, bestemd voor het langdurig verrichten van een maatschappelijke activiteit."
bo_toelichting: "Voorbeelden: autosloperijen, volkstuincomplexen en sportvelden zonder opstallen. Bedoeld om, naast stand- en ligplaatsen, terreinen met een verblijfsfunctie te registreren die geen authentiek maar wel een officieel adres nodig hebben. Wordt alleen geregistreerd voor zover de gemeente dat relevant vindt (GGM-entiteitnaam: OverigBenoemdTerrein — RSGB Deel II noemt het objecttype zelf \"Overig Terrein\")."
bo_subtypes: []
bo_via_kandidaten: []
bo_synoniemen:
  - naam: OverigBenoemdTerrein
    context: "GGM-entiteitnaam"
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/bag/standplaats|Standplaats (BAG)]]"
    richting: bidirectioneel
    kardinaliteit:
    beschrijving: "Beide zijn specialisaties van Benoemd Terrein (abstract), samen met Ligplaats"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/sport/sportpark|Sportpark]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een sportpark ligt op een overig terrein"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/sport/veld|Veld]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een veld ligt op een overig terrein"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/bag/buurt|Buurt]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Ligt in een buurt"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Heeft betekenis binnen het onderwerp | ✅ Vult de terreinregistratie aan met onbebouwde terreinen die geen stand-/ligplaats zijn maar wel een officieel adres nodig hebben |
| Herkenbaar voor domeinexperts | ✅ Herkenbare voorbeelden: autosloperijen, volkstuincomplexen, sportvelden zonder opstal |
| Heeft een eigen bestaan binnen het onderwerp | ✅ Zelfstandig aangewezen terrein, los van stand- en ligplaatsen |
| Kan in meervoud bestaan | ✅ Elke gemeente registreert er meerdere, voor zover relevant geacht |
| Heeft een eigen levenscyclus | ✅ Datum begin/einde geldigheid benoemd terrein |
| Heeft relaties met andere concepten | ✅ Buurt, adresaanduiding, sportparken/velden |

6/6 — sterke BO. Parallel aan de al bestaande [[Wiki/Bedrijfsobjecten/99-kern/bag/standplaats|Standplaats (BAG)]] en Ligplaats: samen dekken zij de specialisaties van de GGM-generalisatie Benoemd Terrein.

## Beschrijving

Overig Terrein is de aanvulling die de gemeente kan registreren naast de BAG-standplaatsen en -ligplaatsen: onbebouwde terreinen met een verblijfsfunctie waarvan de vindbaarheid op basis van een officieel adres gewenst is, maar die geen authentiek BAG-object zijn. Voorbeelden: autosloperijen, volkstuincomplexen en sportvelden zonder opstallen.

Net als bij [[Wiki/Bedrijfsobjecten/99-kern/rsgbplus/overig-gebouwd-object|Overig Gebouwd Object]] is registratie optioneel en alleen voor zover de gemeente dat relevant vindt. Elk overig terrein krijgt een eigen "overige adresseerbaar object aanduiding" (geen apart BO).

## Generalisatie

Overig Terrein is, samen met [[Wiki/Bedrijfsobjecten/99-kern/bag/standplaats|Standplaats (BAG)]] en Ligplaats, een specialisatie van de GGM-generalisatie Benoemd Terrein, die op haar beurt een specialisatie is van Benoemd Object — beide eerder beoordeeld als "geen eigen BO" (zie [[Wiki/Onderwerpoverzichten/basisregistraties|Onderwerpoverzicht Basisregistraties]] §RSGBPlus). Alle drie specialisaties delen dezelfde relaties naar Buurt, Kadastrale Onroerende Zaak, WOZ-deelobject en Vestiging.

## GGM-bron

> "Een door het bevoegde gemeentelijke orgaan als zodanig aangewezen onbebouwd terrein of een gedeelte daarvan, geen standplaats of gedeelte van een ligplaats zijnde, dat bestemd is voor het gedurende langere tijd verrichten van een maatschappelijke activiteit."

- **Entiteit:** OverigBenoemdTerrein
- **Package:** RSGB Model > Model Kern RSGB
- **Attributen:** overigBenoemdTerreinIdentificatie, gebruiksdoelOverigBenoemdTerrein (+ attributen van de generalisatie Benoemd Terrein: geometrie, geldigheidsdatums, typering)
- **Matchsterkte:** exact — de GGM-entiteitnaam ("OverigBenoemdTerrein") wijkt af van de RSGB Deel II-objecttypenaam ("Overig Terrein"); zelfde concept, vastgelegd als synoniem

## Relaties

| Relatie | Richting | BO | Beschrijving | Bron |
|---|---|---|---|---|
| ligt in | → | [[Wiki/Bedrijfsobjecten/99-kern/bag/buurt\|Buurt]] | Via generalisatie Benoemd Object | GGM |
| ligt op | ← | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/sport/sportpark\|Sportpark]] | Sportpark ligt op een overig terrein | GGM |
| ligt op | ← | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/sport/veld\|Veld]] | Veld ligt op een overig terrein | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rsgb-deel-ii-specificaties]]
