---
type: element
naam: Overig Gebouwd Object
onderwerp: [Basisregistraties, RSGBPlus]
archimate_type: business-object
grondslag: ggm-entiteit

# GGM-velden
ggm_entiteit: OverigGebouwdObject
ggm_guid: EAID_7CDF37D9_26D7_46a5_9CF3_392601BDCECA
ggm_uml_type: Class
ggm_beleidsdomein: RSGBPlus
ggm_taakveld: "99 Kern"
ggm_diagram:
  - "Ruimte Adressen, gebouwen en terreinen"
  - "Vastgoed verankering RSGB IMBAG"
  - "Detaillering adressen, gebouwen en terreinen op hoofdlijnen"
  - "Detaillering adressen, gebouwen en terreinen met attributen"
ggm_diagram_ids: []
ggm_definitie: "De kleinste eenheid van gebruik, geen verblijfsobject zijnde, binnen een bij de totstandkoming functioneel en bouwkundig constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden."
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

# GEMMA-waarden
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
bo_definitie: "De kleinste eenheid van gebruik, geen verblijfsobject zijnde, binnen een functioneel en bouwkundig zelfstandige eenheid die direct en duurzaam met de aarde is verbonden."
bo_toelichting: "Aanvulling op Verblijfsobject en Pand: bouwvergunningplichtige gebouwde objecten waarin niet verbleven kan worden in de zin van de BAG, zoals onbemande benzinestations en niet-afsluitbare parkeergarages. De gemeente kan de afbakening verbreden voor centraal beheer, bijvoorbeeld hoogspanningsmasten, GSM-zendmasten en windturbines. Elk overig gebouwd object krijgt precies één (niet-authentiek) adres: een eigen 'overige adresseerbaar object aanduiding' (geen apart BO, zie Onderwerpoverzicht Basisregistraties §RSGBPlus), een bestaande nummeraanduiding met locatie-aanduiding, of een bestaande openbare ruimte met locatie-aanduiding. Wordt alleen geregistreerd voor zover de gemeente dat relevant vindt; bouwvergunningplichtige objecten zonder verblijfsfunctie die al als Inrichtingselement geregistreerd zijn, vallen hierbuiten."
bo_subtypes: []
bo_via_kandidaten: []
bo_synoniemen: []
bo_homoniemen: []
element_tegenhangers: []
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/bag/verblijfsobject|Verblijfsobject]]"
    richting: bidirectioneel
    kardinaliteit:
    beschrijving: "Beide zijn specialisaties van Gebouwd Object (abstract); Verblijfsobject is de BAG-kant, Overig Gebouwd Object vult aan met niet-authentieke gebouwde objecten"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/bag/buurt|Buurt]]"
    richting: van-dit-BO
    kardinaliteit: "1"
    beschrijving: "Ligt in een buurt"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging|Vestiging]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Is hoofd- of nevenlocatie van vestigingen"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/99-kern/woz-deelobject|WOZ-deelobject]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Bestaat uit een of meer WOZ-deelobjecten"
bedrijfsprocessen: []
bedrijfsfuncties: []
---

## BO-criteria toetsing

| Criterium | Oordeel |
|---|---|
| Heeft betekenis binnen het onderwerp | ✅ Vult de gebouwenregistratie aan met objecten die geen verblijfsfunctie hebben maar wel adresvindbaar moeten zijn |
| Herkenbaar voor domeinexperts | ✅ Concrete, herkenbare voorbeelden: tankstations, parkeergarages, zendmasten, windturbines |
| Heeft een eigen bestaan binnen het onderwerp | ✅ Zelfstandig bouwkundig object, los van verblijfsobjecten |
| Kan in meervoud bestaan | ✅ Elke gemeente registreert er meerdere, voor zover relevant geacht |
| Heeft een eigen levenscyclus | ✅ Datum begin/einde geldigheid gebouwd object, status voortgang bouw |
| Heeft relaties met andere concepten | ✅ Buurt, Vestiging, WOZ-deelobject, adresaanduiding |

6/6 — sterke BO. Parallel aan het al bestaande [[Wiki/Bedrijfsobjecten/99-kern/bag/verblijfsobject|Verblijfsobject]]: samen dekken zij de twee specialisaties van de GGM-generalisatie Gebouwd Object.

## Beschrijving

Overig Gebouwd Object is de aanvulling die de gemeente kan registreren náást de BAG-verblijfsobjecten: bouwkundig zelfstandige, duurzaam met de aarde verbonden objecten zonder verblijfsfunctie, zoals onbemande benzinestations en niet-afsluitbare parkeergarages. Gemeenten kunnen de afbakening verbreden tot objecten die primair van belang zijn voor centraal beheer, zoals hoogspanningsmasten, GSM-zendmasten en windturbines.

Registratie is altijd optioneel en gebeurt alleen voor zover de gemeente dat relevant vindt. Elk geregistreerd overig gebouwd object krijgt precies één adres, via een eigen adresaanduiding of gekoppeld aan een bestaande nummeraanduiding/openbare ruimte. Objecten zonder verblijfsfunctie die al generiek als Inrichtingselement zijn geregistreerd, worden niet dubbel als Overig Gebouwd Object vastgelegd.

## Generalisatie

Overig Gebouwd Object is, samen met [[Wiki/Bedrijfsobjecten/99-kern/bag/verblijfsobject|Verblijfsobject]], een specialisatie van de GGM-generalisatie Gebouwd Object, die op haar beurt een specialisatie is van Benoemd Object. Beide abstracte niveaus zijn eerder beoordeeld als "geen eigen BO" (zie [[Wiki/Onderwerpoverzichten/basisregistraties|Onderwerpoverzicht Basisregistraties]] §RSGBPlus). Beide specialisaties delen dezelfde relaties naar Buurt, Kadastrale Onroerende Zaak, WOZ-deelobject en Vestiging.

## GGM-bron

> "De kleinste eenheid van gebruik, geen verblijfsobject zijnde, binnen een bij de totstandkoming functioneel en bouwkundig constructief zelfstandige eenheid die direct en duurzaam met de aarde is verbonden."

- **Entiteit:** OverigGebouwdObject
- **Package:** RSGB Model > Model Kern RSGB
- **Attributen:** overigGebouwdObjectIdentificatie, bouwjaar, indicatiePlanobject (+ attributen van de generalisatie Gebouwd Object: gebouwd object puntgeometrie, gebruiksdoel, oppervlakte, bouwkundige bestemming, bruto inhoud, status voortgang bouw)
- **Matchsterkte:** exact

## Relaties

| Relatie | Richting | BO | Beschrijving | Bron |
|---|---|---|---|---|
| ligt in | → | [[Wiki/Bedrijfsobjecten/99-kern/bag/buurt\|Buurt]] | Via generalisatie Benoemd Object | GGM |
| hoofd-/nevenlocatie van | ← | [[Wiki/Bedrijfsobjecten/99-kern/nhr/vestiging\|Vestiging]] | Via generalisatie Benoemd Object | GGM |
| bestaat uit | → | [[Wiki/Bedrijfsobjecten/99-kern/woz-deelobject\|WOZ-deelobject]] | Via generalisatie Benoemd Object | GGM |

## Bronnen

- [[Wiki/Bronsamenvattingen/Standaarden/rsgb-deel-ii-specificaties]]
