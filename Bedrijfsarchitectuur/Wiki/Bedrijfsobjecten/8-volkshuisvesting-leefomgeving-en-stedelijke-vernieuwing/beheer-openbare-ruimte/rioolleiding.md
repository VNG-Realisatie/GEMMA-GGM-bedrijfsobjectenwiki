---
type: element
naam: Rioolleiding
onderwerp: [Beheer Openbare Ruimte, Milieu]
archimate_type: business-object
grondslag: ggm-afgeleid

# GGM-velden — geen directe entiteit; afgeleid via generalisatie van GGM-entiteit Leiding
ggm_entiteit:
ggm_guid:
ggm_uml_type:
ggm_beleidsdomein:
ggm_taakveld:
ggm_diagram: []
ggm_diagram_ids: []
ggm_definitie:
ggm_toelichting:
ggm_synoniemen:
ggm_herkomst:

ggm_gemma_naam:
ggm_gemma_guid:
ggm_gemma_definitie:
ggm_gemma_toelichting:
ggm_gemma_synoniemen:
ggm_gemma_type:
ggm_gemma_url:
ggm_gemma_bron:
ggm_gemma_alternate_name:

ggm_duplicaat_entiteiten: []

analyse_ggm_dekking: |
  Dit BO heeft geen directe GGM-entiteit; het is een specialisatie van GGM-entiteit **Leiding**, vastgelegd als generalisatie-relatie naar [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/leiding|Leiding]].
bo_definitie: "Buisinfrastructuur voor transport van afval- en/of hemelwater in het gemeentelijk rioleringssysteem."
bo_toelichting:
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/leiding|Leiding]]"
    richting: naar-dit-BO
    kardinaliteit:
    beschrijving: "Rioolleiding is een specialisatie van Leiding"
  - type: associatie
    bedrijfsobject: "[[Put]]"
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

## Generalisatie

Rioolleiding heeft geen eigen GGM-entiteit. Het is een specialisatie van GGM-entiteit **Leiding** (Beheer Openbare Ruimte, Model IMBOR) — zie [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/leiding|Leiding]] voor de GGM-bron en matchsterkte. GGM Leiding is breder (alle leidingtypen: riool, gas, water, elektriciteit); de gemeentelijke praktijk is uitsluitend riolering — andere leidingtypen liggen bij nutsbedrijven.

## BO-definitie

De GGM-definitie wijkt inhoudelijk af van het gemeentelijke gebruik van dit begrip. De BO-definitie is gebaseerd op de bronnen.

## Relaties

| Gerelateerd BO | Relatie | Richting | Toelichting |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/leiding\|Leiding]] | generalisatie | naar-dit-BO | Rioolleiding is een specialisatie van Leiding |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/put\|Put]] | sluit aan op | bidirectioneel | Verticale constructie voor inspectie en onderhoud |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/gemaal\|Gemaal]] | wordt bemalen door | naar-dit-BO | Gemaal pompt water uit leiding |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/kolk\|Kolk]] | ontvangt water van | naar-dit-BO | Hemelwater via straatkolk |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioleringsgebied\|Rioleringsgebied]] | behoort tot | naar-dit-BO | Administratief beheersgebied |
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/overstortconstructie\|Overstortconstructie]] | loost via | naar-dit-BO | Bij zware neerslag naar oppervlaktewater |

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/gwr-twenterand-2024-2028]]
