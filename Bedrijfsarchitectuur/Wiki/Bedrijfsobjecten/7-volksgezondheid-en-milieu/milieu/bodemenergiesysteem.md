---
type: bedrijfsobject
naam: Bodemenergiesysteem
domein: [Milieu]
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
bo_definitie: "Installatie voor warmte-koude opslag (WKO) in de ondergrond, geregistreerd met locatie, capaciteit en diepte."
bedrijfsprocessen: [vergunningverlening bodemenergie, gebiedsgericht grondwaterbeheer, energietransitie]
bedrijfsfuncties: [milieubeheer, vergunningverlening, duurzaamheidsbeleid]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemverontreiniging|Bodemverontreiniging]]"
    richting: bidirectioneel
    kardinaliteit: "0..*"
    beschrijving: "WKO-systemen kunnen verontreinigingen beïnvloeden (positief door afbraak, negatief door verspreiding)"
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Duurzame energieoplossing, raakvlak bodem en energie |
| Herkenbaar voor domeinexperts | ✅ WKO is gangbaar begrip in milieu en energie |
| Heeft eigen bestaan | ✅ Individuele installatie met eigen vergunning |
| Kan in meervoud bestaan | ✅ Tientallen tot honderden per gemeente |
| Heeft eigen levenscyclus | ✅ Vergunning → installatie → exploitatie → buitengebruikstelling |
| Heeft relaties met andere concepten | ✅ Verontreiniging, grondwaterbeheer, vergunning |

**6/6 criteria van toepassing.**

## Beschrijving

Een bodemenergiesysteem (ook: WKO, warmte-koude opslag) is een installatie die grondwater gebruikt voor het verwarmen en koelen van gebouwen. Het systeem pompt grondwater rond tussen een warme en koude bron in de ondergrond. Elk systeem heeft een locatie, capaciteit, diepte en vereist een vergunning.

In het gebiedsplan Utrecht wordt bodemenergie gestimuleerd omdat het rondpompen van grondwater de biologische afbraak van verontreinigingen bevordert. Tegelijk gelden voorwaarden om verspreiding van verontreiniging te voorkomen, zoals maximale boordieptes.

> "Tegelijk willen we dat het grondwater onder de stad gebruikt kan worden voor bijvoorbeeld duurzame bodemenergie om gebouwen mee te verwarmen en koelen." (bron: [[Wiki/Bronsamenvattingen/Milieu/beleid-bodem-grondwater-en-ondergrond|Beleid voor bodem, grondwater en ondergrond]])

## Procesbron

Bodemenergiesystemen worden geregistreerd via het vergunningsproces. De gemeente (of provincie, afhankelijk van capaciteit) is bevoegd gezag. Het systeem raakt zowel het energiebeleid als het grondwaterbeheer.

## Relaties

- **[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/bodemverontreiniging|Bodemverontreiniging]]** — WKO kan verontreinigingen beïnvloeden: rondpompen stimuleert afbraak, maar verspreiding moet worden voorkomen


## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/beleid-bodem-grondwater-en-ondergrond]]

## Terugmelding GGM

Het GGM heeft geen entiteit voor bodemenergiesystemen. Dit raakt zowel taakveld 7 (Milieu) als het energiedomein. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].
