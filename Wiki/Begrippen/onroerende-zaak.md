---
type: begrip
naam: onroerende zaak
definitie: Grond, gebouw of combinatie daarvan dat als zelfstandig object wordt gewaardeerd onder de Wet WOZ en als grondslag dient voor belastingheffing.
begripstype: object
abstractieniveau: operationeel
domein: [Belastingen]
synoniemen: [onroerend goed, WOZ-object, pand]
bronnen: ["[[Sources/Onderwerpen VNG/Belastingen/raadgever-woz]]"]
ggm_entiteit: WOZ-object (RSGBPlus, taakveld 99 Kern)
status: concept
---

# Onroerende zaak

Het fysieke object — grond, gebouw of combinatie — waarvan de gemeente jaarlijks de [[woz-waarde]] vaststelt. De onroerende zaak is het heffingsobject voor de OZB en de basis voor andere heffingen die de WOZ-waarde als [[heffingsmaatstaf]] gebruiken.

## Context

Onder de Wet WOZ verzamelt de gemeente per onroerende zaak gegevens als oppervlakte, bouwtype, bouwjaar, onderhoud, omgevingsfactoren, verkoop- en huurcijfers. Deze gegevens vormen de basis voor het taxatiemodel en worden ook gebruikt door veiligheidsdiensten, brandweer en geo-diensten.

De WOZ-objectafbakening bepaalt wat als één zelfstandig object geldt. Dit is niet altijd gelijk aan een kadastraal perceel of een BAG-verblijfsobject.

## Relaties

- Wordt gewaardeerd op [[woz-waarde]]
- Waarde wordt bekendgemaakt via [[woz-beschikking]]
- Is heffingsobject voor [[belastingaanslag]] (OZB)
- Eigenaar/gebruiker is de [[belastingplichtige]]
- Toezicht op waardering door de [[waarderingskamer]]

## Afbakening

- Niet hetzelfde als een kadastraal perceel (BRK) — de WOZ-objectafbakening is een eigenstandige afbakening
- Niet hetzelfde als een verblijfsobject (BAG) — een WOZ-object kan meerdere verblijfsobjecten omvatten
- Roerende zaken (auto's, inventaris) vallen buiten de WOZ

## GGM

**Match:** GGM-entiteit "WOZ-object" in RSGBPlus (taakveld 99 Kern, herkomst BRWOZ). Attributen: WOZObjectnummer, geometrieWOZObject, grondoppervlakte, gebruikscode, soortobjectcode, vastgesteldeWaarde. Zie bedrijfsobject [[woz-object]].

Het GGM kent ook "KadastraleOnroerendeZaak" (BRK) voor de kadastrale registratie. De WOZ-objectafbakening is een eigenstandige afbakening die niet altijd samenvalt met kadastrale percelen.
