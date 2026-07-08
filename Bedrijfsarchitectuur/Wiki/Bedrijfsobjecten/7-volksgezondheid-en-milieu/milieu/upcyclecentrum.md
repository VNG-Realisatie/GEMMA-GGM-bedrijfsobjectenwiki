---
type: element
naam: Upcyclecentrum
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
bo_definitie: "Voorziening voor inname, reparatie en hoogwaardig hergebruik van grof huishoudelijk afval."
bo_toelichting: ''
bedrijfsprocessen: [Upcycling, Hergebruik goederen, Educatie circulaire economie]
bedrijfsfuncties: [Afvalbeheer, Circulaire economie]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Milieustraat]]"
    richting: "van-dit-BO"
    kardinaliteit: 0..1
    beschrijving: nabij afvalscheidingsstation
  - type: associatie
    bedrijfsobject: "[[Grondstofstroom]]"
    richting: "naar-dit-BO"
    kardinaliteit: "0..*"
    beschrijving: verwerkt grondstofstromen
---

## BO-criteria toetsing

| Criterium | Van toepassing? |
|---|---|
| Heeft betekenis binnen het domein | ✅ Circulaire hergebruikvoorziening, raakvlak afvalbeheer en circulaire economie |
| Herkenbaar voor domeinexperts | ✅ Herkenbaar als nieuw type voorziening in circulair beleid |
| Heeft eigen bestaan | ✅ Zelfstandige faciliteit, onderscheiden van milieustraat |
| Kan in meervoud bestaan | ✅ Twee gepland: Tractieweg en Lunetten |
| Heeft eigen levenscyclus | ✅ Ontwikkeling → realisatie → exploitatie → eventueel sluiting |
| Heeft relaties met andere concepten | ✅ Milieustraat, grondstofstromen, upcyclepartners |

**6/6 criteria van toepassing.**

## Beschrijving

Een upcyclecentrum is een voorziening nabij afvalscheidingsstations waar inwoners bruikbare huishoudelijke goederen kunnen brengen voor hergebruik. De faciliteit omvat ruimtes voor sortering, reparatie, demontage, workshops en educatie. Upcyclecentra worden ontwikkeld samen met circulaire ondernemers en maatschappelijke partners. Ze vormen de verbindende schakel in een ecosysteem van lokale upcyclepartners: kringlopen, repair cafes, circulaire bouwmarkten. Medewerkers worden opgeleid als upcyclecoaches.

> "We ontwikkelen twee upcyclecentra voor meer en hoogwaardiger hergebruik van grof huishoudelijk afval." (bron: [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-utrecht-circulair-2030|Beleidsnota Utrecht Circulair 2030]], par. B.4.1)

## Procesbron

Het upcyclecentrum ontstaat uit gemeentelijk circulaire-economiebeleid. Dit is een nieuw type voorziening dat de brug slaat tussen afvalbeheer en circulaire economie. Niet gemodelleerd in het GGM.

## Relaties

- **[[Wiki/Bedrijfsobjecten/7-volksgezondheid-en-milieu/milieu/milieustraat|Milieustraat]]** — upcyclecentrum wordt nabij een afvalscheidingsstation gerealiseerd
- **[[Grondstofstroom]]** — het centrum verwerkt grondstofstromen tot herbruikbare producten


## Bronnen

- [[Wiki/Bronsamenvattingen/Milieu/beleidsnota-utrecht-circulair-2030]]

## Terugmelding GGM

GGM-hiaat. Het GGM bevat geen entiteit voor upcyclecentra. Het concept is verwant aan maar onderscheiden van [[Milieustraat]] (die gericht is op afvalscheiding, niet op hergebruik). Zie [[Wiki/Analyses/ggm-terugmeldingen|GGM-terugmeldingen]].

## Bedrijfsprocessen

- Upcycling
- Hergebruik goederen
- Educatie circulaire economie

## Bedrijfsfuncties

- Afvalbeheer
- Circulaire economie
