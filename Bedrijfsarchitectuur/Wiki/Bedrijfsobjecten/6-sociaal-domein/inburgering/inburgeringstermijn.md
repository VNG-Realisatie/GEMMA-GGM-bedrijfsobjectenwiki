---
type: element
naam: Inburgeringstermijn
domein:
- Asiel en Integratie
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Inburgeringstermijn
ggm_guid: EAID_E07490AD_C5DE_4665_8540_92B19656A027
ggm_uml_type: Class
ggm_beleidsdomein: Inburgering
ggm_taakveld: 6 Sociaal Domein
ggm_diagram:
- Inburgering
ggm_diagram_ids:
- EAID_96927C60_9F7B_4e67_806A_02EE0191983D
ggm_definitie: <font color="#0e0e0e">De </font><font color="#0e0e0e"><b>Inburgeringstermijn</b></font><font color="#0e0e0e"> is de wettelijke periode waarbinnen een inburgeringsplichtige moet voldoen aan
  de inburgeringsplicht, gerekend vanaf de startdatum van de verplichting zoals vastgesteld door DUO of de gemeente.</font>
ggm_toelichting: ''
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: ''
ggm_gemma_guid: ''
ggm_gemma_definitie: ''
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: ''
ggm_gemma_url: ''
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Inburgeringstermijn** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Aanvraag verlenging Inburgeringstermijn** (detail) — Detailgegeven (geassocieerd met BO)
  - **Verlengingsgrond** (detail) — Component van Inburgeringstermijn
bo_definitie: "De Inburgeringstermijn is de wettelijke periode waarbinnen een inburgeringsplichtige moet voldoen aan de inburgeringsplicht, gerekend vanaf de startdatum van de verplichting zoals vastgesteld door DUO of de gemeente."
bo_toelichting: ''
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht|Inburgeringsplicht]]'
  richting: naar-dit-BO
  kardinaliteit: 1
  beschrijving: Inburgeringsplicht heeft een termijn
---

# Inburgeringstermijn

De wettelijke periode waarbinnen een inburgeringsplichtige moet voldoen aan de inburgeringsplicht, inclusief eventuele verlengingen en boetebevoegdheid.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein
- ✅ Is herkenbaar voor domeinexperts
- ✅ Heeft een eigen bestaan binnen het domein
- ✅ Kan in meervoud bestaan
- ✅ Heeft een eigen levenscyclus
- ✅ Heeft relaties met andere concepten

Aanvraag verlenging is een processtap, geen apart bedrijfsobject. Het GGM modelleert "Aanvraag verlenging Inburgeringstermijn" als aparte entiteit, maar op bedrijfsniveau is het een gebeurtenis in de levenscyclus van de inburgeringstermijn.

## GGM-bron

> De Inburgeringstermijn is de wettelijke periode waarbinnen een inburgeringsplichtige moet voldoen aan de inburgeringsplicht, gerekend vanaf de startdatum van de verplichting zoals vastgesteld door DUO of de gemeente.

- **Entiteit:** Inburgeringstermijn
- **Beleidsdomein:** Inburgering (taakveld 6 — Sociaal Domein)
- **Attributen:** DatumAanvangInburgeringstermijn, DatumEindeInburgeringstermijn, VooraankondigingBoete, BoeteBedrag, DatumBoete
- **Matchsterkte:** exact

## Relaties

- ← [[Wiki/Bedrijfsobjecten/6-sociaal-domein/inburgering/inburgeringsplicht|inburgeringsplicht]] — inburgeringsplicht heeft een termijn [1]

## Bronnen

- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/asielopvangwijzer]]
- [[Wiki/Bronsamenvattingen/Inburgering en Asielopvang/coa-dienstverleningsgids]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-asielopvang]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-inburgering]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-opvang-oekraine]]
- [[Wiki/Bronsamenvattingen/Asiel en Integratie/vng-rubriek-asiel]]
