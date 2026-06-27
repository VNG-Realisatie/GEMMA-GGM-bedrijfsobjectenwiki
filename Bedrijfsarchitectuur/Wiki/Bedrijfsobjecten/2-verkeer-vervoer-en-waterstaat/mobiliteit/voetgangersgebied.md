---
type: bedrijfsobject
naam: Voetgangersgebied
domein:
- mobiliteit
archimate_type: business-object
grondslag: governance-object
ggm_entiteit: ''
ggm_beleidsdomein: Mobiliteit
ggm_guid: ''
ggm_uml_type: ''
ggm_taakveld: ''
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ''
ggm_toelichting: ''
ggm_synoniemen: ''
ggm_herkomst: ''
ggm_gemma_naam: ''
ggm_gemma_guid: ''
ggm_gemma_definitie: ''
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: ''
ggm_gemma_type: ''
ggm_gemma_url: ''
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
bo_definitie: Aangewezen gebied waar de voetganger hoofdgebruiker is en gemotoriseerd verkeer beperkt is toegestaan.
bedrijfsprocessen:
- Verkeersbeleid
- Inrichting openbare ruimte
- Handhaving
bedrijfsfuncties:
- Verkeersmanagement
- Beheer openbare ruimte
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/verkeersbesluit|Verkeersbesluit]]'
  richting: naar-dit-BO
  kardinaliteit: 1
  beschrijving: Voetgangersgebied wordt ingesteld via een verkeersbesluit
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/halte|Halte]]'
  richting: van-dit-BO
  kardinaliteit: 0..*
  beschrijving: OV-haltes binnen of aan de rand van het voetgangersgebied
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/laad-en-losplaats|Laad- en Losplaats]]'
  richting: van-dit-BO
  kardinaliteit: 0..*
  beschrijving: Voetgangersgebied bevat laad- en losplaatsen met venstertijden
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/zero-emissiezone|Zero-emissiezone]]'
  richting: bidirectioneel
  kardinaliteit: 0..1
  beschrijving: Voetgangersgebied kan overlappen met zero-emissiezone
---

# Voetgangersgebied

Aangewezen gebied waar de voetganger hoofdgebruiker is en gemotoriseerd verkeer beperkt is toegestaan.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — formeel aangewezen gebied met specifieke inrichtingseisen en verkeersregels
- ✅ Is herkenbaar voor domeinexperts — beleidsmedewerkers en verkeerskundigen werken met voetgangersgebieden als ruimtelijke categorie
- ✅ Heeft een eigen bestaan binnen het domein — heeft afgebakende grenzen, eigen regime (fietsers te gast, auto alleen bestemmingsverkeer)
- ✅ Kan in meervoud bestaan — binnenstad Utrecht, Utrecht Science Park, Leidsche Rijn Centrum; mogelijk meer in 2040
- ✅ Heeft een eigen levenscyclus — aanwijzing, uitbreiding, eventueel opheffing; binnenstad en USP worden uitgebreid
- ✅ Heeft relaties met andere concepten — relatie met verkeersbesluiten, haltes, laad-/losplaatsen, zero-emissiezones

## Beschrijving

Een voetgangersgebied is een door de gemeente aangewezen zone waar de voetganger (samen met de fietser) hoofdgebruiker is. Autoverkeer en logistiek verkeer zijn alleen toegestaan als bestemmingsverkeer, vaak binnen venstertijden. De inrichting moet zo helder en veilig zijn dat verkeer zichzelf regelt en verkeerslichten zo min mogelijk nodig zijn.

Het Mobiliteitsplan 2040 definieert voetgangersgebieden als kern van de A-zones. In de binnenstad en het Utrecht Science Park wordt het voetgangersgebied vergroot. Het voetgangersgebied verschilt van de bredere A-zone doordat gemotoriseerd verkeer er niet alleen lager geprioriteerd is, maar daadwerkelijk beperkt wordt.

> "In de A-zones is de verkeersruimte schaars en is verblijfskwaliteit van het grootste belang. Fietser en vooral voetganger zijn hoofdgebruiker en krijgen prioriteit." (bron: Mobiliteitsplan 2040)

## Juridische bron

Governance-object met juridische grondslag in verkeersbesluiten. Het [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040 - Jouw straat en onze stad gezond, aantrekkelijk en bereikbaar voor iedereen]] beschrijft de aanwijzing en uitbreiding van voetgangersgebieden als kernonderdeel van het A-zone beleid.

## Relaties

- ← [[Verkeersbesluit]] — voetgangersgebied wordt ingesteld via een verkeersbesluit [1]
- → [[Halte]] — OV-haltes binnen of aan de rand van het voetgangersgebied [0..*]
- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/mobiliteit/laad-en-losplaats|Laad- en Losplaats]] — laad-/losplaatsen met venstertijden binnen het gebied [0..*]
- ↔ [[Zero-emissiezone]] — voetgangersgebied kan overlappen met zero-emissiezone [0..1]


## Bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor voetgangersgebieden of verkeerszonering. Als governance-object valt dit structureel buiten de GGM-scope. Het voetgangersgebied heeft relevante eigenschappen (begrenzing, geldend regime, venstertijden, toegangsregels) die als data-object modelleerbaar zijn. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
