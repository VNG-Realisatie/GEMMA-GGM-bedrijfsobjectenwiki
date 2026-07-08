---
type: bedrijfsobject
naam: VTH-zaak
onderwerp: [Omgevingswet]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: VTHzaak
ggm_guid: EAID_88AF7A2E_C508_464a_AD22_DD9B156D570D
ggm_uml_type: Class
ggm_beleidsdomein: "1 Veiligheid en Vergunningen"
ggm_taakveld: "1 Veiligheid en Vergunningen"
ggm_diagram: [Diagram Vergunningen en Meldingen, Verkamering en Woonoverlast]
ggm_diagram_ids: [EAID_BB52C835_0B2D_4164_AC9D_9D6EDBD7E267, EAID_B039478A_DAF7_458f_A7C7_E4744EC08DBF]
ggm_definitie: "Een VTHzaak is een zaak of dossier binnen de gemeentelijke administratie die betrekking heeft op vergunningverlening, toezicht en handhaving (VTH) van regels en voorschriften in de fysieke leefomgeving."
ggm_toelichting: "VTH staat voor Vergunningverlening, Toezicht en Handhaving, de samenhangende taken waarmee gemeenten (en bevoegde overheden) controleren of activiteiten voldoen aan wettelijke eisen, vergunningen verlenen en handhavend optreden."
ggm_synoniemen: ""
ggm_herkomst: ""

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
  Dit BO is de hernoeming van GGM-entiteit **VTHzaak**. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Activiteit Omgevingswet** (detail) — Detailgegeven
  - **Kosten** (detail) — Detailgegeven
  - **Leges_Grondslag** (detail) — Detailgegeven
  - **Producttype** (classificatie) — Typering/referentietabel
  - **SubProducttype** (classificatie) — Typering/referentietabel
bo_definitie: "Een VTHzaak is een zaak of dossier binnen de gemeentelijke administratie die betrekking heeft op vergunningverlening, toezicht en handhaving (VTH) van regels en voorschriften in de fysieke leefomgeving."
bo_toelichting: ''
bo_subtypes: []
bo_via_kandidaten:
  - ggm_entiteit: "Activiteit Omgevingswet"
    ggm_guid: "EAID_9547BC67_7488_4d9a_B651_2B69A62D789F"
    reden: "Gereguleerde activiteiten worden behandeld binnen een VTH-zaak (vergunningverlening, toezicht, handhaving)."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Inspectie]]"
    richting: naar-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "Een VTH-zaak heeft één of meer inspecties"
  - type: generalisatie
    bedrijfsobject: "[[Zaak]]"
    richting: van-dit-BO
    kardinaliteit: ""
    beschrijving: "VTH-zaak is een specialisatie van Zaak"
bedrijfsprocessen: [vergunningverlening, toezicht, handhaving, vooroverleg]
bedrijfsfuncties: [vergunningverlening, toezicht en handhaving]
---

## BO-criteria toetsing

1. **Identificeerbare instanties** — elke VTH-zaak heeft een eigen zaaknummer en dossier
2. **Eigen attributen** — bevoegd gezag, uitvoerende instantie, behandelaar, prioritering, teambehandelaar
3. **Levenscyclus** — doorloopt fasen van aanvraag/melding via behandeling naar afhandeling
4. **Meerdere processen** — wordt gebruikt bij vergunningverlening, toezicht op realisatie, toezicht op bestaande bouw en handhaving
5. **Relevant op bedrijfsniveau** — centraal dossier waarover wordt gerapporteerd in VTH-jaarplannen en dat de verantwoordingscyclus draagt
6. **Gemeentelijk perspectief** — de gemeente beheert VTH-zaken als kerntaak onder de Omgevingswet

## Beschrijving

Een VTH-zaak is het centrale dossier waarin de gemeente alle activiteiten rondom vergunningverlening, toezicht en handhaving in de fysieke leefomgeving bundelt. Het dossier verbindt de aanvraag of melding met de inspecties, bevindingen, kosten en eventuele vorderingen die daaruit voortkomen. De zaak wordt geprioriteerd op basis van risico-inschatting en de categorisering van taken (wettelijke kerntaken, risicogerichte taken, bovenwettelijke aandachtsgebieden).

> "Het Uitvoeringsbeleid VTH beschrijft hoe de gemeente Delft haar gemeentelijke taken op het gebied van vergunningverlening, toezicht en handhaving in de fysieke leefomgeving uitvoert." (bron: Uitvoeringsbeleid VTH Delft §1)

## GGM-bron

> Een VTHzaak is een zaak of dossier binnen de gemeentelijke administratie die betrekking heeft op vergunningverlening, toezicht en handhaving (VTH) van regels en voorschriften in de fysieke leefomgeving.

- **Entiteit:** VTHzaak
- **Beleidsdomein:** 1 Veiligheid en Vergunningen
- **Attributen:** verkamering, bevoegdGezag, uitvoerendeInstantie, behandelaar, prioritering, teamBehandelaar
- **Matchsterkte:** exact — definitie en scope komen overeen

## Relaties

| Relatie | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/inspectie\|Inspectie]] | naar-dit-BO | 1..* | Een VTH-zaak heeft één of meer inspecties | GGM |
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/aanvraag-of-melding\|Aanvraag of melding]] | naar-dit-BO | 0..* | Een aanvraag of melding kan leiden tot een VTH-zaak | beleidsbron |
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/handhavingsbesluit\|Handhavingsbesluit]] | van-dit-BO | 0..* | Een VTH-zaak kan leiden tot een handhavingsbesluit | beleidsbron |

## Bedrijfsprocessen

- Vergunningverlening (behandeling aanvraag omgevingsvergunning)
- Toezicht op realisatie (controle op vergunde plannen)
- Toezicht op bestaande bouw (signaaltoezicht, steekproeven)
- Handhaving (sanctionering bij overtredingen)
- Vooroverleg (verkenning initiatieven)

## Bronnen
- [[Wiki/Bronsamenvattingen/Omgevingswet/uitvoeringsbeleid-vth-delft]]
