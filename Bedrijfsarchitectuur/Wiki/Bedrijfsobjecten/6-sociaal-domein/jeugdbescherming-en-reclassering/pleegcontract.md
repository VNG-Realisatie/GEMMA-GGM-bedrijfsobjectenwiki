---
type: bedrijfsobject
naam: Pleegcontract
onderwerp: [Maatschappelijke Ondersteuning]
archimate_type: contract
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

bo_definitie: "Overeenkomst tussen pleegzorgaanbieder en pleegouder over de verzorging, opvoeding en begeleiding van een jeugdige in het kader van pleegzorg."
bo_toelichting: ''
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client|Client]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "betreft jeugdige"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening|Voorziening]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "betreft pleegzorg als voorziening"
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/hulpverleningsplan|Hulpverleningsplan]]"
    richting: naar-dit-BO
    kardinaliteit: "0..1"
    beschrijving: "sluit aan op hulpverleningsplan"
bedrijfsprocessen: [pleegzorg organiseren, pleegouder screenen en contracteren]
bedrijfsfuncties: [jeugdhulpverlening, pleegzorgbeheer]
---

## BO-criteria toetsing

| Criterium | Voldoet | Toelichting |
|---|---|---|
| Herkenbaar in gemeentelijk domein | ✅ | Wettelijk verplicht contract (Jeugdwet art. 5.1); gemeente bekostigt pleegzorg |
| Besproken op bestuurlijk niveau | ✅ | Aantallen pleegzorgplaatsingen in raadsinformatie |
| Vastgelegd in systemen | ✅ | Geregistreerd bij pleegzorgaanbieder; gemeente heeft zicht via toewijzing |
| Eigen attributen | ✅ | Pleegouder, jeugdige, pleegzorgaanbieder, begin-/einddatum, afspraken, verklaring van geen bezwaar |
| Relaties met andere objecten | ✅ | [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]], [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening\|Voorziening]], [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/hulpverleningsplan\|Hulpverleningsplan]] |
| Levenscyclus | ✅ | Screening → sluiting → wijziging → opzegging/beëindiging |

## Beschrijving

Het pleegcontract is de overeenkomst tussen een pleegzorgaanbieder en een pleegouder. Het bevat afspraken over de verzorging en opvoeding van een specifieke jeugdige en over de begeleiding die de pleegouder ontvangt van de pleegzorgaanbieder (art. 5.2).

De gemeente sluit het contract niet zelf — dat doet de pleegzorgaanbieder — maar bekostigt de pleegzorg via de reguliere toewijzingsketen en is verantwoordelijk voor een toereikend pleegzorgaanbod. De wet stelt strenge voorwaarden aan het pleegcontract: de pleegouder moet minimaal 21 jaar zijn, een selectietraject doorlopen, en beschikken over een verklaring van geen bezwaar van de Raad voor de Kinderbescherming (art. 5.1).

Bij pleegoudervoogdij beperkt de begeleiding zich tot minimaal één gesprek per jaar (art. 5.2 lid 2). Een jeugdige van 18 jaar of ouder kan de pleegzorg zelf beëindigen (art. 5.5).

## Procesbron

Het pleegcontract ontstaat in het pleegzorgproces. De pleegzorgaanbieder sluit het contract nadat de pleegouder aan alle voorwaarden voldoet en beoordeeld is dat de jeugdige in het gezin kan worden geplaatst.

> "De pleegzorgaanbieder sluit een pleegcontract met een pleegouder indien deze voldoet aan de volgende voorwaarden: a. de pleegouder heeft ten minste de leeftijd van eenentwintig jaar bereikt" (art. 5.1 lid 1)

> "Het pleegcontract bevat in ieder geval afspraken omtrent de wijze waarop de verzorging en opvoeding van de desbetreffende jeugdige door de pleegouder worden uitgevoerd en de begeleiding die zij daarbij ontvangen van de pleegzorgaanbieder." (art. 5.2 lid 1)

## Relaties

| Gerelateerd BO | Relatie | Richting | Bron |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/sociaal-domein-generiek/client\|Client]] | betreft jeugdige | naar dit BO | Jeugdwet art. 5.1 |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/voorziening\|Voorziening]] | pleegzorg als voorzieningsoort | naar dit BO | Jeugdwet art. 5.1 |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/hulpverleningsplan\|Hulpverleningsplan]] | sluit aan op hulpverleningsplan | naar dit BO | Jeugdwet art. 4.1.3 lid 3, 6 |
| [[Wiki/Bedrijfsobjecten/6-sociaal-domein/generiek-jeugd-en-wmo/toewijzing\|Toewijzing]] | gemeente wijst pleegzorg toe | gerelateerd | Jeugdwet art. 2.3 |

## Bronnen

- [[Wiki/Bronsamenvattingen/Maatschappelijke Ondersteuning/jeugdwet]]

## Terugmelding GGM

Het GGM modelleert geen entiteit voor het pleegcontract. Pleegzorg wordt in het GGM alleen als Voorzieningsoort benaderd, niet als eigen objectstructuur. Het pleegcontract is een zelfstandig registratieobject met eigen attributen (partijen, voorwaarden, verklaring van geen bezwaar) en levenscyclus.
