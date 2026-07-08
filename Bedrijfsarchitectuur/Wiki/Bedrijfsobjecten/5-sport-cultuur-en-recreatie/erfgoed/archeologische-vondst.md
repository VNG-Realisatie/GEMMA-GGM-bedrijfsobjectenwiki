---
type: bedrijfsobject
naam: Archeologische vondst
domein:
- Cultuur
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Vondst
ggm_guid: EAID_F8283401_70F8_41b8_A97C_32A9074AD4B1
ggm_uml_type: Class
ggm_beleidsdomein: Archeologie
ggm_taakveld: Erfgoed
ggm_diagram:
- Erfgoed: Archeologie Domeinmodel
ggm_diagram_ids:
- EAID_C91D2D84_69FA_4320_BFE0_F10EFEB8F49B
ggm_definitie: Overblijfsel, voorwerp of ander spoor van menselijke aanwezigheid in het verleden afkomstig van een archeologisch monument
ggm_toelichting: ''
ggm_synoniemen: Archeologische vondst
ggm_herkomst: ''
ggm_gemma_naam: Vondst
ggm_gemma_guid: fc805177-e231-40eb-8f59-0fb3bdc896a1
ggm_gemma_definitie: Overblijfsel, voorwerp of ander spoor van menselijke aanwezigheid in het verleden afkomstig van een archeologisch monument
ggm_gemma_toelichting: ''
ggm_gemma_synoniemen: Archeologische vondst
ggm_gemma_type: business-object
ggm_gemma_url: https://gemmaonline.nl/index.php/GEMMA/id-fc805177-e231-40eb-8f59-0fb3bdc896a1
ggm_gemma_bron: ''
ggm_gemma_alternate_name: ''
analyse_ggm_dekking: |
  Dit BO is de hernoeming van GGM-entiteit **Vondst**. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Artefact** (detail) — Detailgegeven
  - **Artefactsoort** (classificatie) — Typering/referentietabel
  - **Spoor** (detail) — Detailgegeven
  - **Vulling** (detail) — Detailgegeven
bo_definitie: Archeologisch overblijfsel of voorwerp dat door de gemeente is aangetroffen bij onderzoek en wordt beheerd in het gemeentelijk depot.
bo_toelichting: ''
bedrijfsprocessen:
- Archeologisch onderzoek
- Depotbeheer
- Publieksactiviteiten
bedrijfsfuncties:
- Erfgoedbeheer
- Collectiebeheer
bo_relaties:
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologische-vindplaats|Archeologische vindplaats]]'
  richting: van-dit-BO
  kardinaliteit: 0..1
  beschrijving: Een vondst is aangetroffen op een vindplaats (via Project/Put/Vulling in GGM)
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologisch-onderzoek|Archeologisch onderzoek]]'
  richting: van-dit-BO
  kardinaliteit: 1
  beschrijving: Een vondst komt voort uit een onderzoeksproject (via Put/Vlak/Spoor/Vulling in GGM)
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/musea/museumobject|Museumobject]]'
  richting: van-dit-BO
  kardinaliteit: 0..1
  beschrijving: Een vondst kan worden opgenomen in een museale collectie
---

# Archeologische vondst

Overblijfsel of voorwerp uit het verleden dat bij archeologisch onderzoek is aangetroffen. De gemeente beheert vondsten en bijbehorende documentatie in een eigen depot en stelt ze waar mogelijk tentoon nabij de vindplaats.

## BO-criteria toetsing

| Criterium | Van toepassing | Toelichting |
|---|---|---|
| Betekenis binnen domein | ✅ | Vondsten vormen "het geheugen van de stad" |
| Herkenbaar voor experts | ✅ | Kernbegrip in archeologisch werkveld |
| Eigen bestaan | ✅ | Fysiek object dat onafhankelijk van het onderzoeksproces bestaat |
| Meervoud | ✅ | Gemeente beheert collectie uit 50 jaar onderzoek |
| Eigen levenscyclus | ✅ | Aantreffen → documenteren → conserveren → bewaren/exposeren |
| Relaties | ✅ | Met vindplaats, onderzoeksproject, depot, eventueel museumcollectie |

## GGM-bron

> **Vondst**: Overblijfsel, voorwerp of ander spoor van menselijke aanwezigheid in het verleden afkomstig van een archeologisch monument
> — *GGM v2.5.1, Archeologie (taakveld 5 Sport, Cultuur en Recreatie)*

**Entiteit:** Vondst
**Attributen:** projectCD, vondstnummer, putnummer, vlaknummer, spoornummer, vullingnummer, omstandigheden, omschrijving, key, keyVulling, datum, XCoordinaat, YCoordinaat
**Matchsterkte:** exact

### Aggregatie

In het GGM is Vondst de vondstcontext (locatie, omstandigheden) en bevat het Artefacten (de fysieke objecten). Op bedrijfsniveau spreekt de gemeente over "vondsten" als geheel — de context en de objecten samen. Het GGM-detailniveau (Vondst → Artefact → Artefactsoort, en de opgravinghiërarchie Put → Vlak → Spoor → Vulling → Vondst) is te granulair voor de bedrijfsarchitectuur. De GGM-entiteit **Artefact** (EAID_2C230EE7) is daarom geaggregeerd in dit BO.

> "De gemeente beheert de vondsten en documentatie van 50 jaar archeologisch en bouwhistorisch onderzoek door de gemeente Utrecht. Dit materiaal is meestal het enige materiële wat resteert na onderzoek en vormt dus in veel opzichten 'het geheugen van de stad'." (bron: [[Wiki/Bronsamenvattingen/Cultuur/erfgoednota-utrecht|Erfgoednota 'Utrechts erfgoed verbindt mensen en tijden']])

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Relatie | Bedrijfsobject | GGM-bron | Afwijking |
|---|---|---|---|
| Aangetroffen op | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologische-vindplaats\|archeologische-vindplaats]] | Vindplaats → Project → Put → Vulling → Vondst (indirect) | Ingekort: directe relatie op bedrijfsniveau |
| Voortgekomen uit | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/erfgoed/archeologisch-onderzoek\|archeologisch-onderzoek]] | Project → Put → Vlak → Spoor → Vulling → Vondst (indirect) | Ingekort: directe relatie op bedrijfsniveau |
| Kan museumobject worden | [[Wiki/Bedrijfsobjecten/5-sport-cultuur-en-recreatie/musea/museumobject\|museumobject]] | *(geen directe GGM-relatie)* | Toegevoegd: vondst kan naar museale collectie |

## Bedrijfsprocessen

- **Archeologisch onderzoek**: vondsten worden gedocumenteerd tijdens opgraving
- **Depotbeheer**: bewaren, conserveren en ontsluiten van vondsten
- **Publieksactiviteiten**: vondsten tentoonstellen nabij vindplaats (Museum Hoge Woerd, bibliotheken, scholen)

## Bedrijfsfuncties

- Erfgoedbeheer
- Collectiebeheer

## Bronnen

- [[Wiki/Bronsamenvattingen/Cultuur/erfgoednota-utrecht]]
