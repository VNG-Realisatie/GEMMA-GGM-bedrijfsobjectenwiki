---
type: element
naam: Welstandsadvies
onderwerp: [Welstand, VTH]
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

bo_definitie: "Formeel oordeel over de vraag of een bouwplan voldoet aan redelijke eisen van welstand, uitgebracht door de Commissie Welstand en Monumenten of via ambtelijke toetsing."
bo_toelichting:
bo_subtypes: []
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/advies|Advies]]"
    richting: naar-dit-BO
    kardinaliteit:
    beschrijving: "Welstandsadvies is een specialisatie van Advies"
  - type: associatie
    bedrijfsobject: "[[Omgevingsvergunning]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "Welstandsadvies is onderdeel van de vergunningprocedure"
  - type: associatie
    bedrijfsobject: "[[Beschermde Status]]"
    richting: van-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Bij beschermde monumenten/stadsgezichten is maatwerk vereist"
bedrijfsprocessen: [welstandstoetsing, vergunningverlening]
bedrijfsfuncties: [vergunningverlening, ruimtelijke kwaliteit]
---

## BO-criteria toetsing

| Criterium | Score |
|-----------|-------|
| Heeft betekenis binnen het domein | ✅ Centraal concept in de welstandstoetsing |
| Herkenbaar voor domeinexperts | ✅ Elke VTH-medewerker en initiatiefnemer kent dit |
| Eigen bestaan | ✅ Zelfstandig oordeel dat los staat van de vergunningbeslissing |
| Meervoud | ✅ Per bouwaanvraag (minimaal) één advies |
| Eigen levenscyclus | ✅ Uitgebracht, afgegeven, eventueel betwist of herzien |
| Relaties | ✅ Omgevingsvergunning, bouwwerk, commissie, beleidsniveau |

Score: 6/6.

## Beschrijving

Een welstandsadvies is het formele oordeel op een bouwaanvraag over de vraag of het bouwplan voldoet aan "redelijke eisen van welstand." Het advies wordt uitgebracht door de Commissie Welstand en Monumenten (bij complexe of grootschalige plannen, monumenten en beschermde stadsgezichten) of via ambtelijke toetsing (bij veelvoorkomende kleinere bouwwerken).

Het advies wordt getoetst aan:
- De **gebiedsgerichte criteria** uit deel A van de welstandsnota, gekoppeld aan het beleidsniveau (Open: 9 criteria, Respect: 13 criteria, Behoud: 17 criteria)
- De **welstandscriteria** uit deel B voor veelvoorkomende kleine bouwwerken (dakkapellen, erkers, erfafscheidingen etc.)

Bij een negatief advies moet de motivatie worden onderbouwd vanuit de welstandscriteria. Het College van B&W kan afwijken van het advies, mits gemotiveerd.

## Procesbron

Het welstandsadvies ontstaat in het **omgevingsvergunningproces**. Na ontvangst van een aanvraag omgevingsvergunning wordt beoordeeld of een welstandstoets nodig is (kanbepaling). Het advies is een verplicht onderdeel van de vergunningprocedure voor vergunningplichtige bouwwerken, tenzij het bouwwerk welstandsvrij is verklaard.

Zie [[Wiki/Bronsamenvattingen/Welstand/welstandsnota-utrechtse-aanpak|Welstandsnota De schoonheid van Utrecht — De Utrechtse aanpak (Deel A)]] voor het toetsingskader.

## GGM-relatie

Geen directe GGM-match. De GGM-entiteit **Bevinding** (beleidsdomein VTH) is het meest verwant: "de uitkomst van een waarneming of onderzoek die aangeeft wat is geconstateerd bij beoordeling of inspectie." Een welstandsadvies is echter specifieker — het is een formeel advies van een commissie of ambtelijk toetser, niet een generieke inspectieconstatering.

**Classificatie:** procesobject (artefact dat in het vergunningproces ontstaat). Het GGM modelleert het vergunningproces via VTHzaak en Bevinding, maar heeft geen specifieke entiteit voor het welstandsadvies.

## Generalisatie

[[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/advies|Advies]] → **Welstandsadvies**

Welstandsadvies is een specialisatie van het generieke BO [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/advies|Advies]] (formeel oordeel van een adviescollege of externe partij op verzoek van een bestuursorgaan). Wat dit niveau onderscheidt: de toetsing is specifiek gericht op redelijke eisen van welstand voor bouwplannen, uitgebracht door de Commissie Welstand en Monumenten of via ambtelijke toetsing, en staat in directe relatie tot het omgevingsvergunningproces.

## Relaties

| Relatie | Richting | Kardinaliteit | Bron |
|---------|----------|---------------|------|
| [[Wiki/Bedrijfsobjecten/10-dienstverlening/dienstverlening/advies\|Advies]] | Advies → Welstandsadvies | generalisatie | — |
| [[Omgevingsvergunning]] | Welstandsadvies → Omgevingsvergunning | 0..1 | Beleidsbron |
| [[Beschermde Status]] | Welstandsadvies → Beschermde Status | 0..* | Beleidsbron |

## Bedrijfsprocessen

- Welstandstoetsing (ambtelijk of via commissie)
- Vergunningverlening (omgevingsvergunning)

## Bedrijfsfuncties

- Vergunningverlening
- Ruimtelijke kwaliteit


## Bronnen

- [[Wiki/Bronsamenvattingen/Welstand/welstandsnota-utrechtse-aanpak]]

## Terugmelding GGM

Het welstandsadvies is een procesobject; procesobjecten zijn in het GGM niet compleet gedekt. De bestaande GGM-entiteit Bevinding is generiek en dekt het concept niet volledig.
