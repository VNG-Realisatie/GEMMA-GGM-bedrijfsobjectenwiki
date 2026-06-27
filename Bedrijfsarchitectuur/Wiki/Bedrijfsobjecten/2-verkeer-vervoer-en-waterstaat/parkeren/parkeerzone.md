---
type: bedrijfsobject
naam: Parkeerzone
domein: [mobiliteit]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Parkeerzone"
ggm_guid: EAID_27219A32_3B52_4f54_AA67_A972F4B7D9D0
ggm_uml_type: Class
ggm_beleidsdomein: "Parkeren"
ggm_taakveld: "2 Verkeer, Vervoer en Waterstaat"
ggm_diagram: [Model Parkeren]
ggm_diagram_ids: [EAID_84B6B75B_2B58_455d_B019_C9B1E71717C2]
ggm_definitie: "Een afgebakend gebied binnen een gemeente  waar specifieke parkeerregels en -voorwaarden van toepassing zijn."
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""
ggm_gemma_naam: "Perkeerzone"
ggm_gemma_guid: "e5293eea-47b8-4091-8ac3-b28139a17c9f"
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: "business-object"
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-e5293eea-47b8-4091-8ac3-b28139a17c9f"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""
bo_definitie: "Afgebakend gebied binnen een gemeente waar specifieke parkeerregels en -voorwaarden gelden."
bedrijfsprocessen: [Parkeerbeleid, Parkeerhandhaving]
bedrijfsfuncties: [Parkeerbeleid]
bo_relaties:
  - type: compositie
    bedrijfsobject: "[[Parkeervlak]]"
    richting: "van-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: Parkeerzone bevat parkeervlakken
  - type: generalisatie
    bedrijfsobject: "[[Parkeergarage]]"
    richting: "naar-dit-BO"
    kardinaliteit: 
    beschrijving: Parkeergarage is specialisatie van Parkeerzone
  - type: associatie
    bedrijfsobject: "[[Parkeervergunning]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Parkeervergunning geldt binnen een parkeerzone
  - type: associatie
    bedrijfsobject: "[[Parkeerrecht]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Parkeerrecht is gekoppeld aan een parkeerzone
---

# Parkeerzone

Afgebakend gebied binnen een gemeente waar specifieke parkeerregels en -voorwaarden gelden.

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — bepaalt waar welke parkeerregels gelden
- ✅ Is herkenbaar voor domeinexperts — parkeerhandhavers en beleidsmakers werken dagelijks met zones
- ✅ Heeft een eigen bestaan binnen het domein — ruimtelijk afgebakend gebied met eigen regelset
- ✅ Kan in meervoud bestaan — Zone Binnenstad, Zone Lombok, betaald parkeergebieden
- ✅ Heeft een eigen levenscyclus — aanwijzing, instelling, tariefwijziging, uitbreiding, opheffing
- ✅ Heeft relaties met andere concepten — bevat parkeervlakken, vergunningen en rechten zijn zonegebonden

## Beschrijving

Een parkeerzone is een afgebakend gebied waar specifieke parkeerregels gelden, zoals betaald parkeren of vergunningparkeren. Het Mobiliteitsplan 2040 beschrijft uitbreiding van betaald parkeren als sturingsinstrument voor de bereikbaarheid en leefbaarheid van de stad. Elke zone heeft eigen tarieven, tijdvensters en vergunningsregels.

## GGM-bron

> "Een afgebakend gebied binnen een gemeente waar specifieke parkeerregels en -voorwaarden van toepassing zijn." — GGM, Parkeerzone (EAID_27219A32)

**Matchsterkte: exact.**

## Relaties

- ◆ → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervlak|Parkeervlak]] — parkeerzone bevat parkeervlakken
- ▲ ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeergarage|Parkeergarage]] — parkeergarage is specialisatie van parkeerzone
- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeervergunning|Parkeervergunning]] — parkeervergunning geldt binnen een parkeerzone
- ← [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/parkeerrecht|Parkeerrecht]] — parkeerrecht is gekoppeld aan een parkeerzone


## Bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/kwaliteitsnet-goederenvervoer-2007]]
- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]
- [[Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-fiets-2021]]
- [[Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-auto-2021]]
- [[Wiki/Bronsamenvattingen/mobiliteit/module-parkeernormen]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeerhubs]]
- [[Wiki/Bronsamenvattingen/mobiliteit/rapportage-routekaart-parkeerhubs]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-fietsparkeren]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeren-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-toegankelijkheid]]
- [[Wiki/Bronsamenvattingen/mobiliteit/parkeervisie]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitvoeringsprogramma-betaald-parkeren]]

## Terugmelding GGM

De GEMMA-naam bevat een typefout: "Perkeerzone" in plaats van "Parkeerzone". Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
