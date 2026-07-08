---
type: element
naam: Klantcontact
domein: [Dienstverlening]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Klantcontact
ggm_guid: EAID_A3DAD553_0E55_4256_824B_CDB5E12CB545
ggm_uml_type: Class
ggm_beleidsdomein: RGBZPlus
ggm_taakveld: "99 Kern"
ggm_diagram: [Afspraken en Klantcontacten, Entiteiten Dienstverlening, Kern:Klantcontact]
ggm_diagram_ids: [EAID_282A4979_0BBC_4448_B71C_0CE64829083B, EAID_48B6C3F9_CCF1_4794_8252_FC6543409B78, EAID_4F55A673_8DCE_448b_BFAB_1BE924283AB1]
ggm_definitie: "Klantcontacten zijn contactmomenten die werkelijk hebben plaatsgevonden, terwijl Balieafspraken afspraken zijn voor een klantcontact."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "GGM"
ggm_gemma_naam: Klantcontact
ggm_gemma_guid: "a9cb919f-a224-4ab5-9825-40d54104f90d"
ggm_gemma_definitie: "Klantcontacten zijn contactmomenten die werkelijk hebben plaatsgevonden, terwijl Balieafspraken afspraken zijn voor een klantcontact."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-a9cb919f-a224-4ab5-9825-40d54104f90d"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Klantcontact** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Telefoononderwerp** (detail) — Detailgegeven (geassocieerd met BO)
  - **Telefoonstatus** (detail) — Detailgegeven (weinig attributen)
  - **Telefoontje** (detail) — Detailgegeven
  - **VestigingVanZaakbehandelendeOrganisatie** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Contactmoment dat werkelijk heeft plaatsgevonden tussen een burger of bedrijf en de gemeente, via balie, telefoon, e-mail of ander kanaal."
bo_toelichting: ""
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Een klantcontact kan betrekking hebben op een zaak
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker|Medewerker]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Een klantcontact is gevoerd door een medewerker
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding|Aanvraag of melding]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een klantcontact kan leiden tot een aanvraag of melding
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/product-of-dienst|Product of dienst]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een klantcontact kan betrekking hebben op producten of diensten
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak|Balieafspraak]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Een balieafspraak mondt uit in een klantcontact
bedrijfsprocessen:
  - Klantcontactregistratie
  - Dienstverleningsproces
bedrijfsfuncties:
  - Dienstverlening
  - Klantinteractie
---

# Klantcontact

Contactmoment dat werkelijk heeft plaatsgevonden tussen een burger of bedrijf en de gemeente. Onderscheidt zich van [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak|Balieafspraak]]: een balieafspraak is gepland, een klantcontact is gerealiseerd. Kanalen: balie, telefoon, e-mail, chat, post.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Basisregistratie van alle inwoner-/bedrijfsinteracties |
| Herkenbaar voor experts | ✅ | Standaardbegrip in gemeentelijke dienstverlening |
| Eigen bestaan | ✅ | Heeft eigen starttijd, kanaal, notitie; bestaat ook zonder zaak |
| Meervoud | ✅ | Gemeenten registreren dagelijks honderden klantcontacten |
| Eigen levenscyclus | ✅ | Start → registratie → eventueel koppeling aan zaak |
| Relaties | ✅ | Met Zaak, Medewerker, Balieafspraak, AanvraagOfMelding, ProductOfDienst |

## GGM-bron

> **Klantcontact**: Klantcontacten zijn contactmomenten die werkelijk hebben plaatsgevonden, terwijl Balieafspraken afspraken zijn voor een klantcontact.
> — *GGM v2.5.1, RGBZPlus (taakveld 99 Kern)*

**Entiteit:** Klantcontact
**Matchsterkte:** exact
**Herkomst:** GGM (uitbreiding op RGBZ)

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Toelichting |
|---|---|---|---|
| Heeft betrekking op | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Klantcontact → Zaak [0..1] | Optionele koppeling aan lopende zaak |
| Gevoerd door | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/medewerker\|Medewerker]] | Klantcontact → Medewerker [0..1] | De medewerker die het contact voerde |
| Kan leiden tot | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | Klantcontact → AanvraagOfMelding [0..*] | Contactmoment leidt tot formele aanvraag |
| Voortgekomen uit | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/balieafspraak\|Balieafspraak]] | Balieafspraak → Klantcontact [0..1] | Geplande afspraak gerealiseerd als klantcontact |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]]
