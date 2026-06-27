---
type: bedrijfsobject
naam: Organisatorische eenheid
domein: [Dienstverlening]
archimate_type: business-actor
grondslag: ggm-entiteit
ggm_entiteit: OrganisatorischeEenheid
ggm_guid: EAID_936A4E8B_3E5A_44b6_8A5D_EFB39F83FB6D
ggm_uml_type: Class
ggm_beleidsdomein: RGBZPlus
ggm_taakveld: "99 Kern"
ggm_diagram: [Referentiemodel Gemeentelijke Basisgegevens Zaken in schema, Betrokkene]
ggm_diagram_ids: [EAID_8AC9A512_0538_48f7_B25E_5BC65B17A147, EAID_0516C81B_D5F6_4b7a_AD98_82FD3B218A6B]
ggm_definitie: "Het deel van een functioneel afgebakend onderdeel binnen de organisatie dat haar activiteiten uitvoert binnen een VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE en die verantwoordelijk is voor de behandeling van zaken."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "GFO Zaken"
ggm_gemma_naam: OrganisatorischeEenheid
ggm_gemma_guid: "02f66265-00ae-418d-8d0e-dcbaf36652bb"
ggm_gemma_definitie: "Het deel van een functioneel afgebakend onderdeel binnen de organisatie dat haar activiteiten uitvoert binnen een VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE en die verantwoordelijk is voor de behandeling van zaken."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-02f66265-00ae-418d-8d0e-dcbaf36652bb"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
ggm_duplicaat_entiteiten: []
bo_definitie: "Functioneel afgebakend onderdeel binnen de gemeentelijke organisatie dat verantwoordelijk is voor de behandeling van zaken."
bo_toelichting: ""
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker|Medewerker]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een organisatorische eenheid bevat medewerkers
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype|Zaaktype]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een organisatorische eenheid is verantwoordelijk voor zaaktypen
  - type: associatie
    bedrijfsobject: "Organisatorische eenheid"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Een organisatorische eenheid is deel van een andere organisatorische eenheid
bedrijfsprocessen:
  - Organisatiebeheer
bedrijfsfuncties:
  - Dienstverlening
  - Bedrijfsvoering
---

# Organisatorische eenheid

Actor in het zaakgericht werken: het functioneel afgebakende onderdeel van de gemeente dat verantwoordelijk is voor de behandeling van bepaalde zaaktypen. Voorbeelden: afdeling Vergunningen, team Burgerzaken, cluster Sociaal Domein. Organisatorische eenheden vormen een hiërarchie (is deel van) en bevatten medewerkers.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Bepaalt wie verantwoordelijk is voor welke zaken |
| Herkenbaar voor experts | ✅ | Elke gemeente is ingericht in organisatorische eenheden |
| Eigen bestaan | ✅ | Heeft eigen identificatie, naam, ontstaans-/opheffingsdatum |
| Meervoud | ✅ | Gemeenten hebben tientallen tot honderden eenheden |
| Eigen levenscyclus | ✅ | Opgericht → actief → gereorganiseerd → opgeheven |
| Relaties | ✅ | Met Medewerker, Zaaktype, Vestiging, zichzelf (hiërarchie) |

## GGM-bron

> **OrganisatorischeEenheid**: Het deel van een functioneel afgebakend onderdeel binnen de organisatie dat haar activiteiten uitvoert binnen een VESTIGING VAN ZAAKBEHANDELENDE ORGANISATIE en die verantwoordelijk is voor de behandeling van zaken.
> — *GGM v2.5.1, RGBZPlus (taakveld 99 Kern)*

**Entiteit:** OrganisatorischeEenheid
**Matchsterkte:** exact
**Herkomst:** GFO Zaken → RGBZ 1.0 → GGM

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Toelichting |
|---|---|---|---|
| Bevat | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker\|Medewerker]] | Medewerker → OrgEenheid [0..*] | Medewerkers binnen deze eenheid |
| Verantwoordelijk voor | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]] | OrgEenheid → Zaaktype [0..*] | Welke zaaktypen deze eenheid behandelt |
| Is deel van | Organisatorische eenheid | OrgEenheid → OrgEenheid [0..1] | Hiërarchie van eenheden |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]]
