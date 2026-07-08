---
type: bedrijfsobject
naam: Overstortconstructie
domein:
- Beheer Openbare Ruimte
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Overstortconstructie
ggm_guid: EAID_845EC5C5_7B96_4999_9659_5617436D269
ggm_uml_type: Class
ggm_beleidsdomein: Beheer Openbare Ruimte
ggm_taakveld: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
ggm_diagram:
- Hoofdobjecten IMBOR en Geo-object
ggm_diagram_ids: []
ggm_definitie: Een constructie voorzien van een overstortdrempel met een ontworpen drempelbreedte en -hoogte.
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
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Overstortconstructie** als directe tegenhanger.
bo_definitie: "Een constructie voorzien van een overstortdrempel met een ontworpen drempelbreedte en -hoogte."
bo_toelichting: ''
bo_relaties:
- type: generalisatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/kunstwerk|Kunstwerk]]'
  richting: van-dit-BO
  kardinaliteit: null
  beschrijving: Overstortconstructie is een specialisatie van Kunstwerk in het GGM
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/bergingsbassin|Bergingsbassin]]'
  richting: bidirectioneel
  kardinaliteit: 1..*
  beschrijving: Achter de belangrijkste overstorten staan bergbezinkbassins
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/waterobject|Waterobject]]'
  richting: bidirectioneel
  kardinaliteit: null
  beschrijving: Overstortconstructie loost verdund afvalwater op oppervlaktewater
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/gemaal|Gemaal]]'
  richting: bidirectioneel
  kardinaliteit: null
  beschrijving: Gemaal en overstortconstructie zijn onderdelen van hetzelfde rioolstelsel
bedrijfsprocessen:
- Rioolbeheer
- Monitoring overstorten
- Waterkwaliteitsbeheer
bedrijfsfuncties:
- Beheer openbare ruimte
- Rioleringsbeheer
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Veiligheidsklep van het rioolstelsel; directe impact op waterkwaliteit en zwemwaterkwaliteit |
| Is herkenbaar voor domeinexperts | ✅ | Overstort, gemengde overstort — standaardterminologie in rioleringsbeheer |
| Heeft een eigen bestaan binnen het domein | ✅ | Elke overstortconstructie individueel geregistreerd met drempelbreedte, drempelniveau en type |
| Kan in meervoud bestaan | ✅ | 156 gemengde overstorten in Utrecht |
| Heeft een eigen levenscyclus | ✅ | Aanleg → monitoring → onderhoud → eventuele opheffing bij ontvlechting gemengd stelsel |
| Heeft relaties met andere concepten | ✅ | Bergingsbassin, waterobject, rioleringsgebied, gemaal |

Score: 6/6.

## Beschrijving

Een overstortconstructie functioneert als veiligheidsklep in het gemengde rioolstelsel. Bij zware neerslag loost de constructie verdund afvalwater via een overstortdrempel op het oppervlaktewater, om te voorkomen dat het rioolstelsel overbelast raakt en water op straat komt.

Utrecht telt 156 gemengde overstorten. De lozing van verdund afvalwater op oppervlaktewater beïnvloedt de waterkwaliteit en kan gevolgen hebben voor de zwemwaterkwaliteit. Achter de 18 belangrijkste overstorten zijn bergbezinkbassins geplaatst om de milieu-impact te beperken.

Het doel is vermindering van het aantal overstorten door ontvlechting van het gemengde rioolstelsel: bij rioolvervanging wordt het gemengde stelsel gesplitst in een gescheiden hemelwater- en vuilwaterstelsel.

## GGM-bron

> "Een constructie voorzien van een overstortdrempel met een ontworpen drempelbreedte en -hoogte." — [GGM Beheer Openbare Ruimte](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md)

- **Entiteit**: Overstortconstructie
- **Beleidsdomein**: Beheer Openbare Ruimte
- **Taakveld**: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Matchsterkte**: exact
- **Overerving**: Overstortconstructie is een specialisatie van Kunstwerk in het GGM
- **Attributen** (7): bassin, drempelbreedte, drempelniveau, klep, type, vormDrempel, waking

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| generalisatie | Kunstwerk (GGM) | Overstortconstructie → Kunstwerk | GGM |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/bergingsbassin\|Bergingsbassin]] | bidirectioneel | Beleidsbron |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/waterobject\|Waterobject]] | bidirectioneel | Beleidsbron |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/gemaal\|Gemaal]] | bidirectioneel | Beleidsbron |

## Bedrijfsprocessen

- **Rioolbeheer**: beheer van overstortconstructies als onderdeel van het rioolstelsel
- **Monitoring overstorten**: meten van overstortfrequentie en -volume
- **Waterkwaliteitsbeheer**: beheersing van de impact van overstorten op oppervlaktewater

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
