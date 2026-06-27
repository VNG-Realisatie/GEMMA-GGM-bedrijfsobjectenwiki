---
type: bedrijfsobject
naam: Betaling
domein: [Dienstverlening]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Betaling
ggm_guid: EAID_FC488929_8721_402f_A073_1DFDB76A816E
ggm_uml_type: Class
ggm_beleidsdomein: RGBZPlus
ggm_taakveld: "99 Kern"
ggm_diagram: [Entiteiten Dienstverlening, Financien Verwerken Mutaties]
ggm_diagram_ids: [EAID_48B6C3F9_CCF1_4794_8252_FC6543409B78, EAID_B758018F_CB22_420e_B4E4_E17EB5F71EDA]
ggm_definitie: "Het onderhandigen of overboeken van geld in ruil voor goed of dienst."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "GGM"
ggm_gemma_naam: Betaling
ggm_gemma_guid: "8cec89b8-6174-42ac-937f-9500bfb8901b"
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-8cec89b8-6174-42ac-937f-9500bfb8901b"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
ggm_duplicaat_entiteiten: []
bo_definitie: "Het overboeken of ontvangen van geld in het kader van een zaak — leges, heffingen of andere betalingen gerelateerd aan gemeentelijke dienstverlening."
bo_toelichting: ""
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Een betaling hoort bij een zaak
bedrijfsprocessen:
  - Financiële afhandeling
  - Zaakafhandeling
bedrijfsfuncties:
  - Dienstverlening
  - Financieel beheer
---

# Betaling

Financiële transactie gekoppeld aan een zaak. Dekt zowel betalingen van de burger aan de gemeente (leges, heffingen) als betalingen van de gemeente aan de burger (uitkeringen, subsidies). GGM-uitbreiding op het RGBZ.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Financiële afwikkeling is onderdeel van veel gemeentelijke processen |
| Herkenbaar voor experts | ✅ | Standaardbegrip in financiële administratie |
| Eigen bestaan | ✅ | Heeft eigen bedrag, datum, valuta, omschrijving |
| Meervoud | ✅ | Duizenden betalingen per dag |
| Eigen levenscyclus | ✅ | Aangemaakt → verwerkt → geboekt |
| Relaties | ✅ | Met Zaak, Bankafschriftregel, Bankrekening |

## GGM-bron

> **Betaling**: Het onderhandigen of overboeken van geld in ruil voor goed of dienst.
> — *GGM v2.5.1, RGBZPlus (taakveld 99 Kern)*

**Entiteit:** Betaling
**Matchsterkte:** exact
**Herkomst:** GGM (uitbreiding op RGBZ)

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Toelichting |
|---|---|---|---|
| Hoort bij | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Zaak → Betaling [0..*] | Financiële afwikkeling van de zaak |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]]
