---
type: element
naam: Boete
onderwerp: [werk en inkomen]
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Boete
ggm_guid: EAID_05E49616_803F_4C1B_9663_262C4A191DF9
ggm_uml_type: Class
ggm_beleidsdomein: Normafwijking
ggm_taakveld: Inkomen
ggm_diagram: [Normafwijking]
ggm_diagram_ids: [EAID_1818B773_1463_43c7_BACA_FEE391FE27CD]
ggm_definitie: "Een boete is de uitkomst van een onderzoek naar rechtmatigheid. Dit leidt in principe tot een terug te vorderen bedrag. Er is voor gekozen om dit als aparte klasse te modelleren en niet als typering van een vordering, omdat we dit gegeven ook willen gebruiken bij risicoprofilering. Als de vordering niet (meer) bestaat, zou dit gegeven daarmee niet beschikbaar zijn. Daarnaast kan dit ook helpen bij het vastleggen van een boete van een poging tot fraude (zonder financiële consequenties, waardoor geen vordering is ontstaan (tijdig ontdekte valsheid in geschrifte e.d.)). Bij bedragen hoger dan 50.000 euro, wordt aangifte van fraude gedaan en volgt strafrechtelijk onderzoek. Feitelijk is het uitgangspunt bij het opleggen van een boete dat er altijd sprake is van opzet. Daarom is een apart gegeven Fraude niet opgenomen."
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

ggm_duplicaat_entiteiten: []
analyse_ggm_dekking: ""
bo_definitie: "Een bestuurlijke sanctie die het college oplegt wegens het niet of niet behoorlijk nakomen van de inlichtingenplicht, waarmee ten onrechte of te veel ontvangen bijstand is verkregen."
bo_toelichting: "Grondslag: art. 18a Participatiewet (boete tot het benadelingsbedrag, verhoogd bij recidive binnen 5-10 jaar) en art. 47g (boete bij uitvoering door de Sociale verzekeringsbank). Het college kan volstaan met een schriftelijke waarschuwing (lid 4) of afzien van een boete bij dringende redenen (lid 7). Kwijtschelding is mogelijk bij medewerking aan een schuldregeling, tenzij sprake was van opzet of grove schuld (art. 60c)."
bo_subtypes: []
bo_synoniemen:
- naam: Bestuurlijke boete
  context: Participatiewet art. 18a, 47g — de wettelijke term
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
- type: generalisatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/normafwijking/maatregel|Maatregel]]"
  richting: naar-dit-BO
  kardinaliteit:
  beschrijving: Boete is een specialisatie van Maatregel, apart gemodelleerd voor risicoprofilering ook als de onderliggende vordering niet meer bestaat
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening|Inkomensvoorziening]]"
  richting: naar-dit-BO
  kardinaliteit: "0..*"
  beschrijving: Een inkomensvoorziening kan aanleiding geven tot een of meer boetes
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering|Vordering]]"
  richting: van-dit-BO
  kardinaliteit: "0..1"
  beschrijving: Het benadelingsbedrag waarop de boete is gebaseerd kan (ook) als vordering worden teruggevorderd; de boete blijft bestaan als zelfstandig gegeven ook als deze vordering niet (meer) bestaat
bedrijfsprocessen: [rechtmatigheidsonderzoek, opleggen bestuurlijke boete, invordering boete, kwijtschelding boete]
bedrijfsfuncties: [handhaving, inkomensondersteuning]
---

# Boete

Bestuurlijke sanctie die het college oplegt wegens schending van de inlichtingenplicht, ten hoogste het benadelingsbedrag of — bij recidive — 150% daarvan.

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Betekenis binnen domein | ✅ Kernbegrip in fraude- en rechtmatigheidshandhaving |
| Herkenbaar voor domeinexperts | ✅ Standaardterm bij handhavers en klantmanagers |
| Eigen bestaan | ✅ Eigen bedrag, boetevorm en reden, los van een eventuele vordering (bewuste GGM-keuze, zie GGM-bron) |
| Meervoud | ✅ Kan herhaald worden opgelegd; verhoogd tarief bij recidive |
| Levenscyclus | ✅ Onderzoek → oplegging → (evt.) kwijtschelding bij schuldregeling → invordering/verrekening |
| Relaties | ✅ Specialisatie van Maatregel, relatie met Inkomensvoorziening en Vordering |

Score: **6/6**

## Beschrijving

Het college legt een bestuurlijke boete op wanneer een bijstandsgerechtigde de inlichtingenplicht (art. 17 lid 1) niet of niet behoorlijk is nagekomen, met als gevolg dat ten onrechte of te veel bijstand is verstrekt. De boete bedraagt ten hoogste het benadelingsbedrag, oplopend tot het bedrag van de vijfde categorie Wetboek van Strafrecht bij opzettelijk verzwijgen, en tot 150% van het benadelingsbedrag bij recidive binnen vijf jaar (tien jaar na een onvoorwaardelijke gevangenisstraf). Zonder benadelingsbedrag geldt een boete van ten hoogste de tweede categorie. Het college kan volstaan met een schriftelijke waarschuwing, of afzien van een boete bij dringende redenen.

Het GGM modelleert Boete bewust als aparte entiteit, niet als een typering van [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering|Vordering]]: het gegeven moet ook beschikbaar blijven voor risicoprofilering wanneer de onderliggende vordering niet (meer) bestaat, en voor het vastleggen van een boete bij een tijdig ontdekte fraudepoging zonder financiële consequenties. Bij bedragen boven €50.000 volgt aangifte en strafrechtelijk onderzoek.

## GGM-bron

> Een boete is de uitkomst van een onderzoek naar rechtmatigheid. Dit leidt in principe tot een terug te vorderen bedrag. Er is voor gekozen om dit als aparte klasse te modelleren en niet als typering van een vordering, omdat we dit gegeven ook willen gebruiken bij risicoprofilering.

- **Entiteit:** Boete (specialisatie van Maatregel)
- **Beleidsdomein:** Normafwijking (taakveld Inkomen, onder 6 Sociaal Domein)
- **Attributen:** Bedrag boete, Boetevorm, Reden boete, Voorwaarde boete
- **Matchsterkte:** exact

## Relaties

| Relatie | BO | Beschrijving |
|---|---|---|
| ↑ | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/normafwijking/maatregel\|Maatregel]] | Generalisatie: Boete is een specialisatie van Maatregel |
| ← | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Boete volgt uit schending van verplichtingen bij deze inkomensvoorziening |
| → | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Het benadelingsbedrag kan ook als vordering worden teruggevorderd |

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/participatiewet]]
