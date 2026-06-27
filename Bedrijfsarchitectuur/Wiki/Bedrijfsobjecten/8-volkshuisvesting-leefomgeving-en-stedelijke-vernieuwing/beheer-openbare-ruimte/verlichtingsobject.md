---
type: bedrijfsobject
naam: Verlichtingsobject
domein: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Verlichtingsobject"
ggm_guid: EAID_8CD4C799_C403_41B6_B409_06D37398E31
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Hoofdobjecten IMBOR en Geo-object]
ggm_diagram_ids: [EAID_E3EBD7A0_35C4_4bf4_BD01_6D97AD0B8BF3]
ggm_definitie: "Paal of mast waaraan openbare verlichting is bevestigd."
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
bo_definitie: "Paal, mast of gevelarmatuur in de openbare ruimte die voorziet in straatverlichting."
bo_subtypes:
  - naam: "Lichtmast"
    omschrijving: "Vrijstaande paal met armatuur voor straatverlichting, veruit het meeste type (56.000 stuks)"
    ggm_entiteit: Verlichtingsobject
    ggm_guid: EAID_8CD4C799_C403_41B6_B409_06D37398E31
    ggm_attribuut: type
  - naam: "Gevelarmatuur"
    omschrijving: "Aan gevel bevestigde verlichting, met name in de historische binnenstad"
    ggm_entiteit: Verlichtingsobject
    ggm_guid: EAID_8CD4C799_C403_41B6_B409_06D37398E31
    ggm_attribuut: type
bo_relaties:
  - type: generalisatie
    bedrijfsobject: Beheerobject (GGM)
    richting: "van-dit-BO"
    kardinaliteit:
    beschrijving: Verlichtingsobject is een specialisatie van Beheerobject
bedrijfsprocessen: [Onderhoud openbare verlichting, Vervanging armaturen, Inspectie verlichting, Storingsdienst]
bedrijfsfuncties: [Beheer openbare ruimte, Openbare verlichting]
ggm_gemma_naam: "Verlichtingsobject"
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Essentieel voor veiligheid en leefbaarheid van de openbare ruimte |
| Is herkenbaar voor domeinexperts | ✅ | Lantaarnpalen en armaturen — basisbegrip in openbare-ruimtebeheer |
| Heeft een eigen bestaan binnen het domein | ✅ | Elke paal individueel geregistreerd met locatie, type, vermogen |
| Kan in meervoud bestaan | ✅ | Duizenden lichtmasten in de gemeente |
| Heeft een eigen levenscyclus | ✅ | Aanleg → lamp-/armatuurvervanging → renovatie → vervanging; afschrijvingstermijn 25 jaar |
| Heeft relaties met andere concepten | ✅ | Mast, kast (voedingskast), installatie, kwaliteitsniveau, storing |

Score: 6/6.

## Beschrijving

Een verlichtingsobject is een paal of mast in de openbare ruimte waaraan verlichting is bevestigd. De gemeente registreert elke lichtmast met locatie, type armatuur, vermogen en onderhoudsstatus. De afschrijvingstermijn is 25 jaar.

In Utrecht is de openbare verlichting grootschalig gerenoveerd en omgebouwd naar LED. Het Utrechtse Steegarmatuur — een kenmerkend armatuur uit de jaren 60 in de historische binnenstad — is in 2019 gerenoveerd met behoud van het oorspronkelijke ontwerp en omgebouwd naar LED met een warmere uitstraling. Het vermogen daalde van 40 naar 25 Watt met dimming in de nachtelijke uren.

De Nota Beheer OR signaleert dat er voor openbare verlichting (OVL) geen achterstallig onderhoud is. Bij eerdere berekeningen werd uitgegaan van theoretische levensduur; nu wordt gestuurd vanuit technische inspecties.

## Specialisaties

| Subtype | Omschrijving | Bron |
|---|---|---|
| Lichtmast | Vrijstaande paal, 56.000 stuks in Utrecht | Kadernota KOR (infographic) |
| Gevelarmatuur | Aan gevel bevestigde verlichting, met name historische binnenstad | Kadernota KOR (bijzondere verlichtingsarmaturen) |

Het inspectieregime verschilt per type lamp: elke 2 tot 6 jaar (Nota Beheer OR, bijlage inspectieregimes). Het Steegarmatuur — kenmerkend Utrechts gevelarmatuur uit de jaren 60 — is in 2019 gerenoveerd en omgebouwd naar LED met behoud van het oorspronkelijke ontwerp.

Het GGM heeft geen attributen op Verlichtingsobject zelf (alleen geërfd van Beheerobject). De GGM-entiteit Mast ("draagconstructie bestaande uit een verticale buispaal") is een gerelateerd object dat de fysieke drager beschrijft.

## GGM-bron

> "Paal of mast waaraan openbare verlichting is bevestigd."

- **Entiteit**: Verlichtingsobject
- **Beleidsdomein**: Beheer Openbare Ruimte (Model IMBOR)
- **Taakveld**: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Matchsterkte**: exact
- **Attributen**: *(geen attributen op de entiteit zelf — attributen worden geërfd van Beheerobject)*

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| generalisatie | Beheerobject (GGM) | Verlichtingsobject → Beheerobject | GGM |

## Bedrijfsprocessen

- **Onderhoud openbare verlichting**: lamp- en armatuurvervanging, LED-ombouw
- **Vervanging armaturen**: vervanging palen en armaturen bij einde levensduur
- **Inspectie verlichting**: technische inspectie op conditie en veiligheid
- **Storingsdienst**: meldingen van defecte verlichting


## Subtypes

- **Lichtmast** — Vrijstaande paal met armatuur voor straatverlichting, veruit het meeste type (56.000 stuks)
- **Gevelarmatuur** — Aan gevel bevestigde verlichting, met name in de historische binnenstad

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
