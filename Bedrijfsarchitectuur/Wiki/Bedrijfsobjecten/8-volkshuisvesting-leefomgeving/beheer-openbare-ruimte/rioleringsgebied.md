---
type: bedrijfsobject
naam: Rioleringsgebied
domein: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Rioleringsgebied"
ggm_guid: EAID_3252585C_4FAB_4EC1_9BA6_F51EAFF271D
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Hoofdobjecten IMBOR en Geo-object]
ggm_diagram_ids: []
ggm_definitie: "Het gebied waarbinnen één of meerdere inliggende rioolstelsel(s) het afvalwater naar één gemaal of overnamepunt transporteert/teren."
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
gemma_definitie: "Administratief beheersgebied waarbinnen het rioolstelsel afvalwater naar één gemaal of overnamepunt transporteert."
gemma_subtypes:
  - naam: "Bemalingsgebied"
    omschrijving: Rioleringsgebied waaruit afvalwater door een gemaal wordt verwijderd
    ggm_entiteit: Bemalingsgebied
    ggm_guid: EAID_A1EE11DF_4EEA_409A_8E43_F108DC0BF96
    ggm_attribuut: generalisatie
relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/gemaal|Gemaal]]"
    richting: bidirectioneel
    kardinaliteit: ""
    beschrijving: Een rioleringsgebied wordt bediend door een gemaal
  - type: associatie
    bedrijfsobject: "[[Overstortconstructie]]"
    richting: bidirectioneel
    kardinaliteit: ""
    beschrijving: Overstortconstructies functioneren binnen een rioleringsgebied
bedrijfsprocessen: [Rioolbeheer, Gebiedsplanning, Rioolvervangingsplanning]
bedrijfsfuncties: [Beheer openbare ruimte, Rioleringsbeheer]
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Kernbegrip in rioleringsbeheer; bepalend voor vervangingsplanning en hemelwaterontvlechting |
| Is herkenbaar voor domeinexperts | ✅ | Standaardbegrip in het stedelijk waterbeheer, gehanteerd in het Programma Water en Riolering |
| Heeft een eigen bestaan binnen het domein | ✅ | Elk rioleringsgebied is een afgebakend beheersgebied met eigen gemaal en stelselkenmerken |
| Kan in meervoud bestaan | ✅ | Utrecht heeft drie zuiveringsgebieden (Brailledreef, Proostwetering, Zandweg) met daarbinnen meerdere rioleringsgebieden |
| Heeft een eigen levenscyclus | ✅ | Vaststelling → beheer → hemelwaterontvlechting → stelselvervanging → herindeling |
| Heeft relaties met andere concepten | ✅ | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/gemaal\|Gemaal]], [[Overstortconstructie]], Put |

Score: 6/6.

## Beschrijving

Een rioleringsgebied is een administratieve indeling van het rioolstelsel. Het omvat het gebied waarbinnen een of meerdere rioolstelsels het afvalwater naar een centraal punt (gemaal of overnamepunt) transporteren. Per rioleringsgebied wordt het beheer, de vervangingsplanning en de hemelwaterontvlechting gepland.

Utrecht heeft drie zuiveringsgebieden:
- **Stad Utrecht** — afvalwater naar rwzi Brailledreef
- **Leidsche Rijn en Vleuten** — afvalwater naar rwzi Proostwetering
- **De Meern** — afvalwater naar rwzi Zandweg

De gemeente is verantwoordelijk voor het transport van afvalwater tot aan het overnamepunt met het waterschap. De zuivering zelf is een taak van het waterschap.

## Specialisaties

| Subtype | Omschrijving | GGM-entiteit |
|---|---|---|
| Bemalingsgebied | Rioleringsgebied waaruit afvalwater door een gemaal wordt verwijderd | [Bemalingsgebied](Sources/GGM/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte.md) |

## GGM-bron

> "Het gebied waarbinnen één of meerdere inliggende rioolstelsel(s) het afvalwater naar één gemaal of overnamepunt transporteert/teren." — [GGM Beheer Openbare Ruimte](Sources/GGM/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte.md)

- **Entiteit**: Rioleringsgebied
- **Beleidsdomein**: Beheer Openbare Ruimte
- **Matchsterkte**: exact

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| associatie | [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/gemaal\|Gemaal]] | bidirectioneel | GGM / Beleidsbron |
| associatie | [[Overstortconstructie]] | bidirectioneel | Beleidsbron |

## Bedrijfsprocessen

- **Rioolbeheer**: dagelijks beheer van het rioolstelsel binnen het rioleringsgebied
- **Gebiedsplanning**: planvorming voor hemelwaterontvlechting en stelselverbetering per gebied
- **Rioolvervangingsplanning**: programmering van rioolvervanging op gebiedsniveau

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
