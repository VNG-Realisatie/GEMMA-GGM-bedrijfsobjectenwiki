---
type: bedrijfsobject
naam: Zaaktype
domein: [Dienstverlening]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Zaaktype
ggm_guid: EAID_7210A379_17EE_4143_A106_ECD9414B2A0D
ggm_uml_type: Class
ggm_beleidsdomein: RGBZPlus
ggm_taakveld: "99 Kern"
ggm_diagram: [Bedrijfsprocessen, Entiteiten Dienstverlening, Referentiemodel Gemeentelijke Basisgegevens Zaken in schema]
ggm_diagram_ids: [EAID_63323A39_82A4_4607_8A45_E4CBD1D800B0, EAID_48B6C3F9_CCF1_4794_8252_FC6543409B78, EAID_8AC9A512_0538_48f7_B25E_5BC65B17A147]
ggm_definitie: "Generieke aanduiding van de aard van een zaak."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "GFO Zaken"
ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Zaaktype** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Statustype** (detail) — Attribuut/modelleringskeuze, geen zelfstandig BO
bo_definitie: "Definitie van een soort zaak met kenmerken als doorlooptijd, servicenorm, archiefcode en verantwoordelijke organisatorische eenheid."
bo_toelichting: "Zaaktypen worden centraal en door gemeenten gedefinieerd. Zaaktypecatalogi bundelen zaaktypen voor gebruik in zaaksystemen."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Zaken zijn van een zaaktype
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker|Medewerker]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Een medewerker is verantwoordelijk voor zaaktypen
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid|Organisatorische eenheid]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Een organisatorische eenheid is verantwoordelijk voor zaaktypen
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/bedrijfsproces|Bedrijfsproces]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: Een bedrijfsprocestype hoort bij een zaaktype
bedrijfsprocessen:
  - Zaaktypebeheer
bedrijfsfuncties:
  - Dienstverlening
  - Zaakgericht werken
---

# Zaaktype

Definitie van een soort zaak: welke doorlooptijd geldt, welke servicenorm, welk archiefregime, welke statussen doorlopen worden en wie verantwoordelijk is. Zaaktypen worden zowel centraal (VNG, landelijke zaaktypecatalogus) als door individuele gemeenten gedefinieerd. Ze vormen de configuratielaag voor zaakgericht werken.

Onderscheid met [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]]: een zaaktype is de *definitie*, een zaak is een *instantie*. Onderscheid met zaaktypecatalogus: de catalogus is de *bundel*, het zaaktype is het *individuele type* daarin.

Per zaaktype worden ~300 attribuut- en relatiesoorten gespecificeerd: doorlooptijden, mogelijke statussen, documenttypen, besluittypen, resultaattypen, roltypen, eigenschappen en zaakobjecttypen. Zaaktypen worden zowel centraal (VNG referentiezaaktypen) als door gemeenten en sectoren gedefinieerd.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Bepaalt hoe zaken worden afgehandeld — de configuratie achter zaakgericht werken |
| Herkenbaar voor experts | ✅ | Elke zaakbehandelaar kent zaaktypen; ze sturen de inrichting van zaaksystemen |
| Eigen bestaan | ✅ | Heeft eigen omschrijving, doorlooptijd, servicenorm, geldigheidsperiode |
| Meervoud | ✅ | Gemeenten hebben honderden zaaktypen |
| Eigen levenscyclus | ✅ | Gedefinieerd → geldig → verlopen (begin/einddatum geldigheid) |
| Relaties | ✅ | Met Zaak, Medewerker, OrgEenheid, Statustype, Bedrijfsprocestype, Producttype |

## GGM-bron

> **Zaaktype**: Generieke aanduiding van de aard van een zaak.
> — *GGM v2.5.1, RGBZPlus (taakveld 99 Kern)*

**Entiteit:** Zaaktype
**Matchsterkte:** exact
**Herkomst:** GFO Zaken → RGBZ 1.0 → GGM

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Toelichting |
|---|---|---|---|
| Instanties | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Zaak → Zaaktype [1] | Elke zaak is van een zaaktype |
| Verantwoordelijke | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker\|Medewerker]] | Medewerker → Zaaktype [0..*] | Verantwoordelijk medewerker |
| Verantwoordelijke | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid\|Organisatorische eenheid]] | OrgEenheid → Zaaktype [0..*] | Verantwoordelijke afdeling |
| Procestype | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/bedrijfsproces\|Bedrijfsproces]] | Bedrijfsprocestype → Zaaktype [1..*] | Welk proces bij dit zaaktype hoort |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]]
- [[Wiki/Bronsamenvattingen/Standaarden/ztc2-informatiemodel]]
