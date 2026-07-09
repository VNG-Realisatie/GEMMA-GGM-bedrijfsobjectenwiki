---
type: element
naam: Besluit
onderwerp: [Dienstverlening]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Besluit
ggm_guid: EAID_AFB100D2_8C68_4488_8949_13E945D15920
ggm_uml_type: Class
ggm_beleidsdomein: RGBZPlus
ggm_taakveld: "99 Kern"
ggm_diagram: [Diagram Aanvragen, Zaken en Besluiten, Referentiemodel Gemeentelijke Basisgegevens Zaken in schema]
ggm_diagram_ids: [EAID_A2BA1F0D_8428_42fc_80D6_7184F243D268, EAID_8AC9A512_0538_48f7_B25E_5BC65B17A147]
ggm_definitie: "Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst: "GFO Zaken"
ggm_gemma_naam: Besluit
ggm_gemma_guid: "10d36920-683f-4cb4-84bf-b00ac045674f"
ggm_gemma_definitie: "Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval."
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-10d36920-683f-4cb4-84bf-b00ac045674f"
ggm_gemma_bron:
ggm_gemma_alternate_name:
ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Besluit** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Besluittype** (detail) — Typering bij Besluit — waardelijst
bo_definitie: "Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval."
bo_toelichting:
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: Een besluit is uitkomst van een zaak
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document|Document]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een besluit is vastgelegd in een of meer documenten
bedrijfsprocessen:
  - Zaakafhandeling
  - Beschikkingsproces
bedrijfsfuncties:
  - Dienstverlening
  - Besluitvorming
---

# Besluit

Formele beslissing van de gemeente op een individueel geval, genomen binnen de context van een zaak. Voorbeelden: vergunningbesluit, toekenning uitkering, bezwaarbesluit, handhavingsbesluit. Het besluit heeft een eigen levenscyclus (genomen, gepubliceerd, verzonden, eventueel vervallen) en is vastgelegd in een of meer documenten.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Kernobject in zaakgericht werken; elke zaak kan leiden tot een of meer besluiten |
| Herkenbaar voor experts | ✅ | Juridisch en bestuurlijk begrip, herkenbaar voor elke gemeenteambtenaar |
| Eigen bestaan | ✅ | Heeft eigen identificatie, datum, toelichting; bestaat onafhankelijk na afronding zaak |
| Meervoud | ✅ | Gemeenten nemen jaarlijks tienduizenden besluiten |
| Eigen levenscyclus | ✅ | Genomen → gepubliceerd → verzonden → eventueel vervallen |
| Relaties | ✅ | Met Zaak, Document, Besluittype |

## GGM-bron

> **Besluit**: Een na overweging of beraadslaging vastgestelde beslissing voor een individueel of concreet geval.
> — *GGM v2.5.1, RGBZPlus (taakveld 99 Kern)*

**Entiteit:** Besluit
**Matchsterkte:** exact
**Herkomst:** GFO Zaken → RGBZ 1.0 → GGM

## GGM-componenten

**Besluittype** — generieke aanduiding van de aard van een besluit. Configuratie-entiteit per zaaktype.

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Toelichting |
|---|---|---|---|
| Is uitkomst van | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Besluit → Zaak [1] | Het zaakproces waaruit het besluit voortkomt |
| Vastgelegd in | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | Besluit → Document [0..*] | De documenten waarin het besluit beschreven is |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]]
