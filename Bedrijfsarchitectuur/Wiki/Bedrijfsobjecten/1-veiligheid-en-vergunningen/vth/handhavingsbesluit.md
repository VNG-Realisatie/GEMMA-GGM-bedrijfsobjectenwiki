---
type: bedrijfsobject
naam: Handhavingsbesluit
onderwerp: [Omgevingswet]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: ""
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

gemma_definitie: "Formeel besluit van het college om bij een geconstateerde overtreding een sanctie op te leggen, zoals een last onder dwangsom of bestuursdwang."
gemma_subtypes: []
relaties:
  - type: associatie
    bedrijfsobject: "[[VTH-zaak]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Een handhavingsbesluit hoort bij een VTH-zaak"
bedrijfsprocessen: [handhaving]
bedrijfsfuncties: [toezicht en handhaving]
---

## BO-criteria toetsing

1. **Identificeerbare instanties** — elk handhavingsbesluit is een afzonderlijk besluit met eigen kenmerken
2. **Eigen attributen** — datum, sanctietype, begunstigingstermijn, dwangsombedrag, overtreder, overtreding
3. **Levenscyclus** — voornemen → definitief besluit → bezwaar → beroep → onherroepelijk; kan worden ingetrokken of gewijzigd
4. **Meerdere processen** — handhaving bestaande bouw, handhaving na toezicht op realisatie, handhaving op verzoek
5. **Relevant op bedrijfsniveau** — aantallen handhavingsbesluiten worden gemonitord en gerapporteerd in VTH-jaarplannen
6. **Gemeentelijk perspectief** — het college neemt handhavingsbesluiten als bevoegd gezag op grond van de Gemeentewet (art. 125)

## Beschrijving

Een handhavingsbesluit is het formele besluit waarmee het college een sanctie oplegt bij een geconstateerde overtreding van regels in de fysieke leefomgeving. De zwaarte van de sanctie wordt bepaald aan de hand van de sanctiematrix, die de ernst van de overtreding afweegt tegen het gedrag van de overtreder. Het besluit kan een last onder dwangsom, last onder bestuursdwang of een andere sanctie inhouden. Het staat open voor bezwaar en beroep.

> "Artikel 125 van de Gemeentewet geeft het college de algemene bevoegdheid tot het toepassen van bestuursdwang ter uitvoering van wet- en regelgeving. Handhaving is een bevoegdheid, wat betekent dat het college ook kan afzien van handhaving." (bron: Uitvoeringsbeleid VTH Delft §7)

> "Als een zaak wordt opgepakt, bevat de handhavingsstrategie Omgevingswet een matrix waarin aan de hand van de ernst van de overtreding en het gedrag van de overtreder de sanctie kan worden bepaald." (bron: Uitvoeringsbeleid VTH Delft §7.3)

## Subtypes

Herkende specialisaties van Handhavingsbesluit. Gevonden in bronnen. Geen apart BO.

- **Last onder dwangsom** — besluit dat de overtreder verplicht de overtreding te beëindigen op straffe van een geldsom
- **Last onder bestuursdwang** — besluit waarbij de gemeente zelf ingrijpt om de overtreding ongedaan te maken, op kosten van de overtreder
- **Bouwstop** — besluit om bouwwerkzaamheden stil te leggen bij constatering van een ernstige overtreding

## Procesbron

Het handhavingsbesluit ontstaat in het handhavingsproces wanneer de gemeente na constatering van een overtreding besluit om een formele sanctie op te leggen. De Handhavingstrategie Omgevingswet Delft beschrijft de methodiek voor het bepalen van de sanctie via de sanctiematrix. Het VTH-uitvoeringsbeleid Delft beschrijft de kaders waarbinnen deze besluiten worden genomen.

## Relaties

| Relatie | Richting | Kardinaliteit | Beschrijving | Bron |
|---|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/vth-zaak\|VTH-zaak]] | van-dit-BO | 0..* | Een handhavingsbesluit hoort bij een VTH-zaak | beleidsbron |
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/bevinding\|Bevinding]] | van-dit-BO | 1..* | Een handhavingsbesluit is gebaseerd op één of meer bevindingen | beleidsbron |

## Bedrijfsprocessen

- Handhaving (opstellen voornemen, definitief besluit, bezwaarbehandeling)
- Invordering (bij niet-naleving last onder dwangsom)

## Bronnen
- [[Wiki/Bronsamenvattingen/Omgevingswet/uitvoeringsbeleid-vth-delft]]

## Terugmelding GGM

Het GGM bevat geen entiteit voor Handhavingsbesluit. Dit is een procesobject dat ontstaat in het handhavingsproces en een eigen levenscyclus kent (voornemen → besluit → bezwaar → onherroepelijk). Het is vergelijkbaar met [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking|Beschikking]] in het sociaal domein. Voorstel: overweeg toevoeging van een Handhavingsbesluit-entiteit aan het GGM. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
