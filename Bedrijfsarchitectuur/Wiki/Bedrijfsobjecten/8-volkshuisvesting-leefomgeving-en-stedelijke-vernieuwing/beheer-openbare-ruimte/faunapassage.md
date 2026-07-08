---
type: bedrijfsobject
naam: Faunapassage
domein: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Ecoduct"
ggm_guid: EAID_812B8374_F08E_47F6_881D_309B7D23FD4
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: []
ggm_diagram_ids: [EAPK_C3BA35EC_ABFA_4a7d_BEE9_07FF7563442D]
ggm_definitie: "Wildwissel in de vorm van een viaduct voor passages van dieren over een weg of spoorweg. IMGeo
Synoniemen: Natuurbrug, Faunabrug, Ecobrug, Ecopassage, Natuurpassage
Toelichting: Opheffen van barriÃ¨res en de migratie van fauna mogelijk maken tussen of binnen leefgebieden en populaties."
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
  Dit BO is de hernoeming van GGM-entiteit **Ecoduct**. Het BO dekt daarnaast de volgende GGM-entiteiten via een indirecte relatie:
  - **Overbruggingsobject** (detail) — Detailgegeven
bo_definitie: "Wildwissel in de vorm van een viaduct voor passages van dieren over een weg of spoorweg. IMGeo Synoniemen: Natuurbrug, Faunabrug, Ecobrug, Ecopassage, Natuurpassage Toelichting: Opheffen van barriÃ¨res en de migratie van fauna mogelijk maken tussen of binnen leefgebieden en populaties."
bo_toelichting: ''
bedrijfsprocessen: [Groene Web-programma, Monitoring faunapassages, Groenbeheer]
bedrijfsfuncties: [Groenbeheer, Openbare ruimte, Ecologie]
bo_relaties:
  - type: generalisatie
    bedrijfsobject: Overbruggingsobject (GGM)
    richting: "van-dit-BO"
    kardinaliteit: 
    beschrijving: Ecoduct is een specialisatie van Overbruggingsobject in het GGM
  - type: associatie
    bedrijfsobject: "[[Groenobject]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: Faunapassages verbinden groenobjecten en ecologische corridors
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Expliciet benoemd in het Groenstructuurplan en het Groene Web-programma |
| Herkenbaar voor domeinexperts | ✅ | Ecologen, groenbeheerders en verkeersplanners werken met faunapassages |
| Heeft eigen bestaan | ✅ | Fysieke constructie op een specifieke locatie |
| Kan in meervoud bestaan | ✅ | Tientallen passages in Utrecht; geïnventariseerd op overzichtskaart |
| Heeft eigen levenscyclus | ✅ | Planning → aanleg → monitoring effectiviteit → onderhoud |
| Heeft relaties met andere concepten | ✅ | Verbindt [[Groenobject\|groengebieden]], passeert infrastructuur, dient beschermde soorten |

**Conclusie:** 6/6 criteria van toepassing. Faunapassage is een bedrijfsobject.

## Beschrijving

Een faunapassage is een fysieke voorziening die dieren in staat stelt infrastructuurbarrières (wegen, spoorlijnen, kanalen) te passeren. De gemeente Utrecht inventariseert faunapassages op een overzichtskaart met bestaande en gewenste passages, en realiseert ze via het Groene Web-programma.

Typen faunapassages die de gemeente realiseert:
- **Faunatunnels** — ondergrondse passages onder wegen (bijv. Moezeldreef)
- **Ecoducten/faunabruggen** — bovengrondse passages over snelwegen (bijv. Koningsweg over A27)
- **Loopplanken** — over water bij brughoofden
- **Natuurvriendelijke oevers** — geleidelijke overgangen land-water

De actualisatie van het Groenstructuurplan meldt dat meer dan de helft van de geplande passages is gerealiseerd.

## GGM-bron

> "Wildwissel in de vorm van een viaduct voor passages van dieren over een weg of spoorweg."
> Synoniemen: Natuurbrug, Faunabrug, Ecobrug, Ecopassage, Natuurpassage

- **Entiteit:** Ecoduct
- **Beleidsdomein:** Beheer Openbare Ruimte
- **Overerving:** specialisatie van Overbruggingsobject → Kunstwerk → Beheerobject
- **Matchsterkte:** sterk — de GGM-entiteit Ecoduct beschrijft specifiek bovengrondse passages (viaducten). In de gemeentelijke praktijk omvat "faunapassage" ook tunnels en loopplanken, waardoor de GEMMA-definitie breder is dan de GGM-definitie.
- **Attributen:** aantalOverspanningen, draagvermogen, type (8 attributen)

## Relaties

| Gerelateerd BO | Type | Richting | Beschrijving |
|---|---|---|---|
| [[Groenobject]] | associatie | bidirectioneel | Faunapassages verbinden groengebieden langs ecologische corridors |
| Overbruggingsobject (GGM) | generalisatie | van-dit-BO | Ecoduct erft constructie-attributen van Overbruggingsobject |

## Bedrijfsprocessen

- **Groene Web-programma** — planmatige realisatie van faunapassages en ecologische verbindingen
- **Monitoring faunapassages** — effectiviteitsmeting van gerealiseerde passages
- **Groenbeheer** — onderhoud van de passages en omliggende vegetatie


## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]

## Terugmelding GGM

De GGM-entiteit Ecoduct is beperkt tot bovengrondse viaducten. In de gemeentelijke praktijk worden ook faunatunnels, loopplanken en andere constructies als faunapassage beheerd. Overweging: ofwel de Ecoduct-definitie verbreden, ofwel een overkoepelende entiteit "Faunapassage" toevoegen die zowel Ecoduct als Tunnelobject (fauna-specifiek) omvat.
