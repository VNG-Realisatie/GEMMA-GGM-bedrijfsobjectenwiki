---
type: element
naam: Advies
onderwerp: [Informatiesamenleving, Dienstverlening]
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

bo_definitie: "Formeel oordeel of aanbeveling van een adviescollege, commissie of externe partij over een ontwerp, voornemen of ander onderwerp, uitgebracht op verzoek van het bestuursorgaan."
bo_toelichting:
bo_subtypes: []
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/welstandsadvies|Welstandsadvies]]"
    richting: van-dit-BO
    kardinaliteit:
    beschrijving: Welstandsadvies is een specialisatie van Advies, specifiek voor de toetsing van bouwplannen aan redelijke eisen van welstand
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/besluit|Besluit]]"
    richting: van-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Een advies kan de besluitvorming over een ontwerp of aanvraag onderbouwen
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document|Document]]"
    richting: van-dit-BO
    kardinaliteit: "1..1"
    beschrijving: Een advies wordt vastgelegd in een document
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/bibob-toets|Bibob-toets]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: Het Bibob-advies van het Landelijk Bureau Bibob is een specialisatie van Advies, uitgebracht als onderdeel van een Bibob-toets
bedrijfsprocessen: [Adviesaanvraag en -uitbrenging, Actieve openbaarmaking]
bedrijfsfuncties: [Beleidsontwikkeling, Vergunningverlening]
---

# Advies

## BO-criteria toetsing

| Criterium | Toetsing |
|---|---|
| Identificeerbaar | Ja — elk advies is een afzonderlijk uitgebracht oordeel met eigen adviesvrager, adviesorgaan en datum |
| Eigen attributen | Ja — adviesvraag, adviserende partij, datum, inhoud/oordeel, eventuele motivering |
| Levenscyclus | Ja — adviesaanvraag → opstellen → uitbrengen → (evt.) gebruikt in besluitvorming → actief openbaar gemaakt |
| Gemeentelijk eigendom | Ja — de gemeente vraagt het advies of ontvangt het als grondslag voor eigen besluitvorming |
| Wettelijke grondslag | Ja — Wet open overheid art. 3.3 lid 2 sub e (actieve openbaarmaking van adviezen en adviesaanvragen) |
| Registratieverplichting | Ja — adviezen van adviescolleges/-commissies en de bijbehorende adviesaanvraag moeten actief openbaar worden gemaakt, tenzij het individuele gevallen betreft |

Score: 6/6 criteria.

## Beschrijving

Een advies is het formele oordeel of de aanbeveling die een adviescollege, commissie of externe partij uitbrengt op verzoek van een bestuursorgaan — over een ontwerp van wet- of regelgeving, een voorgenomen besluit, of een ander onderwerp. Het advies staat los van het besluit dat er eventueel op volgt: het onderbouwt de besluitvorming maar is zelf geen besluit.

De Woo onderscheidt twee soorten adviezen die actief openbaar moeten worden gemaakt (art. 3.3 lid 2 sub e): adviezen over ontwerpen van wet- en regelgeving (met de bijbehorende adviesaanvraag), en overige adviezen van adviescolleges of -commissies (eveneens met de adviesaanvraag), met uitzondering van adviezen die op individuele gevallen betrekking hebben. Voorbeelden van adviesorganen die de handreiking noemt: de Raad van State, adviescolleges, specifieke autoriteiten (zoals de Autoriteit Persoonsgegevens, de Raad voor de Rechtspraak, het [[Wiki/Actoren/acoi|ACOI]] en de VNG) en externe partijen zoals commerciële adviesbureaus.

## Specialisaties

Herkende specialisaties van Advies met een eigen BO-pagina:

| Specialisatie | Omschrijving | Bron |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/welstandsadvies\|Welstandsadvies]] | Formeel oordeel over de vraag of een bouwplan voldoet aan redelijke eisen van welstand, uitgebracht door de Commissie Welstand en Monumenten of via ambtelijke toetsing | Welstandsnota De schoonheid van Utrecht |

## Procesbron

Het advies ontstaat in het proces van beleids- of besluitvoorbereiding, wanneer een bestuursorgaan een adviescollege, commissie of externe partij om een oordeel vraagt. Zie [[Wiki/Bronsamenvattingen/Informatiesamenleving/wet-open-overheid-actieve-openbaarmaking|Wet open overheid — actieve openbaarmaking]], art. 3.3 lid 2 sub e.

## Relaties

| Relatie | Bedrijfsobject | Richting | Beschrijving |
|---|---|---|---|
| generalisatie | [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/vth/welstandsadvies\|Welstandsadvies]] | → | Welstandsadvies is een specialisatie van Advies |
| associatie | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/besluit\|Besluit]] | → | Onderbouwt eventuele besluitvorming |
| associatie | [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/document\|Document]] | → | Vastgelegd in een document |
| associatie | [[Wiki/Bedrijfsobjecten/1-veiligheid-en-vergunningen/openbare-orde-en-veiligheid/bibob-toets\|Bibob-toets]] | ← | Bibob-advies (uitgebracht door het [[Wiki/Actoren/landelijk-bureau-bibob\|Landelijk Bureau Bibob]]) is een specialisatie van Advies |

## Bronnen
- [[Wiki/Bronsamenvattingen/Informatiesamenleving/wet-open-overheid-actieve-openbaarmaking]]
- [[Wiki/Bronsamenvattingen/Openbare Orde en Veiligheid/wet-bibob-bwbr0013798]]

## Terugmelding GGM

GGM-hiaat: het GGM bevat geen generieke entiteit voor Advies als procesobject van beleids-/besluitvorming (de entiteit InformatieEnAdvies binnen Schuldhulpverlening is een ander, domeinspecifiek concept). Advies is vergelijkbaar met [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/besluit|Besluit]], dat wel een GGM-entiteit heeft (RGBZPlus).

Teruggemeld in [[Wiki/Analyses/ggm-terugmeldingen]].
