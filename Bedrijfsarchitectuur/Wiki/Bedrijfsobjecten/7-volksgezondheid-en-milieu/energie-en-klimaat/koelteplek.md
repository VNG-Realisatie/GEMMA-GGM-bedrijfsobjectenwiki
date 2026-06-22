---
type: bedrijfsobject
naam: Koelteplek
domein: [Energie en Klimaat]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit: ""
ggm_beleidsdomein: ""
ggm_guid: ""
ggm_uml_type: ""
ggm_taakveld: ""
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
gemma_definitie: "Openbaar toegankelijke groene verblijfsplek van minimaal 200 m² waar de gevoelstemperatuur koeler is dan of gelijk aan het buitengebied."
bedrijfsprocessen: [Klimaatadaptatiebeleid, Beheer openbare ruimte, Groenbeleid]
bedrijfsfuncties: [Klimaatadaptatie, Beheer openbare ruimte]
relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/groenobject|Groenobject]]"
    richting: "van-dit-BO"
    kardinaliteit: "1..*"
    beschrijving: Koelteplek bestaat uit of overlapt met groenobjecten
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/boom|Boom]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: Bomen leveren schaduw en verkoeling aan koelteplekken
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Centraal begrip in klimaatadaptatiebeleid, onderdeel van de doelstellingen |
| Herkenbaar voor domeinexperts | ✅ Gedefinieerd in de Visie Klimaatadaptatie met concrete criteria |
| Heeft eigen bestaan | ✅ Fysieke locatie met meetbare eigenschappen (oppervlakte, gevoelstemperatuur) |
| Kan in meervoud bestaan | ✅ Tientallen tot honderden per gemeente |
| Heeft eigen levenscyclus | ✅ Identificatie → aanwijzing → inrichting → monitoring → eventueel verbetering |
| Heeft relaties met andere concepten | ✅ Groenobject, boom, buurt, prioriteitsgebied |

**6/6 criteria van toepassing.**

## Beschrijving

Een koelteplek is een openbaar toegankelijke groene verblijfsplek waar inwoners verkoeling kunnen zoeken bij hitte. De gemeente Utrecht definieert een koelteplek als een locatie van minimaal 200 m² waar de gevoelstemperatuur niet hoger is dan in het buitengebied (referentie KNMI De Bilt). De doelstelling is dat elke inwoner binnen 200 meter loopafstand een koelteplek kan bereiken.

Koelteplekken worden geïnventariseerd via de "afstand tot koelte"-kaart, die per gebouw de loopafstand tot de dichtstbijzijnde koelteplek berekent. Locaties waar deze afstand meer dan 200 meter bedraagt, zijn prioriteitsgebieden voor nieuwe koelteplekken.

De koelteplek combineert meerdere beleidsdoelen: verkoeling (klimaatadaptatie), vergroening (groenbeleid), gezondheid (openbare gezondheid) en recreatie (leefbaarheid). Koelteplekken zijn typisch parken, plantsoenen of grotere groenvoorzieningen met voldoende schaduw door bomen.

Gebieden waar de norm niet wordt gehaald zijn onder meer delen van Lombok, Parkwijk Zuid, 't Zand en Hoge Weide.

## Procesbron

Geen GGM-entiteit — dit is een procesobject dat voortkomt uit het klimaatadaptatiebeleid. Het GGM heeft geen beleidsdomein voor klimaatadaptatie; taakveld 7 bevat alleen het beleidsdomein Afval.

Bron: [[Wiki/Bronsamenvattingen/Energie en Klimaat/visie-klimaatadaptatie-utrecht|Visie Klimaatadaptatie Utrecht]]

## Relaties

| Gerelateerd BO | Type | Beschrijving |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/groenobject\|Groenobject]] | associatie | Koelteplek bestaat uit of overlapt met groenobjecten |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving/beheer-openbare-ruimte/boom\|Boom]] | associatie | Bomen leveren schaduw en verkoeling |

## Bedrijfsprocessen

- **Klimaatadaptatiebeleid** — inventarisatie koelteplekken, prioriteitsgebieden aanwijzen
- **Beheer openbare ruimte** — inrichting en onderhoud van koelteplekken
- **Groenbeleid** — vergroening ten behoeve van verkoeling (Schaalsprong Groen)


## Bronnen

- [[Wiki/Bronsamenvattingen/Energie en Klimaat/visie-klimaatadaptatie-utrecht]]

## Terugmelding GGM

**Koelteplek** — Procesobject voor aangewezen openbare verblijfsplekken met verkoelende functie (minimaal 200 m², gevoelstemperatuur ≤ buitengebied). Systematisch geïnventariseerd op kaarten en gemonitord op afstand tot gebouwen. Zou onder een nieuw beleidsdomein Klimaatadaptatie (taakveld 7) kunnen.
