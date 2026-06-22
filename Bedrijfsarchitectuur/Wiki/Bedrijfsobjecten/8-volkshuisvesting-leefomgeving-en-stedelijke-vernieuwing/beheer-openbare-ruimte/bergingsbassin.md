---
type: bedrijfsobject
naam: Bergingsbassin
domein: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Bergingsbassin"
ggm_guid: EAID_55C683B9_3F66_4E21_B0C1_66E664837CA
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Hoofdobjecten IMBOR en Geo-object]
ggm_diagram_ids: []
ggm_definitie: "Een gesloten reservoir waarin het afvalwater tijdelijk wordt opgevangen Synoniemen: Retentiebassin, bufferbassin"
ggm_toelichting: ""
ggm_synoniemen: "Retentiebassin, bufferbassin"
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
gemma_definitie: "Gesloten reservoir achter een overstortconstructie voor tijdelijke opvang en bezinking van overstortwater."
relaties:
  - type: generalisatie
    bedrijfsobject: Bouwwerk (GGM)
    richting: "van-dit-BO"
    kardinaliteit:
    beschrijving: Bergingsbassin is een specialisatie van Bouwwerk in het GGM
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/overstortconstructie|Overstortconstructie]]"
    richting: bidirectioneel
    kardinaliteit: "1..*"
    beschrijving: Bergbezinkbassin is geplaatst achter een overstortconstructie
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/waterobject|Waterobject]]"
    richting: bidirectioneel
    kardinaliteit:
    beschrijving: Bergingsbassin vermindert de belasting op oppervlaktewater
bedrijfsprocessen: [Rioolbeheer, Onderhoud bergbezinkbassins]
bedrijfsfuncties: [Beheer openbare ruimte, Rioleringsbeheer]
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Beperkt milieu-impact van overstorten door opvang en bezinking van verdund afvalwater |
| Is herkenbaar voor domeinexperts | ✅ | Bergbezinkbassin, retentiebassin — standaardterminologie in rioleringsbeheer |
| Heeft een eigen bestaan binnen het domein | ✅ | Elk bassin individueel geregistreerd met bergend vermogen, pompvoorzieningen en vorm |
| Kan in meervoud bestaan | ✅ | 18 bergbezinkbassins in Utrecht |
| Heeft een eigen levenscyclus | ✅ | Aanleg → periodiek onderhoud (lediging, reiniging) → renovatie → vervanging |
| Heeft relaties met andere concepten | ✅ | Overstortconstructie, waterobject, rioleringsgebied |

Score: 6/6.

## Beschrijving

Een bergingsbassin (bergbezinkbassin) is een gesloten reservoir dat geplaatst wordt achter een overstortconstructie. Bij zware neerslag vangt het bassin verdund afvalwater op dat anders via de overstort op het oppervlaktewater zou worden geloosd. In het bassin bezinken vaste stoffen, waarna het water na de bui wordt teruggepompt naar het riool voor transport naar de zuiveringsinstallatie.

Utrecht beschikt over 18 bergbezinkbassins, geplaatst achter de belangrijkste overstorten. Deze bassins verminderen de milieu-impact van overstorten op het oppervlaktewater aanzienlijk doordat ze de meest vervuilde eerste spoeling opvangen.

## GGM-bron

> "Een gesloten reservoir waarin het afvalwater tijdelijk wordt opgevangen" — [GGM Beheer Openbare Ruimte](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md)

- **Entiteit**: Bergingsbassin
- **Beleidsdomein**: Beheer Openbare Ruimte
- **Taakveld**: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Matchsterkte**: exact
- **Overerving**: Bergingsbassin is een specialisatie van Bouwwerk in het GGM
- **Attributen** (5): bergendVermogen, pompLedigingsVoorziening, pompSpoelVoorziening, spoelleiding, vorm

## BO-definitie

De GEMMA-definitie positioneert het bassin in de functionele context: achter een overstortconstructie, voor opvang en bezinking. De GGM-definitie beschrijft het generiek als tijdelijke opvang van afvalwater.

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| generalisatie | Bouwwerk (GGM) | Bergingsbassin → Bouwwerk | GGM |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/overstortconstructie\|Overstortconstructie]] | bidirectioneel | Beleidsbron |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/waterobject\|Waterobject]] | bidirectioneel | Beleidsbron |

## Bedrijfsprocessen

- **Rioolbeheer**: beheer van bergbezinkbassins als onderdeel van het rioolstelsel
- **Onderhoud bergbezinkbassins**: periodieke lediging, reiniging en inspectie van bassins

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
