---
type: element
naam: Medewerker
domein: [Dienstverlening]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Medewerker
ggm_guid: EAID_16EB3936_03CB_4854_9CD8_9F0911EEA51B
ggm_uml_type: Class
ggm_beleidsdomein: RGBZPlus
ggm_taakveld: "99 Kern"
ggm_diagram: [Referentiemodel Gemeentelijke Basisgegevens Zaken in schema, Betrokkene, Afspraken en Klantcontacten]
ggm_diagram_ids: [EAID_8AC9A512_0538_48f7_B25E_5BC65B17A147, EAID_0516C81B_D5F6_4b7a_AD98_82FD3B218A6B, EAID_282A4979_0BBC_4448_B71C_0CE64829083B]
ggm_definitie: "Een medewerker van de organisatie die zaken behandelt uit hoofde van zijn of haar functie binnen een ORGANISATORISCHE EENHEID."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: "GFO Zaken"
ggm_gemma_naam: Medewerker
ggm_gemma_guid: "6cc6afe6-e4c6-4e2b-a359-f278b23700db"
ggm_gemma_definitie: "Een medewerker van de organisatie die zaken behandelt uit hoofde van zijn of haar functie binnen een ORGANISATORISCHE EENHEID."
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-6cc6afe6-e4c6-4e2b-a359-f278b23700db"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Medewerker** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Actie** (detail) — Detailgegeven (weinig attributen)
  - **CROW-Melding** (detail) — Detailgegeven (weinig attributen)
  - **Inspectie** (detail) — Detailgegeven (weinig attributen)
  - **Kwaliteitscatalogus Openbare Ruimte** (detail) — Detailgegeven (weinig attributen)
  - **Melding** (detail) — Detailgegeven
  - **MeldingOngeval** (detail) — Detailgegeven (weinig attributen)
  - **Samensteller** (detail) — Detailgegeven (weinig attributen)
  - **Schouwronde** (detail) — Detailgegeven (geassocieerd met BO)
  - **Sector** (detail) — Detailgegeven (weinig attributen)
  - **Storing** (detail) — Detailgegeven (weinig attributen)
  - **Subsidie** (detail) — Detailgegeven
  - **Subsidieaanvraag** (detail) — Detailgegeven
  - **Subsidiebeschikking** (detail) — Detailgegeven
  - **Taak** (detail) — Detailgegeven (weinig attributen)
  - **Uitvoerende instantie** (detail) — Detailgegeven (geassocieerd met BO)
bo_definitie: "Een medewerker van de gemeentelijke organisatie die zaken behandelt uit hoofde van zijn of haar functie binnen een organisatorische eenheid."
bo_toelichting: ""
element_tegenhangers:
  - element: "[[Wiki/Actoren/medewerker|Medewerker (actor)]]"
    archimate_type: business-actor
    toelichting: "Dit bedrijfsobject legt de gegevens vast over de gelijknamige actor."
bo_via_kandidaten:
  - ggm_entiteit: "FormulierInhuur"
    ggm_guid: "EAID_B598FF22_CDD0_486f_B528_99421D0FA608"
    reden: "Het inhuurformulier betreft de in te huren persoon/medewerker."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak|Zaak]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een medewerker is afhandelend medewerker van zaken
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact|Klantcontact]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een medewerker voert klantcontacten
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid|Organisatorische eenheid]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een medewerker hoort bij een of meer organisatorische eenheden
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype|Zaaktype]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Een medewerker is verantwoordelijk voor zaaktypen
bedrijfsprocessen:
  - Zaakafhandeling
bedrijfsfuncties:
  - Dienstverlening
  - Zaakgericht werken
---

# Medewerker

De vastgelegde gegevens over de persoon binnen de gemeentelijke organisatie die zaken behandelt, klantcontacten voert en verantwoordelijk is voor zaaktypen. In het RGBZ is Medewerker een specialisatie van Betrokkene — iemand die een rol speelt bij een zaak.

De handelende kant van dit begrip is vastgelegd als actor [[Wiki/Actoren/medewerker|Medewerker (actor)]].

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Centrale actor in zaakgericht werken |
| Herkenbaar voor experts | ✅ | Elke gemeente kent het begrip medewerker als zaakbehandelaar |
| Eigen bestaan | ✅ | Heeft eigen identificatie, naam, functie, in-/uitdienstdatum |
| Meervoud | ✅ | Gemeenten hebben honderden tot duizenden medewerkers |
| Eigen levenscyclus | ✅ | In dienst → actief → uit dienst |
| Relaties | ✅ | Met Zaak, Klantcontact, OrganisatorischeEenheid, Zaaktype, en 20+ domeinrelaties |

## GGM-bron

> **Medewerker**: Een medewerker van de organisatie die zaken behandelt uit hoofde van zijn of haar functie binnen een ORGANISATORISCHE EENHEID.
> — *GGM v2.5.1, RGBZPlus (taakveld 99 Kern)*

**Entiteit:** Medewerker
**Matchsterkte:** exact
**Herkomst:** GFO Zaken → RGBZ 1.0 → GGM

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Toelichting |
|---|---|---|---|
| Behandelt | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaak\|Zaak]] | Zaak → Medewerker [0..*] | Afhandelend medewerker |
| Voert | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/klantcontact\|Klantcontact]] | Klantcontact → Medewerker [0..1] | Gevoerd door |
| Hoort bij | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/organisatorische-eenheid\|Organisatorische eenheid]] | Medewerker → OrgEenheid [0..*] | Organisatorische inbedding |
| Verantwoordelijk voor | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/zaaktype\|Zaaktype]] | Medewerker → Zaaktype [0..*] | Zaaktypeverantwoordelijkheid |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rgbz-informatiemodel]]
