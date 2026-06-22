---
type: bedrijfsobject
naam: Materiaalpasspoort
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
gemma_definitie: "Digitale vastlegging van de materialen in een gebouw of object in de openbare ruimte."
bedrijfsprocessen: [Circulair bouwen, Materiaalmatch, Aanbesteding]
bedrijfsfuncties: [Vastgoedbeheer, Circulaire economie]
bronnen: [Wiki/Bronsamenvattingen/Milieu/visie-utrecht-circulair-2050]
relaties:
  - type: associatie
    bedrijfsobject: "[[Grondstoffendepot]]"
    richting: "van-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: informeert over beschikbare materialen
---

> **ter discussie** — Type is "instrument": een digitaal registratie-instrument in plaats van een fysiek object. Het team moet beoordelen of dit een BO is.

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Maakt circulair hergebruik van materialen mogelijk |
| Herkenbaar voor domeinexperts | ✅ Steeds gangbaarder als standaard in circulair bouwen |
| Heeft eigen bestaan | ✅ Zelfstandig digitaal document per gebouw/object |
| Kan in meervoud bestaan | ✅ Per gebouw of object in de openbare ruimte |
| Heeft eigen levenscyclus | ✅ Aanmaak → bijwerken → gebruik bij sloop/renovatie |
| Heeft relaties met andere concepten | ✅ Grondstoffendepot, aanbestedingen, gebouwen |

**5/6 criteria van toepassing.** Kanttekening: kan worden gezien als eigenschap/attribuut van een gebouw in plaats van een zelfstandig object.

## Beschrijving

Een materiaalpasspoort is een digitale documentatie die vastlegt welke materialen zijn gebruikt in gebouwen en objecten in de openbare ruimte. Het maakt planmatig matchen mogelijk van beschikbare materialen aan nieuwe projecten. Wordt steeds vaker vereist in aanbestedingen. Onderdeel van het Het Nieuwe Normaal-raamwerk. Draagt bij aan MKI-berekeningen en effectmonitoring.

> "Data over materialen in gebouwen en de openbare ruimte is vastgelegd in materiaalpaspoorten." (bron: [[Wiki/Bronsamenvattingen/Milieu/visie-utrecht-circulair-2050|Visie Utrecht Circulair 2050]])

## Procesbron

Het materiaalpasspoort ontstaat in het proces van circulair bouwen en aanbesteden. Het is een cross-domein concept dat Milieu, Bouw en Beheer openbare ruimte raakt. Niet gemodelleerd in het GGM.

## Relaties

- **[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/grondstoffendepot|Grondstoffendepot]]** — het paspoort informeert over beschikbare materialen voor het depot

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor materiaalpasspoorten. Dit is een cross-domein concept (Milieu/Bouw/Beheer openbare ruimte) dat structureel buiten het huidige GGM valt. Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Bedrijfsprocessen

- Circulair bouwen
- Materiaalmatch
- Aanbesteding

## Bedrijfsfuncties

- Vastgoedbeheer
- Circulaire economie
