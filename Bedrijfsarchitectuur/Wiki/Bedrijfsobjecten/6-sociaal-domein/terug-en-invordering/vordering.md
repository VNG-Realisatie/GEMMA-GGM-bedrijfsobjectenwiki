---
type: element
naam: Vordering
onderwerp: [Terug-en-invordering]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Vordering"
ggm_guid: EAID_14116EEA_C461_0DB2_97AB_263C0A4777FC
ggm_uml_type: Class
ggm_beleidsdomein: "Terug- en invordering"
ggm_taakveld: "Inkomen"
ggm_diagram: [Diagram Terug- en invordering]
ggm_diagram_ids: [EAID_CE436DEE_AB15_4f23_B191_FA8A63FB488D]
ggm_definitie: "Een vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag (terug) moet betalen aan de gemeente in het kader van de bijstand of een bijstandsgerelateerde uitkering.De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling.Vorderingen kunnen uit meerdere componenten bestaan.Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: Een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering.Deze type vordering zijn als verbijzonderingen opgenomen, opdat deze relaties expliciet kunnen worden vastgelegd."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:
ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten:
  - entiteit: Vordering
    guid: EAID_341942C1_0F72_4e13_ADD1_235805BB81C0
    beleidsdomein: "1 Veiligheid en Vergunningen"
    taakveld: "1 Veiligheid en Vergunningen"
    afwijkende_attributen:

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Vordering** als directe tegenhanger. Daarnaast is **Vordering** (beleidsdomein 1 Veiligheid en Vergunningen) als vermoedelijk duplicaat gekoppeld — zie ggm_duplicaat_entiteiten. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Betaalcomponent** (onderdeel) — Onderdeel van Vordering
  - **Boetevordering** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Conservatoir beslag** (onderdeel) — Onderdeel van Vordering
  - **Correctie** (onderdeel) — Onderdeel van Vordering
  - **Incassokostenvordering** (detail) — Detailgegeven (geassocieerd met BO)
  - **Rechtmaand** (onderdeel) — Onderdeel van Vordering
  - **Rentevordering** (detail) — Detailgegeven (geassocieerd met BO)
  - **Terugvorderingsverzoek** (detail) — Detailgegeven
  - **Vermindering terugvordering** (onderdeel) — Onderdeel van Vordering
  - **Verrekening** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Verwijtbare vordering** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Vorderingregel** (onderdeel) — Onderdeel (naamindicatie)
  - **Vorderingscomponent** (onderdeel) — Onderdeel van Vordering
bo_definitie: "Een vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag (terug) moet betalen aan de gemeente in het kader van de bijstand of een bijstandsgerelateerde uitkering."
bo_toelichting: "De oorzaak van een vordering is velerlei, zie daarvoor de categorie-indeling. Vorderingen kunnen uit meerdere componenten bestaan. Vorderingen kunnen ook onderling in relatie staan, bijvoorbeeld: een opgelegde boete wegens het schenden van de inlichtingenplicht heeft een relatie met een verwijtbare vordering."
definitie: Een eis op een persoon die een zeker bedrag (terug) moet betalen aan de gemeente
bedrijfsprocessen: [Terugvordering, Invordering]
bedrijfsfuncties: [Inning en invordering]
status: concept
---

# Vordering

Een eis op een persoon (debiteur) die een zeker bedrag (terug) moet betalen aan de gemeente. Kernobject van het invorderingsproces.

## GGM-bron

> Een vordering is een eis op een persoon, zeg debiteur, die een zeker bedrag (terug) moet betalen aan de gemeente in het kader van de bijstand of een bijstandsgerelateerde uitkering. De oorzaak van een vordering is velerlei, Zie daarvoor de categorie-indeling. Vorderingen kunnen uit meerdere componenten bestaan. Vorderingen kunnen ook onderling in relatie staan.

- **Entiteit:** Vordering
- **Beleidsdomein:** Terug-en-invordering (taakveld 6 — Sociaal Domein → Inkomen)
- **Attributen:** Categorie, Fiscaal, Periode einddatum, Periode startdatum, Priotype, Regeling, Stuitingsvoortgangsindicator, Subcategorie, Titel, Vaststeldatum terugvordering, Verjaringsdatum, Verwerkingsstatus

**Specialisaties in GGM (niet als apart bedrijfsobject):** Boetevordering, Incassokostenvordering, Rentevordering, Verwijtbare vordering, Krediethypotheekvordering, Leenbijstandvordering.

## Bo-definitie (afwijkend)

De GGM-definitie beperkt zich tot bijstand; de bedrijfsobjectdefinitie is breder: "Een eis op een persoon die een zeker bedrag (terug) moet betalen aan de gemeente" — dekt ook belastingvorderingen en overige vorderingen.

## Bedrijfsprocessen

- **Terugvordering** — vaststellen van de vordering na constatering
- **Invordering** — innen van de vordering

## Bedrijfsfuncties

- **Inning en invordering** — beheer van vorderingen

## Relaties

- Gericht aan een [[Wiki/Bedrijfsobjecten/9-interne-organisatie/financien/debiteur|debiteur]]
- Kan leiden tot een [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/aflossingsplan|aflossingsplan]]
- Kan worden beëindigd door [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/aflossing|aflossing]], kwijtschelding of [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/afschrijving|afschrijving]]
- Kan aanleiding geven tot [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/interventie|interventie]] bij niet-betaling
- Kan resulteren in [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/restitutie|restitutie]] bij te veel ontvangen aflossing
- Verwant aan belastingaanslag — maar de GGM-vordering is specifiek sociaal domein, terwijl een belastingaanslag publiekrechtelijk is op grond van de belastingverordening

## Bronnen

- [[Wiki/Bronsamenvattingen/Belastingen/invordering-en-kwijtschelding]]
- [[Wiki/Bronsamenvattingen/Werk en Inkomen/participatiewet]] (art. 58-60c: terugvordering bijstand)
