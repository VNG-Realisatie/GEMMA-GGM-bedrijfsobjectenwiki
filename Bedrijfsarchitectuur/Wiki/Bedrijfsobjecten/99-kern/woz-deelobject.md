---
type: element
naam: "WOZ-deelobject"
domein: [Belastingen]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "WOZ-deelobject"
ggm_guid: EAID_EEC30588_0E12_41c9_977E_C885A0A7EDC3
ggm_uml_type: Class
ggm_beleidsdomein: "RSGBPlus"
ggm_taakveld: "99 Kern"
ggm_diagram: [WOZ-DEELOBJECT, BENOEMD OBJECT, Detaillering WOZ-objecttypen op hoofdlijnen, Detaillering WOZ-objecttypen met attributen]
ggm_diagram_ids: [EAID_8312FF96_BCFE_4913_B7AB_27E9F690F89D, EAID_DE2BA1A2_AB9D_40ed_B9C1_E7F2F9A0BC49, EAID_3F813481_9A40_4b1b_9B24_1FD069230A45, EAID_5E76FEEA_58F8_41fd_9FF1_B44274C80FA5]
ggm_definitie: "Aanduiding van afzonderlijke elementen (delen van het object, bijzondere waarderelevante factoren) die voor de onderbouwing van de vastgestelde waarde van belang zijn."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "Gegevenswoordenboek WOZ"
ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **WOZ-deelobject** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **WOZ-Deelobjectcode** (classificatie) — Typering/referentietabel
bo_definitie: "Aanduiding van afzonderlijke elementen (delen van het object, bijzondere waarderelevante factoren) die voor de onderbouwing van de vastgestelde waarde van belang zijn."
bo_toelichting: ''
bo_via_kandidaten:
  - ggm_entiteit: "Winkelvloeroppervlak"
    ggm_guid: "EAID_0EABA880_434F_41c3_A41D_0002222AAC2A"
    reden: "Winkelvloeroppervlak is een waarderelevant deelelement voor de WOZ-waardebepaling."
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/woz-object|WOZ-object]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1"
    beschrijving: "Een WOZ-deelobject is onderdeel van een WOZ-object"
bedrijfsprocessen: [WOZ-taxatie, bezwaarbehandeling WOZ]
bedrijfsfuncties: [Waardering onroerende zaken]
---

# WOZ-deelobject

Afzonderlijk element van een WOZ-object dat bijdraagt aan de onderbouwing van de vastgestelde waarde.

## BO-criteria toetsing

| Criterium | Toelichting |
|---|---|
| Registratie | Eigen identificatie (WOZDeelobjectNummer), code en status |
| Meervoud | Een WOZ-object kan meerdere deelobjecten hebben (woning, garage, grond, bijgebouw) |
| Levenscyclus | Begin- en eindegeldigheid; status wijzigt bij splitsing, sloop of verbouwing |
| Eigendom | Gemeente (taxateur) bepaalt de afbakening van deelobjecten |
| Gemeentelijk belang | Onderbouwt de WOZ-waarde die grondslag is voor OZB en andere heffingen |
| Bronnen | VNG raadgever WOZ, Gegevenswoordenboek WOZ |

## GGM-bron

> **WOZ-deelobject**: Aanduiding van afzonderlijke elementen (delen van het object, bijzondere waarderelevante factoren) die voor de onderbouwing van de vastgestelde waarde van belang zijn.
> — *GGM v2.5.1, RSGBPlus (taakveld 99 Kern)*

**Entiteit:** WOZ-deelobject
**Attributen:** WOZDeelobjectNummer, codeWOZDeelobject, statusWOZDeelobject, datumBeginGeldigheidDeelobject, datumEindeGeldigheidDeelobject
**Herkomst:** Gegevenswoordenboek WOZ
**Matchsterkte:** exact — standaard-entiteit uit het WOZ-gegevensmodel.

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Onderdeel van | [[Wiki/Bedrijfsobjecten/99-kern/woz-object\|WOZ-object]] | WOZ-deelobject → WOZ-object | — |
| Bestaat uit pand | *(Pand)* | WOZ-deelobject → Pand | BAG-object, geen apart BO in dit domein |
| Bestaat uit adresseerbaar object | *(AdresseerbaarObject)* | WOZ-deelobject → AdresseerbaarObject | BAG-object |

## Bedrijfsprocessen

- **WOZ-taxatie**: taxateur splitst WOZ-object in deelobjecten voor waardebepaling
- **Bezwaarbehandeling WOZ**: deelobjecten onderbouwen de getaxeerde waarde

## Bedrijfsfuncties

- Waardering onroerende zaken

## Bronnen

- [[Wiki/Bronsamenvattingen/Belastingen/raadgever-woz]]
- [[Wiki/Bronsamenvattingen/Belastingen/onroerendezaakbelastingen]]
