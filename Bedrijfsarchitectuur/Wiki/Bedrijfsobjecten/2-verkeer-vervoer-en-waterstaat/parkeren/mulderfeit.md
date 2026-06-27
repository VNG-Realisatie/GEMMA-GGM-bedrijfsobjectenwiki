---
type: bedrijfsobject
naam: MulderFeit
domein: [mobiliteit]
archimate_type: "business-object"
grondslag: "ggm-entiteit"
ggm_entiteit: "MulderFeit"
ggm_guid: EAID_4EA4D754_FAD7_4caf_8060_342689EC16FE
ggm_uml_type: Class
ggm_beleidsdomein: "Parkeren"
ggm_taakveld: "2 Verkeer, Vervoer en Waterstaat"
ggm_diagram: [Model Parkeren]
ggm_diagram_ids: [EAID_84B6B75B_2B58_455d_B019_C9B1E71717C2]
ggm_definitie: "Een administratieve overtreding met betrekking tot parkeren, zoals bepaald onder de Wet administratiefrechtelijke handhaving verkeersvoorschriften (WAHV), ook wel bekend als de Mulderwet."
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
bo_definitie: "Een administratieve overtreding met betrekking tot parkeren, zoals bepaald onder de Wet administratiefrechtelijke handhaving verkeersvoorschriften (WAHV), ook wel bekend als de Mulderwet."
bo_toelichting: ''
bedrijfsprocessen: [Parkeerbeleid, Parkeerhandhaving]
bedrijfsfuncties: [Parkeerbeleid]
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Voertuig]]"
    richting: "van-dit-BO"
    kardinaliteit: 1..1
    beschrijving: MulderFeit betreft een voertuig
---

# MulderFeit

Administratieve parkeerovertreding onder de Wet Mulder (WAHV).

## BO-criteria toetsing

- ✅ Heeft betekenis binnen het domein — juridische grondslag voor boetes bij foutparkeren buiten fiscaal parkeren
- ✅ Is herkenbaar voor domeinexperts — handhavers onderscheiden Mulder-feiten expliciet van naheffingen
- ✅ Heeft een eigen bestaan binnen het domein — overtreding met eigen feitcode, boetebedrag en afhandelingsproces
- ✅ Kan in meervoud bestaan — foutparkeren, parkeerovertreding op gehandicaptenplek, parkeren in voetgangersgebied
- ✅ Heeft een eigen levenscyclus — constatering, bekeuring, bezwaar (bij CJIB), betaling of dwanginvordering
- ✅ Heeft relaties met andere concepten — betreft een voertuig, complementair aan naheffing als handhavingsinstrument

## Beschrijving

Een MulderFeit is een administratieve parkeerovertreding die valt onder de Wet Mulder (WAHV). Dit betreft fout parkeren dat niet via een naheffing parkeerbelasting maar via een bestuurlijke boete wordt afgehandeld. Voorbeelden zijn parkeren op een gehandicaptenplek zonder vergunning of parkeren in een voetgangersgebied.

## GGM-bron

> "Een administratieve overtreding met betrekking tot parkeren, zoals bepaald onder de Wet administratiefrechtelijke handhaving verkeersvoorschriften (WAHV), ook wel bekend als de Mulderwet." — GGM, MulderFeit (EAID_4EA4D754)

**Matchsterkte: exact.** Nog niet opgenomen in GEMMA.

## Relaties

- → [[Wiki/Bedrijfsobjecten/2-verkeer-vervoer-en-waterstaat/parkeren/voertuig|Voertuig]] — MulderFeit betreft een voertuig

## Bronnen

- [[Wiki/Bronsamenvattingen/mobiliteit/kwaliteitsnet-goederenvervoer-2007]]
- [[Wiki/Bronsamenvattingen/mobiliteit/mobiliteitsplan-2040]]
- [[Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-fiets-2021]]
- [[Wiki/Bronsamenvattingen/mobiliteit/beleidsregel-parkeernormen-auto-2021]]
- [[Wiki/Bronsamenvattingen/mobiliteit/module-parkeernormen]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeerhubs]]
- [[Wiki/Bronsamenvattingen/mobiliteit/rapportage-routekaart-parkeerhubs]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-fietsparkeren]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-parkeren-openbare-ruimte]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitwerking-toegankelijkheid]]
- [[Wiki/Bronsamenvattingen/mobiliteit/parkeervisie]]
- [[Wiki/Bronsamenvattingen/mobiliteit/uitvoeringsprogramma-betaald-parkeren]]
