---
type: bedrijfsobject
naam: Boom
domein: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Boom"
ggm_guid: EAID_83A942F7_5291_42F0_AFB1_9A57D0FB2F1
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Diagram IMBOR vs IMGeo]
ggm_diagram_ids: [EAID_B832F543_BBE3_421e_B76D_561E53237684]
ggm_definitie: "Een houtachtig gewas (loofboom of conifeer) met een wortelgestel en een enkele, stevige, houtige stam, die zich boven de grond vertakt.
Toelichting: Een houtachtig gewas (loofboom of conifeer) met een wortelgestel en een enkele, stevige, houtige stam, die zich boven de grond vertakt."
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
analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Boom** als directe tegenhanger. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Klimplant** (detail) — Detailgegeven
  - **SolitairePlant** (detail) — Detailgegeven (weinig attributen)
  - **Vegetatieobject** (detail) — Detailgegeven
bo_definitie: "Een houtachtig gewas (loofboom of conifeer) met een wortelgestel en een enkele, stevige, houtige stam, die zich boven de grond vertakt. Toelichting: Een houtachtig gewas (loofboom of conifeer) met een wortelgestel en een enkele, stevige, houtige stam, die zich boven de grond vertakt."
bo_toelichting: ''
bedrijfsprocessen: [Bomenbeheer, Kapvergunningverlening, Boomveiligheid-inspectie (VTA), Verplanting, Herplant]
bedrijfsfuncties: [Groenbeheer, Vergunningverlening, Openbare ruimte]
bo_relaties:
  - type: generalisatie
    bedrijfsobject: Vegetatieobject (GGM)
    richting: "van-dit-BO"
    kardinaliteit: 
    beschrijving: Boom is een specialisatie van Vegetatieobject
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Centraal object in bomenbeleid en groenbeheer |
| Is herkenbaar voor domeinexperts | ✅ | Iedereen in groenbeheer en ruimtelijke ordening kent het concept |
| Heeft een eigen bestaan binnen het domein | ✅ | Individueel beheerd, geïnspecteerd, geregistreerd object |
| Kan in meervoud bestaan | ✅ | 110.000+ gemeentelijke bomen in Utrecht alleen al |
| Heeft een eigen levenscyclus | ✅ | Aanplant → begeleidingssnoei → volwassen fase → veroudering → kap/verplanting |
| Heeft relaties met andere concepten | ✅ | Groeiplaats, inspectie, vergunning, bomenstructuur, subsidieregeling |

Score: 6/6. Boom is een ondubbelzinnig bedrijfsobject.

## Beschrijving

Een boom is een individueel geregistreerd en beheerd groenobject in de openbare ruimte. Gemeenten beheren tienduizenden bomen, elk met eigen registratie van soort, leeftijd, stamdiameter, conditie, locatie en monetaire waarde. Bomen doorlopen een levenscyclus van aanplant, via begeleiding en onderhoud in de jeugdfase, naar de volwassen fase met kroonverzorging, tot de verouderingsfase met intensievere inspectie en eventuele kap of verplanting.

Bomen worden systematisch beoordeeld met Visual Tree Assessment (VTA), een internationale methode voor visuele inspectie op interne gebreken. Alle inspecties worden digitaal gedocumenteerd. Bij geconstateerde risico's volgen maatregelen variërend van snoei tot groeiplaatsverbetering tot kap.

Bijzondere categorieën zijn monumentale bomen (≥80 jaar) en bomen in de stedelijke bomenstructuur (cultuurhistorisch, ruimtelijk of ecologisch waardevol). Deze classificaties worden als beleidsstatus op het boomobject geregistreerd, niet als aparte objecten.

## GGM-bron

> "Een houtachtig gewas (loofboom of conifeer) met een wortelgestel en een enkele, stevige, houtige stam, die zich boven de grond vertakt."

- **Entiteit**: Boom
- **Beleidsdomein**: Beheer Openbare Ruimte (Model IMBOR)
- **Taakveld**: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Matchsterkte**: exact
- **Attributen** (43): beleidsstatus, beoogdeOmlooptijd, boombeeld, boombeschermer, boomgroep, boomhoogteActueel, boomhoogteklasseActueel, boomhoogteklasseEindebeeld, boomspiegel, boomTypeBeschermingsstatusPlus, boomvoorziening, controlefrequentie, feestverlichting, groeifase, groeiplaatsinrichting, herplantplicht, kiemjaar, kroondiameterklasseActueel, kroondiameterklasseEindebeeld, kroonvolume, leeftijd, meerstammig, monetaireBoomwaarde, snoeifase, stamdiameter, stamdiameterklasse, takvrijeRuimteTotGebouw, takvrijeStam, takvrijeZonePrimair, takvrijeZoneSecundair, transponder, type, typeBeschermingsstatus, typeOmgevingsrisicoklasse, typePlus, typeVermeerderingsvorm, veiligheidsklasseBoom, verplant, verplantbaar, vrijeDoorrijhoogte, vrijeDoorrijhoogtePrimair, vrijeDoorrijhoogteSecundair, vrijeTakval

De GGM-entiteit Boom is een specialisatie van **Vegetatieobject** (generalisatie). Vegetatieobject is op zijn beurt een beheerobject in de openbare ruimte.

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| generalisatie | Vegetatieobject (GGM) | Boom → Vegetatieobject | GGM |

## Bedrijfsprocessen

- **Bomenbeheer**: aanplant, begeleidingssnoei, onderhoudssnoei, groeiplaatsverbetering, ziektebestrijding
- **Boomveiligheid-inspectie (VTA)**: periodieke visuele inspectie, digitale registratie, risicoclassificatie
- **Kapvergunningverlening**: aanvraag, veldbeoordeling (4 criteria: ecologisch, ruimtelijk, milieu, cultuurhistorisch), besluit
- **Verplanting**: voorbereiding (1-2 jaar), uitvoering, nazorg
- **Herplant**: compensatie bij kap, keuze boomsoort en locatie

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
