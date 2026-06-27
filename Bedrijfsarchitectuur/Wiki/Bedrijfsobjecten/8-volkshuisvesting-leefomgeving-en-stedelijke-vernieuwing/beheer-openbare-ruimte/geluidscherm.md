---
type: bedrijfsobject
naam: Geluidscherm
domein: [geluid]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "Geluidsscherm"
ggm_guid: EAID_DD64F32C_3273_4E23_9A61_FCC8EC93977
ggm_uml_type: Class
ggm_beleidsdomein: "Beheer Openbare Ruimte"
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: []
ggm_diagram_ids: [EAPK_C3BA35EC_ABFA_4a7d_BEE9_07FF7563442D]
ggm_definitie: "Een scheiding bedoeld om geluidshinder in de buitenlucht te verminderen. (IMGeo)"
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
bo_definitie: "Een scheiding bedoeld om geluidshinder in de buitenlucht te verminderen. (IMGeo)"
bo_toelichting: ''
bedrijfsprocessen: [beheer openbare ruimte, maatregelenonderzoek, actieplan geluid]
bedrijfsfuncties: [beheer openbare ruimte, milieubeheer]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Geluidbron]]"
    richting: "van-dit-BO"
    kardinaliteit: "*..*"
    beschrijving: Schermt geluid van bronnen af
  - type: associatie
    bedrijfsobject: "[[Geluidgevoelig gebouw]]"
    richting: "naar-dit-BO"
    kardinaliteit: "*..*"
    beschrijving: Beschermt geluidgevoelige gebouwen
  - type: generalisatie
    bedrijfsobject: Scheiding
    richting: "naar-dit-BO"
    kardinaliteit: 1
    beschrijving: Geluidscherm is een specialisatie van Scheiding (GGM)
---

## BO-criteria toetsing

| Criterium | Toepassing |
|---|---|
| Betekenis binnen het domein | Ja — belangrijke overdrachts­maatregel in het geluidbeleid |
| Herkenbaar voor domeinexperts | Ja — fysiek herkenbaar object, opgenomen in IMGeo/IMBOR |
| Eigen bestaan | Ja — een geluidscherm is een zelfstandige constructie |
| Meervoud | Ja — de gemeente beheert meerdere geluidschermen langs wegen en spoor |
| Eigen levenscyclus | Ja — worden geplaatst, onderhouden, gerepareerd en verwijderd |
| Relaties | Ja — met geluidbronnen (wegen, spoor), geluidgevoelige gebouwen, beheergebied |

## Beschrijving

Een geluidscherm is een fysieke constructie langs een weg of spoorlijn die de overdracht van geluid naar de omgeving vermindert. Binnenstedelijk zijn geluidschermen vaak niet toepasbaar vanwege ruimtegebrek; ze worden vooral langs hoofdinfrastructuur en spoorlijnen geplaatst.

De beleidsnota noemt ook de diffractor als nieuwere overdrachts­maatregel die geluid kan afbuigen over woningen heen, toepasbaar bij grotere drukke wegen.

> "Geluidschermen of -wallen zijn alleen mogelijk als er voldoende ruimte is tussen de bron en de woningen (veelal alleen bij het hoofdverkeerswegennet en bij spoorlijnen). In principe worden schermen alleen langs hoofdinfrastructuur geplaatst." (Beleidsnota §1.3)

## GGM-bron

> "Een scheiding bedoeld om geluidshinder in de buitenlucht te verminderen. (IMGeo)" — GGM-entiteit Geluidsscherm

- **Entiteit**: Geluidsscherm
- **Beleidsdomein**: Beheer Openbare Ruimte
- **Taakveld**: 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Model**: IMBOR
- **Attributen**: aantalDeuren, aantalPanelen, type
- **Generalisatie**: Scheiding
- **Matchsterkte**: exact — GGM-entiteit en BO zijn hetzelfde concept

## Relaties

- Schermt af → [[Geluidbron]] (vermindert geluidoverdracht van bronnen)
- Beschermt → [[Geluidgevoelig gebouw]] (vermindert geluidbelasting op gebouwen)
- Generaliseert → Scheiding (GGM-generalisatie)

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/bomenbeleid-utrecht]]
- [[Wiki/Bronsamenvattingen/Milieu/groenstructuurplan-utrecht-2007]]
- [[Wiki/Bronsamenvattingen/Milieu/actualisatie-groenstructuurplan-2017-2030]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/nota-beheer-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kadernota-kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/kwaliteit-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/openbare-ruimte-bing]]
- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/visie-speelruimte-utrecht]]
