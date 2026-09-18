---
type: element
naam: Zero-emissiezone
onderwerp:
- mobiliteit
archimate_type: business-object
grondslag: governance-object
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
bo_definitie: "Aangewezen zone waarbinnen alleen voertuigen zonder uitstoot van schadelijke stoffen mogen rijden."
bo_toelichting:
bedrijfsprocessen:
- Milieubeleid
- Goederenvervoerbeleid
- Handhaving
bedrijfsfuncties:
- Verkeersmanagement
- Milieubeleid
bo_relaties:
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/logistieke-route|Logistieke Route]]"
  richting: van-dit-BO
  kardinaliteit: "0..*"
  beschrijving: Zero-emissiezone wordt ontsloten door logistieke routes
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/laad-en-losplaats|Laad- en Losplaats]]"
  richting: van-dit-BO
  kardinaliteit: "0..*"
  beschrijving: Zero-emissiezone bevat laad- en losplaatsen
- type: associatie
  bedrijfsobject: "[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/verkeersbesluit|Verkeersbesluit]]"
  richting: naar-dit-BO
  kardinaliteit: "1"
  beschrijving: Zone wordt ingesteld via een verkeersbesluit
---

# Zero-emissiezone

Aangewezen zone waarbinnen alleen voertuigen zonder uitstoot van schadelijke stoffen mogen rijden.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — centraal instrument in de transitie naar schone stadslogistiek
- ✅ Is herkenbaar voor domeinexperts — beleidsmakers, handhavers en vervoerders werken ermee
- ✅ Heeft een eigen bestaan binnen het domein — ruimtelijk afgebakende zone met juridische status
- ✅ Kan in meervoud bestaan — zones per kern of stadsdeel, met verschillende ingangstijdstippen
- ✅ Heeft een eigen levenscyclus — instelling, uitbreiding, handhaving, evaluatie
- ✅ Heeft relaties met andere concepten — relatie met routes, laad-/losplaatsen en verkeersbesluiten

## Beschrijving

Een zero-emissiezone is een door de gemeente ingesteld gebied waar alleen emissievrije voertuigen mogen rijden. De zone heeft een juridische grondslag via een verkeersbesluit. In Utrecht geldt de zone vanaf 2025 voor logistiek verkeer en vanaf 2030 voor al het verkeer in de binnenstad.

## Juridische bron

Governance-object met juridische grondslag in verkeersbesluiten en Rijksbeleid (Klimaatakkoord). Het [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040 - Jouw straat en onze stad gezond, aantrekkelijk en bereikbaar voor iedereen]] beschrijft de uitrol van zero-emissiezones als kerninstrument voor schone stadslogistiek.

## Relaties

- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/logistieke-route|Logistieke Route]] — zone wordt ontsloten door logistieke routes [0..*]
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/laad-en-losplaats|Laad- en Losplaats]] — zone bevat laad- en losplaatsen [0..*]
- ← [[Verkeersbesluit]] — zone wordt ingesteld via een verkeersbesluit [1]


## Bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor zero-emissiezones — governance-objecten zoals juridische kaders zijn in het GGM niet compleet gedekt. Niettemin heeft de zone registreerbare eigenschappen (begrenzing, ingangsdatum, voertuigcategorieen, ontheffingsregime) die als data-object modelleerbaar zijn. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
