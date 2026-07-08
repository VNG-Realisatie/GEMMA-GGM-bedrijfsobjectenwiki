---
type: bedrijfsobject
naam: Kolk
domein:
- Beheer Openbare Ruimte
archimate_type: business-object
grondslag: ggm-entiteit
ggm_entiteit: Kolk
ggm_guid: EAID_E6AFE8F7_95A7_4A0C_A6E8_F6D2091FB8B
ggm_uml_type: Class
ggm_beleidsdomein: Beheer Openbare Ruimte
ggm_taakveld: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
ggm_diagram:
- Hoofdobjecten IMBOR en Geo-object
ggm_diagram_ids: []
ggm_definitie: 'Een reservoir bestemd voor de opvang van hemelwater afkomstig van erop aangesloten oppervlakken, het laten bezinken van in dit water meegevoerde bezinkbare stoffen en de afvoer van dit water
  naar een rioolstelsel of naar de ondergrond. Synoniemen: Afvoerput'
ggm_toelichting: ''
ggm_synoniemen: Afvoerput
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
  Dit BO heeft de GGM-entiteit **Kolk** als directe tegenhanger.
bo_definitie: "Een reservoir bestemd voor de opvang van hemelwater afkomstig van erop aangesloten oppervlakken, het laten bezinken van in dit water meegevoerde bezinkbare stoffen en de afvoer van dit water naar een rioolstelsel of naar de ondergrond. Synoniemen: Afvoerput"
bo_toelichting: ''
bo_relaties:
- type: generalisatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioolput|Rioolput]]'
  richting: van-dit-BO
  kardinaliteit: null
  beschrijving: Kolk is een specialisatie van Put in het GGM
- type: associatie
  bedrijfsobject: '[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/waterobject|Waterobject]]'
  richting: bidirectioneel
  kardinaliteit: null
  beschrijving: Kolken voeren hemelwater af naar oppervlaktewater of riool
bedrijfsprocessen:
- Rioolbeheer
- Kolkreiniging
- Amfibievriendelijk maken kolken
bedrijfsfuncties:
- Beheer openbare ruimte
- Rioleringsbeheer
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Eerste schakel in de hemelwaterinzameling; essentieel voor voorkomen wateroverlast op straat |
| Is herkenbaar voor domeinexperts | ✅ | Straatkolk, afvoerput — standaardterminologie in rioleringsbeheer |
| Heeft een eigen bestaan binnen het domein | ✅ | Elke kolk individueel geregistreerd met type, bereikbaarheid en risicogebied |
| Kan in meervoud bestaan | ✅ | Duizenden straatkolken verspreid over het gemeentelijk wegennet |
| Heeft een eigen levenscyclus | ✅ | Aanleg → reiniging → vervanging; bij rioolvervanging worden kolken opnieuw aangesloten |
| Heeft relaties met andere concepten | ✅ | Rioleringsgebied, waterobject, rioolstelsel |

Score: 6/6.

## Beschrijving

Een kolk (straatkolk, afvoerput) is de eerste schakel in de hemelwaterinzameling. Straatkolken vangen regenwater op van verharde oppervlakken en voeren dit af naar het rioolstelsel of de ondergrond.

Utrecht maakt nieuwe kolken standaard amfibievriendelijk om te voorkomen dat kleine dieren (met name padden en kikkers) erin vallen en verdrinken. Bij rioolvervanging worden kolken aangesloten op een gescheiden hemelwaterriool in plaats van het gemengde riool, als onderdeel van de ontvlechting van het rioolstelsel.

Kolkreiniging is een periodiek terugkerend onderhoudproces om verstopping en wateroverlast te voorkomen.

## GGM-bron

> "Een reservoir bestemd voor de opvang van hemelwater afkomstig van erop aangesloten oppervlakken, het laten bezinken van in dit water meegevoerde bezinkbare stoffen en de afvoer van dit water naar een rioolstelsel of naar de ondergrond." — [GGM Beheer Openbare Ruimte](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md)

- **Entiteit**: Kolk
- **Beleidsdomein**: Beheer Openbare Ruimte
- **Taakveld**: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Matchsterkte**: exact
- **Overerving**: Kolk is een specialisatie van Put in het GGM
- **Attributen** (3): bereikbaarheidKolk, risicogebied, type

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| generalisatie | Put (GGM) | Kolk → Put | GGM |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/waterobject\|Waterobject]] | bidirectioneel | Beleidsbron |

## Bedrijfsprocessen

- **Rioolbeheer**: beheer van kolken als onderdeel van het rioolstelsel
- **Kolkreiniging**: periodieke reiniging om verstopping en wateroverlast te voorkomen
- **Amfibievriendelijk maken kolken**: ombouw van kolken met amfibievriendelijke roosters

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
