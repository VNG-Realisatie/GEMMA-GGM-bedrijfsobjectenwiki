---
type: element
naam: Vermogenscomponent
onderwerp: [werk en inkomen]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Vermogenscomponent
ggm_guid: EAID_08000E15_8AA2_AE9A_89F0_262C7C061238
ggm_uml_type: Class
ggm_beleidsdomein: Sociaal Domein Generiek
ggm_taakveld: "6 Sociaal Domein"
ggm_diagram: [Diagram Profiel, Diagram Vermogen]
ggm_diagram_ids: [EAID_60B49988_60E9_4fa6_A70B_990FA6C64BC2, EAID_8B78D87D_33A0_48bc_B883_C6C956FB5C6D]
ggm_definitie: "Een vermogenscomponent is een onderdeel van het totale vermogen van een persoon of huishouden, dat afzonderlijk wordt weergegeven (zoals spaargeld, beleggingen, eigen woning netto of pensioenvermogen)."
ggm_toelichting: "In statistische en economische analyses wordt vermogen gezien als het saldo van bezittingen minus schulden van een persoon of huishouden. Het totale vermogen kan worden opgesplitst in verschillende componenten — bijvoorbeeld financiële tegoeden, effecten, onroerend goed, pensioenvermogen of schulden — die elk afzonderlijk bijdragen aan het geheel."
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

ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Vermogenscomponent** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Hypotheek** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Motorvoertuig** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Onroerend goed** (detail) — Detailgegeven (weinig attributen, geen structureel signaal)
  - **Waardepeiling** (onderdeel) — Onderdeel van Vermogenscomponent
bo_definitie: "Een afzonderlijk vastgesteld onderdeel van het vermogen van een bijstandsgerechtigde of diens gezin (bijv. spaargeld, auto, eigen woning), met een eigen vrij te laten grens."
bo_toelichting: "Grondslag: art. 34 Participatiewet. Vermogen is de waarde van bezittingen minus schulden, aangevuld met tijdens de bijstandsperiode ontvangen middelen die geen inkomen zijn. Algemeen gebruikelijke of noodzakelijke bezittingen tellen niet mee; het vermogen in de eigen woning telt niet mee voor zover onder €67.500 (art. 34 lid 2 onderdeel d); spaargeld opgebouwd tijdens de bijstandsperiode telt niet mee. Vrijlatingsgrenzen (art. 34 lid 3): €8.000 (alleenstaande), €16.000 (alleenstaande ouder of gehuwden)."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]"
  richting: naar-dit-BO
  kardinaliteit: "0..*"
  beschrijving: Een client (bijstandsgerechtigde) kan meerdere vermogenscomponenten hebben
bedrijfsprocessen: [middelentoets, vermogensvaststelling, heronderzoek vermogen]
bedrijfsfuncties: [inkomensondersteuning]
---

# Vermogenscomponent

Een afzonderlijk onderdeel van het vermogen van een bijstandsgerechtigde of diens gezin — spaargeld, een auto, de eigen woning — elk met een eigen vastgestelde waarde en vrij te laten grens.

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Betekenis binnen domein | ✅ Kernbegrip van de middelentoets (art. 34 Participatiewet) |
| Herkenbaar voor domeinexperts | ✅ Standaardbegrip bij de vermogensvaststelling |
| Eigen bestaan | ✅ Eigen identificatie, soort en vastgestelde waarde, los van andere componenten |
| Meervoud | ✅ Een gezin heeft doorgaans meerdere vermogenscomponenten (bankrekening, auto, woning) |
| Levenscyclus | ✅ Vaststelling bij aanvraag → periodiek heronderzoek → wijziging bij waardeverandering |
| Relaties | ✅ Relatie met Client (bijstandsgerechtigde) |

Score: **6/6**

## Beschrijving

Bij de beoordeling van het recht op algemene bijstand toetst de gemeente niet alleen het inkomen maar ook het vermogen: de waarde van bezittingen verminderd met schulden (art. 34 lid 1 Participatiewet). Dit vermogen wordt per afzonderlijk bestanddeel — vermogenscomponent — vastgesteld: spaargeld, een auto, beleggingen, de eigen woning. Niet elk bestanddeel telt volledig mee: algemeen gebruikelijke of noodzakelijke bezittingen, tijdens de bijstandsperiode opgebouwd spaargeld, en het vermogen in de eigen woning tot €67.500 blijven buiten beschouwing (art. 34 lid 2). Boven de generieke vrijlatingsgrens (€8.000 voor een alleenstaande, €16.000 voor een alleenstaande ouder of gehuwden, art. 34 lid 3) bestaat geen recht op bijstand.

## Subtypes

Het GGM modelleert Vermogenscomponent als abstract met vier specialisaties. Deze zijn generieke Sociaal Domein-concepten (ook relevant buiten de Participatiewet, bijv. Wmo/Jeugd) en worden hier als subtype vermeld, niet als eigen BO uitgewerkt.

- **Bankrekening** — saldo op een rekening van de bijstandsgerechtigde of diens gezin.
- **Hypotheek** — schuld verbonden aan de eigen woning, in mindering gebracht op de woningwaarde.
- **Motorvoertuig** — waarde van een auto of ander motorvoertuig.
- **Onroerend goed** — de eigen woning of andere onroerende zaken (zie art. 34 lid 2 onderdeel d voor de woning-vrijlating).

## GGM-bron

> Een vermogenscomponent is een onderdeel van het totale vermogen van een persoon of huishouden, dat afzonderlijk wordt weergegeven (zoals spaargeld, beleggingen, eigen woning netto of pensioenvermogen).

- **Entiteit:** Vermogenscomponent (abstract, generaliseert naar Bankrekening, Hypotheek, Motorvoertuig, Onroerend goed)
- **Beleidsdomein:** Sociaal Domein Generiek → Vermogen (taakveld 6 Sociaal Domein)
- **Attributen:** Code soort vermogenscomponent, Datum vaststelling vermogencomponent, identificatie, Nog aan te spreken vermogen, Vrij te laten vermogen
- **Matchsterkte:** exact

## Relaties

| Relatie | BO | Beschrijving |
|---|---|---|
| ← | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | Client kan meerdere vermogenscomponenten hebben |

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/participatiewet]]
- [[Wiki/Bronsamenvattingen/Werk en Inkomen/wet-suwi-en-sgr]] (RDW/Kadaster-gegevens t.b.v. de vermogenstoets)
