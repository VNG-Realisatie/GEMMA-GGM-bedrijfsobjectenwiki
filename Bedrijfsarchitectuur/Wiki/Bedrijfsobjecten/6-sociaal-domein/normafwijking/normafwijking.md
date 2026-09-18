---
type: element
naam: Normafwijking
onderwerp: [werk en inkomen]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Normafwijking
ggm_guid: EAID_167FF4C9_6B66_EEDA_5189_262C4A139258
ggm_uml_type: Class
ggm_beleidsdomein: Normafwijking
ggm_taakveld: Inkomen
ggm_diagram: [Diagram GGM en Inkomen, Normafwijking]
ggm_diagram_ids: [EAID_FD4BAB10_5D3E_4d14_8949_24CA09AC42A7, EAID_1818B773_1463_43c7_BACA_FEE391FE27CD]
ggm_definitie: "Een normafwijking (in het kader van bijstand) is het constateren dat een bijstandsgerechtigde afwijkt van de normatieve verplichtingen die verbonden zijn aan het recht op bijstand (bijv. arbeids- of inlichtingenplicht), wat aanleiding kan geven tot toepassing van een maatregel op de uitkering."
ggm_toelichting: "In de uitvoering van de Participatiewet moet een bijstandsgerechtigde voldoen aan verschillende normen en verplichtingen (zoals het zoeken naar werk, voldoen aan inlichtingen- en medewerkingsplichten, of andere door de gemeente opgelegde verplichtingen). Wanneer deze verplichtingen niet of onvoldoende worden nagekomen, kan dit worden aangemerkt als een normafwijking die leidt tot sanctionering via maatregelen op de uitkering (zoals verlaging van de bijstandsuitkering). Maatregelen worden in gemeentelijke maatregelenverordeningen vastgelegd en zijn verbonden aan de wettelijke kaders van de Participatiewet."
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
  Dit BO heeft de GGM-entiteit **Normafwijking** als directe tegenhanger.
bo_definitie: "Het constateren dat een bijstandsgerechtigde afwijkt van de normatieve verplichtingen die verbonden zijn aan het recht op bijstand, wat aanleiding kan geven tot een maatregel op de uitkering."
bo_toelichting: "Vastgesteld op basis van de arbeids-, inlichtingen- of andere verplichtingen uit hoofdstuk 2 en art. 55 Participatiewet (art. 17, 18, 55). Bevat een aparte beoordeling van verwijtbaarheid: bij het ontbreken van elke vorm van verwijtbaarheid ziet het college af van een maatregel (art. 18 lid 9)."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/normafwijking/maatregel|Maatregel]]"
  richting: van-dit-BO
  kardinaliteit: "0..1"
  beschrijving: Een normafwijking kan leiden tot een maatregel; bij ontbreken van verwijtbaarheid volgt geen maatregel
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening|Inkomensvoorziening]]"
  richting: naar-dit-BO
  kardinaliteit: "0..*"
  beschrijving: Een inkomensvoorziening kan meerdere normafwijkingen kennen over haar looptijd
bedrijfsprocessen: [handhavingsonderzoek, verwijtbaarheidsbeoordeling]
bedrijfsfuncties: [handhaving, inkomensondersteuning]
---

# Normafwijking

Het constateren dat een bijstandsgerechtigde afwijkt van de verplichtingen die aan het recht op bijstand verbonden zijn, met een aparte beoordeling van verwijtbaarheid en recidive, als basis voor een eventuele maatregel.

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Betekenis binnen domein | ✅ Centraal begrip in de handhaving van bijstandsverplichtingen |
| Herkenbaar voor domeinexperts | ✅ Klantmanagers en handhavers kennen dit als aparte beoordelingsstap vóór een maatregel |
| Eigen bestaan | ✅ Eigen identificatie, vaststellingsdatum en verwijtbaarheidsoordeel, los van de uiteindelijke maatregel |
| Meervoud | ✅ Een bijstandsgerechtigde kan meerdere normafwijkingen over de tijd hebben (recidive) |
| Levenscyclus | ✅ Constatering → verwijtbaarheidsbeoordeling → al dan niet leidend tot een maatregel |
| Relaties | ✅ Relatie met Maatregel, Inkomensvoorziening |

Score: **6/6**

## Beschrijving

Voordat een gemeente de bijstand verlaagt, moet eerst worden vastgesteld dát een bijstandsgerechtigde een verplichting niet is nagekomen — bijvoorbeeld de arbeids-, inlichtingen- of medewerkingsplicht (art. 9, 17, 55 Participatiewet). Deze constatering, inclusief het aparte oordeel of de bijstandsgerechtigde dit te verwijten valt en of er sprake is van recidive, is de normafwijking. Alleen bij (een bepaalde mate van) verwijtbaarheid volgt een [[Wiki/Bedrijfsobjecten/6-sociaal-domein/normafwijking/maatregel|Maatregel]]; ontbreekt elke vorm van verwijtbaarheid, dan ziet het college af van een maatregel (art. 18 lid 9 Participatiewet).

Het GGM modelleert dit bewust als aparte entiteit vóór Maatregel: de verwijtbaarheidsbeoordeling en het al dan niet vaststellen van recidive zijn zelfstandig relevante gegevens, ook wanneer zij niet tot een maatregel leiden.

## GGM-bron

> Een normafwijking (in het kader van bijstand) is het constateren dat een bijstandsgerechtigde afwijkt van de normatieve verplichtingen die verbonden zijn aan het recht op bijstand (bijv. arbeids- of inlichtingenplicht), wat aanleiding kan geven tot toepassing van een maatregel op de uitkering.

- **Entiteit:** Normafwijking
- **Beleidsdomein:** Normafwijking (taakveld Inkomen, onder 6 Sociaal Domein)
- **Attributen:** Datum vaststelling normafwijking, Datum vaststelling verwijtbaarheid, identificatie, Motivatie verwijtbaarheid, Recidive, Type normafwijking, Verwijtbaarheid
- **Matchsterkte:** exact

## Relaties

| Relatie | BO | Beschrijving |
|---|---|---|
| → | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/normafwijking/maatregel\|Maatregel]] | Kan leiden tot een maatregel |
| ← | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Normafwijking wordt vastgesteld bij een lopende inkomensvoorziening |

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/participatiewet]]
