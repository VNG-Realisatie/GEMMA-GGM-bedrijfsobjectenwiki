---
type: element
naam: Leiding
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

analyse_ggm_dekking: |
  Dit BO heeft de GGM-entiteit **Leiding** als directe tegenhanger. De gemeentelijke praktijkscope is beperkt tot de specialisatie Rioolleiding.
bo_definitie: "Een geheel van geleiders voorzien van één ommanteling, bestemd voor transport van materie."
bo_toelichting: "GGM Leiding omvat alle typen leidingen (riool, gas, water, elektriciteit). Gas-, water- en elektriciteitsleidingen liggen in de praktijk bij nutsbedrijven, niet bij de gemeente. De gemeentelijke bronnen beschrijven uitsluitend rioolleidingen — zie specialisatie [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioolleiding|Rioolleiding]]."
bo_relaties:
  - type: generalisatie
    bedrijfsobject: "[[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioolleiding|Rioolleiding]]"
    richting: van-dit-BO
    kardinaliteit: ""
    beschrijving: "Rioolleiding is een specialisatie van Leiding"
bedrijfsprocessen: []
bedrijfsfuncties: [beheer openbare ruimte]
---

## BO-criteria toetsing

| Criterium | Score | Toelichting |
|---|---|---|
| Herkenbaarheid | ✅ | Generiek IMBOR-begrip voor alle typen leidingen |
| Meervoud | ✅ | Meerdere typen leidingen denkbaar (riool, gas, water, elektriciteit) |
| Levenscyclus | ✅ | Aanleg → inspectie → onderhoud → vervanging |
| Relaties | ✅ | Specialisatie Rioolleiding |
| Attributen | ✅ | GGM: 13 attributen (materiaal, diameter, diepte, lengte, etc.) |
| Registratie | ✅ | Gemeente registreert leidingen (voor zover eigen beheer) in beheersysteem |

**Score: 6/6**, maar in de gemeentelijke praktijk is dit BO uitsluitend gevuld via de specialisatie Rioolleiding.

## Beschrijving

Leiding is het GGM/IMBOR-containerbegrip voor buisinfrastructuur: een geheel van geleiders met één ommanteling, bestemd voor transport van materie. Dit omvat in potentie riolering, gasleidingen, waterleidingen en elektriciteitskabels. De gemeentelijke bronnen beschrijven uitsluitend het beheer van **rioolleidingen** — andere leidingtypen liggen doorgaans bij nutsbedrijven (Stedin, Vitens e.d.), niet bij de gemeente.

## Specialisaties

| Specialisatie | Omschrijving | Eigen pagina |
|---|---|---|
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioolleiding\|Rioolleiding]] | Buisinfrastructuur voor transport van afval- en/of hemelwater in het gemeentelijk rioleringssysteem | Ja — voldoet zelfstandig aan de 6 BO-criteria (~395.000 meter, eigen subtypes, eigen relaties) |

Andere denkbare leidingtypen (gas, water, elektriciteit) zijn niet in gemeentelijk beheer en hebben geen BO in deze wiki.

## GGM-bron

> "Een geheel van geleiders welke voorzien zijn van één ommanteling en bestemd is voor transport van materie."

- **Entiteit:** Leiding
- **Beleidsdomein:** Beheer Openbare Ruimte (Model IMBOR)
- **Taakveld:** 8 Volkshuisvesting, Leefomgeving en Stedelijke Vernieuwing
- **Attributen:** afwijkendeDieptelegging, breedte, diameter, diepte, eisVoorzorgsmaatregel, geoNauwkeurigheidXY, hoogte, jaarOnderhoudUitgevoerd, lengte, leverancier, materiaal, themaIMKL, verhoogdRisico
- **Matchsterkte:** exact — dit BO is de GGM-entiteit Leiding zelf; de gemeentelijke praktijkscope is beperkt tot de specialisatie Rioolleiding

## Relaties

| Gerelateerd BO | Relatie | Richting | Toelichting |
|---|---|---|---|
| [[Wiki/Bedrijfsobjecten/8-volkshuisvesting-leefomgeving-en-stedelijke-vernieuwing/beheer-openbare-ruimte/rioolleiding\|Rioolleiding]] | generalisatie | van-dit-BO | Rioolleiding is een specialisatie van Leiding |

## Bronnen

- [[Wiki/Bronsamenvattingen/Beheer Openbare Ruimte/gwr-twenterand-2024-2028]]
