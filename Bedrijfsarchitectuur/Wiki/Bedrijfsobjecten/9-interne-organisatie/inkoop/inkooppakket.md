---
type: bedrijfsobject
naam: Inkooppakket
onderwerp: [inkoop]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Inkooppakket
ggm_guid: EAID_170AF8F5_8952_407a_91C4_EAF910DE3304
ggm_uml_type: Class
ggm_beleidsdomein: Inkoop
ggm_taakveld: "9 Interne Organisatie"
ggm_diagram: [Diagram Inkoop Geen Inhuur]
ggm_diagram_ids: [EAID_6683520C_EE21_4038_A418_D4C957172DF2]
ggm_definitie: "Standaard indeling om de werken, diensten en leveringen die de aanbestedende dienst helpt bij het structureren van haar uitgaven. Samenhangende leveringen, diensten en producten zijn hierin gegroepeerd."
ggm_toelichting: ""
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

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Inkooppakket** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **CPV-code** (detail) — EU-referentietabel, geen gemeentelijk object
bo_definitie: "Standaard indeling om de werken, diensten en leveringen die de aanbestedende dienst helpt bij het structureren van haar uitgaven. Samenhangende leveringen, diensten en producten zijn hierin gegroepeerd."
bo_toelichting: ''
bo_via_kandidaten:
  - ggm_entiteit: "CPV-code"
    ggm_guid: "EAID_6A4CF470_3B0E_4141_9DB6_C9E8A525CB49"
    reden: "CPV-codes classificeren inkooppakketten, net als Inkooppakket zelf een structurerings-/classificatieschema is."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Aanbesteding]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "structureert"
bedrijfsprocessen: [Inkopen]
bedrijfsfuncties: [Inkoopfunctie]
---

## BO-criteria toetsing

1. **Heeft betekenis binnen het onderwerp** — ja, structureert de gemeentelijke uitgaven
2. **Is herkenbaar voor domeinexperts** — ja, inkopers werken met pakketindelingen
3. **Heeft een eigen bestaan** — ja, pakket bestaat onafhankelijk van specifieke aanbestedingen
4. **Kan in meervoud bestaan** — ja, gemeente heeft tientallen inkooppakketten
5. **Heeft een eigen levenscyclus** — beperkt: wordt aangemaakt en onderhouden, maar verandert weinig
6. **Heeft relaties met andere concepten** — ja: Aanbesteding, CPV-code

Score: 5/6

## Beschrijving

Een inkooppakket is een categorisering waarmee de gemeente haar inkopen groepeert in samenhangende eenheden. Het helpt bij het structureren van uitgaven, het plannen van aanbestedingen en het bepalen van opdrachtwaarden (aggregatie voor drempelbedragen). Inkooppakketten zijn gekoppeld aan CPV-codes (EU-classificatiesysteem).

## GGM-bron

> "Standaard indeling om de werken, diensten en leveringen die de aanbestedende dienst helpt bij het structureren van haar uitgaven. Samenhangende leveringen, diensten en producten zijn hierin gegroepeerd." (GGM, beleidsdomein Inkoop)

**Matchsterkte:** exact — GGM-entiteit en BO zijn hetzelfde concept.

**Attributen:** code, naam, type

## Relaties

| Gerelateerd BO | Relatie | Richting | Kardinaliteit | Bron |
|---|---|---|---|---|
| [[Aanbesteding\|Aanbesteding]] | structureert | → | 0..* | GGM |

## Bedrijfsprocessen

- **Inkopen** — categorisering en planning van aanbestedingen

## Bedrijfsfuncties

- **Inkoopfunctie** — beheer inkooppakketindeling

## Bronnen

- [[Wiki/Bronsamenvattingen/Inkoop/inkoop-en-aanbestedingsbeleid]]
