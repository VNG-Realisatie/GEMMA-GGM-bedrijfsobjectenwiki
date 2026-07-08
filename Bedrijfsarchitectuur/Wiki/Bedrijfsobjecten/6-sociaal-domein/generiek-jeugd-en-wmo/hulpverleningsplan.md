---
type: element
naam: Hulpverleningsplan
onderwerp: [Maatschappelijke Ondersteuning]
archimate_type: business-object
grondslag: procesobject

ggm_entiteit: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: ""
ggm_taakveld: ""
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie: ""
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: ""
ggm_gemma_guid: ""
ggm_gemma_definitie: ""
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: ""
ggm_gemma_url: ""
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

bo_definitie: "Verplicht plan voor de verlening van jeugdhulp of de uitvoering van een kinderbeschermingsmaatregel, in samenspraak met de jeugdige en ouders opgesteld."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "betreft jeugdige/ouder"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking|Beschikking]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "volgt uit beschikking"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening|Voorziening]]"
    richting: van-dit-BO
    kardinaliteit: "1..*"
    beschrijving: "beschrijft in te zetten voorzieningen"
bedrijfsprocessen: [jeugdhulp verlenen, kinderbeschermingsmaatregel uitvoeren]
bedrijfsfuncties: [toegang sociaal domein, jeugdhulpverlening]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in gemeentelijk domein | ✅ | Wettelijk verplicht document (Jeugdwet art. 4.1.3) |
| Besproken op bestuurlijk niveau | ✅ | Aantallen plannen in verantwoording sociaal domein |
| Vastgelegd in systemen | ✅ | Geregistreerd in jeugdhulp-applicatie met datum en inhoud |
| Eigen attributen | ✅ | Datum vaststelling, betrokkenen, type, inhoud, instemming |
| Relaties met andere objecten | ✅ | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]], [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]], [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening\|Voorziening]] |
| Levenscyclus | ✅ | Opgesteld → vastgesteld → gewijzigd → afgerond |

## Beschrijving

Het hulpverleningsplan is het centrale document in de jeugdhulpketen. Het beschrijft welke jeugdhulp wordt ingezet, met welk doel, en hoe de jeugdige en ouders daarbij betrokken zijn. De Jeugdwet schrijft voor dat het plan "zoveel mogelijk in samenspraak met de jeugdige en de ouders is opgesteld en is afgestemd op de behoeften van de jeugdige" (art. 4.1.3 lid 2).

Het plan moet binnen zes weken worden vastgesteld nadat is besloten geen familiegroepsplan op te stellen. Bij pleegzorg is instemming van de pleegouder vereist voor het deel dat diens rol en begeleiding beschrijft.

De wet kent twee varianten: het **hulpverleningsplan** (bij jeugdhulpverlening) en het **plan van aanpak** (bij kinderbeschermingsmaatregel of jeugdreclassering). Beide volgen dezelfde wettelijke eisen.

## Subtypes

Herkende specialisaties van Hulpverleningsplan. Gevonden in de Jeugdwet. Geen apart BO.

- **Familiegroepsplan** — plan opgesteld door ouders samen met bloedverwanten en sociaal netwerk; moet als eerste optie worden aangeboden (art. 4.1.2)
- **Plan van aanpak** — variant bij uitvoering kinderbeschermingsmaatregel of jeugdreclassering (art. 1.1, 4.1.3)

## Procesbron

Het hulpverleningsplan ontstaat in het proces van jeugdhulpverlening. De wettelijke grondslag is de Jeugdwet, die het plan verplicht stelt bij elke vorm van jeugdhulp tenzij een familiegroepsplan wordt opgesteld.

> "Indien afgezien wordt van het opstellen van een familiegroepsplan omvat het uitvoeren van artikel 4.1.1 het werken op basis van een plan dat zoveel mogelijk in samenspraak met de jeugdige en de ouders is opgesteld en dat is afgestemd op de behoeften van de jeugdige." (art. 4.1.3 lid 2)

## Relaties

| Gerelateerd BO | Relatie | Richting | Bron |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | betreft jeugdige/ouder | naar dit BO | Jeugdwet art. 4.1.3 |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/beschikking\|Beschikking]] | volgt uit beschikking | naar dit BO | Jeugdwet art. 2.3, 2.9 |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening\|Voorziening]] | beschrijft voorzieningen | van dit BO | Jeugdwet art. 4.1.3 |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/jeugdbescherming-en-reclassering/kinderbeschermingsmaatregel\|Kinderbeschermingsmaatregel]] | uitvoering via plan van aanpak | naar dit BO | Jeugdwet art. 4.1.3 lid 1 |

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/jeugdwet]]

## Terugmelding GGM

Het GGM modelleert het hulpverleningsplan niet als aparte entiteit in het domein Generiek Jeugd en Wmo. Het attribuut `datumPlanVastgesteld` op AOM_AanvraagWmoJeugd verwijst ernaar, maar het plan zelf ontbreekt als objecttype. In het domein Schuldhulpverlening bestaat wel een PlanVanAanpak-entiteit. Signalering: het hulpverleningsplan is een zelfstandig registratieobject dat in het GGM ontbreekt voor het jeugd/wmo-domein.
