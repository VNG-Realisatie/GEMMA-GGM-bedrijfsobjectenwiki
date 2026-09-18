---
type: element
naam: Voorschot
onderwerp: [werk en inkomen]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
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
bo_definitie: "Een renteloze geldlening die het college verstrekt zolang het recht op algemene bijstand nog niet is vastgesteld."
bo_toelichting: "Grondslag: art. 52 Participatiewet. Het college verleent uiterlijk 4 weken na de aanvraag, en vervolgens elke 4 weken, een voorschot van ten minste 95% van de bijstandsnorm — tenzij de aanvrager onvoldoende medewerking verleent of bij de aanvraag al duidelijk is dat geen recht op bijstand bestaat. Wordt het recht op bijstand vastgesteld, dan wordt het voorschot zonder machtiging verrekend met de toegekende bijstand (lid 4). Blijkt achteraf geen recht op bijstand te bestaan, dan wordt het voorschot teruggevorderd als [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering|Vordering]] (art. 58 lid 2 onderdeel d)."
bo_subtypes: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening|Inkomensvoorziening]]"
  richting: van-dit-BO
  kardinaliteit: "0..1"
  beschrijving: Voorschot wordt verrekend met de toegekende inkomensvoorziening zodra het recht is vastgesteld
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering|Vordering]]"
  richting: van-dit-BO
  kardinaliteit: "0..1"
  beschrijving: Wordt een vordering als achteraf blijkt dat geen recht op bijstand bestaat
bedrijfsprocessen: [voorschotverstrekking, verrekening voorschot]
bedrijfsfuncties: [inkomensondersteuning]
---

# Voorschot

Renteloze geldlening die de gemeente periodiek verstrekt vooruitlopend op de definitieve vaststelling van het recht op bijstand.

## BO-criteria toetsing

| Criterium | Toets |
|---|---|
| Betekenis binnen domein | ✅ Vast onderdeel van elke bijstandsaanvraag met een doorlooptijd |
| Herkenbaar voor domeinexperts | ✅ Standaardbegrip bij de uitvoering van de Participatiewet |
| Eigen bestaan | ✅ Eigen aard (geldlening), eigen bedrag (≥95% van de norm), los van de definitieve bijstand |
| Meervoud | ✅ Periodiek verstrekt, elke vier weken zolang het recht niet is vastgesteld |
| Levenscyclus | ✅ Verstrekking → verrekening met toegekende bijstand óf omzetting in een vordering |
| Relaties | ✅ Inkomensvoorziening, Vordering |

Score: **6/6**

## Beschrijving

Een bijstandsaanvraag kent een beslistermijn; om de aanvrager in die periode niet zonder middelen te laten, verleent het college uiterlijk vier weken na de aanvraag — en vervolgens telkens na vier weken — een voorschot in de vorm van een renteloze geldlening (art. 52 lid 1 Participatiewet), van ten minste 95% van de toepasselijke bijstandsnorm (lid 2). Het college kan dit weigeren als de aanvrager onvoldoende meewerkt aan het vaststellen van het recht, of als bij de aanvraag al duidelijk is dat geen recht op bijstand bestaat.

Wordt het recht op bijstand vastgesteld, dan verrekent het college het voorschot zonder machtiging met de toegekende bijstand (lid 4) — het voorschot gaat dan op in de reguliere [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening|Inkomensvoorziening]]. Blijkt achteraf geen recht op bijstand te bestaan, dan wordt het voorschot teruggevorderd als [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering|Vordering]] (art. 58 lid 2 onderdeel d).

Het GGM modelleert geen aparte entiteit voor het voorschot — het is een procesmatig, tijdelijk mechanisme dat niet als zelfstandig data-object in het GGM voorkomt.

## Procesbron

Afgeleid uit art. 52-53 Participatiewet. Zie [[Wiki/Bronsamenvattingen/Werk en Inkomen/participatiewet|Participatiewet]].

## Relaties

| Relatie | BO | Beschrijving |
|---|---|---|
| → | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/model-inkomen/inkomensvoorziening\|Inkomensvoorziening]] | Wordt verrekend met de toegekende bijstand |
| → | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/terug-en-invordering/vordering\|Vordering]] | Wordt teruggevorderd als achteraf geen recht op bijstand bestaat |

## Bronnen

- [[Wiki/Bronsamenvattingen/Werk en Inkomen/participatiewet]]

## Terugmelding GGM

GGM-hiaat: het GGM modelleert geen entiteit voor het voorschot als renteloze geldlening vooruitlopend op de bijstandsvaststelling. Teruggemeld als #95 in [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
