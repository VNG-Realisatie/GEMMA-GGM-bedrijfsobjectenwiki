---
type: bedrijfsobject
naam: Buitenzwemplek
domein: [Beheer Openbare Ruimte]
archimate_type: "business-object"
grondslag: "procesobject"
ggm_entiteit: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
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
gemma_definitie: "Locatie in open water waar buiten gezwommen wordt, met onderscheid tussen officieel aangewezen en niet-officiële zwemplekken."
bronnen: [Wiki/Bronsamenvattingen/milieu/beleidsnota-stadswater, Wiki/Bronsamenvattingen/milieu/visie-water-riolering]
  - [[Wiki/Bronsamenvattingen/milieu/beleidsnota-stadswater]]
  - [[Wiki/Bronsamenvattingen/milieu/visie-water-riolering]]
relaties:
  - type: associatie
    bedrijfsobject: "[[Waterobject]]"
    richting: bidirectioneel
    kardinaliteit: ""
    beschrijving: Zwemplek is een locatie in een waterobject
  - type: associatie
    bedrijfsobject: "[[Zwembad]]"
    richting: bidirectioneel
    kardinaliteit: ""
    beschrijving: Beide voorzien in zwembehoefte maar verschillend type — Zwembad is gebouw, Buitenzwemplek is open water
bedrijfsprocessen: [Zwemwaterkwaliteitsmonitoring, Oeverinrichting, Locatiebeheer, Aanwijzing officieel zwemwater]
bedrijfsfuncties: [Beheer openbare ruimte, Waterbeheer, Recreatiebeheer]
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Kernbegrip in stadswater- en recreatiebeleid; groeiende behoefte door stadsgroei en warmer klimaat |
| Is herkenbaar voor domeinexperts | ✅ | Herkenbaar in beleid als officieel zwemwater en niet-officiële zwemplek |
| Heeft een eigen bestaan binnen het domein | ✅ | Elke zwemplek heeft eigen locatie, waterkwaliteitsstatus, capaciteit en beheerregime |
| Kan in meervoud bestaan | ✅ | 3 officiële zwemlocaties en diverse niet-officiële zwemplekken in Utrecht |
| Heeft een eigen levenscyclus | ✅ | Identificatie → aanwijzing/facilitering → monitoring → eventueel ontmoediging/verbod |
| Heeft relaties met andere concepten | ✅ | [[Waterobject]], [[Zwembad]] |

Score: 6/6.

## Beschrijving

Utrecht heeft 3 officiële zwemlocaties (Haarrijnseplas, Strijkviertelplas, Voorveldse Polder) met samen circa 6.000 bezoekers per dag capaciteit. Daarnaast zijn er diverse niet-officiële zwemplekken, zoals Muntsluis, Kromme Rijn bij Amelisweerd en Veilinghaven.

De provincie wijst officieel zwemwater aan; de gemeente is locatiebeheerder en meet sinds 2014 waterkwaliteit bij circa 10 niet-officiële locaties. De behoefte aan buitenzwemplekken groeit 25-30% tot 2040 door stadsgroei en warmere zomers.

Het beleid is: faciliteren waar het kan, ontmoedigen of verbieden waar veiligheid of leefbaarheid in het geding is. Overlast bij Muntsluis en Veilinghaven is een specifiek knelpunt.

## Procesbron

Bron: [[Wiki/Bronsamenvattingen/milieu/beleidsnota-stadswater|Beleidsnota Stadswater]] en [[Wiki/Bronsamenvattingen/milieu/visie-water-riolering|Visie Water en Riolering]]

> Officiële zwemlocaties worden aangewezen door de provincie; de gemeente faciliteert en beheert de locaties. Bij niet-officiële zwemplekken meet de gemeente waterkwaliteit en wordt per locatie bepaald of faciliteren of ontmoedigen gepast is.

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| associatie | [[Waterobject]] | bidirectioneel | Beleidsbron |
| associatie | [[Zwembad]] | bidirectioneel | Beleidsbron |

## Bedrijfsprocessen

- **Zwemwaterkwaliteitsmonitoring**: meting van waterkwaliteit bij officiële en niet-officiële zwemplekken
- **Oeverinrichting**: aanpassing van oevers om veilig zwemmen mogelijk te maken
- **Locatiebeheer**: beheer van voorzieningen op en rond zwemlocaties
- **Aanwijzing officieel zwemwater**: procedure voor aanwijzing door de provincie, met gemeente als locatiebeheerder

## Terugmelding GGM

> **Buitenzwemplek** — Locatie in open water waar buiten gezwommen wordt. Het GGM kent geen entiteit voor buitenzwemlocaties. Het concept is relevant voor gemeentelijk waterbeheer en recreatiebeleid, met eigen processen voor waterkwaliteitsmonitoring, oeverinrichting en aanwijzing van zwemwater. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
