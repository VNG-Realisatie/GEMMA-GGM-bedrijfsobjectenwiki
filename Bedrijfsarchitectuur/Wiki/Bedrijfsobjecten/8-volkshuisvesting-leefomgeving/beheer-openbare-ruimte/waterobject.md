---
type: bedrijfsobject
naam: Waterobject
domein: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Waterobject"
ggm_guid: EAID_81CBE022_0D94_4377_82CA_3AA12937FE8
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Hoofdobjecten IMBOR en Geo-object]
ggm_diagram_ids: []
ggm_definitie: "Kleinste functioneel onafhankelijk stukje water met gelijkblijvende, homogene eigenschappen en relaties dat er binnen het objecttype Water van NEN 3610 wordt onderscheiden en dat permanent met water bedekt is."
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
gemma_definitie: "Functioneel stuk oppervlaktewater dat de gemeente beheert, zoals watergangen, vijvers, grachten en kanalen."
bronnen:
  - [[Wiki/Bronsamenvattingen/milieu/visie-water-riolering]]
  - [[Wiki/Bronsamenvattingen/milieu/programma-water-riolering-2025-2029]]
  - [[Wiki/Bronsamenvattingen/milieu/beleidsnota-stadswater]]
relaties:
  - type: generalisatie
    bedrijfsobject: Beheerobject (GGM)
    richting: "van-dit-BO"
    kardinaliteit:
    beschrijving: Waterobject is een specialisatie van Beheerobject in het GGM
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/overstortconstructie|Overstortconstructie]]"
    richting: bidirectioneel
    kardinaliteit:
    beschrijving: Waterobject ontvangt overstortwater van overstortconstructies
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/gemaal|Gemaal]]"
    richting: bidirectioneel
    kardinaliteit:
    beschrijving: Gemaal verpompt water van of naar waterobjecten
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/kunstwerk|Kunstwerk]]"
    richting: bidirectioneel
    kardinaliteit:
    beschrijving: Kunstwerken (bruggen, kademuren) overbruggen of begrenzen waterobjecten
bedrijfsprocessen: [Maaibeheer, Baggeren, Duikervervanging, Waterkwaliteitsmonitoring, Programma Gezond Water]
bedrijfsfuncties: [Beheer openbare ruimte, Waterbeheer]
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Watergangen, vijvers, grachten en kanalen zijn bepalend voor de leefomgeving en waterhuishouding |
| Is herkenbaar voor domeinexperts | ✅ | Watergang, vijver, gracht, kanaal — herkenbare begrippen in waterbeheer |
| Heeft een eigen bestaan binnen het domein | ✅ | Elk waterobject geregistreerd met waternaam, waterpeil, type, vaarwegtraject |
| Kan in meervoud bestaan | ✅ | 295 ha water, 246 km watergangen, 42 km duikers in Utrecht |
| Heeft een eigen levenscyclus | ✅ | Aanleg → maaien → baggeren → duikervervanging → herinrichting |
| Heeft relaties met andere concepten | ✅ | Overstortconstructie, gemaal, kunstwerk, buitenzwemplek |

Score: 6/6.

## Beschrijving

Een waterobject is een functioneel stuk oppervlaktewater dat de gemeente beheert: watergangen, vijvers, grachten en kanalen. Utrecht onderhoudt 295 hectare water, verdeeld over 246 km watergangen en 42 km duikers.

Het watersysteem bestaat uit drie deelsystemen: het Kromme Rijn-systeem (oost), het Leidsche Rijn-infiltratiesysteem (noord) en het De Meern-systeem (zuid). Elk systeem heeft eigen kenmerken voor waterpeil en doorstroming.

Beheer omvat maaien van oevers en watergangen, baggeren (30 km per jaar) en vervanging van duikers. Het waterobject heeft attributen voor vaarwatertype en waterpeil (zomer/winter). Utrecht kent 16 vaarroutes over het stadswater.

Het programma Gezond Water (samenwerking met Hoogheemraadschap De Stichtse Rijnlanden) richt zich op verbetering van de ecologische waterkwaliteit. Ecoscan-metingen monitoren de biologische en chemische toestand van waterobjecten.

## GGM-bron

> "Kleinste functioneel onafhankelijk stukje water met gelijkblijvende, homogene eigenschappen en relaties dat er binnen het objecttype Water van NEN 3610 wordt onderscheiden en dat permanent met water bedekt is." — [GGM Beheer Openbare Ruimte](Sources/GGM/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte.md)

- **Entiteit**: Waterobject
- **Beleidsdomein**: Beheer Openbare Ruimte
- **Taakveld**: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Matchsterkte**: exact
- **Overerving**: Waterobject is een specialisatie van Beheerobject in het GGM
- **Attributen** (23): breedte, folie, hoogte, infiltrerendOppervlak, infiltrerendVermogen, lengte, lozingspunt, oppervlakte, porositeit, streefdiepte, type, typePlus, typePlus2, typeVaarwater, typeWaterplant, uitstroomniveau, vaarwegtraject, vorm, waternaam, waterpeil, waterpeilWinter, waterpeilZomer, waterplanten

## BO-definitie

De GEMMA-definitie benadrukt het gemeentelijk perspectief: "functioneel stuk oppervlaktewater dat de gemeente beheert" met herkenbare voorbeelden (watergangen, vijvers, grachten, kanalen). De GGM-definitie is technisch en verwijst naar NEN 3610 en homogene eigenschappen.

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| generalisatie | Beheerobject (GGM) | Waterobject → Beheerobject | GGM |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/overstortconstructie\|Overstortconstructie]] | bidirectioneel | Beleidsbron |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/gemaal\|Gemaal]] | bidirectioneel | Beleidsbron |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/kunstwerk\|Kunstwerk]] | bidirectioneel | Beleidsbron |

## Bedrijfsprocessen

- **Maaibeheer**: maaien van oevers en watergangen
- **Baggeren**: verwijderen van baggerslib uit watergangen (30 km/jaar)
- **Duikervervanging**: vervangen van verouderde duikers onder wegen en dijken
- **Waterkwaliteitsmonitoring**: ecoscan-metingen voor biologische en chemische waterkwaliteit
- **Programma Gezond Water**: samenwerking met HDSR voor verbetering ecologische kwaliteit
