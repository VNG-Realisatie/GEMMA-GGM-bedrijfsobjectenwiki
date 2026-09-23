---
type: element
naam: Preventie- en handhavingsplan alcohol
onderwerp: [Openbare Orde en Veiligheid]
archimate_type: business-object
grondslag: governance-object

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

bo_definitie: "Door de gemeenteraad vastgesteld plan met de hoofdzaken van het beleid betreffende de preventie van alcoholgebruik en de handhaving van de Alcoholwet (art. 43a Alcoholwet)."
bo_toelichting:
bo_subtypes: []
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/alcoholoverlastgebied|Alcoholoverlastgebied]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: Het handhavingsbeleid uit het plan kan mede de aanwijzing van alcoholoverlastgebieden onderbouwen
bedrijfsprocessen: [Vaststellen preventie- en handhavingsbeleid alcohol]
bedrijfsfuncties: [Openbare orde en veiligheid, Volksgezondheid]
---

# Preventie- en handhavingsplan alcohol

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — één plan per gemeente, met vaststellingsdatum en geldigheidsperiode |
| Eigen attributen | Ja — doelstellingen, preventieacties, handhavingsbeleid, te behalen resultaten (art. 43a lid 3) |
| Levenscyclus | Ja — eerste vaststelling → elke 4 jaar herzien (gelijktijdig met de nota gemeentelijk gezondheidsbeleid) → tussentijds wijzigbaar |
| Gemeentelijk eigendom | Ja — de gemeenteraad stelt het plan vast |
| Wettelijke grondslag | Ja — Alcoholwet art. 43a |
| Registratieverplichting | Ja — wettelijk verplichte vaststelling binnen een vaste termijn, met verplichte minimuminhoud |

Score: 6/6 criteria.

## Beschrijving

Het preventie- en handhavingsplan alcohol bevat de hoofdzaken van het gemeentelijke beleid voor de preventie van alcoholgebruik — met name onder jongeren — en de handhaving van de Alcoholwet. De gemeenteraad stelt het plan voor het eerst vast, en vervolgens elke vier jaar opnieuw, gelijktijdig met de nota gemeentelijk gezondheidsbeleid (art. 13 lid 2 Wet publieke gezondheid). Het plan kan tussentijds worden gewijzigd.

Het plan bevat in elk geval (art. 43a lid 3): de doelstellingen van het preventie- en handhavingsbeleid; de acties om alcoholgebruik onder jongeren te voorkomen, eventueel in samenhang met andere preventieprogramma's; de wijze waarop het handhavingsbeleid wordt uitgevoerd en welke handhavingsacties in de planperiode worden ondernomen; en de minimaal te behalen resultaten.

## Juridische bron

Wettelijke grondslag: Alcoholwet, artikel 43a.

Toelichting in [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/alcoholwet-wettekst|Alcoholwet — wettekst]].

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| associatie | [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/alcoholoverlastgebied\|Alcoholoverlastgebied]] | → | Handhavingsbeleid uit het plan kan de aanwijzing van overlastgebieden onderbouwen |

## Bedrijfsprocessen

- **Vaststellen preventie- en handhavingsbeleid alcohol** — eerste vaststelling, vierjaarlijkse herziening, tussentijdse wijziging

## Bronnen
- [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/alcoholwet-wettekst]]

## Terugmelding GGM

GGM-hiaat: wettelijk verplicht gemeentelijk beleidsdocument met vaste vierjaarlijkse cyclus en verplichte minimuminhoud (art. 43a Alcoholwet), zonder GGM-tegenhanger. Vergelijkbaar met andere wettelijk verankerde beleidsplannen (bijv. het meerjarenplan digitale informatiehuishouding, zie [[Wiki/Bedrijfsobjecten/9-interne-organisatie/ict/meerjarenplan|Meerjarenplan]]), die evenmin in het GGM zijn gemodelleerd.
