---
type: element
naam: Functioneel gebied
onderwerp: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "FunctioneelGebied"
ggm_guid: EAID_43DD67FD_75F0_4FE0_90F0_DB49048F14C
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Hoofdobjecten IMBOR en Geo-object]
ggm_diagram_ids: [EAID_E3EBD7A0_35C4_4bf4_BD01_6D97AD0B8BF3]
ggm_definitie: "Begrensd en benoemd gebied dat door een functionele eenheid beschreven wordt."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten:
  - entiteit: FunctioneelGebied
    guid: EAID_B8F44180_1F2A_4bbc_8E17_6C472111A92B
    beleidsdomein: RSGBPlus
    taakveld: "99 Kern"
    afwijkende_attributen: "RSGBPlus gebruikt domein-geprefixte BGT-registratievelden (identificatieFunctioneelGebied, statusFunctioneelGebied, datumBeginGeldigheidFunctioneelGebied/datumEindeGeldigheidFunctioneelGebied). Beheer Openbare Ruimte (IMBOR) heeft alleen code, naam, geometrie, omtrek en oppervlakte — geen registratie-tijdvelden."

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **FunctioneelGebied** (beleidsdomein Beheer Openbare Ruimte) als directe tegenhanger. Daarnaast is **FunctioneelGebied** (beleidsdomein RSGBPlus, BGT) als duplicaat gekoppeld — zie ggm_duplicaat_entiteiten.
bo_definitie: "Begrensd en benoemd gebied dat door een functionele eenheid wordt beschreven, bijvoorbeeld een evenemententerrein of recreatiegebied."
bo_toelichting:
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/speelterrein|Speelterrein]]"
    richting: "naar-dit-BO"
    kardinaliteit:
    beschrijving: Speelterrein is een specialisatie van Functioneel gebied in het GGM
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

Alle 6 criteria van toepassing: betekenis binnen het beheerdomein (functionele gebiedsafbakening los van eigendoms- of kadastergrenzen), herkenbaar voor domeinexperts (evenemententerrein, recreatiegebied, bedrijventerrein als functioneel gebied), eigen bestaan (zelfstandig begrensd en benoemd gebied), meervoud (meerdere functionele gebieden per gemeente), eigen levenscyclus (vaststelling, wijziging van begrenzing), relaties (naam, geometrie, oppervlakte).

## Beschrijving

Een functioneel gebied is een begrensd en benoemd gebied dat door een functionele eenheid wordt beschreven — bijvoorbeeld een evenemententerrein, recreatiegebied of bedrijventerrein — los van kadastrale of bestuurlijke grenzen.

Dit begrip komt in het GGM twee keer voor met identieke definitie: als IMBOR-beheerobject in Beheer Openbare Ruimte (dit BO, gekozen als primair) en als topografisch registratieobject in RSGBPlus/BGT (zie GGM-duplicaten). Beide GUID's zijn tot nu toe zonder BO-pagina; dit is de eerste vastlegging.

## GGM-bron

> "Begrensd en benoemd gebied dat door een functionele eenheid beschreven wordt." (GGM, entiteit FunctioneelGebied, beleidsdomein Beheer Openbare Ruimte)

- **Entiteit:** FunctioneelGebied
- **Beleidsdomein:** Beheer Openbare Ruimte (taakveld 8)
- **Attributen:** functioneelGebiedCode, functioneelGebiedNaam, omtrek, oppervlakte
- **Matchsterkte:** exact

## GGM-duplicaten

De GGM-entiteit "FunctioneelGebied" komt voor in 2 beleidsdomeinen:

| Beleidsdomein | GUID | Status |
|---|---|---|
| **Beheer Openbare Ruimte** | `EAID_43DD67FD_75F0_4FE0_90F0_DB49048F14C` | **primair** — gekozen omdat dit BO de beheercontext beschrijft waarin de gemeente functionele gebieden aanwijst en beheert |
| RSGBPlus (BGT) | `EAID_B8F44180_1F2A_4bbc_8E17_6C472111A92B` | duplicaat — topografische registratievariant (identieke definitie), zie ook [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2|Gegevenscatalogus BGT 1.2]] |

Attribuutverschil: RSGBPlus draagt BGT-registratievelden (status, geldigheidsdatums); Beheer Openbare Ruimte heeft alleen code, naam, geometrie en oppervlaktegegevens.

Teruggemeld als #101 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Specialisaties

| Specialisatie | Omschrijving | GGM-entiteit |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/speelterrein\|Speelterrein]] | Afgebakende openbare ruimte ingericht als speelplaats voor kinderen | Speelterrein (eigen GGM-entiteit) |

## Relaties

| Relatie | Richting | Bron |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/speelterrein\|Speelterrein]] | Speelterrein → Functioneel gebied (generalisatie) | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/catalogus-bgt-1.2]]
