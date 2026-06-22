---
type: bedrijfsobject
naam: Put
domein: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Put"
ggm_guid: EAID_B7168388_9EB9_4C95_B35E_1BA2660849E
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Hoofdobjecten IMBOR en Geo-object]
ggm_diagram_ids: []
ggm_definitie: "Verticale waterdichte constructie, toegepast om leidingen aan te sluiten, van richting of niveau te veranderen, om toegang te verschaffen aan personeel en/of apparatuur voor inspectie en onderhoud, en om beluchting en ventilatie mogelijk te maken"
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
gemma_definitie: "Verticale constructie in het rioleringssysteem voor aansluiting, inspectie en onderhoud van leidingen."
gemma_subtypes:
  - naam: "Drainageput"
    omschrijving: Put met poreuze of geperforeerde buisleiding voor verbetering grondwaterafvoer
    ggm_entiteit: Drainageput
    ggm_guid: EAID_01343EF1_EF8E_4FB1_9A58_8E885304D55
    ggm_attribuut: generalisatie
  - naam: "Filterput"
    omschrijving: Put met filterconstructie voor onttrekken van grondwater
    ggm_entiteit: Filterput
    ggm_guid: EAID_6E949D6F_0A40_4BB7_B655_5EF4B8BBA4D
    ggm_attribuut: generalisatie
  - naam: "Infiltratieput"
    omschrijving: Put met waterdoorlatende wanden voor infiltratie van hemelwater
    ggm_entiteit: Infiltratieput
    ggm_guid: EAID_D9ACE9BA_F13C_4EEB_8DD8_73A7E0043DB
    ggm_attribuut: generalisatie
relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/gemaal|Gemaal]]"
    richting: bidirectioneel
    kardinaliteit: ""
    beschrijving: Putten en gemalen zijn onderdelen van hetzelfde rioolstelsel
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioleringsgebied|Rioleringsgebied]]"
    richting: bidirectioneel
    kardinaliteit: ""
    beschrijving: Putten liggen in een rioleringsgebied
  - type: associatie
    bedrijfsobject: "[[Kolk]]"
    richting: bidirectioneel
    kardinaliteit: ""
    beschrijving: Kolken zijn verbonden met putten voor hemelwaterafvoer
bedrijfsprocessen: [Rioolbeheer, Rioolinspectie, Rioolvervanging]
bedrijfsfuncties: [Beheer openbare ruimte, Rioleringsbeheer]
ggm_gemma_naam: "Put"
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Essentieel onderdeel van de rioolinfrastructuur; toegangspunt voor inspectie en onderhoud |
| Is herkenbaar voor domeinexperts | ✅ | Standaardbegrip in rioleringsbeheer en IMBOR |
| Heeft een eigen bestaan binnen het domein | ✅ | Elke put is individueel geregistreerd met locatie, type, materiaal en staat |
| Kan in meervoud bestaan | ✅ | Duizenden putten in het gemeentelijk rioolstelsel |
| Heeft een eigen levenscyclus | ✅ | Aanleg → inspectie → onderhoud → renovatie → vervanging |
| Heeft relaties met andere concepten | ✅ | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/gemaal\|Gemaal]], [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioleringsgebied\|Rioleringsgebied]], Kolk |

Score: 6/6.

## Beschrijving

Een put is een verticale constructie in het rioleringssysteem. Putten vormen de toegangspunten tot het ondergrondse rioolstelsel. Ze worden gebruikt voor het aansluiten van leidingen, het veranderen van richting of niveau, en voor inspectie, reiniging en onderhoud van de riolering. Daarnaast zorgen putten voor beluchting en ventilatie van het stelsel.

Bij rioolvervanging worden ook putten vervangen of gerenoveerd. De staat van putten is een belangrijk criterium bij de beoordeling van het rioolstelsel.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Drainageput | Put met poreuze of geperforeerde buisleiding voor verbetering grondwaterafvoer | [Drainageput](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md) |
| Filterput | Put met filterconstructie voor onttrekken van grondwater | [Filterput](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md) |
| Infiltratieput | Put met waterdoorlatende wanden voor infiltratie van hemelwater | [Infiltratieput](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md) |

## GGM-bron

> "Verticale waterdichte constructie, toegepast om leidingen aan te sluiten, van richting of niveau te veranderen, om toegang te verschaffen aan personeel en/of apparatuur voor inspectie en onderhoud, en om beluchting en ventilatie mogelijk te maken" — [GGM Beheer Openbare Ruimte](Sources/GGM/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte.md)

- **Entiteit**: Put
- **Beleidsdomein**: Beheer Openbare Ruimte
- **Matchsterkte**: exact

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/gemaal\|Gemaal]] | bidirectioneel | GGM / Beleidsbron |
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioleringsgebied\|Rioleringsgebied]] | bidirectioneel | Beleidsbron |
| associatie | [[Kolk]] | bidirectioneel | Beleidsbron |

## Bedrijfsprocessen

- **Rioolbeheer**: dagelijks beheer en registratie van putten
- **Rioolinspectie**: visuele en camera-inspectie van putten en aangesloten leidingen
- **Rioolvervanging**: vervanging of renovatie van putten bij stelselvernieuwing

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
