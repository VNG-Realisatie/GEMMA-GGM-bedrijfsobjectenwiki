---
type: bedrijfsobject
naam: Gemaal
domein:
- Beheer Openbare Ruimte
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Gemaal
ggm_guid: EAID_5D70E69A_2A35_4088_886E_32C0B07275C
ggm_uml_type: Class
ggm_beleidsdomein: Beheer Openbare Ruimte
ggm_taakveld: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
ggm_diagram:
- Hoofdobjecten IMBOR en Geo-object
ggm_diagram_ids: []
ggm_definitie: Een constructie ten behoeve van het verplaatsen van water
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
gemma_definitie: Constructie voor het verpompen van afvalwater, hemelwater of oppervlaktewater binnen het gemeentelijk rioleringssysteem.
relaties:
- type: generalisatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/kunstwerk|Kunstwerk]]'
  richting: van-dit-BO
  kardinaliteit: null
  beschrijving: Gemaal is een specialisatie van Kunstwerk in het GGM
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/overstortconstructie|Overstortconstructie]]'
  richting: bidirectioneel
  kardinaliteit: null
  beschrijving: Gemaal en overstortconstructie zijn onderdelen van hetzelfde rioolstelsel
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/waterobject|Waterobject]]'
  richting: bidirectioneel
  kardinaliteit: null
  beschrijving: Gemaal verpompt water van of naar waterobjecten
bedrijfsprocessen:
- Rioolbeheer
- Gemaalrenovatie
- Kwaliteitsgestuurd beheer
- Storingsbeheer
bedrijfsfuncties:
- Beheer openbare ruimte
- Rioleringsbeheer
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Essentieel voor afvoer van afvalwater en bescherming tegen wateroverlast |
| Is herkenbaar voor domeinexperts | ✅ | Minigemalen, hoofdgemalen, eindgemalen — standaardterminologie in rioleringsbeheer |
| Heeft een eigen bestaan binnen het domein | ✅ | Elk gemaal individueel geregistreerd met type, capaciteit, pompgegevens |
| Kan in meervoud bestaan | ✅ | Circa 700 gemalen in Utrecht (minigemalen, hoofdgemalen, eindgemalen) |
| Heeft een eigen levenscyclus | ✅ | Aanleg → beheer → renovatie → vervanging; renovatieprogramma van 70 minigemalen per jaar |
| Heeft relaties met andere concepten | ✅ | Rioleringsgebied, put, overstortconstructie, waterobject |

Score: 6/6.

## Beschrijving

Een gemaal is een constructie die water verpompt binnen het gemeentelijk rioleringssysteem. Utrecht beheert circa 700 gemalen, onderverdeeld in minigemalen, hoofdgemalen en eindgemalen. De 10 eindgemalen transporteren het afvalwater naar 3 rioolwaterzuiveringsinstallaties (rwzi's).

De gemeente voert een renovatieprogramma uit voor de minigemalen: 70 minigemalen per jaar worden gerenoveerd, naar verwachting gereed in 2029. Het Waterketenregistratiesysteem (WRIS) ondersteunt kwaliteitsgestuurd beheer van gemalen op basis van de feitelijke staat van de constructie.

Bij storingen aan gemalen kan wateroverlast of milieuschade optreden doordat afvalwater niet wordt afgevoerd. Storingsbeheer is daarom een kritisch bedrijfsproces.

## GGM-bron

> "Een constructie ten behoeve van het verplaatsen van water" — [GGM Beheer Openbare Ruimte](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md)

- **Entiteit**: Gemaal
- **Beleidsdomein**: Beheer Openbare Ruimte
- **Taakveld**: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Matchsterkte**: exact
- **Overerving**: Gemaal is een specialisatie van Kunstwerk in het GGM
- **Attributen** (10): aantalBedrijfsaansluitingen, aantalHuisaansluitingen, aantalPompen, bedienaar, effectieveGemaalcapaciteit, hijsinrichting, lanceerinrichting, pompenInSamenloop, type, veiligheidsrooster

## BO-definitie

De GEMMA-definitie specificeert het gemeentelijke perspectief: "verpompen van afvalwater, hemelwater of oppervlaktewater binnen het gemeentelijk rioleringssysteem." De GGM-definitie is breder en spreekt generiek over "het verplaatsen van water."

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| generalisatie | Kunstwerk (GGM) | Gemaal → Kunstwerk | GGM |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/overstortconstructie\|Overstortconstructie]] | bidirectioneel | Beleidsbron |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/waterobject\|Waterobject]] | bidirectioneel | Beleidsbron |

## Bedrijfsprocessen

- **Rioolbeheer**: dagelijks beheer en monitoring van gemalen
- **Gemaalrenovatie**: renovatieprogramma van 70 minigemalen per jaar (gereed 2029)
- **Kwaliteitsgestuurd beheer**: onderhoud op basis van feitelijke staat via WRIS
- **Storingsbeheer**: opvolging en herstel bij storingen om wateroverlast te voorkomen

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
