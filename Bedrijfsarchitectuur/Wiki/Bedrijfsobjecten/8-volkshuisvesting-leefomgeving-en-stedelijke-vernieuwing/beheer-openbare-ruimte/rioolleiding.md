---
type: bedrijfsobject
naam: Rioolleiding
onderwerp: [Beheer Openbare Ruimte, Milieu]
archimate_type: business-object
grondslag: ggm-entiteit

ggm_entiteit: Leiding
ggm_guid: "EAID_4223240C_8786_4D44_889E_9F54BA39A83"
ggm_uml_type: Class
ggm_beleidsdomein: Beheer Openbare Ruimte
ggm_taakveld: "8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing"
ggm_diagram: [Hoofdobjecten IMBOR en Geo-object]
ggm_diagram_ids: ["EAID_E3EBD7A0_35C4_4bf4_BD01_6D97AD0B8BF3"]
ggm_definitie: "Een geheel van geleiders welke voorzien zijn van één ommanteling en bestemd is voor transport van materie"
ggm_toelichting: ""
ggm_synoniemen: ""
ggm_herkomst: ""

ggm_gemma_naam: Leiding
ggm_gemma_guid: "b2bdb817-4007-4c1b-ad24-43929884e0eb"
ggm_gemma_definitie: "Een geheel van geleiders welke voorzien zijn van één ommanteling en bestemd is voor transport van materie"
ggm_gemma_toelichting: ""
ggm_gemma_synoniemen: ""
ggm_gemma_type: business-object
ggm_gemma_url: "https://gemmaonline.nl/index.php/GEMMA/id-b2bdb817-4007-4c1b-ad24-43929884e0eb"
ggm_gemma_bron: ""
ggm_gemma_alternate_name: ""

ggm_duplicaat_entiteiten: []

bo_definitie: "Buisinfrastructuur voor transport van afval- en/of hemelwater in het gemeentelijk rioleringssysteem."
bo_relaties:
  - type: associatie
    bedrijfsobject: "[[Rioolput]]"
    richting: bidirectioneel
    kardinaliteit: "1..*"
    beschrijving: "Rioolleiding sluit aan op putten voor inspectie en onderhoud"
  - type: associatie
    bedrijfsobject: "[[Gemaal]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Gemaal pompt water uit rioolleiding"
  - type: associatie
    bedrijfsobject: "[[Kolk]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Kolk voert hemelwater af naar rioolleiding"
  - type: associatie
    bedrijfsobject: "[[Rioleringsgebied]]"
    richting: naar-dit-BO
    kardinaliteit: "1"
    beschrijving: "Rioolleiding behoort tot een rioleringsgebied"
  - type: associatie
    bedrijfsobject: "[[Overstortconstructie]]"
    richting: naar-dit-BO
    kardinaliteit: "0..*"
    beschrijving: "Overstort loost vanuit gemengde rioolleiding"
bedrijfsprocessen: [rioleringsbeheer, klimaatadaptatie, vervanging infrastructuur]
bedrijfsfuncties: [waterbeheer, beheer openbare ruimte]
---

## BO-criteria toetsing

| Criterium | Score | Toelichting |
|---|---|---|
| Herkenbaarheid | ✅ | Fysiek buizennetwerk, herkenbaar als rioolleiding |
| Meervoud | ✅ | ~395.000 meter in Twenterand, honderden km per gemeente |
| Levenscyclus | ✅ | Aanleg → inspectie → reiniging → renovatie → vervanging (40-60 jaar) |
| Relaties | ✅ | Put (verticale aansluiting), Gemaal (aandrijving), Kolk (instroming), Rioleringsgebied (administratief), Overstortconstructie (uitlaat) |
| Attributen | ✅ | GGM: 13 attributen (materiaal, diameter, diepte, lengte, etc.) |
| Registratie | ✅ | Gemeente registreert in beheersysteem (WRIS), inspectie per km |

## Beschrijving

Rioolleiding is de horizontale buisinfrastructuur van het gemeentelijk rioleringssysteem. De gemeente beheert drie typen riolering: gemengd stelsel (afval- en hemelwater gecombineerd), gescheiden stelsel (apart vuilwater- en hemelwaterriool) en drukriolering (transport onder druk via minigemalen, vooral in buitengebied).

De rioolleiding verbindt de verticale componenten (putten, kolken) met de aandrijving (gemalen) en vormt samen met die objecten het fysieke rioolstelsel. Gemeenten inspecteren en reinigen jaarlijks tientallen kilometers leiding. Vervanging vindt plaats over perioden van 40-60 jaar met miljoeneninvesteringen per kern.

## Subtypes

Herkende specialisaties van Rioolleiding. Geen apart BO.

- **Vuilwaterriool** — leiding voor huishoudelijk en bedrijfsafvalwater in gescheiden stelsel
- **Hemelwaterriool** — leiding voor regenwater in gescheiden stelsel
- **Gemengd riool** — leiding voor gecombineerd afval- en hemelwater
- **Persleiding** — leiding met kunstmatig drukverschil, aangedreven door gemaal (~150 km in Utrecht)

## GGM-bron

> "Een geheel van geleiders welke voorzien zijn van één ommanteling en bestemd is voor transport van materie."

- **Entiteit:** Leiding
- **Beleidsdomein:** Beheer Openbare Ruimte (Model IMBOR)
- **Taakveld:** 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Attributen:** afwijkendeDieptelegging, breedte, diameter, diepte, eisVoorzorgsmaatregel, geoNauwkeurigheidXY, hoogte, jaarOnderhoudUitgevoerd, lengte, leverancier, materiaal, themaIMKL, verhoogdRisico
- **Matchsterkte:** exact — GGM Leiding is breder (alle leidingen) maar de gemeentelijke toepassing is primair riolering

## Relaties

| Gerelateerd BO | Relatie | Richting | Toelichting |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioolput\|Rioolput]] | sluit aan op | bidirectioneel | Verticale constructie voor inspectie en onderhoud |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/gemaal\|Gemaal]] | wordt bemalen door | naar-dit-BO | Gemaal pompt water uit leiding |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/kolk\|Kolk]] | ontvangt water van | naar-dit-BO | Hemelwater via straatkolk |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioleringsgebied\|Rioleringsgebied]] | behoort tot | naar-dit-BO | Administratief beheersgebied |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/overstortconstructie\|Overstortconstructie]] | loost via | naar-dit-BO | Bij zware neerslag naar oppervlaktewater |

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/gwr-twenterand-2024-2028]]
