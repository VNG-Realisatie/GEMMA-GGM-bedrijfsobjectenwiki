---
type: bedrijfsobject
naam: Laadpaal
domein: [mobiliteit]
archimate_type: "business-object"
grondslag: procesobject
ggm_entiteit: ""
ggm_beleidsdomein: "Mobiliteit"
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
bo_definitie: "Oplaadvoorziening voor elektrische voertuigen in de openbare ruimte."
bo_toelichting: ''
bedrijfsprocessen: [Laadinfrastructuurbeheer, Beheer openbare ruimte, Energietransitie]
bedrijfsfuncties: [Verkeersmanagement, Duurzaamheidsbeleid]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Parkeervlak]]"
    richting: "van-dit-BO"
    kardinaliteit: 1
    beschrijving: laadpaal staat bij parkeervlak
  - type: associatie
    bedrijfsobject: "[[Parkeerzone]]"
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: laadpaal valt binnen parkeerzone
---

## BO-criteria toetsing

- **Betekenis**: essentieel voor verschoning mobiliteit, gemeentelijke verantwoordelijkheid
- **Herkenbaar**: herkenbaar voor bewoners, beleidsmakers en netbeheerders
- **Eigen bestaan**: fysiek object op vaste locatie in de openbare ruimte
- **Meervoud**: duizenden laadpalen in de gemeente
- **Levenscyclus**: aanvraag, plaatsing, onderhoud, vervanging
- **Relaties**: met [[Parkeervlak]], [[Parkeerzone]]

## Beschrijving

Een Laadpaal is een oplaadvoorziening voor elektrische voertuigen, geplaatst in de openbare ruimte bij een parkeervlak. De gemeente creëert een netwerk van laadpalen en ondersteunt particulieren bij oplaadvoorzieningen op eigen terrein. Laadpalen zijn cruciaal voor de verschoning van het wagenpark richting 2030/2040.

## Procesbron

Afgeleid uit [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040|Mobiliteitsplan 2040 - Jouw straat en onze stad gezond, aantrekkelijk en bereikbaar voor iedereen]], §6.4 Auto en §7 Slim parkeren.

## Relaties

- [[Parkeervlak]] (GGM) — laadpaal staat bij een parkeervlak
- [[Parkeerzone]] (GGM) — laadpaal valt binnen een parkeerzone


## Bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]

## Terugmelding GGM

GGM-hiaat. De Laadpaal is een dataobject dat gemeenten registreren: locatie, type (normaal/snellader), vermogen, aansluitstatus, exploitant. Verschilt van GGM Installatie (BOR) in functionele betekenis: het is geen generiek technisch object maar een mobiliteitsvoorziening met eigen beleidskader.
