---
type: element
naam: OV-lijn
onderwerp:
- mobiliteit
archimate_type: business-object
grondslag: procesobject
ggm_entiteit:
ggm_beleidsdomein: Mobiliteit
ggm_guid:
ggm_uml_type:
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
bo_definitie: "Tram- of buslijn met een vaste route, dienstregeling en frequentie voor het vervoeren van reizigers."
bo_toelichting:
bedrijfsprocessen:
- OV-beleid
- Concessiebeheer
bedrijfsfuncties:
- Openbaar vervoer
bo_relaties:
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/ov-knooppunt|OV-knooppunt]]"
  richting: van-dit-BO
  kardinaliteit: "1..*"
  beschrijving: Lijn passeert een of meer knooppunten
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/halte|Halte]]"
  richting: van-dit-BO
  kardinaliteit: "2..*"
  beschrijving: Lijn heeft meerdere haltes
---

# OV-lijn

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — basiseenheid van het openbaar vervoer
- ✅ Is herkenbaar voor domeinexperts — OV-beleidsmakers en concessieverleners werken met lijnen
- ✅ Heeft een eigen bestaan binnen het domein — een lijn is een zelfstandig traject met eigen dienstregeling
- ✅ Kan in meervoud bestaan — tientallen tram- en buslijnen in het stedelijk netwerk
- ✅ Heeft een eigen levenscyclus — planning, aanbesteding, exploitatie, frequentiewijziging, opheffing
- ✅ Heeft relaties met andere concepten — verbindt knooppunten en haltes

## Beschrijving

Een OV-lijn is een tram- of buslijn met een vaste route, dienstregeling en frequentie. De gemeente stuurt via concessies op het lijnennet. Het Mobiliteitsplan 2040 zet in op hogere frequenties en nieuwe lijnen om de groei van het OV-gebruik op te vangen.

## Specialisaties

| Subtype | Omschrijving |
|---|---|
| Tramlijn | OV-lijn uitgevoerd met tram over een vast railtraject |
| Buslijn | OV-lijn uitgevoerd met bus over de weg |

## Procesbron

Afgeleid uit het gemeentelijk OV-beleid en concessiebeheer. Het [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040 - Jouw straat en onze stad gezond, aantrekkelijk en bereikbaar voor iedereen]] beschrijft de gewenste uitbreiding van het lijnennet.

## Relaties

- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/ov-knooppunt|OV-knooppunt]] — lijn passeert knooppunten [1..*]
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/halte|Halte]] — lijn heeft meerdere haltes [2..*]


## Bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor OV-lijnen. Dit is een registratieobject: gemeenten registreren lijnen met route, frequentie, modaliteit en concessiehouder. Past bij beleidsdomein Mobiliteit onder taakveld 2. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
