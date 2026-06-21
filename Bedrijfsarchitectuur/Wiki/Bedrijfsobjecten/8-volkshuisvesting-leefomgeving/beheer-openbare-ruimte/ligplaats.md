---
type: bedrijfsobject
naam: Ligplaats
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
gemma_definitie: "Aangewezen plek in een ligplaatszone op het openbaar water waar een vaartuig voor langere tijd mag afmeren."
bronnen:
  - [[Wiki/Bronsamenvattingen/milieu/beleidsnota-stadswater]]
relaties:
  - type: associatie
    bedrijfsobject: "[[Waterobject]]"
    richting: bidirectioneel
    kardinaliteit: ""
    beschrijving: Ligplaats bevindt zich in een waterobject/vaarweg
bedrijfsprocessen: [Ligplaatsvergunningverlening, Havenbeheer, Toezicht en handhaving stadswater]
bedrijfsfuncties: [Beheer openbare ruimte, Havenbeheer]
---

## BO-criteria toetsing

| Criterium | Van toepassing? | Toelichting |
|---|---|---|
| Heeft betekenis binnen het domein | ✅ | Centraal begrip in havenbeheer en stadswatersbeleid; gereguleerd via Havenverordening en Havenatlas |
| Is herkenbaar voor domeinexperts | ✅ | Standaardbegrip in havenbeheer, vergunningverlening en handhaving |
| Heeft een eigen bestaan binnen het domein | ✅ | Elke ligplaats heeft een locatie in een ligplaatszone, een vergunninghouder en een type vaartuig |
| Kan in meervoud bestaan | ✅ | 482 recreatieve ligplaatsvergunningen en 37 commerciële ligplaatsvergunningen in Utrecht |
| Heeft een eigen levenscyclus | ✅ | Aanwijzing → vergunningverlening → in gebruik → toezicht → eventueel intrekking |
| Heeft relaties met andere concepten | ✅ | [[Waterobject]] |

Score: 6/6.

## Beschrijving

De gemeente Utrecht beheert ligplaatsen via de Havenverordening en Havenatlas. Er zijn 482 ligplaatsvergunningen uitgegeven voor recreatieve vaartuigen (maximaal bereikt). Daarvan zijn 337 (70%) voor emissievrije boten. Nieuwe vergunningen worden alleen aan emissievrije vaartuigen uitgegeven.

Daarnaast hebben 37 commerciële vaartuigen (passagiersschepen, rondvaartboten) een ligplaatsvergunning. De gemeente beheert ook passantenligplaatsen, 8 openbare op-en-afstapplaatsen en 3 laad-en-losplekken.

## Procesbron

Bron: [[Wiki/Bronsamenvattingen/milieu/beleidsnota-stadswater|Beleidsnota Stadswater]]

> De gemeente reguleert ligplaatsen via de Havenverordening en Havenatlas. Het maximale aantal recreatieve ligplaatsvergunningen (482) is bereikt; nieuwe vergunningen worden uitsluitend aan emissievrije vaartuigen verstrekt.

## Relaties

| Relatie | Bedrijfsobject | Richting | Bron |
|---|---|---|---|
| associatie | [[Waterobject]] | bidirectioneel | Beleidsbron |

## Bedrijfsprocessen

- **Ligplaatsvergunningverlening**: verlening, wijziging en intrekking van ligplaatsvergunningen voor recreatieve en commerciële vaartuigen
- **Havenbeheer**: beheer van ligplaatszones, op-en-afstapplaatsen en laad-en-losplekken
- **Toezicht en handhaving stadswater**: controle op naleving van ligplaatsregels en Havenverordening

## Terugmelding GGM

> **Ligplaats** — Aangewezen plek in een ligplaatszone op het openbaar water waar een vaartuig voor langere tijd mag afmeren. Het GGM kent geen entiteit voor ligplaatsen in de context van havenbeheer. Het concept is relevant voor gemeentelijk waterbeheer met eigen processen voor vergunningverlening, havenbeheer en handhaving. Zie [[Wiki/Analyses/ggm-terugmeldingen]].
