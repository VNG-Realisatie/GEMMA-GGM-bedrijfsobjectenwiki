---
type: element
naam: Bedrijfsproces
domein: [Dienstverlening]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Bedrijfsproces
ggm_guid: EAID_EDB5D3CD_CE4D_4317_81C6_C01CC7325148
ggm_uml_type: Class
ggm_beleidsdomein: RGBZPlus
ggm_taakveld: "99 Kern"
ggm_diagram: [Bedrijfsprocessen]
ggm_diagram_ids: [EAID_63323A39_82A4_4607_8A45_E4CBD1D800B0]
ggm_definitie: "Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een product of dienst."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "GGM"
ggm_gemma_naam: Bedrijfsproces
ggm_gemma_guid: "7e054df1-48a3-46c3-91a5-5ce10e326f9b"
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-7e054df1-48a3-46c3-91a5-5ce10e326f9b"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Bedrijfsproces** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Bedrijfsprocestype** (classificatie) — Typering/referentietabel
  - **Deelproces** (onderdeel) — Onderdeel (naamindicatie)
  - **Deelprocestype** (classificatie) — Typering/referentietabel
bo_definitie: "Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een product of dienst."
bo_toelichting: ""
bo_via_kandidaten:
  - ggm_entiteit: "Bedrijfsprocestype"
    ggm_guid: "EAID_14E4AF23_21E9_412a_B78D_C208EE9F419D"
    reden: "Soort Bedrijfsproces — expliciet in de GGM-definitie."
  - ggm_entiteit: "Deelprocestype"
    ggm_guid: "EAID_710A1D2B_3C7B_41cf_A947_727186C40A98"
    reden: "Soort Deelproces, een specialisatie van Bedrijfsproces."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: Een bedrijfsproces wordt uitgevoerd binnen een of meer zaken
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype|Zaaktype]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: Een bedrijfsprocestype hoort bij een zaaktype
bedrijfsprocessen:
  - Procesmanagement
bedrijfsfuncties:
  - Dienstverlening
  - Bedrijfsvoering
---

# Bedrijfsproces

Geregistreerde uitvoering van een reeks activiteiten die leidt tot de levering van een product of dienst. Wordt uitgevoerd binnen de context van een zaak. Kan bestaan uit deelprocessen. GGM-uitbreiding op het RGBZ.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Procesregistratie is basis voor sturing en verantwoording |
| Herkenbaar voor experts | ✅ | Standaardbegrip in bedrijfsvoering |
| Eigen bestaan | ✅ | Heeft eigen naam, omschrijving, start/einddatum, status |
| Meervoud | ✅ | Elke zaakafhandeling is een procesinstantie |
| Eigen levenscyclus | ✅ | Gestart → lopend → afgerond |
| Relaties | ✅ | Met Zaak, Bedrijfsprocestype, Deelproces |

## GGM-bron

> **Bedrijfsproces**: Reeks opeenvolgend uit te voeren activiteiten die bijdraagt aan een specifiek resultaat, zoals de levering van een product of dienst.
> — *GGM v2.5.1, RGBZPlus (taakveld 99 Kern)*

**Entiteit:** Bedrijfsproces
**Matchsterkte:** exact
**Herkomst:** GGM (uitbreiding op RGBZ)

## GGM-componenten

**Deelproces** — geordende reeks processtappen binnen één organisatorische eenheid. Onderdeel van een bedrijfsproces.

**Bedrijfsprocestype** — typering van het bedrijfsproces. Configuratie-entiteit gekoppeld aan zaaktype.

**Deelprocestype** — typering van een deelproces.

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Toelichting |
|---|---|---|---|
| Uitgevoerd binnen | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Bedrijfsproces → Zaak [1..*] | De zaak waarin het proces draait |
| Hoort bij | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]] | Bedrijfsprocestype → Zaaktype [1..*] | Via het procestype |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]]
