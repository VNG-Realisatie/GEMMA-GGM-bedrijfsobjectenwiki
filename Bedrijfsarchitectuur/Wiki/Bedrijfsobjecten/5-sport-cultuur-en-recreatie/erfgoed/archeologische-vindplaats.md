---
type: bedrijfsobject
naam: Archeologische vindplaats
domein:
- Cultuur
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Vindplaats
ggm_guid: EAID_D7947186_4317_407b_A456_41DF5187E810
ggm_uml_type: Class
ggm_beleidsdomein: Archief
ggm_taakveld: Erfgoed
ggm_diagram:
- Archief Model
ggm_diagram_ids:
- EAID_59241C4B_FD65_484b_88E5_83189334A510
ggm_definitie: Een plek waar men iets gevonden heeft.
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
bo_definitie: Locatie met archeologische waarde waar sporen of resten uit het verleden zijn aangetroffen of verwacht worden.
bedrijfsprocessen:
- Archeologisch advies
- Selectiebesluit
- Bestemmingsplantoetsing
bedrijfsfuncties:
- Erfgoedbeheer
- Ruimtelijke ordening
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologisch-onderzoek|Archeologisch onderzoek]]'
  richting: naar-dit-BO
  kardinaliteit: 0..1
  beschrijving: Een vindplaats hoort bij een archeologisch onderzoek
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/monument|Monument]]'
  richting: van-dit-BO
  kardinaliteit: 0..1
  beschrijving: Een vindplaats kan beschermde status krijgen als monument
---

# Archeologische vindplaats

Locatie met archeologische waarde waar sporen of resten uit het verleden zijn aangetroffen of verwacht worden. Gemeenten zijn bevoegd gezag voor archeologisch onderzoek en beheren een eigen archeologische beleidskaart die aangeeft bij welke ingrepen onderzoek vereist is.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Kernregistratie in het archeologisch erfgoeddomein |
| Herkenbaar voor experts | ✅ | Elke gemeente met archeologisch beleid kent vindplaatsen |
| Eigen bestaan | ✅ | Een vindplaats bestaat onafhankelijk van het onderzoek dat er plaatsvindt |
| Meervoud | ✅ | Utrecht heeft duizenden (verwachte) vindplaatsen |
| Eigen levenscyclus | ✅ | Verwachting → ontdekking → onderzoek → behoud in situ of opgraving |
| Relaties | ✅ | Met onderzoeksproject, vondsten, locatie, eventueel monumentstatus |

## GGM-bron

> **Vindplaats**: Een plek waar men iets gevonden heeft.
> — *GGM v2.5.1, Archeologie (taakveld 5 Sport, Cultuur en Recreatie)*

**Entiteit:** Vindplaats
**Attributen:** projectcode, locatie, vindplaatsOmschrijving, gemeente, datering, begindatering, einddatering, aard, onderzoek, mobilia, depot, documentatie, bibliografie, beschrijving
**Matchsterkte:** sterk

## BO-definitie

Het bedrijfsobject **Archeologische vindplaats** komt overeen met de GGM-entiteit **Vindplaats**. De GGM-definitie ("Een plek waar men iets gevonden heeft") is zeer kort; op bedrijfsniveau gaat het om locaties met (verwachte) archeologische waarde die op de gemeentelijke beleidskaart staan en waarover de gemeente besluiten neemt.

De naamkeuze "Archeologische vindplaats" is specifieker dan het GGM-"Vindplaats" om verwarring te voorkomen met de gelijknamige Archief-entiteit (opslaglocatie van archiefstukken).

> "De nieuwe Archeologische Beleidskaart geeft op basis van de (verwachte) archeologische waarde aan in welke gevallen archeologisch onderzoek vereist is. Met de kaart wordt gestuurd op behoud van een representatieve voorraad Utrechtse archeologie." (bron: [[Wiki/Bronsamenvattingen/Cultuur/erfgoednota-utrecht|Erfgoednota 'Utrechts erfgoed verbindt mensen en tijden']])

De eerdere beoordeling markeerde dit begrip als niet-BO ("nationaal geregistreerd in ARCHIS, niet primair gemeentelijk"). De erfgoednota maakt duidelijk dat gemeenten wél eigen vindplaatsen registreren en er als bevoegd gezag over beslissen.

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Hoort bij onderzoek | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologisch-onderzoek\|archeologisch-onderzoek]] | Vindplaats → Project [1] | Geen |
| Kan beschermd worden | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/monument\|monument]] | *(geen GGM-relatie)* | Toegevoegd: vindplaats kan monumentstatus krijgen |

## Bedrijfsprocessen

- **Archeologisch advies**: adviseren bij voorgenomen werkzaamheden in de ondergrond
- **Selectiebesluit**: beoordeling of op een locatie onderzoek vereist is
- **Bestemmingsplantoetsing**: archeologische waarden meewegen in ruimtelijke plannen

## Bedrijfsfuncties

- Erfgoedbeheer
- Ruimtelijke ordening

## Bronnen

- [[Wiki/Bronsamenvattingen/Cultuur/erfgoednota-utrecht]]
