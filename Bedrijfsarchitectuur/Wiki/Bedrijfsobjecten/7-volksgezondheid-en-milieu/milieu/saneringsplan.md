---
type: bedrijfsobject
naam: Saneringsplan
domein: [Milieu]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit: ""
ggm_beleidsdomein: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_taakveld: ""
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ""
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
gemma_definitie: "Plan dat beschrijft hoe een bodem- of grondwaterverontreiniging wordt aangepakt, inclusief maatregelen, fasering en nazorg."
bedrijfsprocessen: [bodemsanering, gebiedsgericht grondwaterbeheer, vergunningverlening]
bedrijfsfuncties: [milieubeheer, vergunningverlening]
bronnen: [Wiki/Bronsamenvattingen/Milieu/gebiedsplan-grondwaterbeheer]
relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemverontreiniging|Bodemverontreiniging]]"
    richting: "naar-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: Een saneringsplan adresseert een of meer verontreinigingen
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondwatermeetpunt|Grondwatermeetpunt]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Saneringsplan kan monitoring via meetpunten voorschrijven
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Verplicht instrument bij ernstige verontreinigingen |
| Herkenbaar voor domeinexperts | ✅ Wettelijk gedefinieerd (Wbb art. 39/55e) |
| Heeft eigen bestaan | ✅ Zelfstandig document met eigen goedkeuring |
| Kan in meervoud bestaan | ✅ Per verontreiniging of per beheergebied |
| Heeft eigen levenscyclus | ✅ Opstelling → goedkeuring → uitvoering → nazorg → afmelding |
| Heeft relaties met andere concepten | ✅ Verontreiniging, meetpunten, beheergebied |

**6/6 criteria van toepassing.**

## Beschrijving

Een saneringsplan beschrijft hoe een bodem- of grondwaterverontreiniging wordt aangepakt. Het bevat de aard en omvang van de verontreiniging, de saneringsmaatregelen, fasering, kosten en nazorgverplichtingen. Het plan wordt goedgekeurd door het bevoegd gezag (gemeente of provincie).

Er bestaan twee vormen: een **gevalgericht saneringsplan** (per individuele verontreiniging) en een **gebiedsgericht beheerplan** (voor een heel beheergebied met vermengde verontreinigingen). Het Utrechtse gebiedsplan is een bijzondere vorm van het tweede type.

> "Wettelijke voorwaarde hiervoor is een vastgesteld gebiedsplan waarin de gemeente beschrijft hoe het beheer is georganiseerd en welke beheersmaatregelen worden genomen." (bron: [[Wiki/Bronsamenvattingen/Milieu/gebiedsplan-grondwaterbeheer|Gebiedsplan grondwaterbeheer]])

## Procesbron

Saneringsplannen ontstaan in het saneringsproces wanneer een verontreiniging als ernstig is vastgesteld. Wettelijke basis: Wet bodembescherming art. 39 (gevalgericht) en art. 55e (gebiedsgericht). Onder de Omgevingswet vallen deze onder het overgangsrecht.

## Relaties

- **[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemverontreiniging|Bodemverontreiniging]]** — het plan adresseert een of meer verontreinigingen
- **[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondwatermeetpunt|Grondwatermeetpunt]]** — het plan kan monitoring via meetpunten voorschrijven

## Terugmelding GGM

Saneringsplan is een registratie-object dat gemeenten als bevoegd gezag opstellen en beheren. Geen GGM-equivalent. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
